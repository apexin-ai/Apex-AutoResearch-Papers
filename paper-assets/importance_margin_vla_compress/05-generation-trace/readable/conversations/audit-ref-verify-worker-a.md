# audit ref verify worker A

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 267
- **Recorded user turns:** 0
- **Tool calls:** 133
- **Original source:** `logs/chats/worker_audit_ref_verify_worker_A_20260529T062907.jsonl`
- **Structured JSON:** [`05276a46fc3eaddf2c57.json`](../../sessions/05/05276a46fc3eaddf2c57.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

267 recorded events

### Tool call

_source line 1 · 2026-05-29T06:37:33.888687+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-29T06:37:33.889502+00:00_

1	% References for: The Cliff Edge — Why Vision Token Reduction Fails
2	% Catastrophically in VLA Closed-Loop Control
3	% Auto-generated from literature_map.yaml (verified entries only)
4	% 2026-05-17
5	
6	% ============================================================
7	% Attention Analysis
8	% ============================================================
9	
10	@inproceedings{abnar2020quantifying,
11	  title={Quantifying Attention Flow in Transformers},
12	  author={Abnar, Samira and Zuidema, Willem},
13	  booktitle={Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics},
14	  pages={4190--4197},
15	  year={2020},
16	}
17	
18	% ============================================================
19	% VLA Token Compression (concurrent work)
20	% ============================================================
21	
22	@article{gao2025compressorvla,
23	  title={Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation},
24	  author={Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing},
25	  journal={arXiv preprint arXiv:2511.18950},
26	  year={2025},
27	  eprint={2511.18950},
28	  archivePrefix={arXiv}
29	}
30	
31	@article{wang2025specprunevla,
32	  title={SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning},
33	  author={Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao},
34	  journal={arXiv preprint arXiv:2509.05614},
35	  year={2025},
36	  eprint={2509.05614},
37	  archivePrefix={arXiv}
38	}
39	
40	@inproceedings{jiang2026lightvla,
41	  title={The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning},
42	  author={Jiang, Titong and Jiang, Xuefeng and Ma, Yuan and Wen, Xin and Li, Bailin and Zhan, Kun and Jia, Peng and Liu, Yahui and Sun, Sheng and Lang, Xianpeng},
43	  booktitle={Proceedings of the IEEE International Confe
…[truncated 24180 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-29T06:37:33.889826+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-29T06:37:33.890059+00:00_

docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/experimental_setup.tex
docs/paper/discussion.tex
docs/paper/analysis.tex
docs/paper/background.tex
docs/paper/main.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/results.tex
docs/paper/results_v2.tex
docs/paper/appendix.tex
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/conclusion.tex
docs/paper/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-29T06:37:33.890340+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-29T06:37:33.890606+00:00_

1	\documentclass{article}
2	
3	\usepackage{corl_2026} % Submission version: anonymous, line numbers enabled.
4	% \usepackage[final]{corl_2026} % Uncomment for camera-ready.
5	
6	\usepackage{amsmath,amssymb}
7	\usepackage{graphicx}
8	\usepackage{booktabs}
9	\usepackage{multirow}
10	\usepackage{enumitem}
11	\usepackage{subcaption}
12	\usepackage{wrapfig}
13	
14	% Tighten float spacing for page limit
15	\setlength{\textfloatsep}{6pt plus 2pt minus 4pt}
16	\setlength{\floatsep}{6pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 4pt}
18	\setlength{\abovecaptionskip}{3pt}
19	\setlength{\belowcaptionskip}{0pt}
20	\setlength{\abovedisplayskip}{6pt plus 2pt minus 4pt}
21	\setlength{\belowdisplayskip}{6pt plus 2pt minus 4pt}
22	
23	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	
30	\keywords{vision-language-action models, token pruning, robot learning}
31	
32	\input{introduction}
33	
34	\input{related_work}
35	
36	\input{method}
37	
38	\input{experiments}
39	
40	\input{conclusion}
41	
42	\input{limitations}
43	
44	\bibliography{references}
45	
46	\input{appendix}
47	
48	\end{document}
49	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-29T06:37:33.890823+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-29T06:37:33.891023+00:00_

1	\begin{abstract}
2	Deploying Vision-Language-Action (VLA) models for real-time control requires compressing their vision token sequences, yet identical pruning applied to different architectures produces wildly divergent outcomes---from unscathed performance to total collapse. We trace this divergence to the vision-language connector, the module bridging the visual encoder and language backbone. Across six VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, a single forward-pass diagnostic---the coefficient of variation (CV) of post-connector token norms---predicts pruning tolerance without any task evaluation. Low-CV connectors permit aggressive pruning; high-CV connectors collapse when even a few tokens are removed. No scoring method is universally safe: the advantage of importance-based over random selection follows an inverted-U curve that peaks at moderate compression and reverses at aggressive ratios, with task complexity amplifying connector-dependent patterns. A zero-mask ablation reveals that position disruption, not information loss, is the binding constraint. For architectures where all deletion fails, a lightweight re-encoder (${\sim}$5\% extra parameters) recovers baseline performance at 75\% compression.
3	\end{abstract}
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-29T06:37:33.891251+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-29T06:37:33.891488+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Vision-Language-Action (VLA) models process robot observations as hundreds of vision tokens, creating a computational bottleneck for real-time control. Token pruning---removing low-importance tokens before the language backbone---is well-established for vision transformers~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and has been applied to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}. Yet each method validates on a single architecture, implicitly assuming that pruning transfers across designs.
15	
16	This assumption is unsafe. Current VLAs employ fundamentally different vision connectors---linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}---each imposing distinct constraints on how visual information distributes across tokens. Whether a pruning strategy validated on one connector type will transfer to another is unknown; deploying it blindly risks silent degradation or complete failure.
17	
18	We present the first cross-architecture study of VLA token compressibility, evaluating six architectures (450M--7
…[truncated 1267 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-29T06:37:33.891733+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-29T06:37:33.891952+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv}, PruMerge~\cite{shang2024prumerge}, SparseVLM~\cite{zhang2025sparsevlm}, SparseVILA~\cite{khaki2025sparsevila}, and FitPrune~\cite{ye2025fitprune} reduce vision tokens in VLMs using attention or importance signals. VLA-specific methods have emerged: VLA-IAP~\cite{cheng2026vlaiap}, VLA-Cache~\cite{xu2025vlacache}, EfficientVLA~\cite{yang2025efficientvla}, VLA-Pruner~\cite{liu2025vlapruner}, LightVLA~\cite{jiang2026lightvla}, Compressor-VLA~\cite{gao2025compressorvla}, SpecPrune-VLA~\cite{wang2025specprunevla}, and See What Matters~\cite{feng2026seewhatmatters}. Each validates on a single architecture; we ask how architectural choices determine which compression approaches succeed or fail.
9	
10	\paragraph{Concurrent work.}
11	Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
12	
13	\paragraph{Vision connectors.}
14	LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
15	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-29T06:37:33.892370+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/background.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-29T06:37:33.892696+00:00_

1	% background.tex -- Section 2: Background
2	
3	\section{Background}
4	\label{sec:background}
5	
6	This section describes the architectures and benchmark used in our study: SmolVLA~\cite{shukor2025smolvla} and OpenVLA~\cite{kim2024openvla}, two VLA models with contrasting vision connector designs, and the LIBERO benchmark~\cite{liu2023libero} on which we evaluate closed-loop performance.
7	
8	\subsection{SmolVLA Architecture}
9	\label{sec:smolvla_arch}
10	
11	Vision-Language-Action (VLA) models cast robotic control as conditional generation: given a camera observation and a language instruction, the model predicts a continuous action.
12	SmolVLA~\cite{shukor2025smolvla} instantiates this paradigm with approximately 450M parameters, organized into a vision encoder, a vision connector, a language model backbone, and an action head.
13	Figure~\ref{fig:architecture} contrasts the vision pipelines of SmolVLA and OpenVLA, highlighting the connector designs that determine compressibility.
14	
15	\begin{figure}[t]
16	\centering
17	\includegraphics[width=\linewidth]{figures/paper/fig_architecture.pdf}
18	\caption{Vision connector comparison. \textbf{Left}: SmolVLA applies $4{\times}4$ pixel-shuffle to fold 1024 SigLIP patches into 64 tokens per camera (128 total), creating dense, spatially entangled representations. \textbf{Right}: OpenVLA uses an MLP projector that maps each patch independently, producing 256 tokens with per-token independence. We hypothesize that this architectural difference is the primary factor governing token compressibility: pixel-shuffle tokens resist any form of deletion, while independently projected tokens allow graded pruning.}
19	\label{fig:architecture}
20	\end{figure}
21	
22	\paragraph{Vision encoder.}
23	SmolVLA uses the Sigmoid Loss for Language-Image Pre-training (SigLIP) encoder~\cite{zhai2023siglip} to process visual input.
24	SigLIP divides each camera image into non-overlapping spatial patches on a $32 \times 32$ grid, producing 1024 p
…[truncated 6243 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-29T06:37:33.892937+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-29T06:37:33.893250+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). To preview each connector's compressibility, we report the coefficient of variation (CV) of post-connector token L2 norms---the ratio of standard deviation to mean across all vision tokens from a single forward pass (formally defined in Section~\ref{sec:cv_diagnostic}). \textbf{Linear projection} applies a per-patch matrix multiplication ($\pi_{0}$~\cite{black2024pi0}, $\pi_{0.5}$~\cite{black2025pi05}; CV$\,{<}\,$0.06). \textbf{MLP projectors} map each patch independently through a multi-layer perceptron (OpenVLA~\cite{kim2024openvla}, OFT~\cite{kim2025openoft}; CV$\,{\approx}\,$0.22). \textbf{Token-entangling connectors} create cross-token dependencies: X-VLA~\cite{zheng2025xvla} uses a 12-layer BART encoder~\cite{lewis2020bart} (CV$\,{=}\,$0.151); SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 patches per token (CV$\,{=}\,$0.314). We classify coupling as \emph{independent} (one patch per output) or \emph{entangling} (multiple patches). Four models are evaluated in closed-loop on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT contribute to the CV diagnostic only.
8	
9	\begin{figure*}[t]
10	\centering
11	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v4.pdf}
12	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressibility fragility. Independent connectors yield low CV; entangling connectors create cross-token dependencies and higher CV.}
13	\label{fig:architecture}
14	\end{figure*}
15	
16	\subsection{Pruning Protocol}
17	\label{sec:pruning_protocol}
18	
19	Given $N$ post-connector tokens $\{t_1, \ldots, t_N\}$ with $t_i \in \mathbb{R}^d$, token pruning retains $\lfloor k \cdot N \rfloor$ tokens for 
…[truncated 7308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-29T06:37:33.893497+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-29T06:37:33.893820+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
8	
9	\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only.
10	
11	\paragraph{Protocol.} We prune at $k \in \{0.3, 0.5, 0.7, 0.75, 0.85, 0.9, 0.95\}$ and report mean SR over 500 episodes. Multi-seed results ($\pi_{0.5}$ Long: $n{=}5$; VTR: $n{=}3$) report mean $\pm$ s.d.\ with per-seed breakdowns in the appendix.
12	
13	\begin{figure}[t]
14	\centering
15	\includegraphics[width=0.75\linewidth]{figures/paper/fig_pruning_overview.pdf}
16	\caption{Pruning degradation on LIBERO-Object (L2 norm scoring). $\pi_{0.5}$ maintains ${\geq}$98\% through $k{=}0.85$, OpenVLA degrades linearly, X-VLA cliffs at $k{=}0.7$, SmolVLA collapses to 0\% at $k{=}0.95$.}
17	\label{fig:pruning_overview}
18	\end{figure}
19	
20	\subsection{Two-Axis Framework Overview}
21	\label{sec:two_axis}
22	
23	Three qualitatively distinct response patterns emerge across the connector spectrum (Table~\ref{tab:main_results}; Figure~\ref{fig:pruning_overview}); a fourth (OpenVLA, MLP connector) is detailed in Appendix Table~\ref{tab:full_results}.
24	
25	\textbf{$\pi_{0.5}$ (linear, CV$\,{=}\,$0.055).} Low-CV models are \emph{uniformly critical}: which tokens are removed matters more than how many. On Obje
…[truncated 9294 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-29T06:37:33.894052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-29T06:37:33.894466+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, is strongly associated with pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A pairwise comparison between $\pi_0$ and OpenVLA (both consuming 256 SigLIP-based~\cite{zhai2023siglip} tokens but differing in connector, backbone, and encoder fusion) yields a 63\,pp gap at $k{=}0.1$; this gap is consistent with the monotonic CV-degradation pattern across all seven models (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$: offline metrics only, no clo
…[truncated 15854 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-29T06:37:33.894707+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/results_v2.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-29T06:37:33.895076+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across six VLA models spanning three connector families on LIBERO-Object~\cite{liu2023libero} (10 tasks, 50 episodes each, 500 total). All success rates report Wilson 95\% confidence intervals for single-seed results and mean $\pm$ standard deviation for multi-seed results.
5	
6	\subsection{Taxonomy Overview}
7	\label{sec:taxonomy_overview}
8	
9	Table~\ref{tab:taxonomy} organizes seven models into four response classes. The taxonomy reveals that effective vision-to-LLM pipeline complexity, not the nominal connector label or model scale, determines pruning tolerance. Token importance CV tracks this ordering continuously across an 8$\times$ parameter range (450M to 7B): uniformly critical models cluster at CV $< 0.06$, threshold-graded at $\sim$0.15, smooth graded at $\sim$0.22, and catastrophic cliff at $>$0.3. A controlled comparison between $\pi_0$ and OpenVLA (both using 256 SigLIP~\cite{zhai2023siglip} tokens, differing only in connector) yields a 63\,pp gap at $k{=}0.1$, isolating the pipeline as causal (Section~\ref{sec:linear_results}).
10	
11	The four classes differ qualitatively in their failure mode. Uniformly critical models ($\pi_0$, $\pi_0.5$~\cite{black2025pi05}) distribute importance so evenly that no scoring method can identify dispensable tokens; pruning either preserves random spatial coverage (and survives) or removes a clustered patch (and fails). Threshold-graded models (X-VLA) tolerate removal up to a sharp onset point. Smooth graded models (OpenVLA, OFT, CogACT) degrade proportionally to the fraction removed. Catastrophic cliff models (SmolVLA) collapse at any removal level.
12	
13	\begin{table*}[t]
14	\centering
15	\small
16	\caption{Seven-model connector taxonomy. CV = coefficient of variation of vision token L2 norms. $^\dagger\pi_0$ reports offline normalized L1 action loss (pending closed-loop evaluation). $^\ddagger$X-VLA uses a linear projection followed by a 12-lay
…[truncated 15971 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-29T06:37:33.895344+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-29T06:37:33.895555+00:00_

1	\section{Discussion}
2	\label{sec:analysis}
3	
4	CV predicts connector-level compressibility, but task complexity determines \emph{which} scoring method succeeds within a given connector. On OpenVLA, L2 leads on single-step Object ($+$7.8\,pp at $k{=}0.9$) but the hierarchy inverts on multi-step Long, where Random outperforms both L2 and attention at $k{=}0.7$ (Appendix~\ref{app:extended_discussion}). The monotonic L2 curve versus the non-monotonic random curve on $\pi_{0.5}$ Long (Figure~\ref{fig:cliff_highlight}) reflects position encoding sensitivity: L2 preserves spatial locality after re-indexing, while random creates scattered gaps that maximally disrupt RoPE at $k{\approx}0.9$ before recovering at $k{\leq}0.7$ as surviving positions become approximately uniform (Appendix~\ref{app:extended_discussion}).
5	
6	\paragraph{Limitations.}
7	All evaluations use LIBERO simulation; we provide no sim-to-real evidence. The six architectures differ in backbone, encoder, and scale beyond the connector, preventing causal isolation. The CV--SR correlation relies on four closed-loop models, too few for a general law. VTR is validated on SmolVLA only. Most conditions use a single seed; $\pi_{0.5}$ Long uses five-seed means ($n{=}5$, sample s.d.\ ${\leq}$2.7\,pp; Appendix~\ref{app:pi05_long_multiseed}); cross-seed validation on other models shows $\Delta \leq 5.8$\,pp (Appendix~\ref{app:pi05_multiseed},~\ref{app:openvla_multiseed}). Extended discussion in Appendix~\ref{app:extended_discussion}.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-29T06:37:33.895770+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-29T06:37:33.895967+00:00_

1	% Discussion section moved to Appendix (§\ref{app:discussion}) for space.
2	% Three-sentence limitations retained at end of Experiments section.
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-29T06:37:33.896179+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-29T06:37:33.896384+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	\label{sec:analysis}
4	
5	We set out to understand why identical token pruning produces dramatically different outcomes across VLA architectures. The vision-language connector emerges as the strongest predictor: its coefficient of variation (CV), computable from a single forward pass, partitions architectures into compressibility regimes. Token-independent connectors degrade gracefully while entangling connectors exhibit catastrophic cliffs amplified by task complexity (Appendix~\ref{app:extended_discussion}). No scoring method is universally safe---the importance margin follows an inverted-U curve that reverses at aggressive ratios---and position disruption, not information loss, is the binding constraint. For connectors where all deletion fails, VTR recovers baseline performance at 75\% compression. Practitioners should compute CV before deploying any pruning strategy to identify the appropriate compression regime for their architecture.
6	
7	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-29T06:37:33.896594+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/limitations.tex"
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-29T06:37:33.896797+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	All evaluations use LIBERO simulation; real-robot validation with sensor noise and contact dynamics would further strengthen applicability. Most conditions use a single evaluation seed ($\pi_{0.5}$ Long: $n{=}5$, s.d.\ ${\leq}$2.7\,pp); additional seeds on other models would tighten confidence intervals. VTR is validated on SmolVLA; extending to other entangling connectors is a natural next step.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-29T06:37:33.896994+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-29T06:37:33.897200+00:00_

File content (27358 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-29T06:37:33.897438+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-29T06:37:33.898021+00:00_

1	\clearpage
2	\appendix
3	
4	\section{Full Pruning Results}
5	\label{app:full_results}
6	
7	Table~\ref{tab:full_results} reports the complete closed-loop success rates for all four models across all tested retention ratios, including OpenVLA and $k{=}0.7$ data omitted from Table~\ref{tab:main_results} for space.
8	
9	\begin{table*}[ht]
10	\centering
11	\footnotesize
12	\caption{Available closed-loop success rates (\%) on LIBERO under L2 norm (L2) and random (R) token pruning. Best result per row in \textbf{bold}. ``--'' indicates data not yet collected. OpenVLA Goal, Spatial, and Long use per-suite fine-tuned checkpoints. Single seed (seed 42) except $\pi_{0.5}$ Long (five-seed mean, $n{=}5$). \textsuperscript{$\dagger$}Attention-based scoring (A) at $k{=}0.9$ for OpenVLA.}
13	\label{tab:full_results}
14	\setlength{\tabcolsep}{4pt}
15	\begin{tabular}{llccccc}
16	\toprule
17	Model & Suite & Baseline & $k{=}0.95$ (L2 / R) & $k{=}0.9$ (L2 / R) & $k{=}0.7$ (L2 / R) & $k{=}0.5$ (L2 / R) \\
18	\midrule
19	\multirow{4}{*}{$\pi_{0.5}$}
20	& Object  & \textbf{98.2} & 98.2 / 74.0 & \textbf{98.2} / 9.0 & 55.0 / 74.0 & 33.4 / 69.4 \\
21	& Spatial & \textbf{97.2} & \textbf{97.8} / 76.4 & 95.0 / 54.6 & 67.0 / 74.4 & 55.6 / 71.6 \\
22	& Goal    & \textbf{96.4} & 89.4 / 84.0 & 90.6 / 62.2 & 71.2 / 78.2 & 59.2 / 73.6 \\
23	& Long    & \textbf{91.6} & 86.8 / 61.2 & 80.4 / 33.6 & 63.2 / 64.6 & 51.7 / 50.4 \\
24	\midrule
25	\multirow{4}{*}{X-VLA}
26	& Object  & \textbf{99.2} & 99.0 / 98.8 & 99.2 / 97.8 & 56.2 / 65.2 & 43.4 / 70.6 \\
27	& Spatial & \textbf{93.0} & 71.6 / 70.2 & 78.8 / 77.8 & 72.0 / -- & 58.8 / 71.4 \\
28	& Goal    & \textbf{98.4} & 53.8 / 54.0 & 70.2 / 70.6 & 53.4 / 57.2 & 59.0 / 67.2 \\
29	& Long    & \textbf{94.0} & 47.0 / 48.2 & 27.5 / 29.6 & -- / -- & 45.0 / 61.6 \\
30	\midrule
31	\multirow{4}{*}{OpenVLA}
32	& Object  & \textbf{74.0} & 70.6 / -- & 70.6 / 62.8 / 61.4\textsuperscript{$\dagger$} & -- / -- & 39.2 / 35.8 \\
33	& Goal    & \textbf{74.8} & -- / -- & 74.8 
…[truncated 37518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-29T06:37:33.898303+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-29T06:37:33.898522+00:00_

File unchanged since last read. The content from the earlier Read tool_result in this conversation is still current — refer to that instead of re-reading.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-29T06:37:33.898718+00:00_

called Grep

<details open><summary>🔧 Tool call — Grep</summary>

```json
{
  "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
  "output_mode": "content",
  "head_limit": "0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Grep",
  "tool_args": {
    "pattern": "\\\\cite[pt]?\\{[^}]+\\}",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper",
    "output_mode": "content",
    "head_limit": "0"
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-29T06:37:33.899013+00:00_

&lt;persisted-output>
Output too large (19.9KB). Full output saved to: /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d1c43d49-176c-4cc5-b7a0-739614d052fe/tool-results/toolu_01NmvgK8DNsMqKmFavVDvhT8.txt

Preview (first 2KB):
docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
docs/paper/related_work.tex:8:[Omitted long matching line]
docs/paper/related_work.tex:11:Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
docs/paper/related_work.tex:14:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are e
…[truncated 319 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Grep",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-29T06:37:33.899320+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d1c43d49-176c-4cc5-b7a0-739614d052fe/tool-results/toolu_01NmvgK8DNsMqKmFavVDvhT8.txt"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/d1c43d49-176c-4cc5-b7a0-739614d052fe/tool-results/toolu_01NmvgK8DNsMqKmFavVDvhT8.txt"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-29T06:37:33.899697+00:00_

1	docs/paper/related_work.tex:5:DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, Token Merging~\cite{bolya2023tome}, and CrossGET~\cite{shi2024crossget} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss, but robotic manipulation inverts the spatial-insensitivity assumption. None has been evaluated in closed-loop VLA control.
2	docs/paper/related_work.tex:8:[Omitted long matching line]
3	docs/paper/related_work.tex:11:Jabbour et al.~\cite{jabbour2025dontrun} independently observe that pruning breaks VLA policies and propose recovery fine-tuning. Our work is complementary: we conduct a systematic cross-architecture analysis identifying the connector as the key factor, with a zero-cost CV diagnostic and characterization of connector--scoring--task interactions.
4	docs/paper/related_work.tex:14:LLaVA~\cite{liu2023llava} projects patches independently through an MLP; BLIP-2~\cite{li2023blip2} uses cross-attention queries; pixel shuffle~\cite{shi2016subpixel} folds spatial neighborhoods into channels. These create qualitatively different token dependencies whose pruning consequences have not been characterized.
5	docs/paper/experiments.tex:7:\paragraph{Benchmark.} We evaluate on LIBERO~\cite{liu2023libero}, a simulated tabletop manipulation benchmark with four suites of increasing complexity: \textbf{Object} (10 tasks, visually similar objects), \textbf{Spatial} (10, relative spatial layouts), \textbf{Goal} (10, goal-conditioned manipulation), and \textbf{Long} (10, chained 3--5 step sequences). Each task has 50 demo and 50 evaluation episodes (500 per suite).
6	docs/paper/experiments.tex:9:\paragraph{Models.} Four VLAs are evaluated in closed-loop control (Table~\ref{tab:model_properties}): $\pi_{0.5}$~\cite{black2025pi05}, X-VLA~\cite{zheng2025xvla}, OpenVLA~\cite{kim2024openvla}, and SmolVLA~\cite{shukor2025smolvla}. Two additional models ($\pi_{0}$, OFT) contribute to the CV diagnostic via offline metrics only
…[truncated 18716 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-29T06:37:33.899929+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
  "offset": "500",
  "limit": "500"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex",
    "offset": "500",
    "limit": "500"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-29T06:37:33.900508+00:00_

500	\begin{tabular}{lccccr}
501	\toprule
502	$M$ & Seed 42 & Seed 43 & Seed 44 & Mean $\pm$ Std \\
503	\midrule
504	32 & 61.6 & 59.2 & 59.6 & 60.1 $\pm$ 1.3 \\
505	64 & 61.6 & 60.0 & 64.4 & 62.0 $\pm$ 2.2 \\
506	96 & 52.6 & 58.2 & 52.8 & 54.5 $\pm$ 3.2 \\
507	128 & 59.8 & 54.0 & 60.2 & 58.0 $\pm$ 3.5 \\
508	\bottomrule
509	\end{tabular}
510	\end{table}
511	
512	
513	\section{VTR Full Results}
514	\label{app:vtr_full}
515	
516	\begin{table}[ht]
517	\centering
518	\small
519	\caption{VTR re-encoding on SmolVLA (LIBERO-Object). Cross-attention and MLP adapter results report mean $\pm$ std over 3 seeds (500 episodes each). The M-curve is flat: $M{=}16$ (87.5\% compression) matches $M{=}128$ (passthrough) within 1.1\,pp. The baseline control (100K extra training, no compressor) confirms the gain is architectural. ``Compression'' = fraction of tokens removed.}
520	\label{tab:vtr_results}
521	\begin{tabular}{lccr}
522	\toprule
523	Configuration & $M$ & Compression & SR (\%) \\
524	\midrule
525	\textit{SmolVLA-Base (LoRA)} & 128 & 0\% & 44.8 \\
526	\textit{SmolVLA official} & 128 & 0\% & 59.2 \\
527	\textit{Baseline control (+100K steps)} & 128 & 0\% & 45.0 \\
528	\textit{Hard pruning (any $k$)} & -- & 5--50\% & 0.0 \\
529	\midrule
530	Cross-attn VTR & 16 & 87.5\% & 56.9 $\pm$ 1.3 \\
531	Cross-attn VTR & 32 & 75\% & 60.1 $\pm$ 1.3 \\
532	Cross-attn VTR & 64 & 50\% & \textbf{62.0 $\pm$ 2.2} \\
533	Cross-attn VTR & 96 & 25\% & 54.5 $\pm$ 3.2 \\
534	Cross-attn VTR & 128 & 0\% & 58.0 $\pm$ 3.5 \\
535	\midrule
536	MLP adapter ($\sim$22M) & 32 & 75\% & 63.4 $\pm$ 2.6 \\
537	\bottomrule
538	\end{tabular}
539	\end{table}
540	
541	
542	\section{Full VTR Ablation}
543	\label{app:smart_compress_full}
544	
545	Table~\ref{tab:smart_compress_full} reports all five VTR configurations. The cross-attention module improves performance regardless of compression: $M \in \{32, 64, 128\}$ all achieve $\sim$60\% SR, exceeding the 44.8\% baseline by 15--17 points ($p < 0.001$, two-proportion $z$-t
…[truncated 39292 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-29T06:37:33.900878+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 44 · 2026-05-29T06:37:33.901090+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-29T06:37:33.901333+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 1",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. gao2025compressorvla: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, year 2025.\n\n3. wang2025specprunevla: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, year 2025.\n\n4. jiang2026lightvla: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong and others. ICRA 2026, arXiv 2509.12594.\n\n5. feng2026seewhatmatters: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu and others. ICML 2026, arXiv 2605.11817.\n\n6. zhang2025sparsevlm: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan and others. ICML 2025, arXiv 2410.04417.\n\n7. khaki2025sparsevila: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir and others. ICCV 2025, arXiv 2510.17777.\n\n8. jabbour2025dontrun: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason and others. arXiv 2510.08464, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 1",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n2. gao2025compressorvla: \"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation\" by Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing. arXiv 2511.18950, year 2025.\n\n3. wang2025specprunevla: \"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning\" by Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao. arXiv 2509.05614, year 2025.\n\n4. jiang2026lightvla: \"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-Language-Action Models via Differentiable Token Pruning\" by Jiang, Titong and others. ICRA 2026, arXiv 2509.12594.\n\n5. feng2026seewhatmatters: \"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model\" by Feng, Yixu and others. ICML 2026, arXiv 2605.11817.\n\n6. zhang2025sparsevlm: \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" by Zhang, Yuan and others. ICML 2025, arXiv 2410.04417.\n\n7. khaki2025sparsevila: \"SparseVILA: Decoupled Visual Sparsity for Efficient VLM Inference\" by Khaki, Samir and others. ICCV 2025, arXiv 2510.17777.\n\n8. jabbour2025dontrun: \"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered\" by Jabbour, Jason and others. arXiv 2510.08464, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-29T06:37:33.901623+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 2",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shukor2025smolvla: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa and others. arXiv 2506.01844, year 2025.\n\n2. kim2024openvla: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin and others. CoRL 2024 (8th Conference on Robot Learning).\n\n3. brohan2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony and others. CoRL 2023.\n\n4. black2024pi0: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin and others. arXiv 2410.24164, year 2024.\n\n5. black2025pi05: \"π0.5: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin and others. CoRL 2025, PMLR volume 305, pages 17-40, arXiv 2504.16054.\n\n6. ghosh2024octo: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya and others. RSS 2024.\n\n7. brohan2023rt1: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony and others. RSS 2023.\n\n8. kim2025openoft: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 2",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shukor2025smolvla: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\" by Shukor, Mustafa and others. arXiv 2506.01844, year 2025.\n\n2. kim2024openvla: \"OpenVLA: An Open-Source Vision-Language-Action Model\" by Kim, Moo Jin and others. CoRL 2024 (8th Conference on Robot Learning).\n\n3. brohan2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Brohan, Anthony and others. CoRL 2023.\n\n4. black2024pi0: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" by Black, Kevin and others. arXiv 2410.24164, year 2024.\n\n5. black2025pi05: \"π0.5: a Vision-Language-Action Model with Open-World Generalization\" by Black, Kevin and others. CoRL 2025, PMLR volume 305, pages 17-40, arXiv 2504.16054.\n\n6. ghosh2024octo: \"Octo: An Open-Source Generalist Robot Policy\" by Octo Model Team, Ghosh, Dibya and others. RSS 2024.\n\n7. brohan2023rt1: \"RT-1: Robotics Transformer for Real-World Control at Scale\" by Brohan, Anthony and others. RSS 2023.\n\n8. kim2025openoft: \"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success\" by Kim, Moo Jin and Finn, Chelsea and Liang, Percy. arXiv 2502.19645, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-29T06:37:33.901971+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 48 · 2026-05-29T06:37:33.902364+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-29T06:37:33.902591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Abnar Zuidema \"Quantifying Attention Flow in Transformers\" ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Abnar Zuidema \"Quantifying Attention Flow in Transformers\" ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 50 · 2026-05-29T06:37:33.902792+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Gao Juntao \"Compressor-VLA\" arXiv 2511.18950"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Gao Juntao \"Compressor-VLA\" arXiv 2511.18950"
  }
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-29T06:37:33.902985+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Wang Hanzhen \"SpecPrune-VLA\" arXiv 2509.05614"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Wang Hanzhen \"SpecPrune-VLA\" arXiv 2509.05614"
  }
}
```

</details>

---

### Tool call

_source line 52 · 2026-05-29T06:37:33.903195+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jiang Titong \"LightVLA\" \"Differentiable Token Pruning\" arXiv 2509.12594"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jiang Titong \"LightVLA\" \"Differentiable Token Pruning\" arXiv 2509.12594"
  }
}
```

</details>

---

### Tool call

_source line 53 · 2026-05-29T06:37:33.903393+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 54 · 2026-05-29T06:37:33.903581+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 55 · 2026-05-29T06:37:33.903776+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 3",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. chen2024fastv: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang and others. ECCV 2024, arXiv 2403.06764.\n\n2. xu2025vlacache: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu and others. NeurIPS 2025.\n\n3. cheng2026vlaiap: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao and others. arXiv 2603.22991, year 2026.\n\n4. rao2021dynamicvit: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming and others. NeurIPS 2021.\n\n5. bolya2023tome: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel and others. ICLR 2023.\n\n6. liang2022evit: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei and others. ICLR 2022.\n\n7. liu2023libero: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo and others. NeurIPS 2023.\n\n8. yang2025efficientvla: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai and others. arXiv 2506.10100, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 3",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. chen2024fastv: \"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models\" by Chen, Liang and others. ECCV 2024, arXiv 2403.06764.\n\n2. xu2025vlacache: \"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" by Xu, Siyu and others. NeurIPS 2025.\n\n3. cheng2026vlaiap: \"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models\" by Cheng, Jintao and others. arXiv 2603.22991, year 2026.\n\n4. rao2021dynamicvit: \"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification\" by Rao, Yongming and others. NeurIPS 2021.\n\n5. bolya2023tome: \"Token Merging: Your ViT But Faster\" by Bolya, Daniel and others. ICLR 2023.\n\n6. liang2022evit: \"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations\" by Liang, Youwei and others. ICLR 2022.\n\n7. liu2023libero: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\" by Liu, Bo and others. NeurIPS 2023.\n\n8. yang2025efficientvla: \"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models\" by Yang, Yantai and others. arXiv 2506.10100, year 2025.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool result

_source line 56 · 2026-05-29T06:37:33.904152+00:00_

Web search results for query: "Abnar Zuidema "Quantifying Attention Flow in Transformers" ACL 2020"

Links: [{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"Quantifying Attention Flow in Transformers","url":"https://notes-vault.pages.dev/Scientific-Literature-References/literature-notes/@abnarQuantifyingAttentionFlow2020"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"UvA-DARE (Digital Academic Repository)","url":"https://pure.uva.nl/ws/files/178487922/2020.acl-main.385.pdf"},{"title":"Attention Flow - AmsterdamNLP","url":"https://amsterdamnlp.github.io/blog/attentionflow/"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"},{"title":"dblp: Quantifying Attention Flow in Transformers.","url":"https://dblp.org/rec/conf/acl/AbnarZ20.html"},{"title":"ACL2020: Quantifying Attention Flow in Transformers","url":"https://virtual.acl2020.org/paper_main.385.html"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"(PDF) Quantifying Attention Flow in Transformers","url":"https://www.researchgate.net/publication/341148976_Quantifying_Attention_Flow_in_Transformers"}]

I found the paper! Here are the key details:

## Paper Information

The paper "Quantifying Attention Flow in Transformers" was authored by Samira Abnar and Willem Zuidema in 2020 and published in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 4190–4197.

## Main Contribution

The paper addresses how in the Transformer model, self-attention combines information from attended embeddings into the representation of the focal embedding in the next
…[truncated 712 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-29T06:37:33.904499+00:00_

Web search results for query: "Wang Hanzhen "SpecPrune-VLA" arXiv 2509.05614"

Links: [{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614v1"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"dblp: Hanzhen Wang","url":"https://dblp.org/pid/417/4388.html"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | OpenReview","url":"https://openreview.net/forum?id=t85Ni0LwjC"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"}]

I found the paper you're looking for! Here's what the search revealed:

"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning" is by Hanzhen Wang and 5 other authors, with the arXiv identifier 2509.05614.

**Key Contributions:**

The paper identifies spatial-temporal consistency in VLA tasks and proposes that token selection should combine local information with global context, presenting SpecPrune-VLA, a training-free, two-level pruning method with heuristic control.

**Method Components:**

1. Action-level static pruning that leverages global history and local attention to statically reduce visual tokens per action

2. Layer-
…[truncated 567 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-29T06:37:33.904766+00:00_

Web search results for query: "Gao Juntao "Compressor-VLA" arXiv 2511.18950"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention","url":"https://www.researchgate.net/publication/397934001_AVA-VLA_Improving_Vision-Language-Action_models_with_Active_Visual_Attention"}]

Based on the search results, I found the paper you're looking for:

Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation is an arXiv paper (2511.18950) by Juntao Gao and 3 other authors.

**Overview:**
The paper proposes Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in Vision-Language-Action (VLA) models.

**Key Challenge and Solution:**
The computational overhead of processing redundant visual tokens is a critical bottleneck for real-time robotic deployment, and while standard token pruning techniques can alleviate this, they struggle to preserve task-critical visual information.

**Technical Approach:**
The Compressor-VLA framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

**Results:**
Experimentally, Compressor-VLA achieves a competitive success
…[truncated 354 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-29T06:37:33.905087+00:00_

Web search results for query: "Jiang Titong "LightVLA" "Differentiable Token Pruning" arXiv 2509.12594"

Links: [{"title":"[2509.12594] The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/abs/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/html/2509.12594v1"},{"title":"LightVLA","url":"https://liauto-research.github.io/LightVLA/"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250912594J/abstract"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"AI Bites | YouTube Channel on X: \"LightVLA, a simple yet effective differentiable token pruning framework for vision-language-action (VLA) models. While VLA models have shown impressive capability in executing real-world robotic tasks, their deployment on resource-constrained platforms is often bottlenecked by https://t.co/bE0Zv0mb0c\" / X","url":"https://x.com/ai_bites/status/1970481721163313156"}]

I found the paper! Here are the search results for your query:

## Paper Information

**LightVLA** is a simple yet effective differentiable
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 60 · 2026-05-29T06:37:33.905347+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor arXiv 2506.01844"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor arXiv 2506.01844"
  }
}
```

</details>

---

### Tool call

_source line 61 · 2026-05-29T06:37:33.905660+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA Open-Source Vision-Language-Action Model Kim Moo Jin CoRL 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA Open-Source Vision-Language-Action Model Kim Moo Jin CoRL 2024"
  }
}
```

</details>

---

### Tool call

_source line 62 · 2026-05-29T06:37:33.905855+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control Brohan CoRL 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control Brohan CoRL 2023"
  }
}
```

</details>

---

### Tool call

_source line 63 · 2026-05-29T06:37:33.906043+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0 Vision-Language-Action Flow Model General Robot Control Black Kevin arXiv 2410.24164"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0 Vision-Language-Action Flow Model General Robot Control Black Kevin arXiv 2410.24164"
  }
}
```

</details>

---

### Tool call

_source line 64 · 2026-05-29T06:37:33.906257+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 65 · 2026-05-29T06:37:33.906465+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 66 · 2026-05-29T06:37:33.906676+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 4",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. liu2025vlapruner: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan and others. arXiv 2511.16449, year 2025.\n\n2. shang2024prumerge: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang and others. Listed as ICCV 2025, but bib key says 2024.\n\n3. liu2023llava: \"Visual Instruction Tuning\" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. NeurIPS 2023.\n\n4. shi2016subpixel: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe and others. CVPR 2016.\n\n5. li2023blip2: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan and others. ICML 2023.\n\n6. zhai2023siglip: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua and others. ICCV 2023.\n\n7. yang2024qwen2: \"Qwen2 Technical Report\" by Yang, An and others. arXiv 2407.10671, year 2024.\n\n8. lipman2023flow: \"Flow Matching for Generative Modeling\" by Lipman, Yaron and others. ICLR 2023.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 4",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. liu2025vlapruner: \"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference\" by Liu, Ziyan and others. arXiv 2511.16449, year 2025.\n\n2. shang2024prumerge: \"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models\" by Shang, Yuzhang and others. Listed as ICCV 2025, but bib key says 2024.\n\n3. liu2023llava: \"Visual Instruction Tuning\" by Liu, Haotian and Li, Chunyuan and Wu, Qingyang and Lee, Yong Jae. NeurIPS 2023.\n\n4. shi2016subpixel: \"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" by Shi, Wenzhe and others. CVPR 2016.\n\n5. li2023blip2: \"BLIP-2: Bootstrapping Language-Image Pre-Training with Frozen Image Encoders and Large Language Models\" by Li, Junnan and others. ICML 2023.\n\n6. zhai2023siglip: \"Sigmoid Loss for Language Image Pre-Training\" by Zhai, Xiaohua and others. ICCV 2023.\n\n7. yang2024qwen2: \"Qwen2 Technical Report\" by Yang, An and others. arXiv 2407.10671, year 2024.\n\n8. lipman2023flow: \"Flow Matching for Generative Modeling\" by Lipman, Yaron and others. ICLR 2023.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool call

_source line 67 · 2026-05-29T06:37:33.907048+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Feng Yixu \"See What Matters\" \"Differentiable Grid Sample Pruning\" arXiv 2605.11817"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Feng Yixu \"See What Matters\" \"Differentiable Grid Sample Pruning\" arXiv 2605.11817"
  }
}
```

</details>

---

### Tool call

_source line 68 · 2026-05-29T06:37:33.907280+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zhang Yuan \"SparseVLM\" \"Visual Token Sparsification\" arXiv 2410.04417"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zhang Yuan \"SparseVLM\" \"Visual Token Sparsification\" arXiv 2410.04417"
  }
}
```

</details>

---

### Tool call

_source line 69 · 2026-05-29T06:37:33.907599+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Khaki Samir \"SparseVILA\" \"Decoupled Visual Sparsity\" arXiv 2510.17777"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Khaki Samir \"SparseVILA\" \"Decoupled Visual Sparsity\" arXiv 2510.17777"
  }
}
```

</details>

---

### Tool call

_source line 70 · 2026-05-29T06:37:33.907799+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Jabbour Jason \"Don't Run with Scissors\" \"Pruning Breaks VLA\" arXiv 2510.08464"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Jabbour Jason \"Don't Run with Scissors\" \"Pruning Breaks VLA\" arXiv 2510.08464"
  }
}
```

</details>

---

### Tool result

_source line 71 · 2026-05-29T06:37:33.908015+00:00_

Web search results for query: "SmolVLA Vision-Language-Action Model Affordable Efficient Robotics Shukor arXiv 2506.01844"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844v1] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"}]

I found the paper! Here are the key details:

**SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics**

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance, and is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs.

**Problem it addresses:**
Existing VLAs are typically massive—often with billions of parameters—leading to high training costs and limited real-world deployability, and they rely on academic and industrial datasets, overlooking the growing availability of communit
…[truncated 711 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 72 · 2026-05-29T06:37:33.908298+00:00_

Web search results for query: "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control Brohan CoRL 2023"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control [Quick Review]","url":"https://liner.com/review/rt2-visionlanguageaction-models-transfer-web-knowledge-to-robotic-control"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"}]

Based on the search results, here's what I found about RT-2:

## Overview

RT-2 is a vision-language-action (VLA) model that directly trains state-of-the-art vision-language models to output low-level robot actions.

## Key Approach

The paper studies how vision-language models trained on Internet-scale data can be incorporated directly into end-to-end robotic control to boost generalization and enable emergent semantic reasoning, with the goal of enabling a single end-to-end trained model to both learn to map robot observations to actions an
…[truncated 816 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-29T06:37:33.908559+00:00_

Web search results for query: "OpenVLA Open-Source Vision-Language-Action Model Kim Moo Jin CoRL 2024"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"[2406.09246] OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/abs/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/openvla-open-source-vision-language-action-model"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model | OpenReview","url":"https://openreview.net/forum?id=ZMnD6QZAE6"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"GitHub - reazon-research/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/reazon-research/openvla"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"dblp: OpenVLA: An Open-Source Vision-Language-Action Model.","url":"https://dblp.org/rec/journals/corr/abs-2406-09246.html"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model Moo Jin Kim∗,1","url":"https://groups.csail.mit.edu/robotics-center/public_papers/Kim24.pdf"}]

I've found comprehensive information about OpenVLA. Here are the key findings:

## Overview

OpenVLA is a state-of-the-art, open-source 7B-parameter VLA model that obtains strong performance for cross-embodiment robot control out-of-the-box and can be easily adapted to new robot setups via parameter-efficient fine-tuning. The paper was published at CoRL 2024.

…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 74 · 2026-05-29T06:37:33.908818+00:00_

Web search results for query: "pi0 Vision-Language-Action Flow Model General Robot Control Black Kevin arXiv 2410.24164"

Links: [{"title":"[2410.24164v1] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164v1"},{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"[2410.24164v3] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164v3"},{"title":"[PDF] π0: A Vision-Language-Action Flow Model for General Robot Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%800:-A-Vision-Language-Action-Flow-Model-for-General-Black-Brown/ef0c2a66b7bc82a2f90ac298310c064a49da8213"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"$π_0$: A Vision-Language-Action Flow Model for General Robot Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241024164B/abstract"},{"title":"π0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/pdf/2410.24164v1"}]

I found the paper you're looking for. Here's information about it:

π₀: A Vision-Language-Action Flow Model for General Robot Control is authored by Kevin Black, Noah Brown, Danny Driess, Adnan Esmail, Michael Equi, Chelsea Finn, Niccolo Fusai, Lachy Groom, Karol Hausman, Brian Ichter, Szymon Jakubczak, Tim Jones, Liyiming Ke, Sergey Levine, Adrian Li-Bell, Mohith Mothukuri, Suraj Nair, Karl Pertsch, Lucy Xiaoyang Shi, James Tanner, Quan Vuong, Anna Walling, Haohuan Wang, and Ury Zhilinsky.

The paper was submitted on October 31, 2024, with the latest version (v3) revised on November 13, 2024.

**Key contributions:*
…[truncated 644 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 75 · 2026-05-29T06:37:33.909058+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2403.06764 \"An Image is Worth 1/2 Tokens After Layer 2\" FastV ECCV 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2403.06764 \"An Image is Worth 1/2 Tokens After Layer 2\" FastV ECCV 2024"
  }
}
```

