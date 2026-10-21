# eval p0 ckpt batch eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_p0_ckpt_batch_eval_20260514T214336_result.json`
- **Structured JSON:** [`51b5eebdadcd0f30c135.json`](../../sessions/51/51b5eebdadcd0f30c135.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

当前状态与预期不同——两个 GPU 都不空闲：

| GPU | PID | 运行时间 | 任务 |
|-----|-----|---------|------|
| cuda:2 | 101842 | ~19 min | `lr5e6_r1` **ckpt-40 eval**（已在重跑中） |
| cuda:3 | 103831 | ~3 min | `grpo_ced_lr5e6_rp` ckpt-20 eval（另一个实验） |

Checkpoint 情况：checkpoint-20、40、60 都已存在。

**结论：**
- ckpt-40 eval 不需要重新提交，已经在 cuda:2 上跑了
- ckpt-60 eval 脚本已创建好（`/root/autodl-tmp/scripts/eval_lr5e6_ckpt60.sh`），等 cuda:2 的 ckpt-40 eval 跑完后可以立即提交到 cuda:2
- cuda:3 被另一个实验占着，短期内不可用

需要等 GPU 空出。要我轮询 cuda:2 状态，一空出就自动提交 ckpt-60 eval 吗？

---
