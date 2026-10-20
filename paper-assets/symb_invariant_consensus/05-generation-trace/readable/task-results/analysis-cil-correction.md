# analysis cil correction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cil-correction_20260521T094451_result.json`
- **Structured JSON:** [`2011e9ea08d25846df08.json`](../../sessions/20/2011e9ea08d25846df08.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修正完成。摘要：

**3 pairs 修正：**

| Pair | 旧 SC | 正确 SC | combo_acc | 旧 gain | 新 gain |
|------|-------|---------|-----------|---------|---------|
| Mistral+DeBERTa / FOLIO | 54.41% | 55.88% | 58.82% | +4.41pp | +2.94pp |
| Mistral+SICA / FOLIO | 54.41% | 55.88% | 59.31% | +4.90pp | +3.43pp |
| Qwen14B+DeBERTa / PW | 70.33% | 74.0% (BH) | 74.33% | +0.83pp | +0.33pp |

**相关性变化（修正后更强）：**

| Metric | Before | After |
|--------|--------|-------|
| Spearman ρ | 0.7619 (p=0.028) | **0.8095** (p=0.0149) |
| Pearson r | 0.7340 (p=0.038) | **0.7994** (p=0.0173) |

CIL 值不变，只修正了 combo_gain_w3 和相关性统计。修正后 CIL-gain 相关性反而更强了。

---