</details>

---

### Tool call

_source line 76 · 2026-05-29T06:37:33.909288+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Cache \"Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" Xu Siyu 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Cache \"Efficient Vision-Language-Action Manipulation via Adaptive Token Caching\" Xu Siyu 2025"
  }
}
```

</details>

---

### Tool call

_source line 77 · 2026-05-29T06:37:33.909489+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2603.22991 VLA-IAP \"Training-Free Visual Token Pruning\" Cheng Jintao 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2603.22991 VLA-IAP \"Training-Free Visual Token Pruning\" Cheng Jintao 2026"
  }
}
```

</details>

---

### Tool call

_source line 78 · 2026-05-29T06:37:33.909682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DynamicViT \"Efficient Vision Transformers with Dynamic Token Sparsification\" Rao Yongming NeurIPS 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DynamicViT \"Efficient Vision Transformers with Dynamic Token Sparsification\" Rao Yongming NeurIPS 2021"
  }
}
```

</details>

---

### Tool result

_source line 79 · 2026-05-29T06:37:33.909889+00:00_

Web search results for query: "arXiv 2403.06764 "An Image is Worth 1/2 Tokens After Layer 2" FastV ECCV 2024"

Links: [{"title":"[2403.06764v1] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764v1"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240306764C/abstract"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"}]

I found the paper you're looking for! Here's what I found:

## Paper Overview

FastV is a versatile plug-and-play method designed to optimize computational efficiency by learning adaptive attention patterns in early layers and pruning visual tokens in subsequent ones.

## Key Results

FastV's ability dramatically reduces computational costs (e.g., a 45% reduction in FLOPs for LLaVA-1.5-13B) without sacrificing performance in a wide range
…[truncated 582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-29T06:37:33.910159+00:00_

Web search results for query: "DynamicViT "Efficient Vision Transformers with Dynamic Token Sparsification" Rao Yongming NeurIPS 2021"

Links: [{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://proceedings.neurips.cc/paper/2021/hash/747d3443e319a22747fbb873e8b2f9f2-Abstract.html"},{"title":"GitHub - raoyongming/DynamicViT: [NeurIPS 2021] [T-PAMI] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification · GitHub","url":"https://github.com/raoyongming/DynamicViT"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token   Sparsification","url":"https://arxiv.org/pdf/2106.02034"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210602034R/abstract"},{"title":"[2021 NeurIPS] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://velog.io/@hseop/DynamicViT-Efficient-Vision-Transformers-withDynamic-Token-Sparsification"},{"title":"[2106.02034] DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://arxiv.org/abs/2106.02034"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification","url":"https://www.researchgate.net/publication/352117557_DynamicViT_Efficient_Vision_Transformers_with_Dynamic_Token_Sparsification"},{"title":"DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification | OpenReview","url":"https://openreview.net/forum?id=kR95DuwwXHZ"},{"title":"Dynamic Spatial Sparsification for Efficient Vision Transformers and   Convolutional Neural Networks","url":"https://arxiv.org/pdf/2207.01580"},{"title":"DynamicViT: Efﬁcient Vision Transformers with Dynamic Token Sparsiﬁcation","url":"https://papers.neurips.cc/paper_files/paper/2021/file/747d3443e319a22747fbb873e8b2f9f2-Paper.pdf"}]

I found the paper! Here's a summary of the search results for DynamicViT:

## Paper Overview

…[truncated 1224 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-29T06:37:33.910431+00:00_

Web search results for query: "arXiv 2603.22991 VLA-IAP "Training-Free Visual Token Pruning" Cheng Jintao 2026"

Links: [{"title":"[2603.22991v1] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991v1"},{"title":"[2603.22991] VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22991"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.22991v1"},{"title":"VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2603.22991"},{"title":"History-Conditioned Spatio-Temporal Visual Token Pruning for Efficient Vision-Language Navigation","url":"https://arxiv.org/html/2603.06480"}]

I found the paper! Here's the information about arXiv 2603.22991:

**Title:** VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models

**Authors:** Jintao Cheng, Haozhe Wang, Weibin Li, Gang Wang, Yipu Zhang, Xiaoyu Tang, Jin Wu, Xieyuanli Chen, Yunhui Liu, Wei Zhang

**Submission Date:** March 24, 2026

**Overview:** Vision-Language-Action (VLA) models have rapidly advanced embodied intelligence, enabling robots to execute complex, instruction-driven tasks. However, as model capacity and visual context length grow, the inference cost of VLA systems becomes a major bottleneck for real-world deployment on resource-constrained platforms.

**Key Contribution:** The proposed training-free method, VLA-IAP (Interaction-Aligned Pruning), introduces a geometric prior mechanism to preserve structural anchors and a dynamic scheduling strategy that adapts pruning intensity based on semantic-motion alignment.

**Results:** VLA-IAP achieves a 97.8% success rate with a 1.25× speedup on the LIBERO benchmark, and up 
…[truncated 250 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 82 · 2026-05-29T06:37:33.910663+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 83 · 2026-05-29T06:37:33.910864+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 84 · 2026-05-29T06:37:33.911064+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 5",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. li2024cogact: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu and others. arXiv 2411.19650, year 2024.\n\n2. zheng2025xvla: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang and others. ICLR 2026, arXiv 2510.10274.\n\n3. lewis2020bart: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike and others. ACL 2020.\n\n4. ryoo2021tokenlearner: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. and others. NeurIPS 2021, arXiv 2106.11297.\n\n5. yin2022avit: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu and others. CVPR 2022, arXiv 2112.07658.\n\n6. meng2022adavit: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen and others. CVPR 2022, arXiv 2111.15668.\n\n7. chen2023sparsevit: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao and others. CVPR 2023, arXiv 2303.17605.\n\n8. ye2025fitprune: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao and others. AAAI 2025, arXiv 2409.10197.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 5",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. li2024cogact: \"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation\" by Li, Qixiu and others. arXiv 2411.19650, year 2024.\n\n2. zheng2025xvla: \"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" by Zheng, Jinliang and others. ICLR 2026, arXiv 2510.10274.\n\n3. lewis2020bart: \"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension\" by Lewis, Mike and others. ACL 2020.\n\n4. ryoo2021tokenlearner: \"TokenLearner: Adaptive Space-Time Tokenization for Videos\" by Ryoo, Michael S. and others. NeurIPS 2021, arXiv 2106.11297.\n\n5. yin2022avit: \"A-ViT: Adaptive Tokens for Efficient Vision Transformer\" by Yin, Hongxu and others. CVPR 2022, arXiv 2112.07658.\n\n6. meng2022adavit: \"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition\" by Meng, Lingchen and others. CVPR 2022, arXiv 2111.15668.\n\n7. chen2023sparsevit: \"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer\" by Chen, Xuanyao and others. CVPR 2023, arXiv 2303.17605.\n\n8. ye2025fitprune: \"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models\" by Ye, Weihao and others. AAAI 2025, arXiv 2409.10197.\n\nFor each, search on Google Scholar or Semantic Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool result

_source line 85 · 2026-05-29T06:37:33.911627+00:00_

Web search results for query: "Feng Yixu "See What Matters" "Differentiable Grid Sample Pruning" arXiv 2605.11817"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"ICML Poster See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://icml.cc/virtual/2026/poster/65010"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"Differentiable Mask for Pruning Convolutional and Recurrent Networks","url":"https://arxiv.org/pdf/1909.04567"},{"title":"Differentiable Network Pruning via Polarization of Probabilistic Channelwise Soft Masks","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9098282/"}]

I found the paper! Here's the information from the search results:

The paper "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" is by Yixu Feng and 6 other authors, with arXiv identifier 2605.11817.

**Key details about the research:**

Vision-Language-Action (VLA) models have shown promise in robotics manipulation, but existing token pruning methods suffer from a fundamental trade-off where aggressive compression discards critical geometric details like contact points, leading to performance degradation.

The paper proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.

**Results:**

By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression with fewer than 10% original visual tokens. Experiments on both LIBERO benchmark and a real robotic platform demonstrate that GridS achieves a 76% reduction in
…[truncated 192 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 86 · 2026-05-29T06:37:33.911911+00:00_

Web search results for query: "Zhang Yuan "SparseVLM" "Visual Token Sparsification" arXiv 2410.04417"

Links: [{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://app.apixacrm.com/index.php?q=https%3A%2F%2Farxiv.org%2Fabs%2F2410.04417"},{"title":"SparseVLM","url":"https://leofan90.github.io/SparseVLMs.github.io/"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004417Z/abstract"},{"title":"GitHub - Theia-4869/SparseVLM","url":"https://github.com/Theia-4869/SparseVLM"},{"title":"(PDF) SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://www.researchgate.net/publication/384698552_SparseVLM_Visual_Token_Sparsification_for_Efficient_Vision-Language_Model_Inference"},{"title":"Paper page - SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://huggingface.co/papers/2410.04417"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417v4"},{"title":"Panasonic HD develops “SparseVLM” technology that doubles the processing speed of Vision-Language Models | Innovations/Technologies | Company | Press Releases | Panasonic Newsroom Global","url":"https://news.panasonic.com/global/zh-CHS/press/en250704-2"}]

Great! I found detailed information about this paper. Here's a summary of the search results:

## SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference

The paper is authored by Yuan Zhang and 10 other collaborators including Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, an
…[truncated 1188 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 87 · 2026-05-29T06:37:33.912178+00:00_

Web search results for query: "Khaki Samir "SparseVILA" "Decoupled Visual Sparsity" arXiv 2510.17777"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777"},{"title":"[Literature Review] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://www.themoonlight.io/en/review/sparsevila-decoupling-visual-sparsity-for-efficient-vlm-inference"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efﬁcient VLM Inference Samir Khaki4","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Khaki_SparseVILA_Decoupling_Visual_Sparsity_for_Efficient_VLM_Inference_ICCV_2025_paper.pdf"},{"title":"SparseVILA-R1: Decoupling Visual Sparsity for Efficient VLM Reasoning","url":"https://openreview.net/pdf/6597aa03e44118e07d8bbbe91433da250c6beb33.pdf"}]

I found the paper you were searching for. Here's what I found:

SparseVILA presents a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding.

The paper is authored by Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos N. Plataniotis, Yao Lu, Song Han, and Zhijian Liu, representing affiliations at NVIDIA, MIT, UC San Diego, and the University of Toronto.

This decoupled design matches leading prefill pruning methods while preserving multi-turn fidelity by retaining most of the visual ca
…[truncated 476 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 88 · 2026-05-29T06:37:33.912436+00:00_

Web search results for query: "Jabbour Jason "Don't Run with Scissors" "Pruning Breaks VLA" arXiv 2510.08464"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/pdf/2510.08464"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://gluestick-vla.github.io/"},{"title":"VLN-CE-Isaac Benchmark | Download Scientific Diagram","url":"https://www.researchgate.net/figure/LN-CE-Isaac-Benchmark_fig2_386502820"}]

I found the paper! Here's what I discovered:

The paper "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" is authored by Jason Jabbour, Dong-Ki Kim, Max Smith, Jay Patrikar, Radhika Ghosal, Youhui Wang, Ali Agha, Vijay Janapa Reddi, and Shayegan Omidshafiei, with affiliations at FieldAI and Harvard University.

**Key findings:**

Pruning VLA models leads to drastic degradation and increased safety violations. For example, Open-VLA and NaVILA dropped to 0% success rate when pruned, while unsafe-episode rates increased from 33.4% to 51.6% for OpenVLA and from 23.0% to 100.0% for NaVILA.

**The solution:**

The authors introduce GLUESTICK, a post-pruning recovery method that restores much of the original model's functionality while retaining sparsity benefits by performing a one-time interpolation between the dense and pruned models in weight-space to compute a corrective term, which is then used during inference.

GLUESTICK achieves competitive memory efficiency while substantially recovering success rates and reducing safety violations across diverse VLA architectures and tasks in manipulation and navigation.


REMINDER: You MUST i
…[truncated 80 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 89 · 2026-05-29T06:37:33.912668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.18950 authors Gao Ye Zhang Qian Compressor-VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.18950 authors Gao Ye Zhang Qian Compressor-VLA"
  }
}
```

</details>

---

### Tool call

_source line 90 · 2026-05-29T06:37:33.912865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2509.05614 authors full list SpecPrune-VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2509.05614 authors full list SpecPrune-VLA"
  }
}
```

</details>

---

### Tool call

_source line 91 · 2026-05-29T06:37:33.913052+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseVLM Zhang Yuan ICML 2025 venue accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseVLM Zhang Yuan ICML 2025 venue accepted"
  }
}
```

