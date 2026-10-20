# monitor westb verify status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westb_verify_status_20260516T184713_result.json`
- **Structured JSON:** [`b9841d295e9afc8b6c28.json`](../../sessions/b9/b9841d295e9afc8b6c28.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 任务 | PID | VRAM |
|-----|------|-----|------|
| cuda:0 | `eval_gsm8k.py` (eval_sft_rasp_25) | 602990 | 28.9 / 97.9 GB |
| cuda:1 | `train_grpo_v5.py` (grpo_rasp_rlvr_20) | 635524 | 71.7 / 97.9 GB |

两张卡均正常运行，符合预期。GRPO 训练已启动约 21 分钟（02:26 开始），wandb 已连接。

---
