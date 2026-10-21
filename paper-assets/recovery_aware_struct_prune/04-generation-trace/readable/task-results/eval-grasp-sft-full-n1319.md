# eval grasp sft full n1319

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grasp_sft_full_n1319_20260516T014656_result.json`
- **Structured JSON:** [`fc8f7b2b4eedf9eb05f2.json`](../../sessions/fc/fc8f7b2b4eedf9eb05f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 **不空闲**。PID 74579 正在 cuda:1 上运行 `train_grpo_v5.py`（GRPO unpruned v2 训练），已运行 1 小时 10 分钟，占用 17.6GB 显存。

GPU 状态：
- **cuda:0**: PID 74134 — eval_sft_unpruned_full（不碰）
- **cuda:1**: PID 74579 — grpo_unpruned_v2 训练（`--gpu 0` + `CUDA_VISIBLE_DEVICES=1`）

两块 GPU 都被占满，无法在 cuda:1 上启动 GSM8K eval。需要等 grpo_unpruned_v2 完成或者你决定是否终止它。怎么处理？

---
