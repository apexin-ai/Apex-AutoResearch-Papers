# paper camera ready prose

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 126
- **Recorded user turns:** 0
- **Tool calls:** 49
- **Original source:** `logs/workers/worker_paper_camera_ready_prose_20260522T063803.log`
- **Structured JSON:** [`6cd133adb8075bbe5e94.json`](../../sessions/6c/6cd133adb8075bbe5e94.json)

## Before a recorded user message

126 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction",
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
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
  "uuid": "4a0f1042-983a-4078-98d9-d28e294402ae",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-schema-dag-extraction/memory/"
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
    "resetsAt": 1779438000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5d2672cb-f750-4475-9480-7158d9773dcf",
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1"
}
```

---

### Assistant

_source line 4_

I'll start by reading all the .tex files to understand the full paper structure.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "6623741c-192c-411b-8df8-2a06a678a498",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3zNjXMHH8Tw6PC16PUDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12517,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12517
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

<details open><summary>🔧 Tool call — Glob · `toolu_01MesS7CLqPgWiVU4eUMKfNe`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "41d30321-846b-4098-846f-0a2fa7000d40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015y3zNjXMHH8Tw6PC16PUDW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12517,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12517
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

_source line 6 · 2026-05-22T06:38:16.774Z_

<details><summary>↩ Tool result · reported error · `toolu_01MesS7CLqPgWiVU4eUMKfNe`</summary>

```text
&lt;tool_use_error>Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "4dae9314-d08b-49c0-aaff-3644b4e5ec50",
  "tool_use_result": "Error: Directory does not exist: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/paper. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Glob · `toolu_01W9XCizQwyJjvy2xu7CwPUi`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "4546fc19-94ff-4be3-bcea-b4c6214a18d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VMXRGfRfZMKdi48u3SPEu7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 218,
      "cache_read_input_tokens": 24358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 218
      },
      "output_tokens": 72,
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

_source line 8 · 2026-05-22T06:38:19.728Z_

<details><summary>↩ Tool result · `toolu_01W9XCizQwyJjvy2xu7CwPUi`</summary>

```text
artifacts/dream_reports/dream_20260515T053106/best/paper.tex
artifacts/dream_reports/dream_20260515T053106/median/paper.tex
artifacts/dream_reports/dream_20260515T053106/worst/paper.tex
artifacts/dream_reports/dream_20260515T113743/best/paper.tex
artifacts/dream_reports/dream_20260515T113743/median/paper.tex
artifacts/dream_reports/dream_20260515T113743/worst/paper.tex
artifacts/dream_reports/dream_20260515T140829/best/paper.tex
artifacts/dream_reports/dream_20260515T140829/median/paper.tex
artifacts/dream_reports/dream_20260515T140829/worst/paper.tex
artifacts/_project/paper/dataset_stats.tex
artifacts/paper/tables/dataset_stats.tex
artifacts/_project/paper/sdgd_negative.tex
artifacts/_project/paper/experimental_setup.tex
docs/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/dream_reports/dream_20260516T073533/best/paper.tex
artifacts/dream_reports/dream_20260516T073533/median/paper.tex
artifacts/dream_reports/dream_20260516T073533/worst/paper.tex
docs/paper/supplementary.tex
artifacts/acknowledgements_draft.tex
docs/paper/prompt_appendix.tex
docs/paper/checklist.tex
docs/paper/experimental_setup.tex
artifacts/error_taxonomy_cross_model_table.tex
artifacts/permutation_equivalence_latex.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
artifacts/_project/paper/docred_ridge_appendix.tex
artifacts/docred_ridge_appendix.tex
docs/paper/main.tex
docs/paper/results.tex
docs/paper/discussion.tex
docs/paper/sdgd_negative.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "a2808552-251f-45e3-8e48-ba05270288a6",
  "tool_use_result": {
    "filenames": [
      "artifacts/dream_reports/dream_20260515T053106/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T053106/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T113743/worst/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/best/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/median/paper.tex",
      "artifacts/dream_reports/dream_20260515T140829/worst/paper.tex",
      "artifacts/_project/paper/dataset_stats.tex",
      "artifacts/paper/tables/dataset_stats.tex",
      "artifacts/_project/paper/sdgd_negative.tex",
      "artifacts/_project/paper/experimental_setup.tex",
      "docs/paper/conclusion.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/dream_reports/dream_20260516T073533/best/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/median/paper.tex",
      "artifacts/dream_reports/dream_20260516T073533/worst/paper.tex",
      "docs/paper/supplementary.tex",
      "artifacts/acknowledgements_draft.tex",
      "docs/paper/prompt_appendix.tex",
      "docs/paper/checklist.tex",
      "docs/paper/experimental_setup.tex",
      "artifacts/error_taxonomy_cross_model_table.tex",
      "artifacts/permutation_equivalence_latex.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "artifacts/_project/paper/docred_ridge_appendix.tex",
      "artifacts/docred_ridge_appendix.tex",
      "docs/paper/main.tex",
      "docs/paper/results.tex",
      "docs/paper/discussion.tex",
      "docs/paper/sdgd_negative.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 25,
    "numFiles": 34,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
The paper files are in `docs/paper/`. Let me read all of them.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "5d74f9f8-c551-4115-aedd-52835013fb50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 10_

The paper is in `docs/paper/`. Let me read all the .tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "685964fd-d357-4c97-8275-d06a7dc9ac55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 11_

<details open><summary>🔧 Tool call — Read · `toolu_013haaQHFDSiVeK16EFoUE2m`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "797d233a-5303-427a-9373-54a736d90fd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 12 · 2026-05-22T06:38:23.468Z_

<details><summary>↩ Tool result · reported error · `toolu_013haaQHFDSiVeK16EFoUE2m`</summary>

```text
File content (27034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "221a1c74-3946-4210-8a28-878a43e9860b",
  "tool_use_result": "Error: File content (27034 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Read · `toolu_01QQgZhurFynvWAvTLz9iXYs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "601e9fb7-e5cd-400b-82ee-2b94cc4720cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 14 · 2026-05-22T06:38:23.576Z_

<details><summary>↩ Tool result · `toolu_01QQgZhurFynvWAvTLz9iXYs`</summary>

```text
1	\begin{abstract}
2	Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:
3	(1)~count degradation spans all three tasks (up to $-$49\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \approx 0.22$ on FewRel, VIF${}\,=\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;
4	(2)~BCS explains ${\sim}$22\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;
5	(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.
6	\end{abstract}
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "de1b364a-a8e5-494d-8357-60b8497b847e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nSchema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:\n(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;\n(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.\n\\end{abstract}\n",
      "numLines": 7,
      "startLine": 1,
      "totalLines": 7
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_01YGSk8CG1kc8mXXC3g1tAvx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "2f47dea4-9600-4e1b-b5a8-19241c7a48cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 16 · 2026-05-22T06:38:24.022Z_

<details><summary>↩ Tool result · `toolu_01YGSk8CG1kc8mXXC3g1tAvx`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	\looseness=-1
5	Training-free\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\% with one relation to 50.4\% with 80 relations (sentence-level) and from 88.0\% to 38.7\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.
6	
7	\looseness=-1
8	What explains this degradation? Prior decomposition strategies \citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\S\ref{sec:related_work}).
9	
10	This study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.
11	
12	We ask three questions. \textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \textbf{RQ2}: Through what modes do count and confusability each degrade performance? \textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?
13	
14	\looseness=-1
15	To our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, and MAVEN \citep{maven-2020} using Qwen3-32B (\S\ref{sec:experimental_setup}).
16	
17	Our experiments yield four findings:
18	(1)~Degradation operates along two dimensions with bounded interaction: count-related recall decline (up to $-$49\,pp) and confusability-related type substitution, confirmed on sentence- and document-level RE (\S\ref{sec:count_curves}, \S\ref{sec:multi_channel}).
19	(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\S\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\S\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\S\ref{sec:centrality_confound}).
20	(3)~RE effects are consistent across schema sizes, prompt designs, and three open-weight model families (8B--70B); Gemini Flash provides partial but fragile corroboration. The NER null is not detected on three models (8B--70B; \S\ref{sec:bcs_controlled}).
21	(4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\S\ref{sec:sdgd}).
22	Our contributions are:
23	\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]
24	    \item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\,=\,1.18$), explaining ${\sim}$22\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\S\ref{sec:count_curves}, \S\ref{sec:pairwise}, \S\ref{sec:bcs_controlled}).
25	    \item We document a task asymmetry: on FewRel, BCS explains ${\sim}$22\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\,=\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\S\ref{sec:bcs_controlled}, \S\ref{sec:multi_channel}).
26	    \item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\S\ref{sec:sdgd}).
27	\end{enumerate}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "74659f31-0e9e-476c-b135-cf127b4477d3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\looseness=-1\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \\citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.\n\n\\looseness=-1\nWhat explains this degradation? Prior decomposition strategies \\citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\n\\looseness=-1\nTo our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \\emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\citep{fewnerd-2021}, FewRel \\citep{fewrel-2018}, DocRED \\citep{docred-2019}, and MAVEN \\citep{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield four findings:\n(1)~Degradation operates along two dimensions with bounded interaction: count-related recall decline (up to $-$49\\,pp) and confusability-related type substitution, confirmed on sentence- and document-level RE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:multi_channel}).\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\\S\\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\n(3)~RE effects are consistent across schema sizes, prompt designs, and three open-weight model families (8B--70B); Gemini Flash provides partial but fragile corroboration. The NER null is not detected on three models (8B--70B; \\S\\ref{sec:bcs_controlled}).\n(4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\\S\\ref{sec:sdgd}).\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).\n    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_012B9hBeALy2h1cXBM8V1bKY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "97514d24-efe2-4fca-a139-d4d19f0f5e79",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 18 · 2026-05-22T06:38:24.968Z_

<details><summary>↩ Tool result · `toolu_012B9hBeALy2h1cXBM8V1bKY`</summary>

```text
1	\section{Related Work}
2	\label{sec:related_work}
3	
4	\paragraph{Training-free LLM IE.}
5	\looseness=-1
6	Training-free LLM IE spans instruction tuning \citep{instructuie-2023}, code-style schema encoding \citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \citep{gollie-2024,adelie-2024}, schema-driven decoding \citep{slot-2025,oneke-2025}, and constrained JSON decoding \citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \citep{uniner-2024}, and bidirectional encoders \citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \citep{relationprompt-2022}, constrained generation \citep{josifoski-2022-genie}, and shared embedding spaces \citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work also exploits type embeddings for retrieval \citep{shachar-2025-ner-retriever} and introspective confusion for example selection \citep{reflect-learn-2026}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.
7	
8	\paragraph{Schema complexity in IE.}
9	\looseness=-1
10	The most directly related work is LLM-PEE \citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\to$0.21; \S\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \citep{iepile-2024}, schema definition optimization \citep{parse-2025}, multi-agent debate \citep{crossagentie-2025,cmas-ner-2025}, and active prompting \citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \emph{why} such reduction works.
11	
12	\paragraph{Schema complexity in dialogue and IE.}
13	\looseness=-1
14	The Schema-Guided Dialogue dataset~\citep{rastogi2020towards} and SGD-X~\citep{lee2022sgd} document degradation with schema linguistic variation; \citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \citep{dubey-2018-pairwise-confusion}, correlated label noise \citep{collier-2021-correlated-noise}, hierarchical classification \citep{deng-2010-imagenet}, and label confusion matrices \citep{guo-2021-label-confusion,muller2019when,peterson2019human}.
15	
16	\paragraph{SCS novelty.}
17	\looseness=-1
18	SCS inherits the embedding-similarity criterion from LLM-PEE \citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \citep{snell2017prototypical} and zero-shot classification \citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\%) compounds at the ecological batch level to explain ${\sim}$22\% of cross-batch RE variance on FewRel (\S\ref{sec:bcs_controlled}).
19	
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "92c6ae35-ebb6-490d-bf82-1b698d9ce339",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\n\\looseness=-1\nTraining-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work also exploits type embeddings for retrieval \\citep{shachar-2025-ner-retriever} and introspective confusion for example selection \\citep{reflect-learn-2026}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.\n\n\\paragraph{Schema complexity in IE.}\n\\looseness=-1\nThe most directly related work is LLM-PEE \\citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21; \\S\\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \\citep{iepile-2024}, schema definition optimization \\citep{parse-2025}, multi-agent debate \\citep{crossagentie-2025,cmas-ner-2025}, and active prompting \\citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \\citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \\citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \\emph{why} such reduction works.\n\n\\paragraph{Schema complexity in dialogue and IE.}\n\\looseness=-1\nThe Schema-Guided Dialogue dataset~\\citep{rastogi2020towards} and SGD-X~\\citep{lee2022sgd} document degradation with schema linguistic variation; \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \\citep{dubey-2018-pairwise-confusion}, correlated label noise \\citep{collier-2021-correlated-noise}, hierarchical classification \\citep{deng-2010-imagenet}, and label confusion matrices \\citep{guo-2021-label-confusion,muller2019when,peterson2019human}.\n\n\\paragraph{SCS novelty.}\n\\looseness=-1\nSCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).\n\n",
      "numLines": 20,
      "startLine": 1,
      "totalLines": 20
    }
  }
}
```

</details>

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_011jE7ZmTaiZTuWwvkyGRv9V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "3b22e7d1-2d61-4146-b98c-3994968eaf66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 20 · 2026-05-22T06:38:25.431Z_

<details><summary>↩ Tool result · `toolu_011jE7ZmTaiZTuWwvkyGRv9V`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental_setup}
3	
4	We evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).
5	
6	\subsection{Tasks and Datasets}
7	\label{sec:datasets}
8	
9	\paragraph{Few-NERD (NER).}
10	Few-NERD \citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\binom{66}{2}=2{,}145$ possible pairs.
11	
12	\paragraph{FewRel (RE).}
13	FewRel \citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.
14	
15	\paragraph{DocRED (Document-level RE).}
16	DocRED \citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.
17	
18	\paragraph{MAVEN (ED).}
19	MAVEN \citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\S\ref{sec:centrality_confound}).
20	
21	Table~\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \S\ref{sec:scs}.
22	
23	\begin{table}[t]
24	\centering
25	\small
26	\resizebox{\columnwidth}{!}{%
27	\begin{tabular}{llrrlll}
28	\toprule
29	\textbf{Dataset} & \textbf{Task} & \textbf{\# Types} & \textbf{\# Eval Units} & \textbf{Domain} & \textbf{BCS Range} & \textbf{Embedding} \\
30	\midrule
31	Few-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\
32	FewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\
33	DocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\
34	MAVEN & ED & 168 & 18{,}904\rlap{$^\dagger$} & Same & 0.87--0.97 & MiniLM \\
35	\bottomrule
36	\end{tabular}}
37	\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\dagger$Trigger mentions across 8{,}042 sentences.}
38	\label{tab:datasets}
39	\end{table}
40	
41	\subsection{Schema Confusability Score (SCS)}
42	\label{sec:scs}
43	
44	\looseness=-1
45	We define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\text{name}(t)$, an embedding function $\text{embed}(\cdot)$ maps the type name to a vector representation. The \textbf{pairwise SCS} between types $t_i$ and $t_j$ is:
46	{\small
47	\[
48	\text{SCS}(t_i, t_j) = \cos\bigl(\text{embed}(\text{name}(t_i)),\; \text{embed}(\text{name}(t_j))\bigr)
49	\]
50	}
51	
52	For a batch of types $B = \{t_1, \ldots, t_k\}$, the \textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:
53	\[
54	\text{BCS}(B) = \frac{1}{\binom{k}{2}} \sum_{i < j,\; t_i, t_j \in B} \text{SCS}(t_i, t_j)
55	\]
56	
57	We use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\,=\,0.034$ vs.\ MiniLM std${}\,=\,0.081$), consistent with autoregressive anisotropy \citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\Delta r$: $-0.023$ to $+0.035$; Appendix~\ref{app:scs-ablation}).
58	
59	\paragraph{SCS as a lightweight proxy.}
60	\label{sec:scs-validation}
61	SCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\S\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.
62	
63	\begin{figure*}[t]
64	\centering
65	\begin{minipage}[t]{0.48\textwidth}
66	\centering
67	\includegraphics[width=\linewidth]{../../figures/paper/fig_count_curves.pdf}
68	\end{minipage}
69	\hfill
70	\begin{minipage}[t]{0.48\textwidth}
71	\centering
72	\includegraphics[width=\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}
73	\end{minipage}
74	\caption{\textbf{(a)} Count-degradation curves. Error bars: $\pm 1$\,SD across 3 batch-composition seeds $\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}
75	\label{fig:main_results}
76	\end{figure*}
77	
78	\subsection{Experimental Design}
79	\label{sec:exp_design}
80	
81	We conduct two complementary experimental paradigms.
82	
83	\paragraph{Experiment 1: Count Curves.}
84	We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \{2, 6, 12, 22, 44, 66\} for Few-NERD, \{4, 8, 16, 32, 40, 64, 80\} for FewRel, \{4, 8, 16, 32, 64, 96\} for DocRED, and \{6, 12, 22, 44, 64\} for MAVEN.
85	
86	\paragraph{Experiment 2: BCS-Controlled.}
87	We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\,\in\{6, 12\}$), FewRel (count$\,\in\{8, 16\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\,\in\{16, 32\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\S\ref{sec:centrality_confound}).
88	
89	\subsection{Evaluation Metrics}
90	\label{sec:metrics}
91	
92	\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \emph{and} the type matches; partial spans count as incorrect. \textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.
93	
94	
95	\subsection{Model and Inference}
96	\label{sec:model}
97	
98	\looseness=-1
99	We use Qwen3-32B-FP8 \citep{qwen3-2025} served via vLLM v0.20.2 \citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\,GB) with greedy decoding (temperature${}\,=\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \citep{sclar-sensitivity-2024} (templates in Appendix~\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "5d78196a-d89a-4942-9662-1209f5785638",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \\citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \\citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \\citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with autoregressive anisotropy \\citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}).\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 batch-composition seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \\texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\looseness=-1\nWe use Qwen3-32B-FP8 \\citep{qwen3-2025} served via vLLM v0.20.2 \\citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\citep{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 100
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01Y9RccJS1PrbFGTqDUXA7eR`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "1cc58875-d306-4498-bb01-19d106ea1d5b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 22 · 2026-05-22T06:38:25.945Z_

