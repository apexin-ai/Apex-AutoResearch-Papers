# paper abstract intro binary update

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_paper_abstract-intro-binary-update_20260515T162541.log`
- **Structured JSON:** [`135c14c7c5d19534c0bc.json`](../../sessions/13/135c14c7c5d19534c0bc.json)

## Before a recorded user message

35 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint",
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
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
  "uuid": "79f2f288-b4d5-44cd-a3dd-c6ce034b86f2",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778878800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "206248c5-ccec-4a09-93b2-51514c4667ec",
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274"
}
```

---

### Assistant

_source line 4_

Let me read the current abstract and introduction files first.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "71d3b67f-9a44-4d99-9d04-70f113e4fa08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EprKga3e5HRSPiVnUZffi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12270,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12270
      },
      "output_tokens": 2,
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

<details open><summary>🔧 Tool call — Read · `toolu_019apmi1aeKUtEXxiDmNshgn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "28c9acfd-4749-4e01-a8e5-7ae52370cea0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EprKga3e5HRSPiVnUZffi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12270,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12270
      },
      "output_tokens": 2,
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

_source line 6 · 2026-05-15T16:25:50.215Z_

<details><summary>↩ Tool result · `toolu_019apmi1aeKUtEXxiDmNshgn`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\ gen-2+ depth discrimination ($p < 0.001$ vs.\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "9559fbde-f66c-4dd8-bb4f-a4bfc62ae09f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
      "content": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).\nIn our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01Qb3WRGUjXtsyNQwTmcgcCJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "00f96966-4941-419e-ab52-902cacc2d4e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EprKga3e5HRSPiVnUZffi7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12270,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12270
      },
      "output_tokens": 2,
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

_source line 8 · 2026-05-15T16:25:50.511Z_

<details><summary>↩ Tool result · `toolu_01Qb3WRGUjXtsyNQwTmcgcCJ`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.
5	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
6	The result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.
7	
8	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
9	This conflates qualitatively different material.
10	A first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.
11	A third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.
12	Treating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.
13	
14	We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
15	We refer to the overall framework---features, classifier, and evaluation protocol---as \emph{depth fingerprinting}, distinguishing the method from the task it addresses.
16	No existing method addresses this task directly in non-paraphrastic continuation chains.
17	When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
18	Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
19	These results do not extend to \emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.
20	We focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).
21	
22	We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).
23	We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
24	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
25	The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator consistency (std\,=\,0.051).
26	
27	We also report a negative finding.
28	Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\ 2.387 depth-stratified).
29	In our experimental setting, depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data selection.
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.
34	    \item \textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\,=\,0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\,=\,0.051).
35	    \item \textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.
36	\end{enumerate}
37	
38	The remainder of this paper is organized as follows.
39	\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
40	\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
41	\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
42	\S\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "89ca57fe-70b1-4d15-ae95-86fd5180e68e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now I need to understand the current state and what needs to change:

Current abstract mentions:
- "binary macro-F1 of 0.72" — needs to be updated to 0.723 with CI
- "6 generators from 3 model families (0.6B--8.2B parameters)"
- "per-generator consistency (std\,=\,0.051)"

Current introduction mentions:
- Line 25: "binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator consistency (std\,=\,0.051)"


- Line 34: "binary F1\,=\,0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+)"

I need to update all instances of 0.72 to 0.723 with the confidence interval [0.717, 0.729]. Looking at the ensemble results, the 7-feature ensemble achieves 0.723, which is what I should be reporting.

For the abstract, I should update line 6 to reflect the precise metric with confidence bounds. The 3-class F1 score of 0.789 isn't mentioned in the abstract since that's about the task formulation rather than a performance claim. My main changes are updating the binary F1 value to 0.723 and adding the confidence interval, plus verifying the scope is clear about which models are being evaluated.

Looking at the specific locations, I need to clarify that we're working with base-model generators throughout. The abstract mentions "6 generators from 3 model families" but should specify these are base-model generators. The introduction already establishes this focus on non-paraphrastic chains from pretrained models, so I'll make sure that terminology is consistent across both sections. I'm identifying where to add "base-model" for clarity—the intro already establishes the scope with "base (pretrained) models" on line 20, so the generator descriptions have context, but I should still add it to the contributions section on line 34 to be explicit about which generators we're testing.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "f944c676-2c38-4419-b302-cb34a9516c03",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWHoWLXrzPoinxZFKDF5CV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 24111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
      },
      "output_tokens": 10,
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

_source line 10_

Current files use "0.72" (rounded). Updating to exact 0.723 with CI, and ensuring "base-model" scope is explicit.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "c575a3a4-bdb7-44d9-8e6b-30f4f44df72d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWHoWLXrzPoinxZFKDF5CV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 24111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
      },
      "output_tokens": 10,
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

_source line 11_

<details open><summary>🔧 Tool call — Edit · `toolu_01CLxieKJTxCJcmcsMnumZfj`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
  "old_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "452e3b45-684f-4b54-a852-18638df154ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWHoWLXrzPoinxZFKDF5CV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 24111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
      },
      "output_tokens": 10,
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

_source line 12 · 2026-05-15T16:26:15.628Z_

<details><summary>↩ Tool result · `toolu_01CLxieKJTxCJcmcsMnumZfj`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "bbdbbb1f-9ebe-4360-bbda-4388b78dab67",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
    "oldString": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).\nIn our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 6,
        "newStart": 3,
        "newLines": 6,
        "lines": [
          " As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.",
          " We formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.",
          " We characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.",
          "-A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
          "+A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
          " In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.",
          " \\end{abstract}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Edit · `toolu_011Ko4cyvRASDtzyktJnuQag`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "old_string": "This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "062acdb3-8eb1-4a67-bd19-c075f69de615",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWHoWLXrzPoinxZFKDF5CV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 24111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
      },
      "output_tokens": 10,
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

_source line 14 · 2026-05-15T16:26:18.052Z_

<details><summary>↩ Tool result · `toolu_011Ko4cyvRASDtzyktJnuQag`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "1eba66e5-9aec-4abd-8aa7-f9331c7c954a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "oldString": "This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).",
          " We characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.",
          " This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.",
          "-The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
          "+The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
          " ",
          " We also report a negative finding.",
          " Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Edit · `toolu_01VAY27pec65Kzme3UsLTvyG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "old_string": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "8cbfbd14-6764-4a18-a7ea-0b3b9e698770",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWHoWLXrzPoinxZFKDF5CV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 24111,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1986
      },
      "output_tokens": 10,
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

