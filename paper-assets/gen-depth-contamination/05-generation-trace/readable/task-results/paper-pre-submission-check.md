# paper pre submission check

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_pre-submission-check_20260519T095454_result.json`
- **Structured JSON:** [`854ed942e911569925b7.json`](../../sessions/85/854ed942e911569925b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have everything needed. Here's the full pre-submission check report.

---

## 论文 Pre-Submission 检查报告

检查对象：
- 主论文：`artifacts/dream_reports/dream_20260519T090934/best/paper.tex`（最新完整 draft，571 行）
- 组件文件：`artifacts/_project/paper/method.tex`、`experiments_c1.tex`、`code_crossmodel_table.tex`

---

### 1. Em-dash 清零检查

**主论文 paper.tex（dream report）：** ✅ 通过
- Unicode em-dash `—` (U+2014): 0 匹配
- 解释性 en-dash ` – ` (U+2013): 0 匹配
- LaTeX em-dash `---`: 0 匹配

**组件文件：** ⚠️ 需修复（如果合入最终稿）

`method.tex` 有 3 处 `---`：
- 第 31 行: `...generational identity---the \emph{information-theoretic...`
- 第 111 行: `...improved discrimination---a pathology that renders...`
- 第 183 行: `...the asymmetric transfer---continuation${\to}$rewrite...`

`experiments_c1.tex` 有 8 处 `---`：
- 第 94、182、257-258、273、292、316、323-324 行

如果主论文 dream paper.tex 是最终投稿版，则这些组件文件的 dash 不影响提交。但如果后续需要把组件文件内容合入，必须清理。

---

### 2. Undefined References 检查

⚠️ 有严重问题

**`??` 标记：** ✅ 未发现（但论文未编译，无法从 .log 确认）

**`\ref{}` 交叉引用：** ✅ 全部匹配
- 所有 `\ref{tab:...}` 和 `\ref{sec:...}` 都有对应 `\label{}`

**`\cite{}` 缺失：** ⚠️⚠️ 严重问题
- 主论文 paper.tex 中有 `\bibliographystyle{plainnat}` 和 `\bibliography{references}`
- 但**整篇论文 0 个 `\cite{}` 命令**
- Related Work 中提到多篇论文（DetectGPT, Fast-DetectGPT, Shumailov et al. 2024, Alemohammad et al. 2024, Dohmatob et al. 2024, DSIR, D4, DoReMi 等）全部以文本形式提及，没有使用 `\cite{}`
- 编译后 bibliography 将为空，所有作者年份引用都不会正确渲染
- **必须修复：为所有文内引用添加 `\cite{}`，确保 .bib 文件包含所有条目**

---

### 3. Abstract 模型数量描述检查

⚠️ 需修复

Abstract 声称：**"9 model configurations (6 architecture families, 1B--32B parameters)"**

**实际模型列表**（Introduction 第 134 行）：
Qwen-1.5B, Qwen-7B, Qwen-14B, Qwen-32B, LLaMA-3.1-8B, Mistral-7B, Pythia-1.4B, OLMo-1B = **8 个不同模型**

如果加上 Qwen rewrite+continuation 两种模式 = 9 configs，但这不是独立模型配置，描述有误导性。

**架构族数量错误：**
- Qwen, LLaMA, Mistral, GPT-NeoX (Pythia), OLMo = **5 个架构族**
- 论文声称 **6 个**，多算了 1 个
- Introduction 第 69 行尝试列举 6 个但实际只列了 5 个

**需更新数字：**
| 项目 | 论文声称 | 实际 | 需改? |
|------|---------|------|-------|
| Model configs | 9 | 8 模型 (或 9 含 rewrite) | 需统一口径 |
| Architecture families | 6 | **5** | ⚠️ 必须改为 5 |
| Domains | 4 | 4 | ✅ |
| Decoding strategies | 4 | 4 | ✅ |

**Code domain 描述**（Abstract 第 37 行）：
- 声称 "Code: 4/5 models across 3 architecture families"
- 论文实际测了 5 个模型 (Qwen-1.5B, LLaMA-8B, Mistral-7B, Qwen-7B, Pythia-1.4B)，4/5 达到 ceiling
- Qwen-1.5B 和 Qwen-7B 同属 Qwen 族，LLaMA, Mistral, GPT-NeoX = 共 **4 个架构族**（非 3 个）
- ⚠️ "3 architecture families" 应改为 "4 architecture families"

---

### 4. code_crossmodel_table.tex 嵌入检查

⚠️ 需确认

**嵌入状态：** 主论文 paper.tex 没有 `\input{}` 或 `\include{}`，所有表格都直接内联在 paper.tex 中。`code_crossmodel_table.tex` 未被引用。

**TBD 占位符状态：**
- `code_crossmodel_table.tex` 中 Mistral-7B-v0.3 全部为 TBD（第 18-24 行共 6 处）
- 但主论文 paper.tex 中已有 Mistral-7B Code 完整数据（K*=2, 1v2 AUC=0.6893）
- `code_crossmodel_table.tex` 缺少 Qwen-7B 列，而主论文已有 Qwen-7B Code 数据

**结论：** `code_crossmodel_table.tex` 与主论文数据不同步。如果这个文件不直接参与投稿则无影响，但应更新以保持一致。

---

### 5. 页数检查

⚠️ 多项问题

**无编译 PDF**（`_project/paper/` 目录无 .pdf/.log/.aux 文件）

**粗略估算：**
- paper.tex: 571 行, ~4988 词（含 LaTeX 命令）
- 正文 7 个 section（Abstract 至 Conclusion）
- **16+ 个表格**（大部分为 `[t]` 浮动表格）
- 至少 2 个 figure 引用（fig:auc_decay, fig:transfer_heatmap），但 figure 文件未包含

以 ACL 两栏格式估算，16+ 表格 + 正文文字量**大概率超过 8 页**。需要编译后确认。

**⚠️⚠️ 模板错误（最严重问题）：**
- 当前使用 `\documentclass[11pt,a4paper]{article}` + `geometry` 包
- **EMNLP 2026 要求使用官方 ACL 模板**（`acl_natbib` 或 `acl.sty`）
- 当前模板字号、栏宽、margin 全部不符合投稿要求
- **必须切换到 EMNLP 2026 官方模板后重新排版并确认页数**

---

### 汇总

| 检查项 | 状态 | 严重程度 |
|--------|------|---------|
| Em-dash 清零（主论文） | ✅ 通过 | — |
| Em-dash 清零（组件文件） | ⚠️ method.tex/experiments_c1.tex 有 `---` | 低（若不合入） |
| `??` undefined ref | ✅ 无 | — |
| `\ref` 交叉引用 | ✅ 全匹配 | — |
| **`\cite{}` 缺失** | **⚠️⚠️ 整篇 0 个 cite** | **🔴 Critical** |
| **架构族数量** | **⚠️ 声称 6 实际 5** | **需修复** |
| Code 架构族数量 | ⚠️ 声称 3 实际 4 | 需修复 |
| code_crossmodel_table 同步 | ⚠️ TBD 未更新 | 低 |
| **LaTeX 模板** | **⚠️⚠️ 非官方模板** | **🔴 Critical** |
| 页数 | ⚠️ 大概率超 8 页 | 需编译确认 |

**最紧急修复项：**
1. 补全所有 `\cite{}` 并确保 .bib 文件完整
2. 切换到 EMNLP 2026 官方 LaTeX 模板
3. 修正 "6 architecture families" → "5 architecture families"

---
