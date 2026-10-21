# writing review paper edits batch2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 83
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_writing_review-paper-edits-batch2_20260515T123532.log`
- **Structured JSON:** [`b0b8cf7de5436f2289b6.json`](../../sessions/b0/b0b8cf7de5436f2289b6.json)

## Before a recorded user message

83 recorded events

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
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
    "mcp__agent-ml-research__clone_repo",
    "mcp__agent-ml-research__list_repo_tree",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__read_repo_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__search_repo",
    "mcp__agent-ml-research__sync_code_to_remote"
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
  "uuid": "3fde429e-d71f-484e-82b8-dd131132ef24",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-3-projects-gen-depth-fingerprint/memory/"
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
    "resetsAt": 1778866200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ce53e83f-cbcc-44e4-99c6-362de1ec4ad9",
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204"
}
```

---

### Assistant

_source line 4_

I'll start by reading the relevant files and searching for the values that need updating.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "7c28e897-d022-4609-9c06-187aef31e57c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmhukjjiBT9x11LuviGWsG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12898,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12898
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

<details open><summary>🔧 Tool call — Glob · `toolu_01UL3eqSCDhhH8VwgAGYWRDJ`</summary>

```json
{
  "pattern": "artifacts/_project/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ac325415-ec84-4f62-a55f-a659aa078618",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmhukjjiBT9x11LuviGWsG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12898,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12898
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

_source line 6 · 2026-05-15T12:35:46.364Z_

<details><summary>↩ Tool result · `toolu_01UL3eqSCDhhH8VwgAGYWRDJ`</summary>

```text
artifacts/_project/paper/method_01fe38.tex
artifacts/_project/paper/ethics_7f2659.tex
artifacts/_project/paper/table1.tex
artifacts/_project/paper/table1_329527.tex
artifacts/_project/paper/table2.tex
artifacts/_project/paper/table2_373612.tex
artifacts/_project/paper/table3.tex
artifacts/_project/paper/table3_fc4017.tex
artifacts/_project/paper/discussion_d3a579.tex
artifacts/_project/paper/table4.tex
artifacts/_project/paper/table4_49aebb.tex
artifacts/_project/paper/ethics_25b81b.tex
artifacts/_project/paper/ethics.tex
artifacts/_project/paper/related_work_2ce9dd.tex
artifacts/_project/paper/main_53f11a.tex
artifacts/_project/paper/conclusion_b5f10d.tex
artifacts/_project/paper/introduction_4bbcfd.tex
artifacts/_project/paper/conclusion_70534e.tex
artifacts/_project/paper/discussion_c98572.tex
artifacts/_project/paper/appendix_length.tex
artifacts/_project/paper/abstract_014854.tex
artifacts/_project/paper/results_b30771.tex
artifacts/_project/paper/limitations_69ebec.tex
artifacts/_project/paper/limitations_b3d194.tex
artifacts/_project/paper/method_e59d28.tex
artifacts/_project/paper/appendix_prompt_type.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/appendix_confusion_matrix.tex
artifacts/_project/paper/appendix_finer_depth.tex
artifacts/_project/paper/appendix_classifier.tex
artifacts/_project/paper/appendix_lofo.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/method.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "267d1970-91d3-4c9d-b94c-491bf9555761",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/method_01fe38.tex",
      "artifacts/_project/paper/ethics_7f2659.tex",
      "artifacts/_project/paper/table1.tex",
      "artifacts/_project/paper/table1_329527.tex",
      "artifacts/_project/paper/table2.tex",
      "artifacts/_project/paper/table2_373612.tex",
      "artifacts/_project/paper/table3.tex",
      "artifacts/_project/paper/table3_fc4017.tex",
      "artifacts/_project/paper/discussion_d3a579.tex",
      "artifacts/_project/paper/table4.tex",
      "artifacts/_project/paper/table4_49aebb.tex",
      "artifacts/_project/paper/ethics_25b81b.tex",
      "artifacts/_project/paper/ethics.tex",
      "artifacts/_project/paper/related_work_2ce9dd.tex",
      "artifacts/_project/paper/main_53f11a.tex",
      "artifacts/_project/paper/conclusion_b5f10d.tex",
      "artifacts/_project/paper/introduction_4bbcfd.tex",
      "artifacts/_project/paper/conclusion_70534e.tex",
      "artifacts/_project/paper/discussion_c98572.tex",
      "artifacts/_project/paper/appendix_length.tex",
      "artifacts/_project/paper/abstract_014854.tex",
      "artifacts/_project/paper/results_b30771.tex",
      "artifacts/_project/paper/limitations_69ebec.tex",
      "artifacts/_project/paper/limitations_b3d194.tex",
      "artifacts/_project/paper/method_e59d28.tex",
      "artifacts/_project/paper/appendix_prompt_type.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/discussion.tex",
      "artifacts/_project/paper/appendix_confusion_matrix.tex",
      "artifacts/_project/paper/appendix_finer_depth.tex",
      "artifacts/_project/paper/appendix_classifier.tex",
      "artifacts/_project/paper/appendix_lofo.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/limitations.tex",
      "artifacts/_project/paper/method.tex"
    ],
    "durationMs": 15,
    "numFiles": 39,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Grep · `toolu_018b11Sf4hYM4JWvk87kMT2K`</summary>

```json
{
  "pattern": "1\\.4",
  "path": "artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "0bb0300a-95a1-4012-9ba3-ac2c5c224c94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RHLZ3Co65GtWozo2doyuZZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 599,
      "cache_read_input_tokens": 24739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 599
      },
      "output_tokens": 48,
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

_source line 8 · 2026-05-15T12:35:49.423Z_

<details><summary>↩ Tool result · `toolu_018b11Sf4hYM4JWvk87kMT2K`</summary>

```text
artifacts/_project/paper/appendix_prompt_type.tex:7:Leave-one-prompt-type-out evaluation yields average F1\,=\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\% per depth step), followed by rewriting (6.1\%) and elaboration (1.4\%), consistent with continuation chains applying less semantic constraint on the output.
artifacts/_project/paper/table4_49aebb.tex:8:Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
artifacts/_project/paper/main.tex:26:In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\,pp vs.\ 18--26\,pp for single detectors).
artifacts/_project/paper/discussion.tex:22:The tight cross-generator consistency of the ensemble (CI width 1.4\,pp) makes deployment feasible even when the generating model is unknown.
artifacts/_project/paper/table4.tex:8:Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\
artifacts/_project/paper/abstract.tex:8:In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\,pp vs.\ 18--26\,pp for single detectors).
artifacts/_project/paper/introduction.tex:24:This ensemble maintains tight cross-generator consistency (CI width 1.4\,pp), whereas the best single detector spans over 20\,pp.
artifacts/_project/paper/results.tex:107:\caption{LOGO macro-F1 with 95\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\,pp; the ensemble CI spans 1.4\,pp.}
artifacts/_project/paper/results.tex:134:The ensemble CI spans just 1.4\,pp [0.786, 0.800], while single-detector CIs span 18--26\,pp (e.g., Avg-LogProb [0.616, 0.820]).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "df124bb3-ff50-446e-aa18-4c5f5934e272",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/appendix_prompt_type.tex:7:Leave-one-prompt-type-out evaluation yields average F1\\,=\\,0.753, confirming that depth signal transfers across prompt types. Feature decay rates differ: continuation shows the strongest drift (16.9\\% per depth step), followed by rewriting (6.1\\%) and elaboration (1.4\\%), consistent with continuation chains applying less semantic constraint on the output.\nartifacts/_project/paper/table4_49aebb.tex:8:Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\\\\nartifacts/_project/paper/main.tex:26:In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nartifacts/_project/paper/discussion.tex:22:The tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.\nartifacts/_project/paper/table4.tex:8:Pythia-410M & Pythia & 410M & 0.803 & [$-$1.19, $-$1.40] \\\\\nartifacts/_project/paper/abstract.tex:8:In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nartifacts/_project/paper/introduction.tex:24:This ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.\nartifacts/_project/paper/results.tex:107:\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}\nartifacts/_project/paper/results.tex:134:The ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
    "numLines": 9
  }
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Grep · `toolu_01AmmWNfnZbSBCYrx8d71HaH`</summary>

```json
{
  "pattern": "0\\.786|0\\.800",
  "path": "artifacts/_project/paper",
  "glob": "*.tex",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ebdc25b1-defb-496e-b5e0-9846374eb6b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H2HGAbY1GSd5M2FjWrTk1f",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 25338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 10 · 2026-05-15T12:35:54.512Z_

<details><summary>↩ Tool result · `toolu_01AmmWNfnZbSBCYrx8d71HaH`</summary>

```text
artifacts/_project/paper/appendix_lofo.tex:14:tail\_decay     & 0.786 & $-$0.33\,pp \\
artifacts/_project/paper/appendix_lofo.tex:15:entropy\_std    & 0.786 & $-$0.29\,pp \\
artifacts/_project/paper/results_b30771.tex:44:\multicolumn{3}{l}{Average (5-gen, $\leq$2.8B)} & 0.800 \\
artifacts/_project/paper/results_b30771.tex:103:7-feature ensemble & \textbf{0.798} & [0.786, 0.799] \\
artifacts/_project/paper/results_b30771.tex:117:The ensemble CI spans just 1.3\,pp [0.786, 0.799], while single-detector CIs span 18--26\,pp (e.g., Avg-LogProb [0.616, 0.820]).
artifacts/_project/paper/results.tex:45:\multicolumn{3}{l}{5-gen LOGO (excl.\ Qwen3-8B)} & 0.800 & --- \\
artifacts/_project/paper/results.tex:120:7-feature ensemble & \textbf{0.800} & [0.786, 0.800] \\
artifacts/_project/paper/results.tex:134:The ensemble CI spans just 1.4\,pp [0.786, 0.800], while single-detector CIs span 18--26\,pp (e.g., Avg-LogProb [0.616, 0.820]).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e76a190b-44a5-4c67-ab4c-d762962248e5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "artifacts/_project/paper/appendix_lofo.tex:14:tail\\_decay     & 0.786 & $-$0.33\\,pp \\\\\nartifacts/_project/paper/appendix_lofo.tex:15:entropy\\_std    & 0.786 & $-$0.29\\,pp \\\\\nartifacts/_project/paper/results_b30771.tex:44:\\multicolumn{3}{l}{Average (5-gen, $\\leq$2.8B)} & 0.800 \\\\\nartifacts/_project/paper/results_b30771.tex:103:7-feature ensemble & \\textbf{0.798} & [0.786, 0.799] \\\\\nartifacts/_project/paper/results_b30771.tex:117:The ensemble CI spans just 1.3\\,pp [0.786, 0.799], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nartifacts/_project/paper/results.tex:45:\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.800 & --- \\\\\nartifacts/_project/paper/results.tex:120:7-feature ensemble & \\textbf{0.800} & [0.786, 0.800] \\\\\nartifacts/_project/paper/results.tex:134:The ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
    "numLines": 8
  }
}
```

</details>

---

### Assistant

_source line 11_

Now let me read the key files in detail.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "244175c4-75b4-4f02-8bb1-e3e426c807cd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nR7xqty64xP2yb96QFTZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 26136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 549
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

_source line 12_

<details open><summary>🔧 Tool call — Read · `toolu_01K7ErCaN2iMF2x6x9cLqgoz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "8add3e35-3a0e-43cd-8b8f-b29487cfdcf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014nR7xqty64xP2yb96QFTZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 26136,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 549
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

_source line 13 · 2026-05-15T12:35:59.340Z_

<details><summary>↩ Tool result · `toolu_01K7ErCaN2iMF2x6x9cLqgoz`</summary>

```text
1	% EMNLP 2026 ARR Submission — ACL 2023 Template
2	\documentclass[11pt]{article}
3	\usepackage[review]{acl}
4	\usepackage{times}
5	\usepackage{latexsym}
6	\usepackage{graphicx}
7	\usepackage{booktabs}
8	\usepackage{enumitem}
9	\usepackage{amsmath}
10	
11	\graphicspath{{../chart/}}
12	
13	\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\in Non-Paraphrastic LLM Text Chains}
14	
15	\author{Anonymous}
16	
17	\begin{document}
18	\maketitle
19	
20	\begin{abstract}
21	As large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
22	We formulate \emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.
23	Existing detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.
24	We characterize a \emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.
25	Combining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\,=\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.
26	In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\,pp vs.\ 18--26\,pp for single detectors).
27	A complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.
28	\end{abstract}
29	
30	\input{introduction}
31	\input{related_work}
32	\input{method}
33	\input{results}
34	
35	\input{discussion}
36	\input{conclusion}
37	\input{limitations}
38	\input{ethics}
39	
40	\bibliography{references}
41	
42	\appendix
43	\section{Length Confound Analysis}
44	\label{app:length}
45	\input{appendix_length}
46	
47	\section{Prompt Type Generalization}
48	\label{app:prompt-type}
49	\input{appendix_prompt_type}
50	
51	\section{Finer-Grained Depth Classification}
52	\label{app:finer-depth}
53	\input{appendix_finer_depth}
54	
55	\section{Leave-One-Feature-Out Analysis}
56	\label{app:lofo}
57	\input{appendix_lofo}
58	
59	\section{Confusion Matrix}
60	\label{app:confusion}
61	\input{appendix_confusion_matrix}
62	
63	\section{Classifier Sensitivity}
64	\label{app:classifier}
65	\input{appendix_classifier}
66	
67	\end{document}
68	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "5784c5ba-e85d-40ca-8546-c51b4315c8b2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
      "content": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\\\in Non-Paraphrastic LLM Text Chains}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nAs large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.\nExisting detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.\nWe characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.\nCombining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.\nIn leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nA complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\section{Length Confound Analysis}\n\\label{app:length}\n\\input{appendix_length}\n\n\\section{Prompt Type Generalization}\n\\label{app:prompt-type}\n\\input{appendix_prompt_type}\n\n\\section{Finer-Grained Depth Classification}\n\\label{app:finer-depth}\n\\input{appendix_finer_depth}\n\n\\section{Leave-One-Feature-Out Analysis}\n\\label{app:lofo}\n\\input{appendix_lofo}\n\n\\section{Confusion Matrix}\n\\label{app:confusion}\n\\input{appendix_confusion_matrix}\n\n\\section{Classifier Sensitivity}\n\\label{app:classifier}\n\\input{appendix_classifier}\n\n\\end{document}\n",
      "numLines": 68,
      "startLine": 1,
      "totalLines": 68
    }
  }
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01XumRLwPomHZyFp73p2qcJM`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "7268bebb-2491-41b0-a8f5-73f94fa5b0c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ym7ddVViha7v15ZawZ98N",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1109,
      "cache_read_input_tokens": 26685,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1109
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