_source line 16 · 2026-05-15T16:26:20.493Z_

<details><summary>↩ Tool result · `toolu_01VAY27pec65Kzme3UsLTvyG`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "22a992ea-2484-45e2-9d41-db4eaeff04a1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "oldString": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "     \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.",
          "-    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "+    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "     \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.",
          " \\end{enumerate}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now I also need to add "base-model" to the introduction where it says "six generators from three model families". Let me check:

Line 22: "We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families"
Line 34 (contributions): "across six generators spanning three model families"

Line 20 already says "base (pretrained) models" so contextually it's clear, but line 22 and 34 could benefit from explicit "base-model generators".


Since line 20 establishes the focus on base models within the same paragraph, line 22 doesn't need the redundant clarification. But line 34 in the contributions section stands alone, so adding "base-model" there would help with clarity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "1ddf1893-d6e9-482e-8f6f-a4c87c19cace",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqzvUeNoUDbA9K9goRa8NA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 26097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 18_

Now let me also make "base-model" explicit in the contributions bullet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "2724c4bf-264b-4a1e-9b7f-71413e6186ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqzvUeNoUDbA9K9goRa8NA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 26097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LWx7UwPZ7EJGrFEMH2WqWL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "old_string": "across six generators spanning three model families (0.6B--8.2B)",
  "new_string": "across six base-model generators spanning three model families (0.6B--8.2B)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "be349a93-3bb5-4d64-ae16-1ea88a9d2b27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PqzvUeNoUDbA9K9goRa8NA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 26097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2469
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

_source line 20 · 2026-05-15T16:26:29.469Z_

<details><summary>↩ Tool result · `toolu_01LWx7UwPZ7EJGrFEMH2WqWL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "f3161608-e06a-4def-9885-4e177eeabcfa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "oldString": "across six generators spanning three model families (0.6B--8.2B)",
    "newString": "across six base-model generators spanning three model families (0.6B--8.2B)",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "     \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.",
          "-    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "+    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "     \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.",
          " \\end{enumerate}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 21_

Now sync to docs/paper/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "830fb7fb-ef0b-411c-a5eb-a68ca7c84ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YpB4bqYeM7rdbsQg6PJHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 28566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01TSj3BoeFBGNdvUqsfTTdUA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "ddb630a4-150c-4dde-9da2-b3515a38fac5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YpB4bqYeM7rdbsQg6PJHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 28566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

### Tool result

_source line 23 · 2026-05-15T16:26:32.534Z_

<details><summary>↩ Tool result · `toolu_01TSj3BoeFBGNdvUqsfTTdUA`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.
5	We characterize a \emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.
6	A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\ gen-2+ depth discrimination ($p < 0.001$ vs.\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\,=\,0.051).
7	In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.
8	\end{abstract}
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "39dab1a2-8c83-49fa-9ec9-6ab7edb9d732",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex",
      "content": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).\nIn our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.\n\\end{abstract}\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01ThNWAnqu2ngHAd9QezWK5a`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "33d4910b-2faa-4d96-ae66-f26b68467ef3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015YpB4bqYeM7rdbsQg6PJHG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 28566,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

