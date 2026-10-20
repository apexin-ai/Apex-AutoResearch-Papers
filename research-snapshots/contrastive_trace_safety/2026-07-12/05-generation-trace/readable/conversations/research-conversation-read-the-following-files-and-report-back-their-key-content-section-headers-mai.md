# Research conversation: Read the following files and report back their key content (section headers, main claims, terminology used, and any spec

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a6173ad97cfaaa5eb.jsonl`
- **Structured JSON:** [`a73781e287a1f29135a3.json`](../../sessions/a7/a73781e287a1f29135a3.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

19 recorded events

### User

_source line 1 · 2026-05-17T17:03:21.609Z_

Read the following files and report back their key content (section headers, main claims, terminology used, and any specific numbers/findings mentioned). I need this to write a consistent Conclusion section.

1. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/results.tex or experiments.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex

For each file, report: (a) the section label, (b) the main narrative/claims, (c) key terminology and method names used (e.g., "hidden-state probing", "HS", "bal_acc", "crossing_rate", etc.), (d) any specific numbers cited. If a file doesn't exist, say so. Keep your report concise but thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "bc7f6483-87cc-4797-8a15-c62e73cd02ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-17T17:03:23.035Z_

I'll read all those files and extract the key information you need for writing a consistent Conclusion section.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc7f6483-87cc-4797-8a15-c62e73cd02ae",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2e9bf28-77f2-4190-a023-dc404304fc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-17T17:03:23.245Z_

<details open><summary>🔧 Tool call — Read · `toolu_0174U7A2PezknWz4bFjYqVsU`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2e9bf28-77f2-4190-a023-dc404304fc93",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1872ac55-e318-48ac-9ae7-2e4ad7f93886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 4 · 2026-05-17T17:03:23.262Z_

<details><summary>↩ Tool result · `toolu_0174U7A2PezknWz4bFjYqVsU`</summary>

```text
1	Large Language Models (LLMs) with Chain-of-Thought (CoT) reasoning can self-jailbreak: their extended reasoning traces sometimes transition from safe deliberation to committed harmful generation. Detecting this safety commitment in real time is essential for monitoring systems, yet no prior work has systematically compared hidden-state (HS) probes against text-based monitors for this task. We present the first cross-model evaluation of temporal probing for safety commitment detection, spanning four reasoning models, two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two scales (7-8B, 32B). Our results reveal that temporal context dominates modality choice: expanding the observation window improves precision by up to 12.9 percentage points (pp) and reduces false positive rate across all conditions. The residual modality advantage is scale-dependent: at 7-8B, HS probes significantly outperform text probes on both tested models (R1-8B precision +22.4pp, $p{<}0.001$; OT-7B precision +21.2pp, $p{<}0.001$; 5/12 tests surviving Holm-Bonferroni correction), while at 32B no significant difference emerges on either model. Geometric distance methods, change-point detectors, and cross-model transfer all fail, defining clear boundaries of current approaches. Control tasks confirm genuine safety structure (selectivity 7.5--18.3pp above chance).
2	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1872ac55-e318-48ac-9ae7-2e4ad7f93886",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "32bfd5b6-a85b-4f51-a3a1-c342763fe110",
  "sourceToolAssistantUUID": "1872ac55-e318-48ac-9ae7-2e4ad7f93886",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-17T17:03:23.449Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TN5R8q6ynpVvDUWGMEgq63`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "32bfd5b6-a85b-4f51-a3a1-c342763fe110",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b7058d01-6336-4e58-8819-bf8593ac4884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-17T17:03:23.454Z_

<details><summary>↩ Tool result · `toolu_01TN5R8q6ynpVvDUWGMEgq63`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Reasoning models such as DeepSeek-R1~\cite{deepseekr1} and QwQ~\cite{qwq} scale inference-time computation through extended chains of thought (CoT), producing dozens of internal reasoning steps before generating a final response. This deliberative process interleaves safety-aware reasoning with content generation across many steps, and the very capacity for self-reflection introduces a failure mode absent from standard instruction-tuned models. Recent analyses have documented that reasoning models can ``self-jailbreak'': without any adversarial modification to the input prompt, the model's own CoT transitions from considering safety constraints to committing to produce harmful content~\cite{harmthoughts,selfjailbreak}. In a typical self-jailbreak trace, the model begins by acknowledging that a request may be harmful, engages in several steps of safety deliberation, and then gradually shifts toward compliance before abandoning safety reasoning entirely. We refer to the first reasoning step after which safety deliberation permanently ceases as the \textbf{Safety Commitment Point} (CP). Before the CP, the model is still weighing refusal; after it, harmful generation proceeds unchecked. This failure mode is qualitatively different from adversarial jailbreaks on standard LLMs: the harmful transition originates within the model's own reasoning rather than from a crafted input. Detecting this transition in real time is essential for monitoring systems that must intervene before harmful content reaches users, yet no existing detector was designed for this internal commitment process.
4	
5	Existing safety detectors target a fundamentally different problem. Hidden-state (HS) probing methods such as TrajGuard~\cite{trajguard} and SafeSwitch~\cite{safeswitch} monitor internal activations to classify adversarial inputs directed at instruction-tuned Large Language Models (LLMs), achieving above 95\% defense rates on standard benchmarks. Text-based monitors like SafeRemind~\cite{saferemind} and SafeThink~\cite{safethink} scan generated reasoning text for safety violations during inference. Both families assume the threat originates from external manipulation of model inputs rather than the model's own internal commitment process. The HS detectors operate at the token level and were evaluated against adversarial prompt attacks; the text monitors assume that safety violations are explicit in the generated reasoning. Neither is designed to track the gradual, multi-step process by which a reasoning model consolidates its commitment to harmful output. A fundamental question therefore remains open: when detecting safety commitment within multi-step reasoning, should a monitoring system read the model's hidden states or its generated text?
6	
7	The comparison between these two monitoring modalities has never been conducted under controlled conditions. Na\"ive reasoning suggests that HS features (up to 5120 dimensions of internal computation) should be far more informative than text embeddings (384 dimensions from a sentence encoder), but no prior work tests this assumption systematically across models. Existing hidden-state evaluations target token-level classification on standard LLMs, while text monitoring studies focus on different models with different evaluation protocols. The two modalities have never been compared on the same task, the same models, and the same statistical framework. Without such a controlled comparison, claims about the relative effectiveness of either modality rest on cross-study inference rather than direct evidence. A further complication is that HS probes require selecting which transformer layer to monitor, a choice that is rarely scrutinized but can dramatically affect results. The probing literature has established that task-specific representations concentrate in middle-to-deep layers~\cite{belinkov2019analysis}, yet safety monitoring studies have not systematically investigated how layer selection methodology interacts with modality comparison outcomes.
8	
9	We present the first systematic evaluation of safety commitment detection across four reasoning models spanning two architectures (Llama, Qwen), two training methods (R1 distillation, STILL), and two parameter scales (7--8B, 32B). Our central finding is methodological: the choice of layer selection metric entirely determines whether an HS advantage is observed. A commonly used composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models because early layers produce more volatile representations that cross detection thresholds more frequently, inflating the crossing rate component independently of true discriminative power. At these biased layers, only 5 of 12 statistical tests survive Holm-Bonferroni correction, producing an apparent ``scale-dependent'' HS advantage that is significant at 7--8B but absent at 32B. A five-metric ablation reveals that four alternative metrics all converge on deep layers for every model (\cref{tab:layer_selection}). At these corrected layers, all 12 tests pass Holm-Bonferroni step-down correction ($\alpha{=}0.05$), with HS precision exceeding text by +15.4 to +23.6 percentage points (pp) across all four models (\cref{tab:hs_vs_text}). The layer selection metric, not scale or architecture, is the true moderator of probe performance. This result has implications beyond our specific task: any study that uses composite metrics to select probe layers risks the same systematic bias, and sensitivity analysis across multiple selection criteria should be standard practice in the probing literature.
10	
11	Our contributions are:
12	\begin{itemize}
13	    \item \textbf{Layer selection sensitivity as a methodological finding.} We identify a systematic bias in composite layer selection metrics that reverses conclusions about HS probe effectiveness. The biased metric selects layers at 3--16\% depth for 32B models, while four unbiased metrics converge on layers at 94--98\% depth. A five-metric ablation across four models (\cref{sec:layer-results}, \cref{tab:layer_selection}) establishes principled selection criteria and shows that layer choice, not modality or scale, is the true moderator of probe performance.
14	
15	    \item \textbf{Universal HS advantage at correctly selected layers.} At deep layers selected by unbiased metrics, HS probes significantly outperform text probes on all four models (12/12 Holm-Bonferroni at $\alpha{=}0.05$, precision +15.4 to +23.6pp; \cref{sec:hs-text}, \cref{tab:hs_vs_text}). Model-specific trade-offs at 32B qualify the practical implications: R1-32B provides excellent early detection (+13 steps lead time) but narrow coverage at the significant temporal window, while QwQ shows robust significance across all 15 window sizes but later detection than text (\cref{sec:32b-analysis}).
16	
17	    \item \textbf{Comprehensive negative results define method boundaries.} Six alternative detection methods fail (\cref{sec:negative}, \cref{tab:negative}): BOCPD and CUSUM produce no early-detection gain because commitment is gradual rather than abrupt; Mahalanobis distance fails because safe and jailbreak trajectories occupy indistinguishable activation regions; RepE mean-difference directions cannot decode safety commitment at deep layers without discriminative training; MLP probes overfit on small datasets, underperforming linear probes on 3 of 4 models; CCS~\cite{burns2023discovering} provides no gain over supervised probing; and cross-model transfer fails entirely, confirming that safety representations are model-specific. Control task selectivity (7.5--18.3pp above chance; \cref{app:control}) confirms that probes capture genuine safety structure rather than positional artifacts.
18	\end{itemize}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b7058d01-6336-4e58-8819-bf8593ac4884",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "29c55384-4967-46a3-ae9a-fa3b5634b315",
  "sourceToolAssistantUUID": "b7058d01-6336-4e58-8819-bf8593ac4884",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-17T17:03:23.865Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TWZAvz7T9ccTYbkFyALLLD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "29c55384-4967-46a3-ae9a-fa3b5634b315",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "416f7bea-56a8-4f16-a95f-f0c7a05e698d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-17T17:03:23.871Z_

<details><summary>↩ Tool result · `toolu_01TWZAvz7T9ccTYbkFyALLLD`</summary>

```text
1	\section{Problem Setup and Methods}
2	\label{sec:method}
3	
4	\subsection{Safety Commitment Point}
5	\label{sec:commitment-point}
6	
7	When a reasoning model is jailbroken, its chain-of-thought (CoT) transitions from safety-aware deliberation to committed harmful generation. We define the \textbf{Safety Commitment Point} (CP) as the first reasoning step after which safety reasoning permanently ceases. Formally, given a trace of $T$ reasoning steps, the CP is the earliest step $t^*$ such that no step $t > t^*$ contains safety-relevant deliberation. Steps before CP are \emph{pre-commitment} (the model is still considering refusal); steps at or after CP are \emph{post-commitment} (the model has irrevocably committed to harmful output).
8	
9	We operationalize this definition on HarmThoughts~\citep{harmthoughts} traces, which provide step-level annotations of safety reasoning. Each step receives a binary label: pre-CP ($y_t = 0$ for $t < t^*$) or post-CP ($y_t = 1$ for $t \geq t^*$). The detection task is binary classification at each step, producing a score $s_t \in [0, 1]$ that estimates the probability that the model has passed its commitment point by step $t$.
10	
11	We study four reasoning models spanning two architectures (Llama and Qwen) and two parameter scales (7--8B and 32B), summarized in \cref{tab:models}.
12	
13	\begin{table}[t]
14	\centering
15	\small
16	\begin{tabular}{lcccccc}
17	\toprule
18	\textbf{Model} & \textbf{Arch.} & \textbf{Params} & \textbf{Layers} & \textbf{Hidden} & \textbf{Traces} & \textbf{Test} \\
19	\midrule
20	R1-8B & Llama & 8B & 32 & 4096 & 209 & 43 \\
21	OT-7B & Qwen & 7B & 28 & 3584 & 228 & 47 \\
22	R1-32B & Qwen & 32B & 64 & 5120 & 100 & 20 \\
23	QwQ-32B & Qwen & 32B & 64 & 5120 & 95 & 19 \\
24	\bottomrule
25	\end{tabular}
26	\caption{Models studied. R1-8B and R1-32B are distilled from DeepSeek-R1~\citep{deepseekr1}; QwQ-32B~\citep{qwq} is a native reasoning model; OT-7B~\citep{openthinker} is trained with STILL~\citep{still} on Qwen2.5-7B. Data: HarmThoughts~\citep{harmthoughts} with step-level CP annotations. Split: 60/20/20. Total: 632 traces.}
27	\label{tab:models}
28	\end{table}
29	
30	The two 7--8B models provide larger test sets ($n{=}43$--$47$) than the 32B models ($n{=}19$--$20$), yielding narrower confidence intervals. All four models show significant HS advantage after correcting for layer selection bias (\cref{sec:layer-results}).
31	
32	\subsection{Probe Architecture}
33	\label{sec:probe-architecture}
34	
35	\paragraph{Hidden-state (HS) probes.} At each reasoning step $t$, we extract the last-token hidden state $\mathbf{h}_t^{(\ell)} \in \mathbb{R}^d$ from a selected layer $\ell$ of the target model. We train an L2-regularized logistic regression classifier with balanced class weights on the binary pre-CP vs.\ post-CP labels. The probe produces a score $s_t = \sigma(\mathbf{w}^\top \mathbf{h}_t^{(\ell)} + b)$, where $\sigma$ is the logistic function. Layer selection is the subject of \cref{sec:layer-sensitivity}.
36	
37	\paragraph{Text probes.} We encode each step's text using all-MiniLM-L6-v2, producing a 384-dimensional sentence embedding $\mathbf{e}_t \in \mathbb{R}^{384}$. The same logistic regression procedure is applied to these embeddings. Text probes represent detection performance from surface-level linguistic signals alone, serving as a modality comparison baseline for HS probes.
38	
39	\paragraph{Temporal windowing.} For window size $W$, we concatenate features from steps $[t{-}W{+}1, \ldots, t]$ into a single input vector. We evaluate $W \in \{1, 3, 5, 10, 15, 20, 25\}$ and select the operating-point $W$ per-model on the validation set. This tests whether temporal context improves detection over single-step classification.
40	
41	\paragraph{GRU sequence models.} We train single-layer GRU classifiers that process the full step sequence to produce per-step predictions. We evaluate two variants: a single-layer variant (using hidden states from the best-performing layer) and a multi-layer variant (concatenating representations from 7 layers spanning the model depth). Architectural details are in \cref{app:gru_details}.
42	
43	\paragraph{Training procedure.} All probes are trained with Adam (learning rate $1 \times 10^{-3}$, $\beta_1{=}0.9$, $\beta_2{=}0.999$), batch size 16, maximum 50 epochs with early stopping (patience 10 on validation balanced accuracy). Inputs are z-score normalized per dimension using training set statistics.
44	
45	\subsection{Layer Selection Sensitivity Analysis}
46	\label{sec:layer-sensitivity}
47	
48	Hidden-state probing requires selecting which transformer layer to extract representations from. This choice constitutes a researcher degree of freedom that, as we demonstrate, can entirely determine whether hidden-state probes appear to outperform text-based alternatives. We conduct a systematic sensitivity analysis to expose this bias and recommend principled selection criteria.
49	
50	\paragraph{The composite metric bias.} A natural approach is to select the layer that maximizes some composite performance metric on the validation set. The default composite metric used in our initial experiments, the product of balanced accuracy and crossing rate (the fraction of traces where the probe score crosses the detection threshold at least once), is a common choice for threshold-based detectors. We show that this specific composite systematically biases toward shallow layers through a mechanism unrelated to discriminative power.
51	
52	\paragraph{Mechanistic explanation.} Shallow transformer layers produce more volatile representations across reasoning steps. This volatility causes probe scores derived from shallow layers to cross any fixed threshold more frequently, inflating the crossing rate component independently of whether the probe has learned genuinely informative features. The product metric therefore favors layers that are ``trigger-happy'' (high crossing rate due to representational instability) rather than layers whose representations encode the semantic distinction between pre-CP and post-CP states. The effect is strongest in deeper models: in 64-layer models (R1-32B, QwQ-32B), the biased metric selects layers at 3--16\% depth, while principled metrics converge on layers at 94--98\% depth.
53	
54	\paragraph{Five-metric ablation.} To quantify this bias, we evaluate layer selection under five metrics across all four models:
55	
56	\begin{enumerate}
57	\item \textbf{bal\_acc $\times$ crossing\_rate} (biased composite): Selects layer 2 for QwQ-32B (3\% depth) and layer 10 for R1-32B (16\% depth).
58	\item \textbf{Pure balanced accuracy}: Selects deep layers consistently: layer 14 for R1-8B (44\%), layer 16 for OT-7B (57\%), layer 60 for QwQ-32B (94\%), layer 63 for R1-32B (98\%).
59	\item \textbf{Precision}: Converges on deep layers for all four models.
60	\item \textbf{Inverse pre-CP false positive rate (FPR)}: Converges on deep layers for all four models.
61	\item \textbf{Composite (bal\_acc + precision $-$ FPR)}: Converges on deep layers for all four models.
62	\end{enumerate}
63	
64	Four of five metrics independently converge on deep layers. Only the crossing-rate component of metric (1) drives shallow-layer selection. The full metric $\times$ model ablation is presented in \cref{tab:layer_selection}.
65	
66	\paragraph{Downstream impact.} The practical consequence of biased layer selection is severe. For the 32B models, selecting shallow layers entirely masks the hidden-state probe advantage over text probes: probe performance at layers 2--10 is statistically indistinguishable from text probes, while the same probes at layers 60--63 show clear separation. This demonstrates that layer selection is not a minor implementation detail but a methodological choice that can flip a paper's central conclusion.
67	
68	\paragraph{Why deep layers are correct.} Our claim that deep layers provide the appropriate selection does not rest on the circular argument that ``HS probes outperform text probes at deep layers.'' Three independent lines of evidence support this conclusion. First, the mechanistic analysis above identifies a specific, quantifiable bias in the crossing-rate metric that artificially inflates shallow-layer scores. Second, four of five selection metrics, each capturing a different aspect of probe quality, independently converge on deep layers. Third, the probing literature consistently finds that task-relevant semantic representations form in mid-to-deep transformer layers~\citep{belinkov2022probing, tenney2019bert}. The convergence of mechanistic reasoning, empirical metric agreement, and established probing theory provides a non-circular justification for deep-layer selection.
69	
70	\subsection{Baseline Methods}
71	\label{sec:baselines}
72	
73	We evaluate six alternative detection approaches to contextualize probe performance and test whether simpler or unsupervised methods suffice.
74	
75	\paragraph{BOCPD.} Bayesian Online Change-Point Detection~\citep{adams2007bayesian} is applied to probe score sequences, testing whether the commitment point produces an abrupt distributional shift detectable without supervised labels. We sweep hazard rate and observation model parameters on the validation set.
76	
77	\paragraph{CUSUM.} Cumulative sum control charts accumulate evidence for a mean shift in the probe score sequence. We sweep the reference value $\delta$ and decision threshold $h$ to find optimal configurations per model (\cref{app:bocpd_config}).
78	
79	\paragraph{Mahalanobis distance.} Following TrajGuard~\citep{trajguard}, we compute the Mahalanobis distance of each step's hidden state from the pre-CP distribution centroid, testing whether geometric separation in activation space suffices for detection without training a discriminative probe.
80	
81	\paragraph{Representation Engineering (RepE).} Following \citet{zou2023representation}, we compute the mean-difference direction between labeled pre-CP and post-CP hidden states and project each step's representation onto this direction as a probe score. This direction-based supervised method tests whether a single linear direction, computed from class means rather than discriminative training, captures the commitment distinction.
82	
83	\paragraph{MLP probe.} A two-layer nonlinear probe ($d \rightarrow 128 \rightarrow 1$, ReLU activation) tests whether the linear probe's capacity is a bottleneck, or whether the pre-CP/post-CP distinction is linearly separable.
84	
85	\paragraph{CCS-adapted.} We adapt Contrast-Consistent Search~\citep{burns2023discovering} for commitment detection by constructing contrastive pairs from pre-CP and post-CP steps within each trace. This tests whether weakly supervised representation discovery can match fully supervised probes. CCS still requires CP labels for pair construction, making it semi-supervised rather than fully unsupervised.
86	
87	\paragraph{Cross-model transfer.} We project hidden states into a shared subspace via PCA and evaluate whether a probe trained on one model transfers to another, testing the universality of commitment representations.
88	
89	\paragraph{Position-only baseline.} A classifier that predicts post-CP based solely on the step index $t / T$ (normalized position within the trace). This critical control tests whether probes capture genuine semantic signal beyond the trivial positional correlation that later steps are more likely to be post-CP.
90	
91	\subsection{Evaluation Protocol}
92	\label{sec:evaluation}
93	
94	\paragraph{Metrics.} We report six complementary metrics. \textbf{Balanced accuracy}: mean of sensitivity and specificity at the optimal threshold. \textbf{Precision}: fraction of threshold-exceeding steps that are truly post-CP. \textbf{Pre-CP FPR}: reported at both step-level (pooling all pre-CP steps across traces) and trace-level (mean per-trace FPR, treating each trace as an independent observation). \textbf{Coverage}: fraction of jailbreak traces where at least one step exceeds the detection threshold. \textbf{Lead time}: number of steps between first detection and the true CP ($t^* - t_{\text{detect}}$); positive values indicate early warning.
95	
96	\paragraph{Statistical testing.} All modality comparisons (HS vs.\ text probes) use a two-sided null-centered bootstrap test (1000 resamples) on trace-level metric values. For each resample, we draw paired differences with replacement, center the distribution at the null hypothesis of zero difference, and compute the two-tailed exceedance probability. We conduct 12 hypothesis tests (3 metrics $\times$ 4 models) and apply the Holm-Bonferroni step-down correction at $\alpha{=}0.05$. This procedure controls the family-wise error rate while maintaining power across the test battery.
97	
98	\paragraph{Control task.} Following \citet{hewitt2019control}, we train probes on randomly permuted labels and compute selectivity as real accuracy minus random-label accuracy. Selectivity exceeding 5 percentage points indicates that the probe has learned genuine structure beyond positional artifacts. This complements the position-only baseline by testing whether the probe's internal representations encode semantic content.
99	
100	\paragraph{Detection criterion.} We use $K{=}5$ (five consecutive threshold crossings required for detection) throughout all experiments. This criterion does not affect step-level metrics (balanced accuracy, precision, FPR), which are computed over all steps independently. It governs coverage and lead time: a trace is ``detected'' only when five consecutive steps exceed the threshold, reducing spurious detections from isolated high-scoring steps.
101	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "416f7bea-56a8-4f16-a95f-f0c7a05e698d",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "5949a2f9-0be0-4116-ab84-0bcbc57969c1",
  "sourceToolAssistantUUID": "416f7bea-56a8-4f16-a95f-f0c7a05e698d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-17T17:03:24.083Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DrJGQqBMUBXYJUry1BtDa9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5949a2f9-0be0-4116-ab84-0bcbc57969c1",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "73d9decd-f595-42c0-8179-b288585d3764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-17T17:03:24.092Z_

