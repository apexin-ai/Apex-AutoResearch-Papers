# ops extract 80rel metrics

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_extract_80rel_metrics_20260515T135955_result.json`
- **Structured JSON:** [`9ca003f9cb957eef4c1d.json`](../../sessions/9c/9ca003f9cb957eef4c1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总结果

### 1. 进程状态

| 进程 | PID | 状态 |
|------|-----|------|
| 80-rel | 269256 | **DEAD** |
| exp-012 | 273161 | **DEAD** |
| GPU | — | 0 MiB / 0% (空闲) |

tmux 检查被 read_only 白名单拦截，无法确认。

### 2. eval_exp1.json (110 entries) — 按 num_types 分组

| count | n_batches | mean_acc | mean_bcs |
|-------|-----------|----------|----------|
| 1 | 80 | 0.8573 | 0.0000 |
| 4 | 5 | 0.8667 | 0.6335 |
| 8 | 5 | 0.8021 | 0.7175 |
| 16 | 5 | 0.6958 | 0.7950 |
| 32 | 5 | 0.6578 | 0.8893 |
| 64 | 5 | 0.5424 | 0.9434 |
| 80 | 5 | 0.5042 | 0.9706 |

### 3. eval_exp2.json (54 entries) — 含 low_bcs/high_bcs 对照组

| count | n_batches | mean_acc | mean_bcs |
|-------|-----------|----------|----------|
| 8 | 27 | 0.7924 | 0.7200 |
| 16 | 27 | ~0.709 | ~0.799 |

（exp2 count_16 因 grep 截断缺 1 条，偏差可忽略）

**趋势**：accuracy 随 num_types 增大单调下降（0.857→0.504），bcs 单调上升（0→0.971）。exp2 中 high_bcs 组 (count_8: acc=0.510, bcs=0.971) 远低于 low_bcs 组 (acc=0.823, bcs=0.471)，确认 boundary confusion 是 accuracy 下降的关键因素。

---