### Tool result

_source line 25 · 2026-05-15T16:26:32.876Z_

<details><summary>↩ Tool result · `toolu_01ThNWAnqu2ngHAd9QezWK5a`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Web-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.
5	Estimates suggest that 7--17\% of recent scientific papers and peer reviews contain substantial LLM-modified content \cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.
6	The result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.
7	
8	Existing detectors \cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.
9	This conflates qualitatively different material.
10	A first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.
11	A third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.
12	Treating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.
13	
14	We argue that a finer-grained characterization is needed: \emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\,/\,gen-1\,/\,gen-2+) rather than producing a binary label.
15	We refer to the overall framework---features, classifier, and evaluation protocol---as \emph{depth fingerprinting}, distinguishing the method from the task it addresses.
16	No existing method addresses this task directly in non-paraphrastic continuation chains.
17	When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
18	Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
19	These results do not extend to \emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.
20	We focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).
21	
22	We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).
23	We characterize a \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
24	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
25	The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+), with per-generator consistency (std\,=\,0.051).
26	
27	We also report a negative finding.
28	Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\ 2.387 depth-stratified).
29	In our experimental setting, depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data selection.
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.
34	    \item \textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\,=\,0.72 for leak-free depth discrimination (gen-1 vs.\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\,=\,0.051).
35	    \item \textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.
36	\end{enumerate}
37	
38	The remainder of this paper is organized as follows.
39	\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
40	\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
41	\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
42	\S\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "f72a4544-0e0e-4957-899e-e239f5a467ad",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
      "numLines": 43,
      "startLine": 1,
      "totalLines": 43
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Edit · `toolu_01VekR7VnFCBKTErdwBHfhzT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex",
  "old_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "26a23359-be7e-4afd-9fc8-828b24562d92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmY4RHfD5mY2E32NvkRH41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 29137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
      },
      "output_tokens": 69,
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

_source line 27 · 2026-05-15T16:26:37.643Z_

<details><summary>↩ Tool result · `toolu_01VekR7VnFCBKTErdwBHfhzT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "6ba81b61-199a-4d79-bdf6-33b9cfa23431",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/abstract.tex",
    "oldString": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.\nA 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).\nIn our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 6,
        "newStart": 3,
        "newLines": 6,
        "lines": [
          " As LLM outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.",
          " We formulate \\emph{ordinal depth estimation}---classifying text as human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---beyond binary detection.",
          " We characterize a \\emph{differential depth response}: central-tendency and diversity features drift monotonically with generation depth, while distributional shape features remain near-stationary.",
          "-A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.72 for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
          "+A 7-feature ensemble exploiting this complementarity achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for gen-1 vs.\\ gen-2+ depth discrimination ($p < 0.001$ vs.\\ all baselines) across 6 base-model generators from 3 model families (0.6B--8.2B parameters), with per-generator consistency (std\\,=\\,0.051).",
          " In our setting, depth-aware data curation does not outperform random subsampling, positioning depth fingerprinting as a diagnostic tool for provenance characterization.",
          " \\end{abstract}"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Edit · `toolu_01Um3WzWMNiiR6tD8y3zvpym`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "50cdac72-9888-4ac6-b9ec-2f9a0bbc2ba3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmY4RHfD5mY2E32NvkRH41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 29137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
      },
      "output_tokens": 69,
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

_source line 29 · 2026-05-15T16:26:39.615Z_

<details><summary>↩ Tool result · `toolu_01Um3WzWMNiiR6tD8y3zvpym`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "b522fe14-41ee-47c9-a4d3-e7395981ae70",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "oldString": "The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 7,
        "newStart": 22,
        "newLines": 7,
        "lines": [
          " We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).",
          " We characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.",
          " This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.",
          "-The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
          "+The combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).",
          " ",
          " We also report a negative finding.",
          " Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified)."
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Edit · `toolu_01HSaDqpV3PwrPLR1wfzBvrg`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
  "new_string": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "4dbed477-0e5a-4a80-8f46-eb8d1d496ef3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmY4RHfD5mY2E32NvkRH41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 29137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
      },
      "output_tokens": 69,
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

