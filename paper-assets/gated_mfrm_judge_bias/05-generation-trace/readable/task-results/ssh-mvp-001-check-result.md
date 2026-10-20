# ssh mvp 001 check result

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mvp_001_check_result_20260521T183649_result.json`
- **Structured JSON:** [`06dc979f5f220ded9676.json`](../../sessions/06/06dc979f5f220ded9676.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## mvp_001 实验结果

**VERDICT: FAIL** — 假设被否定。

### 完整结果表

| ρ | method | RMSE mean±std | τ mean±std | p-value |
|---|--------|--------------|------------|---------|
| 0.0 | joint_gmfrm | 0.1540±0.0269 | 0.9042±0.0445 | 0.4782 |
| 0.0 | mfrm_only | 0.1642±0.0255 | 0.8942±0.0482 | — |
| 0.0 | raw_average | 0.8002±0.1643 | 0.8951±0.0468 | — |
| 0.0 | sequential | 0.1540±0.0242 | 0.9016±0.0467 | ref |
| 0.3 | joint_gmfrm | 0.1521±0.0283 | 0.9068±0.0419 | 0.3506 |
| 0.3 | mfrm_only | 0.1635±0.0233 | 0.8989±0.0448 | — |
| 0.3 | raw_average | 0.8014±0.1644 | 0.8999±0.0445 | — |
| 0.3 | sequential | 0.1527±0.0236 | 0.9011±0.0452 | ref |
| 0.6 | joint_gmfrm | 0.1529±0.0285 | 0.9047±0.0418 | 0.3921 |
| 0.6 | mfrm_only | 0.1641±0.0229 | 0.8984±0.0456 | — |
| 0.6 | raw_average | 0.8025±0.1644 | 0.8995±0.0444 | — |
| 0.6 | sequential | 0.1537±0.0237 | 0.9037±0.0419 | ref |

### 诊断细项

| 检查项 | 结果 |
|--------|------|
| 收敛性 (R̂<1.05, ESS>100) | **PASS** |
| ρ=0.3 joint > sequential | p=0.3506 **FAIL** |
| ρ=0.6 joint > sequential | p=0.3921 **FAIL** |
| ρ=0.0 无退化 | p=0.9563 **PASS** |

### 关键发现

joint_gmfrm 在所有 ρ 下 RMSE 略优于 sequential（差异在第3-4位小数），τ 也略高，但**效果量太小、p-value 远未达显著**。confounding 强度从 0→0.6 并未拉大两者差距——说明当前模拟设定下 confounding 信号不够强，或 sequential pipeline 本身已足够 robust。

### Registry 更新

- status: DONE
- conclusion: negative
- metrics: 含所有 ρ 的 RMSE/τ/p-value 和 verdict
- log_path: `/tmp/mvp_run.log`
- checkpoint_path: `/root/gated_mfrm_judge_bias/mvp/results.csv`

---
