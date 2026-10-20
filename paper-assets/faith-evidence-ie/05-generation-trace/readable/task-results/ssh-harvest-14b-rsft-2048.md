# ssh harvest 14b rsft 2048

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_harvest-14b-rsft-2048_20260521T073921_result.json`
- **Structured JSON:** [`ccfef8f4b0215b8e0f98.json`](../../sessions/cc/ccfef8f4b0215b8e0f98.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 汇总

| 指标 | @1024 | @2048 | Delta |
|------|-------|-------|-------|
| **Ign-F1** | 0.5886 | 0.5896 | **+0.10pp** |
| F1 | 0.6003 | 0.6020 | +0.17pp |
| Evi-F1(DREEAM) | — | 0.4871 | — |
| EDCR | — | 0.5496 | — |
| Format OK | 100% | 100% | — |
| **n_truncated** | **0** | **18** | +18 |
| Inference time | — | 17373s (4h50m) | — |

**结论：@1024 可信。** Delta 仅 +0.10pp，远小于 1pp 阈值。18 篇文档在 @2048 下反而出现截断（模型在更大 budget 下生成了更长输出但仍超限），但对整体指标无实质影响。14B RSFT 的 @1024 评估结果可以直接用于论文报告。

---
