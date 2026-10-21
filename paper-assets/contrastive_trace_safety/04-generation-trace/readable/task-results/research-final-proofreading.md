# research final proofreading

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_final_proofreading_20260520T155448_result.json`
- **Structured JSON:** [`875bece6a8cbb518fc07.json`](../../sessions/87/875bece6a8cbb518fc07.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here is the full audit report.

---

# 论文提交前审查报告

## 任务 1: 全文 Proofreading

### 1.1 引用格式 (\cite → \citet/\citep)

🔴 **21 处 plain `\cite{}` 应改为 `\citet{}` 或 `\citep{}`**

ACL 使用 natbib，要求 `\citet` (句中主语位置) 和 `\citep` (括号引用)。以下文件使用了 plain `\cite`：

**introduction.tex:**
- L3: `DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq}` — 作为主语 → `\citet`
- L3: `~\cite{harmthoughts,selfjailbreak}` — 句末 → `\citep`
- L5: `TrajGuard~\cite{trajguard}`, `SafeSwitch~\cite{safeswitch}`, `SafeRemind~\cite{saferemind}` — 作为主语 → `\citet`

**related_work.tex:**
- L4: `~\cite{wang2025lrmsafety}` → `\citep`
- L6: `~\cite{harmthoughts}`, `~\cite{selfjailbreak}` → `\citep`
- L6: `H-CoT~\cite{hcot2025}`, `Unfaithful reasoning~\cite{chen2025unfaithful,turpin2023language}` → `\citet`
- L6: `~\cite{yin2025refusal_cliff,...}` → `\citep`
- L8: `~\cite{baker2025monitoring}`, `~\cite{korbak2025cot_monitorability}` → `\citep`
- L8: `GuardReasoner~\cite{xiang2025guardreasoner}` → `\citet`
- L10: `SafeThink~\cite{safethink}`, `SafeRemind~\cite{saferemind}`, `Chain-of-Guardrails~\cite{mao2025selfjailbreak_reasoning}` → `\citet`
- L19: `BOCPD~\cite{adams2007bayesian}`, `CCS~\cite{burns2023discovering}`, `RepE~\cite{zou2023representation}` → `\citet`

**appendix.tex:**
- L313: `STILL~\cite{still}` → `\citet`
- L452: `\cite{hewitt2019control}` ("framework of") → `\citep`
- L460: `\cite{hewitt2019control}` ("recommended by") → `\citep`
- L733: `TrajGuard~\cite{trajguard}` → `\citet`
- L735: `~\cite{zou2023representation}` → `\citet`
- L739: `~\cite{burns2023discovering}` → `\citet`

### 1.2 术语一致性

🟡 **"Safety Commitment Point" 定义不一致**
- abstract.tex: "commitment point (CP)—the first reasoning step after which safety deliberation permanently ceases" (小写，用 "deliberation")
- introduction.tex L3: "**Safety Commitment Point** (CP)" (title case, bolded, "deliberation")
- method.tex L7: "**Safety Commitment Point** (CP) as the first reasoning step after which safety reasoning permanently ceases" (用 "reasoning" 而非 "deliberation")

abstract 未使用完整名称 "Safety Commitment Point"；method.tex 用了 "safety reasoning" 而非 abstract/intro 的 "safety deliberation"。

🟢 **"crossing rate" / "crossing-rate"**: 基本一致——用作复合形容词时带连字符 (crossing-rate composite)，独立使用时不带。少数地方不完全一致但可接受。

🟢 **"hidden state" / "hidden-state"**: 用法基本正确。

🟡 **"bal_acc" 在 figure caption 中**: `fig_layer_heatmap.pdf` 的 caption (experiments.tex L35) 使用了 `bal\_acc × crossing\_rate` 代码风格写法，正文其他地方用 "balanced accuracy × crossing rate"。Caption 中应统一用可读形式。

### 1.3 Label 命名错误

🔴 **`\label{tab:ba_layer_comparison}` 实际上是一个 `\section{}`** (appendix.tex L1094)

这个 section 的 label 使用了 `tab:` 前缀，但它是一个 section 而非 table。`\cref` 在生成引用时依赖 counter 类型，虽然输出可能仍然正确，但 prefix 命名极具误导性。应改为 `app:ba_layer_comparison`。

### 1.4 数字一致性

✅ 经核对，以下关键数字与表格一致：
- Abstract "+15.4 to +21.9pp" ↔ tab:hs_vs_text (R1-32B +15.4, OT-7B +21.9) ✓
- Abstract "κ=0.606" ↔ tab:iaa ✓
- Abstract "384-dimensional... 4/4 → 1024d BGE-large: 1/4" ↔ tab:encoder_robustness ✓
- Introduction "+20.1 to +21.9pp" for 7-8B ↔ tab:hs_vs_text ✓
- Experiments "+14.2pp" for R1-32B position margin ↔ tab:32b_divergence ✓

---

## 任务 2: Appendix 完整性

### 2.1 Appendix TOC 缺失条目

🔴 以下 `\section` 级别的 appendix 内容不在 TOC (appendix.tex lines 3-26) 中：

| 缺失 Section | Label | 描述 |
|---|---|---|
| CP Annotation Perturbation | `app:cp_perturbation` | 主文有引用 (limitations.tex) |
| Random Projection Baseline | `app:random_projection` | 主文有引用 (experiments.tex) |
| LLM-Based Text Encoder | `app:e5_mistral` | 主文有引用 (experiments.tex) |
| Hyperparameter Robustness | `app:hyperparameter_robustness` | 主文有引用 (experiments.tex, limitations.tex) |

这 4 个 section 从主文引用但不在 TOC 中，读者无法通过 TOC 找到它们。

### 2.2 孤立 Appendix 内容（未被主文引用）

🟡 以下 appendix section/subsection 从未被主文任何 section 引用：

| Section | Label | 说明 |
|---|---|---|
| M002 Bug Disclosure | `app:bug` | 仅在 appendix 内部引用 |
| Adaptive Two-Stage Detection | `app:two_stage` | 仅在 appendix 内部引用 |
| Inter-Annotator Agreement | `app:iaa` | 仅在 appendix 内部引用 |
| Window Size Ablation | `app:window_ablation` | 注：fig:window_ablation 被主文引用，但 section 本身未被引用 |

`app:bug` 和 `app:iaa` 作为透明度声明/补充分析，不被主文引用可以理解。`app:two_stage` 作为 negative result 补充，也是 borderline 可接受。

### 2.3 表格/图 完整性

✅ Appendix 中所有 table 和 figure 均有 `\caption` 和 `\label`。

---

## 任务 3: 交叉引用完整性

### 3.1 main.log 编译警告

✅ **无 undefined reference 或 citation**
✅ **无 multiply defined label**

### 3.2 Overfull hbox（表格溢出）

🔴 **8 个严重 Overfull hbox (>20pt)，均在 appendix 表格中**：

| 溢出量 | 位置 (appendix.tex lines) | 内容 |
|---|---|---|
| **99.5pt** | L837-847 | tab:e5_mistral |
| **93.5pt** | L765-775 | tab:encoder_robustness |
| **90.1pt** | L81-91 | tab:r18b_full_layer |
| **88.6pt** | L944-952 | tab:nested_cv |
| **74.6pt** | L917-925 | tab:fold_ba_layers |
| **61.3pt** | L860-871 | tab:position_residual |
| **42.5pt** | L615-628 | tab:k_ablation |
| **39.8pt** | L650-661 | tab:threshold_r132b |

这些表格大幅超出文本边界。需要用 `\resizebox{\columnwidth}{!}{}` 或 `\small`/`\scriptsize` 缩放。

🟡 另有 ~8 个中等 Overfull hbox (5-37pt) 也在 appendix 表格中。

### 3.3 Float specifier 警告

🟡 **9 处 `h` float specifier 被改为 `ht`** — appendix 中多个 table 使用了 `[h]`，LaTeX 自动改为 `[ht]`。建议统一改为 `[ht]` 或 `[htbp]`。

### 3.4 Hyperref 警告

🟢 2 处 "Token not allowed in a PDF string" — 来自 section title 中的数学符号，不影响正文。

---

## 总结

| 严重程度 | 数量 | 类别 |
|---|---|---|
| 🔴 必须修 | **26** | 21 citation format + 4 TOC 缺失 + 1 label 命名错误 |
| 🟡 建议修 | **15** | 术语不一致 2 + 孤立 appendix 4 + Overfull hbox 8 + float specifier 1 |
| 🟢 可选 | **3** | crossing-rate 连字符 + hyperref warning 2 |

**最高优先级**：21 处 `\cite` → `\citet`/`\citep` 是审稿人最容易注意到的格式问题。8 个严重 Overfull 表格会导致 appendix 视觉上不专业。4 个 appendix section 缺失 TOC 条目会让引用者找不到对应内容。

---
