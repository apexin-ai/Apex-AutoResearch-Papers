"""Failure mode descriptive analysis for ETADN paper.

Analyzes divergence patterns between failure trajectories and expert trajectories.
Produces structured JSON and Markdown report for paper's failure mode characterization.

Input: v7 trajectory JSONL files + expert alfworld_sft.json
Output: failure_mode_summary.json + failure_mode_report.md

Usage:
  python src/analyze_failure_modes.py \
    --failure_dir data/trajectories_v7_icl \
    --expert_file data/alfworld_sft.json \
    --output_dir outputs/failure_analysis
"""

import argparse
import json
import math
import statistics
from collections import Counter, defaultdict
from pathlib import Path


# ---------------------------------------------------------------------------
# Task type mapping
# ---------------------------------------------------------------------------

TASK_TYPE_FROM_PATH = {
    "pick_and_place": "pick_and_place",
    "pick_clean_then_place": "clean",
    "pick_heat_then_place": "heat",
    "pick_cool_then_place": "cool",
    "look_at_obj": "examine",
    "pick_two_obj": "pick_two",
}

CANONICAL_TASK_TYPES = ["pick_and_place", "clean", "heat", "cool", "examine", "pick_two"]


def get_task_type(game_file: str) -> str:
    """Infer canonical task type from game_file path."""
    for key, canonical in TASK_TYPE_FROM_PATH.items():
        if f"/{key}" in game_file or game_file.startswith(key):
            return canonical
    return "unknown"


def normalize_game_file(game_file: str) -> str:
    """Extract <task_dir>/<trial_dir> as matching key."""
    gf = game_file.rstrip("/")
    if gf.endswith("/game.tw-pddl"):
        gf = gf[: -len("/game.tw-pddl")]
    parts = gf.split("/")
    return "/".join(parts[-2:]) if len(parts) >= 2 else gf


# ---------------------------------------------------------------------------
# Message helpers (handle both formats)
# ---------------------------------------------------------------------------

def _role(msg: dict) -> str:
    return msg.get("role") or {"human": "user", "gpt": "assistant"}.get(msg.get("from", ""), "")


def _content(msg: dict) -> str:
    return msg.get("content") or msg.get("value", "")


def find_task_start(conversations: list) -> int:
    """Index of first action step after the last 'Your task is to:' message."""
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


def extract_action_text(content: str) -> str:
    """Extract and normalize 'Action: ...' from a step message."""
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.lower().startswith("action:"):
            return " ".join(stripped[len("action:"):].split()).lower()
    return " ".join(content.split()).lower()


# ---------------------------------------------------------------------------
# Divergence computation
# ---------------------------------------------------------------------------

def find_divergence_point(expert_steps, fail_steps) -> int:
    """First step index where expert and failure take different actions."""
    min_len = min(len(expert_steps), len(fail_steps))
    for i in range(min_len):
        ea = extract_action_text(_content(expert_steps[i][0]))
        fa = extract_action_text(_content(fail_steps[i][0]))
        if ea != fa:
            return i
    return min_len


def compute_divergence(fail_traj: dict, expert: dict) -> dict | None:
    """Compute divergence metrics for a failure trajectory matched to an expert.

    Returns dict with divergence_point, expert_length, d, correction_span,
    or None if computation fails.
    """
    fail_convs = fail_traj.get("conversations", [])
    expert_convs = expert.get("conversations", [])
    if not fail_convs or not expert_convs:
        return None

    fail_start = find_task_start(fail_convs)
    expert_start = find_task_start(expert_convs)

    fail_steps = extract_steps(fail_convs, fail_start)
    expert_steps = extract_steps(expert_convs, expert_start)

    if not fail_steps or not expert_steps:
        return None

    div_point = find_divergence_point(expert_steps, fail_steps)
    expert_len = len(expert_steps)
    d = div_point / expert_len if expert_len > 0 else 0.0
    correction_span = expert_len - div_point

    return {
        "divergence_point": div_point,
        "expert_length": expert_len,
        "failure_length": len(fail_steps),
        "d": d,
        "correction_span": correction_span,
    }


