"""Plan-005 Routing Pattern Analysis.

Extracts per-task routing patterns from plan-001b episode data.
Outputs: routing heatmap figure, failure mode taxonomy, JSON summary.
"""

import argparse
import json
import math
import os
import re
import statistics
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple

# Reuse load_episodes from death_decomposition
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from death_decomposition import load_episodes, is_dead, classify_episode, DEATH_THRESHOLD


# ---------------------------------------------------------------------------
# 1. Per-task routing metrics
# ---------------------------------------------------------------------------

def compute_task_metrics(task_name: str, episodes: List[dict]) -> dict:
    """Compute routing metrics for a single task."""
    n = len(episodes)
    int_scores = [ep["always_internal"]["final_score"] for ep in episodes]
    det_scores = [ep["always_deterministic"]["final_score"] for ep in episodes]

    # det-preferred rate
    det_pref_count = sum(1 for i, d in zip(int_scores, det_scores)
                         if classify_episode(i, d)[0] == "det-preferred")
    int_pref_count = sum(1 for i, d in zip(int_scores, det_scores)
                         if classify_episode(i, d)[0] == "internal-preferred")
    det_pref_rate = det_pref_count / n

    # death rates
    int_death_rate = sum(1 for s in int_scores if is_dead(s)) / n
    det_death_rate = sum(1 for s in det_scores if is_dead(s)) / n

    # score variance (std dev)
    int_std = statistics.pstdev(int_scores) if n > 1 else 0.0
    det_std = statistics.pstdev(det_scores) if n > 1 else 0.0

    # mean score gap Δ(D-I)
    int_mean = statistics.mean(int_scores)
    det_mean = statistics.mean(det_scores)
    delta = det_mean - int_mean

    # death avoidance fraction (DAF)
    nd_int = [i for i, d in zip(int_scores, det_scores) if not is_dead(i) and not is_dead(d)]
    nd_det = [d for i, d in zip(int_scores, det_scores) if not is_dead(i) and not is_dead(d)]
    if nd_int and delta != 0:
        delta_nd = statistics.mean(nd_det) - statistics.mean(nd_int)
        daf = (delta - delta_nd) / delta
    else:
        delta_nd = float("nan")
        daf = float("nan")

    # signal category classification
    if daf is not None and not math.isnan(daf) and daf >= 0.95:
        signal_category = "death-dominated"
    elif det_pref_rate < 0.5:
        signal_category = "internal-preferred"
    else:
        signal_category = "genuine-det"

    return {
        "task": task_name,
        "n_episodes": n,
        "det_pref_rate": round(det_pref_rate, 4),
        "int_pref_rate": round(int_pref_count / n, 4),
        "int_death_rate": round(int_death_rate, 4),
        "det_death_rate": round(det_death_rate, 4),
        "int_score_std": round(int_std, 2),
        "det_score_std": round(det_std, 2),
        "int_mean": round(int_mean, 2),
        "det_mean": round(det_mean, 2),
        "delta_DI": round(delta, 2),
        "delta_no_death": round(delta_nd, 2) if not math.isnan(delta_nd) else None,
        "daf": round(daf, 4) if not math.isnan(daf) else None,
        "signal_category": signal_category,
    }


# ---------------------------------------------------------------------------
# 2. Routing heatmap figure
# ---------------------------------------------------------------------------

CATEGORY_ORDER = ["genuine-det", "death-dominated", "internal-preferred"]
CATEGORY_COLORS = {
    "genuine-det": "#b2182b",
    "death-dominated": "#2166ac",
    "internal-preferred": "#4dac26",
}

HEATMAP_METRICS = [
    ("det_pref_rate", "Det-pref\nrate"),
    ("int_death_rate", "Int death\nrate"),
    ("det_death_rate", "Det death\nrate"),
    ("delta_DI", "Δ(D−I)"),
    ("daf", "DAF"),
]


