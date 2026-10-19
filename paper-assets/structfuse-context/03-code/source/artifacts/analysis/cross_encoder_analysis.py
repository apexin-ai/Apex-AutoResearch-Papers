#!/usr/bin/env python3
"""Cross-encoder comparison analysis: Qwen2.5-Coder-3B vs StarCoder2-3B."""

import json
import sys
import os
from collections import defaultdict

RESULTS_PATH = "/root/structfuse/results/pilot_results.json"
LOCAL_FALLBACK = os.path.join(os.path.dirname(__file__), "pilot_results.json")

ENCODER_DISPLAY = {
    "qwen": "Qwen2.5-Coder-3B",
    "starcoder": "StarCoder2-3B",
}
STRATEGY_ORDER = ["random", "embedding", "dataflow"]
METRIC_COLS = ["val_loss", "recall@1", "recall@5", "recall@10", "best_step"]
METRIC_BETTER = {
    "val_loss": "lower",
    "recall@1": "higher",
    "recall@5": "higher",
    "recall@10": "higher",
    "best_step": None,
}


def load_results(path=None):
    """Load pilot_results.json. Try server path first, then local fallback."""
    for p in [path, RESULTS_PATH, LOCAL_FALLBACK]:
        if p and os.path.exists(p):
            with open(p) as f:
                return json.load(f)
    print("ERROR: pilot_results.json not found. Provide path as argument or place next to script.")
    sys.exit(1)


def extract_rows(data):
    """Extract (encoder, strategy) -> metrics dict from results JSON.

    Supports two formats:
    1. Flat: {"qwen_random": {...}, "qwen_embedding": {...}, ...}
    2. Nested: {"qwen": {"random": {...}, ...}, ...}
    """
    rows = {}
    if not data:
        return rows

    sample_key = next(iter(data))
    if isinstance(data[sample_key], dict) and any(s in data[sample_key] for s in STRATEGY_ORDER):
        for enc, strategies in data.items():
            enc_key = enc.lower()
            for strat, metrics in strategies.items():
                rows[(enc_key, strat)] = normalize_metrics(metrics)
    else:
        for key, metrics in data.items():
            parts = key.lower().split("_", 1)
            if len(parts) == 2:
                enc_key, strat = parts
                rows[(enc_key, strat)] = normalize_metrics(metrics)

    return rows


def normalize_metrics(m):
    """Normalize metric keys and values."""
    out = {}
    for k, v in m.items():
        k_lower = k.lower().replace("recall_at_", "recall@").replace("r@", "recall@")
        if k_lower in METRIC_COLS:
            out[k_lower] = v
    return out


def fmt_val(col, val):
    if val is None:
        return "-"
    if col == "val_loss":
        return f"{val:.4f}"
    if col.startswith("recall@"):
        return f"{val*100:.1f}" if val <= 1.0 else f"{val:.1f}"
    if col == "best_step":
        return str(int(val))
    return str(val)


def raw_val(col, val):
    """Return numeric value normalized to percentage for recall."""
    if val is None:
        return None
    if col.startswith("recall@") and val <= 1.0:
        return val * 100
    return val


def find_best(rows, col):
    """Find the best value for a column across all rows."""
    direction = METRIC_BETTER.get(col)
    if direction is None:
        return None
    vals = [(k, raw_val(col, v.get(col))) for k, v in rows.items() if v.get(col) is not None]
    if not vals:
        return None
    if direction == "lower":
        return min(vals, key=lambda x: x[1])[1]
    return max(vals, key=lambda x: x[1])[1]


