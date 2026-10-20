# code e3 mixed mechanism semisynthetic

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 133
- **Recorded user turns:** 2
- **Tool calls:** 40
- **Original source:** `logs/workers/worker_code_e3_mixed_mechanism_semisynthetic_20260523T012835.log`
- **Structured JSON:** [`93152c255b880e4c63e0.json`](../../sessions/93/93152c255b880e4c63e0.json)

## Before a recorded user message

7 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
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
  "uuid": "fa79b838-d907-45fe-97a0-8ca7c02d7405",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
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
    "resetsAt": 1779508200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "4119333b-e0e9-4f5d-803d-c23971e9c4ad",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by understanding the existing semi-synthetic framework code, then extend it for the new schemes D and E.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "2a5e988e-f288-406e-b45e-75f27b49efa2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxDXJs9WmWPvTgTbGkKPT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13398
      },
      "output_tokens": 23,
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

Let me first read the existing semi-synthetic code to understand the framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "1be51f07-c289-4d9c-88e2-9d3a7b0b0a57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxDXJs9WmWPvTgTbGkKPT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13398
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — Agent · `toolu_01PVpYHhCTFZS2uyht5A1pLh`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Explore semi-synthetic code",
  "prompt": "I need to understand the existing semi-synthetic injection framework in this project. Please find and read all Python files in `artifacts/r19_semisynthetic_gradient/` directory under `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`. Also read the report file there. I need to understand:\n1. How the response matrix is loaded\n2. How models are split into ref/focal cohorts\n3. How injection schemes work (A, B, C)\n4. How MH-DIF is computed\n5. How metrics (rho, chi-squared) are calculated\n6. The overall structure of the experiment pipeline\n\nAlso check `artifacts/model_metadata.csv` to understand the training_method field format (just the first few lines). And check what's in `artifacts/response_matrix.npz` and `artifacts/response_matrix_index.npz` by looking at how they're loaded.\n\nBe very thorough - read all the code files completely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "9c520f4d-4eaa-41ec-a6e7-1afff3bba51c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NxDXJs9WmWPvTgTbGkKPT4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13398,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13398
      },
      "output_tokens": 23,
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

_source line 7_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Explore semi-synthetic code",
  "task_type": "local_agent",
  "prompt": "I need to understand the existing semi-synthetic injection framework in this project. Please find and read all Python files in `artifacts/r19_semisynthetic_gradient/` directory under `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`. Also read the report file there. I need to understand:\n1. How the response matrix is loaded\n2. How models are split into ref/focal cohorts\n3. How injection schemes work (A, B, C)\n4. How MH-DIF is computed\n5. How metrics (rho, chi-squared) are calculated\n6. The overall structure of the experiment pipeline\n\nAlso check `artifacts/model_metadata.csv` to understand the training_method field format (just the first few lines). And check what's in `artifacts/response_matrix.npz` and `artifacts/response_matrix_index.npz` by looking at how they're loaded.\n\nBe very thorough - read all the code files completely.",
  "uuid": "dd83f4c9-3b9c-455b-8edc-323a95e0ff21",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

## Round 1

43 recorded events

### User

_source line 8 · 2026-05-23T01:28:52.220Z_

I need to understand the existing semi-synthetic injection framework in this project. Please find and read all Python files in `artifacts/r19_semisynthetic_gradient/` directory under `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`. Also read the report file there. I need to understand:
1. How the response matrix is loaded
2. How models are split into ref/focal cohorts
3. How injection schemes work (A, B, C)
4. How MH-DIF is computed
5. How metrics (rho, chi-squared) are calculated
6. The overall structure of the experiment pipeline

Also check `artifacts/model_metadata.csv` to understand the training_method field format (just the first few lines). And check what's in `artifacts/response_matrix.npz` and `artifacts/response_matrix_index.npz` by looking at how they're loaded.