</details>

---

### Tool call

_source line 92 · 2026-05-29T06:37:33.913320+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LightVLA ICRA 2026 accepted Jiang Titong authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LightVLA ICRA 2026 accepted Jiang Titong authors"
  }
}
```

</details>

---

### Tool call

_source line 93 · 2026-05-29T06:37:33.913533+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0.5 Vision-Language-Action Model Open-World Generalization Black Kevin arXiv 2504.16054 CoRL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0.5 Vision-Language-Action Model Open-World Generalization Black Kevin arXiv 2504.16054 CoRL 2025"
  }
}
```

</details>

---

### Tool call

_source line 94 · 2026-05-29T06:37:33.913727+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Octo Open-Source Generalist Robot Policy Ghosh Dibya RSS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Octo Open-Source Generalist Robot Policy Ghosh Dibya RSS 2024"
  }
}
```

</details>

---

### Tool call

_source line 95 · 2026-05-29T06:37:33.913911+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-1 Robotics Transformer Real-World Control Scale Brohan RSS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-1 Robotics Transformer Real-World Control Scale Brohan RSS 2023"
  }
}
```

</details>

---

### Tool call

_source line 96 · 2026-05-29T06:37:33.914104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fine-Tuning Vision-Language-Action Models Optimizing Speed Success Kim Moo Jin arXiv 2502.19645"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fine-Tuning Vision-Language-Action Models Optimizing Speed Success Kim Moo Jin arXiv 2502.19645"
  }
}
```

</details>

---

### Tool result

_source line 97 · 2026-05-29T06:37:33.914373+00:00_

Web search results for query: "pi0.5 Vision-Language-Action Model Open-World Generalization Black Kevin arXiv 2504.16054 CoRL 2025"

Links: [{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"},{"title":"[2504.16054v1] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054v1"},{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"π0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/pdf/2504.16054"},{"title":"[PDF] π0.5: a Vision-Language-Action Model with Open-World Generalization | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%800.5:-a-Vision-Language-Action-Model-with-Intelligence-Black/1e2a82ef5e0325a26ca0344c4f8c256c52fae7ec"},{"title":"(PDF) \\pi_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://www.researchgate.net/publication/391019295_pi_05_a_Vision-Language-Action_Model_with_Open-World_Generalization"},{"title":"$π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250416054I/abstract"},{"title":"A review of π0.5 — Scaling Open-World Generalization in Vision-Language-Action Models | by Isaac Edelman | Toward Humanoids | Medium","url":"https://medium.com/correll-lab/a-review-of-%CF%800-5-scaling-open-world-generalization-in-vision-language-action-models-e4cb0d74264e"},{"title":"𝜋_0.5: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/html/2504.16054v1"}]

I found the paper you were searching for. Here are the results:

The paper π₀.₅: a Vision-Language-Action Model with Open-World Generalization was submitted to arXiv on April 22, 2025, with authors from Physical Intelligence including Kevin Black, Noah Brown, 
…[truncated 894 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 98 · 2026-05-29T06:37:33.914636+00:00_

Web search results for query: "Octo Open-Source Generalist Robot Policy Ghosh Dibya RSS 2024"

Links: [{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://arxiv.org/pdf/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy Octo Model Team Dibya Ghosh∗,1","url":"https://openreview.net/pdf/e2dabc0a3fd32239dcab07d7bcfa1fae085f49b0.pdf"},{"title":"[PDF] Octo: An Open-Source Generalist Robot Policy | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Octo:-An-Open-Source-Generalist-Robot-Policy-Team-Ghosh/1d2753d74025e7a71594506623be81f18b073adb"},{"title":"Octo: An Open-Source Generalist Robot Policy | Request PDF","url":"https://www.researchgate.net/publication/383897130_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"[2405.12213] Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/abs/2405.12213"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://octo-models.github.io/"},{"title":"(PDF) Octo: An Open-Source Generalist Robot Policy","url":"https://www.researchgate.net/publication/380730391_Octo_An_Open-Source_Generalist_Robot_Policy"},{"title":"Octo: An Open-Source Generalist Robot Policy","url":"https://arxiv.org/html/2405.12213v1"},{"title":"GitHub - octo-models/octo: Octo is a transformer-based robot policy trained on a diverse mix of 800k robot trajectories. · GitHub","url":"https://github.com/octo-models/octo"}]

Based on the search results, here's what I found:

## Octo: An Open-Source Generalist Robot Policy

Octo is an open-source, generalist policy for robotic manipulation that is a transformer-based policy pretrained on 800k diverse robot episodes from the Open X-Embodiment dataset. It supports flexible task and observation definitions and can be quickly finetuned.

**Publication Details:**
The paper was published in Robotics: Science and Systems in May 2024, with Dibya Ghosh as one of the lead authors from the Octo Model Team.

**Key Fe
…[truncated 484 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 99 · 2026-05-29T06:37:33.914897+00:00_

Web search results for query: "Fine-Tuning Vision-Language-Action Models Optimizing Speed Success Kim Moo Jin arXiv 2502.19645"

Links: [{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"[2502.19645v1] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645v1"},{"title":"[Revue de papier] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/fr/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success | alphaXiv","url":"https://www.alphaxiv.org/resources/2502.19645v1"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"(PDF) Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.researchgate.net/publication/389399234_Fine-Tuning_Vision-Language-Action_Models_Optimizing_Speed_and_Success"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/html/2502.19645v2"}]

I found the paper you're looking for! Here's what the search results show:

## Paper Overview

The paper "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" by Moo Jin Kim and 2 other authors (Chelsea Finn and Percy Liang) addresses how vision-language-action models (VLAs) build upon pretrained vision-language models and leverage diverse robot datasets.

## Key Problem and Solution

Despite VLAs' successes, they struggle with novel robot setups and require fine-tuning to achieve good performance. The authors study key VLA adaptation design ch
…[truncated 866 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 100 · 2026-05-29T06:37:33.915168+00:00_

Web search results for query: "RT-1 Robotics Transformer Real-World Control Scale Brohan RSS 2023"

Links: [{"title":"RT-1: Robotics Transformer for Real-World Control at Scale - R Discovery","url":"https://discovery.researcher.life/article/rt-1-robotics-transformer-for-real-world-control-at-scale/a5a1b925066134a18933ad552f843acf?page=5"},{"title":"(PDF) RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://www.researchgate.net/publication/372803068_RT-1_Robotics_Transformer_for_Real-World_Control_at_Scale"},{"title":"[2212.06817v2] RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/abs/2212.06817v2"},{"title":"dblp: RT-1: Robotics Transformer for Real-World Control at Scale.","url":"https://dblp.org/rec/conf/rss/BrohanBCCDFGHHH23.html"},{"title":"[2212.06817] RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/abs/2212.06817"},{"title":"[PDF] RT-1: Robotics Transformer for Real-World Control at Scale | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-1:-Robotics-Transformer-for-Real-World-Control-Brohan-Brown/fd1cf28a2b8caf2fe29af5e7fa9191cecfedf84d"},{"title":"RT-1: Robotics Transformer for real-world control at scale","url":"https://research.google/blog/rt-1-robotics-transformer-for-real-world-control-at-scale/"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://arxiv.org/pdf/2212.06817"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale","url":"https://www.roboticsproceedings.org/rss19/p025.pdf"},{"title":"RT-1: Robotics Transformer for Real-World Control at Scale · Robotics: Science and Systems","url":"https://rss2023.github.io/rss2023-website/program/papers/025/"}]

I found comprehensive search results for the RT-1 Robotics Transformer paper. Here's what I found:

RT-1: Robotics Transformer for Real-World Control at Scale was presented at Robotics: Science and Systems 2023 by Anthony Brohan, Noah Brown, 
…[truncated 911 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 101 · 2026-05-29T06:37:33.915436+00:00_

Web search results for query: "VLA-Cache "Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" Xu Siyu 2025"

Links: [{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://vla-cache.github.io/"},{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"NeurIPS Poster VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118121"},{"title":"[PDF] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | Semantic Scholar","url":"https://www.semanticscholar.org/paper/VLA-Cache:-Efficient-Vision-Language-Action-via-Xu-Wang/0909365e230474cc372abd04ca5206f6478377b3"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175v2"},{"title":"Paper page - VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://huggingface.co/papers/2502.02175"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching | OpenReview","url":"https://openreview.net/forum?id=QZYZ0Xm58q"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/pdf/2502.02175"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"}]

I found comprehensive information about VLA-Cache. Here's what the research reveals:

## Overview

VLA-Cache: Efficient Vision-Language-Action Manipulation
…[truncated 1429 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool call

_source line 102 · 2026-05-29T06:37:33.915668+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Token Merging: Your ViT But Faster\" Bolya Daniel ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Token Merging: Your ViT But Faster\" Bolya Daniel ICLR 2023"
  }
}
```

</details>

---

### Tool call

_source line 103 · 2026-05-29T06:37:33.915872+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Not All Patches are What You Need\" EViT Liang Youwei ICLR 2022 token reorganization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Not All Patches are What You Need\" EViT Liang Youwei ICLR 2022 token reorganization"
  }
}
```

</details>

---

### Tool call

_source line 104 · 2026-05-29T06:37:33.916065+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LIBERO \"Benchmarking Knowledge Transfer for Lifelong Robot Learning\" Liu Bo NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LIBERO \"Benchmarking Knowledge Transfer for Lifelong Robot Learning\" Liu Bo NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 105 · 2026-05-29T06:37:33.916283+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2506.10100 EfficientVLA \"Training-Free Acceleration and Compression\" Yang Yantai 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2506.10100 EfficientVLA \"Training-Free Acceleration and Compression\" Yang Yantai 2025"
  }
}
```

</details>

---

### Tool call

_source line 106 · 2026-05-29T06:37:33.916477+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Pruner Temporal-Aware Dual-Level Visual Token Pruning arXiv 2511.16449"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Pruner Temporal-Aware Dual-Level Visual Token Pruning arXiv 2511.16449"
  }
}
```

</details>

---

### Tool call

_source line 107 · 2026-05-29T06:37:33.916669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaVA-PruMerge Adaptive Token Reduction Efficient Large Multimodal Models Shang Yuzhang"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaVA-PruMerge Adaptive Token Reduction Efficient Large Multimodal Models Shang Yuzhang"
  }
}
```

</details>

---

### Tool call

_source line 108 · 2026-05-29T06:37:33.916860+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Visual Instruction Tuning\" Liu Haotian NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Visual Instruction Tuning\" Liu Haotian NeurIPS 2023"
  }
}
```

</details>

---

### Tool call

_source line 109 · 2026-05-29T06:37:33.917046+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" Shi Wenzhe CVPR 2016"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network\" Shi Wenzhe CVPR 2016"
  }
}
```

</details>

---

### Tool result

_source line 110 · 2026-05-29T06:37:33.917278+00:00_

Web search results for query: "VLA-Pruner Temporal-Aware Dual-Level Visual Token Pruning arXiv 2511.16449"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v3"},{"title":"Environment-Aware Adaptive Pruning with Interleaved Inference Orchestration for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.00780"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/pdf/2509.05614"}]

I found the paper! Here's what I found about VLA-Pruner:

Vision-Language-Action (VLA) models have shown great promise for embodied AI, yet the heavy computational cost of processing continuous visual streams severely limits their real-time deployment. 

VLA-Pruner is a plug-and-play VLA token pruning method that aligns with the dual-system nature of VLA models and exploits temporal continuity in robot manipulation. It introduces a dual-objective importance criterion for token retention: vision-language prefill attention for semantic relevance and action decode attention, estimated via temporal smoothing, for execution precision.

VLA-Pruner proposes a dual-level token selection strategy that adaptively preserves a compact set of visual tokens for both semantic understanding and action execution under given compute budget.

Experiments show that VLA-Pruner outperforms state-of-the-art approaches across multiple VLA architectures, achieving up to 1.99× speedup with comparable manipulation quality.

The paper was posted on arXiv on February 11, 2026, and the
…[truncated 178 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 111 · 2026-05-29T06:37:33.917537+00:00_

Web search results for query: "LLaVA-PruMerge Adaptive Token Reduction Efficient Large Multimodal Models Shang Yuzhang"

Links: [{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge","url":"https://llava-prumerge.github.io/"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models - Paper Detail","url":"https://deeplearn.org/arxiv/477540/llava-prumerge:-adaptive-token-reduction-for-efficient-large-multimodal-models"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.html"},{"title":"GitHub - 42Shawn/LLaVA-PruMerge: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models · GitHub","url":"https://github.com/42Shawn/LLaVA-PruMerge"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://www.openaccess.thecvf.com/content/ICCV2025/papers/Shang_LLaVA-PruMerge_Adaptive_Token_Reduction_for_Efficient_Large_Multimodal_Models_ICCV_2025_paper.pdf"}]

Based on the search results, here's what I found about LLaVA-PruMerge:

## Overview

LLaVA-PruMerge is a method for effici
…[truncated 1362 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 112 · 2026-05-29T06:37:33.917781+00:00_

Web search results for query: ""Visual Instruction Tuning" Liu Haotian NeurIPS 2023"

Links: [{"title":"Visual Instruction Tuning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"},{"title":"Visual instruction tuning | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/abs/10.5555/3666122.3667638"},{"title":"GitHub - haotian-liu/LLaVA: [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. · GitHub","url":"https://github.com/haotian-liu/llava"},{"title":"Visual Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=w0H2xGHlkw"},{"title":"LLaVA","url":"https://llava-vl.github.io/"},{"title":"Visual Instruction Tuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230408485L/abstract"},{"title":"Less is More: High-value Data Selection for Visual Instruction Tuning","url":"https://arxiv.org/pdf/2403.09559"}]

Based on the search results, here's what I found about "Visual Instruction Tuning" by Liu Haotian at NeurIPS 2023:

## Paper Overview

The paper "Visual Instruction Tuning" was authored by Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee, and presented at the 37th Conference on Neural Information Processing Systems (NeurIPS 2023).

## Main Contribution

The paper presents visual instruction-tuning, the first attempt to extend instruction-tuning to the language-image multimodal space, to pave the way towards building a general-purpose visual assistant.

## Key Methodology

The authors present the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data. Through instruction tuning on such generated data, they introduce LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understand
…[truncated 500 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 113 · 2026-05-29T06:37:33.918026+00:00_

Web search results for query: ""Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network" Shi Wenzhe CVPR 2016"

Links: [{"title":"CVPR 2016 Open Access Repository","url":"https://www.cv-foundation.org/openaccess/content_cvpr_2016/html/Shi_Real-Time_Single_Image_CVPR_2016_paper.html"},{"title":"[1609.05158] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/abs/1609.05158"},{"title":"dblp: Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network.","url":"https://dblp.org/rec/conf/cvpr/ShiCHTABRW16.html"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network [Quick Review]","url":"https://liner.com/review/realtime-single-image-and-video-superresolution-using-efficient-subpixel-convolutional"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network - Technical University of Munich","url":"https://portal.fis.tum.de/en/publications/real-time-single-image-and-video-super-resolution-using-an-effici/"},{"title":"(PDF) Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network (2016) | Wenzhe Shi | 7465 Citations","url":"https://scispace.com/papers/real-time-single-image-and-video-super-resolution-using-an-4ljje8ipch"},{"title":"[PDF] Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Real-Time-Single-Image-and-Video-Super-Resolution-Shi-Caballero/03a5b2aac53443e6078f0f63b35d4f95d6d54c5d"},{"title":"Real-Time Single Image and Video Super-Resolution Using an Efficient   Sub-Pixel Convolutional Neural Network","url":"https://arxiv.org/pdf/1609.05158"}]

I found the paper you're searching for! Here are t
…[truncated 1281 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 114 · 2026-05-29T06:37:33.918280+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 115 · 2026-05-29T06:37:33.918493+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 116 · 2026-05-29T06:37:33.918682+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation arXiv 2411.19650"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation arXiv 2411.19650"
  }
}
```

</details>

---

### Tool call

_source line 117 · 2026-05-29T06:37:33.918883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model arXiv 2510.10274"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model arXiv 2510.10274"
  }
}
```

</details>

---

### Tool call

_source line 118 · 2026-05-29T06:37:33.919077+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation Translation and Comprehension Lewis ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation Translation and Comprehension Lewis ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 119 · 2026-05-29T06:37:33.919296+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TokenLearner: Adaptive Space-Time Tokenization for Videos Ryoo NeurIPS 2021 arXiv 2106.11297"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TokenLearner: Adaptive Space-Time Tokenization for Videos Ryoo NeurIPS 2021 arXiv 2106.11297"
  }
}
```

</details>

---

### Tool call

_source line 120 · 2026-05-29T06:37:33.919488+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "A-ViT: Adaptive Tokens for Efficient Vision Transformer Yin CVPR 2022 arXiv 2112.07658"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "A-ViT: Adaptive Tokens for Efficient Vision Transformer Yin CVPR 2022 arXiv 2112.07658"
  }
}
```

</details>

---

### Tool call

_source line 121 · 2026-05-29T06:37:33.919678+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition Meng CVPR 2022 arXiv 2111.15668"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition Meng CVPR 2022 arXiv 2111.15668"
  }
}
```

</details>

---

### Tool call

_source line 122 · 2026-05-29T06:37:33.919869+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer Chen CVPR 2023 arXiv 2303.17605"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer Chen CVPR 2023 arXiv 2303.17605"
  }
}
```

</details>

---

### Tool call

_source line 123 · 2026-05-29T06:37:33.920056+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models Ye AAAI 2025 arXiv 2409.10197"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models Ye AAAI 2025 arXiv 2409.10197"
  }
}
```

</details>

---

### Tool result

_source line 124 · 2026-05-29T06:37:33.920301+00:00_

Web search results for query: "TokenLearner: Adaptive Space-Time Tokenization for Videos Ryoo NeurIPS 2021 arXiv 2106.11297"

Links: [{"title":"TokenLearner: Adaptive Space-Time Tokenization for Videos","url":"https://proceedings.neurips.cc/paper/2021/hash/6a30e32e56fce5cf381895dfe6ca7b6f-Abstract.html"},{"title":"TokenLearner: Adaptive Space-Time Tokenization for Videos","url":"https://research.google/pubs/tokenlearner-adaptive-space-time-tokenization-for-videos/"},{"title":"scenic/scenic/projects/token_learner at main · google-research/scenic","url":"https://github.com/google-research/scenic/tree/main/scenic/projects/token_learner"},{"title":"[PDF] TokenLearner: Adaptive Space-Time Tokenization for Videos | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TokenLearner:-Adaptive-Space-Time-Tokenization-for-Ryoo-Piergiovanni/eaa09c607780373cc809bce89b6b28b17e301f27"},{"title":"GitHub - ariG23498/TokenLearner: TensorFlow implementation of \"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"","url":"https://github.com/ariG23498/TokenLearner"},{"title":"TokenLearner: adaptive space-time tokenization for videos","url":"https://dl.acm.org/doi/10.5555/3540261.3541240"},{"title":"1 TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://arxiv.org/pdf/2106.11297"},{"title":"TokenLearner: Adaptive Space-Time Tokenization for Videos","url":"https://openreview.net/pdf?id=z-l1kpDXs88"},{"title":"NeurIPS Poster TokenLearner: Adaptive Space-Time Tokenization for Videos","url":"https://neurips.cc/virtual/2021/poster/26578"}]

Based on the search results, here's information about the TokenLearner paper:

## Overview

TokenLearner introduces a novel visual representation learning which relies on a handful of adaptively learned tokens, and which is applicable to both image and video understanding tasks. The paper was published as part of Advances in Neural Information Processing Systems 34 (NeurIPS 2021) by Michael Ryoo, AJ Pie
…[truncated 1072 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 125 · 2026-05-29T06:37:33.920566+00:00_

Web search results for query: "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation arXiv 2411.19650"

Links: [{"title":"[2411.19650v1] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650v1"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"CogACT/CogACT-Large · Hugging Face","url":"https://huggingface.co/CogACT/CogACT-Large"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241119650L/abstract"},{"title":"dblp: CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation.","url":"https://dblp.org/rec/journals/corr/abs-2411-19650.html"}]

I found the paper! Here's what I found about CogACT (arXiv 2411.19650):

**Overview:**
The advancement of large Vision-Language-Action (VLA) models has significantly improved robotic manipulation in terms of lan
…[truncated 1519 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 126 · 2026-05-29T06:37:33.920815+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Verify bib entries group 6",
  "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shi2024crossget: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan and others. ICML 2024, arXiv 2305.17455.\n\n2. oquab2023dinov2 / oquab2024dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime and others. Listed as Transactions on Machine Learning Research (TMLR). Bib has two entries: one with key oquab2023dinov2 (year=2024) and one oquab2024dinov2 (year=2024, arXiv 2304.07193). Check which year is correct and if TMLR is the correct venue.\n\n3. su2024roformer: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin and others. Neurocomputing, volume 568, pages 127063, year 2024.\n\n4. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n5. li2024roboflamingo: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang and others. ICLR 2024, arXiv 2311.01378.\n\n6. alayrac2022flamingo: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste and others. NeurIPS 2022.\n\n7. jaegle2021perceiver: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew and others. ICML 2021.\n\n8. zitkovich2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others. CoRL 2023, arXiv 2307.15818. NOTE: There's also a brohan2023rt2 entry with Brohan, Anthony as first author. Check which author list is correct for RT-2.\n\n9. openxembodiment2024: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n10. zhang2023h2o: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu and others. NeurIPS 2023, arXiv 2306.14048.\n\n11. xiao2024streamingllm: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan and others. ICLR 2024, arXiv 2309.17453.\n\n12. mees2022calvin: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier and others. IEEE Robotics and Automation Letters, year 2022, arXiv 2112.03227.\n\n13. chi2023diffusionpolicy: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng and others. RSS 2023, arXiv 2303.04137.\n\n14. zeng2023transformers_tsf: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing and others. AAAI 2023, arXiv 2205.13504.\n\n15. bouthillier2024negative: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier and others. ICML 2024, arXiv 2406.03980.\n\nFor each, search on Google Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "tool_args": {
    "description": "Verify bib entries group 6",
    "prompt": "You are verifying academic references for a paper. For each entry below, use WebSearch to verify: (1) paper exists, (2) authors correct, (3) title exact, (4) year correct, (5) venue correct, (6) arXiv ID correct if given. Return a structured checklist.\n\nEntries to verify:\n\n1. shi2024crossget: \"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers\" by Shi, Dachuan and others. ICML 2024, arXiv 2305.17455.\n\n2. oquab2023dinov2 / oquab2024dinov2: \"DINOv2: Learning Robust Visual Features without Supervision\" by Oquab, Maxime and others. Listed as Transactions on Machine Learning Research (TMLR). Bib has two entries: one with key oquab2023dinov2 (year=2024) and one oquab2024dinov2 (year=2024, arXiv 2304.07193). Check which year is correct and if TMLR is the correct venue.\n\n3. su2024roformer: \"RoFormer: Enhanced Transformer with Rotary Position Embedding\" by Su, Jianlin and others. Neurocomputing, volume 568, pages 127063, year 2024.\n\n4. abnar2020quantifying: \"Quantifying Attention Flow in Transformers\" by Abnar, Samira and Zuidema, Willem. ACL 2020, pages 4190-4197.\n\n5. li2024roboflamingo: \"Vision-Language Foundation Models as Effective Robot Imitators\" by Li, Xinghang and others. ICLR 2024, arXiv 2311.01378.\n\n6. alayrac2022flamingo: \"Flamingo: a Visual Language Model for Few-Shot Learning\" by Alayrac, Jean-Baptiste and others. NeurIPS 2022.\n\n7. jaegle2021perceiver: \"Perceiver: General Perception with Iterative Attention\" by Jaegle, Andrew and others. ICML 2021.\n\n8. zitkovich2023rt2: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\" by Zitkovich, Brianna and Yu, Tianhe and Xu, Sichun and others. CoRL 2023, arXiv 2307.15818. NOTE: There's also a brohan2023rt2 entry with Brohan, Anthony as first author. Check which author list is correct for RT-2.\n\n9. openxembodiment2024: \"Open X-Embodiment: Robotic Learning Datasets and RT-X Models\" by Open X-Embodiment Collaboration. ICRA 2024, arXiv 2310.08864.\n\n10. zhang2023h2o: \"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models\" by Zhang, Zhenyu and others. NeurIPS 2023, arXiv 2306.14048.\n\n11. xiao2024streamingllm: \"Efficient Streaming Language Models with Attention Sinks\" by Xiao, Guangxuan and others. ICLR 2024, arXiv 2309.17453.\n\n12. mees2022calvin: \"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks\" by Mees, Oier and others. IEEE Robotics and Automation Letters, year 2022, arXiv 2112.03227.\n\n13. chi2023diffusionpolicy: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\" by Chi, Cheng and others. RSS 2023, arXiv 2303.04137.\n\n14. zeng2023transformers_tsf: \"Are Transformers Effective for Time Series Forecasting?\" by Zeng, Ailing and others. AAAI 2023, arXiv 2205.13504.\n\n15. bouthillier2024negative: \"Position: Embracing Negative Results in Machine Learning\" by Bouthillier, Xavier and others. ICML 2024, arXiv 2406.03980.\n\nFor each, search on Google Scholar or arXiv. Report: exists (yes/no), author match, title match, year match, venue match, arXiv ID match, and any issues found."
  }
}
```

</details>

---

### Tool result

_source line 127 · 2026-05-29T06:37:33.921119+00:00_

Web search results for query: "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation Translation and Comprehension Lewis ACL 2020"

Links: [{"title":"BART- Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension","url":"https://hyunyoung2.github.io//2021/01/21/BART/"},{"title":"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.703/"},{"title":"BART: Denoising sequence-to-sequence pre-training for natural language generation, translation, and comprehension - Tel Aviv University","url":"https://cris.tau.ac.il/en/publications/bart-denoising-sequence-to-sequence-pre-training-for-natural-lang-2"},{"title":"(PDF) BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension (2020) | Michael Lewis | 11177 Citations","url":"https://scispace.com/papers/bart-denoising-sequence-to-sequence-pre-training-for-natural-24rhunb8w5"},{"title":"[PDF] BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BART:-Denoising-Sequence-to-Sequence-Pre-training-Lewis-Liu/395de0bd3837fdf4b4b5e5f04835bcc69c279481"},{"title":"Multilingual Denoising Pre-training for Neural Machine Translation - ACL Anthology","url":"https://aclanthology.org/2020.tacl-1.47/"},{"title":"BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension | Request PDF","url":"https://www.researchgate.net/publication/343301801_BART_Denoising_Sequence-to-Sequence_Pre-training_for_Natural_Language_Generation_Translation_and_Comprehension"}]

I found the paper you're looking for. Here's what I can tell you about it:

