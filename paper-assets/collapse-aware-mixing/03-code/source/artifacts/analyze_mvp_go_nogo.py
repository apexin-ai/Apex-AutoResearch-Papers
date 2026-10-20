"""
MVP GO/NO-GO 自动评估脚本

读取 v7 pipeline 输出的 3 代 metrics，按 D008 决策树自动判定 GO/NO-GO。
输入: --output-dir 指向 pipeline 输出根目录（默认 /root/autodl-tmp/output_v7/）
输出: stdout 报告 + go_nogo_report.json

依赖: numpy（纯 CPU，不需要 torch）
"""

import argparse
import glob
import json
import os
import sys
from pathlib import Path

import numpy as np


def find_metrics_files(output_dir: str) -> dict:
    """扫描 G0/G1/G2 目录，发现 metrics 文件。

    支持多种命名模式:
    - G{i}/evaluation/checkpoint-{step}/metrics.json
    - G{i}/evaluation/metrics.json (合并格式)
    - G{i}/evaluation/metrics.jsonl
    - G{i}/evaluation/*.json
    """
    results = {}
    for gen_idx in range(10):
        gen_dir = os.path.join(output_dir, f"G{gen_idx}")
        if not os.path.isdir(gen_dir):
            break

        eval_dir = os.path.join(gen_dir, "evaluation")
        if not os.path.isdir(eval_dir):
            results[f"G{gen_idx}"] = {"status": "no_evaluation_dir", "checkpoints": {}}
            continue

        checkpoints = {}

        # Pattern 1: per-checkpoint subdirectories
        for ckpt_dir in sorted(glob.glob(os.path.join(eval_dir, "checkpoint-*"))):
            step = os.path.basename(ckpt_dir).replace("checkpoint-", "")
            for fname in ["metrics.json", "eval_metrics.json"]:
                fpath = os.path.join(ckpt_dir, fname)
                if os.path.isfile(fpath):
                    checkpoints[int(step)] = load_json(fpath)
                    break

        # Pattern 2: single metrics file with all checkpoints
        if not checkpoints:
            for fname in ["metrics.json", "all_metrics.json", "evaluation_results.json"]:
                fpath = os.path.join(eval_dir, fname)
                if os.path.isfile(fpath):
                    data = load_json(fpath)
                    if isinstance(data, dict) and all(isinstance(v, dict) for v in data.values()):
                        for k, v in data.items():
                            step = int(k.replace("checkpoint-", "").replace("checkpoint_", ""))
                            checkpoints[step] = v
                    elif isinstance(data, dict):
                        checkpoints[0] = data
                    break

        # Pattern 3: JSONL format
        if not checkpoints:
            for fname in ["metrics.jsonl", "eval_metrics.jsonl"]:
                fpath = os.path.join(eval_dir, fname)
                if os.path.isfile(fpath):
                    with open(fpath) as f:
                        for line in f:
                            line = line.strip()
                            if not line:
                                continue
                            entry = json.loads(line)
                            step = entry.get("step", entry.get("checkpoint_step", len(checkpoints)))
                            checkpoints[step] = entry
                    break

        # Pattern 4: individual JSON files named by step
        if not checkpoints:
            for fpath in sorted(glob.glob(os.path.join(eval_dir, "*.json"))):
                fname = os.path.basename(fpath)
                data = load_json(fpath)
                if data and isinstance(data, dict):
                    step_str = fname.replace(".json", "").replace("checkpoint-", "").replace("ckpt_", "")
                    try:
                        step = int(step_str)
                    except ValueError:
                        step = len(checkpoints)
                    checkpoints[step] = data

        status = "complete" if checkpoints else "no_metrics"
        results[f"G{gen_idx}"] = {"status": status, "checkpoints": checkpoints}

    return results


def load_json(path: str) -> dict:
    try:
        with open(path) as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def extract_metric(checkpoint_data: dict, metric_name: str) -> float | None:
    """从 checkpoint metrics 中提取指定指标，处理不同命名约定。"""
    aliases = {
        "eff_rank": ["eff_rank", "effective_rank", "spectral_effective_rank", "rank"],
        "ppl": ["ppl", "perplexity", "eval_ppl", "holdout_ppl"],
        "entropy_var": ["entropy_var", "token_entropy_variance", "entropy_variance"],
        "coverage": ["coverage", "vocab_coverage", "vocabulary_coverage"],
        "kl_divergence": ["kl_divergence", "kl_div", "inter_gen_kl", "logit_kl"],
        "unigram_H": ["unigram_H", "unigram_entropy", "ngram_entropy"],
    }
    for alias in aliases.get(metric_name, [metric_name]):
        if alias in checkpoint_data:
            val = checkpoint_data[alias]
            if val is not None:
                return float(val)
    return None


