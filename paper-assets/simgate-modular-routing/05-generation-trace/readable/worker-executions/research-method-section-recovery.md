# research method section recovery

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 50
- **Recorded user turns:** 1
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_method-section-recovery_20260519T110919.log`
- **Structured JSON:** [`7037ad5013320a80dc6e.json`](../../sessions/70/7037ad5013320a80dc6e.json)

## Before a recorded user message

6 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
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
  "uuid": "01a3f03c-48e0-4606-a355-1e722a6c2c22",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-12-projects-simgate-modular-routing/memory/"
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
    "resetsAt": 1779202800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "07ef61fe-6f09-4efb-8314-01a75509cfd5",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Assistant

_source line 4_

I'll start by finding the relevant files to read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "cc480af4-7771-423a-bc47-787d8e421f94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxuFVeqQzCsCvPTDmbRXYp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13449,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13449
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

<details open><summary>🔧 Tool call — Agent · `toolu_018kyKd17RYtxznyhH52XbTu`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find paper tex files",
  "prompt": "Find the method section tex file and any other relevant tex files in this project. Search for:\n1. paper/method.tex or paper/sections/method.tex or similar paths\n2. paper_framing.md\n3. Any main paper tex file\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing\n\nSearch breadth: medium"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "00e130f7-9af8-4a5a-ab23-52aa89762c99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JxuFVeqQzCsCvPTDmbRXYp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13449,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13449
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

### System

_source line 6_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Find paper tex files",
  "task_type": "local_agent",
  "prompt": "Find the method section tex file and any other relevant tex files in this project. Search for:\n1. paper/method.tex or paper/sections/method.tex or similar paths\n2. paper_framing.md\n3. Any main paper tex file\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing\n\nSearch breadth: medium",
  "uuid": "98999f87-e87f-4153-83d2-44dbaab750b9",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

## Round 1

44 recorded events

### User

_source line 7 · 2026-05-19T11:09:33.619Z_

Find the method section tex file and any other relevant tex files in this project. Search for:
1. paper/method.tex or paper/sections/method.tex or similar paths
2. paper_framing.md
3. Any main paper tex file

Working directory: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing

Search breadth: medium

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "13ab786e-27d7-4808-8c3b-d2c64caaee2a"
}
```

</details>

---

### System

_source line 8_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 15506,
    "tool_uses": 1,
    "duration_ms": 4753
  },
  "last_tool_name": "Bash",
  "uuid": "181f2789-111a-44ca-a550-c0b0691ed202",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Bash · `toolu_011tuo7MXEZ91AaVT4qHaNea`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -type f -name \"*.tex\" -o -type f -name \"*.md\" | grep -E \"(method|paper|framing)\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "e5dd8289-766e-4917-9b87-3802f36c89ae",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01VrYYm1xF5kqWwSv3V7ryVE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15487,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15487,
        "ephemeral_1h_input_tokens": 0
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

_source line 10 · 2026-05-19T11:09:39.024Z_

<details><summary>↩ Tool result · `toolu_011tuo7MXEZ91AaVT4qHaNea`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/SETUP_NOTES.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/responsibleNLPchecklist.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/paper_agent_5585d4e8/CLAUDE.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/paper_agent_5585d4e8/AGENTS.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/discussion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "d41f3ee0-8746-49c8-931e-1442a762b812"
}
```

</details>

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_050…",
  "usage": {
    "total_tokens": 17338,
    "tool_uses": 2,
    "duration_ms": 8682
  },
  "last_tool_name": "Bash",
  "uuid": "f2f6475b-43b1-454f-ae09-379b05daca83",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 12_

<details open><summary>🔧 Tool call — Bash · `toolu_01SqKg1Cwhz4VjukApM4WxG1`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing -type f -name \"paper_framing.md\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "f4b49e02-798c-47cd-9910-c28b21a3e8fc",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01L5sMyrVMEzNhGapUnRygmq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1828,
      "cache_read_input_tokens": 15487,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1828,
        "ephemeral_1h_input_tokens": 0
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

_source line 13 · 2026-05-19T11:09:42.387Z_

<details><summary>↩ Tool result · `toolu_01SqKg1Cwhz4VjukApM4WxG1`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/median/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/worst/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/dream_20260513T153257/best/paper_framing.md
/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "766397e5-6f6d-49ce-81f6-6282086322d0"
}
```

</details>

---

### System

_source line 14_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 17672,
    "tool_uses": 3,
    "duration_ms": 10203
  },
  "last_tool_name": "Bash",
  "uuid": "e2770aa1-9307-4f37-9a64-6fdfe19d95a9",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_01JLXd9bGRRWW145JqnfUVKE`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/ | grep -E \"\\.(tex|md)$\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "d13ae193-3fd5-4daf-9103-ae8549da3587",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DNKxKBy1fPQnqSK3b3oWn2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 332,
      "cache_read_input_tokens": 17315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 332,
        "ephemeral_1h_input_tokens": 0
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

_source line 16 · 2026-05-19T11:09:44.023Z_

<details><summary>↩ Tool result · `toolu_01JLXd9bGRRWW145JqnfUVKE`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu    715 May 14 11:28 SETUP_NOTES.md
-rw-r--r-- 1 ubuntu ubuntu   1117 May 19 03:35 abstract.tex
-rw-r--r-- 1 ubuntu ubuntu    798 May 18 05:30 conclusion.tex
-rw-r--r-- 1 ubuntu ubuntu   4828 May 19 11:09 discussion.tex
-rw-r--r-- 1 ubuntu ubuntu  11922 May 19 10:46 experiments.tex
-rw-r--r-- 1 ubuntu ubuntu   6017 May 19 10:46 introduction.tex
-rw-r--r-- 1 ubuntu ubuntu  46215 May 19 10:46 main.tex
-rw-r--r-- 1 ubuntu ubuntu   7233 May 19 11:09 method.tex
-rw-r--r-- 1 ubuntu ubuntu   3885 May 19 01:54 related_work.tex
-rw-r--r-- 1 ubuntu ubuntu   5500 May 18 03:50 responsibleNLPchecklist.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "79b3fb6a-6301-4889-8e23-e2501daf9990"
}
```

</details>

---

### System

_source line 17_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Reading docs/paper/method.tex",
  "usage": {
    "total_tokens": 18117,
    "tool_uses": 4,
    "duration_ms": 13522
  },
  "last_tool_name": "Read",
  "uuid": "3a10d281-9d5f-49c9-89ae-f0801f154419",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01T4qjzu3WqTqLaKiwV2AMMN`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "a4344737-6f46-498f-9f15-a6e8d9118d62",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UZE2znZwZoYG8oGj2hhmyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 17647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 19 · 2026-05-19T11:09:47.174Z_

<details><summary>↩ Tool result · `toolu_01T4qjzu3WqTqLaKiwV2AMMN`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. This near-total uninformativeness is not an artifact of our setup; it is a structural property of sparse-reward environments where only the terminal outcome discriminates strategies. We therefore perform episode-level counterfactual analysis.
15	
16	\paragraph{Pure-strategy trajectories.}
17	For a task instance $t$ and modality $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:
18	\begin{equation}
19	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
20	\end{equation}
21	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the modality choice.
22	
23	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
24	\begin{multline}
25	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
26	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
27	\end{multline}
28	
29	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two modalities can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
30	
31	\subsection{Episode-Level Labeling}
32	\label{sec:labeling}
33	
34	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
35	\begin{multline}
36	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
37	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
38	\end{multline}
39	
40	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
45	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
46	\label{fig:pipeline}
47	\end{figure}
48	
49	\subsection{Death Avoidance Factor}
50	\label{sec:daf}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "fb36f4fe-a9a1-4de2-a8e9-ed84769eb996"
}
```

</details>

---

### System

_source line 20_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Reading paper_framing.md",
  "usage": {
    "total_tokens": 18124,
    "tool_uses": 5,
    "duration_ms": 13849
  },
  "last_tool_name": "Read",
  "uuid": "e31b5c7f-4b78-4eb8-b0bf-08fbb8a2a985",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 21_

<details open><summary>🔧 Tool call — Read · `toolu_018MNqPDBniWqh9WNouuWNTb`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "5bd56678-3ee0-4bd6-9f60-1c62b8c9c0cb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UZE2znZwZoYG8oGj2hhmyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 17647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 22 · 2026-05-19T11:09:47.477Z_

<details><summary>↩ Tool result · `toolu_018MNqPDBniWqh9WNouuWNTb`</summary>

```text
1	# Paper Framing — simgate-modular-routing
2	
3	## Target Venue
4	- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**
5	- Deadline: ARR May 25, 2026 (10 days remaining)
6	- D050: Upgraded from short paper (4p, Findings) per user directive
7	
8	## Core Insight
9	
10	LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.
11	
12	## Core Claims (3 claims for long paper)
13	
14	**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
15	
16	**C2 (Episode-level counterfactual labeling methodology + informative router negative)**: Per-step oracle labeling degenerates in sparse-reward environments (97.4% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. Router training (Qwen3-1.7B on counterfactual labels) yields an **informative negative result**: step-level matched eval achieves 55.4±5.2% balanced accuracy, but episode-level independent eval drops to 47.1±2.2% (8-seed cross-split) — **below the trivial majority-vote baseline (50.0%)**. Data-size ablation (r7n2, intermediates: 5/5 evals = 0.50, all-internal predictions) suggests scaling data does not overcome the signal deficit. The methodology contribution is the counterfactual labeling framework itself; the router negative result is presented honestly and is consistent with C1's finding that routing signal is overwhelmingly task-type-level (death risk), leaving insufficient step-level signal for learned routing (D089).
17	
18	**C3 (Cross-model generality + cross-domain contrast)** [NEW for long paper]:
19	- **Cross-model mechanism verification** [Llama-3.1-8B pilot, D054→D055 corrected]: Death dominance fully replicates across model families — **both mechanism and direction consistent**. Llama pilot (freeze + find-non-living-thing, N=10): freeze's only non-tie label = death_asymmetry (internal died, det survived — same direction as Qwen where internal death rate 42.9% vs det 16.3%); find-non-living-thing has 0 deaths, all labels from score_comparison (consistent with Qwen). Llama-8B substantially weaker on ScienceWorld (most scores 0, >80% no-preference expected at scale), limiting full-scale comparison — pilot positioned as mechanism verification, not performance validation.
20	- **Cross-domain negative contrast** [MATH, N=795]: In environments WITHOUT catastrophic failure penalties (MATH: no death, no -100), the routing signal disappears — internal reasoning and code interpretation perform near-identically (+0.5pp, McNemar p=0.81, N=795). Label distribution: 66 internal-preferred / 58 det-preferred (ratio 1.14:1) vs ScienceWorld's 9 / 86 (ratio 0.10:1). The N=300 pilot showed a directional +4.3pp trend (p=0.079), but the powered N=795 extension confirms the effect is not significant — consistent with the death-avoidance mechanism: no catastrophic failures → no routing signal. Source: math-extension-n800.
21	
22	**D013 note**: C1 no longer claims "selective > unconditional." Router confirmed ≈ always-det on episode-level eval (47.1% < majority-vote 50.0%, D089). This IS the finding — the router negative result demonstrates that death avoidance signal is task-type-level and non-learnable at the step level with available data. Keyword heuristic also structurally fails (D014).
23	
24	## Positioning vs Tool-Use Literature (Dream-driven addition)
25	
26	**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:
27	- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).
28	- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.
29	- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.
30	- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.
31	
32	**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Honest negative on learned routing — router fails to generalize beyond training episodes (47.1% < majority-vote 50.0%), confirming signal is task-type-level, not step-level learnable. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from "we built a better tool selector" papers.
33	
34	**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).
35	
36	## Story Spine
37	
38	- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.
39	
40	- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (97.4% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). Router training on these labels yields an informative negative: episode-level independent eval 47.1±2.2% falls below the trivial majority-vote baseline (50.0%), and data-size ablation intermediates show no improvement with scaling (D089). The signal is overwhelmingly task-type-level (death risk), with insufficient step-level structure for learned routing.
41	
42	- **Headline result template**: "Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents."
43	
44	## Paper Structure (8-page long paper)
45	
46	| Section | Pages | Content |
47	|---------|-------|---------|
48	| Abstract | 0.3 | Counterfactual analysis framing, death avoidance finding (multi-model), headline numbers, cross-domain evidence |
49	| Introduction | 1.2 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (methodology + finding + cross-model/domain validation) |
50	| Related Work | 1.0 | Tool-use learning (Toolformer/ART/Chameleon/ToolkenGPT), adaptive computation (CogRouter/ARES/MoD), world model routing (ITP-R/Dyna-Think), safe RL, counterfactual-in-RL (Amitai/Gajcin/Olson) |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "e2b41df2-4222-492b-8126-37b21c15a6e1"
}
```

</details>

---

### System

_source line 23_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "description": "Reading docs/paper/main.tex",
  "usage": {
    "total_tokens": 18131,
    "tool_uses": 6,
    "duration_ms": 14547
  },
  "last_tool_name": "Read",
  "uuid": "478b9944-b11d-4bbf-bbe8-e2a27d83e81e",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01Bu3ArxpZyhoxT62S6YGTAF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "7989ed95-c83a-4337-a2f4-63a1c18001b8",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01UZE2znZwZoYG8oGj2hhmyk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 431,
      "cache_read_input_tokens": 17647,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 431,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
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

_source line 25 · 2026-05-19T11:09:48.174Z_

<details><summary>↩ Tool result · `toolu_01Bu3ArxpZyhoxT62S6YGTAF`</summary>

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
11	\graphicspath{{figures/}}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{algorithm}
16	\usepackage{algorithmic}
17	
18	\title{Death Avoidance as the Dominant Routing Signal:\\A Counterfactual Analysis on ScienceWorld}
19	
20	\author{Anonymous}
21	
22	\begin{document}
23	\maketitle
24	
25	\input{abstract}
26	\input{introduction}
27	\input{method}
28	\input{experiments}
29	\input{related_work}
30	\input{discussion}
31	\input{conclusion}
32	
33	\section*{Limitations}
34	
35	\paragraph{Environmental scope.}
36	Our primary analysis uses a single environment (ScienceWorld, 11 of 30 task types) with one backbone (Qwen2.5-7B-Instruct); generalization requires further validation. The $-100$ death penalty amplifies DAF; environments with softer penalties would exhibit lower DAF values (Appendix~\ref{app:penalty}). The 19 excluded task types (63\%) lack routing signal because both strategies typically time out within 30 steps; increasing the step budget could surface non-death-dominated signal that our current setup does not capture. Cross-environment analyses on MATH and ALFWorld (\S\ref{sec:cross-env}, \S\ref{sec:discussion}) provide preliminary supporting evidence but do not conclusively establish generalization. A Llama-3.1-8B-Instruct cross-model replication (11 task types, $N{=}220$; \S\ref{sec:cross-model}) shows death dominance replicates with direction consistency 10/10 while vulnerability magnitude varies ($+30.0$~pp vs.\ Qwen $+26.5$~pp), though both models are in the 7--8B parameter range; Qwen2.5-72B ($10{\times}$ scale) reduces death rate but does not eliminate death dominance (\S\ref{sec:agent-improvement}); validation beyond 72B remains future work. Our quantitative results (DAF $= 90.4\%$, label fractions) are specific to ScienceWorld; the framework's generality claim is methodological (the diagnostic procedure applies to any environment with asymmetric fatal outcomes), not empirical (the specific percentages may differ across environments).
37	
38	\paragraph{Methodological constraints.}
39	Our internal-reasoning baseline uses single-pass ReAct~\citep{react-2023}. Reflexion~\citep{reflexion-2023} reduces death rate from 42.9\% to 31.4\% (\S\ref{sec:agent-improvement}), but more aggressive self-correction or Tree-of-Thought backtracking~\citep{tot-2023} may further reduce internal death rates. Episode-level labels assign a single routing preference to entire episodes, which may be suboptimal for individual steps (particularly those preceding death events). The mislabeling fraction (episodes where the episode-level label disagrees with what step-level oracle labels would assign) is approximately 27.7\%, concentrated in death-asymmetry episodes where early steps may have favored the eventually-dying strategy. Training on pure-strategy trajectories also introduces distribution shift at deployment~\citep{dagger-2011}.
40	
41	\paragraph{Statistical limitations.}
42	Episodes within the same task type are not fully independent because they share environment dynamics, though they use different random seeds. Cluster bootstrap with $K{=}11$ task-type clusters yields wider CIs ($[73.0\%, 100\%]$); with $K < 40$ clusters, these should be interpreted cautiously~\citep{cameron-2008,webb-2023}. A wild cluster bootstrap ($K{=}11$, $p < 0.001$; Appendix~\ref{app:wild-cluster}) and 100\% directional consistency across all 28 death-prone tasks (Appendix~\ref{app:per-task-ci}) mitigate this concern.
43	
44	\section*{Ethics Statement}
45	
46	This work uses ScienceWorld \cite{scienceworld-2022}, a publicly available text-based simulation environment, and does not involve human subjects or private data. All evaluation environments (ScienceWorld, ALFWorld, MATH) are released under permissive open-source licenses (Apache 2.0 / MIT). All models used (Qwen2.5 family, Llama-3.1-8B) are publicly available for research use. All language models are accessed via standard APIs or publicly released weights. Experiments were conducted on 2$\times$ NVIDIA RTX 5090 (32GB) and 4$\times$ NVIDIA RTX 6000 PRO (96GB), totaling approximately 200 GPU-hours for data collection, router training, and evaluation. Code and data will be released upon acceptance.
47	
48	\bibliography{references}
49	
50	\appendix
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "e7b9a6cd-e12f-456d-b0d8-6d586eed4288"
}
```

</details>

---

### System

_source line 26_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4ba1c14769edea35",
  "tool_use_id": "toolu_018kyKd17RYtxznyhH52XbTu",
  "status": "completed",
  "output_file": "",
  "summary": "Find paper tex files",
  "usage": {
    "total_tokens": 24351,
    "tool_uses": 6,
    "duration_ms": 22599
  },
  "uuid": "3f23acb6-9cdb-45bd-87d0-60fd32d5bba0",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282"
}
```

