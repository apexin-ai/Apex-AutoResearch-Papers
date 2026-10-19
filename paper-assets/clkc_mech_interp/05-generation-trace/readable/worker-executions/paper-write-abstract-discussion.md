# paper write abstract discussion

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 43
- **Recorded user turns:** 0
- **Tool calls:** 14
- **Original source:** `logs/workers/worker_paper_write-abstract-discussion_20260522T153557.log`
- **Structured JSON:** [`fcbe8c1d5c8e27ac1d30.json`](../../sessions/fc/fcbe8c1d5c8e27ac1d30.json)

## Before a recorded user message

43 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp",
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "b3adc736-0640-4cda-9ea7-79744452b85b",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779475200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3bf10381-3178-4ff3-abcf-787263beb376",
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing paper sections to understand the style and context before writing the Abstract and Discussion.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "41c4d8aa-a32a-4c96-873b-16aa8c83f012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137dLPrezZmHp4e1wkDV7gF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12495
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 5_

先阅读已有章节了解风格和术语。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "7062acf6-fcf0-4979-8815-3a95b2cbf634",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137dLPrezZmHp4e1wkDV7gF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12495
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 6_

<details open><summary>🔧 Tool call — Read · `toolu_01SXD4wTANqm6dyNxCTramMf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "98094197-0714-4684-b7d1-b4c1cf2e963b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137dLPrezZmHp4e1wkDV7gF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12495
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-22T15:36:07.966Z_

<details><summary>↩ Tool result · `toolu_01SXD4wTANqm6dyNxCTramMf`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	When multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.
5	\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.
6	Yet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?
7	Can it be detected from internal representations?
8	And if detectable, does the detected signal causally influence the model's resolution strategy?
9	These questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.
10	
11	Existing work on probing knowledge conflict signals has been limited to monolingual settings.
12	\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.
13	Extending these approaches cross-lingually introduces additional challenges.
14	Translation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.
15	Token overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.
16	Observed asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.
17	Beyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \citep{hewitt2019designing}.
18	\citet{basu2026interpretability} demonstrated that even near-perfect probe accuracy does not guarantee that the detected direction can steer model behavior.
19	
20	We address these questions through a pipeline (Figure~\ref{fig:pipeline}) that combines residual stream probing with representation steering across two models of distinct architectures: Llama-3.1-8B-Instruct and Qwen3-8B.
21	Probes achieve 77.1\% and 75.3\% balanced accuracy on English within-language conflict detection, respectively, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).
22	Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points (pp) more accurately than the reverse in both models.
23	This asymmetry, however, is not conflict-specific.
24	XNLI entailment-versus-contradiction probes \citep{conneau2018xnli} show the same directional pattern at comparable magnitude (+6.0 and +6.7 pp), with substantially overlapping confidence intervals.
25	The conflict asymmetry thus inherits from a general property of English-dominant models, where Chinese representations project more readily onto English representational space than the reverse.
26	Our causal analysis reveals a dissociation between detection and decision: the probe signal peaks at late layers (L28, 88\% depth), but representation steering succeeds only at a mid-layer (L13, 41\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant behavioral change.
27	To ensure these findings are robust, we apply a confound exclusion pipeline that includes COMET-based translation quality stratification, token overlap analysis, and non-conflict baseline comparison.
28	
29	These results carry two methodological implications.
30	The layer dissociation between probing peak and causal influence demonstrates that the layer with highest probe accuracy is not necessarily where the model resolves the conflict.
31	This challenges the common practice of intervening at the probing peak layer, consistent with the warning from \citet{basu2026interpretability} that detectability and causal relevance can diverge.
32	The directional asymmetry in cross-lingual transfer reflects a structural property of English-dominant multilingual models, not a conflict-specific phenomenon.
33	Any cross-lingual probing study must account for this baseline asymmetry to correctly interpret transfer differences.
34	
35	Our contributions are as follows:
36	\begin{itemize}
37	    \item \textbf{Cross-lingual conflict detectability and asymmetry characterization.} We provide the first evidence that knowledge conflict signals are linearly detectable across languages in residual stream representations. The transfer asymmetry (ZH$\to$EN $>$ EN$\to$ZH by ${\sim}$7 pp) matches the XNLI non-conflict baseline in both magnitude and direction, establishing that it reflects the model's general cross-lingual structure rather than conflict-specific encoding.
38	    \item \textbf{Detection-decision layer dissociation.} Representation steering at the mid-layer (L13, 41\% depth) causally shifts conflict resolution (Fisher $p = 0.002$), while steering at the late-layer probing peak (L28, 88\% depth) produces no significant effect. This dissociation shows that linear detectability does not imply causal relevance, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.
39	    \item \textbf{Confound exclusion pipeline for cross-lingual probing.} We design and validate a systematic pipeline of COMET translation quality ablation, token overlap analysis, and non-conflict task baseline comparison that excludes common confounds in cross-lingual probing studies.
40	\end{itemize}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "ecf17ec5-87a1-4a91-8427-2be6e5c874bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation can determine which answer the model produces.\n\\citet{zhao2026when} showed that linguistic affinity dominates conflict resolution in entity-centric factual conflicts, with models preferring answers from linguistically closer sources.\nYet the internal mechanism behind this behavior remains opaque: how does the model encode the conflict signal?\nCan it be detected from internal representations?\nAnd if detectable, does the detected signal causally influence the model's resolution strategy?\nThese questions sit at the intersection of mechanistic interpretability and multilingual NLP, and answering them requires moving beyond behavioral observations to probe model internals directly.\n\nExisting work on probing knowledge conflict signals has been limited to monolingual settings.\n\\citet{zhao2024analysing} showed that residual stream representations carry linearly detectable conflict signals in English, and \\citet{boer2026probing} performed knowledge attribution probing to localize factual associations within model parameters.\nExtending these approaches cross-lingually introduces additional challenges.\nTranslation quality may confound probe transfer: a poor translation could alter conflict detection for reasons unrelated to the conflict signal itself.\nToken overlap between languages, even when minimal, could provide a shortcut for cross-lingual probes.\nObserved asymmetries in transfer accuracy may reflect general cross-lingual properties rather than conflict-specific phenomena, and disentangling these sources requires careful baseline comparisons.\nBeyond detectability, a fundamental limitation of probing is that it establishes correlation, not causation \\citep{hewitt2019designing}.\n\\citet{basu2026interpretability} demonstrated that even near-perfect probe accuracy does not guarantee that the detected direction can steer model behavior.\n\nWe address these questions through a pipeline (Figure~\\ref{fig:pipeline}) that combines residual stream probing with representation steering across two models of distinct architectures: Llama-3.1-8B-Instruct and Qwen3-8B.\nProbes achieve 77.1\\% and 75.3\\% balanced accuracy on English within-language conflict detection, respectively, and all cross-lingual transfer directions exceed chance (binomial $p < 0.001$).\nCross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese transfer to English approximately 7 percentage points (pp) more accurately than the reverse in both models.\nThis asymmetry, however, is not conflict-specific.\nXNLI entailment-versus-contradiction probes \\citep{conneau2018xnli} show the same directional pattern at comparable magnitude (+6.0 and +6.7 pp), with substantially overlapping confidence intervals.\nThe conflict asymmetry thus inherits from a general property of English-dominant models, where Chinese representations project more readily onto English representational space than the reverse.\nOur causal analysis reveals a dissociation between detection and decision: the probe signal peaks at late layers (L28, 88\\% depth), but representation steering succeeds only at a mid-layer (L13, 41\\% depth; Fisher $p = 0.002$), with all late-layer interventions producing no significant behavioral change.\nTo ensure these findings are robust, we apply a confound exclusion pipeline that includes COMET-based translation quality stratification, token overlap analysis, and non-conflict baseline comparison.\n\nThese results carry two methodological implications.\nThe layer dissociation between probing peak and causal influence demonstrates that the layer with highest probe accuracy is not necessarily where the model resolves the conflict.\nThis challenges the common practice of intervening at the probing peak layer, consistent with the warning from \\citet{basu2026interpretability} that detectability and causal relevance can diverge.\nThe directional asymmetry in cross-lingual transfer reflects a structural property of English-dominant multilingual models, not a conflict-specific phenomenon.\nAny cross-lingual probing study must account for this baseline asymmetry to correctly interpret transfer differences.\n\nOur contributions are as follows:\n\\begin{itemize}\n    \\item \\textbf{Cross-lingual conflict detectability and asymmetry characterization.} We provide the first evidence that knowledge conflict signals are linearly detectable across languages in residual stream representations. The transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7 pp) matches the XNLI non-conflict baseline in both magnitude and direction, establishing that it reflects the model's general cross-lingual structure rather than conflict-specific encoding.\n    \\item \\textbf{Detection-decision layer dissociation.} Representation steering at the mid-layer (L13, 41\\% depth) causally shifts conflict resolution (Fisher $p = 0.002$), while steering at the late-layer probing peak (L28, 88\\% depth) produces no significant effect. This dissociation shows that linear detectability does not imply causal relevance, and that conflict resolution occurs upstream of where the outcome becomes linearly readable.\n    \\item \\textbf{Confound exclusion pipeline for cross-lingual probing.} We design and validate a systematic pipeline of COMET translation quality ablation, token overlap analysis, and non-conflict task baseline comparison that excludes common confounds in cross-lingual probing studies.\n\\end{itemize}\n",
      "numLines": 41,
      "startLine": 1,
      "totalLines": 41
    }
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Read · `toolu_019uh4kYodJ46gwDmqauwkTa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "9c707d5d-4b69-41c3-9157-2bc564a8ba01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137dLPrezZmHp4e1wkDV7gF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12495
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-22T15:36:08.579Z_

<details><summary>↩ Tool result · `toolu_019uh4kYodJ46gwDmqauwkTa`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Figure~\ref{fig:pipeline} illustrates the complete pipeline, from data construction through probing and steering.
5	We first formalize the task (\S\ref{sec:task}), then describe data construction (\S\ref{sec:data}), activation extraction (\S\ref{sec:extraction}), the probing framework (\S\ref{sec:probing}), cross-lingual transfer protocol (\S\ref{sec:transfer}), confound exclusion (\S\ref{sec:confound_method}), and representation steering (\S\ref{sec:steering_method}).
6	
7	\subsection{Task Formulation}
8	\label{sec:task}
9	
10	Given an input $x = (c, q)$ consisting of a context passage $c$ and a question $q$, the model produces an answer $a$ that is either \emph{contextual} (derived from $c$) or \emph{parametric} (derived from the model's pre-trained knowledge).
11	When $c$ contradicts the model's parametric knowledge, the choice between these two answer sources constitutes a knowledge conflict.
12	Let $\mathbf{h}_l \in \mathbb{R}^d$ denote the residual stream representation at layer $l$ for the last input token.
13	Our goal is to train a logistic regression probe $f_\theta(\mathbf{h}_l)$ that predicts a binary label $y \in \{\text{contextual}, \text{parametric}\}$ from $\mathbf{h}_l$, and to examine whether the learned probe direction transfers across languages and causally influences model behavior.
14	
15	\subsection{Data Construction}
16	\label{sec:data}
17	
18	\paragraph{Source dataset.}
19	We build on ConflictQA \citep{xie2024adaptive}, a benchmark that pairs each question with a context passage that contradicts the model's parametric knowledge.
20	Each sample contains a question, a parametric answer (ground truth from the model's training data), and a context-based answer (the contradicting information in the passage).
21	
22	\paragraph{Parametric knowledge verification.}
23	Not all samples in ConflictQA produce genuine conflicts for a given model: if the model cannot answer the question correctly without context, there is no parametric knowledge to conflict with.
24	We filter samples by first querying each model without context and retaining only those where the model produces the correct parametric answer.
25	This verification step yields 1{,}368 samples for Llama-3.1-8B-Instruct \citep{grattafiori2024llama} and 966 for Qwen3-8B \citep{yang2024qwen25}.
26	We split each set 80/20 with stratification by label, producing 1{,}096 train / 272 test for Llama and 773 train / 193 test for Qwen.
27	
28	\paragraph{Translation.}
29	To study cross-lingual transfer, we translate all English contexts and questions into Chinese (EN$\to$ZH) using a Qwen3-8B translation pipeline.
30	We validate translation quality with COMET \citep{rei2020comet} back-translation scores: each Chinese translation is back-translated to English, and the COMET score between the original and back-translated English text serves as a quality measure.
31	This score is later used for confound analysis (\S\ref{sec:confound_method}).
32	
33	\subsection{Activation Extraction}
34	\label{sec:extraction}
35	
36	For each model, we construct two language versions of every input: an English version (EN context + EN question) and a Chinese version (ZH context + ZH question).
37	We pass each version through the model and extract the last-token residual stream representation $\mathbf{h}_l \in \mathbb{R}^d$ at every layer $l \in \{0, \ldots, L-1\}$, where $L$ is the total number of layers (32 for Llama, 36 for Qwen) and $d = 4096$ for both models.
38	The last token is chosen because autoregressive models aggregate information into the final position before generating the next token \citep{belinkov2022probing}.
39	We then record the model's predicted answer for each input and assign the binary label $y$: contextual if the model chose the context-based answer, parametric otherwise.
40	
41	\subsection{Probing Framework}
42	\label{sec:probing}
43	
44	At each layer $l$, we train a logistic regression classifier with $L_2$ regularization on the extracted representations $\{\mathbf{h}_l^{(i)}, y^{(i)}\}_{i=1}^{N_\text{train}}$ \citep{belinkov2022probing, hewitt2019designing}.
45	The probe $f_\theta(\mathbf{h}_l) = \sigma(\mathbf{w}_l^\top \mathbf{h}_l + b_l)$ outputs the probability of the contextual class, where $\mathbf{w}_l \in \mathbb{R}^d$ is the weight vector and $b_l$ is the bias.
46	We evaluate with balanced accuracy (the macro-average of per-class recall) to account for class imbalance.
47	We report the peak-layer accuracy, defined as the maximum balanced accuracy across all layers, as the primary metric for each probe transfer direction.
48	
49	Confidence intervals (CIs) are estimated via bootstrap resampling \citep{ulmer2022deep}.
50	For each bootstrap iteration, we resample the test set with replacement, compute balanced accuracy, and derive 95\% CIs from the empirical distribution.
51	For asymmetry estimation, we use paired bootstrap differences (described in \S\ref{sec:transfer}).
52	
53	\subsection{Cross-Lingual Transfer Protocol}
54	\label{sec:transfer}
55	
56	We evaluate probes in four transfer directions: EN$\to$EN (train and test on English activations), ZH$\to$ZH (train and test on Chinese), EN$\to$ZH (train on English, test on Chinese), and ZH$\to$EN (train on Chinese, test on English).
57	The within-language directions (EN$\to$EN, ZH$\to$ZH) establish upper bounds, while the cross-lingual directions test whether conflict representations share structure across languages.
58	
59	To quantify the directional asymmetry between the two cross-lingual directions, we define:
60	\begin{equation}
61	\Delta_{\text{asym}} = \text{acc}(\text{ZH}{\to}\text{EN}) - \text{acc}(\text{EN}{\to}\text{ZH})
62	\label{eq:asymmetry}
63	\end{equation}
64	A positive $\Delta_{\text{asym}}$ indicates that Chinese-trained probes transfer to English more readily than the reverse.
65	We compute $\Delta_{\text{asym}}$ via paired bootstrap: in each iteration, the same resampled test indices are used for both directions, and the paired difference eliminates sample-level variance.
66	We report the mean and 95\% CI of the bootstrap distribution.
67	
68	\subsection{Confound Exclusion}
69	\label{sec:confound_method}
70	
71	Cross-lingual probe transfer could reflect artifacts of translation quality or lexical overlap rather than shared representations.
72	We design two controls to exclude these confounds.
73	
74	\paragraph{COMET tercile ablation.}
75	We stratify test samples into terciles by their COMET back-translation score (high, medium, low quality) and compare probe accuracy across strata.
76	If translation quality drove transfer, high-quality translations would yield higher probe accuracy.
77	We test this with Fisher's exact test on the accuracy difference between the top and bottom terciles.
78	
79	\paragraph{Token overlap analysis.}
80	Despite the large typographic distance between English and Chinese, some tokens (numbers, proper nouns, punctuation) may be shared after subword tokenization.
81	We compute the per-sample Jaccard similarity between the English and Chinese token sets and test for correlation with probe accuracy via Pearson's $r$.
82	A positive correlation would suggest that shared tokens, rather than shared representations, drive transfer.
83	
84	\paragraph{Non-conflict baseline.}
85	To test whether cross-lingual transfer asymmetry is specific to knowledge conflicts, we apply the same probing pipeline to XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
86	If the asymmetry pattern ($\Delta_{\text{asym}} > 0$) also appears in a non-conflict task, it reflects a general cross-lingual property rather than a conflict-specific phenomenon.
87	
88	\subsection{Representation Steering}
89	\label{sec:steering_method}
90	
91	Probing establishes that conflict signals are linearly detectable, but detection does not imply causal relevance \citep{hewitt2019designing}.
92	We test the causal role of the probe direction by injecting it into the model's forward pass during inference, following the inference-time intervention framework of \citet{li2023iti} and \citet{zou2023representation}.
93	
94	\paragraph{Intervention procedure.}
95	Let $\mathbf{w}_{\text{probe}}$ denote the weight vector of the logistic regression probe trained at a target layer $l$.
96	During inference, we modify the last-token residual stream at layer $l$:
97	\begin{equation}
98	\mathbf{h}'_l = \mathbf{h}_l + \alpha \cdot \mathbf{w}_{\text{probe}}
99	\label{eq:steering}
100	\end{equation}
101	where $\alpha \in \mathbb{R}$ is the steering magnitude.
102	Positive $\alpha$ pushes the representation toward the contextual direction; negative $\alpha$ pushes toward the parametric direction.
103	
104	\paragraph{Control condition.}
105	We replace $\mathbf{w}_{\text{probe}}$ with a random unit vector $\mathbf{w}_{\text{random}}$ of equal norm, injected with the same $\alpha$.
106	This controls for the possibility that any perturbation of sufficient magnitude could alter model behavior.
107	
108	\paragraph{Evaluation.}
109	We measure the flip rate: the fraction of test samples that switch answer category (parametric $\leftrightarrow$ contextual) after intervention.
110	We compare steering and control flip rates with Fisher's exact test, applying Bonferroni correction for multiple comparisons across layers and $\alpha$ values.
111	We test at three layers spanning different depths: L13 (41\% depth), L18 (56\% depth), and L28 (88\% depth, the probing accuracy peak).
112	The steering magnitude $\alpha$ is swept over $\{-20, -10, -5, +2, +5, +10, +20\}$ to characterize the effective range.
113	If the probe direction is causally relevant, the steering flip rate should significantly exceed the control, and the direction of flips (parametric-to-contextual vs.\ contextual-to-parametric) should be consistent with the sign of $\alpha$.
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "15553959-f1f9-4045-a5f3-951fef0fffbd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nFigure~\\ref{fig:pipeline} illustrates the complete pipeline, from data construction through probing and steering.\nWe first formalize the task (\\S\\ref{sec:task}), then describe data construction (\\S\\ref{sec:data}), activation extraction (\\S\\ref{sec:extraction}), the probing framework (\\S\\ref{sec:probing}), cross-lingual transfer protocol (\\S\\ref{sec:transfer}), confound exclusion (\\S\\ref{sec:confound_method}), and representation steering (\\S\\ref{sec:steering_method}).\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven an input $x = (c, q)$ consisting of a context passage $c$ and a question $q$, the model produces an answer $a$ that is either \\emph{contextual} (derived from $c$) or \\emph{parametric} (derived from the model's pre-trained knowledge).\nWhen $c$ contradicts the model's parametric knowledge, the choice between these two answer sources constitutes a knowledge conflict.\nLet $\\mathbf{h}_l \\in \\mathbb{R}^d$ denote the residual stream representation at layer $l$ for the last input token.\nOur goal is to train a logistic regression probe $f_\\theta(\\mathbf{h}_l)$ that predicts a binary label $y \\in \\{\\text{contextual}, \\text{parametric}\\}$ from $\\mathbf{h}_l$, and to examine whether the learned probe direction transfers across languages and causally influences model behavior.\n\n\\subsection{Data Construction}\n\\label{sec:data}\n\n\\paragraph{Source dataset.}\nWe build on ConflictQA \\citep{xie2024adaptive}, a benchmark that pairs each question with a context passage that contradicts the model's parametric knowledge.\nEach sample contains a question, a parametric answer (ground truth from the model's training data), and a context-based answer (the contradicting information in the passage).\n\n\\paragraph{Parametric knowledge verification.}\nNot all samples in ConflictQA produce genuine conflicts for a given model: if the model cannot answer the question correctly without context, there is no parametric knowledge to conflict with.\nWe filter samples by first querying each model without context and retaining only those where the model produces the correct parametric answer.\nThis verification step yields 1{,}368 samples for Llama-3.1-8B-Instruct \\citep{grattafiori2024llama} and 966 for Qwen3-8B \\citep{yang2024qwen25}.\nWe split each set 80/20 with stratification by label, producing 1{,}096 train / 272 test for Llama and 773 train / 193 test for Qwen.\n\n\\paragraph{Translation.}\nTo study cross-lingual transfer, we translate all English contexts and questions into Chinese (EN$\\to$ZH) using a Qwen3-8B translation pipeline.\nWe validate translation quality with COMET \\citep{rei2020comet} back-translation scores: each Chinese translation is back-translated to English, and the COMET score between the original and back-translated English text serves as a quality measure.\nThis score is later used for confound analysis (\\S\\ref{sec:confound_method}).\n\n\\subsection{Activation Extraction}\n\\label{sec:extraction}\n\nFor each model, we construct two language versions of every input: an English version (EN context + EN question) and a Chinese version (ZH context + ZH question).\nWe pass each version through the model and extract the last-token residual stream representation $\\mathbf{h}_l \\in \\mathbb{R}^d$ at every layer $l \\in \\{0, \\ldots, L-1\\}$, where $L$ is the total number of layers (32 for Llama, 36 for Qwen) and $d = 4096$ for both models.\nThe last token is chosen because autoregressive models aggregate information into the final position before generating the next token \\citep{belinkov2022probing}.\nWe then record the model's predicted answer for each input and assign the binary label $y$: contextual if the model chose the context-based answer, parametric otherwise.\n\n\\subsection{Probing Framework}\n\\label{sec:probing}\n\nAt each layer $l$, we train a logistic regression classifier with $L_2$ regularization on the extracted representations $\\{\\mathbf{h}_l^{(i)}, y^{(i)}\\}_{i=1}^{N_\\text{train}}$ \\citep{belinkov2022probing, hewitt2019designing}.\nThe probe $f_\\theta(\\mathbf{h}_l) = \\sigma(\\mathbf{w}_l^\\top \\mathbf{h}_l + b_l)$ outputs the probability of the contextual class, where $\\mathbf{w}_l \\in \\mathbb{R}^d$ is the weight vector and $b_l$ is the bias.\nWe evaluate with balanced accuracy (the macro-average of per-class recall) to account for class imbalance.\nWe report the peak-layer accuracy, defined as the maximum balanced accuracy across all layers, as the primary metric for each probe transfer direction.\n\nConfidence intervals (CIs) are estimated via bootstrap resampling \\citep{ulmer2022deep}.\nFor each bootstrap iteration, we resample the test set with replacement, compute balanced accuracy, and derive 95\\% CIs from the empirical distribution.\nFor asymmetry estimation, we use paired bootstrap differences (described in \\S\\ref{sec:transfer}).\n\n\\subsection{Cross-Lingual Transfer Protocol}\n\\label{sec:transfer}\n\nWe evaluate probes in four transfer directions: EN$\\to$EN (train and test on English activations), ZH$\\to$ZH (train and test on Chinese), EN$\\to$ZH (train on English, test on Chinese), and ZH$\\to$EN (train on Chinese, test on English).\nThe within-language directions (EN$\\to$EN, ZH$\\to$ZH) establish upper bounds, while the cross-lingual directions test whether conflict representations share structure across languages.\n\nTo quantify the directional asymmetry between the two cross-lingual directions, we define:\n\\begin{equation}\n\\Delta_{\\text{asym}} = \\text{acc}(\\text{ZH}{\\to}\\text{EN}) - \\text{acc}(\\text{EN}{\\to}\\text{ZH})\n\\label{eq:asymmetry}\n\\end{equation}\nA positive $\\Delta_{\\text{asym}}$ indicates that Chinese-trained probes transfer to English more readily than the reverse.\nWe compute $\\Delta_{\\text{asym}}$ via paired bootstrap: in each iteration, the same resampled test indices are used for both directions, and the paired difference eliminates sample-level variance.\nWe report the mean and 95\\% CI of the bootstrap distribution.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confound_method}\n\nCross-lingual probe transfer could reflect artifacts of translation quality or lexical overlap rather than shared representations.\nWe design two controls to exclude these confounds.\n\n\\paragraph{COMET tercile ablation.}\nWe stratify test samples into terciles by their COMET back-translation score (high, medium, low quality) and compare probe accuracy across strata.\nIf translation quality drove transfer, high-quality translations would yield higher probe accuracy.\nWe test this with Fisher's exact test on the accuracy difference between the top and bottom terciles.\n\n\\paragraph{Token overlap analysis.}\nDespite the large typographic distance between English and Chinese, some tokens (numbers, proper nouns, punctuation) may be shared after subword tokenization.\nWe compute the per-sample Jaccard similarity between the English and Chinese token sets and test for correlation with probe accuracy via Pearson's $r$.\nA positive correlation would suggest that shared tokens, rather than shared representations, drive transfer.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer asymmetry is specific to knowledge conflicts, we apply the same probing pipeline to XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\nIf the asymmetry pattern ($\\Delta_{\\text{asym}} > 0$) also appears in a non-conflict task, it reflects a general cross-lingual property rather than a conflict-specific phenomenon.\n\n\\subsection{Representation Steering}\n\\label{sec:steering_method}\n\nProbing establishes that conflict signals are linearly detectable, but detection does not imply causal relevance \\citep{hewitt2019designing}.\nWe test the causal role of the probe direction by injecting it into the model's forward pass during inference, following the inference-time intervention framework of \\citet{li2023iti} and \\citet{zou2023representation}.\n\n\\paragraph{Intervention procedure.}\nLet $\\mathbf{w}_{\\text{probe}}$ denote the weight vector of the logistic regression probe trained at a target layer $l$.\nDuring inference, we modify the last-token residual stream at layer $l$:\n\\begin{equation}\n\\mathbf{h}'_l = \\mathbf{h}_l + \\alpha \\cdot \\mathbf{w}_{\\text{probe}}\n\\label{eq:steering}\n\\end{equation}\nwhere $\\alpha \\in \\mathbb{R}$ is the steering magnitude.\nPositive $\\alpha$ pushes the representation toward the contextual direction; negative $\\alpha$ pushes toward the parametric direction.\n\n\\paragraph{Control condition.}\nWe replace $\\mathbf{w}_{\\text{probe}}$ with a random unit vector $\\mathbf{w}_{\\text{random}}$ of equal norm, injected with the same $\\alpha$.\nThis controls for the possibility that any perturbation of sufficient magnitude could alter model behavior.\n\n\\paragraph{Evaluation.}\nWe measure the flip rate: the fraction of test samples that switch answer category (parametric $\\leftrightarrow$ contextual) after intervention.\nWe compare steering and control flip rates with Fisher's exact test, applying Bonferroni correction for multiple comparisons across layers and $\\alpha$ values.\nWe test at three layers spanning different depths: L13 (41\\% depth), L18 (56\\% depth), and L28 (88\\% depth, the probing accuracy peak).\nThe steering magnitude $\\alpha$ is swept over $\\{-20, -10, -5, +2, +5, +10, +20\\}$ to characterize the effective range.\nIf the probe direction is causally relevant, the steering flip rate should significantly exceed the control, and the direction of flips (parametric-to-contextual vs.\\ contextual-to-parametric) should be consistent with the sign of $\\alpha$.\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  }
}
```

</details>

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Read · `toolu_0181sLP58sUxYyqZGL6mJQG6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "375eb0fb-c03b-4465-840e-976dcad0d92c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0137dLPrezZmHp4e1wkDV7gF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12495,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12495
      },
      "output_tokens": 37,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T15:36:09.069Z_

