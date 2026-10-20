# check cuda1 chain status

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cuda1_chain_status_20260514T064855_result.json`
- **Structured JSON:** [`280539b27b37300199c4.json`](../../sessions/28/280539b27b37300199c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全貌清楚了。

## 结果

### 1. cuda:1 — 空闲，auto chain 已退出

`auto_cuda1_chain.sh` 在 11:19 启动，等待 external_seed123 (PID 405067) 完成。external 在 14:39 结束，但此时 `chain_cuda0_seed123.sh` 已于 14:29 在 cuda:0 上启动了 random50_seed123。auto chain 检测到后跳过：

```
[14:39:41] medium_external_seed123 finished.
[14:39:41] random50_seed123 already running on cuda:0, skipping.
```

**GPU 1 当前完全空闲（0MiB, 0% util）。**

### 2. cuda:0 — 正在跑 medium_random50_seed123

chain_cuda0 的顺序是 uncurated → rgds → random50，rgds 8 代全部完成后（14:29:28）自动衔接启动了 random50_seed123，当前在 **Gen 0/7**（训练阶段）。

### 3. rgds seed=123 — 已完成

8 代全部完成：

| Gen | PPL | RankMe | kNN | Rare | Corr |
|-----|-----|--------|-----|------|------|
| 0 | 26.32 | 365.65 | 0.988 | 0.0343 | 0.0301 |
| 7 | 90.25 | 431.19 | 0.988 | 0.0149 | -0.0170 |

### 总结

- **cuda:0**: chain_cuda0_seed123 正在跑 random50_seed123 Gen 0/7
- **cuda:1**: 空闲可用。auto chain 因竞态被 cuda:0 抢先而退出
- GPU 1 现在可以安排其他实验（如 seed=456 系列或其他待跑任务）

---
