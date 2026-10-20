# Appendix → 正文升级计划

Short paper (4 pages) 将大量内容压入 appendix。Long paper (8 pages) 有 ~4 pages 额外空间可用。以下标记每个 appendix section 的升级决策。

---

## 当前 Short Paper Appendix 内容

| Appendix | Short Paper 位置 | 内容 |
|---|---|---|
| A: Labeling Quality Audit | Appendix §A | Tie breakdown, genuine labels, strict retrain |
| B: Per-Task Decomposition | Appendix §B | 11-task table (n, Δ_full, D%, labels) |
| C: Correlation Robustness | Appendix §C | Spearman, bootstrap CI, LOO table |
| D: Router Training Details | Appendix §D | Hyperparameters, GA effect, seed variance |
| E: Penalty Sensitivity | Appendix §E | P vs DAF table |

---

## 升级决策

### ✅ 升级到正文: Per-Task Decomposition (Appendix B → §4.1)

**目标 section**: §4.1 Death Decomposition (核心结果)

**理由**: Per-task table 是 C1 的核心支撑数据 — 展示 DAF 的 bimodal distribution (find-non-living vs 其他 10 tasks)、label 分布、death rate 差异。Short paper 空间不足才放 appendix。

**需要的扩展**:
- 增加 Δ_nd 列和 per-task DAF 列（目前只有 Δ_full）
- 增加 1–2 句 per-task analysis 文字（bimodal pattern, find-non-living exception）
- 估计空间: ~0.5 page（表格 + 文字）

**影响**: Scatter plot (Fig 3) + per-task table (Tab 2) 放在一起，形成 §4.1 的完整 evidence chain。

---

### ✅ 升级到正文: Router Architecture Comparison (Appendix D 部分 → §4.5)

**目标 section**: §4.5 Ablations

**理由**: Logit-generation gap 是重要的 negative finding，暴露 classification head 的根本架构缺陷。GA effect 也是关键发现（GA=1 degenerate vs GA=8 non-degenerate）。Short paper 将这些压在 appendix 里削弱了 narrative。

**需要的扩展**:
- 整合为一张对比表: classification head (logit vs gen metrics) + implicit router (4-seed gen metrics)
- 加 logit-generation gap 的简要讨论 (2–3 sentences)
- 保留 hyperparameter detail table 在 appendix
- 估计空间: ~0.4 page

**影响**: 升级后 §4.5 有完整的 ablation story: architecture comparison + GA fix + keyword baseline failure。

---

### ✅ 升级到正文: Keyword Routing Structural Failure (Appendix 无，仅一句话 → §4.5)

**目标 section**: §4.5 Ablations

**理由**: Short paper 只用一句话 "Keyword-based routing fails structurally" 提了 plan-011 结果。Long paper 应展开为一个小 subsection 或 paragraph + table (v1/v2/v3 match rates)。这回应了 reviewer concern "rule-based baseline missing"。

**需要的扩展**:
- 新建 Table 8: keyword lists + match rates + routing behavior
- 解释 root cause: ScienceWorld actions 用 generic verbs
- 估计空间: ~0.3 page

---

### ⚠️ 部分升级: Labeling Quality Audit (Appendix A → 核心数据到 §4.1, detail 留 appendix)

**目标 section**: §4.1 + Appendix

**理由**: "100% genuine labels, 0% tie-break artifacts" 这个结论太重要了不应只在 appendix。但详细的 breakdown (70 death-asymmetry + 16 score-comparison etc.) 可留 appendix。

**升级内容** (到正文 §4.1 或 §4.5):
- 核心结论: 100% genuine, 0% artifact, strict retrain within 1σ
- Step-level tie rate 97.4% 的 motivating role
- 估计空间: ~2 sentences + 可能 1 行 inline data

**保留 appendix**:
- Tie rate 的 both-alive / both-died breakdown
- Strict retrain 的 detailed metrics (per-class recall etc.)
- 训练 label 的 death-asymmetry vs score-comparison breakdown

