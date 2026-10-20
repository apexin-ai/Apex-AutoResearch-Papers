# code wikievents constrained qwen llama full

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_wikievents_constrained_qwen_llama_full_20260517T193643_result.json`
- **Structured JSON:** [`b446f56d0b2fcb8daef6.json`](../../sessions/b4/b446f56d0b2fcb8daef6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 constrained 实验均已正常启动并在推理中：

| 实验 | GPU | VRAM | 利用率 | 已完成 | 模式 |
|------|-----|------|--------|--------|------|
| Qwen3-8B constrained | cuda:0 | 17585 MiB | 84% | 5/246 docs | full_s1 |
| Llama-3.1-8B constrained | cuda:1 | 16619 MiB | 88% | 11/246 docs | full_s1 |

两个 log 均确认 `Mode: full_s1`，246 samples，56 event types + 80 argument roles 正确加载。Llama 跑得更快（constrained decoding 对 Qwen3 的 thinking mode 可能有额外开销）。

---
