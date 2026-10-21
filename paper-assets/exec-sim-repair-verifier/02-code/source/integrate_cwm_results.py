# Integrate CWM eval results across seeds/models into Table 3, LaTeX, W5 CSV, and quality checks.
import argparse
import json
import math
import os
import sys
from pathlib import Path


CLS_REPO = {
    "Qwen3-8B": {42: 84.48, 123: 85.60, 456: 84.40},  # s42: cls8b-s42-resume-ckpt3600-test-v2
    "DeepSeek": {42: 82.61, 123: 74.93, 456: 86.15},   # s123=74.93 is known_outlier (NaN eval_loss)
}
TRAJ_REPO = {
    "Qwen3-8B": {42: 70.83, 123: 77.08, 456: 70.83},  # s42: qwen3-8b-traj-repo-s42-best-eval (D159)
    "DeepSeek": {42: 81.25, 123: 75.00, 456: 75.00},
}
SEEDS = [42, 123, 456]
SEED_SUFFIXES = ["s42", "s123", "s456"]
KNOWN_OUTLIERS = {("DeepSeek", "CLS", 123)}  # s123=74.93: NaN eval_loss during training


def load_eval(directory: str | None) -> dict | None:
    if directory is None:
        return None
    p = Path(directory) / "eval_repo_cwm.json"
    if not p.exists():
        print(f"WARNING: {p} not found, filling with NaN", file=sys.stderr)
        return None
    with open(p) as f:
        return json.load(f)


def mean_std_ci(vals: list[float]) -> tuple[float, float, float, float]:
    clean = [v for v in vals if not math.isnan(v)]
    if len(clean) == 0:
        return float("nan"), float("nan"), float("nan"), float("nan")
    mu = sum(clean) / len(clean)
    if len(clean) < 2:
        return mu, float("nan"), float("nan"), float("nan")
    var = sum((x - mu) ** 2 for x in clean) / (len(clean) - 1)
    sd = math.sqrt(var)
    # t critical value for 95% CI with df=2 (3 seeds)
    t_crit = 4.303
    margin = t_crit * sd / math.sqrt(len(clean))
    return mu, sd, mu - margin, mu + margin


def write_table3(models: dict, output_dir: Path):
    lines = ["=== Table 3: CWM Repo-level Results ===", ""]
    header = f"{'Model':<13}| {'s42':>6}  | {'s123':>6}  | {'s456':>6}  | {'Mean':>6}  | {'Std':>5}  | 95% CI"
    lines.append(header)
    for name, seeds in models.items():
        accs = [seeds[s].get("accuracy", float("nan")) if seeds[s] else float("nan") for s in SEEDS]
        mu, sd, lo, hi = mean_std_ci(accs)
        vals = [f"{v:6.2f}" if not math.isnan(v) else "   NaN" for v in accs]
        mu_s = f"{mu:6.2f}" if not math.isnan(mu) else "   NaN"
        sd_s = f"{sd:5.2f}" if not math.isnan(sd) else "  NaN"
        ci_s = f"[{lo:.2f}, {hi:.2f}]" if not math.isnan(lo) else "[NaN, NaN]"
        lines.append(f"{name:<13}| {vals[0]}  | {vals[1]}  | {vals[2]}  | {mu_s}  | {sd_s}  | {ci_s}")

    lines += ["", "Unparseable rates:"]
    for name, seeds in models.items():
        rates = [seeds[s].get("unparseable_rate", float("nan")) if seeds[s] else float("nan") for s in SEEDS]
        mu_r = sum(r for r in rates if not math.isnan(r)) / max(sum(1 for r in rates if not math.isnan(r)), 1)
        vals = [f"{v:5.1f}%" if not math.isnan(v) else "  NaN%" for v in rates]
        mu_s = f"{mu_r:5.1f}%" if not math.isnan(mu_r) else "  NaN%"
        lines.append(f"{name:<13}| {vals[0]} | {vals[1]} | {vals[2]} | {mu_s}")

    (output_dir / "table3_cwm.txt").write_text("\n".join(lines) + "\n")


def write_latex(models: dict, output_dir: Path):
    lines = ["% CWM rows for Table 3 - auto-generated"]
    for name, seeds in models.items():
        accs = [seeds[s].get("accuracy", float("nan")) if seeds[s] else float("nan") for s in SEEDS]
        mu, sd, _, _ = mean_std_ci(accs)
        mu_s = f"{mu:.2f}" if not math.isnan(mu) else "NaN"
        sd_s = f"{sd:.2f}" if not math.isnan(sd) else "NaN"
        lines.append(f"% {name} CWM")
        lines.append(f"{mu_s} {{\\small$\\pm${sd_s}}} &")
    (output_dir / "table3_cwm_latex.tex").write_text("\n".join(lines) + "\n")