_source line 15 · 2026-05-15T12:36:02.843Z_

<details><summary>↩ Tool result · `toolu_01XumRLwPomHZyFp73p2qcJM`</summary>

```text
1	% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains
2	\begin{abstract}
3	As large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.
4	We formulate \emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.
5	Existing detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.
6	We characterize a \emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.
7	Combining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\,=\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.
8	In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\,pp vs.\ 18--26\,pp for single detectors).
9	A complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.
10	\end{abstract}
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "0e3ede63-1d74-4b05-8a4b-1e000a01c022",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
      "content": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.\nExisting detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.\nWe characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.\nCombining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.\nIn leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nA complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{abstract}\n",
      "numLines": 11,
      "startLine": 1,
      "totalLines": 11
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_018E99kXVBeEcQseC9sNrYda`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "2d86f5ab-130d-4c3e-a430-b6d9d0d8e354",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPDfxHYzy7s24LUUy69PKD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 576,
      "cache_read_input_tokens": 27794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 576
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

_source line 17 · 2026-05-15T12:36:05.434Z_

<details><summary>↩ Tool result · `toolu_018E99kXVBeEcQseC9sNrYda`</summary>

```text
1	\section{Results}
2	\label{sec:results}
3	
4	We evaluate depth fingerprinting along four axes: cross-generator classification (\S\ref{sec:results-classification}), differential depth response of individual features (\S\ref{sec:results-differential}), comparison with existing detection baselines (\S\ref{sec:results-baselines}), and downstream utility for data curation (\S\ref{sec:results-downstream}).
5	
6	\subsection{Depth Classification Performance}
7	\label{sec:results-classification}
8	
9	Table~\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\,/\,gen-1\,/\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.
10	
11	The 7-feature ensemble achieves LOGO F1\,=\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \S\ref{sec:results-baselines}).
12	Per-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).
13	Per-class F1 varies by depth: gen-0\,=\,0.94, gen-2+\,=\,0.80, gen-1\,=\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.
14	
15	\paragraph{Cross-scale transfer.}
16	The six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\leq$2.8B training generators.
17	However, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\,=\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\leq$2.8B generators.
18	Text generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.
19	Notably, adding Qwen3-8B data \emph{improves} classification on the original five generators (+1.1\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.
20	We note that this gap may narrow with scale-matched training data; our current dataset contains $\sim$1{,}000 samples per generator regardless of scale.
21	
22	\paragraph{Cross-family generalization.}
23	Leave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\Delta$\,=\,$-$2.6\,pp vs.\ LOGO).
24	
25	\paragraph{Length confound control.}
26	Text length correlates weakly with depth (Spearman $|\rho| < 0.14$).
27	Length-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\Delta$\,=\,+0.041), ruling out length as a confound (Appendix~\ref{app:length}).
28	
29	
30	\begin{table}[t]
31	\centering
32	\small
33	\begin{tabular}{llccc}
34	\toprule
35	\textbf{Generator} & \textbf{Family} & \textbf{Params} & \textbf{Held-out F1} & \textbf{95\% CI} \\
36	\midrule
37	Pythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\
38	Pythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\
39	OLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\
40	Qwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\
41	Qwen3-1.7B     & Qwen   & 1.7B & 0.805 & [0.796, 0.817] \\
42	Qwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\
43	\midrule
44	\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\
45	\multicolumn{3}{l}{5-gen LOGO (excl.\ Qwen3-8B)} & 0.800 & --- \\
46	\bottomrule
47	\end{tabular}
48	\caption{Leave-one-generator-out macro-F1 with bootstrap 95\% confidence intervals ($n$\,=\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}
49	\label{tab:logo-results}
50	\end{table}
51	
52	
53	\subsection{Differential Depth Response}
54	\label{sec:results-differential}
55	
56	Features exhibit \emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.
57	This pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).
58	
59	\begin{figure}[t]
60	\centering
61	\includegraphics[width=\columnwidth]{fig1_differential_response.pdf}
62	\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}
63	\label{fig:feature-drift}
64	\end{figure}
65	
66	Individual-level Spearman correlations with depth confirm the split (Figure~\ref{fig:feature-drift}):
67	drifting features show strong monotonic trends (hapax ratio $\rho = -0.558$, TTR $\rho = -0.542$, entropy mean $\rho = -0.475$),
68	while shape features show weak or negligible correlations (entropy std $|\rho| = 0.076$, tail decay $|\rho| = 0.089$).
69	
70	\paragraph{Feature complementarity.}
71	Table~\ref{tab:ablation} reports ablation results.
72	The full 7-feature set (F1\,=\,0.789) significantly outperforms both surface-only features (TTR, hapax\_ratio; F1\,=\,0.729) and reference-only features (entropy mean/std/max/min, tail\_decay; F1\,=\,0.745; McNemar $p \approx 0$).
73	Permutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).
74	Surface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.
75	
76	\paragraph{Cross-family reference models.}
77	To confirm that differential depth response is not an artifact of the Pythia-410M reference model, we compute features using three cross-family references: Pythia-410M, OLMo-2-1B, and Qwen3-0.6B.
78	All three achieve LOGO F1 between 0.80 and 0.82, with consistent drift directions across features.
79	The pattern generalizes across reference model architectures.
80	
81	
82	\begin{table}[t]
83	\centering
84	\small
85	\begin{tabular}{lcc}
86	\toprule
87	\textbf{Feature set} & \textbf{LOGO F1} & \textbf{Top feature (importance)} \\
88	\midrule
89	Full (7 features)     & 0.789 & hapax\_ratio (0.269) \\
90	Surface only (2)      & 0.729 & hapax\_ratio (0.320) \\
91	Reference only (5)    & 0.745 & entropy\_mean (0.218) \\
92	\bottomrule
93	\end{tabular}
94	\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}
95	\label{tab:ablation}
96	\end{table}
97	
98	Leave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\_max showing the largest marginal impact despite modest split frequency (Appendix~\ref{app:lofo}).
99	
100	
101	\subsection{Comparison with Detection Baselines}
102	\label{sec:results-baselines}
103	
104	\begin{figure}[t]
105	\centering
106	\includegraphics[width=\columnwidth]{fig3_baseline_comparison.png}
107	\caption{LOGO macro-F1 with 95\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\,pp; the ensemble CI spans 1.4\,pp.}
108	\label{fig:baseline-ci}
109	\end{figure}
110	
111	We repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\ref{fig:baseline-ci}).
112	
113	\begin{table}[t]
114	\centering
115	\small
116	\begin{tabular}{lcc}
117	\toprule
118	\textbf{Method} & \textbf{LOGO F1} & \textbf{95\% CI} \\
119	\midrule
120	7-feature ensemble & \textbf{0.800} & [0.786, 0.800] \\
121	Avg-LogProb        & 0.765 & [0.616, 0.820] \\
122	LD-Score            & 0.721 & [0.588, 0.770] \\
123	FastDetectGPT       & 0.627 & [0.511, 0.762] \\
124	Binoculars          & 0.579 & [0.405, 0.664] \\
125	\bottomrule
126	\end{tabular}
127	\caption{Ordinal depth classification: 7-feature ensemble vs.\ single detection baselines (5-gen LOGO). The ensemble outperforms the best single detector (Avg-LogProb) by +3.5\,pp (paired bootstrap $p < 0.001$, $\Delta$ CI [3.0, 4.0]).}
128	\label{tab:baselines}
129	\end{table}
130	
131	The ensemble outperforms all baselines in mean F1: +3.5\,pp over Avg-LogProb ($p < 0.001$, $\Delta$ CI [3.0, 4.0]), +7.9\,pp over LD-Score, +17.3\,pp over FastDetectGPT, and +22.1\,pp over Binoculars (Table~\ref{tab:baselines}).
132	
133	The critical distinction is \emph{reliability}.
134	The ensemble CI spans just 1.4\,pp [0.786, 0.800], while single-detector CIs span 18--26\,pp (e.g., Avg-LogProb [0.616, 0.820]).
135	A single detector's CI is wider than \emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.
136	Each detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.
137	The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.
138	
139	
140	\subsection{Downstream Utility: A Negative Finding}
141	\label{sec:results-downstream}
142	
143	Can depth-aware data curation improve downstream language model quality?
144	We fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\ref{tab:downstream}).
145	
146	\begin{table}[t]
147	\centering
148	\small
149	\begin{tabular}{lrc}
150	\toprule
151	\textbf{Variant} & \textbf{$n$} & \textbf{Test PPL} \\
152	\midrule
153	All depths            & 12{,}299 & 2.335 $\pm$ 0.000 \\
154	Size-matched (random) & 3{,}951  & 2.367 $\pm$ 0.000 \\
155	Depth 0--1 only       & 3{,}951  & 2.387 $\pm$ 0.001 \\
156	Binary-filtered       & 3{,}951  & 2.389 $\pm$ 0.000 \\
157	Depth 0 only          & 797      & 2.681 $\pm$ 0.001 \\
158	\bottomrule
159	\end{tabular}
160	\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}
161	\label{tab:downstream}
162	\end{table}
163	
164	The results are unambiguous: data quantity dominates depth composition.
165	Training on all 12{,}299 samples yields the lowest perplexity (2.335).
166	At equal sample count ($n$\,=\,3{,}951), random subsampling (2.367) \emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).
167	Cross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.
168	
169	Restricting training to human-only text (depth 0, $n$\,=\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\times$ reduction in data volume rather than depth composition per se.
170	
171	We report this negative finding transparently: depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data curation.
172	Knowing the generation depth of a document does not, by itself, make it more or less useful for training.
173	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "eee9447a-9742-4e81-a3bc-4d226230b10c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
      "content": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nTable~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\n\nThe 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).\nPer-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).\nPer-class F1 varies by depth: gen-0\\,=\\,0.94, gen-2+\\,=\\,0.80, gen-1\\,=\\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.\n\n\\paragraph{Cross-scale transfer.}\nThe six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.\nHowever, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\\leq$2.8B generators.\nText generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.\nNotably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+1.1\\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.\nWe note that this gap may narrow with scale-matched training data; our current dataset contains $\\sim$1{,}000 samples per generator regardless of scale.\n\n\\paragraph{Cross-family generalization.}\nLeave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\\Delta$\\,=\\,$-$2.6\\,pp vs.\\ LOGO).\n\n\\paragraph{Length confound control.}\nText length correlates weakly with depth (Spearman $|\\rho| < 0.14$).\nLength-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 & [0.796, 0.817] \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\\\\n\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.800 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-generator-out macro-F1 with bootstrap 95\\% confidence intervals ($n$\\,=\\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}\n\\label{tab:logo-results}\n\\end{table}\n\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nIndividual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).\n\n\\paragraph{Feature complementarity.}\nTable~\\ref{tab:ablation} reports ablation results.\nThe full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR, hapax\\_ratio; F1\\,=\\,0.729) and reference-only features (entropy mean/std/max/min, tail\\_decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).\nSurface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.\n\n\\paragraph{Cross-family reference models.}\nTo confirm that differential depth response is not an artifact of the Pythia-410M reference model, we compute features using three cross-family references: Pythia-410M, OLMo-2-1B, and Qwen3-0.6B.\nAll three achieve LOGO F1 between 0.80 and 0.82, with consistent drift directions across features.\nThe pattern generalizes across reference model architectures.\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\\n\\midrule\nFull (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\\nSurface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\\nReference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}\n\\label{tab:ablation}\n\\end{table}\n\nLeave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nWe repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\\ref{fig:baseline-ci}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.800} & [0.786, 0.800] \\\\\nAvg-LogProb        & 0.765 & [0.616, 0.820] \\\\\nLD-Score            & 0.721 & [0.588, 0.770] \\\\\nFastDetectGPT       & 0.627 & [0.511, 0.762] \\\\\nBinoculars          & 0.579 & [0.405, 0.664] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal depth classification: 7-feature ensemble vs.\\ single detection baselines (5-gen LOGO). The ensemble outperforms the best single detector (Avg-LogProb) by +3.5\\,pp (paired bootstrap $p < 0.001$, $\\Delta$ CI [3.0, 4.0]).}\n\\label{tab:baselines}\n\\end{table}\n\nThe ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).\n\nThe critical distinction is \\emph{reliability}.\nThe ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nA single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.\nEach detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.\nThe 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n\nCan depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\nWe report this negative finding transparently: depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data curation.\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training.\n",
      "numLines": 173,
      "startLine": 1,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01PogCYmMPvRKzGsUqx3Bod5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "0ff8b385-d402-4155-b92c-88e389fc3a15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LNwob3HFfK7UuUmtJuZqX3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4102,
      "cache_read_input_tokens": 28370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4102
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

_source line 19 · 2026-05-15T12:36:09.230Z_

<details><summary>↩ Tool result · `toolu_01PogCYmMPvRKzGsUqx3Bod5`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why are shape features stationary?}
5	Distributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\S\ref{sec:results-differential}).
6	One \emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.
7	Recursive generation shifts \emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \emph{how} the model distributes probability mass around its predictions.
8	If this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.
9	We flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.
10	
11	\paragraph{Relation to OOD detection.}
12	Reference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \cite{detectgpt}, GLTR \cite{gltr}, and Binoculars \cite{binoculars}.
13	Our contribution is not these features per se, but the \emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.
14	This connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \cite{ood_baseline}.
15	Recursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.
16	
17	\paragraph{Practical implications.}
18	The differential depth response enables risk-stratified data curation.
19	Rather than binary keep-or-discard filtering, practitioners can flag gen-2+ text for manual review while retaining gen-1 content that preserves much of the source distribution's properties.
20	Three-class granularity is well-suited to this use case: it separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to curation decisions.
21	Finer-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\sim$3 steps \cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.
22	The tight cross-generator consistency of the ensemble (CI width 1.4\,pp) makes deployment feasible even when the generating model is unknown.
23	
24	\paragraph{Information value of the negative finding.}
25	Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\S\ref{sec:results-downstream}).
26	This negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.
27	The dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \cite{self_consuming_mad}.
28	
29	\paragraph{Connection to model collapse.}
30	Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
31	Model collapse describes distributional degradation when models are \emph{retrained} on their own outputs across generations.
32	We observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \emph{inference chains} without any parameter updates.
33	This suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.
34	The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "762c66fd-2d4b-4c5b-9eb2-5d94b903d4db",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why are shape features stationary?}\nDistributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nOne \\emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.\nRecursive generation shifts \\emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \\emph{how} the model distributes probability mass around its predictions.\nIf this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.\nWe flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.\n\n\\paragraph{Relation to OOD detection.}\nReference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nOur contribution is not these features per se, but the \\emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.\nThis connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nRecursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.\n\n\\paragraph{Practical implications.}\nThe differential depth response enables risk-stratified data curation.\nRather than binary keep-or-discard filtering, practitioners can flag gen-2+ text for manual review while retaining gen-1 content that preserves much of the source distribution's properties.\nThree-class granularity is well-suited to this use case: it separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to curation decisions.\nFiner-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\\sim$3 steps \\cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.\nThe tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.\n\n\\paragraph{Information value of the negative finding.}\nDepth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nThis negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.\nThe dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\n\n\\paragraph{Connection to model collapse.}\nOur results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nModel collapse describes distributional degradation when models are \\emph{retrained} on their own outputs across generations.\nWe observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.\nThis suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.\nThe shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n",
      "numLines": 35,
      "startLine": 1,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_0149Fg7aNF8fySCCi85jUH1s`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "c3afed23-2b9f-4aac-ba43-e206af773e72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014CkE3dAYyaHm8rULNdgPHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1102,
      "cache_read_input_tokens": 32472,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1102
      },
      "output_tokens": 35,
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

