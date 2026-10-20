# writing notation figures audit

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_notation-figures-audit_20260514T054927_result.json`
- **Structured JSON:** [`f579a41f9368609274bb.json`](../../sessions/f5/f579a41f9368609274bb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All fixes applied. Here's the report:

---

## 1. Notation 修复列表

| 位置 | 问题 | 修复 |
|------|------|------|
| `main.tex:34` (abstract) | 裸 "AUC" ×2（`yield AUC above`, `(0-vs-1) AUC exceeding`） | → `$\auc$` |
| `main.tex:34` (abstract) | `$\Kstar=2$`（15-feature 上下文中应为 empirical） | → `$\Kempirical=2$` |
| `appendix.tex:7` (caption) | `$\Kstar=2$`（指 empirical 结果） | → `$\Kempirical=2$` |

**无问题项：**
- `$\theta$`：全文统一使用 math mode，无裸 θ
- `≥ ≤ × ±`：无 Unicode 裸字符，全部使用 LaTeX 命令（`\leq`, `\geq`, `\times`, `\pm`）
- `$\auc$` macro：除 abstract 中已修复的两处外，其余全部通过 macro 使用
- `\Kstar` / `\Kempirical` / `\Ktheory`：正文中使用一致（generic concept 用 `\Kstar`，empirical result 用 `\Kempirical`，theoretical bound 用 `\Ktheory`）

## 2. Caption 状况

所有 caption 均自包含，无未展开缩写。具体评估：

- **Table 1** (`tab:features`): 简短但 table 内有 Group/Feature/Description 列，可接受
- **Table 3** (`tab:kstar_ci`): 自包含，定义了 threshold 条件
- **Figure 2** (`fig:auc_decay`): 优秀，完整描述了图中所有视觉元素
- **Table 4** (`tab:transfer_matrix`): 解释了矩阵结构和 retention 计算方式
- **Figure 3** (`fig:transfer_heatmap`): 自包含，有定量结论
- **Table 5** (`tab:top_features`): 解释了 bold 含义，包含 Spearman ρ 数值
- **Figure S1** (`fig:s1_auc_decay_ci`): 自包含（已修复 `\Kstar` → `\Kempirical`）

无需进一步修改。

## 3. Cross-reference 问题

| 位置 | 问题 | 修复 |
|------|------|------|
| `discussion.tex:136` | `\ref{sec:graduated-filtering}` 指向不存在的 label（对应 section 在 main.tex 中已注释） | 移除 `Section~\ref{...}`，改为纯文本 |

**其余 cross-ref 均完整：** 全部 33 个 `\ref{...}` 目标（17 个 section、5 个 table、3 个 figure、3 个 equation）都有对应 `\label{...}` 定义。无硬编码的 "Figure X" / "Table X" / "Section X"（仅注释中有）。无 `??` 输出。

---
