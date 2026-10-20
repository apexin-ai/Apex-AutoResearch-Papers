# analysis cls8b per test pr bucketed

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cls8b-per-test-pr-bucketed_20260516T023650_result.json`
- **Structured JSON:** [`6b24dc78deea979288aa.json`](../../sessions/6b/6b24dc78deea979288aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

### Overall (n=9784, 25 problems)
| | Precision | Recall | F1 |
|---|---|---|---|
| Fail | 80.06 | 56.76 | 66.43 |
| Pass | 85.53 | 94.76 | 89.91 |
| **Macro** | | | **78.17** |

### F2P Bucket 分析

**T=1 bucket 为空**——test set 没有只含 1 个 fail test 的 problem。

| Bucket | #Problems | #Instances | Accuracy | Fail P/R/F1 | Pass P/R/F1 |
|---|---|---|---|---|---|
| T=2-5 | 1 | 442 | 85.07% | 4.3/100/8.3 | 100/85.0/91.9 |
| T=6+ | 15 | 6,177 | 77.08% | 84.6/56.7/67.9 | 74.0/92.3/82.2 |
| (all-pass) | 9 | 3,165 | — | — | — |

### Per-problem 极端分化
- **满分**: matplotlib-24177 (100%), scikit-learn-14053 (100%), sphinx-11445 (97%)
- **灾难级**: astropy-7336 (fail_recall=1.1%), django-12325 (fail_recall=8.0%), sympy-17655 (fail_recall=0%), django-15037 (fail_recall=0%)

### Mutation type 差异显著 (T=6+ bucket)
| Mutation | Fail Recall |
|---|---|
| operator_swap | 69.7% (1159/1664) |
| off_by_one | 66.7% (36/54) |
| return_value | 57.6% (182/316) |
| boundary_removal | **20.0%** (122/609) |

boundary_removal 的 fail recall 远低于其他 mutation 类型，是主要弱项。

Artifact 已注册: `art_20260516_f34b60`

---