<details><summary>↩ Tool result · `toolu_0181sLP58sUxYyqZGL6mJQG6`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Models.}
8	We probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \citep{yang2024qwen25}.
9	
10	\paragraph{Dataset.}
11	We use ConflictQA \citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.
12	After verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.
13	
14	\paragraph{Translation.}
15	We translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\to$ZH), with quality validated by COMET \citep{rei2020comet} back-translation scores.
16	
17	\paragraph{Probing.}
18	For each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.
19	We report balanced accuracy to account for class imbalance.
20	All confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.
21	
22	\paragraph{Non-conflict baseline.}
23	To test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \citep{conneau2018xnli}, classifying entailment versus contradiction.
24	
25	\subsection{Within-Language Conflict Detection}
26	\label{sec:within_lang}
27	
28	Table~\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.
29	Both models encode linearly detectable conflict signals in their residual streams.
30	Llama achieves 77.1\% on EN$\to$EN (peak at layer 28, 88\% depth) and 71.2\% on ZH$\to$ZH.
31	Qwen reaches 75.3\% on EN$\to$EN (peak at layer 22, 61\% depth) and 71.6\% on ZH$\to$ZH.
32	All within-language accuracies are significantly above chance (binomial $p < 0.001$).
33	Figure~\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.
34	These results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.
35	
36	\subsection{Cross-Lingual Transfer and Asymmetry}
37	\label{sec:cross_lingual}
38	
39	All four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.
40	Both models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\to$EN) more accurately than the reverse direction (EN$\to$ZH).
41	For Llama, $\Delta_{\text{asym}} = +7.2$ percentage points (pp) with a 95\% bootstrap CI of [1.1, 13.6]; for Qwen, $\Delta_{\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].
42	The magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\S\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\ref{fig:asymmetry_forest}).
43	
44	%% Table 1: Main cross-lingual probe results
45	\begin{table}[t]
46	\centering
47	\caption{Cross-lingual probe balanced accuracy (\%) with bootstrap 95\% CIs ($n \geq 100$). $\Delta_{\text{asym}}$ = acc(ZH$\to$EN) $-$ acc(EN$\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}
48	\label{tab:main_results}
49	\begin{tabular}{lcc}
50	\toprule
51	Direction & Llama-3.1-8B & Qwen3-8B \\
52	\midrule
53	\multicolumn{3}{l}{\textit{Conflict Task}} \\
54	EN $\to$ EN & \textbf{77.1} & \textbf{75.3} \\
55	ZH $\to$ ZH & 71.2 & 71.6 \\
56	EN $\to$ ZH & 64.1 & 65.0 \\
57	ZH $\to$ EN & 71.3 & 72.2 \\
58	$\Delta_{\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\
59	\midrule
60	\multicolumn{3}{l}{\textit{XNLI Baseline}} \\
61	EN $\to$ EN & 94.0 & 96.6 \\
62	ZH $\to$ ZH & 87.5 & 89.5 \\
63	EN $\to$ ZH & 89.0 & 90.5 \\
64	ZH $\to$ EN & \textbf{94.9} & \textbf{97.2} \\
65	$\Delta_{\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\
66	\bottomrule
67	\end{tabular}
68	\end{table}
69	
70	\subsection{Non-Conflict Baseline Comparison}
71	\label{sec:xnli_baseline}
72	
73	If the ZH$\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.
74	We test this prediction using XNLI entailment-versus-contradiction probes.
75	Both models achieve high within-language accuracy on XNLI (Llama 94.0\% EN, 87.5\% ZH; Qwen 96.6\% EN, 89.5\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.
76	The XNLI probes exhibit the same directional asymmetry: Llama $\Delta_{\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\Delta_{\text{asym}} = +6.7$ pp, CI [2.4, 11.7].
77	Both XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\ref{fig:asymmetry_forest}).
78	The close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\to$EN transfer advantage is not specific to knowledge conflict representations.
79	Instead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.
80	
81	\subsection{Confound Exclusion}
82	\label{sec:confounds}
83	
84	Two potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.
85	
86	\paragraph{Translation quality.}
87	We stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\to$ZH probe accuracy across strata.
88	If translation quality drove probe transfer, high-COMET samples would yield higher accuracy.
89	Table~\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\Delta = +1.7$ pp, Fisher $p = 0.761$).
90	Translation quality does not confound the cross-lingual transfer results.
91	
92	\paragraph{Token overlap.}
93	Per-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\%, consistent with the minimal lexical overlap between the two languages.
94	Neither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \emph{lower} accuracy.
95	Shared tokens do not drive cross-lingual transfer.
96	
97	%% Table 2: Confound exclusion
98	\begin{table}[t]
99	\centering
100	\caption{Confound exclusion analysis. COMET tercile: $\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\to$ZH probe accuracy.}
101	\label{tab:confound}
102	\begin{tabular}{llrl}
103	\toprule
104	Confound & Model & Result & $p$ \\
105	\midrule
106	COMET tercile & Qwen & $\Delta = -5.6$ pp & 0.695 \\
107	COMET tercile & Llama & $\Delta = +1.7$ pp & 0.761 \\
108	\midrule
109	Token overlap & Qwen & n.s. & $>$0.4 \\
110	Token overlap & Llama & $r = -0.15$ & 0.012 \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\subsection{Causal Evidence via Representation Steering}
116	\label{sec:steering}
117	
118	The probing results establish that conflict signals are detectable, but detection does not imply causal relevance.
119	We test whether the probe weight direction $\mathbf{w}_{\text{probe}}$ causally influences conflict resolution by injecting $\alpha \cdot \mathbf{w}_{\text{probe}}$ into the last-token residual stream at a target layer during inference.
120	We measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.
121	
122	\paragraph{L13 (mid-layer, 41\% depth).}
123	Steering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\ref{tab:steering}).
124	Positive steering ($\alpha = +5$) yields a flip rate of 19.9\% versus 6.6\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.
125	Negative steering ($\alpha = -20$) yields 36.0\% versus 17.6\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.
126	Both results survive Bonferroni correction for multiple comparisons.
127	The bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.
128	
129	\paragraph{Negative layers.}
130	Steering at L28 (the probing peak layer, 88\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\ref{tab:steering}).
131	L18 (the MLP probe peak, 56\% depth) also shows no causal influence (all Fisher $p > 0.44$).
132	
133	\paragraph{$\alpha = +20$ reversal.}
134	At extreme perturbation magnitude ($\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).
135	This indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.
136	
137	\paragraph{Detection $\neq$ Decision.}
138	The detectable conflict signal peaks at late layers (L28, 88\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\% depth).
139	Probing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.
140	\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.
141	
142	%% Table 3: Steering results
143	\begin{table}[t]
144	\centering
145	\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
146	\label{tab:steering}
147	\small
148	\begin{tabular}{lcrrrrl}
149	\toprule
150	Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
151	\midrule
152	\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
153	\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
154	L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
155	L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
156	L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 0.370 & \\
157	\midrule
158	\multicolumn{7}{l}{\textit{Qwen3-8B L13: \textbf{[PLACEHOLDER]}}} \\
159	\bottomrule
160	\end{tabular}
161	\begin{flushleft}
162	\footnotesize $^{\dagger}$ At $\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.
163	\end{flushleft}
164	\end{table}
165	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "2d530e44-3ae0-49bf-abd9-43015ab81f90",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Models.}\nWe probe two instruction-tuned models with comparable parameter counts but distinct architectures: Llama-3.1-8B-Instruct (32 layers, hidden dimension 4096) \\citep{grattafiori2024llama} and Qwen3-8B (36 layers, hidden dimension 4096) \\citep{yang2024qwen25}.\n\n\\paragraph{Dataset.}\nWe use ConflictQA \\citep{xie2024adaptive}, a benchmark of context-parametric knowledge conflicts where a provided context contradicts the model's parametric knowledge.\nAfter verifying that each model can correctly answer the parametric-knowledge question without context, we retain 1{,}368 samples for Llama (1{,}096 train / 272 test) and 966 samples for Qwen (773 train / 193 test), split 80/20 with stratification.\n\n\\paragraph{Translation.}\nWe translate all English contexts and questions into Chinese using a Qwen3-8B translation pipeline (EN$\\to$ZH), with quality validated by COMET \\citep{rei2020comet} back-translation scores.\n\n\\paragraph{Probing.}\nFor each layer $l$, we train a logistic regression probe on the last-token residual stream representation $\\mathbf{h}_l$, with binary labels indicating whether the model chose the contextual or parametric answer.\nWe report balanced accuracy to account for class imbalance.\nAll confidence intervals (CIs) are computed via bootstrap resampling with paired differences for asymmetry estimation.\n\n\\paragraph{Non-conflict baseline.}\nTo test whether cross-lingual transfer patterns are specific to knowledge conflicts, we run the same probing pipeline on XNLI \\citep{conneau2018xnli}, classifying entailment versus contradiction.\n\n\\subsection{Within-Language Conflict Detection}\n\\label{sec:within_lang}\n\nTable~\\ref{tab:main_results} reports balanced accuracy for all probe transfer directions.\nBoth models encode linearly detectable conflict signals in their residual streams.\nLlama achieves 77.1\\% on EN$\\to$EN (peak at layer 28, 88\\% depth) and 71.2\\% on ZH$\\to$ZH.\nQwen reaches 75.3\\% on EN$\\to$EN (peak at layer 22, 61\\% depth) and 71.6\\% on ZH$\\to$ZH.\nAll within-language accuracies are significantly above chance (binomial $p < 0.001$).\nFigure~\\ref{fig:layer_probe} shows the layer-wise probe accuracy curves for both models.\nThese results confirm that knowledge conflict signals are linearly separable in the residual stream across both architectures and both languages.\n\n\\subsection{Cross-Lingual Transfer and Asymmetry}\n\\label{sec:cross_lingual}\n\nAll four cross-lingual transfer directions achieve balanced accuracy above chance (binomial $p < 0.001$; Table~\\ref{tab:main_results}), confirming that conflict representations partially overlap across languages.\nBoth models show a consistent directional trend: probes trained on Chinese representations transfer to English (ZH$\\to$EN) more accurately than the reverse direction (EN$\\to$ZH).\nFor Llama, $\\Delta_{\\text{asym}} = +7.2$ percentage points (pp) with a 95\\% bootstrap CI of [1.1, 13.6]; for Qwen, $\\Delta_{\\text{asym}} = +7.2$ pp with CI [$-$0.6, 13.7].\nThe magnitude of this asymmetry closely matches the XNLI non-conflict baseline (\\S\\ref{sec:xnli_baseline}), and the consistent direction across architectures suggests a shared structural property rather than a model-specific artifact (Figure~\\ref{fig:asymmetry_forest}).\n\n%% Table 1: Main cross-lingual probe results\n\\begin{table}[t]\n\\centering\n\\caption{Cross-lingual probe balanced accuracy (\\%) with bootstrap 95\\% CIs ($n \\geq 100$). $\\Delta_{\\text{asym}}$ = acc(ZH$\\to$EN) $-$ acc(EN$\\to$ZH), computed as the mean of paired bootstrap differences. Bold: best per-task direction.}\n\\label{tab:main_results}\n\\begin{tabular}{lcc}\n\\toprule\nDirection & Llama-3.1-8B & Qwen3-8B \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Conflict Task}} \\\\\nEN $\\to$ EN & \\textbf{77.1} & \\textbf{75.3} \\\\\nZH $\\to$ ZH & 71.2 & 71.6 \\\\\nEN $\\to$ ZH & 64.1 & 65.0 \\\\\nZH $\\to$ EN & 71.3 & 72.2 \\\\\n$\\Delta_{\\text{asym}}$ & +7.2 [1.1, 13.6] & +7.2 [$-$0.6, 13.7] \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{XNLI Baseline}} \\\\\nEN $\\to$ EN & 94.0 & 96.6 \\\\\nZH $\\to$ ZH & 87.5 & 89.5 \\\\\nEN $\\to$ ZH & 89.0 & 90.5 \\\\\nZH $\\to$ EN & \\textbf{94.9} & \\textbf{97.2} \\\\\n$\\Delta_{\\text{asym}}$ & +6.0 [0.9, 11.3] & +6.7 [2.4, 11.7] \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Non-Conflict Baseline Comparison}\n\\label{sec:xnli_baseline}\n\nIf the ZH$\\to$EN transfer advantage were specific to knowledge conflicts, it should be absent or substantially reduced in a non-conflict semantic task.\nWe test this prediction using XNLI entailment-versus-contradiction probes.\nBoth models achieve high within-language accuracy on XNLI (Llama 94.0\\% EN, 87.5\\% ZH; Qwen 96.6\\% EN, 89.5\\% ZH), confirming that the probing pipeline captures semantic distinctions beyond knowledge conflicts.\nThe XNLI probes exhibit the same directional asymmetry: Llama $\\Delta_{\\text{asym}} = +6.0$ pp, CI [0.9, 11.3]; Qwen $\\Delta_{\\text{asym}} = +6.7$ pp, CI [2.4, 11.7].\nBoth XNLI CIs exclude zero, and both overlap substantially with the corresponding conflict-task CIs (Figure~\\ref{fig:asymmetry_forest}).\nThe close match in asymmetry magnitude between conflict probes (Llama +7.2, Qwen +7.2 pp) and XNLI probes (Llama +6.0, Qwen +6.7 pp) indicates that the ZH$\\to$EN transfer advantage is not specific to knowledge conflict representations.\nInstead, it reflects a general cross-lingual property: Chinese-trained probes transfer to English more readily than the reverse, regardless of the downstream task.\n\n\\subsection{Confound Exclusion}\n\\label{sec:confounds}\n\nTwo potential confounds could inflate cross-lingual probe accuracy: translation quality and lexical overlap between English and Chinese inputs.\n\n\\paragraph{Translation quality.}\nWe stratify test samples by COMET score into terciles (high, medium, low) and compare EN$\\to$ZH probe accuracy across strata.\nIf translation quality drove probe transfer, high-COMET samples would yield higher accuracy.\nTable~\\ref{tab:confound} shows no such pattern: Qwen exhibits a reversed direction ($\\Delta = -5.6$ pp, Fisher $p = 0.695$), and Llama shows a negligible effect ($\\Delta = +1.7$ pp, Fisher $p = 0.761$).\nTranslation quality does not confound the cross-lingual transfer results.\n\n\\paragraph{Token overlap.}\nPer-sample Jaccard similarity between English and Chinese tokenized inputs averages 3--4\\%, consistent with the minimal lexical overlap between the two languages.\nNeither model shows a positive correlation between token overlap and probe accuracy: Qwen yields no significant correlation ($p > 0.4$), and Llama shows a weak negative correlation ($r = -0.15$, $p = 0.012$), where higher overlap is associated with \\emph{lower} accuracy.\nShared tokens do not drive cross-lingual transfer.\n\n%% Table 2: Confound exclusion\n\\begin{table}[t]\n\\centering\n\\caption{Confound exclusion analysis. COMET tercile: $\\Delta$ = balanced accuracy difference between high and low COMET score terciles for EN$\\to$ZH probes (Fisher's exact test). Token overlap: Pearson correlation between per-sample Jaccard similarity and EN$\\to$ZH probe accuracy.}\n\\label{tab:confound}\n\\begin{tabular}{llrl}\n\\toprule\nConfound & Model & Result & $p$ \\\\\n\\midrule\nCOMET tercile & Qwen & $\\Delta = -5.6$ pp & 0.695 \\\\\nCOMET tercile & Llama & $\\Delta = +1.7$ pp & 0.761 \\\\\n\\midrule\nToken overlap & Qwen & n.s. & $>$0.4 \\\\\nToken overlap & Llama & $r = -0.15$ & 0.012 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Causal Evidence via Representation Steering}\n\\label{sec:steering}\n\nThe probing results establish that conflict signals are detectable, but detection does not imply causal relevance.\nWe test whether the probe weight direction $\\mathbf{w}_{\\text{probe}}$ causally influences conflict resolution by injecting $\\alpha \\cdot \\mathbf{w}_{\\text{probe}}$ into the last-token residual stream at a target layer during inference.\nWe measure the flip rate (fraction of samples that switch answer category) and compare against a random-direction control of equal magnitude via Fisher's exact test.\n\n\\paragraph{L13 (mid-layer, 41\\% depth).}\nSteering at layer 13 produces significantly more behavioral change than random controls in both directions (Table~\\ref{tab:steering}).\nPositive steering ($\\alpha = +5$) yields a flip rate of 19.9\\% versus 6.6\\% for the random control (Fisher $p = 0.002$), with all 4 directional flips moving from parametric to contextual answers.\nNegative steering ($\\alpha = -20$) yields 36.0\\% versus 17.6\\% (Fisher $p < 0.001$), with 5 of 6 directional flips moving from contextual to parametric.\nBoth results survive Bonferroni correction for multiple comparisons.\nThe bidirectionality confirms that the probe weight vector encodes a meaningful axis of conflict resolution: positive perturbations push toward contextual answers, and negative perturbations push toward parametric answers.\n\n\\paragraph{Negative layers.}\nSteering at L28 (the probing peak layer, 88\\% depth) produces no significant effect with either last-token or all-position injection (all Fisher $p > 0.3$; Table~\\ref{tab:steering}).\nL18 (the MLP probe peak, 56\\% depth) also shows no causal influence (all Fisher $p > 0.44$).\n\n\\paragraph{$\\alpha = +20$ reversal.}\nAt extreme perturbation magnitude ($\\alpha = +20$), the control condition produces more flips than the steering condition ($p = 0.053$).\nThis indicates coherence collapse at large perturbation magnitudes, constraining the effective steering range.\n\n\\paragraph{Detection $\\neq$ Decision.}\nThe detectable conflict signal peaks at late layers (L28, 88\\% depth), but causal influence on conflict resolution is localized to the mid-layer (L13, 41\\% depth).\nProbing accuracy and causal relevance thus identify different computational stages: late layers encode the outcome of conflict resolution in a linearly readable form, while mid-layers host the computation that determines the outcome.\n\\textbf{[PLACEHOLDER]} Qwen L13 steering results will provide cross-model validation of this dissociation.\n\n%% Table 3: Steering results\n\\begin{table}[t]\n\\centering\n\\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\\dagger}$}\n\\label{tab:steering}\n\\small\n\\begin{tabular}{lcrrrrl}\n\\toprule\nLayer & Depth & $\\alpha$ & Steer (\\%) & Ctrl (\\%) & Fisher $p$ & Dir. \\\\\n\\midrule\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{+5}$ & \\textbf{19.9} & \\textbf{6.6} & $\\mathbf{0.002}$ & \\textbf{4 p$\\to$c} \\\\\n\\textbf{L13} & \\textbf{41\\%} & $\\mathbf{-20}$ & \\textbf{36.0} & \\textbf{17.6} & $\\mathbf{<0.001}$ & \\textbf{5 c$\\to$p} \\\\\nL18 & 56\\% & $+2$ & 3.7 & 1.5 & 0.447 & \\\\\nL28 & 88\\% & $-20$ & 14.7 & 16.9 & 0.740 & \\\\\nL28 (all) & 88\\% & $-20$ & 11.8 & 11.8 & 0.370 & \\\\\n\\midrule\n\\multicolumn{7}{l}{\\textit{Qwen3-8B L13: \\textbf{[PLACEHOLDER]}}} \\\\\n\\bottomrule\n\\end{tabular}\n\\begin{flushleft}\n\\footnotesize $^{\\dagger}$ At $\\alpha = +20$, the control flip rate exceeds steering ($p = 0.053$), indicating coherence collapse at extreme perturbation magnitudes.\n\\end{flushleft}\n\\end{table}\n",
      "numLines": 165,
      "startLine": 1,
      "totalLines": 165
    }
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check if there are any other existing sections to understand the full paper context, and check the memory/roadmap for any additional context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "7e5afcf7-742d-460f-bf09-e7faea55bac2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2Xukme7JCxwURKgnijvBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 24336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 13_

