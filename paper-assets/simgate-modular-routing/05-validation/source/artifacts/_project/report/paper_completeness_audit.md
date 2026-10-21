# Paper Completeness Audit — 2026-05-14

**Target**: EMNLP 2026 ARR short paper (4 pages), DDL 5/25, 初稿 5/17
**Primary source**: `artifacts/_project/paper/latex/` (8 .tex files + 1 .bib + fig1 + compiled PDF)

---

## Section-by-Section Status

### ✅ Abstract (`abstract.tex`, 3 lines)
- Framing 一致：counterfactual analysis → death avoidance ~90% → r=0.97
- 数字正确：97.4% tie rate, 245 episodes, DAF "approximately 90%", r=0.97
- 缺少 Δ_full/Δ_nd 具体值（可选，word budget 紧张）
- **状态：完成，可直接用**

### ✅ Introduction (`introduction.tex`, 13 lines)
- Story arc 完整：hallucinated transitions → per-step degeneracy → episode-level solution → death avoidance finding
- 所有硬约束数字正确：Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698, p=8.12e-07, 97.4% tie rate
- Label distribution (86/9/150), death rates (42.9%/16.3%), oracle degeneracy (96.3%) 均在
- Contributions 列表 2 项，与 framing C1/C2 对齐
- **状态：完成**

### ✅ Method (`method.tex`, 32 lines)
- §3.1 Counterfactual Episode Collection ✅
- §3.2 Death-Aware Labeling（四分类）✅
- §3.3 DAF 定义与公式 ✅
- 缺少 writing_plan 提到的"deterministic mode operational definition for ScienceWorld"（minor，可加一句）
- writing_plan 的 §3.4 Rule-Based Baseline 实际放在了 experiments §4.2，结构上可接受
- **状态：完成，minor polish 可选**

### ⚠️ Experiments (`experiments.tex`, 64 lines)
- §4.1 Death Avoidance Decomposition ✅ — 所有核心数字正确
- §4.2 Baselines ✅ — Table 1 数字锁定值全部正确
- §4.3 Router Training as Diagnostic ✅ — logit-generation gap, multi-seed results
- Fig 1 (fig1_daf_scatter.pdf) 引用 ✅，文件存在 ✅
- find-non-living-thing exception 在 §4.1 内 ✅

**问题 1 — Table 2 缺失**：writing_plan 指定了 `tab2_decomposition`（per-task breakdown: Task, N, Δ_full, Δ_nd, DAF%, DR_int%, DR_det%），但 experiments.tex 中不存在。11 个 task type 的详细分解只有文字描述（find-non-living-thing），无表格。
→ **优先级：HIGH** — 这是核心 claim 的支撑证据，reviewer 会期望看到 per-task 数据

**问题 2 — CI 值不一致**：Table 1 的 95% CI 与 writing_plan 不同：
| Strategy | Paper CI | Writing Plan CI |
|----------|----------|-----------------|
| Always-Int | [-46.40, -32.27] | [-44.89, -33.37] |
| Always-Det | [-14.71, -4.29] | [-13.66, -5.11] |
| Oracle | [-11.54, -1.70] | [-10.65, -2.43] |
| Random | [-28.67, -15.75] | [-27.75, -17.09] |

Mean scores 一致，CI 不一致。需要确认哪组是 plan-012-full/plan-003 的权威数据。
→ **优先级：MEDIUM** — 数值准确性问题，必须 resolve

- **状态：核心内容完成，缺 Table 2 + CI 需验证**

### ✅ Related Work (`related_work.tex`, 27 lines)
- Tool-use learning: Toolformer, ART, Chameleon, ReTool ✅
- Adaptive computation: CogRouter, ARES, Mixture-of-Recursions ✅
- World model routing: ITP, Dyna-Think ✅
- Agent frameworks: ReAct, MTRouter ✅
- 缺少 EnvSimBench（writing_plan 标记 needs_search）— minor for short paper
- **状态：完成，EnvSimBench 为 nice-to-have**

### ✅ Discussion (`discussion.tex`, 13 lines)
- MATH pilot 数据在：80% vs 72%, label distribution (1/5/44) ✅
- 两个 TODO comment 标记 math-200-fixed 和 ALFWorld — 可接受为 placeholder
- Scope & future directions paragraph 在 ✅
- **状态：完成（TODO comments 无影响，编译不显示）**

### ✅ Conclusion (`conclusion.tex`, 3 lines)
- 核心数字 ✅：DAF=90.41%, Δ_full=+29.60, Δ_nd=+2.84, r=0.9698
- Oracle degeneracy (96.3%), router accuracy (58.1%) ✅
- Cross-environment reference ✅
- Limitations 和 future work 在 main.tex 的 Limitations section，不在 conclusion 里——结构合理
- **状态：完成**

