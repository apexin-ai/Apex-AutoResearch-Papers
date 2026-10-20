# paper page budget analysis

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_page-budget-analysis_20260514T114444_result.json`
- **Structured JSON:** [`feb3f4a5dca8aece5d44.json`](../../sessions/fe/feb3f4a5dca8aece5d44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据已收集完毕。以下是完整的 page budget 分析报告。

---

## 论文 Page Budget 分析报告

### 一、各 Section 精确统计

| Section | 文件 | 原始字数 | 行数 | 表格 | 图 | 公式 | 预估页数(双栏) |
|---------|------|---------|------|------|-----|------|----------------|
| Title + Abstract | abstract.tex | 292 | 14 | 0 | 0 | 0 | **0.7** |
| §1 Introduction | introduction.tex | 644 | 33 | 0 | 0 | 0 | **0.75** |
| §2 Related Work | related_work.tex | 659 | 39 | 0 | 0 | 0 | **0.75** |
| §3 Background | background.tex | 941 | 112 | 0 | 0 | 6 | **1.6** |
| §4 Experimental Setup | methodology.tex | 1002 | 78 | 0 | 0 | 1 | **1.5** |
| §5 Results | results.tex | 2370 | 199 | 5 | 4 | 0 | **4.0** |
| §6 Analysis | analysis.tex | 1156 | 94 | 2 | 0 | 1 | **1.8** |
| §7 Discussion | discussion.tex | 1859 | 102 | 0 | 0 | 0 | **1.8** |
| §8 Conclusion | conclusion.tex | 476 | 31 | 0 | 0 | 0 | **0.55** |
| **主体合计** | | **8399** | **702** | **7** | **4** | **8** | **≈13.5** |
| Title/Abstract | | | | | | | **+0.7** |
| **8页限制内总计** | | | | | | | **≈15.2** |
| References | main.bbl | — | — | — | — | — | ~1.5 |
| Appendix | appendix.tex | 239 | 11 | 0 | 0 | 0 | ~0.3 |
| **全文** | | | | | | | **≈17.0** ✓ |

**需要裁掉: 15.2 → 8.0 = 砍 7.2 页 (47%)**

---

### 二、逐 Section 分析：必留 vs 可移

#### Title + Abstract (0.7p) → 目标 0.5p | 省 0.2p
- **必留**: 核心 claims 的 one-sentence summary
- **可精简**: 当前 abstract 含过多数字细节（具体的 $d_z$ 值、p-value、每个 sparsity level 的具体 II 值）。Abstract 只需报最强结果 + crossover 现象，具体数字留给正文
- 建议：从 ~220 渲染词压到 ~150 词

#### §1 Introduction (0.75p) → 目标 0.6p | 省 0.15p
- **必留**: motivation（compound sparsity 问题）、central finding、3 contributions
- **可精简**: 第 2-3 段的具体数字重复了 abstract；roadmap 段（"The remainder of this paper..."）可删
- 建议：删 roadmap 句；合并数字段

#### §2 Related Work (0.75p) → 目标 0.4p | 省 0.35p
- **必留**: 每个 subsection 的 gap statement（最后 1-2 句）
- **可大幅精简**: 
  - §2.1 Compound Compression: 7 篇引用展开过多，可压缩为 2-3 句综述 + 引用列表
  - §2.2 KV Cache Eviction: 8 篇逐一展开，可压为 3 句综述
  - §2.3 Phase-Aware Inference: 6 篇逐一展开，可压为 2 句
- 关键策略：**每个 subsection 只保留 gap statement + 2-3 句概括**，具体引用方法用 `\cite{a,b,c}` 列举不展开

#### §3 Background (1.6p) → 目标 0.7p | 省 0.9p ⭐ 高收益
- **必留**: Eq. (1) II 定义, Eq. (2) Severity Gradient 定义, Phase Segmentation 的核心思路
- **可移到 appendix**:
  - §3.1 Compound Sparsity Formulation 的 head pruning / KV eviction 数学细节 (Eq. head-mask, kv-mask, kv-importance) → 这些是 standard 方法，reviewer 不需要在正文看完整公式
  - "Choice of additive null" 段 → 已经有 Appendix A 做了验证
  - Phase Segmentation 的 Eq. (attn-sparsity) → 用文字描述即可
- 建议：**6 个公式减到 2 个**（只留 II 和 G 的定义），其余移 appendix

#### §4 Experimental Setup (1.5p) → 目标 0.7p | 省 0.8p ⭐ 高收益
- **必留**: Models（2 句）, Dataset（1 句）, Sparsity levels, 两种 eviction strategy 的名称
- **可移到 appendix**:
  - §4.1 Models 的第二段细节（bfloat16 footnote、NaN 问题）
  - §4.3 Compound Sparsity Config 的 Eq. (importance) → 与 Background 重复
  - §4.4 Phase Segmentation → 与 §3.3 大量重复，可直接引用 "as defined in §3.3"
  - §4.5 Metrics → PPL 和 II 定义重复 Background
  - §4.6 Statistical Analysis 的 bootstrap 细节 → 移 appendix
- 建议：**合并 §3+§4 为一个 section**，避免重复定义

#### §5 Results (4.0p) → 目标 2.5p | 省 1.5p ⭐ 核心但可压缩
- **绝对不能动**:
  - §5.2 C1: Table 1 (aggregate-ii) + 解读段
  - §5.3 C2: Table 2 (main-results) + dose-response 核心结论
  - §5.4 C3: Crossover 数据 + 解读（但可压缩展开文字）
  - §5.5 C5: Cross-model replication 核心结论
- **可精简**:
  - §5.1 Experimental Overview → **删除**，与 §4 完全重复
  - §5.6 Statistical Validation: Table 3 (permutation) + Table 4 (cohens-d) + Fig 4 (forest plot) → **移 1 个 table + Fig 4 到 appendix**，正文只引用关键数字
  - **4 个 figure → 保留 2 个**：最有力的 dose-response 图 + crossover 图。Forest plot 和其他移 appendix
  - **5 个 table → 保留 2-3 个**：aggregate-ii + main-results 必留；permutation 和 cohens-d 合并或移 appendix
- C6 (sub-exponential growth) 段内联到 C2 中一句话提及即可

#### §6 Analysis (1.8p) → 目标 0.6p | 省 1.2p ⭐ 高收益（C4 已降级）
- **必留**: Discrimination collapse 的核心论点（1 段文字）
- **可移到 appendix**:
  - Table 5 (discrimination-metrics) → appendix
  - Table 6 (entropy-deltas) → appendix
  - §6.2 Entropy Redistribution 整个 subsection → appendix（仅部分复现）
  - §6.3 Implications 段 → 移到 Discussion 中 1-2 句
- 建议：正文只留 **~0.5p 的 mechanism overview**，所有量化证据表格移 appendix

#### §7 Discussion (1.8p) → 目标 0.5p | 省 1.3p ⭐⭐ 最高收益
- **必留**: 
  - "Random masking as falsification control" 的核心论点（2 句）
  - Limitations 段的核心 3 条
- **可大幅删除/移 appendix**:
  - "On the predictability of phase-modulated severity" → 这是 preemptive rebuttal，不是 contribution，**整段删**（审稿时放 rebuttal letter）
  - "Cross-model replication and magnitude asymmetry" → 结果已在 §5.5 报告过，**删**
  - "Model-dependent onset threshold" → 重复 §5.5 讨论，**删**
  - "Role of distillation-based training" → 推测性内容，**删**
  - "Statistical scope" → 移 appendix
  - "Sparsity range" → 移 appendix 或删
  - "No throughput evaluation" → 1 句限制声明即可
  - 所有 `% REVIEWER-ATTACK / REBUTTAL` 注释块：不渲染但占心智空间
- 建议：Discussion 压缩为 **Limitations 段（4-5 条 bullet）**，直接放在 Conclusion 之前

#### §8 Conclusion (0.55p) → 目标 0.3p | 省 0.25p
- **必留**: 5 个 claims 的 one-liner summary
- **可精简**: 当前 C1-C6 每条 2-3 句，可各压到 1 句。Limitations 段如果 Discussion 已有则**删**（避免重复）。Future work 压到 1 句
- 建议：conclusion 只列 contributions 的 bullet list + 1 句 future work

---

### 三、裁剪优先级排序

| 优先级 | 操作 | 预估省页数 | 风险 |
|--------|------|-----------|------|
| P1 | §7 Discussion 从 1.8p 砍到 0.5p（删 preemptive rebuttals + 重复分析） | **1.3p** | 低 — 内容重复或防御性 |
| P2 | §6 Analysis 从 1.8p 砍到 0.6p（表格移 appendix，只留 mechanism overview） | **1.2p** | 低 — C4 已降级 |
| P3 | §3 Background 从 1.6p 砍到 0.7p（4 个公式移 appendix） | **0.9p** | 低 — standard formulation |
| P4 | §4 Methodology 从 1.5p 砍到 0.7p（删重复定义、细节移 appendix） | **0.8p** | 低 — 实验细节 |
| P5 | §5 Results 精简（删 §5.1，2 个 table + 2 个 figure 移 appendix） | **1.5p** | 中 — 需谨慎选择保留哪些 |
| P6 | §2 Related Work 从 0.75p 压到 0.4p | **0.35p** | 低 — 综述压缩 |
| P7 | Abstract 精简 | **0.2p** | 低 |
| P8 | §8 Conclusion 从 0.55p 到 0.3p | **0.25p** | 低 |
| P9 | §1 Introduction 微调 | **0.15p** | 低 |
| **合计** | | **≈6.65p** | |

剩余 ~0.55p 差距通过全文句级精简（去冗余修饰词、合并短句）补齐。

---

### 四、推荐 8 页版本目录结构

```
Title + Abstract                          0.5p
§1 Introduction                           0.6p
§2 Related Work                           0.4p
§3 Background & Experimental Setup        1.3p  ← 合并原 §3+§4，去重
§4 Results                                2.5p  ← 原 §5，保留 C1/C2/C3/C5/C6 核心
   §4.1 Strategy-Dependent Severity (C1)
   §4.2 Dose-Response (C2+C6)
   §4.3 Phase-Strategy Crossover (C3)
   §4.4 Cross-Model Replication (C5)
