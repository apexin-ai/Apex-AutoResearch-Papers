"""Plan-011: Offline keyword routing accuracy analysis.

Simulates keyword router decisions on existing episode data,
compares with death-aware episode-level ground truth labels.
"""

import argparse
import json
import os
from collections import defaultdict
from typing import Dict, List, Tuple, Optional


DEATH_THRESHOLD = -100


def is_dead(score: float) -> bool:
    return score <= DEATH_THRESHOLD


def classify_episode(int_score: float, det_score: float) -> Tuple[str, str]:
    int_died = is_dead(int_score)
    det_died = is_dead(det_score)
    if int_died and not det_died:
        return "det-preferred", "int_died_det_alive"
    if det_died and not int_died:
        return "internal-preferred", "det_died_int_alive"
    if int_died and det_died:
        return "no-preference", "both_died"
    if det_score > int_score:
        return "det-preferred", "both_alive_det_wins"
    if int_score > det_score:
        return "internal-preferred", "both_alive_int_wins"
    return "no-preference", "tie"


def load_keywords(path: str) -> List[str]:
    with open(path) as f:
        data = json.load(f)
    if "keywords" in data:
        return data["keywords"]
    return data["route_to_simulator"]


def keyword_match(text: str, keywords: List[str]) -> Tuple[bool, Optional[str]]:
    text_lower = text.lower()
    for kw in keywords:
        if kw.lower() in text_lower:
            return True, kw
    return False, None


def get_episode_steps(episode: Dict) -> Tuple[List[Dict], str]:
    for key in ["oracle", "always_internal"]:
        if key in episode and episode[key].get("steps"):
            return episode[key]["steps"], key
    return [], "none"


def analyze_episode(episode: Dict, keywords: List[str],
                    check_obs: bool = False) -> Dict:
    int_ep = episode["always_internal"]
    det_ep = episode["always_deterministic"]
    int_score = int_ep["final_score"]
    det_score = det_ep["final_score"]
    gt_label, gt_reason = classify_episode(int_score, det_score)

    steps, step_source = get_episode_steps(episode)

    step_details = []
    kw_hits = defaultdict(int)

    for s in steps:
        action = s.get("action", "")
        text = action
        if check_obs:
            obs = s.get("observation", "")
            text = obs + " " + action

        matched, kw = keyword_match(text, keywords)
        step_details.append({
            "step": s.get("step", len(step_details)),
            "action": action,
            "keyword_matched": matched,
            "matched_keyword": kw,
        })
        if matched and kw:
            kw_hits[kw] += 1

    n_steps = len(step_details)
    n_matched = sum(1 for sd in step_details if sd["keyword_matched"])
    match_rate = n_matched / n_steps if n_steps > 0 else 0.0

    kw_label = "det-preferred" if match_rate > 0.5 else "internal-preferred"

    return {
        "episode_idx": episode.get("episode_idx", -1),
        "variation_idx": episode.get("variation_idx", -1),
        "n_steps": n_steps,
        "n_keyword_matched": n_matched,
        "keyword_match_rate": round(match_rate, 4),
        "keyword_route_label": kw_label,
        "ground_truth_label": gt_label,
        "ground_truth_reason": gt_reason,
        "int_score": int_score,
        "det_score": det_score,
        "int_died": is_dead(int_score),
        "det_died": is_dead(det_score),
        "step_source": step_source,
        "keyword_hits": dict(kw_hits),
    }


def compute_metrics(results: List[Dict]) -> Dict:
    confusion = defaultdict(lambda: defaultdict(int))
    for r in results:
        confusion[r["keyword_route_label"]][r["ground_truth_label"]] += 1

    scorable = [r for r in results if r["ground_truth_label"] != "no-preference"]
    correct = sum(1 for r in scorable
                  if r["keyword_route_label"] == r["ground_truth_label"])
    accuracy = correct / len(scorable) if scorable else 0.0

    class_metrics = {}
    for cls in ["det-preferred", "internal-preferred"]:
        tp = sum(1 for r in results
                 if r["keyword_route_label"] == cls and r["ground_truth_label"] == cls)
        fp = sum(1 for r in results
                 if r["keyword_route_label"] == cls and r["ground_truth_label"] != cls)
        fn = sum(1 for r in results
                 if r["keyword_route_label"] != cls and r["ground_truth_label"] == cls)

        prec = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rec = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0

        class_metrics[cls] = {
            "tp": tp, "fp": fp, "fn": fn,
            "precision": round(prec, 4),
            "recall": round(rec, 4),
            "f1": round(f1, 4),
        }

    return {
        "n_total": len(results),
        "n_scorable": len(scorable),
        "n_correct": correct,
        "accuracy": round(accuracy, 4),
        "confusion_matrix": {k: dict(v) for k, v in confusion.items()},
        "class_metrics": class_metrics,
    }


