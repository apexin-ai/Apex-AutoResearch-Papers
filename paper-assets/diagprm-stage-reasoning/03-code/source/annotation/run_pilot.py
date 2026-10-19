"""Main orchestration for DiagPRM annotation pilot study.

Flow: load trajectories -> dual-judge segmentation -> dual-judge quality assessment
     -> save results -> compute agreement -> print report.

CLI: python -m annotation.run_pilot --dry-run --sample-size 5
"""

import argparse
import json
import random
from pathlib import Path

from .data_loader import load_trajectories
from .stage_segmentation import segment_trajectory, StageLabel
from .quality_assessment import assess_stage
from .compute_agreement import compute_agreement, format_report, save_report


def _generate_mock_data(n: int) -> str:
    """Generate mock JSONL trajectories for dry-run testing."""
    rng = random.Random(42)
    actions = {
        "localize": [
            "Let me search for the relevant file using grep.",
            "Looking at the stack trace, the error originates from src/utils.py line 42.",
            "Let me read the source code of the failing module.",
            "Searching for references to the failing function.",
        ],
        "diagnose": [
            "The root cause appears to be an off-by-one error in the loop boundary.",
            "This fails because the input validation doesn't handle None values.",
            "The issue is that the cache isn't invalidated when the config changes.",
            "Analyzing why the test expects a different return type.",
        ],
        "patch": [
            "I'll fix this by adding a boundary check before the loop.",
            "Here's the patch:\n- if x > 0:\n+ if x >= 0:",
            "Adding None check in the validator function.",
            "Updating the return type to match the interface.",
        ],
        "other": [
            "Setting up the test environment.",
            "Running the test suite to verify.",
        ],
    }

    lines = []
    for i in range(n):
        steps = []
        n_steps = rng.randint(6, 12)
        for j in range(n_steps):
            progress = j / (n_steps - 1)
            if progress < 0.3:
                stage = rng.choices(["localize", "other"], [0.8, 0.2])[0]
            elif progress < 0.6:
                stage = rng.choices(["localize", "diagnose", "other"], [0.2, 0.7, 0.1])[0]
            else:
                stage = rng.choices(["diagnose", "patch", "other"], [0.2, 0.7, 0.1])[0]
            content = rng.choice(actions[stage])
            role = "assistant" if j % 2 == 0 else "tool"
            steps.append({"role": role, "content": content})

        record = {
            "instance_id": f"test__issue_{i + 1}",
            "messages": steps,
            "resolved": rng.random() > 0.4,
            "model_name_or_path": "mock-model",
        }
        lines.append(json.dumps(record))
    return "\n".join(lines)


def run_pilot(args: argparse.Namespace) -> None:
    data_path = Path(args.data_path)

    # Auto-generate mock data if file doesn't exist in dry-run mode
    if args.dry_run and not data_path.exists():
        print(f"[dry-run] Generating mock data -> {data_path}")
        data_path.parent.mkdir(parents=True, exist_ok=True)
        data_path.write_text(
            _generate_mock_data(max(args.sample_size, 10)), encoding="utf-8"
        )

    # 1. Load
    print(f"Loading trajectories from {data_path} ...")
    trajectories = load_trajectories(str(data_path), sample_size=args.sample_size)
    print(f"Loaded {len(trajectories)} trajectories")

    judges = [j.strip() for j in args.judges.split(",")]
    print(f"Judges: {judges}")

    # 2. Stage segmentation
    segmentation_results: dict[str, dict] = {}
    print("\n--- Stage Segmentation ---")
    for traj in trajectories:
        segmentation_results[traj.instance_id] = {}
        for judge in judges:
            labels = segment_trajectory(traj, judge=judge, dry_run=args.dry_run)
            segmentation_results[traj.instance_id][judge] = [
                {"step_index": l.step_index, "stage": l.stage, "reasoning": l.reasoning}
                for l in labels
            ]
        print(f"  {traj.instance_id}: {len(traj.steps)} steps segmented")

    # 3. Quality assessment
    quality_results: dict[str, dict] = {}
    assessed_stages = ["localize", "diagnose", "patch"]
    print("\n--- Quality Assessment ---")
    for traj in trajectories:
        quality_results[traj.instance_id] = {}
        # Use first judge's segmentation as the canonical split for both assessments
        first_labels_raw = segmentation_results[traj.instance_id][judges[0]]
        stage_labels = [
            StageLabel(l["step_index"], l["stage"], l["reasoning"])
            for l in first_labels_raw
        ]
        for judge in judges:
            quality_results[traj.instance_id][judge] = {}
            for stage in assessed_stages:
                if any(l.stage == stage for l in stage_labels):
                    ql = assess_stage(
                        traj, stage_labels, stage, judge=judge, dry_run=args.dry_run
                    )
                    quality_results[traj.instance_id][judge][stage] = {
                        "assessment": ql.assessment,
                        "reasoning": ql.reasoning,
                    }
        print(f"  {traj.instance_id}: assessed")

    # 4. Save results
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    seg_path = output_dir / "segmentation_results.json"
    qual_path = output_dir / "quality_results.json"
    with open(seg_path, "w", encoding="utf-8") as f:
        json.dump(segmentation_results, f, indent=2, ensure_ascii=False)
    with open(qual_path, "w", encoding="utf-8") as f:
        json.dump(quality_results, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to {output_dir}/")

    # 5. Agreement
    if len(judges) == 2:
        report = compute_agreement(segmentation_results, quality_results, judges)
        print(f"\n{format_report(report)}")
        save_report(report, str(output_dir / "agreement_report.json"))
    else:
        print(f"\nSkipping agreement (need 2 judges, got {len(judges)})")

    print("\nDone.")


def main():
    parser = argparse.ArgumentParser(description="DiagPRM Annotation Pilot Study")
    parser.add_argument(
        "--data-path", default="data/trajectories.jsonl",
        help="Path to trajectory JSONL file",
    )
    parser.add_argument(
        "--sample-size", type=int, default=50,
        help="Number of trajectories to sample",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Use mock data instead of calling APIs",
    )
    parser.add_argument(
        "--output-dir", default="results/",
        help="Output directory for results",
    )
    parser.add_argument(
        "--judges", default="claude,gpt4o",
        help="Comma-separated list of judges",
    )
    args = parser.parse_args()
    run_pilot(args)


if __name__ == "__main__":
    main()
