"""Generate LaTeX and Markdown tables from detector_formal_validation_v3.json."""
import json
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(SCRIPT_DIR, "..", "analysis", "detector_formal_validation_v3.json")


def load_data():
    with open(JSON_PATH) as f:
        return json.load(f)


def format_step(step):
    if step is None:
        return "--"
    return f"{step // 1000}K"


def format_ve(ve):
    if ve is None:
        return "--"
    return f"{ve:.2f}"


def generate_latex_table(data):
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{CIVO Detector Validation Results. Trigger Step indicates when the detector first fires. Detection Type classifies timing relative to 20\% eval decline from peak.}")
    lines.append(r"\label{tab:detector-validation}")
    lines.append(r"\resizebox{\columnwidth}{!}{%")
    lines.append(r"\begin{tabular}{llcccccc}")
    lines.append(r"\toprule")
    lines.append(r"Experiment & Config & Verdict & Trigger & Det. Type & Peak Eval & $r_\text{ve}$@trig \\")
    lines.append(r"\midrule")

    results = data["results"]
    for exp_id, r in results.items():
        if r.get("verdict") == "data_unavailable":
            continue

        config = r.get("config", "")
        if len(config) > 30:
            config = config[:28] + ".."

        verdict = r["verdict"]
        trigger = format_step(r["trigger_step"])
        det_type = r["detection_type"] if r["detection_type"] else "--"
        peak = f"{r['peak_eval_return']:.0f}" if r["peak_eval_return"] else "--"
        ve_trig = format_ve(r.get("ve_ratio_at_trigger"))

        exp_short = exp_id.replace("_", r"\_")

        lines.append(f"  {exp_short} & {config} & {verdict} & {trigger} & {det_type} & {peak} & {ve_trig} \\\\")

    lines.append(r"\midrule")

    summary = data["summary"]
    lines.append(f"  \\multicolumn{{7}}{{l}}{{TPR = {summary['TPR']}, FPR = {summary['FPR']}}} \\\\")

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}}")
    lines.append(r"\end{table}")
    return "\n".join(lines)


def generate_markdown_table(data):
    lines = []
    lines.append("| Experiment | Config | Verdict | Trigger | Det. Type | Peak Eval | ve_ratio@trig |")
    lines.append("|---|---|---|---|---|---|---|")

    results = data["results"]
    for exp_id, r in results.items():
        if r.get("verdict") == "data_unavailable":
            continue

        config = r.get("config", "")
        verdict = r["verdict"]
        trigger = format_step(r["trigger_step"])
        det_type = r["detection_type"] if r["detection_type"] else "--"
        peak = f"{r['peak_eval_return']:.0f}" if r["peak_eval_return"] else "--"
        ve_trig = format_ve(r.get("ve_ratio_at_trigger"))

        lines.append(f"| {exp_id} | {config} | {verdict} | {trigger} | {det_type} | {peak} | {ve_trig} |")

    lines.append("")
    summary = data["summary"]
    lines.append(f"**Summary**: TPR = {summary['TPR']}, FPR = {summary['FPR']}")
    lines.append(f"- TP: {summary['TP']}, FN: {summary['FN']}, TN: {summary['TN']}, FP: {summary['FP']}")
    lines.append(f"- Detection types: predictive={summary['detection_types']['predictive']}, "
                 f"reactive={summary['detection_types']['reactive']}, "
                 f"concurrent={summary['detection_types']['concurrent']}")
    lines.append(f"- Mean trigger step (TP): {format_step(summary['mean_trigger_step_TP'])}")
    lines.append(f"- Mean trigger step (FP): {format_step(summary['mean_trigger_step_FP'])}")
    return "\n".join(lines)


def print_summary(data):
    s = data["summary"]
    print("=" * 50)
    print("DETECTOR VALIDATION SUMMARY")
    print("=" * 50)
    print(f"  Evaluated experiments: {s['evaluated']}")
    print(f"  Positive cases:        {s['positive_cases']}")
    print(f"  Negative cases:        {s['negative_cases']}")
    print(f"  TP={s['TP']}  FN={s['FN']}  TN={s['TN']}  FP={s['FP']}")
    print(f"  TPR = {s['TPR']}")
    print(f"  FPR = {s['FPR']}")
    print(f"  TNR = {s['TNR']}")
    print(f"  Detection types: {s['detection_types']}")
    print("=" * 50)


def main():
    data = load_data()

    print_summary(data)

    print("\n\n### LaTeX Table ###\n")
    latex = generate_latex_table(data)
    print(latex)

    print("\n\n### Markdown Table ###\n")
    md = generate_markdown_table(data)
    print(md)

    out_dir = os.path.join(SCRIPT_DIR, "..", "analysis")
    latex_path = os.path.join(out_dir, "detector_table.tex")
    md_path = os.path.join(out_dir, "detector_table.md")

    with open(latex_path, "w") as f:
        f.write(latex + "\n")
    with open(md_path, "w") as f:
        f.write(md + "\n")

    print(f"\nWritten: {latex_path}")
    print(f"Written: {md_path}")


if __name__ == "__main__":
    main()
