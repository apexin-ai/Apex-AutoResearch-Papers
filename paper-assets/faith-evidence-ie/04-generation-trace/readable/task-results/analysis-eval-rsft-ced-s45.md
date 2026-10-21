# analysis eval rsft ced s45

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_rsft_ced_s45_20260516T042335_result.json`
- **Structured JSON:** [`bd7f01aca46a64065d5f.json`](../../sessions/bd/bd7f01aca46a64065d5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**eval_rsft_ced_s45 完成，registry 已更新。**

关键 metrics：

| 指标 | 值 |
|------|-----|
| **rel_f1** | 0.4514 |
| **rel_ign_f1** | 0.4416 |
| **evi_f1** | 0.8174 |
| rel_p | 0.4718 |
| rel_r | 0.4326 |
| edcr | 0.655 |
| format_ok | 100% |

**对比 flat-NLI RSFT s45**（0.4876）：CED s45 的 rel_f1 = 0.4514，低 3.6 个百分点。这与 CED 系列整体趋势一致——CED RSFT 在 rel_f1 上落后于 flat-NLI RSFT，但 evi_f1（0.8174）和 edcr（0.655）是 CED 协议的额外产出。

CED s45 的 0.4514 落在预期范围（0.43-0.47）内，结果合理。等 s42/s43/s44 全部到齐后可做配对 t-test。

---
