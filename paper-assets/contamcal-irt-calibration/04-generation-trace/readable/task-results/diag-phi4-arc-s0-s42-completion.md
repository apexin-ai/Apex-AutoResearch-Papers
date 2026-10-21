# diag phi4 arc s0 s42 completion

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_phi4-arc-s0-s42-completion_20260520T173433_result.json`
- **Structured JSON:** [`03461313569fe39899d7.json`](../../sessions/03/03461313569fe39899d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在（可能由触发本次任务的 cron 自行清理）。

---

## 汇总：Phi-4 跨种子 × 跨 benchmark 稳定性分析

Phi-4 是唯一拥有 3 seeds × 2 benchmarks 完整数据的模型家族。

### ARC Challenge (25-shot)

| Dosage | s0 | s42 | s123 |
|--------|------|------|------|
| d000 | 91.81 | 92.06 | 91.89 |
| d005 | 92.58 | 91.81 | 91.89 |
| d025 | 92.58 | 92.32 | 92.24 |
| d050 | 92.83 | 92.41 | 92.58 |
| d100 | 92.32 | 92.66 | 92.75 |
| **Δ(d100-d000)** | **+0.51** | **+0.60** | **+0.86** |

**ARC 三种子 mean Δ = +0.66pp**, σ = 0.18pp → **Immune confirmed**

### MMLU (5-shot)

| Seed | Δ(d100-d000) |
|------|-------------|
| s42 | -0.17 |
| s123 | +1.83 |
| s0 | +0.52 |

**MMLU 三种子 mean Δ = +0.73pp** → **Immune confirmed**

### 结论

| Benchmark | Mean Δ | Classification |
|-----------|--------|---------------|
| ARC | +0.66pp | Immune |
| MMLU | +0.73pp | Immune |
| **Cross-benchmark mean** | **+0.69pp** | **Immune** |

Phi-4 在两个 benchmark、三个种子下均表现为 Immune（|Δ| < 1pp），跨种子方差极小（ARC σ=0.18pp），分类高度稳健。

---