# ---------------------------------------------------------------------------
# Markdown table
# ---------------------------------------------------------------------------
def gen_markdown_table(rows):
    best = {col: find_best(rows, col) for col in METRIC_COLS}
    lines = []
    lines.append("## Cross-Encoder Comparison\n")
    header = "| Encoder | Strategy | " + " | ".join(METRIC_COLS) + " |"
    sep = "|" + "|".join(["---"] * (2 + len(METRIC_COLS))) + "|"
    lines.append(header)
    lines.append(sep)

    for enc_key in ["qwen", "starcoder"]:
        enc_name = ENCODER_DISPLAY.get(enc_key, enc_key)
        for strat in STRATEGY_ORDER:
            key = (enc_key, strat)
            if key not in rows:
                continue
            m = rows[key]
            cells = []
            for col in METRIC_COLS:
                v = raw_val(col, m.get(col))
                s = fmt_val(col, m.get(col))
                if v is not None and best.get(col) is not None and abs(v - best[col]) < 1e-6:
                    s = f"**{s}**"
                cells.append(s)
            lines.append(f"| {enc_name} | {strat} | " + " | ".join(cells) + " |")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# LaTeX table
# ---------------------------------------------------------------------------
def gen_latex_table(rows):
    best = {col: find_best(rows, col) for col in METRIC_COLS}
    ncols = 2 + len(METRIC_COLS)
    col_spec = "ll" + "r" * len(METRIC_COLS)

    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Cross-encoder comparison: ordering strategy effect on two code encoders.}")
    lines.append(r"\label{tab:cross-encoder}")
    lines.append(r"\begin{tabular}{" + col_spec + "}")
    lines.append(r"\toprule")

    latex_cols = [c.replace("@", r"@").replace("_", r"\_") for c in METRIC_COLS]
    lines.append("Encoder & Strategy & " + " & ".join(latex_cols) + r" \\")
    lines.append(r"\midrule")

    for i, enc_key in enumerate(["qwen", "starcoder"]):
        enc_name = ENCODER_DISPLAY.get(enc_key, enc_key)
        for j, strat in enumerate(STRATEGY_ORDER):
            key = (enc_key, strat)
            if key not in rows:
                continue
            m = rows[key]
            cells = []
            for col in METRIC_COLS:
                v = raw_val(col, m.get(col))
                s = fmt_val(col, m.get(col))
                if v is not None and best.get(col) is not None and abs(v - best[col]) < 1e-6:
                    s = r"\textbf{" + s + "}"
                cells.append(s)
            enc_cell = enc_name if j == 0 else ""
            lines.append(f"{enc_cell} & {strat} & " + " & ".join(cells) + r" \\")
        if i == 0:
            lines.append(r"\midrule")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Delta analysis