def get_final_checkpoint(gen_data: dict) -> tuple[int, dict] | None:
    """获取某代的 final checkpoint（最大 step）。"""
    ckpts = gen_data.get("checkpoints", {})
    if not ckpts:
        return None
    max_step = max(ckpts.keys())
    return max_step, ckpts[max_step]


def compute_sigma(gen_data: dict) -> float:
    """计算 G0 训练 checkpoints 的 eff_rank 标准差（排除 final 作为 baseline）。"""
    ckpts = gen_data.get("checkpoints", {})
    if len(ckpts) < 2:
        return 0.0
    ranks = []
    for step in sorted(ckpts.keys()):
        r = extract_metric(ckpts[step], "eff_rank")
        if r is not None:
            ranks.append(r)
    if len(ranks) < 2:
        return 0.0
    return float(np.std(ranks, ddof=1))


def check_spectral_leading(
    checkpoint_data: dict,
    baseline_rank: float,
    baseline_ppl: float,
    sigma: float,
    sigma_mult: float,
    ppl_threshold: float,
    ppl_pct_threshold: float,
) -> bool:
    """判断某个 checkpoint 是否满足谱领先性条件。"""
    rank = extract_metric(checkpoint_data, "eff_rank")
    ppl = extract_metric(checkpoint_data, "ppl")
    if rank is None or ppl is None:
        return False

    rank_drop = baseline_rank - rank
    ppl_rise = ppl - baseline_ppl
    ppl_pct_rise = ppl_rise / baseline_ppl if baseline_ppl > 0 else 0.0

    # eff_rank 下降 ≥ sigma_mult * σ
    rank_condition = rank_drop >= sigma_mult * sigma and sigma > 0
    # PPL 未显著上升
    ppl_condition = ppl_rise < ppl_threshold and ppl_pct_rise < ppl_pct_threshold

    return rank_condition and ppl_condition


