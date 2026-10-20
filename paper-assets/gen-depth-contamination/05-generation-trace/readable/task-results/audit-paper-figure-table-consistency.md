# audit paper figure table consistency

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper_figure_table_consistency_20260513T232830_result.json`
- **Structured JSON:** [`456338b62bd9a92ad683.json`](../../sessions/45/456338b62bd9a92ad683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

检查完成。以下是完整的修正项清单。

---

## 论文图文一致性检查报告

### 1. Caption 描述与图片内容不匹配

| 项 | 详情 |
|---|---|
| **文件** | `experiments_c1.tex:76` |
| **类型** | caption 不匹配 |
| **问题** | Caption 称 "four model-mode configurations (solid) and **four decoding strategies (dashed)**"，但 fig2_auc_decay 实际只有 4 条 solid 曲线（model-mode），**无任何 dashed 解码策略曲线**。Caption 还提到 "decoding strategy curves omit CIs as they were computed on a separate experimental setup"，同样无对应内容。 |
| **修正建议** | 要么从 caption 删除关于 decoding strategy dashed curves 的描述，要么在图中补画 4 条 dashed 曲线（exp_003 数据：greedy/nuc-0.9/T=0.7/T=1.2 的 1v2 AUC 分别为 0.6893/0.6866/0.6887/0.7039）。 |

### 2. 特征分组数目错误

| 项 | 详情 |
|---|---|
| **文件** | `method.tex:46` |
| **类型** | 数值不一致 |
| **当前值** | "organized into **five** groups" |
| **正确值** | "organized into **four** groups" |
| **依据** | Table 1 (tab:features) 明确只有 4 个分组：Surprisal moments (4)、Surprisal derivatives (5)、Vocabulary diversity (3)、Frequency tail (3)，共 15 维。 |

### 3. 重复 label `sec:generation_mode`

| 项 | 详情 |
|---|---|
| **文件** | `method.tex:167` + `experiments_c1.tex:294` |
| **类型** | 悬空引用 / 标签冲突 |
| **问题** | 两个文件都定义了 `\label{sec:generation_mode}`：method.tex 的 "Generation Mode Control" (§3.6) 和 experiments_c1.tex 的 "Generation Mode Effect" (§4.4)。LaTeX 会报 "multiply-defined label" 警告，`\ref{sec:generation_mode}`（出现在 experiments_c1.tex:104）将指向最后定义的那个。 |
| **修正建议** | 将 method.tex:167 改为 `\label{sec:generation_mode_method}`，experiments_c1.tex:294 保留 `\label{sec:generation_mode}`。或反之命名区分（如 `sec:gen_mode_exp`）。 |

### 4. 悬空引用 `\ref{sec:conclusion}`

| 项 | 详情 |
|---|---|
| **文件** | `introduction.tex:56` |
| **类型** | 悬空引用 |
| **问题** | `Section~\ref{sec:conclusion} concludes.` 引用了 `sec:conclusion`，但 `main.tex:53` 的 `\input{conclusion}` 已被注释掉。编译后显示为 "Section **??** concludes." |
| **修正建议** | 取消注释 `main.tex:53` 的 `\input{conclusion}`；或将 introduction.tex:52-56 的论文结构导航段落暂时注释掉。 |

### 5. `discussion.tex` 未被包含

| 项 | 详情 |
|---|---|
| **文件** | `main.tex` / `discussion.tex` |
| **类型** | 孤立标签 |
| **问题** | `discussion.tex` 定义了 6 个 label（`sec:discussion`, `sec:discuss_kstar`, `sec:discuss_transfer`, `sec:discuss_features`, `sec:discuss_llm`, `sec:limitations`），但 `main.tex` 中既无 `\input{discussion}` 也无被注释的版本。这些 label 当前无编译文件引用，不会报错，但 discussion 内容将缺失。 |
| **修正建议** | 在 main.tex 中 conclusion 之前加 `\input{discussion}`（或注释占位 `% \input{discussion}`）。 |

### 6. 跨模型转移 "comparably poorly" 表述不准确

| 项 | 详情 |
|---|---|
| **文件** | `experiments_c1.tex:183` |
| **类型** | caption / 文本不匹配 |
| **问题** | "The reverse direction performs comparably poorly." — 前向（Qwen-rw→Pythia/OLMo）保留率 61-63%，反向（Pythia/OLMo→Qwen-rw）保留率 70-72%（fig3 heatmap 可验证）。10pp 差距使 "comparably" 不太准确。 |
| **修正建议** | 改为 "The reverse direction also shows degraded transfer (70--72\% retention)" 或类似更精确的表述。 |

---

### 无问题项确认

| 检查项 | 结果 |
|---|---|
| `figures/fig2_auc_decay.pdf` 存在 | ✅ |
| `figures/fig3_transfer_heatmap.pdf` 存在 | ✅ |
| `figures/pipeline.pdf`（已注释） | ✅ 不影响编译 |
| `references.bib` 存在 | ✅ |
| tab:kstar_ci 全部数值 vs registry (exp_007) | ✅ 完全一致 |
| tab:transfer_matrix 全部数值 vs registry (exp_013) | ✅ 完全一致 |
| tab:top_features 排名 vs registry (exp_005) | ✅ 完全一致 |
| Spearman ρ 值 (caption of tab:top_features) vs registry | ✅ 完全一致 |
| Kendall τ 值 (§4.3 text) vs registry | ✅ 完全一致 |
| OBD vs multiclass MAE 数值 (§3.3) vs registry (exp_010) | ✅ 一致（四舍五入） |
| LLM zero-shot 数值 (§5.4) vs registry (exp_011) | ✅ 完全一致 |
| 解码消融数值 (§5.1, §5.3) vs registry (exp_003) | ✅ 完全一致 |
| Permutation p 值 (§4.1 text) vs registry | ✅ 完全一致 |
| fig3 heatmap 数值 vs table/registry | ✅ 完全一致 |
| 所有其他 `\ref` ↔ `\label` 对应 | ✅ 无额外悬空 |

---

**优先级排序**：问题 #1（caption-图不匹配）和 #4（悬空引用显示 "??"）最紧急——Reviewer 会直接看到。#2（五→四）是明显事实错误。#3（重复 label）会触发 LaTeX 警告。#5-#6 属于结构/措辞问题。

---