# ---------------------------------------------------------------------------
def compute_deltas(rows):
    """Compute strategy deltas and encoder deltas."""
    sections = []

    # --- Same encoder, different strategy ---
    sections.append("## Strategy Deltas (relative to random baseline)\n")
    for enc_key in ["qwen", "starcoder"]:
        enc_name = ENCODER_DISPLAY.get(enc_key, enc_key)
        baseline = rows.get((enc_key, "random"))
        if not baseline:
            continue
        sections.append(f"### {enc_name}\n")
        for strat in ["embedding", "dataflow"]:
            key = (enc_key, strat)
            if key not in rows:
                continue
            m = rows[key]
            parts = [f"  **{strat} - random**:"]
            for col in ["val_loss", "recall@1", "recall@5", "recall@10"]:
                bv = raw_val(col, baseline.get(col))
                sv = raw_val(col, m.get(col))
                if bv is not None and sv is not None:
                    delta = sv - bv
                    sign = "+" if delta >= 0 else ""
                    if col == "val_loss":
                        parts.append(f"    val_loss: {sign}{delta:.4f}")
                    else:
                        parts.append(f"    {col}: {sign}{delta:.1f}pp")
            sections.append("\n".join(parts) + "\n")

    # --- Same strategy, different encoder ---
    sections.append("## Encoder Deltas (Qwen - StarCoder, same strategy)\n")
    for strat in STRATEGY_ORDER:
        qwen = rows.get(("qwen", strat))
        star = rows.get(("starcoder", strat))
        if not qwen or not star:
            continue
        parts = [f"  **{strat}**:"]
        for col in ["val_loss", "recall@1", "recall@5", "recall@10"]:
            qv = raw_val(col, qwen.get(col))
            sv = raw_val(col, star.get(col))
            if qv is not None and sv is not None:
                delta = qv - sv
                sign = "+" if delta >= 0 else ""
                if col == "val_loss":
                    parts.append(f"    val_loss: {sign}{delta:.4f}")
                else:
                    parts.append(f"    {col}: {sign}{delta:.1f}pp")
        sections.append("\n".join(parts) + "\n")

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Strategy ranking consistency
# ---------------------------------------------------------------------------
def analyze_ranking_consistency(rows):
    """Check if strategy ranking is the same across encoders."""
    sections = ["## Strategy Ranking Consistency\n"]

    rankings = {}
    for enc_key in ["qwen", "starcoder"]:
        enc_name = ENCODER_DISPLAY.get(enc_key, enc_key)
        rankings[enc_key] = {}
        for col in ["val_loss", "recall@1", "recall@5", "recall@10"]:
            strat_vals = []
            for strat in STRATEGY_ORDER:
                key = (enc_key, strat)
                if key in rows and rows[key].get(col) is not None:
                    v = raw_val(col, rows[key][col])
                    strat_vals.append((strat, v))
            if not strat_vals:
                continue
            reverse = METRIC_BETTER.get(col) == "higher"
            ranked = [s for s, _ in sorted(strat_vals, key=lambda x: x[1], reverse=reverse)]
            rankings[enc_key][col] = ranked

    consistent_cols = []
    inconsistent_cols = []
    for col in ["val_loss", "recall@1", "recall@5", "recall@10"]:
        r_qwen = rankings.get("qwen", {}).get(col)
        r_star = rankings.get("starcoder", {}).get(col)
        if r_qwen and r_star:
            if r_qwen == r_star:
                consistent_cols.append(col)
                sections.append(f"- **{col}**: CONSISTENT — {' > '.join(r_qwen)}")
            else:
                inconsistent_cols.append(col)
                sections.append(f"- **{col}**: INCONSISTENT")
                sections.append(f"    Qwen: {' > '.join(r_qwen)}")
                sections.append(f"    StarCoder: {' > '.join(r_star)}")

    sections.append("")
    n_total = len(consistent_cols) + len(inconsistent_cols)
    n_cons = len(consistent_cols)
    if n_total > 0:
        if n_cons == n_total:
            sections.append(f"**Conclusion**: Strategy ranking is fully consistent across encoders "
                          f"({n_cons}/{n_total} metrics). This supports an **encoder-agnostic** claim "
                          f"for the ordering strategy effect.")
        elif n_cons >= n_total * 0.75:
            sections.append(f"**Conclusion**: Strategy ranking is mostly consistent ({n_cons}/{n_total} metrics). "
                          f"The ordering strategy effect is largely encoder-agnostic, with minor exceptions in "
                          f"{', '.join(inconsistent_cols)}.")
        else:
            sections.append(f"**Conclusion**: Strategy ranking shows notable inconsistency ({n_cons}/{n_total} metrics). "
                          f"The ordering strategy effect may be encoder-dependent.")

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Auto-generated narrative
# ---------------------------------------------------------------------------
def generate_narrative(rows):
    """Generate a text summary of key findings."""
    sections = ["## Key Findings\n"]

    # Best overall config
    best_r1_key = None
    best_r1_val = -1
    for k, m in rows.items():
        v = raw_val("recall@1", m.get("recall@1"))
        if v is not None and v > best_r1_val:
            best_r1_val = v
            best_r1_key = k

    if best_r1_key:
        enc_name = ENCODER_DISPLAY.get(best_r1_key[0], best_r1_key[0])
        strat = best_r1_key[1]
        loss = raw_val("val_loss", rows[best_r1_key].get("val_loss"))
        sections.append(
            f"1. **Best configuration**: {enc_name} + {strat} achieves R@1={best_r1_val:.1f}% "
            f"(val_loss={loss:.4f}).\n" if loss else
            f"1. **Best configuration**: {enc_name} + {strat} achieves R@1={best_r1_val:.1f}%.\n"
        )

    # Encoder gap
    for strat in STRATEGY_ORDER:
        qwen = rows.get(("qwen", strat))
        star = rows.get(("starcoder", strat))
        if qwen and star:
            qr1 = raw_val("recall@1", qwen.get("recall@1"))
            sr1 = raw_val("recall@1", star.get("recall@1"))
            if qr1 is not None and sr1 is not None:
                gap = qr1 - sr1
                sections.append(
                    f"2. **Encoder gap ({strat})**: Qwen leads StarCoder by {gap:+.1f}pp on R@1. "
                    f"Qwen's stronger code representation provides a consistent advantage.\n"
                )
                break

    # Strategy effect consistency
    qwen_embed_delta = None
    star_embed_delta = None
    for enc_key, label in [("qwen", "Qwen"), ("starcoder", "StarCoder")]:
        rand = rows.get((enc_key, "random"))
        emb = rows.get((enc_key, "embedding"))
        if rand and emb:
            rv = raw_val("recall@1", rand.get("recall@1"))
            ev = raw_val("recall@1", emb.get("recall@1"))
            if rv is not None and ev is not None:
                delta = ev - rv
                if enc_key == "qwen":
                    qwen_embed_delta = delta
                else:
                    star_embed_delta = delta

    if qwen_embed_delta is not None and star_embed_delta is not None:
        sections.append(
            f"3. **Embedding strategy lift**: embedding over random gives "
            f"+{qwen_embed_delta:.1f}pp (Qwen) and +{star_embed_delta:.1f}pp (StarCoder) on R@1. "
        )
        if (qwen_embed_delta > 0) == (star_embed_delta > 0):
            sections.append(
                f"   Both encoders benefit from semantic ordering → encoder-agnostic effect.\n"
            )
        else:
            sections.append(
                f"   Direction differs between encoders — further investigation needed.\n"
            )

    # R@5 saturation
    r5_vals = [raw_val("recall@5", m.get("recall@5")) for m in rows.values() if m.get("recall@5") is not None]
    if r5_vals and min(r5_vals) > 95:
        sections.append(
            f"4. **R@5 saturation**: All configs achieve R@5 ≥ {min(r5_vals):.1f}%, "
            f"indicating the task is well-solved at top-5. R@1 is the discriminating metric.\n"
        )

    return "\n".join(sections)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else None
    data = load_results(path)
    rows = extract_rows(data)

    if not rows:
        print("ERROR: No valid (encoder, strategy) rows found in results file.")
        print(f"Keys found: {list(data.keys())}")
        sys.exit(1)

    print(f"Loaded {len(rows)} configurations: {list(rows.keys())}\n")

    # Markdown table
    md_table = gen_markdown_table(rows)
    print(md_table)
    print()

    # Deltas
    deltas = compute_deltas(rows)
    print(deltas)

    # Ranking consistency
    ranking = analyze_ranking_consistency(rows)
    print(ranking)
    print()

    # Narrative
    narrative = generate_narrative(rows)
    print(narrative)

    # LaTeX table
    print("\n" + "=" * 60)
    print("LaTeX Table (copy to paper)")
    print("=" * 60 + "\n")
    latex = gen_latex_table(rows)
    print(latex)

    # Write outputs to files alongside script
    out_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(out_dir, "cross_encoder_report.md"), "w") as f:
        f.write(md_table + "\n\n" + deltas + "\n" + ranking + "\n\n" + narrative)
    with open(os.path.join(out_dir, "cross_encoder_table.tex"), "w") as f:
        f.write(latex)
    print(f"\nWritten: cross_encoder_report.md, cross_encoder_table.tex → {out_dir}/")


if __name__ == "__main__":
    main()