§5 Analysis                               0.6p  ← 原 §6，只留 discrimination collapse 概述
§6 Discussion & Limitations               0.5p  ← 合并原 §7+§8，bullet 格式
§7 Conclusion                             0.3p
──────────────────────────────────────────
主体合计                                   6.7p
Title + Abstract                          +0.5p → 用到第 1 页 
余量 (句级微调)                            ~0.8p
──────────────────────────────────────────
总计                                      ≈8.0p

Appendix (不计页数):
  A. Compound Sparsity Formulation (原 §3.1 公式)
  B. Phase Segmentation Details (原 §3.3 公式)
  C. Full Experimental Details (原 §4 细节)
  D. Statistical Validation (permutation tables, forest plot, bootstrap details)
  E. Discrimination Collapse Evidence (原 §6 的 Table 5+6)
  F. Entropy Redistribution Analysis (原 §6.2)
  G. Multiplicative Null Verification (已有)
```

### 五、核心论证链（不可删除的内容）

1. **II 和 G 的定义**（各 1 个公式）→ 读者理解后续所有数字的基础
2. **Table 1 (aggregate-ii)** → C1 的直接证据
3. **Table 2 (main-results)** → C2 的直接证据，含 severity gradient
4. **Crossover 数据**（§5.4 的 4 个数字）→ C3 的直接证据
5. **Cross-model 的 $d_z$ 和 Spearman $\rho$** → C5
6. **Random baseline 的 7/8 FAIL** → C6
7. **Discrimination collapse 论点**（文字，无需表格）→ C4 supporting

其余所有内容均为「支持性细节」，可安全移入 appendix。

---