_source line 21 · 2026-05-15T12:36:12.438Z_

<details><summary>↩ Tool result · `toolu_0149Fg7aNF8fySCCi85jUH1s`</summary>

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
15	No existing method addresses this task directly.
16	When repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---confidence intervals spanning 0.41--0.82 in macro-F1 (\S\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.
17	Concurrent work on iterative paraphrasing chains \cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.
18	These results do not extend to \emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.
19	
20	We study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).
21	Our central empirical finding is \emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.
22	This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.
23	The combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.
24	This ensemble maintains tight cross-generator consistency (CI width 1.4\,pp), whereas the best single detector spans over 20\,pp.
25	The practical advantage is reliability across unknown generators, not just average performance.
26	
27	We also report a negative finding.
28	Depth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\ 2.387 depth-stratified).
29	Depth fingerprinting is an effective \emph{diagnostic} tool for characterizing text provenance, not a \emph{curative} tool for data selection.
30	
31	Our contributions are:
32	\begin{enumerate}[nosep,leftmargin=*]
33	    \item \textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.
34	    \item \textbf{Empirical characterization.} We document differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves LOGO F1\,=\,0.79, significantly outperforming all single-detector baselines ($p < 0.001$) with tight cross-generator consistency.
35	    \item \textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.
36	\end{enumerate}
37	
38	The remainder of this paper is organized as follows.
39	\S\ref{sec:related} surveys related work on text detection, model collapse, and data quality.
40	\S\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.
41	\S\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.
42	\S\ref{sec:discussion} discusses limitations and future directions.
43	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "3f78ef4a-1612-4f15-a7a3-b98c452dcd68",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nNo existing method addresses this task directly.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---confidence intervals spanning 0.41--0.82 in macro-F1 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nOur central empirical finding is \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.\nThis ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.\nThe practical advantage is reliability across unknown generators, not just average performance.\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nDepth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We document differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves LOGO F1\\,=\\,0.79, significantly outperforming all single-detector baselines ($p < 0.001$) with tight cross-generator consistency.\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses limitations and future directions.\n",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01MULSPBqeut1sUEBQ9WckiH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ccd5839b-efae-4fcf-a946-08b39a98f5fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mMzrZdHrqSAVbJpHGEavG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1583,
      "cache_read_input_tokens": 33574,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1583
      },
      "output_tokens": 35,
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

_source line 23 · 2026-05-15T12:36:16.616Z_