def shorten_task(name: str, max_len: int = 22) -> str:
    name = name.replace("measure-melting-point-", "melt-pt-")
    name = name.replace("chemistry-mix-paint-", "chem-paint-")
    name = name.replace("chemistry-mix", "chem-mix")
    name = name.replace("change-the-state-of-matter-of", "state-change")
    name = name.replace("inclined-plane-friction-", "incl-fric-")
    name = name.replace("inclined-plane-determine-angle", "incl-angle")
    name = name.replace("power-component-renewable-vs-nonrenewable-energy", "power-renew")
    name = name.replace("power-component", "power-comp")
    name = name.replace("test-conductivity-of-unknown-substances", "cond-unknown")
    name = name.replace("test-conductivity", "cond-test")
    name = name.replace("mendelian-genetics-", "mendel-")
    name = name.replace("lifespan-longest-lived-then-shortest-lived", "lifespan-long-short")
    name = name.replace("lifespan-longest-lived", "lifespan-long")
    name = name.replace("lifespan-shortest-lived", "lifespan-short")
    name = name.replace("identify-life-stages-", "life-stage-")
    name = name.replace("find-non-living-thing", "find-nonliving")
    name = name.replace("find-living-thing", "find-living")
    name = name.replace("use-thermometer", "thermometer")
    if len(name) > max_len:
        name = name[:max_len - 1] + "…"
    return name


def plot_routing_heatmap(task_metrics: List[dict], output_dir: str):
    """Generate task × metric routing heatmap (Figure 1 for plan-005)."""
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize, TwoSlopeNorm
    from matplotlib.patches import Rectangle

    # Sort tasks: group by signal_category, within each group sort by det_pref_rate desc
    grouped = defaultdict(list)
    for m in task_metrics:
        grouped[m["signal_category"]].append(m)
    for cat in grouped:
        grouped[cat].sort(key=lambda x: x["det_pref_rate"], reverse=True)

    ordered = []
    group_boundaries = []
    for cat in CATEGORY_ORDER:
        if cat in grouped:
            group_boundaries.append((cat, len(ordered), len(ordered) + len(grouped[cat])))
            ordered.extend(grouped[cat])

    n_tasks = len(ordered)
    n_metrics = len(HEATMAP_METRICS)

    # Build matrix
    matrix = np.full((n_tasks, n_metrics), np.nan)
    for i, m in enumerate(ordered):
        for j, (key, _) in enumerate(HEATMAP_METRICS):
            val = m.get(key)
            if val is not None:
                matrix[i, j] = val

    task_labels = [shorten_task(m["task"]) for m in ordered]
    metric_labels = [label for _, label in HEATMAP_METRICS]

    fig_height = max(4, 0.4 * n_tasks + 1.5)
    fig, ax = plt.subplots(figsize=(7, fig_height))

    # Per-column normalization for better contrast
    col_cmaps = ["RdYlBu_r", "Reds", "Reds", "RdBu_r", "Blues"]
    for j in range(n_metrics):
        col = matrix[:, j]
        valid = col[~np.isnan(col)]
        if len(valid) == 0:
            continue

        if HEATMAP_METRICS[j][0] == "delta_DI":
            vmax = max(abs(valid.min()), abs(valid.max()), 1)
            norm = TwoSlopeNorm(vcenter=0, vmin=-vmax, vmax=vmax)
        elif HEATMAP_METRICS[j][0] == "daf":
            norm = Normalize(vmin=0, vmax=1)
        elif HEATMAP_METRICS[j][0] in ("int_death_rate", "det_death_rate"):
            norm = Normalize(vmin=0, vmax=1)
        else:
            norm = Normalize(vmin=0, vmax=1)

        cmap = plt.get_cmap(col_cmaps[j])

        for i in range(n_tasks):
            val = matrix[i, j]
            if np.isnan(val):
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                       facecolor="#f0f0f0", edgecolor="white", linewidth=0.5))
                ax.text(j, i, "—", ha="center", va="center", fontsize=7, color="#999999")
            else:
                color = cmap(norm(val))
                ax.add_patch(Rectangle((j - 0.5, i - 0.5), 1, 1,
                                       facecolor=color, edgecolor="white", linewidth=0.5))
                # Format text
                if HEATMAP_METRICS[j][0] == "delta_DI":
                    txt = f"{val:+.1f}"
                elif HEATMAP_METRICS[j][0] in ("det_pref_rate", "daf", "int_death_rate", "det_death_rate"):
                    txt = f"{val:.0%}"
                else:
                    txt = f"{val:.2f}"
                # Text color: dark on light, light on dark
                lum = 0.299 * color[0] + 0.587 * color[1] + 0.114 * color[2]
                tc = "white" if lum < 0.5 else "black"
                ax.text(j, i, txt, ha="center", va="center", fontsize=7, color=tc, fontweight="bold")

    # Group separators and labels
    for cat, start, end in group_boundaries:
        if start > 0:
            ax.axhline(start - 0.5, color="black", linewidth=1.2)
        # Category label on the right
        mid = (start + end - 1) / 2
        ax.text(n_metrics - 0.5 + 0.3, mid, cat.replace("-", "\n"),
                ha="left", va="center", fontsize=7, fontstyle="italic",
                color=CATEGORY_COLORS.get(cat, "black"))

    ax.set_xlim(-0.5, n_metrics - 0.5)
    ax.set_ylim(n_tasks - 0.5, -0.5)
    ax.set_xticks(range(n_metrics))
    ax.set_xticklabels(metric_labels, fontsize=8, ha="center")
    ax.xaxis.set_ticks_position("top")
    ax.xaxis.set_label_position("top")
    ax.set_yticks(range(n_tasks))
    ax.set_yticklabels(task_labels, fontsize=7.5)
    ax.tick_params(length=0)

    for spine in ax.spines.values():
        spine.set_visible(False)

    fig.tight_layout()
    fig.subplots_adjust(right=0.82)
    os.makedirs(output_dir, exist_ok=True)
    for ext in ["pdf", "png"]:
        path = os.path.join(output_dir, f"fig_routing_heatmap.{ext}")
        fig.savefig(path, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"[Heatmap] saved to {output_dir}/fig_routing_heatmap.{{pdf,png}}")