def determine_verdict(
    all_data: dict,
    sigma: float,
    args,
) -> tuple[str, str]:
    """D008 决策树判定。"""
    g0_final = get_final_checkpoint(all_data.get("G0", {}))
    if g0_final is None:
        return "INCOMPLETE", "G0 数据缺失，无法判定"

    _, g0_metrics = g0_final
    baseline_rank = extract_metric(g0_metrics, "eff_rank")
    baseline_ppl = extract_metric(g0_metrics, "ppl")

    if baseline_rank is None or baseline_ppl is None:
        return "INCOMPLETE", f"G0 final 缺少 eff_rank 或 ppl（rank={baseline_rank}, ppl={baseline_ppl}）"

    has_spectral_lead = False
    leading_checkpoints = []
    all_ranks = []
    all_ppls = []
    gen_final_ranks = [baseline_rank]
    gen_final_ppls = [baseline_ppl]
    kl_values = []

    for gen_name in ["G1", "G2"]:
        gen_data = all_data.get(gen_name, {})
        ckpts = gen_data.get("checkpoints", {})
        if not ckpts:
            continue

        for step in sorted(ckpts.keys()):
            ckpt = ckpts[step]
            r = extract_metric(ckpt, "eff_rank")
            p = extract_metric(ckpt, "ppl")
            if r is not None:
                all_ranks.append(r)
            if p is not None:
                all_ppls.append(p)

            if check_spectral_leading(
                ckpt, baseline_rank, baseline_ppl, sigma,
                args.sigma_multiplier, args.ppl_threshold, args.ppl_pct_threshold,
            ):
                has_spectral_lead = True
                leading_checkpoints.append(f"{gen_name}/checkpoint-{step}")

        gen_final = get_final_checkpoint(gen_data)
        if gen_final:
            _, gf_metrics = gen_final
            fr = extract_metric(gf_metrics, "eff_rank")
            fp = extract_metric(gf_metrics, "ppl")
            if fr is not None:
                gen_final_ranks.append(fr)
            if fp is not None:
                gen_final_ppls.append(fp)

            kl = extract_metric(gf_metrics, "kl_divergence")
            if kl is not None:
                kl_values.append(kl)

    kl_above = any(kl > args.kl_threshold for kl in kl_values)

    # 跨代单调下降
    rank_trending = len(gen_final_ranks) >= 2 and all(
        gen_final_ranks[i] > gen_final_ranks[i + 1] for i in range(len(gen_final_ranks) - 1)
    )

    # CV 对比
    rank_cv = float(np.std(gen_final_ranks) / np.mean(gen_final_ranks)) if len(gen_final_ranks) >= 2 and np.mean(gen_final_ranks) != 0 else float("inf")
    ppl_cv = float(np.std(gen_final_ppls) / np.mean(gen_final_ppls)) if len(gen_final_ppls) >= 2 and np.mean(gen_final_ppls) != 0 else float("inf")
    rank_cv_smaller = rank_cv < ppl_cv

    # 是否有 collapse 信号（任一代的 eff_rank 相对 G0 下降 ≥0.5% 或 PPL 上升 ≥1pt）
    has_collapse_signal = False
    if len(gen_final_ranks) >= 2:
        rank_change_pct = (gen_final_ranks[-1] - baseline_rank) / baseline_rank if baseline_rank != 0 else 0
        ppl_change = gen_final_ppls[-1] - baseline_ppl if len(gen_final_ppls) >= 2 else 0
        has_collapse_signal = rank_change_pct < -0.005 or ppl_change > 1.0

    # PPL 先于 eff_rank 下降检测
    ppl_leads = False
    if len(gen_final_ranks) >= 2 and len(gen_final_ppls) >= 2:
        ppl_rose = gen_final_ppls[-1] > baseline_ppl + args.ppl_threshold
        rank_stable = abs(gen_final_ranks[-1] - baseline_rank) < sigma
        ppl_leads = ppl_rose and rank_stable

    # 决策树
    if has_spectral_lead and kl_above:
        return "GO", (
            f"谱领先性成立（{len(leading_checkpoints)} 个 checkpoint: {', '.join(leading_checkpoints)}）"
            f"+ KL>{args.kl_threshold}，primary framing 可行"
        )
    elif has_spectral_lead and not kl_above and rank_trending:
        return "Conditional GO", (
            f"谱领先但 KL<{args.kl_threshold}，eff_rank 跨代下降趋势明确 "
            f"({' → '.join(f'{r:.1f}' for r in gen_final_ranks)})"
        )
    elif not has_spectral_lead and rank_cv_smaller and has_collapse_signal:
        return "Conditional GO", (
            f"eff_rank 与 PPL 同步变化但 CV 更小 (rank_cv={rank_cv:.4f} < ppl_cv={ppl_cv:.4f})，"
            f"secondary framing: higher-resolution indicator"
        )
    elif ppl_leads:
        return "KILL", (
            f"PPL 先于 eff_rank 上升（PPL: {baseline_ppl:.2f}→{gen_final_ppls[-1]:.2f}，"
            f"rank: {baseline_rank:.1f}→{gen_final_ranks[-1]:.1f} 无显著变化），谱指标对 autoregressive LLM collapse 无效"
        )
    elif not has_collapse_signal:
        rank_delta_str = f"{gen_final_ranks[-1] - baseline_rank:.1f}" if len(gen_final_ranks) >= 2 else "N/A"
        ppl_delta_str = f"{gen_final_ppls[-1] - baseline_ppl:.2f}" if len(gen_final_ppls) >= 2 else "N/A"
        return "NO-GO (延展)", (
            f"3 代无明显 collapse 信号（rank Δ={rank_delta_str}，PPL Δ={ppl_delta_str}）。"
            f"建议加 1 代 50M tokens 观察"
        )
    else:
        return "NO-GO (延展)", (
            f"谱领先性未确立（σ={sigma:.2f}，无 checkpoint 满足 rank 下降 ≥{args.sigma_multiplier}σ + PPL 未上升条件）。"
            f"建议加 1 代 50M tokens 或调整阈值"
        )


