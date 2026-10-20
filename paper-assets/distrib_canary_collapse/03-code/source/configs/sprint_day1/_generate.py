#!/usr/bin/env python3
"""Generate all Day 1 sprint experiment launch scripts."""
import os

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

TEMPLATE = (
    'bash -c "cd /root/autodl-tmp/distrib_canary_collapse'
    " && export HF_HOME=/root/autodl-tmp/.hf_cache"
    " && export HF_HUB_DISABLE_XET=1"
    " && export HF_ENDPOINT=https://hf-mirror.com"
    " && source /root/miniconda3/etc/profile.d/conda.sh"
    " && conda activate base"
    " && PYTHONUNBUFFERED=1 python -u iterative_train.py"
    " --model_name {model}"
    " --seed {seed}"
    " --data_dir data/{data}"
    " --steps_per_gen 5000"
    " --num_generations 10"
    " --synthetic_ratio {alpha}"
    "{extra}"
    ' --output_dir {output_dir}"'
)

EXPERIMENTS = [
    {
        "file": "plan_034_gpt2m_s43.sh",
        "plan": "plan_034",
        "model": "openai-community/gpt2-medium",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "43",
        "extra": "",
        "output_dir": "results/generalize/gpt2m_wiki_a100_s43",
        "category": "generalize",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_030_opt_s43.sh",
        "plan": "plan_030",
        "model": "facebook/opt-1.3b",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "43",
        "extra": " --gradient_checkpointing",
        "output_dir": "results/generalize/opt1b_wiki_a100_s43",
        "category": "generalize",
        "est_hours": "8",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_031_interv_pred_s43.sh",
        "plan": "plan_031",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "43",
        "extra": " --intervention_mode predictive --intervention_metric token_entropy --intervention_threshold 0.15 --intervention_alpha 0.0",
        "output_dir": "results/intervention/predictive_te_s43",
        "category": "intervention",
        "est_hours": "5",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_032_interv_react_s43.sh",
        "plan": "plan_032",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "43",
        "extra": " --intervention_mode reactive --intervention_metric distinct_1 --intervention_threshold 0.10 --intervention_alpha 0.0",
        "output_dir": "results/intervention/reactive_d1_s43",
        "category": "intervention",
        "est_hours": "5",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_033a_interv_a075_pred.sh",
        "plan": "plan_033",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.75",
        "seed": "42",
        "extra": " --intervention_mode predictive --intervention_metric token_entropy --intervention_threshold 0.15 --intervention_alpha 0.0",
        "output_dir": "results/intervention/predictive_te_a075_s42",
        "category": "intervention",
        "est_hours": "5",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_033b_interv_a075_react.sh",
        "plan": "plan_033",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.75",
        "seed": "42",
        "extra": " --intervention_mode reactive --intervention_metric distinct_1 --intervention_threshold 0.10 --intervention_alpha 0.0",
        "output_dir": "results/intervention/reactive_d1_a075_s42",
        "category": "intervention",
        "est_hours": "5",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_026_a060_s42.sh",
        "plan": "plan_026",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.60",
        "seed": "42",
        "extra": "",
        "output_dir": "results/alpha_sweep/a060_s42",
        "category": "alpha_sweep",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_035_c4_a075.sh",
        "plan": "plan_035",
        "model": "EleutherAI/pythia-410m",
        "data": "c4_5k",
        "alpha": "0.75",
        "seed": "42",
        "extra": "",
        "output_dir": "results/alpha_sweep_c4/a075_s42",
        "category": "alpha_sweep_c4",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_036_14b_c4.sh",
        "plan": "plan_036",
        "model": "EleutherAI/pythia-1.4b",
        "data": "c4_5k",
        "alpha": "1.0",
        "seed": "42",
        "extra": " --gradient_checkpointing",
        "output_dir": "results/generalize/pythia14b_c4_a100_s42",
        "category": "generalize",
        "est_hours": "8",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_008_ablation_accum.sh",
        "plan": "plan_008",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.50",
        "seed": "42",
        "extra": " --accumulate",
        "output_dir": "results/ablation/accumulate_a050_s42",
        "category": "ablation",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_039_a010_s43.sh",
        "plan": "plan_039",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.10",
        "seed": "43",
        "extra": "",
        "output_dir": "results/alpha_sweep/a010_s43",
        "category": "alpha_sweep",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_040_a060_s43.sh",
        "plan": "plan_040",
        "model": "EleutherAI/pythia-410m",
        "data": "wikitext103_5k",
        "alpha": "0.60",
        "seed": "43",
        "extra": "",
        "output_dir": "results/alpha_sweep/a060_s43",
        "category": "alpha_sweep",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_004a_c4_a050_s42.sh",
        "plan": "plan_004",
        "model": "EleutherAI/pythia-410m",
        "data": "c4_5k",
        "alpha": "0.50",
        "seed": "42",
        "extra": "",
        "output_dir": "results/alpha_sweep_c4/a050_s42",
        "category": "alpha_sweep_c4",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_004b_c4_a050_s43.sh",
        "plan": "plan_004",
        "model": "EleutherAI/pythia-410m",
        "data": "c4_5k",
        "alpha": "0.50",
        "seed": "43",
        "extra": "",
        "output_dir": "results/alpha_sweep_c4/a050_s43",
        "category": "alpha_sweep_c4",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_004c_c4_a050_s44.sh",
        "plan": "plan_004",
        "model": "EleutherAI/pythia-410m",
        "data": "c4_5k",
        "alpha": "0.50",
        "seed": "44",
        "extra": "",
        "output_dir": "results/alpha_sweep_c4/a050_s44",
        "category": "alpha_sweep_c4",
        "est_hours": "4",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_037a_interv_14b_pred.sh",
        "plan": "plan_037",
        "model": "EleutherAI/pythia-1.4b",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "42",
        "extra": " --intervention_mode predictive --intervention_metric token_entropy --intervention_threshold 0.15 --intervention_alpha 0.0 --gradient_checkpointing",
        "output_dir": "results/intervention/predictive_te_14b_s42",
        "category": "intervention",
        "est_hours": "8",
        "gpu_note": "1x RTX PRO 6000",
    },
    {
        "file": "plan_037b_interv_14b_react.sh",
        "plan": "plan_037",
        "model": "EleutherAI/pythia-1.4b",
        "data": "wikitext103_5k",
        "alpha": "1.0",
        "seed": "42",
        "extra": " --intervention_mode reactive --intervention_metric distinct_1 --intervention_threshold 0.10 --intervention_alpha 0.0 --gradient_checkpointing",
        "output_dir": "results/intervention/reactive_d1_14b_s42",
        "category": "intervention",
        "est_hours": "8",
        "gpu_note": "1x RTX PRO 6000",
    },
]


