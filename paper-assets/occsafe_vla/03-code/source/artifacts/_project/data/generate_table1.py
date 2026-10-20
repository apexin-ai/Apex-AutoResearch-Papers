#!/usr/bin/env python3
"""Generate Table 1 for the 2x2 factorial study (gradient_flow x norm_type).

Usage:
  python generate_table1.py --demo                          # use built-in data
  python generate_table1.py --data-json results.json        # use external data
  python generate_table1.py --demo --format markdown        # markdown output
  python generate_table1.py --demo --format latex           # latex output (default)

Input JSON schema:
  {
    "vanilla":  {"car": [...], "tsr": [...]},
    "cell_1":   {"car": [...], "tsr": [...]},   // Full OCC BN  (ON+BN)
    "cell_2":   {"car": [...], "tsr": [...]},   // Full OCC LN  (ON+LN)
    "cell_3":   {"car": [...], "tsr": [...]},   // Detach BN    (OFF+BN)
    "cell_4":   {"car": [...], "tsr": [...]},   // Detach LN    (OFF+LN)
  }
"""

import argparse
import json
import sys
import numpy as np

DEMO_DATA = {
    "vanilla": {"car": [0.768], "tsr": [0.900]},
    "cell_1":  {"car": [0.746, 0.654, 0.776], "tsr": [0.802, 0.854, 0.906]},
    "cell_2":  {"car": [], "tsr": []},
    "cell_3":  {"car": [0.774, 0.736, 0.762, 0.794], "tsr": [0.870, 0.926, 0.914, 0.922]},
    "cell_4":  {"car": [], "tsr": []},
}

CELL_META = [
    ("vanilla", "Vanilla (no OCC)", "—", "—"),
    ("cell_1",  "Full OCC BN",      "ON",  "BN"),
    ("cell_2",  "Full OCC LN",      "ON",  "LN"),
    ("cell_3",  "Detach BN",        "OFF", "BN"),
    ("cell_4",  "Detach LN",        "OFF", "LN"),
]


def fmt_mean_std(values):
    if not values:
        return "—", None
    arr = np.array(values, dtype=float)
    m = arr.mean()
    if len(arr) == 1:
        return f"{m:.3f}", m
    s = arr.std(ddof=1)
    return f"{m:.3f}±{s:.3f}", m


def build_rows(data):
    vanilla_car = data.get("vanilla", {}).get("car", [])
    baseline_car = np.mean(vanilla_car) if vanilla_car else None

    rows = []
    best_car = -1.0
    best_tsr = -1.0

    for key, label, gf, nt in CELL_META:
        cell = data.get(key, {"car": [], "tsr": []})
        car_vals = cell.get("car", [])
        tsr_vals = cell.get("tsr", [])
        n = len(car_vals)

        tsr_str, tsr_mean = fmt_mean_std(tsr_vals)
        car_str, car_mean = fmt_mean_std(car_vals)

        if car_mean is not None and baseline_car is not None and key != "vanilla":
            delta = car_mean - baseline_car
            delta_str = f"{delta:+.3f}"
        elif key == "vanilla":
            delta_str = "—"
        else:
            delta_str = "—"

        if car_mean is not None and car_mean > best_car:
            best_car = car_mean
        if tsr_mean is not None and tsr_mean > best_tsr:
            best_tsr = tsr_mean

        rows.append({
            "key": key, "label": label, "gf": gf, "nt": nt,
            "n": n if n > 0 else "—",
            "tsr_str": tsr_str, "tsr_mean": tsr_mean,
            "car_str": car_str, "car_mean": car_mean,
            "delta_str": delta_str,
        })

    return rows, best_car, best_tsr


def bold_if_best(val_str, val_mean, best_val, fmt="latex"):
    if val_mean is None or best_val is None:
        return val_str
    if abs(val_mean - best_val) < 1e-6:
        if fmt == "latex":
            return f"\\textbf{{{val_str}}}"
        else:
            return f"**{val_str}**"
    return val_str


def generate_latex(data):
    rows, best_car, best_tsr = build_rows(data)
    lines = [
        r"\begin{table}[t]",
        r"\centering",
        r"\caption{Task success rate (TSR) and collision avoidance rate (CAR) across conditions in the 2$\times$2 factorial design (gradient flow $\times$ normalization type). Mean$\pm$std over $n$ seeds. Best values in \textbf{bold}.}",
        r"\label{tab:factorial_results}",
        r"\begin{tabular}{lcccc}",
        r"\toprule",
        r"Condition & $n$ & TSR $\uparrow$ & CAR $\uparrow$ & $\Delta$CAR \\",
        r"\midrule",
    ]

    for i, r in enumerate(rows):
        tsr = bold_if_best(r["tsr_str"], r["tsr_mean"], best_tsr, "latex")
        car = bold_if_best(r["car_str"], r["car_mean"], best_car, "latex")
        line = f"{r['label']} & {r['n']} & {tsr} & {car} & {r['delta_str']} \\\\"
        lines.append(line)
        if i == 0:
            lines.append(r"\midrule")

    lines.extend([
        r"\bottomrule",
        r"\end{tabular}",
        r"\end{table}",
    ])
    return "\n".join(lines)


def generate_markdown(data):
    rows, best_car, best_tsr = build_rows(data)
    lines = [
        "| Condition | n | TSR ↑ | CAR ↑ | ΔCAR |",
        "|-----------|---|-------|-------|------|",
    ]
    for r in rows:
        tsr = bold_if_best(r["tsr_str"], r["tsr_mean"], best_tsr, "markdown")
        car = bold_if_best(r["car_str"], r["car_mean"], best_car, "markdown")
        lines.append(f"| {r['label']} | {r['n']} | {tsr} | {car} | {r['delta_str']} |")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate Table 1 for factorial study")
    parser.add_argument("--data-json", type=str, help="Path to JSON with CAR/TSR data")
    parser.add_argument("--demo", action="store_true", help="Use built-in demo data")
    parser.add_argument("--format", choices=["latex", "markdown"], default="latex")
    args = parser.parse_args()

    if args.demo:
        data = DEMO_DATA
    elif args.data_json:
        with open(args.data_json) as f:
            data = json.load(f)
    else:
        parser.error("Provide --data-json or --demo")
        sys.exit(1)

    if args.format == "latex":
        print(generate_latex(data))
    else:
        print(generate_markdown(data))


if __name__ == "__main__":
    main()