<details><summary>↩ Tool result · `toolu_01Y9RccJS1PrbFGTqDUXA7eR`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	All experiments use Qwen3-32B and the v1 prompt (\S\ref{sec:model}; Appendix~\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.
5	
6	\subsection{Count-Degradation Curves}
7	\label{sec:count_curves}
8	
9	\looseness=-1
10	Figure~\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\%$\to$38.7\%, $-$56\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\S\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\,pp on Few-NERD; per-batch $r = 0.725$; Table~\ref{tab:cross_model}). The pattern is stable across three seeds (max $\Delta = 10.7$\,pp, within 1\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\times$; Appendix~\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\S\ref{sec:bcs_controlled}).
11	
12	\subsection{Pairwise Confusability and Type Confusion}
13	\label{sec:pairwise}
14	
15	We test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\text{SCS}(t_i, t_j)$. Table~\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\% CIs.
16	
17	\begin{table}[t]
18	\centering
19	\small
20	\resizebox{\columnwidth}{!}{%
21	\begin{tabular}{llrrrrr}
22	\toprule
23	\textbf{Dataset} & \textbf{Embed.} & \textbf{$n$ pairs} & \textbf{$r$} & \textbf{$r^2$} & \textbf{95\% CI} & \textbf{$p$} \\
24	\midrule
25	Few-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\,0.001$ \\
26	MAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\,0.001$ \\
27	\bottomrule
28	\end{tabular}}
29	\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\to}t_j) + C(t_j{\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \S\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}
30	\label{tab:pairwise}
31	\end{table}
32	
33	\looseness=-1
34	The correlations are statistically significant but modest: $r^2 \approx 1.3\text{--}1.7\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\rho = 0.144\text{--}0.227$ across all pairs, strengthening to $\rho = 0.27\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).
35	
36	\looseness=-1
37	The remaining variance reflects entity frequency, prompt position \citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\sim}$22\% of RE accuracy variance on FewRel (\S\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\ref{app:scs-baselines}). Appendix~\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.
38	
39	\begin{figure*}[t]
40	\centering
41	\includegraphics[width=\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}
42	\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\rho = 0.84\text{--}1.0$; Table~\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\%), but NER missed rates are substantially higher (43--65\%) and non-monotonic.}
43	\label{fig:error_taxonomy}
44	\end{figure*}
45	
46	\subsection{BCS-Controlled Experiments}
47	\label{sec:bcs_controlled}
48	
49	\looseness=-1
50	On FewRel, BCS explains ${\sim}$22\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\,=\,1.18$). DocRED partial correlation ($r_{\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\,=\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\ref{sec:appendix_partial_corr}, Table~\ref{tab:partial_corr}).} the within-pool analysis (\S\ref{sec:within_pool}) controls for pool composition.
51	
52	In BCS-controlled FewRel subsets, the high-BCS quartile shows $\Delta=-5.3$\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\,pp (95\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\,=\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\,pp at count 8, $-$31.8\,pp at count 16) and confirms monotonic decline.
53	
54	\paragraph{Document-level RE (DocRED).}
55	The effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\footnote{DocRED uses 5 batches per count level (vs.\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\,pp at count 16 ($\rho = -0.762$, 95\% CI [$-$0.88, $-$0.58]) and $-$15.7\,pp at count 32 ($\rho = -0.693$, 95\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\,=\,50.9$): semipartial $R^2_{\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\% of the explained variance is shared with centrality. Given VIF${}\,=\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\,=\,1.18$).
56	
57	\paragraph{Within-pool controlled comparison.}
58	\label{sec:within_pool}
59	Within-pool analysis confirms slope consistency across pools (permutation $p \approx 0.60$; Appendix~\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\S\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.
60	
61	\paragraph{Practical magnitude.}
62	\label{sec:practical_magnitude}
63	\looseness=-1
64	Direct regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\text{BCS}} = 0.056$ after centrality; Appendix~\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\,pp (95\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\% vs.\ 78.9\% for top-quartile ($\Delta = 3.9$\,pp). The amplification from pairwise $r^2 \approx 1.5\%$ to batch-level $R^2 \approx 22\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\sim}3\times$ amplification illustrated by Monte Carlo simulation; Appendix~\ref{app:aggregation-sim}).
65	
66	\paragraph{Cross-model validation.}
67	\looseness=-1
68	The effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\,pp (count 8) and $-$23.9\,pp (count 16), reaching 77--87\% of Qwen3-32B's gap (Table~\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\Delta = -17.6$\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \to -0.42$, $p = 0.22$; Spearman: $\rho = -0.40 \to -0.18$, $p = 0.64$; Appendix~\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\ref{tab:cross_model_ner_null}).
69	
70	\paragraph{Prompt sensitivity.}
71	\looseness=-1
72	Under the v2 prompt, the extreme-batch BCS gap is $-$25.5\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \approx 0$, $n = 450$; \S\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \leq -0.47$; Appendix~\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\ref{sec:appendix_fewshot_bcs}).
73	
74	\subsection{Multi-Dimensional Degradation}
75	\label{sec:multi_channel}
76	
77	\looseness=-1
78	Error taxonomy decomposition (Table~\ref{tab:error_taxonomy} and Figure~\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\% of errors in high-BCS batches vs.\ 15\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\text{--}27.5\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\ref{tab:cross_model_error_taxonomy}).
79	
80	\looseness=-1
81	These results establish two dimensions: \textbf{Dimension~1} (count predicts recall decline) and \textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\,pp yields $\pm 2.3$\,pp. Both converge on $\pm 2\text{--}3$\,pp.\footnote{Margin sensitivity (Table~\ref{tab:tost_sensitivity}) confirms equivalence from $\pm 2$\,pp ($p = 0.047$) through $\pm 5$\,pp.} On the linear scale, TOST \citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\pm 3$\,pp ($p = 0.003$); at $\pm 2$\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\pm 3$\,pp; Appendix~\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\,pp, consistent with bounded interaction (Appendix~\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\S\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\%) limits statistical detection power to 65\% (Appendix~\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\,=\,0.027$, the minimum detectable correlation is $|r| \approx 0.132$ ($\alpha = 0.05$, power${}\,=\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\ref{app:relaxed-matching}). Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\ref{app:renaming},~\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.
82	
83	\subsection{Centrality as a Potential Confound on Homogeneous Schemas}
84	\label{sec:centrality_confound}
85	\looseness=-1
86	Per-type analysis on MAVEN reveals an anomalous \emph{positive} BCS--F1 correlation ($\rho = +0.184\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "7b35181c-c842-4dfb-a706-365a3e109727",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nAll experiments use Qwen3-32B and the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\looseness=-1\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\n\\looseness=-1\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\n\\looseness=-1\nThe remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}, Table~\\ref{tab:partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. Given VIF${}\\,=\\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\looseness=-1\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).\n\n\\looseness=-1\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.\n\n\\subsection{Centrality as a Potential Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\\looseness=-1\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation ($\\rho = +0.184\\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \\citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01Kh121tvNhwLcYbpsgVhudD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "365175d2-ac60-4e39-8a29-f72f8d20d0c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 24 · 2026-05-22T06:38:26.416Z_

<details><summary>↩ Tool result · `toolu_01Kh121tvNhwLcYbpsgVhudD`</summary>

```text
1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	\paragraph{Boundary conditions.}
5	\looseness=-1
6	The confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\S\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\S\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\ref{sec:appendix_ner_power}).
7	
8	\paragraph{Practical implications and conclusion.}
9	\label{sec:conclusion}
10	\looseness=-1
11	For NER, reducing candidate types is the primary lever; for RE, pre-computing SCS flags high-risk type pairs before deployment. Decompose-then-merge fails (\S\ref{sec:sdgd}), but oracle routing recovers accuracy, confirming approximate additivity of count and confusability (\S\ref{sec:multi_channel}); separability holds on the linear scale but remains open on the logit scale.
12	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "ad8ba6e0-1545-4bee-baac-23535b766848",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/discussion.tex",
      "content": "\\section{Discussion and Conclusion}\n\\label{sec:discussion}\n\n\\paragraph{Boundary conditions.}\n\\looseness=-1\nThe confusability signal applies to cross-domain schemas; same-domain schemas exhibit centrality confounding (\\S\\ref{sec:centrality_confound}). Modest pairwise $r^2$ compounds at the batch level because correlated type interactions aggregate within shared prompts (\\S\\ref{sec:bcs_controlled}). The NER--RE asymmetry reflects dispersed error modes and compressed BCS variance (Appendix~\\ref{sec:appendix_ner_power}).\n\n\\paragraph{Practical implications and conclusion.}\n\\label{sec:conclusion}\n\\looseness=-1\nFor NER, reducing candidate types is the primary lever; for RE, pre-computing SCS flags high-risk type pairs before deployment. Decompose-then-merge fails (\\S\\ref{sec:sdgd}), but oracle routing recovers accuracy, confirming approximate additivity of count and confusability (\\S\\ref{sec:multi_channel}); separability holds on the linear scale but remains open on the logit scale.\n",
      "numLines": 12,
      "startLine": 1,
      "totalLines": 12
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01LCToPkD4TbGuGCDuAy2EUK`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0dcd6683-77a1-49b0-a58d-5aa18187186f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 26 · 2026-05-22T06:38:26.887Z_

<details><summary>↩ Tool result · `toolu_01LCToPkD4TbGuGCDuAy2EUK`</summary>

```text
1	\section{Schema Decomposition}
2	\label{sec:sdgd}
3	
4	\looseness=-1
5	A natural intervention is to partition the schema so confusable types never co-occur. We tested Schema-DAG-Guided Decomposition (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches. While oracle routing recovers accuracy (0.802 vs.\ 0.504 single-pass), all practical routing strategies fall below the single-pass baseline, and NER decomposition amplifies false positives (F1: 0.445$\to$0.251). The bottleneck is routing accuracy rather than partitioning quality. Full protocol, results, and analysis are in Appendix~\ref{sec:appendix_sdgd}.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "865b820a-d61d-486c-9596-b39f16b4d428",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/sdgd_negative.tex",
      "content": "\\section{Schema Decomposition}\n\\label{sec:sdgd}\n\n\\looseness=-1\nA natural intervention is to partition the schema so confusable types never co-occur. We tested Schema-DAG-Guided Decomposition (SDGD), which applies greedy graph coloring on the SCS graph to assign types to low-confusability batches. While oracle routing recovers accuracy (0.802 vs.\\ 0.504 single-pass), all practical routing strategies fall below the single-pass baseline, and NER decomposition amplifies false positives (F1: 0.445$\\to$0.251). The bottleneck is routing accuracy rather than partitioning quality. Full protocol, results, and analysis are in Appendix~\\ref{sec:appendix_sdgd}.\n",
      "numLines": 6,
      "startLine": 1,
      "totalLines": 6
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01V9m1n4RQ383ZL7dTazDMA2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "ece0071e-36e8-42dd-9898-7ad5d0cf7e9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 28 · 2026-05-22T06:38:27.415Z_

<details><summary>↩ Tool result · `toolu_01V9m1n4RQ383ZL7dTazDMA2`</summary>

```text
1	% DEPRECATED — this file is no longer included in main.tex.
2	% The active conclusion is in discussion.tex (\input{discussion}).
3	% Kept for reference only; safe to delete.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "2403efc0-2c07-4002-a3cb-aed17285f3ed",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/conclusion.tex",
      "content": "% DEPRECATED — this file is no longer included in main.tex.\n% The active conclusion is in discussion.tex (\\input{discussion}).\n% Kept for reference only; safe to delete.\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01T2Rt8jmQkSEMyuASVTaih7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f891bc0a-3e4f-4769-a78a-b79ebfdbfefb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 30 · 2026-05-22T06:38:27.937Z_

<details><summary>↩ Tool result · `toolu_01T2Rt8jmQkSEMyuASVTaih7`</summary>

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
10	
11	\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
12	
13	\author{Anonymous}
14	
15	\begin{document}
16	\maketitle
17	
18	All supplementary material is included in the appendix of the main paper.
19	
20	\end{document}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f6f26937-5d63-41c9-a1b0-47e8eb562dd9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/supplementary.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\n\\title{Supplementary Material for: How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\nAll supplementary material is included in the appendix of the main paper.\n\n\\end{document}\n",
      "numLines": 21,
      "startLine": 1,
      "totalLines": 21
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Read · `toolu_01WcANnUHxgRugfgvk4RhuDW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "65b3c112-8626-4633-85e2-4c138ac0b9cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 32 · 2026-05-22T06:38:28.879Z_

<details><summary>↩ Tool result · `toolu_01WcANnUHxgRugfgvk4RhuDW`</summary>

```text
1	\lstset{
2	  basicstyle=\ttfamily\small,
3	  breaklines=true,
4	  breakatwhitespace=true,
5	  columns=fullflexible
6	}
7	
8	\section{Prompt Templates}
9	\label{sec:appendix_prompts}
10	
11	This appendix reproduces the complete prompt templates used for all three extraction tasks.
12	All prompts are injected into a single \texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.
13	Both versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \emph{not} included in the natural-language prompt itself.
14	We use greedy decoding (\texttt{temperature=0}, \texttt{seed=42}) throughout.
15	
16	\medskip\noindent
17	\textbf{Notation.}
18	Placeholders are shown in \texttt{\{braces\}}.
19	Text \textbf{added in v2} (relative to v1) is marked with $\triangleright$.
20	Text \textbf{removed in v2} is marked with \sout{strikethrough}.
21	
22	\subsection{Named Entity Recognition (Few-NERD)}
23	
24	\paragraph{v1 prompt (with character offsets).}
25	
26	\begin{small}
27	\begin{lstlisting}
28	Extract all named entities from the following text.
29	Only extract entities of the following types:
30	- {type_1}: {definition_1}
31	- {type_2}: {definition_2}
32	  ...
33	
34	Text: {input_text}
35	
36	Output as JSON: [{"text": "...", "type": "...",
37	                  "start": ..., "end": ...}]
38	\end{lstlisting}
39	\end{small}
40	
41	\noindent
42	\textbf{v1 constrained-decoding schema:}
43	\begin{small}
44	\begin{lstlisting}
45	{"type": "array",
46	 "items": {"type": "object",
47	   "properties": {
48	     "text":  {"type": "string"},
49	     "type":  {"type": "string",
50	               "enum": [&lt;sorted_types>]},
51	     "start": {"type": "integer"},
52	     "end":   {"type": "integer"}},
53	   "required": ["text","type","start","end"]}}
54	\end{lstlisting}
55	\end{small}
56	
57	\paragraph{v2 prompt (text+type only).}
58	
59	\begin{small}
60	\begin{lstlisting}
61	Extract all named entities from the following text.
62	Only extract entities of the following types:
63	- {type_1}: {definition_1}
64	- {type_2}: {definition_2}
65	  ...
66	
67	Text: {input_text}
68	\end{lstlisting}
69	\end{small}
70	\vspace{-0.5em}
71	\noindent$\triangleright$~\textbf{Added in v2:}
72	\begin{small}
73	\begin{lstlisting}
74	Only extract entities that clearly match one of the
75	given types. If no entities of these types exist in
76	the text, output an empty list [].
77	\end{lstlisting}
78	\end{small}
79	\vspace{-0.5em}
80	\begin{small}
81	\begin{lstlisting}
82	Output as JSON: [{"text": "...", "type": "..."}]
83	\end{lstlisting}
84	\end{small}
85	
86	\noindent
87	\textbf{v2 constrained-decoding schema:}
88	\begin{small}
89	\begin{lstlisting}
90	{"type": "array",
91	 "items": {"type": "object",
92	   "properties": {
93	     "text": {"type": "string"},
94	     "type": {"type": "string",
95	              "enum": [&lt;sorted_types>]}},
96	   "required": ["text","type"]}}
97	\end{lstlisting}
98	\end{small}
99	
100	\paragraph{v1 $\to$ v2 differences (NER).}
101	\begin{enumerate}[leftmargin=*,itemsep=2pt]
102	\item \textbf{Offset fields removed.} The \texttt{start}/\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\% of predicted offsets were hallucinated (\S\ref{sec:model}).
103	\item \textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \ldots output an empty list~\texttt{[]}'' provides an explicit empty-output path.
104	\end{enumerate}
105	
106	\subsection{Event Detection (MAVEN)}
107	
108	\paragraph{v1 prompt (with character offsets).}
109	
110	\begin{small}
111	\begin{lstlisting}
112	Extract all event triggers from the following text.
113	A trigger is the word or phrase that most clearly
114	expresses the event occurrence. Only extract triggers
115	of the following event types:
116	- {type_1}: {definition_1}
117	- {type_2}: {definition_2}
118	  ...
119	
120	Text: {input_text}
121	
122	Output as JSON: [{"text": "...", "type": "...",
123	                  "start": ..., "end": ...}]
124	\end{lstlisting}
125	\end{small}
126	
127	\paragraph{v2 prompt (text+type only).}
128	
129	\begin{small}
130	\begin{lstlisting}
131	Extract all event triggers from the following text.
132	A trigger is the word or phrase that most clearly
133	expresses the event occurrence. Only extract triggers
134	of the following event types:
135	- {type_1}: {definition_1}
136	- {type_2}: {definition_2}
137	  ...
138	
139	Text: {input_text}
140	\end{lstlisting}
141	\end{small}
142	\vspace{-0.5em}
143	\noindent$\triangleright$~\textbf{Added in v2:}
144	\begin{small}
145	\begin{lstlisting}
146	Only extract triggers that clearly match one of the
147	given event types. If no events of these types exist
148	in the text, output an empty list [].
149	\end{lstlisting}
150	\end{small}
151	\vspace{-0.5em}
152	\begin{small}
153	\begin{lstlisting}
154	Output as JSON: [{"text": "...", "type": "..."}]
155	\end{lstlisting}
156	\end{small}
157	
158	\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').
159	
160	\paragraph{v1 $\to$ v2 differences (ED).}
161	Same two changes as NER: offset fields removed, format constraints added.
162	
163	\subsection{Relation Extraction (FewRel)}
164	
165	RE uses only a v2-style prompt (no offset fields are applicable to classification).
166	
167	\paragraph{Prompt.}
168	
169	\begin{small}
170	\begin{lstlisting}
171	Given the following sentence and two entities,
172	classify the relation between them.
173	
174	Sentence: "{sentence}"
175	Head entity: "{head_entity}"
176	Tail entity: "{tail_entity}"
177	
178	Candidate relations: {type_1}, {type_2}, ...
179	
180	Output a single JSON object:
181	  {"relation": "&lt;relation_type>"}
182	If none of the candidate relations apply, output:
183	  {"relation": "none"}
184	\end{lstlisting}
185	\end{small}
186	
187	\noindent
188	\textbf{Constrained-decoding schema:}
189	\begin{small}
190	\begin{lstlisting}
191	{"type": "object",
192	 "properties": {
193	   "relation": {"type": "string",
194	     "enum": [&lt;sorted_types>, "none"]}},
195	 "required": ["relation"]}
196	\end{lstlisting}
197	\end{small}
198	
199	\subsection{Type Definitions}
200	\label{sec:appendix_type_defs}
201	
202	All prompts include per-type natural-language definitions sourced from the respective dataset documentation:
203	\begin{itemize}[leftmargin=*,itemsep=2pt]
204	\item \textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \citep{fewnerd-2021}.
205	\item \textbf{MAVEN:} 168 event types with FrameNet-based definitions \citep{maven-2020}.
206	\item \textbf{FewRel:} 80 relation types with Wikidata property descriptions \citep{fewrel-2018}.
207	\end{itemize}
208	
209	\noindent Type definitions are injected as ``\texttt{- \{type\_name\}: \{definition\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \S\ref{sec:exp_design}).
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "acb2d5c8-f50e-4d28-8b8c-03cf01843ad4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/prompt_appendix.tex",
      "content": "\\lstset{\n  basicstyle=\\ttfamily\\small,\n  breaklines=true,\n  breakatwhitespace=true,\n  columns=fullflexible\n}\n\n\\section{Prompt Templates}\n\\label{sec:appendix_prompts}\n\nThis appendix reproduces the complete prompt templates used for all three extraction tasks.\nAll prompts are injected into a single \\texttt{user} message (no system prompt); the model's chat template adds the system/assistant framing.\nBoth versions provide a JSON-formatted type schema to the vLLM constrained-decoding engine; the schema is \\emph{not} included in the natural-language prompt itself.\nWe use greedy decoding (\\texttt{temperature=0}, \\texttt{seed=42}) throughout.\n\n\\medskip\\noindent\n\\textbf{Notation.}\nPlaceholders are shown in \\texttt{\\{braces\\}}.\nText \\textbf{added in v2} (relative to v1) is marked with $\\triangleright$.\nText \\textbf{removed in v2} is marked with \\sout{strikethrough}.\n\n\\subsection{Named Entity Recognition (Few-NERD)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v1 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\":  {\"type\": \"string\"},\n     \"type\":  {\"type\": \"string\",\n               \"enum\": [&lt;sorted_types>]},\n     \"start\": {\"type\": \"integer\"},\n     \"end\":   {\"type\": \"integer\"}},\n   \"required\": [\"text\",\"type\",\"start\",\"end\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all named entities from the following text.\nOnly extract entities of the following types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract entities that clearly match one of the\ngiven types. If no entities of these types exist in\nthe text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{v2 constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"array\",\n \"items\": {\"type\": \"object\",\n   \"properties\": {\n     \"text\": {\"type\": \"string\"},\n     \"type\": {\"type\": \"string\",\n              \"enum\": [&lt;sorted_types>]}},\n   \"required\": [\"text\",\"type\"]}}\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v1 $\\to$ v2 differences (NER).}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Offset fields removed.} The \\texttt{start}/\\texttt{end} integer fields are dropped from both the natural-language instruction and the JSON schema. In v1, 96.5\\% of predicted offsets were hallucinated (\\S\\ref{sec:model}).\n\\item \\textbf{Format constraints added.} Two sentences are appended: (a)~``Only extract entities that clearly match one of the given types'' suppresses spurious predictions; (b)~``If no entities \\ldots output an empty list~\\texttt{[]}'' provides an explicit empty-output path.\n\\end{enumerate}\n\n\\subsection{Event Detection (MAVEN)}\n\n\\paragraph{v1 prompt (with character offsets).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\",\n                  \"start\": ..., \"end\": ...}]\n\\end{lstlisting}\n\\end{small}\n\n\\paragraph{v2 prompt (text+type only).}\n\n\\begin{small}\n\\begin{lstlisting}\nExtract all event triggers from the following text.\nA trigger is the word or phrase that most clearly\nexpresses the event occurrence. Only extract triggers\nof the following event types:\n- {type_1}: {definition_1}\n- {type_2}: {definition_2}\n  ...\n\nText: {input_text}\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\noindent$\\triangleright$~\\textbf{Added in v2:}\n\\begin{small}\n\\begin{lstlisting}\nOnly extract triggers that clearly match one of the\ngiven event types. If no events of these types exist\nin the text, output an empty list [].\n\\end{lstlisting}\n\\end{small}\n\\vspace{-0.5em}\n\\begin{small}\n\\begin{lstlisting}\nOutput as JSON: [{\"text\": \"...\", \"type\": \"...\"}]\n\\end{lstlisting}\n\\end{small}\n\n\\noindent The JSON schemas for ED are identical to the NER schemas above; only the natural-language framing differs (``event triggers'' instead of ``named entities'').\n\n\\paragraph{v1 $\\to$ v2 differences (ED).}\nSame two changes as NER: offset fields removed, format constraints added.\n\n\\subsection{Relation Extraction (FewRel)}\n\nRE uses only a v2-style prompt (no offset fields are applicable to classification).\n\n\\paragraph{Prompt.}\n\n\\begin{small}\n\\begin{lstlisting}\nGiven the following sentence and two entities,\nclassify the relation between them.\n\nSentence: \"{sentence}\"\nHead entity: \"{head_entity}\"\nTail entity: \"{tail_entity}\"\n\nCandidate relations: {type_1}, {type_2}, ...\n\nOutput a single JSON object:\n  {\"relation\": \"&lt;relation_type>\"}\nIf none of the candidate relations apply, output:\n  {\"relation\": \"none\"}\n\\end{lstlisting}\n\\end{small}\n\n\\noindent\n\\textbf{Constrained-decoding schema:}\n\\begin{small}\n\\begin{lstlisting}\n{\"type\": \"object\",\n \"properties\": {\n   \"relation\": {\"type\": \"string\",\n     \"enum\": [&lt;sorted_types>, \"none\"]}},\n \"required\": [\"relation\"]}\n\\end{lstlisting}\n\\end{small}\n\n\\subsection{Type Definitions}\n\\label{sec:appendix_type_defs}\n\nAll prompts include per-type natural-language definitions sourced from the respective dataset documentation:\n\\begin{itemize}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Few-NERD:} 66 fine-grained entity types with definitions derived from the Few-NERD type ontology \\citep{fewnerd-2021}.\n\\item \\textbf{MAVEN:} 168 event types with FrameNet-based definitions \\citep{maven-2020}.\n\\item \\textbf{FewRel:} 80 relation types with Wikidata property descriptions \\citep{fewrel-2018}.\n\\end{itemize}\n\n\\noindent Type definitions are injected as ``\\texttt{- \\{type\\_name\\}: \\{definition\\}}'' lines in alphabetical order. The number of types per prompt varies by experimental condition (count${}= 1$ to full schema; \\S\\ref{sec:exp_design}).\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01H9r5LJ7EgciezZHPvMjoML`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f963a89c-f931-48d4-8690-b445342621ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JMyhRMNtKBEhQG3Ni2pBgL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 592,
      "cache_read_input_tokens": 24576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 592
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

_source line 34 · 2026-05-22T06:38:28.996Z_

<details><summary>↩ Tool result · `toolu_01H9r5LJ7EgciezZHPvMjoML`</summary>

```text
1	\section*{Responsible NLP Research Checklist}
2	
3	For each question, the answer is \textbf{Yes}, \textbf{No}, or \textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.
4	
5	\subsection*{A \quad For Every Submission}
6	
7	\begin{enumerate}[label=\textbf{A\arabic*.},leftmargin=*,itemsep=4pt]
8	
9	\item \textbf{Did you describe the limitations of your work?}
10	
11	Yes. The Limitations section (after \S\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.
12	
13	\item \textbf{Did you discuss any potential risks of your work?}
14	
15	Yes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.
16	
17	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
18	
19	Yes. The abstract and \S\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.
20	
21	\item \textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}
22	
23	Yes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.
24	
25	\end{enumerate}
26	
27	\subsection*{B \quad Scientific Artifacts}
28	
29	\begin{enumerate}[label=\textbf{B\arabic*.},leftmargin=*,itemsep=4pt]
30	
31	\item \textbf{Did you cite the creators of artifacts you used?}
32	
33	Yes. Few-NERD \citep{fewnerd-2021}, FewRel \citep{fewrel-2018}, DocRED \citep{docred-2019}, MAVEN \citep{maven-2020}, Qwen3-32B \citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \citep{llama3-2024}, Gemini 2.5 Flash \citep{gemini-2025}, vLLM \citep{vllm-2023}, and all-MiniLM-L6-v2 \citep{minilm-2020} are cited in \S\ref{sec:datasets} and \S\ref{sec:model}.
34	
35	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
36	
37	Yes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.
38	
39	\item \textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}
40	
41	Yes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.
42	
43	\item \textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}
44	
45	N/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.
46	
47	\item \textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}
48	
49	Yes. Table~\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \S\ref{sec:datasets} describes dataset provenance and sampling procedures.
50	
51	\item \textbf{Did you report relevant statistics for your dataset(s)?}
52	
53	Yes. \S\ref{sec:datasets} and Table~\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \S\ref{sec:exp_design}.
54	
55	\end{enumerate}
56	
57	\subsection*{C \quad Computational Experiments}
58	
59	\begin{enumerate}[label=\textbf{C\arabic*.},leftmargin=*,itemsep=4pt]
60	
61	\item \textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}
62	
63	Yes. \S\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).
64	
65	\item \textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}
66	
67	Yes. \S\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \S\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.
68	
69	\item \textbf{Did you report descriptive statistics about your results?}
70	
71	Yes. All key metrics include 95\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \S\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \S\ref{sec:count_curves}--\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.
72	
73	\item \textbf{Did you report implementation details, e.g., versions of packages?}
74	
75	Yes. \S\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\S\ref{sec:scs}). Code and scripts will be released upon acceptance.
76	
77	\end{enumerate}
78	
79	\subsection*{D \quad Human Annotators or Crowdworkers}
80	
81	\begin{enumerate}[label=\textbf{D\arabic*.},leftmargin=*,itemsep=4pt]
82	
83	\item \textbf{Did you report the full text of instructions given to participants?}
84	
85	N/A. No human annotation or crowdsourcing was conducted.
86	
87	\item \textbf{Did you report information about how you recruited and paid participants?}
88	
89	N/A.
90	
91	\item \textbf{Did you discuss whether and how consent was obtained?}
92	
93	N/A.
94	
95	\item \textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}
96	
97	N/A.
98	
99	\item \textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}
100	
101	N/A.
102	
103	\end{enumerate}
104	
105	\subsection*{E \quad AI-Assisted Research}
106	
107	\begin{enumerate}[label=\textbf{E\arabic*.},leftmargin=*,itemsep=4pt]
108	
109	\item \textbf{Did you report the use of AI assistants?}
110	
111	Yes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.
112	
113	\end{enumerate}
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "cf94377d-1ce5-4375-b757-dc16603206e9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/checklist.tex",
      "content": "\\section*{Responsible NLP Research Checklist}\n\nFor each question, the answer is \\textbf{Yes}, \\textbf{No}, or \\textbf{N/A}. If Yes, the relevant section is indicated. If No, a justification is provided.\n\n\\subsection*{A \\quad For Every Submission}\n\n\\begin{enumerate}[label=\\textbf{A\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you describe the limitations of your work?}\n\nYes. The Limitations section (after \\S\\ref{sec:discussion}) discusses model coverage, effect size and statistical design (including TOST equivalence), task scope, causal mechanism, data contamination, and domain/language scope.\n\n\\item \\textbf{Did you discuss any potential risks of your work?}\n\nYes (Limitations). SCS/BCS may be misused as a standalone deployment criterion. Since they are proxies for confusability and do not capture domain-specific ambiguity or downstream harms, they should be used for diagnostic monitoring rather than automatic schema rejection or high-stakes deployment decisions.\n\n\\item \\textbf{Do the abstract and introduction summarize the paper's main claims?}\n\nYes. The abstract and \\S\\ref{sec:introduction} state the two-dimensional degradation pattern (count and confusability), the cross-model consistency check, and the negative SDGD result.\n\n\\item \\textbf{Did you use AI assistants (e.g., ChatGPT, Copilot) when working on this paper?}\n\nYes. We used Claude (Anthropic) for writing assistance and experimental code development. All scientific claims, experimental designs, and analyses were conducted by the authors.\n\n\\end{enumerate}\n\n\\subsection*{B \\quad Scientific Artifacts}\n\n\\begin{enumerate}[label=\\textbf{B\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you cite the creators of artifacts you used?}\n\nYes. Few-NERD \\citep{fewnerd-2021}, FewRel \\citep{fewrel-2018}, DocRED \\citep{docred-2019}, MAVEN \\citep{maven-2020}, Qwen3-32B \\citep{qwen3-2025}, Meta-Llama-3.1-70B-Instruct and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}, Gemini 2.5 Flash \\citep{gemini-2025}, vLLM \\citep{vllm-2023}, and all-MiniLM-L6-v2 \\citep{minilm-2020} are cited in \\S\\ref{sec:datasets} and \\S\\ref{sec:model}.\n\n\\item \\textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}\n\nYes. All four datasets are publicly available research benchmarks. Few-NERD is released under CC-BY-SA 4.0; FewRel, DocRED, and MAVEN are publicly released for research use. Open-weight models are used under their respective licenses; Gemini 2.5 Flash is accessed via the Google API under its terms of service.\n\n\\item \\textbf{Did you discuss if your use of existing artifacts is consistent with their intended use?}\n\nYes. All datasets are used for their intended purpose (IE evaluation). No data is used outside the scope specified by the dataset creators.\n\n\\item \\textbf{Did you discuss whether the data contains personally identifiable information or offensive content?}\n\nN/A. We use established benchmarks that have been vetted by the research community. No new data collection or annotation was performed.\n\n\\item \\textbf{Did you provide documentation of the artifacts, e.g., coverage of languages, coverage of domains, etc.?}\n\nYes. Table~\\ref{tab:datasets} reports type counts, evaluation unit counts, domain characteristics, and BCS ranges for each dataset. \\S\\ref{sec:datasets} describes dataset provenance and sampling procedures.\n\n\\item \\textbf{Did you report relevant statistics for your dataset(s)?}\n\nYes. \\S\\ref{sec:datasets} and Table~\\ref{tab:datasets} report evaluation set sizes, type counts, and sampling methodology. Count levels and batch sizes are specified in \\S\\ref{sec:exp_design}.\n\n\\end{enumerate}\n\n\\subsection*{C \\quad Computational Experiments}\n\n\\begin{enumerate}[label=\\textbf{C\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the number of parameters in the models used, the total computational budget, and computing infrastructure?}\n\nYes. \\S\\ref{sec:model}: Qwen3-32B (32B parameters, FP8), Meta-Llama-3.1-70B-Instruct (70B parameters, FP8), and Meta-Llama-3.1-8B-Instruct (8B parameters). Gemini 2.5 Flash was additionally accessed via API for cross-architecture validation. Inference was conducted on NVIDIA RTX PRO 6000 GPUs (96\\,GB) served via vLLM. Total compute was approximately 72 GPU-hours of inference (no training).\n\n\\item \\textbf{Did you discuss the experimental setup, including hyperparameter search and best-found values?}\n\nYes. \\S\\ref{sec:exp_design} describes both experimental paradigms (count curves and BCS-controlled). \\S\\ref{sec:model} reports decoding parameters (greedy, temperature${}=0$, seed${}=42$) and prompt versions. No hyperparameter search was conducted as this is a zero-shot evaluation study.\n\n\\item \\textbf{Did you report descriptive statistics about your results?}\n\nYes. All key metrics include 95\\% bootstrap confidence intervals (10{,}000 resamples, percentile method) as stated in \\S\\ref{sec:model}. Spearman correlations are reported with $p$-values throughout \\S\\ref{sec:count_curves}--\\ref{sec:centrality_confound}. Permutation tests are used for slope comparisons.\n\n\\item \\textbf{Did you report implementation details, e.g., versions of packages?}\n\nYes. \\S\\ref{sec:model} specifies vLLM v0.20.2 for model serving. Embedding models are named with version identifiers (\\S\\ref{sec:scs}). Code and scripts will be released upon acceptance.\n\n\\end{enumerate}\n\n\\subsection*{D \\quad Human Annotators or Crowdworkers}\n\n\\begin{enumerate}[label=\\textbf{D\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the full text of instructions given to participants?}\n\nN/A. No human annotation or crowdsourcing was conducted.\n\n\\item \\textbf{Did you report information about how you recruited and paid participants?}\n\nN/A.\n\n\\item \\textbf{Did you discuss whether and how consent was obtained?}\n\nN/A.\n\n\\item \\textbf{Did you report whether the data collection was approved by an institutional review board (IRB)?}\n\nN/A.\n\n\\item \\textbf{Did you report the basic demographic and geographic characteristics of the annotator population?}\n\nN/A.\n\n\\end{enumerate}\n\n\\subsection*{E \\quad AI-Assisted Research}\n\n\\begin{enumerate}[label=\\textbf{E\\arabic*.},leftmargin=*,itemsep=4pt]\n\n\\item \\textbf{Did you report the use of AI assistants?}\n\nYes. See A4 above. AI assistants were used for code development and document formatting. The research design, execution, and interpretation are the authors' own work.\n\n\\end{enumerate}\n",
      "numLines": 114,
      "startLine": 1,
      "totalLines": 114
    }
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the main.tex file to understand the full structure, including any limitations section and appendix content. Let me read it in parts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f50aede1-2fa1-4e65-b83d-4c2a20de5b50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgmAsdy6FEFU95rcbrcyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32424,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32424
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

_source line 36_

Now let me read main.tex in parts (it was too large to read at once).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "900a6578-8d02-46b4-9b56-7a0d3208ab73",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgmAsdy6FEFU95rcbrcyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32424,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32424
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

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_013wB2jtBd2U8NTjUsdVTE73`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "6d551175-6962-43b2-8af4-737eb9863697",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEgmAsdy6FEFU95rcbrcyP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 32424,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 32424
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

_source line 38 · 2026-05-22T06:38:34.427Z_

<details><summary>↩ Tool result · `toolu_013wB2jtBd2U8NTjUsdVTE73`</summary>

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
10	\usepackage{graphicx}
11	\usepackage{booktabs}
12	\usepackage{amsmath}
13	\usepackage{enumitem}
14	\usepackage[normalem]{ulem}
15	\usepackage{listings}
16	
17	\title{How Does Schema Complexity Predict Performance\\in Training-Free LLM Information Extraction?}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\input{abstract}
25	
26	\input{introduction}
27	
28	\input{related_work}
29	
30	\input{experimental_setup}
31	
32	\input{results}
33	
34	\input{sdgd_negative}
35	
36	\input{discussion}
37	
38	\section*{Limitations}
39	\begin{enumerate}[leftmargin=*,itemsep=2pt]
40	\item \textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\S\ref{sec:multi_channel}) and SDGD failure analysis (\S\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\;{-}0.80 \to {-}0.42$; Appendix~\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.
41	
42	\item \textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\,=\,0$) yields residual SD${}\,=\,0.88$\,pp, approximately 18--44\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\,pp) is far inside the $\pm 3$\,pp equivalence margin.
43	
44	\item \textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.
45	
46	\item \textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\ref{app:split-origin}).
47	\item \textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.
48	\end{enumerate}
49	
50	\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.
51	
52	\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.
53	
54	% \input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF
55	
56	\bibliography{references}
57	
58	\appendix
59	
60	\section{Additional Figures}
61	\label{sec:appendix_figures}
62	
63	\begin{table}[h]
64	\centering
65	\small
66	\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\S\ref{sec:model}) for fair cross-model comparison; the count-curve results in \S\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\ 0.64 at count${}\,=\,1$) due to over-prediction under v1.}
67	\label{tab:cross_model}
68	\begin{tabular}{lrr}
69	\toprule
70	\textbf{Count} & \textbf{Llama-3.1-8B} & \textbf{Qwen3-32B} \\
71	\midrule
72	1 & 0.702 & 0.640 \\
73	64 & 0.273 & 0.304 \\
74	\midrule
75	Decline & $-$43\,pp & $-$34\,pp \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\begin{table}[h]
81	\centering
82	\small
83	\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\approx$51\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\Delta$, in pp) is 77--87\% as large on Llama-3.1-8B as on Qwen3-32B.}
84	\label{tab:cross_model_bcs}
85	\resizebox{\columnwidth}{!}{%
86	\begin{tabular}{crrrrrr}
87	\toprule
88	& \multicolumn{3}{c}{\textbf{Llama-3.1-8B}} & \multicolumn{3}{c}{\textbf{Qwen3-32B}} \\
89	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
90	\textbf{Count} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} & \textbf{Low} & \textbf{High} & \textbf{$\Delta$} \\
91	\midrule
92	8 & 78.1\% & 51.0\% & $-$27.1 & 82.3\% & 51.0\% & $-$31.2 \\
93	16 & 75.5\% & 51.6\% & $-$23.9 & 82.8\% & 51.6\% & $-$31.2 \\
94	\bottomrule
95	\end{tabular}}
96	\end{table}
97	
98	\begin{table}[h]
99	\centering
100	\small
101	\caption{NER batch-level BCS--F1 correlation across models. $^\dagger$Partial correlation controlling for type frequency. $^\ddagger$LLaMA-70B count\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}
102	\label{tab:cross_model_ner_null}
103	\begin{tabular}{lcl}
104	\toprule
105	\textbf{Model} & \textbf{NER BCS--F1 $r$} & \textbf{Status} \\
106	\midrule
107	Qwen3-32B & $0.004$ ($p = 0.94$) & Null \\
108	LLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\rlap{$^\dagger$} & Null \\
109	LLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\rlap{$^\ddagger$} & Null \\
110	Gemini 2.5 Flash & --- & Not tested \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\begin{table}[h]
116	\centering
117	\small
118	\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}
119	\label{tab:error_taxonomy}
120	\resizebox{\columnwidth}{!}{%
121	\begin{tabular}{llrrrrrrr}
122	\toprule
123	 & & \multicolumn{5}{c}{\textbf{BCS Bin}} & & \\
124	\cmidrule(lr){3-7}
125	\textbf{Task} & \textbf{Error} & \textbf{Solo} & \textbf{Low} & \textbf{Mid} & \textbf{High} & \textbf{V.High} & \textbf{$\rho$} & \textbf{$p$} \\
126	\midrule
127	NER & IntraSub & 0\% & 1.6\% & 10.6\% & 49.4\% & --- & 1.000 & ${<}0.001$ \\
128	RE  & IntraSub & 0\% & 4.2\% & 13.0\% & 20.3\% & 32.3\% & 0.954 & ${<}\,0.001$ \\
129	DocRE & IntraSub & --- & 4.8\% & 22.4\% & 37.0\% & 41.9\% & 0.843 & ${<}\,0.001$ \\
130	\midrule
131	NER & Missed & --- & 42.8\% & 64.8\% & 49.9\% & --- & --- & --- \\
132	RE  & Missed & --- & 10.4\% & 11.3\% & 13.1\% & 15.7\% & --- & --- \\
133	DocRE & Missed & --- & 28.1\% & 22.6\% & 21.6\% & 16.2\% & --- & --- \\
134	\bottomrule
135	\end{tabular}}
136	\end{table}
137	
138	\begin{table}[t]
139	\centering
140	\small
141	\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\dagger$LLaMA-70B has only 20 batches with 17.4\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}
142	\label{tab:cross_model_error_taxonomy}
143	\begin{tabular}{lrcc}
144	\toprule
145	\textbf{Model} & $n$ & $\rho$ & $p$ \\
146	\midrule
147	Qwen3-32B & 154 & 0.954 & ${<}\,0.001$ \\
148	Gemini 2.5 Flash & 60 & 0.821 & ${<}\,0.001$ \\
149	LLaMA-3.1-8B & 54 & 0.430 & 0.001 \\
150	LLaMA-3.1-70B$^\dagger$ & 20 & $-$0.086 & 0.719 \\
151	\bottomrule
152	\end{tabular}
153	\end{table}
154	
155	\section{SDGD Full Protocol and Results}
156	\label{sec:appendix_sdgd}
157	
158	We construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\text{SCS}(t_i, t_j) > \tau$. Greedy graph coloring (\textsc{largest\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.
159	
160	\begin{enumerate}[leftmargin=*,itemsep=2pt]
161	\item Compute pairwise SCS matrix $S_{ij} = \cos(\text{embed}(t_i), \text{embed}(t_j))$.
162	\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \tau$.
163	\item Apply greedy graph coloring (\textsc{largest\_first}) to assign each type a color $c(t)$.
164	\item For each color $k$, form batch $B_k = \{t : c(t) = k\}$ and run extraction on all test instances.
165	\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).
166	\end{enumerate}
167	Oracle routing (Table~\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\% vs.\ 50.4\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.
168	
169	We compare four modes: (i)~\textbf{single\_pass}, the undecomposed baseline; (ii)~\textbf{sdgd\_zero}, SCS-guided partitioning; (iii)~\textbf{random\_batch}, random partitioning with matched batch sizes; and (iv)~\textbf{per\_type}, the extreme case where each type is extracted in isolation.
170	
171	Single-pass extraction achieves F1\,=\,0.445 (P\,=\,0.563, R\,=\,0.368). SDGD obtains F1\,=\,0.251 (P\,=\,0.210, R\,=\,0.314), a 44\% relative drop. Random batching reaches F1\,=\,0.320 (P\,=\,0.249, R\,=\,0.446), and per-type extraction yields F1\,=\,0.292 (P\,=\,0.194, R\,=\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\ref{tab:sdgd_results}).
172	
173	\begin{table}[h]
174	\centering
175	\small
176	\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \texttt{min\_batch\_size=8} (reducing 8$\to$4 batches for sdgd\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}
177	\label{tab:sdgd_results}
178	\resizebox{\columnwidth}{!}{%
179	\begin{tabular}{lrccc}
180	\toprule
181	\textbf{Mode} & \textbf{\# Batches} & \textbf{Precision} & \textbf{Recall} & \textbf{F1} \\
182	\midrule
183	single\_pass & 1 & 0.563 & 0.368 & 0.445 \\
184	\midrule
185	sdgd\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\
186	random\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\
187	per\_type & 66 & 0.194 & 0.586 & 0.292 \\
188	\midrule
189	sdgd\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\
190	random\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\
191	\bottomrule
192	\end{tabular}}
193	\end{table}
194	
195	Decomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.
196	
197	Our v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\_zero: 0.210$\to$0.324; random\_batch: 0.249$\to$0.331), but at the cost of disproportionate recall loss (0.314$\to$0.191; 0.446$\to$0.276), and both modes produce lower F1 (sdgd\_zero: 0.251$\to$0.241; random\_batch: 0.320$\to$0.301).
198	
199	\subsection{Practical Routing Strategies on RE}
200	\label{sec:appendix_routing}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "9f88e8bd-e244-4424-b74f-f7bba7ae7ce6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{enumitem}\n\\usepackage[normalem]{ulem}\n\\usepackage{listings}\n\n\\title{How Does Schema Complexity Predict Performance\\\\in Training-Free LLM Information Extraction?}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{abstract}\n\n\\input{introduction}\n\n\\input{related_work}\n\n\\input{experimental_setup}\n\n\\input{results}\n\n\\input{sdgd_negative}\n\n\\input{discussion}\n\n\\section*{Limitations}\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item \\textbf{Model coverage.} Primary experiments use Qwen3-32B; cross-model validation (LLaMA-8B, LLaMA-70B, Gemini Flash) covers Dimensions~1--2 (count curves, BCS-controlled extremes) but does not replicate secondary analyses (error taxonomy, prompt sensitivity, TOST equivalence). Specifically, TOST factorial interaction (\\S\\ref{sec:multi_channel}) and SDGD failure analysis (\\S\\ref{sec:sdgd}) are established on Qwen3-32B alone; error taxonomy replicates on two additional models (Table~\\ref{tab:cross_model_error_taxonomy}), but TOST and SDGD cross-model replication remains the most pressing extension. Gemini provides only partial, leverage-sensitive corroboration (leave-one-out $r{:}\\;{-}0.80 \\to {-}0.42$; Appendix~\\ref{sec:appendix_cross_model_gemini}); proprietary-model generalization remains open.\n\n\\item \\textbf{Effect size and statistical design.} Pairwise SCS explains a small fraction of type confusion variance; entity frequency, prompt position, and mention ambiguity likely account for the remainder. The count $\\times$ BCS interaction is bounded on FewRel but nonzero on DocRED, partially confounded by BCS range restriction at higher counts (Appendix~\\ref{sec:appendix_factorial}); logit-scale evidence remains inconclusive. DocRED count curves use 5 batches per level due to higher per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix~\\ref{app:variance-decomposition}) but precise magnitudes may vary. Greedy decoding (temperature${}\\,=\\,0$) yields residual SD${}\\,=\\,0.88$\\,pp, approximately 18--44\\% of the observed BCS effect size, suggesting effect detection is robust but point estimates carry meaningful uncertainty; the factorial interaction point estimate (0.47\\,pp) is far inside the $\\pm 3$\\,pp equivalence margin.\n\n\\item \\textbf{Task scope.} Format independence is confirmed via paired constrained/unconstrained comparison (Appendix~\\ref{app:format-independence}). BCS batch-level prediction is task-dependent: significant in RE but not detected in NER at current power, where errors scatter across miss, boundary, and type modes rather than concentrating in type substitution. A post-hoc relaxed-matching evaluation confirms that relaxing the span criterion does not recover the BCS signal (Appendix~\\ref{app:relaxed-matching}), ruling out evaluation stringency as the explanation. The NER batch-level BCS null is observed on three models (8B, 32B, 70B; Table~\\ref{tab:cross_model_ner_null}) but not validated on Gemini; the null could in principle differ for proprietary models.\n\n\\item \\textbf{Causal mechanism and data contamination.} The study establishes correlational evidence with controlled stratification; mechanistic analysis at the attention or logit level is needed to confirm the causal pathway. A post-hoc renaming experiment (Appendix~\\ref{app:renaming}) suggests SCS may proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in pretraining corpora, but train-origin relations show lower accuracy than val-origin, opposite to the contamination hypothesis; DocRED (2019) provides a lower-contamination-risk replication (Appendix~\\ref{app:split-origin}).\n\\item \\textbf{Domain and language scope.} All evaluations use English-language datasets derived from Wikipedia or knowledge bases (Wikidata, FrameNet). Whether confusability effects hold for domain-specific schemas (e.g., biomedical NER, legal RE) or languages with different naming conventions is untested. BCS-controlled batches inherit the domain distribution of the source schema; domain-specific type subsets may shift the confusability--accuracy relationship. Sample sizes (1{,}000 instances per dataset) are sufficient for our primary effects but the pairwise SCS correlation approaches the detection floor.\n\\end{enumerate}\n\n\\paragraph{Across-batch correlation.} Batches share prompt template and LLM, introducing potential across-batch correlation; however, type composition is independently sampled per batch, and bootstrap CIs are computed over this independent unit of variation.\n\n\\paragraph{Multiple comparisons.} Few-NERD, FewRel, and DocRED draw from overlapping knowledge bases (Wikipedia, Wikidata), limiting dataset independence; we treat cross-dataset consistency as converging evidence rather than independent statistical replication \\citep{rothman-1990} (noting that within-study prompt comparisons involve correlated observations rather than independent tests). Within-dataset secondary analyses involve multiple looks; we report individual $p$-values and note that core claims rest on $p < 0.001$ \\citep{dror-2018-significance,card-2020-power}. The core claims (count decline, BCS--accuracy correlation) are robust to Bonferroni correction (all $p < 0.001$); the logit-scale interaction ($p = 0.047$) is the only result near the threshold and is already characterized as marginal.\n\n% \\input{checklist}  % EMNLP 2026: checklist goes in OpenReview form, not PDF\n\n\\bibliography{references}\n\n\\appendix\n\n\\section{Additional Figures}\n\\label{sec:appendix_figures}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count-curve replication on Few-NERD (text-match recall). Both models show a general declining trend in recall with schema size. Per-batch correlation $r = 0.725$. Qwen3-32B values use the v2 prompt (\\S\\ref{sec:model}) for fair cross-model comparison; the count-curve results in \\S\\ref{sec:count_curves} use the v1 prompt, yielding higher absolute recall (0.72 vs.\\ 0.64 at count${}\\,=\\,1$) due to over-prediction under v1.}\n\\label{tab:cross_model}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Llama-3.1-8B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1 & 0.702 & 0.640 \\\\\n64 & 0.273 & 0.304 \\\\\n\\midrule\nDecline & $-$43\\,pp & $-$34\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel accuracy.  High-BCS accuracy converges to $\\approx$51\\% regardless of model, while low-BCS accuracy reflects model capacity differences.  The confusability gap ($\\Delta$, in pp) is 77--87\\% as large on Llama-3.1-8B as on Qwen3-32B.}\n\\label{tab:cross_model_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{crrrrrr}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{Llama-3.1-8B}} & \\multicolumn{3}{c}{\\textbf{Qwen3-32B}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\n\\textbf{Count} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} & \\textbf{Low} & \\textbf{High} & \\textbf{$\\Delta$} \\\\\n\\midrule\n8 & 78.1\\% & 51.0\\% & $-$27.1 & 82.3\\% & 51.0\\% & $-$31.2 \\\\\n16 & 75.5\\% & 51.6\\% & $-$23.9 & 82.8\\% & 51.6\\% & $-$31.2 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{NER batch-level BCS--F1 correlation across models. $^\\dagger$Partial correlation controlling for type frequency. $^\\ddagger$LLaMA-70B count\\_12 shows $r{=}{-}0.42$ ($p{=}0.034$, uncorrected; Bonferroni $p{=}0.069$); pooled and count\\_6 are null, consistent with sampling noise at $n{=}25$. The null is observed on three models; Gemini remains untested.}\n\\label{tab:cross_model_ner_null}\n\\begin{tabular}{lcl}\n\\toprule\n\\textbf{Model} & \\textbf{NER BCS--F1 $r$} & \\textbf{Status} \\\\\n\\midrule\nQwen3-32B & $0.004$ ($p = 0.94$) & Null \\\\\nLLaMA-3.1-8B & $-0.12$ ($p = 0.29$)\\rlap{$^\\dagger$} & Null \\\\\nLLaMA-3.1-70B & $-0.13$ ($p = 0.36$)\\rlap{$^\\ddagger$} & Null \\\\\nGemini 2.5 Flash & --- & Not tested \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Intra-batch substitution (IntraSub) and missed-entity rates by BCS bin. Spearman $\\rho$ computed over $n=148$ batches (NER), $n=154$ (RE), and $n=110$ (DocRE). IntraSub scales monotonically with BCS across all three datasets. DocRE missed rates decrease with BCS, indicating high-confusability errors shift from omission to substitution.}\n\\label{tab:error_taxonomy}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrrrr}\n\\toprule\n & & \\multicolumn{5}{c}{\\textbf{BCS Bin}} & & \\\\\n\\cmidrule(lr){3-7}\n\\textbf{Task} & \\textbf{Error} & \\textbf{Solo} & \\textbf{Low} & \\textbf{Mid} & \\textbf{High} & \\textbf{V.High} & \\textbf{$\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nNER & IntraSub & 0\\% & 1.6\\% & 10.6\\% & 49.4\\% & --- & 1.000 & ${<}0.001$ \\\\\nRE  & IntraSub & 0\\% & 4.2\\% & 13.0\\% & 20.3\\% & 32.3\\% & 0.954 & ${<}\\,0.001$ \\\\\nDocRE & IntraSub & --- & 4.8\\% & 22.4\\% & 37.0\\% & 41.9\\% & 0.843 & ${<}\\,0.001$ \\\\\n\\midrule\nNER & Missed & --- & 42.8\\% & 64.8\\% & 49.9\\% & --- & --- & --- \\\\\nRE  & Missed & --- & 10.4\\% & 11.3\\% & 13.1\\% & 15.7\\% & --- & --- \\\\\nDocRE & Missed & --- & 28.1\\% & 22.6\\% & 21.6\\% & 16.2\\% & --- & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication of IntraSub--BCS Spearman correlation on FewRel RE. $^\\dagger$LLaMA-70B has only 20 batches with 17.4\\% missed rate; the null is attributable to insufficient power rather than absence of the effect.}\n\\label{tab:cross_model_error_taxonomy}\n\\begin{tabular}{lrcc}\n\\toprule\n\\textbf{Model} & $n$ & $\\rho$ & $p$ \\\\\n\\midrule\nQwen3-32B & 154 & 0.954 & ${<}\\,0.001$ \\\\\nGemini 2.5 Flash & 60 & 0.821 & ${<}\\,0.001$ \\\\\nLLaMA-3.1-8B & 54 & 0.430 & 0.001 \\\\\nLLaMA-3.1-70B$^\\dagger$ & 20 & $-$0.086 & 0.719 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{SDGD Full Protocol and Results}\n\\label{sec:appendix_sdgd}\n\nWe construct a thresholded confusability graph $G = (V, E)$ where each type is a vertex and an edge connects types $t_i, t_j$ whenever $\\text{SCS}(t_i, t_j) > \\tau$. Greedy graph coloring (\\textsc{largest\\_first}) assigns each type to a color such that no two adjacent (i.e., highly confusable) types share a color. Each color class forms one extraction batch, and predictions are merged via set union.\n\n\\begin{enumerate}[leftmargin=*,itemsep=2pt]\n\\item Compute pairwise SCS matrix $S_{ij} = \\cos(\\text{embed}(t_i), \\text{embed}(t_j))$.\n\\item Construct graph $G$: add edge $(t_i, t_j)$ iff $S_{ij} > \\tau$.\n\\item Apply greedy graph coloring (\\textsc{largest\\_first}) to assign each type a color $c(t)$.\n\\item For each color $k$, form batch $B_k = \\{t : c(t) = k\\}$ and run extraction on all test instances.\n\\item Merge: union of per-batch predictions (v1) or confidence-gated selection (v2).\n\\end{enumerate}\nOracle routing (Table~\\ref{tab:routing_strategies}) recovers substantial accuracy (72.4\\% vs.\\ 50.4\\% single-pass), confirming the sub-schemas contain correct predictions; the failure lies in routing, not decomposition quality.\n\nWe compare four modes: (i)~\\textbf{single\\_pass}, the undecomposed baseline; (ii)~\\textbf{sdgd\\_zero}, SCS-guided partitioning; (iii)~\\textbf{random\\_batch}, random partitioning with matched batch sizes; and (iv)~\\textbf{per\\_type}, the extreme case where each type is extracted in isolation.\n\nSingle-pass extraction achieves F1\\,=\\,0.445 (P\\,=\\,0.563, R\\,=\\,0.368). SDGD obtains F1\\,=\\,0.251 (P\\,=\\,0.210, R\\,=\\,0.314), a 44\\% relative drop. Random batching reaches F1\\,=\\,0.320 (P\\,=\\,0.249, R\\,=\\,0.446), and per-type extraction yields F1\\,=\\,0.292 (P\\,=\\,0.194, R\\,=\\,0.586). Every decomposition mode falls below the single-pass baseline (Table~\\ref{tab:sdgd_results}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Few-NERD extraction under decomposition modes. V1 uses union merge; v2 uses confidence-gated merge with \\texttt{min\\_batch\\_size=8} (reducing 8$\\to$4 batches for sdgd\\_zero). All decomposition modes produce lower F1 than the single-pass baseline. All modes use the v1 prompt.}\n\\label{tab:sdgd_results}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrccc}\n\\toprule\n\\textbf{Mode} & \\textbf{\\# Batches} & \\textbf{Precision} & \\textbf{Recall} & \\textbf{F1} \\\\\n\\midrule\nsingle\\_pass & 1 & 0.563 & 0.368 & 0.445 \\\\\n\\midrule\nsdgd\\_zero (v1) & 8 & 0.210 & 0.314 & 0.251 \\\\\nrandom\\_batch (v1) & 8 & 0.249 & 0.446 & 0.320 \\\\\nper\\_type & 66 & 0.194 & 0.586 & 0.292 \\\\\n\\midrule\nsdgd\\_zero (v2) & 4 & 0.324 & 0.191 & 0.241 \\\\\nrandom\\_batch (v2) & 8 & 0.331 & 0.276 & 0.301 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDecomposition boosts recall (per-type recall reaches 0.586 versus single-pass 0.368) but devastates precision (0.194 versus 0.563). When the same text is presented to the model $k$ times with different type subsets, each pass independently generates entity predictions. Because LLM outputs are not calibrated across passes, the union merge step accumulates overlapping and contradictory predictions and inflates false positives.\n\nOur v2 merge ranks competing predictions by the LLM's self-reported confidence and retains only the highest-scoring candidate for each span. Confidence gating improves precision (sdgd\\_zero: 0.210$\\to$0.324; random\\_batch: 0.249$\\to$0.331), but at the cost of disproportionate recall loss (0.314$\\to$0.191; 0.446$\\to$0.276), and both modes produce lower F1 (sdgd\\_zero: 0.251$\\to$0.241; random\\_batch: 0.320$\\to$0.301).\n\n\\subsection{Practical Routing Strategies on RE}\n\\label{sec:appendix_routing}",
      "numLines": 200,
      "startLine": 1,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01Loo8NaE7izj8eA9JzHguhM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 200,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f6eda0d7-bab3-4113-b7ea-466c5a56709e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EAobfhHnjc2C7TuekQpZYt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5549,
      "cache_read_input_tokens": 44265,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5549
      },
      "output_tokens": 38,
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

_source line 40 · 2026-05-22T06:38:38.929Z_

<details><summary>↩ Tool result · `toolu_01Loo8NaE7izj8eA9JzHguhM`</summary>

```text
200	\label{sec:appendix_routing}
201	
202	We evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.
203	
204	\begin{table}[h]
205	\centering
206	\small
207	\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\%.}
208	\label{tab:routing_strategies}
209	\resizebox{\columnwidth}{!}{\begin{tabular}{@{}lrr@{}}
210	\toprule
211	\textbf{Strategy} & \textbf{Accuracy} & \textbf{$\Delta$ vs.\ Single-Pass} \\
212	\midrule
213	Oracle (gold label) & 72.4\% & +22.0\,pp \\
214	\midrule
215	Max-conf (positive only) & 36.5\% & $-$14.0\,pp \\
216	None-aware & 36.5\% & $-$14.0\,pp \\
217	Margin (positive only) & 35.9\% & $-$14.5\,pp \\
218	Max-conf (all) & 27.7\% & $-$22.7\,pp \\
219	Random & 14.7\% & $-$35.7\,pp \\
220	\midrule
221	Single-pass (no decomposition) & 50.4\% & --- \\
222	\bottomrule
223	\end{tabular}}
224	\end{table}
225	
226	\section{Factorial Analysis and Separability Test}
227	\label{sec:appendix_factorial}
228	
229	To formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\sim$ $\log_2$\,count $+$ BCS $+$ count$\times$BCS) across 69 batches from FewRel spanning five count levels ($k \in \{4, 8, 16, 32, 40\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\,pp). A TOST equivalence test with a $\pm 3$\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.
230	
231	A $2 \times 2$ factorial sensitivity check on FewRel (count $\in \{8, 16\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\S\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.
232	
233	\paragraph{Equivalence margin justification.}
234	We set the $\pm 3$\,pp margin based on three converging anchors. \emph{External}: evaluation variance in IE benchmarks typically spans 2--5\,pp across random seeds, prompt variations, and data splits \citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \emph{Internal}: $0.5 \times$ within-cell SD ($= 2.3$\,pp) corresponds to Cohen's $d \approx 0.5$ (medium effect threshold; \citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\,pp (\S\ref{sec:practical_magnitude})---an interaction exceeding 3\,pp would represent ${>}130\%$ amplification. \emph{Sensitivity}: Table~\ref{tab:tost_sensitivity} shows equivalence holds from $\pm 2$\,pp ($p = 0.047$) through $\pm 5$\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.
235	
236	\begin{table}[h]
237	\centering
238	\small
239	\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\,pp, 90\% CI [$-$1.0, 2.0]\,pp) is bounded below 2\,pp at marginal significance ($p = 0.047$); the $\pm 3$\,pp choice does not drive the equivalence conclusion. At $\pm 1$\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}
240	\label{tab:tost_sensitivity}
241	\begin{tabular}{crrl}
242	\toprule
243	\textbf{Margin (pp)} & \textbf{$t_{\text{upper}}$} & \textbf{$p_{\text{TOST}}$} & \textbf{Conclusion} \\
244	\midrule
245	$\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\
246	$\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\
247	$\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\
248	$\pm 5$ & $-5.02$ & ${<}\,0.001$ & Equivalent \\
249	\bottomrule
250	\end{tabular}
251	\end{table}
252	
253	\paragraph{Logit-scale sensitivity.}
254	Because accuracy near 50\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\pm 3$\,pp margin ($\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\,pp, still within the $\pm 3$\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\pm 3$\,pp and $p = 0.026$ at $\pm 3.5$\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.
255	
256	\paragraph{DocRED factorial (expanded).}
257	With expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \times 2$ factorial (count $\in \{16, 32\}$, BCS median split) yields an apparent interaction ($-$9.4\,pp, 95\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\,pp at count 16 but $-$15.7\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\ 0.38), limiting achievable extremes.
258	
259	\paragraph{Range-matched robustness check.}
260	To control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\,pp to 9.37\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\,pp. The interaction drops from 7.52\,pp (95\% CI [1.49, 12.83]) to 0.93\,pp (95\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\rho = -0.65$ at count 16, $\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\,pp at 80\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\,pp) interaction.
261	
262	\section{Within-Pool CI Details}
263	\label{sec:appendix_within_pool}
264	
265	The quartile $\Delta$ for 80-pool 16-relation subsets ($-$3.92\,pp, 95\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.
266	
267	\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}
268	\label{sec:appendix_residualized_bcs}
269	
270	Section~\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.
271	
272	\paragraph{Confound identification.}
273	For each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:
274	\begin{itemize}[itemsep=2pt,leftmargin=*]
275	\item \textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.
276	\item \textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.
277	\end{itemize}
278	
279	\paragraph{Partial correlation results.}
280	Table~\ref{tab:residualized_bcs} reports raw Spearman $\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.
281	
282	\begin{table}[h]
283	\centering
284	\small
285	\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \texttt{exp\_maven\_residualized\_bcs}.}
286	\label{tab:residualized_bcs}
287	\resizebox{\columnwidth}{!}{%
288	\begin{tabular}{llcccc}
289	\toprule
290	\textbf{Embedding} & \textbf{Control} & \textbf{Raw $\rho$} & \textbf{Raw $p$} & \textbf{Partial $r$} & \textbf{Partial $p$} \\
291	\midrule
292	MiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\
293	MiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\
294	MiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\
295	\midrule
296	Qwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\
297	Qwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\
298	Qwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\
299	\bottomrule
300	\end{tabular}}
301	\end{table}
302	
303	\paragraph{Interpretation.}
304	The two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.
305	
306	Under joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.
307	
308	\subsection{Partial Correlation: Controlling for Degree Centrality}
309	\label{sec:appendix_partial_corr}
310	
311	To rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).
312	
313	\begin{table}[h]
314	\centering
315	\small
316	\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\,=\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\,=\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}
317	\label{tab:partial_corr}
318	\begin{tabular}{lrrrrr}
319	\toprule
320	\textbf{Dataset} & \textbf{$n$} & \textbf{$r_{\text{zero}}$} & \textbf{$r_{\text{partial}}$} & \textbf{$p_{\text{partial}}$} & \textbf{VIF} \\
321	\midrule
322	FewRel & 204 & $-$0.570 & $-$0.537 & ${<}\,0.001$ & 1.18 \\
323	DocRED & 110 & $-$0.760 & $-$0.348 & ${<}\,0.001$ & 50.9 \\
324	\bottomrule
325	\end{tabular}
326	\end{table}
327	
328	As Table~\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\text{partial}} = -0.537$ vs.\ $r_{\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\S\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.
329	
330	\paragraph{Ridge regression under multicollinearity.}
331	Ridge regression (GCV, $\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\,\approx\,$50.9). The standardized BCS coefficient is $\hat{\beta}_{\textsc{bcs}} = -1.53$ ($\hat{\beta}_{\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\hat{\beta}_{\textsc{bcs}} < 0$ for \emph{all} $\lambda \geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\lambda) \times 0.760 + 0.727$, is negative at $\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.
332	
333	\subsection{NER BCS-Null Power Analysis}
334	\label{sec:appendix_ner_power}
335	
336	The Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\% power at $n = 450$ (below the conventional 80\% threshold). The minimum detectable $|r|$ at 80\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.
337	
338	\subsection{Bootstrap CI Robustness}
339	\label{sec:appendix_bootstrap_ci}
340	
341	Because batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\in \{0.1, \ldots, 0.9\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\%$ to $+6\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.
342	
343	\subsection{Domain Distribution in Extreme-BCS Batches}
344	\label{sec:appendix_domain_distribution}
345	
346	We classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\%) and creative work (25.5\%), while high-BCS batches concentrate on science/taxonomy (49.5\%) and event/temporal (26.0\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.
347	
348	\section{Batch Composition Results}
349	\label{sec:appendix_batch_composition}
350	
351	\begin{table}[h]
352	\centering
353	\small
354	\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\dagger$Mean $\pm$ SD across 15 random seeds.}
355	\label{tab:batch_composition}
356	\resizebox{\columnwidth}{!}{%
357	\begin{tabular}{@{}lcc@{}}
358	\toprule
359	\textbf{Condition} & \textbf{Accuracy} & \textbf{Mean BCS} \\
360	\midrule
361	Single-pass (80 types) & 0.504 & 0.557 \\
362	Random batching (15 seeds)$^\dagger$ & 0.788\,$\pm$\,0.018 & 0.559 \\
363	Confus.-aware (graph coloring) & \textbf{0.802} & 0.552 \\
364	\bottomrule
365	\end{tabular}}
366	\end{table}
367	
368	See the accompanying discussion in \S\ref{sec:sdgd}.
369	
370	\input{prompt_appendix}
371	
372	\section{Prompt Version Sensitivity Analysis}
373	\label{sec:appendix_prompt_sensitivity}
374	
375	We assess whether the confusability effects reported in \S\ref{sec:bcs_controlled}--\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\S\ref{sec:model}; full templates in Appendix~\ref{sec:appendix_prompts}).
376	
377	\paragraph{RE (FewRel).}
378	Under the v1 prompt, the extreme-batch BCS gap (Table~\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\,pp (low-BCS 85.2\% vs.\ high-BCS 59.7\%; 95\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\,pp (95\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.
379	
380	\paragraph{NER (Few-NERD).}
381	The batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\text{BCS}, \text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\S\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.
382	
383	\paragraph{Interpretation.}
384	The $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\% vs.\ 82.3\%), but type confusion under high confusability persists (59.7\% vs.\ 51.0\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.
385	
386	\subsection{Cross-Prompt-Variant BCS Correlation}
387	\label{sec:appendix_prompt_variants}
388	
389	To verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\ref{tab:prompt_variants}).
390	
391	\begin{table}[h]
392	\centering
393	\small
394	\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}
395	\label{tab:prompt_variants}
396	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrr}
397	\toprule
398	\textbf{Variant} & \textbf{Count} & \textbf{Mean Acc} & \textbf{$r$} & \textbf{$p$} \\
399	\midrule
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "4c310b81-a81d-48ff-918d-d969591b27c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\\label{sec:appendix_routing}\n\nWe evaluate five non-oracle routing strategies on FewRel 80-relation RE using graph-coloring sub-schema decomposition (same grouping as Table~\\ref{tab:batch_composition}). Each strategy selects a single sub-schema for each test instance and returns that sub-schema's prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Routing strategy comparison on FewRel 80-relation RE with graph-coloring sub-schema decomposition. Oracle requires gold labels. All practical (non-oracle) strategies perform below the single-pass baseline. The failure stems from constrained decoding (enum constraint), which forces confident predictions in every sub-schema: 73.4\\% of instances receive positive predictions from 3--5 sub-schemas simultaneously, with per-sub-schema none-rates of only 20--40\\%.}\n\\label{tab:routing_strategies}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{@{}lrr@{}}\n\\toprule\n\\textbf{Strategy} & \\textbf{Accuracy} & \\textbf{$\\Delta$ vs.\\ Single-Pass} \\\\\n\\midrule\nOracle (gold label) & 72.4\\% & +22.0\\,pp \\\\\n\\midrule\nMax-conf (positive only) & 36.5\\% & $-$14.0\\,pp \\\\\nNone-aware & 36.5\\% & $-$14.0\\,pp \\\\\nMargin (positive only) & 35.9\\% & $-$14.5\\,pp \\\\\nMax-conf (all) & 27.7\\% & $-$22.7\\,pp \\\\\nRandom & 14.7\\% & $-$35.7\\,pp \\\\\n\\midrule\nSingle-pass (no decomposition) & 50.4\\% & --- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Factorial Analysis and Separability Test}\n\\label{sec:appendix_factorial}\n\nTo formally test whether count and confusability effects are additive, we fit a multiple regression (accuracy $\\sim$ $\\log_2$\\,count $+$ BCS $+$ count$\\times$BCS) across 69 batches from FewRel spanning five count levels ($k \\in \\{4, 8, 16, 32, 40\\}$). Both main effects are significant (count: $p = 0.008$; BCS: $p = 0.0002$; $R^2 = 0.52$), but the interaction term is negligible (0.47\\,pp). A TOST equivalence test with a $\\pm 3$\\,pp margin confirms that the interaction is bounded well below practical significance ($p_{\\text{TOST}} = 0.003$); this supports bounded interaction between count and confusability effects.\n\nA $2 \\times 2$ factorial sensitivity check on FewRel (count $\\in \\{8, 16\\}$, BCS low/high; $n = 54$) was inconclusive ($p_{\\text{TOST}} = 0.56$) due to limited power; this does not contradict the primary finding but limits generalization beyond the regression framework. The Few-NERD factorial (\\S\\ref{sec:multi_channel}) similarly did not reach significance ($p = 0.50$). The regression approach provides the stronger test by leveraging the full count range.\n\n\\paragraph{Equivalence margin justification.}\nWe set the $\\pm 3$\\,pp margin based on three converging anchors. \\emph{External}: evaluation variance in IE benchmarks typically spans 2--5\\,pp across random seeds, prompt variations, and data splits \\citep{card-2020-power,dror-2018-significance}; a within-margin interaction would be indistinguishable from routine evaluation noise. \\emph{Internal}: $0.5 \\times$ within-cell SD ($= 2.3$\\,pp) corresponds to Cohen's $d \\approx 0.5$ (medium effect threshold; \\citealt{lakens-2017-equivalence}), cross-validated against the IQR-predicted confusability main effect of 2.2\\,pp (\\S\\ref{sec:practical_magnitude})---an interaction exceeding 3\\,pp would represent ${>}130\\%$ amplification. \\emph{Sensitivity}: Table~\\ref{tab:tost_sensitivity} shows equivalence holds from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp ($p < 0.001$) on the probability scale; the conclusion is not margin-dependent.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{TOST sensitivity analysis across equivalence margins. The interaction effect (0.47\\,pp, 90\\% CI [$-$1.0, 2.0]\\,pp) is bounded below 2\\,pp at marginal significance ($p = 0.047$); the $\\pm 3$\\,pp choice does not drive the equivalence conclusion. At $\\pm 1$\\,pp, equivalence is inconclusive ($p = 0.278$), meaning interaction could reach approximately half the main effect magnitude.}\n\\label{tab:tost_sensitivity}\n\\begin{tabular}{crrl}\n\\toprule\n\\textbf{Margin (pp)} & \\textbf{$t_{\\text{upper}}$} & \\textbf{$p_{\\text{TOST}}$} & \\textbf{Conclusion} \\\\\n\\midrule\n$\\pm 1$ & $-0.59$ & $0.278$ & Inconclusive \\\\\n$\\pm 2$ & $-1.70$ & $0.047$ & Equivalent \\\\\n$\\pm 3$ & $-2.81$ & $0.003$ & Equivalent \\\\\n$\\pm 5$ & $-5.02$ & ${<}\\,0.001$ & Equivalent \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Logit-scale sensitivity.}\nBecause accuracy near 50\\% compresses interaction effects on the linear scale, we refit the regression on logit-transformed accuracy. The logit-scale interaction (0.111 logit units, $p = 0.047$, 90\\% CI [0.019, 0.203]) is marginally significant, and TOST at the equivalent $\\pm 3$\\,pp margin ($\\pm 0.156$ logit at median accuracy) is inconclusive ($p_{\\text{TOST}} = 0.209$). However, back-transforming the interaction to the probability scale at the observed floor ($p = 0.51$) yields 2.78\\,pp, still within the $\\pm 3$\\,pp margin; at the median baseline ($p = 0.65$), the back-transformed effect is 2.53\\,pp. The logit TOST is inconclusive due to limited power ($n = 69$, wide CI) rather than a large effect size: the point estimate remains below the equivalence bound at all observed baselines. We retain the linear-scale TOST as the primary test and report this logit analysis as a sensitivity check. A regression-based TOST ($n = 375$, five count levels with continuous BCS) yields $p = 0.050$ at $\\pm 3$\\,pp and $p = 0.026$ at $\\pm 3.5$\\,pp on the logit scale, confirming the borderline status with substantially greater power than the factorial design.\n\n\\paragraph{DocRED factorial (expanded).}\nWith expanded batches ($n{=}55$ per count level, up from $n{=}5$), the DocRED $2 \\times 2$ factorial (count $\\in \\{16, 32\\}$, BCS median split) yields an apparent interaction ($-$9.4\\,pp, 95\\% CI [$-$12.9, $-$6.0]): the BCS effect is $-$25.0\\,pp at count 16 but $-$15.7\\,pp at count 32. However, this attenuation is confounded by BCS range restriction: higher-count batches have narrower BCS ranges (spread 0.26 vs.\\ 0.38), limiting achievable extremes.\n\n\\paragraph{Range-matched robustness check.}\nTo control for the BCS range confound, we restrict both count levels to the overlapping BCS range [0.43, 0.70]. This retains 29 of 55 batches at count 16 (all 55 at count 32 fall within the range). Within this matched range, the BCS effect at count 16 shrinks from 15.95\\,pp to 9.37\\,pp (reflecting the narrower BCS span), while count 32 remains at 8.44\\,pp. The interaction drops from 7.52\\,pp (95\\% CI [1.49, 12.83]) to 0.93\\,pp (95\\% CI [$-$7.13, 7.44])---the CI spans zero, consistent with no interaction. Spearman correlations remain comparable ($\\rho = -0.65$ at count 16, $\\rho = -0.69$ at count 32), confirming that the underlying BCS--accuracy relationship is robust across counts while the raw interaction magnitude was an artifact of differing achievable BCS ranges. This result aligns with the FewRel TOST equivalence finding and supports bounded association as the cross-dataset pattern. The reduced sample ($n = 29{+}55$) yields a minimum detectable effect of 5.5\\,pp at 80\\% power, consistent with insufficient power to distinguish a true null from a small ($<$5\\,pp) interaction.\n\n\\section{Within-Pool CI Details}\n\\label{sec:appendix_within_pool}\n\nThe quartile $\\Delta$ for 80-pool 16-relation subsets ($-$3.92\\,pp, 95\\% CI [$-$8.17, $+$0.38]) crosses zero, reflecting the compressed BCS range within that pool (0.46--0.68 vs.\\ 0.48--0.71 for the independent pool). Within this narrow band, the quartile contrast lacks statistical power to detect the effect that the regression identifies. The full 80-relation condition ($n = 25$) is underpowered for both the slope (95\\% CI [$-$1.303, $+$1.695]) and quartile analyses; we include it in Table~\\ref{tab:within_pool} for completeness but do not draw inferential conclusions from it.\n\n\\section{Controlling for Centrality Confounds in MAVEN Per-Type Analysis}\n\\label{sec:appendix_residualized_bcs}\n\nSection~\\ref{sec:centrality_confound} identifies a centrality confound in MAVEN's per-type BCS--F1 correlation: both embeddings show a \\emph{positive} raw correlation, opposite to the expected direction. Here we formalize this analysis by identifying specific confounders for each embedding and testing whether the BCS--F1 relationship survives partial correlation controlling for these confounders.\n\n\\paragraph{Confound identification.}\nFor each embedding, we computed the correlation between mean BCS and candidate confounders (type frequency, degree centrality at threshold 0.7) across MAVEN's 149 active event types. The dominant confound differs by embedding:\n\\begin{itemize}[itemsep=2pt,leftmargin=*]\n\\item \\textbf{MiniLM}: BCS correlates with log type frequency ($r = 0.201$). Frequent types have more training signal and are extracted more reliably, which produces the positive BCS--F1 association.\n\\item \\textbf{Qwen3}: BCS correlates strongly with degree centrality ($r = 0.854$). In the Qwen3 embedding space, high-BCS types are those with many semantic neighbors, central, well-represented types that the model extracts well.\n\\end{itemize}\n\n\\paragraph{Partial correlation results.}\nTable~\\ref{tab:residualized_bcs} reports raw Spearman $\\rho$ and partial Pearson $r$ after controlling for the identified confounders. Under single-variable control, both correlations weaken to non-significance. Under joint control (log frequency $+$ degree centrality simultaneously), neither embedding retains a significant BCS--F1 association.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{MAVEN per-type BCS--F1 correlation before and after controlling for centrality confounders. Raw correlations are Spearman $\\rho$; partial correlations are Pearson $r$ from residualized regression. Degree centrality is computed on the SCS graph at threshold 0.7. All values from experiment \\texttt{exp\\_maven\\_residualized\\_bcs}.}\n\\label{tab:residualized_bcs}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Embedding} & \\textbf{Control} & \\textbf{Raw $\\rho$} & \\textbf{Raw $p$} & \\textbf{Partial $r$} & \\textbf{Partial $p$} \\\\\n\\midrule\nMiniLM & --- & $+$0.208 & $0.011$ & --- & --- \\\\\nMiniLM & log freq & --- & --- & $+$0.133 & $0.11$ \\\\\nMiniLM & log freq $+$ degree & --- & --- & --- & $0.23$ \\\\\n\\midrule\nQwen3 & --- & $+$0.184 & $0.025$ & --- & --- \\\\\nQwen3 & degree centrality & --- & --- & $+$0.063 & $0.44$ \\\\\nQwen3 & log freq $+$ degree & --- & --- & --- & $0.44$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Interpretation.}\nThe two embeddings encode different aspects of the same underlying confound. MiniLM, a smaller sentence encoder, produces a tighter embedding cluster for MAVEN's FrameNet-derived types; here, type frequency is the primary confounder because frequent types accumulate higher mean similarity to the dense cluster. Qwen3, with a larger representation space, differentiates types enough that frequency is not the dominant factor, but degree centrality (the count of strong semantic neighbors) becomes the confound instead. In both cases, the positive raw correlation reflects a centrality artifact: types that are semantically central are both high-BCS and easy to extract.\n\nUnder joint control, both embeddings yield $p > 0.2$; the raw positive BCS--F1 correlation on MAVEN is thus fully attributable to centrality-related confounders. This does not invalidate the confusability hypothesis; the pairwise SCS--confusion correlation on MAVEN remains significant (MiniLM $r = 0.129$, $p < 0.001$; Table~\\ref{tab:pairwise}). Rather, it demonstrates that per-type aggregation (mean BCS) conflates confusability with centrality in semantically homogeneous schemas, and that pairwise analysis or explicit confound adjustment is required in such settings.\n\n\\subsection{Partial Correlation: Controlling for Degree Centrality}\n\\label{sec:appendix_partial_corr}\n\nTo rule out degree centrality as a confound in cross-domain datasets, we compute partial correlations between BCS and accuracy controlling for batch mean degree centrality (mean off-diagonal SCS per type, averaged across batch members).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy partial correlation controlling for degree centrality. FewRel shows minimal attenuation (VIF${}\\,=\\,1.18$, low collinearity). DocRED shows high BCS--centrality collinearity (VIF${}\\,=\\,50.9$, $r = 0.99$), but the partial correlation remains highly significant.}\n\\label{tab:partial_corr}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{$n$} & \\textbf{$r_{\\text{zero}}$} & \\textbf{$r_{\\text{partial}}$} & \\textbf{$p_{\\text{partial}}$} & \\textbf{VIF} \\\\\n\\midrule\nFewRel & 204 & $-$0.570 & $-$0.537 & ${<}\\,0.001$ & 1.18 \\\\\nDocRED & 110 & $-$0.760 & $-$0.348 & ${<}\\,0.001$ & 50.9 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nAs Table~\\ref{tab:partial_corr} shows, on FewRel, BCS and degree centrality are only moderately correlated ($r = 0.39$), and the BCS effect survives nearly intact after partialling ($r_{\\text{partial}} = -0.537$ vs.\\ $r_{\\text{zero}} = -0.570$; semipartial $R^2 = 0.273$). On DocRED, the near-perfect BCS--centrality correlation ($r = 0.99$) makes it impossible to fully separate the two predictors; the significant partial correlation ($p < 0.001$) indicates BCS retains predictive value but does not uniquely identify the causal channel. This contrasts with MAVEN (\\S\\ref{sec:appendix_residualized_bcs}), where the BCS signal vanishes after controlling for centrality.\n\n\\paragraph{Ridge regression under multicollinearity.}\nRidge regression (GCV, $\\lambda = 0.001$) on the 110 DocRED batches confirms the negative direction of the BCS--accuracy relationship even after regularizing for the severe BCS--centrality multicollinearity (VIF$\\,\\approx\\,$50.9). The standardized BCS coefficient is $\\hat{\\beta}_{\\textsc{bcs}} = -1.53$ ($\\hat{\\beta}_{\\text{centrality}} = 0.78$, $R^2 = 0.594$). An analytic derivation shows that $\\hat{\\beta}_{\\textsc{bcs}} < 0$ for \\emph{all} $\\lambda \\geq 0$: the numerator of the closed-form ridge solution, $-(1{+}\\lambda) \\times 0.760 + 0.727$, is negative at $\\lambda{=}0$ and monotonically decreasing thereafter. Given the shrinkage bias inherent to ridge estimation, we interpret only the sign---not the magnitude---of the BCS coefficient as directional evidence that higher schema confusability degrades extraction accuracy, independent of degree centrality.\n\n\\subsection{NER BCS-Null Power Analysis}\n\\label{sec:appendix_ner_power}\n\nThe Few-NERD BCS-null may reflect insufficient BCS variance rather than a genuine absence of the BCS--accuracy relationship. Few-NERD's BCS standard deviation (0.027) is only 19\\% of FewRel's (0.141); FewRel's observed $r = -0.570$ would attenuate to $r = -0.111$ under this restricted range, yielding 65\\% power at $n = 450$ (below the conventional 80\\% threshold). The minimum detectable $|r|$ at 80\\% power is 0.132. This analysis characterizes the NER result as absence of evidence (insufficient power at the attenuated effect size) rather than evidence of absence.\n\n\\subsection{Bootstrap CI Robustness}\n\\label{sec:appendix_bootstrap_ci}\n\nBecause batches in the FewRel experiments are constructed by sampling relation types from a shared pool, different batches may share text instances of the same type, potentially inducing residual dependence that makes standard bootstrap CIs anti-conservative. We assess this concern via cluster-robust inference. We cluster the $n = 164$ FewRel batches by instance-weighted type overlap (hierarchical clustering, complete linkage) and compute cluster-robust standard errors. Across six overlap thresholds (Jaccard distance $\\in \\{0.1, \\ldots, 0.9\\}$, yielding 80--83 clusters), the cluster-robust SE for the BCS regression slope is $0.96$--$0.97\\times$ the OLS SE, and the slope remains highly significant ($p < 10^{-11}$). Cluster bootstrap CIs for $R^2$ show width changes of $-6\\%$ to $+6\\%$ relative to standard bootstrap CIs ($[0.14, 0.42]$ vs.\\ $[0.15, 0.41]$). We conclude that the reported CIs are robust to the non-independence induced by shared text instances.\n\n\\subsection{Domain Distribution in Extreme-BCS Batches}\n\\label{sec:appendix_domain_distribution}\n\nWe classify the 80 FewRel relation types into six semantic domains (geography, creative work, person, organization, event/temporal, science/taxonomy) and compare domain composition between the 25 highest-BCS and 25 lowest-BCS batches from our 8-type schema pool. The distributions differ significantly ($\\chi^2 = 230.74$, $p < 0.001$, $df = 5$): low-BCS batches draw heavily from geography (45.5\\%) and creative work (25.5\\%), while high-BCS batches concentrate on science/taxonomy (49.5\\%) and event/temporal (26.0\\%) domains. Normalized Shannon entropy is higher for low-BCS batches ($H' = 0.79$) than high-BCS ($H' = 0.67$), confirming that low-BCS schemas span more diverse domains. Crucially, this domain concentration is an \\emph{expected} property of embedding-based confusability: relation types within the same domain naturally share semantic features, producing higher pairwise cosine similarity and thus higher BCS. Domain composition therefore acts as a mediator---it is \\emph{part of} the mechanism through which BCS captures schema difficulty---rather than an independent confounding variable. The BCS metric intentionally aggregates such semantic overlap into a single predictive score.\n\n\\section{Batch Composition Results}\n\\label{sec:appendix_batch_composition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Batch composition on FewRel 80-relation RE with oracle routing. $^\\dagger$Mean $\\pm$ SD across 15 random seeds.}\n\\label{tab:batch_composition}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\n\\textbf{Condition} & \\textbf{Accuracy} & \\textbf{Mean BCS} \\\\\n\\midrule\nSingle-pass (80 types) & 0.504 & 0.557 \\\\\nRandom batching (15 seeds)$^\\dagger$ & 0.788\\,$\\pm$\\,0.018 & 0.559 \\\\\nConfus.-aware (graph coloring) & \\textbf{0.802} & 0.552 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nSee the accompanying discussion in \\S\\ref{sec:sdgd}.\n\n\\input{prompt_appendix}\n\n\\section{Prompt Version Sensitivity Analysis}\n\\label{sec:appendix_prompt_sensitivity}\n\nWe assess whether the confusability effects reported in \\S\\ref{sec:bcs_controlled}--\\ref{sec:multi_channel} are robust to prompt design by replicating key experiments under the v2 prompt (\\S\\ref{sec:model}; full templates in Appendix~\\ref{sec:appendix_prompts}).\n\n\\paragraph{RE (FewRel).}\nUnder the v1 prompt, the extreme-batch BCS gap (Table~\\ref{tab:bcs_controlled}) is substantial. Under v2, with $n{=}25$ batches per group and wider BCS contrast (low-BCS range [0.356, 0.367]; high-BCS range [0.791, 0.811]), the gap is $-$25.5\\,pp (low-BCS 85.2\\% vs.\\ high-BCS 59.7\\%; 95\\% CI [22.4, 28.6]; $p < 0.001$; Pearson $r = -0.919$). The effect is significant, directionally consistent with v1, and only modestly attenuated in magnitude ($-$5.7\\,pp reduction). An earlier $n{=}5$ evaluation with narrower BCS contrast (0.21) yielded a smaller gap of $-$7.9\\,pp (95\\% CI [$-$5.2, $+$21.5]), illustrating how limited statistical power and restricted BCS range can obscure the underlying signal, a cautionary note for small-sample prompt sensitivity studies.\n\n\\paragraph{NER (Few-NERD).}\nThe batch-level BCS--F1 correlation is null under both prompt versions. Pooling across three seeds and all count levels ($n = 450$), the correlation is $r = 0.004$ ($p = 0.94$). An earlier small-sample analysis ($n = 27$, single seed) had reported positive correlations ($r = +0.50$/$+0.58$), but these were driven by an accidental BCS--type-frequency confound: those 27 batches exhibited $r(\\text{BCS}, \\text{freq}) = 0.53$, creating a spurious path through frequency to F1. After controlling for type frequency, the partial correlation is non-significant in both the small ($r = 0.28$, $p = 0.16$) and large ($r = -0.12$, $p = 0.29$) samples. The pairwise SCS--confusion analysis (\\S\\ref{sec:pairwise}), which is immune to this batch-level aggregation artifact, remains the primary evidence for the NER confusability dimension.\n\n\\paragraph{Interpretation.}\nThe $n{=}25$ v2 result confirms that the confusability effect is directionally consistent across prompt designs, with attenuated magnitude: the gap narrows ($-$5.7\\,pp) but remains highly significant ($p < 0.001$, $r = -0.919$). The earlier $n{=}5$ non-significance reflected insufficient power and narrow BCS contrast, not absence of the effect. V2's stricter format constraints raise the baseline accuracy (low-BCS 85.2\\% vs.\\ 82.3\\%), but type confusion under high confusability persists (59.7\\% vs.\\ 51.0\\%). Prompt design modulates the practical magnitude of the confusability effect but does not eliminate it, ruling out prompt-specific confounding as the primary source. The underlying confusability signal (pairwise SCS--confusion correlation and the directional BCS--accuracy relationship) persists across both prompt versions.\n\n\\subsection{Cross-Prompt-Variant BCS Correlation}\n\\label{sec:appendix_prompt_variants}\n\nTo verify that the BCS--accuracy relationship is not an artifact of a specific prompt template, we evaluate four structurally distinct prompt variants on FewRel 80-relation RE at two count levels (8 and 32), with 10 random batches per condition (Table~\\ref{tab:prompt_variants}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy Pearson correlation across four prompt variants. At count 32, all four variants show negative BCS--accuracy correlations ($r \\leq -0.47$), with two reaching $p < 0.05$. At count 8, the narrower BCS range reduces statistical power.}\n\\label{tab:prompt_variants}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrr}\n\\toprule\n\\textbf{Variant} & \\textbf{Count} & \\textbf{Mean Acc} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule",
      "numLines": 200,
      "startLine": 200,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Assistant

_source line 41_

<details><summary>Logged reasoning block</summary>

```text
Let me continue reading the main.tex file to get the rest of the appendix content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "3617c71e-364f-4a0d-bdaa-8fa1a5b0a1a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167i4xRajGVz2Yb82kfarm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7492,
      "cache_read_input_tokens": 49814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7492
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

_source line 42_

I have enough context now. Let me read the remaining parts of main.tex to check for any more content areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "ab6fd867-bcad-4f6d-bc1e-e4481623f1a2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167i4xRajGVz2Yb82kfarm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7492,
      "cache_read_input_tokens": 49814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7492
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

_source line 43_

<details open><summary>🔧 Tool call — Read · `toolu_01JXjRhLrVCQiQ3pHwHMRLbq`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 400,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "096f39c9-e5a7-48b9-bb03-34f794dc6c83",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0167i4xRajGVz2Yb82kfarm1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7492,
      "cache_read_input_tokens": 49814,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7492
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

_source line 44 · 2026-05-22T06:38:44.691Z_

<details><summary>↩ Tool result · `toolu_01JXjRhLrVCQiQ3pHwHMRLbq`</summary>

```text
400	V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\
401	V2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\
402	Instruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\
403	Instruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\
404	Chain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\
405	Chain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\
406	Minimal & 8 & 0.852 & $-$0.170 & 0.638 \\
407	Minimal & 32 & 0.615 & $-$0.771 & 0.009 \\
408	\bottomrule
409	\end{tabular}}
410	\end{table}
411	
412	At count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.
413	
414	\section{BCS Aggregation Sensitivity}
415	\label{sec:appendix_bcs_sensitivity}
416	
417	We define Batch Confusability Score (BCS) as the \emph{mean} pairwise SCS across all type pairs in a batch (\S\ref{sec:bcs_controlled}). An alternative definition takes the \emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\ref{tab:bcs_aggregation}).
418	
419	\begin{table}[h]
420	\centering
421	\small
422	\caption{BCS--accuracy regression under mean vs.\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \approx 0.60$; MAX $p \approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}
423	\label{tab:bcs_aggregation}
424	\resizebox{\columnwidth}{!}{%
425	\begin{tabular}{llcccc}
426	\toprule
427	\textbf{Aggregation} & \textbf{Condition} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} \\
428	\midrule
429	MEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ \\
430	MEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
431	\midrule
432	MAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\,0.001$ \\
433	MAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\
434	\bottomrule
435	\end{tabular}}
436	\end{table}
437	
438	MAX aggregation yields stronger correlations ($r = -0.637$ vs.\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.
439	
440	\section{BCS-Controlled Detailed Results}
441	\label{app:bcs-controlled-table}
442	
443	\begin{table}[h]
444	\centering
445	\small
446	\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\ref{tab:within_pool}; see \S\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}
447	\label{tab:bcs_controlled}
448	\resizebox{\columnwidth}{!}{%
449	\begin{tabular}{lcrrrr}
450	\toprule
451	\textbf{Schema} & \textbf{Count} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
452	\midrule
453	16-rel & 8 & 88.9\% & 79.8\% & $-$9.1 & --- \\
454	80-rel & 8 & 82.3\% & 51.0\% & $-$31.2 & {[}17.7, 42.7{]} \\
455	80-rel & 16 & 82.8\% & 51.6\% & $-$31.2 & {[}22.9, 39.6{]} \\
456	\bottomrule
457	\end{tabular}}
458	\end{table}
459	
460	\paragraph{Adjusted $R^2$ and confidence intervals.}
461	DocRED regressions (\S\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\% CI [0.47, 0.75]). The small shrinkage ($\Delta R^2 \leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.
462	
463	\section{Format Independence: Paired Constrained vs.\ Unconstrained Comparison}
464	\label{app:format-independence}
465	
466	To test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\ref{tab:format_independence}).
467	
468	\begin{table}[h]
469	\centering
470	\small
471	\caption{Paired comparison of constrained vs.\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\Delta = -0.08$\,pp), ruling out a format-driven accuracy shift.}
472	\label{tab:format_independence}
473	\begin{tabular}{lrr}
474	\toprule
475	\textbf{Metric} & \textbf{Constrained} & \textbf{Unconstrained} \\
476	\midrule
477	Mean accuracy & 79.5\% & 79.6\% \\
478	Pearson $r$ (BCS vs.\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\
479	Spearman $\rho$ (BCS vs.\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\
480	\midrule
481	\multicolumn{3}{l}{\textit{Paired Fisher $z$-test for correlation equality}} \\
482	\quad Pearson $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
483	\quad Spearman $z$ & \multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\
484	\bottomrule
485	\end{tabular}
486	\end{table}
487	
488	The near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\sim}2$\,pp; \S\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.
489	
490	\paragraph{Per-batch paired results.}
491	Table~\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \emph{identical} accuracy; the two exceptions (high\_5, high\_11) differ by a single sample (1/96 $\approx$ 1.04\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\%), confirming that the model generates valid type labels even without format constraints.
492	
493	\begin{table}[h]
494	\centering
495	\small
496	\caption{Per-batch accuracy (\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\Delta = -1.04$\,pp). L = low-BCS, H = high-BCS.}
497	\label{tab:format_perbatch}
498	\resizebox{\columnwidth}{!}{%
499	\begin{tabular}{lcrrrr}
500	\toprule
501	\textbf{Batch} & \textbf{Group} & \textbf{BCS} & \textbf{Constr.} & \textbf{Unconstr.} & \textbf{$\Delta$} \\
502	\midrule
503	low\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\
504	low\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\
505	low\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\
506	low\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\
507	low\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\
508	low\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\
509	low\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\
510	low\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\
511	low\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\
512	low\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\
513	low\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\
514	low\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\
515	low\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\
516	\midrule
517	high\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\
518	high\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\
519	high\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\
520	high\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
521	high\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\
522	high\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\
523	high\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\
524	high\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\
525	high\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\
526	high\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\
527	high\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\
528	high\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\
529	\bottomrule
530	\end{tabular}}
531	\end{table}
532	
533	\section{Within-Pool Analysis Methodology}
534	\label{app:within-pool-method}
535	
536	A potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.
537	
538	\begin{table}[h]
539	\centering
540	\small
541	\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\ref{sec:appendix_within_pool} for CI interpretation.}
542	\label{tab:within_pool}
543	\resizebox{\columnwidth}{!}{%
544	\begin{tabular}{lrrrrrrr}
545	\toprule
546	& \multicolumn{4}{c}{\textbf{Regression (BCS $\to$ Accuracy)}} & \multicolumn{2}{c}{\textbf{Quartile $\Delta$}} \\
547	\cmidrule(lr){2-5} \cmidrule(lr){6-7}
548	\textbf{Setting} & \textbf{Slope} & \textbf{95\% CI} & \textbf{$r$} & \textbf{$p$} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
549	\midrule
550	Independent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\
551	80-pool $\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\
552	Full 80-rel ($n{=}25$)$^\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\
553	\midrule
554	\multicolumn{7}{l}{\footnotesize Permutation test (16-rel vs.\ 80-pool slopes): $p \approx 0.60$ (5{,}000 permutations)} \\
555	\multicolumn{7}{l}{\footnotesize $^\dagger$BCS range (IQR\,=\,0.033) insufficient for regression; slope not interpretable.} \\
556	\bottomrule
557	\end{tabular}}
558	\end{table}
559	
560	The within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \approx 0.60$). The smaller quartile gap ($-$3.92\,pp vs.\ $-$5.31\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\ref{sec:appendix_within_pool}).
561	
562	In the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.
563	
564	\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}
565	\label{app:scs-ablation}
566	
567	Table~\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.
568	
569	\begin{table}[h]
570	\centering
571	\small
572	\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\Delta r$ indicates that definitions provide no systematic benefit.}
573	\label{tab:scs-ablation}
574	\resizebox{\columnwidth}{!}{\begin{tabular}{lcccc}
575	\toprule
576	Dataset & SCS$_\text{name}$ $r$ & SCS$_\text{def}$ $r$ & $\Delta r$ & Matrix corr. \\
577	\midrule
578	Few-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\
579	MAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\
580	FewRel & 0.178 & 0.193 & +0.015 & 0.848 \\
581	\bottomrule
582	\end{tabular}}
583	\end{table}
584	
585	Few-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.
586	
587	\paragraph{Held-out validation.}
588	\label{app:scs-heldout-validation}
589	From the 80-type confusion matrix, we extract the $\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.
590	
591	\section{Pair-to-Batch Aggregation Simulation}
592	\label{app:aggregation-sim}
593	
594	The following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\S\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.
595	
596	\paragraph{Setup.} We examine whether the pair-level $R^2 \approx 7\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \approx 22\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\rho_\text{SCS} = 0.35$). For batches of $k=8$ types ($\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.
597	
598	\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\sim$3$\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\approx 3.4$, not 28).
599	
600	\paragraph{Unconditional baseline.}
601	When the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\text{SNR} \times \text{EF} / (\text{SNR} \times \text{EF} + 1) = 0.042$ with the same effective factor $\text{EF} = 3.35$. This ${\sim}5\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \emph{active} confusable pairs, not uniform contributions from all pairs.
602	
603	\paragraph{Sensitivity to $\rho$.}
604	The inter-pair SCS correlation $\rho = 0.35$ is estimated from pairs sharing a common type. At $\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \approx 0.22$, still matching the observed value; at $\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.
605	
606	\paragraph{Non-independence and ecological inference.}
607	Types within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\text{--}0.578$ (\S\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.
608	
609	\section{BCS Independence from Type Composition}
610	\label{app:bcs-composition}
611	
612	FewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\% of explained variance), composition unique $R^2 = 0.298$ (42.3\%), and shared $R^2 = 0.147$ (20.9\%). The near-orthogonality of predictors (VIF${}\,=\,1.06$, $r(\text{BCS}, \text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.
613	
614	\section{SCS vs.\ Simple Baselines}
615	\label{app:scs-baselines}
616	
617	Table~\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.
618	
619	\begin{table}[h]
620	\centering
621	\small
622	\caption{Pairwise confusion prediction: SCS vs.\ simple baselines. Spearman $\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\dagger$42\% of pairs lack WordNet coverage.}
623	\label{tab:scs_baselines}
624	\resizebox{\columnwidth}{!}{%
625	\begin{tabular}{llrr}
626	\toprule
627	\textbf{Dataset} & \textbf{Metric} & \textbf{Spearman $\rho$} & \textbf{$p$} \\
628	\midrule
629	FewRel & SCS (embedding) & \textbf{0.218} & $< 0.001$ \\
630	(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\
631	& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\
632	& Levenshtein & 0.016 & 0.363 (n.s.) \\
633	\midrule
634	Few-NERD & SCS (embedding) & \textbf{0.166} & $< 0.001$ \\
635	(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\
636	& Same-parent (prefix) & 0.146 & $< 0.001$ \\
637	& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\dagger$ \\
638	\bottomrule
639	\end{tabular}}
640	\end{table}
641	
642	\section{Split-Origin Covariate Analysis}
643	\label{app:split-origin}
644	
645	FewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.
646	
647	\paragraph{Method.}  Across 213 multi-type batches ($k \geq 2$) from the batch-composition experiment (\S\ref{sec:sdgd}) and the factorial design (\S\ref{sec:bcs_controlled}), we compute $\texttt{train\_origin\_ratio} = n_{\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:
648	{\small\begin{equation*}
649	\text{acc} = \beta_0 + \beta_{\text{BCS}} \!\cdot\! \text{BCS} + \beta_{\text{orig}} \!\cdot\! \text{train\_origin\_ratio} + \varepsilon
650	\end{equation*}}
651	
652	\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\beta_{\text{BCS}} = -0.416$, $p < 0.001$ (vs.\ $\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\beta_{\text{origin}} = -0.057$, $p = 0.245$), and $\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.
653	
654	Pairwise SCS distributions do not differ significantly between train-origin (64 types, mean\,=\,0.880) and val-origin (16 types, mean\,=\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.
655	
656	\section{Cross-Seed Variance Decomposition}
657	\label{app:variance-decomposition}
658	
659	\begin{table}[h]
660	\centering
661	\small
662	\caption{Variance decomposition on FewRel (3 seeds $\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}
663	\label{tab:variance_decomposition}
664	\begin{tabular}{rrrr}
665	\toprule
666	\textbf{Count} & \textbf{Batch SD} & \textbf{Seed SD} & \textbf{Ratio} \\
667	\midrule
668	4 & 0.0889 & 0.0122 & 53.5 \\
669	8 & 0.0820 & 0.0098 & 70.0 \\
670	16 & 0.0626 & 0.0270 & 5.4 \\
671	32 & 0.0462 & 0.0091 & 26.0 \\
672	40 & 0.0421 & 0.0019 & 474.4 \\
673	64 & 0.0245 & 0.0022 & 119.8 \\
674	80 & 0.0001 & 0.0088 & $<$0.1 \\
675	\bottomrule
676	\end{tabular}
677	\end{table}
678	
679	Table~\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\times$ across count levels 4--64 (mean 125$\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\,=\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\,pp, likely attributable to FP8 quantization non-determinism).
680	
681	\section{Cross-Domain Connections}
682	\label{app:cross-domain}
683	
684	The schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.
685	
686	\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}
687	\label{sec:appendix_cross_model_70b}
688	
689	To test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\S\ref{sec:count_curves}, \S\ref{sec:bcs_controlled}).
690	
691	\begin{table}[h]
692	\centering
693	\small
694	\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\to$80): $-$30.7\,pp (70B) vs.\ $-$30.1\,pp (32B). NER decline (count 2$\to$22): $-$7.1\,pp (70B) vs.\ $-$23.6\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}
695	\label{tab:cross_model_70b}
696	\begin{tabular}{lrr}
697	\toprule
698	\textbf{Count} & \textbf{LLaMA-70B} & \textbf{Qwen3-32B} \\
699	\midrule
700	\multicolumn{3}{l}{\textit{RE (FewRel, Classification Accuracy)}} \\
701	8  & 0.757 & 0.805 \\
702	16 & 0.685 & 0.719 \\
703	32 & 0.601 & 0.652 \\
704	64 & 0.504 & 0.539 \\
705	80 & 0.450 & 0.504 \\
706	\midrule
707	\multicolumn{3}{l}{\textit{NER (Few-NERD, Text+Type Match Recall)}} \\
708	2  & 0.323 & 0.515 \\
709	6  & 0.300 & 0.399 \\
710	12 & 0.278 & 0.318 \\
711	22 & 0.252 & 0.279 \\
712	44 & 0.297 & 0.309 \\
713	66 & 0.273 & 0.407 \\
714	\bottomrule
715	\end{tabular}
716	\end{table}
717	
718	Table~\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\,pp (70B) versus $-$30.1\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.
719	
720	On NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\to$0.252, $-$7.1\,pp; Qwen3: 0.515$\to$0.279, $-$23.6\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).
721	
722	For the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\Delta = +10.9$\,pp, 95\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.
723	
724	In summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.
725	
726	\section{Cross-Model Validation with Gemini 2.5 Flash (API)}
727	\label{sec:appendix_cross_model_gemini}
728	
729	We validate both dimensions on a proprietary model, Gemini 2.5 Flash \citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.
730	
731	\begin{table}[h]
732	\centering
733	\small
734	\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\rho = -1.0$ for both on counts 4--32). $^\dagger$Count 64: Gemini based on 11/25 batches (partial).}
735	\label{tab:cross_model_gemini}
736	\begin{tabular}{lrr}
737	\toprule
738	\textbf{Count} & \textbf{Gemini Flash} & \textbf{Qwen3-32B} \\
739	\midrule
740	1  & 0.827 & --- \\
741	4  & 0.873 & 0.870 \\
742	8  & 0.820 & 0.805 \\
743	16 & 0.787 & 0.719 \\
744	32 & 0.739 & 0.652 \\
745	64$^\dagger$ & 0.637 & 0.539 \\
746	\bottomrule
747	\end{tabular}
748	\end{table}
749	
750	Table~\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\rho = -1.0$). Including count 1, the Gemini count curve yields $\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\,pp from count 4 to 32) than for Qwen3 ($-$21.8\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\,pp at count 4 vs.\ 8.7\,pp at count 32, 9.8\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.
751	
752	\paragraph{Dimension~2: BCS-controlled confusability.}
753	We replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).
754	
755	At count 8, low-BCS batches achieve 90.5\% vs.\ high-BCS 72.9\% ($\Delta = -17.6$\,pp, 95\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\% vs.\ 82.3\%) leaves less room for degradation.
756	
757	Table~\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.
758	
759	\begin{table}[h]
760	\centering
761	\small
762	\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}
763	\label{tab:cross_model_bcs_summary}
764	\begin{tabular}{llrrrr}
765	\toprule
766	\textbf{Model} & \textbf{Count} & \textbf{Low BCS} & \textbf{High BCS} & \textbf{$\Delta$} & \textbf{95\% CI} \\
767	\midrule
768	Qwen3-32B     & 8  & 82.3\% & 51.0\% & $-$31.2\,pp & --- \\
769	Qwen3-32B     & 16 & 82.8\% & 51.6\% & $-$31.2\,pp & --- \\
770	Llama-8B      & 8  & 78.1\% & 51.0\% & $-$27.1\,pp & --- \\
771	Llama-70B FP8 & 16 & ---    & ---    & $-$10.9\,pp & {[}3.0, 20.1{]} \\
772	Gemini Flash  & 8  & 90.5\% & 72.9\% & $-$17.6\,pp & {[}15.1, 20.1{]} \\
773	\bottomrule
774	\end{tabular}
775	\end{table}
776	
777	\section{Few-Shot Prompting and Confusability}
778	\label{sec:appendix_fewshot_bcs}
779	
780	To test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \S\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\approx 0.36$; 25 high-BCS, mean $\approx 0.80$), drawn from the pre-constructed batch pool of \S\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\ref{tab:fewshot_bcs}).
781	
782	\begin{table}[h]
783	\centering
784	\small
785	\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot). The confusability gap widens from +18.5\,pp (0-shot) to +22.8\,pp (5-shot). All metrics are micro-averaged across batches.}
786	\label{tab:fewshot_bcs}
787	\resizebox{\columnwidth}{!}{\begin{tabular}{lrrrl}
788	\toprule
789	\textbf{Condition} & \textbf{Low-BCS} & \textbf{High-BCS} & \textbf{$\Delta$ (pp)} & \textbf{95\% CI} \\
790	\midrule
791	0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\
792	1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\
793	5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\
794	\bottomrule
795	\end{tabular}}
796	\end{table}
797	
798	Demonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\,pp at 1-shot, $-$1.0\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \citep{lost-in-middle-2024}.
799	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d170167a-c8cb-4414-8980-29a456e9eee9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "V2 (definition-first) & 8 & 0.769 & $-$0.333 & 0.348 \\\\\nV2 (definition-first) & 32 & 0.564 & $-$0.648 & 0.043 \\\\\nInstruction-rewrite & 8 & 0.847 & $-$0.223 & 0.536 \\\\\nInstruction-rewrite & 32 & 0.662 & $-$0.469 & 0.171 \\\\\nChain-of-thought & 8 & 0.749 & $+$0.254 & 0.478 \\\\\nChain-of-thought & 32 & 0.617 & $-$0.566 & 0.088 \\\\\nMinimal & 8 & 0.852 & $-$0.170 & 0.638 \\\\\nMinimal & 32 & 0.615 & $-$0.771 & 0.009 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAt count 32, all four variants produce negative BCS--accuracy correlations ($r$ ranges from $-$0.47 to $-$0.77), with V2 ($p = 0.043$) and Minimal ($p = 0.009$) reaching significance and Chain-of-thought approaching it ($p = 0.088$). At count 8, correlations are weaker and nonsignificant across all variants, consistent with the narrower BCS range at lower schema complexity reducing the detectable effect size. Rather than applying Bonferroni correction, which assumes independent hypotheses inappropriate for correlated prompt variants testing the same underlying signal, we note directional consistency: 7 of 8 conditions show negative BCS--accuracy slopes, consistent with the primary finding \\citep{rothman-1990}. These results confirm that the confusability effect arises from schema composition, not prompt-specific phrasing.\n\n\\section{BCS Aggregation Sensitivity}\n\\label{sec:appendix_bcs_sensitivity}\n\nWe define Batch Confusability Score (BCS) as the \\emph{mean} pairwise SCS across all type pairs in a batch (\\S\\ref{sec:bcs_controlled}). An alternative definition takes the \\emph{maximum} pairwise SCS within each batch to capture the single most confusable pair. Here we compare both aggregation methods to verify that core conclusions are robust to this choice (Table~\\ref{tab:bcs_aggregation}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS--accuracy regression under mean vs.\\ max pairwise SCS aggregation (FewRel, 16-relation batches). Permutation test for slope equivalence across pools: MEAN $p \\approx 0.60$; MAX $p \\approx 0.44$. The 80-pool row is identical under both definitions because these batches were collected using mean-aggregated BCS; the MAX column reflects the same data for completeness.}\n\\label{tab:bcs_aggregation}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llcccc}\n\\toprule\n\\textbf{Aggregation} & \\textbf{Condition} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} \\\\\n\\midrule\nMEAN (primary) & 16-rel & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ \\\\\nMEAN & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\midrule\nMAX & 16-rel & $-$0.449 & [$-$0.552, $-$0.346] & $-$0.637 & ${<}\\,0.001$ \\\\\nMAX & 80-pool 16-sub & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & 0.027 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nMAX aggregation yields stronger correlations ($r = -0.637$ vs.\\ $-0.467$ for 16-rel), consistent with the hypothesis that the single most confusable pair in a batch predicts substitution errors. Both definitions produce significant negative slopes across all conditions, and the permutation tests confirm no significant difference between independent and sampled pools under either definition. We adopt MEAN as the primary definition because it better represents average pairwise difficulty across all schema combinations, while MAX may overweight a single outlier pair. The choice does not affect any paper conclusion.\n\n\\section{BCS-Controlled Detailed Results}\n\\label{app:bcs-controlled-table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS-controlled FewRel accuracy. Low-BCS batches contain maximally dissimilar types; high-BCS batches contain maximally similar types. The 80-relation extreme-batch gap reflects the wider BCS range; regression slopes are consistent across pools ($p = 0.60$; Table~\\ref{tab:within_pool}; see \\S\\ref{sec:practical_magnitude} for typical-batch magnitudes). The 16-relation condition used a single extreme batch per BCS level; bootstrap CIs require multiple batches.}\n\\label{tab:bcs_controlled}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Schema} & \\textbf{Count} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n16-rel & 8 & 88.9\\% & 79.8\\% & $-$9.1 & --- \\\\\n80-rel & 8 & 82.3\\% & 51.0\\% & $-$31.2 & {[}17.7, 42.7{]} \\\\\n80-rel & 16 & 82.8\\% & 51.6\\% & $-$31.2 & {[}22.9, 39.6{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Adjusted $R^2$ and confidence intervals.}\nDocRED regressions (\\S\\ref{sec:bcs_controlled}) use OLS on $n = 55$ batches (15 high-BCS + 15 low-BCS + 25 random) per count level, with one predictor. At count 16, adjusted $R^2 = 0.646$ (unadjusted: 0.653; 95\\% CI [0.53, 0.77]); at count 32, adjusted $R^2 = 0.606$ (unadjusted: 0.614; 95\\% CI [0.47, 0.75]). The small shrinkage ($\\Delta R^2 \\leq 0.01$) indicates the unadjusted values are not inflated by the predictor-to-sample ratio.\n\n\\section{Format Independence: Paired Constrained vs.\\ Unconstrained Comparison}\n\\label{app:format-independence}\n\nTo test whether the BCS--accuracy relationship depends on the output format, we run both constrained (enum-based) and unconstrained (free-text) decoding on the same 25 batch type sets from the FewRel 80-relation pool (13 low-BCS, 12 high-BCS; count 8). Each batch uses identical instances and type sets; only the decoding format differs (Table~\\ref{tab:format_independence}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Paired comparison of constrained vs.\\ unconstrained decoding on 25 identical FewRel batch type sets. Both formats yield virtually identical BCS--accuracy correlations (Fisher $z \\approx 0$), confirming the confusability effect is format-independent. Mean accuracy is also unchanged ($\\Delta = -0.08$\\,pp), ruling out a format-driven accuracy shift.}\n\\label{tab:format_independence}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Metric} & \\textbf{Constrained} & \\textbf{Unconstrained} \\\\\n\\midrule\nMean accuracy & 79.5\\% & 79.6\\% \\\\\nPearson $r$ (BCS vs.\\ acc) & $-$0.448 ($p = 0.025$) & $-$0.439 ($p = 0.028$) \\\\\nSpearman $\\rho$ (BCS vs.\\ acc) & $-$0.157 ($p = 0.455$) & $-$0.144 ($p = 0.492$) \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{Paired Fisher $z$-test for correlation equality}} \\\\\n\\quad Pearson $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\quad Spearman $z$ & \\multicolumn{2}{c}{$-$0.04 ($p = 0.97$)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe near-zero Fisher $z$ statistics ($|z| < 0.05$, $p > 0.96$) confirm that the BCS--accuracy correlation is indistinguishable between formats. Both Pearson $r$ values are significant ($p < 0.03$), reflecting the bimodal BCS distribution of extreme batches (13 low + 12 high); the monotonic Spearman $\\rho$ is modest and non-significant under both formats, consistent with the typical-batch BCS effect size (${\\sim}2$\\,pp; \\S\\ref{sec:practical_magnitude}). This result establishes that the confusability-associated degradation pattern is robust across output formats, not an artifact of forced-choice decoding.\n\n\\paragraph{Per-batch paired results.}\nTable~\\ref{tab:format_perbatch} reports per-batch accuracy under both formats. Of 25 batches, 23 yield \\emph{identical} accuracy; the two exceptions (high\\_5, high\\_11) differ by a single sample (1/96 $\\approx$ 1.04\\,pp). Only 2 out-of-vocabulary predictions occur in unconstrained decoding (OOV rate 0.08\\%), confirming that the model generates valid type labels even without format constraints.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-batch accuracy (\\%) under constrained and unconstrained decoding on 25 identical FewRel batch type sets (count 8, 96 instances each). 23/25 batches yield identical accuracy; the two exceptions differ by exactly one sample ($\\Delta = -1.04$\\,pp). L = low-BCS, H = high-BCS.}\n\\label{tab:format_perbatch}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lcrrrr}\n\\toprule\n\\textbf{Batch} & \\textbf{Group} & \\textbf{BCS} & \\textbf{Constr.} & \\textbf{Unconstr.} & \\textbf{$\\Delta$} \\\\\n\\midrule\nlow\\_0  & L & 0.472 & 83.3 & 83.3 & 0.0 \\\\\nlow\\_1  & L & 0.647 & 81.3 & 81.3 & 0.0 \\\\\nlow\\_2  & L & 0.665 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_3  & L & 0.672 & 82.3 & 82.3 & 0.0 \\\\\nlow\\_4  & L & 0.674 & 67.7 & 67.7 & 0.0 \\\\\nlow\\_5  & L & 0.678 & 72.9 & 72.9 & 0.0 \\\\\nlow\\_6  & L & 0.679 & 80.2 & 80.2 & 0.0 \\\\\nlow\\_7  & L & 0.687 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_8  & L & 0.692 & 77.1 & 77.1 & 0.0 \\\\\nlow\\_9  & L & 0.692 & 91.7 & 91.7 & 0.0 \\\\\nlow\\_10 & L & 0.692 & 87.5 & 87.5 & 0.0 \\\\\nlow\\_11 & L & 0.709 & 84.4 & 84.4 & 0.0 \\\\\nlow\\_12 & L & 0.709 & 68.8 & 68.8 & 0.0 \\\\\n\\midrule\nhigh\\_0  & H & 0.712 & 91.7 & 91.7 & 0.0 \\\\\nhigh\\_1  & H & 0.724 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_2  & H & 0.735 & 67.7 & 67.7 & 0.0 \\\\\nhigh\\_3  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_4  & H & 0.742 & 86.5 & 86.5 & 0.0 \\\\\nhigh\\_5  & H & 0.747 & 81.3 & 82.3 & $-$1.0 \\\\\nhigh\\_6  & H & 0.768 & 83.3 & 83.3 & 0.0 \\\\\nhigh\\_7  & H & 0.778 & 77.1 & 77.1 & 0.0 \\\\\nhigh\\_8  & H & 0.791 & 71.9 & 71.9 & 0.0 \\\\\nhigh\\_9  & H & 0.820 & 70.8 & 70.8 & 0.0 \\\\\nhigh\\_10 & H & 0.823 & 92.7 & 92.7 & 0.0 \\\\\nhigh\\_11 & H & 0.971 & 49.0 & 50.0 & $-$1.0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Within-Pool Analysis Methodology}\n\\label{app:within-pool-method}\n\nA potential confound in the cross-scale comparison is that the 16-relation and 80-relation pools contain different types, so the observed gap could reflect pool composition rather than confusability. To control for this, we draw 100 random 16-relation subsets from the 80-relation pool and evaluate under the same BCS-controlled protocol.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Three-way BCS--accuracy analysis on FewRel. Slope: OLS of batch accuracy on BCS (bootstrap CIs, $B{=}10{,}000$). $\\Delta$: accuracy gap between top- and bottom-quartile BCS batches. See Appendix~\\ref{sec:appendix_within_pool} for CI interpretation.}\n\\label{tab:within_pool}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{lrrrrrrr}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{Regression (BCS $\\to$ Accuracy)}} & \\multicolumn{2}{c}{\\textbf{Quartile $\\Delta$}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-7}\n\\textbf{Setting} & \\textbf{Slope} & \\textbf{95\\% CI} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\nIndependent 16-rel ($n{=}100$) & $-$0.509 & [$-$0.686, $-$0.336] & $-$0.467 & ${<}\\,0.001$ & $-$5.31 & [$-$7.44, $-$3.19] \\\\\n80-pool $\\to$ 16-sub ($n{=}100$) & $-$0.401 & [$-$0.701, $-$0.069] & $-$0.221 & $0.027$ & $-$3.92 & [$-$8.17, $+$0.38] \\\\\nFull 80-rel ($n{=}25$)$^\\dagger$ & $+$0.221 & [$-$1.303, $+$1.695] & $+$0.064 & $0.76$ & $-$1.04 & [$-$10.12, $+$8.04] \\\\\n\\midrule\n\\multicolumn{7}{l}{\\footnotesize Permutation test (16-rel vs.\\ 80-pool slopes): $p \\approx 0.60$ (5{,}000 permutations)} \\\\\n\\multicolumn{7}{l}{\\footnotesize $^\\dagger$BCS range (IQR\\,=\\,0.033) insufficient for regression; slope not interpretable.} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nThe within-pool slope ($-$0.401, CI excludes zero) is statistically indistinguishable from the independent 16-relation pool ($-$0.509; permutation $p \\approx 0.60$). The smaller quartile gap ($-$3.92\\,pp vs.\\ $-$5.31\\,pp) reflects the narrower BCS range within the 80-relation pool (Appendix~\\ref{sec:appendix_within_pool}).\n\nIn the full 80-relation condition, natural BCS variation is insufficient (IQR${}=0.033$) to yield a detectable effect ($n=25$, slope${}=+0.221$, $p \\approx 0.76$). This does not invalidate the confusability effect; the within-pool slope is significant ($p=0.027$) when BCS is deliberately varied, but establishes that natural schema sampling at this scale does not produce sufficient BCS contrast for detection.\n\n\\section{SCS Embedding Ablation: Name-Only vs. Name+Definition}\n\\label{app:scs-ablation}\n\nTable~\\ref{tab:scs-ablation} compares predictive accuracy of name-only SCS against name+definition SCS across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pearson correlation between SCS and empirical confusion rate. ``Def'' concatenates type name with definition before embedding. All correlations significant ($p < 0.001$). The inconsistent direction of $\\Delta r$ indicates that definitions provide no systematic benefit.}\n\\label{tab:scs-ablation}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lcccc}\n\\toprule\nDataset & SCS$_\\text{name}$ $r$ & SCS$_\\text{def}$ $r$ & $\\Delta r$ & Matrix corr. \\\\\n\\midrule\nFew-NERD & 0.172 & 0.149 & $-$0.023 & 0.894 \\\\\nMAVEN & 0.129 & 0.164 & +0.035 & 0.656 \\\\\nFewRel & 0.178 & 0.193 & +0.015 & 0.848 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nFew-NERD is the only dataset whose prompts include type definitions; for MAVEN and FewRel, prompts use type names alone, so name-only SCS directly matches model input. The high matrix correlation (0.66--0.89) confirms that type names capture the dominant semantic structure.\n\n\\paragraph{Held-out validation.}\n\\label{app:scs-heldout-validation}\nFrom the 80-type confusion matrix, we extract the $\\binom{16}{2} = 120$ pairs among the 16 validation-origin types (fully disjoint from the 64 training-pool types). The SCS--confusion Spearman correlation remains positive and significant ($\\rho = 0.216$, $p = 0.018$), nearly identical to the full 80-type pool ($\\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs), ruling out training-set contamination as the driver of the observed relationship.\n\n\\section{Pair-to-Batch Aggregation Simulation}\n\\label{app:aggregation-sim}\n\nThe following simulation provides an illustrative explanatory model for how pair-level effects aggregate to batch-level variance. It is not the evidence base for our claims; the observed batch-level $R^2 = 0.218$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical measurement independent of this simulation.\n\n\\paragraph{Setup.} We examine whether the pair-level $R^2 \\approx 7\\%$ (computed over non-zero confusion pairs) can aggregate to the observed batch-level $R^2 \\approx 22\\%$ via a Monte Carlo simulation. From the FewRel 16-relation experiment, we estimate the inter-pair SCS correlation for pairs sharing a common type ($\\rho_\\text{SCS} = 0.35$). For batches of $k=8$ types ($\\binom{8}{2}=28$ pairs), we simulate 10{,}000 iterations: (1) generate 28 correlated pair-level effects with individual $R^2 = 0.074$; (2) average to obtain batch-level signals; (3) compute batch-level $R^2$.\n\n\\paragraph{Results.} Simulated batch $R^2 = 0.219$ (95\\% CI [0.092, 0.361]), matching the observed value of 0.218. The effective amplification factor is $\\sim$3$\\times$, explained by signal correlation within batches preserving variance while independent noise averages out (effective degrees of freedom $\\approx 3.4$, not 28).\n\n\\paragraph{Unconditional baseline.}\nWhen the simulation uses the unconditional pairwise $r^2 = 0.013$ (computed over all type pairs including zero-confusion pairs; Table~\\ref{tab:pairwise}), the simulated batch-level $R^2$ drops to $0.044$ (95\\% CI [0.001, 0.151]), well below the observed $R^2 = 0.218$. The analytical formula confirms: $\\text{SNR} \\times \\text{EF} / (\\text{SNR} \\times \\text{EF} + 1) = 0.042$ with the same effective factor $\\text{EF} = 3.35$. This ${\\sim}5\\times$ gap reflects the dilution from zero-confusion pairs: approximately 89\\% of type pairs never exhibit mutual confusion, contributing only noise to the unconditional correlation. The conditional model ($R^2 = 0.074 \\to 0.219$) matches the observed value because it isolates the minority of semantically proximate pairs that actually compete during type resolution; BCS predicts batch accuracy through the density of \\emph{active} confusable pairs, not uniform contributions from all pairs.\n\n\\paragraph{Sensitivity to $\\rho$.}\nThe inter-pair SCS correlation $\\rho = 0.35$ is estimated from pairs sharing a common type. At $\\rho = 0.20$ (halved correlation), a parallel simulation yields batch $R^2 \\approx 0.22$, still matching the observed value; at $\\rho = 0.50$, the correlation structure approaches the positive-definiteness boundary; $\\rho = 0.35$ thus sits in a stable regime. The simulation is illustrative; the observed batch $R^2 = 0.218$ is the primary evidence.\n\n\\paragraph{Non-independence and ecological inference.}\nTypes within a batch share prompt context, so their extraction outcomes are not independent---a form of ecological correlation \\citep{robinson-1950-ecological}. This non-independence is built into the design: BCS measures batch-level confusability precisely because co-present types interact during type resolution. The core batch-level $R^2 = 0.218\\text{--}0.578$ (\\S\\ref{sec:practical_magnitude}) is a direct empirical observation from regressing batch accuracy on BCS, not derived from the simulation above. The inter-pair SCS correlation $\\rho = 0.35$ used in the simulation was estimated from the SCS correlation matrix independently of batch-level accuracy data.\n\n\\section{BCS Independence from Type Composition}\n\\label{app:bcs-composition}\n\nFewRel's balanced design (700 instances per type) makes type frequency invariant across batches, ruling out frequency-driven confounding. To test whether BCS captures information beyond type composition effects, we decompose the explained variance in a joint model (accuracy $\\sim$ BCS $+$ mean type difficulty), where type difficulty is the per-type solo-baseline accuracy averaged across batch members. On 100 random 8-type batches from the 16-relation pool, the joint model explains $R^2 = 0.704$. Variance decomposition yields: BCS unique $R^2 = 0.259$ (36.8\\% of explained variance), composition unique $R^2 = 0.298$ (42.3\\%), and shared $R^2 = 0.147$ (20.9\\%). The near-orthogonality of predictors (VIF${}\\,=\\,1.06$, $r(\\text{BCS}, \\text{difficulty}) = -0.21$) confirms that BCS captures confusability-specific signal rather than a proxy for type difficulty.\n\n\\section{SCS vs.\\ Simple Baselines}\n\\label{app:scs-baselines}\n\nTable~\\ref{tab:scs_baselines} compares SCS against simple baselines for pairwise confusion prediction.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Pairwise confusion prediction: SCS vs.\\ simple baselines. Spearman $\\rho$ between each metric and the empirical confusion rate. SCS outperforms all baselines on FewRel; the margin is smaller on Few-NERD, where hierarchical naming conventions provide partial signal to string-based metrics. $^\\dagger$42\\% of pairs lack WordNet coverage.}\n\\label{tab:scs_baselines}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Metric} & \\textbf{Spearman $\\rho$} & \\textbf{$p$} \\\\\n\\midrule\nFewRel & SCS (embedding) & \\textbf{0.218} & $< 0.001$ \\\\\n(3{,}160 pairs) & Same-parent (WordNet) & 0.097 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.073 & $< 0.001$ \\\\\n& Levenshtein & 0.016 & 0.363 (n.s.) \\\\\n\\midrule\nFew-NERD & SCS (embedding) & \\textbf{0.166} & $< 0.001$ \\\\\n(1{,}953 pairs) & Levenshtein & 0.152 & $< 0.001$ \\\\\n& Same-parent (prefix) & 0.146 & $< 0.001$ \\\\\n& WordNet Wu-Palmer & 0.054 & 0.070 (n.s.)$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Split-Origin Covariate Analysis}\n\\label{app:split-origin}\n\nFewRel combines 64 train-split and 16 val-split relation types into a single 80-type pool.  Train-origin types show numerically lower accuracy ($-8.8$\\,pp, $p = 0.06$; see Limitations), raising the question of whether differential pre-training exposure confounds the BCS--accuracy relationship.  We test this by adding a per-batch \\emph{train-origin ratio} (fraction of relation types drawn from the train split) as a covariate in the BCS--accuracy regression.\n\n\\paragraph{Method.}  Across 213 multi-type batches ($k \\geq 2$) from the batch-composition experiment (\\S\\ref{sec:sdgd}) and the factorial design (\\S\\ref{sec:bcs_controlled}), we compute $\\texttt{train\\_origin\\_ratio} = n_{\\text{train}} / k$ for each batch.  The ratio ranges from 0.40 to 1.00 (mean 0.80, consistent with the 64/80 base rate).  We fit:\n{\\small\\begin{equation*}\n\\text{acc} = \\beta_0 + \\beta_{\\text{BCS}} \\!\\cdot\\! \\text{BCS} + \\beta_{\\text{orig}} \\!\\cdot\\! \\text{train\\_origin\\_ratio} + \\varepsilon\n\\end{equation*}}\n\n\\paragraph{Results.}  The BCS partial effect is unchanged after controlling for split-origin: $\\beta_{\\text{BCS}} = -0.416$, $p < 0.001$ (vs.\\ $\\beta = -0.412$, $p < 0.001$ without the covariate).  Train-origin ratio is not independently significant ($\\beta_{\\text{origin}} = -0.057$, $p = 0.245$), and $\\Delta R^2 = 0.005$.  The BCS--accuracy relationship is therefore not confounded by differential pre-training exposure at the batch level.\n\nPairwise SCS distributions do not differ significantly between train-origin (64 types, mean\\,=\\,0.880) and val-origin (16 types, mean\\,=\\,0.874) subsets (Mann-Whitney $p = 0.754$, Cohen's $d = 0.081$); the train/val split does not introduce systematic confusability bias.\n\n\\section{Cross-Seed Variance Decomposition}\n\\label{app:variance-decomposition}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Variance decomposition on FewRel (3 seeds $\\times$ 25 batches per count level). Batch SD: root-mean intra-seed variance averaged over seeds. Seed SD: standard deviation of per-seed means. Ratio = batch variance / seed variance. At count 80, only one batch composition exists, so batch variance vanishes by construction.}\n\\label{tab:variance_decomposition}\n\\begin{tabular}{rrrr}\n\\toprule\n\\textbf{Count} & \\textbf{Batch SD} & \\textbf{Seed SD} & \\textbf{Ratio} \\\\\n\\midrule\n4 & 0.0889 & 0.0122 & 53.5 \\\\\n8 & 0.0820 & 0.0098 & 70.0 \\\\\n16 & 0.0626 & 0.0270 & 5.4 \\\\\n32 & 0.0462 & 0.0091 & 26.0 \\\\\n40 & 0.0421 & 0.0019 & 474.4 \\\\\n64 & 0.0245 & 0.0022 & 119.8 \\\\\n80 & 0.0001 & 0.0088 & $<$0.1 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:variance_decomposition} shows that intra-batch variance dominates inter-seed variance by 5--474$\\times$ across count levels 4--64 (mean 125$\\times$); random batch composition is the primary source of performance variability. Under greedy decoding (temperature${}\\,=\\,0$), model inference is nearly deterministic; the inter-seed variance reflects differences in which random batch compositions each seed generates, not inference stochasticity. At count 80, the full schema admits only one composition, leaving residual model-level noise as the sole variance source (seed SD = 0.88\\,pp, likely attributable to FP8 quantization non-determinism).\n\n\\section{Cross-Domain Connections}\n\\label{app:cross-domain}\n\nThe schema-associated degradation documented here is not unique to information extraction. Schema-Guided Dialogue systems (SGD/SGD-X; \\citealt{rastogi2020towards}) face an analogous challenge: as the number of intent and slot types grows, dialogue state tracking accuracy declines. \\citet{li2023evaluating} observed count-dependent degradation in ChatGPT-based IE, attributing it to prompt overload. Our two-dimensional decomposition offers a more refined explanation: schema size per se is not the sole predictor; rather, larger schemas increase the probability of including high-SCS pairs, which contribute disproportionately to confusion. This distinction has practical implications: a schema of 80 types with low mutual confusability may outperform a 40-type schema with clustered semantics, and suggests that confusability-aware design principles may generalize to any task where an LLM must discriminate among a prompt-specified label inventory.\n\n\\section{Cross-Model Validation with LLaMA-3.1-70B-Instruct (FP8)}\n\\label{sec:appendix_cross_model_70b}\n\nTo test whether the two-dimensional degradation pattern generalizes across models, we replicate the count-curve and BCS-controlled experiments on Meta-LLaMA-3.1-70B-Instruct (FP8 quantization). All batch compositions, type pools, and test samples are identical to those used for Qwen3-32B (\\S\\ref{sec:count_curves}, \\S\\ref{sec:bcs_controlled}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for LLaMA-3.1-70B-Instruct (FP8) and Qwen3-32B. RE decline (count 8$\\to$80): $-$30.7\\,pp (70B) vs.\\ $-$30.1\\,pp (32B). NER decline (count 2$\\to$22): $-$7.1\\,pp (70B) vs.\\ $-$23.6\\,pp (32B); both models exhibit a U-shaped rebound at higher counts. 25 batches per count level, same samples and batch compositions across models (seed 42). All metrics are micro-averaged across batches.}\n\\label{tab:cross_model_70b}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{LLaMA-70B} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{RE (FewRel, Classification Accuracy)}} \\\\\n8  & 0.757 & 0.805 \\\\\n16 & 0.685 & 0.719 \\\\\n32 & 0.601 & 0.652 \\\\\n64 & 0.504 & 0.539 \\\\\n80 & 0.450 & 0.504 \\\\\n\\midrule\n\\multicolumn{3}{l}{\\textit{NER (Few-NERD, Text+Type Match Recall)}} \\\\\n2  & 0.323 & 0.515 \\\\\n6  & 0.300 & 0.399 \\\\\n12 & 0.278 & 0.318 \\\\\n22 & 0.252 & 0.279 \\\\\n44 & 0.297 & 0.309 \\\\\n66 & 0.273 & 0.407 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_70b} shows that RE degradation slopes are near-identical: $-$30.7\\,pp (70B) versus $-$30.1\\,pp (32B) from count 8 to count 80, with the 70B model approximately 4\\,pp lower in absolute accuracy at each count level. This quantitative match provides strong evidence that Dimension~1 (count-related decline) is directionally consistent across architectures for RE.\n\nOn NER, the count-related decline direction is consistent across models: both 70B and Qwen3 show a recall decline from count 2 to count 22 (70B: 0.323$\\to$0.252, $-$7.1\\,pp; Qwen3: 0.515$\\to$0.279, $-$23.6\\,pp). Both models also exhibit a U-shaped rebound at higher counts (70B: 0.252 at count 22 $\\to$ 0.297 at count 44; Qwen3: 0.279 at count 22 $\\to$ 0.407 at count 66), which cross-validates the U-shape phenomenon. The magnitude difference reflects a precision-recall tradeoff: 70B operates more conservatively (higher precision, lower recall), while Qwen3 over-predicts (higher recall, lower precision, especially at low counts).\n\nFor the confusability dimension (Dimension 2), at count 16 on FewRel, LLaMA-70B achieves low-BCS accuracy of 0.708 versus high-BCS accuracy of 0.599 ($\\Delta = +10.9$\\,pp, 95\\% CI [$+$3.0, $+$20.1]). The confidence interval excludes zero; the confusability effect is thus confirmed at the 70B scale.\n\nIn summary, FewRel RE provides a quantitative match across models (near-identical slopes for Dimension~1 and a significant Dimension~2 effect). NER provides directional consistency: the count-related decline direction is preserved and the U-shaped rebound replicates, though magnitudes vary with each model's precision-recall operating point. Together, these results indicate that the degradation pattern is directionally consistent across architectures.\n\n\\section{Cross-Model Validation with Gemini 2.5 Flash (API)}\n\\label{sec:appendix_cross_model_gemini}\n\nWe validate both dimensions on a proprietary model, Gemini 2.5 Flash \\citep{gemini-2025}, accessed via API. This extends the cross-model evidence from open-weight families (Qwen, LLaMA) to a proprietary architecture with unknown training details. We replicate the FewRel count-curve and BCS-controlled experiments using the same 960 balanced samples, batch compositions, and evaluation protocol as Qwen3-32B.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model count curves for Gemini 2.5 Flash (API) and Qwen3-32B on FewRel RE (classification accuracy). 25 batches per count level, same samples and batch compositions (seed 42). Gemini's count-1 result is included for completeness; Qwen3 count-1 was not collected. Both models show monotonic decline from count 4 onward ($\\rho = -1.0$ for both on counts 4--32). $^\\dagger$Count 64: Gemini based on 11/25 batches (partial).}\n\\label{tab:cross_model_gemini}\n\\begin{tabular}{lrr}\n\\toprule\n\\textbf{Count} & \\textbf{Gemini Flash} & \\textbf{Qwen3-32B} \\\\\n\\midrule\n1  & 0.827 & --- \\\\\n4  & 0.873 & 0.870 \\\\\n8  & 0.820 & 0.805 \\\\\n16 & 0.787 & 0.719 \\\\\n32 & 0.739 & 0.652 \\\\\n64$^\\dagger$ & 0.637 & 0.539 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nTable~\\ref{tab:cross_model_gemini} confirms that the count-related accuracy decline replicates on Gemini 2.5 Flash. From count 4 to count 32, both models show perfectly monotonic decline (Spearman $\\rho = -1.0$). Including count 1, the Gemini count curve yields $\\rho = -0.900$ ($p = 0.037$); including partial count-64 data (11/25 batches), $\\rho = -0.943$ ($p = 0.005$). The decline magnitude is smaller for Gemini ($-$13.3\\,pp from count 4 to 32) than for Qwen3 ($-$21.8\\,pp), consistent with Gemini's higher absolute accuracy providing more headroom before degradation saturates. At each count level, Gemini matches or exceeds Qwen3, with the gap widening at higher counts (0.3\\,pp at count 4 vs.\\ 8.7\\,pp at count 32, 9.8\\,pp at partial count 64); Gemini appears more robust to schema scaling but not immune.\n\n\\paragraph{Dimension~2: BCS-controlled confusability.}\nWe replicate the BCS-controlled experiment on Gemini 2.5 Flash using extreme-BCS batches at count 8 ($n = 50$; 25 low-BCS, 25 high-BCS) and count 16 ($n = 10$; 5+5).\n\nAt count 8, low-BCS batches achieve 90.5\\% vs.\\ high-BCS 72.9\\% ($\\Delta = -17.6$\\,pp, 95\\% CI [15.1, 20.1]). At count 16, the gap narrows to $-$8.7\\,pp, but one high-BCS outlier (BCS${}=0.97$, accuracy 59.9\\%) inflates Pearson $r$; leave-one-out excluding this point drops $r$ from $-$0.80 to $-$0.42 ($p = 0.22$) and $\\rho$ from $-$0.40 to $-$0.18 ($p = 0.64$), confirming the count-16 correlation is driven by this single leverage point. The count-8 gap is smaller than Qwen3-32B's ($-$31.2\\,pp), consistent with ceiling compression: Gemini's higher baseline (90.5\\% vs.\\ 82.3\\%) leaves less room for degradation.\n\nTable~\\ref{tab:cross_model_bcs_summary} summarizes BCS-controlled results across all validated models. Both dimensions thus replicate on a proprietary architecture with unknown training details.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-model BCS-controlled FewRel RE summary. All models show significant low-vs-high BCS accuracy gaps. Gap magnitude varies with model capacity (ceiling compression), but the direction is consistent across open-weight (8B--70B) and proprietary architectures.}\n\\label{tab:cross_model_bcs_summary}\n\\begin{tabular}{llrrrr}\n\\toprule\n\\textbf{Model} & \\textbf{Count} & \\textbf{Low BCS} & \\textbf{High BCS} & \\textbf{$\\Delta$} & \\textbf{95\\% CI} \\\\\n\\midrule\nQwen3-32B     & 8  & 82.3\\% & 51.0\\% & $-$31.2\\,pp & --- \\\\\nQwen3-32B     & 16 & 82.8\\% & 51.6\\% & $-$31.2\\,pp & --- \\\\\nLlama-8B      & 8  & 78.1\\% & 51.0\\% & $-$27.1\\,pp & --- \\\\\nLlama-70B FP8 & 16 & ---    & ---    & $-$10.9\\,pp & {[}3.0, 20.1{]} \\\\\nGemini Flash  & 8  & 90.5\\% & 72.9\\% & $-$17.6\\,pp & {[}15.1, 20.1{]} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Few-Shot Prompting and Confusability}\n\\label{sec:appendix_fewshot_bcs}\n\nTo test whether in-context demonstrations mitigate the BCS-associated confusability effect, we evaluate 0-shot, 1-shot, and 5-shot prompting on FewRel 80-relation RE at count 8 using the same extreme-BCS batch design as \\S\\ref{sec:bcs_controlled}. Each condition uses 50 batches (25 low-BCS, mean $\\approx 0.36$; 25 high-BCS, mean $\\approx 0.80$), drawn from the pre-constructed batch pool of \\S\\ref{sec:bcs_controlled}. Few-shot examples are sampled from the FewRel training split for each target type (Table~\\ref{tab:fewshot_bcs}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{BCS gap under few-shot prompting (FewRel, count 8). Demonstrations improve absolute accuracy on low-BCS batches (+3.3--7.2\\,pp over 0-shot) but provide inconsistent benefit on high-BCS batches (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot). The confusability gap widens from +18.5\\,pp (0-shot) to +22.8\\,pp (5-shot). All metrics are micro-averaged across batches.}\n\\label{tab:fewshot_bcs}\n\\resizebox{\\columnwidth}{!}{\\begin{tabular}{lrrrl}\n\\toprule\n\\textbf{Condition} & \\textbf{Low-BCS} & \\textbf{High-BCS} & \\textbf{$\\Delta$ (pp)} & \\textbf{95\\% CI} \\\\\n\\midrule\n0-shot & 0.682 & 0.498 & +18.5 & {[}+14.3, +22.7{]} \\\\\n1-shot & 0.754 & 0.554 & +20.0 & {[}+16.3, +23.5{]} \\\\\n5-shot & 0.715 & 0.488 & +22.8 & {[}+18.9, +26.8{]} \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nDemonstrations improve absolute accuracy primarily on low-BCS (easy) batches, where type boundaries are already distinct and examples reinforce correct mappings. On high-BCS batches, where types are semantically confusable, demonstrations provide inconsistent benefit (+5.6\\,pp at 1-shot, $-$1.0\\,pp at 5-shot): the model still substitutes similar types at comparable rates. The net effect is that the confusability gap widens under few-shot prompting (+4.3\\,pp from 0-shot to 5-shot, bootstrap $p = 0.014$), with all three confidence intervals excluding zero. This indicates that BCS-associated type confusion is a structural property of the schema composition rather than a deficit addressable through prompt engineering. The non-monotonic low-BCS pattern (0.754 at 1-shot vs.\\ 0.715 at 5-shot) may reflect lost-in-middle effects from increased prompt length \\citep{lost-in-middle-2024}.\n",
      "numLines": 400,
      "startLine": 400,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_015Ep5GwYcQ3m8TCqbBkSH9R`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
  "offset": 799,
  "limit": 300
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "b543450d-efd5-4576-8a86-a7f6cbf6013f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaWDP6Yn6BDcSZb8D6mcRt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13184,
      "cache_read_input_tokens": 57306,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13184
      },
      "output_tokens": 38,
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

