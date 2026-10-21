# analysis docred factorial tost

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_factorial_tost_20260518T213650_result.json`
- **Structured JSON:** [`0fe6d83ea0a4e59dd234.json`](../../sessions/0f/0fe6d83ea0a4e59dd234.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果已保存到 `artifacts/docred_factorial_tost/results.json`。

## 2×2 Factorial TOST 结果

**2×2 Cell Means:**
| | low BCS | high BCS |
|---|---|---|
| **count_16** | 64.84% ± 5.29% (n=18) | 54.22% ± 10.26% (n=17) |
| **count_32** | 54.26% ± 6.24% (n=17) | 49.33% ± 7.46% (n=18) |

**Main Effects:**
- Count effect: +7.96pp (count_16 > count_32)
- BCS effect: -7.99pp (high BCS lowers accuracy)

**Interaction:** +5.70pp (CI: [-1.58pp, 12.98pp])

BCS 的负面效果在 count_16 时更大（10.62pp drop）比 count_32（4.93pp drop），差异 5.70pp。

**TOST Results:**
- ±3pp: p_TOST = 0.7698 → **NOT established**
- ±2pp: p_TOST = 0.8436 → **NOT established**

**Bootstrap 95% CI:** [-1.23pp, 12.43pp]

**结论：** 交互效应无法在 ±3pp 或 ±2pp 边界内建立等价性。interaction estimate 为 +5.70pp，CI 跨越 0 但上界达 ~13pp，远超等价边界。BCS median split (0.5488) 将 70 batches (35×2 count levels) 分为近似等大的 4 cells。交互效应表明 confusability 对 accuracy 的影响在较小 schema count 时更严重。

---