Let me also check the paper structure and any existing related work section for terminology consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "9b34c6c0-c5ff-40f8-968f-6985f781414f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2Xukme7JCxwURKgnijvBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 24336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Glob · `toolu_01AadvSGMBvevB9uFh98vUg8`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "19b8ccd9-b4b2-42c6-abb5-eab1868c0a0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2Xukme7JCxwURKgnijvBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 24336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-22T15:36:15.263Z_

<details><summary>↩ Tool result · `toolu_01AadvSGMBvevB9uFh98vUg8`</summary>

```text
docs/paper/acl_latex.tex
docs/paper/sections/experiments.tex
docs/paper/experiments.tex
docs/paper/main.tex
docs/paper/sections/method.tex
docs/paper/method.tex
docs/paper/sections/introduction.tex
docs/paper/introduction.tex
docs/paper/sections/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "bafb03d2-1b45-42b3-903c-087427a61638",
  "tool_use_result": {
    "filenames": [
      "docs/paper/acl_latex.tex",
      "docs/paper/sections/experiments.tex",
      "docs/paper/experiments.tex",
      "docs/paper/main.tex",
      "docs/paper/sections/method.tex",
      "docs/paper/method.tex",
      "docs/paper/sections/introduction.tex",
      "docs/paper/introduction.tex",
      "docs/paper/sections/related_work.tex"
    ],
    "durationMs": 9,
    "numFiles": 9,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01Ag4VnCXahKnmEmscV3e71C`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "b67a3174-3c61-4d92-9cf2-0e38ca4e5123",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G2Xukme7JCxwURKgnijvBw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8543,
      "cache_read_input_tokens": 24336,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8543
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-22T15:36:15.750Z_

<details><summary>↩ Tool result · `toolu_01Ag4VnCXahKnmEmscV3e71C`</summary>

```text
1	# 关键研究发现
2	
3	## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]
4	
5	**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。
6	
7	| Model | XNLI asymmetry | Conflict asymmetry |
8	|-------|---------------|-------------------|
9	| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |
10	| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |
11	
12	**推导**：英语主导预训练 → EN 表征空间更"标准" → ZH→EN 迁移天然更好。C2 需 reframe：从 "conflict-specific asymmetry" 改为 "conflict signals share general cross-lingual transfer pathways"。
13	
14	**Llama 的 excess asymmetry**：conflict(+11.76) - XNLI(+5.97) = +5.79pp，可能有冲突特有成分，但 CI 重叠大，需统计检验。Qwen excess 为负(-0.77pp)。
15	
16	---
17	
18	## Steering 因果节点在 mid-layer [2026-05-22, steering_107 系列]
19	
20	**核心发现**：Llama-3.1-8B 上，probe weight 方向的因果效应具有强层特异性——只在 L13 (mid-layer) 有效，L18 (MLP peak) 和 L28 (final) 均无效。
21	
22	| 层 | 位置 | 最佳 Fisher p | 结论 |
23	|----|------|-------------|------|
24	| L28 | last | 0.31 | NEGATIVE |
25	| L28 | all | 0.37 | NEGATIVE |
26	| L18 | last | 0.45 | NEGATIVE |
27	| **L13** | **last** | **0.0009** | **SUCCESS** |
28	
29	**L13 双向因果效应**：
30	- α=-20: steering 36.0% vs control 17.6%, p=0.0009 (5 c→p)
31	- α=+5: steering 19.9% vs control 6.6%, p=0.002 (4 p→c)
32	
33	**机制解读**：mid-layer 是跨语言表征对齐发生的典型位置 (Conneau et al. 2020)。冲突信号的因果节点与对齐层重合，而非与检测准确率 peak 重合（L28 probe acc 最高但无因果性）。检测≠因果。
34	
35	**对论文影响**：Steering 从全面 NEGATIVE 逆转为 layer-specific SUCCESS，可作为论文亮点之一——probe 不仅检测到信号，该信号在特定层具有因果意义。
36	
37	---
38	
39	# Gemma-2-9B-IT 兼容性报告 (plan_102)
40	
41	## 模型结构
42	
43	| 属性 | 值 |
44	|------|-----|
45	| model_type | gemma2 |
46	| architecture | Gemma2ForCausalLM |
47	| num_hidden_layers | 42 |
48	| hidden_size | 3584 |
49	| num_attention_heads | 16 |
50	| num_key_value_heads | 8 (GQA) |
51	| head_dim | 256 |
52	| vocab_size | 256000 |
53	| torch_dtype | bfloat16 |
54	
55	## 各脚本兼容性
56	- verify_parametric_knowledge.py — ✅ 无需修改
57	- collect_activations.py — ✅ 无需修改（model.model.layers 同构）
58	- train_probe.py — ✅ 无需修改（无硬编码维度）
59	
60	## GPU 需求
61	- 模型加载（bfloat16）：~18GB VRAM
62	- 推荐：单卡 24GB+ 即可
63	
64	---
65	
66	## 踩坑记录
67	
68	### CUDA_VISIBLE_DEVICES 映射规则 [2026-05-22]
69	- `submit_on_allocated` / `submit_training_job` 会自动注入 `CUDA_VISIBLE_DEVICES` 映射物理 GPU，脚本内 `--gpu 0` = 分配的第一块卡
70	- **SSH 手动执行时**，`CUDA_VISIBLE_DEVICES` 直接对应物理 GPU 编号。分配 cuda:1 就必须写 `CUDA_VISIBLE_DEVICES=1`，不是 0
71	- **tmux 内层 `bash -c` 设置的 CUDA_VISIBLE_DEVICES 会覆盖外层值**，必须确保最内层命令的环境变量正确
72	
73	### Steering 脚本不写 W&B → cron 误判 [2026-05-22]
74	- steering_experiment.py 将结果输出到 JSON 文件，不记录 W&B metrics
75	- cron 监控依赖 W&B metrics 判断进程是否成功完成，导致正常完成的 steering 实验被误标 failed
76	- **影响**：steering_107_L13 (实际 SUCCESS)、steering_107_L18 (实际 NEGATIVE)、以及可能的后续 steering 实验都会触发此误判
77	- **处理方式**：收到 steering 实验的 failed 回调时，先读服务器上的结果 JSON 再下结论
78	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "f70f3790-730f-48e9-8378-c807a5aefb79",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/memory.md",
      "content": "# 关键研究发现\n\n## C2 不对称性非冲突特有 [2026-05-22, xnli_baseline_110]\n\n**核心发现**：~6pp ZH→EN > EN→ZH 不对称性在非冲突任务 XNLI 上同样存在，是模型的一般性跨语言属性，非冲突信号特有。\n\n| Model | XNLI asymmetry | Conflict asymmetry |\n|-------|---------------|-------------------|\n| Qwen | +6.72pp CI[2.36,11.73] ✓ | +5.95pp CI[-3.67,14.81] |\n| Llama | +5.97pp CI[0.92,11.33] ✓ | +11.76pp CI[4.29,19.57] ✓ |\n\n**推导**：英语主导预训练 → EN 表征空间更\"标准\" → ZH→EN 迁移天然更好。C2 需 reframe：从 \"conflict-specific asymmetry\" 改为 \"conflict signals share general cross-lingual transfer pathways\"。\n\n**Llama 的 excess asymmetry**：conflict(+11.76) - XNLI(+5.97) = +5.79pp，可能有冲突特有成分，但 CI 重叠大，需统计检验。Qwen excess 为负(-0.77pp)。\n\n---\n\n## Steering 因果节点在 mid-layer [2026-05-22, steering_107 系列]\n\n**核心发现**：Llama-3.1-8B 上，probe weight 方向的因果效应具有强层特异性——只在 L13 (mid-layer) 有效，L18 (MLP peak) 和 L28 (final) 均无效。\n\n| 层 | 位置 | 最佳 Fisher p | 结论 |\n|----|------|-------------|------|\n| L28 | last | 0.31 | NEGATIVE |\n| L28 | all | 0.37 | NEGATIVE |\n| L18 | last | 0.45 | NEGATIVE |\n| **L13** | **last** | **0.0009** | **SUCCESS** |\n\n**L13 双向因果效应**：\n- α=-20: steering 36.0% vs control 17.6%, p=0.0009 (5 c→p)\n- α=+5: steering 19.9% vs control 6.6%, p=0.002 (4 p→c)\n\n**机制解读**：mid-layer 是跨语言表征对齐发生的典型位置 (Conneau et al. 2020)。冲突信号的因果节点与对齐层重合，而非与检测准确率 peak 重合（L28 probe acc 最高但无因果性）。检测≠因果。\n\n**对论文影响**：Steering 从全面 NEGATIVE 逆转为 layer-specific SUCCESS，可作为论文亮点之一——probe 不仅检测到信号，该信号在特定层具有因果意义。\n\n---\n\n# Gemma-2-9B-IT 兼容性报告 (plan_102)\n\n## 模型结构\n\n| 属性 | 值 |\n|------|-----|\n| model_type | gemma2 |\n| architecture | Gemma2ForCausalLM |\n| num_hidden_layers | 42 |\n| hidden_size | 3584 |\n| num_attention_heads | 16 |\n| num_key_value_heads | 8 (GQA) |\n| head_dim | 256 |\n| vocab_size | 256000 |\n| torch_dtype | bfloat16 |\n\n## 各脚本兼容性\n- verify_parametric_knowledge.py — ✅ 无需修改\n- collect_activations.py — ✅ 无需修改（model.model.layers 同构）\n- train_probe.py — ✅ 无需修改（无硬编码维度）\n\n## GPU 需求\n- 模型加载（bfloat16）：~18GB VRAM\n- 推荐：单卡 24GB+ 即可\n\n---\n\n## 踩坑记录\n\n### CUDA_VISIBLE_DEVICES 映射规则 [2026-05-22]\n- `submit_on_allocated` / `submit_training_job` 会自动注入 `CUDA_VISIBLE_DEVICES` 映射物理 GPU，脚本内 `--gpu 0` = 分配的第一块卡\n- **SSH 手动执行时**，`CUDA_VISIBLE_DEVICES` 直接对应物理 GPU 编号。分配 cuda:1 就必须写 `CUDA_VISIBLE_DEVICES=1`，不是 0\n- **tmux 内层 `bash -c` 设置的 CUDA_VISIBLE_DEVICES 会覆盖外层值**，必须确保最内层命令的环境变量正确\n\n### Steering 脚本不写 W&B → cron 误判 [2026-05-22]\n- steering_experiment.py 将结果输出到 JSON 文件，不记录 W&B metrics\n- cron 监控依赖 W&B metrics 判断进程是否成功完成，导致正常完成的 steering 实验被误标 failed\n- **影响**：steering_107_L13 (实际 SUCCESS)、steering_107_L18 (实际 NEGATIVE)、以及可能的后续 steering 实验都会触发此误判\n- **处理方式**：收到 steering 实验的 failed 回调时，先读服务器上的结果 JSON 再下结论\n",
      "numLines": 78,
      "startLine": 1,
      "totalLines": 78
    }
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Let me also read the related work section to understand the full citation style, and check the roadmap for any recent updates on Gemma/DE results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "8a238931-bf00-42b7-87ff-f21bb318a409",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tqjxsn8Eaq7SqBjxjFNEDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 32879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_01V5SwJwiShSECZMHj6r2pxm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "9f699d4f-4bba-4f96-b810-f805ac5c99ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tqjxsn8Eaq7SqBjxjFNEDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 32879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T15:36:20.147Z_

<details><summary>↩ Tool result · `toolu_01V5SwJwiShSECZMHj6r2pxm`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Knowledge conflict detection.}
5	Research on how LLMs handle conflicting knowledge has developed along two axes: behavioral characterization and internal signal analysis.
6	\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent strategies when parametric and contextual knowledge disagree, ranging from faithful context-following to stubborn reliance on memorized answers.
7	\citet{xu2024knowledge} provided a systematic taxonomy of conflict types (intra-memory, context-memory, and inter-context) that has since guided experimental design in this area.
8	More recent work has moved beyond behavioral observation to probe model internals.
9	\citet{zhao2024analysing} demonstrated that residual stream representations carry linearly separable conflict signals in English, while \citet{boer2026probing} used probing classifiers to localize factual associations within model parameters.
10	\citet{pham2026where} investigated the mechanistic pathways through which intra-memory conflicts are processed, and \citet{li2025taming} proposed methods to mitigate conflict-induced errors.
11	These studies, however, operate exclusively in monolingual English settings.
12	Extending conflict probing to cross-lingual scenarios introduces confounds that require explicit control: translation quality can degrade the conflict signal, token overlap between languages can provide spurious shortcuts, and general cross-lingual transfer properties can be mistaken for conflict-specific phenomena.
13	We build on the residual stream probing approach of \citet{zhao2024analysing} and extend it to cross-lingual settings with a confound exclusion pipeline that addresses each of these concerns.
14	
15	\paragraph{Cross-lingual representations in multilingual models.}
16	A consistent finding across multilingual model analyses is that intermediate layers develop language-independent representations.
17	\citet{wu2020emerging} showed that cross-lingual structure emerges in pretrained models without explicit alignment objectives, and \citet{muller2021first} found that multilingual BERT first aligns representations across languages in middle layers before making task predictions.
18	For decoder-only LLMs, \citet{wendler2024llamas} provided evidence that Llama models process non-English inputs through an English-centric latent space, with internal representations converging toward English regardless of the input language.
19	\citet{kargaran2024mexa} quantified this English-centric bias and showed that cross-lingual alignment quality varies substantially across language pairs and model layers.
20	This body of work predicts two patterns that we observe empirically.
21	First, the success of mid-layer steering (L13, 41\% depth) aligns with the finding that language-independent encoding peaks at intermediate layers.
22	Second, the ZH$\to$EN transfer advantage in our probing experiments is consistent with the English-centric structure documented by \citet{wendler2024llamas} and \citet{kargaran2024mexa}: Chinese representations map more readily onto the English space than the reverse.
23	Several studies have documented behavioral consequences of this representational structure.
24	\citet{wang2025lost} found systematic cross-lingual factual inconsistencies in transformer language models, \citet{zhao2026when} constructed the CLEAR benchmark showing that conflict resolution patterns differ across languages, and \citet{ifergan2024beneath} and \citet{xing2024evaluating} evaluated the consistency of cross-lingual knowledge sharing.
25	Our work complements these behavioral studies by providing a mechanistic account of why such asymmetries arise.
26	
27	\paragraph{Representation steering and causal intervention.}
28	Probing establishes correlation between representations and task-relevant information, but causal influence requires intervention.
29	\citet{li2023iti} introduced Inference-Time Intervention, which adds learned bias vectors at specific attention heads to steer model outputs toward truthfulness.
30	\citet{zou2023representation} generalized this idea through Representation Engineering, which extracts and manipulates concept-level directions in activation space.
31	In the knowledge conflict domain, \citet{zhao2025steering} applied SAE-based steering (SpARE) to shift conflict resolution behavior in monolingual settings.
32	These successes, however, are not universal.
33	\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, which raises the question of when detectability implies actionability.
34	\citet{feng2026finegrained} proposed fine-grained activation steering to improve intervention precision by targeting specific layers and positions.
35	Our results contribute to this discussion by identifying layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, even though the late layer achieves higher probe accuracy.
36	This dissociation between the probing peak and the causal locus suggests that conflict resolution occurs upstream of where the outcome becomes linearly readable.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "b47974a0-3af3-4450-bdbb-d02b7c731a43",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Knowledge conflict detection.}\nResearch on how LLMs handle conflicting knowledge has developed along two axes: behavioral characterization and internal signal analysis.\n\\citet{xie2024adaptive} introduced ConflictQA and showed that models exhibit context-dependent strategies when parametric and contextual knowledge disagree, ranging from faithful context-following to stubborn reliance on memorized answers.\n\\citet{xu2024knowledge} provided a systematic taxonomy of conflict types (intra-memory, context-memory, and inter-context) that has since guided experimental design in this area.\nMore recent work has moved beyond behavioral observation to probe model internals.\n\\citet{zhao2024analysing} demonstrated that residual stream representations carry linearly separable conflict signals in English, while \\citet{boer2026probing} used probing classifiers to localize factual associations within model parameters.\n\\citet{pham2026where} investigated the mechanistic pathways through which intra-memory conflicts are processed, and \\citet{li2025taming} proposed methods to mitigate conflict-induced errors.\nThese studies, however, operate exclusively in monolingual English settings.\nExtending conflict probing to cross-lingual scenarios introduces confounds that require explicit control: translation quality can degrade the conflict signal, token overlap between languages can provide spurious shortcuts, and general cross-lingual transfer properties can be mistaken for conflict-specific phenomena.\nWe build on the residual stream probing approach of \\citet{zhao2024analysing} and extend it to cross-lingual settings with a confound exclusion pipeline that addresses each of these concerns.\n\n\\paragraph{Cross-lingual representations in multilingual models.}\nA consistent finding across multilingual model analyses is that intermediate layers develop language-independent representations.\n\\citet{wu2020emerging} showed that cross-lingual structure emerges in pretrained models without explicit alignment objectives, and \\citet{muller2021first} found that multilingual BERT first aligns representations across languages in middle layers before making task predictions.\nFor decoder-only LLMs, \\citet{wendler2024llamas} provided evidence that Llama models process non-English inputs through an English-centric latent space, with internal representations converging toward English regardless of the input language.\n\\citet{kargaran2024mexa} quantified this English-centric bias and showed that cross-lingual alignment quality varies substantially across language pairs and model layers.\nThis body of work predicts two patterns that we observe empirically.\nFirst, the success of mid-layer steering (L13, 41\\% depth) aligns with the finding that language-independent encoding peaks at intermediate layers.\nSecond, the ZH$\\to$EN transfer advantage in our probing experiments is consistent with the English-centric structure documented by \\citet{wendler2024llamas} and \\citet{kargaran2024mexa}: Chinese representations map more readily onto the English space than the reverse.\nSeveral studies have documented behavioral consequences of this representational structure.\n\\citet{wang2025lost} found systematic cross-lingual factual inconsistencies in transformer language models, \\citet{zhao2026when} constructed the CLEAR benchmark showing that conflict resolution patterns differ across languages, and \\citet{ifergan2024beneath} and \\citet{xing2024evaluating} evaluated the consistency of cross-lingual knowledge sharing.\nOur work complements these behavioral studies by providing a mechanistic account of why such asymmetries arise.\n\n\\paragraph{Representation steering and causal intervention.}\nProbing establishes correlation between representations and task-relevant information, but causal influence requires intervention.\n\\citet{li2023iti} introduced Inference-Time Intervention, which adds learned bias vectors at specific attention heads to steer model outputs toward truthfulness.\n\\citet{zou2023representation} generalized this idea through Representation Engineering, which extracts and manipulates concept-level directions in activation space.\nIn the knowledge conflict domain, \\citet{zhao2025steering} applied SAE-based steering (SpARE) to shift conflict resolution behavior in monolingual settings.\nThese successes, however, are not universal.\n\\citet{basu2026interpretability} showed that near-perfect probe accuracy on clinical NLP tasks failed to translate into effective steering, which raises the question of when detectability implies actionability.\n\\citet{feng2026finegrained} proposed fine-grained activation steering to improve intervention precision by targeting specific layers and positions.\nOur results contribute to this discussion by identifying layer selection as a critical variable: mid-layer intervention succeeds where late-layer intervention fails, even though the late layer achieves higher probe accuracy.\nThis dissociation between the probing peak and the causal locus suggests that conflict resolution occurs upstream of where the outcome becomes linearly readable.\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YLDFeL8XwZKs9yeuyEFbAg`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "0b91431d-7f52-45a0-adb1-3180d9ff811c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tqjxsn8Eaq7SqBjxjFNEDT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2085,
      "cache_read_input_tokens": 32879,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2085
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-22T15:36:20.228Z_

