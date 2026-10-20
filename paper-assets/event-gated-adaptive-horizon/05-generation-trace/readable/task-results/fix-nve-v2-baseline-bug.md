# fix nve v2 baseline bug

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_nve_v2_baseline_bug_20260525T212054_result.json`
- **Structured JSON:** [`fcba4c49a92f79763b53.json`](../../sessions/fc/fcba4c49a92f79763b53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇总：

**Bug**: exp_088 NVE 计算使用了错误的 Cheetah baseline ve_ratio（≈0.105 vs 正确值≈0.6），导致 NVE_peak 虚高 6 倍。

**影响范围**: 仅 exp_088。其他 Cheetah 实验（exp_078, exp_082, exp_086, exp_087）baseline 正确，已验证。

**修正后指标变化** (θ=1.5×):

| 指标 | V2 (bug) | V2.1 (修正) |
|------|----------|-------------|
| NVE_peak (exp_088) | 1.82@35K | 0.517@45K |
| AUROC | 0.9863 | 0.9895 |
| F1 | 0.909 | 0.926 |
| FP | 5 | 4 |
| Precision | 83.3% | 86.2% |

修正后 N=63 各指标均优于 V1 (N=61)，符合预期——新增的 exp_086/088 都是 clear TN。Section 8 (step-filtered NVE) 因基于错误前提已删除。

---