The paper "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language G
…[truncated 1226 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 128 · 2026-05-29T06:37:33.921409+00:00_

Web search results for query: ""Token Merging: Your ViT But Faster" Bolya Daniel ICLR 2023"

Links: [{"title":"Token Merging: Your ViT but Faster","url":"https://github.com/facebookresearch/ToMe"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv-export1.library.cornell.edu/abs/2210.09461"},{"title":"Published as a conference paper at ICLR 2023 TOKEN MERGING: YOUR VIT BUT FASTER","url":"https://arxiv.org/pdf/2210.09461"},{"title":"CubistMerge: Spatial-Preserving Token Merging For Diverse ViT Backbones","url":"https://arxiv.org/html/2509.21764v1"},{"title":"[2210.09461] Token Merging: Your ViT But Faster","url":"https://arxiv.org/abs/2210.09461"},{"title":"(PDF) Token Merging: Your ViT But Faster","url":"https://www.researchgate.net/publication/364431397_Token_Merging_Your_ViT_But_Faster"},{"title":"Training-Free Acceleration of ViTs with Delayed Spatial Merging","url":"https://arxiv.org/pdf/2303.02331"}]

I found comprehensive information about the paper "Token Merging: Your ViT but Faster" by Daniel Bolya and colleagues. Here are the key details:

## Paper Overview

The paper "Token Merging: Your ViT but Faster" was published at ICLR 2023 and authored by Daniel Bolya, Cheng-Yang Fu, Xiaoliang Dai, Peizhao Zhang, Christoph Feichtenhofer, and Judy Hoffman from Georgia Tech and Meta AI.

## Main Contribution

Token Merging (ToMe) is a simple method to increase the throughput of existing ViT models without needing to train. ToMe gradually combines similar tokens in a transformer using a general and light-weight matching algorithm that is as fast as pruning while being more accurate.

## Performance Results

Off-the-shelf, ToMe can 2× the throughput of state-of-the-art ViT-L @ 512 and ViT-H @ 518 models on images and 2.2× the throughput of ViT-L on video with only a 0.2-0.3% accuracy drop in each case. ToMe can also easily be applied during training, improving in practice training speed up to 2x for MAE fine-tuning on video.

## Key Differe
…[truncated 518 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 129 · 2026-05-29T06:37:33.921662+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "BLIP-2 Bootstrapping Language-Image Pre-Training Frozen Image Encoders Li Junnan ICML 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "BLIP-2 Bootstrapping Language-Image Pre-Training Frozen Image Encoders Li Junnan ICML 2023"
  }
}
```

</details>

---

### Tool result

_source line 130 · 2026-05-29T06:37:33.921887+00:00_

Web search results for query: "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model arXiv 2510.10274"

Links: [{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2510.10274"},{"title":"2toINF/X-VLA-Pt · Hugging Face","url":"https://huggingface.co/2toINF/X-VLA-Pt"},{"title":"X-VLA","url":"https://thu-air-dream.github.io/X-VLA/"},{"title":"Cross-Hand Latent Representation for Vision-Language-Action Models","url":"https://arxiv.org/html/2603.10158v1"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/html/2510.10274v1"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"}]

I found the paper! Here's what I found about X-VLA:

## Overview

X-VLA focuses on building generalist Vision-Language-Action (VLA) models that rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets.

## Key Approach

The authors propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective 
…[truncated 776 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 131 · 2026-05-29T06:37:33.922163+00:00_

Web search results for query: "LIBERO "Benchmarking Knowledge Transfer for Lifelong Robot Learning" Liu Bo NeurIPS 2023"

Links: [{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning [Quick Review]","url":"https://liner.com/review/libero-benchmarking-knowledge-transfer-for-lifelong-robot-learning"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2023/12/10/liu-neurips23-libero/"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning – Sony AI","url":"https://ai.sony/publications/LIBERO-Benchmarking-Knowledge-Transfer-for-Lifelong-Robot-Learning/"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/pdf/2306.03310"},{"title":"Peter Stone: LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-liu_zhu_NeurIPS2023.html"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"}]

I found comprehensive information about this paper. Here's what I found:

LIBERO is a novel benchmark of lifelong learning for robot manipulation des
…[truncated 1308 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 132 · 2026-05-29T06:37:33.922440+00:00_

Web search results for query: ""Not All Patches are What You Need" EViT Liang Youwei ICLR 2022 token reorganization"

Links: [{"title":"Efficient Vision Transformers via Token Reorganizations","url":"https://www.emergentmind.com/papers/2202.07800"},{"title":"GitHub - youweiliang/evit: Python code for ICLR 2022 spotlight paper EViT: Expediting Vision Transformers via Token Reorganizations · GitHub","url":"https://github.com/youweiliang/evit"},{"title":"Published as a conference paper at ICLR 2022 NOT ALL PATCHES ARE WHAT YOU NEED:","url":"https://openreview.net/pdf?id=BjyvwnXXVn_"},{"title":"Youwei Liang - Homepage","url":"https://youweiliang.github.io/"},{"title":"(PDF) Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://www.researchgate.net/publication/358655949_Not_All_Patches_are_What_You_Need_Expediting_Vision_Transformers_via_Token_Reorganizations"},{"title":"Not All Patches are What You Need: Expediting Vision Transformers via   Token Reorganizations","url":"https://arxiv.org/pdf/2202.07800"},{"title":"ICLR Poster EViT: Expediting Vision Transformers via Token Reorganizations","url":"https://iclr.cc/virtual/2022/poster/6168"},{"title":"Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations | DeepAI","url":"https://deepai.org/publication/not-all-patches-are-what-you-need-expediting-vision-transformers-via-token-reorganizations"},{"title":"[2202.07800v1] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://arxiv.org/abs/2202.07800v1"},{"title":"[2202.07800] Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations","url":"https://arxiv.org/abs/2202.07800"}]

I found the paper you're looking for! The paper "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" is by Youwei Liang, Chongjian Ge, Zhan Tong, Yibing Song, Jue Wang, and Pengtao Xie, pu
…[truncated 1120 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 133 · 2026-05-29T06:37:33.922686+00:00_

Web search results for query: "arxiv 2509.05614 authors full list SpecPrune-VLA"

Links: [{"title":"[2509.05614] SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/abs/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning","url":"https://arxiv.org/html/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware","url":"https://arxiv.org/pdf/2509.05614"},{"title":"SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning | Request PDF","url":"https://www.researchgate.net/publication/395354566_SpecPrune-VLA_Accelerating_Vision-Language-Action_Models_via_Action-Aware_Self-Speculative_Pruning"},{"title":"Specprune-vla Boosts Vision-Language-Action Models, Avoiding Over 20% Success Rate Drops With Smart Pruning","url":"https://quantumzeitgeist.com/faster-models-performance-specprune-vla-boosts-vision-language-action-avoiding-success/"},{"title":"SPECPRUNE-VLA:","url":"https://openreview.net/pdf/f898de78034757b0bb38f30b7b6fd21bca97b4ad.pdf"}]

Based on the search results, the authors of arXiv:2509.05614 are Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, and Guohao Dai.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 134 · 2026-05-29T06:37:33.922917+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Sigmoid Loss for Language Image Pre-Training\" Zhai Xiaohua ICCV 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Sigmoid Loss for Language Image Pre-Training\" Zhai Xiaohua ICCV 2023"
  }
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-29T06:37:33.923128+00:00_

Web search results for query: "SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer Chen CVPR 2023 arXiv 2303.17605"

Links: [{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution   Vision Transformer","url":"https://arxiv.org/pdf/2303.17605"},{"title":"» SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://mitibmwatsonailab.mit.edu/research/blog/sparsevit-revisiting-activation-sparsity-for-efficient-high-resolution-vision-transformer/"},{"title":"[2303.17605] SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://arxiv.org/abs/2303.17605"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer | Efficient AI","url":"https://research.nvidia.com/labs/eai/publication/sparsevit/"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10204119/;jsessionid=E57A45F654BCB46B8A866521E3B76475"},{"title":"[2303.17605] SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://ar5iv.labs.arxiv.org/html/2303.17605"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High ...","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.pdf"}]

I found the paper you're looking for! Here's what the web search revealed:

## SparseViT: Key Information

SparseViT introduces activation sparsity for recent window-based vision transformers (ViTs).

**Main Contributions:**
- Window attentions are naturally batched over blocks, enabling actual speedup with window activation pruning: approximately 50% latency reduction with 60% sparsity
- Different layers should be assig
…[truncated 859 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 136 · 2026-05-29T06:37:33.923410+00:00_

Web search results for query: "AdaViT: Adaptive Vision Transformers for Efficient Image Recognition Meng CVPR 2022 arXiv 2111.15668"

Links: [{"title":"GitHub - MengLcool/AdaViT: [CVPR-22] This is the official implementation of the paper \"Adavit: Adaptive vision transformers for efficient image recognition\". · GitHub","url":"https://github.com/MengLcool/AdaViT"},{"title":"CVPR 2022 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2022/html/Meng_AdaViT_Adaptive_Vision_Transformers_for_Efficient_Image_Recognition_CVPR_2022_paper.html"},{"title":"[PDF] AdaViT: Adaptive Vision Transformers for Efficient Image Recognition | Semantic Scholar","url":"https://www.semanticscholar.org/paper/AdaViT:-Adaptive-Vision-Transformers-for-Efficient-Meng-Li/38212997a6e8c55141574c329bb58d2eadcb0db5"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/pdf/2111.15668"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://xpaperchallenge.org/cv/survey/cvpr2022_summaries/138/"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://openaccess.thecvf.com/content/CVPR2022/papers/Meng_AdaViT_Adaptive_Vision_Transformers_for_Efficient_Image_Recognition_CVPR_2022_paper.pdf"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition | Request PDF","url":"https://www.researchgate.net/publication/363908358_AdaViT_Adaptive_Vision_Transformers_for_Efficient_Image_Recognition"},{"title":"[2111.15668v1] AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/abs/2111.15668v1"}]

I found detailed information about the paper you're looking for. Here are the key findings:

## Paper Overview

AdaViT: Adaptive Vision Transformers for Efficient Image Recognition was authored by Lingchen Meng, Hengduo Li, Bor-Chun Chen, Shiyi Lan, Zuxuan Wu, Yu-Gang Jiang, and Ser-Nam Lim from Fudan Univers
…[truncated 1144 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 137 · 2026-05-29T06:37:33.923646+00:00_

Web search results for query: "arxiv 2511.18950 authors Gao Ye Zhang Qian Compressor-VLA"

Links: [{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"Token Expand-Merge: Training-Free Token Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2512.09927"},{"title":"Implicit neural image field for biological microscopy image compression","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12638249/"}]

Based on the search results, I found the paper you're looking for:

**arXiv:2511.18950** - "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation" by authors Juntao Gao, Feiyang Ye, Jing Zhang, and Wenjing Qian.

The paper proposes Compressor-VLA, a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information in VLA models. The framework consists of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details.

Experimentally, Compressor-VLA achieves a competitive success rate on the LIBERO benchmark while reducing FLOPs by 59% and the visual token count by over 3x compared to its baseline, with real-robot deployments on a dual-arm robot platform validating the model's sim-to-real transferability and practical applicability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 10
}
```

</details>

---

### Tool result

_source line 138 · 2026-05-29T06:37:33.923881+00:00_

Web search results for query: "A-ViT: Adaptive Tokens for Efficient Vision Transformer Yin CVPR 2022 arXiv 2112.07658"

Links: [{"title":"[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658"},{"title":"[2112.07658v3] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v3"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211207658Y/abstract"},{"title":"[2112.07658v1] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v1"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"[2112.07658] A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://ar5iv.labs.arxiv.org/html/2112.07658"},{"title":"[CVPR'22 Oral] A-ViT: Adaptive Tokens for Efficient Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/357046283_CVPR'22_Oral_A-ViT_Adaptive_Tokens_for_Efficient_Vision_Transformer"}]

I found the paper! Here are the search results for your query:

**Paper Details:**

The paper is titled "AdaViT: Adaptive Tokens for Efficient Vision Transformer" with arXiv ID 2112.07658, authored by Hongxu Yin, Arash Vahdat, Jose Alvarez, Arun Mallya, Jan Kautz, and Pavlo Molchanov. The paper was submitted on December 14, 2021, with the final version released on October 5, 2022.

**Summary:**

A-ViT is a method that adaptively adjusts the inference cost of vision transformers for images of different complexity by automatically reducing the number of tokens processed in the network as inference proceeds. 

The method reformulates Adaptive Computation Time (ACT) for this task, extending halting to discard redundant spatial tokens. A-ViT requires no extra parameters or sub-network for halting, as it bases the learning of adaptive halting on the original network parameters.

**
…[truncated 272 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 139 · 2026-05-29T06:37:33.924151+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-2 CoRL 2023 proceedings PMLR volume 229 Zitkovich first author"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-2 CoRL 2023 proceedings PMLR volume 229 Zitkovich first author"
  }
}
```

</details>

---

### Tool call

_source line 140 · 2026-05-29T06:37:33.924373+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Qwen2 Technical Report Yang An arXiv 2407.10671"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Qwen2 Technical Report Yang An arXiv 2407.10671"
  }
}
```

</details>

---

### Tool result

_source line 141 · 2026-05-29T06:37:33.924581+00:00_

Web search results for query: "LightVLA ICRA 2026 accepted Jiang Titong authors"

Links: [{"title":"GitHub - LiAutoAD/LightVLA: Official Code for LightVLA (ICRA 2026)","url":"https://github.com/LiAutoAD/LightVLA"},{"title":"Beyond Training-Free Pruning: LightVLA Introduces Differentiable Token Pruning and Achieves a Dual Breakthrough in the Performance and Efficiency of VLA Models for the First Time | by Beck Moulton | Medium","url":"https://beckmoulton.medium.com/beyond-training-free-pruning-lightvla-introduces-differentiable-token-pruning-and-achieves-a-dual-7b2f562b0ab8"},{"title":"The Better You Learn, The Smarter You Prune: Towards Efficient Vision-language-action Models via Differentiable Token Pruning","url":"https://arxiv.org/pdf/2509.12594"},{"title":"Rethinking the Practicality of Vision-language-action Model: A Comprehensive Benchmark and An Improved Baseline","url":"https://arxiv.org/pdf/2602.22663"},{"title":"ICRA 2026 Program | Author Index","url":"https://ras.papercept.net/conferences/conferences/ICRA26/program/ICRA26_AuthorIndexWeb.html"},{"title":"ICRA 2026 Call for Papers: Important Dates, Submission Guide & Research Tips - Conference Inc.","url":"https://conferenceinc.net/post/icra-2026/"},{"title":"Multicenter validation of artificial intelligence software predicting large vessel occlusion using noncontrast brain CT","url":"https://www.medrxiv.org/content/10.1101/2024.07.01.24309790.full.pdf"}]

Based on the search results, I found information about LightVLA and its acceptance to ICRA 2026:

LightVLA has been accepted by ICRA 2026. 

The authors of the paper include: Titong Jiang, Xuefeng Jiang, Yuan Ma, Xin Wen, Bailin Li, Kun Zhan, Peng Jia, Yahui Liu, Sheng Sun, and Xianpeng Lang.

Titong Jiang is a fifth-year direct Ph.D. student at Tsinghua University, whose research directions include VLA, autonomous driving, and human-computer interaction, and Xuefeng Jiang is a fifth-year direct Ph.D. student at the Institute of Computing Technology, Chin
…[truncated 127 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 11
}
```

</details>

---

### Tool call

_source line 142 · 2026-05-29T06:37:33.924825+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Flow Matching for Generative Modeling\" Lipman Yaron ICLR 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Flow Matching for Generative Modeling\" Lipman Yaron ICLR 2023"
  }
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-29T06:37:33.925032+00:00_

Web search results for query: "SparseVLM Zhang Yuan ICML 2025 venue accepted"

Links: [{"title":"GitHub - Gumpest/SparseVLMs: [ICML'25] Official implementation of paper \"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference\" and \"SparseVLM+: Visual Token Sparsification with Improved Text-Visual Attention Pattern\" · GitHub","url":"https://github.com/Gumpest/SparseVLMs"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference | OpenReview","url":"https://openreview.net/forum?id=80faIPZ67S"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"ICML Poster SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://icml.cc/virtual/2025/poster/46297"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"Enhancing Visual-Language Prompt Tuning Through Sparse Knowledge-Guided Context Optimization","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11941247/"}]

Based on the search results, I can provide you with the information about SparseVLM:

SparseVLM was accepted by ICML 2025. The paper is titled "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" and was authored by Yuan Zhang, Chun-Kai Fan, Junpeng Ma, Wenzhao Zheng, Tao Huang, Kuan Cheng, Denis Gudovskiy, Tomoyuki Okuno, Yohei Nakata, Kurt Keutzer, and Shanghang Zhang.

The paper was published on May 1, 2025, as an ICML 2025 poster. The paper proposes an efficient training-free token optimization mechanism called SparseVLM without extra parameters or fine-tuning costs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 11
}
```

</details>

---

### Tool call

_source line 144 · 2026-05-29T06:37:33.925297+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "pi0.5 CoRL 2025 PMLR volume 305 pages 17-40 Black"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "pi0.5 CoRL 2025 PMLR volume 305 pages 17-40 Black"
  }
}
```

</details>

---

### Tool result

_source line 145 · 2026-05-29T06:37:33.925519+00:00_

Web search results for query: "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models Ye AAAI 2025 arXiv 2409.10197"

Links: [{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34366"},{"title":"GitHub - ywh187/FitPrune","url":"https://github.com/ywh187/FitPrune"},{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for   Multi-modal Large Language Models","url":"https://arxiv.org/pdf/2409.10197"},{"title":"[Literature Review] Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models","url":"https://www.themoonlight.io/en/review/fit-and-prune-fast-and-training-free-visual-token-pruning-for-multi-modal-large-language-models"},{"title":"[2409.10197] Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models","url":"https://arxiv.org/abs/2409.10197"},{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models","url":"https://arxiv.org/html/2409.10197v1"},{"title":"Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/390714965_Fit_and_Prune_Fast_and_Training-free_Visual_Token_Pruning_for_Multi-modal_Large_Language_Models"}]

I found the paper you're looking for! Here's the information:

The paper "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal Large Language Models" by Ye, W., Wu, Q., Lin, W., & Zhou, Y. was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 39(21), 22128–22136 (2025).

**Paper Details:**

- **ArXiv ID:** 2409.10197
- **Available at:** https://arxiv.org/abs/2409.10197 and https://arxiv.org/pdf/2409.10197
- **GitHub Repository:** https://git
…[truncated 938 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool result

_source line 146 · 2026-05-29T06:37:33.925767+00:00_

Web search results for query: "arXiv 2506.10100 EfficientVLA "Training-Free Acceleration and Compression" Yang Yantai 2025"

Links: [{"title":"[2506.10100] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"},{"title":"[Literature Review] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/efficientvla-training-free-acceleration-and-compression-for-vision-language-action-models"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.10100v1"},{"title":"[PDF] EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/EfficientVLA:-Training-Free-Acceleration-and-for-Yang-Wang/310b6b4048e36d5948de19fd26e112cbf05fa754"},{"title":"Paper page - EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.10100"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"}]

I found the paper! Here's information about the arXiv paper 2506.10100:

**Paper Title:** EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models

**Authors:** Yantai Yang, Yuhao Wang, Zichen Wen, Zhongwei Luo, Chang Zou, Zhipeng Zhang, Chuan Wen, and Linfeng Zhang

**Publication Date:** June 11, 2025

**Summary:**

Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent 
…[truncated 1087 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 9
}
```

</details>

---

### Tool call

_source line 147 · 2026-05-29T06:37:33.926016+00:00_

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
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
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

_source line 148 · 2026-05-29T06:37:33.926234+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 149 · 2026-05-29T06:37:33.926470+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"OpenVLA\" kim2024 CoRL 2024 \"8th Conference on Robot Learning\" PMLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"OpenVLA\" kim2024 CoRL 2024 \"8th Conference on Robot Learning\" PMLR"
  }
}
```

</details>

---

### Tool call

_source line 150 · 2026-05-29T06:37:33.926690+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "kim2025openoft \"Fine-Tuning Vision-Language-Action\" title \"OpenOFT\" or \"OpenVLA-OFT\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "kim2025openoft \"Fine-Tuning Vision-Language-Action\" title \"OpenOFT\" or \"OpenVLA-OFT\""
  }
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-29T06:37:33.926897+00:00_

Web search results for query: "RT-2 CoRL 2023 proceedings PMLR volume 229 Zitkovich first author"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"A robot operating system framework for using large language models in embodied AI | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01186-z"},{"title":"Open-World Object Manipulation using Pre-Trained Vision-Language Models","url":"https://proceedings.mlr.press/v229/stone23a.html"},{"title":"Advancing general robotic manipulation with multimodal foundation models: An embodied AI paradigm | Science China Technological Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11431-024-2910-3"},{"title":"Papers — CoRL 2023","url":"https://www.corl2023.org/papers"},{"title":"Emulating human-like adaptive vision for efficient and flexible machine visual perception | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01130-7"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 7th Conference on Robot Learning Held in Atlanta, USA on 06-09 November 2023 Published as Volume 229 by the Proceedings of Machine Learning Research on 02 December 2023. Volume Edited by: Jie Tan Marc Toussaint Kourosh Darvish Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v229/"}]

I found the paper you're looking for! The paper "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" by Brianna Zitkovich and colleagues was published in the Proceedings of The 7th Conference on Robot Learning, PMLR volume 229, pages 2165-2183, in 2023.

The paper is available at the official PMLR proceedings page: https://proceedings.mlr.press/v229/zitkovich23a.html


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 152 · 2026-05-29T06:37:33.927180+00:00_

Web search results for query: ""Sigmoid Loss for Language Image Pre-Training" Zhai Xiaohua ICCV 2023"

Links: [{"title":"Sigmoid Loss for Language Image Pre-Training","url":"https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html"},{"title":"Sigmoid Loss for Language Image Pre-Training [Quick Review]","url":"https://liner.com/review/sigmoid-loss-for-language-image-pretraining"},{"title":"Sigmoid Loss for Language Image Pre-Training","url":"https://ai.updf.com/paper-detail/sigmoid-loss-for-language-image-pre-training-zhai-mustafa-35aba190f28b5c39df333c06ca21f46bd4845eba"},{"title":"dblp: Sigmoid Loss for Language Image Pre-Training.","url":"https://dblp.org/rec/conf/iccv/ZhaiM0B23.html"},{"title":"Sigmoid Loss for Language Image Pre-Training","url":"https://www.researchgate.net/publication/377429802_Sigmoid_Loss_for_Language_Image_Pre-Training"},{"title":"Sigmoid Loss for Language Image Pre-Training - 专知论文","url":"https://zhuanzhi.ai/paper/7aa48d6c521644b44f67b86386052aa3"},{"title":"[Paper Note] Sigmoid Loss for Language Image Pre-Training, Xiaohua Zhai+, ICCV'23 · Issue #2111 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2111"},{"title":"Sigmoid Loss for Language Image Pre-Training","url":"https://arxiv.org/pdf/2303.15343"},{"title":"[2303.15343] Sigmoid Loss for Language Image Pre-Training","url":"https://arxiv.org/abs/2303.15343"},{"title":"Sigmoid Loss for Language Image Pre-Training Xiaohua Zhai⋆ Basil Mustafa","url":"https://openaccess.thecvf.com/content/ICCV2023/papers/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.pdf"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** Sigmoid Loss for Language Image Pre-Training

**Authors:** Xiaohua Zhai, Basil Mustafa, Alexander Kolesnikov, and Lucas Beyer

**Venue:** ICCV 2023 (Proceedings of the IEEE/CVF International Conference on Computer Vision)

**Main 
…[truncated 821 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 153 · 2026-05-29T06:37:33.927448+00:00_

Web search results for query: ""Flow Matching for Generative Modeling" Lipman Yaron ICLR 2023"

Links: [{"title":"Flow Matching for Generative Modeling: Scalable CNFs","url":"https://hunterheidenreich.com/notes/machine-learning/generative-models/flow-matching-for-generative-modeling/"},{"title":"Flow Matching for Generative Modeling - Weizmann Institute of Science","url":"https://weizmann.elsevierpure.com/en/publications/flow-matching-for-generative-modeling/"},{"title":"Flow Matching for Generative Modeling: ICLR 2023 Conference Paper - Studocu","url":"https://www.studocu.com/row/document/xiamen-university/food-technology/flow-matching-for-generative-modeling-iclr-2023-conference-paper/150968099"},{"title":"[Paper Note] Flow Matching for Generative Modeling, Yaron Lipman+, ICLR'23 · Issue #2166 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2166"},{"title":"ICLR Poster Flow Matching for Generative Modeling","url":"https://iclr.cc/virtual/2023/poster/11309"},{"title":"[2210.02747] Flow Matching for Generative Modeling","url":"https://arxiv.org/abs/2210.02747"},{"title":"(PDF) Flow Matching for Generative Modeling (2022) | Yaron Lipman | 292 Citations","url":"https://scispace.com/papers/flow-matching-for-generative-modeling-2ve8v3b6"}]

Based on the search results, here's information about the paper:

## Flow Matching for Generative Modeling

The paper "Flow Matching for Generative Modeling" was authored by Lipman, Y., Chen, R. T. Q., Ben-Hamu, H., Nickel, M., & Le, M., and published at the International Conference on Learning Representations (ICLR) at the 11th International Conference on Learning Representations, ICLR 2023, in Kigali, Rwanda.

### Key Contribution

The paper presents the notion of Flow Matching (FM), a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths.

### Main Innovation

Flow Matching is compatible with a general family of Gaussian proba
…[truncated 672 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 154 · 2026-05-29T06:37:33.927713+00:00_

Web search results for query: "pi0.5 CoRL 2025 PMLR volume 305 pages 17-40 Black"

Links: [{"title":"CoRL 2025 Survey - Speaker Deck","url":"https://speakerdeck.com/harukiabe/corl-2025-survey"},{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"CoRL 2025","url":"https://2025.corl.org/"},{"title":"AI learns racial information from the values of vital signs","url":"https://www.medrxiv.org/content/10.1101/2023.12.11.23299819.full.pdf"},{"title":"Personalized Hemodynamic Management Using Reinforcement Learning to Prevent Persistent Acute Kidney Injury After Cardiac Surgery","url":"https://www.medrxiv.org/content/10.1101/2025.10.23.25338698.full.pdf"},{"title":"GitHub - nepfaff/steerable-scene-generation: Code for \"Steerable Scene Generation with Post Training and Inference-Time Search\", CoRL 2025","url":"https://github.com/nepfaff/steerable-scene-generation"},{"title":"Learning to Play Blackjack: A Curriculum Learning Perspective","url":"https://arxiv.org/pdf/2604.00076"},{"title":"Evaluating General-Purpose LLMs for Patient-Facing Use: Dermatology-Centered Systematic Review and Meta-Analysis","url":"https://www.medrxiv.org/content/10.1101/2025.08.11.25333149.full.pdf"},{"title":"Effect of removing race correction factor in glomerular filtration rate estimation on predicting acute kidney injury after percutaneous coronary intervention","url":"https://www.medrxiv.org/content/10.1101/2022.01.18.22269155.full.pdf"},{"title":"Large Language Models for Supporting Clear Writing and Detecting Spin in Randomized Controlled Trials in Oncology","url":"https://www.medrxiv.org/content/10.1101/2025.05.05.25326991.full.pdf"}]

Based on the search results, I found information about π0.5 and the CoRL 2025 proceedings:

π0.5 is a work by Black et al. that appears to be related to robot foundation models. It's an example of learning diverse skills with a single policy, which is mentioned in a CoRL 2025 survey pre
…[truncated 602 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 155 · 2026-05-29T06:37:33.927970+00:00_

Web search results for query: "BLIP-2 Bootstrapping Language-Image Pre-Training Frozen Image Encoders Li Junnan ICML 2023"

Links: [{"title":"ICML Poster BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://icml.cc/virtual/2023/poster/25182"},{"title":"[Paper Note] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models, Junnan Li+, ICML'23, 2023.01 · Issue #4464 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/4464"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image   Encoders and Large Language Models","url":"https://arxiv.org/pdf/2301.12597"},{"title":"Paper page - BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://huggingface.co/papers/2301.12597"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models [Quick Review]","url":"https://liner.com/review/blip2-bootstrapping-languageimage-pretraining-with-frozen-image-encoders-and-large"},{"title":"[2301.12597] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://arxiv.org/abs/2301.12597"},{"title":"[PDF] BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/BLIP-2:-Bootstrapping-Language-Image-Pre-training-Li-Li/3f5b31c4f7350dc88002c121aecbdc82f86eb5bb"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models","url":"https://proceedings.mlr.press/v202/li23q.html"},{"title":"BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models - Singapore Management University","url":"https://smusg.elsevierpure.com/en/publications/blip-2-bootstrappi
…[truncated 1401 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 6
}
```

</details>

---

### Tool result

_source line 156 · 2026-05-29T06:37:33.928248+00:00_

Web search results for query: ""OpenVLA" kim2024 CoRL 2024 "8th Conference on Robot Learning" PMLR"

Links: [{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"Conference on Robot Learning (CoRL)","url":"https://dblp.org/db/conf/corl/index.html"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"(PDF) OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://www.researchgate.net/publication/381404911_OpenVLA_An_Open-Source_Vision-Language-Action_Model"},{"title":"What matters in building vision–language–action models for generalist robots | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01168-7"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"CoRL 2024 Conference | OpenReview","url":"https://openreview.net/group?id=robot-learning.org%2FCoRL%2F2024%2FConference"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"}]

Based on the search results, here's what I found about OpenVLA:

OpenVLA is a 7B-parameter open-source VLA (Vision-Language-Action model) trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

The model was developed to address the challenge that large policies pretrained on Internet-scale vision-language data and diverse robot demonstrations can fine-tune for new robot skills, but widespread adoption of VLAs for robotics has been challenging because existing VLAs are largely closed and inaccessible to the public, and prior wo
…[truncated 469 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 157 · 2026-05-29T06:37:33.928507+00:00_

Web search results for query: "Qwen2 Technical Report Yang An arXiv 2407.10671"

Links: [{"title":"[2407.10671] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671"},{"title":"[2407.10671v1] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v1"},{"title":"[2407.10671v4] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v4"},{"title":"Paper page - Qwen2 Technical Report","url":"https://huggingface.co/papers/2407.10671"},{"title":"Qwen2 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/382272036_Qwen2_Technical_Report"},{"title":"(PDF) Qwen2.5-Omni Technical Report","url":"https://www.researchgate.net/publication/390213734_Qwen25-Omni_Technical_Report"},{"title":"Qwen2 Technical Report - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240710671Y/abstract"}]

I found the Qwen2 Technical Report paper. Here's what the search revealed:

The report releases a comprehensive suite of foundational and instruction-tuned language models, encompassing a parameter range from 0.5 to 72 billion, featuring dense models and a Mixture-of-Experts model.

Qwen2 surpasses most prior open-weight models, including its predecessor Qwen1.5, and exhibits competitive performance relative to proprietary models across diverse benchmarks on language understanding, generation, multilingual proficiency, coding, mathematics, and reasoning.

The flagship model, Qwen2-72B, showcases remarkable performance: 84.2 on MMLU, 37.9 on GPQA, 64.6 on HumanEval, 89.5 on GSM8K, and 82.4 on BBH as a base language model.

The instruction-tuned variant, Qwen2-72B-Instruct, attains 9.1 on MT-Bench, 48.1 on Arena-Hard, and 35.7 on LiveCodeBench.

Qwen2 demonstrates robust multilingual capabilities, proficient in approximately 30 languages, spanning English, Chinese, Spanish, French, German, Arabic, Russian, Korean, Japanese, Thai, Vietnamese, and more.

The Qwen2 model weights are openly available on Hugging Face and ModelScope, with supplemen
…[truncated 278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 158 · 2026-05-29T06:37:33.928758+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CrossGET Cross-Guided Ensemble of Tokens Accelerating Vision-Language Transformers Shi Dachuan ICML 2024 arXiv 2305.17455"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CrossGET Cross-Guided Ensemble of Tokens Accelerating Vision-Language Transformers Shi Dachuan ICML 2024 arXiv 2305.17455"
  }
}
```

</details>

---

### Tool call

_source line 159 · 2026-05-29T06:37:33.928976+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR arXiv 2304.07193"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR arXiv 2304.07193"
  }
}
```

</details>

---

### Tool call

_source line 160 · 2026-05-29T06:37:33.929214+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2410.04417 SparseVLM first author \"Yuan Zhang\" OR \"Chun-Kai Fan\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2410.04417 SparseVLM first author \"Yuan Zhang\" OR \"Chun-Kai Fan\""
  }
}
```

</details>

---

### Tool call

_source line 161 · 2026-05-29T06:37:33.929433+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2112.07658 \"A-ViT\" title name change AdaViT"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2112.07658 \"A-ViT\" title name change AdaViT"
  }
}
```

