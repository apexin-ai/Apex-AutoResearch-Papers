# Research conversation: I need to read several LaTeX files from a paper directory to review changes. Please read each of the following files and

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a233ac51dbecdff59.jsonl`
- **Structured JSON:** [`6c5fe1923a0da472a86f.json`](../../sessions/6c/6c5fe1923a0da472a86f.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-15T13:13:53.863Z_

I need to read several LaTeX files from a paper directory to review changes. Please read each of the following files and return their FULL contents:

1. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/appendix.tex
2. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/experiments.tex
3. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
4. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
5. /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex

For each file, report:
- The full content (verbatim)
- Any occurrence of "551" or "529" with surrounding context (5 lines each side)
- Any occurrence of "0.469" or "0.386" or "0.379" with surrounding context
- Line numbers for any tables (tabular environments)

This is for a paper review, so accuracy matters. Return ALL content, do not truncate.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "cdd3f2f5-0c20-4640-a476-10083a4c6796",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:13:53.867Z_

```json
{
  "parentUuid": "cdd3f2f5-0c20-4640-a476-10083a4c6796",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__compute_coverage_matrix",
      "mcp__agent-ml-research__fetch_wandb_metrics",
      "mcp__agent-ml-research__get_gpu_health",
      "mcp__agent-ml-research__get_project_resource_usage",
      "mcp__agent-ml-research__list_constraints",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__read_experiment_plan_with_status",
      "mcp__agent-ml-research__read_matrix",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__read_registry",
      "mcp__agent-ml-research__read_roadmap",
      "mcp__agent-ml-research__reviewer_post_to_director",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__tail_training_logs"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "96cb6cf7-4c9b-434c-9533-4a7ae4a781ae",
  "timestamp": "2026-05-15T13:13:53.867Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:13:56.299Z_



I'll read all five files in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "96cb6cf7-4c9b-434c-9533-4a7ae4a781ae",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c51667a6-73fd-459f-9c4e-88382c890868",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22719,
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

_source line 4 · 2026-05-15T13:13:56.780Z_

<details open><summary>🔧 Tool call — Read · `toolu_01NxscbUqx7eENzsRmhzTp53`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c51667a6-73fd-459f-9c4e-88382c890868",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0f684e0a-6af3-4344-b7a8-2a0b71386627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22719,
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

### Tool result

_source line 5 · 2026-05-15T13:13:56.808Z_

<details><summary>↩ Tool result · reported error · `toolu_01NxscbUqx7eENzsRmhzTp53`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0f684e0a-6af3-4344-b7a8-2a0b71386627",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "66917c73-ed6d-43bf-86af-45989725bc29",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56.",
  "sourceToolAssistantUUID": "0f684e0a-6af3-4344-b7a8-2a0b71386627",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-15T13:13:57.247Z_

<details open><summary>🔧 Tool call — Read · `toolu_016MdqajgFQBtDQff18hEFoc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66917c73-ed6d-43bf-86af-45989725bc29",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f000e55a-c44d-4619-8c5e-31cb46f5429c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22719,
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

### Tool result

_source line 7 · 2026-05-15T13:13:57.253Z_

<details><summary>↩ Tool result · reported error · `toolu_016MdqajgFQBtDQff18hEFoc`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f000e55a-c44d-4619-8c5e-31cb46f5429c",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "01a832c1-4ce9-42fd-adbe-173abe8d4952",
  "toolUseResult": "Error: File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56.",
  "sourceToolAssistantUUID": "f000e55a-c44d-4619-8c5e-31cb46f5429c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-15T13:13:57.693Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VFW2hR7eh8qpW8XHtFpeZQ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01a832c1-4ce9-42fd-adbe-173abe8d4952",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8ced0760-c5ed-42f0-b717-309d0d355279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22719,
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

### Tool result

_source line 9 · 2026-05-15T13:13:57.701Z_

<details><summary>↩ Tool result · `toolu_01VFW2hR7eh8qpW8XHtFpeZQ`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (constrained-decoding compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	Under constrained decoding, LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression under constrained decoding---the standard regime for schema-compliant IE---is the primary mechanistic bottleneck, though whether compression fully accounts for the gap remains open.
15	The LP compression mechanism is a direct consequence of constrained decoding's restricted token space; alternative decoding strategies may yield different LP distributions.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Toward mechanistic confirmation.}
24	Our diagnosis predicts that LP score compression should diminish under free-form (unconstrained) generation, where the full token vocabulary is available at each step.
25	A controlled ablation---comparing LP selection under constrained versus free-form decoding on identical instances, with post-hoc JSON parsing for the free-form condition---would directly test whether the bottleneck is decoding-regime-specific.
26	\textit{[Planned experiment: free-form ablation on SciERC NER/RE.]}
27	All findings reported in this paper are specific to the constrained decoding regime; whether the gap persists under relaxed or free-form decoding remains an open question.
28	
29	\paragraph{Methodological implications.}
30	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
31	Effective selection likely requires either per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust} or relaxation of the constrained-decoding regime that compresses LP resolution; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ced0760-c5ed-42f0-b717-309d0d355279",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "3aaa89ef-e595-4ce8-8b24-7a1a6b133fd4",
  "sourceToolAssistantUUID": "8ced0760-c5ed-42f0-b717-309d0d355279",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-15T13:13:58.623Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MqF6uzA9DBNXDEZncrCfrD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aaa89ef-e595-4ce8-8b24-7a1a6b133fd4",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f3c329a1-9a83-41b1-a1ae-cf17a51a2e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 22719,
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

### Tool result

_source line 11 · 2026-05-15T13:13:58.629Z_

<details><summary>↩ Tool result · `toolu_01MqF6uzA9DBNXDEZncrCfrD`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction, but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	Under constrained decoding---the standard regime for schema-compliant IE---we evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.
4	These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom.
5	Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.
6	Neither succeeds: log-probability scores are compressed into effective ties for 60\% of instances under constrained decoding, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.
7	Where log-probability compression is absent, selection recovers significant gains ($+2.9$~pp, $p{=}0.01$), identifying constrained-decoding score compression as the primary bottleneck.
8	Signal rankings further depend on task complexity, with findings consistent across model families.
9	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3c329a1-9a83-41b1-a1ae-cf17a51a2e25",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "f7b7415c-7f08-4577-9852-51327dd9021c",
  "sourceToolAssistantUUID": "f3c329a1-9a83-41b1-a1ae-cf17a51a2e25",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-15T13:13:58.816Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WozExLSAgufLvEJvhGVVNn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7b7415c-7f08-4577-9852-51327dd9021c",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4Qz9m7xCJmoZBBHS6FR",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2fb777c1-be01-440a-bcb5-97444f5e7ce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y14U4HpX8PQHsSHDUGGLvt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 22719,
      "cache_read_input_tokens": 0,
      "output_tokens": 389,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 22719
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 389,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 22719,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 22719,
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

_source line 13 · 2026-05-15T13:13:58.824Z_

<details><summary>↩ Tool result · `toolu_01WozExLSAgufLvEJvhGVVNn`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	Within the constrained decoding regime standard for structured IE, we demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to constrained-decoding-induced score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
7	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
8	A direct free-form generation ablation would confirm whether the bottleneck is decoding-regime-specific.
9	Trained verifiers, relaxed decoding constraints, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2fb777c1-be01-440a-bcb5-97444f5e7ce0",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "1e6a0edd-0d00-454a-af37-a3d73bf3d98d",
  "sourceToolAssistantUUID": "2fb777c1-be01-440a-bcb5-97444f5e7ce0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-15T13:14:01.433Z_

The `appendix.tex` and `experiments.tex` files don't exist at the `docs/paper/` path. Let me search for the actual paper directory structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1e6a0edd-0d00-454a-af37-a3d73bf3d98d",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzXAUxzfmEhJieMJZ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "65173d87-db8a-4c51-ac7a-db9a7c4d8812",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gkkGGmG4viryDCehGiAEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3308,
      "cache_read_input_tokens": 22719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3308,
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

_source line 15 · 2026-05-15T13:14:01.788Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01MtYB8YtagNo1LhqFyLB5tD`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65173d87-db8a-4c51-ac7a-db9a7c4d8812",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzXAUxzfmEhJieMJZ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e0fbbbc1-290f-4d95-a967-545e398464bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017gkkGGmG4viryDCehGiAEo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3308,
      "cache_read_input_tokens": 22719,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3308,
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

### Tool result

_source line 16 · 2026-05-15T13:14:01.827Z_

<details><summary>↩ Tool result · `toolu_01MtYB8YtagNo1LhqFyLB5tD`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/best/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/median/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/worst/paper.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/n_scaling_appendix_tables_44b000.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/n_scaling_appendix_tables.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e0fbbbc1-290f-4d95-a967-545e398464bb",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "998fb2f9-4149-44e5-b833-d1459510de90",
  "sourceToolAssistantUUID": "e0fbbbc1-290f-4d95-a967-545e398464bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-15T13:14:06.651Z_

The files exist at `docs/paper/sections/` not `docs/paper/`. The `docs/paper/` level has `abstract.tex`, `discussion.tex`, `conclusion.tex` (which I already read), but `appendix.tex` and `experiments.tex` are in `docs/paper/sections/`. Let me read the missing files and the sections versions of those already read (since the `sections/` versions appear newer based on modification time).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "998fb2f9-4149-44e5-b833-d1459510de90",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7931da0b-7414-40c2-9d47-a96315a1cf0b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

_source line 18 · 2026-05-15T13:14:07.145Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SAkMD8uwCkioaSkuwZBmFn`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7931da0b-7414-40c2-9d47-a96315a1cf0b",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b0f4ffb6-5548-46ea-bf04-6398fe10f033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

### Tool result

_source line 19 · 2026-05-15T13:14:07.413Z_

<details><summary>↩ Tool result · `toolu_01SAkMD8uwCkioaSkuwZBmFn`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.010$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as population standard deviation.}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.411$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.283 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.411{\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.047$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.034$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	At $N{=}16$, SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$), making it a more stable alternative at higher sample sizes.
82	
83	\paragraph{Transfer across model families.}
84	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$).
85	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
86	At $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\rho{=}0.409$ vs.\ LP 0.239, $\Delta{=}{+}0.170$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
87	
88	\section{Calibration Analysis}\label{app:calibration}
89	
90	\begin{figure*}[t]
91	\centering
92	\includegraphics[width=\textwidth]{fig_reliability}
93	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
94	\label{fig:reliability}
95	\end{figure*}
96	
97	Reliability diagrams use 10 equal-width bins.
98	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
99	
100	\section{Additional Analyses}\label{app:additional}
101	
102	\paragraph{Per-relation diagnostic.}
103	RE signal degradation is relation-specific.
104	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
105	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
106	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
107	
108	\paragraph{Capability stratification.}
109	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
110	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
111	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
112	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
113	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
114	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
115	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
116	
117	\paragraph{Length vs.\ log-probability.}
118	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
119	
120	\begin{figure}[t]
121	\centering
122	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
123	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
124	\label{fig:length_logprob_scatter}
125	\end{figure}
126	
127	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
128	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
130	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
131	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
132	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
133	Evaluation circularity is negligible.
134	
135	\paragraph{Conditional filtering details.}
136	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
137	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
138	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
139	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
140	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
141	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
142	
143	\paragraph{WNUT-17 full signal analysis.}
144	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
145	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
146	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
147	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
148	
149	\begin{table}[t]
150	\centering
151	\small
152	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
153	\label{tab:wnut}
154	\begin{tabular}{lccccc}
155	\toprule
156	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
157	\midrule
158	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
159	FK      & .125 & .001 & .555 & .169 & .002 \\
160	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
161	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
162	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{Cross-configuration selection analysis.}
168	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
169	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
170	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
171	
172	\begin{table*}[t]
173	\centering
174	\small
175	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). Best non-oracle signal per row in \textbf{bold}. At $N{=}8$, no signal significantly outperforms greedy in any configuration. At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
176	\label{tab:cross_selection}
177	\begin{tabular}{llccccccc}
178	\toprule
179	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
180	\midrule
181	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
182	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
183	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
184	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
185	\bottomrule
186	\end{tabular}
187	\end{table*}
188	
189	\paragraph{Diminishing returns of $N$-scaling.}
190	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2025scaling}.
191	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
192	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
193	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
194	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
195	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
196	
197	\paragraph{$N{=}16$ CoNLL selection: small but significant.}
198	While quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ reveals a nuanced exception on LLaMA CoNLL.
199	VC achieves the largest gain over greedy ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).
200	These gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\% of the available headroom.
201	This reinforces the core finding: even under the most favorable conditions---high baseline performance, more candidates, and aggregated multi-seed evidence---signal-based selection recovers only a fraction of the oracle headroom available.
202	
203	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
204	
205	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
206	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
207	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
208	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
209	
210	\begin{table}[t]
211	\centering
212	\small
213	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
214	\label{tab:bootstrap_signal_ci}
215	\begin{tabular}{lcc}
216	\toprule
217	Signal & $\rho$ & 95\% CI \\
218	\midrule
219	VC & +0.379 & [+0.299, +0.456] \\
220	SJ & +0.360 & [+0.277, +0.437] \\
221	EM & +0.295 & [+0.212, +0.371] \\
222	FK & +0.267 & [+0.176, +0.354] \\
223	LP & +0.205 & [+0.119, +0.291] \\
224	\bottomrule
225	\end{tabular}
226	
227	\vspace{0.5em}
228	
229	\begin{tabular}{lccc}
230	\toprule
231	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
232	\midrule
233	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
234	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
235	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
236	\bottomrule
237	\end{tabular}
238	
239	\smallskip
240	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
241	\end{table}
242	
243	\section{Diversity and Selection Analysis}\label{app:diversity}
244	
245	\paragraph{Output diversity quantification.}
246	Table~\ref{tab:diversity} summarizes output diversity across configurations.
247	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
248	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
249	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
250	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
251	
252	\begin{table}[t]
253	\centering
254	\small
255	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
256	\label{tab:diversity}
257	\begin{tabular}{lcc}
258	\toprule
259	Config & Identical & Unique \\
260	\midrule
261	Qwen/SciERC & 11\% & 43\% \\
262	LLaMA/SciERC & 18\% & 39\% \\
263	Qwen/CoNLL & 57\% & --- \\
264	LLaMA/CoNLL & 88\% & --- \\
265	WNUT-17 & 55\% & --- \\
266	\bottomrule
267	\end{tabular}
268	\end{table}
269	
270	\paragraph{Oracle-improvable fraction.}
271	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
272	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
273	
274	\paragraph{Diversity-stratified selection gap.}
275	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
276	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
277	This rules out insufficient diversity as an explanation for the correlation-selection gap.
278	
279	\paragraph{TOST equivalence testing.}
280	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
281	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
282	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
283	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
284	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
285	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
286	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
287	
288	\begin{table}[t]
289	\centering
290	\small
291	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
292	\label{tab:tost}
293	\begin{tabular}{l cccc cccc}
294	\toprule
295	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
296	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
297	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
298	\midrule
299	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
300	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
301	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
302	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
303	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
304	\bottomrule
305	\end{tabular}
306	\end{table}
307	
308	\section{Multi-Seed Stability}\label{app:multiseed}
309	
310	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
311	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
312	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
313	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
314	
315	\begin{table}[t]
316	\centering
317	\small
318	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over 3 seeds.}
319	\label{tab:multiseed}
320	\begin{tabular}{lccccc}
321	\toprule
322	& LP & FK & SJ & VC & EM \\
323	\midrule
324	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
325	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
326	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
327	\midrule
328	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
329	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
330	\midrule
331	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
332	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
333	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
334	\bottomrule
335	\end{tabular}
336	\end{table}
337	
338	\section{Training Configuration}\label{app:training}
339	
340	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
341	
342	\begin{table}[t]
343	\centering
344	\small
345	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
346	\label{tab:training}
347	\begin{tabular}{ll}
348	\toprule
349	Parameter & Value \\
350	\midrule
351	LoRA rank / $\alpha$ & 32 / 64 \\
352	LoRA target & All linear modules \\
353	LoRA dropout & 0 \\
354	Optimizer & AdamW \\
355	Learning rate & 2e-4, cosine schedule \\
356	Warmup ratio & 0.1 \\
357	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
358	Epochs & 5 \\
359	Max sequence length & 2048 \\
360	Precision & bf16 \\
361	Gradient checkpointing & Enabled \\
362	Max gradient norm & 1.0 \\
363	Training seed & 42 \\
364	Framework & LLaMA Factory \\
365	\midrule
366	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
367	SciERC split & 1861 / 275 / 551 \\
368	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
369	& eval\_steps${=}$200, save\_limit${=}$5 \\
370	\bottomrule
371	\end{tabular}
372	\end{table}
373	
374	\paragraph{Prompt template.}
375	For NER, we use a structured prompt:
376	\begin{quote}
377	\small
378	\texttt{System:} You are an expert in Named Entity Recognition.\\
379	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
380	Text: \texttt{\{input\_text\}}\\
381	Entity types: \texttt{\{schema\_types\}}
382	\end{quote}
383	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
384	
385	\paragraph{Constrained decoding.}
386	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
387	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
388	
389	\section{Log-Probability Score Compression}\label{app:logprob_ties}
390	
391	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}, Figure~\ref{fig:lp_range_cdf}).
392	The median within-instance LP range is only 0.041 nats---below the $\varepsilon{=}0.05$ threshold used throughout, providing data-driven justification for this cutoff rather than an arbitrary choice.
393	At $\varepsilon{=}0.05$, 60.3\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below the threshold, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
394	The CDF rises smoothly with no cliff or discontinuity (Figure~\ref{fig:lp_range_cdf}), confirming that compression is a pervasive regime rather than a bimodal split.
395	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
396	
397	\begin{figure}[t]
398	\centering
399	\includegraphics[width=\columnwidth]{fig_lp_range_cdf}
400	\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
401	\label{fig:lp_range_cdf}
402	\end{figure}
403	
404	\begin{table}[t]
405	\centering
406	\small
407	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
408	\label{tab:logprob_ties}
409	\begin{tabular}{lc}
410	\toprule
411	$\varepsilon$ threshold & Tied instances (\%) \\
412	\midrule
413	0.01 & 1.1\% \\
414	0.05 & 60.3\% \\
415	0.1  & ${\sim}$84\% \\
416	0.5  & ${\sim}$99\% \\
417	\bottomrule
418	\end{tabular}
419	\end{table}
420	
421	\paragraph{Non-tied subset.}
422	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
423	As a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\rho(\text{LP}, \text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\% of instances achieve $p{<}0.05$ significance, and $\rho(\text{LP range}, \text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability---LP carries information but compression limits its exploitation.
424	A free-form NER decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.
425	
426	\section{RE Conditional Selection}\label{app:re_conditional_selection}
427	
428	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
429	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
430	All five signals underperform greedy on both subsets.
431	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
432	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
433	
434	\begin{table}[t]
435	\centering
436	\small
437	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
438	\label{tab:re_cond_selection}
439	\begin{tabular}{lcc}
440	\toprule
441	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
442	\midrule
443	Oracle & 0.585 & 0.757 \\
444	\midrule
445	LP & 0.395 & 0.600 \\
446	SJ & 0.386 & 0.604 \\
447	EM & 0.372 & 0.583 \\
448	VC & 0.359 & 0.574 \\
449	\midrule
450	Greedy & 0.404 & 0.674 \\
451	\bottomrule
452	\end{tabular}
453	\end{table}
454	
455	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
456	
457	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
458	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
459	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
460	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
461	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
462	
463	\begin{table*}[t]
464	\centering
465	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
466	\label{tab:freeform_ablation}
467	
468	\vspace{2pt}
469	{\small\textsc{Panel A: Logprob Distribution}}
470	\vspace{2pt}
471	
472	\begin{tabular}{lccc}
473	\toprule
474	Metric & Constrained & Free-form & $\Delta$ \\
475	\midrule
476	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
477	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
478	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
479	\bottomrule
480	\end{tabular}
481	
482	\vspace{8pt}
483	
484	{\small\textsc{Panel B: Selection F1}}
485	\vspace{2pt}
486	
487	\begin{tabular}{llccc}
488	\toprule
489	Task & Method & Constrained & Free-form & $\Delta$ \\
490	\midrule
491	\multirow{3}{*}{NER}
492	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
493	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
494	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
495	\midrule
496	\multirow{3}{*}{RE}
497	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
498	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
499	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
500	\bottomrule
501	\end{tabular}
502	
503	\vspace{8pt}
504	
505	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
506	\vspace{2pt}
507	
508	\begin{tabular}{l ccc ccc}
509	\toprule
510	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
511	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
512	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
513	\midrule
514	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
515	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
516	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
517	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
518	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
519	\bottomrule
520	\end{tabular}
521	
522	\vspace{8pt}
523	
524	{\small\textsc{Panel D: Parse Rate (Free-form)}}
525	\vspace{2pt}
526	
527	\begin{tabular}{lc}
528	\toprule
529	Metric & Value \\
530	\midrule
531	Total samples          & 4408 \\
532	Parse rate             & 99.95\% \\
533	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
534	\bottomrule
535	\end{tabular}
536	
537	\end{table*}
538	
539	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
540	
541	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
542	
543	\paragraph{Pairwise overlap.}
544	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
545	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
546	
547	\paragraph{Instance complexity drives failure.}
548	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
549	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
550	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
551	
552	\begin{table}[t]
553	\centering
554	\small
555	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
556	\label{tab:stable_failures}
557	\begin{tabular}{lcccc}
558	\toprule
559	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
560	\midrule
561	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
562	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
563	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
564	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
565	\bottomrule
566	\end{tabular}
567	\end{table}
568	
569	\paragraph{Flip instances.}
570	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
571	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
572	
573	\section{$N$-Scaling Detailed Analysis}\label{app:n_scaling}
574	
575	Tables~\ref{tab:n-scaling}--\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.
576	
577	\begin{table}[t]
578	\centering
579	\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
580	\label{tab:n-scaling}
581	\small
582	\begin{tabular}{l ccc ccc}
583	\toprule
584	 & \multicolumn{3}{c}{\textbf{NER} $\rho$} & \multicolumn{3}{c}{\textbf{RE} $\rho$} \\
585	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
586	Signal & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ & $N\!=\!8$ & $N\!=\!16$ & $\Delta$ \\
587	\midrule
588	SJ & 0.3641 & 0.4105 & \textbf{+0.0464} & 0.2485 & 0.2758 & \textbf{+0.0273} \\
589	FK & 0.2536 & 0.2833 & \textbf{+0.0297} & 0.2903 & 0.2964 & \textbf{+0.0061} \\
590	VC & 0.3861 & 0.4092 & \textbf{+0.0231} & 0.3088 & 0.3738 & \textbf{+0.0650} \\
591	LP & 0.2167 & 0.2393 & \textbf{+0.0226} & 0.2970 & 0.3100 & \textbf{+0.0130} \\
592	EM & 0.3071 & 0.3395 & \textbf{+0.0324} & 0.1353 & 0.1506 & \textbf{+0.0153} \\
593	\midrule
594	Mean & 0.3055 & 0.3364 & \textbf{+0.0308} & 0.2560 & 0.2813 & \textbf{+0.0253} \\
595	\bottomrule
596	\end{tabular}
597	\end{table}
598	
599	\begin{table}[t]
600	\centering
601	\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
602	\label{tab:ranking-stability}
603	\small
604	\begin{tabular}{ll cc l}
605	\toprule
606	Model & Task & $N$ & Kendall's $W$ & Consensus ranking \\
607	\midrule
608	Qwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
609	Qwen  & NER & 16 & 0.956 & SJ $\approx$ VC $>$ EM $>$ FK $>$ LP \\
610	Qwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
611	Qwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\
612	LLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\
613	\bottomrule
614	\end{tabular}
615	\end{table}
616	
617	\begin{table}[t]
618	\centering
619	\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
620	\label{tab:sigma-comparison}
621	\small
622	\begin{tabular}{l cc cc}
623	\toprule
624	 & \multicolumn{2}{c}{\textbf{NER} $\sigma_\rho$} & \multicolumn{2}{c}{\textbf{RE} $\sigma_\rho$} \\
625	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
626	Signal & $N\!=\!8$ & $N\!=\!16$ & $N\!=\!8$ & $N\!=\!16$ \\
627	\midrule
628	SJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\
629	FK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\
630	VC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\
631	EM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\
632	LP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\
633	\midrule
634	Mean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\
635	\bottomrule
636	\end{tabular}
637	\end{table}
638	
639	Signal rankings are highly stable across seeds: Kendall's $W{=}1.000$ for NER at $N{=}8$ (both models), dropping only to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\ref{tab:ranking-stability}).
640	Doubling $N$ reduces cross-seed $\sigma$ by 32\% on NER and 24\% on RE (Table~\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\%$ NER) and EM ($-59\%$ NER), confirming that additional samples stabilize structural signals more than LP.
641	
642	\section{Cross-Dataset OOD Analysis}\label{app:ood}
643	
644	To test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\to$narrower schema) and vice versa (Table~\ref{tab:ood}).
645	
646	\begin{table}[t]
647	\centering
648	\small
649	\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
650	\label{tab:ood}
651	\begin{tabular}{l ccc ccc}
652	\toprule
653	 & \multicolumn{3}{c}{\textbf{SciERC$\to$CoNLL}} & \multicolumn{3}{c}{\textbf{CoNLL$\to$SciERC}} \\
654	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
655	Signal & $\rho$ & In-dom. & $\Delta$ & $\rho$ & In-dom. & $\Delta$ \\
656	\midrule
657	VC & .469\textsuperscript{***} & .379 & +.090 & +.105\textsuperscript{*} & .379 & $-$.274 \\
658	SJ & .378\textsuperscript{***} & .360 & +.018 & $-$.186\textsuperscript{***} & .360 & $-$.546 \\
659	EM & .300\textsuperscript{***} & .295 & +.005 & $-$.202\textsuperscript{***} & .295 & $-$.497 \\
660	FK & .285\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\
661	LP & .246\textsuperscript{***} & .205 & +.041 & $-$.152\textsuperscript{***} & .205 & $-$.357 \\
662	\bottomrule
663	\end{tabular}
664	\end{table}
665	
666	\paragraph{Wider-to-narrower schema transfer.}
667	When the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\rho$ from Table~\ref{tab:quality_estimation}): VC reaches $\rho{=}0.469$ (in-domain $0.379$, $\Delta{=}{+}0.090$), SJ $\rho{=}0.378$ (in-domain $0.360$, $\Delta{=}{+}0.018$), and FK $\rho{=}0.285$ (in-domain $0.267$, $\Delta{=}{+}0.018$).
668	The wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (greedy F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.
669	
670	\paragraph{Narrower-to-wider schema transfer (excluded).}
671	The reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.
672	The CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (greedy NER F1${=}0.009$, RE F1${=}0.001$).
673	Under this regime, most signals flip to negative or near-zero correlations (Table~\ref{tab:ood}); only VC retains weak positive correlation ($\rho{=}0.105$, $p{=}0.016$).
674	These negative correlations reflect the model systematically generating confident but incorrect outputs---a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}), not evidence against signal utility.
675	
676	\paragraph{Asymmetry interpretation.}
677	The directional asymmetry is driven by schema coverage: wider$\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.
678	This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
679	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b0f4ffb6-5548-46ea-bf04-6398fe10f033",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "2271c935-57bf-4154-91ff-c807a432a7c0",
  "sourceToolAssistantUUID": "b0f4ffb6-5548-46ea-bf04-6398fe10f033",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-15T13:14:07.544Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Qn6BbjEryNzgZm6FpMRZk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2271c935-57bf-4154-91ff-c807a432a7c0",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a2c211a8-1c43-4807-bdc1-9eb8d181a296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

### Tool result

_source line 21 · 2026-05-15T13:14:07.552Z_

<details><summary>↩ Tool result · `toolu_012Qn6BbjEryNzgZm6FpMRZk`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}); detailed $N$-scaling analysis in Appendix~\ref{app:n_scaling}. A 3-seed stability analysis ($\sigma{\leq}0.026$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{Semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA; direct comparison is not meaningful due to different output spaces.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances separates binary success detection (can the model extract \textit{anything}?) from quality gradation (among successful extractions, which are better?), but excludes the hardest instances where models fail completely---the conditional set is easier on average.
79	This reshuffles signal rankings (Figure~\ref{fig:signal_heatmap}, right).
80	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
81	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
82	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
83	
84	%% ============================================================
85	\subsection{The Correlation-Selection Gap}
86	\label{sec:selection_gap}
87	
88	\begin{figure*}[t]
89	\centering
90	\includegraphics[width=\textwidth]{fig_selection_gap}
91	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
92	\label{fig:selection_gap}
93	\end{figure*}
94	
95	\begin{table}[t]
96	\centering
97	\small
98	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. Instance-level signals (SJ, FK, EM, VC) select the sample closest to the consensus output; VC uses majority-threshold voting ($>{N/2}$) for selection, distinct from the continuous QE score (Eq.~\ref{eq:voting}).}
99	\label{tab:selection}
100	\begin{tabular}{lcc}
101	\toprule
102	Method & NER F1 & RE F1 \\
103	\midrule
104	Oracle & 0.776 & 0.585 \\
105	\midrule
106	LP           & \textbf{0.650} & 0.395 \\
107	SJ       & 0.645 & 0.386 \\
108	EM        & 0.636 & 0.372 \\
109	VC                 & 0.634 & 0.359 \\
110	\midrule
111	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
112	Random             & 0.608 & 0.354 \\
113	\bottomrule
114	\end{tabular}
115	\end{table}
116	
117	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
118	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
119	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
120	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
121	
122	\paragraph{No significant improvement over greedy.}
123	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
124	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
125	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
126	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains; cross-seed analysis confirms RE LP failures are partially systematic (Appendix~\ref{app:lp_failure_stability}).
127	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
128	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{significantly below} greedy ($\Delta{=}{-}2.6$~pp, $p{<}0.03$ across 3 seeds).
129	The gap extends to CoNLL at $N{=}8$ (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
130	
131	\paragraph{Quality estimation $\neq$ output selection.}
132	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
133	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
134	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2025scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
135	
136	%% ============================================================
137	\subsection{Robustness}
138	\label{sec:robustness_main}
139	
140	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all NER settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
141	On RE, only VC consistently outperforms LP ($\Delta\rho{=}{+}0.012$, preliminary).
142	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2c211a8-1c43-4807-bdc1-9eb8d181a296",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "cebac21c-ff9a-4409-8f81-e914e2559bd5",
  "sourceToolAssistantUUID": "a2c211a8-1c43-4807-bdc1-9eb8d181a296",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-15T13:14:08.553Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WQTBKmRnnyyGP3fKasmt8o`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cebac21c-ff9a-4409-8f81-e914e2559bd5",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b42e7b95-7d7d-4931-af48-b27730042538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

### Tool result

_source line 23 · 2026-05-15T13:14:08.578Z_

<details><summary>↩ Tool result · `toolu_01WQTBKmRnnyyGP3fKasmt8o`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across two model families at 8B scale, though with model-dependent magnitude.
6	At higher sample sizes ($N{=}16$), SJ converges to comparable NER performance with VC ($\Delta{=}0.002$) with lower cross-seed variance ($\sigma{=}0.010$ vs.\ $0.026$); on RE, only VC consistently outperforms LP (preliminary).
7	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
8	
9	\paragraph{Why the gap exists: two layers.}
10	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
11	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
12	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
13	LP scores are severely compressed: the median within-instance LP range is only 0.041 nats, below the $\varepsilon{=}0.05$ threshold at which 60\% of instances are effectively tied, and 75\% of pairwise comparisons fall within $|\Delta|{<}0.026$ (Appendix~\ref{app:logprob_ties}).
14	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
15	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
16	A controlled NER ablation (\S\ref{sec:ablation}) confirms that LP compression persists without constrained decoding; on RE, the interaction is task-dependent.
17	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
18	
19	\paragraph{Connection to MBR decoding.}
20	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
21	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
22	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
23	
24	\paragraph{Score compression under free-form decoding.}\label{sec:ablation}
25	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
26	We test this via controlled ablation on SciERC (Qwen3-8B, single dataset): generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
27	For NER, LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%) and selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained), establishing that NER LP compression persists independent of decoding regime in our setting.
28	However, the ablation reveals a task-dependent interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single seed).
29	This reversal falls within the NER bootstrap 95\% CI [$-3.0$, $+4.2$]~pp and is based on a single seed, so we do not treat it as a confirmed finding; it suggests that constrained decoding may interact differently with RE but requires multi-seed replication.
30	The NER/RE divergence indicates that the relationship between decoding regime and selection is task-specific in our setting.
31	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
32	
33	\paragraph{Task-specific decoding interactions.}
34	The free-form ablation reveals divergent behavior across tasks.
35	On RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is driven by selective variance reallocation ($p{<}0.0001$).
36	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
37	This interaction does not generalize to NER, where selection remains negligible under both regimes.
38	This ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.
39	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
40	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
41	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
42	
43	\paragraph{Methodological implications.}
44	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
45	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:n_scaling}) shows $N{=}8$ captures most quality estimation benefit.
46	Cross-dataset evaluation confirms that structural signals are robust to domain shift when the training schema subsumes the target (VC $\rho{=}0.469$ OOD vs.\ $0.379$ in-domain); the reverse direction fails due to catastrophic model failure, not signal failure (Appendix~\ref{app:ood}).
47	Our findings are established under constrained decoding at 8B scale; a single-dataset NER ablation suggests LP compression persists without constrained decoding, but RE shows task-dependent interaction with decoding regime.
48	Whether these patterns generalize across datasets, model scales, and decoding strategies warrants further investigation.
49	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b42e7b95-7d7d-4931-af48-b27730042538",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "75974a17-7773-44c1-896b-61d9384aac03",
  "sourceToolAssistantUUID": "b42e7b95-7d7d-4931-af48-b27730042538",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-15T13:14:09.015Z_

