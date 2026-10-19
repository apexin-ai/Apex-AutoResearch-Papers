#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TASK_CONFIG = ROOT / "configs" / "tasks.json"
REPOSITORY_CONFIG = ROOT / "configs" / "repositories.json"
OVERLAYS = (
    ROOT / "tasks" / "main",
    ROOT / "tasks" / "ablations" / "no_feedback",
    ROOT / "baselines" / "tpe",
    ROOT / "baselines" / "bohb",
)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def main() -> int:
    errors: list[str] = []
    task_items = load_json(TASK_CONFIG)["tasks"]
    task_ids = [item["id"] for item in task_items]
    repository_items = load_json(REPOSITORY_CONFIG)["repositories"]

    if len(task_ids) != 30 or len(set(task_ids)) != 30:
        errors.append(f"expected 30 unique tasks, found {len(task_ids)}")
    if {item["task"] for item in repository_items} != set(task_ids):
        errors.append("repository manifest does not match task manifest")

    for overlay in OVERLAYS:
        found = {
            path.name
            for path in overlay.iterdir()
            if path.is_dir() and not path.name.startswith("__")
        }
        missing = sorted(set(task_ids) - found)
        extra = sorted(found - set(task_ids) - {"seed_shim"})
        if missing:
            errors.append(f"{overlay.relative_to(ROOT)} missing: {', '.join(missing)}")
        if extra:
            errors.append(f"{overlay.relative_to(ROOT)} extra: {', '.join(extra)}")
        for task_id in task_ids:
            baseline = overlay / task_id / "baseline.json"
            if not baseline.is_file():
                errors.append(f"missing {baseline.relative_to(ROOT)}")
                continue
            try:
                load_json(baseline)
            except Exception as exc:
                errors.append(f"invalid {baseline.relative_to(ROOT)}: {exc}")

    print(f"tasks: {len(task_ids)}")
    print(f"ray tasks: {sum(bool(item['ray']) for item in task_items)}")
    print(f"overlays: {len(OVERLAYS)}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("task validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
