"""Cross-seed comparison for generational spectral-collapse experiments.

Reads multiple per-seed JSON result files (each a JSON array of per-generation
records) and produces:
  1. A human-readable per-generation comparison table with deltas.
  2. A LaTeX mean±std summary table (Table 1 format).
  3. A JSON file with detected phase boundaries per seed.
"""

import argparse
import json
import math
from pathlib import Path

import numpy as np

METRICS = ["log_det", "effective_rank", "perplexity", "distinct_4"]
METRIC_DISPLAY = {
    "log_det": "SLV (log_det)",
    "effective_rank": "eff_rank",
    "perplexity": "ppl",
    "distinct_4": "distinct4",
}
METRIC_FMT = {
    "log_det": ".2f",
    "effective_rank": ".2f",
    "perplexity": ".2f",
    "distinct_4": ".4f",
}


def load_seed_data(path: str) -> list[dict]:
    """Load a single seed's generational JSON and return sorted by generation."""
    with open(path) as f:
        data = json.load(f)
    return sorted(data, key=lambda r: r["generation"])


def detect_phase_boundaries(records: list[dict], ppl_growth_threshold: float = 0.3) -> dict:
    """Detect three phase boundaries from a seed's generational data.

    Returns dict with:
      - decompression_peak: gen where log_det is maximal
      - onset: first gen after peak with 2 consecutive log_det decreases
      - collapse_confirmation: first gen where ppl growth rate > threshold
    """
    if not records:
        return {"decompression_peak": None, "onset": None, "collapse_confirmation": None}

    gens = [r["generation"] for r in records]
    slvs = [r["log_det"] for r in records]
    ppls = [r["perplexity"] for r in records]

    # decompression peak: argmax of log_det
    peak_idx = int(np.argmax(slvs))
    peak = {"gen": gens[peak_idx], "log_det": slvs[peak_idx]}

    # onset: first gen after peak where log_det decreases for 2 consecutive gens
    onset = None
    for i in range(peak_idx + 1, len(slvs) - 1):
        if slvs[i] < slvs[i - 1] and slvs[i + 1] < slvs[i]:
            onset = {"gen": gens[i], "log_det": slvs[i]}
            break

    # collapse confirmation: first gen where ppl growth rate exceeds threshold
    collapse = None
    for i in range(1, len(ppls)):
        if ppls[i - 1] > 0:
            growth = (ppls[i] - ppls[i - 1]) / ppls[i - 1]
            if growth > ppl_growth_threshold:
                collapse = {"gen": gens[i], "ppl": ppls[i], "ppl_growth": growth}
                break

    return {
        "decompression_peak": peak,
        "onset": onset,
        "collapse_confirmation": collapse,
    }


def build_comparison_table(all_data: dict[str, list[dict]], labels: list[str]) -> str:
    """Build a human-readable per-generation comparison table."""
    all_gens = sorted({r["generation"] for data in all_data.values() for r in data})

    # index by (label, gen)
    indexed = {}
    for label, records in all_data.items():
        for r in records:
            indexed[(label, r["generation"])] = r

    lines = []
    header_parts = ["Gen"]
    for m in METRICS:
        name = METRIC_DISPLAY[m]
        for label in labels:
            header_parts.append(f"{name}({label})")
        if len(labels) == 2:
            header_parts.append(f"Δ{name}")
            header_parts.append(f"%Δ{name}")

    sep = " | "
    header = sep.join(f"{h:>16s}" for h in header_parts)
    lines.append(header)
    lines.append("-" * len(header))

    for gen in all_gens:
        parts = [f"{gen:>16d}"]
        for m in METRICS:
            fmt = METRIC_FMT[m]
            vals = []
            for label in labels:
                key = (label, gen)
                if key in indexed and m in indexed[key]:
                    v = indexed[key][m]
                    vals.append(v)
                    parts.append(f"{v:>16{fmt}}")
                else:
                    vals.append(None)
                    parts.append(f"{'n/a':>16s}")

            if len(labels) == 2:
                if vals[0] is not None and vals[1] is not None:
                    delta = vals[1] - vals[0]
                    pct = (delta / abs(vals[0]) * 100) if vals[0] != 0 else float("inf")
                    parts.append(f"{delta:>+16{fmt}}")
                    parts.append(f"{pct:>+15.2f}%")
                else:
                    parts.append(f"{'n/a':>16s}")
                    parts.append(f"{'n/a':>16s}")

        lines.append(sep.join(parts))

    return "\n".join(lines)