<details><summary>↩ Tool result · `toolu_01YLDFeL8XwZKs9yeuyEFbAg`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "c4eca043-fbcf-4c45-8719-b3acb0b52245",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WJjTeNHS8fpCKQ7dJzicCw`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "ROADMAP.md",
  "max_chars": 6000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "e0ba173e-1d5d-405a-8dbc-a2ce0601042b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No3d1hGziwnidDdti4B7WG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 34964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1770
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-22T15:36:23.777Z_

<details><summary>↩ Tool result · `toolu_01WJjTeNHS8fpCKQ7dJzicCw`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 12:56 UTC | 更新原因: EMNLP 2026 DDL May 25 确认, Paper Agent 启动\\n\\n## 核心方向\\n跨语言知识冲突信号的机制解释。详见 paper_framing.md。\\n\\n## 当前阶段\\n**EMNLP 2026 ARR 冲刺** — DDL **2026-05-25**（剩余3天）。论文写作已启动。\\n\\n### Claim 状态\\n- **C1 detectability** ✅ Llama 77.1%, Qwen 75.3%\\n- **C2 asymmetry** ✅ Reframed: 通用跨语言属性（XNLI 对照）\\n- **C3 non-linearity** ❌ CI含零 (D012)，降为 observation\\n- **Steering v1** ❌ L28/last NEGATIVE\\n- **Steering v2c** ❌ L28/all NEGATIVE\\n- **Steering v2a/v2b** ⏳ L13/L18 ~70%, ETA <1h\\n- **Steering Qwen** ⏳ 重启中 (L23)\\n\\n### 并行轨道\\n**写作轨道**: Paper Agent 已激活，Full Draft 模式\\n**实验轨道**: Steering v2 + Gemma + DE + Bootstrap 继续跑，完成即补入论文\\n\\n### GPU 状态\\n- cuda:0: Qwen Steering L23（重启中）\\n- cuda:1: Steering v2a L13 (~70%)\\n- cuda:2: Steering v2b L18 (~70%)\\n- cuda:3: DE translate test 集\\n\\n### 紧急任务\\n- [ ] Paper Agent: writing_plan.yaml 审批\\n- [ ] Steering v2a/v2b 结果判定 — Llama 最后机会\\n- [ ] Qwen Steering L23 启动确认\\n- [ ] Gemma/DE/Bootstrap — 完成即通知 Paper Agent 补入\\n\\n## GPU 预算\\n本项目分配: cuda:0,1,2,3 (westd-41302)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-22 | Steering L13 SUCCESS (p=0.0009/0.002)! 因果节点在 mid-l | steering_107_L13, steering_107, steering_107_L18, steering_107_L28_all |\\n| D013 | 2026-05-22 | DDL确认: EMNLP 2026 ARR May 25 (3天), 立即启动论文写作 | mvp_probe_llama_v1, mvp_probe_v1, xnli_baseline_110, steering_107 |\\n| D012 | 2026-05-22 | D009 撤回：C3 non-linearity 降为 \\\"trend only\\\"，双模型 boots | xnli_baseline_110, mvp_002 |\\n| D011 | 2026-05-22 | Steering v1 NEGATIVE; 启动诊断性变体轮（3配置并行）后再判定 Track 3  | steering_107 |\\n| D010 | 2026-05-22 | Steering (plan_107) 升为最高优先级；C3 需统计加固但不作为唯一卖点 | xnli_baseline_110, mvp_002 |\\n| D009 | 2026-05-22 | C3 confirmed conflict-specific：XNLI MLP 对照证明非线性 en | xnli_baseline_110, mvp_002 |\\n| D008 | 2026-05-22 | C2 reframe：不对称性非冲突特异性，改为\\\"冲突信号继承模型一般跨语言迁移偏置\\\" | xnli_baseline_110 |\\n| D007 | 2026-05-22 | Dream 审稿结果处理：新增 3 个 P0 实验（非冲突基线、bootstrap 升级、EN↔DE | dream_20260522T023801 |\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\n\\n\", \"total_chars\": 2165, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "575eef71-3a8d-4d8b-a346-0521354b6403",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\\\", \\\"content\\\": \\\"# clkc_mech_interp — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-22 12:56 UTC | 更新原因: EMNLP 2026 DDL May 25 确认, Paper Agent 启动\\\\n\\\\n## 核心方向\\\\n跨语言知识冲突信号的机制解释。详见 paper_framing.md。\\\\n\\\\n## 当前阶段\\\\n**EMNLP 2026 ARR 冲刺** — DDL **2026-05-25**（剩余3天）。论文写作已启动。\\\\n\\\\n### Claim 状态\\\\n- **C1 detectability** ✅ Llama 77.1%, Qwen 75.3%\\\\n- **C2 asymmetry** ✅ Reframed: 通用跨语言属性（XNLI 对照）\\\\n- **C3 non-linearity** ❌ CI含零 (D012)，降为 observation\\\\n- **Steering v1** ❌ L28/last NEGATIVE\\\\n- **Steering v2c** ❌ L28/all NEGATIVE\\\\n- **Steering v2a/v2b** ⏳ L13/L18 ~70%, ETA <1h\\\\n- **Steering Qwen** ⏳ 重启中 (L23)\\\\n\\\\n### 并行轨道\\\\n**写作轨道**: Paper Agent 已激活，Full Draft 模式\\\\n**实验轨道**: Steering v2 + Gemma + DE + Bootstrap 继续跑，完成即补入论文\\\\n\\\\n### GPU 状态\\\\n- cuda:0: Qwen Steering L23（重启中）\\\\n- cuda:1: Steering v2a L13 (~70%)\\\\n- cuda:2: Steering v2b L18 (~70%)\\\\n- cuda:3: DE translate test 集\\\\n\\\\n### 紧急任务\\\\n- [ ] Paper Agent: writing_plan.yaml 审批\\\\n- [ ] Steering v2a/v2b 结果判定 — Llama 最后机会\\\\n- [ ] Qwen Steering L23 启动确认\\\\n- [ ] Gemma/DE/Bootstrap — 完成即通知 Paper Agent 补入\\\\n\\\\n## GPU 预算\\\\n本项目分配: cuda:0,1,2,3 (westd-41302)\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D014 | 2026-05-22 | Steering L13 SUCCESS (p=0.0009/0.002)! 因果节点在 mid-l | steering_107_L13, steering_107, steering_107_L18, steering_107_L28_all |\\\\n| D013 | 2026-05-22 | DDL确认: EMNLP 2026 ARR May 25 (3天), 立即启动论文写作 | mvp_probe_llama_v1, mvp_probe_v1, xnli_baseline_110, steering_107 |\\\\n| D012 | 2026-05-22 | D009 撤回：C3 non-linearity 降为 \\\\\\\"trend only\\\\\\\"，双模型 boots | xnli_baseline_110, mvp_002 |\\\\n| D011 | 2026-05-22 | Steering v1 NEGATIVE; 启动诊断性变体轮（3配置并行）后再判定 Track 3  | steering_107 |\\\\n| D010 | 2026-05-22 | Steering (plan_107) 升为最高优先级；C3 需统计加固但不作为唯一卖点 | xnli_baseline_110, mvp_002 |\\\\n| D009 | 2026-05-22 | C3 confirmed conflict-specific：XNLI MLP 对照证明非线性 en | xnli_baseline_110, mvp_002 |\\\\n| D008 | 2026-05-22 | C2 reframe：不对称性非冲突特异性，改为\\\\\\\"冲突信号继承模型一般跨语言迁移偏置\\\\\\\" | xnli_baseline_110 |\\\\n| D007 | 2026-05-22 | Dream 审稿结果处理：新增 3 个 P0 实验（非冲突基线、bootstrap 升级、EN↔DE | dream_20260522T023801 |\\\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\\\n\\\\n\\\", \\\"total_chars\\\": 2165, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/ROADMAP.md\", \"content\": \"# clkc_mech_interp — Research Dashboard\\n\\n> 最后更新: 2026-05-22 12:56 UTC | 更新原因: EMNLP 2026 DDL May 25 确认, Paper Agent 启动\\n\\n## 核心方向\\n跨语言知识冲突信号的机制解释。详见 paper_framing.md。\\n\\n## 当前阶段\\n**EMNLP 2026 ARR 冲刺** — DDL **2026-05-25**（剩余3天）。论文写作已启动。\\n\\n### Claim 状态\\n- **C1 detectability** ✅ Llama 77.1%, Qwen 75.3%\\n- **C2 asymmetry** ✅ Reframed: 通用跨语言属性（XNLI 对照）\\n- **C3 non-linearity** ❌ CI含零 (D012)，降为 observation\\n- **Steering v1** ❌ L28/last NEGATIVE\\n- **Steering v2c** ❌ L28/all NEGATIVE\\n- **Steering v2a/v2b** ⏳ L13/L18 ~70%, ETA <1h\\n- **Steering Qwen** ⏳ 重启中 (L23)\\n\\n### 并行轨道\\n**写作轨道**: Paper Agent 已激活，Full Draft 模式\\n**实验轨道**: Steering v2 + Gemma + DE + Bootstrap 继续跑，完成即补入论文\\n\\n### GPU 状态\\n- cuda:0: Qwen Steering L23（重启中）\\n- cuda:1: Steering v2a L13 (~70%)\\n- cuda:2: Steering v2b L18 (~70%)\\n- cuda:3: DE translate test 集\\n\\n### 紧急任务\\n- [ ] Paper Agent: writing_plan.yaml 审批\\n- [ ] Steering v2a/v2b 结果判定 — Llama 最后机会\\n- [ ] Qwen Steering L23 启动确认\\n- [ ] Gemma/DE/Bootstrap — 完成即通知 Paper Agent 补入\\n\\n## GPU 预算\\n本项目分配: cuda:0,1,2,3 (westd-41302)\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D014 | 2026-05-22 | Steering L13 SUCCESS (p=0.0009/0.002)! 因果节点在 mid-l | steering_107_L13, steering_107, steering_107_L18, steering_107_L28_all |\\n| D013 | 2026-05-22 | DDL确认: EMNLP 2026 ARR May 25 (3天), 立即启动论文写作 | mvp_probe_llama_v1, mvp_probe_v1, xnli_baseline_110, steering_107 |\\n| D012 | 2026-05-22 | D009 撤回：C3 non-linearity 降为 \\\"trend only\\\"，双模型 boots | xnli_baseline_110, mvp_002 |\\n| D011 | 2026-05-22 | Steering v1 NEGATIVE; 启动诊断性变体轮（3配置并行）后再判定 Track 3  | steering_107 |\\n| D010 | 2026-05-22 | Steering (plan_107) 升为最高优先级；C3 需统计加固但不作为唯一卖点 | xnli_baseline_110, mvp_002 |\\n| D009 | 2026-05-22 | C3 confirmed conflict-specific：XNLI MLP 对照证明非线性 en | xnli_baseline_110, mvp_002 |\\n| D008 | 2026-05-22 | C2 reframe：不对称性非冲突特异性，改为\\\"冲突信号继承模型一般跨语言迁移偏置\\\" | xnli_baseline_110 |\\n| D007 | 2026-05-22 | Dream 审稿结果处理：新增 3 个 P0 实验（非冲突基线、bootstrap 升级、EN↔DE | dream_20260522T023801 |\\n| D006 | 2026-05-22 | COMET 0.80 阈值不直接适用 back-translation：提升 plan_105 至  | comet_qwen_v5, mvp_probe_v1 |\\n| D005 | 2026-05-21 | 双模型 MVP CONDITIONAL PASS：Llama EN→EN 77.6% + Qwen  | mvp_probe_llama_v1, mvp_probe_v1 |\\n\\n\", \"total_chars\": 2165, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_012CPU13qnMmCWbZkmcPFhj8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "5281b48f-9105-4b2a-bfc0-b2e87d85373c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01No3d1hGziwnidDdti4B7WG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1770,
      "cache_read_input_tokens": 34964,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1770
      },
      "output_tokens": 66,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-22T15:36:23.846Z_

<details><summary>↩ Tool result · `toolu_012CPU13qnMmCWbZkmcPFhj8`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}
20	
21	\author{Anonymous ACL submission}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	% [PLACEHOLDER — Step 4]
28	\end{abstract}
29	
30	% [PLACEHOLDER — introduction]
31	
32	% [PLACEHOLDER — related_work]
33	
34	\input{method}
35	
36	\input{experiments}
37	
38	% [PLACEHOLDER — discussion]
39	
40	% [PLACEHOLDER — conclusion]
41	
42	% [PLACEHOLDER — limitations]
43	
44	\bibliographystyle{acl_natbib}
45	\bibliography{references}
46	
47	\end{document}
48	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "d69cd40e-f962-4406-bb17-2c041afa39e5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\title{Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries from General Multilingual Representations}\n\n\\author{Anonymous ACL submission}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\n% [PLACEHOLDER — Step 4]\n\\end{abstract}\n\n% [PLACEHOLDER — introduction]\n\n% [PLACEHOLDER — related_work]\n\n\\input{method}\n\n\\input{experiments}\n\n% [PLACEHOLDER — discussion]\n\n% [PLACEHOLDER — conclusion]\n\n% [PLACEHOLDER — limitations]\n\n\\bibliographystyle{acl_natbib}\n\\bibliography{references}\n\n\\end{document}\n",
      "numLines": 48,
      "startLine": 1,
      "totalLines": 48
    }
  }
}
```

</details>

---

### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now let me also read the paper_framing.md and writing_plan.yaml for more context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "7e1adf9a-b6ec-4ada-91f5-26dd651687f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWiUmPYsMru4mEWKoTDJ2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 36734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W5WgxGxgxfR4YdVbrMNKZA`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "paper_framing.md",
  "max_chars": 6000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "f8e8a66d-c366-44e5-bba9-2f28e366774a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWiUmPYsMru4mEWKoTDJ2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 36734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-22T15:36:27.979Z_