<details><summary>↩ Tool result · reported error · `toolu_01DrJGQqBMUBXYJUry1BtDa9`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "73d9decd-f595-42c0-8179-b288585d3764",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "f507bd9d-b5b2-476e-885a-707754de85d1",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety.",
  "sourceToolAssistantUUID": "73d9decd-f595-42c0-8179-b288585d3764",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-17T17:03:24.162Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Vo6NDD8PthvLoGFiaAYB2M`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f507bd9d-b5b2-476e-885a-707754de85d1",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W6s6ZBGAkmPrJbmbwT",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a97f6b11-0e78-42ff-a8e4-35af86de288c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JJWH5koWWixVG9XaTn2KBb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 27478,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 27478,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-17T17:03:24.168Z_

<details><summary>↩ Tool result · `toolu_01Vo6NDD8PthvLoGFiaAYB2M`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Layer selection as researcher degree of freedom.}
4	Layer selection is an underexamined methodological choice in the probing literature that can silently determine a study's conclusions. Our five-metric ablation (\cref{sec:layer-results}) demonstrates that a single metric component, the crossing rate, reverses the central finding of an HS vs.\ text comparison: at biased layers, only 5 of 12 tests survive Holm-Bonferroni correction, producing an apparent scale-dependent modality effect; at corrected layers, all 12 tests pass. The mechanism is general: crossing rate rewards representational volatility at shallow layers independently of discriminative power, and any composite metric that incorporates threshold-crossing frequency risks the same systematic bias toward early layers. This bias is not specific to safety probing. Any threshold-based detection study that uses crossing rate as a layer selection criterion, whether for sentiment, factuality, or toxicity, could produce analogous reversals. We recommend that probing studies report results under at least two independent layer selection criteria, and that five-metric ablations (or at minimum, results at multiple candidate layers spanning shallow, middle, and deep positions) become standard practice. The cost is modest: evaluating five metrics across all layers adds minutes to an experiment that takes hours. The alternative is that conclusions about representational structure reflect layer selection methodology rather than the phenomenon under study.
5	
6	\paragraph{Temporal context and modality choice.}
7	Information-theoretic reasoning suggests that hidden states (4096 to 5120 dimensions of internal computation) should dominate text features (384-dimensional sentence embeddings) purely by signal capacity. Both temporal context and modality choice significantly improve detection, but their relative magnitudes differ by scale. At 7--8B, the modality advantage (precision +22pp) exceeds the temporal improvement (+13pp), establishing that modality choice matters more at this scale. At 32B, the relative magnitudes depend on model and window size (\cref{sec:temporal}). Text probes benefit more from temporal context than HS probes because they start from a weaker single-step baseline and extract proportionally more from observing multi-step progressions. Safety commitment is a gradual process: the model progressively consolidates its intent over multiple reasoning steps rather than switching abruptly at a single token. Both modalities benefit from temporal context; for text probes, the improvement is universal across all four models. The practical implication is that temporal windowing ($W{=}3$ to $15$) remains the most robust single default for safety monitoring, as it provides guaranteed improvement regardless of modality, while the modality choice requires principled layer selection to realize its full potential.
8	
9	\paragraph{Cross-model divergence within identical architecture.}
10	R1-32B and QwQ-32B share the same base architecture (Qwen-32B, 64 layers) but present opposite detection profiles (\cref{tab:32b_divergence}). R1-32B provides excellent lead time (+11.7 to +13.3 steps before commitment) with narrow coverage (25\% at the only significant window, $W{=}1$) and a strong margin over the position baseline (+14.2pp). QwQ-32B provides robust statistical significance (all 15 window sizes pass Holm-Bonferroni, 3/3 metrics each) with 74\% coverage, but lead time is negative ($-$1.2 to +1.9 steps) and the position baseline is competitive ($-$0.6pp difference). This divergence arises despite identical architecture and parameter count, making training method (R1 distillation vs.\ native reasoning) the likely differentiator. The practical implication is that per-model validation is essential: no single detection configuration generalizes even within the same architecture at the same scale. A monitoring system validated on QwQ-32B would fail to provide early warning on R1-32B, and one tuned for R1-32B's narrow operating window would achieve only 25\% coverage in deployment. An open question remains: whether the R1-32B dimensionality constraint ($51200 \times W$ features for $n{=}20$ traces) would resolve with more training data, or whether deep-layer signal at large $W$ is fundamentally sparse for distilled models.
11	
12	\paragraph{Design implications for safety monitoring.}
13	Based on these findings, we recommend temporal windowing ($W{=}3$ to $15$) combined with principled layer selection (pure balanced accuracy or precision as the selection metric, never crossing rate) as defaults for deployment. At 7-8B, HS probes Pareto-dominate text probes: +22.4pp precision on R1-8B and +21.9pp on OT-7B, with lower FPR and comparable timing. At 32B, HS probes are statistically superior across all metrics, but practical trade-offs require model-specific decisions between lead time, coverage, and significance breadth. All current methods produce 39-62\% FPR on safe traces at standard operating thresholds, which means they characterize the safety commitment phenomenon rather than constitute production-ready detectors. The 85.5\% oracle gap (the fraction of theoretical early detection potential not captured by the best learned method) indicates that passive monitoring captures only a small portion of available signal (\cref{sec:oracle}). The gap between learned probes (+4.5 steps lead) and the oracle (+31 steps lead) suggests that hidden states at step $t$ encode the model's current safety state but carry limited predictive power about future trajectory evolution. Future work should explore active intervention through activation patching at candidate commitment points, expansion to multilingual and multi-turn settings, and evaluation at intermediate scales (13B, 70B) to determine whether the R1-32B dimensionality constraint reflects small-sample limitations or a fundamental property of distilled reasoning models.
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a97f6b11-0e78-42ff-a8e4-35af86de288c",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "8e9dac36-9b44-4321-a849-11288cbc50b9",
  "sourceToolAssistantUUID": "a97f6b11-0e78-42ff-a8e4-35af86de288c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-17T17:03:25.591Z_

Now let me check if there's an experiments.tex file instead of results.tex:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e9dac36-9b44-4321-a849-11288cbc50b9",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W747LQH77GTzMfLNjJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e340f2e-6eff-4914-9541-380bdd2db7d7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011UeRh38aq9LbwyyYj6VVmP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8610,
      "cache_read_input_tokens": 27478,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8610,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-17T17:03:26.356Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0177zBAVF9RmYqJLuHDFvU4Q`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e340f2e-6eff-4914-9541-380bdd2db7d7",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W747LQH77GTzMfLNjJ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8713de25-df2e-46f3-8454-b264954d9083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011UeRh38aq9LbwyyYj6VVmP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8610,
      "cache_read_input_tokens": 27478,
      "output_tokens": 107,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8610
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 107,
          "cache_read_input_tokens": 27478,
          "cache_creation_input_tokens": 8610,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8610,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-17T17:03:26.373Z_

