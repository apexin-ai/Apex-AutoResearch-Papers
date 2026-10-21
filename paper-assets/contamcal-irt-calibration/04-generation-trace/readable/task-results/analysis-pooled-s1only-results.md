# analysis pooled s1only results

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_pooled-s1only-results_20260515T034215_result.json`
- **Structured JSON:** [`3cfd0c5ca6c3e6a59cab.json`](../../sessions/3c/3cfd0c5ca6c3e6a59cab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。以下是完整结果和对比分析。

---

## S1-only vs Oracle 对比表

### 1. Gamma (contamination sensitivity parameter)

| | **ARC S1-only** | **ARC Oracle** | **GSM8K S1-only** | **GSM8K Oracle** |
|---|---|---|---|---|
| γ mean | **-1.464** | -1.46 | **0.187** | 3.773 |
| γ SD | 0.528 | — | 0.569 | 0.504 |
| 95% CI | [-2.51, -0.41] | — | [-0.92, 1.33] | [2.74, 4.71] |
| CI excludes 0 | **Yes** ✓ | Yes | **No** ✗ | Yes |
| 方向一致? | **完全一致** (负) | — | **不一致** (oracle 强正, S1≈0) | — |

### 2. Model Fit & Diagnostics

| | **ARC S1-only** | **ARC Oracle** | **GSM8K S1-only** | **GSM8K Oracle** |
|---|---|---|---|---|
| PPP | **0.968** (极端高) | — | **0.336** (合理) | 0.000 (极端低) |
| max Rhat | 1.010 ✓ | 1.002 | **1.015** ✗ | 1.002 |
| min ESS | 770 ✓ | 1222 | **330** ✗ | 1222 |
| Divergent | 0 ✓ | 0 | 0 ✓ | 0 |
| All diagnostics OK | **Yes** | Yes | **No** | Yes |

### 3. Calibration Metrics (ARC only — GSM8K v2 无 evaluation pipeline)

| Method | MAE | ECE | Brier | Cov50 | Cov80 | Cov95 | τ |
|---|---|---|---|---|---|---|---|
| **IRT 4PL+γ** | **0.035** | **0.032** | **0.002** | 0.0% | 25.0% | 62.5% | 0.756 |
| B0 Raw | 0.059 | 0.059 | 0.009 | 62.5% | 62.5% | 62.5% | 0.800 |
| B1 Remove+Rescore | 0.059 | 0.059 | 0.009 | 62.5% | 62.5% | 62.5% | 0.800 |
| B2 2PL+γ | 0.064 | 0.064 | 0.007 | 12.5% | 12.5% | 25.0% | 0.756 |
| B3 Vanilla 4PL | 0.071 | 0.071 | 0.007 | 12.5% | 12.5% | 12.5% | 0.756 |
| B4 Linear Reg | 0.056 | 0.056 | 0.006 | 75.0% | 75.0% | 87.5% | 0.756 |
| B5 Emperor | 0.059 | 0.059 | 0.009 | 62.5% | 62.5% | 62.5% | 0.800 |
| B6 DCR Fuzzy | 0.245 | 0.245 | 0.109 | 37.5% | 37.5% | 37.5% | 0.378 |

### 4. 关键发现

**ARC: S1-only ≈ Oracle** — gamma 几乎完全相同 (-1.464 vs -1.46)。S1 exposure（仅看到题目）足以让 IRT 检测到 ARC 上的污染信号。这符合预期：ARC 是多选题，看到题目本身就等同于记住答案。

**GSM8K: S1-only 信号消失** — gamma 从 oracle 的 3.77 降到 0.19，95% CI 包含零。S1 exposure 不足以检测 GSM8K 污染。这也符合预期：GSM8K 是开放式数学题，仅看到题目不够，需要看到解题过程（S2 exposure）。

**Coverage collapse**:
- ARC S1-only: Cov50=0%, Cov80=25% — 比 oracle (~31%) 更严重地 collapse，IRT 过度自信
- GSM8K S1-only: 无 evaluation 数据，无法对比

**PPP 方向相反**:
- ARC S1-only PPP=0.968 (过高，模型预测的 accuracy 系统性高于观测值)
- GSM8K Oracle PPP=0.000 (过低)
- 两者都是极端值，表明模型-数据 misfit，但方向不同

**GSM8K 诊断质量差**: rhat=1.015 和 ESS=330 未达标，说明 gamma≈0 导致后验分布平坦难以收敛，sampler 在缺乏信号时效率下降。

---
