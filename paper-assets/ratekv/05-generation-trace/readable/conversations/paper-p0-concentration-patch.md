# paper p0 concentration patch

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/chats/worker_paper_p0-concentration-patch_20260514T221709.jsonl`
- **Structured JSON:** [`3be1844a789009db91f1.json`](../../sessions/3b/3be1844a789009db91f1.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

44 recorded events

### Assistant

_source line 1 · 2026-05-14T22:17:19.057401+00:00_

You've hit your limit · resets May 16, 9am (UTC)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_p0-concentration-patch_20260514T221709"
}
```

</details>

---

### Tool call

_source line 2 · 2026-05-14T22:19:38.753513+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/",
  "description": "List paper directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/",
    "description": "List paper directory"
  }
}
```

</details>

---

### Tool result

_source line 3 · 2026-05-14T22:19:38.753831+00:00_

Exit code 2
ls: cannot access '/home/ubuntu/.agent-ml-research-idea_gen_0509_2/docs/paper/': No such file or directory

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-14T22:19:38.753986+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/",
  "description": "List working dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_2/",
    "description": "List working dir"
  }
}
```

</details>

---

### Tool result

_source line 5 · 2026-05-14T22:19:38.754121+00:00_

AGENTS.md
config
global
idea_generator
projects
skills
state
workspace.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-14T22:19:38.754242+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"*.tex\" -type f 2>/dev/null | head -50",
  "description": "Find tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_2 -name \"*.tex\" -type f 2>/dev/null | head -50",
    "description": "Find tex files"
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-14T22:19:38.754378+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T163256/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/demo_calibrated_sim/artifacts/dream_reports/dream_20260513T153032/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/_project/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/artifacts/dream_reports/dream_20260514T002109/median/paper.tex
/home/ubuntu/.agent-ml-research-id
…[truncated 216 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-14T22:19:38.754517+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv && ls docs/paper/",
  "description": "List paper dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv && ls docs/paper/",
    "description": "List paper dir"
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T22:19:38.754669+00:00_

_pdf_images
abstract.tex
acl.sty
acl_natbib.bst
analysis.tex
appendix.tex
conclusion.tex
experiments.tex
figures
introduction.tex
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
method.tex
references.bib
references.bib.prev
related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-14T22:19:38.754849+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.(59|5856|5909|66|6156|6104|61)|0\\.50|concentration|Qwen|bf16|float32",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True",
  "head_limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.(59|5856|5909|66|6156|6104|61)|0\\.50|concentration|Qwen|bf16|float32",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True",
    "head_limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-14T22:19:38.755104+00:00_

docs/paper/analysis.tex:8:We quantify this with a \emph{top-5\% concentration metric}: sort per-head 2-bit distortions $d_h(2)$ in descending order and compute the fraction of total distortion contributed by the top 5\% of heads.
docs/paper/analysis.tex:9:High concentration indicates that a few heads are disproportionately sensitive; low concentration indicates near-uniform sensitivity.
docs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
docs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
docs/paper/analysis.tex:22:This is the ``spike'' pattern: high concentration driven by a single outlier with sensitivity at only one bitwidth.
docs/paper/analysis.tex:24:In contrast, Qwen's Layer-0 heads exhibit non-zero deltas at multiple bitwidths (e.g., L0H0: 2-bit delta ${=}6.74$, with positive 4-bit and 8-bit deltas), giving the solver a multi-bitwidth sensitivity gradient across several heads---a ``spread'' pattern that enables meaningful budget reallocation. %exp_id=qwen_hires_profiling
docs/paper/analysis.tex:27:Llama-3.1-8B shows above-threshold concentration ($0.57$) with a pronounced spike ($t_1/t_5{=}0.85$, $t_1/t_2{=}34.8$); its allocation is essentially indistinguishable from uniform ($+$0.36 vs.\ $+$0.38). %exp_id=llama_hires_bf16_2bitonly %exp_id=llama_hires_constrained
docs/paper/analysis.tex:28:Mistral-7B-v0.3 and Gemma-2-9B both exhibit flat distributions ($t_1/t_5{=}0.18$) with low concentration ($0.22$ and $0.23$ respectively), leaving the profiler with no reliable signal; constrained MCKP is slightly worse than uniform in both cases ($+$0.13 vs.\ $+$0.10 for Mistral; $+$0.15 vs.\ $+$0.13 for Gemma-2). %exp_id=mistral_c4
…[truncated 17563 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-14T22:19:38.755273+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
  "offset": "40",
  "limit": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/experiments.tex",
    "offset": "40",
    "limit": "80"
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T22:19:38.755474+00:00_

40	\begin{table}[t]
41	\centering
42	\small
43	\caption{PPL ($\downarrow$) on WikiText-2 at 4$\times$ compression. Unconstrained allocation fails catastrophically on $\{2,4,8,16\}$; our cardinality constraint restores performance. Best constrained result per model in \textbf{bold}. $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); standard profiling does not improve over uniform on these architectures. $^\ddagger$Best $k$ from ablation ($k{=}4$). The $\pm$0.06 on Qwen reports std over 3 calibration seeds (hires profiling); bit distributions are identical across seeds.}
44	\label{tab:main_results}
45	\begin{tabular}{lcccccc}
46	\toprule
47	Model & Baseline & Uniform & \multicolumn{2}{c}{Unconstrained} & Ours \\
48	 & (bf16) & (4-bit) & Greedy & MCKP & (Constr.) \\
49	\midrule
50	Qwen2.5-7B      & 9.81  & 15.45 & 32.45 & 36.92 & \textbf{11.23}$\pm$0.06 \\
51	Llama-3.1-8B    & 8.09  & 8.47  & ---   & ---   & \textbf{8.45}$^\dagger$ \\
52	Mistral-7B-v0.3 & 7.04  & 7.13  & ---   & ---   & 7.16$^{\dagger\ddagger}$ \\
53	Yi-1.5-9B$^\dagger$       & 7.02  & 7.22  & ---   & ---   & 7.22 \\
54	Gemma-2-9B      & 8.90  & 9.03  & ---   & ---   & 9.05 \\
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Table~\ref{tab:main_results} summarizes the main results.
60	On Qwen2.5-7B, constrained MCKP achieves 11.23 PPL, a 27.3\% reduction over uniform 4-bit (15.45).
61	Higher-resolution profiling (64 seq $\times$ 2048 tok) further improves this to 10.91; we report the standard-profiling result here and analyze the effect of profiling resolution in Appendix~\ref{sec:profiling_resolution}.
62	Without the cardinality constraint, both greedy (32.45) and MCKP (36.92) perform \emph{worse} than uniform---a catastrophic failure caused by excessive 2-bit assignments that compound across layers.
63	The constraint eliminates this failure mode entirely.
64	Across 3 calibration seeds, constrained MCKP yields mean PPL 10.99$\pm$0.06 (std is 1.3\% of the uniform gap), with 90.2\% three-way al
…[truncated 4003 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-14T22:19:38.755685+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.59|0\\.5856|0\\.5909|0\\.66|0\\.6156|0\\.6104|0\\.62",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.59|0\\.5856|0\\.5909|0\\.66|0\\.6156|0\\.6104|0\\.62",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T22:19:38.755874+00:00_

docs/paper/experiments.tex:101:2$\times$ & 10.10 & 10.66 & $-$0.56 \\
docs/paper/experiments.tex:111:Per-head optimization has no headroom here; constrained MCKP is slightly worse (10.66) due to unnecessary 2-bit assignments that the budget permits but the model does not need.
docs/paper/experiments.tex:168:WinoGrande & ---   & 0.662 & 0.682 & $+$2.0 pts \\
docs/paper/experiments.tex:170:Average    & 0.695 & 0.660 & 0.686 & $+$2.6 pts \\
docs/paper/experiments.tex:176:Constrained MCKP improves average 0-shot accuracy by 2.6 points over uniform 4-bit (0.686 vs.\ 0.660), with gains on all four benchmarks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-14T22:19:38.756032+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "bf16 range|float32|fp32|0\\.59.{0,3}0\\.66|range.*concentration|concentration.*range",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "bf16 range|float32|fp32|0\\.59.{0,3}0\\.66|range.*concentration|concentration.*range",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T22:19:38.756154+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-14T22:19:38.756268+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Qwen.{0,80}concentration|concentration.{0,80}Qwen",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Qwen.{0,80}concentration|concentration.{0,80}Qwen",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T22:19:38.756393+00:00_

docs/paper/introduction.tex:43:On our five architectures, the diagnostic separates the beneficial case (Qwen, concentration 0.61, spread pattern) from cases where non-uniform allocation provides no meaningful benefit.
docs/paper/introduction.tex:44:Yi-1.5 is a critical test: its concentration ($0.71$) exceeds Qwen's, but its heterogeneity is a single-outlier spike with no cross-bitwidth gradient---precisely the pattern where MCKP cannot redistribute budget.
docs/paper/introduction.tex:53:\item We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly separates architectures where non-uniform allocation helps from those where it does not, across all five models tested. Yi-1.5-9B serves as a critical test: its concentration exceeds Qwen's, yet its single-outlier spike pattern means MCKP provides no benefit over uniform (\S\ref{sec:heterogeneity}).
docs/paper/analysis.tex:14:Qwen2.5-7B exemplifies the spread pattern (top-5\% concentration 0.61, $t_1/t_5{=}0.57$), with Layer-0 heads contributing the majority of total 2-bit distortion across multiple bitwidths.
docs/paper/analysis.tex:17:Yi-1.5-9B is a critical counterexample: despite the highest concentration tested ($0.71$, exceeding Qwen's $0.61$), constrained MCKP matches uniform ($+$0.20 vs.\ $+$0.20). %exp_id=yi15_hires_constrained_mckp
docs/paper/analysis.tex:52:[Omitted long matching line]
docs/paper/conclusion.tex:7:Qwen2.5-7B (concentration 0.61, $t_1/t_5{=}0.57$, spread pattern) shows large gains; Llama-3.1-8B (concentration 0.57, $t_1/t_5{=}0.85$, spike) is essentially indistinguishable from uniform (8.45 vs.\ 8.47 PPL); Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B show no benefit.
docs/paper/conclusion.tex:8:Yi-1.5-9B is a critical test case: despite the highest concentration tested ($0.71$, exceeding Qwen), its heterogeneity is a single-outlier spike ($t_1/t_5{=}0.90$) with no cross-bitwidth sensitivity gradient, so MCKP cannot redistribute budget.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-14T22:19:38.756562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
  "offset": "30",
  "limit": "60"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/analysis.tex",
    "offset": "30",
    "limit": "60"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T22:19:38.756760+00:00_

30	\begin{table}[t]
31	\centering
32	\small
33	\caption{Head sensitivity heterogeneity and constrained allocation benefit across architectures at $4\times$ compression. $t_1/t_5$: ratio of top-1 to top-5 per-head 2-bit distortion (low${=}$spread, high${=}$spike). $^\dagger$Hires profiling (64 seq $\times$ 2048 tok); $^\ddagger$standard profiling, hires pending.}
34	\label{tab:heterogeneity}
35	\begin{tabular}{lcccccc}
36	\toprule
37	Model & GQA & Top-5\% & $t_1/t_5$ & $\Delta$ PPL & $\Delta$ PPL & Shape \\
38	 & Ratio & Conc. & & (Uniform) & (Ours) & \\
39	\midrule
40	Qwen2.5-7B & 7:1 & 0.61 & 0.57 & $+$5.64 & $+$1.42 & Spread \\
41	Yi-1.5-9B$^\dagger$ & 8:1 & 0.71 & 0.90 & $+$0.20 & $+$0.20 & Spike \\
42	Llama-3.1-8B$^\dagger$ & 4:1 & 0.57 & 0.85 & $+$0.38 & $+$0.36 & Spike \\
43	Mistral-7B-v0.3$^\dagger$ & 4:1 & 0.22 & 0.18 & $+$0.10 & $+$0.13 & Flat \\
44	Gemma-2-9B$^\ddagger$ & 2:1 & 0.23 & 0.18 & $+$0.13 & $+$0.15 & Flat \\
45	\bottomrule
46	\end{tabular}
47	\end{table}
48	
49	\begin{figure*}[t]
50	\centering
51	\includegraphics[width=\textwidth]{figures/fig1_head_delta_heatmap.pdf}
52	\caption{Per-head 2-bit quantization sensitivity across five architectures. Qwen2.5-7B shows high concentration in Layer-0 heads (``spread'' pattern); Yi-1.5-9B shows a single extreme outlier at Layer-4 Head-3 (``spike'' pattern); Llama-3.1-8B shows a dominant outlier at Layer-2 Head-5 (49\% of total distortion, ``spike'' pattern); Mistral-7B-v0.3 shows near-zero sensitivity across all heads; Gemma-2-9B exhibits the most uniform distribution, consistent with its low GQA ratio (2:1). Color intensity indicates PPL increase when the head is quantized to 2-bit.}
53	\label{fig:heatmap}
54	\end{figure*}
55	
56	Figure~\ref{fig:heatmap} visualizes the per-head 2-bit distortion as a heatmap.
57	The contrast is stark: Qwen's Layer-0 heads show high distortion (dark cells) while mid-to-deep layers are near-zero; Yi-1.5 shows a single bright spot at Layer-4 Head-3 (34\% of total delta) with 
…[truncated 3178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-14T22:19:38.756941+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T22:19:38.757133+00:00_

1	Per-head mixed-precision quantization of the KV cache promises lower perplexity than uniform quantization at the same average bit-width, but on hardware-aligned bit-widths $\{2, 4, 8, 16\}$, existing solvers fail catastrophically: unconstrained greedy and MCKP allocation achieve 32.45 and 36.92 perplexity on Qwen2.5-7B---far worse than uniform 4-bit (15.45).
2	We trace this failure to \emph{2-bit distortion compounding}: when the majority of heads are assigned 2-bit precision, per-head quantization errors interact non-additively through the residual stream, violating the additive objective assumed by standard solvers.
3	We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
4	On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
5	The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
6	However, the benefit depends on architecture: on Llama-3.1-8B the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation provides no benefit.
7	Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet gains nothing from non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.
8	We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly identifies all five architectures studied---distinguishing spread heterogeneity (MCKP-exploitable) from spik
…[truncated 72 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-14T22:19:38.757288+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "concentration|0\\.6|hires|profil",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "concentration|0\\.6|hires|profil",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T22:19:38.757419+00:00_

12:\label{sec:profiling_resolution}
14:We compare standard-resolution profiling (16 sequences $\times$ 512 tokens) against high-resolution profiling (64 sequences $\times$ 2048 tokens) on Qwen2.5-7B at $4\times$ compression.
16:High-resolution profiling improves constrained MCKP from 11.23 to 10.91 PPL ($-$0.32 absolute).
18:The improvement comes from finer-grained sensitivity estimates: standard profiling detects non-zero 2-bit distortion in 37 of 112 heads, while high-resolution profiling detects 100 of 112 (2.7$\times$ more).
21:High-resolution profiling protects shallow layers (L1--L3) at higher bit-widths while compressing mid-layers (L5--L11) more aggressively---a redistribution that standard profiling misses because its distortion estimates for these heads fall below the noise floor.
24:The profiled allocation is stable across calibration subsets.
25:Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
30:Float32 profiling (64 $\times$ 2048 tokens) yields an identical constrained allocation and PPL within seed variance (10.89 vs.\ 10.91, $\Delta = 0.02 < \sigma = 0.06$), confirming that bfloat16 precision is sufficient for the profiling step.
33:To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-14T22:19:38.757606+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
  "offset": "25",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper/appendix.tex",
    "offset": "25",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T22:19:38.757780+00:00_

25	Under hires profiling on Qwen2.5-7B, constrained MCKP yields mean PPL $10.99 \pm 0.06$ across 3 random calibration seeds (individual runs: 11.02, 10.90, 11.05), with std/mean below 0.6\%.
26	The bit distribution is identical across all seeds ($\{$2-bit: 8, 4-bit: 100, 8-bit: 4$\}$), and 101 of 112 heads (90.2\%) receive the same assignment in all three runs.
27	This stability confirms that the per-head sensitivity ranking is robust to calibration sampling noise.
28	
29	\paragraph{Numerical precision.}
30	Float32 profiling (64 $\times$ 2048 tokens) yields an identical constrained allocation and PPL within seed variance (10.89 vs.\ 10.91, $\Delta = 0.02 < \sigma = 0.06$), confirming that bfloat16 precision is sufficient for the profiling step.
31	
32	\paragraph{Per-layer optimality.}
33	To validate the additive distortion assumption underlying the MCKP formulation, we compare constrained MCKP against a per-layer brute-force oracle that exhaustively enumerates all $4^4 = 256$ bit-width combinations within each 4-head group on Qwen2.5-7B (hires profiling).
34	Of the 8 layers admitting multiple feasible allocations, MCKP matches the oracle exactly in 5; the remaining 3 show gaps of 0.018 (Layer~1), 0.014 (Layer~11), and 0.005 (Layer~4) PPL.
35	All three gaps involve repositioning a 2-bit assignment among heads with near-identical sensitivity within the same layer bit budget.
36	The negligible total gap ($<0.04$ PPL) confirms that the per-head additive distortion model closely approximates the true layer-level interaction.
37	
38	\section{KV Separation Ablation}
39	\label{sec:kv_separation}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-14T22:19:38.757929+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git status && echo \"---\" && git log --oneline -10",
  "description": "Check git status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "git status && echo \"---\" && git log --oneline -10",
    "description": "Check git status"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T22:19:38.758085+00:00_

On branch master
Changes not staged for commit:
  (use "git add &lt;file>..." to update what will be committed)
  (use "git restore &lt;file>..." to discard changes in working directory)
	modified:   docs/paper/abstract.tex
	modified:   docs/paper/analysis.tex
	modified:   docs/paper/appendix.tex
	modified:   docs/paper/conclusion.tex
	modified:   docs/paper/experiments.tex
	modified:   docs/paper/figures/fig1_head_delta_heatmap.pdf
	modified:   docs/paper/introduction.tex
	modified:   docs/paper/main.aux
	modified:   docs/paper/main.bbl
	modified:   docs/paper/main.blg
	modified:   docs/paper/main.fdb_latexmk
	modified:   docs/paper/main.fls
	modified:   docs/paper/main.log
	modified:   docs/paper/main.out
	modified:   docs/paper/main.pdf
	modified:   docs/paper/references.bib
	modified:   docs/paper/related_work.tex
	modified:   paper_provenance.yaml
	modified:   run_qwen_hires_constrained.py
	modified:   run_yi15_full_pipeline.py

Untracked files:
  (use "git add &lt;file>..." to include in what will be committed)
	.claude/
	AGENTS.md
	ROADMAP.lock
	ROADMAP.md
	artifacts/
	checkpoints/
	decisions.lock
	decisions.yaml
	docs/IDEA_BRIEF.md
	docs/paper/_pdf_images/
	docs/paper/figures/fig1_head_delta_heatmap.png
	docs/paper/figures/fig_concentration_scatter.pdf
	docs/paper/figures/fig_concentration_scatter.png
	dream_registry.lock
	dream_registry.yaml
	dream_registry.yaml.bak
	experiment_plan.lock
	experiment_plan.yaml
	figures/
	generate_hires_heatmap.py
	literature_map.lock
	literature_map.yaml
	logs/
	memory.md
	paper_framing.md
	paper_provenance.lock
	registry.lock
	registry.yaml
	report.md
	run_c4_cross_dataset.py
	run_gemma2_full_pipeline.py
	run_gemma2_hires_bf16_2bitonly.py
	run_k_ablation.py
	run_kv_separation.py
	run_llama_heuristic_k2.py
	run_llama_hires_bf16_2bitonly.py
	run_mistral_c4_cross_dataset.py
	run_mistral_hires_bf16_2bitonly.py
	run_yi15_hires_bf16_2bitonly.py
	run_yi15_hires_constrained.py
	run_yi15_hires_profiling.py
	study_status.lock
	task_context/
	
…[truncated 373 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-14T22:19:38.758235+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git diff docs/paper/abstract.tex docs/paper/analysis.tex docs/paper/appendix.tex docs/paper/conclusion.tex docs/paper/experiments.tex docs/paper/introduction.tex",
  "description": "Diff tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "git diff docs/paper/abstract.tex docs/paper/analysis.tex docs/paper/appendix.tex docs/paper/conclusion.tex docs/paper/experiments.tex docs/paper/introduction.tex",
    "description": "Diff tex files"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T22:19:38.758448+00:00_

&lt;persisted-output>
Output too large (30.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/b3uh5wxsl.txt

Preview (first 2KB):
diff --git a/docs/paper/abstract.tex b/docs/paper/abstract.tex
index f56c7d6..26e3464 100644
--- a/docs/paper/abstract.tex
+++ b/docs/paper/abstract.tex
@@ -3,5 +3,6 @@ We trace this failure to \emph{2-bit distortion compounding}: when the majority
 We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
 On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
 The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
-However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
-We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
+However, the benefit depends on architecture: on Llama-3.1-8B the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation provides no benefit.
+Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet gains nothing from non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enab
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-14T22:19:38.758604+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/b3uh5wxsl.txt",
  "description": "Read full diff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/b3uh5wxsl.txt",
    "description": "Read full diff"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T22:19:38.758833+00:00_

&lt;persisted-output>
Output too large (30.5KB). Full output saved to: /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/bzu5q4tdc.txt

Preview (first 2KB):
diff --git a/docs/paper/abstract.tex b/docs/paper/abstract.tex
index f56c7d6..26e3464 100644
--- a/docs/paper/abstract.tex
+++ b/docs/paper/abstract.tex
@@ -3,5 +3,6 @@ We trace this failure to \emph{2-bit distortion compounding}: when the majority
 We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
 On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
 The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
-However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
-We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
+However, the benefit depends on architecture: on Llama-3.1-8B the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation provides no benefit.
+Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet gains nothing from non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enab
…[truncated 69 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-14T22:19:38.758980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/b3uh5wxsl.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2/d01416c0-6fc1-4e02-b20b-b6d511da8957/tool-results/b3uh5wxsl.txt"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T22:19:38.759266+00:00_

1	diff --git a/docs/paper/abstract.tex b/docs/paper/abstract.tex
2	index f56c7d6..26e3464 100644
3	--- a/docs/paper/abstract.tex
4	+++ b/docs/paper/abstract.tex
5	@@ -3,5 +3,6 @@ We trace this failure to \emph{2-bit distortion compounding}: when the majority
6	 We show that a single cardinality constraint capping the number of 2-bit assignments is a minimal sufficient fix.
7	 On Qwen2.5-7B at $4\times$ compression, constrained allocation achieves 11.23 perplexity, a 27.3\% reduction over uniform 4-bit.
8	 The constraint also renders solver choice irrelevant: constrained greedy and constrained MCKP produce equivalent bit-width assignments across all three tested architectures ($\Delta{=}0.0000$), enabling use of a simple $O(H \log H)$ greedy algorithm; per-layer brute-force oracle confirms near-optimality (max gap 0.02 PPL).
9	-However, the benefit depends on architecture: on Llama-3.1-8B the improvement is marginal (8.45 vs.\ 8.47), and on Mistral-7B-v0.3 non-uniform allocation is slightly counterproductive (7.16 vs.\ 7.13).
10	-We propose a heterogeneity diagnostic based on the concentration of per-head sensitivity that can indicate, before any allocation, whether a given architecture will benefit from non-uniform quantization.
11	+However, the benefit depends on architecture: on Llama-3.1-8B the result is essentially indistinguishable from uniform (8.45 vs.\ 8.47), and on Mistral-7B-v0.3, Yi-1.5-9B, and Gemma-2-9B non-uniform allocation provides no benefit.
12	+Notably, Yi-1.5-9B has the highest GQA ratio tested (8:1) and the highest top-5\% concentration (0.71), yet gains nothing from non-uniform allocation---because its heterogeneity is a single-outlier ``spike'' with no cross-bitwidth sensitivity gradient, rather than the ``spread'' pattern that enables MCKP to redistribute budget across heads.
13	+We propose a joint diagnostic combining concentration and distribution shape ($t_1/t_5$ ratio) that correctly identifies all five architectures studied---distinguish
…[truncated 30307 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-14T22:19:38.759468+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git diff docs/paper/related_work.tex",
  "description": "Check related_work diff"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "git diff docs/paper/related_work.tex",
    "description": "Check related_work diff"
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T22:19:38.759620+00:00_

diff --git a/docs/paper/related_work.tex b/docs/paper/related_work.tex
index edeb3f2..26ff723 100644
--- a/docs/paper/related_work.tex
+++ b/docs/paper/related_work.tex
@@ -6,12 +6,13 @@ We extend the design space to per-head non-uniform allocation over hardware-alig
 
 \paragraph{KV Cache Eviction.}
 Complementary to quantization, eviction methods reduce cache size by discarding tokens---retaining heavy-hitters~\cite{zhang2023h2o}, per-head important tokens~\cite{li2024snapkv,ge2024fastgen}, persistent-importance tokens~\cite{liu2024scissorhands}, attention sinks~\cite{xiao2024streamingllm}, or progressively fewer tokens in deeper layers~\cite{yang2024pyramidinfer}.
-Our work focuses exclusively on the quantization allocation problem.
+Recent per-head eviction methods allocate non-uniform budgets across heads based on retrieval-vs-reasoning importance~\cite{fu2025headkv} or adaptive optimization extending SnapKV/PyramidKV~\cite{feng2025adakv}, confirming that head-level heterogeneity is exploitable for eviction; our work shows it is equally exploitable for quantization.
+
 
 \paragraph{Mixed-Precision Rate-Distortion Allocation.}
 RateQuant~\cite{zuo2026ratequant} formulates per-head bit-width selection as an MCKP and proves greedy optimality for consecutive bit-widths $\{2,\ldots,6\}$ via the polymatroid structure.
 On hardware-aligned $\{2,4,8,16\}$, this structure breaks; we show that unconstrained solvers fail catastrophically due to 2-bit distortion compounding, a failure mode absent in RateQuant's setting.
-Related mixed-precision work operates at coarser granularity (layer-level~\cite{li2025kvmix}, memory-budget-level~\cite{lei2026arkv}), at the weight level~\cite{kim2024squeezellm}, or dynamically at inference time~\cite{zhang2025mixkvq}; our allocation is static and per-head.
+Related mixed-precision work operates at coarser granularity---layer-level via gradient-based sensitivity~\cite{li2025kvmix} or Pareto search over hardware-friendly precision pairs~\
…[truncated 385 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-14T22:19:38.759825+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.59--0\\.66|0\\.59-0\\.66|0\\.5856|0\\.5909|0\\.6156|0\\.6104",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.59--0\\.66|0\\.59-0\\.66|0\\.5856|0\\.5909|0\\.6156|0\\.6104",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/ratekv/docs/paper",
    "glob": "*.tex"
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-14T22:19:38.759957+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-14T22:19:38.760130+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git add docs/paper/abstract.tex docs/paper/analysis.tex docs/paper/appendix.tex docs/paper/conclusion.tex docs/paper/experiments.tex docs/paper/introduction.tex docs/paper/related_work.tex && git commit -m \"$(cat <<'EOF'\nP0: unify Qwen concentration to 0.61 (float32 verified)\n\nCo-Authored-By: Claude Opus 4.7 (1M context) &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit tex changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "git add docs/paper/abstract.tex docs/paper/analysis.tex docs/paper/appendix.tex docs/paper/conclusion.tex docs/paper/experiments.tex docs/paper/introduction.tex docs/paper/related_work.tex && git commit -m \"$(cat <<'EOF'\nP0: unify Qwen concentration to 0.61 (float32 verified)\n\nCo-Authored-By: Claude Opus 4.7 (1M context) &lt;noreply@anthropic.com>\nEOF\n)\"",
    "description": "Commit tex changes"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-14T22:19:38.760274+00:00_

[master bfaea4e] P0: unify Qwen concentration to 0.61 (float32 verified)
 Committer: Ubuntu &lt;ubuntu@ip-172-31-2-106.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 7 files changed, 114 insertions(+), 45 deletions(-)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 42 · 2026-05-14T22:19:38.760464+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "git log --oneline -3",
  "description": "Verify commit"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "tool_args": {
    "command": "git log --oneline -3",
    "description": "Verify commit"
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T22:19:38.760626+00:00_

bfaea4e P0: unify Qwen concentration to 0.61 (float32 verified)
c4ead3c add Qwen2.5-7B constrained MCKP + WikiText-2 eval script
0ddb176 add Yi-1.5-9B full pipeline script

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_p0-concentration-patch_20260514T221709",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-14T22:19:38.760826+00:00_

完成。

**核查结果**：
- `docs/paper/` 下所有 .tex 文件中 Qwen 的 top-5% concentration 值已全部为 **0.61**（共 6 处：`analysis.tex` ×4、`introduction.tex` ×1、`conclusion.tex` ×1）
- 旧值 `0.59--0.66` / `0.59-0.66` / `0.5856` / `0.5909` / `0.66` / `0.6156` / `0.6104` 已无残留
- 其他模型值未动：Yi=0.71、Llama=0.57、Mistral=0.22、Gemma-2=0.23
- 5-model table（`analysis.tex:40`）Qwen 行 concentration 列为 `0.61`，未标 float32/range
- 无 "bf16 range" 表述

**Commit**: `bfaea4e P0: unify Qwen concentration to 0.61 (float32 verified)` — 7 files changed (含 `related_work.tex` 引用更新一并提交)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_p0-concentration-patch_20260514T221709"
}
```

</details>

---
