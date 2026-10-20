# analysis a060 bf16 leadlag

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_a060_bf16_leadlag_20260518T211552_result.json`
- **Structured JSON:** [`7c7646fca00478948f77.json`](../../sessions/7c/7c7646fca00478948f77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## α=0.60 s42 bf16 完整分析结果

### Metrics Drift (gen_0 → gen_10)
| 指标 | gen_0 | gen_10 | Drift |
|------|-------|--------|-------|
| d1 | 0.0914 | 0.0663 | **-27.5%** |
| d2 | 0.5043 | 0.3157 | **-37.4%** |
| d3 | 0.8329 | 0.5707 | **-31.5%** |
| entropy | 3.2574 | 2.6404 | -18.9% |
| ece | 0.0123 | 0.0426 | +246.5% |
| ppl | 27.68 | 20.27 | -26.8% (bf16) |

### 5-Method Lead-Lag (Unified 2σ)
| Method | Fwd | Rev |
|--------|-----|-----|
| naive_xcorr | 8/8 | 8/8 |
| diff_xcorr | 8/8 | 8/8 |
| threshold_onset | **6/8** | 0/8 |
| perm_granger | **8/8** | **0/8** |
| ty_granger | 0/8 | 1/8 |
| **K≥4** | **6/8** | |

Perm Granger 完美方向性不对称 (8/8 fwd vs 0/8 rev)。TY 0/8 符合 C003。

### MMCT Detection
| Mode | Sig |
|------|-----|
| uniform_forward | 0/8 |
| weighted_pair_forward | **6/8** |
| weighted_global_forward | 0/8 |

### Table 7 格式行
`naive: 8/8, diff: 8/8, thresh: 6/8, pg_fwd: 8/8, pg_rev: 0/8, ty: 0/8, K≥4: 6/8`

### Regime Map 定位
α=0.60 是 **method-dependent detectability** 区域：perm_granger 和 threshold_onset 可靠检测到 forward 方向性，MMCT 仅在 weighted_pair 模式下检出（6/8），uniform 和 global 模式不检出。位于 α=0.50 (boundary) 和 α=0.75 (broadly detectable) 之间，weighted_pair_forward 的检出率可以精确定位 detectability threshold。

---