<details open><summary>🔧 Tool call — Read · `toolu_01H22Gdk6MRqB9k58iMY4TVz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75974a17-7773-44c1-896b-61d9384aac03",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8f9d88d5-c280-451c-b128-676308c25ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1833,
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

### Tool result

_source line 25 · 2026-05-15T13:14:09.022Z_

<details><summary>↩ Tool result · `toolu_01H22Gdk6MRqB9k58iMY4TVz`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We evaluate five confidence signals on three NER benchmarks and one RE benchmark with two 8B-parameter model families.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom.
5	Given that four of five signals are instance-level by construction and cannot rank candidates, the empirical question is whether per-sample log-probability or consensus-proximity selection (MBR decoding) can bridge the gap.
6	Neither succeeds: log-probability scores are compressed into effective ties within instances (median within-instance range 0.041 nats), and MBR utility correlates with quality across instances but not within them.
7	A controlled NER ablation confirms that LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary, single seed), suggesting task-dependent interaction with decoding regime.
8	These findings, observed across two model families at 8B scale, indicate that closing the gap likely requires per-sample scoring beyond unsupervised signals.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f9d88d5-c280-451c-b128-676308c25ddf",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "54ea187a-053f-43d5-a2ef-ad30cb3490ce",
  "sourceToolAssistantUUID": "8f9d88d5-c280-451c-b128-676308c25ddf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-15T13:14:09.295Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QNEtjV2Dtgz5eotSr9LTkV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54ea187a-053f-43d5-a2ef-ad30cb3490ce",
  "isSidechain": true,
  "agentId": "a233ac51dbecdff59",
  "requestId": "req_011Cb4QzkDoMWJoNcXUD5Pex",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a8016c13-e70c-4e0f-bea7-50649618929c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcAquFidsCfteb1LSgHHU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1833,
      "cache_read_input_tokens": 26027,
      "output_tokens": 490,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 490,
          "cache_read_input_tokens": 26027,
          "cache_creation_input_tokens": 1833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1833,
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

_source line 27 · 2026-05-15T13:14:09.300Z_

<details><summary>↩ Tool result · `toolu_01QNEtjV2Dtgz5eotSr9LTkV`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We systematically evaluate five confidence signals across quality estimation, binary discrimination, and sample selection for LLM-based structured IE, revealing that these metrics decouple---single-metric evaluation risks selecting the wrong signal for the intended use case.
4	All signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) yet none significantly improves sample selection on SciERC despite 13--18~pp oracle headroom---the \textit{correlation-selection gap}.
5	The instance-level failure of four signals is definitional; the empirical finding is that neither consensus-proximity selection (MBR decoding) nor log-probability bridges the gap.
6	MBR utility correlates with quality across instances but not within them; LP scores are compressed into effective ties (60\% of instances), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
7	A controlled free-form decoding ablation confirms that NER LP compression persists without constrained decoding; on RE, LP selection reverses direction (preliminary), indicating task-dependent interaction with decoding regime.
8	Signal rankings shift with task difficulty---EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude; at the capability boundary (WNUT-17), all signals collapse to non-significance.
9	RE findings rest on SciERC alone (preliminary) and warrant multi-benchmark validation.
10	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a8016c13-e70c-4e0f-bea7-50649618929c",
  "isSidechain": true,
  "promptId": "3e89eb9c-275e-40b4-a303-e81b85a9cda9",
  "agentId": "a233ac51dbecdff59",
  "type": "user",
  "uuid": "ea171852-70fd-4171-abae-6d399674066c",
  "sourceToolAssistantUUID": "a8016c13-e70c-4e0f-bea7-50649618929c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "6a04e9f4-28e4-46a0-b4e7-626be34b3be2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---