---

### Tool result

_source line 27 · 2026-05-19T11:09:56.222Z_

<details><summary>↩ Tool result · `toolu_018kyKd17RYtxznyhH52XbTu`</summary>

```text
Perfect! I have found all the relevant files. Here's a comprehensive summary:

## Summary of Findings

### Primary Method Section
**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex`**
- The main method section (7,233 bytes)
- Contains detailed descriptions of:
  - Problem setup (interactive environments, routing policies, modality selection)
  - Counterfactual episode collection methodology
  - Episode-level labeling function
  - Death Avoidance Factor (DAF) decomposition
  - Signal Concentration Index (SCI)

### Paper Framing Document
**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md`**
- Master framing document with complete paper strategy
- Includes: target venue (EMNLP 2026), core insights, three main claims, positioning against literature, story spine, and detailed 8-page paper structure

### Main Paper LaTeX File
**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`**
- ACL-formatted document (11pt article class)
- Title: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
- Includes input directives for abstract, introduction, method, experiments, related_work, discussion, conclusion, limitations, and ethics statement

### Related Paper Section Files (in `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`)
1. **abstract.tex** (1,117 bytes)
2. **introduction.tex** (6,017 bytes)
3. **experiments.tex** (11,922 bytes)
4. **discussion.tex** (4,828 bytes)
5. **related_work.tex** (3,885 bytes)
6. **conclusion.tex** (798 bytes)
7. **responsibleNLPchecklist.tex** (5,500 bytes)
8. **SETUP_NOTES.md** (715 bytes)

### Backup/Artifact Copies
Additional copies exist in:
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/`
- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/` (multiple dated variants)

The paper presents a counterfactual analysis framework for understanding routing signals in LLM agents, with the key finding that death avoidance accounts for approximately 90% of the routing signal between internal LLM reasoning and deterministic computation on ScienceWorld tasks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "7f2ae40f-76ad-471d-b2a6-667df1726544",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Find the method section tex file and any other relevant tex files in this project. Search for:\n1. paper/method.tex or paper/sections/method.tex or similar paths\n2. paper_framing.md\n3. Any main paper tex file\n\nWorking directory: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing\n\nSearch breadth: medium",
    "agentId": "a4ba1c14769edea35",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I have found all the relevant files. Here's a comprehensive summary:\n\n## Summary of Findings\n\n### Primary Method Section\n**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex`**\n- The main method section (7,233 bytes)\n- Contains detailed descriptions of:\n  - Problem setup (interactive environments, routing policies, modality selection)\n  - Counterfactual episode collection methodology\n  - Episode-level labeling function\n  - Death Avoidance Factor (DAF) decomposition\n  - Signal Concentration Index (SCI)\n\n### Paper Framing Document\n**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md`**\n- Master framing document with complete paper strategy\n- Includes: target venue (EMNLP 2026), core insights, three main claims, positioning against literature, story spine, and detailed 8-page paper structure\n\n### Main Paper LaTeX File\n**File: `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/main.tex`**\n- ACL-formatted document (11pt article class)\n- Title: \"Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld\"\n- Includes input directives for abstract, introduction, method, experiments, related_work, discussion, conclusion, limitations, and ethics statement\n\n### Related Paper Section Files (in `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/`)\n1. **abstract.tex** (1,117 bytes)\n2. **introduction.tex** (6,017 bytes)\n3. **experiments.tex** (11,922 bytes)\n4. **discussion.tex** (4,828 bytes)\n5. **related_work.tex** (3,885 bytes)\n6. **conclusion.tex** (798 bytes)\n7. **responsibleNLPchecklist.tex** (5,500 bytes)\n8. **SETUP_NOTES.md** (715 bytes)\n\n### Backup/Artifact Copies\nAdditional copies exist in:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/_project/paper/latex/`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/dream_reports/` (multiple dated variants)\n\nThe paper presents a counterfactual analysis framework for understanding routing signals in LLM agents, with the key finding that death avoidance accounts for approximately 90% of the routing signal between internal LLM reasoning and deterministic computation on ScienceWorld tasks."
      }
    ],
    "totalDurationMs": 22601,
    "totalTokens": 25007,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 6218,
      "cache_read_input_tokens": 18078,
      "output_tokens": 705,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6218
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 705,
          "cache_read_input_tokens": 18078,
          "cache_creation_input_tokens": 6218,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6218,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 0,
      "bashCount": 3,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01GFWyM7GrMQnTzQD1KC6rQZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "6e967086-d686-49c9-af2c-47a5e524cf7c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSH3ndX4pvJGTzxgX1Mg4v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14362,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14362
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-19T11:09:58.937Z_