# ---------------------------------------------------------------------------
# γ(d) mapping
# ---------------------------------------------------------------------------

def gamma_from_d(d: float, gamma_min: float = 0.85, gamma_max: float = 0.97) -> float:
    """Map divergence position d ∈ [0,1] to γ via linear interpolation.

    Early divergence (d→0) → γ_min (action-error-like, concentrated credit).
    Late divergence (d→1) → γ_max (planning-error-like, spread credit).
    """
    return gamma_min + d * (gamma_max - gamma_min)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------

def load_trajectories(failure_dir: str) -> list[dict]:
    """Load all trajectory JSONL files from a directory."""
    records = []
    p = Path(failure_dir)
    for jsonl_file in sorted(p.glob("*.jsonl")):
        with open(jsonl_file) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
    return records


def load_expert_index(expert_file: str) -> dict[str, dict]:
    """Load expert trajectories indexed by normalized game_file."""
    with open(expert_file) as f:
        experts = json.load(f)
    return {normalize_game_file(ex["game_file"]): ex for ex in experts}


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------

def analyze(trajectories: list[dict], expert_index: dict[str, dict],
            gamma_min: float = 0.85, gamma_max: float = 0.97) -> dict:
    """Run all failure mode analyses. Returns structured results dict."""

    # -- 1. Basic statistics --
    total = len(trajectories)
    successes = [t for t in trajectories if t.get("reward")]
    failures = [t for t in trajectories if not t.get("reward")]
    n_success = len(successes)
    n_failure = len(failures)
    success_rate = n_success / total if total > 0 else 0.0

    # Per-task-type success rate
    type_total = Counter()
    type_success = Counter()
    for t in trajectories:
        tt = t.get("task_type") or get_task_type(t.get("game_file", ""))
        type_total[tt] += 1
        if t.get("reward"):
            type_success[tt] += 1

    per_type_sr = {}
    for tt in CANONICAL_TASK_TYPES:
        tot = type_total.get(tt, 0)
        suc = type_success.get(tt, 0)
        per_type_sr[tt] = {
            "total": tot,
            "success": suc,
            "failure": tot - suc,
            "success_rate": suc / tot if tot > 0 else None,
        }

    basic_stats = {
        "total_tasks": total,
        "success": n_success,
        "failure": n_failure,
        "success_rate": success_rate,
        "per_task_type": per_type_sr,
    }

    # -- 4. Expert/Failure matching --
    exact_match = 0
    template_match = 0
    unmatched = 0
    matched_failures = []

    for t in failures:
        gf = t.get("game_file", "")
        key = normalize_game_file(gf)
        expert = expert_index.get(key)

        if expert is not None:
            exact_match += 1
            div_info = compute_divergence(t, expert)
            if div_info is not None:
                tt = t.get("task_type") or get_task_type(gf)
                matched_failures.append({
                    "task_type": tt,
                    "game_file": gf,
                    **div_info,
                })
        else:
            tt = t.get("task_type") or get_task_type(gf)
            found_template = False
            for ek, ev in expert_index.items():
                expert_tt = get_task_type(ev.get("game_file", ""))
                if expert_tt == tt:
                    found_template = True
                    break
            if found_template:
                template_match += 1
            else:
                unmatched += 1

    match_stats = {
        "exact_match": exact_match,
        "exact_match_rate": exact_match / n_failure if n_failure > 0 else 0.0,
        "template_match_only": template_match,
        "template_match_rate": (exact_match + template_match) / n_failure if n_failure > 0 else 0.0,
        "unmatched": unmatched,
        "divergence_computed": len(matched_failures),
    }

    # -- 2. Divergence analysis --
    d_values = [m["d"] for m in matched_failures]
    d_by_type = defaultdict(list)
    for m in matched_failures:
        d_by_type[m["task_type"]].append(m["d"])

    bins = [(i / 10, (i + 1) / 10) for i in range(10)]
    bin_labels = [f"{lo:.1f}-{hi:.1f}" for lo, hi in bins]
    histogram = {label: 0 for label in bin_labels}
    for d in d_values:
        idx = min(int(d * 10), 9)
        histogram[bin_labels[idx]] += 1

    early = [d for d in d_values if d < 0.33]
    mid = [d for d in d_values if 0.33 <= d < 0.67]
    late = [d for d in d_values if d >= 0.67]

    def _dist_stats(vals):
        if not vals:
            return None
        return {
            "n": len(vals),
            "mean": statistics.mean(vals),
            "median": statistics.median(vals),
            "std": statistics.stdev(vals) if len(vals) > 1 else 0.0,
            "min": min(vals),
            "max": max(vals),
            "q1": statistics.quantiles(vals, n=4)[0] if len(vals) >= 2 else vals[0],
            "q3": statistics.quantiles(vals, n=4)[2] if len(vals) >= 2 else vals[0],
        }

    per_type_d = {}
    for tt in CANONICAL_TASK_TYPES:
        per_type_d[tt] = _dist_stats(d_by_type.get(tt, []))

    divergence_analysis = {
        "overall": _dist_stats(d_values),
        "histogram": histogram,
        "temporal_groups": {
            "early_d_lt_0.33": {"n": len(early), "mean_d": statistics.mean(early) if early else None},
            "mid_0.33_le_d_lt_0.67": {"n": len(mid), "mean_d": statistics.mean(mid) if mid else None},
            "late_d_ge_0.67": {"n": len(late), "mean_d": statistics.mean(late) if late else None},
        },
        "per_task_type": per_type_d,
    }

    # -- 3. γ(d) mapping preview --
    gamma_values = [gamma_from_d(d, gamma_min, gamma_max) for d in d_values]
    gamma_analysis = {
        "gamma_min": gamma_min,
        "gamma_max": gamma_max,
        "distribution": _dist_stats(gamma_values) if gamma_values else None,
        "temporal_group_gamma": {
            "early": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in early]) if early else None,
            "mid": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in mid]) if mid else None,
            "late": statistics.mean([gamma_from_d(d, gamma_min, gamma_max) for d in late]) if late else None,
        },
    }

    # -- 5. Trajectory length analysis --
    fail_lengths = [m["failure_length"] for m in matched_failures]
    expert_lengths = [m["expert_length"] for m in matched_failures]
    correction_spans = [m["correction_span"] for m in matched_failures]

    length_analysis = {
        "failure_trajectory_length": _dist_stats(fail_lengths),
        "expert_trajectory_length": _dist_stats(expert_lengths),
        "correction_span": _dist_stats(correction_spans),
    }

    return {
        "basic_stats": basic_stats,
        "divergence_analysis": divergence_analysis,
        "gamma_mapping_preview": gamma_analysis,
        "match_stats": match_stats,
        "length_analysis": length_analysis,
    }


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def _fmt(val, decimals=3):
    if val is None:
        return "-"
    if isinstance(val, float):
        return f"{val:.{decimals}f}"
    return str(val)


