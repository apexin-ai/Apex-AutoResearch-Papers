# check home val sweep collect

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_home-val-sweep-collect_20260514T084704_result.json`
- **Structured JSON:** [`53ec7cd4276bf2240321.json`](../../sessions/53/53ec7cd4276bf2240321.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。

## D063 Val Sweep 状态报告

### 运行状态
- **tmux `val_sweep`: RUNNING**
- 总计 13 个 checkpoints，已完成 5 个，正在跑第 6 个
- 当前: `v5/checkpoint-600` (2240/9335, ~24%)

### 已完成 Val 结果 (9335 samples, val split)

**seed123_home 系列** (5/5 完成):

| Checkpoint | Accuracy | F1_macro | F1_fail | F1_pass | Gap vs Maj |
|-----------|----------|----------|---------|---------|------------|
| ckpt-200 | 62.51 | 55.54 | 37.94 | 73.14 | -13.37 |
| ckpt-400 | 80.72 | 67.03 | 45.78 | 88.27 | +4.84 |
| ckpt-600 | 76.78 | 66.81 | 48.63 | 85.00 | +0.90 |
| **ckpt-800** | **81.81** | **69.14** | **49.37** | **88.91** | **+5.93** |
| ckpt-1000 | 82.30 | 67.63 | 45.84 | 89.42 | +6.43 |

**seed123_home val-best**: **ckpt-800** (f1_macro 69.14%)
- ckpt-1000 有更高 accuracy (82.30 vs 81.81)，但 f1_macro 低 1.5pp，fail recall 只有 31% (vs ckpt-800 的 37%)，过度偏向 pass 类

### 剩余进度

| # | Checkpoint | 状态 |
|---|-----------|------|
| 6 | v5/ckpt-600 | **RUNNING** (~24%) |
| 7 | v5/ckpt-4000 | pending |
| 8 | v5/ckpt-4200 | pending |
| 9 | v5/ckpt-4400 | pending |
| 10 | v5/ckpt-4600 | pending |
| 11 | home/ckpt-200 | pending |
| 12 | home/ckpt-2400 | pending |
| 13 | home/ckpt-2600 | pending |

### 时间估算
- 每个 checkpoint ~26 分钟
- v5 ckpt-600 预计 ~02:06 PDT (09:06 UTC) 完成
- 剩余 8 个 × 26min ≈ 3.5 小时
- **全部完成预计: ~05:30 PDT (12:30 UTC)**

### 注意
- `val_eval_results/` 目录存 val 结果；`results/` 目录是之前的 test 结果（9784 instances），两者别混淆
- 1883 个 unparseable predictions 被 majority fallback，数量一致说明是模型 tokenizer/format 问题，非数据问题

---