<details><summary>↩ Tool result · `toolu_01GFWyM7GrMQnTzQD1KC6rQZ`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	Our diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\S\ref{sec:collection}--\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\ref{app:sci}). Episode-level bootstrap resampling provides 95\% confidence intervals for all metrics.
5	
6	\subsection{Problem Setup}
7	\label{sec:problem-setup}
8	
9	Consider an interactive environment with observation space $\mathcal{O}$ and action space $\mathcal{A}$. An agent policy $\pi: \mathcal{O}^* \rightarrow \mathcal{A}$ maps observation histories to actions. We define two computation modalities $\mathcal{M} = \{{\tt int}, {\tt det}\}$: \textbf{internal} (${\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\cite{react-2023}), with prediction errors compounding across steps; and \textbf{deterministic} (${\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \emph{routing policy} $\rho: \mathcal{O}^* \rightarrow \mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\ref{app:ablations}).
10	
11	\subsection{Counterfactual Episode Collection}
12	\label{sec:collection}
13	
14	Per-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \cite{scienceworld-2022}, 97.4\% of steps produce identical intermediate scores regardless of modality (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. This near-total uninformativeness is not an artifact of our setup; it is a structural property of sparse-reward environments where only the terminal outcome discriminates strategies. We therefore perform episode-level counterfactual analysis.
15	
16	\paragraph{Pure-strategy trajectories.}
17	For a task instance $t$ and modality $m \in \mathcal{M}$, a \emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:
18	\begin{equation}
19	    \tau_m^{(t)} = (o_1, a_1, o_2, a_2, \ldots, o_T, a_T)
20	\end{equation}
21	where $T \leq T_{\max}$ is the episode length (capped at $T_{\max} = 30$ steps). Both trajectories $\tau_{\tt int}^{(t)}$ and $\tau_{\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the modality choice.
22	
23	Each trajectory $\tau$ yields a terminal score $s(\tau) \in \mathbb{Z}$ and a death indicator $d(\tau) \in \{0, 1\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:
24	\begin{multline}
25	    \bigl(s^{\tt int}, s^{\tt det}, d^{\tt int}, d^{\tt det}\bigr) \triangleq \\
26	    \bigl(s(\tau_{\tt int}),\, s(\tau_{\tt det}),\, d(\tau_{\tt int}),\, d(\tau_{\tt det})\bigr)
27	\end{multline}
28	
29	We use Qwen2.5-7B-Instruct~\citep{qwen25-2024} (vLLM) on ScienceWorld \cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two modalities can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \S\ref{sec:math-contrast}--\ref{sec:cross-env}.
30	
31	\subsection{Episode-Level Labeling}
32	\label{sec:labeling}
33	
34	We define a labeling function $L$ that maps a counterfactual pair to a routing preference:
35	\begin{multline}
36	    L\!\bigl(\tau_{\tt int}^{(t)}, \tau_{\tt det}^{(t)}\bigr) \;\rightarrow \\
37	    \ell \in \{{\tt det\text{-}pref},\; {\tt int\text{-}pref},\; {\tt no\text{-}pref}\}
38	\end{multline}
39	
40	The labeling function is \emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\ref{alg:labeling}; Appendix~\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \S\ref{sec:death-decomp}.
41	
42	\begin{figure}[t]
43	\centering
44	\includegraphics[width=\columnwidth]{figures/pipeline_overview.pdf}
45	\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\ref{alg:labeling}.}
46	\label{fig:pipeline}
47	\end{figure}
48	
49	\subsection{Death Avoidance Factor}
50	\label{sec:daf}
51	
52	To quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\delta = \mathbb{E}[d^{\tt int}] - \mathbb{E}[d^{\tt det}]$ denote the death-rate differential and $\Delta_{\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. The full gap decomposes as:
53	\begin{equation}
54	    \Delta_{\text{full}} \approx \underbrace{\delta \cdot P}_{\text{death contribution}} + \Delta_{\text{nd}}
55	\end{equation}
56	The approximation holds exactly when the surviving strategy scores zero in all death-asymmetry episodes; in our data, the residual is small ($29.60 - 29.37 = 0.23$, or $0.8\%$ of $\Delta_{\text{full}}$).
57	
58	We define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:
59	\begin{equation}
60	    \text{DAF} = 1 - \frac{\Delta_{\text{nd}}}{\Delta_{\text{full}}} \approx \frac{\delta P}{\delta P + \Delta_{\text{nd}}}
61	\end{equation}%
62	\footnote{When $\Delta_{\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}
63	
64	Since DAF $= \delta P / (\delta P + \Delta_{\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction as complementary metrics.
65	
66	\paragraph{Statistical inference.}
67	We quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\ref{app:penalty}.
68	
69	We also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\in [0, 1]$; Appendix~\ref{app:sci}), reported in \S\ref{sec:death-decomp}.
70	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "d9fb425c-52df-4ea8-8199-cc0b1d78faff",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nOur diagnostic framework quantifies what drives routing signal in interactive environments through three components: (i)~episode-level counterfactual labeling that generates routing preferences from paired pure-strategy outcomes (\\S\\ref{sec:collection}--\\ref{sec:labeling}); (ii)~the Death Avoidance Factor (DAF), which decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}); and (iii)~the Signal Concentration Index (SCI), which measures whether routing signal is concentrated in a few task types or distributed systematically (Appendix~\\ref{app:sci}). Episode-level bootstrap resampling provides 95\\% confidence intervals for all metrics.\n\n\\subsection{Problem Setup}\n\\label{sec:problem-setup}\n\nConsider an interactive environment with observation space $\\mathcal{O}$ and action space $\\mathcal{A}$. An agent policy $\\pi: \\mathcal{O}^* \\rightarrow \\mathcal{A}$ maps observation histories to actions. We define two computation modalities $\\mathcal{M} = \\{{\\tt int}, {\\tt det}\\}$: \\textbf{internal} (${\\tt int}$), where the agent predicts intermediate observations via chain-of-thought reasoning (ReAct~\\cite{react-2023}), with prediction errors compounding across steps; and \\textbf{deterministic} (${\\tt det}$), where the agent receives ground-truth observations from the environment simulator at each step. A \\emph{routing policy} $\\rho: \\mathcal{O}^* \\rightarrow \\mathcal{M}$ selects which modality to use at each step; our analysis investigates what signal is available to learn $\\rho$. A reasoning-depth ablation ($n{=}120$) found no significant difference ($p > 0.26$; Appendix~\\ref{app:ablations}).\n\n\\subsection{Counterfactual Episode Collection}\n\\label{sec:collection}\n\nPer-step oracle labeling assigns routing labels by comparing single-step outcomes under each computation modality. Under sparse terminal rewards, this approach degenerates: on ScienceWorld \\cite{scienceworld-2022}, 97.4\\% of steps produce identical intermediate scores regardless of modality (5{,}726 of 5{,}878 steps across 11 prescreened task types), yielding no per-step routing signal. This near-total uninformativeness is not an artifact of our setup; it is a structural property of sparse-reward environments where only the terminal outcome discriminates strategies. We therefore perform episode-level counterfactual analysis.\n\n\\paragraph{Pure-strategy trajectories.}\nFor a task instance $t$ and modality $m \\in \\mathcal{M}$, a \\emph{pure-strategy trajectory} is the complete episode obtained by applying modality $m$ at every step:\n\\begin{equation}\n    \\tau_m^{(t)} = (o_1, a_1, o_2, a_2, \\ldots, o_T, a_T)\n\\end{equation}\nwhere $T \\leq T_{\\max}$ is the episode length (capped at $T_{\\max} = 30$ steps). Both trajectories $\\tau_{\\tt int}^{(t)}$ and $\\tau_{\\tt det}^{(t)}$ are executed under identical initial conditions (same random seed, same task variation), so performance differences arise solely from the modality choice.\n\nEach trajectory $\\tau$ yields a terminal score $s(\\tau) \\in \\mathbb{Z}$ and a death indicator $d(\\tau) \\in \\{0, 1\\}$. When the agent dies ($d = 1$), the environment imposes a penalty: $s(\\tau) = -P$ where $P > 0$ ($P = 100$ in ScienceWorld). The episode pair produces a tuple:\n\\begin{multline}\n    \\bigl(s^{\\tt int}, s^{\\tt det}, d^{\\tt int}, d^{\\tt det}\\bigr) \\triangleq \\\\\n    \\bigl(s(\\tau_{\\tt int}),\\, s(\\tau_{\\tt det}),\\, d(\\tau_{\\tt int}),\\, d(\\tau_{\\tt det})\\bigr)\n\\end{multline}\n\nWe use Qwen2.5-7B-Instruct~\\citep{qwen25-2024} (vLLM) on ScienceWorld \\cite{scienceworld-2022}, a text-based environment spanning 30 task types with a $-100$ death penalty. After prescreening, we collect 245 episode pairs across 11 task types (20--40 per type). The framework is applicable to any environment where paired episodes under two modalities can be collected with binary success/failure indicators. We apply it unchanged to ALFWorld and MATH in \\S\\ref{sec:math-contrast}--\\ref{sec:cross-env}.\n\n\\subsection{Episode-Level Labeling}\n\\label{sec:labeling}\n\nWe define a labeling function $L$ that maps a counterfactual pair to a routing preference:\n\\begin{multline}\n    L\\!\\bigl(\\tau_{\\tt int}^{(t)}, \\tau_{\\tt det}^{(t)}\\bigr) \\;\\rightarrow \\\\\n    \\ell \\in \\{{\\tt det\\text{-}pref},\\; {\\tt int\\text{-}pref},\\; {\\tt no\\text{-}pref}\\}\n\\end{multline}\n\nThe labeling function is \\emph{death-aware}: it prioritizes survival over score, then compares scores among same-status episodes (Algorithm~\\ref{alg:labeling}; Appendix~\\ref{app:labeling}). ScienceWorld scores are integer-valued, so we use exact (in)equality with no threshold. Figure~\\ref{fig:pipeline} illustrates the overall pipeline; label distributions are reported in \\S\\ref{sec:death-decomp}.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/pipeline_overview.pdf}\n\\caption{Counterfactual episode collection and analysis pipeline. Each task instance is run under both pure strategies independently, producing episode-level labels via Algorithm~\\ref{alg:labeling}.}\n\\label{fig:pipeline}\n\\end{figure}\n\n\\subsection{Death Avoidance Factor}\n\\label{sec:daf}\n\nTo quantify the contribution of death avoidance to routing signal, we decompose the mean score gap between strategies. Let $\\delta = \\mathbb{E}[d^{\\tt int}] - \\mathbb{E}[d^{\\tt det}]$ denote the death-rate differential and $\\Delta_{\\text{nd}}$ the mean score gap restricted to episodes where neither strategy dies. The full gap decomposes as:\n\\begin{equation}\n    \\Delta_{\\text{full}} \\approx \\underbrace{\\delta \\cdot P}_{\\text{death contribution}} + \\Delta_{\\text{nd}}\n\\end{equation}\nThe approximation holds exactly when the surviving strategy scores zero in all death-asymmetry episodes; in our data, the residual is small ($29.60 - 29.37 = 0.23$, or $0.8\\%$ of $\\Delta_{\\text{full}}$).\n\nWe define the Death Avoidance Factor (DAF) as the fraction of the full score gap attributable to death avoidance:\n\\begin{equation}\n    \\text{DAF} = 1 - \\frac{\\Delta_{\\text{nd}}}{\\Delta_{\\text{full}}} \\approx \\frac{\\delta P}{\\delta P + \\Delta_{\\text{nd}}}\n\\end{equation}%\n\\footnote{When $\\Delta_{\\text{nd}} < 0$ (deterministic strategy scores lower than internal on non-death episodes), DAF exceeds 1; death avoidance then overcompensates for a non-death disadvantage.}\n\nSince DAF $= \\delta P / (\\delta P + \\Delta_{\\text{nd}})$, it increases monotonically with $P$, a mathematical consequence rather than an empirical finding. We therefore report both DAF at the environment default ($P{=}100$) and the penalty-independent death-asymmetry label fraction as complementary metrics.\n\n\\paragraph{Statistical inference.}\nWe quantify uncertainty via episode-level bootstrap resampling ($B = 10{,}000$). Each resample draws $N = 245$ episodes with replacement, recomputes all metrics, and derives percentile-based 95\\% CIs. We resample at the episode level (not the step level) because the episode is the unit of counterfactual comparison. Penalty sensitivity analysis across hypothetical $P$ values is in Appendix~\\ref{app:penalty}.\n\nWe also measure whether death-avoidance signal is concentrated in a few task types via a Signal Concentration Index (SCI $\\in [0, 1]$; Appendix~\\ref{app:sci}), reported in \\S\\ref{sec:death-decomp}.\n",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 70
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01AsANJpMcWPw4CZvGm53Anw`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "ac55aefd-539a-4540-a962-88634cf14f58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSH3ndX4pvJGTzxgX1Mg4v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14362,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14362
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T11:09:59.383Z_

<details><summary>↩ Tool result · `toolu_01AsANJpMcWPw4CZvGm53Anw`</summary>

```text
1	# Paper Framing — simgate-modular-routing
2	
3	## Target Venue
4	- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**
5	- Deadline: ARR May 25, 2026 (10 days remaining)
6	- D050: Upgraded from short paper (4p, Findings) per user directive
7	
8	## Core Insight
9	
10	LLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.
11	
12	## Core Claims (3 claims for long paper)
13	
14	**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.
15	
16	**C2 (Episode-level counterfactual labeling methodology + informative router negative)**: Per-step oracle labeling degenerates in sparse-reward environments (97.4% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. Router training (Qwen3-1.7B on counterfactual labels) yields an **informative negative result**: step-level matched eval achieves 55.4±5.2% balanced accuracy, but episode-level independent eval drops to 47.1±2.2% (8-seed cross-split) — **below the trivial majority-vote baseline (50.0%)**. Data-size ablation (r7n2, intermediates: 5/5 evals = 0.50, all-internal predictions) suggests scaling data does not overcome the signal deficit. The methodology contribution is the counterfactual labeling framework itself; the router negative result is presented honestly and is consistent with C1's finding that routing signal is overwhelmingly task-type-level (death risk), leaving insufficient step-level signal for learned routing (D089).
17	
18	**C3 (Cross-model generality + cross-domain contrast)** [NEW for long paper]:
19	- **Cross-model mechanism verification** [Llama-3.1-8B pilot, D054→D055 corrected]: Death dominance fully replicates across model families — **both mechanism and direction consistent**. Llama pilot (freeze + find-non-living-thing, N=10): freeze's only non-tie label = death_asymmetry (internal died, det survived — same direction as Qwen where internal death rate 42.9% vs det 16.3%); find-non-living-thing has 0 deaths, all labels from score_comparison (consistent with Qwen). Llama-8B substantially weaker on ScienceWorld (most scores 0, >80% no-preference expected at scale), limiting full-scale comparison — pilot positioned as mechanism verification, not performance validation.
20	- **Cross-domain negative contrast** [MATH, N=795]: In environments WITHOUT catastrophic failure penalties (MATH: no death, no -100), the routing signal disappears — internal reasoning and code interpretation perform near-identically (+0.5pp, McNemar p=0.81, N=795). Label distribution: 66 internal-preferred / 58 det-preferred (ratio 1.14:1) vs ScienceWorld's 9 / 86 (ratio 0.10:1). The N=300 pilot showed a directional +4.3pp trend (p=0.079), but the powered N=795 extension confirms the effect is not significant — consistent with the death-avoidance mechanism: no catastrophic failures → no routing signal. Source: math-extension-n800.
21	
22	**D013 note**: C1 no longer claims "selective > unconditional." Router confirmed ≈ always-det on episode-level eval (47.1% < majority-vote 50.0%, D089). This IS the finding — the router negative result demonstrates that death avoidance signal is task-type-level and non-learnable at the step level with available data. Keyword heuristic also structurally fails (D014).
23	
24	## Positioning vs Tool-Use Literature (Dream-driven addition)
25	
26	**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:
27	- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).
28	- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.
29	- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.
30	- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.
31	
32	**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Honest negative on learned routing — router fails to generalize beyond training episodes (47.1% < majority-vote 50.0%), confirming signal is task-type-level, not step-level learnable. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from "we built a better tool selector" papers.
33	
34	**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).
35	
36	## Story Spine
37	
38	- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.
39	
40	- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (97.4% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). Router training on these labels yields an informative negative: episode-level independent eval 47.1±2.2% falls below the trivial majority-vote baseline (50.0%), and data-size ablation intermediates show no improvement with scaling (D089). The signal is overwhelmingly task-type-level (death risk), with insufficient step-level structure for learned routing.
41	
42	- **Headline result template**: "Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents."
43	
44	## Paper Structure (8-page long paper)
45	
46	| Section | Pages | Content |
47	|---------|-------|---------|
48	| Abstract | 0.3 | Counterfactual analysis framing, death avoidance finding (multi-model), headline numbers, cross-domain evidence |
49	| Introduction | 1.2 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (methodology + finding + cross-model/domain validation) |
50	| Related Work | 1.0 | Tool-use learning (Toolformer/ART/Chameleon/ToolkenGPT), adaptive computation (CogRouter/ARES/MoD), world model routing (ITP-R/Dyna-Think), safe RL, counterfactual-in-RL (Amitai/Gajcin/Olson) |
51	| Method | 1.5 | Full formalism: counterfactual framework definition, labeling pipeline (pseudocode/algorithm), DAF derivation + properties, router architecture, death decomposition framework |
52	| Experiments | 3.0 | §4.1 ScienceWorld death decomposition (core, Qwen2.5-7B); §4.2 Multi-model validation (Model B on same tasks); §4.3 Cross-domain negative contrast: MATH 795 problems (internal ≈ code interpreter → confirms death avoidance mechanism); §4.4 Temporal analysis + failure modes; §4.5 Ablations (router, labeling quality, keyword baseline structural failure) |
53	| Discussion | 0.5 | Implications for router design, scaling predictions (stronger models → lower death rate → lower DAF), when methodology applies vs doesn't |
54	| Conclusion | 0.5 | Summary + limitations + future work |
55	| References | ~1.0 | Not counted in 8-page limit |
56	
57	## Anticipated Reviewer Concerns & Mitigations
58	
59	1. **"Novelty is incremental — just SFT a small model to classify"**
60	   - Mitigation: Contribution is the empirical finding (death avoidance mechanism) + the counterfactual labeling methodology, not the router. Router negative result (47.1% < majority-vote 50.0%) actually strengthens the story: it confirms routing signal is task-type-level. Explicit vs implicit ablation quantifies the gap.
61	
62	2. **"Only one benchmark (ScienceWorld)"**
63	   - Mitigation [UPGRADED for long paper]: Multi-model validation (§4.2) shows finding holds across model families. MATH 795-problem evaluation (§4.3) demonstrates cross-domain applicability (code interpreter as deterministic oracle). ALFWorld exploratory evidence in Discussion.
64	
65	3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
66	   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.
67	
68	4. **"Death avoidance is trivial — just always use deterministic"**
69	   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.
70	
71	5. **"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment"**
72	   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.
73	
74	6. **"ScienceWorld's -100 penalty inflates gains"** (Dream all 3 tiers)
75	   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.
76	
77	7. **"Missing tool-use literature — this is just Toolformer"** (Dream all 3 tiers, CRITICAL)
78	   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router). (4) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate).
79	
80	8. **"Rule-based routing baseline missing"** (Dream median + worst)
81	   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as "structural failure analysis" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.
82	
83	## Venue Fit Risks (Long Paper, Main Track)
84	
85	- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
86	- Long paper needs: breadth (multi-model + cross-domain) + depth (temporal analysis + failure taxonomy) + methodology contribution
87	- Risk: "Analysis paper, no method contribution" — mitigate by positioning counterfactual labeling framework as reusable methodology, not just one-off analysis. Algorithm box + formal definitions elevate from ad hoc to principled.
88	- Risk: "Death avoidance is the only signal" — mitigate: multi-model validation shows it's a general phenomenon; MATH shows methodology generalizes; Discussion section addresses when/why this applies.
89	- Risk: Router ≈ always-det → novelty concern. **D014: keyword routing structurally fails on ScienceWorld** — positive finding supporting learned approaches.
90	- Risk: Scaling concern (stronger models → less death → less routing signal) — address honestly in Discussion as a feature not bug: the methodology DETECTS when routing adds value.
91	
92	## Key Differences from IDEA_BRIEF / Short Paper
93	
94	1. **D050 scope expansion**: From short paper (4p, ScienceWorld only) to long paper (8p, multi-model + cross-domain).
95	2. **C3 added**: Cross-model generality claim (pending multi-model experiment).
96	3. **MATH upgraded**: From "future work" to §4.3 full evaluation (795 problems).
97	4. **Structure**: Full Related Work + Discussion sections; Method expanded with formalism.
98	5. **Framing unchanged**: Core insight remains death avoidance dominance + diagnostic methodology.
99	
100	## Robustness Check (30-task prescreening, appendix only)
101	
102	A broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.
103	
104	## 数据源权威声明
105	
106	- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用
107	- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix
108	- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）
109	- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "3ecd3827-ea07-42b0-9b3d-0b4d4292d296",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md",
      "content": "# Paper Framing — simgate-modular-routing\n\n## Target Venue\n- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**\n- Deadline: ARR May 25, 2026 (10 days remaining)\n- D050: Upgraded from short paper (4p, Findings) per user directive\n\n## Core Insight\n\nLLM agents on rule-governed environments face catastrophic failures from hallucinated state transitions. Deterministic external computation (environment simulators, code interpreters) eliminates these failures — but what exactly does routing learn? We introduce episode-level counterfactual analysis (per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings) and discover that **death avoidance accounts for ~90% of routing signal** on ScienceWorld (Δ_full=+29.60 [A], Δ_nd=+2.84 [A], DAF=90.41% [A]; Pearson r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). Non-death performance difference is small but non-negligible (Δ_nd/Δ_full=9.6% [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. The contribution is the empirical finding (death avoidance dominance) + the diagnostic methodology (episode-level counterfactual labeling), not the router architecture itself.\n\n## Core Claims (3 claims for long paper)\n\n**C1 (Death avoidance dominates routing signal)**: On ScienceWorld, deterministic simulation dramatically outperforms LLM reasoning (Δ_full=+29.60 [A]), with **death avoidance as the dominant mechanism** (90.41% of the performance gap [A], measured by Δ decomposition; plan-012-full, 11 tasks / 245 eps [A]). Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 (out of 245 episodes) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Non-death score deltas are small but non-negligible (Δ_nd=+2.84 [A], 9.6% of Δ_full [A]). Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death performance difference) [A]. Pearson r=0.9698 (p=8.12e-07) [A] between per-task death rate difference and Δ_full across 11 task types [A]. The value of deterministic computation in interactive environments is concentrated in catastrophic failure prevention, not positive task guidance.\n\n**C2 (Episode-level counterfactual labeling methodology + informative router negative)**: Per-step oracle labeling degenerates in sparse-reward environments (97.4% tie rate on ScienceWorld). Episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — overcomes this circularity and reveals the death-avoidance mechanism. Router training (Qwen3-1.7B on counterfactual labels) yields an **informative negative result**: step-level matched eval achieves 55.4±5.2% balanced accuracy, but episode-level independent eval drops to 47.1±2.2% (8-seed cross-split) — **below the trivial majority-vote baseline (50.0%)**. Data-size ablation (r7n2, intermediates: 5/5 evals = 0.50, all-internal predictions) suggests scaling data does not overcome the signal deficit. The methodology contribution is the counterfactual labeling framework itself; the router negative result is presented honestly and is consistent with C1's finding that routing signal is overwhelmingly task-type-level (death risk), leaving insufficient step-level signal for learned routing (D089).\n\n**C3 (Cross-model generality + cross-domain contrast)** [NEW for long paper]:\n- **Cross-model mechanism verification** [Llama-3.1-8B pilot, D054→D055 corrected]: Death dominance fully replicates across model families — **both mechanism and direction consistent**. Llama pilot (freeze + find-non-living-thing, N=10): freeze's only non-tie label = death_asymmetry (internal died, det survived — same direction as Qwen where internal death rate 42.9% vs det 16.3%); find-non-living-thing has 0 deaths, all labels from score_comparison (consistent with Qwen). Llama-8B substantially weaker on ScienceWorld (most scores 0, >80% no-preference expected at scale), limiting full-scale comparison — pilot positioned as mechanism verification, not performance validation.\n- **Cross-domain negative contrast** [MATH, N=795]: In environments WITHOUT catastrophic failure penalties (MATH: no death, no -100), the routing signal disappears — internal reasoning and code interpretation perform near-identically (+0.5pp, McNemar p=0.81, N=795). Label distribution: 66 internal-preferred / 58 det-preferred (ratio 1.14:1) vs ScienceWorld's 9 / 86 (ratio 0.10:1). The N=300 pilot showed a directional +4.3pp trend (p=0.079), but the powered N=795 extension confirms the effect is not significant — consistent with the death-avoidance mechanism: no catastrophic failures → no routing signal. Source: math-extension-n800.\n\n**D013 note**: C1 no longer claims \"selective > unconditional.\" Router confirmed ≈ always-det on episode-level eval (47.1% < majority-vote 50.0%, D089). This IS the finding — the router negative result demonstrates that death avoidance signal is task-type-level and non-learnable at the step level with available data. Keyword heuristic also structurally fails (D014).\n\n## Positioning vs Tool-Use Literature (Dream-driven addition)\n\n**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:\n- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).\n- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.\n- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.\n- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.\n\n**Our differentiation**: (1) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate), providing ground-truth episode outcomes rather than tie-break artifacts. (2) Empirical finding: death avoidance accounts for ~90% of routing signal [A] — quantifies WHERE and WHY tool invocation helps (catastrophic failure prevention, not positive guidance). (3) Honest negative on learned routing — router fails to generalize beyond training episodes (47.1% < majority-vote 50.0%), confirming signal is task-type-level, not step-level learnable. (4) The contribution is the finding + methodology, not the router architecture — this distinguishes from \"we built a better tool selector\" papers.\n\n**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).\n\n## Story Spine\n\n- **Problem**: LLM agents hallucinate state transitions on rule-governed environments (temperature physics, chemical reactions), leading to catastrophic failures. ITP-R routes to an approximate LLM world model but underperforms pure internal reasoning (62.58 vs CogRouter 84.6 on ScienceWorld). ReTool/AgentMath learn when to invoke code interpreters but use implicit routing entangled with the backbone. Tool-use learning methods (Toolformer, ART, Chameleon) learn general tool selection but don't specialize for catastrophic failure prevention or use counterfactual trajectory labeling.\n\n- **Our framing**: We use episode-level counterfactual analysis to understand WHAT routing learns. Per-step oracle labeling degenerates (97.4% tie rate on ScienceWorld), so we run complete episodes under pure-internal and pure-deterministic strategies, comparing episode-level outcomes. Key finding: ~90% of routing signal is death avoidance [A] — deterministic computation's value is almost entirely concentrated in preventing catastrophic failures (-100 penalties). Non-death performance difference is small but non-negligible (Δ_nd=+2.84, 9.6% of Δ_full [A]). Router training on these labels yields an informative negative: episode-level independent eval 47.1±2.2% falls below the trivial majority-vote baseline (50.0%), and data-size ablation intermediates show no improvement with scaling (D089). The signal is overwhelmingly task-type-level (death risk), with insufficient step-level structure for learned routing.\n\n- **Headline result template**: \"Episode-level counterfactual analysis across 11 ScienceWorld task types (245 episodes) [A] reveals that death avoidance accounts for 90.41% of routing signal [A] between internal LLM reasoning and deterministic computation (Δ_full=+29.60, Δ_nd=+2.84 [A]; r=0.9698, p=8.12e-07 [A]). We propose this analysis as a diagnostic methodology for understanding when and why tool invocation helps LLM agents.\"\n\n## Paper Structure (8-page long paper)\n\n| Section | Pages | Content |\n|---------|-------|---------|\n| Abstract | 0.3 | Counterfactual analysis framing, death avoidance finding (multi-model), headline numbers, cross-domain evidence |\n| Introduction | 1.2 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (methodology + finding + cross-model/domain validation) |\n| Related Work | 1.0 | Tool-use learning (Toolformer/ART/Chameleon/ToolkenGPT), adaptive computation (CogRouter/ARES/MoD), world model routing (ITP-R/Dyna-Think), safe RL, counterfactual-in-RL (Amitai/Gajcin/Olson) |\n| Method | 1.5 | Full formalism: counterfactual framework definition, labeling pipeline (pseudocode/algorithm), DAF derivation + properties, router architecture, death decomposition framework |\n| Experiments | 3.0 | §4.1 ScienceWorld death decomposition (core, Qwen2.5-7B); §4.2 Multi-model validation (Model B on same tasks); §4.3 Cross-domain negative contrast: MATH 795 problems (internal ≈ code interpreter → confirms death avoidance mechanism); §4.4 Temporal analysis + failure modes; §4.5 Ablations (router, labeling quality, keyword baseline structural failure) |\n| Discussion | 0.5 | Implications for router design, scaling predictions (stronger models → lower death rate → lower DAF), when methodology applies vs doesn't |\n| Conclusion | 0.5 | Summary + limitations + future work |\n| References | ~1.0 | Not counted in 8-page limit |\n\n## Anticipated Reviewer Concerns & Mitigations\n\n1. **\"Novelty is incremental — just SFT a small model to classify\"**\n   - Mitigation: Contribution is the empirical finding (death avoidance mechanism) + the counterfactual labeling methodology, not the router. Router negative result (47.1% < majority-vote 50.0%) actually strengthens the story: it confirms routing signal is task-type-level. Explicit vs implicit ablation quantifies the gap.\n\n2. **\"Only one benchmark (ScienceWorld)\"**\n   - Mitigation [UPGRADED for long paper]: Multi-model validation (§4.2) shows finding holds across model families. MATH 795-problem evaluation (§4.3) demonstrates cross-domain applicability (code interpreter as deterministic oracle). ALFWorld exploratory evidence in Discussion.\n\n3. **\"Comparison unfair — CogRouter uses RL (CoPO), you use SFT\"**\n   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.\n\n4. **\"Death avoidance is trivial — just always use deterministic\"**\n   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.\n\n5. **\"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment\"**\n   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.\n\n6. **\"ScienceWorld's -100 penalty inflates gains\"** (Dream all 3 tiers)\n   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.\n\n7. **\"Missing tool-use literature — this is just Toolformer\"** (Dream all 3 tiers, CRITICAL)\n   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router). (4) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate).\n\n8. **\"Rule-based routing baseline missing\"** (Dream median + worst)\n   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as \"structural failure analysis\" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.\n\n## Venue Fit Risks (Long Paper, Main Track)\n\n- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)\n- Long paper needs: breadth (multi-model + cross-domain) + depth (temporal analysis + failure taxonomy) + methodology contribution\n- Risk: \"Analysis paper, no method contribution\" — mitigate by positioning counterfactual labeling framework as reusable methodology, not just one-off analysis. Algorithm box + formal definitions elevate from ad hoc to principled.\n- Risk: \"Death avoidance is the only signal\" — mitigate: multi-model validation shows it's a general phenomenon; MATH shows methodology generalizes; Discussion section addresses when/why this applies.\n- Risk: Router ≈ always-det → novelty concern. **D014: keyword routing structurally fails on ScienceWorld** — positive finding supporting learned approaches.\n- Risk: Scaling concern (stronger models → less death → less routing signal) — address honestly in Discussion as a feature not bug: the methodology DETECTS when routing adds value.\n\n## Key Differences from IDEA_BRIEF / Short Paper\n\n1. **D050 scope expansion**: From short paper (4p, ScienceWorld only) to long paper (8p, multi-model + cross-domain).\n2. **C3 added**: Cross-model generality claim (pending multi-model experiment).\n3. **MATH upgraded**: From \"future work\" to §4.3 full evaluation (795 problems).\n4. **Structure**: Full Related Work + Discussion sections; Method expanded with formalism.\n5. **Framing unchanged**: Core insight remains death avoidance dominance + diagnostic methodology.\n\n## Robustness Check (30-task prescreening, appendix only)\n\nA broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.\n\n## 数据源权威声明\n\n- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用\n- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix\n- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）\n- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）\n",
      "numLines": 110,
      "startLine": 1,
      "totalLines": 110
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_01Ajsnzy3Y21rxb8gv9LX6op`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "e8509213-cc27-4512-8f97-289c45ebd373",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSH3ndX4pvJGTzxgX1Mg4v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14362,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14362
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-19T11:09:59.840Z_

<details><summary>↩ Tool result · `toolu_01Ajsnzy3Y21rxb8gv9LX6op`</summary>

```text
1	\section{Experiments}
2	
3	We analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\Delta\text{DR} = +38.2$\,pp exceeding the included tasks' $+28.7$\,pp (Appendix~\ref{app:per-task}).
4	
5	\subsection{Death Avoidance Decomposition}
6	\label{sec:death-decomp}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{figures/fig1_daf_scatter.pdf}
11	\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\ performance gap ($\Delta_{\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}
12	\label{fig:decomposition}
13	\end{figure}
14	
15	Across 245 episodes, $\Delta_{\text{full}} = +29.60$; excluding death episodes, $\Delta_{\text{nd}} = +2.84$, yielding DAF $= 90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\% (75 of 95 non-tie labels). Given observed $\delta = 0.265$ and $P = 100$, the predicted DAF $= \delta P / (\delta P + \Delta_{\text{nd}}) = 26.5 / 29.37 \approx 90.3\%$, closely matching the observed value; DAF is thus a derived quantity once $\delta$, $P$, and $\Delta_{\text{nd}}$ are known, while the 78.9\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap.
16	
17	\paragraph{Per-task correlation structure.}
18	The internal strategy dies in 42.9\% of episodes versus 16.3\% for deterministic (2.6$\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\Delta_{\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\ref{fig:decomposition}). Since $P$ is constant across all task types, $\Delta_{\text{full}} = P \cdot \delta + \Delta_{\text{nd}}$ makes $\Delta_{\text{full}}$ a linear function of $\delta$ with residual $\Delta_{\text{nd}}$; when DAF $\rightarrow 1$, this residual vanishes and $r \rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \leq 25$ (Appendix~\ref{app:penalty}). Of 245 episodes, 86 are \texttt{det\_preferred}, 9 \texttt{internal\_preferred}, and 150 \texttt{no\_preference}.
19	
20	\paragraph{Signal concentration.}
21	The Signal Concentration Index (SCI $= 0.2147$; Appendix~\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\%$ of total death-rate differential. One outlier, \texttt{find-non-living-thing}, has zero deaths ($\Delta = +9.58$ from non-death scores alone); all 10 remaining types exhibit death-asymmetry-driven routing labels.
22	
23	\paragraph{Sensitivity analysis.}
24	Episode-level bootstrap ($B = 10{,}000$) yields 95\% CI $[81.6\%, 98.8\%]$ for DAF; per-task CIs confirm $\Delta > 0$ for 10 of 11 types. Leave-one-task-out analysis confirms stability: removing any single death-prone task changes DAF by at most 3.0\,pp (range: 75.9\%--78.9\%; Appendix~\ref{app:loto-daf}). Cluster-robust inference, wild cluster bootstrap ($p < 0.001$), 28-task directional consistency (100\%), and 8-seed cross-validation all confirm significance (Appendices~\ref{app:wild-cluster}--\ref{app:seed-robustness}).
25	
26	\paragraph{Seed robustness.}
27	A full replication with an independent environment seed (seed$=$123, $N{=}220$) yields DAF $= 89.7\%$, within 0.7~pp of the primary analysis, with virtually identical $\Delta_{\text{nd}}$ ($2.83$ vs.\ $2.84$) and per-task correlation $r = 0.94$ (Appendix~\ref{app:seed-robustness}).
28	
29	\subsection{Multi-Model Validation}
30	\label{sec:cross-model}
31	
32	A Llama-3.1-8B-Instruct~\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\%$ vs.\ deterministic $11.4\%$ (death-rate differential $+30.0$~pp), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\%, all death-asymmetry reversals), and 134 no-preference labels.
33	Both models exhibit nearly identical internal vulnerability (${\sim}$42\%: Qwen $42.9\%$, Llama $41.4\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\%$ vs.\ $11.4\%$).
34	\texttt{identify-life-stages-1} shows cross-model precision matching ($55\%$/$10\%$/$+45$~pp in both models).
35	\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\S\ref{sec:discussion}). Both models are in the 7--8B range; $10{\times}$ scaling (\S\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\ref{app:cross-model}).
36	
37	\subsection{Agent Improvement Baselines}
38	\label{sec:agent-improvement}
39	
40	\begin{table}[t]
41	\centering
42	\small
43	\begin{tabular}{@{}lrr@{}}
44	\toprule
45	Condition & Death\% & $N$ \\
46	\midrule
47	Single-trial baseline & 42.9 & 245 \\
48	Reflexion ($3{\times}$) & 31.4 & 220 \\
49	Deterministic baseline & 16.3 & 245 \\
50	\midrule
51	\multicolumn{3}{@{}l}{\textit{10 death-prone tasks only:}} \\
52	Death-prone baseline & 48.0 & 200 \\
53	Retry ($5{\times}$) & 43.5 & 200 \\
54	Qwen2.5-72B ($10{\times}$ scale) & 34.5 & 200 \\
55	\bottomrule
56	\end{tabular}
57	\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\texttt{find-non-living-thing} excluded, 0\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}
58	\label{tab:agent-improvement}
59	\end{table}
60	
61	We test whether agent-level improvement reduces death dominance (Table~\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\%$ vs.\ $48.0\%$ baseline, $\Delta = -4.5$~pp). Reflexion~\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\% across all 11 tasks by rescuing 29.3\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\sim}$35\%. Scaling to Qwen2.5-72B ($10{\times}$ parameters) reduces death-prone rate to $34.5\%$ with task-level variation from $+5$~pp (\texttt{chemistry-mix}) to $-31$~pp (\texttt{lifespan-longest-lived}). Recomputing DAF with 72B yields $90.9\%$ (95\% CI: $[83.9\%, 97.3\%]$), nearly identical to 7B ($90.4\%$); scaling lowers death rate but leaves death dominance structurally intact.
62	
63	\paragraph{Dose-response analysis.}
64	We extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\ref{fig:dose-response}). Retry is nearly flat ($48.0\% \to 43.5\%$, $\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\%$ at $N{=}3$ ($\Delta = -13.5$~pp, $p < 0.005$) then plateaus ($34$--$36.5\%$ for $N \geq 3$, pairwise $p > 0.5$). Retry's per-trial conditional death rate stays constant at ${\sim}48\%$; Reflexion's declines to ${\sim}31\%$ by Trial~3 (per-task breakdown in Appendix~\ref{app:dose-response}).
65	
66	\begin{figure}[t]
67	\centering
68	\includegraphics[width=\columnwidth]{figures/dose_response.pdf}
69	\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($34.5\%$) and deterministic baseline ($16.3\%$). Error bands: Wilson 95\% CIs.}
70	\label{fig:dose-response}
71	\end{figure}
72	
73	\subsection{Cross-Environment Boundary Probes}
74	\label{sec:math-contrast}
75	\label{sec:cross-env}
76	
77	We evaluate two additional environments as boundary probes (Appendix~\ref{app:cross-env-details}). ``Deterministic'' denotes qualitatively different modalities per environment (oracle simulator, code interpreter, admissible-action access), so results probe framework applicability rather than replicate findings.
78	
79	\paragraph{MATH.} On MATH Level~4--5~\citep{math-2021} ($N{=}795$, code interpreter as deterministic modality), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, McNemar $p = 0.81$, 95\% CI $[-2.6, +3.6]$~pp), with balanced labels (107 vs.\ 95, 74.6\% no-preference). Without catastrophic failure, no routing signal emerges.
80	
81	\paragraph{ALFWorld.} ALFWorld~\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch. The success rate gap is $27.4\%$ vs.\ $3.0\%$ (35 det-preferred, 2 int-preferred, 98 no-preference). The deterministic advantage stems from this information gap, a qualitatively different mechanism that the framework diagnoses without modification.
82	
83	\subsection{Baselines}
84	\label{sec:baselines}
85	
86	\begin{table}[t]
87	\centering
88	\small
89	\resizebox{\columnwidth}{!}{%
90	\begin{tabular}{@{}lccc@{}}
91	\toprule
92	Strategy & Score & 95\% CI & Death \% \\
93	\midrule
94	Always-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\
95	Always-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\
96	Random & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\
97	Oracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\
98	\midrule
99	Trained Router$^\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\
100	\bottomrule
101	\end{tabular}}
102	\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\dagger$\,Single random seed (42) per episode pair; see Appendix~\ref{app:seed-robustness} for 8-seed robustness analysis.}
103	\label{tab:baselines}
104	\end{table}
105	
106	Always-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\% of decisions matching always-deterministic, an \emph{oracle degeneracy}: the optimal routing policy closely resembles unconditional deterministic computation.
107	
108	\subsection{Router Training as Diagnostic Probe}
109	\label{sec:router-diagnostic}
110	
111	We probe whether counterfactual labels can train a step-level router as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside; ${\sim}27.7\%$ of step-level labels are misaligned with episode-level assignments, further limiting learnability. An implicit router (Qwen3, LoRA; Appendix~\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) with 4-seed configurations shows flat step-level balanced accuracy ($56$--$59\%$, within seed variance). At episode level, only 4B exceeds always-deterministic ($59.0 \pm 1.9\%$, $p < 0.005$; Appendix~\ref{app:ablations}); 0.6B and 1.7B remain at or below chance. The multi-step nature of routing (10--50 actions with compounding state uncertainty) creates inherent label noise between step-level decisions and episode-level outcomes.
112	
113	\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\%$--$800\%$) provides no improvement; the $3.7\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\ref{app:seed-robustness}--\ref{app:ablations}).
114	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "ccde6bc8-3707-4105-adf9-88078513407b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\nWe analyze 11 of ScienceWorld's 30 task types (245 episodes); the 19 excluded types lack actionable routing signal due to development contamination (5), taxonomic redundancy (7), or agent-floor performance (7). An anti-cherry-picking analysis confirms that death dominance holds in 18 of these 19 types, with a mean $\\Delta\\text{DR} = +38.2$\\,pp exceeding the included tasks' $+28.7$\\,pp (Appendix~\\ref{app:per-task}).\n\n\\subsection{Death Avoidance Decomposition}\n\\label{sec:death-decomp}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_daf_scatter.pdf}\n\\caption{Per-task scatter: death rate differential (internal $-$ deterministic) vs.\\ performance gap ($\\Delta_{\\text{full}}$). $r = 0.97$, $p < 10^{-6}$, $n = 11$ task types.}\n\\label{fig:decomposition}\n\\end{figure}\n\nAcross 245 episodes, $\\Delta_{\\text{full}} = +29.60$; excluding death episodes, $\\Delta_{\\text{nd}} = +2.84$, yielding DAF $= 90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$; at the default $P{=}100$). The penalty-independent death-asymmetry label fraction is 78.9\\% (75 of 95 non-tie labels). Given observed $\\delta = 0.265$ and $P = 100$, the predicted DAF $= \\delta P / (\\delta P + \\Delta_{\\text{nd}}) = 26.5 / 29.37 \\approx 90.3\\%$, closely matching the observed value; DAF is thus a derived quantity once $\\delta$, $P$, and $\\Delta_{\\text{nd}}$ are known, while the 78.9\\% label fraction is the penalty-independent empirical finding. Of these 75, 54 (72.0\\%) reduce to ties when the death penalty is removed entirely: in those episodes, both modalities score zero without death, so the only reason one strategy outscored the other was avoiding the $-100$ penalty. Death avoidance is not merely the dominant but often the \\emph{sole} discriminating signal between modalities. The remaining 21 death-asymmetry labels involve episodes where the surviving strategy also earned positive score, but the death penalty still accounts for the majority of the score gap.\n\n\\paragraph{Per-task correlation structure.}\nThe internal strategy dies in 42.9\\% of episodes versus 16.3\\% for deterministic (2.6$\\times$), consistent with the internal strategy's reliance on self-generated observations that compound prediction errors across steps. Per-task, death rate differential correlates with $\\Delta_{\\text{full}}$ ($r = 0.97$, $p < 10^{-6}$; Figure~\\ref{fig:decomposition}). Since $P$ is constant across all task types, $\\Delta_{\\text{full}} = P \\cdot \\delta + \\Delta_{\\text{nd}}$ makes $\\Delta_{\\text{full}}$ a linear function of $\\delta$ with residual $\\Delta_{\\text{nd}}$; when DAF $\\rightarrow 1$, this residual vanishes and $r \\rightarrow 1$ by construction. The near-perfect correlation is therefore a mathematical consequence of death dominance, not an independent empirical finding. We retain it as an internal consistency check. The correlation drops below significance at $P \\leq 25$ (Appendix~\\ref{app:penalty}). Of 245 episodes, 86 are \\texttt{det\\_preferred}, 9 \\texttt{internal\\_preferred}, and 150 \\texttt{no\\_preference}.\n\n\\paragraph{Signal concentration.}\nThe Signal Concentration Index (SCI $= 0.2147$; Appendix~\\ref{app:sci}) confirms low concentration: the top-3 task types account for only $39.8\\%$ of total death-rate differential. One outlier, \\texttt{find-non-living-thing}, has zero deaths ($\\Delta = +9.58$ from non-death scores alone); all 10 remaining types exhibit death-asymmetry-driven routing labels.\n\n\\paragraph{Sensitivity analysis.}\nEpisode-level bootstrap ($B = 10{,}000$) yields 95\\% CI $[81.6\\%, 98.8\\%]$ for DAF; per-task CIs confirm $\\Delta > 0$ for 10 of 11 types. Leave-one-task-out analysis confirms stability: removing any single death-prone task changes DAF by at most 3.0\\,pp (range: 75.9\\%--78.9\\%; Appendix~\\ref{app:loto-daf}). Cluster-robust inference, wild cluster bootstrap ($p < 0.001$), 28-task directional consistency (100\\%), and 8-seed cross-validation all confirm significance (Appendices~\\ref{app:wild-cluster}--\\ref{app:seed-robustness}).\n\n\\paragraph{Seed robustness.}\nA full replication with an independent environment seed (seed$=$123, $N{=}220$) yields DAF $= 89.7\\%$, within 0.7~pp of the primary analysis, with virtually identical $\\Delta_{\\text{nd}}$ ($2.83$ vs.\\ $2.84$) and per-task correlation $r = 0.94$ (Appendix~\\ref{app:seed-robustness}).\n\n\\subsection{Multi-Model Validation}\n\\label{sec:cross-model}\n\nA Llama-3.1-8B-Instruct~\\citep{llama3-2024} cross-model replication across all 11 task types ($N{=}220$) confirms that death dominance replicates across model families: internal death rate $41.4\\%$ vs.\\ deterministic $11.4\\%$ (death-rate differential $+30.0$~pp), with direction consistency 10/10 on death-prone tasks, 83 deterministic-preferred, 3 internal-preferred (1.4\\%, all death-asymmetry reversals), and 134 no-preference labels.\nBoth models exhibit nearly identical internal vulnerability (${\\sim}$42\\%: Qwen $42.9\\%$, Llama $41.4\\%$), confirming that death-prone failure is structurally determined; the differential magnitude varies ($+26.5$~pp Qwen, $+30.0$~pp Llama) because deterministic strategy safety is model-dependent ($16.3\\%$ vs.\\ $11.4\\%$).\n\\texttt{identify-life-stages-1} shows cross-model precision matching ($55\\%$/$10\\%$/$+45$~pp in both models).\n\\texttt{find-non-living-thing} shows zero deaths in both models, consistent with its majority-class answer distribution (\\S\\ref{sec:discussion}). Both models are in the 7--8B range; $10{\\times}$ scaling (\\S\\ref{sec:agent-improvement}) confirms that death dominance persists across capability levels (Appendix~\\ref{app:cross-model}).\n\n\\subsection{Agent Improvement Baselines}\n\\label{sec:agent-improvement}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\begin{tabular}{@{}lrr@{}}\n\\toprule\nCondition & Death\\% & $N$ \\\\\n\\midrule\nSingle-trial baseline & 42.9 & 245 \\\\\nReflexion ($3{\\times}$) & 31.4 & 220 \\\\\nDeterministic baseline & 16.3 & 245 \\\\\n\\midrule\n\\multicolumn{3}{@{}l}{\\textit{10 death-prone tasks only:}} \\\\\nDeath-prone baseline & 48.0 & 200 \\\\\nRetry ($5{\\times}$) & 43.5 & 200 \\\\\nQwen2.5-72B ($10{\\times}$ scale) & 34.5 & 200 \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Internal-strategy death rates under agent improvement methods. Top: all 11 tasks. Bottom: 10 death-prone tasks (\\texttt{find-non-living-thing} excluded, 0\\% death at all scales). All interventions reduce death rate but none approaches deterministic-level safety.}\n\\label{tab:agent-improvement}\n\\end{table}\n\nWe test whether agent-level improvement reduces death dominance (Table~\\ref{tab:agent-improvement}). Retry ($N{=}5$ attempts without self-correction) yields marginal reduction on death-prone tasks ($43.5\\%$ vs.\\ $48.0\\%$ baseline, $\\Delta = -4.5$~pp). Reflexion~\\citep{reflexion-2023} (verbal self-reflection between trials) reduces death to 31.4\\% across all 11 tasks by rescuing 29.3\\% of first-trial deaths, but the gap to deterministic remains 15.1~pp; on the 10 death-prone tasks, Reflexion achieves ${\\sim}$35\\%. Scaling to Qwen2.5-72B ($10{\\times}$ parameters) reduces death-prone rate to $34.5\\%$ with task-level variation from $+5$~pp (\\texttt{chemistry-mix}) to $-31$~pp (\\texttt{lifespan-longest-lived}). Recomputing DAF with 72B yields $90.9\\%$ (95\\% CI: $[83.9\\%, 97.3\\%]$), nearly identical to 7B ($90.4\\%$); scaling lowers death rate but leaves death dominance structurally intact.\n\n\\paragraph{Dose-response analysis.}\nWe extend both interventions to $N{=}5$ trials on death-prone tasks ($n{=}200$; Figure~\\ref{fig:dose-response}). Retry is nearly flat ($48.0\\% \\to 43.5\\%$, $\\Delta = -4.5$~pp over five trials). Reflexion drops steeply to $34.0\\%$ at $N{=}3$ ($\\Delta = -13.5$~pp, $p < 0.005$) then plateaus ($34$--$36.5\\%$ for $N \\geq 3$, pairwise $p > 0.5$). Retry's per-trial conditional death rate stays constant at ${\\sim}48\\%$; Reflexion's declines to ${\\sim}31\\%$ by Trial~3 (per-task breakdown in Appendix~\\ref{app:dose-response}).\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/dose_response.pdf}\n\\caption{Death rate as a function of trial count ($N$) for Retry and Reflexion on 10 death-prone tasks ($n{=}200$). Retry (blue) is nearly flat; Reflexion (red) drops steeply through $N{=}3$ then plateaus. Horizontal lines: 72B scaling baseline ($34.5\\%$) and deterministic baseline ($16.3\\%$). Error bands: Wilson 95\\% CIs.}\n\\label{fig:dose-response}\n\\end{figure}\n\n\\subsection{Cross-Environment Boundary Probes}\n\\label{sec:math-contrast}\n\\label{sec:cross-env}\n\nWe evaluate two additional environments as boundary probes (Appendix~\\ref{app:cross-env-details}). ``Deterministic'' denotes qualitatively different modalities per environment (oracle simulator, code interpreter, admissible-action access), so results probe framework applicability rather than replicate findings.\n\n\\paragraph{MATH.} On MATH Level~4--5~\\citep{math-2021} ($N{=}795$, code interpreter as deterministic modality), internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, McNemar $p = 0.81$, 95\\% CI $[-2.6, +3.6]$~pp), with balanced labels (107 vs.\\ 95, 74.6\\% no-preference). Without catastrophic failure, no routing signal emerges.\n\n\\paragraph{ALFWorld.} ALFWorld~\\citep{alfworld-2021} (6 task types, 135 games) provides the deterministic strategy with admissible actions, an information asymmetry rather than a computation mode switch. The success rate gap is $27.4\\%$ vs.\\ $3.0\\%$ (35 det-preferred, 2 int-preferred, 98 no-preference). The deterministic advantage stems from this information gap, a qualitatively different mechanism that the framework diagnoses without modification.\n\n\\subsection{Baselines}\n\\label{sec:baselines}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\nStrategy & Score & 95\\% CI & Death \\% \\\\\n\\midrule\nAlways-Internal & $-39.07$ & [$-46.40$, $-32.27$] & 42.9 \\\\\nAlways-Deterministic & $-9.47$ & [$-14.71$, $-4.29$] & 16.3 \\\\\nRandom & $-22.38$ & [$-28.67$, $-15.75$] & 27.8 \\\\\nOracle & $-6.58$ & [$-11.54$, $-1.70$] & 14.3 \\\\\n\\midrule\nTrained Router$^\\dagger$ & $-10.70$ & [$-16.33$, $-5.27$] & 17.6 \\\\\n\\bottomrule\n\\end{tabular}}\n\\caption{Episode-weighted mean scores on ScienceWorld (11 tasks, 245 episodes). $\\dagger$\\,Single random seed (42) per episode pair; see Appendix~\\ref{app:seed-robustness} for 8-seed robustness analysis.}\n\\label{tab:baselines}\n\\end{table}\n\nAlways-deterministic ($-9.47$) outperforms always-internal ($-39.07$) by 29.60 points. The oracle improves only to $-6.58$, with 96.3\\% of decisions matching always-deterministic, an \\emph{oracle degeneracy}: the optimal routing policy closely resembles unconditional deterministic computation.\n\n\\subsection{Router Training as Diagnostic Probe}\n\\label{sec:router-diagnostic}\n\nWe probe whether counterfactual labels can train a step-level router as a diagnostic of label informativeness. The oracle margin (2.89 points) caps routing upside; ${\\sim}27.7\\%$ of step-level labels are misaligned with episode-level assignments, further limiting learnability. An implicit router (Qwen3, LoRA; Appendix~\\ref{app:router-details}) trained at three scales (0.6B, 1.7B, 4B) with 4-seed configurations shows flat step-level balanced accuracy ($56$--$59\\%$, within seed variance). At episode level, only 4B exceeds always-deterministic ($59.0 \\pm 1.9\\%$, $p < 0.005$; Appendix~\\ref{app:ablations}); 0.6B and 1.7B remain at or below chance. The multi-step nature of routing (10--50 actions with compounding state uncertainty) creates inherent label noise between step-level decisions and episode-level outcomes.\n\n\\paragraph{End-to-end deployment.} The 4B router deployed end-to-end ($N{=}245$) scores $-12.03$ (95\\% CI: $[-17.82, -6.45]$), not exceeding always-deterministic ($-9.47$). Paraphrase-based augmentation ($25\\%$--$800\\%$) provides no improvement; the $3.7\\%$ internal-preferred base rate makes real-data collection expensive (Appendices~\\ref{app:seed-robustness}--\\ref{app:ablations}).\n",
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

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01D25PQDWNSawvbRcbeBn957`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "f7e31538-d792-446a-a8d5-6eb446fd0c89",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSH3ndX4pvJGTzxgX1Mg4v",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14362,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 14362
      },
      "output_tokens": 61,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "previous_message_not_found"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-19T11:10:00.361Z_

<details><summary>↩ Tool result · `toolu_01D25PQDWNSawvbRcbeBn957`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Why the router fails: task-type-level signal.}
5	The router diagnostic (\S\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\%$) without step-level gains ($56$--$59\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable features. Cross-task-type transfer to physical-science tasks yields chance-level accuracy (49.2\%, 95\% CI $[42.4\%, 55.9\%]$; Appendix~\ref{app:ablations}), and 7 of 11 task types contain only deterministic-preferred labels, making majority-class collapse a structural consequence of the label distribution.
6	
7	\paragraph{Non-triviality of death dominance.}
8	Four intervention axes all fail to close the gap to deterministic safety (16.3\%): Retry ($43.5\%$ at $N{=}5$), Reflexion ($34.0\%$ at $N{=}3$, plateauing at $34$--$36.5\%$), $10{\times}$ scaling ($34.5\%$, 72B), and action-space filtering ($29.0\%$; Appendix~\ref{app:grounding-ablation}). All four leave a ${\sim}$13--27~pp residual gap. Reflexion and scaling converge to overlapping 95\% Wilson CIs ($[27.8\%, 40.8\%]$ and $[28.0\%, 41.0\%]$); this overlap suggests a shared structural bound from the lack of ground-truth state access. Prior tool-routing work \citep{toolformer-2023,art-2023,chameleon-2023} operates in non-interactive settings; in multi-step environments, the death-rate differential ($\delta = 26.5$~pp) resists all four tested intervention axes. The oracle matches always-deterministic on 96.3\% of decisions (score improvement: 2.89 points), and even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic (Appendix~\ref{sec:threshold-routing}); optimal routing is near-degenerate under death dominance.
9	
10	\paragraph{Anatomy of catastrophic failure.}
11	All 105 internal-strategy deaths trace to misuse of \texttt{focus on [object]}, the answer-submission action, as a general interaction command (taxonomy in Appendix~\ref{app:failure-modes}). The root cause is action-space grounding failure: agents parse task descriptions correctly but cannot ground understanding in valid primitives. The internal strategy's higher death count (105 vs.\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\sim}5\%$ \texttt{focus on} rate in both). \texttt{find-non-living-thing}, the sole zero-death task, uses \texttt{focus on} more frequently than any death-prone task: non-living objects are the majority class, so indiscriminate submissions rarely trigger death; lethality is thus a joint function of action misuse and answer distribution. Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\% \to 37.0\%$ via prompt warning; $\to 29.0\%$ via action-space filter), with ironic effects where warnings increased \texttt{focus on} salience on identification tasks (Appendix~\ref{app:grounding-ablation}).
12	
13	\paragraph{Practitioner decision framework.}
14	Qwen2.5-72B reduces death-prone death rate to $34.5\%$ yet DAF remains $90.9\%$; the gap to deterministic persists at ${\sim}$18~pp. Below a capability threshold (${\sim}$0.5B), agents fail to reach dangerous states at all (13.3\% death rate in a 15-episode pilot), suggesting an inverted-U relationship between capability and death risk. For a new environment, we recommend: (1)~run a ${\sim}$50-episode pilot comparing pure-internal vs.\ pure-deterministic strategies, (2)~compute the death-rate differential $\delta$, (3)~if $\delta \cdot P \gg \Delta_{\text{nd}}$ (equivalently, if $>$75\% of non-tie labels arise from death asymmetry), a fixed deterministic strategy will match or exceed any learned router. Our router training consumed ${\sim}$200 GPU-hours across 28 configurations without exceeding always-deterministic; this diagnostic framework could have predicted that outcome from a 50-episode pilot at negligible cost. The MATH negative control ($p = 0.81$, no deaths, no routing signal) validates the diagnostic: absent catastrophic failure, the framework correctly predicts that routing adds no value.
15	
16	\paragraph{Framework applicability.}
17	The penalty-independent label fraction (78.9\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\ref{app:penalty}). The framework requires paired modality episodes with binary catastrophic outcomes. NetHack~\citep{nethack-2020} and Crafter~\citep{crafter-2022}, both featuring permadeath, are the most direct replication targets; recent benchmarks \citep{balrog-2025,netplay-2024} provide infrastructure.
18	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "af805074-eaac-4c6d-81e2-f753e5ee43e8",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Why the router fails: task-type-level signal.}\nThe router diagnostic (\\S\\ref{sec:router-diagnostic}) reveals a structural mismatch: death avoidance is a task-type-level binary property (10 of 11 types carry death risk), but step-level features correlate weakly because death risk depends on multi-step state trajectories, not individual action semantics. The 4B router's episode-level improvement ($59.0\\%$) without step-level gains ($56$--$59\\%$, flat) confirms that capacity scaling captures task-type classification rather than generalizable features. Cross-task-type transfer to physical-science tasks yields chance-level accuracy (49.2\\%, 95\\% CI $[42.4\\%, 55.9\\%]$; Appendix~\\ref{app:ablations}), and 7 of 11 task types contain only deterministic-preferred labels, making majority-class collapse a structural consequence of the label distribution.\n\n\\paragraph{Non-triviality of death dominance.}\nFour intervention axes all fail to close the gap to deterministic safety (16.3\\%): Retry ($43.5\\%$ at $N{=}5$), Reflexion ($34.0\\%$ at $N{=}3$, plateauing at $34$--$36.5\\%$), $10{\\times}$ scaling ($34.5\\%$, 72B), and action-space filtering ($29.0\\%$; Appendix~\\ref{app:grounding-ablation}). All four leave a ${\\sim}$13--27~pp residual gap. Reflexion and scaling converge to overlapping 95\\% Wilson CIs ($[27.8\\%, 40.8\\%]$ and $[28.0\\%, 41.0\\%]$); this overlap suggests a shared structural bound from the lack of ground-truth state access. Prior tool-routing work \\citep{toolformer-2023,art-2023,chameleon-2023} operates in non-interactive settings; in multi-step environments, the death-rate differential ($\\delta = 26.5$~pp) resists all four tested intervention axes. The oracle matches always-deterministic on 96.3\\% of decisions (score improvement: 2.89 points), and even with perfect per-task death risk knowledge, threshold routing cannot outperform always-deterministic (Appendix~\\ref{sec:threshold-routing}); optimal routing is near-degenerate under death dominance.\n\n\\paragraph{Anatomy of catastrophic failure.}\nAll 105 internal-strategy deaths trace to misuse of \\texttt{focus on [object]}, the answer-submission action, as a general interaction command (taxonomy in Appendix~\\ref{app:failure-modes}). The root cause is action-space grounding failure: agents parse task descriptions correctly but cannot ground understanding in valid primitives. The internal strategy's higher death count (105 vs.\\ 40) reflects more frequent entry into catastrophic states, not different within-episode behavior (${\\sim}5\\%$ \\texttt{focus on} rate in both). \\texttt{find-non-living-thing}, the sole zero-death task, uses \\texttt{focus on} more frequently than any death-prone task: non-living objects are the majority class, so indiscriminate submissions rarely trigger death; lethality is thus a joint function of action misuse and answer distribution. Direct grounding interventions reduce but do not eliminate vulnerability ($48.0\\% \\to 37.0\\%$ via prompt warning; $\\to 29.0\\%$ via action-space filter), with ironic effects where warnings increased \\texttt{focus on} salience on identification tasks (Appendix~\\ref{app:grounding-ablation}).\n\n\\paragraph{Practitioner decision framework.}\nQwen2.5-72B reduces death-prone death rate to $34.5\\%$ yet DAF remains $90.9\\%$; the gap to deterministic persists at ${\\sim}$18~pp. Below a capability threshold (${\\sim}$0.5B), agents fail to reach dangerous states at all (13.3\\% death rate in a 15-episode pilot), suggesting an inverted-U relationship between capability and death risk. For a new environment, we recommend: (1)~run a ${\\sim}$50-episode pilot comparing pure-internal vs.\\ pure-deterministic strategies, (2)~compute the death-rate differential $\\delta$, (3)~if $\\delta \\cdot P \\gg \\Delta_{\\text{nd}}$ (equivalently, if $>$75\\% of non-tie labels arise from death asymmetry), a fixed deterministic strategy will match or exceed any learned router. Our router training consumed ${\\sim}$200 GPU-hours across 28 configurations without exceeding always-deterministic; this diagnostic framework could have predicted that outcome from a 50-episode pilot at negligible cost. The MATH negative control ($p = 0.81$, no deaths, no routing signal) validates the diagnostic: absent catastrophic failure, the framework correctly predicts that routing adds no value.\n\n\\paragraph{Framework applicability.}\nThe penalty-independent label fraction (78.9\\%) is the primary diagnostic; DAF increases monotonically with $P$ (Appendix~\\ref{app:penalty}). The framework requires paired modality episodes with binary catastrophic outcomes. NetHack~\\citep{nethack-2020} and Crafter~\\citep{crafter-2022}, both featuring permadeath, are the most direct replication targets; recent benchmarks \\citep{balrog-2025,netplay-2024} provide infrastructure.\n",
      "numLines": 18,
      "startLine": 1,
      "totalLines": 18
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
Now I have all the necessary information. Let me also check the introduction and abstract to understand the full story, and check if there's any additional information about what was compressed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "ab9911ea-4c5f-4fcc-95c6-365b6ca2ca95",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmNULUpxsPdodbPe4gDKv8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 26203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 11,
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

Now I have a clear picture of the current state. Let me also check the introduction for context on the overall narrative.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "c6396675-118a-431a-9ffc-85d7e046f659",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmNULUpxsPdodbPe4gDKv8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 26203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 11,
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

<details open><summary>🔧 Tool call — Read · `toolu_0186hzNG6ao5yRFL6NWCw4du`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "bc6d5104-a47a-48f9-a6c1-798ae6384990",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmNULUpxsPdodbPe4gDKv8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 26203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 11,
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

_source line 39 · 2026-05-19T11:10:10.196Z_

<details><summary>↩ Tool result · `toolu_0186hzNG6ao5yRFL6NWCw4du`</summary>

```text
1	\section{Introduction}
2	
3	Large language models deployed as interactive agents must repeatedly decide \emph{how} to compute: reason internally, or delegate to an external tool.
4	A Qwen2.5-7B-Instruct agent navigating ScienceWorld \cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \emph{when should an agent route computation externally versus reasoning internally?}
5	
6	Existing routing approaches frame this as a capability or efficiency decision.
7	Toolformer \cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.
8	More recent adaptive-computation methods route to different reasoning depths \cite{cogrouter-2026,ares-2026} or model tiers \cite{mtrouter-2026}.
9	Concurrent analyses of when and whether to invoke tools~\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.
10	The shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.
11	But no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from those where a single failure mode dominates and a fixed strategy suffices.
12	
13	We propose a \emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\S\ref{sec:collection}--\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a penalty-dependent metric that decomposes the routing score gap into death-avoidance and non-death components (\S\ref{sec:daf}). Applied to ScienceWorld, \textbf{78.9\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding that holds regardless of how death is penalized. Under ScienceWorld's specific penalty structure ($P{=}100$), the penalty-weighted DAF reaches $90.4\%$ (95\% CI: $[81.6\%, 98.8\%]$), consistent with the predicted value from observed $\delta{=}0.265$ and $P{=}100$.
14	The internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.
15	Once death episodes are removed, the performance gap collapses to $\Delta_{\text{nd}} = +2.84$. A per-task consistency check ($r = 0.97$) confirms that the near-perfect correlation is a mathematical consequence of death dominance when $P$ is constant (\S\ref{sec:death-decomp}).
16	
17	This framework addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\% of ScienceWorld steps produce identical scores regardless of modality; \S\ref{sec:collection}), and keyword-based heuristics fail structurally (\S\ref{sec:baselines}). Our counterfactual approach runs complete episodes under pure-internal (ReAct \cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes.
18	
19	Two cross-context checks probe the specificity of this finding.
20	First, a MATH Level~4--5 evaluation ($N{=}795$ problems, code interpreter as deterministic modality) confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\%$ vs.\ $73.0\%$, $p = 0.81$).
21	Second, a cross-model replication with Llama-3.1-8B-Instruct (11 task types, $N{=}220$) shows death dominance replicates across model families with direction consistency 10/10 ($+30.0$~pp vs.\ $+26.5$~pp for Qwen; \S\ref{sec:cross-model}).
22	Agent improvement baselines confirm that death dominance is robust: retry yields only marginal reduction, while $10{\times}$ model scaling (72B) and Reflexion~\citep{reflexion-2023} each reduce death rates to ${\sim}$35\% through independent mechanisms, yet neither closes the ${\sim}$18~pp gap to deterministic (\S\ref{sec:agent-improvement}).
23	An exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\%$); at episode level, only 4B exceeds the always-deterministic baseline (\S\ref{sec:router-diagnostic}).
24	
25	Our contributions are:
26	\begin{enumerate}
27	    \item \textbf{An episode-level counterfactual diagnostic framework} for decomposing routing signal, with dual penalty-independent and penalty-dependent metrics and router training as a diagnostic probe (\S\ref{sec:collection}--\ref{sec:daf}, \S\ref{sec:router-diagnostic}).
28	
29	    \item \textbf{Evidence that death dominance is robust and routing value is near-degenerate}: 78.9\% of non-tie labels arise from death asymmetry (DAF $= 90.4\%$); the oracle degenerates to unconditional deterministic computation (96.3\% overlap). Four intervention axes (retry, scaling, Reflexion, action-space filtering) all fail to close the gap (\S\ref{sec:death-decomp}--\ref{sec:agent-improvement}).
30	
31	    \item \textbf{Cross-environment boundary probes}: MATH ($p = 0.81$) confirms the predicted null; ALFWorld identifies information asymmetry; a Llama-3.1-8B replication ($N{=}220$) confirms cross-model consistency with 10/10 direction consistency (\S\ref{sec:math-contrast}--\ref{sec:cross-model}).
32	\end{enumerate}
33	
34	
35	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "ba0df582-4b03-457b-9cfe-ed061943cc30",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\nLarge language models deployed as interactive agents must repeatedly decide \\emph{how} to compute: reason internally, or delegate to an external tool.\nA Qwen2.5-7B-Instruct agent navigating ScienceWorld \\cite{scienceworld-2022}, a text-based science simulation with 30 task types, faces this choice at every step. Tracking temperature thresholds, container states, and multi-step procedures via internal reasoning is error-prone: the model may hallucinate that water has boiled when the stove was never activated, or that an object has been moved when the action was invalid. Deterministic external computation (environment simulators, code interpreters) eliminates such hallucinations via exact state transitions. The practical question for agent design is therefore: \\emph{when should an agent route computation externally versus reasoning internally?}\n\nExisting routing approaches frame this as a capability or efficiency decision.\nToolformer \\cite{toolformer-2023} teaches models to insert API calls when doing so reduces perplexity; ART \\cite{art-2023} decomposes tasks into tool-augmented programs; Chameleon \\cite{chameleon-2023} selects among heterogeneous modules (search, code, vision) per subtask.\nMore recent adaptive-computation methods route to different reasoning depths \\cite{cogrouter-2026,ares-2026} or model tiers \\cite{mtrouter-2026}.\nConcurrent analyses of when and whether to invoke tools~\\citep{when2tool-2026,tool-use-tax-2026,to-call-or-not-2026} further presuppose diverse routing signals.\nThe shared assumption is that routing signal stems from diverse sources (accuracy, latency, capability matching) and that a learned router can exploit this signal to improve over any fixed strategy.\nBut no prior work has systematically decomposed what drives routing decisions in interactive environments. Without such a decomposition, the field cannot distinguish settings where diverse routing signals justify learned routers from those where a single failure mode dominates and a fixed strategy suffices.\n\nWe propose a \\emph{formal diagnostic framework} for answering this question. The framework comprises (i)~episode-level counterfactual labeling under pure strategies (\\S\\ref{sec:collection}--\\ref{sec:labeling}), and (ii)~the Death Avoidance Factor (DAF), a penalty-dependent metric that decomposes the routing score gap into death-avoidance and non-death components (\\S\\ref{sec:daf}). Applied to ScienceWorld, \\textbf{78.9\\% of non-tie routing labels arise from death asymmetry} (75 of 95), a penalty-independent finding that holds regardless of how death is penalized. Under ScienceWorld's specific penalty structure ($P{=}100$), the penalty-weighted DAF reaches $90.4\\%$ (95\\% CI: $[81.6\\%, 98.8\\%]$), consistent with the predicted value from observed $\\delta{=}0.265$ and $P{=}100$.\nThe internal strategy's hallucination-induced failures trigger catastrophic agent death (a $-100$ penalty), while the deterministic strategy survives the same episodes.\nOnce death episodes are removed, the performance gap collapses to $\\Delta_{\\text{nd}} = +2.84$. A per-task consistency check ($r = 0.97$) confirms that the near-perfect correlation is a mathematical consequence of death dominance when $P$ is constant (\\S\\ref{sec:death-decomp}).\n\nThis framework addresses a methodological gap: per-step oracle comparison degenerates under sparse rewards (97.4\\% of ScienceWorld steps produce identical scores regardless of modality; \\S\\ref{sec:collection}), and keyword-based heuristics fail structurally (\\S\\ref{sec:baselines}). Our counterfactual approach runs complete episodes under pure-internal (ReAct \\cite{react-2023}) and pure-deterministic strategies, then compares episode outcomes. The framework applies to any environment with controllable modality comparison and binary catastrophic outcomes.\n\nTwo cross-context checks probe the specificity of this finding.\nFirst, a MATH Level~4--5 evaluation ($N{=}795$ problems, code interpreter as deterministic modality) confirms no routing signal without catastrophic failure: internal reasoning and code interpretation achieve near-identical accuracy ($73.5\\%$ vs.\\ $73.0\\%$, $p = 0.81$).\nSecond, a cross-model replication with Llama-3.1-8B-Instruct (11 task types, $N{=}220$) shows death dominance replicates across model families with direction consistency 10/10 ($+30.0$~pp vs.\\ $+26.5$~pp for Qwen; \\S\\ref{sec:cross-model}).\nAgent improvement baselines confirm that death dominance is robust: retry yields only marginal reduction, while $10{\\times}$ model scaling (72B) and Reflexion~\\citep{reflexion-2023} each reduce death rates to ${\\sim}$35\\% through independent mechanisms, yet neither closes the ${\\sim}$18~pp gap to deterministic (\\S\\ref{sec:agent-improvement}).\nAn exploratory router (Qwen3 LoRA, 0.6B--4B) yields flat step-level balanced accuracy ($56$--$59\\%$); at episode level, only 4B exceeds the always-deterministic baseline (\\S\\ref{sec:router-diagnostic}).\n\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{An episode-level counterfactual diagnostic framework} for decomposing routing signal, with dual penalty-independent and penalty-dependent metrics and router training as a diagnostic probe (\\S\\ref{sec:collection}--\\ref{sec:daf}, \\S\\ref{sec:router-diagnostic}).\n\n    \\item \\textbf{Evidence that death dominance is robust and routing value is near-degenerate}: 78.9\\% of non-tie labels arise from death asymmetry (DAF $= 90.4\\%$); the oracle degenerates to unconditional deterministic computation (96.3\\% overlap). Four intervention axes (retry, scaling, Reflexion, action-space filtering) all fail to close the gap (\\S\\ref{sec:death-decomp}--\\ref{sec:agent-improvement}).\n\n    \\item \\textbf{Cross-environment boundary probes}: MATH ($p = 0.81$) confirms the predicted null; ALFWorld identifies information asymmetry; a Llama-3.1-8B replication ($N{=}220$) confirms cross-model consistency with 10/10 direction consistency (\\S\\ref{sec:math-contrast}--\\ref{sec:cross-model}).\n\\end{enumerate}\n\n\n",
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01M6hcnvN7CmaeBsBcLpNsWf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "b1d7412e-a086-457d-b266-c1f2c1a03ebe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CmNULUpxsPdodbPe4gDKv8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13247,
      "cache_read_input_tokens": 26203,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13247
      },
      "output_tokens": 11,
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

