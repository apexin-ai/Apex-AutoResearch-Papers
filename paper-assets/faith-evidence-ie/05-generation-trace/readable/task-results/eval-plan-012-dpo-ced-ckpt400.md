# eval plan 012 dpo ced ckpt400

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_012_dpo_ced_ckpt400_20260515T193207_result.json`
- **Structured JSON:** [`122aea0abd4df1337542.json`](../../sessions/12/122aea0abd4df1337542.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已在运行，进度 0/62 batches。

**状态汇总：**
- 实验 ID: `eval_plan_012_dpo_ced_ckpt400`
- PID: **242796**
- GPU: cuda:3 (rtx5090-4x)
- 模型已加载，LoRA adapter 已挂载，985 个 eval 文档准备就绪
- 正在推理中 (62 batches)

| Checkpoint | rel_f1 | 说明 |
|---|---|---|
| ckpt-501 (3ep) | 0.3429 | 过拟合版本 |
| ckpt-400 (~2.4ep) | 待出 | 本次 eval |
| SFT baseline | 0.4057 | 基准 |

---
