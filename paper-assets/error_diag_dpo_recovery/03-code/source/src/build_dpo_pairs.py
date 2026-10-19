"""Build DPO preference pairs from classified failures and expert trajectories.

Fix [2026-05-12]: Use true divergence point instead of LLM-reported failure_step.
Old logic used failure_step as split point, but expert and failure trajectories
may already differ before that step → prompt-chosen state inconsistency.
New logic compares action sequences step-by-step to find the real divergence.

For each classified failure:
  1. Match expert trajectory by game_file
  2. Compare actions step-by-step to find divergence point
  3. Shared prefix = prompt, expert continuation = chosen, failure continuation = rejected

Input:
  - classified_errors.jsonl (error_type, failure_step, conversations)
  - alfworld_sft.json (expert trajectories)
  - (optional) trajectory_dir with failure JSONL files
  - (optional) trajectory JSONL files directly (--trajectory_input, v8 format)

Output per line:
  {prompt, chosen, rejected, error_type, gamma_e, correction_span,
   task_id, task_type, game_file, failure_step, divergence_step, d, metadata}

Usage:
  # Discrete gamma (original):
  python src/build_dpo_pairs.py \
    --classified outputs/classify_compare_with_hint_20.jsonl \
    --expert data/alfworld_sft.json \
    --output data/dpo_pairs_v2.jsonl \
    --gamma action=0.85,verification=0.92,planning=0.97

  # Continuous gamma (ETADN):
  python src/build_dpo_pairs.py \
    --trajectory_input "outputs/traj_v8_*.jsonl" \
    --expert data/alfworld_sft.json \
    --output data/dpo_pairs_continuous.jsonl \
    --gamma_mode continuous --gamma_min 0.85 --gamma_max 1.0

Dependencies: (stdlib only)
"""

import argparse
import glob as glob_mod
import json
import logging
import statistics
from collections import Counter, defaultdict
from pathlib import Path

logger = logging.getLogger("build_dpo")

DEFAULT_GAMMA_MAP = {
    "action": 0.85,
    "verification": 0.92,
    "planning": 1.0,
}


def parse_gamma_arg(s: str) -> dict[str, float]:
    """Parse 'action=0.85,verification=0.92,planning=0.97' → dict."""
    gamma_map = dict(DEFAULT_GAMMA_MAP)
    for item in s.split(","):
        k, v = item.strip().split("=")
        gamma_map[k.strip()] = float(v.strip())
    return gamma_map


# ---------------------------------------------------------------------------
# Game file normalization
# ---------------------------------------------------------------------------

def normalize_game_file(game_file: str) -> str:
    """Extract <task_dir>/<trial_dir> as matching key.

    Expert:     data/json_2.1.1/train/<task>/<trial>
    Trajectory: /root/.../json_2.1.1/train/<task>/<trial>/game.tw-pddl
    """
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


# ---------------------------------------------------------------------------
# Message helpers
# ---------------------------------------------------------------------------

def _role(msg: dict) -> str:
    """Get role from either format."""
    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")


def _content(msg: dict) -> str:
    """Get content from either format."""
    return msg.get("content") or msg.get("value", "")


def msg_to_standard(msg: dict) -> dict:
    return {"role": _role(msg), "content": _content(msg)}


# ---------------------------------------------------------------------------
# Step extraction
# ---------------------------------------------------------------------------

def find_task_start(conversations: list) -> int:
    """Index of first action step after the actual task description.

    Handles both expert (no ICL) and trajectory (with ICL prefix) formats by
    finding the LAST 'Your task is to:' user message, then the first action after it.
    """
    task_desc_idx = -1
    for i, msg in enumerate(conversations):
        if _role(msg) in ("user", "human") and "Your task is to:" in _content(msg):
            task_desc_idx = i

    search_from = task_desc_idx + 1 if task_desc_idx >= 0 else 0
    for i in range(search_from, len(conversations)):
        if _role(conversations[i]) in ("assistant", "gpt") and "Action:" in _content(conversations[i]):
            return i

    return len(conversations)


def extract_steps(conversations: list, start_idx: int) -> list[tuple[dict, dict | None]]:
    """Extract (action_msg, obs_msg|None) pairs from start_idx onward."""
    steps = []
    i = start_idx
    while i < len(conversations):
        if _role(conversations[i]) in ("assistant", "gpt"):
            action = conversations[i]
            obs = None
            if i + 1 < len(conversations) and _role(conversations[i + 1]) in ("user", "human"):
                obs = conversations[i + 1]
                i += 2
            else:
                i += 1
            steps.append((action, obs))
        else:
            i += 1
    return steps


def count_expert_action_steps(expert: dict) -> int:
    return sum(
        1
        for m in expert["conversations"]
        if m["from"] == "gpt" and "Action:" in m.get("value", "")
    )


