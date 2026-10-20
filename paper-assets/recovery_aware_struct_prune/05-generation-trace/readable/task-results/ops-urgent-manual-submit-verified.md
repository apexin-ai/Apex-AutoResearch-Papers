# ops urgent manual submit verified

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_manual_submit_verified_20260520T130027_result.json`
- **Structured JSON:** [`f69cce91c3cec6f44d71.json`](../../sessions/f6/f69cce91c3cec6f44d71.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**M023 完成。两个 GRPO 训练已确认 RUNNING：**

| 实验 | PID | GPU | 显存 | 状态 |
|------|-----|-----|------|------|
| grpo_cka_only_20_seed456 | 249963 | cuda:0 | 12497 MiB | RUNNING |
| grpo_cka_only_15_v2 | 250149 | cuda:1 | 13193 MiB | RUNNING |

两个日志均无错误，模型已加载到 GPU，数据集已就绪，正在加载 ref_model 准备开始训练。按训练 1 历史 ~12.7s/step 估算，100 steps 约 21 分钟完成。

---
