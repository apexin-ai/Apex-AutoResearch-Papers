# eval baseline gsm8k

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_baseline_gsm8k_20260514T135509_result.json`
- **Structured JSON:** [`820e909300d7c8d09fbf.json`](../../sessions/82/820e909300d7c8d09fbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件在增长（5317→5378），进程活跃。50 样本大约还要 40 分钟。这个需要等比较久，我总结当前状态：

---

**当前状态：**

1. **第一次快速 eval (max_new_tokens=512, 100 样本)** — 已完成
   - Accuracy: **30%** (30/100)
   - **但结果不可靠**：所有 100 个样本的输出都被截断在 ~500 字符，R1 模型的思维链没有足够 token 完成推理

2. **第二次 eval (max_new_tokens=4096, 50 样本)** — **正在运行**
   - PID 197442，在 GPU 1 上
   - 约 30-57s/样本，预计总耗时 ~45 分钟
   - 这次应该能给出准确的 baseline accuracy

3. GPU 0 上有个不属于我们的进程 (PID 196400, 10656 MiB)

**后续：** 等 quick2 eval 完成后汇报准确的 baseline accuracy。如果需要完整 1319 样本的结果，可以在此之后启动全量 eval（预计需要约 15-20 小时，需要用 nohup 后台跑）。

要继续等待结果还是先做其他事情？

---