<details><summary>↩ Tool result · `toolu_01W5WgxGxgxfR4YdVbrMNKZA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: EMNLP 2026 via ARR (DDL 2026-05-25, 3天)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致。**关键发现（plan_110 XNLI 基线）**：该不对称性并非冲突特有——非冲突语义任务 (XNLI) 展现几乎相同幅度的迁移不对称性（Qwen +6.72pp, Llama +5.97pp）。这说明冲突信号**编码在模型的通用跨语言表征空间中**，继承其方向性偏置，而非独立的专用机制。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**机制分析驱动**（非 \\\"发现新现象\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？与一般跨语言语义表征的关系是什么？\\n3. **Our answer**: 冲突信号可线性检测且跨架构一致，但其跨语言迁移模式（方向不对称性）**与一般语义任务 (XNLI) 无异**——冲突检测 piggyback 在模型已有的跨语言对齐结构上，而非专用子空间。通过层结构分析和因果干预验证这一机制。\\n4. **Methodological contribution**: 严格的 confound exclusion pipeline (COMET ablation + token overlap) + 非冲突基线对照，为跨语言 probing 研究树立方法论标准\\n\\n**Secondary framing**: 跨语言 probing 中方向性偏置的普遍性——English-dominant 模型的固有属性，影响所有跨语言迁移研究的结论解读\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP + plan_110 证据倾向**:\\nZH→EN 迁移优势（~7pp）在冲突和 XNLI 任务中均存在且幅度一致，说明这是模型跨语言表征的固有属性（H1 部分支持：英语锚点存在，但非冲突特有）。冲突信号编码在通用跨语言空间中。非线性成分（MLP EN→ZH gains）是否冲突特有待 XNLI 上的 MLP 对照验证。\\n\\n## Core Claims\\n\\n### Claim 1: Cross-lingual conflict detectability\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\n**Evidence needed**:\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\n- Permutation test p < 0.001 ✅ (all directions)\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\n**Status**: MVP 已验证 ✅\\n\\n### Claim 2: Cross-lingual transfer asymmetry as general model property [REFRAMED per D008]\\n**Statement**: 跨语言探针迁移呈方向一致的不对称（ZH→EN > EN→ZH ~7pp），但 **XNLI 非冲突基线展现几乎相同幅度的不对称性**（Qwen +6.72pp, Llama +5.97pp），说明这是 English-dominant 模型的一般跨语言迁移属性，非冲突特有。冲突信号继承了模型的通用跨语言表征结构。\\n**Evidence**:\\n- 冲突不对称性: Llama +7.22pp CI[1.1,13.6], Qwen +7.18pp CI[-1.2,13.4] ✅\\n- XNLI 不对称性: Llama +5.97pp CI[0.92,11.33], Qwen +6.72pp CI[2.36,11.73] ✅\\n- 两者量级无显著差异，CI 大幅重叠 ✅\\n- Token overlap 排除 ✅ | COMET confound 排除 ✅\\n- ≥1 additional architecture 验证 ❌ (plan_102 Gemma 进行中)\\n**Status**: XNLI 基线已完成，C2 reframed ✅⚠️ (待第三模型确认)\\n\\n### Claim 3: Non-linear encoding trend [DEAD — D012 双模型 CI 含零]\\n**Statement**: ~~冲突信号包含非线性成分~~ → 降为 supporting observation，不作为独立 claim。\\n**Evidence**:\\n- 冲突 MLP Δ (EN→ZH): Qwen +3.84pp CI[-3.57,+11.31] 含零 ❌; Llama +5.21pp CI[-2.21,+12.87] 含零 ❌\\n- XNLI MLP Δ (EN→ZH): Qwen -2.0pp, Llama -0.5pp — 方向对比成立但不显著\\n- **双模型 bootstrap 均不显著**，方向一致（冲突正、XNLI 负）可作为 suggestive trend 在 discussion 中提及\\n**Status**: ❌ 不作为论文 claim。Discussion 中作为 observation 报告。\\n\\n### Claim 4: Layer-wise conflict signal structure\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\n**Evidence needed**:\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\n- 与 \\\"Lost in Multilinguality\\\" 的 language transition 层对比 ❌\\n**Status**: 未验证 ❌\\n\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\n**Evidence needed**:\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\n- LangFIR random-token filtering 控制 ❌\\n- Cross-lingual feature Jaccard 分析 ❌\\n**Status**: 未开始 ❌\\n\\n### Claim 6: Causal evidence via representation steering (Track 3) [v1 NEGATIVE — D011 diagnostic round]\\n**Statement**: 探针权重方向具有因果意义——沿此方向 steering 可改变模型冲突解决行为。\\n**Evidence needed**:\\n- Probe-weight steering 显著改变 p↔c flip rate (vs random control) ✅ (L13)\\n- ≥1 layer/position 配置 Fisher p < 0.05 ✅ (α=+5 p=0.002, α=-20 p=0.0009)\\n**L13 result (D014, SUCCESS)**: Llama L13, last-token — α=+5 p=0.002 (19.9% vs 6.6%), α=-20 p=0.0009 (36.0% vs 17.6%)。方向性正确：正α→p→c, 负α→c→p。\\n**L28/L18/L28-all NEGATIVE**: 因果节点在 mid-layer (L13, ~40% depth), NOT probe peak (L28, ~88%)。\\n**核心机制发现**: Detection ≠ Decision — 模型在 late-layer 编码可检测信号，但因果决策在 mid-layer 形成。\\n- 待 Qwen L13 跨模型验证 → C6 fully supported\\n**Status**: Llama L13 ✅ SUCCESS, Qwen L13 验证中 ⏳\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Translation quality confound [RESOLVED ✅]\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\n\\n### RC2: Token overlap confound [RESOLVED ✅]\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\n\\n### RC3: Model coverage insufficient [HIGH]\\n**Concern**: 只有 2 个模型，无法声称 \\\"架构无关\\\"\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\n**Experiment**: P0 — additional model verification\\n\\n### RC4: Dataset size and diversity [MEDIUM]\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\n\\n### RC5: Linear probe expressiveness [LOW]\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\n**Experi\\n\\n... [截断: 省略 3218 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 9218, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "89a2daa2-5454-4f46-a9b4-dc85384a873e",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — clkc_mech_interp\\\\n\\\\n> 最后更新: 2026-05-22 | 目标: EMNLP 2026 via ARR (DDL 2026-05-25, 3天)\\\\n\\\\n## Core Insight\\\\n\\\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致。**关键发现（plan_110 XNLI 基线）**：该不对称性并非冲突特有——非冲突语义任务 (XNLI) 展现几乎相同幅度的迁移不对称性（Qwen +6.72pp, Llama +5.97pp）。这说明冲突信号**编码在模型的通用跨语言表征空间中**，继承其方向性偏置，而非独立的专用机制。\\\\n\\\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\\\n\\\\n## Narrative Structure\\\\n\\\\n**机制分析驱动**（非 \\\\\\\"发现新现象\\\\\\\"）：\\\\n\\\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 决定跨语言冲突解决，但未提供机制解释\\\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？与一般跨语言语义表征的关系是什么？\\\\n3. **Our answer**: 冲突信号可线性检测且跨架构一致，但其跨语言迁移模式（方向不对称性）**与一般语义任务 (XNLI) 无异**——冲突检测 piggyback 在模型已有的跨语言对齐结构上，而非专用子空间。通过层结构分析和因果干预验证这一机制。\\\\n4. **Methodological contribution**: 严格的 confound exclusion pipeline (COMET ablation + token overlap) + 非冲突基线对照，为跨语言 probing 研究树立方法论标准\\\\n\\\\n**Secondary framing**: 跨语言 probing 中方向性偏置的普遍性——English-dominant 模型的固有属性，影响所有跨语言迁移研究的结论解读\\\\n\\\\n## Competing Hypotheses (pre-registered)\\\\n\\\\n**H1 — English-anchored universal detection**:\\\\n冲突检测信号本身是 language-independent 的（\\\\\\\"是否存在冲突\\\\\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\\\n\\\\n**H2 — Language-pair-specific encoding**:\\\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\\\n\\\\n**MVP + plan_110 证据倾向**:\\\\nZH→EN 迁移优势（~7pp）在冲突和 XNLI 任务中均存在且幅度一致，说明这是模型跨语言表征的固有属性（H1 部分支持：英语锚点存在，但非冲突特有）。冲突信号编码在通用跨语言空间中。非线性成分（MLP EN→ZH gains）是否冲突特有待 XNLI 上的 MLP 对照验证。\\\\n\\\\n## Core Claims\\\\n\\\\n### Claim 1: Cross-lingual conflict detectability\\\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\\\n**Evidence needed**:\\\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\\\n- Permutation test p < 0.001 ✅ (all directions)\\\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\\\n**Status**: MVP 已验证 ✅\\\\n\\\\n### Claim 2: Cross-lingual transfer asymmetry as general model property [REFRAMED per D008]\\\\n**Statement**: 跨语言探针迁移呈方向一致的不对称（ZH→EN > EN→ZH ~7pp），但 **XNLI 非冲突基线展现几乎相同幅度的不对称性**（Qwen +6.72pp, Llama +5.97pp），说明这是 English-dominant 模型的一般跨语言迁移属性，非冲突特有。冲突信号继承了模型的通用跨语言表征结构。\\\\n**Evidence**:\\\\n- 冲突不对称性: Llama +7.22pp CI[1.1,13.6], Qwen +7.18pp CI[-1.2,13.4] ✅\\\\n- XNLI 不对称性: Llama +5.97pp CI[0.92,11.33], Qwen +6.72pp CI[2.36,11.73] ✅\\\\n- 两者量级无显著差异，CI 大幅重叠 ✅\\\\n- Token overlap 排除 ✅ | COMET confound 排除 ✅\\\\n- ≥1 additional architecture 验证 ❌ (plan_102 Gemma 进行中)\\\\n**Status**: XNLI 基线已完成，C2 reframed ✅⚠️ (待第三模型确认)\\\\n\\\\n### Claim 3: Non-linear encoding trend [DEAD — D012 双模型 CI 含零]\\\\n**Statement**: ~~冲突信号包含非线性成分~~ → 降为 supporting observation，不作为独立 claim。\\\\n**Evidence**:\\\\n- 冲突 MLP Δ (EN→ZH): Qwen +3.84pp CI[-3.57,+11.31] 含零 ❌; Llama +5.21pp CI[-2.21,+12.87] 含零 ❌\\\\n- XNLI MLP Δ (EN→ZH): Qwen -2.0pp, Llama -0.5pp — 方向对比成立但不显著\\\\n- **双模型 bootstrap 均不显著**，方向一致（冲突正、XNLI 负）可作为 suggestive trend 在 discussion 中提及\\\\n**Status**: ❌ 不作为论文 claim。Discussion 中作为 observation 报告。\\\\n\\\\n### Claim 4: Layer-wise conflict signal structure\\\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\\\n**Evidence needed**:\\\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\\\n- 与 \\\\\\\"Lost in Multilinguality\\\\\\\" 的 language transition 层对比 ❌\\\\n**Status**: 未验证 ❌\\\\n\\\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\\\n**Evidence needed**:\\\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\\\n- LangFIR random-token filtering 控制 ❌\\\\n- Cross-lingual feature Jaccard 分析 ❌\\\\n**Status**: 未开始 ❌\\\\n\\\\n### Claim 6: Causal evidence via representation steering (Track 3) [v1 NEGATIVE — D011 diagnostic round]\\\\n**Statement**: 探针权重方向具有因果意义——沿此方向 steering 可改变模型冲突解决行为。\\\\n**Evidence needed**:\\\\n- Probe-weight steering 显著改变 p↔c flip rate (vs random control) ✅ (L13)\\\\n- ≥1 layer/position 配置 Fisher p < 0.05 ✅ (α=+5 p=0.002, α=-20 p=0.0009)\\\\n**L13 result (D014, SUCCESS)**: Llama L13, last-token — α=+5 p=0.002 (19.9% vs 6.6%), α=-20 p=0.0009 (36.0% vs 17.6%)。方向性正确：正α→p→c, 负α→c→p。\\\\n**L28/L18/L28-all NEGATIVE**: 因果节点在 mid-layer (L13, ~40% depth), NOT probe peak (L28, ~88%)。\\\\n**核心机制发现**: Detection ≠ Decision — 模型在 late-layer 编码可检测信号，但因果决策在 mid-layer 形成。\\\\n- 待 Qwen L13 跨模型验证 → C6 fully supported\\\\n**Status**: Llama L13 ✅ SUCCESS, Qwen L13 验证中 ⏳\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Translation quality confound [RESOLVED ✅]\\\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\\\n\\\\n### RC2: Token overlap confound [RESOLVED ✅]\\\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\\\n\\\\n### RC3: Model coverage insufficient [HIGH]\\\\n**Concern**: 只有 2 个模型，无法声称 \\\\\\\"架构无关\\\\\\\"\\\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\\\n**Experiment**: P0 — additional model verification\\\\n\\\\n### RC4: Dataset size and diversity [MEDIUM]\\\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\\\n\\\\n### RC5: Linear probe expressiveness [LOW]\\\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\\\n**Experi\\\\n\\\\n... [截断: 省略 3218 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 9218, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/paper_framing.md\", \"content\": \"# Paper Framing — clkc_mech_interp\\n\\n> 最后更新: 2026-05-22 | 目标: EMNLP 2026 via ARR (DDL 2026-05-25, 3天)\\n\\n## Core Insight\\n\\n多语言 LLM 中，跨语言知识冲突的检测信号可在残差流中被线性探针检测，且跨语言迁移呈现**方向性不对称**（ZH→EN >> EN→ZH ~7.2pp），该不对称性跨架构高度一致。**关键发现（plan_110 XNLI 基线）**：该不对称性并非冲突特有——非冲突语义任务 (XNLI) 展现几乎相同幅度的迁移不对称性（Qwen +6.72pp, Llama +5.97pp）。这说明冲突信号**编码在模型的通用跨语言表征空间中**，继承其方向性偏置，而非独立的专用机制。\\n\\n**注意**: CLEAR 的发现是 task-dependent 的——entity-centric factual conflicts 由 linguistic affinity 主导，reasoning-intensive tasks 由 resource abundance 主导。我们使用 ConflictQA（entity-centric），引用 CLEAR 时必须限定为 entity-centric 场景。\\n\\n## Narrative Structure\\n\\n**机制分析驱动**（非 \\\"发现新现象\\\"）：\\n\\n1. **Phenomenon**: CLEAR 发现在 entity-centric factual conflicts 中，linguistic affinity 决定跨语言冲突解决，但未提供机制解释\\n2. **Mechanistic question**: 冲突信号在模型内部如何编码？与一般跨语言语义表征的关系是什么？\\n3. **Our answer**: 冲突信号可线性检测且跨架构一致，但其跨语言迁移模式（方向不对称性）**与一般语义任务 (XNLI) 无异**——冲突检测 piggyback 在模型已有的跨语言对齐结构上，而非专用子空间。通过层结构分析和因果干预验证这一机制。\\n4. **Methodological contribution**: 严格的 confound exclusion pipeline (COMET ablation + token overlap) + 非冲突基线对照，为跨语言 probing 研究树立方法论标准\\n\\n**Secondary framing**: 跨语言 probing 中方向性偏置的普遍性——English-dominant 模型的固有属性，影响所有跨语言迁移研究的结论解读\\n\\n## Competing Hypotheses (pre-registered)\\n\\n**H1 — English-anchored universal detection**:\\n冲突检测信号本身是 language-independent 的（\\\"是否存在冲突\\\" 是语言无关判断），编码在 mid-layer 共享表征空间中。final-layer language transition 引入 similarity-dependent 干扰，影响 resolution 但不影响 detection。\\n- 预测: mid-layer conflict feature 跨语言 Jaccard >> late-layer Jaccard (paired permutation test p < 0.05)\\n- 预测: 英语探针跨语言迁移更强（英语作为训练数据主导语言，表征空间以英语为锚点）\\n\\n**H2 — Language-pair-specific encoding**:\\n冲突特征从 mid-layer 起即为 language-pair-specific 的，linguistic distance 直接编码在冲突表征中。\\n- 预测: mid-layer 和 late-layer Jaccard 无显著差异，或 mid < late\\n- 预测: 探针迁移准确率与语言对 typological distance 强相关\\n\\n**MVP + plan_110 证据倾向**:\\nZH→EN 迁移优势（~7pp）在冲突和 XNLI 任务中均存在且幅度一致，说明这是模型跨语言表征的固有属性（H1 部分支持：英语锚点存在，但非冲突特有）。冲突信号编码在通用跨语言空间中。非线性成分（MLP EN→ZH gains）是否冲突特有待 XNLI 上的 MLP 对照验证。\\n\\n## Core Claims\\n\\n### Claim 1: Cross-lingual conflict detectability\\n**Statement**: 跨语言知识冲突信号可在残差流中被线性探针检测，准确率显著高于随机基线。\\n**Evidence needed**:\\n- ≥2 model architectures 的 within-language probe acc > 70% (balanced) ✅ (Llama 77.1%, Qwen 75.3%)\\n- Permutation test p < 0.001 ✅ (all directions)\\n- Cross-lingual transfer acc > chance (50%) with statistical significance ✅ (all directions 64-72%)\\n**Status**: MVP 已验证 ✅\\n\\n### Claim 2: Cross-lingual transfer asymmetry as general model property [REFRAMED per D008]\\n**Statement**: 跨语言探针迁移呈方向一致的不对称（ZH→EN > EN→ZH ~7pp），但 **XNLI 非冲突基线展现几乎相同幅度的不对称性**（Qwen +6.72pp, Llama +5.97pp），说明这是 English-dominant 模型的一般跨语言迁移属性，非冲突特有。冲突信号继承了模型的通用跨语言表征结构。\\n**Evidence**:\\n- 冲突不对称性: Llama +7.22pp CI[1.1,13.6], Qwen +7.18pp CI[-1.2,13.4] ✅\\n- XNLI 不对称性: Llama +5.97pp CI[0.92,11.33], Qwen +6.72pp CI[2.36,11.73] ✅\\n- 两者量级无显著差异，CI 大幅重叠 ✅\\n- Token overlap 排除 ✅ | COMET confound 排除 ✅\\n- ≥1 additional architecture 验证 ❌ (plan_102 Gemma 进行中)\\n**Status**: XNLI 基线已完成，C2 reframed ✅⚠️ (待第三模型确认)\\n\\n### Claim 3: Non-linear encoding trend [DEAD — D012 双模型 CI 含零]\\n**Statement**: ~~冲突信号包含非线性成分~~ → 降为 supporting observation，不作为独立 claim。\\n**Evidence**:\\n- 冲突 MLP Δ (EN→ZH): Qwen +3.84pp CI[-3.57,+11.31] 含零 ❌; Llama +5.21pp CI[-2.21,+12.87] 含零 ❌\\n- XNLI MLP Δ (EN→ZH): Qwen -2.0pp, Llama -0.5pp — 方向对比成立但不显著\\n- **双模型 bootstrap 均不显著**，方向一致（冲突正、XNLI 负）可作为 suggestive trend 在 discussion 中提及\\n**Status**: ❌ 不作为论文 claim。Discussion 中作为 observation 报告。\\n\\n### Claim 4: Layer-wise conflict signal structure\\n**Statement**: 冲突信号在 mid-to-upper layers 集中，峰值层在不同模型架构中占比一致（Llama ~88% depth, Qwen ~67% depth 有差异——需更多模型确认 pattern）。\\n**Evidence needed**:\\n- Layer-wise probe accuracy curves for ≥3 models ❌\\n- Layer-wise CKA/SVCCA 量化 EN vs ZH 表征相似度 ❌\\n- 与 \\\"Lost in Multilinguality\\\" 的 language transition 层对比 ❌\\n**Status**: 未验证 ❌\\n\\n### Claim 5: Cross-lingual SAE conflict features (Track 2)\\n**Statement**: SAE 特征空间中存在跨语言共享的冲突编码特征，可与 language-identity 特征解耦。\\n**Evidence needed**:\\n- Qwen-Scope SAE 特征分析 on Qwen3-8B-Base ❌\\n- LangFIR random-token filtering 控制 ❌\\n- Cross-lingual feature Jaccard 分析 ❌\\n**Status**: 未开始 ❌\\n\\n### Claim 6: Causal evidence via representation steering (Track 3) [v1 NEGATIVE — D011 diagnostic round]\\n**Statement**: 探针权重方向具有因果意义——沿此方向 steering 可改变模型冲突解决行为。\\n**Evidence needed**:\\n- Probe-weight steering 显著改变 p↔c flip rate (vs random control) ✅ (L13)\\n- ≥1 layer/position 配置 Fisher p < 0.05 ✅ (α=+5 p=0.002, α=-20 p=0.0009)\\n**L13 result (D014, SUCCESS)**: Llama L13, last-token — α=+5 p=0.002 (19.9% vs 6.6%), α=-20 p=0.0009 (36.0% vs 17.6%)。方向性正确：正α→p→c, 负α→c→p。\\n**L28/L18/L28-all NEGATIVE**: 因果节点在 mid-layer (L13, ~40% depth), NOT probe peak (L28, ~88%)。\\n**核心机制发现**: Detection ≠ Decision — 模型在 late-layer 编码可检测信号，但因果决策在 mid-layer 形成。\\n- 待 Qwen L13 跨模型验证 → C6 fully supported\\n**Status**: Llama L13 ✅ SUCCESS, Qwen L13 验证中 ⏳\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Translation quality confound [RESOLVED ✅]\\n**Concern**: 中文翻译质量差可能导致虚假的冲突信号或迁移失败\\n**Result**: Plan_105 COMET tercile ablation 证明翻译质量非 confounder。Qwen test: Low COMET (mean 0.585) → 66.35% acc, High COMET (mean 0.816) → 60.71% acc, delta=-5.64pp (反向), Fisher p=0.695。冲突信号检测不依赖翻译质量。Back-translation COMET ≥0.80 阈值过严（两步翻译天然拉低），但 ablation 实证排除了翻译质量 confound。\\n**Remaining**: Llama test COMET 完成后重复此分析确认一致性。\\n\\n### RC2: Token overlap confound [RESOLVED ✅]\\n**Concern**: 跨语言迁移可能由 EN-ZH 共享 token（数字、专有名词、标点）驱动\\n**Result**: Per-sample Jaccard 仅 3-4%（type-level 10-15% 被膨胀）。Qwen 无相关 (p>0.4)，Llama 显著负相关 (r=-0.15, p=0.012, tercile Δ=-23.9pp)。高 overlap 反而降低准确率，方向与 RC2 相反。**共享 token 不驱动跨语言迁移，迁移发生在语义表示层。**\\n\\n### RC3: Model coverage insufficient [HIGH]\\n**Concern**: 只有 2 个模型，无法声称 \\\"架构无关\\\"\\n**Mitigation**: 加 ≥1 不同架构（Mistral/Gemma），验证 ~7.2pp 不对称性\\n**Experiment**: P0 — additional model verification\\n\\n### RC4: Dataset size and diversity [MEDIUM]\\n**Concern**: ConflictQA 覆盖面有限（~1000 samples/model），只有 EN-ZH 一个语言对\\n**Mitigation**: Phase 1 聚焦 EN-ZH 验证核心机制，Phase 2 扩展多语言（≥1 额外语言对）\\n**Experiment**: P0 — multilingual extension (EN↔JA or EN↔DE)\\n\\n### RC5: Linear probe expressiveness [LOW]\\n**Concern**: 线性探针可能遗漏复杂非线性信号\\n**Mitigation**: MLP 对比实验已完成 ✅，非线性成分已量化\\n**Experi\\n\\n... [截断: 省略 3218 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 9218, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01QzWaUpoeLqtoxDKe1MitxV`</summary>