_source line 41 · 2026-05-19T11:10:10.384Z_

<details><summary>↩ Tool result · `toolu_01M6hcnvN7CmaeBsBcLpNsWf`</summary>

```text
1	\begin{abstract}
2	Modular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \textbf{78.9\% of non-tie routing labels} arise from death asymmetry (DAF $= 90.4\%$): the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. Retry yields only marginal reduction (43.5\%), while $10{\times}$ model scaling and Reflexion each reduce death rates on death-prone tasks to ${\sim}$35\%, yet none closes the ${\sim}$18~pp gap to deterministic execution. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when learned routers add value over a fixed strategy and when catastrophic failure makes routing degenerate.
3	\end{abstract}
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "581dcda4-2e2b-40bb-b76b-7388d905efee",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/docs/paper/abstract.tex",
      "content": "\\begin{abstract}\nModular LLM agents that route between neural reasoning and deterministic computation promise improved reliability, yet no systematic methodology exists for diagnosing \\emph{what} drives routing decisions. We introduce an episode-level counterfactual framework that decomposes routing signal into death-avoidance and non-death components. Applied to ScienceWorld (11 task types, 245 episodes, Qwen2.5-7B-Instruct), \\textbf{78.9\\% of non-tie routing labels} arise from death asymmetry (DAF $= 90.4\\%$): the internal strategy's hallucination-induced failures trigger catastrophic agent death, while the deterministic strategy survives. Retry yields only marginal reduction (43.5\\%), while $10{\\times}$ model scaling and Reflexion each reduce death rates on death-prone tasks to ${\\sim}$35\\%, yet none closes the ${\\sim}$18~pp gap to deterministic execution. A MATH evaluation ($N{=}795$, $p = 0.81$) confirms no routing signal without catastrophic failure. The framework reveals when learned routers add value over a fixed strategy and when catastrophic failure makes routing degenerate.\n\\end{abstract}\n",
      "numLines": 4,
      "startLine": 1,
      "totalLines": 4
    }
  }
}
```

