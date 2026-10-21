# knowledge appendix error entropy addition

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/chats/worker_knowledge_appendix-error-entropy-addition_20260520T030113.jsonl`
- **Structured JSON:** [`81c843e7d64a670d46d4.json`](../../sessions/81/81c843e7d64a670d46d4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

13 recorded events

### Tool call

_source line 1 · 2026-05-20T03:01:55.413310+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-20T03:01:55.413636+00:00_

File content (43603 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-20T03:01:55.413809+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fs_vs_zs_error_correlation.json 2>/dev/null | python3 -m json.tool 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fs_vs_zs_error_correlation.json 2>/dev/null",
  "description": "Read error correlation JSON data"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fs_vs_zs_error_correlation.json 2>/dev/null | python3 -m json.tool 2>/dev/null || cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/fs_vs_zs_error_correlation.json 2>/dev/null",
    "description": "Read error correlation JSON data"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-20T03:01:55.413984+00:00_

{
    "scierc": {
        "fs": {
            "mean_pairwise_error_jaccard": 0.4537,
            "std_pairwise_error_jaccard": 0.3007,
            "median_pairwise_error_jaccard": 0.489,
            "mean_entity_entropy": 0.4828,
            "std_entity_entropy": 0.261
        },
        "zs": {
            "mean_pairwise_error_jaccard": 0.4524,
            "std_pairwise_error_jaccard": 0.2959,
            "median_pairwise_error_jaccard": 0.5089,
            "mean_entity_entropy": 0.4848,
            "std_entity_entropy": 0.2573
        },
        "jaccard_test": {
            "test_name": "wilcoxon_signed_rank",
            "statistic": 51318.5,
            "p_value": 0.8442039112000504,
            "effect_size_r": 0.0084,
            "direction": "fs>zs"
        },
        "entropy_test": {
            "test_name": "wilcoxon_signed_rank",
            "statistic": 57215.0,
            "p_value": 0.8069014200592761,
            "effect_size_r": 0.0104,
            "direction": "zs>fs"
        },
        "n_instances": 551,
        "n_skipped_no_errors": 67,
        "interpretation": "No significant difference in error overlap between FS and ZS"
    },
    "conll": {
        "fs": {
            "mean_pairwise_error_jaccard": 0.1026,
            "std_pairwise_error_jaccard": 0.2329,
            "median_pairwise_error_jaccard": 0.0,
            "mean_entity_entropy": 0.2093,
            "std_entity_entropy": 0.2857
        },
        "zs": {
            "mean_pairwise_error_jaccard": 0.104,
            "std_pairwise_error_jaccard": 0.2384,
            "median_pairwise_error_jaccard": 0.0,
            "mean_entity_entropy": 0.1839,
            "std_entity_entropy": 0.2812
        },
        "jaccard_test": {
            "test_name": "wilcoxon_signed_rank",
            "statistic": 229924.0,
            "p_value": 0.6377686633294677,
            "effect_size_r": 0.008,
            "direction": "zs>fs"
        },
        "entropy_test": {
            "test_name": "wilcox
…[truncated 341 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-20T03:01:55.414198+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "error.correlation|fs_error|fs.vs.zs|few-shot.*zero-shot.*compar|ZS.*FS|FS.*ZS",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "output_mode": "content",
  "-i": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Grep",
  "tool_args": {
    "pattern": "error.correlation|fs_error|fs.vs.zs|few-shot.*zero-shot.*compar|ZS.*FS|FS.*ZS",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "output_mode": "content",
    "-i": "True"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-20T03:01:55.414377+00:00_

1621:\subsection{Few-Shot Error Correlation Analysis}\label{app:fs_error}
1624:Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).
1649:\subsection{Zero-Shot vs.\ Few-Shot Comparison}\label{app:zs_vs_fs}
1651:Table~\ref{tab:72b_zs_vs_fs} presents the full zero-shot (ZS) vs.\ few-shot (FS) comparison on Qwen2.5-72B-Instruct-AWQ.
1652:LP-weighted construction yields a significant gain only on SciERC under ZS ($+$1.53\,pp, $p{=}.008$); all five FS configurations show non-significant deltas ($|{\Delta}| \leq 0.08$\,pp).
1653:Few-shot demonstrations raise the greedy baseline (e.g., SciERC: .399$\to$.461) but do not translate into construction improvements, suggesting that the dual-gating mechanism---where both signal quality and diversity are necessary---holds within the FT+ZS regime while FS introduces an independent failure mode whose origin remains open (\S\ref{app:fs_error}).
1658:\label{tab:72b_zs_vs_fs}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-20T03:01:55.414516+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1618",
  "limit": "40"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1618",
    "limit": "40"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T03:01:55.414668+00:00_

1618	}
1619	\end{table}
1620	
1621	\subsection{Few-Shot Error Correlation Analysis}\label{app:fs_error}
1622	
1623	We investigated whether few-shot demonstrations induce correlated entity-level errors that explain construction failure.
1624	Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).
1625	The mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error diversity may be preserved while the \emph{nature} of errors shifts in ways that defeat LP-weighted voting.
1626	
1627	\subsection{Construction Weighting Variants}\label{app:weighting_variants}
1628	
1629	Table~\ref{tab:weighting_variants} compares LP-weighted, VC-weighted, and SJ-weighted entity construction on LLaMA-3.1-8B (3-seed mean, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$).
1630	All three weighting schemes beat greedy on SciERC, where degeneracy is low; LP and VC also improve Few-NERD, though gains are smaller than the Qwen results in Table~\ref{tab:entity_construction}.
1631	The optimal weighting scheme is model-dependent (VC leads on LLaMA SciERC; LP leads on Qwen), but the core finding is robust: entity-level voting improves F1 in low-degeneracy regimes regardless of the specific weighting function.
1632	SJ-weighted construction degrades on Few-NERD ($-0.20$\,pp), consistent with SJ over-weighting high-consensus samples, which correlates with the degeneracy direction rather than opposing it.
1633	
1634	\begin{table}[h]
1635	\centering
1636	\small
1637	\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$, 3-seed mean). $\Delta$: F1 difference vs.\ greedy in pp. Main-text construction results (Table~\ref{tab:entity_construction}) use Qwen3-8B.}
1638	\label{tab:weighting_variants}
1639	\begin{
…[truncated 1231 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T03:01:55.414844+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).\nThe mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error diversity may be preserved while the \\emph{nature} of errors shifts in ways that defeat LP-weighted voting.",
  "new_string": "Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).\nWe additionally measure entity-level prediction entropy across $N{=}8$ samples per instance.\nOn SciERC, FS and ZS entropies are indistinguishable ($0.483$ vs.\\ $0.485$, $p{=}0.81$).\nOn CoNLL, however, entity prediction entropy is significantly \\emph{higher} under FS ($0.209$ vs.\\ $0.184$, $p{<}10^{-9}$, $r{=}0.106$, small effect; Wilcoxon signed-rank test), contrary to the hypothesis that demonstrations concentrate predictions---they instead \\emph{increase} output diversity on this dataset.\nThe mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error overlap is preserved while prediction entropy may even rise, suggesting that the \\emph{nature} rather than the \\emph{diversity} of errors shifts in ways that defeat LP-weighted voting."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "old_string": "Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).\nThe mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error diversity may be preserved while the \\emph{nature} of errors shifts in ways that defeat LP-weighted voting.",
    "new_string": "Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).\nWe additionally measure entity-level prediction entropy across $N{=}8$ samples per instance.\nOn SciERC, FS and ZS entropies are indistinguishable ($0.483$ vs.\\ $0.485$, $p{=}0.81$).\nOn CoNLL, however, entity prediction entropy is significantly \\emph{higher} under FS ($0.209$ vs.\\ $0.184$, $p{<}10^{-9}$, $r{=}0.106$, small effect; Wilcoxon signed-rank test), contrary to the hypothesis that demonstrations concentrate predictions---they instead \\emph{increase} output diversity on this dataset.\nThe mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error overlap is preserved while prediction entropy may even rise, suggesting that the \\emph{nature} rather than the \\emph{diversity} of errors shifts in ways that defeat LP-weighted voting."
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T03:01:55.415435+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T03:01:55.415631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": "1621",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "offset": "1621",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-20T03:01:55.415786+00:00_

1621	\subsection{Few-Shot Error Correlation Analysis}\label{app:fs_error}
1622	
1623	We investigated whether few-shot demonstrations induce correlated entity-level errors that explain construction failure.
1624	Pairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).
1625	We additionally measure entity-level prediction entropy across $N{=}8$ samples per instance.
1626	On SciERC, FS and ZS entropies are indistinguishable ($0.483$ vs.\ $0.485$, $p{=}0.81$).
1627	On CoNLL, however, entity prediction entropy is significantly \emph{higher} under FS ($0.209$ vs.\ $0.184$, $p{<}10^{-9}$, $r{=}0.106$, small effect; Wilcoxon signed-rank test), contrary to the hypothesis that demonstrations concentrate predictions---they instead \emph{increase} output diversity on this dataset.
1628	The mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error overlap is preserved while prediction entropy may even rise, suggesting that the \emph{nature} rather than the \emph{diversity} of errors shifts in ways that defeat LP-weighted voting.
1629	
1630	\subsection{Construction Weighting Variants}\label{app:weighting_variants}
1631	
1632	Table~\ref{tab:weighting_variants} compares LP-weighted, VC-weighted, and SJ-weighted entity construction on LLaMA-3.1-8B (3-seed mean, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$).
1633	All three weighting schemes beat greedy on SciERC, where degeneracy is low; LP and VC also improve Few-NERD, though gains are smaller than the Qwen results in Table~\ref{tab:entity_construction}.
1634	The optimal weighting scheme is model-dependent (VC leads on LLaMA SciERC; LP leads on Qwen), but the core finding is robust: entity-level voting improves F1 in low-degeneracy regimes regardless of the specific 
…[truncated 215 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-20T03:01:55.415977+00:00_

**插入位置**：`\subsection{Few-Shot Error Correlation Analysis}`（`\label{app:fs_error}`），原 Jaccard 段落之后、closing 句之前（第 1625-1628 行）。

**插入内容**（3 句）：
- SciERC entropy 无显著差异（0.483 vs 0.485, p=0.81）
- CoNLL entropy 在 FS 下显著更高（0.209 vs 0.184, p<10⁻⁹, r=0.106 small effect, Wilcoxon signed-rank）
- 更新了 closing 句：error overlap preserved + entropy may rise → nature rather than diversity of errors

所有数值与 `fs_vs_zs_error_correlation.json` 一致。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_knowledge_appendix-error-entropy-addition_20260520T030113"
}
```

</details>

---