### ✅ Limitations (`main.tex` lines 24-29)
- 单 benchmark、单 LLM、death penalty amplification、step-level extension ✅
- Labeling quality audit（245 labels 全审计，零 tie-break artifacts）✅
- 非常详尽，质量高
- **状态：完成**

### ✅ Ethics Statement (`main.tex` lines 31-33)
- ScienceWorld public dataset, no human subjects ✅
- GPU hours: ~40 GPU-hours on 2× RTX 5090 ✅
- **状态：完成**

### ✅ References (`references.bib`, 12 entries)
- 核心引用全在：ScienceWorld, Toolformer, ART, Chameleon, ReTool, ReAct, CogRouter, ARES, MoR, ITP, Dyna-Think, MTRouter
- DAgger (Ross et al. 2011) 在 bib 但未在正文 `\cite{}` — 要么引用要么删除
- 缺少 EnvSimBench（同 Related Work）
- **状态：基本完成，minor cleanup**

### ✅ Figure 1 (`fig1_daf_scatter.pdf`)
- 文件存在，experiments.tex 正确引用
- **状态：完成**

### ✅ Main Document Structure (`main.tex`)
- 编译顺序：abstract → intro → method → experiments → related_work → discussion → conclusion → limitations → ethics → references
- ACL template ✅ (`\usepackage[review]{acl}`)
- Compiled PDF exists (`main.pdf`)
- **状态：完成**

---

## 硬约束验证

| 约束 | 论文中的值 | 要求值 | 状态 |
|------|-----------|--------|------|
| Trained router score | -10.70 | -10.70 | ✅ |
| Always-det score | -9.47 | -9.47 | ✅ |
| Oracle score | -6.58 | -6.58 | ✅ |
| Step tie rate | 97.4% | 97.4% | ✅ |
| DAF | 90.41% | 90.41% | ✅ |
| Pearson r | 0.9698 | 0.9698 | ✅ |
| p-value | 8.12e-07 | 8.12e-07 | ✅ |
| Δ_full | +29.60 | +29.60 | ✅ |
| Δ_nd | +2.84 | +2.84 | ✅ |

**所有硬约束数字通过。**

---

## 缺口清单（按优先级）

### 5/17 前必须完成

| # | 问题 | Section | 工作量 | 说明 |
|---|------|---------|--------|------|
| 1 | **Table 2 缺失** | Experiments | 1-2h | Per-task decomposition 表（11 rows: Task, N, Δ_full, Δ_nd, DAF%, DR_int%, DR_det%）。数据在 plan-012-full registry，需提取并格式化。这是 DAF claim 的逐 task 证据，reviewer 必看。 |
| 2 | **CI 值不一致** | Experiments | 0.5h | Table 1 的 bootstrap CI 与 writing_plan 不同。需回溯 plan-003/plan-012 数据确认权威值。 |

### Nice-to-have（5/17 后可补）

| # | 问题 | Section | 工作量 | 说明 |
|---|------|---------|--------|------|
| 3 | DAgger 引用孤立 | references.bib | 5min | `dagger-2011` 在 bib 但未被 `\cite{}`。要么在 Limitations 中引用（DAgger gap 讨论），要么删除。 |
| 4 | EnvSimBench 引用缺失 | Related Work | 0.5h | writing_plan 标记 needs_search。如找到合适引用可加入 World Model Routing 段落。 |
| 5 | Deterministic mode 操作定义 | Method | 15min | writing_plan 要求 Method 中解释 ScienceWorld 的 deterministic mode 具体如何工作（"equivalent to giving the agent a perfect world model" 已有一句，可扩展）。 |
| 6 | writing_plan abstract "98% ties" | writing_plan.yaml | 5min | writing_plan 写的是 "98% ties"，实际论文正确用 97.4%。修正 writing_plan 保持一致。 |
| 7 | 页数检查 | 全文 | 0.5h | 7 个 content section + Limitations + Ethics + References。4 页 short paper 可能偏紧，需编译后检查是否超页。Discussion 和 Related Work 合计约 40 行，可能需要压缩。 |

---

## 总结

论文初稿**完成度约 90%**。所有 section 已有实质内容，硬约束数字全部正确，framing 与 paper_framing.md 一致。

**唯一 blocking 缺口**是 Table 2（per-task decomposition），这是核心 claim 的直接证据表。CI 值不一致需要快速验证。其余均为 minor polish。

5/17 初稿可交——补上 Table 2 + 确认 CI 即可。
