# paper reviewer framing fixes

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 18
- **Original source:** `logs/chats/worker_paper_reviewer_framing_fixes_20260516T073046.jsonl`
- **Structured JSON:** [`58c093aa06cf39da5474.json`](../../sessions/58/58c093aa06cf39da5474.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

37 recorded events

### Tool call

_source line 1 · 2026-05-16T07:31:58.385011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T07:31:58.385408+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We evaluate nine models spanning seven architecture families and diverse attention configurations:
9	\textbf{Qwen2.5-7B} (GQA 7:1, 28 layers $\times$ 4 KV heads = 112),
10	\textbf{Qwen2.5-14B} (GQA 5:1, 48 $\times$ 8 = 384),
11	\textbf{Yi-1.5-9B} (GQA 8:1, 48 $\times$ 4 = 192),
12	\textbf{Llama-3.1-8B} (GQA 4:1, 32 $\times$ 8 = 256),
13	\textbf{CodeLlama-7B}\footnote{CodeLlama multi-bit profiles synthesized from 2-bit-only profiling; classification robust as constrained allocation is dominated by 4-bit heads.} (MHA 1:1, 32 $\times$ 32 = 1024),
14	\textbf{Mistral-7B-v0.3} (GQA 4:1, 32 $\times$ 8 = 256, sliding window attention),
15	\textbf{Gemma-2-9B} (GQA 2:1, 42 $\times$ 8 = 336, \texttt{head\_dim}=256, attention logit softcapping),
16	\textbf{Phi-3-medium-14B} (GQA 4:1, 40 $\times$ 10 = 400),
17	and \textbf{Pythia-1.4B} (MHA 1:1, 24 $\times$ 16 = 384).
18	All nine models undergo full constrained evaluation.
19	This selection spans GQA ratios from 1:1 (MHA) to 8:1 and covers standard, sliding-window, softcapped, and multi-head attention.
20	
21	\paragraph{Evaluation.}
22	We report perplexity (PPL, $\downarrow$) on the WikiText-2 test split (298{,}938 tokens) under bf16 inference with stride 512.
23	For downstream evaluation, we use ARC-Challenge, HellaSwag, PIQA, and WinoGrande under 0-shot prompting.
24	
25	\paragraph{Profiling.}
26	Per-head sensitivity is measured by independently quantizing each head to each candidate bit-width in $\{2, 4, 8, 16\}$ and recording the PPL increase over the bf16 baseline.
27	All results use high-resolution profiling (64 sequences $\times$ 2048 tokens from WikiText-2 train); Appendix~\ref{sec:profiling_resolution} compares against standard-resolution profiling (16 seq $\times$ 512 tok).
28	
29	\paragraph{Compression and constraint.}
30	The default target is 4$\times$ compression (average 4 bits, budge
…[truncated 11074 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T07:31:58.385606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T07:31:58.385831+00:00_

1	\section{Analysis}
2	\label{sec:analysis}
3	
4	\subsection{Heterogeneity Characterization}
5	\label{sec:heterogeneity}
6	
7	The benefit of non-uniform allocation depends on how unevenly head sensitivities are distributed.
8	We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
9	High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
10	
11	Table~\ref{tab:heterogeneity} summarizes the results across nine models at $4\times$ compression.
12	The central finding is that MCKP benefit requires \emph{spread heterogeneity}---multiple heads with cross-bitwidth sensitivity gradients---rather than sensitivity concentrated in a single outlier at one bitwidth.
13	
14	Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
15	Constrained MCKP reduces degradation from $+$5.64 PPL (uniform) to $+$1.10 PPL, a 29.4\% improvement over uniform 4-bit. %exp_id=qwen_constrained_mckp
16	
17	Yi-1.5-9B is a critical counterexample: despite high concentration ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
18	Yi-1.5's sensitivity is dominated by a single extreme outlier: Layer-4 Head-3 ($d_h(2){=}13.12$, second-ranked head: $0.55$, a $24\times$ gap; $t_1/t_5{=}0.90$). %exp_id=yi15_hires_profiling
19	Critically, L4H3's 4-bit and 8-bit deltas are ${\approx}\,0$, so upgrading it from 2-bit to 4-bit removes the distortion, but budget freed by downgrading other heads has nowhere useful to go---a ``spike'' pattern with sensitivity at only one bitwidth.
20	In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6
…[truncated 7466 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T07:31:58.386018+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/appendix*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/appendix*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T07:31:58.386148+00:00_

docs/paper/appendix.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T07:31:58.386265+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T07:31:58.386406+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	Per-head mixed-precision KV cache quantization over hardware-aligned bit-widths \{2, 4, 8, 16\} requires a cardinality constraint on 2-bit assignments to prevent non-additive distortion compounding.
4	On Qwen2.5-7B, limiting 2-bit heads to $k{\leq}8$ reduces PPL from 15.45 (uniform 4-bit) to 10.91 ($-$29.4\%) at $4\times$ compression, while making solver choice irrelevant: constrained greedy and MCKP produce identical allocations across all tested architectures.
5	Whether non-uniform allocation helps depends on the \emph{shape} of head sensitivity heterogeneity---spread patterns (Qwen-7B, $t_1/t_5{=}0.57$) yield large gains, while spike (Yi-1.5, CodeLlama, Llama) and flat (Mistral, Gemma-2, Phi-3-medium, Qwen-14B, Pythia) patterns show no benefit.
6	An empirical characterization based on concentration and $t_1/t_5$ ratio correctly predicts allocation benefit for all nine models (9/9), including a within-family scale contrast where Qwen-14B's spread dilutes into flat.
7	Extending to 70B+ models, production inference engines, and per-side K/V cardinality constraints (Appendix~\ref{sec:kv_separation}) are natural next steps.
8	
9	\section*{Limitations}
10	
11	\paragraph{$N{=}1$ spread.}
12	The spread pattern is observed in only one model (Qwen2.5-7B); the decision rule thresholds (concentration $\geq 0.50$, $t_1/t_5 \leq 0.70$) are calibrated on nine models with a single positive example and should be treated as a preliminary observation rather than a validated classifier.
13	
14	\paragraph{Model scale.}
15	The largest model evaluated is 14B parameters (up to 400 heads). The Qwen-7B/14B contrast suggests that concentration dilutes with increasing head count, which may make spread less likely at larger scales; this trend is a hypothesis, not a confirmed finding.
16	
17	\paragraph{Runtime.}
18	All latency measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} dispatch and do not represent optimized 
…[truncated 1273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T07:31:58.386546+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": "170",
  "limit": "50"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "offset": "170",
    "limit": "50"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T07:31:58.386724+00:00_

170	Table~\ref{tab:runtime} reports end-to-end latency for three KV cache configurations.
171	Uniform 4-bit quantization adds 25.7\% decode overhead relative to the bf16 baseline (42.46 vs.\ 33.78~ms/tok), reflecting per-head quantize/dequantize calls at every attention step.
172	Constrained MCKP adds a further 8.5\% over uniform (46.09 vs.\ 42.46~ms/tok), because mixed-precision allocation dispatches different dequantization kernels for 2-bit, 4-bit, and 8-bit heads within the same layer.
173	The MCKP solver itself runs in ${\sim}5$~ms and is invoked once at initialization, contributing negligibly to end-to-end latency.
174	Both quantized conditions achieve the same $4\times$ KV cache compression (5.25~MB vs.\ 21~MB at bf16), so the latency difference between uniform and MCKP reflects only the mixed-precision dispatch overhead, not a memory trade-off.
175	
176	\paragraph{Caveat.}
177	These measurements use PyTorch-level per-head \texttt{quantize}/\texttt{dequantize} calls and do \emph{not} represent optimized CUDA kernel performance.
178	Production inference engines such as vLLM and TensorRT-LLM employ fused attention kernels that batch dequantization with the matrix multiply, amortizing the per-head dispatch cost that dominates the gap between uniform and MCKP in our simulation.
179	The 8.5\% overhead reported here should therefore be treated as an upper bound on the mixed-precision penalty; real-world deployment with fused kernels would likely narrow or eliminate this gap.
180	As noted in the Limitations section, we report no real-kernel latency benchmarks: the numbers above quantify simulation overhead, not production inference speedup.
181	
182	\section{Long-Context Generalization}
183	\label{sec:long_context}
184	
185	\begin{table}[ht]
186	\centering
187	\small
188	\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
189	\label{tab:long_context}
190	\begin{tabular}{l
…[truncated 1235 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T07:31:58.386901+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "8/8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "8/8",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T07:31:58.387024+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T07:31:58.387140+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Yi-1.5 excluded",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Yi-1.5 excluded",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T07:31:58.387260+00:00_

docs/paper/appendix.tex:188:\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}
docs/paper/main.aux:1390:\@writefile{lot}{\contentsline {table}{\numberline {8}{\ignorespaces PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096).}}{14}{table.caption.40}\protected@file@percent }
docs/paper/main.aux:1391:\newlabel{tab:long_context}{{8}{14}{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096)}{table.caption.40}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T07:31:58.387418+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit, consistent with spike classification.",
  "new_string": "Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "old_string": "Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit, consistent with spike classification.",
    "new_string": "Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\\times$ bf16, MCKP $1.06\\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification."
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T07:31:58.387585+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T07:31:58.387733+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "old_string": "The uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.",
  "new_string": "The uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.\nWe note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "old_string": "The uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.",
    "new_string": "The uniform-to-constrained PPL ratio on Qwen widens from $1.4\\times$ at 2K to $9.1\\times$ at 8K, while Llama, Mistral, and Yi remain flat---long-context stress amplifies the spread-specific benefit of per-head allocation.\nWe note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models."
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-16T07:31:58.387903+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T07:31:58.388033+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "old_string": "\\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}\n\\label{tab:long_context}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\bottomrule\n\\end{tabular}",
  "new_string": "\\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times$ 2048 tok).}\n\\label{tab:long_context}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\midrule\n & BF16 baseline & 7.04 & 4.83 \\\\\nMistral-7B-v0.3 & MCKP ($k{=}2$) & 7.13 & 4.92 \\\\\n & Uniform 4-bit & 7.13 & 4.92 \\\\\n\\midrule\n & BF16 baseline & 7.02 & 5.26 \\\\\nYi-1.5-9B & MCKP ($k{=}2$) & 7.22 & 5.56 \\\\\n & Uniform 4-bit & 7.22 & 5.50 \\\\\n\\bottomrule\n\\end{tabular}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "old_string": "\\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times$ 2048 tok). Yi-1.5 excluded (max position 4096).}\n\\label{tab:long_context}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\bottomrule\n\\end{tabular}",
    "new_string": "\\caption{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\\times$ 2048 tok).}\n\\label{tab:long_context}\n\\begin{tabular}{llcc}\n\\toprule\nModel & Method & 2K PPL & 8K PPL \\\\\n\\midrule\n & BF16 baseline & 9.81 & 6.97 \\\\\nQwen2.5-7B & MCKP ($k{=}8$) & 10.89 & 8.59 \\\\\n & Uniform 4-bit & 15.45 & 77.75 \\\\\n\\midrule\n & BF16 baseline & 8.09 & 5.60 \\\\\nLlama-3.1-8B & MCKP ($k{=}2$) & 8.50 & 6.05 \\\\\n & Uniform 4-bit & 8.47 & 6.04 \\\\\n\\midrule\n & BF16 baseline & 7.04 & 4.83 \\\\\nMistral-7B-v0.3 & MCKP ($k{=}2$) & 7.13 & 4.92 \\\\\n & Uniform 4-bit & 7.13 & 4.92 \\\\\n\\midrule\n & BF16 baseline & 7.02 & 5.26 \\\\\nYi-1.5-9B & MCKP ($k{=}2$) & 7.22 & 5.56 \\\\\n & Uniform 4-bit & 7.22 & 5.50 \\\\\n\\bottomrule\n\\end{tabular}"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T07:31:58.388226+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T07:31:58.388360+00:00_

called Edit

<details open><summary>🔧 Tool call — Edit</summary>

```json
{
  "replace_all": "False",
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "old_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp",
  "new_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL).\nAlthough $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "tool_args": {
    "replace_all": "False",
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "old_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL). %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp",
    "new_string": "Phi-3-medium-14B (GQA 4:1, 400 heads) has the lowest concentration in our test set ($0.17$) with $t_1/t_5{=}0.23$; the joint rule classifies it as flat, confirmed by evaluation (constrained $+$0.18 vs.\\ uniform $+$0.16 PPL).\nAlthough $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-16T07:31:58.388522+00:00_

The file /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex has been updated successfully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Edit",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T07:31:58.388674+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\+0\\.06",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\+0\\.06",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T07:31:58.388803+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T07:31:58.388918+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "fewest KV heads",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "fewest KV heads",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-16T07:31:58.389032+00:00_

146:We note that Qwen-7B also has the fewest KV heads (112) in our test set; whether the long-context amplification is driven by the spread pattern, the low head count, or their interaction remains an open question requiring evaluation on additional spread-pattern models.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T07:31:58.389148+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Yi-1.5 excluded",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Yi-1.5 excluded",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T07:31:58.389264+00:00_

docs/paper/main.aux:1390:\@writefile{lot}{\contentsline {table}{\numberline {8}{\ignorespaces PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096).}}{14}{table.caption.40}\protected@file@percent }
docs/paper/main.aux:1391:\newlabel{tab:long_context}{{8}{14}{PPL at 2K and 8K context length on WikiText-2. Profiles calibrated at 2K (64 seq $\times $ 2048 tok). Yi-1.5 excluded (max position 4096)}{table.caption.40}{}}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T07:31:58.389385+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "concentration of 0.17",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "concentration of 0.17",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-16T07:31:58.389500+00:00_

30:Although $t_1/t_5$ is low (indicating no dominant outlier), the concentration of 0.17 places the cumulative top-5\% delta below the level required for meaningful reallocation---spread structure without sufficient absolute magnitude does not create optimization opportunities. %exp_id=phi3_medium_hires_profiling_v2 %exp_id=phi3_medium_constrained_mckp

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T07:31:58.389613+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Mistral-7B-v0.3.*4\\.83",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Mistral-7B-v0.3.*4\\.83",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-16T07:31:58.389748+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T07:31:58.389860+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "8/8",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "8/8",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-16T07:31:58.389967+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T07:31:58.390098+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.06.*PPL",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.06.*PPL",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T07:31:58.390210+00:00_

144:Yi-1.5-9B (spike, $c{=}0.71$, $t_1/t_5{=}0.90$): uniform $1.05\times$ bf16, MCKP $1.06\times$---no benefit or slight degradation ($+$0.06~PPL), consistent with spike classification.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T07:31:58.390362+00:00_

All verifications pass:

1. **Yi 8K description** (experiments.tex:144) — now includes "+0.06 PPL" and "no benefit or slight degradation"
2. **KV head count caveat** (experiments.tex:146) — added after the long-context discussion
3. **Appendix long-context table** (appendix.tex) — removed "Yi-1.5 excluded" from caption, added Mistral-7B-v0.3 and Yi-1.5-9B rows
4. **Phi-3 concentration explanation** (analysis.tex:30) — added the sentence about concentration 0.17 and insufficient absolute magnitude
5. **"Yi-1.5 excluded"** — only remains in main.aux (stale LaTeX build cache, will be overwritten on next compile)
6. **"8/8"** — no matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_reviewer_framing_fixes_20260516T073046"
}
```

</details>

---