_source line 46 · 2026-05-22T06:38:49.002Z_

<details><summary>↩ Tool result · `toolu_015Ep5GwYcQ3m8TCqbBkSH9R`</summary>

```text
799	
800	The 0-shot gap (+18.5\,pp) is smaller than the extreme-batch gap reported in \S\ref{sec:bcs_controlled} (+25.5\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.
801	
802	\section{Qualitative Error Analysis}
803	\label{app:error-analysis}
804	
805	Tables~\ref{tab:top10_re} and~\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\ref{tab:error_examples} provides illustrative confusion instances with SCS values.
806	
807	\begin{table}[h]
808	\centering
809	\footnotesize
810	\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \textit{followed by}/\textit{follows}, SCS\,=\,0.90) and family-relation pairs (\textit{child}/\textit{father}, \textit{child}/\textit{mother}) dominate. Some low-SCS pairs (\textit{instance of}/\textit{taxon rank}, SCS\,=\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}
811	\label{tab:top10_re}
812	\begin{tabular}{cllrr}
813	\toprule
814	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
815	\midrule
816	1 & instance of & taxon rank & 0.53 & 875 \\
817	2 & child & father & 0.84 & 700 \\
818	3 & participant of & participating team & 0.75 & 675 \\
819	4 & mountain range & part of & 0.57 & 575 \\
820	5 & mouth of watercourse & tributary & 0.65 & 549 \\
821	6 & child & mother & 0.84 & 500 \\
822	7 & league & member of & 0.66 & 450 \\
823	8 & country of citizenship & country of origin & 0.76 & 400 \\
824	9 & followed by & follows & 0.90 & 400 \\
825	10 & occupation & voice type & 0.57 & 400 \\
826	\bottomrule
827	\end{tabular}
828	\end{table}
829	
830	\begin{table}[h]
831	\centering
832	\footnotesize
833	\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \textit{person-other}/\textit{person-politician}, SCS\,=\,0.93) and cross-category pairs sharing referent overlap (\textit{building-other}/\textit{location-GPE}, SCS\,=\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}
834	\label{tab:top10_ner}
835	\begin{tabular}{cllrr}
836	\toprule
837	\textbf{\#} & \textbf{Type A} & \textbf{Type B} & \textbf{SCS} & \textbf{$N$} \\
838	\midrule
839	1 & person-other & person-politician & 0.93 & 121 \\
840	2 & location-GPE & organization-other & 0.83 & 81 \\
841	3 & art-film & location-GPE & 0.69 & 57 \\
842	4 & building-other & location-GPE & 0.85 & 56 \\
843	5 & building-other & person-other & 0.90 & 43 \\
844	6 & location-GPE & product-other & 0.69 & 39 \\
845	7 & org-gov/agency & person-other & 0.85 & 34 \\
846	8 & person-actor & person-other & 0.90 & 34 \\
847	9 & building-other & location-road/transit & 0.76 & 32 \\
848	10 & location-GPE & org-sportsleague & 0.81 & 30 \\
849	\bottomrule
850	\end{tabular}
851	\end{table}
852	
853	\begin{table*}[t]
854	\centering
855	\small
856	\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\,$>$\,0.90: \textit{participant} vs.\ \textit{participant of} reverses directionality; \textit{contains} vs.\ \textit{located in} inverts containment; \textit{part of} vs.\ \textit{member of} conflates meronymy with membership. a.t.e.\ = admin.\ territorial entity.}
857	\label{tab:error_examples}
858	\begin{tabular}{p{8cm}llc}
859	\toprule
860	\textbf{Sentence} & \textbf{Gold} & \textbf{Pred.} & \textbf{SCS} \\
861	\midrule
862	\ldots\ played for \textbf{Valencia} \ldots\ [\textbf{EuroLeague}] & participant & participant of & 0.97 \\
863	\addlinespace
864	\textbf{Pilões} is a municipality in \textbf{Rio Grande do Norte} \ldots & contains a.t.e. & located in a.t.e. & 0.92 \\
865	\addlinespace
866	Davies \ldots\ appointed to \textbf{Cabinet} as \textbf{Sec.\ of State} & part of & member of & 0.90 \\
867	\bottomrule
868	\end{tabular}
869	\end{table*}
870	
871	\section{Schema Label Renaming Experiment}
872	\label{app:renaming}
873	
874	To test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \textit{participant of} $\to$ \textit{event involvement} (SCS: 0.97 $\to$ 0.72), \textit{follows} $\to$ \textit{prior entry} (0.90 $\to$ 0.69), \textit{part of} $\to$ \textit{integral segment of} (0.90 $\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\ref{tab:renaming}).
875	
876	\begin{table}[h!]
877	\centering
878	\small
879	\caption{Accuracy (\%) under original vs.\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\Delta_{\text{high}} - \Delta_{\text{low}} = -5.9$\,pp ($t = -7.23$, $p < 0.001$).}
880	\label{tab:renaming}
881	\begin{tabular}{lccc}
882	\toprule
883	& \textbf{Control} & \textbf{Treatment} & \textbf{$\Delta$\,(pp)} \\
884	\midrule
885	Low-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\
886	High-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\
887	\bottomrule
888	\end{tabular}
889	\end{table}
890	
891	Renaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\geq$ original $-5$\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.
892	
893	\section{Relaxed Matching Evaluation (NER)}
894	\label{app:relaxed-matching}
895	
896	To test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\times$ 25 batches $\times$ 3 seeds; Table~\ref{tab:relaxed_matching}).
897	
898	\begin{table}[h!]
899	\centering
900	\small
901	\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\,pp (98.4\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}
902	\label{tab:relaxed_matching}
903	\begin{tabular}{lrrrrr}
904	\toprule
905	\textbf{Match mode} & \textbf{$r$} & \textbf{$p$} & \textbf{$\rho$} & \textbf{$p$} & \textbf{F1} \\
906	\midrule
907	Exact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\
908	Relaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\
909	Token overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\
910	Type-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\
911	\bottomrule
912	\end{tabular}
913	\end{table}
914	
915	A per-error-mode analysis confirms this null extends to all individual categories: miss ($\rho = 0.017$), boundary ($\rho = -0.043$), and type substitution ($\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.
916	
917	\end{document}
918	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "b4d4ebff-b8e6-405c-83ac-b0ddf910cc23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/main.tex",
      "content": "\nThe 0-shot gap (+18.5\\,pp) is smaller than the extreme-batch gap reported in \\S\\ref{sec:bcs_controlled} (+25.5\\,pp) because the two experiments use different test splits and batch sampling seeds; direct magnitude comparison across experiments is not appropriate.\n\n\\section{Qualitative Error Analysis}\n\\label{app:error-analysis}\n\nTables~\\ref{tab:top10_re} and~\\ref{tab:top10_ner} list the ten most frequently confused type pairs on FewRel 80-relation RE and Few-NERD NER. Confusion counts are aggregated bidirectionally across three random seeds (72{,}000 predictions per seed for RE; single-seed 66-type extraction for NER). Table~\\ref{tab:error_examples} provides illustrative confusion instances with SCS values.\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused relation pairs on FewRel 80-relation RE. $N$: bidirectional confusion count aggregated over 3 seeds $\\times$ 25 batches. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). High-SCS pairs (e.g., \\textit{followed by}/\\textit{follows}, SCS\\,=\\,0.90) and family-relation pairs (\\textit{child}/\\textit{father}, \\textit{child}/\\textit{mother}) dominate. Some low-SCS pairs (\\textit{instance of}/\\textit{taxon rank}, SCS\\,=\\,0.53) reflect domain-specific co-occurrence rather than semantic similarity.}\n\\label{tab:top10_re}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & instance of & taxon rank & 0.53 & 875 \\\\\n2 & child & father & 0.84 & 700 \\\\\n3 & participant of & participating team & 0.75 & 675 \\\\\n4 & mountain range & part of & 0.57 & 575 \\\\\n5 & mouth of watercourse & tributary & 0.65 & 549 \\\\\n6 & child & mother & 0.84 & 500 \\\\\n7 & league & member of & 0.66 & 450 \\\\\n8 & country of citizenship & country of origin & 0.76 & 400 \\\\\n9 & followed by & follows & 0.90 & 400 \\\\\n10 & occupation & voice type & 0.57 & 400 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\footnotesize\n\\caption{Top-10 confused entity type pairs on Few-NERD NER. $N$: bidirectional confusion count from 66-type full-schema extraction. SCS: pairwise Schema Confusability Score (Qwen3 embedding cosine similarity). Intra-category confusions (e.g., \\textit{person-other}/\\textit{person-politician}, SCS\\,=\\,0.93) and cross-category pairs sharing referent overlap (\\textit{building-other}/\\textit{location-GPE}, SCS\\,=\\,0.85) are most frequent. The ``other'' subtypes absorb diverse entities and confuse with more specific siblings.}\n\\label{tab:top10_ner}\n\\begin{tabular}{cllrr}\n\\toprule\n\\textbf{\\#} & \\textbf{Type A} & \\textbf{Type B} & \\textbf{SCS} & \\textbf{$N$} \\\\\n\\midrule\n1 & person-other & person-politician & 0.93 & 121 \\\\\n2 & location-GPE & organization-other & 0.83 & 81 \\\\\n3 & art-film & location-GPE & 0.69 & 57 \\\\\n4 & building-other & location-GPE & 0.85 & 56 \\\\\n5 & building-other & person-other & 0.90 & 43 \\\\\n6 & location-GPE & product-other & 0.69 & 39 \\\\\n7 & org-gov/agency & person-other & 0.85 & 34 \\\\\n8 & person-actor & person-other & 0.90 & 34 \\\\\n9 & building-other & location-road/transit & 0.76 & 32 \\\\\n10 & location-GPE & org-sportsleague & 0.81 & 30 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Illustrative confusion instances from FewRel 80-rel RE. All gold-predicted pairs have SCS\\,$>$\\,0.90: \\textit{participant} vs.\\ \\textit{participant of} reverses directionality; \\textit{contains} vs.\\ \\textit{located in} inverts containment; \\textit{part of} vs.\\ \\textit{member of} conflates meronymy with membership. a.t.e.\\ = admin.\\ territorial entity.}\n\\label{tab:error_examples}\n\\begin{tabular}{p{8cm}llc}\n\\toprule\n\\textbf{Sentence} & \\textbf{Gold} & \\textbf{Pred.} & \\textbf{SCS} \\\\\n\\midrule\n\\ldots\\ played for \\textbf{Valencia} \\ldots\\ [\\textbf{EuroLeague}] & participant & participant of & 0.97 \\\\\n\\addlinespace\n\\textbf{Pilões} is a municipality in \\textbf{Rio Grande do Norte} \\ldots & contains a.t.e. & located in a.t.e. & 0.92 \\\\\n\\addlinespace\nDavies \\ldots\\ appointed to \\textbf{Cabinet} as \\textbf{Sec.\\ of State} & part of & member of & 0.90 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Schema Label Renaming Experiment}\n\\label{app:renaming}\n\nTo test whether reducing pairwise SCS through label renaming improves accuracy, we conducted a controlled intervention on FewRel 80-relation RE (count 8, Qwen3-32B). We identified 14 high-SCS relation pairs (covering 12 unique relation types, as two types each appear in multiple pairs; mean SCS = 0.87) and replaced one label in each pair with a semantically distinct paraphrase chosen to minimize embedding cosine similarity (all-MiniLM-L6-v2). Examples: \\textit{participant of} $\\to$ \\textit{event involvement} (SCS: 0.97 $\\to$ 0.72), \\textit{follows} $\\to$ \\textit{prior entry} (0.90 $\\to$ 0.69), \\textit{part of} $\\to$ \\textit{integral segment of} (0.90 $\\to$ 0.64). The renaming reduced mean pairwise SCS from 0.87 to 0.67 ($\\Delta = -0.20$). We ran the same 50 BCS-controlled batches (25 low-BCS, 25 high-BCS; 96 samples each) under both original (control) and renamed (treatment) label sets (Table~\\ref{tab:renaming}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{Accuracy (\\%) under original vs.\\ renamed labels on FewRel count-8 batches. Renaming reduced embedding similarity but decreased accuracy in both groups, with a larger drop on high-BCS batches (Cohen's $d = -2.92$) than low-BCS ($d = -1.09$). Interaction: $\\Delta_{\\text{high}} - \\Delta_{\\text{low}} = -5.9$\\,pp ($t = -7.23$, $p < 0.001$).}\n\\label{tab:renaming}\n\\begin{tabular}{lccc}\n\\toprule\n& \\textbf{Control} & \\textbf{Treatment} & \\textbf{$\\Delta$\\,(pp)} \\\\\n\\midrule\nLow-BCS ($n=25$)  & 90.1 & 87.1 & $-$3.0 \\\\\nHigh-BCS ($n=25$) & 69.3 & 60.5 & $-$8.8 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nRenaming hurt accuracy uniformly: both groups showed significant declines (paired $t$-test, both $p < 0.001$). The number of renamed types per batch correlated negatively with accuracy change ($r = -0.625$, $p < 0.001$). A solo sanity check confirmed that 11 of 12 renamed labels were individually recognizable (accuracy $\\geq$ original $-5$\\,pp). The results indicate that replacing familiar Wikidata labels with unfamiliar paraphrases disrupts the model's type semantics; this label unfamiliarity effect outweighs any benefit from reduced confusability.\n\n\\section{Relaxed Matching Evaluation (NER)}\n\\label{app:relaxed-matching}\n\nTo test whether exact-match F1 masks the BCS signal in NER by conflating boundary errors with type errors, we evaluate three progressively relaxed matching criteria on the full Few-NERD NER dataset ($n = 450$ batches: 6 count levels $\\times$ 25 batches $\\times$ 3 seeds; Table~\\ref{tab:relaxed_matching}).\n\n\\begin{table}[h!]\n\\centering\n\\small\n\\caption{BCS--F1 correlation under progressively relaxed NER matching. Relaxed span credits a match if the predicted span overlaps the gold span and the type is correct; token overlap uses token-level intersection; type-ignored drops the type constraint entirely. Relaxed matching improves mean F1 by 4.2\\,pp (98.4\\% of batches improve), but Pearson $r$ remains near zero across all modes (bootstrap 95\\% CI crosses zero in all cases). Boundary errors affect all batches uniformly and do not mask a BCS signal.}\n\\label{tab:relaxed_matching}\n\\begin{tabular}{lrrrrr}\n\\toprule\n\\textbf{Match mode} & \\textbf{$r$} & \\textbf{$p$} & \\textbf{$\\rho$} & \\textbf{$p$} & \\textbf{F1} \\\\\n\\midrule\nExact        & 0.014 & 0.760 & $-$0.101 & 0.033 & 0.304 \\\\\nRelaxed span & 0.003 & 0.946 & $-$0.110 & 0.020 & 0.346 \\\\\nToken overlap & 0.004 & 0.936 & $-$0.113 & 0.017 & 0.349 \\\\\nType-ignored & 0.023 & 0.621 & $-$0.097 & 0.039 & 0.425 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nA per-error-mode analysis confirms this null extends to all individual categories: miss ($\\rho = 0.017$), boundary ($\\rho = -0.043$), and type substitution ($\\rho = -0.010$) rates show no BCS association (all $p > 0.3$, $n = 450$). The null holds within each count level (count 2: $r = 0.022$; count 6: $r = 0.110$; count 12: $r = 0.028$; all $p > 0.3$), ruling out count as a confound.\n\n\\end{document}\n",
      "numLines": 120,
      "startLine": 799,
      "totalLines": 918
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full paper. Let me systematically go through it and identify all the issues mentioned in the task:

1. **Repeated expressions** - same point said in multiple sections
2. **Vague language** - "some", "several", "various", "significant" 
3. **Passive → active** voice
4. **Long sentences** - >35 words
5. **Figure/Table captions** - self-contained?
6. **Abstract polish**

Let me plan my edits carefully. I need to track all changes for the summary table.

Let me work through each file systematically.

### ABSTRACT (abstract.tex)


Checking the abstract for clarity and consistency. The main claims look solid—schema complexity drives performance through two independent dimensions, type count affects recall, and inter-type confusability predicts substitution errors. I'm verifying the reported statistics against the body text to make sure the numbers align correctly. I'm noticing that findings (1) and (2) both report the same R² ≈ 0.22 result, which creates redundancy — (1) frames it at the individual error level while (2) presents it at the ecological level across models. I should consider whether both formulations are necessary or if one could be trimmed to tighten the abstract. I need to remove the redundant R² and VIF statistics from the first point and consolidate them into the second point where they're more central. I should also eliminate the duplicate mention of the NER null result, keeping it only in the second point. Let me revise the abstract to tighten these overlaps while maintaining the logical flow of the argument. I'm checking the word count on this sentence about training-free LLM information extraction—it's running long at 32 words, so I should tighten it up while keeping the core idea that prompting models without fine-tuning enables quick deployment across different domains and schemas.

The zero-shot approach eliminates the need for labeled data, which is valuable when annotation is costly or schemas change frequently. But there's a fundamental tradeoff: performance drops significantly as the schema grows larger. Looking at the named entity recognition results, recall plummets from 0.72 with a single type down to around 0.27 when the schema expands to 22-44 types, with only partial recovery at the full schema size.

The relation extraction numbers are even more dramatic. Accuracy falls from 85.7% with one relation type to 50.4% with 80 relations at the sentence level, and from 88.0% down to 38.7% with 96 relations at the document level—essentially cutting performance in half or worse.

This matters in practice because real-world ontologies typically define 50 to 200+ types, putting them right in the zone where training-free extraction becomes unreliable.

Prior work on decomposition strategies has conflated two separate issues: the sheer number of types to distinguish between, and the semantic similarity between types that causes confusion. These are distinct dimensions that need separate treatment.

I'm now checking the word counts on the contribution statements. The first one establishes that type confusability—measured through embedding similarity metrics—independently predicts substitution errors in relation extraction, accounting for roughly 22% of variance at the batch level on the FewRel dataset.

The second contribution documents a task asymmetry, though it's cut off mid-sentence.

Looking at the redundancy issue: both contributions mention the same ~22% variance explained and VIF = 1.18 statistic. I should consolidate this into the first contribution and remove it from the second to avoid repetition.

For Contribution 2, the next thinking shows it's about BCS explaining variance in RE accuracy through type substitution, with format-independence confirmed, but NER showing no batch-level signal despite pairwise effects. That's roughly 50 words as noted, so I need to split it into shorter pieces.

For Contribution 3, it's cut off but appears to be about structural barriers to confusability-aware extraction, with schema decomposition failing due to merge amplification and routing issues.

Let me rewrite more concisely:

We find that type confusability, measured through embedding similarity, independently predicts substitution errors in relation extraction on FewRel—explaining roughly 22% of batch-level variance with minimal confounding (VIF = 1.18). This effect holds across different formats, yet we don't detect comparable batch-level signal in NER despite observing significant pairwise patterns. Additionally, schema decomposition approaches fail due to merge amplification in NER and ED tasks, plus routing failures in RE, suggesting the decompose-then-merge paradigm faces fundamental limitations. I'm checking the Related Work section now. The opening sentence about moderate schemas is concise and active. The main contribution statement is lengthy at 50+ words with its three-part enumeration, but the numbered structure keeps it readable, so I'll keep it as is. The key point is that we're contrasting our controlled analysis approach against LLM-PEE's assumption that decomposition inherently helps.

The follow-up sentences establish what we actually demonstrate: the role of confusability, the merge amplification bottleneck, and BCS as a predictor. Then I'm noting that other concurrent work treats schema complexity as an engineering problem through hard negative mining, schema optimization, multi-agent debate, and active prompting—all missing the underlying degradation factors. There's also a recent finding that instance count matters more than context length for LLM processing, which aligns with our count-dominant results. I'm now looking at a citation about familiarity that seems incomplete. I'm splitting that paragraph since it's running long, then noting that the modest pairwise correlation compounds at the batch level to explain around 22% of variance—though I'm realizing I've already cited this finding multiple times across the abstract and introduction, so I should probably just reference the detailed section instead of repeating the number again.

Now I'm reviewing the experimental setup section. The Few-NERD description is mostly solid, but I can tighten it by cutting the vague phrase about cross-domain suitability. The sampling strategy and evaluation approach are clear. I'm checking the pairwise analysis coverage across the type pairs.

For FewRel, I notice they combined training and validation splits to get the full 80-relation pool, then sampled 1,000 balanced instances. That sentence is a bit long—I could split it after mentioning the combined pool. The validation check for generalization across the split boundary is fine. The task description is straightforward: classify relations between marked entities in sentences.

FewRel's balanced design with 700 instances per relation type removes frequency as a confound, making it ideal for BCS analysis. The contamination analysis shows extraction difficulty correlates with training prevalence, but BCS effects hold even when controlling for this.

For DocRED, they're using 96 relation types from Wikidata at the document level. They sampled 1,000 instances balanced across those types from the development set and framed the task the same way as FewRel—classify the relation given a document with marked entities.

DocRED extends the evaluation to a larger schema and document-level context, testing whether confusability effects persist across longer inputs and multi-sentence reasoning.

MAVEN defines 168 event types from FrameNet, all within a single ontology. They're using the validation set for evaluation since test labels aren't public. MAVEN plays a supplementary role because its same-domain schema introduces centrality confounds at the batch level.

For SCS, I'm computing it with Qwen3-32B's hidden-state representations and all-MiniLM-L6-v2, a sentence encoder. Few-NERD uses Qwen3 because its fine-grained category pairs need the higher-dimensional space, while MiniLM serves as the primary BCS embedding since sentence-transformers are trained for semantic similarity.

I'm noting that Qwen3's causal language model states show compressed BCS range compared to MiniLM, which aligns with known autoregressive anisotropy patterns. Using only names for SCS yields equivalent predictive accuracy to including definitions. Most importantly, SCS acts as a pre-hoc proxy that doesn't require running extraction, and pairwise SCS correlates meaningfully with observed type confusion across both Few-NERD and FewRel datasets.

For the experimental setup, I'm sampling multiple random type batches at each count level to evaluate the same test samples consistently, with the count levels themselves following natural partition points in the schema hierarchy rather than uniform spacing.

In Experiment 2, I'm fixing the type count and varying batch confusability to isolate that factor from schema size effects, constructing both extreme batches through greedy search and random batches for comparison. For inference, I'm using Qwen3-32B-FP8 served through vLLM on a single RTX PRO 6000 GPU with greedy decoding. I'm testing two prompt versions—one requesting character offsets and another adding format constraints that improve precision—and reporting both to show how sensitive the results are to formatting choices.

Since I'm using single-seed greedy decoding, model-level randomness is minimal, though FP8 quantization introduces some residual variance that I'm capturing through bootstrap confidence intervals at both the pair and batch levels.

Now I'm reviewing the results section, checking that all experiments use the same model and prompt unless otherwise specified, with cross-model validation limited to the first two dimensions while other analyses stick with the single model.

Looking at the count-degradation curves, I'm seeing that relation extraction accuracy drops consistently as schema size increases, NER recall shows a dip through mid-range counts before recovering slightly at full schema when type-filtering overhead is removed, and DocRED follows the same monotonic decline pattern.

The effect holds across different model sizes and random seeds, with inter-seed variance staying well below the within-batch variance, and formal statistical tests confirm the monotonic trend in relation extraction performance.

Now I'm checking whether pairwise semantic similarity predicts confusion patterns between entity types—for each type pair, I'm computing how often instances of one type get misclassified as another and correlating that with their semantic similarity scores.

The correlations are statistically significant but weak, explaining only about 1.3–1.7% of the variance. The remaining confusion comes from factors like entity frequency, prompt position, and mention-level ambiguity. I notice this explanation overlaps with what I said earlier in the SCS section, so I should probably just reference that earlier point rather than repeat it. But the key finding is that even though pairwise similarity alone is modest, when I look at how correlated type pairs cluster within batches, the batch-level signal becomes much stronger—explaining around 22% of the variance in relation extraction accuracy on FewRel.

I'm noticing I've mentioned that 22% figure way too many times already—it appears in the abstract, both contribution statements in the intro, the related work section, and now again here. Let me count exactly how many times this number shows up across the paper to see if I need to trim some of these repetitions.

Looking through the results sections, the actual primary finding is reported in §4.3, but I've been anticipating it earlier in §4.2 and then referencing it again in §4.5. The abstract and intro contributions definitely need it, but I should probably consolidate the other mentions and just point back to §4.3 instead of restating the figure each time.

The practical fix here is to keep the main report in §4.3 where it belongs, keep it in the abstract and intro since those are essential, but cut the redundant mentions in the related work section and the anticipatory reference in §4.2.

Let me work through the specific changes systematically. I'll start with the abstract — I can remove the R² value from the first finding since it's already in the second one, and that'll tighten things up. Then I'll tackle the introduction, particularly that long contribution sentence that needs breaking up.

For related work, I need to split that 38-word sentence about LLM-PEE and our metrics, and replace the ecological batch level mention with a forward reference to section 4.3 instead of spelling out the 22% figure again.

In the experimental setup section, I'm trimming the vague language about cross-domain suitability, breaking up the long sentences about validation splits and sampling procedures, and handling the DocRED description. The greedy search for extreme batches is cut off, so I'll finish that thought naturally based on what comes next.

For the extreme batch construction, the algorithm selects types based on similarity scores from the pairwise matrix—the low-BCS batch greedily picks the least-similar pair first and keeps adding types with the lowest maximum similarity to what's already selected, while the high-BCS batch does the opposite by maximizing similarity at each step.

In the results section, I'm noting that forward references should replace repeated numbers, and the discussion of residual variance should either reference the earlier validation section or provide more specific analysis depending on what the results actually show.

Looking at the overlap between sections, the SCS validation mentions context-dependent factors that contribute to residual variance, while the results section lists entity frequency, position, mention ambiguity, and definition quality—these are complementary rather than redundant, so I'll keep both as written.

The 22% variance explained appears both in the section header and in the first results sentence, but since this is where it's formally reported with statistical backing, the repetition is justified.

For the FewRel balanced design note, it does restate information from the datasets section, but the footnote provides necessary context for readers following the results without reviewing earlier sections. This is standard practice, so I'll leave it intact.

Now I'm checking the practical magnitude paragraph to see if there are similar issues with repetition or unnecessary restating. I'm checking section 4.5 on multi-dimensional degradation and verifying that the error taxonomy decomposition results are clearly presented—specifically the monotonic scaling of intra-batch substitution errors with BCS across the three datasets, with correlation coefficients and p-values for each. I'm reviewing the statistical methodology for establishing separability across these datasets. The full-range regression with five count levels serves as my primary test, while the factorial design acts as a sensitivity check. For the equivalence margin, I'm using convergent evidence: an interaction that exceeds the main effect would undermine dimensional separability, and Cohen's medium effect size combined with the within-cell standard deviation gives me a margin of ±2.3 percentage points. Now I'm setting up the TOST equivalence test on the linear scale... On DocRED, the confounding from narrow BCS ranges shrinks the raw interaction effect substantially when I account for range-matched analysis. In NER, I'm not detecting a batch-level BCS signal at the current statistical power, which stems from two sources: errors scatter across multiple failure modes rather than concentrating in one type, and the restricted BCS range limits my ability to detect effects.

With the sample size and BCS variability in NER, I'd need a correlation of at least |r| ≈ 0.132 to detect it reliably, but FewRel's much stronger effect would weaken considerably under this compression. The real issue is that I can't tell whether there's genuinely no BCS effect on NER or whether any effect is simply too subtle to measure—the data are consistent with both possibilities. The error-mode distribution explanation fits equally well: degradation spreads across different failure channels rather than concentrating in type substitution.

I'm noticing I've already made this point about error distribution, so I should avoid restating it. The mitigation attempts—renaming types and few-shot prompting—both fail to bridge the confusability gap, which suggests BCS reflects something fundamental about how the schema and model interact rather than just a naming quirk.

For the discussion section, I'm seeing the same issue: the modest pairwise r² value keeps getting repeated across related work, results, and now here. I should either reference the earlier section or reframe it. And I notice the NER-RE thought cuts off mid-sentence.

Looking at the SDGD section, it's checking whether partitioning the schema to separate confusable types actually works. The approach uses a greedy graph-based decomposition strategy, but the thinking trails off before explaining the outcome.

The next chunk reveals the key finding: oracle routing can recover performance, but practical routing strategies underperform the baseline, and decomposing NER actually makes false positives worse. The real constraint is routing accuracy, not how well the types are partitioned. The full details are deferred to the appendix.

Now moving into table and figure captions, starting with the dataset statistics table. For Figure 1, the key findings are that RE performance declines steadily while NER follows a U-shaped pattern, and the BCS-controlled accuracy shows consistent slopes across different relation conditions despite wider variance at 80 relations. Table 2 measures pairwise confusion correlations using bidirectional confusion rates.

Now looking at Figure 2, the error taxonomy shows IntraSub scaling monotonically with BCS across datasets, while RE missed rates stay relatively flat at 10-16% but NER missed rates are much higher at 43-65% and vary non-monotonically.

For Table 3, I'm checking the IntraSub and missed-entity rates across BCS bins—computed over 148 NER batches, 154 RE batches, and 110 DocRE batches. The key insight is that DocRE missed rates actually decrease with BCS, suggesting high-confusability errors shift from omission to substitution rather than staying constant.

I should also flag some passive voice that could be tightened—like "the batch-level BCS signal is not detected in NER" would be stronger as "we do not detect a batch-level BCS signal in NER." I'm checking for vague language now—scanning for "some," "several," "various," and "significant" throughout the text. Most instances are either absent or used appropriately in academic contexts. The word "significant" appears correctly as "statistically significant" and "highly significant," though I should verify the remaining uses are precise rather than hedging.

Looking at modifiers like "substantially," they're generally acceptable since they're paired with quantitative support—like when "substantially reduces" is followed by specific residual SD values. The paper seems fairly tight on vague language overall, so I should focus on concrete, actionable improvements rather than minor word choices.

I'm starting with a list of planned edits: removing the redundant R² value from the abstract since it's already stated elsewhere.

For the introduction, I need to break up that 60-word contribution sentence and eliminate the VIF statistic that duplicates information from earlier. The related work section has a 38-word sentence about SCS novelty that needs splitting, plus I should replace the approximate percentage with a proper reference to the results section.

In experimental setup, I'm trimming unnecessary qualifiers from the Few-NERD description, splitting the long FewRel and DocRED sentences, and converting passive voice to active when describing batch construction. The results section needs similar attention to sentence length and clarity.

For the discussion, I'm replacing a vague phrase about compounding effects with a direct section reference. I should also watch the page budget carefully—splitting sentences doesn't add words, just punctuation, so the real savings come from removing redundancies. Let me verify I'm staying within the 8-page limit as I make these edits.

Now I'm reconsidering the abstract. The current version states the R² value twice—once as 0.22 in the first point and again as ~22% in the second—which is redundant. I need to consolidate these to avoid repeating the same finding.

The key insight is that point (1) should emphasize BCS's independent predictive power for type substitution errors (shown by the VIF), while point (2) should carry the variance explanation at the ecological level. Let me restructure to remove the R² from (1) and keep the fuller interpretation in (2), then compress the abstract findings into a cleaner narrative. I'm checking whether splitting these findings changes the claim strength—it shouldn't, since I'm just reorganizing how the results are presented rather than altering what they actually show. Now let me look at how to frame the first contribution more concisely, focusing on the core finding about confusability predicting type substitution errors in RE while controlling for count effects. I'm wrestling with how to preserve the quantitative specificity of contribution 2 while avoiding redundancy with contribution 1. The key distinction is that while contribution 1 establishes the RE effect magnitude, contribution 2 needs to highlight the task asymmetry—that this confusability signal appears robustly in RE but remains undetected for NER even at the pairwise level, suggesting a genuine task difference rather than a power issue. I'm verifying that the count_40 constraint is already satisfied in the paper—the results section explicitly states "40-relation subsets sampled from the 80-relation pool," and the experimental setup lists the full range of count levels including 40. The constraint is met.

Now I need to finalize my editing plan and check the table captions for clarity. Looking at the dataset statistics table, I notice the caption defines BCS range and embedding choices but doesn't explain what S represents, so I should add that definition to make it self-contained.

The pairwise correlation table caption already includes the metric definition with the bidirectional confusion formula, so that's fine. The error taxonomy table is also self-contained with its key findings. For the figures, the captions look adequate.

I should also review the Discussion section to see if numbers reported there are just repeating what's already in Results without adding new insight.

The first discussion paragraph mentions "modest pairwise r²" conceptually rather than citing a specific number, and while it references batch-level compounding that appeared earlier, it's appropriately condensed for discussion purposes. The second paragraph starts discussing practical implications for NER and RE, which seems to be moving toward recommendations rather than restating results.

Now I'm planning the specific edits needed. For the abstract, I need to remove the redundant R² ≈ 0.22 measurement and the NER null finding from the main findings, since those details are already covered in the results section. The goal is to tighten the abstract by keeping only the most essential discoveries and letting the detailed metrics live in the body of the paper. I'm double-checking the original formulations to make sure I've reorganized the findings correctly—the R² value and VIF should stay with the RE results in point (1), while the replication across model sizes belongs in point (2) along with the NER null finding. I'm refining the contribution statement to be clearer and more concise. The key insight is that type confusability independently predicts substitution errors in relation extraction, explaining about 22% of variance across models—a finding that's only possible because the batch design separates confusability effects from type frequency. I'll split this into a tighter, more focused claim without the methodological details cluttering the main point. I'm refining contribution 2 to avoid redundancy with the first point—removing the specific variance numbers since they're already established, and instead focusing on the key finding that the confusability effect holds across formats while the NER signal remains elusive, which I'm attributing to error distribution differences and measurement constraints. I'm splitting that long sentence about SCS/BCS metrics into two clearer statements, then replacing the ~22% reference with a pointer to the controlled batch methodology section.

For the pairwise r² finding, I need to fix the grammar—"compounds to explain" works better than "compounds to substantial"—and keep the cross-batch variance explanation intact.

On the Few-NERD dataset description, "spans diverse domains" already conveys cross-domain suitability, so removing the redundant phrase is the right call.

Now I'm splitting up the FewRel and DocRED sampling descriptions into separate sentences for clarity. The FewRel point about combining splits to get the full 80-relation pool deserves its own sentence, separate from the sampling details. Same approach for DocRED—breaking out the instance count and relation type distribution from whatever comes next in the task formulation.

For the extreme batch construction, I'm converting the passive voice to active ("we construct") and splitting the greedy search explanation into its own sentence before diving into the low-BCS and high-BCS logic.

Now looking at the results section edits. For the batch-level BCS variance claim, I'm removing the specific ~22% figure and the forward reference, instead just noting that correlated type pairs compound the signal into substantial variance with a reference to the controlled analysis section.

Then in the NER error modes section, there's redundancy where the distribution across miss, boundary, and type gets mentioned twice. I should consolidate this so it's stated once rather than repeated. I'm working through the logic of this section on statistical power and error modes. The key issue is that the current evidence can't distinguish between no real effect and an effect too small to detect given the sample size and range restrictions. The second sentence about error-mode structure is redundant—it restates what was already covered earlier as one of the possible explanations. I should trim this down to just the core distinction between absence of evidence and evidence of absence, then move forward without repeating the error-mode point. I'm realizing the structural difference explanation is redundant—I already covered that reasoning earlier as factor (1). The "absence of evidence" framing captures the epistemological problem more concisely without restating what's already been established. I'll cut the detailed restatement and let the two-factor explanation stand on its own, then move directly to the post-hoc mitigation discussion. This keeps the flow tighter and trusts the reader to connect the dots.

Now I'm looking at a long TOST sentence that needs splitting. The original runs 41 words and mixes the justification for using probability-scale TOST with the logit-scale results. I'm breaking it into two sentences—the first explains why probability-scale is primary, the second reports the logit-scale findings separately. This improves readability without losing any information.

For the "two factors explain the asymmetry" sentence, it's already well-structured with enumerated points (1) and (2), making it easy to follow despite being 47 words. The enumeration serves a purpose here, so I'm keeping it as is.

The next item about $n=450$ appears to be cut off mid-sentence, so I'll wait to see the complete thought before addressing it. I'm verifying the word count for that sentence about FewRel's correlation attenuation—it comes to about 24 content words plus the mathematical notation, which is acceptable. I should also check the discussion section where I mention how modest pairwise correlations compound at the batch level due to correlated type interactions within shared prompts, and that seems fine as a conceptual summary for that section. Now I'm scanning through for passive voice constructions like "was observed" or "was found" that could be tightened—I notice the experimental setup describes evaluating two NER/ED prompt versions in a somewhat passive way that could shift to active voice, though it's borderline. instructed to keep it concise, so I need to trim this down significantly. The Limitations section should focus on the most critical constraints rather than enumerate every possible limitation. I'll consolidate the five numbered points into three main categories and remove the extra paragraphs to match the requirement. I'm told not to change the paper structure—no moving paragraphs or adding/removing sections. But trimming content within the Limitations section should be fine, especially since the EMNLP 2026 guidelines say it only needs to cover about 3 points without being lengthy. The constraint about not changing claim strength is tricky though, since cutting limitations could weaken the candor. Let me focus on the main task: scanning for repetition, vagueness, passive voice, and long sentences. The Limitations section doesn't seem to have obvious issues in those areas, so I'll leave it unless I spot specific problems. Let me check for vague language like "various," "some," or "several," and scan the sentence lengths. Gemini only provides partial corroboration through leave-one-out analysis, with correlation dropping substantially, and the question of whether proprietary models generalize remains unresolved.

The pairwise SCS effect captures just a small slice of type confusion variance—entity frequency, prompt position, and mention ambiguity likely explain most of the rest.

The count-by-BCS interaction shows different patterns across datasets: bounded on FewRel but present on DocRED, though the BCS range restriction at higher counts muddies the picture, and the logit-scale evidence isn't definitive.

For DocRED, I'm using 5 batches per level to manage the higher computational cost of evaluation.

The controlled experiments rely on a single seed with greedy decoding, keeping residual variance small, though exact magnitudes could shift slightly.

Greedy decoding produces a residual standard deviation around 0.88 percentage points—roughly 18 to 44 percent of the observed BCS effect—which suggests the effect is detectable but the point estimates carry real uncertainty; the interaction estimate of 0.47 percentage points sits comfortably within the equivalence margin.

I should also verify the page count against the 8-page body limit, but I don't have that information yet.

My edits are mostly neutral or slightly reducing text, so the page count should work out fine once I compile and check.

Let me do a final pass for any remaining issues—scanning for redundant phrases like "In this paper" or filler words like "importantly" and "notably."

I notice the checklist is commented out in the main file, so that's not included in the PDF. Now looking at the dataset table caption more carefully, it's mostly self-contained but doesn't explicitly define SCS and BCS. Since those are defined just above in the section, I could add a cross-reference to make it clearer—something like adding "(§\ref{sec:scs})" after mentioning SCS/BCS to help readers find the definitions.

Actually, wait—the task specifies that abbreviations should be defined at first occurrence, but SCS and BCS first appear in the abstract, not here in the table. The table comes after the full definition in §3.2, so there's no need to redefine them in the caption.

For Figure 1, I need to check if the caption conveys the key takeaway or just describes what's shown. The current caption explains the technical details—error bars, the U-shape pattern for NER, the monotonic decline for RE—but it doesn't explicitly state what we should learn from this. I should add a sentence that captures the main finding, like how the degradation patterns differ between tasks or what this reveals about the models' behavior.

Looking at Figure 2's caption, it already includes the key findings: the monotonic scaling of IntraSub with BCS, the flat RE missed rates versus the higher and non-monotonic NER missed rates. That's good—it's not just describing the taxonomy but highlighting what matters.

I'm satisfied with my edits. Let me add one more guideline to my list about how to handle the discussion section.

For Contribution 3 in the introduction, that sentence is right at the boundary—35 words with good structure explaining the three failure modes and their implications. I'll keep it as is.

Now I'm ready to execute all these edits across the document.

Actually, let me also check for consistency in how we're representing the R² values. I'm seeing "${\sim}$22\%" used throughout most sections, but there's also "$R^2 \approx 0.22$" in the abstract and "$R^2 = 0.218$" elsewhere. I should verify this notation is consistent across the paper.

Looking at the specific instances: the abstract has both forms, the intro repeats the tilde notation, and in the results section around line 64, there's "22\%" without the tilde followed immediately by the exact R² value. Since the precise measurement comes right after, the rounded percentage doesn't need the tilde there. That's actually fine.

Now I'm ready to go through and make the 11 edits systematically. Let me double-check the multi_channel section one more time to get the exact text I need to replace for edit 10.

Looking at line 81 in results.tex, I can see the passage starts with "Current evidence cannot distinguish..." and I need to remove the middle section about NER's error-mode structure and the relaxed matching pattern, leaving just the two sentences about post-hoc mitigation attempts connected together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "95f29c19-cda8-489f-a8fa-1a30252dfdbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh4Ea9QeWL1U1VbzXD51Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 70490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
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

_source line 48_

I've read all files. Now I'll systematically scan for the issues and make edits. Let me start executing changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "97e32120-d353-4a3e-bc2f-729003b70ca4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh4Ea9QeWL1U1VbzXD51Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 70490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
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

_source line 49_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VE32tp8gZb5yJCdCU4dvKN`</summary>

