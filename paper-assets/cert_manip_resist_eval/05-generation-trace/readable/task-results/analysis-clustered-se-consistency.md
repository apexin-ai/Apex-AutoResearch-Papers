# analysis clustered se consistency

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_clustered-se-consistency_20260522T210421_result.json`
- **Structured JSON:** [`95024da4a2145061512e.json`](../../sessions/95/95024da4a2145061512e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the comparison report:

---

## 一致性检查

### 代码实现

**Clustered SE** (`run_clustered_se_analysis.py`):
- 对每个 panel 的 3 个 judge position (k=0,1,2) 分别做 clustering
- cluster 变量 = `judge_ids_list[panel][k]`（该 position 上的 judge identity）
- 每个 position 有 **13** 个 unique cluster（C(15,3) 有序组合结构导致每个位置只出现 13 个 judge）
- SE 聚合方式：**取 3 个 position 中的 max SE**，再用 max SE 计算 t 值和 p 值

**Mixed Effects** (`run_clustered_se_analysis.py`):
- 对 judge0/judge1/judge2 分别拟合 3 个 mixed-effects model（random intercept per judge）
- p 值聚合方式：**取 3 个 model 中的 max p-value**

**Wild Cluster Bootstrap** (`run_wild_cluster_bootstrap_v2.py`):
- 对 3 个 position 分别做 bootstrap（Rademacher weights, B=9999）
- p 值聚合方式：**取 max p-value across 3 positions**
- 每个 position **13** clusters

### 论文描述 (§3.6)

> **Clustered SE:** "We cluster at the judge level (15 clusters) using CR1 bias-corrected sandwich estimators, where each panel is assigned to the cluster of its most vulnerable member."

> **Mixed Effects:** "We add random intercepts for each judge ($J_j$, $j{=}1,\ldots,15$), allowing the baseline vulnerability to vary by judge while estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed effects."

> **Wild Bootstrap:** "We perform $B{=}9{,}999$ bootstrap resamples using Rademacher weights, clustering by each of the three panel positions in turn and taking the maximum $p$-value across positions (the most conservative aggregation)."

### 不一致之处

| # | 问题 | 论文 | 代码 | 严重性 |
|---|------|------|------|--------|
| 1 | **Clustered SE 策略描述错误** | "each panel is assigned to the cluster of its most vulnerable member"（单次 clustering，按最脆弱 judge 归类） | 3-position max-SE（3 次独立 clustering，每次按一个 position 的 judge 归类，取 max SE） | **高** — 描述的是完全不同的方法 |
| 2 | **Cluster 数量错误** | "15 clusters" | 每个 position 实际 **13** clusters（sorted C(15,3) 组合中，每个位置只能出现 13 个 judge） | **中** — 数值不符 |
| 3 | **Mixed Effects 缺少 3-position 描述** | 只说 "random intercepts for each judge"，暗示单个模型 | 实际拟合 3 个模型（分别对 judge0/1/2 做 random intercept），取 max p-value | **中** — 遗漏关键实现细节 |
| 4 | **Wild Bootstrap 描述正确** | ✓ 准确描述了 3-position max-p 策略 | ✓ 一致 | 无 |

### 建议修改

将 §3.6 的 Clustered SE 和 Mixed Effects 段落替换为：

```latex
\paragraph{Clustered Standard Errors.} Because each panel of $K{=}3$ judges
does not map to a single cluster, we perform three separate one-way
clusterings---one for each judge position in the ordered panel tuple---using
CR1 bias-corrected sandwich estimators (13 clusters per position). The
reported standard error for each coefficient is the maximum across the three
clusterings, yielding the most conservative inference.

\paragraph{Mixed Effects.} For each of the three judge positions, we fit a
linear mixed-effects model with a random intercept for the judge occupying
that position, estimating $K_{\mathrm{eff}}$ and $\eta_{\max}$ as fixed
effects. The reported $p$-value for each coefficient is the maximum across
the three models.
```

---