Be very thorough - read all the code files completely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "c91fe26b-8ea1-42b8-a123-84d2f7bd8e0a"
}
```

</details>

---

### System

_source line 9_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Finding artifacts/r19_semisynthetic_gradient/*.py",
  "usage": {
    "total_tokens": 15633,
    "tool_uses": 1,
    "duration_ms": 3647
  },
  "last_tool_name": "Glob",
  "uuid": "6d18ce95-68e3-4202-90af-632979e39503",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 10_

<details open><summary>🔧 Tool call — Glob · `toolu_013ZbPQRwzyUjexzp4x2KBYi`</summary>

```json
{
  "pattern": "artifacts/r19_semisynthetic_gradient/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "dae6ca7e-c5be-4cc5-9bd3-833fb3bd5ea2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hhJXsJNh6suKjofo3ocGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 11 · 2026-05-23T01:28:55.982Z_

<details><summary>↩ Tool result · `toolu_013ZbPQRwzyUjexzp4x2KBYi`</summary>

```text
artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "bddeafc4-105d-4890-8ece-6b2b43bd56bb"
}
```

</details>

---

### System

_source line 12_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Finding artifacts/r19_semisynthetic_gradient/*.md",
  "usage": {
    "total_tokens": 15636,
    "tool_uses": 2,
    "duration_ms": 3817
  },
  "last_tool_name": "Glob",
  "uuid": "809de60e-5139-4534-8b5b-ee429f16a911",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01WwXty5N2jmgBDUK82Db5P8`</summary>

```json
{
  "pattern": "artifacts/r19_semisynthetic_gradient/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "200537d1-06c0-491f-a02b-8f1e5ca66da4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hhJXsJNh6suKjofo3ocGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 14 · 2026-05-23T01:28:56.103Z_

<details><summary>↩ Tool result · `toolu_01WwXty5N2jmgBDUK82Db5P8`</summary>

```text
artifacts/r19_semisynthetic_gradient/semisynthetic_gradient_report.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "7842538b-821e-47f3-8e14-8cc94bd150a1"
}
```

</details>

---

### System

_source line 15_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 15639,
    "tool_uses": 3,
    "duration_ms": 4126
  },
  "last_tool_name": "Bash",
  "uuid": "f3f31a27-4e52-42f3-87c0-ca48f2ebf383",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Bash · `toolu_01AFcfEgb34wqg49xjY9VP3m`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/ | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "792872f8-af4c-4dab-9824-d7feed7429d0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011hhJXsJNh6suKjofo3ocGD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 654,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 654,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 17 · 2026-05-23T01:28:56.524Z_

<details><summary>↩ Tool result · `toolu_01AFcfEgb34wqg49xjY9VP3m`</summary>

```text
total 56
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 19:00 .
drwxr-xr-x 90 ubuntu ubuntu  4096 May 23 00:32 ..
-rw-r--r--  1 ubuntu ubuntu 24788 May 22 19:00 semisynthetic_gradient.py
-rw-r--r--  1 ubuntu ubuntu  5964 May 22 19:01 semisynthetic_gradient_report.md
-rw-r--r--  1 ubuntu ubuntu 10700 May 22 19:01 semisynthetic_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "f9a93332-2732-4ef1-846f-ad3ed8b2067e"
}
```

</details>

---

### System

_source line 18_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Reading artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
  "usage": {
    "total_tokens": 17088,
    "tool_uses": 4,
    "duration_ms": 7345
  },
  "last_tool_name": "Read",
  "uuid": "55ee0d90-2363-4ac8-a378-2473a066283b",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 19_

<details open><summary>🔧 Tool call — Read · `toolu_014KgiQB92aaWV1AbeePt6mf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "94173dcb-d6f4-4e32-8a61-bb05bcadc90f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCwnDRB1LCxTZZDPXSsoMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1443,
      "cache_read_input_tokens": 15624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1443,
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

_source line 20 · 2026-05-23T01:28:59.574Z_

<details><summary>↩ Tool result · `toolu_014KgiQB92aaWV1AbeePt6mf`</summary>

```text
1	"""
2	R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection
3	Tests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.
4	"""
5	
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse, stats
9	from scipy.stats import chi2 as chi2_dist
10	import time, os, sys
11	
12	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
13	OUT = os.path.join(ROOT, "r19_semisynthetic_gradient")
14	
15	N_SEEDS = 5
16	N_STRATA = 5
17	FOC_INJECT_FRAC = 0.30
18	ITEM_INJECT_FRAC = 0.24
19	
20	# ════════════════════════════════════════════════════════════════════════════
21	#  VECTORIZED MH-DIF — returns per-item results
22	# ════════════════════════════════════════════════════════════════════════════
23	def mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):
24	    """Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction."""
25	    n_ref, J = X_ref.shape
26	    n_foc = X_foc.shape[0]
27	
28	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
29	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
30	    s_all = np.concatenate([tot_ref, tot_foc])
31	
32	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
33	    n_bins = len(edges) - 1
34	    if n_bins < 1:
35	        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
36	
37	    k_ref = np.digitize(tot_ref, edges[1:-1])
38	    k_foc = np.digitize(tot_foc, edges[1:-1])
39	
40	    n1 = np.zeros(n_bins, dtype=np.float64)
41	    n0 = np.zeros(n_bins, dtype=np.float64)
42	    A = np.zeros((n_bins, J), dtype=np.float64)
43	    C_mat = np.zeros((n_bins, J), dtype=np.float64)
44	
45	    for k in range(n_bins):
46	        mr = (k_ref == k)
47	        mf = (k_foc == k)
48	        n1[k] = mr.sum()
49	        n0[k] = mf.sum()
50	        if mr.any():
51	            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
52	        if mf.any():
53	            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)
54	
55	    B = n1[:, None] - A
56	    D = n0[:, None] - C_mat
57	    Nk = (n1 + n0)[:, None]
58	    m1 = A + C_mat
59	    m0 = B + D
60	
61	    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
62	             (Nk > 1) & (m1 > 0) & (m0 > 0))
63	
64	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
65	    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)
66	
67	    finite_mask = (Rj > 0) & (Sj > 0)
68	
69	    with np.errstate(divide="ignore", invalid="ignore"):
70	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
71	
72	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
73	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
74	
75	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
76	    sum_var = np.where(
77	        valid,
78	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
79	        0,
80	    ).sum(axis=0)
81	
82	    chi2_j = np.where(
83	        sum_var > 0,
84	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
85	        0,
86	    )
87	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
88	
89	    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
90	
91	    return delta_j, pval_j, is_c
92	
93	
94	# ════════════════════════════════════════════════════════════════════════════
95	#  LOAD DATA
96	# ════════════════════════════════════════════════════════════════════════════
97	print("Loading data...")
98	rm = np.load(f"{ROOT}/response_matrix.npz")
99	X_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))
100	idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
101	model_names = idx['model_names']
102	item_ids = idx['item_ids']
103	
104	meta = pd.read_csv(f"{ROOT}/model_metadata.csv")
105	name_to_row = {n: i for i, n in enumerate(model_names)}
106	
107	ref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values
108	foc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values
109	
110	ref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])
111	foc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])
112	
113	N_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)
114	N_inject_models = int(N_foc * FOC_INJECT_FRAC)
115	N_inject_items = int(J * ITEM_INJECT_FRAC)
116	
117	print(f"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}")
118	print(f"  Injection targets: {N_inject_models} models, {N_inject_items} items")
119	
120	# Densify the ref/foc submatrices
121	X_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)
122	X_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)
123	
124	# Ref cohort accuracy per item (= item difficulty proxy)
125	item_difficulty = X_ref_base.mean(axis=0)  # shape (J,)
126	
127	print(f"  Item difficulty: mean={item_difficulty.mean():.3f}, "
128	      f"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}")
129	
130	# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)
131	item_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])
132	unique_subjects = np.unique(item_subjects)
133	print(f"  Unique subjects: {len(unique_subjects)}")
134	
135	
136	# ════════════════════════════════════════════════════════════════════════════
137	#  INJECTION SCHEMES
138	# ════════════════════════════════════════════════════════════════════════════
139	def inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):
140	    """Capability-like: injection probability ∝ difficulty (easy items more likely flipped)."""
141	    X = X_foc.copy()
142	    n_flipped = 0
143	    for j in inject_item_idx:
144	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
145	        for i in np.where(inject_model_mask)[0]:
146	            if X[i, j] == 0 and rng.random() < p_inject:
147	                X[i, j] = 1
148	                n_flipped += 1
149	    return X, n_flipped
150	
151	
152	def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
153	    """Contamination-like: uniform injection probability, restricted to 5 random subjects."""
154	    X = X_foc.copy()
155	    n_flipped = 0
156	    for j in inject_item_idx:
157	        for i in np.where(inject_model_mask)[0]:
158	            if X[i, j] == 0 and rng.random() < p_const:
159	                X[i, j] = 1
160	                n_flipped += 1
161	    return X, n_flipped
162	
163	
164	def inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,
165	                    item_diff, rng, p_const=0.5):
166	    """Mixed: half items use scheme A, half use scheme B."""
167	    X = X_foc.copy()
168	    n_flipped = 0
169	    # Scheme A half
170	    for j in inject_item_idx_a:
171	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
172	        for i in np.where(inject_model_mask)[0]:
173	            if X[i, j] == 0 and rng.random() < p_inject:
174	                X[i, j] = 1
175	                n_flipped += 1
176	    # Scheme B half
177	    for j in inject_item_idx_b:
178	        for i in np.where(inject_model_mask)[0]:
179	            if X[i, j] == 0 and rng.random() < p_const:
180	                X[i, j] = 1
181	                n_flipped += 1
182	    return X, n_flipped
183	
184	
185	# ════════════════════════════════════════════════════════════════════════════
186	#  BASELINE (no injection)
187	# ════════════════════════════════════════════════════════════════════════════
188	print("\n=== Baseline (no injection) ===")
189	delta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)
190	c_idx_base = np.where(is_c_base)[0]
191	rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])
192	n_c_base = is_c_base.sum()
193	# δ > 0 = focal-favoring, δ < 0 = ref-favoring
194	n_focal_base = (is_c_base & (delta_base > 0)).sum()
195	n_ref_base = (is_c_base & (delta_base < 0)).sum()
196	print(f"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, "
197	      f"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}")
198	
199	
200	# ════════════════════════════════════════════════════════════════════════════
201	#  RUN EXPERIMENTS
202	# ════════════════════════════════════════════════════════════════════════════
203	print("\n=== Running experiments ===")
204	results = []
205	t0 = time.time()
206	
207	for seed in range(1, N_SEEDS + 1):
208	    rng = np.random.RandomState(seed * 42)
209	
210	    # Select injection models and items (shared across schemes within seed)
211	    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)
212	    inject_model_mask = np.zeros(N_foc, dtype=bool)
213	    inject_model_mask[inject_model_idx] = True
214	
215	    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)
216	
217	    # Scheme B: select 5 random subjects, pick injection items from those subjects
218	    selected_subjects = rng.choice(unique_subjects, 5, replace=False)
219	    subject_mask = np.isin(item_subjects, selected_subjects)
220	    subject_item_pool = np.where(subject_mask)[0]
221	    n_b_items = min(N_inject_items, len(subject_item_pool))
222	    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
223	
224	    # Scheme C: split A items in half
225	    half = N_inject_items // 2
226	    inject_item_idx_c_a = inject_item_idx_all[:half]
227	    # For scheme C's B half, pick from 5 random subjects
228	    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)
229	    subject_mask_c = np.isin(item_subjects, selected_subjects_c)
230	    subject_pool_c = np.where(subject_mask_c)[0]
231	    # Exclude items already used by A half
232	    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)
233	    n_c_b = min(half, len(subject_pool_c))
234	    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)
235	
236	    schemes = {
237	        'A_capability': lambda: inject_scheme_a(
238	            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),
239	        'B_contamination': lambda: inject_scheme_b(
240	            X_foc_base, inject_model_mask, inject_item_idx_b, rng),
241	        'C_mixed': lambda: inject_scheme_c(
242	            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,
243	            item_difficulty, rng),
244	    }
245	
246	    for scheme_name, inject_fn in schemes.items():
247	        t1 = time.time()
248	
249	        X_foc_inj, n_flipped = inject_fn()
250	
251	        # Determine which items were injected for this scheme
252	        if scheme_name == 'A_capability':
253	            injected_items = set(inject_item_idx_all)
254	        elif scheme_name == 'B_contamination':
255	            injected_items = set(inject_item_idx_b)
256	        else:  # C_mixed
257	            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)
258	
259	        # Run MH-DIF
260	        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)
261	
262	        # Delta change from baseline (isolates injection effect)
263	        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive
264	        ddelta = delta_j - delta_base
265	
266	        # C% among all / injected / non-injected items
267	        inj_arr = np.array(sorted(injected_items))
268	        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))
269	        c_pct_all = is_c.sum() / J * 100
270	        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0
271	        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100
272	
273	        # ρ(difficulty, δ) among all C items
274	        c_idx = np.where(is_c)[0]
275	        rho_all = np.nan
276	        if len(c_idx) >= 3:
277	            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])
278	
279	        # ρ(difficulty, δ) among injected C items
280	        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)
281	        c_inj_idx = np.where(c_inj_mask)[0]
282	        rho_inj = np.nan
283	        if len(c_inj_idx) >= 3:
284	            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])
285	
286	        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal
287	        rho_ddelta_inj = np.nan
288	        if len(inj_arr) >= 3:
289	            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])
290	
291	        # ρ(difficulty, Δδ) among all items
292	        rho_ddelta_all = np.nan
293	        if J >= 3:
294	            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)
295	
296	        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring
297	        n_c_total = is_c.sum()
298	        n_focal_favoring = (is_c & (delta_j > 0)).sum()
299	        n_ref_favoring = (is_c & (delta_j < 0)).sum()
300	        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
301	
302	        # Direction among injected C items
303	        n_c_inj = c_inj_mask.sum()
304	        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()
305	        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0
306	
307	        # Newly flagged items (C after injection but not in baseline)
308	        newly_c = is_c & ~is_c_base
309	        n_newly_c = newly_c.sum()
310	        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)
311	        n_newly_c_inj = newly_c_inj.sum()
312	
313	        # Mean Δδ among injected items (injection effect magnitude)
314	        mean_ddelta_inj = ddelta[inj_arr].mean()
315	
316	        # Per-quintile analysis
317	        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
318	        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])
319	        quintile_data = {}
320	        for q in range(5):
321	            q_mask = (quintile_labels == q)
322	            q_items = np.where(q_mask)[0]
323	            q_inj_items = np.intersect1d(q_items, inj_arr)
324	            q_c = is_c[q_items].sum()
325	            q_total = len(q_items)
326	            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0
327	            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()
328	            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0
329	            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0
330	            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0
331	            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0
332	            quintile_data[f'q{q+1}_c_pct'] = q_c_pct
333	            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal
334	            quintile_data[f'q{q+1}_n_c'] = q_c
335	            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj
336	            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)
337	            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta
338	
339	        elapsed = time.time() - t1
340	        row = dict(
341	            scheme=scheme_name, seed=seed,
342	            n_inject_models=N_inject_models,
343	            n_inject_items=len(injected_items),
344	            n_flipped=n_flipped,
345	            c_pct_all=c_pct_all,
346	            c_pct_inj=c_pct_inj,
347	            c_pct_noninj=c_pct_noninj,
348	            n_c_total=n_c_total,
349	            n_c_inj=n_c_inj,
350	            rho_all=rho_all,
351	            rho_inj=rho_inj,
352	            rho_ddelta_inj=rho_ddelta_inj,
353	            rho_ddelta_all=rho_ddelta_all,
354	            pct_focal=pct_focal,
355	            pct_focal_inj=pct_focal_inj,
356	            n_focal_favoring=n_focal_favoring,
357	            n_ref_favoring=n_ref_favoring,
358	            n_newly_c=n_newly_c,
359	            n_newly_c_inj=n_newly_c_inj,
360	            mean_ddelta_inj=mean_ddelta_inj,
361	            elapsed_sec=elapsed,
362	        )
363	        row.update(quintile_data)
364	        results.append(row)
365	        print(f"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, "
366	              f"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, "
367	              f"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s")
368	
369	total_time = time.time() - t0
370	print(f"\nTotal time: {total_time:.0f}s")
371	
372	
373	# ════════════════════════════════════════════════════════════════════════════
374	#  SAVE RESULTS
375	# ════════════════════════════════════════════════════════════════════════════
376	df = pd.DataFrame(results)
377	df.to_csv(os.path.join(OUT, "semisynthetic_results.csv"), index=False)
378	print(f"\nSaved: semisynthetic_results.csv ({len(df)} rows)")
379	
380	
381	# ════════════════════════════════════════════════════════════════════════════
382	#  GENERATE REPORT
383	# ════════════════════════════════════════════════════════════════════════════
384	report_lines = ["# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n"]
385	report_lines.append(f"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
386	report_lines.append(f"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), "
387	                    f"{N_foc} foc models (2024), {J} items\n")
388	report_lines.append(f"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), "
389	                    f"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\n")
390	
391	report_lines.append(f"\n## Baseline (no injection)\n")
392	report_lines.append(f"- C%: {n_c_base/J*100:.2f}%")
393	report_lines.append(f"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}")
394	report_lines.append(f"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%")
395	report_lines.append(f"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%")
396	report_lines.append(f"- N DIF-C: {n_c_base}")
397	
398	for scheme in ['A_capability', 'B_contamination', 'C_mixed']:
399	    sub = df[df['scheme'] == scheme]
400	    report_lines.append(f"\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\n")
401	
402	    report_lines.append(f"| Metric | Mean ± SD |")
403	    report_lines.append(f"|--------|-----------|")
404	    report_lines.append(f"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |")
405	    report_lines.append(f"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |")
406	    report_lines.append(f"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |")
407	    report_lines.append(f"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |")
408	    report_lines.append(f"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |")
409	    report_lines.append(f"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |")
410	    report_lines.append(f"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |")
411	    report_lines.append(f"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |")
412	    report_lines.append(f"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |")
413	    report_lines.append(f"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |")
414	    report_lines.append(f"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |")
415	    report_lines.append(f"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |")
416	    report_lines.append(f"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |")
417	    report_lines.append(f"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |")
418	    report_lines.append(f"| Items injected | {sub['n_inject_items'].mean():.0f} |")
419	
420	    report_lines.append(f"\n### Quintile Breakdown\n")
421	    report_lines.append(f"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |")
422	    report_lines.append(f"|----------|----------|----------|---------|---------------|-----|-------|")
423	    for q in range(1, 6):
424	        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}
425	        if cols['c_pct'] in sub.columns:
426	            report_lines.append(
427	                f"| Q{q} | {sub[cols['c_pct']].mean():.1f} | "
428	                f"{sub[cols['c_pct_inj']].mean():.1f} | "
429	                f"{sub[cols['pct_focal']].mean():.1f} | "
430	                f"{sub[cols['mean_ddelta']].mean():.3f} | "
431	                f"{sub[cols['n_c']].mean():.0f} | "
432	                f"{sub[cols['n_inj']].mean():.0f} |")
433	
434	report_lines.append(f"\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n")
435	report_lines.append("Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n")
436	report_lines.append(f"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |")
437	report_lines.append(f"|--------|---------------------|-----------------|----------|")
438	for scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),
439	                         ('B_contamination', '≈ 0 (uniform)'),
440	                         ('C_mixed', 'intermediate')]:
441	    sub = df[df['scheme'] == scheme]
442	    report_lines.append(f"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | "
443	                       f"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |")
444	
445	report_lines.append(f"\n## Interpretation\n")
446	report_lines.append("**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. "
447	                    "Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\n")
448	report_lines.append("### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\n")
449	report_lines.append("1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. "
450	                    "Injection probability ∝ item accuracy → easy items receive more flips → "
451	                    "larger focal-favoring Δδ on easy items. Strong positive correlation.")
452	report_lines.append("2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). "
453	                    "Uniform p=0.5 injection gives equal probability per response, but hard items "
454	                    "have more 0→1 flippable responses (ceiling effect). "
455	                    "Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.")
456	report_lines.append("3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, "
457	                    "as expected from mixing both injection mechanisms.\n")
458	report_lines.append("### Ceiling effect insight\n")
459	report_lines.append("The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability "
460	                    "does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → "
461	                    "small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. "
462	                    "This ceiling effect is an inherent property of binary response matrices and means "
463	                    "the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' "
464	                    "but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\n")
465	report_lines.append("### Discriminability\n")
466	report_lines.append("- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds")
467	report_lines.append("- A vs C separation: Δρ ≈ 0.38, clear but smaller")
468	report_lines.append("- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone")
469	
470	report_text = "\n".join(report_lines) + "\n"
471	
472	with open(os.path.join(OUT, "semisynthetic_gradient_report.md"), "w") as f:
473	    f.write(report_text)
474	
475	print(f"Saved: semisynthetic_gradient_report.md")
476	print("\n" + report_text)
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "8c07b63d-1482-41d6-88bc-1e210f3d5bf7"
}
```

</details>

---

### System

_source line 21_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Reading artifacts/r19_semisynthetic_gradient/semisynthetic_gradient_report.md",
  "usage": {
    "total_tokens": 17089,
    "tool_uses": 5,
    "duration_ms": 7434
  },
  "last_tool_name": "Read",
  "uuid": "03ab9af6-1516-43a1-9496-f31c2e7efd6a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_015oYuAUWonorShb9gBzvH6T`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "6ff2c178-3442-4c35-ae84-52f663daa54e",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCwnDRB1LCxTZZDPXSsoMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1443,
      "cache_read_input_tokens": 15624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1443,
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

_source line 23 · 2026-05-23T01:28:59.667Z_

<details><summary>↩ Tool result · `toolu_015oYuAUWonorShb9gBzvH6T`</summary>

```text
1	# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection
2	
3	**Date**: 2026-05-22 19:01
4	
5	**Config**: 5 seeds, 1080 ref models (2023), 807 foc models (2024), 12508 items
6	
7	**Injection**: 242 foc models (30%), ~3001 items (24%)
8	
9	
10	## Baseline (no injection)
11	
12	- C%: 31.32%
13	- ρ(difficulty, δ_MH) among C: -0.587
14	- % focal-favoring (δ>0): 43.9%
15	- % ref-favoring (δ<0): 56.1%
16	- N DIF-C: 3918
17	
18	## Scheme A — Capability
19	
20	| Metric | Mean ± SD |
21	|--------|-----------|
22	| C% (all items) | 31.88 ± 0.65 |
23	| C% (injected items) | 27.33 ± 0.94 |
24	| C% (non-injected) | 33.32 ± 0.82 |
25	| ρ(diff, δ) all C | -0.532 ± 0.021 |
26	| ρ(diff, δ) injected C | -0.229 ± 0.058 |
27	| **ρ(diff, Δδ) injected items** | **0.771 ± 0.029** |
28	| ρ(diff, Δδ) all items | -0.160 ± 0.131 |
29	| % focal-favoring (all C, δ>0) | 45.8 ± 1.3 |
30	| % focal-favoring (inj C, δ>0) | 85.2 ± 1.5 |
31	| N DIF-C items | 3988 ± 81 |
32	| N DIF-C (injected) | 820 ± 28 |
33	| Newly flagged C | 725 ± 74 |
34	| Mean Δδ (injected items) | 0.796 ± 0.049 |
35	| Responses flipped | 102528 ± 3208 |
36	| Items injected | 3001 |
37	
38	### Quintile Breakdown
39	
40	| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
41	|----------|----------|----------|---------|---------------|-----|-------|
42	| Q1 | 34.1 | 35.4 | 88.4 | -0.080 | 853 | 585 |
43	| Q2 | 38.5 | 35.9 | 60.3 | 0.426 | 961 | 602 |
44	| Q3 | 32.4 | 30.0 | 33.3 | 1.045 | 811 | 620 |
45	| Q4 | 31.4 | 24.5 | 21.0 | 1.378 | 777 | 596 |
46	| Q5 | 23.2 | 10.9 | 10.0 | 1.188 | 587 | 598 |
47	
48	## Scheme B — Contamination
49	
50	| Metric | Mean ± SD |
51	|--------|-----------|
52	| C% (all items) | 32.07 ± 0.79 |
53	| C% (injected items) | 39.22 ± 6.34 |
54	| C% (non-injected) | 31.46 ± 0.23 |
55	| ρ(diff, δ) all C | -0.599 ± 0.015 |
56	| ρ(diff, δ) injected C | -0.729 ± 0.047 |
57	| **ρ(diff, Δδ) injected items** | **-0.517 ± 0.107** |
58	| ρ(diff, Δδ) all items | 0.181 ± 0.136 |
59	| % focal-favoring (all C, δ>0) | 43.6 ± 0.4 |
60	| % focal-favoring (inj C, δ>0) | 85.7 ± 3.4 |
61	| N DIF-C items | 4011 ± 99 |
62	| N DIF-C (injected) | 351 ± 136 |
63	| Newly flagged C | 354 ± 150 |
64	| Mean Δδ (injected items) | 1.018 ± 0.108 |
65	| Responses flipped | 45860 ± 18588 |
66	| Items injected | 873 |
67	
68	### Quintile Breakdown
69	
70	| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
71	|----------|----------|----------|---------|---------------|-----|-------|
72	| Q1 | 38.2 | 87.4 | 90.2 | 1.938 | 956 | 210 |
73	| Q2 | 39.9 | 40.5 | 59.4 | 0.829 | 996 | 208 |
74	| Q3 | 32.8 | 27.4 | 25.1 | 0.698 | 820 | 175 |
75	| Q4 | 28.8 | 18.2 | 11.1 | 0.744 | 713 | 137 |
76	| Q5 | 20.8 | 9.4 | 2.1 | 0.682 | 526 | 144 |
77	
78	## Scheme C — Mixed
79	
80	| Metric | Mean ± SD |
81	|--------|-----------|
82	| C% (all items) | 31.98 ± 0.54 |
83	| C% (injected items) | 31.28 ± 2.87 |
84	| C% (non-injected) | 32.18 ± 0.25 |
85	| ρ(diff, δ) all C | -0.561 ± 0.017 |
86	| ρ(diff, δ) injected C | -0.496 ± 0.028 |
87	| **ρ(diff, Δδ) injected items** | **0.394 ± 0.053** |
88	| ρ(diff, Δδ) all items | -0.008 ± 0.101 |
89	| % focal-favoring (all C, δ>0) | 45.8 ± 1.6 |
90	| % focal-favoring (inj C, δ>0) | 83.8 ± 2.7 |
91	| N DIF-C items | 4000 ± 67 |
92	| N DIF-C (injected) | 749 ± 99 |
93	| Newly flagged C | 626 ± 51 |
94	| Mean Δδ (injected items) | 0.850 ± 0.039 |
95	| Responses flipped | 93752 ± 14432 |
96	| Items injected | 2407 |
97	
98	### Quintile Breakdown
99	
100	| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |
101	|----------|----------|----------|---------|---------------|-----|-------|
102	| Q1 | 37.2 | 53.8 | 89.2 | 0.600 | 931 | 469 |
103	| Q2 | 39.1 | 36.4 | 60.0 | 0.554 | 978 | 493 |
104	| Q3 | 32.6 | 30.1 | 29.5 | 0.926 | 815 | 467 |
105	| Q4 | 29.7 | 23.6 | 17.8 | 1.169 | 735 | 474 |
106	| Q5 | 21.4 | 12.5 | 8.3 | 1.029 | 542 | 503 |
107	
108	## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated
109	
110	Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.
111	
112	| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |
113	|--------|---------------------|-----------------|----------|
114	| A_capability | 0.771 ± 0.029 | -0.160 ± 0.131 | positive (easy→more focal DIF) |
115	| B_contamination | -0.517 ± 0.107 | 0.181 ± 0.136 | ≈ 0 (uniform) |
116	| C_mixed | 0.394 ± 0.053 | -0.008 ± 0.101 | intermediate |
117	
118	## Interpretation
119	
120	**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.
121	
122	### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures
123	
124	1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. Injection probability ∝ item accuracy → easy items receive more flips → larger focal-favoring Δδ on easy items. Strong positive correlation.
125	2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). Uniform p=0.5 injection gives equal probability per response, but hard items have more 0→1 flippable responses (ceiling effect). Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.
126	3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, as expected from mixing both injection mechanisms.
127	
128	### Ceiling effect insight
129	
130	The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. This ceiling effect is an inherent property of binary response matrices and means the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.
131	
132	### Discriminability
133	
134	- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds
135	- A vs C separation: Δρ ≈ 0.38, clear but smaller
136	- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone
137	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "4de6f5dc-c2b2-4c7a-b7c3-3bc601300d6b"
}
```

</details>

---

### System

_source line 24_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Reading artifacts/model_metadata.csv",
  "usage": {
    "total_tokens": 17090,
    "tool_uses": 6,
    "duration_ms": 7450
  },
  "last_tool_name": "Read",
  "uuid": "a4f8a84a-03f6-40e2-be29-30c2a50a708b",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_0122pBDzGGi9ZvR1FN7wEgpB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv",
  "limit": 10
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "91259177-3844-4c1a-a1ec-40733a960959",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01TCwnDRB1LCxTZZDPXSsoMT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1443,
      "cache_read_input_tokens": 15624,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1443,
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

_source line 26 · 2026-05-23T01:28:59.676Z_

<details><summary>↩ Tool result · `toolu_0122pBDzGGi9ZvR1FN7wEgpB`</summary>

```text
1	model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
2	0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
3	0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
4	0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
5	0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3
6	0-hero/Matter-0.1-7B-boost-DPO-preview,,unknown,unknown,DPO,0.65614,other,3
7	0-hero/Matter-0.1-Slim-7B,unknown,unknown,unknown,unknown,0.62456,other,2
8	0-hero/Matter-0.1-Slim-7B-A,unknown,unknown,unknown,unknown,0.62456,other,2
9	0-hero/Matter-0.1-Slim-7B-B,unknown,unknown,unknown,unknown,0.633435,other,3
10	0-hero/Matter-0.1-Slim-7B-C,unknown,unknown,unknown,unknown,0.642709,other,3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "98882ef2-0588-4669-b545-39475ea11914"
}
```

</details>

---

### System

_source line 27_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "description": "Running python3 << 'EOF'\nimport numpy as np\nfrom scipy impo…",
  "usage": {
    "total_tokens": 30989,
    "tool_uses": 7,
    "duration_ms": 12847
  },
  "last_tool_name": "Bash",
  "uuid": "6b88c069-f95f-4e38-9834-b95b4212389a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Bash · `toolu_0115roHtoQFiKrr7sqLb2kNk`</summary>

```json
{
  "command": "python3 << 'EOF'\nimport numpy as np\nfrom scipy import sparse\n\n# Load response_matrix.npz\nprint(\"=== response_matrix.npz ===\")\nrm = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz\")\nprint(\"Keys:\", list(rm.files))\nprint(f\"Shape: {rm['shape']}\")\nprint(f\"Data dtype: {rm['data'].dtype}, shape: {rm['data'].shape}\")\nprint(f\"Data sample (first 20): {rm['data'][:20]}\")\nprint(f\"Indices dtype: {rm['indices'].dtype}, shape: {rm['indices'].shape}\")\nprint(f\"Indices sample (first 20): {rm['indices'][:20]}\")\nprint(f\"Indptr dtype: {rm['indptr'].dtype}, shape: {rm['indptr'].shape}\")\nprint(f\"Indptr sample (first 20): {rm['indptr'][:20]}\")\n\n# Reconstruct sparse matrix\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nprint(f\"\\nReconstructed sparse matrix: {X.shape}, dtype: {X.dtype}, nnz: {X.nnz}\")\nprint(f\"Density: {X.nnz / (X.shape[0] * X.shape[1]):.4f}\")\n\n# Load response_matrix_index.npz\nprint(\"\\n=== response_matrix_index.npz ===\")\nidx = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz\", allow_pickle=True)\nprint(\"Keys:\", list(idx.files))\nprint(f\"model_names shape: {idx['model_names'].shape}, dtype: {idx['model_names'].dtype}\")\nprint(f\"model_names (first 10): {idx['model_names'][:10]}\")\nprint(f\"item_ids shape: {idx['item_ids'].shape}, dtype: {idx['item_ids'].dtype}\")\nprint(f\"item_ids (first 10): {idx['item_ids'][:10]}\")\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "39d1a5d7-411f-4107-a68f-f9545c6b7f70",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CCDgeEbDfK1U9eCr4YoWfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 13897,
      "cache_read_input_tokens": 17067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 13897,
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

### System

_source line 29_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b011huub3",
  "tool_use_id": "toolu_0115roHtoQFiKrr7sqLb2kNk",
  "description": "python3 << 'EOF'\nimport numpy as np\nfrom scipy import sparse\n\n# Load response_matrix.npz\nprint(\"=== response_matrix.npz ===\")\nrm = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz\")\nprint(\"Keys:\", list(rm.files))\nprint(f\"Shape: {rm['shape']}\")\nprint(f\"Data dtype: {rm['data'].dtype}, shape: {rm['data'].shape}\")\nprint(f\"Data sample (first 20): {rm['data'][:20]}\")\nprint(f\"Indices dtype: {rm['indices'].dtype}, shape: {rm['indices'].shape}\")\nprint(f\"Indices sample (first 20): {rm['indices'][:20]}\")\nprint(f\"Indptr dtype: {rm['indptr'].dtype}, shape: {rm['indptr'].shape}\")\nprint(f\"Indptr sample (first 20): {rm['indptr'][:20]}\")\n\n# Reconstruct sparse matrix\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nprint(f\"\\nReconstructed sparse matrix: {X.shape}, dtype: {X.dtype}, nnz: {X.nnz}\")\nprint(f\"Density: {X.nnz / (X.shape[0] * X.shape[1]):.4f}\")\n\n# Load response_matrix_index.npz\nprint(\"\\n=== response_matrix_index.npz ===\")\nidx = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz\", allow_pickle=True)\nprint(\"Keys:\", list(idx.files))\nprint(f\"model_names shape: {idx['model_names'].shape}, dtype: {idx['model_names'].dtype}\")\nprint(f\"model_names (first 10): {idx['model_names'][:10]}\")\nprint(f\"item_ids shape: {idx['item_ids'].shape}, dtype: {idx['item_ids'].dtype}\")\nprint(f\"item_ids (first 10): {idx['item_ids'][:10]}\")\nEOF\n",
  "task_type": "local_bash",
  "uuid": "274bf2e2-ad3f-4426-938a-ce880339dbfe",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### System

_source line 30_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b011huub3",
  "tool_use_id": "toolu_0115roHtoQFiKrr7sqLb2kNk",
  "status": "completed",
  "output_file": "",
  "summary": "python3 << 'EOF'\nimport numpy as np\nfrom scipy import sparse\n\n# Load response_matrix.npz\nprint(\"=== response_matrix.npz ===\")\nrm = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix.npz\")\nprint(\"Keys:\", list(rm.files))\nprint(f\"Shape: {rm['shape']}\")\nprint(f\"Data dtype: {rm['data'].dtype}, shape: {rm['data'].shape}\")\nprint(f\"Data sample (first 20): {rm['data'][:20]}\")\nprint(f\"Indices dtype: {rm['indices'].dtype}, shape: {rm['indices'].shape}\")\nprint(f\"Indices sample (first 20): {rm['indices'][:20]}\")\nprint(f\"Indptr dtype: {rm['indptr'].dtype}, shape: {rm['indptr'].shape}\")\nprint(f\"Indptr sample (first 20): {rm['indptr'][:20]}\")\n\n# Reconstruct sparse matrix\nX = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nprint(f\"\\nReconstructed sparse matrix: {X.shape}, dtype: {X.dtype}, nnz: {X.nnz}\")\nprint(f\"Density: {X.nnz / (X.shape[0] * X.shape[1]):.4f}\")\n\n# Load response_matrix_index.npz\nprint(\"\\n=== response_matrix_index.npz ===\")\nidx = np.load(\"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_matrix_index.npz\", allow_pickle=True)\nprint(\"Keys:\", list(idx.files))\nprint(f\"model_names shape: {idx['model_names'].shape}, dtype: {idx['model_names'].dtype}\")\nprint(f\"model_names (first 10): {idx['model_names'][:10]}\")\nprint(f\"item_ids shape: {idx['item_ids'].shape}, dtype: {idx['item_ids'].dtype}\")\nprint(f\"item_ids (first 10): {idx['item_ids'][:10]}\")\nEOF\n",
  "uuid": "3a174a0c-d2b5-4130-b413-077bf4699e8f",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool result

_source line 31 · 2026-05-23T01:29:09.427Z_

<details><summary>↩ Tool result · `toolu_0115roHtoQFiKrr7sqLb2kNk`</summary>

```text
=== response_matrix.npz ===
Keys: ['indices', 'indptr', 'format', 'shape', 'data']
Shape: [ 5227 12508]
Data dtype: int8, shape: (38654082,)
Data sample (first 20): [1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1]
Indices dtype: int32, shape: (38654082,)
Indices sample (first 20): [ 92  95  96  98 101 102 103 105 107 108 111 112 114 115 116 117 118 119
 121 122]
Indptr dtype: int32, shape: (5228,)
Indptr sample (first 20): [     0   7007  15279  23452  31644  39851  47663  55475  63398  71437
  79381  87455  97050 105252 113519 123442 133397 143182 153133 161381]

Reconstructed sparse matrix: (5227, 12508), dtype: int8, nnz: 38654082
Density: 0.5912

=== response_matrix_index.npz ===
Keys: ['model_names', 'item_ids']
model_names shape: (5227,), dtype: object
model_names (first 10): ['0-hero/Matter-0.1-7B' '0-hero/Matter-0.1-7B-DPO-preview'
 '0-hero/Matter-0.1-7B-boost' '0-hero/Matter-0.1-7B-boost-DPO'
 '0-hero/Matter-0.1-7B-boost-DPO-preview' '0-hero/Matter-0.1-Slim-7B'
 '0-hero/Matter-0.1-Slim-7B-A' '0-hero/Matter-0.1-Slim-7B-B'
 '0-hero/Matter-0.1-Slim-7B-C' '0-hero/Matter-0.1-Slim-7B-C-DPO']
item_ids shape: (12508,), dtype: object
item_ids (first 10): ['abstract_algebra.1' 'abstract_algebra.10' 'abstract_algebra.100'
 'abstract_algebra.11' 'abstract_algebra.12' 'abstract_algebra.13'
 'abstract_algebra.14' 'abstract_algebra.15' 'abstract_algebra.16'
 'abstract_algebra.17']
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "db50179e-ae95-4506-9bc2-65f5743babe4"
}
```

</details>

---

### System

_source line 32_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a7da8593ef2e8328f",
  "tool_use_id": "toolu_01PVpYHhCTFZS2uyht5A1pLh",
  "status": "completed",
  "output_file": "",
  "summary": "Explore semi-synthetic code",
  "usage": {
    "total_tokens": 32290,
    "tool_uses": 7,
    "duration_ms": 47790
  },
  "uuid": "2ef9b392-a103-456a-bf54-c70f1f93c67a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool result

_source line 33 · 2026-05-23T01:29:40.013Z_

<details><summary>↩ Tool result · `toolu_01PVpYHhCTFZS2uyht5A1pLh`</summary>

````text
Perfect! Now let me create a comprehensive summary of my findings:

## Comprehensive Framework Documentation

Based on my thorough review of the semi-synthetic injection framework, here's a complete understanding:

### 1. **Response Matrix Loading**

The system loads a sparse matrix from two NPZ files:

- **`response_matrix.npz`**: Contains CSR (Compressed Sparse Row) format data:
  - `data`: int8 array of response values (38,654,082 elements) - binary responses (0/1)
  - `indices`: int32 column indices (38,654,082 elements)
  - `indptr`: int32 row pointers (5,228 elements)
  - `shape`: (5227 models, 12508 items)
  - Density: 59.12% (sparse but dense enough to densify into memory)

- **`response_matrix_index.npz`**: Contains mapping arrays:
  - `model_names`: Array of 5227 model name strings (e.g., "0-hero/Matter-0.1-7B")
  - `item_ids`: Array of 12508 item ID strings (e.g., "abstract_algebra.1")

The code reconstructs the sparse matrix as: `X_sparse = sparse.csr_matrix((data, indices, indptr), shape=(5227, 12508))`

### 2. **Ref/Focal Cohort Splitting**

From `/artifacts/model_metadata.csv`, models are split on `cohort_temporal`:

```python
ref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values  # 1,080 models
foc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values  # 807 models
```

The framework then:
- Maps model names to row indices in the response matrix
- Extracts ref/focal submatrices: `X_ref_base = X_sparse[ref_idx].toarray()` (1080×12508)
- Extracts foc submatrices: `X_foc_base = X_sparse[foc_idx].toarray()` (807×12508)
- Computes item difficulty as ref cohort accuracy: `item_difficulty = X_ref_base.mean(axis=0)` per-item mean

### 3. **Three Injection Schemes (A, B, C)**

All schemes modify responses in focal cohort on selected items/models:

**Scheme A (Capability-like)**:
```python
def inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):
    # Injection probability ∝ difficulty (easy items more likely flipped)
    p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
    # Flip 0→1 responses with this probability for selected models
```
- **Logic**: If focal models have lower accuracy on easy items, they can "memorize" easy items easily (less real learning needed). Easy items more likely flipped.
- **Result**: Easy items get positive focal-favoring DIF (δ > 0)

**Scheme B (Contamination-like)**:
```python
def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
    # Uniform injection probability p=0.5
    # Items restricted to 5 random subjects (domain-based clustering)
    p_inject = p_const  # Fixed at 0.5
```
- **Logic**: Contamination affects arbitrary items with uniform probability
- **Key insight**: Despite uniform probability, ceiling effect means hard items accumulate more flips (they have more 0s to flip), resulting in stronger negative correlation with difficulty
- **Result**: Hard items get more positive DIF shifts → negative ρ(difficulty, Δδ)

**Scheme C (Mixed)**:
```python
def inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,
                    item_diff, rng, p_const=0.5):
    # Half items use Scheme A (difficulty-dependent)
    # Half items use Scheme B (uniform) from 5 random subjects
```
- **Result**: Intermediate ρ between A and B

**Injection targets per seed** (all schemes use same targets within seed):
- `N_inject_models = int(807 * 0.30) = 242` focal models (30%)
- `N_inject_items = int(12508 * 0.24) = 3001` items (24%)

### 4. **MH-DIF Computation**

The vectorized function `mh_dif_vec(X_ref, X_foc, n_strata=5)` performs:

**Step 1: Stratification**
- Compute row totals: `tot_ref = X_ref.sum(axis=1)`, `tot_foc = X_foc.sum(axis=1)` (ability proxies)
- Combine: `s_all = concatenate([tot_ref, tot_foc])`
- Create 5 quantile-based bins: `edges = unique(quantile(s_all, linspace(0, 1, 6)))`
- Assign each person to stratum: `k_ref = digitize(tot_ref, edges)`, `k_foc = digitize(tot_foc, edges)`

**Step 2: Contingency Tables per Stratum**
For each stratum k and item j:
- `A[k,j]`: # ref correct (1s) on item j in stratum k
- `B[k,j] = n1[k] - A[k,j]`: # ref incorrect (0s)
- `C[k,j]`: # focal correct
- `D[k,j] = n0[k] - C[k,j]`: # focal incorrect
- `m1[k,j] = A + C`: # total correct
- `m0[k,j] = B + D`: # total incorrect
- `N[k] = n1[k] + n0[k]`: # total in stratum

**Step 3: Compute δ_MH per Item** (log odds ratio, -2.35 scaling)
```
Rj = Σ_k (A[k,j] * D[k,j] / N[k])  # ref×incorrect products
Sj = Σ_k (B[k,j] * C[k,j] / N[k])  # ref-incorrect×focal-correct products
δ_j = -2.35 * log(Rj / Sj)
```
- δ > 0: focal-favoring DIF (focal better)
- δ < 0: ref-favoring DIF (ref better)
- δ ≈ 0: no DIF

**Step 4: Compute χ² Test Statistic** (with continuity correction)
```
E[A] = n1 * m1 / N  (expected # ref correct under no-DIF)
Σdiff = Σ_k (A[k,j] - E[A])  (observed - expected)
Var = Σ_k (n1*n0*m1*m0 / (N²*(N-1)))  (hypergeometric variance)
χ² = max(|Σdiff| - 0.5, 0)² / Var
p_value = 1 - χ²_cdf(χ², df=1)
```

**Step 5: Flagging C-level DIF**
```
is_c = (|δ| ≥ 1.5) & (p-value < 0.05)
```
- Items must meet BOTH criteria to be flagged as statistically significant DIF

### 5. **Metrics (ρ and χ²)**

**Spearman Correlation ρ**: Measures relationship between item difficulty and DIF

- `rho_all = spearmanr(item_difficulty[C_items], delta_j[C_items])` among all flagged C items
- `rho_inj = spearmanr(item_difficulty[inj_C_items], delta_j[inj_C_items])` among injected C items
- **KEY METRIC**: `rho_ddelta_inj = spearmanr(item_difficulty[inj_items], Δδ[inj_items])` isolates injection effect
  - Δδ = δ_after_injection - δ_baseline

**χ² Test**: Already computed per-item as `chi2_j` (see step 4 above)
- One-tailed test: `p_val = 1 - chi2_cdf(chi2_j, df=1)`

**Expected Signatures**:
- **Scheme A**: ρ(difficulty, Δδ) ≈ **+0.77** (positive: easy items get more flips)
- **Scheme B**: ρ(difficulty, Δδ) ≈ **-0.52** (negative: hard items have more 0s to flip, ceiling effect)
- **Scheme C**: ρ(difficulty, Δδ) ≈ **+0.39** (intermediate from mixing A & B)

### 6. **Overall Pipeline Structure**

```
LOAD DATA
├─ response_matrix.npz → sparse 5227×12508 matrix (int8, 59% dense)
├─ response_matrix_index.npz → model names, item IDs
└─ model_metadata.csv → cohort_temporal field to split ref/focal

BASELINE (no injection)
└─ mh_dif_vec(X_ref_base, X_foc_base) → delta_base, pval_base, is_c_base

EXPERIMENTS (5 seeds × 3 schemes = 15 runs)
├─ SEED LOOP
│  ├─ Select targets (shared across schemes within seed)
│  │  ├─ 242 focal models to inject (30% of 807)
│  │  ├─ 3001 items to inject (24% of 12508)
│  │  └─ For Scheme B & C: select 5 random subjects, pick items within
│  │
│  └─ SCHEME LOOP (A, B, C)
│     ├─ inject_scheme_*() → X_foc_injected, n_flipped
│     ├─ mh_dif_vec(X_ref_base, X_foc_injected) → delta_j, pval_j, is_c
│     └─ Compute metrics:
│        ├─ C% (all / injected / non-injected items)
│        ├─ ρ(difficulty, δ) on all C items
│        ├─ ρ(difficulty, δ) on injected C items
│        ├─ ρ(difficulty, Δδ) on injected items [KEY METRIC]
│        ├─ ρ(difficulty, Δδ) on all items
│        ├─ Direction distribution (% focal vs ref favoring)
│        ├─ Per-quintile breakdown (difficulty quintiles)
│        └─ Newly flagged C items

OUTPUT
├─ semisynthetic_results.csv (15 rows: 5 seeds × 3 schemes)
└─ semisynthetic_gradient_report.md (summary tables & interpretation)
```

### 7. **Key Design Insights**

1. **Baseline subtraction (Δδ)** isolates the injection signal from any natural/baseline DIF pattern
2. **Five quantile strata** adjust for ability differences when comparing ref vs focal cohorts
3. **Ceiling effect** in Scheme B shows that uniform memorization probability on binary responses doesn't produce uniform DIF—hard items (more 0s) accumulate larger DIF shifts
4. **Spearman ρ** captures whether DIF pattern correlates with difficulty, distinguishing:
   - Capability-like: positive (learned/memorized easy things first)
   - Contamination-like: negative (contamination affects hard items more due to binary nature)
   - Mixed: intermediate signature

### Configuration Summary

- `N_SEEDS = 5`: Different random selections of models/items
- `N_STRATA = 5`: Ability quantiles for MH stratification
- `FOC_INJECT_FRAC = 0.30`: 30% of focal models selected for injection per seed
- `ITEM_INJECT_FRAC = 0.24`: 24% of items targeted for injection per seed
- Injection threshold: `|δ| ≥ 1.5` AND `p < 0.05` (joint significance)
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "d35edd36-910a-4a28-82a5-0934578d073b",
  "tool_use_result": {
    "status": "completed",
    "prompt": "I need to understand the existing semi-synthetic injection framework in this project. Please find and read all Python files in `artifacts/r19_semisynthetic_gradient/` directory under `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`. Also read the report file there. I need to understand:\n1. How the response matrix is loaded\n2. How models are split into ref/focal cohorts\n3. How injection schemes work (A, B, C)\n4. How MH-DIF is computed\n5. How metrics (rho, chi-squared) are calculated\n6. The overall structure of the experiment pipeline\n\nAlso check `artifacts/model_metadata.csv` to understand the training_method field format (just the first few lines). And check what's in `artifacts/response_matrix.npz` and `artifacts/response_matrix_index.npz` by looking at how they're loaded.\n\nBe very thorough - read all the code files completely.",
    "agentId": "a7da8593ef2e8328f",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary of my findings:\n\n## Comprehensive Framework Documentation\n\nBased on my thorough review of the semi-synthetic injection framework, here's a complete understanding:\n\n### 1. **Response Matrix Loading**\n\nThe system loads a sparse matrix from two NPZ files:\n\n- **`response_matrix.npz`**: Contains CSR (Compressed Sparse Row) format data:\n  - `data`: int8 array of response values (38,654,082 elements) - binary responses (0/1)\n  - `indices`: int32 column indices (38,654,082 elements)\n  - `indptr`: int32 row pointers (5,228 elements)\n  - `shape`: (5227 models, 12508 items)\n  - Density: 59.12% (sparse but dense enough to densify into memory)\n\n- **`response_matrix_index.npz`**: Contains mapping arrays:\n  - `model_names`: Array of 5227 model name strings (e.g., \"0-hero/Matter-0.1-7B\")\n  - `item_ids`: Array of 12508 item ID strings (e.g., \"abstract_algebra.1\")\n\nThe code reconstructs the sparse matrix as: `X_sparse = sparse.csr_matrix((data, indices, indptr), shape=(5227, 12508))`\n\n### 2. **Ref/Focal Cohort Splitting**\n\nFrom `/artifacts/model_metadata.csv`, models are split on `cohort_temporal`:\n\n```python\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values  # 1,080 models\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values  # 807 models\n```\n\nThe framework then:\n- Maps model names to row indices in the response matrix\n- Extracts ref/focal submatrices: `X_ref_base = X_sparse[ref_idx].toarray()` (1080×12508)\n- Extracts foc submatrices: `X_foc_base = X_sparse[foc_idx].toarray()` (807×12508)\n- Computes item difficulty as ref cohort accuracy: `item_difficulty = X_ref_base.mean(axis=0)` per-item mean\n\n### 3. **Three Injection Schemes (A, B, C)**\n\nAll schemes modify responses in focal cohort on selected items/models:\n\n**Scheme A (Capability-like)**:\n```python\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    # Injection probability ∝ difficulty (easy items more likely flipped)\n    p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n    # Flip 0→1 responses with this probability for selected models\n```\n- **Logic**: If focal models have lower accuracy on easy items, they can \"memorize\" easy items easily (less real learning needed). Easy items more likely flipped.\n- **Result**: Easy items get positive focal-favoring DIF (δ > 0)\n\n**Scheme B (Contamination-like)**:\n```python\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    # Uniform injection probability p=0.5\n    # Items restricted to 5 random subjects (domain-based clustering)\n    p_inject = p_const  # Fixed at 0.5\n```\n- **Logic**: Contamination affects arbitrary items with uniform probability\n- **Key insight**: Despite uniform probability, ceiling effect means hard items accumulate more flips (they have more 0s to flip), resulting in stronger negative correlation with difficulty\n- **Result**: Hard items get more positive DIF shifts → negative ρ(difficulty, Δδ)\n\n**Scheme C (Mixed)**:\n```python\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    # Half items use Scheme A (difficulty-dependent)\n    # Half items use Scheme B (uniform) from 5 random subjects\n```\n- **Result**: Intermediate ρ between A and B\n\n**Injection targets per seed** (all schemes use same targets within seed):\n- `N_inject_models = int(807 * 0.30) = 242` focal models (30%)\n- `N_inject_items = int(12508 * 0.24) = 3001` items (24%)\n\n### 4. **MH-DIF Computation**\n\nThe vectorized function `mh_dif_vec(X_ref, X_foc, n_strata=5)` performs:\n\n**Step 1: Stratification**\n- Compute row totals: `tot_ref = X_ref.sum(axis=1)`, `tot_foc = X_foc.sum(axis=1)` (ability proxies)\n- Combine: `s_all = concatenate([tot_ref, tot_foc])`\n- Create 5 quantile-based bins: `edges = unique(quantile(s_all, linspace(0, 1, 6)))`\n- Assign each person to stratum: `k_ref = digitize(tot_ref, edges)`, `k_foc = digitize(tot_foc, edges)`\n\n**Step 2: Contingency Tables per Stratum**\nFor each stratum k and item j:\n- `A[k,j]`: # ref correct (1s) on item j in stratum k\n- `B[k,j] = n1[k] - A[k,j]`: # ref incorrect (0s)\n- `C[k,j]`: # focal correct\n- `D[k,j] = n0[k] - C[k,j]`: # focal incorrect\n- `m1[k,j] = A + C`: # total correct\n- `m0[k,j] = B + D`: # total incorrect\n- `N[k] = n1[k] + n0[k]`: # total in stratum\n\n**Step 3: Compute δ_MH per Item** (log odds ratio, -2.35 scaling)\n```\nRj = Σ_k (A[k,j] * D[k,j] / N[k])  # ref×incorrect products\nSj = Σ_k (B[k,j] * C[k,j] / N[k])  # ref-incorrect×focal-correct products\nδ_j = -2.35 * log(Rj / Sj)\n```\n- δ > 0: focal-favoring DIF (focal better)\n- δ < 0: ref-favoring DIF (ref better)\n- δ ≈ 0: no DIF\n\n**Step 4: Compute χ² Test Statistic** (with continuity correction)\n```\nE[A] = n1 * m1 / N  (expected # ref correct under no-DIF)\nΣdiff = Σ_k (A[k,j] - E[A])  (observed - expected)\nVar = Σ_k (n1*n0*m1*m0 / (N²*(N-1)))  (hypergeometric variance)\nχ² = max(|Σdiff| - 0.5, 0)² / Var\np_value = 1 - χ²_cdf(χ², df=1)\n```\n\n**Step 5: Flagging C-level DIF**\n```\nis_c = (|δ| ≥ 1.5) & (p-value < 0.05)\n```\n- Items must meet BOTH criteria to be flagged as statistically significant DIF\n\n### 5. **Metrics (ρ and χ²)**\n\n**Spearman Correlation ρ**: Measures relationship between item difficulty and DIF\n\n- `rho_all = spearmanr(item_difficulty[C_items], delta_j[C_items])` among all flagged C items\n- `rho_inj = spearmanr(item_difficulty[inj_C_items], delta_j[inj_C_items])` among injected C items\n- **KEY METRIC**: `rho_ddelta_inj = spearmanr(item_difficulty[inj_items], Δδ[inj_items])` isolates injection effect\n  - Δδ = δ_after_injection - δ_baseline\n\n**χ² Test**: Already computed per-item as `chi2_j` (see step 4 above)\n- One-tailed test: `p_val = 1 - chi2_cdf(chi2_j, df=1)`\n\n**Expected Signatures**:\n- **Scheme A**: ρ(difficulty, Δδ) ≈ **+0.77** (positive: easy items get more flips)\n- **Scheme B**: ρ(difficulty, Δδ) ≈ **-0.52** (negative: hard items have more 0s to flip, ceiling effect)\n- **Scheme C**: ρ(difficulty, Δδ) ≈ **+0.39** (intermediate from mixing A & B)\n\n### 6. **Overall Pipeline Structure**\n\n```\nLOAD DATA\n├─ response_matrix.npz → sparse 5227×12508 matrix (int8, 59% dense)\n├─ response_matrix_index.npz → model names, item IDs\n└─ model_metadata.csv → cohort_temporal field to split ref/focal\n\nBASELINE (no injection)\n└─ mh_dif_vec(X_ref_base, X_foc_base) → delta_base, pval_base, is_c_base\n\nEXPERIMENTS (5 seeds × 3 schemes = 15 runs)\n├─ SEED LOOP\n│  ├─ Select targets (shared across schemes within seed)\n│  │  ├─ 242 focal models to inject (30% of 807)\n│  │  ├─ 3001 items to inject (24% of 12508)\n│  │  └─ For Scheme B & C: select 5 random subjects, pick items within\n│  │\n│  └─ SCHEME LOOP (A, B, C)\n│     ├─ inject_scheme_*() → X_foc_injected, n_flipped\n│     ├─ mh_dif_vec(X_ref_base, X_foc_injected) → delta_j, pval_j, is_c\n│     └─ Compute metrics:\n│        ├─ C% (all / injected / non-injected items)\n│        ├─ ρ(difficulty, δ) on all C items\n│        ├─ ρ(difficulty, δ) on injected C items\n│        ├─ ρ(difficulty, Δδ) on injected items [KEY METRIC]\n│        ├─ ρ(difficulty, Δδ) on all items\n│        ├─ Direction distribution (% focal vs ref favoring)\n│        ├─ Per-quintile breakdown (difficulty quintiles)\n│        └─ Newly flagged C items\n\nOUTPUT\n├─ semisynthetic_results.csv (15 rows: 5 seeds × 3 schemes)\n└─ semisynthetic_gradient_report.md (summary tables & interpretation)\n```\n\n### 7. **Key Design Insights**\n\n1. **Baseline subtraction (Δδ)** isolates the injection signal from any natural/baseline DIF pattern\n2. **Five quantile strata** adjust for ability differences when comparing ref vs focal cohorts\n3. **Ceiling effect** in Scheme B shows that uniform memorization probability on binary responses doesn't produce uniform DIF—hard items (more 0s) accumulate larger DIF shifts\n4. **Spearman ρ** captures whether DIF pattern correlates with difficulty, distinguishing:\n   - Capability-like: positive (learned/memorized easy things first)\n   - Contamination-like: negative (contamination affects hard items more due to binary nature)\n   - Mixed: intermediate signature\n\n### Configuration Summary\n\n- `N_SEEDS = 5`: Different random selections of models/items\n- `N_STRATA = 5`: Ability quantiles for MH stratification\n- `FOC_INJECT_FRAC = 0.30`: 30% of focal models selected for injection per seed\n- `ITEM_INJECT_FRAC = 0.24`: 24% of items targeted for injection per seed\n- Injection threshold: `|δ| ≥ 1.5` AND `p < 0.05` (joint significance)"
      }
    ],
    "totalDurationMs": 47792,
    "totalTokens": 35428,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1301,
      "cache_read_input_tokens": 30964,
      "output_tokens": 3157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1301
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 3157,
          "cache_read_input_tokens": 30964,
          "cache_creation_input_tokens": 1301,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1301,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 2,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 34_

Now let me read the actual code file to understand the exact implementation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "c774d12a-33de-4780-abd7-8196e5affaea",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HrkYBRYwBQXJMALFZFAtU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3548
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

_source line 35_

<details open><summary>🔧 Tool call — Glob · `toolu_01EXukdwuiJtF2DsQQ4DcHh7`</summary>

```json
{
  "pattern": "artifacts/r19_semisynthetic_gradient/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "385a962d-cff4-408d-8c19-83f7dcb16d1f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015HrkYBRYwBQXJMALFZFAtU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3548,
      "cache_read_input_tokens": 25239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3548
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

_source line 36 · 2026-05-23T01:29:44.870Z_

<details><summary>↩ Tool result · `toolu_01EXukdwuiJtF2DsQQ4DcHh7`</summary>

```text
artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "d170308a-2b98-413a-9c4c-c9e1fbc2550c",
  "tool_use_result": {
    "filenames": [
      "artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py"
    ],
    "durationMs": 13,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Read · `toolu_01LiRDPPzVvfcYmrYvttUWVk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "f194e1e5-d57c-49fc-84c8-c0e0bbfb3d94",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H4yo5HmM9Xbxysr8nMYHpL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 160,
      "cache_read_input_tokens": 28787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 160
      },
      "output_tokens": 53,
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

_source line 38 · 2026-05-23T01:29:47.734Z_

<details><summary>↩ Tool result · `toolu_01LiRDPPzVvfcYmrYvttUWVk`</summary>

```text
1	"""
2	R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection
3	Tests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.
4	"""
5	
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse, stats
9	from scipy.stats import chi2 as chi2_dist
10	import time, os, sys
11	
12	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
13	OUT = os.path.join(ROOT, "r19_semisynthetic_gradient")
14	
15	N_SEEDS = 5
16	N_STRATA = 5
17	FOC_INJECT_FRAC = 0.30
18	ITEM_INJECT_FRAC = 0.24
19	
20	# ════════════════════════════════════════════════════════════════════════════
21	#  VECTORIZED MH-DIF — returns per-item results
22	# ════════════════════════════════════════════════════════════════════════════
23	def mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):
24	    """Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction."""
25	    n_ref, J = X_ref.shape
26	    n_foc = X_foc.shape[0]
27	
28	    tot_ref = X_ref.sum(axis=1).astype(np.float64)
29	    tot_foc = X_foc.sum(axis=1).astype(np.float64)
30	    s_all = np.concatenate([tot_ref, tot_foc])
31	
32	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
33	    n_bins = len(edges) - 1
34	    if n_bins < 1:
35	        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
36	
37	    k_ref = np.digitize(tot_ref, edges[1:-1])
38	    k_foc = np.digitize(tot_foc, edges[1:-1])
39	
40	    n1 = np.zeros(n_bins, dtype=np.float64)
41	    n0 = np.zeros(n_bins, dtype=np.float64)
42	    A = np.zeros((n_bins, J), dtype=np.float64)
43	    C_mat = np.zeros((n_bins, J), dtype=np.float64)
44	
45	    for k in range(n_bins):
46	        mr = (k_ref == k)
47	        mf = (k_foc == k)
48	        n1[k] = mr.sum()
49	        n0[k] = mf.sum()
50	        if mr.any():
51	            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)
52	        if mf.any():
53	            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)
54	
55	    B = n1[:, None] - A
56	    D = n0[:, None] - C_mat
57	    Nk = (n1 + n0)[:, None]
58	    m1 = A + C_mat
59	    m0 = B + D
60	
61	    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &
62	             (Nk > 1) & (m1 > 0) & (m0 > 0))
63	
64	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
65	    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)
66	
67	    finite_mask = (Rj > 0) & (Sj > 0)
68	
69	    with np.errstate(divide="ignore", invalid="ignore"):
70	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
71	
72	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
73	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
74	
75	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
76	    sum_var = np.where(
77	        valid,
78	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),
79	        0,
80	    ).sum(axis=0)
81	
82	    chi2_j = np.where(
83	        sum_var > 0,
84	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
85	        0,
86	    )
87	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
88	
89	    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)
90	
91	    return delta_j, pval_j, is_c
92	
93	
94	# ════════════════════════════════════════════════════════════════════════════
95	#  LOAD DATA
96	# ════════════════════════════════════════════════════════════════════════════
97	print("Loading data...")
98	rm = np.load(f"{ROOT}/response_matrix.npz")
99	X_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))
100	idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
101	model_names = idx['model_names']
102	item_ids = idx['item_ids']
103	
104	meta = pd.read_csv(f"{ROOT}/model_metadata.csv")
105	name_to_row = {n: i for i, n in enumerate(model_names)}
106	
107	ref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values
108	foc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values
109	
110	ref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])
111	foc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])
112	
113	N_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)
114	N_inject_models = int(N_foc * FOC_INJECT_FRAC)
115	N_inject_items = int(J * ITEM_INJECT_FRAC)
116	
117	print(f"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}")
118	print(f"  Injection targets: {N_inject_models} models, {N_inject_items} items")
119	
120	# Densify the ref/foc submatrices
121	X_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)
122	X_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)
123	
124	# Ref cohort accuracy per item (= item difficulty proxy)
125	item_difficulty = X_ref_base.mean(axis=0)  # shape (J,)
126	
127	print(f"  Item difficulty: mean={item_difficulty.mean():.3f}, "
128	      f"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}")
129	
130	# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)
131	item_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])
132	unique_subjects = np.unique(item_subjects)
133	print(f"  Unique subjects: {len(unique_subjects)}")
134	
135	
136	# ════════════════════════════════════════════════════════════════════════════
137	#  INJECTION SCHEMES
138	# ════════════════════════════════════════════════════════════════════════════
139	def inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):
140	    """Capability-like: injection probability ∝ difficulty (easy items more likely flipped)."""
141	    X = X_foc.copy()
142	    n_flipped = 0
143	    for j in inject_item_idx:
144	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
145	        for i in np.where(inject_model_mask)[0]:
146	            if X[i, j] == 0 and rng.random() < p_inject:
147	                X[i, j] = 1
148	                n_flipped += 1
149	    return X, n_flipped
150	
151	
152	def inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):
153	    """Contamination-like: uniform injection probability, restricted to 5 random subjects."""
154	    X = X_foc.copy()
155	    n_flipped = 0
156	    for j in inject_item_idx:
157	        for i in np.where(inject_model_mask)[0]:
158	            if X[i, j] == 0 and rng.random() < p_const:
159	                X[i, j] = 1
160	                n_flipped += 1
161	    return X, n_flipped
162	
163	
164	def inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,
165	                    item_diff, rng, p_const=0.5):
166	    """Mixed: half items use scheme A, half use scheme B."""
167	    X = X_foc.copy()
168	    n_flipped = 0
169	    # Scheme A half
170	    for j in inject_item_idx_a:
171	        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))
172	        for i in np.where(inject_model_mask)[0]:
173	            if X[i, j] == 0 and rng.random() < p_inject:
174	                X[i, j] = 1
175	                n_flipped += 1
176	    # Scheme B half
177	    for j in inject_item_idx_b:
178	        for i in np.where(inject_model_mask)[0]:
179	            if X[i, j] == 0 and rng.random() < p_const:
180	                X[i, j] = 1
181	                n_flipped += 1
182	    return X, n_flipped
183	
184	
185	# ════════════════════════════════════════════════════════════════════════════
186	#  BASELINE (no injection)
187	# ════════════════════════════════════════════════════════════════════════════
188	print("\n=== Baseline (no injection) ===")
189	delta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)
190	c_idx_base = np.where(is_c_base)[0]
191	rho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])
192	n_c_base = is_c_base.sum()
193	# δ > 0 = focal-favoring, δ < 0 = ref-favoring
194	n_focal_base = (is_c_base & (delta_base > 0)).sum()
195	n_ref_base = (is_c_base & (delta_base < 0)).sum()
196	print(f"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, "
197	      f"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}")
198	
199	
200	# ════════════════════════════════════════════════════════════════════════════
201	#  RUN EXPERIMENTS
202	# ════════════════════════════════════════════════════════════════════════════
203	print("\n=== Running experiments ===")
204	results = []
205	t0 = time.time()
206	
207	for seed in range(1, N_SEEDS + 1):
208	    rng = np.random.RandomState(seed * 42)
209	
210	    # Select injection models and items (shared across schemes within seed)
211	    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)
212	    inject_model_mask = np.zeros(N_foc, dtype=bool)
213	    inject_model_mask[inject_model_idx] = True
214	
215	    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)
216	
217	    # Scheme B: select 5 random subjects, pick injection items from those subjects
218	    selected_subjects = rng.choice(unique_subjects, 5, replace=False)
219	    subject_mask = np.isin(item_subjects, selected_subjects)
220	    subject_item_pool = np.where(subject_mask)[0]
221	    n_b_items = min(N_inject_items, len(subject_item_pool))
222	    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)
223	
224	    # Scheme C: split A items in half
225	    half = N_inject_items // 2
226	    inject_item_idx_c_a = inject_item_idx_all[:half]
227	    # For scheme C's B half, pick from 5 random subjects
228	    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)
229	    subject_mask_c = np.isin(item_subjects, selected_subjects_c)
230	    subject_pool_c = np.where(subject_mask_c)[0]
231	    # Exclude items already used by A half
232	    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)
233	    n_c_b = min(half, len(subject_pool_c))
234	    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)
235	
236	    schemes = {
237	        'A_capability': lambda: inject_scheme_a(
238	            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),
239	        'B_contamination': lambda: inject_scheme_b(
240	            X_foc_base, inject_model_mask, inject_item_idx_b, rng),
241	        'C_mixed': lambda: inject_scheme_c(
242	            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,
243	            item_difficulty, rng),
244	    }
245	
246	    for scheme_name, inject_fn in schemes.items():
247	        t1 = time.time()
248	
249	        X_foc_inj, n_flipped = inject_fn()
250	
251	        # Determine which items were injected for this scheme
252	        if scheme_name == 'A_capability':
253	            injected_items = set(inject_item_idx_all)
254	        elif scheme_name == 'B_contamination':
255	            injected_items = set(inject_item_idx_b)
256	        else:  # C_mixed
257	            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)
258	
259	        # Run MH-DIF
260	        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)
261	
262	        # Delta change from baseline (isolates injection effect)
263	        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive
264	        ddelta = delta_j - delta_base
265	
266	        # C% among all / injected / non-injected items
267	        inj_arr = np.array(sorted(injected_items))
268	        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))
269	        c_pct_all = is_c.sum() / J * 100
270	        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0
271	        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100
272	
273	        # ρ(difficulty, δ) among all C items
274	        c_idx = np.where(is_c)[0]
275	        rho_all = np.nan
276	        if len(c_idx) >= 3:
277	            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])
278	
279	        # ρ(difficulty, δ) among injected C items
280	        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)
281	        c_inj_idx = np.where(c_inj_mask)[0]
282	        rho_inj = np.nan
283	        if len(c_inj_idx) >= 3:
284	            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])
285	
286	        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal
287	        rho_ddelta_inj = np.nan
288	        if len(inj_arr) >= 3:
289	            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])
290	
291	        # ρ(difficulty, Δδ) among all items
292	        rho_ddelta_all = np.nan
293	        if J >= 3:
294	            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)
295	
296	        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring
297	        n_c_total = is_c.sum()
298	        n_focal_favoring = (is_c & (delta_j > 0)).sum()
299	        n_ref_favoring = (is_c & (delta_j < 0)).sum()
300	        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0
301	
302	        # Direction among injected C items
303	        n_c_inj = c_inj_mask.sum()
304	        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()
305	        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0
306	
307	        # Newly flagged items (C after injection but not in baseline)
308	        newly_c = is_c & ~is_c_base
309	        n_newly_c = newly_c.sum()
310	        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)
311	        n_newly_c_inj = newly_c_inj.sum()
312	
313	        # Mean Δδ among injected items (injection effect magnitude)
314	        mean_ddelta_inj = ddelta[inj_arr].mean()
315	
316	        # Per-quintile analysis
317	        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])
318	        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])
319	        quintile_data = {}
320	        for q in range(5):
321	            q_mask = (quintile_labels == q)
322	            q_items = np.where(q_mask)[0]
323	            q_inj_items = np.intersect1d(q_items, inj_arr)
324	            q_c = is_c[q_items].sum()
325	            q_total = len(q_items)
326	            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0
327	            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()
328	            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0
329	            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0
330	            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0
331	            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0
332	            quintile_data[f'q{q+1}_c_pct'] = q_c_pct
333	            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal
334	            quintile_data[f'q{q+1}_n_c'] = q_c
335	            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj
336	            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)
337	            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta
338	
339	        elapsed = time.time() - t1
340	        row = dict(
341	            scheme=scheme_name, seed=seed,
342	            n_inject_models=N_inject_models,
343	            n_inject_items=len(injected_items),
344	            n_flipped=n_flipped,
345	            c_pct_all=c_pct_all,
346	            c_pct_inj=c_pct_inj,
347	            c_pct_noninj=c_pct_noninj,
348	            n_c_total=n_c_total,
349	            n_c_inj=n_c_inj,
350	            rho_all=rho_all,
351	            rho_inj=rho_inj,
352	            rho_ddelta_inj=rho_ddelta_inj,
353	            rho_ddelta_all=rho_ddelta_all,
354	            pct_focal=pct_focal,
355	            pct_focal_inj=pct_focal_inj,
356	            n_focal_favoring=n_focal_favoring,
357	            n_ref_favoring=n_ref_favoring,
358	            n_newly_c=n_newly_c,
359	            n_newly_c_inj=n_newly_c_inj,
360	            mean_ddelta_inj=mean_ddelta_inj,
361	            elapsed_sec=elapsed,
362	        )
363	        row.update(quintile_data)
364	        results.append(row)
365	        print(f"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, "
366	              f"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, "
367	              f"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s")
368	
369	total_time = time.time() - t0
370	print(f"\nTotal time: {total_time:.0f}s")
371	
372	
373	# ════════════════════════════════════════════════════════════════════════════
374	#  SAVE RESULTS
375	# ════════════════════════════════════════════════════════════════════════════
376	df = pd.DataFrame(results)
377	df.to_csv(os.path.join(OUT, "semisynthetic_results.csv"), index=False)
378	print(f"\nSaved: semisynthetic_results.csv ({len(df)} rows)")
379	
380	
381	# ════════════════════════════════════════════════════════════════════════════
382	#  GENERATE REPORT
383	# ════════════════════════════════════════════════════════════════════════════
384	report_lines = ["# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\n"]
385	report_lines.append(f"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\n")
386	report_lines.append(f"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), "
387	                    f"{N_foc} foc models (2024), {J} items\n")
388	report_lines.append(f"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), "
389	                    f"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\n")
390	
391	report_lines.append(f"\n## Baseline (no injection)\n")
392	report_lines.append(f"- C%: {n_c_base/J*100:.2f}%")
393	report_lines.append(f"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}")
394	report_lines.append(f"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%")
395	report_lines.append(f"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%")
396	report_lines.append(f"- N DIF-C: {n_c_base}")
397	
398	for scheme in ['A_capability', 'B_contamination', 'C_mixed']:
399	    sub = df[df['scheme'] == scheme]
400	    report_lines.append(f"\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\n")
401	
402	    report_lines.append(f"| Metric | Mean ± SD |")
403	    report_lines.append(f"|--------|-----------|")
404	    report_lines.append(f"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |")
405	    report_lines.append(f"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |")
406	    report_lines.append(f"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |")
407	    report_lines.append(f"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |")
408	    report_lines.append(f"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |")
409	    report_lines.append(f"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |")
410	    report_lines.append(f"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |")
411	    report_lines.append(f"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |")
412	    report_lines.append(f"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |")
413	    report_lines.append(f"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |")
414	    report_lines.append(f"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |")
415	    report_lines.append(f"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |")
416	    report_lines.append(f"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |")
417	    report_lines.append(f"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |")
418	    report_lines.append(f"| Items injected | {sub['n_inject_items'].mean():.0f} |")
419	
420	    report_lines.append(f"\n### Quintile Breakdown\n")
421	    report_lines.append(f"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |")
422	    report_lines.append(f"|----------|----------|----------|---------|---------------|-----|-------|")
423	    for q in range(1, 6):
424	        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}
425	        if cols['c_pct'] in sub.columns:
426	            report_lines.append(
427	                f"| Q{q} | {sub[cols['c_pct']].mean():.1f} | "
428	                f"{sub[cols['c_pct_inj']].mean():.1f} | "
429	                f"{sub[cols['pct_focal']].mean():.1f} | "
430	                f"{sub[cols['mean_ddelta']].mean():.3f} | "
431	                f"{sub[cols['n_c']].mean():.0f} | "
432	                f"{sub[cols['n_inj']].mean():.0f} |")
433	
434	report_lines.append(f"\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\n")
435	report_lines.append("Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\n")
436	report_lines.append(f"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |")
437	report_lines.append(f"|--------|---------------------|-----------------|----------|")
438	for scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),
439	                         ('B_contamination', '≈ 0 (uniform)'),
440	                         ('C_mixed', 'intermediate')]:
441	    sub = df[df['scheme'] == scheme]
442	    report_lines.append(f"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | "
443	                       f"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |")
444	
445	report_lines.append(f"\n## Interpretation\n")
446	report_lines.append("**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. "
447	                    "Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\n")
448	report_lines.append("### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\n")
449	report_lines.append("1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. "
450	                    "Injection probability ∝ item accuracy → easy items receive more flips → "
451	                    "larger focal-favoring Δδ on easy items. Strong positive correlation.")
452	report_lines.append("2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). "
453	                    "Uniform p=0.5 injection gives equal probability per response, but hard items "
454	                    "have more 0→1 flippable responses (ceiling effect). "
455	                    "Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.")
456	report_lines.append("3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, "
457	                    "as expected from mixing both injection mechanisms.\n")
458	report_lines.append("### Ceiling effect insight\n")
459	report_lines.append("The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability "
460	                    "does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → "
461	                    "small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. "
462	                    "This ceiling effect is an inherent property of binary response matrices and means "
463	                    "the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' "
464	                    "but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\n")
465	report_lines.append("### Discriminability\n")
466	report_lines.append("- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds")
467	report_lines.append("- A vs C separation: Δρ ≈ 0.38, clear but smaller")
468	report_lines.append("- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone")
469	
470	report_text = "\n".join(report_lines) + "\n"
471	
472	with open(os.path.join(OUT, "semisynthetic_gradient_report.md"), "w") as f:
473	    f.write(report_text)
474	
475	print(f"Saved: semisynthetic_gradient_report.md")
476	print("\n" + report_text)
477	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "3e28a74d-9e35-4f8e-9557-e16b2578d8c4",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r19_semisynthetic_gradient/semisynthetic_gradient.py",
      "content": "\"\"\"\nR19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\nTests whether MH-DIF can distinguish capability-like vs contamination-like DIF patterns.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os, sys\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"r19_semisynthetic_gradient\")\n\nN_SEEDS = 5\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF — returns per-item results\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item delta_mh, p_value, is_c, direction.\"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1),\n        0,\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),\n        0,\n    )\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_models = int(N_foc * FOC_INJECT_FRAC)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\nprint(f\"  Ref: {N_ref}, Foc: {N_foc}, Items: {J}\")\nprint(f\"  Injection targets: {N_inject_models} models, {N_inject_items} items\")\n\n# Densify the ref/foc submatrices\nX_ref_base = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Ref cohort accuracy per item (= item difficulty proxy)\nitem_difficulty = X_ref_base.mean(axis=0)  # shape (J,)\n\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}, \"\n      f\"min={item_difficulty.min():.3f}, max={item_difficulty.max():.3f}\")\n\n# Get MMLU subjects per item for Scheme B (format: subject_name.question_number)\nitem_subjects = np.array([str(iid).rsplit('.', 1)[0] for iid in item_ids])\nunique_subjects = np.unique(item_subjects)\nprint(f\"  Unique subjects: {len(unique_subjects)}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION SCHEMES\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_scheme_a(X_foc, inject_model_mask, inject_item_idx, item_diff, rng):\n    \"\"\"Capability-like: injection probability ∝ difficulty (easy items more likely flipped).\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_b(X_foc, inject_model_mask, inject_item_idx, rng, p_const=0.5):\n    \"\"\"Contamination-like: uniform injection probability, restricted to 5 random subjects.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    for j in inject_item_idx:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_scheme_c(X_foc, inject_model_mask, inject_item_idx_a, inject_item_idx_b,\n                    item_diff, rng, p_const=0.5):\n    \"\"\"Mixed: half items use scheme A, half use scheme B.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    # Scheme A half\n    for j in inject_item_idx_a:\n        p_inject = max(0.0, min(1.0, (item_diff[j] - 0.2) / 0.6))\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    # Scheme B half\n    for j in inject_item_idx_b:\n        for i in np.where(inject_model_mask)[0]:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline (no injection) ===\")\ndelta_base, pval_base, is_c_base = mh_dif_vec(X_ref_base, X_foc_base, n_strata=N_STRATA)\nc_idx_base = np.where(is_c_base)[0]\nrho_base, _ = stats.spearmanr(item_difficulty[c_idx_base], delta_base[c_idx_base])\nn_c_base = is_c_base.sum()\n# δ > 0 = focal-favoring, δ < 0 = ref-favoring\nn_focal_base = (is_c_base & (delta_base > 0)).sum()\nn_ref_base = (is_c_base & (delta_base < 0)).sum()\nprint(f\"  Baseline C%: {n_c_base/J*100:.2f}%, ρ={rho_base:.3f}, \"\n      f\"focal%={n_focal_base/n_c_base*100:.1f}%, ref%={n_ref_base/n_c_base*100:.1f}%, N_C={n_c_base}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running experiments ===\")\nresults = []\nt0 = time.time()\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection models and items (shared across schemes within seed)\n    inject_model_idx = rng.choice(N_foc, N_inject_models, replace=False)\n    inject_model_mask = np.zeros(N_foc, dtype=bool)\n    inject_model_mask[inject_model_idx] = True\n\n    inject_item_idx_all = rng.choice(J, N_inject_items, replace=False)\n\n    # Scheme B: select 5 random subjects, pick injection items from those subjects\n    selected_subjects = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask = np.isin(item_subjects, selected_subjects)\n    subject_item_pool = np.where(subject_mask)[0]\n    n_b_items = min(N_inject_items, len(subject_item_pool))\n    inject_item_idx_b = rng.choice(subject_item_pool, n_b_items, replace=False)\n\n    # Scheme C: split A items in half\n    half = N_inject_items // 2\n    inject_item_idx_c_a = inject_item_idx_all[:half]\n    # For scheme C's B half, pick from 5 random subjects\n    selected_subjects_c = rng.choice(unique_subjects, 5, replace=False)\n    subject_mask_c = np.isin(item_subjects, selected_subjects_c)\n    subject_pool_c = np.where(subject_mask_c)[0]\n    # Exclude items already used by A half\n    subject_pool_c = np.setdiff1d(subject_pool_c, inject_item_idx_c_a)\n    n_c_b = min(half, len(subject_pool_c))\n    inject_item_idx_c_b = rng.choice(subject_pool_c, n_c_b, replace=False)\n\n    schemes = {\n        'A_capability': lambda: inject_scheme_a(\n            X_foc_base, inject_model_mask, inject_item_idx_all, item_difficulty, rng),\n        'B_contamination': lambda: inject_scheme_b(\n            X_foc_base, inject_model_mask, inject_item_idx_b, rng),\n        'C_mixed': lambda: inject_scheme_c(\n            X_foc_base, inject_model_mask, inject_item_idx_c_a, inject_item_idx_c_b,\n            item_difficulty, rng),\n    }\n\n    for scheme_name, inject_fn in schemes.items():\n        t1 = time.time()\n\n        X_foc_inj, n_flipped = inject_fn()\n\n        # Determine which items were injected for this scheme\n        if scheme_name == 'A_capability':\n            injected_items = set(inject_item_idx_all)\n        elif scheme_name == 'B_contamination':\n            injected_items = set(inject_item_idx_b)\n        else:  # C_mixed\n            injected_items = set(inject_item_idx_c_a) | set(inject_item_idx_c_b)\n\n        # Run MH-DIF\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base, X_foc_inj, n_strata=N_STRATA)\n\n        # Delta change from baseline (isolates injection effect)\n        # δ > 0 = focal-favoring; injection flips focal 0→1 → pushes δ positive\n        ddelta = delta_j - delta_base\n\n        # C% among all / injected / non-injected items\n        inj_arr = np.array(sorted(injected_items))\n        non_inj_arr = np.array(sorted(set(range(J)) - injected_items))\n        c_pct_all = is_c.sum() / J * 100\n        c_pct_inj = is_c[inj_arr].sum() / len(inj_arr) * 100 if len(inj_arr) > 0 else 0\n        c_pct_noninj = is_c[non_inj_arr].sum() / len(non_inj_arr) * 100\n\n        # ρ(difficulty, δ) among all C items\n        c_idx = np.where(is_c)[0]\n        rho_all = np.nan\n        if len(c_idx) >= 3:\n            rho_all, _ = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])\n\n        # ρ(difficulty, δ) among injected C items\n        c_inj_mask = is_c & np.isin(np.arange(J), inj_arr)\n        c_inj_idx = np.where(c_inj_mask)[0]\n        rho_inj = np.nan\n        if len(c_inj_idx) >= 3:\n            rho_inj, _ = stats.spearmanr(item_difficulty[c_inj_idx], delta_j[c_inj_idx])\n\n        # ρ(difficulty, Δδ) among injected items — KEY METRIC isolating injection signal\n        rho_ddelta_inj = np.nan\n        if len(inj_arr) >= 3:\n            rho_ddelta_inj, _ = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])\n\n        # ρ(difficulty, Δδ) among all items\n        rho_ddelta_all = np.nan\n        if J >= 3:\n            rho_ddelta_all, _ = stats.spearmanr(item_difficulty, ddelta)\n\n        # Direction distribution: δ > 0 = focal-favoring, δ < 0 = ref-favoring\n        n_c_total = is_c.sum()\n        n_focal_favoring = (is_c & (delta_j > 0)).sum()\n        n_ref_favoring = (is_c & (delta_j < 0)).sum()\n        pct_focal = n_focal_favoring / n_c_total * 100 if n_c_total > 0 else 0\n\n        # Direction among injected C items\n        n_c_inj = c_inj_mask.sum()\n        n_focal_inj = (c_inj_mask & (delta_j > 0)).sum()\n        pct_focal_inj = n_focal_inj / n_c_inj * 100 if n_c_inj > 0 else 0\n\n        # Newly flagged items (C after injection but not in baseline)\n        newly_c = is_c & ~is_c_base\n        n_newly_c = newly_c.sum()\n        newly_c_inj = newly_c & np.isin(np.arange(J), inj_arr)\n        n_newly_c_inj = newly_c_inj.sum()\n\n        # Mean Δδ among injected items (injection effect magnitude)\n        mean_ddelta_inj = ddelta[inj_arr].mean()\n\n        # Per-quintile analysis\n        quintile_edges = np.quantile(item_difficulty, [0, 0.2, 0.4, 0.6, 0.8, 1.0])\n        quintile_labels = np.digitize(item_difficulty, quintile_edges[1:-1])\n        quintile_data = {}\n        for q in range(5):\n            q_mask = (quintile_labels == q)\n            q_items = np.where(q_mask)[0]\n            q_inj_items = np.intersect1d(q_items, inj_arr)\n            q_c = is_c[q_items].sum()\n            q_total = len(q_items)\n            q_c_pct = q_c / q_total * 100 if q_total > 0 else 0\n            q_focal = (is_c[q_items] & (delta_j[q_items] > 0)).sum()\n            q_pct_focal = q_focal / q_c * 100 if q_c > 0 else 0\n            q_c_inj = is_c[q_inj_items].sum() if len(q_inj_items) > 0 else 0\n            q_c_pct_inj = q_c_inj / len(q_inj_items) * 100 if len(q_inj_items) > 0 else 0\n            q_mean_ddelta = ddelta[q_inj_items].mean() if len(q_inj_items) > 0 else 0\n            quintile_data[f'q{q+1}_c_pct'] = q_c_pct\n            quintile_data[f'q{q+1}_pct_focal'] = q_pct_focal\n            quintile_data[f'q{q+1}_n_c'] = q_c\n            quintile_data[f'q{q+1}_c_pct_inj'] = q_c_pct_inj\n            quintile_data[f'q{q+1}_n_inj'] = len(q_inj_items)\n            quintile_data[f'q{q+1}_mean_ddelta'] = q_mean_ddelta\n\n        elapsed = time.time() - t1\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_models=N_inject_models,\n            n_inject_items=len(injected_items),\n            n_flipped=n_flipped,\n            c_pct_all=c_pct_all,\n            c_pct_inj=c_pct_inj,\n            c_pct_noninj=c_pct_noninj,\n            n_c_total=n_c_total,\n            n_c_inj=n_c_inj,\n            rho_all=rho_all,\n            rho_inj=rho_inj,\n            rho_ddelta_inj=rho_ddelta_inj,\n            rho_ddelta_all=rho_ddelta_all,\n            pct_focal=pct_focal,\n            pct_focal_inj=pct_focal_inj,\n            n_focal_favoring=n_focal_favoring,\n            n_ref_favoring=n_ref_favoring,\n            n_newly_c=n_newly_c,\n            n_newly_c_inj=n_newly_c_inj,\n            mean_ddelta_inj=mean_ddelta_inj,\n            elapsed_sec=elapsed,\n        )\n        row.update(quintile_data)\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: C%={c_pct_all:.1f}%, \"\n              f\"ρ_all={rho_all:.3f}, ρ_Δδ_inj={rho_ddelta_inj:.3f}, \"\n              f\"focal_inj%={pct_focal_inj:.1f}%, flips={n_flipped}, {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\ndf.to_csv(os.path.join(OUT, \"semisynthetic_results.csv\"), index=False)\nprint(f\"\\nSaved: semisynthetic_results.csv ({len(df)} rows)\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nreport_lines = [\"# R19 Exp 4 — Difficulty-Dependent Semi-Synthetic Injection\\n\"]\nreport_lines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nreport_lines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models (2023), \"\n                    f\"{N_foc} foc models (2024), {J} items\\n\")\nreport_lines.append(f\"**Injection**: {N_inject_models} foc models ({FOC_INJECT_FRAC*100:.0f}%), \"\n                    f\"~{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nreport_lines.append(f\"\\n## Baseline (no injection)\\n\")\nreport_lines.append(f\"- C%: {n_c_base/J*100:.2f}%\")\nreport_lines.append(f\"- ρ(difficulty, δ_MH) among C: {rho_base:.3f}\")\nreport_lines.append(f\"- % focal-favoring (δ>0): {n_focal_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- % ref-favoring (δ<0): {n_ref_base/n_c_base*100:.1f}%\")\nreport_lines.append(f\"- N DIF-C: {n_c_base}\")\n\nfor scheme in ['A_capability', 'B_contamination', 'C_mixed']:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"\\n## Scheme {scheme.split('_')[0]} — {scheme.split('_',1)[1].replace('_',' ').title()}\\n\")\n\n    report_lines.append(f\"| Metric | Mean ± SD |\")\n    report_lines.append(f\"|--------|-----------|\")\n    report_lines.append(f\"| C% (all items) | {sub['c_pct_all'].mean():.2f} ± {sub['c_pct_all'].std():.2f} |\")\n    report_lines.append(f\"| C% (injected items) | {sub['c_pct_inj'].mean():.2f} ± {sub['c_pct_inj'].std():.2f} |\")\n    report_lines.append(f\"| C% (non-injected) | {sub['c_pct_noninj'].mean():.2f} ± {sub['c_pct_noninj'].std():.2f} |\")\n    report_lines.append(f\"| ρ(diff, δ) all C | {sub['rho_all'].mean():.3f} ± {sub['rho_all'].std():.3f} |\")\n    report_lines.append(f\"| ρ(diff, δ) injected C | {sub['rho_inj'].mean():.3f} ± {sub['rho_inj'].std():.3f} |\")\n    report_lines.append(f\"| **ρ(diff, Δδ) injected items** | **{sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f}** |\")\n    report_lines.append(f\"| ρ(diff, Δδ) all items | {sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} |\")\n    report_lines.append(f\"| % focal-favoring (all C, δ>0) | {sub['pct_focal'].mean():.1f} ± {sub['pct_focal'].std():.1f} |\")\n    report_lines.append(f\"| % focal-favoring (inj C, δ>0) | {sub['pct_focal_inj'].mean():.1f} ± {sub['pct_focal_inj'].std():.1f} |\")\n    report_lines.append(f\"| N DIF-C items | {sub['n_c_total'].mean():.0f} ± {sub['n_c_total'].std():.0f} |\")\n    report_lines.append(f\"| N DIF-C (injected) | {sub['n_c_inj'].mean():.0f} ± {sub['n_c_inj'].std():.0f} |\")\n    report_lines.append(f\"| Newly flagged C | {sub['n_newly_c'].mean():.0f} ± {sub['n_newly_c'].std():.0f} |\")\n    report_lines.append(f\"| Mean Δδ (injected items) | {sub['mean_ddelta_inj'].mean():.3f} ± {sub['mean_ddelta_inj'].std():.3f} |\")\n    report_lines.append(f\"| Responses flipped | {sub['n_flipped'].mean():.0f} ± {sub['n_flipped'].std():.0f} |\")\n    report_lines.append(f\"| Items injected | {sub['n_inject_items'].mean():.0f} |\")\n\n    report_lines.append(f\"\\n### Quintile Breakdown\\n\")\n    report_lines.append(f\"| Quintile | C% (all) | C% (inj) | % Focal | Mean Δδ (inj) | N_C | N_inj |\")\n    report_lines.append(f\"|----------|----------|----------|---------|---------------|-----|-------|\")\n    for q in range(1, 6):\n        cols = {k: f'q{q}_{k}' for k in ['c_pct', 'c_pct_inj', 'pct_focal', 'mean_ddelta', 'n_c', 'n_inj']}\n        if cols['c_pct'] in sub.columns:\n            report_lines.append(\n                f\"| Q{q} | {sub[cols['c_pct']].mean():.1f} | \"\n                f\"{sub[cols['c_pct_inj']].mean():.1f} | \"\n                f\"{sub[cols['pct_focal']].mean():.1f} | \"\n                f\"{sub[cols['mean_ddelta']].mean():.3f} | \"\n                f\"{sub[cols['n_c']].mean():.0f} | \"\n                f\"{sub[cols['n_inj']].mean():.0f} |\")\n\nreport_lines.append(f\"\\n## Key Comparison: ρ(difficulty, Δδ) — injection signal isolated\\n\")\nreport_lines.append(\"Δδ = δ_after − δ_baseline isolates the injection-induced DIF shift.\\n\")\nreport_lines.append(f\"| Scheme | ρ(diff, Δδ) injected | ρ(diff, Δδ) all | Expected |\")\nreport_lines.append(f\"|--------|---------------------|-----------------|----------|\")\nfor scheme, expected in [('A_capability', 'positive (easy→more focal DIF)'),\n                         ('B_contamination', '≈ 0 (uniform)'),\n                         ('C_mixed', 'intermediate')]:\n    sub = df[df['scheme'] == scheme]\n    report_lines.append(f\"| {scheme} | {sub['rho_ddelta_inj'].mean():.3f} ± {sub['rho_ddelta_inj'].std():.3f} | \"\n                       f\"{sub['rho_ddelta_all'].mean():.3f} ± {sub['rho_ddelta_all'].std():.3f} | {expected} |\")\n\nreport_lines.append(f\"\\n## Interpretation\\n\")\nreport_lines.append(\"**Sign convention**: δ > 0 = focal-favoring, δ < 0 = ref-favoring. \"\n                    \"Δδ = δ_after − δ_before; positive Δδ = injection shifted item toward focal-favoring.\\n\")\nreport_lines.append(\"### Key finding: three schemes produce cleanly separable ρ(diff, Δδ) signatures\\n\")\nreport_lines.append(\"1. **Scheme A** (capability-like): ρ(diff, Δδ) ≈ **+0.77**. \"\n                    \"Injection probability ∝ item accuracy → easy items receive more flips → \"\n                    \"larger focal-favoring Δδ on easy items. Strong positive correlation.\")\nreport_lines.append(\"2. **Scheme B** (contamination-like): ρ(diff, Δδ) ≈ **−0.52** (NOT ≈ 0 as naively expected). \"\n                    \"Uniform p=0.5 injection gives equal probability per response, but hard items \"\n                    \"have more 0→1 flippable responses (ceiling effect). \"\n                    \"Result: hard items accumulate more flips → larger Δδ on hard items → negative ρ.\")\nreport_lines.append(\"3. **Scheme C** (mixed): ρ(diff, Δδ) ≈ **+0.39**, intermediate between A and B, \"\n                    \"as expected from mixing both injection mechanisms.\\n\")\nreport_lines.append(\"### Ceiling effect insight\\n\")\nreport_lines.append(\"The Scheme B result (ρ ≈ −0.5 instead of 0) reveals that **uniform memorization probability \"\n                    \"does NOT produce uniform DIF**. Easy items have high baseline accuracy → few 0s to flip → \"\n                    \"small Δδ even at p=0.5. Hard items have low accuracy → many 0s → large Δδ. \"\n                    \"This ceiling effect is an inherent property of binary response matrices and means \"\n                    \"the capability vs. contamination distinction is NOT simply 'correlated vs. uncorrelated with difficulty,' \"\n                    \"but rather the SIGN and MAGNITUDE of the difficulty-DIF gradient.\\n\")\nreport_lines.append(\"### Discriminability\\n\")\nreport_lines.append(\"- A vs B separation: Δρ ≈ 1.29 (0.77 − (−0.52)), massive and non-overlapping across all seeds\")\nreport_lines.append(\"- A vs C separation: Δρ ≈ 0.38, clear but smaller\")\nreport_lines.append(\"- The three patterns are unambiguously distinguishable by ρ(diff, Δδ) alone\")\n\nreport_text = \"\\n\".join(report_lines) + \"\\n\"\n\nwith open(os.path.join(OUT, \"semisynthetic_gradient_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"Saved: semisynthetic_gradient_report.md\")\nprint(\"\\n\" + report_text)\n",
      "numLines": 477,
      "startLine": 1,
      "totalLines": 477
    }
  }
}
```

</details>

---

### Assistant

_source line 39_

Now let me check the model metadata to understand the `training_method` field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "308f5e60-50b7-4115-8f4a-22ec417afa17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LKzHhrQHpZxLXtpeY92DY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10112,
      "cache_read_input_tokens": 28947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10112
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

_source line 40_

<details open><summary>🔧 Tool call — Bash · `toolu_01LCtsoCeoQ4kAK62mXaSzNb`</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv && echo \"---\" && cut -d',' -f1,3,4,5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/model_metadata.csv | head -10",
  "description": "Check model_metadata.csv columns and training_method field"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "7810d056-32b5-4591-add8-2b60e161c3a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LKzHhrQHpZxLXtpeY92DY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10112,
      "cache_read_input_tokens": 28947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10112
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

_source line 41 · 2026-05-23T01:29:53.981Z_

<details><summary>↩ Tool result · `toolu_01LCtsoCeoQ4kAK62mXaSzNb`</summary>

```text
model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile
0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3
0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3
0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3
0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3
---
model_name,release_year,release_half,training_method
0-hero/Matter-0.1-7B,unknown,unknown,unknown
0-hero/Matter-0.1-7B-DPO-preview,unknown,unknown,DPO
0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown
0-hero/Matter-0.1-7B-boost-DPO,unknown,unknown,DPO
0-hero/Matter-0.1-7B-boost-DPO-preview,unknown,unknown,DPO
0-hero/Matter-0.1-Slim-7B,unknown,unknown,unknown
0-hero/Matter-0.1-Slim-7B-A,unknown,unknown,unknown
0-hero/Matter-0.1-Slim-7B-B,unknown,unknown,unknown
0-hero/Matter-0.1-Slim-7B-C,unknown,unknown,unknown
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "9fcd9f4a-394c-46ce-a6f8-f265a525edc6",
  "tool_use_result": {
    "stdout": "model_name,family,release_year,release_half,training_method,accuracy,cohort_temporal,cohort_accuracy_quintile\n0-hero/Matter-0.1-7B,unknown,unknown,unknown,unknown,0.661225,other,3\n0-hero/Matter-0.1-7B-DPO-preview,,unknown,unknown,DPO,0.661337,other,3\n0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown,unknown,0.653422,other,3\n0-hero/Matter-0.1-7B-boost-DPO,,unknown,unknown,DPO,0.654941,other,3\n---\nmodel_name,release_year,release_half,training_method\n0-hero/Matter-0.1-7B,unknown,unknown,unknown\n0-hero/Matter-0.1-7B-DPO-preview,unknown,unknown,DPO\n0-hero/Matter-0.1-7B-boost,unknown,unknown,unknown\n0-hero/Matter-0.1-7B-boost-DPO,unknown,unknown,DPO\n0-hero/Matter-0.1-7B-boost-DPO-preview,unknown,unknown,DPO\n0-hero/Matter-0.1-Slim-7B,unknown,unknown,unknown\n0-hero/Matter-0.1-Slim-7B-A,unknown,unknown,unknown\n0-hero/Matter-0.1-Slim-7B-B,unknown,unknown,unknown\n0-hero/Matter-0.1-Slim-7B-C,unknown,unknown,unknown",
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

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01NSwS9EaVALp3Vc1AhvYESP`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/model_metadata.csv')\nprint('Columns:', list(meta.columns))\nprint()\nprint('training_method values:', meta['training_method'].value_counts())\nprint()\nprint('Crosstab cohort × training_method:')\nprint(pd.crosstab(meta['cohort_temporal'], meta['training_method']))\n\"",
  "description": "Get training_method distribution and crosstab with cohort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "794bc464-7968-4729-9f84-0f27a2985f97",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018LKzHhrQHpZxLXtpeY92DY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10112,
      "cache_read_input_tokens": 28947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10112
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

_source line 43 · 2026-05-23T01:29:56.532Z_

<details><summary>↩ Tool result · `toolu_01NSwS9EaVALp3Vc1AhvYESP`</summary>

```text
Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']

training_method values: training_method
unknown    4676
DPO         347
SFT         136
ORPO         52
PPO          10
KTO           6
Name: count, dtype: int64

Crosstab cohort × training_method:
training_method  DPO  KTO  ORPO  PPO  SFT  unknown
cohort_temporal                                   
2023              23    0     3    4   65      985
2024              40    2    20    0   26      719
other            284    4    29    6   45     2972
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "7dc8a8f7-dc70-4691-bce6-77f901022391",
  "tool_use_result": {
    "stdout": "Columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']\n\ntraining_method values: training_method\nunknown    4676\nDPO         347\nSFT         136\nORPO         52\nPPO          10\nKTO           6\nName: count, dtype: int64\n\nCrosstab cohort × training_method:\ntraining_method  DPO  KTO  ORPO  PPO  SFT  unknown\ncohort_temporal                                   \n2023              23    0     3    4   65      985\n2024              40    2    20    0   26      719\nother            284    4    29    6   45     2972",
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

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
The `training_method` field has values: unknown, DPO, SFT, ORPO, PPO, KTO. The user's context says:
- Base: 1409 total (861 ref=2023, 548 foc=2024)
- Instruct: 478 total (219 ref=2023, 259 foc=2024)

So "base" = training_method == "unknown" and "instruct" = everything else (DPO, SFT, ORPO, PPO, KTO). Let me verify these counts.


Looking at the 2023 data, I'm getting unknown=985 and the sum of all instruct methods (DPO, KTO, ORPO, PPO, SFT) equals 95, which adds up to 1080 total. But the context shows 861 base and 219 instruct for 2023, which also totals 1080. This doesn't match—base can't equal unknown if the numbers don't align. I need to reconsider how base and instruct are actually defined, maybe they're using a different filtering or the "other" cohort is excluded from this analysis.

For 2024, I'm seeing unknown=719 and instruct methods sum to 88 for a total of 807. The discrepancy suggests that models with "unknown" training methods might still be classified as instruct based on their model names (patterns like "-instruct" or "-chat"), so the split isn't purely determined by the training_method field alone. I should look for existing code or logic that handles this base/instruct classification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "a128b9e7-347f-4cbd-b861-ab727caddc5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Aks9n3DnWUz6oYfu65S6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 39059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1024
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

_source line 45_

The training_method field alone doesn't match the base/instruct counts from R18 (861/219 for 2023, 548/259 for 2024). Let me find how that split was determined.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "c1aa01f3-3aaa-4691-8ef0-ebae5d8e91ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Aks9n3DnWUz6oYfu65S6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 39059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1024
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

_source line 46_

<details open><summary>🔧 Tool call — Bash · `toolu_019inYr1oTQiPC3tuqM1zGmd`</summary>

```json
{
  "command": "python3 -c \"\nimport pandas as pd\nmeta = pd.read_csv('artifacts/model_metadata.csv')\n# Check if there's a model_type or is_instruct column\nprint('All columns:', list(meta.columns))\n# Check if model names have instruct/chat patterns\nref = meta[meta['cohort_temporal']=='2023']\nfoc = meta[meta['cohort_temporal']=='2024']\n# Try name-based classification\nimport re\ndef is_instruct(name):\n    patterns = ['instruct', 'chat', 'rlhf', 'dpo', 'sft', 'aligned', 'assistant']\n    return any(p in name.lower() for p in patterns)\nprint('2023 instruct by name:', ref['model_name'].apply(is_instruct).sum(), '/', len(ref))\nprint('2024 instruct by name:', foc['model_name'].apply(is_instruct).sum(), '/', len(foc))\n# Try training_method != unknown\nprint('2023 training_method!=unknown:', (ref['training_method']!='unknown').sum())\nprint('2024 training_method!=unknown:', (foc['training_method']!='unknown').sum())\n\"",
  "description": "Investigate base/instruct split logic"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "e9358ef3-5715-4cc0-9555-67372d8bd854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Aks9n3DnWUz6oYfu65S6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1024,
      "cache_read_input_tokens": 39059,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1024
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

_source line 47 · 2026-05-23T01:30:16.468Z_

<details><summary>↩ Tool result · `toolu_019inYr1oTQiPC3tuqM1zGmd`</summary>

```text
All columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']
2023 instruct by name: 295 / 1080
2024 instruct by name: 262 / 807
2023 training_method!=unknown: 95
2024 training_method!=unknown: 88
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "d66268e2-47d1-49d2-b433-3da80ec4072c",
  "tool_use_result": {
    "stdout": "All columns: ['model_name', 'family', 'release_year', 'release_half', 'training_method', 'accuracy', 'cohort_temporal', 'cohort_accuracy_quintile']\n2023 instruct by name: 295 / 1080\n2024 instruct by name: 262 / 807\n2023 training_method!=unknown: 95\n2024 training_method!=unknown: 88",
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

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Name-based: 295/1080 for 2023, 262/807 for 2024. The context says 219/1080 for 2023 and 259/807 for 2024. Neither name-based nor training_method-based matches exactly.

Let me look more carefully. Maybe there's a separate file for this classification, or maybe R18 used a more refined heuristic. Let me search for R18 analysis code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "81d72703-14fe-4a52-9fbe-4a16147d497d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GUcuuNkiyaQo6jWULrZYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 40083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

<details open><summary>🔧 Tool call — Agent · `toolu_01ViRLXs9GVxF2te3o5iEf9n`</summary>

```json
{
  "subagent_type": "Explore",
  "description": "Find base/instruct split logic",
  "prompt": "In the project at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`, I need to find how models are classified as \"base\" vs \"instruct\". The expected counts are:\n- Base: 861 ref (2023), 548 foc (2024) \n- Instruct: 219 ref (2023), 259 foc (2024)\n\nSearch for:\n1. Any R18 analysis code or files that implement this split\n2. Any Python files that define is_instruct or is_base logic\n3. Any CSV files that have a base/instruct column or model_type column\n4. Grep for \"is_instruct\", \"is_base\", \"model_type\", \"base_model\", \"instruct\" in Python files\n5. Check artifacts/ directory for any file that might contain this mapping\n\nLook in `artifacts/`, `scripts/`, and any other directories."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "75be6ed7-7382-4a53-911f-89bd1a3137e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018GUcuuNkiyaQo6jWULrZYN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1148,
      "cache_read_input_tokens": 40083,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1148
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

### System

_source line 50_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Find base/instruct split logic",
  "task_type": "local_agent",
  "prompt": "In the project at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`, I need to find how models are classified as \"base\" vs \"instruct\". The expected counts are:\n- Base: 861 ref (2023), 548 foc (2024) \n- Instruct: 219 ref (2023), 259 foc (2024)\n\nSearch for:\n1. Any R18 analysis code or files that implement this split\n2. Any Python files that define is_instruct or is_base logic\n3. Any CSV files that have a base/instruct column or model_type column\n4. Grep for \"is_instruct\", \"is_base\", \"model_type\", \"base_model\", \"instruct\" in Python files\n5. Check artifacts/ directory for any file that might contain this mapping\n\nLook in `artifacts/`, `scripts/`, and any other directories.",
  "uuid": "1fc7a4d2-2d17-4479-91b7-908d959a8ffc",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

## Round 2

83 recorded events

### User

_source line 51 · 2026-05-23T01:30:26.746Z_

In the project at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`, I need to find how models are classified as "base" vs "instruct". The expected counts are:
- Base: 861 ref (2023), 548 foc (2024) 
- Instruct: 219 ref (2023), 259 foc (2024)

Search for:
1. Any R18 analysis code or files that implement this split
2. Any Python files that define is_instruct or is_base logic
3. Any CSV files that have a base/instruct column or model_type column
4. Grep for "is_instruct", "is_base", "model_type", "base_model", "instruct" in Python files
5. Check artifacts/ directory for any file that might contain this mapping

Look in `artifacts/`, `scripts/`, and any other directories.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "6175b269-962a-4b00-bc08-a6f31756c04e"
}
```

</details>

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 15625,
    "tool_uses": 1,
    "duration_ms": 1493
  },
  "last_tool_name": "Bash",
  "uuid": "7981ddf3-13ce-4eff-90a4-0d849dcf597d",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Bash · `toolu_01HwSyn6eW3ucxAWFQzNZpXp`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -type f -name \"*.R\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "6275e4d2-4eb8-4d23-bd34-ea797af701e5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019t9xZKQ2RQgKeeDg1cJXpU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 646,
      "cache_read_input_tokens": 14970,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 646,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 54 · 2026-05-23T01:30:28.312Z_

<details><summary>↩ Tool result · `toolu_01HwSyn6eW3ucxAWFQzNZpXp`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "5d3e6537-4f75-4f17-af49-f5c56f2e89b4"
}
```

</details>

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 16608,
    "tool_uses": 2,
    "duration_ms": 2937
  },
  "last_tool_name": "Bash",
  "uuid": "880f2a69-1b9b-437c-820d-64ee5fbcb151",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Bash · `toolu_015KkTZFnopHSxztvAhi4jVF`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "305be15b-8c01-4634-a858-9482f3d5e957",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BBCmuvcpLmKmwEtdukpp75",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 979,
      "cache_read_input_tokens": 15616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 979,
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

_source line 57 · 2026-05-23T01:30:29.734Z_

<details><summary>↩ Tool result · `toolu_015KkTZFnopHSxztvAhi4jVF`</summary>

```text
total 368
drwxr-xr-x 13 ubuntu ubuntu  4096 May 22 21:36 .
drwxrwxr-x  4 ubuntu ubuntu  4096 May 20 17:11 ..
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 17:11 .claude
drwxr-xr-x  7 ubuntu ubuntu  4096 May 23 00:32 .git
-rw-r--r--  1 ubuntu ubuntu 15068 May 23 01:27 AGENTS.md
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:15 ROADMAP.lock
-rw-------  1 ubuntu ubuntu  3063 May 22 21:36 ROADMAP.md
-rw-r--r--  1 ubuntu ubuntu    90 May 22 20:38 _last_visual_review.json
drwxr-xr-x 90 ubuntu ubuntu  4096 May 23 00:32 artifacts
drwxr-xr-x  2 ubuntu ubuntu 16384 May 21 16:24 checkpoints
-rw-r--r--  1 ubuntu ubuntu     0 May 20 18:50 decisions.lock
-rw-------  1 ubuntu ubuntu 38794 May 22 19:21 decisions.yaml
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 12:46 distill_tmp
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 19:42 docs
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 19:34 dream_registry.lock
-rw-------  1 ubuntu ubuntu 15399 May 21 17:54 dream_registry.yaml
-rw-r--r--  1 ubuntu ubuntu 15404 May 21 17:54 dream_registry.yaml.bak
-rw-r--r--  1 ubuntu ubuntu 15097 May 21 10:02 experiment_plan.yaml
drwxr-xr-x  3 ubuntu ubuntu  4096 May 20 23:41 figures
-rw-r--r--  1 ubuntu ubuntu     0 May 21 01:40 literature_map.lock
-rw-------  1 ubuntu ubuntu 36148 May 21 03:50 literature_map.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 20 17:17 logs
-rw-r--r--  1 ubuntu ubuntu 10145 May 21 16:25 memory.md
-rw-r--r--  1 ubuntu ubuntu     0 May 21 03:15 mistakes.lock
-rw-------  1 ubuntu ubuntu  5412 May 21 13:50 mistakes.yaml
drwxr-xr-x  4 ubuntu ubuntu  4096 May 22 22:54 paper
-rw-r--r--  1 ubuntu ubuntu 20977 May 22 12:53 paper_framing.md
-rw-r--r--  1 ubuntu ubuntu     0 May 21 04:18 paper_provenance.lock
-rw-------  1 ubuntu ubuntu  4755 May 21 09:00 paper_provenance.yaml
-rw-r--r--  1 ubuntu ubuntu     0 May 20 17:16 registry.lock
-rw-------  1 ubuntu ubuntu 50016 May 21 16:24 registry.yaml
-rw-r--r--  1 ubuntu ubuntu  2741 May 21 16:24 report.md
-rw-r--r--  1 ubuntu ubuntu  4238 May 22 16:26 review_visual_check_state.json
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 13:32 scripts
-rwxr-xr-x  1 ubuntu ubuntu     0 May 20 17:12 study_status.lock
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 19:16 task_context
-rw-r--r--  1 ubuntu ubuntu 40296 May 21 08:24 writing_plan.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "de95cf2e-45f9-4c0c-88cb-334c5fc4e11c"
}
```

</details>

---

### System

_source line 58_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Finding **/*.py",
  "usage": {
    "total_tokens": 17799,
    "tool_uses": 3,
    "duration_ms": 5379
  },
  "last_tool_name": "Glob",
  "uuid": "8366f51a-06b3-457a-866c-6cfbe8a4066d",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Glob · `toolu_01HfarXML7BPj6mmTi7yxro6`</summary>

```json
{
  "pattern": "**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "4af6c8eb-ac93-4dbf-87e7-4ff273c004b1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012wp3gRF65XGMTgc84qMr2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 16595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1189,
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

_source line 60 · 2026-05-23T01:30:32.138Z_

<details><summary>↩ Tool result · `toolu_01HfarXML7BPj6mmTi7yxro6`</summary>

```text
scripts/r14_domain_profile.py
scripts/r14_cooks_d_analysis.py
scripts/r16_dif_union.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "e6b634f1-0ee0-4d26-997f-30a2f420d5c2"
}
```

</details>

---

### System

_source line 61_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Finding **/*.R",
  "usage": {
    "total_tokens": 17800,
    "tool_uses": 4,
    "duration_ms": 5619
  },
  "last_tool_name": "Glob",
  "uuid": "9c716eaf-0806-4fd5-b38d-4289b7209d93",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Glob · `toolu_01BDUAWcNYQr5fTWGBTypZVN`</summary>

```json
{
  "pattern": "**/*.R",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "4d951312-b40e-463a-b14b-0f24cd9ed943",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012wp3gRF65XGMTgc84qMr2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 16595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1189,
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

_source line 63 · 2026-05-23T01:30:32.382Z_

<details><summary>↩ Tool result · `toolu_01BDUAWcNYQr5fTWGBTypZVN`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "00fbc01b-54c6-4c05-879a-b194f4d9079f"
}
```

</details>

---

### System

_source line 64_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Finding **/*.csv",
  "usage": {
    "total_tokens": 17801,
    "tool_uses": 5,
    "duration_ms": 6082
  },
  "last_tool_name": "Glob",
  "uuid": "9e836958-59ca-42d2-b46f-2bad25104868",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Glob · `toolu_01Dwi7m9uV5VNUfyv8zBvkHK`</summary>

```json
{
  "pattern": "**/*.csv",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "90c914d4-a7c5-44a5-b372-f28a88bcf887",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_012wp3gRF65XGMTgc84qMr2h",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1189,
      "cache_read_input_tokens": 16595,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1189,
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

_source line 66 · 2026-05-23T01:30:32.853Z_

<details><summary>↩ Tool result · `toolu_01Dwi7m9uV5VNUfyv8zBvkHK`</summary>

```text
artifacts/metabench_data/benchmark-data/gsm8k_prompts.csv
artifacts/metabench_data/benchmark-data/hellaswag_prompts.csv
artifacts/metabench_data/benchmark-data/truthfulqa_prompts.csv
artifacts/metabench_data/benchmark-data/arc_prompts.csv
artifacts/metabench_data/benchmark-data/arc.csv
artifacts/metabench_data/benchmark-data/gsm8k.csv
artifacts/metabench_data/benchmark-data/hellaswag.csv
artifacts/metabench_data/benchmark-data/truthfulqa.csv
artifacts/metabench_data/benchmark-data/winogrande.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_abstract_algebra.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_anatomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_astronomy.csv
artifacts/metabench_data/benchmark-data/mmlu_business_ethics.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_clinical_knowledge.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_biology.csv
artifacts/metabench_data/benchmark-data/mmlu_college_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_college_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_college_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_computer_security.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_electrical_engineering.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_global_facts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_chemistry.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_computer_science.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_european_history.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_geography.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_macroeconomics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_high_school_us_history.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_human_sexuality.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_international_law.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_logical_fallacies.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_machine_learning.csv
artifacts/metabench_data/benchmark-data/mmlu_management_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_management.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_marketing.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_medical_genetics.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_miscellaneous.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_disputes.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_moral_scenarios.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_accounting.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_law.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_medicine.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_professional_psychology.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_public_relations.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_security_studies.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_us_foreign_policy.csv
artifacts/metabench_data/benchmark-data/mmlu_virology_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_virology.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_world_religions.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_econometrics.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_elementary_mathematics.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics_prompts.csv
artifacts/metabench_data/benchmark-data/mmlu_conceptual_physics.csv
artifacts/metabench_data/benchmark-data/mmlu_formal_logic_prompts.csv
(Results are truncated. Consider using a more specific path or pattern.)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "dd82ee2c-4bd4-47da-8c3c-b126d0732f75"
}
```

</details>

---

### System

_source line 67_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Searching for is_instruct|is_base|model_type|instruct_model|bas…",
  "usage": {
    "total_tokens": 20504,
    "tool_uses": 6,
    "duration_ms": 9090
  },
  "last_tool_name": "Grep",
  "uuid": "483cb774-e03c-40e0-aaa2-b1ee8001a93a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Grep · `toolu_01L8qdQjrkATKvhaq6SSXUAh`</summary>

```json
{
  "pattern": "is_instruct|is_base|model_type|instruct_model|base_model",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "83d6d0b0-9f83-4eac-86a9-9c32858e61ac",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CKyR59reV8bdEB9kjYyD47",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 17784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2700,
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

_source line 69 · 2026-05-23T01:30:35.868Z_

<details><summary>↩ Tool result · `toolu_01L8qdQjrkATKvhaq6SSXUAh`</summary>

```text
Found 1 file
artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "a426baee-1009-40b8-9a6d-264e489ecb1f"
}
```

</details>

---

### System

_source line 70_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 20505,
    "tool_uses": 7,
    "duration_ms": 9284
  },
  "last_tool_name": "Bash",
  "uuid": "84fb559e-e5dd-4714-8274-ac3501d66fcd",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ro443Chh7MCXvgrQDbBtr8`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts -name \"*.py\" | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "bca79e11-1463-4aa1-9f73-80bad6b1595c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CKyR59reV8bdEB9kjYyD47",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2700,
      "cache_read_input_tokens": 17784,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2700,
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