```json
{
  "query": "select:TodoWrite",
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
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "77625f5c-5bcc-49af-93a1-35a9f217e8fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lh4Ea9QeWL1U1VbzXD51Y1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3450,
      "cache_read_input_tokens": 70490,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3450
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

_source line 50 · 2026-05-22T06:47:02.804Z_

<details><summary>↩ Tool result · `toolu_01VE32tp8gZb5yJCdCU4dvKN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
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
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "58d75502-1a06-4217-afb7-44ac3aca306d",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
Let me set up my todo list and start making edits systematically.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "28f10901-0693-4add-81ed-b2e1fc13d5c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns3u6Ro331MPCYshax6bvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25806,
      "cache_read_input_tokens": 73940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25806
      },
      "output_tokens": 47,
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

_source line 52_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Mz9ZficiRyzaCzFP7imgDJ`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "in_progress",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "pending",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "pending",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "pending",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "pending",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "pending",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "9de421ff-2b12-479a-a5ac-1225077bb972",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ns3u6Ro331MPCYshax6bvb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 25806,
      "cache_read_input_tokens": 73940,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25806
      },
      "output_tokens": 47,
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

_source line 53 · 2026-05-22T06:47:12.411Z_

<details><summary>↩ Tool result · `toolu_01Mz9ZficiRyzaCzFP7imgDJ`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "223494a7-284b-48bd-b4e2-5a7f4734c79b",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "in_progress",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "pending",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "pending",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 54_

Starting edits. Abstract first — consolidating redundant R²≈0.22 between findings (1) and (2).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "899f2c81-7e4f-4a1f-92d5-fc3770f4f6d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjgEBxBV27DUnp9ugUZfbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 99746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 55_

<details open><summary>🔧 Tool call — Edit · `toolu_01GdYrCeEYcxDmY4yhYnRGEf`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
  "old_string": "(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;",
  "new_string": "(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\\,=\\,1.18$ on FewRel);\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel ($R^2 \\approx 0.22$, ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "186aa032-9a95-4010-8d41-8f3c1b271f0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LjgEBxBV27DUnp9ugUZfbA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 436,
      "cache_read_input_tokens": 99746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 436
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

_source line 56 · 2026-05-22T06:47:23.614Z_

<details><summary>↩ Tool result · `toolu_01GdYrCeEYcxDmY4yhYnRGEf`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f112f715-1818-4327-8090-b45eef45b41d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/abstract.tex",
    "oldString": "(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;",
    "newString": "(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\\,=\\,1.18$ on FewRel);\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel ($R^2 \\approx 0.22$, ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;",
    "originalFile": "\\begin{abstract}\nSchema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:\n(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;\n(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;\n(3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 1,
        "oldLines": 6,
        "newStart": 1,
        "newLines": 6,
        "lines": [
          " \\begin{abstract}",
          " Schema complexity affects training-free LLM information extraction through two independent dimensions: type count drives recall decline, while inter-type confusability predicts type substitution errors. We present what is, to our knowledge, the first controlled study isolating these factors in zero-shot LLM IE across NER, RE, and event detection on four datasets. Using embedding-based confusability metrics (SCS/BCS) with controlled batch design, we find:",
          "-(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) predicts type substitution errors in RE ($R^2 \\approx 0.22$ on FewRel, VIF${}\\,=\\,1.18$); the batch-level BCS signal is not detected in NER at current statistical power;",
          "-(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel (ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;",
          "+(1)~count degradation spans all three tasks (up to $-$49\\,pp); inter-type confusability (measured by BCS) independently predicts RE type substitution errors (VIF${}\\,=\\,1.18$ on FewRel);",
          "+(2)~BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance on FewRel ($R^2 \\approx 0.22$, ecological level), replicating across three open-weight model families (8B--70B); NER batch-level signal is not detected at current power;",
          " (3)~schema decomposition fails due to merge amplification and routing failure, though oracle routing confirms the two dimensions are independently addressable.",
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

_source line 57_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Q3FMGwT68CGSmwaLXurFNh`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "in_progress",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "pending",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "pending",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "pending",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "pending",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "64336d41-1639-4e68-aa3b-a91c612528c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NKgioQnbrrwt2U5UJdwogf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 512,
      "cache_read_input_tokens": 100182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 512
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

