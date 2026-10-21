# fix gpt2xl seed43 eval v3

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_gpt2xl_seed43_eval_v3_20260518T130527_result.json`
- **Structured JSON:** [`e8bc9234c459efc02cd2.json`](../../sessions/e8/e8bc9234c459efc02cd2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集。以下是完整结果。

---

## 1. seed=43 RF Evaluation 结果

| 指标 | 值 |
|------|-----|
| 4-class accuracy | **86.32%** |
| 95% CI | [86.17%, 86.49%] |
| d1v2 AUC | 0.9489 |
| Per-class recall | d0=99.36%, d1=92.0%, d2=73.44%, d3=80.48% |
| Fold accs | 86.18, 86.30, 86.38, 86.65, 86.10 |
| Top features | p90_ppl, p75_ppl, mean_surprisal, var_surprisal, p50_ppl |

## 2. 与 seed=42 Baseline 的差异

9-cell battery 中 gpt2xl_nucleus RF seed=42 = **83.97%**，rf_eval_seed42_rerun（带 clip）= **84.28%**。

seed=43 (86.32%) 比 seed=42 高 **+2.04pp ~ +2.35pp**。脚本中 `BASELINE_ACC=0.782` 是 Pythia nucleus 而非 GPT-2 XL。

## 3. d3 mean_ppl 分布对比

| 指标 | seed=42 | seed=43 |
|------|---------|---------|
| n | 5000 | 5000 |
| mean | 1,076,268 | 2,114,829 |
| median | 56.92 | 23.92 |
| max | 2,736,048,367 | 892,187,977 |
| p95 | 7,920 | 7,909,552 |
| p99 | 243,008 | 39,871,399 |
| std | 46,731,979 | 16,914,519 |
| >1M samples | 28 (0.56%) | 640 (12.8%) |
| >10K samples | 232 (4.6%) | 1125 (22.5%) |

## 4. d3 稳定性判断

**d3 不稳定是系统性问题，非 seed=43 特有。**

- seed=42 的 d3 max_ppl = 2.7B >> 1e6，确认 depth-3 LoRA 训练本身存在发散风险
- seed=43 重尾更严重：12.8% 样本 >1M（vs seed=42 的 0.56%），说明 seed=43 的 d3 LoRA 训练更不稳定
- 但两个 seed 的 median 都在合理范围（57 vs 24），大部分样本正常，极端值集中在少数发散样本
- 尽管 seed=43 的 d3 更不稳定，clip 后 RF accuracy 反而更高（86.32% vs 84.28%），可能因为极端 ppl 值被截断到 1e10 后仍提供了 d3 的区分信号

**结论：d3 ppl 发散是 depth-3 recursive LoRA fine-tuning 的固有特性，需要在论文中 frame 为 limitation（高 depth 训练不稳定），不是实验 bug。**

---
