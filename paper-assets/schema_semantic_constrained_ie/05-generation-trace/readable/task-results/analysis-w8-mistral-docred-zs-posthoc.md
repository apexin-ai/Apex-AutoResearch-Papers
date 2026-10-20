# analysis w8 mistral docred zs posthoc

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w8_mistral_docred_zs_posthoc_20260516T091422_result.json`
- **Structured JSON:** [`b9ccd05b4cb5b1f8cfe3.json`](../../sessions/b9/b9ccd05b4cb5b1f8cfe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。结果汇总：

**Mistral DocRED Post-hoc Filtering**

| 指标 | 值 |
|------|-----|
| Total triples | 11,836 |
| Rejected | 8,727 (73.7%) |
| — RV (relation vocabulary) | 4,172 (35.2%) |
| — ET (entity type) | 3,382 (28.6%) |
| — DR (domain-range) | 1,173 (9.9%) |
| R_F1 before | 0.0434 |
| R_F1 posthoc | 0.0385 ↓ |
| R_F1 constrained | 0.0552 |
| TP before→after | 518 → 292 (lost 226, 43.6%) |

这是 6 组 ZS 实验中唯一 post-hoc 导致 R_F1 下降的 case。73.7% 的拒绝率砍掉了近一半的 TP，precision 翻倍（0.044→0.094）但 recall 崩塌（0.043→0.024），净效果为负。key_finding 已更新：ZS 下 post-hoc ≥ constrained 在 5/6 组成立，Mistral DocRED 是例外。

---