_source line 72 · 2026-05-23T01:30:36.098Z_

<details><summary>↩ Tool result · `toolu_01Ro443Chh7MCXvgrQDbBtr8`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/mf2_deff_estimation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step3_gsm1k_dif_correlation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/dif_power_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_024_within_family.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_014_within_subject_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/rank_shift_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/metabench_explore.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_016_within_subject_injection.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_013_q3_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/bootstrap_dfpr.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/dif_phase2_simulation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/lofo_robustness.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_035_q3_inflation_sim.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_004_step2_gsm8k_semi_synthetic.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/metabench_explore_0bd873.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_021_nonuniform_dif.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/intermediate/plan_012_irt_theta_analysis.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/mf1_lofo_power_calibration.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_020_circularity_ablation.py
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/data/plan_004_step1_gsm8k_temporal_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "8da4c179-3733-46ec-a4fe-caee2df4967e"
}
```

</details>

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Reading artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "usage": {
    "total_tokens": 21870,
    "tool_uses": 8,
    "duration_ms": 11547
  },
  "last_tool_name": "Read",
  "uuid": "6efa423b-df7d-4803-9821-afe9a30c6374",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 74_

<details open><summary>🔧 Tool call — Read · `toolu_01M7CEX2ZWoq8HbvP7CJdmrZ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "a190dca2-504c-4050-a71d-0573585ecbeb",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01AAkVXViCtB58kVWJJCErVc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1363,
      "cache_read_input_tokens": 20484,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1363,
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

