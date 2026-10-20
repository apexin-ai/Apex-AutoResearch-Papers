# launch grpo alpha3p0 westb0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_launch_grpo_alpha3p0_westb0_20260522T084857_result.json`
- **Structured JSON:** [`2843f338ca59fe4934ff.json`](../../sessions/28/2843f338ca59fe4934ff.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

管线已成功启动，当前处于数据集准备阶段。

```
PID: 170671 (bash) → 170676 (python)
GPU 0 显存: 12491 MiB
日志确认: 正常启动
  - 模型加载完成 (checkpoint-935 → cuda:0)
  - 当前阶段: Preparing GSM8K training dataset（tokenization 中）
```

管线流程：GRPO 训练 (100 steps) → eval_gsm8k 评估。训练开始后可用 `tail -f /tmp/alpha3p0_grpo.log` 监控进度。

---
