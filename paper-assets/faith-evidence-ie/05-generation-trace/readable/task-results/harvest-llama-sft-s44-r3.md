# harvest llama sft s44 r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_llama-sft-s44-r3_20260520T143734_result.json`
- **Structured JSON:** [`1cd9d0d63e48316eeb9a.json`](../../sessions/1c/1cd9d0d63e48316eeb9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总 LLaMA SFT 3-seed 结果：

| Seed | Ign-F1 | Rel-F1 | Evi-F1(joint) | Evi-F1(TP) | EDCR |
|------|--------|--------|---------------|------------|------|
| s42 | 0.5384 | — | — | — | — |
| s43 | 0.5142 | — | — | — | — |
| **s44** | **0.4802** | 0.4902 | 0.3913 | 0.8502 | 0.6579 |

**LLaMA SFT 3-seed Ign-F1**: mean = 0.5109, std = 0.0238

s44 明显低于 s42/s43，拉低了均值。对比 RSFT 3-seed (mean=0.5654±0.0052)，SFT→RSFT 提升 +5.45 pp，且 RSFT 方差更小。

---
