# paper write conclusion limitations

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_paper_write-conclusion-limitations_20260522T155221.log`
- **Structured JSON:** [`d0241ca7d9d02204cb6c.json`](../../sessions/d0/d0241ca7d9d02204cb6c.json)

## Before a recorded user message

18 recorded events

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
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
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
  "uuid": "5c768c4c-7746-4e01-9aaa-16aee1fdeebb",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-prod42-projects-clkc-mech-interp/memory/"
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
  "uuid": "a62a3c35-cff4-4794-833f-88b2f630e0a3",
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the existing introduction to understand the writing style, then draft the Conclusion and Limitations sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "1fd7aed1-9207-4498-9bc9-e10b0f849e43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQtbp4E4Dx6f86CZX2PSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
      },
      "output_tokens": 30,
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

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_01WS34V8bayBjJJz6kuVxEkm`</summary>

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
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "719e86ca-0a3c-44cd-b40d-2e162b925fbb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQtbp4E4Dx6f86CZX2PSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
      },
      "output_tokens": 30,
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

_source line 6 · 2026-05-22T15:52:31.693Z_

<details><summary>↩ Tool result · `toolu_01WS34V8bayBjJJz6kuVxEkm`</summary>

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
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "080202db-54c2-4435-a5c9-6405e68eb320",
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

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01Mc8CGurgQWMaHBFpTU2rSm`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/",
  "description": "List paper sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "d00a8681-5f96-4ce7-9e79-63be0db1c220",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AQtbp4E4Dx6f86CZX2PSJo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12291,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12291
      },
      "output_tokens": 30,
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

_source line 8 · 2026-05-22T15:52:32.439Z_

<details><summary>↩ Tool result · `toolu_01Mc8CGurgQWMaHBFpTU2rSm`</summary>

```text
discussion.tex
experiments.tex
introduction.tex
method.tex
related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "103889f5-8e8f-418b-857c-6f44e41386bf",
  "tool_use_result": {
    "stdout": "discussion.tex\nexperiments.tex\nintroduction.tex\nmethod.tex\nrelated_work.tex",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_01XLvVJiEoMWAw4QpyxEdUW9`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "b67bf0ea-7a5a-4fde-b417-c213f2ff3dcb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NymRGjbKNGKXm72SiomGmu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1604,
      "cache_read_input_tokens": 24132,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1604
      },
      "output_tokens": 65,
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

_source line 10 · 2026-05-22T15:52:34.882Z_

<details><summary>↩ Tool result · `toolu_01XLvVJiEoMWAw4QpyxEdUW9`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Detection and decision occur at different layers.}
5	Our central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.
6	In Llama, probe accuracy on EN$\to$EN peaks at layer~28 (88\% depth), yet representation steering succeeds only at layer~13 (41\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).
7	This dissociation has a cross-lingual counterpart: the Llama ZH$\to$ZH probe peaks at L13, the same layer where steering succeeds.
8	Mid-layers thus serve a dual role as the site of cross-lingual alignment \citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.
9	The EN$\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.
10	A practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.
11	Cross-layer sweeps, as conducted here, are necessary to locate the true decision point.
12	
13	\paragraph{Conflict signals are encoded in a general cross-lingual space.}
14	The XNLI baseline comparison reveals that the ZH$\to$EN transfer advantage ($+6.0$ and $+6.7$~pp for Llama and Qwen) closely matches the conflict task asymmetry ($+7.2$~pp for both models), with substantially overlapping confidence intervals.
15	The asymmetry is therefore not conflict-specific; conflict detection piggybacks on the model's pre-existing cross-lingual alignment structure.
16	This interpretation connects to the linguistic affinity effects reported by \citet{zhao2026when}: the CLEAR benchmark found that conflict resolution preferences vary by language pair, a pattern that may inherit from the quality of underlying representational alignment documented by \citet{kargaran2024mexa} and \citet{wendler2024llamas}.
17	Any cross-lingual probing study must account for this baseline asymmetry before attributing transfer differences to task-specific phenomena.
18	
19	\paragraph{Relation to interpretability without actionability.}
20	\citet{basu2026interpretability} reported that steering failed in clinical NLP tasks despite near-perfect probe accuracy (98.2\% AUROC).
21	Our results present a partial contrast: mid-layer steering in knowledge conflict tasks succeeds with a weaker probe signal.
22	A key difference is layer selection.
23	\citeauthor{basu2026interpretability} evaluated steering at layers selected for probe accuracy; our analysis shows that the layer with highest probe accuracy (L28) also fails to steer, and causal influence is found only at L13.
24	Task characteristics may also contribute: knowledge conflict resolution involves a discrete choice between two competing answer sources, which may concentrate causal structure at a single computational stage.
25	We frame this as a difference in causal influence rather than full causal control, since steering shifts resolution probabilities without fully determining the outcome.
26	
27	\paragraph{A suggestive MLP trend.}
28	When MLP sublayer representations replace full residual stream inputs for EN$\to$ZH probes, the conflict task shows positive MLP gains (Qwen $+3.84$~pp, Llama $+5.21$~pp), while the XNLI baseline yields negative or near-zero gains.
29	However, bootstrap confidence intervals include zero for both models, so this difference does not reach statistical significance.
30	We report it as a suggestive trend: if confirmed with larger samples or additional models, it would indicate that conflict-specific information has a nonlinear component beyond what general semantic representations capture.
31	
32	\paragraph{Scope and forward look.}
33	Our analysis covers one language pair (EN-ZH), two models, and steering experiments on Llama only.
34	These constraints, along with dataset and task limitations, are discussed in \S\ref{sec:limitations}.
35	Extending the steering analysis to Qwen and to typologically diverse language pairs would test whether the detection-decision dissociation generalizes beyond the configurations studied here.
36	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "322f9e43-99ec-4232-b4fb-97226e4464ef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Detection and decision occur at different layers.}\nOur central mechanistic finding is a dissociation between where conflict signals become linearly readable and where they exert causal influence on model behavior.\nIn Llama, probe accuracy on EN$\\to$EN peaks at layer~28 (88\\% depth), yet representation steering succeeds only at layer~13 (41\\% depth; Fisher $p = 0.002$), and all late-layer interventions produce no significant behavioral change ($p > 0.3$).\nThis dissociation has a cross-lingual counterpart: the Llama ZH$\\to$ZH probe peaks at L13, the same layer where steering succeeds.\nMid-layers thus serve a dual role as the site of cross-lingual alignment \\citep{muller2021first, wendler2024llamas} and the locus where conflict signals acquire causal force.\nThe EN$\\to$EN peak at L28 is best understood as a diagnostic readout, a linearly readable trace of a decision that has already been made upstream.\nA practical implication follows: the probe peak layer is not the causal layer, and intervention experiments that target only the highest-accuracy layer risk missing the computationally relevant site.\nCross-layer sweeps, as conducted here, are necessary to locate the true decision point.\n\n\\paragraph{Conflict signals are encoded in a general cross-lingual space.}\nThe XNLI baseline comparison reveals that the ZH$\\to$EN transfer advantage ($+6.0$ and $+6.7$~pp for Llama and Qwen) closely matches the conflict task asymmetry ($+7.2$~pp for both models), with substantially overlapping confidence intervals.\nThe asymmetry is therefore not conflict-specific; conflict detection piggybacks on the model's pre-existing cross-lingual alignment structure.\nThis interpretation connects to the linguistic affinity effects reported by \\citet{zhao2026when}: the CLEAR benchmark found that conflict resolution preferences vary by language pair, a pattern that may inherit from the quality of underlying representational alignment documented by \\citet{kargaran2024mexa} and \\citet{wendler2024llamas}.\nAny cross-lingual probing study must account for this baseline asymmetry before attributing transfer differences to task-specific phenomena.\n\n\\paragraph{Relation to interpretability without actionability.}\n\\citet{basu2026interpretability} reported that steering failed in clinical NLP tasks despite near-perfect probe accuracy (98.2\\% AUROC).\nOur results present a partial contrast: mid-layer steering in knowledge conflict tasks succeeds with a weaker probe signal.\nA key difference is layer selection.\n\\citeauthor{basu2026interpretability} evaluated steering at layers selected for probe accuracy; our analysis shows that the layer with highest probe accuracy (L28) also fails to steer, and causal influence is found only at L13.\nTask characteristics may also contribute: knowledge conflict resolution involves a discrete choice between two competing answer sources, which may concentrate causal structure at a single computational stage.\nWe frame this as a difference in causal influence rather than full causal control, since steering shifts resolution probabilities without fully determining the outcome.\n\n\\paragraph{A suggestive MLP trend.}\nWhen MLP sublayer representations replace full residual stream inputs for EN$\\to$ZH probes, the conflict task shows positive MLP gains (Qwen $+3.84$~pp, Llama $+5.21$~pp), while the XNLI baseline yields negative or near-zero gains.\nHowever, bootstrap confidence intervals include zero for both models, so this difference does not reach statistical significance.\nWe report it as a suggestive trend: if confirmed with larger samples or additional models, it would indicate that conflict-specific information has a nonlinear component beyond what general semantic representations capture.\n\n\\paragraph{Scope and forward look.}\nOur analysis covers one language pair (EN-ZH), two models, and steering experiments on Llama only.\nThese constraints, along with dataset and task limitations, are discussed in \\S\\ref{sec:limitations}.\nExtending the steering analysis to Qwen and to typologically diverse language pairs would test whether the detection-decision dissociation generalizes beyond the configurations studied here.\n",
      "numLines": 36,
      "startLine": 1,
      "totalLines": 36
    }
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good sense of the writing style. Let me draft the Conclusion and Limitations sections.

Key style notes from the intro and discussion:
- Direct, precise language
- No fluff words
- Specific numbers when relevant
- Academic but not pompous
- No "novel", "groundbreaking", etc.
- Clean sentence structure

Let me write both sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "8d35f5ba-5644-4c0e-b010-5ddb1ea4d5f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DH6UqvJfSvk3Yw8k6WJEfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 25736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1155
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

_source line 12_

风格已确认。现在写两个章节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "2d6c80ca-8691-479c-b106-bd10ff59b10e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DH6UqvJfSvk3Yw8k6WJEfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 25736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1155
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

_source line 13_

<details open><summary>🔧 Tool call — Write · `toolu_012F6SiapgNCQqsYkswtxcpR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/conclusion_draft.md",
  "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a mechanistic analysis of cross-lingual knowledge conflicts in multilingual LLMs, combining residual stream probing with representation steering across Llama-3.1-8B-Instruct and Qwen3-8B.\nOur results establish three findings: conflict signals are linearly detectable in residual stream representations and transfer across languages via the model's general cross-lingual representational space, not through a conflict-specific encoding mechanism; the transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) mirrors a baseline asymmetry observed in non-conflict tasks, attributing it to structural properties of English-dominant models; and a detection--decision layer dissociation places the causal node at mid-layers (${\\sim}$41\\% depth), upstream of the late-layer probing peak where the conflict outcome becomes linearly readable but is no longer causally relevant.\nThe confound exclusion pipeline---COMET translation quality stratification, token overlap analysis, and non-conflict baseline comparison---provides a reusable methodological template for cross-lingual probing studies.\nFuture work should extend these analyses to typologically diverse language pairs and additional model families to test whether the detection--decision dissociation holds more broadly.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "a6b3b4f1-1594-4236-849c-9d20c473079e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DH6UqvJfSvk3Yw8k6WJEfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 25736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1155
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

_source line 14 · 2026-05-22T15:52:45.895Z_

<details><summary>↩ Tool result · `toolu_012F6SiapgNCQqsYkswtxcpR`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/conclusion_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "7f849f8d-96ee-47da-aff9-5ff8200fb2ca",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/conclusion_draft.md",
    "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented a mechanistic analysis of cross-lingual knowledge conflicts in multilingual LLMs, combining residual stream probing with representation steering across Llama-3.1-8B-Instruct and Qwen3-8B.\nOur results establish three findings: conflict signals are linearly detectable in residual stream representations and transfer across languages via the model's general cross-lingual representational space, not through a conflict-specific encoding mechanism; the transfer asymmetry (ZH$\\to$EN $>$ EN$\\to$ZH by ${\\sim}$7~pp) mirrors a baseline asymmetry observed in non-conflict tasks, attributing it to structural properties of English-dominant models; and a detection--decision layer dissociation places the causal node at mid-layers (${\\sim}$41\\% depth), upstream of the late-layer probing peak where the conflict outcome becomes linearly readable but is no longer causally relevant.\nThe confound exclusion pipeline---COMET translation quality stratification, token overlap analysis, and non-conflict baseline comparison---provides a reusable methodological template for cross-lingual probing studies.\nFuture work should extend these analyses to typologically diverse language pairs and additional model families to test whether the detection--decision dissociation holds more broadly.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Write · `toolu_01LMdrv3m7qo8DiEZz5tgJr5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/limitations_draft.md",
  "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nOur analysis has three main limitations in scope.\nFirst, the probing and steering experiments focus primarily on the English--Chinese language pair, with German serving only as supplementary evidence for cross-lingual transfer; whether the detection--decision dissociation and transfer asymmetry patterns hold for typologically distant pairs (e.g., English--Japanese, English--Arabic) remains to be verified.\nSecond, we evaluate two model families (Llama-3.1-8B-Instruct and Qwen3-8B), which limits the generality of architectural conclusions; in particular, the causal steering intervention succeeded only in Llama at layer~13, and we cannot confirm whether the mid-layer causal node exists at comparable depth in Qwen or other architectures.\nThird, our conflict dataset is constructed from entity-centric factual statements following \\citet{zhao2026when}, and the findings may not extend to other conflict types such as opinion-based or temporally contingent contradictions.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "57fd5bf9-ed5e-4a44-8d10-694abd361ad1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DH6UqvJfSvk3Yw8k6WJEfS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1155,
      "cache_read_input_tokens": 25736,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1155
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

_source line 16 · 2026-05-22T15:52:51.533Z_

<details><summary>↩ Tool result · `toolu_01LMdrv3m7qo8DiEZz5tgJr5`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/limitations_draft.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "8960e78c-ce04-46f5-8a29-5cce096dd461",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-prod42/projects/clkc_mech_interp/artifacts/limitations_draft.md",
    "content": "\\section{Limitations}\n\\label{sec:limitations}\n\nOur analysis has three main limitations in scope.\nFirst, the probing and steering experiments focus primarily on the English--Chinese language pair, with German serving only as supplementary evidence for cross-lingual transfer; whether the detection--decision dissociation and transfer asymmetry patterns hold for typologically distant pairs (e.g., English--Japanese, English--Arabic) remains to be verified.\nSecond, we evaluate two model families (Llama-3.1-8B-Instruct and Qwen3-8B), which limits the generality of architectural conclusions; in particular, the causal steering intervention succeeded only in Llama at layer~13, and we cannot confirm whether the mid-layer causal node exists at comparable depth in Qwen or other architectures.\nThird, our conflict dataset is constructed from entity-centric factual statements following \\citet{zhao2026when}, and the findings may not extend to other conflict types such as opinion-based or temporally contingent contradictions.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 17_

已写入：

- **Conclusion** (`conclusion_draft.md`): 4句。第1句定位工作，第2句三个核心发现（detectability + general transfer pathway + detection-decision dissociation），第3句方法论贡献（confound exclusion pipeline），第4句未来方向。
- **Limitations** (`limitations_draft.md`): 4句覆盖3个点——language pair coverage (EN-ZH为主, DE补充)、model coverage (2个模型家族, steering仅Llama成功)、dataset scope (entity-centric factual conflicts)。

注意：Limitations 第3点我用了 dataset/conflict type scope 替代了你原始列表中的第3点（steering model-specificity），因为 steering 的局限性已经自然融入了第2点 model coverage 中（"causal steering intervention succeeded only in Llama at layer 13"）。这样避免重复，同时补上了一个 reviewers 更可能关注的 dataset scope 限制。如需调整回原始3点结构，告诉我。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "uuid": "8badb404-6609-4c35-817c-4c03ff233bf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xu5bk4sDyJRsWQ5pzZJoPq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 964,
      "cache_read_input_tokens": 26891,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 964
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

_source line 18_

已写入：

- **Conclusion** (`conclusion_draft.md`): 4句。第1句定位工作，第2句三个核心发现（detectability + general transfer pathway + detection-decision dissociation），第3句方法论贡献（confound exclusion pipeline），第4句未来方向。
- **Limitations** (`limitations_draft.md`): 4句覆盖3个点——language pair coverage (EN-ZH为主, DE补充)、model coverage (2个模型家族, steering仅Llama成功)、dataset scope (entity-centric factual conflicts)。

注意：Limitations 第3点我用了 dataset/conflict type scope 替代了你原始列表中的第3点（steering model-specificity），因为 steering 的局限性已经自然融入了第2点 model coverage 中（"causal steering intervention succeeded only in Llama at layer 13"）。这样避免重复，同时补上了一个 reviewers 更可能关注的 dataset scope 限制。如需调整回原始3点结构，告诉我。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 32687,
  "duration_api_ms": 33416,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "7b4f045e-10fd-4001-a289-1db688a86352",
  "total_cost_usd": 0.1814115,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 16014,
    "cache_read_input_tokens": 88600,
    "output_tokens": 1412,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 16014,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 285,
        "cache_read_input_tokens": 26891,
        "cache_creation_input_tokens": 964,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 964
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1599,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001699,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 1412,
      "cacheReadInputTokens": 88600,
      "cacheCreationInputTokens": 16014,
      "webSearchRequests": 0,
      "costUSD": 0.1797125,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b936677d-24a8-4a42-86e3-236272b7ea1c"
}
```

</details>

---