def generate_markdown(results: dict) -> str:
    """Generate Markdown report from analysis results."""
    lines = []
    bs = results["basic_stats"]
    da = results["divergence_analysis"]
    gm = results["gamma_mapping_preview"]
    ms = results["match_stats"]
    la = results["length_analysis"]

    # -- Section 1 --
    lines.append("# Failure Mode Analysis Report\n")
    lines.append("## 1. Basic Statistics\n")
    lines.append(f"| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Total tasks | {bs['total_tasks']} |")
    lines.append(f"| Success | {bs['success']} |")
    lines.append(f"| Failure | {bs['failure']} |")
    lines.append(f"| Success rate | {_fmt(bs['success_rate'])} |")
    lines.append("")

    lines.append("### Per-task-type Success Rate\n")
    lines.append("| Task Type | Total | Success | Failure | Success Rate |")
    lines.append("|-----------|-------|---------|---------|--------------|")
    for tt in CANONICAL_TASK_TYPES:
        info = bs["per_task_type"].get(tt, {})
        lines.append(
            f"| {tt} | {info.get('total', 0)} | {info.get('success', 0)} "
            f"| {info.get('failure', 0)} | {_fmt(info.get('success_rate'))} |"
        )
    lines.append("")

    # -- Section 2 --
    lines.append("## 2. Divergence Analysis\n")
    ov = da.get("overall")
    if ov:
        lines.append(f"Divergence position d = divergence_point / expert_length\n")
        lines.append("| Statistic | Value |")
        lines.append("|-----------|-------|")
        for k in ("n", "mean", "median", "std", "min", "max", "q1", "q3"):
            lines.append(f"| {k} | {_fmt(ov[k])} |")
        lines.append("")

    lines.append("### d-value Histogram\n")
    lines.append("| Bin | Count |")
    lines.append("|-----|-------|")
    for bin_label, count in da["histogram"].items():
        lines.append(f"| {bin_label} | {count} |")
    lines.append("")

    lines.append("### Temporal Groups\n")
    lines.append("| Group | n | Mean d |")
    lines.append("|-------|---|--------|")
    tg = da["temporal_groups"]
    for label, key in [("Early (d<0.33)", "early_d_lt_0.33"),
                        ("Mid (0.33≤d<0.67)", "mid_0.33_le_d_lt_0.67"),
                        ("Late (d≥0.67)", "late_d_ge_0.67")]:
        g = tg[key]
        lines.append(f"| {label} | {g['n']} | {_fmt(g.get('mean_d'))} |")
    lines.append("")

    lines.append("### Per-task-type d Distribution\n")
    lines.append("| Task Type | n | Mean | Median | Std |")
    lines.append("|-----------|---|------|--------|-----|")
    for tt in CANONICAL_TASK_TYPES:
        info = da["per_task_type"].get(tt)
        if info:
            lines.append(
                f"| {tt} | {info['n']} | {_fmt(info['mean'])} "
                f"| {_fmt(info['median'])} | {_fmt(info['std'])} |"
            )
        else:
            lines.append(f"| {tt} | 0 | - | - | - |")
    lines.append("")

    # -- Section 3 --
    lines.append("## 3. γ(d) Mapping Preview\n")
    lines.append(f"γ(d) = γ_min + d·(γ_max - γ_min), γ_min={gm['gamma_min']}, γ_max={gm['gamma_max']}\n")
    gd = gm.get("distribution")
    if gd:
        lines.append("| Statistic | γ value |")
        lines.append("|-----------|---------|")
        for k in ("mean", "median", "std", "min", "max"):
            lines.append(f"| {k} | {_fmt(gd[k], 4)} |")
        lines.append("")

    lines.append("### Mean γ by Temporal Group\n")
    lines.append("| Group | Mean γ |")
    lines.append("|-------|--------|")
    tgg = gm["temporal_group_gamma"]
    for label, key in [("Early", "early"), ("Mid", "mid"), ("Late", "late")]:
        lines.append(f"| {label} | {_fmt(tgg.get(key), 4)} |")
    lines.append("")

    # -- Section 4 --
    lines.append("## 4. Expert/Failure Matching\n")
    lines.append("| Metric | Value |")
    lines.append("|--------|-------|")
    lines.append(f"| Exact match (game_file) | {ms['exact_match']} ({_fmt(ms['exact_match_rate'])}) |")
    lines.append(f"| Template match (same task type) | {ms['template_match_only']} |")
    lines.append(f"| Combined match rate | {_fmt(ms['template_match_rate'])} |")
    lines.append(f"| Unmatched failures | {ms['unmatched']} |")
    lines.append(f"| Divergence computed | {ms['divergence_computed']} |")
    lines.append("")

    # -- Section 5 --
    lines.append("## 5. Trajectory Length Analysis\n")
    lines.append("| Metric | Failure | Expert | Correction Span |")
    lines.append("|--------|---------|--------|-----------------|")
    fl = la.get("failure_trajectory_length")
    el = la.get("expert_trajectory_length")
    cs = la.get("correction_span")
    for stat in ("n", "mean", "median", "std", "min", "max"):
        lines.append(
            f"| {stat} | {_fmt(fl.get(stat) if fl else None)} "
            f"| {_fmt(el.get(stat) if el else None)} "
            f"| {_fmt(cs.get(stat) if cs else None)} |"
        )
    lines.append("")

    return "\n".join(lines)


