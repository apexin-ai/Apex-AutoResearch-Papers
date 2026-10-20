# research citation audit 1

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 303
- **Recorded user turns:** 0
- **Tool calls:** 151
- **Original source:** `logs/chats/worker_research_citation-audit-1_20260526T101436.jsonl`
- **Structured JSON:** [`ae637dbf6ea90fcedd00.json`](../../sessions/ae/ae637dbf6ea90fcedd00.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

303 recorded events

### Tool call

_source line 1 · 2026-05-26T10:24:49.843171+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-26T10:24:49.843760+00:00_

1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{hong2025rhea,
14	  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15	  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16	  journal = {arXiv preprint arXiv:2512.06869},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2512.06869}
19	}
20	
21	@article{laban2025lost,
22	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2505.06120},
25	  year    = {2025},
26	  url     = {https://arxiv.org/abs/2505.06120}
27	}
28	
29	@article{liu2026intent,
30	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32	  journal = {arXiv preprint arXiv:2602.07338},
33	  year    = {2026},
34	  url     = {https://arxiv.org/abs/2602.07338}
35	}
36	
37	@inproceedings{bai2024mtbench101,
38	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40	  booktitle = {Annual Meeting of the Ass
…[truncated 25029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:24:49.843979+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[tp]?\\{|\\\\citealp\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections",
  "output_mode": "content",
  "-n": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[tp]?\\{|\\\\citealp\\{",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections",
    "output_mode": "content",
    "-n": "True"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-26T10:24:49.844148+00:00_

docs/paper/sections/analysis.tex:14:[Omitted long matching line]
docs/paper/sections/analysis.tex:18:[Omitted long matching line]
docs/paper/sections/analysis.tex:24:[Omitted long matching line]
docs/paper/sections/analysis.tex:39:[Omitted long matching line]
docs/paper/sections/related_work.tex:4:[Omitted long matching line]
docs/paper/sections/related_work.tex:7:[Omitted long matching line]
docs/paper/sections/related_work.tex:10:[Omitted long matching line]
docs/paper/sections/related_work.tex:15:[Omitted long matching line]
docs/paper/sections/method.tex:6:[Omitted long matching line]
docs/paper/sections/method.tex:28:[Omitted long matching line]
docs/paper/sections/method.tex:32:[Omitted long matching line]
docs/paper/sections/method.tex:59:We design a five-way comparison where each adjacent pair isolates one factor: \textbf{ThreadGate (TG) vs.\ Uniform Gate (UG)} (turn conditioning), \textbf{TG vs.\ LoRA-only} (gating mechanism), \textbf{ThreadGate vs.\ +PCGrad} (gradient conflict via gradient surgery \citep{yu2020pcgrad}), and \textbf{Fine-tuned vs.\ Base} (LoRA adaptation). All fine-tuned variants share training data, LoRA configuration, optimizer, and seed (Appendix~\ref{sec:appendix-hyper}).
docs/paper/sections/experiments.tex:6:[Omitted long matching line]
docs/paper/sections/experiments.tex:38:[Omitted long matching line]
docs/paper/sections/limitations.tex:3:[Omitted long matching line]
docs/paper/sections/discussion.tex:3:[Omitted long matching line]
docs/paper/sections/introduction.tex:3:[Omitted long matching line]
docs/paper/sections/introduction.tex:5:[Omitted long matching line]
docs/paper/sections/introduction.tex:7:[Omitted long matching line]
docs/paper/sections/appendix.tex:374:Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
docs/paper/sections/appendix.tex:472:[Omitted long matching line]
docs/paper/sections/appendix.tex:476:\caption{Training and evaluation data
…[truncated 396 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:24:49.844333+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}|\\\\citealp\\{[^}]+\\}' docs/paper/sections/*.tex | sort",
  "description": "Extract all citation keys from tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}|\\\\citealp\\{[^}]+\\}' docs/paper/sections/*.tex | sort",
    "description": "Extract all citation keys from tex files"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-26T10:24:49.844532+00:00_

docs/paper/sections/analysis.tex:\citep{bengio2015scheduled,zhang2019bridging,arora2022exposure}
docs/paper/sections/analysis.tex:\citep{dong2021attention}
docs/paper/sections/analysis.tex:\citep{grattafiori2024llama3}
docs/paper/sections/analysis.tex:\citep{yu2020pcgrad}
docs/paper/sections/appendix.tex:\citep{ding2023ultrachat}
docs/paper/sections/appendix.tex:\citep{ding2023ultrachat}
docs/paper/sections/appendix.tex:\citep{hendrycks2021measuring}
docs/paper/sections/appendix.tex:\citet{bengio2015scheduled}
docs/paper/sections/appendix.tex:\citet{dongre2026attention}
docs/paper/sections/discussion.tex:\citealp{chen2018gradnorm}
docs/paper/sections/discussion.tex:\citep{he2019exposure}
docs/paper/sections/discussion.tex:\citep{li2024measuring,hong2025rhea}
docs/paper/sections/discussion.tex:\citet{dou2019attention,dou2022parallel}
docs/paper/sections/experiments.tex:\citealp{bengio2015scheduled}
docs/paper/sections/experiments.tex:\citep{ding2023ultrachat}
docs/paper/sections/experiments.tex:\citep{dongre2026attention}
docs/paper/sections/experiments.tex:\citep{hu2022lora,dettmers2023qlora}
docs/paper/sections/introduction.tex:\citep{bengio2015scheduled,lamb2016professor}
docs/paper/sections/introduction.tex:\citep{li2024measuring}
docs/paper/sections/introduction.tex:\citep{qiu2025gated}
docs/paper/sections/introduction.tex:\citep{xiao2024streaming}
docs/paper/sections/introduction.tex:\citep{yu2020pcgrad}
docs/paper/sections/introduction.tex:\citet{dongre2026attention}
docs/paper/sections/limitations.tex:\citep{hendrycks2021measuring,lin2022truthfulqa}
docs/paper/sections/method.tex:\citep{bachlechner2021rezero}
docs/paper/sections/method.tex:\citep{gromov2024unreasonable}
docs/paper/sections/method.tex:\citep{veit2016residual}
docs/paper/sections/method.tex:\citep{yu2020pcgrad}
docs/paper/sections/method.tex:\citet{dongre2026attention}
docs/paper/sections/related_work.tex:\citealp{zhang2019bridging}
docs/paper/sections/related_work.tex:\citealp{zhang2024tell}
d
…[truncated 1849 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-26T10:24:49.844724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T10:24:49.844878+00:00_

1	\section{Introduction}\label{sec:introduction}
2	
3	Multi-turn dialogue is central to how large language models are deployed, from customer service to tutoring to long-form reasoning. Yet a persistent failure accompanies even the most fluent generation: as conversations grow longer, models pay progressively less attention to the system-prompt goals that define their task. \citet{dongre2026attention} measured significant Goal Accessibility Ratio (GAR) decline across 12 models over extended conversations; in our own evaluation, goal attention drops by over 70\% within just five turns. Crucially, this is not a representation problem: residual stream probes confirm that goal information persists (AUC\,=\,0.98). The model retains the knowledge of what it should attend to; it simply stops attending.
4	
5	Existing remedies address this decay at inference time. Split-softmax \citep{li2024measuring} separates instruction from conversation tokens; StreamingLLM \citep{xiao2024streaming} retains anchor tokens; Gated Attention \citep{qiu2025gated} applies per-head sigmoid gates within a single forward pass. A natural alternative is to intervene during training: optimize goal attention directly through auxiliary losses trained alongside next-token prediction (NTP). Yet this strategy rests on an untested assumption: attention patterns learned under teacher forcing (TF) transfer to autoregressive (AR) generation. Classical exposure bias research \citep{bengio2015scheduled,lamb2016professor} has shown that TF creates a training--inference distribution mismatch for RNN sequence models, but whether this mismatch extends to auxiliary attention objectives in multi-turn transformers remains unknown.
6	
7	We test this assumption and find it fails. We introduce a controlled five-way testbed (ThreadGate, +PCGrad \citep{yu2020pcgrad}, Uniform Gate, LoRA-only, and Base) designed not as competing solutions but as a diagnostic exclusion chain (\S\ref{sec:comparison-design}), where each adjace
…[truncated 2674 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-26T10:24:49.845027+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-26T10:24:49.845183+00:00_

1	\section{Related Work}\label{sec:related}
2	
3	\paragraph{Multi-turn dialogue and attention decay.}
4	Multi-turn coherence has been a persistent challenge from early dialogue systems \citep{li2016persona,roller2021recipes,zhang2020dialogpt} through modern long-context models \citep{xu2022goldfish}, with benchmarks such as MT-Bench \citep{zheng2024judging} and MT-Bench-101 \citep{bai2024mtbench101} continuing to expose quality gaps at later turns \citep{laban2025lost,liu2026intent}. Most relevant to our work, \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) and showed that attention to goal tokens decays 27--48\% across 12 models while residual probes retain goal information (AUC\,=\,0.98). We observe a steeper 70.8\% decline on Qwen-2.5-7B. \citet{li2024measuring} independently quantified instruction instability and proposed split-softmax as an inference-time remedy. Our work differs in scope: we diagnose \emph{why} training-time attention optimization fails to transfer to inference, and provide the first training-time mitigation.
5	
6	\paragraph{Gating and attention manipulation.}
7	Residual gating spans highway networks \citep{srivastava2015highway}, ReZero \citep{bachlechner2021rezero}, layer pruning \citep{gromov2024unreasonable,fan2020layerdrop}, and adaptive depth \citep{schuster2022calm,raposo2024mixture}. Most relevant is Gated Attention \citep{qiu2025gated}: per-head sigmoid gates achieving MMLU \citep{hendrycks2021measuring} $+$2.03 at 15B scale; ThreadGate differs in conditioning on turn position. On the analysis side, head specialization \citep{clark2019what,voita2019analyzing,kovaleva2019revealing}, positional bias calibration \citep{liu2024lost,xiao2024streaming}, and attention steering (PASTA; \citealp{zhang2024tell}) address inference behavior; our $\beta$-steering serves a diagnostic role. PCGrad \citep{yu2020pcgrad} and CAGrad \citep{liu2021cagrad} treat gradient conflict as the root cause; we show direction conflict is a sy
…[truncated 3059 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-26T10:24:49.845328+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-26T10:24:49.845538+00:00_

1	\section{Method}\label{sec:method}
2	
3	\subsection{Preliminaries}\label{sec:background}
4	
5	\paragraph{Goal Accessibility Ratio.}
6	Standard metrics such as perplexity and attention entropy capture generation quality but not \emph{what} the model attends to. In multi-turn dialogue, a model may generate fluent text while progressively ignoring task specifications in the system prompt. We need a metric that directly measures whether goal-relevant context receives attention. To formalize this, we denote the task specification tokens in the system prompt as \emph{goal tokens} $\mathcal{G}$. \citet{dongre2026attention} defined the Goal Accessibility Ratio (GAR) for a model with $L$ layers and $H$ heads at turn $\tau$ as
7	\begin{equation}\label{eq:gar}
8	  \text{GAR}(\tau) = \frac{1}{L \cdot H \cdot |\mathcal{R}_\tau|} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{i \in \mathcal{R}_\tau} \sum_{j \in \mathcal{G}} A_{i,j}^{(\ell,h)},
9	\end{equation}
10	where $\mathcal{R}_\tau$ is the set of response tokens at turn $\tau$ and $A_{i,j}^{(\ell,h)}$ is the attention weight from token $i$ to token $j$ at layer $\ell$, head $h$.
11	
12	\paragraph{Two GAR variants.}
13	\textbf{GAR-Dongre} is the original definition (Eq.~\ref{eq:gar}), averaging over all response tokens. However, averaging dilutes the signal with intermediate positions that may legitimately attend to local context rather than the system prompt. The last token of each assistant turn is where the model aggregates information for the next continuation; attention at this position most directly reflects the model's awareness of task specifications. \textbf{GAR-ours} restricts the measurement accordingly:
14	\begin{equation}\label{eq:gar-ours}
15	  \text{GAR\text{-}ours}(\tau) = \frac{1}{L \cdot H} \sum_{\ell=1}^{L} \sum_{h=1}^{H} \sum_{j \in \mathcal{G}} A_{t_\tau,\, j}^{(\ell,h)},
16	\end{equation}
17	where $t_\tau$ is the last token index at turn $\tau$. Attention at this position reflects the information drawn upon fo
…[truncated 6289 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-26T10:24:49.845695+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-26T10:24:49.845860+00:00_

1	\section{Analysis}\label{sec:analysis}
2	
3	\begin{figure*}[!t]
4	  \centering
5	  \includegraphics[width=\textwidth]{fig3_gate_shift.pdf}
6	  \caption{(a)~Gate turn conditioning: per-layer gate values at turn~1 vs turn~21. In 27/28 layers, gates approach 1.0 at late turns, inverting the design intent ($p = 3.73 \times 10^{-8}$). (b)~Distribution shift ($N$\,=\,5 pilot): the TF-AR GAR gap persists across all five variants. Pilot gaps (20--34$\times$) exceed final $N$\,=\,50 estimates (8--17$\times$; Table~\ref{tab:five-way}) due to smaller sample size.}
7	  \label{fig:gate-shift}
8	\end{figure*}
9	
10	Each subsection kills one alternative hypothesis via diagnostic exclusion: \S\ref{subsec:gate-conditioning}~turn conditioning, \S\ref{subsec:pcgrad}~gradient direction conflict, leaving exposure bias as the primary remaining explanation consistent with current evidence (\S\ref{subsec:dist-shift}). \S\ref{subsec:mechanism-specificity} confirms selectivity; \S\ref{subsec:cross-model} confirms cross-architecture generalization.
11	
12	\subsection{Gate Turn Conditioning}\label{subsec:gate-conditioning}
13	
14	We compare gate values at turn~1 (early) and turn~21 (late) across all 28 layers. The gates invert the design intent: in 27/28 layers, gate values are \emph{lower} at turn~1 than turn~21 (Wilcoxon $p = 3.73 \times 10^{-8}$, $r = 0.975$); e.g., layer~23 shifts from 0.769 to 0.979. NTP pressure pushes gates toward 1.0, a convergence pattern reminiscent of attention collapse in deep transformers \citep{dong2021attention}, yielding inference-time values of 0.93--0.98 (2--7\% attenuation; Table~\ref{tab:five-way}; full gate profiles in Appendix~\ref{sec:appendix-gate-profile}; training dynamics in Appendix~\ref{sec:appendix-training-ext}). The Uniform Gate learns comparable per-layer variation (L3\,=\,0.777, L27\,=\,1.000) despite lacking turn conditioning; the structure thus arises from LoRA$+$GAR pressure (Figure~\ref{fig:gate-shift}a). Does the NTP-GAR gradient confli
…[truncated 4896 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-26T10:24:49.846021+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-26T10:24:49.846182+00:00_

1	\section{Discussion}\label{sec:discussion}
2	
3	\looseness=-1 Our diagnostic exclusion identifies exposure bias as a primary factor in the TF-AR gap but cannot fully rule out KV cache drift (\S\ref{sec:limitations}); PCGrad rules out gradient direction conflict but not magnitude imbalance (7.5--25.7$\times$ NTP dominance; \citealp{chen2018gradnorm}). Despite weak downstream correlation ($r^2$\,=\,0.04), GAR retains diagnostic value by quantifying attention reallocation---a category-dependent effect (+23.8\,pp for content constraints under $\beta$\,=\,3, no change for format/positional). More broadly, the collapse should generalize to any auxiliary objective targeting distributional properties rather than prediction itself \citep{he2019exposure}. Our $\beta$-steering is a \emph{diagnostic}, complementary to inference-time remedies \citep{li2024measuring,hong2025rhea}. These findings resonate with \citet{dou2019attention,dou2022parallel}, who independently observed TF-to-AR attention degradation in NMT. SS's benefit may partly reflect a curriculum effect, though consistent gap compression across seeds and architectures supports the exposure bias interpretation.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-26T10:24:49.846312+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-26T10:24:49.846498+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Setup}
5	
6	We fine-tune Qwen-2.5-7B-Instruct with LoRA \citep{hu2022lora,dettmers2023qlora} on 8K multi-turn conversations from the UltraChat \citep{ding2023ultrachat} training split. Training uses 3 epochs with AdamW (lr $= 2 \times 10^{-4}$, batch size 1, gradient accumulation 8, seed 42; ThreadGate additionally with seed 123); each variant requires approximately 6 hours on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (96\,GB; training costs in Appendix~\ref{sec:appendix-cost}). Full hyperparameters are in Appendix~\ref{sec:appendix-hyper}; dataset statistics in Appendices~\ref{sec:appendix-data} and~\ref{sec:appendix-dataset-ext}; the controlled comparison design is described in \S\ref{sec:comparison-design}. We evaluate under \emph{IID} (same-distribution UltraChat text) and \emph{held-out} (50 non-overlapping conversations) teacher-forced protocols, reporting GAR-ours, GAR-Dongre \citep{dongre2026attention}, and perplexity (PPL).
7	
8	\subsection{Main Results}
9	
10	Table~\ref{tab:five-way} presents the five-way comparison. Under TF evaluation, all fine-tuned variants converge: GAR-ours spans 0.49--0.51 ($\leq$2\,pp), PPL is 2.78 for all. IID and held-out protocols produce identical rankings (held-out GAR-ours differs by $\leq$1\,pp), ruling out data overlap as a confound. GAR-Dongre remains low (0.01--0.02) with no TF-AR gap, indicating that only concentrated last-token attention is vulnerable to distribution shift; scheduled sampling breaks this pattern (\S\ref{subsec:ss}).
11	
12	Under AR generation ($N$\,=\,50), GAR-ours drops to 0.019--0.064, an 8--17$\times$ gap (Figure~\ref{fig:headline}). The ordering (ThreadGate 0.064 $>$ LoRA-only 0.037 $>$ Uniform Gate 0.033 $>$ PCGrad 0.030 $>$ Base 0.019) shows ThreadGate vs.\ LoRA-only is significant ($p$\,=\,0.004; Appendices~\ref{sec:appendix-stats} and~\ref{sec:appendix-stats-ext}), yet the gap remains 7.8$\times$. A second seed co
…[truncated 4119 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-26T10:24:49.846663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-26T10:24:49.846789+00:00_

1	\section*{Limitations}\label{sec:limitations}
2	
3	Our findings are demonstrated on two model families (Qwen-2.5-7B and Llama-3.1-8B) and a single dataset (UltraChat, 8K conversations). Although UltraChat spans 18 dialogue categories providing reasonable domain diversity, cross-dataset validation (e.g., ShareGPT, LMSYS-Chat) remains future work; generalization to other architectures and domains (e.g., code, reasoning) is likewise untested. All experiments use LoRA (rank 16); full fine-tuning may exhibit different sensitivity to the TF-AR gap, and the LoRA capacity constraint could confound the capacity exclusion step (LoRA-only vs.\ Base comparison in \S\ref{sec:comparison-design}). Most configurations use a single seed (scheduled sampling validated on three seeds; \S\ref{subsec:ss}), and quality assessment relies on PPL rather than comprehensive benchmarks \citep{hendrycks2021measuring,lin2022truthfulqa}. Our diagnostic exclusion identifies exposure bias as a primary factor but does not rule out KV cache drift as a contributing mechanism.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-26T10:24:49.846913+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-26T10:24:49.847025+00:00_

File content (26375 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-26T10:24:49.847161+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": "370",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
    "offset": "370",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-26T10:24:49.847298+00:00_

370	\paragraph{Cross-model comparison.} See \S\ref{sec:appendix-viz} for the full cross-model gate profile comparison (Figure~\ref{fig:gate-crossmodel}). Llama-3.1-8B shows a qualitatively different profile---a V-shaped valley at mid-to-late layers rather than early-layer dips---suggesting architecture-dependent layer importance hierarchies.
371	
372	\section{Scheduled Sampling Implementation}\label{sec:appendix-ss}
373	
374	Our scheduled sampling implementation follows \citet{bengio2015scheduled} with modifications for multi-turn transformer training:
375	
376	\paragraph{Sampling schedule.} The model-generated context ratio $\rho$ increases linearly from 0 to 0.3 over 3 epochs. At each training step, a Bernoulli trial with probability $\rho$ determines whether the input prefix is replaced with model-generated tokens. The effective usage rate (29.7--37.1\%) is lower than the nominal schedule due to per-sample Bernoulli variance.
377	
378	\paragraph{Context generation.} When model-generated context is selected, the model autoregressively generates the assistant turns from the conversation prefix up to the current training position. The generated tokens replace the ground-truth assistant tokens in the input, while user turns remain unchanged. This preserves the multi-turn structure while introducing distributional diversity in the conditioning context.
379	
380	\paragraph{Training dynamics.} The scheduled sampling variant converges to similar final loss (NTP 0.932 vs.\ 0.930 for standard ThreadGate) but with higher variance in early epochs due to the stochastic context mixing (Figure~\ref{fig:ss-dynamics}). Gate profiles remain similar (mean 0.953 vs.\ 0.947, min at L4 vs.\ L1), indicating that scheduled sampling does not fundamentally alter gate optimization but rather improves the robustness of the learned attention patterns to distributional shift. Training time increases by 8--80\% across seeds (seed-dependent; dominated by GAR forward pass overhead): 6.5h (seed 4
…[truncated 271 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-26T10:24:49.847477+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": "468",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
    "offset": "468",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-26T10:24:49.847617+00:00_

468	\end{figure*}
469	
470	\section{Training Data Characteristics}\label{sec:appendix-data}
471	
472	All experiments use 8,000 multi-turn conversations sampled from the UltraChat \citep{ding2023ultrachat} training split. Table~\ref{tab:data-stats} summarizes the dataset characteristics. Conversations are truncated to 2,048 tokens; conversations shorter than 3 user turns are excluded to ensure sufficient multi-turn structure for GAR computation. The held-out evaluation sets use separate non-overlapping samples: $N$\,=\,50 conversations (mean 3.6 user turns) for the primary AR evaluation and $N$\,=\,5 conversations (10 turns each) for the long-conversation analysis (Appendix~\ref{sec:appendix-n5}).
473	
474	\begin{table}[t]
475	\centering\small
476	\caption{Training and evaluation data characteristics. All data from UltraChat \citep{ding2023ultrachat}.}
477	\label{tab:data-stats}
478	\begin{tabular}{lcc}
479	\toprule
480	\textbf{Property} & \textbf{Train} & \textbf{Eval (primary)} \\
481	\midrule
482	Conversations & 8,000 & 50 \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-26T10:24:49.847747+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": "575",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
    "offset": "575",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-26T10:24:49.847877+00:00_

575	ThreadGate improvements are query-position-specific: the two definitions using the last token as query (ours: $0.015 \to 0.325$; goal-only: $0.005 \to 0.310$) show large gains, while all-token ($0.025$) and first-token ($0.039$) remain near base levels. This is expected: the GAR loss optimizes attention at the last-token position, so the learned routing does not generalize to other query positions.
576	
577	Scheduled Sampling raises all four definitions above 0.36, with no definition falling below Base-relative gains. This confirms that SS builds a broad goal-attention pattern across token positions, rather than overfitting to the specific position targeted by the GAR loss. The pattern holds regardless of GAR definition: both the exposure bias diagnosis and the SS mitigation are robust to metric choice.
578	
579	\section{General Capability Preservation (MMLU)}\label{sec:appendix-mmlu}
580	
581	To confirm that auxiliary GAR losses and attention steering do not degrade general language understanding, we evaluate all six Qwen-2.5-7B variants on MMLU 5-shot \citep{hendrycks2021measuring} ($N$\,=\,14{,}042 questions).
582	
583	\begin{table}[t]
584	\centering\small
585	\caption{MMLU 5-shot accuracy on Qwen-2.5-7B-Instruct. All fine-tuned variants remain within 0.8\,pp of the base LoRA-only checkpoint.}
586	\label{tab:mmlu}
587	\begin{tabular}{lcc}
588	\toprule
589	\textbf{Model} & \textbf{Acc (\%)} & \textbf{$\Delta$ vs Base} \\

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-26T10:24:49.848001+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
  "offset": "685",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/docs/paper/sections/appendix.tex",
    "offset": "685",
    "limit": "15"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-26T10:24:49.848135+00:00_

685	\paragraph{Domain diversity.} UltraChat covers a broad range of conversational topics including knowledge Q\&A, creative writing, reasoning, and open-ended discussion. We do not stratify by topic, as our focus is on the architectural mechanism (attention routing) rather than domain-specific performance. The topic diversity serves as implicit regularization against overfitting to specific conversation patterns.
686	
687	\input{../artifacts/appendix_expansion/tab_dataset_stats.tex}
688	
689	\section{Extended GAR Robustness Analysis}\label{sec:appendix-gar-ext}
690	
691	Table~\ref{tab:gar_robustness} and Figure~\ref{fig:gar-robust-grouped} extend the GAR robustness analysis from \S\ref{sec:appendix-gar-robust} with turn-1 GAR and gap ratio metrics across all four token-position variants. We evaluate four ways to select the query token position for gradient attribution: (1)~\textit{Last} (our default): the final token of each assistant turn, which captures the model's ``summary'' attention pattern at the prediction boundary; (2)~\textit{All}: the mean over all assistant tokens, providing a position-averaged view; (3)~\textit{First}: the first assistant token, which reflects initial attention allocation; (4)~\textit{Goal-only}: attention to goal tokens as defined by \citet{dongre2026attention}, which restricts the target set to system-prompt tokens.
692	
693	\paragraph{Position-specific vs.\ broad improvement.} The key finding is a clear dichotomy between ThreadGate and Scheduled Sampling. ThreadGate improvements are restricted to last-token and goal-only positions (the two definitions sharing the query position targeted by the GAR loss): gap ratios drop to 1.21$\times$ and 1.07$\times$ respectively. All-token (5.04$\times$) and first-token (8.24$\times$) GAR remain near base levels, confirming that the learned routing is position-specific. Scheduled Sampling raises all four definitions above 0.36 with gap ratios $\leq$1.83$\times$, demonstrating that distributional 
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-26T10:24:49.848320+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-26T10:24:49.848463+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-26T10:24:49.848630+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify citations group 1",
  "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **dongre2026attention**: Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-Tür, Dilek. \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\". arXiv:2605.12922, 2026.\n\n2. **hong2025rhea**: Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng. \"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs\". arXiv:2512.06869, 2025.\n\n3. **laban2025lost**: Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer. \"LLMs Get Lost In Multi-Turn Conversation\". arXiv:2505.06120, 2025.\n\n4. **liu2026intent**: Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng. \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\". arXiv:2602.07338, 2026.\n\n5. **bai2024mtbench101**: Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli. \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\". ACL 2024. arXiv:2402.14762.\n\n6. **li2024measuring**: Li, Kenneth and Liu, Tianle and Bashkansky, Naomi and Bau, David and Viégas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin. \"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\". COLM 2024. arXiv:2402.10962.\n\n7. **xiao2024streaming**: Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike. \"Efficient Streaming Language Models with Attention Sinks\". ICLR 2024. arXiv:2309.17453.\n\n8. **zhang2024tell**: Zhang, Qingru and Singh, Chandan and Liu, Liyuan and Liu, Xiaodong and Yu, Bin and Gao, Jianfeng and Zhao, Tuo. \"Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs\". ICLR 2024. arXiv:2311.02262.\n\n9. **hsieh2024found**: Hsieh, Cheng-Yu and Chuang, Yung-Sung and Li, Chun-Liang and Wang, Zifeng and Le, Long and Kumar, Abhishek and Glass, James and Ratner, Alexander and Lee, Chen-Yu and Krishna, Ranjay and Pfister, Tomas. \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\". Findings of ACL 2024. arXiv:2406.16008.\n\n10. **qiu2025gated**: Qiu, Zihan and Wang, Zekun and Zheng, Bo and Huang, Zeyu and Wen, Kaiyue and Yang, Songlin and Men, Rui and Yu, Le and Huang, Fei and Huang, Suozhi and Liu, Dayiheng and Zhou, Jingren and Lin, Junyang. \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\". NeurIPS 2025. arXiv:2505.06708.\n\nSearch each one individually using WebSearch. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify citations group 1",
    "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **dongre2026attention**: Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-Tür, Dilek. \"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\". arXiv:2605.12922, 2026.\n\n2. **hong2025rhea**: Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng. \"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs\". arXiv:2512.06869, 2025.\n\n3. **laban2025lost**: Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer. \"LLMs Get Lost In Multi-Turn Conversation\". arXiv:2505.06120, 2025.\n\n4. **liu2026intent**: Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng. \"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\". arXiv:2602.07338, 2026.\n\n5. **bai2024mtbench101**: Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli. \"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\". ACL 2024. arXiv:2402.14762.\n\n6. **li2024measuring**: Li, Kenneth and Liu, Tianle and Bashkansky, Naomi and Bau, David and Viégas, Fernanda and Pfister, Hanspeter and Wattenberg, Martin. \"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\". COLM 2024. arXiv:2402.10962.\n\n7. **xiao2024streaming**: Xiao, Guangxuan and Tian, Yuandong and Chen, Beidi and Han, Song and Lewis, Mike. \"Efficient Streaming Language Models with Attention Sinks\". ICLR 2024. arXiv:2309.17453.\n\n8. **zhang2024tell**: Zhang, Qingru and Singh, Chandan and Liu, Liyuan and Liu, Xiaodong and Yu, Bin and Gao, Jianfeng and Zhao, Tuo. \"Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs\". ICLR 2024. arXiv:2311.02262.\n\n9. **hsieh2024found**: Hsieh, Cheng-Yu and Chuang, Yung-Sung and Li, Chun-Liang and Wang, Zifeng and Le, Long and Kumar, Abhishek and Glass, James and Ratner, Alexander and Lee, Chen-Yu and Krishna, Ranjay and Pfister, Tomas. \"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization\". Findings of ACL 2024. arXiv:2406.16008.\n\n10. **qiu2025gated**: Qiu, Zihan and Wang, Zekun and Zheng, Bo and Huang, Zeyu and Wen, Kaiyue and Yang, Songlin and Men, Rui and Yu, Le and Huang, Fei and Huang, Suozhi and Liu, Dayiheng and Zhou, Jingren and Lin, Junyang. \"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\". NeurIPS 2025. arXiv:2505.06708.\n\nSearch each one individually using WebSearch. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-26T10:24:49.848870+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-26T10:24:49.848998+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-26T10:24:49.849116+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2605.12922 Dongre \"When Attention Closes\" multi-turn interaction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2605.12922 Dongre \"When Attention Closes\" multi-turn interaction 2026"
  }
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-26T10:24:49.849233+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2512.06869 Hong \"Rhea Role-aware Heuristic Episodic Attention\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2512.06869 Hong \"Rhea Role-aware Heuristic Episodic Attention\" 2025"
  }
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-26T10:24:49.849346+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.06120 Laban \"LLMs Get Lost In Multi-Turn Conversation\" 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.06120 Laban \"LLMs Get Lost In Multi-Turn Conversation\" 2025"
  }
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-26T10:24:49.849477+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2602.07338 Liu \"Intent Mismatch Causes LLMs to Get Lost\" 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2602.07338 Liu \"Intent Mismatch Causes LLMs to Get Lost\" 2026"
  }
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-26T10:24:49.849591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2402.14762 Bai \"MT-Bench-101 Fine-Grained Benchmark\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2402.14762 Bai \"MT-Bench-101 Fine-Grained Benchmark\" ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-26T10:24:49.849712+00:00_

Web search results for query: "arXiv 2512.06869 Hong "Rhea Role-aware Heuristic Episodic Attention" 2025"

Links: [{"title":"[2512.06869] Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/abs/2512.06869"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.arxiv.org/pdf/2512.06869"},{"title":"(PDF) Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.researchgate.net/publication/398476529_Rhea_Role-aware_Heuristic_Episodic_Attention_for_Conversational_LLMs"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/html/2512.06869"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v1"}]

I found the arXiv paper you're looking for. Here are the details:

**Title:** Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs

**arXiv ID:** 2512.06869

**Date:** December 7, 2025

**Main Focus:** The paper addresses how Large Language Models (LLMs) have achieved remarkable performance on single-turn tasks, yet their effectiveness deteriorates in multi-turn conversations.

**Proposed Solution:** The authors propose Rhea, a novel framework that decouples conversation history into two functionally independent memory modules: (1) an Instructional Memory (IM) that persistently stores high-fidelity global constraints via a structural priority mechanism, and (2) an Episodic Memory (EM) that dynamically manages user-model interactions via asymmetric noise control and heuristic context retrieval.

**Key Problem Addressed:** The paper defines a phenomenon called cumulative contextual decay - a progressive degradation of contextual integrity caused by attention pollution, dilution, and drift.

The full paper is available on arXiv at https://arxiv.org/abs/2512.06869.


REMINDER: You MUST include the sources above in your respons
…[truncated 40 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-26T10:24:49.849862+00:00_

Web search results for query: "arXiv 2602.07338 Liu "Intent Mismatch Causes LLMs to Get Lost" 2026"

Links: [{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260207338L/abstract"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://goatstack.ai/articles/2602.07338"},{"title":"(PDF) Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://www.researchgate.net/publication/400604289_Intent_Mismatch_Causes_LLMs_to_Get_Lost_in_Multi-Turn_Conversation"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation | alphaXiv","url":"https://www.alphaxiv.org/overview/2602.07338v1"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation - PULRC Portal","url":"https://lrc.perdanauniversity.edu.my/sdi/intent-mismatch-causes-llms-to-get-lost-in-multi-turn-conversation/"},{"title":"LLMS GET LOST IN MULTI-TURN CONVERSATION","url":"https://openreview.net/pdf?id=VKGTGGcwl6"}]

I found the paper you're looking for! Here are the key details:

**Paper Title:** Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

**Authors:** Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, and Gaofeng Meng from the College of Computing at City University of Hong Kong and the Centre for Artificial Intelligence and Robotics at HKISI, CAS

**ArXiv ID:** 2602.07338 (submitted February 7, 2026)

**Main Argument:** The authors argue that the root cause of the "Lost in Conversation" (LiC) phenomenon lies in an intent alignment gap rather than intrinsic capability deficits, demonstrating that LiC is not a failure of model capability but rather a breakdown
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-26T10:24:49.850016+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify citations group 2",
  "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **fan2020layerdrop**: Fan, Angela and Grave, Edouard and Joulin, Armand. \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\". ICLR 2020. arXiv:1909.11556.\n\n2. **raposo2024mixture**: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam. \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\". ICML 2024. arXiv:2404.02258.\n\n3. **schuster2022calm**: Schuster, Tal and Fisch, Adam and Gupta, Jai and Dehghani, Mostafa and Bahri, Dara and Tran, Vinh Q. and Tay, Yi and Metzler, Donald. \"Confident Adaptive Language Modeling\". NeurIPS 2022. arXiv:2207.07061.\n\n4. **luo2025flexidepth**: Luo, Xuan and Wang, Weizhi and Yan, Xifeng. \"Adaptive Layer-skipping in Pre-trained LLMs\". COLM 2025. arXiv:2503.23798.\n\n5. **bachlechner2021rezero**: Bachlechner, Thomas and Majumder, Bodhisattwa Prasad and Mao, Henry and Cottrell, Gary and McAuley, Julian. \"ReZero is All You Need: Fast Convergence at Large Depth\". UAI 2021. arXiv:2003.04887.\n\n6. **gromov2024unreasonable**: Gromov, Andrey and Tirumala, Kushal and Shapourian, Hassan and Glorioso, Paolo and Roberts, Daniel A. \"The Unreasonable Ineffectiveness of the Deeper Layers\". ICLR 2025. arXiv:2403.17887.\n\n7. **vaswani2017attention**: Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, Łukasz and Polosukhin, Illia. \"Attention Is All You Need\". NeurIPS 2017. arXiv:1706.03762.\n\n8. **he2016deep**: He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian. \"Deep Residual Learning for Image Recognition\". CVPR 2016. arXiv:1512.03385.\n\n9. **srivastava2015highway**: Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, Jürgen. \"Highway Networks\". ICML 2015 Deep Learning Workshop. arXiv:1505.00387.\n\n10. **hu2022lora**: Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu. \"LoRA: Low-Rank Adaptation of Large Language Models\". ICLR 2022. arXiv:2106.09685.\n\n11. **veit2016residual**: Veit, Andreas and Wilber, Michael and Belongie, Serge. \"Residual Networks Behave Like Ensembles of Relatively Shallow Networks\". NeurIPS 2016. arXiv:1605.06431.\n\nSearch each one individually using WebSearch. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify citations group 2",
    "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **fan2020layerdrop**: Fan, Angela and Grave, Edouard and Joulin, Armand. \"Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\". ICLR 2020. arXiv:1909.11556.\n\n2. **raposo2024mixture**: Raposo, David and Ritter, Sam and Richards, Blake and Lillicrap, Timothy and Humphreys, Peter Conway and Santoro, Adam. \"Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\". ICML 2024. arXiv:2404.02258.\n\n3. **schuster2022calm**: Schuster, Tal and Fisch, Adam and Gupta, Jai and Dehghani, Mostafa and Bahri, Dara and Tran, Vinh Q. and Tay, Yi and Metzler, Donald. \"Confident Adaptive Language Modeling\". NeurIPS 2022. arXiv:2207.07061.\n\n4. **luo2025flexidepth**: Luo, Xuan and Wang, Weizhi and Yan, Xifeng. \"Adaptive Layer-skipping in Pre-trained LLMs\". COLM 2025. arXiv:2503.23798.\n\n5. **bachlechner2021rezero**: Bachlechner, Thomas and Majumder, Bodhisattwa Prasad and Mao, Henry and Cottrell, Gary and McAuley, Julian. \"ReZero is All You Need: Fast Convergence at Large Depth\". UAI 2021. arXiv:2003.04887.\n\n6. **gromov2024unreasonable**: Gromov, Andrey and Tirumala, Kushal and Shapourian, Hassan and Glorioso, Paolo and Roberts, Daniel A. \"The Unreasonable Ineffectiveness of the Deeper Layers\". ICLR 2025. arXiv:2403.17887.\n\n7. **vaswani2017attention**: Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N. and Kaiser, Łukasz and Polosukhin, Illia. \"Attention Is All You Need\". NeurIPS 2017. arXiv:1706.03762.\n\n8. **he2016deep**: He, Kaiming and Zhang, Xiangyu and Ren, Shaoqing and Sun, Jian. \"Deep Residual Learning for Image Recognition\". CVPR 2016. arXiv:1512.03385.\n\n9. **srivastava2015highway**: Srivastava, Rupesh Kumar and Greff, Klaus and Schmidhuber, Jürgen. \"Highway Networks\". ICML 2015 Deep Learning Workshop. arXiv:1505.00387.\n\n10. **hu2022lora**: Hu, Edward J. and Shen, Yelong and Wallis, Phillip and Allen-Zhu, Zeyuan and Li, Yuanzhi and Wang, Shean and Wang, Lu and Chen, Weizhu. \"LoRA: Low-Rank Adaptation of Large Language Models\". ICLR 2022. arXiv:2106.09685.\n\n11. **veit2016residual**: Veit, Andreas and Wilber, Michael and Belongie, Serge. \"Residual Networks Behave Like Ensembles of Relatively Shallow Networks\". NeurIPS 2016. arXiv:1605.06431.\n\nSearch each one individually using WebSearch. Be thorough."
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-26T10:24:49.850299+00:00_

Web search results for query: "arXiv 2402.14762 Bai "MT-Bench-101 Fine-Grained Benchmark" ACL 2024"

Links: [{"title":"[2402.14762] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues","url":"https://arxiv.org/abs/2402.14762"},{"title":"GitHub - mtbench101/mt-bench-101: [ACL 2024] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues · GitHub","url":"https://github.com/mtbench101/mt-bench-101"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large","url":"https://arxiv.org/pdf/2402.14762"},{"title":"[PDF] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MT-Bench-101:-A-Fine-Grained-Benchmark-for-Large-in-Bai-Liu/9978f937189a279a726545a734d20558095e7a0a"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.401/"},{"title":"[2402.14762v3] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues","url":"https://arxiv.org/abs/2402.14762v3"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating ...","url":"https://aclanthology.org/2024.acl-long.401.pdf"},{"title":"[Literature Review] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues","url":"https://www.themoonlight.io/en/review/mt-bench-101-a-fine-grained-benchmark-for-evaluating-large-language-models-in-multi-turn-dialogues"}]

I found the paper you were searching for. Here are the results:

**MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues** is a paper by Ge Bai and co-authors, published at ACL 2024.

**Key Information:**
- arXiv ID: 2402.14762 (submitted February 22, 2024, last revised November 5, 2024)
- Published in the Pro
…[truncated 944 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-26T10:24:49.850490+00:00_

Web search results for query: "arXiv 2605.12922 Dongre "When Attention Closes" multi-turn interaction 2026"

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"[2605.02323v1] When Attention Collapses: Residual Evidence Modeling for Compositional Inference","url":"https://arxiv.org/abs/2605.02323v1"},{"title":"[2605.21422] Preference-aware Influence-function-based Data Selection Method for Efficient Fine-Tuning","url":"https://arxiv.org/abs/2605.21422"},{"title":"[2605.12920] Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue","url":"https://arxiv.org/abs/2605.12920"},{"title":"[2605.13784] Attention Once Is All You Need: Efficient Streaming Inference with Stateful Transformers","url":"https://arxiv.org/abs/2605.13784"},{"title":"[2605.21770] Manifold-Guided Attention Steering","url":"https://arxiv.org/abs/2605.21770"}]

I found the paper you're looking for! Here are the details:

**Title:** "When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction"

**arXiv ID:** 2605.12922

**Authors:** Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür

**Submission Date:** May 13, 2026

**Main Finding:** Large language models can follow complex instructions in a single turn, yet over long multi-turn interactions they often lose the thread of instructions, persona, and rules.

**Methodology:** The authors propose a channel-transition account where goal-defining tokens become less accessible through attention, while goal-related information may persist in residual representations. They introduce the Goal Accessibility Ratio (GAR), measuring attention from generated tokens to task-defining goal tokens, and combine it with sliding-window ablations and residual-stream probes.
…[truncated 397 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-26T10:24:49.850640+00:00_

Web search results for query: "arXiv 2505.06120 Laban "LLMs Get Lost In Multi-Turn Conversation" 2025"

Web search error: unavailable

I apologize, but I'm unable to complete the web search at this moment as the web search tool is currently unavailable. 

However, I can tell you that the arXiv identifier you're looking for (2505.06120) appears to be a paper from May 2025. If you'd like to access this paper, you can typically find arXiv papers directly by:

1. Visiting **arxiv.org** and searching for the paper ID: 2505.06120
2. Searching for the title "LLMs Get Lost In Multi-Turn Conversation" along with the author Laban
3. Checking academic research aggregators like Google Scholar

Would you like me to try searching again later, or is there something specific about this paper you'd like to know?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-26T10:24:49.850768+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.06120 Laban Hayashi \"LLMs Get Lost In Multi-Turn Conversation\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.06120 Laban Hayashi \"LLMs Get Lost In Multi-Turn Conversation\""
  }
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-26T10:24:49.850884+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-26T10:24:49.850995+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-26T10:24:49.851110+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fan Grave Joulin \"Reducing Transformer Depth on Demand with Structured Dropout\" LayerDrop ICLR 2020 arXiv:1909.11556"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fan Grave Joulin \"Reducing Transformer Depth on Demand with Structured Dropout\" LayerDrop ICLR 2020 arXiv:1909.11556"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-26T10:24:49.851239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Raposo Ritter Richards Lillicrap \"Mixture-of-Depths\" dynamically allocating compute transformer ICML 2024 arXiv:2404.02258"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Raposo Ritter Richards Lillicrap \"Mixture-of-Depths\" dynamically allocating compute transformer ICML 2024 arXiv:2404.02258"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-26T10:24:49.851437+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Schuster Fisch Gupta Dehghani \"Confident Adaptive Language Modeling\" NeurIPS 2022 arXiv:2207.07061"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Schuster Fisch Gupta Dehghani \"Confident Adaptive Language Modeling\" NeurIPS 2022 arXiv:2207.07061"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-26T10:24:49.851584+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Luo Wang Yan \"Adaptive Layer-skipping in Pre-trained LLMs\" FlexiDepth COLM 2025 arXiv:2503.23798"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Luo Wang Yan \"Adaptive Layer-skipping in Pre-trained LLMs\" FlexiDepth COLM 2025 arXiv:2503.23798"
  }
}
```

</details>

---

### Tool call

_source line 54 · 2026-05-26T10:24:49.851702+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bachlechner Majumder Mao Cottrell McAuley \"ReZero is All You Need\" fast convergence large depth UAI 2021 arXiv:2003.04887"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bachlechner Majumder Mao Cottrell McAuley \"ReZero is All You Need\" fast convergence large depth UAI 2021 arXiv:2003.04887"
  }
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-26T10:24:49.851816+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gromov Tirumala Shapourian Glorioso Roberts \"Unreasonable Ineffectiveness of the Deeper Layers\" ICLR 2025 arXiv:2403.17887"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gromov Tirumala Shapourian Glorioso Roberts \"Unreasonable Ineffectiveness of the Deeper Layers\" ICLR 2025 arXiv:2403.17887"
  }
}
```

</details>

---

### Tool call

_source line 56 · 2026-05-26T10:24:49.851926+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vaswani Shazeer Parmar Uszkoreit \"Attention Is All You Need\" NeurIPS 2017 arXiv:1706.03762"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vaswani Shazeer Parmar Uszkoreit \"Attention Is All You Need\" NeurIPS 2017 arXiv:1706.03762"
  }
}
```

</details>

---

### Tool call

_source line 57 · 2026-05-26T10:24:49.852036+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "He Zhang Ren Sun \"Deep Residual Learning for Image Recognition\" CVPR 2016 arXiv:1512.03385"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "He Zhang Ren Sun \"Deep Residual Learning for Image Recognition\" CVPR 2016 arXiv:1512.03385"
  }
}
```

</details>

---

### Tool call

_source line 58 · 2026-05-26T10:24:49.852143+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Srivastava Greff Schmidhuber \"Highway Networks\" ICML 2015 arXiv:1505.00387"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Srivastava Greff Schmidhuber \"Highway Networks\" ICML 2015 arXiv:1505.00387"
  }
}
```

</details>

---

### Tool call

_source line 59 · 2026-05-26T10:24:49.852251+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hu Shen Wallis Allen-Zhu Li Wang Chen \"LoRA Low-Rank Adaptation of Large Language Models\" ICLR 2022 arXiv:2106.09685"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hu Shen Wallis Allen-Zhu Li Wang Chen \"LoRA Low-Rank Adaptation of Large Language Models\" ICLR 2022 arXiv:2106.09685"
  }
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-26T10:24:49.852359+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Veit Wilber Belongie \"Residual Networks Behave Like Ensembles of Relatively Shallow Networks\" NeurIPS 2016 arXiv:1605.06431"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Veit Wilber Belongie \"Residual Networks Behave Like Ensembles of Relatively Shallow Networks\" NeurIPS 2016 arXiv:1605.06431"
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-26T10:24:49.852505+00:00_

Web search results for query: "Bachlechner Majumder Mao Cottrell McAuley "ReZero is All You Need" fast convergence large depth UAI 2021 arXiv:2003.04887"

Links: [{"title":"GitHub - majumderb/rezero: Official PyTorch Repo for \"ReZero is All You Need: Fast Convergence at Large Depth\" · GitHub","url":"https://github.com/majumderb/rezero"},{"title":"ReZero is all you need: fast convergence at large depth. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/11a06c41b4457c79df40f0d38bbce187f/dblp"},{"title":"ReZero is All You Need: Fast Convergence at Large Depth Thomas Bachlechner*1","url":"https://auai.org/uai2021/pdf/uai2021.519.preliminary.pdf"},{"title":"ReZero is all you need: fast convergence at large depth","url":"https://proceedings.mlr.press/v161/bachlechner21a.html"},{"title":"ReZero is All You Need: Fast Convergence at Large Depth Thomas Bachlechner1","url":"https://proceedings.mlr.press/v161/bachlechner21a/bachlechner21a.pdf"},{"title":"Underline | ReZero is All You Need: Fast Convergence at Large Depth","url":"https://underline.io/lecture/28903-rezero-is-all-you-need-fast-convergence-at-large-depth"},{"title":"ReZero is All You Need: Fast Convergence at Large Depth | Underline","url":"https://underline.io/lecture/28903-519-iv-f5-rezero-is-all-you-need-fast-convergence-at-large-depth"},{"title":"ReZero is All You Need: Fast Convergence at Large Depth","url":"https://arxiv.org/pdf/2003.04887"}]

Based on the web search results, I found the paper you're looking for:

"ReZero is All You Need: Fast Convergence at Large Depth" was published at the Uncertainty in AI (UAI) conference in 2021 by Thomas Bachlechner, Bodhisattwa Prasad Majumder, Huanru Henry Mao, Garrison W. Cottrell, and Julian McAuley.

The paper shows that gating each residual connection using a single zero-initialized parameter satisfies initial dynamical isometry and outperforms more complex approaches. The technique enables training 120-layer Transformers, and when applied to 12 layer Transfo
…[truncated 490 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-26T10:24:49.852667+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify citations group 3",
  "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **bengio2015scheduled**: Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam. \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\". NeurIPS 2015. arXiv:1506.03099.\n\n2. **ranzato2016sequence**: Ranzato, Marc'Aurelio and Chopra, Sumit and Auli, Michael and Zaremba, Wojciech. \"Sequence Level Training with Recurrent Neural Networks\". ICLR 2016. arXiv:1511.06732.\n\n3. **lamb2016professor**: Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville, Aaron and Bengio, Yoshua. \"Professor Forcing: A New Algorithm for Training Recurrent Networks\". NeurIPS 2016. arXiv:1610.09038.\n\n4. **leblond2018searnn**: Leblond, Rémi and Alayrac, Jean-Baptiste and Osokin, Anton and Lacoste-Julien, Simon. \"SEARNN: Training RNNs with Global-Local Losses\". ICLR 2018. arXiv:1706.04499.\n\n5. **he2019exposure**: He, Tianxing and Zhang, Jingzhao and Zhou, Zhiming and Glass, James. \"Quantifying Exposure Bias for Neural Language Generation\". arXiv:1905.10617, 2019.\n\n6. **wiseman2016sequence**: Wiseman, Sam and Rush, Alexander M. \"Sequence-to-Sequence Learning as Beam-Search Optimization\". EMNLP 2016. arXiv:1606.02960.\n\n7. **arora2022exposure**: Arora, Kushal and El Asri, Layla and Bahuleyan, Hareesh and Cheung, Jackie Chi Kit. \"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\". Findings of ACL 2022. arXiv:2204.01171.\n\n8. **zhang2019bridging**: Zhang, Wen and Feng, Yang and Meng, Fandong and You, Di and Liu, Qun. \"Bridging the Gap between Training and Inference for Neural Machine Translation\". ACL 2019. arXiv:1906.02448.\n\n9. **mihaylova2019scheduled**: Mihaylova, Tsvetomila and Martins, André F. T. \"Scheduled Sampling for Transformers\". ACL 2019 Student Research Workshop. pp. 351-356. URL: https://aclanthology.org/P19-2049/\n\n10. **dou2019attention**: Dou, Qingyun and Lu, Yiting and Efiong, Joshua and Gales, Mark J. F. \"Attention Forcing for Sequence-to-sequence Model Training\". arXiv:1909.12289, 2019.\n\n11. **dou2022parallel**: Dou, Qingyun and Gales, Mark J. F. \"Parallel Attention Forcing for Machine Translation\". arXiv:2211.03237, 2022.\n\nSearch each one individually using WebSearch. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify citations group 3",
    "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **bengio2015scheduled**: Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam. \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\". NeurIPS 2015. arXiv:1506.03099.\n\n2. **ranzato2016sequence**: Ranzato, Marc'Aurelio and Chopra, Sumit and Auli, Michael and Zaremba, Wojciech. \"Sequence Level Training with Recurrent Neural Networks\". ICLR 2016. arXiv:1511.06732.\n\n3. **lamb2016professor**: Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville, Aaron and Bengio, Yoshua. \"Professor Forcing: A New Algorithm for Training Recurrent Networks\". NeurIPS 2016. arXiv:1610.09038.\n\n4. **leblond2018searnn**: Leblond, Rémi and Alayrac, Jean-Baptiste and Osokin, Anton and Lacoste-Julien, Simon. \"SEARNN: Training RNNs with Global-Local Losses\". ICLR 2018. arXiv:1706.04499.\n\n5. **he2019exposure**: He, Tianxing and Zhang, Jingzhao and Zhou, Zhiming and Glass, James. \"Quantifying Exposure Bias for Neural Language Generation\". arXiv:1905.10617, 2019.\n\n6. **wiseman2016sequence**: Wiseman, Sam and Rush, Alexander M. \"Sequence-to-Sequence Learning as Beam-Search Optimization\". EMNLP 2016. arXiv:1606.02960.\n\n7. **arora2022exposure**: Arora, Kushal and El Asri, Layla and Bahuleyan, Hareesh and Cheung, Jackie Chi Kit. \"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\". Findings of ACL 2022. arXiv:2204.01171.\n\n8. **zhang2019bridging**: Zhang, Wen and Feng, Yang and Meng, Fandong and You, Di and Liu, Qun. \"Bridging the Gap between Training and Inference for Neural Machine Translation\". ACL 2019. arXiv:1906.02448.\n\n9. **mihaylova2019scheduled**: Mihaylova, Tsvetomila and Martins, André F. T. \"Scheduled Sampling for Transformers\". ACL 2019 Student Research Workshop. pp. 351-356. URL: https://aclanthology.org/P19-2049/\n\n10. **dou2019attention**: Dou, Qingyun and Lu, Yiting and Efiong, Joshua and Gales, Mark J. F. \"Attention Forcing for Sequence-to-sequence Model Training\". arXiv:1909.12289, 2019.\n\n11. **dou2022parallel**: Dou, Qingyun and Gales, Mark J. F. \"Parallel Attention Forcing for Machine Translation\". arXiv:2211.03237, 2022.\n\nSearch each one individually using WebSearch. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-26T10:24:49.852864+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2402.10962 Li \"Measuring and Controlling Instruction Instability\" COLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2402.10962 Li \"Measuring and Controlling Instruction Instability\" COLM 2024"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-26T10:24:49.853081+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2309.17453 Xiao \"Efficient Streaming Language Models with Attention Sinks\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2309.17453 Xiao \"Efficient Streaming Language Models with Attention Sinks\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 65 · 2026-05-26T10:24:49.853208+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2311.02262 Zhang \"Tell Your Model Where to Attend Post-hoc Attention Steering\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2311.02262 Zhang \"Tell Your Model Where to Attend Post-hoc Attention Steering\" ICLR 2024"
  }
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-26T10:24:49.853327+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2406.16008 Hsieh \"Found in the Middle Calibrating Positional Attention Bias\" ACL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2406.16008 Hsieh \"Found in the Middle Calibrating Positional Attention Bias\" ACL 2024"
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-26T10:24:49.853474+00:00_

Web search results for query: "arXiv 2505.06120 Laban Hayashi "LLMs Get Lost In Multi-Turn Conversation""

Links: [{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/pdf/2505.06120"},{"title":"[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120v1"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"},{"title":"GitHub - microsoft/lost_in_conversation: Code that accompanies the public release of the paper Lost in Conversation (https://arxiv.org/abs/2505.06120) · GitHub","url":"https://github.com/microsoft/lost_in_conversation"},{"title":"LLMs Get Lost In Multi-Turn Conversation - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.06120"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://lost-in-conversation.github.io/"},{"title":"(PDF) LLMs Get Lost In Multi-Turn Conversation","url":"https://www.researchgate.net/publication/391658658_LLMs_Get_Lost_In_Multi-Turn_Conversation"}]

I found the paper! Here's a summary of arXiv:2505.06120:

**Title:** "LLMs Get Lost In Multi-Turn Conversation"

**Authors:** Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville

**Submission Date:** Submitted on 9 May 2025

**Main Findings:**

Although LLM conversation logs show that underspecification occurs frequently in user instructions, LLM evaluation has predominantly focused on single-turn, fully-specified instruction settings. The work performs large-scale simulation experiments to compare LLM performance in single- and multi-turn settings.

The experiments confirm that all the top open- and closed-weight LLMs tested exhibit significantly lower performance in multi-turn conversations than single-turn, with an 
…[truncated 516 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-26T10:24:49.853637+00:00_

Web search results for query: "arXiv 2402.10962 Li "Measuring and Controlling Instruction Instability" COLM 2024"

Links: [{"title":"[2402.10962] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962"},{"title":"arXiv:2402.10962v4 [cs.CL] 25 Jul 2024","url":"https://arxiv.org/pdf/2402.10962"},{"title":"VCG Harvard | Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://vcg.seas.harvard.edu/publications/https-arxiv-org-pdf-2402-10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/html/2402.10962"},{"title":"Controlling Instruction Drift in LLM Dialogs","url":"https://api.emergentmind.com/papers/2402.10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/paperview/details/measuring-and-controlling-instruction-instability-in-language-model-dialogs-7499-1350985"},{"title":"Preprint Measuring and Controlling Instruction (In)Stability","url":"https://www.arxiv.org/pdf/2402.10962v3"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs (arXiv:2402.10962v4) - ScienceStack","url":"https://www.sciencestack.ai/paper/2402.10962"},{"title":"[2402.10962v4] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962v4"},{"title":"Artificial Intelligence Feb 2024","url":"https://web3.arxiv.org/list/cs.AI/2024-02?skip=1700&show=25"}]

I found the paper! Here are the key details:

**Paper Title:** Measuring and Controlling Instruction (In)Stability in Language Model Dialogs

**Authors:** Kenneth Li, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg

**Conference:** Published as a conference paper at COLM 2024

**arXiv ID:** 2402.10962

**Summary:** System
…[truncated 922 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 69 · 2026-05-26T10:24:49.853788+00:00_

Web search results for query: "arXiv 2311.02262 Zhang "Tell Your Model Where to Attend Post-hoc Attention Steering" ICLR 2024"

Links: [{"title":"[2311.02262] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/abs/2311.02262"},{"title":"Published as a conference paper at ICLR 2024 TELL YOUR MODEL WHERE TO ATTEND:","url":"https://arxiv.org/pdf/2311.02262"},{"title":"Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/html/2311.02262v2"},{"title":"Paper page - Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://huggingface.co/papers/2311.02262"},{"title":"[2311.02262v1] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/abs/2311.02262v1"},{"title":"[2311.02262v2] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs","url":"https://arxiv.org/abs/2311.02262v2"},{"title":"[PDF] Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Tell-Your-Model-Where-to-Attend:-Post-hoc-Attention-Zhang-Singh/881845a7ea41a0dd2411a41ea9ce9770cdc38c6a"},{"title":"GitHub - QingruZhang/PASTA: PASTA: Post-hoc Attention Steering for LLMs · GitHub","url":"https://github.com/QingruZhang/PASTA"},{"title":"Selected Recent Papers on Interpretable Machine Learning","url":"https://binyu.stat.berkeley.edu/papers/interpretable-machine-learning.html"}]

Great! I found the paper. Here are the key details about arXiv 2311.02262:

**Title:** Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs

**Authors:** Qingru Zhang, Chandan Singh, Liyuan Liu, Xiaodong Liu, Bin Yu, Jianfeng Gao, Tuo Zhao

**Publication:** Published as a conference paper at ICLR 2024

**Key Contribution:** The paper introduces PASTA -- Post-hoc Attention STeering Approach, a method that allows LLMs to read text with user-specified emphasis marks by identifyi
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-26T10:24:49.853936+00:00_

Web search results for query: "arXiv 2309.17453 Xiao "Efficient Streaming Language Models with Attention Sinks" ICLR 2024"

Links: [{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"[2309.17453v1] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v1"},{"title":"[2309.17453v2] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v2"},{"title":"[2309.17453v4] Efficient Streaming Language Models with Attention Sinks","url":"http://arxiv.org/abs/2309.17453v4"},{"title":"[2309.17453v3] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453v3"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/html/2309.17453"}]

I found the paper you're looking for! Here's information about arXiv:2309.17453:

**Paper Title:** Efficient Streaming Language Models with Attention Sinks

**Authors:** Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis

**Key Focus:** The paper addresses challenges in deploying Large Language Models (LLMs) in streaming applications such as multi-round dialogue, where long interactions are expected. 

**Main Challenges Addressed:**
1. During the decoding stage, caching previous tokens' Key and Value states (KV) consumes extensive memory
2. Popular LLMs cannot generalize to longer texts than the training sequence length

**Key Contribution:** The paper observes an interesting phenomenon, namely attention sink, that keeping the KV of initial tokens will largely recover the performance of window attention.

**Framework:** StreamingLLM is introduced, an eff
…[truncated 506 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-26T10:24:49.854088+00:00_

Web search results for query: "arXiv 2406.16008 Hsieh "Found in the Middle Calibrating Positional Attention Bias" ACL 2024"

Links: [{"title":"[2406.16008] Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/abs/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias","url":"https://arxiv.org/pdf/2406.16008"},{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.890/"},{"title":"Paper page - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://huggingface.co/papers/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/html/2406.16008v1"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization | Request PDF","url":"https://www.researchgate.net/publication/381665889_Found_in_the_Middle_Calibrating_Positional_Attention_Bias_Improves_Long_Context_Utilization"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long-Context RAG - Beancount.io","url":"https://beancount.io/bean-labs/research-logs/2026/07/02/found-in-the-middle-calibrating-positional-attention-bias"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization by Arxiv Papers","url":"https://creators.spotify.com/pod/show/arxiv-papers/episodes/Found-in-the-Middle-Calibrating-Positional-Attention-Bias-Improves-Long-Context-Utilization-e2leojv"}]

I found the paper for you. Here are the key details:

## Paper Overview

"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization" was published in Findings of the Association for Computational Linguistics: ACL 2024, pages 14982–14995, Bangkok, Thailand.

## Main Contrib
…[truncated 1125 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 72 · 2026-05-26T10:24:49.854232+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2505.06708 Qiu \"Gated Attention for Large Language Models\" NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2505.06708 Qiu \"Gated Attention for Large Language Models\" NeurIPS 2025"
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-26T10:24:49.854382+00:00_

Web search results for query: "Luo Wang Yan "Adaptive Layer-skipping in Pre-trained LLMs" FlexiDepth COLM 2025 arXiv:2503.23798"

Links: [{"title":"[2503.23798] Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/abs/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs Xuan Luo, Weizhi Wang, Xifeng Yan","url":"https://arxiv.org/pdf/2503.23798"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs","url":"https://arxiv.org/html/2503.23798"},{"title":"Paper page - Adaptive Layer-skipping in Pre-trained LLMs","url":"https://huggingface.co/papers/2503.23798"},{"title":"Adaptive Inference in Pre-trained LLMs Layer-skipping","url":"https://sites.cs.ucsb.edu/~xyan/presentation/Colm2025_Adaptive.pdf"},{"title":"Adaptive Layer-skipping in Pre-trained LLMs - Xuan Luo","url":"https://luoxuan-cs.github.io/flexidepth/"},{"title":"GitHub - luoxuan-cs/Flexidepth: The official repo for the paper \"Adaptive Layer-skipping in Pre-trained LLMs\" · GitHub","url":"https://github.com/luoxuan-cs/Flexidepth"},{"title":"Papers by Xuan Luo","url":"https://www.aimodels.fyi/authors/arxiv/Xuan%20Luo"}]

I found the paper! Here are the key details about the research:

## Paper Information

The paper is authored by Xuan Luo, Weizhi Wang, and Xifeng Yan, with arXiv identifier 2503.23798, and it was published at the Second Conference on Language Modeling (COLM) in 2025.

## FlexiDepth Method

FlexiDepth dynamically adjusts the number of Transformer layers used in text generation. By incorporating a plug-in router and adapter, FlexiDepth enables adaptive computation in LLMs without modifying their original parameters.

## Key Results

Applied to Llama-3-8B, it skips 8 out of 32 layers while maintaining full benchmark performance. Computational demands in LLMs significantly vary based on token type, with generating repetitive tokens or fixed phrases requiring fewer layers, whereas producing tokens involving computation or high uncertainty requiring more layers.

## Op
…[truncated 294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-26T10:24:49.854622+00:00_

Web search results for query: "Vaswani Shazeer Parmar Uszkoreit "Attention Is All You Need" NeurIPS 2017 arXiv:1706.03762"

Links: [{"title":"[1706.03762] Attention Is All You Need","url":"https://arxiv.org/abs/1706.03762"},{"title":"Attention is All you Need","url":"https://papers.nips.cc/paper/7181-attention-is-all-you-need"},{"title":"Attention Is All You Need - Wikipedia","url":"https://en.wikipedia.org/wiki/Attention_Is_All_You_Need"},{"title":"Attention is All you Need","url":"https://proceedings.neurips.cc/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html"},{"title":"Attention Is All You Need Ashish Vaswani∗ Google Brain avaswani@google.com","url":"https://papers.neurips.cc/paper/7181-attention-is-all-you-need.pdf"},{"title":"Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N. and Polosukhin, I. (2017) Attention Is All You Need. Proceedings of the 31st International Conference on Neural Information Processing Systems (NeurIPS 2017), Long Beach, California, 4-9 December 2017, 5998-6008. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3709107"},{"title":"(PDF) Attention is All you Need (2017) | Ashish Vaswani | 93950 Citations","url":"https://scispace.com/papers/attention-is-all-you-need-1hodz0wcqb"},{"title":"ATTENTION IS ALL YOU NEED. Original Paper by Ashish Vaswani, Noam… | by Vishal dhawal | Medium","url":"https://medium.com/@vishaldhawal8853/all-you-need-is-attention-75bb845d1827"},{"title":"Vaswani, A., Shazeer, N., Parmar, N., et al. (2017) Attention Is All You Need. Advances in Neural Information Processing Systems 30 Annual Conference on Neural Information Processing Systems 2017, Long Beach, 4-9 December 2017, 5998-6008 - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3381180"},{"title":"Attention is all you need | BibSonomy","url":"https://www.bibsonomy.org/bibtex/c9bf08cbcb15680c8
…[truncated 1013 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 75 · 2026-05-26T10:24:49.854796+00:00_

Web search results for query: "Schuster Fisch Gupta Dehghani "Confident Adaptive Language Modeling" NeurIPS 2022 arXiv:2207.07061"

Links: [{"title":"Confident Adaptive Language Modeling","url":"https://papers.neurips.cc/paper_files/paper/2022/file/6fac9e316a4ae75ea244ddcef1982c71-Paper-Conference.pdf"},{"title":"[2207.07061] Confident Adaptive Language Modeling","url":"https://arxiv.org/abs/2207.07061"},{"title":"Confident adaptive language modeling | Proceedings of the 36th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3600270.3601539"},{"title":"Publications | Tal Schuster","url":"https://people.csail.mit.edu/tals/publication/"},{"title":"[Quick Review] Confident Adaptive Language Modeling","url":"https://liner.com/review/confident-adaptive-language-modeling"},{"title":"Confident Adaptive Language Modeling. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1e1462f300263b9cea75b3f967f0850ca"},{"title":"[PDF] Confident Adaptive Language Modeling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Confident-Adaptive-Language-Modeling-Schuster-Fisch/2ef60a4ea4ea53056be811ff55679eb59fb4b586"}]

Great! I found the paper. Here are the search results for "Confident Adaptive Language Modeling":

## Summary

The paper "Confident Adaptive Language Modeling" was authored by Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, and Donald Metzler, and was published in Neural Information Processing Systems (NeurIPS), 2022.

## Main Contribution

The paper introduces Confident Adaptive Language Modeling (CALM), a framework for dynamically allocating different amounts of compute per input and generation timestep. Recent advances in Transformer-based large language models (LLMs) have led to significant performance improvements across many tasks, but these gains come with a drastic increase in the models' size, potentially leading to slow and costly use at inference time.

…[truncated 596 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 76 · 2026-05-26T10:24:49.854956+00:00_

Web search results for query: "Raposo Ritter Richards Lillicrap "Mixture-of-Depths" dynamically allocating compute transformer ICML 2024 arXiv:2404.02258"

Links: [{"title":"[PDF] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mixture-of-Depths:-Dynamically-allocating-compute-Raposo-Ritter/a1f23f04421cdc62e80fe9f04c1ce60f4a6af9f0"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models, David Raposo+, N/A, arXiv'24 · Issue #1273 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1273"},{"title":"[2404.02258] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/abs/2404.02258"},{"title":"γ−MOD: EXPLORING MIXTURE-OF-DEPTH ADAPTA","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf"},{"title":"REINFORCED ADAPTIVE ROUTING FOR MIXTURE-OF","url":"https://openreview.net/pdf/1f7aee75d6c7230669eca4fb80e138c2790fdb96.pdf"},{"title":"GitHub - sramshetty/mixture-of-depths: An unofficial implementation of \"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models\" · GitHub","url":"https://github.com/sramshetty/mixture-of-depths"},{"title":"[2404.02258v1] Mixture-of-Depths: Dynamically allocating compute in transformer-based language models","url":"https://arxiv.org/abs/2404.02258v1"},{"title":"Mixture-of-Depths: Dynamically allocating compute in transformer-based language models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240402258R/abstract"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/955499a8e2860ed746717c1374224c43-Paper-Conference.pdf"},{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipe
…[truncated 1384 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 77 · 2026-05-26T10:24:49.855110+00:00_

Web search results for query: "Fan Grave Joulin "Reducing Transformer Depth on Demand with Structured Dropout" LayerDrop ICLR 2020 arXiv:1909.11556"

Links: [{"title":"ICLR: Reducing Transformer Depth on Demand with Structured Dropout","url":"https://iclr.cc/virtual_2020/poster_SylO2yStDr.html"},{"title":"[1909.11556] Reducing Transformer Depth on Demand with Structured Dropout","url":"https://arxiv.org/abs/1909.11556"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | Request PDF","url":"https://www.researchgate.net/publication/336056561_Reducing_Transformer_Depth_on_Demand_with_Structured_Dropout"},{"title":"Reducing Transformer Depth on Demand with Structured Dropout | OpenReview","url":"https://openreview.net/forum?id=SylO2yStDr"},{"title":"[PDF] Reducing Transformer Depth on Demand with Structured Dropout | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Reducing-Transformer-Depth-on-Demand-with-Dropout-Fan-Grave/f4a8480cffa491020bdbb8c4c4e7a7e923b1c2c1"},{"title":"Dropout layers, not weights or nodes! \"LayerDrop\" proposal | AI-SCHOLAR | AI: (Artificial Intelligence) Articles and technical information media","url":"https://ai-scholar.tech/en/articles/dropout/LayerDrop"},{"title":"REDUCING TRANSFORMER DEPTH ON DEMAND WITH STRUCTURED DROPOUT Angela Fan","url":"https://arxiv.org/pdf/1909.11556"},{"title":"fairseq/examples/layerdrop/README.md at main · facebookresearch/fairseq","url":"https://github.com/facebookresearch/fairseq/blob/main/examples/layerdrop/README.md"},{"title":"ICLR 2020: Efficient Deep Learning and More | ntentional","url":"https://www.ntentional.com/papers/nlp/efficient-nlp/transformers/2020/05/09/iclr-highlights-2.html"}]

Based on the search results, I found comprehensive information about the paper you're looking for:

## Paper Details

The paper "Reducing Transformer Depth on Demand with Structured Dropout" was written by Angela Fan, Edouard Grave, and Armand Joulin, submitted on September 25, 2019, and
…[truncated 980 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 78 · 2026-05-26T10:24:49.855264+00:00_

Web search results for query: "Gromov Tirumala Shapourian Glorioso Roberts "Unreasonable Ineffectiveness of the Deeper Layers" ICLR 2025 arXiv:2403.17887"

Links: [{"title":"[2403.17887] The Unreasonable Ineffectiveness of the Deeper Layers","url":"https://arxiv.org/abs/2403.17887"},{"title":"[Paper Note] The Unreasonable Ineffectiveness of the Deeper Layers, Andrey Gromov+, ICLR'25, 2024.03 · Issue #1292 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/1292"},{"title":"The Unreasonable Ineffectiveness of the Deeper Layers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240317887G/abstract"},{"title":"Paper page - The Unreasonable Ineffectiveness of the Deeper Layers","url":"https://huggingface.co/papers/2403.17887"},{"title":"The Unreasonable Ineffectiveness of the Deeper Layers","url":"https://arxiv.org/html/2403.17887.pdf"},{"title":"ICLR Poster The Unreasonable Ineffectiveness of the Deeper Layers","url":"https://iclr.cc/virtual/2025/poster/28400"},{"title":"[PDF] The Unreasonable Ineffectiveness of the Deeper Layers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/The-Unreasonable-Ineffectiveness-of-the-Deeper-Gromov-Tirumala/2ccbafd636184c6edd83e585359514923b6cf849"},{"title":"The Unreasonable Ineffectiveness of the Deeper Layers | alphaXiv","url":"https://www.alphaxiv.org/abs/2403.17887"},{"title":"E25 : The Unreasonable Ineffectiveness of the Deeper Layers | by Praveen Thenraj | summarAIze | Medium","url":"https://medium.com/papers-i-found/the-unreasonable-ineffectiveness-of-the-deeper-layers-536e4a6bc67e"}]

I found the paper you're looking for! Here's the information:

**Title:** The Unreasonable Ineffectiveness of the Deeper Layers

**Authors:** Andrey Gromov, Kushal Tirumala, Hassan Shapourian, Paolo Glorioso, and Daniel A. Roberts

**ArXiv ID:** 2403.17887

**Venue:** International Conference on Learning Representations (ICLR) 2025

**Summary:** The paper studies how knowledge is stored
…[truncated 835 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-26T10:24:49.855462+00:00_

Web search results for query: "Hu Shen Wallis Allen-Zhu Li Wang Chen "LoRA Low-Rank Adaptation of Large Language Models" ICLR 2022 arXiv:2106.09685"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/html/2106.09685v2"},{"title":"GitHub - microsoft/LoRA: Code for loralib, an implementation of \"LoRA: Low-Rank Adaptation of Large Language Models\" · GitHub","url":"https://github.com/microsoft/LoRA"},{"title":"[PDF] LoRA: Low-Rank Adaptation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LoRA:-Low-Rank-Adaptation-of-Large-Language-Models-Hu-Shen/a8ca46b171467ceb2d7652fbfb67fe701ad86092"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models Edward Hu∗ Yelong Shen∗","url":"https://arxiv.org/pdf/2106.09685v1/1000"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models | BibSonomy","url":"https://www.bibsonomy.org/bibtex/5fa57783e2dbd09410e0ddfbdf0efce7"},{"title":"[2106.09685v2] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685v2"},{"title":"LORA: LOW-RANK ADAPTATION OF LARGE LAN","url":"https://openreview.net/pdf?id=nZeVKeeFYf9"},{"title":"[2106.09685v1] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685v1"}]

I found the paper you're searching for. The paper "LoRA: Low-Rank Adaptation of Large Language Models" is authored by Edward Hu, Yelong Shen, Phillip Wallis, Zeyuan Allen-Zhu, Yuanzhi Li, Shean Wang, Lu Wang, and Weizhu Chen from Microsoft Corporation, with arXiv identifier 2106.09685.

The paper proposes LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture, greatly reducing the number of trainable parameters for downstream tasks. Compared to GPT-3 175B fine-tuned with Adam
…[truncated 433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-26T10:24:49.855654+00:00_

Web search results for query: "He Zhang Ren Sun "Deep Residual Learning for Image Recognition" CVPR 2016 arXiv:1512.03385"

Links: [{"title":"Deep Residual Learning for Image Recognition","url":"https://openaccess.thecvf.com/content_cvpr_2016/html/He_Deep_Residual_Learning_CVPR_2016_paper.html"},{"title":"Deep Residual Learning for Image Recognition Kaiming He Xiangyu Zhang","url":"https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/He_Deep_Residual_Learning_CVPR_2016_paper.pdf"},{"title":"He, K., Zhang, X., Ren, S. and Sun, J. (2016) Deep Residual Learning for Image Recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Las Vegas, 27-30 June 2016, 770-778. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3166599"},{"title":"Deep Residual Learning for Image Recognition","url":"https://bibbase.org/network/publication/he-zhang-ren-sun-deepresiduallearningforimagerecognition"},{"title":"He, K., Zhang, X., Ren, S., et al. (2016) Deep Residual Learning for Image Recognition. Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, Las Vegas, 27-30 June 2016, 770-778. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=2935503"},{"title":"Deep Residual Learning for Image Recognition | Encyclopedia MDPI","url":"https://encyclopedia.pub/entry/27415"},{"title":"He, K.M., Zhang, X.Y., Ren, S.Q. and Sun, J. (2016) Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Las Vegas, 27-30 June 2016, 770-778. - References - Scientific Research Publishing","url":"https://www.scirp.org/(S(351jmbntvnsjt1aadkposzje))/reference/referencespapers.aspx?referenceid=3209894"},{"title":"He, K., Zhang, X., Ren, S. and Sun, J. (2015) Deep Residual Learning for Image Recognition. 2016 IEEE Conference on Computer Vision and Pattern Reco
…[truncated 1325 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-26T10:24:49.855809+00:00_

Web search results for query: "Veit Wilber Belongie "Residual Networks Behave Like Ensembles of Relatively Shallow Networks" NeurIPS 2016 arXiv:1605.06431"

Links: [{"title":"Residual networks behave like ensembles of relatively shallow networks | Proceedings of the 30th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3157096.3157158"},{"title":"[1605.06431] Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://arxiv.org/abs/1605.06431"},{"title":"(PDF) Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://www.researchgate.net/publication/303409435_Residual_Networks_Behave_Like_Ensembles_of_Relatively_Shallow_Networks"},{"title":"[PDF] Residual Networks Behave Like Ensembles of Relatively Shallow Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Residual-Networks-Behave-Like-Ensembles-of-Shallow-Veit-Wilber/2a24b68ef180c0c8742bd494a55fb6f68864efed"},{"title":"Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://papers.nips.cc/paper/2016/hash/37bc2f75bf1bcfe8450a1a41c200364c-Abstract.html"},{"title":"Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://arxiv.org/pdf/1605.06431"},{"title":"NIPS Poster Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://nips.cc/virtual/2016/poster/7167"},{"title":"Neurips","url":"https://proceedings.neurips.cc/paper/2016/file/37bc2f75bf1bcfe8450a1a41c200364c-Paper.pdf"},{"title":"Reviews: Residual Networks Behave Like Ensembles of Relatively Shallow Networks","url":"https://proceedings.neurips.cc/paper/2016/file/37bc2f75bf1bcfe8450a1a41c200364c-Reviews.html"},{"title":"Residual Networks Behave Like Ensembles of Relatively Shallow Networks | SE(3) Computer Vision Group at Cornell Tech","url":"https://vision.cornell.edu/se3/residual-networks-behave-like-ensembles-of-relatively-shallow-network
…[truncated 1093 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-26T10:24:49.855965+00:00_

Web search results for query: "Srivastava Greff Schmidhuber "Highway Networks" ICML 2015 arXiv:1505.00387"

Links: [{"title":"[1505.00387] Highway Networks","url":"https://arxiv.org/abs/1505.00387"},{"title":"(PDF) Highway Networks","url":"https://www.researchgate.net/publication/275897262_Highway_Networks"},{"title":"Highway Networks Rupesh Kumar Srivastava RUPESH@IDSIA.CH Klaus Greff","url":"https://arxiv.org/pdf/1505.00387"},{"title":"Highway Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150500387S/abstract"},{"title":"Recurrent Highway Networks","url":"https://proceedings.mlr.press/v70/zilly17a/zilly17a.pdf"},{"title":"[PDF] Highway Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Highway-Networks-Srivastava-Greff/e0945081b5b87187a53d4329cf77cd8bff635795"},{"title":"Recurrent Highway Networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305890.3306114"},{"title":"Srivastava, R.K., Greff, K. and Schmidhuber, J. (2015) Highway ...","url":"https://www.scirp.org/reference/referencespapers"},{"title":"Highway Networks","url":"https://bibbase.org/network/publication/srivastava-greff-schmidhuber-highwaynetworks-2015"},{"title":"Training Very Deep Networks","url":"https://papers.nips.cc/paper/5850-training-very-deep-networks"}]

I found the paper you're searching for. Here are the key details:

**Paper Information:**
- Title: "Highway Networks" by authors Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber
- arXiv identifier: 1505.00387, submitted May 3, 2015
- Published in Advances in Neural Information Processing Systems 28 (NIPS 2015)

**Main Contribution:**
The paper introduces a new architecture designed to ease gradient-based training of very deep networks. These "highway networks" allow unimpeded information flow across several layers on "information highways" and are characterized by the use of gating units which learn to regulate t
…[truncated 472 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 83 · 2026-05-26T10:24:49.856108+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Raposo \"Mixture-of-Depths\" ICML 2024 OR ICLR 2025 venue published conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Raposo \"Mixture-of-Depths\" ICML 2024 OR ICLR 2025 venue published conference"
  }
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-26T10:24:49.856230+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Srivastava Greff Schmidhuber \"Highway Networks\" ICML 2015 deep learning workshop OR NeurIPS 2015 venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Srivastava Greff Schmidhuber \"Highway Networks\" ICML 2015 deep learning workshop OR NeurIPS 2015 venue"
  }
}
```

</details>

---

### Tool call

_source line 85 · 2026-05-26T10:24:49.856353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bachlechner \"ReZero\" authors \"Garrison\" OR \"Gary\" Cottrell UAI 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bachlechner \"ReZero\" authors \"Garrison\" OR \"Gary\" Cottrell UAI 2021"
  }
}
```

</details>

---

### Tool call

_source line 86 · 2026-05-26T10:24:49.856514+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Huanru Henry Mao\" OR \"Henry Mao\" ReZero authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Huanru Henry Mao\" OR \"Henry Mao\" ReZero authors"
  }
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-26T10:24:49.856652+00:00_

Web search results for query: ""Huanru Henry Mao" OR "Henry Mao" ReZero authors"

Links: [{"title":"ReZero is all you need: fast convergence at large depth","url":"https://proceedings.mlr.press/v161/bachlechner21a.html"},{"title":"GitHub - majumderb/rezero: Official PyTorch Repo for \"ReZero is All You Need: Fast Convergence at Large Depth\" · GitHub","url":"https://github.com/majumderb/rezero"},{"title":"dblp: Huanru Henry Mao","url":"https://dblp.org/pid/213/7630.html"},{"title":"Tappei Nagatsuki - Wikipedia","url":"https://en.wikipedia.org/wiki/Tappei_Nagatsuki"},{"title":"Re:Zero - Wikipedia","url":"https://en.wikipedia.org/wiki/Re:Zero"},{"title":"Amazon.com: Re:Zero: Starting Life in Another World, Vol. 1: 9780316315302: Nagatsuki, Tappei, Otsuka, Shinichirou: Books","url":"https://www.amazon.com/Re-Zero-Starting-Another-World/dp/0316315303"},{"title":"GitHub - vvvm23/ReZero: PyTorch implementation of \"ReZero is All You Need: Fast Convergence at Large Depth\".","url":"https://github.com/vvvm23/ReZero"},{"title":"Re: Zero: 10 Things You Never Knew About The Making Of The Dark Isekai Anime","url":"https://www.cbr.com/rezero-anime-making-of-facts/"},{"title":"Abaddon on X: \"Here's a compilation of interesting Q&amp;A the author of Re:Zero (Tappei Nagatsuki) made about the story and world building. There will be NO major spoilers for anime onlies.\" / X","url":"https://x.com/AbdFmL/status/1291691747819638785"}]

Based on the search results, I found information about Henry Mao, but he is not an author of the Re:Zero light novel series.

Huanru Henry Mao is a co-author of the paper "ReZero is All You Need: Fast Convergence at Large Depth", which is a machine learning research paper about deep neural network architectures, not related to the Re:Zero anime/light novel series.

The actual author of the Re:Zero light novel series is Tappei Nagatsuki. There is no connection between Henry Mao and the Re:Zero fictional work you may have been thinking of.


REMINDER: You 
…[truncated 86 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-26T10:24:49.856798+00:00_

Web search results for query: "Raposo "Mixture-of-Depths" ICML 2024 OR ICLR 2025 venue published conference"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf"},{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipedia-mixture-of-depths/"},{"title":"ICML 2025 Schedule","url":"https://icml.cc/virtual/2025/calendar"},{"title":"GitHub - falcon-xu/early-exit-papers: A curated list of early exiting (LLM, CV, NLP, etc) · GitHub","url":"https://github.com/falcon-xu/early-exit-papers"},{"title":"GitHub - DmitryRyumin/ICML-2025-Papers: ICML 2025 Papers: Dive into cutting-edge research from the premier machine learning conference. Stay current with breakthroughs in deep learning, generative AI, optimization, reinforcement learning, and beyond. Code implementations included. ⭐ support the future of machine learning research!","url":"https://github.com/DmitryRyumin/ICML-2025-Papers"}]

Based on the search results, I can provide you with information about the Raposo "Mixture-of-Depths" paper's publication venue:

The Mixture-of-Depths paper by Raposo et al. was published at ICML 2024 (International Conference on Machine Learning). While it appeared on arXiv as 2404.02258, the official peer-reviewed conference publication was at ICML 2024, not ICLR 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-26T10:24:49.856939+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 90 · 2026-05-26T10:24:49.857055+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-26T10:24:49.857167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Bengio Vinyals Jaitly Shazeer \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\" NeurIPS 2015 arXiv:1506.03099"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Bengio Vinyals Jaitly Shazeer \"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\" NeurIPS 2015 arXiv:1506.03099"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-26T10:24:49.857280+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ranzato Chopra Auli Zaremba \"Sequence Level Training with Recurrent Neural Networks\" ICLR 2016 arXiv:1511.06732"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ranzato Chopra Auli Zaremba \"Sequence Level Training with Recurrent Neural Networks\" ICLR 2016 arXiv:1511.06732"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-26T10:24:49.857392+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lamb Goyal Zhang Zhang Courville Bengio \"Professor Forcing: A New Algorithm for Training Recurrent Networks\" NeurIPS 2016 arXiv:1610.09038"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lamb Goyal Zhang Zhang Courville Bengio \"Professor Forcing: A New Algorithm for Training Recurrent Networks\" NeurIPS 2016 arXiv:1610.09038"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-26T10:24:49.857526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Leblond Alayrac Osokin Lacoste-Julien \"SEARNN: Training RNNs with Global-Local Losses\" ICLR 2018 arXiv:1706.04499"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Leblond Alayrac Osokin Lacoste-Julien \"SEARNN: Training RNNs with Global-Local Losses\" ICLR 2018 arXiv:1706.04499"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-26T10:24:49.857640+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "He Zhang Zhou Glass \"Quantifying Exposure Bias for Neural Language Generation\" arXiv:1905.10617 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "He Zhang Zhou Glass \"Quantifying Exposure Bias for Neural Language Generation\" arXiv:1905.10617 2019"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-26T10:24:49.857751+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wiseman Rush \"Sequence-to-Sequence Learning as Beam-Search Optimization\" EMNLP 2016 arXiv:1606.02960"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wiseman Rush \"Sequence-to-Sequence Learning as Beam-Search Optimization\" EMNLP 2016 arXiv:1606.02960"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-26T10:24:49.857874+00:00_

Web search results for query: "Lamb Goyal Zhang Zhang Courville Bengio "Professor Forcing: A New Algorithm for Training Recurrent Networks" NeurIPS 2016 arXiv:1610.09038"

Links: [{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://proceedings.neurips.cc/paper/2016/hash/16026d60ff9b54410b3435b403afd226-Abstract.html"},{"title":"[PDF] Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/2fe874a1c85ecc9e848bf9defd76535e19d51f39"},{"title":"[1610.09038] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://arxiv.org/abs/1610.09038"},{"title":"Figure 1 from Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/db38edba294b7d2fd8ca3aad65721bd9dce32619/figure/0"},{"title":"[Quick Review] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://liner.com/review/professor-forcing-a-new-algorithm-for-training-recurrent-networks"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2016arXiv161009038L/abstract"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Professor+forcing:+A+new+algorithm+for+training+recurrent+networks&author=Anirudh+Goyal&author=Alex+Lamb&author=Ying+Zhang&author=Saizheng+Zhang&author=Aaron+C.+Courville&author=Yoshua+Bengio&publication_year=2016&journal=Advances+in+Neural+Information+Processing+Systems+29:+Annual+Conference+on+Neural+Information+Processing+Systems+2016,+December+5%E2%80%9310,+2016,+Barcelona,+Spain&pages=4601-4609"},{"title":"NIPS Poster Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://neurips.cc/virtual/2016/poster/7377"},{"title":"B
…[truncated 1433 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-26T10:24:49.858020+00:00_

Web search results for query: "Bengio Vinyals Jaitly Shazeer "Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks" NeurIPS 2015 arXiv:1506.03099"

Links: [{"title":"[1506.03099] Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://arxiv.org/abs/1506.03099"},{"title":"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://arxiv.org/pdf/1506.03099"},{"title":"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://www.researchgate.net/publication/278048447_Scheduled_Sampling_for_Sequence_Prediction_with_Recurrent_Neural_Networks"},{"title":"Scheduled sampling for sequence prediction with recurrent Neural networks | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 1","url":"https://dl.acm.org/doi/10.5555/2969239.2969370"},{"title":"[1506.03099v3] Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://arxiv.org/abs/1506.03099v3"},{"title":"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks on ShortScience.org","url":"https://shortscience.org/paper?bibtexKey=conf/nips/BengioVJS15"},{"title":"[PDF] Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Sequence-Prediction-with-Bengio-Vinyals/df137487e20ba7c6e1e2b9a1e749f2a578b5ad99"},{"title":"A Word of Caution on Scheduled Sampling for Training RNNs","url":"https://www.inference.vc/scheduled-sampling-for-rnns-scoring-rule-interpretation/"},{"title":"Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks","url":"https://papers.nips.cc/paper/5956-scheduled-sampling-for-sequence-prediction-with-recurrent-neural-networks"}]

I found the paper you were looking for! Here are the key details:

**Title:** Scheduled Sampling for Sequence Prediction with Recurrent Neural Netw
…[truncated 779 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 99 · 2026-05-26T10:24:49.858169+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Efficient Streaming Language Models with Attention Sinks\" ICLR 2024 conference paper published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Efficient Streaming Language Models with Attention Sinks\" ICLR 2024 conference paper published"
  }
}
```

</details>

---

### Tool call

_source line 100 · 2026-05-26T10:24:49.858300+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify citations group 4",
  "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **yu2020pcgrad**: Yu, Tianhe and Kumar, Saurabh and Gupta, Abhishek and Levine, Sergey and Hausman, Karol and Finn, Chelsea. \"Gradient Surgery for Multi-Task Learning\". NeurIPS 2020. arXiv:2001.06782.\n\n2. **chen2018gradnorm**: Chen, Zhao and Badrinarayanan, Vijay and Lee, Chen-Yu and Rabinovich, Andrew. \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\". ICML 2018. arXiv:1711.02257.\n\n3. **liu2021cagrad**: Liu, Bo and Liu, Xingchao and Jin, Xiaojie and Stone, Peter and Liu, Qiang. \"Conflict-Averse Gradient Descent for Multi-task Learning\". NeurIPS 2021. arXiv:2110.14048.\n\n4. **navon2022nash**: Navon, Aviv and Shamsian, Aviv and Achituve, Idan and Maron, Haggai and Kawaguchi, Kenji and Chechik, Gal and Fetaya, Ethan. \"Multi-Task Learning as a Bargaining Game\". ICML 2022. arXiv:2202.01017.\n\n5. **dong2021attention**: Dong, Yihe and Cordonnier, Jean-Baptiste and Loukas, Andreas. \"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\". ICML 2021, pp 2793-2803. arXiv:2103.03404.\n\n6. **zhou2020drophead**: Zhou, Wangchunshu and Ge, Tao and Wei, Furu and Zhou, Ming and Xu, Ke. \"Scheduled DropHead: A Regularization Method for Transformer Models\". Findings of EMNLP 2020. arXiv:2004.13342.\n\n7. **dauphin2017language**: Dauphin, Yann N. and Fan, Angela and Auli, Michael and Grangier, David. \"Language Modeling with Gated Convolutional Networks\". ICML 2017, pp 933-941. arXiv:1612.08083.\n\n8. **shazeer2020glu**: Shazeer, Noam. \"GLU Variants Improve Transformer\". arXiv:2002.05202, 2020.\n\n9. **lin2022truthfulqa**: Lin, Stephanie and Hilton, Jacob and Evans, Owain. \"TruthfulQA: Measuring How Models Mimic Human Falsehoods\". ACL 2022, pp 3214-3252. URL: https://aclanthology.org/2022.acl-long.229/\n\n10. **hendrycks2021measuring**: Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob. \"Measuring Massive Multitask Language Understanding\". ICLR 2021. arXiv:2009.03300.\n\n11. **dettmers2023qlora**: Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke. \"QLoRA: Efficient Finetuning of Quantized LLMs\". NeurIPS 2023. arXiv:2305.14314.\n\nSearch each one individually using WebSearch. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify citations group 4",
    "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **yu2020pcgrad**: Yu, Tianhe and Kumar, Saurabh and Gupta, Abhishek and Levine, Sergey and Hausman, Karol and Finn, Chelsea. \"Gradient Surgery for Multi-Task Learning\". NeurIPS 2020. arXiv:2001.06782.\n\n2. **chen2018gradnorm**: Chen, Zhao and Badrinarayanan, Vijay and Lee, Chen-Yu and Rabinovich, Andrew. \"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\". ICML 2018. arXiv:1711.02257.\n\n3. **liu2021cagrad**: Liu, Bo and Liu, Xingchao and Jin, Xiaojie and Stone, Peter and Liu, Qiang. \"Conflict-Averse Gradient Descent for Multi-task Learning\". NeurIPS 2021. arXiv:2110.14048.\n\n4. **navon2022nash**: Navon, Aviv and Shamsian, Aviv and Achituve, Idan and Maron, Haggai and Kawaguchi, Kenji and Chechik, Gal and Fetaya, Ethan. \"Multi-Task Learning as a Bargaining Game\". ICML 2022. arXiv:2202.01017.\n\n5. **dong2021attention**: Dong, Yihe and Cordonnier, Jean-Baptiste and Loukas, Andreas. \"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\". ICML 2021, pp 2793-2803. arXiv:2103.03404.\n\n6. **zhou2020drophead**: Zhou, Wangchunshu and Ge, Tao and Wei, Furu and Zhou, Ming and Xu, Ke. \"Scheduled DropHead: A Regularization Method for Transformer Models\". Findings of EMNLP 2020. arXiv:2004.13342.\n\n7. **dauphin2017language**: Dauphin, Yann N. and Fan, Angela and Auli, Michael and Grangier, David. \"Language Modeling with Gated Convolutional Networks\". ICML 2017, pp 933-941. arXiv:1612.08083.\n\n8. **shazeer2020glu**: Shazeer, Noam. \"GLU Variants Improve Transformer\". arXiv:2002.05202, 2020.\n\n9. **lin2022truthfulqa**: Lin, Stephanie and Hilton, Jacob and Evans, Owain. \"TruthfulQA: Measuring How Models Mimic Human Falsehoods\". ACL 2022, pp 3214-3252. URL: https://aclanthology.org/2022.acl-long.229/\n\n10. **hendrycks2021measuring**: Hendrycks, Dan and Burns, Collin and Basart, Steven and Zou, Andy and Mazeika, Mantas and Song, Dawn and Steinhardt, Jacob. \"Measuring Massive Multitask Language Understanding\". ICLR 2021. arXiv:2009.03300.\n\n11. **dettmers2023qlora**: Dettmers, Tim and Pagnoni, Artidoro and Holtzman, Ari and Zettlemoyer, Luke. \"QLoRA: Efficient Finetuning of Quantized LLMs\". NeurIPS 2023. arXiv:2305.14314.\n\nSearch each one individually using WebSearch. Be thorough."
  }
}
```

</details>

---

### Tool call

_source line 101 · 2026-05-26T10:24:49.858673+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "hong2025rhea \"Rhea\" authors Wanyang Hong Zhaoning Zhang published conference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "hong2025rhea \"Rhea\" authors Wanyang Hong Zhaoning Zhang published conference 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 102 · 2026-05-26T10:24:49.858827+00:00_

Web search results for query: "hong2025rhea "Rhea" authors Wanyang Hong Zhaoning Zhang published conference 2025 2026"

Links: [{"title":"Zhaoning Zhang's research works | National University of Defense Technology and other places","url":"https://www.researchgate.net/scientific-contributions/Zhaoning-Zhang-2059945368"},{"title":"Translationese-index: Using Likelihood Ratios for Graded and Generalizable Measurement of Translationese - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.633/"},{"title":"Holiday Planning: Hong Kong School Holiday Dates for 2025-2026","url":"https://www.internationalschoolparent.com/articles/holiday-planning-hong-kong-school-holiday-dates-for-2025-2026/"},{"title":"2025 Year in Review / 2026 Look Forward – Hong Kong Employment Law | Seyfarth Shaw LLP","url":"https://www.seyfarth.com/news-insights/2025-year-in-review-2026-look-forward-hong-kong-employment-law.html"},{"title":"专属会员| Xiuli Weng Hua","url":"https://www.facebook.com/xiuli.w.hua/videos/%E4%B8%93%E5%B1%9E%E4%BC%9A%E5%91%98/939379041238208/"},{"title":"Index - Executive Dean of the School of Management and Economics, Director of the Center for FinTech and Social Finance at Shenzhen Finance Institute, SFI Chair Professor, Associate Director of Shenzhen Institute of Data Economy","url":"https://myweb.cuhk.edu.cn/bohuizhang"},{"title":"CVPR 2025 Accepted Papers","url":"https://cvpr.thecvf.com/Conferences/2025/AcceptedPapers"},{"title":"Light in Winter - Chinese Drama 2026 - CPOP HOME","url":"https://www.cpophome.com/light-in-winter-deng-lingshu-zhang-chi/"},{"title":"Wanyang Dai's Editorial Experiences","url":"http://maths.nju.edu.cn/~wydai/WanyangDaiHtml/editor.html"},{"title":"请帮助我获得更多浏览量| Xiuli Weng Hua","url":"https://www.facebook.com/xiuli.w.hua/videos/%E8%AF%B7%E5%B8%AE%E5%8A%A9%E6%88%91%E8%8E%B7%E5%BE%97%E6%9B%B4%E5%A4%9A%E6%B5%8F%E8%A7%88%E9%87%8F/948306236625820/"}]

Based on the search results, I found information about the paper you're looking for:

**"Rhea: 
…[truncated 730 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 103 · 2026-05-26T10:24:49.858987+00:00_

Web search results for query: "arXiv 2505.06708 Qiu "Gated Attention for Large Language Models" NeurIPS 2025"

Links: [{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708"},{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"[2505.06708] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://ar5iv.labs.arxiv.org/html/2505.06708"},{"title":"[2505.06708v1] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiv.org/abs/2505.06708v1"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250506708Q/abstract"},{"title":"Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://www.researchgate.net/publication/391675977_Gated_Attention_for_Large_Language_Models_Non-linearity_Sparsity_and_Attention-Sink-Free"},{"title":"Gated Attention for Large Language Models: Non-linearity, ...","url":"https://arxiv.org/pdf/2505.06708"}]

Here's what I found about the paper:

**Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free** is a paper by Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men, Le Yu, Fei Huang, Suozhi Huang, Dayiheng Liu, Jingren Zhou, and Junyang Lin (Qwen Team).

**Key Findings:**

The authors introduce Gated Attention, a mechanism that applies 
…[truncated 750 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-26T10:24:49.859138+00:00_

Web search results for query: ""Efficient Streaming Language Models with Attention Sinks" ICLR 2024 conference paper published"

Links: [{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://hanlab.mit.edu/projects/streamingllm"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/5e5fd18f863cbe6d8ae392a93fd271c9-Abstract-Conference.html"},{"title":"ICLR Poster Efficient Streaming Language Models with Attention Sinks","url":"https://iclr.cc/virtual/2024/poster/18794"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**
"Efficient Streaming Language Models with Attention Sinks" was published at ICLR 2024 with authors Xiao, Guangxuan, Tian, Yuandong, Chen, Beidi, Han, Song, and Lewis, Mike.

**What the Paper Addresses:**
The paper addresses two major challenges in deploying LLMs for streaming applications: caching previous tokens' Key and Value states (KV) consumes extensive memory, and LLMs cannot generalize to longer texts than the training sequence length.

**Main Contribution:**
The paper introduces StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence length without any fine-
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-26T10:24:49.859282+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2505.06120 Laban \"LLMs Get Lost\" authors Neville published conference ICLR NeurIPS ACL 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2505.06120 Laban \"LLMs Get Lost\" authors Neville published conference ICLR NeurIPS ACL 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-26T10:24:49.859431+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2602.07338 Liu Geng authors \"Intent Mismatch\" published venue conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2602.07338 Liu Geng authors \"Intent Mismatch\" published venue conference"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-26T10:24:49.859559+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.12922 Dongre authors Hsieh Lai Yoon Bui Hakkani-Tur published conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.12922 Dongre authors Hsieh Lai Yoon Bui Hakkani-Tur published conference"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-26T10:24:49.859674+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Rhea role-aware heuristic episodic attention arxiv 2512.06869 published venue conference journal 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Rhea role-aware heuristic episodic attention arxiv 2512.06869 published venue conference journal 2025 2026"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-26T10:24:49.859785+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2406.16008 \"Found in the Middle\" authors list Hsieh Chuang Li Wang Le Kumar"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2406.16008 \"Found in the Middle\" authors list Hsieh Chuang Li Wang Le Kumar"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-26T10:24:49.859911+00:00_

Web search results for query: "arxiv 2605.12922 Dongre authors Hsieh Lai Yoon Bui Hakkani-Tur published conference"

Links: [{"title":"[2605.12922] When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/abs/2605.12922"},{"title":"[2510.07777v1] Drift No More? Context Equilibria in Multi-Turn LLM Interactions","url":"https://arxiv.org/abs/2510.07777v1"},{"title":"[2510.07777] Drift No More? Context Equilibria in Multi-Turn LLM Interactions","url":"https://arxiv.org/abs/2510.07777"},{"title":"When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction","url":"https://arxiv.org/html/2605.12922"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/recent?skip=1237&show=1000"},{"title":"[2605.12920] Embodied Multi-Agent Coordination by Aligning World Models Through Dialogue","url":"https://arxiv.org/abs/2605.12920"},{"title":"(PDF) Drift No More? Context Equilibria in Multi-Turn LLM Interactions","url":"https://www.researchgate.net/publication/396373136_Drift_No_More_Context_Equilibria_in_Multi-Turn_LLM_Interactions"},{"title":"Machine Learning Jun 2025","url":"https://www.arxiv.org/list/cs.LG/2025-06?skip=1950&show=2000"}]

Based on the search results, here is the information about arxiv paper 2605.12922:

**Title:** When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction

**Authors:** Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, and Dilek Hakkani-Tür

**Submission Date:** May 13, 2026

**Affiliations:** Vardhan Dongre and Dilek Hakkani-Tür are from University of Illinois Urbana-Champaign, while Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, and Trung Bui are from Adobe Research

**Summary:** The paper examines how large language models can follow complex instructions in a single turn, yet over long multi-turn interactions often lose the thread of instructions, persona, and rules. The authors propose a channel-transition account where goal-defining tokens become 
…[truncated 400 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-26T10:24:49.860075+00:00_

Web search results for query: "arxiv 2505.06120 Laban "LLMs Get Lost" authors Neville published conference ICLR NeurIPS ACL 2025 2026"

Links: [{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"GitHub - microsoft/lost_in_conversation: Code that accompanies the public release of the paper Lost in Conversation (https://arxiv.org/abs/2505.06120) · GitHub","url":"https://github.com/microsoft/lost_in_conversation"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"},{"title":"[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120v1"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/pdf/2505.06120"},{"title":"LLMs Get Lost In Multi-Turn Conversation - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.06120"},{"title":"Philippe Laban on X: \"🆕paper: LLMs Get Lost in Multi-Turn Conversation In real life, people don’t speak in perfect prompts. So we simulate multi-turn conversations — less lab-like, more like real use. We find that LLMs get lost in conversation. 👀What does that mean? 🧵1/N 📄https://t.co/xt2EfGRh7e https://t.co/YgK6IyqcRv\" / X","url":"https://x.com/PhilippeLaban/status/1921936307816694206"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://www.summarizepaper.com/en/arxiv-id/2505.06120v1/"},{"title":"LLMs Get Lost In Multi-Turn Conversation (2505.06120v1)","url":"https://www.emergentmind.com/papers/2505.06120"},{"title":"(PDF) LLMs Get Lost In Multi-Turn Conversation","url":"https://www.researchgate.net/publication/391658658_LLMs_Get_Lost_In_Multi-Turn_Conversation"}]

Based on the search results, here's the information about arxiv 2505.06120:

**Paper Title:** LLMs Get Lost In Multi-Turn Conversation

**Authors:** Philippe Laban, Hiroak
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-26T10:24:49.860230+00:00_

Web search results for query: "arxiv 2602.07338 Liu Geng authors "Intent Mismatch" published venue conference"

Links: [{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://goatstack.ai/articles/2602.07338"},{"title":"SLIME: Stabilized Likelihood Implicit Margin Enforcement for Preference Optimization","url":"https://arxiv.org/html/2602.02383"},{"title":"Cross-lingual Matryoshka Representation Learning across Speech and Text","url":"https://arxiv.org/html/2602.19991"},{"title":"[2602.00899] Domain-Adaptive and Scalable Dense Retrieval for Content-Based Recommendation","url":"https://arxiv.org/abs/2602.00899"},{"title":"Intent-Driven Dynamic Chunking: Segmenting Documents to Reflect Predicted Information Needs","url":"https://arxiv.org/html/2602.14784v1"},{"title":"[2602.11902v1] Mitigating Mismatch within Reference-based Preference Optimization","url":"https://arxiv.org/abs/2602.11902v1"},{"title":"Intent Laundering: AI Safety Datasets Are Not What They Seem","url":"https://arxiv.org/html/2602.16729v1"}]

Based on the search results, here is the information about arxiv 2602.07338:

**Title:** Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation

**Authors:** Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, Gaofeng Meng

**Publication Date:** February 7, 2026

**Venue:** The search results show this is an arXiv preprint (identifier arXiv:2602.07338v1), but do not indicate a published conference venue. It appears to be a recent preprint that has not yet been published at a conference.

**Summary:** The paper argues that the root cause of performance drops in multi-turn LLM conversations lies in an intent alignment gap rather than intrinsic capability deficits, d
…[truncated 224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-26T10:24:49.860379+00:00_

Web search results for query: "arxiv 2406.16008 "Found in the Middle" authors list Hsieh Chuang Li Wang Le Kumar"

Links: [{"title":"[2406.16008] Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/abs/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://arxiv.org/html/2406.16008"},{"title":"Found in the Middle: Calibrating Positional Attention Bias","url":"https://arxiv.org/pdf/2406.16008"},{"title":"Paper page - Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization","url":"https://huggingface.co/papers/2406.16008"},{"title":"Computer Science Jun 2024","url":"https://arxiv.org/list/cs/2024-06?skip=7700"},{"title":"Published as a workshop paper at ICLR 2025 (SSI-FM) RMBOOST: REWARD MODEL","url":"https://arxiv.org/pdf/2407.16008"},{"title":"An Error Mitigated Non-Orthogonal Quantum Eigensolver via Shadow Tomography","url":"https://arxiv.org/html/2504.16008"},{"title":"Unmasking Dementia Detection by Masking Input Gradients: A JSM Approach to Model Interpretability and Precision","url":"https://arxiv.org/html/2402.16008"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=1550&show=2000"},{"title":"ChatAR: Conversation Support using Large Language Model and Augmented Reality","url":"https://arxiv.org/html/2506.16008"}]

Based on the search results, I found the authors list for the paper arxiv 2406.16008 "Found in the Middle: Calibrating Positional Attention Bias Improves Long Context Utilization":

The authors are: Cheng-Yu Hsieh, Yung-Sung Chuang, Chun-Liang Li, Zifeng Wang, Long T. Le, Abhishek Kumar, James Glass, Alexander Ratner, Chen-Yu Lee, Ranjay Krishna, and Tomas Pfister.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-26T10:24:49.860557+00:00_

Web search results for query: "Rhea role-aware heuristic episodic attention arxiv 2512.06869 published venue conference journal 2025 2026"

Links: [{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.arxiv.org/pdf/2512.06869"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/html/2512.06869v1"},{"title":"(PDF) Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.researchgate.net/publication/398476529_Rhea_Role-aware_Heuristic_Episodic_Attention_for_Conversational_LLMs"},{"title":"TUM School of Management Technische Universität München","url":"https://mediatum.ub.tum.de/doc/1774497/1774497.pdf"},{"title":"(PDF) Proceedings of 1st Workshop on Advancing Artificial Intelligence through Theory of Mind","url":"https://www.researchgate.net/publication/391530928_Proceedings_of_1st_Workshop_on_Advancing_Artificial_Intelligence_through_Theory_of_Mind/fulltext/681c1fd2df0e3f544f52c2de/Proceedings-of-1st-Workshop-on-Advancing-Artificial-Intelligence-through-Theory-of-Mind.pdf?origin=publication_detail&_tp=eyJjb250ZXh0Ijp7ImZpcnN0UGFnZSI6InByb2ZpbGUiLCJwYWdlIjoicHVibGljYXRpb25Eb3dubG9hZCIsInByZXZpb3VzUGFnZSI6InB1YmxpY2F0aW9uIn19&__cf_chl_tk=e9xZpr2z6M_T2jzqz.H5dBuLwD_DTGN0XAxi3_L3FwA-1759595645-1.0.1.1-tiblS5iUObSFnqYtZUxi9EOs32vdsceQKjzt8TJP1H0"},{"title":"TechRxiv: preprints in engineering, computer science, and related technology","url":"https://www.techrxiv.org/doi/pdf/10.36227/techrxiv.176581395.56964766/v2"},{"title":"Implementation of an intelligent decision-support system ...","url":"https://theses.hal.science/tel-05436923v1/file/TH2023PA120029.pdf"},{"title":"Building a Psychological Foundation for Human Reliability ...","url":"https://www.nrc.gov/docs/ML1131/ML113180490.pdf"},{"title":"The Landscape of Medical Agents: A Survey Xiaobin Huα† Yunhang Qianα†","url":"https://www.techrxiv.org/users/1005258/articles/1368207/master/file/
…[truncated 1261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-26T10:24:49.860708+00:00_

Web search results for query: "Srivastava Greff Schmidhuber "Highway Networks" ICML 2015 deep learning workshop OR NeurIPS 2015 venue"

Links: [{"title":"[1505.00387] Highway Networks","url":"https://arxiv.org/abs/1505.00387"},{"title":"Training Very Deep Networks Rupesh Kumar Srivastava Klaus Greff","url":"https://proceedings.neurips.cc/paper/2015/file/215a71a12769b056c3c32e7299f1c5ed-Paper.pdf"},{"title":"Recurrent Highway Networks","url":"https://proceedings.mlr.press/v70/zilly17a/zilly17a.pdf"},{"title":"Training Very Deep Networks","url":"https://papers.nips.cc/paper/5850-training-very-deep-networks"},{"title":"Highway Networks Rupesh Kumar Srivastava RUPESH@IDSIA.CH Klaus Greff","url":"https://arxiv.org/pdf/1505.00387"},{"title":"HIGHER ORDER RECURRENT NEURAL NETWORKS","url":"https://openreview.net/pdf?id=ByZvfijeg"},{"title":"[PDF] Highway Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Highway-Networks-Srivastava-Greff/e0945081b5b87187a53d4329cf77cd8bff635795"},{"title":"[PDF] Recurrent Highway Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Recurrent-Highway-Networks-Zilly-Srivastava/7dba53e72c182e25e98e8f73a99d75ff69dda0c2"}]

Based on the search results, I can provide you with information about the "Highway Networks" paper:

The Highway Networks paper by Rupesh K Srivastava, Klaus Greff, and Jürgen Schmidhuber was published at Advances in Neural Information Processing Systems 28 (NIPS 2015). 

The paper is not from an ICML 2015 deep learning workshop, but rather from NeurIPS 2015 (which was called NIPS 2015 at the time).

The paper introduces highway networks, which allow unimpeded information flow across many layers on information highways, inspired by Long Short-Term Memory recurrent networks and using adaptive gating units to regulate information flow.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-26T10:24:49.860857+00:00_

Web search results for query: "Bachlechner "ReZero" authors "Garrison" OR "Gary" Cottrell UAI 2021"

Links: [{"title":"GitHub - majumderb/rezero: Official PyTorch Repo for \"ReZero is All You Need: Fast Convergence at Large Depth\" · GitHub","url":"https://github.com/majumderb/rezero"},{"title":"ReZero is all you need: fast convergence at large depth","url":"https://proceedings.mlr.press/v161/bachlechner21a.html"},{"title":"Garrison W. Cottrell Publications - Computer Science","url":"https://cseweb.ucsd.edu/~gary/Publications.html"},{"title":"dblp: Garrison W. Cottrell","url":"https://dblp.org/pid/c/GWCottrell.html"},{"title":"Figure 3 from ReZero is All You Need: Fast Convergence at Large Depth | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReZero-is-All-You-Need:-Fast-Convergence-at-Large-Bachlechner-Majumder/17d3066c9a47c6c30bc84a217ce78ecce1ff08b2/figure/4"},{"title":"Henry Mao","url":"https://calclavia.com/"},{"title":"ReZero is All You Need: Fast Convergence at Large Depth","url":"https://www.researchgate.net/publication/339841021_ReZero_is_All_You_Need_Fast_Convergence_at_Large_Depth"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar?q=Bachlechner%2C+Thomas%2C+Bodhisattwa+Prasad+Majumder%2C+Huanru+Henry+Mao%2C+Garrison+W.+Cottrell%2C+and+Julian+McAuley+%282020%29.+ReZero+is+All+You+Need%3A+Fast+Convergence+at+Large+Depth."},{"title":"ReZero is All You Need: Fast Convergence at Large Depth Thomas Bachlechner1","url":"https://proceedings.mlr.press/v161/bachlechner21a/bachlechner21a.pdf"},{"title":"[2003.04887] ReZero is All You Need: Fast Convergence at Large Depth","url":"https://arxiv.org/abs/2003.04887"}]

Based on the search results, I found the information about the ReZero paper:

The paper "ReZero is All You Need: Fast Convergence at Large Depth" was published at UAI (Uncertainty in AI) 2021 and was authored by Thomas Bachlechner, Bodhisattwa Prasad Majumder, Huanru Henry Mao, Garrison W. Cottrell, and Julian McAuley.

…[truncated 359 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-26T10:24:49.860998+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Mixture-of-Depths\" Raposo ICLR 2025 published conference paper proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Mixture-of-Depths\" Raposo ICLR 2025 published conference paper proceedings"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-26T10:24:49.861123+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Srivastava Greff Schmidhuber \"Highway Networks\" 1505.00387 \"ICML 2015\" workshop"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Srivastava Greff Schmidhuber \"Highway Networks\" 1505.00387 \"ICML 2015\" workshop"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-26T10:24:49.861239+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Srivastava Greff Schmidhuber \"Training Very Deep Networks\" NIPS 2015"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Srivastava Greff Schmidhuber \"Training Very Deep Networks\" NIPS 2015"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-26T10:24:49.861353+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Edward Hu LoRA author \"Edward J. Hu\" full name middle initial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Edward Hu LoRA author \"Edward J. Hu\" full name middle initial"
  }
}
```

</details>

---

### Tool result

_source line 121 · 2026-05-26T10:24:49.861506+00:00_

Web search results for query: "Edward Hu LoRA author "Edward J. Hu" full name middle initial"

Links: [{"title":"[2106.09685] LoRA: Low-Rank Adaptation of Large Language Models","url":"https://arxiv.org/abs/2106.09685"},{"title":"Edward Hu on LinkedIn: The inventor of LoRA - Edward Hu","url":"https://www.linkedin.com/posts/edwardjhu_the-inventor-of-lora-edward-hu-activity-7158112183241891840-eaJP"},{"title":"About | Edward Hu","url":"https://edwardjhu.com/about/"},{"title":"Edward J. Hu - CatalyzeX","url":"https://www.catalyzex.com/author/Edward%20J.%20Hu"},{"title":"Edward J. Hu's scientific contributions","url":"https://www.researchgate.net/scientific-contributions/Edward-J-Hu-2184735551"},{"title":"Ather Gattami on LinkedIn: The inventor of LoRA - Edward Hu","url":"https://www.linkedin.com/posts/ather-gattami-7935012_the-inventor-of-lora-edward-hu-activity-7156690200042061824-tFft"},{"title":"Perspectives in AI: From LLMs to Reasoning with Edward Hu, Inventor of LoRA and μTransfer - Pear VC","url":"https://pear.vc/perspectives-in-ai-from-llms-to-reasoning-with-edward-hu-inventor-of-lora-and-%CE%BCtransfer/"},{"title":"[PDF] LoRA: Low-Rank Adaptation of Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LoRA:-Low-Rank-Adaptation-of-Large-Language-Models-Hu-Shen/a8ca46b171467ceb2d7652fbfb67fe701ad86092"},{"title":"Edward J. Hu | Semantic Scholar","url":"https://www.semanticscholar.org/author/Edward-J.-Hu/2157840220"},{"title":"LoRA: Low-Rank Adaptation of Large Language Models - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/lora-low-rank-adaptation-of-large-language-models/"}]

Based on the search results, I found the information about Edward Hu, the LoRA author:

Edward J. Hu is one of the authors of the LoRA paper "LoRA: Low-Rank Adaptation of Large Language Models." His full name as listed in the paper's BibTeX citation is "J. Edward Hu," which indicates his middle initial is "J."

The search 
…[truncated 248 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 122 · 2026-05-26T10:24:49.861668+00:00_

Web search results for query: "Srivastava Greff Schmidhuber "Highway Networks" 1505.00387 "ICML 2015" workshop"

Links: [{"title":"[1505.00387] Highway Networks","url":"https://arxiv.org/abs/1505.00387"},{"title":"Highway Networks Rupesh Kumar Srivastava RUPESH@IDSIA.CH Klaus Greff","url":"https://arxiv.org/pdf/1505.00387"},{"title":"[PDF] Highway Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Highway-Networks-Srivastava-Greff/e0945081b5b87187a53d4329cf77cd8bff635795"},{"title":"[1505.00387v2] Highway Networks","url":"https://arxiv.org/abs/1505.00387v2"},{"title":"Recurrent Highway Networks","url":"https://proceedings.mlr.press/v70/zilly17a/zilly17a.pdf"},{"title":"[1505.00387] Highway Networks","url":"http://export.arxiv.org/abs/1505.00387"},{"title":"[1505.00387] Highway Networks - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/1505.00387"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Highway+networks&amp=&author=R.K.+Srivastava&amp=&author=K.+Greff&amp=&author=J.+Schmidhuber&amp=&publication_year=2015"},{"title":"highway-networks/README.md at master · flukeskywalker/highway-networks","url":"https://github.com/flukeskywalker/highway-networks/blob/master/README.md"}]

Based on the search results, here's what I found about the Highway Networks paper:

The paper "Highway Networks" was authored by Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber, with the work submitted on May 3, 2015 and last revised on November 3, 2015.

The paper introduces a new architecture designed to ease gradient-based training of very deep networks, called highway networks, since they allow unimpeded information flow across several layers on "information highways". The architecture is characterized by the use of gating units which learn to regulate the flow of information through a network.

In preliminary experiments, the authors found that highway networks as deep as 900 layers can be optimized using simple Stochast
…[truncated 436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 123 · 2026-05-26T10:24:49.861824+00:00_

Web search results for query: "Srivastava Greff Schmidhuber "Training Very Deep Networks" NIPS 2015"

Links: [{"title":"Training Very Deep Networks Rupesh Kumar Srivastava Klaus Greff","url":"https://proceedings.neurips.cc/paper/2015/file/215a71a12769b056c3c32e7299f1c5ed-Paper.pdf"},{"title":"Training Very Deep Networks","url":"https://papers.nips.cc/paper/2015/hash/215a71a12769b056c3c32e7299f1c5ed-Abstract.html"},{"title":"[1507.06228] Training Very Deep Networks","url":"https://arxiv.org/abs/1507.06228"},{"title":"[PDF] Training Very Deep Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Training-Very-Deep-Networks-Srivastava-Greff/b92aa7024b87f50737b372e5df31ef091ab54e62"},{"title":"Training Very Deep Networks | Request PDF","url":"https://www.researchgate.net/publication/280329704_Training_Very_Deep_Networks"},{"title":"Training very deep networks | Proceedings of the 29th International Conference on Neural Information Processing Systems - Volume 2","url":"https://dl.acm.org/doi/10.5555/2969442.2969505"},{"title":"Advances in Neural Information Processing Systems 28","url":"https://papers.nips.cc/paper_files/paper/2015"},{"title":"Training Very Deep Networks","url":"https://www.emergentmind.com/papers/1507.06228"},{"title":"Training Very Deep Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150706228S/abstract"},{"title":"Training Very Deep Networks","url":"https://arxiv.org/pdf/1507.06228"}]

I found the paper you're looking for! "Training Very Deep Networks" by Rupesh K Srivastava, Klaus Greff, and Jürgen Schmidhuber was published at NIPS 2015.

The paper introduces "highway networks" which allow unimpeded information flow across many layers, inspired by Long Short-Term Memory recurrent networks and use adaptive gating units to regulate the information flow. Even with hundreds of layers, highway networks can be trained directly through simple gradient descent.

The paper is available from multiple sources:
- Official NI
…[truncated 358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-26T10:24:49.861965+00:00_

Web search results for query: ""Mixture-of-Depths" Raposo ICLR 2025 published conference paper proceedings"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=WwpYSOkkCt"},{"title":"Neural Mixture Models with Expectation-Maximization for End-to-end Deep   Clustering","url":"https://arxiv.org/pdf/2107.02453"},{"title":"Neural Mixture Distributional Regression","url":"https://arxiv.org/pdf/2010.06889"},{"title":"DA-MoE: Addressing Depth-Sensitivity in Graph-Level Analysis through   Mixture of Experts","url":"https://arxiv.org/pdf/2411.03025"}]

I found the search results for your query. The results show that "Mixture-of-Depths: Dynamically allocating compute in transformer-based language models" by David Raposo, Samuel Ritter, Blake A. Richards, Timothy P. Lillicrap, Peter Conway Humphreys, and Adam Santoro was published in 2024 (CoRR, abs/2404.02258).

However, the paper appears to be cited in ICLR 2025 proceedings papers, but the original Mixture-of-Depths paper itself was published earlier (2024). The search results show references to this work in ICLR 2025 conference papers, particularly in papers that build upon or reference the Mixture-of-Depths approach.

The direct paper links found are:
1. **ICLR 2025 Proceedings**: https://proceedings.iclr.cc/paper_files/paper/2025/file/b3847cda0c8cc0cfcdacf462dc122214-Paper-Conference.pdf
2. **OpenReview**: https://openreview.net/pdf?id=WwpYSOkkCt

Would you like me to search for more specific information about the original Mixture-of-Depths paper or papers that cite it at ICLR 2025?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 125 · 2026-05-26T10:24:49.862102+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview \"Mixture-of-Depths\" Raposo ICLR 2025 OR ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview \"Mixture-of-Depths\" Raposo ICLR 2025 OR ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-26T10:24:49.862221+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1505.00387 \"Highway Networks\" \"ICML 2015 Deep Learning Workshop\" published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1505.00387 \"Highway Networks\" \"ICML 2015 Deep Learning Workshop\" published venue"
  }
}
```

</details>

---

### Tool call

_source line 127 · 2026-05-26T10:24:49.862335+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Srivastava \"Highway Networks\" arxiv 1505.00387 \"published\" venue workshop OR conference proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Srivastava \"Highway Networks\" arxiv 1505.00387 \"published\" venue workshop OR conference proceedings"
  }
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-26T10:24:49.862476+00:00_

Web search results for query: "Srivastava "Highway Networks" arxiv 1505.00387 "published" venue workshop OR conference proceedings"

Links: [{"title":"Highway Networks Rupesh Kumar Srivastava RUPESH@IDSIA.CH Klaus Greff","url":"https://arxiv.org/pdf/1505.00387"},{"title":"[1505.00387] Highway Networks","url":"https://arxiv.org/abs/1505.00387"},{"title":"[PDF] Highway Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Highway-Networks-Srivastava-Greff/e0945081b5b87187a53d4329cf77cd8bff635795"},{"title":"[1505.00387v2] Highway Networks","url":"https://arxiv.org/abs/1505.00387v2"},{"title":"[1505.00387] Highway Networks - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/1505.00387"},{"title":"[1505.00387] Highway Networks","url":"http://export.arxiv.org/abs/1505.00387"},{"title":"Highway Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150500387S/abstract"},{"title":"Recurrent Highway Networks","url":"https://proceedings.mlr.press/v70/zilly17a/zilly17a.pdf"},{"title":"(PDF) Highway Networks","url":"https://www.researchgate.net/publication/275897262_Highway_Networks"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Highway+networks&amp=&author=R.+K.+Srivastava&amp=&author=K.+Greff&amp=&author=J.+Schmidhuber&amp=&publication_year=2015"}]

Based on the search results, I found the information you were looking for:

The Highway Networks paper by Srivastava et al. (arxiv 1505.00387) was presented at the ICML 2015 Deep Learning workshop. The paper is described as "an extended abstract" introducing the highway networks architecture.

Additionally, a full paper version is available at arXiv:1507.06228, which likely represents the extended conference or workshop proceedings version of this initial arxiv submission.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 129 · 2026-05-26T10:24:49.862618+00:00_

Web search results for query: "Ranzato Chopra Auli Zaremba "Sequence Level Training with Recurrent Neural Networks" ICLR 2016 arXiv:1511.06732"

Links: [{"title":"[1511.06732] Sequence Level Training with Recurrent Neural Networks","url":"https://arxiv.org/abs/1511.06732"},{"title":"Published as a conference paper at ICLR 2016 SEQUENCE LEVEL TRAINING WITH","url":"https://michaelauli.github.io/papers/iclr2016_mixer.pdf"},{"title":"Sequence level training with recurrent neural networks - NYU Scholars","url":"https://nyuscholars.nyu.edu/en/publications/sequence-level-training-with-recurrent-neural-networks"},{"title":"Sequence Level Training with Recurrent Neural Networks","url":"https://arxiv.org/pdf/1511.06732"},{"title":"Sequence Level Training with Recurrent Neural Networks | Request PDF","url":"https://www.researchgate.net/publication/284476269_Sequence_Level_Training_with_Recurrent_Neural_Networks"},{"title":"dblp: Sequence Level Training with Recurrent Neural Networks.","url":"https://dblp.org/rec/journals/corr/RanzatoCAZ15.html"},{"title":"Sequence Level Training with Recurrent Neural Networks - Meta Research | Meta Research","url":"https://research.facebook.com/publications/sequence-level-training-with-recurrent-neural-networks/"},{"title":"Sequence Level Training with Recurrent Neural Networks | Facebook AI Research","url":"https://ai.meta.com/research/publications/sequence-level-training-with-recurrent-neural-networks/"},{"title":"Ranzato, et al. - Sequence Level Training with Recurrent Neural Networks (2016) - Machine Learning Papers - Quora","url":"https://mlpapers.quora.com/Ranzato-et-al-Sequence-Level-Training-with-Recurrent-Neural-Networks-2016"},{"title":"Untitled","url":"https://inria.hal.science/hal-01851612v1/html_references"}]

I found comprehensive information about this paper. Here are the search results:

## Paper Details

The paper "Sequence Level Training with Recurrent Neural Networks" was authored by Marc'Aurelio Ranzato, Sumit Chopra, Micha
…[truncated 909 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-26T10:24:49.862768+00:00_

Web search results for query: "He Zhang Zhou Glass "Quantifying Exposure Bias for Neural Language Generation" arXiv:1905.10617 2019"

Links: [{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"},{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Exposure-Bias-for-Neural-Language-He-Zhang/cbb1a1a80d26043867bb8bf2b7227c9139710ee5"},{"title":"[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v1"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/333418764_Quantifying_Exposure_Bias_for_Neural_Language_Generation"},{"title":"arXiv:1905.10617v10 [cs.LG] 3 Sep 2021","url":"https://arxiv.org/pdf/1905.10617"},{"title":"(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation","url":"https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"}]

I found the paper you're looking for. Here are the key details:

**Paper Information:**
- Authors: Tianxing He, Jingzhao Zhang, Zhiming Zhou, James Glass
- Title: "Quantifying Exposure Bias for Neural Language Generation"
- arXiv ID: 1905.10617
- Year: 2019

**Summary:**
The exposure bias problem refers to the training-generation discrepancy, caused by teacher forcing, in maximum likelihood estimation (MLE) training for auto-regressive neural network language models (LM). 

The paper proposes sequence-l
…[truncated 439 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-26T10:24:49.862918+00:00_

Web search results for query: "Leblond Alayrac Osokin Lacoste-Julien "SEARNN: Training RNNs with Global-Local Losses" ICLR 2018 arXiv:1706.04499"

Links: [{"title":"[1706.04499] SEARNN: Training RNNs with Global-Local Losses","url":"https://arxiv.org/abs/1706.04499"},{"title":"ICLR 2018 Schedule","url":"https://iclr.cc/Conferences/2018/Schedule?showEvent=191"},{"title":"SeaRNN: Training RNNs with Global-Local Losses - Inria - Institut national de recherche en sciences et technologies du numérique","url":"https://inria.hal.science/hal-01950555"},{"title":"[PDF] SEARNN: Training RNNs with Global-Local Losses | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SEARNN:-Training-RNNs-with-Global-Local-Losses-Leblond-Alayrac/345bbd344177815dfb9214c61403cb7eac6de450"},{"title":"SEARNN: Training RNNs with global-local losses","url":"https://www.di.ens.fr/~alayrac/papers/searnn_workshop.pdf"},{"title":"SeaRnn: Training RNNs with global-local losses","url":"https://www.jbalayrac.com/papers/searnn_workshop.pdf"},{"title":"GitHub - RemiLeblond/SeaRNN-open: Open source implementation of SeaRNN (ICLR 2018, https://openreview.net/forum?id=HkUR_y-RZ)","url":"https://github.com/RemiLeblond/SeaRNN-open"},{"title":"SEARNN: Training RNNs with global-local losses | OpenReview","url":"https://openreview.net/forum?id=HkUR_y-RZ"},{"title":"SEARNN: Training RNNs with Global-Local Losses | Papers With Code","url":"https://paperswithcode.com/paper/searnn-training-rnns-with-global-local-losses"},{"title":"6th International Conference on Learning Representations, ICLR 2018, Vancouver, BC, Canada, April 30 - May 3, 2018, Conference Track Proceedings - researchr publication","url":"https://researchr.org/publication/iclr-2018"}]

I found the paper you're looking for. Here's what I found:

## SEARNN: Training RNNs with Global-Local Losses

The paper "SeaRNN: Training RNNs with Global-Local Losses" was written by Rémi Leblond, Jean-Baptiste Alayrac, Anton Osokin, and Simon Lacoste-Julie
…[truncated 946 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-26T10:24:49.863069+00:00_

Web search results for query: "Wiseman Rush "Sequence-to-Sequence Learning as Beam-Search Optimization" EMNLP 2016 arXiv:1606.02960"

Links: [{"title":"[1606.02960] Sequence-to-Sequence Learning as Beam-Search Optimization","url":"https://arxiv.org/abs/1606.02960"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization","url":"https://arxiv.org/pdf/1606.02960"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization","url":"https://www.researchgate.net/publication/303879790_Sequence-to-Sequence_Learning_as_Beam-Search_Optimization"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization - ACL Anthology","url":"https://aclanthology.org/D16-1137/"},{"title":"[PDF] Sequence-to-Sequence Learning as Beam-Search Optimization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Sequence-to-Sequence-Learning-as-Beam-Search-Wiseman-Rush/5507dc32b368c8afd3b9507e9b5888da7bd7d7cd"},{"title":"Sequence-to-Sequence Learning as Beam-Search Optimization on ShortScience.org","url":"https://www.shortscience.org/paper?bibtexKey=journals%2Fcorr%2F1606.02960"},{"title":"GitHub - harvardnlp/BSO · GitHub","url":"https://github.com/harvardnlp/BSO"},{"title":"Beam Search Shahrzad Kiani and Zihao Chen CSC2547 Presentation","url":"https://duvenaud.github.io/learning-to-search/slides/week7/beam.pdf"},{"title":"Reinforcement Learning for on-line Sequence ...","url":"https://annals-csis.org/Volume_30/drp/70.html"}]

Based on the search results, here's information about this paper:

**Paper Details:**
"Sequence-to-Sequence Learning as Beam-Search Optimization" by Sam Wiseman and Alexander M. Rush was published in the Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing (pages 1296–1306, Austin, Texas). The paper addresses Sequence-to-Sequence (seq2seq) modeling as an important general-purpose NLP tool proven effective for many text-generation and sequence-labeling tasks.

**Main Contribution:**
The authors introduc
…[truncated 782 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 133 · 2026-05-26T10:24:49.863211+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Arora El Asri Bahuleyan Cheung \"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\" Findings ACL 2022 arXiv:2204.01171"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Arora El Asri Bahuleyan Cheung \"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\" Findings ACL 2022 arXiv:2204.01171"
  }
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-26T10:24:49.863334+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang Feng Meng You Liu \"Bridging the Gap between Training and Inference for Neural Machine Translation\" ACL 2019 arXiv:1906.02448"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang Feng Meng You Liu \"Bridging the Gap between Training and Inference for Neural Machine Translation\" ACL 2019 arXiv:1906.02448"
  }
}
```

</details>

---

### Tool call

_source line 135 · 2026-05-26T10:24:49.863483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Mihaylova Martins \"Scheduled Sampling for Transformers\" ACL 2019 Student Research Workshop aclanthology.org/P19-2049"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Mihaylova Martins \"Scheduled Sampling for Transformers\" ACL 2019 Student Research Workshop aclanthology.org/P19-2049"
  }
}
```

</details>

---

### Tool call

_source line 136 · 2026-05-26T10:24:49.863602+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dou Lu Efiong Gales \"Attention Forcing for Sequence-to-sequence Model Training\" arXiv:1909.12289 2019"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dou Lu Efiong Gales \"Attention Forcing for Sequence-to-sequence Model Training\" arXiv:1909.12289 2019"
  }
}
```

</details>

---

### Tool call

_source line 137 · 2026-05-26T10:24:49.863714+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dou Gales \"Parallel Attention Forcing for Machine Translation\" arXiv:2211.03237 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dou Gales \"Parallel Attention Forcing for Machine Translation\" arXiv:2211.03237 2022"
  }
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-26T10:24:49.863845+00:00_

Web search results for query: "Arora El Asri Bahuleyan Cheung "Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation" Findings ACL 2022 arXiv:2204.01171"

Links: [{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of...","url":"https://arxiv.org/abs/2204.01171"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error","url":"https://arxiv.org/pdf/2204.01171"},{"title":"[PDF] Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Why-Exposure-Bias-Matters:-An-Imitation-Learning-of-Arora-Asri/0e3d6a7c9c04cf3ba9c902724548846a5ade04b4"},{"title":"(PDF) Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation","url":"https://www.researchgate.net/publication/359729383_Why_Exposure_Bias_Matters_An_Imitation_Learning_Perspective_of_Error_Accumulation_in_Language_Generation"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - McGill NLP","url":"https://mcgill-nlp.github.io/publications/2204.01171/"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - ACL Anthology","url":"https://aclanthology.org/2022.findings-acl.58/"},{"title":"A Survey of Hallucination Problems Based on Large Language Models","url":"https://ace.ewapub.com/article/view/17851"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/why-exposure-bias-matters-an-imitation-learning-perspective-of-error-accumulation-in-language-generation/"},{"title":"Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation | Request PDF","url":"https:/
…[truncated 1255 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 139 · 2026-05-26T10:24:49.864002+00:00_

Web search results for query: "Zhang Feng Meng You Liu "Bridging the Gap between Training and Inference for Neural Machine Translation" ACL 2019 arXiv:1906.02448"

Links: [{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/P19-1426/"},{"title":"GitHub - ictnlp/OR-NMT: Source Code for ACL2019 paper &lt;Bridging the Gap between Training and Inference for Neural Machine Translation>","url":"https://github.com/ictnlp/OR-NMT"},{"title":"[1906.02448] Bridging the Gap between Training and Inference for Neural Machine Translation","url":"https://arxiv.org/abs/1906.02448"},{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190602448Z/abstract"},{"title":"[PDF] Bridging the Gap between Training and Inference for Neural Machine Translation (Extended Abstract) | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Bridging-the-Gap-between-Training-and-Inference-for-Zhang-Feng/773f171388d42ea7878b00f6778c2dabd9a012b8"},{"title":"Bridging the Gap between Training and Inference for ...","url":"https://aclanthology.org/P19-1426.pdf"},{"title":"Bridging the Gap between Training and Inference for ...","url":"https://cs.uwaterloo.ca/~mli/Ng.pdf"},{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation | Request PDF","url":"https://www.researchgate.net/publication/335778783_Bridging_the_Gap_between_Training_and_Inference_for_Neural_Machine_Translation"},{"title":"Bridging the Gap between Training and Inference for Neural Machine Translation∗","url":"https://www.ijcai.org/proceedings/2020/0667.pdf"}]

I found the paper you're looking for! Here are the key details:

**Publication Information:**
The paper "Bridging the Gap between Training and Inference for Neural Machine Translation" was authored by Wen Zhang, Yang Feng, Fandong Meng, Di You, and Qun Liu, and published 
…[truncated 1115 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 140 · 2026-05-26T10:24:49.864153+00:00_

Web search results for query: "Mihaylova Martins "Scheduled Sampling for Transformers" ACL 2019 Student Research Workshop aclanthology.org/P19-2049"

Links: [{"title":"Scheduled Sampling for Transformers - ACL Anthology","url":"https://aclanthology.org/P19-2049/"},{"title":"[1906.07651] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651"},{"title":"GitHub - deep-spin/scheduled-sampling-transformers: Code for the paper \"Scheduled Sampling for Transformers\"","url":"https://github.com/deep-spin/scheduled-sampling-transformers"},{"title":"Scheduled Sampling for Transformers | Papers With Code","url":"https://paperswithcode.com/paper/scheduled-sampling-for-transformers"},{"title":"[PDF] Scheduled Sampling for Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-Sampling-for-Transformers-Mihaylova-Martins/6b6befbff611ddc98ef268b3c51353593bb07e77"},{"title":"Scheduled Sampling for Transformers | Request PDF","url":"https://www.researchgate.net/publication/335784238_Scheduled_Sampling_for_Transformers"},{"title":"[1906.07651v1] Scheduled Sampling for Transformers","url":"https://arxiv.org/abs/1906.07651v1"},{"title":"2019 ACL Student Research Workshop - Accepted Papers","url":"https://sites.google.com/view/acl19studentresearchworkshop/accepted-papers"},{"title":"Tsvetomila Mihaylova - ACL Anthology","url":"https://www.aclweb.org/anthology/people/t/tsvetomila-mihaylova/"}]

I found the paper successfully! Here's the information about "Scheduled Sampling for Transformers":

**"Scheduled Sampling for Transformers"** is a paper by Tsvetomila Mihaylova and André F. T. Martins, published in the Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: Student Research Workshop in 2019, pages 351–356, Florence, Italy.

**Paper Summary:**

The paper addresses scheduled sampling as a technique for avoiding exposure bias in sequence-to-sequence generation. The technique consists of feeding t
…[truncated 929 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-26T10:24:49.864301+00:00_

Web search results for query: "Dou Lu Efiong Gales "Attention Forcing for Sequence-to-sequence Model Training" arXiv:1909.12289 2019"

Links: [{"title":"[1909.12289] Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/abs/1909.12289"},{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"Attention Forcing for Machine Translation","url":"https://arxiv.org/pdf/2104.01264"},{"title":"[2104.01264] Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2104.01264"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"ISCA Archive - Attention Forcing for Speech Synthesis","url":"https://www.isca-archive.org/interspeech_2020/dou20_interspeech.html"},{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"}]

I found information about the paper you're searching for. Here are the details:

The paper "Attention Forcing for Sequence-to-sequence Model Training" (arXiv:1909.12289) was authored by Qingyun Dou, Yiting Lu, Joshua Efiong, and Mark J. F. Gales, published in 2019.

The paper addresses auto-regressive sequence-to-sequence models with attention mechanisms that have achieved state-of-the-art performance in tasks such as machine translation and speech synthesis. The paper introduces attention forcing, which guides the model with generated output history and reference attention, allowing the model to train to recover from its mistakes in a stable fashion without requiring a schedule or a classifier.

The paper is available on arXiv at https://arxiv.org/abs/1909.12289.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-26T10:24:49.864453+00:00_

Web search results for query: "Dou Gales "Parallel Attention Forcing for Machine Translation" arXiv:2211.03237 2022"

Links: [{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Parallel Attention Mechanisms in Neural Machine Translation","url":"https://arxiv.org/pdf/1810.12427"},{"title":"Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/pdf/1909.12289"},{"title":"Attention Is All You Need","url":"https://arxiv.org/pdf/1706.03762"}]

I found the paper you're looking for! Here are the search results:

The paper "Parallel Attention Forcing for Machine Translation" is by Qingyun Dou and Mark Gales, with arXiv identifier 2211.03237. The paper introduces attention forcing to address the mismatch between training with reference back-history and inference with generated back-history.

The paper introduces two extensions of attention forcing: (1) Scheduled attention forcing, which automatically turns attention forcing on and off, essential for tasks with discrete outputs. 

The paper was published on November 6, 2022. You can access the full paper at:
- **Abstract**: https://arxiv.org/abs/2211.03237
- **PDF**: https://arxiv.org/pdf/2211.03237


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 143 · 2026-05-26T10:24:49.864593+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1610.09038 \"Professor Forcing\" author order Lamb Goyal first author NeurIPS 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1610.09038 \"Professor Forcing\" author order Lamb Goyal first author NeurIPS 2016"
  }
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-26T10:24:49.864715+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1905.10617 \"Quantifying Exposure Bias\" He Zhang Zhou Glass published conference journal venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1905.10617 \"Quantifying Exposure Bias\" He Zhang Zhou Glass published conference journal venue"
  }
}
```

</details>

---

### Tool call

_source line 145 · 2026-05-26T10:24:49.864829+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1909.12289 \"Attention Forcing\" Dou Lu Efiong Gales published conference venue ICLR 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1909.12289 \"Attention Forcing\" Dou Lu Efiong Gales published conference venue ICLR 2020"
  }
}
```

</details>

---

### Tool call

_source line 146 · 2026-05-26T10:24:49.864941+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2211.03237 \"Parallel Attention Forcing\" Dou Gales published conference journal venue 2022 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2211.03237 \"Parallel Attention Forcing\" Dou Gales published conference journal venue 2022 2023"
  }
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-26T10:24:49.865053+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 148 · 2026-05-26T10:24:49.865164+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-26T10:24:49.865273+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Yu Tianhe Kumar Saurabh \"Gradient Surgery for Multi-Task Learning\" NeurIPS 2020 arXiv 2001.06782"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Yu Tianhe Kumar Saurabh \"Gradient Surgery for Multi-Task Learning\" NeurIPS 2020 arXiv 2001.06782"
  }
}
```

</details>

---

### Tool result

_source line 150 · 2026-05-26T10:24:49.865398+00:00_

Web search results for query: "Yu Tianhe Kumar Saurabh "Gradient Surgery for Multi-Task Learning" NeurIPS 2020 arXiv 2001.06782"

Links: [{"title":"Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/pdf/2001.06782"},{"title":"Gradient Surgery for Multi-Task Learning","url":"https://papers.nips.cc/paper/2020/hash/3fe78a8acf5fda99de95303940a2420c-Abstract.html"},{"title":"[2001.06782] Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/abs/2001.06782"},{"title":"Tianhe Kevin Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, Chelsea Finn · Gradient Surgery for Multi-Task Learning","url":"https://slideslive.com/38935965/gradient-surgery-for-multitask-learning"},{"title":"Review for NeurIPS paper: Gradient Surgery for Multi-Task Learning","url":"https://proceedings.neurips.cc/paper/2020/file/3fe78a8acf5fda99de95303940a2420c-Review.html"},{"title":"Gradient Surgery for Multi-Task Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200106782Y/abstract"},{"title":"Yu Et Al. - 2020 - Gradient Surgery for Multi-Task Learning","url":"https://www.scribd.com/document/558287008/Yu-Et-Al-2020-Gradient-Surgery-for-Multi-Task-Learning"},{"title":"NeurIPS 2020 : Gradient Surgery for Multi-Task Learning","url":"https://nips.cc/virtual/2020/public/poster_3fe78a8acf5fda99de95303940a2420c.html"},{"title":"Gradient surgery for multi-task learning | Proceedings of the 34th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3495724.3496213"}]

I found the paper you're looking for. Here's what I discovered:

"Gradient Surgery for Multi-Task Learning" was authored by Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn from Stanford University, UC Berkeley, and Robotics at Google.

The paper w
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 151 · 2026-05-26T10:24:49.865563+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Chen Zhao Badrinarayanan \"GradNorm: Gradient Normalization for Adaptive Loss Balancing\" ICML 2018 arXiv 1711.02257"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Chen Zhao Badrinarayanan \"GradNorm: Gradient Normalization for Adaptive Loss Balancing\" ICML 2018 arXiv 1711.02257"
  }
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-26T10:24:49.865692+00:00_

Web search results for query: "Chen Zhao Badrinarayanan "GradNorm: Gradient Normalization for Adaptive Loss Balancing" ICML 2018 arXiv 1711.02257"

Links: [{"title":"[1711.02257] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss ...","url":"https://arxiv.org/pdf/1711.02257"},{"title":"(PDF) GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://www.researchgate.net/publication/320920333_GradNorm_Gradient_Normalization_for_Adaptive_Loss_Balancing_in_Deep_Multitask_Networks"},{"title":"Gradnorm: Gradient Normalization For Adaptive Loss Balancing in Deep Multitask Networks | PDF | Image Segmentation | Computer Science","url":"https://www.scribd.com/document/615850392/1711-02257"},{"title":"GradNorm: Gradient Normalization for Adaptive","url":"https://arxiv.org/pdf/1711.02257v3"},{"title":"[1711.02257v4] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257v4"},{"title":"[1711.02257v2] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257v2"},{"title":"[1711.02257v3] GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks","url":"https://arxiv.org/abs/1711.02257v3"},{"title":"GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2017arXiv171102257C/abstract"}]

I found the paper you were looking for. Here are the search results:

The paper "GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks" was authored by Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, and Andrew Rabinovich, with arXiv identifier 1711.02257.

The paper presents a gradient normalization (GradNorm) algorithm that automatic
…[truncated 591 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 153 · 2026-05-26T10:24:49.865824+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Liu Bo Liu Xingchao \"Conflict-Averse Gradient Descent for Multi-task Learning\" NeurIPS 2021 arXiv 2110.14048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Liu Bo Liu Xingchao \"Conflict-Averse Gradient Descent for Multi-task Learning\" NeurIPS 2021 arXiv 2110.14048"
  }
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-26T10:24:49.865944+00:00_

Web search results for query: "openreview "Mixture-of-Depths" Raposo ICLR 2025 OR ICML 2024"

Links: [{"title":"Aikipedia: Mixture of Depths – Champaign Magazine","url":"https://champaignmagazine.com/2025/11/03/aikipedia-mixture-of-depths/"},{"title":"A Comprehensive Survey of Mixture-of-Experts: Algorithms, Theory, and Applications","url":"https://arxiv.org/pdf/2503.07137"},{"title":"MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models","url":"https://arxiv.org/pdf/2512.12121"},{"title":"DA-MoE: Addressing Depth-Sensitivity in Graph-Level Analysis through   Mixture of Experts","url":"https://arxiv.org/pdf/2411.03025"},{"title":"Attention Is All You Need For Mixture-of-Depths Routing","url":"https://arxiv.org/pdf/2412.20875"}]

Based on the search results, the Mixture-of-Depths paper was published at ICML 2024 (International Conference on Machine Learning). The paper is authored by Raposo, D., Ritter, S., Richards, B., Lillicrap, T., Humphreys, P., & Santoro, A. (2024) and is titled "Mixture-of-Depths: Dynamically allocating compute in transformer-based language models". It also appeared on arXiv as 2404.02258.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 155 · 2026-05-26T10:24:49.866092+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify citations group 5",
  "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **zhang2020dialogpt**: Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill. \"DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation\". ACL 2020 System Demonstrations. arXiv:1911.00536.\n\n2. **roller2021recipes**: Roller, Stephen and Dinan, Emily and Goyal, Naman and Ju, Da and Williamson, Mary and Liu, Yinhan and Xu, Jing and Ott, Myle and Smith, Eric Michael and Boureau, Y-Lan and Weston, Jason. \"Recipes for Building an Open-Domain Chatbot\". EACL 2021. arXiv:2004.13637.\n\n3. **zheng2024judging**: Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion. \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\". NeurIPS 2023 (NOTE: bib key says 2024 but year field says 2023). arXiv:2306.05685.\n\n4. **clark2019what**: Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D. \"What Does BERT Look At? An Analysis of BERT's Attention\". ACL 2019 BlackboxNLP Workshop. arXiv:1906.04341.\n\n5. **voita2019analyzing**: Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan. \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\". ACL 2019. arXiv:1905.09418.\n\n6. **kovaleva2019revealing**: Kovaleva, Olga and Romanov, Alexey and Rogers, Anna and Rumshisky, Anna. \"Revealing the Dark Secrets of BERT\". EMNLP 2019. arXiv:1908.08593.\n\n7. **liu2024lost**: Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy. \"Lost in the Middle: How Language Models Use Long Contexts\". TACL 2024. arXiv:2307.03172.\n\n8. **li2016persona**: Li, Jiwei and Galley, Michel and Brockett, Chris and Spithourakis, Georgios and Gao, Jianfeng and Dolan, Bill. \"A Persona-Based Neural Conversation Model\". ACL 2016, pp 994-1003. URL: https://aclanthology.org/P16-1094/\n\n9. **xu2022goldfish**: Xu, Jing and Szlam, Arthur and Weston, Jason. \"Beyond Goldfish Memory: Long-Term Open-Domain Conversation\". ACL 2022, pp 5180-5197. URL: https://aclanthology.org/2022.acl-long.356/\n\n10. **vig2019multiscale**: Vig, Jesse. \"A Multiscale Visualization of Attention in the Transformer Model\". ACL 2019 System Demonstrations, pp 37-42. URL: https://aclanthology.org/P19-3007/\n\n11. **abnar2020quantifying**: Abnar, Samira and Zuidema, Willem. \"Quantifying Attention Flow in Transformers\". ACL 2020, pp 4190-4197. URL: https://aclanthology.org/2020.acl-main.385/\n\n12. **ethayarajh2019contextual**: Ethayarajh, Kawin. \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\". EMNLP 2019, pp 55-65. URL: https://aclanthology.org/D19-1006/\n\n13. **brunner2020identifiability**: Brunner, Gino and Liu, Yang and Pascual, Damian and Richter, Oliver and Ciaramita, Massimiliano and Krause, Andreas. \"On Identifiability in Transformers\". ICLR 2020. arXiv:1908.04211.\n\n14. **ding2023ultrachat**: Ding, Ning and Chen, Yulin and Xu, Bokai and Qin, Yujia and Zheng, Zhi and Hu, Shengding and Liu, Zhiyuan and Sun, Maosong and Zhou, Bowen. \"Enhancing Chat Language Models by Scaling High-quality Instructional Conversations\". EMNLP 2023. arXiv:2305.14233.\n\n15. **grattafiori2024llama3**: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and others. \"The Llama 3 Herd of Models\". arXiv:2407.21783, 2024.\n\nSearch each one individually using WebSearch. Be thorough."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify citations group 5",
    "prompt": "You are verifying academic citations for a paper. For each citation below, use WebSearch to verify:\n1. Paper exists (real vs hallucinated)\n2. Authors correct\n3. Year correct\n4. Title exact match\n5. Venue correct\n6. If arXiv, check if published at a conference/journal (should cite published version)\n7. arXiv ID correct\n\nReport findings in this format per entry:\n### [bib_key] Author (Year) — Title\n- Exists: ✓/✗\n- Authors: ✓/✗ (detail if wrong)\n- Year: ✓/✗ (detail if wrong)\n- Title: ✓/✗ (detail if wrong)\n- Venue: ✓/✗ (detail if wrong)\n- arXiv→published upgrade needed: Yes/No (detail)\n- Notes: ...\n\nHere are the citations to verify:\n\n1. **zhang2020dialogpt**: Zhang, Yizhe and Sun, Siqi and Galley, Michel and Chen, Yen-Chun and Brockett, Chris and Gao, Xiang and Gao, Jianfeng and Liu, Jingjing and Dolan, Bill. \"DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation\". ACL 2020 System Demonstrations. arXiv:1911.00536.\n\n2. **roller2021recipes**: Roller, Stephen and Dinan, Emily and Goyal, Naman and Ju, Da and Williamson, Mary and Liu, Yinhan and Xu, Jing and Ott, Myle and Smith, Eric Michael and Boureau, Y-Lan and Weston, Jason. \"Recipes for Building an Open-Domain Chatbot\". EACL 2021. arXiv:2004.13637.\n\n3. **zheng2024judging**: Zheng, Lianmin and Chiang, Wei-Lin and Sheng, Ying and Zhuang, Siyuan and Wu, Zhanghao and Zhuang, Yonghao and Lin, Zi and Li, Zhuohan and Li, Dacheng and Xing, Eric P. and Zhang, Hao and Gonzalez, Joseph E. and Stoica, Ion. \"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\". NeurIPS 2023 (NOTE: bib key says 2024 but year field says 2023). arXiv:2306.05685.\n\n4. **clark2019what**: Clark, Kevin and Khandelwal, Urvashi and Levy, Omer and Manning, Christopher D. \"What Does BERT Look At? An Analysis of BERT's Attention\". ACL 2019 BlackboxNLP Workshop. arXiv:1906.04341.\n\n5. **voita2019analyzing**: Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan. \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\". ACL 2019. arXiv:1905.09418.\n\n6. **kovaleva2019revealing**: Kovaleva, Olga and Romanov, Alexey and Rogers, Anna and Rumshisky, Anna. \"Revealing the Dark Secrets of BERT\". EMNLP 2019. arXiv:1908.08593.\n\n7. **liu2024lost**: Liu, Nelson F. and Lin, Kevin and Hewitt, John and Paranjape, Ashwin and Bevilacqua, Michele and Petroni, Fabio and Liang, Percy. \"Lost in the Middle: How Language Models Use Long Contexts\". TACL 2024. arXiv:2307.03172.\n\n8. **li2016persona**: Li, Jiwei and Galley, Michel and Brockett, Chris and Spithourakis, Georgios and Gao, Jianfeng and Dolan, Bill. \"A Persona-Based Neural Conversation Model\". ACL 2016, pp 994-1003. URL: https://aclanthology.org/P16-1094/\n\n9. **xu2022goldfish**: Xu, Jing and Szlam, Arthur and Weston, Jason. \"Beyond Goldfish Memory: Long-Term Open-Domain Conversation\". ACL 2022, pp 5180-5197. URL: https://aclanthology.org/2022.acl-long.356/\n\n10. **vig2019multiscale**: Vig, Jesse. \"A Multiscale Visualization of Attention in the Transformer Model\". ACL 2019 System Demonstrations, pp 37-42. URL: https://aclanthology.org/P19-3007/\n\n11. **abnar2020quantifying**: Abnar, Samira and Zuidema, Willem. \"Quantifying Attention Flow in Transformers\". ACL 2020, pp 4190-4197. URL: https://aclanthology.org/2020.acl-main.385/\n\n12. **ethayarajh2019contextual**: Ethayarajh, Kawin. \"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings\". EMNLP 2019, pp 55-65. URL: https://aclanthology.org/D19-1006/\n\n13. **brunner2020identifiability**: Brunner, Gino and Liu, Yang and Pascual, Damian and Richter, Oliver and Ciaramita, Massimiliano and Krause, Andreas. \"On Identifiability in Transformers\". ICLR 2020. arXiv:1908.04211.\n\n14. **ding2023ultrachat**: Ding, Ning and Chen, Yulin and Xu, Bokai and Qin, Yujia and Zheng, Zhi and Hu, Shengding and Liu, Zhiyuan and Sun, Maosong and Zhou, Bowen. \"Enhancing Chat Language Models by Scaling High-quality Instructional Conversations\". EMNLP 2023. arXiv:2305.14233.\n\n15. **grattafiori2024llama3**: Grattafiori, Aaron and Dubey, Abhimanyu and Jauhri, Abhinav and Pandey, Abhinav and Kadian, Abhishek and Al-Dahle, Ahmad and others. \"The Llama 3 Herd of Models\". arXiv:2407.21783, 2024.\n\nSearch each one individually using WebSearch. Be thorough."
  }
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-26T10:24:49.866310+00:00_

Web search results for query: "arxiv 1505.00387 "Highway Networks" "ICML 2015 Deep Learning Workshop" published venue"

Links: [{"title":"[1505.00387] Highway Networks","url":"https://arxiv.org/abs/1505.00387"},{"title":"Highway Networks Rupesh Kumar Srivastava RUPESH@IDSIA.CH Klaus Greff","url":"https://arxiv.org/pdf/1505.00387"},{"title":"[1505.00387v2] Highway Networks","url":"https://arxiv.org/abs/1505.00387v2"},{"title":"[1505.00387] Highway Networks","url":"http://export.arxiv.org/abs/1505.00387"},{"title":"Highway Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150500387S/abstract"},{"title":"[1505.00387] Highway Networks - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/1505.00387"},{"title":"(PDF) Highway Networks","url":"https://www.researchgate.net/publication/275897262_Highway_Networks"},{"title":"Recurrent Highway Networks","url":"https://proceedings.mlr.press/v70/zilly17a/zilly17a.pdf"},{"title":"[1607.03474] Recurrent Highway Networks","url":"https://ar5iv.labs.arxiv.org/html/1607.03474"},{"title":"Highway Value Iteration Networks","url":"https://arxiv.org/html/2406.03485v1"}]

Based on the search results, I found the information about the published venue for arxiv 1505.00387 "Highway Networks":

The paper was presented at ICML 2015 Deep Learning workshop. Additionally, according to the search results, the full paper is at arXiv:1507.06228, suggesting that the extended abstract (1505.00387) was later published as a more complete version.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-26T10:24:49.866476+00:00_

Web search results for query: "arxiv 1610.09038 "Professor Forcing" author order Lamb Goyal first author NeurIPS 2016"

Links: [{"title":"[1610.09038] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://arxiv.org/abs/1610.09038"},{"title":"[1610.09038v1] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://arxiv.org/abs/1610.09038v1"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks Alex Lamb*","url":"https://arxiv.org/pdf/1610.09038"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks : Alex Lamb : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/arxiv-1610.09038"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2016arXiv161009038L/abstract"},{"title":"(PDF) Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://www.researchgate.net/publication/309551292_Professor_Forcing_A_New_Algorithm_for_Training_Recurrent_Networks"},{"title":"(PDF) Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://www.academia.edu/92050492/Professor_Forcing_A_New_Algorithm_for_Training_Recurrent_Networks"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks on ShortScience.org","url":"https://shortscience.org/paper?a=guest&bibtexKey=journals%2Fcorr%2F1610.09038"},{"title":"[PDF] Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/db38edba294b7d2fd8ca3aad65721bd9dce32619"},{"title":"a2c [1610.09038] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://michin7.org/1610.09038"}]

Based on the search results, I found information about the "Professor Forcing" paper (arxiv 1610.09038):

**Author Order:** The authors are Al
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-26T10:24:49.866636+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 159 · 2026-05-26T10:24:49.866756+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-26T10:24:49.866881+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"Mixture-of-Depths\" Raposo WwpYSOkkCt ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"Mixture-of-Depths\" Raposo WwpYSOkkCt ICLR 2025"
  }
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-26T10:24:49.867009+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "semanticscholar \"Highway Networks\" Srivastava 1505.00387 venue \"ICML 2015 Deep Learning Workshop\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "semanticscholar \"Highway Networks\" Srivastava 1505.00387 venue \"ICML 2015 Deep Learning Workshop\""
  }
}
```

</details>

---

### Tool result

_source line 162 · 2026-05-26T10:24:49.867135+00:00_

Web search results for query: "arxiv 1905.10617 "Quantifying Exposure Bias" He Zhang Zhou Glass published conference journal venue"

Links: [{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"},{"title":"[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v1"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Request PDF","url":"https://www.researchgate.net/publication/333418764_Quantifying_Exposure_Bias_for_Neural_Language_Generation"},{"title":"arXiv:1905.10617v10 [cs.LG] 3 Sep 2021","url":"https://arxiv.org/pdf/1905.10617"},{"title":"Quantifying Exposure Bias for Neural Language Generation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Exposure-Bias-for-Neural-Language-He-Zhang/cbb1a1a80d26043867bb8bf2b7227c9139710ee5"},{"title":"[PDF] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exposure-Bias-versus-Self-Recovery:-Are-Distortions-He-Zhang/cb51b53d5d26537ed6d458f83b81afe0f2efa289"}]

Based on the search results, here's what I found about arxiv 1905.10617:

**Paper Details:**
The paper is titled "Quantifying Exposure Bias for Neural Language Generation" by authors Tianxing He, Jingzhao Zhang, Zhiming Zhou, and James Glass.

**Publication Information:**
The paper appears to be a preprint published on arxiv. According to Semantic Scholar, it was published in ArXiv in 2019, with the original submission date being May 25, 2019.

**Content:**
The paper addresses the exposure bias probl
…[truncated 652 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-26T10:24:49.867287+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qiu Zihan \"Gated Attention\" NeurIPS 2025 oral best paper authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qiu Zihan \"Gated Attention\" NeurIPS 2025 oral best paper authors full list"
  }
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-26T10:24:49.867445+00:00_

Web search results for query: "Liu Bo Liu Xingchao "Conflict-Averse Gradient Descent for Multi-task Learning" NeurIPS 2021 arXiv 2110.14048"

Links: [{"title":"Conflict-Averse Gradient Descent for Multi-task learning","url":"https://proceedings.neurips.cc/paper/2021/hash/9d27fdf2477ffbff837d73ef7ae23db9-Abstract.html"},{"title":"NeurIPS Poster Conflict-Averse Gradient Descent for Multi-task learning","url":"https://neurips.cc/virtual/2021/poster/27328"},{"title":"Peter Stone: Conflict-Averse Gradient Descent for Multi-task learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-NeurIPS2021-Liu.html"},{"title":"[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/abs/2110.14048"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html-links/NeurIPS2021-Liu.pdf"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning [Quick Review]","url":"https://liner.com/review/conflictaverse-gradient-descent-for-multitask-learning"},{"title":"Conflict-Averse Gradient Descent for Multi-task learning | OpenReview","url":"https://openreview.net/forum?id=_61Qh8tULj_"},{"title":"NeurIPS 2021","url":"https://neurips.cc/Conferences/2021/ScheduleMultitrack?event=26653"},{"title":"Conflict-Averse Gradient Descent for Multi-task learning - researchr publication","url":"https://researchr.org/publication/LiuLJSL21"}]

I've found comprehensive information about this paper. Here are the search results:

## Paper Overview

The paper "Conflict-Averse Gradient Descent for Multi-task learning" was authored by Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, and Qiang Liu, and presented at NeurIPS 2021.

## Main Contribution

The paper introduces Conflict-Averse Gradient descent (CAGrad) which minimizes the average loss function while leveraging the worst local improvement of individual tasks to regularize the algorithm trajectory. CAGrad balances the objectives 
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-26T10:24:49.867602+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DialoGPT Large-Scale Generative Pre-training Conversational Response Generation Zhang 2020 ACL arXiv:1911.00536"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DialoGPT Large-Scale Generative Pre-training Conversational Response Generation Zhang 2020 ACL arXiv:1911.00536"
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-26T10:24:49.867732+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Laban 2505.06120 \"LLMs Get Lost\" published ICLR 2026 NeurIPS 2025 conference accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Laban 2505.06120 \"LLMs Get Lost\" published ICLR 2026 NeurIPS 2025 conference accepted"
  }
}
```

</details>

---

### Tool result

_source line 167 · 2026-05-26T10:24:49.867868+00:00_

Web search results for query: "arxiv 1909.12289 "Attention Forcing" Dou Lu Efiong Gales published conference venue ICLR 2020"

Links: [{"title":"[1909.12289] Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/abs/1909.12289"},{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"},{"title":"Attention Needs to Focus: A Unified Perspective on Attention Allocation","url":"https://arxiv.org/html/2601.00919v1"},{"title":"[2104.01264] Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2104.01264"},{"title":"Efficient Attention Mechanisms for Large Language Models: A Survey","url":"https://arxiv.org/html/2507.19595v1"},{"title":"Towards understanding how attention mechanism works in deep learning","url":"https://arxiv.org/html/2412.18288v1"},{"title":"Attention Optimization","url":"https://www.aussieai.com/research/attention"},{"title":"[2601.00919] Attention Needs to Focus: A Unified Perspective on Attention Allocation","url":"https://arxiv.org/abs/2601.00919"},{"title":"Attention in Diffusion Model: A Survey","url":"https://arxiv.org/html/2504.03738v1"}]

Based on the search results, I found information about the paper arxiv 1909.12289:

The paper is titled "Attention Forcing for Sequence-to-sequence Model Training" by authors Qingyun Dou, Yiting Lu, Joshua Efiong, and Mark J. F. Gales. (Note: The author name in the search results is "Yiting Lu," not "Efiong" as an author—Efiong is Joshua Efiong, a co-author.)

The paper introduces attention forcing, which guides the model with generated output history and reference attention, enabling the model to recover from its mistakes in a stable fashion without requiring a schedule or a classifier.

The paper was posted to arXiv on October 2, 2019. According to the OpenRev
…[truncated 426 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-26T10:24:49.868020+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Recipes for Building an Open-Domain Chatbot Roller 2021 EACL arXiv:2004.13637"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Recipes for Building an Open-Domain Chatbot Roller 2021 EACL arXiv:2004.13637"
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-26T10:24:49.868146+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Judging LLM-as-a-Judge MT-Bench Chatbot Arena Zheng NeurIPS 2023 arXiv:2306.05685"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Judging LLM-as-a-Judge MT-Bench Chatbot Arena Zheng NeurIPS 2023 arXiv:2306.05685"
  }
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-26T10:24:49.868271+00:00_

Web search results for query: "arxiv 2211.03237 "Parallel Attention Forcing" Dou Gales published conference journal venue 2022 2023"

Links: [{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Parallel Attention Forcing for Machine Translation","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2211.03237"},{"title":"Fast attention mechanisms: a tale of parallelism","url":"https://arxiv.org/pdf/2509.09001"},{"title":"Generalized Neighborhood Attention: Multi-dimensional Sparse Attention at the Speed of Light","url":"https://arxiv.org/html/2504.16922v1"},{"title":"A foundation model with multi-variate parallel attention to ...","url":"https://arxiv.org/pdf/2506.20354"},{"title":"Attention Mechanisms in Neural Networks A Comprehensive Mathematical Treatment From Theory to Implementation","url":"https://arxiv.org/html/2601.03329v1"},{"title":"Hardware-Efficient Attention for Fast Decoding","url":"https://arxiv.org/html/2505.21487v1"}]

Based on the search results, here's what I found about arxiv 2211.03237:

**Paper Details:**
- Title: "Parallel Attention Forcing for Machine Translation" by Qingyun Dou and Mark Gales
- ArXiv ID: 2211.03237, published November 6, 2022

**Paper Summary:**
The paper addresses challenges in training attention-based autoregressive models, noting that while teacher forcing guides models with reference back-history during training, during inference generated back-history must be used, causing a mismatch that limits evaluation performance. Attention forcing has been introduced to address this by guiding the model with both generated back-history and reference attention.

**Regarding Conference/Journal Publication:**
The search results show this is an arXiv preprint from November 2022, but the results do not contain information about whether thi
…[truncated 364 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 171 · 2026-05-26T10:24:49.868438+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "What Does BERT Look At Analysis of BERT's Attention Clark 2019 ACL BlackboxNLP arXiv:1906.04341"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "What Does BERT Look At Analysis of BERT's Attention Clark 2019 ACL BlackboxNLP arXiv:1906.04341"
  }
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-26T10:24:49.868573+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Voita 2019 ACL arXiv:1905.09418"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Voita 2019 ACL arXiv:1905.09418"
  }
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-26T10:24:49.868695+00:00_

Web search results for query: "openreview.net "Mixture-of-Depths" Raposo WwpYSOkkCt ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=WwpYSOkkCt"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/56aa4f45f74423431c41dd1c6a97a523330e36ba.pdf"},{"title":"Attention Is All You Need For Mixture-of-Depths Routing | OpenReview","url":"https://openreview.net/forum?id=jIAKjjEmWi"},{"title":"MixtureKit: A General Framework for Composing, Training, and Visualizing Mixture-of-Experts Models","url":"https://arxiv.org/pdf/2512.12121"},{"title":"DA-MoE: Addressing Depth-Sensitivity in Graph-Level Analysis through   Mixture of Experts","url":"https://arxiv.org/pdf/2411.03025"}]

The search was successful. I found the paper you're looking for:

The paper "Mixture-of-Depths: Dynamically allocating compute in transformer-based language models" by David Raposo, Samuel Ritter, Blake A. Richards, Timothy P. Lillicrap, Peter Conway Humphreys, and Adam Santoro is published as a conference paper at ICLR 2025.

The paper is available at the OpenReview link: https://openreview.net/pdf?id=WwpYSOkkCt

The work focuses on dynamically allocating compute in transformer-based language models, and the authors propose Continuous Depthwise Batching, a promising new inference paradigm enabled by this approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 174 · 2026-05-26T10:24:49.868833+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Navon Aviv Shamsian \"Multi-Task Learning as a Bargaining Game\" ICML 2022 arXiv 2202.01017"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Navon Aviv Shamsian \"Multi-Task Learning as a Bargaining Game\" ICML 2022 arXiv 2202.01017"
  }
}
```

</details>

---

### Tool call

_source line 175 · 2026-05-26T10:24:49.868959+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1905.10617 latest version title \"Exposure Bias versus Self-Recovery\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1905.10617 latest version title \"Exposure Bias versus Self-Recovery\""
  }
}
```

</details>

---

### Tool call

_source line 176 · 2026-05-26T10:24:49.869095+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview \"Attention Forcing for Sequence-to-sequence Model Training\" rJe5_CNtPB ICLR rejected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview \"Attention Forcing for Sequence-to-sequence Model Training\" rJe5_CNtPB ICLR rejected"
  }
}
```

</details>

---

### Tool call

_source line 177 · 2026-05-26T10:24:49.869222+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Professor Forcing\" NeurIPS 2016 author order \"Goyal, Lamb\" OR \"Lamb, Goyal\" proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Professor Forcing\" NeurIPS 2016 author order \"Goyal, Lamb\" OR \"Lamb, Goyal\" proceedings"
  }
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-26T10:24:49.869348+00:00_

Web search results for query: "Qiu Zihan "Gated Attention" NeurIPS 2025 oral best paper authors full list"

Links: [{"title":"GitHub - qiuzh20/gated_attention: The official implementation for [NeurIPS2025 Oral] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free · GitHub","url":"https://github.com/qiuzh20/gated_attention"},{"title":"[NeurIPS 2025] Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://arxiviq.substack.com/p/neurips-2025-gated-attention-for"},{"title":"NeurIPS 2025 Best Paper Review: Qwen’s Systematic Exploration of Attention Gating | Towards Data Science","url":"https://towardsdatascience.com/neurips-2025-best-paper-review-qwens-systematic-exploration-of-attention-gating/"},{"title":"Announcing the NeurIPS 2025 Best Paper Awards – NeurIPS Blog","url":"https://blog.neurips.cc/2025/11/26/announcing-the-neurips-2025-best-paper-awards/"},{"title":"NeurIPS Oral Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free","url":"https://neurips.cc/virtual/2025/oral/130320"},{"title":"NeurIPS 2025 Orals","url":"https://neurips.cc/virtual/2025/loc/mexico-city/events/oral"},{"title":"Top 4 Papers of NeurIPS 2025 That You Must Read","url":"https://www.analyticsvidhya.com/blog/2025/11/top-papers-of-neurips-2025/"},{"title":"Gated Attention ~ NeurIPS 2025 Best Paper","url":"https://www.byhand.ai/p/gated-attention-neurips-2025-best"}]

Based on the search results, here is the information about the "Gated Attention" paper:

## Paper Details

The paper "Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free" was awarded the NeurIPS 2025 Best Paper Award, and it was selected as an Oral Presentation at NeurIPS 2025, placing among the top 1.5% of submissions (77 out of 5,290 accepted papers).

## Full Author List

The authors are: Zihan Qiu, Zekun Wang, Bo Zheng, Zeyu Huang, Kaiyue Wen, Songlin Yang, Rui Men
…[truncated 372 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-26T10:24:49.869515+00:00_

Web search results for query: "semanticscholar "Highway Networks" Srivastava 1505.00387 venue "ICML 2015 Deep Learning Workshop""

Links: [{"title":"Highway Networks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2015arXiv150500387S/abstract"},{"title":"Highway Networks","url":"https://arxiv.org/pdf/1505.00387"},{"title":"Training Very Deep Networks","url":"https://arxiv.org/pdf/1507.06228"},{"title":"An Empirical Evaluation of Deep Learning on Highway Driving","url":"https://arxiv.org/pdf/1504.01716"},{"title":"Iterative Deep Learning for Road Topology Extraction","url":"https://arxiv.org/pdf/1808.09814"},{"title":"Mapping road safety features from streetview imagery: A deep learning   approach","url":"https://arxiv.org/pdf/1907.12647"}]

The search results confirm the details about the "Highway Networks" paper. The paper with arXiv ID 1505.00387 was presented at the ICML 2015 Deep Learning workshop. The paper is authored by Rupesh Kumar Srivastava, Klaus Greff, and Jürgen Schmidhuber from the Swiss AI Lab IDSIA.

The paper introduces a new architecture designed to ease gradient-based training of very deep networks, called highway networks, which allow unimpeded information flow across several layers through the use of gating units that regulate the flow of information. Highway networks with hundreds of layers can be trained directly using stochastic gradient descent and with a variety of activation functions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-26T10:24:49.869666+00:00_

Web search results for query: "DialoGPT Large-Scale Generative Pre-training Conversational Response Generation Zhang 2020 ACL arXiv:1911.00536"

Links: [{"title":"[1911.00536] DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation","url":"https://arxiv.org/abs/1911.00536"},{"title":"DIALOGPT : Large-Scale Generative Pre-training for Conversational Response Generation - ACL Anthology","url":"https://aclanthology.org/2020.acl-demos.30/"},{"title":"DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation | Request PDF","url":"https://www.researchgate.net/publication/337019571_DialoGPT_Large-Scale_Generative_Pre-training_for_Conversational_Response_Generation"},{"title":"DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv191100536Z/abstract"},{"title":"GitHub - microsoft/DialoGPT: Large-scale pretraining for dialogue · GitHub","url":"https://github.com/microsoft/DialoGPT"},{"title":"[1911.00536v1] DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation","url":"https://arxiv.org/abs/1911.00536v1"},{"title":"[1911.00536v3] DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation","url":"https://arxiv.org/abs/1911.00536v3"},{"title":"DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation. - Yizhe Zhang","url":"https://dreasysnail.github.io/publication/2020-04-02-DialoGPT:-Large-Scale-Generative-Pre-training-for-Conversational-Response-Generation"},{"title":"Paper page - DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation","url":"https://huggingface.co/papers/1911.00536"}]

I've successfully found the paper you're looking for. Here's what the search revealed:

DialoGPT is a large, tunable neural conversational response generation model trained on 147M conversation-like exchanges extracted from Reddit comment c
…[truncated 948 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 181 · 2026-05-26T10:24:49.869822+00:00_

Web search results for query: "Laban 2505.06120 "LLMs Get Lost" published ICLR 2026 NeurIPS 2025 conference accepted"

Links: [{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/pdf/2505.06120"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"},{"title":"GitHub - microsoft/lost_in_conversation: Code that accompanies the public release of the paper Lost in Conversation (https://arxiv.org/abs/2505.06120) · GitHub","url":"https://github.com/microsoft/lost_in_conversation"},{"title":"Philippe Laban on X: \"🆕paper: LLMs Get Lost in Multi-Turn Conversation In real life, people don’t speak in perfect prompts. So we simulate multi-turn conversations — less lab-like, more like real use. We find that LLMs get lost in conversation. 👀What does that mean? 🧵1/N 📄https://t.co/xt2EfGRh7e https://t.co/YgK6IyqcRv\" / X","url":"https://x.com/PhilippeLaban/status/1921936307816694206"},{"title":"[2505.06120v1] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120v1"},{"title":"LLMs Get Lost In Multi-Turn Conversation - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2505.06120"},{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation · HUMAN TECHNOLOGY eXCELLENCE","url":"https://ht-x.com/posts/2025/09/2505-06120-llms-get-lost-in-multi-turn-conversatio/"},{"title":"LLMs Get Lost In Multi-Turn Conversation (2505.06120v1)","url":"https://www.emergentmind.com/papers/2505.06120"}]

Based on the search results, I found the paper you're asking about:

**Paper Details:**

The paper is titled "LLMs Get Lost In Multi-Turn Conversation" by Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville. The arXiv identifier is 2505.06120.

**Key Findings:**

…[truncated 718 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-26T10:24:49.869991+00:00_

Web search results for query: "Analyzing Multi-Head Self-Attention Specialized Heads Heavy Lifting Pruned Voita 2019 ACL arXiv:1905.09418"

Links: [{"title":"[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418"},{"title":"[1905.09418] Analyzing Multi-Head Self-Attention - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1905.09418"},{"title":"[1905.09418v1] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418v1"},{"title":"[1905.09418v2] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418v2"},{"title":"[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.18653/v1/P19-1580"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190509418V/abstract"},{"title":"(PDF) Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://www.researchgate.net/publication/333337639_Analyzing_Multi-Head_Self-Attention_Specialized_Heads_Do_the_Heavy_Lifting_the_Rest_Can_Be_Pruned"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned · Issue #1276 · arXivTimes/arXivTimes","url":"https://github.com/arXivTimes/arXivTimes/issues/1276"}]

I found the paper you're looking for! Here's what I found:

**"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest
…[truncated 956 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-26T10:24:49.870142+00:00_

Web search results for query: "What Does BERT Look At Analysis of BERT's Attention Clark 2019 ACL BlackboxNLP arXiv:1906.04341"

Links: [{"title":"What Does BERT Look at? An Analysis of BERT’s Attention - ACL Anthology","url":"https://aclanthology.org/W19-4828/"},{"title":"[1906.04341] What Does BERT Look At? An Analysis of BERT's Attention","url":"https://arxiv.org/abs/1906.04341"},{"title":"What Does BERT Look At? An Analysis of BERT’s Attention Kevin Clark†","url":"https://www-nlp.stanford.edu/pubs/clark2019what.pdf"},{"title":"What Does BERT Look at? An Analysis of BERT's Attention - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/what-does-bert-look-at-an-analysis-of-berts-attention/"},{"title":"What Does BERT Look at? An Analysis of BERT’s Attention | Request PDF","url":"https://www.researchgate.net/publication/335778955_What_Does_BERT_Look_at_An_Analysis_of_BERT's_Attention"},{"title":"[PDF] What Does BERT Look at? An Analysis of BERT’s Attention | Semantic Scholar","url":"https://www.semanticscholar.org/paper/What-Does-BERT-Look-at-An-Analysis-of-BERT%E2%80%99s-Clark-Khandelwal/95a251513853c6032bdecebd4b74e15795662986"},{"title":"A paper a day#2: What Does BERT Look At? An Analysis of BERT’s Attention | by Peratham Wiriyathammabhum | Medium","url":"https://peratham.medium.com/a-paper-a-day-2-what-does-bert-look-at-an-analysis-of-berts-attention-2f24d855302"},{"title":"(PDF) What Does BERT Look at? An Analysis of BERT’s Attention","url":"https://www.academia.edu/121847697/What_Does_BERT_Look_at_An_Analysis_of_BERT_s_Attention"}]

I found the paper you're looking for! Here are the key details:

**Publication Information:**
"What Does BERT Look at? An Analysis of BERT's Attention" by Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning was published in Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 276–286, Florence, Italy.

The paper is also available on arXiv as 
…[truncated 810 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-26T10:24:49.870297+00:00_

Web search results for query: "Judging LLM-as-a-Judge MT-Bench Chatbot Arena Zheng NeurIPS 2023 arXiv:2306.05685"

Links: [{"title":"[2306.05685] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/abs/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | OpenReview","url":"https://openreview.net/forum?id=uccHPGDlao"},{"title":"(PDF) Judging LLM-as-a-judge with MT-Bench and Chatbot Arena","url":"https://www.researchgate.net/publication/371490428_Judging_LLM-as-a-judge_with_MT-Bench_and_Chatbot_Arena"},{"title":"Paper page - Judging LLM-as-a-judge with MT-Bench and Chatbot Arena","url":"https://huggingface.co/papers/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena Lianmin Zheng1∗","url":"https://arxiv.org/pdf/2306.05685"},{"title":"[Paper Note] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, Lianmin Zheng+, NeurIPS'23, 2023.06 · Issue #903 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/903"},{"title":"[PDF] Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Judging-LLM-as-a-judge-with-MT-Bench-and-Chatbot-Zheng-Chiang/a0a79dad89857a96f8f71b14238e5237cbfc4787"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/html/2306.05685v4"},{"title":"Evaluating LLM Judges: MT-Bench & Chatbot Arena","url":"https://www.emergentmind.com/papers/2306.05685"}]

I found the research paper you're looking for. Here's what I found:

The paper "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (arXiv:2306.05685) was submitted on June 9, 2023, with the final version (v4) revised on December 24, 2023, and is authored by Lianmin Zheng and 12 other researchers. It was published as part of the 37th Conference on Neural Information Processing Systems (NeurIPS 2023) Track on Datasets and Benchmarks.

**Overview of the Paper:**

The paper addresses 
…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-26T10:24:49.870463+00:00_

Web search results for query: "arxiv 1905.10617 latest version title "Exposure Bias versus Self-Recovery""

Links: [{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Exposure Bias versus Self-Recovery:","url":"https://arxiv.org/pdf/1905.10617"},{"title":"[1905.10617v4] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v4"},{"title":"Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/pdf/1905.10617v4"},{"title":"[1905.10617v1] Quantifying Exposure Bias for Neural Language Generation","url":"https://arxiv.org/abs/1905.10617v1"},{"title":"[PDF] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exposure-Bias-versus-Self-Recovery:-Are-Distortions-He-Zhang/cb51b53d5d26537ed6d458f83b81afe0f2efa289"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Request PDF","url":"https://www.researchgate.net/publication/357121582_Exposure_Bias_versus_Self-Recovery_Are_Distortions_Really_Incremental_for_Autoregressive_Text_Generation"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.415/"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions ...","url":"https://aclanthology.org/2021.emnlp-main.415.pdf"}]

Based on the search results, here's the information about arXiv paper 1905.10617:

**Latest Version Title:** "Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?"

**Version Information:** The paper was submitted on May 25, 2019 (v1) and last revised on September 3, 2021 (v10)

**Authors:** Tian
…[truncated 608 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-26T10:24:49.870622+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.bib",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-26T10:24:49.870742+00:00_

artifacts/dream_reports/dream_20260519T135115/median/references.bib
artifacts/dream_reports/dream_20260519T145320/best/custom.bib
paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 188 · 2026-05-26T10:24:49.870861+00:00_

Web search results for query: "openreview "Attention Forcing for Sequence-to-sequence Model Training" rJe5_CNtPB ICLR rejected"

Links: [{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"},{"title":"Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/pdf/1909.12289"},{"title":"Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/pdf/2211.03237"},{"title":"Supervised Attention in Sequence-to-Sequence Models for Speech   Recognition","url":"https://arxiv.org/pdf/2204.12308"},{"title":"Minimum Word Error Rate Training for Attention-based   Sequence-to-Sequence Models","url":"https://arxiv.org/pdf/1712.01818"}]

Based on the search results, I found the paper "Attention Forcing for Sequence-to-sequence Model Training" on OpenReview with the ID rJe5_CNtPB.

The paper introduces attention forcing, which guides the model with generated output history and reference attention, allowing the model to recover from its mistakes in a stable fashion without the need for a schedule or a classifier. Experiments on speech synthesis show that attention forcing yields significant performance gain, while experiments on machine translation show that guiding the model with reference attention is beneficial for tasks where various re-orderings of the output are valid.

The paper is available on OpenReview at https://openreview.net/forum?id=rJe5_CNtPB and was posted on September 25, 2019. The work has also been published on arXiv.

Regarding the rejection status at ICLR, the search results do not contain explicit information about whether this paper was rejected by ICLR, so I cannot confirm that detail from the available sources.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-26T10:24:49.871007+00:00_

Web search results for query: "Recipes for Building an Open-Domain Chatbot Roller 2021 EACL arXiv:2004.13637"

Links: [{"title":"[2004.13637] Recipes for building an open-domain chatbot","url":"https://arxiv.org/abs/2004.13637?_hsenc=p2ANqtz-812IhL294q5bT5M5HLvLxD6pL7M9lE2Hd0-wf5UNphYYcVx-f2K7KwaNh68AO8zDpN8Vfv"},{"title":"Recipes for Building an Open-Domain Chatbot - ACL Anthology","url":"https://aclanthology.org/2021.eacl-main.24/"},{"title":"Recipes for building an open-domain chatbot – ScienceOpen","url":"https://www.scienceopen.com/document?vid=4bf217dc-ec2f-4d9e-8b88-bc6b2ce0becf"},{"title":"(PDF) Recipes for Building an Open-Domain Chatbot","url":"https://www.academia.edu/122661824/Recipes_for_Building_an_Open_Domain_Chatbot"},{"title":"Paper page - Recipes for building an open-domain chatbot","url":"https://huggingface.co/papers/2004.13637"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?doi=10.18653/v1/2021.eacl-main.24"},{"title":"Recipes for building an open-domain chatbot","url":"https://parl.ai/projects/recipes/"},{"title":"Recipes for Building an Open-Domain Chatbot","url":"https://www.researchgate.net/publication/355433420_Recipes_for_Building_an_Open-Domain_Chatbot"}]

I found the paper you're looking for! Here are the key details:

"Recipes for Building an Open-Domain Chatbot" was authored by Stephen Roller, Emily Dinan, Naman Goyal, Da Ju, Mary Williamson, Yinhan Liu, Jing Xu, Myle Ott, Eric Michael Smith, Y-Lan Boureau, and Jason Weston at EACL 2021.

**About the Paper:**

Building open-domain chatbots is a challenging area for machine learning research. While prior work has shown that scaling neural models in the number of parameters and the size of the data they are trained on gives improved results, the paper shows that other ingredients are important for a high-performing chatbot.

Good conversation requires a number of skills that an expert conversationalist blends in a seamless way: providing engaging talking poin
…[truncated 714 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 190 · 2026-05-26T10:24:49.871158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"LLMs Get Lost In Multi-Turn Conversation\" Laban ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"LLMs Get Lost In Multi-Turn Conversation\" Laban ICLR 2026"
  }
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-26T10:24:49.871290+00:00_

Web search results for query: "Navon Aviv Shamsian "Multi-Task Learning as a Bargaining Game" ICML 2022 arXiv 2202.01017"

Links: [{"title":"GitHub - AvivNavon/nash-mtl: Official implementation of \"Multi-Task Learning as a Bargaining Game\" [ICML 2022] · GitHub","url":"https://github.com/avivnavon/nash-mtl"},{"title":"Multi-Task Learning as a Bargaining Game","url":"https://proceedings.mlr.press/v162/navon22a/navon22a.pdf"},{"title":"Multi-Task Learning as a Bargaining Game - Bar-Ilan University","url":"https://cris.biu.ac.il/en/publications/multi-task-learning-as-a-bargaining-game/"},{"title":"Multi-Task Learning as a Bargaining Game A. Navon1 A. Shamsian1 I. Achituve1","url":"https://icml.cc/media/icml-2022/Slides/17114.pdf"},{"title":"[2202.01017] Multi-Task Learning as a Bargaining Game","url":"https://arxiv.org/abs/2202.01017"},{"title":"(PDF) Multi-Task Learning as a Bargaining Game","url":"https://www.researchgate.net/publication/358306683_Multi-Task_Learning_as_a_Bargaining_Game"},{"title":"Multi-Task Learning as a Bargaining Game [Quick Review]","url":"https://liner.com/review/multitask-learning-as-bargaining-game?entry-type=quick_review_inventory"},{"title":"BIBTEX","url":"https://ml.comp.nus.edu.sg/bibtex/navon2022multi.html"},{"title":"Track: Transfer/Multitask/Meta Learning","url":"https://icml.cc/virtual/2022/session/20052"},{"title":"Publications - Aviv Navon","url":"https://avivnavon.github.io/publications/"}]

I found detailed information about the paper you're looking for. Here's what I found:

## Paper Overview

"Multi-Task Learning as a Bargaining Game" was published with arXiv ID 2202.01017 by authors Aviv Navon, Aviv Shamsian, Idan Achituve, Haggai Maron, Kenji Kawaguchi, Gal Chechik, and Ethan Fetaya in 2022, and it appeared in the Proceedings of the 39th International Conference on Machine Learning in Baltimore, Maryland, USA.

## Key Contribution

In Multi-task learning (MTL), a joint model is trained to simultaneously make predictions for 
…[truncated 912 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 192 · 2026-05-26T10:24:49.871495+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "MT-Bench-101 Bai authors full list ACL 2024 \"Xingyuan Bu\" \"Yancheng He\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "MT-Bench-101 Bai authors full list ACL 2024 \"Xingyuan Bu\" \"Yancheng He\""
  }
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-26T10:24:49.871643+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 194 · 2026-05-26T10:24:49.871849+00:00_

1	% ============================================================
2	% Multi-Turn Attention
3	% ============================================================
4	
5	@article{dongre2026attention,
6	  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7	  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8	  journal = {arXiv preprint arXiv:2605.12922},
9	  year    = {2026},
10	  url     = {https://arxiv.org/abs/2605.12922}
11	}
12	
13	@article{hong2025rhea,
14	  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15	  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16	  journal = {arXiv preprint arXiv:2512.06869},
17	  year    = {2025},
18	  url     = {https://arxiv.org/abs/2512.06869}
19	}
20	
21	@article{laban2025lost,
22	  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23	  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24	  journal = {arXiv preprint arXiv:2505.06120},
25	  year    = {2025},
26	  url     = {https://arxiv.org/abs/2505.06120}
27	}
28	
29	@article{liu2026intent,
30	  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31	  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32	  journal = {arXiv preprint arXiv:2602.07338},
33	  year    = {2026},
34	  url     = {https://arxiv.org/abs/2602.07338}
35	}
36	
37	@inproceedings{bai2024mtbench101,
38	  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39	  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40	  booktitle = {Annual Meeting of the Ass
…[truncated 25029 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 195 · 2026-05-26T10:24:49.872012+00:00_

Web search results for query: ""Professor Forcing" NeurIPS 2016 author order "Goyal, Lamb" OR "Lamb, Goyal" proceedings"

Links: [{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://papers.neurips.cc/paper/2016/hash/16026d60ff9b54410b3435b403afd226-Abstract.html"},{"title":"Figure 1 from Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/db38edba294b7d2fd8ca3aad65721bd9dce32619/figure/0"},{"title":"[Quick Review] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://liner.com/review/professor-forcing-a-new-algorithm-for-training-recurrent-networks"},{"title":"[PDF] Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/2fe874a1c85ecc9e848bf9defd76535e19d51f39"},{"title":"Book - NIPS papers - NeurIPS","url":"https://papers.neurips.cc/paper/2016"},{"title":"Advances in Neural Information Processing Systems 29","url":"https://proceedings.neurips.cc/paper/2016"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Professor+forcing:+A+new+algorithm+for+training+recurrent+networks&author=Anirudh+Goyal&author=Alex+Lamb&author=Ying+Zhang&author=Saizheng+Zhang&author=Aaron+C.+Courville&author=Yoshua+Bengio&publication_year=2016&journal=Advances+in+Neural+Information+Processing+Systems+29:+Annual+Conference+on+Neural+Information+Processing+Systems+2016,+December+5%E2%80%9310,+2016,+Barcelona,+Spain&pages=4601-4609"},{"title":"NIPS Poster Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://neurips.cc/virtual/2016/poster/7377"},{"title":"[1610.09038] Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://arxiv.org/abs/1610.09038"},{"title":"[1610.09038
…[truncated 701 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-26T10:24:49.872165+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Revealing the Dark Secrets of BERT Kovaleva 2019 EMNLP arXiv:1908.08593"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Revealing the Dark Secrets of BERT Kovaleva 2019 EMNLP arXiv:1908.08593"
  }
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-26T10:24:49.872296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lost in the Middle How Language Models Use Long Contexts Liu 2024 TACL arXiv:2307.03172"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lost in the Middle How Language Models Use Long Contexts Liu 2024 TACL arXiv:2307.03172"
  }
}
```

</details>

---

### Tool call

_source line 198 · 2026-05-26T10:24:49.872443+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Jiwei Persona-Based Neural Conversation Model ACL 2016 aclanthology P16-1094"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Jiwei Persona-Based Neural Conversation Model ACL 2016 aclanthology P16-1094"
  }
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-26T10:24:49.872635+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dong Yihe Cordonnier \"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\" ICML 2021 arXiv 2103.03404"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dong Yihe Cordonnier \"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\" ICML 2021 arXiv 2103.03404"
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-26T10:24:49.872774+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Beyond Goldfish Memory Long-Term Open-Domain Conversation Xu 2022 ACL aclanthology 2022.acl-long.356"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Beyond Goldfish Memory Long-Term Open-Domain Conversation Xu 2022 ACL aclanthology 2022.acl-long.356"
  }
}
```

</details>

---

### Tool call

_source line 201 · 2026-05-26T10:24:49.872903+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "He Zhang Zhou Glass \"Exposure Bias versus Self-Recovery\" EMNLP 2021 aclanthology 2021.emnlp-main.415"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "He Zhang Zhou Glass \"Exposure Bias versus Self-Recovery\" EMNLP 2021 aclanthology 2021.emnlp-main.415"
  }
}
```

</details>

---

### Tool call

_source line 202 · 2026-05-26T10:24:49.873037+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vig Multiscale Visualization Attention Transformer Model ACL 2019 System Demonstrations aclanthology P19-3007"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vig Multiscale Visualization Attention Transformer Model ACL 2019 System Demonstrations aclanthology P19-3007"
  }
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-26T10:24:49.873166+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Parallel Attention Forcing\" Dou Gales EACL 2023 OR ACL 2023 OR EMNLP 2023 OR NAACL 2023 published"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Parallel Attention Forcing\" Dou Gales EACL 2023 OR ACL 2023 OR EMNLP 2023 OR NAACL 2023 published"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-26T10:24:49.873299+00:00_

Web search results for query: "MT-Bench-101 Bai authors full list ACL 2024 "Xingyuan Bu" "Yancheng He""

Links: [{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.401/"},{"title":"GitHub - mtbench101/mt-bench-101: [ACL 2024] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues · GitHub","url":"https://github.com/mtbench101/mt-bench-101"},{"title":"[PDF] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues | Semantic Scholar","url":"https://www.semanticscholar.org/paper/MT-Bench-101:-A-Fine-Grained-Benchmark-for-Large-in-Bai-Liu/9978f937189a279a726545a734d20558095e7a0a"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues | Request PDF","url":"https://www.researchgate.net/publication/384215139_MT-Bench-101_A_Fine-Grained_Benchmark_for_Evaluating_Large_Language_Models_in_Multi-Turn_Dialogues"},{"title":"[2402.14762] MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues","url":"https://arxiv.org/abs/2402.14762"},{"title":"MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues [Quick Review]","url":"https://liner.com/review/mtbench101-finegrained-benchmark-for-evaluating-large-language-models-in-multiturn"},{"title":"Accepted Main Conference Papers - ACL 2024","url":"https://2024.aclweb.org/program/main_conference_papers/"},{"title":"Jiaheng Liu","url":"https://liujiaheng.github.io/"}]

Based on the search results, here is the complete list of authors for the MT-Bench-101 paper published at ACL 2024:

Ge Bai, Jie Liu, Xingyuan Bu, Yancheng He, Jiaheng Liu, Zhanhui Zhou, Zhuoran Lin, Wenbo Su, Tiezheng Ge, Bo Zheng, and Wanli Ouyang

The paper was published in Proceedings of the 62nd Annual Meeting of the Associ
…[truncated 199 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-26T10:24:49.873498+00:00_

Web search results for query: "He Zhang Zhou Glass "Exposure Bias versus Self-Recovery" EMNLP 2021 aclanthology 2021.emnlp-main.415"

Links: [{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.415/"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? - researchr publication","url":"https://researchr.org/publication/HeZZG21"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Request PDF","url":"https://www.researchgate.net/publication/357121582_Exposure_Bias_versus_Self-Recovery_Are_Distortions_Really_Incremental_for_Autoregressive_Text_Generation"},{"title":"[PDF] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Exposure-Bias-versus-Self-Recovery:-Are-Distortions-He-Zhang/cb51b53d5d26537ed6d458f83b81afe0f2efa289"},{"title":"Papers with Code - Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://paperswithcode.com/paper/quantifying-exposure-bias-for-neural-language"},{"title":"[1905.10617] Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?","url":"https://arxiv.org/abs/1905.10617"},{"title":"Exposure Bias versus Self-Recovery: Are Distortions ...","url":"https://aclanthology.org/2021.emnlp-main.415.pdf"},{"title":"Generating Self-Contained and Summary-Centric Question Answer Pairs via Differentiable Reward Imitation Learning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.416/"}]

I found the paper you were looking for. Here are the search results:

"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text G
…[truncated 590 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-26T10:24:49.873687+00:00_

Web search results for query: "Revealing the Dark Secrets of BERT Kovaleva 2019 EMNLP arXiv:1908.08593"

Links: [{"title":"[1908.08593] Revealing the Dark Secrets of BERT","url":"https://arxiv.org/abs/1908.08593"},{"title":"[PDF] Revealing the Dark Secrets of BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revealing-the-Dark-Secrets-of-BERT-Kovaleva-Romanov/d78aed1dac6656affa4a04cbf225ced11a83d103"},{"title":"Revealing the Dark Secrets of BERT","url":"https://bibbase.org/network/publication/kovaleva-romanov-rogers-rumshisky-revealingthedarksecretsofbert-2019"},{"title":"[1908.08593] Revealing the Dark Secrets of BERT","url":"https://export.arxiv.org/abs/1908.08593?context=cs"},{"title":"[1908.08593v1] Revealing the Dark Secrets of BERT","url":"https://arxiv.org/abs/1908.08593v1"},{"title":"[1908.08593] Revealing the Dark Secrets of BERT - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1908.08593"},{"title":"Revealing the Dark Secrets of BERT","url":"https://arxiv.org/pdf/1908.08593"},{"title":"[1908.08593v2] Revealing the Dark Secrets of BERT","url":"https://arxiv.org/abs/1908.08593v2"},{"title":"Revealing the Dark Secrets of BERT | Request PDF","url":"https://www.researchgate.net/publication/335395256_Revealing_the_Dark_Secrets_of_BERT"}]

I found the paper you're looking for! Here's information about "Revealing the Dark Secrets of BERT":

**Paper Details:**
- Authors: Olga Kovaleva, Alexey Romanov, Anna Rogers, and Anna Rumshisky
- Published at EMNLP (Empirical Methods in Natural Language Processing)
- arXiv ID: 1908.08593
- First submitted on August 21, 2019, with revision on September 11, 2019

**Main Contribution:**
The paper examines the interpretation of self-attention, a fundamental component of BERT, using a subset of GLUE tasks and analyzing the information encoded by individual BERT's attention heads.

**Key Findings:**
- There is a limited set of attention patterns that are repeated across different heads, indicating the ov
…[truncated 329 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-26T10:24:49.873845+00:00_

Web search results for query: "Dong Yihe Cordonnier "Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth" ICML 2021 arXiv 2103.03404"

Links: [{"title":"[2103.03404] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404"},{"title":"Attention is not all you need:","url":"https://arxiv.org/pdf/2103.03404"},{"title":"[2103.03404v1] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404v1"},{"title":"(PDF) Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://www.researchgate.net/publication/349880007_Attention_is_Not_All_You_Need_Pure_Attention_Loses_Rank_Doubly_Exponentially_with_Depth"},{"title":"[2103.03404v2] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth","url":"https://arxiv.org/abs/2103.03404v2"},{"title":"[PDF] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Attention-is-Not-All-You-Need:-Pure-Attention-Loses-Dong-Cordonnier/dfb37e6216e792bf6bd5a30c0fc7ad55df1cb71e"},{"title":"Attention is Not All You Need","url":"https://www.summarizepaper.com/en/arxiv-id/2103.03404v2/"},{"title":"Jean-Baptiste Cordonnier","url":"https://jbcordonnier.com/"},{"title":"GitHub - twistedcubic/attention-rank-collapse: [ICML 2021 Oral] We show pure attention suffers rank collapse, and how different mechanisms combat it. · GitHub","url":"https://github.com/twistedcubic/attention-rank-collapse"}]

I found the paper successfully. Here are the key details:

**Paper Information:**
The paper "Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth" (arXiv:2103.03404) was authored by Yihe Dong, Jean-Baptiste Cordonnier, and Andreas Loukas, and was submitted on March 5, 2021. Th
…[truncated 774 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 208 · 2026-05-26T10:24:49.874006+00:00_

Web search results for query: "Li Jiwei Persona-Based Neural Conversation Model ACL 2016 aclanthology P16-1094"

Links: [{"title":"A Persona-Based Neural Conversation Model - ACL Anthology","url":"https://aclanthology.org/P16-1094/"},{"title":"A Persona-Based Neural Conversation Model | Request PDF","url":"https://www.researchgate.net/publication/306093549_A_Persona-Based_Neural_Conversation_Model"},{"title":"A Persona-Based Neural Conversation Model","url":"https://lingo.iitgn.ac.in/nlpexplorer/paper/P16-1094"},{"title":"dblp: A Persona-Based Neural Conversation Model.","url":"https://dblp.org/rec/conf/acl/LiGBSGD16.html"},{"title":"[PDF] A Persona-Based Neural Conversation Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Persona-Based-Neural-Conversation-Model-Li-Galley/1ea75cdb7ce8c4f5f2599165e3698034b4142e08"},{"title":"Table 1 from A Persona-Based Neural Conversation Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Persona-Based-Neural-Conversation-Model-Li-Galley/1ea75cdb7ce8c4f5f2599165e3698034b4142e08/figure/0"},{"title":"A Persona-Based Neural Conversation Model : Jiwei Li : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/arxiv-1603.06155"},{"title":"[1603.06155] A Persona-Based Neural Conversation Model","url":"https://arxiv.org/abs/1603.06155"},{"title":"Jiwei's Homepage","url":"https://nlp.stanford.edu/~bdlijiwei/Publications_ByTopic.html"}]

I've found the paper you're looking for. The paper "A Persona-Based Neural Conversation Model" was authored by Jiwei Li, Michel Galley, Chris Brockett, Georgios Spithourakis, Jianfeng Gao, and Bill Dolan, and was published in the Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 994–1003, Berlin, Germany in 2016.

The paper presents persona-based models for handling speaker consistency in neural response generation, with a speaker model that encodes personas
…[truncated 660 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-26T10:24:49.874161+00:00_

Web search results for query: "Vig Multiscale Visualization Attention Transformer Model ACL 2019 System Demonstrations aclanthology P19-3007"

Links: [{"title":"A Multiscale Visualization of Attention in the Transformer Model - ACL Anthology","url":"https://aclanthology.org/P19-3007/"},{"title":"[1906.05714] A Multiscale Visualization of Attention in the Transformer Model","url":"https://arxiv.org/abs/1906.05714"},{"title":"A Multiscale Visualization of Attention in the Transformer Model Jesse Vig","url":"https://arxiv.org/pdf/1906.05714"},{"title":"[PDF] A Multiscale Visualization of Attention in the Transformer Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-Multiscale-Visualization-of-Attention-in-the-Vig/0de0a44b859a3719d11834479112314b4caba669"},{"title":"(PDF) A Multiscale Visualization of Attention in the Transformer Model","url":"https://www.researchgate.net/publication/335784229_A_Multiscale_Visualization_of_Attention_in_the_Transformer_Model"},{"title":"A Multiscale Visualization of Attention in the Transformer ...","url":"https://aclanthology.org/P19-3007.pdf"},{"title":"A Multiscale Visualization of Attention in the Transformer Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190605714V/abstract"},{"title":"[1906.05714v1] A Multiscale Visualization of Attention in the Transformer Model","url":"https://arxiv.org/abs/1906.05714v1"},{"title":"Paper page - A Multiscale Visualization of Attention in the Transformer Model","url":"https://huggingface.co/papers/1906.05714"},{"title":"GitHub - jessevig/bertviz: BertViz: Visualize Attention in Transformer Models · GitHub","url":"https://github.com/jessevig/bertviz"}]

I found the paper you're looking for! Here's what I found:

**"A Multiscale Visualization of Attention in the Transformer Model"** by Jesse Vig was published in 2019 in the Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pages 37–42, in Florence, It
…[truncated 744 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-26T10:24:49.874317+00:00_

Web search results for query: "openreview.net "LLMs Get Lost In Multi-Turn Conversation" Laban ICLR 2026"

Links: [{"title":"LLMs Get Lost In Multi-Turn Conversation | OpenReview","url":"https://openreview.net/forum?id=VKGTGGcwl6"},{"title":"LLMS GET LOST IN MULTI-TURN CONVERSATION","url":"https://openreview.net/pdf?id=VKGTGGcwl6"},{"title":"LLMs Get Lost In Multi-Turn Conversation [Quick Review]","url":"https://liner.com/review/llms-get-lost-in-multiturn-conversation"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf?id=5J6u03ObRZ"},{"title":"ICLR 2026 LLMs Get Lost In Multi-Turn Conversation Oral","url":"https://iclr.cc/virtual/2026/oral/10009147"},{"title":"[2505.06120] LLMs Get Lost In Multi-Turn Conversation","url":"https://arxiv.org/abs/2505.06120"},{"title":"LLMs Get Lost In Multi-Turn Conversation - Microsoft Research","url":"https://www.microsoft.com/en-us/research/publication/llms-get-lost-in-multi-turn-conversation/"},{"title":"LLMs Lose 39% Accuracy in Multi-Turn Conversations | ICLR","url":"https://beam.ai/agentic-insights/iclr-2026-llms-lose-accuracy-in-multi-turn-conversations"},{"title":"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation | OpenReview","url":"https://openreview.net/forum?id=3x94uVDCeq"},{"title":"[PDF] LLMs Get Lost In Multi-Turn Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/LLMs-Get-Lost-In-Multi-Turn-Conversation-Laban-Hayashi/bb5d81576c113f0b16234fd0db4238a4281c8388"}]

I found the paper! Here's a summary of the search results:

"LLMs Get Lost In Multi-Turn Conversation" is a paper by Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, and Jennifer Neville that was presented as an oral presentation at ICLR 2026 on April 23, 2026.

**Key Findings:**

The experiments confirm that all the top open- and closed-weight LLMs tested exhibit significantly lower performance in multi-turn conversations than single-turn, with an average drop 
…[truncated 584 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-26T10:24:49.874500+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhou Wangchunshu \"Scheduled DropHead: A Regularization Method for Transformer Models\" Findings EMNLP 2020 arXiv 2004.13342"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhou Wangchunshu \"Scheduled DropHead: A Regularization Method for Transformer Models\" Findings EMNLP 2020 arXiv 2004.13342"
  }
}
```

</details>

---

### Tool result

_source line 212 · 2026-05-26T10:24:49.874644+00:00_

Web search results for query: "Lost in the Middle How Language Models Use Long Contexts Liu 2024 TACL arXiv:2307.03172"

Links: [{"title":"[2307.03172] Lost in the Middle: How Language Models Use Long Contexts","url":"https://arxiv.org/abs/2307.03172"},{"title":"Lost in the Middle: How Language Models Use Long Contexts - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.9/"},{"title":"Lost in the Middle: How Language Models Use Long Contexts | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long"},{"title":"(PDF) Lost in the Middle: How Language Models Use Long Contexts","url":"https://www.researchgate.net/publication/378284067_Lost_in_the_Middle_How_Language_Models_Use_Long_Contexts"},{"title":"Lost in the Middle: How Language Models Use Long Contexts - researchr publication","url":"https://researchr.org/publication/LiuLHPBPL24"},{"title":"Lost in the Middle: How Language Models Use Long Contexts Nelson F. Liu1∗","url":"https://aclanthology.org/2024.tacl-1.9.pdf"},{"title":"Lost in the Middle: How Language Models Use Long Contexts | Transactions of the Association for Computational Linguistics","url":"https://transacl.org/index.php/tacl/article/view/5757"},{"title":"Paper page - Lost in the Middle: How Language Models Use Long Contexts","url":"https://huggingface.co/papers/2307.03172"},{"title":"[PDF] Lost in the Middle: How Language Models Use Long Contexts | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Lost-in-the-Middle:-How-Language-Models-Use-Long-Liu-Lin/1733eb7792f7a43dd21f51f4d1017a1bffd217b5"}]

I found the paper you were looking for! Here's what I found:

## Paper Details

"Lost in the Middle: How Language Models Use Long Contexts" by Liu, Nelson F., Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang was published in the Transactions of the Asso
…[truncated 984 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 213 · 2026-05-26T10:24:49.874798+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview \"Intent Mismatch\" \"Lost in Multi-Turn\" Liu Geng ICLR 2026 conference"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview \"Intent Mismatch\" \"Lost in Multi-Turn\" Liu Geng ICLR 2026 conference"
  }
}
```

</details>

---

### Tool call

_source line 214 · 2026-05-26T10:24:49.874929+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview \"Explicating the Implicit\" \"Bridging the Intent Alignment Gap\" ICLR 2026 Liu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview \"Explicating the Implicit\" \"Bridging the Intent Alignment Gap\" ICLR 2026 Liu"
  }
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-26T10:24:49.875062+00:00_

Web search results for query: "Beyond Goldfish Memory Long-Term Open-Domain Conversation Xu 2022 ACL aclanthology 2022.acl-long.356"

Links: [{"title":"Beyond Goldfish Memory: Long-Term Open-Domain Conversation - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.356/"},{"title":"[PDF] Beyond Goldfish Memory: Long-Term Open-Domain Conversation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Beyond-Goldfish-Memory:-Long-Term-Open-Domain-Xu-Szlam/88064de690af282dbdf222774f03ff070b9df22b"},{"title":"Long-Term Open-Domain Conversation","url":"https://aclanthology.org/2022.acl-long.356.pdf"},{"title":"[2107.07567] Beyond Goldfish Memory: Long-Term Open-Domain Conversation","url":"https://arxiv.org/abs/2107.07567"},{"title":"dblp: Beyond Goldfish Memory: Long-Term Open-Domain Conversation.","url":"https://dblp.uni-trier.de/rec/conf/acl/XuSW22.html"},{"title":"Beyond Goldfish Memory: Long-Term Open-Domain Conversation | Underline","url":"https://underline.io/lecture/50296-beyond-goldfish-memory-long-term-open-domain-conversation"},{"title":"[2107.07567v1] Beyond Goldfish Memory: Long-Term Open-Domain Conversation","url":"https://arxiv.org/abs/2107.07567v1"},{"title":"Beyond Goldﬁsh Memory∗: Long-Term Open-Domain Conversation Jing Xu Arthur Szlam","url":"https://arxiv.org/pdf/2107.07567v1"},{"title":"[Quick Review] Beyond Goldfish Memory: Long-Term Open-Domain Conversation","url":"https://liner.com/review/beyond-goldfish-memory-longterm-opendomain-conversation"}]

I found the paper! Here are the details:

**Paper Title:** Beyond Goldfish Memory: Long-Term Open-Domain Conversation

**Authors:** Jing Xu, Arthur Szlam, and Jason Weston

**Publication:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 5180–5197, Dublin, Ireland

**DOI:** 10.18653/v1/2022.acl-long.356

**About the Paper:** Despite recent improvements in open-domain dialogue models, state-of-the-art models are traine
…[truncated 906 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 216 · 2026-05-26T10:24:49.875218+00:00_

Web search results for query: ""Parallel Attention Forcing" Dou Gales EACL 2023 OR ACL 2023 OR EMNLP 2023 OR NAACL 2023 published"

Links: [{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Attention Forcing for Machine Translation","url":"https://arxiv.org/pdf/2104.01264"},{"title":"Parallel Attention","url":"https://www.linkedin.com/company/parallelattention"},{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"},{"title":"Parallel Attention Forcing for Machine Translation","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2211.03237"},{"title":"Analyzing Parallelization of Attention · Better Tomorrow with Computer Science","url":"https://insujang.github.io/2022-08-03/analyzing-parallelization-of-attention/"},{"title":"Parallel Attention | Custom ML integrated into your tech stack","url":"https://parallelattention.com/"}]

Based on the search results, I found information about "Parallel Attention Forcing for Machine Translation" by Qingyun Dou and Mark Gales. 

According to the search results, the paper addresses attention-based autoregressive models in sequence-to-sequence tasks like Text-To-Speech (TTS) and Neural Machine Translation (NMT). Attention forcing has been introduced to address the mismatch between training and inference by guiding the model with the generated back-history and reference attention, and while successful in tasks with continuous outputs like TTS, attention forcing faces additional challenges in tasks with discrete outputs like NMT, which this paper introduces extensions to tackle.

The paper appears to be hosted on arXiv (preprint arXiv:2211.03237) from November 6, 2022. However, the search results do not clearly specify which major conference (EACL 2023, AC
…[truncated 328 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 217 · 2026-05-26T10:24:49.875376+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Abnar Zuidema Quantifying Attention Flow Transformers ACL 2020 aclanthology 2020.acl-main.385"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Abnar Zuidema Quantifying Attention Flow Transformers ACL 2020 aclanthology 2020.acl-main.385"
  }
}
```

</details>

---

### Tool call

_source line 218 · 2026-05-26T10:24:49.875549+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "semantic scholar \"Professor Forcing\" Goyal Lamb NeurIPS 2016 proceedings author order"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "semantic scholar \"Professor Forcing\" Goyal Lamb NeurIPS 2016 proceedings author order"
  }
}
```

</details>

---

### Tool call

_source line 219 · 2026-05-26T10:24:49.875679+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ethayarajh How Contextual Contextualized Word Representations Geometry BERT ELMo GPT-2 EMNLP 2019 aclanthology D19-1006"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ethayarajh How Contextual Contextualized Word Representations Geometry BERT ELMo GPT-2 EMNLP 2019 aclanthology D19-1006"
  }
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-26T10:24:49.875806+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Attention Forcing\" Dou 2020 Interspeech OR ICASSP OR conference proceedings published version"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Attention Forcing\" Dou 2020 Interspeech OR ICASSP OR conference proceedings published version"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-26T10:24:49.875931+00:00_

Web search results for query: "openreview "Intent Mismatch" "Lost in Multi-Turn" Liu Geng ICLR 2026 conference"

Links: [{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"(PDF) Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://www.researchgate.net/publication/400604289_Intent_Mismatch_Causes_LLMs_to_Get_Lost_in_Multi-Turn_Conversation"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/pdf/2602.07338"},{"title":"Verifiable Accuracy and Abstention Rewards in Curriculum RL to Alleviate Lost-in-Conversation","url":"https://arxiv.org/pdf/2510.18731"},{"title":"Beyond More Context: Retrieval Diversity Boosts Multi-Turn Intent Understanding","url":"https://arxiv.org/pdf/2510.17940"}]

Based on the web search results, I found the paper you're looking for:

The paper is titled "Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation" by Geng Liu and 5 other authors. 

The authors are Geng Liu (College of Computing, City University of Hong Kong), Fei Zhu, Rong Feng, Changyi Ma (School of Artificial Intelligence, Jilin University), Shiqi Wang, and Gaofeng Meng (Centre for Artificial Intelligence and Robotics, HKISI, CAS).

The paper addresses the "Lost in Conversation" (LiC) phenomenon where LLMs suffer performance drops in multi-turn settings, arguing that the root cause lies in an intent alignment gap rather than intrinsic capability deficits.

The paper proposes decoupling intent understanding from task execution through a Mediator-Assistant architecture, where an experience-driven Mediator explicates user inputs into explicit, well-structured instructions based on historical interaction patterns.

The paper was posted on arXiv on February 7, 2026, and is available at arxiv.org/abs/2602.07338.


REMINDER: You MUST include the sources above in your response to the user using markdown hyp
…[truncated 8 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-26T10:24:49.876072+00:00_

Web search results for query: "openreview "Explicating the Implicit" "Bridging the Intent Alignment Gap" ICLR 2026 Liu"

Links: [{"title":"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation | OpenReview","url":"https://openreview.net/forum?id=3x94uVDCeq"},{"title":"Discovering Implicit Large Language Model Alignment Objectives","url":"https://arxiv.org/pdf/2602.15338"},{"title":"Aligning Deep Implicit Preferences by Learning to Reason Defensively","url":"https://arxiv.org/pdf/2510.11194"},{"title":"The Unlocking Spell on Base LLMs: Rethinking Alignment via In-Context   Learning","url":"https://arxiv.org/pdf/2312.01552"},{"title":"How Far Can In-Context Alignment Go? Exploring the State of In-Context   Alignment","url":"https://arxiv.org/pdf/2406.11474"}]

Perfect! I found the paper you're looking for. 

The paper "Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation" proposes using an experience-driven Mediator to explicate user inputs into explicit, well-structured instructions based on historical interaction patterns, which bridges the gap between vague user intent and model interpretation.

The paper addresses the phenomenon of "Lost in Conversation" (LiC), where LLMs suffer substantial performance drops in multi-turn settings compared to single-turn interactions, arguing that the root cause lies in an intent alignment gap rather than model capability deficits.

The researchers propose decoupling intent understanding from task execution through a Mediator-Assistant architecture. Experimental results demonstrate that this method significantly mitigates performance degradation in multi-turn conversations across diverse LLMs.

The paper is available on OpenReview at: https://openreview.net/forum?id=3x94uVDCeq


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 223 · 2026-05-26T10:24:49.876221+00:00_

Web search results for query: "Zhou Wangchunshu "Scheduled DropHead: A Regularization Method for Transformer Models" Findings EMNLP 2020 arXiv 2004.13342"

Links: [{"title":"Scheduled DropHead: A Regularization Method for Transformer Models - ACL Anthology","url":"https://aclanthology.org/2020.findings-emnlp.178/"},{"title":"Scheduled DropHead: A Regularization Method for Transformer Models | Request PDF","url":"https://www.researchgate.net/publication/347233845_Scheduled_DropHead_A_Regularization_Method_for_Transformer_Models"},{"title":"EMNLP2020: Scheduled DropHead: A Regularization Method for Transformer Models","url":"https://virtual.2020.emnlp.org/paper_findings.178.html"},{"title":"[PDF] Scheduled DropHead: A Regularization Method for Transformer Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Scheduled-DropHead:-A-Regularization-Method-for-Zhou-Ge/5c27f7106d2f0c95fc51fb98ece672e00185ffa1"},{"title":"[2004.13342] Scheduled DropHead: A Regularization Method for Transformer Models","url":"https://arxiv.org/abs/2004.13342"},{"title":"Scheduled DropHead: A Regularization Method for Transformer Models | DeepAI","url":"https://deepai.org/publication/scheduled-drophead-a-regularization-method-for-transformer-models"},{"title":"Wangchunshu Zhou - ACL Anthology","url":"https://www.aclweb.org/anthology/people/w/wangchunshu-zhou/"},{"title":"(PDF) Scheduled DropHead: A Regularization Method for Transformer Models","url":"https://www.researchgate.net/publication/340997445_Scheduled_DropHead_A_Regularization_Method_for_Transformer_Models"},{"title":"ml-papers/papers/2020/200427 Scheduled DropHead.md at main · rosinality/ml-papers","url":"https://github.com/rosinality/ml-papers/blob/main/papers/2020/200427%20Scheduled%20DropHead.md"},{"title":"GitHub - ZurichNLP/monotonicity_loss","url":"https://github.com/ZurichNLP/monotonicity_loss"}]

Based on the search results, I found comprehensive information about the paper you requested:

## Paper Informati
…[truncated 1269 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-26T10:24:49.876370+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brunner Liu Pascual Richter Ciaramita Krause On Identifiability in Transformers ICLR 2020 arXiv:1908.04211"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brunner Liu Pascual Richter Ciaramita Krause On Identifiability in Transformers ICLR 2020 arXiv:1908.04211"
  }
}
```

</details>

---

### Tool call

_source line 225 · 2026-05-26T10:24:49.876526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Ding Ning UltraChat Enhancing Chat Language Models Scaling High-quality Instructional Conversations EMNLP 2023 arXiv:2305.14233"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Ding Ning UltraChat Enhancing Chat Language Models Scaling High-quality Instructional Conversations EMNLP 2023 arXiv:2305.14233"
  }
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-26T10:24:49.876656+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Grattafiori Llama 3 Herd of Models arXiv:2407.21783 2024 published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Grattafiori Llama 3 Herd of Models arXiv:2407.21783 2024 published venue"
  }
}
```

</details>

---

### Tool call

_source line 227 · 2026-05-26T10:24:49.876783+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dauphin \"Language Modeling with Gated Convolutional Networks\" ICML 2017 arXiv 1612.08083"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dauphin \"Language Modeling with Gated Convolutional Networks\" ICML 2017 arXiv 1612.08083"
  }
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-26T10:24:49.876909+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net 3x94uVDCeq \"Explicating the Implicit\" authors ICLR 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net 3x94uVDCeq \"Explicating the Implicit\" authors ICLR 2026 accepted"
  }
}
```

</details>

---

### Tool call

_source line 229 · 2026-05-26T10:24:49.877034+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"When Attention Closes\" Dongre openreview ICLR 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"When Attention Closes\" Dongre openreview ICLR 2026 accepted"
  }
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-26T10:24:49.877158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Rhea\" \"Role-aware Heuristic Episodic Attention\" openreview ICLR 2026 ACL 2026 accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Rhea\" \"Role-aware Heuristic Episodic Attention\" openreview ICLR 2026 ACL 2026 accepted"
  }
}
```

</details>

---

### Tool result

_source line 231 · 2026-05-26T10:24:49.877283+00:00_

Web search results for query: "semantic scholar "Professor Forcing" Goyal Lamb NeurIPS 2016 proceedings author order"

Links: [{"title":"[PDF] Professor Forcing: A New Algorithm for Training Recurrent Networks - Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/12dd078034f72e4ebd9dfd9f80010d2ae7aaa337"},{"title":"Figure 1 from Professor Forcing: A New Algorithm for Training Recurrent Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Professor-Forcing:-A-New-Algorithm-for-Training-Goyal-Lamb/2fe874a1c85ecc9e848bf9defd76535e19d51f39/figure/0"},{"title":"Anirudh Goyal | Semantic Scholar","url":"https://www.semanticscholar.org/author/Anirudh-Goyal/1996705"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Professor+forcing:+A+new+algorithm+for+training+recurrent+networks&author=Anirudh+Goyal&author=Alex+Lamb&author=Ying+Zhang&author=Saizheng+Zhang&author=Aaron+C.+Courville&author=Yoshua+Bengio&publication_year=2016&journal=Advances+in+Neural+Information+Processing+Systems+29:+Annual+Conference+on+Neural+Information+Processing+Systems+2016,+December+5%E2%80%9310,+2016,+Barcelona,+Spain&pages=4601-4609"},{"title":"Advances in Neural Information Processing Systems 29","url":"https://proceedings.neurips.cc/paper/2016"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://papers.neurips.cc/paper/6099-professor-forcing-a-new-algorithm-for-training-recurrent-networks.pdf"},{"title":"Alex Lamb | Semantic Scholar","url":"https://www.semanticscholar.org/author/Alex-Lamb/49071560"},{"title":"Professor Forcing: A New Algorithm for Training Recurrent Networks","url":"https://proceedings.neurips.cc/paper/2016/hash/16026d60ff9b54410b3435b403afd226-Abstract.html"},{"title":"AMOR: Ambiguous Authorship Order","url":"https://arxiv.org/pdf/2404.00994"}]

Based on the search results, I found the author order for the "Professo
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-26T10:24:49.877448+00:00_

Web search results for query: "Brunner Liu Pascual Richter Ciaramita Krause On Identifiability in Transformers ICLR 2020 arXiv:1908.04211"

Links: [{"title":"Published as a conference paper at ICLR 2020 ON IDENTIFIABILITY IN TRANSFORMERS","url":"https://tik-old.ee.ethz.ch/file/84248b631689290b665ce39984611681/on_identifiability_in_transformers.pdf"},{"title":"ICLR: On Identifiability in Transformers","url":"https://iclr.cc/virtual_2020/poster_BJg1f6EFDB.html"},{"title":"(PDF) On Identifiability in Transformers","url":"https://www.researchgate.net/publication/339377132_On_Identifiability_in_Transformers"},{"title":"On Identifiability in Transformers – Google Research","url":"https://research.google/pubs/pub48972/"},{"title":"[PDF] On Identifiability in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Identifiability-in-Transformers-Brunner-Liu/1fe62a928bf5cfac0f373728f3a4de3cefe0951d"},{"title":"On Identifiability in Transformers","url":"https://research.google/pubs/on-identifiability-in-transformers/"},{"title":"Papers with Code - On Identifiability in Transformers","url":"https://paperswithcode.com/paper/on-the-validity-of-self-attention-as"},{"title":"[1908.04211] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211"},{"title":"On Identifiability in Transformers | OpenReview","url":"https://openreview.net/forum?id=BJg1f6EFDB"},{"title":"[1908.04211v4] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211v4"}]

I found the paper you were looking for! Here's the information:

"On Identifiability in Transformers" was published at ICLR 2020 by Gino Brunner, Yang Liu, Damián Pascual, Oliver Richter, Massimiliano Ciaramita, and Roger Wattenhofer. The paper is available on arXiv as 1908.04211.

The paper investigates two core components of the Transformer architecture: self-attention and contextual embeddings, specifically studying the identifiability of attention weights and token embeddings, a
…[truncated 669 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-26T10:24:49.877601+00:00_

Web search results for query: ""Attention Forcing" Dou 2020 Interspeech OR ICASSP OR conference proceedings published version"

Links: [{"title":"ISCA Archive - Attention Forcing for Speech Synthesis","url":"https://www.isca-archive.org/interspeech_2020/dou20_interspeech.html"},{"title":"ISCA Archive","url":"https://www.isca-speech.org/archive/interspeech_2020/dou20_interspeech.html"},{"title":"Attention Forcing for Speech Synthesis","url":"https://www.isca-archive.org/interspeech_2020/dou20_interspeech.pdf"},{"title":"Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/pdf/1909.12289"},{"title":"Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/pdf/2211.03237"},{"title":"NeuFA: Neural Network Based End-to-End Forced Alignment with   Bidirectional Attention Mechanism","url":"https://arxiv.org/pdf/2203.16838"}]

I found the published version you're looking for. The paper "Attention Forcing for Speech Synthesis" by Dou, Efiong, and Gales was published in Interspeech 2020, pages 4014-4018. The paper is available on the ISCA Archive at https://www.isca-archive.org/interspeech_2020/dou20_interspeech.html with DOI: 10.21437/Interspeech.2020-2520.

The paper introduces attention forcing, which guides the model with the generated output history and reference attention. This approach reduces the training-evaluation mismatch without the need for a schedule or a classifier.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-26T10:24:49.877744+00:00_

Web search results for query: "Abnar Zuidema Quantifying Attention Flow Transformers ACL 2020 aclanthology 2020.acl-main.385"

Links: [{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"},{"title":"Quantifying Attention Flow in Transformers","url":"https://notes-vault.pages.dev/Scientific-Literature-References/literature-notes/@abnarQuantifyingAttentionFlow2020"},{"title":"Attention Flow - AmsterdamNLP","url":"https://amsterdamnlp.github.io/blog/attentionflow/"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"ACL2020: Quantifying Attention Flow in Transformers","url":"https://virtual.acl2020.org/paper_main.385.html"},{"title":"UvA-DARE (Digital Academic Repository)","url":"https://pure.uva.nl/ws/files/178487922/2020.acl-main.385.pdf"},{"title":"(PDF) Quantifying Attention Flow in Transformers","url":"https://www.researchgate.net/publication/341148976_Quantifying_Attention_Flow_in_Transformers"},{"title":"Quantifying Attention Flow in Transformers | Request PDF","url":"https://www.researchgate.net/publication/343298597_Quantifying_Attention_Flow_in_Transformers"}]

I've found the paper you're looking for! Here's the information about it:

"Quantifying Attention Flow in Transformers" by Samira Abnar and Willem Zuidema was published in 2020 in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 4190–4197.

**Summary of the paper:**

The paper addresses how in the Transformer model, "self-attention" combines information from atte
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-26T10:24:49.877897+00:00_

Web search results for query: "Ding Ning UltraChat Enhancing Chat Language Models Scaling High-quality Instructional Conversations EMNLP 2023 arXiv:2305.14233"

Links: [{"title":"[2305.14233] Enhancing Chat Language Models by Scaling High-quality Instructional Conversations","url":"https://arxiv.org/abs/2305.14233"},{"title":"arXiv:2305.14233v1 [cs.CL] 23 May 2023","url":"https://arxiv.org/pdf/2305.14233"},{"title":"[2305.14233v1] Enhancing Chat Language Models by Scaling High-quality Instructional Conversations","url":"https://arxiv.org/abs/2305.14233v1"},{"title":"Enhancing Chat Language Models by Scaling High-quality Instructional Conversations","url":"https://www.researchgate.net/publication/370981823_Enhancing_Chat_Language_Models_by_Scaling_High-quality_Instructional_Conversations"},{"title":"Paper page - Enhancing Chat Language Models by Scaling High-quality Instructional Conversations","url":"https://huggingface.co/papers/2305.14233"},{"title":"Enhancing Chat Language Models by Scaling High-quality","url":"https://arxiv.org/pdf/2305.14233v1"},{"title":"GitHub - thunlp/UltraChat: Large-scale, Informative, and Diverse Multi-round Chat Data (and Models) · GitHub","url":"https://github.com/thunlp/UltraChat"},{"title":"ULTRAFEEDBACK: Boosting Language Models with Scaled AI Feedback","url":"https://arxiv.org/pdf/2310.01377"},{"title":"HuggingFaceH4/ultrachat_200k · Datasets at Hugging Face","url":"https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k"},{"title":"Mastering Text, Code and Math Simultaneously via Fusing Highly Specialized Language Models","url":"https://arxiv.org/html/2403.08281v4"}]

I found the paper you're looking for! Here are the key details:

**Paper Information:**
- **Title:** Enhancing Chat Language Models by Scaling High-quality Instructional Conversations
- **Authors:** Ning Ding, Yulin Chen, Bokai Xu, Yujia Qin, Zhi Zheng, Shengding Hu, Zhiyuan Liu, Maosong Sun, Bowen Zhou
- **arXiv ID:** 2305.14233
- **Submission Date:** May 23, 20
…[truncated 833 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-26T10:24:49.878055+00:00_

Web search results for query: "Ethayarajh How Contextual Contextualized Word Representations Geometry BERT ELMo GPT-2 EMNLP 2019 aclanthology D19-1006"

Links: [{"title":"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings - ACL Anthology","url":"https://aclanthology.org/D19-1006/"},{"title":"[PDF] How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings | Semantic Scholar","url":"https://www.semanticscholar.org/paper/How-Contextual-are-Contextualized-Word-Comparing-of-Ethayarajh/9d7902e834d5d1d35179962c7a5b9d16623b0d39"},{"title":"How Contextual are Contextualized Word Representations? Comparing the Geometry of BERT, ELMo, and GPT-2 Embeddings","url":"https://www.researchgate.net/publication/336998283_How_Contextual_are_Contextualized_Word_Representations_Comparing_the_Geometry_of_BERT_ELMo_and_GPT-2_Embeddings"},{"title":"GitHub - kawine/contextual: How Contextual are Contextualized Word Representations? · GitHub","url":"https://github.com/kawine/contextual"},{"title":"BERT, ELMo, & GPT-2: How contextual are contextualized word representations? | Kawin Ethayarajh","url":"https://kawine.github.io/blog/nlp/2020/02/03/contextual.html"},{"title":"How Contextual are Contextualized Word Representations? Kawin Ethayarajh","url":"https://kawine.github.io/assets/emnlp_2019_contextual_slides.pdf"},{"title":"Ethayarajh, K. (2019) How Contextual Are Contextualized Word Representations Comparing the Geometry of BERT, Elmo, and GPT-2 Embeddings. Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), Hong Kong, 3-7 November 2019, 55-65. - References - Scientific Research Publishing","url":"https://www.scirp.org/reference/referencespapers?referenceid=3936303"},{"title":"How Contextual are Contextualized Word Representations? Comparing the Ge
…[truncated 1638 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 237 · 2026-05-26T10:24:49.878207+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net rJe5_CNtPB \"Attention Forcing\" ICLR 2020 decision accepted rejected"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net rJe5_CNtPB \"Attention Forcing\" ICLR 2020 decision accepted rejected"
  }
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-26T10:24:49.878333+00:00_

Web search results for query: "Grattafiori Llama 3 Herd of Models arXiv:2407.21783 2024 published venue"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"The Llama 3 Herd of Models Llama Team, AI @ Meta1","url":"https://arxiv.org/pdf/2407.21783v3"}]

Based on the search results, here's what I found about the paper:

**Title:** The Llama 3 Herd of Models

**ArXiv ID:** arXiv:2407.21783

**First Author:** Aaron Grattafiori

**Publication Date:** Submitted on 31 Jul 2024, last revised 23 Nov 2024

**Published Venue:** This paper is published on arXiv as a preprint. The search results indicate it is an arXiv paper in the computer science category, but it does not appear to have been published in a traditional peer-reviewed conference or journal venue as of the most recent version (v3).

**Content:** This paper presents a new set of foundation models, called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 239 · 2026-05-26T10:24:49.878501+00:00_

Web search results for query: ""When Attention Closes" Dongre openreview ICLR 2026 accepted"

Links: [{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"ICLR 2026 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/iclr-paper-list/iclr-2026-paper-list/"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026 Reviewer Guide","url":"https://iclr.cc/Conferences/2026/ReviewerGuide"},{"title":"2026 Conference","url":"https://iclr.cc/"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=202&venue=ICLR.cc/2026/Conference"},{"title":"ICLR 2026 Call for Papers","url":"https://iclr.cc/Conferences/2026/CallForPapers"},{"title":"An Attentive Survey of Attention Models","url":"https://arxiv.org/pdf/1904.02874"},{"title":"Learning representations of learning representations","url":"https://arxiv.org/pdf/2404.08403"}]

The search results show general information about ICLR 2026 but don't contain specific information about the paper "When Attention Closes" by Dongre. The results include references to ICLR 2026 OpenReview pages and general ICLR information, but the specific paper submission doesn't appear in these results.

Based on the search results returned, I was unable to find specific information about the paper "When Attention Closes" by Dongre in the ICLR 2026 accepted papers. The search returned general ICLR 2026 conference information, but the specific paper details you're looking for are not appearing in the available search results.

To find this paper, you might want to try:
1. Visiting OpenReview directly at https://openreview.net and searching for the paper title or author name
2. Checking the ICLR 2026 accepted papers list on the conference website
3. Searching ArXiv or other preprint servers with 
…[truncated 118 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 240 · 2026-05-26T10:24:49.878651+00:00_

Web search results for query: "Dauphin "Language Modeling with Gated Convolutional Networks" ICML 2017 arXiv 1612.08083"

Links: [{"title":"Language Modeling with Gated Convolutional Networks","url":"http://proceedings.mlr.press/v70/dauphin17a/dauphin17a.pdf"},{"title":"[1612.08083] Language Modeling with Gated Convolutional Networks","url":"https://arxiv.org/abs/1612.08083"},{"title":"dblp: Language Modeling with Gated Convolutional Networks.","url":"https://dblp.org/rec/conf/icml/DauphinFAG17.html"},{"title":"Language modeling with gated convolutional networks | Proceedings of the 34th International Conference on Machine Learning - Volume 70","url":"https://dl.acm.org/doi/10.5555/3305381.3305478"},{"title":"2017 LanguageModelingwithGatedConvol - GM-RKB","url":"http://www.gabormelli.com/RKB/2017_LanguageModelingwithGatedConvol"},{"title":"[PDF] Language Modeling with Gated Convolutional Networks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Language-Modeling-with-Gated-Convolutional-Networks-Dauphin-Fan/88caa4a0253a8b0076176745ebc072864eab66e1"},{"title":"(PDF) Language Modeling with Gated Convolutional Networks","url":"https://www.researchgate.net/publication/311900760_Language_Modeling_with_Gated_Convolutional_Networks"},{"title":"Language Modeling with Gated Convolutional Networks | Facebook AI Research","url":"https://ai.meta.com/research/publications/language-modeling-with-gated-convolutional-networks/"},{"title":"Language Modeling with Gated Convolutional Networks Yann N. Dauphin Angela Fan","url":"https://michaelauli.github.io/papers/gcnn.pdf"}]

I found the paper you're looking for. Here are the key details:

The paper "Language Modeling with Gated Convolutional Networks" was authored by Yann N. Dauphin, Angela Fan, Michael Auli, and David Grangier, and was published at ICML 2017 (pages 933-941).

The arXiv identifier is 1612.08083, with the first version submitted on December 23, 2016.

The paper's core contributions include:

- A finite
…[truncated 727 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-26T10:24:49.878808+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Attention Forcing for Machine Translation\" Dou Gales 2104.01264 EACL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Attention Forcing for Machine Translation\" Dou Gales 2104.01264 EACL 2023"
  }
}
```

</details>

---

### Tool result

_source line 242 · 2026-05-26T10:24:49.878940+00:00_

Web search results for query: "openreview.net 3x94uVDCeq "Explicating the Implicit" authors ICLR 2026 accepted"

Links: [{"title":"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation | OpenReview","url":"https://openreview.net/forum?id=3x94uVDCeq"},{"title":"Published as a conference paper at ICLR 2026 SYNERGIZING UNDERSTANDING","url":"https://openreview.net/pdf?id=GtqmPJf00A"},{"title":"ICLR 2026 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICLR 2026 Workshop Proposals | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop_Proposals"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=202&venue=ICLR.cc/2026/Conference"},{"title":"Venues | OpenReview","url":"https://openreview.net/"}]

Based on the search results, I found the paper you're looking for. The paper titled "Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation" theoretically shows that scaling model size or improving training alone cannot resolve the intent alignment gap in conversational contexts, and proposes a Mediator-Assistant architecture that decouples intent understanding from task execution by using an experience-driven Mediator to explicate user inputs into explicit, well-structured instructions based on historical interaction patterns.

The paper is available at openreview.net/forum?id=3x94uVDCeq. However, the search results don't explicitly list all the authors' names in detail. To get the complete author information, you would need to visit the OpenReview page directly at https://openreview.net/forum?id=3x
…[truncated 196 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 243 · 2026-05-26T10:24:49.879094+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shazeer Noam \"GLU Variants Improve Transformer\" arXiv 2002.05202 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shazeer Noam \"GLU Variants Improve Transformer\" arXiv 2002.05202 2020"
  }
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-26T10:24:49.879225+00:00_

Web search results for query: ""Rhea" "Role-aware Heuristic Episodic Attention" openreview ICLR 2026 ACL 2026 accepted"

Links: [{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/html/2512.06869v1"},{"title":"Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.arxiv.org/pdf/2512.06869"},{"title":"[2512.06869] Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://arxiv.org/abs/2512.06869"},{"title":"(PDF) Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs","url":"https://www.researchgate.net/publication/398476529_Rhea_Role-aware_Heuristic_Episodic_Attention_for_Conversational_LLMs"},{"title":"ICLR 2026 Conference Submissions","url":"https://openreview.net/submissions?page=54&venue=ICLR.cc/2026/Conference"},{"title":"ICLR 2026 Workshop Proposal MemAgents: Memory for LLM-Based Agentic Systems","url":"https://openreview.net/pdf?id=U51WxL382H"},{"title":"ICLR 2026 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FConference"},{"title":"PROPOSAL FOR ICLR 2026 WORKSHOP ON LOGICAL ...","url":"https://openreview.net/pdf?id=N6hLnZ9q47"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"}]

Based on the search results, I found information about the "Rhea" paper:

Rhea (Role-aware Heuristic Episodic Attention) is a novel framework that decouples conversation history into two functionally independent memory modules: (1) an Instructional Memory (IM) that persistently stores high-fidelity global constraints via a structural priority mechanism, and (2) an Episodic Memory (EM) that dynamically manages user-model interactions via asymmetric noise control and heuristic context retrieval.

During inference, Rhea constructs a high signal-to-noise context by applying its priority attention: selectively integrating relevant episodic information while always prioritizing global instructions.

…[truncated 444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 245 · 2026-05-26T10:24:49.879375+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Voita \"Analyzing Multi-Head Self-Attention\" ACL 2019 main conference proceedings venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Voita \"Analyzing Multi-Head Self-Attention\" ACL 2019 main conference proceedings venue"
  }
}
```

</details>

---

### Tool call

_source line 246 · 2026-05-26T10:24:49.879542+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Clark \"What Does BERT Look At\" ACL 2019 BlackboxNLP workshop proceedings venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Clark \"What Does BERT Look At\" ACL 2019 BlackboxNLP workshop proceedings venue"
  }
}
```

</details>

---

### Tool call

_source line 247 · 2026-05-26T10:24:49.879672+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Revealing the Dark Secrets of BERT\" Kovaleva EMNLP 2019 EMNLP-IJCNLP proceedings venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Revealing the Dark Secrets of BERT\" Kovaleva EMNLP 2019 EMNLP-IJCNLP proceedings venue"
  }
}
```

</details>

---

### Tool call

_source line 248 · 2026-05-26T10:24:49.879795+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "UltraChat Ding Ning EMNLP 2023 published proceedings venue aclanthology"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "UltraChat Ding Ning EMNLP 2023 published proceedings venue aclanthology"
  }
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-26T10:24:49.879921+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Brunner \"On Identifiability in Transformers\" authors Roger Wattenhofer Andreas Krause"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Brunner \"On Identifiability in Transformers\" authors Roger Wattenhofer Andreas Krause"
  }
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-26T10:24:49.880045+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Explicating the Implicit\" \"Intent Mismatch\" same paper arxiv 2602.07338 ICLR 2026 Liu Geng"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Explicating the Implicit\" \"Intent Mismatch\" same paper arxiv 2602.07338 ICLR 2026 Liu Geng"
  }
}
```

</details>

---

### Tool result

_source line 251 · 2026-05-26T10:24:49.880177+00:00_

Web search results for query: ""Attention Forcing for Machine Translation" Dou Gales 2104.01264 EACL 2023"

Links: [{"title":"[2104.01264] Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2104.01264"},{"title":"Attention Forcing for Machine Translation","url":"https://arxiv.org/pdf/2104.01264"},{"title":"Attention Forcing for Machine Translation","url":"https://axi.lims.ac.uk/paper/2104.01264"},{"title":"[2211.03237] Parallel Attention Forcing for Machine Translation","url":"https://arxiv.org/abs/2211.03237"},{"title":"Parallel Attention Forcing for Machine Translation Qingyun Dou and Mark Gales","url":"https://arxiv.org/pdf/2211.03237"},{"title":"[1909.12289] Attention Forcing for Sequence-to-sequence Model Training","url":"https://arxiv.org/abs/1909.12289"},{"title":"[1706.03762] Attention Is All You Need","url":"https://arxiv.org/abs/1706.03762"},{"title":"[1508.04025] Effective Approaches to Attention-based Neural Machine Translation","url":"https://arxiv.org/abs/1508.04025"},{"title":"[PDF] Effective Approaches to Attention-based Neural Machine Translation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Effective-Approaches-to-Attention-based-Neural-Luong-Pham/93499a7c7f699b6630a86fad964536f9423bb6d0"}]

Based on the search results, I found information about "Attention Forcing for Machine Translation" paper:

The paper is authored by Qingyun Dou, Yiting Lu, Potsawee Manakul, Xixin Wu, and Mark J. F. Gales.

The paper introduces attention forcing for NMT, which guides the model with the generated output history and reference attention, and can reduce the training-inference mismatch without a schedule or a classifier.

The core problem it addresses is that the standard training approach (teacher forcing) guides a model with the reference output history, but at inference stage the generated output history must be used, and this mismatch can impact performance. Several approaches have been proposed to address this problem, no
…[truncated 570 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 252 · 2026-05-26T10:24:49.880328+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Li Kenneth \"Measuring Controlling Instruction Instability\" COLM 2024 published proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Li Kenneth \"Measuring Controlling Instruction Instability\" COLM 2024 published proceedings"
  }
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-26T10:24:49.880471+00:00_

Web search results for query: "openreview.net rJe5_CNtPB "Attention Forcing" ICLR 2020 decision accepted rejected"

Links: [{"title":"Under review as a conference paper at ICLR 2020","url":"https://openreview.net/pdf?id=rJe5_CNtPB"},{"title":"Attention Forcing for Sequence-to-sequence Model Training | OpenReview","url":"https://openreview.net/forum?id=rJe5_CNtPB"},{"title":"Published as a conference paper at ICLR 2020","url":"https://openreview.net/pdf?id=rkgNKkHtvB"},{"title":"ICLR 2020 Conference | OpenReview","url":"https://openreview.net/group?id=ICLR.cc/2020/Conference"},{"title":"8th ICLR 2020: Addis Ababa, Ethiopia","url":"https://dblp.org/db/conf/iclr/iclr2020.html"},{"title":"ICLR | OpenReview","url":"https://openreview.net/group?id=ICLR.cc"},{"title":"Published as a conference paper at ICLR 2025","url":"https://openreview.net/pdf?id=1eQT9OzfNQ"},{"title":"OpenReview Support | OpenReview","url":"https://openreview.net/group?id=OpenReview.net%2FSupport"}]

Based on the search results, I found the paper on OpenReview. The paper titled "Attention Forcing for Sequence-to-sequence Model Training" describes a method to train attention-based sequence-to-sequence models. 

The paper introduces attention forcing, which guides the model with generated output history, and during inference, the attention forcing model operates in free running mode.

However, the search results show that the paper is "Under review as a conference paper at ICLR 2020", which indicates this was a submission under review. The search results do not contain explicit information about whether the paper was ultimately accepted or rejected at ICLR 2020. To find that specific decision information, you would need to visit the OpenReview forum page directly at https://openreview.net/forum?id=rJe5_CNtPB, which may contain the decision status and reviewer comments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-26T10:24:49.880706+00:00_

Now I have all the information needed. Let me compile the full verification report.

Here are the verification results for all 11 citations:

---

### [fan2020layerdrop] Fan, Grave, Joulin (2020) — Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)
- **Exists:** ✓
- **Authors:** ✓ — Angela Fan, Edouard Grave, Armand Joulin
- **Year:** ✓ — 2020
- **Title:** ✓ — Exact match
- **Venue:** ✓ — ICLR 2020 (confirmed via OpenReview and ICLR virtual site)
- **arXiv ID:** ✓ — 1909.11556
- **arXiv->published upgrade needed:** No
- **Notes:** Clean entry. No issues.

---

### [raposo2024mixture] Raposo et al. (2024) — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models
- **Exists:** ✓
- **Authors:** ✓ — David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro (note: OpenReview lists "Samuel Ritter" and "Blake A. Richards" and "Timothy P. Lillicrap" — the bib uses shorter forms, which is acceptable)
- **Year:** ✗ — The bib says 2024 and lists "ICML", but the paper was **published as a conference paper at ICLR 2025** (confirmed via OpenReview ID WwpYSOkkCt and ICLR proceedings PDF header). It was NOT published at ICML 2024.
- **Title:** ✓ — Exact match (though original uses lowercase "allocating" and "transformer-based" — minor style)
- **Venue:** ✗ — Should be **ICLR 2025**, not ICML 2024
- **arXiv ID:** ✓ — 2404.02258
- **arXiv->published upgrade needed:** N/A (already uses `@inproceedings`, but venue/year are wrong)
- **Notes:** **CRITICAL FIX NEEDED.** Change `booktitle` to `{International Conference on Learning Representations}`, change `year` to `2025`, and update bib key to `raposo2025mixture` if desired.

---

### [schuster2022calm] Schuster et al. (2022) — Confident Adaptive Language Modeling
- **Exists:** ✓
- **Authors:** ✓ — Tal Schuster, Adam Fisch, Jai Gupta, Mostafa Dehghani, Dara Bahri, Vinh Q. Tran, Yi Tay, Donald Metzler
- **Year:** ✓ — 2022
- **Title:** ✓ — Exact ma
…[truncated 5843 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "elapsed_ms": 30
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-26T10:24:49.880872+00:00_

Web search results for query: "Shazeer Noam "GLU Variants Improve Transformer" arXiv 2002.05202 2020"

Links: [{"title":"[2002.05202] GLU Variants Improve Transformer","url":"https://arxiv.org/abs/2002.05202"},{"title":"GLU Variants Improve Transformer | Request PDF","url":"https://www.researchgate.net/publication/339252250_GLU_Variants_Improve_Transformer"},{"title":"GLU Variants Improve Transformer | alphaXiv","url":"https://www.alphaxiv.org/overview/2002.05202v1"},{"title":"[2002.05202] GLU Variants Improve Transformer - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2002.05202"},{"title":"arXiv:2002.05202v1 [cs.LG] 12 Feb 2020 GLU Variants Improve Transformer","url":"https://arxiv.org/pdf/2002.05202"},{"title":"GitHub - ngdonna2020/glu: GLU variants improve transformer · GitHub","url":"https://github.com/ngdonna2020/glu"},{"title":"[2002.05202v1] GLU Variants Improve Transformer","url":"https://arxiv.org/abs/2002.05202v1"},{"title":"GLU Variants Boost Transformer Performance","url":"https://www.emergentmind.com/papers/2002.05202"}]

Based on the search results, I found the paper you're looking for:

"GLU Variants Improve Transformer" is an arXiv paper (2002.05202) submitted on February 12, 2020 by Noam Shazeer from Google. 

The paper discusses Gated Linear Units (GLUs), which consist of the component-wise product of two linear projections where one is passed through a sigmoid function. Variations on GLU are possible using different nonlinear or linear functions in place of sigmoid, and the author tests these variants in the feed-forward sublayers of the Transformer sequence-to-sequence model, finding that some of them yield quality improvements over the typically-used ReLU or GELU activations.

The paper is available on arXiv at https://arxiv.org/abs/2002.05202.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-26T10:24:49.881032+00:00_

Web search results for query: "Voita "Analyzing Multi-Head Self-Attention" ACL 2019 main conference proceedings venue"

Links: [{"title":"GitHub - lena-voita/the-story-of-heads: This is a repository with the code for the ACL 2019 paper \"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\" and the ACL 2021 paper \"Analyzing Source and Target Contributions to NMT Predictions\". · GitHub","url":"https://github.com/lena-voita/the-story-of-heads"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - ACL Anthology","url":"https://aclanthology.org/P19-1580/"},{"title":"[1905.09418] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://arxiv.org/abs/1905.09418"},{"title":"The Story of Heads","url":"https://lena-voita.github.io/posts/acl19_heads.html"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/analyzing-multi-head-self-attention-specialized-heads-do-the-heav/"},{"title":"lena-voita (Lena Voita) · GitHub","url":"https://github.com/lena-voita"},{"title":"Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https://bibbase.org/network/publication/voita-talbot-moiseev-sennrich-titov-analyzingmultiheadselfattentionspecializedheadsdotheheavyliftingtherestcanbepruned-2019"},{"title":"[PDF] Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Analyzing-Multi-Head-Self-Attention:-Specialized-Do-Voita-Talbot/07a64686ce8e43ac475a8d820a8a9f1d87989583"},{"title":"Papers with Code - Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned","url":"https
…[truncated 607 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 257 · 2026-05-26T10:24:49.881188+00:00_

Web search results for query: ""Revealing the Dark Secrets of BERT" Kovaleva EMNLP 2019 EMNLP-IJCNLP proceedings venue"

Links: [{"title":"Revealing the Dark Secrets of BERT - ACL Anthology","url":"https://aclanthology.org/D19-1445/"},{"title":"[PDF] Revealing the Dark Secrets of BERT | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Revealing-the-Dark-Secrets-of-BERT-Kovaleva-Romanov/d78aed1dac6656affa4a04cbf225ced11a83d103"},{"title":"Revealing the Dark Secrets of BERT","url":"https://bibbase.org/network/publication/kovaleva-romanov-rogers-rumshisky-revealingthedarksecretsofbert-2019"},{"title":"Revealing the Dark Secrets of BERT - University of Copenhagen Research Portal","url":"https://researchprofiles.ku.dk/en/publications/revealing-the-dark-secrets-of-bert/"},{"title":"Revealing the Dark Secrets of BERT | Request PDF","url":"https://www.researchgate.net/publication/336999411_Revealing_the_Dark_Secrets_of_BERT"},{"title":"The Dark Secrets of BERT | Text Machine Blog","url":"https://text-machine-lab.github.io/blog/2020/bert-secrets/"},{"title":"(Open Access) Revealing the Dark Secrets of BERT (2019) | Olga Kovaleva | 466 Citations","url":"https://typeset.io/papers/revealing-the-dark-secrets-of-bert-509elm9ak9"},{"title":"Revealing the Dark Secrets of BERT - IT-University of Copenhagen","url":"https://pure.itu.dk/en/publications/revealing-the-dark-secrets-of-bert/"}]

Based on the search results, here are the details about the paper:

**"Revealing the Dark Secrets of BERT"** is a paper by Olga Kovaleva, Alexey Romanov, Anna Rogers, and Anna Rumshisky, published in the Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 4365–4374, Hong Kong, China.

The paper's key contribution involves a qualitative and quantitative analysis of the information encoded by individual BERT's heads using a subset of GLUE tasks and a set of 
…[truncated 502 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 258 · 2026-05-26T10:24:49.881341+00:00_

Web search results for query: "Clark "What Does BERT Look At" ACL 2019 BlackboxNLP workshop proceedings venue"

Links: [{"title":"What Does BERT Look at? An Analysis of BERT’s Attention - ACL Anthology","url":"https://aclanthology.org/W19-4828/"},{"title":"What Does BERT Look at? An Analysis of BERT's Attention - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/what-does-bert-look-at-an-analysis-of-berts-attention/"},{"title":"What Does BERT Look at? An Analysis of BERT’s Attention | Request PDF","url":"https://www.researchgate.net/publication/335778955_What_Does_BERT_Look_at_An_Analysis_of_BERT's_Attention"},{"title":"Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP","url":"https://1library.net/document/q0579l3y-proceedings-acl-workshop-blackboxnlp-analyzing-interpreting-neural-networks.html"},{"title":"What Does BERT Look at? An Analysis of BERT’s Attention | CiNii Research","url":"https://cir.nii.ac.jp/crid/1361981470578490112"},{"title":"2nd BlackboxNLP@ACL 2019: Florence, Italy","url":"https://dblp.org/db/conf/blackboxnlp/blackboxnlp2019.html"},{"title":"(PDF) What Does BERT Look at? An Analysis of BERT’s Attention","url":"https://www.academia.edu/121847697/What_Does_BERT_Look_at_An_Analysis_of_BERT_s_Attention"},{"title":"Fine-Tuning BERT on Coarse-Grained Labels: Exploring Hidden States for Fine-Grained Classification | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-70239-6_1"},{"title":"What Does BERT Look At? An Analysis of BERT’s Attention Kevin Clark†","url":"https://www-nlp.stanford.edu/pubs/clark2019what.pdf"}]

Based on the search results, here are the details about the Clark paper "What Does BERT Look At":

The paper "What Does BERT Look at? An Analysis of BERT's Attention" was authored by Kevin Clark, Urvashi Khandelwal, Omer Levy, and Christopher D. Manning and was published in the Proceedings of the 2019 ACL Workshop BlackboxNLP: Analyzing and In
…[truncated 236 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 259 · 2026-05-26T10:24:49.881522+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Lin Stephanie Hilton Jacob \"TruthfulQA: Measuring How Models Mimic Human Falsehoods\" ACL 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Lin Stephanie Hilton Jacob \"TruthfulQA: Measuring How Models Mimic Human Falsehoods\" ACL 2022"
  }
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-26T10:24:49.881657+00:00_

Web search results for query: "UltraChat Ding Ning EMNLP 2023 published proceedings venue aclanthology"

Links: [{"title":"Enhancing Chat Language Models by Scaling High-quality Instructional Conversations - ACL Anthology","url":"https://aclanthology.org/2023.emnlp-main.183/"},{"title":"Aclanthology","url":"https://aclanthology.org/2023.emnlp-main.183.pdf"},{"title":"EMNLP 2023 — 3 main conference papers accepted! | TsinghuaC3I","url":"https://c3i.ee.tsinghua.edu.cn/en/post/23-10-08-emnlp/"},{"title":"The 2023 Conference on Empirical Methods in Natural Language Processing - ACL Anthology","url":"https://aclanthology.org/events/emnlp-2023/"},{"title":"EMNLP 2023 The 2023 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2023.emnlp-main.0.pdf"},{"title":"EMNLP 2023 Accepted Paper List - Paper Copilot","url":"https://papercopilot.com/paper-list/emnlp-paper-list/emnlp-2023-paper-list/"},{"title":"UltraIF: Advancing Instruction Following from the Wild - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.945/"},{"title":"Towards Making the Most of ChatGPT for Machine Translation - ACL Anthology","url":"https://aclanthology.org/2023.findings-emnlp.373/"}]

Based on the search results, I found the information about the UltraChat paper:

The UltraChat paper by Ding Ning and colleagues titled "Enhancing Chat Language Models by Scaling High-quality Instructional Conversations" was published in the Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing (pages 3029–3051, Singapore).

It was published by the Association for Computational Linguistics, and the paper provides a systematically designed, diverse, informative, large-scale dataset of instructional conversations, UltraChat.

The paper is available on ACL Anthology at: https://aclanthology.org/2023.emnlp-main.183/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-26T10:24:49.881803+00:00_

Web search results for query: ""Explicating the Implicit" "Intent Mismatch" same paper arxiv 2602.07338 ICLR 2026 Liu Geng"

Links: [{"title":"[2602.07338] Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/abs/2602.07338"},{"title":"Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://arxiv.org/html/2602.07338v1"},{"title":"(PDF) Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation","url":"https://www.researchgate.net/publication/400604289_Intent_Mismatch_Causes_LLMs_to_Get_Lost_in_Multi-Turn_Conversation"},{"title":"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation | OpenReview","url":"https://openreview.net/forum?id=3x94uVDCeq"},{"title":"Mitigating Mismatch within Reference-based Preference Optimization","url":"https://arxiv.org/html/2602.11902"},{"title":"Explicating the Implicit: Argument Detection Beyond Sentence Boundaries","url":"https://www.arxiv.org/pdf/2408.04246"},{"title":"Explicating the Implicit: Argument Detection Beyond Sentence Boundaries","url":"https://arxiv.org/html/2408.04246"}]

Based on the search results, I found the paper you're looking for:

"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation" addresses the phenomenon termed "Lost in Conversation" (LiC), where LLMs suffer a substantial performance drop in multi-turn settings compared to single-turn interactions.

The paper's key contributions include:

1. **Problem Identification**: The authors argue that the root cause of LiC lies in an intent alignment gap rather than intrinsic capability deficits, demonstrating that it is not a failure of model capability but rather a breakdown in interaction between users and LLMs, arising from structural ambiguity in conversational context rather than representational limitations.

2. **Proposed Solution**: The paper proposes to decouple intent understanding from task execution through a Mediat
…[truncated 350 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-26T10:24:49.881957+00:00_

Web search results for query: "Li Kenneth "Measuring Controlling Instruction Instability" COLM 2024 published proceedings"

Links: [{"title":"[2402.10962] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | OpenReview","url":"https://openreview.net/forum?id=60a1SAtH4e"},{"title":"[2402.10962v4] Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/abs/2402.10962v4"},{"title":"COLM 2024: Accepted Papers","url":"https://colmweb.org/2024/AcceptedPapers.html"},{"title":"Controlling Instruction Drift in LLM Dialogs","url":"https://api.emergentmind.com/papers/2402.10962"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs - AI Research Paper Analysis | ArxivLens - Arxivlens","url":"https://arxivlens.com/paperview/details/measuring-and-controlling-instruction-instability-in-language-model-dialogs-7499-1350985"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/measuring-controlling-instruction-instability-language-model-dialogs"},{"title":"Measuring and Controlling Instruction (In)Stability in Language Model Dialogs","url":"https://arxiv.org/html/2402.10962v2"}]

Based on the search results, I found the paper you're looking for:

**Title:** Measuring and Controlling Instruction (In)Stability in Language Model Dialogs

**Authors:** Kenneth Li, Tianle Liu, Naomi Bashkansky, David Bau, Fernanda Viégas, Hanspeter Pfister, Martin Wattenberg

**Publication:** The paper was published at COLM 2024 on July 10, 2024

**Overview:** The paper proposes a quantitative benchmark to test instruction stability via self-chats between two instructed chatbots, testing popular models like LLaMA2-chat-70B and GPT-3.5, and reveals significant i
…[truncated 522 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-26T10:24:49.882112+00:00_

Web search results for query: "Lin Stephanie Hilton Jacob "TruthfulQA: Measuring How Models Mimic Human Falsehoods" ACL 2022"

Links: [{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods - ACL Anthology","url":"https://aclanthology.org/2022.acl-long.229/"},{"title":"TruthfulQA: Measuring How Models Mimic Human ...","url":"https://aclanthology.org/2022.acl-long.229.pdf"},{"title":"[2109.07958] TruthfulQA: Measuring How Models Mimic Human Falsehoods","url":"https://arxiv.org/abs/2109.07958"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods","url":"https://www.researchgate.net/publication/361063493_TruthfulQA_Measuring_How_Models_Mimic_Human_Falsehoods"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/1e808a2538c58d9338699b0312abec8f3"},{"title":"dblp: Stephanie Lin","url":"https://dblp.org/pid/55/11455.html"},{"title":"[PDF] TruthfulQA: Measuring How Models Mimic Human Falsehoods | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TruthfulQA:-Measuring-How-Models-Mimic-Human-Lin-Hilton/77d956cdab4508d569ae5741549b78e715fd0749"},{"title":"lm-evaluation-harness/lm_eval/tasks/truthfulqa at feff1b55c57993c4d42c8f913a22eeec395cd690 · EleutherAI/lm-evaluation-harness","url":"https://github.com/EleutherAI/lm-evaluation-harness/tree/feff1b55c57993c4d42c8f913a22eeec395cd690/lm_eval/tasks/truthfulqa"},{"title":"TruthfulQA: Measuring How Models Mimic Human Falsehoods","url":"https://bibbase.org/network/publication/lin-hilton-evans-truthfulqameasuringhowmodelsmimichumanfalsehoods-2022"},{"title":"TruthfulQA | AI Wiki","url":"https://aiwiki.ai/wiki/truthfulqa"}]

I found the paper you're looking for! Here are the details:

## TruthfulQA: Measuring How Models Mimic Human Falsehoods

**Authors:** Stephanie Lin, Jacob Hilton, and Owain Evans

**Publication:** Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers),
…[truncated 664 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-26T10:24:49.882267+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Hendrycks Dan Burns Collin \"Measuring Massive Multitask Language Understanding\" ICLR 2021 arXiv 2009.03300"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Hendrycks Dan Burns Collin \"Measuring Massive Multitask Language Understanding\" ICLR 2021 arXiv 2009.03300"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-26T10:24:49.882419+00:00_

Web search results for query: "Brunner "On Identifiability in Transformers" authors Roger Wattenhofer Andreas Krause"

Links: [{"title":"[PDF] On Identifiability in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Identifiability-in-Transformers-Brunner-Liu/1fe62a928bf5cfac0f373728f3a4de3cefe0951d"},{"title":"[1908.04211] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211"},{"title":"Published as a conference paper at ICLR 2020 ON IDENTIFIABILITY IN TRANSFORMERS","url":"https://tik-old.ee.ethz.ch/file/84248b631689290b665ce39984611681/on_identifiability_in_transformers.pdf"},{"title":"On Identifiability in Transformers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190804211B/abstract"},{"title":"[1908.04211v4] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211v4"},{"title":"(PDF) On Identifiability in Transformers","url":"https://www.researchgate.net/publication/339377132_On_Identifiability_in_Transformers"},{"title":"On Identifiability in Transformers – Google Research","url":"https://research.google/pubs/pub48972/"},{"title":"On Identifiability in Transformers","url":"https://research.google/pubs/on-identifiability-in-transformers/"},{"title":"On Identifiability in Transformers - Paper Detail","url":"https://deeplearn.org/arxiv/114546/on-identifiability-in-transformers"},{"title":"On Identifiability in Transformers | OpenReview","url":"https://openreview.net/forum?id=BJg1f6EFDB"}]

Based on the search results, I found information about the paper "On Identifiability in Transformers":

The authors are Gino Brunner, Yang Liu, Damián Pascual, Oliver Richter, Massimiliano Ciaramita, and Roger Wattenhofer. 

However, I should note that **Andreas Krause is not listed as an author** of this paper. The paper was published at ICLR 2020 and the authors were affiliated with the Departments of Electrical Engineering and Information Technology and Computer Science at ETH Zurich, and Goog
…[truncated 361 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 266 · 2026-05-26T10:24:49.882580+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "dongre2026|hong2025rhea|laban2025lost|liu2026intent|bai2024mtbench|li2024measuring|xiao2024streaming|zhang2024tell|hsieh2024found|qiu2025gated",
  "glob": "*.bib",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "dongre2026|hong2025rhea|laban2025lost|liu2026intent|bai2024mtbench|li2024measuring|xiao2024streaming|zhang2024tell|hsieh2024found|qiu2025gated",
    "glob": "*.bib",
    "output_mode": "files_with_matches"
  }
}
```

</details>

---

### Tool result

_source line 267 · 2026-05-26T10:24:49.882707+00:00_

Found 3 files
paper/references.bib
artifacts/dream_reports/dream_20260519T145320/best/custom.bib
artifacts/dream_reports/dream_20260519T135115/median/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 268 · 2026-05-26T10:24:49.882834+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 1908.04211 \"On Identifiability in Transformers\" full author list Brunner Liu Pascual Richter Ciaramita Wattenhofer"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 1908.04211 \"On Identifiability in Transformers\" full author list Brunner Liu Pascual Richter Ciaramita Wattenhofer"
  }
}
```

</details>

---

### Tool call

_source line 269 · 2026-05-26T10:24:49.882963+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2307.03172 \"Lost in the Middle\" full author list Nelson Liu Kevin Lin John Hewitt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2307.03172 \"Lost in the Middle\" full author list Nelson Liu Kevin Lin John Hewitt"
  }
}
```

</details>

---

### Tool result

_source line 270 · 2026-05-26T10:24:49.883092+00:00_

Web search results for query: "Hendrycks Dan Burns Collin "Measuring Massive Multitask Language Understanding" ICLR 2021 arXiv 2009.03300"

Links: [{"title":"GitHub - hendrycks/test: Measuring Massive Multitask Language Understanding | ICLR 2021 · GitHub","url":"https://github.com/hendrycks/test"},{"title":"GitHub - hendrycks/test: Measuring Massive Multitask Language Understanding | ICLR 2021","url":"https://github.com/hendrycks/test?tab=readme-ov-file"},{"title":"Measuring Massive Multitask Language Understanding | OpenReview","url":"https://openreview.net/forum?id=d7KBjmI3GmQ"},{"title":"Measuring Massive Multitask Language Understanding","url":"https://orkg.org/papers/R461192/R644448"},{"title":"test/README.md at master · hendrycks/test","url":"https://github.com/hendrycks/test/blob/master/README.md"},{"title":"GitHub - standardgalactic/mmlu: Measuring Massive Multitask Language Understanding | ICLR 2021 · GitHub","url":"https://github.com/standardgalactic/mmlu"},{"title":"Published as a conference paper at ICLR 2021 MEASURING MASSIVE MULTITASK","url":"https://openreview.net/pdf?id=d7KBjmI3GmQ"},{"title":"GitHub - Helw150/mmlu: Measuring Massive Multitask Language Understanding | ICLR 2021","url":"https://github.com/Helw150/mmlu"},{"title":"Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, Jacob Steinhardt · Measuring Massive Multitask Language Understanding","url":"https://slideslive.com/38953931/measuring-massive-multitask-language-understanding"},{"title":"MEASURING MASSIVE MULTITASK LANGUAGE UNDERSTANDING (MMLU)","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/vajpayee_zhao_mmlu.pdf"}]

I found comprehensive information about the paper "Measuring Massive Multitask Language Understanding" by Hendrycks and Burns.

## Summary of Results

The paper "Measuring Massive Multitask Language Understanding" was authored by Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou, Mantas Mazeika, Dawn Song, and Jac
…[truncated 1098 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 271 · 2026-05-26T10:24:49.883239+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "dongre2026|hong2025rhea|laban2025lost|liu2026intent|bai2024mtbench|li2024measuring|xiao2024streaming|zhang2024tell|hsieh2024found|qiu2025gated",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
  "output_mode": "content",
  "-C": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "tool_args": {
    "pattern": "dongre2026|hong2025rhea|laban2025lost|liu2026intent|bai2024mtbench|li2024measuring|xiao2024streaming|zhang2024tell|hsieh2024found|qiu2025gated",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/paper/references.bib",
    "output_mode": "content",
    "-C": "15"
  }
}
```

</details>

---

### Tool result

_source line 272 · 2026-05-26T10:24:49.883392+00:00_

1-% ============================================================
2-% Multi-Turn Attention
3-% ============================================================
4-
5:@article{dongre2026attention,
6-  author  = {Dongre, Vardhan and Hsieh, Joseph and Lai, Viet Dac and Yoon, Seunghyun and Bui, Trung and Hakkani-T\"{u}r, Dilek},
7-  title   = {{When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction}},
8-  journal = {arXiv preprint arXiv:2605.12922},
9-  year    = {2026},
10-  url     = {https://arxiv.org/abs/2605.12922}
11-}
12-
13:@article{hong2025rhea,
14-  author  = {Hong, Wanyang and Zhang, Zhaoning and Chen, Yi and Zhang, Libo and Liu, Baihui and Qiao, Linbo and Tian, Zhiliang and Li, Dongsheng},
15-  title   = {{Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs}},
16-  journal = {arXiv preprint arXiv:2512.06869},
17-  year    = {2025},
18-  url     = {https://arxiv.org/abs/2512.06869}
19-}
20-
21:@article{laban2025lost,
22-  author  = {Laban, Philippe and Hayashi, Hiroaki and Zhou, Yingbo and Neville, Jennifer},
23-  title   = {{LLMs Get Lost In Multi-Turn Conversation}},
24-  journal = {arXiv preprint arXiv:2505.06120},
25-  year    = {2025},
26-  url     = {https://arxiv.org/abs/2505.06120}
27-}
28-
29:@article{liu2026intent,
30-  author  = {Liu, Geng and Zhu, Fei and Feng, Rong and Ma, Changyi and Wang, Shiqi and Meng, Gaofeng},
31-  title   = {{Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation}},
32-  journal = {arXiv preprint arXiv:2602.07338},
33-  year    = {2026},
34-  url     = {https://arxiv.org/abs/2602.07338}
35-}
36-
37:@inproceedings{bai2024mtbench101,
38-  author    = {Bai, Ge and Liu, Jie and Bu, Xingyuan and He, Yancheng and Liu, Jiaheng and Zhou, Zhanhui and Lin, Zhuoran and Su, Wenbo and Ge, Tiezheng and Zheng, Bo and Ouyang, Wanli},
39-  title     = {{MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues}},
40-  booktitle = {Annual Meeting of the Ass
…[truncated 5773 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 273 · 2026-05-26T10:24:49.883583+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Llama 3 Herd of Models arxiv 2407.21783 first author \"Dubey\" OR \"Grattafiori\" \"Llama Team\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Llama 3 Herd of Models arxiv 2407.21783 first author \"Dubey\" OR \"Grattafiori\" \"Llama Team\""
  }
}
```

</details>

---

### Tool call

_source line 274 · 2026-05-26T10:24:49.883718+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Li Jiwei\" \"Persona-Based Neural Conversation\" authors Spithourakis OR \"Georgios P.\" full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Li Jiwei\" \"Persona-Based Neural Conversation\" authors Spithourakis OR \"Georgios P.\" full author list"
  }
}
```

</details>

---

### Tool call

_source line 275 · 2026-05-26T10:24:49.883845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dettmers Tim Pagnoni Artidoro \"QLoRA: Efficient Finetuning of Quantized LLMs\" NeurIPS 2023 arXiv 2305.14314"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dettmers Tim Pagnoni Artidoro \"QLoRA: Efficient Finetuning of Quantized LLMs\" NeurIPS 2023 arXiv 2305.14314"
  }
}
```

</details>

---

### Tool call

_source line 276 · 2026-05-26T10:24:49.883970+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL anthology 2024.findings-acl.890 \"Found in the Middle\" authors \"Long Le\" OR \"Long T. Le\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL anthology 2024.findings-acl.890 \"Found in the Middle\" authors \"Long Le\" OR \"Long T. Le\""
  }
}
```

</details>

---

### Tool result

_source line 277 · 2026-05-26T10:24:49.884092+00:00_

Web search results for query: "arxiv 1908.04211 "On Identifiability in Transformers" full author list Brunner Liu Pascual Richter Ciaramita Wattenhofer"

Links: [{"title":"[1908.04211] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211"},{"title":"Published as a conference paper at ICLR 2020 ON IDENTIFIABILITY IN TRANSFORMERS","url":"https://arxiv.org/pdf/1908.04211"},{"title":"On Identifiability in Transformers - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190804211B/abstract"},{"title":"[1908.04211v4] On Identifiability in Transformers","url":"https://arxiv.org/abs/1908.04211v4"},{"title":"More Identiﬁable yet Equally Performant Transformers for Text Classiﬁcation","url":"https://arxiv.org/pdf/2106.01269"},{"title":"ON IDENTIFIABILITY IN TRANSFORMERS","url":"https://www.readkong.com/page/on-identifiability-in-transformers-4380972"},{"title":"[PDF] On Identifiability in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-Identifiability-in-Transformers-Brunner-Liu/1fe62a928bf5cfac0f373728f3a4de3cefe0951d"},{"title":"Universal Approximability of Sparse Transformers","url":"https://arxiv.org/pdf/2006.04862"}]

Based on the search results, the full author list for arxiv 1908.04211 "On Identifiability in Transformers" is: Gino Brunner, Yang Liu, Damián Pascual, Oliver Richter, Massimiliano Ciaramita, and Roger Wattenhofer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 278 · 2026-05-26T10:24:49.884235+00:00_

Web search results for query: ""Li Jiwei" "Persona-Based Neural Conversation" authors Spithourakis OR "Georgios P." full author list"

Links: [{"title":"A Persona-Based Neural Conversation Model - ACL Anthology","url":"https://aclanthology.org/P16-1094/"},{"title":"[1603.06155] A Persona-Based Neural Conversation Model","url":"https://arxiv.org/abs/1603.06155"},{"title":"Jiwei's Homepage","url":"https://nlp.stanford.edu/~bdlijiwei/Publications_ByTopic.html"},{"title":"A Persona-Based Neural Conversation Model Jiwei Li1* Michel Galley2","url":"https://arxiv.org/pdf/1603.06155"},{"title":"A Persona-Based Neural Conversation Model : Jiwei Li : Free Download, Borrow, and Streaming : Internet Archive","url":"https://archive.org/details/arxiv-1603.06155"},{"title":"A Persona-Based Neural Conversation Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/2016arXiv160306155L/abstract"},{"title":"A Persona-Based Neural Conversation Model","url":"https://aclanthology.org/P16-1094.pdf"},{"title":"A Persona-Based Neural Conversation Model | Request PDF","url":"https://www.researchgate.net/publication/306093549_A_Persona-Based_Neural_Conversation_Model"},{"title":"A Persona-Based Neural Conversation Model: Enhancements & Results - Studocu","url":"https://www.studocu.com/row/document/jimma-university/computer-networking/a-persona-based-neural-conversation-model/69156333"},{"title":"[1603.06155v2] A Persona-Based Neural Conversation Model","url":"https://arxiv.org/abs/1603.06155v2"}]

Based on the search results, here is the complete author list for "A Persona-Based Neural Conversation Model":

The authors are: Jiwei Li, Michel Galley, Chris Brockett, Georgios P. Spithourakis, Jianfeng Gao, and Bill Dolan.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 279 · 2026-05-26T10:24:49.884370+00:00_

Web search results for query: "Llama 3 Herd of Models arxiv 2407.21783 first author "Dubey" OR "Grattafiori" "Llama Team""

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"The Llama 3 Herd of Models","url":"https://arxiv.org/pdf/2407.21783"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 herd of models - Archive ouverte HAL","url":"https://hal.science/hal-05414211"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"}]

I found the paper! Here are the search results for arxiv 2407.21783:

The paper presents a new set of foundation models called Llama 3, which is a herd of language models that natively support multilinguality, coding, reasoning, and tool usage. The largest model is a dense Transformer with 405B parameters and a context window of up to 128K tokens.

The paper is authored by Aaron Grattafiori and 558 other authors (in the latest version v3), though earlier versions list Abhimanyu Dubey as the first author with 530 other authors.

Llama 3 delivers comparable quality to leading language models such as GPT-4 on a plethora of tasks. The paper also presents results of experiments integrating image, video, and speech capabilities into Llama 3 via a compositional approach.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 280 · 2026-05-26T10:24:49.884535+00:00_

Web search results for query: "ACL anthology 2024.findings-acl.890 "Found in the Middle" authors "Long Le" OR "Long T. Le""

Links: [{"title":"Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.890/"},{"title":"Found in the Middle: Permutation Self-Consistency Improves Listwise Ranking in Large Language Models - ACL Anthology","url":"https://aclanthology.org/2024.naacl-long.129/"},{"title":"Lost in the Middle: How Language Models Use Long Contexts - ACL Anthology","url":"https://aclanthology.org/2024.tacl-1.9/"},{"title":"Never Lost in the Middle: Mastering Long-Context Question Answering with Position-Agnostic Decompositional Training - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.736/"},{"title":"Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.0/"},{"title":"2024.acl-long.0.pdf","url":"https://aclanthology.org/2024.acl-long.0.pdf"}]

Perfect! I found the paper you were searching for. 

The paper "Found in the middle: Calibrating Positional Attention Bias Improves Long Context Utilization" from ACL 2024 Findings includes Long Le as one of the authors. The complete author list is: Cheng-Yu Hsieh, Yung-Sung Chuang, Chun-Liang Li, Zifeng Wang, Long Le, Abhishek Kumar, James Glass, Alexander Ratner, Chen-Yu Lee, Ranjay Krishna, and Tomas Pfister.

The paper was published in the Findings of the Association for Computational Linguistics: ACL 2024, pages 14982–14995, in Bangkok, Thailand.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 281 · 2026-05-26T10:24:49.884683+00:00_

Web search results for query: "Dettmers Tim Pagnoni Artidoro "QLoRA: Efficient Finetuning of Quantized LLMs" NeurIPS 2023 arXiv 2305.14314"

Links: [{"title":"QLORA: Efficient Finetuning of Quantized LLMs Tim Dettmers∗ Artidoro Pagnoni∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/1feb87871436031bdc0f2beaa62a049b-Paper-Conference.pdf"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs | OpenReview","url":"https://openreview.net/forum?id=OUIFPHEgJU"},{"title":"[2305.14314] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://arxiv.org/abs/2305.14314"},{"title":"QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/1feb87871436031bdc0f2beaa62a049b-Abstract-Conference.html"},{"title":"NeurIPS Poster QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://neurips.cc/virtual/2023/poster/71815"},{"title":"QLORA: efficient finetuning of quantized LLMs","url":"https://dl.acm.org/doi/10.5555/3666122.3666563"},{"title":"NeurIPS 2023 QLoRA: Efficient Finetuning of Quantized LLMs Oral","url":"https://nips.cc/virtual/2023/oral/73855"},{"title":"[Quick Review] QLoRA: Efficient Finetuning of Quantized LLMs","url":"https://liner.com/review/qlora-efficient-finetuning-of-quantized-llms"},{"title":"Brief Review — QLoRA: Efficient Finetuning of Quantized LLMs | by Sik-Ho Tsang | Medium","url":"https://sh-tsang.medium.com/brief-review-qlora-efficient-finetuning-of-quantized-llms-6f20a7255701"}]

I found comprehensive information about the paper you searched for. Here are the results:

## QLoRA: Efficient Finetuning of Quantized LLMs

The paper is authored by Tim Dettmers and 3 other authors and published on arXiv with identifier 2305.14314. It was presented at NeurIPS 2023 as an oral presentation.

### Key Contribution

QLoRA is an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning
…[truncated 920 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 282 · 2026-05-26T10:24:49.884839+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2001.06782 authors \"Tianhe Yu\" OR \"Tianhe Kevin Yu\" PCGrad"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2001.06782 authors \"Tianhe Yu\" OR \"Tianhe Kevin Yu\" PCGrad"
  }
}
```

</details>

---

### Tool result

_source line 283 · 2026-05-26T10:24:49.884968+00:00_

Web search results for query: "arxiv 2307.03172 "Lost in the Middle" full author list Nelson Liu Kevin Lin John Hewitt"

Links: [{"title":"[2307.03172] Lost in the Middle: How Language Models Use Long Contexts","url":"https://arxiv.org/abs/2307.03172"},{"title":"[2307.03172] Lost in the Middle: How Language Models Use Long Contexts","url":"https://ar5iv.labs.arxiv.org/html/2307.03172"},{"title":"Lost in the Middle: How Language Models Use Long Contexts Nelson F. Liu1∗","url":"https://arxiv.org/pdf/2307.03172"},{"title":"Paper page - Lost in the Middle: How Language Models Use Long Contexts","url":"https://huggingface.co/papers/2307.03172"},{"title":"Practical AI/ML Paper reading： “Lost in the Middle”: How Language Models Use Long Contexts | by Christmas Carol | Medium","url":"https://medium.com/@carolzhu/lost-in-the-middle-how-language-models-use-long-contexts-2891830f8000"},{"title":"GitHub - nelson-liu/lost-in-the-middle: Code and data for \"Lost in the Middle: How Language Models Use Long Contexts\" · GitHub","url":"https://github.com/nelson-liu/lost-in-the-middle"},{"title":"[2307.03172v3] Lost in the Middle: How Language Models Use Long Contexts","url":"https://arxiv.org/abs/2307.03172v3"},{"title":"[2307.03172v1] Lost in the Middle: How Language Models Use Long Contexts","url":"https://arxiv.org/abs/2307.03172v1"}]

Based on the search results, the full author list for arXiv paper 2307.03172 "Lost in the Middle: How Language Models Use Long Contexts" is: Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 284 · 2026-05-26T10:24:49.885114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2407.21783v1 \"Dubey\" first author vs v3 \"Grattafiori\" first author Llama 3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2407.21783v1 \"Dubey\" first author vs v3 \"Grattafiori\" first author Llama 3"
  }
}
```

</details>

---

### Tool result

_source line 285 · 2026-05-26T10:24:49.885247+00:00_

Web search results for query: "arXiv 2001.06782 authors "Tianhe Yu" OR "Tianhe Kevin Yu" PCGrad"

Links: [{"title":"Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/pdf/2001.06782"},{"title":"[2001.06782] Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/abs/2001.06782"},{"title":"GitHub - OrthoDex/PCGrad-PyTorch: PyTorch implementation for \"Gradient Surgery for Multi-Task Learning\" https://arxiv.org/abs/2001.06782 · GitHub","url":"https://github.com/OrthoDex/PCGrad-PyTorch"},{"title":"GitHub - tianheyu927/PCGrad: Code for \"Gradient Surgery for Multi-Task Learning\" · GitHub","url":"https://github.com/tianheyu927/PCGrad"},{"title":"[2001.06782v4] Gradient Surgery for Multi-Task Learning","url":"https://arxiv.org/abs/2001.06782v4"},{"title":"GitHub - WeiChengTseng/Pytorch-PCGrad: Pytorch reimplementation for \"Gradient Surgery for Multi-Task Learning\" · GitHub","url":"https://github.com/WeiChengTseng/Pytorch-PCGrad"},{"title":"GitHub - rangwani-harsh/PC_Grad_Pytorch · GitHub","url":"https://github.com/rangwani-harsh/PC_Grad_Pytorch"},{"title":"GitHub - sailfish009/Pytorch-PCGrad: Pytorch reimplementation for \"Gradient Surgery for Multi-Task Learning\"","url":"https://github.com/sailfish009/Pytorch-PCGrad"},{"title":"PCGrad: Gradient Surgery for Multi-Task Learning | PDF | Mathematical Optimization | Computer Vision","url":"https://www.scribd.com/document/558287008/Yu-Et-Al-2020-Gradient-Surgery-for-Multi-Task-Learning"},{"title":"Supported Algorithms — mtrl 1.0.0 documentation","url":"https://mtrl.readthedocs.io/en/latest/pages/algorithms/supported.html"}]

Based on the search results, I can confirm that arXiv paper 2001.06782 is titled "Gradient Surgery for Multi-Task Learning" and was authored by Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn.

The paper introduces PCGrad (Projecting Conflicting Gradients), a method for multi-task learning. PCGrad projects each task's gradient onto th
…[truncated 178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 286 · 2026-05-26T10:24:49.885402+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Zheng Lianmin\" \"Judging LLM-as-a-Judge\" NeurIPS 2023 Datasets Benchmarks track proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Zheng Lianmin\" \"Judging LLM-as-a-Judge\" NeurIPS 2023 Datasets Benchmarks track proceedings"
  }
}
```

</details>

---

### Tool call

_source line 287 · 2026-05-26T10:24:49.885558+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Shazeer \"GLU Variants Improve Transformer\" published conference journal venue 2020 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Shazeer \"GLU Variants Improve Transformer\" published conference journal venue 2020 2021"
  }
}
```

</details>

---

### Tool result

_source line 288 · 2026-05-26T10:24:49.885682+00:00_

Web search results for query: "arxiv 2407.21783v1 "Dubey" first author vs v3 "Grattafiori" first author Llama 3"

Links: [{"title":"[2407.21783] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783"},{"title":"[2407.21783] The Llama 3 Herd of Models - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2407.21783"},{"title":"The Llama 3 Herd of Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240721783G/abstract"},{"title":"Paper page - The Llama 3 Herd of Models","url":"https://huggingface.co/papers/2407.21783"},{"title":"(PDF) The Llama 3 Herd of Models","url":"https://www.researchgate.net/publication/382739128_The_Llama_3_Herd_of_Models"},{"title":"The Llama 3 Herd of Models. Paper Review | by Eleventh Hour Enthusiast | Medium","url":"https://medium.com/@EleventhHourEnthusiast/the-llama-3-herd-of-models-2f62252ce1c8"},{"title":"[2407.21783v2] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v2"},{"title":"[2407.21783v1] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v1"},{"title":"[2407.21783v3] The Llama 3 Herd of Models","url":"https://arxiv.org/abs/2407.21783v3"}]

Based on the search results, I can now address your query about the differences between the two versions:

In version 1 (v1), Abhimanyu Dubey is listed as the first author, while in version 3 (v3), Aaron Grattafiori is listed as the first author. 

Version 2 (v2) also had Abhimanyu Dubey as the first author, so the authorship order was changed between v2 and v3, with the last revision to v3 occurring on November 23, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 289 · 2026-05-26T10:24:49.885905+00:00_

Now I have enough information to compile the complete verification report. Here are the findings:

---

### [bengio2015scheduled] Bengio, Samy and Vinyals, Oriol and Jaitly, Navdeep and Shazeer, Noam (2015) -- "Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks"
- **Exists:** ✓
- **Authors:** ✓ (Samy Bengio, Oriol Vinyals, Navdeep Jaitly, Noam Shazeer)
- **Year:** ✓ (2015)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (NeurIPS 2015, originally published as NIPS 2015)
- **arXiv ID:** ✓ (1506.03099)
- **arXiv->published upgrade needed:** No (already cites the NeurIPS venue)
- **Notes:** Clean entry.

---

### [ranzato2016sequence] Ranzato, Marc'Aurelio and Chopra, Sumit and Auli, Michael and Zaremba, Wojciech (2016) -- "Sequence Level Training with Recurrent Neural Networks"
- **Exists:** ✓
- **Authors:** ✓ (Marc'Aurelio Ranzato, Sumit Chopra, Michael Auli, Wojciech Zaremba)
- **Year:** ✓ (2016)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (ICLR 2016)
- **arXiv ID:** ✓ (1511.06732)
- **arXiv->published upgrade needed:** No
- **Notes:** Clean entry.

---

### [lamb2016professor] Lamb, Alex and Goyal, Anirudh and Zhang, Ying and Zhang, Saizheng and Courville, Aaron and Bengio, Yoshua (2016) -- "Professor Forcing: A New Algorithm for Training Recurrent Networks"
- **Exists:** ✓
- **Authors:** ✓ (Alex Lamb is first author on arXiv; NeurIPS proceedings list "Alex M Lamb" first, then "Anirudh Goyal ALIAS PARTH GOYAL". Some citation databases like Semantic Scholar and Google Scholar list Goyal first, but the official arXiv and NeurIPS proceedings both list Lamb first, matching the bib entry.)
- **Year:** ✓ (2016)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (NeurIPS 2016)
- **arXiv ID:** ✓ (1610.09038)
- **arXiv->published upgrade needed:** No
- **Notes:** Clean entry. The author ordering as "Lamb, ... Goyal, ..." is correct per the official paper PDF and NeurIPS proceedings.

---

### [leblond2018searnn] Leblond, Remi and Alayrac, Jean-Baptiste and Osokin
…[truncated 6191 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "elapsed_ms": 33
}
```

</details>

---

### Tool result

_source line 290 · 2026-05-26T10:24:49.886074+00:00_

Web search results for query: ""Zheng Lianmin" "Judging LLM-as-a-Judge" NeurIPS 2023 Datasets Benchmarks track proceedings"

Links: [{"title":"NeurIPS Poster Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://neurips.cc/virtual/2023/poster/73434"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena - United Arab Emirates - Ministry of Health and Prevention","url":"https://nchr.elsevierpure.com/en/publications/judging-llm-as-a-judge-with-mt-bench-and-chatbot-arena/"},{"title":"[2306.05685] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/abs/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena Lianmin Zheng1∗","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf"},{"title":"llm-as-judge-zheng-2023 | Skills Mar...","url":"https://lobehub.com/skills/curiositech-windags-skills-llm-as-judge-zheng-2023"},{"title":"[Paper Note] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena, Lianmin Zheng+, NeurIPS'23, 2023.06 · Issue #903 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/903"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html"},{"title":"[Quick Review] Judging LLM-as-a-judge with MT-Bench and Chatbot Arena","url":"https://liner.com/review/judging-llmasajudge-with-mtbench-and-chatbot-arena"},{"title":"LLM-as-a-Judge: How to Build Reliable, Scalable Evaluation for LLM Apps and Agents","url":"https://www.comet.com/site/blog/llm-as-a-judge/"}]

Based on the search results, I found the information you're looking for:

The paper "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" by Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P.
…[truncated 886 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 291 · 2026-05-26T10:24:49.886232+00:00_

Web search results for query: "Shazeer "GLU Variants Improve Transformer" published conference journal venue 2020 2021"

Links: [{"title":"[PDF] GLU Variants Improve Transformer | Semantic Scholar","url":"https://www.semanticscholar.org/paper/GLU-Variants-Improve-Transformer-Shazeer/bdbf780dfd6b3eb0c9e980887feae5f23af15bc4"},{"title":"GLU Variants Improve Transformer | Request PDF","url":"https://www.researchgate.net/publication/339252250_GLU_Variants_Improve_Transformer"},{"title":"SwiGLU: GLU Variants Improve Transformer (2020) – Naoki Shibuya","url":"https://naokishibuya.github.io/blog/2023-04-30-swiglu-2020/index.html"},{"title":"dblp: GLU Variants Improve Transformer.","url":"https://dblp.org/rec/journals/corr/abs-2002-05202.html"},{"title":"GLU Variants Improve Transformer - Consensus","url":"https://www.consensus.app/papers/glu-variants-improve-transformer-shazeer/a61336c71bd8535aa0f6696f4a7a7bda/"},{"title":"GitHub - ngdonna2020/glu: GLU variants improve transformer · GitHub","url":"https://github.com/ngdonna2020/glu"},{"title":"GLU Variants Improve Transformer | alphaXiv","url":"https://www.alphaxiv.org/overview/2002.05202v1"},{"title":"Improving Vision Transformers with Novel GLU-Type Nonlinearities","url":"https://www.techrxiv.org/users/749272/articles/720560/master/file/data/main/main.pdf?inline=true"},{"title":"SwiGLU: GLU Variants Improve Transformer (2020) – KiKaBeN","url":"https://kikaben.com/swiglu-2020/"}]

Based on the search results, here's what I found about the paper:

The paper "GLU Variants Improve Transformer" by Noam Shazeer was published in 2020 in ArXiv (abs/2002.05202). It was published on February 12, 2020.

The publication venue was CoRR (Computation and Language Research), which is the arXiv preprint repository. The paper was not published in a traditional peer-reviewed conference journal during the 2020-2021 timeframe based on these search results—it appears to have remained as an arXiv preprint.


REMINDER: You MUST include the sour
…[truncated 65 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 292 · 2026-05-26T10:24:49.886386+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Dong Cordonnier Loukas \"Attention is Not All You Need\" ICML 2021 pages proceedings.mlr.press"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Dong Cordonnier Loukas \"Attention is Not All You Need\" ICML 2021 pages proceedings.mlr.press"
  }
}
```

</details>

---

### Tool result

_source line 293 · 2026-05-26T10:24:49.886544+00:00_

Web search results for query: "Dong Cordonnier Loukas "Attention is Not All You Need" ICML 2021 pages proceedings.mlr.press"

Links: [{"title":"Attention is not all you need: pure attention loses rank doubly exponentially with depth - Ben-Gurion University Research Portal","url":"https://cris.bgu.ac.il/en/publications/attention-is-not-all-you-need-pure-attention-loses-rank-doubly-ex-2/"},{"title":"GitHub - twistedcubic/attention-rank-collapse: [ICML 2021 Oral] We show pure attention suffers rank collapse, and how different mechanisms combat it. · GitHub","url":"https://github.com/twistedcubic/attention-rank-collapse"},{"title":"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth [Quick Review]","url":"https://liner.com/review/attention-is-not-all-you-need-pure-attention-loses-rank"},{"title":"ICML 2021 Attention is not all you need: pure attention loses rank doubly exponentially with depth Oral","url":"https://icml.cc/virtual/2021/oral/9822"},{"title":"[PDF] Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Attention-is-Not-All-You-Need:-Pure-Attention-Loses-Dong-Cordonnier/dfb37e6216e792bf6bd5a30c0fc7ad55df1cb71e"},{"title":"Attention is not all you need: pure attention loses rank doubly exponentially with depth","url":"https://proceedings.mlr.press/v139/dong21a.html"},{"title":"Jean-Baptiste Cordonnier","url":"https://jbcordonnier.com/"},{"title":"Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303404D/abstract"},{"title":"Yihe Dong, Jean-Baptiste Cordonnier, Andreas Loukas · Attention is not all you need: pure attention loses rank doubly exponentially with depth","url":"https://slideslive.com/38958633/attention-is-not-all-you-need-pure-attention-loses-rank-doubly-exponentially-with-depth"}]

Based on the search results, here 
…[truncated 517 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 294 · 2026-05-26T10:24:49.886703+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:arxiv.org 2110.14048 \"Conflict-Averse Gradient Descent\" authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:arxiv.org 2110.14048 \"Conflict-Averse Gradient Descent\" authors"
  }
}
```

</details>

---

### Tool result

_source line 295 · 2026-05-26T10:24:49.886920+00:00_

Now I have all the information needed. Here is the complete verification report:

---

### [dongre2026attention] Dongre et al. (2026) -- When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction
- Exists: **Yes**
- Authors: **Correct** -- Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tur
- Year: **Correct** -- May 2026
- Title: **Correct** -- exact match
- Venue: **Correct** -- arXiv preprint (2605.12922)
- arXiv ID: **Correct**
- arXiv to published upgrade needed: **No** -- very recent preprint (May 2026), no published venue found
- Notes: None

### [hong2025rhea] Hong et al. (2025) -- Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs
- Exists: **Yes**
- Authors: **Correct** -- Wanyang Hong, Zhaoning Zhang, Yi Chen, Libo Zhang, Baihui Liu, Linbo Qiao, Zhiliang Tian, Dongsheng Li
- Year: **Correct** -- December 2025
- Title: **Correct** -- exact match
- Venue: **Correct** -- arXiv preprint (2512.06869)
- arXiv ID: **Correct**
- arXiv to published upgrade needed: **No** -- no published venue found
- Notes: None

### [laban2025lost] Laban et al. (2025) -- LLMs Get Lost In Multi-Turn Conversation
- Exists: **Yes**
- Authors: **Correct** -- Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville
- Year: Technically correct for arXiv (May 2025), but **should be updated to 2026 for the published version**
- Title: **Correct** -- exact match
- Venue: **WRONG** -- Currently cited as arXiv preprint, but the paper was **published at ICLR 2026 as an Oral presentation** (and won Best Paper). Must upgrade.
- arXiv ID: **Correct**
- arXiv to published upgrade needed: **YES** -- Should be changed from `@article` with `arXiv preprint` to `@inproceedings` at ICLR 2026. The bib key should also change from `laban2025lost` to something like `laban2026lost`.
- Notes: This is a high-profile paper (ICLR 2026 Best Paper, Oral). Citing it as an arXiv preprint is a significant error that reviewers would notice.
…[truncated 6436 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "elapsed_ms": 38
}
```

</details>

---

### Tool result

_source line 296 · 2026-05-26T10:24:49.887078+00:00_

Web search results for query: "site:arxiv.org 2110.14048 "Conflict-Averse Gradient Descent" authors"

Links: [{"title":"[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/abs/2110.14048"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/html/2110.14048v2"},{"title":"[2110.14048v1] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv.org/abs/2110.14048v1"},{"title":"[2110.14048] Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://arxiv-export-lb.library.cornell.edu/abs/2110.14048?context=cs.AI"},{"title":"Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://oamonitor.ireland.openaire.eu/rpo/rcsi/search/publication?pid=10.48550/arxiv.2110.14048"},{"title":"(PDF) Conflict-Averse Gradient Descent for Multi-task Learning","url":"https://www.researchgate.net/publication/355698823_Conflict-Averse_Gradient_Descent_for_Multi-task_Learning"},{"title":"CAGrad: Conflict-Averse Gradient Descent for MTL","url":"https://www.emergentmind.com/papers/2110.14048"},{"title":"[PDF] Conflict-Averse Gradient Descent for Multi-task Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conflict-Averse-Gradient-Descent-for-Multi-task-Liu-Liu/b7e531104c95eb67ce6c20d6dc1318e8bf837bf8"}]

Based on the search results, the authors of the paper "Conflict-Averse Gradient Descent for Multi-task Learning" (arXiv:2110.14048) are Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, and Qiang Liu. The affiliations include The University of Texas at Austin, Sony AI, and Bytedance Research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 297 · 2026-05-26T10:24:49.887314+00:00_

Now I have all the information needed to compile the full verification report. Here are my findings:

---

### [zhang2020dialogpt] Zhang (2020) — DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation
- **Exists:** ✓
- **Authors:** ✓ (Zhang, Sun, Galley, Chen, Brockett, Gao, Gao, Liu, Dolan all confirmed)
- **Year:** ✓ (2020)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (ACL 2020 System Demonstrations — confirmed at ACL Anthology: `aclanthology.org/2020.acl-demos.30/`)
- **arXiv ID:** ✓ (1911.00536)
- **arXiv->published upgrade needed:** No (already cites the published ACL version)
- **Notes:** Clean entry.

---

### [roller2021recipes] Roller (2021) — Recipes for Building an Open-Domain Chatbot
- **Exists:** ✓
- **Authors:** ✓ (Roller, Dinan, Goyal, Ju, Williamson, Liu, Xu, Ott, Smith, Boureau, Weston all confirmed)
- **Year:** ✓ (2021)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (EACL 2021 — confirmed at ACL Anthology: `aclanthology.org/2021.eacl-main.24/`)
- **arXiv ID:** ✓ (2004.13637)
- **arXiv->published upgrade needed:** No (already cites the published EACL version)
- **Notes:** Clean entry.

---

### [zheng2024judging] Zheng (2023) — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena
- **Exists:** ✓
- **Authors:** ✓ (Zheng, Chiang, Sheng, Zhuang, Wu, Zhuang, Lin, Li, Li, Xing, Zhang, Gonzalez, Stoica all confirmed)
- **Year:** ✓ (2023, published at NeurIPS 2023)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (NeurIPS 2023, Datasets and Benchmarks Track)
- **arXiv ID:** ✓ (2306.05685)
- **arXiv->published upgrade needed:** No (already cites NeurIPS 2023)
- **Notes:** The bib key `zheng2024judging` uses year 2024 but the paper was published at NeurIPS 2023. The bib key is cosmetically inconsistent but not a citation error if the year field in the .bib is correctly 2023. Worth renaming the key to `zheng2023judging` for consistency.

---

### [clark2019what] Clark (2019) — What Does BERT Look At? An Analysis of BERT's Attention
- **
…[truncated 8167 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "elapsed_ms": 21
}
```

</details>

---

### Tool result

_source line 298 · 2026-05-26T10:24:49.887583+00:00_

All searches are complete. Let me compile the full verification report.

---

## Citation Verification Report

### [yu2020pcgrad] Yu et al. (2020) — Gradient Surgery for Multi-Task Learning
- **Exists:** ✓
- **Authors:** ✓ (Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, Chelsea Finn -- note: arXiv/NeurIPS listing uses "Tianhe Yu" but some sources say "Tianhe Kevin Yu"; bib entry is acceptable)
- **Year:** ✓ (2020)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (NeurIPS 2020)
- **arXiv ID:** ✓ (2001.06782)
- **arXiv->published upgrade needed:** No (already cites NeurIPS 2020)
- **Notes:** Clean.

---

### [chen2018gradnorm] Chen et al. (2018) — GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks
- **Exists:** ✓
- **Authors:** ✓ (Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, Andrew Rabinovich)
- **Year:** ✓ (2018)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (ICML 2018)
- **arXiv ID:** ✓ (1711.02257)
- **arXiv->published upgrade needed:** No (already cites ICML 2018)
- **Notes:** Clean.

---

### [liu2021cagrad] Liu et al. (2021) — Conflict-Averse Gradient Descent for Multi-task Learning
- **Exists:** ✓
- **Authors:** ✓ (Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, Qiang Liu)
- **Year:** ✓ (2021)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (NeurIPS 2021)
- **arXiv ID:** ✓ (2110.14048)
- **arXiv->published upgrade needed:** No (already cites NeurIPS 2021)
- **Notes:** Clean.

---

### [navon2022nash] Navon et al. (2022) — Multi-Task Learning as a Bargaining Game
- **Exists:** ✓
- **Authors:** ✓ (Aviv Navon, Aviv Shamsian, Idan Achituve, Haggai Maron, Kenji Kawaguchi, Gal Chechik, Ethan Fetaya)
- **Year:** ✓ (2022)
- **Title:** ✓ (exact match)
- **Venue:** ✓ (ICML 2022)
- **arXiv ID:** ✓ (2202.01017)
- **arXiv->published upgrade needed:** No (already cites ICML 2022)
- **Notes:** Clean.

---

### [dong2021attention] Dong et al. (2021) — Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponential
…[truncated 4409 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Agent",
  "elapsed_ms": 29
}
```

</details>

---

### Tool call

_source line 299 · 2026-05-26T10:24:49.887810+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}|\\\\citealp\\{[^}]+\\}' docs/paper/sections/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u",
  "description": "Extract unique cited bib keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Bash",
  "tool_args": {
    "command": "grep -oP '\\\\cite[tp]?\\{[^}]+\\}|\\\\citealp\\{[^}]+\\}' docs/paper/sections/*.tex | grep -oP '\\{[^}]+\\}' | tr ',' '\\n' | sed 's/[{}]//g' | sed 's/^ *//;s/ *$//' | sort -u",
    "description": "Extract unique cited bib keys"
  }
}
```

</details>

---

### Tool result

_source line 300 · 2026-05-26T10:24:49.887955+00:00_

arora2022exposure
bachlechner2021rezero
bai2024mtbench101
bengio2015scheduled
chen2018gradnorm
clark2019what
dettmers2023qlora
ding2023ultrachat
dong2021attention
dongre2026attention
dou2019attention
dou2022parallel
fan2020layerdrop
grattafiori2024llama3
gromov2024unreasonable
he2019exposure
hendrycks2021measuring
hong2025rhea
hu2022lora
kovaleva2019revealing
laban2025lost
lamb2016professor
leblond2018searnn
li2016persona
li2024measuring
lin2022truthfulqa
liu2021cagrad
liu2024lost
liu2026intent
mihaylova2019scheduled
qiu2025gated
ranzato2016sequence
raposo2024mixture
roller2021recipes
schuster2022calm
srivastava2015highway
veit2016residual
voita2019analyzing
wiseman2016sequence
xiao2024streaming
xu2022goldfish
yu2020pcgrad
zhang2019bridging
zhang2020dialogpt
zhang2024tell
zheng2024judging

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 301 · 2026-05-26T10:24:49.888204+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/citation_audit_worker1.md",
  "content": "# Citation Audit Report — Worker 1\n\n## Summary\n- Total bib entries: 58\n- Cited in paper: 46\n- Uncited (in bib only): 12\n- Verified OK: 41\n- Issues found: 5 (3 critical, 2 minor)\n- Potentially hallucinated: 0\n\n## Critical Issues\n\n| # | Bib Key | Issue |\n|---|---------|-------|\n| 1 | `laban2025lost` | Published at **ICLR 2026 (Oral, Best Paper)**, but cited as arXiv 2025 preprint. Must upgrade venue, year, and entry type. |\n| 2 | `raposo2024mixture` | Venue is **ICLR 2025**, NOT ICML 2024. Year should be 2025. |\n| 3 | `he2019exposure` | Published at **EMNLP 2021** with new title \"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\". Currently cites old arXiv 2019 title/year. |\n\n## Other Issues\n\n| # | Bib Key | Severity | Issue |\n|---|---------|----------|-------|\n| 4 | `brunner2020identifiability` | Medium | Last author \"Andreas Krause\" is **wrong** — should be \"Roger Wattenhofer\" (both ETH Zurich, likely confusion). Entry is uncited so low practical impact. |\n| 5 | `bachlechner2021rezero` | Minor | Author names should be \"Huanru Henry Mao\" (not \"Henry Mao\") and \"Garrison W. Cottrell\" (not \"Gary Cottrell\") per official UAI proceedings. |\n\n## Uncited Bib Entries (12)\n\nThese entries exist in `references.bib` but are not `\\cite`d anywhere in the paper:\n\n| Bib Key | Paper |\n|---------|-------|\n| `hsieh2024found` | Found in the Middle (Findings ACL 2024) |\n| `luo2025flexidepth` | Adaptive Layer-skipping (COLM 2025) |\n| `navon2022nash` | Multi-Task Learning as Bargaining Game (ICML 2022) |\n| `vaswani2017attention` | Attention Is All You Need (NeurIPS 2017) |\n| `he2016deep` | Deep Residual Learning (CVPR 2016) |\n| `vig2019multiscale` | Multiscale Visualization of Attention (ACL 2019 Demo) |\n| `abnar2020quantifying` | Quantifying Attention Flow (ACL 2020) |\n| `ethayarajh2019contextual` | How Contextual are Contextualized Word Representations (EMNLP 2019) |\n| `brunner2020identifiability` | On Identifiability in Transformers (ICLR 2020) |\n| `zhou2020drophead` | Scheduled DropHead (Findings EMNLP 2020) |\n| `dauphin2017language` | Language Modeling with Gated CNNs (ICML 2017) |\n| `shazeer2020glu` | GLU Variants Improve Transformer (arXiv 2020) |\n\n## Per-Citation Checklist\n\n### [dongre2026attention] Dongre et al. (2026) — When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\n- Exists: ✓\n- Authors: ✓ (Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür)\n- Year: ✓ (2026)\n- Title: ✓\n- Venue: ✓ (arXiv preprint arXiv:2605.12922)\n- arXiv→published upgrade needed: No (very recent, May 2026)\n- Context usage correct: ✓ — Paper claims \"measured significant GAR decline across 12 models\" and \"residual probes retain goal information (AUC=0.98)\". Consistent with the paper's contributions.\n- Notes: Clean.\n\n### [hong2025rhea] Hong et al. (2025) — Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2025)\n- Title: ✓\n- Venue: ✓ (arXiv preprint arXiv:2512.06869)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as an \"inference-time remedy\" alongside li2024measuring. Rhea proposes episodic attention for conversational LLMs, consistent with this characterization.\n- Notes: Clean.\n\n### [laban2025lost] Laban et al. (2025) — LLMs Get Lost In Multi-Turn Conversation\n- Exists: ✓\n- Authors: ✓ (Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville)\n- Year: ✗ — Should be **2026** (ICLR 2026)\n- Title: ✓\n- Venue: ✗ — Cited as arXiv 2025 preprint, but **published at ICLR 2026 as Oral / Best Paper**\n- arXiv→published upgrade needed: **YES** — Must upgrade to `@inproceedings{laban2026lost, booktitle={ICLR}, year={2026}}`\n- Context usage correct: ✓ — Cited for \"quality gaps at later turns\" in multi-turn dialogue.\n- Notes: **CRITICAL.** Citing an ICLR Best Paper as arXiv preprint is a reviewer red flag.\n\n### [liu2026intent] Liu et al. (2026) — Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\n- Exists: ✓\n- Authors: ✓ (Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, Gaofeng Meng)\n- Year: ✓ (2026)\n- Title: ✓ (matches arXiv version)\n- Venue: ✓ (arXiv preprint arXiv:2602.07338)\n- arXiv→published upgrade needed: Possibly — An OpenReview submission for ICLR 2026 exists (id=3x94uVDCeq) possibly under a different title (\"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation\"). Needs investigation.\n- Context usage correct: ✓ — Cited for quality gaps at later turns.\n- Notes: Investigate ICLR 2026 acceptance status and possible title change.\n\n### [bai2024mtbench101] Bai et al. (2024) — MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ACL 2024, confirmed on ACL Anthology 2024.acl-long.401)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as a multi-turn benchmark.\n- Notes: Clean.\n\n### [fan2020layerdrop] Fan et al. (2020) — Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\n- Exists: ✓\n- Authors: ✓ (Angela Fan, Edouard Grave, Armand Joulin)\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (ICLR 2020)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"layer pruning\" alongside gromov2024unreasonable.\n- Notes: Clean.\n\n### [raposo2024mixture] Raposo et al. (2024) — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- Exists: ✓\n- Authors: ✓ (David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro)\n- Year: ✗ — Should be **2025** (published at ICLR 2025, not ICML 2024)\n- Title: ✓\n- Venue: ✗ — Bib says \"International Conference on Machine Learning\" (ICML 2024), but actually published at **ICLR 2025**\n- arXiv→published upgrade needed: N/A (venue/year correction needed)\n- Context usage correct: ✓ — Cited for \"adaptive depth\" alongside schuster2022calm.\n- Notes: **CRITICAL.** Wrong venue (ICML→ICLR) and wrong year (2024→2025).\n\n### [schuster2022calm] Schuster et al. (2022) — Confident Adaptive Language Modeling\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"adaptive depth\".\n- Notes: Clean.\n\n### [qiu2025gated] Qiu et al. (2025) — Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (NeurIPS 2025)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2025, Oral, Best Paper Award)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"per-head sigmoid gates achieving MMLU +2.03 at 15B scale\". Consistent with the paper's findings.\n- Notes: Clean.\n\n### [xiao2024streaming] Xiao et al. (2024) — Efficient Streaming Language Models with Attention Sinks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ICLR 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"retains anchor tokens\" (StreamingLLM). Accurate description.\n- Notes: Clean.\n\n### [zhang2024tell] Zhang et al. (2024) — Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ICLR 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as \"PASTA\" for attention steering. Accurate.\n- Notes: Clean.\n\n### [bengio2015scheduled] Bengio et al. (2015) — Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\n- Exists: ✓\n- Authors: ✓ (Samy Bengio, Oriol Vinyals, Navdeep Jaitly, Noam Shazeer)\n- Year: ✓ (2015)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2015)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"curriculum-based mixing\" and exposure bias. Foundational scheduled sampling paper.\n- Notes: Clean.\n\n### [ranzato2016sequence] Ranzato et al. (2016) — Sequence Level Training with Recurrent Neural Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (ICLR 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"sequence-level objectives\".\n- Notes: Clean.\n\n### [lamb2016professor] Lamb et al. (2016) — Professor Forcing: A New Algorithm for Training Recurrent Networks\n- Exists: ✓\n- Authors: ✓ (Alex Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron Courville, Yoshua Bengio)\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"adversarial regularization\" to address exposure bias. Accurate.\n- Notes: Clean.\n\n### [leblond2018searnn] Leblond et al. (2018) — SEARNN: Training RNNs with Global-Local Losses\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2018)\n- Title: ✓\n- Venue: ✓ (ICLR 2018)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"search-based training\".\n- Notes: Clean.\n\n### [he2019exposure] He et al. (2019) — Quantifying Exposure Bias for Neural Language Generation\n- Exists: ✓ (but outdated citation)\n- Authors: ✓ (Tianxing He, Jingzhao Zhang, Zhiming Zhou, James Glass)\n- Year: ✗ — Should be **2021** (published at EMNLP 2021)\n- Title: ✗ — Published title is **\"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\"**\n- Venue: ✗ — Should be **EMNLP 2021**, not arXiv 2019\n- arXiv→published upgrade needed: **YES** — Must update title, year, venue. ACL Anthology: 2021.emnlp-main.415\n- Context usage correct: ✓ — Cited for \"self-recovery analysis\" which aligns with the published title about self-recovery.\n- Notes: **CRITICAL.** Title, year, and venue all need correction. The paper evolved significantly from 2019 preprint to 2021 publication.\n\n### [wiseman2016sequence] Wiseman & Rush (2016) — Sequence-to-Sequence Learning as Beam-Search Optimization\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (EMNLP 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for training-inference distributional mismatch context.\n- Notes: Clean.\n\n### [arora2022exposure] Arora et al. (2022) — Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (Findings of ACL 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for exposure bias and error accumulation.\n- Notes: Clean.\n\n### [li2024measuring] Li et al. (2024) — Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (COLM 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"independently quantified instruction instability and proposed split-softmax\".\n- Notes: Clean.\n\n### [yu2020pcgrad] Yu et al. (2020) — Gradient Surgery for Multi-Task Learning\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2020)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"projects conflicting gradients onto the other's normal plane\". Accurate description of PCGrad.\n- Notes: Clean.\n\n### [chen2018gradnorm] Chen et al. (2018) — GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2018)\n- Title: ✓\n- Venue: ✓ (ICML 2018)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited alongside discussion of gradient magnitude imbalance.\n- Notes: Clean.\n\n### [liu2021cagrad] Liu et al. (2021) — Conflict-Averse Gradient Descent for Multi-task Learning\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"treat gradient conflict as the root cause\".\n- Notes: Clean.\n\n### [bachlechner2021rezero] Bachlechner et al. (2021) — ReZero is All You Need: Fast Convergence at Large Depth\n- Exists: ✓\n- Authors: ✗ — \"Mao, Henry\" should be **\"Mao, Huanru Henry\"**; \"Cottrell, Gary\" should be **\"Cottrell, Garrison W.\"** per UAI proceedings (PMLR v161)\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (UAI 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"initializes a single trainable scalar at zero to stabilize deep network training\". Exact description of ReZero.\n- Notes: Minor author name corrections needed.\n\n### [grattafiori2024llama3] Grattafiori et al. (2024) — The Llama 3 Herd of Models\n- Exists: ✓\n- Authors: ✓ (Aaron Grattafiori first author in latest arXiv version v3)\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (arXiv preprint, no peer-reviewed venue)\n- arXiv→published upgrade needed: No (industry report, no conference publication)\n- Context usage correct: ✓ — Cited for Llama-3.1-8B-Instruct model.\n- Notes: Clean.\n\n### [gromov2024unreasonable] Gromov et al. (2025) — The Unreasonable Ineffectiveness of the Deeper Layers\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (bib says 2025, correct for ICLR 2025; bib key uses 2024 arXiv year, cosmetic only)\n- Title: ✓\n- Venue: ✓ (ICLR 2025)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"early layers capture local syntax while later layers integrate long-range context\" and \"layer pruning\". Consistent with the paper's findings about deeper layers being removable.\n- Notes: Clean.\n\n### [srivastava2015highway] Srivastava et al. (2015) — Highway Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2015)\n- Title: ✓\n- Venue: ✓ (ICML 2015 Deep Learning Workshop)\n- arXiv→published upgrade needed: No (workshop citation is standard practice; full paper \"Training Very Deep Networks\" exists at NeurIPS 2015 but under different title)\n- Context usage correct: ✓ — Cited for \"highway networks\" in gating context.\n- Notes: Clean.\n\n### [hu2022lora] Hu et al. (2022) — LoRA: Low-Rank Adaptation of Large Language Models\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ICLR 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for LoRA fine-tuning method.\n- Notes: Clean.\n\n### [zhang2020dialogpt] Zhang et al. (2020) — DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (ACL 2020 System Demonstrations)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Clean.\n\n### [roller2021recipes] Roller et al. (2021) — Recipes for Building an Open-Domain Chatbot\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (EACL 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Clean.\n\n### [zheng2024judging] Zheng et al. (2023) — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (year field says 2023, correct for NeurIPS 2023)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2023, Datasets and Benchmarks Track)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"MT-Bench\" benchmark.\n- Notes: Bib key `zheng2024judging` uses 2024 but year field is 2023. Cosmetic key inconsistency only; no impact on rendered output.\n\n### [clark2019what] Clark et al. (2019) — What Does BERT Look At? An Analysis of BERT's Attention\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019 BlackboxNLP Workshop)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"head specialization\" analysis.\n- Notes: Clean.\n\n### [voita2019analyzing] Voita et al. (2019) — Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"head specialization\" analysis.\n- Notes: Clean.\n\n### [kovaleva2019revealing] Kovaleva et al. (2019) — Revealing the Dark Secrets of BERT\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (EMNLP 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for attention analysis/head specialization.\n- Notes: Clean.\n\n### [liu2024lost] Liu et al. (2024) — Lost in the Middle: How Language Models Use Long Contexts\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (TACL 2024, volume 12, pp 157-173)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"positional bias calibration\".\n- Notes: Clean.\n\n### [zhang2019bridging] Zhang et al. (2019) — Bridging the Gap between Training and Inference for Neural Machine Translation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"bridging strategies for NMT\" in exposure bias context.\n- Notes: Clean.\n\n### [mihaylova2019scheduled] Mihaylova & Martins (2019) — Scheduled Sampling for Transformers\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019 Student Research Workshop, pp 351-356)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"extended scheduled sampling to transformers for single-turn NMT\". Accurate.\n- Notes: Clean.\n\n### [dou2019attention] Dou et al. (2019) — Attention Forcing for Sequence-to-sequence Model Training\n- Exists: ✓\n- Authors: ✓ (Qingyun Dou, Yiting Lu, Joshua Efiong, Mark J. F. Gales)\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (arXiv preprint; ICLR 2020 submission was not accepted)\n- arXiv→published upgrade needed: No (remains unpublished)\n- Context usage correct: ✓ — Cited for \"proposed attention forcing (supervising cross-attention during NMT)\". Accurate description.\n- Notes: Clean.\n\n### [dou2022parallel] Dou & Gales (2022) — Parallel Attention Forcing for Machine Translation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (arXiv preprint; no peer-reviewed venue found)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"extended [attention forcing] with KL-divergence switching\". Consistent with the paper.\n- Notes: Clean.\n\n### [li2016persona] Li et al. (2016) — A Persona-Based Neural Conversation Model\n- Exists: ✓\n- Authors: ✓ (minor: \"Georgios Spithourakis\" missing middle initial \"P.\" per ACL Anthology)\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (ACL 2016, pp 994-1003)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Very minor — \"Georgios Spithourakis\" could be \"Georgios P. Spithourakis\".\n\n### [xu2022goldfish] Xu et al. (2022) — Beyond Goldfish Memory: Long-Term Open-Domain Conversation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ACL 2022, pp 5180-5197)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"modern long-context models\" in dialogue.\n- Notes: Clean.\n\n### [veit2016residual] Veit et al. (2016) — Residual Networks Behave Like Ensembles of Relatively Shallow Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"residual networks can be viewed as ensembles of shallow paths\". Exact main thesis.\n- Notes: Clean.\n\n### [dong2021attention] Dong et al. (2021) — Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (ICML 2021, pp 2793-2803)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"attention collapse in deep transformers\". Accurate.\n- Notes: Clean.\n\n### [lin2022truthfulqa] Lin et al. (2022) — TruthfulQA: Measuring How Models Mimic Human Falsehoods\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ACL 2022, pp 3214-3252)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as an evaluation benchmark in Limitations section.\n- Notes: Clean.\n\n### [hendrycks2021measuring] Hendrycks et al. (2021) — Measuring Massive Multitask Language Understanding\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (ICLR 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"MMLU 5-shot\" benchmark. Accurate.\n- Notes: Clean.\n\n### [dettmers2023qlora] Dettmers et al. (2023) — QLoRA: Efficient Finetuning of Quantized LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2023)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2023)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited alongside LoRA for fine-tuning setup.\n- Notes: Clean.\n\n### [ding2023ultrachat] Ding et al. (2023) — Enhancing Chat Language Models by Scaling High-quality Instructional Conversations\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2023)\n- Title: ✓\n- Venue: ✓ (EMNLP 2023)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for UltraChat dataset used in all experiments.\n- Notes: Clean.\n\n---\n\n## Uncited Entries Detail (for completeness)\n\n### [hsieh2024found] — Verified ✓, Findings ACL 2024, all fields correct. Not cited.\n### [luo2025flexidepth] — Verified ✓, COLM 2025, all fields correct. Not cited.\n### [navon2022nash] — Verified ✓, ICML 2022, all fields correct. Not cited.\n### [vaswani2017attention] — Verified ✓, NeurIPS 2017, all fields correct. Not cited.\n### [he2016deep] — Verified ✓, CVPR 2016, all fields correct. Not cited.\n### [vig2019multiscale] — Verified ✓, ACL 2019 Demo, all fields correct. Not cited.\n### [abnar2020quantifying] — Verified ✓, ACL 2020, all fields correct. Not cited.\n### [ethayarajh2019contextual] — Verified ✓, EMNLP 2019, all fields correct. Not cited.\n### [brunner2020identifiability] — **Author error**: \"Andreas Krause\" should be \"Roger Wattenhofer\". Not cited.\n### [zhou2020drophead] — Verified ✓, Findings EMNLP 2020, all fields correct. Not cited.\n### [dauphin2017language] — Verified ✓, ICML 2017, all fields correct. Not cited.\n### [shazeer2020glu] — Verified ✓, arXiv preprint (never published), all fields correct. Not cited.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/citation_audit_worker1.md",
    "content": "# Citation Audit Report — Worker 1\n\n## Summary\n- Total bib entries: 58\n- Cited in paper: 46\n- Uncited (in bib only): 12\n- Verified OK: 41\n- Issues found: 5 (3 critical, 2 minor)\n- Potentially hallucinated: 0\n\n## Critical Issues\n\n| # | Bib Key | Issue |\n|---|---------|-------|\n| 1 | `laban2025lost` | Published at **ICLR 2026 (Oral, Best Paper)**, but cited as arXiv 2025 preprint. Must upgrade venue, year, and entry type. |\n| 2 | `raposo2024mixture` | Venue is **ICLR 2025**, NOT ICML 2024. Year should be 2025. |\n| 3 | `he2019exposure` | Published at **EMNLP 2021** with new title \"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\". Currently cites old arXiv 2019 title/year. |\n\n## Other Issues\n\n| # | Bib Key | Severity | Issue |\n|---|---------|----------|-------|\n| 4 | `brunner2020identifiability` | Medium | Last author \"Andreas Krause\" is **wrong** — should be \"Roger Wattenhofer\" (both ETH Zurich, likely confusion). Entry is uncited so low practical impact. |\n| 5 | `bachlechner2021rezero` | Minor | Author names should be \"Huanru Henry Mao\" (not \"Henry Mao\") and \"Garrison W. Cottrell\" (not \"Gary Cottrell\") per official UAI proceedings. |\n\n## Uncited Bib Entries (12)\n\nThese entries exist in `references.bib` but are not `\\cite`d anywhere in the paper:\n\n| Bib Key | Paper |\n|---------|-------|\n| `hsieh2024found` | Found in the Middle (Findings ACL 2024) |\n| `luo2025flexidepth` | Adaptive Layer-skipping (COLM 2025) |\n| `navon2022nash` | Multi-Task Learning as Bargaining Game (ICML 2022) |\n| `vaswani2017attention` | Attention Is All You Need (NeurIPS 2017) |\n| `he2016deep` | Deep Residual Learning (CVPR 2016) |\n| `vig2019multiscale` | Multiscale Visualization of Attention (ACL 2019 Demo) |\n| `abnar2020quantifying` | Quantifying Attention Flow (ACL 2020) |\n| `ethayarajh2019contextual` | How Contextual are Contextualized Word Representations (EMNLP 2019) |\n| `brunner2020identifiability` | On Identifiability in Transformers (ICLR 2020) |\n| `zhou2020drophead` | Scheduled DropHead (Findings EMNLP 2020) |\n| `dauphin2017language` | Language Modeling with Gated CNNs (ICML 2017) |\n| `shazeer2020glu` | GLU Variants Improve Transformer (arXiv 2020) |\n\n## Per-Citation Checklist\n\n### [dongre2026attention] Dongre et al. (2026) — When Attention Closes: How LLMs Lose the Thread in Multi-Turn Interaction\n- Exists: ✓\n- Authors: ✓ (Vardhan Dongre, Joseph Hsieh, Viet Dac Lai, Seunghyun Yoon, Trung Bui, Dilek Hakkani-Tür)\n- Year: ✓ (2026)\n- Title: ✓\n- Venue: ✓ (arXiv preprint arXiv:2605.12922)\n- arXiv→published upgrade needed: No (very recent, May 2026)\n- Context usage correct: ✓ — Paper claims \"measured significant GAR decline across 12 models\" and \"residual probes retain goal information (AUC=0.98)\". Consistent with the paper's contributions.\n- Notes: Clean.\n\n### [hong2025rhea] Hong et al. (2025) — Rhea: Role-aware Heuristic Episodic Attention for Conversational LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2025)\n- Title: ✓\n- Venue: ✓ (arXiv preprint arXiv:2512.06869)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as an \"inference-time remedy\" alongside li2024measuring. Rhea proposes episodic attention for conversational LLMs, consistent with this characterization.\n- Notes: Clean.\n\n### [laban2025lost] Laban et al. (2025) — LLMs Get Lost In Multi-Turn Conversation\n- Exists: ✓\n- Authors: ✓ (Philippe Laban, Hiroaki Hayashi, Yingbo Zhou, Jennifer Neville)\n- Year: ✗ — Should be **2026** (ICLR 2026)\n- Title: ✓\n- Venue: ✗ — Cited as arXiv 2025 preprint, but **published at ICLR 2026 as Oral / Best Paper**\n- arXiv→published upgrade needed: **YES** — Must upgrade to `@inproceedings{laban2026lost, booktitle={ICLR}, year={2026}}`\n- Context usage correct: ✓ — Cited for \"quality gaps at later turns\" in multi-turn dialogue.\n- Notes: **CRITICAL.** Citing an ICLR Best Paper as arXiv preprint is a reviewer red flag.\n\n### [liu2026intent] Liu et al. (2026) — Intent Mismatch Causes LLMs to Get Lost in Multi-Turn Conversation\n- Exists: ✓\n- Authors: ✓ (Geng Liu, Fei Zhu, Rong Feng, Changyi Ma, Shiqi Wang, Gaofeng Meng)\n- Year: ✓ (2026)\n- Title: ✓ (matches arXiv version)\n- Venue: ✓ (arXiv preprint arXiv:2602.07338)\n- arXiv→published upgrade needed: Possibly — An OpenReview submission for ICLR 2026 exists (id=3x94uVDCeq) possibly under a different title (\"Explicating the Implicit: Bridging the Intent Alignment Gap in Multi-Turn Conversation\"). Needs investigation.\n- Context usage correct: ✓ — Cited for quality gaps at later turns.\n- Notes: Investigate ICLR 2026 acceptance status and possible title change.\n\n### [bai2024mtbench101] Bai et al. (2024) — MT-Bench-101: A Fine-Grained Benchmark for Evaluating Large Language Models in Multi-Turn Dialogues\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ACL 2024, confirmed on ACL Anthology 2024.acl-long.401)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as a multi-turn benchmark.\n- Notes: Clean.\n\n### [fan2020layerdrop] Fan et al. (2020) — Reducing Transformer Depth on Demand with Structured Dropout (LayerDrop)\n- Exists: ✓\n- Authors: ✓ (Angela Fan, Edouard Grave, Armand Joulin)\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (ICLR 2020)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"layer pruning\" alongside gromov2024unreasonable.\n- Notes: Clean.\n\n### [raposo2024mixture] Raposo et al. (2024) — Mixture-of-Depths: Dynamically Allocating Compute in Transformer-Based Language Models\n- Exists: ✓\n- Authors: ✓ (David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter Conway Humphreys, Adam Santoro)\n- Year: ✗ — Should be **2025** (published at ICLR 2025, not ICML 2024)\n- Title: ✓\n- Venue: ✗ — Bib says \"International Conference on Machine Learning\" (ICML 2024), but actually published at **ICLR 2025**\n- arXiv→published upgrade needed: N/A (venue/year correction needed)\n- Context usage correct: ✓ — Cited for \"adaptive depth\" alongside schuster2022calm.\n- Notes: **CRITICAL.** Wrong venue (ICML→ICLR) and wrong year (2024→2025).\n\n### [schuster2022calm] Schuster et al. (2022) — Confident Adaptive Language Modeling\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"adaptive depth\".\n- Notes: Clean.\n\n### [qiu2025gated] Qiu et al. (2025) — Gated Attention for Large Language Models: Non-linearity, Sparsity, and Attention-Sink-Free\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (NeurIPS 2025)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2025, Oral, Best Paper Award)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"per-head sigmoid gates achieving MMLU +2.03 at 15B scale\". Consistent with the paper's findings.\n- Notes: Clean.\n\n### [xiao2024streaming] Xiao et al. (2024) — Efficient Streaming Language Models with Attention Sinks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ICLR 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"retains anchor tokens\" (StreamingLLM). Accurate description.\n- Notes: Clean.\n\n### [zhang2024tell] Zhang et al. (2024) — Tell Your Model Where to Attend: Post-hoc Attention Steering for LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (ICLR 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as \"PASTA\" for attention steering. Accurate.\n- Notes: Clean.\n\n### [bengio2015scheduled] Bengio et al. (2015) — Scheduled Sampling for Sequence Prediction with Recurrent Neural Networks\n- Exists: ✓\n- Authors: ✓ (Samy Bengio, Oriol Vinyals, Navdeep Jaitly, Noam Shazeer)\n- Year: ✓ (2015)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2015)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"curriculum-based mixing\" and exposure bias. Foundational scheduled sampling paper.\n- Notes: Clean.\n\n### [ranzato2016sequence] Ranzato et al. (2016) — Sequence Level Training with Recurrent Neural Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (ICLR 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"sequence-level objectives\".\n- Notes: Clean.\n\n### [lamb2016professor] Lamb et al. (2016) — Professor Forcing: A New Algorithm for Training Recurrent Networks\n- Exists: ✓\n- Authors: ✓ (Alex Lamb, Anirudh Goyal, Ying Zhang, Saizheng Zhang, Aaron Courville, Yoshua Bengio)\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"adversarial regularization\" to address exposure bias. Accurate.\n- Notes: Clean.\n\n### [leblond2018searnn] Leblond et al. (2018) — SEARNN: Training RNNs with Global-Local Losses\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2018)\n- Title: ✓\n- Venue: ✓ (ICLR 2018)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"search-based training\".\n- Notes: Clean.\n\n### [he2019exposure] He et al. (2019) — Quantifying Exposure Bias for Neural Language Generation\n- Exists: ✓ (but outdated citation)\n- Authors: ✓ (Tianxing He, Jingzhao Zhang, Zhiming Zhou, James Glass)\n- Year: ✗ — Should be **2021** (published at EMNLP 2021)\n- Title: ✗ — Published title is **\"Exposure Bias versus Self-Recovery: Are Distortions Really Incremental for Autoregressive Text Generation?\"**\n- Venue: ✗ — Should be **EMNLP 2021**, not arXiv 2019\n- arXiv→published upgrade needed: **YES** — Must update title, year, venue. ACL Anthology: 2021.emnlp-main.415\n- Context usage correct: ✓ — Cited for \"self-recovery analysis\" which aligns with the published title about self-recovery.\n- Notes: **CRITICAL.** Title, year, and venue all need correction. The paper evolved significantly from 2019 preprint to 2021 publication.\n\n### [wiseman2016sequence] Wiseman & Rush (2016) — Sequence-to-Sequence Learning as Beam-Search Optimization\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (EMNLP 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for training-inference distributional mismatch context.\n- Notes: Clean.\n\n### [arora2022exposure] Arora et al. (2022) — Why Exposure Bias Matters: An Imitation Learning Perspective of Error Accumulation in Language Generation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (Findings of ACL 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for exposure bias and error accumulation.\n- Notes: Clean.\n\n### [li2024measuring] Li et al. (2024) — Measuring and Controlling Instruction (In)Stability in Language Model Dialogs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (COLM 2024)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"independently quantified instruction instability and proposed split-softmax\".\n- Notes: Clean.\n\n### [yu2020pcgrad] Yu et al. (2020) — Gradient Surgery for Multi-Task Learning\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2020)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"projects conflicting gradients onto the other's normal plane\". Accurate description of PCGrad.\n- Notes: Clean.\n\n### [chen2018gradnorm] Chen et al. (2018) — GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2018)\n- Title: ✓\n- Venue: ✓ (ICML 2018)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited alongside discussion of gradient magnitude imbalance.\n- Notes: Clean.\n\n### [liu2021cagrad] Liu et al. (2021) — Conflict-Averse Gradient Descent for Multi-task Learning\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"treat gradient conflict as the root cause\".\n- Notes: Clean.\n\n### [bachlechner2021rezero] Bachlechner et al. (2021) — ReZero is All You Need: Fast Convergence at Large Depth\n- Exists: ✓\n- Authors: ✗ — \"Mao, Henry\" should be **\"Mao, Huanru Henry\"**; \"Cottrell, Gary\" should be **\"Cottrell, Garrison W.\"** per UAI proceedings (PMLR v161)\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (UAI 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"initializes a single trainable scalar at zero to stabilize deep network training\". Exact description of ReZero.\n- Notes: Minor author name corrections needed.\n\n### [grattafiori2024llama3] Grattafiori et al. (2024) — The Llama 3 Herd of Models\n- Exists: ✓\n- Authors: ✓ (Aaron Grattafiori first author in latest arXiv version v3)\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (arXiv preprint, no peer-reviewed venue)\n- arXiv→published upgrade needed: No (industry report, no conference publication)\n- Context usage correct: ✓ — Cited for Llama-3.1-8B-Instruct model.\n- Notes: Clean.\n\n### [gromov2024unreasonable] Gromov et al. (2025) — The Unreasonable Ineffectiveness of the Deeper Layers\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (bib says 2025, correct for ICLR 2025; bib key uses 2024 arXiv year, cosmetic only)\n- Title: ✓\n- Venue: ✓ (ICLR 2025)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"early layers capture local syntax while later layers integrate long-range context\" and \"layer pruning\". Consistent with the paper's findings about deeper layers being removable.\n- Notes: Clean.\n\n### [srivastava2015highway] Srivastava et al. (2015) — Highway Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2015)\n- Title: ✓\n- Venue: ✓ (ICML 2015 Deep Learning Workshop)\n- arXiv→published upgrade needed: No (workshop citation is standard practice; full paper \"Training Very Deep Networks\" exists at NeurIPS 2015 but under different title)\n- Context usage correct: ✓ — Cited for \"highway networks\" in gating context.\n- Notes: Clean.\n\n### [hu2022lora] Hu et al. (2022) — LoRA: Low-Rank Adaptation of Large Language Models\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ICLR 2022)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for LoRA fine-tuning method.\n- Notes: Clean.\n\n### [zhang2020dialogpt] Zhang et al. (2020) — DialoGPT: Large-Scale Generative Pre-training for Conversational Response Generation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2020)\n- Title: ✓\n- Venue: ✓ (ACL 2020 System Demonstrations)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Clean.\n\n### [roller2021recipes] Roller et al. (2021) — Recipes for Building an Open-Domain Chatbot\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (EACL 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Clean.\n\n### [zheng2024judging] Zheng et al. (2023) — Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (year field says 2023, correct for NeurIPS 2023)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2023, Datasets and Benchmarks Track)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"MT-Bench\" benchmark.\n- Notes: Bib key `zheng2024judging` uses 2024 but year field is 2023. Cosmetic key inconsistency only; no impact on rendered output.\n\n### [clark2019what] Clark et al. (2019) — What Does BERT Look At? An Analysis of BERT's Attention\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019 BlackboxNLP Workshop)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"head specialization\" analysis.\n- Notes: Clean.\n\n### [voita2019analyzing] Voita et al. (2019) — Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"head specialization\" analysis.\n- Notes: Clean.\n\n### [kovaleva2019revealing] Kovaleva et al. (2019) — Revealing the Dark Secrets of BERT\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (EMNLP 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for attention analysis/head specialization.\n- Notes: Clean.\n\n### [liu2024lost] Liu et al. (2024) — Lost in the Middle: How Language Models Use Long Contexts\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2024)\n- Title: ✓\n- Venue: ✓ (TACL 2024, volume 12, pp 157-173)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"positional bias calibration\".\n- Notes: Clean.\n\n### [zhang2019bridging] Zhang et al. (2019) — Bridging the Gap between Training and Inference for Neural Machine Translation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"bridging strategies for NMT\" in exposure bias context.\n- Notes: Clean.\n\n### [mihaylova2019scheduled] Mihaylova & Martins (2019) — Scheduled Sampling for Transformers\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (ACL 2019 Student Research Workshop, pp 351-356)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"extended scheduled sampling to transformers for single-turn NMT\". Accurate.\n- Notes: Clean.\n\n### [dou2019attention] Dou et al. (2019) — Attention Forcing for Sequence-to-sequence Model Training\n- Exists: ✓\n- Authors: ✓ (Qingyun Dou, Yiting Lu, Joshua Efiong, Mark J. F. Gales)\n- Year: ✓ (2019)\n- Title: ✓\n- Venue: ✓ (arXiv preprint; ICLR 2020 submission was not accepted)\n- arXiv→published upgrade needed: No (remains unpublished)\n- Context usage correct: ✓ — Cited for \"proposed attention forcing (supervising cross-attention during NMT)\". Accurate description.\n- Notes: Clean.\n\n### [dou2022parallel] Dou & Gales (2022) — Parallel Attention Forcing for Machine Translation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (arXiv preprint; no peer-reviewed venue found)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"extended [attention forcing] with KL-divergence switching\". Consistent with the paper.\n- Notes: Clean.\n\n### [li2016persona] Li et al. (2016) — A Persona-Based Neural Conversation Model\n- Exists: ✓\n- Authors: ✓ (minor: \"Georgios Spithourakis\" missing middle initial \"P.\" per ACL Anthology)\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (ACL 2016, pp 994-1003)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for early dialogue systems.\n- Notes: Very minor — \"Georgios Spithourakis\" could be \"Georgios P. Spithourakis\".\n\n### [xu2022goldfish] Xu et al. (2022) — Beyond Goldfish Memory: Long-Term Open-Domain Conversation\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ACL 2022, pp 5180-5197)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"modern long-context models\" in dialogue.\n- Notes: Clean.\n\n### [veit2016residual] Veit et al. (2016) — Residual Networks Behave Like Ensembles of Relatively Shallow Networks\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2016)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2016)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"residual networks can be viewed as ensembles of shallow paths\". Exact main thesis.\n- Notes: Clean.\n\n### [dong2021attention] Dong et al. (2021) — Attention is Not All You Need: Pure Attention Loses Rank Doubly Exponentially with Depth\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (ICML 2021, pp 2793-2803)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"attention collapse in deep transformers\". Accurate.\n- Notes: Clean.\n\n### [lin2022truthfulqa] Lin et al. (2022) — TruthfulQA: Measuring How Models Mimic Human Falsehoods\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2022)\n- Title: ✓\n- Venue: ✓ (ACL 2022, pp 3214-3252)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited as an evaluation benchmark in Limitations section.\n- Notes: Clean.\n\n### [hendrycks2021measuring] Hendrycks et al. (2021) — Measuring Massive Multitask Language Understanding\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2021)\n- Title: ✓\n- Venue: ✓ (ICLR 2021)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for \"MMLU 5-shot\" benchmark. Accurate.\n- Notes: Clean.\n\n### [dettmers2023qlora] Dettmers et al. (2023) — QLoRA: Efficient Finetuning of Quantized LLMs\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2023)\n- Title: ✓\n- Venue: ✓ (NeurIPS 2023)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited alongside LoRA for fine-tuning setup.\n- Notes: Clean.\n\n### [ding2023ultrachat] Ding et al. (2023) — Enhancing Chat Language Models by Scaling High-quality Instructional Conversations\n- Exists: ✓\n- Authors: ✓\n- Year: ✓ (2023)\n- Title: ✓\n- Venue: ✓ (EMNLP 2023)\n- arXiv→published upgrade needed: No\n- Context usage correct: ✓ — Cited for UltraChat dataset used in all experiments.\n- Notes: Clean.\n\n---\n\n## Uncited Entries Detail (for completeness)\n\n### [hsieh2024found] — Verified ✓, Findings ACL 2024, all fields correct. Not cited.\n### [luo2025flexidepth] — Verified ✓, COLM 2025, all fields correct. Not cited.\n### [navon2022nash] — Verified ✓, ICML 2022, all fields correct. Not cited.\n### [vaswani2017attention] — Verified ✓, NeurIPS 2017, all fields correct. Not cited.\n### [he2016deep] — Verified ✓, CVPR 2016, all fields correct. Not cited.\n### [vig2019multiscale] — Verified ✓, ACL 2019 Demo, all fields correct. Not cited.\n### [abnar2020quantifying] — Verified ✓, ACL 2020, all fields correct. Not cited.\n### [ethayarajh2019contextual] — Verified ✓, EMNLP 2019, all fields correct. Not cited.\n### [brunner2020identifiability] — **Author error**: \"Andreas Krause\" should be \"Roger Wattenhofer\". Not cited.\n### [zhou2020drophead] — Verified ✓, Findings EMNLP 2020, all fields correct. Not cited.\n### [dauphin2017language] — Verified ✓, ICML 2017, all fields correct. Not cited.\n### [shazeer2020glu] — Verified ✓, arXiv preprint (never published), all fields correct. Not cited.\n"
  }
}
```

</details>

---

### Tool result

_source line 302 · 2026-05-26T10:24:49.888672+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/turn_residual_gating/artifacts/citation_audit_worker1.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_research_citation-audit-1_20260526T101436",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 303 · 2026-05-26T10:24:49.888860+00:00_

审计完成。报告已写入 `artifacts/citation_audit_worker1.md`。

核心发现：

**3 个关键错误：**
1. **`laban2025lost`** — 已发表于 ICLR 2026（Oral + Best Paper），但 bib 仍引为 arXiv 2025 预印本
2. **`raposo2024mixture`** — 会议写错：实际是 ICLR 2025，bib 写成 ICML 2024
3. **`he2019exposure`** — 已发表于 EMNLP 2021 且标题完全改变（"Exposure Bias versus Self-Recovery..."），bib 仍用 2019 arXiv 旧标题

**2 个次要问题：**
4. **`brunner2020identifiability`**（未被引用）— 末位作者 "Andreas Krause" 应为 "Roger Wattenhofer"
5. **`bachlechner2021rezero`** — 作者名应为 "Huanru Henry Mao" 和 "Garrison W. Cottrell"

**0 篇幻觉论文。** 全部 58 条 bib entry 均真实存在。12 条在 bib 中但未被正文引用。46 条被引用的论文中，41 条完全正确，上下文使用均准确。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_research_citation-audit-1_20260526T101436"
}
```

</details>

---
