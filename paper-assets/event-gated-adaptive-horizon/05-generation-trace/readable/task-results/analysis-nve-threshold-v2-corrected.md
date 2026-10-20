# analysis nve threshold v2 corrected

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_nve_threshold_v2_corrected_20260515T150538_result.json`
- **Structured JSON:** [`36cb5966ae4b4df9619a.json`](../../sessions/36/36cb5966ae4b4df9619a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### Per-experiment Max NVE

| Experiment | Max NVE | Label |
|---|---|---|
| exp_001_baseline | 1.0000 | HEALTHY |
| exp_008a_no_subsample_dt2 | 1.7191 | HEALTHY |
| exp_008e_v3_walker_s1 | 1.9285 | HEALTHY |
| exp_008f_no_dt_embed_subsample_on_h8 | 1.0198 | HEALTHY |
| exp_006_fixed_dt2 | **4.8362** | COLLAPSED |
| exp_008d_subsample_on_h8 | **4.1292** | COLLAPSED |
| exp_007_fixed_dt4 | 1.2236 | COLLAPSED |
| exp_008c_no_subsample_dt2_h8 | 1.2234 | COLLAPSED |
| exp_008e_v3_walker_s2 | **3.7801** | COLLAPSED |

### Group A (CIVO-specific): N=6, AUROC=1.0, CI=[1.0, 1.0]

| Threshold | TP | TN | FP | FN | Acc | Prec | Rec | F1 |
|---|---|---|---|---|---|---|---|---|
| 1.3 | 2 | 2 | 2 | 0 | 0.667 | 0.500 | 1.000 | 0.667 |
| 1.5 | 2 | 2 | 2 | 0 | 0.667 | 0.500 | 1.000 | 0.667 |
| 1.7 | 2 | 2 | 2 | 0 | 0.667 | 0.500 | 1.000 | 0.667 |
| **2.0** | **2** | **4** | **0** | **0** | **1.000** | **1.000** | **1.000** | **1.000** |

### Group B (all-failure): N=9, AUROC=0.8, CI=[0.4, 1.0]

| Threshold | TP | TN | FP | FN | Acc | Prec | Rec | F1 |
|---|---|---|---|---|---|---|---|---|
| 1.3 | 3 | 2 | 2 | 2 | 0.556 | 0.600 | 0.600 | 0.600 |
| 1.5 | 3 | 2 | 2 | 2 | 0.556 | 0.600 | 0.600 | 0.600 |
| 1.7 | 3 | 2 | 2 | 2 | 0.556 | 0.600 | 0.600 | 0.600 |
| **2.0** | **3** | **4** | **0** | **2** | **0.778** | **1.000** | **0.600** | **0.750** |

**Recommended threshold: 2.0x**

Reviewer 的判断得到了验证：exp_007（MaxNVE=1.22）和 exp_008c（MaxNVE=1.22）的 v/e 确实没有病态上升，与 healthy 实验在同一量级。NVE 无法检测这两类 non-CIVO failure，导致 Group B 的 AUROC 从 1.0 降到 0.8，CI 宽到 [0.4, 1.0]。threshold=2.0x 在两组上都零 FP，是最佳选择。

JSON 已保存到 `artifacts/nve_threshold_v2.json`，脚本在 `scripts/nve_threshold_analysis_v2.py`。

---