_source line 75 · 2026-05-23T01:30:38.303Z_

<details><summary>↩ Tool result · `toolu_01M7CEX2ZWoq8HbvP7CJdmrZ`</summary>

```text
1	#!/usr/bin/env python3
2	"""R18: Base vs Instruct MH-DIF separation experiment."""
3	
4	import re
5	import sys
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse
9	from scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency
10	
11	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
12	OUT = f"{ROOT}/r18_base_vs_instruct_dif"
13	
14	N_STRATA = 5
15	N_BOOT = 1000
16	ALPHA = 0.05
17	DELTA_THRESH = 1.5
18	
19	# ── Part 1: Model classification ─────────────────────────────────────────
20	
21	INSTRUCT_SUFFIXES = re.compile(
22	    r"[-_\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)"
23	    r"([-_\.]|$)",
24	    re.IGNORECASE,
25	)
26	
27	QUANT_SUFFIXES = re.compile(
28	    r"[-_\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])",
29	    re.IGNORECASE,
30	)
31	
32	FAMILY_PREFIX_EXCLUDE = re.compile(
33	    r"^(openchat|chatglm|chatml)",
34	    re.IGNORECASE,
35	)
36	
37	
38	def classify_model(name: str) -> str:
39	    short = name.split("/")[-1] if "/" in name else name
40	    stripped = QUANT_SUFFIXES.sub("", short)
41	
42	    if stripped.lower().endswith("-it"):
43	        return "instruct"
44	
45	    if INSTRUCT_SUFFIXES.search(stripped):
46	        prefix_part = stripped.split("-")[0].split("_")[0]
47	        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):
48	            rest = stripped[len(prefix_part):]
49	            if not INSTRUCT_SUFFIXES.search(rest):
50	                return "base"
51	        return "instruct"
52	
53	    return "base"
54	
55	
56	# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────
57	
58	def mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):
59	    """Vectorized MH-DIF returning per-item details.
60	
61	    Returns (c_pct, delta_mh, pval, is_c).
62	    """
63	    n_ref, J = X_ref.shape
64	    n_foc = X_foc.shape[0]
65	
66	    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()
67	    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()
68	    s_all = np.concatenate([tot_ref, tot_foc])
69	
70	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
71	    n_bins = len(edges) - 1
72	    if n_bins < 1:
73	        return 0.0, np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)
74	
75	    k_ref = np.digitize(tot_ref, edges[1:-1])
76	    k_foc = np.digitize(tot_foc, edges[1:-1])
77	
78	    n1 = np.zeros(n_bins, dtype=np.float64)
79	    n0 = np.zeros(n_bins, dtype=np.float64)
80	    A = np.zeros((n_bins, J), dtype=np.float64)
81	    C = np.zeros((n_bins, J), dtype=np.float64)
82	
83	    for k in range(n_bins):
84	        mr = k_ref == k
85	        mf = k_foc == k
86	        n1[k] = mr.sum()
87	        n0[k] = mf.sum()
88	        if mr.any():
89	            A[k] = np.asarray(X_ref[mr].sum(axis=0), dtype=np.float64).ravel()
90	        if mf.any():
91	            C[k] = np.asarray(X_foc[mf].sum(axis=0), dtype=np.float64).ravel()
92	
93	    B = n1[:, None] - A
94	    D = n0[:, None] - C
95	    Nk = (n1 + n0)[:, None]
96	    m1 = A + C
97	    m0 = B + D
98	
99	    valid = (n1[:, None] > 0) & (n0[:, None] > 0) & (Nk > 1) & (m1 > 0) & (m0 > 0)
100	
101	    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)
102	    Sj = np.where(valid, B * C / Nk, 0).sum(axis=0)
103	
104	    finite_mask = (Rj > 0) & (Sj > 0)
105	    with np.errstate(divide="ignore", invalid="ignore"):
106	        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)
107	
108	    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)
109	    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)
110	    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)
111	    sum_var = np.where(
112	        valid,
113	        n1[:, None] * n0[:, None] * m1 * m0 / (Nk**2 * Nk_m1),
114	        0,
115	    ).sum(axis=0)
116	
117	    chi2_j = np.where(
118	        sum_var > 0,
119	        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30),
120	        0,
121	    )
122	    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)
123	
124	    is_c = finite_mask & (np.abs(delta_j) >= DELTA_THRESH) & (pval_j < ALPHA)
125	    c_pct = is_c.sum() / J * 100
126	
127	    return c_pct, delta_j, pval_j, is_c
128	
129	
130	def ets_class(delta):
131	    a = abs(delta)
132	    if a < 1.0:
133	        return "A"
134	    elif a < 1.5:
135	        return "B"
136	    else:
137	        return "C"
138	
139	
140	# ── Main ──────────────────────────────────────────────────────────────────
141	
142	def main():
143	    print("Loading data...")
144	    meta = pd.read_csv(f"{ROOT}/plan_032_dif_cleaned_mmlu/cleaned_mmlu_analysis.csv")
145	    rm = np.load(f"{ROOT}/response_matrix.npz")
146	    X = sparse.csr_matrix((rm["data"], rm["indices"], rm["indptr"]), shape=tuple(rm["shape"]))
147	    idx = np.load(f"{ROOT}/response_matrix_index.npz", allow_pickle=True)
148	    model_names = idx["model_names"]
149	    item_ids = idx["item_ids"]
150	
151	    # Build model name → row index lookup
152	    name2row = {n: i for i, n in enumerate(model_names)}
153	
154	    # Classify models
155	    meta = meta[meta["cohort_temporal"].isin(["2023", "2024"])].copy()
156	    meta["model_type"] = meta["model_name"].apply(classify_model)
157	
158	    # Save classification
159	    class_df = meta[["model_name", "model_type", "cohort_temporal", "family"]].copy()
160	    class_df.to_csv(f"{OUT}/model_classification.csv", index=False)
161	
162	    # Map to response matrix rows
163	    meta["rm_idx"] = meta["model_name"].map(name2row)
164	    meta = meta.dropna(subset=["rm_idx"])
165	    meta["rm_idx"] = meta["rm_idx"].astype(int)
166	
167	    # Group counts
168	    groups = {}
169	    for mtype in ["base", "instruct"]:
170	        ref_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2023")
171	        foc_mask = (meta["model_type"] == mtype) & (meta["cohort_temporal"] == "2024")
172	        groups[mtype] = {
173	            "ref_idx": meta.loc[ref_mask, "rm_idx"].values,
174	            "foc_idx": meta.loc[foc_mask, "rm_idx"].values,
175	        }
176	
177	    print("\n=== Part 4: Sample sizes ===")
178	    for mtype in ["base", "instruct"]:
179	        n_ref = len(groups[mtype]["ref_idx"])
180	        n_foc = len(groups[mtype]["foc_idx"])
181	        flag = " ⚠ UNDERPOWERED" if min(n_ref, n_foc) < 80 else ""
182	        print(f"  {mtype:>10s}: ref(2023)={n_ref}, foc(2024)={n_foc}{flag}")
183	    print(f"  {'full':>10s}: ref(2023)=1080, foc(2024)=807  (reported baseline)")
184	
185	    # Run MH-DIF per group
186	    results = {}
187	    for mtype in ["base", "instruct"]:
188	        ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
189	        print(f"\nRunning MH-DIF for {mtype} ({len(ri)} ref, {len(fi)} foc)...")
190	        X_ref = X[ri]
191	        X_foc = X[fi]
192	        c_pct, delta, pval, is_c = mh_dif_full(X_ref, X_foc)
193	        results[mtype] = {"c_pct": c_pct, "delta": delta, "pval": pval, "is_c": is_c}
194	        print(f"  C% = {c_pct:.1f}%  ({is_c.sum()}/{len(is_c)} items)")
195	
196	    # ── Part 3a: Bootstrap CI for C% difference ──────────────────────────
197	    print("\n=== Part 3a: Bootstrap C% difference ===")
198	    rng = np.random.default_rng(42)
199	    boot_diff = np.zeros(N_BOOT)
200	
201	    for b in range(N_BOOT):
202	        if (b + 1) % 200 == 0:
203	            print(f"  bootstrap {b+1}/{N_BOOT}...")
204	        cpcts = {}
205	        for mtype in ["base", "instruct"]:
206	            ri, fi = groups[mtype]["ref_idx"], groups[mtype]["foc_idx"]
207	            ri_b = rng.choice(ri, size=len(ri), replace=True)
208	            fi_b = rng.choice(fi, size=len(fi), replace=True)
209	            c, _, _, _ = mh_dif_full(X[ri_b], X[fi_b])
210	            cpcts[mtype] = c
211	        boot_diff[b] = cpcts["base"] - cpcts["instruct"]
212	
213	    ci_lo, ci_hi = np.percentile(boot_diff, [2.5, 97.5])
214	    mean_diff = boot_diff.mean()
215	    print(f"  C%_base - C%_instruct = {results['base']['c_pct']:.1f} - {results['instruct']['c_pct']:.1f} = {results['base']['c_pct'] - results['instruct']['c_pct']:.1f}")
216	    print(f"  Bootstrap 95% CI: [{ci_lo:.1f}, {ci_hi:.1f}]")
217	
218	    # ── Part 3b: Difficulty-direction gradient ────────────────────────────
219	    print("\n=== Part 3b: Difficulty-direction gradient ===")
220	    all_2023_idx = meta.loc[meta["cohort_temporal"] == "2023", "rm_idx"].values
221	    X_2023 = X[all_2023_idx]
222	    item_diff = np.asarray(X_2023.mean(axis=0), dtype=np.float64).ravel()
223	
224	    for mtype in ["base", "instruct"]:
225	        c_mask = results[mtype]["is_c"]
226	        if c_mask.sum() < 3:
227	            print(f"  {mtype}: too few C items ({c_mask.sum()}) for correlation")
228	            continue
229	        rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
230	        print(f"  {mtype}: ρ(difficulty, Δ_MH) = {rho:.3f}  (p={p:.2e}, n={c_mask.sum()})")
231	
232	    # ── Part 3c: DIF item overlap ─────────────────────────────────────────
233	    print("\n=== Part 3c: DIF item overlap ===")
234	    c_base = set(np.where(results["base"]["is_c"])[0])
235	    c_inst = set(np.where(results["instruct"]["is_c"])[0])
236	    inter = c_base & c_inst
237	    union = c_base | c_inst
238	    jaccard = len(inter) / len(union) if union else 0
239	
240	    p_b = len(c_base) / len(item_ids)
241	    p_i = len(c_inst) / len(item_ids)
242	    expected_jaccard = (p_b * p_i) / (p_b + p_i - p_b * p_i) if (p_b + p_i - p_b * p_i) > 0 else 0
243	
244	    only_base = len(c_base - c_inst)
245	    only_inst = len(c_inst - c_base)
246	    both = len(inter)
247	    print(f"  |C_base|={len(c_base)}, |C_instruct|={len(c_inst)}")
248	    print(f"  Only base: {only_base}, Only instruct: {only_inst}, Both: {both}")
249	    print(f"  Jaccard = {jaccard:.3f}  (expected under independence: {expected_jaccard:.3f})")
250	
251	    # ── Part 3d: Direction distribution ───────────────────────────────────
252	    print("\n=== Part 3d: DIF direction distribution ===")
253	    dir_table = {}
254	    for mtype in ["base", "instruct"]:
255	        d = results[mtype]["delta"][results[mtype]["is_c"]]
256	        n_foc_fav = (d > 0).sum()
257	        n_ref_fav = (d < 0).sum()
258	        dir_table[mtype] = (int(n_foc_fav), int(n_ref_fav))
259	        total = n_foc_fav + n_ref_fav
260	        print(f"  {mtype}: focal-favoring={n_foc_fav} ({n_foc_fav/total*100:.1f}%), ref-favoring={n_ref_fav} ({n_ref_fav/total*100:.1f}%)")
261	
262	    ct = np.array([[dir_table["base"][0], dir_table["base"][1]],
263	                    [dir_table["instruct"][0], dir_table["instruct"][1]]])
264	    if ct.min() > 0:
265	        chi2_val, p_dir, _, _ = chi2_contingency(ct)
266	        print(f"  χ²={chi2_val:.2f}, p={p_dir:.3e}")
267	    else:
268	        p_dir = np.nan
269	        print("  χ² test not possible (zero cell)")
270	
271	    # ── Save per-item CSV ─────────────────────────────────────────────────
272	    print("\nSaving per-item results...")
273	
274	    # Extract subject from item_id (format: subject_qXXXX or similar)
275	    def get_subject(iid):
276	        parts = iid.rsplit("_", 1)
277	        return parts[0] if len(parts) > 1 else iid
278	
279	    item_df = pd.DataFrame({
280	        "item_id": item_ids,
281	        "subject": [get_subject(str(i)) for i in item_ids],
282	        "difficulty": item_diff,
283	        "delta_mh_base": results["base"]["delta"],
284	        "p_base": results["base"]["pval"],
285	        "ets_base": [ets_class(d) for d in results["base"]["delta"]],
286	        "is_c_base": results["base"]["is_c"],
287	        "delta_mh_instruct": results["instruct"]["delta"],
288	        "p_instruct": results["instruct"]["pval"],
289	        "ets_instruct": [ets_class(d) for d in results["instruct"]["delta"]],
290	        "is_c_instruct": results["instruct"]["is_c"],
291	    })
292	    item_df.to_csv(f"{OUT}/base_instruct_item_results.csv", index=False)
293	
294	    # ── Generate report ───────────────────────────────────────────────────
295	    print("Writing report...")
296	
297	    n_base_ref = len(groups["base"]["ref_idx"])
298	    n_base_foc = len(groups["base"]["foc_idx"])
299	    n_inst_ref = len(groups["instruct"]["ref_idx"])
300	    n_inst_foc = len(groups["instruct"]["foc_idx"])
301	
302	    report = f"""# R18: Base vs Instruct DIF Separation Experiment
303	
304	## Sample Sizes
305	
306	| Group | Ref (2023) | Foc (2024) | Total |
307	|-------|-----------|-----------|-------|
308	| Base | {n_base_ref} | {n_base_foc} | {n_base_ref + n_base_foc} |
309	| Instruct | {n_inst_ref} | {n_inst_foc} | {n_inst_ref + n_inst_foc} |
310	| Full (reported) | 1,080 | 807 | 1,887 |
311	
312	{"**⚠ Warning:** Some subgroups have N < 80; interpret with caution." if min(n_base_ref, n_base_foc, n_inst_ref, n_inst_foc) < 80 else "All subgroups have N ≥ 80; adequate power."}
313	
314	## C% Comparison
315	
316	| Group | C% | DIF-C items |
317	|-------|-----|------------|
318	| Base | {results['base']['c_pct']:.1f}% | {results['base']['is_c'].sum()}/{len(item_ids)} |
319	| Instruct | {results['instruct']['c_pct']:.1f}% | {results['instruct']['is_c'].sum()}/{len(item_ids)} |
320	| Full (reported) | 31.3% | — |
321	
322	**Difference (base − instruct):** {results['base']['c_pct'] - results['instruct']['c_pct']:.1f} pp
323	**Bootstrap 95% CI:** [{ci_lo:.1f}, {ci_hi:.1f}] (N={N_BOOT})
324	
325	## Difficulty–Direction Gradient
326	
327	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
328	
329	"""
330	
331	    for mtype in ["base", "instruct"]:
332	        c_mask = results[mtype]["is_c"]
333	        if c_mask.sum() >= 3:
334	            rho, p = spearmanr(item_diff[c_mask], results[mtype]["delta"][c_mask])
335	            report += f"- **{mtype.capitalize()}:** ρ = {rho:.3f} (p = {p:.2e}, n = {c_mask.sum()})\n"
336	        else:
337	            report += f"- **{mtype.capitalize()}:** too few C items ({c_mask.sum()}) for correlation\n"
338	
339	    report += f"""
340	## DIF Item Overlap
341	
342	| Metric | Value |
343	|--------|-------|
344	| C_base only | {only_base} |
345	| C_instruct only | {only_inst} |
346	| Both | {both} |
347	| Jaccard index | {jaccard:.3f} |
348	| Expected Jaccard (independence) | {expected_jaccard:.3f} |
349	| Jaccard / Expected ratio | {jaccard / expected_jaccard:.1f}× |
350	
351	## DIF Direction Distribution
352	
353	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
354	|-------|----------------------|---------------------|
355	| Base | {dir_table['base'][0]} ({dir_table['base'][0]/(sum(dir_table['base']))*100:.1f}%) | {dir_table['base'][1]} ({dir_table['base'][1]/(sum(dir_table['base']))*100:.1f}%) |
356	| Instruct | {dir_table['instruct'][0]} ({dir_table['instruct'][0]/(sum(dir_table['instruct']))*100:.1f}%) | {dir_table['instruct'][1]} ({dir_table['instruct'][1]/(sum(dir_table['instruct']))*100:.1f}%) |
357	
358	χ² = {chi2_val:.2f}, p = {p_dir:.3e}
359	
360	## Output Files
361	
362	- `model_classification.csv` — {len(class_df)} models classified
363	- `base_instruct_item_results.csv` — {len(item_ids)} items with per-group DIF statistics
364	"""
365	
366	    with open(f"{OUT}/base_instruct_dif_report.md", "w") as f:
367	        f.write(report)
368	
369	    print(f"\nDone. Results in {OUT}/")
370	
371	
372	if __name__ == "__main__":
373	    main()
374	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "cb5d990b-e9f8-4c99-9b4e-870aafeac179"
}
```

</details>

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 28463,
    "tool_uses": 9,
    "duration_ms": 24326
  },
  "last_tool_name": "Bash",
  "uuid": "339ae077-82f7-42f1-906e-9f25a444e91f",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — Bash · `toolu_01YEFupvDye1yJCP9GKCtt4X`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "79696088-07fe-4e61-bdd6-588a4b80dc5c",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015JHudJVj6FxDhmK95Cxr53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 21847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6592,
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

_source line 78 · 2026-05-23T01:30:51.125Z_

<details><summary>↩ Tool result · `toolu_01YEFupvDye1yJCP9GKCtt4X`</summary>

```text
total 1912
drwxr-xr-x  2 ubuntu ubuntu    4096 May 22 17:51 .
drwxr-xr-x 90 ubuntu ubuntu    4096 May 23 00:32 ..
-rw-r--r--  1 ubuntu ubuntu   14768 May 22 17:47 base_instruct_dif.py
-rw-r--r--  1 ubuntu ubuntu    1445 May 22 17:51 base_instruct_dif_report.md
-rw-r--r--  1 ubuntu ubuntu 1824610 May 22 17:51 base_instruct_item_results.csv
-rw-r--r--  1 ubuntu ubuntu  102000 May 22 17:47 model_classification.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "7bf735c9-11bc-43d1-9599-a5774ce91812"
}
```

</details>

---

### System

_source line 79_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running head -50 /home/ubuntu/.agent-ml-research-idea_gen…",
  "usage": {
    "total_tokens": 28464,
    "tool_uses": 10,
    "duration_ms": 24493
  },
  "last_tool_name": "Bash",
  "uuid": "81fb2f6b-9ed5-4b2c-aabb-6552cce558fa",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 80_

<details open><summary>🔧 Tool call — Bash · `toolu_01VuYPQxKgeUFPNq85rSywgg`</summary>

```json
{
  "command": "head -50 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv 2>/dev/null || echo \"File not found\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "dcee39a3-8563-4e24-b1ce-ec645e135f36",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015JHudJVj6FxDhmK95Cxr53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6592,
      "cache_read_input_tokens": 21847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6592,
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

_source line 81 · 2026-05-23T01:30:51.304Z_

<details><summary>↩ Tool result · `toolu_01VuYPQxKgeUFPNq85rSywgg`</summary>

```text
model_name,model_type,cohort_temporal,family
01-ai/Yi-1.5-34B,base,2024,yi-1.5
01-ai/Yi-1.5-34B-32K,base,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat,instruct,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat-16K,instruct,2024,yi-1.5
01-ai/Yi-1.5-6B,base,2024,yi-1.5
01-ai/Yi-1.5-6B-Chat,instruct,2024,yi-1.5
01-ai/Yi-1.5-9B,base,2024,yi-1.5
01-ai/Yi-1.5-9B-32K,base,2024,yi-1.5
01-ai/Yi-1.5-9B-Chat,instruct,2024,yi-1.5
01-ai/Yi-1.5-9B-Chat-16K,instruct,2024,yi-1.5
01-ai/Yi-34B-200K,base,2023,yi
01-ai/Yi-34B-Chat,instruct,2023,yi
01-ai/Yi-9B,base,2023,yi
01-ai/Yi-9B-200K,base,2023,yi
222gate/TinyMistral-248Mx4-MOE,base,2023,mistral
922-CA/Llama-3-monika-ddlc-8b-v1,base,2024,llama-3
922-CA/Llama-3-natsuki-ddlc-8b-v1,base,2024,llama-3
922CA/Llama-3-monika-ddlc-11.5b-v1,base,2024,llama-3
AIGeekLabs/radiantloom-mixtral-8x7b-fusion,base,2024,mixtral
AIGym/Llama-2-7b-chat-hf-structured-responses,instruct,2023,llama-2
AIGym/deepseek-coder-1.3b-chat,instruct,2024,deepseek
AIGym/deepseek-coder-1.3b-chat-and-function-calling,instruct,2024,deepseek
AIGym/deepseek-coder-6.7b-chat,instruct,2024,deepseek
AIGym/deepseek-coder-6.7b-chat-and-function-calling,instruct,2024,deepseek
AIJUUD/juud-Mistral-7B,base,2023,mistral
Aabbhishekk/llama2-7b-function-calling-slerp,base,2023,llama-2
Abhaykoul/Qwen1.5-0.5B-vortex,base,2024,qwen-1.5
Abhaykoul/Qwen1.5-0.5B-vortex-v2,base,2024,qwen-1.5
Abhaykoul/qwen1.5-vortex,base,2024,qwen-1.5
Amu/dpo-Qwen1.5-0.5B-Chat-alignment-handbook,instruct,2024,qwen-1.5
Aratako/Mixtral-8x7B-Instruct-v0.1-upscaled,instruct,2024,mixtral
Aratako/Qwen1.5-MoE-2x7B,base,2024,qwen-1.5
Aratako/c4ai-command-r-v01-japanese-instruct,instruct,2024,command-r
ArianAskari/NeuralHermes-2.5-Mistral-7B,base,2023,mistral
ArianAskari/SOLID-SFT-DPO-MixQV2-SOLIDChosen-SFTRejected-Zephyr-7b-beta,instruct,2023,zephyr
ArianAskari/SOLID-SFT-DPO-MixQV2-SOLIDRejected-SFTChosen-Zephyr-7b-beta,instruct,2023,zephyr
ArianAskari/SOLID-SFT-DPO-MixQV3-SOLIDChosen-SFTRejected-Zephyr-7b-beta,instruct,2023,zephyr
ArianAskari/SOLID-SFT-DPO-MixQV3-SOLIDRejected-SFTChosen-Zephyr-7b-beta,instruct,2023,zephyr
ArianAskari/SOLID-SFT-WoDPO-MixQV2-Zephyr-7b-beta,instruct,2023,zephyr
AwanLLM/Awanllm-Llama-3-8B-Cumulus-v0.2,base,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Dolfin-v0.3,base,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Dolfin-v0.3-DPO,instruct,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Dolfin-v0.6-Abliterated,base,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Instruct-DPO-v0.1,instruct,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Instruct-DPO-v0.2,instruct,2024,llama-3
AwanLLM/Awanllm-Llama-3-8B-Instruct-ORPO-v0.1,instruct,2024,llama-3
AwanLLM/Llama-3-8B-Cumulus-v0.1,base,2024,llama-3
AwanLLM/Llama-3-8B-Dolfin-v0.2-Instruct,instruct,2024,llama-3
AwanLLM/Meta-Llama-3-8B-Instruct-Dolfin-v0.1,instruct,2024,llama-3
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "aa69f7cf-82d6-41e6-9dd4-1df2313bff79"
}
```

</details>

---

### System

_source line 82_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running cd /home/ubuntu/.agent-ml-research-idea_gen_0520_…",
  "usage": {
    "total_tokens": 30651,
    "tool_uses": 11,
    "duration_ms": 29182
  },
  "last_tool_name": "Bash",
  "uuid": "f658253c-343a-4089-837b-ab7fe2e16e2a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 83_

<details open><summary>🔧 Tool call — Bash · `toolu_01JVkCd2S3sLmtZTsZbvVNF2`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif && python3 << 'EOF'\nimport pandas as pd\n\ndf = pd.read_csv('model_classification.csv')\n\n# Count by type and cohort\nprint(\"=== Model Classification Counts ===\\n\")\nfor cohort in ['2023', '2024']:\n    print(f\"Cohort {cohort}:\")\n    subset = df[df['cohort_temporal'] == cohort]\n    base_count = len(subset[subset['model_type'] == 'base'])\n    instruct_count = len(subset[subset['model_type'] == 'instruct'])\n    print(f\"  Base: {base_count}\")\n    print(f\"  Instruct: {instruct_count}\")\n    print(f\"  Total: {len(subset)}\\n\")\n\n# Full summary\nprint(\"Summary by type:\")\nfor mtype in ['base', 'instruct']:\n    counts = df[df['model_type'] == mtype]['cohort_temporal'].value_counts().sort_index()\n    print(f\"{mtype.capitalize()}:\")\n    for cohort in ['2023', '2024']:\n        if cohort in counts.index:\n            print(f\"  {cohort}: {counts[cohort]}\")\n        else:\n            print(f\"  {cohort}: 0\")\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "e4a33646-e6b1-4c14-88ff-b5533734eac6",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DAhhEc9pjDjtzZxUEQuJsW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 28439,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2178,
        "ephemeral_1h_input_tokens": 0
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

_source line 84 · 2026-05-23T01:30:56.587Z_

<details><summary>↩ Tool result · `toolu_01JVkCd2S3sLmtZTsZbvVNF2`</summary>

```text
=== Model Classification Counts ===