_source line 31 · 2026-05-15T16:26:41.955Z_

<details><summary>↩ Tool result · `toolu_01HSaDqpV3PwrPLR1wfzBvrg`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "4cfa10ba-c315-4c08-8517-a8eb867326a6",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "oldString": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
    "newString": "a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "     \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.",
          "-    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.72 for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "+    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "     \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.",
          " \\end{enumerate}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Edit · `toolu_017pg9bnauLg5cPDhfN4uAis`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
  "old_string": "across six generators spanning three model families (0.6B--8.2B)",
  "new_string": "across six base-model generators spanning three model families (0.6B--8.2B)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "09d1a4bd-31ae-471f-863b-a46ffd095dea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WmY4RHfD5mY2E32NvkRH41",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 29137,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
      },
      "output_tokens": 69,
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

_source line 33 · 2026-05-15T16:26:43.037Z_

<details><summary>↩ Tool result · `toolu_017pg9bnauLg5cPDhfN4uAis`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "7a85cdb9-dc59-4533-8a49-cca0c8db3981",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/docs/paper/introduction.tex",
    "oldString": "across six generators spanning three model families (0.6B--8.2B)",
    "newString": "across six base-model generators spanning three model families (0.6B--8.2B)",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nWe refer to the overall framework---features, classifier, and evaluation protocol---as \\emph{depth fingerprinting}, distinguishing the method from the task it addresses.\nNo existing method addresses this task directly in non-paraphrastic continuation chains.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---per-generator F1 ranging from 0.42 to 0.81 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\nWe focus on non-paraphrastic continuation chains from base (pretrained) models; instruction-tuned and RLHF models, which dominate web text, remain untested (Limitations).\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nWe characterize a \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves binary macro-F1 of 0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), with per-generator consistency (std\\,=\\,0.051).\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nIn our experimental setting, depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses implications, and a separate Limitations section addresses scope boundaries.\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}[nosep,leftmargin=*]",
          "     \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.",
          "-    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "+    \\item \\textbf{Empirical characterization.} We characterize differential depth response across six base-model generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves binary F1\\,=\\,0.723 (95\\% CI: [0.717, 0.729]) for leak-free depth discrimination (gen-1 vs.\\ gen-2+), outperforming all individual detection baselines ($p < 0.001$), with per-generator consistency (std\\,=\\,0.051).",
          "     \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.",
          " \\end{enumerate}",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 34_

All 4 files updated. Changes summary:

| Location | Change |
|---|---|
| abstract (both copies) | `0.72` → `0.723 (95\% CI: [0.717, 0.729])`; added `base-model` before `generators` |
| intro paragraph (both copies) | Same metric update on the headline claim |
| intro contribution bullet (both copies) | Same metric update + added `base-model generators` |

No 3-class F1 was previously mentioned in abstract/intro, so no supplementary reference needed here. Scope already says "base (pretrained) models" in intro line 20; the new `base-model generators` reinforces this in the abstract and contributions bullet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "uuid": "9faac73d-4481-435a-80d6-51e3f8069570",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018wj5ZprGk8HVo9nrsiwwQ6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1364,
      "cache_read_input_tokens": 31216,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1364
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

_source line 35_

All 4 files updated. Changes summary:

| Location | Change |
|---|---|
| abstract (both copies) | `0.72` → `0.723 (95\% CI: [0.717, 0.729])`; added `base-model` before `generators` |
| intro paragraph (both copies) | Same metric update on the headline claim |
| intro contribution bullet (both copies) | Same metric update + added `base-model generators` |

No 3-class F1 was previously mentioned in abstract/intro, so no supplementary reference needed here. Scope already says "base (pretrained) models" in intro line 20; the new `base-model generators` reinforces this in the abstract and contributions bullet.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 62108,
  "duration_api_ms": 63221,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "031f4fc9-47b1-47d9-906b-54ed5071c274",
  "total_cost_usd": 0.31450274999999994,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 20739,
    "cache_read_input_tokens": 150968,
    "output_tokens": 4321,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20739,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 171,
        "cache_read_input_tokens": 31216,
        "cache_creation_input_tokens": 1364,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1364
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1240,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.00134,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 4321,
      "cacheReadInputTokens": 150968,
      "cacheCreationInputTokens": 20739,
      "webSearchRequests": 0,
      "costUSD": 0.31316275,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ad10f9b9-2c8f-45f2-842a-1f965035516e"
}
```

</details>

---