</details>

---

### Tool call

_source line 162 · 2026-05-29T06:37:33.929639+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2403.06764 FastV authors \"Liang Chen\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2403.06764 FastV authors \"Liang Chen\""
  }
}
```

</details>

---

### Tool call

_source line 163 · 2026-05-29T06:37:33.929845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RoFormer Enhanced Transformer Rotary Position Embedding Su Jianlin Neurocomputing 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RoFormer Enhanced Transformer Rotary Position Embedding Su Jianlin Neurocomputing 2024"
  }
}
```

</details>

---

### Tool call

_source line 164 · 2026-05-29T06:37:33.930061+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2510.17777 exact title \"Decoupled\" OR \"Decoupling\" SparseVILA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2510.17777 exact title \"Decoupled\" OR \"Decoupling\" SparseVILA"
  }
}
```

</details>

---

### Tool call

_source line 165 · 2026-05-29T06:37:33.930300+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Quantifying Attention Flow Transformers Abnar Zuidema ACL 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Quantifying Attention Flow Transformers Abnar Zuidema ACL 2020"
  }
}
```

</details>

---

### Tool call

_source line 166 · 2026-05-29T06:37:33.930526+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "VLA-Cache arxiv 2502.02175 authors \"Siyu Xu\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "VLA-Cache arxiv 2502.02175 authors \"Siyu Xu\""
  }
}
```

</details>

---

### Tool call

_source line 167 · 2026-05-29T06:37:33.930733+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Vision-Language Foundation Models Effective Robot Imitators Li Xinghang ICLR 2024 arXiv 2311.01378"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Vision-Language Foundation Models Effective Robot Imitators Li Xinghang ICLR 2024 arXiv 2311.01378"
  }
}
```

</details>

---

### Tool call

_source line 168 · 2026-05-29T06:37:33.930948+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "TokenLearner arXiv 2106.11297 title \"What Can 8 Learned Tokens Do\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "TokenLearner arXiv 2106.11297 title \"What Can 8 Learned Tokens Do\""
  }
}
```

</details>

---

### Tool call

_source line 169 · 2026-05-29T06:37:33.931174+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"See What Matters\" ICML 2026 Feng Yixu authors list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"See What Matters\" ICML 2026 Feng Yixu authors list"
  }
}
```

</details>

---

### Tool call

_source line 170 · 2026-05-29T06:37:33.931380+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseViT CVPR 2023 authors Xuanyao Chen full author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseViT CVPR 2023 authors Xuanyao Chen full author list"
  }
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-29T06:37:33.931607+00:00_

Web search results for query: "kim2025openoft "Fine-Tuning Vision-Language-Action" title "OpenOFT" or "OpenVLA-OFT""

Links: [{"title":"moojink/openvla-7b-oft-finetuned-libero-10 · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-10"},{"title":"moojink/openvla-7b-oft-finetuned-libero-goal · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-goal"},{"title":"openvla-oft/README.md at main · moojink/openvla-oft","url":"https://github.com/moojink/openvla-oft/blob/main/README.md"},{"title":"moojink/openvla-7b-oft-finetuned-libero-object · Hugging Face","url":"https://huggingface.co/moojink/openvla-7b-oft-finetuned-libero-object"},{"title":"[2502.19645] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/abs/2502.19645"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"},{"title":"[Literature Review] Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://www.themoonlight.io/en/review/fine-tuning-vision-language-action-models-optimizing-speed-and-success"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://openvla-oft.github.io/"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://openvla.github.io/"},{"title":"GitHub - moojink/openvla-oft: Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success · GitHub","url":"https://github.com/moojink/openvla-oft"}]

I found relevant results for your search about the Kim et al. 2025 paper on fine-tuning vision-language-action models. Here's what I found:

## Paper Details

The paper is titled "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" by Kim, Moo Jin, Finn, Chelsea, and Liang, Percy (arXiv preprint arXiv:2502.19645, 2025).

## Key Contributions

The work proposes an Optimized Fine-Tuning (OFT) recip
…[truncated 907 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 172 · 2026-05-29T06:37:33.931865+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025"
  }
}
```

</details>

---

### Tool call

_source line 173 · 2026-05-29T06:37:33.932076+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2407.10671 Qwen2 first author \"An Yang\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2407.10671 Qwen2 first author \"An Yang\""
  }
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-29T06:37:33.932477+00:00_

Web search results for query: "arxiv 2410.04417 SparseVLM first author "Yuan Zhang" OR "Chun-Kai Fan""

Links: [{"title":"Paper page - SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://huggingface.co/papers/2410.04417"},{"title":"[Literature Review] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://www.themoonlight.io/en/review/sparsevlm-visual-token-sparsification-for-efficient-vision-language-model-inference"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference · Issue #38509 · huggingface/transformers","url":"https://github.com/huggingface/transformers/issues/38509"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241004417Z/abstract"},{"title":"[2410.04417] SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/abs/2410.04417"},{"title":"SparseVLM","url":"https://leofan90.github.io/SparseVLMs.github.io/"},{"title":"Panasonic HD develops “SparseVLM” technology that doubles the processing speed of Vision-Language Models | Innovations/Technologies | Company | Press Releases | Panasonic Newsroom Global","url":"https://news.panasonic.com/global/zh-CHS/press/en250704-2"},{"title":"SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference","url":"https://arxiv.org/html/2410.04417"},{"title":"GitHub - Theia-4869/SparseVLM","url":"https://github.com/Theia-4869/SparseVLM"}]

I found the paper! The arxiv paper 2410.04417 is titled "SparseVLM: Visual Token Sparsification for Efficient Vision-Language Model Inference" and the first authors are Yuan Zhang and Chun-Kai Fan, confirming that both authors you mentioned are indeed the first authors listed.

SparseVLM optimizes vision-language models by pruning irrelevant visual tokens using text-relevant 
…[truncated 390 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-29T06:37:33.932729+00:00_

Web search results for query: "SparseViT CVPR 2023 authors Xuanyao Chen full author list"

Links: [{"title":"CVPR 2023 Open Access Repository","url":"https://openaccess.thecvf.com/content/CVPR2023/html/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.html"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer | Request PDF","url":"https://www.researchgate.net/publication/373309740_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer"},{"title":"dblp: Xuanyao Chen","url":"https://dblp.org/pid/294/6120.html"},{"title":"CVPR Poster SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://cvpr.thecvf.com/virtual/2023/poster/21307"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High ...","url":"https://openaccess.thecvf.com/content/CVPR2023/papers/Chen_SparseViT_Revisiting_Activation_Sparsity_for_Efficient_High-Resolution_Vision_Transformer_CVPR_2023_paper.pdf"},{"title":"[2303.17605] SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution Vision Transformer","url":"https://arxiv.org/abs/2303.17605"},{"title":"SparseViT: Revisiting Activation Sparsity for Efficient High-Resolution   Vision Transformer","url":"https://arxiv.org/pdf/2303.17605"}]

The full author list for the SparseViT CVPR 2023 paper is: Xuanyao Chen, Zhijian Liu, Haotian Tang, Li Yi, Hang Zhao, and Song Han.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-29T06:37:33.932964+00:00_

Web search results for query: "CrossGET Cross-Guided Ensemble of Tokens Accelerating Vision-Language Transformers Shi Dachuan ICML 2024 arXiv 2305.17455"

Links: [{"title":"Releases · sdc17/CrossGET","url":"https://github.com/sdc17/CrossGET/releases"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | OpenReview","url":"https://openreview.net/forum?id=CSIfCpXhCF"},{"title":"GitHub - sdc17/CrossGET: [ICML 2024] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers.","url":"https://github.com/sdc17/CrossGET"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating   Vision-Language Transformers","url":"https://arxiv.org/pdf/2305.17455"},{"title":"[2305.17455] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/abs/2305.17455"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/html/2305.17455"},{"title":"Sparsity Meets Similarity: Leveraging Long-Tail Distribution for Dynamic Optimized Token Representation in Multimodal Large Language Models","url":"https://arxiv.org/html/2409.01162v2"},{"title":"GitHub - daixiangzi/Awesome-Token-Compress: A paper list of some recent works about Token Compress for Vit and VLM · GitHub","url":"https://github.com/daixiangzi/Awesome-Token-Compress"}]

I found the paper you're looking for! Here's what I found about CrossGET:

CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers was presented at ICML 2024. The paper is authored by Shi Dachuan and colleagues, with the arXiv identifier 2305.17455.

The paper introduces CrossGET, a general acceleration framework for vision-language Transformers that adaptively combines tokens in real-time during inference, significantly reducing computational costs while maintaining high performance.

The framework features two main innovations:

1
…[truncated 746 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 177 · 2026-05-29T06:37:33.933236+00:00_

Web search results for query: "arXiv 2112.07658 "A-ViT" title name change AdaViT"

Links: [{"title":"[2112.07658v3] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v3"},{"title":"[2112.07658] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658"},{"title":"[2112.07658v1] AdaViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://arxiv.org/abs/2112.07658v1"},{"title":"[2112.07658] A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://ar5iv.labs.arxiv.org/html/2112.07658"},{"title":"AdaViT: Adaptive Tokens for Efficient Vision Transformer - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211207658Y/abstract"},{"title":"A-ViT: Adaptive Tokens for Efficient Vision Transformer","url":"https://a-vit.github.io/"},{"title":"[2111.15668] AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/abs/2111.15668"},{"title":"AdaViT: Adaptive Vision Transformers for Efficient Image Recognition","url":"https://arxiv.org/pdf/2111.15668"}]

Based on the search results, I can provide you with information about the arXiv paper 2112.07658:

The paper's title is "AdaViT: Adaptive Tokens for Efficient Vision Transformer", though the method itself is introduced as "A-ViT". 

The title naming shows an interesting pattern: the initial version (v1) submitted on December 14, 2021 used "AdaViT" in the abstract, while later versions (v3 from October 5, 2022) refer to the method as "A-ViT" in the abstract. However, the official project page and citations show both naming conventions being used: "A-ViT: Adaptive Tokens for Efficient Vision Transformer" for the conference paper and "AdaViT: Adaptive Tokens for Efficient Vision Transformer" for the arXiv version.

So to clarify: the paper's official title appears to be "AdaViT" or "A-ViT" (with both forms used interchangeably), while the method name in the abstract evolved between 
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 178 · 2026-05-29T06:37:33.933496+00:00_

Web search results for query: "DINOv2 Learning Robust Visual Features without Supervision Oquab TMLR arXiv 2304.07193"

Links: [{"title":"DINOv2: Learning Robust Visual Features without Supervision | alphaXiv","url":"https://www.alphaxiv.org/overview/2304.07193"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"[2304.07193v1] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v1"},{"title":"[2304.07193v2] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193v2"},{"title":"Paper page - DINOv2: Learning Robust Visual Features without Supervision","url":"https://huggingface.co/papers/2304.07193"},{"title":"[PDF] DINOv2: Learning Robust Visual Features without Supervision | Semantic Scholar","url":"https://www.semanticscholar.org/paper/DINOv2:-Learning-Robust-Visual-Features-without-Oquab-Darcet/5a9cb1b3dc4655218b3deeaf4a2417a9a8cd0891"},{"title":"GitHub - facebookresearch/dinov2: PyTorch code and models for the DINOv2 self-supervised learning method. · GitHub","url":"https://github.com/facebookresearch/dinov2"}]

I found the paper you're searching for. Here's what I found:

**DINOv2: Learning Robust Visual Features without Supervision** is authored by Maxime Oquab, Timothée Darcet, and others, with the arXiv identifier 2304.07193.

**Key Points:**

The paper presents a foundation model in computer vision that produces all-purpose visual features that work across image distributions and tasks without fine-tuning.

The work demonstrates that existing self-supervised pretraining methods can produce such features if trained on enough curated data from diverse sources.

The authors revisit existing approaches and combine different techniques to scale pretraining in terms of data and model size, with most technical contributions aimed at accelerating and stabilizing training at scale.

For data,
…[truncated 555 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 179 · 2026-05-29T06:37:33.933739+00:00_

Web search results for query: "arxiv 2403.06764 FastV authors "Liang Chen""

Links: [{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/abs/2403.06764"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"https://arxiv.org/html/2403.06764v1"},{"title":"[2403.06764] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models","url":"http://export.arxiv.org/abs/2403.06764"},{"title":"GitHub - chenllliang/FastV: Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/chenllliang/FastV"},{"title":"[PDF] An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/An-Image-is-Worth-1-2-Tokens-After-Layer-2:-for-Chen-Zhao/3421d12d98956c36c5d39c0ef023b378b6922068"},{"title":"GitHub - pkunlp-icler/FastV: [ECCV 2024 Oral] Code for paper: An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models · GitHub","url":"https://github.com/pkunlp-icler/FastV"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-PLay Acceleration for VLLM Inference","url":"https://arxiv.org/html/2403.06764v3"},{"title":"An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play ...","url":"https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/10478.pdf"}]

Based on the search results, here's what I found about the paper arxiv 2403.06764 FastV:

**Paper Title:** An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models

**Authors:** Liang Chen, Haozhe Zhao, Tianyu Liu, Shuai Bai, Junyang Lin, Chang Zhou, Baobao Chan
…[truncated 972 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 180 · 2026-05-29T06:37:33.933993+00:00_

Web search results for query: "Vision-Language Foundation Models Effective Robot Imitators Li Xinghang ICLR 2024 arXiv 2311.01378"

Links: [{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"Paper page - Vision-Language Foundation Models as Effective Robot Imitators","url":"https://huggingface.co/papers/2311.01378"},{"title":"Vision-Language Foundation Models as Effective Robot Imitators | alphaXiv","url":"https://www.alphaxiv.org/hi/overview/2311.01378v3"},{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation","url":"https://arxiv.org/html/2406.04339v2"},{"title":"[PDF] Vision-Language Foundation Models as Effective Robot Imitators | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Vision-Language-Foundation-Models-as-Effective-Li-Liu/857efca0d4cbece97da4b904de1d506c2af25f9c"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"}]

I found the paper you're looking for. Here's what the search revealed:

The paper titled "Vision-Language Foundation Models as Effective Robot Imitators" was submitted on November 2, 2023 (arXiv:2311.01378) and last revised on February 5, 2024. The authors are Xinghang Li, Minghuan Liu, Hanbo Zhang, Cunjun Yu, Jie Xu, Hongtao Wu, Chilam Cheang, Ya Jing, Weinan Zhang, Huaping Liu, Hang Li, and Tao Kong.

The research seeks a straightforward way of making use of existing vision-language models (VLMs) with simple fine-tuning on robotics d
…[truncated 716 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 181 · 2026-05-29T06:37:33.934269+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "proceedings.mlr.press v305 black25a pi0.5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "proceedings.mlr.press v305 black25a pi0.5"
  }
}
```

</details>

---

### Tool result

_source line 182 · 2026-05-29T06:37:33.934507+00:00_

Web search results for query: "TokenLearner arXiv 2106.11297 title "What Can 8 Learned Tokens Do""

Links: [{"title":"[2106.11297] TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://arxiv.org/abs/2106.11297"},{"title":"GitHub - xiamenwcy/TokenLearner: A PyTorch implementation of \"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"","url":"https://github.com/xiamenwcy/TokenLearner"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210611297R/abstract"},{"title":"GitHub - ariG23498/TokenLearner: TensorFlow implementation of \"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?\"","url":"https://github.com/ariG23498/TokenLearner"},{"title":"Paper page - TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://huggingface.co/papers/2106.11297"},{"title":"[PDF] TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TokenLearner%3A-What-Can-8-Learned-Tokens-Do-for-and-Ryoo-Piergiovanni/48bcfea07f343b29128c71bb2cce5f3ab62f6d85"},{"title":"1 TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?","url":"https://arxiv.org/pdf/2106.11297"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | Request PDF","url":"https://www.researchgate.net/publication/352642552_TokenLearner_What_Can_8_Learned_Tokens_Do_for_Images_and_Videos"},{"title":"TokenLearner: What Can 8 Learned Tokens Do for Images and Videos? | alphaXiv","url":"https://www.alphaxiv.org/overview/2106.11297v4"}]

I found the paper you're looking for! Here's what I found:

**TokenLearner: What Can 8 Learned Tokens Do for Images and Videos?** is a paper by Michael S. Ryoo, AJ Piergiovanni, Anurag Arnab, Mostafa Dehghani, and Anelia Angelova, with the arXiv identifier 2106.11297.

**Overview:**
The paper introduces a novel visual representation 
…[truncated 731 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 183 · 2026-05-29T06:37:33.934746+00:00_

Web search results for query: "arxiv 2510.17777 exact title "Decoupled" OR "Decoupling" SparseVILA"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"2025-10-21 SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/html/2510.17777"},{"title":"Decoupled Action Expert: Confining Task Knowledge to the Conditioning Pathway","url":"https://arxiv.org/pdf/2511.12101"},{"title":"Decoupled Seg Tokens Make Stronger Reasoning Video Segmenter and Grounder","url":"https://arxiv.org/pdf/2506.22880"},{"title":"Decoupling Global and Local Representations via Invertible Generative   Flows","url":"https://arxiv.org/pdf/2004.11820"}]

I found the paper! The search results show that SparseVILA is a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages.

**Paper Details:**
- **ArXiv ID:** 2510.17777
- **Title:** "SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference"
- **Submitted:** October 20, 2025

**Key Points:**
SparseVILA distributes sparsity across stages by pruning redundant visual tokens during prefill and retrieving only query-relevant tokens during decoding. This decoupled design matches leading prefill pruning methods while preserving multi-turn fidelity by retaining most of the visual cache so that query-aware tokens can be retrieved at each conversation round.

Built on an AWQ-optimized inference pipeline, SparseVILA achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 184 · 2026-05-29T06:37:33.934988+00:00_

Web search results for query: "VLA-Cache arxiv 2502.02175 authors "Siyu Xu""

Links: [{"title":"[2502.02175] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/abs/2502.02175"},{"title":"(PDF) VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://www.researchgate.net/publication/388685612_VLA-Cache_Towards_Efficient_Vision-Language-Action_Model_via_Adaptive_Token_Caching_in_Robotic_Manipulation"},{"title":"GitHub - siyuhsu/vla-cache: [NeurIPS 2025] VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching · GitHub","url":"https://github.com/siyuhsu/vla-cache"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=1554&show=1919"},{"title":"VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching","url":"https://arxiv.org/html/2502.02175"},{"title":"VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://arxiv.org/html/2502.02175v1"},{"title":"Paper page - VLA-Cache: Towards Efficient Vision-Language-Action Model via Adaptive Token Caching in Robotic Manipulation","url":"https://huggingface.co/papers/2502.02175"}]

I found the paper you're looking for. Here are the key details:

**Paper Title:** VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching

**arXiv ID:** 2502.02175

**Authors:** Siyu Xu, Yunke Wang, Chenghao Xia, Dihao Zhu, Tao Huang, and Chang Xu

**Overview:** The paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. VLA-Cache exploits temporal continuity in robotic manipulation by identifying minimally changed tokens between adjacent frames and reusing their cached key-value representations, while selectively re-computing task-relev
…[truncated 302 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 185 · 2026-05-29T06:37:33.935269+00:00_

Web search results for query: "Quantifying Attention Flow Transformers Abnar Zuidema ACL 2020"

Links: [{"title":"Quantifying Attention Flow in Transformers - ACL Anthology","url":"https://aclanthology.org/2020.acl-main.385/"},{"title":"Quantifying Attention Flow in Transformers","url":"https://notes-vault.pages.dev/Scientific-Literature-References/literature-notes/@abnarQuantifyingAttentionFlow2020"},{"title":"UvA-DARE (Digital Academic Repository)","url":"https://pure.uva.nl/ws/files/178487922/2020.acl-main.385.pdf"},{"title":"Attention Flow - AmsterdamNLP","url":"https://amsterdamnlp.github.io/blog/attentionflow/"},{"title":"Quantifying Attention Flow in Transformers | MYRIAD","url":"https://creatis-myriad.github.io/2022/07/07/AttentionRollout.html"},{"title":"[PDF] Quantifying Attention Flow in Transformers | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Quantifying-Attention-Flow-in-Transformers-Abnar-Zuidema/76a9f336481b39515d6cea2920696f11fb686451"},{"title":"Quantifying Attention Flow in Transformers","url":"https://aclanthology.org/2020.acl-main.385.pdf"},{"title":"ACL2020: Quantifying Attention Flow in Transformers","url":"https://virtual.acl2020.org/paper_main.385.html"},{"title":"Quantifying Attention Flow in Transformers | Request PDF","url":"https://www.researchgate.net/publication/343298597_Quantifying_Attention_Flow_in_Transformers"},{"title":"Quantifying Attention Flow in Transformers","url":"https://arxiv.org/pdf/2005.00928"}]

I found the paper you're looking for. Here's what I found:

"Quantifying Attention Flow in Transformers" is a paper by Samira Abnar and Willem Zuidema, published in 2020 in the Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics (ACL), pages 4190–4197.

The paper addresses how "self-attention" in the Transformer model combines information from attended embeddings into the representation of the focal embedding in the next layer, causing information originating from differen
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool call

_source line 186 · 2026-05-29T06:37:33.935528+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-2 Brohan first author or Zitkovich CoRL 2023 author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-2 Brohan first author or Zitkovich CoRL 2023 author list"
  }
}
```

</details>

---

### Tool result

_source line 187 · 2026-05-29T06:37:33.935732+00:00_

Web search results for query: "RoFormer Enhanced Transformer Rotary Position Embedding Su Jianlin Neurocomputing 2024"

Links: [{"title":"dblp: RoFormer: Enhanced transformer with Rotary Position Embedding.","url":"https://dblp.org/rec/journals/ijon/SuALPBL24.html"},{"title":"RoFormer: Enhanced transformer with Rotary Position Embedding - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0925231223011864"},{"title":"[2104.09864] RoFormer: Enhanced Transformer with Rotary Position Embedding","url":"https://arxiv.org/abs/2104.09864"},{"title":"ROFORMER: ENHANCED TRANSFORMER WITH ROTARY POSITION EMBEDDING Jianlin Su","url":"https://arxiv.org/pdf/2104.09864"},{"title":"RoFormer: Enhanced transformer with Rotary Position Embedding | Request PDF","url":"https://www.researchgate.net/publication/375900997_RoFormer_Enhanced_transformer_with_Rotary_Position_Embedding"},{"title":"(PDF) RoFormer: Enhanced Transformer with Rotary Position Embedding","url":"https://www.researchgate.net/publication/351019664_RoFormer_Enhanced_Transformer_with_Rotary_Position_Embedding"},{"title":"RoFormer: : Enhanced transformer with Rotary Position Embedding: Neurocomputing: Vol 568, No C","url":"https://dl.acm.org/doi/10.1016/j.neucom.2023.127063"}]

Based on the search results, I found the paper you're looking for:

The paper "RoFormer: Enhanced transformer with Rotary Position Embedding" was authored by Jianlin Su, Murtadha H. M. Ahmed, Yu Lu, Shengfeng Pan, Wen Bo, and Yunfeng Liu, and was published in Neurocomputing volume 568 in 2024.

The paper proposes a novel method named Rotary Position Embedding (RoPE) to effectively leverage positional information, which encodes the absolute position with a rotation matrix and incorporates the explicit relative position dependency in the self-attention formulation. 

RoPE enables valuable properties including the flexibility of sequence length, decaying inter-token dependency with increasing relative distances, and the capab
…[truncated 447 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 5
}
```

</details>

---

### Tool call

_source line 188 · 2026-05-29T06:37:33.935968+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SmolVLA 2506.01844 submission date June 2025 year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SmolVLA 2506.01844 submission date June 2025 year"
  }
}
```

</details>

---

### Tool result

_source line 189 · 2026-05-29T06:37:33.936317+00:00_

Web search results for query: "arxiv 2511.16449 VLA-Pruner authors Liu Ziyan 2025"

Links: [{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"Computer Vision and Pattern Recognition 2025","url":"https://www.arxiv.org/list/cs.CV/2025?skip=24300&show=50"},{"title":"Computer Science Nov 2025","url":"https://arxiv.org/list/cs/2025-11?skip=7900"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/pdf/2511.16449"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449v2"}]

Based on the search results, here's the information about arxiv 2511.16449:

**Paper:** VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference

**Authors:** Ziyan Liu, Yeqiu Chen, Hongyi Cai, Tao Lin, Shuo Yang, Zheng Liu, Bo Zhao

**Submission Date:** Submitted on 20 Nov 2025 (v1), last revised 10 Feb 2026 (this version, v3)

**Affiliations:** School of AI, Shanghai Jiao Tong University; University of Science and Technology of China; Harbin Institute of Technology (Shenzhen); BAAI

**Overview:** VLA-Pruner is a versatile plug-and-play VLA-specific token prune method that aligns with the dual-system nature of VLA models and exploits the temporal continuity in robot manipulation.

The paper addresses the challenge of computational efficiency in Vision-Language-Action models for embodied AI applications, particularly focusing on token pruning strategies tailored to VLA systems rather than generic Vision-Language Models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 190 · 2026-05-29T06:37:33.936572+00:00_

Web search results for query: "arXiv 2407.10671 Qwen2 first author "An Yang""

Links: [{"title":"[2407.10671] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671"},{"title":"[2407.10671v1] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v1"},{"title":"[2407.10671v4] Qwen2 Technical Report","url":"https://arxiv.org/abs/2407.10671v4"},{"title":"Qwen2 Technical Report | Request PDF","url":"https://www.researchgate.net/publication/382272036_Qwen2_Technical_Report"},{"title":"Paper page - Qwen2 Technical Report","url":"https://huggingface.co/papers/2407.10671"},{"title":"(PDF) Qwen2.5-Omni Technical Report","url":"https://www.researchgate.net/publication/390213734_Qwen25-Omni_Technical_Report"},{"title":"[PDF] Qwen2 Technical Report | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Qwen2-Technical-Report-Yang-Yang/54fb839f621e3fe787437ab8ca5f37e7e4726bfe"},{"title":"arXiv:2407.10671v4 [cs.CL] 10 Sep 2024","url":"https://arxiv.org/pdf/2407.10671"}]

Based on the search results, I can confirm that arXiv:2407.10671 is the Qwen2 Technical Report with An Yang listed as the first author. The paper was submitted on July 15, 2024, with the latest version (v4) revised on September 10, 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 191 · 2026-05-29T06:37:33.936804+00:00_

Web search results for query: "proceedings.mlr.press v305 black25a pi0.5"

Links: [{"title":"$\\pi_0.5$: a Vision-Language-Action Model with Open-World Generalization","url":"https://proceedings.mlr.press/v305/black25a.html"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://proceedings.mlr.press/v305/haon25a.html"},{"title":"First Order Model-Based RL through Decoupled Backpropagation","url":"https://proceedings.mlr.press/v305/amigo25a.html"},{"title":"FlashBack: Consistency Model-Accelerated Shared Autonomy","url":"https://proceedings.mlr.press/v305/sun25a.html"},{"title":"Meta-Optimization and Program Search using Language Models for Task and Motion Planning","url":"https://proceedings.mlr.press/v305/shcherba25a.html"},{"title":"GitHub - mlresearch/v305: Proceedings of CoRL 2025 · GitHub","url":"https://github.com/mlresearch/v305"},{"title":"Diffusion-Guided Multi-Arm Motion Planning","url":"https://proceedings.mlr.press/v305/parimi25a.html"},{"title":"LocoFormer: Generalist Locomotion via Long-context Adaptation","url":"https://proceedings.mlr.press/v305/liu25a.html"},{"title":"Neural Robot Dynamics","url":"https://proceedings.mlr.press/v305/xu25g.html"}]

Based on the search results, I found the paper you're looking for:

**π₀.₅: a Vision-Language-Action Model with Open-World Generalization** is published in Proceedings of The 9th Conference on Robot Learning, in Proceedings of Machine Learning Research volume 305, pages 17-40.

The paper has multiple authors including K. Black, N. Brown, J. Darpinian, and many others, and was published in 2025. The paper appears to be available at https://proceedings.mlr.press/v305/black25a.html.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 192 · 2026-05-29T06:37:33.937046+00:00_

Web search results for query: "SmolVLA 2506.01844 submission date June 2025 year"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"[2506.01844v1] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"lerobot/smolvla_base · Hugging Face","url":"https://huggingface.co/lerobot/smolvla_base"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"}]

Based on the search results, the SmolVLA paper (arXiv:2506.01844) was submitted on June 2, 2025. This confirms the submission date is in June 2025 as you mentioned in your query.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 193 · 2026-05-29T06:37:33.937311+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CogACT arXiv 2411.19650 authors \"Qixiu Li\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CogACT arXiv 2411.19650 authors \"Qixiu Li\""
  }
}
```

</details>

---

### Tool call

_source line 194 · 2026-05-29T06:37:33.937527+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "X-VLA arXiv 2510.10274 authors \"Jinliang Zheng\" year 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "X-VLA arXiv 2510.10274 authors \"Jinliang Zheng\" year 2025"
  }
}
```

</details>

---

### Tool call

_source line 195 · 2026-05-29T06:37:33.937735+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Flamingo Visual Language Model Few-Shot Learning Alayrac Jean-Baptiste NeurIPS 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Flamingo Visual Language Model Few-Shot Learning Alayrac Jean-Baptiste NeurIPS 2022"
  }
}
```