<details><summary>↩ Tool result · `toolu_0177zBAVF9RmYqJLuHDFvU4Q`</summary>

```text
docs/paper/sections/abstract.tex
docs/paper/sections/conclusion.tex
docs/paper/sections/appendix.tex
docs/paper/sections/method.tex
docs/paper/sections/introduction.tex
docs/paper/sections/related_work.tex
docs/paper/sections/experiments.tex
docs/paper/sections/discussion.tex
docs/paper/sections/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8713de25-df2e-46f3-8454-b264954d9083",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "02068766-089c-4321-8712-795fbcdf72c9",
  "sourceToolAssistantUUID": "8713de25-df2e-46f3-8454-b264954d9083",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-17T17:03:27.393Z_

Perfect, now let me read the experiments.tex file:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02068766-089c-4321-8712-795fbcdf72c9",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W7DSAtTjax5PTkCfqM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5d94dcbc-b9be-4d56-9d0e-74d534a617c5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FHsrW1nUwimEKNRXqbdYk7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 36088,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 212,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-17T17:03:27.650Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FbewBhysYvoXygrJvtqNGy`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d94dcbc-b9be-4d56-9d0e-74d534a617c5",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W7DSAtTjax5PTkCfqM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "08d42e8b-b9b4-4c2e-81dc-199cf3d0fc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FHsrW1nUwimEKNRXqbdYk7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 36088,
      "output_tokens": 104,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 212
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 104,
          "cache_read_input_tokens": 36088,
          "cache_creation_input_tokens": 212,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 212,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-17T17:03:27.666Z_

