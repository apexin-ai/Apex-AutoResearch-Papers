# ssh dgec heterogeneous t

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_dgec-heterogeneous-t_20260520T083947_result.json`
- **Structured JSON:** [`c2eb1285e569276e354a.json`](../../sessions/c2/c2eb1285e569276e354a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果汇总

### 数据可用性
SciERC NER, 529 instances (gold-filtered), N=8 samples/instance：
- **T=0.7**: `exp_lp_scierc_t07` (1 seed)
- **T=1.0**: `exp_026_t10_seed{42,123,456}` (3 seeds)
- **T=0.8**: `exp_026_t08_seed{123,456}` (2 seeds, 作为 secondary)

M030 greedy match ~95%（浮点非确定性，同一模型）。

### T=0.7 + T=1.0 核心结果（3 seeds aggregate）

**Degeneracy 降低 ✓**
| Pool | Degeneracy | Mean Unique Outputs |
|------|-----------|-------------------|
| T=0.7 | 0.2231 | 2.73 |
| T=1.0 | 0.1235 | 3.38 |
| Mixed | 0.1701 | 3.09 |

混合 pool degeneracy 介于两者之间（从 T=0.7 的 22.3% 降至 17.0%），但未降到 T=1.0 水平。

**Construction vs Greedy (θ=0.25)**
| Pool | Uniform F1 | VC F1 |
|------|-----------|-------|
| T=0.7 | 0.6623* | 0.6559* |
| T=1.0 | 0.6525 | 0.6570 |
| Mixed | 0.6584 | 0.6609 |

Mixed pool 的 construction 在多数 seeds 上显著优于 greedy（uniform 2/3 sig, VC 3/3 sig），而纯 T=1.0 仅在部分 seeds 上显著。

**Cross-pool: Mixed vs T=1.0**
- Uniform: Δ=+0.006 (1/3 seeds significant, p=0.028)
- VC: Δ=+0.004 (1/3 seeds significant, p=0.033)

方向一致正向，但跨 seed 不稳定，未达到 robust significance。

### T=0.8 + T=1.0 (Secondary) — 失败
混合 T=0.8+T=1.0 的 degeneracy **反而升高**（0.21-0.22），construction 表现**劣于** T=1.0 单独。T 差异太小时混合无益。

### 结论
1. **Hypothesis 部分成立**：T=0.7+T=1.0 混合确实降低 degeneracy 并提升 construction，但改善幅度不够大，cross-pool comparison 不 robust (1/3 seeds)
2. **T 间距很关键**：T=0.8+T=1.0 (ΔT=0.2) 混合反而有害，T=0.7+T=1.0 (ΔT=0.3) 才有正效应
3. **VC 权重跨 T 可用**：混合 pool 上 VC-weighted construction 表现稳定，证实 VC 作为 output-based signal 的跨温度兼容性

---
