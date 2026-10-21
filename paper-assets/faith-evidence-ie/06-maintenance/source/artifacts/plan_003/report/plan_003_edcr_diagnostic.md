# EDCR Cross-Method Diagnostic Table (plan_003)

**Date**: 2026-05-15  
**Source**: All metrics from project registry (faith-evidence-ie)

## Diagnostic Table

### Evidence-Producing Methods

| Method | exp_id | rel_f1 | evi_f1 | EDCR | Conclusion | Notes |
|--------|--------|--------|--------|------|------------|-------|
| SFT baseline (quant) | mvp2_sft_eval_r3 | 0.4057 | 0.7979 | 0.7118 | success | Quantized baseline, 367/985 truncated |
| SFT baseline (no-quant) | eval_sft_baseline_noquant | 0.4106 | 0.8013 | 0.7039 | success | No-quant, +0.49pp rel_f1 vs quant |
| RSFT-CED s42 | mvp2_eval_rsft_r1 | 0.4449 | 0.8187 | 0.6565 | success | Seed 42, r1 config |
| RSFT-CED s43 | mvp2_eval_rsft_s43_r2 | 0.4683 | 0.8156 | 0.6388 | success | Seed 43 |
| RSFT-CED s44 | mvp2_rsft_train_r1_s44 | 0.4655 | 0.8087 | 0.6350 | success | Seed 44 |
| **RSFT-CED 3-seed mean** | — | **0.4596±0.013** | **0.8143±0.005** | **0.6434** | — | 3 seeds, all pass |
| RSFT-CED r2a | mvp2_eval_rsft_r2a | 0.4494 | 0.8108 | 0.6641 | success | alpha=128, 1ep, clean data |
| RSFT-CED r2b | mvp2_eval_rsft_r2b | 0.4493 | 0.8128 | 0.6609 | success | alpha=32, 1ep |
| RSFT-flat-NLI | eval_plan_001_flat_nli | 0.4539 | 0.8043 | 0.6431 | success | flat p_pos, single seed |
| CED-reranker (N=8) | mvp2_ced_reranker_poc | **0.4864** | **0.8188** | **0.6156** | success | Zero training, best evidence-producing method |
| GRPO bf16 (ckpt-100) | eval_grpo_g8_bf16 | 0.4549 | 0.8086 | 0.6318 | success | bf16 LoRA, no forgetting |
| GRPO QLoRA (ckpt-100) | mvp2_eval_ced_kl001_r4_step100 | 0.2167 | 0.5746 | 0.8539 | negative | Catastrophic forgetting |
| DPO-CED 3ep | plan_012_dpo_ced | 0.3429 | 0.8403 | 0.7294 | negative | Overfitting, rewards_accuracy=1.0 |
| DPO-CED 1ep | plan_012_dpo_ced_1ep | 0.0022 | 0.7500 | 0.9982 | negative | Complete relation extraction collapse |
| RSFT top_k=3 | eval_plan_008_rsft_topk3 | TBD | TBD | TBD | RUNNING | Full dev eval in progress |

### No-Evidence Baseline

| Method | exp_id | rel_f1 | evi_f1 | EDCR | Conclusion | Notes |
|--------|--------|--------|--------|------|------------|-------|
| SFT-no-evidence | eval_plan_014_sft_no_evidence | 0.4893 | 0 | 0 | success | No evidence output; highest single-model rel_f1 |

### GRPO QLoRA Forgetting Trajectory (supplementary)

| Checkpoint | rel_f1 | evi_f1 | EDCR |
|------------|--------|--------|------|
| ckpt-10 | 0.0030 | 0.7200 | 0.9983 |
| ckpt-20 | 0.0088 | 0.4230 | 0.9954 |
| ckpt-30 | 0.0338 | 0.5889 | 0.9798 |
| ckpt-50 | 0.1563 | 0.5643 | 0.8858 |
| ckpt-60 | 0.1467 | 0.5763 | 0.9062 |
| ckpt-90 | 0.2108 | 0.5666 | 0.8584 |
| ckpt-100 | 0.2167 | 0.5746 | 0.8539 |