_source line 58 · 2026-05-22T06:47:28.305Z_

<details><summary>↩ Tool result · `toolu_01Q3FMGwT68CGSmwaLXurFNh`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "a2da3d57-6aee-40dc-b9a3-4dfd19f077dc",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "in_progress",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "pending",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "pending",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "in_progress",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "pending",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 59_

Now introduction — split the 60+ word contribution 1, and remove redundant numbers from contribution 2.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0cc36f27-0f1d-4b3d-8771-0c51cf1ebb8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ak4A2EJLbcHb35CrVDQd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 100694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01T3c7v422mds9W3SnvxaBYd`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
  "new_string": "    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE on FewRel (VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design that isolates confusability from type count---a methodology not previously applied in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "b6fbb06b-7c3c-4cf9-8f25-caa95a9f9084",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ak4A2EJLbcHb35CrVDQd7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 100694,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 61 · 2026-05-22T06:47:37.764Z_

<details><summary>↩ Tool result · `toolu_01T3c7v422mds9W3SnvxaBYd`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "774a7b3c-e5fc-4838-a773-20e6cd411941",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
    "newString": "    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE on FewRel (VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design that isolates confusability from type count---a methodology not previously applied in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\looseness=-1\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \\citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.\n\n\\looseness=-1\nWhat explains this degradation? Prior decomposition strategies \\citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\n\\looseness=-1\nTo our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \\emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\citep{fewnerd-2021}, FewRel \\citep{fewrel-2018}, DocRED \\citep{docred-2019}, and MAVEN \\citep{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield four findings:\n(1)~Degradation operates along two dimensions with bounded interaction: count-related recall decline (up to $-$49\\,pp) and confusability-related type substitution, confirmed on sentence- and document-level RE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:multi_channel}).\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\\S\\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\n(3)~RE effects are consistent across schema sizes, prompt designs, and three open-weight model families (8B--70B); Gemini Flash provides partial but fragile corroboration. The NER null is not detected on three models (8B--70B; \\S\\ref{sec:bcs_controlled}).\n(4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\\S\\ref{sec:sdgd}).\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).\n    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 7,
        "newStart": 21,
        "newLines": 7,
        "lines": [
          " (4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\\S\\ref{sec:sdgd}).",
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]",
          "-    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE (on FewRel where confusability is not confounded with centrality, VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance on FewRel (ecological level)---a finding enabled by controlled batch design that isolates confusability from type count, but not previously documented in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
          "+    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE on FewRel (VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design that isolates confusability from type count---a methodology not previously applied in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
          "     \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
          "     \\item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\\S\\ref{sec:sdgd}).",
          " \\end{enumerate}",
          "\\ No newline at end of file"
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_01LF83jzxScSzWbA7vhh927D`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
  "old_string": "    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
  "new_string": "    \\item We document a task asymmetry: the RE confusability effect is confirmed as format-independent, yet NER batch-level BCS signal is not detected at current power despite significant pairwise effects---an asymmetry attributable to dispersed NER error modes and BCS range compression (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "550a1a12-6bfd-4aa3-aa4b-baaa745361f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012brqMhiandTsNViUdTpiDu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 542,
      "cache_read_input_tokens": 101098,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 542
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