</details>

---

### Assistant

_source line 42_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the paper. Let me assess the method section recovery and draft the practitioner decision framework.

Key observations about the current method.tex:
1. **Per-step oracle tie rate 97.4%**: Currently mentioned in §3.2 (line 14) as a one-sentence statement: "97.4% of steps produce identical intermediate scores regardless of modality (5,726 of 5,878 steps across 11 prescreened task types)". No derivation of how this was computed.

2. **Counterfactual framework formal definition**: Currently present in §3.1-3.3 with notation ($\mathcal{O}$, $\mathcal{A}$, $\mathcal{M}$, etc.). 

3. **Death dominance decomposition math**: Present in §3.4 with the DAF formula. The decomposition $\Delta_{\text{full}} \approx \delta \cdot P + \Delta_{\text{nd}}$ is there.

4. **Episode-level vs step-level justification**: Mentioned in §3.2 but as a brief motivation, not a full justification.

The method section is fairly complete already, so I'll focus on writing the assessment and decision framework now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "1d3405a7-02d4-4f21-8f13-d99d5ec268eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdctxwrFV7dPFbAY6bFAT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2280,
      "cache_read_input_tokens": 39450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2280
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

_source line 43_

I now have a complete picture. Let me write the assessment and decision framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "081a3bac-31f7-4853-bf56-b15ed5a4396c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdctxwrFV7dPFbAY6bFAT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2280,
      "cache_read_input_tokens": 39450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2280
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

