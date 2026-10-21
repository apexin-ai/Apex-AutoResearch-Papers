# ops disk cleanup execute

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_disk_cleanup_execute_20260516T095655_result.json`
- **Structured JSON:** [`b24b627a85996f4a27c2.json`](../../sessions/b2/b24b627a85996f4a27c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

| | 清理前 | 清理后 |
|---|---|---|
| 已用 | 244GB (98%) | 202GB (81%) |
| 可用 | 6.1GB | 49GB |

**释放约 42GB**，已删除 6 个目录：

- `grpo_ced_g4_bf16/` (16GB) — GRPO LoRA + checkpoints
- `grpo_ced_g8_bf16/` (16GB) — GRPO LoRA + checkpoints
- `dpo_output/` (7GB) — DPO 3ep 输出
- `dpo_output_1ep/` (5GB) — DPO 1ep 输出
- `dpo_data/` (13MB) — DPO 训练数据
- `eval_plan_012_dpo_ced/` (7.5MB) — DPO eval 输出

DPO 已删除，因 plan_012 两组 metrics (1ep + 3ep) 均已完整录入 registry，conclusion=negative。

---