</details>

---

### Tool call

_source line 196 · 2026-05-29T06:37:33.937949+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Perceiver General Perception Iterative Attention Jaegle Andrew ICML 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Perceiver General Perception Iterative Attention Jaegle Andrew ICML 2021"
  }
}
```

</details>

---

### Tool call

_source line 197 · 2026-05-29T06:37:33.938178+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control arXiv 2307.15818 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control arXiv 2307.15818 authors"
  }
}
```

</details>

---

### Tool result

_source line 198 · 2026-05-29T06:37:33.938415+00:00_

Web search results for query: "RT-2 Brohan first author or Zitkovich CoRL 2023 author list"

Links: [{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"Training Strategies for Efficient Embodied Reasoning","url":"https://arxiv.org/html/2505.08243v1"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"Real-time open-vocabulary perception for mobile robots on edge devices: a systematic analysis of the accuracy-latency trade-off - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12583037/"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"}]

Based on the search results, I can answer your query:

The first author of the RT-2 paper is Anthony Brohan, and Brianna Zitkovich is the first-listed author in the CoRL 2023 version of the paper. 

It's worth noting that the authors are listed in alphabetical order, with a contribution statement provided in the paper appendix, which explains why the author order differs between the arXiv version (which lists Brohan first) and the off
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 199 · 2026-05-29T06:37:33.938669+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Open X-Embodiment Robotic Learning Datasets RT-X Models ICRA 2024 arXiv 2310.08864"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Open X-Embodiment Robotic Learning Datasets RT-X Models ICRA 2024 arXiv 2310.08864"
  }
}
```

</details>

---

### Tool call

_source line 200 · 2026-05-29T06:37:33.938883+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "H2O Heavy-Hitter Oracle Efficient Generative Inference Large Language Models Zhang Zhenyu NeurIPS 2023 arXiv 2306.14048"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "H2O Heavy-Hitter Oracle Efficient Generative Inference Large Language Models Zhang Zhenyu NeurIPS 2023 arXiv 2306.14048"
  }
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-29T06:37:33.939100+00:00_

Web search results for query: "CogACT arXiv 2411.19650 authors "Qixiu Li""

Links: [{"title":"[2411.19650v1] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650v1"},{"title":"[2411.19650] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/abs/2411.19650"},{"title":"[PDF] CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CogACT:-A-Foundational-Vision-Language-Action-Model-Li-Liang/54caf5927a6d656bb84d2a16e16fa2b0c5d6f522"},{"title":"(PDF) CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://www.researchgate.net/publication/386335138_CogACT_A_Foundational_Vision-Language-Action_Model_for_Synergizing_Cognition_and_Action_in_Robotic_Manipulation"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://cogact.github.io/"},{"title":"Scalable Vision-Language-Action Model Pretraining for ​Robotic Manipulation with Real-Life Human Activity Videos","url":"https://arxiv.org/html/2510.21571v1"},{"title":"README.md · CogACT/CogACT-Small at 8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d","url":"https://huggingface.co/CogACT/CogACT-Small/blob/8afbf8b0b3ab13fe6bb08d17c6f5956218d45e8d/README.md"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"GitHub - microsoft/CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://github.com/microsoft/CogACT"},{"title":"GeoVLA: Empowering 3D Representations in Vision-Language-Action 
…[truncated 1309 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-29T06:37:33.939389+00:00_

Web search results for query: "Flamingo Visual Language Model Few-Shot Learning Alayrac Jean-Baptiste NeurIPS 2022"

Links: [{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html"},{"title":"[PDF] Flamingo: a Visual Language Model for Few-Shot Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flamingo:-a-Visual-Language-Model-for-Few-Shot-Alayrac-Donahue/26218bdcc3945c7edae7aa2adbfba4cd820a2df3"},{"title":"[2204.14198] Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/abs/2204.14198"},{"title":"Flamingo: a visual language model for few-shot learning - ORA - Oxford University Research Archive","url":"https://ora.ox.ac.uk/objects/uuid:72fd0848-5ee3-43fa-bdab-d777270d7a58"},{"title":"Flamingo: a Visual - Language Model for Few-Shot Learning","url":"https://faculty.cc.gatech.edu/~zk15/teaching/AY2024_cs8803vlm_fall/slides/L10_Flamingo.pdf"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://arxiv.org/pdf/2204.14198"},{"title":"Flamingo: a Visual Language Model for Few-Shot Learning - Samuel Albanie","url":"https://samuelalbanie.com/digests/2022-05-flamingo/"},{"title":"🦩 Flamingo: a Visual Language Model for Few-Shot Learning","url":"https://papers.neurips.cc/paper_files/paper/2022/file/960a172bc7fbf0177ccccbb411a7d800-Paper-Conference.pdf"}]

I've successfully found information about the Flamingo Visual Language Model paper. Here are the search results:

## Overview

The paper introduces Flamingo, a family of Visual Language Models (VLM) designed to address the challenge of building models that can be rapidly adapted to novel tasks using only a handful of annotated examples.

## Key Details

- **Authors**: The paper was authored by Jean-Baptiste Alayrac, Jeff Donahue, Pauline Luc, Antoine Miech, and 24 other co-authors
- **Publication**: Published a
…[truncated 809 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 203 · 2026-05-29T06:37:33.939649+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Visual Instruction Tuning\" LLaVA authors \"Qingyang Wu\" NeurIPS 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Visual Instruction Tuning\" LLaVA authors \"Qingyang Wu\" NeurIPS 2023"
  }
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-29T06:37:33.939897+00:00_

Web search results for query: ""See What Matters" ICML 2026 Feng Yixu authors list"

Links: [{"title":"Downloads 2026","url":"https://icml.cc/Downloads/2026"},{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"},{"title":"Knowledge Graph and Accurate Portrait Construction of Scientific and   Technological Academic Conferences","url":"https://arxiv.org/pdf/2204.04888"},{"title":"AI Can Learn Scientific Taste","url":"https://arxiv.org/pdf/2603.14473"},{"title":"Paper Digest: ICML 2026 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2026/05/icml-2026-papers-highlights/"},{"title":"Paper Digest: ICML 2026 Papers & Highlights – Resources | Paper Digest","url":"https://resources.paperdigest.org/2026/05/icml-2026-papers-highlights/"},{"title":"ICLR 2026 Thursday 04/23","url":"https://iclr.cc/virtual/2026/day/4/23"}]

Let me search more specifically for the paper with that exact title:

Links: [{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"},{"title":"ICML 2022 Reviewers","url":"https://icml.cc/Conferences/2022/Reviewers"},{"title":"Model stability of COVID-19 mortality prediction with biomarkers","url":"https://www.medrxiv.org/content/10.1101/2020.07.29.20161323.full.pdf"},{"title":"The ICML 2023 Ranking Experiment: Examining Author Self-Assessment in ML/AI Peer Review","url":"https://arxiv.org/pdf/2408.13430"},{"title":"ICML 2022 Authorship - Paper Copilot","url":"https://papercopilot.com/icml-authorship/icml-2022-authorship/"}]

Let me try a more direct search on arXiv for this paper:

Links: [{"title":"ICML 2026 Call for Papers","url":"https://icml.cc/Conferences/2026/CallForPapers"},{"title":"Recommending Best Paper Awards for ML/AI Conferences via the Isotonic Mechanism","url":"https://arxiv.org/html/2601.15249v2"},{"title":"Stop Automating Peer Review Without Rigorous Evaluation","url":"https://arxiv.org/html/2605.032
…[truncated 3977 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 8
}
```

</details>

---

### Tool call

_source line 205 · 2026-05-29T06:37:33.940167+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "OpenVLA CoRL 2024 PMLR volume 270 publication year 2025 kim25c"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "OpenVLA CoRL 2024 PMLR volume 270 publication year 2025 kim25c"
  }
}
```

</details>

---

### Tool call

_source line 206 · 2026-05-29T06:37:33.940392+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Octo RSS 2024 PMLR proceedings Ghosh authors full list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Octo RSS 2024 PMLR proceedings Ghosh authors full list"
  }
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-29T06:37:33.940597+00:00_

Web search results for query: "RT-2 Vision-Language-Action Models Transfer Web Knowledge Robotic Control arXiv 2307.15818 authors"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://stevengong.co/research-papers/RT2-VisionLanguageAction-Models-Transfer-Web-Knowledge-to-Robotic-Control"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"}]

Based on the search results, here's the information about the RT-2 paper (arXiv 2307.15818):

**Paper Title:** RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control

**Authors:** Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Cho
…[truncated 1035 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 208 · 2026-05-29T06:37:33.940848+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuzhang year venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuzhang year venue"
  }
}
```

</details>

---

### Tool result

_source line 209 · 2026-05-29T06:37:33.941066+00:00_

Web search results for query: "X-VLA arXiv 2510.10274 authors "Jinliang Zheng" year 2025"