<details><summary>↩ Tool result · `toolu_01MULSPBqeut1sUEBQ9WckiH`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task Formulation}
5	\label{sec:task}
6	
7	Given a text $x$, the goal is to predict its \emph{generation depth} $d \in \{0, 1, 2{+}\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.
8	Formally, let $\mathcal{C}_0$ be a reference corpus of human-written text.
9	A generation chain of depth $k$ is defined recursively: $x^{(0)} \sim \mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.
10	We frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.
11	Depths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\S\ref{sec:results-differential}).
12	
13	\subsection{Generation Chain Construction}
14	\label{sec:generation}
15	
16	We construct generation chains using six generators spanning three model families: \textbf{Pythia} (2.8B, 1B) \cite{pythia}, \textbf{OLMo} (OLMo-2-1B) \cite{olmo}, and \textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \cite{qwen3}.
17	This selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.
18	
19	For each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\mathcal{C}_0$.
20	Each seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\texttt{Continue the following text: \{text\}}''.
21	All generation uses temperature $\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.
22	The resulting dataset contains approximately 27{,}000 texts across all generators and depths.
23	For classification, depths 2--4 are collapsed into the $2{+}$ class.
24	
25	\subsection{Feature Extraction}
26	\label{sec:features}
27	
28	The seven features are motivated by two complementary views of distributional drift.
29	Reference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.
30	Together, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).
31	This two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\S\ref{sec:results-differential}).
32	
33	We extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.
34	
35	\paragraph{Reference-model features.}
36	A held-out reference model (Pythia-410M, chosen to be smaller than and architecturally independent of all generators) computes per-token negative log-likelihood (NLL) for each text.
37	From the resulting NLL sequence, we extract five statistics:
38	\begin{itemize}[nosep,leftmargin=*]
39	    \item \textbf{entropy\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;
40	    \item \textbf{entropy\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;
41	    \item \textbf{entropy\_max}: maximum token-level NLL, capturing the most surprising token;
42	    \item \textbf{entropy\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs;
43	    \item \textbf{tail\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.
44	\end{itemize}
45	
46	\paragraph{Surface features.}
47	Two features capture lexical diversity without requiring a reference model:
48	\begin{itemize}[nosep,leftmargin=*]
49	    \item \textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);
50	    \item \textbf{hapax\_ratio}: proportion of words appearing exactly once (\emph{hapax legomena}).
51	\end{itemize}
52	
53	\paragraph{Feature complementarity.}
54	The grouping reflects an empirical pattern we term \emph{differential depth response}: central-tendency and diversity features (entropy\_mean, TTR, hapax\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\_std, tail\_decay) remain near-stationary.
55	This differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.
56	As shown in \S\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.
57	
58	\subsection{Evaluation Protocol}
59	\label{sec:evaluation}
60	
61	\paragraph{Cross-validation.}
62	To evaluate generalization to unseen generators, we use \textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.
63	We additionally report \textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.
64	
65	\paragraph{Classifier.}
66	We use XGBoost \cite{xgboost} as the classifier throughout.
67	Gradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.
68	We use $n\_\text{estimators}{=}200$, $\max\_\text{depth}{=}6$, and learning rate $0.1$ throughout all experiments, including baseline comparisons, to ensure a controlled comparison.
69	LOGO F1 is stable across random seeds (mean\,=\,0.789, std\,=\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.
70	Alternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.
71	
72	\paragraph{Metrics and statistical testing.}
73	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
74	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).
75	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
76	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
77	All reported $p$-values are two-sided.
78	
79	\paragraph{Baselines.}
80	We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \cite{fast_detectgpt}, Binoculars \cite{binoculars}, and LD-Score \cite{ld_score}.
81	Each baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.
82	
83	\paragraph{Length confound control.}
84	Since TTR and hapax\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.
85	We conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.
86	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e3460d9b-01b6-48e1-908d-a7256be604ae",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than and architecturally independent of all generators) computes per-token negative log-likelihood (NLL) for each text.\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ throughout all experiments, including baseline comparisons, to ensure a controlled comparison.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
      "numLines": 86,
      "startLine": 1,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

Now I have all the context. Let me also check the docs/paper directory structure and search for any remaining occurrences.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "09dc0c02-cece-4a67-ab9f-b9901fce6d32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rs9XLrrAD7cTTDTYotr3yA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2387,
      "cache_read_input_tokens": 35157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2387
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

_source line 25_

<details open><summary>🔧 Tool call — Glob · `toolu_01J1W7bNUPwZDW4eprFmQQiY`</summary>

```json
{
  "pattern": "docs/paper/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "1042a5a3-a61c-4fb8-ab4f-349ac7731d7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rs9XLrrAD7cTTDTYotr3yA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2387,
      "cache_read_input_tokens": 35157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2387
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

_source line 26 · 2026-05-15T12:36:20.606Z_

<details><summary>↩ Tool result · `toolu_01J1W7bNUPwZDW4eprFmQQiY`</summary>

```text
docs/paper/discussion.tex
docs/paper/conclusion.tex
docs/paper/ethics.tex
docs/paper/appendix_length.tex
docs/paper/appendix_prompt_type.tex
docs/paper/appendix_finer_depth.tex
docs/paper/appendix_confusion_matrix.tex
docs/paper/appendix_classifier.tex
docs/paper/appendix_lofo.tex
docs/paper/results.tex
docs/paper/related_work.tex
docs/paper/introduction.tex
docs/paper/abstract.tex
docs/paper/main.tex
docs/paper/method.tex
docs/paper/limitations.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "895d96d9-22db-4a37-b00c-c58b192b952b",
  "tool_use_result": {
    "filenames": [
      "docs/paper/discussion.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/ethics.tex",
      "docs/paper/appendix_length.tex",
      "docs/paper/appendix_prompt_type.tex",
      "docs/paper/appendix_finer_depth.tex",
      "docs/paper/appendix_confusion_matrix.tex",
      "docs/paper/appendix_classifier.tex",
      "docs/paper/appendix_lofo.tex",
      "docs/paper/results.tex",
      "docs/paper/related_work.tex",
      "docs/paper/introduction.tex",
      "docs/paper/abstract.tex",
      "docs/paper/main.tex",
      "docs/paper/method.tex",
      "docs/paper/limitations.tex"
    ],
    "durationMs": 16,
    "numFiles": 16,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HSa4hid4SdkyJZAMke5Ldv`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "95de9904-482a-413d-bb90-db63582316a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012pyo8WB1PrridU9cTCCUFu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 37544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 250
      },
      "output_tokens": 33,
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

_source line 28 · 2026-05-15T12:36:22.997Z_

<details><summary>↩ Tool result · `toolu_01HSa4hid4SdkyJZAMke5Ldv`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e2bbfcdc-609c-4498-bc14-314ff9338158",
  "tool_use_result": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 27
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Let me organize the work and track progress. I need to:

1. W11 — Update CI width from 1.4pp to 0.9pp across all .tex files
2. W3 — Add topic drift paragraph to discussion.tex
3. Class-balanced annotation in method.tex
4. Sync to docs/paper/
5. Git commits for each

Let me set up the todo list and start working.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "93def985-48e5-4156-87f9-f59bb56ce296",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018szULszhzg1LWh6X1neTZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 37794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2466
      },
      "output_tokens": 17,
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

_source line 30_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Ssgc3LWGhxJ5hdmfsr4qHi`</summary>

```json
{
  "todos": [
    {
      "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
      "status": "in_progress",
      "activeForm": "Updating CI width and values across all .tex files"
    },
    {
      "content": "W3: Add topic drift paragraph to discussion.tex",
      "status": "pending",
      "activeForm": "Adding topic drift paragraph to discussion.tex"
    },
    {
      "content": "W3: Add class-balanced annotation to method.tex",
      "status": "pending",
      "activeForm": "Adding class-balanced annotation to method.tex"
    },
    {
      "content": "Sync modified files to docs/paper/",
      "status": "pending",
      "activeForm": "Syncing modified files to docs/paper/"
    },
    {
      "content": "Git commits for each change",
      "status": "pending",
      "activeForm": "Creating git commits"
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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "7912f125-0e95-4b9f-ba39-21ed03b27a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018szULszhzg1LWh6X1neTZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 37794,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2466
      },
      "output_tokens": 17,
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

_source line 31 · 2026-05-15T12:36:30.866Z_

<details><summary>↩ Tool result · `toolu_01Ssgc3LWGhxJ5hdmfsr4qHi`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "f15426d9-e312-4558-b848-0fd4737857be",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "in_progress",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "pending",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "pending",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 32_

Starting W11. I found "1.4" in 6 locations across tex files. Two are false positives (appendix_prompt_type.tex "1.4%" elaboration rate, and table4.tex "$-$1.40" log-prob value). The 4 real hits plus the CI values need updating.

Let me make all the W11 edits now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "d314104b-3c5b-4a1e-90c7-f8cbf7a1bdf3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTyyyyhnGBGBK4rNnnM4Sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 40260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_017gA6PPCxYQARmQoPQ7RpuR`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
  "old_string": "with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
  "new_string": "with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "9079d172-58d7-4db3-8609-23eae351af06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PTyyyyhnGBGBK4rNnnM4Sc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 402,
      "cache_read_input_tokens": 40260,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 402
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

_source line 34 · 2026-05-15T12:36:39.342Z_

<details><summary>↩ Tool result · `toolu_017gA6PPCxYQARmQoPQ7RpuR`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "7076288c-744a-450d-8496-424e70d4eb69",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/main.tex",
    "oldString": "with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
    "newString": "with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors).",
    "originalFile": "% EMNLP 2026 ARR Submission — ACL 2023 Template\n\\documentclass[11pt]{article}\n\\usepackage[review]{acl}\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{amsmath}\n\n\\graphicspath{{../chart/}}\n\n\\title{Depth Fingerprinting: Ordinal Generation Depth Estimation\\\\in Non-Paraphrastic LLM Text Chains}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\begin{abstract}\nAs large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.\nExisting detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.\nWe characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.\nCombining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.\nIn leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nA complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{results}\n\n\\input{discussion}\n\\input{conclusion}\n\\input{limitations}\n\\input{ethics}\n\n\\bibliography{references}\n\n\\appendix\n\\section{Length Confound Analysis}\n\\label{app:length}\n\\input{appendix_length}\n\n\\section{Prompt Type Generalization}\n\\label{app:prompt-type}\n\\input{appendix_prompt_type}\n\n\\section{Finer-Grained Depth Classification}\n\\label{app:finer-depth}\n\\input{appendix_finer_depth}\n\n\\section{Leave-One-Feature-Out Analysis}\n\\label{app:lofo}\n\\input{appendix_lofo}\n\n\\section{Confusion Matrix}\n\\label{app:confusion}\n\\input{appendix_confusion_matrix}\n\n\\section{Classifier Sensitivity}\n\\label{app:classifier}\n\\input{appendix_classifier}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " Existing detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.",
          " We characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.",
          " Combining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.",
          "-In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
          "+In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors).",
          " A complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.",
          " \\end{abstract}",
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

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_013xuK4X7TacgMfBHF9vaY1i`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
  "old_string": "with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
  "new_string": "with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e10872d7-266e-49ea-9ce8-ccaa70befc6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017i6Pyh1UgLmEnD7Z8gmJ6u",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 352,
      "cache_read_input_tokens": 40662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 352
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

_source line 36 · 2026-05-15T12:36:43.279Z_

<details><summary>↩ Tool result · `toolu_013xuK4X7TacgMfBHF9vaY1i`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6cce24d5-9642-432e-8d6d-58c16e1cc048",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/abstract.tex",
    "oldString": "with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
    "newString": "with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors).",
    "originalFile": "% Abstract — Depth Fingerprinting of Recursive LLM Generation Chains\n\\begin{abstract}\nAs large language model (LLM) outputs accumulate on the web, training corpora increasingly contain recursively generated text of unknown provenance depth.\nWe formulate \\emph{ordinal depth estimation}---classifying whether text is human-written (gen-0), first-generation synthetic (gen-1), or deeper (gen-2+)---a task that moves beyond binary real-versus-synthetic detection.\nExisting detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.\nWe characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.\nCombining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.\nIn leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).\nA complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.\n\\end{abstract}\n",
    "structuredPatch": [
      {
        "oldStart": 5,
        "oldLines": 6,
        "newStart": 5,
        "newLines": 6,
        "lines": [
          " Existing detectors provide only binary scores and, when repurposed for ordinal prediction, exhibit high cross-generator variance (confidence intervals spanning 0.41--0.82), making them unreliable depth estimators.",
          " We characterize a \\emph{differential depth response} in distributional features computed under a held-out reference model: central-tendency and diversity features (entropy mean, type-token ratio, hapax ratio) drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay rate) remain near-stationary.",
          " Combining both feature types into a 7-feature ensemble exploits this complementarity: the full set (macro-F1\\,=\\,0.79) outperforms surface-only (0.73) and reference-only (0.75) subsets.",
          "-In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width 1.4\\,pp vs.\\ 18--26\\,pp for single detectors).",
          "+In leave-one-generator-out evaluation across 6 generators from 3 model families (0.6B--8.2B parameters), the ensemble achieves macro-F1 of 0.79 ($p < 0.001$ vs.\\ all single-detector baselines) with tight cross-generator consistency (CI width $<$\\,1\\,pp vs.\\ 18--26\\,pp for single detectors).",
          " A complementary analysis shows that depth-aware data curation does not outperform random subsampling---data quantity dominates depth composition---positioning depth fingerprinting as a diagnostic tool for provenance characterization, not a curative tool for data selection.",
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

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_011k3yDyawy5494Ukr8odJ8k`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
  "old_string": "This ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.",
  "new_string": "This ensemble maintains tight cross-generator consistency (CI width $<$\\,1\\,pp), whereas the best single detector spans over 20\\,pp."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "dabee196-5a89-4aa0-ba6b-addeb704551b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017u7wxNQR5Hqme7jXPN8yEx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 41014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 38 · 2026-05-15T12:36:48.423Z_

<details><summary>↩ Tool result · `toolu_011k3yDyawy5494Ukr8odJ8k`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "3f3df548-3d5a-419d-986b-0a628c908370",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/introduction.tex",
    "oldString": "This ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.",
    "newString": "This ensemble maintains tight cross-generator consistency (CI width $<$\\,1\\,pp), whereas the best single detector spans over 20\\,pp.",
    "originalFile": "\\section{Introduction}\n\\label{sec:introduction}\n\nWeb-crawled corpora are the dominant source of pretraining data for large language models (LLMs), yet an increasing fraction of this data is itself LLM-generated.\nEstimates suggest that 7--17\\% of recent scientific papers and peer reviews contain substantial LLM-modified content \\cite{mapping_llm_science,monitoring_ai_review}, and this proportion continues to grow as generated text enters the web and becomes seed material for subsequent generation.\nThe result is recursive generation chains whose outputs progressively diverge from human-written text---a problem that current detection methods are ill-equipped to address.\n\nExisting detectors \\cite{fast_detectgpt,binoculars,ld_score,detectgpt} provide binary real-vs-synthetic classification, forcing an all-or-nothing filtering decision: discard everything flagged as synthetic, losing potentially useful first-generation content, or retain everything, admitting text with compounding distributional drift.\nThis conflates qualitatively different material.\nA first-generation continuation---an LLM expanding a human-written passage---retains much of the source distribution's lexical and structural properties.\nA third- or fourth-generation text, conditioned recursively on prior LLM outputs, exhibits measurably reduced vocabulary diversity, compressed perplexity, and narrower token probability distributions.\nTreating these as a single ``synthetic'' category discards provenance information that could inform risk-stratified curation decisions.\n\nWe argue that a finer-grained characterization is needed: \\emph{ordinal depth estimation}, the task of classifying text into generation depth classes (gen-0\\,/\\,gen-1\\,/\\,gen-2+) rather than producing a binary label.\nNo existing method addresses this task directly.\nWhen repurposed as ordinal depth predictors, individual detection scores exhibit high cross-generator variance---confidence intervals spanning 0.41--0.82 in macro-F1 (\\S\\ref{sec:results-baselines})---making any single detector unreliable across unknown generators.\nConcurrent work on iterative paraphrasing chains \\cite{broken_telephone,markovian_chains} analyzes convergence behavior under semantic-preservation constraints, which bound distinguishable depth classes to approximately three.\nThese results do not extend to \\emph{non-paraphrastic} generation chains (e.g., continuation), where the absence of semantic anchoring permits richer depth signal.\n\nWe study distributional drift in non-paraphrastic LLM generation chains across six generators from three model families (Pythia, OLMo, Qwen; 0.6B--8.2B parameters).\nOur central empirical finding is \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.\nThe combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.\nThis ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.\nThe practical advantage is reliability across unknown generators, not just average performance.\n\nWe also report a negative finding.\nDepth-aware data curation---selecting training data based on estimated generation depth---does not improve downstream language model quality compared to random subsampling at equal sample count (perplexity: 2.367 random vs.\\ 2.387 depth-stratified).\nDepth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data selection.\n\nOur contributions are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Task formulation.} We define ordinal generation depth estimation as a task beyond binary detection, providing a framework for finer-grained provenance characterization of web-crawled text.\n    \\item \\textbf{Empirical characterization.} We document differential depth response across six generators spanning three model families (0.6B--8.2B): a 7-feature ensemble combining drifting and stationary features achieves LOGO F1\\,=\\,0.79, significantly outperforming all single-detector baselines ($p < 0.001$) with tight cross-generator consistency.\n    \\item \\textbf{Complementary analysis.} As a complementary analysis, we show that depth-aware data curation does not improve downstream language model quality compared to random subsampling, establishing depth fingerprinting as a diagnostic rather than curative tool.\n\\end{enumerate}\n\nThe remainder of this paper is organized as follows.\n\\S\\ref{sec:related} surveys related work on text detection, model collapse, and data quality.\n\\S\\ref{sec:method} describes generation chain construction, feature extraction, and evaluation protocol.\n\\S\\ref{sec:results} presents classification results, differential depth response analysis, baseline comparisons, and the downstream utility experiment.\n\\S\\ref{sec:discussion} discusses limitations and future directions.\n",
    "structuredPatch": [
      {
        "oldStart": 21,
        "oldLines": 7,
        "newStart": 21,
        "newLines": 7,
        "lines": [
          " Our central empirical finding is \\emph{differential depth response}: central-tendency and diversity features---including reference-model mean entropy (functionally an NLL-based out-of-distribution score \\cite{ood_baseline}), type-token ratio, and hapax ratio---drift monotonically with generation depth, while distributional shape features (entropy standard deviation, tail decay) remain near-stationary.",
          " This pattern is consistent with recursive generation inducing a location shift in the NLL distribution: text becomes progressively more predictable on average while the functional form of the distribution is preserved.",
          " The combination of drifting and stationary features yields a 7-feature ensemble that achieves leave-one-generator-out (LOGO) macro-F1 of 0.79, with per-generator held-out F1 ranging from 0.68 to 0.86.",
          "-This ensemble maintains tight cross-generator consistency (CI width 1.4\\,pp), whereas the best single detector spans over 20\\,pp.",
          "+This ensemble maintains tight cross-generator consistency (CI width $<$\\,1\\,pp), whereas the best single detector spans over 20\\,pp.",
          " The practical advantage is reliability across unknown generators, not just average performance.",
          " ",
          " We also report a negative finding."
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

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01YWL58qAvbyJuKWSSRHAAJX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
  "old_string": "The tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.",
  "new_string": "The tight cross-generator consistency of the ensemble (CI width $<$\\,1\\,pp) makes deployment feasible even when the generating model is unknown."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "9abf9b00-a863-4eec-9f3e-c557411476f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013uQXeADRpe5ZNhG8YtYhwz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 41279,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 40 · 2026-05-15T12:36:53.719Z_

<details><summary>↩ Tool result · `toolu_01YWL58qAvbyJuKWSSRHAAJX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ab9b6dc5-636a-42f7-b13a-6d1d7b6fc22c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
    "oldString": "The tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.",
    "newString": "The tight cross-generator consistency of the ensemble (CI width $<$\\,1\\,pp) makes deployment feasible even when the generating model is unknown.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why are shape features stationary?}\nDistributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nOne \\emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.\nRecursive generation shifts \\emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \\emph{how} the model distributes probability mass around its predictions.\nIf this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.\nWe flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.\n\n\\paragraph{Relation to OOD detection.}\nReference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nOur contribution is not these features per se, but the \\emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.\nThis connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nRecursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.\n\n\\paragraph{Practical implications.}\nThe differential depth response enables risk-stratified data curation.\nRather than binary keep-or-discard filtering, practitioners can flag gen-2+ text for manual review while retaining gen-1 content that preserves much of the source distribution's properties.\nThree-class granularity is well-suited to this use case: it separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to curation decisions.\nFiner-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\\sim$3 steps \\cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.\nThe tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.\n\n\\paragraph{Information value of the negative finding.}\nDepth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nThis negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.\nThe dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\n\n\\paragraph{Connection to model collapse.}\nOur results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nModel collapse describes distributional degradation when models are \\emph{retrained} on their own outputs across generations.\nWe observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.\nThis suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.\nThe shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n",
    "structuredPatch": [
      {
        "oldStart": 19,
        "oldLines": 7,
        "newStart": 19,
        "newLines": 7,
        "lines": [
          " Rather than binary keep-or-discard filtering, practitioners can flag gen-2+ text for manual review while retaining gen-1 content that preserves much of the source distribution's properties.",
          " Three-class granularity is well-suited to this use case: it separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to curation decisions.",
          " Finer-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\\sim$3 steps \\cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.",
          "-The tight cross-generator consistency of the ensemble (CI width 1.4\\,pp) makes deployment feasible even when the generating model is unknown.",
          "+The tight cross-generator consistency of the ensemble (CI width $<$\\,1\\,pp) makes deployment feasible even when the generating model is unknown.",
          " ",
          " \\paragraph{Information value of the negative finding.}",
          " Depth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream})."
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

_source line 41_

Now update results.tex — the figure caption and the baselines comparison paragraph. Table 3 stays at 5-gen values, but I need to update the caption CI width, the prose CI span, and add the 6-gen sentence after the Table 3 discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "40b2cb06-7a71-4bd1-97da-5929ebe87d65",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J67K5Q3osLGTX6wTkUyA1H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 41544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 42_

<details open><summary>🔧 Tool call — Edit · `toolu_01RSNX5NCDqv23eRJKhkrcjE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}",
  "new_string": "\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans $<$\\,1\\,pp.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "4a458550-2264-4242-a09f-927e68eb1516",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J67K5Q3osLGTX6wTkUyA1H",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 265,
      "cache_read_input_tokens": 41544,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 265
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

_source line 43 · 2026-05-15T12:37:00.895Z_

<details><summary>↩ Tool result · `toolu_01RSNX5NCDqv23eRJKhkrcjE`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ca28b0aa-6f18-4697-bc95-4a383861640f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}",
    "newString": "\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans $<$\\,1\\,pp.}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nTable~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\n\nThe 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).\nPer-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).\nPer-class F1 varies by depth: gen-0\\,=\\,0.94, gen-2+\\,=\\,0.80, gen-1\\,=\\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.\n\n\\paragraph{Cross-scale transfer.}\nThe six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.\nHowever, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\\leq$2.8B generators.\nText generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.\nNotably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+1.1\\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.\nWe note that this gap may narrow with scale-matched training data; our current dataset contains $\\sim$1{,}000 samples per generator regardless of scale.\n\n\\paragraph{Cross-family generalization.}\nLeave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\\Delta$\\,=\\,$-$2.6\\,pp vs.\\ LOGO).\n\n\\paragraph{Length confound control.}\nText length correlates weakly with depth (Spearman $|\\rho| < 0.14$).\nLength-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 & [0.796, 0.817] \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\\\\n\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.800 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-generator-out macro-F1 with bootstrap 95\\% confidence intervals ($n$\\,=\\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}\n\\label{tab:logo-results}\n\\end{table}\n\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nIndividual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).\n\n\\paragraph{Feature complementarity.}\nTable~\\ref{tab:ablation} reports ablation results.\nThe full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR, hapax\\_ratio; F1\\,=\\,0.729) and reference-only features (entropy mean/std/max/min, tail\\_decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).\nSurface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.\n\n\\paragraph{Cross-family reference models.}\nTo confirm that differential depth response is not an artifact of the Pythia-410M reference model, we compute features using three cross-family references: Pythia-410M, OLMo-2-1B, and Qwen3-0.6B.\nAll three achieve LOGO F1 between 0.80 and 0.82, with consistent drift directions across features.\nThe pattern generalizes across reference model architectures.\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\\n\\midrule\nFull (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\\nSurface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\\nReference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}\n\\label{tab:ablation}\n\\end{table}\n\nLeave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nWe repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\\ref{fig:baseline-ci}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.800} & [0.786, 0.800] \\\\\nAvg-LogProb        & 0.765 & [0.616, 0.820] \\\\\nLD-Score            & 0.721 & [0.588, 0.770] \\\\\nFastDetectGPT       & 0.627 & [0.511, 0.762] \\\\\nBinoculars          & 0.579 & [0.405, 0.664] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal depth classification: 7-feature ensemble vs.\\ single detection baselines (5-gen LOGO). The ensemble outperforms the best single detector (Avg-LogProb) by +3.5\\,pp (paired bootstrap $p < 0.001$, $\\Delta$ CI [3.0, 4.0]).}\n\\label{tab:baselines}\n\\end{table}\n\nThe ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).\n\nThe critical distinction is \\emph{reliability}.\nThe ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nA single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.\nEach detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.\nThe 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n\nCan depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\nWe report this negative finding transparently: depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data curation.\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training.\n",
    "structuredPatch": [
      {
        "oldStart": 104,
        "oldLines": 7,
        "newStart": 104,
        "newLines": 7,
        "lines": [
          " \\begin{figure}[t]",
          " \\centering",
          " \\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}",
          "-\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans 1.4\\,pp.}",
          "+\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans $<$\\,1\\,pp.}",
          " \\label{fig:baseline-ci}",
          " \\end{figure}",
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

_source line 44_

<details open><summary>🔧 Tool call — Edit · `toolu_01UPvXUt6b9hks4YcBh4DgtX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "The ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
  "new_string": "The ensemble CI spans just 0.9\\,pp [0.783, 0.792], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820])."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "3088fe09-770b-4a85-bc9b-878f8be4e333",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015BnwN3Cijr8ZLZthJuXmZa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 375,
      "cache_read_input_tokens": 41809,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 375
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

_source line 45 · 2026-05-15T12:37:05.228Z_

<details><summary>↩ Tool result · `toolu_01UPvXUt6b9hks4YcBh4DgtX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "607842bb-f02a-40a1-99f9-068769f30409",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "The ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
    "newString": "The ensemble CI spans just 0.9\\,pp [0.783, 0.792], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nTable~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\n\nThe 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).\nPer-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).\nPer-class F1 varies by depth: gen-0\\,=\\,0.94, gen-2+\\,=\\,0.80, gen-1\\,=\\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.\n\n\\paragraph{Cross-scale transfer.}\nThe six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.\nHowever, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\\leq$2.8B generators.\nText generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.\nNotably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+1.1\\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.\nWe note that this gap may narrow with scale-matched training data; our current dataset contains $\\sim$1{,}000 samples per generator regardless of scale.\n\n\\paragraph{Cross-family generalization.}\nLeave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\\Delta$\\,=\\,$-$2.6\\,pp vs.\\ LOGO).\n\n\\paragraph{Length confound control.}\nText length correlates weakly with depth (Spearman $|\\rho| < 0.14$).\nLength-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 & [0.796, 0.817] \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\\\\n\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.800 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-generator-out macro-F1 with bootstrap 95\\% confidence intervals ($n$\\,=\\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}\n\\label{tab:logo-results}\n\\end{table}\n\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nIndividual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).\n\n\\paragraph{Feature complementarity.}\nTable~\\ref{tab:ablation} reports ablation results.\nThe full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR, hapax\\_ratio; F1\\,=\\,0.729) and reference-only features (entropy mean/std/max/min, tail\\_decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).\nSurface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.\n\n\\paragraph{Cross-family reference models.}\nTo confirm that differential depth response is not an artifact of the Pythia-410M reference model, we compute features using three cross-family references: Pythia-410M, OLMo-2-1B, and Qwen3-0.6B.\nAll three achieve LOGO F1 between 0.80 and 0.82, with consistent drift directions across features.\nThe pattern generalizes across reference model architectures.\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\\n\\midrule\nFull (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\\nSurface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\\nReference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}\n\\label{tab:ablation}\n\\end{table}\n\nLeave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans $<$\\,1\\,pp.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nWe repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\\ref{fig:baseline-ci}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.800} & [0.786, 0.800] \\\\\nAvg-LogProb        & 0.765 & [0.616, 0.820] \\\\\nLD-Score            & 0.721 & [0.588, 0.770] \\\\\nFastDetectGPT       & 0.627 & [0.511, 0.762] \\\\\nBinoculars          & 0.579 & [0.405, 0.664] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal depth classification: 7-feature ensemble vs.\\ single detection baselines (5-gen LOGO). The ensemble outperforms the best single detector (Avg-LogProb) by +3.5\\,pp (paired bootstrap $p < 0.001$, $\\Delta$ CI [3.0, 4.0]).}\n\\label{tab:baselines}\n\\end{table}\n\nThe ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).\n\nThe critical distinction is \\emph{reliability}.\nThe ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nA single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.\nEach detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.\nThe 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n\nCan depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\nWe report this negative finding transparently: depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data curation.\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training.\n",
    "structuredPatch": [
      {
        "oldStart": 131,
        "oldLines": 7,
        "newStart": 131,
        "newLines": 7,
        "lines": [
          " The ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).",
          " ",
          " The critical distinction is \\emph{reliability}.",
          "-The ensemble CI spans just 1.4\\,pp [0.786, 0.800], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
          "+The ensemble CI spans just 0.9\\,pp [0.783, 0.792], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).",
          " A single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.",
          " Each detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.",
          " The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator."
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

_source line 46_

Now add the 6-gen overall CI sentence after the Table 3 discussion. The Table 3 block ends around line 129 and then the baselines comparison paragraph starts at line 131. The sentence should go after the table caption/label block. Let me find the right spot — after the baselines table discussion but keeping Table 3 (tab:baselines) at 5-gen. I'll add the 6-gen sentence right after line 134 (the updated CI line).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "45be00cd-1bf5-438e-b952-da4857b29b25",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4GHEU46KjFVXFPFXrSeNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 47_

<details open><summary>🔧 Tool call — Read · `toolu_01BuwHseoAwkHLHD6FdvKrG5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "offset": 128,
  "limit": 15
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "eb897858-fc56-474d-a072-8fcdc52ff935",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y4GHEU46KjFVXFPFXrSeNa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 315,
      "cache_read_input_tokens": 42184,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 315
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

_source line 48 · 2026-05-15T12:37:10.634Z_

<details><summary>↩ Tool result · `toolu_01BuwHseoAwkHLHD6FdvKrG5`</summary>

```text
128	\label{tab:baselines}
129	\end{table}
130	
131	The ensemble outperforms all baselines in mean F1: +3.5\,pp over Avg-LogProb ($p < 0.001$, $\Delta$ CI [3.0, 4.0]), +7.9\,pp over LD-Score, +17.3\,pp over FastDetectGPT, and +22.1\,pp over Binoculars (Table~\ref{tab:baselines}).
132	
133	The critical distinction is \emph{reliability}.
134	The ensemble CI spans just 0.9\,pp [0.783, 0.792], while single-detector CIs span 18--26\,pp (e.g., Avg-LogProb [0.616, 0.820]).
135	A single detector's CI is wider than \emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.
136	Each detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.
137	The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.
138	
139	
140	\subsection{Downstream Utility: A Negative Finding}
141	\label{sec:results-downstream}
142	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6c17910e-e941-4363-9389-cde48ee3d7c8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
      "content": "\\label{tab:baselines}\n\\end{table}\n\nThe ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).\n\nThe critical distinction is \\emph{reliability}.\nThe ensemble CI spans just 0.9\\,pp [0.783, 0.792], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nA single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.\nEach detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.\nThe 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n",
      "numLines": 15,
      "startLine": 128,
      "totalLines": 173
    }
  }
}
```

</details>

---

### Assistant

_source line 49_

The 6-gen sentence should go after line 134 since that's where the CI discussion is. But actually, the task says to add it after the Table 3 discussion. Table 3 is `tab:baselines` which reports 5-gen LOGO. The sentence should go right after the baselines comparison paragraph (after line 137).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "8d55aa9f-566e-4a41-8729-3c381092c8e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155yznX2TYfYQT45bn4JCZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 42499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01BqnXpdTu62k9FTLZTkq41n`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
  "old_string": "The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}",
  "new_string": "The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\nAcross all six generators including Qwen3-8B, the ensemble achieves F1\\,=\\,0.789 with a 95\\% CI of [0.783, 0.792] (width 0.9\\,pp).\n\n\n\\subsection{Downstream Utility: A Negative Finding}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "3a10f732-1f51-418f-9bad-8afc65aa5b43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0155yznX2TYfYQT45bn4JCZf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 798,
      "cache_read_input_tokens": 42499,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 798
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

_source line 51 · 2026-05-15T12:37:20.707Z_

<details><summary>↩ Tool result · `toolu_01BqnXpdTu62k9FTLZTkq41n`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "fcc23d7f-48be-4144-a933-6b058cab95da",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/results.tex",
    "oldString": "The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}",
    "newString": "The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\nAcross all six generators including Qwen3-8B, the ensemble achieves F1\\,=\\,0.789 with a 95\\% CI of [0.783, 0.792] (width 0.9\\,pp).\n\n\n\\subsection{Downstream Utility: A Negative Finding}",
    "originalFile": "\\section{Results}\n\\label{sec:results}\n\nWe evaluate depth fingerprinting along four axes: cross-generator classification (\\S\\ref{sec:results-classification}), differential depth response of individual features (\\S\\ref{sec:results-differential}), comparison with existing detection baselines (\\S\\ref{sec:results-baselines}), and downstream utility for data curation (\\S\\ref{sec:results-downstream}).\n\n\\subsection{Depth Classification Performance}\n\\label{sec:results-classification}\n\nTable~\\ref{tab:logo-results} reports leave-one-generator-out (LOGO) macro-F1 for 3-class depth estimation (gen-0\\,/\\,gen-1\\,/\\,gen-2+) across six generators spanning three model families and parameter counts from 0.6B to 8.2B.\n\nThe 7-feature ensemble achieves LOGO F1\\,=\\,0.789, significantly outperforming all single-detector baselines ($p<0.001$; \\S\\ref{sec:results-baselines}).\nPer-generator held-out F1 ranges from 0.683 (Qwen3-8B) to 0.856 (Pythia-1B).\nPer-class F1 varies by depth: gen-0\\,=\\,0.94, gen-2+\\,=\\,0.80, gen-1\\,=\\,0.64; the primary difficulty lies in distinguishing gen-1 from gen-2+, where feature margins narrow.\n\n\\paragraph{Cross-scale transfer.}\nThe six-generator evaluation includes Qwen3-8B (8.2B parameters), confirming that depth signal persists at scales beyond the $\\leq$2.8B training generators.\nHowever, cross-scale transfer incurs a moderate gap: Qwen3-8B held-out F1\\,=\\,0.683 (CI [0.668, 0.694]), compared to 0.76--0.86 for $\\leq$2.8B generators.\nText generated by larger models is more fluent, compressing feature margins and making depth distinctions harder.\nNotably, adding Qwen3-8B data \\emph{improves} classification on the original five generators (+1.1\\,pp to 0.811), indicating that cross-scale diversity benefits rather than dilutes the training signal.\nWe note that this gap may narrow with scale-matched training data; our current dataset contains $\\sim$1{,}000 samples per generator regardless of scale.\n\n\\paragraph{Cross-family generalization.}\nLeave-one-family-out (LOFO) evaluation---holding out an entire model family and training on the remaining two---yields macro-F1 of 0.772 (Pythia held out), 0.762 (OLMo held out), and 0.754 (Qwen held out), confirming that depth features transfer across architectural families with only modest degradation (average $\\Delta$\\,=\\,$-$2.6\\,pp vs.\\ LOGO).\n\n\\paragraph{Length confound control.}\nText length correlates weakly with depth (Spearman $|\\rho| < 0.14$).\nLength-normalized feature trends are preserved, and length-matched subsampling yields comparable or higher F1 ($\\Delta$\\,=\\,+0.041), ruling out length as a confound (Appendix~\\ref{app:length}).\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{llccc}\n\\toprule\n\\textbf{Generator} & \\textbf{Family} & \\textbf{Params} & \\textbf{Held-out F1} & \\textbf{95\\% CI} \\\\\n\\midrule\nPythia-1B       & Pythia & 1.0B & 0.856 & [0.843, 0.863] \\\\\nPythia-2.8B     & Pythia & 2.8B & 0.804 & [0.793, 0.813] \\\\\nOLMo-2-1B      & OLMo   & 1.5B & 0.764 & [0.754, 0.776] \\\\\nQwen3-0.6B     & Qwen   & 0.6B & 0.824 & [0.813, 0.834] \\\\\nQwen3-1.7B     & Qwen   & 1.7B & 0.805 & [0.796, 0.817] \\\\\nQwen3-8B       & Qwen   & 8.2B & 0.683 & [0.668, 0.694] \\\\\n\\midrule\n\\multicolumn{3}{l}{Average (6-gen LOGO)} & 0.789 & --- \\\\\n\\multicolumn{3}{l}{5-gen LOGO (excl.\\ Qwen3-8B)} & 0.800 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Leave-one-generator-out macro-F1 with bootstrap 95\\% confidence intervals ($n$\\,=\\,1000) for 3-class depth estimation using the 7-feature ensemble. Each row holds out one generator for testing and trains on the remaining five.}\n\\label{tab:logo-results}\n\\end{table}\n\n\n\\subsection{Differential Depth Response}\n\\label{sec:results-differential}\n\nFeatures exhibit \\emph{differential depth response}: central-tendency and diversity measures drift monotonically with depth, while distributional shape measures remain near-stationary.\nThis pattern is consistent with recursive generation inducing a location shift in the token-level NLL distribution---the text becomes progressively more predictable (mean shifts), while the functional form of the distribution is preserved (shape is invariant).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig1_differential_response.pdf}\n\\caption{Differential depth response: Spearman correlations between individual features and generation depth. Central-tendency and diversity features (hapax ratio, TTR, entropy mean) show strong monotonic drift, while shape features (entropy std, tail decay) remain near-stationary.}\n\\label{fig:feature-drift}\n\\end{figure}\n\nIndividual-level Spearman correlations with depth confirm the split (Figure~\\ref{fig:feature-drift}):\ndrifting features show strong monotonic trends (hapax ratio $\\rho = -0.558$, TTR $\\rho = -0.542$, entropy mean $\\rho = -0.475$),\nwhile shape features show weak or negligible correlations (entropy std $|\\rho| = 0.076$, tail decay $|\\rho| = 0.089$).\n\n\\paragraph{Feature complementarity.}\nTable~\\ref{tab:ablation} reports ablation results.\nThe full 7-feature set (F1\\,=\\,0.789) significantly outperforms both surface-only features (TTR, hapax\\_ratio; F1\\,=\\,0.729) and reference-only features (entropy mean/std/max/min, tail\\_decay; F1\\,=\\,0.745; McNemar $p \\approx 0$).\nPermutation importance ranks hapax ratio highest (0.269), followed by entropy mean (0.164) and TTR (0.159).\nSurface features capture vocabulary impoverishment; reference features capture distributional shift---neither subsumes the other.\n\n\\paragraph{Cross-family reference models.}\nTo confirm that differential depth response is not an artifact of the Pythia-410M reference model, we compute features using three cross-family references: Pythia-410M, OLMo-2-1B, and Qwen3-0.6B.\nAll three achieve LOGO F1 between 0.80 and 0.82, with consistent drift directions across features.\nThe pattern generalizes across reference model architectures.\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Feature set} & \\textbf{LOGO F1} & \\textbf{Top feature (importance)} \\\\\n\\midrule\nFull (7 features)     & 0.789 & hapax\\_ratio (0.269) \\\\\nSurface only (2)      & 0.729 & hapax\\_ratio (0.320) \\\\\nReference only (5)    & 0.745 & entropy\\_mean (0.218) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Feature ablation (6-gen LOGO). Full $>$ surface = reference confirms complementarity between surface diversity features and reference-model distributional features.}\n\\label{tab:ablation}\n\\end{table}\n\nLeave-one-feature-out analysis confirms that 6 of 7 features contribute positively, with entropy\\_max showing the largest marginal impact despite modest split frequency (Appendix~\\ref{app:lofo}).\n\n\n\\subsection{Comparison with Detection Baselines}\n\\label{sec:results-baselines}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig3_baseline_comparison.png}\n\\caption{LOGO macro-F1 with 95\\% bootstrap confidence intervals for each detection baseline and the 7-feature ensemble. Single-detector CIs span 18--26\\,pp; the ensemble CI spans $<$\\,1\\,pp.}\n\\label{fig:baseline-ci}\n\\end{figure}\n\nWe repurpose four existing detection scores as ordinal depth predictors by training the same ordinal classifier on each score as a single feature, using identical LOGO evaluation (Figure~\\ref{fig:baseline-ci}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lcc}\n\\toprule\n\\textbf{Method} & \\textbf{LOGO F1} & \\textbf{95\\% CI} \\\\\n\\midrule\n7-feature ensemble & \\textbf{0.800} & [0.786, 0.800] \\\\\nAvg-LogProb        & 0.765 & [0.616, 0.820] \\\\\nLD-Score            & 0.721 & [0.588, 0.770] \\\\\nFastDetectGPT       & 0.627 & [0.511, 0.762] \\\\\nBinoculars          & 0.579 & [0.405, 0.664] \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Ordinal depth classification: 7-feature ensemble vs.\\ single detection baselines (5-gen LOGO). The ensemble outperforms the best single detector (Avg-LogProb) by +3.5\\,pp (paired bootstrap $p < 0.001$, $\\Delta$ CI [3.0, 4.0]).}\n\\label{tab:baselines}\n\\end{table}\n\nThe ensemble outperforms all baselines in mean F1: +3.5\\,pp over Avg-LogProb ($p < 0.001$, $\\Delta$ CI [3.0, 4.0]), +7.9\\,pp over LD-Score, +17.3\\,pp over FastDetectGPT, and +22.1\\,pp over Binoculars (Table~\\ref{tab:baselines}).\n\nThe critical distinction is \\emph{reliability}.\nThe ensemble CI spans just 0.9\\,pp [0.783, 0.792], while single-detector CIs span 18--26\\,pp (e.g., Avg-LogProb [0.616, 0.820]).\nA single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.\nEach detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.\nThe 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.\n\n\n\\subsection{Downstream Utility: A Negative Finding}\n\\label{sec:results-downstream}\n\nCan depth-aware data curation improve downstream language model quality?\nWe fine-tune OLMo-2-0425-1B on five data variants (3 seeds each) and evaluate perplexity on a held-out test set (Table~\\ref{tab:downstream}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{lrc}\n\\toprule\n\\textbf{Variant} & \\textbf{$n$} & \\textbf{Test PPL} \\\\\n\\midrule\nAll depths            & 12{,}299 & 2.335 $\\pm$ 0.000 \\\\\nSize-matched (random) & 3{,}951  & 2.367 $\\pm$ 0.000 \\\\\nDepth 0--1 only       & 3{,}951  & 2.387 $\\pm$ 0.001 \\\\\nBinary-filtered       & 3{,}951  & 2.389 $\\pm$ 0.000 \\\\\nDepth 0 only          & 797      & 2.681 $\\pm$ 0.001 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Downstream fine-tuning perplexity (OLMo-2-0425-1B, mean $\\pm$ std across 3 seeds). At equal sample count, random subsampling (2.367) outperforms depth-aware curation (depth 0--1: 2.387, binary-filtered: 2.389).}\n\\label{tab:downstream}\n\\end{table}\n\nThe results are unambiguous: data quantity dominates depth composition.\nTraining on all 12{,}299 samples yields the lowest perplexity (2.335).\nAt equal sample count ($n$\\,=\\,3{,}951), random subsampling (2.367) \\emph{outperforms} both depth-stratified selection (depth 0--1: 2.387) and binary detection filtering (2.389).\nCross-seed variance is below 0.002 across all variants, confirming the robustness of this null result.\n\nRestricting training to human-only text (depth 0, $n$\\,=\\,797) produces a sharp perplexity increase to 2.681, driven primarily by the 5$\\times$ reduction in data volume rather than depth composition per se.\n\nWe report this negative finding transparently: depth fingerprinting is an effective \\emph{diagnostic} tool for characterizing text provenance, not a \\emph{curative} tool for data curation.\nKnowing the generation depth of a document does not, by itself, make it more or less useful for training.\n",
    "structuredPatch": [
      {
        "oldStart": 135,
        "oldLines": 6,
        "newStart": 135,
        "newLines": 7,
        "lines": [
          " A single detector's CI is wider than \\emph{all pairwise detector differences}, meaning no single detector is reliably best across generators.",
          " Each detector captures partial depth signal---Avg-LogProb tracks mean perplexity shift, LD-Score captures character-level distributional change---but each fails on specific generator families.",
          " The 7-feature ensemble aggregates complementary signals, producing stable performance regardless of the held-out generator.",
          "+Across all six generators including Qwen3-8B, the ensemble achieves F1\\,=\\,0.789 with a 95\\% CI of [0.783, 0.792] (width 0.9\\,pp).",
          " ",
          " ",
          " \\subsection{Downstream Utility: A Negative Finding}"
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

_source line 52_

W11 done. Now commit, then move to W3.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ccfdc581-4b9e-4bb2-8479-9a424b0a611f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgxMMzZgn37NtdvAXJ5uWM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 43297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 410
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

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01PW8p2rfGxTY9xDrAy5gra6`</summary>

```json
{
  "command": "git add artifacts/_project/paper/main.tex artifacts/_project/paper/abstract.tex artifacts/_project/paper/introduction.tex artifacts/_project/paper/discussion.tex artifacts/_project/paper/results.tex && git commit -m \"$(cat <<'EOF'\npaper: W11 — CI width unified to 6-gen 0.9pp across all .tex files\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit W11 CI width changes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "faae1846-0aac-4a9d-9d73-898cc83d957c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgxMMzZgn37NtdvAXJ5uWM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 410,
      "cache_read_input_tokens": 43297,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 410
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

_source line 54 · 2026-05-15T12:37:25.776Z_

<details><summary>↩ Tool result · `toolu_01PW8p2rfGxTY9xDrAy5gra6`</summary>

```text
[master 91c9e8e] paper: W11 — CI width unified to 6-gen 0.9pp across all .tex files
 Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 5 files changed, 7 insertions(+), 6 deletions(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "4a37053a-a481-4546-9e01-bd50a5cd0b8e",
  "tool_use_result": {
    "stdout": "[master 91c9e8e] paper: W11 — CI width unified to 6-gen 0.9pp across all .tex files\n Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 5 files changed, 7 insertions(+), 6 deletions(-)",
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

_source line 55_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01UpaUh8kCwTrttQkMKEpWs7`</summary>

```json
{
  "todos": [
    {
      "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
      "status": "completed",
      "activeForm": "Updating CI width and values across all .tex files"
    },
    {
      "content": "W3: Add topic drift paragraph to discussion.tex",
      "status": "in_progress",
      "activeForm": "Adding topic drift paragraph to discussion.tex"
    },
    {
      "content": "W3: Add class-balanced annotation to method.tex",
      "status": "pending",
      "activeForm": "Adding class-balanced annotation to method.tex"
    },
    {
      "content": "Sync modified files to docs/paper/",
      "status": "pending",
      "activeForm": "Syncing modified files to docs/paper/"
    },
    {
      "content": "Git commits for each change",
      "status": "pending",
      "activeForm": "Creating git commits"
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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "7a2bb98c-1f1e-4b13-a16b-3eb97903b766",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtdqLprwTTjjx5cwMdCpEP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 389,
      "cache_read_input_tokens": 43707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 389
      },
      "output_tokens": 33,
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

_source line 56 · 2026-05-15T12:37:29.726Z_

<details><summary>↩ Tool result · `toolu_01UpaUh8kCwTrttQkMKEpWs7`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6270b344-dd27-48b3-8332-cc13f9ce76d8",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "in_progress",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "pending",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "pending",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
      }
    ],
    "newTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "in_progress",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "pending",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 57_

Now W3 — topic drift paragraph. Adding it to discussion.tex after the "Connection to model collapse" paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e2f48753-1050-47a3-85f3-c3258186debc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbVGpKiykv1WoSCofATPsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 44096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 58_

<details open><summary>🔧 Tool call — Read · `toolu_01T88oG3icNwDUaV3tKzCT2F`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
  "offset": 29,
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "02146c31-cc24-4777-a942-cb0bf879e3da",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EbVGpKiykv1WoSCofATPsY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 44096,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 59 · 2026-05-15T12:37:33.077Z_

<details><summary>↩ Tool result · `toolu_01T88oG3icNwDUaV3tKzCT2F`</summary>

```text
29	\paragraph{Connection to model collapse.}
30	Our results relate to, but are distinct from, model collapse \cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.
31	Model collapse describes distributional degradation when models are \emph{retrained} on their own outputs across generations.
32	We observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \emph{inference chains} without any parameter updates.
33	This suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.
34	The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "efb76324-1af1-4fbf-b1e6-dc878bb26b83",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
      "content": "\\paragraph{Connection to model collapse.}\nOur results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nModel collapse describes distributional degradation when models are \\emph{retrained} on their own outputs across generations.\nWe observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.\nThis suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.\nThe shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n",
      "numLines": 7,
      "startLine": 29,
      "totalLines": 35
    }
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01JG86r4g9wD1WVMpaEvT4Gp`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
  "old_string": "The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.",
  "new_string": "The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n\n\\paragraph{Topic drift as mediator, not confounder.}\nRecursive generation narrows topic diversity: cosine similarity between adjacent depths increases monotonically from 0.62 (depth 0$\\to$1) to 0.86 (depth 3$\\to$4), consistent with regression toward high-probability modes.\nHowever, topic narrowing accounts for less than 9\\% of feature variance (maximum: entropy\\_mean, $\\rho = -0.286$, $R^2 = 0.082$).\nShape features are near-independent of semantic drift (tail\\_decay $|\\rho| = 0.068$, $R^2 = 0.005$).\nTopic drift is best understood as a \\emph{mediator}---one mechanism through which depth manifests---rather than a confound that invalidates depth features.\nThe depth signal primarily reflects sampling-induced distributional compression, not topic narrowing per se."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "c8332f6a-f907-4f2c-8f6b-215675d5e42f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018h9tt4BzHKoidKcTPnuwA7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 44387,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
      },
      "output_tokens": 39,
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

_source line 61 · 2026-05-15T12:37:43.264Z_

<details><summary>↩ Tool result · `toolu_01JG86r4g9wD1WVMpaEvT4Gp`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "f94eb8b6-ad49-4d29-8033-bf0bd649564c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/discussion.tex",
    "oldString": "The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.",
    "newString": "The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n\n\\paragraph{Topic drift as mediator, not confounder.}\nRecursive generation narrows topic diversity: cosine similarity between adjacent depths increases monotonically from 0.62 (depth 0$\\to$1) to 0.86 (depth 3$\\to$4), consistent with regression toward high-probability modes.\nHowever, topic narrowing accounts for less than 9\\% of feature variance (maximum: entropy\\_mean, $\\rho = -0.286$, $R^2 = 0.082$).\nShape features are near-independent of semantic drift (tail\\_decay $|\\rho| = 0.068$, $R^2 = 0.005$).\nTopic drift is best understood as a \\emph{mediator}---one mechanism through which depth manifests---rather than a confound that invalidates depth features.\nThe depth signal primarily reflects sampling-induced distributional compression, not topic narrowing per se.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why are shape features stationary?}\nDistributional shape features (entropy standard deviation, tail decay) remain near-stationary across generation depths, while central-tendency features drift monotonically (\\S\\ref{sec:results-differential}).\nOne \\emph{speculative} explanation is that shape is primarily determined by the sampling mechanism (temperature, top-$p$ truncation) and the model's architecture-level output distribution, both of which are fixed across generation steps.\nRecursive generation shifts \\emph{what} the model talks about---steering toward higher-probability vocabulary regions---but does not alter \\emph{how} the model distributes probability mass around its predictions.\nIf this account is correct, shape features should remain stationary even at much greater depths and across different prompt types, while level features should continue to drift until reaching a fixed point.\nWe flag this as a hypothesis for future investigation, not a conclusion supported by our current experiments.\n\n\\paragraph{Relation to OOD detection.}\nReference-model entropy features are functionally NLL-based out-of-distribution scores---the same signal backbone underlying DetectGPT \\cite{detectgpt}, GLTR \\cite{gltr}, and Binoculars \\cite{binoculars}.\nOur contribution is not these features per se, but the \\emph{ordinal} depth formulation and the empirical finding that they exhibit differential depth response under recursive generation.\nThis connection also offers a lens on shape stationarity: in the OOD detection literature, distributional location statistics (mean log-likelihood) shift under domain drift, while shape statistics (variance, tail behavior) are more robust \\cite{ood_baseline}.\nRecursive generation chains produce an analogous effect---progressive drift away from human text that manifests primarily as a location shift in the NLL distribution.\n\n\\paragraph{Practical implications.}\nThe differential depth response enables risk-stratified data curation.\nRather than binary keep-or-discard filtering, practitioners can flag gen-2+ text for manual review while retaining gen-1 content that preserves much of the source distribution's properties.\nThree-class granularity is well-suited to this use case: it separates human text from moderate-drift first-generation content and from deeper text with compounding distributional shift---the distinction most relevant to curation decisions.\nFiner-grained depth distinctions may be achievable for non-paraphrastic chains (unlike paraphrastic chains, which converge within $\\sim$3 steps \\cite{broken_telephone}), but the three-class scheme already captures the practically relevant boundaries.\nThe tight cross-generator consistency of the ensemble (CI width $<$\\,1\\,pp) makes deployment feasible even when the generating model is unknown.\n\n\\paragraph{Information value of the negative finding.}\nDepth-aware curation does not improve downstream language model quality over random subsampling at equal sample count (\\S\\ref{sec:results-downstream}).\nThis negative result carries positive information value: it rules out depth-based filtering as a data selection strategy, sparing practitioners from building depth-conditional pipelines that would not yield quality gains.\nThe dominant factor is data quantity, not depth composition---consistent with findings emphasizing data volume over curation sophistication \\cite{self_consuming_mad}.\n\n\\paragraph{Connection to model collapse.}\nOur results relate to, but are distinct from, model collapse \\cite{curse_of_recursion,strong_model_collapse,self_consuming_mad}.\nModel collapse describes distributional degradation when models are \\emph{retrained} on their own outputs across generations.\nWe observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.\nThis suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.\nThe shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.\n",
    "structuredPatch": [
      {
        "oldStart": 32,
        "oldLines": 3,
        "newStart": 32,
        "newLines": 10,
        "lines": [
          " We observe analogous drift---monotonic decrease in vocabulary diversity, compression of perplexity---in \\emph{inference chains} without any parameter updates.",
          " This suggests that the mechanisms documented in model collapse theory (regression toward high-probability modes, loss of distributional tails) operate at inference time as well, driven by the sampling process rather than gradient updates.",
          " The shared phenomenology motivates using depth fingerprinting features as early indicators of data that, if fed back into training, may accelerate model collapse.",
          "+",
          "+\\paragraph{Topic drift as mediator, not confounder.}",
          "+Recursive generation narrows topic diversity: cosine similarity between adjacent depths increases monotonically from 0.62 (depth 0$\\to$1) to 0.86 (depth 3$\\to$4), consistent with regression toward high-probability modes.",
          "+However, topic narrowing accounts for less than 9\\% of feature variance (maximum: entropy\\_mean, $\\rho = -0.286$, $R^2 = 0.082$).",
          "+Shape features are near-independent of semantic drift (tail\\_decay $|\\rho| = 0.068$, $R^2 = 0.005$).",
          "+Topic drift is best understood as a \\emph{mediator}---one mechanism through which depth manifests---rather than a confound that invalidates depth features.",
          "+The depth signal primarily reflects sampling-induced distributional compression, not topic narrowing per se."
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

<details open><summary>🔧 Tool call — Bash · `toolu_01LCGHQjpkz169YdFrrMUknL`</summary>

```json
{
  "command": "git add artifacts/_project/paper/discussion.tex && git commit -m \"$(cat <<'EOF'\npaper: W3 — add topic drift mediator analysis to Discussion\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit W3 topic drift paragraph"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "9d1d7093-03ad-437b-a1e6-887703480d1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01838Tkc3DdwfMX3LfbAstXH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 477,
      "cache_read_input_tokens": 44742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 477
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

_source line 63 · 2026-05-15T12:37:47.497Z_

<details><summary>↩ Tool result · `toolu_01LCGHQjpkz169YdFrrMUknL`</summary>

```text
[master b5d0c42] paper: W3 — add topic drift mediator analysis to Discussion
 Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 7 insertions(+)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "4cec7d07-0945-4bf8-ad54-dd3763ca9065",
  "tool_use_result": {
    "stdout": "[master b5d0c42] paper: W3 — add topic drift mediator analysis to Discussion\n Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 7 insertions(+)",
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

_source line 64_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_013BbSvKtJsXFFMZxgecU9Ud`</summary>

```json
{
  "todos": [
    {
      "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
      "status": "completed",
      "activeForm": "Updating CI width and values across all .tex files"
    },
    {
      "content": "W3: Add topic drift paragraph to discussion.tex",
      "status": "completed",
      "activeForm": "Adding topic drift paragraph to discussion.tex"
    },
    {
      "content": "W3: Add class-balanced annotation to method.tex",
      "status": "in_progress",
      "activeForm": "Adding class-balanced annotation to method.tex"
    },
    {
      "content": "Sync modified files to docs/paper/",
      "status": "pending",
      "activeForm": "Syncing modified files to docs/paper/"
    },
    {
      "content": "Git commits for each change",
      "status": "pending",
      "activeForm": "Creating git commits"
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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "5ba6c571-d1e9-493c-b178-5cbe09769660",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Lwe9r7E4RY3R7K7zh3sDkQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 310,
      "cache_read_input_tokens": 45219,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 310
      },
      "output_tokens": 32,
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

_source line 65 · 2026-05-15T12:37:54.070Z_

<details><summary>↩ Tool result · `toolu_013BbSvKtJsXFFMZxgecU9Ud`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "ab4da52a-46c8-4fd4-9d2e-7d3b4f2f5e1d",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "in_progress",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "pending",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
      }
    ],
    "newTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "completed",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "in_progress",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
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

Now the class-balanced annotation in method.tex. The metrics discussion is in the "Metrics and statistical testing" paragraph (line 72). I'll add the annotation after that paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6ba1fb6c-dc11-4ad7-8ff7-9d68ffc964cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASDgYUTVqkwAZT56PPfLj4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 45529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 67_

<details open><summary>🔧 Tool call — Read · `toolu_01LKfVPBwHQgkiXGJdEd22v5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "offset": 72,
  "limit": 8
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "b086a5c6-e47b-4d68-9ac0-e911ce4e888a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASDgYUTVqkwAZT56PPfLj4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 291,
      "cache_read_input_tokens": 45529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 291
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

_source line 68 · 2026-05-15T12:37:58.184Z_

<details><summary>↩ Tool result · `toolu_01LKfVPBwHQgkiXGJdEd22v5`</summary>

```text
72	\paragraph{Metrics and statistical testing.}
73	The primary metric is \textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.
74	We report per-class F1 scores and 95\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).
75	For pairwise model comparisons (e.g., full features vs.\ ablated subsets), we use the \textbf{McNemar test} on disagreement tables.
76	For comparisons against detection baselines, we use \textbf{paired bootstrap} significance tests.
77	All reported $p$-values are two-sided.
78	
79	\paragraph{Baselines.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "694f6bda-7fb4-423e-ad0e-086b89969dac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
      "content": "\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\n\n\\paragraph{Baselines.}",
      "numLines": 8,
      "startLine": 72,
      "totalLines": 86
    }
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Edit · `toolu_01SiwukBDwBcFDWJTTF3fn56`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
  "old_string": "All reported $p$-values are two-sided.\n\n\\paragraph{Baselines.}",
  "new_string": "All reported $p$-values are two-sided.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6d90a6a4-8e89-48fa-a546-a946aba23782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DEoEZMnHmSBRhxakTVW8Cd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 45820,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 46,
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

_source line 70 · 2026-05-15T12:38:03.571Z_

<details><summary>↩ Tool result · `toolu_01SiwukBDwBcFDWJTTF3fn56`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "beaa4b9c-3b99-45f3-bd6a-6349d37fc18c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_3/projects/gen-depth-fingerprint/artifacts/_project/paper/method.tex",
    "oldString": "All reported $p$-values are two-sided.\n\n\\paragraph{Baselines.}",
    "newString": "All reported $p$-values are two-sided.\nFeature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.\n\n\\paragraph{Baselines.}",
    "originalFile": "\\section{Method}\n\\label{sec:method}\n\n\\subsection{Task Formulation}\n\\label{sec:task}\n\nGiven a text $x$, the goal is to predict its \\emph{generation depth} $d \\in \\{0, 1, 2{+}\\}$, where $d{=}0$ denotes human-written text, $d{=}1$ denotes first-generation LLM output conditioned on human text, and $d{=}2{+}$ denotes text produced by recursively conditioning an LLM on its own prior output at least twice.\nFormally, let $\\mathcal{C}_0$ be a reference corpus of human-written text.\nA generation chain of depth $k$ is defined recursively: $x^{(0)} \\sim \\mathcal{C}_0$, and $x^{(k)} = G(x^{(k-1)})$ for $k \\geq 1$, where $G$ denotes stochastic LLM generation conditioned on its input.\nWe frame depth estimation as an ordinal classification task over three classes rather than binary real-vs-synthetic detection, enabling finer-grained provenance characterization.\nDepths beyond 2 are merged into a single $2{+}$ class, consistent with monotonic feature convergence that compresses inter-class margins beyond depth 2 (\\S\\ref{sec:results-differential}).\n\n\\subsection{Generation Chain Construction}\n\\label{sec:generation}\n\nWe construct generation chains using six generators spanning three model families: \\textbf{Pythia} (2.8B, 1B) \\cite{pythia}, \\textbf{OLMo} (OLMo-2-1B) \\cite{olmo}, and \\textbf{Qwen} (Qwen3-1.7B, Qwen3-0.6B, Qwen3-8B-Base) \\cite{qwen3}.\nThis selection covers parameter scales from 0.6B to 8.2B and diverse pretraining corpora, enabling evaluation of cross-generator and cross-scale generalization.\n\nFor each generator, we sample approximately 1{,}000 seed passages from English Wikipedia as $\\mathcal{C}_0$.\nEach seed is iteratively fed through the generator to produce a chain of depth 4 (i.e., gen-0 through gen-4), using the prompt ``\\texttt{Continue the following text: \\{text\\}}''.\nAll generation uses temperature $\\tau{=}0.7$, nucleus sampling with $p{=}0.9$, and maximum length of 256 new tokens.\nThe resulting dataset contains approximately 27{,}000 texts across all generators and depths.\nFor classification, depths 2--4 are collapsed into the $2{+}$ class.\n\n\\subsection{Feature Extraction}\n\\label{sec:features}\n\nThe seven features are motivated by two complementary views of distributional drift.\nReference-model features capture how the text's token-level surprise distribution shifts relative to a fixed model; surface features capture how lexical diversity contracts under recursive generation.\nTogether, they span both the generative mechanism (what the model produces) and the surface manifestation (how the vocabulary changes).\nThis two-pronged design is not post-hoc: it follows directly from the hypothesis that recursive generation induces a location shift in the NLL distribution (\\S\\ref{sec:results-differential}).\n\nWe extract seven distributional features per text, organized into two groups based on what they measure rather than how they are computed.\n\n\\paragraph{Reference-model features.}\nA held-out reference model (Pythia-410M, chosen to be smaller than and architecturally independent of all generators) computes per-token negative log-likelihood (NLL) for each text.\nFrom the resulting NLL sequence, we extract five statistics:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{entropy\\_mean}: mean token-level NLL, capturing the average predictability of the text under the reference model;\n    \\item \\textbf{entropy\\_std}: standard deviation of token-level NLL, measuring the spread of per-token surprise;\n    \\item \\textbf{entropy\\_max}: maximum token-level NLL, capturing the most surprising token;\n    \\item \\textbf{entropy\\_min}: minimum token-level NLL, capturing the most predictable token---as generation depth increases, the floor of token-level surprise drops, reflecting the model's increasing confidence on its own outputs;\n    \\item \\textbf{tail\\_decay}: proportion of tokens whose NLL exceeds the 90th percentile of the reference distribution (computed over $\\mathcal{C}_0$), measuring how heavy-tailed the NLL distribution is relative to human text.\n\\end{itemize}\n\n\\paragraph{Surface features.}\nTwo features capture lexical diversity without requiring a reference model:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{TTR}: type-token ratio (number of unique word types divided by total tokens);\n    \\item \\textbf{hapax\\_ratio}: proportion of words appearing exactly once (\\emph{hapax legomena}).\n\\end{itemize}\n\n\\paragraph{Feature complementarity.}\nThe grouping reflects an empirical pattern we term \\emph{differential depth response}: central-tendency and diversity features (entropy\\_mean, TTR, hapax\\_ratio) drift monotonically with generation depth, while distributional shape features (entropy\\_std, tail\\_decay) remain near-stationary.\nThis differential behavior---consistent with recursive generation inducing a location shift in the NLL distribution while preserving its functional form---motivates combining both feature types.\nAs shown in \\S\\ref{sec:results}, the full 7-feature set significantly outperforms either group alone.\n\n\\subsection{Evaluation Protocol}\n\\label{sec:evaluation}\n\n\\paragraph{Cross-validation.}\nTo evaluate generalization to unseen generators, we use \\textbf{Leave-One-Generator-Out (LOGO)} cross-validation: in each fold, one of the six generators is held out for testing and the remaining five provide training data.\nWe additionally report \\textbf{Leave-One-Family-Out (LOFO)} results, where an entire model family (e.g., all Qwen models) is held out, testing generalization across architectural lineages.\n\n\\paragraph{Classifier.}\nWe use XGBoost \\cite{xgboost} as the classifier throughout.\nGradient-boosted trees handle heterogeneous feature scales and nonlinear interactions without extensive hyperparameter tuning, and their feature importance scores support interpretability.\nWe use $n\\_\\text{estimators}{=}200$, $\\max\\_\\text{depth}{=}6$, and learning rate $0.1$ throughout all experiments, including baseline comparisons, to ensure a controlled comparison.\nLOGO F1 is stable across random seeds (mean\\,=\\,0.789, std\\,=\\,0.0009 over 5 seeds), confirming that results are not sensitive to classifier initialization.\nAlternative classifiers (random forest, logistic regression) yield comparable performance (Appendix~\\ref{app:classifier}), confirming that discriminative power resides in the features, not the classifier.\n\n\\paragraph{Metrics and statistical testing.}\nThe primary metric is \\textbf{macro-averaged F1} over the three depth classes, which weights minority classes (gen-1, gen-2+) equally against the typically easier gen-0 class.\nWe report per-class F1 scores and 95\\% bootstrap confidence intervals ($n{=}1{,}000$ resamples).\nFor pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.\nFor comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.\nAll reported $p$-values are two-sided.\n\n\\paragraph{Baselines.}\nWe compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}.\nEach baseline score is used as a univariate feature in the same XGBoost framework under LOGO cross-validation, ensuring a controlled comparison.\n\n\\paragraph{Length confound control.}\nSince TTR and hapax\\_ratio are mechanically length-dependent, we verify that depth signal is not an artifact of systematic length variation.\nWe conduct three complementary analyses: (1) Spearman correlation between text length and each feature (requiring $|\\rho| < 0.15$ for non-confounded features), (2) classification with length-normalized features, and (3) comparison on length-matched subsets.\n",
    "structuredPatch": [
      {
        "oldStart": 75,
        "oldLines": 6,
        "newStart": 75,
        "newLines": 7,
        "lines": [
          " For pairwise model comparisons (e.g., full features vs.\\ ablated subsets), we use the \\textbf{McNemar test} on disagreement tables.",
          " For comparisons against detection baselines, we use \\textbf{paired bootstrap} significance tests.",
          " All reported $p$-values are two-sided.",
          "+Feature--depth correlations (\\S\\ref{sec:results-differential}) are computed on class-balanced subsamples (equal samples per depth class) to control for depth-class imbalance in the generation pipeline.",
          " ",
          " \\paragraph{Baselines.}",
          " We compare the 7-feature ensemble against four single-score detection methods repurposed as ordinal depth predictors: Avg-LogProb, FastDetectGPT \\cite{fast_detectgpt}, Binoculars \\cite{binoculars}, and LD-Score \\cite{ld_score}."
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

<details open><summary>🔧 Tool call — Bash · `toolu_01MuaWFsoFfVmMj1KVQBzYuY`</summary>

```json
{
  "command": "git add artifacts/_project/paper/method.tex && git commit -m \"$(cat <<'EOF'\npaper: W3 — add class-balanced subsample note to Metrics paragraph\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit class-balanced annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "5147f5d8-d2e7-415e-bdae-3f28490595f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jo7W3eQD1pe2g3cHXV2GfV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 289,
      "cache_read_input_tokens": 46187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 289
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

_source line 72 · 2026-05-15T12:38:07.683Z_

<details><summary>↩ Tool result · `toolu_01MuaWFsoFfVmMj1KVQBzYuY`</summary>

```text
[master 572894d] paper: W3 — add class-balanced subsample note to Metrics paragraph
 Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 1 insertion(+)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "31cdafc8-9606-49e6-ae21-168d1eb9ecd6",
  "tool_use_result": {
    "stdout": "[master 572894d] paper: W3 — add class-balanced subsample note to Metrics paragraph\n Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 1 file changed, 1 insertion(+)",
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

_source line 73_

Now sync all modified files to docs/paper/.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "745374bf-2a04-4184-ad63-aa1a0c7ddf18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcaQ8hJs9e1Vwdu7WdfVMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 46476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
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

_source line 74_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01FcWrLK3CvbRcv6CximeWrt`</summary>

```json
{
  "todos": [
    {
      "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
      "status": "completed",
      "activeForm": "Updating CI width and values across all .tex files"
    },
    {
      "content": "W3: Add topic drift paragraph to discussion.tex",
      "status": "completed",
      "activeForm": "Adding topic drift paragraph to discussion.tex"
    },
    {
      "content": "W3: Add class-balanced annotation to method.tex",
      "status": "completed",
      "activeForm": "Adding class-balanced annotation to method.tex"
    },
    {
      "content": "Sync modified files to docs/paper/ and commit",
      "status": "in_progress",
      "activeForm": "Syncing modified files to docs/paper/"
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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "164f8120-73b4-43cc-b6f4-dc8ce41e0785",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcaQ8hJs9e1Vwdu7WdfVMq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 311,
      "cache_read_input_tokens": 46476,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 311
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

_source line 75 · 2026-05-15T12:38:13.107Z_

<details><summary>↩ Tool result · `toolu_01FcWrLK3CvbRcv6CximeWrt`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "6c6e7d27-ec1f-4d7b-b8d6-419e9a611e34",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "completed",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "in_progress",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/",
        "status": "pending",
        "activeForm": "Syncing modified files to docs/paper/"
      },
      {
        "content": "Git commits for each change",
        "status": "pending",
        "activeForm": "Creating git commits"
      }
    ],
    "newTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "completed",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "completed",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/ and commit",
        "status": "in_progress",
        "activeForm": "Syncing modified files to docs/paper/"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 76_

<details open><summary>🔧 Tool call — Bash · `toolu_01Q77kkEtE5LjTNrWSGSvrpf`</summary>

```json
{
  "command": "cp artifacts/_project/paper/main.tex docs/paper/main.tex && cp artifacts/_project/paper/abstract.tex docs/paper/abstract.tex && cp artifacts/_project/paper/introduction.tex docs/paper/introduction.tex && cp artifacts/_project/paper/discussion.tex docs/paper/discussion.tex && cp artifacts/_project/paper/results.tex docs/paper/results.tex && cp artifacts/_project/paper/method.tex docs/paper/method.tex",
  "description": "Copy modified tex files to docs/paper/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "41ad0479-f7ff-4f23-b7ea-e55a1327e3fd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xf9e7Jse68hQGhdXeQbTUh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 46787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 279
      },
      "output_tokens": 48,
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

_source line 77 · 2026-05-15T12:38:16.524Z_

<details><summary>↩ Tool result · `toolu_01Q77kkEtE5LjTNrWSGSvrpf`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "340c6597-cbb3-408f-aac2-202186bf00f9",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": true
  }
}
```

</details>

---

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — Bash · `toolu_01GxWGvf2nfLaHrdAa8gTPYB`</summary>

```json
{
  "command": "git add docs/paper/main.tex docs/paper/abstract.tex docs/paper/introduction.tex docs/paper/discussion.tex docs/paper/results.tex docs/paper/method.tex && git commit -m \"$(cat <<'EOF'\npaper: sync W11/W3 changes to docs/paper/\n\nCo-Authored-By: Claude Opus 4.6 &lt;noreply@anthropic.com>\nEOF\n)\"",
  "description": "Commit docs/paper sync"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "5a02cec5-a1a8-43d3-a61b-8edb448df474",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW52sZR5x8xvRZ5CDNLayY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 201,
      "cache_read_input_tokens": 47066,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 201
      },
      "output_tokens": 70,
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

_source line 79 · 2026-05-15T12:38:19.956Z_

<details><summary>↩ Tool result · `toolu_01GxWGvf2nfLaHrdAa8gTPYB`</summary>

```text
[master 9815fef] paper: sync W11/W3 changes to docs/paper/
 Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 6 files changed, 15 insertions(+), 6 deletions(-)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "e11bb112-7e80-4237-809e-40cf1167a81f",
  "tool_use_result": {
    "stdout": "[master 9815fef] paper: sync W11/W3 changes to docs/paper/\n Committer: Ubuntu &lt;ubuntu@ip-172-31-15-53.ap-northeast-1.compute.internal>\nYour name and email address were configured automatically based\non your username and hostname. Please check that they are accurate.\nYou can suppress this message by setting them explicitly. Run the\nfollowing command and follow the instructions in your editor to edit\nyour configuration file:\n\n    git config --global --edit\n\nAfter doing this, you may fix the identity used for this commit with:\n\n    git commit --amend --reset-author\n\n 6 files changed, 15 insertions(+), 6 deletions(-)",
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

_source line 80_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01LG183xCcktLMSdK8XXQw9f`</summary>

```json
{
  "todos": [
    {
      "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
      "status": "completed",
      "activeForm": "Updating CI width and values across all .tex files"
    },
    {
      "content": "W3: Add topic drift paragraph to discussion.tex",
      "status": "completed",
      "activeForm": "Adding topic drift paragraph to discussion.tex"
    },
    {
      "content": "W3: Add class-balanced annotation to method.tex",
      "status": "completed",
      "activeForm": "Adding class-balanced annotation to method.tex"
    },
    {
      "content": "Sync modified files to docs/paper/ and commit",
      "status": "completed",
      "activeForm": "Syncing modified files to docs/paper/"
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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "f7403dc6-e888-4837-874f-46892bfc205e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VhWhimvTcBKjcLoS9SFmTL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 349,
      "cache_read_input_tokens": 47267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 349
      },
      "output_tokens": 73,
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

_source line 81 · 2026-05-15T12:38:23.048Z_

<details><summary>↩ Tool result · `toolu_01LG183xCcktLMSdK8XXQw9f`</summary>

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
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "f4a854d2-485c-4692-a65f-4bae06093332",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "completed",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "completed",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/ and commit",
        "status": "in_progress",
        "activeForm": "Syncing modified files to docs/paper/"
      }
    ],
    "newTodos": [
      {
        "content": "W11: Update CI width 1.4pp → 0.9pp and CI values across all .tex files",
        "status": "completed",
        "activeForm": "Updating CI width and values across all .tex files"
      },
      {
        "content": "W3: Add topic drift paragraph to discussion.tex",
        "status": "completed",
        "activeForm": "Adding topic drift paragraph to discussion.tex"
      },
      {
        "content": "W3: Add class-balanced annotation to method.tex",
        "status": "completed",
        "activeForm": "Adding class-balanced annotation to method.tex"
      },
      {
        "content": "Sync modified files to docs/paper/ and commit",
        "status": "completed",
        "activeForm": "Syncing modified files to docs/paper/"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 82_

完成。汇总如下：

---

### Commits

| Commit | Hash | 内容 |
|--------|------|------|
| W11 | `91c9e8e` | CI width 统一为 6-gen 0.9pp |
| W3 (topic drift) | `b5d0c42` | Discussion 加 topic drift mediator 段落 |
| W3 (class-balanced) | `572894d` | Method 加 class-balanced subsample 注释 |
| sync | `9815fef` | 同步到 docs/paper/ |

### W11 — "1.4" 出现位置及处理

| 文件 | 行 | 内容 | 处理 |
|------|-----|------|------|
| `main.tex:26` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `abstract.tex:8` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `introduction.tex:24` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `discussion.tex:22` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `results.tex:107` | caption `spans 1.4\,pp` | → `spans $<$\,1\,pp` |
| `results.tex:134` | `1.4\,pp [0.786, 0.800]` | → `0.9\,pp [0.783, 0.792]` |
| `appendix_prompt_type.tex:7` | `1.4%` (elaboration drift rate) | **不改** — 无关 |
| `table4.tex:8` / `table4_49aebb.tex:8` | `$-$1.40` (log-prob值) | **不改** — 无关 |

### W11 — CI 值更新

- `results.tex` 正文: `[0.786, 0.800]` → `[0.783, 0.792]`
- Table 3 (`tab:baselines`): **保持 5-gen 口径** `0.800 [0.786, 0.800]` 不动
- 新增 6-gen 报告句: "Across all six generators including Qwen3-8B, the ensemble achieves F1=0.789 with a 95% CI of [0.783, 0.792] (width 0.9pp)."

### W3 — Topic drift 段落

添加到 `discussion.tex`，在 "Connection to model collapse" 段落之后。

### Class-balanced 注释

添加到 `method.tex` "Metrics and statistical testing" 段末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "uuid": "1bd74a12-1c49-4563-8df8-1aed6c92999c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MZ1HWtciaWEjGFijXHoHGe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 266,
      "cache_read_input_tokens": 47616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 266
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

_source line 83_

完成。汇总如下：

---

### Commits

| Commit | Hash | 内容 |
|--------|------|------|
| W11 | `91c9e8e` | CI width 统一为 6-gen 0.9pp |
| W3 (topic drift) | `b5d0c42` | Discussion 加 topic drift mediator 段落 |
| W3 (class-balanced) | `572894d` | Method 加 class-balanced subsample 注释 |
| sync | `9815fef` | 同步到 docs/paper/ |

### W11 — "1.4" 出现位置及处理

| 文件 | 行 | 内容 | 处理 |
|------|-----|------|------|
| `main.tex:26` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `abstract.tex:8` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `introduction.tex:24` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `discussion.tex:22` | `CI width 1.4\,pp` | → `CI width $<$\,1\,pp` |
| `results.tex:107` | caption `spans 1.4\,pp` | → `spans $<$\,1\,pp` |
| `results.tex:134` | `1.4\,pp [0.786, 0.800]` | → `0.9\,pp [0.783, 0.792]` |
| `appendix_prompt_type.tex:7` | `1.4%` (elaboration drift rate) | **不改** — 无关 |
| `table4.tex:8` / `table4_49aebb.tex:8` | `$-$1.40` (log-prob值) | **不改** — 无关 |

### W11 — CI 值更新

- `results.tex` 正文: `[0.786, 0.800]` → `[0.783, 0.792]`
- Table 3 (`tab:baselines`): **保持 5-gen 口径** `0.800 [0.786, 0.800]` 不动
- 新增 6-gen 报告句: "Across all six generators including Qwen3-8B, the ensemble achieves F1=0.789 with a 95% CI of [0.783, 0.792] (width 0.9pp)."

### W3 — Topic drift 段落

添加到 `discussion.tex`，在 "Connection to model collapse" 段落之后。

### Class-balanced 注释

添加到 `method.tex` "Metrics and statistical testing" 段末尾。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 179027,
  "duration_api_ms": 179736,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "863c4bf2-f699-41df-a731-ddf85242c204",
  "total_cost_usd": 1.0614467500000002,
  "usage": {
    "input_tokens": 37,
    "cache_creation_input_tokens": 36041,
    "cache_read_input_tokens": 1316891,
    "output_tokens": 7016,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36041,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 746,
        "cache_read_input_tokens": 47616,
        "cache_creation_input_tokens": 266,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 266
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2080,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0021599999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 37,
      "outputTokens": 7016,
      "cacheReadInputTokens": 1316891,
      "cacheCreationInputTokens": 36041,
      "webSearchRequests": 0,
      "costUSD": 1.05928675,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "37cec84c-2247-4f86-a10d-913023aa9a4c"
}
```

</details>

---