Cohort 2023:
  Base: 0
  Instruct: 0
  Total: 0

Cohort 2024:
  Base: 0
  Instruct: 0
  Total: 0

Summary by type:
Base:
  2023: 0
  2024: 0
Instruct:
  2023: 0
  2024: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "6bd82033-018f-4be0-afad-edd104fe813c"
}
```

</details>

---

### System

_source line 85_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running wc -l /home/ubuntu/.agent-ml-research-idea_gen_05…",
  "usage": {
    "total_tokens": 31204,
    "tool_uses": 12,
    "duration_ms": 31741
  },
  "last_tool_name": "Bash",
  "uuid": "89385962-beda-4ed6-a18c-95ef6bded424",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — Bash · `toolu_014avrpYnaBChm1JPVsq53hr`</summary>

```json
{
  "command": "wc -l /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "296e3432-a0a9-4bfa-bf94-dcb14f48f2df",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LMPRdaKAgzX8CnR8TS2bBE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 552,
      "cache_read_input_tokens": 30617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 552,
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

_source line 87 · 2026-05-23T01:30:58.548Z_

<details><summary>↩ Tool result · `toolu_014avrpYnaBChm1JPVsq53hr`</summary>

```text
1888 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "26142e01-5557-4689-927b-5de60c1cc6b4"
}
```

</details>

---

### System

_source line 88_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running cd /home/ubuntu/.agent-ml-research-idea_gen_0520_…",
  "usage": {
    "total_tokens": 31466,
    "tool_uses": 13,
    "duration_ms": 34465
  },
  "last_tool_name": "Bash",
  "uuid": "5207a484-238a-42a2-be64-98e31f90925d",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01FQB3Y81ZRWUTsaYtRHugE6`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif && python3 << 'EOF'\nimport pandas as pd\n\ndf = pd.read_csv('model_classification.csv')\nprint(\"DataFrame shape:\", df.shape)\nprint(\"\\nColumn names:\", df.columns.tolist())\nprint(\"\\nFirst 10 rows:\")\nprint(df.head(10))\nprint(\"\\nUnique cohorts:\", df['cohort_temporal'].unique())\nprint(\"\\nValue counts by cohort_temporal:\")\nprint(df['cohort_temporal'].value_counts())\nprint(\"\\nCross-tabulation:\")\nprint(pd.crosstab(df['model_type'], df['cohort_temporal'], margins=True))\nEOF\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "05085798-4413-4e54-8602-c1acfa2004c9",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011dwf3avF3UCuwEvRCikYrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 189,
      "cache_read_input_tokens": 31169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 189,
        "ephemeral_1h_input_tokens": 0
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

_source line 90 · 2026-05-23T01:31:01.944Z_

<details><summary>↩ Tool result · `toolu_01FQB3Y81ZRWUTsaYtRHugE6`</summary>

```text
DataFrame shape: (1887, 4)

Column names: ['model_name', 'model_type', 'cohort_temporal', 'family']

First 10 rows:
                  model_name model_type  cohort_temporal  family
0           01-ai/Yi-1.5-34B       base             2024  yi-1.5
1       01-ai/Yi-1.5-34B-32K       base             2024  yi-1.5
2      01-ai/Yi-1.5-34B-Chat   instruct             2024  yi-1.5
3  01-ai/Yi-1.5-34B-Chat-16K   instruct             2024  yi-1.5
4            01-ai/Yi-1.5-6B       base             2024  yi-1.5
5       01-ai/Yi-1.5-6B-Chat   instruct             2024  yi-1.5
6            01-ai/Yi-1.5-9B       base             2024  yi-1.5
7        01-ai/Yi-1.5-9B-32K       base             2024  yi-1.5
8       01-ai/Yi-1.5-9B-Chat   instruct             2024  yi-1.5
9   01-ai/Yi-1.5-9B-Chat-16K   instruct             2024  yi-1.5

Unique cohorts: [2024 2023]

Value counts by cohort_temporal:
cohort_temporal
2023    1080
2024     807
Name: count, dtype: int64

Cross-tabulation:
cohort_temporal  2023  2024   All
model_type                       
base              861   548  1409
instruct          219   259   478
All              1080   807  1887
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "bd55b7bc-df7b-4be4-8b41-a866bee8bf62"
}
```

</details>

---

### System

_source line 91_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Reading artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md",
  "usage": {
    "total_tokens": 32180,
    "tool_uses": 14,
    "duration_ms": 37060
  },
  "last_tool_name": "Read",
  "uuid": "5d584e32-37b5-4814-bf59-fef668569bf3",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 92_

<details open><summary>🔧 Tool call — Read · `toolu_01McvnKogL1T8ozbgwdtqxSD`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif_report.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "a9226ca1-a36a-40d3-9172-729191e215b2",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01BXHkAxUqAWL9Z5xbkBMvxJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 712,
      "cache_read_input_tokens": 31358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 712,
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

_source line 93 · 2026-05-23T01:31:03.818Z_

<details><summary>↩ Tool result · `toolu_01McvnKogL1T8ozbgwdtqxSD`</summary>

```text
1	# R18: Base vs Instruct DIF Separation Experiment
2	
3	## Sample Sizes
4	
5	| Group | Ref (2023) | Foc (2024) | Total |
6	|-------|-----------|-----------|-------|
7	| Base | 861 | 548 | 1409 |
8	| Instruct | 219 | 259 | 478 |
9	| Full (reported) | 1,080 | 807 | 1,887 |
10	
11	All subgroups have N ≥ 80; adequate power.
12	
13	## C% Comparison
14	
15	| Group | C% | DIF-C items |
16	|-------|-----|------------|
17	| Base | 32.1% | 4018/12508 |
18	| Instruct | 36.5% | 4567/12508 |
19	| Full (reported) | 31.3% | — |
20	
21	**Difference (base − instruct):** -4.4 pp
22	**Bootstrap 95% CI:** [-13.4, 4.3] (N=1000)
23	
24	## Difficulty–Direction Gradient
25	
26	Spearman correlation between item difficulty (2023 accuracy) and Δ_MH among DIF-C items:
27	
28	- **Base:** ρ = -0.570 (p = 0.00e+00, n = 4018)
29	- **Instruct:** ρ = -0.079 (p = 1.02e-07, n = 4567)
30	
31	## DIF Item Overlap
32	
33	| Metric | Value |
34	|--------|-------|
35	| C_base only | 1965 |
36	| C_instruct only | 2514 |
37	| Both | 2053 |
38	| Jaccard index | 0.314 |
39	| Expected Jaccard (independence) | 0.206 |
40	| Jaccard / Expected ratio | 1.5× |
41	
42	## DIF Direction Distribution
43	
44	| Group | Focal-favoring (2024↑) | Ref-favoring (2023↑) |
45	|-------|----------------------|---------------------|
46	| Base | 1605 (39.9%) | 2413 (60.1%) |
47	| Instruct | 2994 (65.6%) | 1573 (34.4%) |
48	
49	χ² = 562.70, p = 2.178e-124
50	
51	## Output Files
52	
53	- `model_classification.csv` — 1887 models classified
54	- `base_instruct_item_results.csv` — 12508 items with per-group DIF statistics
55	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "e7d9a70e-2448-44f0-9e7b-cfa14eefcabe"
}
```

</details>

---

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running ls -la /home/ubuntu/.agent-ml-research-idea_gen_0…",
  "usage": {
    "total_tokens": 33051,
    "tool_uses": 15,
    "duration_ms": 39339
  },
  "last_tool_name": "Bash",
  "uuid": "9f9db812-864c-40e2-92ec-51ef6876fc9e",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 95_

<details open><summary>🔧 Tool call — Bash · `toolu_01CMYjvj5wNGryTKCtVjXSAJ`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts/"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "953b3933-78b5-4ddc-8494-64d799fb14ad",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8XnjoidJp9BQ6Cx5feCUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 32070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 869,
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

_source line 96 · 2026-05-23T01:31:06.153Z_

<details><summary>↩ Tool result · `toolu_01CMYjvj5wNGryTKCtVjXSAJ`</summary>

```text
total 36
drwxr-xr-x  2 ubuntu ubuntu  4096 May 22 13:32 .
drwxr-xr-x 13 ubuntu ubuntu  4096 May 22 21:36 ..
-rw-r--r--  1 ubuntu ubuntu  6243 May 22 12:16 r14_cooks_d_analysis.py
-rw-r--r--  1 ubuntu ubuntu 10615 May 22 11:58 r14_domain_profile.py
-rw-r--r--  1 ubuntu ubuntu  4789 May 22 13:32 r16_dif_union.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "cdd1a2c5-104f-43f8-a87c-37881b6eb75f"
}
```

</details>

---

### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Searching for is_instruct|classify_model|model_type",
  "usage": {
    "total_tokens": 33052,
    "tool_uses": 16,
    "duration_ms": 40038
  },
  "last_tool_name": "Grep",
  "uuid": "43fdf87c-9271-4bd2-ad02-8df8a6bf384d",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 98_

<details open><summary>🔧 Tool call — Grep · `toolu_01YXzLaXs9YAX1NhD4Z9J6am`</summary>

```json
{
  "pattern": "is_instruct|classify_model|model_type",
  "type": "py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/scripts",
  "output_mode": "content",
  "head_limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "ad3c4083-0572-4221-982d-ace9780c1bc1",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01X8XnjoidJp9BQ6Cx5feCUZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 32070,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 869,
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

_source line 99 · 2026-05-23T01:31:06.805Z_

<details><summary>↩ Tool result · `toolu_01YXzLaXs9YAX1NhD4Z9J6am`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "b4517709-c859-4e8c-aebe-b9ce3849b400"
}
```

</details>

---

### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running find /home/ubuntu/.agent-ml-research-idea_gen_052…",
  "usage": {
    "total_tokens": 33541,
    "tool_uses": 17,
    "duration_ms": 41726
  },
  "last_tool_name": "Bash",
  "uuid": "be67c604-bc6f-4866-9cae-6cf08837e904",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 101_

<details open><summary>🔧 Tool call — Bash · `toolu_01Nrt6g7pUQfLHuNz3W7vuei`</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen -name \"*r18*\" -o -name \"*base*instruct*\" 2>/dev/null | head -20"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "beaef0e7-00f9-4001-bc7d-e8c5d5d95ae5",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Hmn3VuK8bWMNqdi4jJUVSA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 486,
      "cache_read_input_tokens": 32939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 486,
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

_source line 102 · 2026-05-23T01:31:08.569Z_

<details><summary>↩ Tool result · `toolu_01Nrt6g7pUQfLHuNz3W7vuei`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_research_base_vs_instruct_metadata_20260522T174407.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_research_base_vs_instruct_metadata_20260522T174407_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_restricted_range_rho_20260522T163431_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_dedup_k_curve_20260522T163407.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_icc_by_family_size_20260522T163330.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_base_vs_instruct_dif_20260522T174522_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_icc_by_family_size_20260522T163330_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_base_vs_instruct_dif_20260522T174522.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_rank_bucket_reversal_20260522T163346_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_restricted_range_rho_20260522T163431.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_rank_bucket_reversal_20260522T163346.log
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/logs/workers/worker_code_r18_dedup_k_curve_20260522T163407_result.json
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/base_instruct_survey.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/_project/report/base_instruct_dif_report.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_restricted_range_rho
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_icc_by_family_size
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif
/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "bbba8790-78ee-435b-a49a-f6caac84c352"
}
```

</details>

---

### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Reading artifacts/r18_base_instruct_survey/base_instruct_survey.md",
  "usage": {
    "total_tokens": 34818,
    "tool_uses": 18,
    "duration_ms": 43738
  },
  "last_tool_name": "Read",
  "uuid": "4cfbefcb-d7b2-4864-9083-822aab524f3a",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Read · `toolu_012GSUVgpkFKaqtvmd5gCpLV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "41faee1d-be99-446b-960f-f304e170c9ff",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016sBB4D5QLqQwStrQYDFYNx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1276,
      "cache_read_input_tokens": 33425,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1276,
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

_source line 105 · 2026-05-23T01:31:10.495Z_

<details><summary>↩ Tool result · `toolu_012GSUVgpkFKaqtvmd5gCpLV`</summary>

```text
1	# R18: Base vs Instruct Model Classification Survey
2	
3	## 1. Existing Metadata
4	
5	`model_metadata.csv` (5,227 models) contains a `training_method` column with values:
6	
7	| training_method | count |
8	|---|---|
9	| unknown | 4,676 |
10	| DPO | 347 |
11	| SFT | 136 |
12	| ORPO | 52 |
13	| PPO | 10 |
14	| KTO | 6 |
15	
16	No explicit `is_base` / `is_instruct` field exists. The `training_method` field identifies 551 instruct/aligned models (10.5%), but 89.5% are `unknown`.
17	
18	## 2. Heuristic Classification
19	
20	Two-signal approach:
21	1. **training_method**: DPO/SFT/ORPO/PPO/KTO → instruct
22	2. **Name patterns** (case-insensitive): `-instruct`, `-chat`, `-it` (word boundary), `-rlhf`, `-dpo`, `-sft`, `-aligned`, `-ift`, `-assistant`, `-turbo`
23	
24	| model_type | count | pct |
25	|---|---|---|
26	| base | 4,109 | 78.6% |
27	| instruct | 1,118 | 21.4% |
28	
29	Classification reason breakdown:
30	
31	| reason | count |
32	|---|---|
33	| default_base (no instruct signal) | 4,109 |
34	| name_pattern (regex match) | 511 |
35	| training_method (explicit) | 551 |
36	| name_keyword (Instruct/Chat/IT) | 56 |
37	
38	**Known limitations**: The 4,109 "base" models include fine-tuned/merged models that lack instruct keywords (e.g., `alignment-model-test`, `*-merged`, `*-mix`). Approximately 234 base-classified models have ambiguous patterns (`finetun`, `align`, `merged`, `mix`, `gguf`, `gptq`, `awq`). Most of these are quantized variants (GGUF/GPTQ/AWQ) which preserve the original model's type, so the misclassification risk is moderate but not zero.
39	
40	## 3. Sub-group Sizes
41	
42	### By Cohort
43	
44	| cohort | base | instruct | total |
45	|---|---|---|---|
46	| 2023 (ref) | 838 | 242 | 1,080 |
47	| 2024 (foc) | 518 | 289 | 807 |
48	| other | 2,753 | 587 | 3,340 |
49	| **All** | **4,109** | **1,118** | **5,227** |
50	
51	### DIF Sub-groups (cohort × model_type)
52	
53	| sub-group | n | ≥80 threshold |
54	|---|---|---|
55	| 2023-base | 838 | pass |
56	| 2023-instruct | 242 | pass |
57	| 2024-base | 518 | pass |
58	| 2024-instruct | 289 | pass |
59	
60	All four sub-groups far exceed the minimum n=80 for MH-DIF.
61	
62	### By Family (families with both base and instruct)
63	
64	32 families have both base and instruct variants. Top families:
65	
66	| family | base | instruct | instruct% |
67	|---|---|---|---|
68	| mistral | 444 | 103 | 19.0% |
69	| llama-3 | 184 | 131 | 41.6% |
70	| llama-2 | 108 | 53 | 32.9% |
71	| mixtral | 100 | 20 | 16.7% |
72	| gemma | 55 | 17 | 23.6% |
73	| gemma-2 | 17 | 19 | 52.8% |
74	| deepseek | 14 | 10 | 41.7% |
75	
76	## 4. Accuracy Distributions
77	
78	| group | n | mean | median |
79	|---|---|---|---|
80	| base (all) | 4,109 | 0.594 | 0.664 |
81	| instruct (all) | 1,118 | 0.582 | 0.646 |
82	| 2023-base | 838 | 0.593 | 0.638 |
83	| 2023-instruct | 242 | 0.541 | 0.608 |
84	| 2024-base | 518 | 0.598 | 0.668 |
85	| 2024-instruct | 289 | 0.623 | 0.677 |
86	
87	Notable: In 2024, instruct models are slightly higher-performing than base models (mean 0.623 vs 0.598), while in 2023 the pattern reverses (0.541 vs 0.593). This ability-level difference is important for DIF matching.
88	
89	## 5. MH-DIF Feasibility Assessment
90	
91	**Verdict: Feasible, with caveats.**
92	
93	**Strengths:**
94	- All four sub-groups (base/instruct × 2023/2024) have n ≥ 200, well above the n=80 minimum
95	- 32 families have both base and instruct variants, enabling within-family controls
96	- The `training_method` field provides ground-truth labels for 551 models
97	
98	**Caveats:**
99	- 78.6% of models are classified as "base" by default (no instruct signal detected). Some fraction of these are actually fine-tuned/instruction-tuned models that lack standard naming conventions
100	- Accuracy distributions differ between base and instruct groups, especially in 2023 cohort. MH-DIF requires ability matching — the theta-stratification in our existing pipeline handles this, but the base/instruct imbalance means some strata may be dominated by one type
101	- The "other" cohort (n=3,340) is excluded from temporal DIF but could be used for a base-vs-instruct DIF analysis ignoring temporal effects
102	
103	**Possible experimental designs:**
104	1. **3-way DIF**: cohort(2023/2024) × model_type(base/instruct) as grouping variable — tests whether contamination DIF differs for base vs instruct models
105	2. **Within-family paired analysis**: For families with both variants (e.g., Llama-3), compare DIF item flags between base and instruct sub-populations
106	3. **Conservative subset**: Use only the 551 models with explicit training_method labels + name-matched base counterparts for higher-confidence classification
107	
108	## 6. Output Files
109	
110	- `model_type_classification.csv`: Full classification with columns `model_name, family, cohort_temporal, training_method, accuracy, model_type, classification_reason`
111	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "28410795-bb95-453d-9f22-60ff94168c94"
}
```

</details>

---

### System

_source line 106_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Running grep -r \"is_instruct\\|base_model\\|instruct_model\\…",
  "usage": {
    "total_tokens": 36843,
    "tool_uses": 19,
    "duration_ms": 46592
  },
  "last_tool_name": "Bash",
  "uuid": "8ebb48ed-a250-4a93-b6a7-0b8e93b1114f",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — Bash · `toolu_013FDMkqPpuzNeRMxsjXsuL9`</summary>

```json
{
  "command": "grep -r \"is_instruct\\|base_model\\|instruct_model\\|model_type\\|861.*548\\|219.*259\" /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/*.md --ignore-case 2>/dev/null | head -30"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "bb7060cf-1ffc-4aca-bcff-357872e7ea3f",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013f2WQpVAoHVkWNe6jRYw4j",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 2023,
      "cache_read_input_tokens": 34701,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2023,
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

_source line 108 · 2026-05-23T01:31:13.400Z_

<details><summary>↩ Tool result · `toolu_013FDMkqPpuzNeRMxsjXsuL9`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "8ace6a3b-7af1-4aec-91d3-e8f23d4293b9"
}
```

</details>

---

### System

_source line 109_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "description": "Reading memory.md",
  "usage": {
    "total_tokens": 37023,
    "tool_uses": 20,
    "duration_ms": 48209
  },
  "last_tool_name": "Read",
  "uuid": "9064032f-e22f-4e5f-b33a-8e5033863fbb",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Read · `toolu_01HEzvJJRsxJarPCitJpaAuk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/memory.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "8155e2db-0955-47f1-be39-dfa4939ac999",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DJPAjv7No86RAocCgtSXNs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 36724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 173,
        "ephemeral_1h_input_tokens": 0
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

_source line 111 · 2026-05-23T01:31:14.961Z_

<details><summary>↩ Tool result · `toolu_01HEzvJJRsxJarPCitJpaAuk`</summary>

```text
1	## MVP 验证关键经验 (2026-05-20)
2	
3	### D001 决策：ETS C 分类 > p-value 检验
4	- **p-value based DIF 检测在 200-item benchmark 上严重 underpowered**：BH 校正后 TPR 仅 0.04-0.07（N=50, δ=1.0）
5	- **ETS C 分类（|Δ_MH|≥1.5 + 显著性）是可行的替代**：TPR=0.68-0.85 at N≥80, δ≥1.4
6	- **AUC 一直很好（0.91-0.96）**
7	
8	### 关键操作参数
9	- N≥80/group 最低要求，N≥100 显著改善
10	- δ≥1.4 logits 可靠检测区间
11	- MH 5 层 quantile + ETS C 阈值是最佳组合
12	- Subject ≥200 items 才有足够 matching precision（<100 items baseline FPR 膨胀至 ~56%）
13	
14	## D006: plan_011 Semi-Synthetic 验证成功 ✅
15	
16	### DIF 检测差异性污染有效
17	- **External MH**: temporal ΔTPR=+0.674 (0.326→1.000), FPR 恒定 0.314
18	- **Matching variable contamination**: 20% items 注入时 standard MH FPR 0.298→0.616, anchor/external 免疫
19	- **Li et al. enrichment≈1.0 原因**: web-overlap = 全局性污染，不产生 DIF
20	
21	## D007-D010: 降低 FPR 路线全部穷尽 ⚠️
22	
23	### plan_012 θ-Conditioning 失败
24	- logit θ 与 total score 相关性 0.9986 → 单维 θ 分层 ≡ 总分分层
25	
26	### plan_014 Within-Subject 前置检查：C% = 38.1% (>25%)
27	- 5 个高 C% subjects 的 within-subject temporal C% 均 >25%（31-45%）
28	- Within vs cross-subject matching 差异仅 -2.4pp → 信号对 matching 不敏感
29	- **结论**：temporal DIF 渗透到每个 subject 内部，不是 between-subject 能力差异的伪影
30	- Bifactor 方向因此否定（D010）
31	
32	### plan_013 Q3 局部独立性：温和但存在
33	- Within-subject mean Q3 = 0.009（低于 0.20 阈值）
34	- 但 11.3% within-subject pairs |Q3|>0.20（vs 2.2% cross-subject，5x）
35	- 最严重: moral_scenarios 34.2%, world_religions 18%, marketing 17.5%
36	- 不太可能单独解释 31% FPR
37	
38	### plan_016 Within-Subject Semi-Synthetic：DIF 在 subject 内也有效 ✅
39	- Cross-subject matching FPR 完全稳定（ΔFPR=0.000），4/5 subjects ΔTPR>0.3
40	- Within-subject matching FPR 膨胀 +0.067 to +0.281（matching variable 包含注入 items）
41	- **结论**：within-subject 38% C% 是真实 temporal DIF，方法论有效
42	
43	### 综合推导：31% temporal FPR 不是 artifact
44	证伪链完整：1D θ 无效 → within-subject 仍高 → bifactor 否定 → Q3 不是主因 → **这是 genuine temporal DIF**（2023→2024 模型在特定 items 上的真实差异性表现变化）。DIF 方法有效但无法区分 contamination-DIF 和 capability-DIF。
45	
46	## D012: plan_017 Downstream Impact — DIF Items ≠ 噪声 ⚠️
47	
48	### Hypothesis 被证伪但发现更有价值
49	- **假设**: 移除 DIF items → 排名更稳定 → DIF 标记了 problematic items
50	- **实际**: DIF 移除造成 **更大** 排名扰动（z = -8 to -49σ, 21/21 条件）
51	- DIF items 是浓缩的差异化信息载体，不是噪声
52	
53	### 关键数字
54	- Full vs stable-only: ρ = 0.996-0.999（排名本身极鲁棒）
55	- DIF items 跨代准确率变化 = full benchmark 的 1.09×, stable = 0.96×
56	- Top beneficiaries: phi-3, llama-3 衍生（+700-850 rank positions）
57	- Top hurt: mistral merge/slerp 模型（-400 to -587 rank positions）
58	
59	### 对论文的启示
60	- DIF items 不是"要清洗的坏题"——是"揭示模型代际差异的诊断工具"
61	- 支持 characterization narrative > cleaning narrative
62	- "Stable-only benchmark" 不是"更好的 benchmark"，而是"不同视角的 benchmark"
63	
64	## plan_004: GSM8K Cross-Benchmark Validation (2026-05-21) 🔑
65	
66	### Step 1: GSM8K Temporal DIF 跨 benchmark 泛化 ✅
67	- GSM8K standard C% = 18.9%（MMLU 31.3%，同一量级）
68	- Sanity check 0.3%（通过）
69	- External matching C% = 47.4%——**非 contamination absorption**，是 construct validity gap（external benchmarks 测不同能力，控制了这些能力后 GSM8K item 行为差异更大）
70	- Standard vs external Spearman ρ = 0.926（高度一致）
71	
72	### Step 2: GSM8K Semi-Synthetic 验证 ✅
73	- Standard ΔTPR = +0.818 at p=1.0（MMLU +0.508，GSM8K 更强）
74	- External ΔTPR = +0.517
75	- GSM8K 的 DIF 对差异性污染更敏感（单域 benchmark, items 更同质）
76	
77	### Step 3: GSM1K Contamination Gap × DIF Correlation — 方向反转 ❌→🔑
78	- **r = −0.478 (p=0.005)**：contaminated 模型在 DIF-C items 上更差，非更好
79	- Partial r = −0.385 控制整体准确率后仍显著
80	- Permutation p = 0.014，robust to leave-one-out
81	- 171/249 DIF-C items α_MH < 1 → favor focal (2024) models（捕获真实代际能力提升）
82	- 78/249 DIF-C items α_MH > 1 → favor reference (2023) models
83	
84	### Step 3 核心洞察
85	- **DIF ⊥ contamination**：DIF 捕捉的 measurement anomalies 与 contamination 正交
86	- 171 个 focal-favoring DIF-C items 捕获真实代际能力提升，但 contaminated 模型在这些 items 上反而更差（r=−0.347, p=0.048）——contamination 的"浅层"boost 无法泛化到区分真实能力的题目
87	- **这是 characterization narrative 的强 evidence**：DIF 不标记"被污染的 items"，标记的是"不同模型代际间行为模式不一致的 items"
88	- 与 Xu et al. (2024) GSM1K 互补——他们检测 contamination，我们检测 construct-level measurement anomalies
89	
90	### α_MH 方向约定（Reviewer 修正 2026-05-21）
91	- α_MH > 1 → item 对 reference group 更容易
92	- α_MH < 1 → item 对 focal group 更容易
93	- 在 temporal cohort 中：reference = 2023, focal = 2024
94	
95	## plan_028: Multi-Benchmark Temporal DIF (2026-05-21) ✅
96	
97	### 跨 benchmark 泛化确认
98	- 6/6 benchmarks 全部显示显著 temporal DIF (C% 17.9-31.3%)
99	- Knowledge/reasoning 类 C% 更高: MMLU 31.3%, WinoGrande 30.3%, TruthfulQA 29.7%, ARC 26.9%
100	- Math/commonsense 类 C% 稍低: GSM8K 18.9%, HellaSwag 17.9%
101	- 所有 random-split controls < 1% (0.18-0.60%)
102	- C%/random 比值范围 45×-174×
103	- 直接回应 Dream #6 "only MMLU + GSM8K, generalizability insufficient" 的审稿意见
104	
105	### 技术教训
106	- hellaswag.csv 2GB / 52M rows，7.6GB RAM 机器上 pd.read_csv + pivot 必 OOM
107	- 解决方案：chunked loading (2M rows/chunk)，先扫 source/item 索引再填矩阵
108	
109	## plan_031: Temporal Granularity (2026-05-21) ✅
110	
111	### DIF 在 6 个月内即饱和
112	- Half-year (H2 vs H1) C% > full-year C%，5/5 benchmarks 一致
113	- MMLU: 34.35% vs 31.32% (+3.03pp), ARC: 29.27% vs 26.88% (+2.39pp)
114	- 机制：去掉 62 个 2023-H1 早期模型 → reference group 更同质 → DIF 检测灵敏度提升
115	- **cohort purity > temporal distance** 对 DIF 检测的影响更大
116	- 回应 Dream #7 "binary temporal split 过于粗糙" 审稿意见
117	
118	## plan_032: DIF-Cleaned MMLU Demonstration (2026-05-21) ⭐
119	
120	### ρ=0.997 掩盖的系统性偏差（化解 actionability paradox 的关键）
121	- 全局 ρ=0.9965 确实高，但 **89.5% 模型排名变化 ≥5 位，24.8% 变化 ≥100 位**
122	- **系统性 cohort 偏差**: 2024 模型清洗后平均掉 73.6 位，2023 模型上升 22.6 位
123	- DIF items 系统性偏向 2024 新模型（phi-3 +258, llama-3 +121, solar +149; mistral -53）
124	- 论文 narrative: ρ 高不代表 DIF 不重要——局部排名剧变 + 系统性 cohort 偏差 = benchmark fairness 问题
125	
126	## plan_033: Subject-Level DIF Concentration (2026-05-21) ⭐
127	
128	### DIF rate 均匀但 direction 分化
129	- DIF rate 跨 domain 无差异: STEM 30.9%, Humanities 31.1%, Social 31.6% (p=0.78)
130	- **DIF direction 有强领域依赖**: STEM 55.4% favor 2024 vs Humanities 仅 35.6%
131	- world_religions (83% favor 2023), logical_fallacies (80% favor 2023) 呈近单向偏向
132	- **解释**: 2024 模型 STEM 能力提升但人文类知识表现模式改变（可能是 alignment/蒸馏影响）
133	- Item properties (difficulty + discrimination) 仅解释 4% DIF variance (R²=0.042) → **content 是 DIF 主驱动力**
134	- 5 个 subject 有 excess DIF: professional_law, human_aging, world_religions, business_ethics, professional_medicine
135	
136	## plan_034: Multi-Subject Simultaneous Injection (2026-05-21) ⭐
137	
138	### Proposition 1 boundary: k ≈ 5-10 subjects
139	- **k ≤ 5 (≤8.8% subjects)**: ΔFPR < 0.007，Proposition 1 实际成立
140	- **k = 10 (17.5%)**: p ≥ 0.3 时 ΔFPR 显著（+0.026 ~ +0.069）
141	- **k = 20 (35.1%)**: ΔFPR 大幅膨胀（p=0.5 时 +0.167）
142	- **p=0.1 全 k robust**: 即使 k=20，ΔFPR ≈ 0.001
143	- **TPR 随 k 下降**: 0.834→0.611 at p=0.5（matching variable 吸收 DIF 信号）
144	- **实际意义**: real-world 污染通常 <10% subjects，cross-subject auditing 有充足 safety margin
145	- **boundary rule**: contaminated fraction < 10% matching variable → ΔFPR negligible
146	
147	## plan_035: Q3 LD Inflation Simulation (2026-05-21) ⭐
148	
149	### Cross-subject matching 完全隔离 LD 影响
150	- 8 subjects（Q3 4.6%-34.2%），1000 permutations + independence control
151	- **ETS-C LD 膨胀**: mean +0.0004pp, max +0.001pp → 远低于 3pp
152	- **p<0.05 LD 膨胀**: mean −0.0019pp（无膨胀，甚至略反向）
153	- **两个保护机制**: (1) cross-subject matching 不含当前 subject → LD 无法污染 matching; (2) ETS-C |Δ|≥1.5 极保守（actual FPR ~0.1% vs nominal 5%）
154	- Q3 与膨胀无显著相关（ρ=−0.24, p=0.57）
155	- **直接回应 Reviewer 对 local independence violation 的担忧**
156	
157	## 数据源 (2026-05-20)
158	
159	### METABENCH (Kipnis et al., ICLR 2025) ⭐
160	- GitHub: https://github.com/adkipnis/metabench
161	- Zenodo: https://zenodo.org/records/12819251 (620MB)
162	- MMLU 12,508 items, 5,219 模型
163	
164	### D002: preproc.rds diff/disc 是 CTT 不是 IRT
165	- diff = 0.75 × p_correct, disc = rpbis
166	- 实际 IRT 在 crossvalidate.R 用 mirt::mirt() slope-intercept
167	
168	### Li et al. (EMNLP 2024) Proxy Ground Truth
169	- 9,229/12,508 items 有标注（73.8%）
170	- clean 60.5% / input_and_label 33.0% / input_only 6.5%
171	- Web overlap proxy，非训练数据精确标签——全局性污染，不适合 DIF 验证
172	
173	## plan_036: Growing Pains Paper Lookup (2026-05-21)
174	
175	### FPC = Fixed Parameter Calibration, 非污染检测
176	- Habba et al., arXiv 2604.12843 (April 2026)
177	- 用 IRT anchor items 做高效 benchmark 校准，非 contamination detection
178	- Anchor items 动态计算、未公开持久化，无法做 overlap 分析
179	- Limitations 承认 anchor items 可能被污染 → 支持我们 DIF 的必要性论点
180	- 适合在 Related Work 中引用
181	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "508edb7d-41f0-475e-8a1b-de6f506b3db3"
}
```

</details>

---

### System

_source line 112_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac97c55aacb86e0e3",
  "tool_use_id": "toolu_01ViRLXs9GVxF2te3o5iEf9n",
  "status": "completed",
  "output_file": "",
  "summary": "Find base/instruct split logic",
  "usage": {
    "total_tokens": 41813,
    "tool_uses": 20,
    "duration_ms": 62963
  },
  "uuid": "4104a7eb-4fbb-458b-925f-e8e4d34a5624",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool result

_source line 113 · 2026-05-23T01:31:29.713Z_

<details><summary>↩ Tool result · `toolu_01ViRLXs9GVxF2te3o5iEf9n`</summary>

````text
Perfect! Now let me create a comprehensive summary document with all the findings:

## Summary: Model Classification as "Base" vs "Instruct"

I found the complete implementation of the base/instruct classification logic. Here are the key findings:

### Primary Implementation File
**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py`

This is the R18 (Research 18) experiment that performs the base vs instruct DIF separation analysis.

### Classification Logic (Lines 21-53 of base_instruct_dif.py)

The classification uses a **regex-based heuristic** with two main patterns:

1. **INSTRUCT_SUFFIXES** (lines 21-25): Detects instruction-tuning indicators
   ```python
   r"[-_\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)"
   ```
   - Matches: `instruct`, `chat`, `it`, `rlhf`, `dpo`, `sft`, `aligned`, `ppo`
   - Case-insensitive matching

2. **QUANT_SUFFIXES** (lines 27-30): Strips quantization/format suffixes before classification
   - Prevents false positives from quantized variants (GPTQ, AWQ, GGUF, etc.)

3. **FAMILY_PREFIX_EXCLUDE** (lines 32-35): Handles special families
   - Models starting with `openchat`, `chatglm`, `chatml` that contain "chat" but are still base models

### The `classify_model()` Function (Lines 38-53)

```python
def classify_model(name: str) -> str:
    1. Extract short name (after last "/" if present)
    2. Strip quantization suffixes
    3. Check for "-it" ending → classify as "instruct"
    4. Check INSTRUCT_SUFFIXES pattern → classify as "instruct" (with family exclusion handling)
    5. Default → classify as "base"
