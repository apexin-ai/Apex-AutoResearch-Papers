# analysis bh correction

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bh-correction_20260520T152347_result.json`
- **Structured JSON:** [`c32de2b02be55224815e.json`](../../sessions/c3/c32de2b02be55224815e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果如下：

## 6 个 raw p-values

| Comparison | b | c | n | raw p |
|---|---|---|---|---|
| FOLIO w=1 | 0 | 4 | 4 | 0.1250 |
| FOLIO w=3 | 5 | 11 | 16 | 0.2101 |
| **FOLIO w=5** | **7** | **16** | **23** | **0.0931** |
| PW w=1 | 4 | 9 | 13 | 0.2668 |
| PW w=3 | 22 | 43 | 65 | 0.0125 |
| **PW w=5** | **35** | **99** | **134** | **2.89×10⁻⁸** |

## BH 校正表 (α=0.05, m=6)

| Rank | Comparison | raw p | BH threshold | adj p (BH) | Survives? |
|---|---|---|---|---|---|
| 1 | PW w=5 | 2.89×10⁻⁸ | 0.0083 | 1.73×10⁻⁷ | **YES** |
| 2 | PW w=3 | 0.0125 | 0.0167 | 0.0375 | **YES** |
| 3 | FOLIO w=5 | 0.0931 | 0.0250 | 0.1863 | no |
| 4 | FOLIO w=1 | 0.1250 | 0.0333 | 0.1875 | no |
| 5 | FOLIO w=3 | 0.2101 | 0.0417 | 0.2521 | no |
| 6 | PW w=1 | 0.2668 | 0.0500 | 0.2668 | no |

## 结论

**2/6 comparisons survive BH at α=0.05:**
- **PW w=5**: raw p=2.89×10⁻⁸, adj p=1.73×10⁻⁷
- **PW w=3**: raw p=0.0125 < threshold 0.0167, adj p=0.0375

关键验证：PW w=3 排在 rank 2，BH threshold = (2/6)×0.05 = 0.0167，raw p=0.0125 < 0.0167 → survives。

---