def generate_sh(exp):
    return TEMPLATE.format(**exp) + "\n"


def generate_readme():
    lines = []
    lines.append("# Day 1 Sprint Experiments")
    lines.append("")
    lines.append("Generated: 2026-05-18")
    lines.append("")
    lines.append("Target server: **westd-17855** (6x RTX PRO 6000 98GB)")
    lines.append("Fallback server: westd-19828")
    lines.append("")
    lines.append("## Parameter Compatibility Notes")
    lines.append("")
    lines.append("| Requested param | Actual support |")
    lines.append("|----------------|---------------|")
    lines.append("| `--bf16` | NOT supported (script uses fp32/auto) |")
    lines.append("| `--optimizer` | Use `--optim` instead |")
    lines.append("| `--data_strategy accumulate` | Use `--accumulate` flag |")
    lines.append("| `--gradient_checkpointing` | Supported (added for 1.3B+ models) |")
    lines.append("")
    lines.append("## Experiment List")
    lines.append("")
    lines.append("| # | File | Plan | Model | Data | Alpha | Seed | Category | Est Hours |")
    lines.append("|---|------|------|-------|------|-------|------|----------|-----------|")
    for i, exp in enumerate(EXPERIMENTS, 1):
        model_short = exp["model"].split("/")[-1]
        lines.append(
            f"| {i} | `{exp['file']}` | {exp['plan']} | {model_short} | {exp['data']} | {exp['alpha']} | {exp['seed']} | {exp['category']} | ~{exp['est_hours']}h |"
        )
    lines.append("")
    lines.append(f"**Total: {len(EXPERIMENTS)} experiments**")
    lines.append("")

    # GPU assignment suggestion
    lines.append("## Suggested GPU Assignment (6 GPUs)")
    lines.append("")
    lines.append("Strategy: large models (OPT-1.3b, Pythia-1.4b) take 1 GPU each; Pythia-410m experiments queue on remaining GPUs.")
    lines.append("")
    lines.append("### Wave 1 (start immediately, ~4-8h)")
    lines.append("")
    lines.append("| GPU | Experiment | Est Time |")
    lines.append("|-----|-----------|----------|")
    lines.append("| GPU 0 | plan_030 (OPT-1.3b) | ~8h |")
    lines.append("| GPU 1 | plan_036 (Pythia-1.4b C4) | ~8h |")
    lines.append("| GPU 2 | plan_034 (GPT2-medium) | ~4h |")
    lines.append("| GPU 3 | plan_031 (interv pred s43) | ~5h |")
    lines.append("| GPU 4 | plan_032 (interv react s43) | ~5h |")
    lines.append("| GPU 5 | plan_026 (a060 s42) | ~4h |")
    lines.append("")
    lines.append("### Wave 2 (after Wave 1 GPUs free up, ~4-5h)")
    lines.append("")
    lines.append("| GPU | Experiment | Est Time |")
    lines.append("|-----|-----------|----------|")
    lines.append("| GPU 2 | plan_033a (interv a075 pred) | ~5h |")
    lines.append("| GPU 3 | plan_033b (interv a075 react) | ~5h |")
    lines.append("| GPU 4 | plan_035 (C4 a075) | ~4h |")
    lines.append("| GPU 5 | plan_008 (ablation accum) | ~4h |")
    lines.append("")
    lines.append("### Wave 3 (backfill)")
    lines.append("")
    lines.append("| GPU | Experiment | Est Time |")
    lines.append("|-----|-----------|----------|")
    lines.append("| GPU 2 | plan_039 (a010 s43) | ~4h |")
    lines.append("| GPU 3 | plan_040 (a060 s43) | ~4h |")
    lines.append("| GPU 4 | plan_004a (C4 a050 s42) | ~4h |")
    lines.append("| GPU 5 | plan_004b (C4 a050 s43) | ~4h |")
    lines.append("")
    lines.append("### Wave 4 (final)")
    lines.append("")
    lines.append("| GPU | Experiment | Est Time |")
    lines.append("|-----|-----------|----------|")
    lines.append("| GPU 0 | plan_037a (interv 1.4b pred) | ~8h |")
    lines.append("| GPU 1 | plan_037b (interv 1.4b react) | ~8h |")
    lines.append("| GPU 2 | plan_004c (C4 a050 s44) | ~4h |")
    lines.append("")
    lines.append("## Dependencies")
    lines.append("")
    lines.append("- plan_037a/b (1.4b intervention) depends on plan_036 (1.4b baseline) completing to validate model works")
    lines.append("- plan_033a/b (a075 intervention) independent of plan_031/032 (a100 intervention)")
    lines.append("- All C4 experiments (plan_004a/b/c, plan_035, plan_036) require `data/c4_5k` to be synced to westd-17855")
    lines.append("- All wikitext experiments require `data/wikitext103_5k` to be synced to westd-17855")
    lines.append("- HF model cache: if westd-17855 has no cache, first run per model will download (~1-3GB each)")
    lines.append("")
    lines.append("## Quick Launch Commands")
    lines.append("")
    lines.append("Each .sh file contains the full `bash -c \"...\"` command ready for `submit_training_job`.")
    lines.append("")
    lines.append("To run directly on the server:")
    lines.append("```bash")
    lines.append("# Single experiment")
    lines.append("CUDA_VISIBLE_DEVICES=0 bash configs/sprint_day1/plan_034_gpt2m_s43.sh &")
    lines.append("")
    lines.append("# Or use nohup for persistence")
    lines.append("CUDA_VISIBLE_DEVICES=0 nohup bash configs/sprint_day1/plan_034_gpt2m_s43.sh > logs/plan_034.log 2>&1 &")
    lines.append("```")
    lines.append("")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    for exp in EXPERIMENTS:
        path = os.path.join(OUT_DIR, exp["file"])
        with open(path, "w") as f:
            f.write(generate_sh(exp))
        os.chmod(path, 0o755)
        print(f"  wrote {exp['file']}")

    readme_path = os.path.join(OUT_DIR, "README.md")
    with open(readme_path, "w") as f:
        f.write(generate_readme())
    print(f"  wrote README.md")
    print(f"\nTotal: {len(EXPERIMENTS)} experiment scripts generated.")
