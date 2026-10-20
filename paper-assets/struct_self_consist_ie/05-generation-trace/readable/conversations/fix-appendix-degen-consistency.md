# fix appendix degen consistency

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_fix_appendix_degen_consistency_20260519T143858.jsonl`
- **Structured JSON:** [`092f66beaa12af51df14.json`](../../sessions/09/092f66beaa12af51df14.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-19T14:39:46.806352+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "355",
  "limit": "20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "355",
    "limit": "20"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-19T14:39:46.806676+00:00_

355	\small
356	\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
357	\label{tab:degeneracy}
358	\begin{tabular}{lccc}
359	\toprule
360	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}16$)} \\
361	\midrule
362	Constant F1 & 17.8\% & 10.4\% & 61.7\% \\
363	Constant utility & 13\% & 7.0\% & 49\% \\
364	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
365	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\
366	\bottomrule
367	\end{tabular}
368	\end{table}
369	
370	\paragraph{TOST equivalence testing.}\label{app:tost}
371	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
372	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\delta$.
373	The $\delta$ values are contextualized against oracle headroom (12--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
374	These proportions use the same test data that defines the headroom, introducing circularity: $\delta$ is anchored to the very quantity it contextualizes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-19T14:39:46.806865+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "680",
  "limit": "30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "680",
    "limit": "30"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-19T14:39:46.807025+00:00_

680	\end{tabular}
681	\end{table}
682	
683	\paragraph{Within-instance LP-quality alignment.}\label{app:within_instance_rho}
684	
685	Table~\ref{tab:within_rho} reports median within-instance $\rho(\text{LP}, \text{F1})$ across datasets, computed over non-degenerate instances (those with ${\geq}2$ distinct F1 values across $N{=}8$ samples).
686	Few-NERD exhibits substantially stronger alignment ($\rho{=}0.667$) than SciERC ($\rho{=}0.262$), directly explaining why LP selection succeeds only on Few-NERD.
687	CoNLL alignment is moderate ($\rho{\approx}0.51$), but the valid-instance fraction is low (41\% for Qwen, 11\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.
688	LP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\S\ref{sec:discussion}).
689	
690	\begin{table}[h]
691	\centering
692	\small
693	\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\text{valid}}$: ${\geq}2$ distinct F1 values).}
694	\label{tab:within_rho}
695	\resizebox{\columnwidth}{!}{%
696	\begin{tabular}{@{}llccc@{}}
697	\toprule
698	Dataset & Model & Med.\ $\rho$ & $n_{\text{valid}}$ / $n_{\text{total}}$ & Valid\% \\
699	\midrule
700	SciERC & Qwen3-8B & 0.262 & 435 / 529 & 82\% \\
701	Few-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\% \\
702	CoNLL & Qwen3-8B & 0.506 & 1{,}124 / 2{,}756 & 41\% \\
703	CoNLL & LLaMA-3.1-8B & 0.512 & 298 / 2{,}756 & 11\% \\
704	\bottomrule
705	\end{tabular}}
706	\end{table}
707	
708	\section{Consistency-Stratified Selection Analysis}\label{app:vc_quartile}
709	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-19T14:39:46.807224+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "41",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Grep",
  "tool_args": {
    "pattern": "41",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-19T14:39:46.807391+00:00_

37:\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
53:\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
81:Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
137:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
148:For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
200:EM ranks first across all four tested conditional configurations: SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$). This holds despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
221:LP & $-$.410 & .219 & .350 & ${<}$1e-10 \\
342:[Omitted long matching line]
364:Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
561:The estimated LP shift is 0.001 nats per token (2.68\% of the median within-instance LP range of 0.041 nats).
576:The median within-instance LP range is only 0.041 nats; we use $\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.
579:This compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied 
…[truncated 1962 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-19T14:39:46.807579+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\",
  "new_string": "& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}8$)} \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}16$)} \\\\",
    "new_string": "& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}8$)} \\\\"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-19T14:39:46.808064+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-19T14:39:46.808245+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (41\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.",
  "new_string": "CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (38\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (41\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.",
    "new_string": "CoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (38\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-19T14:39:46.808672+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-19T14:39:46.808817+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values).}",
  "new_string": "\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values).}",
    "new_string": "\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-19T14:39:46.809268+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-19T14:39:46.809443+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "358",
  "limit": "8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "358",
    "limit": "8"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T14:39:46.809579+00:00_

358	\begin{tabular}{lccc}
359	\toprule
360	& \shortstack{SciERC 8B\\($N{=}8$)} & \shortstack{SciERC 4B\\($N{=}8$)} & \shortstack{CoNLL 8B\\($N{=}8$)} \\
361	\midrule
362	Constant F1 & 17.8\% & 10.4\% & 61.7\% \\
363	Constant utility & 13\% & 7.0\% & 49\% \\
364	Oracle gap closed (non-deg.) & 23\% & 25.2\% & 41\% \\
365	Within-inst.\ SJ $\rho$ (median) & 0.524 & 0.550 & 0.994 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-19T14:39:46.809702+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "685",
  "limit": "12"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "685",
    "limit": "12"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T14:39:46.809831+00:00_

685	Table~\ref{tab:within_rho} reports median within-instance $\rho(\text{LP}, \text{F1})$ across datasets, computed over non-degenerate instances (those with ${\geq}2$ distinct F1 values across $N{=}8$ samples).
686	Few-NERD exhibits substantially stronger alignment ($\rho{=}0.667$) than SciERC ($\rho{=}0.262$), directly explaining why LP selection succeeds only on Few-NERD.
687	CoNLL alignment is moderate ($\rho{\approx}0.51$), but the valid-instance fraction is low (38\% for Qwen, 11\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.
688	LP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\S\ref{sec:discussion}).
689	
690	\begin{table}[h]
691	\centering
692	\small
693	\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\text{valid}}$: ${\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}
694	\label{tab:within_rho}
695	\resizebox{\columnwidth}{!}{%
696	\begin{tabular}{@{}llccc@{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-19T14:39:46.810003+00:00_

Diff 摘要：

| 行 | 修改 | 原值 | 新值 |
|---|---|---|---|
| L360 | 表头 CoNLL 8B 列 N 值 | `$N{=}16$` | `$N{=}8$` |
| L687 | 正文 Qwen valid fraction | `41\%` | `38\%` (匹配 100% − 61.7% 3-seed 均值) |
| L693 | within_rho 表 caption | — | 末尾追加 "Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates." |

一致性确认：
- L360 三列表头现在全部为 N=8
- L687 的 38% 与 L362 的 degeneracy 61.7% 互补（100−61.7≈38）
- L702-703 表格数据不变（仍为 seed 42 实际计算值 41%/11%），caption 已注明数据来源
- LLaMA 11% 无需改动（LLaMA 只有单种子推理数据，与 3-seed 均值无矛盾）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_fix_appendix_degen_consistency_20260519T143858"
}
```

</details>

---
