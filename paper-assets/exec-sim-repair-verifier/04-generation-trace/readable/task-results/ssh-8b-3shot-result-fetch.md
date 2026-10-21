# ssh 8b 3shot result fetch

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_8b-3shot-result-fetch_20260522T215921_result.json`
- **Structured JSON:** [`9460f52e3628c336c9af.json`](../../sessions/94/9460f52e3628c336c9af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个结果都拿到了。汇总如下：

## Qwen3-8B NF4 Eval 结果

| 指标 | 0-shot | 3-shot |
|------|--------|--------|
| **per_test_accuracy** | 60.53 | 60.42 |
| **f1_macro** | 55.73 | 56.09 |
| **f1_fail** | 70.30 | 69.89 |
| **f1_pass** | 41.17 | 42.28 |
| **n_unparseable** | 5 | 1 |

**Confusion matrix:**

|  | 0-shot | 3-shot |
|--|--------|--------|
| TN (fail→fail) | 883 | 868 |
| FP (fail→pass) | 29 | 44 |
| FN (pass→fail) | 717 | 704 |
| TP (pass→pass) | 261 | 274 |

**要点：**
- 0-shot 和 3-shot 性能几乎一样（accuracy 差 0.11pp，f1_macro 差 0.36pp），3-shot 没有带来实质性提升。
- 两者都严重偏向预测 fail（FN 远大于 FP），pass 召回率极低（~27%）。
- 3-shot 略微改善了 pass 的召回（TP 261→274），但代价是更多 FP（29→44）和更多 unparseable 减少（5→1）。
- N=1890，majority baseline 51.75%，两者均高出 ~8.7pp。

---
