# audit paper section status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 53
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/chats/worker_audit_paper_section_status_20260527T042940.jsonl`
- **Structured JSON:** [`a72ee3e7ceefc564d200.json`](../../sessions/a7/a72ee3e7ceefc564d200.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

53 recorded events

### Tool call

_source line 1 · 2026-05-27T04:33:50.646483+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ -name \"*.tex\" -o -name \"*.md\" 2>/dev/null | sort",
  "description": "List paper directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ 2>/dev/null; echo \"---\"; find /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper/ -name \"*.tex\" -o -name \"*.md\" 2>/dev/null | sort",
    "description": "List paper directory structure"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-27T04:33:50.646958+00:00_

---

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-27T04:33:50.647226+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.tex",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-27T04:33:50.647473+00:00_

artifacts/corl_template/corl_2026_template_submission/example.tex
artifacts/corl_template/__MACOSX/corl_2026_template_submission/._example.tex
artifacts/dream_reports/dream_20260516T075046/best/paper.tex
artifacts/dream_reports/dream_20260516T075046/median/paper.tex
artifacts/dream_reports/dream_20260516T075046/worst/paper.tex
docs/paper/sections/analysis.tex
docs/paper/sections/background.tex
docs/paper/sections/experimental_setup.tex
artifacts/_project/paper/results_draft.tex
docs/paper/sections/results_draft.tex
docs/paper/sections/analysis_draft.tex
docs/paper/experiments_deprecated.tex
docs/paper/sections/experiments.tex
docs/paper/sections/related_work_draft.tex
docs/paper/sections/introduction.tex
docs/paper/background.tex
artifacts/dream_reports/dream_20260520T155932/best/paper.tex
artifacts/dream_reports/dream_20260520T155932/median/paper.tex
artifacts/dream_reports/dream_20260520T155932/worst/paper.tex
docs/paper/results_v2.tex
docs/paper/experimental_setup.tex
docs/paper/results.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/abstract.tex
docs/paper/discussion.tex
docs/paper/related_work.tex
docs/paper/method.tex
artifacts/dream_reports/dream_20260525T050917/best/paper.tex
artifacts/dream_reports/dream_20260525T050917/median/paper.tex
artifacts/dream_reports/dream_20260525T050917/worst/paper.tex
docs/paper/appendix.tex
docs/paper/main.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/abstract.tex
artifacts/_project/paper/tab_model_properties_56d5eb.tex
artifacts/_project/paper/tab_model_properties.tex
artifacts/tab_model_properties.tex
artifacts/_project/paper/tab_main_results_8f3985.tex
artifacts/_project/paper/tab_main_results.tex
artifacts/tab_main_results.tex
docs/paper/experiments.tex
docs/paper/analysis.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-27T04:33:50.647702+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/*.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-27T04:33:50.647955+00:00_

artifacts/.venv/lib/python3.14/site-packages/torchgen/packaged/autograd/README.md
artifacts/architecture_report.md
task_context/history/reviewer/loop_1.md
task_context/history/director/loop_1.md
task_context/history/agent/loop_1.md
task_context/history/agent/loop_1_1778878965.md
task_context/history/director/loop_2.md
task_context/history/agent/loop_2.md
task_context/history/director/loop_3.md
task_context/history/reviewer/loop_2.md
task_context/history/agent/loop_2_1778890120.md
task_context/history/agent/loop_3.md
task_context/history/agent/loop_3_1778900113.md
.claude/sessions/agent_175a0fc4/CLAUDE.md
.claude/sessions/agent_175a0fc4/AGENTS.md
task_context/history/agent/loop_2_1778903096.md
task_context/history/agent/loop_4.md
.claude/sessions/agent_567a8628/CLAUDE.md
.claude/sessions/agent_567a8628/AGENTS.md
task_context/history/reviewer/loop_3.md
task_context/history/director/loop_4.md
task_context/history/agent/loop_4_1778929745.md
.claude/sessions/agent_117c0105/CLAUDE.md
.claude/sessions/agent_117c0105/AGENTS.md
artifacts/mvp_imm_v8b_twostage/diagnosis.md
docs/IDEA_BRIEF.md
artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/review_report.md
artifacts/dream_reports/dream_20260516T075046/best/review_report.md
artifacts/dream_reports/dream_20260516T075046/worst/review_report.md
task_context/history/reviewer/loop_4.md
task_context/history/director/loop_5.md
task_context/history/agent/loop_5.md
artifacts/research_lora_mode_collapse_fix.md
task_context/history/reviewer/loop_5.md
task_context/history/agent/loop_5_1778944487.md
task_context/history/agent/loop_6.md
task_context/history/director/loop_6.md
artifacts/_project/chart/paper_figures_v1.md
task_context/history/reviewer/loop_6.md
task_context/history/agent/loop_7.md
.claude/sessions/agent_a95c4df4/CLAUDE.
…[truncated 2548 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-27T04:33:50.648272+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/main.tex"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-27T04:33:50.648597+00:00_

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
12	
13	\title{Why Token Pruning Crashes Some Robot Policies but Not Others:\\Vision Connectors and VLA Token Compressibility}
14	
15	\begin{document}
16	\maketitle
17	
18	\input{abstract}
19	
20	\keywords{vision-language-action models, token pruning, robot learning}
21	
22	\input{introduction}
23	
24	\input{related_work}
25	
26	\input{method}
27	
28	\input{experiments}
29	
30	\input{analysis}
31	
32	\input{conclusion}
33	
34	\bibliography{references}
35	
36	\input{appendix}
37	
38	\end{document}
39	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-27T04:33:50.648813+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/abstract.tex"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-27T04:33:50.649040+00:00_

1	\begin{abstract}
2	Vision-Language-Action (VLA) models encode observations as hundreds of vision tokens, creating a computational bottleneck for real-time robotic control. Token pruning offers a training-free remedy, yet its effect varies dramatically across architectures: at retention ratio $k{=}0.95$, $\pi_{0.5}$ preserves 98\% task success while SmolVLA collapses to 0\%---why?
3	
4	We identify the vision-language connector as the primary architectural factor governing pruning tolerance. The coefficient of variation (CV) of post-connector token norms, computable in a single forward pass, predicts compressibility across the full architecture spectrum: from CV$\,{=}\,$0.038 (near-immune linear projection) to CV$\,{=}\,$0.314 (catastrophic pixel-shuffle collapse). Across five VLA architectures (450\,M--7\,B parameters) and four LIBERO manipulation suites, token-independent connectors degrade gracefully, while token-entangling connectors exhibit abrupt cliffs: SmolVLA collapses when just 6 of 128 tokens are removed.
5	
6	Importance-based selection is not universally beneficial---it can be actively harmful. At moderate compression, L2 norm selection preserves 98\% success on $\pi_{0.5}$ where random yields 5\% (93\,pp gap); at aggressive ratios, random outperforms L2 by up to 36\,pp. Attention-based scoring exhibits within-model reversals across task suites. No scoring method is universally safe: task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to $20{\times}$. A zero-mask ablation isolates the mechanism: on $\pi_{0.5}$, zeroing 10\% of tokens preserves 98.0\% SR while physical removal collapses to 9.0\%---the 89\,pp gap is entirely attributable to position disruption, not information loss. For architectures where all deletion strategies fail, a lightweight re-encoding module (${\sim}$5\% extra parameters) recovers $>$60\% success at 75\% compression.
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T04:33:50.649296+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/introduction.tex"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-27T04:33:50.649554+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\begin{figure*}[t]
5	\centering
6	\includegraphics[width=\textwidth]{figures/paper/fig_hero_overview.pdf}
7	\caption{Overview of VLA token compressibility.
8	\textbf{(a)}~The same robot observation produces qualitatively different token importance patterns through different vision connectors, quantified by the coefficient of variation (CV) of post-connector token norms.
9	\textbf{(b)}~Connector architecture determines pruning tolerance: independent connectors degrade gracefully, entangling connectors exhibit cliffs; task complexity amplifies the divergence.
10	\textbf{(c)}~A single forward pass CV diagnostic routes each architecture to an appropriate compression strategy: uniform pruning, importance-based scoring, or learned re-encoding.}
11	\label{fig:teaser}
12	\end{figure*}
13	
14	Remove 5\% of vision tokens from SmolVLA and its success rate collapses from 59.2\% to near-zero (${\leq}$6.6\%) across all task suites and pruning methods. Apply the same 5\% reduction to $\pi_{0.5}$ and it retains 98.2\% under L2 norm selection. Both are Vision-Language-Action (VLA) models built on a Vision Transformer (ViT) encoder feeding tokens through a connector into a language model backbone; the critical difference is not model scale (450M vs.\ 4B parameters) but the connector architecture. Token pruning is well-established for ViTs~\cite{rao2021dynamicvit,bolya2023tome,liang2022evit} and a growing body of work extends it to VLAs~\cite{cheng2026vlaiap,xu2025vlacache,yang2025efficientvla,liu2025vlapruner}, but each method validates on a single architecture.
15	
16	These methods implicitly assume that pruning transfers across VLA designs. Yet current VLAs employ fundamentally different vision connectors: linear projections~\cite{black2024pi0}, MLP projectors~\cite{kim2024openvla}, pixel-shuffle folding~\cite{shukor2025smolvla}, and learned encoders with cross-token self-attention~\cite{zheng2025xvla}. Each imposes distinct 
…[truncated 3133 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-27T04:33:50.649785+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/related_work.tex"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T04:33:50.650017+00:00_

1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{ViT token pruning.}
5	DynamicViT~\cite{rao2021dynamicvit}, EViT~\cite{liang2022evit}, A-ViT~\cite{yin2022avit}, and Token Merging~\cite{bolya2023tome} remove 50--66\% of tokens with under 0.5\,pp ImageNet accuracy loss. Their success rests on classification's insensitivity to spatial layout; robotic manipulation inverts this assumption, as grasping depends on spatial arrangement. None has been evaluated in closed-loop VLA control.
6	
7	\paragraph{Token efficiency in VLMs and VLAs.}
8	FastV~\cite{chen2024fastv} and PruMerge~\cite{shang2024prumerge} reduce vision tokens in VLMs using language-backbone attention signals. ``Don't Run with Scissors''~\cite{jabbour2025dontrun} analyzes VLM token pruning for visual question answering; our work targets closed-loop robotic manipulation, where pruning failures directly impact physical task execution rather than text generation quality. VLA-specific methods have emerged in parallel: VLA-IAP~\cite{cheng2026vlaiap} aligns pruning with action-prediction importance, VLA-Cache~\cite{xu2025vlacache} compresses at the KV-cache level, EfficientVLA~\cite{yang2025efficientvla} combines pruning with merging, and VLA-Pruner~\cite{liu2025vlapruner} learns a pruning policy jointly with the action head. LightVLA~\cite{jiang2026lightvla} introduces differentiable pruning and Compressor-VLA~\cite{gao2025compressorvla} applies instruction-guided compression, both targeting individual architectures; our work instead asks how architectural choices determine which compression approaches succeed or fail, finding that scoring validity is architecture-dependent; L2 norm selection is anti-informative on entangling connectors while attention scoring recovers near-baseline performance.
9	
10	\paragraph{Vision connectors.}
11	The connector between ViT and language backbone governs how spatial information distributes across tokens. LLaVA~\cite{liu2023llava} projects patches independently 
…[truncated 747 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T04:33:50.650271+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/method.tex"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-27T04:33:50.650553+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Models and Connectors}
5	\label{sec:models}
6	
7	We evaluate token pruning across six VLA architectures spanning three vision connector families (Table~\ref{tab:model_properties}; Figure~\ref{fig:architecture}). These connectors differ in whether they process ViT patches independently or create cross-token dependencies, a distinction we formalize as \emph{coupling}.
8	
9	\textbf{Linear projection} applies a single matrix multiplication per patch. $\pi_{0}$~\cite{black2024pi0} projects 256 patches through a linear layer; $\pi_{0.5}$~\cite{black2025pi05} uses a $\times\!\sqrt{d}$-scaled linear projection across 768 tokens from three cameras (CV$\,{<}\,$0.06).
10	
11	\textbf{MLP projector} maps each patch independently through a multi-layer perceptron. OpenVLA~\cite{kim2024openvla} uses a three-layer MLP (256 tokens; CV$\,{=}\,$0.215); OFT~\cite{kim2025openoft}, an OpenVLA fine-tuning variant evaluated offline, shares the same connector (512 tokens; CV$\,{=}\,$0.219).
12	
13	\textbf{Token-entangling connectors} introduce cross-token dependencies. X-VLA~\cite{zheng2025xvla} feeds linearly projected tokens through a 12-layer BART encoder~\cite{lewis2020bart} (50 tokens). SmolVLA~\cite{shukor2025smolvla} applies pixel-shuffle $4{\times}4$ folding, concatenating 16 contiguous patches into each output token's channel dimension (128 tokens).
14	
15	We classify coupling as \emph{independent} when each output token depends on a single input patch, and \emph{entangling} when output tokens encode information from multiple patches. Four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA) are evaluated in closed-loop control on LIBERO~\cite{liu2023libero}; $\pi_{0}$ and OFT are analyzed via offline metrics only.
16	
17	\begin{figure*}[t]
18	\centering
19	\includegraphics[width=\textwidth]{figures/paper/fig_architecture_v2.pdf}
20	\caption{Vision connector architectures across four closed-loop VLAs, ordered by increasing compressib
…[truncated 4986 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T04:33:50.650795+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-27T04:33:50.651241+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:exp_setup}
6	
7	We evaluate vision token pruning across six VLA architectures spanning three connector families on the LIBERO benchmark~\cite{liu2023libero}. LIBERO provides four task suites of increasing complexity: Object (object manipulation), Spatial (spatial reasoning), Goal (goal-conditioned tasks), and Long (long-horizon multi-step tasks). Each suite contains 10 tasks evaluated over 50 episodes, yielding 500 episodes per condition.
8	
9	Four models are evaluated in closed-loop robotic control: $\pi_{0.5}$~\cite{black2025pi05} (4B parameters, linear projection with $\times\!\sqrt{d}$ scaling, 768 tokens from three cameras, CV$\,{=}\,$0.055), X-VLA~\cite{zheng2025xvla} (880M, linear projection followed by a 12-layer BART encoder~\cite{lewis2020bart}, 50 tokens, CV$\,{=}\,$0.151), OpenVLA~\cite{kim2024openvla} (7B, three-layer MLP projector, 256 tokens, CV$\,{=}\,$0.215), and SmolVLA~\cite{shukor2025smolvla} (450M, pixel-shuffle $4{\times}4$ folding, 128 tokens, CV$\,{=}\,$0.314). Two additional models are analyzed via offline metrics only: $\pi_{0}$~\cite{black2024pi0} (3.3B, linear projection, 256 tokens, CV$\,{=}\,$0.038) and OFT~\cite{kim2025openoft} (7B, three-layer MLP, 512 tokens, CV$\,{=}\,$0.219). All six architectures contribute to the CV diagnostic (Section~\ref{sec:cv_sensitivity}). Table~\ref{tab:model_properties} summarizes model properties and connector details.
10	
11	We follow the pruning protocol of Section~\ref{sec:pruning_protocol} at retention ratios $k \in \{0.3, 0.5, 0.7, 0.85, 0.9, 0.95\}$, reporting mean success rate (SR) over 500 episodes with Wilson 95\% confidence intervals.
12	
13	\subsection{Two-Axis Framework Overview}
14	\label{sec:two_axis}
15	
16	The pruning response depends on token independence imposed by the connector and task complexity (Figure~\ref{fig:teaser}). Token-independent connectors degrade gracefully; token-entanglin
…[truncated 22149 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T04:33:50.651502+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/analysis.tex"
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-27T04:33:50.651775+00:00_

1	\section{Discussion}
2	\label{sec:analysis}
3	
4	\paragraph{Re-encoding and CV diagnostics.}
5	Both cross-attention and MLP modules achieve comparable recovery ($p = 0.15$); the stable M-curve ($M{=}16 \approx M{=}128$) confirms token count is secondary once entanglement is broken (Appendix~\ref{app:reencoding_analysis}). CV captures effective pipeline complexity beyond connector labels, differentiating X-VLA's threshold-graded behavior (CV$\,{=}\,$0.151) from $\pi_0$'s uniformly critical profile (CV$\,{=}\,$0.038); the interaction reverses at $k{=}0.3$ (Appendices~\ref{app:cv_strategy_interaction},~\ref{app:cv_extended}). For extended mechanistic analysis of how connector architecture creates the observed token independence structure, see Appendices~\ref{app:connector_analysis} and~\ref{app:reencoding_analysis}.
6	
7	\paragraph{Task complexity compresses the importance margin.}
8	The CV diagnostic correctly identifies connector-level compressibility, but practitioners must additionally consider task complexity. On LIBERO-Object (single-step manipulation), L2 norm selection outperforms random on OpenVLA at $k{=}0.9$ ($+$7.8\,pp: L2 70.6\% vs.\ Random 62.8\%). However, this advantage is not robust to deeper compression: at $k{=}0.85$, the importance margin flips to $-$5.2\,pp (Random 60.4\% $>$ L2 55.2\% $\approx$ Attention 55.0\%). The three methods exhibit distinct cliff locations: L2 cliffs earliest ($k{=}0.9{\to}0.85$, $-$15.4\,pp), random next ($k{=}0.85{\to}0.7$, $-$16\,pp), and attention latest ($k{=}0.75{\to}0.7$, $-$9.4\,pp), with attention maintaining a plateau from $k{=}0.85$ to $k{=}0.75$ ($-$1.8\,pp). This staggered cliff onset defines an effective compression window for each scoring method (Figure~\ref{fig:openvla_sweep}). At $k{=}0.5$, all three methods converge within 4.8\,pp (L2: 39.2\%, Random: 35.8\%, Attention: 40.6\%), and scoring choice ceases to matter. On LIBERO-Goal, degradation is smooth with no cliff: all three methods converge within 2\,
…[truncated 4707 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-27T04:33:50.652017+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/conclusion.tex"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-27T04:33:50.652258+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	Connector architecture is the primary factor governing VLA token compressibility. Across five architectures and four LIBERO suites, token-independent connectors degrade gracefully; entangling connectors exhibit catastrophic cliffs amplified by task complexity ($20{\times}$ from Object to Goal). While confounders prevent causal isolation (Appendix~\ref{app:confounders}), connector design is the most consistent structural predictor. CV partitions models into uniform, graded, and catastrophic classes in a single forward pass. Under sufficient compression, scoring effectiveness becomes connector- and k-dependent: L2 norm aids independent connectors at moderate ratios but reverses at aggressive compression; attention shows the converse on entangling connectors. In the cliff zone ($k{=}0.85$--$0.95$), scoring method alone determines success or failure: at $k{=}0.925$ on $\pi_{0.5}$ Long, L2 preserves 83\% while random collapses to 39\% (44.6\,pp gap). Method differentiation requires pruning stress---at $k{=}0.9$ on OpenVLA, all three scoring methods converge within 3\,pp on Long. A zero-mask ablation confirms the mechanism: on $\pi_{0.5}$, zeroing 10\% of tokens retains 98.0\% SR while physical removal collapses to 9.0\%, proving position disruption---not information loss---drives the failure. Where all deletion fails, VTR recovers over 60\% SR at 75\% compression.
5	
6	Two directions remain open: real-robot validation and adaptive per-task pruning schedules. Code and evaluation data will be released upon acceptance. \textbf{AI disclosure:} This work used AI tools (Claude) for code development and manuscript drafting; all scientific claims are the authors' own.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-27T04:33:50.652489+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/discussion.tex"
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-27T04:33:50.652712+00:00_

1	% Discussion section moved to Appendix (§\ref{app:discussion}) for space.
2	% Three-sentence limitations retained at end of Experiments section.
3	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T04:33:50.652913+00:00_

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
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/appendix.tex"
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-27T04:33:50.653754+00:00_

1	\appendix
2	
3	\section{Extended Discussion}
4	\label{app:discussion}
5	
6	\paragraph{Limitations (extended).}
7	All closed-loop evaluations use the LIBERO simulation benchmark; real-robot validation is absent. The six architectures differ in backbone capacity, vision encoder, and fusion strategy beyond the connector, so the connector effect cannot be causally isolated. $\pi_{0}$ and OFT are evaluated through offline metrics only, without closed-loop verification. The CV diagnostic spans six architectures across all three connector families; closed-loop validation covers four models ($\pi_{0.5}$, X-VLA, OpenVLA, SmolVLA). SmolVLA baselines (59.2\% official, 44.8\% LoRA reproduction) are substantially weaker than those of the other models; whether VTR recovery generalizes to stronger baselines is unknown.
8	
9	\paragraph{Non-monotonicity as structural property.}
10	X-VLA on Goal exhibits non-monotonic degradation: $k{=}0.95$ drops to 53.8\% (L2) and 54.0\% (random), while $k{=}0.9$ recovers to 70.2\% under L2 selection (Table~\ref{tab:main_results}). The 0.2\,pp method gap at $k{=}0.95$ confirms that the anomaly is independent of the token scoring criterion. This pattern is consistent with position sensitivity in the 12-layer BART encoder~\cite{lewis2020bart}, where specific token positions carry disproportionate structural importance regardless of content.
11	
12	\paragraph{$\pi_{0.5}$ random subsampling anomaly and RoPE amplification.}
13	Random selection on $\pi_{0.5}$ Object collapses from 74.0\% at $k{=}0.95$ to 9.0\% at $k{=}0.9$, then recovers to 74.0\% at $k{=}0.7$ (Table~\ref{tab:main_results}). The re-indexing step of our pruning protocol (Section~\ref{sec:pruning_protocol}) contributes to this non-monotonicity. $\pi_{0.5}$'s linear connector preserves a one-to-one mapping between spatial patches and token positions; when random removal shifts surviving tokens to new positions, the backbone's Rotary Position Embeddings (RoPE)~\cite{su2024roformer} encode 
…[truncated 66303 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T04:33:50.654069+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Find paper_framing.md",
  "subagent_type": "Explore",
  "prompt": "Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing \"paper_framing\" in the docs/ or artifacts/ directories. Report the full paths found."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Agent",
  "tool_args": {
    "description": "Find paper_framing.md",
    "subagent_type": "Explore",
    "prompt": "Find any file named paper_framing.md in /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/. Also search for any files containing \"paper_framing\" in the docs/ or artifacts/ directories. Report the full paths found."
  }
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-27T04:33:50.654333+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/experimental_setup.tex"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T04:33:50.654602+00:00_

1	% experimental_setup.tex -- Section 3: Experimental Setup
2	
3	\section{Experimental Setup}
4	\label{sec:experimental_setup}
5	
6	We design a controlled ablation study to test whether vision token reduction can preserve closed-loop VLA performance under any configuration. The study varies three independent axes (scoring function, retention ratio, pruning mechanism) around a shared baseline, using a lightweight learned scorer whose training does not alter the pretrained VLA weights. This section describes the scorer, the ablation design, and the evaluation protocol.
7	
8	\subsection{ACIS Importance Scorer}
9	\label{sec:acis_scorer}
10	
11	To select which vision tokens to prune, we train an Attention-weighted Cumulative Importance Score (ACIS) module that predicts a scalar importance score for each of the 256 projected vision tokens (Section~\ref{sec:smolvla_arch}). The ACIS scorer is a lightweight MLP with 3.46M parameters, constituting 0.77\% of SmolVLA's 451.5M total. At inference time, the scorer adds 0.24\% FLOPs overhead and 0.63\% wall-clock latency overhead relative to the unmodified forward pass.
12	
13	Training follows a Stage-1-only protocol: the ACIS scorer parameters are optimized while all VLA expert weights (vision encoder, MLP connector, LLM backbone, and action head) remain frozen. This separation is deliberate. Fine-tuning the full model during scorer training would conflate two effects: the model could learn to compensate for missing tokens rather than learning to score token importance. By freezing the expert, we ensure that the scorer must identify genuinely important tokens under the original model's representation, and that any subsequent failure cannot be attributed to training-induced degradation of action prediction.
14	
15	The scorer is trained with an importance margin loss that encourages a clear separation between the scores of retained tokens and those of pruned tokens. Given a retention ratio $k$, the loss penalizes configurations whe
…[truncated 3646 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-27T04:33:50.654836+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/sections/results_draft.tex"
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-27T04:33:50.655122+00:00_

1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate token pruning across two VLA architectures on the LIBERO-Object benchmark~\cite{liu2023libero}, comprising 10 tasks with 50 episodes each (500 total). All success rates are reported with Wilson score 95\% confidence intervals.
5	
6	\subsection{SmolVLA: Cliff-Edge Under All Pruning Methods}
7	\label{sec:smolvla_results}
8	
9	SmolVLA~\cite{shukor2025smolvla} uses a pixel-shuffle vision connector that spatially rearranges patch embeddings before projecting them into the language model's embedding space. This operation creates inter-token spatial dependencies: each output token encodes information from a local grid of input patches. We hypothesize that this coupling makes the token sequence fragile under any form of pruning, since removing or masking a single token disrupts the spatial structure that downstream layers expect.
10	
11	\paragraph{Setup.}
12	We use a SmolVLA checkpoint fine-tuned on LIBERO-Object with the ACIS (Adaptive Contextual Importance Scoring) module attached but pruning disabled during training. The baseline (bypass mode) achieves 44.8\% SR (224/500, CI [40.5\%, 49.2\%]).\footnote{The official SmolVLA result on LIBERO is 87.3\% SR, trained with batch size 64 on 8 GPUs. Our reproduction uses a smaller batch size due to compute constraints, yielding a lower baseline. The relevant comparison is the relative change under pruning, not the absolute SR.} We then activate pruning under six configurations that vary three axes: scoring function (learned ACIS vs.\ random), retention ratio $k \in \{0.5, 0.7, 0.9\}$, and pruning mechanism (zero-masking, true token removal, token merging via ToMe~\cite{bolya2023tome}).
13	
14	\paragraph{All configurations collapse to 0\% SR.}
15	Table~\ref{tab:smolvla_ablation} reports the full ablation. Every pruning configuration produces 0\% success rate (Wilson CI upper bounds $\leq$1.26\%; see Table~\ref{tab:smolvla_ablation} for per-condition episode counts). Three 
…[truncated 6743 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T04:33:50.655404+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/paper_framing.md",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/paper_framing.md",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-27T04:33:50.655605+00:00_

artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md
paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 34 · 2026-05-27T04:33:50.655818+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/docs/**/*paper_framing*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/docs/**/*paper_framing*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-27T04:33:50.656027+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/artifacts/**/*paper_framing*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/artifacts/**/*paper_framing*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-27T04:33:50.656238+00:00_

No files found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-27T04:33:50.656418+00:00_

artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md
artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md
artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md
artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-27T04:33:50.656671+00:00_

I found multiple paper_framing.md files in the project directory. Here are the full paths:

**Root level:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md`

