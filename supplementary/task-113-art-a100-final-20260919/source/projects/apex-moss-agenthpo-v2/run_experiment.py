"""Orchestrates the full 28h pilot: baseline → evolution → finals → cross → builder0.

Checkpointed: each completed stage writes a marker into results/checkpoints/, so the
script can be re-run after any interruption and will skip finished work.

Usage: python run_experiment.py [--iterations 6]
"""

import argparse
import json
import subprocess
import sys
import threading
from pathlib import Path

from eval import evaluate

HERE = Path(__file__).resolve().parent
CKPT = HERE / "results" / "checkpoints"
FAMILIES = ["bugfix", "tddgen"]


def done(stage: str) -> bool:
    return (CKPT / stage).exists()


def mark(stage: str) -> None:
    CKPT.mkdir(parents=True, exist_ok=True)
    (CKPT / stage).write_text("done")


def official(harness: Path, family: str, split: str, tag: str) -> dict:
    """3-repeat scored evaluation with a stable results path."""
    out = HERE / "results" / "official" / tag
    summary_file = out / "summary.json"
    if summary_file.exists():
        return json.loads(summary_file.read_text())
    s = evaluate(str(harness), str(HERE / "benchmarks" / family / split),
                 repeats=3, concurrency=4, out_dir=str(out))
    return s


def latest_version(family: str) -> Path:
    fam = HERE / "harnesses" / family
    versions = sorted([d for d in fam.iterdir() if d.is_dir() and d.name.startswith("v")])
    return versions[-1]


def smoke() -> None:
    import anthropic
    import config
    config.load_env()
    for model in [config.EXECUTOR_MODEL, config.PROPOSER_MODEL]:
        r = anthropic.Anthropic().messages.create(
            model=model, max_tokens=16,
            messages=[{"role": "user", "content": "reply with exactly: ok"}])
        print(f"smoke {model}: {r.content[0].text.strip()}")


def stage_baseline() -> None:
    for family in FAMILIES:
        for split in ["train", "val"]:
            official(HERE / "harnesses" / family / "v001" / "harness.py",
                     family, split, f"v001-{family}-{split}")


def stage_evolution(iterations: int) -> None:
    def run_family(family: str) -> None:
        subprocess.run([sys.executable, str(HERE / "loop.py"), family,
                        "--iterations", str(iterations)], check=True)

    threads = [threading.Thread(target=run_family, args=(f,)) for f in FAMILIES]
    for t in threads:
        t.start()
    for t in threads:
        t.join()


def stage_finals() -> None:
    for family in FAMILIES:
        v = latest_version(family)
        for split in ["train", "val"]:
            official(v / "harness.py", family, split, f"{family}-{v.name}-{family}-{split}")


def stage_cross() -> None:
    pairs = [("bugfix", "tddgen"), ("tddgen", "bugfix")]
    for own, other in pairs:
        v = latest_version(own)
        official(v / "harness.py", other, "val", f"{own}-{v.name}-{other}-val")


def stage_builder() -> None:
    for family in FAMILIES:
        h = HERE / "harnesses" / family / "builder0" / "harness.py"
        if not h.exists():
            subprocess.run([sys.executable, str(HERE / "builder.py"), family], check=True)
        for split in ["train", "val"]:
            official(h, family, split, f"builder0-{family}-{split}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--iterations", type=int, default=6)
    a = ap.parse_args()

    smoke()
    stages = [
        ("baseline", stage_baseline),
        ("evolution", lambda: stage_evolution(a.iterations)),
        ("finals", stage_finals),
        ("cross", stage_cross),
        ("builder", stage_builder),
    ]
    for name, fn in stages:
        if done(name):
            print(f">>> stage {name}: already done, skipping")
            continue
        print(f"\n>>> stage {name}")
        fn()
        mark(name)
    print("\nAll stages complete. Summaries in results/official/*/summary.json")


if __name__ == "__main__":
    main()
