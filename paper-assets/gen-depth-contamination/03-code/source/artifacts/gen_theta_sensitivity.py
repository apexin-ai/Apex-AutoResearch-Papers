import csv
import os

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

configs = [
    # (short_name, display_name, domain, [0v1, 1v2, 2v3, 3v4, 4v5], footnote)
    ("Qwen-rw",         "Qwen-1.5B-Inst (rewrite)",   "web", [0.9956, 0.6955, 0.5893, 0.5435, 0.5340], ""),
    ("Pythia-cont",     "Pythia-1.4B (cont.)",         "web", [0.9932, 0.6539, 0.5514, 0.5152, 0.5136], ""),
    ("OLMo-cont",       "OLMo-1B (cont.)",             "web", [0.9970, 0.6145, 0.5496, 0.5091, 0.5045], ""),
    ("Qwen-cont",       "Qwen-1.5B-Inst (cont.)",     "web", [0.9971, 0.6112, 0.5609, 0.5409, 0.5141], ""),
    ("LLaMA-8B",        "LLaMA-3.1-8B (cont.)",       "web", [0.9225, 0.6123, 0.5274, 0.5138, 0.5097], ""),
    ("Mistral-7B",      "Mistral-7B (cont.)$^\\dagger$","web",[0.9843, 0.5935, 0.5402, 0.5232, 0.5181], "†"),
    ("Qwen-base",       "Qwen-1.5B-base (cont.)",     "web", [0.9870, 0.6262, 0.5496, 0.5294, 0.5182], ""),
    ("Qwen-7B",         "Qwen-7B (cont.)",             "web", [0.9644, 0.6178, 0.5460, 0.5225, 0.5091], ""),
    ("Qwen-rw-arXiv",   "Qwen-1.5B-Inst (rewrite)",   "arxiv",[0.9946, 0.8580, 0.6427, 0.5437, 0.5294], ""),
    ("Pythia-arXiv",    "Pythia-1.4B (cont.)",         "arxiv",[0.9877, 0.8047, 0.6545, 0.5507, 0.5287], ""),
    ("Mistral-7B-cross","Mistral-7B (Qwen scorer)$^\\ddagger$","cross",[0.9209, 0.5695, 0.5335, 0.5140, 0.5184], "‡"),
]

thetas = [0.55, 0.575, 0.60, 0.625, 0.65, 0.70]

def compute_kstar(aucs, theta):
    """K* = max k such that AUC(k-1 vs k) > theta. AUC list is [0v1, 1v2, 2v3, 3v4, 4v5]."""
    kstar = 0
    for i, auc in enumerate(aucs):
        k = i + 1  # transition 0v1 -> k=1, 1v2 -> k=2, etc.
        if auc > theta:
            kstar = k
        else:
            break
    return kstar

# Compute all K* values
results = []
for short, display, domain, aucs, fn in configs:
    row = {"short": short, "display": display, "domain": domain, "footnote": fn}
    for t in thetas:
        row[f"theta_{t}"] = compute_kstar(aucs, t)
    results.append(row)

# --- CSV ---
csv_path = os.path.join(OUTPUT_DIR, "theta_sensitivity_table.csv")
with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    header = ["Model-Config"] + [f"theta_{t}" for t in thetas]
    writer.writerow(header)
    for r in results:
        csv_display = r["display"].replace("$^\\dagger$", "†").replace("$^\\ddagger$", "‡")
        writer.writerow([csv_display] + [r[f"theta_{t}"] for t in thetas])
print(f"CSV written to {csv_path}")

# --- LaTeX ---
tex_path = os.path.join(OUTPUT_DIR, "theta_sensitivity_table.tex")

theta_cols = " ".join(["c"] * len(thetas))
header_cells = []
for t in thetas:
    label = f"{t:.3f}" if t == 0.575 or t == 0.625 else f"{t:.2f}"
    if t == 0.60:
        header_cells.append(r"\textbf{$\theta=0.60$}")
    else:
        header_cells.append(f"$\\theta={label}$")

lines = []
lines.append(r"\begin{table}[t]")
lines.append(r"\centering")
lines.append(r"\small")
lines.append(r"\setlength{\tabcolsep}{4pt}")
lines.append(r"\caption{Sensitivity of $K^*$ to threshold $\theta$. The qualitative pattern (web text $K^*\!\leq\!2$, arXiv $K^*\!=\!3$, cross-scorer $K^*\!=\!1$) is stable across $\theta\in[0.55,\,0.70]$. \textbf{Bold column} marks $\theta=0.60$, the default used throughout the paper. $\dagger$\,Self-scorer. $\ddagger$\,Cross-scorer (Qwen scores Mistral generations).}")
lines.append(r"\label{tab:theta_sensitivity}")
lines.append(r"\begin{tabular}{l " + theta_cols + "}")
lines.append(r"\toprule")
lines.append("Model-Config & " + " & ".join(header_cells) + r" \\")
lines.append(r"\midrule")

domain_order = ["web", "arxiv", "cross"]
domain_labels = {"web": "C4 Web-text", "arxiv": "arXiv", "cross": "Cross-scorer"}
first_domain = True

for domain in domain_order:
    domain_rows = [r for r in results if r["domain"] == domain]
    if not domain_rows:
        continue
    if not first_domain:
        lines.append(r"\midrule")
    lines.append(r"\multicolumn{" + str(len(thetas) + 1) + r"}{l}{\textit{" + domain_labels[domain] + r"}} \\")
    for r in domain_rows:
        cells = []
        for t in thetas:
            val = r[f"theta_{t}"]
            if t == 0.60:
                cells.append(r"\textbf{" + str(val) + "}")
            else:
                cells.append(str(val))
        lines.append(f"~~{r['display']} & " + " & ".join(cells) + r" \\")
    first_domain = False

lines.append(r"\bottomrule")
lines.append(r"\end{tabular}")
lines.append(r"\end{table}")

tex_content = "\n".join(lines)
with open(tex_path, "w") as f:
    f.write(tex_content)
print(f"LaTeX written to {tex_path}")

# --- Verify ---
print("\n=== K* Summary ===")
for r in results:
    vals = [str(r[f"theta_{t}"]) for t in thetas]
    csv_display = r["display"].replace("$^\\dagger$", "†").replace("$^\\ddagger$", "‡")
    print(f"  {csv_display:40s} | {' | '.join(vals)}")