Links: [{"title":"[2510.10274] X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://arxiv.org/abs/2510.10274"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model - ADS","url":"https://ui.adsabs.harvard.edu/abs/arXiv:2510.10274"},{"title":"(PDF) X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://www.researchgate.net/publication/396462440_X-VLA_Soft-Prompted_Transformer_as_Scalable_Cross-Embodiment_Vision-Language-Action_Model"},{"title":"GitHub - 2toinf/X-VLA: [ICLR 2026] The offical Implementation of \"Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model\" · GitHub","url":"https://github.com/2toinf/X-VLA"},{"title":"2025-10-14 X-VLA: Soft-Prompted Transformer as Scalable","url":"https://arxiv.org/pdf/2510.10274"},{"title":"dblp: X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model.","url":"https://dblp.org/rec/journals/corr/abs-2510-10274.html"},{"title":"X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2510.10274"},{"title":"Paper page - X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model","url":"https://huggingface.co/papers/2510.10274"}]

I found the paper you were looking for. Here are the details:

**Paper:** X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model

**arXiv ID:** 2510.10274

**Submission Date:** October 11, 2025

**Authors:** Jinliang Zheng, Jianxiong Li, Zhihao Wang, Dongxiu Liu, Xirui Kang, Yuchun Feng, Yinan Zheng, Jiayin Zou, Yilun Chen, Jia Zeng, Ya-Qin Zhang, Jiangmiao Pang, Jingjing Liu, Tai Wang, and Xianyuan Zhan

**Affiliations:** In
…[truncated 875 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool result

_source line 210 · 2026-05-29T06:37:33.941341+00:00_

Web search results for query: "Open X-Embodiment Robotic Learning Datasets RT-X Models ICRA 2024 arXiv 2310.08864"

Links: [{"title":"Open X-Embodiment: Robotic learning datasets and RT-X models - University of Edinburgh Research Explorer","url":"https://www.research.ed.ac.uk/en/publications/open-x-embodiment-robotic-learning-datasets-and-rt-x-models/"},{"title":"Open x-embodiment: Robotic learning datasets and rt-x models - UCSD ARCLAB","url":"https://ucsdarclab.com/autopublication/open-x-embodiment-robotic-learning-datasets-and-rt-x-models/"},{"title":"Open X-Embodiment: Robotic learning datasets and RT-X models | Centre for AI in Assistive Autonomy","url":"https://assistive-autonomy.ed.ac.uk/project/feature-publication-oxe/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2024/05/13/rtx-icra24-rtx/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration>0> - Arizona State University","url":"https://asu.elsevierpure.com/en/publications/open-x-embodiment-robotic-learning-datasets-and-rt-x-models-open-/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://robotics-transformer-x.github.io/"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://arxiv.org/pdf/2310.08864"},{"title":"[2310.08864] Open X-Embodiment: Robotic Learning Datasets and RT-X Models","url":"https://arxiv.org/abs/2310.08864"},{"title":"Open X-Embodiment: Robotic Learning Datasets and RT-X Models : Open X-Embodiment Collaboration0 | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/10611477"}]

Based on the search results, here's information about the Open X-Embodiment project:

## Overview

Open X-Embodiment: Robotic learning datasets and RT-X models was published at the 2024 IEEE International Conference on Robotics and Automat
…[truncated 1261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 211 · 2026-05-29T06:37:33.941591+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.11817 \"See What Matters\" authors Feng Yixu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.11817 \"See What Matters\" authors Feng Yixu"
  }
}
```

</details>

---

### Tool call

_source line 212 · 2026-05-29T06:37:33.941805+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Compressor-VLA arxiv 2511.18950 year submitted 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Compressor-VLA arxiv 2511.18950 year submitted 2025"
  }
}
```

</details>

---

### Tool result

_source line 213 · 2026-05-29T06:37:33.942017+00:00_

Web search results for query: "Perceiver General Perception Iterative Attention Jaegle Andrew ICML 2021"

Links: [{"title":"Perceiver: General Perception with Iterative Attention - researchr publication","url":"https://researchr.org/publication/JaegleGBVZC21"},{"title":"[Quick Review] Perceiver: General Perception with Iterative Attention","url":"https://liner.com/review/perceiver-general-perception-with-iterative-attention"},{"title":"Perceiver: General Perception with Iterative Attention — Paper summary | by Gowthami Somepalli | ML Summaries | Medium","url":"https://medium.com/ml-summaries/perceiver-paper-s-summary-3c589ec74238"},{"title":"[2103.03206] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206"},{"title":"[2103.03206v2] Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/abs/2103.03206v2"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://proceedings.mlr.press/v139/jaegle21a/jaegle21a.pdf"},{"title":"ICML Poster Perceiver: General Perception with Iterative Attention","url":"https://icml.cc/virtual/2021/poster/10291"},{"title":"Perceiver: General Perception with Iterative Attention - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210303206J/abstract"},{"title":"ICML 2021 Perceiver: General Perception with Iterative Attention Spotlight","url":"https://icml.cc/virtual/2021/spotlight/10292"},{"title":"Perceiver: General Perception with Iterative Attention","url":"https://arxiv.org/pdf/2103.03206"}]

I found comprehensive information about this paper. Here are the key details:

## Paper Information

The paper "Perceiver: General Perception with Iterative Attention" was authored by Andrew Jaegle, Felix Gimeno, Andy Brock, Oriol Vinyals, Andrew Zisserman, and João Carreira, and was published in the Proceedings of the 38th International Conference on Machine Learning (ICML 2021) held July 18-24, 2021.

## Core Concept

The Perceiver is a model that bui
…[truncated 924 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 214 · 2026-05-29T06:37:33.942284+00:00_

Web search results for query: "LLaVA-PruMerge arXiv 2403.15388 authors Shang Yuzhang year venue"

Links: [{"title":"[2403.15388v5] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v5"},{"title":"[2403.15388v4] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388v4"},{"title":"[Paper Review] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://velog.io/@euisuk-chung/LLaVA-PruMerge-Adaptive-Token-Reduction-for-Efficient-Large-Multimodal-Models"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/pdf/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/llava-prumerge-adaptive-token-reduction-efficient-large"},{"title":"[2403.15388] LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://arxiv.org/abs/2403.15388"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models","url":"https://www.emergentmind.com/papers/2403.15388"},{"title":"dblp: LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models.","url":"https://dblp.org/rec/journals/corr/abs-2403-15388.html"},{"title":"LLaVA-PruMerge: Adaptive Token Reduction for Efficient ...","url":"https://arxiv.org/pdf/2403.15388v3/"}]

Based on the search results, here is the information for the LLaVA-PruMerge paper (arXiv 2403.15388):

**Authors:** Yuzhang Shang, Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan

**Year:** Submitted on 22 Mar 2024

**Venue:** ICCV 2025

**Title:** LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 215 · 2026-05-29T06:37:33.942547+00:00_

Web search results for query: ""Visual Instruction Tuning" LLaVA authors "Qingyang Wu" NeurIPS 2023"

Links: [{"title":"Visual Instruction Tuning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6dcf277ea32ce3288914faf369fe6de0-Paper-Conference.pdf"},{"title":"Visual Instruction Tuning: LLaVA Model Insights and Benchmarks (2023) - Studocu","url":"https://www.studocu.com/en-us/document/mitchell-technical-college/microbiology/visual-instruction-tuning-llava-model-insights-and-benchmarks-2023/143249240"},{"title":"NeurIPS Poster Visual Instruction Tuning","url":"https://neurips.cc/virtual/2023/poster/70080"},{"title":"Visual Instruction Tuning | OpenReview","url":"https://openreview.net/forum?id=w0H2xGHlkw"},{"title":"LLaVA","url":"https://llava-vl.github.io/"},{"title":"GitHub - haotian-liu/LLaVA: [NeurIPS'23 Oral] Visual Instruction Tuning (LLaVA) built towards GPT-4V level capabilities and beyond. · GitHub","url":"https://github.com/haotian-liu/llava"},{"title":"Visual Instruction Tuning","url":"https://arxiv.org/pdf/2304.08485"},{"title":"[PDF] Visual Instruction Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Visual-Instruction-Tuning-Liu-Li/a5036f31f0e629dc661f120b8c3b1f374d479ab8"}]

Based on the search results, I found comprehensive information about the "Visual Instruction Tuning" paper:

The paper was authored by Haotian Liu, Chunyuan Li, Qingyang Wu, and Yong Jae Lee from the University of Wisconsin–Madison, Microsoft Research, and Columbia University. The paper was presented at NeurIPS 2023 as an Oral presentation.

The paper presents the first attempt to use language-only GPT-4 to generate multimodal language-image instruction-following data, and introduces LLaVA: Large Language and Vision Assistant, an end-to-end trained large multimodal model that connects a vision encoder and an LLM for general-purpose visual and language understanding.

To facilitate future research on visual instruction following, the authors 
…[truncated 334 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 216 · 2026-05-29T06:37:33.942809+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Don't Run with Scissors\" Jabbour arxiv 2510.08464 venue conference accepted 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Don't Run with Scissors\" Jabbour arxiv 2510.08464 venue conference accepted 2025 2026"
  }
}
```

</details>

---

### Tool result

_source line 217 · 2026-05-29T06:37:33.943033+00:00_

Web search results for query: "H2O Heavy-Hitter Oracle Efficient Generative Inference Large Language Models Zhang Zhenyu NeurIPS 2023 arXiv 2306.14048"

Links: [{"title":"[2306.14048] H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://arxiv.org/abs/2306.14048"},{"title":"AI-Powered Paper Summarization about the arXiv paper 2306.14048v1","url":"https://www.summarizepaper.com/en/arxiv-id/2306.14048v1/"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large   Language Models","url":"https://arxiv.org/pdf/2306.14048"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html"},{"title":"Paper page - H_2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models","url":"https://huggingface.co/papers/2306.14048"},{"title":"dblp: H&lt;sub>2&lt;/sub>O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models.","url":"https://dblp.org/rec/journals/corr/abs-2306-14048.html"},{"title":"H$_2$O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/371871295_H_2O_Heavy-Hitter_Oracle_for_Efficient_Generative_Inference_of_Large_Language_Models"},{"title":"H2O: Heavy-Hitter Oracle for Efficient Generative Inference ...","url":"https://proceedings.neurips.cc/paper_files/paper/2023/file/6ceefa7b15572587b78ecfcebb2827f8-Paper-Conference.pdf"}]

I've successfully found the research paper. Here are the key findings:

## Paper Overview

The paper "H₂O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models" was authored by Zhenyu Zhang, Ying Sheng, Tianyi Zhou, Tianlong Chen, Lianmin Zheng, Ruisi Cai, Zhao Song, Yuandong Tian, Christopher Ré, Clark Barrett, Zhangyang Wang, and Beidi Chen.

## Publi
…[truncated 1112 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 4
}
```

</details>

---

### Tool result

_source line 218 · 2026-05-29T06:37:33.943303+00:00_

Web search results for query: "Octo RSS 2024 PMLR proceedings Ghosh authors full list"

Links: [{"title":"A Closer Look at the Limitations of Instruction Tuning","url":"https://proceedings.mlr.press/v235/ghosh24a.html"},{"title":"LoRA+: Efficient Low Rank Adaptation of Large Models","url":"https://proceedings.mlr.press/v235/hayou24a.html"},{"title":"What matters in building vision–language–action models for generalist robots | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-025-01168-7"},{"title":"Towards Achieving Sub-linear Regret and Hard Constraint Violation in Model-free RL","url":"https://proceedings.mlr.press/v238/ghosh24a.html"},{"title":"Proceedings of Machine Learning Research | Proceedings of The 27th International Conference on Artificial Intelligence and Statistics Held in Palau de Congressos, Valencia, Spain on 02-04 May 2024 Published as Volume 238 by the Proceedings of Machine Learning Research on 18 April 2024. Volume Edited by: Sanjoy Dasgupta Stephan Mandt Yingzhen Li Series Editors: Neil D. Lawrence","url":"https://proceedings.mlr.press/v238/"},{"title":"Author Correction: Exploring online public survey lifestyle datasets with statistical analysis, machine learning and semantic ontology","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11810986/"},{"title":"Author Information · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/information/authorinfo/"}]

Based on the search results, I found a reference to the Octo paper from RSS 2024. The paper "Octo: an open-source generalist robot policy" was presented at Robotics: Science and Systems (RSS) 2024 with authors including Ghosh, D. et al.

However, the search results don't provide the complete full list of all authors for the Octo RSS 2024 paper in PMLR proceedings format. The reference found appears in a Nature Machine Intelligence article citing the work, but it doesn't include the full author list. The Octo paper may not be formally published
…[truncated 430 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 219 · 2026-05-29T06:37:33.943552+00:00_

Web search results for query: "OpenVLA CoRL 2024 PMLR volume 270 publication year 2025 kim25c"

Links: [{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://proceedings.mlr.press/v270/kim25c.html"},{"title":"GitHub - mlresearch/v270: Proceedings of CoRL 2024","url":"https://github.com/mlresearch/v270"},{"title":"CoRL.2024 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/CoRL.2024"},{"title":"[PDF] OpenVLA: An Open-Source Vision-Language-Action Model | Semantic Scholar","url":"https://www.semanticscholar.org/paper/OpenVLA:-An-Open-Source-Vision-Language-Action-Kim-Pertsch/8f9ceb5ffad8e7a066dfc9d9aaa5153b714740ee"},{"title":"OpenVLA: An Open-Source Vision-Language-Action Model","url":"https://arxiv.org/pdf/2406.09246"},{"title":"Enhancing Linguistic Generalization of VLA: Fine-Tuning OpenVLA via Synthetic Instruction Augmentation","url":"https://arxiv.org/pdf/2603.16044"}]

Based on the search results, I found the paper you're looking for:

**OpenVLA: An Open-Source Vision-Language-Action Model** was published in Proceedings of The 8th Conference on Robot Learning (CoRL 2024), PMLR Volume 270, pages 2679-2713, in 2025. The paper citation is kim25c.

OpenVLA is a 7B-parameter open-source VLA trained on a diverse collection of 970k real-world robot demonstrations. OpenVLA builds on a Llama 2 language model combined with a visual encoder that fuses pretrained features from DINOv2 and SigLIP.

The paper is authored by Kim, Moo Jin and multiple co-authors including Pertsch, Karamcheti, Xiao, and others, with the proceedings published on January 12, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 3
}
```

</details>

---

### Tool call

_source line 220 · 2026-05-29T06:37:33.943782+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Efficient Streaming Language Models Attention Sinks Xiao Guangxuan ICLR 2024 arXiv 2309.17453"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Efficient Streaming Language Models Attention Sinks Xiao Guangxuan ICLR 2024 arXiv 2309.17453"
  }
}
```

</details>

---

### Tool result

_source line 221 · 2026-05-29T06:37:33.943985+00:00_

Web search results for query: "arxiv 2605.11817 "See What Matters" authors Feng Yixu"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/html/2605.11817"},{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"Advancing a Vision Foundation Model for Ming-Style Furniture Image Segmentation: A New Dataset and Method","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11722721/"},{"title":"Maximum Value Matters: Finding Hot Topics in Scholarly Fields","url":"https://arxiv.org/pdf/1710.06637"}]

Based on the search results, I found the paper you're looking for:

**Title:** "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model"

**Authors:** &lt;cite index="1-6">Yixu Feng, Zinan Zhao, Yanxiang Ma, Chenghao Xia, Chengbin Du, Yunke Wang, and Chang Xu

**ArXiv ID:** 2605.11817

**Overview:** The paper addresses Vision-Language-Action (VLA) models and their high computational cost that hinders real-time deployment in robotics manipulation. The authors propose the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA.

The paper was submitted on May 12, 2026, with a revised version (v2) on May 17, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 222 · 2026-05-29T06:37:33.944213+00:00_

Web search results for query: "Compressor-VLA arxiv 2511.18950 year submitted 2025"

Links: [{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/pdf/2511.18950"},{"title":"[2511.18950] Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/abs/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://arxiv.org/html/2511.18950"},{"title":"Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation","url":"https://chatpaper.com/paper/212383"},{"title":"EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2506.10100"}]

Based on the search results, Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation is a paper with arxiv ID 2511.18950.

Regarding the submission year: The paper proposes a framework consisting of two token compression modules: a Semantic Task Compressor (STC) that distills holistic, task-relevant context, and a Spatial Refinement Compressor (SRC) that preserves fine-grained spatial details. Based on the arxiv ID format (2511.18950), this indicates the paper was submitted in November 2025 (the "25" refers to 2025, and "11" refers to November).

The paper addresses the significant computational overhead of processing redundant visual tokens in Vision-Language-Action (VLA) models, proposing a novel hybrid instruction-conditioned token compression framework designed for efficient, task-oriented compression of visual information.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 223 · 2026-05-29T06:37:33.944447+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CALVIN Benchmark Language-Conditioned Policy Learning Long-Horizon Robot Manipulation Mees Oier IEEE RA-L 2022 arXiv 2112.03227"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CALVIN Benchmark Language-Conditioned Policy Learning Long-Horizon Robot Manipulation Mees Oier IEEE RA-L 2022 arXiv 2112.03227"
  }
}
```

</details>

---

### Tool call

_source line 224 · 2026-05-29T06:37:33.944667+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Diffusion Policy Visuomotor Policy Learning Action Diffusion Chi Cheng RSS 2023 arXiv 2303.04137"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Diffusion Policy Visuomotor Policy Learning Action Diffusion Chi Cheng RSS 2023 arXiv 2303.04137"
  }
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-29T06:37:33.944966+00:00_

Now I have all the information needed. Let me also confirm the ICLR 2022 paper's exact title formatting — it says "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" (plural "Reorganizations"), while the bib entry says "Token Reorganizations" — let me check if the cited title matches exactly.

The bib entry states the title as: "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" — this matches the actual title found on arXiv and OpenReview.

Here is the structured verification checklist:

---

## Reference Verification Checklist

### 1. chen2024fastv
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Liang Chen (note: surname is Chen, given name is Liang) |
| Title | MATCH | "An Image is Worth 1/2 Tokens After Layer 2: Plug-and-Play Inference Acceleration for Large Vision-Language Models" |
| Year | MATCH | 2024 |
| Venue | MATCH | ECCV 2024 (Oral) |
| arXiv ID | MATCH | 2403.06764 |
| Issues | None | |

---

### 2. xu2025vlacache
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Siyu Xu (GitHub username: siyuhsu) |
| Title | MATCH | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" |
| Year | MATCH | 2025 (arXiv Feb 2025, accepted NeurIPS 2025) |
| Venue | MATCH | NeurIPS 2025 |
| arXiv ID | 2502.02175 (not listed in bib entry, but correct if needed) |
| Issues | None | |

---

### 3. cheng2026vlaiap
| Field | Status | Notes |
|-------|--------|-------|
| Exists | YES | |
| Authors | MATCH | First author is Jintao Cheng |
| Title | MATCH | "VLA-IAP: Training-Free Visual Token Pruning via Interaction Alignment for Vision-Language-Action Models" |
| Year | MATCH | 2026 (submitted March 24, 2026) |
| Venue | N/A | arXiv preprint only (no conference acceptance found) |
| arXiv ID | MATCH | 2603.22991 |
| Issues | None | |

---

### 4. r
…[truncated 2313 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 41
}
```

</details>

---

### Tool call

_source line 226 · 2026-05-29T06:37:33.945251+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Are Transformers Effective for Time Series Forecasting\" Zeng Ailing AAAI 2023 arXiv 2205.13504"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Are Transformers Effective for Time Series Forecasting\" Zeng Ailing AAAI 2023 arXiv 2205.13504"
  }
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-29T06:37:33.945477+00:00_

Web search results for query: ""Don't Run with Scissors" Jabbour arxiv 2510.08464 venue conference accepted 2025 2026"

Links: [{"title":"[2510.08464] Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered","url":"https://arxiv.org/abs/2510.08464"},{"title":"Running With Scissors - Therapy by Dr. Nathan Miller","url":"https://www.nathanmillertherapy.com/give-this-some-thought/running-with-scissors"},{"title":"Don’t Run With Scissors | Theo Heartist","url":"https://theoheartist.com/2021/06/14/dont-run-with-scissors/"},{"title":"Don't run with scissors: young children's knowledge of home safety rules | Request PDF","url":"https://www.researchgate.net/publication/12148912_Don't_run_with_scissors_young_children's_knowledge_of_home_safety_rules"},{"title":"Don't run with scissors: young children's knowledge of home safety rules - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/11181886/"},{"title":"Workshop Safety, a.k.a. Don't Run With Scissors","url":"https://www.kitplanes.com/running-with-scissors-shop-safety/"},{"title":"Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered | OpenReview","url":"https://openreview.net/forum?id=c8g57pKdXD"},{"title":"Modeling and predicting single-cell multi-gene perturbation responses with scLAMBDA","url":"https://www.biorxiv.org/content/10.1101/2024.12.04.626878.full.pdf"},{"title":"Prompt injection attacks on vision-language models for surgical decision support","url":"https://www.medrxiv.org/content/10.1101/2025.07.16.25331645.full.pdf"},{"title":"Large Language Models for Detecting CONSORT Guideline Compliance in Published Randomized Clinical Trials: A Cross-Sectional Evaluation Study","url":"https://www.medrxiv.org/content/10.1101/2025.10.03.25337291.full.pdf"}]

Based on the search results, I found information about the paper "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" (arxiv 2510.08464):

The paper addresses Vision-Language-Action (VLA) models and sh
…[truncated 1151 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 228 · 2026-05-29T06:37:33.945734+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Embracing Negative Results in Machine Learning\" Bouthillier Xavier ICML 2024 arXiv 2406.03980"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Embracing Negative Results in Machine Learning\" Bouthillier Xavier ICML 2024 arXiv 2406.03980"
  }
}
```

</details>

---

### Tool result

_source line 229 · 2026-05-29T06:37:33.945951+00:00_

Web search results for query: "Efficient Streaming Language Models Attention Sinks Xiao Guangxuan ICLR 2024 arXiv 2309.17453"

Links: [{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://proceedings.iclr.cc/paper_files/paper/2024/hash/5e5fd18f863cbe6d8ae392a93fd271c9-Abstract-Conference.html"},{"title":"GitHub - mit-han-lab/streaming-llm: [ICLR 2024] Efficient Streaming Language Models with Attention Sinks · GitHub","url":"https://github.com/mit-han-lab/streaming-llm"},{"title":"Efficient Streaming Language Models with Attention Sinks | OpenReview","url":"https://openreview.net/forum?id=NG7sS51zVF"},{"title":"[PDF] Efficient Streaming Language Models with Attention Sinks | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Efficient-Streaming-Language-Models-with-Attention-Xiao-Tian/fdc53c2c10742464087c0525f77e32604827a21d"},{"title":"[2309.17453] Efficient Streaming Language Models with Attention Sinks","url":"https://arxiv.org/abs/2309.17453"},{"title":"efficient streaming language models","url":"https://proceedings.iclr.cc/paper_files/paper/2024/file/5e5fd18f863cbe6d8ae392a93fd271c9-Paper-Conference.pdf"},{"title":"Efficient Streaming Language Models with Attention Sinks","url":"https://hanlab.mit.edu/projects/streamingllm"},{"title":"Efficient streaming language models with at","url":"https://arxiv.org/pdf/2309.17453"},{"title":"Efficient Streaming Language Models with Attention Sinks Paper written by:","url":"https://minjiazhang.github.io/courses/sp24-resource/streaming-attention-sink-pre.pdf"}]

I found the paper you're looking for! Here's a summary of the search results:

"Efficient Streaming Language Models with Attention Sinks" is a paper by Guangxuan Xiao, Yuandong Tian, Beidi Chen, Song Han, and Mike Lewis, published at ICLR 2024. The paper is also available on arXiv as arXiv 2309.17453.

**Key Problem and Solution:**

The paper addresses challenges in deploying LLMs for streaming applications like multi-round di
…[truncated 1032 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 230 · 2026-05-29T06:37:33.946230+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "SparseVILA Khaki \"Decoupled\" OR \"Decoupling\" exact title ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "SparseVILA Khaki \"Decoupled\" OR \"Decoupling\" exact title ICCV 2025"
  }
}
```

</details>

---

### Tool call

_source line 231 · 2026-05-29T06:37:33.946483+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv 2605.11817 \"See What Matters\" ICML 2026 poster accepted"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv 2605.11817 \"See What Matters\" ICML 2026 poster accepted"
  }
}
```

</details>

---

### Tool result

_source line 232 · 2026-05-29T06:37:33.946694+00:00_

Web search results for query: "CALVIN Benchmark Language-Conditioned Policy Learning Long-Horizon Robot Manipulation Mees Oier IEEE RA-L 2022 arXiv 2112.03227"

Links: [{"title":"[2112.03227] CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/abs/2112.03227"},{"title":"[2112.03227v2] CALVIN: A Benchmark for Language-conditioned Policy Learning for Long-horizon Robot Manipulation Tasks","url":"https://arxiv.org/abs/2112.03227v2"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv211203227M/abstract"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for   Long-Horizon Robot Manipulation Tasks","url":"https://arxiv.org/pdf/2112.03227"},{"title":"CALVIN: Benchmark for Language-Driven Robot Tasks","url":"https://www.emergentmind.com/papers/2112.03227"},{"title":"Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"http://ais.informatik.uni-freiburg.de/publications/papers/mees22rsspi.pdf"},{"title":"(PDF) CALVIN: A Benchmark for Language-conditioned Policy Learning for Long-horizon Robot Manipulation Tasks","url":"https://www.researchgate.net/publication/356817042_CALVIN_A_Benchmark_for_Language-conditioned_Policy_Learning_for_Long-horizon_Robot_Manipulation_Tasks"}]

I found the paper you're searching for. Here's the information about it:

**CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks**

The paper is authored by Oier Mees, Lukas Hermann, Erick Rosete-Beas, and Wolfram Burgard.

**Overview:**
CALVIN (Composing Actions from Language and Vision) is an open-source simulated benchmark to learn long-horizon language-conditioned tasks. The aim is to develop agents that can solve many robotic manipulation tasks over a long horizon, from onboard sensors, and specified only
…[truncated 823 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 233 · 2026-05-29T06:37:33.946924+00:00_

Web search results for query: "Diffusion Policy Visuomotor Policy Learning Action Diffusion Chi Cheng RSS 2023 arXiv 2303.04137"

Links: [{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"[2303.04137v1] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v1"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"[2303.04137v3] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v3"},{"title":"[2303.04137v5] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v5"},{"title":"[2303.04137v4] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137v4"},{"title":"Paper page - Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://huggingface.co/papers/2303.04137"},{"title":"[2303.04137] Diffusion Policy - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/2303.04137"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"}]

I found the paper you're searching for! Here's the information:

## Diffusion Policy: Visuomotor Policy Learning via Action Diffusion

This paper introduces Diffusion Policy, a new way of generating robot behavior by representing a robot's visuomotor policy as a conditional denoising diffusion process.

**Authors:** Cheng Chi, Siyuan Feng, Yilun Du, Zhenjia Xu, Eric Cousineau, Benjamin Burchfiel, and Shuran Song (with later versions adding Russ Tedrake)

**Publication:** Robotics: Science and Systems (RSS) 2023

**arXiv Identifier:**
…[truncated 930 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 2
}
```

</details>

---

### Tool result

_source line 234 · 2026-05-29T06:37:33.947195+00:00_

Web search results for query: ""Are Transformers Effective for Time Series Forecasting" Zeng Ailing AAAI 2023 arXiv 2205.13504"

Links: [{"title":"Yes, Transformers are Effective for Time Series Forecasting (+ Autoformer)","url":"https://huggingface.co/blog/autoformer"},{"title":"Are Transformers Effective for Time Series Forecasting? - R Discovery","url":"https://discovery.researcher.life/article/are-transformers-effective-for-time-series-forecasting/55dd0976743c3dbea291291e7d41dc3f"},{"title":"Aaai","url":"https://ojs.aaai.org/index.php/AAAI/citationstylelanguage/get/apa?submissionId=26317&publicationId=24597"},{"title":"Are Transformers Effective for Time Series Forecasting? | Request PDF","url":"https://www.researchgate.net/publication/371915865_Are_Transformers_Effective_for_Time_Series_Forecasting"},{"title":"GitHub - cure-lab/LTSF-Linear: [AAAI-23 Oral] Official implementation of the paper \"Are Transformers Effective for Time Series Forecasting?\" · GitHub","url":"https://github.com/cure-lab/LTSF-Linear"},{"title":"Are transformers effective for time series forecasting? | Proceedings of the Thirty-Seventh AAAI Conference on Artificial Intelligence and Thirty-Fifth Conference on Innovative Applications of Artificial Intelligence and Thirteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v37i9.26317"},{"title":"Are Transformers Effective for Time Series Forecasting?","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26317/26089"},{"title":"[PDF] Are Transformers Effective for Time Series Forecasting? | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Are-Transformers-Effective-for-Time-Series-Zeng-Chen/5f404dbba07619cc7f28d75d03f124a52290046e"},{"title":"Are Transformers Effective for Time Series Forecasting? | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/26317"}]

I've found the paper you're looking for. He
…[truncated 936 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 235 · 2026-05-29T06:37:33.947445+00:00_

Web search results for query: ""Embracing Negative Results in Machine Learning" Bouthillier Xavier ICML 2024 arXiv 2406.03980"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"dblp: Position: Embracing Negative Results in Machine Learning.","url":"https://dblp.org/rec/journals/corr/abs-2406-03980.html"},{"title":"Negative chemical data boosts language models in reaction outcome prediction","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12164950/"}]

I found the paper! Here are the search results for "Embracing Negative Results in Machine Learning" with arXiv ID 2406.03980 from ICML 2024:

**Paper Details:**
- Authors: Florian Karl, Lukas Malte Kemeter, Gabriel Dax, and Paulina Sierak
- arXiv: 2406.03980v1, submitted June 6, 2024
- Published in Proceedings of the 41st International Conference on Machine Learning, PMLR 235:23256-23265, 2024

**Main Argument:**
The position paper argues that predictive performance alone is not a good indicator for the worth of a publication, and us
…[truncated 765 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 236 · 2026-05-29T06:37:33.947686+00:00_

Web search results for query: "SparseVILA Khaki "Decoupled" OR "Decoupling" exact title ICCV 2025"

Links: [{"title":"[2510.17777] SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/abs/2510.17777"},{"title":"SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://arxiv.org/pdf/2510.17777"},{"title":"ICCV Poster SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference","url":"https://iccv.thecvf.com/virtual/2025/poster/1739"},{"title":"Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering","url":"https://arxiv.org/pdf/2603.18636"},{"title":"ICCV Poster DecAD: Decoupling Anomalies in Latent Space for Multi-Class Unsupervised Anomaly Detection","url":"https://iccv.thecvf.com/virtual/2025/poster/362"}]

I found the paper you're looking for! 

SparseVILA: Decoupling Visual Sparsity for Efficient VLM Inference is authored by Samir Khaki, Junxian Guo, Jiaming Tang, Shang Yang, Yukang Chen, Konstantinos Plataniotis, Yao Lu, Song Han, and Zhijian Liu. 

SparseVILA presents a new paradigm for efficient VLM inference that decouples visual sparsity across the prefilling and decoding stages. The method achieves up to 4.0 times faster prefilling, 2.5 times faster decoding, and an overall 2.6 times end-to-end speedup on long-context video tasks while improving accuracy on document-understanding and reasoning tasks.

The paper has been published at ICCV 2025 and is available on arXiv (paper ID: 2510.17777).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 237 · 2026-05-29T06:37:33.947913+00:00_

Web search results for query: "arxiv 2605.11817 "See What Matters" ICML 2026 poster accepted"

Links: [{"title":"[2605.11817] See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model","url":"https://arxiv.org/abs/2605.11817"},{"title":"ICML 2026 Peer Review FAQ","url":"https://icml.cc/Conferences/2026/PeerReviewFAQ"},{"title":"Stop Automating Peer Review Without Rigorous Evaluation","url":"https://arxiv.org/html/2605.03202v1"},{"title":"MLLMs Know Where to Look: Training-free Perception of Small Visual   Details with Multimodal LLMs","url":"https://arxiv.org/pdf/2502.17422"},{"title":"A Two-Stage Approach to Important Area Detection in Gathering Place Using a Novel Multi-Input Attention Network","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749720/"},{"title":"OpenNovelty: An LLM-powered Agentic System for Verifiable Scholarly Novelty Assessment","url":"https://arxiv.org/pdf/2601.01576"}]

Based on the search results, I found information about the paper arxiv 2605.11817:

The paper titled "See What Matters: Differentiable Grid Sample Pruning for Generalizable Vision-Language-Action Model" is by Yixu Feng and 6 other authors. The paper addresses Vision-Language-Action (VLA) models in robotics manipulation, which have shown promise but have high computational costs that hinder real-time deployment.

The paper proposes the Differentiable Grid Sampler (GridS), a plug-and-play module that performs task-aware, continuous resampling of visual tokens in VLA. By adaptively predicting a minimal set of salient coordinates and extracting features via differentiable interpolation, GridS preserves essential spatial information while achieving drastic compression.

The paper was submitted to arXiv on May 12, 2026 with the latest revision on May 17, 2026.

However, I was unable to find specific information in the search results confirming whether this paper was accepted as a poster at ICML 2026. The search results show the arXiv pap
…[truncated 170 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 238 · 2026-05-29T06:37:33.948185+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DINOv2 Oquab 2024 TMLR Transactions Machine Learning Research published venue"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DINOv2 Oquab 2024 TMLR Transactions Machine Learning Research published venue"
  }
}
```

</details>

---

### Tool call

_source line 239 · 2026-05-29T06:37:33.948412+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RT-2 CoRL 2023 proceedings first author Zitkovich Brohan"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RT-2 CoRL 2023 proceedings first author Zitkovich Brohan"
  }
}
```

</details>

---

### Tool call

_source line 240 · 2026-05-29T06:37:33.948631+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "\"Position: Embracing Negative Results\" Bouthillier Xavier author ICML 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "\"Position: Embracing Negative Results\" Bouthillier Xavier author ICML 2024"
  }
}
```

</details>

---

### Tool call

_source line 241 · 2026-05-29T06:37:33.948845+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "CALVIN Mees 2022 IEEE RA-L Robotics Automation Letters publication year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "CALVIN Mees 2022 IEEE RA-L Robotics Automation Letters publication year"
  }
}
```

</details>

---

### Tool call

_source line 242 · 2026-05-29T06:37:33.949054+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2305.17455 CrossGET authors Shi Dachuan first author list"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2305.17455 CrossGET authors Shi Dachuan first author list"
  }
}
```

</details>

---

### Tool result

_source line 243 · 2026-05-29T06:37:33.949287+00:00_

Web search results for query: "RT-2 CoRL 2023 proceedings first author Zitkovich Brohan"

Links: [{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"Papers — CoRL 2023","url":"https://www.corl2023.org/papers"},{"title":"Real-time open-vocabulary perception for mobile robots on edge devices: a systematic analysis of the accuracy-latency trade-off - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12583037/"},{"title":"Advancing general robotic manipulation with multimodal foundation models: An embodied AI paradigm | Science China Technological Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11431-024-2910-3"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"}]

Based on the search results, I found the information about the RT-2 paper from the CoRL 2023 proceedings. 

Brianna Zitkovich is listed as the first author of the RT-2 paper in the CoRL 2023 proceedings, with Anthony Brohan among the co-authors. 

The full title is "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control" and it was published in the Proceedings of The 7th Conference on Robot Learning, in Proceedings of Machine Learning Research 229:2165-2183.

The authors are listed in alphabetical order, with contributions listed in Appendix A.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 244 · 2026-05-29T06:37:33.949540+00:00_

Web search results for query: "DINOv2 Oquab 2024 TMLR Transactions Machine Learning Research published venue"

Links: [{"title":"DINOv2: Learning Robust Visual Features Without Supervision | ML Anthology","url":"https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/"},{"title":"Published in Transactions on Machine Learning Research (05/2024)","url":"https://openreview.net/pdf/129f9aa6abb956d6b52bcae0458ab67f1ebad847.pdf"},{"title":"Transactions on Machine Learning Research on X: \"Outstanding Finalist 2: “DINOv2: Learning Robust Visual Features without Supervision,\" by Maxime Oquab, Timothée Darcet (@TimDarcet), Théo Moutakanni (@TheoMoutakanni) et al. 5/n https://t.co/XBQJk03R8R\" / X","url":"https://x.com/TmlrOrg/status/1869867717953483138"},{"title":"A generalised vision transformer-based self-supervised model for diagnosing and grading prostate cancer using histological images | Prostate Cancer and Prostatic Diseases","url":"https://www.nature.com/articles/s41391-025-00957-w"},{"title":"dblp: Transactions on Machine Learning Research, Volume 2024","url":"https://dblp.org/db/journals/tmlr/tmlr2024.html"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | by Jim Canary | Medium","url":"https://medium.com/@jimcanary/dinov2-learning-robust-visual-features-without-supervision-bfd1cd94cbdd"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | OpenReview","url":"https://openreview.net/forum?id=a68SUt6zFt"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"}]

Based on the search results, I found information about the DINOv2 paper by Oquab et al. and its publication venue:

DINOv2: Learning Robust Visual Features Without Supervision was published in Transactions on Machine Learning Research in 2024. The paper was authored by Maxime Oquab, 
…[truncated 745 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 245 · 2026-05-29T06:37:33.949778+00:00_

Web search results for query: "arXiv 2305.17455 CrossGET authors Shi Dachuan first author list"

Links: [{"title":"[2305.17455] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/abs/2305.17455"},{"title":"GitHub - sdc17/CrossGET: [ICML 2024] CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers · GitHub","url":"https://github.com/sdc17/crossget"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | Request PDF","url":"https://www.researchgate.net/publication/371136150_CrossGET_Cross-Guided_Ensemble_of_Tokens_for_Accelerating_Vision-Language_Transformers"},{"title":"dblp: Dachuan Shi","url":"https://dblp.org/pid/283/0549.html"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers","url":"https://arxiv.org/html/2305.17455"},{"title":"CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers | OpenReview","url":"https://openreview.net/forum?id=CSIfCpXhCF"}]

Based on the search results, here are the authors of the CrossGET paper (arXiv 2305.17455) in order:

1. Dachuan Shi
2. Chaofan Tao
3. Anyi Rao
4. Zhendong Yang
5. Chun Yuan
6. Jiaqi Wang

Dachuan Shi is the first author, and the paper presents Cross-Guided Ensemble of Tokens (CrossGET), a general acceleration framework for vision-language Transformers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 246 · 2026-05-29T06:37:33.950016+00:00_

Web search results for query: ""Position: Embracing Negative Results" Bouthillier Xavier author ICML 2024"

Links: [{"title":"Position: Embracing Negative Results in Machine Learning | OpenReview","url":"https://openreview.net/forum?id=3RXAiU7sss"},{"title":"ICML Poster Position: Embracing Negative Results in Machine Learning","url":"https://icml.cc/virtual/2024/poster/35063"},{"title":"[ICML 2024] Position: Embracing Negative Results in Machine Learning - YouTube","url":"https://www.youtube.com/watch?v=JDP6cXWmChI"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/pdf/2406.03980"},{"title":"Position: Embracing Negative Results in Machine Learning","url":"https://proceedings.mlr.press/v235/karl24a.html"},{"title":"ICML 2024 Schedule","url":"https://icml.cc/virtual/2024/calendar"},{"title":"[2406.03980] Position: Embracing Negative Results in Machine Learning","url":"https://arxiv.org/abs/2406.03980"},{"title":"(PDF) Position: Embracing Negative Results in Machine Learning","url":"https://www.researchgate.net/publication/381226301_Position_Embracing_Negative_Results_in_Machine_Learning"},{"title":"Negativity towards negative results: a discussion of the disconnect between scientific worth and scientific culture","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3917235/"}]

I found information about the paper "Position: Embracing Negative Results in Machine Learning" presented at ICML 2024. However, I should note that the authors listed in the search results are **Florian Karl, Malte Kemeter, Gabriel Dax, and Paulina Sierak**, not Xavier Bouthillier as mentioned in your query.

Here's what the paper is about:

The paper was published at ICML 2024, and it argues that predictive performance alone is not a good indicator for the worth of a publication, and that using it as such fosters problems like inefficiencies of the machine learning research community and wrong incentives for researchers.

The authors call for the publi
…[truncated 514 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 247 · 2026-05-29T06:37:33.950279+00:00_

Web search results for query: "CALVIN Mees 2022 IEEE RA-L Robotics Automation Letters publication year"

Links: [{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks","url":"https://github.com/mees/calvin?tab=readme-ov-file"},{"title":"GitHub - mees/calvin: CALVIN - A benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks · GitHub","url":"https://github.com/mees/calvin"},{"title":"CALVIN: A Benchmark for Language-Conditioned Policy Learning for Long-Horizon Robot Manipulation Tasks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2022IRAL....7.7327M/abstract"},{"title":"IEEE ROBOTICS AND AUTOMATION LETTERS. PREPRINT VERSION. ACCEPTED JULY, 2022 1","url":"https://arxiv.org/pdf/2204.06252"},{"title":"RA-L Paper Awards - IEEE Robotics and Automation Society Website","url":"https://www.ieee-ras.org/publications/ra-l/ra-l-paper-awards/"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Calvin:+a+benchmark+for+language-conditioned+policy+learning+for+long-horizon+robot+manipulation+tasks&amp=&author=O+Mees&amp=&author=L+Hermann&amp=&author=E+Rosete-Beas&amp=&publication_year=2022&amp=&journal=IEEE+Robotics+and+Automation+Letters&amp=&pages=7327-7334&amp=&doi=10.1109/LRA.2022.3180108"},{"title":"Oier Mees","url":"https://www.oiermees.com/"},{"title":"IEEE Robotics and Automation Letters (RA-L)","url":"https://www.myhuiban.com/journal/1037?lang=en_us"}]

Based on the search results, the CALVIN paper by Mees et al. was published in IEEE Robotics and Automation Letters (RA-L) in 2022, specifically in volume 7, number 3, pages 7327-7334. More specifically, the publication was in July 2022.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool result

_source line 248 · 2026-05-29T06:37:33.950643+00:00_

Here is the structured verification checklist for all 8 references:

---

## Reference Verification Checklist

### 1. liu2025vlapruner — VLA-Pruner
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference" — exact match |
| Authors match | YES | First author is Liu, Ziyan — confirmed |
| Year match | **ISSUE** | arXiv submission date is **Nov 2025**, but the arXiv ID prefix `2511` means Nov 2025. The bib key says 2025, which is technically correct for the submission year. However, the latest revision is Feb 2026. The year 2025 is acceptable as the original submission year. |
| Venue match | N/A | No venue claimed (arXiv preprint) |
| arXiv ID match | YES | 2511.16449 confirmed |

**Verdict: OK.** No issues.

---

### 2. shang2024prumerge — LLaVA-PruMerge
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" — exact match |
| Authors match | YES | Shang, Yuzhang is first author. Co-authors: Mu Cai, Bingxin Xu, Yong Jae Lee, Yan Yan |
| Year match | **ISSUE** | Bib key says `2024`, venue listed as ICCV 2025. The arXiv submission is Mar 2024, but the published venue is **ICCV 2025**. The year in the bibliography entry should be **2025** to match the publication venue. |
| Venue match | YES | ICCV 2025 confirmed via CVF Open Access |
| arXiv ID | Not given in entry | arXiv: 2403.15388 |

**Verdict: Year inconsistency.** The bib key `shang2024prumerge` implies year 2024, but the venue is ICCV 2025. The bibliography year should be **2025**.

---

### 3. liu2023llava — Visual Instruction Tuning
| Check | Result | Notes |
|-------|--------|-------|
| Exists | YES | |
| Title match | YES | "Visual Instruction Tuning" — exact match |
| Authors match | YES | Liu, Haotian; Li, Chunyuan; Wu, Qingyang; Lee, Yong Jae —
…[truncated 4507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 43
}
```

</details>

---

### Tool call

_source line 249 · 2026-05-29T06:37:33.950914+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arXiv 2307.15818 RT-2 author list order Brohan first Zitkovich"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arXiv 2307.15818 RT-2 author list order Brohan first Zitkovich"
  }
}
```

</details>

---

### Tool call

_source line 250 · 2026-05-29T06:37:33.951158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "DINOv2 TMLR 2024 publication date month year openreview"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "DINOv2 TMLR 2024 publication date month year openreview"
  }
}
```

</details>

---

### Tool call