def format_report(all_data: dict, sigma: float, verdict: str, reason: str, args) -> str:
    """格式化输出报告。"""
    lines = ["=" * 60, "MVP GO/NO-GO Report", "=" * 60, ""]

    g0_final = get_final_checkpoint(all_data.get("G0", {}))
    if g0_final is None:
        lines.append("ERROR: G0 数据缺失")
        return "\n".join(lines)

    g0_step, g0_metrics = g0_final
    baseline_rank = extract_metric(g0_metrics, "eff_rank")
    baseline_ppl = extract_metric(g0_metrics, "ppl")

    lines.append(f"G0 baseline (final checkpoint, step {g0_step}):")
    lines.append(f"  eff_rank = {baseline_rank:.2f}" if baseline_rank else "  eff_rank = N/A")
    lines.append(f"  ppl      = {baseline_ppl:.4f}" if baseline_ppl else "  ppl      = N/A")
    lines.append(f"  σ(eff_rank, G0 checkpoints) = {sigma:.4f}")
    lines.append("")

    for gen_name in ["G0", "G1", "G2"]:
        gen_data = all_data.get(gen_name, {})
        ckpts = gen_data.get("checkpoints", {})
        if not ckpts:
            lines.append(f"{gen_name}: {gen_data.get('status', 'missing')}")
            lines.append("")
            continue

        lines.append(f"{gen_name} checkpoints ({len(ckpts)} total):")
        for step in sorted(ckpts.keys()):
            ckpt = ckpts[step]
            r = extract_metric(ckpt, "eff_rank")
            p = extract_metric(ckpt, "ppl")

            r_str = f"{r:.2f}" if r is not None else "N/A"
            p_str = f"{p:.4f}" if p is not None else "N/A"

            delta_r = ""
            delta_p = ""
            leading = ""
            if baseline_rank is not None and r is not None and gen_name != "G0":
                dr = r - baseline_rank
                dr_pct = dr / baseline_rank * 100 if baseline_rank != 0 else 0
                delta_r = f" (Δ={dr:+.2f}, {dr_pct:+.2f}%)"
            if baseline_ppl is not None and p is not None and gen_name != "G0":
                dp = p - baseline_ppl
                dp_pct = dp / baseline_ppl * 100 if baseline_ppl != 0 else 0
                delta_p = f" (Δ={dp:+.4f}, {dp_pct:+.2f}%)"

            if gen_name != "G0" and baseline_rank and baseline_ppl:
                is_leading = check_spectral_leading(
                    ckpt, baseline_rank, baseline_ppl, sigma,
                    args.sigma_multiplier, args.ppl_threshold, args.ppl_pct_threshold,
                )
                leading = " [LEADING]" if is_leading else ""

            lines.append(f"  step {step:>5}: eff_rank={r_str}{delta_r}, ppl={p_str}{delta_p}{leading}")
        lines.append("")

    # Cross-generation trends
    lines.append("Cross-generation trends:")
    prev_gen = "G0"
    for gen_name in ["G1", "G2"]:
        prev_final = get_final_checkpoint(all_data.get(prev_gen, {}))
        curr_final = get_final_checkpoint(all_data.get(gen_name, {}))
        if prev_final and curr_final:
            _, pm = prev_final
            _, cm = curr_final
            pr = extract_metric(pm, "eff_rank")
            cr = extract_metric(cm, "eff_rank")
            pp = extract_metric(pm, "ppl")
            cp = extract_metric(cm, "ppl")
            kl = extract_metric(cm, "kl_divergence")

            if pr is not None and cr is not None:
                dr = cr - pr
                dr_pct = dr / pr * 100 if pr != 0 else 0
                lines.append(f"  {prev_gen}→{gen_name} eff_rank: {dr:+.2f} ({dr_pct:+.2f}%)")
            if pp is not None and cp is not None:
                dp = cp - pp
                dp_pct = dp / pp * 100 if pp != 0 else 0
                lines.append(f"  {prev_gen}→{gen_name} ppl:      {dp:+.4f} ({dp_pct:+.2f}%)")
            if kl is not None:
                lines.append(f"  {prev_gen}→{gen_name} KL:       {kl:.4f} nats")
            else:
                lines.append(f"  {prev_gen}→{gen_name} KL:       N/A")
        prev_gen = gen_name

    lines.append("")
    lines.append("=" * 60)
    lines.append(f"判定: {verdict}")
    lines.append(f"理由: {reason}")
    lines.append("=" * 60)

    return "\n".join(lines)