<details><summary>↩ Tool result · `toolu_01FbewBhysYvoXygrJvtqNGy`</summary>

```text
1	\section{Experiments}\label{sec:experiments}
2	
3	We evaluate temporal probes across four reasoning models (\cref{tab:models}), comparing hidden-state (HS) and text modalities under different layer selection criteria. Our experiments address three questions: (1)~Does the layer selection metric determine whether HS probes appear effective? (2)~Do HS probes outperform text probes at correctly selected layers? (3)~Which alternative detection methods fail, and why?
4	
5	\subsection{Experimental Setup}\label{sec:setup}
6	
7	\paragraph{Models and data.} We study four models spanning two architectures and two parameter scales: R1-8B (Llama-8B, R1-distilled, $n{=}43$ test traces), OT-7B (Qwen-7B, STILL-trained, $n{=}47$), QwQ-32B (Qwen-32B, native reasoning, $n{=}19$--$20$), and R1-32B (Qwen-32B, R1-distilled, $n{=}20$). All traces come from HarmThoughts with step-level commitment point (CP) annotations. We use a 60/20/20 train/validation/test split across all models (\cref{tab:models}).
8	
9	\paragraph{Training and evaluation.} All probes use L2-regularized logistic regression with balanced class weights. For each model, we select the temporal window $W$ on the validation set from $W \in \{1, 3, 5, 10, 15, 20, 25\}$. HS probes extract last-token hidden states from a selected transformer layer; text probes encode each reasoning step with all-MiniLM-L6-v2 (384 dimensions). Detection requires $K{=}5$ consecutive threshold crossings. Modality comparisons use a two-sided null-centered bootstrap test (1000 resamples) with Holm-Bonferroni step-down correction across 12 tests (3 metrics $\times$ 4 models, $\alpha{=}0.05$).
10	
11	\paragraph{Layer selection.} We evaluate five layer selection metrics per model (\cref{sec:layer-sensitivity}). The biased composite metric (balanced accuracy $\times$ crossing rate) systematically selects shallow layers for 32B models because representational volatility at early layers inflates the crossing rate component. Four unbiased metrics (pure balanced accuracy, precision, inverse FPR, and an additive composite) converge on deep layers. Results throughout this section use the corrected deep layers, with explicit comparison to biased-layer outcomes in \cref{sec:layer-results}.
12	
13	\subsection{Layer Selection Results}\label{sec:layer-results}
14	
15	\cref{tab:layer_selection} presents the layer selected by the biased composite metric and the consensus of four unbiased metrics across all four models. For R1-8B, all five metrics agree on layer~14 (44\% depth), with no discrepancy. For the remaining three models, the biased metric selects shallow layers: L0 (0\%) for OT-7B, L2 (3\%) for QwQ-32B, and L10 (16\%) for R1-32B. All four unbiased metrics converge on deep layers: L16 (57\%) for OT-7B, L60 (94\%) for QwQ-32B, and L63 (98\%) for R1-32B. The bias is most extreme for the 64-layer 32B models, where the composite metric selects layers in the bottom 16\% of the network while all other metrics select layers above 94\%.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\begin{tabular}{lccc}
21	\toprule
22	\textbf{Model} & \textbf{Biased}$^a$ & \textbf{Corrected}$^b$ & $p$ \textbf{(corr.)} \\
23	\midrule
24	R1-8B & L14 (44\%) & L14 (44\%) & ${<}0.001$ \\
25	OT-7B & L0 (0\%)$^c$ & L16 (57\%) & ${<}0.001$ \\
26	QwQ-32B & L2 (3\%) & L60 (94\%) & ${<}0.005$ \\
27	R1-32B & L10 (16\%) & L63 (98\%) & ${<}0.001$ \\
28	\bottomrule
29	\end{tabular}
30	\caption{Layer selection sensitivity. $^a$\,Selected by bal\_acc $\times$ crossing\_rate. $^b$\,Consensus of four unbiased metrics (pure bal\_acc, precision, inverse FPR, additive composite). $^c$\,OT-7B has only 28 layers; bias is less extreme than for 64-layer models. The rightmost column reports HS vs.\ text precision $p$-values at the corrected layer (two-sided null-centered bootstrap, 1000 resamples). At the \emph{biased} layers for 32B models, corresponding $p$-values were 0.064 (R1-32B) and 0.35--0.83 (QwQ-32B), both non-significant.}
31	\label{tab:layer_selection}
32	\end{table}
33	
34	The downstream impact on modality comparison is severe for the 32B models. At biased layers, two-sided bootstrap $p$-values for HS precision advantage are 0.064 for R1-32B (not significant) and 0.35--0.83 for QwQ-32B (not significant). At the corrected deep layers, all $p$-values drop below 0.005. The R1-32B case illustrates the magnitude of this effect: the biased metric selects L10 (16\% depth, precision $p{=}0.064$), while pure balanced accuracy selects L63 (98\% depth, $p{<}0.001$). For QwQ-32B, the shift is from L2 ($p{=}0.35$--$0.83$) to L60 ($p{<}0.005$ across all 15 window sizes tested). OT-7B represents an intermediate case: the biased metric selects L0 (0\%), but OT-7B has only 28 layers, so the practical impact is smaller than for 64-layer models. The corrected layer (L16, 57\% depth) still produces stronger HS-text separation ($p{<}0.001$ on all three metrics).
35	
36	This sensitivity analysis reveals that a single metric component (crossing rate) can reverse a study's central conclusion. Had we reported only biased-layer results, we would have concluded that the HS advantage is scale-dependent: significant at 7--8B, absent at 32B. The corrected analysis shows HS advantage across all four models, with the apparent scale-dependence being a methodological artifact of biased layer selection.
37	
38	\subsection{HS vs.\ Text Comparison}\label{sec:hs-text}
39	
40	\cref{tab:hs_vs_text} presents the main HS vs.\ text comparison at corrected layers. All 12 hypothesis tests (3 metrics $\times$ 4 models) pass Holm-Bonferroni step-down correction at $\alpha{=}0.05$. At the previously used biased layers, only 5 of 12 tests passed (all from the two 7--8B models that were unaffected by the metric bias). The corrected analysis recovers all 7 previously failing tests across the full battery.
41	
42	\begin{table}[t]
43	\centering
44	\small
45	\begin{tabular}{llcrrrr}
46	\toprule
47	\textbf{Model} & \textbf{Layer} & $W$ & $\Delta$\textbf{BA} & $\Delta$\textbf{Prec} & $\Delta$\textbf{FPR} & \textbf{HB} \\
48	\midrule
49	R1-8B & L14 & 15 & +8.2 & +22.4 & $-$7.4 & 3/3 \\
50	OT-7B & L16 & 3 & +10.7 & +21.9 & $-$17.1 & 3/3 \\
51	QwQ & L60 & 3 & +15.4 & \textbf{+23.6} & $-$9.8 & 3/3 \\
52	R1-32B & L63 & 1 & \textbf{+18.7} & +15.4 & \textbf{$-$14.6} & 3/3 \\
53	\bottomrule
54	\end{tabular}
55	\caption{HS vs.\ text probe comparison at corrected layers. $\Delta$BA, $\Delta$Prec, and $\Delta$FPR report the HS$-$text difference in percentage points for balanced accuracy, precision, and pre-CP false positive rate. HB: tests passing Holm-Bonferroni step-down ($\alpha{=}0.05$, 12 tests total). All comparisons use a two-sided null-centered bootstrap (1000 resamples). $W$: validation-selected temporal window per model.}
56	\label{tab:hs_vs_text}
57	\end{table}
58	
59	\paragraph{7--8B models.} R1-8B ($n{=}43$, L14, $W{=}15$) shows HS advantages of +8.2pp balanced accuracy ($p{=}0.005$), +22.4pp precision ($p{<}0.001$), and $-$7.4pp FPR ($p{=}0.044$). All three survive Holm-Bonferroni correction. OT-7B ($n{=}47$, L16, matched $W{=}3$) shows +10.7pp balanced accuracy ($p{<}0.001$), +21.9pp precision ($p{<}0.001$), and $-$17.1pp FPR ($p{<}0.001$), with all three tests surviving correction. The precision advantage is consistent across these architecturally distinct models: +22.4pp on the Llama-based R1-8B and +21.9pp on the Qwen-based OT-7B, despite different training methods (R1 distillation vs.\ STILL).
60	
61	\paragraph{32B models.} QwQ-32B ($n{=}19$--$20$, L60, $W{=}3$) shows +15.4pp balanced accuracy ($p{<}0.001$), +23.6pp precision ($p{<}0.001$), and $-$9.8pp FPR ($p{=}0.004$), all surviving correction. R1-32B ($n{=}20$, L63, $W{=}1$) shows +18.7pp balanced accuracy ($p{<}0.001$), +15.4pp precision ($p{<}0.001$), and $-$14.6pp FPR ($p{=}0.007$), all surviving correction. The precision advantage ranges from +15.4 to +23.6pp across all four models.
62	
63	\paragraph{Control task selectivity.} Following \citet{hewitt2019control}, selectivity scores confirm genuine safety signal beyond positional artifacts: R1-8B 12.5pp, OT-7B 18.3pp, QwQ-32B 15.3pp, R1-32B 7.5pp. All four models exceed the 5pp threshold.
64	
65	\paragraph{Caveats.} Three qualifications apply. First, the validation-selected $W$ differs per model ($W{=}15$ for R1-8B, $W{=}3$ for OT-7B and QwQ-32B, $W{=}1$ for R1-32B). The tests measure whether HS outperforms text at each model's best operating point, not at a uniform window. Second, R1-32B at $W{=}1$ achieves only 25\% coverage (5 of 20 test traces detected), which limits practical utility despite strong per-detection performance. At $W{\geq}3$, R1-32B significance vanishes due to the dimensionality constraint ($51200 \times W$ features for $n{=}20$ training traces). Third, QwQ-32B HS lead time is negative ($-$1.2 to +1.9 steps) compared to text probes (3.7 to 12.3 steps): HS probes are more accurate but detect later on this model. In safety deployment, earlier detection by several steps may outweigh higher per-step accuracy.
66	
67	\subsection{Temporal Context Effects}\label{sec:temporal}
68	
69	Text probes benefit universally from larger temporal windows across all four models. Balanced accuracy improves by +3 to +12pp and precision by +8 to +23pp from $W{=}1$ to $W{=}25$, with consistent FPR reductions.
70	
71	HS probes show similar benefits on 3 of 4 models. On R1-8B (L14), increasing $W$ from 1 to 25 improves balanced accuracy from 77.8\% to 81.0\% (+3.2pp), precision from 69.3\% to 82.2\% (+12.9pp), and reduces FPR from 9.65\% to 4.8\% ($-$4.9pp). At the validation-selected $W{=}15$, performance reaches 80.2\% balanced accuracy, 77.7\% precision, and 6.4\% FPR, which captures most of the precision gain with higher coverage than $W{=}25$. QwQ-32B and R1-32B follow similar monotonic patterns for precision and FPR across the full $W$ range.
72	
73	\begin{figure}[t]
74	\centering
75	\includegraphics[width=\columnwidth]{figures/fig2_temporal_improvement.pdf}
76	\caption{Effect of temporal window size on R1-8B HS probe performance (L14). Precision increases monotonically from 69.3\% ($W{=}1$) to 82.2\% ($W{=}25$); FPR decreases from 9.65\% to 4.8\%.}
77	\label{fig:window_ablation}
78	\end{figure}
79	
80	OT-7B is the exception. HS balanced accuracy peaks at $W{=}3$ (68.8\%) and declines to 65.9\% at $W{=}25$ ($-$2.9pp). Precision and FPR continue to improve: precision rises from 42.8\% ($W{=}1$) to 49.4\% ($W{=}25$), and FPR drops from 12.0\% to 7.5\%. The saturation is specific to balanced accuracy; larger windows trade balanced accuracy for better precision and lower FPR. This pattern holds on both L0 and L16, which confirms it as a genuine OT-7B characteristic rather than a layer-specific artifact. The validation selection of $W{=}3$ reflects this trade-off: balanced accuracy is maximized without sacrificing the precision gains available at moderate windows.
81	
82	The consistent finding across all four models is that precision improvement (+1.7 to +12.9pp from $W{=}1$ to best) and FPR reduction ($-$4.0 to $-$5.9pp) are positive for both modalities (\cref{fig:window_ablation}). Both temporal context and signal modality significantly improve detection. At 7--8B scale, the modality advantage (precision +22pp) exceeds the temporal improvement (+13pp), while at 32B the relative magnitudes depend on model and window size. Larger windows make probes more conservative, reducing coverage but improving confidence on detected traces. Deployment systems would tune $K$ alongside $W$ to balance coverage against precision.
83	
84	\subsection{32B Model-Specific Analysis}\label{sec:32b-analysis}
85	
86	The two 32B models present contrasting detection profiles despite sharing the Qwen-32B architecture (\cref{tab:32b_divergence}). Per-model analysis is required; a unified scale-level narrative would obscure important differences.
87	
88	\begin{table}[t]
89	\centering
90	\small
91	\begin{tabular}{lcc}
92	\toprule
93	\textbf{Dimension} & \textbf{R1-32B (L63)} & \textbf{QwQ (L60)} \\
94	\midrule
95	Holm-Bonf.\ sig.\ & $W{=}1$ only (3/3) & All 15 $W$ (3/3) \\
96	Lead time (steps) & +11.7 to +13.3 & $-$1.2 to +1.9 \\
97	HS vs.\ Position & +14.2pp & $-$0.6pp \\
98	Coverage ($W{=}1$) & 25\% & 74\% \\
99	\bottomrule
100	\end{tabular}
101	\caption{32B cross-model divergence. R1-32B provides excellent early warning with narrow coverage; QwQ-32B provides robust significance with poor lead time.}
102	\label{tab:32b_divergence}
103	\end{table}
104	
105	\paragraph{R1-32B (L63, $W{=}1$).} R1-32B achieves excellent lead time (+11.7 to +13.3 steps before commitment), and the HS probe strongly outperforms the position-only baseline (+14.2pp balanced accuracy). These properties make R1-32B the strongest candidate for early warning among the four models. The limitation is statistical narrowness: only $W{=}1$ passes Holm-Bonferroni (3/3 metrics), with $W{\geq}3$ non-significant due to dimensionality ($51200 \times W$ features for $n{=}20$ traces). At $W{=}1$, coverage is 25\% (5 of 20 traces detected). The evidence supports HS superiority on R1-32B but under restrictive operating conditions.
106	
107	\paragraph{QwQ-32B (L60, $W{=}3$).} QwQ-32B shows the most robust statistical significance of any model: HS outperforms text at all 15 window sizes tested ($p{<}0.005$), with 74\% coverage at $W{=}1$. The limitation is detection timing: HS lead time is negative ($-$1.2 to +1.9 steps), compared to text probes (3.7 to 12.3 steps). The position-only baseline achieves comparable balanced accuracy (0.746 vs.\ HS 0.740). HS probes are more precise but detect later, and they offer minimal advantage over simple positional features for this model.
108	
109	The complementary profiles suggest that the practical value of HS monitoring depends on model-specific detection requirements. Early warning applications favor R1-32B's high lead time despite narrow coverage. Broad reliable detection applications favor QwQ-32B's robust significance despite poor timing. These divergent patterns within the same architecture underscore that per-model validation is essential.
110	
111	\subsection{Negative Results}\label{sec:negative}
112	
113	\cref{tab:negative} summarizes seven alternative detection approaches that fail to match supervised temporal probing. The failures span change-point detection, geometric methods, direction-based probing, nonlinear models, semi-supervised learning, and cross-model transfer.
114	
115	\begin{table}[t]
116	\centering
117	\small
118	\begin{tabular}{p{1.5cm}p{2.9cm}p{2.3cm}}
119	\toprule
120	\textbf{Method} & \textbf{Result} & \textbf{Failure Mode} \\
121	\midrule
122	BOCPD & R1-8B 93\% det., lead +3.5 $<$ thresh.\ +4.9; others 0\% & Commitment gradual \\
123	CUSUM & Worse than threshold, all models & Same as BOCPD \\
124	Mahalanobis & $\Delta d \approx 0$ (R1-8B +0.07, OT-7B +0.03) & Signal in minor PCA dirs. \\
125	RepE & R1-8B 74.9\%, QwQ 75.6\%, R1-32B 55.9\%$^a$ & Model-dependent \\
126	MLP & 3/4 worse than LR & Overfitting ($n$ small) \\
127	CCS$^b$ & R1-8B 77.7\%; R1-32B FPR\,=\,0.41 & No gain over supervised \\
128	Transfer & Best PCA 59.5\%; direct 67.3\%$^c$ & Model-specific repr. \\
129	\bottomrule
130	\end{tabular}
131	\caption{Negative results. $^a$\,RepE at corrected layers: QwQ L60 achieves 0.756 bal\_acc (vs.\ LR 0.740) but R1-32B L63 nearly fails (0.559 vs.\ LR 0.826). $^b$\,CCS is semi-supervised (requires CP labels for pair construction), not truly unsupervised. $^c$\,QwQ$\rightarrow$R1-32B direct transfer achieves 67.3\% accuracy but 1\% crossing rate (zero practical utility).}
132	\label{tab:negative}
133	\end{table}
134	
135	BOCPD achieves 93\% detection rate on R1-8B but with worse lead time (+3.5 steps) than simple thresholding (+4.9 steps). On OT-7B and both 32B models, BOCPD achieves 0\% detection across all hazard rate configurations. CUSUM underperforms thresholding on all four models. Both methods assume abrupt distributional shifts, but safety commitment is gradual: representations transition smoothly toward post-CP states rather than producing a sharp regime change.
136	
137	Mahalanobis distance produces near-zero separation between safe and jailbreak trajectories across all four models (R1-8B $\Delta d{=}+0.07$, OT-7B $+0.03$). The discriminative signal resides in minor PCA components rather than the principal variance directions that Mahalanobis distance captures.
138	
139	RepE direction probing~\citep{zou2023representation} shows model-dependent performance at corrected layers. QwQ-32B achieves near-supervised balanced accuracy at L60 (0.756 vs.\ LR 0.740 at $W{=}1$), but with lower precision (0.512) and higher FPR (0.309). R1-32B nearly fails at L63 (0.559 vs.\ LR 0.826), with FPR of 0.499. On R1-8B (L14, 0.749 vs.\ LR 0.817) and OT-7B (L16, 0.642), RepE also underperforms supervised probes. The divergence between QwQ and R1-32B demonstrates that direction-based methods are insufficient for models where safety commitment requires discriminative training to decode. Layer selection sensitivity affects RepE differently from supervised probes: R1-32B RepE performs better at shallow layers while supervised LR performs better at deep layers, which further underscores that layer selection interacts with method choice. MLP probes underperform LR on 3 of 4 models, which confirms that the pre-CP/post-CP distinction is linearly separable and that additional model capacity leads to overfitting on small training sets. CCS~\citep{burns2023discovering} achieves 77.7\% balanced accuracy on R1-8B (between supervised LR and RepE) but FPR reaches 0.41 on R1-32B. CCS requires CP labels for contrastive pair construction, which makes it semi-supervised rather than truly unsupervised, and it provides no advantage over fully supervised probes.
140	
141	Cross-model transfer fails across all 17 configurations tested (5 directional model pairs $\times$ 3 PCA dimensionalities, plus 2 direct transfers). The best PCA transfer achieves 59.5\% balanced accuracy (R1-8B$\rightarrow$QwQ, 2048 components). One direct transfer direction (QwQ$\rightarrow$R1-32B) reaches 67.3\% accuracy, which exceeds the within-model baseline. However, its crossing rate is 1\%, which means the probe almost never triggers detection in practice. PCA projection into shared dimensionality spaces does not recover transferable structure, and the single above-baseline direction has zero practical utility due to negligible coverage.
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08d42e8b-b9b4-4c2e-81dc-199cf3d0fc6b",
  "isSidechain": true,
  "promptId": "a2ec04bf-6cb1-499c-bb7c-be4f917fb3d8",
  "agentId": "a6173ad97cfaaa5eb",
  "type": "user",
  "uuid": "6b0809f2-4998-4eee-8ba9-bbdb5a8e8362",
  "sourceToolAssistantUUID": "08d42e8b-b9b4-4c2e-81dc-199cf3d0fc6b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-17T17:04:04.299Z_

Perfect. Now I have all the material needed. Let me compile a comprehensive summary for you.

---

## Summary of Key Content for Conclusion Section

### 1. **ABSTRACT** 
- **Section Label:** (Unnamed; introduction/framing)
- **Main Claims:** 
  - LLMs with CoT can self-jailbreak via transitions from safe deliberation to harmful generation
  - First cross-model evaluation of temporal probing for safety commitment detection
  - Temporal context dominates modality choice: expanding observation window improves precision by up to 12.9pp
  - HS probes significantly outperform text probes at 7-8B scale (R1-8B +22.4pp, OT-7B +21.2pp precision)
  - No significant difference at 32B emerges on either model (initially claimed, later disputed)
  - Geometric distance methods, change-point detectors, and cross-model transfer all fail
- **Key Terminology:** Hidden-state (HS) probes, text probes, temporal probing, safety commitment, chain-of-thought (CoT), modality comparison, Holm-Bonferroni correction
- **Specific Numbers:** 
  - Precision improvement: +12.9pp (window expansion)
  - R1-8B precision: +22.4pp (p<0.001, 5/12 tests surviving correction)
  - OT-7B precision: +21.2pp (p<0.001)
  - Control task selectivity: 7.5–18.3pp above chance
  - Four models: Llama (R1-distilled) and Qwen (STILL, native reasoning), two scales (7-8B, 32B)

---

### 2. **INTRODUCTION**
- **Section Label:** `\section{Introduction}\label{sec:introduction}`
- **Main Claims:**
  - Self-jailbreaking is a failure mode unique to reasoning models where the model's own CoT transitions from safety-aware reasoning to committed harmful generation
  - **Safety Commitment Point (CP)**: defined as the first reasoning step after which safety deliberation permanently ceases
  - Existing detectors (TrajGuard, SafeSwitch for HS; SafeRemind, SafeThink for text) target different threats and were never compared systematically on the same task
  - **Central finding**: Layer selection metric entirely determines whether HS advantage is observed
  - Composite metric (balanced accuracy × crossing rate) systematically selects shallow layers for 32B models, artificially inflating crossing rate
  - At corrected deep layers, all 12 tests pass Holm-Bonferroni correction with HS precision +15.4 to +23.6pp across all four models
  - Layer selection bias, not scale or architecture, is the true moderator of probe performance
- **Key Terminology:** 
  - Safety Commitment Point (CP), balanced accuracy (bal_acc), crossing rate, layer selection sensitivity, hidden-state (HS) probes, text probes, Holm-Bonferroni step-down correction, composite metrics, biased metric
- **Specific Numbers:**
  - Precision improvement range: +15.4 to +23.6pp (HS vs. text at corrected deep layers)
  - Layer selection bias magnitude: biased metric selects layers at 3–16% depth for 32B models; four unbiased metrics converge on 94–98% depth
  - Control selectivity: 7.5–18.3pp above chance (confirms genuine safety structure)
  - Temporal lead time (R1-32B): +13 steps early detection
  - Four models tested with different dimensions: R1-8B (32 layers, 4096 hidden), OT-7B (28 layers, 3584), R1-32B (64 layers, 5120), QwQ-32B (64 layers, 5120)

---

### 3. **METHOD**
- **Section Label:** `\section{Problem Setup and Methods}\label{sec:method}`
- **Main Claims:**
  - Safety Commitment Point formally defined as earliest step t* where no step t > t* contains safety-relevant deliberation
  - Binary classification task: pre-CP (y_t = 0) vs. post-CP (y_t = 1)
  - Four models span two architectures (Llama, Qwen) and two training methods (R1 distillation, STILL)
  - HS probes extract last-token hidden states from a selected layer with L2-regularized logistic regression
  - Text probes use all-MiniLM-L6-v2 (384 dimensions) sentence embeddings
  - Temporal windowing tested at W ∈ {1, 3, 5, 10, 15, 20, 25}
  - Layer selection is a critical researcher degree of freedom that can flip conclusions
  - Five-metric ablation employed to identify bias and establish principled selection criteria
- **Key Terminology:**
  - Safety Commitment Point (CP), pre-CP, post-CP, hidden-state (HS) probes, text probes, all-MiniLM-L6-v2, temporal windowing, balanced accuracy, crossing rate, composite metrics, L2-regularized logistic regression, Holm-Bonferroni correction, layer selection sensitivity, GRU sequence models
- **Specific Numbers:**
  - 632 total traces from HarmThoughts dataset
  - Split: 60/20/20 (train/validation/test)
  - R1-8B: 209 traces, 43 test; OT-7B: 228 traces, 47 test; R1-32B: 100 traces, 20 test; QwQ-32B: 95 traces, 19 test
  - Hidden dimensions: R1-8B 4096, OT-7B 3584, R1-32B/QwQ-32B 5120
  - Text embedding dimensions: 384 (all-MiniLM-L6-v2)
  - Window sizes tested: W ∈ {1, 3, 5, 10, 15, 20, 25}
  - Detection criterion: K=5 (five consecutive threshold crossings required)
  - Adam optimizer: lr=1e-3, β1=0.9, β2=0.999; batch size 16; max 50 epochs with early stopping (patience 10)

---

### 4. **EXPERIMENTS** (results section)
- **Section Label:** `\section{Experiments}\label{sec:experiments}`
- **Main Claims:**
  - Layer selection metric determines whether HS probes appear effective—this is the primary finding, not true modality differences
  - At corrected deep layers, all 12 hypothesis tests (3 metrics × 4 models) pass Holm-Bonferroni correction
  - Biased composite metric (bal_acc × crossing_rate) selects: OT-7B L0 (0%), QwQ-32B L2 (3%), R1-32B L10 (16%)
  - Four unbiased metrics converge on: OT-7B L16 (57%), QwQ-32B L60 (94%), R1-32B L63 (98%)
  - HS precision advantage at corrected layers: +15.4pp to +23.6pp across all models
  - Temporal context effect: precision improves +1.7 to +12.9pp from W=1 to best W; FPR reduces -4.0 to -5.9pp
  - 7-8B models: modality advantage (precision +22pp) exceeds temporal improvement (+13pp)
  - 32B models present contrasting profiles: R1-32B excellent lead time (+11.7–+13.3 steps) with 25% coverage; QwQ-32B robust significance (all 15 W) with negative lead time (-1.2 to +1.9 steps)
  - Negative results: BOCPD, CUSUM, Mahalanobis distance, RepE, MLP probes, CCS, and cross-model transfer all fail
- **Key Terminology:**
  - Temporal windowing (W), balanced accuracy (bal_acc), precision, false positive rate (FPR), lead time, coverage, crossing rate, Holm-Bonferroni correction, layer selection metrics, BOCPD, CUSUM, Mahalanobis distance, Representation Engineering (RepE), CCS (Contrast-Consistent Search), dimensionality constraint, position-only baseline, selectivity
- **Specific Numbers:**
  - **R1-8B (L14, W=15):** HS bal_acc +8.2pp (p=0.005), precision +22.4pp (p<0.001), FPR -7.4pp (p=0.044); selectivity 12.5pp
  - **OT-7B (L16, W=3):** HS bal_acc +10.7pp (p<0.001), precision +21.9pp (p<0.001), FPR -17.1pp (p<0.001); selectivity 18.3pp
  - **QwQ-32B (L60, W=3):** HS bal_acc +15.4pp (p<0.001), precision +23.6pp (p<0.001), FPR -9.8pp (p=0.004); selectivity 15.3pp; HS lead time -1.2 to +1.9 steps; coverage 74%
  - **R1-32B (L63, W=1):** HS bal_acc +18.7pp (p<0.001), precision +15.4pp (p<0.001), FPR -14.6pp (p=0.007); selectivity 7.5pp; HS lead time +11.7–+13.3 steps; coverage 25%; dimensionality: 51200 × W features for n=20 traces
  - Control task thresholds: all models exceed 5pp selectivity (genuine safety structure, not positional artifacts)
  - Temporal improvements (R1-8B, L14): W=1→25 increases precision from 69.3% to 82.2% (+12.9pp), reduces FPR from 9.65% to 4.8%
  - BOCPD on R1-8B: 93% detection but lead +3.5 steps < threshold +4.9 steps
  - Cross-model transfer best result: QwQ→R1-32B direct transfer 67.3% accuracy but 1% crossing rate (impractical)

---

### 5. **DISCUSSION**
- **Section Label:** `\section{Discussion}\label{sec:discussion}`
- **Main Claims:**
  - Layer selection is an underexamined methodological choice that can reverse central conclusions
  - Five-metric ablation proves crossing rate is the sole bias driver: reverses HS advantage from "scale-dependent" (significant at 7–8B, absent at 32B with biased metric) to "universal" (all 12 tests pass at corrected layers)
  - Temporal context and modality choice both improve detection, with relative magnitudes depending on scale
  - At 7-8B: modality advantage (+22pp precision) exceeds temporal improvement (+13pp)
  - At 32B: relative magnitudes depend on model and window size; text probes benefit more from temporal context due to weaker single-step baseline
  - Safety commitment is gradual, not abrupt—representations transition smoothly rather than switching
  - R1-32B and QwQ-32B (identical Qwen-32B architecture) present opposite detection profiles: likely due to training method (R1 distillation vs. native reasoning)
  - R1-32B: excellent lead time (+11.7–+13.3 steps) but narrow coverage (25%); dimensionality constraint (51200 × W features, n=20 traces) limits significance at W≥3
  - QwQ-32B: robust significance (all 15 window sizes pass Holm-Bonferroni) but negative lead time (-1.2 to +1.9 steps); position baseline nearly matches HS probe
  - Per-model validation is essential; no single configuration generalizes even within same architecture
  - Current methods achieve 39–62% FPR on safe traces; characterize phenomenon rather than constitute production-ready detectors
  - Oracle gap of 85.5% (fraction of early detection potential not captured by learned methods); learned probes achieve +4.5 steps lead time vs. oracle +31 steps
  - Hidden states encode current safety state but carry limited predictive power about future trajectory
- **Key Terminology:**
  - Researcher degree of freedom, composite metrics, layer selection bias, crossing rate, Holm-Bonferroni step-down correction, modality choice, temporal context, gradual transition, activation patching, false positive rate (FPR), coverage, lead time, oracle gap, dimensionality constraint, training method divergence
- **Specific Numbers:**
  - Biased metric selects shallow layers at 3–16% depth for 64-layer models; unbiased metrics at 94–98% depth
  - At biased layers (32B): 5 of 12 tests survive Holm-Bonferroni; at corrected layers: all 12 pass
  - Modality advantage at 7-8B: precision +22pp (exceeds temporal +13pp)
  - R1-32B lead time: +11.7–+13.3 steps before commitment; coverage 25% at W=1; dimensionality 51200 × W for n=20
  - QwQ-32B lead time: -1.2 to +1.9 steps; coverage 74%; position baseline margin -0.6pp
  - Current FPR on safe traces: 39–62% at standard operating thresholds
  - Oracle gap: 85.5% (learned +4.5 steps lead vs. oracle +31 steps)
  - Recommended defaults: temporal windowing W=3–15, principled layer selection (pure balanced accuracy or precision, never crossing rate), avoid crossing rate as selection criterion

---

## Key Takeaway for Conclusion
The paper's core narrative centers on **methodological rigor**: layer selection bias almost reverses the main finding about modality advantage. The corrected analysis reveals **universal HS dominance** (all 12 tests pass Holm-Bonferroni at correct deep layers with +15.4–+23.6pp precision) across all four models, though **practical deployment requires model-specific tuning** (R1-32B excels at early warning, QwQ-32B at robust detection). Temporal context is a universally beneficial orthogonal factor, and **alternative methods fail systematically**, confirming that supervised linear probes at deep layers with temporal windowing remain the best current approach for safety commitment detection.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6b0809f2-4998-4eee-8ba9-bbdb5a8e8362",
  "isSidechain": true,
  "agentId": "a6173ad97cfaaa5eb",
  "requestId": "req_011Cb8W7Jx4PzWpYDpR1ERrE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17ab6d97-8b89-4352-a2c4-1b62a0f271ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety",
  "sessionId": "1eb37d51-9cd9-4923-b979-fc520b94a635",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_0157YnpGNYhw9KQua59Bzatj",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6590,
      "cache_read_input_tokens": 36300,
      "output_tokens": 3560,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6590
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 3560,
          "cache_read_input_tokens": 36300,
          "cache_creation_input_tokens": 6590,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6590,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---