_source line 63 · 2026-05-22T06:47:45.314Z_

<details><summary>↩ Tool result · `toolu_01LF83jzxScSzWbA7vhh927D`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "830f7c71-6fd8-42b4-80d8-668595606b5c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/introduction.tex",
    "oldString": "    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
    "newString": "    \\item We document a task asymmetry: the RE confusability effect is confirmed as format-independent, yet NER batch-level BCS signal is not detected at current power despite significant pairwise effects---an asymmetry attributable to dispersed NER error modes and BCS range compression (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\n\\looseness=-1\nTraining-free\\footnote{We use ``training-free'' and ``zero-shot'' interchangeably to denote prompting without parameter updates.}\\footnote{Code and data will be released upon acceptance.} LLM information extraction (prompting a large language model with a target schema and asking it to extract structured information without any task-specific fine-tuning) enables rapid deployment across new domains and ontologies. This zero-shot paradigm eliminates the need for labeled data, and is attractive for applications where annotation is expensive or schemas evolve frequently \\citep{llm4ie-survey-2024}. Yet the paradigm carries a critical limitation: performance degrades sharply as the number of candidate types in the prompt schema grows. On named entity recognition, recall drops from 0.72 with a single candidate type to a plateau of ${\\sim}$0.27 across intermediate schema sizes (22--44 types) before partial recovery at full-schema. On relation extraction, accuracy falls from 85.7\\% with one relation to 50.4\\% with 80 relations (sentence-level) and from 88.0\\% to 38.7\\% with 96 relations (document-level), near-halving or worse. This degradation is not academic: real-world ontologies routinely define 50--200+ types, which places them squarely in the regime where training-free extraction becomes unreliable.\n\n\\looseness=-1\nWhat explains this degradation? Prior decomposition strategies \\citep{uniner-2024,llm-pee-2025,parse-2025} conflate two factors: having more types to discriminate among (count) and having semantically similar types to confuse (confusability) (hereafter Dimension~1 and Dimension~2). None isolates which factor predicts the gains (\\S\\ref{sec:related_work}).\n\nThis study combines correlational analyses with quasi-experimental manipulation (BCS-controlled batches) to characterize how schema properties predict extraction accuracy.\n\nWe ask three questions. \\textbf{RQ1}: Does type confusability independently predict extraction degradation beyond the effect of type count? \\textbf{RQ2}: Through what modes do count and confusability each degrade performance? \\textbf{RQ3}: Can confusability-aware schema decomposition improve extraction quality?\n\n\\looseness=-1\nTo our knowledge, we present the first controlled study simultaneously isolating type count and inter-type confusability as independent dimensions via embedding-based metrics and stratified batch design in zero-shot LLM IE, spanning NER, RE, and event detection (ED). We quantify confusability using pairwise embedding similarity, the \\emph{Schema Confusability Score} (SCS), and its batch-level aggregation, the \\emph{Batch Confusability Score} (BCS). We evaluate on Few-NERD \\citep{fewnerd-2021}, FewRel \\citep{fewrel-2018}, DocRED \\citep{docred-2019}, and MAVEN \\citep{maven-2020} using Qwen3-32B (\\S\\ref{sec:experimental_setup}).\n\nOur experiments yield four findings:\n(1)~Degradation operates along two dimensions with bounded interaction: count-related recall decline (up to $-$49\\,pp) and confusability-related type substitution, confirmed on sentence- and document-level RE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:multi_channel}).\n(2)~Pairwise SCS predicts type confusion across NER, RE, and ED (\\S\\ref{sec:pairwise}); at batch level, BCS predicts RE accuracy independent of output format (\\S\\ref{sec:bcs_controlled}) but not NER accuracy at current statistical power; per-type aggregation is confounded by centrality on homogeneous schemas (\\S\\ref{sec:centrality_confound}).\n(3)~RE effects are consistent across schema sizes, prompt designs, and three open-weight model families (8B--70B); Gemini Flash provides partial but fragile corroboration. The NER null is not detected on three models (8B--70B; \\S\\ref{sec:bcs_controlled}).\n(4)~Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), despite oracle routing recovering substantial accuracy (\\S\\ref{sec:sdgd}).\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]\n    \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE on FewRel (VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design that isolates confusability from type count---a methodology not previously applied in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).\n    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).\n    \\item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\\S\\ref{sec:sdgd}).\n\\end{enumerate}",
    "structuredPatch": [
      {
        "oldStart": 22,
        "oldLines": 6,
        "newStart": 22,
        "newLines": 6,
        "lines": [
          " Our contributions are:",
          " \\begin{enumerate}[leftmargin=*,itemsep=2pt,topsep=2pt]",
          "     \\item We establish that type confusability, quantified by embedding similarity (SCS/BCS, building on \\citealt{llm-pee-2025}), independently predicts type substitution errors in RE on FewRel (VIF${}\\,=\\,1.18$), explaining ${\\sim}$22\\% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design that isolates confusability from type count---a methodology not previously applied in training-free LLM IE (\\S\\ref{sec:count_curves}, \\S\\ref{sec:pairwise}, \\S\\ref{sec:bcs_controlled}).",
          "-    \\item We document a task asymmetry: on FewRel, BCS explains ${\\sim}$22\\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}\\,=\\,1.18$; ecological level)---an effect confirmed as format-independent---yet NER batch-level signal is not detected at current power despite significant pairwise effects (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
          "+    \\item We document a task asymmetry: the RE confusability effect is confirmed as format-independent, yet NER batch-level BCS signal is not detected at current power despite significant pairwise effects---an asymmetry attributable to dispersed NER error modes and BCS range compression (\\S\\ref{sec:bcs_controlled}, \\S\\ref{sec:multi_channel}).",
          "     \\item We identify structural barriers to confusability-aware extraction: schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE), establishing that the decompose-then-merge paradigm faces fundamental precision--recall tradeoffs in training-free IE (\\S\\ref{sec:sdgd}).",
          " \\end{enumerate}",
          "\\ No newline at end of file"
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

_source line 64_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01DoGniEPht7adZwHRDPuEjd`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "in_progress",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "pending",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "pending",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "pending",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c3a81e8b-61d9-496b-98b6-c2d85a6c0632",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BrBqkyLkRZwxd5JHkDpU6w",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 399,
      "cache_read_input_tokens": 101640,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 399
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

_source line 65 · 2026-05-22T06:47:51.281Z_

<details><summary>↩ Tool result · `toolu_01DoGniEPht7adZwHRDPuEjd`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "90b86fed-98a3-4167-b56a-7faffe7c33d3",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "in_progress",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "pending",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "in_progress",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 66_

Related work — split long sentence in SCS novelty paragraph, replace repeated ~22% with section reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c1db9029-0930-410b-8151-b0f14c9577f7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaT695dEqL9J12nxHHDtCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 102039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 67_

<details open><summary>🔧 Tool call — Edit · `toolu_01LWCXTbXPSi8FRtZzjJRJ5Z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy.",
  "new_string": "Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d9f8d570-00f7-4e85-96f4-8cfb6f3d26d4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TaT695dEqL9J12nxHHDtCa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 102039,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 68 · 2026-05-22T06:47:57.868Z_

<details><summary>↩ Tool result · `toolu_01LWCXTbXPSi8FRtZzjJRJ5Z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "3aee7038-15b3-4770-ac4f-cc13848ad8d1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy.",
    "newString": "Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy.",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\n\\looseness=-1\nTraining-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work also exploits type embeddings for retrieval \\citep{shachar-2025-ner-retriever} and introspective confusion for example selection \\citep{reflect-learn-2026}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.\n\n\\paragraph{Schema complexity in IE.}\n\\looseness=-1\nThe most directly related work is LLM-PEE \\citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21; \\S\\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \\citep{iepile-2024}, schema definition optimization \\citep{parse-2025}, multi-agent debate \\citep{crossagentie-2025,cmas-ner-2025}, and active prompting \\citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \\citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \\citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \\emph{why} such reduction works.\n\n\\paragraph{Schema complexity in dialogue and IE.}\n\\looseness=-1\nThe Schema-Guided Dialogue dataset~\\citep{rastogi2020towards} and SGD-X~\\citep{lee2022sgd} document degradation with schema linguistic variation; \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \\citep{dubey-2018-pairwise-confusion}, correlated label noise \\citep{collier-2021-correlated-noise}, hierarchical classification \\citep{deng-2010-imagenet}, and label confusion matrices \\citep{guo-2021-label-confusion,muller2019when,peterson2019human}.\n\n\\paragraph{SCS novelty.}\n\\looseness=-1\nSCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 5,
        "newStart": 15,
        "newLines": 5,
        "lines": [
          " ",
          " \\paragraph{SCS novelty.}",
          " \\looseness=-1",
          "-SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role: SCS quantifies pairwise type confusability, and BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
          "+SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
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

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01V4YWbthrsV1Un9UvXhthXC`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
  "old_string": "The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
  "new_string": "The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain substantial cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "f031b1e4-cfee-4dc0-af15-1a50357947c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MvrQE8atxU8JFDHDgFKLmq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 351,
      "cache_read_input_tokens": 102443,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 351
      },
      "output_tokens": 72,
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

_source line 70 · 2026-05-22T06:48:04.047Z_

<details><summary>↩ Tool result · `toolu_01V4YWbthrsV1Un9UvXhthXC`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "fed140b7-2a5f-41d0-9fad-49e3aeb91ff3",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/related_work.tex",
    "oldString": "The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
    "newString": "The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain substantial cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
    "originalFile": "\\section{Related Work}\n\\label{sec:related_work}\n\n\\paragraph{Training-free LLM IE.}\n\\looseness=-1\nTraining-free LLM IE spans instruction tuning \\citep{instructuie-2023}, code-style schema encoding \\citep{knowcoder-2024,codeie-2023}, annotation-guided extraction \\citep{gollie-2024,adelie-2024}, schema-driven decoding \\citep{slot-2025,oneke-2025}, and constrained JSON decoding \\citep{json-schema-bench-2025,willard2023efficient}. NER methods include zero-shot decomposition \\citep{xie-zeroshot-ner-2023,promptner-2023}, distillation \\citep{uniner-2024}, and bidirectional encoders \\citep{gliner-2024,gliner2-2025}; RE methods include zero-shot triplet extraction \\citep{relationprompt-2022}, constrained generation \\citep{josifoski-2022-genie}, and shared embedding spaces \\citep{boylan-2025-glirel,wadhwa-re-llm-2023}. Related work also exploits type embeddings for retrieval \\citep{shachar-2025-ner-retriever} and introspective confusion for example selection \\citep{reflect-learn-2026}. These methods perform well with moderate schemas (4--20 types) but none investigates how performance degrades as schema complexity scales.\n\n\\paragraph{Schema complexity in IE.}\n\\looseness=-1\nThe most directly related work is LLM-PEE \\citep{llm-pee-2025}, which partitions large event schemas by type embedding similarity. Our work differs in three ways: (1)~we conduct controlled analysis to understand \\emph{why} extraction degrades rather than developing an engineering solution; (2)~our BCS-controlled experiments isolate count from confusability, which LLM-PEE conflates; (3)~our SDGD experiments reveal that merge amplification (not partitioning quality) is the bottleneck in decompose-then-merge pipelines. LLM-PEE's union merge suffers the same precision collapse (0.56$\\to$0.21; \\S\\ref{sec:sdgd}). In short, LLM-PEE assumes decomposition helps; we show why it should (confusability), why it does not (merge amplification), and what predicts the degradation (BCS). Other approaches address schema complexity via hard negative mining \\citep{iepile-2024}, schema definition optimization \\citep{parse-2025}, multi-agent debate \\citep{crossagentie-2025,cmas-ner-2025}, and active prompting \\citep{reflect-learn-2026}; all treat it as an engineering problem rather than isolating degradation factors. Concurrently, \\citet{chen-2026-multi-instance} show that instance count degrades LLM multi-instance processing more than context length, consistent with our count-dominant finding. \\citet{golde-2025-familiarity} quantify training--evaluation type similarity to predict zero-shot NER difficulty; our SCS instead measures within-schema inter-type confusability without assuming access to training data. Label-space reduction approaches \\citep{haystack-to-needle-2025,dlisc-2025,spt-2025} implicitly lower batch confusability---our framework explains \\emph{why} such reduction works.\n\n\\paragraph{Schema complexity in dialogue and IE.}\n\\looseness=-1\nThe Schema-Guided Dialogue dataset~\\citep{rastogi2020towards} and SGD-X~\\citep{lee2022sgd} document degradation with schema linguistic variation; \\citet{li2023evaluating} observe count-dependent degradation in ChatGPT IE. The relationship between label similarity and confusion has precedent in visual recognition \\citep{dubey-2018-pairwise-confusion}, correlated label noise \\citep{collier-2021-correlated-noise}, hierarchical classification \\citep{deng-2010-imagenet}, and label confusion matrices \\citep{guo-2021-label-confusion,muller2019when,peterson2019human}.\n\n\\paragraph{SCS novelty.}\n\\looseness=-1\nSCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).\n\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 5,
        "newStart": 15,
        "newLines": 5,
        "lines": [
          " ",
          " \\paragraph{SCS novelty.}",
          " \\looseness=-1",
          "-SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain ${\\sim}$22\\% of cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
          "+SCS inherits the embedding-similarity criterion from LLM-PEE \\citep{llm-pee-2025}. Unlike LLM-PEE, which uses embedding similarity to partition schemas for improved extraction, our SCS/BCS metrics serve an analytical role. SCS quantifies pairwise type confusability; BCS averages all pairwise SCS values within a batch to predict batch-level accuracy. The metric is a means; the empirical findings are the contribution, enabled by a controlled experimental methodology that previous work lacked---BCS-controlled batches that isolate confusability from count. The use of embedding distance for type discrimination has parallels in metric learning \\citep{snell2017prototypical} and zero-shot classification \\citep{yin-2019-zero-shot-bench}. The modest pairwise $r^2$ (1.3--1.7\\%) compounds at the ecological batch level to explain substantial cross-batch RE variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
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

_source line 71_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01X4WuFYdXfi7Tyebi7pWnjS`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "completed",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "in_progress",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "pending",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "pending",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c932fda3-02d7-4525-b680-ae8a6c844df5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JL4SRCjMM6QWniLxw2WiSj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 102794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
      },
      "output_tokens": 72,
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

_source line 72 · 2026-05-22T06:48:08.786Z_

<details><summary>↩ Tool result · `toolu_01X4WuFYdXfi7Tyebi7pWnjS`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "3aa1bd57-97d9-4bab-83f0-9dd0e1e616cb",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "in_progress",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "pending",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "in_progress",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 73_

Experimental setup — 4 edits: remove vague phrase, split FewRel sentence, split DocRED sentence, passive→active for extreme batches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "9a0a8f7b-4b67-4aca-8009-7d327c6adcce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEe4J8zPG6xSAsPBPAMS6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 103105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
      },
      "output_tokens": 5,
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

_source line 74_

<details open><summary>🔧 Tool call — Edit · `toolu_01PAg74TJr6RMzrxUJv3vHas`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "The dataset spans diverse domains and is suitable for cross-domain evaluation.",
  "new_string": "The dataset spans diverse domains."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0aa5b8f5-d66e-460a-9919-7ebeb8e55896",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UEe4J8zPG6xSAsPBPAMS6Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 103105,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
      },
      "output_tokens": 5,
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

_source line 75 · 2026-05-22T06:48:13.373Z_

<details><summary>↩ Tool result · `toolu_01PAg74TJr6RMzrxUJv3vHas`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "ecc2b756-12d4-4386-8493-7b092c1c2cf0",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "The dataset spans diverse domains and is suitable for cross-domain evaluation.",
    "newString": "The dataset spans diverse domains.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \\citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \\citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \\citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with autoregressive anisotropy \\citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}).\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 batch-composition seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \\texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\looseness=-1\nWe use Qwen3-32B-FP8 \\citep{qwen3-2025} served via vLLM v0.20.2 \\citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\citep{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 7,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " \\label{sec:datasets}",
          " ",
          " \\paragraph{Few-NERD (NER).}",
          "-Few-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains and is suitable for cross-domain evaluation. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.",
          "+Few-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.",
          " ",
          " \\paragraph{FewRel (RE).}",
          " FewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination."
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

_source line 76_

<details open><summary>🔧 Tool call — Edit · `toolu_01RwrdSDoFxjcYmjkYJr9bZN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation).",
  "new_string": "Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "eeef02b2-ba8c-469c-a93e-58b71e3e7cfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017L6Uk4fA4MXW4tiKn8RVWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 254,
      "cache_read_input_tokens": 103509,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 254
      },
      "output_tokens": 72,
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

_source line 77 · 2026-05-22T06:48:19.627Z_

<details><summary>↩ Tool result · `toolu_01RwrdSDoFxjcYmjkYJr9bZN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "e7769485-1620-45ec-99b5-07235ea2f07f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation).",
    "newString": "Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation).",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \\citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \\citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \\citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with autoregressive anisotropy \\citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}).\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 batch-composition seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \\texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\looseness=-1\nWe use Qwen3-32B-FP8 \\citep{qwen3-2025} served via vLLM v0.20.2 \\citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\citep{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " Few-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.",
          " ",
          " \\paragraph{FewRel (RE).}",
          "-FewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments, and sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.",
          "+FewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.",
          " ",
          " \\paragraph{DocRED (Document-level RE).}",
          " DocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning."
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

_source line 78_

<details open><summary>🔧 Tool call — Edit · `toolu_014euVP9gV2GKxWsQbDZjPUZ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation.",
  "new_string": "We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "a06491dc-b2e5-4787-8250-7afae4dcf7ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0165yRycroAxHVYbK7GtjWRD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 321,
      "cache_read_input_tokens": 103763,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 321
      },
      "output_tokens": 72,
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