**In artifacts/dream_reports:**
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260516T075046/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260520T155932/worst/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/best/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/median/paper_framing.md`
- `/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/dream_reports/dream_20260525T050917/worst/paper_framing.md`

**No matching files found in docs/ directory.**

There are 10 total paper_framing.md files found: 1 at the root level and 9 within the artifacts/dream_reports directory structure across three dated dream report folders (best, median, and worst subdirectories for each).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Agent",
  "elapsed_ms": 2
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-27T04:33:50.656948+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md"
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-27T04:33:50.657748+00:00_

1	# Paper Framing — importance_margin_vla_compress
2	
3	## Target Venue
4	- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)
5	- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)
6	
7	## Title (working)
8	"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility"
9	
10	## Core Insight
11	
12	**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA "threshold-graded" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:
13	
14	**Axis 1 — Token Coupling (connector architecture):**
15	| Type | Connectors | CV Range | Mechanism |
16	|------|-----------|----------|-----------|
17	| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |
18	| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |
19	
20	**Axis 2 — Task Complexity:**
21	| Level | Suites | Characteristics |
22	|-------|--------|----------------|
23	| **Simple** | Object, Spatial | Single-step, pruning impact contained |
24	| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |
25	
26	**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:
27	- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)
28	- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance
29	- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen
30	- Token-independent (π0.5 Goal/Long): 
…[truncated 52058 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 41 · 2026-05-27T04:33:50.658071+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/figures/paper/*.pdf",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/figures/paper/*.pdf",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-27T04:33:50.658309+00:00_

docs/paper/figures/paper/fig_attention_heatmap.pdf
docs/paper/figures/paper/fig_action_divergence.pdf
docs/paper/figures/paper/fig_token_heatmap.pdf
docs/paper/figures/paper/fig_entropy_layers.pdf
docs/paper/figures/paper/fig_pixel_shuffle.pdf
docs/paper/figures/paper/fig_crosssuite.pdf
docs/paper/figures/paper/fig_cliff_model.pdf
docs/paper/figures/paper/fig_degradation_curve.pdf
docs/paper/figures/paper/fig_cliff_edge.pdf
docs/paper/figures/paper/fig_compression_curve.pdf
docs/paper/figures/paper/fig_architecture.pdf
docs/paper/figures/paper/fig_architecture_v2.pdf
docs/paper/figures/paper/fig_method_gap.pdf
docs/paper/figures/paper/fig_hero_overview.pdf
docs/paper/figures/paper/fig_scoring_crossover.pdf
docs/paper/figures/paper/fig_pruning_overview.pdf
docs/paper/figures/paper/fig_teaser.pdf
docs/paper/figures/paper/fig_openvla_sweep.pdf
docs/paper/figures/paper/fig_cliff_highlight.pdf

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-27T04:33:50.658532+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "docs/paper/references.*",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "tool_args": {
    "pattern": "docs/paper/references.*",
    "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress"
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-27T04:33:50.658724+00:00_

docs/paper/references.bib.prev
docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-27T04:33:50.658913+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/ 2>/dev/null | head -30; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib 2>/dev/null || echo \"NO_REFERENCES_BIB\"",
  "description": "Check figures and references files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/figures/paper/ 2>/dev/null | head -30; echo \"---\"; ls -la /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/docs/paper/references.bib 2>/dev/null || echo \"NO_REFERENCES_BIB\"",
    "description": "Check figures and references files"
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-27T04:33:50.659149+00:00_

total 9384
drwxr-xr-x 6 ubuntu ubuntu    4096 May 27 00:27 .
drwxr-xr-x 3 ubuntu ubuntu    4096 May 20 12:35 ..
-rw-r--r-- 1 ubuntu ubuntu   38360 May 18 18:12 fig_action_divergence.pdf
-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture.pdf
-rw-r--r-- 1 ubuntu ubuntu   57833 May 22 14:21 fig_architecture_v2.pdf
-rw-r--r-- 1 ubuntu ubuntu  266752 May 22 14:21 fig_architecture_v2.png
-rw-r--r-- 1 ubuntu ubuntu   34161 May 18 18:12 fig_attention_heatmap.pdf
-rw-r--r-- 1 ubuntu ubuntu   34985 May 22 14:18 fig_cliff_edge.pdf
-rw-r--r-- 1 ubuntu ubuntu   33320 May 27 00:27 fig_cliff_highlight.pdf
-rw-r--r-- 1 ubuntu ubuntu  154046 May 27 00:27 fig_cliff_highlight.png
-rw-r--r-- 1 ubuntu ubuntu   37441 May 22 14:14 fig_cliff_model.pdf
-rw-r--r-- 1 ubuntu ubuntu   26360 May 22 14:18 fig_compression_curve.pdf
-rw-r--r-- 1 ubuntu ubuntu   31132 May 22 14:14 fig_crosssuite.pdf
-rw-r--r-- 1 ubuntu ubuntu  197642 May 22 14:14 fig_crosssuite.png
-rw-r--r-- 1 ubuntu ubuntu   57361 May 22 14:18 fig_degradation_curve.pdf
-rw-r--r-- 1 ubuntu ubuntu  336496 May 22 14:18 fig_degradation_curve.png
-rw-r--r-- 1 ubuntu ubuntu  175091 May 22 13:34 fig_degradation_overview.png
-rw-r--r-- 1 ubuntu ubuntu   30759 May 22 14:14 fig_entropy_layers.pdf
-rw-r--r-- 1 ubuntu ubuntu  151216 May 22 14:14 fig_entropy_layers.png
-rw-r--r-- 1 ubuntu ubuntu  311633 May 24 08:26 fig_hero_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu 2126046 May 24 08:26 fig_hero_overview.png
-rw-r--r-- 1 ubuntu ubuntu 3768870 May 24 08:26 fig_hero_overview_real.png
-rw-r--r-- 1 ubuntu ubuntu   22092 May 24 02:11 fig_method_gap.pdf
-rw-r--r-- 1 ubuntu ubuntu  100579 May 24 02:11 fig_method_gap.png
-rw-r--r-- 1 ubuntu ubuntu   29272 May 26 21:33 fig_openvla_sweep.pdf
-rw-r--r-- 1 ubuntu ubuntu  226567 May 26 21:33 fig_openvla_sweep.png
-rw-r--r-- 1 ubuntu ubuntu   23434 May 22 14:14 fig_pixel_shuffle.pdf
-rw-r--r-- 1 ubuntu ubuntu   35105 May 25 20:08 fig_pruning_overview.pdf
-rw-r--r-- 1 ubuntu ubuntu  128828 May 25
…[truncated 198 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Bash",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-27T04:33:50.659535+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__register_artifact",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-27T04:33:50.659744+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-27T04:33:50.660001+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
  "content": "# Paper Section Audit — CoRL 2026 Submission\n\n**Audit date**: 2026-05-27  \n**Deadline**: ~5h remaining  \n**Paper location**: `docs/paper/` (main.tex + section files)  \n**Main structure**: Abstract → Introduction → Related Work → Method → Experiments → Discussion → Conclusion → Appendix\n\n---\n\n## Section Status Summary\n\n| Section | 文件 | 状态 | 具体问题 | 优先级 |\n|---------|------|------|----------|--------|\n| Abstract | `abstract.tex` | **定稿** | \"five VLA architectures\" vs Method \"six\" — 需统一 | P2 |\n| Introduction | `introduction.tex` | **定稿** | 与 paper_framing 2-axis framework 对齐，claims 一致 | — |\n| Related Work | `related_work.tex` | **定稿** | 完整，覆盖 6 篇 concurrent work | — |\n| Method | `method.tex` | **定稿** | 6 模型 Table 1 完整，CV 公式、VTR 描述清晰 | — |\n| Experiments | `experiments.tex` | **待数据/待修改** | 3 个关键问题，见下 | **P0/P1** |\n| Discussion | `analysis.tex` | **定稿** | OpenVLA sweep 分析完整，limitations 在位 | — |\n| Conclusion | `conclusion.tex` | **定稿** | 5 claims 总结，AI disclosure 已加 | — |\n| Appendix | `appendix.tex` | **基本定稿** | ~820 行，SmolVLA baseline 不一致需修 | P1 |\n| References | `references.bib` | **存在** | 未做编译验证 | P3 |\n| Figures | `figures/paper/` | **完整** | 19 个 PDF 全在位，所有 \\includegraphics 有对应文件 | — |\n\n---\n\n## Critical Issues (P0)\n\n### 1. π0.5 Goal/Long 数据污染 (D248)\n\ncqa1 上的 π0.5 实验使用宽松 success 条件 (`done|reward>0.5`)，导致 SR 可能虚高。\n\n**受影响的 Table 2 单元格**:\n| Suite | 受影响列 | 当前值 | 可信度 |\n|-------|----------|--------|--------|\n| Goal | baseline | 96.4% | **不可信** — 可能虚高 |\n| Goal | k=0.95 (89.4/84.0) | 全部 | **不可信** |\n| Goal | k=0.9 (90.6/62.2) | 全部 | **不可信** |\n| Goal | k=0.7 (71.2/78.2) | 全部 | **不可信** |\n| Goal | k=0.5 (59.2/73.6) | 全部 | **不可信** |\n| Long | k=0.7 (63.2/64.6) | 全部 | **不可信** (k≤0.85) |\n| Long | k=0.5 (50.2/50.2) | 全部 | **不可信** (k≤0.85) |\n| Long | baseline (91.6%) | — | **待确认** — 来源需查 |\n| Long | k=0.95 (86.8/61.2) | — | **可信** (k≥0.9) |\n| Long | k=0.9 (81.0/31.8) | — | **可信** (k≥0.9) |\n\n**受影响的论文 claims**:\n- Abstract: \"task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to 20×\" — 20× 来自 X-VLA（不受影响），但 π0.5 Goal/Long 数据支撑同一论点\n- Sec 5.5 (Experiments): importance margin gradient \"Object +93pp > Goal +35.2pp > Long +28.6pp\" — Goal 和 Long 的 margin 值依赖污染数据\n- Sec 5.7 (cliff highlight): π0.5 Long k=0.85 random=49.4% 对比 — k=0.85 处于 k≤0.85 污染区间\n- Discussion: OpenVLA 的 task complexity 分析不受影响（独立数据源）\n\n**Strict 重跑进度**: k=0.95/0.9/0.85 Attn Long 正在进行中。\n\n**建议处理方案**:\n- **方案 A (保守)**: 从 Table 2 移除所有不可信 π0.5 Goal 数据，标注 \"—\"，仅保留 Object/Spatial/Long k≥0.9。Task complexity 论点仅用 X-VLA 数据（不受污染）\n- **方案 B (折中)**: 保留数据但加脚注 \"π0.5 Goal and Long (k≤0.85) results use a lenient success criterion; strict re-evaluation in progress. X-VLA cross-suite patterns (unaffected) provide independent support for the task complexity claim.\"\n- **方案 C**: 如果 strict 重跑在截止前完成，替换数据\n\n### 2. Table 2 数据缺口 (\"--\" 单元格)\n\n共 19+ 个 \"--\" 单元格：\n\n| 模型 | 缺失 | 影响 |\n|------|------|------|\n| X-VLA Spatial | k=0.7 L2 | 文中未引用 |\n| X-VLA Long | k=0.7 L2/R | 文中未引用 |\n| OpenVLA Object | k=0.95 R, k=0.7 L2/R | k=0.95 R 缺失稍影响叙事 |\n| OpenVLA Goal | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Spatial | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Long | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n\n**评估**: 论文叙事主要围绕 k=0.9 和 k=0.5 展开。OpenVLA 的 k=0.9 三方法对比数据完整（含 attention†），支撑 scoring crossover 论点。X-VLA 的 attention 对比在 k=0.5 完整（Table 8）。**缺口不阻塞核心 claims，但 Table 2 视觉上稀疏。**\n\n**建议**: 接受现状，或将 OpenVLA 改为仅展示 k=0.9 和 k=0.5 两列（去掉 k=0.95/k=0.7 空列）。\n\n---\n\n## High Priority Issues (P1)\n\n### 3. SmolVLA 跨 suite baselines 不一致\n\n| Suite | Table 2 (main) | VTR cross-suite table (App) | paper_framing |\n|-------|----------------|---------------------------|---------------|\n| Object | 59.2% (official) | 44.8% (LoRA) | 59.2% official |\n| Spatial | 44.6% | 51.8% | 43.8% or 44.6% |\n| Goal | 60.8% | 63.0% | 60.8% |\n\n- Table 2 用 official checkpoint baseline；VTR appendix 用 LoRA checkpoint baseline\n- Spatial 有三个不同值 (43.8% / 44.6% / 51.8%)\n- 论文 appendix 文本已做 caveat 处理，但数字混乱容易让 reviewer 质疑\n\n**建议**: 在 VTR cross-suite table (Tab 10) 加脚注明确说明 \"baselines from LoRA-trained checkpoint (batch size 4); main table baselines from official checkpoint\"。统一 Spatial 基线值。\n\n### 4. \"Five\" vs \"Six\" architectures 不一致\n\n- Abstract line 4: \"five VLA architectures (450M--7B parameters)\"\n- Method Sec 3.1 line 7: \"six VLA architectures spanning three vision connector families\"\n- Table 1 列出 6 行（含 OFT）\n\n**建议**: 统一为 \"six VLA architectures\" 或在 abstract 说 \"five VLA architectures (with a sixth offline variant)\"。最简单是改 abstract 为 \"six\"。\n\n### 5. X-VLA baseline 小幅偏差\n\n| Suite | Table 2 | paper_framing |\n|-------|---------|---------------|\n| Spatial | 93.0% | 91.6% |\n| Goal | 98.4% | 98.0% |\n\n可能来自不同 eval seed 或不同 checkpoint。Table 2 是论文定稿数据，paper_framing 是早期记录。**如果 Table 2 数据可信，以 Table 2 为准。** 但需确认 93.0% 和 98.4% 来源无误。\n\n---\n\n## Medium Priority Issues (P2)\n\n### 6. discussion.tex 是空 stub\n\n文件内容仅为注释：\"Discussion section moved to Appendix\"。实际 Discussion 内容在 `analysis.tex`（标题为 `\\section{Discussion}`，label 为 `sec:analysis`）。main.tex include 的是 `\\input{analysis}`。功能正常但维护混乱。\n\n### 7. sections/ 目录残留旧稿\n\n`docs/paper/sections/` 下有 `results_draft.tex`, `analysis_draft.tex`, `related_work_draft.tex` 等旧版文件，不被 main.tex include。不影响编译但增加困惑。\n\n### 8. Constraint C001 合规性\n\nC001 要求 \"Spatial suite 对比禁止用 LoRA baseline (6.2%)\"。检查结果：\n- VTR cross-suite table 中 Spatial baseline=51.8%，VTR=53.2%（差值仅 1.4pp）\n- 文本明确说 \"we therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline\"\n- **合规** — 未使用 LoRA 6.2% baseline 做对比\n\n---\n\n## Low Priority Issues (P3)\n\n### 9. LaTeX 编译未验证\n\nreferences.bib 存在（23KB），所有 figure PDF 在位。未实际运行 `pdflatex` 验证编译。建议在提交前做一次完整编译。\n\n### 10. Appendix 长度\n\nAppendix 约 820 行 LaTeX，包含 18 个 tables/figures。CoRL 通常不限 appendix 页数，但过长可能影响 reviewer 体验。当前内容信息密度高，无明显冗余。\n\n---\n\n## Claim-Framing 一致性检查\n\n| Core Claim (paper_framing) | 论文中对应 | 一致性 |\n|---------------------------|-----------|--------|\n| Claim 1: 2-Axis Framework | Sec 4.2 + Fig 1 teaser | **一致** — connector × task complexity |\n| Claim 2: Pixel-shuffle entanglement | Sec 4.3 + Fig 5 | **一致** — 0% at k=0.95, official+LoRA 双 checkpoint |\n| Claim 3: Connector determines tolerance | Sec 3.1 Table 1 + Sec 4.2-4.5 | **一致** — CV spectrum 0.038→0.314 |\n| Claim 4: VTR recovery | Sec 4.6 + Table 4 | **一致** — 60.1±1.3% at M=32, MLP adapter control |\n| Claim 5: CV predicts optimal strategy | Sec 4.5 + Table 6 (appendix) | **一致** — monotonic Δ(R-L2) trend |\n\n**额外 claims 在论文但不在 framing**:\n- Zero-mask ablation (Sec 4.4): 89pp gap，position disruption — 论文中新增的重要发现\n- Per-task reversal within L2-dominant regimes (Sec 4.5 末段): Task 6 reversal — 细粒度分析\n\n---\n\n## 优先行动建议 (按时间紧迫度)\n\n1. **[P0, 30min]** 决定 π0.5 Goal/Long 污染数据处理方案 (A/B/C)，如选 B 则写脚注\n2. **[P1, 10min]** 统一 abstract \"five\"→\"six\" architectures\n3. **[P1, 15min]** 确认 X-VLA Spatial=93.0% 和 Goal=98.4% 数据来源\n4. **[P1, 15min]** 统一 SmolVLA Spatial baseline (44.6% vs 51.8% vs 43.8%)，加 VTR table 脚注\n5. **[P2, 5min]** 确认 Table 2 \"--\" 缺口可接受\n6. **[P3, 10min]** 运行一次完整 LaTeX 编译\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
    "content": "# Paper Section Audit — CoRL 2026 Submission\n\n**Audit date**: 2026-05-27  \n**Deadline**: ~5h remaining  \n**Paper location**: `docs/paper/` (main.tex + section files)  \n**Main structure**: Abstract → Introduction → Related Work → Method → Experiments → Discussion → Conclusion → Appendix\n\n---\n\n## Section Status Summary\n\n| Section | 文件 | 状态 | 具体问题 | 优先级 |\n|---------|------|------|----------|--------|\n| Abstract | `abstract.tex` | **定稿** | \"five VLA architectures\" vs Method \"six\" — 需统一 | P2 |\n| Introduction | `introduction.tex` | **定稿** | 与 paper_framing 2-axis framework 对齐，claims 一致 | — |\n| Related Work | `related_work.tex` | **定稿** | 完整，覆盖 6 篇 concurrent work | — |\n| Method | `method.tex` | **定稿** | 6 模型 Table 1 完整，CV 公式、VTR 描述清晰 | — |\n| Experiments | `experiments.tex` | **待数据/待修改** | 3 个关键问题，见下 | **P0/P1** |\n| Discussion | `analysis.tex` | **定稿** | OpenVLA sweep 分析完整，limitations 在位 | — |\n| Conclusion | `conclusion.tex` | **定稿** | 5 claims 总结，AI disclosure 已加 | — |\n| Appendix | `appendix.tex` | **基本定稿** | ~820 行，SmolVLA baseline 不一致需修 | P1 |\n| References | `references.bib` | **存在** | 未做编译验证 | P3 |\n| Figures | `figures/paper/` | **完整** | 19 个 PDF 全在位，所有 \\includegraphics 有对应文件 | — |\n\n---\n\n## Critical Issues (P0)\n\n### 1. π0.5 Goal/Long 数据污染 (D248)\n\ncqa1 上的 π0.5 实验使用宽松 success 条件 (`done|reward>0.5`)，导致 SR 可能虚高。\n\n**受影响的 Table 2 单元格**:\n| Suite | 受影响列 | 当前值 | 可信度 |\n|-------|----------|--------|--------|\n| Goal | baseline | 96.4% | **不可信** — 可能虚高 |\n| Goal | k=0.95 (89.4/84.0) | 全部 | **不可信** |\n| Goal | k=0.9 (90.6/62.2) | 全部 | **不可信** |\n| Goal | k=0.7 (71.2/78.2) | 全部 | **不可信** |\n| Goal | k=0.5 (59.2/73.6) | 全部 | **不可信** |\n| Long | k=0.7 (63.2/64.6) | 全部 | **不可信** (k≤0.85) |\n| Long | k=0.5 (50.2/50.2) | 全部 | **不可信** (k≤0.85) |\n| Long | baseline (91.6%) | — | **待确认** — 来源需查 |\n| Long | k=0.95 (86.8/61.2) | — | **可信** (k≥0.9) |\n| Long | k=0.9 (81.0/31.8) | — | **可信** (k≥0.9) |\n\n**受影响的论文 claims**:\n- Abstract: \"task complexity amplifies connector-dependent patterns, with multi-step tasks magnifying entangling-connector losses by up to 20×\" — 20× 来自 X-VLA（不受影响），但 π0.5 Goal/Long 数据支撑同一论点\n- Sec 5.5 (Experiments): importance margin gradient \"Object +93pp > Goal +35.2pp > Long +28.6pp\" — Goal 和 Long 的 margin 值依赖污染数据\n- Sec 5.7 (cliff highlight): π0.5 Long k=0.85 random=49.4% 对比 — k=0.85 处于 k≤0.85 污染区间\n- Discussion: OpenVLA 的 task complexity 分析不受影响（独立数据源）\n\n**Strict 重跑进度**: k=0.95/0.9/0.85 Attn Long 正在进行中。\n\n**建议处理方案**:\n- **方案 A (保守)**: 从 Table 2 移除所有不可信 π0.5 Goal 数据，标注 \"—\"，仅保留 Object/Spatial/Long k≥0.9。Task complexity 论点仅用 X-VLA 数据（不受污染）\n- **方案 B (折中)**: 保留数据但加脚注 \"π0.5 Goal and Long (k≤0.85) results use a lenient success criterion; strict re-evaluation in progress. X-VLA cross-suite patterns (unaffected) provide independent support for the task complexity claim.\"\n- **方案 C**: 如果 strict 重跑在截止前完成，替换数据\n\n### 2. Table 2 数据缺口 (\"--\" 单元格)\n\n共 19+ 个 \"--\" 单元格：\n\n| 模型 | 缺失 | 影响 |\n|------|------|------|\n| X-VLA Spatial | k=0.7 L2 | 文中未引用 |\n| X-VLA Long | k=0.7 L2/R | 文中未引用 |\n| OpenVLA Object | k=0.95 R, k=0.7 L2/R | k=0.95 R 缺失稍影响叙事 |\n| OpenVLA Goal | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Spatial | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n| OpenVLA Long | k=0.95, k=0.7, k=0.5 全缺 | 仅有 k=0.9 三方法对比 |\n\n**评估**: 论文叙事主要围绕 k=0.9 和 k=0.5 展开。OpenVLA 的 k=0.9 三方法对比数据完整（含 attention†），支撑 scoring crossover 论点。X-VLA 的 attention 对比在 k=0.5 完整（Table 8）。**缺口不阻塞核心 claims，但 Table 2 视觉上稀疏。**\n\n**建议**: 接受现状，或将 OpenVLA 改为仅展示 k=0.9 和 k=0.5 两列（去掉 k=0.95/k=0.7 空列）。\n\n---\n\n## High Priority Issues (P1)\n\n### 3. SmolVLA 跨 suite baselines 不一致\n\n| Suite | Table 2 (main) | VTR cross-suite table (App) | paper_framing |\n|-------|----------------|---------------------------|---------------|\n| Object | 59.2% (official) | 44.8% (LoRA) | 59.2% official |\n| Spatial | 44.6% | 51.8% | 43.8% or 44.6% |\n| Goal | 60.8% | 63.0% | 60.8% |\n\n- Table 2 用 official checkpoint baseline；VTR appendix 用 LoRA checkpoint baseline\n- Spatial 有三个不同值 (43.8% / 44.6% / 51.8%)\n- 论文 appendix 文本已做 caveat 处理，但数字混乱容易让 reviewer 质疑\n\n**建议**: 在 VTR cross-suite table (Tab 10) 加脚注明确说明 \"baselines from LoRA-trained checkpoint (batch size 4); main table baselines from official checkpoint\"。统一 Spatial 基线值。\n\n### 4. \"Five\" vs \"Six\" architectures 不一致\n\n- Abstract line 4: \"five VLA architectures (450M--7B parameters)\"\n- Method Sec 3.1 line 7: \"six VLA architectures spanning three vision connector families\"\n- Table 1 列出 6 行（含 OFT）\n\n**建议**: 统一为 \"six VLA architectures\" 或在 abstract 说 \"five VLA architectures (with a sixth offline variant)\"。最简单是改 abstract 为 \"six\"。\n\n### 5. X-VLA baseline 小幅偏差\n\n| Suite | Table 2 | paper_framing |\n|-------|---------|---------------|\n| Spatial | 93.0% | 91.6% |\n| Goal | 98.4% | 98.0% |\n\n可能来自不同 eval seed 或不同 checkpoint。Table 2 是论文定稿数据，paper_framing 是早期记录。**如果 Table 2 数据可信，以 Table 2 为准。** 但需确认 93.0% 和 98.4% 来源无误。\n\n---\n\n## Medium Priority Issues (P2)\n\n### 6. discussion.tex 是空 stub\n\n文件内容仅为注释：\"Discussion section moved to Appendix\"。实际 Discussion 内容在 `analysis.tex`（标题为 `\\section{Discussion}`，label 为 `sec:analysis`）。main.tex include 的是 `\\input{analysis}`。功能正常但维护混乱。\n\n### 7. sections/ 目录残留旧稿\n\n`docs/paper/sections/` 下有 `results_draft.tex`, `analysis_draft.tex`, `related_work_draft.tex` 等旧版文件，不被 main.tex include。不影响编译但增加困惑。\n\n### 8. Constraint C001 合规性\n\nC001 要求 \"Spatial suite 对比禁止用 LoRA baseline (6.2%)\"。检查结果：\n- VTR cross-suite table 中 Spatial baseline=51.8%，VTR=53.2%（差值仅 1.4pp）\n- 文本明确说 \"we therefore do not treat the Spatial comparison as evidence that re-encoding improves over the uncompressed official baseline\"\n- **合规** — 未使用 LoRA 6.2% baseline 做对比\n\n---\n\n## Low Priority Issues (P3)\n\n### 9. LaTeX 编译未验证\n\nreferences.bib 存在（23KB），所有 figure PDF 在位。未实际运行 `pdflatex` 验证编译。建议在提交前做一次完整编译。\n\n### 10. Appendix 长度\n\nAppendix 约 820 行 LaTeX，包含 18 个 tables/figures。CoRL 通常不限 appendix 页数，但过长可能影响 reviewer 体验。当前内容信息密度高，无明显冗余。\n\n---\n\n## Claim-Framing 一致性检查\n\n| Core Claim (paper_framing) | 论文中对应 | 一致性 |\n|---------------------------|-----------|--------|\n| Claim 1: 2-Axis Framework | Sec 4.2 + Fig 1 teaser | **一致** — connector × task complexity |\n| Claim 2: Pixel-shuffle entanglement | Sec 4.3 + Fig 5 | **一致** — 0% at k=0.95, official+LoRA 双 checkpoint |\n| Claim 3: Connector determines tolerance | Sec 3.1 Table 1 + Sec 4.2-4.5 | **一致** — CV spectrum 0.038→0.314 |\n| Claim 4: VTR recovery | Sec 4.6 + Table 4 | **一致** — 60.1±1.3% at M=32, MLP adapter control |\n| Claim 5: CV predicts optimal strategy | Sec 4.5 + Table 6 (appendix) | **一致** — monotonic Δ(R-L2) trend |\n\n**额外 claims 在论文但不在 framing**:\n- Zero-mask ablation (Sec 4.4): 89pp gap，position disruption — 论文中新增的重要发现\n- Per-task reversal within L2-dominant regimes (Sec 4.5 末段): Task 6 reversal — 细粒度分析\n\n---\n\n## 优先行动建议 (按时间紧迫度)\n\n1. **[P0, 30min]** 决定 π0.5 Goal/Long 污染数据处理方案 (A/B/C)，如选 B 则写脚注\n2. **[P1, 10min]** 统一 abstract \"five\"→\"six\" architectures\n3. **[P1, 15min]** 确认 X-VLA Spatial=93.0% 和 Goal=98.4% 数据来源\n4. **[P1, 15min]** 统一 SmolVLA Spatial baseline (44.6% vs 51.8% vs 43.8%)，加 VTR table 脚注\n5. **[P2, 5min]** 确认 Table 2 \"--\" 缺口可接受\n6. **[P3, 10min]** 运行一次完整 LaTeX 编译\n"
  }
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-27T04:33:50.660399+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 51 · 2026-05-27T04:33:50.660665+00:00_

called mcp__agent-ml-research__register_artifact

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact</summary>

```json
{
  "name": "paper_section_audit",
  "type": "report",
  "description": "CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查",
  "project": "importance_margin_vla_compress",
  "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
  "tags": "['paper', 'audit', 'corl2026']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "mcp__agent-ml-research__register_artifact",
  "tool_args": {
    "name": "paper_section_audit",
    "type": "report",
    "description": "CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查",
    "project": "importance_margin_vla_compress",
    "source_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/paper_section_audit.md",
    "tags": "['paper', 'audit', 'corl2026']"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-27T04:33:50.660917+00:00_

{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260527_67ccde\", \"name\": \"paper_section_audit\", \"type\": \"report\", \"description\": \"CoRL 2026 论文各 section 定稿状态盘点：逐节审计状态、数据污染影响、baseline 不一致、claim 对齐检查\", \"path\": \"projects/importance_margin_vla_compress/artifacts/_project/report/paper_section_audit.md\", \"url\": null, \"project\": \"importance_margin_vla_compress\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-27T04:33:39.633720+00:00\", \"tags\": [\"paper\", \"audit\", \"corl2026\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_audit_paper_section_status_20260527T042940",
  "tool": "mcp__agent-ml-research__register_artifact",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 53 · 2026-05-27T04:33:50.661213+00:00_

盘点完成。核心发现：

**论文整体成熟度高** — Abstract/Intro/Related Work/Method/Discussion/Conclusion 均已定稿，figures 全在位，claims 与 paper_framing 一致。

**3 个需立即处理的问题**：

1. **[P0] π0.5 Goal/Long 数据污染** — cqa1 宽松 success 条件影响 Table 2 整行 π0.5 Goal 数据和 Long k≤0.85 数据。建议加脚注说明，并用 X-VLA（不受影响）独立支撑 task complexity claim
2. **[P1] "Five" vs "six" architectures** — Abstract 说 five，Method 说 six，需统一
3. **[P1] SmolVLA Spatial baseline 三个不同值** (43.8%/44.6%/51.8%) — VTR cross-suite table 需加脚注区分 checkpoint 来源

Table 2 有 19+ "--" 缺口，但核心叙事围绕 k=0.9 展开，数据完整，缺口不阻塞。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_audit_paper_section_status_20260527T042940"
}
```

</details>

---
