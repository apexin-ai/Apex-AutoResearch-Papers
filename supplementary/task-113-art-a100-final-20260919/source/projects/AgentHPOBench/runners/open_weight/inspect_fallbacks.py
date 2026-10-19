#!/usr/bin/env python3
import json
import pathlib
import sys


def main() -> None:
    for raw_path in sys.argv[1:]:
        path = pathlib.Path(raw_path)
        result = json.loads(path.read_text())
        print(f"FILE={path}")
        print(f"FALLBACK_COUNT={result.get('fallback_decision_count', 0)}")
        for index, decision in enumerate(result.get("decisions") or [], start=1):
            metadata = decision.get("metadata") or {}
            if metadata.get("fallback") is not True:
                continue
            response = metadata.get("raw_response") or metadata.get("raw_text") or ""
            print(
                json.dumps(
                    {
                        "index": index,
                        "error": metadata.get("error"),
                        "reasoning": decision.get("reasoning"),
                        "new_config": decision.get("new_config"),
                        "raw_response_chars": len(response),
                        "raw_response_head": response[:500],
                        "raw_response_tail": response[-500:],
                    },
                    ensure_ascii=True,
                    indent=2,
                )
            )


if __name__ == "__main__":
    main()