def build_pairwise_tables(all_data: dict[str, list[dict]], labels: list[str]) -> str:
    """For 3+ seeds, produce pairwise delta tables."""
    sections = []
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            pair_data = {labels[i]: all_data[labels[i]], labels[j]: all_data[labels[j]]}
            section_title = f"\n=== Pairwise: {labels[i]} vs {labels[j]} ===\n"
            sections.append(section_title + build_comparison_table(pair_data, [labels[i], labels[j]]))
    return "\n".join(sections)


def build_latex_table(all_data: dict[str, list[dict]], labels: list[str]) -> str:
    """Build a LaTeX mean±std summary table across seeds."""
    all_gens = sorted({r["generation"] for data in all_data.values() for r in data})

    indexed = {}
    for label, records in all_data.items():
        for r in records:
            indexed[(label, r["generation"])] = r

    n_metrics = len(METRICS)
    col_spec = "c" + "c" * n_metrics
    header_cols = " & ".join(METRIC_DISPLAY[m] for m in METRICS)

    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Per-generation metrics (mean $\pm$ std across seeds).}",
        r"\label{tab:seed_comparison}",
        rf"\begin{{tabular}}{{{col_spec}}}",
        r"\toprule",
        rf"Gen & {header_cols} \\",
        r"\midrule",
    ]

    for gen in all_gens:
        row_parts = [str(gen)]
        for m in METRICS:
            fmt = METRIC_FMT[m]
            vals = []
            for label in labels:
                key = (label, gen)
                if key in indexed and m in indexed[key]:
                    vals.append(indexed[key][m])
            if vals:
                mean = np.mean(vals)
                std = np.std(vals, ddof=0) if len(vals) > 1 else 0.0
                if std < 1e-6:
                    row_parts.append(f"${mean:{fmt}}$")
                else:
                    row_parts.append(f"${mean:{fmt}} \\pm {std:{fmt}}$")
            else:
                row_parts.append("---")
        lines.append(" & ".join(row_parts) + r" \\")

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Compare generational metrics across seeds."
    )
    parser.add_argument(
        "--files", nargs="+", required=True,
        help="Paths to per-seed result JSON files.",
    )
    parser.add_argument(
        "--labels", nargs="+", default=None,
        help="Labels for each seed (must match --files count). Defaults to filenames.",
    )
    parser.add_argument(
        "--output-dir", default="results/comparison/",
        help="Output directory for results.",
    )
    parser.add_argument(
        "--ppl-threshold", type=float, default=0.3,
        help="PPL growth rate threshold for collapse confirmation (default: 0.3).",
    )
    args = parser.parse_args()

    if args.labels:
        if len(args.labels) != len(args.files):
            parser.error("--labels count must match --files count")
        labels = args.labels
    else:
        labels = [Path(f).stem for f in args.files]

    # Load data
    all_data = {}
    for label, fpath in zip(labels, args.files):
        all_data[label] = load_seed_data(fpath)
        print(f"Loaded {label}: {len(all_data[label])} generations")

    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # 1. Comparison table
    if len(labels) == 2:
        table_text = build_comparison_table(all_data, labels)
    else:
        table_text = build_comparison_table(all_data, labels)
        if len(labels) > 2:
            table_text += "\n\n" + build_pairwise_tables(all_data, labels)

    table_path = out_dir / "comparison_table.txt"
    table_path.write_text(table_text)
    print(f"Wrote {table_path}")

    # 2. Phase boundaries
    boundaries = {}
    for label in labels:
        boundaries[label] = detect_phase_boundaries(
            all_data[label], ppl_growth_threshold=args.ppl_threshold
        )

    # Consistency check
    peaks = [b["decompression_peak"]["gen"] for b in boundaries.values()
             if b["decompression_peak"] is not None]
    if peaks and len(set(peaks)) == 1:
        print(f"Phase boundary check: decompression peak consistent at gen {peaks[0]}")
    elif peaks:
        print(f"Phase boundary check: decompression peak VARIES across seeds: {peaks}")

    onsets = [b["onset"]["gen"] for b in boundaries.values() if b["onset"] is not None]
    if onsets and len(set(onsets)) == 1:
        print(f"Phase boundary check: onset consistent at gen {onsets[0]}")
    elif onsets:
        print(f"Phase boundary check: onset VARIES across seeds: {onsets}")
    else:
        print("Phase boundary check: onset not detected in any seed (insufficient data?)")

    boundaries_path = out_dir / "phase_boundaries.json"
    boundaries_path.write_text(json.dumps(boundaries, indent=2))
    print(f"Wrote {boundaries_path}")

    # 3. LaTeX mean±std table
    latex_text = build_latex_table(all_data, labels)
    latex_path = out_dir / "summary_mean_std.tex"
    latex_path.write_text(latex_text)
    print(f"Wrote {latex_path}")


if __name__ == "__main__":
    main()