---

### ⚠️ 部分升级: Penalty Sensitivity (Appendix E → 核心公式到 §3, table 留 appendix)

**目标 section**: §3 Method (DAF definition)

**理由**: Δ_full(P) = δ·P + Δ_nd 公式和 "DAF 单调递增于 P" 是 DAF 定义的数学性质，应在 Method section 讨论而非只在 appendix。但完整的 P vs DAF table 可留 appendix。

**升级内容** (到正文 §3.3):
- DAF(P) = δP/(δP + Δ_nd) 公式
- 一句话: DAF increases monotonically with P — 数学性质而非经验发现
- 引入 penalty-independent companion metric (78.9% death-asymmetry label fraction)
- 估计空间: 已部分在 short paper §3.3 中实现，long paper 可更展开

**保留 appendix**:
- 完整 P ∈ {10, 25, 50, 100, 200} table
- Δ_nd 两种定义的差异说明 (strict vs inclusive both-died)

---

### ❌ 保留 Appendix: Correlation Robustness (Appendix C)

**理由**: LOO table、Spearman ρ、bootstrap CI 属于统计诊断细节。正文引用结论 (r = 0.97, robust across diagnostics) 已足够，详细 LOO 表格对主 narrative 贡献有限。

**保留内容**: 完整保留 Appendix C。正文 §4.1 引用 "See Appendix for robustness diagnostics"。

---

### ❌ 保留 Appendix: Hyperparameter Table (Appendix D 部分)

**理由**: 具体 hyperparameters (LoRA r/α, LR, optimizer, etc.) 是 reproducibility detail，不需要在正文。

**保留内容**: Tab A3 (hyperparameter table) 保留 appendix。Router comparison table (architecture-level 对比) 升级到正文。

---

## 新增 Appendix 内容 (Long Paper)

以下内容不在 short paper 中，long paper 需新增到 appendix:

| 内容 | 来源 | 说明 |
|---|---|---|
| 30-Task Prescreening Robustness | paper_framing.md | 30 tasks / 249 eps, DAF=98.75%, r=0.9864。仅 appendix |
| Step-Level Tie Rate by Task | plan-012-step-tie-rate | 11 tasks 的 per-task step tie rate breakdown |
| MATH Per-Level Breakdown | math-negative-contrast | Level 4 vs Level 5 accuracy 分开报告 |
| ALFWorld Per-Task-Type Results | alfworld-counterfactual-full | 6 task types 的详细结果 |
| 4-Seed Router Variance | plan-004-ablation-b | Bar chart: 4 seeds 的 balanced acc / internal recall |

---

## 空间预算

| 升级内容 | 估计空间 |
|---|---|
| Per-task decomposition table → §4.1 | 0.5 page |
| Router architecture comparison → §4.5 | 0.4 page |
| Keyword routing failure → §4.5 | 0.3 page |
| Labeling audit core → §4.1 inline | 0.1 page |
| Penalty sensitivity formula → §3 | 0.1 page |
| **Total appendix→正文升级** | **~1.4 pages** |

Long paper 从 4→8 pages = +4 pages。其中:
- Introduction 扩展: +0.5 page (motivating figure, more context)
- Related Work 新增: +1.0 page
- Method 扩展: +0.5 page (pipeline figure, algorithm box, formalism)
- §4.2 Multi-Model Validation: +0.5 page (new)
- §4.3 MATH Cross-Domain: +0.5 page (new)
- §4.4 Temporal Analysis: +0.3 page (new)
- Appendix 升级到正文: +1.4 page (from above)
- Discussion 扩展: +0.2 page
- **Total**: ~4.9 pages → 需要 tight writing，但可行

**结论**: 大部分新空间用于新 sections (Related Work, Multi-Model, MATH, Temporal) 和 appendix 升级。关键是正文展示核心数据而非只引用 appendix。
