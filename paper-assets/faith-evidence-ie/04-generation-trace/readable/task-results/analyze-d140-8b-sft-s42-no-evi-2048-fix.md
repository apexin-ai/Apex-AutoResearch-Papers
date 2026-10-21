# analyze d140 8b sft s42 no evi 2048 fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_d140_8b_sft_s42_no_evi_2048_fix_20260521T103134_result.json`
- **Structured JSON:** [`3e43a6d199ad5c39b7e0.json`](../../sessions/3e/3e43a6d199ad5c39b7e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。总结：

### d140_8b_sft_s42_no_evi_2048_fix 结果

| 指标 | no-evi (本实验) | with-evi (配对) | 差异 |
|------|----------------|----------------|------|
| **Ign-F1** | **0.5019** | 0.5012 | +0.0007 |
| F1 | 0.5227 | 0.5219 | +0.0008 |
| Evi-F1(DREEAM) | 0.0130 | 0.4087 | — |
| EDCR | 0.7051 | 0.7039 | +0.0012 |
| Format OK | 100% | 99.9% | — |
| Truncated | 260/985 | 236/985 | +24 |

**Evidence Tax = -0.0007**（本质为零）。在 8B SFT + 2048 tokens 条件下，要求模型额外输出 evidence 对 RE 性能无显著影响——既不帮助也不损害关系抽取。

---