```json
{
  "project": "clkc_mech_interp",
  "file": "writing_plan.yaml",
  "max_chars": 6000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "025821ae-28fb-4048-b769-e56748883514",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MWiUmPYsMru4mEWKoTDJ2W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2218,
      "cache_read_input_tokens": 36734,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2218
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-22T15:36:28.200Z_

<details><summary>↩ Tool result · `toolu_01QzWaUpoeLqtoxDKe1MitxV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main (via ARR)\\n  template: \\\"\\\"\\n  template_note: \\\"需要下载 ACL/EMNLP 2026 ARR LaTeX 模板（acl_latex style）\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >-\\n    跨语言知识冲突信号可在多语言 LLM 残差流中被线性探针检测（2模型 75-77% balanced acc），\\n    其跨语言迁移不对称性（ZH→EN > EN→ZH ~7pp）与非冲突语义任务(XNLI)无异——\\n    冲突信号编码在模型通用跨语言表征空间中，继承其方向性偏置。\\n    因果 steering 揭示 detection-decision 层分离：可检测信号 peak 在 late-layer (L28, ~88% depth)，\\n    但因果决策节点在 mid-layer (L13, ~40% depth)，Fisher p=0.002。\\n    方法论贡献：严格的 confound exclusion pipeline（COMET ablation + token overlap 排除 + 非冲突基线对照）。\\n  title_draft: >-\\n    Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries\\n    from General Multilingual Representations\\n  created_at: 2026-05-22T13:00:00Z\\n  updated_at: 2026-05-22T14:00:00Z\\n  update_reason: \\\"Steering L13 SUCCESS — 新增因果证据，narrative 升级\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 150\\n    core_bullets:\\n      - \\\"问题：多语言 LLM 在跨语言知识冲突时的内部机制未知——CLEAR 发现 linguistic affinity 决定冲突解决行为，但未解释信号编码机制\\\"\\n      - \\\"方法：残差流线性探针 + 跨语言迁移 + XNLI 基线对照 + confound exclusion + representation steering\\\"\\n      - \\\"结果：2模型 balanced acc 75-77%；ZH→EN > EN→ZH ~7pp 与 XNLI 一致；mid-layer (L13) steering 成功因果改变冲突解决(Fisher p=0.002)而 late-layer (L28) 不成功\\\"\\n      - \\\"贡献：(1) 跨语言冲突检测 + 不对称性继承通用跨语言对齐 (2) Detection ≠ Decision 层分离 (3) confound exclusion pipeline\\\"\\n    dependencies: [experiments, method, introduction]\\n\\n  - section: introduction\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Hook: 多语言 LLM 面对跨语言知识冲突时表现出 language-dependent 解决偏好(CLEAR)，但冲突信号在模型内部如何编码？可检测性是否等于因果性？\\\"\\n      - \\\"Gap: 现有 probing 工作仅限单语（Zhao et al. 2024; Boer et al. 2026），跨语言扩展面临 confound 问题；probing 只证明 detectability 不证明 causality\\\"\\n      - \\\"Insight: 冲突信号可线性检测且迁移呈方向不对称(~7pp)，但该不对称性与 XNLI 无异——冲突信号 piggyback 通用跨语言对齐。更关键的是，因果 steering 揭示 detection 和 decision 发生在不同层\\\"\\n      - \\\"Detection ≠ Decision: probe peak 在 late-layer (L28, ~88% depth) 但因果 steering 仅在 mid-layer (L13, ~40% depth) 成功\\\"\\n      - \\\"Contributions: [C1: cross-lingual detectability + asymmetry as general property, C2: detection-decision layer dissociation via steering, C3: confound exclusion pipeline]\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"CLEAR (Zhao et al. 2026)\\\"\\n      - \\\"Zhao et al. (2024) — 单语冲突 probing\\\"\\n      - \\\"Boer et al. (2026) — 单语 knowledge attribution probing\\\"\\n      - \\\"ConflictQA 原始论文\\\"\\n      - \\\"Wang et al. (2025) Lost in Multilinguality\\\"\\n      - \\\"Basu et al. (2026) — interpretability without actionability (对比 steering 结果)\\\"\\n    figures: [fig1_pipeline]\\n\\n  - section: related_work\\n    word_budget: 550\\n    core_bullets:\\n      - \\\"Cluster 1: Knowledge conflict detection — 单语 probing 与 activation analysis → 我们扩展至跨语言 + confound controls\\\"\\n      - \\\"Cluster 2: Cross-lingual representations — mid-layer language-independent encoding + final-layer language transition → 我们的 steering 结果与 mid-layer 跨语言对齐位置一致\\\"\\n      - \\\"Cluster 3: Representation steering — SpARE 在单语冲突场景成功, Basu 在临床场景失败 → 我们发现层选择是关键：mid-layer 成功而 late-layer 失败\\\"\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"3.1 Task formulation: 残差流二分类(contextual vs parametric) across languages\\\"\\n      - \\\"3.2 Data construction: ConflictQA → parametric verification → translation → COMET validation\\\"\\n      - \\\"3.3 Activation extraction: last-token residual stream h_l at all L layers\\\"\\n      - \\\"3.4 Probing: per-layer logistic regression + bootstrap CI(n=2000)\\\"\\n      - \\\"3.5 Cross-lingual transfer: 4 directions + asymmetry quantification\\\"\\n      - \\\"3.6 Confound exclusion: COMET tercile + token overlap + XNLI baseline\\\"\\n      - \\\"3.7 Representation steering: 沿探针权重方向注入 α·w_probe 到 last-token residual stream; 测量 flip rate(parametric↔contextual answer switch) vs random-direction control; Fisher exact test; 在 L13/L18/L28 三层分别测试以定位因果决策节点\\\"\\n    dependencies: []\\n    notation_table:\\n      h_l: \\\"layer-l residual stream representation\\\"\\n      f_theta: \\\"logistic regression probe\\\"\\n      w_probe: \\\"probe weight vector (steering direction)\\\"\\n      Delta_asym: \\\"transfer asymmetry = acc(ZH→EN) - acc(EN→ZH)\\\"\\n    figures: [fig1_pipeline]\\n    registry_refs: [mvp_probe_v1, mvp_probe_llama_v1, steering_107, steering_107_L13]\\n\\n  - section: experiments\\n    word_budget: 1800\\n    core_bullets:\\n      - \\\"4.1 Setup: Llama-3.1-8B-Instruct(32层, 1368 samples) + Qwen3-8B(36层, 966 samples); bootstrap n=2000; balanced accuracy\\\"\\n      - \\\"4.2 Within-language detection (C1): Llama EN 77.6%, Qwen EN 75.3%; peak layers Llama L28(88% depth) vs Qwen L22(61% depth)\\\"\\n      - \\\"4.3 Cross-lingual transfer & asymmetry: all 4 directions above chance; Llama Δ=+7.22pp CI[1.1,13.6]; Qwen Δ=+7.18pp CI[-1.2,13.4]\\\"\\n      - \\\"4.4 XNLI non-conflict baseline: Llama Δ=+5.97pp CI[0.92,11.33]; Qwen Δ=+6.72pp CI[2.36,11.73] — 与冲突任务 CI 大幅重叠 → asymmetry is general\\\"\\n      - \\\"4.5 Confound analysis: COMET tercile not significant; Token overlap no positive correlation\\\"\\n      - \\\"4.6 Causal steering (C2): L13 SUCCESS — α=+5 Fisher p=0.002, flip 19.9% vs control 6.6%, directional flips all p→c; α=-20 Fisher p=0.0009, flip 36.0% vs control 17.6%, c→p direction. L28 and L18 both NEGATIVE (all Fisher p>0.3). Detection-Decision dissociation: detectable signal peaks late (L28) but causal node is mid (L13)\\\"\\n      - \\\"[PLACEHOLDER] Qwen L13 steering — 跨模型验证\\\"\\n      - \\\"[PLACEHOLDER] Third model (Gemma-2-9B-IT)\\\"\\n    dependencies: []\\n    registry_refs:\\n      - mvp_probe_v1\\n      - mvp_probe_llama_v1\\n      - xnli_baseline_110\\n      - steering_107\\n      - steering_107_L13\\n      - steering_107_L18\\n      - steering_107_L28_all\\n      - bootstrap_n2000_111\\n      - gemma_full_pipeline_102\\n    tables: [tab1_main_results, tab2_confound, tab3_steering]\\n    figures: [fig2_layer_probe, fig3_asymmetry_forest]\\n\\n  - section: discussion\\n    word_budget: 500\\n    core_bullets:\\n      - \\\"Detection ≠ Decision: 模型在 late-layer 编码可检测冲突信号(probe peak L28)，但因果决策在 mid-layer(L13, ~40% depth)已形成。与 Wang et al. (2025) 一致——mid-layer 是跨语言对齐发生的层，也是冲突信号获得因果力的位置\\\"\\n      - \\\"冲突信号编码在通用跨语言空间: XNLI 对照证明不对称性非冲突特有，冲突信号 piggyback 通用表征\\\"\\n\\n... [截断: 省略 6623 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12623, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "7d988154-3362-4c19-b15e-9fb62c562820",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml\\\", \\\"content\\\": \\\"meta:\\\\n  venue: EMNLP 2026\\\\n  track: main (via ARR)\\\\n  template: \\\\\\\"\\\\\\\"\\\\n  template_note: \\\\\\\"需要下载 ACL/EMNLP 2026 ARR LaTeX 模板（acl_latex style）\\\\\\\"\\\\n  page_limit: 8\\\\n  deadline: 2026-05-25\\\\n  core_claim: >-\\\\n    跨语言知识冲突信号可在多语言 LLM 残差流中被线性探针检测（2模型 75-77% balanced acc），\\\\n    其跨语言迁移不对称性（ZH→EN > EN→ZH ~7pp）与非冲突语义任务(XNLI)无异——\\\\n    冲突信号编码在模型通用跨语言表征空间中，继承其方向性偏置。\\\\n    因果 steering 揭示 detection-decision 层分离：可检测信号 peak 在 late-layer (L28, ~88% depth)，\\\\n    但因果决策节点在 mid-layer (L13, ~40% depth)，Fisher p=0.002。\\\\n    方法论贡献：严格的 confound exclusion pipeline（COMET ablation + token overlap 排除 + 非冲突基线对照）。\\\\n  title_draft: >-\\\\n    Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries\\\\n    from General Multilingual Representations\\\\n  created_at: 2026-05-22T13:00:00Z\\\\n  updated_at: 2026-05-22T14:00:00Z\\\\n  update_reason: \\\\\\\"Steering L13 SUCCESS — 新增因果证据，narrative 升级\\\\\\\"\\\\n\\\\npaper_outline:\\\\n  - section: abstract\\\\n    word_budget: 150\\\\n    core_bullets:\\\\n      - \\\\\\\"问题：多语言 LLM 在跨语言知识冲突时的内部机制未知——CLEAR 发现 linguistic affinity 决定冲突解决行为，但未解释信号编码机制\\\\\\\"\\\\n      - \\\\\\\"方法：残差流线性探针 + 跨语言迁移 + XNLI 基线对照 + confound exclusion + representation steering\\\\\\\"\\\\n      - \\\\\\\"结果：2模型 balanced acc 75-77%；ZH→EN > EN→ZH ~7pp 与 XNLI 一致；mid-layer (L13) steering 成功因果改变冲突解决(Fisher p=0.002)而 late-layer (L28) 不成功\\\\\\\"\\\\n      - \\\\\\\"贡献：(1) 跨语言冲突检测 + 不对称性继承通用跨语言对齐 (2) Detection ≠ Decision 层分离 (3) confound exclusion pipeline\\\\\\\"\\\\n    dependencies: [experiments, method, introduction]\\\\n\\\\n  - section: introduction\\\\n    word_budget: 900\\\\n    core_bullets:\\\\n      - \\\\\\\"Hook: 多语言 LLM 面对跨语言知识冲突时表现出 language-dependent 解决偏好(CLEAR)，但冲突信号在模型内部如何编码？可检测性是否等于因果性？\\\\\\\"\\\\n      - \\\\\\\"Gap: 现有 probing 工作仅限单语（Zhao et al. 2024; Boer et al. 2026），跨语言扩展面临 confound 问题；probing 只证明 detectability 不证明 causality\\\\\\\"\\\\n      - \\\\\\\"Insight: 冲突信号可线性检测且迁移呈方向不对称(~7pp)，但该不对称性与 XNLI 无异——冲突信号 piggyback 通用跨语言对齐。更关键的是，因果 steering 揭示 detection 和 decision 发生在不同层\\\\\\\"\\\\n      - \\\\\\\"Detection ≠ Decision: probe peak 在 late-layer (L28, ~88% depth) 但因果 steering 仅在 mid-layer (L13, ~40% depth) 成功\\\\\\\"\\\\n      - \\\\\\\"Contributions: [C1: cross-lingual detectability + asymmetry as general property, C2: detection-decision layer dissociation via steering, C3: confound exclusion pipeline]\\\\\\\"\\\\n    dependencies: [experiments]\\\\n    citation_hints:\\\\n      - \\\\\\\"CLEAR (Zhao et al. 2026)\\\\\\\"\\\\n      - \\\\\\\"Zhao et al. (2024) — 单语冲突 probing\\\\\\\"\\\\n      - \\\\\\\"Boer et al. (2026) — 单语 knowledge attribution probing\\\\\\\"\\\\n      - \\\\\\\"ConflictQA 原始论文\\\\\\\"\\\\n      - \\\\\\\"Wang et al. (2025) Lost in Multilinguality\\\\\\\"\\\\n      - \\\\\\\"Basu et al. (2026) — interpretability without actionability (对比 steering 结果)\\\\\\\"\\\\n    figures: [fig1_pipeline]\\\\n\\\\n  - section: related_work\\\\n    word_budget: 550\\\\n    core_bullets:\\\\n      - \\\\\\\"Cluster 1: Knowledge conflict detection — 单语 probing 与 activation analysis → 我们扩展至跨语言 + confound controls\\\\\\\"\\\\n      - \\\\\\\"Cluster 2: Cross-lingual representations — mid-layer language-independent encoding + final-layer language transition → 我们的 steering 结果与 mid-layer 跨语言对齐位置一致\\\\\\\"\\\\n      - \\\\\\\"Cluster 3: Representation steering — SpARE 在单语冲突场景成功, Basu 在临床场景失败 → 我们发现层选择是关键：mid-layer 成功而 late-layer 失败\\\\\\\"\\\\n    dependencies: [introduction]\\\\n\\\\n  - section: method\\\\n    word_budget: 1200\\\\n    core_bullets:\\\\n      - \\\\\\\"3.1 Task formulation: 残差流二分类(contextual vs parametric) across languages\\\\\\\"\\\\n      - \\\\\\\"3.2 Data construction: ConflictQA → parametric verification → translation → COMET validation\\\\\\\"\\\\n      - \\\\\\\"3.3 Activation extraction: last-token residual stream h_l at all L layers\\\\\\\"\\\\n      - \\\\\\\"3.4 Probing: per-layer logistic regression + bootstrap CI(n=2000)\\\\\\\"\\\\n      - \\\\\\\"3.5 Cross-lingual transfer: 4 directions + asymmetry quantification\\\\\\\"\\\\n      - \\\\\\\"3.6 Confound exclusion: COMET tercile + token overlap + XNLI baseline\\\\\\\"\\\\n      - \\\\\\\"3.7 Representation steering: 沿探针权重方向注入 α·w_probe 到 last-token residual stream; 测量 flip rate(parametric↔contextual answer switch) vs random-direction control; Fisher exact test; 在 L13/L18/L28 三层分别测试以定位因果决策节点\\\\\\\"\\\\n    dependencies: []\\\\n    notation_table:\\\\n      h_l: \\\\\\\"layer-l residual stream representation\\\\\\\"\\\\n      f_theta: \\\\\\\"logistic regression probe\\\\\\\"\\\\n      w_probe: \\\\\\\"probe weight vector (steering direction)\\\\\\\"\\\\n      Delta_asym: \\\\\\\"transfer asymmetry = acc(ZH→EN) - acc(EN→ZH)\\\\\\\"\\\\n    figures: [fig1_pipeline]\\\\n    registry_refs: [mvp_probe_v1, mvp_probe_llama_v1, steering_107, steering_107_L13]\\\\n\\\\n  - section: experiments\\\\n    word_budget: 1800\\\\n    core_bullets:\\\\n      - \\\\\\\"4.1 Setup: Llama-3.1-8B-Instruct(32层, 1368 samples) + Qwen3-8B(36层, 966 samples); bootstrap n=2000; balanced accuracy\\\\\\\"\\\\n      - \\\\\\\"4.2 Within-language detection (C1): Llama EN 77.6%, Qwen EN 75.3%; peak layers Llama L28(88% depth) vs Qwen L22(61% depth)\\\\\\\"\\\\n      - \\\\\\\"4.3 Cross-lingual transfer & asymmetry: all 4 directions above chance; Llama Δ=+7.22pp CI[1.1,13.6]; Qwen Δ=+7.18pp CI[-1.2,13.4]\\\\\\\"\\\\n      - \\\\\\\"4.4 XNLI non-conflict baseline: Llama Δ=+5.97pp CI[0.92,11.33]; Qwen Δ=+6.72pp CI[2.36,11.73] — 与冲突任务 CI 大幅重叠 → asymmetry is general\\\\\\\"\\\\n      - \\\\\\\"4.5 Confound analysis: COMET tercile not significant; Token overlap no positive correlation\\\\\\\"\\\\n      - \\\\\\\"4.6 Causal steering (C2): L13 SUCCESS — α=+5 Fisher p=0.002, flip 19.9% vs control 6.6%, directional flips all p→c; α=-20 Fisher p=0.0009, flip 36.0% vs control 17.6%, c→p direction. L28 and L18 both NEGATIVE (all Fisher p>0.3). Detection-Decision dissociation: detectable signal peaks late (L28) but causal node is mid (L13)\\\\\\\"\\\\n      - \\\\\\\"[PLACEHOLDER] Qwen L13 steering — 跨模型验证\\\\\\\"\\\\n      - \\\\\\\"[PLACEHOLDER] Third model (Gemma-2-9B-IT)\\\\\\\"\\\\n    dependencies: []\\\\n    registry_refs:\\\\n      - mvp_probe_v1\\\\n      - mvp_probe_llama_v1\\\\n      - xnli_baseline_110\\\\n      - steering_107\\\\n      - steering_107_L13\\\\n      - steering_107_L18\\\\n      - steering_107_L28_all\\\\n      - bootstrap_n2000_111\\\\n      - gemma_full_pipeline_102\\\\n    tables: [tab1_main_results, tab2_confound, tab3_steering]\\\\n    figures: [fig2_layer_probe, fig3_asymmetry_forest]\\\\n\\\\n  - section: discussion\\\\n    word_budget: 500\\\\n    core_bullets:\\\\n      - \\\\\\\"Detection ≠ Decision: 模型在 late-layer 编码可检测冲突信号(probe peak L28)，但因果决策在 mid-layer(L13, ~40% depth)已形成。与 Wang et al. (2025) 一致——mid-layer 是跨语言对齐发生的层，也是冲突信号获得因果力的位置\\\\\\\"\\\\n      - \\\\\\\"冲突信号编码在通用跨语言空间: XNLI 对照证明不对称性非冲突特有，冲突信号 piggyback 通用表征\\\\\\\"\\\\n\\\\n... [截断: 省略 6623 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 12623, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/writing_plan.yaml\", \"content\": \"meta:\\n  venue: EMNLP 2026\\n  track: main (via ARR)\\n  template: \\\"\\\"\\n  template_note: \\\"需要下载 ACL/EMNLP 2026 ARR LaTeX 模板（acl_latex style）\\\"\\n  page_limit: 8\\n  deadline: 2026-05-25\\n  core_claim: >-\\n    跨语言知识冲突信号可在多语言 LLM 残差流中被线性探针检测（2模型 75-77% balanced acc），\\n    其跨语言迁移不对称性（ZH→EN > EN→ZH ~7pp）与非冲突语义任务(XNLI)无异——\\n    冲突信号编码在模型通用跨语言表征空间中，继承其方向性偏置。\\n    因果 steering 揭示 detection-decision 层分离：可检测信号 peak 在 late-layer (L28, ~88% depth)，\\n    但因果决策节点在 mid-layer (L13, ~40% depth)，Fisher p=0.002。\\n    方法论贡献：严格的 confound exclusion pipeline（COMET ablation + token overlap 排除 + 非冲突基线对照）。\\n  title_draft: >-\\n    Cross-Lingual Knowledge Conflict Signals Inherit Directional Asymmetries\\n    from General Multilingual Representations\\n  created_at: 2026-05-22T13:00:00Z\\n  updated_at: 2026-05-22T14:00:00Z\\n  update_reason: \\\"Steering L13 SUCCESS — 新增因果证据，narrative 升级\\\"\\n\\npaper_outline:\\n  - section: abstract\\n    word_budget: 150\\n    core_bullets:\\n      - \\\"问题：多语言 LLM 在跨语言知识冲突时的内部机制未知——CLEAR 发现 linguistic affinity 决定冲突解决行为，但未解释信号编码机制\\\"\\n      - \\\"方法：残差流线性探针 + 跨语言迁移 + XNLI 基线对照 + confound exclusion + representation steering\\\"\\n      - \\\"结果：2模型 balanced acc 75-77%；ZH→EN > EN→ZH ~7pp 与 XNLI 一致；mid-layer (L13) steering 成功因果改变冲突解决(Fisher p=0.002)而 late-layer (L28) 不成功\\\"\\n      - \\\"贡献：(1) 跨语言冲突检测 + 不对称性继承通用跨语言对齐 (2) Detection ≠ Decision 层分离 (3) confound exclusion pipeline\\\"\\n    dependencies: [experiments, method, introduction]\\n\\n  - section: introduction\\n    word_budget: 900\\n    core_bullets:\\n      - \\\"Hook: 多语言 LLM 面对跨语言知识冲突时表现出 language-dependent 解决偏好(CLEAR)，但冲突信号在模型内部如何编码？可检测性是否等于因果性？\\\"\\n      - \\\"Gap: 现有 probing 工作仅限单语（Zhao et al. 2024; Boer et al. 2026），跨语言扩展面临 confound 问题；probing 只证明 detectability 不证明 causality\\\"\\n      - \\\"Insight: 冲突信号可线性检测且迁移呈方向不对称(~7pp)，但该不对称性与 XNLI 无异——冲突信号 piggyback 通用跨语言对齐。更关键的是，因果 steering 揭示 detection 和 decision 发生在不同层\\\"\\n      - \\\"Detection ≠ Decision: probe peak 在 late-layer (L28, ~88% depth) 但因果 steering 仅在 mid-layer (L13, ~40% depth) 成功\\\"\\n      - \\\"Contributions: [C1: cross-lingual detectability + asymmetry as general property, C2: detection-decision layer dissociation via steering, C3: confound exclusion pipeline]\\\"\\n    dependencies: [experiments]\\n    citation_hints:\\n      - \\\"CLEAR (Zhao et al. 2026)\\\"\\n      - \\\"Zhao et al. (2024) — 单语冲突 probing\\\"\\n      - \\\"Boer et al. (2026) — 单语 knowledge attribution probing\\\"\\n      - \\\"ConflictQA 原始论文\\\"\\n      - \\\"Wang et al. (2025) Lost in Multilinguality\\\"\\n      - \\\"Basu et al. (2026) — interpretability without actionability (对比 steering 结果)\\\"\\n    figures: [fig1_pipeline]\\n\\n  - section: related_work\\n    word_budget: 550\\n    core_bullets:\\n      - \\\"Cluster 1: Knowledge conflict detection — 单语 probing 与 activation analysis → 我们扩展至跨语言 + confound controls\\\"\\n      - \\\"Cluster 2: Cross-lingual representations — mid-layer language-independent encoding + final-layer language transition → 我们的 steering 结果与 mid-layer 跨语言对齐位置一致\\\"\\n      - \\\"Cluster 3: Representation steering — SpARE 在单语冲突场景成功, Basu 在临床场景失败 → 我们发现层选择是关键：mid-layer 成功而 late-layer 失败\\\"\\n    dependencies: [introduction]\\n\\n  - section: method\\n    word_budget: 1200\\n    core_bullets:\\n      - \\\"3.1 Task formulation: 残差流二分类(contextual vs parametric) across languages\\\"\\n      - \\\"3.2 Data construction: ConflictQA → parametric verification → translation → COMET validation\\\"\\n      - \\\"3.3 Activation extraction: last-token residual stream h_l at all L layers\\\"\\n      - \\\"3.4 Probing: per-layer logistic regression + bootstrap CI(n=2000)\\\"\\n      - \\\"3.5 Cross-lingual transfer: 4 directions + asymmetry quantification\\\"\\n      - \\\"3.6 Confound exclusion: COMET tercile + token overlap + XNLI baseline\\\"\\n      - \\\"3.7 Representation steering: 沿探针权重方向注入 α·w_probe 到 last-token residual stream; 测量 flip rate(parametric↔contextual answer switch) vs random-direction control; Fisher exact test; 在 L13/L18/L28 三层分别测试以定位因果决策节点\\\"\\n    dependencies: []\\n    notation_table:\\n      h_l: \\\"layer-l residual stream representation\\\"\\n      f_theta: \\\"logistic regression probe\\\"\\n      w_probe: \\\"probe weight vector (steering direction)\\\"\\n      Delta_asym: \\\"transfer asymmetry = acc(ZH→EN) - acc(EN→ZH)\\\"\\n    figures: [fig1_pipeline]\\n    registry_refs: [mvp_probe_v1, mvp_probe_llama_v1, steering_107, steering_107_L13]\\n\\n  - section: experiments\\n    word_budget: 1800\\n    core_bullets:\\n      - \\\"4.1 Setup: Llama-3.1-8B-Instruct(32层, 1368 samples) + Qwen3-8B(36层, 966 samples); bootstrap n=2000; balanced accuracy\\\"\\n      - \\\"4.2 Within-language detection (C1): Llama EN 77.6%, Qwen EN 75.3%; peak layers Llama L28(88% depth) vs Qwen L22(61% depth)\\\"\\n      - \\\"4.3 Cross-lingual transfer & asymmetry: all 4 directions above chance; Llama Δ=+7.22pp CI[1.1,13.6]; Qwen Δ=+7.18pp CI[-1.2,13.4]\\\"\\n      - \\\"4.4 XNLI non-conflict baseline: Llama Δ=+5.97pp CI[0.92,11.33]; Qwen Δ=+6.72pp CI[2.36,11.73] — 与冲突任务 CI 大幅重叠 → asymmetry is general\\\"\\n      - \\\"4.5 Confound analysis: COMET tercile not significant; Token overlap no positive correlation\\\"\\n      - \\\"4.6 Causal steering (C2): L13 SUCCESS — α=+5 Fisher p=0.002, flip 19.9% vs control 6.6%, directional flips all p→c; α=-20 Fisher p=0.0009, flip 36.0% vs control 17.6%, c→p direction. L28 and L18 both NEGATIVE (all Fisher p>0.3). Detection-Decision dissociation: detectable signal peaks late (L28) but causal node is mid (L13)\\\"\\n      - \\\"[PLACEHOLDER] Qwen L13 steering — 跨模型验证\\\"\\n      - \\\"[PLACEHOLDER] Third model (Gemma-2-9B-IT)\\\"\\n    dependencies: []\\n    registry_refs:\\n      - mvp_probe_v1\\n      - mvp_probe_llama_v1\\n      - xnli_baseline_110\\n      - steering_107\\n      - steering_107_L13\\n      - steering_107_L18\\n      - steering_107_L28_all\\n      - bootstrap_n2000_111\\n      - gemma_full_pipeline_102\\n    tables: [tab1_main_results, tab2_confound, tab3_steering]\\n    figures: [fig2_layer_probe, fig3_asymmetry_forest]\\n\\n  - section: discussion\\n    word_budget: 500\\n    core_bullets:\\n      - \\\"Detection ≠ Decision: 模型在 late-layer 编码可检测冲突信号(probe peak L28)，但因果决策在 mid-layer(L13, ~40% depth)已形成。与 Wang et al. (2025) 一致——mid-layer 是跨语言对齐发生的层，也是冲突信号获得因果力的位置\\\"\\n      - \\\"冲突信号编码在通用跨语言空间: XNLI 对照证明不对称性非冲突特有，冲突信号 piggyback 通用表征\\\"\\n\\n... [截断: 省略 6623 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 12623, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper's context, style, claims, and existing sections. Let me also read the paper-writing-norms skill for style guidance since this is for EMNLP 2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "a03843a3-d62b-4e9d-ac31-a559fd0b9dff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyFLdQUgyoCgVBWEAFvbhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7080,
      "cache_read_input_tokens": 38952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7080
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 33_