```

### Verified Classification Counts

The classification was run on the full metadata and produced the **exact counts you expected**:

| Group | Ref (2023) | Foc (2024) | Total |
|-------|-----------|-----------|-------|
| **Base** | **861** | **548** | 1,409 |
| **Instruct** | **219** | **259** | 478 |
| **Full** | 1,080 | 807 | 1,887 |

### Output Files Generated

1. **model_classification.csv** (102 KB, 1,887 models)
   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv`
   - Columns: `model_name`, `model_type`, `cohort_temporal`, `family`

2. **base_instruct_dif_report.md** (detailed analysis report)
   - Shows C% comparison (Base 32.1% vs Instruct 36.5%)
   - Bootstrap 95% CI: [-13.4, 4.3]
   - Spearman correlation between difficulty and DIF effect size
   - DIF item overlap analysis (Jaccard 0.314)
   - Direction distribution (base models 39.9% focal-favoring, instruct 65.6%)

3. **base_instruct_item_results.csv** (1.8 MB)
   - Per-item DIF statistics for all 12,508 MMLU items
   - Separate delta_mh, p-values, and ETS classification for base and instruct groups

### Additional Survey File

**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md`

This contains metadata analysis showing:
- 78.6% of all 5,227 models classified as base
- 21.4% classified as instruct
- 551 models have explicit `training_method` field (DPO/SFT/ORPO/PPO/KTO)
- 32 model families have both base and instruct variants (Mistral, Llama-3, Llama-2, Mixtral, Gemma, etc.)

### Technical Details

- **MH-DIF Analysis**: 5 stratification bins on quantile totals, threshold |Δ_MH| ≥ 1.5, α = 0.05
- **Response Matrix**: 1,887 models × 12,508 MMLU items (sparse CSR format)
- **Bootstrap Resampling**: 1,000 iterations for confidence intervals
- **Direction Analysis**: Chi-square test for independence (χ² = 562.70, p = 2.178e-124)

The classification is simple, transparent, and has been validated against the expected counts perfectly.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "f11a9792-09f7-426f-9ba7-879a8264561e",
  "tool_use_result": {
    "status": "completed",
    "prompt": "In the project at `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/`, I need to find how models are classified as \"base\" vs \"instruct\". The expected counts are:\n- Base: 861 ref (2023), 548 foc (2024) \n- Instruct: 219 ref (2023), 259 foc (2024)\n\nSearch for:\n1. Any R18 analysis code or files that implement this split\n2. Any Python files that define is_instruct or is_base logic\n3. Any CSV files that have a base/instruct column or model_type column\n4. Grep for \"is_instruct\", \"is_base\", \"model_type\", \"base_model\", \"instruct\" in Python files\n5. Check artifacts/ directory for any file that might contain this mapping\n\nLook in `artifacts/`, `scripts/`, and any other directories.",
    "agentId": "ac97c55aacb86e0e3",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now let me create a comprehensive summary document with all the findings:\n\n## Summary: Model Classification as \"Base\" vs \"Instruct\"\n\nI found the complete implementation of the base/instruct classification logic. Here are the key findings:\n\n### Primary Implementation File\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py`\n\nThis is the R18 (Research 18) experiment that performs the base vs instruct DIF separation analysis.\n\n### Classification Logic (Lines 21-53 of base_instruct_dif.py)\n\nThe classification uses a **regex-based heuristic** with two main patterns:\n\n1. **INSTRUCT_SUFFIXES** (lines 21-25): Detects instruction-tuning indicators\n   ```python\n   r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)\"\n   ```\n   - Matches: `instruct`, `chat`, `it`, `rlhf`, `dpo`, `sft`, `aligned`, `ppo`\n   - Case-insensitive matching\n\n2. **QUANT_SUFFIXES** (lines 27-30): Strips quantization/format suffixes before classification\n   - Prevents false positives from quantized variants (GPTQ, AWQ, GGUF, etc.)\n\n3. **FAMILY_PREFIX_EXCLUDE** (lines 32-35): Handles special families\n   - Models starting with `openchat`, `chatglm`, `chatml` that contain \"chat\" but are still base models\n\n### The `classify_model()` Function (Lines 38-53)\n\n```python\ndef classify_model(name: str) -> str:\n    1. Extract short name (after last \"/\" if present)\n    2. Strip quantization suffixes\n    3. Check for \"-it\" ending → classify as \"instruct\"\n    4. Check INSTRUCT_SUFFIXES pattern → classify as \"instruct\" (with family exclusion handling)\n    5. Default → classify as \"base\"\n```\n\n### Verified Classification Counts\n\nThe classification was run on the full metadata and produced the **exact counts you expected**:\n\n| Group | Ref (2023) | Foc (2024) | Total |\n|-------|-----------|-----------|-------|\n| **Base** | **861** | **548** | 1,409 |\n| **Instruct** | **219** | **259** | 478 |\n| **Full** | 1,080 | 807 | 1,887 |\n\n### Output Files Generated\n\n1. **model_classification.csv** (102 KB, 1,887 models)\n   - Location: `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv`\n   - Columns: `model_name`, `model_type`, `cohort_temporal`, `family`\n\n2. **base_instruct_dif_report.md** (detailed analysis report)\n   - Shows C% comparison (Base 32.1% vs Instruct 36.5%)\n   - Bootstrap 95% CI: [-13.4, 4.3]\n   - Spearman correlation between difficulty and DIF effect size\n   - DIF item overlap analysis (Jaccard 0.314)\n   - Direction distribution (base models 39.9% focal-favoring, instruct 65.6%)\n\n3. **base_instruct_item_results.csv** (1.8 MB)\n   - Per-item DIF statistics for all 12,508 MMLU items\n   - Separate delta_mh, p-values, and ETS classification for base and instruct groups\n\n### Additional Survey File\n\n**Location:** `/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_instruct_survey/base_instruct_survey.md`\n\nThis contains metadata analysis showing:\n- 78.6% of all 5,227 models classified as base\n- 21.4% classified as instruct\n- 551 models have explicit `training_method` field (DPO/SFT/ORPO/PPO/KTO)\n- 32 model families have both base and instruct variants (Mistral, Llama-3, Llama-2, Mixtral, Gemma, etc.)\n\n### Technical Details\n\n- **MH-DIF Analysis**: 5 stratification bins on quantile totals, threshold |Δ_MH| ≥ 1.5, α = 0.05\n- **Response Matrix**: 1,887 models × 12,508 MMLU items (sparse CSR format)\n- **Bootstrap Resampling**: 1,000 iterations for confidence intervals\n- **Direction Analysis**: Chi-square test for independence (χ² = 562.70, p = 2.178e-124)\n\nThe classification is simple, transparent, and has been validated against the expected counts perfectly."
      }
    ],
    "totalDurationMs": 62965,
    "totalTokens": 42945,
    "totalToolUseCount": 20,
    "usage": {
      "input_tokens": 4,
      "cache_creation_input_tokens": 4789,
      "cache_read_input_tokens": 36897,
      "output_tokens": 1255,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4789
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4,
          "output_tokens": 1255,
          "cache_read_input_tokens": 36897,
          "cache_creation_input_tokens": 4789,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4789,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 4,
      "searchCount": 5,
      "bashCount": 11,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  }
}
````

</details>

---

### Assistant

_source line 114_

Now I have everything I need. The R18 classification code is at `artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py` and there's already a `model_classification.csv`. Let me read the classification function and the existing CSV, then build the new experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "acf29178-a296-4dfb-bd5f-a5beafdb83f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5V5MWmPQn1uWnMS5gKycY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 41231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 115_

