# analysis nve ci supplement d054 fix

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_ci_supplement_d054_fix_20260515T173839_result.json`
- **Structured JSON:** [`26f581c9e2660e1e0043.json`](../../sessions/26/26f581c9e2660e1e0043.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

**task_b2** (≥1.5x threshold, 3 pos / 5 neg):
| 指标 | 值 |
|------|-----|
| AUROC | 14/15 = 0.9333 |
| Accuracy | 7/8 = 87.5% |
| Clopper-Pearson 95% CI | [0.4735, 0.9968] |
| Separation margin | -2.16 (有重叠) |
| False positive | 008e_v3_s2 (NVE=3.78, Imagination-Reality Divergence) |

**task_b1** (≥1.7x threshold, 2 pos / 6 neg):
| 指标 | 值 |
|------|-----|
| AUROC | 12/12 = 1.0 |
| Accuracy | 8/8 = 100% |
| Clopper-Pearson 95% CI | [0.6306, 1.0] |
| Separation margin | +0.35 (完美分离) |

**注意**: task_b1 的 CI 下界 scipy 计算为 0.6306（`0.025^(1/8)`），与 Director 预期的 0.6877 有差异。0.6306 是标准 Clopper-Pearson 精确值。

JSON 已输出到服务器和本地 `artifacts/nve_threshold_v3_ci_supplement_d054.json`。

---