# ---------------------------------------------------------------------------
# Action comparison
# ---------------------------------------------------------------------------

def extract_action_text(content: str) -> str:
    """Extract normalized 'Action: ...' line from a step message.

    ALFWorld actions follow "Thought: ...\\nAction: <action>". We extract
    the action part and normalize whitespace + case for robust comparison.
    """
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("action:"):
            return " ".join(stripped[len("action:"):].split()).lower()
    return " ".join(content.split()).lower()


def find_divergence_point(
    expert_steps: list[tuple[dict, dict | None]],
    fail_steps: list[tuple[dict, dict | None]],
) -> int:
    """Find the first step where expert and failure trajectories take different actions.

    Compares normalized action strings step-by-step. In ALFWorld, same game_file
    + same actions → same observations, so action match guarantees state match.

    Args:
        expert_steps: List of (action_msg, obs_msg|None) from expert trajectory.
        fail_steps: List of (action_msg, obs_msg|None) from failure trajectory.

    Returns:
        0-based index of the first differing step. If one is a prefix of the
        other, returns the shorter length (no shared step beyond that).
    """
    min_len = min(len(expert_steps), len(fail_steps))
    for i in range(min_len):
        expert_action = extract_action_text(_content(expert_steps[i][0]))
        fail_action = extract_action_text(_content(fail_steps[i][0]))
        if expert_action != fail_action:
            return i
    return min_len


# ---------------------------------------------------------------------------
# Pair construction
# ---------------------------------------------------------------------------

def build_pair(
    rec: dict,
    expert: dict,
    gamma_map: dict[str, float] | None = None,
    gamma_mode: str = "error_type",
    gamma_min: float = 0.85,
    gamma_max: float = 1.0,
) -> dict | None:
    """Build one DPO pair using true divergence point between expert and failure."""
    if gamma_map is None:
        gamma_map = DEFAULT_GAMMA_MAP

    fail_convs = rec["conversations"]
    expert_convs = expert["conversations"]

    fail_start = find_task_start(fail_convs)
    expert_start = find_task_start(expert_convs)

    fail_steps = extract_steps(fail_convs, fail_start)
    expert_steps = extract_steps(expert_convs, expert_start)

    if not fail_steps or not expert_steps:
        return None

    divergence = find_divergence_point(expert_steps, fail_steps)

    if divergence >= len(expert_steps) or divergence >= len(fail_steps):
        logger.debug(
            "task_id=%s: no divergence found (expert=%d, fail=%d steps, div=%d)",
            rec.get("task_id"), len(expert_steps), len(fail_steps), divergence,
        )
        return None

    correction_span = len(expert_steps) - divergence
    error_type = rec.get("error_type", "unknown")

    # Compute d (normalized divergence position) and gamma_e
    # d = div_point / expert_length; early diverge (d≈0) → low γ (steep φ decay)
    d = divergence / len(expert_steps) if len(expert_steps) > 0 else 0.0
    if gamma_mode == "continuous":
        gamma_e = gamma_min + (gamma_max - gamma_min) * d
    else:
        gamma_e = gamma_map.get(error_type, gamma_map.get("verification", 0.92))

    # Prompt: ICL/header + shared prefix steps (identical actions + observations)
    prompt_msgs = [msg_to_standard(m) for m in fail_convs[:fail_start]]
    for i in range(divergence):
        action, obs = expert_steps[i]
        prompt_msgs.append(msg_to_standard(action))
        if obs is not None:
            prompt_msgs.append(msg_to_standard(obs))

    # Chosen: expert continuation from divergence point
    chosen_msgs = []
    for i in range(divergence, len(expert_steps)):
        action, obs = expert_steps[i]
        chosen_msgs.append(msg_to_standard(action))
        if obs is not None:
            chosen_msgs.append(msg_to_standard(obs))

    # Rejected: failure continuation from divergence point
    rejected_msgs = []
    for i in range(divergence, len(fail_steps)):
        action, obs = fail_steps[i]
        rejected_msgs.append(msg_to_standard(action))
        if obs is not None:
            rejected_msgs.append(msg_to_standard(obs))

    if not chosen_msgs or not rejected_msgs:
        return None

    # Infer task_type from expert game_file (format: <task_type>/<trial_id>)
    gf = expert.get("game_file", "")
    parts = gf.split("/")
    task_type = ""
    for p in parts:
        if p.startswith(("pick_", "clean_", "heat_", "cool_", "put_", "examine_", "look_")):
            task_type = p
            break
    if not task_type:
        task_type = rec.get("task_type", "")

    return {
        "prompt": prompt_msgs,
        "chosen": chosen_msgs,
        "rejected": rejected_msgs,
        "error_type": error_type,
        "gamma_e": round(gamma_e, 6),
        "d": round(d, 6),
        "correction_span": correction_span,
        "task_id": rec.get("task_id"),
        "task_type": task_type,
        "game_file": rec.get("game_file", ""),
        "failure_step": rec.get("failure_step", -1),
        "divergence_step": divergence + 1,
        "metadata": {
            "expert_steps": len(expert_steps),
            "model_steps": len(fail_steps),
            "divergence_step": divergence,
            "gamma_mode": gamma_mode,
            "classification_source": rec.get("llm_original_type_source", "unknown"),
        },
    }


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_expert_index(path: str) -> dict:
    with open(path) as f:
        experts = json.load(f)
    index = {}
    for ex in experts:
        index[normalize_game_file(ex["game_file"])] = ex
    logger.info("Loaded %d experts", len(experts))
    return index