<details open><summary>🔧 Tool call — Read · `toolu_01Xpfz8XTDgUwWWzcXMce24N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
  "limit": 70
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "d1fe238e-f546-4162-841d-3acf12c7c8ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5V5MWmPQn1uWnMS5gKycY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 41231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 116 · 2026-05-23T01:31:34.954Z_

<details><summary>↩ Tool result · `toolu_01Xpfz8XTDgUwWWzcXMce24N`</summary>

```text
1	#!/usr/bin/env python3
2	"""R18: Base vs Instruct MH-DIF separation experiment."""
3	
4	import re
5	import sys
6	import numpy as np
7	import pandas as pd
8	from scipy import sparse
9	from scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency
10	
11	ROOT = "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts"
12	OUT = f"{ROOT}/r18_base_vs_instruct_dif"
13	
14	N_STRATA = 5
15	N_BOOT = 1000
16	ALPHA = 0.05
17	DELTA_THRESH = 1.5
18	
19	# ── Part 1: Model classification ─────────────────────────────────────────
20	
21	INSTRUCT_SUFFIXES = re.compile(
22	    r"[-_\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)"
23	    r"([-_\.]|$)",
24	    re.IGNORECASE,
25	)
26	
27	QUANT_SUFFIXES = re.compile(
28	    r"[-_\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])",
29	    re.IGNORECASE,
30	)
31	
32	FAMILY_PREFIX_EXCLUDE = re.compile(
33	    r"^(openchat|chatglm|chatml)",
34	    re.IGNORECASE,
35	)
36	
37	
38	def classify_model(name: str) -> str:
39	    short = name.split("/")[-1] if "/" in name else name
40	    stripped = QUANT_SUFFIXES.sub("", short)
41	
42	    if stripped.lower().endswith("-it"):
43	        return "instruct"
44	
45	    if INSTRUCT_SUFFIXES.search(stripped):
46	        prefix_part = stripped.split("-")[0].split("_")[0]
47	        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):
48	            rest = stripped[len(prefix_part):]
49	            if not INSTRUCT_SUFFIXES.search(rest):
50	                return "base"
51	        return "instruct"
52	
53	    return "base"
54	
55	
56	# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────
57	
58	def mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):
59	    """Vectorized MH-DIF returning per-item details.
60	
61	    Returns (c_pct, delta_mh, pval, is_c).
62	    """
63	    n_ref, J = X_ref.shape
64	    n_foc = X_foc.shape[0]
65	
66	    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()
67	    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()
68	    s_all = np.concatenate([tot_ref, tot_foc])
69	
70	    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "dee400a4-07a7-47f3-828c-65ce5fddb124",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/base_instruct_dif.py",
      "content": "#!/usr/bin/env python3\n\"\"\"R18: Base vs Instruct MH-DIF separation experiment.\"\"\"\n\nimport re\nimport sys\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse\nfrom scipy.stats import chi2 as chi2_dist, spearmanr, chi2_contingency\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = f\"{ROOT}/r18_base_vs_instruct_dif\"\n\nN_STRATA = 5\nN_BOOT = 1000\nALPHA = 0.05\nDELTA_THRESH = 1.5\n\n# ── Part 1: Model classification ─────────────────────────────────────────\n\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)\"\n    r\"([-_\\.]|$)\",\n    re.IGNORECASE,\n)\n\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\",\n    re.IGNORECASE,\n)\n\nFAMILY_PREFIX_EXCLUDE = re.compile(\n    r\"^(openchat|chatglm|chatml)\",\n    re.IGNORECASE,\n)\n\n\ndef classify_model(name: str) -> str:\n    short = name.split(\"/\")[-1] if \"/\" in name else name\n    stripped = QUANT_SUFFIXES.sub(\"\", short)\n\n    if stripped.lower().endswith(\"-it\"):\n        return \"instruct\"\n\n    if INSTRUCT_SUFFIXES.search(stripped):\n        prefix_part = stripped.split(\"-\")[0].split(\"_\")[0]\n        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):\n            rest = stripped[len(prefix_part):]\n            if not INSTRUCT_SUFFIXES.search(rest):\n                return \"base\"\n        return \"instruct\"\n\n    return \"base\"\n\n\n# ── Part 2: MH-DIF (extended) ────────────────────────────────────────────\n\ndef mh_dif_full(X_ref, X_foc, n_strata=N_STRATA):\n    \"\"\"Vectorized MH-DIF returning per-item details.\n\n    Returns (c_pct, delta_mh, pval, is_c).\n    \"\"\"\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = np.asarray(X_ref.sum(axis=1), dtype=np.float64).ravel()\n    tot_foc = np.asarray(X_foc.sum(axis=1), dtype=np.float64).ravel()\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))",
      "numLines": 70,
      "startLine": 1,
      "totalLines": 374
    }
  }
}
```

</details>

---

### Tool call

_source line 117_

<details open><summary>🔧 Tool call — Bash · `toolu_01TcAfcumRZ25HbS9vdRDb6J`</summary>

```json
{
  "command": "head -5 /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/r18_base_vs_instruct_dif/model_classification.csv && echo \"---\" && python3 -c \"\nimport pandas as pd\nmc = pd.read_csv('artifacts/r18_base_vs_instruct_dif/model_classification.csv')\nprint('Columns:', list(mc.columns))\nprint()\nprint(pd.crosstab(mc['cohort_temporal'], mc['model_type']))\n\"",
  "description": "Check model_classification.csv format and counts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "a3c336b8-66e0-4385-8085-4206e16ea16f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5V5MWmPQn1uWnMS5gKycY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1700,
      "cache_read_input_tokens": 41231,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1700
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

_source line 118 · 2026-05-23T01:31:37.815Z_

<details><summary>↩ Tool result · `toolu_01TcAfcumRZ25HbS9vdRDb6J`</summary>

```text
model_name,model_type,cohort_temporal,family
01-ai/Yi-1.5-34B,base,2024,yi-1.5
01-ai/Yi-1.5-34B-32K,base,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat,instruct,2024,yi-1.5
01-ai/Yi-1.5-34B-Chat-16K,instruct,2024,yi-1.5
---
Columns: ['model_name', 'model_type', 'cohort_temporal', 'family']

model_type       base  instruct
cohort_temporal                
2023              861       219
2024              548       259
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "ea56f383-667e-4a8b-86f4-e93c15ac9b7d",
  "tool_use_result": {
    "stdout": "model_name,model_type,cohort_temporal,family\n01-ai/Yi-1.5-34B,base,2024,yi-1.5\n01-ai/Yi-1.5-34B-32K,base,2024,yi-1.5\n01-ai/Yi-1.5-34B-Chat,instruct,2024,yi-1.5\n01-ai/Yi-1.5-34B-Chat-16K,instruct,2024,yi-1.5\n---\nColumns: ['model_name', 'model_type', 'cohort_temporal', 'family']\n\nmodel_type       base  instruct\ncohort_temporal                \n2023              861       219\n2024              548       259",
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

Now I have all the pieces. Let me create the output directory and write the mixed-mechanism experiment script.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "8b32d086-5f08-4636-8e0b-ec9f1b8563c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MieyBaTvVAhp4Rz6mxgEYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 42931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1580
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

_source line 120_

<details open><summary>🔧 Tool call — Bash · `toolu_0164nMSZrg1gmLBNFhSf3GTf`</summary>

```json
{
  "command": "mkdir -p /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic",
  "description": "Create output directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "3f312e64-9d2f-4b0c-bcf7-f9b927af1400",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MieyBaTvVAhp4Rz6mxgEYy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1580,
      "cache_read_input_tokens": 42931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1580
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

_source line 121 · 2026-05-23T01:31:42.866Z_

<details><summary>↩ Tool result · `toolu_0164nMSZrg1gmLBNFhSf3GTf`</summary>

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
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "d7917cd0-e238-482e-a497-91d8ea5cc197",
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

_source line 122_

<details open><summary>🔧 Tool call — Write · `toolu_015SbxDqcci9kY78wc9YPCiA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_semisynthetic.py",
  "content": "\"\"\"\nMixed-mechanism semi-synthetic injection: difficulty × model_type.\nScheme D: base=difficulty-dependent, instruct=uniform\nScheme E: base=uniform, instruct=difficulty-dependent\n\"\"\"\n\nimport re\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"mixed_mechanism_semisynthetic\")\n\nN_SEEDS = 20\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MODEL CLASSIFICATION (from R18)\n# ════════════════════════════════════════════════════════════════════════════\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)([-_\\.]|$)\", re.IGNORECASE)\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\", re.IGNORECASE)\nFAMILY_PREFIX_EXCLUDE = re.compile(r\"^(openchat|chatglm|chatml)\", re.IGNORECASE)\n\ndef classify_model(name: str) -> str:\n    short = name.split(\"/\")[-1] if \"/\" in name else name\n    stripped = QUANT_SUFFIXES.sub(\"\", short)\n    if stripped.lower().endswith(\"-it\"):\n        return \"instruct\"\n    if INSTRUCT_SUFFIXES.search(stripped):\n        prefix_part = stripped.split(\"-\")[0].split(\"_\")[0]\n        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):\n            rest = stripped[len(prefix_part):]\n            if not INSTRUCT_SUFFIXES.search(rest):\n                return \"base\"\n        return \"instruct\"\n    return \"base\"\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1), 0\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30), 0)\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION FUNCTIONS\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_difficulty_dependent(X_foc, model_mask, item_idx, item_diff, rng):\n    \"\"\"Contamination-like: injection prob ∝ (1 - item_accuracy), hard items more likely.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    models = np.where(model_mask)[0]\n    for j in item_idx:\n        p_inject = max(0.0, min(1.0, (1.0 - item_diff[j] - 0.2) / 0.6))\n        for i in models:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_uniform(X_foc, model_mask, item_idx, rng, p_const=0.5):\n    \"\"\"Uniform injection probability p=0.5.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    models = np.where(model_mask)[0]\n    for j in item_idx:\n        for i in models:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_mixed(X_foc, base_foc_mask, instruct_foc_mask,\n                 inject_model_mask_base, inject_model_mask_instruct,\n                 inject_item_idx, item_diff, rng,\n                 base_scheme='difficulty', instruct_scheme='uniform'):\n    \"\"\"\n    Mixed injection: different schemes for base vs instruct focal models.\n    base_scheme/instruct_scheme: 'difficulty' or 'uniform'\n    \"\"\"\n    X = X_foc.copy()\n    n_flipped_base = 0\n    n_flipped_instruct = 0\n\n    base_models = np.where(inject_model_mask_base)[0]\n    instruct_models = np.where(inject_model_mask_instruct)[0]\n\n    for j in inject_item_idx:\n        p_diff = max(0.0, min(1.0, (1.0 - item_diff[j] - 0.2) / 0.6))\n        p_unif = 0.5\n\n        p_base = p_diff if base_scheme == 'difficulty' else p_unif\n        p_inst = p_diff if instruct_scheme == 'difficulty' else p_unif\n\n        for i in base_models:\n            if X[i, j] == 0 and rng.random() < p_base:\n                X[i, j] = 1\n                n_flipped_base += 1\n\n        for i in instruct_models:\n            if X[i, j] == 0 and rng.random() < p_inst:\n                X[i, j] = 1\n                n_flipped_instruct += 1\n\n    return X, n_flipped_base, n_flipped_instruct\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\n# Classify focal models as base/instruct\nfoc_model_names = np.array([model_names[i] for i in foc_idx])\nfoc_model_types = np.array([classify_model(n) for n in foc_model_names])\nfoc_base_mask = (foc_model_types == 'base')\nfoc_instruct_mask = (foc_model_types == 'instruct')\n\nN_foc_base = foc_base_mask.sum()\nN_foc_instruct = foc_instruct_mask.sum()\nN_inject_base = int(N_foc_base * FOC_INJECT_FRAC)\nN_inject_instruct = int(N_foc_instruct * FOC_INJECT_FRAC)\n\n# Classify ref models\nref_model_names = np.array([model_names[i] for i in ref_idx])\nref_model_types = np.array([classify_model(n) for n in ref_model_names])\nref_base_mask = (ref_model_types == 'base')\nref_instruct_mask = (ref_model_types == 'instruct')\n\nN_ref_base = ref_base_mask.sum()\nN_ref_instruct = ref_instruct_mask.sum()\n\nprint(f\"  Ref: {N_ref} (base={N_ref_base}, instruct={N_ref_instruct})\")\nprint(f\"  Foc: {N_foc} (base={N_foc_base}, instruct={N_foc_instruct})\")\nprint(f\"  Items: {J}\")\nprint(f\"  Injection: {N_inject_base} base models, {N_inject_instruct} instruct models, {N_inject_items} items\")\n\n# Densify submatrices\nX_ref_base_all = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base_all = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Submatrices by model type (for type-specific DIF)\nX_ref_base_type = X_ref_base_all[ref_base_mask]\nX_ref_instruct_type = X_ref_base_all[ref_instruct_mask]\nX_foc_base_type = X_foc_base_all[foc_base_mask]\nX_foc_instruct_type = X_foc_base_all[foc_instruct_mask]\n\nitem_difficulty = X_ref_base_all.mean(axis=0)\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline ===\")\n\ndelta_base_all, pval_base_all, is_c_base_all = mh_dif_vec(X_ref_base_all, X_foc_base_all)\ndelta_base_b, pval_base_b, is_c_base_b = mh_dif_vec(X_ref_base_type, X_foc_base_type)\ndelta_base_i, pval_base_i, is_c_base_i = mh_dif_vec(X_ref_instruct_type, X_foc_instruct_type)\n\nc_all = is_c_base_all.sum()\nc_b = is_c_base_b.sum()\nc_i = is_c_base_i.sum()\n\nrho_base_all, _ = stats.spearmanr(item_difficulty[is_c_base_all], delta_base_all[is_c_base_all])\nrho_base_b, _ = stats.spearmanr(item_difficulty[is_c_base_b], delta_base_b[is_c_base_b]) if c_b >= 3 else (np.nan, None)\nrho_base_i, _ = stats.spearmanr(item_difficulty[is_c_base_i], delta_base_i[is_c_base_i]) if c_i >= 3 else (np.nan, None)\n\npct_focal_base_all = (is_c_base_all & (delta_base_all > 0)).sum() / c_all * 100\npct_focal_base_b = (is_c_base_b & (delta_base_b > 0)).sum() / c_b * 100 if c_b > 0 else 0\npct_focal_base_i = (is_c_base_i & (delta_base_i > 0)).sum() / c_i * 100 if c_i > 0 else 0\n\nprint(f\"  Overall: C%={c_all/J*100:.1f}%, ρ={rho_base_all:.3f}, focal%={pct_focal_base_all:.1f}%\")\nprint(f\"  Base-only: C%={c_b/J*100:.1f}%, ρ={rho_base_b:.3f}, focal%={pct_focal_base_b:.1f}%\")\nprint(f\"  Instruct-only: C%={c_i/J*100:.1f}%, ρ={rho_base_i:.3f}, focal%={pct_focal_base_i:.1f}%\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DIRECTION REVERSAL χ² (helper)\n# ════════════════════════════════════════════════════════════════════════════\ndef direction_reversal_chi2(is_c_base, delta_base, is_c_inst, delta_inst):\n    \"\"\"χ² for difference in focal-favoring proportion between base and instruct DIF-C items.\"\"\"\n    n_c_b = is_c_base.sum()\n    n_c_i = is_c_inst.sum()\n    if n_c_b == 0 or n_c_i == 0:\n        return 0.0, 1.0\n\n    n_focal_b = (is_c_base & (delta_base > 0)).sum()\n    n_ref_b = n_c_b - n_focal_b\n    n_focal_i = (is_c_inst & (delta_inst > 0)).sum()\n    n_ref_i = n_c_i - n_focal_i\n\n    table = np.array([[n_focal_b, n_ref_b], [n_focal_i, n_ref_i]])\n    if table.min() == 0:\n        return 0.0, 1.0\n    chi2_val, p_val, _, _ = stats.chi2_contingency(table, correction=True)\n    return chi2_val, p_val\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running mixed-mechanism experiments ===\")\nresults = []\nt0 = time.time()\n\nschemes = {\n    'D_base_diff_instruct_unif': ('difficulty', 'uniform'),\n    'E_base_unif_instruct_diff': ('uniform', 'difficulty'),\n}\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection items (shared across schemes within seed)\n    inject_item_idx = rng.choice(J, N_inject_items, replace=False)\n\n    # Select injection models separately for base and instruct\n    base_foc_indices = np.where(foc_base_mask)[0]\n    instruct_foc_indices = np.where(foc_instruct_mask)[0]\n\n    inject_base_idx = rng.choice(base_foc_indices, N_inject_base, replace=False)\n    inject_instruct_idx = rng.choice(instruct_foc_indices, N_inject_instruct, replace=False)\n\n    inject_model_mask_base = np.zeros(N_foc, dtype=bool)\n    inject_model_mask_base[inject_base_idx] = True\n\n    inject_model_mask_instruct = np.zeros(N_foc, dtype=bool)\n    inject_model_mask_instruct[inject_instruct_idx] = True\n\n    for scheme_name, (base_scheme, instruct_scheme) in schemes.items():\n        t1 = time.time()\n\n        # Use a fresh RNG copy per scheme to avoid cross-contamination\n        rng_scheme = np.random.RandomState(seed * 42 + hash(scheme_name) % (2**31))\n\n        X_foc_inj, n_flipped_base, n_flipped_instruct = inject_mixed(\n            X_foc_base_all, foc_base_mask, foc_instruct_mask,\n            inject_model_mask_base, inject_model_mask_instruct,\n            inject_item_idx, item_difficulty, rng_scheme,\n            base_scheme=base_scheme, instruct_scheme=instruct_scheme)\n\n        n_flipped = n_flipped_base + n_flipped_instruct\n        injected_items = set(inject_item_idx)\n        inj_arr = np.array(sorted(injected_items))\n\n        # ── Overall MH-DIF ──\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base_all, X_foc_inj)\n        ddelta = delta_j - delta_base_all\n\n        c_pct_all = is_c.sum() / J * 100\n        n_c_total = is_c.sum()\n        c_idx = np.where(is_c)[0]\n        rho_all = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])[0] if len(c_idx) >= 3 else np.nan\n\n        n_focal_all = (is_c & (delta_j > 0)).sum()\n        pct_focal_all = n_focal_all / n_c_total * 100 if n_c_total > 0 else 0\n\n        rho_ddelta_inj = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Base-only MH-DIF ──\n        X_foc_inj_base = X_foc_inj[foc_base_mask]\n        delta_b, pval_b, is_c_b = mh_dif_vec(X_ref_base_type, X_foc_inj_base)\n        ddelta_b = delta_b - delta_base_b\n\n        c_pct_b = is_c_b.sum() / J * 100\n        n_c_b = is_c_b.sum()\n        c_idx_b = np.where(is_c_b)[0]\n        rho_base = stats.spearmanr(item_difficulty[c_idx_b], delta_b[c_idx_b])[0] if len(c_idx_b) >= 3 else np.nan\n\n        n_focal_b = (is_c_b & (delta_b > 0)).sum()\n        pct_focal_b = n_focal_b / n_c_b * 100 if n_c_b > 0 else 0\n\n        rho_ddelta_b = stats.spearmanr(item_difficulty[inj_arr], ddelta_b[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Instruct-only MH-DIF ──\n        X_foc_inj_instruct = X_foc_inj[foc_instruct_mask]\n        delta_i, pval_i, is_c_i = mh_dif_vec(X_ref_instruct_type, X_foc_inj_instruct)\n        ddelta_i = delta_i - delta_base_i\n\n        c_pct_i = is_c_i.sum() / J * 100\n        n_c_i = is_c_i.sum()\n        c_idx_i = np.where(is_c_i)[0]\n        rho_instruct = stats.spearmanr(item_difficulty[c_idx_i], delta_i[c_idx_i])[0] if len(c_idx_i) >= 3 else np.nan\n\n        n_focal_i = (is_c_i & (delta_i > 0)).sum()\n        pct_focal_i = n_focal_i / n_c_i * 100 if n_c_i > 0 else 0\n\n        rho_ddelta_i = stats.spearmanr(item_difficulty[inj_arr], ddelta_i[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Direction reversal χ² ──\n        chi2_rev, p_rev = direction_reversal_chi2(is_c_b, delta_b, is_c_i, delta_i)\n\n        elapsed = time.time() - t1\n\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_base=N_inject_base,\n            n_inject_instruct=N_inject_instruct,\n            n_inject_items=len(injected_items),\n            n_flipped_base=n_flipped_base,\n            n_flipped_instruct=n_flipped_instruct,\n            n_flipped_total=n_flipped,\n            # Overall\n            rho_overall=rho_all,\n            rho_ddelta_overall=rho_ddelta_inj,\n            c_pct_overall=c_pct_all,\n            n_c_overall=n_c_total,\n            pct_focal_overall=pct_focal_all,\n            # Base-only\n            rho_base=rho_base,\n            rho_ddelta_base=rho_ddelta_b,\n            c_pct_base=c_pct_b,\n            n_c_base=n_c_b,\n            pct_focal_base=pct_focal_b,\n            # Instruct-only\n            rho_instruct=rho_instruct,\n            rho_ddelta_instruct=rho_ddelta_i,\n            c_pct_instruct=c_pct_i,\n            n_c_instruct=n_c_i,\n            pct_focal_instruct=pct_focal_i,\n            # Direction reversal\n            chi2_reversal=chi2_rev,\n            p_reversal=p_rev,\n            elapsed_sec=elapsed,\n        )\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: \"\n              f\"ρ_all={rho_all:.3f}, ρ_base={rho_base:.3f}, ρ_inst={rho_instruct:.3f}, \"\n              f\"χ²={chi2_rev:.1f}, focal%: all={pct_focal_all:.1f}/base={pct_focal_b:.1f}/inst={pct_focal_i:.1f}, \"\n              f\"flips={n_flipped} ({n_flipped_base}B+{n_flipped_instruct}I), {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\nfor scheme_name in schemes:\n    sub = df[df['scheme'] == scheme_name]\n    fname = f\"scheme_{scheme_name[0].lower()}_results.csv\"\n    sub.to_csv(os.path.join(OUT, fname), index=False)\n    print(f\"Saved: {fname} ({len(sub)} rows)\")\n\ndf.to_csv(os.path.join(OUT, \"all_results.csv\"), index=False)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nobs = dict(rho_overall=-0.597, rho_base=-0.570, rho_instruct=-0.079, chi2=562.7)\n\nlines = [\"# Mixed-Mechanism Semi-Synthetic Injection\\n\"]\nlines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nlines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models ({N_ref_base} base, {N_ref_instruct} instruct), \"\n             f\"{N_foc} foc models ({N_foc_base} base, {N_foc_instruct} instruct), {J} items\\n\")\nlines.append(f\"**Injection**: 30% focal models per type ({N_inject_base} base, {N_inject_instruct} instruct), \"\n             f\"{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nlines.append(\"\\n## Observed Data (for comparison)\\n\")\nlines.append(f\"| Metric | Observed |\")\nlines.append(f\"|--------|----------|\")\nlines.append(f\"| ρ(difficulty, δ_MH) overall | {obs['rho_overall']:.3f} |\")\nlines.append(f\"| ρ(difficulty, δ_MH) base-only | {obs['rho_base']:.3f} |\")\nlines.append(f\"| ρ(difficulty, δ_MH) instruct-only | {obs['rho_instruct']:.3f} |\")\nlines.append(f\"| Direction reversal χ² | {obs['chi2']:.1f} |\")\n\nlines.append(\"\\n## Baseline (no injection)\\n\")\nlines.append(f\"| Metric | Overall | Base-only | Instruct-only |\")\nlines.append(f\"|--------|---------|-----------|---------------|\")\nlines.append(f\"| C% | {c_all/J*100:.1f}% | {is_c_base_b.sum()/J*100:.1f}% | {is_c_base_i.sum()/J*100:.1f}% |\")\nlines.append(f\"| ρ(diff, δ) | {rho_base_all:.3f} | {rho_base_b:.3f} | {rho_base_i:.3f} |\")\nlines.append(f\"| % focal-favoring | {pct_focal_base_all:.1f}% | {pct_focal_base_b:.1f}% | {pct_focal_base_i:.1f}% |\")\n\nfor scheme_name, (bs, ins) in schemes.items():\n    sub = df[df['scheme'] == scheme_name]\n    letter = scheme_name[0]\n    lines.append(f\"\\n## Scheme {letter} — base={bs}, instruct={ins}\\n\")\n\n    lines.append(f\"| Metric | Overall | Base-only | Instruct-only | Observed |\")\n    lines.append(f\"|--------|---------|-----------|---------------|----------|\")\n\n    def fmt(col):\n        return f\"{sub[col].mean():.3f} ± {sub[col].std():.3f}\"\n\n    lines.append(f\"| ρ(diff, δ_MH) among C items | {fmt('rho_overall')} | {fmt('rho_base')} | {fmt('rho_instruct')} | {obs['rho_overall']:.3f} / {obs['rho_base']:.3f} / {obs['rho_instruct']:.3f} |\")\n    lines.append(f\"| ρ(diff, Δδ) injected items | {fmt('rho_ddelta_overall')} | {fmt('rho_ddelta_base')} | {fmt('rho_ddelta_instruct')} | — |\")\n    lines.append(f\"| C% | {sub['c_pct_overall'].mean():.1f}±{sub['c_pct_overall'].std():.1f} | {sub['c_pct_base'].mean():.1f}±{sub['c_pct_base'].std():.1f} | {sub['c_pct_instruct'].mean():.1f}±{sub['c_pct_instruct'].std():.1f} | — |\")\n    lines.append(f\"| % focal-favoring | {sub['pct_focal_overall'].mean():.1f}±{sub['pct_focal_overall'].std():.1f} | {sub['pct_focal_base'].mean():.1f}±{sub['pct_focal_base'].std():.1f} | {sub['pct_focal_instruct'].mean():.1f}±{sub['pct_focal_instruct'].std():.1f} | — |\")\n    lines.append(f\"| Direction reversal χ² | {sub['chi2_reversal'].mean():.1f} ± {sub['chi2_reversal'].std():.1f} | — | — | {obs['chi2']:.1f} |\")\n    lines.append(f\"| N DIF-C | {sub['n_c_overall'].mean():.0f}±{sub['n_c_overall'].std():.0f} | {sub['n_c_base'].mean():.0f}±{sub['n_c_base'].std():.0f} | {sub['n_c_instruct'].mean():.0f}±{sub['n_c_instruct'].std():.0f} | — |\")\n    lines.append(f\"| Flips (base/instruct) | {sub['n_flipped_total'].mean():.0f} | {sub['n_flipped_base'].mean():.0f} | {sub['n_flipped_instruct'].mean():.0f} | — |\")\n\n# Comparison summary\nlines.append(f\"\\n## Comparison with Observed Data\\n\")\nlines.append(f\"| Metric | Observed | Scheme D | Scheme E |\")\nlines.append(f\"|--------|----------|----------|----------|\")\n\nd = df[df['scheme'] == 'D_base_diff_instruct_unif']\ne = df[df['scheme'] == 'E_base_unif_instruct_diff']\n\nfor metric, obs_val, col in [\n    ('ρ overall', obs['rho_overall'], 'rho_overall'),\n    ('ρ base', obs['rho_base'], 'rho_base'),\n    ('ρ instruct', obs['rho_instruct'], 'rho_instruct'),\n    ('χ² reversal', obs['chi2'], 'chi2_reversal'),\n]:\n    d_val = f\"{d[col].mean():.3f} ± {d[col].std():.3f}\"\n    e_val = f\"{e[col].mean():.3f} ± {e[col].std():.3f}\"\n    if col == 'chi2_reversal':\n        d_val = f\"{d[col].mean():.1f} ± {d[col].std():.1f}\"\n        e_val = f\"{e[col].mean():.1f} ± {e[col].std():.1f}\"\n    lines.append(f\"| {metric} | {obs_val} | {d_val} | {e_val} |\")\n\nlines.append(f\"\\n### Distance from observed (L2 on [ρ_overall, ρ_base, ρ_instruct])\\n\")\nobs_vec = np.array([obs['rho_overall'], obs['rho_base'], obs['rho_instruct']])\nd_vec = np.array([d['rho_overall'].mean(), d['rho_base'].mean(), d['rho_instruct'].mean()])\ne_vec = np.array([e['rho_overall'].mean(), e['rho_base'].mean(), e['rho_instruct'].mean()])\nd_dist = np.sqrt(((d_vec - obs_vec)**2).sum())\ne_dist = np.sqrt(((e_vec - obs_vec)**2).sum())\nlines.append(f\"- Scheme D: L2 = {d_dist:.3f}\")\nlines.append(f\"- Scheme E: L2 = {e_dist:.3f}\")\nwinner = \"D\" if d_dist < e_dist else \"E\"\nlines.append(f\"- **Scheme {winner} is closer to observed pattern**\")\n\nlines.append(f\"\\n### Key questions answered\\n\")\nlines.append(f\"1. **Can mixed mechanism reproduce overall ρ≈-0.6?**\")\nd_rho = d['rho_overall'].mean()\ne_rho = e['rho_overall'].mean()\nlines.append(f\"   - Scheme D: ρ={d_rho:.3f} → {'YES' if abs(d_rho - obs['rho_overall']) < 0.15 else 'NO'}\")\nlines.append(f\"   - Scheme E: ρ={e_rho:.3f} → {'YES' if abs(e_rho - obs['rho_overall']) < 0.15 else 'NO'}\")\n\nlines.append(f\"2. **Can mixed mechanism reproduce direction reversal (χ²>100)?**\")\nd_chi = d['chi2_reversal'].mean()\ne_chi = e['chi2_reversal'].mean()\nlines.append(f\"   - Scheme D: χ²={d_chi:.1f} → {'YES' if d_chi > 100 else 'NO'}\")\nlines.append(f\"   - Scheme E: χ²={e_chi:.1f} → {'YES' if e_chi > 100 else 'NO'}\")\n\nlines.append(f\"3. **Can mixed mechanism simultaneously reproduce BOTH?**\")\nd_both = abs(d_rho - obs['rho_overall']) < 0.15 and d_chi > 100\ne_both = abs(e_rho - obs['rho_overall']) < 0.15 and e_chi > 100\nlines.append(f\"   - Scheme D: {'YES' if d_both else 'NO'}\")\nlines.append(f\"   - Scheme E: {'YES' if e_both else 'NO'}\")\n\n# Also compare with R19 schemes\nlines.append(f\"\\n## Comparison with R19 Schemes (A/B/C)\\n\")\nlines.append(f\"| Scheme | ρ overall | ρ base | ρ instruct | χ² reversal | Mechanism |\")\nlines.append(f\"|--------|-----------|--------|------------|-------------|-----------|\")\nlines.append(f\"| A (R19) | — | — | — | — | capability: prob∝accuracy |\")\nlines.append(f\"| B (R19) | — | — | — | — | contamination: uniform p=0.5 |\")\nlines.append(f\"| C (R19) | — | — | — | — | mixed A+B items |\")\n\ndef fmt_mean_sd(s):\n    return f\"{s.mean():.3f}±{s.std():.3f}\"\n\nlines.append(f\"| **D** | {fmt_mean_sd(d['rho_overall'])} | {fmt_mean_sd(d['rho_base'])} | {fmt_mean_sd(d['rho_instruct'])} | {d['chi2_reversal'].mean():.1f}±{d['chi2_reversal'].std():.1f} | base=diff-dep, instruct=uniform |\")\nlines.append(f\"| **E** | {fmt_mean_sd(e['rho_overall'])} | {fmt_mean_sd(e['rho_base'])} | {fmt_mean_sd(e['rho_instruct'])} | {e['chi2_reversal'].mean():.1f}±{e['chi2_reversal'].std():.1f} | base=uniform, instruct=diff-dep |\")\nlines.append(f\"| **Observed** | {obs['rho_overall']:.3f} | {obs['rho_base']:.3f} | {obs['rho_instruct']:.3f} | {obs['chi2']:.1f} | ? |\")\n\nreport_text = \"\\n\".join(lines) + \"\\n\"\nwith open(os.path.join(OUT, \"mixed_mechanism_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"\\nSaved: mixed_mechanism_report.md\")\nprint(\"\\n\" + report_text)\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "c4bee243-7236-4e86-a04d-f40621d54e4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015s3cUVd5Hz8TSaGADKHRRu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 44511,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 53,
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

_source line 123 · 2026-05-23T01:33:51.673Z_

<details><summary>↩ Tool result · `toolu_015SbxDqcci9kY78wc9YPCiA`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_semisynthetic.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "80c9171d-ae4d-4f67-9b77-b8edd3db40d4",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_semisynthetic.py",
    "content": "\"\"\"\nMixed-mechanism semi-synthetic injection: difficulty × model_type.\nScheme D: base=difficulty-dependent, instruct=uniform\nScheme E: base=uniform, instruct=difficulty-dependent\n\"\"\"\n\nimport re\nimport numpy as np\nimport pandas as pd\nfrom scipy import sparse, stats\nfrom scipy.stats import chi2 as chi2_dist\nimport time, os\n\nROOT = \"/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts\"\nOUT = os.path.join(ROOT, \"mixed_mechanism_semisynthetic\")\n\nN_SEEDS = 20\nN_STRATA = 5\nFOC_INJECT_FRAC = 0.30\nITEM_INJECT_FRAC = 0.24\n\n# ════════════════════════════════════════════════════════════════════════════\n#  MODEL CLASSIFICATION (from R18)\n# ════════════════════════════════════════════════════════════════════════════\nINSTRUCT_SUFFIXES = re.compile(\n    r\"[-_\\.](instruct|chat|it|rlhf|dpo|sft|aligned|ppo)([-_\\.]|$)\", re.IGNORECASE)\nQUANT_SUFFIXES = re.compile(\n    r\"[-_\\.](gptq|awq|gguf|ggml|exl2|fp16|bf16|int[48]|q[2-8]_[0-9])\", re.IGNORECASE)\nFAMILY_PREFIX_EXCLUDE = re.compile(r\"^(openchat|chatglm|chatml)\", re.IGNORECASE)\n\ndef classify_model(name: str) -> str:\n    short = name.split(\"/\")[-1] if \"/\" in name else name\n    stripped = QUANT_SUFFIXES.sub(\"\", short)\n    if stripped.lower().endswith(\"-it\"):\n        return \"instruct\"\n    if INSTRUCT_SUFFIXES.search(stripped):\n        prefix_part = stripped.split(\"-\")[0].split(\"_\")[0]\n        if FAMILY_PREFIX_EXCLUDE.match(prefix_part):\n            rest = stripped[len(prefix_part):]\n            if not INSTRUCT_SUFFIXES.search(rest):\n                return \"base\"\n        return \"instruct\"\n    return \"base\"\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  VECTORIZED MH-DIF\n# ════════════════════════════════════════════════════════════════════════════\ndef mh_dif_vec(X_ref, X_foc, n_strata=N_STRATA):\n    n_ref, J = X_ref.shape\n    n_foc = X_foc.shape[0]\n\n    tot_ref = X_ref.sum(axis=1).astype(np.float64)\n    tot_foc = X_foc.sum(axis=1).astype(np.float64)\n    s_all = np.concatenate([tot_ref, tot_foc])\n\n    edges = np.unique(np.quantile(s_all, np.linspace(0, 1, n_strata + 1)))\n    n_bins = len(edges) - 1\n    if n_bins < 1:\n        return np.zeros(J), np.ones(J), np.zeros(J, dtype=bool)\n\n    k_ref = np.digitize(tot_ref, edges[1:-1])\n    k_foc = np.digitize(tot_foc, edges[1:-1])\n\n    n1 = np.zeros(n_bins, dtype=np.float64)\n    n0 = np.zeros(n_bins, dtype=np.float64)\n    A = np.zeros((n_bins, J), dtype=np.float64)\n    C_mat = np.zeros((n_bins, J), dtype=np.float64)\n\n    for k in range(n_bins):\n        mr = (k_ref == k)\n        mf = (k_foc == k)\n        n1[k] = mr.sum()\n        n0[k] = mf.sum()\n        if mr.any():\n            A[k] = X_ref[mr].sum(axis=0).astype(np.float64)\n        if mf.any():\n            C_mat[k] = X_foc[mf].sum(axis=0).astype(np.float64)\n\n    B = n1[:, None] - A\n    D = n0[:, None] - C_mat\n    Nk = (n1 + n0)[:, None]\n    m1 = A + C_mat\n    m0 = B + D\n\n    valid = ((n1[:, None] > 0) & (n0[:, None] > 0) &\n             (Nk > 1) & (m1 > 0) & (m0 > 0))\n\n    Rj = np.where(valid, A * D / Nk, 0).sum(axis=0)\n    Sj = np.where(valid, B * C_mat / Nk, 0).sum(axis=0)\n\n    finite_mask = (Rj > 0) & (Sj > 0)\n    with np.errstate(divide=\"ignore\", invalid=\"ignore\"):\n        delta_j = np.where(finite_mask, -2.35 * np.log(Rj / Sj), 0)\n\n    EA = np.where(valid, n1[:, None] * m1 / Nk, 0)\n    sum_diff = np.where(valid, A - EA, 0).sum(axis=0)\n    Nk_m1 = np.where(Nk > 1, Nk - 1, 1)\n    sum_var = np.where(\n        valid,\n        n1[:, None] * n0[:, None] * m1 * m0 / (Nk ** 2 * Nk_m1), 0\n    ).sum(axis=0)\n\n    chi2_j = np.where(\n        sum_var > 0,\n        np.maximum(np.abs(sum_diff) - 0.5, 0) ** 2 / np.maximum(sum_var, 1e-30), 0)\n    pval_j = np.where(sum_var > 0, 1 - chi2_dist.cdf(chi2_j, df=1), 1.0)\n\n    is_c = finite_mask & (np.abs(delta_j) >= 1.5) & (pval_j < 0.05)\n    return delta_j, pval_j, is_c\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  INJECTION FUNCTIONS\n# ════════════════════════════════════════════════════════════════════════════\ndef inject_difficulty_dependent(X_foc, model_mask, item_idx, item_diff, rng):\n    \"\"\"Contamination-like: injection prob ∝ (1 - item_accuracy), hard items more likely.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    models = np.where(model_mask)[0]\n    for j in item_idx:\n        p_inject = max(0.0, min(1.0, (1.0 - item_diff[j] - 0.2) / 0.6))\n        for i in models:\n            if X[i, j] == 0 and rng.random() < p_inject:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_uniform(X_foc, model_mask, item_idx, rng, p_const=0.5):\n    \"\"\"Uniform injection probability p=0.5.\"\"\"\n    X = X_foc.copy()\n    n_flipped = 0\n    models = np.where(model_mask)[0]\n    for j in item_idx:\n        for i in models:\n            if X[i, j] == 0 and rng.random() < p_const:\n                X[i, j] = 1\n                n_flipped += 1\n    return X, n_flipped\n\n\ndef inject_mixed(X_foc, base_foc_mask, instruct_foc_mask,\n                 inject_model_mask_base, inject_model_mask_instruct,\n                 inject_item_idx, item_diff, rng,\n                 base_scheme='difficulty', instruct_scheme='uniform'):\n    \"\"\"\n    Mixed injection: different schemes for base vs instruct focal models.\n    base_scheme/instruct_scheme: 'difficulty' or 'uniform'\n    \"\"\"\n    X = X_foc.copy()\n    n_flipped_base = 0\n    n_flipped_instruct = 0\n\n    base_models = np.where(inject_model_mask_base)[0]\n    instruct_models = np.where(inject_model_mask_instruct)[0]\n\n    for j in inject_item_idx:\n        p_diff = max(0.0, min(1.0, (1.0 - item_diff[j] - 0.2) / 0.6))\n        p_unif = 0.5\n\n        p_base = p_diff if base_scheme == 'difficulty' else p_unif\n        p_inst = p_diff if instruct_scheme == 'difficulty' else p_unif\n\n        for i in base_models:\n            if X[i, j] == 0 and rng.random() < p_base:\n                X[i, j] = 1\n                n_flipped_base += 1\n\n        for i in instruct_models:\n            if X[i, j] == 0 and rng.random() < p_inst:\n                X[i, j] = 1\n                n_flipped_instruct += 1\n\n    return X, n_flipped_base, n_flipped_instruct\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  LOAD DATA\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"Loading data...\")\nrm = np.load(f\"{ROOT}/response_matrix.npz\")\nX_sparse = sparse.csr_matrix((rm['data'], rm['indices'], rm['indptr']), shape=tuple(rm['shape']))\nidx = np.load(f\"{ROOT}/response_matrix_index.npz\", allow_pickle=True)\nmodel_names = idx['model_names']\nitem_ids = idx['item_ids']\n\nmeta = pd.read_csv(f\"{ROOT}/model_metadata.csv\")\nname_to_row = {n: i for i, n in enumerate(model_names)}\n\nref_models = meta[meta['cohort_temporal'] == '2023']['model_name'].values\nfoc_models = meta[meta['cohort_temporal'] == '2024']['model_name'].values\n\nref_idx = np.array([name_to_row[n] for n in ref_models if n in name_to_row])\nfoc_idx = np.array([name_to_row[n] for n in foc_models if n in name_to_row])\n\nN_ref, N_foc, J = len(ref_idx), len(foc_idx), len(item_ids)\nN_inject_items = int(J * ITEM_INJECT_FRAC)\n\n# Classify focal models as base/instruct\nfoc_model_names = np.array([model_names[i] for i in foc_idx])\nfoc_model_types = np.array([classify_model(n) for n in foc_model_names])\nfoc_base_mask = (foc_model_types == 'base')\nfoc_instruct_mask = (foc_model_types == 'instruct')\n\nN_foc_base = foc_base_mask.sum()\nN_foc_instruct = foc_instruct_mask.sum()\nN_inject_base = int(N_foc_base * FOC_INJECT_FRAC)\nN_inject_instruct = int(N_foc_instruct * FOC_INJECT_FRAC)\n\n# Classify ref models\nref_model_names = np.array([model_names[i] for i in ref_idx])\nref_model_types = np.array([classify_model(n) for n in ref_model_names])\nref_base_mask = (ref_model_types == 'base')\nref_instruct_mask = (ref_model_types == 'instruct')\n\nN_ref_base = ref_base_mask.sum()\nN_ref_instruct = ref_instruct_mask.sum()\n\nprint(f\"  Ref: {N_ref} (base={N_ref_base}, instruct={N_ref_instruct})\")\nprint(f\"  Foc: {N_foc} (base={N_foc_base}, instruct={N_foc_instruct})\")\nprint(f\"  Items: {J}\")\nprint(f\"  Injection: {N_inject_base} base models, {N_inject_instruct} instruct models, {N_inject_items} items\")\n\n# Densify submatrices\nX_ref_base_all = X_sparse[ref_idx].toarray().astype(np.float64)\nX_foc_base_all = X_sparse[foc_idx].toarray().astype(np.float64)\n\n# Submatrices by model type (for type-specific DIF)\nX_ref_base_type = X_ref_base_all[ref_base_mask]\nX_ref_instruct_type = X_ref_base_all[ref_instruct_mask]\nX_foc_base_type = X_foc_base_all[foc_base_mask]\nX_foc_instruct_type = X_foc_base_all[foc_instruct_mask]\n\nitem_difficulty = X_ref_base_all.mean(axis=0)\nprint(f\"  Item difficulty: mean={item_difficulty.mean():.3f}\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  BASELINE (no injection)\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Baseline ===\")\n\ndelta_base_all, pval_base_all, is_c_base_all = mh_dif_vec(X_ref_base_all, X_foc_base_all)\ndelta_base_b, pval_base_b, is_c_base_b = mh_dif_vec(X_ref_base_type, X_foc_base_type)\ndelta_base_i, pval_base_i, is_c_base_i = mh_dif_vec(X_ref_instruct_type, X_foc_instruct_type)\n\nc_all = is_c_base_all.sum()\nc_b = is_c_base_b.sum()\nc_i = is_c_base_i.sum()\n\nrho_base_all, _ = stats.spearmanr(item_difficulty[is_c_base_all], delta_base_all[is_c_base_all])\nrho_base_b, _ = stats.spearmanr(item_difficulty[is_c_base_b], delta_base_b[is_c_base_b]) if c_b >= 3 else (np.nan, None)\nrho_base_i, _ = stats.spearmanr(item_difficulty[is_c_base_i], delta_base_i[is_c_base_i]) if c_i >= 3 else (np.nan, None)\n\npct_focal_base_all = (is_c_base_all & (delta_base_all > 0)).sum() / c_all * 100\npct_focal_base_b = (is_c_base_b & (delta_base_b > 0)).sum() / c_b * 100 if c_b > 0 else 0\npct_focal_base_i = (is_c_base_i & (delta_base_i > 0)).sum() / c_i * 100 if c_i > 0 else 0\n\nprint(f\"  Overall: C%={c_all/J*100:.1f}%, ρ={rho_base_all:.3f}, focal%={pct_focal_base_all:.1f}%\")\nprint(f\"  Base-only: C%={c_b/J*100:.1f}%, ρ={rho_base_b:.3f}, focal%={pct_focal_base_b:.1f}%\")\nprint(f\"  Instruct-only: C%={c_i/J*100:.1f}%, ρ={rho_base_i:.3f}, focal%={pct_focal_base_i:.1f}%\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  DIRECTION REVERSAL χ² (helper)\n# ════════════════════════════════════════════════════════════════════════════\ndef direction_reversal_chi2(is_c_base, delta_base, is_c_inst, delta_inst):\n    \"\"\"χ² for difference in focal-favoring proportion between base and instruct DIF-C items.\"\"\"\n    n_c_b = is_c_base.sum()\n    n_c_i = is_c_inst.sum()\n    if n_c_b == 0 or n_c_i == 0:\n        return 0.0, 1.0\n\n    n_focal_b = (is_c_base & (delta_base > 0)).sum()\n    n_ref_b = n_c_b - n_focal_b\n    n_focal_i = (is_c_inst & (delta_inst > 0)).sum()\n    n_ref_i = n_c_i - n_focal_i\n\n    table = np.array([[n_focal_b, n_ref_b], [n_focal_i, n_ref_i]])\n    if table.min() == 0:\n        return 0.0, 1.0\n    chi2_val, p_val, _, _ = stats.chi2_contingency(table, correction=True)\n    return chi2_val, p_val\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  RUN EXPERIMENTS\n# ════════════════════════════════════════════════════════════════════════════\nprint(\"\\n=== Running mixed-mechanism experiments ===\")\nresults = []\nt0 = time.time()\n\nschemes = {\n    'D_base_diff_instruct_unif': ('difficulty', 'uniform'),\n    'E_base_unif_instruct_diff': ('uniform', 'difficulty'),\n}\n\nfor seed in range(1, N_SEEDS + 1):\n    rng = np.random.RandomState(seed * 42)\n\n    # Select injection items (shared across schemes within seed)\n    inject_item_idx = rng.choice(J, N_inject_items, replace=False)\n\n    # Select injection models separately for base and instruct\n    base_foc_indices = np.where(foc_base_mask)[0]\n    instruct_foc_indices = np.where(foc_instruct_mask)[0]\n\n    inject_base_idx = rng.choice(base_foc_indices, N_inject_base, replace=False)\n    inject_instruct_idx = rng.choice(instruct_foc_indices, N_inject_instruct, replace=False)\n\n    inject_model_mask_base = np.zeros(N_foc, dtype=bool)\n    inject_model_mask_base[inject_base_idx] = True\n\n    inject_model_mask_instruct = np.zeros(N_foc, dtype=bool)\n    inject_model_mask_instruct[inject_instruct_idx] = True\n\n    for scheme_name, (base_scheme, instruct_scheme) in schemes.items():\n        t1 = time.time()\n\n        # Use a fresh RNG copy per scheme to avoid cross-contamination\n        rng_scheme = np.random.RandomState(seed * 42 + hash(scheme_name) % (2**31))\n\n        X_foc_inj, n_flipped_base, n_flipped_instruct = inject_mixed(\n            X_foc_base_all, foc_base_mask, foc_instruct_mask,\n            inject_model_mask_base, inject_model_mask_instruct,\n            inject_item_idx, item_difficulty, rng_scheme,\n            base_scheme=base_scheme, instruct_scheme=instruct_scheme)\n\n        n_flipped = n_flipped_base + n_flipped_instruct\n        injected_items = set(inject_item_idx)\n        inj_arr = np.array(sorted(injected_items))\n\n        # ── Overall MH-DIF ──\n        delta_j, pval_j, is_c = mh_dif_vec(X_ref_base_all, X_foc_inj)\n        ddelta = delta_j - delta_base_all\n\n        c_pct_all = is_c.sum() / J * 100\n        n_c_total = is_c.sum()\n        c_idx = np.where(is_c)[0]\n        rho_all = stats.spearmanr(item_difficulty[c_idx], delta_j[c_idx])[0] if len(c_idx) >= 3 else np.nan\n\n        n_focal_all = (is_c & (delta_j > 0)).sum()\n        pct_focal_all = n_focal_all / n_c_total * 100 if n_c_total > 0 else 0\n\n        rho_ddelta_inj = stats.spearmanr(item_difficulty[inj_arr], ddelta[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Base-only MH-DIF ──\n        X_foc_inj_base = X_foc_inj[foc_base_mask]\n        delta_b, pval_b, is_c_b = mh_dif_vec(X_ref_base_type, X_foc_inj_base)\n        ddelta_b = delta_b - delta_base_b\n\n        c_pct_b = is_c_b.sum() / J * 100\n        n_c_b = is_c_b.sum()\n        c_idx_b = np.where(is_c_b)[0]\n        rho_base = stats.spearmanr(item_difficulty[c_idx_b], delta_b[c_idx_b])[0] if len(c_idx_b) >= 3 else np.nan\n\n        n_focal_b = (is_c_b & (delta_b > 0)).sum()\n        pct_focal_b = n_focal_b / n_c_b * 100 if n_c_b > 0 else 0\n\n        rho_ddelta_b = stats.spearmanr(item_difficulty[inj_arr], ddelta_b[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Instruct-only MH-DIF ──\n        X_foc_inj_instruct = X_foc_inj[foc_instruct_mask]\n        delta_i, pval_i, is_c_i = mh_dif_vec(X_ref_instruct_type, X_foc_inj_instruct)\n        ddelta_i = delta_i - delta_base_i\n\n        c_pct_i = is_c_i.sum() / J * 100\n        n_c_i = is_c_i.sum()\n        c_idx_i = np.where(is_c_i)[0]\n        rho_instruct = stats.spearmanr(item_difficulty[c_idx_i], delta_i[c_idx_i])[0] if len(c_idx_i) >= 3 else np.nan\n\n        n_focal_i = (is_c_i & (delta_i > 0)).sum()\n        pct_focal_i = n_focal_i / n_c_i * 100 if n_c_i > 0 else 0\n\n        rho_ddelta_i = stats.spearmanr(item_difficulty[inj_arr], ddelta_i[inj_arr])[0] if len(inj_arr) >= 3 else np.nan\n\n        # ── Direction reversal χ² ──\n        chi2_rev, p_rev = direction_reversal_chi2(is_c_b, delta_b, is_c_i, delta_i)\n\n        elapsed = time.time() - t1\n\n        row = dict(\n            scheme=scheme_name, seed=seed,\n            n_inject_base=N_inject_base,\n            n_inject_instruct=N_inject_instruct,\n            n_inject_items=len(injected_items),\n            n_flipped_base=n_flipped_base,\n            n_flipped_instruct=n_flipped_instruct,\n            n_flipped_total=n_flipped,\n            # Overall\n            rho_overall=rho_all,\n            rho_ddelta_overall=rho_ddelta_inj,\n            c_pct_overall=c_pct_all,\n            n_c_overall=n_c_total,\n            pct_focal_overall=pct_focal_all,\n            # Base-only\n            rho_base=rho_base,\n            rho_ddelta_base=rho_ddelta_b,\n            c_pct_base=c_pct_b,\n            n_c_base=n_c_b,\n            pct_focal_base=pct_focal_b,\n            # Instruct-only\n            rho_instruct=rho_instruct,\n            rho_ddelta_instruct=rho_ddelta_i,\n            c_pct_instruct=c_pct_i,\n            n_c_instruct=n_c_i,\n            pct_focal_instruct=pct_focal_i,\n            # Direction reversal\n            chi2_reversal=chi2_rev,\n            p_reversal=p_rev,\n            elapsed_sec=elapsed,\n        )\n        results.append(row)\n        print(f\"  [{scheme_name}] seed={seed}: \"\n              f\"ρ_all={rho_all:.3f}, ρ_base={rho_base:.3f}, ρ_inst={rho_instruct:.3f}, \"\n              f\"χ²={chi2_rev:.1f}, focal%: all={pct_focal_all:.1f}/base={pct_focal_b:.1f}/inst={pct_focal_i:.1f}, \"\n              f\"flips={n_flipped} ({n_flipped_base}B+{n_flipped_instruct}I), {elapsed:.1f}s\")\n\ntotal_time = time.time() - t0\nprint(f\"\\nTotal time: {total_time:.0f}s\")\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  SAVE RESULTS\n# ════════════════════════════════════════════════════════════════════════════\ndf = pd.DataFrame(results)\nfor scheme_name in schemes:\n    sub = df[df['scheme'] == scheme_name]\n    fname = f\"scheme_{scheme_name[0].lower()}_results.csv\"\n    sub.to_csv(os.path.join(OUT, fname), index=False)\n    print(f\"Saved: {fname} ({len(sub)} rows)\")\n\ndf.to_csv(os.path.join(OUT, \"all_results.csv\"), index=False)\n\n\n# ════════════════════════════════════════════════════════════════════════════\n#  GENERATE REPORT\n# ════════════════════════════════════════════════════════════════════════════\nobs = dict(rho_overall=-0.597, rho_base=-0.570, rho_instruct=-0.079, chi2=562.7)\n\nlines = [\"# Mixed-Mechanism Semi-Synthetic Injection\\n\"]\nlines.append(f\"**Date**: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}\\n\")\nlines.append(f\"**Config**: {N_SEEDS} seeds, {N_ref} ref models ({N_ref_base} base, {N_ref_instruct} instruct), \"\n             f\"{N_foc} foc models ({N_foc_base} base, {N_foc_instruct} instruct), {J} items\\n\")\nlines.append(f\"**Injection**: 30% focal models per type ({N_inject_base} base, {N_inject_instruct} instruct), \"\n             f\"{N_inject_items} items ({ITEM_INJECT_FRAC*100:.0f}%)\\n\")\n\nlines.append(\"\\n## Observed Data (for comparison)\\n\")\nlines.append(f\"| Metric | Observed |\")\nlines.append(f\"|--------|----------|\")\nlines.append(f\"| ρ(difficulty, δ_MH) overall | {obs['rho_overall']:.3f} |\")\nlines.append(f\"| ρ(difficulty, δ_MH) base-only | {obs['rho_base']:.3f} |\")\nlines.append(f\"| ρ(difficulty, δ_MH) instruct-only | {obs['rho_instruct']:.3f} |\")\nlines.append(f\"| Direction reversal χ² | {obs['chi2']:.1f} |\")\n\nlines.append(\"\\n## Baseline (no injection)\\n\")\nlines.append(f\"| Metric | Overall | Base-only | Instruct-only |\")\nlines.append(f\"|--------|---------|-----------|---------------|\")\nlines.append(f\"| C% | {c_all/J*100:.1f}% | {is_c_base_b.sum()/J*100:.1f}% | {is_c_base_i.sum()/J*100:.1f}% |\")\nlines.append(f\"| ρ(diff, δ) | {rho_base_all:.3f} | {rho_base_b:.3f} | {rho_base_i:.3f} |\")\nlines.append(f\"| % focal-favoring | {pct_focal_base_all:.1f}% | {pct_focal_base_b:.1f}% | {pct_focal_base_i:.1f}% |\")\n\nfor scheme_name, (bs, ins) in schemes.items():\n    sub = df[df['scheme'] == scheme_name]\n    letter = scheme_name[0]\n    lines.append(f\"\\n## Scheme {letter} — base={bs}, instruct={ins}\\n\")\n\n    lines.append(f\"| Metric | Overall | Base-only | Instruct-only | Observed |\")\n    lines.append(f\"|--------|---------|-----------|---------------|----------|\")\n\n    def fmt(col):\n        return f\"{sub[col].mean():.3f} ± {sub[col].std():.3f}\"\n\n    lines.append(f\"| ρ(diff, δ_MH) among C items | {fmt('rho_overall')} | {fmt('rho_base')} | {fmt('rho_instruct')} | {obs['rho_overall']:.3f} / {obs['rho_base']:.3f} / {obs['rho_instruct']:.3f} |\")\n    lines.append(f\"| ρ(diff, Δδ) injected items | {fmt('rho_ddelta_overall')} | {fmt('rho_ddelta_base')} | {fmt('rho_ddelta_instruct')} | — |\")\n    lines.append(f\"| C% | {sub['c_pct_overall'].mean():.1f}±{sub['c_pct_overall'].std():.1f} | {sub['c_pct_base'].mean():.1f}±{sub['c_pct_base'].std():.1f} | {sub['c_pct_instruct'].mean():.1f}±{sub['c_pct_instruct'].std():.1f} | — |\")\n    lines.append(f\"| % focal-favoring | {sub['pct_focal_overall'].mean():.1f}±{sub['pct_focal_overall'].std():.1f} | {sub['pct_focal_base'].mean():.1f}±{sub['pct_focal_base'].std():.1f} | {sub['pct_focal_instruct'].mean():.1f}±{sub['pct_focal_instruct'].std():.1f} | — |\")\n    lines.append(f\"| Direction reversal χ² | {sub['chi2_reversal'].mean():.1f} ± {sub['chi2_reversal'].std():.1f} | — | — | {obs['chi2']:.1f} |\")\n    lines.append(f\"| N DIF-C | {sub['n_c_overall'].mean():.0f}±{sub['n_c_overall'].std():.0f} | {sub['n_c_base'].mean():.0f}±{sub['n_c_base'].std():.0f} | {sub['n_c_instruct'].mean():.0f}±{sub['n_c_instruct'].std():.0f} | — |\")\n    lines.append(f\"| Flips (base/instruct) | {sub['n_flipped_total'].mean():.0f} | {sub['n_flipped_base'].mean():.0f} | {sub['n_flipped_instruct'].mean():.0f} | — |\")\n\n# Comparison summary\nlines.append(f\"\\n## Comparison with Observed Data\\n\")\nlines.append(f\"| Metric | Observed | Scheme D | Scheme E |\")\nlines.append(f\"|--------|----------|----------|----------|\")\n\nd = df[df['scheme'] == 'D_base_diff_instruct_unif']\ne = df[df['scheme'] == 'E_base_unif_instruct_diff']\n\nfor metric, obs_val, col in [\n    ('ρ overall', obs['rho_overall'], 'rho_overall'),\n    ('ρ base', obs['rho_base'], 'rho_base'),\n    ('ρ instruct', obs['rho_instruct'], 'rho_instruct'),\n    ('χ² reversal', obs['chi2'], 'chi2_reversal'),\n]:\n    d_val = f\"{d[col].mean():.3f} ± {d[col].std():.3f}\"\n    e_val = f\"{e[col].mean():.3f} ± {e[col].std():.3f}\"\n    if col == 'chi2_reversal':\n        d_val = f\"{d[col].mean():.1f} ± {d[col].std():.1f}\"\n        e_val = f\"{e[col].mean():.1f} ± {e[col].std():.1f}\"\n    lines.append(f\"| {metric} | {obs_val} | {d_val} | {e_val} |\")\n\nlines.append(f\"\\n### Distance from observed (L2 on [ρ_overall, ρ_base, ρ_instruct])\\n\")\nobs_vec = np.array([obs['rho_overall'], obs['rho_base'], obs['rho_instruct']])\nd_vec = np.array([d['rho_overall'].mean(), d['rho_base'].mean(), d['rho_instruct'].mean()])\ne_vec = np.array([e['rho_overall'].mean(), e['rho_base'].mean(), e['rho_instruct'].mean()])\nd_dist = np.sqrt(((d_vec - obs_vec)**2).sum())\ne_dist = np.sqrt(((e_vec - obs_vec)**2).sum())\nlines.append(f\"- Scheme D: L2 = {d_dist:.3f}\")\nlines.append(f\"- Scheme E: L2 = {e_dist:.3f}\")\nwinner = \"D\" if d_dist < e_dist else \"E\"\nlines.append(f\"- **Scheme {winner} is closer to observed pattern**\")\n\nlines.append(f\"\\n### Key questions answered\\n\")\nlines.append(f\"1. **Can mixed mechanism reproduce overall ρ≈-0.6?**\")\nd_rho = d['rho_overall'].mean()\ne_rho = e['rho_overall'].mean()\nlines.append(f\"   - Scheme D: ρ={d_rho:.3f} → {'YES' if abs(d_rho - obs['rho_overall']) < 0.15 else 'NO'}\")\nlines.append(f\"   - Scheme E: ρ={e_rho:.3f} → {'YES' if abs(e_rho - obs['rho_overall']) < 0.15 else 'NO'}\")\n\nlines.append(f\"2. **Can mixed mechanism reproduce direction reversal (χ²>100)?**\")\nd_chi = d['chi2_reversal'].mean()\ne_chi = e['chi2_reversal'].mean()\nlines.append(f\"   - Scheme D: χ²={d_chi:.1f} → {'YES' if d_chi > 100 else 'NO'}\")\nlines.append(f\"   - Scheme E: χ²={e_chi:.1f} → {'YES' if e_chi > 100 else 'NO'}\")\n\nlines.append(f\"3. **Can mixed mechanism simultaneously reproduce BOTH?**\")\nd_both = abs(d_rho - obs['rho_overall']) < 0.15 and d_chi > 100\ne_both = abs(e_rho - obs['rho_overall']) < 0.15 and e_chi > 100\nlines.append(f\"   - Scheme D: {'YES' if d_both else 'NO'}\")\nlines.append(f\"   - Scheme E: {'YES' if e_both else 'NO'}\")\n\n# Also compare with R19 schemes\nlines.append(f\"\\n## Comparison with R19 Schemes (A/B/C)\\n\")\nlines.append(f\"| Scheme | ρ overall | ρ base | ρ instruct | χ² reversal | Mechanism |\")\nlines.append(f\"|--------|-----------|--------|------------|-------------|-----------|\")\nlines.append(f\"| A (R19) | — | — | — | — | capability: prob∝accuracy |\")\nlines.append(f\"| B (R19) | — | — | — | — | contamination: uniform p=0.5 |\")\nlines.append(f\"| C (R19) | — | — | — | — | mixed A+B items |\")\n\ndef fmt_mean_sd(s):\n    return f\"{s.mean():.3f}±{s.std():.3f}\"\n\nlines.append(f\"| **D** | {fmt_mean_sd(d['rho_overall'])} | {fmt_mean_sd(d['rho_base'])} | {fmt_mean_sd(d['rho_instruct'])} | {d['chi2_reversal'].mean():.1f}±{d['chi2_reversal'].std():.1f} | base=diff-dep, instruct=uniform |\")\nlines.append(f\"| **E** | {fmt_mean_sd(e['rho_overall'])} | {fmt_mean_sd(e['rho_base'])} | {fmt_mean_sd(e['rho_instruct'])} | {e['chi2_reversal'].mean():.1f}±{e['chi2_reversal'].std():.1f} | base=uniform, instruct=diff-dep |\")\nlines.append(f\"| **Observed** | {obs['rho_overall']:.3f} | {obs['rho_base']:.3f} | {obs['rho_instruct']:.3f} | {obs['chi2']:.1f} | ? |\")\n\nreport_text = \"\\n\".join(lines) + \"\\n\"\nwith open(os.path.join(OUT, \"mixed_mechanism_report.md\"), \"w\") as f:\n    f.write(report_text)\n\nprint(f\"\\nSaved: mixed_mechanism_report.md\")\nprint(\"\\n\" + report_text)\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 124_

Running the experiment. The inner loops are O(items × models) with 20 seeds × 2 schemes, so it will take some time.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "5fc88252-0492-40f6-8ad4-f8f6f651b0dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcreuB1WvKj7a5dmPZ1pX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10484,
      "cache_read_input_tokens": 44668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10484
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

_source line 125_

<details open><summary>🔧 Tool call — Bash · `toolu_01HjvAbHmjFGMymBScucC82T`</summary>

```json
{
  "command": "python3 artifacts/mixed_mechanism_semisynthetic/mixed_mechanism_semisynthetic.py 2>&1",
  "description": "Run mixed-mechanism semi-synthetic experiment (20 seeds × 2 schemes)",
  "timeout": 600000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "ca2428ad-4e8b-4833-a1be-305798465c9a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NVcreuB1WvKj7a5dmPZ1pX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10484,
      "cache_read_input_tokens": 44668,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10484
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

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "be4bxnd84",
  "tool_use_id": "toolu_01HjvAbHmjFGMymBScucC82T",
  "description": "Run mixed-mechanism semi-synthetic experiment (20 seeds × 2 schemes)",
  "task_type": "local_bash",
  "uuid": "1ece6dec-0393-48e8-b926-bb110084bce5",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### System

_source line 127_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "be4bxnd84",
  "tool_use_id": "toolu_01HjvAbHmjFGMymBScucC82T",
  "status": "completed",
  "output_file": "",
  "summary": "Run mixed-mechanism semi-synthetic experiment (20 seeds × 2 schemes)",
  "uuid": "791d80d8-f82e-4541-b5fa-84776955ba18",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74"
}
```

---

### Tool result

_source line 128 · 2026-05-23T01:35:03.525Z_

<details><summary>↩ Tool result · `toolu_01HjvAbHmjFGMymBScucC82T`</summary>

```text
Loading data...
  Ref: 1080 (base=861, instruct=219)
  Foc: 807 (base=548, instruct=259)
  Items: 12508
  Injection: 164 base models, 77 instruct models, 3001 items
  Item difficulty: mean=0.581

=== Baseline ===
  Overall: C%=31.3%, ρ=-0.587, focal%=43.9%
  Base-only: C%=32.1%, ρ=-0.570, focal%=39.9%
  Instruct-only: C%=36.5%, ρ=-0.079, focal%=65.6%

=== Running mixed-mechanism experiments ===
  [D_base_diff_instruct_unif] seed=1: ρ_all=-0.674, ρ_base=-0.636, ρ_inst=-0.279, χ²=727.0, focal%: all=43.9/base=38.0/inst=65.8, flips=164069 (121757B+42312I), 1.2s
  [E_base_unif_instruct_diff] seed=1: ρ_all=-0.664, ρ_base=-0.624, ρ_inst=-0.410, χ²=392.0, focal%: all=46.2/base=41.3/inst=62.1, flips=154086 (98906B+55180I), 1.3s
  [D_base_diff_instruct_unif] seed=2: ρ_all=-0.677, ρ_base=-0.633, ρ_inst=-0.360, χ²=622.4, focal%: all=45.1/base=38.0/inst=64.0, flips=167444 (122355B+45089I), 1.2s
  [E_base_unif_instruct_diff] seed=2: ρ_all=-0.668, ρ_base=-0.625, ρ_inst=-0.496, χ²=283.2, focal%: all=46.5/base=41.3/inst=59.1, flips=152321 (95039B+57282I), 1.2s
  [D_base_diff_instruct_unif] seed=3: ρ_all=-0.674, ρ_base=-0.628, ρ_inst=-0.391, χ²=445.2, focal%: all=43.5/base=39.6/inst=61.6, flips=172258 (127411B+44847I), 1.9s
  [E_base_unif_instruct_diff] seed=3: ρ_all=-0.667, ρ_base=-0.614, ρ_inst=-0.503, χ²=211.9, focal%: all=44.2/base=43.0/inst=58.5, flips=159042 (100071B+58971I), 1.7s
  [D_base_diff_instruct_unif] seed=4: ρ_all=-0.681, ρ_base=-0.637, ρ_inst=-0.363, χ²=660.6, focal%: all=41.0/base=36.9/inst=63.0, flips=170782 (125098B+45684I), 1.8s
  [E_base_unif_instruct_diff] seed=4: ρ_all=-0.679, ρ_base=-0.631, ρ_inst=-0.450, χ²=398.9, focal%: all=42.5/base=40.9/inst=61.6, flips=157843 (99606B+58237I), 1.8s
  [D_base_diff_instruct_unif] seed=5: ρ_all=-0.673, ρ_base=-0.639, ρ_inst=-0.191, χ²=874.3, focal%: all=43.4/base=37.2/inst=67.6, flips=167494 (123615B+43879I), 1.4s
  [E_base_unif_instruct_diff] seed=5: ρ_all=-0.661, ρ_base=-0.634, ρ_inst=-0.332, χ²=538.9, focal%: all=46.5/base=40.9/inst=65.2, flips=157213 (100250B+56963I), 1.2s
  [D_base_diff_instruct_unif] seed=6: ρ_all=-0.680, ρ_base=-0.641, ρ_inst=-0.288, χ²=690.6, focal%: all=42.2/base=38.7/inst=66.0, flips=169819 (123590B+46229I), 1.3s
  [E_base_unif_instruct_diff] seed=6: ρ_all=-0.675, ρ_base=-0.629, ρ_inst=-0.441, χ²=380.5, focal%: all=43.6/base=42.4/inst=63.1, flips=155401 (96424B+58977I), 1.2s
  [D_base_diff_instruct_unif] seed=7: ρ_all=-0.672, ρ_base=-0.637, ρ_inst=-0.237, χ²=632.4, focal%: all=43.8/base=39.0/inst=65.1, flips=165659 (122231B+43428I), 1.3s
  [E_base_unif_instruct_diff] seed=7: ρ_all=-0.667, ρ_base=-0.626, ρ_inst=-0.374, χ²=357.1, focal%: all=44.6/base=42.4/inst=62.3, flips=151283 (95002B+56281I), 1.3s
  [D_base_diff_instruct_unif] seed=8: ρ_all=-0.682, ρ_base=-0.638, ρ_inst=-0.247, χ²=860.7, focal%: all=42.1/base=35.8/inst=65.5, flips=170264 (127044B+43220I), 1.2s
  [E_base_unif_instruct_diff] seed=8: ρ_all=-0.676, ρ_base=-0.639, ρ_inst=-0.365, χ²=532.2, focal%: all=43.7/base=38.7/inst=62.6, flips=157650 (99381B+58269I), 1.4s
  [D_base_diff_instruct_unif] seed=9: ρ_all=-0.666, ρ_base=-0.630, ρ_inst=-0.218, χ²=851.0, focal%: all=45.8/base=37.8/inst=67.8, flips=164523 (119393B+45130I), 1.9s
  [E_base_unif_instruct_diff] seed=9: ρ_all=-0.654, ρ_base=-0.622, ρ_inst=-0.389, χ²=471.3, focal%: all=47.3/base=41.2/inst=63.9, flips=149703 (95079B+54624I), 1.8s
  [D_base_diff_instruct_unif] seed=10: ρ_all=-0.671, ρ_base=-0.639, ρ_inst=-0.382, χ²=393.6, focal%: all=44.6/base=40.1/inst=60.6, flips=165316 (121908B+43408I), 1.9s
  [E_base_unif_instruct_diff] seed=10: ρ_all=-0.660, ρ_base=-0.624, ρ_inst=-0.450, χ²=299.4, focal%: all=47.6/base=42.7/inst=60.9, flips=152425 (95965B+56460I), 1.8s
  [D_base_diff_instruct_unif] seed=11: ρ_all=-0.679, ρ_base=-0.639, ρ_inst=-0.335, χ²=596.7, focal%: all=44.3/base=38.2/inst=63.4, flips=170641 (126463B+44178I), 1.9s
  [E_base_unif_instruct_diff] seed=11: ρ_all=-0.667, ρ_base=-0.624, ρ_inst=-0.413, χ²=400.4, focal%: all=46.4/base=42.2/inst=63.3, flips=157610 (98778B+58832I), 1.7s
  [D_base_diff_instruct_unif] seed=12: ρ_all=-0.679, ρ_base=-0.653, ρ_inst=-0.133, χ²=930.1, focal%: all=42.4/base=38.9/inst=70.0, flips=171551 (126768B+44783I), 1.5s
  [E_base_unif_instruct_diff] seed=12: ρ_all=-0.670, ρ_base=-0.635, ρ_inst=-0.268, χ²=629.9, focal%: all=44.9/base=41.9/inst=68.1, flips=161636 (103889B+57747I), 1.2s
  [D_base_diff_instruct_unif] seed=13: ρ_all=-0.677, ρ_base=-0.641, ρ_inst=-0.340, χ²=497.8, focal%: all=44.6/base=39.5/inst=62.6, flips=168465 (123042B+45423I), 1.3s
  [E_base_unif_instruct_diff] seed=13: ρ_all=-0.665, ρ_base=-0.630, ρ_inst=-0.443, χ²=258.7, focal%: all=46.3/base=43.2/inst=60.2, flips=155103 (98915B+56188I), 1.2s
  [D_base_diff_instruct_unif] seed=14: ρ_all=-0.666, ρ_base=-0.623, ρ_inst=-0.493, χ²=447.4, focal%: all=42.1/base=36.5/inst=58.2, flips=166570 (124340B+42230I), 1.2s
  [E_base_unif_instruct_diff] seed=14: ρ_all=-0.669, ρ_base=-0.628, ρ_inst=-0.575, χ²=227.6, focal%: all=44.3/base=40.1/inst=55.7, flips=152966 (97359B+55607I), 1.2s
  [D_base_diff_instruct_unif] seed=15: ρ_all=-0.680, ρ_base=-0.644, ρ_inst=-0.222, χ²=885.5, focal%: all=44.7/base=38.8/inst=69.5, flips=165680 (119556B+46124I), 1.2s
  [E_base_unif_instruct_diff] seed=15: ρ_all=-0.671, ρ_base=-0.632, ρ_inst=-0.411, χ²=455.7, focal%: all=47.1/base=42.4/inst=64.8, flips=154117 (98086B+56031I), 1.2s
  [D_base_diff_instruct_unif] seed=16: ρ_all=-0.675, ρ_base=-0.641, ρ_inst=-0.438, χ²=340.0, focal%: all=44.5/base=40.3/inst=59.6, flips=169605 (123849B+45756I), 1.2s
  [E_base_unif_instruct_diff] seed=16: ρ_all=-0.666, ρ_base=-0.612, ρ_inst=-0.512, χ²=174.1, focal%: all=45.7/base=43.8/inst=57.8, flips=159820 (101894B+57926I), 1.2s
  [D_base_diff_instruct_unif] seed=17: ρ_all=-0.682, ρ_base=-0.652, ρ_inst=-0.247, χ²=622.9, focal%: all=43.4/base=40.1/inst=66.1, flips=165066 (122934B+42132I), 1.3s
  [E_base_unif_instruct_diff] seed=17: ρ_all=-0.673, ρ_base=-0.631, ρ_inst=-0.358, χ²=324.5, focal%: all=46.0/base=43.7/inst=62.8, flips=156522 (100910B+55612I), 1.2s
  [D_base_diff_instruct_unif] seed=18: ρ_all=-0.676, ρ_base=-0.640, ρ_inst=-0.374, χ²=349.8, focal%: all=43.1/base=40.6/inst=60.1, flips=164296 (121973B+42323I), 1.2s
  [E_base_unif_instruct_diff] seed=18: ρ_all=-0.668, ρ_base=-0.619, ρ_inst=-0.415, χ²=232.1, focal%: all=44.7/base=44.1/inst=60.3, flips=151624 (95073B+56551I), 1.2s
  [D_base_diff_instruct_unif] seed=19: ρ_all=-0.676, ρ_base=-0.637, ρ_inst=-0.241, χ²=689.8, focal%: all=42.6/base=38.1/inst=65.6, flips=167625 (126692B+40933I), 1.2s
  [E_base_unif_instruct_diff] seed=19: ρ_all=-0.668, ρ_base=-0.620, ρ_inst=-0.360, χ²=392.4, focal%: all=45.0/base=41.5/inst=62.5, flips=155975 (99045B+56930I), 1.2s
  [D_base_diff_instruct_unif] seed=20: ρ_all=-0.676, ρ_base=-0.640, ρ_inst=-0.262, χ²=570.7, focal%: all=42.9/base=39.9/inst=64.6, flips=170685 (125450B+45235I), 1.2s
  [E_base_unif_instruct_diff] seed=20: ρ_all=-0.671, ρ_base=-0.626, ρ_inst=-0.392, χ²=296.9, focal%: all=45.3/base=43.3/inst=61.5, flips=158539 (100302B+58237I), 1.3s

Total time: 56s
Saved: scheme_d_results.csv (20 rows)
Saved: scheme_e_results.csv (20 rows)

Saved: mixed_mechanism_report.md

# Mixed-Mechanism Semi-Synthetic Injection

**Date**: 2026-05-23 01:35

**Config**: 20 seeds, 1080 ref models (861 base, 219 instruct), 807 foc models (548 base, 259 instruct), 12508 items

**Injection**: 30% focal models per type (164 base, 77 instruct), 3001 items (24%)


## Observed Data (for comparison)

| Metric | Observed |
|--------|----------|
| ρ(difficulty, δ_MH) overall | -0.597 |
| ρ(difficulty, δ_MH) base-only | -0.570 |
| ρ(difficulty, δ_MH) instruct-only | -0.079 |
| Direction reversal χ² | 562.7 |

## Baseline (no injection)

| Metric | Overall | Base-only | Instruct-only |
|--------|---------|-----------|---------------|
| C% | 31.3% | 32.1% | 36.5% |
| ρ(diff, δ) | -0.587 | -0.570 | -0.079 |
| % focal-favoring | 43.9% | 39.9% | 65.6% |

## Scheme D — base=difficulty, instruct=uniform

| Metric | Overall | Base-only | Instruct-only | Observed |
|--------|---------|-----------|---------------|----------|
| ρ(diff, δ_MH) among C items | -0.676 ± 0.005 | -0.638 ± 0.007 | -0.302 ± 0.090 | -0.597 / -0.570 / -0.079 |
| ρ(diff, Δδ) injected items | -0.897 ± 0.018 | -0.875 ± 0.026 | -0.670 ± 0.111 | — |
| C% | 35.3±1.0 | 37.4±1.3 | 37.5±0.7 | — |
| % focal-favoring | 43.5±1.2 | 38.6±1.3 | 64.3±3.2 | — |
| Direction reversal χ² | 634.4 ± 183.9 | — | — | 562.7 |
| N DIF-C | 4416±127 | 4677±169 | 4692±83 | — |
| Flips (base/instruct) | 167891 | 123773 | 44117 | — |

## Scheme E — base=uniform, instruct=difficulty

| Metric | Overall | Base-only | Instruct-only | Observed |
|--------|---------|-----------|---------------|----------|
| ρ(diff, δ_MH) among C items | -0.668 ± 0.006 | -0.626 ± 0.007 | -0.418 ± 0.070 | -0.597 / -0.570 / -0.079 |
| ρ(diff, Δδ) injected items | -0.743 ± 0.058 | -0.448 ± 0.097 | -0.894 ± 0.027 | — |
| C% | 34.1±0.9 | 34.0±1.0 | 38.5±0.6 | — |
| % focal-favoring | 45.4±1.4 | 42.1±1.3 | 61.8±2.8 | — |
| Direction reversal χ² | 362.9 ± 120.7 | — | — | 562.7 |
| N DIF-C | 4268±118 | 4249±128 | 4814±72 | — |
| Flips (base/instruct) | 155544 | 98499 | 57045 | — |

## Comparison with Observed Data

| Metric | Observed | Scheme D | Scheme E |
|--------|----------|----------|----------|
| ρ overall | -0.597 | -0.676 ± 0.005 | -0.668 ± 0.006 |
| ρ base | -0.57 | -0.638 ± 0.007 | -0.626 ± 0.007 |
| ρ instruct | -0.079 | -0.302 ± 0.090 | -0.418 ± 0.070 |
| χ² reversal | 562.7 | 634.4 ± 183.9 | 362.9 ± 120.7 |

### Distance from observed (L2 on [ρ_overall, ρ_base, ρ_instruct])

- Scheme D: L2 = 0.246
- Scheme E: L2 = 0.351
- **Scheme D is closer to observed pattern**

### Key questions answered

1. **Can mixed mechanism reproduce overall ρ≈-0.6?**
   - Scheme D: ρ=-0.676 → YES
   - Scheme E: ρ=-0.668 → YES
2. **Can mixed mechanism reproduce direction reversal (χ²>100)?**
   - Scheme D: χ²=634.4 → YES
   - Scheme E: χ²=362.9 → YES
3. **Can mixed mechanism simultaneously reproduce BOTH?**
   - Scheme D: YES
   - Scheme E: YES

## Comparison with R19 Schemes (A/B/C)

| Scheme | ρ overall | ρ base | ρ instruct | χ² reversal | Mechanism |
|--------|-----------|--------|------------|-------------|-----------|
| A (R19) | — | — | — | — | capability: prob∝accuracy |
| B (R19) | — | — | — | — | contamination: uniform p=0.5 |
| C (R19) | — | — | — | — | mixed A+B items |
| **D** | -0.676±0.005 | -0.638±0.007 | -0.302±0.090 | 634.4±183.9 | base=diff-dep, instruct=uniform |
| **E** | -0.668±0.006 | -0.626±0.007 | -0.418±0.070 | 362.9±120.7 | base=uniform, instruct=diff-dep |
| **Observed** | -0.597 | -0.570 | -0.079 | 562.7 | ? |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "7dcef96e-dda2-4bc2-8656-5125f278ec25",
  "tool_use_result": {
    "stdout": "Loading data...\n  Ref: 1080 (base=861, instruct=219)\n  Foc: 807 (base=548, instruct=259)\n  Items: 12508\n  Injection: 164 base models, 77 instruct models, 3001 items\n  Item difficulty: mean=0.581\n\n=== Baseline ===\n  Overall: C%=31.3%, ρ=-0.587, focal%=43.9%\n  Base-only: C%=32.1%, ρ=-0.570, focal%=39.9%\n  Instruct-only: C%=36.5%, ρ=-0.079, focal%=65.6%\n\n=== Running mixed-mechanism experiments ===\n  [D_base_diff_instruct_unif] seed=1: ρ_all=-0.674, ρ_base=-0.636, ρ_inst=-0.279, χ²=727.0, focal%: all=43.9/base=38.0/inst=65.8, flips=164069 (121757B+42312I), 1.2s\n  [E_base_unif_instruct_diff] seed=1: ρ_all=-0.664, ρ_base=-0.624, ρ_inst=-0.410, χ²=392.0, focal%: all=46.2/base=41.3/inst=62.1, flips=154086 (98906B+55180I), 1.3s\n  [D_base_diff_instruct_unif] seed=2: ρ_all=-0.677, ρ_base=-0.633, ρ_inst=-0.360, χ²=622.4, focal%: all=45.1/base=38.0/inst=64.0, flips=167444 (122355B+45089I), 1.2s\n  [E_base_unif_instruct_diff] seed=2: ρ_all=-0.668, ρ_base=-0.625, ρ_inst=-0.496, χ²=283.2, focal%: all=46.5/base=41.3/inst=59.1, flips=152321 (95039B+57282I), 1.2s\n  [D_base_diff_instruct_unif] seed=3: ρ_all=-0.674, ρ_base=-0.628, ρ_inst=-0.391, χ²=445.2, focal%: all=43.5/base=39.6/inst=61.6, flips=172258 (127411B+44847I), 1.9s\n  [E_base_unif_instruct_diff] seed=3: ρ_all=-0.667, ρ_base=-0.614, ρ_inst=-0.503, χ²=211.9, focal%: all=44.2/base=43.0/inst=58.5, flips=159042 (100071B+58971I), 1.7s\n  [D_base_diff_instruct_unif] seed=4: ρ_all=-0.681, ρ_base=-0.637, ρ_inst=-0.363, χ²=660.6, focal%: all=41.0/base=36.9/inst=63.0, flips=170782 (125098B+45684I), 1.8s\n  [E_base_unif_instruct_diff] seed=4: ρ_all=-0.679, ρ_base=-0.631, ρ_inst=-0.450, χ²=398.9, focal%: all=42.5/base=40.9/inst=61.6, flips=157843 (99606B+58237I), 1.8s\n  [D_base_diff_instruct_unif] seed=5: ρ_all=-0.673, ρ_base=-0.639, ρ_inst=-0.191, χ²=874.3, focal%: all=43.4/base=37.2/inst=67.6, flips=167494 (123615B+43879I), 1.4s\n  [E_base_unif_instruct_diff] seed=5: ρ_all=-0.661, ρ_base=-0.634, ρ_inst=-0.332, χ²=538.9, focal%: all=46.5/base=40.9/inst=65.2, flips=157213 (100250B+56963I), 1.2s\n  [D_base_diff_instruct_unif] seed=6: ρ_all=-0.680, ρ_base=-0.641, ρ_inst=-0.288, χ²=690.6, focal%: all=42.2/base=38.7/inst=66.0, flips=169819 (123590B+46229I), 1.3s\n  [E_base_unif_instruct_diff] seed=6: ρ_all=-0.675, ρ_base=-0.629, ρ_inst=-0.441, χ²=380.5, focal%: all=43.6/base=42.4/inst=63.1, flips=155401 (96424B+58977I), 1.2s\n  [D_base_diff_instruct_unif] seed=7: ρ_all=-0.672, ρ_base=-0.637, ρ_inst=-0.237, χ²=632.4, focal%: all=43.8/base=39.0/inst=65.1, flips=165659 (122231B+43428I), 1.3s\n  [E_base_unif_instruct_diff] seed=7: ρ_all=-0.667, ρ_base=-0.626, ρ_inst=-0.374, χ²=357.1, focal%: all=44.6/base=42.4/inst=62.3, flips=151283 (95002B+56281I), 1.3s\n  [D_base_diff_instruct_unif] seed=8: ρ_all=-0.682, ρ_base=-0.638, ρ_inst=-0.247, χ²=860.7, focal%: all=42.1/base=35.8/inst=65.5, flips=170264 (127044B+43220I), 1.2s\n  [E_base_unif_instruct_diff] seed=8: ρ_all=-0.676, ρ_base=-0.639, ρ_inst=-0.365, χ²=532.2, focal%: all=43.7/base=38.7/inst=62.6, flips=157650 (99381B+58269I), 1.4s\n  [D_base_diff_instruct_unif] seed=9: ρ_all=-0.666, ρ_base=-0.630, ρ_inst=-0.218, χ²=851.0, focal%: all=45.8/base=37.8/inst=67.8, flips=164523 (119393B+45130I), 1.9s\n  [E_base_unif_instruct_diff] seed=9: ρ_all=-0.654, ρ_base=-0.622, ρ_inst=-0.389, χ²=471.3, focal%: all=47.3/base=41.2/inst=63.9, flips=149703 (95079B+54624I), 1.8s\n  [D_base_diff_instruct_unif] seed=10: ρ_all=-0.671, ρ_base=-0.639, ρ_inst=-0.382, χ²=393.6, focal%: all=44.6/base=40.1/inst=60.6, flips=165316 (121908B+43408I), 1.9s\n  [E_base_unif_instruct_diff] seed=10: ρ_all=-0.660, ρ_base=-0.624, ρ_inst=-0.450, χ²=299.4, focal%: all=47.6/base=42.7/inst=60.9, flips=152425 (95965B+56460I), 1.8s\n  [D_base_diff_instruct_unif] seed=11: ρ_all=-0.679, ρ_base=-0.639, ρ_inst=-0.335, χ²=596.7, focal%: all=44.3/base=38.2/inst=63.4, flips=170641 (126463B+44178I), 1.9s\n  [E_base_unif_instruct_diff] seed=11: ρ_all=-0.667, ρ_base=-0.624, ρ_inst=-0.413, χ²=400.4, focal%: all=46.4/base=42.2/inst=63.3, flips=157610 (98778B+58832I), 1.7s\n  [D_base_diff_instruct_unif] seed=12: ρ_all=-0.679, ρ_base=-0.653, ρ_inst=-0.133, χ²=930.1, focal%: all=42.4/base=38.9/inst=70.0, flips=171551 (126768B+44783I), 1.5s\n  [E_base_unif_instruct_diff] seed=12: ρ_all=-0.670, ρ_base=-0.635, ρ_inst=-0.268, χ²=629.9, focal%: all=44.9/base=41.9/inst=68.1, flips=161636 (103889B+57747I), 1.2s\n  [D_base_diff_instruct_unif] seed=13: ρ_all=-0.677, ρ_base=-0.641, ρ_inst=-0.340, χ²=497.8, focal%: all=44.6/base=39.5/inst=62.6, flips=168465 (123042B+45423I), 1.3s\n  [E_base_unif_instruct_diff] seed=13: ρ_all=-0.665, ρ_base=-0.630, ρ_inst=-0.443, χ²=258.7, focal%: all=46.3/base=43.2/inst=60.2, flips=155103 (98915B+56188I), 1.2s\n  [D_base_diff_instruct_unif] seed=14: ρ_all=-0.666, ρ_base=-0.623, ρ_inst=-0.493, χ²=447.4, focal%: all=42.1/base=36.5/inst=58.2, flips=166570 (124340B+42230I), 1.2s\n  [E_base_unif_instruct_diff] seed=14: ρ_all=-0.669, ρ_base=-0.628, ρ_inst=-0.575, χ²=227.6, focal%: all=44.3/base=40.1/inst=55.7, flips=152966 (97359B+55607I), 1.2s\n  [D_base_diff_instruct_unif] seed=15: ρ_all=-0.680, ρ_base=-0.644, ρ_inst=-0.222, χ²=885.5, focal%: all=44.7/base=38.8/inst=69.5, flips=165680 (119556B+46124I), 1.2s\n  [E_base_unif_instruct_diff] seed=15: ρ_all=-0.671, ρ_base=-0.632, ρ_inst=-0.411, χ²=455.7, focal%: all=47.1/base=42.4/inst=64.8, flips=154117 (98086B+56031I), 1.2s\n  [D_base_diff_instruct_unif] seed=16: ρ_all=-0.675, ρ_base=-0.641, ρ_inst=-0.438, χ²=340.0, focal%: all=44.5/base=40.3/inst=59.6, flips=169605 (123849B+45756I), 1.2s\n  [E_base_unif_instruct_diff] seed=16: ρ_all=-0.666, ρ_base=-0.612, ρ_inst=-0.512, χ²=174.1, focal%: all=45.7/base=43.8/inst=57.8, flips=159820 (101894B+57926I), 1.2s\n  [D_base_diff_instruct_unif] seed=17: ρ_all=-0.682, ρ_base=-0.652, ρ_inst=-0.247, χ²=622.9, focal%: all=43.4/base=40.1/inst=66.1, flips=165066 (122934B+42132I), 1.3s\n  [E_base_unif_instruct_diff] seed=17: ρ_all=-0.673, ρ_base=-0.631, ρ_inst=-0.358, χ²=324.5, focal%: all=46.0/base=43.7/inst=62.8, flips=156522 (100910B+55612I), 1.2s\n  [D_base_diff_instruct_unif] seed=18: ρ_all=-0.676, ρ_base=-0.640, ρ_inst=-0.374, χ²=349.8, focal%: all=43.1/base=40.6/inst=60.1, flips=164296 (121973B+42323I), 1.2s\n  [E_base_unif_instruct_diff] seed=18: ρ_all=-0.668, ρ_base=-0.619, ρ_inst=-0.415, χ²=232.1, focal%: all=44.7/base=44.1/inst=60.3, flips=151624 (95073B+56551I), 1.2s\n  [D_base_diff_instruct_unif] seed=19: ρ_all=-0.676, ρ_base=-0.637, ρ_inst=-0.241, χ²=689.8, focal%: all=42.6/base=38.1/inst=65.6, flips=167625 (126692B+40933I), 1.2s\n  [E_base_unif_instruct_diff] seed=19: ρ_all=-0.668, ρ_base=-0.620, ρ_inst=-0.360, χ²=392.4, focal%: all=45.0/base=41.5/inst=62.5, flips=155975 (99045B+56930I), 1.2s\n  [D_base_diff_instruct_unif] seed=20: ρ_all=-0.676, ρ_base=-0.640, ρ_inst=-0.262, χ²=570.7, focal%: all=42.9/base=39.9/inst=64.6, flips=170685 (125450B+45235I), 1.2s\n  [E_base_unif_instruct_diff] seed=20: ρ_all=-0.671, ρ_base=-0.626, ρ_inst=-0.392, χ²=296.9, focal%: all=45.3/base=43.3/inst=61.5, flips=158539 (100302B+58237I), 1.3s\n\nTotal time: 56s\nSaved: scheme_d_results.csv (20 rows)\nSaved: scheme_e_results.csv (20 rows)\n\nSaved: mixed_mechanism_report.md\n\n# Mixed-Mechanism Semi-Synthetic Injection\n\n**Date**: 2026-05-23 01:35\n\n**Config**: 20 seeds, 1080 ref models (861 base, 219 instruct), 807 foc models (548 base, 259 instruct), 12508 items\n\n**Injection**: 30% focal models per type (164 base, 77 instruct), 3001 items (24%)\n\n\n## Observed Data (for comparison)\n\n| Metric | Observed |\n|--------|----------|\n| ρ(difficulty, δ_MH) overall | -0.597 |\n| ρ(difficulty, δ_MH) base-only | -0.570 |\n| ρ(difficulty, δ_MH) instruct-only | -0.079 |\n| Direction reversal χ² | 562.7 |\n\n## Baseline (no injection)\n\n| Metric | Overall | Base-only | Instruct-only |\n|--------|---------|-----------|---------------|\n| C% | 31.3% | 32.1% | 36.5% |\n| ρ(diff, δ) | -0.587 | -0.570 | -0.079 |\n| % focal-favoring | 43.9% | 39.9% | 65.6% |\n\n## Scheme D — base=difficulty, instruct=uniform\n\n| Metric | Overall | Base-only | Instruct-only | Observed |\n|--------|---------|-----------|---------------|----------|\n| ρ(diff, δ_MH) among C items | -0.676 ± 0.005 | -0.638 ± 0.007 | -0.302 ± 0.090 | -0.597 / -0.570 / -0.079 |\n| ρ(diff, Δδ) injected items | -0.897 ± 0.018 | -0.875 ± 0.026 | -0.670 ± 0.111 | — |\n| C% | 35.3±1.0 | 37.4±1.3 | 37.5±0.7 | — |\n| % focal-favoring | 43.5±1.2 | 38.6±1.3 | 64.3±3.2 | — |\n| Direction reversal χ² | 634.4 ± 183.9 | — | — | 562.7 |\n| N DIF-C | 4416±127 | 4677±169 | 4692±83 | — |\n| Flips (base/instruct) | 167891 | 123773 | 44117 | — |\n\n## Scheme E — base=uniform, instruct=difficulty\n\n| Metric | Overall | Base-only | Instruct-only | Observed |\n|--------|---------|-----------|---------------|----------|\n| ρ(diff, δ_MH) among C items | -0.668 ± 0.006 | -0.626 ± 0.007 | -0.418 ± 0.070 | -0.597 / -0.570 / -0.079 |\n| ρ(diff, Δδ) injected items | -0.743 ± 0.058 | -0.448 ± 0.097 | -0.894 ± 0.027 | — |\n| C% | 34.1±0.9 | 34.0±1.0 | 38.5±0.6 | — |\n| % focal-favoring | 45.4±1.4 | 42.1±1.3 | 61.8±2.8 | — |\n| Direction reversal χ² | 362.9 ± 120.7 | — | — | 562.7 |\n| N DIF-C | 4268±118 | 4249±128 | 4814±72 | — |\n| Flips (base/instruct) | 155544 | 98499 | 57045 | — |\n\n## Comparison with Observed Data\n\n| Metric | Observed | Scheme D | Scheme E |\n|--------|----------|----------|----------|\n| ρ overall | -0.597 | -0.676 ± 0.005 | -0.668 ± 0.006 |\n| ρ base | -0.57 | -0.638 ± 0.007 | -0.626 ± 0.007 |\n| ρ instruct | -0.079 | -0.302 ± 0.090 | -0.418 ± 0.070 |\n| χ² reversal | 562.7 | 634.4 ± 183.9 | 362.9 ± 120.7 |\n\n### Distance from observed (L2 on [ρ_overall, ρ_base, ρ_instruct])\n\n- Scheme D: L2 = 0.246\n- Scheme E: L2 = 0.351\n- **Scheme D is closer to observed pattern**\n\n### Key questions answered\n\n1. **Can mixed mechanism reproduce overall ρ≈-0.6?**\n   - Scheme D: ρ=-0.676 → YES\n   - Scheme E: ρ=-0.668 → YES\n2. **Can mixed mechanism reproduce direction reversal (χ²>100)?**\n   - Scheme D: χ²=634.4 → YES\n   - Scheme E: χ²=362.9 → YES\n3. **Can mixed mechanism simultaneously reproduce BOTH?**\n   - Scheme D: YES\n   - Scheme E: YES\n\n## Comparison with R19 Schemes (A/B/C)\n\n| Scheme | ρ overall | ρ base | ρ instruct | χ² reversal | Mechanism |\n|--------|-----------|--------|------------|-------------|-----------|\n| A (R19) | — | — | — | — | capability: prob∝accuracy |\n| B (R19) | — | — | — | — | contamination: uniform p=0.5 |\n| C (R19) | — | — | — | — | mixed A+B items |\n| **D** | -0.676±0.005 | -0.638±0.007 | -0.302±0.090 | 634.4±183.9 | base=diff-dep, instruct=uniform |\n| **E** | -0.668±0.006 | -0.626±0.007 | -0.418±0.070 | 362.9±120.7 | base=uniform, instruct=diff-dep |\n| **Observed** | -0.597 | -0.570 | -0.079 | 562.7 | ? |",
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

_source line 129_

实验完成。验证输出文件已正确生成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "c67edff6-f8bd-477f-bb0d-3d38d6c9c5ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uyvjv54QRFhphHdoyY9GRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6035,
      "cache_read_input_tokens": 55152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6035
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

_source line 130_

<details open><summary>🔧 Tool call — Bash · `toolu_01QLjzsu867U1CJ3kFdgYW75`</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/mixed_mechanism_semisynthetic/",
  "description": "Verify output files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "6372f5e5-e94e-491e-b09e-5194880fb0e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uyvjv54QRFhphHdoyY9GRQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6035,
      "cache_read_input_tokens": 55152,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6035
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

_source line 131 · 2026-05-23T01:35:08.428Z_

<details><summary>↩ Tool result · `toolu_01QLjzsu867U1CJ3kFdgYW75`</summary>

```text
total 72
drwxr-xr-x  2 ubuntu ubuntu  4096 May 23 01:35 .
drwxr-xr-x 93 ubuntu ubuntu  4096 May 23 01:31 ..
-rw-r--r--  1 ubuntu ubuntu 14919 May 23 01:35 all_results.csv
-rw-r--r--  1 ubuntu ubuntu  3662 May 23 01:35 mixed_mechanism_report.md
-rw-r--r--  1 ubuntu ubuntu 27480 May 23 01:33 mixed_mechanism_semisynthetic.py
-rw-r--r--  1 ubuntu ubuntu  7634 May 23 01:35 scheme_d_results.csv
-rw-r--r--  1 ubuntu ubuntu  7646 May 23 01:35 scheme_e_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "656cf0e8-a6ee-4f27-a184-800761f2a7da",
  "tool_use_result": {
    "stdout": "total 72\ndrwxr-xr-x  2 ubuntu ubuntu  4096 May 23 01:35 .\ndrwxr-xr-x 93 ubuntu ubuntu  4096 May 23 01:31 ..\n-rw-r--r--  1 ubuntu ubuntu 14919 May 23 01:35 all_results.csv\n-rw-r--r--  1 ubuntu ubuntu  3662 May 23 01:35 mixed_mechanism_report.md\n-rw-r--r--  1 ubuntu ubuntu 27480 May 23 01:33 mixed_mechanism_semisynthetic.py\n-rw-r--r--  1 ubuntu ubuntu  7634 May 23 01:35 scheme_d_results.csv\n-rw-r--r--  1 ubuntu ubuntu  7646 May 23 01:35 scheme_e_results.csv",
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

_source line 132_

全部文件已生成。结果总结：

**Scheme D** (base=difficulty-dependent, instruct=uniform) 更接近观测数据（L2=0.246 vs 0.351）：
- ρ_overall = **-0.676** (观测 -0.597，方向正确但偏强)
- ρ_base = **-0.638** (观测 -0.570，接近)
- ρ_instruct = **-0.302** (观测 -0.079，偏强 — 注入推动 instruct ρ 负向太多)
- χ² = **634.4** (观测 562.7，匹配良好)

**关键发现**：
1. 两个 scheme 都能**同时复现** overall ρ≈-0.6 AND direction reversal χ²>100
2. Scheme D 更优，因为它的 instruct ρ 更接近 0（-0.302 vs -0.418），但仍然比观测值 -0.079 强太多
3. 残差主要在 instruct 维度：即使用 uniform injection，instruct 的 ρ 也被 ceiling effect 推向 -0.3，而观测值仅 -0.079 — 说明实际中 instruct models 的"contamination"可能比我们注入的 30% 更稀疏，或者存在其他机制（如 instruction-following 能力提升）抵消了 contamination 信号

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "uuid": "2cdcb0df-67a0-4dc9-bf2f-3f20bca6730c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JgTGBzpShwAFcE6odJJL8e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 476,
      "cache_read_input_tokens": 61187,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 476
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

_source line 133_

全部文件已生成。结果总结：

**Scheme D** (base=difficulty-dependent, instruct=uniform) 更接近观测数据（L2=0.246 vs 0.351）：
- ρ_overall = **-0.676** (观测 -0.597，方向正确但偏强)
- ρ_base = **-0.638** (观测 -0.570，接近)
- ρ_instruct = **-0.302** (观测 -0.079，偏强 — 注入推动 instruct ρ 负向太多)
- χ² = **634.4** (观测 562.7，匹配良好)

**关键发现**：
1. 两个 scheme 都能**同时复现** overall ρ≈-0.6 AND direction reversal χ²>100
2. Scheme D 更优，因为它的 instruct ρ 更接近 0（-0.302 vs -0.418），但仍然比观测值 -0.079 强太多
3. 残差主要在 instruct 维度：即使用 uniform injection，instruct 的 ρ 也被 ceiling effect 推向 -0.3，而观测值仅 -0.079 — 说明实际中 instruct models 的"contamination"可能比我们注入的 30% 更稀疏，或者存在其他机制（如 instruction-following 能力提升）抵消了 contamination 信号

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 397011,
  "duration_api_ms": 329662,
  "num_turns": 14,
  "stop_reason": "end_turn",
  "session_id": "341243f4-3a11-4f53-b15a-98e69b4cde74",
  "total_cost_usd": 1.04588725,
  "usage": {
    "input_tokens": 14,
    "cache_creation_input_tokens": 49822,
    "cache_read_input_tokens": 463636,
    "output_tokens": 14078,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49822,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 409,
        "cache_read_input_tokens": 61187,
        "cache_creation_input_tokens": 476,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 476
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1712,
      "outputTokens": 8502,
      "cacheReadInputTokens": 514260,
      "cacheCreationInputTokens": 44011,
      "webSearchRequests": 0,
      "costUSD": 0.15066175,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 14,
      "outputTokens": 14078,
      "cacheReadInputTokens": 463636,
      "cacheCreationInputTokens": 49822,
      "webSearchRequests": 0,
      "costUSD": 0.8952254999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5fd19d46-5143-4755-b910-63b4da2b7b69"
}
```

</details>

---
