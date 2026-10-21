# paper placeholder audit

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 0
- **Tool calls:** 16
- **Original source:** `logs/chats/worker_paper_placeholder_audit_20260523T144109.jsonl`
- **Structured JSON:** [`048d54c6be2aadb4ea2e.json`](../../sessions/04/048d54c6be2aadb4ea2e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

33 recorded events

### Tool call

_source line 1 · 2026-05-23T14:43:45.555915+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-23T14:43:45.556468+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct on 8K multi-turn conversations from the UltraChat training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and PPL.
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\to$${\sim}$0.50). Convergence near $\tau$\,=\,0.5 is expected given the shared GAR loss and does not demonstrate gating benefit. GAR-Dongre remains low (0.01--0.02); scheduled sampling breaks this pattern (\S\ref{sec:discussion}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}a). ThreadGate significantly outperforms LoRA-only (Wilcoxon $p$\,=\,0.004, $r$\,=\,0.454; GAR-ours 0.064 vs 0.037; Appendix~\ref{sec:appendix-stats}), yet the residual gap remains large (7.8$\times$). A second seed (123) confirms TF stability ($0.504\pm0.001$). We analyze this distribution shift in \S\ref{sec:analysis}.
13	
14	\begin{table*}[t]
15	\centering
16	\small
17	\caption{Five-way comparison on Qwen-2.5-7B-Instruct. TF evaluation uses IID UltraChat and 50 held-out conversations; AR evaluation uses $N$\,=\,50 held-out conversations (
…[truncated 2869 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-23T14:43:45.556715+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-23T14:43:45.556866+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	The failure traces to an incompatibility between teacher-forcing and GAR-family auxiliary losses, not to the gating architecture. NTP gradient pressure (7.5--14.7$\times$ GAR magnitude) pushes gates toward identity (2--7\% attenuation). Steering ($\beta$\,=\,5) recovers GAR from 0.064 to 0.727, confirming attention misallocation as the proximal cause (\S\ref{subsec:steering}).
4	
5	\paragraph{Scheduled sampling and downstream effects.} Scheduled sampling \citep{bengio2015scheduled} increases AR GAR-ours from 0.064 to 0.347 (5.4$\times$), compressing the 7.8$\times$ gap to 1.44$\times$ with negligible PPL change (1.44 vs.\ 1.43); a second seed yields 0.418 (gap 1.20$\times$). GAR-Dongre also rises (0.019$\to$0.353; $N$\,=\,5 pilot). The gating benefit diminishes in longer dialogues (Appendix~\ref{sec:appendix-n5}), consistent with compounding over turns. KV cache drift is a downstream consequence; instruction retention ($\beta$\,=\,3) shows content compliance rising +23.8\,pp ($p$\,=\,0.077) with GAR correlation $r$\,=\,0.200 ($p$\,=\,0.007), while format constraints show no change (Appendix~\ref{sec:appendix-ir}).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-23T14:43:45.557011+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T14:43:45.557812+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Fine-tuned to allocate 50\% of its attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse that widens to 27$\times$ on Llama-3.1-8B. This paper traces the failure to exposure bias \citep{bengio2015scheduled}: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text, even when next-token prediction (NTP) remains robust.
4	
5	Multi-turn attention decay is well-documented---\citet{dongre2026attention} showed that the Goal Accessibility Ratio (GAR), measuring attention to system-prompt goal tokens, declines 27--48\% across 12 models (we observe 70.8\% on Qwen-2.5-7B) while residual stream probes retain goal content (AUC\,=\,0.98)---but three research gaps remain open. To our knowledge, no work examines how per-layer transformer behavior varies across conversation turns (the \emph{turn$\times$depth} gap). Existing remediations---split-softmax \citep{li2024measuring}, StreamingLLM \citep{xiao2024streaming}, gated attention \citep{qiu2025gated}---operate at inference time or are turn-agnostic; \emph{training-time} multi-turn attention optimization has not been attempted. And classical exposure bias mitigation \citep{bengio2015scheduled,lamb2016professor} targets RNN sequence generation; no \emph{multi-turn transformer equivalent} exists.
6	
7	ThreadGate addresses these gaps with per-layer content-and-turn-conditioned MLP gates on the residual stream: $x_{l+1} = x_l + g_l \cdot f_l(x_l)$, where $g_l$ is a two-layer network conditioned on hidden states and turn position. A five-way controlled comparison---ThreadGate, +PCGrad, Uniform Gate, LoRA-only, Base---isolates turn conditioning, gating, gradient conflict, and fine-tuning (\S\ref{sec:comparison-design}), where each adjacent pair kills exactly one alternative hypothesis.
8	
9	\begin{figure*}[t]
10	  \centerin
…[truncated 1651 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-23T14:43:45.558004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T14:43:45.558144+00:00_

1	\begin{abstract}
2	Fine-tuned to allocate 50\% of attention to system-prompt goals (GAR\,=\,0.50 under teacher forcing), Qwen-2.5-7B-Instruct retains only GAR\,=\,0.064 under autoregressive generation---an 8$\times$ collapse. We trace this failure to exposure bias: attention patterns optimized under teacher-forced prefixes do not transfer to model-generated text. ThreadGate, per-layer content-and-turn-conditioned MLP gates trained with an auxiliary GAR loss, provides a controlled testbed. A five-way comparison isolates turn conditioning, gating, gradient conflict, and fine-tuning; each pair kills one hypothesis. Gating outperforms LoRA-only ($p$\,=\,0.004) but the gap remains 7.8$\times$; PCGrad eliminates gradient conflict but \emph{worsens} AR GAR ($p$\,=\,0.002), ruling out the most intuitive failure mechanism by \emph{modus tollens}. Steering ($\beta$\,=\,5) recovers GAR to 0.727; scheduled sampling compresses the gap to 1.44$\times$ (single seed). Cross-model evaluation on Llama-3.1-8B confirms a 27$\times$ gap. These findings establish that exposure bias selectively destroys auxiliary attention losses while NTP self-recovers---a failure mode without prior multi-turn transformer characterization.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-23T14:43:45.558284+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-23T14:43:45.558442+00:00_

1	\section{Conclusion}\label{sec:conclusion}
2	
3	A five-way controlled comparison on ThreadGate---per-layer content-and-turn-conditioned gates with an auxiliary GAR loss---reveals that training succeeds (TF GAR\,=\,0.50) but autoregressive GAR collapses 8--17$\times$ on Qwen-2.5-7B (27$\times$ on Llama-3.1-8B). Each ablation pair kills one hypothesis: turn conditioning does not rescue late-turn attention; gradient conflict is causally inconsequential ($p$\,=\,0.002, effect reverses); gating outperforms LoRA-only ($p$\,=\,0.004) but cannot close the gap. The failure traces to exposure bias---a mechanism classical in origin but with no prior multi-turn transformer characterization. Steering ($\beta$\,=\,5, GAR 0.727) and scheduled sampling (gap 7.8$\times$$\to$1.44$\times$; single seed) provide the first evidence that this barrier is surmountable.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-23T14:43:45.558666+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "TODO|XXX|FIXME|TBD|PLACEHOLDER|\\?\\?|single seed|preliminary|to be updated",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "TODO|XXX|FIXME|TBD|PLACEHOLDER|\\?\\?|single seed|preliminary|to be updated",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T14:43:45.558800+00:00_

paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/abstract.tex:2:[Omitted long matching line]
paper/sections/limitations.tex:3:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-23T14:43:45.558919+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\textbf\\{\\?\\}|---\\s*$|1\\.5B|MMLU|bootstrap|multi-seed|three.seed|3.seed",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\textbf\\{\\?\\}|---\\s*$|1\\.5B|MMLU|bootstrap|multi-seed|three.seed|3.seed",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T14:43:45.559038+00:00_

paper/sections/related_work.tex:13:[Omitted long matching line]
paper/sections/appendix.tex:120:\paragraph{Bootstrap confidence intervals.} The 95\% CIs in Table~\ref{tab:four-way} are computed via 10,000 bootstrap resamples of per-conversation mid-turn GAR averages (turns 2--$T$), using the percentile method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-23T14:43:45.559170+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "% .*update|% .*fill|% .*replace|% .*pending|% .*need",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "% .*update|% .*fill|% .*replace|% .*pending|% .*need",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-23T14:43:45.559288+00:00_

No matches found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-23T14:43:45.559437+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "single seed",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": "True",
  "-C": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "single seed",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True",
    "-C": "1"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T14:43:45.559609+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/conclusion.tex-2-
paper/sections/conclusion.tex:3:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex-2-
paper/sections/limitations.tex:3:[Omitted long matching line]
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-1-\begin{abstract}
paper/sections/abstract.tex:2:[Omitted long matching line]
/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/abstract.tex-3-\end{abstract}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-23T14:43:45.559734+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "Llama.*gap|cross.model|27",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
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
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "Llama.*gap|cross.model|27",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-23T14:43:45.560010+00:00_

paper/sections/analysis.tex:3:[Omitted long matching line]
paper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
paper/sections/analysis.tex:16:  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}
paper/sections/analysis.tex:39:We test specificity with Turn-level Residual Coherence (TRC), the cosine similarity between adjacent-turn hidden states. TF/AR TRC is 0.334/0.332 for ThreadGate (gap $+$0.002) and 0.349/0.411 for LoRA-only (gap $-$0.062, reversed), confirming exposure bias disrupts a specific routing behavior while leaving representations intact. Cross-model evaluation confirms: GAR-Dongre shows negligible shift on both Llama (1.002$\times$) and Qwen (1.28$\times$) vs.\ the order-of-magnitude GAR-ours collapse.
paper/sections/analysis.tex:41:\subsection{Cross-Model Replication}\label{subsec:cross-model}
paper/sections/analysis.tex:43:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:19:[Omitted long matching line]
paper/sections/experiments.tex:34:LoRA-only         & 0.50 & 0.01 & 2.78 & 0.50 & 0.01 & 2.78 & 0.037 & {\scriptsize[.027,\,.050]} & 1.00 \\
paper/sections/experiments.tex:48:[Omitted long matching line]
paper/sections/conclusion.tex:3:[Omitted long matching line]
paper/sections/discussion.t
…[truncated 4570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-23T14:43:45.560292+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-23T14:43:45.560467+00:00_

1	\section{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B), one dataset (UltraChat, 8K conversations), and primarily a single seed (ThreadGate adds seed\,=\,123; the remaining variants rely on cross-variant convergence); the instruction retention analysis is exploratory (single model, single $\beta$). We test only one auxiliary loss family (GAR with MSE target $\tau$\,=\,0.5); head-specific or layer-specific attention losses may exhibit different sensitivity to exposure bias, and all variants share the same GAR objective, so we do not test whether gating could succeed under a different training signal. The PCGrad exclusion addresses gradient direction conflict only; magnitude imbalance \citep{chen2018gradnorm} and Nash equilibrium approaches \citep{navon2022nash} remain untested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-23T14:43:45.560646+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-23T14:43:45.560820+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	The five-way comparison (\S\ref{sec:experiments}) yields a paradox: training succeeds but inference fails, and no single architectural factor explains the gap. This section resolves it through a causal exclusion chain---each subsection kills one alternative hypothesis: \S\ref{subsec:gate-conditioning} kills ``turn conditioning rescues late-turn attention''; \S\ref{subsec:pcgrad} kills ``gradient conflict prevents GAR convergence''; \S\ref{subsec:dist-shift} identifies exposure bias as the surviving explanation. \S\ref{subsec:mechanism-specificity} confirms selectivity via an orthogonal metric, and \S\ref{subsec:cross-model} confirms generalization across architectures.
4	
5	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
6	
7	The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
8	
9	The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
10	
11	Inference-time gate values range from 0.93 to 0.98 (2--7\% attenuation), explaining the near-convergence in Table~\ref{tab:four-way}. Figure~\ref{fig:gate-shift}(a) visualizes the inversion (Appendix~\ref{sec:appendix-viz}). Does the NTP-GAR gradient conflict prevent the intended behavior? If so, resolving it should rescue gate conditioning.
12	
13	\begin{figure}[t]
14	  \centering
15	  \includegraphics[width=\columnwidth,he
…[truncated 4426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-23T14:43:45.560974+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "0\\.347|0\\.418|scheduled sampling|SS |seed 123|seed.?42|\\\\pm",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
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
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "0\\.347|0\\.418|scheduled sampling|SS |seed 123|seed.?42|\\\\pm",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-23T14:43:45.561177+00:00_

paper/sections/analysis.tex:3:[Omitted long matching line]
paper/sections/analysis.tex:7:The design intent of ThreadGate is to modulate the residual stream more aggressively at late conversation turns, where GAR naturally decays (\S\ref{sec:background}). We test whether the learned gates achieve this by comparing gate values at turn~1 (early) and turn~21 (late) across all 28 layers of the trained model.
paper/sections/analysis.tex:9:The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$). For example, layer~23 gates from 0.769 (turn~1) to 0.979 (turn~21). Gates suppress more at early turns (high GAR) and become passive at late turns (low GAR), because NTP pressure---strongest at late turns with long contexts---pushes gates toward 1.0 to preserve sublayer computation.
paper/sections/analysis.tex:16:  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift: the TF-AR GAR gap persists across all five variants (TG, +PCGrad, UG, LoRA-only, Base) under our evaluation conditions.}
paper/sections/analysis.tex:35:[Omitted long matching line]
paper/sections/related_work.tex:4:[Omitted long matching line]
paper/sections/related_work.tex:7:[Omitted long matching line]
paper/sections/related_work.tex:13:[Omitted long matching line]
paper/sections/related_work.tex:19:[Omitted long matching line]
paper/sections/experiments.tex:6:[Omitted long matching line]
paper/sections/experiments.tex:10:Table~\ref{tab:four-way} presents the five-way comparison. Under TF evaluation, all four fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. The Base model confirms LoRA fine-tuning as the operative variable (GAR-ours: 0.01$\to$${\sim}$0.50). Convergence near $\tau$\,=\,0.5 is expected given the shared GA
…[truncated 12750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-23T14:43:45.561349+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T14:43:45.561668+00:00_

1	\section{Training Configuration}\label{sec:appendix-hyper}
2	
3	Table~\ref{tab:hyperparams} lists the full training configuration shared across all fine-tuned variants. ThreadGate gate parameters receive a $10\times$ learning rate multiplier and are initialized with bias 1.5 ($\sigma(1.5) \approx 0.82$); the gate MLP adds ${\sim}$57K parameters per variant ($<$0.001\% of 7B). The scheduled sampling variant (v8b) linearly increases the model-generated context ratio from 0 to 0.5 over 3 epochs (29.7--37.1\% effective usage due to per-sample Bernoulli sampling). All experiments were conducted on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (102\,GB VRAM), requiring 6--8 hours per variant.
4	
5	\begin{table}[h]
6	\centering\small
7	\caption{Training hyperparameters for all fine-tuned variants. Entries marked $\dagger$ apply only to ThreadGate and its ablations.}
8	\label{tab:hyperparams}
9	\begin{tabular}{l@{\hspace{8pt}}l}
10	\toprule
11	\textbf{Parameter} & \textbf{Value} \\
12	\midrule
13	Base model & Qwen-2.5-7B-Instruct \\
14	LoRA rank / $\alpha$ & 16 / 32 \\
15	LoRA targets & \texttt{q\_proj}, \texttt{v\_proj} \\
16	Optimizer & AdamW ($\beta_1$\!=\!0.9, $\beta_2$\!=\!0.999) \\
17	Learning rate & $2 \times 10^{-4}$ \\
18	Gate LR mult.$^\dagger$ & $10\times$ \\
19	Batch / grad accum & 1 / 8 (eff.\ 8) \\
20	Epochs & 3 \\
21	Max seq length & 2048 \\
22	Training data & 8K UltraChat convs \\
23	Seed & 42 (+123 for TG, SS) \\
24	$\lambda_\text{GAR}$/$\lambda_\text{div}$ & 1.0 / 1.0 \\
25	GAR target $\tau$ & 0.5 \\
26	Gate init bias$^\dagger$ & 1.5 ($\sigma\!\approx\!0.82$) \\
27	Gate hidden dim$^\dagger$ & 64 \\
28	Turn embed dim$^\dagger$ & 16 \\
29	GPU & RTX PRO 6000 (102\,GB) \\
30	Training time & 6--8 h / variant \\
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	\section{Loss Formulation Search}\label{sec:appendix-loss}
36	
37	The final MSE + gate diversity loss (\S\ref{sec:loss}) emerged from seven iterations spanning four loss families. Table~
…[truncated 26799 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-23T14:43:45.561889+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "1\\.5B|1\\.5b|MMLU|mmlu",
  "-i": "True",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
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
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "tool_args": {
    "pattern": "1\\.5B|1\\.5b|MMLU|mmlu",
    "-i": "True",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper",
    "glob": "*.tex",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T14:43:45.562023+00:00_

paper/sections/related_work.tex:13:[Omitted long matching line]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-23T14:43:45.562144+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/ROADMAP.md"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T14:43:45.562289+00:00_

1	# turn_residual_gating — Research Dashboard
2	
3	> 最后更新: 2026-05-22 16:57 UTC | 更新原因: DDL 修正 5/25 + 今日大量工作完成反映 + 写作线收尾
4	
5	## 核心方向
6	Diagnostic framework: lightweight residual gating 的 auxiliary attention loss 在 text distribution shift (exposure bias) 下泛化失败（~31× gap）。PCGrad 排除梯度方向冲突。**双路 mitigation 已验证**：inference-time attention steering (β=5, GAR 0.064→0.727, N=50) + training-time scheduled sampling (GAR 0.016→0.318, gap → 1.57×, PPL 不变)。**跨模型泛化确认**：Llama-3.1-8B gap 27× (median, N=20)。详见 paper_framing.md。
7	
8	## 当前进展
9	- **阶段**: D048 修复 + 提交准备（**DDL: ARR May 2026-05-25，剩余 3 天**）
10	- **核心 claim**: C1✅ C2✅ C3✅ C4✅ C5✅ C6✅(N=50) C7✅(dual-seed)
11	- **成功率**: 27 success / 5 negative / 3 failed / 37 total
12	- **审稿**: Group C Round 3 Overall 3.0 (Findings)，目标 3.5 (Conference)
13	- **写作**: Round 3 全部 13 项修复完成，主文 8 页，编译 0 error
14	- **附录**: Appendix A-D 完整（超参/loss iterations/instruction retention/可视化 6 图表）
15	- **论文编译**: 14 页 0 error 0 undefined ref
16	
17	## 近期任务
18	
19	### 实验线（GPU 串行，westd-20861:cuda:0）
20	- [ ] **SS s42 训练** — resume v3 运行中，epoch 1-2，预计 ~20:00 UTC 完成
21	- [ ] **SS s42 eval** — TF + AR N=50 + bootstrap CI（训练完成后立即执行，~1h）
22	- [ ] **AR N=50 existing** — TG/UG/PCGrad/LO 4 条件扩容（~8h）
23	- [ ] **SS s123 + s456 训练+eval** — 各 ~5h+1h
24	- [ ] **Base/TG multi-seed** — s123/s456 各 ~5h+1h
25	- [ ] ~~GradNorm~~ / ~~Llama PCGrad+UG~~ / ~~N=200~~ — 如时间允许
26	
27	### 写作线（已基本完成）
28	- [x] Round 3 全部 13 项写作修复（GAR 命名/Rhea/贡献措辞/PCGrad scope/页数/Discussion 压缩等）
29	- [x] Appendix D: 6 个可视化（gate heatmap/cross-model/AR GAR decay/gate distribution/loss curves/β-steering table）
30	- [x] Table 2 扩展 Failure Mechanism 列
31	- [x] 图片同步 + 编译验证（14 页 0 error）
32	- [ ] Abstract/Intro/Conclusion 数字更新为 mean±std（等 multi-seed 数据）
33	
34	### 提交准备
35	- [ ] Multi-seed 数字更新论文
36	- [ ] 最终编译 + 视觉审查
37	- [ ] Round 4 Group C 审稿
38	- [ ] 5/25 提交 ARR May
39	
40	## GPU 预算
41	- **已分配**: westd-20861:cuda:0 (1×RTX PRO 6000 Blackwell, 102GB)
42	- **当前**: SS s42 resume v3 训练中
43	- **累计 GPU 时间**: ~160h
44	-
…[truncated 1679 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_placeholder_audit_20260523T144109",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-23T14:43:45.562534+00:00_

## 占位符清单

| # | 文件 | 行号 | 当前内容 | 需要什么数据 |
|---|------|------|---------|------------|
| **abstract.tex** | | | | |
| 1 | abstract.tex | L2 | `1.44× (single seed)` | SS 3-seed mean±std 后的 gap 值，去掉 "single seed" 标记 |
| **introduction.tex** | | | | |
| 2 | introduction.tex | L16 | `gap 7.8×→1.44×` | SS 3-seed gap 更新值 |
| 3 | introduction.tex | L18 | `(gap 7.8×→1.44×)` | 同上，贡献 (3) 中的 SS gap |
| **experiments.tex** | | | | |
| 4 | experiments.tex | L6 | `seed 42; ThreadGate additionally with seed 123` | 如有 multi-seed，需更新描述 |
| 5 | experiments.tex | L12 | `A second seed (123) confirms TF stability ($0.504\pm0.001$)` | AR 方面也需要 multi-seed 数据 |
| 6 | experiments.tex | L29 | ThreadGate AR GAR `0.064` CI `[.041,.091]` | s42 单 seed，需 multi-seed mean±std |
| 7 | experiments.tex | L30 | +PCGrad AR GAR `0.030` CI `[.023,.038]` | s42 单 seed，需 multi-seed mean±std |
| 8 | experiments.tex | L31 | Uniform Gate AR GAR `0.033` CI `[.025,.043]` | s42 单 seed，需 multi-seed mean±std |
| 9 | experiments.tex | L34 | LoRA-only AR GAR `0.037` CI `[.027,.050]` | s42 单 seed，需 multi-seed mean±std |
| 10 | experiments.tex | L12 | `Wilcoxon p=0.004, r=0.454` | multi-seed 后可能需更新统计检验 |
| 11 | experiments.tex | L12 | `GAR-ours 0.064 vs 0.037` | 更新为 multi-seed 值 |
| 12 | experiments.tex | L10 | `8--17×` gap range | multi-seed 后 gap range 可能变化 |
| 13 | experiments.tex | L48 | steering `0.064→0.556` (β=3), `0.727±0.061` (β=5) | 基于 TG s42 单 seed，可能需 multi-seed |
| **discussion.tex** | | | | |
| 14 | discussion.tex | L3 | `0.064 to 0.727` | TG 单 seed steering 数据 |
| 15 | discussion.tex | L5 | SS GAR `0.064 to 0.347 (5.4×)` | SS s42 单 seed → 需 3-seed mean±std |
| 16 | discussion.tex | L5 | `gap to 1.44× with negligible PPL change (1.44 vs. 1.43)` | SS 3-seed mean±std gap 和 PPL |
| 17 | discussion.tex | L5 | `a second seed yields 0.418 (gap 1.20×)` | 合并为 3-seed mean±std 报告 |
| 18 | discussion.tex | L5 | `GAR-Dongre also rises (0.019→0.353; N=5 pilot)` | 仍是 N=5 pilot，是否扩大到 N=50？ |
| 19 | discussion.tex | L5 | `content compliance rising +23.8 pp (p=0.077)` | 单模型探索性数据，limitations 已声明 |
| **conclusion.tex** | | | | |
| 20 | conclusion.tex | L3 | `gap 7.8×→1.44×; single seed` | SS 3-seed gap，去掉 "single seed" |
| 21 | conclusion.tex | L3 | `8--17×` on Qwen | multi-seed 后 gap range 可能变化 |
| **limitations.tex** | | | | |
| 22 | limitations.tex | L3 | `primarily a single seed` | multi-seed 完成后需更新措辞 |
| **analysis.tex** | | | | |
| 23 | analysis.tex | L43 | Llama TF `0.484`/`0.481`, AR mean `0.043`/`0.028`, median `0.018`/`0.018` | Llama 单 seed，无 ±std |
| 24 | analysis.tex | L43 | Llama gap `27×`/`26×` (median), `11×`/`17×` (mean) | 单 seed，无置信区间 |
| **appendix.tex** | | | | |
| 25 | appendix.tex | L138 | `SS vs. TG` Wilcoxon `p<0.001, r=0.869` | 基于 s42 单 seed 对比 |
| 26 | appendix.tex | L156 | Llama AR: `mean 0.043, std 0.100` | 单 seed，无跨 seed 统计 |
| 27 | appendix.tex | L301-302 | SS s42 `6.5h`, SS s123 `10.8h` | 若有 s456 需补充训练时间 |

### 按优先级分组

**P0 — 论文中已标记 "single seed"，必须更新：**
- #1, #20: abstract/conclusion 显式标记 `single seed`
- #15-17: discussion 中 SS 两个 seed 的独立数值 → 合并为 3-seed mean±std
- #22: limitations 措辞更新

**P1 — 主表/主文 AR 数字（当前 s42 单 seed）：**
- #6-9: Table 1 所有 AR GAR 和 CI
- #10-12: 关联统计检验和 gap range
- #2-3: intro 中引用的 SS gap

**P2 — Llama 跨模型数据（单 seed，无 CI）：**
- #23-24: analysis 中 Llama 所有数字
- #26: appendix Llama 详细数据

**P3 — 论文中完全缺失的数据：**
- **1.5B cross-model**: 论文全文无任何 1.5B 模型数据
- **MMLU**: 论文全文无 MMLU 评估
- 这两项在当前论文中未承诺也未引用，如不做可无需占位

**P4 — 次要/探索性：**
- #13-14: steering 数据（单 seed，但作为 diagnostic 可接受）
- #18: GAR-Dongre SS pilot（N=5）
- #19: instruction retention（已在 limitations 声明为 exploratory）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_placeholder_audit_20260523T144109"
}
```

</details>

---
