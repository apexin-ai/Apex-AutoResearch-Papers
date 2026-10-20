# review caption consistency

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_review_caption_consistency_20260523T173725_result.json`
- **Structured JSON:** [`96a502fd86bd27069c51.json`](../../sessions/96/96a502fd86bd27069c51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Here's the full consistency check report.

---

## Figure/Table Caption 一致性检查报告

### 1. 所有 Figure/Table 列表

**Figures（按编译顺序）：**

| 编号 | Label | 文件 | Caption 简述 |
|------|-------|------|-------------|
| Fig 1 | `fig:teaser` | introduction.tex:13 | D-study projections for MMLU (single-model baseline) |
| Fig 2 | `fig:design_diagram` | method.tex:58 | Fully crossed G-theory design (7 facets) |
| Fig 3 | `fig:cross_benchmark` | experiments.tex:75 | Variance decomposition across 5 benchmarks and 8 models |
| Fig 4 | `fig:budget_sensitivity` | appendix.tex:137 | Budget sensitivity to estimation error |
| Fig 5 | `fig:difficulty_scatter` | appendix.tex:189 | Item difficulty heterogeneity vs item variance share |

**Tables（按编译顺序）：**

| 编号 | Label | 文件 | Caption 简述 |
|------|-------|------|-------------|
| Tab 1 | `tab:design_matrix` | method.tex:34 | Fully crossed G-theory design matrix |
| Tab 2 | `tab:cross_model` | experiments.tex:23 | Cross-model MMLU variance decomposition |
| Tab 3 | `tab:cross_benchmark` | experiments.tex:52 | Format-associated variance across 5 benchmarks |
| Tab 4 | `tab:dstudy` | experiments.tex:91 | D-study reproducibility budgets (single-model) |
| Tab 5 | `tab:lomo_full` | appendix.tex:25 | LOMO stability across 5 benchmarks |
| Tab 6 | `tab:fixed_vs_random` | appendix.tex:51 | Random vs fixed model G coefficients |
| Tab 7 | `tab:dstudy_cross` | appendix.tex:79 | Cross-model D-study budgets with CIs |
| Tab 8 | `tab:forward_pred` | appendix.tex:108 | Four-model vs eight-model consistency |
| Tab 9 | `tab:intermediate_dstudy` | appendix.tex:151 | Intermediate D-study designs |
| Tab 10 | `tab:subject_gstudy` | appendix.tex:201 | MMLU subject-level variance |
| Tab 11 | `tab:ff_residual` | appendix.tex:236 | FF residual variance regression |
| Tab 12 | `tab:model_ids` | appendix.tex:260 | Model HuggingFace identifiers |

---

### 2. Figure 1 caption vs Table 3 数字对比

**Figure 1 caption 中的数字**：552 items, 178 items, 55 items (MMLU single-model D-study budgets)
**Table 3 中的数字**：per-benchmark variance percentages (cross-model, 8 models)

这两者是**不同分析**（single-model D-study vs. cross-benchmark variance decomposition），不存在直接对应关系。Figure 1 的数字与 **Table 4**（`tab:dstudy`）对应，经核验全部一致：
- Multi-facet: 55 items, G_200 = .936 ✓
- Single-condition: 552 items, G_200 = .592 ✓
- 3p×3s moderate: 178 items (from Table 9) ✓

---

### 3. 正文数字 vs 表格数字一致性

**已验证一致的数字（✓）：**
- item_id 58.4% → 37.9% cross-model (experiments.tex:19 vs Tab 2) ✓
- model×item 30.2% (experiments.tex:19 vs Tab 2) ✓
- model×item up to 36% (HellaSwag, Tab 3) ✓
- MC item-related variance 68–72% (Tab 3 计算：68.1%, 71.6%, 70.3%) ✓
- FF item-related variance 31–41% (Tab 3 计算：31.5%, 41.3%) ✓
- HellaSwag exception 36.0% > 34.3% (Fig 3 caption vs Tab 3) ✓
- 552/55 = 10.0× budget ratio (experiments.tex:86 vs Tab 4) ✓
- IRT 116 items: G=0.457 single, G=0.895 multi (experiments.tex:109 vs Tab 4) ✓
- |ΔG| ≤ 0.029 MC, ≤ 0.065 FF (experiments.tex:109 vs Tab 8) ✓
- G_item 0.863–0.896 range (experiments.tex:113 vs Tab 5) ✓
- Fixed vs random ΔG 0.077–0.113 (experiments.tex:119 vs Tab 6) ✓
- Total records 460,800 and 2,304,000 (math verified) ✓
- 1,296 conditions per item (math verified) ✓
- 178 × 9 = 1,602 evaluations (math verified) ✓
- 55 × 1,296 = 71,280 evaluations (Tab 4) ✓
- ARC model×prompt 8.0%, GSM8K model×prompt 8.5% (method.tex:85 vs Tab 3) ✓

---

### 4. 发现的不一致/问题

#### 问题 A：Model main effect 范围不精确（experiments.tex:19）

正文：`model main effect is 3--5\% (MC) and 9--11\% (FF)`

Table 3 实际值：
- MC: MMLU **2.8%**, ARC 3.1%, HellaSwag 5.4% → 实际范围 **2.8–5.4%**，不是 3–5%
- FF: MATH **8.5%**, GSM8K 10.7% → 实际范围 **8.5–10.7%**，不是 9–11%

MMLU 的 2.8% 和 MATH 的 8.5% 都低于正文声称的下限。

#### 问题 B：Introduction 中 model×prompt "approximately 9%" 偏高（introduction.tex:4）

正文：`model×prompt interaction alone accounts for approximately 9%`（指 GSM8K）
Table 3：GSM8K model×prompt = **8.5%**

8.5% 说成 "approximately 9%" 是可以接受的近似，但作为 Introduction 中的关键数字，建议精确为 "approximately 8.5%" 或 "nearly 9%"。

#### 问题 C：Multi-facet budget "71 to 162 items" 混淆点估计与 CI（experiments.tex:111）

正文：`multi-facet budgets ranging from 71 to 162 items (Table~\ref{tab:dstudy_cross})`

Table 7 实际值：
- **点估计**范围：93–128 items
- **95% CI** 全范围：71（ARC 下限）– 162（GSM8K 上限）

正文的 71–162 是 CI 的极端边界，但写法 "budgets ranging from 71 to 162" 读起来像点估计范围。建议明确标注为 CI 范围。

#### 问题 D：三处硬编码章节号（应使用 `\ref{}`）

| 位置 | 硬编码 | 应引用的 subsection |
|------|--------|-------------------|
| experiments.tex:80 | `\S4.1` | Single-Model Baseline（无 label） |
| experiments.tex:113 | `\S4.6` | Preliminary Scale Validation（无 label） |
| limitations.tex:4 | `\S4.6` | 同上 |

这两个 subsection 缺少 `\label{}`，若章节重排，引用会错乱。

#### 问题 E：`\label{sec:partial_credit}` 定义但未引用

appendix.tex:42 定义了 `\label{sec:partial_credit}`，但全文无 `\ref{sec:partial_credit}`。

#### 问题 F：`docs/paper/sections/experiments.tex` 是过期版本

该文件包含旧数据（4 models, 239,200 records, item_id=61.1%, G=0.918），与当前 `docs/paper/experiments.tex`（8 models, 259,200 records, item_id=58.4%, G=0.936）严重不一致。`main.tex` 引用的是后者，但旧文件的存在可能造成混淆。

#### 问题 G：`fig3_dstudy_curves.pdf` 为孤立图片

`figures/paper/` 中存在 `fig3_dstudy_curves.pdf`，但无 tex 文件引用它。

---

### 5. Label 一致性

**所有 `\ref{}` 均指向已定义的 `\label{}`**，无悬空引用。✓

**未引用的 labels**（不影响编译，但可考虑清理）：
`sec:introduction`, `sec:related`, `sec:method`, `sec:gtheory`, `sec:exp001`, `sec:protocol`, `sec:conclusion`, `sec:partial_credit`, `app:ai-assistants`, `app:budget_sensitivity`

---

### 总结

- **严重问题**：0 个（无悬空引用、无数字矛盾到影响结论的程度）
- **需修正**：问题 A（model main effect 范围偏差）、问题 D（硬编码章节号）
- **建议改进**：问题 B（近似精度）、问题 C（CI 标注）、问题 F（删除旧文件）
- **低优先级**：问题 E（unused label）、问题 G（orphan figure）

---
