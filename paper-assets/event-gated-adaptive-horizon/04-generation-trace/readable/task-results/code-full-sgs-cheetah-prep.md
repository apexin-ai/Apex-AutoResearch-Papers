# code full sgs cheetah prep

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_full-sgs-cheetah-prep_20260516T202257_result.json`
- **Structured JSON:** [`45e61ca4bab835f0cb5e.json`](../../sessions/45/45e61ca4bab835f0cb5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

---

**Cheetah 环境可用性**: 已确认。`exp_010b_cheetah_civo_trigger` 和 `exp_010a_cheetah_baseline_s1` 均在 bjb1-45299 成功完成（logdir 包含 latest.pt + metrics.jsonl）。

**010a Cheetah Baseline v/e Trajectory** (NVE 归一化参考):

| Step | eval_return | value_mean | v/e ratio |
|------|-------------|------------|-----------|
| 5K | 11.63 | 0.0008 | 0.000067 |
| 25K | 177.82 | 12.62 | 0.071 |
| 55K | 212.24 | 87.60 | 0.413 |
| 105K | 420.68 | 245.81 | 0.584 |
| 205K | 696.97 | 410.18 | 0.589 |
| 305K | 657.90 | 499.67 | 0.759 |
| 405K | 789.86 | 550.82 | 0.697 |
| 515K | 849.77 | 592.89 | 0.698 |

Baseline 终态 v/e ≈ 0.70，收敛正常无 collapse。

**实验脚本**: `artifacts/scripts/exp_021_full_sgs_cheetah_s1.sh` — 配置与 018v2 完全一致，仅 `--task dmc_cheetah_run`。

**Registry**: `exp_021_full_sgs_cheetah_s1` 已创建为 **PENDING**，待 Director 审批后在 018_full_sgs_s2 完成后上 cuda:0 执行。

---
