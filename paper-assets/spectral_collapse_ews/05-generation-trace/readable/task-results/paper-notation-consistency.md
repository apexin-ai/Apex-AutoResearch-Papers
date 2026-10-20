# paper notation consistency

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_notation-consistency_20260519T181220_result.json`
- **Structured JSON:** [`da8be2162b31bf525db8.json`](../../sessions/da/da8be2162b31bf525db8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All `\cite{}` converted — zero bare `\cite{` remaining. The two `Gen 2` in table cells are acceptable (no line-break risk).

## 汇总

### 已修复：22 个问题

| 类别 | 数量 | 文件 |
|------|------|------|
| `\cite{}` → `\citep{}` (parenthetical引用) | 18 | introduction.tex (6), related_work.tex (8), experiments.tex (3), conclusion.tex (1) |
| `Gen 0--2` → `Gen~0--2` (段落标题缺 `~`) | 3 | experiments.tex (lines 44, 52, 55) |
| EWS 缩写首次展开 | 1 | introduction.tex line 16: 添加 "(EWS)" |

### 检查通过（无需修改）

- `$r_{\text{crit}}$` — 全文统一 ✅
- `$\widetilde{S}_t$` — 全文统一，无 `\tilde` 混用 ✅
- `$r_{\text{eff}}$` — 全文统一 ✅
- `$\sigma_1$` — 全文统一 ✅
- `$\Delta_t$` — 全文统一 ✅
- `$r{=}0.x$` thin space — 全文统一 ✅
- Table/Figure 引用 — 3 个 label 全部有对应 ref，无 undefined ✅
- En-dash `--` 数值范围 — 全文统一，无 hyphen 混用 ✅
- `\%` 格式 — 全文统一（无空格） ✅
- SLV 缩写 — abstract + introduction 均展开 ✅
- EMA 缩写 — method 首次使用时展开 ✅
- Subsection labels — 全部 `\ref` 有对应 `\label` ✅

### 待确认：2 个

1. **PPL 缩写**：仅出现在 Table 1/2 列头（`PPL`、`PPL growth`），正文均用全称 "perplexity"。作为 NLP 标准缩写可接受，但如需严谨可在 Table 1 caption 中注明。
2. **未被引用的 subsection labels**：`subsec:cross_scale` 和 `subsec:second_order` 定义了但未被 `\ref` 引用。如果需要正文交叉引用可补上。

---
