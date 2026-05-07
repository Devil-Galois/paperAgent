import argparse
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape
from zipfile import ZIP_DEFLATED, ZipFile


W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CP_NS = "http://schemas.openxmlformats.org/package/2006/metadata/core-properties"
DC_NS = "http://purl.org/dc/elements/1.1/"
DCTERMS_NS = "http://purl.org/dc/terms/"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
VT_NS = "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes"


def read_markdown(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").splitlines()


def paragraph_xml(text: str, style: str | None = None) -> str:
    paragraph_props = []
    run_props = []

    if style:
        paragraph_props.append(f'<w:pStyle w:val="{style}"/>')

    if style == "Title":
        paragraph_props.extend(
            [
                '<w:jc w:val="center"/>',
                '<w:spacing w:before="120" w:after="240"/>',
            ]
        )
        run_props.extend(
            [
                "<w:b/>",
                "<w:bCs/>",
                '<w:sz w:val="36"/>',
                '<w:szCs w:val="36"/>',
                '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>',
            ]
        )
    elif style == "Heading1":
        paragraph_props.extend(
            [
                '<w:jc w:val="left"/>',
                '<w:spacing w:before="240" w:after="120"/>',
                '<w:ind w:firstLine="0"/>',
            ]
        )
        run_props.extend(
            [
                "<w:b/>",
                "<w:bCs/>",
                '<w:sz w:val="32"/>',
                '<w:szCs w:val="32"/>',
                '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>',
            ]
        )
    elif style == "Heading2":
        paragraph_props.extend(
            [
                '<w:jc w:val="left"/>',
                '<w:spacing w:before="180" w:after="80"/>',
                '<w:ind w:firstLine="0"/>',
            ]
        )
        run_props.extend(
            [
                "<w:b/>",
                "<w:bCs/>",
                '<w:sz w:val="28"/>',
                '<w:szCs w:val="28"/>',
                '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>',
            ]
        )
    elif style == "Heading3":
        paragraph_props.extend(
            [
                '<w:jc w:val="left"/>',
                '<w:spacing w:before="120" w:after="60"/>',
                '<w:ind w:firstLine="0"/>',
            ]
        )
        run_props.extend(
            [
                "<w:b/>",
                "<w:bCs/>",
                '<w:sz w:val="26"/>',
                '<w:szCs w:val="26"/>',
                '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>',
            ]
        )
    else:
        paragraph_props.extend(
            [
                '<w:jc w:val="both"/>',
                '<w:spacing w:line="420" w:lineRule="auto" w:after="120"/>',
                '<w:ind w:firstLine="420"/>',
            ]
        )
        run_props.extend(
            [
                '<w:sz w:val="24"/>',
                '<w:szCs w:val="24"/>',
                '<w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="宋体"/>',
            ]
        )

    style_xml = ""
    if paragraph_props:
        style_xml = f"<w:pPr>{''.join(paragraph_props)}</w:pPr>"

    run_props_xml = ""
    if run_props:
        run_props_xml = f"<w:rPr>{''.join(run_props)}</w:rPr>"

    safe_text = escape(text)
    if not safe_text:
        return "<w:p/>"
    return (
        f'<w:p>{style_xml}<w:r>{run_props_xml}<w:t xml:space="preserve">{safe_text}</w:t></w:r></w:p>'
    )


def markdown_to_paragraphs(lines: list[str], title: str | None = None) -> list[str]:
    paragraphs: list[str] = []
    skipped_title_line = False
    if title:
        paragraphs.append(paragraph_xml(title, "Title"))

    buffer: list[str] = []

    def flush_buffer():
        if buffer:
            paragraphs.append(paragraph_xml(" ".join(buffer).strip(), "Normal"))
            buffer.clear()

    for raw_line in lines:
        stripped = raw_line.strip().lstrip("\ufeff")
        if not stripped:
            flush_buffer()
            continue
        if title and not skipped_title_line and stripped.startswith("# "):
            skipped_title_line = True
            continue
        if stripped.startswith("### "):
            flush_buffer()
            paragraphs.append(paragraph_xml(stripped[4:].strip(), "Heading3"))
            continue
        if stripped.startswith("## "):
            flush_buffer()
            paragraphs.append(paragraph_xml(stripped[3:].strip(), "Heading2"))
            continue
        if stripped.startswith("# "):
            flush_buffer()
            paragraphs.append(paragraph_xml(stripped[2:].strip(), "Heading1"))
            continue
        if stripped.startswith(("- ", "* ")):
            flush_buffer()
            paragraphs.append(paragraph_xml(stripped[2:].strip(), "ListBullet"))
            continue
        if len(stripped) > 2 and stripped[0].isdigit() and ". " in stripped[:4]:
            flush_buffer()
            paragraphs.append(paragraph_xml(stripped, "ListNumber"))
            continue
        buffer.append(stripped)

    flush_buffer()
    return paragraphs


def content_types_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
"""


def package_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
"""


def document_rels_xml() -> str:
    return """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>
"""


def styles_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="{W_NS}">
  <w:style w:type="paragraph" w:default="1" w:styleId="Normal">
    <w:name w:val="Normal"/>
    <w:pPr>
      <w:jc w:val="both"/>
      <w:spacing w:line="420" w:lineRule="auto" w:after="120"/>
      <w:ind w:firstLine="420"/>
    </w:pPr>
    <w:rPr>
      <w:sz w:val="24"/>
      <w:szCs w:val="24"/>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="宋体"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Title">
    <w:name w:val="Title"/>
    <w:qFormat/>
    <w:pPr>
      <w:jc w:val="center"/>
      <w:spacing w:before="120" w:after="240"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="36"/>
      <w:szCs w:val="36"/>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading1">
    <w:name w:val="heading 1"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:before="240" w:after="120"/>
      <w:ind w:firstLine="0"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="32"/>
      <w:szCs w:val="32"/>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading2">
    <w:name w:val="heading 2"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:before="180" w:after="80"/>
      <w:ind w:firstLine="0"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="28"/>
      <w:szCs w:val="28"/>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="Heading3">
    <w:name w:val="heading 3"/>
    <w:basedOn w:val="Normal"/>
    <w:qFormat/>
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:before="120" w:after="60"/>
      <w:ind w:firstLine="0"/>
    </w:pPr>
    <w:rPr>
      <w:b/>
      <w:sz w:val="26"/>
      <w:szCs w:val="26"/>
      <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman" w:eastAsia="黑体"/>
    </w:rPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListBullet">
    <w:name w:val="List Bullet"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:line="360" w:lineRule="auto" w:after="80"/>
      <w:ind w:left="420" w:hanging="210"/>
    </w:pPr>
  </w:style>
  <w:style w:type="paragraph" w:styleId="ListNumber">
    <w:name w:val="List Number"/>
    <w:basedOn w:val="Normal"/>
    <w:pPr>
      <w:jc w:val="left"/>
      <w:spacing w:line="360" w:lineRule="auto" w:after="80"/>
      <w:ind w:left="420" w:hanging="210"/>
    </w:pPr>
  </w:style>
</w:styles>
"""


def document_xml(paragraphs: list[str]) -> str:
    body = "".join(paragraphs)
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="{W_NS}" xmlns:r="{R_NS}">
  <w:body>
    {body}
    <w:sectPr>
      <w:pgSz w:w="11906" w:h="16838"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="708" w:footer="708" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
"""


def core_xml(title: str, author: str = "paperAgent") -> str:
    created = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="{CP_NS}" xmlns:dc="{DC_NS}" xmlns:dcterms="{DCTERMS_NS}" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="{XSI_NS}">
  <dc:title>{escape(title)}</dc:title>
  <dc:creator>{escape(author)}</dc:creator>
  <cp:lastModifiedBy>{escape(author)}</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">{created}</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">{created}</dcterms:modified>
</cp:coreProperties>
"""


def app_xml() -> str:
    return f"""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="{VT_NS}">
  <Application>paperAgent</Application>
</Properties>
"""


def export_docx(input_path: Path, output_path: Path, title: str | None = None):
    lines = read_markdown(input_path)
    if not title:
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("# "):
                title = stripped[2:].strip()
                break
    title = title or input_path.stem
    paragraphs = markdown_to_paragraphs(lines, title=title)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(output_path, "w", ZIP_DEFLATED) as docx:
        docx.writestr("[Content_Types].xml", content_types_xml())
        docx.writestr("_rels/.rels", package_rels_xml())
        docx.writestr("word/document.xml", document_xml(paragraphs))
        docx.writestr("word/styles.xml", styles_xml())
        docx.writestr("word/_rels/document.xml.rels", document_rels_xml())
        docx.writestr("docProps/core.xml", core_xml(title))
        docx.writestr("docProps/app.xml", app_xml())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to the manuscript markdown file.")
    parser.add_argument("--output", required=True, help="Path to the exported docx file.")
    parser.add_argument("--title", help="Optional manuscript title.")
    args = parser.parse_args()
    export_docx(Path(args.input), Path(args.output), args.title)
    print(str(Path(args.output)))


if __name__ == "__main__":
    main()
