import argparse
import json
import re


def slug_terms(topic: str):
    parts = [p.strip() for p in re.split(r"[,:;/()\-]+", topic) if p.strip()]
    return [p for p in parts if len(p) > 1]


def merge_parts(*parts: str):
    return " ".join(part.strip() for part in parts if part and part.strip())


def split_csv(raw: str | None):
    if not raw:
        return []
    return [part.strip() for part in raw.split(",") if part.strip()]


def build_queries(
    topic: str,
    focus: str | None = None,
    method: str | None = None,
    application: str | None = None,
    must_include: list[str] | None = None,
    exclude: list[str] | None = None,
):
    terms = slug_terms(topic)
    must_include = must_include or []
    exclude = exclude or []
    base = merge_parts(topic, focus, method, application, " ".join(must_include))
    quoted = f"\"{base or topic}\""
    exclusion_suffix = ""
    if exclude:
        exclusion_suffix = " " + " ".join(f'-"{item}"' for item in exclude)
    core = [
        (base or topic) + exclusion_suffix,
        quoted,
        merge_parts(base or topic, "survey") + exclusion_suffix,
        merge_parts(base or topic, "review") + exclusion_suffix,
        merge_parts(base or topic, "benchmark") + exclusion_suffix,
    ]
    frontier = [
        merge_parts(base or topic, "recent advances") + exclusion_suffix,
        merge_parts(base or topic, "state of the art") + exclusion_suffix,
        merge_parts(base or topic, "arXiv") + exclusion_suffix,
    ]
    scholar = [f"https://scholar.google.com/scholar?q={q.replace(' ', '+')}" for q in core[:3]]
    arxiv = [f"https://arxiv.org/search/?query={q.replace(' ', '+')}&searchtype=all" for q in frontier[:2]]
    return {
        "topic": topic,
        "focus": focus,
        "method": method,
        "application": application,
        "must_include": must_include,
        "exclude": exclude,
        "terms": terms,
        "core_queries": core,
        "frontier_queries": frontier,
        "scholar_urls": scholar,
        "arxiv_urls": arxiv,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--topic", required=True)
    parser.add_argument("--focus")
    parser.add_argument("--method")
    parser.add_argument("--application")
    parser.add_argument("--must-include", help="Comma-separated required keywords.")
    parser.add_argument("--exclude", help="Comma-separated exclusion keywords.")
    args = parser.parse_args()
    print(
        json.dumps(
            build_queries(
                args.topic,
                focus=args.focus,
                method=args.method,
                application=args.application,
                must_include=split_csv(args.must_include),
                exclude=split_csv(args.exclude),
            ),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