_source line 251 · 2026-05-29T06:37:33.951385+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Diffusion Policy Chi Cheng RSS 2023 or IJRR venue proceedings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Diffusion Policy Chi Cheng RSS 2023 or IJRR venue proceedings"
  }
}
```

</details>

---

### Tool result

_source line 252 · 2026-05-29T06:37:33.951593+00:00_

Web search results for query: "arXiv 2307.15818 RT-2 author list order Brohan first Zitkovich"

Links: [{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"[2307.15818v1] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818v1"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"}]

Based on the search results, the author list for arXiv paper 2307.15818 (RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control) begins with Anthony Brohan as the first author and ends with Brianna Zitkovich as the last author.

Additionally, the authors are listed in alphabetical order, with a contribution statement in the paper appendix.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-29T06:37:33.951810+00:00_

Web search results for query: "DINOv2 TMLR 2024 publication date month year openreview"

Links: [{"title":"DINOv2: Learning Robust Visual Features without Supervision | OpenReview","url":"https://openreview.net/forum?id=a68SUt6zFt"},{"title":"DINOv2: Learning Robust Visual Features Without Supervision | ML Anthology","url":"https://mlanthology.org/tmlr/2024/oquab2024tmlr-dinov2/"},{"title":"Published in Transactions on Machine Learning Research (01/2024)","url":"https://arxiv.org/pdf/2304.07193"},{"title":"HAL Id: hal-04376640 https://hal.science/hal-04376640v2 Submitted on 2 Feb 2024","url":"https://hal.science/hal-04376640v2/file/CVPR_2023_dinov2%20(4).pdf"},{"title":"Accepted papers at TMLR on X: \"DINOv2: Learning Robust Visual Features without Supervision Maxime Oquab, Timothée Darcet, Théo Moutakanni et al.. Action editor: Abhishek Kumar. https://t.co/M0YHJp3SuI #supervised #visual #features\" / X","url":"https://x.com/TmlrPub/status/1749446940125757691"},{"title":"A generalised vision transformer-based self-supervised model for diagnosing and grading prostate cancer using histological images | Prostate Cancer and Prostatic Diseases","url":"https://www.nature.com/articles/s41391-025-00957-w"},{"title":"[2304.07193] DINOv2: Learning Robust Visual Features without Supervision","url":"https://arxiv.org/abs/2304.07193"},{"title":"DINOv2: Learning Robust Visual Features without Supervision | by Jim Canary | Medium","url":"https://medium.com/@jimcanary/dinov2-learning-robust-visual-features-without-supervision-bfd1cd94cbdd"},{"title":"Explainable self-supervised learning for medical image diagnosis based on DINO V2 model and semantic search","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12402508/"}]

The DINOv2 paper was published in TMLR on January 11, 2024. The OpenReview page is available at openreview.net/forum?id=a68SUt6zFt.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-29T06:37:33.952184+00:00_

Here is the structured verification checklist for all 8 entries:

---

## Reference Verification Checklist

### 1. li2024cogact — CogACT
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author is Qixiu Li (Li, Qixiu). Confirmed. |
| Title | MATCH | "CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation" |
| Year | MATCH | Submitted 2024-11-29 |
| Venue | N/A | No venue claimed in the bib entry (arXiv preprint) |
| arXiv ID | MATCH | 2411.19650 |
| Issues | None | |

### 2. zheng2025xvla — X-VLA
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author is Jinliang Zheng (Zheng, Jinliang). Confirmed. |
| Title | MATCH | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model" |
| Year | **ISSUE** | arXiv submission date is **2025-10-11** (arXiv ID 2510.xxxxx = October 2025). The bib key says "2025" which is correct for the arXiv posting. However, ICLR 2026 proceedings would formally be year 2026. If the bib entry lists year=2025, it should be updated to **2026** to match the ICLR publication year. |
| Venue | MATCH | GitHub repo and metadata confirm "[ICLR 2026]" acceptance. |
| arXiv ID | MATCH | 2510.10274 |
| Issues | **Year ambiguity**: arXiv posted 2025, but venue is ICLR 2026. Bib entry should use year=2026 if citing the conference version, or year=2025 if citing the preprint. Verify which year is used in the bib. |

### 3. lewis2020bart — BART
| Check | Status | Detail |
|-------|--------|--------|
| Exists | YES | |
| Authors | MATCH | First author Mike Lewis, with Yinhan Liu, Naman Goyal, et al. Confirmed. |
| Title | MATCH | "BART: Denoising Sequence-to-Sequence Pre-training for Natural Language Generation, Translation, and Comprehension" |
| Year | MATCH | 2020 |
| Venue | MATCH | ACL 2020 (ACL Anthology: 2020.acl-main.703) |
| arXiv ID | N/A | No arXiv ID claimed
…[truncated 5884 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 41
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-29T06:37:33.952591+00:00_

Now I have enough information to compile the full structured checklist. Here is the verification report:

---

## Reference Verification Checklist

### 1. shukor2025smolvla

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv, Semantic Scholar, HuggingFace |
| Authors | **MATCH** | First author is Mustafa Shukor; confirmed |
| Title | **MATCH** | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" -- exact |
| Year | **ISSUE** | The arXiv submission date is **June 2, 2025**. The arXiv ID prefix `2506` confirms June 2025. Listing year as 2025 is correct, but note the paper appeared mid-2025, not earlier |
| Venue | **N/A** | Listed as arXiv preprint only; no formal venue claimed. OK |
| arXiv ID | **MATCH** | 2506.01844 confirmed |

**Verdict: PASS**

---

### 2. kim2024openvla

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2406.09246), PMLR, OpenReview |
| Authors | **MATCH** | First author Moo Jin Kim; confirmed |
| Title | **MATCH** | "OpenVLA: An Open-Source Vision-Language-Action Model" -- exact |
| Year | **ISSUE** | The conference was CoRL 2024 (held Nov 2024), but the PMLR proceedings (volume 270) were published **January 12, 2025**. The bib key `kim2024` is acceptable if citing the conference year. However, the PMLR entry uses `kim25c`. Either 2024 or 2025 is defensible; using 2024 (conference year) is the common convention |
| Venue | **MATCH** | CoRL 2024, 8th Conference on Robot Learning -- confirmed |
| arXiv ID | **Not provided in entry** | arXiv:2406.09246 exists if needed |

**Verdict: PASS (minor: year ambiguity 2024 vs 2025 for PMLR publication date)**

---

### 3. brohan2023rt2

| Check | Result | Notes |
|-------|--------|-------|
| Exists | **YES** | Found on arXiv (2307.15818), PMLR, Semantic Scholar |
| Authors | **ISSUE** | On arXiv, Anthony Brohan is listed first. In the official CoRL 2023 PMLR proceedings (v229), the paper is listed
…[truncated 5826 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 50
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-29T06:37:33.952860+00:00_

Web search results for query: "Diffusion Policy Chi Cheng RSS 2023 or IJRR venue proceedings"

Links: [{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"Diffusion Policy","url":"https://arxiv.org/html/2502.12371v2"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"[PDF] Diffusion policy: Visuomotor policy learning via action diffusion | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Diffusion-policy:-Visuomotor-policy-learning-via-Chi-Feng/bdba3bd30a49ea4c5b20b43dbd8f0eb59e9d80e2"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion","url":"https://www.researchgate.net/publication/384857010_Diffusion_policy_Visuomotor_policy_learning_via_action_diffusion"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion · Robotics: Science and Systems","url":"https://roboticsconference.org/2023/program/papers/026/"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/pdf/2303.04137"}]

Based on the search results, here's what I found about Diffusion Policy by Chi Cheng:

The paper "Diffusion Policy: Visuomotor Policy Learning via Action Diff
…[truncated 910 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 1
}
```

</details>

---

### Tool call

_source line 257 · 2026-05-29T06:37:33.953114+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "arxiv.org abs 2307.15818 RT-2 \"Anthony Brohan\" first author alphabetical"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "arxiv.org abs 2307.15818 RT-2 \"Anthony Brohan\" first author alphabetical"
  }
}
```

</details>

---

### Tool call

_source line 258 · 2026-05-29T06:37:33.953351+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "RoboFlamingo ICLR 2024 accepted Li Xinghang title exact"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "RoboFlamingo ICLR 2024 accepted Li Xinghang title exact"
  }
}
```

</details>

---

### Tool result

_source line 259 · 2026-05-29T06:37:33.953557+00:00_

Web search results for query: "arxiv.org abs 2307.15818 RT-2 "Anthony Brohan" first author alphabetical"

Links: [{"title":"[2307.15818] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://arxiv.org/abs/2307.15818"},{"title":"Paper page - RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://huggingface.co/papers/2307.15818"},{"title":"RT-2: Vision-Language-Action Models Transfer Web ...","url":"https://arxiv.org/pdf/2307.15818"},{"title":"(PDF) RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://www.researchgate.net/publication/372784419_RT-2_Vision-Language-Action_Models_Transfer_Web_Knowledge_to_Robotic_Control"},{"title":"[PDF] RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/RT-2:-Vision-Language-Action-Models-Transfer-Web-to-Brohan-Brown/38939304bb760473141c2aca0305e44fbe04e6e8"},{"title":"dblp: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control.","url":"https://dblp.org/rec/journals/corr/abs-2307-15818.html"},{"title":"RT-2: Vision-Language-Action Models","url":"https://robotics-transformer2.github.io/"},{"title":"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control","url":"https://proceedings.mlr.press/v229/zitkovich23a.html"}]

Based on the search results, I can confirm the following about arxiv paper 2307.15818:

**Paper Details:**
- Title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
- First author: Anthony Brohan (with 53 other authors)

**Regarding author alphabetization:** The complete author list in alphabetical order is: Anthony Brohan, Noah Brown, Justice Carbajal, Yevgen Chebotar, Xi Chen, Krzysztof Choromanski, Tianli Ding, Danny Driess, Avinava Dubey, Chelsea Finn, Pete Florence, Chuyuan Fu, Montse Gonzalez Arenas, Keerthana Gopalakrishnan, Kehang
…[truncated 807 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 260 · 2026-05-29T06:37:33.953801+00:00_

Web search results for query: "RoboFlamingo ICLR 2024 accepted Li Xinghang title exact"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"RoboFlamingo Review | gracefullight.dev","url":"https://gracefullight.dev/en/2025/08/31/roboflamingo-review/"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"RoboFlamingo-Plus: Fusion of Depth and RGB Perception with   Vision-Language Models for Enhanced Robotic Manipulation","url":"https://arxiv.org/pdf/2503.19510"},{"title":"RoboFlamingo - Overview","url":"https://github.com/roboflamingo"},{"title":"GitHub - RoboFlamingo/RoboFlamingo: Code for RoboFlamingo · GitHub","url":"https://github.com/RoboFlamingo/RoboFlamingo"}]

Based on the search results, I found information about RoboFlamingo by Li Xinghang. However, the paper appears to have been published as a preprint on arXiv in 2023, not accepted to ICLR 2024.

The exact title is "Vision-Language Foundation Models as Effective Robot Imitators", authored by Xinghang Li and colleagues from ByteDance Research, Tsinghua University, Shanghai Jiao Tong University, and National University of Singapore.

The search results show this as an ICLR 2023 paper rather than ICLR 2024. The paper was first submitted to arXiv on November 2, 2023, according to the search results. If you're looking for information about an ICLR 2024 acceptance of this work, I would need to search for more recent publication information to verify that specific claim.


REMINDER: You MUST include the sources abov
…[truncated 57 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 261 · 2026-05-29T06:37:33.954057+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024 accepted decision"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024 accepted decision"
  }
}
```

</details>

---

### Tool result

_source line 262 · 2026-05-29T06:37:33.954432+00:00_

Earlier search results did find an ICML 2026 poster page for this paper. Let me confirm the year for the Compressor-VLA entry — the arXiv ID 2511.* indicates November 2025, which matches the claimed year 2025.

Here is the structured verification checklist:

---

## Reference Verification Checklist

### 1. abnar2020quantifying
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "Quantifying Attention Flow in Transformers" | "Quantifying Attention Flow in Transformers" | OK |
| Authors | Abnar, Samira and Zuidema, Willem | Samira Abnar, Willem Zuidema | OK |
| Year | 2020 | 2020 | OK |
| Venue | ACL 2020 | ACL 2020 (Proceedings of the 58th Annual Meeting of the ACL) | OK |
| Pages | 4190-4197 | 4190-4197 (ACL Anthology confirms) | OK |
| **Verdict** | **PASS -- no issues** |

---

### 2. gao2025compressorvla
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "Compressor-VLA: Instruction-Guided Visual Token Compression for Efficient Robotic Manipulation" | Exact match on arXiv | OK |
| Authors | Gao, Juntao and Ye, Feiyang and Zhang, Jing and Qian, Wenjing | Juntao Gao, Feiyang Ye, Jing Zhang, Wenjing Qian | OK |
| Year | 2025 | arXiv ID 2511.18950 = November 2025 | OK |
| Venue | arXiv preprint | arXiv preprint | OK |
| arXiv ID | 2511.18950 | 2511.18950 | OK |
| **Verdict** | **PASS -- no issues** |

---

### 3. wang2025specprunevla
| Field | Bib Entry | Verified | Match? |
|---|---|---|---|
| Exists | — | Yes | OK |
| Title | "SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning" | Exact match on arXiv | OK |
| Authors | Wang, Hanzhen and Xu, Jiaming and Xiang, Yushun and Pan, Jiayi and Zhou, Yongkang and Li, Yong-Lu and Dai, Guohao | Hanzhen Wang, Jiaming Xu, Yushun Xiang, Jiayi Pan, Yongkang Zhou, Yong-Lu Li, Guohao Dai | OK |
| Year | 2025 | arXiv submitted September 2025 | OK |
| Venue | arXiv preprint | arXiv preprint | OK |
|
…[truncated 5805 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 53
}
```

</details>

---

### Tool result

_source line 263 · 2026-05-29T06:37:33.954690+00:00_

Web search results for query: "openreview.net "Vision-Language Foundation Models as Effective Robot Imitators" ICLR 2024 accepted decision"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"Unveiling the Potential of Vision-Language-Action Models with Open-Ended Multimodal Instructions","url":"https://arxiv.org/html/2505.11214v1"},{"title":"CogACT: A Foundational Vision-Language-Action Model for Synergizing Cognition and Action in Robotic Manipulation","url":"https://arxiv.org/html/2411.19650v1"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v1"},{"title":"Can Pretrained Vision-Language Embeddings Alone Guide Robot Navigation?","url":"https://arxiv.org/pdf/2506.14507"},{"title":"RoboMamba: Efficient Vision-Language-Action Model for Robotic Reasoning and Manipulation","url":"https://arxiv.org/html/2406.04339v2"}]

Based on the search results, I found the paper "Vision-Language Foundation Models as Effective Robot Imitators" on OpenReview. The paper presents RoboFlamingo, a vision-language manipulation framework built upon OpenFlamingo that utilizes pre-trained vision-language models for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is fine-tuned by imitation learning on language-conditioned manipulation datasets.

However, I should note that the search results indicate this paper was presented at The Twelfth International Conference on Learning Representations in October 2023, not ICLR 2024. The paper appears to have 
…[truncated 493 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 264 · 2026-05-29T06:37:33.954947+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "site:openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "tool_args": {
    "query": "site:openreview.net \"Vision-Language Foundation Models as Effective Robot Imitators\" ICLR 2024"
  }
}
```

</details>

---

### Tool result

_source line 265 · 2026-05-29T06:37:33.955181+00:00_

Web search results for query: "site:openreview.net "Vision-Language Foundation Models as Effective Robot Imitators" ICLR 2024"

Links: [{"title":"Vision-Language Foundation Models as Effective Robot Imitators | OpenReview","url":"https://openreview.net/forum?id=lFYj0oibGR"},{"title":"ICLR Poster Vision-Language Foundation Models as Effective Robot Imitators","url":"https://iclr.cc/virtual/2024/poster/17943"},{"title":"[Quick Review] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://liner.com/review/visionlanguage-foundation-models-as-effective-robot-imitators"},{"title":"[2311.01378] Vision-Language Foundation Models as Effective Robot Imitators","url":"https://arxiv.org/abs/2311.01378"},{"title":"AutoRT: Embodied Foundation Models for Large Scale Orchestration of Robotic Agents | OpenReview","url":"https://openreview.net/forum?id=xVlcbh0poD"},{"title":"Can Pretrained Vision-Language Embeddings Alone Guide Robot Navigation?","url":"https://arxiv.org/pdf/2506.14507"},{"title":"RoboFlamingo | Vision-Language Foundation Models as Effective Robot Imitators","url":"https://roboflamingo.github.io/"},{"title":"Foundation Model Driven Robotics: A Comprehensive Review","url":"https://arxiv.org/pdf/2507.10087"}]

I found the paper you're looking for! Here are the search results:

"Vision-Language Foundation Models as Effective Robot Imitators" presents RoboFlamingo, a framework built upon OpenFlamingo that leverages vision-language models for robotics manipulation.

**Key Details:**

- **Paper Title:** Vision-Language Foundation Models as Effective Robot Imitators
- **Venue:** ICLR 2024 (presented as a poster on May 7, 2024)
- **OpenReview Link:** https://openreview.net/forum?id=lFYj0oibGR

**Main Contributions:**

RoboFlamingo utilizes pre-trained VLMs for single-step vision-language comprehension, models sequential history information with an explicit policy head, and is slightly fine-tuned by imitation learning only on language-conditioned mani
…[truncated 504 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "WebSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 266 · 2026-05-29T06:37:33.955579+00:00_

Good, ICLR 2024 is confirmed. Now I have all the information I need. Let me compile the structured verification checklist.

Here is the structured verification checklist for all 15 entries:

---

## Reference Verification Checklist

### 1. shi2024crossget — CrossGET
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "CrossGET: Cross-Guided Ensemble of Tokens for Accelerating Vision-Language Transformers" | Same | YES |
| Authors | Shi, Dachuan and others | Dachuan Shi, Chaofan Tao, Anyi Rao, Zhendong Yang, Chun Yuan, Jiaqi Wang | YES |
| Year | 2024 | 2024 | YES |
| Venue | ICML 2024 | ICML 2024 | YES |
| arXiv ID | 2305.17455 | 2305.17455 | YES |
| **Issues** | None | | |

---

### 2. oquab2023dinov2 / oquab2024dinov2 — DINOv2
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "DINOv2: Learning Robust Visual Features without Supervision" | Same | YES |
| Authors | Oquab, Maxime and others | Maxime Oquab, Timothee Darcet, et al. | YES |
| Year | 2024 (both entries) | 2024 (TMLR publication: January 2024) | YES |
| Venue | TMLR | Transactions on Machine Learning Research (TMLR) | YES |
| arXiv ID | 2304.07193 | 2304.07193 | YES |
| **Issues** | **Duplicate bib keys**: `oquab2023dinov2` and `oquab2024dinov2` both exist with year=2024. The key `oquab2023dinov2` is misleading — the "2023" in the key suggests year 2023, but the year field says 2024. The arXiv preprint was April 2023, the TMLR publication was January 2024. Recommend keeping only one entry (e.g., `oquab2024dinov2`) with year=2024 and removing the duplicate. | | |

---

### 3. su2024roformer — RoFormer
| Field | Bib Value | Verified Value | Match? |
|-------|-----------|----------------|--------|
| Exists | — | Yes | YES |
| Title | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | Same | YES |
| Authors | Su, Jianlin and others |
…[truncated 8444 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907",
  "tool": "Agent",
  "elapsed_ms": 34
}
```

</details>

---

### Assistant

_source line 267 · 2026-05-29T06:37:33.956084+00:00_

All verification complete. Let me now compile the full checklist, including citation context checks.

---

## 引用核对清单

### A. 主论文中引用的条目（37条被引用，按出现顺序）

```
[✓] rao2021dynamicvit | Rao, Yongming et al. | "DynamicViT: Efficient Vision Transformers with Dynamic Token Sparsification" | 2021 | NeurIPS 2021
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — ViT token pruning代表工作 ✓

[✓] bolya2023tome | Bolya, Daniel et al. | "Token Merging: Your ViT But Faster" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5, appendix — token merging方法 ✓

[✓] liang2022evit | Liang, Youwei et al. | "Not All Patches are What You Need: Expediting Vision Transformers via Token Reorganizations" | 2022 | ICLR 2022
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L5 — ViT token pruning ✓

[✓] cheng2026vlaiap | Cheng, Jintao et al. | "VLA-IAP: Training-Free Visual Token Pruning..." | 2026 | arXiv 2603.22991
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning方法 ✓

[✓] xu2025vlacache | Xu, Siyu et al. | "VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching" | 2025 | NeurIPS 2025
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token caching ✓

[✓] yang2025efficientvla | Yang, Yantai et al. | "EfficientVLA: Training-Free Acceleration and Compression for VLA Models" | 2025 | arXiv 2506.10100
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8, results — CogACT pruning结果来源 ✓

[✓] liu2025vlapruner | Liu, Ziyan et al. | "VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning..." | 2025 | arXiv 2511.16449
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L14, related_work.tex L8 — VLA token pruning ✓

[✓] black2024pi0 | Black, Kevin et al. | "π0: A Vision-Language-Action Flow Model for General Robot Control" | 2024 | arXiv 2410.24164
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction.tex L16, method.tex, results — linear projection connector ✓

[✓] kim2024openvla | Kim, Moo Jin et al. | "OpenVLA: An Open-Source Vision-Language-Action Model" | 2024 | CoRL 2024
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: introduction.tex L16, background, method, results — MLP projector connector ✓

[✓] shukor2025smolvla | Shukor, Mustafa et al. | "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics" | 2025 | arXiv 2506.01844
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: introduction, background, method, results — pixel-shuffle connector ✓

[✓] zheng2025xvla | Zheng, Jinliang et al. | "X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment VLA Model" | 2026 | ICLR 2026, arXiv 2510.10274
- 验证结果: 真实存在/作者正确/标题正确/年份正确(field=2026)/venue正确/arXiv ID正确
- 正文用法: introduction.tex L16, method, experiments, results — BART encoder connector ✓

[✓] chen2024fastv | Chen, Liang et al. | "An Image is Worth 1/2 Tokens After Layer 2..." | 2024 | ECCV 2024, arXiv 2403.06764
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✗] shang2024prumerge | Shang, Yuzhang et al. | "LLaVA-PruMerge: Adaptive Token Reduction for Efficient Large Multimodal Models" | 2024→2025 | ICCV 2025
- 验证结果: 真实存在/作者正确/标题正确/venue正确
- 问题: **年份错误**。Bib year=2025 正确匹配 ICCV 2025，但 bib key 暗示 2024。实际 booktitle 写的是 "IEEE/CVF International Conference on Computer Vision (ICCV)" year=2025，这是正确的。（复查：bib 文件中 year=2025，OK。bib key 中的 2024 仅是标识符不影响输出。）
- **修正**: 复查后 bib year field = 2025，venue = ICCV 2025，均正确。bib key "2024" 不影响输出。**改判为 ✓**。

[✓] zhang2025sparsevlm | Zhang, Yuan et al. | "SparseVLM: Visual Token Sparsification..." | 2025 | ICML 2025, arXiv 2410.04417
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✗] khaki2025sparsevila | Khaki, Samir et al. | "SparseVILA: Decoupled Visual Sparsity..." | 2025 | ICCV 2025, arXiv 2510.17777
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题: **标题错误**。Bib 写 "Decoupled"，实际标题为 "Decoupling"（动名词形式）
- 正文用法: related_work.tex L8 — VLM token sparsification ✓

[✓] ye2025fitprune | Ye, Weihao et al. | "Fit and Prune: Fast and Training-free Visual Token Pruning for Multi-modal LLMs" | 2025 | AAAI 2025, arXiv 2409.10197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLM token pruning ✓

[✓] jiang2026lightvla | Jiang, Titong et al. | "The Better You Learn, The Smarter You Prune..." | 2026 | ICRA 2026, arXiv 2509.12594
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA differentiable token pruning ✓

[✓] gao2025compressorvla | Gao, Juntao et al. | "Compressor-VLA: Instruction-Guided Visual Token Compression..." | 2025 | arXiv 2511.18950
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token compression ✓

[✓] wang2025specprunevla | Wang, Hanzhen et al. | "SpecPrune-VLA: Accelerating VLA Models via Action-Aware Self-Speculative Pruning" | 2025 | arXiv 2509.05614
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA pruning ✓

[✓] feng2026seewhatmatters | Feng, Yixu et al. | "See What Matters: Differentiable Grid Sample Pruning..." | 2026 | ICML 2026, arXiv 2605.11817
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L8 — VLA token pruning ✓

[✓] jabbour2025dontrun | Jabbour, Jason et al. | "Don't Run with Scissors: Pruning Breaks VLA Models but They Can Be Recovered" | 2025 | arXiv 2510.08464
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: related_work.tex L11 — concurrent work on VLA pruning failure ✓

[✓] liu2023llava | Liu, Haotian et al. | "Visual Instruction Tuning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — LLaVA MLP projector ✓

[✓] li2023blip2 | Li, Junnan et al. | "BLIP-2: Bootstrapping Language-Image Pre-Training..." | 2023 | ICML 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — cross-attention queries ✓

[✓] shi2016subpixel | Shi, Wenzhe et al. | "Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel CNN" | 2016 | CVPR 2016
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: related_work.tex L14 — pixel shuffle origin ✓

[✓] zhai2023siglip | Zhai, Xiaohua et al. | "Sigmoid Loss for Language Image Pre-Training" | 2023 | ICCV 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — SmolVLA vision encoder ✓

[✓] yang2024qwen2 | Yang, An et al. | "Qwen2 Technical Report" | 2024 | arXiv 2407.10671
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: background.tex — Qwen2-0.5B LLM backbone ✓

[✓] lipman2023flow | Lipman, Yaron et al. | "Flow Matching for Generative Modeling" | 2023 | ICLR 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background.tex — flow matching action head ✓

[✓] oquab2023dinov2 | Oquab, Maxime et al. | "DINOv2: Learning Robust Visual Features without Supervision" | 2024 | TMLR
- 验证结果: 真实存在/作者正确/标题正确/year field=2024正确(TMLR 2024)/venue正确
- 问题（次要）: bib key 含 "2023" 但 year field = 2024。arXiv 发布于 2023.04，TMLR 发表于 2024.01。Key 不影响输出。
- 正文用法: background.tex — OpenVLA dual encoder ✓

[✓] black2025pi05 | Black, Kevin et al. | "π0.5: a Vision-Language-Action Model with Open-World Generalization" | 2025 | CoRL 2025, PMLR v305, pp.17-40, arXiv 2504.16054
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确/pages正确/arXiv ID正确
- 正文用法: method.tex, experiments.tex, results — linear connector model ✓

[✓] kim2025openoft | Kim, Moo Jin et al. | "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success" | 2025 | arXiv 2502.19645
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: method.tex, results — OFT variant of OpenVLA ✓

[✓] lewis2020bart | Lewis, Mike et al. | "BART: Denoising Sequence-to-Sequence Pre-training..." | 2020 | ACL 2020
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: method.tex — X-VLA uses BART encoder ✓

[✓] liu2023libero | Liu, Bo et al. | "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning" | 2023 | NeurIPS 2023
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确
- 正文用法: background, method, experiments, results — evaluation benchmark ✓

[✓] li2024cogact | Li, Qixiu et al. | "CogACT: A Foundational Vision-Language-Action Model..." | 2024 | arXiv 2411.19650
- 验证结果: 真实存在/作者正确/标题正确/年份正确/arXiv ID正确
- 正文用法: results — MLP projector corroboration from EfficientVLA ✓

[✓] shi2024crossget | Shi, Dachuan et al. | "CrossGET: Cross-Guided Ensemble of Tokens..." | 2024 | ICML 2024, arXiv 2305.17455
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/arXiv ID正确
- 正文用法: related_work.tex L5 — ViT token pruning ✓

[✓] yin2022avit | Yin, Hongxu et al. | "A-ViT: Adaptive Tokens for Efficient Vision Transformer" | 2022 | CVPR 2022, arXiv 2112.07658
- 验证结果: 真实存在/作者正确/年份正确/venue正确/arXiv ID正确
- 问题（次要）: arXiv 标题为 "AdaViT"，CVPR 发表版改名 "A-ViT"。Bib 使用 CVPR 标题，正确。
- 正文用法: related_work.tex L5 — ViT adaptive tokens ✓

[✓] abnar2020quantifying | Abnar, Samira & Zuidema, Willem | "Quantifying Attention Flow in Transformers" | 2020 | ACL 2020, pp.4190-4197
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/pages正确
- 正文用法: appendix — attention rollout method ✓

[✓] su2024roformer | Su, Jianlin et al. | "RoFormer: Enhanced Transformer with Rotary Position Embedding" | 2024 | Neurocomputing v568 p127063
- 验证结果: 真实存在/作者正确/标题正确/年份正确/venue正确/volume正确
- 正文用法: appendix — RoPE position encoding ✓
```

---

### B. 问题条目汇总

| # | 状态 | cite_key | 问题 | 严重度 |
|---|------|----------|------|--------|
| 1 | **✗** | `khaki2025sparsevila` | 标题 "Decoupled" 应为 "**Decoupling**" | **需修复** |

其余 36 条引用条目均验证通过。

---

### C. 未被主论文引用的 bib 条目（25条）

以下条目存在于 `references.bib` 但未在 main.tex 编译链中被 `\cite` 引用（可能来自早期草稿）：

| cite_key | 备注 |
|----------|------|
| `li2024roboflamingo` | 未引用 |
| `brohan2023rt2` | 未引用；与 `zitkovich2023rt2` 重复（同一论文，arXiv vs proceedings 作者顺序不同） |
| `brohan2023rt1` | 未引用 |
| `ghosh2024octo` | 未引用 |
| `alayrac2022flamingo` | 未引用 |
| `chen2024internvl` | 未引用 |
| `jaegle2021perceiver` | 未引用 |
| `li2024tokenpacker` | 未引用 |
| `wen2024tinyvla` | 未引用 |
| `ryoo2021tokenlearner` | 未引用 |
| `meng2022adavit` | 未引用 |
| `chen2023sparsevit` | 未引用 |
| `zhang2024fastervlm` | 未引用 |
| `liu2024llava15` | 未引用 |
| `chen2024internvl25` | 未引用 |
| `gao2024miniinternvl` | 未引用 |
| `zitkovich2023rt2` | 未引用；与 `brohan2023rt2` 重复 |
| `openxembodiment2024` | 未引用 |
| `zhang2023h2o` | 未引用 |
| `xiao2024streamingllm` | 未引用 |
| `mees2022calvin` | 未引用 |
| `chi2023diffusionpolicy` | 未引用 |
| `zeng2023transformers_tsf` | 未引用（仅在 sections/ 草稿中出现） |
| `bouthillier2024negative` | 未引用；**且作者错误**（实际第一作者为 Florian Karl，非 Xavier Bouthillier） |
| `oquab2024dinov2` | 未引用；与 `oquab2023dinov2` 重复 |

---

### D. 总结

**需修复（1条）：**
- `khaki2025sparsevila`：标题 "Decoupled" → "**Decoupling**"

**建议清理（不影响编译输出，但建议处理）：**
- 25 条未引用条目可从 bib 中移除以保持整洁
- `oquab2023dinov2` 和 `oquab2024dinov2` 是同一论文的重复条目
- `brohan2023rt2` 和 `zitkovich2023rt2` 是同一论文的重复条目（arXiv vs proceedings 作者顺序不同）
- `bouthillier2024negative` 的作者字段有误（但未被引用，不影响论文）

**全部 37 条被引用条目中**：36 条完全正确，1 条有标题拼写错误。所有引用在正文中的使用语境均准确，无张冠李戴的情况。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_ref_verify_worker_A_20260529T062907"
}
```

</details>

---