def build_json_report(all_data: dict, sigma: float, verdict: str, reason: str, args) -> dict:
    """构建 JSON 格式报告。"""
    g0_final = get_final_checkpoint(all_data.get("G0", {}))
    baseline_rank = None
    baseline_ppl = None
    if g0_final:
        _, g0m = g0_final
        baseline_rank = extract_metric(g0m, "eff_rank")
        baseline_ppl = extract_metric(g0m, "ppl")

    generations = {}
    for gen_name in ["G0", "G1", "G2"]:
        gen_data = all_data.get(gen_name, {})
        ckpts = gen_data.get("checkpoints", {})
        gen_report = {"status": gen_data.get("status", "missing"), "checkpoints": {}}
        for step in sorted(ckpts.keys()):
            ckpt = ckpts[step]
            entry = {
                "eff_rank": extract_metric(ckpt, "eff_rank"),
                "ppl": extract_metric(ckpt, "ppl"),
                "entropy_var": extract_metric(ckpt, "entropy_var"),
                "coverage": extract_metric(ckpt, "coverage"),
                "kl_divergence": extract_metric(ckpt, "kl_divergence"),
                "unigram_H": extract_metric(ckpt, "unigram_H"),
            }
            if baseline_rank and entry["eff_rank"] is not None and gen_name != "G0":
                entry["eff_rank_delta"] = entry["eff_rank"] - baseline_rank
                entry["eff_rank_delta_pct"] = entry["eff_rank_delta"] / baseline_rank if baseline_rank != 0 else None
            if baseline_ppl and entry["ppl"] is not None and gen_name != "G0":
                entry["ppl_delta"] = entry["ppl"] - baseline_ppl
                entry["ppl_delta_pct"] = entry["ppl_delta"] / baseline_ppl if baseline_ppl != 0 else None
            gen_report["checkpoints"][str(step)] = entry
        generations[gen_name] = gen_report

    return {
        "baseline": {"eff_rank": baseline_rank, "ppl": baseline_ppl, "sigma_eff_rank": sigma},
        "generations": generations,
        "verdict": verdict,
        "reason": reason,
        "thresholds": {
            "sigma_multiplier": args.sigma_multiplier,
            "ppl_threshold": args.ppl_threshold,
            "ppl_pct_threshold": args.ppl_pct_threshold,
            "kl_threshold": args.kl_threshold,
        },
    }


def main():
    parser = argparse.ArgumentParser(description="MVP GO/NO-GO 自动评估")
    parser.add_argument("--output-dir", required=True, help="Pipeline 输出根目录 (e.g., /root/autodl-tmp/output_v7/)")
    parser.add_argument("--sigma-multiplier", type=float, default=1.0, help="谱领先性 σ 倍数阈值 (default: 1.0)")
    parser.add_argument("--ppl-threshold", type=float, default=2.0, help="PPL 绝对上升阈值 (default: 2.0)")
    parser.add_argument("--ppl-pct-threshold", type=float, default=0.05, help="PPL 相对上升阈值 (default: 0.05 = 5%)")
    parser.add_argument("--kl-threshold", type=float, default=0.1, help="代际 KL 散度阈值 (default: 0.1 nats)")
    args = parser.parse_args()

    if not os.path.isdir(args.output_dir):
        print(f"ERROR: Output directory not found: {args.output_dir}")
        sys.exit(1)

    print(f"Scanning: {args.output_dir}")
    all_data = find_metrics_files(args.output_dir)

    if not all_data:
        print("ERROR: No generation data found")
        sys.exit(1)

    found_gens = [g for g, d in all_data.items() if d.get("checkpoints")]
    missing_gens = [g for g, d in all_data.items() if not d.get("checkpoints")]
    print(f"Found: {', '.join(found_gens) if found_gens else 'none'}")
    if missing_gens:
        print(f"Missing/incomplete: {', '.join(missing_gens)}")

    sigma = compute_sigma(all_data.get("G0", {}))
    verdict, reason = determine_verdict(all_data, sigma, args)

    report = format_report(all_data, sigma, verdict, reason, args)
    print()
    print(report)

    json_report = build_json_report(all_data, sigma, verdict, reason, args)
    json_path = os.path.join(args.output_dir, "go_nogo_report.json")
    try:
        with open(json_path, "w") as f:
            json.dump(json_report, f, indent=2, ensure_ascii=False)
        print(f"\nJSON report saved: {json_path}")
    except OSError as e:
        print(f"\nWARNING: Could not save JSON report to {json_path}: {e}")
        fallback = "/tmp/go_nogo_report.json"
        with open(fallback, "w") as f:
            json.dump(json_report, f, indent=2, ensure_ascii=False)
        print(f"Saved to fallback: {fallback}")


if __name__ == "__main__":
    main()
