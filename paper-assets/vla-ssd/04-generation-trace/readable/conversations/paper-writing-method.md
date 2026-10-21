# paper writing method

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 17
- **Recorded user turns:** 0
- **Tool calls:** 8
- **Original source:** `logs/chats/worker_paper_writing_method_20260516T022801.jsonl`
- **Structured JSON:** [`cdbff68a01a9f27d3377.json`](../../sessions/cd/cdbff68a01a9f27d3377.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

17 recorded events

### Tool call

_source line 1 · 2026-05-16T02:29:29.150278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/experiments.tex"
  }
}
```

</details>

---

### Tool result

_source line 2 · 2026-05-16T02:29:29.150682+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Benchmark and model.}
8	We evaluate on the LIBERO-Goal suite~\cite{liu2023_libero}, comprising 10 tabletop manipulation tasks with 50 human demonstrations each.
9	We use OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a vision-language-action model consisting of a SigLIP-SO400M vision encoder~\cite{zhai2023_siglip}, an MLP projector, and a Llama-2 7B language backbone, fine-tuned on the LIBERO-10 split.
10	
11	\paragraph{Representation sources.}
12	We extract representations from five sources:
13	(a)~\textbf{SigLIP+Projector}---the vision encoder output after MLP projection into LLM input space;
14	(b)~\textbf{LLM image\_mean}---the mean of image token activations at each LLM layer, capturing distributed visual information;
15	(c)~\textbf{LLM last\_preaction}---the final token position before action decoding (readout token) at each LLM layer;
16	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} \texttt{cls\_token}; and
17	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} \texttt{patch\_mean}.
18	Sources (d) and (e) serve as external baselines with no VLA training signal.
19	
20	\paragraph{Experimental conditions.}
21	We use a $2 \times 2$ factorial design crossing \emph{training status} (trained vs.\ untrained) with \emph{instruction presence} (with vs.\ without language instruction).
22	The untrained control applies \texttt{from\_config()} to reinitialize the LLM parameters (6.74B random weights) while preserving the frozen SigLIP encoder (0.80B pretrained weights), isolating the LLM's learned contribution from the vision encoder's pretrained geometry.
23	
24	\paragraph{Representational Similarity Analysis (RSA).}
25	Following~\cite{kriegeskorte2008}, we compute pairwise representational dissimilarity matrices (RDMs) for each representation source and for the 7-dimensional action space.
26	We report Spearman rank correlation $\rho$ betwee
…[truncated 13148 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-16T02:29:29.150877+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper"
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-16T02:29:29.151064+00:00_

artifacts/_project/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Glob",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T02:29:29.151246+00:00_

called Write

<details open><summary>🔧 Tool call — Write</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex",
  "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.\n\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.\n\n\\paragraph{Training data.}\nWe fine-tune OpenVLA on the LIBERO-10 split~\\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).\nWe evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.\n\n\\paragraph{Untrained control.}\nTo isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \\texttt{from\\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).\nThe untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.\n\n\\subsection{Representation Extraction}\n\\label{sec:rep_extraction}\n\nWe extract representations from five sources spanning the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),nosep,leftmargin=*]\n    \\item \\textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.\n    \\item \\textbf{LLM image\\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.\n    \\item \\textbf{LLM last\\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.\n    \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.\n    \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.\n\\end{enumerate}\n\nSources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.\n\n\\paragraph{Factorial design.}\nWe cross two factors in a $2 \\times 2$ design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nThis yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.\nExternal baselines (d) and (e) are evaluated once, as they are independent of both factors.\n\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.\n\n\\paragraph{Representational dissimilarity matrices.}\nFor a set of $n$ observations, we compute an $n \\times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.\nWe similarly construct an action RDM from the 7-dimensional action vectors.\n\n\\paragraph{RSA correlation.}\nWe measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ between their upper-triangular elements.\nHigher $\\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.\n\n\\paragraph{Statistical inference.}\nWe compute 95\\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.\nRSA is computed per task and aggregated across the 10 tasks.\n\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.\nWe complement RSA with functional probing~\\cite{alain2017} to measure the action information accessible to a lightweight decoder.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.\n\n\\paragraph{Training protocol.}\nProbes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).\nRepresentations are frozen throughout; only probe parameters are updated.\nWe use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.\n\n\\paragraph{Action-delta probes.}\nIn addition to predicting absolute actions $\\mathbf{a}_t$, we train probes to predict action deltas $\\Delta\\mathbf{a} = \\mathbf{a}_{t+1} - \\mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.\n\n\\subsection{Centered Kernel Alignment}\n\\label{sec:cka}\n\nRSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.\nTo assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} in two variants.\n\n\\paragraph{Linear CKA.}\nLinear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.\nIt is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.\n\n\\paragraph{RDM kernel CKA.}\nWe also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.\n\n\\paragraph{Dimensionality caveat.}\nWhen comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.\nWe report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Write",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex",
    "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate where action-relevant representations originate within a vision-language-action (VLA) model by combining representational similarity analysis, functional probing, and kernel alignment across a factorial design of training and instruction conditions.\n\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\n\\paragraph{Architecture.}\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA model comprising four components: (1)~a SigLIP-SO400M vision encoder~\\cite{zhai2023_siglip} that maps RGB observations to patch-level visual tokens, (2)~an MLP projector that maps vision tokens into the language model's embedding space, (3)~a Llama-2 7B language backbone (32 transformer layers) that processes the concatenated sequence of projected image tokens and tokenized language instructions, and (4)~an action head that decodes 7-dimensional continuous actions (3D translation, 3D rotation, 1D gripper) from the final hidden states.\n\n\\paragraph{Training data.}\nWe fine-tune OpenVLA on the LIBERO-10 split~\\cite{liu2023_libero}, which contains 10 tabletop manipulation tasks with 50 human demonstrations each (500 demonstrations total).\nWe evaluate generalization on LIBERO-Goal, an out-of-distribution benchmark where episodes share initial object configurations but differ in goal specifications.\n\n\\paragraph{Untrained control.}\nTo isolate the LLM's learned contribution from the vision encoder's pretrained geometry, we construct an untrained control by calling \\texttt{from\\_config()} to reinitialize all LLM parameters (6.74B weights drawn from random initialization) while preserving the frozen SigLIP encoder (0.80B pretrained weights).\nThe untrained model processes identical visual inputs through an identical vision encoder but lacks any learned language or action structure in its LLM layers.\n\n\\subsection{Representation Extraction}\n\\label{sec:rep_extraction}\n\nWe extract representations from five sources spanning the VLA processing pipeline and two external baselines:\n\n\\begin{enumerate}[label=(\\alph*),nosep,leftmargin=*]\n    \\item \\textbf{SigLIP+Projector} --- the vision encoder output after MLP projection into the LLM's input space, before any LLM processing. This captures the representation that the LLM receives as input.\n    \\item \\textbf{LLM image\\_mean} --- the mean activation across all image token positions at each of the 32 LLM layers. This captures how the LLM transforms distributed visual information through its depth.\n    \\item \\textbf{LLM last\\_preaction} --- the activation at the final token position before action decoding (the readout token) at each LLM layer. This captures the representation from which actions are directly decoded.\n    \\item \\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} \\texttt{cls\\_token} --- a vision-only baseline pretrained with self-supervised objectives and no language supervision.\n    \\item \\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} \\texttt{patch\\_mean} --- a vision-language baseline pretrained on image-text pairs, serving as a generalization control for VL pretraining effects independent of the VLA pipeline.\n\\end{enumerate}\n\nSources (a)--(c) probe representations within the VLA model itself, while (d) and (e) provide external references with no VLA training signal.\n\n\\paragraph{Factorial design.}\nWe cross two factors in a $2 \\times 2$ design: \\emph{training status} (trained vs.\\ untrained LLM) and \\emph{instruction presence} (with vs.\\ without language instruction).\nThis yields four conditions per LLM representation source, enabling us to disentangle the contributions of LLM training and language grounding to action-relevant structure.\nExternal baselines (d) and (e) are evaluated once, as they are independent of both factors.\n\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt Representational Similarity Analysis (RSA)~\\cite{kriegeskorte2008} to quantify the geometric alignment between neural representations and the action space.\n\n\\paragraph{Representational dissimilarity matrices.}\nFor a set of $n$ observations, we compute an $n \\times n$ representational dissimilarity matrix (RDM) for each representation source using Euclidean distance between representation vectors.\nWe similarly construct an action RDM from the 7-dimensional action vectors.\n\n\\paragraph{RSA correlation.}\nWe measure alignment between a representation RDM and the action RDM via Spearman rank correlation $\\rho$ between their upper-triangular elements.\nHigher $\\rho$ indicates that observations with similar representations also have similar actions, i.e., the representation geometry mirrors the action space geometry.\n\n\\paragraph{Statistical inference.}\nWe compute 95\\% confidence intervals from 10{,}000 bootstrap resamples of observation pairs for all pairwise comparisons.\nRSA is computed per task and aggregated across the 10 tasks.\n\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but does not assess whether action information is linearly decodable from representations.\nWe complement RSA with functional probing~\\cite{alain2017} to measure the action information accessible to a lightweight decoder.\n\n\\paragraph{Probe architecture.}\nWe train two-layer MLP probes (Linear $\\to$ ReLU $\\to$ Linear) mapping from the representation dimensionality to a 256-dimensional hidden layer and then to the 7-dimensional action space.\n\n\\paragraph{Training protocol.}\nProbes are optimized with Adam (learning rate $10^{-3}$, batch size 256) for 50 epochs with early stopping (patience 5 epochs on validation loss).\nRepresentations are frozen throughout; only probe parameters are updated.\nWe use per-task 80/20 train/validation splits and report mean $R^2$ across the 7 action dimensions as the primary metric.\n\n\\paragraph{Action-delta probes.}\nIn addition to predicting absolute actions $\\mathbf{a}_t$, we train probes to predict action deltas $\\Delta\\mathbf{a} = \\mathbf{a}_{t+1} - \\mathbf{a}_t$, which capture the dynamic component of action structure independent of the current action magnitude.\n\n\\paragraph{Statistical comparison.}\nWe use bootstrap paired comparison (10{,}000 resamples) to test whether $R^2$ differences between representation sources are statistically significant.\n\n\\subsection{Centered Kernel Alignment}\n\\label{sec:cka}\n\nRSA captures local geometric alignment---whether pairwise distances in representation space mirror those in action space.\nTo assess global structural preservation, we additionally employ Centered Kernel Alignment (CKA)~\\cite{kornblith2019} in two variants.\n\n\\paragraph{Linear CKA.}\nLinear CKA computes the normalized Hilbert-Schmidt Independence Criterion between linear kernel matrices of two representation sets.\nIt is invariant to orthogonal transformations and isotropic scaling, making it sensitive to global structure rather than local distance preservation.\n\n\\paragraph{RDM kernel CKA.}\nWe also compute CKA using the RDMs themselves as kernel matrices, providing a bridge between the local sensitivity of RSA and the global perspective of linear CKA.\n\n\\paragraph{Dimensionality caveat.}\nWhen comparing high-dimensional representations (e.g., 4096-D LLM activations) with low-dimensional action vectors (7-D), linear CKA may be dominated by the few directions that span the action space, potentially inflating similarity estimates.\nWe report both CKA variants alongside RSA to ensure that conclusions are robust to metric choice.\n"
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T02:29:29.151461+00:00_

File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "Write",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T02:29:29.151591+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__save_project_file",
    "max_results": "1"
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T02:29:29.151712+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T02:29:29.151842+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "register_artifact",
  "max_results": "3"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "register_artifact",
    "max_results": "3"
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T02:29:29.151996+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T02:29:29.152124+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "artifact",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "artifact",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T02:29:29.152246+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T02:29:29.152358+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "write_paper",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "write_paper",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-16T02:29:29.152468+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T02:29:29.152576+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "paper section project",
  "max_results": "5"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "paper section project",
    "max_results": "5"
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T02:29:29.152690+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "worker_paper_writing_method_20260516T022801",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-16T02:29:29.152837+00:00_

`register_artifact` 工具不可用。文件已写入指定路径。

`method.tex` 已生成：`/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/_project/paper/method.tex`

结构：
- **2.1 Model and Data** — OpenVLA-7B 架构、LIBERO-10/Goal 数据、untrained control 设计
- **2.2 Representation Extraction** — 5 个表征源 (a)-(e) + 2×2 factorial design
- **2.3 RSA** — RDM 构建、Spearman ρ、bootstrap CI
- **2.4 Functional Action Probes** — MLP 探针架构/训练、R²、action-delta probes、统计检验
- **2.5 CKA** — Linear CKA + RDM kernel CKA、维度不匹配 caveat

术语和引用格式与 `experiments.tex` 保持一致，无实验结果数字。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "worker_paper_writing_method_20260516T022801"
}
```

</details>

---