def main():
    parser = argparse.ArgumentParser(
        description="Plan-011: Keyword routing accuracy analysis")
    parser.add_argument("--data_dirs", type=str, required=True,
                        help="Comma-separated data directories")
    parser.add_argument("--keywords", type=str,
                        default="src/rule_based_keywords_v2.json")
    parser.add_argument("--output", type=str,
                        default="results/rule_based_accuracy_report.json")
    parser.add_argument("--check_obs", action="store_true",
                        help="Also check observation text for keywords")
    args = parser.parse_args()

    keywords = load_keywords(args.keywords)
    print(f"Keywords ({len(keywords)}): {keywords}")

    data_dirs = [d.strip() for d in args.data_dirs.split(",") if d.strip()]

    all_results = []
    per_task = {}

    for data_dir in data_dirs:
        if not os.path.isdir(data_dir):
            print(f"SKIP: {data_dir} not found")
            continue

        dir_label = os.path.basename(data_dir.rstrip("/"))

        for task_name in sorted(os.listdir(data_dir)):
            task_dir = os.path.join(data_dir, task_name)
            ep_path = os.path.join(task_dir, "episodes.jsonl")
            if not os.path.isfile(ep_path):
                continue

            task_key = f"{dir_label}/{task_name}"
            task_results = []

            with open(ep_path) as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    episode = json.loads(line)
                    result = analyze_episode(episode, keywords,
                                             check_obs=args.check_obs)
                    result["task"] = task_name
                    result["data_dir"] = dir_label
                    task_results.append(result)

            if task_results:
                task_metrics = compute_metrics(task_results)
                avg_mr = (sum(r["keyword_match_rate"] for r in task_results)
                          / len(task_results))

                per_task[task_key] = {
                    "n_episodes": len(task_results),
                    "avg_keyword_match_rate": round(avg_mr, 4),
                    "metrics": task_metrics,
                    "episodes": task_results,
                }
                all_results.extend(task_results)

    if not all_results:
        print("No episodes found.")
        return

    overall = compute_metrics(all_results)
    avg_mr_all = sum(r["keyword_match_rate"] for r in all_results) / len(all_results)

    total_kw_hits = defaultdict(int)
    for r in all_results:
        for kw, cnt in r["keyword_hits"].items():
            total_kw_hits[kw] += cnt

    report = {
        "n_keywords": len(keywords),
        "keywords": keywords,
        "n_total_episodes": len(all_results),
        "avg_keyword_match_rate": round(avg_mr_all, 4),
        "check_observation": args.check_obs,
        "overall_metrics": overall,
        "top_keyword_hits": sorted(total_kw_hits.items(),
                                   key=lambda x: -x[1]),
        "per_task": {
            k: {kk: vv for kk, vv in v.items() if kk != "episodes"}
            for k, v in per_task.items()
        },
        "episode_details": all_results,
    }

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\nReport saved: {args.output}")

    # --- Terminal summary ---
    print(f"\n{'='*70}")
    print("KEYWORD ROUTING ACCURACY ANALYSIS")
    print(f"{'='*70}")
    print(f"Keywords: {len(keywords)}  |  Check obs: {args.check_obs}")
    print(f"Episodes: {len(all_results)}  |  "
          f"Avg keyword match rate: {avg_mr_all:.1%}")
    print()

    hdr = (f"{'Task':<45} {'Eps':>4} {'Match%':>7} "
           f"{'Acc':>6}  GT distribution")
    print(hdr)
    print("-" * 95)
    for task_key in sorted(per_task.keys()):
        t = per_task[task_key]
        m = t["metrics"]
        gt_cnt = defaultdict(int)
        for ep in t["episodes"]:
            gt_cnt[ep["ground_truth_label"]] += 1
        gt_str = "  ".join(f"{k}:{v}" for k, v in sorted(gt_cnt.items()))
        print(f"{task_key:<45} {t['n_episodes']:>4} "
              f"{t['avg_keyword_match_rate']:>6.1%} "
              f"{m['accuracy']:>5.1%}  {gt_str}")

    print()
    print(f"Overall accuracy (excl no-preference): "
          f"{overall['accuracy']:.1%} "
          f"({overall['n_correct']}/{overall['n_scorable']})")
    print()

    print("Confusion matrix  (rows=keyword_route, cols=ground_truth):")
    cm = overall["confusion_matrix"]
    gt_labels = sorted({gt for row in cm.values() for gt in row})
    print(f"{'':>20}" + "".join(f"{l:>18}" for l in gt_labels))
    for kw_label in ["det-preferred", "internal-preferred"]:
        row = cm.get(kw_label, {})
        vals = "".join(f"{row.get(gt, 0):>18}" for gt in gt_labels)
        print(f"{kw_label:>20}{vals}")
    print()

    print(f"{'Class':<20} {'Prec':>8} {'Rec':>8} {'F1':>8}")
    print("-" * 44)
    for cls in ["det-preferred", "internal-preferred"]:
        c = overall["class_metrics"][cls]
        print(f"{cls:<20} {c['precision']:>7.1%} {c['recall']:>7.1%} "
              f"{c['f1']:>7.1%}")

    if total_kw_hits:
        print(f"\nTop matched keywords:")
        for kw, cnt in sorted(total_kw_hits.items(),
                              key=lambda x: -x[1])[:10]:
            print(f"  {kw}: {cnt}")


if __name__ == "__main__":
    main()
