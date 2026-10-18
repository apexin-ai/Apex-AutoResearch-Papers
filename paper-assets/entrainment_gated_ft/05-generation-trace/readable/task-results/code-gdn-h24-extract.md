# code gdn h24 extract

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_gdn_h24_extract_20260519T043545_result.json`
- **Structured JSON:** [`4b32aa78d351d06f71ef.json`](../../sessions/4b/4b32aa78d351d06f71ef.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 GDN 340M 的 lambada_openai 结果，全部模型都有完整 6-benchmark（lambada, hellaswag, winogrande, arc_easy, arc_challenge, mmlu）：

| Model | lambada acc | lambada ppl |
|---|---|---|
| **GDN-New-hybrid-24-1** | **0.3507** | **38.43** |
| GDN-hybrid-12-1 | 0.3252 | 42.98 |
| GDN-hybrid-3-1 | 0.3268 | 47.96 |
| GDN-hybrid-6-1 | 0.3513 | 39.10 |
| GDN-pure-baseline | 0.3753 | 34.81 |

GDN-New-hybrid-24-1 的 lambada acc=0.3507, ppl=38.43。pure baseline 仍是 lambada 最优（acc=0.3753, ppl=34.81）。hybrid-6-1 和 New-hybrid-24-1 接近，但都不及 pure。

---