# ---------------------------------------------------------------------------
# 3. Failure mode taxonomy
# ---------------------------------------------------------------------------

DEATH_KEYWORDS = [
    ("focus on", "focus-action"),
    ("eat", "eat-action"),
    ("drink", "drink-action"),
    ("use", "use-action"),
    ("mix", "mix-action"),
    ("pour", "pour-action"),
    ("connect", "connect-action"),
    ("open", "open-action"),
    ("activate", "activate-action"),
    ("move", "move-action"),
    ("pick up", "pickup-action"),
]

OBS_DEATH_PATTERNS = [
    (r"you have died", "explicit-death-msg"),
    (r"game over", "game-over-msg"),
    (r"penalty", "penalty-msg"),
    (r"(?:burned|burnt|melted|exploded|poisoned|shocked|electrocuted)", "hazard-death"),
]


def extract_death_steps(episodes: List[dict], mode: str = "always_internal") -> List[dict]:
    """Extract steps that caused death (score drop to <= DEATH_THRESHOLD)."""
    death_steps = []
    for ep in episodes:
        run = ep.get(mode, {})
        steps = run.get("steps", [])
        if not steps:
            continue
        final = run.get("final_score", 0)
        if not is_dead(final):
            continue
        # Find the death step: the step where score crosses threshold
        for s in steps:
            score_after = s.get("score_after", s.get("score", None))
            if score_after is not None and is_dead(score_after):
                death_steps.append({
                    "task": ep.get("always_internal", {}).get("task_name",
                           ep.get("always_deterministic", {}).get("task_name", "unknown")),
                    "mode": mode.replace("always_", ""),
                    "step_idx": s.get("step", -1),
                    "action": s.get("action", ""),
                    "observation": s.get("observation", ""),
                    "score_before": s.get("score_before", None),
                    "score_after": score_after,
                })
                break
    return death_steps


def classify_death_action(action: str) -> str:
    """Classify death-causing action into category."""
    action_lower = action.lower()
    for keyword, category in DEATH_KEYWORDS:
        if keyword in action_lower:
            return category
    return "other-action"


def classify_death_observation(obs: str) -> List[str]:
    """Extract death-related patterns from observation."""
    obs_lower = obs.lower()
    found = []
    for pattern, label in OBS_DEATH_PATTERNS:
        if re.search(pattern, obs_lower):
            found.append(label)
    if not found:
        found.append("unclassified-obs")
    return found


