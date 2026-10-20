# analysis exp fewnerd mf4 v2 s123

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_fewnerd_mf4_v2_s123_20260521T073956_result.json`
- **Structured JSON:** [`04321af85cd162ac363b.json`](../../sessions/04/04321af85cd162ac363b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 实验结果汇总：exp_fewnerd_mf4_v2_s123

### 核心指标

| 指标 | 值 |
|------|-----|
| greedy_f1 (micro-F1) | **0.7883** |
| oracle_f1 | **0.8891** |
| oracle_headroom | **+0.1009** |
| fleiss_kappa_mean | 0.3483 |
| soft_jaccard_mean | 0.6689 |
| sample_f1_mean | 0.6364 |
| sample_f1_std | 0.3819 |
| sample_f1_pct_zero | 20.49% |

### 相关性指标

| 指标 | Full | Conditional |
|------|------|-------------|
| ρ(SJ, F1) | **+0.3070** | +0.1966 |
| ρ(κ, F1) | +0.1588 | +0.0031 (n.s.) |
| rho_advantage | **+0.1482** | +0.1935 |
| n | 32565 | 28685 |

### Logprob baseline

| 指标 | Full | Conditional |
|------|------|-------------|
| ρ | +0.2193 | +0.1818 |
| τ | +0.1641 | +0.1369 |
| AUROC | 0.6056 | 0.5892 |

### Verdict: **MARGINAL** → Conclusion: **success**

### 与已有 FewNERD 数据对比

| 指标 | 本实验 (MF4v2 s123) | 14B N=8 (exp_14b) | T=0.8 s456 |
|------|---------------------|-------------------|------------|
| greedy_f1 | 0.7883 | 0.7984 | 0.788 |
| oracle_f1 | 0.8891 | 0.8791 | 0.877 |
| oracle_headroom | +0.1009 | +0.081 | +0.088 |
| rho_SJ_full | 0.307 | 0.324 | 0.328 |
| rho_advantage | 0.148 | 0.083 | 0.126 |

### 判定理由

1. greedy_f1=0.7883 在 FewNERD 正常范围内（0.70-0.80）
2. structural_beats_surface=true，rho_advantage=+0.148 是所有 FewNERD 实验中最高之一
3. 所有指标完整，无 NaN/异常
4. pct_zero=20.5% 偏高但未超 50% 阈值

### 注意事项

- **rho_kappa_cond=0.0031 (p=0.60)**：conditional 条件下 Fleiss kappa 完全失效，soft Jaccard 优势极大
- **seed=42 仍在 RUNNING**，完成后可做 2-seed 对比
- verdict=MARGINAL 而非 PASS，因 rho_SJ_full=0.307 未达 PASS 阈值（通常 ≥0.35）

---