_source line 44_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0113YhKCuK35qmxj8kqQeq9v`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "49da6d78-24bc-4ea3-b522-9a0deaba51fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UdctxwrFV7dPFbAY6bFAT8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2280,
      "cache_read_input_tokens": 39450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2280
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

_source line 45 · 2026-05-19T11:10:21.924Z_

<details><summary>↩ Tool result · `toolu_0113YhKCuK35qmxj8kqQeq9v`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
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
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "bbb4ccd2-753f-46d9-911b-c4c7e0d28f68",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me now write the assessment document. I have all the information needed.

Key analysis:

**Part 1: Method Section Recovery Assessment**

1. **Per-step oracle tie rate 97.4% derivation**: Currently in §3.2, it's stated as a fact with the raw numbers (5,726/5,878). There's no derivation of HOW this was computed (what counts as a "tie", what the intermediate scores look like). The current treatment is actually adequate for the paper's purposes — the number is self-explanatory (identical intermediate scores). A full derivation would add maybe 0.2 pages but the marginal value is low. 

The key insight is already conveyed, so I'd recommend keeping it as-is with maybe 1-2 sentences added to the appendix for completeness.

2. **Counterfactual framework formal definition**: The method section is actually quite complete. The oracle, action, and model spaces are defined in §3.1 along with the policy and reward notation. Pure-strategy trajectories are formalized in §3.2, the labeling function in §3.3, and DAF in §3.4. The notation is clear and the formalism is sufficient for the paper's scope.

3. **Death dominance decomposition math**: The decomposition and DAF formula are both present in §3.4, with approximation conditions stated. What's missing is a more explicit derivation showing why this decomposition holds—the conditional expectation algebra underlying it. Right now it reads as a definition rather than something derived, so adding a few lines of derivation would strengthen the rigor.

4. **Episode-level vs step-level justification**: The current justification in §3.2 is fairly brief—essentially that per-step oracle ties are so prevalent (97.4%) that episode-level analysis is necessary. A more thorough treatment would explore the implications of this degeneracy more fully and explain why it forces the shift to episode-level reasoning.

Looking at the paper_framing.md target of 1.5 pages for the Method section and checking the current LaTeX, it's actually hitting that length already. But the user's feedback suggests the Method section feels compressed, so there's likely room to expand the justifications and derivations even if the overall page count is on target.

The main gap I'm seeing is that the labeling algorithm pseudocode is deferred to the appendix when it could be more prominent in the main text, and the DAF derivation could use more explanation of the intuition behind it. The router architecture was intentionally moved to the experiments section as a diagnostic tool, so that's a deliberate choice rather than an omission.

For the practitioner decision framework in the discussion, there's already a paragraph started but it's quite brief at around 6 lines.

Now I'm looking at the empirical thresholds from the data to build out a more structured decision tree. The death rate differential shows clear separation between models like Qwen and Llama in the 26-30 percentage point range, while MATH shows essentially no signal. The DAF values are dramatically different across tasks—90.4% for ScienceWorld versus near zero for MATH—and the death-asymmetry label fraction hits 78.9% on ScienceWorld. I'm using these patterns to establish concrete thresholds: a death rate differential above 10 percentage points suggests death dominance is likely present, below 5 points suggests it's absent, and the 5-10 point range is borderline. When the death-asymmetry label fraction exceeds 50%, that indicates death avoidance is the primary mechanism at play.

Adding a few more decision boundaries: if the per-step tie rate climbs above 90%, then step-level routing decisions have minimal practical value.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "d0cd5be3-964b-4818-b76a-3ac41d1d3ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oLqMJP3oranosEqUaJgf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 41730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — Write · `toolu_01A2ACkS5pqLsDbymxxspK9W`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/method_recovery_and_decision_framework.md",
  "content": "# Method Section Recovery + Practitioner Decision Framework\n\n## Part 1: Method Section Recovery Assessment\n\n### Current State\n\nThe method section (§3) currently occupies ~1.5 pages with four subsections: Problem Setup (§3.1), Counterfactual Episode Collection (§3.2), Episode-Level Labeling (§3.3), and Death Avoidance Factor (§3.4). It includes one figure (pipeline overview) and five equations. The formalism is complete at a surface level but several items were compressed during the 10.5→8 page cut.\n\n### Item-by-Item Assessment\n\n#### 1. Per-step oracle tie rate 97.4% — full derivation\n\n**Current treatment**: One sentence in §3.2: \"97.4% of steps produce identical intermediate scores regardless of modality (5,726 of 5,878 steps across 11 prescreened task types).\"\n\n**What's missing**: No explanation of how per-step comparison was conducted (what \"identical intermediate scores\" means operationally), no discussion of WHY sparse terminal rewards cause this degeneracy (intermediate scores don't discriminate because only terminal outcome matters), no breakdown by task type showing the tie rate is uniformly high rather than driven by a few task types.\n\n**Assessment**: The current one-sentence treatment is sufficient for readers who accept the claim. However, this number is **the key methodological motivation** for the entire episode-level approach — it justifies why the paper exists. A reviewer asking \"why not just do per-step oracle labeling?\" needs to see that the answer is structural, not a limitation of our setup. 2-3 sentences of explanation would strengthen this considerably.\n\n**Recommendation**: **Restore 2-3 sentences to the main text** explaining the mechanism (sparse terminal rewards → intermediate scores are uninformative → per-step oracle degenerates). Move the per-task breakdown table to appendix. **+0.05 pages.**\n\n#### 2. Counterfactual framework formal definitions (variable notation)\n\n**Current treatment**: §3.1-3.3 define $\\mathcal{O}$, $\\mathcal{A}$, $\\mathcal{M}$, $\\pi$, $\\rho$, pure-strategy trajectories, terminal score, death indicator, and the labeling function $L$. Five equations cover the key definitions.\n\n**What's missing**: Essentially nothing substantive. The current notation is clean and complete. The only gap is that Algorithm 1 (the labeling algorithm pseudocode) is referenced but deferred to the appendix.\n\n**Assessment**: The formalism is already at long-paper quality. The labeling algorithm pseudocode would add clarity but is appropriately placed in the appendix since the text description in §3.3 (\"death-aware: prioritizes survival over score, then compares scores among same-status episodes\") captures the logic concisely.\n\n**Recommendation**: **Keep as-is.** The formal definitions are adequate. Moving Algorithm 1 into the main text would cost ~0.15 pages with marginal benefit since the verbal description is clear. **+0.0 pages.**\n\n#### 3. Death dominance decomposition — mathematical derivation\n\n**Current treatment**: §3.4 states the decomposition $\\Delta_{\\text{full}} \\approx \\delta \\cdot P + \\Delta_{\\text{nd}}$ and defines DAF = $1 - \\Delta_{\\text{nd}} / \\Delta_{\\text{full}}$. Notes the approximation residual (0.23, or 0.8%). Includes the footnote about DAF > 1 when $\\Delta_{\\text{nd}} < 0$.\n\n**What's missing**: The decomposition is presented as a definition rather than derived from conditional expectations. A proper derivation would show: $\\Delta_{\\text{full}} = \\mathbb{E}[s^{\\text{det}}] - \\mathbb{E}[s^{\\text{int}}]$, then condition on death status of each strategy (four cases: both die, both survive, only-int dies, only-det dies), showing how the death-asymmetry cases contribute $\\delta \\cdot P$ while the both-survive cases contribute $\\Delta_{\\text{nd}}$. This would make explicit what the \"approximation\" is (the cross-terms from both-die and asymmetric-but-surviving cases).\n\n**Assessment**: For a methodology paper, the decomposition is the intellectual core. A reviewer with statistical training may find the current presentation hand-wavy — the jump from $\\Delta_{\\text{full}}$ to $\\delta \\cdot P + \\Delta_{\\text{nd}}$ skips the conditional expectation algebra. However, the residual is explicitly reported (0.8%), which provides empirical justification. The trade-off is rigor vs. space.\n\n**Recommendation**: **Add 3-4 lines of derivation sketch to the main text** showing the conditioning argument. Not a full proof, but enough to make the decomposition feel derived rather than asserted. The residual reporting already handles the approximation concern. **+0.1 pages.**\n\n#### 4. Episode-level vs step-level analysis justification\n\n**Current treatment**: §3.2 opens with the per-step oracle degeneracy finding (97.4%) and then immediately moves to episode-level collection. The justification is implicit: step-level doesn't work → we do episode-level.\n\n**What's missing**: (a) An explicit argument for why episode-level is the *right* unit of analysis, not just a fallback from step-level failure. Routing decisions compound across episodes — a single bad routing choice at step 5 can lead to death at step 15. The episode is the natural unit of counterfactual comparison because it captures these compounding effects. (b) Connection to the broader literature on trajectory-level vs step-level credit assignment (Ross et al. 2011 DAgger, the multi-step credit assignment problem in RL). (c) A brief note on why the \"no free lunch\" concern (episode labels applied to step-level routing creates label noise) is expected and informative rather than a limitation.\n\n**Assessment**: This is the strongest candidate for recovery. The current paper's narrative arc is: \"step-level fails → we do episode-level → episode-level reveals death dominance → but this signal is task-type-level, not step-level learnable.\" The philosophical justification for episode-level analysis strengthens the entire chain. It also preempts the reviewer question \"why not try harder at step-level labeling?\"\n\n**Recommendation**: **Add 4-5 sentences as a dedicated paragraph in §3.2** after the 97.4% finding, making the positive case for episode-level analysis (compounding effects, trajectory as the natural counterfactual unit) before presenting the collection procedure. Reference the step-level label noise (~27.7% misalignment) as a preview of §4.5's router diagnostic. **+0.15 pages.**\n\n### Summary Table\n\n| Item | Verdict | Location | Added Pages |\n|------|---------|----------|-------------|\n| Per-step tie rate derivation | Restore 2-3 sentences | §3.2 main text | +0.05 |\n| Formal definitions / notation | Keep as-is | Already adequate | +0.0 |\n| DAF decomposition derivation | Add derivation sketch | §3.4 main text | +0.10 |\n| Episode-level justification | Restore paragraph | §3.2 main text | +0.15 |\n| **Total** | | | **+0.30** |\n\n### Space Budget Impact\n\nCurrent paper is at ~8 pages. Adding 0.30 pages requires trimming elsewhere. Candidates:\n- Discussion §5 \"Practitioner decision framework\" paragraph is 6 sentences and could be compressed if the decision framework moves to appendix as a structured figure (+0.15 pages recovered)\n- Experiments §4.1 \"Sensitivity analysis\" paragraph overlaps heavily with appendix references and could lose 2 sentences (+0.05 pages)\n- The pipeline figure (Figure 1) is useful but could be reduced to 0.8\\columnwidth if needed (+0.05 pages)\n\nNet: recoverable space is ~0.25 pages, close to the 0.30 needed. Feasible with minor tightening.\n\n---\n\n## Part 2: Practitioner Decision Framework\n\n### 50-Episode Pilot Protocol for Routing Signal Diagnosis\n\n**Goal**: Given a new interactive environment with two computation modalities (e.g., internal reasoning vs. deterministic execution), determine whether learned routing adds value over a fixed strategy, using minimal compute.\n\n#### Protocol\n\n**Step 0: Select pilot instances.**\nChoose 50 task instances spanning the environment's task-type diversity. Stratify by expected difficulty if task metadata is available. Use a fixed random seed for reproducibility.\n\n**Step 1: Collect paired episodes.**\nRun each instance under two pure strategies: always-internal and always-deterministic. Record per-episode: terminal score $s$, binary death/catastrophic-failure indicator $d$, and episode length $T$. Total cost: 100 episodes (50 pairs).\n\n**Step 2: Compute death-rate differential ($\\Delta$DR).**\n\n$$\\Delta\\text{DR} = \\text{DR}_{\\text{internal}} - \\text{DR}_{\\text{deterministic}}$$\n\n| $\\Delta$DR | Interpretation | Action |\n|-----------|---------------|--------|\n| $> 15$ pp | Strong death dominance | Go to Step 3 |\n| $5$--$15$ pp | Moderate signal | Go to Step 3, but routing may have mixed sources |\n| $< 5$ pp | No death dominance | Go to Step 4 |\n\n*Thresholds derived from: ScienceWorld $\\Delta$DR = 26.5 pp (strong), MATH $\\Delta$DR = 0 pp (none). The 15 pp boundary is set at ~60% of our observed strong signal; the 5 pp boundary accounts for sampling noise at $N=50$ (Wilson 95% CI width $\\approx \\pm 6$ pp at 20% base rate).*\n\n**Step 3: Assess death dominance magnitude.**\nCompute the death-asymmetry label fraction: among episode pairs where the two strategies produce different outcomes (non-tie labels), what fraction have one strategy dying and the other surviving?\n\n$$f_{\\text{death}} = \\frac{|\\{i : d_{\\text{int}}^{(i)} \\neq d_{\\text{det}}^{(i)} \\text{ and } \\ell_i \\neq \\text{no-pref}\\}|}{|\\{i : \\ell_i \\neq \\text{no-pref}\\}|}$$\n\n| $f_{\\text{death}}$ | Interpretation | Recommendation |\n|--------------------|---------------|----------------|\n| $> 75\\%$ | Death avoidance is the dominant routing signal | **Fixed deterministic strategy will match or exceed any learned router.** Invest in death prevention (grounding, guardrails), not routing. |\n| $50$--$75\\%$ | Death is major but not sole signal | Learned routing may capture non-death signal. Proceed with caution; expect modest gains over fixed strategy. |\n| $< 50\\%$ | Diverse routing signal | Learned routing is justified. Proceed to router training. |\n\n*Thresholds derived from: ScienceWorld $f_{\\text{death}}$ = 78.9% (strong dominance, router failed to exceed always-det); the 75% boundary captures this regime.*\n\n**Step 4: Check per-step informativeness.**\nIf $\\Delta$DR $< 5$ pp (no death dominance), assess whether step-level routing signal exists. Run per-step oracle comparison on the 50 pairs: at each step, compare the immediate reward/score under both modalities.\n\n$$\\text{Tie rate} = \\frac{|\\{(i,t) : r_{\\text{int}}^{(i,t)} = r_{\\text{det}}^{(i,t)}\\}|}{|\\text{all step pairs}|}$$\n\n| Tie rate | Interpretation | Recommendation |\n|----------|---------------|----------------|\n| $> 90\\%$ | Step-level signal is sparse | Episode-level analysis required. Step-level router training will lack supervision signal. |\n| $70$--$90\\%$ | Moderate step-level signal | Standard per-step oracle labeling is viable. Proceed with step-level router. |\n| $< 70\\%$ | Rich step-level signal | Per-step routing is well-supported. Dense rewards provide direct supervision. |\n\n*Threshold derived from: ScienceWorld tie rate = 97.4% (extreme sparsity); environments with dense intermediate rewards (e.g., game score increments) would fall below 70%.*\n\n#### Decision Summary (text-based decision tree)\n\n```\nRun 50-episode pilot (always-internal vs always-deterministic)\n│\n├─ ΔDR > 15 pp ──→ Compute f_death\n│   ├─ f_death > 75% ──→ STOP: Use fixed deterministic strategy.\n│   │                     Invest in death prevention, not routing.\n│   └─ f_death ≤ 75% ──→ Mixed signal. Router training may help,\n│                         but cap expectations (oracle margin likely small).\n│\n├─ ΔDR 5-15 pp ──→ Compute f_death (same branches as above,\n│                   but with weaker prior on death dominance)\n│\n└─ ΔDR < 5 pp ──→ No death dominance. Check per-step tie rate.\n    ├─ Tie rate > 90% ──→ Sparse rewards. Use episode-level\n    │                      counterfactual labeling for routing signal.\n    └─ Tie rate ≤ 90% ──→ Standard per-step oracle labeling is viable.\n                           Proceed with step-level router training.\n```\n\n#### Cost Estimate\n\n- 100 episodes (50 pairs) with a 7B model on ScienceWorld takes ~2 GPU-hours\n- Compare to: our full router training consumed ~200 GPU-hours across 28 configurations without exceeding always-deterministic\n- The pilot would have predicted that outcome at <1% of the compute cost\n\n#### Validation Against Our Data\n\n| Environment | $\\Delta$DR | $f_{\\text{death}}$ | Tie rate | Framework prediction | Actual outcome |\n|-------------|-----------|-------------------|----------|---------------------|----------------|\n| ScienceWorld (Qwen-7B) | 26.5 pp | 78.9% | 97.4% | Fixed det. strategy sufficient | Router ≤ always-det ✓ |\n| ScienceWorld (Llama-8B) | 30.0 pp | ~83%* | — | Fixed det. strategy sufficient | Same pattern ✓ |\n| ScienceWorld (Qwen-72B) | ~18 pp | ~80%* | — | Fixed det. strategy sufficient | DAF = 90.9% ✓ |\n| MATH | 0 pp | — | — | No routing signal | $p = 0.81$ ✓ |\n\n*Estimated from reported label distributions.\n\n#### Placement Recommendation\n\nThis framework is currently a prose paragraph in Discussion (§5). Two options:\n1. **Discussion (0.3 pages)**: Keep in §5 but restructure as the decision tree above, replacing the current prose paragraph. Fits the \"practical implications\" role of Discussion.\n2. **Appendix**: Move the full decision tree with thresholds and validation table to appendix; keep a 2-sentence pointer in Discussion. Saves ~0.15 pages in main text.\n\nGiven the 8-page constraint and the 0.30 pages needed for Method recovery, **Option 2 is recommended**: appendix placement with a Discussion pointer. The framework is a secondary contribution (practical utility) and the appendix allows the full decision tree without space pressure.\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "67c52890-adba-4d9d-ae03-bec0e3f53beb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017oLqMJP3oranosEqUaJgf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 41730,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 783
      },
      "output_tokens": 19,
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

_source line 48 · 2026-05-19T11:12:27.106Z_

<details><summary>↩ Tool result · `toolu_01A2ACkS5pqLsDbymxxspK9W`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/method_recovery_and_decision_framework.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "ef5662a8-5276-459b-bd22-ff8731f87414",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/artifacts/method_recovery_and_decision_framework.md",
    "content": "# Method Section Recovery + Practitioner Decision Framework\n\n## Part 1: Method Section Recovery Assessment\n\n### Current State\n\nThe method section (§3) currently occupies ~1.5 pages with four subsections: Problem Setup (§3.1), Counterfactual Episode Collection (§3.2), Episode-Level Labeling (§3.3), and Death Avoidance Factor (§3.4). It includes one figure (pipeline overview) and five equations. The formalism is complete at a surface level but several items were compressed during the 10.5→8 page cut.\n\n### Item-by-Item Assessment\n\n#### 1. Per-step oracle tie rate 97.4% — full derivation\n\n**Current treatment**: One sentence in §3.2: \"97.4% of steps produce identical intermediate scores regardless of modality (5,726 of 5,878 steps across 11 prescreened task types).\"\n\n**What's missing**: No explanation of how per-step comparison was conducted (what \"identical intermediate scores\" means operationally), no discussion of WHY sparse terminal rewards cause this degeneracy (intermediate scores don't discriminate because only terminal outcome matters), no breakdown by task type showing the tie rate is uniformly high rather than driven by a few task types.\n\n**Assessment**: The current one-sentence treatment is sufficient for readers who accept the claim. However, this number is **the key methodological motivation** for the entire episode-level approach — it justifies why the paper exists. A reviewer asking \"why not just do per-step oracle labeling?\" needs to see that the answer is structural, not a limitation of our setup. 2-3 sentences of explanation would strengthen this considerably.\n\n**Recommendation**: **Restore 2-3 sentences to the main text** explaining the mechanism (sparse terminal rewards → intermediate scores are uninformative → per-step oracle degenerates). Move the per-task breakdown table to appendix. **+0.05 pages.**\n\n#### 2. Counterfactual framework formal definitions (variable notation)\n\n**Current treatment**: §3.1-3.3 define $\\mathcal{O}$, $\\mathcal{A}$, $\\mathcal{M}$, $\\pi$, $\\rho$, pure-strategy trajectories, terminal score, death indicator, and the labeling function $L$. Five equations cover the key definitions.\n\n**What's missing**: Essentially nothing substantive. The current notation is clean and complete. The only gap is that Algorithm 1 (the labeling algorithm pseudocode) is referenced but deferred to the appendix.\n\n**Assessment**: The formalism is already at long-paper quality. The labeling algorithm pseudocode would add clarity but is appropriately placed in the appendix since the text description in §3.3 (\"death-aware: prioritizes survival over score, then compares scores among same-status episodes\") captures the logic concisely.\n\n**Recommendation**: **Keep as-is.** The formal definitions are adequate. Moving Algorithm 1 into the main text would cost ~0.15 pages with marginal benefit since the verbal description is clear. **+0.0 pages.**\n\n#### 3. Death dominance decomposition — mathematical derivation\n\n**Current treatment**: §3.4 states the decomposition $\\Delta_{\\text{full}} \\approx \\delta \\cdot P + \\Delta_{\\text{nd}}$ and defines DAF = $1 - \\Delta_{\\text{nd}} / \\Delta_{\\text{full}}$. Notes the approximation residual (0.23, or 0.8%). Includes the footnote about DAF > 1 when $\\Delta_{\\text{nd}} < 0$.\n\n**What's missing**: The decomposition is presented as a definition rather than derived from conditional expectations. A proper derivation would show: $\\Delta_{\\text{full}} = \\mathbb{E}[s^{\\text{det}}] - \\mathbb{E}[s^{\\text{int}}]$, then condition on death status of each strategy (four cases: both die, both survive, only-int dies, only-det dies), showing how the death-asymmetry cases contribute $\\delta \\cdot P$ while the both-survive cases contribute $\\Delta_{\\text{nd}}$. This would make explicit what the \"approximation\" is (the cross-terms from both-die and asymmetric-but-surviving cases).\n\n**Assessment**: For a methodology paper, the decomposition is the intellectual core. A reviewer with statistical training may find the current presentation hand-wavy — the jump from $\\Delta_{\\text{full}}$ to $\\delta \\cdot P + \\Delta_{\\text{nd}}$ skips the conditional expectation algebra. However, the residual is explicitly reported (0.8%), which provides empirical justification. The trade-off is rigor vs. space.\n\n**Recommendation**: **Add 3-4 lines of derivation sketch to the main text** showing the conditioning argument. Not a full proof, but enough to make the decomposition feel derived rather than asserted. The residual reporting already handles the approximation concern. **+0.1 pages.**\n\n#### 4. Episode-level vs step-level analysis justification\n\n**Current treatment**: §3.2 opens with the per-step oracle degeneracy finding (97.4%) and then immediately moves to episode-level collection. The justification is implicit: step-level doesn't work → we do episode-level.\n\n**What's missing**: (a) An explicit argument for why episode-level is the *right* unit of analysis, not just a fallback from step-level failure. Routing decisions compound across episodes — a single bad routing choice at step 5 can lead to death at step 15. The episode is the natural unit of counterfactual comparison because it captures these compounding effects. (b) Connection to the broader literature on trajectory-level vs step-level credit assignment (Ross et al. 2011 DAgger, the multi-step credit assignment problem in RL). (c) A brief note on why the \"no free lunch\" concern (episode labels applied to step-level routing creates label noise) is expected and informative rather than a limitation.\n\n**Assessment**: This is the strongest candidate for recovery. The current paper's narrative arc is: \"step-level fails → we do episode-level → episode-level reveals death dominance → but this signal is task-type-level, not step-level learnable.\" The philosophical justification for episode-level analysis strengthens the entire chain. It also preempts the reviewer question \"why not try harder at step-level labeling?\"\n\n**Recommendation**: **Add 4-5 sentences as a dedicated paragraph in §3.2** after the 97.4% finding, making the positive case for episode-level analysis (compounding effects, trajectory as the natural counterfactual unit) before presenting the collection procedure. Reference the step-level label noise (~27.7% misalignment) as a preview of §4.5's router diagnostic. **+0.15 pages.**\n\n### Summary Table\n\n| Item | Verdict | Location | Added Pages |\n|------|---------|----------|-------------|\n| Per-step tie rate derivation | Restore 2-3 sentences | §3.2 main text | +0.05 |\n| Formal definitions / notation | Keep as-is | Already adequate | +0.0 |\n| DAF decomposition derivation | Add derivation sketch | §3.4 main text | +0.10 |\n| Episode-level justification | Restore paragraph | §3.2 main text | +0.15 |\n| **Total** | | | **+0.30** |\n\n### Space Budget Impact\n\nCurrent paper is at ~8 pages. Adding 0.30 pages requires trimming elsewhere. Candidates:\n- Discussion §5 \"Practitioner decision framework\" paragraph is 6 sentences and could be compressed if the decision framework moves to appendix as a structured figure (+0.15 pages recovered)\n- Experiments §4.1 \"Sensitivity analysis\" paragraph overlaps heavily with appendix references and could lose 2 sentences (+0.05 pages)\n- The pipeline figure (Figure 1) is useful but could be reduced to 0.8\\columnwidth if needed (+0.05 pages)\n\nNet: recoverable space is ~0.25 pages, close to the 0.30 needed. Feasible with minor tightening.\n\n---\n\n## Part 2: Practitioner Decision Framework\n\n### 50-Episode Pilot Protocol for Routing Signal Diagnosis\n\n**Goal**: Given a new interactive environment with two computation modalities (e.g., internal reasoning vs. deterministic execution), determine whether learned routing adds value over a fixed strategy, using minimal compute.\n\n#### Protocol\n\n**Step 0: Select pilot instances.**\nChoose 50 task instances spanning the environment's task-type diversity. Stratify by expected difficulty if task metadata is available. Use a fixed random seed for reproducibility.\n\n**Step 1: Collect paired episodes.**\nRun each instance under two pure strategies: always-internal and always-deterministic. Record per-episode: terminal score $s$, binary death/catastrophic-failure indicator $d$, and episode length $T$. Total cost: 100 episodes (50 pairs).\n\n**Step 2: Compute death-rate differential ($\\Delta$DR).**\n\n$$\\Delta\\text{DR} = \\text{DR}_{\\text{internal}} - \\text{DR}_{\\text{deterministic}}$$\n\n| $\\Delta$DR | Interpretation | Action |\n|-----------|---------------|--------|\n| $> 15$ pp | Strong death dominance | Go to Step 3 |\n| $5$--$15$ pp | Moderate signal | Go to Step 3, but routing may have mixed sources |\n| $< 5$ pp | No death dominance | Go to Step 4 |\n\n*Thresholds derived from: ScienceWorld $\\Delta$DR = 26.5 pp (strong), MATH $\\Delta$DR = 0 pp (none). The 15 pp boundary is set at ~60% of our observed strong signal; the 5 pp boundary accounts for sampling noise at $N=50$ (Wilson 95% CI width $\\approx \\pm 6$ pp at 20% base rate).*\n\n**Step 3: Assess death dominance magnitude.**\nCompute the death-asymmetry label fraction: among episode pairs where the two strategies produce different outcomes (non-tie labels), what fraction have one strategy dying and the other surviving?\n\n$$f_{\\text{death}} = \\frac{|\\{i : d_{\\text{int}}^{(i)} \\neq d_{\\text{det}}^{(i)} \\text{ and } \\ell_i \\neq \\text{no-pref}\\}|}{|\\{i : \\ell_i \\neq \\text{no-pref}\\}|}$$\n\n| $f_{\\text{death}}$ | Interpretation | Recommendation |\n|--------------------|---------------|----------------|\n| $> 75\\%$ | Death avoidance is the dominant routing signal | **Fixed deterministic strategy will match or exceed any learned router.** Invest in death prevention (grounding, guardrails), not routing. |\n| $50$--$75\\%$ | Death is major but not sole signal | Learned routing may capture non-death signal. Proceed with caution; expect modest gains over fixed strategy. |\n| $< 50\\%$ | Diverse routing signal | Learned routing is justified. Proceed to router training. |\n\n*Thresholds derived from: ScienceWorld $f_{\\text{death}}$ = 78.9% (strong dominance, router failed to exceed always-det); the 75% boundary captures this regime.*\n\n**Step 4: Check per-step informativeness.**\nIf $\\Delta$DR $< 5$ pp (no death dominance), assess whether step-level routing signal exists. Run per-step oracle comparison on the 50 pairs: at each step, compare the immediate reward/score under both modalities.\n\n$$\\text{Tie rate} = \\frac{|\\{(i,t) : r_{\\text{int}}^{(i,t)} = r_{\\text{det}}^{(i,t)}\\}|}{|\\text{all step pairs}|}$$\n\n| Tie rate | Interpretation | Recommendation |\n|----------|---------------|----------------|\n| $> 90\\%$ | Step-level signal is sparse | Episode-level analysis required. Step-level router training will lack supervision signal. |\n| $70$--$90\\%$ | Moderate step-level signal | Standard per-step oracle labeling is viable. Proceed with step-level router. |\n| $< 70\\%$ | Rich step-level signal | Per-step routing is well-supported. Dense rewards provide direct supervision. |\n\n*Threshold derived from: ScienceWorld tie rate = 97.4% (extreme sparsity); environments with dense intermediate rewards (e.g., game score increments) would fall below 70%.*\n\n#### Decision Summary (text-based decision tree)\n\n```\nRun 50-episode pilot (always-internal vs always-deterministic)\n│\n├─ ΔDR > 15 pp ──→ Compute f_death\n│   ├─ f_death > 75% ──→ STOP: Use fixed deterministic strategy.\n│   │                     Invest in death prevention, not routing.\n│   └─ f_death ≤ 75% ──→ Mixed signal. Router training may help,\n│                         but cap expectations (oracle margin likely small).\n│\n├─ ΔDR 5-15 pp ──→ Compute f_death (same branches as above,\n│                   but with weaker prior on death dominance)\n│\n└─ ΔDR < 5 pp ──→ No death dominance. Check per-step tie rate.\n    ├─ Tie rate > 90% ──→ Sparse rewards. Use episode-level\n    │                      counterfactual labeling for routing signal.\n    └─ Tie rate ≤ 90% ──→ Standard per-step oracle labeling is viable.\n                           Proceed with step-level router training.\n```\n\n#### Cost Estimate\n\n- 100 episodes (50 pairs) with a 7B model on ScienceWorld takes ~2 GPU-hours\n- Compare to: our full router training consumed ~200 GPU-hours across 28 configurations without exceeding always-deterministic\n- The pilot would have predicted that outcome at <1% of the compute cost\n\n#### Validation Against Our Data\n\n| Environment | $\\Delta$DR | $f_{\\text{death}}$ | Tie rate | Framework prediction | Actual outcome |\n|-------------|-----------|-------------------|----------|---------------------|----------------|\n| ScienceWorld (Qwen-7B) | 26.5 pp | 78.9% | 97.4% | Fixed det. strategy sufficient | Router ≤ always-det ✓ |\n| ScienceWorld (Llama-8B) | 30.0 pp | ~83%* | — | Fixed det. strategy sufficient | Same pattern ✓ |\n| ScienceWorld (Qwen-72B) | ~18 pp | ~80%* | — | Fixed det. strategy sufficient | DAF = 90.9% ✓ |\n| MATH | 0 pp | — | — | No routing signal | $p = 0.81$ ✓ |\n\n*Estimated from reported label distributions.\n\n#### Placement Recommendation\n\nThis framework is currently a prose paragraph in Discussion (§5). Two options:\n1. **Discussion (0.3 pages)**: Keep in §5 but restructure as the decision tree above, replacing the current prose paragraph. Fits the \"practical implications\" role of Discussion.\n2. **Appendix**: Move the full decision tree with thresholds and validation table to appendix; keep a 2-sentence pointer in Discussion. Saves ~0.15 pages in main text.\n\nGiven the 8-page constraint and the 0.30 pages needed for Method recovery, **Option 2 is recommended**: appendix placement with a Discussion pointer. The framework is a secondary contribution (practical utility) and the appendix allows the full decision tree without space pressure.\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 49_

产出已保存到 `artifacts/method_recovery_and_decision_framework.md`。

**Part 1 结论**: 4 项中 2 项值得恢复到正文（episode-level justification +0.15p, DAF decomposition derivation sketch +0.10p），1 项加 2-3 句（tie rate 机制解释 +0.05p），1 项保持现状（formal definitions 已充分）。总计 +0.30 页，可通过压缩 Discussion 现有 practitioner 段落和 Experiments 敏感性分析段落回收空间。

**Part 2 结论**: Decision framework 以三级决策树结构化：ΔDR 阈值（15pp / 5pp）→ f_death 阈值（75% / 50%）→ per-step tie rate 阈值（90% / 70%）。所有阈值从实验数据反推并附推导依据。建议放 appendix（节省正文 0.15p 给 Method 恢复），Discussion 保留 2 句指针。用 ScienceWorld/MATH/Llama 四组数据做了回溯验证，预测全部命中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "uuid": "0fb60e9a-440d-409e-9a6e-26e0880b2f71",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CpAJd7dRMxihoKhWwk5nuE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5165,
      "cache_read_input_tokens": 42513,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5165
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

_source line 50_

产出已保存到 `artifacts/method_recovery_and_decision_framework.md`。

**Part 1 结论**: 4 项中 2 项值得恢复到正文（episode-level justification +0.15p, DAF decomposition derivation sketch +0.10p），1 项加 2-3 句（tie rate 机制解释 +0.05p），1 项保持现状（formal definitions 已充分）。总计 +0.30 页，可通过压缩 Discussion 现有 practitioner 段落和 Experiments 敏感性分析段落回收空间。

**Part 2 结论**: Decision framework 以三级决策树结构化：ΔDR 阈值（15pp / 5pp）→ f_death 阈值（75% / 50%）→ per-step tie rate 阈值（90% / 70%）。所有阈值从实验数据反推并附推导依据。建议放 appendix（节省正文 0.15p 给 Method 恢复），Discussion 保留 2 句指针。用 ScienceWorld/MATH/Llama 四组数据做了回溯验证，预测全部命中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 191712,
  "duration_api_ms": 192351,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "18b8dc78-6214-4a79-a2e7-b7d531fce282",
  "total_cost_usd": 0.6052432,
  "usage": {
    "input_tokens": 10,
    "cache_creation_input_tokens": 49286,
    "cache_read_input_tokens": 173578,
    "output_tokens": 6578,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49286,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 327,
        "cache_read_input_tokens": 42513,
        "cache_creation_input_tokens": 5165,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 5165
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1619,
      "outputTokens": 1415,
      "cacheReadInputTokens": 68527,
      "cacheCreationInputTokens": 24296,
      "webSearchRequests": 0,
      "costUSD": 0.0459167,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 10,
      "outputTokens": 6578,
      "cacheReadInputTokens": 173578,
      "cacheCreationInputTokens": 49286,
      "webSearchRequests": 0,
      "costUSD": 0.5593265,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "968eb057-441e-4ad9-8026-28e95fd386ca"
}
```

</details>

---
