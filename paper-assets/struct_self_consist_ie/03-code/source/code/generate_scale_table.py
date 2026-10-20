#!/usr/bin/env python3
"""Generate LaTeX scaling comparison table."""

import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

DATA = [
    {"model": "Qwen3-4B",     "size": "4B",  "regime": "FT", "dataset": "SciERC",
     "greedy": 0.6622, "oracle": 0.7925, "headroom": 13.03, "degen": 10.4,
     "lp_rho": None, "lp_delta": None, "constr_delta": None},
    {"model": "Qwen3-8B",     "size": "8B",  "regime": "FT", "dataset": "FewNERD",
     "greedy": 0.7481, "oracle": 0.8739, "headroom": 12.58, "degen": 12.69,
     "lp_rho": None, "lp_delta": 1.38, "constr_delta": None},
    {"model": "LLaMA-3.1-8B", "size": "8B",  "regime": "FT", "dataset": "FewNERD",
     "greedy": 0.7842, "oracle": 0.8843, "headroom": 10.01, "degen": 23.36,
     "lp_rho": None, "lp_delta": 0.36, "constr_delta": None},
    {"model": "Qwen2.5-72B",  "size": "72B", "regime": "ZS", "dataset": "SciERC",
     "greedy": 0.399,  "oracle": 0.549,  "headroom": 15.0,  "degen": None,
     "lp_rho": None, "lp_delta": None, "constr_delta": None},
    # === PLACEHOLDER ===
    # {"model": "Qwen2.5-7B",  "size": "7B",  "regime": "FT", "dataset": "FewNERD", ...},
    # {"model": "Qwen2.5-14B", "size": "14B", "regime": "FT", "dataset": "FewNERD", ...},
    # {"model": "Qwen2.5-32B", "size": "32B", "regime": "FT", "dataset": "FewNERD", ...},
]

NUMERIC_COLS = ["greedy", "oracle", "headroom", "degen", "lp_rho", "lp_delta", "constr_delta"]


def find_best(data: list[dict], col: str, higher_better: bool = True) -> float | None:
    vals = [d[col] for d in data if d.get(col) is not None]
    if not vals:
        return None
    return max(vals) if higher_better else min(vals)


def fmt_val(val, best_val, decimals=2, higher_better=True, bold=True):
    if val is None:
        return "--"
    s = f"{val:.{decimals}f}"
    if bold and best_val is not None and abs(val - best_val) < 1e-8:
        s = f"\\textbf{{{s}}}"
    return s


def generate_latex(data: list[dict]) -> str:
    best = {
        "greedy":       find_best(data, "greedy", True),
        "oracle":       find_best(data, "oracle", True),
        "headroom":     find_best(data, "headroom", True),
        "degen":        find_best(data, "degen", False),
        "lp_rho":       find_best(data, "lp_rho", True),
        "lp_delta":     find_best(data, "lp_delta", True),
        "constr_delta": find_best(data, "constr_delta", True),
    }

    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\small")
    lines.append(r"\setlength{\tabcolsep}{4pt}")
    lines.append(r"\begin{tabular}{llll rrr r rr r}")
    lines.append(r"\toprule")
    lines.append(r"Model & Size & Regime & Dataset & "
                 r"Greedy & Oracle & Head. & Degen & "
                 r"$\rho_{\text{LP}}$ & $\Delta_{\text{LP}}$ & $\Delta_{\text{C}}$ \\")
    lines.append(r" & & & & F1 & F1 & (pp) & (\%) & & (pp) & (pp) \\")
    lines.append(r"\midrule")

    for d in data:
        row = [
            d["model"].replace("_", r"\_"),
            d["size"],
            d["regime"],
            d["dataset"],
            fmt_val(d["greedy"],       best["greedy"],       4),
            fmt_val(d["oracle"],       best["oracle"],       4),
            fmt_val(d["headroom"],     best["headroom"],     2),
            fmt_val(d["degen"],        best["degen"],        2, higher_better=False),
            fmt_val(d.get("lp_rho"),   best["lp_rho"],      4),
            fmt_val(d.get("lp_delta"), best["lp_delta"],     2),
            fmt_val(d.get("constr_delta"), best["constr_delta"], 2),
        ]
        lines.append(" & ".join(row) + r" \\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\caption{Scaling comparison across model families and sizes. "
                 r"Head.\ = oracle headroom, Degen = degeneracy rate, "
                 r"$\rho_{\text{LP}}$ = log-prob signal Spearman correlation, "
                 r"$\Delta_{\text{LP}}$ = LP selection gain, "
                 r"$\Delta_{\text{C}}$ = entity construction gain. "
                 r"Best values per column in \textbf{bold}.}")
    lines.append(r"\label{tab:scaling}")
    lines.append(r"\end{table}")

    return "\n".join(lines)


def main():
    data_path = os.path.join(SCRIPT_DIR, "scaling_results.json")
    if os.path.exists(data_path):
        with open(data_path) as f:
            raw = json.load(f)
        data = []
        for r in raw:
            data.append({
                "model": r["model"],
                "size": f"{r['size_b']:.0f}B" if isinstance(r.get("size_b"), (int, float)) else r.get("size", "?"),
                "regime": "FT" if r.get("regime", "").startswith("fine") else "ZS",
                "dataset": r.get("dataset", "?"),
                "greedy": r.get("greedy_f1") or r.get("greedy"),
                "oracle": r.get("oracle_f1") or r.get("oracle"),
                "headroom": r.get("headroom_pp") or r.get("headroom"),
                "degen": r.get("degen_pct") or r.get("degen"),
                "lp_rho": r.get("lp_rho"),
                "lp_delta": r.get("lp_delta_pp") or r.get("lp_delta"),
                "constr_delta": r.get("constr_delta_pp") or r.get("constr_delta"),
            })
    else:
        data = DATA

    latex = generate_latex(data)
    print(latex)

    out_path = os.path.join(SCRIPT_DIR, "scale_table.tex")
    with open(out_path, "w") as f:
        f.write(latex + "\n")
    print(f"\nSaved: {out_path}", file=sys.stderr)


if __name__ == "__main__":
    main()
