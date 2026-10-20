# analyze exp fewnerd mf4 s123 v2

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_exp_fewnerd_mf4_s123_v2_20260522T134002_result.json`
- **Structured JSON:** [`99ada1198c8d533be542.json`](../../sessions/99/99ada1198c8d533be542.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。

## exp_fewnerd_mf4_s123_v2 结果

实验正常完成，verdict=MARGINAL（与其他 seed 一致）。

### seed=123 关键指标

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.7883 |
| oracle_f1 | **0.8892** |
| oracle_headroom | **10.09pp** |
| fleiss_kappa | 0.3503 |
| soft_jaccard | 0.6701 |
| rho_sj_full / cond | +0.308 / +0.201 |
| logprob_auroc_full | 0.6069 |
| sample_f1_pct_zero | 20.4% |

MV/LP selection metrics 未计算（pipeline 未包含），与 s42/s456 一致。

### 3-Seed 汇总 (mean ± std)

| 指标 | mean | std |
|------|------|-----|
| greedy_f1 | **0.7884** | 0.0001 |
| oracle_f1 | **0.8830** | 0.0055 |
| oracle_headroom | **9.46pp** | 0.56pp |
| fleiss_kappa | 0.3532 | 0.0026 |
| soft_jaccard | 0.6766 | 0.0073 |
| sample_f1_pct_zero | 20.9% | 1.9% |

**要点**：greedy_f1 跨 seed 极其稳定（std=0.0001）；oracle_f1 s123 最高（0.8892 vs 0.8787/0.8810），拉高了 headroom 均值到 9.46pp；structural_beats_surface 三个 seed 均为 YES。

Registry 已更新 metrics + conclusion=success，分析报告已注册为 artifact。

---
