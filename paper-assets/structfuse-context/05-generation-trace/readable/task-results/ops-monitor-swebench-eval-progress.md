# ops monitor swebench eval progress

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_monitor-swebench-eval-progress_20260515T183706_result.json`
- **Structured JSON:** [`c02073c2f998c55a8923.json`](../../sessions/c0/c02073c2f998c55a8923.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是状态汇总：

---

## SWE-bench 纯检索 Eval

| 项目 | 状态 |
|------|------|
| PID | 58268 (alive), eval PID 58275 |
| 当前 checkpoint | **random_s42 (1/6)** |
| 进度 | **1/300 instances (0.3%)** |
| 速度 | ~131s/instance |
| ETA random_s42 | ~May 16 13:30 CST |
| ETA 全部 6 个 checkpoints | **~May 19 CST** |

首个实例结果（astropy__astropy-14365）：R@1=0, R@5=0, R@10=0, R@20=0, MRR=0.008。gold 文件是 `astropy/io/ascii/qdp.py`，模型预测全部偏离。仅 1 个实例，无统计意义。

**注意**：eval 与 Qwen 训练共享 GPU 0（eval 占 11.5GB，训练占 50GB，合计 62.5/97.9GB），暂无冲突。

---

## 训练进度

**Qwen dataflow_aware_s43** (GPU 0, PID 18427):
- step ~680/2810, epoch 1/2
- eval@500: val_loss=0.4617, **R@1=0.5495**, R@5=0.9728
- 下一个 eval@1000: ETA ~04:00 CST
- 无新 eval 数据点（上次记录的 eval@500 未变）

**StarCoder embedding_distance_s42** (GPU 1, PID 38016):
- step ~300/4242, epoch 1/3
- **尚无 checkpoint/eval**（首次 eval@500 ETA ~03:40 CST）

---

## 关键观察

1. SWE-bench eval 极慢（每实例需 clone repo + 编码 ~900 候选文件），6 checkpoints 约需 **3 天**
2. Qwen dataflow_s43 的 R@1=0.5495 低于 random_s44 的 0.6009 和 embed_s44 的 0.5942，但仅有 eval@500 一个数据点，需等 eval@1000 确认
3. 两条训练 + SWE-bench eval 三路并行，GPU 利用率 100%，VRAM 充足

---
