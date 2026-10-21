# eval qwen docred lora eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_qwen_docred_lora_eval_20260515T200302_result.json`
- **Structured JSON:** [`b63409c1146498768d3f.json`](../../sessions/b6/b63409c1146498768d3f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认两张 GPU 都在工作：

| GPU | PID | 显存 | 任务 |
|-----|-----|------|------|
| cuda:0 | 303530 | 16442 MiB | Llama DocRED unconstrained eval |
| cuda:1 | 304011 | 14988 MiB | **Qwen DocRED LoRA unconstrained eval** ✓ |

Qwen eval 已成功提交到 cuda:1，模型已加载（~15GB 显存）。日志文件：`~/runs/schema_semantic_constrained_ie/w5_qwen_docred_lora_unconstrained_eval.log`。预计 1-2h 完成（998 条 DocRED dev）。constrained eval 已预注册，等本次完成后再提交。

---