def write_w5_csv(models: dict, output_dir: Path):
    rows = ["model,formulation,complexity,seed,accuracy,unparseable_rate"]
    for name, seeds in models.items():
        for s in SEEDS:
            d = seeds[s]
            acc = f"{d['accuracy']:.2f}" if d and "accuracy" in d else "NaN"
            upr = f"{d['unparseable_rate']:.2f}" if d and "unparseable_rate" in d else "NaN"
            rows.append(f"{name},CWM,repo,{s},{acc},{upr}")
    (output_dir / "w5_cwm_data.csv").write_text("\n".join(rows) + "\n")

    all_rows = ["model,formulation,complexity,seed,accuracy,unparseable_rate"]
    for name in ["Qwen3-8B", "DeepSeek"]:
        for s in SEEDS:
            all_rows.append(f"{name},CLS,repo,{s},{CLS_REPO[name][s]:.2f},0.00")
        for s in SEEDS:
            all_rows.append(f"{name},TRAJ,repo,{s},{TRAJ_REPO[name][s]:.2f},0.00")
        for s in SEEDS:
            d = models[name][s]
            acc = f"{d['accuracy']:.2f}" if d and "accuracy" in d else "NaN"
            upr = f"{d['unparseable_rate']:.2f}" if d and "unparseable_rate" in d else "NaN"
            all_rows.append(f"{name},CWM,repo,{s},{acc},{upr}")
    (output_dir / "w5_all_data.csv").write_text("\n".join(all_rows) + "\n")


def write_quality_check(models: dict, output_dir: Path):
    lines = ["=== Quality Check ===", ""]
    any_issue = False

    for name, seeds in models.items():
        lines.append(f"--- {name} ---")
        accs = {}
        for s in SEEDS:
            d = seeds[s]
            if d is None:
                lines.append(f"  seed {s}: MISSING")
                any_issue = True
                continue
            acc = d.get("accuracy", float("nan"))
            upr = d.get("unparseable_rate", float("nan"))
            accs[s] = acc

            if not math.isnan(upr) and upr > 50:
                lines.append(f"  seed {s}: unparseable_rate={upr:.1f}% > 50% (expected for CWM repo-level)")
            elif not math.isnan(upr):
                lines.append(f"  seed {s}: unparseable_rate={upr:.1f}% <= 50% — UNEXPECTEDLY LOW")
                any_issue = True

            if not math.isnan(acc) and not (40 <= acc <= 90):
                lines.append(f"  seed {s}: accuracy={acc:.2f} OUT OF RANGE [40, 90] — CHECK")
                any_issue = True

        if 42 in accs:
            baseline = accs[42]
            for s in [123, 456]:
                if s in accs and abs(accs[s] - baseline) > 15:
                    if (name, "CLS", s) in KNOWN_OUTLIERS or (name, "CWM", s) in KNOWN_OUTLIERS:
                        lines.append(f"  seed {s}: accuracy ({accs[s]:.2f}) deviates from s42 ({baseline:.2f}) — known_outlier, skipping alert")
                    else:
                        lines.append(f"  ANOMALY: seed {s} accuracy ({accs[s]:.2f}) differs from s42 ({baseline:.2f}) by >{15}pp")
                        any_issue = True
        lines.append("")

    if not any_issue:
        lines.append("All checks passed.")
    else:
        lines.append("Some checks flagged — review above.")

    (output_dir / "quality_check.txt").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Integrate CWM eval results across seeds and models.")
    parser.add_argument("--qwen_s42_dir", type=str, default=None)
    parser.add_argument("--qwen_s123_dir", type=str, default=None)
    parser.add_argument("--qwen_s456_dir", type=str, default=None)
    parser.add_argument("--deepseek_s42_dir", type=str, default=None)
    parser.add_argument("--deepseek_s123_dir", type=str, default=None)
    parser.add_argument("--deepseek_s456_dir", type=str, default=None)
    parser.add_argument("--output_dir", type=str, default="artifacts/cwm_integration/")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    qwen_dirs = [args.qwen_s42_dir, args.qwen_s123_dir, args.qwen_s456_dir]
    ds_dirs = [args.deepseek_s42_dir, args.deepseek_s123_dir, args.deepseek_s456_dir]

    models = {
        "Qwen3-8B": {s: load_eval(d) for s, d in zip(SEEDS, qwen_dirs)},
        "DeepSeek": {s: load_eval(d) for s, d in zip(SEEDS, ds_dirs)},
    }

    loaded = sum(1 for m in models.values() for v in m.values() if v is not None)
    print(f"Loaded {loaded}/6 eval results.")

    write_table3(models, output_dir)
    write_latex(models, output_dir)
    write_w5_csv(models, output_dir)
    write_quality_check(models, output_dir)

    print(f"Outputs written to {output_dir}/")
    for f in sorted(output_dir.iterdir()):
        print(f"  {f.name}")


if __name__ == "__main__":
    main()