def build_failure_taxonomy(task_episodes: Dict[str, List[dict]]) -> dict:
    """Build failure mode taxonomy from step-level death analysis."""
    all_death_steps_int = []
    all_death_steps_det = []

    for task_name, episodes in task_episodes.items():
        all_death_steps_int.extend(extract_death_steps(episodes, "always_internal"))
        all_death_steps_det.extend(extract_death_steps(episodes, "always_deterministic"))

    def analyze_deaths(death_steps: List[dict]) -> dict:
        if not death_steps:
            return {"count": 0, "action_categories": {}, "obs_patterns": {}, "top_actions": {}, "per_task": {}}

        action_cats = Counter()
        obs_pats = Counter()
        raw_actions = Counter()
        per_task = defaultdict(int)

        for ds in death_steps:
            action_cats[classify_death_action(ds["action"])] += 1
            for pat in classify_death_observation(ds["observation"]):
                obs_pats[pat] += 1
            raw_actions[ds["action"]] += 1
            per_task[ds["task"]] += 1

        return {
            "count": len(death_steps),
            "action_categories": dict(action_cats.most_common()),
            "obs_patterns": dict(obs_pats.most_common()),
            "top_actions": dict(raw_actions.most_common(15)),
            "per_task": dict(sorted(per_task.items(), key=lambda x: -x[1])),
        }

    return {
        "internal": analyze_deaths(all_death_steps_int),
        "deterministic": analyze_deaths(all_death_steps_det),
        "death_step_examples": {
            "internal": [
                {"task": ds["task"], "step": ds["step_idx"],
                 "action": ds["action"], "observation": ds["observation"][:200]}
                for ds in all_death_steps_int[:10]
            ],
            "deterministic": [
                {"task": ds["task"], "step": ds["step_idx"],
                 "action": ds["action"], "observation": ds["observation"][:200]}
                for ds in all_death_steps_det[:10]
            ],
        },
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Plan-005 Routing Pattern Analysis")
    parser.add_argument("--data_dirs", required=True,
                        help="Comma-separated data directories")
    parser.add_argument("--output_dir", default="results/plan005",
                        help="Output directory")
    parser.add_argument("--min_episodes", type=int, default=5,
                        help="Minimum episodes per task (filter threshold)")
    args = parser.parse_args()

    data_dirs = [d.strip() for d in args.data_dirs.split(",") if d.strip()]
    os.makedirs(args.output_dir, exist_ok=True)

    # Load episodes
    task_episodes = load_episodes(data_dirs)
    if not task_episodes:
        print("ERROR: No episodes found")
        return

    # Filter by min_episodes
    filtered = {k: v for k, v in task_episodes.items() if len(v) >= args.min_episodes}
    skipped = {k: len(v) for k, v in task_episodes.items() if len(v) < args.min_episodes}
    if skipped:
        print(f"Skipped {len(skipped)} tasks with < {args.min_episodes} episodes: {skipped}")

    print(f"Loaded {sum(len(v) for v in filtered.values())} episodes "
          f"across {len(filtered)} tasks")

    # 1. Per-task metrics
    task_metrics = []
    for task_name in sorted(filtered.keys()):
        m = compute_task_metrics(task_name, filtered[task_name])
        task_metrics.append(m)

    # Print summary table
    print(f"\n{'Task':<42} {'N':>4} {'DetPref':>7} {'I_d%':>5} {'D_d%':>5} "
          f"{'Δ(D-I)':>7} {'DAF':>6} {'Category':<18}")
    print("-" * 100)
    for m in task_metrics:
        daf_str = f"{m['daf']:.0%}" if m["daf"] is not None else "N/A"
        print(f"{m['task']:<42} {m['n_episodes']:>4} {m['det_pref_rate']:>7.0%} "
              f"{m['int_death_rate']*100:>4.0f}% {m['det_death_rate']*100:>4.0f}% "
              f"{m['delta_DI']:>+7.1f} {daf_str:>6} {m['signal_category']:<18}")

    # Category summary
    cat_counts = Counter(m["signal_category"] for m in task_metrics)
    print(f"\nCategories: {dict(cat_counts)}")

    # Save JSON
    metrics_path = os.path.join(args.output_dir, "routing_metrics.json")
    with open(metrics_path, "w") as f:
        json.dump(task_metrics, f, indent=2)
    print(f"[Saved] {metrics_path}")

    # 2. Heatmap figure
    plot_routing_heatmap(task_metrics, args.output_dir)

    # 3. Failure mode taxonomy
    taxonomy = build_failure_taxonomy(filtered)
    taxonomy_path = os.path.join(args.output_dir, "failure_taxonomy.json")
    with open(taxonomy_path, "w") as f:
        json.dump(taxonomy, f, indent=2)
    print(f"[Saved] {taxonomy_path}")

    # Print taxonomy summary
    print(f"\n--- Failure Mode Taxonomy ---")
    for mode in ["internal", "deterministic"]:
        t = taxonomy[mode]
        print(f"\n{mode.upper()} deaths: {t['count']}")
        if t["action_categories"]:
            print(f"  Action categories: {t['action_categories']}")
        if t["top_actions"]:
            top3 = dict(list(t["top_actions"].items())[:5])
            print(f"  Top actions: {top3}")


if __name__ == "__main__":
    main()