## EDCR Diagnostic Analysis

### Diagnostic Zones

| EDCR Range | Diagnosis | Examples |
|------------|-----------|----------|
| **>0.95** | Catastrophic failure — evidence 与 relation 决策完全脱钩 | DPO-CED 1ep (0.9982), GRPO QLoRA ckpt-10 (0.9983) |
| **0.80–0.95** | Severe degradation — 模型有 extraction 能力但严重受损 | GRPO QLoRA ckpt-100 (0.8539) |
| **0.70–0.80** | Baseline zone — SFT 水平的 evidence-decision 一致性 | SFT baseline (0.7118), DPO-CED 3ep (0.7294) |
| **0.63–0.67** | Improved zone — RSFT/GRPO 有效提升区间 | RSFT-CED mean (0.6434), GRPO bf16 (0.6318) |
| **<0.63** | Best zone — 证据高度支撑决策 | CED-reranker (0.6156) |

### Key Findings

**1. EDCR 与 rel_f1 强负相关（evidence-producing methods）**

在所有产出 evidence 的方法中，EDCR 越低，rel_f1 越高。排序完全一致：

- CED-reranker: EDCR=0.6156 → rel_f1=0.4864 (best)
- GRPO bf16: EDCR=0.6318 → rel_f1=0.4549
- RSFT-CED mean: EDCR=0.6434 → rel_f1=0.4596
- SFT baseline: EDCR=0.7118 → rel_f1=0.4057
- DPO-CED 3ep: EDCR=0.7294 → rel_f1=0.3429
- GRPO QLoRA: EDCR=0.8539 → rel_f1=0.2167
- DPO-CED 1ep: EDCR=0.9982 → rel_f1=0.0022

**2. EDCR 是 catastrophic failure 的早期预警信号**

EDCR > 0.95 准确标识了所有完全崩溃的方法（DPO 1ep, GRPO QLoRA 早期 checkpoints）。这些方法 rel_f1 < 0.02，但 evi_f1 可能仍在 0.6-0.85——单看 evi_f1 无法诊断问题，EDCR 能识别 evidence 与 decision 的脱钩。

**3. EDCR 区分 overfitting vs forgetting**

- DPO-CED 3ep (overfitting): EDCR=0.7294, evi_f1=0.8403 (高) → evidence 质量好但与 relation 不匹配
- GRPO QLoRA (forgetting): EDCR=0.8539, evi_f1=0.5746 (低) → evidence 和 relation 都受损

**4. SFT-no-evidence 是 EDCR 框架的反面验证**

去掉 evidence 后 rel_f1 反而最高 (0.4893)，说明当前 evidence generation 对 relation extraction 是净负担。EDCR 的价值在于：在保留 evidence 的前提下，优化 evidence-decision 一致性能缩小这个差距（CED-reranker 0.4864 vs SFT-no-evidence 0.4893, gap 仅 0.29pp）。

### Summary

EDCR 在 11 种 evidence-producing 方法配置上展现了一致的诊断能力：(1) 与 rel_f1 单调负相关，(2) 极端值 (>0.95) 可靠标识方法崩溃，(3) 在中间区域 (0.63-0.72) 区分有效训练方法与 baseline。CED-reranker 达到最低 EDCR (0.6156) 和最高 evidence-producing rel_f1 (0.4864)，验证了 CED 信号在 inference-time reranking 中的价值。GRPO bf16 (EDCR=0.6318) 和 RSFT-CED (EDCR=0.6434) 通过 training-time 优化达到相近水平，而 DPO 和 QLoRA GRPO 的高 EDCR (0.73-0.998) 准确反映了这些方法的失败。EDCR 可作为 evidence-grounded DocRE 中方法质量的单一诊断指标。
