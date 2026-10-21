# audit dose response narrative

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_dose_response_narrative_20260524T071531_result.json`
- **Structured JSON:** [`fe1328578c25264d1971.json`](../../sessions/fe/fe1328578c25264d1971.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Dose-Response Narrative 完整性检查报告

### 1. α=2.0 GRPO 追平 CKA-only 的结论
**✅ 已有**

- `experiments.tex:62` — "increasing $\alpha$ from 1.0 to 2.0 shifts RASP from collapse to peak recovery (66.11% vs. 64.39% for CKA-only on GSM8K)"
- `appendix.tex:93` — "inverted-U pattern peaking at α=2.0 (SFT 64.97%, GRPO 66.11%)"
- `conclusion.tex:6` — "recovery peaks at α=2.0 (66.11%)"
- `tables/table3_alpha.tex:12` — 表格中 α=2.0 行加粗，GRPO 66.11%

数值完整，"追平/超过"语义通过 66.11% vs 64.39% 的对比明确传达。

### 2. 倒 U 型 dose-response 曲线描述
**✅ 已有**

- `experiments.tex:101-102` — "recovery follows an inverted-U across α ∈ {0.5, 1.0, 2.0, 3.0, 4.0}, peaking at α=2.0"，并给出 α=1.0 collapse 和 α=4.0 恢复到 62.77% 的完整两侧描述
- `introduction.tex:17,22` — Figure 1 caption 和正文均描述 "inverted-U"
- `abstract.tex:5` — "a dose-response analysis reveals an inverted-U in recovery accuracy, peaking at α=2.0"
- `appendix.tex:93-97` — 完整五点 α 值的逐点描述，包括 α=3.0 排除 plateau 假说

### 3. §4.4 dose-response 段引用
**⚠️ 部分缺失**

`experiments.tex:99-104`（§4.4 Dose-response and sparsity limits）当前引用：
- ✅ `Appendix~\ref{sec:appendix_alpha}` (line 102)
- ✅ `Table~\ref{tab:math500}` (line 103)
- ❌ **未引用 Figure~\ref{fig:dose_response}**（Figure 1，dose-response 曲线图）
- ❌ **未直接引用 Table~\ref{tab:alpha}**（仅通过 Appendix 间接关联）

`Table~\ref{tab:alpha}` 在 §4.3 (line 82) 被引用过，但 §4.4 本身——作为 dose-response 的核心段落——应该直接引用 Figure 1 和 Table 5。

**建议**：在 `experiments.tex:102` 中添加 `(Figure~\ref{fig:dose_response}; Table~\ref{tab:alpha})`，例如改为：
> "...peaking at α=2.0 (SFT 64.97%, GRPO 66.11%; Figure~\ref{fig:dose_response}, Table~\ref{tab:alpha})"

### 4. Appendix D（α ablation）被正文引用
**✅ 已有**

- `experiments.tex:102` — `Appendix~\ref{sec:appendix_alpha}` 直接引用
- `appendix.tex:89` — `\label{sec:appendix_alpha}` 定义（编译后为 Appendix D）

### 5. α=2.0 作为 practitioner guideline
**✅ 已有**

- `conclusion.tex:13-14` — `\paragraph{Practitioner guidelines.} Use RASP at α ≈ 2.0, which outperforms both pure importance (Standard) and pure diversity (CKA-only) on the dose-response curve (Figure~\ref{fig:dose_response}).`
- 同段 line 16 还给出配套建议：per-layer floors ≥40%、sparsity <25%、monitor early f₀

---

**总结**：5 项中 4 项完整，1 项部分缺失。§4.4 dose-response 段应直接引用 Figure 1 和 Table 5（tab_alpha），当前仅间接通过 Appendix 关联。

---