Now I have full context. Let me also load the paper writing norms skill for style reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "8a3efc40-729e-4340-ab45-48ef61d33f78",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyFLdQUgyoCgVBWEAFvbhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7080,
      "cache_read_input_tokens": 38952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7080
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01EauVcQtewJ3pbdTsqPwqDA`</summary>

```json
{
  "file_path": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
  "limit": 100
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "700e4ce6-685f-4abf-a327-dadc8cedbe62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SyFLdQUgyoCgVBWEAFvbhk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7080,
      "cache_read_input_tokens": 38952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7080
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-22T15:36:33.155Z_

<details><summary>↩ Tool result · `toolu_01EauVcQtewJ3pbdTsqPwqDA`</summary>

```text
1	---
2	name: paper-writing-norms
3	description: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。
4	allowed-tools: [Read, Write, Edit, Glob, Grep]
5	scope: global
6	version: 2
7	priority: 9
8	tags:
9	  - writing
10	  - paper
11	  - style
12	  - norms
13	roles:
14	  - agent
15	  - worker
16	  - paper_agent
17	---
18	
19	# 论文写作风格规范
20	
21	> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。
22	
23	---
24	
25	## 一、总体写作哲学
26	
27	### 1.1 故事驱动，不是数据堆砌
28	
29	- 论文必须以"故事线"为核心展开：问题 → 洞察 → 方法 → 验证
30	- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进
31	- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌
32	- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing
33	
34	### 1.2 主线统一性
35	
36	- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**
37	- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C
38	- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机
39	- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线
40	
41	### 1.3 专有名词必须有定义
42	
43	- 首次出现的专有名词/缩写必须给出完整定义和解释
44	- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）
45	- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用
46	- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug
47	
48	### 1.4 写作前必读同类优秀论文
49	
50	- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可
51	- 重点学：
52	  - Abstract 怎么用最少篇幅讲完故事
53	  - Introduction 怎么从大问题切入到具体贡献
54	  - Related Work 怎么 positioning 自己（不是 survey）
55	  - Table/Figure 怎么压缩信息密度
56	- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大
57	- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文
58	
59	---
60	
61	## 二、Abstract 写作规范
62	
63	### 2.1 四个必答问题（150-250 words）
64	
65	Abstract 必须在很短的篇幅内清楚回答：
66	1. **研究什么问题** — 1-2 句话交代背景和痛点
67	2. **为什么重要** — 现有方法的不足（不用写太多）
68	3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）
69	4. **结果说明什么** — 用具体实验结论支撑贡献
70	
71	### 2.2 禁忌
72	
73	- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim
74	- **禁止过度宣传**：不说 "revolutionary"、"groundbreaking"
75	- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元
76	- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了
77	- **缩写必须定义**：Abstract 中首次出现的缩写必须展开
78	
79	### 2.3 审稿人视角检验
80	
81	写完后用这个标准自检：审稿人能否在 30 秒内判断——
82	- 问题是否重要？
83	- 方法是否清楚？
84	- 贡献是否可信？
85	- 结果是否有说服力？
86	
87	---
88	
89	## 三、Introduction 写作规范
90	
91	### 3.1 完整叙事线（5 段结构）
92	
93	Introduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：
94	
95	1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈
96	2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题
97	3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）
98	4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题
99	5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "28514953-f05b-40fb-ab47-39c46ba97625",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md",
      "content": "---\nname: paper-writing-norms\ndescription: 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。\nallowed-tools: [Read, Write, Edit, Glob, Grep]\nscope: global\nversion: 2\npriority: 9\ntags:\n  - writing\n  - paper\n  - style\n  - norms\nroles:\n  - agent\n  - worker\n  - paper_agent\n---\n\n# 论文写作风格规范\n\n> 核心哲学：**论文是一个有说服力的故事，不是实验报告。** 审稿人在几十秒内判断论文价值——如果 Abstract 和 Introduction 读起来像实验日志，论文就已经失败了。\n\n---\n\n## 一、总体写作哲学\n\n### 1.1 故事驱动，不是数据堆砌\n\n- 论文必须以\"故事线\"为核心展开：问题 → 洞察 → 方法 → 验证\n- 禁止大量实验数据堆砌——每个数字出现必须服务于叙事推进\n- 附录内容必须在正文中有明确引用且融入叙事，禁止简单堆砌\n- 如果附录数据对核心叙事有重大影响，根据附录数据调整论文 framing\n\n### 1.2 主线统一性\n\n- 当 idea 在研究过程中发生变化后，**必须重审全文逻辑**\n- 常见问题：Introduction 讲的故事 A，Method 做的是故事 B，Results 又在讲故事 C\n- 修复方式：从最终实验结论反推，重写 Introduction 的问题定义和动机\n- 每次 idea 调整后检查：Abstract → Introduction → Method → Results → Discussion → Conclusion 是否形成一条连贯主线\n\n### 1.3 专有名词必须有定义\n\n- 首次出现的专有名词/缩写必须给出完整定义和解释\n- Abstract 中使用的缩写也必须在 Abstract 内定义（如 LLM = Large Language Model）\n- 不能假设读者知道你自己定义的术语——论文从来没解释过的概念不能直接使用\n- 通用规则：如果一个非标准术语第一次出现时没有括号定义，就是写作 bug\n\n### 1.4 写作前必读同类优秀论文\n\n- 每个章节动笔前，找 **2-3 篇目标会议近 1-2 年的高分论文**作为风格参考——同类问题或同类方法皆可\n- 重点学：\n  - Abstract 怎么用最少篇幅讲完故事\n  - Introduction 怎么从大问题切入到具体贡献\n  - Related Work 怎么 positioning 自己（不是 survey）\n  - Table/Figure 怎么压缩信息密度\n- **不是抄袭**，是学习同行的故事节奏和审美——不同子领域叙事节奏差异很大\n- 实操：Paper Agent 可以从 `literature_map.yaml` 中挑 `role=foundation` 或 `role=direct-competitor` 的论文，把 `{title, venue, year, abstract}` 附在 Worker 的 task_prompt 中作为概念参考；如需学习写作风格本身，让 Worker 通过 WebSearch 取得论文链接并 fetch 全文\n\n---\n\n## 二、Abstract 写作规范\n\n### 2.1 四个必答问题（150-250 words）\n\nAbstract 必须在很短的篇幅内清楚回答：\n1. **研究什么问题** — 1-2 句话交代背景和痛点\n2. **为什么重要** — 现有方法的不足（不用写太多）\n3. **本文提出什么** — 核心贡献的关键机制（简要，不堆砌细节）\n4. **结果说明什么** — 用具体实验结论支撑贡献\n\n### 2.2 禁忌\n\n- **禁止堆砌数据**：Abstract 不是 Results 的缩写。最多引用 2-3 个关键数字，要服务于 claim\n- **禁止过度宣传**：不说 \"revolutionary\"、\"groundbreaking\"\n- **禁止写成 Introduction 的缩写**：Abstract 是独立阅读单元\n- **禁止术语堆积**：如果审稿人几十秒内判断不出价值，就失败了\n- **缩写必须定义**：Abstract 中首次出现的缩写必须展开\n\n### 2.3 审稿人视角检验\n\n写完后用这个标准自检：审稿人能否在 30 秒内判断——\n- 问题是否重要？\n- 方法是否清楚？\n- 贡献是否可信？\n- 结果是否有说服力？\n\n---\n\n## 三、Introduction 写作规范\n\n### 3.1 完整叙事线（5 段结构）\n\nIntroduction 需要从一个清晰、重要的问题切入，逐步把读者带到核心贡献：\n\n1. **研究背景**（1-2 段）：大模型在某类能力/应用中已取得进展，但仍存在一个关键瓶颈\n2. **问题重要性**（1 段）：结合真实应用、已有方法局限或当前趋势，说明这不是小问题\n3. **现有方法不足**（1 段）：系统梳理为什么不够（依赖更大模型/更多数据/更复杂推理/更高成本，或只在特定 benchmark 有效）\n4. **本文核心想法**（1 段）：我们观察到什么、提出了什么方法、为什么能解决上述问题\n5. **贡献总结**（列表）：清楚列出方法贡献、实验贡献和分析贡献\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 276
    }
  }
}
```

</details>

---

### Assistant

_source line 36_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me write the Abstract and Discussion sections.

Key points for the Abstract:
- 150-250 words
- Structure: problem → method → findings → significance
- Don't overstate (C3 not significant, steering only Llama success)
- Key numbers: 2 models, probe acc 75-77%, ZH→EN asymmetry ~7pp
- Academic English, no AI-style words
- Hedging for uncertain findings

Key points for Discussion:
- 4-5 paragraphs
- P1: Detection ≠ Decision mechanism implications


- P2: Asymmetry as general English-anchored property (connect XNLI)
- P3: C3 non-linearity as observation
- P4: Steering model-specificity
- P5: Broader implications for CLEAR and cross-lingual NLP

I need to match the tone and style of the existing introduction, method, and experiments sections. Looking at what's already written, the prose is direct and economical—specific numbers appear inline, active voice carries the argument, and hedging language like "consistent with" and "suggests" appears where findings are uncertain. Citations integrate smoothly without disrupting the flow. I'll maintain that same academic register while drafting these sections now.

For the abstract, I'm aiming for around 200 words given the user's 150–250 range. Let me pull the key experimental results to ground the writing: Llama achieves 77.1% on English-to-English steering at layer 28 with 88% depth, while Qwen peaks at 75.3% at layer 22 with 61% depth. Both models show similar asymmetry effects of +7.2 percentage points. Cross-lingual performance drops noticeably—Llama reaches 64.1% on English-to-Chinese and 71.3% on Chinese-to-English, with Qwen at 65.0% and 72.2% respectively. These numbers will anchor the abstract's claims about model-specificity and the asymmetry phenomenon.

The steering experiments reveal layer-specific effects: at layer 13, Llama shows dramatic shifts with α=+5 producing 19.9% versus 6.6% baseline (p=0.002), and α=-20 reaching 36.0% versus 17.6% (p<0.001). Deeper layers like L28 and L18 show no significant steering effects. I should also note that confounds like COMET tercile and token overlap don't explain the results, strengthening the claim that we're observing genuine knowledge conflict signals rather than artifacts.

Now I'm drafting the abstract, which needs to synthesize all these findings concisely. The key is establishing that we've identified directional asymmetries in how multilingual models handle conflicting knowledge, demonstrated through probing and steering, and that these patterns generalize across architecturally distinct models. The findings suggest that cross-lingual conflict signals exist within the model's general multilingual representation space, but the layer where these signals are most detectable isn't necessarily where the model actually uses them to make decisions. Now I'm reviewing the abstract against the introduction to avoid redundancy, and thinking through the key stylistic elements—making sure it's self-contained, includes only the most critical numbers, and defines any abbreviations on first use. encoding of this conflict signal remains unexplored beyond monolingual settings. We probe the residual stream representations of two architecturally distinct LLMs (Llama-3.1-8B-Instruct and Qwen3-8B) and find that knowledge conflict signals are linearly detectable both within and across languages, with balanced accuracy reaching 75–77% on English inputs and all cross-lingual transfer directions exceeding chance. Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese representations transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry, however, is not conflict-specific—probes trained on a non-conflict semantic task (XNLI) show the same pattern at comparable magnitude—indicating that conflict signals inherit the directional biases of the model's general cross-lingual representations. Representation steering reveals a further dissociation: the detectable signal peaks at late layers (~88% depth), but causal influence on conflict resolution is confined to a mid-layer (~41% depth; Fisher p = 0.002), with all late-layer interventions producing no behavioral change. These findings demonstrate that cross-lingual conflict detection operates within shared multilingual representation space, and that linear detectability does not imply causal relevance at the same computational stage.

Now I'm drafting the discussion section, starting with the key insight that detectability and causal influence operate at different layers—the conflict signal is most readable at layer 28 in Llama where accuracy peaks at 88%, but steering at that layer has no effect on behavior, whereas the actual causal influence happens earlier at layer 13 where the probe accuracy is lower but perturbations actually matter. The asymmetry of about 7 percentage points in cross-lingual transfer—where Chinese-trained probes generalize better to English than vice versa—turns out to reflect the model's underlying representational geometry rather than something specific to conflict encoding. When I compare this against XNLI baselines using entailment-versus-contradiction classification, the same directional asymmetry emerges at nearly identical magnitudes with overlapping confidence intervals, suggesting the effect is language-independent and tied to how these multilingual models embed English-dominant structure into their latent space.

For cross-lingual probing work more broadly, this means any transfer asymmetry needs to be validated against a non-conflict control task before attributing it to the phenomenon being studied. On the non-linearity side, MLP probes do show a suggestive pattern of larger gains on the conflict task compared to XNLI when transferring from English to Chinese, and this direction holds across both models, but the confidence intervals straddle zero in both cases, so I'm treating this as a directional observation rather than a statistically confirmed finding.

If there is a non-linear component to how these models encode conflict signals, it appears to be quite small and would need either more data or more sophisticated probes to pin down reliably. The fact that we're not seeing strong non-linear effects is actually meaningful—it indicates the conflict signal that cross-lingual probes pick up is fundamentally linear in nature, which aligns with what we know about how logistic regression probes work well for capturing cross-lingual semantic information.

The steering experiments reveal a constraint: Llama shows clear bidirectional steering effects at layer 13, but Qwen at comparable depths hasn't produced significant results yet. This model-specificity doesn't undermine the detection-decision dissociation we found, but it does limit how broadly we can claim the effect generalizes.

The difference might stem from architectural variations—grouped-query attention, layer normalization approaches, or differences in pretraining data could all shift where conflict resolution happens across layers. Or Qwen's cross-lingual alignment might be organized differently enough that the steering layer needs to be at a different depth. What's important here is that causal interventions don't transfer as smoothly across architectures as behavioral patterns do, suggesting each model architecture needs its own mechanistic validation.

These findings bear on both the CLEAR framework and cross-lingual NLP more broadly. Prior work showed that linguistic affinity determines which answer wins in entity-centric factual conflicts, and our mechanistic analysis starts to explain the underlying machinery behind that pattern.

Conflict signals live in the model's shared multilingual space and pick up directional biases from it—in English-dominant models, that means English gets favored. The confound exclusion pipeline I developed—combining translation quality checks, token overlap analysis, and non-conflict baselines—fills methodological gaps that matter for any cross-lingual probing work. As multilingual models get deployed where conflicting information might arrive in different languages, understanding how they resolve those conflicts internally becomes practically important. The detection-decision split is particularly useful here: it suggests that if we want to control conflict resolution behavior, we should focus on mid-layer representations rather than the layers where the outcome is easiest to read off.

I'm also checking the Qwen steering results—both L14 and L23 came back negative, so that's already settled. Gemma's still being verified.

For P4, I need to be careful about the steering model-specificity claim since it's only shown up in Llama so far, with Qwen negative and Gemma still pending. If Gemma also comes back negative, that would actually be a meaningful finding in itself—that steering effectiveness is model-specific. But for now I should note that the current evidence is limited to Llama, with Qwen showing negative results.

I also need to add P5 about the broader implications for CLEAR and cross-lingual NLP more generally. And I should write these sections as markdown files in clean academic prose, using LaTeX-style citations and math notation where needed, while avoiding AI-style language and being appropriately hedged about uncertain findings. I need to be careful with my language here—only claiming consistency when I have solid evidence from multiple models, and using appropriate hedging for the findings. The key metrics are 75-77% balanced accuracy across two models with roughly 7 percentage points of cross-lingual transfer, and I should avoid overstating what C3 shows or how general the steering effects are. Now I'm drafting the abstract, making sure it captures the core finding about directional asymmetry in cross-lingual transfer while staying grounded in what the data actually supports. I've confirmed the word count reaches exactly 200 words. I should be more precise about the language in the final sentence though—"demonstrate" is appropriate for the cross-lingual detection finding since it's supported across both models, and the steering evidence from Llama is statistically significant enough to warrant that strength of claim for the detectability-causality dissociation. I'll note that the Qwen steering results came back negative, which is worth flagging for the Discussion section.

Now I'm drafting the Discussion to carefully distinguish between what the data shows: the core finding is that conflict signals are detectable at layer 28 in Llama with high accuracy, but steering at that layer has no behavioral effect, whereas layer 13 shows the actual causal influence on the model's responses with strong statistical significance. This layer dissociation is the key insight—the representation of conflict is most linearly separable late in the network, but the actual computation that drives behavior happens much earlier.

The asymmetry in cross-lingual probe transfer—Chinese-trained probes generalizing better to English than vice versa—initially seemed like it might reveal something fundamental about how conflict is encoded across languages, but the XNLI baseline comparison suggests a different explanation.

When I look at probes trained on non-conflict distinctions like entailment versus contradiction, they exhibit the same directional asymmetry at nearly identical magnitudes, with overlapping confidence intervals. This means the asymmetry isn't specific to conflict representation but rather reflects the model's underlying geometry: English-dominant models allow Chinese representations to project more cleanly onto English space than the reverse. This aligns with prior findings on English-centric latent spaces and cross-lingual alignment patterns, which suggests that any future cross-lingual probing work needs to validate transfer asymmetries against non-conflict baselines to avoid attributing general geometric properties to task-specific phenomena.

Now I'm examining the non-linear encoding patterns, where MLP probes show some suggestive but inconclusive gains... linear probes on the conflict task than on XNLI for cross-lingual transfer (EN→ZH) in both models—a direction consistent with conflict-specific non-linear structure. However, bootstrap confidence intervals include zero in both cases (Llama +5.2 pp, CI [−2.2, +12.9]; Qwen +3.8 pp, CI [−3.6, +11.3]), and we report this as a directional trend rather than a confirmed finding. The absence of a significant non-linear component is itself informative: it indicates that the conflict signal captured by cross-lingual probes is predominantly linear, consistent with the sufficiency of logistic regression probes for cross-lingual semantic classification (Belinkov, 2022).

**P4: Steering model-specificity**

The causal steering result holds up well in Llama-3.1-8B-Instruct at layer 13 with clear bidirectional effects, but when I run the same experiment on Qwen3-8B at equivalent relative depths, I don't see significant steering effects. This model-specificity doesn't undermine the detection–decision dissociation we found—both models show the absence of late-layer causal effects—but it does limit how broadly we can apply mid-layer steering as an intervention. The difference likely stems from architectural variations in how conflict resolution is distributed across layers, such as differences in layer normalization, attention mechanisms, or the language distributions used during pre-training. The fact that causal interventions are model-specific is actually revealing: it suggests that mechanistic interpretability findings may not generalize across architectures the way probing results do, and each model architecture probably needs its own causal validation.

**P5: Broader implications**

These results advance both our understanding of cross-lingual knowledge conflicts and the methodology of cross-lingual probing. Zhao et al. (2026) demonstrated that in entity-centric factual conflicts, linguistic affinity determines which answer the model selects. Our analysis offers a partial mechanistic explanation: conflict signals live in the model's shared multilingual representation space and inherit its directional biases, which favor English in English-dominant models. The confound exclusion pipeline we developed—combining translation quality stratification, token overlap analysis, and non-conflict baseline comparison—fills methodological gaps relevant to any cross-lingual probing study. The detection–decision dissociation has practical consequences for controlling model behavior: targeting the layer where a signal is most detectable might miss the computational stage where the actual decision happens.

Now I need to rewrite the next thinking (P5 continuation) in 1-3 sentences, maintaining the academic tone and avoiding repetition of what's already in the current rewritten thinking.

Our mechanistic findings align with Zhao et al.'s behavioral observations while providing a layer-by-layer account of how conflict resolution unfolds. The methodological framework we've developed—particularly the confound exclusion pipeline—generalizes beyond this specific task and should improve the rigor of future cross-lingual probing work. The detection–decision dissociation underscores a critical distinction for intervention design: identifying where a signal is encoded is not the same as identifying where it drives behavior, a principle that extends beyond cross-lingual settings to any mechanistic study of model decision-making. I'm checking that "consistent with" is being used correctly to reference prior work rather than claiming repeated observations across models. Now I need to add proper LaTeX citations using the paper's existing format and write out both files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "17d06bf7-8f37-4bf0-977e-5be3b1b97a0b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSTJW9cV3Bp297X6e31n5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2168,
      "cache_read_input_tokens": 46032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2168
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 37_

Now writing both sections based on the existing paper's style, claims, and experimental evidence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "f238c294-fca1-4f91-836b-3f26a08fad96",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSTJW9cV3Bp297X6e31n5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2168,
      "cache_read_input_tokens": 46032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2168
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Write · `toolu_01SwsstQLUnJ6qyvLRGr1EW4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md",
  "content": "# Abstract Draft\n\n> ~200 words | Ready for LaTeX integration\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation influences which answer prevails, yet the internal encoding of this conflict signal has not been studied beyond monolingual settings. We probe the residual stream representations of two architecturally distinct LLMs (Llama-3.1-8B-Instruct and Qwen3-8B) and find that knowledge conflict signals are linearly detectable both within and across languages, with balanced accuracy reaching 75--77\\% and all cross-lingual transfer directions exceeding chance. Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese representations transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry, however, is not conflict-specific---probes trained on a non-conflict semantic task (XNLI) show the same pattern at comparable magnitude---indicating that conflict signals inherit the directional biases of the model's general cross-lingual representations. Representation steering reveals a further dissociation: the detectable signal peaks at late layers (~88\\% depth), but causal influence on conflict resolution is confined to a mid-layer (~41\\% depth; Fisher $p = 0.002$) in Llama, with all late-layer interventions producing no behavioral change. These findings demonstrate that cross-lingual conflict detection operates within shared multilingual representation space, and that linear detectability does not imply causal relevance at the same computational stage.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "d9f255a9-60d2-4679-943d-22746feba3c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSTJW9cV3Bp297X6e31n5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2168,
      "cache_read_input_tokens": 46032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2168
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-22T15:38:42.200Z_

<details><summary>↩ Tool result · `toolu_01SwsstQLUnJ6qyvLRGr1EW4`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "9bbda8a1-24e0-41ae-b8a2-838042d8eef3",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/abstract_draft.md",
    "content": "# Abstract Draft\n\n> ~200 words | Ready for LaTeX integration\n\nWhen multilingual large language models (LLMs) encounter conflicting information across languages, the language of presentation influences which answer prevails, yet the internal encoding of this conflict signal has not been studied beyond monolingual settings. We probe the residual stream representations of two architecturally distinct LLMs (Llama-3.1-8B-Instruct and Qwen3-8B) and find that knowledge conflict signals are linearly detectable both within and across languages, with balanced accuracy reaching 75--77\\% and all cross-lingual transfer directions exceeding chance. Cross-lingual transfer exhibits a directional asymmetry: probes trained on Chinese representations transfer to English approximately 7 percentage points more accurately than the reverse. This asymmetry, however, is not conflict-specific---probes trained on a non-conflict semantic task (XNLI) show the same pattern at comparable magnitude---indicating that conflict signals inherit the directional biases of the model's general cross-lingual representations. Representation steering reveals a further dissociation: the detectable signal peaks at late layers (~88\\% depth), but causal influence on conflict resolution is confined to a mid-layer (~41\\% depth; Fisher $p = 0.002$) in Llama, with all late-layer interventions producing no behavioral change. These findings demonstrate that cross-lingual conflict detection operates within shared multilingual representation space, and that linear detectability does not imply causal relevance at the same computational stage.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Write · `toolu_01H48ktxyGyR3kjfFVFMr25j`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md",
  "content": "# Discussion Draft\n\n> 5 paragraphs | LaTeX citations use \\citep{}/\\citet{} matching existing sections\n\n## Detection Does Not Imply Decision\n\nThe central finding of our causal analysis is the layer dissociation between where conflict signals are detectable and where they influence behavior. Probing accuracy for Llama peaks at layer 28 (88\\% depth), where the model's representation of the conflict outcome is most linearly separable. Yet steering at this layer produces no significant behavioral change (Fisher $p > 0.3$). Causal influence instead resides at layer 13 (41\\% depth), where perturbations along the probe direction shift the model's answer between contextual and parametric responses in both directions (Fisher $p = 0.002$ and $p < 0.001$). This pattern suggests that conflict resolution is computed at intermediate layers, and the late-layer signal is a post-hoc encoding of a decision already formed upstream. The mid-layer locus aligns with prior work showing that language-independent representations emerge at intermediate depths in multilingual models \\citep{muller2021first, wendler2024llamas}, suggesting that conflict resolution and cross-lingual alignment share a computational stage. From a methodological standpoint, this result reinforces the caution of \\citet{basu2026interpretability}: probe accuracy alone is an unreliable guide for selecting intervention targets, and steering experiments restricted to the probing peak can produce false negatives about the causal role of detected signals.\n\n## Asymmetry as a General Cross-Lingual Property\n\nThe directional asymmetry in cross-lingual transfer---where Chinese-trained probes transfer to English more accurately than the reverse by approximately 7 percentage points---initially appeared to reveal something specific about how conflict signals are organized across languages. The XNLI baseline reframes this interpretation. Probes trained on a non-conflict semantic distinction (entailment versus contradiction) show the same asymmetry at comparable magnitude (Llama $+6.0$ pp, Qwen $+6.7$ pp), with confidence intervals that overlap substantially with those of the conflict task (Llama $+7.2$ pp, Qwen $+7.2$ pp). The asymmetry is therefore not a property of conflict encoding but of the model's representational geometry: in English-dominant models, Chinese representations project more readily onto English subspace than the reverse. This connects to the English-centric latent space documented by \\citet{wendler2024llamas} and the cross-lingual alignment asymmetries measured by \\citet{kargaran2024mexa}. For cross-lingual probing studies more broadly, any observed transfer asymmetry must be benchmarked against a non-conflict baseline before being attributed to the phenomenon under investigation.\n\n## Non-Linear Encoding: A Directional Trend\n\nWe observe a suggestive but inconclusive pattern in non-linear encoding. MLP probes show larger gains over linear probes on the conflict task than on XNLI for cross-lingual transfer (EN$\\to$ZH) in both models---a direction that would be expected if conflict signals contained task-specific non-linear structure. However, bootstrap confidence intervals include zero in both cases (Llama $+5.2$ pp, CI [$-2.2$, $+12.9$]; Qwen $+3.8$ pp, CI [$-3.6$, $+11.3$]), and we report this as a directional trend rather than a confirmed finding. The absence of a significant non-linear component is itself informative: it indicates that the conflict signal captured by cross-lingual probes is predominantly linear, consistent with the sufficiency of logistic regression probes for cross-lingual semantic classification \\citep{belinkov2022probing}.\n\n## Model-Specificity of Causal Interventions\n\nThe causal steering result is supported by Llama-3.1-8B-Instruct, where layer 13 shows robust bidirectional effects that survive Bonferroni correction. Analogous experiments on Qwen3-8B at comparable relative depths (layers 14 and 23) yield no significant steering effects. This model-specificity does not invalidate the detection--decision dissociation---the absence of late-layer causal effects holds in both models---but it constrains the generality of mid-layer steering as an intervention strategy. The difference may reflect architectural factors that affect how conflict resolution is distributed across layers, such as differences in layer normalization, attention mechanisms, or pre-training language distributions. Model-specificity of causal interventions is itself an informative result: it suggests that mechanistic interpretability findings may not transfer across architectures as readily as probing patterns do, and that each model family may require independent causal validation even when probing results are qualitatively similar.\n\n## Broader Implications\n\nThese results contribute to both the understanding of cross-lingual knowledge conflicts and the methodology of cross-lingual probing. \\citet{zhao2026when} showed that in entity-centric factual conflicts, linguistic affinity determines which answer the model selects. Our analysis provides a partial mechanistic account: conflict signals are encoded in the model's shared multilingual representation space and inherit its directional biases, which in English-dominant models favor the English direction. The confound exclusion pipeline---combining translation quality stratification, token overlap analysis, and non-conflict baseline comparison---addresses methodological gaps that apply to any cross-lingual probing study where translation artifacts or general transfer properties could be mistaken for task-specific phenomena. The detection--decision dissociation carries practical implications for work on controlling model behavior in multilingual settings: interventions targeting the layer where a signal is most detectable may miss the computational stage where the decision is formed, and mid-layer representations deserve priority as intervention targets in future work.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "ede0e357-52bb-4a87-8a1c-91e1e1873ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HSTJW9cV3Bp297X6e31n5q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2168,
      "cache_read_input_tokens": 46032,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2168
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T15:38:56.153Z_

<details><summary>↩ Tool result · `toolu_01H48ktxyGyR3kjfFVFMr25j`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "d4d707cf-98c1-48aa-aca5-255b9ada3008",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/discussion_draft.md",
    "content": "# Discussion Draft\n\n> 5 paragraphs | LaTeX citations use \\citep{}/\\citet{} matching existing sections\n\n## Detection Does Not Imply Decision\n\nThe central finding of our causal analysis is the layer dissociation between where conflict signals are detectable and where they influence behavior. Probing accuracy for Llama peaks at layer 28 (88\\% depth), where the model's representation of the conflict outcome is most linearly separable. Yet steering at this layer produces no significant behavioral change (Fisher $p > 0.3$). Causal influence instead resides at layer 13 (41\\% depth), where perturbations along the probe direction shift the model's answer between contextual and parametric responses in both directions (Fisher $p = 0.002$ and $p < 0.001$). This pattern suggests that conflict resolution is computed at intermediate layers, and the late-layer signal is a post-hoc encoding of a decision already formed upstream. The mid-layer locus aligns with prior work showing that language-independent representations emerge at intermediate depths in multilingual models \\citep{muller2021first, wendler2024llamas}, suggesting that conflict resolution and cross-lingual alignment share a computational stage. From a methodological standpoint, this result reinforces the caution of \\citet{basu2026interpretability}: probe accuracy alone is an unreliable guide for selecting intervention targets, and steering experiments restricted to the probing peak can produce false negatives about the causal role of detected signals.\n\n## Asymmetry as a General Cross-Lingual Property\n\nThe directional asymmetry in cross-lingual transfer---where Chinese-trained probes transfer to English more accurately than the reverse by approximately 7 percentage points---initially appeared to reveal something specific about how conflict signals are organized across languages. The XNLI baseline reframes this interpretation. Probes trained on a non-conflict semantic distinction (entailment versus contradiction) show the same asymmetry at comparable magnitude (Llama $+6.0$ pp, Qwen $+6.7$ pp), with confidence intervals that overlap substantially with those of the conflict task (Llama $+7.2$ pp, Qwen $+7.2$ pp). The asymmetry is therefore not a property of conflict encoding but of the model's representational geometry: in English-dominant models, Chinese representations project more readily onto English subspace than the reverse. This connects to the English-centric latent space documented by \\citet{wendler2024llamas} and the cross-lingual alignment asymmetries measured by \\citet{kargaran2024mexa}. For cross-lingual probing studies more broadly, any observed transfer asymmetry must be benchmarked against a non-conflict baseline before being attributed to the phenomenon under investigation.\n\n## Non-Linear Encoding: A Directional Trend\n\nWe observe a suggestive but inconclusive pattern in non-linear encoding. MLP probes show larger gains over linear probes on the conflict task than on XNLI for cross-lingual transfer (EN$\\to$ZH) in both models---a direction that would be expected if conflict signals contained task-specific non-linear structure. However, bootstrap confidence intervals include zero in both cases (Llama $+5.2$ pp, CI [$-2.2$, $+12.9$]; Qwen $+3.8$ pp, CI [$-3.6$, $+11.3$]), and we report this as a directional trend rather than a confirmed finding. The absence of a significant non-linear component is itself informative: it indicates that the conflict signal captured by cross-lingual probes is predominantly linear, consistent with the sufficiency of logistic regression probes for cross-lingual semantic classification \\citep{belinkov2022probing}.\n\n## Model-Specificity of Causal Interventions\n\nThe causal steering result is supported by Llama-3.1-8B-Instruct, where layer 13 shows robust bidirectional effects that survive Bonferroni correction. Analogous experiments on Qwen3-8B at comparable relative depths (layers 14 and 23) yield no significant steering effects. This model-specificity does not invalidate the detection--decision dissociation---the absence of late-layer causal effects holds in both models---but it constrains the generality of mid-layer steering as an intervention strategy. The difference may reflect architectural factors that affect how conflict resolution is distributed across layers, such as differences in layer normalization, attention mechanisms, or pre-training language distributions. Model-specificity of causal interventions is itself an informative result: it suggests that mechanistic interpretability findings may not transfer across architectures as readily as probing patterns do, and that each model family may require independent causal validation even when probing results are qualitatively similar.\n\n## Broader Implications\n\nThese results contribute to both the understanding of cross-lingual knowledge conflicts and the methodology of cross-lingual probing. \\citet{zhao2026when} showed that in entity-centric factual conflicts, linguistic affinity determines which answer the model selects. Our analysis provides a partial mechanistic account: conflict signals are encoded in the model's shared multilingual representation space and inherit its directional biases, which in English-dominant models favor the English direction. The confound exclusion pipeline---combining translation quality stratification, token overlap analysis, and non-conflict baseline comparison---addresses methodological gaps that apply to any cross-lingual probing study where translation artifacts or general transfer properties could be mistaken for task-specific phenomena. The detection--decision dissociation carries practical implications for work on controlling model behavior in multilingual settings: interventions targeting the layer where a signal is most detectable may miss the computational stage where the decision is formed, and mid-layer representations deserve priority as intervention targets in future work.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 42_

两个文件已写入：

**Abstract** (~200 词)
- 结构：现象（跨语言冲突内部机制未知）→ 方法（残差流探针 + 跨语言迁移 + steering）→ 三个核心发现（检测 75-77%、不对称性继承通用跨语言属性、Detection ≠ Decision）→ 结论
- Steering 结果限定为 "in Llama"，未过度泛化
- 未使用 "consistently"

**Discussion** (5 段)
1. **Detection ≠ Decision** — L13 因果 vs L28 检测峰值，连接 mid-layer 跨语言对齐文献，引用 Basu 方法论警告
2. **不对称性是通用属性** — XNLI 对照数据（+6.0/+6.7 pp vs +7.2/+7.2 pp），CI 重叠，连接 Wendler & Kargaran
3. **非线性作为 observation** — MLP gains 方向对但 CI 含零，用 "directional trend" 定性
4. **Steering 的 model-specificity** — Llama 成功 Qwen 失败，框架为 "mechanistic results 跨架构迁移性本身是有意义的发现"
5. **Broader implications** — 连接 CLEAR，方法论贡献（confound pipeline），detection-decision dissociation 的实践意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "uuid": "212c0c41-6180-4f2c-8edf-9953ad0948b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013cMSUriVAu8cDy3XBVWBKU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8428,
      "cache_read_input_tokens": 48200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8428
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 43_

两个文件已写入：

**Abstract** (~200 词)
- 结构：现象（跨语言冲突内部机制未知）→ 方法（残差流探针 + 跨语言迁移 + steering）→ 三个核心发现（检测 75-77%、不对称性继承通用跨语言属性、Detection ≠ Decision）→ 结论
- Steering 结果限定为 "in Llama"，未过度泛化
- 未使用 "consistently"

**Discussion** (5 段)
1. **Detection ≠ Decision** — L13 因果 vs L28 检测峰值，连接 mid-layer 跨语言对齐文献，引用 Basu 方法论警告
2. **不对称性是通用属性** — XNLI 对照数据（+6.0/+6.7 pp vs +7.2/+7.2 pp），CI 重叠，连接 Wendler & Kargaran
3. **非线性作为 observation** — MLP gains 方向对但 CI 含零，用 "directional trend" 定性
4. **Steering 的 model-specificity** — Llama 成功 Qwen 失败，框架为 "mechanistic results 跨架构迁移性本身是有意义的发现"
5. **Broader implications** — 连接 CLEAR，方法论贡献（confound pipeline），detection-decision dissociation 的实践意义

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 182826,
  "duration_api_ms": 183942,
  "num_turns": 15,
  "stop_reason": "end_turn",
  "session_id": "aabb56ba-d9b2-4041-96b4-b1211227826e",
  "total_cost_usd": 0.66972075,
  "usage": {
    "input_tokens": 11,
    "cache_creation_input_tokens": 44787,
    "cache_read_input_tokens": 273938,
    "output_tokens": 10035,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44787,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 411,
        "cache_read_input_tokens": 48200,
        "cache_creation_input_tokens": 8428,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 8428
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1808,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001903,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 11,
      "outputTokens": 10035,
      "cacheReadInputTokens": 273938,
      "cacheCreationInputTokens": 44787,
      "webSearchRequests": 0,
      "costUSD": 0.66781775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c6537705-a37f-4345-a166-b275b1dcd2be"
}
```

</details>

---
