# analysis mvp2 eval rsft s43 r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_eval_rsft_s43_r2_20260515T131820_result.json`
- **Structured JSON:** [`2b4445afd9f50900dd76.json`](../../sessions/2b/2b4445afd9f50900dd76.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成，结果如下：

```
rel_f1: 0.4683
ign_f1: 0.4683
evi_f1: 0.8156
edcr: 0.6388
precision: 0.4817
recall: 0.4556
evi_precision: 0.8142
evi_recall: 0.8170
n_predictions: 14970
n_truncated: 171
format_ok_rate: 1.0
inference_time_s: 6316.7
```

**PASS** — rel_f1=0.4683 > 0.4057, evi_f1=0.8156 > 0.798。

三个 seed 汇总：

| Seed | rel_f1 | evi_f1 | EDCR |
|------|--------|--------|------|
| 42 (r1) | 0.4449 | 0.8187 | 0.6565 |
| 44 | 0.4655 | 0.8087 | 0.6350 |
| 43 (r2) | 0.4683 | 0.8156 | 0.6388 |
| **均值** | **0.4596** | **0.8143** | **0.6434** |
| **标准差** | **0.0127** | **0.0051** | **0.0113** |

三个 seed 均稳定超过 SFT baseline（rel_f1=0.4057, evi_f1=0.7979），RSFT 提升显著。EDCR 均低于 SFT 的 0.7118，说明 RSFT 引入了更多 distractor citations。

---
