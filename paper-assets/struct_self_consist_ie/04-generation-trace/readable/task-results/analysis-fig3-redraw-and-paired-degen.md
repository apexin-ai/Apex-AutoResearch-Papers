# analysis fig3 redraw and paired degen

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_fig3_redraw_and_paired_degen_20260517T082657_result.json`
- **Structured JSON:** [`3a70e67319e52f57f843.json`](../../sessions/3a/3a70e67319e52f57f843.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个子任务完成。汇总：

---

### 子任务 1: Figure 3 重绘

**X 轴更新 (Constant F1, gold-filtered degeneracy):**

| | 旧值 | 新值 |
|---|---|---|
| CoNLL | 58.0% | 47.4% |
| SciERC | 21.0% | 17.8% |
| Few-NERD | 13.8% | 13.8% |

**Per-type degeneracy (旧定义 → Constant F1 gold-filtered):**

| Type | 旧 | 新 |
|---|---|---|
| organization | 6.74% | 10.89% |
| other | 6.61% | 11.13% |
| building | 7.18% | 12.35% |
| event | 5.97% | 12.71% |
| product | 8.17% | 14.32% |
| location | 11.42% | 14.08% |
| person | 13.42% | 15.28% |
| art | 19.81% | 25.84% |

**Y 轴不变。**

**Spearman ρ:**
- Per-type (n=8): ρ = −0.29, p = 0.49
- Combined (n=11): ρ = −0.53, p = 0.096
- Pearson (n=11): r = −0.60, p = 0.053

PDF/PNG 已保存到 `output/figures/fig_degeneracy_lp_scatter.{pdf,png}` 和本地 artifacts。

---

### 子任务 2: Paired Degeneracy 确认

旧值使用的不是 Constant F1 定义。用统一定义重算：

```
Paired degeneracy (Constant F1, gold-filtered, 4,351 matched instances):
N=8:  14.6% (was 11.1%)
N=16:  7.0% (was 4.5%)
```

论文 experiments.tex:175 的 "11.1% → 4.5%" 需更新为 **"14.6% → 7.0%"**。趋势不变（N 增加，degeneracy 减半），但绝对值偏高。

---
