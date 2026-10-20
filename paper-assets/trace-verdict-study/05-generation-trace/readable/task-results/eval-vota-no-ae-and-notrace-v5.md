# eval vota no ae and notrace v5

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_vota_no_ae_and_notrace_v5_20260515T063956_result.json`
- **Structured JSON:** [`6c6d92ef327530426612.json`](../../sessions/6c/6c6d92ef327530426612.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## 产出

### 1. vota_no_ae_seed42（已验证）
| Metric | Value | 95% CI |
|---|---|---|
| Accuracy | **99.4%** | [98.9%, 99.8%] |
| Lift vs majority | +27.9pp | [25.5pp, 30.4pp] |
| Lift vs no_trace | +24.3pp | (点估计，paired CI ≈ vota 的 [21.8, 26.8]) |
| Pass F1 | 99.6% | — |
| Fail F1 | 98.9% | — |

之前 registry 的 0.9941 **被确认为准确**。

### 2. no_trace_seed42_v5
| Metric | Value | 95% CI |
|---|---|---|
| Accuracy | **75.1%** | [72.8%, 77.5%] |
| Lift vs majority | +3.6pp | [+0.4pp, +7.1pp] |

与 v4 完全一致（75.1%），符合预期。

### 3. full_trace vs no_trace_v5 正确 CI
| Comparison | Diff | 95% Paired CI | Sig |
|---|---|---|---|
| **full_trace vs no_trace** | **+6.6pp** | **[+4.4, +9.0]pp** | *** |
| vota vs no_trace | +24.3pp | [+21.8, +26.8]pp | *** |
| vota vs full_trace | +17.7pp | [+15.5, +19.8]pp | *** |

**Table 1 TBD 已修正**：full_trace vs no_trace lift = +6.6pp [4.4, 9.0]pp（显著）。

**MVP Verdict: PASS** — VOTA 在所有对比中显著领先。

---
