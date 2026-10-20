# Evaluation metrics: SVS vs Self-Consistency accuracy, agreement, per-label breakdown, confusion matrix.

from __future__ import annotations

from collections import defaultdict

from svs_pipeline.types import SVSResult

LABELS = ["True", "False", "Unknown"]


def evaluate_results(results: list[SVSResult]) -> dict:
    n = len(results)
    if n == 0:
        return {"n": 0, "svs_accuracy": 0.0, "sc_accuracy": 0.0, "delta": 0.0,
                "svs_correct": 0, "sc_correct": 0, "both_correct": 0,
                "svs_only_correct": 0, "sc_only_correct": 0, "both_wrong": 0,
                "agreement_rate": 0.0, "per_label": {}, "confusion": {}}

    svs_correct = sum(r.correct_svs for r in results)
    sc_correct = sum(r.correct_sc for r in results)
    both_correct = sum(r.correct_svs and r.correct_sc for r in results)
    svs_only = sum(r.correct_svs and not r.correct_sc for r in results)
    sc_only = sum(not r.correct_svs and r.correct_sc for r in results)
    both_wrong = sum(not r.correct_svs and not r.correct_sc for r in results)
    agreement = sum(r.selected_answer == r.sc_answer for r in results)

    svs_acc = svs_correct / n
    sc_acc = sc_correct / n

    # per-label breakdown
    per_label: dict[str, dict] = {}
    by_label: dict[str, list[SVSResult]] = defaultdict(list)
    for r in results:
        by_label[r.gold_label].append(r)
    for label in LABELS:
        group = by_label[label]
        gn = len(group)
        if gn == 0:
            per_label[label] = {"n": 0, "svs_acc": 0.0, "sc_acc": 0.0}
        else:
            per_label[label] = {
                "n": gn,
                "svs_acc": sum(r.correct_svs for r in group) / gn,
                "sc_acc": sum(r.correct_sc for r in group) / gn,
            }

    # confusion matrix: predicted -> {gold: count}
    confusion: dict[str, dict[str, int]] = {
        p: {g: 0 for g in LABELS} for p in LABELS
    }
    for r in results:
        if r.selected_answer in confusion and r.gold_label in LABELS:
            confusion[r.selected_answer][r.gold_label] += 1

    return {
        "n": n,
        "svs_accuracy": svs_acc,
        "sc_accuracy": sc_acc,
        "delta": svs_acc - sc_acc,
        "svs_correct": svs_correct,
        "sc_correct": sc_correct,
        "both_correct": both_correct,
        "svs_only_correct": svs_only,
        "sc_only_correct": sc_only,
        "both_wrong": both_wrong,
        "agreement_rate": agreement / n,
        "per_label": per_label,
        "confusion": confusion,
    }


def format_report(metrics: dict) -> str:
    if metrics["n"] == 0:
        return "No results to report."

    lines = [
        f"=== SVS Evaluation Report (n={metrics['n']}) ===",
        "",
        f"SVS accuracy:  {metrics['svs_accuracy']:.4f}  ({metrics['svs_correct']}/{metrics['n']})",
        f"SC  accuracy:  {metrics['sc_accuracy']:.4f}  ({metrics['sc_correct']}/{metrics['n']})",
        f"Delta (SVS-SC): {metrics['delta']:+.4f}",
        f"Agreement rate:  {metrics['agreement_rate']:.4f}",
        "",
        "--- Overlap ---",
        f"Both correct:      {metrics['both_correct']}",
        f"SVS only correct:  {metrics['svs_only_correct']}",
        f"SC  only correct:  {metrics['sc_only_correct']}",
        f"Both wrong:        {metrics['both_wrong']}",
    ]

    if metrics["per_label"]:
        lines += ["", "--- Per Label ---"]
        for label, info in metrics["per_label"].items():
            if info["n"] > 0:
                lines.append(
                    f"  {label:>7s}  n={info['n']:<4d}  svs={info['svs_acc']:.4f}  sc={info['sc_acc']:.4f}"
                )

    if metrics["confusion"]:
        lines += ["", "--- Confusion (SVS predicted -> gold) ---"]
        lines.append(f"  {'pred\\gold':>10s}  {'True':>6s}  {'False':>6s}  {'Unknown':>7s}")
        for pred in LABELS:
            row = metrics["confusion"].get(pred, {})
            lines.append(
                f"  {pred:>10s}  {row.get('True',0):>6d}  {row.get('False',0):>6d}  {row.get('Unknown',0):>7d}"
            )

    return "\n".join(lines)