def print_summary(results: dict):
    """Print concise summary to stdout."""
    bs = results["basic_stats"]
    da = results["divergence_analysis"]
    ms = results["match_stats"]

    print(f"\n{'=' * 55}")
    print("FAILURE MODE ANALYSIS SUMMARY")
    print(f"{'=' * 55}")
    print(f"Tasks: {bs['total_tasks']}  Success: {bs['success']}  "
          f"Failure: {bs['failure']}  SR: {bs['success_rate']:.3f}")

    print(f"\nPer-type SR:")
    for tt in CANONICAL_TASK_TYPES:
        info = bs["per_task_type"].get(tt, {})
        sr = info.get("success_rate")
        sr_str = f"{sr:.3f}" if sr is not None else "-"
        print(f"  {tt:<16} {info.get('total', 0):>4} tasks  SR={sr_str}")

    print(f"\nMatching: exact={ms['exact_match']}  "
          f"template_only={ms['template_match_only']}  "
          f"unmatched={ms['unmatched']}  "
          f"divergence_computed={ms['divergence_computed']}")

    ov = da.get("overall")
    if ov:
        print(f"\nDivergence d (n={ov['n']}):")
        print(f"  mean={ov['mean']:.3f}  median={ov['median']:.3f}  "
              f"std={ov['std']:.3f}  [{ov['min']:.3f}, {ov['max']:.3f}]")

    tg = da["temporal_groups"]
    print(f"\nTemporal groups:")
    for label, key in [("Early  d<0.33 ", "early_d_lt_0.33"),
                        ("Mid    0.33-0.67", "mid_0.33_le_d_lt_0.67"),
                        ("Late   d≥0.67 ", "late_d_ge_0.67")]:
        g = tg[key]
        print(f"  {label}  n={g['n']}")

    print(f"{'=' * 55}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Failure mode descriptive analysis for ETADN paper"
    )
    parser.add_argument("--failure_dir", type=str, required=True,
                        help="Directory with trajectory JSONL files")
    parser.add_argument("--expert_file", type=str, required=True,
                        help="Expert trajectories JSON (alfworld_sft.json)")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="Output directory for results")
    parser.add_argument("--gamma_min", type=float, default=0.85,
                        help="γ_min for γ(d) mapping (default: 0.85)")
    parser.add_argument("--gamma_max", type=float, default=0.97,
                        help="γ_max for γ(d) mapping (default: 0.97)")
    args = parser.parse_args()

    trajectories = load_trajectories(args.failure_dir)
    if not trajectories:
        print(f"ERROR: No trajectories found in {args.failure_dir}")
        return

    expert_index = load_expert_index(args.expert_file)
    print(f"Loaded {len(trajectories)} trajectories, {len(expert_index)} experts")

    results = analyze(trajectories, expert_index, args.gamma_min, args.gamma_max)

    out = Path(args.output_dir)
    out.mkdir(parents=True, exist_ok=True)

    json_path = out / "failure_mode_summary.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    md_path = out / "failure_mode_report.md"
    report = generate_markdown(results)
    with open(md_path, "w") as f:
        f.write(report)

    print_summary(results)
    print(f"\nOutput: {json_path}")
    print(f"        {md_path}")


if __name__ == "__main__":
    main()