def load_classified(path: str) -> list:
    records = []
    with open(path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    logger.info("Loaded %d classified records", len(records))
    return records


def load_trajectories_from_dir(traj_dir: str) -> dict:
    """Index trajectory files by normalized game_file (fallback for missing conversations)."""
    index = {}
    for p in sorted(Path(traj_dir).glob("*.jsonl")):
        with open(p) as f:
            for line in f:
                if line.strip():
                    traj = json.loads(line)
                    index[normalize_game_file(traj.get("game_file", ""))] = traj
    logger.info("Loaded %d trajectories from %s", len(index), traj_dir)
    return index


def load_trajectory_input(pattern: str) -> list[dict]:
    """Load failure records from trajectory JSONL files (v8 format).

    Supports comma-separated paths and glob patterns.
    Only returns records with reward=False.
    """
    paths: list[str] = []
    for part in pattern.split(","):
        part = part.strip()
        expanded = glob_mod.glob(part)
        if expanded:
            paths.extend(expanded)
        else:
            paths.append(part)

    records = []
    for p in sorted(set(paths)):
        with open(p) as f:
            for line in f:
                if not line.strip():
                    continue
                traj = json.loads(line)
                if traj.get("reward") is True:
                    continue
                records.append(traj)
    logger.info("Loaded %d failure trajectories from %d files", len(records), len(paths))
    return records


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Build DPO pairs from classified failures + expert trajectories"
    )
    parser.add_argument(
        "--classified",
        type=str,
        default="data/classified/classified_errors.jsonl",
        help="Classified errors JSONL",
    )
    parser.add_argument(
        "--expert",
        type=str,
        default="eto_repo/data/alfworld_sft.json",
        help="Expert trajectories JSON",
    )
    parser.add_argument(
        "--trajectory_dir",
        type=str,
        default=None,
        help="Failure trajectory JSONL dir (optional; uses classified conversations if omitted)",
    )
    parser.add_argument(
        "--trajectory_input",
        type=str,
        default=None,
        help="Trajectory JSONL files (v8 format), comma-separated or glob pattern. "
             "Only reward=False records are used. Bypasses --classified.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/dpo_pairs_v2.jsonl",
        help="Output JSONL path",
    )
    parser.add_argument(
        "--gamma",
        type=str,
        default="action=0.85,verification=0.92,planning=0.97",
        help="Per-error-type γ_e values (error_type mode): action=0.85,verification=0.92,planning=0.97",
    )
    parser.add_argument(
        "--gamma_mode",
        type=str,
        choices=["error_type", "continuous"],
        default="error_type",
        help="Gamma computation mode: 'error_type' (discrete per error type) or "
             "'continuous' (γ(d) = γ_min + (γ_max - γ_min) × d)",
    )
    parser.add_argument(
        "--gamma_min",
        type=float,
        default=0.85,
        help="γ_min for continuous mode (early divergence → heavy discount). Default: 0.85",
    )
    parser.add_argument(
        "--gamma_max",
        type=float,
        default=1.0,
        help="γ_max for continuous mode (late divergence → near uniform). Default: 1.0",
    )
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(name)s %(levelname)s %(message)s")

    gamma_map = parse_gamma_arg(args.gamma)
    if args.gamma_mode == "continuous":
        logger.info("γ mode: continuous, γ_min=%.4f, γ_max=%.4f", args.gamma_min, args.gamma_max)
    else:
        logger.info("γ mode: error_type, map: %s", gamma_map)

    expert_index = load_expert_index(args.expert)

    # Load failure records: --trajectory_input (v8) or --classified
    if args.trajectory_input:
        classified = load_trajectory_input(args.trajectory_input)
    else:
        classified = load_classified(args.classified)

    traj_index = None
    if args.trajectory_dir:
        traj_index = load_trajectories_from_dir(args.trajectory_dir)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)

    pairs = []
    skipped: Counter = Counter()

    for rec in classified:
        # In error_type mode, skip unknown error types; in continuous mode, skip nothing
        if args.gamma_mode == "error_type" and rec.get("error_type") in ("unknown", None):
            skipped["unknown_error_type"] += 1
            continue

        key = normalize_game_file(rec.get("game_file", ""))
        expert = expert_index.get(key)
        if expert is None:
            skipped["no_expert_match"] += 1
            continue

        if not rec.get("conversations"):
            if traj_index:
                traj = traj_index.get(key)
                if traj and traj.get("conversations"):
                    rec["conversations"] = traj["conversations"]
                else:
                    skipped["no_conversations"] += 1
                    continue
            else:
                skipped["no_conversations"] += 1
                continue

        pair = build_pair(
            rec, expert, gamma_map,
            gamma_mode=args.gamma_mode,
            gamma_min=args.gamma_min,
            gamma_max=args.gamma_max,
        )
        if pair is None:
            skipped["build_failed"] += 1
            continue
        pairs.append(pair)

    with open(out, "w") as f:
        for pair in pairs:
            f.write(json.dumps(pair, ensure_ascii=False) + "\n")

    logger.info("Built %d DPO pairs -> %s", len(pairs), out)
    if skipped:
        logger.info("Skipped: %s", dict(skipped))

    # --- summary ---
    print(f"\n{'=' * 60}")
    print("DPO PAIR CONSTRUCTION SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total pairs: {len(pairs)}")
    print(f"Gamma mode:  {args.gamma_mode}")

    if args.gamma_mode == "continuous":
        _print_continuous_summary(pairs, args)
    else:
        _print_error_type_summary(pairs, gamma_map)

    # Common: divergence step distribution
    div_steps = [p["divergence_step"] for p in pairs]
    if div_steps:
        print(f"\nDivergence step distribution:")
        print(f"  min={min(div_steps)}, max={max(div_steps)}, "
              f"mean={sum(div_steps)/len(div_steps):.1f}, "
              f"step1={sum(1 for d in div_steps if d == 1)}")
    if skipped:
        print(f"\nSkipped: {dict(skipped)}")
    print(f"{'=' * 60}")


