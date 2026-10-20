# infra mvp b pr fix

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_mvp-b-pr-fix_20260512T042357_result.json`
- **Structured JSON:** [`6fda5b623fd94dc526ee.json`](../../sessions/6f/6fda5b623fd94dc526ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

mvp-b-train eval 结果（`eval_results.json`）：

| 指标 | 值 |
|------|-----|
| **test_set_size** | 1890 |
| **overall_accuracy** | 87.51% |
| **majority_baseline** | 51.75% |
| **accuracy vs baseline gap** | +35.77pp |

**Per-class metrics:**

| Class | Precision | Recall | F1 | Support |
|-------|-----------|--------|-----|---------|
| **pass** | **93.24** | **81.80** | 87.15 | 978 |
| **fail** | **82.75** | **93.64** | 87.86 | 912 |

**Confusion matrix:** TP=800, TN=854, FP=58, FN=178, unparseable=0

模型对 fail 的召回率高（93.64），对 pass 的精确率高（93.24）。整体 F1 两类接近平衡（~87）。

---
