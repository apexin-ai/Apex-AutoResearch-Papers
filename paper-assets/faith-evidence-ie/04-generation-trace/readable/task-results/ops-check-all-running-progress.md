# ops check all running progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_all_running_progress_20260515T195558_result.json`
- **Structured JSON:** [`ccfc1a15060c8a3af8cf.json`](../../sessions/cc/ccfc1a15060c8a3af8cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | PID | 进度 | 预计剩余 |
|-----|------|-----|------|---------|
| 0 | plan_001_flat_nli_seed43 (RSFT) | 236779 | **502/507** (99%), epoch 2.96/3, loss 0.60 | **~25s** |
| 1 | plan_009 eval: grpo_flatnli_r3/ckpt-20 | 246982 | 1/62 batches (2%), inference | ~1h40m |
| 1 | plan_011 eval: bf16_g8/ckpt-30 | 247244 | 1/62 batches (2%), inference | ~1h50m |
| 2 | plan_012_dpo_ced_1ep (DPO) | 245108 | **63/167** (38%), epoch 0.36/1, loss 0.642 | **~21min** |
| 3 | plan_008_rsft_topk3 (RSFT) | 234494 | **1006/1509** (67%), epoch 1.99/3, loss 0.50 | **~36min** |

要点：
- **plan_001** 即将完成（剩 5 步），checkpoints: 300-500
- **plan_011** 训练已结束（PID 246041 DEAD），当前 GPU 1 跑的是两个 eval inference，刚开始
- **plan_012** DPO 训练正常，loss 从 0.693→0.642，rewards accuracy 0.41→0.70，暂无 checkpoint
- **plan_008** 进入 epoch 2 末尾，checkpoints: 800-1000，预计 ~36min 后完成 epoch 2 并继续 epoch 3

---