def _print_continuous_summary(pairs: list[dict], args) -> None:
    """Summary for continuous gamma mode."""
    d_vals = [p["d"] for p in pairs]
    gamma_vals = [p["gamma_e"] for p in pairs]

    if not d_vals:
        return

    print(f"γ_min={args.gamma_min}, γ_max={args.gamma_max}")

    print(f"\nd (normalized divergence position):")
    print(f"  min={min(d_vals):.4f}, max={max(d_vals):.4f}, "
          f"mean={statistics.mean(d_vals):.4f}, median={statistics.median(d_vals):.4f}")

    print(f"\nγ_e distribution:")
    print(f"  min={min(gamma_vals):.4f}, max={max(gamma_vals):.4f}, "
          f"mean={statistics.mean(gamma_vals):.4f}, median={statistics.median(gamma_vals):.4f}")

    early = sum(1 for d in d_vals if d < 0.2)
    mid = sum(1 for d in d_vals if 0.2 <= d < 0.5)
    late = sum(1 for d in d_vals if d >= 0.5)
    print(f"\n{'Region':<20} {'Count':>6} {'Fraction':>10}")
    print("-" * 40)
    n = len(d_vals)
    print(f"{'early (d<0.2)':<20} {early:>6} {early/n:>10.1%}")
    print(f"{'mid (0.2≤d<0.5)':<20} {mid:>6} {mid/n:>10.1%}")
    print(f"{'late (d≥0.5)':<20} {late:>6} {late/n:>10.1%}")


def _print_error_type_summary(pairs: list[dict], gamma_map: dict) -> None:
    """Summary for error_type gamma mode."""
    by_type: dict[str, list[int]] = defaultdict(list)
    for p in pairs:
        by_type[p["error_type"]].append(p["correction_span"])

    print(f"\n{'Type':<15} {'Count':>6} {'Avg CSpan':>10} {'γ_e':>6}")
    print("-" * 42)
    for et in ("action", "verification", "planning"):
        spans = by_type.get(et, [])
        ge = gamma_map.get(et, "-")
        if spans:
            avg = sum(spans) / len(spans)
            print(f"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}")
        else:
            print(f"{et:<15}      0          - {ge:>6}")
    # Show any other types that appeared
    for et, spans in sorted(by_type.items()):
        if et not in ("action", "verification", "planning"):
            avg = sum(spans) / len(spans)
            ge = gamma_map.get(et, "-")
            print(f"{et:<15} {len(spans):>6} {avg:>10.2f} {ge:>6}")


if __name__ == "__main__":
    main()
