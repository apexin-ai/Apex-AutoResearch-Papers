# exp downstream benchmark 002

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_downstream_benchmark_002_20260517T172537_result.json`
- **Structured JSON:** [`522aa5fc84c90b8fc0fa.json`](../../sessions/52/522aa5fc84c90b8fc0fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常进行中。有一个小问题（logs 目录不存在导致 tee 报错），但主日志正常写入到 runs 目录。

关键确认：
- 数据加载正确：4 × 500 训练 + 200 eval
- d0_only 训练已开始，loss 从 2.577 → 2.536 下降（不再全部 3.021）
- LoRA 参数：786,432 trainable / 406M total (0.19%)
- 训练速度 ~6.7 it/s，每个 subset 96 steps × 3 epochs

预计总时长：~30 min 训练（4 models × ~7 min each）+ ~5 min 评估 = ~35 min。

已完成：
- 从 gpu-6000pro-2 采样 2200 条文本（4 depths × 500 train + 200 eval）
- 传输到 westd-48862
- 编写完整 pipeline（训练 + held-out perplexity 评估 + 基线对比）
- 注册实验 `downstream_benchmark_002`，状态 RUNNING

---
