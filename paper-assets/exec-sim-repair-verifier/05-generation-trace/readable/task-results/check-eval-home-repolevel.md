# check eval home repolevel

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_eval-home-repolevel_20260514T014720_result.json`
- **Structured JSON:** [`c196d158f67122ccf132.json`](../../sessions/c1/c196d158f67122ccf132.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

找到了。项目根目录下的 `eval_repo_cls.json` 就是 seed123 的 repo-level eval 结果。

## Repo-level CLS Seed123 Eval 结果

**状态**: 已完成（May 13 18:46），进程已退出（PID 3018282 不存在，GPU 空闲）

**Checkpoint**: `checkpoints_repo_cls_seed123_home/checkpoint-200`

| 指标 | 值 |
|------|------|
| n_instances | **9784** (repo-level ✓) |
| accuracy | 64.75% |
| majority_baseline | 72.96% |
| gap_vs_majority | **-8.21 pp** |
| f1_fail | **55.16** |
| f1_pass | 70.96 |
| **f1_macro** | **63.06** |
| precision_fail | 42.04 |
| precision_pass | 88.92 |
| recall_fail | **80.16** |
| recall_pass | 59.04 |
| unparseable | 132 (1.35%) |

**Confusion Matrix**: tn=2121, fp=525, fn=2924, tp=4214 (support: fail=2646, pass=7138)

**对比原始 seed (results/repo_cls_v4_eval)**:

| 指标 | 原始 seed | seed123 | 差异 |
|------|-----------|---------|------|
| accuracy | 66.11 | 64.75 | -1.36 |
| f1_fail | 36.30 | **55.16** | **+18.86** |
| f1_pass | 76.91 | 70.96 | -5.95 |
| f1_macro | 56.61 | **63.06** | **+6.45** |
| recall_fail | 35.71 | **80.16** | **+44.45** |

seed123 在 f1_macro（+6.45）和 fail 召回（+44.45 pp）上大幅优于原始 seed，虽然 accuracy 略低（因为原始 seed 几乎全预测 pass 来凑 majority baseline）。seed123 的预测更平衡，fail 检测能力显著更强。

注意：两者都只 eval 了 checkpoint-200（早期 checkpoint），seed123 训练产生了更多 checkpoint（到 1000），尚未 eval 更优 checkpoint。

---
