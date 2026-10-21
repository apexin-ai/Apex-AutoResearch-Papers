# analysis scierc n8 s123 s456

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_n8_s123_s456_20260522T113642_result.json`
- **Structured JSON:** [`24ea3365075ed0c0c4f4.json`](../../sessions/24/24ea3365075ed0c0c4f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据就绪。以下是完整结果。

---

## 实验 1: exp_scierc_n8_s123

**状态**: 正常完成，EXIT_CODE=0，无 error/traceback

**产出文件**:
- `output/scierc_n8_seed123/report.json` (1,729 bytes)
- `output/scierc_n8_seed123/samples.jsonl` (20,054,496 bytes)

**指标**:
| Metric | Value |
|--------|-------|
| greedy_f1 | 0.6613 |
| mv_f1 | 0.6648 |
| mv_delta | **+0.34pp** |
| lp_f1 | 0.6698 |
| lp_delta | +0.85pp |
| degeneracy_rate | 11.6% |
| agreement_rate | 0.6646 |
| oracle_f1 | 0.7794 |
| fleiss_kappa | 0.3847 |
| soft_jaccard | 0.6979 |

**注意**: s123 是唯一一个 MV delta 为正的 seed。

---

## 实验 2: exp_scierc_n8_s456

**状态**: 正常完成，EXIT_CODE=0，无 error/traceback

**产出文件**:
- `output/scierc_n8_seed456/report.json` (1,730 bytes)
- `output/scierc_n8_seed456/samples.jsonl` (19,984,016 bytes)

**指标**:
| Metric | Value |
|--------|-------|
| greedy_f1 | 0.6657 |
| mv_f1 | 0.6573 |
| mv_delta | **-0.84pp** |
| lp_f1 | 0.6626 |
| lp_delta | -0.31pp |
| degeneracy_rate | 12.0% |
| agreement_rate | 0.6597 |
| oracle_f1 | 0.7733 |
| fleiss_kappa | 0.3864 |
| soft_jaccard | 0.6939 |

---

## Seed=42 参考值 (scierc_mf4v2_seed42)

| Metric | Value |
|--------|-------|
| greedy_f1 | 0.6651 |
| mv_f1 | 0.6550 |
| mv_delta | **-1.01pp** |
| lp_f1 | 0.6604 |
| lp_delta | -0.47pp |
| degeneracy_rate | 14.2% |
| agreement_rate | 0.6767 |

> ⚠️ s42 的 MV Δ 为 -1.01pp（此处用 micro-F1 重新计算），与先前 hypothesis 中的 -0.74pp 有差异，可能因之前使用了不同的 F1 计算方式。

---

## 3-Seed 汇总 (SciERC N=8 Finetuned, T=1.0)

| Metric | s42 | s123 | s456 | **Mean** | **Std** |
|--------|-----|------|------|----------|---------|
| greedy_f1 | 0.6651 | 0.6613 | 0.6657 | **0.6640** | 0.0024 |
| mv_f1 | 0.6550 | 0.6648 | 0.6573 | **0.6590** | 0.0051 |
| mv_delta (pp) | -1.01 | +0.34 | -0.84 | **-0.50** | 0.74 |
| lp_f1 | 0.6604 | 0.6698 | 0.6626 | **0.6643** | 0.0049 |
| lp_delta (pp) | -0.47 | +0.85 | -0.31 | **+0.02** | 0.72 |
| degeneracy_rate | 14.2% | 11.6% | 12.0% | **12.6%** | 1.4% |
| agreement_rate | 0.6767 | 0.6646 | 0.6597 | **0.6670** | 0.0088 |

### 关键发现

1. **MV Δ = -0.50 ± 0.74pp** — 均值为负但跨 0（s123 为正），说明 SciERC finetuned 模型上 MV 不稳定地 hurt greedy。方差大（std=0.74 > |mean|=0.50），统计上不显著。
2. **LP Δ = +0.02 ± 0.72pp** — LP selection 基本持平 greedy，同样方差大。
3. **Degeneracy ≈ 12.6%** — 远低于 CoNLL（~60%），接近 FewNERD 水平。
4. **Greedy F1 在三 seed 间非常稳定**（0.6640 ± 0.0024），说明模型本身稳定，不稳定性来自 MV 聚合。

---
