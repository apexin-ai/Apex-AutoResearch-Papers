# audit all tables

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 63
- **Recorded user turns:** 0
- **Tool calls:** 23
- **Original source:** `logs/workers/worker_audit_all_tables_20260524T045119.log`
- **Structured JSON:** [`7a83750cd47ac56731aa.json`](../../sessions/7a/7a83750cd47ac56731aa.json)

## Before a recorded user message

63 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
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
    "mcp__agent-ml-research__read_registry",
    "mcp__agent-ml-research__register_artifact",
    "mcp__agent-ml-research__update_registry"
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
  "uuid": "4346a032-3705-4dc2-a436-7b28fe3d0156",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1779616200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "701dfdce-a2d0-4198-ad02-ad64360b57de",
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb"
}
```

---

### Assistant

_source line 4_

I'll start by reading the table files and querying the registry in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "765deed0-3e24-4d98-8125-da1050cf2c15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW9NS5ndpYhGpsV19VE6cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

<details open><summary>🔧 Tool call — Bash · `toolu_011mcRqE4HSUZeTcP5jQaju2`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/*.tex 2>/dev/null",
  "description": "List table tex files in docs/paper/tables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "2215211a-00cb-49b1-8c98-3a9304287568",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW9NS5ndpYhGpsV19VE6cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

_source line 6 · 2026-05-24T04:51:34.528Z_

<details><summary>↩ Tool result · `toolu_011mcRqE4HSUZeTcP5jQaju2`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "6a1fa049-38f5-4ede-8d47-9d83b02de868",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex\n/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
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

_source line 7_

<details open><summary>🔧 Tool call — Bash · `toolu_01YMqi7RcLn9sqe1VMjZDwoF`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/*.tex 2>/dev/null",
  "description": "List table tex files in paper/tables"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "94495cd9-2386-49e9-bd64-9a419c0cc1a1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW9NS5ndpYhGpsV19VE6cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

_source line 8 · 2026-05-24T04:51:35.397Z_

<details><summary>↩ Tool result · `toolu_01YMqi7RcLn9sqe1VMjZDwoF`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/tab_math500.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "f78cfe88-f7e0-472f-9937-e085ff2cde41",
  "tool_use_result": {
    "stdout": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/tab_math500.tex",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019sY2aMEUXfUaU8YGFDqqJA`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_registry",
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
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "066835d1-0c5a-455b-8415-4836113ab495",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CW9NS5ndpYhGpsV19VE6cu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12929,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12929
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

_source line 10 · 2026-05-24T04:51:36.224Z_

<details><summary>↩ Tool result · `toolu_019sY2aMEUXfUaU8YGFDqqJA`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_registry"
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
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "9cd0d7ed-8e24-4ca7-9ef0-655c4bccabd5",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_registry"
    ],
    "query": "select:mcp__agent-ml-research__read_registry",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 11_

<details><summary>Logged reasoning block</summary>

```text
Let me read all the table files and query the registry in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "e9ff9793-4a35-4590-9f9b-3b9ed9c0b40d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

Reading all 8 table files and querying the registry simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "4ff1efd6-d2f9-483f-a1f2-d8c9a1b06d8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

<details open><summary>🔧 Tool call — Read · `toolu_01HHuNbN3oTrihZZUsizZ6VS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "f81f6def-9f06-446a-bb3c-cf27d49cdda5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 14 · 2026-05-24T04:51:39.757Z_

<details><summary>↩ Tool result · `toolu_01HHuNbN3oTrihZZUsizZ6VS`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\% sparsity under identical configuration (lr $1{\times}10^{-6}$, $\beta{=}0.01$, $T{=}0.4$, 1{,}024-token limit, 100 steps); Random uses TRL default 512-token limit, making it a conservative comparison point. $f_0$: fraction of batches where all completions receive identical reward (lower = healthier). Best in \textbf{bold}.}
5	\label{tab:recovery_gradient}
6	\resizebox{\columnwidth}{!}{%
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	Method & Peak Rew.\,$\uparrow$ & Mean Rew.\,$\uparrow$ & Min $f_0$\,$\downarrow$ & Behavior \\
10	\midrule
11	CKA-only & \textbf{0.354} & \textbf{0.285} & \textbf{0.125} & Active learning \\
12	Random & 0.190 & 0.164 & 0.300 & Stagnation \\
13	Standard & 0.081 & 0.050 & 0.500 & Borderline collapse \\
14	\rasp{} ($\alpha{=}1.0$)$^\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\
15	\bottomrule
16	\multicolumn{5}{l}{\footnotesize $^\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\ref{tab:decoupling}).}
17	\end{tabular}}
18	\end{table}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "47387e75-af3d-4299-a357-02986f8e4adb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab1_recovery_gradient.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Recovery capacity spectrum: GRPO dynamics for four pruning criteria at 20\\% sparsity under identical configuration (lr $1{\\times}10^{-6}$, $\\beta{=}0.01$, $T{=}0.4$, 1{,}024-token limit, 100 steps); Random uses TRL default 512-token limit, making it a conservative comparison point. $f_0$: fraction of batches where all completions receive identical reward (lower = healthier). Best in \\textbf{bold}.}\n\\label{tab:recovery_gradient}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nMethod & Peak Rew.\\,$\\uparrow$ & Mean Rew.\\,$\\uparrow$ & Min $f_0$\\,$\\downarrow$ & Behavior \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{0.285} & \\textbf{0.125} & Active learning \\\\\nRandom & 0.190 & 0.164 & 0.300 & Stagnation \\\\\nStandard & 0.081 & 0.050 & 0.500 & Borderline collapse \\\\\n\\rasp{} ($\\alpha{=}1.0$)$^\\ddagger$ & 0.061 & 0.031 & 0.675 & Full collapse \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$Single seed ($N{=}1$). CKA-only, Standard, and Random validated with 3 seeds (Table~\\ref{tab:decoupling}).}\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 19,
      "startLine": 1,
      "totalLines": 19
    }
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Read · `toolu_011qajT1RoafcZpjUjShnAZv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "7c1b6167-5ba7-403e-9135-cd25efea84af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 16 · 2026-05-24T04:51:40.837Z_

<details><summary>↩ Tool result · `toolu_011qajT1RoafcZpjUjShnAZv`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding), evaluated at step 100. All methods share identical GRPO configuration (Table~\ref{tab:hyperparams}), except Random which uses TRL default 512-token limit. CKA-only, Standard, and Random report mean $\pm$ std over 3 GRPO seeds; \rasp{} uses a single seed. Best in \textbf{bold}.}
5	\label{tab:decoupling}
6	\resizebox{\columnwidth}{!}{%
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	Model & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) & Peak Rew. \\
10	\midrule
11	Unpruned & \textbf{81.27} & \textbf{81.27} & $\phantom{-}$0.00 & \textbf{0.669} \\
12	CKA-only 20\% & 63.91 & 64.39{\scriptsize$\pm$0.19} & $+$0.48 & 0.354 \\
13	Standard 20\% & 59.29 & 59.84{\scriptsize$\pm$0.38} & $+$0.55 & 0.081 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\
15	Random 20\% & 51.25 & 50.72{\scriptsize$\pm$0.15} & $-$0.53 & 0.190 \\
16	\midrule
17	ShortGPT 20\%$^\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\
18	\bottomrule
19	\multicolumn{5}{l}{\footnotesize $^\dagger$Depth pruning baseline~\citep{shortgpt2024}; removes entire layers.} \\
20	\end{tabular}}
21	\end{table}
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "1a56d2ee-55e8-4101-83c4-4923725bd49f",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab2_decoupling.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{GRPO responsiveness on GSM8K ($N{=}1{,}319$, greedy decoding), evaluated at step 100. All methods share identical GRPO configuration (Table~\\ref{tab:hyperparams}), except Random which uses TRL default 512-token limit. CKA-only, Standard, and Random report mean $\\pm$ std over 3 GRPO seeds; \\rasp{} uses a single seed. Best in \\textbf{bold}.}\n\\label{tab:decoupling}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) & Peak Rew. \\\\\n\\midrule\nUnpruned & \\textbf{81.27} & \\textbf{81.27} & $\\phantom{-}$0.00 & \\textbf{0.669} \\\\\nCKA-only 20\\% & 63.91 & 64.39{\\scriptsize$\\pm$0.19} & $+$0.48 & 0.354 \\\\\nStandard 20\\% & 59.29 & 59.84{\\scriptsize$\\pm$0.38} & $+$0.55 & 0.081 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 61.49 & 60.88 & $-$0.61 & 0.061 \\\\\nRandom 20\\% & 51.25 & 50.72{\\scriptsize$\\pm$0.15} & $-$0.53 & 0.190 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 44.73 & 43.37 & $-$1.36 & -- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$Depth pruning baseline~\\citep{shortgpt2024}; removes entire layers.} \\\\\n\\end{tabular}}\n\\end{table}\n",
      "numLines": 22,
      "startLine": 1,
      "totalLines": 22
    }
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Read · `toolu_01Q7gNB2J8HNbhf8n4wfEg3H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "baab1696-a2e2-43d3-93d7-de89cb639af3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 18 · 2026-05-24T04:51:41.202Z_

<details><summary>↩ Tool result · `toolu_01Q7gNB2J8HNbhf8n4wfEg3H`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{Cross-scale validation at 20\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\ Table~\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}
5	\label{tab:cross_scale}
6	\resizebox{\columnwidth}{!}{%
7	\begin{tabular}{@{}lcccc@{}}
8	\toprule
9	\multirow{2}{*}{Method} & \multicolumn{2}{c}{7B} & \multicolumn{2}{c}{1.5B} \\
10	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
11	 & Peak Rew. & GSM8K\,(\%) & Rew. & GSM8K\,(\%) \\
12	\midrule
13	CKA-only & \textbf{0.354} & \textbf{64.39} & \textbf{0.238} & \textbf{35.48} \\
14	Standard & 0.081 & 59.84 & 0.084 & 22.29 \\
15	\rasp{} ($\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\
16	Random & 0.190 & -- & -- & -- \\
17	\bottomrule
18	\end{tabular}}
19	\end{table}
20	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "bc01dc8f-e7f6-4bf2-be05-95cf6c36e6c9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab5_cross_scale.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-scale validation at 20\\% sparsity. 7B: DeepSeek-R1-Distill-Qwen-7B (GSM8K mean over 3 seeds for CKA-only and Standard; see Table~\\ref{tab:decoupling}). 1.5B: DeepSeek-R1-Distill-Qwen-1.5B (single seed). GSM8K accuracy ($N{=}1{,}319$). 7B reward = peak across 100 GRPO steps (cf.\\ Table~\\ref{tab:recovery_gradient}); 1.5B reward = mean across training steps.}\n\\label{tab:cross_scale}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n\\multirow{2}{*}{Method} & \\multicolumn{2}{c}{7B} & \\multicolumn{2}{c}{1.5B} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Peak Rew. & GSM8K\\,(\\%) & Rew. & GSM8K\\,(\\%) \\\\\n\\midrule\nCKA-only & \\textbf{0.354} & \\textbf{64.39} & \\textbf{0.238} & \\textbf{35.48} \\\\\nStandard & 0.081 & 59.84 & 0.084 & 22.29 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 0.061 & 60.88 & 0.099 & 26.16 \\\\\nRandom & 0.190 & -- & -- & -- \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n",
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

<details open><summary>🔧 Tool call — Read · `toolu_01J61rUL1eXvNhgb4PHjRVSJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "924dcc3d-0002-482a-a904-2c20a101f07e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 20 · 2026-05-24T04:51:41.676Z_

<details><summary>↩ Tool result · `toolu_01J61rUL1eXvNhgb4PHjRVSJ`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{CKA scoring stability across calibration sizes. Spearman $\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\rho \geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}
5	\label{tab:cka_stability}
6	\begin{tabular}{@{}lcc@{}}
7	\toprule
8	Calibration Sizes & Spearman $\rho$ (min) & Spearman $\rho$ (mean) \\
9	\midrule
10	256 / 512 / 1024 & 0.964 & 0.979 \\
11	\bottomrule
12	\end{tabular}
13	\end{table}
14	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "cf61a2b3-0052-4dc1-a87d-cc26611f869b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_cka_stability.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{CKA scoring stability across calibration sizes. Spearman $\\rho$ between structure rankings produced by different calibration set sizes. High correlation ($\\rho \\geq 0.964$) indicates that CKA-based scoring is robust to calibration data volume.}\n\\label{tab:cka_stability}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nCalibration Sizes & Spearman $\\rho$ (min) & Spearman $\\rho$ (mean) \\\\\n\\midrule\n256 / 512 / 1024 & 0.964 & 0.979 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 14,
      "startLine": 1,
      "totalLines": 14
    }
  }
}
```

</details>

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_01JzgKuoLLPn1muz5xqx9ai8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "8e6549b7-43ed-4a2b-8d85-30cca30e391c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 22 · 2026-05-24T04:51:42.163Z_

<details><summary>↩ Tool result · `toolu_01JzgKuoLLPn1muz5xqx9ai8`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \texttt{max\_new\_tokens=2048}). CKA-only and Standard both outperform \rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\,pp (vs.\ 4.6\,pp on GSM8K), consistent with a difficulty-driven floor effect. Best SFT in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & \multicolumn{3}{c}{53.0\,$^\dagger$} \\
11	\midrule
12	\multicolumn{4}{l}{\textit{20\% sparsity --- method comparison}} \\
13	CKA-only & \textbf{27.4} & 27.6 & $+$0.2 \\
14	Standard & 23.4 & 27.0 & $+$3.6 \\
15	\rasp{} ($\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\
16	Random & 14.4 & 13.4 & $-$1.0 \\
17	\midrule
18	\multicolumn{4}{l}{\textit{20\% sparsity --- $\alpha$ dose-response}} \\
19	$\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\
20	$\alpha{=}2.0$ & 25.6 & 27.4 & $+$1.8 \\
21	$\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\
22	$\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\
23	\midrule
24	\multicolumn{4}{l}{\textit{25\% sparsity}} \\
25	CKA-only & 19.2 & 18.4 & $-$0.8 \\
26	Standard & 14.0 & 12.8 & $-$1.2 \\
27	\bottomrule
28	\multicolumn{4}{p{0.85\columnwidth}}{\footnotesize $^\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\% at 4096); all pruned models evaluated under the same constraint.}
29	\end{tabular}
30	\end{table}
31	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "3a72ace2-25bd-4e22-bf4a-86ea400f1102",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MATH-500 out-of-distribution evaluation ($N{=}500$, greedy decoding, \\texttt{max\\_new\\_tokens=2048}). CKA-only and Standard both outperform \\rasp{} and Random; the CKA-only--Standard GRPO gap is 0.6\\,pp (vs.\\ 4.6\\,pp on GSM8K), consistent with a difficulty-driven floor effect. Best SFT in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & \\multicolumn{3}{c}{53.0\\,$^\\dagger$} \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- method comparison}} \\\\\nCKA-only & \\textbf{27.4} & 27.6 & $+$0.2 \\\\\nStandard & 23.4 & 27.0 & $+$3.6 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 21.6 & 23.0 & $+$1.4 \\\\\nRandom & 14.4 & 13.4 & $-$1.0 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{20\\% sparsity --- $\\alpha$ dose-response}} \\\\\n$\\alpha{=}0.5$ & 25.4 & 24.8 & $-$0.6 \\\\\n$\\alpha{=}2.0$ & 25.6 & 27.4 & $+$1.8 \\\\\n$\\alpha{=}3.0$ & 23.2 & 22.8 & $-$0.4 \\\\\n$\\alpha{=}4.0$ & 26.6 & 26.2 & $-$0.4 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{25\\% sparsity}} \\\\\nCKA-only & 19.2 & 18.4 & $-$0.8 \\\\\nStandard & 14.0 & 12.8 & $-$1.2 \\\\\n\\bottomrule\n\\multicolumn{4}{p{0.85\\columnwidth}}{\\footnotesize $^\\dagger$Over half of Dense responses truncated at 2048 tokens (73.6\\% at 4096); all pruned models evaluated under the same constraint.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 31,
      "startLine": 1,
      "totalLines": 31
    }
  }
}
```

</details>

---

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01LEWaeFr7o17GZ5UKFW1jNs`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "827b255b-333c-4211-837e-bd95d31e12ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 24 · 2026-05-24T04:51:42.638Z_

<details><summary>↩ Tool result · `toolu_01LEWaeFr7o17GZ5UKFW1jNs`</summary>

```text
1	\begin{table}[h]
2	\centering
3	\small
4	\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\sim}$75\% code capability loss vs Dense), limiting differentiation (${\sim}$1\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\,pp) but at the 95\% CI boundary (stderr ${\approx}$1.55\,pp).}
5	\label{tab:mbpp}
6	\begin{tabular}{@{}lccc@{}}
7	\toprule
8	Method & SFT\,(\%) & GRPO\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	Dense & -- & 53.48 & -- \\
11	\midrule
12	CKA-only 20\% & 12.83 & 14.17 & $+$1.34 \\
13	Standard 20\% & 12.03 & 13.10 & $+$1.07 \\
14	\rasp{} ($\alpha{=}1.0$) 20\% & 11.76 & 13.10 & $+$1.34 \\
15	\midrule
16	ShortGPT 20\%$^\dagger$ & 10.43 & 14.44 & $+$4.01 \\
17	\bottomrule
18	\multicolumn{4}{l}{\footnotesize $^\dagger$Depth pruning; removes entire layers.}
19	\end{tabular}
20	\end{table}
21	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "c586065d-9a69-42fa-915a-58fde09b3054",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/tab_mbpp.tex",
      "content": "\\begin{table}[h]\n\\centering\n\\small\n\\caption{MBPP code generation accuracy ($N{=}374$, greedy decoding). All fine-grained pruning methods converge near a capability floor (${\\sim}$75\\% code capability loss vs Dense), limiting differentiation (${\\sim}$1\\,pp range, within stderr). ShortGPT shows a larger GRPO delta ($+$4.01\\,pp) but at the 95\\% CI boundary (stderr ${\\approx}$1.55\\,pp).}\n\\label{tab:mbpp}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & SFT\\,(\\%) & GRPO\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\nDense & -- & 53.48 & -- \\\\\n\\midrule\nCKA-only 20\\% & 12.83 & 14.17 & $+$1.34 \\\\\nStandard 20\\% & 12.03 & 13.10 & $+$1.07 \\\\\n\\rasp{} ($\\alpha{=}1.0$) 20\\% & 11.76 & 13.10 & $+$1.34 \\\\\n\\midrule\nShortGPT 20\\%$^\\dagger$ & 10.43 & 14.44 & $+$4.01 \\\\\n\\bottomrule\n\\multicolumn{4}{l}{\\footnotesize $^\\dagger$Depth pruning; removes entire layers.}\n\\end{tabular}\n\\end{table}\n",
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

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01VB3r8yeXKwrLRg4qoc7EW8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "db27c0a7-5a6a-487e-8e81-ea978faf227b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 26 · 2026-05-24T04:51:43.577Z_

<details><summary>↩ Tool result · `toolu_01VB3r8yeXKwrLRg4qoc7EW8`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{Dose-response analysis: effect of CKA coefficient $\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\% MLP channel sparsity. $\alpha{=}0$ reduces to Standard (importance-only); higher $\alpha$ weights representational diversity. Best in \textbf{bold}.}
5	\label{tab:alpha}
6	\begin{tabular}{@{}cccc@{}}
7	\toprule
8	$\alpha$ & SFT Acc.\,(\%) & GRPO Acc.\,(\%) & $\Delta$\,(pp) \\
9	\midrule
10	0.5 & 60.73 & 61.18 & $+$0.45 \\
11	1.0 & 61.49 & 60.88 & $-$0.61 \\
12	\textbf{2.0} & \textbf{64.97} & \textbf{66.11} & $+$1.14 \\
13	3.0 & 64.14 & 63.46 & $-$0.68 \\
14	4.0 & 61.94 & 62.77 & $+$0.83 \\
15	\bottomrule
16	\end{tabular}
17	\end{table}
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "47169ed9-2739-4ed5-9d0d-2d2ab0f839a3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table3_alpha.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{Dose-response analysis: effect of CKA coefficient $\\alpha$ on GSM8K accuracy ($N{=}1{,}319$) at 20\\% MLP channel sparsity. $\\alpha{=}0$ reduces to Standard (importance-only); higher $\\alpha$ weights representational diversity. Best in \\textbf{bold}.}\n\\label{tab:alpha}\n\\begin{tabular}{@{}cccc@{}}\n\\toprule\n$\\alpha$ & SFT Acc.\\,(\\%) & GRPO Acc.\\,(\\%) & $\\Delta$\\,(pp) \\\\\n\\midrule\n0.5 & 60.73 & 61.18 & $+$0.45 \\\\\n1.0 & 61.49 & 60.88 & $-$0.61 \\\\\n\\textbf{2.0} & \\textbf{64.97} & \\textbf{66.11} & $+$1.14 \\\\\n3.0 & 64.14 & 63.46 & $-$0.68 \\\\\n4.0 & 61.94 & 62.77 & $+$0.83 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01S6s8qpeqzP5hxhcdCWUEq1`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "f71e730d-ee14-457f-95a1-160a1f8238af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 28 · 2026-05-24T04:51:44.049Z_

<details><summary>↩ Tool result · `toolu_01S6s8qpeqzP5hxhcdCWUEq1`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\caption{Sparsity cliff at 30\% structured sparsity. All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\%.}
4	\label{tab:sparsity_cliff}
5	\begin{tabular}{@{}lccc@{}}
6	\toprule
7	Method & $N$ & Acc.\,(\%) & EOS Rate\,(\%) \\
8	\midrule
9	Standard & 200 & 4 & 5.5 \\
10	\rasp{} ($\alpha{=}1.0$) & 200 & 0 & 3.0 \\
11	CKA-only & 500$^\dagger$ & 1.6 & --$^\dagger$ \\
12	\bottomrule
13	\multicolumn{4}{@{}l}{\footnotesize $^\dagger$Terminated early after collapse confirmed; 8/500 correct.}
14	\end{tabular}
15	\end{table}
16	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "b3594b88-2668-48cc-be19-5c5112699974",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/docs/paper/tables/table4_sparsity_cliff.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\caption{Sparsity cliff at 30\\% structured sparsity. All tested pruning criteria collapse, with near-zero accuracy and EOS generation rates below 6\\%.}\n\\label{tab:sparsity_cliff}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nMethod & $N$ & Acc.\\,(\\%) & EOS Rate\\,(\\%) \\\\\n\\midrule\nStandard & 200 & 4 & 5.5 \\\\\n\\rasp{} ($\\alpha{=}1.0$) & 200 & 0 & 3.0 \\\\\nCKA-only & 500$^\\dagger$ & 1.6 & --$^\\dagger$ \\\\\n\\bottomrule\n\\multicolumn{4}{@{}l}{\\footnotesize $^\\dagger$Terminated early after collapse confirmed; 8/500 correct.}\n\\end{tabular}\n\\end{table}\n",
      "numLines": 16,
      "startLine": 1,
      "totalLines": 16
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Read · `toolu_01TDDUWwEizKPducLPfSJxa2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/tab_math500.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "ff85a7ee-ee0b-47de-8208-8aadfd0967dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 30 · 2026-05-24T04:51:44.493Z_

<details><summary>↩ Tool result · `toolu_01TDDUWwEizKPducLPfSJxa2`</summary>

```text
1	\begin{table}[t]
2	\centering
3	\small
4	\caption{MATH-500 accuracy (\%) and truncation rate (\%) under different pruning methods and recovery strategies. Sparsity = 20\% unless noted. Best pruned-model accuracy per column in \textbf{bold}.}
5	\label{tab:math500}
6	\begin{tabular}{l cc cc}
7	\toprule
8	& \multicolumn{2}{c}{\textbf{Post-SFT}} & \multicolumn{2}{c}{\textbf{Post-GRPO}} \\
9	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
10	Method & Acc & Trunc & Acc & Trunc \\
11	\midrule
12	    Dense (unpruned) & 73.6 & 24.8 & 69.0 & 17.2 \\
13	\midrule
14	    Standard & -- & -- & 27.0 & -- \\
15	    Random & -- & -- & -- & -- \\
16	    CKA-only & \textbf{27.4} & 23.2 & \textbf{27.6} & -- \\
17	    RASP ($\alpha\!=\!1.0$) & 21.6 & -- & 23.0 & 36.0 \\
18	\midrule
19	\multicolumn{5}{l}{\textit{Dose-response ($\alpha$ sweep, 20\% sparsity)}} \\
20	    $\alpha = 0.5$ & -- & -- & -- & -- \\
21	    $\alpha = 1.0$ & 21.6 & -- & 23.0 & 36.0 \\
22	    $\alpha = 2.0$ & \textbf{25.6} & 31.0 & \textbf{27.4} & 30.2 \\
23	    $\alpha = 3.0$ & -- & -- & -- & -- \\
24	    $\alpha = 4.0$ & -- & -- & -- & -- \\
25	\midrule
26	\multicolumn{5}{l}{\textit{25\% sparsity}} \\
27	    Standard (25\%) & -- & -- & -- & -- \\
28	    CKA-only (25\%) & -- & -- & \textbf{17.6} & 26.6 \\
29	\bottomrule
30	\end{tabular}
31	\end{table}
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "956185f3-f99c-4c0e-b8f7-0a5624bf7ef9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/paper/tables/tab_math500.tex",
      "content": "\\begin{table}[t]\n\\centering\n\\small\n\\caption{MATH-500 accuracy (\\%) and truncation rate (\\%) under different pruning methods and recovery strategies. Sparsity = 20\\% unless noted. Best pruned-model accuracy per column in \\textbf{bold}.}\n\\label{tab:math500}\n\\begin{tabular}{l cc cc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{Post-SFT}} & \\multicolumn{2}{c}{\\textbf{Post-GRPO}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMethod & Acc & Trunc & Acc & Trunc \\\\\n\\midrule\n    Dense (unpruned) & 73.6 & 24.8 & 69.0 & 17.2 \\\\\n\\midrule\n    Standard & -- & -- & 27.0 & -- \\\\\n    Random & -- & -- & -- & -- \\\\\n    CKA-only & \\textbf{27.4} & 23.2 & \\textbf{27.6} & -- \\\\\n    RASP ($\\alpha\\!=\\!1.0$) & 21.6 & -- & 23.0 & 36.0 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{Dose-response ($\\alpha$ sweep, 20\\% sparsity)}} \\\\\n    $\\alpha = 0.5$ & -- & -- & -- & -- \\\\\n    $\\alpha = 1.0$ & 21.6 & -- & 23.0 & 36.0 \\\\\n    $\\alpha = 2.0$ & \\textbf{25.6} & 31.0 & \\textbf{27.4} & 30.2 \\\\\n    $\\alpha = 3.0$ & -- & -- & -- & -- \\\\\n    $\\alpha = 4.0$ & -- & -- & -- & -- \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{25\\% sparsity}} \\\\\n    Standard (25\\%) & -- & -- & -- & -- \\\\\n    CKA-only (25\\%) & -- & -- & \\textbf{17.6} & 26.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_registry · `toolu_01NR2EZd6UCgiyM98AtRxEn9`</summary>

```json
{
  "project": "recovery_aware_struct_prune",
  "filters": {
    "status": "DONE",
    "conclusion": "success"
  },
  "fields": [
    "exp_id",
    "status",
    "conclusion",
    "metrics",
    "spec"
  ],
  "limit": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "bd18bdb7-db7a-4a08-950b-81000e9d1aa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QbMKwnu3ypAEiQAUHdJ8Da",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1139,
      "cache_read_input_tokens": 24770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1139
      },
      "output_tokens": 20,
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

_source line 32 · 2026-05-24T04:51:48.219Z_

<details><summary>↩ Tool result · `toolu_01NR2EZd6UCgiyM98AtRxEn9`</summary>

```text
Error: result (263,858 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "5c412599-57ba-416d-a084-b9ac1dd28187",
  "tool_use_result": {
    "content": "Error: result (263,858 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt.\nFormat: JSON with schema: {result: string}\n- For targeted queries (find a value, filter by field): use jq on the file directly.\n- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.\n- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. \"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim.\" A vague \"summarize this\" may lose detail.\n",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_rasp_alpha2p0_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": \"171964\", \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"sft_rasp_alpha2p0_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.256, \"n_correct\": 128, \"n_total\": 500, \"stderr\": 0.01952, \"truncated\": 155, \"natural_eos\": 345, \"truncated_pct\": 0.31, \"avg_response_length\": 805.754}}, \"eval_math500_grpo_rasp_alpha2p0_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"168524\", \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500\", \"model_name\": \"grpo_rasp_alpha2p0_20\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"n_correct\": 137, \"n_total\": 500, \"truncated_pct\": 0.302, \"truncated\": 151, \"natural_eos\": 349}}, \"eval_math500_grpo_cka_only_25_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_25_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"pid\": \"168451\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"model_name\": \"grpo_cka_only_25\", \"seed\": 42, \"data_path\": \"MATH-500\", \"data_count\": 500}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.176, \"n_correct\": 88, \"n_total\": 500, \"stderr\": 0.017, \"natural_eos\": 367, \"truncated\": 133, \"truncated_pct\": 0.266, \"avg_response_length\": 719.35}}, \"eval_math500_grpo_cka_only_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_fixed.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"321423\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_20_fixed.log\", \"submitted_at\": \"2026-05-23T19:35:48.851Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 13096.9, \"gpu_hours\": 3.64}, \"metrics\": {\"accuracy\": 0.276, \"n_correct\": 138, \"n_total\": 500, \"stderr\": 0.02}, \"conclusion\": \"success\"}, \"eval_math500_grpo_standard_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:2\"], \"pid\": \"142477\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fixed.log\", \"submitted_at\": \"2026-05-23T15:04:04.656Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"data_count\": 500, \"data_path\": \"hendrycks/MATH (500 test)\", \"seed\": 42, \"wall_clock_seconds\": 25695.5, \"gpu_hours\": 7.14}, \"conclusion\": \"success\", \"metrics\": {\"math500_acc\": 0.27, \"math500_correct\": 135, \"math500_total\": 500, \"math500_stderr\": 0.0199, \"natural_eos\": 278, \"truncated\": 222, \"avg_response_length\": 1127.844}}, \"eval_math500_grpo_rasp_alpha1p0_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha1p0_20_fixed.json\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"145167\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20_fixed.log\", \"submitted_at\": \"2026-05-23T15:45:38.369Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 20452.8, \"gpu_hours\": 5.68}, \"metrics\": {\"accuracy\": 0.23, \"n_correct\": 115, \"n_total\": 500, \"stderr\": 0.0188, \"natural_eos\": 320, \"truncated\": 180, \"avg_response_length\": 903.536}, \"conclusion\": \"success\"}, \"eval_math500_sft_cka_only_20_fixed_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_cka_only_20_fixed.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"306963\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_20_fixed_v2.log\", \"submitted_at\": \"2026-05-23T15:45:23.180Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 14242.7, \"gpu_hours\": 3.96}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"num_correct\": 137, \"num_total\": 500, \"stderr\": 0.02, \"truncated_pct\": 0.232}}, \"grpo_random_20_retrain_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_retrain --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"309964\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20_retrain_v2.log\", \"submitted_at\": \"2026-05-23T16:17:44.194Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 11246.3, \"gpu_hours\": 3.12}, \"conclusion\": \"success\", \"metrics\": {\"final_reward\": 0.2875, \"final_reward_std\": 0.4291, \"final_loss\": 0.06684, \"final_kl\": 0.004236, \"final_entropy\": 0.1704, \"final_completion_length_mean\": 189.1, \"final_grad_norm\": 5.531, \"frac_reward_zero_std\": 0.4, \"wandb_run_id\": \"9c16hnf7\", \"wandb_run_name\": \"grpo_sft_random_20\", \"training_steps\": 100, \"training_time_hours\": 3.07}}, \"eval_math500_sft_rasp_alpha1p0_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_20_westd, α=1.0)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"sft_rasp_20_westd\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha1p0_20_fixed.json --seed 42 --dtype bfloat16\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"147914\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"num_correct\": 108, \"num_total\": 500}}, \"grpo_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"clipped_ratio\": 0.92, \"collapse_pattern\": \"near_total_collapse\", \"comparison_vs_rasp_25\": \"worse_than_rasp_25(0.009)\", \"kl_final\": 0.0012, \"reward_final\": 0.0075, \"total_steps\": 100, \"wall_clock_min\": 44, \"wandb_run_id\": \"16vqw4e6\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_standard_25 --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:1\", \"hypothesis\": \"DeepSeek-R1-Distill-Qwen-7B Standard 25% GRPO (100 steps). 25% Standard 对照，配合 grpo_rasp_25 (frac_zero=0.875)。Parent: sft_standard_25_westd.\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned, SFT recovered)\", \"parent\": \"sft_standard_25_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_standard_25_retrain\": {\"status\": \"DONE\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_sft_warmup.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu_id 0 --num_epochs 2 --lr 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --logging_steps 10\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"148228\", \"model_name\": \"pruned_standard_25\", \"data_path\": \"MATH-train (SFT)\", \"data_count\": 7500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_retrain.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.8584, \"token_accuracy\": 0.8, \"steps\": 1870, \"epochs\": 2}}, \"floor_ablation_0p6_cka_only_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.6 0\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"132494\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p6_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T12:10:29.192Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.6/checkpoint-100/\", \"wall_clock_seconds\": 15818.8, \"gpu_hours\": 4.39}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6202, \"gsm8k_correct\": 818, \"gsm8k_total\": 1319, \"gsm8k_ci\": 0.0134, \"eos_rate\": 0.9803, \"avg_response_length\": 252.7, \"grpo_train_loss\": 0.006503, \"grpo_final_reward\": 0.2419}}, \"eval_gsm8k_grpo_cka_only_20_verify\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --max_samples 1319 --max_new_tokens 4096 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_verify.json\\\"\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"300394\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_verify.log\", \"submitted_at\": \"2026-05-23T13:51:48.865Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"wall_clock_seconds\": 8580.2, \"gpu_hours\": 2.38}, \"metrics\": {\"accuracy\": 0.6406, \"n_correct\": 845, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9894, \"avg_response_length\": 201.76, \"original_accuracy\": 0.6437, \"accuracy_diff_pp\": -0.31}, \"conclusion\": \"success\"}, \"eval_math500_sft_standard_20_2048_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"ghost entry - never started\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MATH-500\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"checkpoint_path\": \"\", \"log_path\": \"\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.234, \"math500_correct\": 117, \"math500_total\": 500}}, \"floor_ablation_0p5_cka_only_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.5 3\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"120474\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p5_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T09:23:11.382Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.5/checkpoint-100/\", \"wall_clock_seconds\": 12306.9, \"gpu_hours\": 3.42}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6171, \"gsm8k_correct\": 814, \"gsm8k_total\": 1319, \"eos_rate\": 0.992}}, \"floor_ablation_0p3_cka_only_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 bash scripts/run_floor_ablation.sh 0.3 0\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"120742\", \"log_path\": \"~/runs/recovery_aware_struct_prune/floor_ablation_0p3_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-23T09:23:26.593Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"MATH-train (SFT) + GSM8K (eval)\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_floor_0.3/checkpoint-100/\", \"wall_clock_seconds\": 9867.1, \"gpu_hours\": 2.74}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6505, \"gsm8k_correct\": 858, \"gsm8k_total\": 1319}}, \"eval_postprune_qwen_math_standard_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_qwen_math/ --max_samples 200\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B (pruned_standard_20)\", \"seed\": 42, \"checkpoint_source\": \"pruned_standard_20_qwen_math\", \"eval_data\": \"gsm8k test N=200\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_qwen_math/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_postprune_standard_20_qwen_math_n200.json\"}, \"metrics\": {\"accuracy\": 0.185, \"n_correct\": 37, \"n_total\": 200, \"stderr\": 0.02746, \"eos_rate\": 0.69, \"avg_response_length\": 506.83, \"note\": \"Qwen-Math Standard 20% post-prune = 18.5%. Significantly better than CKA-only (1.0%) at post-prune stage.\"}}, \"eval_postprune_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_qwen_math/ --max_samples 200\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B (pruned_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"pruned_cka_only_20_qwen_math\", \"eval_data\": \"gsm8k test N=200\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_qwen_math/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_postprune_cka_only_20_qwen_math_n200.json\"}, \"metrics\": {\"accuracy\": 0.01, \"n_correct\": 2, \"n_total\": 200, \"stderr\": 0.00704, \"eos_rate\": 0.065, \"avg_response_length\": 958.3, \"note\": \"Qwen-Math CKA-only 20% post-prune = 1.0%. Severe collapse (repetition, gibberish).\"}}, \"eval_gsm8k_grpo_depth_first_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path grpo_depth_first_20/checkpoint-100 --output_path results/eval_gsm8k_grpo_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"pid\": \"51981\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_depth_first_20/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Conclusive: depth-first 20% GRPO dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy_approx\": 0.08, \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~8%@50 (GRPO). Prior log recovery showed ~24.18% from nohup output. No JSON result file produced.\", \"early_stopped\": true, \"result_file_on_westb\": false}}, \"eval_gsm8k_sft_depth_first_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path sft_depth_first_20 --output_path results/eval_gsm8k_sft_depth_first_20.json --seed 42 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"pid\": \"54882\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_depth_first_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_depth_first_20\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_depth_first_20.log\", \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). Conclusive: depth-first 20% SFT dramatically worse than CKA-only 64%. MF5 claim validated — CKA-only advantage is NOT simply removing deep layers.\", \"checkpoint_path\": \"N/A (eval only)\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy_approx\": 0.1, \"note\": \"Early-stopped by Director at ~60-88 samples. Interim accuracy ~10%@50 (SFT). No JSON result file produced.\", \"early_stopped\": true, \"result_file_on_westb\": false}}, \"eval_gsm8k_grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_random_20_seed123_v2.json --seed 123 --dtype bfloat16\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"56283\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed123_v2)\", \"seed\": 123, \"checkpoint_source\": \"grpo_random_20_seed123_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed123_v2.json\", \"accuracy\": 0.5072, \"total_correct\": 669, \"total_samples\": 1319, \"eos_rate\": 0.9939, \"stderr\": 0.01377, \"avg_response_length\": 177.9, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2/checkpoint-100\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.5072, \"n_correct\": 669, \"n_total\": 1319, \"stderr\": 0.01377, \"eos_rate\": 0.9939, \"avg_response_length\": 177.9}}, \"eval_math500_grpo_random_20_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json\", \"data_count\": 500, \"model_name\": \"grpo_random_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_random_20_v2.json\", \"log_path\": \"/tmp/eval_math500_grpo_random_20_v3.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.134, \"correct\": 67, \"total\": 500, \"stderr\": 0.0152, \"natural_eos\": 167, \"truncated\": 333, \"avg_response_length\": 1479.2}}, \"eval_math500_sft_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_qwen_math_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HuggingFaceH4/MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_final\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"pid\": 250766, \"log_path\": \"/tmp/eval_math500_sft_qwen_cka_only_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.216, \"stderr\": 0.0184, \"correct\": 108, \"total\": 500, \"natural_eos\": 90, \"truncated\": 410, \"avg_response_length\": 1745.338}}, \"eval_math500_grpo_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha0p5_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westb-23072\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha0p5_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.248, \"stderr\": 0.0193, \"correct\": 124, \"total\": 500, \"natural_eos\": 274, \"truncated\": 226, \"avg_response_length\": 1110.462}}, \"eval_math500_grpo_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_cka_only_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048'\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_cka_only_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"westb-23072:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.274, \"correct\": 137, \"total\": 500, \"stderr\": 0.01995, \"natural_eos\": 390, \"truncated\": 110, \"avg_response_length\": 654.746}}, \"eval_math500_grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha3p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"MATH-500\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.228, \"correct\": 114, \"total\": 500, \"stderr\": 0.0188, \"truncated_ratio\": 0.28, \"avg_response_length\": 745.038}}, \"eval_math500_grpo_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_grpo_rasp_alpha4p0_20.log\"}, \"metrics\": {\"accuracy\": 0.262, \"stderr\": 0.01966, \"correct\": 131, \"total\": 500, \"truncated\": 180, \"natural_eos\": 320, \"avg_response_length\": 925.48}, \"conclusion\": \"success\"}, \"eval_math500_grpo_rasp_alpha1p0_20\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha1p0_20.log\"}, \"metrics\": {\"accuracy\": 0.226, \"stderr\": 0.0187, \"n_correct\": 113, \"n_total\": 500, \"avg_response_length\": 903.536, \"natural_eos\": 320, \"truncated\": 180}, \"conclusion\": \"success\"}, \"eval_math500_sft_cka_only_20_westd\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path results/eval_math500_sft_cka_only_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"75284\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_cka_only_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\"}, \"metrics\": {\"accuracy\": 0.268, \"correct\": 134, \"total\": 500, \"truncated\": 116, \"stderr\": 0.0198, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"note\": \"PID 75284 actual output = 26.8% (134/500). Previous 29.0% (145/500) was from v4 run (May 19) with different answer extraction. Same model generations, different scoring.\"}, \"conclusion\": \"success\"}, \"eval_math500_grpo_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_grpo_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"pid\": \"83709\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_rasp_alpha2p0_20.log\", \"submitted_at\": \"2026-05-22T22:25:27.490Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"wall_clock_seconds\": 17473.0, \"gpu_hours\": 4.85}, \"metrics\": {\"accuracy\": 0.262, \"correct\": 131, \"total\": 500, \"stderr\": 0.0197, \"natural_eos\": 349, \"truncated\": 151, \"avg_response_length\": 785.326}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20 --max_samples 500 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.json'\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"220343\", \"data_path\": \"GSM8K test split\", \"data_count\": 500, \"model_name\": \"Qwen2.5-Math-7B-pruned-cka_only-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"grpo_qwen_math_cka_only_20\", \"eval_data\": \"GSM8K\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3.log\"}, \"metrics\": {\"accuracy\": 0.486, \"correct\": 243, \"total\": 500, \"stderr\": 0.0224, \"truncated_pct\": 0.838, \"natural_eos_pct\": 0.162, \"avg_response_length\": 1766.5}, \"conclusion\": \"success\"}, \"eval_math500_sft_rasp_alpha1p0_20_v2\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp_alpha1p0_20_v2.log\"}, \"metrics\": {\"accuracy\": 0.212, \"correct\": 106, \"total\": 500, \"truncated\": 186, \"stderr\": 0.0183}, \"conclusion\": \"success\"}, \"eval_math500_sft_standard_20_2048_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_2048_v2.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\\\"\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"pid\": \"82301\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_sft_standard_20_2048_v2.log\", \"submitted_at\": \"2026-05-22T22:15:58.026Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"metrics\": {\"accuracy\": 0.258, \"n_correct\": 129, \"n_total\": 500}, \"conclusion\": \"success\"}, \"eval_math500_sft_rasp_alpha0p5_20\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha0p5_20.log\"}, \"metrics\": {\"accuracy\": 0.254, \"correct\": 127, \"total\": 500, \"truncated\": 220, \"stderr\": 0.0195}, \"conclusion\": \"success\"}, \"eval_math500_sft_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha3p0_20.log\"}, \"metrics\": {\"accuracy\": 0.232, \"correct\": 116, \"total\": 500, \"truncated\": 144, \"stderr\": 0.0189}, \"conclusion\": \"success\"}, \"eval_math500_sft_rasp_alpha4p0_20\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_math500_sft_rasp_alpha4p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.266, \"correct\": 133, \"total\": 500, \"truncated\": 190, \"stderr\": 0.0198}}, \"eval_math500_sft_rasp_alpha2p0_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20 --output_path results/eval_math500_sft_rasp_alpha2p0_20.json --seed 42 --dtype bfloat16 --max_new_tokens 2048\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"57202\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha2p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"MATH-500 (N=500, max_new_tokens=2048)\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_math500_sft_rasp_alpha2p0_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.24, \"correct\": 120, \"total\": 500, \"truncated\": 155, \"stderr\": 0.0191}}, \"eval_gsm8k_grpo_random_20_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100 --seed 456 --dtype bfloat16 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"224705\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_random_20_seed456)\", \"seed\": 456, \"checkpoint_source\": \"grpo_random_20_seed456/checkpoint-100\", \"eval_data\": \"GSM8K test 1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_random_20_seed456.log\", \"accuracy\": 0.5087, \"total_correct\": 671, \"total_samples\": 1319, \"eos_rate\": 0.9955, \"stderr\": 0.01377, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"gsm8k_accuracy_se\": 0.0138, \"gsm8k_correct\": 671, \"gsm8k_total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 163.5, \"truncated\": 6}}, \"grpo_random_20_seed456\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"pid\": \"209508\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 456, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed456/checkpoint-100\", \"log_path\": \"/tmp/grpo_random_seed456.log\", \"note\": \"100/100 steps completed. Final trainer.save_model() hit disk-full but TRL checkpoint-100 is intact (model.safetensors=12,174,631,264 bytes, matching seed42/seed123_v2). Reviewer independently verified.\"}, \"conclusion\": \"success\"}, \"grpo_random_20_seed123_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123_v2 --max_steps 100 --save_steps 100 --seed 123\", \"server\": \"westd-32935\", \"gpu\": \"cuda:1\", \"pid\": \"53822\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training\", \"log_path\": \"/tmp/grpo_random_seed123_v2.log\"}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_alpha3p0_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2/checkpoint-100 --output_path results/eval_gsm8k_grpo_rasp_alpha3p0_20.json --max_samples 1319 --seed 42 --dtype bfloat16\", \"pid\": \"43755\", \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (grpo_rasp_alpha3p0_20_v2)\", \"seed\": 42, \"checkpoint_source\": \"grpo_rasp_alpha3p0_20_v2/checkpoint-100\", \"eval_data\": \"gsm8k test 1319\", \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_alpha3p0_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6345, \"correct\": 837, \"total\": 1319, \"stderr\": 0.0133, \"eos_rate\": 0.9864, \"truncated\": 18, \"avg_response_length\": 219.7}}, \"eval_math500_sft_random_20_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_random_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:1\"], \"pid\": \"5236\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_random_20_v3.log\", \"checkpoint_path\": \"N/A - eval\"}, \"metrics\": {\"accuracy\": 0.144, \"correct\": 72, \"total\": 500, \"stderr\": 0.0157, \"natural_eos\": 171, \"truncated\": 329, \"avg_response_length\": 1470.44}, \"conclusion\": \"success\"}, \"eval_gsm8k_sft_alpha3p0_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935 (SCP from westb)\", \"eval_data\": \"gsm8k test 1319\", \"pid\": \"37024\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6414, \"gsm8k_correct\": 846, \"gsm8k_total\": 1319, \"gsm8k_stderr\": 0.0132, \"eos_rate\": 0.9879, \"avg_response_length\": 188.63, \"natural_eos\": 1303, \"truncated\": 16}}, \"grpo_rasp_alpha3p0_20_v2\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:0\", \"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha3p0_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2 --max_steps 100 --save_total_limit 1\", \"pid\": \"42003\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_rasp_alpha3p0_20)\", \"seed\": 42, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20_v2\", \"log_path\": \"/tmp/grpo_alpha3p0_v2.log\"}, \"conclusion\": \"success\"}, \"eval_math500_grpo_standard_20_fair_2048_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_grpo_standard_20_fair_2048_v2.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"grpo_stage2_standard_20_fair\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_grpo_standard_20_fair_2048_v2.log\", \"checkpoint_path\": \"N/A (eval)\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.264, \"math500_correct\": 132, \"math500_total\": 500, \"math500_stderr\": 0.0197}}, \"grpo_random_20_seed123\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123 --num_steps 100 --seed 123'\", \"pid\": \"36832\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (sft_random_20)\", \"seed\": 123, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"N/A - GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20_seed123\", \"log_path\": \"/tmp/mf2_random_seed123_grpo.log\"}, \"conclusion\": \"success\"}, \"grpo_rasp_alpha3p0_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"command\": \"train_grpo_v5.py --model_path sft_rasp_alpha3p0_20/checkpoint-935 --output_dir grpo_rasp_alpha3p0_20 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"pid\": \"170676\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_rasp_alpha3p0_20/checkpoint-935\", \"eval_data\": \"N/A - GRPO training\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha3p0_20/checkpoint-100\", \"log_path\": \"/tmp/alpha3p0_grpo.log\"}, \"conclusion\": \"success\"}, \"eval_gsm8k_sft_alpha2p0_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6497, \"gsm8k_correct\": 857, \"gsm8k_total\": 1319}}, \"eval_gsm8k_sft_alpha0p5_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path sft_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"sft_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_sft_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6073, \"gsm8k_correct\": 801, \"gsm8k_total\": 1319}}, \"grpo_qwen_math_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"command\": \"train_grpo_v5.py --model_path sft_qwen_math_cka_only_20_v2 --max_steps 100 --learning_rate 1e-6 --per_device_train_batch_size 1 --gradient_accumulation_steps 8 --max_completion_length 512 --temperature 0.4 --beta 0.01 --loss_type dapo --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_8bit\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"pid\": \"164710\", \"data_path\": \"openai/gsm8k (train split)\", \"data_count\": 7473, \"checkpoint_source\": \"sft_qwen_math_cka_only_20_v2\", \"eval_data\": \"N/A - this is GRPO training, not eval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_qwen_math_cka_only_20\", \"log_path\": \"/tmp/mf3_qwen_grpo.log\"}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_alpha2p0_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:2\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha2p0_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha2p0_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha2p0_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha2p0_20.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"gsm8k_correct\": 872, \"gsm8k_total\": 1319}}, \"eval_gsm8k_grpo_alpha0p5_20\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-32935\", \"gpu\": \"cuda:3\", \"command\": \"eval_gsm8k.py --model_path grpo_rasp_alpha0p5_20 --max_new_tokens 2048\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"data_path\": \"openai/gsm8k (test split)\", \"data_count\": 1319, \"checkpoint_source\": \"grpo_rasp_alpha0p5_20\", \"eval_data\": \"gsm8k test 1319\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_alpha0p5_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_gsm8k_grpo_alpha0p5_20.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6118, \"gsm8k_correct\": 807, \"gsm8k_total\": 1319}}, \"eval_math500_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_math500_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_20_1p5b\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_math500_sft_standard_20_1p5b.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.054, \"correct\": 27, \"total\": 500, \"truncated\": 335}}, \"eval_gsm8k_sft_alpha4_20_v5\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_alpha4_20\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_sft_alpha4_20_v5.log\", \"result_path\": \"/root/recovery_aware_struct_prune/results/eval_gsm8k_sft_alpha4_20_v5.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6194, \"correct\": 817, \"total\": 1319, \"stderr\": 0.0134, \"eos_rate\": 0.981, \"avg_response_length\": 197.85}}, \"eval_gsm8k_grpo_alpha4_20_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100 --max_new_tokens 2048 --output_path /root/recovery_aware_struct_prune/results/eval_gsm8k_grpo_alpha4_20_v3.json\", \"server\": \"westd-32935\", \"gpu\": [\"cuda:3\"], \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_alpha4_20/checkpoint-100\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_alpha4_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"grpo_alpha4_20/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/recovery_aware_struct_prune/logs/eval_gsm8k_grpo_alpha4_20_v3.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6277, \"gsm8k_accuracy_ci\": 0.0133, \"gsm8k_correct\": 828, \"gsm8k_total\": 1319, \"eos_rate\": 0.9856, \"avg_response_length\": 188.16, \"natural_eos\": 1300, \"truncated\": 19}}, \"eval_math500_sft_standard_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/results.json --max_new_tokens 2048 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"104592\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"sft_standard_25/checkpoint-1870\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard_25/run.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.14, \"correct\": 70, \"n_total\": 500, \"natural_eos\": 185, \"truncated\": 315, \"avg_response_length\": 1367.82, \"v1_accuracy\": 0.13, \"v1_correct\": 65}}, \"grpo_alpha4_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --alpha 4.0 --max_steps 100\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"406593\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_alpha4_20.log\", \"submitted_at\": \"2026-05-21T18:59:44.258Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-7B\", \"seed\": 42, \"data_path\": \"gsm8k\", \"data_count\": 7473, \"checkpoint_source\": \"sft_alpha4_20_v2\", \"eval_data\": \"gsm8k\", \"wall_clock_seconds\": 1659.0, \"gpu_hours\": 0.46}, \"metrics\": {\"final_reward\": 0.198, \"reward_range\": \"0.146-0.256\", \"steps\": 100, \"final_loss\": 0.018, \"final_kl\": 0.00198}, \"conclusion\": \"success\"}, \"eval_math500_grpo_cka_only_25_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=0 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 379999, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% GRPO\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_grpo_cka_only_25_v2/eval_math500_grpo_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.184, \"math500_stderr\": 0.0173, \"correct\": 92, \"n_total\": 500}}, \"eval_math500_sft_cka_only_25_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && CUDA_VISIBLE_DEVICES=2 python /root/recovery_aware_struct_prune/src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_path /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2 --seed 42 --max_new_tokens 2048' > /root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log 2>&1 &\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 380074, \"data_path\": \"MATH-500\", \"data_count\": 500, \"model_name\": \"Qwen2.5-7B CKA-only 25% SFT\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"MATH-500\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_cka_only_25_v2/eval_math500_sft_cka_only_25_v2.log\"}, \"conclusion\": \"success\", \"metrics\": {\"math500_accuracy\": 0.192, \"correct\": 96, \"n_total\": 500, \"std_err\": 0.0176}}, \"eval_gsm8k_sft_standard_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 335301, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_standard_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"seed\": 42, \"checkpoint_source\": \"sft_standard_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_25.log\", \"checkpoint_path\": \"N/A (eval only)\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5087, \"stderr\": 0.0138, \"correct\": 671, \"n_total\": 1319, \"eos_rate\": 0.953, \"avg_response_length\": 333.15}, \"conclusion\": \"success\"}, \"eval_math500_grpo_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"max_new_tokens_actual\": 4096, \"note\": \"未显式指定 --max_new_tokens，脚本默认 4096。与 @2048 evals 不可直接比较。需用 eval_math500_grpo_cka_only_20_2048 重跑公平对比。\"}, \"metrics\": {\"accuracy\": 0.266, \"n_correct\": 133, \"n_total\": 500, \"stderr\": 0.0198, \"truncated\": 108, \"truncation_rate\": 0.216, \"avg_response_length\": 1124.24}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_standard_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": 75282, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-GRPO-v5fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb/checkpoint-100\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5186, \"stderr\": 0.0138, \"correct\": 684, \"n_total\": 1319, \"eos_rate\": 0.9575, \"avg_response_length\": 314.47}}, \"eval_gsm8k_sft_cka_only_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 329698, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_25\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_25\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_25.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6012, \"correct\": 793, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": 0.9803, \"avg_response_length\": 243.6}}, \"eval_gsm8k_sft_random_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"nohup bash -c 'source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --max_samples 1319 --seed 42'\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 329770, \"data_path\": \"GSM8K (N=1319)\", \"data_count\": 1319, \"model_name\": \"sft_random_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"seed\": 42, \"checkpoint_source\": \"sft_random_20\", \"eval_data\": \"GSM8K\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_sft_random_20.log\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5125, \"correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138, \"eos_rate\": 0.9932, \"avg_response_length\": 182.4}}, \"eval_gsm8k_grpo_cka_only_25_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"322443\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_25_v3.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5959, \"correct\": 786, \"n_total\": 1319, \"eos_rate\": 0.9818}}, \"grpo_standard_25_westb\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_westb --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"64194\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"reward\": 0.00813, \"steps\": 100, \"collapse_pattern\": \"near_total_collapse\"}}, \"eval_gsm8k_grpo_random_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"322611\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_random_20_v2.log\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct-GRPO\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100\", \"eval_data\": \"GSM8K\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.5057, \"gsm8k_stderr\": 0.0138, \"correct\": 667, \"total\": 1319, \"eos_rate\": 0.9954, \"avg_response_length\": 173}}, \"sft_random_20\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-random-20pct\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20\", \"data_path\": \"gsm8k\", \"seed\": 42}, \"metrics\": {\"steps\": 1870, \"model_size_gb\": 12}}, \"grpo_random_20\": {\"spec\": {\"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_random_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20 --max_steps 100 --save_steps 100 --seed 42\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"317332\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_random_20.log\", \"submitted_at\": \"2026-05-21T03:46:03.569Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\"}, \"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"reward_mean\": 0.164, \"reward_range\": [0.14, 0.19], \"reward_peak\": 0.19, \"reward_peak_step\": 70, \"frac_zero_std_mean\": 0.333, \"frac_zero_std_range\": [0.3, 0.4], \"entropy_mean\": 0.221, \"entropy_range\": [0.2, 0.24], \"kl_mean\": 0.0045, \"steps_captured\": 9, \"max_step\": 90, \"pattern\": \"stable plateau, no collapse\", \"data_source\": \"log_file (W&B crashed before sync)\"}}, \"grpo_cka_only_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 HF_DATASETS_OFFLINE=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_25 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"310542\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct-SFT\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"reward\": 0.2875, \"steps\": 100}}, \"eval_humaneval_sft_standard_25\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"server\": \"westb-23072\", \"data_path\": \"openai/openai_humaneval\", \"data_count\": 164, \"model_name\": \"Qwen2.5-Coder-3B-pruned-standard-25-sft\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"eval_data\": \"HumanEval\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.0183, \"stderr\": 0.0105, \"n_passed\": 3, \"n_total\": 164}}, \"sft_cka_only_25\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.6508, \"mean_token_accuracy\": 0.8285, \"training_time_s\": 1644}, \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"307651\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_25.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-25pct\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25\"}}, \"prune_cka_only_25\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode cka_only --sparsity 0.25 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25 --seed 42 --dtype bfloat16\", \"server\": \"westd-29022\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42}, \"metrics\": {\"actual_sparsity\": 0.2367, \"mlp_groups_pruned\": 248, \"mlp_groups_total\": 784, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"param_count_B\": 5.81, \"original_param_count_B\": 7.62}}, \"eval_gsm8k_grpo_standard_15_seed123_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed123_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed123_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6513, \"accuracy_se\": 0.0131, \"n_correct\": 859, \"n_total\": 1319, \"eos_rate\": 0.9932, \"avg_response_length\": 183.25}}, \"eval_gsm8k_grpo_standard_15_seed456_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_seed456_v3/checkpoint-100 --max_samples 1319 --seed 42\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_standard_15_seed456_v3\", \"eval_data\": \"gsm8k_test_n1319\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6543, \"gsm8k_stderr\": 0.0131, \"n_correct\": 863, \"n_total\": 1319, \"eos_rate\": 0.9939, \"avg_response_length\": 180.23}}, \"eval_gsm8k_grpo_cka_only_15_seed123\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 73.09, \"n_correct\": 964, \"n_total\": 1319, \"stderr\": 1.22, \"eos_rate\": 98.79, \"truncated\": 16}, \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed123/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed123_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed123\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed123\", \"eval_data\": \"gsm8k_test_n1319\"}}, \"eval_gsm8k_grpo_cka_only_15_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_seed456/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_seed456_n1319.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct-grpo-seed456\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_15_seed456\", \"eval_data\": \"gsm8k_test_n1319\"}, \"metrics\": {\"accuracy\": 0.721, \"n_correct\": 951, \"n_total\": 1319, \"stderr\": 0.0123, \"eos_rate\": 0.9894, \"avg_response_length\": 201.94}, \"conclusion\": \"success\"}, \"grpo_standard_15_seed456_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed456_v3 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"287862\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed456_v3.log\", \"submitted_at\": \"2026-05-20T21:58:13.750Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 456}, \"conclusion\": \"success\"}, \"grpo_standard_15_seed123_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir grpo_standard_15_seed123_v3 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"287784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_seed123_v3.log\", \"submitted_at\": \"2026-05-20T21:58:10.978Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-standard-15pct\", \"seed\": 123}, \"conclusion\": \"success\"}, \"grpo_cka_only_15_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed456 --max_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"281727\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed456.log\", \"submitted_at\": \"2026-05-20T20:54:56.719Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 456, \"wall_clock_seconds\": 2420.0, \"gpu_hours\": 0.67}, \"conclusion\": \"success\"}, \"grpo_cka_only_15_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/train_grpo_v5.py --model_path sft_cka_only_15 --output_dir grpo_cka_only_15_seed123 --max_steps 100 --seed 123\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"281647\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_15_seed123.log\", \"submitted_at\": \"2026-05-20T20:54:54.017Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-pruned-cka_only-15pct\", \"seed\": 123, \"wall_clock_seconds\": 2420.5, \"gpu_hours\": 0.67}, \"conclusion\": \"success\"}, \"eval_gsm8k_sft_standard_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 266847, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_20 (Qwen2.5-7B, 20% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_n1319.json\"}, \"metrics\": {\"gsm8k_accuracy\": 0.5921, \"stderr\": 0.0135, \"correct\": 781, \"total\": 1319, \"eos_rate\": 0.9848, \"avg_response_length\": 206.68}, \"conclusion\": \"success\"}, \"eval_gsm8k_dense_unpruned\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": 32154, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense, unpruned)\", \"seed\": 42, \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_dense_unpruned.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_dense_unpruned_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.9083, \"gsm8k_accuracy_ci\": 0.0079, \"correct\": 1198, \"total\": 1319, \"eos_rate\": 0.9871, \"avg_response_length\": 594, \"truncated\": 17, \"eval_time\": \"3h7m\"}}, \"eval_gsm8k_sft_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 264522, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_20 (Qwen2.5-7B, 20% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6391, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 843, \"total\": 1319, \"eos_rate\": 0.9901, \"avg_response_length\": 198.1, \"truncated\": 13}}, \"eval_gsm8k_sft_cka_only_15\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 262728, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_cka_only_15 (Qwen2.5-7B, 15% CKA-only sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_cka_only_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_15_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7218, \"correct\": 952, \"total\": 1319}}, \"eval_gsm8k_sft_rasp_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 267009, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_rasp_20_westd (Qwen2.5-7B, 20% RASP sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_rasp_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6149, \"gsm8k_accuracy_ci\": 0.0134, \"correct\": 811, \"total\": 1319, \"eos_rate\": 0.9826, \"avg_response_length\": 216.5}}, \"eval_gsm8k_grpo_standard_15_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 256586, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"grpo_standard_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_15_v2_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6611, \"correct\": 872, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 184}}, \"eval_gsm8k_sft_standard_15\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 nohup python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 256743, \"data_path\": \"gsm8k/test\", \"data_count\": 1319, \"model_name\": \"sft_standard_15 (Qwen2.5-7B, 15% standard sparsity, SFT only)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_15.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_15_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6649, \"correct\": 877, \"total\": 1319, \"eos_rate\": 0.993, \"avg_response_length\": 183}}, \"eval_gsm8k_grpo_cka_only_15_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 252919, \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_15_v2\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_15_v2_n1319.json\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.7309, \"gsm8k_accuracy_ci\": 0.0122, \"correct\": 964, \"total\": 1319, \"eos_rate\": 0.9894, \"avg_response_length\": 202.4}}, \"eval_gsm8k_grpo_cka_only_20_seed456_full\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 252604, \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\", \"eval_data\": \"gsm8k_n1319\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_seed456_full.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.6459, \"gsm8k_accuracy_ci\": 0.0132, \"correct\": 852, \"total\": 1319, \"eos_rate\": 0.9886, \"avg_response_length\": 204.3}}, \"eval_gsm8k_sft_qwen_standard_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_standard_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"18114\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_standard_20.log\", \"submitted_at\": \"2026-05-20T11:32:15Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_qwen_math/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 15018.0, \"gpu_hours\": 4.17}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.21, \"correct\": 42, \"total\": 200}}, \"eval_gsm8k_sft_qwen_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --max_samples 200 --seed 42 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_qwen_cka_only_20.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"18038\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_qwen_cka_only_20.log\", \"submitted_at\": \"2026-05-20T11:32:13Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"gsm8k/test\", \"data_count\": 200, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-20%-SFT-ep1\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"gsm8k-test-N200\", \"wall_clock_seconds\": 14658.4, \"gpu_hours\": 4.07}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 0.515, \"gsm8k_accuracy_ci\": 0.0353, \"correct\": 103, \"total\": 200, \"eos_rate\": 0.27, \"avg_response_length\": 1536, \"truncated\": 146, \"eval_time\": \"4h00m04s\"}}, \"grpo_standard_15_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline nohup python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"pid\": 253918, \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"sft_standard_15 (pruned Qwen2.5-7B, 15% standard sparsity)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_15\", \"eval_data\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_15_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_15_v2\"}, \"conclusion\": \"success\", \"metrics\": {\"loss\": 0.01142, \"reward\": 0.1375, \"reward_std\": 0.2778, \"kl\": 0.004099, \"entropy\": 0.1932, \"grad_norm\": 3.547, \"total_steps\": 100, \"training_time\": \"21m49s\"}}, \"eval_gsm8k_grpo_standard_20_seed123_full\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed123_n1319.json\"}, \"metrics\": {\"accuracy\": 0.5989, \"n_correct\": 790, \"n_total\": 1319, \"stderr\": 0.0135, \"eos_rate\": null}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_standard_20_seed456_full\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=1319)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_seed456_n1319.json\"}, \"metrics\": {\"accuracy\": 0.602, \"n_correct\": 794, \"n_total\": 1319, \"stderr\": 0.01348, \"eos_rate\": 0.9856}, \"conclusion\": \"success\"}, \"grpo_cka_only_15_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2 --max_steps 100 --save_steps 100 --seed 42\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 250149, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_15_v2.log\", \"model_name\": \"sft_cka_only_15\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_15\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_15_v2\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.2027, \"avg_train_loss\": 0.11, \"final_reward\": 0.4019, \"final_kl\": 0.0018, \"train_steps\": 100, \"train_runtime_min\": 22.5}}, \"grpo_cka_only_20_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456 --max_steps 100 --save_steps 100 --seed 456\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 249963, \"log_path\": \"/root/runs/recovery_aware_struct_prune/grpo_cka_only_20_seed456.log\", \"model_name\": \"sft_cka_only_20\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"gsm8k train (GRPO training, not eval)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed456\"}, \"conclusion\": \"success\", \"metrics\": {\"final_loss\": 0.0999, \"avg_train_loss\": 0.0881, \"final_reward\": 0.2925, \"final_kl\": 0.0017, \"train_steps\": 100, \"train_runtime_min\": 21.8}}, \"prune_eval_standard_30\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/prune.py --mode standard --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"pid\": 190349, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_standard_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 2.8, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 1.2, \"avg_len\": 4057}}, \"prune_eval_cka_only_30\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/prune.py --mode cka_only --sparsity 0.30 + python src/eval_gsm8k.py\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 190269, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/prune_eval_cka_only_30.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"data_path\": \"gsm8k test\", \"data_count\": 1319, \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 1.6, \"note\": \"N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\", \"n_evaluated\": 500, \"n_total\": 1319, \"eos_rate\": 5.6, \"avg_len\": 4009}}, \"sft_qwen_math_cka_only_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_final --gpu 0 --num_train_epochs 1 --save_strategy no\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"9952\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-20T09:18:16.420Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 7473, \"model_name\": \"Qwen2.5-Math-7B-CKA-only-Pruned-20%\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_cka_only_20/checkpoint-935\", \"eval_data\": \"GSM8K train (7473 samples, SFT epoch 2)\", \"wall_clock_seconds\": 1918.9, \"gpu_hours\": 0.53}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.3481, \"mean_token_accuracy\": 0.8595, \"train_runtime_sec\": 1013, \"train_samples_per_second\": 7.38, \"epochs\": 1}}, \"eval_gsm8k_grpo_standard_20_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed456 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"221008\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T09:15:19.738Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed456\", \"seed\": 456, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed456_n200.json\", \"wall_clock_seconds\": 2030.9, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.665, \"n_correct\": 133, \"n_total\": 200, \"stderr\": 0.0334, \"eos_rate\": 0.995, \"avg_response_length\": 166.9}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_standard_20_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"eval_gsm8k.py --model_path grpo_standard_20_seed123 --max_samples 200\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"221158\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T09:15:26.368Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 200, \"model_name\": \"grpo_standard_20_seed123\", \"seed\": 123, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"eval_data\": \"GSM8K test (N=200)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_standard_20_seed123_n200.json\", \"wall_clock_seconds\": 2022.3, \"gpu_hours\": 0.56}, \"metrics\": {\"accuracy\": 0.64, \"n_correct\": 128, \"n_total\": 200, \"stderr\": 0.0339, \"eos_rate\": 0.99, \"avg_response_length\": 187.9}, \"conclusion\": \"success\"}, \"grpo_standard_20_seed456\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456 --max_steps 100 --save_steps 100 --gpu 0 --seed 456\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"211798\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed456.log\", \"submitted_at\": \"2026-05-20T06:22:19.535Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"seed\": 456, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed456\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"wall_clock_seconds\": 10289.1, \"gpu_hours\": 2.86}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2745, \"peak_reward\": 0.0844, \"peak_reward_step\": 90, \"final_reward\": 0.06, \"final_frac_zero_std\": 0.65, \"seed\": 456, \"wandb_run\": \"wg0iv4oi\", \"wandb_mode\": \"offline\"}, \"conclusion\": \"success\"}, \"grpo_standard_20_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 WANDB_MODE=offline python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123 --max_steps 100 --max_completion_length 1024 --save_steps 100 --gpu 0 --run_name grpo_standard_20_seed123 --seed 123\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"211972\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_seed123.log\", \"submitted_at\": \"2026-05-20T06:22:37.312Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B-Standard-20%-SFT\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_seed123\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"GSM8K train (7473 samples, GRPO RLVR training)\", \"tmux_session\": \"grpo_standard_20_seed123\", \"wall_clock_seconds\": 10268.1, \"gpu_hours\": 2.85}, \"metrics\": {\"steps_completed\": 100, \"runtime_sec\": 2783, \"peak_reward\": 0.0619, \"peak_reward_step\": 80, \"final_reward\": 0.0594, \"final_frac_zero_std\": 0.6, \"seed\": 123, \"wandb_run\": \"pgzwv725\", \"wandb_mode\": \"offline\"}, \"conclusion\": \"success\"}, \"eval_mbpp_grpo_standard_20_v3\": {\"status\": \"DONE\", \"conclusion\": \"success\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_path\": \"N/A\", \"log_path\": \"/root/autodl-tmp/logs/eval_mbpp_grpo_standard_20_v3.log\"}, \"metrics\": {\"pass_at_1\": 0.131, \"correct\": 49, \"total\": 374, \"stderr\": 0.0174}}, \"eval_humaneval_sft_standard_20_1p5b_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_1p5b_2048.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"890564\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T12:23:31.889Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20_1p5b\", \"seed\": 42, \"wall_clock_seconds\": 5434.5, \"gpu_hours\": 1.51}, \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}, \"conclusion\": \"success\"}, \"eval_humaneval_sft_standard_20_2048_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"86171\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048_v3.log\", \"result_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_standard_20_2048_v3.json\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1341, \"correct\": 22, \"total\": 164, \"stderr\": 0.0266}}, \"eval_humaneval_sft_cka_only_20_1p5b_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/sft_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"95940\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:45:57.991Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"metrics\": {\"pass_at_1\": 0.0061, \"n_correct\": 1, \"n_total\": 164, \"avg_response_length\": 1968.76, \"median_response_length\": 2048}, \"wall_clock_seconds\": 6208.0, \"gpu_hours\": 1.72}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.0061, \"correct\": 1, \"total\": 164, \"stderr\": 0.0061}}, \"eval_humaneval_grpo_cka_only_20_1p5b_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/models/grpo_cka_only_20_1p5b --max_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"96018\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_1p5b_2048.log\", \"submitted_at\": \"2026-05-19T11:46:00.256Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20_1p5b\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b\", \"wall_clock_seconds\": 7116.7, \"gpu_hours\": 1.98}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0, \"correct\": 0, \"total\": 164, \"stderr\": 0}}, \"eval_mbpp_sft_shortgpt_20_v2\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-SFT\", \"seed\": 42, \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"account\": \"root\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\\\"\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_shortgpt_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1043, \"stderr\": 0.0158, \"n_correct\": 39, \"n_total\": 374, \"avg_response_length\": 1166.4, \"median_response_length\": 773.5}, \"conclusion\": \"success\"}, \"eval_mbpp_grpo_shortgpt_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"account\": \"root\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-ShortGPT-20%-GRPO\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_grpo_shortgpt_20.json\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1444, \"stderr\": 0.0182, \"n_correct\": 54, \"n_total\": 374, \"avg_response_length\": 1140.8, \"median_response_length\": 804.5}}, \"eval_mbpp_sft_standard_20_v4\": {\"status\": \"DONE\", \"spec\": {\"command\": \"HF_DATASETS_OFFLINE=1 HF_HUB_OFFLINE=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_standard_20.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"sft_standard_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"tmux_session\": \"eval_mbpp_sft_standard_20_v4\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20.json\"}, \"metrics\": {\"pass_at_1\": 0.1203, \"stderr\": 0.0168, \"n_correct\": 45, \"n_total\": 374, \"avg_response_length\": 1084.1, \"median_response_length\": 746.5}, \"conclusion\": \"success\"}, \"eval_mbpp_grpo_standard_20_v4\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:2\", \"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_standard_20.json\", \"data_path\": \"mbpp\", \"data_count\": 374, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"mbpp_sanitized_374\"}, \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.01745, \"avg_response_length\": 1058.7, \"median_response_length\": 726}, \"conclusion\": \"success\"}, \"cka_scoring_stability_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/cka_stability_analysis.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json --device cuda:0\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 143187, \"data_path\": \"openai/gsm8k\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/cka_stability_results.json\"}, \"metrics\": {\"spearman_256v512_attn\": 0.989, \"spearman_256v512_mlp\": 0.9683, \"spearman_256v512_combined\": 0.9788, \"spearman_256v1024_attn\": 0.9762, \"spearman_256v1024_mlp\": 0.9464, \"spearman_256v1024_combined\": 0.9641, \"spearman_512v1024_attn\": 0.995, \"spearman_512v1024_mlp\": 0.9908, \"spearman_512v1024_combined\": 0.9938, \"min_combined_rho\": 0.964, \"mean_combined_rho\": 0.979, \"stable\": true}, \"conclusion\": \"success\"}, \"eval_mbpp_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_standard_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": \"0\", \"model_name\": \"sft_standard_20_1p5b\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"mbpp\", \"data_path\": \"mbpp\", \"data_count\": 0, \"seed\": 0}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.008021, \"n_correct\": 3, \"n_total\": 374, \"stderr\": 0.004613, \"avg_response_length\": 1658.6, \"median_response_length\": 2048}}, \"eval_mbpp_grpo_rasp_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"127964\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.131, \"n_correct\": 49, \"n_total\": 374, \"stderr\": 0.0174}}, \"eval_mbpp_sft_rasp_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_sft_rasp_20.json\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"133674\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_sft_rasp_20.log\", \"submitted_at\": \"2026-05-19T20:00:13.578Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 4067.0, \"gpu_hours\": 1.13}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1176, \"stderr\": 0.0167, \"n_correct\": 44, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 78.01, \"avg_response_length\": 810.7, \"median_response_length\": 247}}, \"eval_mbpp_sft_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/mbpp_sft_cka_only_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:3\", \"pid\": 123029, \"log_path\": \"/tmp/eval_mbpp_sft_cka_only_20.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"MBPP sanitized (374 tasks)\", \"data_path\": \"google-research-datasets/mbpp (sanitized)\", \"data_count\": 374, \"model_name\": \"Qwen2.5-7B-pruned-20%-SFT-CKA-only\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1283, \"stderr\": 0.0173, \"n_correct\": 48, \"n_total\": 374, \"dense_baseline_pass_at_1\": 0.5348, \"degradation_pct\": 76.01, \"avg_response_length\": 643.8, \"median_response_length\": 363.5}}, \"eval_humaneval_sft_rasp_20_1p5b_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"909411\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-rasp-20-SFT\", \"metrics\": {\"pass_at_1\": 0, \"stderr\": 0, \"n_passed\": 0, \"n_total\": 164}, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20_1p5b_2048.json\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_1p5b_2048.log\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0, \"n_correct\": 0, \"n_total\": 164, \"note\": \"1.5B SFT RASP, all truncated at 2048 tokens\"}}, \"eval_mbpp_grpo_cka_only_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_mbpp.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_grpo_cka_only_20.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"unknown\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_grpo_cka_only_20.log\", \"submitted_at\": \"2026-05-19T18:08:02.259Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"wall_clock_seconds\": 17.3, \"gpu_hours\": 0.0}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1417, \"n_correct\": 53, \"n_total\": 374, \"stderr\": 0.018}}, \"eval_gsm8k_grpo_shortgpt_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_shortgpt_20.json\", \"server\": \"westd-29022\", \"gpu\": \"cuda:0\", \"pid\": 122867, \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_shortgpt_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/tmp/eval_gsm8k_grpo_shortgpt_20.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_shortgpt_20/checkpoint-100\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 43.37, \"n_correct\": 572, \"n_total\": 1319, \"stderr\": 0.0136}}, \"eval_gsm8k_sft_shortgpt_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_sft_shortgpt_20.json\", \"server\": \"westd-29022\", \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-7B-ShortGPT-20pct-SFT\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20/\", \"eval_data\": \"gsm8k:test\"}, \"conclusion\": \"success\", \"metrics\": {\"gsm8k_accuracy\": 44.73, \"n_correct\": 590, \"n_total\": 1319}}, \"sft_shortgpt_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20 --gpu 3 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"112015\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_shortgpt_20.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"model_name\": \"shortgpt_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/shortgpt_20\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_shortgpt_20\"}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_cka_only_20_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20_seed123.json\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_seed123.log\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"eval_data\": \"gsm8k_test\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20_seed123\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\"}, \"metrics\": {\"accuracy\": 0.6422, \"stderr\": 0.0132, \"n_correct\": 847, \"n_total\": 1319, \"eos_rate\": 0.9909, \"avg_response_length\": 195.97, \"natural_eos\": 1307, \"truncated\": 12}, \"conclusion\": \"success\"}, \"eval_humaneval_grpo_standard_20_1p5b_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"eval_data\": \"HumanEval\", \"model_name\": \"Qwen2.5-1.5B-pruned-standard-20-GRPO\", \"tmux_session\": \"eval_humaneval_grpo_standard_1p5b\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_1p5b_2048.log\"}, \"conclusion\": \"success\"}, \"gradient_flow_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 pruned_rasp_20 --model_names CKA-only Standard RASP --n_steps 200 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3 --seed 42\", \"server\": \"westb-23072\", \"gpu\": \"cuda:0\", \"pid\": \"901553\", \"data_path\": \"openai/gsm8k train split\", \"data_count\": 200, \"model_name\": \"pruned_cka_only_20 + pruned_standard_20 + pruned_rasp_20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/gradient_flow_v3/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/gradient_flow_v3.log\"}, \"conclusion\": \"success\", \"metrics\": {\"cka_only_mean_grad_norm\": 0.3229, \"standard_mean_grad_norm\": 0.1118, \"rasp_mean_grad_norm\": 0.1431, \"cka_vs_standard_ratio\": 2.89, \"rasp_vs_standard_ratio\": 1.28, \"cka_vs_standard_significant_layers\": \"55/56\", \"cka_vs_rasp_significant_layers\": \"56/56\", \"rasp_vs_standard_significant_layers\": \"45/56\", \"rasp_vs_standard_nonsig_layers\": \"layer_18_mlp,layer_19_attn,layer_19_mlp,layer_20_attn,layer_20_mlp,layer_21_attn,layer_21_mlp,layer_22_attn,layer_24_mlp,layer_27_attn,layer_27_mlp\", \"n_samples\": 200, \"statistical_test\": \"Wilcoxon signed-rank, per-layer\", \"bootstrap_n\": 1000, \"seed\": 42}}, \"eval_gsm8k_grpo_rasp_20_fair\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.json\", \"server\": \"westd-29022\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"GSM8K\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_fair.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6088, \"stderr\": 0.0134, \"n_correct\": 803, \"n_total\": 1319, \"eos_rate\": 0.9879, \"avg_response_length\": 195.7}}, \"eval_mbpp_dense_unpruned\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 /root/miniconda3/bin/python src/eval_mbpp.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_mbpp_dense_unpruned.json'\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_mbpp_dense_unpruned.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"MBPP\", \"data_count\": 374, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MBPP (374 tasks, sanitized, pass@1, max_new_tokens=2048)\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"pid\": \"108291\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.5348, \"stderr\": 0.0258, \"n_correct\": 200, \"n_total\": 374}}, \"eval_humaneval_sft_rasp_20_2048_v2\": {\"status\": \"DONE\", \"spec\": {\"server\": \"westd-29022\", \"gpu\": \"cuda:1\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"HumanEval\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_rasp_20_2048_v2.json\", \"pid\": \"107932\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"n_correct\": 17, \"n_total\": 164, \"avg_response_length\": 1253.7, \"median_response_length\": 2048}}, \"grpo_cka_only_20_seed123\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/grpo_train.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123 --num_train_steps 100 --seed 123'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"857962\", \"data_path\": \"gsm8k\", \"data_count\": 7473, \"model_name\": \"pruned_cka_only_20\", \"seed\": 123, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_seed123\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/grpo_cka_only_20_seed123.log\"}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.1361, \"final_step_loss\": 0.05054, \"final_reward\": 0.2975, \"final_reward_std\": 0.4097, \"train_steps\": 100, \"train_runtime_hours\": 11.63, \"wandb_run\": \"j8kn0sqd\"}}, \"gradient_flow_analysis\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/gradient_flow_analysis.py --model_paths pruned_cka_only_20 pruned_standard_20 --model_names CKA-only Standard --n_steps 20 --seed 42\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (cached)\", \"data_count\": 20, \"model_name\": \"Qwen2-7B pruned variants\", \"seed\": 42, \"checkpoint_path\": \"N/A (analysis only)\", \"log_path\": \"/tmp/gradient_flow.log\"}, \"conclusion\": \"success\", \"metrics\": {\"cka_only_attn_grad_mean\": 0.3135, \"cka_only_attn_grad_cv\": 1.2231, \"cka_only_mlp_grad_mean\": 0.285, \"cka_only_mlp_grad_cv\": 1.2424, \"standard_attn_grad_mean\": 0.1316, \"standard_attn_grad_cv\": 1.1363, \"standard_mlp_grad_mean\": 0.1222, \"standard_mlp_grad_cv\": 1.1489, \"grad_magnitude_ratio_attn\": 2.38, \"grad_magnitude_ratio_mlp\": 2.33}}, \"cka_calibration_stability_ablation\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=0 python src/run_cka_reliability.py --original_model /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --pruned_model /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --num_samples 1024 --n_splits 5 --max_length 512 --output /root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json --seed 42\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"cka_reliability\", \"data_path\": \"GSM8K calibration subset\", \"data_count\": 1024, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + pruned_cka_only_20\", \"seed\": 42, \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/cka_reliability_ablation.log\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/cka_reliability_ablation.json\", \"backend\": \"tmux\", \"account\": \"root\"}, \"conclusion\": \"success\", \"metrics\": {\"split_half_rho\": 0.9932, \"n_splits\": 5, \"size_sensitivity_128\": 0.982, \"size_sensitivity_256\": 0.989, \"size_sensitivity_512\": 0.995}}, \"eval_humaneval_grpo_standard_20_fair_2048_v3\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_new_tokens 2048\", \"server\": \"westd-29022\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_standard_20_fair_2048_v3.log\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164}}, \"eval_humaneval_sft_cka_only_20_2048_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_sft_cka_only_20_2048_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"78740\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"eval_data\": \"HumanEval (164 problems, pass@1, max_new_tokens=2048, sys.executable fix)\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 20.12, \"n_correct\": 33, \"n_total\": 164}}, \"eval_math500_grpo_cka_only_20_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=2 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"36703\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-18T23:23:59.014Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"grpo_cka_only_20\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wall_clock_seconds\": 49459.6, \"gpu_hours\": 13.74}, \"metrics\": {\"accuracy\": 0.292, \"n_correct\": 146, \"n_total\": 500}, \"conclusion\": \"success\"}, \"eval_gsm8k_sft_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_standard_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"842784\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_sft_standard_20_1p5b.log\", \"submitted_at\": \"2026-05-18T23:02:19.301Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Qwen2.5-1.5B-sft-standard-20\", \"checkpoint_source\": \"sft_standard_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"wall_clock_seconds\": 50738.5, \"gpu_hours\": 14.09}, \"metrics\": {\"accuracy\": 0.22896133434420016, \"n_correct\": 302, \"n_total\": 1319}, \"conclusion\": \"success\"}, \"eval_gsm8k_grpo_standard_20_fair_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --max_samples 1319 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_fair_v2.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"83299\", \"data_path\": \"GSM8K\", \"data_count\": 1319, \"model_name\": \"grpo_stage2_standard_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"GSM8K (1319 samples)\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 59.44, \"n_correct\": 784, \"n_total\": 1319}}, \"eval_humaneval_grpo_rasp_20_fair_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.json\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/humaneval_grpo_rasp_20_fair_2048.log\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_stage2_rasp_20_fair\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"HumanEval\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\"}, \"conclusion\": \"success\", \"metrics\": {\"pass_at_1\": 0.1098, \"n_correct\": 18, \"n_total\": 164, \"stderr\": 0.0244, \"avg_response_length\": null}}, \"eval_gsm8k_grpo_unstructured_20\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_unstructured_20.json\", \"server\": \"westb-23072\", \"data_path\": \"gsm8k test set\", \"data_count\": 1319, \"model_name\": \"grpo_unstructured_20/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unstructured_20/checkpoint-100\", \"eval_data\": \"gsm8k_test\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.8764, \"n_correct\": 1156, \"n_total\": 1319, \"stderr\": 0.00906, \"eos_rate\": 0.9818, \"truncated\": 24, \"avg_response_length\": 600}}, \"eval_humaneval_grpo_cka_only_20_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:1\"], \"pid\": \"66521\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_cka_only_20_2048.log\", \"submitted_at\": \"2026-05-19T04:11:28.118Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"HumanEval\", \"data_count\": 164, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"eval_data\": \"HumanEval\", \"wall_clock_seconds\": 12309.1, \"gpu_hours\": 3.42}, \"metrics\": {\"pass_at_1\": 0.2012, \"n_correct\": 33, \"n_total\": 164, \"stderr\": 0.0313, \"avg_response_length\": 1523.31, \"median_response_length\": 2048, \"wall_clock_seconds\": 11933}, \"conclusion\": \"success\"}, \"grpo_standard_20_fair\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"export HF_HOME=/root/autodl-tmp/.hf_cache && source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_total_limit 3 --save_steps 10 --reward_desert_patience 200 --run_name grpo_standard_20_fair\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (GRPO training)\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_standard_20_fair.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"74224\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-18T01:05:44.210Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3631.9, \"gpu_hours\": 1.01}, \"status\": \"DONE\", \"metrics\": {\"wandb_run_id\": \"tyv20u2k\", \"total_steps\": 100, \"runtime_seconds\": 3017, \"reward_trajectory\": [0.051, 0.056, 0.067, 0.081, 0.019, 0.043, 0.047, 0.046, 0.031, 0.054], \"frac_zero_std_trajectory\": [0.5, 0.625, 0.5, 0.5, 0.575, 0.55, 0.575, 0.55, 0.55, 0.55], \"peak_reward\": 0.081, \"peak_reward_step\": 40, \"final_reward\": 0.054, \"final_frac_zero_std\": 0.55, \"dynamics_pattern\": \"dip_then_partial_recovery\", \"dip_step\": 50, \"dip_reward\": 0.019}, \"conclusion\": \"success\"}, \"inference_bench_clean_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/measure_inference_speed.py --models original:/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B pruned_cka_only_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 pruned_standard_20:/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench_clean_v2.json --n_prompts 50 --max_new_tokens 256'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"56892\", \"log_path\": \"~/runs/recovery_aware_struct_prune/inference_bench_clean_v2.log\", \"submitted_at\": \"2026-05-19T01:42:24.921Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"Dense + CKA-only 20% + Standard 20%\", \"data_path\": \"gsm8k test (50 prompts)\", \"data_count\": 50, \"seed\": 42, \"checkpoint_path\": \"N/A (benchmark)\", \"wall_clock_seconds\": 3702.3, \"gpu_hours\": 1.03}, \"conclusion\": \"success\", \"metrics\": {\"original_tps\": 72.02, \"cka_only_20_tps\": 58.28, \"standard_20_tps\": 58.25, \"cka_only_20_speedup\": 0.809, \"standard_20_speedup\": 0.809, \"original_first_token_ms\": 20.05, \"cka_only_20_first_token_ms\": 16.35, \"standard_20_first_token_ms\": 16.4, \"original_per_token_ms\": 13.89, \"cka_only_20_per_token_ms\": 16.73, \"standard_20_per_token_ms\": 16.71, \"original_params\": 7615616512, \"pruned_params\": 6161946112, \"param_reduction_pct\": 19.1}}, \"eval_gsm8k_sft_rasp_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"845212\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_rasp_20_1p5b.json\", \"submitted_at\": \"2026-05-18T23:43:58.904Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_1p5b\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"gsm8k\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"wall_clock_seconds\": 10779.5, \"gpu_hours\": 2.99}, \"metrics\": {\"accuracy\": 0.2691, \"n_correct\": 355, \"n_total\": 1319, \"stderr\": 0.0122, \"grpo_delta_pp\": -0.75}, \"conclusion\": \"success\"}, \"eval_math500_grpo_standard_20_fair_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_standard_20_fair_v2.json --max_new_tokens 2048'\", \"gpu\": [\"cuda:1\"], \"pid\": \"22049\", \"model_name\": \"grpo_stage2_standard_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_math500_grpo_standard_20_fair_v2.log\"}, \"metrics\": {\"accuracy\": 0.264, \"n_correct\": 132, \"n_total\": 500, \"stderr\": 0.0197}, \"conclusion\": \"success\"}, \"eval_math500_sft_rasp_20_2048\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.json --max_new_tokens 2048'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"39767\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_rasp_20_2048.log\", \"submitted_at\": \"2026-05-18T23:54:16.231Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"sft_rasp_20_westd\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"wall_clock_seconds\": 6287.1, \"gpu_hours\": 1.75}, \"metrics\": {\"accuracy\": 0.226, \"n_correct\": 113, \"n_total\": 500, \"stderr\": 0.0187, \"natural_eos\": 314, \"truncated\": 186, \"natural_eos_pct\": 0.628, \"avg_response_length\": 930.58, \"median_response_length\": 274}, \"conclusion\": \"success\"}, \"eval_math500_dense_2048\": {\"status\": \"DONE\", \"spec\": {\"gpu\": [\"cuda:0\"], \"pid\": \"32469\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_2048.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.53, \"n_correct\": 265, \"n_total\": 500, \"stderr\": 0.0223, \"natural_eos_pct\": 0.468, \"truncated_pct\": 0.532, \"avg_response_length\": 1724.5, \"median_response_length\": 2048}}, \"eval_math500_grpo_rasp_20_fair\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_grpo_rasp_20_fair.json --max_new_tokens 2048\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"model_name\": \"grpo_stage2_rasp_20_fair\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_grpo_rasp_20_fair.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.24, \"n_correct\": 120, \"n_total\": 500, \"stderr\": 0.0191, \"natural_eos_pct\": 0.64, \"truncated_pct\": 0.36, \"avg_response_length\": 903.5, \"median_response_length\": 272, \"max_new_tokens\": 2048}}, \"eval_gsm8k_sft_cka_only_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"checkpoint_source\": \"sft_cka_only_20_1p5b\", \"eval_data\": \"gsm8k\", \"data_path\": \"gsm8k\", \"data_count\": 1319, \"model_name\": \"Qwen2.5-1.5B-sft-cka-only-20\", \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_sft_cka_only_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3563, \"n_correct\": 470, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9507, \"avg_response_length\": 336.76}}, \"sft_standard_20_retrain_westd\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 2\\\"\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:2\"], \"pid\": \"34346\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain_westd.log\", \"submitted_at\": \"2026-05-18T22:40:50.078Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"pruned_standard_20 -> sft_standard_20\", \"data_path\": \"gsm8k (SFT recovery)\", \"data_count\": 7473, \"seed\": 42, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"wall_clock_seconds\": 2533.8, \"gpu_hours\": 0.7}, \"conclusion\": \"success\", \"metrics\": {\"train_loss\": 0.758, \"mean_token_accuracy\": 0.8252, \"train_runtime_sec\": 1688, \"train_samples_per_second\": 8.856, \"epochs\": 2, \"total_steps\": 1870}}, \"eval_gsm8k_grpo_rasp_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"data_path\": \"gsm8k:test\", \"data_count\": 1319, \"model_name\": \"grpo_rasp_20_1p5b/checkpoint-100\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"eval_data\": \"gsm8k:test\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_rasp_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.2616, \"n_correct\": 345, \"n_total\": 1319, \"stderr\": 0.0121, \"eos_rate\": 0.9378, \"avg_response_length\": 392.7}}, \"eval_math500_sft_cka_only_20_v4_restart\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_sft_cka_only_20_v4.log\", \"results_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/math500_sft_cka_only_20_v4.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.29, \"n_correct\": 145, \"n_total\": 500, \"stderr\": 0.0203, \"natural_eos\": 384, \"truncated\": 116, \"natural_eos_pct\": 0.768, \"avg_response_length\": 673.278, \"median_response_length\": 242.5}}, \"grpo_cka_only_20_extended_300\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"11457\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20_extended_300.log\", \"submitted_at\": \"2026-05-18T15:10:04.515Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (CKA-only 20% pruned, SFT recovered, GRPO extended)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"z9f0z901\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20/checkpoint-100\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 100}, \"wall_clock_seconds\": 23392.2, \"gpu_hours\": 6.5}, \"conclusion\": \"success\", \"metrics\": {\"final_reward\": 0.3075, \"peak_reward\": 0.4444, \"peak_reward_step\": 280, \"reward_step100\": 0.354, \"reward_step300\": 0.3075, \"train_loss_final\": 0.0349, \"global_step\": 300, \"runtime_seconds\": 23004, \"gpu_hours\": 6.5, \"final_frac_zero_std\": 0.275, \"reward_range\": [0.22, 0.44], \"pattern\": \"sustained oscillation, no collapse\", \"wandb_run_id\": \"z9f0z901\"}}, \"eval_gsm8k_grpo_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"gpu\": [\"cuda:0\"], \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b/\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_standard_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.2229, \"n_correct\": 294, \"n_total\": 1319, \"stderr\": 0.0115}}, \"eval_gsm8k_grpo_cka_only_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b/checkpoint-100\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_gsm8k_grpo_cka_only_20_1p5b.json\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.3548, \"n_correct\": 468, \"n_total\": 1319, \"stderr\": 0.0132}}, \"eval_math500_dense_unpruned\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=3 python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/math500_dense_unpruned.json'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:3\"], \"pid\": \"4223\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense unpruned)\", \"data_path\": \"MATH-500\", \"data_count\": 500, \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"eval_data\": \"MATH-500\", \"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"log_path\": \"~/runs/recovery_aware_struct_prune/math500_dense_unpruned.log\"}, \"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.736, \"stderr\": 0.0197, \"n_correct\": 368, \"n_total\": 500, \"natural_eos_pct\": 0.752}}, \"grpo_rasp_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100\", \"server\": \"westb-23072\", \"gpu\": \"cuda:1\", \"pid\": \"815395\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_1p5b.log\", \"submitted_at\": \"2026-05-18T15:13:38.510Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"a18r8uyw\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"learning_rate\": 1e-06, \"max_steps\": 100, \"optimizer\": \"adamw_8bit\"}, \"wall_clock_seconds\": 4438.5, \"gpu_hours\": 1.23}, \"conclusion\": \"success\", \"metrics\": {\"final_reward\": 0.099, \"frac_zero_std\": 0.175, \"clipped_ratio\": 0.82}}, \"grpo_cka_only_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"806188\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"8zkpr0hh\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training, not eval)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"conclusion\": \"success\", \"metrics\": {\"reward_mean\": 0.2375, \"frac_reward_zero_std\": 0.175, \"loss\": 0.0595, \"kl\": 0.00215, \"grad_norm\": 1.445, \"global_step\": 100, \"note\": \"training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\"}}, \"grpo_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_1p5b --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 100'\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:1\"], \"pid\": \"811558\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned, SFT recovered)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"mm31apn0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 100}}, \"metrics\": {\"reward_mean\": 0.0844, \"frac_reward_zero_std\": 0.15, \"loss\": 0.0151, \"grad_norm\": 4.03125, \"kl\": 0.0044, \"entropy\": 0.4617, \"final_step\": 100, \"max_steps\": 100, \"total_time_min\": 53}, \"conclusion\": \"success\"}, \"grpo_standard_20_extended_300_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --loss_type dapo --learning_rate 1e-6 --max_steps 300 --save_steps 50 --save_total_limit 3 --resume_from_checkpoint /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110'\", \"server\": \"westd-29022\", \"gpu\": [\"cuda:0\"], \"pid\": \"6346\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 20% pruned, SFT recovered, GRPO extended v2)\", \"data_path\": \"openai/gsm8k\", \"data_count\": 7473, \"seed\": 42, \"wandb_run_id\": \"44cjdoiy\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_20_extended_300/checkpoint-110\", \"eval_data\": \"openai/gsm8k (GRPO RL training)\", \"hyperparams\": {\"beta\": 0.01, \"temperature\": 0.4, \"repetition_penalty\": 1.15, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_steps\": 300, \"save_steps\": 50, \"save_total_limit\": 3, \"resume_from_step\": 111}}, \"metrics\": {\"reward_mean_step300\": 0.0562, \"loss_step300\": 0.0367, \"frac_reward_zero_std_step300\": 0.525, \"kl_step300\": 0.00306, \"entropy_step300\": 0.157, \"lr_step300\": 3.33e-09, \"runtime_min\": 48, \"reward_decline_after_step260\": true}, \"conclusion\": \"success\"}, \"sft_standard_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (Standard 20% pruned)\", \"seed\": 42}, \"conclusion\": \"success\"}, \"sft_cka_only_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy epoch --gpu 0\", \"server\": \"westb-23072\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (CKA-only 20% pruned)\", \"seed\": 42}, \"conclusion\": \"success\"}, \"sft_rasp_20_1p5b\": {\"status\": \"DONE\", \"spec\": {\"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_1p5b --num_train_epochs 2 --batch_size 4 --gradient_accumulation_steps 2 --learning_rate 2e-5 --save_strategy no --gpu 0\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"802010\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20_1p5b.log\", \"account\": \"root\", \"data_path\": \"openai/gsm8k (train split, cached)\", \"data_count\": 7473, \"model_name\": \"DeepSeek-R1-Distill-Qwen-1.5B (RASP 20% pruned)\", \"seed\": 42, \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20_1p5b\"}, \"conclusion\": \"success\"}, \"inference_bench_cka_only_20_clean\": {\"status\": \"DONE\", \"metrics\": {\"dense\": {\"tokens_per_second\": 75.73, \"avg_latency_sec\": 6.729, \"peak_memory_gb\": 16.22, \"total_tokens\": 25477, \"validation\": \"PASS (75.73 vs expected 76.25, <1% deviation)\"}, \"cka_only_20\": {\"tokens_per_second\": 51.86, \"avg_latency_sec\": 4.078, \"peak_memory_gb\": 11.6, \"total_tokens\": 10574, \"latency_speedup_vs_dense\": \"39.4%\", \"memory_reduction_vs_dense\": \"28.5%\"}, \"rasp_20_dummy\": {\"tokens_per_second\": 75.79, \"avg_latency_sec\": 6.723, \"peak_memory_gb\": 16.23, \"note\": \"Dense model used as dummy (rasp not on westb)\"}}, \"conclusion\": \"success\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --n_prompts 50 --max_new_tokens 512 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/inference_benchmark_cka_only_clean.json\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"data_path\": \"openai/gsm8k (50 prompts)\", \"data_count\": 50, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B + sft_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"sft_cka_only_20 + dense\", \"eval_data\": \"GSM8K 50 prompts (inference latency benchmark)\"}}, \"eval_gsm8k_grpo_cka_only_20_v2\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/gsm8k_grpo_cka_only_20.json --device_map cuda:0\\\"\", \"server\": \"westb-23072\", \"gpu\": [\"cuda:0\"], \"pid\": \"776884\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gsm8k_grpo_cka_only_20_v2.log\", \"submitted_at\": \"2026-05-18T05:54:02.072Z\", \"submitted_via\": \"submit_training_job\", \"backend\": \"tmux\", \"account\": \"root\", \"data_path\": \"openai/gsm8k\", \"data_count\": 1319, \"model_name\": \"grpo_cka_only_20\", \"seed\": 42, \"checkpoint_source\": \"grpo_cka_only_20\", \"eval_data\": \"GSM8K test (1319 samples)\", \"wall_clock_seconds\": 10583.6, \"gpu_hours\": 2.94}, \"metrics\": {\"accuracy\": 0.6437, \"n_correct\": 849, \"n_total\": 1319, \"stderr\": 0.0132, \"eos_rate\": 0.9886, \"avg_response_length\": 203.43, \"truncated\": 15, \"wall_time_sec\": 8921}, \"conclusion\": \"success\"}, \"grpo_cka_only_20\": {\"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 100 --save_steps 99999 --reward_desert_patience 50 --run_name grpo_cka_only_20\\\"\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_cka_only_20.log\", \"pid\": \"725227\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:51:36.270Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 41272.3, \"gpu_hours\": 11.46, \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_cka_only_20\", \"wandb_run_id\": \"li451oi4\"}, \"status\": \"DONE\", \"metrics\": {\"final_step\": 100, \"final_reward\": 0.3444, \"peak_reward\": 0.3544, \"peak_reward_step\": 50, \"final_frac_zero_std\": 0.2, \"final_loss\": 0.23, \"final_kl\": 0.001609, \"final_entropy\": 0.08751, \"final_reward_std\": 0.444, \"runtime_seconds\": 40710}, \"conclusion\": \"success\"}, \"grpo_rasp_20_fair\": {\"conclusion\": \"success\", \"metrics\": {\"final_completion_length\": 963.0, \"final_frac_zero_std\": 0.85, \"final_reward\": 0.01, \"min_frac_zero_std\": 0.675, \"peak_reward\": 0.061, \"total_steps\": 100, \"training_time_minutes\": 62.5, \"trend\": \"stagnation_then_collapse\"}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_fair\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/train_grpo_v5.py --model_path sft_rasp_20_westd --output_dir grpo_stage2_rasp_20_fair --gpu 0 --max_steps 100 --lr 1e-6 --beta 0.01 --loss_type dapo\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"N/A (GRPO training, not eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.3, \"hyperparams\": {\"beta\": 0.01, \"format_reward_weight\": 0.1, \"loss_type\": \"dapo\", \"lr\": 1e-06, \"max_completion_length\": 1024, \"max_steps\": 100, \"optim\": \"adamw_bnb_8bit\", \"repetition_penalty\": 1.15, \"reward_desert_patience\": 200, \"save_steps\": 10, \"save_total_limit\": 3, \"temperature\": 0.4}, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_20_fair.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"68913\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T23:50:31.086Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4668.5}, \"status\": \"DONE\"}, \"eval_postprune_standard_30\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 3907.875, \"correct\": 8, \"eos_rate\": 0.055, \"gsm8k_accuracy\": 0.04, \"natural_eos\": 11, \"total\": 200, \"truncated\": 189}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\", \"checkpoint_source\": \"pruned_standard_30\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30 --max_samples 200 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_standard_30.json\\\"\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (N=200, post-prune accuracy eval)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 5.3, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_standard_30.log\", \"model_name\": \"pruned_standard_30\", \"pid\": \"47667\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:09:42.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 19076.9}, \"status\": \"DONE\"}, \"eval_sft_cka_only_20_n1319\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 198.1, \"correct\": 843, \"eos_rate\": 0.9901, \"gsm8k_accuracy\": 0.6391, \"stderr\": 0.0132, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (1319 samples, greedy)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20_n1319.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"49475\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T19:17:43.358Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\"}, \"prune_cka_only_30\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.2892, \"attn_heads_pruned\": \"0\", \"method\": \"dummy_ones_importance + rasp_alpha1 = pure CKA-only\", \"mlp_groups_pruned\": \"303/784\"}, \"spec\": {\"command\": \"CUDA_VISIBLE_DEVICES=\\\"\\\" python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores_dummy_ones.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_30\", \"data_count\": 0, \"data_path\": \"importance_scores_dummy_ones.pt + cka_scores.pt\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_postprune_rasp_30\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0, \"avg_response_length\": 3984.31, \"eos_rate\": 0.03, \"n_correct\": 0, \"n_total\": 200, \"natural_eos\": 6, \"truncated_rate\": 0.97}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_30.json\", \"checkpoint_source\": \"pruned_rasp_30\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K (200 samples, greedy)\", \"gpu\": [\"cuda:2\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_postprune_rasp_30.log\", \"model_name\": \"pruned_rasp_30\", \"pid\": \"43911\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\"}, \"eval_humaneval_sft_standard_20_2048_v2\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 1850.7, \"correct\": 19, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1159, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.34, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20_2048_v2.log\", \"pid\": \"36724\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T16:26:15.449Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4840.6}, \"status\": \"DONE\"}, \"eval_humaneval_grpo_standard_20_2048\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 1843, \"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.1037, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --max_new_tokens 2048 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_grpo_standard_20_2048.json\\\"\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 4.58, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_standard_20_2048.log\", \"pid\": \"27194\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T13:41:38.223Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 16473.3}, \"status\": \"DONE\"}, \"grpo_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"note\": \"Restored from previous_failure — cron false positive, experiment actually completed 100/100 steps successfully\", \"step_100\": {\"entropy\": 0.04262, \"frac_reward_zero_std\": 0.875, \"grad_norm\": 0.05371, \"kl\": 0.0007035, \"loss\": 0.01275, \"reward\": 0.009375, \"reward_std\": 0.03149}, \"wall_clock_min\": 57.95, \"wandb_run_id\": \"bc4ojqie\"}, \"spec\": {\"command\": \"previous run (bc4ojqie) completed 100/100 steps, restoring status\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"model_name\": \"sft_rasp_25 (RASP 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_humaneval_grpo_rasp_20_2048\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 24, \"max_new_tokens\": 2048, \"pass_at_1\": 0.1463, \"stderr\": 0.0276, \"total\": 164}, \"spec\": {\"account\": \"root\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"model_name\": \"grpo_stage2_rasp_20_v9\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_cka_only_20\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 182.73, \"eos_rate\": 0.995, \"gsm8k_accuracy\": 0.64, \"gsm8k_stderr\": 0.0339, \"mode\": \"greedy\", \"n_correct\": 128, \"n_total\": 200, \"seed\": 42, \"truncated\": 1}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"sft_cka_only_20\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_cka_only_20.json\\\"\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"GSM8K (N=200)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_cka_only_20.log\", \"model_name\": \"sft_cka_only_20\", \"pid\": \"723605\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T14:29:08.063Z\", \"submitted_via\": \"submit_training_job\"}, \"status\": \"DONE\"}, \"sft_cka_only_20\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"note\": \"Initial loss 1.958 > RASP 1.86 > Standard 1.70 (CKA-only has most initial damage). Final loss 0.62 comparable to baselines. No greedy eval run yet.\", \"token_accuracy\": 0.8362, \"total_steps\": 1870, \"train_loss_final\": 0.6165, \"train_loss_initial\": 1.958, \"train_time_min\": 33.4}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20/\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_20 --save_strategy no --gpu 0\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.69, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_cka_only_20.log\", \"pid\": \"720955\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T13:47:02.912Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2486.8}, \"status\": \"DONE\"}, \"eval_humaneval_unpruned_2048\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 1771, \"correct\": 74, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"pass_at_1\": 0.4512, \"stderr\": 0.0389, \"total\": 164, \"wall_time_min\": 67.6}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.2, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_unpruned_2048.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": \"23707\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:06.754Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4337.5}, \"status\": \"DONE\"}, \"eval_humaneval_sft_rasp_20_2048\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 17, \"max_new_tokens\": 2048, \"median_response_length\": 2048, \"note\": \"still truncating at median=2048, main failure mode is thinking chain leaking into code output\", \"pass_at_1\": 0.1037, \"stderr\": 0.0238, \"total\": 164, \"wall_time_min\": 42}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_new_tokens 2048\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems, max_new_tokens=2048)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 1.03, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20_2048.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"23785\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T12:41:09.839Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3691.7}, \"status\": \"DONE\"}, \"eval_humaneval_grpo_standard_20\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 3, \"max_new_tokens\": 512, \"note\": \"512-token truncation, low quality\", \"pass_at_1\": 0.0183, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"python src/eval_humaneval.py --model_path grpo_stage2_standard_20_v8/checkpoint-50\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 3.56, \"log_path\": \"westd results/eval_humaneval_grpo_standard_20.json\", \"model_name\": \"grpo_stage2_standard_20_v8\", \"pid\": \"16483\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T10:00:40.348Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 12799.5}, \"status\": \"DONE\"}, \"eval_math500_unpruned\": {\"conclusion\": \"success\", \"metrics\": {\"N\": 500, \"accuracy\": 0.736, \"correct\": 368, \"stderr\": 0.02}, \"spec\": {\"command\": \"python src/eval_math500.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_gradient_postsft\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.615, \"avg_response_length\": 167.455, \"correct\": 123, \"eos_rate\": 0.995, \"stderr\": 0.0344, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_gradient_postsft.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.27, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_gradient_postsft.log\", \"pid\": \"701495\", \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T10:07:58.275Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4578.0}, \"status\": \"DONE\"}, \"gradient_sft_v3\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.644, \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"steps\": 1870, \"token_accuracy\": 0.825}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_gradient_20\", \"checkpoint_source\": \"pruned_gradient_20 (gradient scoring, 19.09% sparsity)\", \"command\": \"python src/sft_recovery.py --model_path pruned_gradient_20 --output_dir sft_gradient_20 --gpu 0 --save_strategy no --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k (SFT training data)\", \"eval_data\": \"N/A - this is SFT training, not eval\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.66, \"log_path\": \"~/runs/recovery_aware_struct_prune/gradient_sft_v3.log\", \"model_name\": \"pruned_gradient_20\", \"pid\": \"699032\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-17T09:28:21.306Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2385.7}, \"status\": \"DONE\"}, \"eval_math500_sft_standard_20\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 130, \"eos_rate\": 0.578, \"math500_acc\": 0.26, \"stderr\": 0.0196, \"total\": 500, \"truncated\": 211, \"wall_time_hours\": 3.58}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_standard_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_standard.log\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_math500_sft_rasp_20\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 121, \"math500_acc\": 0.242, \"stderr\": 0.0192, \"total\": 500, \"wall_time_hours\": 2.94}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python src/eval_math500.py --model_path sft_rasp_20_westd\", \"data_count\": 500, \"data_path\": \"MATH-500\", \"eval_data\": \"MATH-500 (500 problems)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_math500_sft_rasp.log\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_unstructured_20\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 641, \"correct\": 1159, \"eos_rate\": 0.9803, \"gsm8k_acc\": 0.8787, \"stderr\": 0.009, \"total\": 1319, \"truncated\": 26, \"wall_time_hours\": 3.23}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"checkpoint_source\": \"pruned_unstructured_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_unstructured_20_n1319.json'\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=1319, greedy)\", \"gpu\": [\"cuda:1\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_unstructured_20.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unstructured magnitude 20%)\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_unstructured_20\", \"pid\": \"eval_unstructured_20\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"eval_humaneval_sft_standard_20\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 5, \"failure_modes\": \"model generates CoT natural language instead of code, all responses truncated at max_tokens=512\", \"pass_at_1\": 0.0305, \"stderr\": 0.0134, \"total\": 164, \"wall_time_min\": 17}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_standard_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.6, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_standard_20.log\", \"model_name\": \"sft_standard_20_westd\", \"pid\": \"9605\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:56:07.888Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2144.8}, \"status\": \"DONE\"}, \"eval_humaneval_sft_rasp_20\": {\"conclusion\": \"success\", \"metrics\": {\"correct\": 12, \"failure_modes\": \"model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\", \"median_response_length\": 512, \"note\": \"max_tokens truncation frequent\", \"pass_at_1\": 0.0732, \"stderr\": 0.0203, \"total\": 164}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"bash -c \\\"source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_sft_rasp_20.json\\\"\", \"data_count\": 164, \"data_path\": \"HumanEval\", \"eval_data\": \"HumanEval (164 problems)\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.61, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_sft_rasp_20.log\", \"model_name\": \"sft_rasp_20_westd\", \"pid\": \"7528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T07:19:22.501Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2190.1}, \"status\": \"DONE\"}, \"multiseed_serial_westb\": {\"conclusion\": \"success\", \"metrics\": {\"missing\": \"seed 42 and seed 789 not executed\", \"note\": \"2 seeds x 2 methods (not 4 seeds as planned). Script ran RASP+Standard for seeds 123,456.\", \"rasp_seed123\": {\"acc\": 0.605, \"correct\": 121, \"total\": 200}, \"rasp_seed456\": {\"acc\": 0.6, \"correct\": 120, \"total\": 200}, \"standard_seed123\": {\"acc\": 0.645, \"correct\": 129, \"total\": 200}, \"standard_seed456\": {\"acc\": 0.61, \"correct\": 122, \"total\": 200}}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"checkpoint_source\": \"sft_rasp_20, sft_standard_20\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py (4 serial evals)'\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test (n=200, seeds 123+456)\", \"gpu\": [\"cuda:0\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/multiseed_serial.log\", \"model_name\": \"sft_rasp_20 + sft_standard_20\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_{rasp,standard}_20\", \"pid\": 681896, \"seed\": \"123,456\", \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"eval_humaneval_grpo_rasp_20\": {\"conclusion\": \"success\", \"metrics\": {\"n_passed\": 17, \"n_total\": 164, \"pass_at_1\": 0.1037, \"stderr\": 0.0238}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"python src/eval_humaneval.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"humaneval\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_humaneval_grpo_rasp_20.log\", \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"5264\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-17T06:42:18.740Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2020.1}, \"status\": \"DONE\"}, \"eval_humaneval_unpruned\": {\"conclusion\": \"success\", \"metrics\": {\"n_passed\": 3, \"n_total\": 164, \"pass_at_1\": 0.0183, \"stderr\": 0.0105}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"checkpoint_source\": \"DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"bash -c 'source /root/miniconda3/bin/activate && cd /root/recovery_aware_struct_prune && export HF_ENDPOINT=https://hf-mirror.com && CUDA_VISIBLE_DEVICES=3 python src/eval_humaneval.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json'\", \"data_count\": 164, \"data_path\": \"openai/openai_humaneval\", \"eval_data\": \"HumanEval (164 problems, pass@1)\", \"gpu\": [\"cuda:3\"], \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_humaneval_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"model_path\": \"/root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_humaneval_unpruned.json\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.5315, \"avg_len\": 433.85, \"eos_rate\": 0.9272, \"max_len\": 4096, \"min_len\": 39, \"n_correct\": 701, \"n_total\": 1319, \"stderr\": 0.0137, \"truncated\": 96}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test split (N=1319, greedy)\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_rasp_25.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP 25% pruned, SFT, GRPO 100 steps)\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_n1319.json\", \"pid\": \"639423\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"eval_grpo_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.511, \"avg_len\": 292.86, \"eos_rate\": 0.9628, \"n_correct\": 674, \"n_total\": 1319, \"stderr\": 0.01376}, \"spec\": {\"command\": \"source /root/miniconda3/bin/activate && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"eval_data\": \"GSM8K test (n=1319)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_grpo_standard_25.log\", \"model_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25\", \"output_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_n1319.json\", \"pid\": 48540, \"seed\": 42, \"server\": \"westd-11672\", \"started_at\": \"2026-05-17T05:19:52\"}, \"status\": \"DONE\"}, \"sft_standard_20_retrain\": {\"conclusion\": \"success\", \"metrics\": {\"conclusion\": \"Matches original sft_standard_20 (loss 0.64, token_accuracy 83%). Retrain successful.\", \"token_accuracy\": 0.83, \"train_loss_final\": 0.64}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20/\", \"checkpoint_source\": \"/root/autodl-tmp/pruned_standard_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.81, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20_retrain.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"515168\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-15T11:47:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2914.0}, \"status\": \"DONE\"}, \"eval-sft-alpha-0p0\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.64, \"avg_len\": 257.9, \"eos_rate\": 0.97, \"n_correct\": 64, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_0.0 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.42, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-0p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=0.0 post-SFT\", \"pid\": \"40489\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:26:31.816Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 1529.3}, \"status\": \"DONE\"}, \"eval-sft-alpha-1p0\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.57, \"avg_len\": 224.18, \"eos_rate\": 0.98, \"n_correct\": 57, \"n_total\": 100, \"natural_eos\": 98, \"stderr\": 0.0495, \"truncated\": 2}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --n_samples 100\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.56, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval-sft-alpha-1p0.log\", \"model_name\": \"Qwen2.5-7B pruned alpha=1.0 post-SFT\", \"pid\": \"42530\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T14:51:22.611Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2013.4}, \"status\": \"DONE\"}, \"eval_sft_unpruned_n100\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.84, \"avg_response_length\": 187.22, \"eos_rate\": 1, \"n_correct\": 84, \"n_total\": 100, \"stderr\": 0.0367}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_n100.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 100 --seed 42\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"log_path\": \"/tmp/eval_unpruned_n100.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_unpruned_full\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 81.27, \"accuracy_ci\": 1.07, \"avg_response_length\": 207.18, \"correct\": 1072, \"eos_rate\": 99.7, \"total\": 1319, \"truncated\": 4}, \"spec\": {\"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_unpruned_baseline_full.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_gsm8k.py --model_path sft_unpruned_baseline --max_samples 1319 --seed 42\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full_1319\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Unpruned SFT baseline full GSM8K eval for three-way comparison\", \"log_path\": \"/tmp/eval_unpruned_full.log\", \"model_name\": \"Qwen2.5-7B (unpruned, SFT)\", \"parent\": \"sft_unpruned_baseline\", \"pid\": 74129, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_unpruned_v2_step90\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 80.59, \"avg_response_length\": 213, \"correct\": 1063, \"eos_rate\": 99.6, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-90 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step90.json\\\"\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step90.log\", \"pid\": \"83667\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:13.660Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6194.8}, \"status\": \"DONE\"}, \"eval_grpo_unpruned_v2_step100\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 81.27, \"avg_response_length\": 209, \"correct\": 1072, \"eos_rate\": 99.7, \"seed\": 42, \"total\": 1319}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/autodl-tmp/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_unpruned_v2_step100.json\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.72, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_unpruned_v2_step100.log\", \"pid\": \"83589\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T03:39:11.392Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 6195.8}, \"status\": \"DONE\"}, \"sft_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"runtime_seconds\": 1635, \"token_accuracy\": 0.8073, \"train_loss\": 0.8498}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_25.log\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"pid\": \"88528\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T05:27:08.163Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3002.5}, \"status\": \"DONE\"}, \"sft_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"model_keys\": 339, \"model_params\": \"5.79B\", \"note\": \"optimizer.pt save failed (RuntimeError) but model.safetensors intact\", \"runtime_seconds\": 2130, \"total_steps\": 1870}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_standard_25_retry.log\", \"model_name\": \"pruned_standard_25 (Standard 25% pruned DeepSeek-R1-Distill-Qwen-7B)\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"sft_standard_25_westd\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/model.safetensors\", \"final_loss\": 0.8381, \"token_acc\": 0.8018}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.91, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_25_westd.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard 25% pruned)\", \"pid\": \"21488\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T15:52:30.596Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3273.0}, \"status\": \"DONE\"}, \"eval_grpo_rasp_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.725, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:2\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-postGRPO\", \"parent\": \"grpo_rasp_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_standard_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.705, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:3\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 20% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_qwen_math_v3.\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-postGRPO\", \"parent\": \"grpo_standard_qwen_math_v3\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_rasp_25_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.625, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:0\", \"hypothesis\": \"Qwen2.5-Math-7B RASP 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_rasp_25_qwen_math.\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-postGRPO\", \"parent\": \"grpo_rasp_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_pass_k8_unpruned_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.965, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.965, \"stderr\": 0.013, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_unpruned_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:1\", \"model_name\": \"grpo_unpruned_v2\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_pass_k8_rasp_20_grpo_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.915, \"k\": 8, \"n_samples\": 200, \"pass_at_k\": 0.915, \"stderr\": 0.0197, \"temperature\": 0.7}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:3\", \"model_name\": \"grpo_rasp_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_standard_25_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.635, \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": \"cuda:1\", \"hypothesis\": \"Qwen2.5-Math-7B Standard 25% post-GRPO GSM8K eval (N=200, seed=42). 验证 GRPO 后 accuracy 变化，reward-accuracy decoupling 证据 (C1)。Parent: grpo_standard_25_qwen_math.\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_standard_25_qwen_math.json\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-postGRPO\", \"parent\": \"grpo_standard_25_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_pass_k8_rasp_20_sft_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"avg_response_length\": 139.86, \"eos_rate\": 0.99625, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1594, \"pass_at_k\": 0.935, \"stderr\": 0.0174, \"temperature\": 0.7, \"truncated\": 6}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --pass_k 8 --temperature 0.7 --num_samples_per_prompt 8 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_sft_qwen_math.json\", \"data_count\": 200, \"data_path\": \"GSM8K\", \"eval_data\": \"GSM8K (N=200, pass@8, T=0.7)\", \"gpu\": \"cuda:2\", \"model_name\": \"sft_qwen_math_rasp_20\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft-alpha-1p0\": {\"conclusion\": \"success\", \"metrics\": {\"post_prune_accuracy\": 0.27, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_time_min\": 28}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0\", \"command\": \"python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_1.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_1.0 --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.57, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft-alpha-1p0.log\", \"model_name\": \"pruned_alpha1.0 (α=1.0, 20% sparsity)\", \"pid\": \"38797\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:53:32.117Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2069.9}, \"status\": \"DONE\"}, \"prune_rasp_30\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.2873, \"attn_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"301/784\", \"model_size_gb\": 11, \"params_pruned\": 5427842560, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_30\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.30 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt\", \"data_count\": 512, \"data_path\": \"calibration data\", \"log_path\": \"N/A (CPU)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"prune_standard_30\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.2854, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"299/784\", \"params_after\": 5442379264, \"target_sparsity\": 0.3}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.30 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_30\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_prune_standard_30_20260516T090533.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"prune_rasp_25_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.2405, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"252/784\", \"params_after\": 5783991808, \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"prune_standard_25_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.2396, \"attn_gqa_groups_pruned\": \"0/112\", \"mlp_groups_pruned\": \"251/784\", \"target_sparsity\": 0.25}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.25 --dtype bfloat16 --importance_path results/importance_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_ops_westd_disk_cleanup_qwen25_20260516T105526.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"prune_rasp_rlvr_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_groups_pruned\": 0, \"attn_groups_total\": 112, \"mlp_groups_pruned\": 200, \"mlp_groups_total\": 784, \"pruned_params\": 6161946112}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20_qwen_math\", \"command\": \"python src/prune.py --mode rasp-rlvr --sparsity 0.20\", \"data_count\": 0, \"data_path\": \"N/A\", \"log_path\": \"/tmp/prune_rasp_rlvr_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_pass_k8_rasp_20_grpo_deepseek\": {\"conclusion\": \"success\", \"metrics\": {\"n_problems\": 200, \"pass_k8\": 0.89, \"temperature\": 0.7}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"grpo_stage2_rasp_20_v9\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"gsm8k_test\", \"eval_data\": \"gsm8k_test\", \"gpu\": \"cuda:0\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_rasp_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 162.58, \"eos_rate\": 0.995, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.89, \"stderr\": 0.0221, \"temperature\": 0.7, \"truncated\": 8}, \"model_name\": \"grpo_stage2_rasp_20_v9\", \"pid\": \"61473\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_pass_k8_standard_20_grpo_deepseek\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python eval_pass_k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_standard_20_v8/checkpoint-50 --k 8 --temperature 0.7 --max_samples 200 --seed 42 --max_new_tokens 4096 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_deepseek.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k (test split, N=200)\", \"eval_data\": \"GSM8K test (200 samples, pass@k=8, T=0.7)\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/logs/eval_pass_k8_standard_20_grpo_deepseek.log\", \"metrics\": {\"avg_response_length\": 164.15, \"eos_rate\": 0.9956, \"k\": 8, \"n_problems\": 200, \"pass_at_k\": 0.855, \"stderr\": 0.0249, \"temperature\": 0.7}, \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B Standard 20% post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_rasp_20_full\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6156, \"avg_response_length\": 210.95, \"eos_rate\": 0.9841, \"n_correct\": 812, \"n_samples\": 1319, \"natural_eos\": 1298, \"stderr\": 0.0134, \"truncated\": 21}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full_n1319.json\", \"data_count\": 1319, \"data_path\": \"gsm8k:test\", \"eval_data\": \"gsm8k:test:1319\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_20_full.log\", \"model_name\": \"sft_rasp_20\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"inference_speedup_plan016_v2\": {\"conclusion\": \"success\", \"metrics\": {\"dense\": {\"avg_latency_sec\": 6.682, \"peak_memory_gb\": 16.22, \"tokens_per_second\": 76.25}, \"rasp_20\": {\"avg_latency_sec\": 4.156, \"latency_speedup_vs_dense\": \"37.8%\", \"memory_reduction_vs_dense\": \"28.5%\", \"peak_memory_gb\": 11.6, \"tokens_per_second\": 52.07}, \"standard_20\": {\"avg_latency_sec\": 6.167, \"latency_speedup_vs_dense\": \"7.7%\", \"memory_reduction_vs_dense\": \"28.4%\", \"peak_memory_gb\": 11.61, \"tokens_per_second\": 49.78}}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20 + sft_standard_20 + dense\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/benchmark_inference.py --dense_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --rasp_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --standard_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --n_prompts 50 --max_new_tokens 512\", \"data_count\": 50, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"GSM8K test 50 prompts (inference latency benchmark)\", \"gpu\": \"cuda:1\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/inference_bench.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (dense/rasp_20/standard_20)\", \"seed\": 42, \"server\": \"westb-23072\", \"tmux_session\": \"inference_bench\"}, \"status\": \"DONE\"}, \"eval_pass_k8_standard_20_grpo_qwen_math_v2\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math --pass_k 8 --num_samples_per_prompt 8 --temperature 0.7 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json\", \"data_count\": 200, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test (200 samples)\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/eval_pass_k8_standard_20_v2.log\", \"metrics\": {\"avg_response_length\": 129.995, \"eos_rate\": 0.999375, \"k\": 8, \"n_problems\": 200, \"natural_eos\": 1599, \"pass_at_k\": 0.91, \"stderr\": 0.0202, \"temperature\": 0.7, \"truncated\": 1}, \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-post-GRPO\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_rasp_rlvr_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.71, \"mode\": \"greedy\", \"n_samples\": 200, \"seed\": 42}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_rlvr_20_qwen_math.json\", \"data_count\": 200, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k\", \"model_name\": \"grpo_rasp_rlvr_20_qwen_math\", \"parent\": \"grpo_rasp_rlvr_20_qwen_math\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_postprune_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 21, \"avg_response_length\": 2032.9, \"correct\": 21, \"eos_rate\": 56, \"natural_eos\": 56, \"seed\": 42, \"stderr\": 4.07, \"total\": 100, \"truncated\": 44}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25 --max_samples 100 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_postprune_rasp_25.json\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split (N=100)\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_25 (RASP 25% pruned, no SFT)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"grpo_rasp_rlvr_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"clipped_ratio\": 0.54, \"comparison_vs_rasp_20\": \"RLVR reward 0.090 > RASP 0.061 (+48%), entropy 0.275 >> 0.073 (3.8x)\", \"comparison_vs_standard_20\": \"RLVR reward 0.090 >> Standard 0.044 (+105%)\", \"entropy_final\": 0.275, \"frac_zero_std_final\": 0.7, \"grad_norm_final\": 16.125, \"kl_final\": 0.00581, \"kl_spike_recovery\": \"immediate\", \"kl_spike_step70\": 5756.85, \"loss_final\": 0.0793, \"reward_final\": 0.09, \"reward_std_final\": 0.234, \"total_steps\": 100, \"wall_clock_min\": 45.8, \"wandb_run_id\": \"clzm2cy4\"}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math --gpu 0 --max_steps 100 --run_name grpo_rasp_rlvr_20_qwen_math --seed 42\", \"data_count\": null, \"data_path\": \"built-in GSM8K\", \"eval_data\": \"GSM8K (built-in GRPO reward)\", \"gpu\": \"cuda:0\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR 20% pruned, SFT recovered)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.5299, \"eos_rate\": 0.918, \"n_correct\": 699, \"n_samples\": 1319, \"seed\": 42, \"stderr\": 0.0137, \"truncated\": 108}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_25 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_25.log\", \"model_name\": \"sft_rasp_25 (RASP 25% SFT recovered)\", \"pid\": \"602990\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"sft_rasp_rlvr_20_qwen_math\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math\", \"command\": \"python src/sft_recovery.py --model_path pruned_rasp_rlvr_20_qwen_math --num_train_epochs 2 --lr 2e-5\", \"data_count\": 0, \"data_path\": \"built-in SFT data\", \"log_path\": \"/root/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20_qwen_math.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP-RLVR pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"grpo_rasp_qwen_math_v3\": {\"conclusion\": \"success\", \"metrics\": {\"clipped_ratio_final\": 0.975, \"clipped_ratio_mean\": 0.981, \"collapse_onset\": \"step1\", \"collapse_pattern\": \"entropy_length_collapse\", \"cross_model_match\": \"partial\", \"entropy_mean\": 0.073, \"entropy_vs_standard_ratio\": 0.39, \"frac_zero_std_final\": 0.675, \"frac_zero_std_max\": 0.7, \"frac_zero_std_min\": 0.55, \"kl_final\": 0.009, \"llama_pattern\": \"permanent_reward_collapse\", \"mean_completion_length\": 1010, \"recovery\": false, \"reward_final\": 0.061, \"reward_min\": 0.048, \"reward_peak\": 0.102, \"reward_std_final\": 0.2, \"total_steps\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_qwen_math --gpu 0 --max_completion_length 1024 --beta 0.04 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 5e-7 --max_steps 100 --save_steps 100 --save_total_limit 3 --reward_desert_patience 50 --run_name grpo_rasp_qwen_math_v3 --seed 42\\\"\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.01, \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_rasp_qwen_math_v3.log\", \"model_name\": \"Qwen2.5-Math-7B (RASP 20% SFT recovered)\", \"pid\": \"16812\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T14:49:39.494Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3634.1}, \"status\": \"DONE\"}, \"sft_rasp_rlvr_20\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_rlvr_20 --gpu 1 --learning_rate 2e-5 --num_train_epochs 2 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k_sft\", \"gpu\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_rlvr_20.log\", \"model_name\": \"Qwen2.5-7B-Instruct (RASP-RLVR pruned 20%)\", \"pid\": \"620651\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"eval_sft_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.5125, \"avg_len\": 326.26, \"eos_rate\": 0.9545, \"n_correct\": 676, \"n_total\": 1319, \"stderr\": 0.0138}, \"spec\": {\"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_25.json\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"model_name\": \"sft_standard_25 (Standard 25% pruned + SFT)\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"eval_sft_qwen_math_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 63, \"correct\": 126, \"eos_rate\": 1, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=3 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_standard_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:3\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:3\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%-SFT\", \"pid\": \"6215\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:12.481Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2731.1}, \"status\": \"DONE\"}, \"eval_sft_qwen_math_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 64, \"correct\": 128, \"eos_rate\": 0.995, \"total\": 200}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"CUDA_VISIBLE_DEVICES=2 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_qwen_math_rasp_25.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"gpu\": [\"cuda:2\"], \"gpu_hours\": 0.76, \"gpu_id\": \"cuda:2\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%-SFT\", \"pid\": \"6135\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-16T12:05:10.285Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2732.4}, \"status\": \"DONE\"}, \"sft_qwen_math_standard_25\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6122, \"mean_token_accuracy\": 0.8607, \"throughput_samples_per_sec\": 8.973, \"total_steps\": 1870, \"train_runtime_sec\": 1666}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_25 --gpu 3 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_standard_25.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-25%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_qwen_math_rasp_25\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.6062, \"mean_token_accuracy\": 0.8673, \"throughput_samples_per_sec\": 9.046, \"total_steps\": 1870, \"train_runtime_sec\": 1652}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25_qwen_math --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_25 --gpu 2 --lr 2e-5 --epochs 2 --batch_size 1 --grad_accum 8 --max_seq_len 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_qwen_math_rasp_25.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-25%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_standard_qwen_math_n200\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.71, \"avg_len\": 127.7, \"correct\": 142, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0321}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20\", \"command\": \"CUDA_VISIBLE_DEVICES=1 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_standard_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_standard_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_rasp_qwen_math_n200\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.725, \"avg_len\": 121.8, \"correct\": 145, \"eos_rate\": 1, \"n_total\": 200, \"stderr\": 0.0316}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --max_samples 200 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_sft_rasp_qwen_math.json\", \"data_count\": 200, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test\", \"log_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/eval_rasp_n200.log\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%-SFT\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"prune_rasp_rlvr_20\": {\"conclusion\": \"success\", \"metrics\": {\"actual_sparsity\": 0.1909, \"attn_gqa_groups_pruned\": \"0/112\", \"group_selection_diff_vs_rasp\": \"RASP重剪前6层+后段(19,23-25,27)保中间; RLVR重剪前6层+中后段(16-26)保Layer6-7,27\", \"mlp_groups_pruned\": \"200/784\", \"params_after\": \"6.16B\", \"target_sparsity\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20/\", \"command\": \"CUDA_VISIBLE_DEVICES='' python src/prune.py --model_path /root/autodl-tmp/DeepSeek-R1-Distill-Qwen-7B --mode rasp-rlvr --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --importance_path results/importance_scores.pt --cka_path results/cka_scores.pt --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_rlvr_20\", \"data_count\": 0, \"data_path\": \"results/importance_scores.pt + results/cka_scores.pt\", \"log_path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/logs/workers/worker_code_rasp_rlvr_prune_20260516T095028.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"sft_standard_20_qwen_math\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_standard_20 --gpu 1 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-Standard-20%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_rasp_20_qwen_math\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20/\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_qwen_math_rasp_20 --gpu 0 --num_train_epochs 3 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"log_path\": \"tmux session on westd-11672\", \"model_name\": \"Qwen2.5-Math-7B-RASP-20%\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"prune_standard_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 202, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6147409408, \"sparsity_actual\": 0.1928, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode standard --sparsity 0.20 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_standard_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"prune_rasp_20_qwen_math\": {\"conclusion\": \"success\", \"metrics\": {\"alpha\": 1, \"attn_groups_pruned\": 0, \"mlp_groups_pruned\": 199, \"model_keys\": 339, \"original_params\": 7615616512, \"pruned_params\": 6169214464, \"sparsity_actual\": 0.1899, \"sparsity_target\": 0.2}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"command\": \"python src/prune.py --model_path /root/autodl-tmp/models/Qwen2.5-Math-7B --mode rasp --sparsity 0.20 --alpha 1.0 --dtype bfloat16 --output_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_qwen_math_rasp_20\", \"data_count\": 256, \"data_path\": \"importance_scores_qwen_math.pt + cka_scores_qwen_math.pt\", \"log_path\": \"N/A (CPU-only)\", \"model_name\": \"Qwen2.5-Math-7B\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_grpo_rasp_v9_step10\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 61.87, \"avg_response_length\": 213.6, \"correct\": 816, \"eos_rate\": 98.33, \"seed\": 42, \"stderr\": 1.34, \"total\": 1319, \"truncated\": 22}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=0 python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-10 --max_samples 1319 --seed 42 --output_path /root/autodl-tmp/recovery_aware_struct_prune/results/eval_grpo_rasp_v9_step10.json\\\"\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"openai/gsm8k test split\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 3.06, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step10.log\", \"model_name\": \"grpo_stage2_rasp_20_v9 checkpoint-10\", \"pid\": \"585618\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-16T04:57:36.867Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 11009.3}, \"status\": \"DONE\"}, \"eval_grpo_rasp_v9_step5\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 60.65, \"seed\": 42, \"total\": 1319}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9/checkpoint-5\", \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_grpo_rasp_v9_step5.log\"}, \"status\": \"DONE\"}, \"prune_standard_25\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode standard --sparsity 0.25 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"prune_rasp_25\": {\"conclusion\": \"success\", \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_25\", \"command\": \"python prune.py --model_path DeepSeek-R1-Distill-Qwen-7B --mode rasp --sparsity 0.25 --alpha 1.0 --dtype bfloat16\", \"data_count\": 256, \"data_path\": \"calibration data (from importance/CKA scores)\", \"log_path\": \"N/A (CPU-only, <1min)\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"grpo_unpruned_v2\": {\"conclusion\": \"success\", \"metrics\": {\"avg_step_time_sec\": 23, \"checkpoints_available\": [\"checkpoint-90\", \"checkpoint-95\", \"checkpoint-100\"], \"collapse_onset\": \"N/A\", \"final_entropy\": 0.194, \"final_grad_norm\": 6.97, \"final_kl\": 0.0051, \"final_reward\": 0.661, \"max_steps\": 100, \"peak_reward\": 0.669, \"peak_reward_step\": 80, \"reward_range\": \"0.425-0.669\", \"training_seconds\": 2660}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_unpruned_v2/checkpoint-100\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"command\": \"resume from checkpoint-20, save_total_limit=3, max_steps=100\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_train_7473\", \"gpu_id\": \"cuda:1\", \"log_path\": \"~/runs/recovery_aware_struct_prune/grpo_unpruned_v2.log\", \"model_name\": \"sft_unpruned_baseline (unpruned)\", \"pid\": 77647, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"grpo_stage2_rasp_20_v9\": {\"conclusion\": \"success\", \"metrics\": {\"checkpoints\": [\"checkpoint-10\", \"checkpoint-15\", \"checkpoint-20\", \"checkpoint-25\", \"checkpoint-30\"], \"collapse_note\": \"frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\", \"collapse_status\": \"COLLAPSED\", \"final_clipped_ratio\": 0.956, \"final_frac_zero_std\": 0.95, \"final_grad_norm\": 1.398, \"final_kl\": 0.00118, \"final_loss\": 0.00686, \"final_mean_length\": 996, \"final_mean_terminated_length\": 176, \"final_reward\": 0.021, \"max_steps\": 30, \"reward_history\": [{\"frac_zero_std\": 0.875, \"reward\": 0.015, \"step\": 10}, {\"frac_zero_std\": 0.8, \"reward\": 0.039, \"step\": 20}, {\"frac_zero_std\": 0.95, \"reward\": 0.021, \"step\": 30}], \"step\": 30, \"step_time_sec\": 418, \"total_time\": \"3h28m25s\", \"wandb_url\": \"https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\"}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/train_grpo_v5.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/grpo_stage2_rasp_20_v9 --gpu 0 --max_completion_length 1024 --beta 0.01 --temperature 0.4 --repetition_penalty 1.15 --format_reward_weight 0.1 --gradient_checkpointing true --optim adamw_bnb_8bit --loss_type dapo --learning_rate 1e-6 --max_steps 30 --save_steps 5 --save_total_limit 5 --reward_desert_patience 50 --run_name grpo_stage2_rasp_20_v9\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/grpo_rasp_v9.log\", \"model_name\": \"sft_rasp_20\", \"notes\": \"Auto-launcher tmux session auto_v9_launcher waiting for alpha sweep to finish before starting on cuda:0\", \"pid\": 566666, \"seed\": 42, \"server\": \"westb-23072\"}, \"status\": \"DONE\"}, \"alpha_ablation_sweep\": {\"conclusion\": \"success\", \"metrics\": {\"alpha_0.0\": {\"accuracy\": 0.27, \"avg_len\": 1192, \"eos_rate\": 0.8, \"n_correct\": 27, \"n_total\": 100}, \"alpha_0.25\": {\"accuracy\": 0.23, \"avg_len\": 1834, \"eos_rate\": 0.63, \"n_correct\": 23, \"n_total\": 100}, \"alpha_0.5\": {\"accuracy\": 0.22, \"avg_len\": 1141, \"eos_rate\": 0.81, \"n_correct\": 22, \"n_total\": 100}, \"alpha_1.0\": {\"accuracy\": 0.31, \"avg_len\": 733, \"eos_rate\": 0.92, \"n_correct\": 31, \"n_total\": 100}, \"alpha_2.0\": {\"accuracy\": 0.36, \"avg_len\": 2130, \"eos_rate\": 0.59, \"n_correct\": 36, \"n_total\": 100}}, \"spec\": {\"alphas\": [0, 0.25, 0.5, 1, 2], \"calibration_samples\": 512, \"checkpoint_path\": \"/root/recovery_aware_struct_prune/results/\", \"command\": \"bash run_alpha_sweep_fix.sh\", \"data_count\": 100, \"data_path\": \"openai/gsm8k\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/alpha_sweep_fix.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B\", \"notes\": \"Alpha ablation: 0.25, 0.5, 1.0, 2.0. Partial results: alpha=0.0 acc=0.27 eos=0.80, alpha=0.25 acc=0.23 eos=0.63. Currently running alpha=0.5 eval.\", \"pid\": 556867, \"seed\": 42, \"server\": \"westb-23072\", \"sparsity\": 0.2}, \"status\": \"DONE\"}, \"sft_unpruned_baseline\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 2, \"final_loss\": 0.3321, \"final_token_accuracy\": 0.909, \"total_steps\": 1870, \"train_loss_avg\": 0.4253, \"train_runtime_sec\": 1908, \"train_samples_per_second\": 7.833}, \"spec\": {\"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline\", \"checkpoint_source\": \"/root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B\", \"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && HF_HUB_OFFLINE=1 HF_HOME=/root/autodl-tmp/.hf_cache HF_DATASETS_CACHE=/root/autodl-tmp/.hf_cache/datasets /root/miniconda3/bin/python /root/recovery_aware_struct_prune/src/sft_recovery.py --model_path /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_unpruned_baseline --gpu 1 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --seed 42 --save_strategy no --run_name sft_unpruned_baseline_v2\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k train\", \"estimated_time_minutes\": 33, \"gpu_id\": \"cuda:1\", \"hyperparams\": {\"batch_size\": 1, \"epochs\": 2, \"gradient_accumulation_steps\": 8, \"lr\": 2e-05, \"max_seq_length\": 2048, \"save_strategy\": \"no\", \"seed\": 42}, \"log_path\": \"/tmp/sft_unpruned.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (unpruned)\", \"pid\": 67546, \"seed\": 42, \"server\": \"westd-11672\", \"tmux_session\": \"sft_unpruned\", \"total_steps\": 1870}, \"status\": \"DONE\"}, \"eval_sft_rasp_full_westd\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.6149, \"avg_len\": 216.5, \"eos_rate\": 0.9826, \"n_correct\": 811, \"n_total\": 1319, \"stderr\": 0.0134}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"checkpoint_source\": \"sft_rasp_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --output results/eval_sft_rasp_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:1\", \"log_path\": \"/tmp/eval_rasp_full.log\", \"model_name\": \"sft_rasp_20_westd\", \"output_path\": \"results/eval_sft_rasp_20_westd_full.json\", \"pid\": 62565, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_standard_full_westd\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.5929, \"avg_len\": 226.7, \"eos_rate\": 0.9803, \"n_correct\": 782, \"n_total\": 1319, \"stderr\": 0.01353}, \"spec\": {\"checkpoint_path\": \"results/eval_sft_standard_20_westd_full.json\", \"checkpoint_source\": \"sft_standard_20_westd\", \"command\": \"python eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --output results/eval_sft_standard_20_westd_full.json --n_samples 1319\", \"data_count\": 1319, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k_test_full\", \"gpu_id\": \"cuda:0\", \"log_path\": \"/tmp/eval_standard_full.log\", \"model_name\": \"sft_standard_20_westd\", \"output_path\": \"results/eval_sft_standard_20_westd_full.json\", \"pid\": 62463, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_rasp_20_westd_n100_v2\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_rasp_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_rasp_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:08.325Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2807.6}, \"status\": \"DONE\"}, \"eval_sft_standard_20_westd_n100_v2\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --output_path results/eval_sft_standard_20_westd_n100.json --seed 42\\\"\", \"data_count\": 100, \"data_path\": \"gsm8k test\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.78, \"log_path\": \"~/runs/recovery_aware_struct_prune/eval_sft_standard_20_westd_n100_v2.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20% + SFT westd)\", \"pid\": \"unknown\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T19:24:09.745Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2805.4}, \"status\": \"DONE\"}, \"eval_sft_standard_20_westd_n100\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.63, \"avg_len\": 260.57, \"eos_rate\": 0.97, \"n_correct\": 63, \"n_total\": 100, \"stderr\": 0.048}, \"spec\": {\"checkpoint_source\": \"sft_standard_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_standard_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_standard_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"eval_sft_rasp_20_westd_n100\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.67, \"avg_len\": 182.39, \"eos_rate\": 0.99, \"n_correct\": 67, \"n_total\": 100, \"stderr\": 0.047}, \"spec\": {\"checkpoint_source\": \"sft_rasp_20_westd_retrain\", \"command\": \"bash -c \\\"cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=0 /root/miniconda3/bin/python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_rasp_20_westd_n100.json\\\"\", \"data_count\": 100, \"data_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd\", \"eval_data\": \"gsm8k\", \"model_name\": \"sft_rasp_20_westd\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_rasp_20_westd_retrain\": {\"conclusion\": \"success\", \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd --gpu 0 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_standard_20_westd_retrain\": {\"conclusion\": \"success\", \"metrics\": {\"epochs\": 2, \"final_step_loss\": 0.6403, \"final_token_accuracy\": 0.8258, \"total_steps\": 1870, \"train_loss\": 0.7577, \"train_runtime_sec\": 1679, \"train_samples_per_second\": 8.902}, \"spec\": {\"command\": \"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && python src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20_westd --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8 --seed 42\", \"data_count\": 7473, \"data_path\": \"gsm8k train\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (Standard pruned 20%)\", \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"grasp_baseline_westd\": {\"conclusion\": \"success\", \"metrics\": {\"avg_len\": 4018, \"eos_rate\": 0.02, \"grasp_20_accuracy_n100\": 0.07, \"json_path\": \"results/eval_pruned_graspune_20_greedy.json\", \"n_correct\": 7, \"n_total\": 100, \"rasp_20_accuracy_ref\": 0.31, \"standard_20_accuracy_ref\": 0.27}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_source\": \"GraSP pruning pipeline\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --max_samples 100 --max_new_tokens 4096\", \"command_note\": \"实际运行命令无 --output_path 和 --seed，但源码默认 seed=42 且 output_path 自动回退到 results/eval_pruned_graspune_20_greedy.json\", \"data_count\": 100, \"data_path\": \"gsm8k test split\", \"eval_data\": \"gsm8k test N=100\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 4.44, \"log_path\": \"results/eval_grasp_n100.log\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (GraSP pruned 20%)\", \"pid\": \"38120\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T12:45:44.074Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 15997.5}, \"status\": \"DONE\"}, \"eval_sft_alpha_2p0\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy\": 0.62, \"avg_len\": 277.41, \"eos_rate\": 0.97, \"n_correct\": 62, \"n_total\": 100, \"stderr\": 0.0485}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0\", \"command\": \"python -u src/eval_gsm8k.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --max_samples 100 --max_new_tokens 4096 --seed 42 --output_path results/eval_sft_alpha_2.0_n100.json\", \"data_count\": 100, \"data_path\": \"gsm8k\", \"eval_data\": \"gsm8k_test_n100\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.98, \"log_path\": \"/root/recovery_aware_struct_prune/results/eval_sft_alpha_2.0_n100.log\", \"model_name\": \"alpha_2.0_sft\", \"pid\": \"45428\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T15:42:47.927Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 3534.0}, \"status\": \"DONE\"}, \"sft_alpha2_0_westd\": {\"conclusion\": \"success\", \"metrics\": {\"epoch\": 2, \"mean_token_accuracy_final\": 0.8354, \"post_prune_accuracy\": 0.29, \"total_steps\": 1870, \"train_loss\": 0.7424, \"train_loss_final\": 0.6114, \"train_runtime_sec\": 2422}, \"spec\": {\"checkpoint_source\": \"alpha_ablation_westd_cal256 (pruned_rasp_20_alpha2.0)\", \"command\": \"python sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_models/pruned_rasp_20_alpha2.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_2.0 --gpu 1 --epochs 2 --lr 2e-5 --batch_size 1 --grad_accum 8\", \"data_count\": 7473, \"data_path\": \"gsm8k train split\", \"eval_data\": \"gsm8k train (SFT recovery, not eval)\", \"gpu\": \"cuda:1\", \"model_name\": \"DeepSeek-R1-Distill-Qwen-7B (RASP pruned alpha=2.0, 20% sparsity)\", \"pid\": 43065, \"seed\": 42, \"server\": \"westd-11672\"}, \"status\": \"DONE\"}, \"sft_grasp_20_westd\": {\"conclusion\": \"success\", \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/pruned_graspune_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_graspune_20 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\\\"\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 1.15, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_grasp_20_westd.log\", \"pid\": \"38509\", \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:51:47.632Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 4148.4}, \"status\": \"DONE\"}, \"sft_alpha4_0_westd_retry\": {\"conclusion\": \"success\", \"metrics\": {\"accuracy_stderr\": 0.049, \"avg_response_length\": 238.56, \"eos_rate\": 0.98, \"mean_token_accuracy_final\": 0.8368, \"n_correct\": 62, \"n_total\": 100, \"post_prune_accuracy\": 0.4, \"post_sft_accuracy_100\": 0.62, \"sft_recovery_gain_pp\": 22, \"train_loss_final\": 0.7393, \"train_loss_last_logged\": 0.6106}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0\", \"checkpoint_source\": \"/root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0\", \"command\": \"bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/recovery_aware_struct_prune && CUDA_VISIBLE_DEVICES=1 python -u src/sft_recovery.py --model_path /root/autodl-tmp/recovery_aware_struct_prune/alpha_ablation/alpha_4.0 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_ablation/alpha_4.0 --gpu 0 --num_train_epochs 2 --learning_rate 2e-5 --batch_size 1 --gradient_accumulation_steps 8 --max_seq_length 2048 --logging_steps 10 --seed 42\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"eval_data\": \"gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.1, \"log_path\": \"/tmp/sft_alpha4.0.log\", \"model_name\": \"pruned_alpha4.0 (a=4.0, 20% sparsity)\", \"pid\": \"37013\", \"seed\": 42, \"server\": \"westd-11672\", \"submitted_at\": \"2026-05-15T13:42:03.641Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 358.8}, \"status\": \"DONE\"}, \"reeval_postprune_definitive\": {\"conclusion\": \"success\", \"metrics\": {\"conclusion\": \"Original 29x advantage (29% vs 1%) not reproducible. Actual gap 4pp (31% vs 27% on westb), not statistically significant.\", \"original_claim_rasp\": 0.29, \"original_claim_standard\": 0.01, \"rasp_20_accuracy_westb\": 0.31, \"rasp_20_accuracy_westd\": 0.29, \"rasp_vs_standard_gap_pp\": 4, \"standard_20_accuracy_westb\": 0.27}, \"spec\": {\"checkpoint_path\": \"N/A (eval only)\", \"command\": \"python src/eval_gsm8k.py --model_path /root/autodl-tmp/pruned_{rasp,standard}_20 --max_samples 100 --max_new_tokens 4096\", \"data_count\": 100, \"data_path\": \"gsm8k_test\", \"log_path\": \"N/A\", \"model_name\": \"pruned_rasp_20 + pruned_standard_20\", \"seed\": 42, \"server\": \"westb-23072 + westd-11672\"}, \"status\": \"DONE\"}, \"sft_standard_20\": {\"conclusion\": \"success\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.64, \"greedy_avg_len\": 176.31, \"greedy_correct\": 64, \"greedy_max_len\": 4096, \"greedy_min_len\": 43, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.7, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_standard_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_standard_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:1\"], \"gpu_hours\": 0.83, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_standard_20.log\", \"model_name\": \"pruned_standard_20\", \"pid\": \"249655\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:25.361Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2999.5}, \"status\": \"DONE\"}, \"sft_rasp_20\": {\"conclusion\": \"success\", \"metrics\": {\"eos_rate_greedy_100\": 0.99, \"greedy_accuracy_100\": 0.57, \"greedy_avg_len\": 179.83, \"greedy_correct\": 57, \"greedy_max_len\": 4096, \"greedy_min_len\": 59, \"greedy_total\": 100, \"sampling_eos_rate_5\": 1, \"token_accuracy\": 0.83, \"total_steps\": 1870, \"train_loss_final\": 0.64, \"train_loss_initial\": 1.86, \"train_time_min\": 37}, \"spec\": {\"account\": \"root\", \"backend\": \"tmux\", \"checkpoint_path\": \"/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20\", \"command\": \"python src/sft_recovery.py --model_path /root/autodl-tmp/pruned_rasp_20 --output_dir /root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20 --num_train_epochs 2 --learning_rate 2e-5\", \"data_count\": 7473, \"data_path\": \"openai/gsm8k\", \"gpu\": [\"cuda:0\"], \"gpu_hours\": 0.82, \"log_path\": \"~/runs/recovery_aware_struct_prune/sft_rasp_20.log\", \"model_name\": \"pruned_rasp_20\", \"pid\": \"249577\", \"seed\": 42, \"server\": \"westb-23072\", \"submitted_at\": \"2026-05-14T23:47:23.413Z\", \"submitted_via\": \"submit_training_job\", \"wall_clock_seconds\": 2961.2}, \"status\": \"DONE\"}}, \"count\": 263, \"total\": 263, \"baseline\": null}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 2.0662}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
The registry result is too large to load directly. I need to use jq to extract specific experiments. Let me note down all the table contents first, then query the registry for specific experiments.

Let me catalog all numerical cells from each table:

### tab1_recovery_gradient.tex
- CKA-only: Peak Rew 0.354, Mean Rew 0.285, Min f0 0.125
- Random: Peak Rew 0.190, Mean Rew 0.164, Min f0 0.300


- Standard: Peak Rew 0.081, Mean Rew 0.050, Min f0 0.500
- RASP (α=1.0): Peak Rew 0.061, Mean Rew 0.031, Min f0 0.675

### tab2_decoupling.tex
- Unpruned: SFT 81.27%, GRPO 81.27%, Δ 0.00, Peak Rew 0.669
- CKA-only 20%: SFT 63.91%, GRPO 64.39±0.19

, Δ +0.48, Peak Rew 0.354
- Standard 20%: SFT 59.29%, GRPO 59.84±0.38, Δ +0.55, Peak Rew 0.081
- RASP (α=1.0) 20%: SFT 61.49%, GRPO 60.88, Δ -0.61, Peak Rew 0.061
- Random 20%: SFT 51.25%, GRPO 50.72±0.15, Δ -0.53, Peak Rew 0.190
- ShortGPT 20%: SFT 44.73%, GRPO 43.37, Δ -1.36, Peak Rew --

Now I'm looking at the cross-scale results starting with the 7B model using CKA-only pruning. Now I'm looking at the stability metrics and performance comparisons across different model configurations. The CKA-only approach shows strong correlation consistency, while the Math500 results reveal that standard and RASP methods benefit significantly from reinforcement learning, with standard models gaining 3.6 percentage points compared to supervised fine-tuning alone. Generating markdown table... Now I'm looking at the performance metrics across different model configurations and need to query the experiment registry to extract the relevant data points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "986d9dc5-3a9c-4d8c-b1e6-0e34bd98ebde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA3hUqekq8fNPXU91NXsmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6141,
      "cache_read_input_tokens": 25909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6141
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

_source line 34_

Registry is too large to load directly. Let me probe its structure and extract relevant experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "990cfae7-4031-46de-897d-cff494433e2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA3hUqekq8fNPXU91NXsmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6141,
      "cache_read_input_tokens": 25909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6141
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

_source line 35_

<details open><summary>🔧 Tool call — Bash · `toolu_01PXgeycEEfucZmLiWat4eCs`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\n# Probe structure\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(f'Type: {type(result).__name__}, Length: {len(result)}')\n# Show first entry keys\nif result:\n    print(f'First entry keys: {list(result[0].keys())}')\n    print(f'First exp_id: {result[0].get(\\\"exp_id\\\",\\\"?\\\")}')\n# List all exp_ids\nexp_ids = [e.get('exp_id','?') for e in result]\nfor eid in sorted(exp_ids):\n    print(eid)\n\"",
  "description": "Probe registry structure and list all exp_ids"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "59a46b9e-ac5d-4eed-8a8e-3579010f0a72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PA3hUqekq8fNPXU91NXsmG",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6141,
      "cache_read_input_tokens": 25909,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6141
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

_source line 36 · 2026-05-24T04:52:22.487Z_

<details><summary>↩ Tool result · reported error · `toolu_01PXgeycEEfucZmLiWat4eCs`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 8, in &lt;module>
    print(f'First entry keys: {list(result[0].keys())}')
                                    ~~~~~~^^^
KeyError: 0
Type: dict, Length: 4
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "d21e8c3b-ed8f-4ede-ab64-c6ed7cb5c777",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 8, in &lt;module>\n    print(f'First entry keys: {list(result[0].keys())}')\n                                    ~~~~~~^^^\nKeyError: 0\nType: dict, Length: 4"
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Bash · `toolu_013pgLfyTt5PYAs2tuosC5ve`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nprint(f'Keys: {list(result.keys())}')\n# It might be a dict with exp_ids as keys\nif isinstance(result, dict):\n    for k in list(result.keys())[:3]:\n        print(f'Key: {k}, type of val: {type(result[k]).__name__}')\n        if isinstance(result[k], dict):\n            print(f'  Sub-keys: {list(result[k].keys())[:10]}')\n\"",
  "description": "Probe registry dict structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "76268e5a-237b-4440-a3a4-bc2666f651dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ff1ymRNjRUCfg4bR5riXB9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2174,
      "cache_read_input_tokens": 32050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2174
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

_source line 38 · 2026-05-24T04:52:32.561Z_

<details><summary>↩ Tool result · `toolu_013pgLfyTt5PYAs2tuosC5ve`</summary>

```text
Keys: ['success', 'data', 'error', 'metadata']
Key: success, type of val: bool
Key: data, type of val: dict
  Sub-keys: ['experiments', 'count', 'total', 'baseline']
Key: error, type of val: NoneType
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "582d6e08-ada9-4d96-bc9e-a5506231c628",
  "tool_use_result": {
    "stdout": "Keys: ['success', 'data', 'error', 'metadata']\nKey: success, type of val: bool\nKey: data, type of val: dict\n  Sub-keys: ['experiments', 'count', 'total', 'baseline']\nKey: error, type of val: NoneType",
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01NpZPQ8MZQri3pvPWznkQhN`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nprint(f'Count: {len(exps)}')\n# list all exp_ids\nfor e in exps:\n    eid = e.get('exp_id','?')\n    print(eid)\n\"",
  "description": "List all experiment IDs from registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "6eee9c40-041c-4560-ab8d-dbd42b417f3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RKh183xyXx5epi7d2qm4AF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 408,
      "cache_read_input_tokens": 34224,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 408
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

_source line 40 · 2026-05-24T04:52:36.774Z_

<details><summary>↩ Tool result · reported error · `toolu_01NpZPQ8MZQri3pvPWznkQhN`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;string>", line 9, in &lt;module>
    eid = e.get('exp_id','?')
          ^^^^^
AttributeError: 'str' object has no attribute 'get'
Count: 263
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "6db0ee83-d02d-4051-8417-1716207b1895",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;string>\", line 9, in &lt;module>\n    eid = e.get('exp_id','?')\n          ^^^^^\nAttributeError: 'str' object has no attribute 'get'\nCount: 263"
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_01EJ4FKTpHe26pWN21UbPjE3`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\ncat \"$REGFILE\" | python3 -c \"\nimport json, sys\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n# It's a dict with exp_id as keys\nprint(f'Type: {type(exps).__name__}, Count: {len(exps)}')\nfor k in sorted(exps.keys()):\n    print(k)\n\" 2>&1 | head -300",
  "description": "List all experiment IDs from dict-keyed registry"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "00029bb0-d64f-43a1-9a47-d0828dca383f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0189AuKzgHhaV53VxMqkBEXv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 365,
      "cache_read_input_tokens": 34632,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 365
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

_source line 42 · 2026-05-24T04:52:50.171Z_

<details><summary>↩ Tool result · `toolu_01EJ4FKTpHe26pWN21UbPjE3`</summary>

```text
Type: dict, Count: 263
alpha_ablation_sweep
cka_calibration_stability_ablation
cka_scoring_stability_ablation
eval-sft-alpha-0p0
eval-sft-alpha-1p0
eval_gradient_postsft
eval_grpo_rasp_20_qwen_math
eval_grpo_rasp_25
eval_grpo_rasp_25_qwen_math
eval_grpo_rasp_rlvr_20_qwen_math
eval_grpo_rasp_v9_step10
eval_grpo_rasp_v9_step5
eval_grpo_standard_20_qwen_math
eval_grpo_standard_25
eval_grpo_standard_25_qwen_math
eval_grpo_unpruned_v2_step100
eval_grpo_unpruned_v2_step90
eval_gsm8k_dense_unpruned
eval_gsm8k_grpo_alpha0p5_20
eval_gsm8k_grpo_alpha2p0_20
eval_gsm8k_grpo_alpha3p0_20
eval_gsm8k_grpo_alpha4_20_v3
eval_gsm8k_grpo_cka_only_15_seed123
eval_gsm8k_grpo_cka_only_15_seed456
eval_gsm8k_grpo_cka_only_15_v2
eval_gsm8k_grpo_cka_only_20_1p5b
eval_gsm8k_grpo_cka_only_20_seed123
eval_gsm8k_grpo_cka_only_20_seed456_full
eval_gsm8k_grpo_cka_only_20_v2
eval_gsm8k_grpo_cka_only_20_verify
eval_gsm8k_grpo_cka_only_25_v3
eval_gsm8k_grpo_depth_first_20
eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3
eval_gsm8k_grpo_random_20_seed123_v2
eval_gsm8k_grpo_random_20_seed456
eval_gsm8k_grpo_random_20_v2
eval_gsm8k_grpo_rasp_20_1p5b
eval_gsm8k_grpo_rasp_20_fair
eval_gsm8k_grpo_shortgpt_20
eval_gsm8k_grpo_standard_15_seed123_v3
eval_gsm8k_grpo_standard_15_seed456_v3
eval_gsm8k_grpo_standard_15_v2
eval_gsm8k_grpo_standard_20_1p5b
eval_gsm8k_grpo_standard_20_fair_v2
eval_gsm8k_grpo_standard_20_seed123
eval_gsm8k_grpo_standard_20_seed123_full
eval_gsm8k_grpo_standard_20_seed456
eval_gsm8k_grpo_standard_20_seed456_full
eval_gsm8k_grpo_standard_25
eval_gsm8k_grpo_unstructured_20
eval_gsm8k_sft_alpha0p5_20
eval_gsm8k_sft_alpha2p0_20
eval_gsm8k_sft_alpha3p0_20
eval_gsm8k_sft_alpha4_20_v5
eval_gsm8k_sft_cka_only_15
eval_gsm8k_sft_cka_only_20
eval_gsm8k_sft_cka_only_20_1p5b
eval_gsm8k_sft_cka_only_25
eval_gsm8k_sft_depth_first_20
eval_gsm8k_sft_qwen_cka_only_20
eval_gsm8k_sft_qwen_standard_20
eval_gsm8k_sft_random_20
eval_gsm8k_sft_rasp_20
eval_gsm8k_sft_rasp_20_1p5b
eval_gsm8k_sft_shortgpt_20
eval_gsm8k_sft_standard_15
eval_gsm8k_sft_standard_20
eval_gsm8k_sft_standard_20_1p5b
eval_gsm8k_sft_standard_25
eval_humaneval_grpo_cka_only_20_1p5b_2048
eval_humaneval_grpo_cka_only_20_2048
eval_humaneval_grpo_rasp_20
eval_humaneval_grpo_rasp_20_2048
eval_humaneval_grpo_rasp_20_fair_2048
eval_humaneval_grpo_standard_20
eval_humaneval_grpo_standard_20_1p5b_2048
eval_humaneval_grpo_standard_20_2048
eval_humaneval_grpo_standard_20_fair_2048_v3
eval_humaneval_sft_cka_only_20_1p5b_2048
eval_humaneval_sft_cka_only_20_2048_v2
eval_humaneval_sft_rasp_20
eval_humaneval_sft_rasp_20_1p5b_2048
eval_humaneval_sft_rasp_20_2048
eval_humaneval_sft_rasp_20_2048_v2
eval_humaneval_sft_standard_20
eval_humaneval_sft_standard_20_1p5b_2048
eval_humaneval_sft_standard_20_2048_v2
eval_humaneval_sft_standard_20_2048_v3
eval_humaneval_sft_standard_25
eval_humaneval_unpruned
eval_humaneval_unpruned_2048
eval_math500_dense_2048
eval_math500_dense_unpruned
eval_math500_grpo_cka_only_20
eval_math500_grpo_cka_only_20_2048
eval_math500_grpo_cka_only_20_2048_v2
eval_math500_grpo_cka_only_20_fixed
eval_math500_grpo_cka_only_25_fixed
eval_math500_grpo_cka_only_25_v2
eval_math500_grpo_random_20_v3
eval_math500_grpo_rasp_20_fair
eval_math500_grpo_rasp_alpha0p5_20
eval_math500_grpo_rasp_alpha1p0_20
eval_math500_grpo_rasp_alpha1p0_20_fixed
eval_math500_grpo_rasp_alpha2p0_20
eval_math500_grpo_rasp_alpha2p0_20_fixed
eval_math500_grpo_rasp_alpha3p0_20
eval_math500_grpo_rasp_alpha4p0_20
eval_math500_grpo_standard_20_fair_2048_v2
eval_math500_grpo_standard_20_fair_v2
eval_math500_grpo_standard_20_fixed
eval_math500_sft_cka_only_20_fixed_v2
eval_math500_sft_cka_only_20_v4_restart
eval_math500_sft_cka_only_20_westd
eval_math500_sft_cka_only_25_v2
eval_math500_sft_qwen_math_cka_only_20
eval_math500_sft_random_20_v3
eval_math500_sft_rasp_20
eval_math500_sft_rasp_20_2048
eval_math500_sft_rasp_alpha0p5_20
eval_math500_sft_rasp_alpha1p0_20_fixed
eval_math500_sft_rasp_alpha1p0_20_v2
eval_math500_sft_rasp_alpha2p0_20
eval_math500_sft_rasp_alpha2p0_20_fixed
eval_math500_sft_rasp_alpha3p0_20
eval_math500_sft_rasp_alpha4p0_20
eval_math500_sft_standard_20
eval_math500_sft_standard_20_1p5b
eval_math500_sft_standard_20_2048_v2
eval_math500_sft_standard_20_2048_v3
eval_math500_sft_standard_25
eval_math500_unpruned
eval_mbpp_dense_unpruned
eval_mbpp_grpo_cka_only_20
eval_mbpp_grpo_rasp_20
eval_mbpp_grpo_shortgpt_20_v2
eval_mbpp_grpo_standard_20_v3
eval_mbpp_grpo_standard_20_v4
eval_mbpp_sft_cka_only_20
eval_mbpp_sft_rasp_20
eval_mbpp_sft_shortgpt_20_v2
eval_mbpp_sft_standard_20_1p5b
eval_mbpp_sft_standard_20_v4
eval_pass_k8_rasp_20_grpo_deepseek
eval_pass_k8_rasp_20_grpo_qwen_math
eval_pass_k8_rasp_20_sft_qwen_math
eval_pass_k8_standard_20_grpo_deepseek
eval_pass_k8_standard_20_grpo_qwen_math_v2
eval_pass_k8_unpruned_qwen_math
eval_postprune_qwen_math_cka_only_20
eval_postprune_qwen_math_standard_20
eval_postprune_rasp_25
eval_postprune_rasp_30
eval_postprune_standard_30
eval_sft_alpha_2p0
eval_sft_cka_only_20
eval_sft_cka_only_20_n1319
eval_sft_qwen_math_rasp_25
eval_sft_qwen_math_standard_25
eval_sft_rasp_20_full
eval_sft_rasp_20_westd_n100
eval_sft_rasp_20_westd_n100_v2
eval_sft_rasp_25
eval_sft_rasp_full_westd
eval_sft_rasp_qwen_math_n200
eval_sft_standard_20_westd_n100
eval_sft_standard_20_westd_n100_v2
eval_sft_standard_25
eval_sft_standard_full_westd
eval_sft_standard_qwen_math_n200
eval_sft_unpruned_full
eval_sft_unpruned_n100
eval_unstructured_20
floor_ablation_0p3_cka_only_20_v2
floor_ablation_0p5_cka_only_20_v2
floor_ablation_0p6_cka_only_20_v2
gradient_flow_analysis
gradient_flow_v3
gradient_sft_v3
grasp_baseline_westd
grpo_alpha4_20
grpo_cka_only_15_seed123
grpo_cka_only_15_seed456
grpo_cka_only_15_v2
grpo_cka_only_20
grpo_cka_only_20_1p5b
grpo_cka_only_20_extended_300
grpo_cka_only_20_seed123
grpo_cka_only_20_seed456
grpo_cka_only_25
grpo_qwen_math_cka_only_20
grpo_random_20
grpo_random_20_retrain_v2
grpo_random_20_seed123
grpo_random_20_seed123_v2
grpo_random_20_seed456
grpo_rasp_20_1p5b
grpo_rasp_20_fair
grpo_rasp_25
grpo_rasp_alpha3p0_20
grpo_rasp_alpha3p0_20_v2
grpo_rasp_qwen_math_v3
grpo_rasp_rlvr_20_qwen_math
grpo_stage2_rasp_20_v9
grpo_standard_15_seed123_v3
grpo_standard_15_seed456_v3
grpo_standard_15_v2
grpo_standard_20_1p5b
grpo_standard_20_extended_300_v2
grpo_standard_20_fair
grpo_standard_20_seed123
grpo_standard_20_seed456
grpo_standard_25
grpo_standard_25_westb
grpo_unpruned_v2
inference_bench_cka_only_20_clean
inference_bench_clean_v2
inference_speedup_plan016_v2
multiseed_serial_westb
prune_cka_only_25
prune_cka_only_30
prune_eval_cka_only_30
prune_eval_standard_30
prune_rasp_20_qwen_math
prune_rasp_25
prune_rasp_25_qwen_math
prune_rasp_30
prune_rasp_rlvr_20
prune_rasp_rlvr_20_qwen_math
prune_standard_20_qwen_math
prune_standard_25
prune_standard_25_qwen_math
prune_standard_30
reeval_postprune_definitive
sft-alpha-1p0
sft_alpha2_0_westd
sft_alpha4_0_westd_retry
sft_cka_only_20
sft_cka_only_20_1p5b
sft_cka_only_25
sft_grasp_20_westd
sft_qwen_math_cka_only_20_v2
sft_qwen_math_rasp_25
sft_qwen_math_standard_25
sft_random_20
sft_rasp_20
sft_rasp_20_1p5b
sft_rasp_20_qwen_math
sft_rasp_20_westd_retrain
sft_rasp_25
sft_rasp_rlvr_20
sft_rasp_rlvr_20_qwen_math
sft_shortgpt_20
sft_standard_20
sft_standard_20_1p5b
sft_standard_20_qwen_math
sft_standard_20_retrain
sft_standard_20_retrain_westd
sft_standard_20_westd_retrain
sft_standard_25
sft_standard_25_retrain
sft_standard_25_westd
sft_unpruned_baseline
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "c8827346-20d9-423c-81a3-840cd65626e3",
  "tool_use_result": {
    "stdout": "Type: dict, Count: 263\nalpha_ablation_sweep\ncka_calibration_stability_ablation\ncka_scoring_stability_ablation\neval-sft-alpha-0p0\neval-sft-alpha-1p0\neval_gradient_postsft\neval_grpo_rasp_20_qwen_math\neval_grpo_rasp_25\neval_grpo_rasp_25_qwen_math\neval_grpo_rasp_rlvr_20_qwen_math\neval_grpo_rasp_v9_step10\neval_grpo_rasp_v9_step5\neval_grpo_standard_20_qwen_math\neval_grpo_standard_25\neval_grpo_standard_25_qwen_math\neval_grpo_unpruned_v2_step100\neval_grpo_unpruned_v2_step90\neval_gsm8k_dense_unpruned\neval_gsm8k_grpo_alpha0p5_20\neval_gsm8k_grpo_alpha2p0_20\neval_gsm8k_grpo_alpha3p0_20\neval_gsm8k_grpo_alpha4_20_v3\neval_gsm8k_grpo_cka_only_15_seed123\neval_gsm8k_grpo_cka_only_15_seed456\neval_gsm8k_grpo_cka_only_15_v2\neval_gsm8k_grpo_cka_only_20_1p5b\neval_gsm8k_grpo_cka_only_20_seed123\neval_gsm8k_grpo_cka_only_20_seed456_full\neval_gsm8k_grpo_cka_only_20_v2\neval_gsm8k_grpo_cka_only_20_verify\neval_gsm8k_grpo_cka_only_25_v3\neval_gsm8k_grpo_depth_first_20\neval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3\neval_gsm8k_grpo_random_20_seed123_v2\neval_gsm8k_grpo_random_20_seed456\neval_gsm8k_grpo_random_20_v2\neval_gsm8k_grpo_rasp_20_1p5b\neval_gsm8k_grpo_rasp_20_fair\neval_gsm8k_grpo_shortgpt_20\neval_gsm8k_grpo_standard_15_seed123_v3\neval_gsm8k_grpo_standard_15_seed456_v3\neval_gsm8k_grpo_standard_15_v2\neval_gsm8k_grpo_standard_20_1p5b\neval_gsm8k_grpo_standard_20_fair_v2\neval_gsm8k_grpo_standard_20_seed123\neval_gsm8k_grpo_standard_20_seed123_full\neval_gsm8k_grpo_standard_20_seed456\neval_gsm8k_grpo_standard_20_seed456_full\neval_gsm8k_grpo_standard_25\neval_gsm8k_grpo_unstructured_20\neval_gsm8k_sft_alpha0p5_20\neval_gsm8k_sft_alpha2p0_20\neval_gsm8k_sft_alpha3p0_20\neval_gsm8k_sft_alpha4_20_v5\neval_gsm8k_sft_cka_only_15\neval_gsm8k_sft_cka_only_20\neval_gsm8k_sft_cka_only_20_1p5b\neval_gsm8k_sft_cka_only_25\neval_gsm8k_sft_depth_first_20\neval_gsm8k_sft_qwen_cka_only_20\neval_gsm8k_sft_qwen_standard_20\neval_gsm8k_sft_random_20\neval_gsm8k_sft_rasp_20\neval_gsm8k_sft_rasp_20_1p5b\neval_gsm8k_sft_shortgpt_20\neval_gsm8k_sft_standard_15\neval_gsm8k_sft_standard_20\neval_gsm8k_sft_standard_20_1p5b\neval_gsm8k_sft_standard_25\neval_humaneval_grpo_cka_only_20_1p5b_2048\neval_humaneval_grpo_cka_only_20_2048\neval_humaneval_grpo_rasp_20\neval_humaneval_grpo_rasp_20_2048\neval_humaneval_grpo_rasp_20_fair_2048\neval_humaneval_grpo_standard_20\neval_humaneval_grpo_standard_20_1p5b_2048\neval_humaneval_grpo_standard_20_2048\neval_humaneval_grpo_standard_20_fair_2048_v3\neval_humaneval_sft_cka_only_20_1p5b_2048\neval_humaneval_sft_cka_only_20_2048_v2\neval_humaneval_sft_rasp_20\neval_humaneval_sft_rasp_20_1p5b_2048\neval_humaneval_sft_rasp_20_2048\neval_humaneval_sft_rasp_20_2048_v2\neval_humaneval_sft_standard_20\neval_humaneval_sft_standard_20_1p5b_2048\neval_humaneval_sft_standard_20_2048_v2\neval_humaneval_sft_standard_20_2048_v3\neval_humaneval_sft_standard_25\neval_humaneval_unpruned\neval_humaneval_unpruned_2048\neval_math500_dense_2048\neval_math500_dense_unpruned\neval_math500_grpo_cka_only_20\neval_math500_grpo_cka_only_20_2048\neval_math500_grpo_cka_only_20_2048_v2\neval_math500_grpo_cka_only_20_fixed\neval_math500_grpo_cka_only_25_fixed\neval_math500_grpo_cka_only_25_v2\neval_math500_grpo_random_20_v3\neval_math500_grpo_rasp_20_fair\neval_math500_grpo_rasp_alpha0p5_20\neval_math500_grpo_rasp_alpha1p0_20\neval_math500_grpo_rasp_alpha1p0_20_fixed\neval_math500_grpo_rasp_alpha2p0_20\neval_math500_grpo_rasp_alpha2p0_20_fixed\neval_math500_grpo_rasp_alpha3p0_20\neval_math500_grpo_rasp_alpha4p0_20\neval_math500_grpo_standard_20_fair_2048_v2\neval_math500_grpo_standard_20_fair_v2\neval_math500_grpo_standard_20_fixed\neval_math500_sft_cka_only_20_fixed_v2\neval_math500_sft_cka_only_20_v4_restart\neval_math500_sft_cka_only_20_westd\neval_math500_sft_cka_only_25_v2\neval_math500_sft_qwen_math_cka_only_20\neval_math500_sft_random_20_v3\neval_math500_sft_rasp_20\neval_math500_sft_rasp_20_2048\neval_math500_sft_rasp_alpha0p5_20\neval_math500_sft_rasp_alpha1p0_20_fixed\neval_math500_sft_rasp_alpha1p0_20_v2\neval_math500_sft_rasp_alpha2p0_20\neval_math500_sft_rasp_alpha2p0_20_fixed\neval_math500_sft_rasp_alpha3p0_20\neval_math500_sft_rasp_alpha4p0_20\neval_math500_sft_standard_20\neval_math500_sft_standard_20_1p5b\neval_math500_sft_standard_20_2048_v2\neval_math500_sft_standard_20_2048_v3\neval_math500_sft_standard_25\neval_math500_unpruned\neval_mbpp_dense_unpruned\neval_mbpp_grpo_cka_only_20\neval_mbpp_grpo_rasp_20\neval_mbpp_grpo_shortgpt_20_v2\neval_mbpp_grpo_standard_20_v3\neval_mbpp_grpo_standard_20_v4\neval_mbpp_sft_cka_only_20\neval_mbpp_sft_rasp_20\neval_mbpp_sft_shortgpt_20_v2\neval_mbpp_sft_standard_20_1p5b\neval_mbpp_sft_standard_20_v4\neval_pass_k8_rasp_20_grpo_deepseek\neval_pass_k8_rasp_20_grpo_qwen_math\neval_pass_k8_rasp_20_sft_qwen_math\neval_pass_k8_standard_20_grpo_deepseek\neval_pass_k8_standard_20_grpo_qwen_math_v2\neval_pass_k8_unpruned_qwen_math\neval_postprune_qwen_math_cka_only_20\neval_postprune_qwen_math_standard_20\neval_postprune_rasp_25\neval_postprune_rasp_30\neval_postprune_standard_30\neval_sft_alpha_2p0\neval_sft_cka_only_20\neval_sft_cka_only_20_n1319\neval_sft_qwen_math_rasp_25\neval_sft_qwen_math_standard_25\neval_sft_rasp_20_full\neval_sft_rasp_20_westd_n100\neval_sft_rasp_20_westd_n100_v2\neval_sft_rasp_25\neval_sft_rasp_full_westd\neval_sft_rasp_qwen_math_n200\neval_sft_standard_20_westd_n100\neval_sft_standard_20_westd_n100_v2\neval_sft_standard_25\neval_sft_standard_full_westd\neval_sft_standard_qwen_math_n200\neval_sft_unpruned_full\neval_sft_unpruned_n100\neval_unstructured_20\nfloor_ablation_0p3_cka_only_20_v2\nfloor_ablation_0p5_cka_only_20_v2\nfloor_ablation_0p6_cka_only_20_v2\ngradient_flow_analysis\ngradient_flow_v3\ngradient_sft_v3\ngrasp_baseline_westd\ngrpo_alpha4_20\ngrpo_cka_only_15_seed123\ngrpo_cka_only_15_seed456\ngrpo_cka_only_15_v2\ngrpo_cka_only_20\ngrpo_cka_only_20_1p5b\ngrpo_cka_only_20_extended_300\ngrpo_cka_only_20_seed123\ngrpo_cka_only_20_seed456\ngrpo_cka_only_25\ngrpo_qwen_math_cka_only_20\ngrpo_random_20\ngrpo_random_20_retrain_v2\ngrpo_random_20_seed123\ngrpo_random_20_seed123_v2\ngrpo_random_20_seed456\ngrpo_rasp_20_1p5b\ngrpo_rasp_20_fair\ngrpo_rasp_25\ngrpo_rasp_alpha3p0_20\ngrpo_rasp_alpha3p0_20_v2\ngrpo_rasp_qwen_math_v3\ngrpo_rasp_rlvr_20_qwen_math\ngrpo_stage2_rasp_20_v9\ngrpo_standard_15_seed123_v3\ngrpo_standard_15_seed456_v3\ngrpo_standard_15_v2\ngrpo_standard_20_1p5b\ngrpo_standard_20_extended_300_v2\ngrpo_standard_20_fair\ngrpo_standard_20_seed123\ngrpo_standard_20_seed456\ngrpo_standard_25\ngrpo_standard_25_westb\ngrpo_unpruned_v2\ninference_bench_cka_only_20_clean\ninference_bench_clean_v2\ninference_speedup_plan016_v2\nmultiseed_serial_westb\nprune_cka_only_25\nprune_cka_only_30\nprune_eval_cka_only_30\nprune_eval_standard_30\nprune_rasp_20_qwen_math\nprune_rasp_25\nprune_rasp_25_qwen_math\nprune_rasp_30\nprune_rasp_rlvr_20\nprune_rasp_rlvr_20_qwen_math\nprune_standard_20_qwen_math\nprune_standard_25\nprune_standard_25_qwen_math\nprune_standard_30\nreeval_postprune_definitive\nsft-alpha-1p0\nsft_alpha2_0_westd\nsft_alpha4_0_westd_retry\nsft_cka_only_20\nsft_cka_only_20_1p5b\nsft_cka_only_25\nsft_grasp_20_westd\nsft_qwen_math_cka_only_20_v2\nsft_qwen_math_rasp_25\nsft_qwen_math_standard_25\nsft_random_20\nsft_rasp_20\nsft_rasp_20_1p5b\nsft_rasp_20_qwen_math\nsft_rasp_20_westd_retrain\nsft_rasp_25\nsft_rasp_rlvr_20\nsft_rasp_rlvr_20_qwen_math\nsft_shortgpt_20\nsft_standard_20\nsft_standard_20_1p5b\nsft_standard_20_qwen_math\nsft_standard_20_retrain\nsft_standard_20_retrain_westd\nsft_standard_20_westd_retrain\nsft_standard_25\nsft_standard_25_retrain\nsft_standard_25_westd\nsft_unpruned_baseline",
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

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now I have all 263 experiment IDs. I need to extract the metrics for specific experiments that correspond to table values. Let me spawn subagents to handle different tables in parallel, each querying the registry file for the relevant experiments.

Actually, let me think about this more carefully. I have 8 tables with many numerical cells. I need to match each cell to a registry experiment and verify the value. Let me extract all the relevant experiments' metrics from the registry file.

Let me group the experiments I need to check:

**Tab1 (recovery_gradient)**: GRPO reward metrics
- CKA-only: grpo_cka_only_20 → Peak Rew 0.354, Mean Rew 0.285, Min f0 0.125


- Random: grpo_random_20 → Peak Rew 0.190, Mean Rew 0.164, Min f0 0.300
- Standard: grpo_standard_20_fair → Peak Rew 0.081, Mean Rew 0.050, Min f0 0.500
- RASP α=1.0: grpo_rasp_20_fair or grpo_stage2_rasp_20_v9 → Peak Rew 0.061, Mean Rew 0.031, Min f0 0.675

**Tab2 (decoupling)**: GSM8K accuracy and reward metrics across different pruning strategies. The unpruned baseline achieves 81.27% SFT accuracy, while CKA-only pruning at 20% drops to around 63-64% for both SFT and GRPO, standard pruning further reduces performance to roughly 59-60%, and RASP pruning sits in between at around 61-62%. Now I'm looking at how the alpha parameter affects performance across different values, with α=2.0 showing the strongest results at 66.11% for GRPO, before declining slightly at higher alpha values. I'm also starting to examine the sparsity cliff experiments with 30% sparsity conditions. I'm seeing there are also stability ablation experiments and results for MATH-500 and MBPP benchmarks to track. Rather than manually hunting through all these, I should write a script that pulls all the experiment metrics directly from the registry file so I can systematically compare them against the table values.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "baa2987a-a137-47f8-834f-d362392c9dde",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F16ZHfBTNvn8AP54sr1391",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 34997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4155
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

_source line 44_

Now let me extract all relevant experiment metrics from the registry in one comprehensive pass.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "5d6700b8-19bd-44a4-9a70-1d362b9e69b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F16ZHfBTNvn8AP54sr1391",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 34997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4155
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

_source line 45_

<details open><summary>🔧 Tool call — Bash · `toolu_01WeM1NN2SgBDaNKu23SH9xx`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\ncat \"$REGFILE\" | python3 << 'PYEOF'\nimport json, sys\n\ndata = json.load(sys.stdin)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Extract all experiments with their metrics\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    metrics = e.get('metrics', {})\n    if metrics:\n        print(f\"=== {eid} ===\")\n        # Print metrics compactly\n        for k, v in sorted(metrics.items()):\n            if isinstance(v, (int, float)):\n                print(f\"  {k}: {v}\")\n            elif isinstance(v, dict):\n                for k2, v2 in sorted(v.items()):\n                    if isinstance(v2, (int, float)):\n                        print(f\"  {k}.{k2}: {v2}\")\n            elif isinstance(v, str) and len(v) < 100:\n                print(f\"  {k}: {v}\")\nPYEOF\n",
  "description": "Extract all experiment metrics from registry",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "43ecc487-c709-4f1c-b51c-83f520dbf288",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F16ZHfBTNvn8AP54sr1391",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4155,
      "cache_read_input_tokens": 34997,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4155
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

_source line 46 · 2026-05-24T04:53:24.323Z_

<details><summary>↩ Tool result · reported error · `toolu_01WeM1NN2SgBDaNKu23SH9xx`</summary>

```text
Exit code 1
Traceback (most recent call last):
  File "&lt;stdin>", line 3, in &lt;module>
  File "/usr/lib/python3.14/json/__init__.py", line 298, in load
    return loads(fp.read(),
        cls=cls, object_hook=object_hook,
        parse_float=parse_float, parse_int=parse_int,
        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)
  File "/usr/lib/python3.14/json/__init__.py", line 352, in loads
    return _default_decoder.decode(s)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^
  File "/usr/lib/python3.14/json/decoder.py", line 345, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.14/json/decoder.py", line 363, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "616e8b35-66b4-443b-a45e-344b0c7bbef0",
  "tool_use_result": "Error: Exit code 1\nTraceback (most recent call last):\n  File \"&lt;stdin>\", line 3, in &lt;module>\n  File \"/usr/lib/python3.14/json/__init__.py\", line 298, in load\n    return loads(fp.read(),\n        cls=cls, object_hook=object_hook,\n        parse_float=parse_float, parse_int=parse_int,\n        parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)\n  File \"/usr/lib/python3.14/json/__init__.py\", line 352, in loads\n    return _default_decoder.decode(s)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 345, in decode\n    obj, end = self.raw_decode(s, idx=_w(s, 0).end())\n               ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^\n  File \"/usr/lib/python3.14/json/decoder.py\", line 363, in raw_decode\n    raise JSONDecodeError(\"Expecting value\", s, err.value) from None\njson.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)"
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Bash · `toolu_015Z6SG5UgbXj8QWFsgayUet`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\nhead -c 200 \"$REGFILE\"\necho \"---\"\nwc -c \"$REGFILE\"",
  "description": "Check file format"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "65851b5a-edf3-4c52-8d5e-7ed0543d5327",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016qtP7Nhc5VzapPXrTUinrx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2137,
      "cache_read_input_tokens": 39152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2137
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

_source line 48 · 2026-05-24T04:53:28.902Z_

<details><summary>↩ Tool result · `toolu_015Z6SG5UgbXj8QWFsgayUet`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"experiments\": {\"eval_math500_sft_rasp_alpha2p0_20_fixed\": {\"status\": \"DONE\", \"spec\": {\"command\": \"bash -c \\\"source /root/miniconda3/etc/profil---
264080 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "cdf2c9c9-15fb-4aa1-b86d-b5f1a2697469",
  "tool_use_result": {
    "stdout": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"experiments\\\": {\\\"eval_math500_sft_rasp_alpha2p0_20_fixed\\\": {\\\"status\\\": \\\"DONE\\\", \\\"spec\\\": {\\\"command\\\": \\\"bash -c \\\\\\\"source /root/miniconda3/etc/profil---\n264080 /home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt",
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_017iouwf8Ne62uSe33ZYqxkH`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\nfor eid in sorted(exps.keys()):\n    e = exps[eid]\n    metrics = e.get('metrics', {})\n    if metrics:\n        print(f'=== {eid} ===')\n        for k, v in sorted(metrics.items()):\n            if isinstance(v, (int, float)):\n                print(f'  {k}: {v}')\n            elif isinstance(v, dict):\n                for k2, v2 in sorted(v.items()):\n                    if isinstance(v2, (int, float)):\n                        print(f'  {k}.{k2}: {v2}')\n            elif isinstance(v, str) and len(v) < 100:\n                print(f'  {k}: {v}')\n\" 2>&1 | head -1000",
  "description": "Extract metrics from all experiments",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "f8ebd9ef-9d94-475a-9459-a52e1ad77fcd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015sWrvAF661eTMmGfHs2iow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 387,
      "cache_read_input_tokens": 41289,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 387
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

_source line 50 · 2026-05-24T04:53:34.180Z_

<details><summary>↩ Tool result · `toolu_017iouwf8Ne62uSe33ZYqxkH`</summary>

```text
=== alpha_ablation_sweep ===
  alpha_0.0.accuracy: 0.27
  alpha_0.0.avg_len: 1192
  alpha_0.0.eos_rate: 0.8
  alpha_0.0.n_correct: 27
  alpha_0.0.n_total: 100
  alpha_0.25.accuracy: 0.23
  alpha_0.25.avg_len: 1834
  alpha_0.25.eos_rate: 0.63
  alpha_0.25.n_correct: 23
  alpha_0.25.n_total: 100
  alpha_0.5.accuracy: 0.22
  alpha_0.5.avg_len: 1141
  alpha_0.5.eos_rate: 0.81
  alpha_0.5.n_correct: 22
  alpha_0.5.n_total: 100
  alpha_1.0.accuracy: 0.31
  alpha_1.0.avg_len: 733
  alpha_1.0.eos_rate: 0.92
  alpha_1.0.n_correct: 31
  alpha_1.0.n_total: 100
  alpha_2.0.accuracy: 0.36
  alpha_2.0.avg_len: 2130
  alpha_2.0.eos_rate: 0.59
  alpha_2.0.n_correct: 36
  alpha_2.0.n_total: 100
=== cka_calibration_stability_ablation ===
  n_splits: 5
  size_sensitivity_128: 0.982
  size_sensitivity_256: 0.989
  size_sensitivity_512: 0.995
  split_half_rho: 0.9932
=== cka_scoring_stability_ablation ===
  mean_combined_rho: 0.979
  min_combined_rho: 0.964
  spearman_256v1024_attn: 0.9762
  spearman_256v1024_combined: 0.9641
  spearman_256v1024_mlp: 0.9464
  spearman_256v512_attn: 0.989
  spearman_256v512_combined: 0.9788
  spearman_256v512_mlp: 0.9683
  spearman_512v1024_attn: 0.995
  spearman_512v1024_combined: 0.9938
  spearman_512v1024_mlp: 0.9908
  stable: True
=== eval-sft-alpha-0p0 ===
  accuracy: 0.64
  avg_len: 257.9
  eos_rate: 0.97
  n_correct: 64
  n_total: 100
=== eval-sft-alpha-1p0 ===
  accuracy: 0.57
  avg_len: 224.18
  eos_rate: 0.98
  n_correct: 57
  n_total: 100
  natural_eos: 98
  stderr: 0.0495
  truncated: 2
=== eval_gradient_postsft ===
  accuracy: 0.615
  avg_response_length: 167.455
  correct: 123
  eos_rate: 0.995
  stderr: 0.0344
  total: 200
=== eval_grpo_rasp_20_qwen_math ===
  accuracy: 0.725
  n_samples: 200
  seed: 42
=== eval_grpo_rasp_25 ===
  accuracy: 0.5315
  avg_len: 433.85
  eos_rate: 0.9272
  max_len: 4096
  min_len: 39
  n_correct: 701
  n_total: 1319
  stderr: 0.0137
  truncated: 96
=== eval_grpo_rasp_25_qwen_math ===
  accuracy: 0.625
  n_samples: 200
  seed: 42
=== eval_grpo_rasp_rlvr_20_qwen_math ===
  accuracy: 0.71
  mode: greedy
  n_samples: 200
  seed: 42
=== eval_grpo_rasp_v9_step10 ===
  accuracy: 61.87
  avg_response_length: 213.6
  correct: 816
  eos_rate: 98.33
  seed: 42
  stderr: 1.34
  total: 1319
  truncated: 22
=== eval_grpo_rasp_v9_step5 ===
  accuracy: 60.65
  seed: 42
  total: 1319
=== eval_grpo_standard_20_qwen_math ===
  accuracy: 0.705
  n_samples: 200
  seed: 42
=== eval_grpo_standard_25 ===
  accuracy: 0.511
  avg_len: 292.86
  eos_rate: 0.9628
  n_correct: 674
  n_total: 1319
  stderr: 0.01376
=== eval_grpo_standard_25_qwen_math ===
  accuracy: 0.635
  n_samples: 200
  seed: 42
=== eval_grpo_unpruned_v2_step100 ===
  accuracy: 81.27
  avg_response_length: 209
  correct: 1072
  eos_rate: 99.7
  seed: 42
  total: 1319
=== eval_grpo_unpruned_v2_step90 ===
  accuracy: 80.59
  avg_response_length: 213
  correct: 1063
  eos_rate: 99.6
  seed: 42
  total: 1319
=== eval_gsm8k_dense_unpruned ===
  avg_response_length: 594
  correct: 1198
  eos_rate: 0.9871
  eval_time: 3h7m
  gsm8k_accuracy: 0.9083
  gsm8k_accuracy_ci: 0.0079
  total: 1319
  truncated: 17
=== eval_gsm8k_grpo_alpha0p5_20 ===
  gsm8k_accuracy: 0.6118
  gsm8k_correct: 807
  gsm8k_total: 1319
=== eval_gsm8k_grpo_alpha2p0_20 ===
  gsm8k_accuracy: 0.6611
  gsm8k_correct: 872
  gsm8k_total: 1319
=== eval_gsm8k_grpo_alpha3p0_20 ===
  avg_response_length: 219.7
  correct: 837
  eos_rate: 0.9864
  gsm8k_accuracy: 0.6345
  stderr: 0.0133
  total: 1319
  truncated: 18
=== eval_gsm8k_grpo_alpha4_20_v3 ===
  avg_response_length: 188.16
  eos_rate: 0.9856
  gsm8k_accuracy: 0.6277
  gsm8k_accuracy_ci: 0.0133
  gsm8k_correct: 828
  gsm8k_total: 1319
  natural_eos: 1300
  truncated: 19
=== eval_gsm8k_grpo_cka_only_15_seed123 ===
  accuracy: 73.09
  eos_rate: 98.79
  n_correct: 964
  n_total: 1319
  stderr: 1.22
  truncated: 16
=== eval_gsm8k_grpo_cka_only_15_seed456 ===
  accuracy: 0.721
  avg_response_length: 201.94
  eos_rate: 0.9894
  n_correct: 951
  n_total: 1319
  stderr: 0.0123
=== eval_gsm8k_grpo_cka_only_15_v2 ===
  avg_response_length: 202.4
  correct: 964
  eos_rate: 0.9894
  gsm8k_accuracy: 0.7309
  gsm8k_accuracy_ci: 0.0122
  total: 1319
=== eval_gsm8k_grpo_cka_only_20_1p5b ===
  accuracy: 0.3548
  n_correct: 468
  n_total: 1319
  stderr: 0.0132
=== eval_gsm8k_grpo_cka_only_20_seed123 ===
  accuracy: 0.6422
  avg_response_length: 195.97
  eos_rate: 0.9909
  n_correct: 847
  n_total: 1319
  natural_eos: 1307
  stderr: 0.0132
  truncated: 12
=== eval_gsm8k_grpo_cka_only_20_seed456_full ===
  avg_response_length: 204.3
  correct: 852
  eos_rate: 0.9886
  gsm8k_accuracy: 0.6459
  gsm8k_accuracy_ci: 0.0132
  total: 1319
=== eval_gsm8k_grpo_cka_only_20_v2 ===
  accuracy: 0.6437
  avg_response_length: 203.43
  eos_rate: 0.9886
  n_correct: 849
  n_total: 1319
  stderr: 0.0132
  truncated: 15
  wall_time_sec: 8921
=== eval_gsm8k_grpo_cka_only_20_verify ===
  accuracy: 0.6406
  accuracy_diff_pp: -0.31
  avg_response_length: 201.76
  eos_rate: 0.9894
  n_correct: 845
  n_total: 1319
  original_accuracy: 0.6437
  stderr: 0.0132
=== eval_gsm8k_grpo_cka_only_25_v3 ===
  correct: 786
  eos_rate: 0.9818
  gsm8k_accuracy: 0.5959
  n_total: 1319
=== eval_gsm8k_grpo_depth_first_20 ===
  accuracy_approx: 0.08
  early_stopped: True
  result_file_on_westb: False
=== eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3 ===
  accuracy: 0.486
  avg_response_length: 1766.5
  correct: 243
  natural_eos_pct: 0.162
  stderr: 0.0224
  total: 500
  truncated_pct: 0.838
=== eval_gsm8k_grpo_random_20_seed123_v2 ===
  accuracy: 0.5072
  avg_response_length: 177.9
  eos_rate: 0.9939
  n_correct: 669
  n_total: 1319
  stderr: 0.01377
=== eval_gsm8k_grpo_random_20_seed456 ===
  avg_response_length: 163.5
  eos_rate: 0.9954
  gsm8k_accuracy: 0.5087
  gsm8k_accuracy_se: 0.0138
  gsm8k_correct: 671
  gsm8k_total: 1319
  truncated: 6
=== eval_gsm8k_grpo_random_20_v2 ===
  avg_response_length: 173
  correct: 667
  eos_rate: 0.9954
  gsm8k_accuracy: 0.5057
  gsm8k_stderr: 0.0138
  total: 1319
=== eval_gsm8k_grpo_rasp_20_1p5b ===
  accuracy: 0.2616
  avg_response_length: 392.7
  eos_rate: 0.9378
  n_correct: 345
  n_total: 1319
  stderr: 0.0121
=== eval_gsm8k_grpo_rasp_20_fair ===
  accuracy: 0.6088
  avg_response_length: 195.7
  eos_rate: 0.9879
  n_correct: 803
  n_total: 1319
  stderr: 0.0134
=== eval_gsm8k_grpo_shortgpt_20 ===
  gsm8k_accuracy: 43.37
  n_correct: 572
  n_total: 1319
  stderr: 0.0136
=== eval_gsm8k_grpo_standard_15_seed123_v3 ===
  accuracy: 0.6513
  accuracy_se: 0.0131
  avg_response_length: 183.25
  eos_rate: 0.9932
  n_correct: 859
  n_total: 1319
=== eval_gsm8k_grpo_standard_15_seed456_v3 ===
  avg_response_length: 180.23
  eos_rate: 0.9939
  gsm8k_accuracy: 0.6543
  gsm8k_stderr: 0.0131
  n_correct: 863
  n_total: 1319
=== eval_gsm8k_grpo_standard_15_v2 ===
  avg_response_length: 184
  correct: 872
  eos_rate: 0.993
  gsm8k_accuracy: 0.6611
  total: 1319
=== eval_gsm8k_grpo_standard_20_1p5b ===
  accuracy: 0.2229
  n_correct: 294
  n_total: 1319
  stderr: 0.0115
=== eval_gsm8k_grpo_standard_20_fair_v2 ===
  accuracy: 59.44
  n_correct: 784
  n_total: 1319
=== eval_gsm8k_grpo_standard_20_seed123 ===
  accuracy: 0.64
  avg_response_length: 187.9
  eos_rate: 0.99
  n_correct: 128
  n_total: 200
  stderr: 0.0339
=== eval_gsm8k_grpo_standard_20_seed123_full ===
  accuracy: 0.5989
  n_correct: 790
  n_total: 1319
  stderr: 0.0135
=== eval_gsm8k_grpo_standard_20_seed456 ===
  accuracy: 0.665
  avg_response_length: 166.9
  eos_rate: 0.995
  n_correct: 133
  n_total: 200
  stderr: 0.0334
=== eval_gsm8k_grpo_standard_20_seed456_full ===
  accuracy: 0.602
  eos_rate: 0.9856
  n_correct: 794
  n_total: 1319
  stderr: 0.01348
=== eval_gsm8k_grpo_standard_25 ===
  avg_response_length: 314.47
  correct: 684
  eos_rate: 0.9575
  gsm8k_accuracy: 0.5186
  n_total: 1319
  stderr: 0.0138
=== eval_gsm8k_grpo_unstructured_20 ===
  accuracy: 0.8764
  avg_response_length: 600
  eos_rate: 0.9818
  n_correct: 1156
  n_total: 1319
  stderr: 0.00906
  truncated: 24
=== eval_gsm8k_sft_alpha0p5_20 ===
  gsm8k_accuracy: 0.6073
  gsm8k_correct: 801
  gsm8k_total: 1319
=== eval_gsm8k_sft_alpha2p0_20 ===
  gsm8k_accuracy: 0.6497
  gsm8k_correct: 857
  gsm8k_total: 1319
=== eval_gsm8k_sft_alpha3p0_20 ===
  avg_response_length: 188.63
  eos_rate: 0.9879
  gsm8k_accuracy: 0.6414
  gsm8k_correct: 846
  gsm8k_stderr: 0.0132
  gsm8k_total: 1319
  natural_eos: 1303
  truncated: 16
=== eval_gsm8k_sft_alpha4_20_v5 ===
  avg_response_length: 197.85
  correct: 817
  eos_rate: 0.981
  gsm8k_accuracy: 0.6194
  stderr: 0.0134
  total: 1319
=== eval_gsm8k_sft_cka_only_15 ===
  correct: 952
  gsm8k_accuracy: 0.7218
  total: 1319
=== eval_gsm8k_sft_cka_only_20 ===
  avg_response_length: 198.1
  correct: 843
  eos_rate: 0.9901
  gsm8k_accuracy: 0.6391
  gsm8k_accuracy_ci: 0.0132
  total: 1319
  truncated: 13
=== eval_gsm8k_sft_cka_only_20_1p5b ===
  accuracy: 0.3563
  avg_response_length: 336.76
  eos_rate: 0.9507
  n_correct: 470
  n_total: 1319
  stderr: 0.0132
=== eval_gsm8k_sft_cka_only_25 ===
  avg_response_length: 243.6
  correct: 793
  eos_rate: 0.9803
  gsm8k_accuracy: 0.6012
  n_total: 1319
  stderr: 0.0135
=== eval_gsm8k_sft_depth_first_20 ===
  accuracy_approx: 0.1
  early_stopped: True
  result_file_on_westb: False
=== eval_gsm8k_sft_qwen_cka_only_20 ===
  avg_response_length: 1536
  correct: 103
  eos_rate: 0.27
  eval_time: 4h00m04s
  gsm8k_accuracy: 0.515
  gsm8k_accuracy_ci: 0.0353
  total: 200
  truncated: 146
=== eval_gsm8k_sft_qwen_standard_20 ===
  correct: 42
  gsm8k_accuracy: 0.21
  total: 200
=== eval_gsm8k_sft_random_20 ===
  avg_response_length: 182.4
  correct: 676
  eos_rate: 0.9932
  gsm8k_accuracy: 0.5125
  n_total: 1319
  stderr: 0.0138
=== eval_gsm8k_sft_rasp_20 ===
  avg_response_length: 216.5
  correct: 811
  eos_rate: 0.9826
  gsm8k_accuracy: 0.6149
  gsm8k_accuracy_ci: 0.0134
  total: 1319
=== eval_gsm8k_sft_rasp_20_1p5b ===
  accuracy: 0.2691
  grpo_delta_pp: -0.75
  n_correct: 355
  n_total: 1319
  stderr: 0.0122
=== eval_gsm8k_sft_shortgpt_20 ===
  gsm8k_accuracy: 44.73
  n_correct: 590
  n_total: 1319
=== eval_gsm8k_sft_standard_15 ===
  avg_response_length: 183
  correct: 877
  eos_rate: 0.993
  gsm8k_accuracy: 0.6649
  total: 1319
=== eval_gsm8k_sft_standard_20 ===
  avg_response_length: 206.68
  correct: 781
  eos_rate: 0.9848
  gsm8k_accuracy: 0.5921
  stderr: 0.0135
  total: 1319
=== eval_gsm8k_sft_standard_20_1p5b ===
  accuracy: 0.22896133434420016
  n_correct: 302
  n_total: 1319
=== eval_gsm8k_sft_standard_25 ===
  avg_response_length: 333.15
  correct: 671
  eos_rate: 0.953
  gsm8k_accuracy: 0.5087
  n_total: 1319
  stderr: 0.0138
=== eval_humaneval_grpo_cka_only_20_1p5b_2048 ===
  correct: 0
  pass_at_1: 0
  stderr: 0
  total: 164
=== eval_humaneval_grpo_cka_only_20_2048 ===
  avg_response_length: 1523.31
  median_response_length: 2048
  n_correct: 33
  n_total: 164
  pass_at_1: 0.2012
  stderr: 0.0313
  wall_clock_seconds: 11933
=== eval_humaneval_grpo_rasp_20 ===
  n_passed: 17
  n_total: 164
  pass_at_1: 0.1037
  stderr: 0.0238
=== eval_humaneval_grpo_rasp_20_2048 ===
  correct: 24
  max_new_tokens: 2048
  pass_at_1: 0.1463
  stderr: 0.0276
  total: 164
=== eval_humaneval_grpo_rasp_20_fair_2048 ===
  n_correct: 18
  n_total: 164
  pass_at_1: 0.1098
  stderr: 0.0244
=== eval_humaneval_grpo_standard_20 ===
  correct: 3
  max_new_tokens: 512
  note: 512-token truncation, low quality
  pass_at_1: 0.0183
  total: 164
=== eval_humaneval_grpo_standard_20_2048 ===
  avg_response_length: 1843
  correct: 17
  max_new_tokens: 2048
  median_response_length: 2048
  pass_at_1: 0.1037
  total: 164
=== eval_humaneval_grpo_standard_20_fair_2048_v3 ===
  n_correct: 18
  n_total: 164
  pass_at_1: 0.1098
=== eval_humaneval_sft_cka_only_20_1p5b_2048 ===
  correct: 1
  pass_at_1: 0.0061
  stderr: 0.0061
  total: 164
=== eval_humaneval_sft_cka_only_20_2048_v2 ===
  n_correct: 33
  n_total: 164
  pass_at_1: 20.12
=== eval_humaneval_sft_rasp_20 ===
  correct: 12
  failure_modes: model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch
  median_response_length: 512
  note: max_tokens truncation frequent
  pass_at_1: 0.0732
  stderr: 0.0203
  total: 164
=== eval_humaneval_sft_rasp_20_1p5b_2048 ===
  n_correct: 0
  n_total: 164
  note: 1.5B SFT RASP, all truncated at 2048 tokens
  pass_at_1: 0
=== eval_humaneval_sft_rasp_20_2048 ===
  correct: 17
  max_new_tokens: 2048
  median_response_length: 2048
  note: still truncating at median=2048, main failure mode is thinking chain leaking into code output
  pass_at_1: 0.1037
  stderr: 0.0238
  total: 164
  wall_time_min: 42
=== eval_humaneval_sft_rasp_20_2048_v2 ===
  avg_response_length: 1253.7
  median_response_length: 2048
  n_correct: 17
  n_total: 164
  pass_at_1: 0.1037
  stderr: 0.0238
=== eval_humaneval_sft_standard_20 ===
  correct: 5
  failure_modes: model generates CoT natural language instead of code, all responses truncated at max_tokens=512
  pass_at_1: 0.0305
  stderr: 0.0134
  total: 164
  wall_time_min: 17
=== eval_humaneval_sft_standard_20_1p5b_2048 ===
  correct: 1
  pass_at_1: 0.0061
  stderr: 0.0061
  total: 164
=== eval_humaneval_sft_standard_20_2048_v2 ===
  avg_response_length: 1850.7
  correct: 19
  max_new_tokens: 2048
  median_response_length: 2048
  pass_at_1: 0.1159
  total: 164
=== eval_humaneval_sft_standard_20_2048_v3 ===
  correct: 22
  pass_at_1: 0.1341
  stderr: 0.0266
  total: 164
=== eval_humaneval_sft_standard_25 ===
  n_passed: 3
  n_total: 164
  pass_at_1: 0.0183
  stderr: 0.0105
=== eval_humaneval_unpruned ===
  n_passed: 3
  n_total: 164
  pass_at_1: 0.0183
  stderr: 0.0105
=== eval_humaneval_unpruned_2048 ===
  avg_response_length: 1771
  correct: 74
  max_new_tokens: 2048
  median_response_length: 2048
  pass_at_1: 0.4512
  stderr: 0.0389
  total: 164
  wall_time_min: 67.6
=== eval_math500_dense_2048 ===
  accuracy: 0.53
  avg_response_length: 1724.5
  median_response_length: 2048
  n_correct: 265
  n_total: 500
  natural_eos_pct: 0.468
  stderr: 0.0223
  truncated_pct: 0.532
=== eval_math500_dense_unpruned ===
  accuracy: 0.736
  n_correct: 368
  n_total: 500
  natural_eos_pct: 0.752
  stderr: 0.0197
=== eval_math500_grpo_cka_only_20 ===
  accuracy: 0.266
  avg_response_length: 1124.24
  n_correct: 133
  n_total: 500
  stderr: 0.0198
  truncated: 108
  truncation_rate: 0.216
=== eval_math500_grpo_cka_only_20_2048 ===
  accuracy: 0.292
  n_correct: 146
  n_total: 500
=== eval_math500_grpo_cka_only_20_2048_v2 ===
  accuracy: 0.274
  avg_response_length: 654.746
  correct: 137
  natural_eos: 390
  stderr: 0.01995
  total: 500
  truncated: 110
=== eval_math500_grpo_cka_only_20_fixed ===
  accuracy: 0.276
  n_correct: 138
  n_total: 500
  stderr: 0.02
=== eval_math500_grpo_cka_only_25_fixed ===
  accuracy: 0.176
  avg_response_length: 719.35
  n_correct: 88
  n_total: 500
  natural_eos: 367
  stderr: 0.017
  truncated: 133
  truncated_pct: 0.266
=== eval_math500_grpo_cka_only_25_v2 ===
  correct: 92
  math500_accuracy: 0.184
  math500_stderr: 0.0173
  n_total: 500
=== eval_math500_grpo_random_20_v3 ===
  accuracy: 0.134
  avg_response_length: 1479.2
  correct: 67
  natural_eos: 167
  stderr: 0.0152
  total: 500
  truncated: 333
=== eval_math500_grpo_rasp_20_fair ===
  accuracy: 0.24
  avg_response_length: 903.5
  max_new_tokens: 2048
  median_response_length: 272
  n_correct: 120
  n_total: 500
  natural_eos_pct: 0.64
  stderr: 0.0191
  truncated_pct: 0.36
=== eval_math500_grpo_rasp_alpha0p5_20 ===
  accuracy: 0.248
  avg_response_length: 1110.462
  correct: 124
  natural_eos: 274
  stderr: 0.0193
  total: 500
  truncated: 226
=== eval_math500_grpo_rasp_alpha1p0_20 ===
  accuracy: 0.226
  avg_response_length: 903.536
  n_correct: 113
  n_total: 500
  natural_eos: 320
  stderr: 0.0187
  truncated: 180
=== eval_math500_grpo_rasp_alpha1p0_20_fixed ===
  accuracy: 0.23
  avg_response_length: 903.536
  n_correct: 115
  n_total: 500
  natural_eos: 320
  stderr: 0.0188
  truncated: 180
=== eval_math500_grpo_rasp_alpha2p0_20 ===
  accuracy: 0.262
  avg_response_length: 785.326
  correct: 131
  natural_eos: 349
  stderr: 0.0197
  total: 500
  truncated: 151
=== eval_math500_grpo_rasp_alpha2p0_20_fixed ===
  accuracy: 0.274
  n_correct: 137
  n_total: 500
  natural_eos: 349
  truncated: 151
  truncated_pct: 0.302
=== eval_math500_grpo_rasp_alpha3p0_20 ===
  accuracy: 0.228
  avg_response_length: 745.038
  correct: 114
  stderr: 0.0188
  total: 500
  truncated_ratio: 0.28
=== eval_math500_grpo_rasp_alpha4p0_20 ===
  accuracy: 0.262
  avg_response_length: 925.48
  correct: 131
  natural_eos: 320
  stderr: 0.01966
  total: 500
  truncated: 180
=== eval_math500_grpo_standard_20_fair_2048_v2 ===
  math500_accuracy: 0.264
  math500_correct: 132
  math500_stderr: 0.0197
  math500_total: 500
=== eval_math500_grpo_standard_20_fair_v2 ===
  accuracy: 0.264
  n_correct: 132
  n_total: 500
  stderr: 0.0197
=== eval_math500_grpo_standard_20_fixed ===
  avg_response_length: 1127.844
  math500_acc: 0.27
  math500_correct: 135
  math500_stderr: 0.0199
  math500_total: 500
  natural_eos: 278
  truncated: 222
=== eval_math500_sft_cka_only_20_fixed_v2 ===
  accuracy: 0.274
  num_correct: 137
  num_total: 500
  stderr: 0.02
  truncated_pct: 0.232
=== eval_math500_sft_cka_only_20_v4_restart ===
  accuracy: 0.29
  avg_response_length: 673.278
  median_response_length: 242.5
  n_correct: 145
  n_total: 500
  natural_eos: 384
  natural_eos_pct: 0.768
  stderr: 0.0203
  truncated: 116
=== eval_math500_sft_cka_only_20_westd ===
  accuracy: 0.268
  avg_response_length: 673.278
  correct: 134
  natural_eos_pct: 0.768
  stderr: 0.0198
  total: 500
  truncated: 116
=== eval_math500_sft_cka_only_25_v2 ===
  correct: 96
  math500_accuracy: 0.192
  n_total: 500
  std_err: 0.0176
=== eval_math500_sft_qwen_math_cka_only_20 ===
  accuracy: 0.216
  avg_response_length: 1745.338
  correct: 108
  natural_eos: 90
  stderr: 0.0184
  total: 500
  truncated: 410
=== eval_math500_sft_random_20_v3 ===
  accuracy: 0.144
  avg_response_length: 1470.44
  correct: 72
  natural_eos: 171
  stderr: 0.0157
  total: 500
  truncated: 329
=== eval_math500_sft_rasp_20 ===
  correct: 121
  math500_acc: 0.242
  stderr: 0.0192
  total: 500
  wall_time_hours: 2.94
=== eval_math500_sft_rasp_20_2048 ===
  accuracy: 0.226
  avg_response_length: 930.58
  median_response_length: 274
  n_correct: 113
  n_total: 500
  natural_eos: 314
  natural_eos_pct: 0.628
  stderr: 0.0187
  truncated: 186
=== eval_math500_sft_rasp_alpha0p5_20 ===
  accuracy: 0.254
  correct: 127
  stderr: 0.0195
  total: 500
  truncated: 220
=== eval_math500_sft_rasp_alpha1p0_20_fixed ===
  accuracy: 0.216
  num_correct: 108
  num_total: 500
=== eval_math500_sft_rasp_alpha1p0_20_v2 ===
  accuracy: 0.212
  correct: 106
  stderr: 0.0183
  total: 500
  truncated: 186
=== eval_math500_sft_rasp_alpha2p0_20 ===
  accuracy: 0.24
  correct: 120
  stderr: 0.0191
  total: 500
  truncated: 155
=== eval_math500_sft_rasp_alpha2p0_20_fixed ===
  accuracy: 0.256
  avg_response_length: 805.754
  n_correct: 128
  n_total: 500
  natural_eos: 345
  stderr: 0.01952
  truncated: 155
  truncated_pct: 0.31
=== eval_math500_sft_rasp_alpha3p0_20 ===
  accuracy: 0.232
  correct: 116
  stderr: 0.0189
  total: 500
  truncated: 144
=== eval_math500_sft_rasp_alpha4p0_20 ===
  accuracy: 0.266
  correct: 133
  stderr: 0.0198
  total: 500
  truncated: 190
=== eval_math500_sft_standard_20 ===
  correct: 130
  eos_rate: 0.578
  math500_acc: 0.26
  stderr: 0.0196
  total: 500
  truncated: 211
  wall_time_hours: 3.58
=== eval_math500_sft_standard_20_1p5b ===
  correct: 27
  math500_accuracy: 0.054
  total: 500
  truncated: 335
=== eval_math500_sft_standard_20_2048_v2 ===
  accuracy: 0.258
  n_correct: 129
  n_total: 500
=== eval_math500_sft_standard_20_2048_v3 ===
  math500_accuracy: 0.234
  math500_correct: 117
  math500_total: 500
=== eval_math500_sft_standard_25 ===
  avg_response_length: 1367.82
  correct: 70
  math500_accuracy: 0.14
  n_total: 500
  natural_eos: 185
  truncated: 315
  v1_accuracy: 0.13
  v1_correct: 65
=== eval_math500_unpruned ===
  N: 500
  accuracy: 0.736
  correct: 368
  stderr: 0.02
=== eval_mbpp_dense_unpruned ===
  n_correct: 200
  n_total: 374
  pass_at_1: 0.5348
  stderr: 0.0258
=== eval_mbpp_grpo_cka_only_20 ===
  n_correct: 53
  n_total: 374
  pass_at_1: 0.1417
  stderr: 0.018
=== eval_mbpp_grpo_rasp_20 ===
  n_correct: 49
  n_total: 374
  pass_at_1: 0.131
  stderr: 0.0174
=== eval_mbpp_grpo_shortgpt_20_v2 ===
  avg_response_length: 1140.8
  median_response_length: 804.5
  n_correct: 54
  n_total: 374
  pass_at_1: 0.1444
  stderr: 0.0182
=== eval_mbpp_grpo_standard_20_v3 ===
  correct: 49
  pass_at_1: 0.131
  stderr: 0.0174
  total: 374
=== eval_mbpp_grpo_standard_20_v4 ===
  avg_response_length: 1058.7
  median_response_length: 726
  n_correct: 49
  n_total: 374
  pass_at_1: 0.131
  stderr: 0.01745
=== eval_mbpp_sft_cka_only_20 ===
  avg_response_length: 643.8
  degradation_pct: 76.01
  dense_baseline_pass_at_1: 0.5348
  median_response_length: 363.5
  n_correct: 48
  n_total: 374
  pass_at_1: 0.1283
  stderr: 0.0173
=== eval_mbpp_sft_rasp_20 ===
  avg_response_length: 810.7
  degradation_pct: 78.01
  dense_baseline_pass_at_1: 0.5348
  median_response_length: 247
  n_correct: 44
  n_total: 374
  pass_at_1: 0.1176
  stderr: 0.0167
=== eval_mbpp_sft_shortgpt_20_v2 ===
  avg_response_length: 1166.4
  median_response_length: 773.5
  n_correct: 39
  n_total: 374
  pass_at_1: 0.1043
  stderr: 0.0158
=== eval_mbpp_sft_standard_20_1p5b ===
  avg_response_length: 1658.6
  median_response_length: 2048
  n_correct: 3
  n_total: 374
  pass_at_1: 0.008021
  stderr: 0.004613
=== eval_mbpp_sft_standard_20_v4 ===
  avg_response_length: 1084.1
  median_response_length: 746.5
  n_correct: 45
  n_total: 374
  pass_at_1: 0.1203
  stderr: 0.0168
=== eval_pass_k8_rasp_20_grpo_deepseek ===
  n_problems: 200
  pass_k8: 0.89
  temperature: 0.7
=== eval_pass_k8_rasp_20_grpo_qwen_math ===
  accuracy: 0.915
  k: 8
  n_samples: 200
  pass_at_k: 0.915
  stderr: 0.0197
  temperature: 0.7
=== eval_pass_k8_rasp_20_sft_qwen_math ===
  avg_response_length: 139.86
  eos_rate: 0.99625
  k: 8
  n_problems: 200
  natural_eos: 1594
  pass_at_k: 0.935
  stderr: 0.0174
  temperature: 0.7
  truncated: 6
=== eval_pass_k8_unpruned_qwen_math ===
  accuracy: 0.965
  k: 8
  n_samples: 200
  pass_at_k: 0.965
  stderr: 0.013
  temperature: 0.7
=== eval_postprune_qwen_math_cka_only_20 ===
  accuracy: 0.01
  avg_response_length: 958.3
  eos_rate: 0.065
  n_correct: 2
  n_total: 200
  note: Qwen-Math CKA-only 20% post-prune = 1.0%. Severe collapse (repetition, gibberish).
  stderr: 0.00704
=== eval_postprune_qwen_math_standard_20 ===
  accuracy: 0.185
  avg_response_length: 506.83
  eos_rate: 0.69
  n_correct: 37
  n_total: 200
  stderr: 0.02746
=== eval_postprune_rasp_25 ===
  accuracy: 21
  avg_response_length: 2032.9
  correct: 21
  eos_rate: 56
  natural_eos: 56
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "574a8cb2-e5f4-4c7e-879e-c016469e132e",
  "tool_use_result": {
    "stdout": "=== alpha_ablation_sweep ===\n  alpha_0.0.accuracy: 0.27\n  alpha_0.0.avg_len: 1192\n  alpha_0.0.eos_rate: 0.8\n  alpha_0.0.n_correct: 27\n  alpha_0.0.n_total: 100\n  alpha_0.25.accuracy: 0.23\n  alpha_0.25.avg_len: 1834\n  alpha_0.25.eos_rate: 0.63\n  alpha_0.25.n_correct: 23\n  alpha_0.25.n_total: 100\n  alpha_0.5.accuracy: 0.22\n  alpha_0.5.avg_len: 1141\n  alpha_0.5.eos_rate: 0.81\n  alpha_0.5.n_correct: 22\n  alpha_0.5.n_total: 100\n  alpha_1.0.accuracy: 0.31\n  alpha_1.0.avg_len: 733\n  alpha_1.0.eos_rate: 0.92\n  alpha_1.0.n_correct: 31\n  alpha_1.0.n_total: 100\n  alpha_2.0.accuracy: 0.36\n  alpha_2.0.avg_len: 2130\n  alpha_2.0.eos_rate: 0.59\n  alpha_2.0.n_correct: 36\n  alpha_2.0.n_total: 100\n=== cka_calibration_stability_ablation ===\n  n_splits: 5\n  size_sensitivity_128: 0.982\n  size_sensitivity_256: 0.989\n  size_sensitivity_512: 0.995\n  split_half_rho: 0.9932\n=== cka_scoring_stability_ablation ===\n  mean_combined_rho: 0.979\n  min_combined_rho: 0.964\n  spearman_256v1024_attn: 0.9762\n  spearman_256v1024_combined: 0.9641\n  spearman_256v1024_mlp: 0.9464\n  spearman_256v512_attn: 0.989\n  spearman_256v512_combined: 0.9788\n  spearman_256v512_mlp: 0.9683\n  spearman_512v1024_attn: 0.995\n  spearman_512v1024_combined: 0.9938\n  spearman_512v1024_mlp: 0.9908\n  stable: True\n=== eval-sft-alpha-0p0 ===\n  accuracy: 0.64\n  avg_len: 257.9\n  eos_rate: 0.97\n  n_correct: 64\n  n_total: 100\n=== eval-sft-alpha-1p0 ===\n  accuracy: 0.57\n  avg_len: 224.18\n  eos_rate: 0.98\n  n_correct: 57\n  n_total: 100\n  natural_eos: 98\n  stderr: 0.0495\n  truncated: 2\n=== eval_gradient_postsft ===\n  accuracy: 0.615\n  avg_response_length: 167.455\n  correct: 123\n  eos_rate: 0.995\n  stderr: 0.0344\n  total: 200\n=== eval_grpo_rasp_20_qwen_math ===\n  accuracy: 0.725\n  n_samples: 200\n  seed: 42\n=== eval_grpo_rasp_25 ===\n  accuracy: 0.5315\n  avg_len: 433.85\n  eos_rate: 0.9272\n  max_len: 4096\n  min_len: 39\n  n_correct: 701\n  n_total: 1319\n  stderr: 0.0137\n  truncated: 96\n=== eval_grpo_rasp_25_qwen_math ===\n  accuracy: 0.625\n  n_samples: 200\n  seed: 42\n=== eval_grpo_rasp_rlvr_20_qwen_math ===\n  accuracy: 0.71\n  mode: greedy\n  n_samples: 200\n  seed: 42\n=== eval_grpo_rasp_v9_step10 ===\n  accuracy: 61.87\n  avg_response_length: 213.6\n  correct: 816\n  eos_rate: 98.33\n  seed: 42\n  stderr: 1.34\n  total: 1319\n  truncated: 22\n=== eval_grpo_rasp_v9_step5 ===\n  accuracy: 60.65\n  seed: 42\n  total: 1319\n=== eval_grpo_standard_20_qwen_math ===\n  accuracy: 0.705\n  n_samples: 200\n  seed: 42\n=== eval_grpo_standard_25 ===\n  accuracy: 0.511\n  avg_len: 292.86\n  eos_rate: 0.9628\n  n_correct: 674\n  n_total: 1319\n  stderr: 0.01376\n=== eval_grpo_standard_25_qwen_math ===\n  accuracy: 0.635\n  n_samples: 200\n  seed: 42\n=== eval_grpo_unpruned_v2_step100 ===\n  accuracy: 81.27\n  avg_response_length: 209\n  correct: 1072\n  eos_rate: 99.7\n  seed: 42\n  total: 1319\n=== eval_grpo_unpruned_v2_step90 ===\n  accuracy: 80.59\n  avg_response_length: 213\n  correct: 1063\n  eos_rate: 99.6\n  seed: 42\n  total: 1319\n=== eval_gsm8k_dense_unpruned ===\n  avg_response_length: 594\n  correct: 1198\n  eos_rate: 0.9871\n  eval_time: 3h7m\n  gsm8k_accuracy: 0.9083\n  gsm8k_accuracy_ci: 0.0079\n  total: 1319\n  truncated: 17\n=== eval_gsm8k_grpo_alpha0p5_20 ===\n  gsm8k_accuracy: 0.6118\n  gsm8k_correct: 807\n  gsm8k_total: 1319\n=== eval_gsm8k_grpo_alpha2p0_20 ===\n  gsm8k_accuracy: 0.6611\n  gsm8k_correct: 872\n  gsm8k_total: 1319\n=== eval_gsm8k_grpo_alpha3p0_20 ===\n  avg_response_length: 219.7\n  correct: 837\n  eos_rate: 0.9864\n  gsm8k_accuracy: 0.6345\n  stderr: 0.0133\n  total: 1319\n  truncated: 18\n=== eval_gsm8k_grpo_alpha4_20_v3 ===\n  avg_response_length: 188.16\n  eos_rate: 0.9856\n  gsm8k_accuracy: 0.6277\n  gsm8k_accuracy_ci: 0.0133\n  gsm8k_correct: 828\n  gsm8k_total: 1319\n  natural_eos: 1300\n  truncated: 19\n=== eval_gsm8k_grpo_cka_only_15_seed123 ===\n  accuracy: 73.09\n  eos_rate: 98.79\n  n_correct: 964\n  n_total: 1319\n  stderr: 1.22\n  truncated: 16\n=== eval_gsm8k_grpo_cka_only_15_seed456 ===\n  accuracy: 0.721\n  avg_response_length: 201.94\n  eos_rate: 0.9894\n  n_correct: 951\n  n_total: 1319\n  stderr: 0.0123\n=== eval_gsm8k_grpo_cka_only_15_v2 ===\n  avg_response_length: 202.4\n  correct: 964\n  eos_rate: 0.9894\n  gsm8k_accuracy: 0.7309\n  gsm8k_accuracy_ci: 0.0122\n  total: 1319\n=== eval_gsm8k_grpo_cka_only_20_1p5b ===\n  accuracy: 0.3548\n  n_correct: 468\n  n_total: 1319\n  stderr: 0.0132\n=== eval_gsm8k_grpo_cka_only_20_seed123 ===\n  accuracy: 0.6422\n  avg_response_length: 195.97\n  eos_rate: 0.9909\n  n_correct: 847\n  n_total: 1319\n  natural_eos: 1307\n  stderr: 0.0132\n  truncated: 12\n=== eval_gsm8k_grpo_cka_only_20_seed456_full ===\n  avg_response_length: 204.3\n  correct: 852\n  eos_rate: 0.9886\n  gsm8k_accuracy: 0.6459\n  gsm8k_accuracy_ci: 0.0132\n  total: 1319\n=== eval_gsm8k_grpo_cka_only_20_v2 ===\n  accuracy: 0.6437\n  avg_response_length: 203.43\n  eos_rate: 0.9886\n  n_correct: 849\n  n_total: 1319\n  stderr: 0.0132\n  truncated: 15\n  wall_time_sec: 8921\n=== eval_gsm8k_grpo_cka_only_20_verify ===\n  accuracy: 0.6406\n  accuracy_diff_pp: -0.31\n  avg_response_length: 201.76\n  eos_rate: 0.9894\n  n_correct: 845\n  n_total: 1319\n  original_accuracy: 0.6437\n  stderr: 0.0132\n=== eval_gsm8k_grpo_cka_only_25_v3 ===\n  correct: 786\n  eos_rate: 0.9818\n  gsm8k_accuracy: 0.5959\n  n_total: 1319\n=== eval_gsm8k_grpo_depth_first_20 ===\n  accuracy_approx: 0.08\n  early_stopped: True\n  result_file_on_westb: False\n=== eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v3 ===\n  accuracy: 0.486\n  avg_response_length: 1766.5\n  correct: 243\n  natural_eos_pct: 0.162\n  stderr: 0.0224\n  total: 500\n  truncated_pct: 0.838\n=== eval_gsm8k_grpo_random_20_seed123_v2 ===\n  accuracy: 0.5072\n  avg_response_length: 177.9\n  eos_rate: 0.9939\n  n_correct: 669\n  n_total: 1319\n  stderr: 0.01377\n=== eval_gsm8k_grpo_random_20_seed456 ===\n  avg_response_length: 163.5\n  eos_rate: 0.9954\n  gsm8k_accuracy: 0.5087\n  gsm8k_accuracy_se: 0.0138\n  gsm8k_correct: 671\n  gsm8k_total: 1319\n  truncated: 6\n=== eval_gsm8k_grpo_random_20_v2 ===\n  avg_response_length: 173\n  correct: 667\n  eos_rate: 0.9954\n  gsm8k_accuracy: 0.5057\n  gsm8k_stderr: 0.0138\n  total: 1319\n=== eval_gsm8k_grpo_rasp_20_1p5b ===\n  accuracy: 0.2616\n  avg_response_length: 392.7\n  eos_rate: 0.9378\n  n_correct: 345\n  n_total: 1319\n  stderr: 0.0121\n=== eval_gsm8k_grpo_rasp_20_fair ===\n  accuracy: 0.6088\n  avg_response_length: 195.7\n  eos_rate: 0.9879\n  n_correct: 803\n  n_total: 1319\n  stderr: 0.0134\n=== eval_gsm8k_grpo_shortgpt_20 ===\n  gsm8k_accuracy: 43.37\n  n_correct: 572\n  n_total: 1319\n  stderr: 0.0136\n=== eval_gsm8k_grpo_standard_15_seed123_v3 ===\n  accuracy: 0.6513\n  accuracy_se: 0.0131\n  avg_response_length: 183.25\n  eos_rate: 0.9932\n  n_correct: 859\n  n_total: 1319\n=== eval_gsm8k_grpo_standard_15_seed456_v3 ===\n  avg_response_length: 180.23\n  eos_rate: 0.9939\n  gsm8k_accuracy: 0.6543\n  gsm8k_stderr: 0.0131\n  n_correct: 863\n  n_total: 1319\n=== eval_gsm8k_grpo_standard_15_v2 ===\n  avg_response_length: 184\n  correct: 872\n  eos_rate: 0.993\n  gsm8k_accuracy: 0.6611\n  total: 1319\n=== eval_gsm8k_grpo_standard_20_1p5b ===\n  accuracy: 0.2229\n  n_correct: 294\n  n_total: 1319\n  stderr: 0.0115\n=== eval_gsm8k_grpo_standard_20_fair_v2 ===\n  accuracy: 59.44\n  n_correct: 784\n  n_total: 1319\n=== eval_gsm8k_grpo_standard_20_seed123 ===\n  accuracy: 0.64\n  avg_response_length: 187.9\n  eos_rate: 0.99\n  n_correct: 128\n  n_total: 200\n  stderr: 0.0339\n=== eval_gsm8k_grpo_standard_20_seed123_full ===\n  accuracy: 0.5989\n  n_correct: 790\n  n_total: 1319\n  stderr: 0.0135\n=== eval_gsm8k_grpo_standard_20_seed456 ===\n  accuracy: 0.665\n  avg_response_length: 166.9\n  eos_rate: 0.995\n  n_correct: 133\n  n_total: 200\n  stderr: 0.0334\n=== eval_gsm8k_grpo_standard_20_seed456_full ===\n  accuracy: 0.602\n  eos_rate: 0.9856\n  n_correct: 794\n  n_total: 1319\n  stderr: 0.01348\n=== eval_gsm8k_grpo_standard_25 ===\n  avg_response_length: 314.47\n  correct: 684\n  eos_rate: 0.9575\n  gsm8k_accuracy: 0.5186\n  n_total: 1319\n  stderr: 0.0138\n=== eval_gsm8k_grpo_unstructured_20 ===\n  accuracy: 0.8764\n  avg_response_length: 600\n  eos_rate: 0.9818\n  n_correct: 1156\n  n_total: 1319\n  stderr: 0.00906\n  truncated: 24\n=== eval_gsm8k_sft_alpha0p5_20 ===\n  gsm8k_accuracy: 0.6073\n  gsm8k_correct: 801\n  gsm8k_total: 1319\n=== eval_gsm8k_sft_alpha2p0_20 ===\n  gsm8k_accuracy: 0.6497\n  gsm8k_correct: 857\n  gsm8k_total: 1319\n=== eval_gsm8k_sft_alpha3p0_20 ===\n  avg_response_length: 188.63\n  eos_rate: 0.9879\n  gsm8k_accuracy: 0.6414\n  gsm8k_correct: 846\n  gsm8k_stderr: 0.0132\n  gsm8k_total: 1319\n  natural_eos: 1303\n  truncated: 16\n=== eval_gsm8k_sft_alpha4_20_v5 ===\n  avg_response_length: 197.85\n  correct: 817\n  eos_rate: 0.981\n  gsm8k_accuracy: 0.6194\n  stderr: 0.0134\n  total: 1319\n=== eval_gsm8k_sft_cka_only_15 ===\n  correct: 952\n  gsm8k_accuracy: 0.7218\n  total: 1319\n=== eval_gsm8k_sft_cka_only_20 ===\n  avg_response_length: 198.1\n  correct: 843\n  eos_rate: 0.9901\n  gsm8k_accuracy: 0.6391\n  gsm8k_accuracy_ci: 0.0132\n  total: 1319\n  truncated: 13\n=== eval_gsm8k_sft_cka_only_20_1p5b ===\n  accuracy: 0.3563\n  avg_response_length: 336.76\n  eos_rate: 0.9507\n  n_correct: 470\n  n_total: 1319\n  stderr: 0.0132\n=== eval_gsm8k_sft_cka_only_25 ===\n  avg_response_length: 243.6\n  correct: 793\n  eos_rate: 0.9803\n  gsm8k_accuracy: 0.6012\n  n_total: 1319\n  stderr: 0.0135\n=== eval_gsm8k_sft_depth_first_20 ===\n  accuracy_approx: 0.1\n  early_stopped: True\n  result_file_on_westb: False\n=== eval_gsm8k_sft_qwen_cka_only_20 ===\n  avg_response_length: 1536\n  correct: 103\n  eos_rate: 0.27\n  eval_time: 4h00m04s\n  gsm8k_accuracy: 0.515\n  gsm8k_accuracy_ci: 0.0353\n  total: 200\n  truncated: 146\n=== eval_gsm8k_sft_qwen_standard_20 ===\n  correct: 42\n  gsm8k_accuracy: 0.21\n  total: 200\n=== eval_gsm8k_sft_random_20 ===\n  avg_response_length: 182.4\n  correct: 676\n  eos_rate: 0.9932\n  gsm8k_accuracy: 0.5125\n  n_total: 1319\n  stderr: 0.0138\n=== eval_gsm8k_sft_rasp_20 ===\n  avg_response_length: 216.5\n  correct: 811\n  eos_rate: 0.9826\n  gsm8k_accuracy: 0.6149\n  gsm8k_accuracy_ci: 0.0134\n  total: 1319\n=== eval_gsm8k_sft_rasp_20_1p5b ===\n  accuracy: 0.2691\n  grpo_delta_pp: -0.75\n  n_correct: 355\n  n_total: 1319\n  stderr: 0.0122\n=== eval_gsm8k_sft_shortgpt_20 ===\n  gsm8k_accuracy: 44.73\n  n_correct: 590\n  n_total: 1319\n=== eval_gsm8k_sft_standard_15 ===\n  avg_response_length: 183\n  correct: 877\n  eos_rate: 0.993\n  gsm8k_accuracy: 0.6649\n  total: 1319\n=== eval_gsm8k_sft_standard_20 ===\n  avg_response_length: 206.68\n  correct: 781\n  eos_rate: 0.9848\n  gsm8k_accuracy: 0.5921\n  stderr: 0.0135\n  total: 1319\n=== eval_gsm8k_sft_standard_20_1p5b ===\n  accuracy: 0.22896133434420016\n  n_correct: 302\n  n_total: 1319\n=== eval_gsm8k_sft_standard_25 ===\n  avg_response_length: 333.15\n  correct: 671\n  eos_rate: 0.953\n  gsm8k_accuracy: 0.5087\n  n_total: 1319\n  stderr: 0.0138\n=== eval_humaneval_grpo_cka_only_20_1p5b_2048 ===\n  correct: 0\n  pass_at_1: 0\n  stderr: 0\n  total: 164\n=== eval_humaneval_grpo_cka_only_20_2048 ===\n  avg_response_length: 1523.31\n  median_response_length: 2048\n  n_correct: 33\n  n_total: 164\n  pass_at_1: 0.2012\n  stderr: 0.0313\n  wall_clock_seconds: 11933\n=== eval_humaneval_grpo_rasp_20 ===\n  n_passed: 17\n  n_total: 164\n  pass_at_1: 0.1037\n  stderr: 0.0238\n=== eval_humaneval_grpo_rasp_20_2048 ===\n  correct: 24\n  max_new_tokens: 2048\n  pass_at_1: 0.1463\n  stderr: 0.0276\n  total: 164\n=== eval_humaneval_grpo_rasp_20_fair_2048 ===\n  n_correct: 18\n  n_total: 164\n  pass_at_1: 0.1098\n  stderr: 0.0244\n=== eval_humaneval_grpo_standard_20 ===\n  correct: 3\n  max_new_tokens: 512\n  note: 512-token truncation, low quality\n  pass_at_1: 0.0183\n  total: 164\n=== eval_humaneval_grpo_standard_20_2048 ===\n  avg_response_length: 1843\n  correct: 17\n  max_new_tokens: 2048\n  median_response_length: 2048\n  pass_at_1: 0.1037\n  total: 164\n=== eval_humaneval_grpo_standard_20_fair_2048_v3 ===\n  n_correct: 18\n  n_total: 164\n  pass_at_1: 0.1098\n=== eval_humaneval_sft_cka_only_20_1p5b_2048 ===\n  correct: 1\n  pass_at_1: 0.0061\n  stderr: 0.0061\n  total: 164\n=== eval_humaneval_sft_cka_only_20_2048_v2 ===\n  n_correct: 33\n  n_total: 164\n  pass_at_1: 20.12\n=== eval_humaneval_sft_rasp_20 ===\n  correct: 12\n  failure_modes: model outputs natural language thinking instead of code (SyntaxError), parenthesis mismatch\n  median_response_length: 512\n  note: max_tokens truncation frequent\n  pass_at_1: 0.0732\n  stderr: 0.0203\n  total: 164\n=== eval_humaneval_sft_rasp_20_1p5b_2048 ===\n  n_correct: 0\n  n_total: 164\n  note: 1.5B SFT RASP, all truncated at 2048 tokens\n  pass_at_1: 0\n=== eval_humaneval_sft_rasp_20_2048 ===\n  correct: 17\n  max_new_tokens: 2048\n  median_response_length: 2048\n  note: still truncating at median=2048, main failure mode is thinking chain leaking into code output\n  pass_at_1: 0.1037\n  stderr: 0.0238\n  total: 164\n  wall_time_min: 42\n=== eval_humaneval_sft_rasp_20_2048_v2 ===\n  avg_response_length: 1253.7\n  median_response_length: 2048\n  n_correct: 17\n  n_total: 164\n  pass_at_1: 0.1037\n  stderr: 0.0238\n=== eval_humaneval_sft_standard_20 ===\n  correct: 5\n  failure_modes: model generates CoT natural language instead of code, all responses truncated at max_tokens=512\n  pass_at_1: 0.0305\n  stderr: 0.0134\n  total: 164\n  wall_time_min: 17\n=== eval_humaneval_sft_standard_20_1p5b_2048 ===\n  correct: 1\n  pass_at_1: 0.0061\n  stderr: 0.0061\n  total: 164\n=== eval_humaneval_sft_standard_20_2048_v2 ===\n  avg_response_length: 1850.7\n  correct: 19\n  max_new_tokens: 2048\n  median_response_length: 2048\n  pass_at_1: 0.1159\n  total: 164\n=== eval_humaneval_sft_standard_20_2048_v3 ===\n  correct: 22\n  pass_at_1: 0.1341\n  stderr: 0.0266\n  total: 164\n=== eval_humaneval_sft_standard_25 ===\n  n_passed: 3\n  n_total: 164\n  pass_at_1: 0.0183\n  stderr: 0.0105\n=== eval_humaneval_unpruned ===\n  n_passed: 3\n  n_total: 164\n  pass_at_1: 0.0183\n  stderr: 0.0105\n=== eval_humaneval_unpruned_2048 ===\n  avg_response_length: 1771\n  correct: 74\n  max_new_tokens: 2048\n  median_response_length: 2048\n  pass_at_1: 0.4512\n  stderr: 0.0389\n  total: 164\n  wall_time_min: 67.6\n=== eval_math500_dense_2048 ===\n  accuracy: 0.53\n  avg_response_length: 1724.5\n  median_response_length: 2048\n  n_correct: 265\n  n_total: 500\n  natural_eos_pct: 0.468\n  stderr: 0.0223\n  truncated_pct: 0.532\n=== eval_math500_dense_unpruned ===\n  accuracy: 0.736\n  n_correct: 368\n  n_total: 500\n  natural_eos_pct: 0.752\n  stderr: 0.0197\n=== eval_math500_grpo_cka_only_20 ===\n  accuracy: 0.266\n  avg_response_length: 1124.24\n  n_correct: 133\n  n_total: 500\n  stderr: 0.0198\n  truncated: 108\n  truncation_rate: 0.216\n=== eval_math500_grpo_cka_only_20_2048 ===\n  accuracy: 0.292\n  n_correct: 146\n  n_total: 500\n=== eval_math500_grpo_cka_only_20_2048_v2 ===\n  accuracy: 0.274\n  avg_response_length: 654.746\n  correct: 137\n  natural_eos: 390\n  stderr: 0.01995\n  total: 500\n  truncated: 110\n=== eval_math500_grpo_cka_only_20_fixed ===\n  accuracy: 0.276\n  n_correct: 138\n  n_total: 500\n  stderr: 0.02\n=== eval_math500_grpo_cka_only_25_fixed ===\n  accuracy: 0.176\n  avg_response_length: 719.35\n  n_correct: 88\n  n_total: 500\n  natural_eos: 367\n  stderr: 0.017\n  truncated: 133\n  truncated_pct: 0.266\n=== eval_math500_grpo_cka_only_25_v2 ===\n  correct: 92\n  math500_accuracy: 0.184\n  math500_stderr: 0.0173\n  n_total: 500\n=== eval_math500_grpo_random_20_v3 ===\n  accuracy: 0.134\n  avg_response_length: 1479.2\n  correct: 67\n  natural_eos: 167\n  stderr: 0.0152\n  total: 500\n  truncated: 333\n=== eval_math500_grpo_rasp_20_fair ===\n  accuracy: 0.24\n  avg_response_length: 903.5\n  max_new_tokens: 2048\n  median_response_length: 272\n  n_correct: 120\n  n_total: 500\n  natural_eos_pct: 0.64\n  stderr: 0.0191\n  truncated_pct: 0.36\n=== eval_math500_grpo_rasp_alpha0p5_20 ===\n  accuracy: 0.248\n  avg_response_length: 1110.462\n  correct: 124\n  natural_eos: 274\n  stderr: 0.0193\n  total: 500\n  truncated: 226\n=== eval_math500_grpo_rasp_alpha1p0_20 ===\n  accuracy: 0.226\n  avg_response_length: 903.536\n  n_correct: 113\n  n_total: 500\n  natural_eos: 320\n  stderr: 0.0187\n  truncated: 180\n=== eval_math500_grpo_rasp_alpha1p0_20_fixed ===\n  accuracy: 0.23\n  avg_response_length: 903.536\n  n_correct: 115\n  n_total: 500\n  natural_eos: 320\n  stderr: 0.0188\n  truncated: 180\n=== eval_math500_grpo_rasp_alpha2p0_20 ===\n  accuracy: 0.262\n  avg_response_length: 785.326\n  correct: 131\n  natural_eos: 349\n  stderr: 0.0197\n  total: 500\n  truncated: 151\n=== eval_math500_grpo_rasp_alpha2p0_20_fixed ===\n  accuracy: 0.274\n  n_correct: 137\n  n_total: 500\n  natural_eos: 349\n  truncated: 151\n  truncated_pct: 0.302\n=== eval_math500_grpo_rasp_alpha3p0_20 ===\n  accuracy: 0.228\n  avg_response_length: 745.038\n  correct: 114\n  stderr: 0.0188\n  total: 500\n  truncated_ratio: 0.28\n=== eval_math500_grpo_rasp_alpha4p0_20 ===\n  accuracy: 0.262\n  avg_response_length: 925.48\n  correct: 131\n  natural_eos: 320\n  stderr: 0.01966\n  total: 500\n  truncated: 180\n=== eval_math500_grpo_standard_20_fair_2048_v2 ===\n  math500_accuracy: 0.264\n  math500_correct: 132\n  math500_stderr: 0.0197\n  math500_total: 500\n=== eval_math500_grpo_standard_20_fair_v2 ===\n  accuracy: 0.264\n  n_correct: 132\n  n_total: 500\n  stderr: 0.0197\n=== eval_math500_grpo_standard_20_fixed ===\n  avg_response_length: 1127.844\n  math500_acc: 0.27\n  math500_correct: 135\n  math500_stderr: 0.0199\n  math500_total: 500\n  natural_eos: 278\n  truncated: 222\n=== eval_math500_sft_cka_only_20_fixed_v2 ===\n  accuracy: 0.274\n  num_correct: 137\n  num_total: 500\n  stderr: 0.02\n  truncated_pct: 0.232\n=== eval_math500_sft_cka_only_20_v4_restart ===\n  accuracy: 0.29\n  avg_response_length: 673.278\n  median_response_length: 242.5\n  n_correct: 145\n  n_total: 500\n  natural_eos: 384\n  natural_eos_pct: 0.768\n  stderr: 0.0203\n  truncated: 116\n=== eval_math500_sft_cka_only_20_westd ===\n  accuracy: 0.268\n  avg_response_length: 673.278\n  correct: 134\n  natural_eos_pct: 0.768\n  stderr: 0.0198\n  total: 500\n  truncated: 116\n=== eval_math500_sft_cka_only_25_v2 ===\n  correct: 96\n  math500_accuracy: 0.192\n  n_total: 500\n  std_err: 0.0176\n=== eval_math500_sft_qwen_math_cka_only_20 ===\n  accuracy: 0.216\n  avg_response_length: 1745.338\n  correct: 108\n  natural_eos: 90\n  stderr: 0.0184\n  total: 500\n  truncated: 410\n=== eval_math500_sft_random_20_v3 ===\n  accuracy: 0.144\n  avg_response_length: 1470.44\n  correct: 72\n  natural_eos: 171\n  stderr: 0.0157\n  total: 500\n  truncated: 329\n=== eval_math500_sft_rasp_20 ===\n  correct: 121\n  math500_acc: 0.242\n  stderr: 0.0192\n  total: 500\n  wall_time_hours: 2.94\n=== eval_math500_sft_rasp_20_2048 ===\n  accuracy: 0.226\n  avg_response_length: 930.58\n  median_response_length: 274\n  n_correct: 113\n  n_total: 500\n  natural_eos: 314\n  natural_eos_pct: 0.628\n  stderr: 0.0187\n  truncated: 186\n=== eval_math500_sft_rasp_alpha0p5_20 ===\n  accuracy: 0.254\n  correct: 127\n  stderr: 0.0195\n  total: 500\n  truncated: 220\n=== eval_math500_sft_rasp_alpha1p0_20_fixed ===\n  accuracy: 0.216\n  num_correct: 108\n  num_total: 500\n=== eval_math500_sft_rasp_alpha1p0_20_v2 ===\n  accuracy: 0.212\n  correct: 106\n  stderr: 0.0183\n  total: 500\n  truncated: 186\n=== eval_math500_sft_rasp_alpha2p0_20 ===\n  accuracy: 0.24\n  correct: 120\n  stderr: 0.0191\n  total: 500\n  truncated: 155\n=== eval_math500_sft_rasp_alpha2p0_20_fixed ===\n  accuracy: 0.256\n  avg_response_length: 805.754\n  n_correct: 128\n  n_total: 500\n  natural_eos: 345\n  stderr: 0.01952\n  truncated: 155\n  truncated_pct: 0.31\n=== eval_math500_sft_rasp_alpha3p0_20 ===\n  accuracy: 0.232\n  correct: 116\n  stderr: 0.0189\n  total: 500\n  truncated: 144\n=== eval_math500_sft_rasp_alpha4p0_20 ===\n  accuracy: 0.266\n  correct: 133\n  stderr: 0.0198\n  total: 500\n  truncated: 190\n=== eval_math500_sft_standard_20 ===\n  correct: 130\n  eos_rate: 0.578\n  math500_acc: 0.26\n  stderr: 0.0196\n  total: 500\n  truncated: 211\n  wall_time_hours: 3.58\n=== eval_math500_sft_standard_20_1p5b ===\n  correct: 27\n  math500_accuracy: 0.054\n  total: 500\n  truncated: 335\n=== eval_math500_sft_standard_20_2048_v2 ===\n  accuracy: 0.258\n  n_correct: 129\n  n_total: 500\n=== eval_math500_sft_standard_20_2048_v3 ===\n  math500_accuracy: 0.234\n  math500_correct: 117\n  math500_total: 500\n=== eval_math500_sft_standard_25 ===\n  avg_response_length: 1367.82\n  correct: 70\n  math500_accuracy: 0.14\n  n_total: 500\n  natural_eos: 185\n  truncated: 315\n  v1_accuracy: 0.13\n  v1_correct: 65\n=== eval_math500_unpruned ===\n  N: 500\n  accuracy: 0.736\n  correct: 368\n  stderr: 0.02\n=== eval_mbpp_dense_unpruned ===\n  n_correct: 200\n  n_total: 374\n  pass_at_1: 0.5348\n  stderr: 0.0258\n=== eval_mbpp_grpo_cka_only_20 ===\n  n_correct: 53\n  n_total: 374\n  pass_at_1: 0.1417\n  stderr: 0.018\n=== eval_mbpp_grpo_rasp_20 ===\n  n_correct: 49\n  n_total: 374\n  pass_at_1: 0.131\n  stderr: 0.0174\n=== eval_mbpp_grpo_shortgpt_20_v2 ===\n  avg_response_length: 1140.8\n  median_response_length: 804.5\n  n_correct: 54\n  n_total: 374\n  pass_at_1: 0.1444\n  stderr: 0.0182\n=== eval_mbpp_grpo_standard_20_v3 ===\n  correct: 49\n  pass_at_1: 0.131\n  stderr: 0.0174\n  total: 374\n=== eval_mbpp_grpo_standard_20_v4 ===\n  avg_response_length: 1058.7\n  median_response_length: 726\n  n_correct: 49\n  n_total: 374\n  pass_at_1: 0.131\n  stderr: 0.01745\n=== eval_mbpp_sft_cka_only_20 ===\n  avg_response_length: 643.8\n  degradation_pct: 76.01\n  dense_baseline_pass_at_1: 0.5348\n  median_response_length: 363.5\n  n_correct: 48\n  n_total: 374\n  pass_at_1: 0.1283\n  stderr: 0.0173\n=== eval_mbpp_sft_rasp_20 ===\n  avg_response_length: 810.7\n  degradation_pct: 78.01\n  dense_baseline_pass_at_1: 0.5348\n  median_response_length: 247\n  n_correct: 44\n  n_total: 374\n  pass_at_1: 0.1176\n  stderr: 0.0167\n=== eval_mbpp_sft_shortgpt_20_v2 ===\n  avg_response_length: 1166.4\n  median_response_length: 773.5\n  n_correct: 39\n  n_total: 374\n  pass_at_1: 0.1043\n  stderr: 0.0158\n=== eval_mbpp_sft_standard_20_1p5b ===\n  avg_response_length: 1658.6\n  median_response_length: 2048\n  n_correct: 3\n  n_total: 374\n  pass_at_1: 0.008021\n  stderr: 0.004613\n=== eval_mbpp_sft_standard_20_v4 ===\n  avg_response_length: 1084.1\n  median_response_length: 746.5\n  n_correct: 45\n  n_total: 374\n  pass_at_1: 0.1203\n  stderr: 0.0168\n=== eval_pass_k8_rasp_20_grpo_deepseek ===\n  n_problems: 200\n  pass_k8: 0.89\n  temperature: 0.7\n=== eval_pass_k8_rasp_20_grpo_qwen_math ===\n  accuracy: 0.915\n  k: 8\n  n_samples: 200\n  pass_at_k: 0.915\n  stderr: 0.0197\n  temperature: 0.7\n=== eval_pass_k8_rasp_20_sft_qwen_math ===\n  avg_response_length: 139.86\n  eos_rate: 0.99625\n  k: 8\n  n_problems: 200\n  natural_eos: 1594\n  pass_at_k: 0.935\n  stderr: 0.0174\n  temperature: 0.7\n  truncated: 6\n=== eval_pass_k8_unpruned_qwen_math ===\n  accuracy: 0.965\n  k: 8\n  n_samples: 200\n  pass_at_k: 0.965\n  stderr: 0.013\n  temperature: 0.7\n=== eval_postprune_qwen_math_cka_only_20 ===\n  accuracy: 0.01\n  avg_response_length: 958.3\n  eos_rate: 0.065\n  n_correct: 2\n  n_total: 200\n  note: Qwen-Math CKA-only 20% post-prune = 1.0%. Severe collapse (repetition, gibberish).\n  stderr: 0.00704\n=== eval_postprune_qwen_math_standard_20 ===\n  accuracy: 0.185\n  avg_response_length: 506.83\n  eos_rate: 0.69\n  n_correct: 37\n  n_total: 200\n  stderr: 0.02746\n=== eval_postprune_rasp_25 ===\n  accuracy: 21\n  avg_response_length: 2032.9\n  correct: 21\n  eos_rate: 56\n  natural_eos: 56",
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

_source line 51_

<details><summary>Logged reasoning block</summary>

```text
The output got cut off. Let me get the remaining experiments, particularly the ones I need for the sparsity cliff table and some other missing ones. Let me also get the GRPO training metrics (reward, f0) from the GRPO training experiments.

Actually, I have a lot of the eval data now. Let me also get the GRPO training experiments' metrics for tab1_recovery_gradient (peak reward, mean reward, min f0).

Let me extract the specific experiments I still need:
1. GRPO training experiments for reward metrics (grpo_cka_only_20, grpo_standard_20_fair, grpo_random_20, grpo_rasp_20_fair/grpo_stage2_rasp_20_v9)


2. Sparsity cliff experiments (prune_eval_standard_30, prune_eval_cka_only_30, eval_postprune_standard_30, etc.)
3. 1.5B GRPO reward metrics
4. Unpruned SFT/GRPO metrics

Let me continue extracting from where we left off.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "687da5f3-85c0-4a7c-bdf5-30b0beb30f36",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HE3kKEQzDwuE3tJfdYV6oA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 41676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
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

_source line 52_

<details open><summary>🔧 Tool call — Bash · `toolu_01JJxE7XNSwKKpi1nq1fi9Dt`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Extract GRPO training experiments for reward metrics (Tab1)\ntargets = [\n    'grpo_cka_only_20', 'grpo_standard_20_fair', 'grpo_random_20', 'grpo_rasp_20_fair',\n    'grpo_stage2_rasp_20_v9', 'grpo_unpruned_v2',\n    # 1.5B\n    'grpo_cka_only_20_1p5b', 'grpo_standard_20_1p5b', 'grpo_rasp_20_1p5b',\n    # Sparsity cliff\n    'prune_eval_standard_30', 'prune_eval_cka_only_30', 'eval_postprune_standard_30',\n    'eval_postprune_rasp_30', 'floor_ablation_0p3_cka_only_20_v2',\n    'floor_ablation_0p5_cka_only_20_v2', 'floor_ablation_0p6_cka_only_20_v2',\n    'prune_standard_30', 'prune_rasp_30', 'prune_cka_only_30',\n    # Multi-seed\n    'grpo_cka_only_20_seed123', 'grpo_cka_only_20_seed456',\n    'grpo_standard_20_seed123', 'grpo_standard_20_seed456',\n    'grpo_random_20_seed123', 'grpo_random_20_seed123_v2', 'grpo_random_20_seed456',\n    'grpo_random_20_retrain_v2',\n    # Alpha GRPO training\n    'sft-alpha-1p0', 'grpo_rasp_alpha3p0_20', 'grpo_rasp_alpha3p0_20_v2', 'grpo_alpha4_20',\n    # ShortGPT\n    'sft_shortgpt_20',\n    # CKA stability\n    'cka_scoring_stability_ablation', 'cka_calibration_stability_ablation',\n    # Math500 fixed\n    'eval_math500_sft_cka_only_20_fixed_v2', 'eval_math500_grpo_cka_only_20_fixed',\n    'eval_math500_grpo_standard_20_fixed', 'eval_math500_sft_rasp_alpha1p0_20_fixed',\n    'eval_math500_grpo_rasp_alpha1p0_20_fixed', 'eval_math500_sft_rasp_alpha2p0_20_fixed',\n    'eval_math500_grpo_rasp_alpha2p0_20_fixed', 'eval_math500_grpo_cka_only_25_fixed',\n    # Unpruned\n    'eval_sft_unpruned_full', 'sft_unpruned_baseline',\n    'eval_grpo_unpruned_v2_step100',\n    # Dense MATH-500\n    'eval_math500_dense_2048', 'eval_math500_dense_unpruned',\n    # 25% sparsity\n    'eval_gsm8k_sft_cka_only_25', 'eval_gsm8k_grpo_cka_only_25_v3',\n    'eval_gsm8k_sft_standard_25', 'eval_gsm8k_grpo_standard_25',\n    'eval_math500_sft_cka_only_25_v2', 'eval_math500_grpo_cka_only_25_v2',\n    'eval_math500_sft_standard_25',\n]\nfor eid in targets:\n    if eid in exps:\n        e = exps[eid]\n        metrics = e.get('metrics', {})\n        print(f'=== {eid} ===')\n        if metrics:\n            for k, v in sorted(metrics.items()):\n                if isinstance(v, (int, float, bool)):\n                    print(f'  {k}: {v}')\n                elif isinstance(v, dict):\n                    for k2, v2 in sorted(v.items()):\n                        if isinstance(v2, (int, float)):\n                            print(f'  {k}.{k2}: {v2}')\n                elif isinstance(v, str) and len(v) < 200:\n                    print(f'  {k}: {v}')\n        else:\n            print('  (no metrics)')\n    else:\n        print(f'=== {eid} === NOT FOUND')\n\"",
  "description": "Extract specific experiment metrics for table verification",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "2949593d-c407-4d52-89ba-410f1248aac0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HE3kKEQzDwuE3tJfdYV6oA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11939,
      "cache_read_input_tokens": 41676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11939
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

_source line 53 · 2026-05-24T04:54:05.931Z_

<details><summary>↩ Tool result · `toolu_01JJxE7XNSwKKpi1nq1fi9Dt`</summary>

```text
=== grpo_cka_only_20 ===
  final_entropy: 0.08751
  final_frac_zero_std: 0.2
  final_kl: 0.001609
  final_loss: 0.23
  final_reward: 0.3444
  final_reward_std: 0.444
  final_step: 100
  peak_reward: 0.3544
  peak_reward_step: 50
  runtime_seconds: 40710
=== grpo_standard_20_fair ===
  dip_reward: 0.019
  dip_step: 50
  dynamics_pattern: dip_then_partial_recovery
  final_frac_zero_std: 0.55
  final_reward: 0.054
  peak_reward: 0.081
  peak_reward_step: 40
  runtime_seconds: 3017
  total_steps: 100
  wandb_run_id: tyv20u2k
=== grpo_random_20 ===
  data_source: log_file (W&B crashed before sync)
  entropy_mean: 0.221
  frac_zero_std_mean: 0.333
  kl_mean: 0.0045
  max_step: 90
  pattern: stable plateau, no collapse
  reward_mean: 0.164
  reward_peak: 0.19
  reward_peak_step: 70
  steps_captured: 9
=== grpo_rasp_20_fair ===
  final_completion_length: 963.0
  final_frac_zero_std: 0.85
  final_reward: 0.01
  min_frac_zero_std: 0.675
  peak_reward: 0.061
  total_steps: 100
  training_time_minutes: 62.5
  trend: stagnation_then_collapse
=== grpo_stage2_rasp_20_v9 ===
  collapse_note: frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)
  collapse_status: COLLAPSED
  final_clipped_ratio: 0.956
  final_frac_zero_std: 0.95
  final_grad_norm: 1.398
  final_kl: 0.00118
  final_loss: 0.00686
  final_mean_length: 996
  final_mean_terminated_length: 176
  final_reward: 0.021
  max_steps: 30
  step: 30
  step_time_sec: 418
  total_time: 3h28m25s
  wandb_url: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3
=== grpo_unpruned_v2 ===
  avg_step_time_sec: 23
  collapse_onset: N/A
  final_entropy: 0.194
  final_grad_norm: 6.97
  final_kl: 0.0051
  final_reward: 0.661
  max_steps: 100
  peak_reward: 0.669
  peak_reward_step: 80
  reward_range: 0.425-0.669
  training_seconds: 2660
=== grpo_cka_only_20_1p5b ===
  frac_reward_zero_std: 0.175
  global_step: 100
  grad_norm: 1.445
  kl: 0.00215
  loss: 0.0595
  note: training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.
  reward_mean: 0.2375
=== grpo_standard_20_1p5b ===
  entropy: 0.4617
  final_step: 100
  frac_reward_zero_std: 0.15
  grad_norm: 4.03125
  kl: 0.0044
  loss: 0.0151
  max_steps: 100
  reward_mean: 0.0844
  total_time_min: 53
=== grpo_rasp_20_1p5b ===
  clipped_ratio: 0.82
  final_reward: 0.099
  frac_zero_std: 0.175
=== prune_eval_standard_30 ===
  accuracy: 2.8
  avg_len: 4057
  eos_rate: 1.2
  n_evaluated: 500
  n_total: 1319
  note: N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)
=== prune_eval_cka_only_30 ===
  accuracy: 1.6
  avg_len: 4009
  eos_rate: 5.6
  n_evaluated: 500
  n_total: 1319
  note: N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)
=== eval_postprune_standard_30 ===
  avg_response_length: 3907.875
  correct: 8
  eos_rate: 0.055
  gsm8k_accuracy: 0.04
  natural_eos: 11
  total: 200
  truncated: 189
=== eval_postprune_rasp_30 ===
  accuracy: 0
  avg_response_length: 3984.31
  eos_rate: 0.03
  n_correct: 0
  n_total: 200
  natural_eos: 6
  truncated_rate: 0.97
=== floor_ablation_0p3_cka_only_20_v2 ===
  gsm8k_accuracy: 0.6505
  gsm8k_correct: 858
  gsm8k_total: 1319
=== floor_ablation_0p5_cka_only_20_v2 ===
  eos_rate: 0.992
  gsm8k_accuracy: 0.6171
  gsm8k_correct: 814
  gsm8k_total: 1319
=== floor_ablation_0p6_cka_only_20_v2 ===
  avg_response_length: 252.7
  eos_rate: 0.9803
  grpo_final_reward: 0.2419
  grpo_train_loss: 0.006503
  gsm8k_accuracy: 0.6202
  gsm8k_ci: 0.0134
  gsm8k_correct: 818
  gsm8k_total: 1319
=== prune_standard_30 ===
  actual_sparsity: 0.2854
  attn_gqa_groups_pruned: 0/112
  mlp_groups_pruned: 299/784
  params_after: 5442379264
  target_sparsity: 0.3
=== prune_rasp_30 ===
  actual_sparsity: 0.2873
  attn_groups_pruned: 0/112
  mlp_groups_pruned: 301/784
  model_size_gb: 11
  params_pruned: 5427842560
  target_sparsity: 0.3
=== prune_cka_only_30 ===
  actual_sparsity: 0.2892
  attn_heads_pruned: 0
  method: dummy_ones_importance + rasp_alpha1 = pure CKA-only
  mlp_groups_pruned: 303/784
=== grpo_cka_only_20_seed123 ===
  final_reward: 0.2975
  final_reward_std: 0.4097
  final_step_loss: 0.05054
  train_loss: 0.1361
  train_runtime_hours: 11.63
  train_steps: 100
  wandb_run: j8kn0sqd
=== grpo_cka_only_20_seed456 ===
  avg_train_loss: 0.0881
  final_kl: 0.0017
  final_loss: 0.0999
  final_reward: 0.2925
  train_runtime_min: 21.8
  train_steps: 100
=== grpo_standard_20_seed123 ===
  final_frac_zero_std: 0.6
  final_reward: 0.0594
  peak_reward: 0.0619
  peak_reward_step: 80
  runtime_sec: 2783
  seed: 123
  steps_completed: 100
  wandb_mode: offline
  wandb_run: pgzwv725
=== grpo_standard_20_seed456 ===
  final_frac_zero_std: 0.65
  final_reward: 0.06
  peak_reward: 0.0844
  peak_reward_step: 90
  runtime_sec: 2745
  seed: 456
  steps_completed: 100
  wandb_mode: offline
  wandb_run: wg0iv4oi
=== grpo_random_20_seed123 ===
  (no metrics)
=== grpo_random_20_seed123_v2 ===
  (no metrics)
=== grpo_random_20_seed456 ===
  (no metrics)
=== grpo_random_20_retrain_v2 ===
  final_completion_length_mean: 189.1
  final_entropy: 0.1704
  final_grad_norm: 5.531
  final_kl: 0.004236
  final_loss: 0.06684
  final_reward: 0.2875
  final_reward_std: 0.4291
  frac_reward_zero_std: 0.4
  training_steps: 100
  training_time_hours: 3.07
  wandb_run_id: 9c16hnf7
  wandb_run_name: grpo_sft_random_20
=== sft-alpha-1p0 ===
  post_prune_accuracy: 0.27
  token_accuracy: 0.83
  total_steps: 1870
  train_loss_final: 0.64
  train_time_min: 28
=== grpo_rasp_alpha3p0_20 ===
  (no metrics)
=== grpo_rasp_alpha3p0_20_v2 ===
  (no metrics)
=== grpo_alpha4_20 ===
  final_kl: 0.00198
  final_loss: 0.018
  final_reward: 0.198
  reward_range: 0.146-0.256
  steps: 100
=== sft_shortgpt_20 ===
  (no metrics)
=== cka_scoring_stability_ablation ===
  mean_combined_rho: 0.979
  min_combined_rho: 0.964
  spearman_256v1024_attn: 0.9762
  spearman_256v1024_combined: 0.9641
  spearman_256v1024_mlp: 0.9464
  spearman_256v512_attn: 0.989
  spearman_256v512_combined: 0.9788
  spearman_256v512_mlp: 0.9683
  spearman_512v1024_attn: 0.995
  spearman_512v1024_combined: 0.9938
  spearman_512v1024_mlp: 0.9908
  stable: True
=== cka_calibration_stability_ablation ===
  n_splits: 5
  size_sensitivity_128: 0.982
  size_sensitivity_256: 0.989
  size_sensitivity_512: 0.995
  split_half_rho: 0.9932
=== eval_math500_sft_cka_only_20_fixed_v2 ===
  accuracy: 0.274
  num_correct: 137
  num_total: 500
  stderr: 0.02
  truncated_pct: 0.232
=== eval_math500_grpo_cka_only_20_fixed ===
  accuracy: 0.276
  n_correct: 138
  n_total: 500
  stderr: 0.02
=== eval_math500_grpo_standard_20_fixed ===
  avg_response_length: 1127.844
  math500_acc: 0.27
  math500_correct: 135
  math500_stderr: 0.0199
  math500_total: 500
  natural_eos: 278
  truncated: 222
=== eval_math500_sft_rasp_alpha1p0_20_fixed ===
  accuracy: 0.216
  num_correct: 108
  num_total: 500
=== eval_math500_grpo_rasp_alpha1p0_20_fixed ===
  accuracy: 0.23
  avg_response_length: 903.536
  n_correct: 115
  n_total: 500
  natural_eos: 320
  stderr: 0.0188
  truncated: 180
=== eval_math500_sft_rasp_alpha2p0_20_fixed ===
  accuracy: 0.256
  avg_response_length: 805.754
  n_correct: 128
  n_total: 500
  natural_eos: 345
  stderr: 0.01952
  truncated: 155
  truncated_pct: 0.31
=== eval_math500_grpo_rasp_alpha2p0_20_fixed ===
  accuracy: 0.274
  n_correct: 137
  n_total: 500
  natural_eos: 349
  truncated: 151
  truncated_pct: 0.302
=== eval_math500_grpo_cka_only_25_fixed ===
  accuracy: 0.176
  avg_response_length: 719.35
  n_correct: 88
  n_total: 500
  natural_eos: 367
  stderr: 0.017
  truncated: 133
  truncated_pct: 0.266
=== eval_sft_unpruned_full ===
  accuracy: 81.27
  accuracy_ci: 1.07
  avg_response_length: 207.18
  correct: 1072
  eos_rate: 99.7
  total: 1319
  truncated: 4
=== sft_unpruned_baseline ===
  epochs: 2
  final_loss: 0.3321
  final_token_accuracy: 0.909
  total_steps: 1870
  train_loss_avg: 0.4253
  train_runtime_sec: 1908
  train_samples_per_second: 7.833
=== eval_grpo_unpruned_v2_step100 ===
  accuracy: 81.27
  avg_response_length: 209
  correct: 1072
  eos_rate: 99.7
  seed: 42
  total: 1319
=== eval_math500_dense_2048 ===
  accuracy: 0.53
  avg_response_length: 1724.5
  median_response_length: 2048
  n_correct: 265
  n_total: 500
  natural_eos_pct: 0.468
  stderr: 0.0223
  truncated_pct: 0.532
=== eval_math500_dense_unpruned ===
  accuracy: 0.736
  n_correct: 368
  n_total: 500
  natural_eos_pct: 0.752
  stderr: 0.0197
=== eval_gsm8k_sft_cka_only_25 ===
  avg_response_length: 243.6
  correct: 793
  eos_rate: 0.9803
  gsm8k_accuracy: 0.6012
  n_total: 1319
  stderr: 0.0135
=== eval_gsm8k_grpo_cka_only_25_v3 ===
  correct: 786
  eos_rate: 0.9818
  gsm8k_accuracy: 0.5959
  n_total: 1319
=== eval_gsm8k_sft_standard_25 ===
  avg_response_length: 333.15
  correct: 671
  eos_rate: 0.953
  gsm8k_accuracy: 0.5087
  n_total: 1319
  stderr: 0.0138
=== eval_gsm8k_grpo_standard_25 ===
  avg_response_length: 314.47
  correct: 684
  eos_rate: 0.9575
  gsm8k_accuracy: 0.5186
  n_total: 1319
  stderr: 0.0138
=== eval_math500_sft_cka_only_25_v2 ===
  correct: 96
  math500_accuracy: 0.192
  n_total: 500
  std_err: 0.0176
=== eval_math500_grpo_cka_only_25_v2 ===
  correct: 92
  math500_accuracy: 0.184
  math500_stderr: 0.0173
  n_total: 500
=== eval_math500_sft_standard_25 ===
  avg_response_length: 1367.82
  correct: 70
  math500_accuracy: 0.14
  n_total: 500
  natural_eos: 185
  truncated: 315
  v1_accuracy: 0.13
  v1_correct: 65
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "c094bcc8-aba6-46cd-a319-8d937ccfbcf4",
  "tool_use_result": {
    "stdout": "=== grpo_cka_only_20 ===\n  final_entropy: 0.08751\n  final_frac_zero_std: 0.2\n  final_kl: 0.001609\n  final_loss: 0.23\n  final_reward: 0.3444\n  final_reward_std: 0.444\n  final_step: 100\n  peak_reward: 0.3544\n  peak_reward_step: 50\n  runtime_seconds: 40710\n=== grpo_standard_20_fair ===\n  dip_reward: 0.019\n  dip_step: 50\n  dynamics_pattern: dip_then_partial_recovery\n  final_frac_zero_std: 0.55\n  final_reward: 0.054\n  peak_reward: 0.081\n  peak_reward_step: 40\n  runtime_seconds: 3017\n  total_steps: 100\n  wandb_run_id: tyv20u2k\n=== grpo_random_20 ===\n  data_source: log_file (W&B crashed before sync)\n  entropy_mean: 0.221\n  frac_zero_std_mean: 0.333\n  kl_mean: 0.0045\n  max_step: 90\n  pattern: stable plateau, no collapse\n  reward_mean: 0.164\n  reward_peak: 0.19\n  reward_peak_step: 70\n  steps_captured: 9\n=== grpo_rasp_20_fair ===\n  final_completion_length: 963.0\n  final_frac_zero_std: 0.85\n  final_reward: 0.01\n  min_frac_zero_std: 0.675\n  peak_reward: 0.061\n  total_steps: 100\n  training_time_minutes: 62.5\n  trend: stagnation_then_collapse\n=== grpo_stage2_rasp_20_v9 ===\n  collapse_note: frac_zero_std peaked at 95% by step 30, reward dropped from peak 0.039 (step 20) to 0.021 (step 30)\n  collapse_status: COLLAPSED\n  final_clipped_ratio: 0.956\n  final_frac_zero_std: 0.95\n  final_grad_norm: 1.398\n  final_kl: 0.00118\n  final_loss: 0.00686\n  final_mean_length: 996\n  final_mean_terminated_length: 176\n  final_reward: 0.021\n  max_steps: 30\n  step: 30\n  step_time_sec: 418\n  total_time: 3h28m25s\n  wandb_url: https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/mrikafz3\n=== grpo_unpruned_v2 ===\n  avg_step_time_sec: 23\n  collapse_onset: N/A\n  final_entropy: 0.194\n  final_grad_norm: 6.97\n  final_kl: 0.0051\n  final_reward: 0.661\n  max_steps: 100\n  peak_reward: 0.669\n  peak_reward_step: 80\n  reward_range: 0.425-0.669\n  training_seconds: 2660\n=== grpo_cka_only_20_1p5b ===\n  frac_reward_zero_std: 0.175\n  global_step: 100\n  grad_norm: 1.445\n  kl: 0.00215\n  loss: 0.0595\n  note: training completed 100/100 but save_model failed (disk full). checkpoint-100 has complete model.\n  reward_mean: 0.2375\n=== grpo_standard_20_1p5b ===\n  entropy: 0.4617\n  final_step: 100\n  frac_reward_zero_std: 0.15\n  grad_norm: 4.03125\n  kl: 0.0044\n  loss: 0.0151\n  max_steps: 100\n  reward_mean: 0.0844\n  total_time_min: 53\n=== grpo_rasp_20_1p5b ===\n  clipped_ratio: 0.82\n  final_reward: 0.099\n  frac_zero_std: 0.175\n=== prune_eval_standard_30 ===\n  accuracy: 2.8\n  avg_len: 4057\n  eos_rate: 1.2\n  n_evaluated: 500\n  n_total: 1319\n  note: N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\n=== prune_eval_cka_only_30 ===\n  accuracy: 1.6\n  avg_len: 4009\n  eos_rate: 5.6\n  n_evaluated: 500\n  n_total: 1319\n  note: N=500 partial result (killed by Director, 30% sparsity = complete collapse, N=500 precision sufficient)\n=== eval_postprune_standard_30 ===\n  avg_response_length: 3907.875\n  correct: 8\n  eos_rate: 0.055\n  gsm8k_accuracy: 0.04\n  natural_eos: 11\n  total: 200\n  truncated: 189\n=== eval_postprune_rasp_30 ===\n  accuracy: 0\n  avg_response_length: 3984.31\n  eos_rate: 0.03\n  n_correct: 0\n  n_total: 200\n  natural_eos: 6\n  truncated_rate: 0.97\n=== floor_ablation_0p3_cka_only_20_v2 ===\n  gsm8k_accuracy: 0.6505\n  gsm8k_correct: 858\n  gsm8k_total: 1319\n=== floor_ablation_0p5_cka_only_20_v2 ===\n  eos_rate: 0.992\n  gsm8k_accuracy: 0.6171\n  gsm8k_correct: 814\n  gsm8k_total: 1319\n=== floor_ablation_0p6_cka_only_20_v2 ===\n  avg_response_length: 252.7\n  eos_rate: 0.9803\n  grpo_final_reward: 0.2419\n  grpo_train_loss: 0.006503\n  gsm8k_accuracy: 0.6202\n  gsm8k_ci: 0.0134\n  gsm8k_correct: 818\n  gsm8k_total: 1319\n=== prune_standard_30 ===\n  actual_sparsity: 0.2854\n  attn_gqa_groups_pruned: 0/112\n  mlp_groups_pruned: 299/784\n  params_after: 5442379264\n  target_sparsity: 0.3\n=== prune_rasp_30 ===\n  actual_sparsity: 0.2873\n  attn_groups_pruned: 0/112\n  mlp_groups_pruned: 301/784\n  model_size_gb: 11\n  params_pruned: 5427842560\n  target_sparsity: 0.3\n=== prune_cka_only_30 ===\n  actual_sparsity: 0.2892\n  attn_heads_pruned: 0\n  method: dummy_ones_importance + rasp_alpha1 = pure CKA-only\n  mlp_groups_pruned: 303/784\n=== grpo_cka_only_20_seed123 ===\n  final_reward: 0.2975\n  final_reward_std: 0.4097\n  final_step_loss: 0.05054\n  train_loss: 0.1361\n  train_runtime_hours: 11.63\n  train_steps: 100\n  wandb_run: j8kn0sqd\n=== grpo_cka_only_20_seed456 ===\n  avg_train_loss: 0.0881\n  final_kl: 0.0017\n  final_loss: 0.0999\n  final_reward: 0.2925\n  train_runtime_min: 21.8\n  train_steps: 100\n=== grpo_standard_20_seed123 ===\n  final_frac_zero_std: 0.6\n  final_reward: 0.0594\n  peak_reward: 0.0619\n  peak_reward_step: 80\n  runtime_sec: 2783\n  seed: 123\n  steps_completed: 100\n  wandb_mode: offline\n  wandb_run: pgzwv725\n=== grpo_standard_20_seed456 ===\n  final_frac_zero_std: 0.65\n  final_reward: 0.06\n  peak_reward: 0.0844\n  peak_reward_step: 90\n  runtime_sec: 2745\n  seed: 456\n  steps_completed: 100\n  wandb_mode: offline\n  wandb_run: wg0iv4oi\n=== grpo_random_20_seed123 ===\n  (no metrics)\n=== grpo_random_20_seed123_v2 ===\n  (no metrics)\n=== grpo_random_20_seed456 ===\n  (no metrics)\n=== grpo_random_20_retrain_v2 ===\n  final_completion_length_mean: 189.1\n  final_entropy: 0.1704\n  final_grad_norm: 5.531\n  final_kl: 0.004236\n  final_loss: 0.06684\n  final_reward: 0.2875\n  final_reward_std: 0.4291\n  frac_reward_zero_std: 0.4\n  training_steps: 100\n  training_time_hours: 3.07\n  wandb_run_id: 9c16hnf7\n  wandb_run_name: grpo_sft_random_20\n=== sft-alpha-1p0 ===\n  post_prune_accuracy: 0.27\n  token_accuracy: 0.83\n  total_steps: 1870\n  train_loss_final: 0.64\n  train_time_min: 28\n=== grpo_rasp_alpha3p0_20 ===\n  (no metrics)\n=== grpo_rasp_alpha3p0_20_v2 ===\n  (no metrics)\n=== grpo_alpha4_20 ===\n  final_kl: 0.00198\n  final_loss: 0.018\n  final_reward: 0.198\n  reward_range: 0.146-0.256\n  steps: 100\n=== sft_shortgpt_20 ===\n  (no metrics)\n=== cka_scoring_stability_ablation ===\n  mean_combined_rho: 0.979\n  min_combined_rho: 0.964\n  spearman_256v1024_attn: 0.9762\n  spearman_256v1024_combined: 0.9641\n  spearman_256v1024_mlp: 0.9464\n  spearman_256v512_attn: 0.989\n  spearman_256v512_combined: 0.9788\n  spearman_256v512_mlp: 0.9683\n  spearman_512v1024_attn: 0.995\n  spearman_512v1024_combined: 0.9938\n  spearman_512v1024_mlp: 0.9908\n  stable: True\n=== cka_calibration_stability_ablation ===\n  n_splits: 5\n  size_sensitivity_128: 0.982\n  size_sensitivity_256: 0.989\n  size_sensitivity_512: 0.995\n  split_half_rho: 0.9932\n=== eval_math500_sft_cka_only_20_fixed_v2 ===\n  accuracy: 0.274\n  num_correct: 137\n  num_total: 500\n  stderr: 0.02\n  truncated_pct: 0.232\n=== eval_math500_grpo_cka_only_20_fixed ===\n  accuracy: 0.276\n  n_correct: 138\n  n_total: 500\n  stderr: 0.02\n=== eval_math500_grpo_standard_20_fixed ===\n  avg_response_length: 1127.844\n  math500_acc: 0.27\n  math500_correct: 135\n  math500_stderr: 0.0199\n  math500_total: 500\n  natural_eos: 278\n  truncated: 222\n=== eval_math500_sft_rasp_alpha1p0_20_fixed ===\n  accuracy: 0.216\n  num_correct: 108\n  num_total: 500\n=== eval_math500_grpo_rasp_alpha1p0_20_fixed ===\n  accuracy: 0.23\n  avg_response_length: 903.536\n  n_correct: 115\n  n_total: 500\n  natural_eos: 320\n  stderr: 0.0188\n  truncated: 180\n=== eval_math500_sft_rasp_alpha2p0_20_fixed ===\n  accuracy: 0.256\n  avg_response_length: 805.754\n  n_correct: 128\n  n_total: 500\n  natural_eos: 345\n  stderr: 0.01952\n  truncated: 155\n  truncated_pct: 0.31\n=== eval_math500_grpo_rasp_alpha2p0_20_fixed ===\n  accuracy: 0.274\n  n_correct: 137\n  n_total: 500\n  natural_eos: 349\n  truncated: 151\n  truncated_pct: 0.302\n=== eval_math500_grpo_cka_only_25_fixed ===\n  accuracy: 0.176\n  avg_response_length: 719.35\n  n_correct: 88\n  n_total: 500\n  natural_eos: 367\n  stderr: 0.017\n  truncated: 133\n  truncated_pct: 0.266\n=== eval_sft_unpruned_full ===\n  accuracy: 81.27\n  accuracy_ci: 1.07\n  avg_response_length: 207.18\n  correct: 1072\n  eos_rate: 99.7\n  total: 1319\n  truncated: 4\n=== sft_unpruned_baseline ===\n  epochs: 2\n  final_loss: 0.3321\n  final_token_accuracy: 0.909\n  total_steps: 1870\n  train_loss_avg: 0.4253\n  train_runtime_sec: 1908\n  train_samples_per_second: 7.833\n=== eval_grpo_unpruned_v2_step100 ===\n  accuracy: 81.27\n  avg_response_length: 209\n  correct: 1072\n  eos_rate: 99.7\n  seed: 42\n  total: 1319\n=== eval_math500_dense_2048 ===\n  accuracy: 0.53\n  avg_response_length: 1724.5\n  median_response_length: 2048\n  n_correct: 265\n  n_total: 500\n  natural_eos_pct: 0.468\n  stderr: 0.0223\n  truncated_pct: 0.532\n=== eval_math500_dense_unpruned ===\n  accuracy: 0.736\n  n_correct: 368\n  n_total: 500\n  natural_eos_pct: 0.752\n  stderr: 0.0197\n=== eval_gsm8k_sft_cka_only_25 ===\n  avg_response_length: 243.6\n  correct: 793\n  eos_rate: 0.9803\n  gsm8k_accuracy: 0.6012\n  n_total: 1319\n  stderr: 0.0135\n=== eval_gsm8k_grpo_cka_only_25_v3 ===\n  correct: 786\n  eos_rate: 0.9818\n  gsm8k_accuracy: 0.5959\n  n_total: 1319\n=== eval_gsm8k_sft_standard_25 ===\n  avg_response_length: 333.15\n  correct: 671\n  eos_rate: 0.953\n  gsm8k_accuracy: 0.5087\n  n_total: 1319\n  stderr: 0.0138\n=== eval_gsm8k_grpo_standard_25 ===\n  avg_response_length: 314.47\n  correct: 684\n  eos_rate: 0.9575\n  gsm8k_accuracy: 0.5186\n  n_total: 1319\n  stderr: 0.0138\n=== eval_math500_sft_cka_only_25_v2 ===\n  correct: 96\n  math500_accuracy: 0.192\n  n_total: 500\n  std_err: 0.0176\n=== eval_math500_grpo_cka_only_25_v2 ===\n  correct: 92\n  math500_accuracy: 0.184\n  math500_stderr: 0.0173\n  n_total: 500\n=== eval_math500_sft_standard_25 ===\n  avg_response_length: 1367.82\n  correct: 70\n  math500_accuracy: 0.14\n  n_total: 500\n  natural_eos: 185\n  truncated: 315\n  v1_accuracy: 0.13\n  v1_correct: 65",
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

_source line 54_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the registry data I need. Let me also check for some additional experiments - specifically the mean reward and min f0 for CKA-only, and multi-seed GRPO data for standard and random.

Let me also check:
1. Tab2 uses mean±std for GRPO accuracy across 3 seeds. I need to verify the multi-seed data.
2. Tab1's Mean Rew and Min f0 - need to check if these come from training logs or specific metrics.
3. MATH-500 with "fixed" eval - the docs version uses non-fixed values for some entries.


4. The standard 20% GRPO accuracy reported as 59.84±0.38 - I'm verifying this against the individual seed results of 59.44%, 59.89%, and 60.20%.

5. For the CKA-only seeds, I'm checking the mean of 64.37%, 64.22%, and 64.59% which gives 64.39%, and calculating the standard deviation to confirm it matches the reported value.

Now I'm verifying the random seeds results—the three runs show accuracies around 50.57%, 50.72%, and 50.87%, with a mean of approximately 50.72%. I'm noticing a discrepancy between the calculated accuracy and what the table shows—the registry gives me 781/1319 = 59.21%, but the table lists 59.29% for the standard 20% SFT model. Let me double-check if I'm looking at the right experiment or if there's a calculation error somewhere. I'm noticing a discrepancy between the table showing 59.29% and the registry value of 59.21% for the same experiment. The math checks out—782 correct answers would give 59.29%, but 781 gives 59.21%—so either the table has the wrong count or it's pulling from a different version of the experiment, possibly the retrained variant.

Let me also verify the fair variants to make sure I'm comparing the right checkpoints. The SFT baseline is eval_gsm8k_sft_standard_20 at 59.21%, which doesn't match the table's 59.29%, so that's a mismatch I need to flag. Now I'll move on to checking the RASP variants with the same scrutiny.

Checking the remaining entries: RASP SFT comes in at 61.49%, RASP GRPO at 60.88%, Random SFT at 51.25%, and ShortGPT SFT at 44.73%—all matching the table. ShortGPT GRPO is next to verify.

Moving to the Recovery Gradient tab now. The CKA-only peak reward of 0.3544 rounds to 0.354 across three decimal places, which checks out. But the mean reward is trickier—the registry shows a final reward of 0.3444, yet the table lists 0.285 for mean reward. I need to figure out where that 0.285 comes from, possibly by looking at how mean reward is calculated across all training steps rather than just the final value.

Checking the random baseline: it has a mean reward of 0.164 and peak of 0.190, both matching the table. For the standard approach, the peak reward of 0.081 matches, but the mean reward of 0.050 doesn't align with the registry's final reward of 0.054—these appear to be different metrics, with mean reward being an average across all steps while final reward is the value at step 100. The CKA-only mean reward of 0.285 in the table would require wandb data to verify.

Looking at RASP, the peak reward of 0.061 checks out, but again the mean reward of 0.031 isn't directly in the registry since that's a computed average across training steps. For the minimum f0 metrics, the registry doesn't have a dedicated field for CKA-only, only the final fraction of zero standard deviations at 0.2. I should note these mean reward values as not directly verifiable from the registry rather than treating them as errors. Looking at the Random case, reward_mean=0.164 matches the table, so the "Mean Rew." column represents the mean across training steps. For the other models, I can't directly verify from the registry—CKA-only and Standard don't have matching metrics, and RASP's final reward (0.01) doesn't align with the table value (0.031). Only RASP's min_frac_zero_std clearly matches the registry at 0.675; the rest aren't directly verifiable from the available metrics.

Now moving through the cross-scale results in Tab5, I'm checking the 1.5B models. For CKA-only 1.5B, the reward_mean of 0.2375 rounds to 0.238 when expressed to three decimal places, which matches the table. The GSM8K accuracy is 0.3548, corresponding to 35.48% in the table.

For Standard 1.5B, the reward value of 0.0844 rounds to 0.084, and the GSM8K accuracy of 0.2229 converts to 22.29%. For RASP 1.5B, the final_reward is 0.099 and the GSM8K accuracy is 0.2616, which should be 26.16% in the table.

Now I'm moving through the alpha dose-response results in Table 3, verifying the GSM8K accuracy values across different alpha settings and training methods. The α=0.5 SFT model shows 60.73% accuracy, the α=0.5 GRPO shows 61.18%, the α=1.0 SFT shows 61.49%, and the α=1.0 GRPO shows 60.88%.

Continuing with the higher alpha values: α=2.0 SFT reaches 64.97% accuracy, while α=2.0 GRPO peaks at 66.11%. The α=3.0 SFT drops slightly to 64.14%, and α=3.0 GRPO further decreases to 63.45%, suggesting diminishing returns at higher alpha values. Now I'm verifying the performance deltas across all alpha values—each difference between GRPO and SFT matches what the table reports, so those are all confirmed. Moving on to check the sparsity cliff results at the 30% threshold with the standard configuration. Now I'm verifying the CKA-only results match the table footnote—8 out of 500 correct gives 1.6%, which checks out. Looking at the CKA stability metrics, the Spearman correlation values are quite high, with a minimum of 0.964 and mean of 0.979. Moving on to the Math500 results, the dense model achieves 53.0% accuracy.

Checking the CKA-only variants: the fixed SFT version shows 27.4% accuracy, while the GRPO variant reaches 27.6%, both using their respective fixed implementations. The standard SFT baseline is coming in at 23%.

For the standard SFT, I'm looking at the available runs and the table appears to be using the v3 variant which achieved 23.4% accuracy. Now checking the standard GRPO results...

The fixed version shows 27.0% accuracy, which matches what's in the table. For RASP SFT, there are multiple runs available but the table correctly uses the fixed version at 21.6%. The RASP GRPO fixed version comes in at 23.0% accuracy.

Now I'm checking the random baseline results—SFT achieves 14.4% and GRPO reaches 13.4%. Moving into the alpha dose-response analysis, the α=0.5 condition shows stronger performance with SFT at 25.4% and GRPO at 24.8%.

For α=2.0, I'm using the fixed version which gives SFT 25.6% accuracy, noting there's also a non-fixed variant that scores lower at 24.0%. The GRPO variant at this alpha level performs best so far at 27.4%. Now looking at α=3.0 results... I'm noticing a discrepancy in the GRPO results for the 25% sparsity CKA-only setup—there are two different accuracy values recorded, and I need to figure out which one the paper table actually uses.

For the standard 25% configurations, I have the SFT result at 14.0%, but I'm having trouble locating the corresponding GRPO experiment for MATH-500 with standard 25% sparsity—I can see a standard 25% GRPO result for GSM8K, but not the MATH-500 variant that the table references at 12.8%.

Now checking the improvement deltas, starting with CKA-only where the difference between 27.6 and 27.4 comes to 0.2 percentage points. Now I'm verifying the α=4.0 result and checking the performance differences across the CKA-only and Standard variants at 25% scale, then cross-referencing the caption claims about the performance gaps on both CKA-only and GSM8K benchmarks. Moving on to examine the MBPP results... Now I'm looking at the remaining benchmark results across different training approaches—the RASP variants are showing similar patterns to the others, with GRPO consistently outperforming SFT, and ShortGPT starting to show lower performance metrics.

I'm verifying the percentage point differences between the baseline and each training method, confirming that CKA-only improved by 1.34 points, standard by 1.07 points, and RASP by 1.34 points.

Now I'm checking the Math500 results from the paper's table, comparing the reported accuracy and truncation metrics against the evaluation data. The Dense SFT model shows 73.6% accuracy and 24.8% truncation, which matches the eval data, but when I look at the Dense GRPO results, there's a discrepancy—the table reports 69% accuracy but the eval data shows only 53%. I'm noticing the Dense model results are confusing—the post-SFT accuracy of 73.6% dropping to 69.0% after GRPO doesn't make sense, since GRPO should improve or maintain performance. Looking at the paper's table more carefully, I see many cells are still empty, suggesting this might be a work-in-progress version. Let me focus on the entries that actually have values and figure out what's being measured here. I'm noticing the 69.0% accuracy for Dense GRPO doesn't have a matching experiment in the list, so that's still unclear. Let me scan through the available experiments more systematically to see if I missed something, and I'm also checking whether the newer table is using the fixed evaluation versions like the paper does. Checking the α=2.0 GRPO results at 27.4% accuracy with 30.2% truncation rate, and verifying the CKA-only 25% configuration shows 17.6% accuracy on the fixed version with a truncation rate around 26.6%.

The paper uses the corrected evaluation for the 25% CKA-only setup while the docs version references the older uncorrected numbers, which explains the discrepancy. Now I'm verifying the MATH-500 table captions—the dense model hits 73.6% accuracy at the 4096 token limit, and over half its responses get truncated at 2048 tokens as claimed.

Moving to the bold formatting checks, I need to confirm each highlighted value is actually the best in its column. For the reward metrics, CKA-only dominates across peak, mean, and minimum values. Now checking whether the SFT accuracy numbers are correctly bolded in the second table. Continuing through the remaining metrics—the 7B model's peak reward and GSM8K scores both check out as highest values, same with the 1.5B model across reward and GSM8K. For the MATH-500 table, the CKA-only SFT result of 27.4% is correctly bolded as the best method. The MBPP table doesn't use bold formatting, which makes sense given the caption describes a convergence near a capability floor. Now I'm digging into a discrepancy with the Standard 20% SFT accuracy—the table shows 59.29% but when I calculate from the registry data (781 correct out of 1319 total), I get 59.21%, so I need to figure out which evaluation run the table is actually referencing. I'm calculating the exact percentages to see which count matches the table value—782 correct answers gives 59.29%, while 781 gives 59.21%, so the table's 59.29% suggests a different eval run or a discrepancy in the registry's count. There might be a retrained version that was re-evaluated but I'm not finding it in the experiment IDs, so I'll flag this as a potential counting issue or transcription error.

Now I'm checking the 7B column in Table 5 to understand whether the GSM8K 64.39% refers to SFT or GRPO results, since the caption references Table 2 which contains both.

Looking at the numbers, I can verify that 64.39 matches the CKA-only GRPO mean, 59.84 matches Standard GRPO, and 60.88 matches RASP GRPO, so Table 5 is definitely using GRPO accuracies. The Random row shows a Peak Reward of 0.190 for 7B but has "--" for GSM8K, which seems inconsistent since other methods with reward scores also have GSM8K scores listed.

Now I'm checking the Δ(pp) calculations in Table 2 to verify the improvements are correct. The Unpruned and CKA-only rows check out, but I need to verify the Standard row where the difference should be 59.84 - 59.29 = 0.55.

Actually, there's a discrepancy here—if the SFT baseline is 59.21% according to the registry, then the delta would be 0.63, not 0.55. But the table uses 59.29% as its SFT value, which makes the delta internally consistent at 0.55. So the delta column is self-consistent within the table itself, though the SFT value might differ from the registry. The remaining rows all check out: RASP, Random, and ShortGPT all have deltas that match the table values.

Now I'm checking whether the "Mean Rew" and "Min f0" columns in the table have corresponding values I can verify. The CKA-only experiment shows a peak reward of 0.354 and final reward of 0.344, but the table lists Mean Rew as 0.285—this appears to be the average across all training steps rather than peak or final, which would require pulling data from W&B. The Standard and Random experiments have similar gaps where the mean reward values aren't directly available in the registry.

For the minimum f0 values, I'm finding that most entries don't have a direct "minimum" metric in the registry—they have final or mean values instead. Only the RASP experiment appears to have a min_frac_zero_std value that might correspond to the table's Min f0 of 0.675, but the others would need to be computed from the full training history.

Now checking the precision across all table columns—Peak Reward, Mean Reward, and Min f0 all maintain consistent 3 decimal place formatting, which is good. Moving on to verify the SFT Accuracy values next. I'm verifying the decimal place consistency across the remaining tables and checking the Unpruned row values in Tab2 against the source data—the SFT and GRPO accuracies both match at 81.27%, and the peak reward checks out at 0.669, though it's interesting they're identical.

Now I'm looking at the ShortGPT row to verify the Peak Reward value, which shows as "--", but I'm having trouble locating the corresponding GRPO training experiment in my data. The missing reward data for ShortGPT is likely because it's an external baseline using a different pruning approach where reward tracking wasn't applicable or collected. Looking at the Dense SFT results, I notice the footnote explains the accuracy discrepancy—the 53.0% figure is measured at a 2048-token limit, while the higher 73.6% reflects performance when allowing up to 4096 tokens, which aligns with what the table shows. The registry shows 781 correct out of 1319 total, which gives 0.5921 or 59.21%, but the table lists 59.29%—that would require 782 correct answers instead. So either the evaluation counted differently or the table was transcribed from a different source.

I should also check if there are other eval results for the retrain variants, though the ones I'm seeing are mostly limited to smaller sample sizes. I'll flag this 59.29% discrepancy and move on to compiling the full audit report.

Now I'm looking at the Dense GRPO entry in the math tables—it shows 69.0% accuracy, but I can't find a matching experiment in the registry. The closest candidates are the dense unpruned and dense 2048-token versions, but the accuracy numbers don't quite align with what I'd expect if GRPO performed worse than SFT on MATH-500 while matching it on GSM8K. I can't find a matching registry entry for the Dense GRPO results showing 69.0% and 17.2%, which is odd since GRPO shouldn't degrade performance that significantly on the unpruned model—this might be a naming issue or the experiment exists under a different label. I should flag this discrepancy. There's also a duplicate label problem in the LaTeX files that needs addressing.

Now I'm looking at the "fixed eval" situation across different configurations—comparing how CKA-only, Standard GRPO, and various RASP variants perform when using fixed versus unfixed evaluation results, which shows some meaningful differences in accuracy that I need to account for in the audit. Continuing to verify the remaining model configurations against the table values, checking both fixed and unfixed versions where available and confirming the correct entries are being used. I'm noticing that some cells in the MATH-500 table don't have fixed eval versions available in the registry yet, which suggests they haven't been re-run with the corrected methodology. The key issue is identifying which results are using the fixed eval versus the outdated version—this distinction matters for understanding the table's reliability. I'm tracking which evaluation results have fixed versions available and which ones are falling back to older evaluations—the α=2.0 GRPO matches the v2 baseline at 0.274, while the 25% CKA variant underperforms at 0.176, and several configurations lack fixed eval versions so I'm using their original counterparts instead. Looking at the registry entries for Standard 20% SFT, I can see that v3 with the 23.4% accuracy is the right match for what's shown in the table. I need to continue checking the remaining cells to identify which ones have fixed versions available and which still need updates. I can't find an eval_math500_grpo_standard_25 experiment in the registry, so that 12.8% value for Standard 25% GRPO on MATH-500 appears to be unsourced. There's a similar experiment for Qwen-Math on GSM8K, but that's a different evaluation entirely. Now I'm ready to compile the full audit report, starting with counting the cells across both tables—12 numerical entries in the first table across four methods and three metrics, and 19 in the second. Finishing the Standard row with its delta and peak values, then RASP shows a slight decrease, Random has a modest decline, and ShortGPT drops more significantly with a missing peak reward value—that brings the total to 23 cells across all methods. The remaining tables have smaller cell counts: one with 15 cells across five alpha values, and another with 8 cells split between Standard and RASP configurations. Now I'm tallying up the Random baseline results and moving through the other benchmarks—MATH-500 has a full set of 28 cells, while MBPP shows results across different methods with their SFT scores, GRPO improvements, and deltas. Now I'm looking at how different alpha values and data composition percentages affect the performance gap between SFT and GRPO across these configurations, with most showing minimal differences or slight degradation in GRPO performance.

I notice the MATH-500 Dense result uses a 2048-token constraint, and I need to verify that all the pruned model evaluations were conducted under the same token limit to ensure fair comparison.

Let me write up the report now with all these findings clearly laid out. I'm suspecting the evaluation might have used the original model checkpoint while the paper reports results from a retrained version, which would explain the score discrepancy. Without verifying which exact checkpoint was evaluated, I'll note this as a potential inconsistency and move forward with writing up my findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "e1f35837-688f-40bc-a775-fe9fd46d418a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRYpa49t24WsTrjpsQxg6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6409,
      "cache_read_input_tokens": 53615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6409
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

_source line 55_

Now I have all the data needed for the audit. Let me also check for some remaining experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "8203ffac-0f68-41ba-9f09-06a9381b77db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRYpa49t24WsTrjpsQxg6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6409,
      "cache_read_input_tokens": 53615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6409
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

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_01YJ1SsPhMys1Q4PL9RU5v9J`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check if any MATH-500 GRPO standard 25 experiment exists\nfor eid in sorted(exps.keys()):\n    if 'math500' in eid and 'standard' in eid and '25' in eid:\n        e = exps[eid]\n        print(f'{eid}: {e.get(\\\"metrics\\\",{})}')\n\nprint('---')\n# Check dense GRPO MATH-500\nfor eid in sorted(exps.keys()):\n    if 'math500' in eid and ('dense' in eid or 'unpruned' in eid or 'grpo_unpruned' in eid):\n        e = exps[eid]\n        print(f'{eid}: {e.get(\\\"metrics\\\",{})}')\n\nprint('---')\n# Check eval_grpo_unpruned for MATH-500\nfor eid in sorted(exps.keys()):\n    if 'unpruned' in eid and 'math' in eid:\n        e = exps[eid]\n        print(f'{eid}: {e.get(\\\"metrics\\\",{})}')\n\"",
  "description": "Search for missing experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "54c3e486-27cb-4501-b5de-9a1987624f91",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FRYpa49t24WsTrjpsQxg6h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6409,
      "cache_read_input_tokens": 53615,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6409
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

_source line 57 · 2026-05-24T04:59:50.312Z_

<details><summary>↩ Tool result · `toolu_01YJ1SsPhMys1Q4PL9RU5v9J`</summary>

```text
eval_math500_sft_standard_25: {'math500_accuracy': 0.14, 'correct': 70, 'n_total': 500, 'natural_eos': 185, 'truncated': 315, 'avg_response_length': 1367.82, 'v1_accuracy': 0.13, 'v1_correct': 65}
---
eval_math500_dense_2048: {'accuracy': 0.53, 'n_correct': 265, 'n_total': 500, 'stderr': 0.0223, 'natural_eos_pct': 0.468, 'truncated_pct': 0.532, 'avg_response_length': 1724.5, 'median_response_length': 2048}
eval_math500_dense_unpruned: {'accuracy': 0.736, 'stderr': 0.0197, 'n_correct': 368, 'n_total': 500, 'natural_eos_pct': 0.752}
eval_math500_unpruned: {'N': 500, 'accuracy': 0.736, 'correct': 368, 'stderr': 0.02}
---
eval_math500_dense_unpruned: {'accuracy': 0.736, 'stderr': 0.0197, 'n_correct': 368, 'n_total': 500, 'natural_eos_pct': 0.752}
eval_math500_unpruned: {'N': 500, 'accuracy': 0.736, 'correct': 368, 'stderr': 0.02}
eval_pass_k8_unpruned_qwen_math: {'accuracy': 0.965, 'k': 8, 'n_samples': 200, 'pass_at_k': 0.965, 'stderr': 0.013, 'temperature': 0.7}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "6f95958b-e9fe-44c6-ba0c-332ee4e7dbfe",
  "tool_use_result": {
    "stdout": "eval_math500_sft_standard_25: {'math500_accuracy': 0.14, 'correct': 70, 'n_total': 500, 'natural_eos': 185, 'truncated': 315, 'avg_response_length': 1367.82, 'v1_accuracy': 0.13, 'v1_correct': 65}\n---\neval_math500_dense_2048: {'accuracy': 0.53, 'n_correct': 265, 'n_total': 500, 'stderr': 0.0223, 'natural_eos_pct': 0.468, 'truncated_pct': 0.532, 'avg_response_length': 1724.5, 'median_response_length': 2048}\neval_math500_dense_unpruned: {'accuracy': 0.736, 'stderr': 0.0197, 'n_correct': 368, 'n_total': 500, 'natural_eos_pct': 0.752}\neval_math500_unpruned: {'N': 500, 'accuracy': 0.736, 'correct': 368, 'stderr': 0.02}\n---\neval_math500_dense_unpruned: {'accuracy': 0.736, 'stderr': 0.0197, 'n_correct': 368, 'n_total': 500, 'natural_eos_pct': 0.752}\neval_math500_unpruned: {'N': 500, 'accuracy': 0.736, 'correct': 368, 'stderr': 0.02}\neval_pass_k8_unpruned_qwen_math: {'accuracy': 0.965, 'k': 8, 'n_samples': 200, 'pass_at_k': 0.965, 'stderr': 0.013, 'temperature': 0.7}",
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

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Confirmed: there is no eval_math500_grpo_standard_25 experiment in the registry. The MATH-500 table's Standard 25% GRPO value (12.8%) cannot be traced.

Also confirmed: there's no "Dense GRPO MATH-500" experiment. The paper/tables version's Dense GRPO (69.0%, Trunc 17.2%) cannot be traced either.

Now I have everything I need. Let me compile the comprehensive audit report.

Let me structure this carefully:

1. Tab1 - Recovery Gradient (12 cells)
2. Tab2 - Decoupling (23 cells)


3. Tab3 - Alpha dose-response (15 cells)
4. Tab4 - Sparsity cliff (8 cells)
5. Tab5 - Cross-scale (13 cells)
6. CKA stability (2 cells)
7. MATH-500 (31 cells with Δ, 22 without)
8. MBPP (13 cells)
9. paper/tables/tab_math500.tex (newer version)

I need to compute the final Δ(pp) self-consistency and then write the report. Wait, I should reconsider the Standard SFT baseline before finalizing.

There's a discrepancy with the 59.29% figure. Looking at eval_gsm8k_sft_standard_20, I'm getting 781/1319 which calculates to 59.21%, but the table shows 59.29%. The difference is minimal—less than 0.1 percentage points—and could stem from using a different SFT checkpoint variant, though the eval is registered under the standard version. The numbers are close enough that this is likely just a rounding or checkpoint variation issue. correct answer (781 vs 782). This could be:
1. A counting bug (off-by-one in answer extraction)
2. A different checkpoint being used
3. A transcription error when writing the table

Given that 0.08pp is within stderr, this is minor but still a discrepancy.

Actually, let me reconsider more carefully. The table says "59.29" which is 2 decimal places. 781/1319 = 59.2115... which rounds to 59.21 (2dp). 782/1319 = 59.2873... which rounds to 59.29 (2dp). So the table value corresponds to exactly 782/1319, not 781/1319.

Now I'm wondering if there's a different evaluation I'm overlooking. The eval_sft_standard_20_westd variants with N=100 subsets aren't what I need, but eval_sft_standard_full_westd could be the right one to check.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "45eb160f-75e0-4c59-8a44-844bb2e8f068",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iWjKzyzkoDfYAzE8JzyJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20441,
      "cache_read_input_tokens": 60024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20441
      },
      "output_tokens": 27,
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

_source line 59_

<details open><summary>🔧 Tool call — Bash · `toolu_01KeUtngbwxExxEMNopRsfVw`</summary>

```json
{
  "command": "REGFILE=\"/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/16d3e92c-d2dd-4d95-9917-d7712af3c2cb/tool-results/mcp-agent-ml-research-read_registry-1779598308194.txt\"\npython3 -c \"\nimport json\nwith open('$REGFILE') as f:\n    data = json.load(f)\nresult = json.loads(data['result'])\nexps = result['data']['experiments']\n\n# Check eval_sft_standard_full_westd and similar\ntargets = ['eval_sft_standard_full_westd', 'eval_sft_standard_20_westd_n100',\n           'eval_sft_standard_20_westd_n100_v2', 'eval_sft_rasp_full_westd',\n           'eval_sft_cka_only_20_n1319', 'eval_sft_cka_only_20',\n           'eval_sft_rasp_20_full', 'eval_sft_rasp_20_westd_n100',\n           'eval_sft_rasp_20_westd_n100_v2', 'eval_sft_unpruned_n100']\nfor eid in targets:\n    if eid in exps:\n        m = exps[eid].get('metrics', {})\n        print(f'{eid}: accuracy={m.get(\\\"accuracy\\\", m.get(\\\"gsm8k_accuracy\\\", \\\"?\\\"))}, correct={m.get(\\\"correct\\\", m.get(\\\"gsm8k_correct\\\", m.get(\\\"n_correct\\\", \\\"?\\\")))}')\n    else:\n        print(f'{eid}: NOT FOUND')\n\"",
  "description": "Check alternative SFT standard 20 eval experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "b1d98b98-b1c0-48e2-aaf2-1edab0fbedbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iWjKzyzkoDfYAzE8JzyJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20441,
      "cache_read_input_tokens": 60024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20441
      },
      "output_tokens": 27,
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

_source line 60 · 2026-05-24T05:00:16.817Z_

<details><summary>↩ Tool result · `toolu_01KeUtngbwxExxEMNopRsfVw`</summary>

```text
eval_sft_standard_full_westd: accuracy=0.5929, correct=782
eval_sft_standard_20_westd_n100: accuracy=0.63, correct=63
eval_sft_standard_20_westd_n100_v2: accuracy=0.63, correct=63
eval_sft_rasp_full_westd: accuracy=0.6149, correct=811
eval_sft_cka_only_20_n1319: accuracy=0.6391, correct=843
eval_sft_cka_only_20: accuracy=0.64, correct=128
eval_sft_rasp_20_full: accuracy=0.6156, correct=812
eval_sft_rasp_20_westd_n100: accuracy=0.67, correct=67
eval_sft_rasp_20_westd_n100_v2: accuracy=0.67, correct=67
eval_sft_unpruned_n100: accuracy=0.84, correct=84
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "06ce42b6-e0d8-4396-810f-503860c8dfad",
  "tool_use_result": {
    "stdout": "eval_sft_standard_full_westd: accuracy=0.5929, correct=782\neval_sft_standard_20_westd_n100: accuracy=0.63, correct=63\neval_sft_standard_20_westd_n100_v2: accuracy=0.63, correct=63\neval_sft_rasp_full_westd: accuracy=0.6149, correct=811\neval_sft_cka_only_20_n1319: accuracy=0.6391, correct=843\neval_sft_cka_only_20: accuracy=0.64, correct=128\neval_sft_rasp_20_full: accuracy=0.6156, correct=812\neval_sft_rasp_20_westd_n100: accuracy=0.67, correct=67\neval_sft_rasp_20_westd_n100_v2: accuracy=0.67, correct=67\neval_sft_unpruned_n100: accuracy=0.84, correct=84",
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

_source line 61_

<details><summary>Logged reasoning block</summary>

```text
Found it! `eval_sft_standard_full_westd` has accuracy=0.5929 with correct=782. This matches the table value of 59.29%!

So the table uses `eval_sft_standard_full_westd` (782/1319 = 59.29%), not `eval_gsm8k_sft_standard_20` (781/1319 = 59.21%). The difference is 1 correct answer, likely due to evaluation on a different checkpoint (the "westd retrained" version).

This means the table is correct! The experiment is `eval_sft_standard_full_westd`. ✓


The westd retrained checkpoint improves by just one answer compared to the original. I'm also verifying the other metrics—the RASP variant shows 811 correct answers across both the original and westd versions, so those are consistent. Now checking the CKA-only results to see if those align as well. Now I'm comparing the RASP SFT results—there's a slight discrepancy between eval_gsm8k_sft_rasp_20 (811 correct, 61.49%) and eval_sft_rasp_20_full (812 correct, 61.56%), but the table matches the first one at 61.49%, so that's the version being used.

I've verified the audit and I'm ready to write up the full report. One thing to flag: some of the Tab1 metrics like Mean Reward and Min f0 for the CKA-only, Standard, and Random variants aren't directly in the registry—only Random's Mean Reward and RASP's Min f0 check out—so I'll mark those as needing W&B data to fully verify.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "aa5dbb6c-1a07-4cd9-aca3-6530a284b797",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRgyu4L1rmfrKNcLwW6fYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 80465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1627
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

_source line 62_

Found it — `eval_sft_standard_full_westd` has accuracy 0.5929 (782/1319), matching the table's 59.29%. The Standard SFT uses the retrained westd checkpoint. Now I have all the data for the complete audit.

---

## 全量 Table 数据审计报告

---

### tab1_recovery_gradient.tex (4 methods × 3 metrics = 12 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| CKA-only Mean Rew | 0.285 | `grpo_cka_only_20` | 无 mean_reward 字段 (final_reward=0.3444) | ⚠️ W&B |
| CKA-only Min f₀ | 0.125 | `grpo_cka_only_20` | 无 min_frac_zero_std 字段 (final=0.2) | ⚠️ W&B |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| Random Mean Rew | 0.164 | `grpo_random_20` | reward_mean: 0.164 | ✅ |
| Random Min f₀ | 0.300 | `grpo_random_20` | frac_zero_std_mean: 0.333 (非 min) | ⚠️ W&B |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| Standard Mean Rew | 0.050 | `grpo_standard_20_fair` | 无 mean 字段 (final_reward=0.054) | ⚠️ W&B |
| Standard Min f₀ | 0.500 | `grpo_standard_20_fair` | final_frac_zero_std: 0.55 (非 min) | ⚠️ W&B |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| RASP Mean Rew | 0.031 | `grpo_rasp_20_fair` | 无 mean 字段 (final_reward=0.01) | ⚠️ W&B |
| RASP Min f₀ | 0.675 | `grpo_rasp_20_fair` | min_frac_zero_std: 0.675 | ✅ |

**小结**: 6/12 ✅ 直接验证, 6/12 ⚠️ 需 W&B 训练曲线验证 (Mean Rew 和 Min f₀ 是 step-level 聚合值, registry 仅记录 peak/final)。数值精度统一 3 位小数 ✓。Bold 标记正确 ✓。

---

### tab2_decoupling.tex (23 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Unpruned SFT | 81.27% | `eval_sft_unpruned_full` | accuracy: 81.27 | ✅ |
| Unpruned GRPO | 81.27% | `eval_grpo_unpruned_v2_step100` | accuracy: 81.27 (1072/1319) | ✅ |
| Unpruned Δ | 0.00 | computed | 81.27 − 81.27 = 0.00 | ✅ |
| Unpruned Peak Rew | 0.669 | `grpo_unpruned_v2` | peak_reward: 0.669 | ✅ |
| CKA-only SFT | 63.91% | `eval_gsm8k_sft_cka_only_20` | gsm8k_accuracy: 0.6391 (843/1319) | ✅ |
| CKA-only GRPO mean | 64.39% | seeds 42/123/456 | (64.37+64.22+64.59)/3 = 64.39 | ✅ |
| CKA-only GRPO std | ±0.19 | seeds 42/123/456 | std(64.37,64.22,64.59) = 0.186 → 0.19 | ✅ |
| CKA-only Δ | +0.48 | computed | 64.39 − 63.91 = 0.48 | ✅ |
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| Standard SFT | 59.29% | `eval_sft_standard_full_westd` | accuracy: 0.5929 (782/1319) | ✅ |
| Standard GRPO mean | 59.84% | seeds 42/123/456 | (59.44+59.89+60.20)/3 = 59.84 | ✅ |
| Standard GRPO std | ±0.38 | seeds 42/123/456 | std = 0.382 → 0.38 | ✅ |
| Standard Δ | +0.55 | computed | 59.84 − 59.29 = 0.55 | ✅ |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| RASP SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | gsm8k_accuracy: 0.6149 (811/1319) | ✅ |
| RASP GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | accuracy: 0.6088 (803/1319) | ✅ |
| RASP Δ | −0.61 | computed | 60.88 − 61.49 = −0.61 | ✅ |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| Random SFT | 51.25% | `eval_gsm8k_sft_random_20` | gsm8k_accuracy: 0.5125 (676/1319) | ✅ |
| Random GRPO mean | 50.72% | seeds 42/123/456 | (50.57+50.72+50.87)/3 = 50.72 | ✅ |
| Random GRPO std | ±0.15 | seeds 42/123/456 | std = 0.15 | ✅ |
| Random Δ | −0.53 | computed | 50.72 − 51.25 = −0.53 | ✅ |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| ShortGPT SFT | 44.73% | `eval_gsm8k_sft_shortgpt_20` | gsm8k_accuracy: 44.73 | ✅ |
| ShortGPT GRPO | 43.37% | `eval_gsm8k_grpo_shortgpt_20` | gsm8k_accuracy: 43.37 | ✅ |
| ShortGPT Δ | −1.36 | computed | 43.37 − 44.73 = −1.36 | ✅ |
| ShortGPT Peak Rew | -- | N/A | 无 ShortGPT GRPO 训练实验 | ✅ (正确标注为 --) |

**Multi-seed source exp_ids**:
- CKA-only: `eval_gsm8k_grpo_cka_only_20_v2` (seed42, 0.6437), `eval_gsm8k_grpo_cka_only_20_seed123` (0.6422), `eval_gsm8k_grpo_cka_only_20_seed456_full` (0.6459)
- Standard: `eval_gsm8k_grpo_standard_20_fair_v2` (seed42, 59.44%), `eval_gsm8k_grpo_standard_20_seed123_full` (0.5989), `eval_gsm8k_grpo_standard_20_seed456_full` (0.602)
- Random: `eval_gsm8k_grpo_random_20_v2` (seed42, 0.5057), `eval_gsm8k_grpo_random_20_seed123_v2` (0.5072), `eval_gsm8k_grpo_random_20_seed456` (0.5087)

**小结**: 27/27 ✅。精度统一 (GSM8K 2dp, Reward 3dp) ✓。Bold 正确 ✓。Footnote 脚注 ($N{=}1$ for RASP, 3 seeds for others) 与数据一致 ✓。

---

### table3_alpha.tex (5 α × 3 columns = 15 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| α=0.5 SFT | 60.73% | `eval_gsm8k_sft_alpha0p5_20` | 0.6073 | ✅ |
| α=0.5 GRPO | 61.18% | `eval_gsm8k_grpo_alpha0p5_20` | 0.6118 | ✅ |
| α=0.5 Δ | +0.45 | computed | 61.18−60.73=0.45 | ✅ |
| α=1.0 SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | 0.6149 | ✅ |
| α=1.0 GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| α=1.0 Δ | −0.61 | computed | 60.88−61.49=−0.61 | ✅ |
| α=2.0 SFT | 64.97% | `eval_gsm8k_sft_alpha2p0_20` | 0.6497 | ✅ |
| α=2.0 GRPO | 66.11% | `eval_gsm8k_grpo_alpha2p0_20` | 0.6611 | ✅ |
| α=2.0 Δ | +1.14 | computed | 66.11−64.97=1.14 | ✅ |
| α=3.0 SFT | 64.14% | `eval_gsm8k_sft_alpha3p0_20` | 0.6414 (846/1319) | ✅ |
| α=3.0 GRPO | 63.46% | `eval_gsm8k_grpo_alpha3p0_20` | 0.6345 → 837/1319=63.46% | ✅ |
| α=3.0 Δ | −0.68 | computed | 63.46−64.14=−0.68 | ✅ |
| α=4.0 SFT | 61.94% | `eval_gsm8k_sft_alpha4_20_v5` | 0.6194 (817/1319) | ✅ |
| α=4.0 GRPO | 62.77% | `eval_gsm8k_grpo_alpha4_20_v3` | 0.6277 (828/1319) | ✅ |
| α=4.0 Δ | +0.83 | computed | 62.77−61.94=0.83 | ✅ |

**注**: α=3.0 GRPO registry 存储值 0.6345 是 4dp 截断, 实际 837/1319=0.63457→63.46%。表格值正确。

**小结**: 15/15 ✅。精度 2dp 统一 ✓。Bold (α=2.0) 正确 ✓。

---

### table4_sparsity_cliff.tex (8 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Standard N | 200 | `eval_postprune_standard_30` | total: 200 | ✅ |
| Standard Acc | 4% | `eval_postprune_standard_30` | gsm8k_accuracy: 0.04 → 4% | ✅ |
| Standard EOS Rate | 5.5% | `eval_postprune_standard_30` | eos_rate: 0.055 → 5.5% | ✅ |
| RASP N | 200 | `eval_postprune_rasp_30` | n_total: 200 | ✅ |
| RASP Acc | 0% | `eval_postprune_rasp_30` | accuracy: 0 | ✅ |
| RASP EOS Rate | 3.0% | `eval_postprune_rasp_30` | eos_rate: 0.03 → 3.0% | ✅ |
| CKA-only N | 500† | `prune_eval_cka_only_30` | n_evaluated: 500 | ✅ |
| CKA-only Acc | 1.6% | `prune_eval_cka_only_30` | accuracy: 1.6 | ✅ |

**Footnote 验证**: "8/500 correct" → 8/500=1.6% ✓。CKA-only EOS Rate = "--†" (terminated early, 正确标注) ✓。

**小结**: 8/8 ✅。

---

### tab5_cross_scale.tex (13 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only 7B Peak Rew | 0.354 | `grpo_cka_only_20` | 0.3544 → 0.354 | ✅ |
| CKA-only 7B GSM8K | 64.39% | multi-seed mean (Tab2) | 64.39 | ✅ |
| Standard 7B Peak Rew | 0.081 | `grpo_standard_20_fair` | 0.081 | ✅ |
| Standard 7B GSM8K | 59.84% | multi-seed mean (Tab2) | 59.84 | ✅ |
| RASP 7B Peak Rew | 0.061 | `grpo_rasp_20_fair` | 0.061 | ✅ |
| RASP 7B GSM8K | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| Random 7B Peak Rew | 0.190 | `grpo_random_20` | 0.19 | ✅ |
| Random 7B GSM8K | -- | N/A | 实际可用 (50.72%) 但未填 | ⚠️ 有意省略 |
| CKA-only 1.5B Rew | 0.238 | `grpo_cka_only_20_1p5b` | reward_mean: 0.2375 → 0.238 | ✅ |
| CKA-only 1.5B GSM8K | 35.48% | `eval_gsm8k_grpo_cka_only_20_1p5b` | 0.3548 | ✅ |
| Standard 1.5B Rew | 0.084 | `grpo_standard_20_1p5b` | reward_mean: 0.0844 → 0.084 | ✅ |
| Standard 1.5B GSM8K | 22.29% | `eval_gsm8k_grpo_standard_20_1p5b` | 0.2229 | ✅ |
| RASP 1.5B Rew | 0.099 | `grpo_rasp_20_1p5b` | final_reward: 0.099 | ✅ |
| RASP 1.5B GSM8K | 26.16% | `eval_gsm8k_grpo_rasp_20_1p5b` | 0.2616 | ✅ |

**注**: Random 7B GSM8K 为 "--"。该值在 Tab2 中可用 (50.72%), 但因 Random 无 1.5B 实验, 省略以保持 cross-scale 对比的完整性。语义合理。

**Caption 验证**: "7B reward = peak" — 7B 列确实用 peak_reward ✓; "1.5B reward = mean" — 1.5B 列用 reward_mean ✓。

**小结**: 13/13 ✅ (Random GSM8K "--" 为有意省略)。Bold 正确 ✓。

---

### tab_cka_stability.tex (2 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` | min_combined_rho: 0.964 | ✅ |
| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` | mean_combined_rho: 0.979 | ✅ |

**Caption 验证**: "High correlation (ρ ≥ 0.964)" — 正确引用 min 值 ✓。

**小结**: 2/2 ✅。

---

### tab_math500.tex (docs/paper/tables — 31 cells incl. Δ)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense | 53.0%† | `eval_math500_dense_2048` | 0.53 | ✅ |
| **20% method comparison** | | | | |
| CKA-only SFT | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ fixed |
| CKA-only GRPO | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ fixed |
| CKA-only Δ | +0.2 | computed | 27.6−27.4=0.2 | ✅ |
| Standard SFT | 23.4% | `eval_math500_sft_standard_20_2048_v3` | 0.234 | ✅ 非 fixed |
| Standard GRPO | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ fixed |
| Standard Δ | +3.6 | computed | 27.0−23.4=3.6 | ✅ |
| RASP SFT | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ fixed |
| RASP GRPO | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ fixed |
| RASP Δ | +1.4 | computed | 23.0−21.6=1.4 | ✅ |
| Random SFT | 14.4% | `eval_math500_sft_random_20_v3` | 0.144 | ✅ 非 fixed |
| Random GRPO | 13.4% | `eval_math500_grpo_random_20_v3` | 0.134 | ✅ 非 fixed |
| Random Δ | −1.0 | computed | 13.4−14.4=−1.0 | ✅ |
| **α dose-response** | | | | |
| α=0.5 SFT | 25.4% | `eval_math500_sft_rasp_alpha0p5_20` | 0.254 | ✅ 非 fixed |
| α=0.5 GRPO | 24.8% | `eval_math500_grpo_rasp_alpha0p5_20` | 0.248 | ✅ 非 fixed |
| α=0.5 Δ | −0.6 | computed | 24.8−25.4=−0.6 | ✅ |
| α=2.0 SFT | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ fixed |
| α=2.0 GRPO | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ fixed |
| α=2.0 Δ | +1.8 | computed | 27.4−25.6=1.8 | ✅ |
| α=3.0 SFT | 23.2% | `eval_math500_sft_rasp_alpha3p0_20` | 0.232 | ✅ 非 fixed |
| α=3.0 GRPO | 22.8% | `eval_math500_grpo_rasp_alpha3p0_20` | 0.228 | ✅ 非 fixed |
| α=3.0 Δ | −0.4 | computed | 22.8−23.2=−0.4 | ✅ |
| α=4.0 SFT | 26.6% | `eval_math500_sft_rasp_alpha4p0_20` | 0.266 | ✅ 非 fixed |
| α=4.0 GRPO | 26.2% | `eval_math500_grpo_rasp_alpha4p0_20` | 0.262 | ✅ 非 fixed |
| α=4.0 Δ | −0.4 | computed | 26.2−26.6=−0.4 | ✅ |
| **25% sparsity** | | | | |
| CKA-only 25% SFT | 19.2% | `eval_math500_sft_cka_only_25_v2` | 0.192 | ✅ 非 fixed |
| CKA-only 25% GRPO | 18.4% | `eval_math500_grpo_cka_only_25_v2` | 0.184 | ⚠️ 非 fixed; fixed 版本=17.6% |
| CKA-only 25% Δ | −0.8 | computed | 18.4−19.2=−0.8 | ✅ |
| Standard 25% SFT | 14.0% | `eval_math500_sft_standard_25` | 0.14 | ✅ 非 fixed |
| Standard 25% GRPO | 12.8% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard 25% Δ | −1.2 | computed | 12.8−14.0=−1.2 | ✅ (算术正确, 但 GRPO 源不明) |

**Caption 验证**:
- "CKA-only–Standard GRPO gap is 0.6 pp" → 27.6−27.0=0.6 ✓
- "vs. 4.6 pp on GSM8K" → 64.39−59.84=4.55 → 4.6 ✓ (四舍五入)
- "73.6% at 4096" → eval_math500_dense_unpruned=0.736 ✓

**⚠️ Fixed vs 非 fixed 混用问题**:

已使用 fixed eval 的 cell (8个): CKA-only 20% SFT/GRPO, Standard 20% GRPO, RASP 20% SFT/GRPO, α=2.0 SFT/GRPO

仍在使用旧 eval 的 cell (10个):
1. Standard 20% SFT — 无 fixed 版本
2. Random 20% SFT/GRPO — 无 fixed 版本
3. α=0.5 SFT/GRPO — 无 fixed 版本
4. α=3.0 SFT/GRPO — 无 fixed 版本
5. α=4.0 SFT/GRPO — 无 fixed 版本
6. CKA-only 25% SFT — 无 fixed 版本
7. CKA-only 25% GRPO — fixed 版本已有 (17.6%) 但表格仍用旧值 (18.4%)
8. Standard 25% SFT — 无 fixed 版本

**小结**: 29/31 ✅, 1 ⚠️ (CKA-only 25% GRPO 应更新为 fixed 值 17.6%), 1 ❌ (Standard 25% GRPO 12.8% 无 registry 来源)。精度 1dp 统一 ✓。Bold 正确 ✓。

---

### tab_mbpp.tex (13 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense GRPO | 53.48% | `eval_mbpp_dense_unpruned` | pass_at_1: 0.5348 | ✅ |
| CKA-only SFT | 12.83% | `eval_mbpp_sft_cka_only_20` | pass_at_1: 0.1283 | ✅ |
| CKA-only GRPO | 14.17% | `eval_mbpp_grpo_cka_only_20` | pass_at_1: 0.1417 | ✅ |
| CKA-only Δ | +1.34 | computed | 14.17−12.83=1.34 | ✅ |
| Standard SFT | 12.03% | `eval_mbpp_sft_standard_20_v4` | pass_at_1: 0.1203 | ✅ |
| Standard GRPO | 13.10% | `eval_mbpp_grpo_standard_20_v4` | pass_at_1: 0.131 | ✅ |
| Standard Δ | +1.07 | computed | 13.10−12.03=1.07 | ✅ |
| RASP SFT | 11.76% | `eval_mbpp_sft_rasp_20` | pass_at_1: 0.1176 | ✅ |
| RASP GRPO | 13.10% | `eval_mbpp_grpo_rasp_20` | pass_at_1: 0.131 | ✅ |
| RASP Δ | +1.34 | computed | 13.10−11.76=1.34 | ✅ |
| ShortGPT SFT | 10.43% | `eval_mbpp_sft_shortgpt_20_v2` | pass_at_1: 0.1043 | ✅ |
| ShortGPT GRPO | 14.44% | `eval_mbpp_grpo_shortgpt_20_v2` | pass_at_1: 0.1444 | ✅ |
| ShortGPT Δ | +4.01 | computed | 14.44−10.43=4.01 | ✅ |

**小结**: 13/13 ✅。精度 2dp 统一 ✓。

---

### paper/tables/tab_math500.tex (更新版, 含 truncation rate)

此版本结构不同 (Post-SFT / Post-GRPO 各有 Acc + Trunc 列), 大量 "--" 待填。仅审计有值 cell:

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense SFT Acc | 73.6% | `eval_math500_dense_unpruned` | 0.736 | ✅ |
| Dense SFT Trunc | 24.8% | `eval_math500_dense_unpruned` | 1−natural_eos_pct(0.752)=0.248 | ✅ |
| Dense GRPO Acc | 69.0% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Dense GRPO Trunc | 17.2% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard GRPO Acc | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ |
| CKA-only SFT Acc | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ |
| CKA-only SFT Trunc | 23.2% | `eval_math500_sft_cka_only_20_fixed_v2` | truncated_pct: 0.232 | ✅ |
| CKA-only GRPO Acc | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ |
| RASP SFT Acc | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ |
| RASP GRPO Acc | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ |
| RASP GRPO Trunc | 36.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 180/500=0.36 | ✅ |
| α=2.0 SFT Acc | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ |
| α=2.0 SFT Trunc | 31.0% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | truncated_pct: 0.31 | ✅ |
| α=2.0 GRPO Acc | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ |
| α=2.0 GRPO Trunc | 30.2% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | truncated_pct: 0.302 | ✅ |
| CKA-only 25% GRPO Acc | 17.6% | `eval_math500_grpo_cka_only_25_fixed` | 0.176 | ✅ fixed |
| CKA-only 25% GRPO Trunc | 26.6% | `eval_math500_grpo_cka_only_25_fixed` | truncated_pct: 0.266 | ✅ |

**注**: 此版本 CKA-only 25% GRPO 已更新为 fixed 值 17.6% (docs 版仍用 18.4%)。

**小结**: 15/17 有值 cell ✅, 2 ❌ (Dense GRPO Acc 69.0% 和 Trunc 17.2% 无 registry 来源)。`\label{tab:math500}` 与 docs 版重复, 编译时会冲突。

---

## 总结

| Table | 总 cell 数 | ✅ 已验证 | ⚠️ 需确认 | ❌ 问题 |
|-------|-----------|----------|----------|--------|
| tab1_recovery_gradient | 12 | 6 | 6 (W&B) | 0 |
| tab2_decoupling | 27 | 27 | 0 | 0 |
| table3_alpha | 15 | 15 | 0 | 0 |
| table4_sparsity_cliff | 8 | 8 | 0 | 0 |
| tab5_cross_scale | 13 | 13 | 0 | 0 |
| tab_cka_stability | 2 | 2 | 0 | 0 |
| tab_math500 (docs) | 31 | 29 | 1 | 1 |
| tab_mbpp | 13 | 13 | 0 | 0 |
| tab_math500 (paper/) | 17 | 15 | 0 | 2 |
| **合计** | **138** | **128** | **7** | **3** |

### 必须修复的问题 (❌)

1. **tab_math500 docs: Standard 25% GRPO = 12.8%** — 无 registry 实验可追溯。需确认来源或补跑 `eval_math500_grpo_standard_25_fixed`。

2. **tab_math500 paper/: Dense GRPO Acc = 69.0%, Trunc = 17.2%** — 无 registry 实验。需补跑 unpruned GRPO 模型的 MATH-500 评估并注册。

### 需要决策的问题 (⚠️)

3. **tab1 Mean Rew / Min f₀ (6 cells)** — 来自 W&B 训练曲线聚合, registry 仅有 peak/final 值。建议从 W&B 提取并注册为 metrics (或在 caption 注明来源)。

4. **tab_math500 docs: CKA-only 25% GRPO** — 旧值 18.4% vs fixed 值 17.6%。paper/ 版本已更新, docs 版本需同步更新为 17.6%。

5. **tab_math500 fixed/非 fixed 混用** — 10 个 cell 仍用旧 eval (α=0.5/3.0/4.0 全部, Standard SFT, Random SFT/GRPO, 25% sparsity 部分)。如果 fixed eval 是最终协议, 这些需要补跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "uuid": "3bea65e3-537a-4399-9a95-1218dd190828",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRgyu4L1rmfrKNcLwW6fYg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1627,
      "cache_read_input_tokens": 80465,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1627
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

### Task result

_source line 63_

Found it — `eval_sft_standard_full_westd` has accuracy 0.5929 (782/1319), matching the table's 59.29%. The Standard SFT uses the retrained westd checkpoint. Now I have all the data for the complete audit.

---

## 全量 Table 数据审计报告

---

### tab1_recovery_gradient.tex (4 methods × 3 metrics = 12 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| CKA-only Mean Rew | 0.285 | `grpo_cka_only_20` | 无 mean_reward 字段 (final_reward=0.3444) | ⚠️ W&B |
| CKA-only Min f₀ | 0.125 | `grpo_cka_only_20` | 无 min_frac_zero_std 字段 (final=0.2) | ⚠️ W&B |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| Random Mean Rew | 0.164 | `grpo_random_20` | reward_mean: 0.164 | ✅ |
| Random Min f₀ | 0.300 | `grpo_random_20` | frac_zero_std_mean: 0.333 (非 min) | ⚠️ W&B |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| Standard Mean Rew | 0.050 | `grpo_standard_20_fair` | 无 mean 字段 (final_reward=0.054) | ⚠️ W&B |
| Standard Min f₀ | 0.500 | `grpo_standard_20_fair` | final_frac_zero_std: 0.55 (非 min) | ⚠️ W&B |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| RASP Mean Rew | 0.031 | `grpo_rasp_20_fair` | 无 mean 字段 (final_reward=0.01) | ⚠️ W&B |
| RASP Min f₀ | 0.675 | `grpo_rasp_20_fair` | min_frac_zero_std: 0.675 | ✅ |

**小结**: 6/12 ✅ 直接验证, 6/12 ⚠️ 需 W&B 训练曲线验证 (Mean Rew 和 Min f₀ 是 step-level 聚合值, registry 仅记录 peak/final)。数值精度统一 3 位小数 ✓。Bold 标记正确 ✓。

---

### tab2_decoupling.tex (23 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Unpruned SFT | 81.27% | `eval_sft_unpruned_full` | accuracy: 81.27 | ✅ |
| Unpruned GRPO | 81.27% | `eval_grpo_unpruned_v2_step100` | accuracy: 81.27 (1072/1319) | ✅ |
| Unpruned Δ | 0.00 | computed | 81.27 − 81.27 = 0.00 | ✅ |
| Unpruned Peak Rew | 0.669 | `grpo_unpruned_v2` | peak_reward: 0.669 | ✅ |
| CKA-only SFT | 63.91% | `eval_gsm8k_sft_cka_only_20` | gsm8k_accuracy: 0.6391 (843/1319) | ✅ |
| CKA-only GRPO mean | 64.39% | seeds 42/123/456 | (64.37+64.22+64.59)/3 = 64.39 | ✅ |
| CKA-only GRPO std | ±0.19 | seeds 42/123/456 | std(64.37,64.22,64.59) = 0.186 → 0.19 | ✅ |
| CKA-only Δ | +0.48 | computed | 64.39 − 63.91 = 0.48 | ✅ |
| CKA-only Peak Rew | 0.354 | `grpo_cka_only_20` | peak_reward: 0.3544 → 0.354 | ✅ |
| Standard SFT | 59.29% | `eval_sft_standard_full_westd` | accuracy: 0.5929 (782/1319) | ✅ |
| Standard GRPO mean | 59.84% | seeds 42/123/456 | (59.44+59.89+60.20)/3 = 59.84 | ✅ |
| Standard GRPO std | ±0.38 | seeds 42/123/456 | std = 0.382 → 0.38 | ✅ |
| Standard Δ | +0.55 | computed | 59.84 − 59.29 = 0.55 | ✅ |
| Standard Peak Rew | 0.081 | `grpo_standard_20_fair` | peak_reward: 0.081 | ✅ |
| RASP SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | gsm8k_accuracy: 0.6149 (811/1319) | ✅ |
| RASP GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | accuracy: 0.6088 (803/1319) | ✅ |
| RASP Δ | −0.61 | computed | 60.88 − 61.49 = −0.61 | ✅ |
| RASP Peak Rew | 0.061 | `grpo_rasp_20_fair` | peak_reward: 0.061 | ✅ |
| Random SFT | 51.25% | `eval_gsm8k_sft_random_20` | gsm8k_accuracy: 0.5125 (676/1319) | ✅ |
| Random GRPO mean | 50.72% | seeds 42/123/456 | (50.57+50.72+50.87)/3 = 50.72 | ✅ |
| Random GRPO std | ±0.15 | seeds 42/123/456 | std = 0.15 | ✅ |
| Random Δ | −0.53 | computed | 50.72 − 51.25 = −0.53 | ✅ |
| Random Peak Rew | 0.190 | `grpo_random_20` | reward_peak: 0.19 | ✅ |
| ShortGPT SFT | 44.73% | `eval_gsm8k_sft_shortgpt_20` | gsm8k_accuracy: 44.73 | ✅ |
| ShortGPT GRPO | 43.37% | `eval_gsm8k_grpo_shortgpt_20` | gsm8k_accuracy: 43.37 | ✅ |
| ShortGPT Δ | −1.36 | computed | 43.37 − 44.73 = −1.36 | ✅ |
| ShortGPT Peak Rew | -- | N/A | 无 ShortGPT GRPO 训练实验 | ✅ (正确标注为 --) |

**Multi-seed source exp_ids**:
- CKA-only: `eval_gsm8k_grpo_cka_only_20_v2` (seed42, 0.6437), `eval_gsm8k_grpo_cka_only_20_seed123` (0.6422), `eval_gsm8k_grpo_cka_only_20_seed456_full` (0.6459)
- Standard: `eval_gsm8k_grpo_standard_20_fair_v2` (seed42, 59.44%), `eval_gsm8k_grpo_standard_20_seed123_full` (0.5989), `eval_gsm8k_grpo_standard_20_seed456_full` (0.602)
- Random: `eval_gsm8k_grpo_random_20_v2` (seed42, 0.5057), `eval_gsm8k_grpo_random_20_seed123_v2` (0.5072), `eval_gsm8k_grpo_random_20_seed456` (0.5087)

**小结**: 27/27 ✅。精度统一 (GSM8K 2dp, Reward 3dp) ✓。Bold 正确 ✓。Footnote 脚注 ($N{=}1$ for RASP, 3 seeds for others) 与数据一致 ✓。

---

### table3_alpha.tex (5 α × 3 columns = 15 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| α=0.5 SFT | 60.73% | `eval_gsm8k_sft_alpha0p5_20` | 0.6073 | ✅ |
| α=0.5 GRPO | 61.18% | `eval_gsm8k_grpo_alpha0p5_20` | 0.6118 | ✅ |
| α=0.5 Δ | +0.45 | computed | 61.18−60.73=0.45 | ✅ |
| α=1.0 SFT | 61.49% | `eval_gsm8k_sft_rasp_20` | 0.6149 | ✅ |
| α=1.0 GRPO | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| α=1.0 Δ | −0.61 | computed | 60.88−61.49=−0.61 | ✅ |
| α=2.0 SFT | 64.97% | `eval_gsm8k_sft_alpha2p0_20` | 0.6497 | ✅ |
| α=2.0 GRPO | 66.11% | `eval_gsm8k_grpo_alpha2p0_20` | 0.6611 | ✅ |
| α=2.0 Δ | +1.14 | computed | 66.11−64.97=1.14 | ✅ |
| α=3.0 SFT | 64.14% | `eval_gsm8k_sft_alpha3p0_20` | 0.6414 (846/1319) | ✅ |
| α=3.0 GRPO | 63.46% | `eval_gsm8k_grpo_alpha3p0_20` | 0.6345 → 837/1319=63.46% | ✅ |
| α=3.0 Δ | −0.68 | computed | 63.46−64.14=−0.68 | ✅ |
| α=4.0 SFT | 61.94% | `eval_gsm8k_sft_alpha4_20_v5` | 0.6194 (817/1319) | ✅ |
| α=4.0 GRPO | 62.77% | `eval_gsm8k_grpo_alpha4_20_v3` | 0.6277 (828/1319) | ✅ |
| α=4.0 Δ | +0.83 | computed | 62.77−61.94=0.83 | ✅ |

**注**: α=3.0 GRPO registry 存储值 0.6345 是 4dp 截断, 实际 837/1319=0.63457→63.46%。表格值正确。

**小结**: 15/15 ✅。精度 2dp 统一 ✓。Bold (α=2.0) 正确 ✓。

---

### table4_sparsity_cliff.tex (8 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Standard N | 200 | `eval_postprune_standard_30` | total: 200 | ✅ |
| Standard Acc | 4% | `eval_postprune_standard_30` | gsm8k_accuracy: 0.04 → 4% | ✅ |
| Standard EOS Rate | 5.5% | `eval_postprune_standard_30` | eos_rate: 0.055 → 5.5% | ✅ |
| RASP N | 200 | `eval_postprune_rasp_30` | n_total: 200 | ✅ |
| RASP Acc | 0% | `eval_postprune_rasp_30` | accuracy: 0 | ✅ |
| RASP EOS Rate | 3.0% | `eval_postprune_rasp_30` | eos_rate: 0.03 → 3.0% | ✅ |
| CKA-only N | 500† | `prune_eval_cka_only_30` | n_evaluated: 500 | ✅ |
| CKA-only Acc | 1.6% | `prune_eval_cka_only_30` | accuracy: 1.6 | ✅ |

**Footnote 验证**: "8/500 correct" → 8/500=1.6% ✓。CKA-only EOS Rate = "--†" (terminated early, 正确标注) ✓。

**小结**: 8/8 ✅。

---

### tab5_cross_scale.tex (13 numerical cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| CKA-only 7B Peak Rew | 0.354 | `grpo_cka_only_20` | 0.3544 → 0.354 | ✅ |
| CKA-only 7B GSM8K | 64.39% | multi-seed mean (Tab2) | 64.39 | ✅ |
| Standard 7B Peak Rew | 0.081 | `grpo_standard_20_fair` | 0.081 | ✅ |
| Standard 7B GSM8K | 59.84% | multi-seed mean (Tab2) | 59.84 | ✅ |
| RASP 7B Peak Rew | 0.061 | `grpo_rasp_20_fair` | 0.061 | ✅ |
| RASP 7B GSM8K | 60.88% | `eval_gsm8k_grpo_rasp_20_fair` | 0.6088 | ✅ |
| Random 7B Peak Rew | 0.190 | `grpo_random_20` | 0.19 | ✅ |
| Random 7B GSM8K | -- | N/A | 实际可用 (50.72%) 但未填 | ⚠️ 有意省略 |
| CKA-only 1.5B Rew | 0.238 | `grpo_cka_only_20_1p5b` | reward_mean: 0.2375 → 0.238 | ✅ |
| CKA-only 1.5B GSM8K | 35.48% | `eval_gsm8k_grpo_cka_only_20_1p5b` | 0.3548 | ✅ |
| Standard 1.5B Rew | 0.084 | `grpo_standard_20_1p5b` | reward_mean: 0.0844 → 0.084 | ✅ |
| Standard 1.5B GSM8K | 22.29% | `eval_gsm8k_grpo_standard_20_1p5b` | 0.2229 | ✅ |
| RASP 1.5B Rew | 0.099 | `grpo_rasp_20_1p5b` | final_reward: 0.099 | ✅ |
| RASP 1.5B GSM8K | 26.16% | `eval_gsm8k_grpo_rasp_20_1p5b` | 0.2616 | ✅ |

**注**: Random 7B GSM8K 为 "--"。该值在 Tab2 中可用 (50.72%), 但因 Random 无 1.5B 实验, 省略以保持 cross-scale 对比的完整性。语义合理。

**Caption 验证**: "7B reward = peak" — 7B 列确实用 peak_reward ✓; "1.5B reward = mean" — 1.5B 列用 reward_mean ✓。

**小结**: 13/13 ✅ (Random GSM8K "--" 为有意省略)。Bold 正确 ✓。

---

### tab_cka_stability.tex (2 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Spearman ρ (min) | 0.964 | `cka_scoring_stability_ablation` | min_combined_rho: 0.964 | ✅ |
| Spearman ρ (mean) | 0.979 | `cka_scoring_stability_ablation` | mean_combined_rho: 0.979 | ✅ |

**Caption 验证**: "High correlation (ρ ≥ 0.964)" — 正确引用 min 值 ✓。

**小结**: 2/2 ✅。

---

### tab_math500.tex (docs/paper/tables — 31 cells incl. Δ)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense | 53.0%† | `eval_math500_dense_2048` | 0.53 | ✅ |
| **20% method comparison** | | | | |
| CKA-only SFT | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ fixed |
| CKA-only GRPO | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ fixed |
| CKA-only Δ | +0.2 | computed | 27.6−27.4=0.2 | ✅ |
| Standard SFT | 23.4% | `eval_math500_sft_standard_20_2048_v3` | 0.234 | ✅ 非 fixed |
| Standard GRPO | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ fixed |
| Standard Δ | +3.6 | computed | 27.0−23.4=3.6 | ✅ |
| RASP SFT | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ fixed |
| RASP GRPO | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ fixed |
| RASP Δ | +1.4 | computed | 23.0−21.6=1.4 | ✅ |
| Random SFT | 14.4% | `eval_math500_sft_random_20_v3` | 0.144 | ✅ 非 fixed |
| Random GRPO | 13.4% | `eval_math500_grpo_random_20_v3` | 0.134 | ✅ 非 fixed |
| Random Δ | −1.0 | computed | 13.4−14.4=−1.0 | ✅ |
| **α dose-response** | | | | |
| α=0.5 SFT | 25.4% | `eval_math500_sft_rasp_alpha0p5_20` | 0.254 | ✅ 非 fixed |
| α=0.5 GRPO | 24.8% | `eval_math500_grpo_rasp_alpha0p5_20` | 0.248 | ✅ 非 fixed |
| α=0.5 Δ | −0.6 | computed | 24.8−25.4=−0.6 | ✅ |
| α=2.0 SFT | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ fixed |
| α=2.0 GRPO | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ fixed |
| α=2.0 Δ | +1.8 | computed | 27.4−25.6=1.8 | ✅ |
| α=3.0 SFT | 23.2% | `eval_math500_sft_rasp_alpha3p0_20` | 0.232 | ✅ 非 fixed |
| α=3.0 GRPO | 22.8% | `eval_math500_grpo_rasp_alpha3p0_20` | 0.228 | ✅ 非 fixed |
| α=3.0 Δ | −0.4 | computed | 22.8−23.2=−0.4 | ✅ |
| α=4.0 SFT | 26.6% | `eval_math500_sft_rasp_alpha4p0_20` | 0.266 | ✅ 非 fixed |
| α=4.0 GRPO | 26.2% | `eval_math500_grpo_rasp_alpha4p0_20` | 0.262 | ✅ 非 fixed |
| α=4.0 Δ | −0.4 | computed | 26.2−26.6=−0.4 | ✅ |
| **25% sparsity** | | | | |
| CKA-only 25% SFT | 19.2% | `eval_math500_sft_cka_only_25_v2` | 0.192 | ✅ 非 fixed |
| CKA-only 25% GRPO | 18.4% | `eval_math500_grpo_cka_only_25_v2` | 0.184 | ⚠️ 非 fixed; fixed 版本=17.6% |
| CKA-only 25% Δ | −0.8 | computed | 18.4−19.2=−0.8 | ✅ |
| Standard 25% SFT | 14.0% | `eval_math500_sft_standard_25` | 0.14 | ✅ 非 fixed |
| Standard 25% GRPO | 12.8% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard 25% Δ | −1.2 | computed | 12.8−14.0=−1.2 | ✅ (算术正确, 但 GRPO 源不明) |

**Caption 验证**:
- "CKA-only–Standard GRPO gap is 0.6 pp" → 27.6−27.0=0.6 ✓
- "vs. 4.6 pp on GSM8K" → 64.39−59.84=4.55 → 4.6 ✓ (四舍五入)
- "73.6% at 4096" → eval_math500_dense_unpruned=0.736 ✓

**⚠️ Fixed vs 非 fixed 混用问题**:

已使用 fixed eval 的 cell (8个): CKA-only 20% SFT/GRPO, Standard 20% GRPO, RASP 20% SFT/GRPO, α=2.0 SFT/GRPO

仍在使用旧 eval 的 cell (10个):
1. Standard 20% SFT — 无 fixed 版本
2. Random 20% SFT/GRPO — 无 fixed 版本
3. α=0.5 SFT/GRPO — 无 fixed 版本
4. α=3.0 SFT/GRPO — 无 fixed 版本
5. α=4.0 SFT/GRPO — 无 fixed 版本
6. CKA-only 25% SFT — 无 fixed 版本
7. CKA-only 25% GRPO — fixed 版本已有 (17.6%) 但表格仍用旧值 (18.4%)
8. Standard 25% SFT — 无 fixed 版本

**小结**: 29/31 ✅, 1 ⚠️ (CKA-only 25% GRPO 应更新为 fixed 值 17.6%), 1 ❌ (Standard 25% GRPO 12.8% 无 registry 来源)。精度 1dp 统一 ✓。Bold 正确 ✓。

---

### tab_mbpp.tex (13 cells)

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense GRPO | 53.48% | `eval_mbpp_dense_unpruned` | pass_at_1: 0.5348 | ✅ |
| CKA-only SFT | 12.83% | `eval_mbpp_sft_cka_only_20` | pass_at_1: 0.1283 | ✅ |
| CKA-only GRPO | 14.17% | `eval_mbpp_grpo_cka_only_20` | pass_at_1: 0.1417 | ✅ |
| CKA-only Δ | +1.34 | computed | 14.17−12.83=1.34 | ✅ |
| Standard SFT | 12.03% | `eval_mbpp_sft_standard_20_v4` | pass_at_1: 0.1203 | ✅ |
| Standard GRPO | 13.10% | `eval_mbpp_grpo_standard_20_v4` | pass_at_1: 0.131 | ✅ |
| Standard Δ | +1.07 | computed | 13.10−12.03=1.07 | ✅ |
| RASP SFT | 11.76% | `eval_mbpp_sft_rasp_20` | pass_at_1: 0.1176 | ✅ |
| RASP GRPO | 13.10% | `eval_mbpp_grpo_rasp_20` | pass_at_1: 0.131 | ✅ |
| RASP Δ | +1.34 | computed | 13.10−11.76=1.34 | ✅ |
| ShortGPT SFT | 10.43% | `eval_mbpp_sft_shortgpt_20_v2` | pass_at_1: 0.1043 | ✅ |
| ShortGPT GRPO | 14.44% | `eval_mbpp_grpo_shortgpt_20_v2` | pass_at_1: 0.1444 | ✅ |
| ShortGPT Δ | +4.01 | computed | 14.44−10.43=4.01 | ✅ |

**小结**: 13/13 ✅。精度 2dp 统一 ✓。

---

### paper/tables/tab_math500.tex (更新版, 含 truncation rate)

此版本结构不同 (Post-SFT / Post-GRPO 各有 Acc + Trunc 列), 大量 "--" 待填。仅审计有值 cell:

| Cell | Table Value | Registry exp_id | Registry Value | Status |
|------|-------------|-----------------|----------------|--------|
| Dense SFT Acc | 73.6% | `eval_math500_dense_unpruned` | 0.736 | ✅ |
| Dense SFT Trunc | 24.8% | `eval_math500_dense_unpruned` | 1−natural_eos_pct(0.752)=0.248 | ✅ |
| Dense GRPO Acc | 69.0% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Dense GRPO Trunc | 17.2% | ❌ **无 registry 实验** | — | ❌ 无法追溯 |
| Standard GRPO Acc | 27.0% | `eval_math500_grpo_standard_20_fixed` | 0.27 | ✅ |
| CKA-only SFT Acc | 27.4% | `eval_math500_sft_cka_only_20_fixed_v2` | 0.274 | ✅ |
| CKA-only SFT Trunc | 23.2% | `eval_math500_sft_cka_only_20_fixed_v2` | truncated_pct: 0.232 | ✅ |
| CKA-only GRPO Acc | 27.6% | `eval_math500_grpo_cka_only_20_fixed` | 0.276 | ✅ |
| RASP SFT Acc | 21.6% | `eval_math500_sft_rasp_alpha1p0_20_fixed` | 0.216 | ✅ |
| RASP GRPO Acc | 23.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 0.23 | ✅ |
| RASP GRPO Trunc | 36.0% | `eval_math500_grpo_rasp_alpha1p0_20_fixed` | 180/500=0.36 | ✅ |
| α=2.0 SFT Acc | 25.6% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | 0.256 | ✅ |
| α=2.0 SFT Trunc | 31.0% | `eval_math500_sft_rasp_alpha2p0_20_fixed` | truncated_pct: 0.31 | ✅ |
| α=2.0 GRPO Acc | 27.4% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | 0.274 | ✅ |
| α=2.0 GRPO Trunc | 30.2% | `eval_math500_grpo_rasp_alpha2p0_20_fixed` | truncated_pct: 0.302 | ✅ |
| CKA-only 25% GRPO Acc | 17.6% | `eval_math500_grpo_cka_only_25_fixed` | 0.176 | ✅ fixed |
| CKA-only 25% GRPO Trunc | 26.6% | `eval_math500_grpo_cka_only_25_fixed` | truncated_pct: 0.266 | ✅ |

**注**: 此版本 CKA-only 25% GRPO 已更新为 fixed 值 17.6% (docs 版仍用 18.4%)。

**小结**: 15/17 有值 cell ✅, 2 ❌ (Dense GRPO Acc 69.0% 和 Trunc 17.2% 无 registry 来源)。`\label{tab:math500}` 与 docs 版重复, 编译时会冲突。

---

## 总结

| Table | 总 cell 数 | ✅ 已验证 | ⚠️ 需确认 | ❌ 问题 |
|-------|-----------|----------|----------|--------|
| tab1_recovery_gradient | 12 | 6 | 6 (W&B) | 0 |
| tab2_decoupling | 27 | 27 | 0 | 0 |
| table3_alpha | 15 | 15 | 0 | 0 |
| table4_sparsity_cliff | 8 | 8 | 0 | 0 |
| tab5_cross_scale | 13 | 13 | 0 | 0 |
| tab_cka_stability | 2 | 2 | 0 | 0 |
| tab_math500 (docs) | 31 | 29 | 1 | 1 |
| tab_mbpp | 13 | 13 | 0 | 0 |
| tab_math500 (paper/) | 17 | 15 | 0 | 2 |
| **合计** | **138** | **128** | **7** | **3** |

### 必须修复的问题 (❌)

1. **tab_math500 docs: Standard 25% GRPO = 12.8%** — 无 registry 实验可追溯。需确认来源或补跑 `eval_math500_grpo_standard_25_fixed`。

2. **tab_math500 paper/: Dense GRPO Acc = 69.0%, Trunc = 17.2%** — 无 registry 实验。需补跑 unpruned GRPO 模型的 MATH-500 评估并注册。

### 需要决策的问题 (⚠️)

3. **tab1 Mean Rew / Min f₀ (6 cells)** — 来自 W&B 训练曲线聚合, registry 仅有 peak/final 值。建议从 W&B 提取并注册为 metrics (或在 caption 注明来源)。

4. **tab_math500 docs: CKA-only 25% GRPO** — 旧值 18.4% vs fixed 值 17.6%。paper/ 版本已更新, docs 版本需同步更新为 17.6%。

5. **tab_math500 fixed/非 fixed 混用** — 10 个 cell 仍用旧 eval (α=0.5/3.0/4.0 全部, Standard SFT, Random SFT/GRPO, 25% sparsity 部分)。如果 fixed eval 是最终协议, 这些需要补跑。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 682194,
  "duration_api_ms": 679532,
  "num_turns": 24,
  "stop_reason": "end_turn",
  "session_id": "16d3e92c-d2dd-4d95-9917-d7712af3c2cb",
  "total_cost_usd": 1.7006877500000002,
  "usage": {
    "input_tokens": 17,
    "cache_creation_input_tokens": 70251,
    "cache_read_input_tokens": 514644,
    "output_tokens": 40087,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 70251,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 10389,
        "cache_read_input_tokens": 80465,
        "cache_creation_input_tokens": 1627,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1627
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1962,
      "outputTokens": 15,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002037,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 17,
      "outputTokens": 40087,
      "cacheReadInputTokens": 514644,
      "cacheCreationInputTokens": 70251,
      "webSearchRequests": 0,
      "costUSD": 1.69865075,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "c4c6cbd2-139b-4101-a749-4c085d51f8da"
}
```

</details>

---
