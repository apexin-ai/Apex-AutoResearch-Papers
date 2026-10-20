# research paper consistency check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-consistency-check_20260514T094622_result.json`
- **Structured JSON:** [`bc354d6afe6ac1637921.json`](../../sessions/bc/bc354d6afe6ac1637921.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I've collected all registry data and read all paper sections. Now compiling the cross-check report.

---

## 数字一致性检查报告

### ✅ 一致的数字

**SciERC 主表 (§5 inline table + paper_tables_draft Table 1)**：所有 20 个单元格与 registry 完全一致。

| 指标 | Unconstrained | Grammar | Semantic | Full S1 | Full S2 |
|------|:-:|:-:|:-:|:-:|:-:|
| DR | 15.37% ✅ | 14.84% ✅ | 11.65% ✅ | 0.93% ✅ | 0.97% ✅ |
| RV | 1.39% ✅ | 0% ✅ | 1.51% ✅ | 0% ✅ | 0% ✅ |
| ET | 0.40% ✅ | 0% ✅ | 0.40% ✅ | 0% ✅ | 0% ✅ |
| CF | 0.08% ✅ | 0.08% ✅ | 2.71% ✅ | 9.90% ✅ | 8.03% ✅ |
| R-F1 | 8.23 ✅ | 8.23 ✅ | 8.15 ✅ | 8.36 ✅ | 8.03 ✅ |
| E-F1 | 31.01 ✅ | 30.98 ✅ | 31.01 ✅ | 30.98 ✅ | 31.90 ✅ |

**Per-relation DR (Table 2)**：7 行全部一致 (Compare 42.4→2.8, Feature-of 33.5→1.2, Part-of 25.0→0, Evaluate-for 24.1→5.8, Hyponym-of 14.5→0, Used-for 0.8→0, Conjunction 0→0) ✅

**DocRED Phase 0 (Table 3)**：Minimal(18.7/28.9/7.5/96.4) 和 Schema-informed(12.8/18.4/0.6/94.5) 1dp 四舍五入均正确 ✅

**跨章节一致性**：
- Abstract "15.37%→0.93% (↓94%)" = §5 = §7 Conclusion ✅
- Abstract "+0.13pp" = §5 = §7 ✅
- Abstract "CF 0.08%→9.9%" = §5 "0.08%→9.90%" = §7 ✅
- §1 Intro "15.4%→0.9% (↓94%)" 与 §5 一致（不同精度）✅
- §6 Related Work "15.37%→0.93%", "R-F1 8.36 vs 8.23, +0.13pp" = §5 ✅
- §3 Violation Landscape per-relation 分子分母 (28/66, 163/486, 18/72, 32/133, 6/787, 0/32) 全部 = registry ✅

**派生数字**：
- ΔDR(S1) = 93.9% → paper 说 "94%" (合理四舍五入) ✅
- Semantic-only DR reduction = 24.2% → paper 说 "24%" ✅
- Schema prompt SciERC reduction = 62.4% → paper 说 "62%" ✅
- Schema prompt DocRED reduction = 31.3% ✅

---

### ❌ 不一致的数字

**1. §3 Violation Landscape line 52: DocRED schema-informed DR**

| | 论文中 | Registry 正确值 |
|--|--------|----------------|
| DR (2dp) | **12.80%** | **12.84%** |

文件：`section3_violation_landscape.tex:52`
原文：`DR drops from 18.70\% to 12.80\% ($-$31.3\%)`
问题：12.80% 应为 12.84%。31.3% 的相对降幅也验证了 12.84% 才对 ((18.70−12.84)/18.70 = 31.3%)，12.80% 得出的是 31.6%。

**2. §2 Background 内部矛盾：SciERC valid pairs 数值**

| | Line 11 | Line 14 |
|--|---------|---------|
| SciERC avg valid pairs | **3.73** | **26.1** |

文件：`section2_background.tex:11` vs `section2_background.tex:14`
- Line 11: "|σ(r)| ranges from 3 (Part-of) to 6 (Used-for) valid pairs per relation, with an average of 3.73 pairs"
- Line 14: "SciERC relations average 26.1 valid pairs (out of 36)"

两个数字用不同方式度量同一概念。3.73 来自显式列出的合法 type pair 集合 |σ(r)|；26.1 来自 |dom(r)| × |range(r)| 的独立乘积（Method §4 使用此定义）。论文需要统一——Method 用的是 dom/range 独立定义，所以 26.1 是对的，3.73 应该删除或注明不同度量。

---

### 📝 Placeholder 列表

| # | 文件 | 位置 | 内容 | 可用数据 |
|---|------|------|------|----------|
| 1 | `abstract.tex:15` | Abstract | `\placeholder{DocRED results.}` | DR 18.70%→10.19% (↓45.5%), RV 28.90%→0.03% (↓99.9%), ET 7.50%→0% (↓100%), R-F1 8.17 |
| 2 | `section7_conclusion.tex:20` | Conclusion | `\placeholder{DocRED DR result...}` | 同上 |
| 3 | `paper_tables_draft.tex:119` | Table 4 Cross-dataset | DocRED S1 = *TBD* | DR\_S1=10.19%, ΔDR=−8.5pp |

**注意**：`phase2_docred_full_s1` 和 `phase2_docred_grammar_only` 均已 DONE，placeholder 数据已就绪。`phase2_docred_unconstrained` 和 `phase2_docred_semantic_only` 仍 RUNNING——DocRED 完整消融表还差这 2 个实验。

---

### 建议修复清单

1. **`section3_violation_landscape.tex:52`**：`12.80\%` → `12.84\%`

2. **`section2_background.tex:11`**：要么删除 "with an average of 3.73 pairs"，要么加注释说明这是 joint pair 定义 vs §3 的 independent domain/range 定义 (26.1)。建议统一到 26.1（与 Method 一致）。

3. **填充 3 个 placeholder**（DocRED full\_s1 数据已就绪）：
   - Abstract: "On DocRED, OntoCoDec reduces DR from 18.70% to 10.19% (↓45%), with RV 28.90%→0.03% and ET 7.50%→0%."
   - Conclusion: 同上
   - Table 4: DR\_S1 = 10.2, ΔDR = −8.5

4. **DocRED 消融结果**：等 `phase2_docred_unconstrained` 和 `phase2_docred_semantic_only` 跑完后，补 DocRED 消融表。注意 DocRED grammar\_only DR=26.17% 高于 Phase 0 unconstrained 的 18.7%——公平对比需要 Phase 2 unconstrained baseline。

---