_source line 79 · 2026-05-22T06:48:24.659Z_

<details><summary>↩ Tool result · `toolu_014euVP9gV2GKxWsQbDZjPUZ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "43228c14-23a9-4cb0-aa11-377265a2befd",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation.",
    "newString": "We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \\citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \\citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \\citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with autoregressive anisotropy \\citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}).\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 batch-composition seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \\texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\looseness=-1\nWe use Qwen3-32B-FP8 \\citep{qwen3-2025} served via vLLM v0.20.2 \\citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\citep{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 7,
        "newStart": 13,
        "newLines": 7,
        "lines": [
          " FewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.",
          " ",
          " \\paragraph{DocRED (Document-level RE).}",
          "-DocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set and formulate the task identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.",
          "+DocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.",
          " ",
          " \\paragraph{MAVEN (ED).}",
          " MAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound})."
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_01T9HS7D7M9i3bjqXeSgT5B4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
  "old_string": "Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity.",
  "new_string": "We construct extreme batches via greedy search over the pairwise SCS matrix. The low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "bbbf6c08-f677-417c-a796-b4b0a2c4db3b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RMNTXigzxiQR9TBRxU7g43",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 104084,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 72,
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

_source line 81 · 2026-05-22T06:48:30.301Z_

<details><summary>↩ Tool result · `toolu_01T9HS7D7M9i3bjqXeSgT5B4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "3ee8d240-a8f9-4805-b2f1-3c36a3e347dc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/experimental_setup.tex",
    "oldString": "Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity.",
    "newString": "We construct extreme batches via greedy search over the pairwise SCS matrix. The low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity.",
    "originalFile": "\\section{Experimental Setup}\n\\label{sec:experimental_setup}\n\nWe evaluate how prompt schema size and inter-type confusability affect zero-shot LLM extraction across three information extraction tasks and four datasets: named entity recognition (NER), sentence-level relation extraction (RE), document-level RE, and event detection (ED).\n\n\\subsection{Tasks and Datasets}\n\\label{sec:datasets}\n\n\\paragraph{Few-NERD (NER).}\nFew-NERD \\citep{fewnerd-2021} provides 66 fine-grained entity types organized into 8 coarse categories (person, location, organization, building, art, product, event, other). The dataset spans diverse domains. We sample 1{,}000 instances uniformly from the test set; type frequency follows the natural long-tail distribution of Few-NERD. Evaluation uses token-level text matching. Pairwise analysis covers 1{,}953 type pairs with non-zero co-occurrence out of $\\binom{66}{2}=2{,}145$ possible pairs.\n\n\\paragraph{FewRel (RE).}\nFewRel \\citep{fewrel-2018} contains 80 relation types sourced from Wikidata. Since the validation split covers only 16 relations, we combine the training and validation splits to obtain the full 80-relation pool required for schema-scale experiments. We sample 1{,}000 balanced instances (12--13 per relation type, stratified to ensure equal representation). A held-out validation confirms SCS--confusion generalization across the split boundary (Appendix~\\ref{app:scs-heldout-validation}). Each instance provides a sentence with marked head and tail entities; the task is to classify the relation. FewRel's balanced design (700 instances per relation type) eliminates type frequency as a potential confound; this balance makes it the primary dataset for BCS analysis. Contamination analysis (Appendix~\\ref{app:split-origin}) shows extraction difficulty correlates inversely with training-set prevalence, and BCS effects are unchanged when controlling for contamination.\n\n\\paragraph{DocRED (Document-level RE).}\nDocRED \\citep{docred-2019} contains 96 relation types sourced from Wikidata, evaluated at the document level where entity pairs may span multiple sentences. We sample 1{,}000 instances balanced across 96 relation types ($\\sim$10 per type) from the DocRED development set. The task is formulated identically to FewRel: given a document with marked head and tail entities, classify the relation. DocRED extends the RE evaluation to a larger schema (96 vs.\\ 80 types) and document-level context, testing whether confusability effects persist under longer input contexts and cross-sentence reasoning.\n\n\\paragraph{MAVEN (ED).}\nMAVEN \\citep{maven-2020} defines 168 event types derived from the FrameNet ontology; all types belong to a single ontology (FrameNet), so this is a same-domain schema. We use the validation set (8{,}042 sentences containing 18{,}904 event mentions) for evaluation, as test set labels are not publicly available. The task requires both trigger identification and event type classification. MAVEN serves a supplementary role because its same-domain schema produces centrality confounds at the batch level (\\S\\ref{sec:centrality_confound}).\n\nTable~\\ref{tab:datasets} summarizes the dataset statistics, including the Schema Confusability Score (SCS) ranges defined in \\S\\ref{sec:scs}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrlll}\n\\toprule\n\\textbf{Dataset} & \\textbf{Task} & \\textbf{\\# Types} & \\textbf{\\# Eval Units} & \\textbf{Domain} & \\textbf{BCS Range} & \\textbf{Embedding} \\\\\n\\midrule\nFew-NERD & NER & 66 & 1{,}000 & Cross & 0.77--0.93 & Qwen3-32B \\\\\nFewRel & RE (sent.) & 80 & 1{,}000 & Cross & 0.42--0.97 & MiniLM \\\\\nDocRED & RE (doc.) & 96 & 1{,}000 & Cross & 0.53--0.73 & MiniLM \\\\\nMAVEN & ED & 168 & 18{,}904\\rlap{$^\\dagger$} & Same & 0.87--0.97 & MiniLM \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Dataset statistics. BCS Range: min--max over count-curve batches. Embedding: model used for SCS/BCS; ranges are not comparable across embedding models. $^\\dagger$Trigger mentions across 8{,}042 sentences.}\n\\label{tab:datasets}\n\\end{table}\n\n\\subsection{Schema Confusability Score (SCS)}\n\\label{sec:scs}\n\n\\looseness=-1\nWe define the Schema Confusability Score (SCS) to quantify semantic overlap between types in a schema. Given a type $t$ with name string $\\text{name}(t)$, an embedding function $\\text{embed}(\\cdot)$ maps the type name to a vector representation. The \\textbf{pairwise SCS} between types $t_i$ and $t_j$ is:\n{\\small\n\\[\n\\text{SCS}(t_i, t_j) = \\cos\\bigl(\\text{embed}(\\text{name}(t_i)),\\; \\text{embed}(\\text{name}(t_j))\\bigr)\n\\]\n}\n\nFor a batch of types $B = \\{t_1, \\ldots, t_k\\}$, the \\textbf{Batch Confusability Score (BCS)} aggregates all pairwise similarities:\n\\[\n\\text{BCS}(B) = \\frac{1}{\\binom{k}{2}} \\sum_{i < j,\\; t_i, t_j \\in B} \\text{SCS}(t_i, t_j)\n\\]\n\nWe use two embeddings to provide complementary perspectives: Qwen3 captures the extraction model's own type representations (self-similarity), while MiniLM provides an independent general-purpose baseline. Cross-embedding consistency holds on all datasets (Appendix~\\ref{sec:appendix_bcs_sensitivity}); MiniLM consistently yields equal or stronger correlations, which confirms that Qwen3-based estimates are conservative. We compute SCS with: (1)~Qwen3-32B \\citep{qwen3-2025} hidden-state representations (5{,}120-d) and (2)~all-MiniLM-L6-v2 \\citep{minilm-2020,sentence-bert-2019}, a 384-d sentence encoder. Few-NERD uses Qwen3 because its fine-grained same-category pairs (e.g., ``person-artist'' vs.\\ ``person-actor'') require the higher-dimensional space. MiniLM is the primary BCS embedding because sentence-transformers are trained for semantic similarity \\citep{sentence-bert-2019}; Qwen3 causal-LM states show compressed BCS range (std${}\\,=\\,0.034$ vs.\\ MiniLM std${}\\,=\\,0.081$), consistent with autoregressive anisotropy \\citep{ethayarajh-contextual-2019}. Name-only SCS yields equivalent predictive accuracy to name+definition ($\\Delta r$: $-0.023$ to $+0.035$; Appendix~\\ref{app:scs-ablation}).\n\n\\paragraph{SCS as a lightweight proxy.}\n\\label{sec:scs-validation}\nSCS is a pre-hoc proxy computable without running extraction. Pairwise SCS correlates with observed type confusion (Few-NERD $r = 0.112$, FewRel $r = 0.187$, both $p < 0.001$; Table~\\ref{tab:pairwise}), though context, frequency, and definition quality also contribute (\\S\\ref{sec:pairwise}). SCS does not capture context-dependent disambiguation or mention-level ambiguity; these factors contribute to the residual variance in pairwise analysis.\n\n\\begin{figure*}[t]\n\\centering\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_count_curves.pdf}\n\\end{minipage}\n\\hfill\n\\begin{minipage}[t]{0.48\\textwidth}\n\\centering\n\\includegraphics[width=\\linewidth]{../../figures/paper/fig_bcs_scaling.pdf}\n\\end{minipage}\n\\caption{\\textbf{(a)} Count-degradation curves. Error bars: $\\pm 1$\\,SD across 3 batch-composition seeds $\\times$ 25 batches. RE declines monotonically; NER shows a U-shape. Rightmost points are full-schema (negligible sampling variance). \\textbf{(b)} BCS-controlled FewRel accuracy. Slopes are consistent across the independent and within-pool 16-relation conditions ($p = 0.60$); wider BCS range at 80 relations produces larger gaps.}\n\\label{fig:main_results}\n\\end{figure*}\n\n\\subsection{Experimental Design}\n\\label{sec:exp_design}\n\nWe conduct two complementary experimental paradigms.\n\n\\paragraph{Experiment 1: Count Curves.}\nWe vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.\n\n\\paragraph{Experiment 2: BCS-Controlled.}\nWe fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).\n\n\\subsection{Evaluation Metrics}\n\\label{sec:metrics}\n\n\\textbf{NER}: text-match F1, where a prediction is correct if the exact text string matches after lowercasing and whitespace normalization, \\emph{and} the type matches; partial spans count as incorrect. \\textbf{RE}: accuracy (exact match of predicted relation label to gold). Each batch evaluates only samples whose gold relation is included in the candidate set; out-of-schema samples are excluded before inference. The prompt allows a \\texttt{none} response for cases where the model judges no candidate applies; any such prediction is scored as incorrect since the gold is always among the candidates by construction. \\textbf{ED}: relaxed F1, where any token overlap between predicted and gold trigger spans, with correct event type.\n\n\n\\subsection{Model and Inference}\n\\label{sec:model}\n\n\\looseness=-1\nWe use Qwen3-32B-FP8 \\citep{qwen3-2025} served via vLLM v0.20.2 \\citep{vllm-2023} on a single NVIDIA RTX PRO 6000 GPU (96\\,GB) with greedy decoding (temperature${}\\,=\\,0$, seed 42). Two NER/ED prompt versions are evaluated: v1 requests character offsets (evaluated via text matching); v2 adds format constraints that double precision with minimal recall loss. RE uses a single prompt version throughout. Both versions produce consistent degradation patterns; we report both where applicable to quantify formatting sensitivity \\citep{sclar-sensitivity-2024} (templates in Appendix~\\ref{sec:appendix_prompts}). Cross-model validation uses Meta-Llama-3.1-70B-Instruct (FP8) and Meta-Llama-3.1-8B-Instruct \\citep{llama3-2024}. All experiments use single-seed evaluation with greedy decoding, which substantially reduces model-level randomness (residual SD = 0.88\\,pp at count 80 under greedy decoding, likely attributable to FP8 quantization non-determinism); bootstrap CIs capture the remaining sampling variance from batch composition. Pair-level CIs use percentile bootstrap ($B{=}10{,}000$); batch-level CIs use $B{=}1{,}000$.\n",
    "structuredPatch": [
      {
        "oldStart": 84,
        "oldLines": 7,
        "newStart": 84,
        "newLines": 7,
        "lines": [
          " We vary the number of types presented in the prompt schema to measure performance as a function of schema size. For each count level, we sample 25 random type batches for Few-NERD and FewRel (5 for DocRED and MAVEN)\\footnote{DocRED and MAVEN use fewer batches due to higher per-batch evaluation cost (document-level RE and 8{,}042 sentences, respectively).} and evaluate the same 1{,}000 test samples across all batches. At count${}=1$, every type is evaluated individually as a solo baseline. The remaining count levels follow natural partition points in each schema's type hierarchy rather than uniform spacing: \\{2, 6, 12, 22, 44, 66\\} for Few-NERD, \\{4, 8, 16, 32, 40, 64, 80\\} for FewRel, \\{4, 8, 16, 32, 64, 96\\} for DocRED, and \\{6, 12, 22, 44, 64\\} for MAVEN.",
          " ",
          " \\paragraph{Experiment 2: BCS-Controlled.}",
          "-We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).",
          "+We fix type count and vary BCS to isolate confusability from schema size. For each count level, we construct one low-BCS batch, one high-BCS batch, and 25 random batches (27 total). We construct extreme batches via greedy search over the pairwise SCS matrix. The low-BCS batch starts from the least-similar type pair and iteratively adds the type with lowest maximum similarity to already-selected types; the high-BCS batch mirrors this with maximum similarity. We evaluate on Few-NERD (count$\\,\\in\\{6, 12\\}$), FewRel (count$\\,\\in\\{8, 16\\}$, both 16-relation (pilot) and 80-relation pools), and DocRED (count$\\,\\in\\{16, 32\\}$). Within-pool 16-relation subsets from the 80-relation pool isolate confusability from pool composition. MAVEN results are reported separately due to a centrality confound (\\S\\ref{sec:centrality_confound}).",
          " ",
          " \\subsection{Evaluation Metrics}",
          " \\label{sec:metrics}"
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

_source line 82_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01ThprBpq92HpLko33ShQw7J`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "completed",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "completed",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "in_progress",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "pending",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "87dd961b-ddbd-4406-a2c3-f49acecaadcc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HxaZASeYb365PL4skLzAsQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 318,
      "cache_read_input_tokens": 104402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 318
      },
      "output_tokens": 72,
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

_source line 83 · 2026-05-22T06:48:35.439Z_

<details><summary>↩ Tool result · `toolu_01ThprBpq92HpLko33ShQw7J`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "dcefbe74-91e8-4e8a-a504-2cd59517f35b",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "in_progress",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "pending",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "in_progress",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 84_

Results — 3 edits: replace repeated ~22% in §4.2, remove redundant NER error-mode restatement in §4.5, split long TOST sentence.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "57d58074-1682-43c9-8a95-41c45385e472",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1U3ah4DDYeJviWiu7JADY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 104720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
      },
      "output_tokens": 4,
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

_source line 85_

<details open><summary>🔧 Tool call — Edit · `toolu_0178FpAFU1RFoFvkFkyRt1K4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
  "new_string": "While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (\\S\\ref{sec:bcs_controlled})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "9468aaa2-6456-49f1-a242-c11fce1de86a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K1U3ah4DDYeJviWiu7JADY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 104720,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
      },
      "output_tokens": 4,
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

_source line 86 · 2026-05-22T06:48:41.616Z_

<details><summary>↩ Tool result · `toolu_0178FpAFU1RFoFvkFkyRt1K4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "fb6eff3b-c1ea-4997-ac47-d5e31206190c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}).",
    "newString": "While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (\\S\\ref{sec:bcs_controlled}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nAll experiments use Qwen3-32B and the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\looseness=-1\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\n\\looseness=-1\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\n\\looseness=-1\nThe remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}, Table~\\ref{tab:partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. Given VIF${}\\,=\\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\looseness=-1\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).\n\n\\looseness=-1\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.\n\n\\subsection{Centrality as a Potential Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\\looseness=-1\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation ($\\rho = +0.184\\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \\citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.",
    "structuredPatch": [
      {
        "oldStart": 34,
        "oldLines": 7,
        "newStart": 34,
        "newLines": 7,
        "lines": [
          " The correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).",
          " ",
          " \\looseness=-1",
          "-The remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal: batch-level BCS explains ${\\sim}$22\\% of RE accuracy variance on FewRel (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.",
          "+The remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.",
          " ",
          " \\begin{figure*}[t]",
          " \\centering"
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

_source line 87_

<details open><summary>🔧 Tool call — Edit · `toolu_0177Fo6gStQ4jZcPoRJvE2eL`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts",
  "new_string": "Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0ac2f91f-08e4-4d68-ab62-95fa213a7a4d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N4cQFGSZ7LV74eHoEVaagm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 341,
      "cache_read_input_tokens": 105124,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 341
      },
      "output_tokens": 72,
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

_source line 88 · 2026-05-22T06:48:48.654Z_

<details><summary>↩ Tool result · `toolu_0177Fo6gStQ4jZcPoRJvE2eL`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "5f760eb2-712b-4fbe-b0c2-abb805ec37f4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts",
    "newString": "Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nAll experiments use Qwen3-32B and the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\looseness=-1\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\n\\looseness=-1\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\n\\looseness=-1\nThe remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}, Table~\\ref{tab:partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. Given VIF${}\\,=\\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\looseness=-1\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).\n\n\\looseness=-1\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.\n\n\\subsection{Centrality as a Potential Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\\looseness=-1\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation ($\\rho = +0.184\\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \\citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).",
          " ",
          " \\looseness=-1",
          "-These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix~\\ref{app:relaxed-matching}). Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.",
          "+These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.",
          " ",
          " \\subsection{Centrality as a Potential Confound on Homogeneous Schemas}",
          " \\label{sec:centrality_confound}"
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

_source line 89_

<details open><summary>🔧 Tool call — Edit · `toolu_01NTTSw6pwhQB78MWCzf5K7G`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
  "old_string": "Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
  "new_string": "Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference. The logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "1a35b3bc-1a8d-4a52-a35f-d580f8bbdacd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Sm5NKJmEa8JjHjfEugVnX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 334,
      "cache_read_input_tokens": 105465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 334
      },
      "output_tokens": 72,
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

_source line 90 · 2026-05-22T06:48:55.759Z_

<details><summary>↩ Tool result · `toolu_01NTTSw6pwhQB78MWCzf5K7G`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "cfb89aff-0524-4ddc-8f59-64cfa4e04289",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper/results.tex",
    "oldString": "Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
    "newString": "Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference. The logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nAll experiments use Qwen3-32B and the v1 prompt (\\S\\ref{sec:model}; Appendix~\\ref{sec:appendix_prompts}) unless noted; cross-model validation covers Dimensions~1--2, while secondary analyses (error taxonomy, DocRED $R^2$, TOST) remain single-model.\n\n\\subsection{Count-Degradation Curves}\n\\label{sec:count_curves}\n\n\\looseness=-1\nFigure~\\ref{fig:main_results}a shows RE accuracy declines monotonically with schema size (0.86$\\to$0.50 for FewRel). NER recall declines through intermediate counts (0.51$\\to$0.27, plateauing across counts 22--44) before partial recovery at full-schema (0.41), where eliminating type-filtering overhead restores extraction performance. DocRED replicates the monotonic RE pattern (88.0\\%$\\to$38.7\\%, $-$56\\%; Appendix). MAVEN exhibits a reversed trend attributable to centrality confounding (\\S\\ref{sec:centrality_confound}). The effect replicates on Llama-3.1-8B-Instruct ($-$43\\,pp on Few-NERD; per-batch $r = 0.725$; Table~\\ref{tab:cross_model}). The pattern is stable across three seeds (max $\\Delta = 10.7$\\,pp, within 1\\,SD; intra-batch variance exceeds inter-seed variance by ${>}$5$\\times$; Appendix~\\ref{app:variance-decomposition}). Formal trend analysis confirms monotonic RE decline (Jonckheere-Terpstra $J = 109{,}707$, $p < 0.001$). Count decline replicates on LLaMA-70B with comparable magnitude and on Gemini Flash (Appendix~\\ref{sec:appendix_cross_model_gemini}). Count curves establish trend direction; magnitude estimation relies on the higher-powered BCS-controlled experiments (\\S\\ref{sec:bcs_controlled}).\n\n\\subsection{Pairwise Confusability and Type Confusion}\n\\label{sec:pairwise}\n\nWe test whether pairwise SCS predicts type-level confusion rates. For each type pair $(t_i, t_j)$, we compute the confusion rate (the fraction of $t_i$ gold instances misclassified as $t_j$) and correlate it with $\\text{SCS}(t_i, t_j)$. Table~\\ref{tab:pairwise} reports Pearson correlations with bootstrap 95\\% CIs.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{llrrrrr}\n\\toprule\n\\textbf{Dataset} & \\textbf{Embed.} & \\textbf{$n$ pairs} & \\textbf{$r$} & \\textbf{$r^2$} & \\textbf{95\\% CI} & \\textbf{$p$} \\\\\n\\midrule\nFew-NERD & Qwen3 & 1{,}953 & 0.112 & 0.013 & {[}0.076, 0.156{]} & ${<}\\,0.001$ \\\\\nMAVEN & MiniLM & 11{,}026 & 0.129 & 0.017 & {[}0.104, 0.156{]} & ${<}\\,0.001$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Pairwise SCS--confusion correlation. Confusion rate is bidirectional $C(t_i{\\to}t_j) + C(t_j{\\to}t_i)$ divided by gold frequency sum; CIs are percentile bootstrap ($B{=}10{,}000$). FewRel ($r = 0.187$; \\S\\ref{sec:scs-validation}) excluded (per-instance RE format). Type-level cluster bootstrap CIs exclude zero (Few-NERD [0.069, 0.219]; MAVEN [0.081, 0.185]).}\n\\label{tab:pairwise}\n\\end{table}\n\n\\looseness=-1\nThe correlations are statistically significant but modest: $r^2 \\approx 1.3\\text{--}1.7\\%$. Type-level cluster bootstrap yields wider but still significant CIs (Few-NERD: [0.069, 0.219]; MAVEN: [0.081, 0.185]; $B = 10{,}000$). Spearman correlations corroborate: $\\rho = 0.144\\text{--}0.227$ across all pairs, strengthening to $\\rho = 0.27\\text{--}0.31$ among pairs with nonzero confusion (though conditioning on the dependent variable may inflate this).\n\n\\looseness=-1\nThe remaining variance reflects entity frequency, prompt position \\citep{lost-in-middle-2024}, mention ambiguity, and definition quality. While pairwise $r^2$ is modest, correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (\\S\\ref{sec:bcs_controlled}). The independent MiniLM embedding yields a \\emph{stronger} SCS--confusion correlation on Few-NERD ($r = 0.172$ vs.\\ Qwen3 $r = 0.138$; Appendix), indicating that shared-representation bias is conservative. SCS outperforms simpler baselines (Levenshtein, WordNet Wu-Palmer, same-parent; Appendix~\\ref{app:scs-baselines}). Appendix~\\ref{app:error-analysis} lists the most confusable type pairs with concrete examples.\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{../../figures/paper/fig_error_taxonomy.pdf}\n\\caption{Error taxonomy decomposition (Few-NERD NER and FewRel RE). IntraSub scales monotonically with BCS across all evaluated datasets ($\\rho = 0.84\\text{--}1.0$; Table~\\ref{tab:error_taxonomy} includes DocRED). RE missed rates remain flat (10--16\\%), but NER missed rates are substantially higher (43--65\\%) and non-monotonic.}\n\\label{fig:error_taxonomy}\n\\end{figure*}\n\n\\subsection{BCS-Controlled Experiments}\n\\label{sec:bcs_controlled}\n\n\\looseness=-1\nOn FewRel, BCS explains ${\\sim}$22\\% of cross-batch RE accuracy variance; confusability is a substantial predictor alongside count. We fix type count and vary BCS to isolate this effect. FewRel's balanced design (700 instances per type) eliminates type frequency as a confound;\\footnote{Partial correlation controlling for degree centrality: FewRel $r_{\\text{partial}} = -0.537$ ($p < 0.001$, VIF${}\\,=\\,1.18$). DocRED partial correlation ($r_{\\text{partial}} = -0.348$, $p < 0.001$) is reported for completeness, but VIF${}\\,=\\,50.9$ (BCS--centrality $r = 0.99$) renders the estimate unstable; the clean evidence for BCS's independent contribution comes from FewRel (Appendix~\\ref{sec:appendix_partial_corr}, Table~\\ref{tab:partial_corr}).} the within-pool analysis (\\S\\ref{sec:within_pool}) controls for pool composition.\n\nIn BCS-controlled FewRel subsets, the high-BCS quartile shows $\\Delta=-5.3$\\,pp lower accuracy than low-BCS (quartile comparison on 100 random batches; based on a single extreme batch per BCS level at 16-rel scale; full data in Appendix~\\ref{app:bcs-controlled-table}). At 80 relations, extreme-batch construction amplifies this to $-$31.2\\,pp (95\\% CI [17.7, 42.7]), stable across count levels. An intermediate count${}\\,=\\,40$ evaluation (40-relation subsets sampled from the 80-relation pool) yields consistent gaps ($-$33.3\\,pp at count 8, $-$31.8\\,pp at count 16) and confirms monotonic decline.\n\n\\paragraph{Document-level RE (DocRED).}\nThe effect replicates on DocRED's 96-relation schema ($n{=}55$ per count level;\\footnote{DocRED uses 5 batches per count level (vs.\\ 25 for FewRel) due to higher per-batch evaluation cost; CIs are correspondingly wider.}): extreme-BCS gap $-$25.0\\,pp at count 16 ($\\rho = -0.762$, 95\\% CI [$-$0.88, $-$0.58]) and $-$15.7\\,pp at count 32 ($\\rho = -0.693$, 95\\% CI [$-$0.83, $-$0.50]; both $p < 0.001$). Pooled across counts, $R^2 = 0.578$ ($n = 110$; 95\\% CI [0.46, 0.68]; per-count: $R^2 = 0.653$ at count 16, $0.614$ at count 32). The substantially higher $R^2$ relative to FewRel (0.218) largely reflects BCS--centrality collinearity (VIF${}\\,=\\,50.9$): semipartial $R^2_{\\text{BCS}} = 0.056$ after partialing degree centrality, confirming that 90\\% of the explained variance is shared with centrality. Given VIF${}\\,=\\,50.9$, the partial correlation standard errors are inflated approximately 7-fold; this result serves as directional evidence that the BCS--accuracy relationship extends beyond FewRel's schema, not as independent quantitative support. Ridge regression confirms the negative direction under regularization (Appendix~\\ref{sec:appendix_partial_corr}). The clean evidence for BCS's independent contribution comes from FewRel (semipartial $R^2 = 0.273$, VIF${}\\,=\\,1.18$).\n\n\\paragraph{Within-pool controlled comparison.}\n\\label{sec:within_pool}\nWithin-pool analysis confirms slope consistency across pools (permutation $p \\approx 0.60$; Appendix~\\ref{app:within-pool-method}). The 80-relation extreme-batch gap (\\S\\ref{sec:bcs_controlled}) reflects wider BCS range, not stronger per-unit sensitivity.\n\n\\paragraph{Practical magnitude.}\n\\label{sec:practical_magnitude}\n\\looseness=-1\nDirect regression on 100 random 16-type batches from the 80-relation pool shows BCS explains 22\\% of cross-batch accuracy variance ($R^2 = 0.218$, $p < 0.001$). DocRED pooled $R^2 = 0.578$ ($n = 110$; semipartial $R^2_{\\text{BCS}} = 0.056$ after centrality; Appendix~\\ref{sec:appendix_partial_corr}). The typical BCS span (IQR = 0.054) yields an expected accuracy gap of 2.2\\,pp (95\\% CI [0.4, 4.0]). Quartile comparison confirms: bottom-quartile BCS batches average 82.8\\% vs.\\ 78.9\\% for top-quartile ($\\Delta = 3.9$\\,pp). The amplification from pairwise $r^2 \\approx 1.5\\%$ to batch-level $R^2 \\approx 22\\%$ is not a statistical artifact but the operative mechanism. Correlated confusable-type interactions compound within shared prompts \\citep{robinson-1950-ecological,baan-2023-ecological}, producing the batch-level signal that makes BCS practically predictive (${\\sim}3\\times$ amplification illustrated by Monte Carlo simulation; Appendix~\\ref{app:aggregation-sim}).\n\n\\paragraph{Cross-model validation.}\n\\looseness=-1\nThe effect replicates on Meta-Llama-3.1-8B-Instruct: extreme-BCS gaps of $-$27.1\\,pp (count 8) and $-$23.9\\,pp (count 16), reaching 77--87\\% of Qwen3-32B's gap (Table~\\ref{tab:cross_model_bcs}). All three open-weight families (Qwen3-32B, LLaMA-70B, LLaMA-8B) show consistent negative BCS slopes on FewRel RE. Gemini 2.5 Flash provides partial but fragile corroboration ($\\Delta = -17.6$\\,pp at count 8) with substantial leverage sensitivity (leave-one-out Pearson: $r = -0.80 \\to -0.42$, $p = 0.22$; Spearman: $\\rho = -0.40 \\to -0.18$, $p = 0.64$; Appendix~\\ref{sec:appendix_cross_model_gemini}). LLaMA-8B and LLaMA-70B both show no NER BCS signal ($r{=}{-}0.13$, $p{=}0.36$ for 70B), confirming the task asymmetry across three models (Table~\\ref{tab:cross_model_ner_null}).\n\n\\paragraph{Prompt sensitivity.}\n\\looseness=-1\nUnder the v2 prompt, the extreme-batch BCS gap is $-$25.5\\,pp ($r = -0.919$, $p < 0.001$; $n{=}25$), modestly attenuated from v1 but highly significant. NER shows no batch-level BCS--F1 correlation under either prompt ($r \\approx 0$, $n = 450$; \\S\\ref{sec:multi_channel}). The effect holds across four structurally distinct prompt variants at count 32 (all $r \\leq -0.47$; Appendix~\\ref{sec:appendix_prompt_variants}), ruling out prompt design as the source. Few-shot demonstrations widen the confusability gap (+4.3\\,pp under 5-shot), though this finding is limited to a single dataset and count level (Appendix~\\ref{sec:appendix_fewshot_bcs}).\n\n\\subsection{Multi-Dimensional Degradation}\n\\label{sec:multi_channel}\n\n\\looseness=-1\nError taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).\n\n\\looseness=-1\nThese results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.\n\n\\subsection{Centrality as a Potential Confound on Homogeneous Schemas}\n\\label{sec:centrality_confound}\n\\looseness=-1\nPer-type analysis on MAVEN reveals an anomalous \\emph{positive} BCS--F1 correlation ($\\rho = +0.184\\text{--}0.208$, $p < 0.03$): FrameNet-derived types cluster tightly \\citep{cai-isotropy-clusters-2021}, conflating confusability with centrality. Controlling for log frequency and degree centrality, the correlation vanishes ($p > 0.2$; Appendix~\\ref{sec:appendix_residualized_bcs}), though the pairwise SCS signal remains intact ($r = 0.129$, $p < 0.001$). Few-NERD's cross-domain schema shows the expected negative direction ($\\rho = -0.293$, $p = 0.02$); mean BCS is reliable only for cross-domain schemas.",
    "structuredPatch": [
      {
        "oldStart": 78,
        "oldLines": 7,
        "newStart": 78,
        "newLines": 7,
        "lines": [
          " Error taxonomy decomposition (Table~\\ref{tab:error_taxonomy} and Figure~\\ref{fig:error_taxonomy}) shows intra-batch substitution (IntraSub) scales monotonically with BCS across all three datasets: $\\rho = 1.0$ ($p < 0.001$) for Few-NERD NER, $\\rho = 0.954$ ($p < 0.001$) for FewRel sentence-level RE, and $\\rho = 0.843$ ($p < 10^{-30}$, $n = 110$) for DocRED document-level RE. The slightly lower DocRED correlation reflects additional noise from document-level context and cross-sentence reasoning. In NER, missed rates are higher (43--65\\%) and non-monotonic; confusable types impair entity detection itself. In DocRED, IntraSub accounts for 72\\% of errors in high-BCS batches vs.\\ 15\\% in low-BCS batches; ExtraSub is zero (forced-choice format). Extreme-BCS batches produce $9.9\\text{--}27.5\\times$ more confusion than low-BCS batches. Cross-model replication confirms the IntraSub--BCS correlation on FewRel RE: Gemini~2.5~Flash ($\\rho = 0.821$, $p < 0.001$, $n = 60$) and LLaMA-3.1-8B ($\\rho = 0.430$, $p = 0.001$, $n = 54$; Table~\\ref{tab:cross_model_error_taxonomy}).",
          " ",
          " \\looseness=-1",
          "-These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.",
          "+These results establish two dimensions: \\textbf{Dimension~1} (count predicts recall decline) and \\textbf{Dimension~2} (confusability predicts type confusion). The full-range regression ($n = 69$, five count levels) serves as the primary separability test; the $2 \\times 2$ factorial ($n = 54$) as a sensitivity check. We select the equivalence margin via convergent evidence: (i)~an interaction exceeding the main effect magnitude would undermine dimensional separability; (ii)~Cohen's $d = 0.5$ \\citep{cohen-1988-statistical} (medium effect) at the within-cell SD of 4.6\\,pp yields $\\pm 2.3$\\,pp. Both converge on $\\pm 2\\text{--}3$\\,pp.\\footnote{Margin sensitivity (Table~\\ref{tab:tost_sensitivity}) confirms equivalence from $\\pm 2$\\,pp ($p = 0.047$) through $\\pm 5$\\,pp.} On the linear scale, TOST \\citep{lakens-2017-equivalence,schuirmann-1987-tost} bounds the FewRel interaction within $\\pm 3$\\,pp ($p = 0.003$); at $\\pm 2$\\,pp, equivalence is marginal ($p = 0.047$). Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference. The logit-scale result is inconclusive ($p = 0.209$; regression-based TOST: $p = 0.050$ at $\\pm 3$\\,pp; Appendix~\\ref{sec:appendix_factorial}). On DocRED, the raw factorial interaction ($-$9.4\\,pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93\\,pp, consistent with bounded interaction (Appendix~\\ref{sec:appendix_factorial}). In NER, batch-level BCS signal is not detected at current power (\\S\\ref{sec:bcs_controlled}). Two factors explain the asymmetry: (1)~NER errors distribute across miss, boundary, and type modes rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact; Appendix~\\ref{app:relaxed-matching}), and (2)~BCS range restriction (SD ratio 19\\%) limits statistical detection power to 65\\% (Appendix~\\ref{sec:appendix_ner_power}). The factorial test is inconclusive ($p = 0.50$). At $n{=}450$ with BCS SD${}\\,=\\,0.027$, the minimum detectable correlation is $|r| \\approx 0.132$ ($\\alpha = 0.05$, power${}\\,=\\,0.80$), while FewRel's $r = -0.57$ would attenuate to $r \\approx -0.11$ under this SD compression. Current evidence cannot distinguish absence of a BCS$\\to$NER effect from an effect too small to detect---absence of evidence rather than evidence of absence. Post-hoc mitigation attempts---type renaming to reduce SCS and few-shot prompting---fail to close the confusability gap (Appendices~\\ref{app:renaming},~\\ref{sec:appendix_fewshot_bcs}), confirming that BCS captures a structural property of the schema--model interaction rather than a surface-level naming artifact.",
          " ",
          " \\subsection{Centrality as a Potential Confound on Homogeneous Schemas}",
          " \\label{sec:centrality_confound}"
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

_source line 91_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_011qVceARAJnRgQs43XGoMvq`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "completed",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "completed",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "completed",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "in_progress",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "pending",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "8424a618-d98e-48fa-a241-74b777db96e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XxaySgCxv9yCsEVrMf5Zb1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 391,
      "cache_read_input_tokens": 105799,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 391
      },
      "output_tokens": 72,
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

_source line 92 · 2026-05-22T06:49:00.808Z_

<details><summary>↩ Tool result · `toolu_011qVceARAJnRgQs43XGoMvq`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "1fb69026-d9a1-4eea-bea5-263575b33e13",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "in_progress",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "pending",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "completed",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "in_progress",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 93_

Now compiling to verify no errors and ≤8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "9df1e6c4-0886-4d74-94db-3b13198bdfe4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9ZDkG2tSPgn2aJvPi3Gun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 106190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 94_

<details open><summary>🔧 Tool call — Bash · `toolu_018f8YYo1ur4SUiJwRez5Dtd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/schema-dag-extraction/docs/paper && pdflatex -interaction=nonstopmode main.tex 2>&1 | tail -20",
  "description": "First pdflatex pass"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d6a09353-5a65-4923-86b3-5be763170ec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D9ZDkG2tSPgn2aJvPi3Gun",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 404,
      "cache_read_input_tokens": 106190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 404
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

_source line 95 · 2026-05-22T06:49:07.069Z_

<details><summary>↩ Tool result · `toolu_018f8YYo1ur4SUiJwRez5Dtd`</summary>

```text
s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type
1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi
c/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo
nts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/
cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr
/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t
exlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t
exmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font
s/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public
/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon
ts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p
fb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha
re/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm
f-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty
pe1/urw/times/utmri8a.pfb>
Output written on main.pdf (27 pages, 480312 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c1d1b832-20ab-499c-b81f-a4678b2b1c43",
  "tool_use_result": {
    "stdout": "s/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type\n1/public/amsfonts/cm/cmmi6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/publi\nc/amsfonts/cm/cmmi7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfo\nnts/cm/cmmi8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/\ncmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr10.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr6.pfb>&lt;/usr\n/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr7.pfb>&lt;/usr/share/t\nexlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmr8.pfb>&lt;/usr/share/texlive/t\nexmf-dist/fonts/type1/public/amsfonts/cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmsy10.pfb>&lt;/usr/share/texlive/texmf-dist/font\ns/type1/public/amsfonts/cm/cmsy6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public\n/amsfonts/cm/cmsy8.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfon\nts/cm/cmsy9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/courier/ucrr8a.p\nfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/helvetic/uhvb8a.pfb>&lt;/usr/sha\nre/texlive/texmf-dist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texm\nf-dist/fonts/type1/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/ty\npe1/urw/times/utmri8a.pfb>\nOutput written on main.pdf (27 pages, 480312 bytes).\nTranscript written on main.log.",
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

_source line 96_

<details open><summary>🔧 Tool call — Bash · `toolu_013mQBQMyAvT6J97G2PBCBSg`</summary>

```json
{
  "command": "bibtex main 2>&1 | tail -5 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^(Output|!|.*Warning.*undefined)\" | head -10 && pdflatex -interaction=nonstopmode main.tex 2>&1 | grep -E \"^(Output|!|.*Warning.*undefined)\" | head -10",
  "description": "bibtex + two more pdflatex passes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0f5d0276-2cb4-467c-9f5d-60902980468a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TJofb77ZeqRaxQKEoSX5Pn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 886,
      "cache_read_input_tokens": 106594,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 886
      },
      "output_tokens": 71,
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

### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b0csvtoie",
  "tool_use_id": "toolu_013mQBQMyAvT6J97G2PBCBSg",
  "description": "bibtex + two more pdflatex passes",
  "task_type": "local_bash",
  "uuid": "7c937177-96e1-46eb-b295-d3ae561157e8",
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1"
}
```

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b0csvtoie",
  "tool_use_id": "toolu_013mQBQMyAvT6J97G2PBCBSg",
  "status": "completed",
  "output_file": "",
  "summary": "bibtex + two more pdflatex passes",
  "uuid": "8ba64522-81bb-4fdb-be82-e805d193e939",
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1"
}
```

---

### Tool result

_source line 99 · 2026-05-22T06:49:14.609Z_

<details><summary>↩ Tool result · `toolu_013mQBQMyAvT6J97G2PBCBSg`</summary>

```text
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Database file #1: references.bib
Warning--can't use both volume and number fields in guo-2021-label-confusion
(There was 1 warning)
Output written on main.pdf (27 pages, 480119 bytes).
Output written on main.pdf (27 pages, 480119 bytes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "7c922402-d591-4283-bb1c-d2e86dcbdec6",
  "tool_use_result": {
    "stdout": "The top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nDatabase file #1: references.bib\nWarning--can't use both volume and number fields in guo-2021-label-confusion\n(There was 1 warning)\nOutput written on main.pdf (27 pages, 480119 bytes).\nOutput written on main.pdf (27 pages, 480119 bytes).",
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q9C2vsC79Pv5gN4NDRgMhF`</summary>

```json
{
  "command": "grep -c \"^!\" main.log; grep \"undefined\" main.log | head -5",
  "description": "Check for errors and undefined refs"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "a412c99e-5007-412e-a9df-880402ddb70e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Qf7Bb6uKABv2QugQ4oNXXr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 107480,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 101 · 2026-05-22T06:49:18.368Z_

<details><summary>↩ Tool result · `toolu_01Q9C2vsC79Pv5gN4NDRgMhF`</summary>

```text
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "7e390ac7-af75-4f42-b4d4-878a322480e4",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 102_

0 errors, 0 undefined refs. Now check page boundary — body must be ≤8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "18210f05-a38f-412d-8eda-7490e874039b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtVy7FEUo65YxoemQnyM5L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 107765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 107
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

_source line 103_

<details open><summary>🔧 Tool call — Bash · `toolu_01WgrNASD1mdbrjo2HX7BpRH`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - | head -80",
  "description": "Check page 8/9 boundary content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "1a7859ce-d256-4bb1-896e-4418b5c57538",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AtVy7FEUo65YxoemQnyM5L",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 107,
      "cache_read_input_tokens": 107765,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 107
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

_source line 104 · 2026-05-22T06:49:22.791Z_

<details><summary>↩ Tool result · `toolu_01WgrNASD1mdbrjo2HX7BpRH`</summary>

```text
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616

(ρ = 0.821, p < 0.001, n = 60) and LLaMA-3.18B (ρ = 0.430, p = 0.001, n = 54; Table 7).

4.5

Centrality as a Potential Confound on
Homogeneous Schemas

617

These results establish two dimensions: Dimension 1 (count predicts recall decline) and Dimension 2 (confusability predicts type confusion). The
full-range regression (n = 69, five count levels)
serves as the primary separability test; the 2 × 2
factorial (n = 54) as a sensitivity check. We select
the equivalence margin via convergent evidence:
(i) an interaction exceeding the main effect magnitude would undermine dimensional separability;
(ii) Cohen’s d = 0.5 (Cohen, 1988) (medium effect) at the within-cell SD of 4.6 pp yields ±2.3 pp.
Both converge on ±2–3 pp.6 On the linear scale,
TOST (Lakens, 2017; Schuirmann, 1987) bounds
the FewRel interaction within ±3 pp (p = 0.003);
at ±2 pp, equivalence is marginal (p = 0.047).
Probability-scale TOST is the primary analysis because accuracy values (0.37–0.86) remain in the
mid-range where logit and linear scales yield similar inference. The logit-scale result is inconclusive
(p = 0.209; regression-based TOST: p = 0.050
at ±3 pp; Appendix C). On DocRED, the raw factorial interaction (−9.4 pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93 pp, consistent with bounded
interaction (Appendix C). In NER, batch-level BCS
signal is not detected at current power (§4.3). Two
factors explain the asymmetry: (1) NER errors
distribute across miss, boundary, and type modes
rather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact;
Appendix Y), and (2) BCS range restriction (SD
ratio 19%) limits statistical detection power to 65%
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0f62f8b0-ab43-4b10-829c-cfb130716f41",
  "tool_use_result": {
    "stdout": "569\n570\n571\n572\n573\n574\n575\n576\n577\n578\n579\n580\n581\n582\n583\n584\n585\n586\n587\n588\n589\n590\n591\n592\n593\n594\n595\n596\n597\n598\n599\n600\n601\n602\n603\n604\n605\n606\n607\n608\n609\n610\n611\n612\n613\n614\n615\n616\n\n(ρ = 0.821, p < 0.001, n = 60) and LLaMA-3.18B (ρ = 0.430, p = 0.001, n = 54; Table 7).\n\n4.5\n\nCentrality as a Potential Confound on\nHomogeneous Schemas\n\n617\n\nThese results establish two dimensions: Dimension 1 (count predicts recall decline) and Dimension 2 (confusability predicts type confusion). The\nfull-range regression (n = 69, five count levels)\nserves as the primary separability test; the 2 × 2\nfactorial (n = 54) as a sensitivity check. We select\nthe equivalence margin via convergent evidence:\n(i) an interaction exceeding the main effect magnitude would undermine dimensional separability;\n(ii) Cohen’s d = 0.5 (Cohen, 1988) (medium effect) at the within-cell SD of 4.6 pp yields ±2.3 pp.\nBoth converge on ±2–3 pp.6 On the linear scale,\nTOST (Lakens, 2017; Schuirmann, 1987) bounds\nthe FewRel interaction within ±3 pp (p = 0.003);\nat ±2 pp, equivalence is marginal (p = 0.047).\nProbability-scale TOST is the primary analysis because accuracy values (0.37–0.86) remain in the\nmid-range where logit and linear scales yield similar inference. The logit-scale result is inconclusive\n(p = 0.209; regression-based TOST: p = 0.050\nat ±3 pp; Appendix C). On DocRED, the raw factorial interaction (−9.4 pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93 pp, consistent with bounded\ninteraction (Appendix C). In NER, batch-level BCS\nsignal is not detected at current power (§4.3). Two\nfactors explain the asymmetry: (1) NER errors\ndistribute across miss, boundary, and type modes\nrather than concentrating in type substitution (relaxed matching confirms this is not a metric artifact;\nAppendix Y), and (2) BCS range restriction (SD\nratio 19%) limits statistical detection power to 65%",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 105_

<details><summary>Logged reasoning block</summary>

```text
Let me check exactly where page 8 ends and page 9 begins. The output shows the page 8/9 content. It seems like the body text continues past page 8 — the TOST discussion, §4.5, §4.6 content all appear on pages 8-9. Let me check more carefully where the Limitations section starts, as that marks the end of the body.

Let me check what's on the later pages to find where the main body ends.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "5ee66802-a68c-4172-98f8-dc144875b54b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1vEhpLQYheGm2wA8dbqV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 107872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 106_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y7VXpe4ZDaFW3DzTcv69LY`</summary>

```json
{
  "command": "pdftotext -f 9 -l 10 main.pdf - | head -80",
  "description": "Check page 9/10 boundary"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "8e621766-0843-4a27-9326-2fedbde9c339",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M1vEhpLQYheGm2wA8dbqV7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 797,
      "cache_read_input_tokens": 107872,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 797
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

_source line 107 · 2026-05-22T06:49:29.014Z_

<details><summary>↩ Tool result · `toolu_01Y7VXpe4ZDaFW3DzTcv69LY`</summary>

```text
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713

mensions 1–2 (count curves, BCS-controlled
extremes) but does not replicate secondary
analyses (error taxonomy, prompt sensitivity,
TOST equivalence). Specifically, TOST factorial interaction (§4.4) and SDGD failure
analysis (§5) are established on Qwen3-32B
alone; error taxonomy replicates on two additional models (Table 7), but TOST and SDGD
cross-model replication remains the most pressing extension. Gemini provides only partial,
leverage-sensitive corroboration (leave-one-out
r: −0.80 → −0.42; Appendix U); proprietarymodel generalization remains open.

The study establishes correlational evidence
with controlled stratification; mechanistic analysis at the attention or logit level is needed to
confirm the causal pathway. A post-hoc renaming experiment (Appendix X) suggests SCS may
proxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in
pretraining corpora, but train-origin relations
show lower accuracy than val-origin, opposite to
the contamination hypothesis; DocRED (2019)
provides a lower-contamination-risk replication
(Appendix Q).
5. Domain and language scope. All evaluations use English-language datasets derived
from Wikipedia or knowledge bases (Wikidata,
FrameNet). Whether confusability effects hold
for domain-specific schemas (e.g., biomedical
NER, legal RE) or languages with different naming conventions is untested. BCS-controlled
batches inherit the domain distribution of the
source schema; domain-specific type subsets
may shift the confusability–accuracy relationship. Sample sizes (1,000 instances per dataset)
are sufficient for our primary effects but the pairwise SCS correlation approaches the detection
floor.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d7d6e258-487d-438b-ae22-7b94a341929d",
  "tool_use_result": {
    "stdout": "664\n665\n666\n667\n668\n669\n670\n671\n672\n673\n674\n675\n676\n677\n678\n679\n680\n681\n682\n683\n684\n685\n686\n687\n688\n689\n690\n691\n692\n693\n694\n695\n696\n697\n698\n699\n700\n701\n702\n703\n704\n705\n706\n707\n708\n709\n710\n711\n712\n713\n\nmensions 1–2 (count curves, BCS-controlled\nextremes) but does not replicate secondary\nanalyses (error taxonomy, prompt sensitivity,\nTOST equivalence). Specifically, TOST factorial interaction (§4.4) and SDGD failure\nanalysis (§5) are established on Qwen3-32B\nalone; error taxonomy replicates on two additional models (Table 7), but TOST and SDGD\ncross-model replication remains the most pressing extension. Gemini provides only partial,\nleverage-sensitive corroboration (leave-one-out\nr: −0.80 → −0.42; Appendix U); proprietarymodel generalization remains open.\n\nThe study establishes correlational evidence\nwith controlled stratification; mechanistic analysis at the attention or logit level is needed to\nconfirm the causal pathway. A post-hoc renaming experiment (Appendix X) suggests SCS may\nproxy deeper conceptual overlap rather than surface similarity. FewRel (2018) may appear in\npretraining corpora, but train-origin relations\nshow lower accuracy than val-origin, opposite to\nthe contamination hypothesis; DocRED (2019)\nprovides a lower-contamination-risk replication\n(Appendix Q).\n5. Domain and language scope. All evaluations use English-language datasets derived\nfrom Wikipedia or knowledge bases (Wikidata,\nFrameNet). Whether confusability effects hold\nfor domain-specific schemas (e.g., biomedical\nNER, legal RE) or languages with different naming conventions is untested. BCS-controlled\nbatches inherit the domain distribution of the\nsource schema; domain-specific type subsets\nmay shift the confusability–accuracy relationship. Sample sizes (1,000 instances per dataset)\nare sufficient for our primary effects but the pairwise SCS correlation approaches the detection\nfloor.",
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

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ejm21RSzhaXBonLdnCjfVr`</summary>

```json
{
  "command": "pdftotext -f 7 -l 9 main.pdf - | grep -n \"Limitations\\|Discussion\\|Schema Decomposition\\|References\\|Appendix\\|\\\\*\" | head -20",
  "description": "Find section boundaries on pages 7-9"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "35c00285-b618-4ffd-8c1d-0b4e3c7ecb1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UCCojWBZZAxoZDoctdCXbz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 108669,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 758
      },
      "output_tokens": 57,
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

_source line 109 · 2026-05-22T06:49:32.611Z_

<details><summary>↩ Tool result · `toolu_01Ejm21RSzhaXBonLdnCjfVr`</summary>

```text
113:= 0.056 after centrality; Appendix E.1). The
123:BCS practically predictive (∼3× amplification illustrated by Monte Carlo simulation; Appendix N).
132:(all r ≤ −0.47; Appendix H.1), ruling out prompt
136:and count level (Appendix V).
171:−0.18, p = 0.64; Appendix U). LLaMA-8B
280:at ±3 pp; Appendix C). On DocRED, the raw factorial interaction (−9.4 pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93 pp, consistent with bounded
281:interaction (Appendix C). In NER, batch-level BCS
286:Appendix Y), and (2) BCS range restriction (SD
288:(Appendix E.2). The factorial test is inconclusive
305:Appendix E), though the pairwise SCS signal
323:Schema Decomposition
349:results, and analysis are in Appendix B.
357:Discussion and Conclusion
378:compressed BCS variance (Appendix E.2).
393:Limitations
480:r: −0.80 → −0.42; Appendix U); proprietarymodel generalization remains open.
484:confirm the causal pathway. A post-hoc renaming experiment (Appendix X) suggests SCS may
490:(Appendix Q).
507:at higher counts (Appendix C); logit-scale evidence remains inconclusive. DocRED count
509:per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix R) but
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d317463a-1dd8-4ad9-964b-0841892ec049",
  "tool_use_result": {
    "stdout": "113:= 0.056 after centrality; Appendix E.1). The\n123:BCS practically predictive (∼3× amplification illustrated by Monte Carlo simulation; Appendix N).\n132:(all r ≤ −0.47; Appendix H.1), ruling out prompt\n136:and count level (Appendix V).\n171:−0.18, p = 0.64; Appendix U). LLaMA-8B\n280:at ±3 pp; Appendix C). On DocRED, the raw factorial interaction (−9.4 pp) is confounded by narrower BCS ranges at count 32; range-matched analysis reduces it to 0.93 pp, consistent with bounded\n281:interaction (Appendix C). In NER, batch-level BCS\n286:Appendix Y), and (2) BCS range restriction (SD\n288:(Appendix E.2). The factorial test is inconclusive\n305:Appendix E), though the pairwise SCS signal\n323:Schema Decomposition\n349:results, and analysis are in Appendix B.\n357:Discussion and Conclusion\n378:compressed BCS variance (Appendix E.2).\n393:Limitations\n480:r: −0.80 → −0.42; Appendix U); proprietarymodel generalization remains open.\n484:confirm the causal pathway. A post-hoc renaming experiment (Appendix X) suggests SCS may\n490:(Appendix Q).\n507:at higher counts (Appendix C); logit-scale evidence remains inconclusive. DocRED count\n509:per-batch evaluation cost. BCS-controlled experiments use a single seed with greedy decoding; residual variance is small (Appendix R) but",
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

_source line 110_

<details open><summary>🔧 Tool call — Bash · `toolu_01GxCxG5pzD6zyXiqJcFdmqq`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - | grep -n \"Limitations\\|Discussion\\|Schema Decomposition\\|References\" | head -10",
  "description": "Find exactly where Limitations/Discussion start"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "17aaaaad-5648-410b-8037-c4576510aa4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KX6M5sFqjmWqps4WxAY7gK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 109427,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 555
      },
      "output_tokens": 67,
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

_source line 111 · 2026-05-22T06:49:36.007Z_

<details><summary>↩ Tool result · `toolu_01GxCxG5pzD6zyXiqJcFdmqq`</summary>

```text
116:Schema Decomposition
150:Discussion and Conclusion
186:Limitations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "cd15c5a9-6867-496b-89a1-dd472cbec352",
  "tool_use_result": {
    "stdout": "116:Schema Decomposition\n150:Discussion and Conclusion\n186:Limitations",
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

_source line 112_

<details open><summary>🔧 Tool call — Bash · `toolu_01HFpJwnnp32HYnYZY4Gcvvw`</summary>

```json
{
  "command": "pdftotext main.pdf - | grep -n \"Limitations\" | head -5",
  "description": "Find Limitations section line in full text"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "38ee5bb9-31b1-4f77-8af7-cd03966f5e5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AsgL9tQ5N6jbKmRMVmfzFW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 147,
      "cache_read_input_tokens": 109982,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 147
      },
      "output_tokens": 49,
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

_source line 113 · 2026-05-22T06:49:39.802Z_

<details><summary>↩ Tool result · `toolu_01HFpJwnnp32HYnYZY4Gcvvw`</summary>

```text
1651:Limitations
5298:p = 0.06; see Limitations), raising the question
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "5f5bbf8a-0189-49d6-9d3c-f7230e7715df",
  "tool_use_result": {
    "stdout": "1651:Limitations\n5298:p = 0.06; see Limitations), raising the question",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 114_

<details><summary>Logged reasoning block</summary>

```text
Let me check precisely which page the "Limitations" section is on. On the pdftotext output for pages 8-9, "Limitations" appears at line 186 within those 2 pages. Let me check more precisely. Let me see what page the Discussion and Conclusion section is on and how the body content fits.

Looking at the pdftotext output for pages 8-9:
- Line 116: "Schema Decomposition" (§5) starts on page 8
- Line 150: "Discussion and Conclusion" (§6) starts on page 8  


- Line 186: "Limitations" starts on page 9

So the Limitations section begins on page 9, after the Discussion and Conclusion. Since EMNLP's 8-page limit applies only to main text—with Limitations and References excluded—the body content through the Discussion needs to fit within page 8. The Discussion paragraph appears to be quite brief, which means the main sections are compressed into that space.

Let me check the exact page 8 content to determine whether the Discussion actually stays within the 8-page boundary or spills into page 9.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "1f233692-370d-4bae-9d60-03188eefa0b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhdQCjeogyMKAJyNYvcg4W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 110129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
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

_source line 115_

<details open><summary>🔧 Tool call — Bash · `toolu_01QFbm4Hywn8txGQGDdWdPeA`</summary>

```json
{
  "command": "pdftotext -f 8 -l 8 main.pdf - | tail -30",
  "description": "Check end of page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c8884371-b61a-4b2d-8097-a7e4697e8dcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DhdQCjeogyMKAJyNYvcg4W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 420,
      "cache_read_input_tokens": 110129,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 420
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

_source line 116 · 2026-05-22T06:49:55.132Z_

<details><summary>↩ Tool result · `toolu_01QFbm4Hywn8txGQGDdWdPeA`</summary>

```text
Limitations

660

1. Model coverage. Primary experiments use
Qwen3-32B; cross-model validation (LLaMA8B, LLaMA-70B, Gemini Flash) covers Di-

661

645
646
647
648
649
650
651

653
654
655
656
657
658
659

662
663
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "910323c7-ceab-431c-8041-73e8a0c123c2",
  "tool_use_result": {
    "stdout": "Limitations\n\n660\n\n1. Model coverage. Primary experiments use\nQwen3-32B; cross-model validation (LLaMA8B, LLaMA-70B, Gemini Flash) covers Di-\n\n661\n\n645\n646\n647\n648\n649\n650\n651\n\n653\n654\n655\n656\n657\n658\n659\n\n662\n663",
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

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_0137E8XQ1Tonmpe4DjgagWfu`</summary>

```json
{
  "command": "pdftotext -f 8 -l 8 main.pdf - | grep -n \"Limitations\\|Discussion\\|Schema Decomposition\" | head -10",
  "description": "Find section headers on page 8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "448e72b4-9e5a-44b5-8f53-482572ce944c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017MVH4kqr14nNXvDcHNXDV4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 110549,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 676
      },
      "output_tokens": 64,
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

_source line 118 · 2026-05-22T06:49:58.877Z_

<details><summary>↩ Tool result · `toolu_0137E8XQ1Tonmpe4DjgagWfu`</summary>

```text
116:Schema Decomposition
150:Discussion and Conclusion
186:Limitations
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "a26c8e0e-af7f-4806-83f4-53696b5f6281",
  "tool_use_result": {
    "stdout": "116:Schema Decomposition\n150:Discussion and Conclusion\n186:Limitations",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 119_

Page 8 contains: Schema Decomposition (§5), Discussion and Conclusion (§6), and the start of Limitations. Since Limitations doesn't count toward the 8-page limit, the body text (through Discussion) fits within page 8. Good.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "aad7df54-7874-463c-ab52-332e6ef001ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzZ3BocUJKjNC5ywZya95h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 143,
      "cache_read_input_tokens": 111225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 143
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

_source line 120_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01CMu7mk3DWRm93P385YUKS1`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "completed",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "completed",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "completed",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "completed",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "in_progress",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "c4b61b67-2b13-44f2-9d38-8035c277f915",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TzZ3BocUJKjNC5ywZya95h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 143,
      "cache_read_input_tokens": 111225,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 143
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

_source line 121 · 2026-05-22T06:50:04.886Z_

<details><summary>↩ Tool result · `toolu_01CMu7mk3DWRm93P385YUKS1`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "698d5a54-e44f-4938-bb05-310336276792",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "completed",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "in_progress",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "pending",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "completed",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "completed",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "in_progress",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 122_

Compilation: 0 errors, 0 undefined refs, body ≤ 8 pages (Limitations starts on page 8, after Discussion). All clear.

---

## 修改摘要表

| # | 文件:行号 | 类型 | 修改前 | 修改后 | 原因 |
|---|-----------|------|--------|--------|------|
| 1 | abstract.tex:3 | 重复 | `(1)~...predicts type substitution errors in RE ($R^2 \approx 0.22$ on FewRel, VIF${}=1.18$); the batch-level BCS signal is not detected in NER at current statistical power;` | `(1)~...independently predicts RE type substitution errors (VIF${}=1.18$ on FewRel);` | R²≈0.22 与 finding (2) 的 ~22% 重复；NER null 与 (2) 重复。R² 移至 (2)，NER null 仅保留在 (2) |
| 2 | abstract.tex:4 | 重复 | `(2)~BCS explains ${\sim}$22\% ... (ecological level),` | `(2)~BCS explains ${\sim}$22\% ... ($R^2 \approx 0.22$, ecological level),` | 将 R² 具体数值归并到 (2) 作为唯一报告位置 |
| 3 | introduction.tex:24 | 长句 | 单句 ~60 词：`We establish that...not previously documented in training-free LLM IE (§...)` | 拆为两句：`...explaining ~22% of batch-level variance (ecological level). This finding is enabled by BCS-controlled batch design...` | 原句超 35 词限制，拆分后各 ~30 词；同时删除 "where confusability is not confounded with centrality"（VIF=1.18 已隐含低共线性） |
| 4 | introduction.tex:25 | 重复 | `on FewRel, BCS explains ${\sim}$22\% of RE accuracy variance through type substitution ($R^2 = 0.218$, VIF${}=1.18$; ecological level)---an effect confirmed as format-independent---yet NER...` | `the RE confusability effect is confirmed as format-independent, yet NER batch-level BCS signal is not detected at current power...---an asymmetry attributable to dispersed NER error modes and BCS range compression` | R²=0.218、VIF=1.18、~22% 均已在 C1 中报告，C2 不应重复。改为阐述 asymmetry 的原因，增加信息量 |
| 5 | related_work.tex:18 | 长句 | `Unlike LLM-PEE, which...our SCS/BCS metrics serve an analytical role: SCS quantifies...` (38 词) | 拆为两句：`...serve an analytical role. SCS quantifies...; BCS averages...` | 超 35 词，拆分为独立陈述 |
| 6 | related_work.tex:18 | 重复 | `...to explain ${\sim}$22\% of cross-batch RE variance on FewRel` | `...to explain substantial cross-batch RE variance on FewRel` | ~22% 在 abstract、intro、results §4.3 已出现多次；related work 改为定性描述 + §4.3 引用 |
| 7 | experimental_setup.tex:10 | 模糊 | `The dataset spans diverse domains and is suitable for cross-domain evaluation.` | `The dataset spans diverse domains.` | "is suitable for cross-domain evaluation" 无信息量，前半句已传达同义 |
| 8 | experimental_setup.tex:13 | 长句 | `Since the validation split covers only 16 relations, we combine...and sample 1,000 balanced instances...` (37 词) | 拆为两句：`...required for schema-scale experiments. We sample 1,000 balanced instances...` | 拆分后各 ~18 词，逻辑独立 |
| 9 | experimental_setup.tex:16 | 长句 | `We sample 1,000 instances...from the DocRED development set and formulate the task identically to FewRel:...` (38 词) | 拆为两句：`...from the DocRED development set. The task is formulated identically to FewRel:...` | 采样和任务定义是独立信息，拆分提高可读性 |
| 10 | experimental_setup.tex:87 | 被动→主动 + 长句 | `Extreme batches are constructed via greedy search over the pairwise SCS matrix: the low-BCS batch starts...` (42 词) | `We construct extreme batches via greedy search over the pairwise SCS matrix. The low-BCS batch starts...` | 被动改主动 + 拆分 42 词长句 |
| 11 | results.tex:37 | 重复 | `batch-level BCS explains ${\sim}$22\% of RE accuracy variance on FewRel (§4.3)` | `correlated type pairs within batches compound this signal into substantial batch-level RE accuracy variance (§4.3)` | §4.2 预告 §4.3 的结果不必重复具体数字，改为定性前瞻 + 引用 |
| 12 | results.tex:81 | 重复 | `...absence of evidence rather than evidence of absence. The null is equally consistent with NER's error-mode structure, where degradation distributes across miss, boundary, and type channels rather than concentrating in type substitution---a pattern confirmed by relaxed matching (Appendix). Post-hoc mitigation attempts...` | `...absence of evidence rather than evidence of absence. Post-hoc mitigation attempts...` | 删除的句子与同段 factor (1) 几乎逐字重复（"NER errors distribute across miss, boundary, and type modes...relaxed matching"），冗余 |
| 13 | results.tex:81 | 长句 | `Probability-scale TOST is the primary analysis because accuracy values (0.37--0.86) remain in the mid-range where logit and linear scales yield similar inference; the logit-scale result is inconclusive...` (41 词) | 拆为两句：`...yield similar inference. The logit-scale result is inconclusive...` | 主分析选择理由与 logit 结果是独立论点，拆分提高可读性 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "0870a04b-547b-486b-9bd1-efd488a81fb0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfYb7gMFbRLh48i5ArGtg6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 111368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 123_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01KJpZ9Z1JsfJLBUiCTLA25Z`</summary>

```json
{
  "todos": [
    {
      "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
      "status": "completed",
      "activeForm": "Editing abstract.tex to remove redundant numbers"
    },
    {
      "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
      "status": "completed",
      "activeForm": "Editing introduction.tex contributions"
    },
    {
      "content": "Related work: split 38-word sentence, replace ~22% with section reference",
      "status": "completed",
      "activeForm": "Editing related_work.tex"
    },
    {
      "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
      "status": "completed",
      "activeForm": "Editing experimental_setup.tex"
    },
    {
      "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
      "status": "completed",
      "activeForm": "Editing results.tex"
    },
    {
      "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
      "status": "completed",
      "activeForm": "Compiling and verifying LaTeX"
    },
    {
      "content": "Produce change summary table",
      "status": "completed",
      "activeForm": "Producing change summary table"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "d6dc8ad5-5b82-4bc1-9f3e-ebe9c1bffc98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SfYb7gMFbRLh48i5ArGtg6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 111368,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 124 · 2026-05-22T06:50:46.792Z_

<details><summary>↩ Tool result · `toolu_01KJpZ9Z1JsfJLBUiCTLA25Z`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "dfdfb41b-278b-4135-8717-e21f87aa82f7",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "completed",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "completed",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "in_progress",
        "activeForm": "Producing change summary table"
      }
    ],
    "newTodos": [
      {
        "content": "Abstract: remove redundant R²≈0.22 from finding (1), consolidate with (2)",
        "status": "completed",
        "activeForm": "Editing abstract.tex to remove redundant numbers"
      },
      {
        "content": "Introduction: split long contribution 1 sentence (~60 words), remove redundant numbers from contribution 2",
        "status": "completed",
        "activeForm": "Editing introduction.tex contributions"
      },
      {
        "content": "Related work: split 38-word sentence, replace ~22% with section reference",
        "status": "completed",
        "activeForm": "Editing related_work.tex"
      },
      {
        "content": "Experimental setup: remove vague phrase, split long sentences, fix passive voice",
        "status": "completed",
        "activeForm": "Editing experimental_setup.tex"
      },
      {
        "content": "Results: replace repeated ~22% with forward ref, remove redundant NER error-mode restatement, split long TOST sentence",
        "status": "completed",
        "activeForm": "Editing results.tex"
      },
      {
        "content": "Compile LaTeX and verify 0 errors, ≤8 pages",
        "status": "completed",
        "activeForm": "Compiling and verifying LaTeX"
      },
      {
        "content": "Produce change summary table",
        "status": "completed",
        "activeForm": "Producing change summary table"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 125_

13 处修改完成。编译验证：0 errors，0 undefined refs，body ≤ 8 pages（Discussion/Conclusion 在 page 8，Limitations 从 page 8 底部开始，不计入正文页数）。所有修改均为 prose 层面优化，未改变 claim 强度、数值、引用或 paper structure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "uuid": "88093f93-65bd-446b-80b7-b6e02bb9e630",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EVYQTHtYudJzYPawmQoiYa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2124,
      "cache_read_input_tokens": 111831,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2124
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

_source line 126_

13 处修改完成。编译验证：0 errors，0 undefined refs，body ≤ 8 pages（Discussion/Conclusion 在 page 8，Limitations 从 page 8 底部开始，不计入正文页数）。所有修改均为 prose 层面优化，未改变 claim 强度、数值、引用或 paper structure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 757608,
  "duration_api_ms": 752453,
  "num_turns": 50,
  "stop_reason": "end_turn",
  "session_id": "82345c4c-5417-47e4-ae39-ed4a684ccbb1",
  "total_cost_usd": 3.3826547500000004,
  "usage": {
    "input_tokens": 42,
    "cache_creation_input_tokens": 115441,
    "cache_read_input_tokens": 3538119,
    "output_tokens": 35599,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 115441,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 102,
        "cache_read_input_tokens": 111831,
        "cache_creation_input_tokens": 2124,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2124
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1814,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001904,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 42,
      "outputTokens": 35599,
      "cacheReadInputTokens": 3538119,
      "cacheCreationInputTokens": 115441,
      "webSearchRequests": 0,
      "costUSD": 3.3807507500000007,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "3c7800d3-ff19-49fe-b856-38fabb84306b"
}
```

</details>

---
