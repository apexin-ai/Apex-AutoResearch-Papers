# code paper final polish

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_paper_final_polish_20260525T104936_result.json`
- **Structured JSON:** [`64be25eb50a9341e028c.json`](../../sessions/64/64be25eb50a9341e028c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译通过，15 页不变。

---

## Final Polish 报告

### 已修复

| # | 文件 | 问题 | 修复 |
|---|------|------|------|
| 1 | results.tex Table 1 | CI 值缺少前导零 (`[.770, .832]`) | → `[0.770, 0.832]`（共 8 处） |
| 2 | results.tex L81 | fig:gradient_analysis caption 中 "Detach+BN" 与全文术语不一致 | → "Detach OCC" |
| 3 | related_work.tex L7 | "59pp" 缺少 thin space | → `59\,pp` |

### 需要确认（不自动修复）

**P1 — 检查 fig:gradient_analysis caption 与图的一致性**
Caption 写 "four conditions: Vanilla, Full OCC, Detach OCC, Full OCC+LN"，但 panel (a) 和 (c) 的描述还提到了 Random OCC。如果图中确实显示 5 个 condition，应改 "four" → "five" 并补 Random OCC 到列表中。

**P2 — 页数恰好 8 页**
主文（Abstract→Conclusion）结束于第 8 页底部，Bibliography 从第 9 页开始，Appendix 从第 12 页开始。正好踩在 CoRL 8-page 限制上，任何新增内容都会超页。

### 无问题项（已验证通过）

- **\ref / \cite 完整性**: 无 undefined reference、无 undefined citation。所有 46 个 bib 条目都被引用，所有引用都有对应 bib 条目。
- **Figure/Table 编号**: 所有 `\label{fig:...}` 和 `\label{tab:...}` 至少被 `\ref` 引用一次。
- **Appendix 交叉引用**: `\ref{app:per_task}`, `\ref{app:temporal}`, `\ref{app:training}` 均正确指向 Appendix 中的对应 label。
- **\todo{} 残留**: 仅 main.tex 有 `\newcommand{\todo}` 定义，无实际使用。
- **Em-dash**: 无 `---` 在正文中出现（Table 1 中 `---` 是缺失值标记，符合惯例）。
- **Caption 句号**: 所有 11 个 caption 均以句号结尾。
- **术语一致性**: BN/BatchNorm/BatchNorm2d 按 shorthand/prose/code 分层使用，一致。pp 全文统一使用 `\,pp` 格式。
- **数字格式**: 全文使用 `0.xxx` 格式（CI 已修复）。
- **数学公式**: 格式一致，无问题。

### 低优先级备注

- `\todo` 命令定义可在 camera-ready 时删除
- 目录中有未使用的 .tex 文件（experiment_setup.tex, experiments.tex, experiments_old.tex）
- "pp" 全文未展开为 "percentage points"——在 ML 论文中常见，但部分 reviewer 可能偏好首次展开

---
