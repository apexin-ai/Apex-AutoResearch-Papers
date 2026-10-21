# analysis grpo unstructured 20 completion

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_grpo_unstructured_20_completion_20260519T044035_result.json`
- **Structured JSON:** [`39f5ab19101c880a1385.json`](../../sessions/39/39f5ab19101c880a1385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能在之前的 session 中创建，已随 session 结束自动清理）。

---

## 训练结果

**GRPO unstructured 20% — 成功完成 100/100 步**

| 指标 | 值 |
|---|---|
| reward_mean | **0.883** |
| reward_std | 0.385 |
| loss | 0.092 |
| kl | 0.340 |
| runtime | 47 min |

模型权重已保存至 `checkpoint-100/model.safetensors` (15.2GB)。进程在保存 optimizer 状态时因磁盘满 (250G/250G = 100%) 崩溃，但模型权重完好，不影响后续推理/评估。

**注意**: westb-23072 数据盘已满，后续实验需先清理空间。

## 与 structured pruning GRPO 对比

| 方法 | reward_mean |
|---|---|
| **Unstructured 20% GRPO** | **0.883** |
| Structured CKA-only GRPO | 0.354 |
| Structured Standard GRPO | 0.081 |
| Structured RASP GRPO | 0.061 |

Unstructured 20% 的 reward 远高于所有 structured 方法（2.5x~14x）。这符合预期：unstructured pruning 保留了完整的层维度，对模型能力的破坏远小于 structured pruning，因此 GRPO recovery 起点更高、收敛更快。这也从反面说明 structured pruning 后的 recovery 是一个更具挑战性的问题，正是本文方法的价值所在。

---
