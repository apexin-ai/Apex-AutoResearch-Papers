# backfill walker trained nve

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_backfill_walker_trained_nve_20260524T061820_result.json`
- **Structured JSON:** [`bb407516b590a9d1aded.json`](../../sessions/bb/bb407516b590a9d1aded.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据结构确认 OK — value_mean 和 eval_return 在同一 step 的不同行，merge 正确。exp_009b 历史 notes 中 "nve 2.05x@25K" 可能使用了不同基线或旧算法；当前按 baseline=0.683 标准计算结果已更新。

3 个 registry 已全部更新完成。

---

## 汇总表

| 实验 | seed | ve_ratio peak | NVE peak | NVE≥1.5 窗口 | 分类 |
|------|------|---------------|----------|-------------|------|
| exp_009e_008d_walker_s1 | s1 | 1.6663 @55K | 2.44 | 55K-105K (50K steps, non-consecutive) | transient |
| exp_009b_008d_walker_s2 | s2 | 0.5703 @55K | 0.83 | N/A | no_civo |
| exp_008d_civo_trigger_s4 | s4 | 3.0294 @105K | 4.44 | 105K-105K (0K steps) | transient |

注：exp_009e 和 exp_009b 原始 metrics.jsonl 未记录 `civo/ve_ratio`（CIVO 检测模块未启用），回溯从 `value_mean/eval_return` 计算得到。exp_009e 的 NVE≥1.5 出现在 55K/75K/95K/105K 四个点但非连续（65K=1.02, 85K=1.18 跌破），判定 transient。

## exp_059_walker_trained_s5

**状态：RUNNING**（PID 186176 仍在运行），已有 checkpoint_25000.pt 和 checkpoint_75000.pt，不更新 registry。

---
