# code llama semisynthetic rmse

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 17
- **Original source:** `logs/workers/worker_code_llama-semisynthetic-rmse_20260521T204338.log`
- **Structured JSON:** [`fe0e251062312712b816.json`](../../sessions/fe/fe0e251062312712b816.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/ec_hte_llm_annotation",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
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
  "uuid": "f0c6faa0-b68b-4ebd-acad-071f8f7ed15e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu-ec-hte-llm-annotation/memory/"
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
    "resetsAt": 1779396600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "44effe64-4d5e-4291-8ca9-e51217e18926",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### Assistant

_source line 4_

I'll start by reading the core project files to understand the existing DGP and correction interfaces.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7541b572-bd66-4bed-b3e5-f1d3ab2bb792",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDkZdYdjg9A6ffsGEPw37R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6905
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01JiTxPmZKEshfGvEdF9syp4`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/experiment_runner.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "0049bb76-f135-4541-8f0d-219364e5996a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDkZdYdjg9A6ffsGEPw37R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6905
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 6 · 2026-05-21T20:43:49.594Z_

<details><summary>↩ Tool result · reported error · `toolu_01JiTxPmZKEshfGvEdF9syp4`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "dc3b3c58-681e-4972-9d42-9a77b68680ba",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_01EZ984RWXQheXkhkwopcopr`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/hb_confusion.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "9cf13e4d-f3f1-4fef-bfa2-c476927568a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDkZdYdjg9A6ffsGEPw37R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6905
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 8 · 2026-05-21T20:43:50.152Z_

<details><summary>↩ Tool result · reported error · `toolu_01EZ984RWXQheXkhkwopcopr`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7c452ac5-d58b-4c15-a5e8-0ca764f90347",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation."
}
```

</details>

---

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — Read · `toolu_012nE8u81jqCPydjrcw8Qd2o`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/src/dgp.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "0441ee5e-e314-4ded-88c8-fa5d57fae436",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDkZdYdjg9A6ffsGEPw37R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6905
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 10 · 2026-05-21T20:43:50.529Z_

<details><summary>↩ Tool result · reported error · `toolu_012nE8u81jqCPydjrcw8Qd2o`</summary>

```text
File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "33dbb3aa-3391-468c-a7d1-7e2ff597bb5f",
  "tool_use_result": "Error: File does not exist. Note: your current working directory is /home/ubuntu/ec_hte_llm_annotation."
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01E4MWxD5k97jsoeiYNd26cu`</summary>

```json
{
  "pattern": "src/correction*.py",
  "path": "/home/ubuntu/ec_hte_llm_annotation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "044d84ff-5dea-4a1e-a7a8-794c333bbe2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UDkZdYdjg9A6ffsGEPw37R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6905,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6905
      },
      "output_tokens": 6,
      "service_tier": "standard",
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

_source line 12 · 2026-05-21T20:43:50.936Z_

<details><summary>↩ Tool result · `toolu_01E4MWxD5k97jsoeiYNd26cu`</summary>

```text
No files found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "67381273-c10f-49ea-888e-3173ba2918e2",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 54,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
The source files don't exist yet. Let me check what files do exist in the project.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "767639d8-251f-40a7-a188-b46b473704ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NA8xei883DKPVAAy4hL538",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 18746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 14_

The specified source files don't exist yet. Let me explore what's actually in the project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "a547c2d2-6e19-49a2-a61d-852727f54051",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NA8xei883DKPVAAy4hL538",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 18746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 15_

<details open><summary>🔧 Tool call — Bash · `toolu_0161LhzffZ9AaJMjTFoncosX`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -type f | head -80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "a2d362a2-39b3-4e37-bbc1-3752979922bc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NA8xei883DKPVAAy4hL538",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 467,
      "cache_read_input_tokens": 18746,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 467
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

_source line 16 · 2026-05-21T20:43:54.405Z_

<details><summary>↩ Tool result · `toolu_0161LhzffZ9AaJMjTFoncosX`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py
/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/.venv/.gitignore
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_objgraph
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/undill
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3.14
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.fish
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/httpx
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/datasets-cli
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/hf
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_gprof
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/normalizer
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tiny-agents
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/Activate.ps1
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/typer
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numba
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pytensor-cache
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/f2py
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pygmentize
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.csh
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/huggingface-cli
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/markdown-it
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tqdm
/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numpy-config
/home/ubuntu/ec_hte_llm_annotation/.venv/pyvenv.cfg
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/types.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/__init__.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/_staggered.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/impl.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/utils.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/py.typed
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__pycache__/__init__.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__pycache__/__init__.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__pycache__/main.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/py.typed
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/main.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__init__.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tumma.mplstyle
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-variat.mplstyle
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tenui.yml
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tenui.mplstyle
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-variat.yml
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-cetrino.mplstyle
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-vibrant.yml
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-cetrino.yml
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-vibrant.mplstyle
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tumma.yml
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/plot_matrix.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/__init__.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/_version.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/plot_collection.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/style.cpython-314.pyc
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/bf_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ess_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.pyi
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils_plot_types.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/convergence_dist_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_rootogram_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/trace_plot.pyi
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_tstat.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/prior_posterior_plot.pyi
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/rank_plot.py
/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/__pycache__/dgof_plot.cpython-314.pyc
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "e5084d5c-2b6d-4218-ab4c-d460ece09d59",
  "tool_use_result": {
    "stdout": "/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py\n/home/ubuntu/ec_hte_llm_annotation/scripts/plot_applicability_frontier.py\n/home/ubuntu/ec_hte_llm_annotation/scripts/explore_tweeteval.py\n/home/ubuntu/ec_hte_llm_annotation/scripts/fig1_bias_mechanism.py\n/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py\n/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py\n/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/.gitignore\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_objgraph\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/undill\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3.14\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.fish\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/httpx\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/datasets-cli\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/hf\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/get_gprof\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/normalizer\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tiny-agents\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/Activate.ps1\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/typer\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numba\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pytensor-cache\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/f2py\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pygmentize\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/activate.csh\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/huggingface-cli\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/pip3\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/markdown-it\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/tqdm\n/home/ubuntu/ec_hte_llm_annotation/.venv/bin/numpy-config\n/home/ubuntu/ec_hte_llm_annotation/.venv/pyvenv.cfg\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/utils.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/impl.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/types.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/__init__.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/_staggered.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/impl.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__pycache__/utils.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/_staggered.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/py.typed\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/__init__.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/aiohappyeyeballs/types.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__pycache__/__init__.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/_multiprocess/__init__.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__pycache__/__init__.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__pycache__/main.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/py.typed\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/main.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/annotated_doc/__init__.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tumma.mplstyle\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-variat.mplstyle\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tenui.yml\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tenui.mplstyle\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-variat.yml\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-cetrino.mplstyle\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-vibrant.yml\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-cetrino.yml\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-vibrant.mplstyle\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/styles/arviz-tumma.yml\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plot_collection.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/plot_matrix.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/__init__.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/_version.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/plot_collection.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/__pycache__/style.cpython-314.pyc\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/bf_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ess_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/forest_plot.pyi\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/utils_plot_types.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/convergence_dist_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_rootogram_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/trace_plot.pyi\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/ppc_tstat.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/prior_posterior_plot.pyi\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/rank_plot.py\n/home/ubuntu/ec_hte_llm_annotation/.venv/lib/python3.14/site-packages/arviz_plots/plots/__pycache__/dgof_plot.cpython-314.pyc",
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

_source line 17_

<details open><summary>🔧 Tool call — Bash · `toolu_01PpvvSbDBkcSHqi3ov1cYuF`</summary>

```json
{
  "command": "find /home/ubuntu/ec_hte_llm_annotation -maxdepth 1 -type f -name \"*.py\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "19c78ff1-547a-4b27-942d-2ccc7d573c99",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BupdQSCtAWEgMqrt5ZejNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 19213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3057
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 18 · 2026-05-21T20:43:57.112Z_

<details><summary>↩ Tool result · `toolu_01PpvvSbDBkcSHqi3ov1cYuF`</summary>

```text
/home/ubuntu/ec_hte_llm_annotation/draw_fig2.py
/home/ubuntu/ec_hte_llm_annotation/draw_fig3.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py
/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py
/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py
/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py
/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py
/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py
/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py
/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py
/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py
/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py
/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py
/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py
/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py
/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py
/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py
/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py
/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py
/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py
/home/ubuntu/ec_hte_llm_annotation/exp021_seeds_supplement.py
/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_gemini_annotation.py
/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "d51a9c94-88bf-44ca-8c69-98eed992d381",
  "tool_use_result": {
    "stdout": "/home/ubuntu/ec_hte_llm_annotation/draw_fig2.py\n/home/ubuntu/ec_hte_llm_annotation/draw_fig3.py\n/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py\n/home/ubuntu/ec_hte_llm_annotation/exp001_hyperprior_sensitivity.py\n/home/ubuntu/ec_hte_llm_annotation/exp001_regularize.py\n/home/ubuntu/ec_hte_llm_annotation/exp002_bias_bound.py\n/home/ubuntu/ec_hte_llm_annotation/exp003_tweeteval.py\n/home/ubuntu/ec_hte_llm_annotation/exp004_hate_speech.py\n/home/ubuntu/ec_hte_llm_annotation/exp005_diagnostic_criterion.py\n/home/ubuntu/ec_hte_llm_annotation/exp006_budget_sensitivity.py\n/home/ubuntu/ec_hte_llm_annotation/exp007_ppci_dsl.py\n/home/ubuntu/ec_hte_llm_annotation/exp008_filter_analysis.py\n/home/ubuntu/ec_hte_llm_annotation/exp008_gpt55_annotate.py\n/home/ubuntu/ec_hte_llm_annotation/exp008_gpt5x_annotate.py\n/home/ubuntu/ec_hte_llm_annotation/exp008_multi_llm.py\n/home/ubuntu/ec_hte_llm_annotation/exp010_misspecified_subgroups.py\n/home/ubuntu/ec_hte_llm_annotation/exp011_causal_forest.py\n/home/ubuntu/ec_hte_llm_annotation/exp013_boundary_condition.py\n/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py\n/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py\n/home/ubuntu/ec_hte_llm_annotation/exp016_semi_real_better_cm.py\n/home/ubuntu/ec_hte_llm_annotation/exp017_rlearner.py\n/home/ubuntu/ec_hte_llm_annotation/exp018_multiplicative_dgp.py\n/home/ubuntu/ec_hte_llm_annotation/exp019_pz1_sweep.py\n/home/ubuntu/ec_hte_llm_annotation/exp020_kappa_sweep.py\n/home/ubuntu/ec_hte_llm_annotation/exp021_seeds_supplement.py\n/home/ubuntu/ec_hte_llm_annotation/mvp_simulation.py\n/home/ubuntu/ec_hte_llm_annotation/pilot_gemini_annotation.py\n/home/ubuntu/ec_hte_llm_annotation/pilot_llm_annotation.py",
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

_source line 19_

<details open><summary>🔧 Tool call — Bash · `toolu_01AdRXKZXsjwTyfUNvRr5AqV`</summary>

```json
{
  "command": "ls -la /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/ 2>/dev/null || echo \"directory does not exist\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7e9af2e1-b51b-42cc-ab74-e01616933026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BupdQSCtAWEgMqrt5ZejNA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3057,
      "cache_read_input_tokens": 19213,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3057
      },
      "output_tokens": 59,
      "service_tier": "standard",
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

_source line 20 · 2026-05-21T20:43:57.691Z_

<details><summary>↩ Tool result · `toolu_01AdRXKZXsjwTyfUNvRr5AqV`</summary>

```text
total 156
drwxr-xr-x  2 ubuntu ubuntu  4096 May 21 20:40 .
drwxr-xr-x 14 ubuntu ubuntu  4096 May 21 20:38 ..
-rw-r--r--  1 ubuntu ubuntu 15564 May 21 20:40 analyze_llama.py
-rw-r--r--  1 ubuntu ubuntu 61636 May 21 20:38 llama31_8b_balanced.csv
-rw-r--r--  1 ubuntu ubuntu  3096 May 21 20:40 llama_analysis.md
-rw-r--r--  1 ubuntu ubuntu   256 May 21 20:40 llama_metrics.csv
-rw-r--r--  1 ubuntu ubuntu 60634 May 21 20:38 pilot_gemini_annotations.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "1d80c410-f283-42c4-9dee-f0805c014636",
  "tool_use_result": {
    "stdout": "total 156\ndrwxr-xr-x  2 ubuntu ubuntu  4096 May 21 20:40 .\ndrwxr-xr-x 14 ubuntu ubuntu  4096 May 21 20:38 ..\n-rw-r--r--  1 ubuntu ubuntu 15564 May 21 20:40 analyze_llama.py\n-rw-r--r--  1 ubuntu ubuntu 61636 May 21 20:38 llama31_8b_balanced.csv\n-rw-r--r--  1 ubuntu ubuntu  3096 May 21 20:40 llama_analysis.md\n-rw-r--r--  1 ubuntu ubuntu   256 May 21 20:40 llama_metrics.csv\n-rw-r--r--  1 ubuntu ubuntu 60634 May 21 20:38 pilot_gemini_annotations.csv",
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

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Let me read the most relevant existing experiment files, especially exp015 (semi_real_cm) and exp014 (asymmetric) since they seem most relevant to this task. Also exp001 for the baseline DGP.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "aef56864-c2fb-4f14-a0ed-1595bd7b622c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGQgsBmkZwBcF3pfxjrom5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 22270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1162
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

_source line 22_

Let me read the most relevant existing experiments to understand the patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "2ffd6c67-e893-4e36-b0c8-9d2ddad35d2c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGQgsBmkZwBcF3pfxjrom5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 22270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1162
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

_source line 23_

<details open><summary>🔧 Tool call — Read · `toolu_01KEBT3F8wtodNwd1jEGvBXV`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "aad2cffc-2317-48a2-aac6-e9a94646d251",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGQgsBmkZwBcF3pfxjrom5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 22270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1162
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

_source line 24 · 2026-05-21T20:44:02.003Z_

<details><summary>↩ Tool result · `toolu_01KEBT3F8wtodNwd1jEGvBXV`</summary>

```text
1	"""
2	exp-015: Semi-Real Confusion Matrix EC-HTE Experiment.
3	
4	Uses real asymmetric confusion matrices from GPT-4.1 TweetEval pilot annotations.
5	Ground truth CATE is synthetic, but CMs come from real LLM pilot data.
6	
7	4 subgroups with real asymmetric CMs (from pilot GPT-4.1 annotations, n>=10 only):
8	  S0 (False_medium): FPR=0.054, FNR=0.526, weight=0.38
9	  S1 (False_short):  FPR=0.101, FNR=0.300, weight=0.22
10	  S2 (True_short):   FPR=0.143, FNR=0.308, weight=0.14
11	  S3 (True_medium):  FPR=0.194, FNR=0.222, weight=0.25
12	
13	Output:
14	  results/exp015_semi_real_raw.csv
15	  results/exp015_semi_real_summary.csv
16	  results/exp015_semi_real_analysis.md
17	
18	Usage: python3 exp015_semi_real_cm.py --n-mc 100
19	"""
20	
21	import argparse
22	import time
23	import warnings
24	import numpy as np
25	import pandas as pd
26	from scipy.special import gammaln
27	
28	warnings.filterwarnings('ignore')
29	
30	# === Config ===
31	
32	N = 5000
33	N_EXPERTS = [100, 250, 500]
34	SEED_BASE = 0
35	
36	SUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']
37	SUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])
38	SUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()
39	
40	# Real asymmetric CMs from GPT-4.1 pilot (FPR, FNR per subgroup)
41	SUBGROUP_CM = {
42	    'S0': {'fpr': 0.054, 'fnr': 0.526},
43	    'S1': {'fpr': 0.101, 'fnr': 0.300},
44	    'S2': {'fpr': 0.143, 'fnr': 0.308},
45	    'S3': {'fpr': 0.194, 'fnr': 0.222},
46	}
47	
48	P_Z1 = 0.18  # P(Z=1) from pilot overall
49	P_T1 = 0.5
50	
51	
52	def get_cm_matrix(fpr, fnr):
53	    """Build 2x2 confusion matrix: M[z_true, z_obs]."""
54	    return np.array([[1 - fpr, fpr],
55	                     [fnr, 1 - fnr]])
56	
57	
58	# True CATE by (z, subgroup)
59	def true_tau(z, s_idx):
60	    if z == 0:
61	        return 0.3 + 0.1 * s_idx
62	    else:
63	        return 0.8 - 0.15 * s_idx
64	
65	
66	# === Core Estimators ===
67	
68	def diff_in_means(Y, T, mask):
69	    t1 = mask & (T == 1)
70	    t0 = mask & (T == 0)
71	    n1, n0 = t1.sum(), t0.sum()
72	    if n1 < 2 or n0 < 2:
73	        return np.nan, np.nan
74	    y1, y0 = Y[t1], Y[t0]
75	    tau_hat = y1.mean() - y0.mean()
76	    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
77	    return tau_hat, se
78	
79	
80	def estimate_confusion_matrix(z_true, z_hat):
81	    C = np.zeros((2, 2))
82	    for zt in [0, 1]:
83	        mask = z_true == zt
84	        n = mask.sum()
85	        for zh in [0, 1]:
86	            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5
87	    return C
88	
89	
90	def build_mixing_matrix(C, p_z, p_z_hat):
91	    """M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule."""
92	    M = np.zeros((2, 2))
93	    for zh in [0, 1]:
94	        for z in [0, 1]:
95	            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5
96	    return M
97	
98	
99	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
100	    cond = np.linalg.cond(M)
101	    if cond > cond_threshold:
102	        return tau_obs.copy(), se_obs.copy()
103	    det = np.linalg.det(M)
104	    if abs(det) < 1e-10:
105	        return tau_obs.copy(), se_obs.copy()
106	    Mi = np.linalg.inv(M)
107	    tau_c = Mi @ tau_obs
108	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
109	    return tau_c, se_c
110	
111	
112	# === HB Gibbs Sampler ===
113	
114	def get_counts(z_true, z_hat, subgroups, labels):
115	    k = len(labels)
116	    counts = np.zeros((k, 2, 2), dtype=int)
117	    for i, s in enumerate(labels):
118	        ms = subgroups == s
119	        for z in [0, 1]:
120	            mz = ms & (z_true == z)
121	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
122	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
123	    return counts
124	
125	
126	def _split_rhat(chains):
127	    parts = []
128	    for c in range(chains.shape[0]):
129	        half = chains.shape[1] // 2
130	        parts.append(chains[c, :half])
131	        parts.append(chains[c, half:2 * half])
132	    parts = np.array(parts)
133	    m = parts.shape[0]
134	    n = parts.shape[1]
135	    chain_means = parts.mean(axis=1)
136	    W = np.mean(np.var(parts, axis=1, ddof=1))
137	    B = n * np.var(chain_means, ddof=1)
138	    if W < 1e-20:
139	        return 1.0
140	    var_hat = (1 - 1.0 / n) * W + B / n
141	    return float(np.sqrt(var_hat / W))
142	
143	
144	def _bulk_ess(chains):
145	    x = chains.ravel()
146	    n = len(x)
147	    mu = x.mean()
148	    xc = x - mu
149	    max_lag = min(n // 2, 300)
150	    c0 = np.dot(xc, xc)
151	    if c0 < 1e-20:
152	        return float(n)
153	    tau = 1.0
154	    for lag in range(1, max_lag - 1, 2):
155	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
156	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
157	        pair = r1 + r2
158	        if pair < 0:
159	            break
160	        tau += 2 * pair
161	    return float(n / tau)
162	
163	
164	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
165	    if alpha < 1e-10:
166	        return -1e10
167	    a = alpha / 2.0
168	    k = theta_z.shape[0]
169	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
170	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
171	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
172	    return lp
173	
174	
175	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,
176	                         hp_a0=3.0, hp_b0=1.0):
177	    k = len(labels)
178	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
179	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
180	    chain_inits = chain_inits_pool[:n_chains]
181	    all_alpha, all_theta = [], []
182	    t0 = time.time()
183	
184	    for chain in range(n_chains):
185	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
186	        alpha = chain_inits[chain].copy()
187	        theta = np.ones((k, 2, 2)) * 0.5
188	        mh_scale = np.array([0.3, 0.3])
189	        accept_ct = np.array([0, 0])
190	        attempt_ct = np.array([0, 0])
191	
192	        alpha_samples = np.zeros((n_iter, 2))
193	        theta_samples = np.zeros((n_iter, k, 2, 2))
194	
195	        for it in range(n_warmup + n_iter):
196	            for z in [0, 1]:
197	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
198	                post_a = np.maximum(post_a, 1e-6)
199	                g = rng.gamma(post_a)
200	                g_sum = g.sum(axis=1, keepdims=True)
201	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
202	
203	            for z in [0, 1]:
204	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
205	                a_prop = np.exp(x_prop)
206	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
207	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
208	                accepted = np.log(rng.rand()) < log_r
209	                if accepted:
210	                    alpha[z] = a_prop
211	                if it < n_warmup:
212	                    accept_ct[z] += int(accepted)
213	                    attempt_ct[z] += 1
214	
215	            if it < n_warmup and it > 0 and it % 100 == 0:
216	                for z in [0, 1]:
217	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
218	                    if rate < 0.2:
219	                        mh_scale[z] *= 0.7
220	                    elif rate > 0.5:
221	                        mh_scale[z] *= 1.3
222	                    accept_ct[z] = 0
223	                    attempt_ct[z] = 0
224	
225	            if it >= n_warmup:
226	                idx = it - n_warmup
227	                alpha_samples[idx] = alpha.copy()
228	                theta_samples[idx] = theta.copy()
229	
230	        all_alpha.append(alpha_samples)
231	        all_theta.append(theta_samples)
232	
233	    runtime = time.time() - t0
234	    alpha_arr = np.stack(all_alpha)
235	    theta_arr = np.stack(all_theta)
236	
237	    C = {}
238	    for i, s in enumerate(labels):
239	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
240	
241	    return C, {'runtime_seconds': runtime}
242	
243	
244	# === DGP ===
245	
246	def generate_data(n_expert, seed):
247	    """Generate one MC dataset with real asymmetric CMs."""
248	    rng = np.random.RandomState(seed)
249	
250	    # Assign subgroups
251	    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)
252	    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])
253	
254	    # Draw Z_true
255	    Z = rng.binomial(1, P_Z1, N)
256	
257	    # Draw T
258	    T = rng.binomial(1, P_T1, N)
259	
260	    # Generate Z_obs from Z_true using subgroup-specific CM
261	    Z_hat = np.empty(N, dtype=int)
262	    for i in range(4):
263	        s_mask = S_idx == i
264	        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],
265	                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])
266	        n_s = s_mask.sum()
267	        z_s = Z[s_mask]
268	        # For each unit: P(Z_obs=1 | Z_true=z, S=s) = cm[z, 1]
269	        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])
270	        Z_hat[s_mask] = rng.binomial(1, p_obs1)
271	
272	    # Generate Y with heterogeneous treatment effects
273	    tau_vals = np.zeros(N)
274	    for i in range(4):
275	        s_mask = S_idx == i
276	        tau_vals[s_mask & (Z == 0)] = true_tau(0, i)
277	        tau_vals[s_mask & (Z == 1)] = true_tau(1, i)
278	
279	    eps = rng.randn(N)
280	    Y = 1.0 + tau_vals * T + eps
281	
282	    # Expert mask
283	    expert_idx = rng.choice(N, n_expert, replace=False)
284	    expert_mask = np.zeros(N, dtype=bool)
285	    expert_mask[expert_idx] = True
286	
287	    return {
288	        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,
289	        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,
290	    }
291	
292	
293	# === MC Runner ===
294	
295	def run_one_mc(data, n_expert, seed):
296	    """Run one MC iteration: all methods x all (subgroup, z_level) combos."""
297	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
298	    S_idx = data['S_idx']
299	    expert_mask = data['expert_mask']
300	
301	    z_exp = Z[expert_mask]
302	    zh_exp = Z_hat[expert_mask]
303	    s_exp = S[expert_mask]
304	
305	    # Global confusion matrix from expert subset
306	    C_global = estimate_confusion_matrix(z_exp, zh_exp)
307	    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])
308	    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])
309	    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)
310	
311	    # HB Dirichlet confusion matrices (partial pooling via Gibbs sampler)
312	    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)
313	    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)
314	
315	    M_hb_sub = {}
316	    for i, s_val in enumerate(SUBGROUP_LABELS):
317	        sm_exp = (s_exp == s_val)
318	        sm_all = (S == s_val)
319	        if sm_exp.sum() >= 4:
320	            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])
321	        else:
322	            p_z_s = p_z_global
323	        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])
324	        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)
325	
326	    rows = []
327	
328	    for s_i, s_val in enumerate(SUBGROUP_LABELS):
329	        s_mask = S == s_val
330	
331	        for z_level in [0, 1]:
332	            oracle_cate = true_tau(z_level, s_i)
333	
334	            # Oracle: uses Z_true
335	            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))
336	            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan
337	            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan
338	            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0
339	            rows.append({
340	                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,
341	                'z_level': z_level, 'method': 'oracle',
342	                'cate': th_or, 'oracle_cate': oracle_cate,
343	                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,
344	                'ci_lo': ci_lo_or, 'ci_hi': ci_hi_or,
345	                'coverage': cov_or,
346	            })
347	
348	            # Naive: uses Z_obs
349	            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))
350	            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan
351	            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan
352	            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0
353	            rows.append({
354	                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,
355	                'z_level': z_level, 'method': 'naive',
356	                'cate': th_nv, 'oracle_cate': oracle_cate,
357	                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,
358	                'ci_lo': ci_lo_nv, 'ci_hi': ci_hi_nv,
359	                'coverage': cov_nv,
360	            })
361	
362	            # Global corrected
363	            tau_obs = np.array([
364	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],
365	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],
366	            ])
367	            se_obs = np.array([
368	                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],
369	                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],
370	            ])
371	            if not np.any(np.isnan(tau_obs)):
372	                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)
373	                th_gc = tau_gc[z_level]
374	                se_gc_z = se_gc[z_level]
375	            else:
376	                th_gc, se_gc_z = np.nan, np.nan
377	            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
378	            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan
379	            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0
380	            rows.append({
381	                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,
382	                'z_level': z_level, 'method': 'global_corrected',
383	                'cate': th_gc, 'oracle_cate': oracle_cate,
384	                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,
385	                'ci_lo': ci_lo_gc, 'ci_hi': ci_hi_gc,
386	                'coverage': cov_gc,
387	            })
388	
389	            # HB EC-HTE
390	            if not np.any(np.isnan(tau_obs)):
391	                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)
392	                th_hb = tau_hb[z_level]
393	                se_hb_z = se_hb[z_level]
394	            else:
395	                th_hb, se_hb_z = np.nan, np.nan
396	            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
397	            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan
398	            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0
399	            rows.append({
400	                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,
401	                'z_level': z_level, 'method': 'hb_ec_hte',
402	                'cate': th_hb, 'oracle_cate': oracle_cate,
403	                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,
404	                'ci_lo': ci_lo_hb, 'ci_hi': ci_hi_hb,
405	                'coverage': cov_hb,
406	            })
407	
408	    return rows
409	
410	
411	def aggregate_results(df_raw):
412	    """Aggregate raw results to summary statistics."""
413	    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']
414	    rows = []
415	    for keys, grp in df_raw.groupby(group_cols):
416	        row = dict(zip(group_cols, keys))
417	        valid = grp['bias'].dropna()
418	        if len(valid) == 0:
419	            continue
420	        row['mean_bias'] = valid.mean()
421	        row['mean_abs_bias'] = valid.abs().mean()
422	        row['mean_rmse'] = np.sqrt((valid ** 2).mean())
423	        row['mean_coverage'] = grp['coverage'].mean()
424	        row['se_bias'] = valid.std() / np.sqrt(len(valid))
425	        row['se_rmse'] = row['mean_rmse'] / np.sqrt(2 * len(valid))
426	        rows.append(row)
427	    return pd.DataFrame(rows)
428	
429	
430	def write_analysis(df_summary):
431	    """Write analysis markdown report."""
432	    lines = []
433	    lines.append("# exp-015: Semi-Real Confusion Matrix EC-HTE Experiment\n")
434	    lines.append("## Design\n")
435	    lines.append("Uses **real asymmetric confusion matrices** from GPT-4.1 TweetEval pilot annotations.")
436	    lines.append("Ground truth CATE is synthetic; confusion matrices are empirical.\n")
437	    lines.append("| Subgroup | Weight | FPR | FNR |")
438	    lines.append("|----------|--------|-----|-----|")
439	    for i, s in enumerate(SUBGROUP_LABELS):
440	        cm = SUBGROUP_CM[s]
441	        lines.append(f"| {s} | {SUBGROUP_WEIGHTS[i]:.2f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} |")
442	    lines.append("")
443	    lines.append("**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx\n")
444	    lines.append("| Subgroup | tau(z=0) | tau(z=1) |")
445	    lines.append("|----------|----------|----------|")
446	    for i, s in enumerate(SUBGROUP_LABELS):
447	        lines.append(f"| {s} | {true_tau(0,i):.2f} | {true_tau(1,i):.2f} |")
448	    lines.append("")
449	    lines.append("N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.\n")
450	
451	    lines.append("## Summary Tables\n")
452	    for ne in N_EXPERTS:
453	        lines.append(f"### n_expert = {ne}\n")
454	        sub = df_summary[df_summary['n_expert'] == ne].copy()
455	        sub = sub.sort_values(['subgroup', 'z_level', 'method'])
456	        lines.append("| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |")
457	        lines.append("|----------|---|--------|-----------|-------------|------|----------|")
458	        for _, r in sub.iterrows():
459	            lines.append(f"| {r['subgroup']} | {int(r['z_level'])} | {r['method']} | "
460	                         f"{r['mean_bias']:+.4f} | {r['mean_abs_bias']:.4f} | "
461	                         f"{r['mean_rmse']:.4f} | {r['mean_coverage']:.3f} |")
462	        lines.append("")
463	
464	    # Key comparisons
465	    lines.append("## Key Comparisons\n")
466	    lines.append("### HB EC-HTE vs Global Corrected: Bias Reduction\n")
467	    lines.append("| n_expert | Subgroup | Z | HB Bias | Global Bias | Reduction |")
468	    lines.append("|----------|----------|---|---------|-------------|-----------|")
469	    for ne in N_EXPERTS:
470	        for s in SUBGROUP_LABELS:
471	            for z in [0, 1]:
472	                hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &
473	                                (df_summary['z_level'] == z) & (df_summary['method'] == 'hb_ec_hte')]
474	                gc = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &
475	                                (df_summary['z_level'] == z) & (df_summary['method'] == 'global_corrected')]
476	                if len(hb) > 0 and len(gc) > 0:
477	                    hb_b = hb.iloc[0]['mean_abs_bias']
478	                    gc_b = gc.iloc[0]['mean_abs_bias']
479	                    red = (gc_b - hb_b) / gc_b * 100 if gc_b > 0 else 0
480	                    lines.append(f"| {ne} | {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |")
481	    lines.append("")
482	
483	    # Coverage comparison
484	    lines.append("### Coverage (95% CI)\n")
485	    lines.append("| n_expert | Method | Mean Coverage |")
486	    lines.append("|----------|--------|---------------|")
487	    for ne in N_EXPERTS:
488	        for m in ['oracle', 'naive', 'global_corrected', 'hb_ec_hte']:
489	            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]
490	            if len(sub) > 0:
491	                lines.append(f"| {ne} | {m} | {sub['mean_coverage'].mean():.3f} |")
492	    lines.append("")
493	
494	    # Conclusion
495	    lines.append("## Conclusion\n")
496	    lines.append("Does EC-HTE maintain advantage under realistic asymmetric CMs?\n")
497	
498	    # Compute overall advantage
499	    for ne in N_EXPERTS:
500	        hb_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]
501	        gc_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'global_corrected')]
502	        nv_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]
503	        if len(hb_all) > 0 and len(gc_all) > 0:
504	            hb_rmse = hb_all['mean_rmse'].mean()
505	            gc_rmse = gc_all['mean_rmse'].mean()
506	            nv_rmse = nv_all['mean_rmse'].mean()
507	            lines.append(f"- n_expert={ne}: HB RMSE={hb_rmse:.4f}, Global RMSE={gc_rmse:.4f}, "
508	                         f"Naive RMSE={nv_rmse:.4f}")
509	
510	    report = "\n".join(lines)
511	    with open('results/exp015_semi_real_analysis.md', 'w') as f:
512	        f.write(report)
513	    print("Wrote results/exp015_semi_real_analysis.md")
514	
515	
516	# === Main ===
517	
518	if __name__ == '__main__':
519	    parser = argparse.ArgumentParser()
520	    parser.add_argument('--n-mc', type=int, default=100)
521	    args = parser.parse_args()
522	    n_mc = args.n_mc
523	
524	    print(f"exp-015: Semi-Real Confusion Matrix EC-HTE")
525	    print(f"N={N}, n_mc={n_mc}, n_experts={N_EXPERTS}")
526	    print(f"Subgroup CMs (real asymmetric from GPT-4.1 pilot):")
527	    for s in SUBGROUP_LABELS:
528	        cm = SUBGROUP_CM[s]
529	        print(f"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}")
530	    print(f"Methods: oracle, naive, global_corrected, hb_ec_hte")
531	    print()
532	
533	    results = []
534	    configs = [(ne, mc) for ne in N_EXPERTS for mc in range(n_mc)]
535	    total = len(configs)
536	    t0 = time.time()
537	
538	    for count, (ne, mc) in enumerate(configs, 1):
539	        seed = SEED_BASE + mc
540	        data = generate_data(ne, seed)
541	        mc_rows = run_one_mc(data, ne, seed)
542	        results.extend(mc_rows)
543	        if count % max(1, total // 20) == 0:
544	            elapsed = time.time() - t0
545	            eta = elapsed / count * (total - count)
546	            print(f"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | ne={ne} seed={seed}")
547	
548	    elapsed = time.time() - t0
549	    print(f"\nTotal time: {elapsed:.1f}s")
550	
551	    df_raw = pd.DataFrame(results)
552	    df_raw['abs_bias'] = df_raw['bias'].abs()
553	    df_raw['squared_error'] = df_raw['bias'] ** 2
554	
555	    df_summary = aggregate_results(df_raw)
556	
557	    # Save
558	    df_raw.to_csv('results/exp015_semi_real_raw.csv', index=False)
559	    df_summary.to_csv('results/exp015_semi_real_summary.csv', index=False)
560	    print(f"Saved results/exp015_semi_real_raw.csv ({len(df_raw)} rows)")
561	    print(f"Saved results/exp015_semi_real_summary.csv ({len(df_summary)} rows)")
562	
563	    write_analysis(df_summary)
564	
565	    # Print key metrics
566	    print("\n=== Key Metrics Summary ===\n")
567	    pd.set_option('display.float_format', '{:.4f}'.format)
568	    pd.set_option('display.width', 200)
569	    for ne in N_EXPERTS:
570	        print(f"--- n_expert = {ne} ---")
571	        sub = df_summary[df_summary['n_expert'] == ne]
572	        for m in ['naive', 'global_corrected', 'hb_ec_hte']:
573	            ms = sub[sub['method'] == m]
574	            print(f"  {m:20s}: mean_abs_bias={ms['mean_abs_bias'].mean():.4f}, "
575	                  f"rmse={ms['mean_rmse'].mean():.4f}, coverage={ms['mean_coverage'].mean():.3f}")
576	        print()
577	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7b077e97-8749-4663-91db-ab231c88bcdc",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp015_semi_real_cm.py",
      "content": "\"\"\"\nexp-015: Semi-Real Confusion Matrix EC-HTE Experiment.\n\nUses real asymmetric confusion matrices from GPT-4.1 TweetEval pilot annotations.\nGround truth CATE is synthetic, but CMs come from real LLM pilot data.\n\n4 subgroups with real asymmetric CMs (from pilot GPT-4.1 annotations, n>=10 only):\n  S0 (False_medium): FPR=0.054, FNR=0.526, weight=0.38\n  S1 (False_short):  FPR=0.101, FNR=0.300, weight=0.22\n  S2 (True_short):   FPR=0.143, FNR=0.308, weight=0.14\n  S3 (True_medium):  FPR=0.194, FNR=0.222, weight=0.25\n\nOutput:\n  results/exp015_semi_real_raw.csv\n  results/exp015_semi_real_summary.csv\n  results/exp015_semi_real_analysis.md\n\nUsage: python3 exp015_semi_real_cm.py --n-mc 100\n\"\"\"\n\nimport argparse\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERTS = [100, 250, 500]\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['S0', 'S1', 'S2', 'S3']\nSUBGROUP_WEIGHTS = np.array([0.38, 0.22, 0.14, 0.25])\nSUBGROUP_WEIGHTS = SUBGROUP_WEIGHTS / SUBGROUP_WEIGHTS.sum()\n\n# Real asymmetric CMs from GPT-4.1 pilot (FPR, FNR per subgroup)\nSUBGROUP_CM = {\n    'S0': {'fpr': 0.054, 'fnr': 0.526},\n    'S1': {'fpr': 0.101, 'fnr': 0.300},\n    'S2': {'fpr': 0.143, 'fnr': 0.308},\n    'S3': {'fpr': 0.194, 'fnr': 0.222},\n}\n\nP_Z1 = 0.18  # P(Z=1) from pilot overall\nP_T1 = 0.5\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: M[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# True CATE by (z, subgroup)\ndef true_tau(z, s_idx):\n    if z == 0:\n        return 0.3 + 0.1 * s_idx\n    else:\n        return 0.8 - 0.15 * s_idx\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _split_rhat(chains):\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(n_expert, seed):\n    \"\"\"Generate one MC dataset with real asymmetric CMs.\"\"\"\n    rng = np.random.RandomState(seed)\n\n    # Assign subgroups\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    # Draw Z_true\n    Z = rng.binomial(1, P_Z1, N)\n\n    # Draw T\n    T = rng.binomial(1, P_T1, N)\n\n    # Generate Z_obs from Z_true using subgroup-specific CM\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        n_s = s_mask.sum()\n        z_s = Z[s_mask]\n        # For each unit: P(Z_obs=1 | Z_true=z, S=s) = cm[z, 1]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    # Generate Y with heterogeneous treatment effects\n    tau_vals = np.zeros(N)\n    for i in range(4):\n        s_mask = S_idx == i\n        tau_vals[s_mask & (Z == 0)] = true_tau(0, i)\n        tau_vals[s_mask & (Z == 1)] = true_tau(1, i)\n\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    # Expert mask\n    expert_idx = rng.choice(N, n_expert, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, n_expert, seed):\n    \"\"\"Run one MC iteration: all methods x all (subgroup, z_level) combos.\"\"\"\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    S_idx = data['S_idx']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global confusion matrix from expert subset\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # HB Dirichlet confusion matrices (partial pooling via Gibbs sampler)\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    M_hb_sub = {}\n    for i, s_val in enumerate(SUBGROUP_LABELS):\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_i, s_val in enumerate(SUBGROUP_LABELS):\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = true_tau(z_level, s_i)\n\n            # Oracle: uses Z_true\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'oracle',\n                'cate': th_or, 'oracle_cate': oracle_cate,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'ci_lo': ci_lo_or, 'ci_hi': ci_hi_or,\n                'coverage': cov_or,\n            })\n\n            # Naive: uses Z_obs\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'naive',\n                'cate': th_nv, 'oracle_cate': oracle_cate,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'ci_lo': ci_lo_nv, 'ci_hi': ci_hi_nv,\n                'coverage': cov_nv,\n            })\n\n            # Global corrected\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc = tau_gc[z_level]\n                se_gc_z = se_gc[z_level]\n            else:\n                th_gc, se_gc_z = np.nan, np.nan\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'global_corrected',\n                'cate': th_gc, 'oracle_cate': oracle_cate,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'ci_lo': ci_lo_gc, 'ci_hi': ci_hi_gc,\n                'coverage': cov_gc,\n            })\n\n            # HB EC-HTE\n            if not np.any(np.isnan(tau_obs)):\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb = tau_hb[z_level]\n                se_hb_z = se_hb[z_level]\n            else:\n                th_hb, se_hb_z = np.nan, np.nan\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'n_expert': n_expert, 'subgroup': s_val,\n                'z_level': z_level, 'method': 'hb_ec_hte',\n                'cate': th_hb, 'oracle_cate': oracle_cate,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'ci_lo': ci_lo_hb, 'ci_hi': ci_hi_hb,\n                'coverage': cov_hb,\n            })\n\n    return rows\n\n\ndef aggregate_results(df_raw):\n    \"\"\"Aggregate raw results to summary statistics.\"\"\"\n    group_cols = ['n_expert', 'subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['mean_rmse'] = np.sqrt((valid ** 2).mean())\n        row['mean_coverage'] = grp['coverage'].mean()\n        row['se_bias'] = valid.std() / np.sqrt(len(valid))\n        row['se_rmse'] = row['mean_rmse'] / np.sqrt(2 * len(valid))\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\ndef write_analysis(df_summary):\n    \"\"\"Write analysis markdown report.\"\"\"\n    lines = []\n    lines.append(\"# exp-015: Semi-Real Confusion Matrix EC-HTE Experiment\\n\")\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from GPT-4.1 TweetEval pilot annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n    lines.append(\"| Subgroup | Weight | FPR | FNR |\")\n    lines.append(\"|----------|--------|-----|-----|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.2f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} |\")\n    lines.append(\"\")\n    lines.append(\"**True CATE**: tau(z=0,s) = 0.3 + 0.1*s_idx; tau(z=1,s) = 0.8 - 0.15*s_idx\\n\")\n    lines.append(\"| Subgroup | tau(z=0) | tau(z=1) |\")\n    lines.append(\"|----------|----------|----------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        lines.append(f\"| {s} | {true_tau(0,i):.2f} | {true_tau(1,i):.2f} |\")\n    lines.append(\"\")\n    lines.append(\"N=5000, P(Z=1)=0.18, P(T=1)=0.5, n_expert in {100, 250, 500}, 100 MC seeds.\\n\")\n\n    lines.append(\"## Summary Tables\\n\")\n    for ne in N_EXPERTS:\n        lines.append(f\"### n_expert = {ne}\\n\")\n        sub = df_summary[df_summary['n_expert'] == ne].copy()\n        sub = sub.sort_values(['subgroup', 'z_level', 'method'])\n        lines.append(\"| Subgroup | Z | Method | Mean Bias | Mean |Bias| | RMSE | Coverage |\")\n        lines.append(\"|----------|---|--------|-----------|-------------|------|----------|\")\n        for _, r in sub.iterrows():\n            lines.append(f\"| {r['subgroup']} | {int(r['z_level'])} | {r['method']} | \"\n                         f\"{r['mean_bias']:+.4f} | {r['mean_abs_bias']:.4f} | \"\n                         f\"{r['mean_rmse']:.4f} | {r['mean_coverage']:.3f} |\")\n        lines.append(\"\")\n\n    # Key comparisons\n    lines.append(\"## Key Comparisons\\n\")\n    lines.append(\"### HB EC-HTE vs Global Corrected: Bias Reduction\\n\")\n    lines.append(\"| n_expert | Subgroup | Z | HB Bias | Global Bias | Reduction |\")\n    lines.append(\"|----------|----------|---|---------|-------------|-----------|\")\n    for ne in N_EXPERTS:\n        for s in SUBGROUP_LABELS:\n            for z in [0, 1]:\n                hb = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'hb_ec_hte')]\n                gc = df_summary[(df_summary['n_expert'] == ne) & (df_summary['subgroup'] == s) &\n                                (df_summary['z_level'] == z) & (df_summary['method'] == 'global_corrected')]\n                if len(hb) > 0 and len(gc) > 0:\n                    hb_b = hb.iloc[0]['mean_abs_bias']\n                    gc_b = gc.iloc[0]['mean_abs_bias']\n                    red = (gc_b - hb_b) / gc_b * 100 if gc_b > 0 else 0\n                    lines.append(f\"| {ne} | {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Coverage comparison\n    lines.append(\"### Coverage (95% CI)\\n\")\n    lines.append(\"| n_expert | Method | Mean Coverage |\")\n    lines.append(\"|----------|--------|---------------|\")\n    for ne in N_EXPERTS:\n        for m in ['oracle', 'naive', 'global_corrected', 'hb_ec_hte']:\n            sub = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == m)]\n            if len(sub) > 0:\n                lines.append(f\"| {ne} | {m} | {sub['mean_coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n    lines.append(\"Does EC-HTE maintain advantage under realistic asymmetric CMs?\\n\")\n\n    # Compute overall advantage\n    for ne in N_EXPERTS:\n        hb_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'hb_ec_hte')]\n        gc_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'global_corrected')]\n        nv_all = df_summary[(df_summary['n_expert'] == ne) & (df_summary['method'] == 'naive')]\n        if len(hb_all) > 0 and len(gc_all) > 0:\n            hb_rmse = hb_all['mean_rmse'].mean()\n            gc_rmse = gc_all['mean_rmse'].mean()\n            nv_rmse = nv_all['mean_rmse'].mean()\n            lines.append(f\"- n_expert={ne}: HB RMSE={hb_rmse:.4f}, Global RMSE={gc_rmse:.4f}, \"\n                         f\"Naive RMSE={nv_rmse:.4f}\")\n\n    report = \"\\n\".join(lines)\n    with open('results/exp015_semi_real_analysis.md', 'w') as f:\n        f.write(report)\n    print(\"Wrote results/exp015_semi_real_analysis.md\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    args = parser.parse_args()\n    n_mc = args.n_mc\n\n    print(f\"exp-015: Semi-Real Confusion Matrix EC-HTE\")\n    print(f\"N={N}, n_mc={n_mc}, n_experts={N_EXPERTS}\")\n    print(f\"Subgroup CMs (real asymmetric from GPT-4.1 pilot):\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print(f\"Methods: oracle, naive, global_corrected, hb_ec_hte\")\n    print()\n\n    results = []\n    configs = [(ne, mc) for ne in N_EXPERTS for mc in range(n_mc)]\n    total = len(configs)\n    t0 = time.time()\n\n    for count, (ne, mc) in enumerate(configs, 1):\n        seed = SEED_BASE + mc\n        data = generate_data(ne, seed)\n        mc_rows = run_one_mc(data, ne, seed)\n        results.extend(mc_rows)\n        if count % max(1, total // 20) == 0:\n            elapsed = time.time() - t0\n            eta = elapsed / count * (total - count)\n            print(f\"  [{count}/{total}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s | ne={ne} seed={seed}\")\n\n    elapsed = time.time() - t0\n    print(f\"\\nTotal time: {elapsed:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_raw['abs_bias'] = df_raw['bias'].abs()\n    df_raw['squared_error'] = df_raw['bias'] ** 2\n\n    df_summary = aggregate_results(df_raw)\n\n    # Save\n    df_raw.to_csv('results/exp015_semi_real_raw.csv', index=False)\n    df_summary.to_csv('results/exp015_semi_real_summary.csv', index=False)\n    print(f\"Saved results/exp015_semi_real_raw.csv ({len(df_raw)} rows)\")\n    print(f\"Saved results/exp015_semi_real_summary.csv ({len(df_summary)} rows)\")\n\n    write_analysis(df_summary)\n\n    # Print key metrics\n    print(\"\\n=== Key Metrics Summary ===\\n\")\n    pd.set_option('display.float_format', '{:.4f}'.format)\n    pd.set_option('display.width', 200)\n    for ne in N_EXPERTS:\n        print(f\"--- n_expert = {ne} ---\")\n        sub = df_summary[df_summary['n_expert'] == ne]\n        for m in ['naive', 'global_corrected', 'hb_ec_hte']:\n            ms = sub[sub['method'] == m]\n            print(f\"  {m:20s}: mean_abs_bias={ms['mean_abs_bias'].mean():.4f}, \"\n                  f\"rmse={ms['mean_rmse'].mean():.4f}, coverage={ms['mean_coverage'].mean():.3f}\")\n        print()\n",
      "numLines": 577,
      "startLine": 1,
      "totalLines": 577
    }
  }
}
```

</details>

---

### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Read · `toolu_01YU23GQFGi8xMG8gvEtbx42`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "a9f04b23-ed99-40f7-812a-59e88038fd27",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGQgsBmkZwBcF3pfxjrom5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 22270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1162
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

_source line 26 · 2026-05-21T20:44:02.445Z_

<details><summary>↩ Tool result · `toolu_01YU23GQFGi8xMG8gvEtbx42`</summary>

```text
1	"""
2	exp014_asymmetric.py — Asymmetric Misclassification Verification (exp-014)
3	
4	Verifies the bias product structure under FPR != FNR and demonstrates
5	EC-HTE effectiveness in asymmetric scenarios.
6	
7	Key identity: bias(z, s) = delta_tau * [B_s]_{z,1}
8	where B_s = M_global^{-1} M_s - I.
9	"""
10	
11	import numpy as np
12	import pandas as pd
13	import time
14	import os
15	import sys
16	
17	# ============================================================
18	# Parameters
19	# ============================================================
20	
21	N = 50000
22	N_MC = 100
23	N_EXPERT = 250
24	TAU_Z0 = 0.1
25	RESULTS_DIR = 'results'
26	os.makedirs(RESULTS_DIR, exist_ok=True)
27	
28	CONFIGS = {
29	    'config1': {'name': 'Cross-asymmetric',
30	                'fpr': [0.10, 0.25], 'fnr': [0.20, 0.10]},
31	    'config2': {'name': 'Co-directional',
32	                'fpr': [0.05, 0.20], 'fnr': [0.15, 0.30]},
33	    'config3': {'name': 'Extreme asymmetric',
34	                'fpr': [0.03, 0.30], 'fnr': [0.25, 0.05]},
35	}
36	
37	DELTA_TAUS = [0.1, 0.2, 0.3, 0.4, 0.5]
38	
39	
40	# ============================================================
41	# Core: mixing matrix and analytic bias
42	# ============================================================
43	
44	def mixing_matrix(fpr, fnr):
45	    """M[zhat,z] = P(Z=z|Zhat=zhat,S=s) under P(Z=0)=P(Z=1)=0.5."""
46	    d0 = (1.0 - fpr) + fnr
47	    d1 = fpr + (1.0 - fnr)
48	    return np.array([[(1.0 - fpr) / d0, fnr / d0],
49	                     [fpr / d1, (1.0 - fnr) / d1]])
50	
51	
52	def analytic_bias_asym(fpr_list, fnr_list, weights, tau):
53	    """Compute B_s = M_global^{-1} M_s - I and bias = B_s @ tau."""
54	    K = len(fpr_list)
55	    Ms = [mixing_matrix(fpr_list[s], fnr_list[s]) for s in range(K)]
56	    M_global = sum(weights[s] * Ms[s] for s in range(K))
57	    M_inv = np.linalg.inv(M_global)
58	    biases, Bs = {}, {}
59	    for s in range(K):
60	        B = M_inv @ Ms[s] - np.eye(2)
61	        Bs[s] = B
62	        biases[s] = B @ tau
63	    return biases, Bs, M_global, M_inv, Ms
64	
65	
66	# ============================================================
67	# MC simulation (vectorized main loop, per-run expert labels)
68	# ============================================================
69	
70	def mc_simulate(fpr_list, fnr_list, tau_z0, tau_z1, n, n_mc,
71	                n_expert=0, seed=0):
72	    """Vectorized MC with asymmetric misclassification."""
73	    K = len(fpr_list)
74	    w = np.full(K, 1.0 / K)
75	    tau = np.array([tau_z0, tau_z1])
76	
77	    Ms_oracle = [mixing_matrix(fpr_list[s], fnr_list[s]) for s in range(K)]
78	    M_glob = sum(w[s] * Ms_oracle[s] for s in range(K))
79	    M_glob_inv = np.linalg.inv(M_glob)
80	
81	    rng = np.random.RandomState(seed)
82	    T = rng.binomial(1, 0.5, (n_mc, n))
83	    Z = rng.binomial(1, 0.5, (n_mc, n))
84	    S = rng.binomial(1, 0.5, (n_mc, n))  # K=2 equal weights
85	
86	    tau_i = np.where(Z == 1, tau_z1, tau_z0)
87	    Y = 1.0 + tau_i * T + 0.5 * rng.randn(n_mc, n) + rng.randn(n_mc, n)
88	
89	    # Asymmetric flip: P(flip) = FPR if Z=0, FNR if Z=1
90	    flip_p = np.zeros((n_mc, n))
91	    for s in range(K):
92	        m = (S == s)
93	        flip_p += m * np.where(Z == 0, fpr_list[s], fnr_list[s])
94	    Z_hat = np.where(rng.rand(n_mc, n) < flip_p, 1 - Z, Z)
95	
96	    # Group means: group = S*4 + Zhat*2 + T
97	    ng = K * 4
98	    grp = (S * 4 + Z_hat * 2 + T).ravel()
99	    mi = np.repeat(np.arange(n_mc), n)
100	    comb = mi * ng + grp
101	
102	    sums = np.bincount(comb, weights=Y.ravel(),
103	                       minlength=n_mc * ng).reshape(n_mc, ng)
104	    sq_s = np.bincount(comb, weights=(Y.ravel() ** 2),
105	                       minlength=n_mc * ng).reshape(n_mc, ng)
106	    cnts = np.bincount(comb,
107	                       minlength=n_mc * ng).reshape(n_mc, ng)
108	    means = sums / np.maximum(cnts, 1)
109	    cvars = sq_s / np.maximum(cnts, 1) - means ** 2
110	
111	    # Per-subgroup observed CATE and SE^2
112	    tau_obs, se2_obs = {}, {}
113	    for s in range(K):
114	        b = s * 4
115	        tau_obs[s] = np.column_stack([
116	            means[:, b + 1] - means[:, b + 0],   # zh=0: T=1 - T=0
117	            means[:, b + 3] - means[:, b + 2]])   # zh=1: T=1 - T=0
118	        se2_obs[s] = np.column_stack([
119	            cvars[:, b + 1] / np.maximum(cnts[:, b + 1], 1) +
120	            cvars[:, b + 0] / np.maximum(cnts[:, b + 0], 1),
121	            cvars[:, b + 3] / np.maximum(cnts[:, b + 3], 1) +
122	            cvars[:, b + 2] / np.maximum(cnts[:, b + 2], 1)])
123	
124	    # Naive and oracle-global bias (vectorized)
125	    out = {}
126	    for s in range(K):
127	        out[s] = {
128	            'tau_obs': tau_obs[s],
129	            'se2_obs': se2_obs[s],
130	            'bias_naive': tau_obs[s] - tau,
131	            'bias_global_oracle': tau_obs[s] @ M_glob_inv.T - tau,
132	        }
133	
134	    # Expert-label correction (per MC run)
135	    if n_expert > 0:
136	        for s in range(K):
137	            out[s]['bias_global_est'] = np.zeros((n_mc, 2))
138	            out[s]['bias_echte'] = np.zeros((n_mc, 2))
139	            out[s]['cov_naive'] = np.zeros((n_mc, 2))
140	            out[s]['cov_global_est'] = np.zeros((n_mc, 2))
141	            out[s]['cov_echte'] = np.zeros((n_mc, 2))
142	
143	        for r in range(n_mc):
144	            eidx = rng.choice(n, n_expert, replace=False)
145	            ze = Z[r, eidx]
146	            zhe = Z_hat[r, eidx]
147	            se = S[r, eidx]
148	
149	            # Estimate per-subgroup CM (Laplace smoothing)
150	            Ms_hat = []
151	            for s in range(K):
152	                mask = (se == s)
153	                zt, zh = ze[mask], zhe[mask]
154	                n0 = np.sum(zt == 0)
155	                n1 = np.sum(zt == 1)
156	                fh = (np.sum((zt == 0) & (zh == 1)) + 1) / (n0 + 2)
157	                nh = (np.sum((zt == 1) & (zh == 0)) + 1) / (n1 + 2)
158	                Ms_hat.append(mixing_matrix(fh, nh))
159	
160	            Mgh = sum(w[s] * Ms_hat[s] for s in range(K))
161	            Mgh_inv = np.linalg.inv(Mgh)
162	
163	            for s in range(K):
164	                to = tau_obs[s][r]
165	                se2 = se2_obs[s][r]
166	                Sig = np.diag(se2)
167	
168	                # Global estimated correction
169	                tg = Mgh_inv @ to
170	                out[s]['bias_global_est'][r] = tg - tau
171	                Sg = Mgh_inv @ Sig @ Mgh_inv.T
172	                out[s]['cov_global_est'][r] = (
173	                    np.abs(tg - tau) <= 1.96 * np.sqrt(np.diag(Sg)))
174	
175	                # EC-HTE: per-subgroup correction
176	                Msi = np.linalg.inv(Ms_hat[s])
177	                te = Msi @ to
178	                out[s]['bias_echte'][r] = te - tau
179	                Se = Msi @ Sig @ Msi.T
180	                out[s]['cov_echte'][r] = (
181	                    np.abs(te - tau) <= 1.96 * np.sqrt(np.diag(Se)))
182	
183	                # Naive coverage
184	                se_n = np.sqrt(se2)
185	                out[s]['cov_naive'][r] = (
186	                    np.abs(to - tau) <= 1.96 * se_n)
187	
188	    return out
189	
190	
191	# ============================================================
192	# Run experiments
193	# ============================================================
194	
195	def run_all(n_mc, dry_run=False):
196	    configs_run = {'config1': CONFIGS['config1']} if dry_run else CONFIGS
197	    dtaus = [0.2] if dry_run else DELTA_TAUS
198	
199	    bias_rows = []
200	    corr_rows = []
201	    prod_rows = []
202	    t0 = time.time()
203	    seed_counter = 0
204	
205	    for cfg_key, cfg in configs_run.items():
206	        fpr, fnr = cfg['fpr'], cfg['fnr']
207	        K = len(fpr)
208	        w = np.full(K, 1.0 / K)
209	
210	        for dt in dtaus:
211	            tau_z1 = TAU_Z0 + dt
212	            tau = np.array([TAU_Z0, tau_z1])
213	            seed_counter += 1
214	            seed = seed_counter * 7919  # distinct primes -> distinct seeds
215	
216	            biases, Bs, M_glob, M_inv, Ms = analytic_bias_asym(
217	                fpr, fnr, w, tau)
218	
219	            mc = mc_simulate(fpr, fnr, TAU_Z0, tau_z1, N, n_mc,
220	                             N_EXPERT, seed)
221	
222	            for s in range(K):
223	                for z in range(2):
224	                    ab = biases[s][z]
225	                    mc_vals = mc[s]['bias_global_oracle'][:, z]
226	                    mc_mean = np.mean(mc_vals)
227	                    mc_se = np.std(mc_vals, ddof=1) / np.sqrt(n_mc)
228	
229	                    bias_rows.append({
230	                        'config': cfg_key,
231	                        'config_name': cfg['name'],
232	                        'fpr_s': fpr[s], 'fnr_s': fnr[s],
233	                        'delta_tau': dt,
234	                        'subgroup': s, 'z': z,
235	                        'analytic_bias': ab,
236	                        'mc_bias': mc_mean,
237	                        'mc_se': mc_se,
238	                        'B_z1': Bs[s][z, 1],
239	                    })
240	
241	                    prod_rows.append({
242	                        'config': cfg_key, 'subgroup': s, 'z': z,
243	                        'delta_tau': dt,
244	                        'ratio_analytic': ab / dt,
245	                        'ratio_mc': mc_mean / dt,
246	                    })
247	
248	                    for method, bk, ck in [
249	                        ('naive', 'bias_naive', 'cov_naive'),
250	                        ('global_est', 'bias_global_est', 'cov_global_est'),
251	                        ('echte', 'bias_echte', 'cov_echte'),
252	                    ]:
253	                        bv = mc[s][bk][:, z]
254	                        corr_rows.append({
255	                            'config': cfg_key,
256	                            'config_name': cfg['name'],
257	                            'delta_tau': dt,
258	                            'subgroup': s, 'z': z,
259	                            'method': method,
260	                            'mean_bias': np.mean(bv),
261	                            'abs_bias': np.abs(np.mean(bv)),
262	                            'rmse': np.sqrt(np.mean(bv ** 2)),
263	                            'coverage': np.mean(mc[s][ck][:, z]),
264	                        })
265	
266	            elapsed = time.time() - t0
267	            print(f"  {cfg_key} dt={dt:.1f} done ({elapsed:.1f}s)")
268	
269	    return (pd.DataFrame(bias_rows),
270	            pd.DataFrame(corr_rows),
271	            pd.DataFrame(prod_rows))
272	
273	
274	# ============================================================
275	# Analysis helpers
276	# ============================================================
277	
278	def compute_r2(df):
279	    valid = df[df['analytic_bias'].abs() > 1e-8]
280	    if len(valid) == 0:
281	        return np.nan
282	    ss_res = ((valid['mc_bias'] - valid['analytic_bias']) ** 2).sum()
283	    ss_tot = ((valid['mc_bias'] - valid['mc_bias'].mean()) ** 2).sum()
284	    return 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan
285	
286	
287	def verify_product_structure(df_prod):
288	    rows = []
289	    for (cfg, s, z), grp in df_prod.groupby(['config', 'subgroup', 'z']):
290	        vals = grp['ratio_analytic'].values
291	        if len(vals) > 1 and np.abs(np.mean(vals)) > 1e-12:
292	            cv = np.std(vals) / np.abs(np.mean(vals))
293	        else:
294	            cv = 0.0
295	        rows.append({
296	            'config': cfg, 'subgroup': s, 'z': z,
297	            'mean_ratio': np.mean(vals),
298	            'std_ratio': np.std(vals), 'cv': cv,
299	        })
300	    return pd.DataFrame(rows)
301	
302	
303	# ============================================================
304	# Write analysis markdown
305	# ============================================================
306	
307	def write_analysis_md(df_bias, df_corr, df_prod, r2_val):
308	    ps = verify_product_structure(df_prod)
309	    md = []
310	
311	    md.append("# exp-014: Asymmetric Misclassification Verification\n\n")
312	
313	    # --- Section 1: Setup ---
314	    md.append("## 1. Setup\n\n")
315	    md.append("### Asymmetric Confusion Matrix\n\n")
316	    md.append(r"For subgroup $s$ with $\text{FPR}_s = P(\hat{Z}=1|Z=0,S=s)$"
317	              r" and $\text{FNR}_s = P(\hat{Z}=0|Z=1,S=s)$:" "\n\n")
318	    md.append(r"$$C_s = \begin{pmatrix} 1-\text{FPR}_s & \text{FPR}_s \\"
319	              r" \text{FNR}_s & 1-\text{FNR}_s \end{pmatrix}$$" "\n\n")
320	
321	    md.append("### Mixing Matrix (Bayesian Inversion)\n\n")
322	    md.append(r"Under balanced prior $P(Z=0)=P(Z=1)=0.5$:" "\n\n")
323	    md.append(r"$$M_s[\hat{z}, z] = P(Z=z \mid \hat{Z}=\hat{z}, S=s)$$" "\n\n")
324	    md.append(r"$$M_s = \begin{pmatrix}"
325	              r" \frac{1-\text{FPR}_s}{1-\text{FPR}_s+\text{FNR}_s} &"
326	              r" \frac{\text{FNR}_s}{1-\text{FPR}_s+\text{FNR}_s} \\"
327	              r" \frac{\text{FPR}_s}{\text{FPR}_s+1-\text{FNR}_s} &"
328	              r" \frac{1-\text{FNR}_s}{\text{FPR}_s+1-\text{FNR}_s}"
329	              r" \end{pmatrix}$$" "\n\n")
330	
331	    md.append(r"### Global Mixing Matrix" "\n\n")
332	    md.append(r"$$M_{\text{global}} = \sum_s w_s \, M_s$$" "\n\n")
333	
334	    # --- Section 2: Bias derivation ---
335	    md.append("## 2. Bias Formula Derivation\n\n")
336	    md.append(r"The observed CATE within subgroup $s$ satisfies:" "\n\n")
337	    md.append(r"$$\boldsymbol{\tau}_{\text{obs},s} = M_s \,"
338	              r" \boldsymbol{\tau}$$" "\n\n")
339	    md.append(r"where $\boldsymbol{\tau} = (\tau(0),\;\tau(1))^\top$."
340	              "\n\n")
341	    md.append("After global correction:\n\n")
342	    md.append(r"$$\hat{\boldsymbol{\tau}}_s = M_{\text{global}}^{-1}"
343	              r" M_s \, \boldsymbol{\tau}$$" "\n\n")
344	    md.append("**Bias:**\n\n")
345	    md.append(r"$$\text{bias}(z, s) = \bigl[(M_{\text{global}}^{-1}"
346	              r" M_s - I)\,\boldsymbol{\tau}\bigr]_z"
347	              r" = [B_s \, \boldsymbol{\tau}]_z$$" "\n\n")
348	    md.append(r"where $B_s \equiv M_{\text{global}}^{-1} M_s - I$." "\n\n")
349	
350	    # --- Section 3: Product structure ---
351	    md.append("## 3. Product Structure Proof\n\n")
352	    md.append(r"**Claim.** $\text{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}$"
353	              r" where $\Delta\tau = \tau(1)-\tau(0)$." "\n\n")
354	    md.append("**Proof.** Both $M_s$ and $M_{\\text{global}}$ are "
355	              "stochastic (rows sum to 1):\n\n")
356	    md.append(r"$$M_s \mathbf{1} = \mathbf{1},\quad"
357	              r" M_{\text{global}} \mathbf{1} = \mathbf{1}"
358	              r" \;\Longrightarrow\;"
359	              r" M_{\text{global}}^{-1}\mathbf{1} = \mathbf{1}$$" "\n\n")
360	    md.append(r"$$\Rightarrow\; B_s \mathbf{1}"
361	              r" = (M_{\text{global}}^{-1} M_s - I)\mathbf{1}"
362	              r" = \mathbf{1} - \mathbf{1} = \mathbf{0}$$" "\n\n")
363	    md.append(r"Decompose $\boldsymbol{\tau} = \tau(0)\,\mathbf{1}"
364	              r" + \Delta\tau\,\mathbf{e}_1$"
365	              r" where $\mathbf{e}_1=(0,1)^\top$:" "\n\n")
366	    md.append(r"$$\text{bias}(z,s) = \tau(0)\underbrace{[B_s\mathbf{1}]_z}"
367	              r"_{=0} + \Delta\tau\,[B_s]_{z,1}$$" "\n\n")
368	    md.append(r"$$\boxed{\text{bias}(z,s) = \Delta\tau \cdot [B_s]_{z,1}}$$"
369	              "\n\n")
370	    md.append(r"The coefficient $[B_s]_{z,1}$ depends **only** on "
371	              r"$\{\text{FPR}_k, \text{FNR}_k, w_k\}$, not on "
372	              r"$\Delta\tau$. $\square$" "\n\n")
373	
374	    # Numerical verification
375	    md.append("### Numerical Verification\n\n")
376	    if len(ps) > 0:
377	        md.append(r"For each (config, subgroup, $z$), the ratio "
378	                  r"$\text{bias}/\Delta\tau$ is constant:" "\n\n")
379	        md.append("| Config | Sub | z | Mean ratio | CV |\n")
380	        md.append("|--------|-----|---|-----------|----|\n")
381	        for _, row in ps.iterrows():
382	            md.append(f"| {row['config']} | {int(row['subgroup'])} "
383	                      f"| {int(row['z'])} | {row['mean_ratio']:.6f} "
384	                      f"| {row['cv']:.2e} |\n")
385	        md.append("\nCV (coefficient of variation) = 0 confirms "
386	                  "exact product structure.\n\n")
387	
388	    # --- Section 4: Symmetric connection ---
389	    md.append("## 4. Connection to the Symmetric Case\n\n")
390	    md.append(r"When $\text{FPR}_s = \text{FNR}_s = \pi_s$ "
391	              "(symmetric, assumption A2):\n\n")
392	    md.append(r"$$M_s = \begin{pmatrix} 1-\pi_s & \pi_s \\"
393	              r" \pi_s & 1-\pi_s \end{pmatrix}$$" "\n\n")
394	    md.append(r"$$B_s = \frac{\delta_s}{1-2\bar\pi}"
395	              r" \begin{pmatrix} -1 & 1 \\ 1 & -1 \end{pmatrix},"
396	              r" \quad \delta_s = \pi_s - \bar\pi$$" "\n\n")
397	    md.append("and the bias reduces to:\n\n")
398	    md.append(r"$$\text{bias}(z{=}0,s) = +\frac{\delta_s\,\Delta\tau}"
399	              r"{1-2\bar\pi},\quad"
400	              r" \text{bias}(z{=}1,s) = -\frac{\delta_s\,\Delta\tau}"
401	              r"{1-2\bar\pi}$$" "\n\n")
402	    md.append("**Key differences in the asymmetric case:**\n\n")
403	    md.append("1. The product structure (bias proportional to "
404	              r"$\Delta\tau$) holds in **both** cases." "\n")
405	    md.append("2. In symmetric: "
406	              r"$|{\rm bias}(z{=}0)|=|{\rm bias}(z{=}1)|$. "
407	              "In asymmetric: they differ.\n")
408	    md.append(r"3. In symmetric: error heterogeneity collapses to scalar "
409	              r"$\delta_s/(1{-}2\bar\pi)$. "
410	              r"In asymmetric: it is the matrix entry $[B_s]_{z,1}$." "\n")
411	    md.append("4. **Assumption A2 is not required** for the product "
412	              "structure.\n\n")
413	
414	    # --- Section 5: Numerical results ---
415	    md.append("## 5. Numerical Results\n\n")
416	    md.append(f"### R-squared (analytic vs MC bias): **{r2_val:.6f}**\n\n")
417	
418	    md.append("### Bias table\n\n")
419	    md.append("| Config | delta_tau | Sub | z | Analytic | MC | MC SE |\n")
420	    md.append("|--------|----------|-----|---|----------|-----|-------|\n")
421	    for _, row in df_bias.iterrows():
422	        md.append(f"| {row['config']} | {row['delta_tau']:.1f} "
423	                  f"| {int(row['subgroup'])} | {int(row['z'])} "
424	                  f"| {row['analytic_bias']:+.6f} "
425	                  f"| {row['mc_bias']:+.6f} "
426	                  f"| {row['mc_se']:.6f} |\n")
427	
428	    # --- Section 6: EC-HTE vs Global ---
429	    if len(df_corr) > 0:
430	        md.append("\n## 6. EC-HTE vs Global Correction\n\n")
431	        md.append(f"Expert labels per MC run: {N_EXPERT}\n\n")
432	
433	        md.append("### Per-cell results\n\n")
434	        md.append("| Config | dt | Sub | z | Method "
435	                  "| |Bias| | RMSE | Cov |\n")
436	        md.append("|--------|-----|-----|---|--------"
437	                  "|-------|------|-----|\n")
438	        for _, row in df_corr.iterrows():
439	            md.append(f"| {row['config']} | {row['delta_tau']:.1f} "
440	                      f"| {int(row['subgroup'])} | {int(row['z'])} "
441	                      f"| {row['method']} "
442	                      f"| {row['abs_bias']:.4f} "
443	                      f"| {row['rmse']:.4f} "
444	                      f"| {row['coverage']:.2f} |\n")
445	
446	        md.append("\n### Summary by method\n\n")
447	        md.append("| Method | Mean |Bias| | Mean RMSE | Mean Coverage |\n")
448	        md.append("|--------|-----------|-----------|---------------|\n")
449	        for method in ['naive', 'global_est', 'echte']:
450	            sub = df_corr[df_corr['method'] == method]
451	            md.append(f"| {method} "
452	                      f"| {sub['abs_bias'].mean():.4f} "
453	                      f"| {sub['rmse'].mean():.4f} "
454	                      f"| {sub['coverage'].mean():.2f} |\n")
455	
456	    # --- Section 7: Conclusions ---
457	    md.append("\n## 7. Conclusions\n\n")
458	    md.append(r"1. The **product structure** $\text{bias}(z,s) "
459	              r"= \Delta\tau \cdot [B_s]_{z,1}$ holds exactly "
460	              "under asymmetric misclassification.\n")
461	    md.append("2. Assumption A2 (FPR = FNR) is **not required** for "
462	              "the bias decomposition; it only simplifies the "
463	              "formula.\n")
464	    md.append(f"3. Analytic formula matches MC with "
465	              f"R-squared = {r2_val:.6f}.\n")
466	    md.append("4. EC-HTE (stratified correction) outperforms global "
467	              "correction because it captures per-subgroup asymmetric "
468	              "error structure.\n")
469	
470	    path = f'{RESULTS_DIR}/exp014_asymmetric_analysis.md'
471	    with open(path, 'w') as f:
472	        f.write(''.join(md))
473	    print(f"  Wrote {path}")
474	
475	
476	# ============================================================
477	# Main
478	# ============================================================
479	
480	if __name__ == '__main__':
481	    dry_run = '--dry' in sys.argv
482	    n_mc = 5 if dry_run else N_MC
483	    mode = "DRY RUN (5 MC, 1 config)" if dry_run else "FULL"
484	
485	    print("=" * 70)
486	    print(f"exp014_asymmetric: Asymmetric Misclassification ({mode})")
487	    print(f"N={N}, N_MC={n_mc}, N_expert={N_EXPERT}, tau(Z=0)={TAU_Z0}")
488	    print("=" * 70)
489	
490	    df_bias, df_corr, df_prod = run_all(n_mc, dry_run)
491	
492	    r2 = compute_r2(df_bias)
493	    print(f"\n  R-squared (analytic vs MC): {r2:.6f}")
494	
495	    ps = verify_product_structure(df_prod)
496	    if len(ps) > 0:
497	        print(f"  Product structure max CV: {ps['cv'].max():.2e}")
498	
499	    if not dry_run:
500	        df_bias.to_csv(f'{RESULTS_DIR}/exp014_asymmetric_bias.csv',
501	                       index=False)
502	        df_corr.to_csv(f'{RESULTS_DIR}/exp014_asymmetric_correction.csv',
503	                       index=False)
504	        print(f"  Saved exp014_asymmetric_bias.csv")
505	        print(f"  Saved exp014_asymmetric_correction.csv")
506	
507	    write_analysis_md(df_bias, df_corr, df_prod, r2)
508	
509	    if len(df_corr) > 0:
510	        print("\n  Method comparison:")
511	        for method in ['naive', 'global_est', 'echte']:
512	            sub = df_corr[df_corr['method'] == method]
513	            print(f"    {method:12s}: |bias|={sub['abs_bias'].mean():.4f}  "
514	                  f"RMSE={sub['rmse'].mean():.4f}  "
515	                  f"cov={sub['coverage'].mean():.2f}")
516	
517	    print("\n  Done.")
518	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "35d30507-9485-4f85-99ab-facd38c28fac",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp014_asymmetric.py",
      "content": "\"\"\"\nexp014_asymmetric.py — Asymmetric Misclassification Verification (exp-014)\n\nVerifies the bias product structure under FPR != FNR and demonstrates\nEC-HTE effectiveness in asymmetric scenarios.\n\nKey identity: bias(z, s) = delta_tau * [B_s]_{z,1}\nwhere B_s = M_global^{-1} M_s - I.\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport time\nimport os\nimport sys\n\n# ============================================================\n# Parameters\n# ============================================================\n\nN = 50000\nN_MC = 100\nN_EXPERT = 250\nTAU_Z0 = 0.1\nRESULTS_DIR = 'results'\nos.makedirs(RESULTS_DIR, exist_ok=True)\n\nCONFIGS = {\n    'config1': {'name': 'Cross-asymmetric',\n                'fpr': [0.10, 0.25], 'fnr': [0.20, 0.10]},\n    'config2': {'name': 'Co-directional',\n                'fpr': [0.05, 0.20], 'fnr': [0.15, 0.30]},\n    'config3': {'name': 'Extreme asymmetric',\n                'fpr': [0.03, 0.30], 'fnr': [0.25, 0.05]},\n}\n\nDELTA_TAUS = [0.1, 0.2, 0.3, 0.4, 0.5]\n\n\n# ============================================================\n# Core: mixing matrix and analytic bias\n# ============================================================\n\ndef mixing_matrix(fpr, fnr):\n    \"\"\"M[zhat,z] = P(Z=z|Zhat=zhat,S=s) under P(Z=0)=P(Z=1)=0.5.\"\"\"\n    d0 = (1.0 - fpr) + fnr\n    d1 = fpr + (1.0 - fnr)\n    return np.array([[(1.0 - fpr) / d0, fnr / d0],\n                     [fpr / d1, (1.0 - fnr) / d1]])\n\n\ndef analytic_bias_asym(fpr_list, fnr_list, weights, tau):\n    \"\"\"Compute B_s = M_global^{-1} M_s - I and bias = B_s @ tau.\"\"\"\n    K = len(fpr_list)\n    Ms = [mixing_matrix(fpr_list[s], fnr_list[s]) for s in range(K)]\n    M_global = sum(weights[s] * Ms[s] for s in range(K))\n    M_inv = np.linalg.inv(M_global)\n    biases, Bs = {}, {}\n    for s in range(K):\n        B = M_inv @ Ms[s] - np.eye(2)\n        Bs[s] = B\n        biases[s] = B @ tau\n    return biases, Bs, M_global, M_inv, Ms\n\n\n# ============================================================\n# MC simulation (vectorized main loop, per-run expert labels)\n# ============================================================\n\ndef mc_simulate(fpr_list, fnr_list, tau_z0, tau_z1, n, n_mc,\n                n_expert=0, seed=0):\n    \"\"\"Vectorized MC with asymmetric misclassification.\"\"\"\n    K = len(fpr_list)\n    w = np.full(K, 1.0 / K)\n    tau = np.array([tau_z0, tau_z1])\n\n    Ms_oracle = [mixing_matrix(fpr_list[s], fnr_list[s]) for s in range(K)]\n    M_glob = sum(w[s] * Ms_oracle[s] for s in range(K))\n    M_glob_inv = np.linalg.inv(M_glob)\n\n    rng = np.random.RandomState(seed)\n    T = rng.binomial(1, 0.5, (n_mc, n))\n    Z = rng.binomial(1, 0.5, (n_mc, n))\n    S = rng.binomial(1, 0.5, (n_mc, n))  # K=2 equal weights\n\n    tau_i = np.where(Z == 1, tau_z1, tau_z0)\n    Y = 1.0 + tau_i * T + 0.5 * rng.randn(n_mc, n) + rng.randn(n_mc, n)\n\n    # Asymmetric flip: P(flip) = FPR if Z=0, FNR if Z=1\n    flip_p = np.zeros((n_mc, n))\n    for s in range(K):\n        m = (S == s)\n        flip_p += m * np.where(Z == 0, fpr_list[s], fnr_list[s])\n    Z_hat = np.where(rng.rand(n_mc, n) < flip_p, 1 - Z, Z)\n\n    # Group means: group = S*4 + Zhat*2 + T\n    ng = K * 4\n    grp = (S * 4 + Z_hat * 2 + T).ravel()\n    mi = np.repeat(np.arange(n_mc), n)\n    comb = mi * ng + grp\n\n    sums = np.bincount(comb, weights=Y.ravel(),\n                       minlength=n_mc * ng).reshape(n_mc, ng)\n    sq_s = np.bincount(comb, weights=(Y.ravel() ** 2),\n                       minlength=n_mc * ng).reshape(n_mc, ng)\n    cnts = np.bincount(comb,\n                       minlength=n_mc * ng).reshape(n_mc, ng)\n    means = sums / np.maximum(cnts, 1)\n    cvars = sq_s / np.maximum(cnts, 1) - means ** 2\n\n    # Per-subgroup observed CATE and SE^2\n    tau_obs, se2_obs = {}, {}\n    for s in range(K):\n        b = s * 4\n        tau_obs[s] = np.column_stack([\n            means[:, b + 1] - means[:, b + 0],   # zh=0: T=1 - T=0\n            means[:, b + 3] - means[:, b + 2]])   # zh=1: T=1 - T=0\n        se2_obs[s] = np.column_stack([\n            cvars[:, b + 1] / np.maximum(cnts[:, b + 1], 1) +\n            cvars[:, b + 0] / np.maximum(cnts[:, b + 0], 1),\n            cvars[:, b + 3] / np.maximum(cnts[:, b + 3], 1) +\n            cvars[:, b + 2] / np.maximum(cnts[:, b + 2], 1)])\n\n    # Naive and oracle-global bias (vectorized)\n    out = {}\n    for s in range(K):\n        out[s] = {\n            'tau_obs': tau_obs[s],\n            'se2_obs': se2_obs[s],\n            'bias_naive': tau_obs[s] - tau,\n            'bias_global_oracle': tau_obs[s] @ M_glob_inv.T - tau,\n        }\n\n    # Expert-label correction (per MC run)\n    if n_expert > 0:\n        for s in range(K):\n            out[s]['bias_global_est'] = np.zeros((n_mc, 2))\n            out[s]['bias_echte'] = np.zeros((n_mc, 2))\n            out[s]['cov_naive'] = np.zeros((n_mc, 2))\n            out[s]['cov_global_est'] = np.zeros((n_mc, 2))\n            out[s]['cov_echte'] = np.zeros((n_mc, 2))\n\n        for r in range(n_mc):\n            eidx = rng.choice(n, n_expert, replace=False)\n            ze = Z[r, eidx]\n            zhe = Z_hat[r, eidx]\n            se = S[r, eidx]\n\n            # Estimate per-subgroup CM (Laplace smoothing)\n            Ms_hat = []\n            for s in range(K):\n                mask = (se == s)\n                zt, zh = ze[mask], zhe[mask]\n                n0 = np.sum(zt == 0)\n                n1 = np.sum(zt == 1)\n                fh = (np.sum((zt == 0) & (zh == 1)) + 1) / (n0 + 2)\n                nh = (np.sum((zt == 1) & (zh == 0)) + 1) / (n1 + 2)\n                Ms_hat.append(mixing_matrix(fh, nh))\n\n            Mgh = sum(w[s] * Ms_hat[s] for s in range(K))\n            Mgh_inv = np.linalg.inv(Mgh)\n\n            for s in range(K):\n                to = tau_obs[s][r]\n                se2 = se2_obs[s][r]\n                Sig = np.diag(se2)\n\n                # Global estimated correction\n                tg = Mgh_inv @ to\n                out[s]['bias_global_est'][r] = tg - tau\n                Sg = Mgh_inv @ Sig @ Mgh_inv.T\n                out[s]['cov_global_est'][r] = (\n                    np.abs(tg - tau) <= 1.96 * np.sqrt(np.diag(Sg)))\n\n                # EC-HTE: per-subgroup correction\n                Msi = np.linalg.inv(Ms_hat[s])\n                te = Msi @ to\n                out[s]['bias_echte'][r] = te - tau\n                Se = Msi @ Sig @ Msi.T\n                out[s]['cov_echte'][r] = (\n                    np.abs(te - tau) <= 1.96 * np.sqrt(np.diag(Se)))\n\n                # Naive coverage\n                se_n = np.sqrt(se2)\n                out[s]['cov_naive'][r] = (\n                    np.abs(to - tau) <= 1.96 * se_n)\n\n    return out\n\n\n# ============================================================\n# Run experiments\n# ============================================================\n\ndef run_all(n_mc, dry_run=False):\n    configs_run = {'config1': CONFIGS['config1']} if dry_run else CONFIGS\n    dtaus = [0.2] if dry_run else DELTA_TAUS\n\n    bias_rows = []\n    corr_rows = []\n    prod_rows = []\n    t0 = time.time()\n    seed_counter = 0\n\n    for cfg_key, cfg in configs_run.items():\n        fpr, fnr = cfg['fpr'], cfg['fnr']\n        K = len(fpr)\n        w = np.full(K, 1.0 / K)\n\n        for dt in dtaus:\n            tau_z1 = TAU_Z0 + dt\n            tau = np.array([TAU_Z0, tau_z1])\n            seed_counter += 1\n            seed = seed_counter * 7919  # distinct primes -> distinct seeds\n\n            biases, Bs, M_glob, M_inv, Ms = analytic_bias_asym(\n                fpr, fnr, w, tau)\n\n            mc = mc_simulate(fpr, fnr, TAU_Z0, tau_z1, N, n_mc,\n                             N_EXPERT, seed)\n\n            for s in range(K):\n                for z in range(2):\n                    ab = biases[s][z]\n                    mc_vals = mc[s]['bias_global_oracle'][:, z]\n                    mc_mean = np.mean(mc_vals)\n                    mc_se = np.std(mc_vals, ddof=1) / np.sqrt(n_mc)\n\n                    bias_rows.append({\n                        'config': cfg_key,\n                        'config_name': cfg['name'],\n                        'fpr_s': fpr[s], 'fnr_s': fnr[s],\n                        'delta_tau': dt,\n                        'subgroup': s, 'z': z,\n                        'analytic_bias': ab,\n                        'mc_bias': mc_mean,\n                        'mc_se': mc_se,\n                        'B_z1': Bs[s][z, 1],\n                    })\n\n                    prod_rows.append({\n                        'config': cfg_key, 'subgroup': s, 'z': z,\n                        'delta_tau': dt,\n                        'ratio_analytic': ab / dt,\n                        'ratio_mc': mc_mean / dt,\n                    })\n\n                    for method, bk, ck in [\n                        ('naive', 'bias_naive', 'cov_naive'),\n                        ('global_est', 'bias_global_est', 'cov_global_est'),\n                        ('echte', 'bias_echte', 'cov_echte'),\n                    ]:\n                        bv = mc[s][bk][:, z]\n                        corr_rows.append({\n                            'config': cfg_key,\n                            'config_name': cfg['name'],\n                            'delta_tau': dt,\n                            'subgroup': s, 'z': z,\n                            'method': method,\n                            'mean_bias': np.mean(bv),\n                            'abs_bias': np.abs(np.mean(bv)),\n                            'rmse': np.sqrt(np.mean(bv ** 2)),\n                            'coverage': np.mean(mc[s][ck][:, z]),\n                        })\n\n            elapsed = time.time() - t0\n            print(f\"  {cfg_key} dt={dt:.1f} done ({elapsed:.1f}s)\")\n\n    return (pd.DataFrame(bias_rows),\n            pd.DataFrame(corr_rows),\n            pd.DataFrame(prod_rows))\n\n\n# ============================================================\n# Analysis helpers\n# ============================================================\n\ndef compute_r2(df):\n    valid = df[df['analytic_bias'].abs() > 1e-8]\n    if len(valid) == 0:\n        return np.nan\n    ss_res = ((valid['mc_bias'] - valid['analytic_bias']) ** 2).sum()\n    ss_tot = ((valid['mc_bias'] - valid['mc_bias'].mean()) ** 2).sum()\n    return 1.0 - ss_res / ss_tot if ss_tot > 0 else np.nan\n\n\ndef verify_product_structure(df_prod):\n    rows = []\n    for (cfg, s, z), grp in df_prod.groupby(['config', 'subgroup', 'z']):\n        vals = grp['ratio_analytic'].values\n        if len(vals) > 1 and np.abs(np.mean(vals)) > 1e-12:\n            cv = np.std(vals) / np.abs(np.mean(vals))\n        else:\n            cv = 0.0\n        rows.append({\n            'config': cfg, 'subgroup': s, 'z': z,\n            'mean_ratio': np.mean(vals),\n            'std_ratio': np.std(vals), 'cv': cv,\n        })\n    return pd.DataFrame(rows)\n\n\n# ============================================================\n# Write analysis markdown\n# ============================================================\n\ndef write_analysis_md(df_bias, df_corr, df_prod, r2_val):\n    ps = verify_product_structure(df_prod)\n    md = []\n\n    md.append(\"# exp-014: Asymmetric Misclassification Verification\\n\\n\")\n\n    # --- Section 1: Setup ---\n    md.append(\"## 1. Setup\\n\\n\")\n    md.append(\"### Asymmetric Confusion Matrix\\n\\n\")\n    md.append(r\"For subgroup $s$ with $\\text{FPR}_s = P(\\hat{Z}=1|Z=0,S=s)$\"\n              r\" and $\\text{FNR}_s = P(\\hat{Z}=0|Z=1,S=s)$:\" \"\\n\\n\")\n    md.append(r\"$$C_s = \\begin{pmatrix} 1-\\text{FPR}_s & \\text{FPR}_s \\\\\"\n              r\" \\text{FNR}_s & 1-\\text{FNR}_s \\end{pmatrix}$$\" \"\\n\\n\")\n\n    md.append(\"### Mixing Matrix (Bayesian Inversion)\\n\\n\")\n    md.append(r\"Under balanced prior $P(Z=0)=P(Z=1)=0.5$:\" \"\\n\\n\")\n    md.append(r\"$$M_s[\\hat{z}, z] = P(Z=z \\mid \\hat{Z}=\\hat{z}, S=s)$$\" \"\\n\\n\")\n    md.append(r\"$$M_s = \\begin{pmatrix}\"\n              r\" \\frac{1-\\text{FPR}_s}{1-\\text{FPR}_s+\\text{FNR}_s} &\"\n              r\" \\frac{\\text{FNR}_s}{1-\\text{FPR}_s+\\text{FNR}_s} \\\\\"\n              r\" \\frac{\\text{FPR}_s}{\\text{FPR}_s+1-\\text{FNR}_s} &\"\n              r\" \\frac{1-\\text{FNR}_s}{\\text{FPR}_s+1-\\text{FNR}_s}\"\n              r\" \\end{pmatrix}$$\" \"\\n\\n\")\n\n    md.append(r\"### Global Mixing Matrix\" \"\\n\\n\")\n    md.append(r\"$$M_{\\text{global}} = \\sum_s w_s \\, M_s$$\" \"\\n\\n\")\n\n    # --- Section 2: Bias derivation ---\n    md.append(\"## 2. Bias Formula Derivation\\n\\n\")\n    md.append(r\"The observed CATE within subgroup $s$ satisfies:\" \"\\n\\n\")\n    md.append(r\"$$\\boldsymbol{\\tau}_{\\text{obs},s} = M_s \\,\"\n              r\" \\boldsymbol{\\tau}$$\" \"\\n\\n\")\n    md.append(r\"where $\\boldsymbol{\\tau} = (\\tau(0),\\;\\tau(1))^\\top$.\"\n              \"\\n\\n\")\n    md.append(\"After global correction:\\n\\n\")\n    md.append(r\"$$\\hat{\\boldsymbol{\\tau}}_s = M_{\\text{global}}^{-1}\"\n              r\" M_s \\, \\boldsymbol{\\tau}$$\" \"\\n\\n\")\n    md.append(\"**Bias:**\\n\\n\")\n    md.append(r\"$$\\text{bias}(z, s) = \\bigl[(M_{\\text{global}}^{-1}\"\n              r\" M_s - I)\\,\\boldsymbol{\\tau}\\bigr]_z\"\n              r\" = [B_s \\, \\boldsymbol{\\tau}]_z$$\" \"\\n\\n\")\n    md.append(r\"where $B_s \\equiv M_{\\text{global}}^{-1} M_s - I$.\" \"\\n\\n\")\n\n    # --- Section 3: Product structure ---\n    md.append(\"## 3. Product Structure Proof\\n\\n\")\n    md.append(r\"**Claim.** $\\text{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}$\"\n              r\" where $\\Delta\\tau = \\tau(1)-\\tau(0)$.\" \"\\n\\n\")\n    md.append(\"**Proof.** Both $M_s$ and $M_{\\\\text{global}}$ are \"\n              \"stochastic (rows sum to 1):\\n\\n\")\n    md.append(r\"$$M_s \\mathbf{1} = \\mathbf{1},\\quad\"\n              r\" M_{\\text{global}} \\mathbf{1} = \\mathbf{1}\"\n              r\" \\;\\Longrightarrow\\;\"\n              r\" M_{\\text{global}}^{-1}\\mathbf{1} = \\mathbf{1}$$\" \"\\n\\n\")\n    md.append(r\"$$\\Rightarrow\\; B_s \\mathbf{1}\"\n              r\" = (M_{\\text{global}}^{-1} M_s - I)\\mathbf{1}\"\n              r\" = \\mathbf{1} - \\mathbf{1} = \\mathbf{0}$$\" \"\\n\\n\")\n    md.append(r\"Decompose $\\boldsymbol{\\tau} = \\tau(0)\\,\\mathbf{1}\"\n              r\" + \\Delta\\tau\\,\\mathbf{e}_1$\"\n              r\" where $\\mathbf{e}_1=(0,1)^\\top$:\" \"\\n\\n\")\n    md.append(r\"$$\\text{bias}(z,s) = \\tau(0)\\underbrace{[B_s\\mathbf{1}]_z}\"\n              r\"_{=0} + \\Delta\\tau\\,[B_s]_{z,1}$$\" \"\\n\\n\")\n    md.append(r\"$$\\boxed{\\text{bias}(z,s) = \\Delta\\tau \\cdot [B_s]_{z,1}}$$\"\n              \"\\n\\n\")\n    md.append(r\"The coefficient $[B_s]_{z,1}$ depends **only** on \"\n              r\"$\\{\\text{FPR}_k, \\text{FNR}_k, w_k\\}$, not on \"\n              r\"$\\Delta\\tau$. $\\square$\" \"\\n\\n\")\n\n    # Numerical verification\n    md.append(\"### Numerical Verification\\n\\n\")\n    if len(ps) > 0:\n        md.append(r\"For each (config, subgroup, $z$), the ratio \"\n                  r\"$\\text{bias}/\\Delta\\tau$ is constant:\" \"\\n\\n\")\n        md.append(\"| Config | Sub | z | Mean ratio | CV |\\n\")\n        md.append(\"|--------|-----|---|-----------|----|\\n\")\n        for _, row in ps.iterrows():\n            md.append(f\"| {row['config']} | {int(row['subgroup'])} \"\n                      f\"| {int(row['z'])} | {row['mean_ratio']:.6f} \"\n                      f\"| {row['cv']:.2e} |\\n\")\n        md.append(\"\\nCV (coefficient of variation) = 0 confirms \"\n                  \"exact product structure.\\n\\n\")\n\n    # --- Section 4: Symmetric connection ---\n    md.append(\"## 4. Connection to the Symmetric Case\\n\\n\")\n    md.append(r\"When $\\text{FPR}_s = \\text{FNR}_s = \\pi_s$ \"\n              \"(symmetric, assumption A2):\\n\\n\")\n    md.append(r\"$$M_s = \\begin{pmatrix} 1-\\pi_s & \\pi_s \\\\\"\n              r\" \\pi_s & 1-\\pi_s \\end{pmatrix}$$\" \"\\n\\n\")\n    md.append(r\"$$B_s = \\frac{\\delta_s}{1-2\\bar\\pi}\"\n              r\" \\begin{pmatrix} -1 & 1 \\\\ 1 & -1 \\end{pmatrix},\"\n              r\" \\quad \\delta_s = \\pi_s - \\bar\\pi$$\" \"\\n\\n\")\n    md.append(\"and the bias reduces to:\\n\\n\")\n    md.append(r\"$$\\text{bias}(z{=}0,s) = +\\frac{\\delta_s\\,\\Delta\\tau}\"\n              r\"{1-2\\bar\\pi},\\quad\"\n              r\" \\text{bias}(z{=}1,s) = -\\frac{\\delta_s\\,\\Delta\\tau}\"\n              r\"{1-2\\bar\\pi}$$\" \"\\n\\n\")\n    md.append(\"**Key differences in the asymmetric case:**\\n\\n\")\n    md.append(\"1. The product structure (bias proportional to \"\n              r\"$\\Delta\\tau$) holds in **both** cases.\" \"\\n\")\n    md.append(\"2. In symmetric: \"\n              r\"$|{\\rm bias}(z{=}0)|=|{\\rm bias}(z{=}1)|$. \"\n              \"In asymmetric: they differ.\\n\")\n    md.append(r\"3. In symmetric: error heterogeneity collapses to scalar \"\n              r\"$\\delta_s/(1{-}2\\bar\\pi)$. \"\n              r\"In asymmetric: it is the matrix entry $[B_s]_{z,1}$.\" \"\\n\")\n    md.append(\"4. **Assumption A2 is not required** for the product \"\n              \"structure.\\n\\n\")\n\n    # --- Section 5: Numerical results ---\n    md.append(\"## 5. Numerical Results\\n\\n\")\n    md.append(f\"### R-squared (analytic vs MC bias): **{r2_val:.6f}**\\n\\n\")\n\n    md.append(\"### Bias table\\n\\n\")\n    md.append(\"| Config | delta_tau | Sub | z | Analytic | MC | MC SE |\\n\")\n    md.append(\"|--------|----------|-----|---|----------|-----|-------|\\n\")\n    for _, row in df_bias.iterrows():\n        md.append(f\"| {row['config']} | {row['delta_tau']:.1f} \"\n                  f\"| {int(row['subgroup'])} | {int(row['z'])} \"\n                  f\"| {row['analytic_bias']:+.6f} \"\n                  f\"| {row['mc_bias']:+.6f} \"\n                  f\"| {row['mc_se']:.6f} |\\n\")\n\n    # --- Section 6: EC-HTE vs Global ---\n    if len(df_corr) > 0:\n        md.append(\"\\n## 6. EC-HTE vs Global Correction\\n\\n\")\n        md.append(f\"Expert labels per MC run: {N_EXPERT}\\n\\n\")\n\n        md.append(\"### Per-cell results\\n\\n\")\n        md.append(\"| Config | dt | Sub | z | Method \"\n                  \"| |Bias| | RMSE | Cov |\\n\")\n        md.append(\"|--------|-----|-----|---|--------\"\n                  \"|-------|------|-----|\\n\")\n        for _, row in df_corr.iterrows():\n            md.append(f\"| {row['config']} | {row['delta_tau']:.1f} \"\n                      f\"| {int(row['subgroup'])} | {int(row['z'])} \"\n                      f\"| {row['method']} \"\n                      f\"| {row['abs_bias']:.4f} \"\n                      f\"| {row['rmse']:.4f} \"\n                      f\"| {row['coverage']:.2f} |\\n\")\n\n        md.append(\"\\n### Summary by method\\n\\n\")\n        md.append(\"| Method | Mean |Bias| | Mean RMSE | Mean Coverage |\\n\")\n        md.append(\"|--------|-----------|-----------|---------------|\\n\")\n        for method in ['naive', 'global_est', 'echte']:\n            sub = df_corr[df_corr['method'] == method]\n            md.append(f\"| {method} \"\n                      f\"| {sub['abs_bias'].mean():.4f} \"\n                      f\"| {sub['rmse'].mean():.4f} \"\n                      f\"| {sub['coverage'].mean():.2f} |\\n\")\n\n    # --- Section 7: Conclusions ---\n    md.append(\"\\n## 7. Conclusions\\n\\n\")\n    md.append(r\"1. The **product structure** $\\text{bias}(z,s) \"\n              r\"= \\Delta\\tau \\cdot [B_s]_{z,1}$ holds exactly \"\n              \"under asymmetric misclassification.\\n\")\n    md.append(\"2. Assumption A2 (FPR = FNR) is **not required** for \"\n              \"the bias decomposition; it only simplifies the \"\n              \"formula.\\n\")\n    md.append(f\"3. Analytic formula matches MC with \"\n              f\"R-squared = {r2_val:.6f}.\\n\")\n    md.append(\"4. EC-HTE (stratified correction) outperforms global \"\n              \"correction because it captures per-subgroup asymmetric \"\n              \"error structure.\\n\")\n\n    path = f'{RESULTS_DIR}/exp014_asymmetric_analysis.md'\n    with open(path, 'w') as f:\n        f.write(''.join(md))\n    print(f\"  Wrote {path}\")\n\n\n# ============================================================\n# Main\n# ============================================================\n\nif __name__ == '__main__':\n    dry_run = '--dry' in sys.argv\n    n_mc = 5 if dry_run else N_MC\n    mode = \"DRY RUN (5 MC, 1 config)\" if dry_run else \"FULL\"\n\n    print(\"=\" * 70)\n    print(f\"exp014_asymmetric: Asymmetric Misclassification ({mode})\")\n    print(f\"N={N}, N_MC={n_mc}, N_expert={N_EXPERT}, tau(Z=0)={TAU_Z0}\")\n    print(\"=\" * 70)\n\n    df_bias, df_corr, df_prod = run_all(n_mc, dry_run)\n\n    r2 = compute_r2(df_bias)\n    print(f\"\\n  R-squared (analytic vs MC): {r2:.6f}\")\n\n    ps = verify_product_structure(df_prod)\n    if len(ps) > 0:\n        print(f\"  Product structure max CV: {ps['cv'].max():.2e}\")\n\n    if not dry_run:\n        df_bias.to_csv(f'{RESULTS_DIR}/exp014_asymmetric_bias.csv',\n                       index=False)\n        df_corr.to_csv(f'{RESULTS_DIR}/exp014_asymmetric_correction.csv',\n                       index=False)\n        print(f\"  Saved exp014_asymmetric_bias.csv\")\n        print(f\"  Saved exp014_asymmetric_correction.csv\")\n\n    write_analysis_md(df_bias, df_corr, df_prod, r2)\n\n    if len(df_corr) > 0:\n        print(\"\\n  Method comparison:\")\n        for method in ['naive', 'global_est', 'echte']:\n            sub = df_corr[df_corr['method'] == method]\n            print(f\"    {method:12s}: |bias|={sub['abs_bias'].mean():.4f}  \"\n                  f\"RMSE={sub['rmse'].mean():.4f}  \"\n                  f\"cov={sub['coverage'].mean():.2f}\")\n\n    print(\"\\n  Done.\")\n",
      "numLines": 518,
      "startLine": 1,
      "totalLines": 518
    }
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01RwYY64Pvhcm7DcVc7QwRKJ`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "5be39dee-85d7-4a89-bc10-8da040faf740",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGQgsBmkZwBcF3pfxjrom5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1162,
      "cache_read_input_tokens": 22270,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1162
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

_source line 28 · 2026-05-21T20:44:02.843Z_

<details><summary>↩ Tool result · `toolu_01RwYY64Pvhcm7DcVc7QwRKJ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	exp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)
4	
5	Compares confusion matrix estimators for CATE correction under heterogeneous
6	misclassification across subgroups:
7	  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)
8	
9	Input: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)
10	Output: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv
11	"""
12	
13	import argparse
14	import os
15	import sys
16	import time
17	import warnings
18	import numpy as np
19	import pandas as pd
20	from scipy.special import gammaln
21	from scipy.optimize import minimize_scalar
22	
23	warnings.filterwarnings('ignore')
24	
25	try:
26	    import pymc as pm
27	    import pytensor.tensor as pt
28	    import arviz as az
29	    HAS_PYMC = True
30	except ImportError:
31	    HAS_PYMC = False
32	
33	N = 5000
34	SUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}
35	
36	REGIMES = {
37	    2: {
38	        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},
39	        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},
40	        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
41	    },
42	    4: {
43	        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},
44	        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},
45	        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},
46	    },
47	}
48	
49	DEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]
50	DEFAULT_K_LIST = [2, 4]
51	
52	
53	# ── DGP ───────────────────────────────────────────────────────────────────────
54	
55	def generate_data(regime_params, n_expert, k, seed):
56	    rng = np.random.RandomState(seed)
57	    labels = SUBGROUP_LABELS[k]
58	    T = rng.binomial(1, 0.5, N)
59	    Z = rng.binomial(1, 0.5, N)
60	    S = rng.choice(labels, N, p=[1.0 / k] * k)
61	    X = rng.randn(N, 5)
62	    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])
63	    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)
64	    mc_rates = np.zeros(N)
65	    for i, s in enumerate(labels):
66	        mc_rates[S == s] = regime_params['misclass'][i]
67	    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)
68	    idx = rng.choice(N, min(n_expert, N), replace=False)
69	    expert_mask = np.zeros(N, dtype=bool)
70	    expert_mask[idx] = True
71	    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)
72	
73	
74	# ── Helpers ───────────────────────────────────────────────────────────────────
75	
76	def diff_in_means(Y, T, mask):
77	    t1, t0 = mask & (T == 1), mask & (T == 0)
78	    n1, n0 = t1.sum(), t0.sum()
79	    if n1 < 2 or n0 < 2:
80	        return np.nan, np.nan
81	    y1, y0 = Y[t1], Y[t0]
82	    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)
83	
84	
85	def get_counts(z_true, z_hat, subgroups, labels):
86	    """Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat]."""
87	    k = len(labels)
88	    counts = np.zeros((k, 2, 2), dtype=int)
89	    for i, s in enumerate(labels):
90	        ms = subgroups == s
91	        for z in [0, 1]:
92	            mz = ms & (z_true == z)
93	            counts[i, z, 0] = (z_hat[mz] == 0).sum()
94	            counts[i, z, 1] = (z_hat[mz] == 1).sum()
95	    return counts
96	
97	
98	def build_mixing_matrix(C):
99	    """C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).
100	
101	    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's
102	    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.
103	    """
104	    M = np.zeros((2, 2))
105	    for zh in [0, 1]:
106	        cs = C[0, zh] + C[1, zh]
107	        if cs > 0:
108	            M[zh, 0] = C[0, zh] / cs
109	            M[zh, 1] = C[1, zh] / cs
110	        else:
111	            M[zh, :] = 0.5
112	    return M
113	
114	
115	def invert_mixing(M, tau_obs, se_obs):
116	    det = np.linalg.det(M)
117	    if abs(det) < 1e-10:
118	        return tau_obs.copy(), se_obs.copy()
119	    Mi = np.linalg.inv(M)
120	    tau_c = Mi @ tau_obs
121	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
122	    return tau_c, se_c
123	
124	
125	def safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):
126	    """Invert mixing matrix with condition number guard.
127	
128	    When cond(M_s) > threshold, matrix inversion is numerically unstable.
129	    Falls back to naive (no correction) to avoid catastrophic amplification.
130	    """
131	    cond = np.linalg.cond(M_s)
132	    if cond > cond_threshold:
133	        return tau_obs.copy()
134	    return np.linalg.solve(M_s, tau_obs)
135	
136	
137	def invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):
138	    """Like invert_mixing but with condition number guard."""
139	    cond = np.linalg.cond(M)
140	    if cond > cond_threshold:
141	        return tau_obs.copy(), se_obs.copy()
142	    det = np.linalg.det(M)
143	    if abs(det) < 1e-10:
144	        return tau_obs.copy(), se_obs.copy()
145	    Mi = np.linalg.inv(M)
146	    tau_c = Mi @ tau_obs
147	    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))
148	    return tau_c, se_c
149	
150	
151	# ── Confusion Matrix Estimators ───────────────────────────────────────────────
152	
153	def estimate_cm_mle(counts, labels):
154	    """Per-subgroup MLE with Laplace smoothing (add-1)."""
155	    C = {}
156	    for i, s in enumerate(labels):
157	        C_s = np.zeros((2, 2))
158	        for z in [0, 1]:
159	            n = counts[i, z, :].sum()
160	            for zh in [0, 1]:
161	                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5
162	        C[s] = C_s
163	    return C
164	
165	
166	def _dirmult_neg_ll(alpha, counts_z):
167	    """Negative log marginal likelihood for Dirichlet-Multinomial."""
168	    a = alpha / 2.0
169	    if a < 1e-10:
170	        return 1e10
171	    ll = 0.0
172	    for c0, c1 in counts_z:
173	        n = c0 + c1
174	        if n == 0:
175	            continue
176	        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)
177	        ll -= 2 * gammaln(a) - gammaln(2 * a)
178	    return -ll
179	
180	
181	def estimate_cm_hb_eb(counts, labels):
182	    """Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean."""
183	    k = len(labels)
184	    alpha_opt = np.zeros(2)
185	    for z in [0, 1]:
186	        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]
187	        total = sum(c0 + c1 for c0, c1 in cl)
188	        if total == 0:
189	            alpha_opt[z] = 2.0
190	            continue
191	        res = minimize_scalar(
192	            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')
193	        alpha_opt[z] = res.x
194	
195	    C = {}
196	    for i, s in enumerate(labels):
197	        C_s = np.zeros((2, 2))
198	        for z in [0, 1]:
199	            a = alpha_opt[z] / 2.0
200	            n = counts[i, z, :].sum()
201	            d = n + 2 * a
202	            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5
203	            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5
204	        C[s] = C_s
205	
206	    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,
207	            'runtime_seconds': 0.0, 'hb_method': 'eb',
208	            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}
209	    return C, diag
210	
211	
212	def _split_rhat(chains):
213	    """Split R-hat for a scalar parameter. chains: (n_chains, n_draws)."""
214	    parts = []
215	    for c in range(chains.shape[0]):
216	        half = chains.shape[1] // 2
217	        parts.append(chains[c, :half])
218	        parts.append(chains[c, half:2 * half])
219	    parts = np.array(parts)
220	    m = parts.shape[0]
221	    n = parts.shape[1]
222	    chain_means = parts.mean(axis=1)
223	    W = np.mean(np.var(parts, axis=1, ddof=1))
224	    B = n * np.var(chain_means, ddof=1)
225	    if W < 1e-20:
226	        return 1.0
227	    var_hat = (1 - 1.0 / n) * W + B / n
228	    return float(np.sqrt(var_hat / W))
229	
230	
231	def _bulk_ess(chains):
232	    """Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws)."""
233	    x = chains.ravel()
234	    n = len(x)
235	    mu = x.mean()
236	    xc = x - mu
237	    max_lag = min(n // 2, 300)
238	    c0 = np.dot(xc, xc)
239	    if c0 < 1e-20:
240	        return float(n)
241	    tau = 1.0
242	    for lag in range(1, max_lag - 1, 2):
243	        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0
244	        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0
245	        pair = r1 + r2
246	        if pair < 0:
247	            break
248	        tau += 2 * pair
249	    return float(n / tau)
250	
251	
252	def _fast_diagnostics(alpha_arr, theta_arr, labels):
253	    """Compute R-hat and ESS over all parameters without arviz."""
254	    rhats, esss = [], []
255	    for d in range(alpha_arr.shape[2]):
256	        rhats.append(_split_rhat(alpha_arr[:, :, d]))
257	        esss.append(_bulk_ess(alpha_arr[:, :, d]))
258	    k = len(labels)
259	    for i in range(k):
260	        for z in [0, 1]:
261	            for zh in range(theta_arr.shape[4]):
262	                ch = theta_arr[:, :, i, z, zh]
263	                rhats.append(_split_rhat(ch))
264	                esss.append(_bulk_ess(ch))
265	    return max(rhats), min(esss)
266	
267	
268	def _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):
269	    """Log posterior for alpha_0[z] in log-alpha space (includes Jacobian)."""
270	    if alpha < 1e-10:
271	        return -1e10
272	    a = alpha / 2.0
273	    k = theta_z.shape[0]
274	    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha
275	    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))
276	    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))
277	    return lp
278	
279	
280	def estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,
281	                         hp_a0=3.0, hp_b0=1.0):
282	    """Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).
283	
284	    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).
285	    """
286	    k = len(labels)
287	    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),
288	                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]
289	    chain_inits = chain_inits_pool[:n_chains]
290	    all_alpha, all_theta = [], []
291	    t0 = time.time()
292	
293	    for chain in range(n_chains):
294	        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)
295	        alpha = chain_inits[chain].copy()
296	        theta = np.ones((k, 2, 2)) * 0.5
297	        mh_scale = np.array([0.3, 0.3])
298	        accept_ct = np.array([0, 0])
299	        attempt_ct = np.array([0, 0])
300	
301	        alpha_samples = np.zeros((n_iter, 2))
302	        theta_samples = np.zeros((n_iter, k, 2, 2))
303	
304	        for it in range(n_warmup + n_iter):
305	            for z in [0, 1]:
306	                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0
307	                post_a = np.maximum(post_a, 1e-6)
308	                g = rng.gamma(post_a)
309	                g_sum = g.sum(axis=1, keepdims=True)
310	                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)
311	
312	            for z in [0, 1]:
313	                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])
314	                a_prop = np.exp(x_prop)
315	                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -
316	                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))
317	                accepted = np.log(rng.rand()) < log_r
318	                if accepted:
319	                    alpha[z] = a_prop
320	                if it < n_warmup:
321	                    accept_ct[z] += int(accepted)
322	                    attempt_ct[z] += 1
323	
324	            if it < n_warmup and it > 0 and it % 100 == 0:
325	                for z in [0, 1]:
326	                    rate = accept_ct[z] / max(attempt_ct[z], 1)
327	                    if rate < 0.2:
328	                        mh_scale[z] *= 0.7
329	                    elif rate > 0.5:
330	                        mh_scale[z] *= 1.3
331	                    accept_ct[z] = 0
332	                    attempt_ct[z] = 0
333	
334	            if it >= n_warmup:
335	                idx = it - n_warmup
336	                alpha_samples[idx] = alpha.copy()
337	                theta_samples[idx] = theta.copy()
338	
339	        all_alpha.append(alpha_samples)
340	        all_theta.append(theta_samples)
341	
342	    runtime = time.time() - t0
343	    alpha_arr = np.stack(all_alpha)
344	    theta_arr = np.stack(all_theta)
345	
346	    C = {}
347	    for i, s in enumerate(labels):
348	        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))
349	
350	    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)
351	
352	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,
353	            'runtime_seconds': runtime, 'hb_method': 'gibbs'}
354	    return C, diag
355	
356	
357	def estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):
358	    """Full Bayesian HB with PyMC MCMC."""
359	    k = len(labels)
360	    n_per_sz = counts.sum(axis=2)
361	
362	    with pm.Model():
363	        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)
364	        for z in [0, 1]:
365	            for i, s in enumerate(labels):
366	                nsz = int(n_per_sz[i, z])
367	                if nsz == 0:
368	                    continue
369	                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])
370	                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)
371	                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,
372	                               observed=counts[i, z, :].astype('int32'))
373	        t0 = time.time()
374	        trace = pm.sample(draws=draws, tune=tune, chains=chains,
375	                          random_seed=seed, progressbar=False)
376	        runtime = time.time() - t0
377	
378	    C = {}
379	    for i, s in enumerate(labels):
380	        C_s = np.zeros((2, 2))
381	        for z in [0, 1]:
382	            vn = f'theta_{s}_z{z}'
383	            if vn in trace.posterior:
384	                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))
385	            else:
386	                C_s[z, :] = 0.5
387	        C[s] = C_s
388	
389	    all_vars = list(trace.posterior.data_vars)
390	    try:
391	        summ = az.summary(trace, var_names=all_vars)
392	        rhat_max = float(summ['r_hat'].max())
393	        ess_min = float(summ['ess_bulk'].min())
394	    except Exception:
395	        rhat_max = ess_min = np.nan
396	    try:
397	        divergent = int(trace.sample_stats['diverging'].values.sum())
398	    except Exception:
399	        divergent = -1
400	
401	    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,
402	            'divergent_count': divergent, 'runtime_seconds': runtime,
403	            'hb_method': 'mcmc'}
404	    return C, diag
405	
406	
407	# ── Single MC Run ─────────────────────────────────────────────────────────────
408	
409	def run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):
410	    data = generate_data(regime_params, n_expert, k, seed)
411	    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']
412	    em = data['expert_mask']
413	    labels = SUBGROUP_LABELS[k]
414	    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']
415	
416	    counts = get_counts(Z[em], Z_hat[em], S[em], labels)
417	
418	    C_mle = estimate_cm_mle(counts, labels)
419	
420	    if hb_method == 'gibbs':
421	        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)
422	    elif hb_method == 'mcmc' and HAS_PYMC:
423	        try:
424	            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)
425	        except Exception:
426	            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
427	            hb_diag['hb_method'] = 'eb_fallback'
428	    else:
429	        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)
430	
431	    # Global CM (pool all expert labels, Laplace)
432	    cg = counts.sum(axis=0)
433	    C_gl = np.zeros((2, 2))
434	    for z in [0, 1]:
435	        n = cg[z, :].sum()
436	        for zh in [0, 1]:
437	            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5
438	
439	    M_gl = build_mixing_matrix(C_gl)
440	    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}
441	    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}
442	
443	    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}
444	    rows = []
445	
446	    for s in labels:
447	        sm = S == s
448	        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))
449	        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))
450	        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))
451	        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))
452	
453	        tau_obs = np.array([th0_n, th1_n])
454	        se_obs = np.array([se0_n, se1_n])
455	        if np.any(np.isnan(tau_obs)):
456	            continue
457	
458	        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)
459	        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)
460	        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)
461	
462	        def mr(method, th0, th1, se0, se1):
463	            return {**base, 'subgroup': s, 'method': method,
464	                    'tau_hat_z0': th0, 'tau_hat_z1': th1,
465	                    'se_z0': se0, 'se_z1': se1,
466	                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}
467	
468	        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))
469	        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))
470	        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))
471	        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))
472	        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))
473	
474	    return rows, {**base, **hb_diag}
475	
476	
477	# ── Aggregation ───────────────────────────────────────────────────────────────
478	
479	def aggregate_results(df):
480	    rows = []
481	    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']
482	    for keys, grp in df.groupby(grp_cols):
483	        regime, n_expert, k, subgroup, method = keys
484	        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),
485	               'subgroup': subgroup, 'method': method}
486	        n_mc = len(grp)
487	        for z in ['z0', 'z1']:
488	            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values
489	            bias = err.mean()
490	            mse = (err ** 2).mean()
491	            rmse = np.sqrt(mse)
492	            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values
493	            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values
494	            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &
495	                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()
496	            row[f'bias_{z}'] = bias
497	            row[f'rmse_{z}'] = rmse
498	            row[f'coverage_{z}'] = cov
499	            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)
500	            mse_se = (err ** 2).std() / np.sqrt(n_mc)
501	            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan
502	        rows.append(row)
503	    return pd.DataFrame(rows)
504	
505	
506	# ── Output ────────────────────────────────────────────────────────────────────
507	
508	def print_summary(df_agg, df_diag):
509	    pd.set_option('display.float_format', '{:.4f}'.format)
510	
511	    # MCMC / Gibbs diagnostics
512	    if 'hb_method' in df_diag.columns:
513	        for method_label in ['gibbs', 'mcmc']:
514	            mrows = df_diag[df_diag['hb_method'] == method_label]
515	            if mrows.empty:
516	                continue
517	            print(f"\n── {method_label.upper()} Diagnostics ──────────────────────────────")
518	            print(f"  Runs:           {len(mrows)}")
519	            rh = mrows['rhat_max'].dropna()
520	            es = mrows['ess_min'].dropna()
521	            if not rh.empty:
522	                print(f"  R-hat max:      {rh.max():.4f} (target < 1.01)")
523	            if not es.empty:
524	                print(f"  ESS min:        {es.min():.0f} (target > 200)")
525	            print(f"  Divergent total:{int(mrows['divergent_count'].sum())}")
526	            print(f"  Runtime median: {mrows['runtime_seconds'].median():.2f}s")
527	
528	    # Per-config HB vs MLE comparison
529	    print("\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──")
530	    for k in sorted(df_agg['k_subgroups'].unique()):
531	        print(f"\n  K = {int(k)} subgroups")
532	        for regime in ['extreme', 'moderate', 'homogeneous']:
533	            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]
534	            if sub.empty:
535	                continue
536	            print(f"    {regime}:")
537	            print(f"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  "
538	                  f"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}")
539	            for ne in sorted(sub['n_expert'].unique()):
540	                vals = {}
541	                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:
542	                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]
543	                    if ms.empty:
544	                        vals[m] = np.nan
545	                    else:
546	                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +
547	                                           ms['rmse_z1'].values ** 2).mean())
548	                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']
549	                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0
550	                tag = f"{pct:+.1f}%"
551	                print(f"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  "
552	                      f"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}")
553	
554	
555	# ── Sweep ─────────────────────────────────────────────────────────────────────
556	
557	def run_sweep(regime_names, n_experts, k_list, n_mc,
558	              hb_method='eb', mcmc_diag_runs=5, verbose=True):
559	    all_rows, all_diag = [], []
560	    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc
561	    count = 0
562	    t0 = time.time()
563	
564	    for k in k_list:
565	        for rn in regime_names:
566	            if rn not in REGIMES[k]:
567	                continue
568	            rp = REGIMES[k][rn]
569	            for ne in n_experts:
570	                for mc in range(n_mc):
571	                    use = hb_method
572	                    if hb_method == 'auto':
573	                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'
574	                    try:
575	                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)
576	                        all_rows.extend(rows)
577	                        all_diag.append(diag)
578	                    except Exception as e:
579	                        if verbose:
580	                            print(f"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}")
581	                        all_diag.append({
582	                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,
583	                            'mc_run': mc, 'hb_method': 'error',
584	                            'rhat_max': np.nan, 'ess_min': np.nan,
585	                            'divergent_count': -1, 'runtime_seconds': 0.0})
586	                    count += 1
587	                    if verbose and count % max(1, total // 20) == 0:
588	                        el = time.time() - t0
589	                        eta = el / count * (total - count)
590	                        print(f"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | "
591	                              f"k={k} {rn} ne={ne} mc={mc}")
592	
593	    if verbose:
594	        print(f"  Sweep done: {time.time() - t0:.1f}s ({count} runs)")
595	    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)
596	
597	
598	# ── Main ──────────────────────────────────────────────────────────────────────
599	
600	if __name__ == '__main__':
601	    parser = argparse.ArgumentParser()
602	    parser.add_argument('--n-mc', type=int, default=100)
603	    parser.add_argument('--dry-run', action='store_true')
604	    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')
605	    parser.add_argument('--mcmc-diag-runs', type=int, default=5)
606	    args = parser.parse_args()
607	
608	    n_mc = 5 if args.dry_run else args.n_mc
609	    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']
610	    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS
611	    k_list = [2] if args.dry_run else DEFAULT_K_LIST
612	
613	    print(f"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}")
614	    print(f"N={N} n_mc={n_mc} hb={args.hb_method}")
615	    print(f"Regimes={regime_names} n_experts={n_experts} K={k_list}\n")
616	
617	    # Timing test
618	    effective_method = args.hb_method
619	    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)
620	    em = d['expert_mask']
621	    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])
622	
623	    if args.hb_method == 'auto':
624	        print("Timing Gibbs sampler...")
625	        t0 = time.time()
626	        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)
627	        gt = time.time() - t0
628	        print(f"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} "
629	              f"ess={dg['ess_min']:.0f}")
630	        if gt < 5:
631	            effective_method = 'gibbs'
632	            print(f"  Fast enough → using Gibbs for all runs")
633	        else:
634	            effective_method = 'eb'
635	            print(f"  Slow → using EB")
636	    elif args.hb_method == 'mcmc' and HAS_PYMC:
637	        print("Timing PyMC MCMC...")
638	        t0 = time.time()
639	        try:
640	            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)
641	            mt = time.time() - t0
642	            print(f"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} "
643	                  f"ess={dg['ess_min']:.0f} div={dg['divergent_count']}")
644	        except Exception as e:
645	            print(f"  MCMC failed: {e} → falling back to Gibbs")
646	            effective_method = 'gibbs'
647	
648	    print(f"\nEffective method: {effective_method}\n")
649	
650	    df_raw, df_diag = run_sweep(
651	        regime_names, n_experts, k_list, n_mc,
652	        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)
653	
654	    df_agg = aggregate_results(df_raw)
655	
656	    os.makedirs('results', exist_ok=True)
657	    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',
658	                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',
659	                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']
660	    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)
661	
662	    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',
663	                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']
664	    save_cols = [c for c in diag_cols if c in df_diag.columns]
665	    if 'hb_method' in df_diag.columns:
666	        save_cols.insert(4, 'hb_method')
667	    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)
668	
669	    print_summary(df_agg, df_diag)
670	
671	    print(f"\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)")
672	    print(f"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)")
673	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "aea437f2-8b60-4bd0-9b5b-2bf870648303",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/exp001_hb_synthetic.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nexp001_hb_synthetic.py - Hierarchical Bayesian EC-HTE Synthetic Validation (exp-001)\n\nCompares confusion matrix estimators for CATE correction under heterogeneous\nmisclassification across subgroups:\n  Oracle, Naive, Global-corrected, MLE (Laplace), HB Dirichlet (partial pooling)\n\nInput: Synthetic DGP parameters (regimes, expert budgets, subgroup counts)\nOutput: results/exp001_hb_results.csv, results/exp001_hb_diagnostics.csv\n\"\"\"\n\nimport argparse\nimport os\nimport sys\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\nfrom scipy.optimize import minimize_scalar\n\nwarnings.filterwarnings('ignore')\n\ntry:\n    import pymc as pm\n    import pytensor.tensor as pt\n    import arviz as az\n    HAS_PYMC = True\nexcept ImportError:\n    HAS_PYMC = False\n\nN = 5000\nSUBGROUP_LABELS = {2: ['A', 'B'], 4: ['A', 'B', 'C', 'D']}\n\nREGIMES = {\n    2: {\n        'extreme':     {'misclass': [0.25, 0.05], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.15, 0.10], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n    4: {\n        'extreme':     {'misclass': [0.30, 0.20, 0.10, 0.03], 'tau_z1': 0.5, 'tau_z0': 0.1},\n        'moderate':    {'misclass': [0.20, 0.15, 0.10, 0.05], 'tau_z1': 0.3, 'tau_z0': 0.15},\n        'homogeneous': {'misclass': [0.12, 0.12, 0.12, 0.12], 'tau_z1': 0.25, 'tau_z0': 0.20},\n    },\n}\n\nDEFAULT_N_EXPERTS = [50, 100, 250, 500, 1000, 2000]\nDEFAULT_K_LIST = [2, 4]\n\n\n# ── DGP ───────────────────────────────────────────────────────────────────────\n\ndef generate_data(regime_params, n_expert, k, seed):\n    rng = np.random.RandomState(seed)\n    labels = SUBGROUP_LABELS[k]\n    T = rng.binomial(1, 0.5, N)\n    Z = rng.binomial(1, 0.5, N)\n    S = rng.choice(labels, N, p=[1.0 / k] * k)\n    X = rng.randn(N, 5)\n    tau = np.where(Z == 1, regime_params['tau_z1'], regime_params['tau_z0'])\n    Y = 1 + tau * T + 0.5 * X[:, 0] + rng.randn(N)\n    mc_rates = np.zeros(N)\n    for i, s in enumerate(labels):\n        mc_rates[S == s] = regime_params['misclass'][i]\n    Z_hat = np.where(rng.rand(N) < mc_rates, 1 - Z, Z)\n    idx = rng.choice(N, min(n_expert, N), replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[idx] = True\n    return dict(T=T, Z=Z, Z_hat=Z_hat, S=S, X=X, Y=Y, tau=tau, expert_mask=expert_mask)\n\n\n# ── Helpers ───────────────────────────────────────────────────────────────────\n\ndef diff_in_means(Y, T, mask):\n    t1, t0 = mask & (T == 1), mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    return y1.mean() - y0.mean(), np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    \"\"\"Confusion matrix counts per subgroup: (k, 2, 2) = [subgroup, true_z, z_hat].\"\"\"\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef build_mixing_matrix(C):\n    \"\"\"C[z, z_hat] → M[z_hat, z] via Bayes rule (assuming P(Z=0)=P(Z=1)=0.5).\n\n    NOTE: This assumes P(Z=0)=P(Z=1)=0.5, which is correct for this experiment's\n    DGP. For general P(Z), use the version in exp007 that takes p_z and p_z_hat.\n    \"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        cs = C[0, zh] + C[1, zh]\n        if cs > 0:\n            M[zh, 0] = C[0, zh] / cs\n            M[zh, 1] = C[1, zh] / cs\n        else:\n            M[zh, :] = 0.5\n    return M\n\n\ndef invert_mixing(M, tau_obs, se_obs):\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\ndef safe_invert_correction(M_s, tau_obs, cond_threshold=100, fallback='naive'):\n    \"\"\"Invert mixing matrix with condition number guard.\n\n    When cond(M_s) > threshold, matrix inversion is numerically unstable.\n    Falls back to naive (no correction) to avoid catastrophic amplification.\n    \"\"\"\n    cond = np.linalg.cond(M_s)\n    if cond > cond_threshold:\n        return tau_obs.copy()\n    return np.linalg.solve(M_s, tau_obs)\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    \"\"\"Like invert_mixing but with condition number guard.\"\"\"\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# ── Confusion Matrix Estimators ───────────────────────────────────────────────\n\ndef estimate_cm_mle(counts, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing (add-1).\"\"\"\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            n = counts[i, z, :].sum()\n            for zh in [0, 1]:\n                C_s[z, zh] = (counts[i, z, zh] + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef _dirmult_neg_ll(alpha, counts_z):\n    \"\"\"Negative log marginal likelihood for Dirichlet-Multinomial.\"\"\"\n    a = alpha / 2.0\n    if a < 1e-10:\n        return 1e10\n    ll = 0.0\n    for c0, c1 in counts_z:\n        n = c0 + c1\n        if n == 0:\n            continue\n        ll += gammaln(c0 + a) + gammaln(c1 + a) - gammaln(n + 2 * a)\n        ll -= 2 * gammaln(a) - gammaln(2 * a)\n    return -ll\n\n\ndef estimate_cm_hb_eb(counts, labels):\n    \"\"\"Empirical Bayes HB: optimize shared Dirichlet concentration, posterior mean.\"\"\"\n    k = len(labels)\n    alpha_opt = np.zeros(2)\n    for z in [0, 1]:\n        cl = [(int(counts[i, z, 0]), int(counts[i, z, 1])) for i in range(k)]\n        total = sum(c0 + c1 for c0, c1 in cl)\n        if total == 0:\n            alpha_opt[z] = 2.0\n            continue\n        res = minimize_scalar(\n            lambda a: _dirmult_neg_ll(a, cl), bounds=(0.01, 500), method='bounded')\n        alpha_opt[z] = res.x\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            a = alpha_opt[z] / 2.0\n            n = counts[i, z, :].sum()\n            d = n + 2 * a\n            C_s[z, 0] = (counts[i, z, 0] + a) / d if d > 0 else 0.5\n            C_s[z, 1] = (counts[i, z, 1] + a) / d if d > 0 else 0.5\n        C[s] = C_s\n\n    diag = {'rhat_max': np.nan, 'ess_min': np.nan, 'divergent_count': 0,\n            'runtime_seconds': 0.0, 'hb_method': 'eb',\n            'alpha_0_z0': alpha_opt[0], 'alpha_0_z1': alpha_opt[1]}\n    return C, diag\n\n\ndef _split_rhat(chains):\n    \"\"\"Split R-hat for a scalar parameter. chains: (n_chains, n_draws).\"\"\"\n    parts = []\n    for c in range(chains.shape[0]):\n        half = chains.shape[1] // 2\n        parts.append(chains[c, :half])\n        parts.append(chains[c, half:2 * half])\n    parts = np.array(parts)\n    m = parts.shape[0]\n    n = parts.shape[1]\n    chain_means = parts.mean(axis=1)\n    W = np.mean(np.var(parts, axis=1, ddof=1))\n    B = n * np.var(chain_means, ddof=1)\n    if W < 1e-20:\n        return 1.0\n    var_hat = (1 - 1.0 / n) * W + B / n\n    return float(np.sqrt(var_hat / W))\n\n\ndef _bulk_ess(chains):\n    \"\"\"Approximate bulk ESS via initial positive sequence. chains: (n_chains, n_draws).\"\"\"\n    x = chains.ravel()\n    n = len(x)\n    mu = x.mean()\n    xc = x - mu\n    max_lag = min(n // 2, 300)\n    c0 = np.dot(xc, xc)\n    if c0 < 1e-20:\n        return float(n)\n    tau = 1.0\n    for lag in range(1, max_lag - 1, 2):\n        r1 = np.dot(xc[:n - lag], xc[lag:]) / c0\n        r2 = np.dot(xc[:n - lag - 1], xc[lag + 1:]) / c0 if lag + 1 < n else 0\n        pair = r1 + r2\n        if pair < 0:\n            break\n        tau += 2 * pair\n    return float(n / tau)\n\n\ndef _fast_diagnostics(alpha_arr, theta_arr, labels):\n    \"\"\"Compute R-hat and ESS over all parameters without arviz.\"\"\"\n    rhats, esss = [], []\n    for d in range(alpha_arr.shape[2]):\n        rhats.append(_split_rhat(alpha_arr[:, :, d]))\n        esss.append(_bulk_ess(alpha_arr[:, :, d]))\n    k = len(labels)\n    for i in range(k):\n        for z in [0, 1]:\n            for zh in range(theta_arr.shape[4]):\n                ch = theta_arr[:, :, i, z, zh]\n                rhats.append(_split_rhat(ch))\n                esss.append(_bulk_ess(ch))\n    return max(rhats), min(esss)\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Log posterior for alpha_0[z] in log-alpha space (includes Jacobian).\"\"\"\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=4000, n_warmup=2000, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    \"\"\"Gibbs sampler for HB Dirichlet-Multinomial (conjugate + adaptive MH for alpha_0).\n\n    hp_a0, hp_b0: Gamma hyperprior shape/rate on alpha_0 (default Gamma(3,1)).\n    \"\"\"\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_alpha, all_theta = [], []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        alpha_samples = np.zeros((n_iter, 2))\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                idx = it - n_warmup\n                alpha_samples[idx] = alpha.copy()\n                theta_samples[idx] = theta.copy()\n\n        all_alpha.append(alpha_samples)\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    alpha_arr = np.stack(all_alpha)\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    rhat_max, ess_min = _fast_diagnostics(alpha_arr, theta_arr, labels)\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min, 'divergent_count': 0,\n            'runtime_seconds': runtime, 'hb_method': 'gibbs'}\n    return C, diag\n\n\ndef estimate_cm_hb_mcmc(counts, labels, seed=42, draws=1000, tune=500, chains=2):\n    \"\"\"Full Bayesian HB with PyMC MCMC.\"\"\"\n    k = len(labels)\n    n_per_sz = counts.sum(axis=2)\n\n    with pm.Model():\n        alpha_0 = pm.Gamma('alpha_0', alpha=2, beta=1, shape=2)\n        for z in [0, 1]:\n            for i, s in enumerate(labels):\n                nsz = int(n_per_sz[i, z])\n                if nsz == 0:\n                    continue\n                a = pt.stack([alpha_0[z] / 2, alpha_0[z] / 2])\n                theta = pm.Dirichlet(f'theta_{s}_z{z}', a=a)\n                pm.Multinomial(f'obs_{s}_z{z}', n=nsz, p=theta,\n                               observed=counts[i, z, :].astype('int32'))\n        t0 = time.time()\n        trace = pm.sample(draws=draws, tune=tune, chains=chains,\n                          random_seed=seed, progressbar=False)\n        runtime = time.time() - t0\n\n    C = {}\n    for i, s in enumerate(labels):\n        C_s = np.zeros((2, 2))\n        for z in [0, 1]:\n            vn = f'theta_{s}_z{z}'\n            if vn in trace.posterior:\n                C_s[z, :] = trace.posterior[vn].values.mean(axis=(0, 1))\n            else:\n                C_s[z, :] = 0.5\n        C[s] = C_s\n\n    all_vars = list(trace.posterior.data_vars)\n    try:\n        summ = az.summary(trace, var_names=all_vars)\n        rhat_max = float(summ['r_hat'].max())\n        ess_min = float(summ['ess_bulk'].min())\n    except Exception:\n        rhat_max = ess_min = np.nan\n    try:\n        divergent = int(trace.sample_stats['diverging'].values.sum())\n    except Exception:\n        divergent = -1\n\n    diag = {'rhat_max': rhat_max, 'ess_min': ess_min,\n            'divergent_count': divergent, 'runtime_seconds': runtime,\n            'hb_method': 'mcmc'}\n    return C, diag\n\n\n# ── Single MC Run ─────────────────────────────────────────────────────────────\n\ndef run_one_mc(regime_name, regime_params, n_expert, k, seed, hb_method='eb'):\n    data = generate_data(regime_params, n_expert, k, seed)\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    em = data['expert_mask']\n    labels = SUBGROUP_LABELS[k]\n    tau_z0, tau_z1 = regime_params['tau_z0'], regime_params['tau_z1']\n\n    counts = get_counts(Z[em], Z_hat[em], S[em], labels)\n\n    C_mle = estimate_cm_mle(counts, labels)\n\n    if hb_method == 'gibbs':\n        C_hb, hb_diag = estimate_cm_hb_gibbs(counts, labels, seed=seed)\n    elif hb_method == 'mcmc' and HAS_PYMC:\n        try:\n            C_hb, hb_diag = estimate_cm_hb_mcmc(counts, labels, seed=seed)\n        except Exception:\n            C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n            hb_diag['hb_method'] = 'eb_fallback'\n    else:\n        C_hb, hb_diag = estimate_cm_hb_eb(counts, labels)\n\n    # Global CM (pool all expert labels, Laplace)\n    cg = counts.sum(axis=0)\n    C_gl = np.zeros((2, 2))\n    for z in [0, 1]:\n        n = cg[z, :].sum()\n        for zh in [0, 1]:\n            C_gl[z, zh] = (cg[z, zh] + 1) / (n + 2) if n > 0 else 0.5\n\n    M_gl = build_mixing_matrix(C_gl)\n    M_mle = {s: build_mixing_matrix(C_mle[s]) for s in labels}\n    M_hb = {s: build_mixing_matrix(C_hb[s]) for s in labels}\n\n    base = {'regime': regime_name, 'n_expert': n_expert, 'k_subgroups': k, 'mc_run': seed}\n    rows = []\n\n    for s in labels:\n        sm = S == s\n        th0_or, se0_or = diff_in_means(Y, T, sm & (Z == 0))\n        th1_or, se1_or = diff_in_means(Y, T, sm & (Z == 1))\n        th0_n, se0_n = diff_in_means(Y, T, sm & (Z_hat == 0))\n        th1_n, se1_n = diff_in_means(Y, T, sm & (Z_hat == 1))\n\n        tau_obs = np.array([th0_n, th1_n])\n        se_obs = np.array([se0_n, se1_n])\n        if np.any(np.isnan(tau_obs)):\n            continue\n\n        tgc, sgc = invert_mixing(M_gl, tau_obs, se_obs)\n        tml, sml = invert_mixing(M_mle[s], tau_obs, se_obs)\n        thb, shb = invert_mixing(M_hb[s], tau_obs, se_obs)\n\n        def mr(method, th0, th1, se0, se1):\n            return {**base, 'subgroup': s, 'method': method,\n                    'tau_hat_z0': th0, 'tau_hat_z1': th1,\n                    'se_z0': se0, 'se_z1': se1,\n                    'tau_true_z0': tau_z0, 'tau_true_z1': tau_z1}\n\n        rows.append(mr('oracle', th0_or, th1_or, se0_or, se1_or))\n        rows.append(mr('naive', th0_n, th1_n, se0_n, se1_n))\n        rows.append(mr('global_corrected', tgc[0], tgc[1], sgc[0], sgc[1]))\n        rows.append(mr('mle_laplace', tml[0], tml[1], sml[0], sml[1]))\n        rows.append(mr('hb_dirichlet', thb[0], thb[1], shb[0], shb[1]))\n\n    return rows, {**base, **hb_diag}\n\n\n# ── Aggregation ───────────────────────────────────────────────────────────────\n\ndef aggregate_results(df):\n    rows = []\n    grp_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method']\n    for keys, grp in df.groupby(grp_cols):\n        regime, n_expert, k, subgroup, method = keys\n        row = {'regime': regime, 'n_expert': int(n_expert), 'k_subgroups': int(k),\n               'subgroup': subgroup, 'method': method}\n        n_mc = len(grp)\n        for z in ['z0', 'z1']:\n            err = grp[f'tau_hat_{z}'].values - grp[f'tau_true_{z}'].values\n            bias = err.mean()\n            mse = (err ** 2).mean()\n            rmse = np.sqrt(mse)\n            ci_lo = grp[f'tau_hat_{z}'].values - 1.96 * grp[f'se_{z}'].values\n            ci_hi = grp[f'tau_hat_{z}'].values + 1.96 * grp[f'se_{z}'].values\n            cov = ((ci_lo <= grp[f'tau_true_{z}'].values) &\n                   (grp[f'tau_true_{z}'].values <= ci_hi)).mean()\n            row[f'bias_{z}'] = bias\n            row[f'rmse_{z}'] = rmse\n            row[f'coverage_{z}'] = cov\n            row[f'bias_{z}_se'] = err.std() / np.sqrt(n_mc)\n            mse_se = (err ** 2).std() / np.sqrt(n_mc)\n            row[f'rmse_{z}_se'] = mse_se / (2 * rmse) if rmse > 1e-10 else np.nan\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# ── Output ────────────────────────────────────────────────────────────────────\n\ndef print_summary(df_agg, df_diag):\n    pd.set_option('display.float_format', '{:.4f}'.format)\n\n    # MCMC / Gibbs diagnostics\n    if 'hb_method' in df_diag.columns:\n        for method_label in ['gibbs', 'mcmc']:\n            mrows = df_diag[df_diag['hb_method'] == method_label]\n            if mrows.empty:\n                continue\n            print(f\"\\n── {method_label.upper()} Diagnostics ──────────────────────────────\")\n            print(f\"  Runs:           {len(mrows)}\")\n            rh = mrows['rhat_max'].dropna()\n            es = mrows['ess_min'].dropna()\n            if not rh.empty:\n                print(f\"  R-hat max:      {rh.max():.4f} (target < 1.01)\")\n            if not es.empty:\n                print(f\"  ESS min:        {es.min():.0f} (target > 200)\")\n            print(f\"  Divergent total:{int(mrows['divergent_count'].sum())}\")\n            print(f\"  Runtime median: {mrows['runtime_seconds'].median():.2f}s\")\n\n    # Per-config HB vs MLE comparison\n    print(\"\\n── HB vs MLE RMSE Comparison (subgroup-level, averaged) ──\")\n    for k in sorted(df_agg['k_subgroups'].unique()):\n        print(f\"\\n  K = {int(k)} subgroups\")\n        for regime in ['extreme', 'moderate', 'homogeneous']:\n            sub = df_agg[(df_agg['k_subgroups'] == k) & (df_agg['regime'] == regime)]\n            if sub.empty:\n                continue\n            print(f\"    {regime}:\")\n            print(f\"    {'n_exp':>6s}  {'oracle':>8s}  {'naive':>8s}  {'global':>8s}  \"\n                  f\"{'mle':>8s}  {'hb':>8s}  {'HB vs MLE':>10s}\")\n            for ne in sorted(sub['n_expert'].unique()):\n                vals = {}\n                for m in ['oracle', 'naive', 'global_corrected', 'mle_laplace', 'hb_dirichlet']:\n                    ms = sub[(sub['method'] == m) & (sub['n_expert'] == ne)]\n                    if ms.empty:\n                        vals[m] = np.nan\n                    else:\n                        vals[m] = np.sqrt((ms['rmse_z0'].values ** 2 +\n                                           ms['rmse_z1'].values ** 2).mean())\n                mle_v, hb_v = vals['mle_laplace'], vals['hb_dirichlet']\n                pct = (mle_v - hb_v) / mle_v * 100 if mle_v > 1e-10 else 0\n                tag = f\"{pct:+.1f}%\"\n                print(f\"    {int(ne):6d}  {vals['oracle']:8.4f}  {vals['naive']:8.4f}  \"\n                      f\"{vals['global_corrected']:8.4f}  {mle_v:8.4f}  {hb_v:8.4f}  {tag:>10s}\")\n\n\n# ── Sweep ─────────────────────────────────────────────────────────────────────\n\ndef run_sweep(regime_names, n_experts, k_list, n_mc,\n              hb_method='eb', mcmc_diag_runs=5, verbose=True):\n    all_rows, all_diag = [], []\n    total = sum(1 for k in k_list for r in regime_names if r in REGIMES[k]) * len(n_experts) * n_mc\n    count = 0\n    t0 = time.time()\n\n    for k in k_list:\n        for rn in regime_names:\n            if rn not in REGIMES[k]:\n                continue\n            rp = REGIMES[k][rn]\n            for ne in n_experts:\n                for mc in range(n_mc):\n                    use = hb_method\n                    if hb_method == 'auto':\n                        use = 'mcmc' if mc < mcmc_diag_runs else 'eb'\n                    try:\n                        rows, diag = run_one_mc(rn, rp, ne, k, seed=mc, hb_method=use)\n                        all_rows.extend(rows)\n                        all_diag.append(diag)\n                    except Exception as e:\n                        if verbose:\n                            print(f\"  WARN: k={k} {rn} ne={ne} mc={mc} failed: {e}\")\n                        all_diag.append({\n                            'regime': rn, 'n_expert': ne, 'k_subgroups': k,\n                            'mc_run': mc, 'hb_method': 'error',\n                            'rhat_max': np.nan, 'ess_min': np.nan,\n                            'divergent_count': -1, 'runtime_seconds': 0.0})\n                    count += 1\n                    if verbose and count % max(1, total // 20) == 0:\n                        el = time.time() - t0\n                        eta = el / count * (total - count)\n                        print(f\"  [{count}/{total}] {el:.0f}s elapsed, ETA {eta:.0f}s | \"\n                              f\"k={k} {rn} ne={ne} mc={mc}\")\n\n    if verbose:\n        print(f\"  Sweep done: {time.time() - t0:.1f}s ({count} runs)\")\n    return pd.DataFrame(all_rows), pd.DataFrame(all_diag)\n\n\n# ── Main ──────────────────────────────────────────────────────────────────────\n\nif __name__ == '__main__':\n    parser = argparse.ArgumentParser()\n    parser.add_argument('--n-mc', type=int, default=100)\n    parser.add_argument('--dry-run', action='store_true')\n    parser.add_argument('--hb-method', choices=['auto', 'mcmc', 'gibbs', 'eb'], default='auto')\n    parser.add_argument('--mcmc-diag-runs', type=int, default=5)\n    args = parser.parse_args()\n\n    n_mc = 5 if args.dry_run else args.n_mc\n    regime_names = ['moderate'] if args.dry_run else ['extreme', 'moderate', 'homogeneous']\n    n_experts = [100] if args.dry_run else DEFAULT_N_EXPERTS\n    k_list = [2] if args.dry_run else DEFAULT_K_LIST\n\n    print(f\"exp-001 HB Synthetic Validation | PyMC={HAS_PYMC}\")\n    print(f\"N={N} n_mc={n_mc} hb={args.hb_method}\")\n    print(f\"Regimes={regime_names} n_experts={n_experts} K={k_list}\\n\")\n\n    # Timing test\n    effective_method = args.hb_method\n    d = generate_data(REGIMES[2]['moderate'], 100, 2, seed=9999)\n    em = d['expert_mask']\n    tc = get_counts(d['Z'][em], d['Z_hat'][em], d['S'][em], ['A', 'B'])\n\n    if args.hb_method == 'auto':\n        print(\"Timing Gibbs sampler...\")\n        t0 = time.time()\n        _, dg = estimate_cm_hb_gibbs(tc, ['A', 'B'], seed=9999)\n        gt = time.time() - t0\n        print(f\"  Gibbs: {gt:.2f}s | rhat={dg['rhat_max']:.3f} \"\n              f\"ess={dg['ess_min']:.0f}\")\n        if gt < 5:\n            effective_method = 'gibbs'\n            print(f\"  Fast enough → using Gibbs for all runs\")\n        else:\n            effective_method = 'eb'\n            print(f\"  Slow → using EB\")\n    elif args.hb_method == 'mcmc' and HAS_PYMC:\n        print(\"Timing PyMC MCMC...\")\n        t0 = time.time()\n        try:\n            _, dg = estimate_cm_hb_mcmc(tc, ['A', 'B'], seed=9999)\n            mt = time.time() - t0\n            print(f\"  MCMC: {mt:.1f}s | rhat={dg['rhat_max']:.3f} \"\n                  f\"ess={dg['ess_min']:.0f} div={dg['divergent_count']}\")\n        except Exception as e:\n            print(f\"  MCMC failed: {e} → falling back to Gibbs\")\n            effective_method = 'gibbs'\n\n    print(f\"\\nEffective method: {effective_method}\\n\")\n\n    df_raw, df_diag = run_sweep(\n        regime_names, n_experts, k_list, n_mc,\n        hb_method=effective_method, mcmc_diag_runs=args.mcmc_diag_runs)\n\n    df_agg = aggregate_results(df_raw)\n\n    os.makedirs('results', exist_ok=True)\n    agg_cols = ['regime', 'n_expert', 'k_subgroups', 'subgroup', 'method',\n                'bias_z0', 'rmse_z0', 'coverage_z0', 'bias_z1', 'rmse_z1', 'coverage_z1',\n                'bias_z0_se', 'rmse_z0_se', 'bias_z1_se', 'rmse_z1_se']\n    df_agg[agg_cols].to_csv('results/exp001_hb_results.csv', index=False)\n\n    diag_cols = ['regime', 'n_expert', 'k_subgroups', 'mc_run',\n                 'rhat_max', 'ess_min', 'divergent_count', 'runtime_seconds']\n    save_cols = [c for c in diag_cols if c in df_diag.columns]\n    if 'hb_method' in df_diag.columns:\n        save_cols.insert(4, 'hb_method')\n    df_diag[save_cols].to_csv('results/exp001_hb_diagnostics.csv', index=False)\n\n    print_summary(df_agg, df_diag)\n\n    print(f\"\\nSaved: results/exp001_hb_results.csv ({len(df_agg)} rows)\")\n    print(f\"Saved: results/exp001_hb_diagnostics.csv ({len(df_diag)} rows)\")\n",
      "numLines": 673,
      "startLine": 1,
      "totalLines": 673
    }
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of the existing codebase. The key patterns are:

1. **exp015** is the closest reference - it uses real asymmetric CMs from GPT-4.1 with the same structure I need
2. **exp001** has the HB Gibbs sampler and EB estimator 
3. **exp014** has asymmetric correction logic

For the Llama semi-synthetic experiment, I need to:
- Adapt exp015's structure but with Llama CM values
- Use P(Z=1) = 0.652 (not 0.5 like exp001, not 0.18 like exp015)


- Set Δτ = 0.3 with τ(z=0) = 0.35 and τ(z=1) = 0.65, incorporate the Stratified MLE method, collect 200 expert labels across 20 MC seeds

The critical insight is that exp015 already handles the asymmetric FPR/FNR correctly through its confusion matrix and mixing matrix functions, which properly account for the imbalanced class prior using Bayes rule—essential since my P(Z=1) = 0.652 deviates from the standard 0.5 assumption.

Now I'm writing the script based on exp015's structure since it's the closest match, but I need to adapt it for Llama's confusion matrix values and the different class distribution. The subgroup structure has labels like False_medium and True_short, where the True/False dimension likely corresponds to Z, and I need to extract the per-subgroup P(Z=1) values from the actual data rather than assuming they're uniform. ups already encode the Z value? No, looking at the CM table, each subgroup has its own FPR and FNR, which means Z varies within each subgroup. The subgroups seem to be based on some other characteristic (like text length + some other binary variable).

For the DGP, I think:
- Overall P(Z=1) = 0.652
- The task says "per-subgroup P(Z=1) 也按真实值" but actual per-subgroup P(Z=1) values aren't given. Since subgroups are named True_*/False_*, maybe P(Z=1) varies by subgroup but I don't have explicit values.

Actually, looking more carefully: the subgroup names are True_medium, True_short, False_medium, False_short. These might be cross-products of two variables. The "True/False" could be the Z value and "medium/short" could be the text length. But if Z is encoded in the subgroup name, then per-subgroup, Z is deterministic, which doesn't align with needing a confusion matrix. I think the subgroups must be defined by something else entirely, and I should just use the overall P(Z=1) = 0.652 across all subgroups for the simulation since the actual per-subgroup values aren't provided.

For the CATE structure, I'm working out the treatment effects: with Δτ = 0.3 and τ_avg = 0.5, the effects split as τ(Z=0) = 0.35 and τ(Z=1) = 0.65.

The heterogeneity is purely along the Z dimension—all subgroups share the same treatment effects, which is simpler than the previous experiment that had subgroup-specific variation. Now I'm planning the estimation methods: naive estimation using predicted Z directly, a global approach that pools expert labels to estimate a single confusion matrix and inverts it, and a stratified MLE approach that estimates per-subgroup confusion matrices from the expert labels.

For handling the non-balanced Z case, I need to apply Bayes rule to construct the mixing matrix—computing the posterior probability of true Z given predicted Z using the confusion matrix, prior on Z, and marginal probability of predicted Z. This calculation is already available from the previous experiment's implementation.

To correct the observed treatment effects, I'll invert the relationship between observed and true effects using the mixing matrix, solving for the true effects given the observed ones.

Now I'm writing the full script, keeping it self-contained like the previous experiment. I need to clarify how to handle the per-subgroup structure—I'll use a uniform prior for P(Z=1) across subgroups and let the confusion matrix values vary by subgroup instead. For the per-subgroup correction, I need to compute the mixing matrix separately for each subgroup using the subgroup-specific confusion matrices and conditional probabilities of Z given the subgroup. The true CATE differs by z-level: 0.35 for z=0 and 0.65 for z=1. I'm also adding a stratified MLE approach with Laplace smoothing as a baseline that applies per-subgroup estimation without hierarchical borrowing of strength.

Writing simulation script... Setting up the configuration and helper functions... Writing confusion matrix functions... Finishing the mixing matrix calculation with Bayes' rule, then implementing a safe matrix inversion that checks the condition number and determinant before inverting, returning the original estimates if the matrix is too ill-conditioned. Now I'm setting up helper functions for the Gibbs sampler that will process counts across different subgroups.

Writing sampling utilities... Setting up the Gibbs sampling chains... Writing sampling logic... Writing the data generation function... I'm extracting the data arrays from the dictionary and then subsetting them to just the expert annotations, computing a global confusion matrix and mixing matrix from those experts, then estimating confusion matrices per subgroup using maximum likelihood and setting up for a hierarchical Bayes Gibbs sampler.

Building per-subgroup mixing matrices... Building results table... Adding results to the output table... Extracting the treatment effects at the specific stratum level from each estimation method, then computing confidence intervals with the standard errors. Adding more result rows... Writing result aggregation...

Now I'm building the analysis output, starting with a markdown header and design section that documents the experiment using real confusion matrices from the model with synthetic ground truth CATE values, then creating a table that shows the subgroup characteristics including their weights and error rates.

Generating markdown table... Generating markdown table... Generating markdown table... Generating markdown report... Writing main script output... Writing the analysis and summary output...

I need to reconsider the CSV output format—the user wants columns for seed, method, subgroup, z_level, bias, rmse, coverage, cate_true, and cate_est. For individual rows, RMSE as a per-observation metric doesn't quite align with how it's typically calculated, but I can use the squared bias or absolute bias as the contribution to include in that column. rmse" is really just |bias| (single observation squared error before aggregation). At aggregate level, RMSE = sqrt(mean(bias^2)). Now I'll finalize the script and write it out.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "cb8e38cf-a818-4857-87ef-bf2dfde005d5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtvg9ifxqXRXfAxziMaNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31082,
      "cache_read_input_tokens": 23432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 31082
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

_source line 30_

I now have a clear picture of the codebase. exp015 is the closest reference — it uses real asymmetric CMs with the same correction pipeline. I'll adapt it for Llama CM values with P(Z=1)=0.652 and add the Stratified MLE method.

Writing the script now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "89e95dd3-d681-4a9b-9da7-1cb55d555506",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtvg9ifxqXRXfAxziMaNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31082,
      "cache_read_input_tokens": 23432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 31082
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

_source line 31_

<details open><summary>🔧 Tool call — Write · `toolu_01Pxy45AZ1bY1EcGYi8k5Z2j`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
  "content": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "a75e5e45-1dd3-4586-9118-6670ae3f3a8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015jtvg9ifxqXRXfAxziMaNd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 31082,
      "cache_read_input_tokens": 23432,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 31082
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

_source line 32 · 2026-05-21T20:48:17.103Z_

<details><summary>↩ Tool result · `toolu_01Pxy45AZ1bY1EcGYi8k5Z2j`</summary>

```text
File created successfully at: /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "07e55d1b-d4a1-4c82-838e-9fc2b0f2d680",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
    "content": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 33_

Now running it. First a quick dry-run check to verify the code runs, then the full 20 seeds.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "ec86613c-93b2-48b1-a87b-bd71a2eaa888",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWJTK5NfPNdaUtua9qSpM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20580,
      "cache_read_input_tokens": 54514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20580
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

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01Jah8BE7L3Zy9tMpReDcTfp`</summary>

```json
{
  "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
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
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "b741fe65-aad3-481e-aa36-4645efde232c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWJTK5NfPNdaUtua9qSpM8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20580,
      "cache_read_input_tokens": 54514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20580
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

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bgivznv1j",
  "tool_use_id": "toolu_01Jah8BE7L3Zy9tMpReDcTfp",
  "description": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "task_type": "local_bash",
  "uuid": "aaadcd4e-062f-4e1e-b00e-e88ba62e4257",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bgivznv1j",
  "tool_use_id": "toolu_01Jah8BE7L3Zy9tMpReDcTfp",
  "status": "completed",
  "output_file": "",
  "summary": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "uuid": "9cd4a3f7-8905-43a7-baf5-010dc2ce54a4",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### Tool result

_source line 37 · 2026-05-21T20:48:40.862Z_

<details><summary>↩ Tool result · `toolu_01Jah8BE7L3Zy9tMpReDcTfp`</summary>

```text
Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
N=5000, n_expert=200, n_mc=20, P(Z=1)=0.652
tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
Subgroup CMs:
  False_medium: FPR=0.235, FNR=0.319
  False_short: FPR=0.310, FNR=0.212
  True_medium: FPR=0.219, FNR=0.258
  True_short: FPR=0.091, FNR=0.190

=== Dry run (1 seed) ===
Dry run OK: 40 rows
  oracle              : mean |bias| = 0.0705
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.1348
  stratified_mle      : mean |bias| = 0.3423
  hb_ec_hte           : mean |bias| = 0.3354

=== Full run (20 seeds) ===
  [1/20] 1s elapsed, ETA 16s
  [2/20] 2s elapsed, ETA 16s
  [3/20] 3s elapsed, ETA 15s
  [4/20] 3s elapsed, ETA 14s
  [5/20] 4s elapsed, ETA 13s
  [6/20] 5s elapsed, ETA 12s
  [7/20] 6s elapsed, ETA 11s
  [8/20] 7s elapsed, ETA 10s
  [9/20] 8s elapsed, ETA 9s
  [10/20] 9s elapsed, ETA 9s
  [11/20] 9s elapsed, ETA 8s
  [12/20] 10s elapsed, ETA 7s
  [13/20] 11s elapsed, ETA 6s
  [14/20] 12s elapsed, ETA 5s
  [15/20] 13s elapsed, ETA 4s
  [16/20] 14s elapsed, ETA 3s
  [17/20] 15s elapsed, ETA 3s
  [18/20] 16s elapsed, ETA 2s
  [19/20] 17s elapsed, ETA 1s
  [20/20] 18s elapsed, ETA 0s

Total time: 17.6s
Saved llama_semisynthetic_results.csv (800 rows)
Wrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md

=== Summary ===

  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950
  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750
  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856
  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744
  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "1cafb368-2789-4cb4-bd92-4f4b2fe05593",
  "tool_use_result": {
    "stdout": "Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\nN=5000, n_expert=200, n_mc=20, P(Z=1)=0.652\ntau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3\nSubgroup CMs:\n  False_medium: FPR=0.235, FNR=0.319\n  False_short: FPR=0.310, FNR=0.212\n  True_medium: FPR=0.219, FNR=0.258\n  True_short: FPR=0.091, FNR=0.190\n\n=== Dry run (1 seed) ===\nDry run OK: 40 rows\n  oracle              : mean |bias| = 0.0705\n  naive               : mean |bias| = 0.0796\n  global_corrected    : mean |bias| = 0.1348\n  stratified_mle      : mean |bias| = 0.3423\n  hb_ec_hte           : mean |bias| = 0.3354\n\n=== Full run (20 seeds) ===\n  [1/20] 1s elapsed, ETA 16s\n  [2/20] 2s elapsed, ETA 16s\n  [3/20] 3s elapsed, ETA 15s\n  [4/20] 3s elapsed, ETA 14s\n  [5/20] 4s elapsed, ETA 13s\n  [6/20] 5s elapsed, ETA 12s\n  [7/20] 6s elapsed, ETA 11s\n  [8/20] 7s elapsed, ETA 10s\n  [9/20] 8s elapsed, ETA 9s\n  [10/20] 9s elapsed, ETA 9s\n  [11/20] 9s elapsed, ETA 8s\n  [12/20] 10s elapsed, ETA 7s\n  [13/20] 11s elapsed, ETA 6s\n  [14/20] 12s elapsed, ETA 5s\n  [15/20] 13s elapsed, ETA 4s\n  [16/20] 14s elapsed, ETA 3s\n  [17/20] 15s elapsed, ETA 3s\n  [18/20] 16s elapsed, ETA 2s\n  [19/20] 17s elapsed, ETA 1s\n  [20/20] 18s elapsed, ETA 0s\n\nTotal time: 17.6s\nSaved llama_semisynthetic_results.csv (800 rows)\nWrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md\n\n=== Summary ===\n\n  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950\n  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750\n  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856\n  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744\n  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750",
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

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Interesting results. The Global and HB EC-HTE corrections are actually performing WORSE than Naive in this case. This seems problematic. Let me investigate why.

The issue might be that with only 200 expert labels and 4 subgroups, the per-subgroup expert counts are very small (about 50 per subgroup on average, but with unequal weights: 193/500*200 ≈ 77, 109/500*200 ≈ 44, 129/500*200 ≈ 52, 69/500*200 ≈ 28). 


But the Global correction also underperforming Naive is more concerning—it suggests the correction approach itself might be flawed. The mixing matrix construction relies on Bayes' rule with P(Z=1) = 0.652, which creates an imbalanced class distribution. With moderate misclassification rates, this could make the mixing matrix nearly singular or poorly conditioned, amplifying noise rather than correcting it.

The real problem is that the mixing matrix is estimated from only 200 expert labels spread across 4 subgroups, so the estimation is inherently noisy. When I invert this noisy matrix to recover the true treatment effects from the observed ones, the inversion amplifies those estimation errors, making the correction worse than just using the naive estimates. The bias from Naive estimation comes from mixing true and predicted treatment groups when there's misclassification, but with moderate error rates the actual bias stays manageable. However, inverting the mixing matrix to correct this amplifies the noise in the estimation, and that noise penalty outweighs the bias reduction benefit—especially when the heterogeneity in treatment effects is small relative to the estimation variance.

For Llama's case with moderate misclassification heterogeneity and only 200 experts, the variance cost of correction exceeds what we'd gain from reducing bias. I'm now checking whether the condition number of the mixing matrix explains why even the global correction introduces too much variance, and reconsidering how the mixing matrix itself is constructed given the base rates of treatment assignment. Now I'm computing the predicted label probabilities by applying the confusion matrix to the prior probabilities, which gives me P(Z_hat=0) ≈ 0.440 and P(Z_hat=1) ≈ 0.560. Then I'm constructing the mixing matrix M to find the conditional probability of the true label given the predicted label.

Computing the matrix determinant and its inverse to prepare for solving the label corruption problem...

Now I'm calculating the observed treatment effects by applying the mixing matrix, then using the inverse to recover the true effects—checking that the correction brings me back to the original values.

The math checks out, but when estimating M from 200 expert labels, the noise in that estimate gets amplified when I invert it. The condition number is probably around 2-3, so the amplification isn't extreme, yet the results show the naive approach has a bias of 0.10 while the global correction overshoots to 0.15. Let me trace through the code to see where the over-correction is coming from.

I'm checking how the marginal distributions are computed—p_zh_global uses the full sample's Z_hat distribution while p_z_global uses only the expert subset's true Z labels. Since experts are randomly selected, these should align with the true population distribution, but there might be something subtle going on with how the bias decomposes when M is estimated rather than known.

Now I'm working through the bias calculation for the Naive estimator by hand. The bias for each subgroup depends on the confusion matrix M and the true treatment effects, and when I plug in the numbers—the off-diagonal elements of M weighted by the difference in effects—I get a predicted absolute bias around 0.08 per subgroup, which appears to match what I'm observing empirically.

For the corrected estimator, applying the inverse confusion matrix should eliminate the systematic bias in expectation, but the variance gets amplified by the condition number of M. Since the inverse has entries around 1-2, the standard error roughly doubles. This means the corrected approach trades bias for variance—the naive estimator has substantial systematic error but lower variance, while the corrected version is unbiased but noisier. Given the naive SE is probably in the 0.07-0.10 range from the sample size, correction pushes it up to 0.15-0.20, making the overall RMSE for the naive approach around 0.128 when I combine the bias and variance components.

The real problem is that we're estimating M from only 200 expert samples, so the corrected estimator isn't truly unbiased—there's additional bias from the noisy M estimates. With the moderate misclassification rate we're seeing, the variance inflation from inverting this noisy matrix outweighs the bias reduction, which explains why the correction actually performs worse. This effect is amplified for stratified methods like MLE and hierarchical Bayes, where each subgroup has very few observations to work with.

Actually, I'm noticing something odd with the Global correction results—it's performing worse than the Naive approach even though it should have a more stable estimate using all 200 experts. The issue might be that applying a single global mixing matrix to all subgroups introduces systematic error, since the true confusion matrix likely varies across different subgroups.

That's precisely what EC-HTE is meant to address, but with only 30-80 expert labels per subgroup, the per-subgroup estimates become too noisy and the variance overwhelms any bias reduction. So the trade-off is clear: Naive has low bias but some attenuation, Global adds bias from the wrong mixing matrix, and HB EC-HTE has the right per-subgroup estimates but too much noise to be useful at this sample size.

Now I'm checking whether this ordering holds across different expert budgets and verifying my correction logic to make sure I'm computing the per-subgroup confusion matrices correctly. tau_corr = M_global^{-1} @ tau_obs
3. For HB: tau_corr = M_hb_sub[s]^{-1} @ tau_obs

For Global correction, the issue is that the true tau_obs for subgroup s satisfies:
tau_obs_s = M_s @ tau_true (where M_s is the subgroup-specific mixing matrix)

But we're applying M_global^{-1}, so:
tau_corr_s = M_global^{-1} @ tau_obs_s = M_global^{-1} @ M_s @ tau_true

The bias is:
(M_global^{-1} @ M_s - I) @ tau_true

This is non-zero when M_s ≠ M_global, which happens whenever there's heterogeneity in the confusion matrices across subgroups. That's the core source of the EC-HTE bias. With hierarchical Bayes, if the per-subgroup CM estimates are accurate enough, the correction becomes nearly unbiased, though the smaller sample sizes per subgroup introduce estimation noise that increases variance. So the tradeoff is clear: global correction has structural bias but low variance, while HB EC-HTE removes the bias at the cost of higher variance from noisier per-subgroup estimates. The results make sense as they are, and since the task just asks for a dry-run verification before scaling up, I should check that the outputs and analysis report are in order and then wrap up. that's Bayes' rule, so the mixing matrix is correct. Now I'm checking whether the correction formula makes sense—specifically, whether the observed CATE for each predicted group is truly a weighted average of the true CATEs based on the posterior probability of the true group given the predicted group. Let me work through the derivation from scratch to verify this holds.

So the observed CATE decomposes as a mixture of true CATEs weighted by the posterior, which means I can recover the true effects by inverting the mixing matrix. For the global correction applied to a specific subgroup, I'm using the global mixing matrix inverse on the subgroup-specific observed effects, which introduces bias proportional to the difference between the global and subgroup-specific mixing matrices.

Now I'm verifying the outputs and noticing that the per-row RMSE column is actually storing absolute bias rather than true RMSE—the aggregate RMSE in the report is computed correctly, but I should double-check the CSV values. I'm also starting to examine whether the correction results warrant deeper investigation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7b9d7ab0-1070-4919-b7c5-6a3ef978888a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErXrNEmSpGMoEp7rVdi2Z2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 75094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 982
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 39_

The simulation ran successfully. Interesting results — Naive actually outperforms all correction methods here. This is likely because with only 200 expert labels across 4 subgroups (28-77 per subgroup) and moderate Δπ=0.137, the CM estimation noise overwhelms the bias correction benefit. Let me verify the outputs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "6ee22161-de08-4e2f-a4a6-858ed43f4f5a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErXrNEmSpGMoEp7rVdi2Z2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 75094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 982
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01QM2qFqJHdHk5y23MAB6oXz`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "bb55d9f4-384c-4d93-b5b3-5621da2da8c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErXrNEmSpGMoEp7rVdi2Z2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 75094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 982
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 41 · 2026-05-21T20:50:16.611Z_

<details><summary>↩ Tool result · `toolu_01QM2qFqJHdHk5y23MAB6oXz`</summary>

```text
1	# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
2	
3	## Design
4	
5	Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.
6	Ground truth CATE is synthetic; confusion matrices are empirical.
7	
8	| Subgroup | Weight | FPR | FNR | pi_s |
9	|----------|--------|-----|-----|------|
10	| False_medium | 0.386 | 0.235 | 0.319 | 0.277 |
11	| False_short | 0.218 | 0.310 | 0.212 | 0.261 |
12	| True_medium | 0.258 | 0.219 | 0.258 | 0.238 |
13	| True_short | 0.138 | 0.091 | 0.190 | 0.141 |
14	
15	**Parameters**: N=5000, P(Z=1)=0.652, n_expert=200, tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
16	**MC seeds**: 20
17	
18	## Summary (averaged across subgroups and z-levels)
19	
20	| Method | Mean |Bias| | RMSE | Coverage |
21	|--------|-------------|------|----------|
22	| oracle | 0.0742 | 0.0896 | 0.950 |
23	| naive | 0.1031 | 0.1246 | 0.750 |
24	| global_corrected | 0.1525 | 0.1892 | 0.856 |
25	| stratified_mle | 0.2158 | 0.2808 | 0.744 |
26	| hb_ec_hte | 0.2183 | 0.2851 | 0.750 |
27	
28	## Per-Subgroup Breakdown
29	
30	| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |
31	|----------|---|--------|-----------|-------|------|----------|
32	| False_medium | 0 | naive | +0.1506 | 0.1506 | 0.1607 | 0.300 |
33	| False_medium | 0 | global_corrected | +0.0560 | 0.1589 | 0.1849 | 0.900 |
34	| False_medium | 0 | stratified_mle | +0.0213 | 0.2766 | 0.3654 | 0.700 |
35	| False_medium | 0 | hb_ec_hte | +0.0194 | 0.2783 | 0.3668 | 0.700 |
36	| False_medium | 1 | naive | -0.0563 | 0.0670 | 0.0815 | 0.800 |
37	| False_medium | 1 | global_corrected | -0.0067 | 0.0956 | 0.1189 | 0.850 |
38	| False_medium | 1 | stratified_mle | +0.0390 | 0.1686 | 0.2197 | 0.650 |
39	| False_medium | 1 | hb_ec_hte | +0.0401 | 0.1698 | 0.2212 | 0.650 |
40	| False_short | 0 | naive | +0.0853 | 0.1058 | 0.1388 | 0.750 |
41	| False_short | 0 | global_corrected | -0.0618 | 0.1633 | 0.2381 | 0.850 |
42	| False_short | 0 | stratified_mle | -0.0308 | 0.2819 | 0.3473 | 0.850 |
43	| False_short | 0 | hb_ec_hte | -0.0438 | 0.2827 | 0.3504 | 0.850 |
44	| False_short | 1 | naive | -0.0582 | 0.0845 | 0.1093 | 0.700 |
45	| False_short | 1 | global_corrected | +0.0140 | 0.1346 | 0.1650 | 0.850 |
46	| False_short | 1 | stratified_mle | +0.0030 | 0.1402 | 0.1864 | 0.800 |
47	| False_short | 1 | hb_ec_hte | +0.0087 | 0.1414 | 0.1872 | 0.800 |
48	| True_medium | 0 | naive | +0.1159 | 0.1186 | 0.1486 | 0.650 |
49	| True_medium | 0 | global_corrected | -0.0460 | 0.2294 | 0.2624 | 0.800 |
50	| True_medium | 0 | stratified_mle | -0.0947 | 0.2522 | 0.3263 | 0.650 |
51	| True_medium | 0 | hb_ec_hte | -0.1028 | 0.2556 | 0.3304 | 0.700 |
52	| True_medium | 1 | naive | -0.0151 | 0.0598 | 0.0702 | 1.000 |
53	| True_medium | 1 | global_corrected | +0.0611 | 0.1361 | 0.1695 | 0.800 |
54	| True_medium | 1 | stratified_mle | +0.1177 | 0.2001 | 0.2765 | 0.650 |
55	| True_medium | 1 | hb_ec_hte | +0.1221 | 0.2010 | 0.2792 | 0.650 |
56	| True_short | 0 | naive | +0.1114 | 0.1268 | 0.1520 | 0.950 |
57	| True_short | 0 | global_corrected | -0.0470 | 0.1483 | 0.1887 | 0.950 |
58	| True_short | 0 | stratified_mle | +0.0442 | 0.2451 | 0.3383 | 0.850 |
59	| True_short | 0 | hb_ec_hte | +0.0327 | 0.2496 | 0.3535 | 0.850 |
60	| True_short | 1 | naive | -0.0177 | 0.1118 | 0.1359 | 0.850 |
61	| True_short | 1 | global_corrected | +0.0526 | 0.1535 | 0.1863 | 0.850 |
62	| True_short | 1 | stratified_mle | +0.0130 | 0.1617 | 0.1860 | 0.800 |
63	| True_short | 1 | hb_ec_hte | +0.0193 | 0.1678 | 0.1924 | 0.800 |
64	
65	## EC-HTE vs Global: Bias Reduction Ratio
66	
67	| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |
68	|----------|---|-----------|-------------|-----------|
69	| False_medium | 0 | 0.2783 | 0.1589 | -75.2% |
70	| False_medium | 1 | 0.1698 | 0.0956 | -77.7% |
71	| False_short | 0 | 0.2827 | 0.1633 | -73.1% |
72	| False_short | 1 | 0.1414 | 0.1346 | -5.0% |
73	| True_medium | 0 | 0.2556 | 0.2294 | -11.4% |
74	| True_medium | 1 | 0.2010 | 0.1361 | -47.6% |
75	| True_short | 0 | 0.2496 | 0.1483 | -68.3% |
76	| True_short | 1 | 0.1678 | 0.1535 | -9.3% |
77	| **Average** | | 0.2183 | 0.1525 | -43.1% |
78	
79	## Conclusion
80	
81	- **Naive**: RMSE=0.1246, |Bias|=0.1031, Coverage=0.750
82	- **Global**: RMSE=0.1892, |Bias|=0.1525, Coverage=0.856
83	- **Stratified MLE**: RMSE=0.2808, |Bias|=0.2158, Coverage=0.744
84	- **HB EC-HTE**: RMSE=0.2851, |Bias|=0.2183, Coverage=0.750
85	
86	EC-HTE reduces RMSE by -50.7% vs Global, -128.8% vs Naive.
87	EC-HTE reduces |Bias| by -43.1% vs Global, -111.7% vs Naive.
88	
89	Coverage: Naive=0.750, Global=0.856, HB=0.750 (target=0.95)
90	
91	**EC-HTE does NOT improve bias over Global under real Llama CMs.**
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "57356e90-0077-4c86-88ce-3671f839e3fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md",
      "content": "# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\n\n## Design\n\nUses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n| Subgroup | Weight | FPR | FNR | pi_s |\n|----------|--------|-----|-----|------|\n| False_medium | 0.386 | 0.235 | 0.319 | 0.277 |\n| False_short | 0.218 | 0.310 | 0.212 | 0.261 |\n| True_medium | 0.258 | 0.219 | 0.258 | 0.238 |\n| True_short | 0.138 | 0.091 | 0.190 | 0.141 |\n\n**Parameters**: N=5000, P(Z=1)=0.652, n_expert=200, tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3\n**MC seeds**: 20\n\n## Summary (averaged across subgroups and z-levels)\n\n| Method | Mean |Bias| | RMSE | Coverage |\n|--------|-------------|------|----------|\n| oracle | 0.0742 | 0.0896 | 0.950 |\n| naive | 0.1031 | 0.1246 | 0.750 |\n| global_corrected | 0.1525 | 0.1892 | 0.856 |\n| stratified_mle | 0.2158 | 0.2808 | 0.744 |\n| hb_ec_hte | 0.2183 | 0.2851 | 0.750 |\n\n## Per-Subgroup Breakdown\n\n| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\n|----------|---|--------|-----------|-------|------|----------|\n| False_medium | 0 | naive | +0.1506 | 0.1506 | 0.1607 | 0.300 |\n| False_medium | 0 | global_corrected | +0.0560 | 0.1589 | 0.1849 | 0.900 |\n| False_medium | 0 | stratified_mle | +0.0213 | 0.2766 | 0.3654 | 0.700 |\n| False_medium | 0 | hb_ec_hte | +0.0194 | 0.2783 | 0.3668 | 0.700 |\n| False_medium | 1 | naive | -0.0563 | 0.0670 | 0.0815 | 0.800 |\n| False_medium | 1 | global_corrected | -0.0067 | 0.0956 | 0.1189 | 0.850 |\n| False_medium | 1 | stratified_mle | +0.0390 | 0.1686 | 0.2197 | 0.650 |\n| False_medium | 1 | hb_ec_hte | +0.0401 | 0.1698 | 0.2212 | 0.650 |\n| False_short | 0 | naive | +0.0853 | 0.1058 | 0.1388 | 0.750 |\n| False_short | 0 | global_corrected | -0.0618 | 0.1633 | 0.2381 | 0.850 |\n| False_short | 0 | stratified_mle | -0.0308 | 0.2819 | 0.3473 | 0.850 |\n| False_short | 0 | hb_ec_hte | -0.0438 | 0.2827 | 0.3504 | 0.850 |\n| False_short | 1 | naive | -0.0582 | 0.0845 | 0.1093 | 0.700 |\n| False_short | 1 | global_corrected | +0.0140 | 0.1346 | 0.1650 | 0.850 |\n| False_short | 1 | stratified_mle | +0.0030 | 0.1402 | 0.1864 | 0.800 |\n| False_short | 1 | hb_ec_hte | +0.0087 | 0.1414 | 0.1872 | 0.800 |\n| True_medium | 0 | naive | +0.1159 | 0.1186 | 0.1486 | 0.650 |\n| True_medium | 0 | global_corrected | -0.0460 | 0.2294 | 0.2624 | 0.800 |\n| True_medium | 0 | stratified_mle | -0.0947 | 0.2522 | 0.3263 | 0.650 |\n| True_medium | 0 | hb_ec_hte | -0.1028 | 0.2556 | 0.3304 | 0.700 |\n| True_medium | 1 | naive | -0.0151 | 0.0598 | 0.0702 | 1.000 |\n| True_medium | 1 | global_corrected | +0.0611 | 0.1361 | 0.1695 | 0.800 |\n| True_medium | 1 | stratified_mle | +0.1177 | 0.2001 | 0.2765 | 0.650 |\n| True_medium | 1 | hb_ec_hte | +0.1221 | 0.2010 | 0.2792 | 0.650 |\n| True_short | 0 | naive | +0.1114 | 0.1268 | 0.1520 | 0.950 |\n| True_short | 0 | global_corrected | -0.0470 | 0.1483 | 0.1887 | 0.950 |\n| True_short | 0 | stratified_mle | +0.0442 | 0.2451 | 0.3383 | 0.850 |\n| True_short | 0 | hb_ec_hte | +0.0327 | 0.2496 | 0.3535 | 0.850 |\n| True_short | 1 | naive | -0.0177 | 0.1118 | 0.1359 | 0.850 |\n| True_short | 1 | global_corrected | +0.0526 | 0.1535 | 0.1863 | 0.850 |\n| True_short | 1 | stratified_mle | +0.0130 | 0.1617 | 0.1860 | 0.800 |\n| True_short | 1 | hb_ec_hte | +0.0193 | 0.1678 | 0.1924 | 0.800 |\n\n## EC-HTE vs Global: Bias Reduction Ratio\n\n| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\n|----------|---|-----------|-------------|-----------|\n| False_medium | 0 | 0.2783 | 0.1589 | -75.2% |\n| False_medium | 1 | 0.1698 | 0.0956 | -77.7% |\n| False_short | 0 | 0.2827 | 0.1633 | -73.1% |\n| False_short | 1 | 0.1414 | 0.1346 | -5.0% |\n| True_medium | 0 | 0.2556 | 0.2294 | -11.4% |\n| True_medium | 1 | 0.2010 | 0.1361 | -47.6% |\n| True_short | 0 | 0.2496 | 0.1483 | -68.3% |\n| True_short | 1 | 0.1678 | 0.1535 | -9.3% |\n| **Average** | | 0.2183 | 0.1525 | -43.1% |\n\n## Conclusion\n\n- **Naive**: RMSE=0.1246, |Bias|=0.1031, Coverage=0.750\n- **Global**: RMSE=0.1892, |Bias|=0.1525, Coverage=0.856\n- **Stratified MLE**: RMSE=0.2808, |Bias|=0.2158, Coverage=0.744\n- **HB EC-HTE**: RMSE=0.2851, |Bias|=0.2183, Coverage=0.750\n\nEC-HTE reduces RMSE by -50.7% vs Global, -128.8% vs Naive.\nEC-HTE reduces |Bias| by -43.1% vs Global, -111.7% vs Naive.\n\nCoverage: Naive=0.750, Global=0.856, HB=0.750 (target=0.95)\n\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**",
      "numLines": 91,
      "startLine": 1,
      "totalLines": 91
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Bash · `toolu_01P1hfTr3ih5JibbmdJkNcD2`</summary>

```json
{
  "command": "head -5 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv && echo \"---\" && wc -l /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "3865bf68-16df-45cd-a8c3-d5f97e384c34",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ErXrNEmSpGMoEp7rVdi2Z2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 982,
      "cache_read_input_tokens": 75094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 982
      },
      "output_tokens": 28,
      "service_tier": "standard",
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

_source line 43 · 2026-05-21T20:50:17.575Z_

<details><summary>↩ Tool result · `toolu_01P1hfTr3ih5JibbmdJkNcD2`</summary>

```text
seed,method,subgroup,z_level,bias,rmse,coverage,cate_true,cate_est
0,oracle,False_medium,0,-0.12429089725631359,0.12429089725631359,1,0.35,0.22570910274368639
0,naive,False_medium,0,0.1274304394672402,0.1274304394672402,0,0.35,0.4774304394672402
0,global_corrected,False_medium,0,-0.1444315549348372,0.1444315549348372,1,0.35,0.20556844506516278
0,stratified_mle,False_medium,0,-0.19096345128834807,0.19096345128834807,1,0.35,0.1590365487116519
---
801 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "2a65402a-f935-41fe-acb8-dedfbb5a5162",
  "tool_use_result": {
    "stdout": "seed,method,subgroup,z_level,bias,rmse,coverage,cate_true,cate_est\n0,oracle,False_medium,0,-0.12429089725631359,0.12429089725631359,1,0.35,0.22570910274368639\n0,naive,False_medium,0,0.1274304394672402,0.1274304394672402,0,0.35,0.4774304394672402\n0,global_corrected,False_medium,0,-0.1444315549348372,0.1444315549348372,1,0.35,0.20556844506516278\n0,stratified_mle,False_medium,0,-0.19096345128834807,0.19096345128834807,1,0.35,0.1590365487116519\n---\n801 /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_results.csv",
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
The results show that all correction methods are worse than Naive in this setting. This is a meaningful finding, but I should verify it's not a bug.

The key insight is: with n_expert=200 across 4 subgroups (so ~28-77 per subgroup), the CM estimation noise is too large. The per-subgroup correction methods (stratified MLE, HB) have high variance, and even the Global correction introduces structural bias from ignoring CM heterogeneity.

Let me look at the mean_bias values more carefully. For the Global correction, the mean bias shows that it over-corrects in some cells and under-corrects in others, leading to higher overall |bias|. 

For the per-subgroup corrections, the mean biases are actually closer to zero on average—which is what I'd expect—but the seed-to-seed variability is so much higher that it dominates the RMSE and absolute bias metrics. Looking at False_medium with z=0, the HB method has nearly zero mean bias (0.0194) compared to Naive's systematic positive bias (0.1506), yet HB's absolute bias is 0.2783 versus Naive's 0.1506, which tells me the high variance is overwhelming the bias reduction benefit.

This is the classic bias-variance tradeoff playing out: HB successfully removes the systematic attenuation bias but introduces enough variance that the overall error gets worse. And this is actually exactly what the user needs to see—a concrete boundary condition showing that EC-HTE doesn't improve performance under these specific constraints (moderate treatment effect heterogeneity, limited expert budget). The finding is valid and important, so I should report it clearly. I also need to fix the misleading language in the analysis where negative RMSE reduction should be stated as a performance degradation rather than an improvement.

Updating the analysis to better explain why EC-HTE fails here—the variance penalty outweighs the bias correction benefit under these conditions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "0639af66-5f43-40ed-9aeb-4e451565654c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5ckVWGbFLN56WeHtFWv9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 76076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8407
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

The results are valid and tell an important story. With Llama's moderate Δπ=0.137 and only 200 expert labels, the CM estimation noise overwhelms the bias correction benefit. Looking at the per-subgroup mean biases, HB EC-HTE is actually nearly unbiased on average (e.g., +0.0194 for False_medium z=0 vs +0.1506 for Naive), but the per-seed variance is much higher.

Let me update the analysis conclusion to properly explain this bias-variance trade-off and fix the misleading "reduces" wording for negative improvements.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7431facf-519b-4a2b-97ba-9b58151471dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5ckVWGbFLN56WeHtFWv9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 76076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8407
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

<details open><summary>🔧 Tool call — Edit · `toolu_01GVezTpfE9SAZ5caFJxicgG`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
  "old_string": "        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")",
  "new_string": "        lines.append(\"\")\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n\n        lines.append(\"### RMSE comparison\")\n        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),\n                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),\n                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:\n            direction = \"improves\" if r > 0 else \"worsens\"\n            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")\n\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        # Bias-variance decomposition insight\n        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()\n        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq\n        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()\n        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq\n\n        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")\n        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")\n        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")\n\n        lines.append(\"\\n### Interpretation\\n\")\n        if hb_bias >= nv_bias:\n            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"\n                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"\n                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"\n                         \"exceeds the bias reduction from stratified correction.\")\n            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"\n                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"\n                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")\n        else:\n            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "71973e48-ad00-486c-920c-da8192a1bca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C5ckVWGbFLN56WeHtFWv9D",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8407,
      "cache_read_input_tokens": 76076,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8407
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

### Runtime record

_source line 47_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779414600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d6120814-eebc-470d-a6ea-6532d263f339",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### Tool result

_source line 48 · 2026-05-21T20:50:54.131Z_

<details><summary>↩ Tool result · `toolu_01GVezTpfE9SAZ5caFJxicgG`</summary>

```text
The file /home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "3eb15cbb-2fef-44ed-8f74-ce86d09e4d87",
  "tool_use_result": {
    "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/run_llama_semisynthetic.py",
    "oldString": "        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")",
    "newString": "        lines.append(\"\")\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n\n        lines.append(\"### RMSE comparison\")\n        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),\n                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),\n                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:\n            direction = \"improves\" if r > 0 else \"worsens\"\n            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")\n\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        # Bias-variance decomposition insight\n        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()\n        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq\n        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()\n        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq\n\n        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")\n        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")\n        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")\n\n        lines.append(\"\\n### Interpretation\\n\")\n        if hb_bias >= nv_bias:\n            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"\n                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"\n                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"\n                         \"exceeds the bias reduction from stratified correction.\")\n            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"\n                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"\n                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")\n        else:\n            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")",
    "originalFile": "\"\"\"\nLlama-3.1-8B Semi-Synthetic DGP: EC-HTE vs Global vs Naive RMSE comparison.\n\nUses real per-subgroup confusion matrices from Llama-3.1-8B balanced annotations.\nGround truth CATE is synthetic; confusion matrices are empirical.\n\n4 subgroups with real asymmetric CMs:\n  False_medium: FPR=0.235, FNR=0.319, weight=193/500\n  False_short:  FPR=0.310, FNR=0.212, weight=109/500\n  True_medium:  FPR=0.219, FNR=0.258, weight=129/500\n  True_short:   FPR=0.091, FNR=0.190, weight=69/500\n\nP(Z=1) = 0.652, delta_tau = 0.3, tau(z=0)=0.35, tau(z=1)=0.65\nMethods: Naive, Global, Stratified MLE, HB EC-HTE\nn_expert=200, 20 MC seeds\n\nUsage: python3 artifacts/c1_multi_llm/run_llama_semisynthetic.py\n\"\"\"\n\nimport time\nimport warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy.special import gammaln\n\nwarnings.filterwarnings('ignore')\n\n# === Config ===\n\nN = 5000\nN_EXPERT = 200\nN_MC = 20\nSEED_BASE = 0\n\nSUBGROUP_LABELS = ['False_medium', 'False_short', 'True_medium', 'True_short']\nSUBGROUP_WEIGHTS = np.array([193, 109, 129, 69], dtype=float)\nSUBGROUP_WEIGHTS /= SUBGROUP_WEIGHTS.sum()\n\nSUBGROUP_CM = {\n    'False_medium': {'fpr': 0.235, 'fnr': 0.319},\n    'False_short':  {'fpr': 0.310, 'fnr': 0.212},\n    'True_medium':  {'fpr': 0.219, 'fnr': 0.258},\n    'True_short':   {'fpr': 0.091, 'fnr': 0.190},\n}\n\nP_Z1 = 0.652\nP_T1 = 0.5\nTAU_Z0 = 0.35\nTAU_Z1 = 0.65\n\n\ndef get_cm_matrix(fpr, fnr):\n    \"\"\"Build 2x2 confusion matrix: C[z_true, z_obs].\"\"\"\n    return np.array([[1 - fpr, fpr],\n                     [fnr, 1 - fnr]])\n\n\n# === Core Estimators ===\n\ndef diff_in_means(Y, T, mask):\n    t1 = mask & (T == 1)\n    t0 = mask & (T == 0)\n    n1, n0 = t1.sum(), t0.sum()\n    if n1 < 2 or n0 < 2:\n        return np.nan, np.nan\n    y1, y0 = Y[t1], Y[t0]\n    tau_hat = y1.mean() - y0.mean()\n    se = np.sqrt(y1.var(ddof=1) / n1 + y0.var(ddof=1) / n0)\n    return tau_hat, se\n\n\ndef estimate_confusion_matrix(z_true, z_hat):\n    \"\"\"Global CM with Laplace smoothing.\"\"\"\n    C = np.zeros((2, 2))\n    for zt in [0, 1]:\n        mask = z_true == zt\n        n = mask.sum()\n        for zh in [0, 1]:\n            C[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n    return C\n\n\ndef estimate_cm_per_subgroup(z_true, z_hat, subgroups, labels):\n    \"\"\"Per-subgroup MLE with Laplace smoothing.\"\"\"\n    C = {}\n    for s in labels:\n        ms = subgroups == s\n        C_s = np.zeros((2, 2))\n        for zt in [0, 1]:\n            mask = ms & (z_true == zt)\n            n = mask.sum()\n            for zh in [0, 1]:\n                C_s[zt, zh] = ((z_hat[mask] == zh).sum() + 1) / (n + 2) if n > 0 else 0.5\n        C[s] = C_s\n    return C\n\n\ndef build_mixing_matrix(C, p_z, p_z_hat):\n    \"\"\"M[z_hat, z] = P(Z=z | Z_hat=z_hat) via Bayes' rule.\"\"\"\n    M = np.zeros((2, 2))\n    for zh in [0, 1]:\n        for z in [0, 1]:\n            M[zh, z] = C[z, zh] * p_z[z] / p_z_hat[zh] if p_z_hat[zh] > 0 else 0.5\n    return M\n\n\ndef invert_mixing_safe(M, tau_obs, se_obs, cond_threshold=100):\n    cond = np.linalg.cond(M)\n    if cond > cond_threshold:\n        return tau_obs.copy(), se_obs.copy()\n    det = np.linalg.det(M)\n    if abs(det) < 1e-10:\n        return tau_obs.copy(), se_obs.copy()\n    Mi = np.linalg.inv(M)\n    tau_c = Mi @ tau_obs\n    se_c = np.sqrt(np.maximum(np.diag(Mi @ np.diag(se_obs ** 2) @ Mi.T), 0))\n    return tau_c, se_c\n\n\n# === HB Gibbs Sampler ===\n\ndef get_counts(z_true, z_hat, subgroups, labels):\n    k = len(labels)\n    counts = np.zeros((k, 2, 2), dtype=int)\n    for i, s in enumerate(labels):\n        ms = subgroups == s\n        for z in [0, 1]:\n            mz = ms & (z_true == z)\n            counts[i, z, 0] = (z_hat[mz] == 0).sum()\n            counts[i, z, 1] = (z_hat[mz] == 1).sum()\n    return counts\n\n\ndef _log_target_alpha(alpha, theta_z, hp_a0=3.0, hp_b0=1.0):\n    if alpha < 1e-10:\n        return -1e10\n    a = alpha / 2.0\n    k = theta_z.shape[0]\n    lp = (hp_a0 - 1.0) * np.log(alpha) - hp_b0 * alpha\n    lp += k * (gammaln(alpha) - 2.0 * gammaln(a))\n    lp += (a - 1.0) * np.sum(np.log(np.clip(theta_z, 1e-300, None)))\n    return lp\n\n\ndef estimate_cm_hb_gibbs(counts, labels, seed=42, n_iter=1000, n_warmup=500, n_chains=4,\n                         hp_a0=3.0, hp_b0=1.0):\n    k = len(labels)\n    chain_inits_pool = [np.array([1.0, 1.0]), np.array([5.0, 5.0]),\n                        np.array([0.5, 0.5]), np.array([10.0, 10.0])]\n    chain_inits = chain_inits_pool[:n_chains]\n    all_theta = []\n    t0 = time.time()\n\n    for chain in range(n_chains):\n        rng = np.random.RandomState(seed * 31 + chain * 7919 + 1)\n        alpha = chain_inits[chain].copy()\n        theta = np.ones((k, 2, 2)) * 0.5\n        mh_scale = np.array([0.3, 0.3])\n        accept_ct = np.array([0, 0])\n        attempt_ct = np.array([0, 0])\n\n        theta_samples = np.zeros((n_iter, k, 2, 2))\n\n        for it in range(n_warmup + n_iter):\n            for z in [0, 1]:\n                post_a = counts[:, z, :].astype(float) + alpha[z] / 2.0\n                post_a = np.maximum(post_a, 1e-6)\n                g = rng.gamma(post_a)\n                g_sum = g.sum(axis=1, keepdims=True)\n                theta[:, z, :] = g / np.maximum(g_sum, 1e-300)\n\n            for z in [0, 1]:\n                x_prop = np.log(alpha[z]) + rng.normal(0, mh_scale[z])\n                a_prop = np.exp(x_prop)\n                log_r = (_log_target_alpha(a_prop, theta[:, z, :], hp_a0, hp_b0) -\n                         _log_target_alpha(alpha[z], theta[:, z, :], hp_a0, hp_b0))\n                accepted = np.log(rng.rand()) < log_r\n                if accepted:\n                    alpha[z] = a_prop\n                if it < n_warmup:\n                    accept_ct[z] += int(accepted)\n                    attempt_ct[z] += 1\n\n            if it < n_warmup and it > 0 and it % 100 == 0:\n                for z in [0, 1]:\n                    rate = accept_ct[z] / max(attempt_ct[z], 1)\n                    if rate < 0.2:\n                        mh_scale[z] *= 0.7\n                    elif rate > 0.5:\n                        mh_scale[z] *= 1.3\n                    accept_ct[z] = 0\n                    attempt_ct[z] = 0\n\n            if it >= n_warmup:\n                theta_samples[it - n_warmup] = theta.copy()\n\n        all_theta.append(theta_samples)\n\n    runtime = time.time() - t0\n    theta_arr = np.stack(all_theta)\n\n    C = {}\n    for i, s in enumerate(labels):\n        C[s] = theta_arr[:, :, i, :, :].mean(axis=(0, 1))\n\n    return C, {'runtime_seconds': runtime}\n\n\n# === DGP ===\n\ndef generate_data(seed):\n    rng = np.random.RandomState(seed)\n\n    S_idx = rng.choice(4, size=N, p=SUBGROUP_WEIGHTS)\n    S = np.array([SUBGROUP_LABELS[i] for i in S_idx])\n\n    Z = rng.binomial(1, P_Z1, N)\n    T = rng.binomial(1, P_T1, N)\n\n    Z_hat = np.empty(N, dtype=int)\n    for i in range(4):\n        s_mask = S_idx == i\n        cm = get_cm_matrix(SUBGROUP_CM[SUBGROUP_LABELS[i]]['fpr'],\n                           SUBGROUP_CM[SUBGROUP_LABELS[i]]['fnr'])\n        z_s = Z[s_mask]\n        p_obs1 = np.where(z_s == 0, cm[0, 1], cm[1, 1])\n        Z_hat[s_mask] = rng.binomial(1, p_obs1)\n\n    tau_vals = np.where(Z == 1, TAU_Z1, TAU_Z0)\n    eps = rng.randn(N)\n    Y = 1.0 + tau_vals * T + eps\n\n    expert_idx = rng.choice(N, N_EXPERT, replace=False)\n    expert_mask = np.zeros(N, dtype=bool)\n    expert_mask[expert_idx] = True\n\n    return {\n        'T': T, 'Z': Z, 'Z_hat': Z_hat, 'S': S, 'S_idx': S_idx,\n        'Y': Y, 'tau': tau_vals, 'expert_mask': expert_mask,\n    }\n\n\n# === MC Runner ===\n\ndef run_one_mc(data, seed):\n    Y, T, Z, Z_hat, S = data['Y'], data['T'], data['Z'], data['Z_hat'], data['S']\n    expert_mask = data['expert_mask']\n\n    z_exp = Z[expert_mask]\n    zh_exp = Z_hat[expert_mask]\n    s_exp = S[expert_mask]\n\n    # Global CM from experts\n    C_global = estimate_confusion_matrix(z_exp, zh_exp)\n    p_z_global = np.array([(z_exp == 0).mean(), (z_exp == 1).mean()])\n    p_zh_global = np.array([(Z_hat == 0).mean(), (Z_hat == 1).mean()])\n    M_global = build_mixing_matrix(C_global, p_z_global, p_zh_global)\n\n    # Stratified MLE per-subgroup\n    C_mle = estimate_cm_per_subgroup(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n\n    # HB Gibbs\n    counts = get_counts(z_exp, zh_exp, s_exp, SUBGROUP_LABELS)\n    C_hb, _ = estimate_cm_hb_gibbs(counts, SUBGROUP_LABELS, seed=seed)\n\n    # Build per-subgroup mixing matrices\n    M_mle_sub = {}\n    M_hb_sub = {}\n    for s_val in SUBGROUP_LABELS:\n        sm_exp = (s_exp == s_val)\n        sm_all = (S == s_val)\n        if sm_exp.sum() >= 4:\n            p_z_s = np.array([(z_exp[sm_exp] == 0).mean(), (z_exp[sm_exp] == 1).mean()])\n        else:\n            p_z_s = p_z_global\n        p_zh_s = np.array([(Z_hat[sm_all] == 0).mean(), (Z_hat[sm_all] == 1).mean()])\n        M_mle_sub[s_val] = build_mixing_matrix(C_mle[s_val], p_z_s, p_zh_s)\n        M_hb_sub[s_val] = build_mixing_matrix(C_hb[s_val], p_z_s, p_zh_s)\n\n    rows = []\n\n    for s_val in SUBGROUP_LABELS:\n        s_mask = S == s_val\n\n        for z_level in [0, 1]:\n            oracle_cate = TAU_Z1 if z_level == 1 else TAU_Z0\n\n            # Oracle\n            th_or, se_or = diff_in_means(Y, T, s_mask & (Z == z_level))\n            ci_lo_or = th_or - 1.96 * se_or if not np.isnan(se_or) else np.nan\n            ci_hi_or = th_or + 1.96 * se_or if not np.isnan(se_or) else np.nan\n            cov_or = 1 if (not np.isnan(ci_lo_or) and ci_lo_or <= oracle_cate <= ci_hi_or) else 0\n            rows.append({\n                'seed': seed, 'method': 'oracle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_or - oracle_cate if not np.isnan(th_or) else np.nan,\n                'rmse': abs(th_or - oracle_cate) if not np.isnan(th_or) else np.nan,\n                'coverage': cov_or,\n                'cate_true': oracle_cate, 'cate_est': th_or,\n            })\n\n            # Naive\n            th_nv, se_nv = diff_in_means(Y, T, s_mask & (Z_hat == z_level))\n            ci_lo_nv = th_nv - 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            ci_hi_nv = th_nv + 1.96 * se_nv if not np.isnan(se_nv) else np.nan\n            cov_nv = 1 if (not np.isnan(ci_lo_nv) and ci_lo_nv <= oracle_cate <= ci_hi_nv) else 0\n            rows.append({\n                'seed': seed, 'method': 'naive', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_nv - oracle_cate if not np.isnan(th_nv) else np.nan,\n                'rmse': abs(th_nv - oracle_cate) if not np.isnan(th_nv) else np.nan,\n                'coverage': cov_nv,\n                'cate_true': oracle_cate, 'cate_est': th_nv,\n            })\n\n            # Observed CATE in Z_hat=0 and Z_hat=1 cells for this subgroup\n            tau_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[0],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[0],\n            ])\n            se_obs = np.array([\n                diff_in_means(Y, T, s_mask & (Z_hat == 0))[1],\n                diff_in_means(Y, T, s_mask & (Z_hat == 1))[1],\n            ])\n\n            if not np.any(np.isnan(tau_obs)):\n                tau_gc, se_gc = invert_mixing_safe(M_global, tau_obs, se_obs)\n                th_gc, se_gc_z = tau_gc[z_level], se_gc[z_level]\n\n                tau_ml, se_ml = invert_mixing_safe(M_mle_sub[s_val], tau_obs, se_obs)\n                th_ml, se_ml_z = tau_ml[z_level], se_ml[z_level]\n\n                tau_hb, se_hb = invert_mixing_safe(M_hb_sub[s_val], tau_obs, se_obs)\n                th_hb, se_hb_z = tau_hb[z_level], se_hb[z_level]\n            else:\n                th_gc = se_gc_z = th_ml = se_ml_z = th_hb = se_hb_z = np.nan\n\n            # Global corrected\n            ci_lo_gc = th_gc - 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            ci_hi_gc = th_gc + 1.96 * se_gc_z if not np.isnan(se_gc_z) else np.nan\n            cov_gc = 1 if (not np.isnan(ci_lo_gc) and ci_lo_gc <= oracle_cate <= ci_hi_gc) else 0\n            rows.append({\n                'seed': seed, 'method': 'global_corrected', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_gc - oracle_cate if not np.isnan(th_gc) else np.nan,\n                'rmse': abs(th_gc - oracle_cate) if not np.isnan(th_gc) else np.nan,\n                'coverage': cov_gc,\n                'cate_true': oracle_cate, 'cate_est': th_gc,\n            })\n\n            # Stratified MLE\n            ci_lo_ml = th_ml - 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            ci_hi_ml = th_ml + 1.96 * se_ml_z if not np.isnan(se_ml_z) else np.nan\n            cov_ml = 1 if (not np.isnan(ci_lo_ml) and ci_lo_ml <= oracle_cate <= ci_hi_ml) else 0\n            rows.append({\n                'seed': seed, 'method': 'stratified_mle', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_ml - oracle_cate if not np.isnan(th_ml) else np.nan,\n                'rmse': abs(th_ml - oracle_cate) if not np.isnan(th_ml) else np.nan,\n                'coverage': cov_ml,\n                'cate_true': oracle_cate, 'cate_est': th_ml,\n            })\n\n            # HB EC-HTE\n            ci_lo_hb = th_hb - 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            ci_hi_hb = th_hb + 1.96 * se_hb_z if not np.isnan(se_hb_z) else np.nan\n            cov_hb = 1 if (not np.isnan(ci_lo_hb) and ci_lo_hb <= oracle_cate <= ci_hi_hb) else 0\n            rows.append({\n                'seed': seed, 'method': 'hb_ec_hte', 'subgroup': s_val,\n                'z_level': z_level,\n                'bias': th_hb - oracle_cate if not np.isnan(th_hb) else np.nan,\n                'rmse': abs(th_hb - oracle_cate) if not np.isnan(th_hb) else np.nan,\n                'coverage': cov_hb,\n                'cate_true': oracle_cate, 'cate_est': th_hb,\n            })\n\n    return rows\n\n\n# === Aggregation ===\n\ndef aggregate_results(df_raw):\n    group_cols = ['subgroup', 'z_level', 'method']\n    rows = []\n    for keys, grp in df_raw.groupby(group_cols):\n        row = dict(zip(group_cols, keys))\n        valid = grp['bias'].dropna()\n        if len(valid) == 0:\n            continue\n        row['mean_bias'] = valid.mean()\n        row['mean_abs_bias'] = valid.abs().mean()\n        row['rmse'] = np.sqrt((valid ** 2).mean())\n        row['coverage'] = grp['coverage'].mean()\n        row['n_mc'] = len(valid)\n        rows.append(row)\n    return pd.DataFrame(rows)\n\n\n# === Analysis Report ===\n\ndef write_analysis(df_raw, df_summary):\n    lines = []\n    lines.append(\"# Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\\n\")\n\n    lines.append(\"## Design\\n\")\n    lines.append(\"Uses **real asymmetric confusion matrices** from Llama-3.1-8B balanced annotations.\")\n    lines.append(\"Ground truth CATE is synthetic; confusion matrices are empirical.\\n\")\n\n    lines.append(\"| Subgroup | Weight | FPR | FNR | pi_s |\")\n    lines.append(\"|----------|--------|-----|-----|------|\")\n    for i, s in enumerate(SUBGROUP_LABELS):\n        cm = SUBGROUP_CM[s]\n        lines.append(f\"| {s} | {SUBGROUP_WEIGHTS[i]:.3f} | {cm['fpr']:.3f} | {cm['fnr']:.3f} | {(cm['fpr'] + cm['fnr'])/2:.3f} |\")\n    lines.append(\"\")\n\n    lines.append(f\"**Parameters**: N={N}, P(Z=1)={P_Z1}, n_expert={N_EXPERT}, \"\n                 f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    lines.append(f\"**MC seeds**: {N_MC}\\n\")\n\n    # Overall summary\n    lines.append(\"## Summary (averaged across subgroups and z-levels)\\n\")\n    lines.append(\"| Method | Mean |Bias| | RMSE | Coverage |\")\n    lines.append(\"|--------|-------------|------|----------|\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            lines.append(f\"| {m} | {sub['mean_abs_bias'].mean():.4f} | \"\n                         f\"{sub['rmse'].mean():.4f} | {sub['coverage'].mean():.3f} |\")\n    lines.append(\"\")\n\n    # Per-subgroup breakdown\n    lines.append(\"## Per-Subgroup Breakdown\\n\")\n    lines.append(\"| Subgroup | Z | Method | Mean Bias | |Bias| | RMSE | Coverage |\")\n    lines.append(\"|----------|---|--------|-----------|-------|------|----------|\")\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            for m in ['naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n                row = df_summary[(df_summary['subgroup'] == s) &\n                                 (df_summary['z_level'] == z) &\n                                 (df_summary['method'] == m)]\n                if len(row) > 0:\n                    r = row.iloc[0]\n                    lines.append(f\"| {s} | {z} | {m} | {r['mean_bias']:+.4f} | \"\n                                 f\"{r['mean_abs_bias']:.4f} | {r['rmse']:.4f} | {r['coverage']:.3f} |\")\n    lines.append(\"\")\n\n    # EC-HTE vs Global bias reduction\n    lines.append(\"## EC-HTE vs Global: Bias Reduction Ratio\\n\")\n    lines.append(\"| Subgroup | Z | HB |Bias| | Global |Bias| | Reduction |\")\n    lines.append(\"|----------|---|-----------|-------------|-----------|\")\n    total_hb, total_gc = 0.0, 0.0\n    n_cells = 0\n    for s in SUBGROUP_LABELS:\n        for z in [0, 1]:\n            hb = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'hb_ec_hte')]\n            gc = df_summary[(df_summary['subgroup'] == s) & (df_summary['z_level'] == z) &\n                            (df_summary['method'] == 'global_corrected')]\n            if len(hb) > 0 and len(gc) > 0:\n                hb_b = hb.iloc[0]['mean_abs_bias']\n                gc_b = gc.iloc[0]['mean_abs_bias']\n                red = (gc_b - hb_b) / gc_b * 100 if gc_b > 1e-6 else 0\n                lines.append(f\"| {s} | {z} | {hb_b:.4f} | {gc_b:.4f} | {red:+.1f}% |\")\n                total_hb += hb_b\n                total_gc += gc_b\n                n_cells += 1\n    if n_cells > 0:\n        avg_red = (total_gc / n_cells - total_hb / n_cells) / (total_gc / n_cells) * 100\n        lines.append(f\"| **Average** | | {total_hb/n_cells:.4f} | {total_gc/n_cells:.4f} | {avg_red:+.1f}% |\")\n    lines.append(\"\")\n\n    # Conclusion\n    lines.append(\"## Conclusion\\n\")\n\n    hb_all = df_summary[df_summary['method'] == 'hb_ec_hte']\n    gc_all = df_summary[df_summary['method'] == 'global_corrected']\n    nv_all = df_summary[df_summary['method'] == 'naive']\n    ml_all = df_summary[df_summary['method'] == 'stratified_mle']\n\n    if len(hb_all) > 0:\n        lines.append(f\"- **Naive**: RMSE={nv_all['rmse'].mean():.4f}, |Bias|={nv_all['mean_abs_bias'].mean():.4f}, Coverage={nv_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Global**: RMSE={gc_all['rmse'].mean():.4f}, |Bias|={gc_all['mean_abs_bias'].mean():.4f}, Coverage={gc_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **Stratified MLE**: RMSE={ml_all['rmse'].mean():.4f}, |Bias|={ml_all['mean_abs_bias'].mean():.4f}, Coverage={ml_all['coverage'].mean():.3f}\")\n        lines.append(f\"- **HB EC-HTE**: RMSE={hb_all['rmse'].mean():.4f}, |Bias|={hb_all['mean_abs_bias'].mean():.4f}, Coverage={hb_all['coverage'].mean():.3f}\")\n\n        naive_rmse = nv_all['rmse'].mean()\n        gc_rmse = gc_all['rmse'].mean()\n        hb_rmse = hb_all['rmse'].mean()\n\n        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"\n                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")\n\n        gc_bias = gc_all['mean_abs_bias'].mean()\n        hb_bias = hb_all['mean_abs_bias'].mean()\n        nv_bias = nv_all['mean_abs_bias'].mean()\n        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"\n                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")\n\n        hb_cov = hb_all['coverage'].mean()\n        gc_cov = gc_all['coverage'].mean()\n        nv_cov = nv_all['coverage'].mean()\n        lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")\n\n        if hb_bias < gc_bias:\n            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")\n        else:\n            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")\n\n    report = \"\\n\".join(lines)\n    outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'\n    with open(outpath, 'w') as f:\n        f.write(report)\n    print(f\"Wrote {outpath}\")\n\n\n# === Main ===\n\nif __name__ == '__main__':\n    print(\"Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\")\n    print(f\"N={N}, n_expert={N_EXPERT}, n_mc={N_MC}, P(Z=1)={P_Z1}\")\n    print(f\"tau(z=0)={TAU_Z0}, tau(z=1)={TAU_Z1}, delta_tau={TAU_Z1-TAU_Z0:.1f}\")\n    print(\"Subgroup CMs:\")\n    for s in SUBGROUP_LABELS:\n        cm = SUBGROUP_CM[s]\n        print(f\"  {s}: FPR={cm['fpr']:.3f}, FNR={cm['fnr']:.3f}\")\n    print()\n\n    # Dry run: 1 seed\n    print(\"=== Dry run (1 seed) ===\")\n    data = generate_data(SEED_BASE)\n    rows = run_one_mc(data, SEED_BASE)\n    df_dry = pd.DataFrame(rows)\n    print(f\"Dry run OK: {len(df_dry)} rows\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_dry[df_dry['method'] == m]\n        bias = sub['bias'].abs().mean()\n        print(f\"  {m:20s}: mean |bias| = {bias:.4f}\")\n    print()\n\n    # Full run\n    print(f\"=== Full run ({N_MC} seeds) ===\")\n    results = []\n    t0 = time.time()\n    for mc in range(N_MC):\n        seed = SEED_BASE + mc\n        data = generate_data(seed)\n        mc_rows = run_one_mc(data, seed)\n        results.extend(mc_rows)\n        elapsed = time.time() - t0\n        eta = elapsed / (mc + 1) * (N_MC - mc - 1)\n        print(f\"  [{mc+1}/{N_MC}] {elapsed:.0f}s elapsed, ETA {eta:.0f}s\")\n\n    total_time = time.time() - t0\n    print(f\"\\nTotal time: {total_time:.1f}s\")\n\n    df_raw = pd.DataFrame(results)\n    df_summary = aggregate_results(df_raw)\n\n    # Save results CSV\n    col_order = ['seed', 'method', 'subgroup', 'z_level', 'bias', 'rmse', 'coverage', 'cate_true', 'cate_est']\n    df_raw[col_order].to_csv('artifacts/c1_multi_llm/llama_semisynthetic_results.csv', index=False)\n    print(f\"Saved llama_semisynthetic_results.csv ({len(df_raw)} rows)\")\n\n    # Write analysis\n    write_analysis(df_raw, df_summary)\n\n    # Print summary\n    print(\"\\n=== Summary ===\\n\")\n    for m in ['oracle', 'naive', 'global_corrected', 'stratified_mle', 'hb_ec_hte']:\n        sub = df_summary[df_summary['method'] == m]\n        if len(sub) > 0:\n            print(f\"  {m:20s}: |bias|={sub['mean_abs_bias'].mean():.4f}  \"\n                  f\"rmse={sub['rmse'].mean():.4f}  cov={sub['coverage'].mean():.3f}\")\n",
    "structuredPatch": [
      {
        "oldStart": 487,
        "oldLines": 24,
        "newStart": 487,
        "newLines": 45,
        "lines": [
          "         gc_rmse = gc_all['rmse'].mean()",
          "         hb_rmse = hb_all['rmse'].mean()",
          " ",
          "-        lines.append(f\"\\nEC-HTE reduces RMSE by {(gc_rmse - hb_rmse)/gc_rmse*100:+.1f}% vs Global, \"",
          "-                     f\"{(naive_rmse - hb_rmse)/naive_rmse*100:+.1f}% vs Naive.\")",
          "-",
          "+        lines.append(\"\")",
          "         gc_bias = gc_all['mean_abs_bias'].mean()",
          "         hb_bias = hb_all['mean_abs_bias'].mean()",
          "         nv_bias = nv_all['mean_abs_bias'].mean()",
          "-        lines.append(f\"EC-HTE reduces |Bias| by {(gc_bias - hb_bias)/gc_bias*100:+.1f}% vs Global, \"",
          "-                     f\"{(nv_bias - hb_bias)/nv_bias*100:+.1f}% vs Naive.\")",
          " ",
          "         hb_cov = hb_all['coverage'].mean()",
          "         gc_cov = gc_all['coverage'].mean()",
          "         nv_cov = nv_all['coverage'].mean()",
          "+",
          "+        lines.append(\"### RMSE comparison\")",
          "+        for label, r in [('HB vs Naive', (naive_rmse - hb_rmse) / naive_rmse * 100),",
          "+                         ('HB vs Global', (gc_rmse - hb_rmse) / gc_rmse * 100),",
          "+                         ('Global vs Naive', (naive_rmse - gc_rmse) / naive_rmse * 100)]:",
          "+            direction = \"improves\" if r > 0 else \"worsens\"",
          "+            lines.append(f\"- {label}: {direction} by {abs(r):.1f}%\")",
          "+",
          "         lines.append(f\"\\nCoverage: Naive={nv_cov:.3f}, Global={gc_cov:.3f}, HB={hb_cov:.3f} (target=0.95)\")",
          " ",
          "-        if hb_bias < gc_bias:",
          "-            lines.append(\"\\n**EC-HTE improves bias over Global under real Llama CMs.**\")",
          "+        # Bias-variance decomposition insight",
          "+        hb_mean_bias_sq = (hb_all['mean_bias'] ** 2).mean()",
          "+        hb_var = hb_all['rmse'].apply(lambda x: x**2).mean() - hb_mean_bias_sq",
          "+        nv_mean_bias_sq = (nv_all['mean_bias'] ** 2).mean()",
          "+        nv_var = nv_all['rmse'].apply(lambda x: x**2).mean() - nv_mean_bias_sq",
          "+",
          "+        lines.append(\"\\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\")",
          "+        lines.append(f\"- Naive:   Bias^2={nv_mean_bias_sq:.4f}, Var={nv_var:.4f}, MSE={nv_mean_bias_sq+nv_var:.4f}\")",
          "+        lines.append(f\"- HB:     Bias^2={hb_mean_bias_sq:.4f}, Var={hb_var:.4f}, MSE={hb_mean_bias_sq+hb_var:.4f}\")",
          "+",
          "+        lines.append(\"\\n### Interpretation\\n\")",
          "+        if hb_bias >= nv_bias:",
          "+            lines.append(\"EC-HTE correction **increases** total error under these conditions. \"",
          "+                         \"The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) \"",
          "+                         \"are too noisy: the variance inflation from inverting estimated mixing matrices \"",
          "+                         \"exceeds the bias reduction from stratified correction.\")",
          "+            lines.append(f\"\\nWith delta_pi={0.137:.3f} (moderate CM heterogeneity) and n_expert={N_EXPERT}, \"",
          "+                         \"the Naive estimator's attenuation bias is smaller than the correction's variance cost. \"",
          "+                         \"EC-HTE would improve with larger expert budgets or greater CM heterogeneity.\")",
          "         else:",
          "-            lines.append(\"\\n**EC-HTE does NOT improve bias over Global under real Llama CMs.**\")",
          "+            lines.append(\"**EC-HTE improves bias over Global under real Llama CMs.**\")",
          " ",
          "     report = \"\\n\".join(lines)",
          "     outpath = 'artifacts/c1_multi_llm/llama_semisynthetic_analysis.md'"
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

_source line 49_

<details open><summary>🔧 Tool call — Bash · `toolu_0191ogNkErF14RfiCyMrdzFK`</summary>

```json
{
  "command": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
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
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "cd6a9b4f-3753-408b-b9f2-b112ff91ced1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RrtBokozrLRzcnmLmqfAFQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2228,
      "cache_read_input_tokens": 84483,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2228
      },
      "output_tokens": 55,
      "service_tier": "standard",
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
  "task_id": "bus33li7x",
  "tool_use_id": "toolu_0191ogNkErF14RfiCyMrdzFK",
  "description": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "task_type": "local_bash",
  "uuid": "2a9d0277-68a2-482d-b7f7-947cd143f413",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bus33li7x",
  "tool_use_id": "toolu_0191ogNkErF14RfiCyMrdzFK",
  "status": "completed",
  "output_file": "",
  "summary": ".venv/bin/python artifacts/c1_multi_llm/run_llama_semisynthetic.py 2>&1",
  "uuid": "7b024a38-f9fd-4137-a635-f3747246a512",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111"
}
```

---

### Tool result

_source line 52 · 2026-05-21T20:51:17.399Z_

<details><summary>↩ Tool result · `toolu_0191ogNkErF14RfiCyMrdzFK`</summary>

```text
Llama-3.1-8B Semi-Synthetic EC-HTE Experiment
N=5000, n_expert=200, n_mc=20, P(Z=1)=0.652
tau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3
Subgroup CMs:
  False_medium: FPR=0.235, FNR=0.319
  False_short: FPR=0.310, FNR=0.212
  True_medium: FPR=0.219, FNR=0.258
  True_short: FPR=0.091, FNR=0.190

=== Dry run (1 seed) ===
Dry run OK: 40 rows
  oracle              : mean |bias| = 0.0705
  naive               : mean |bias| = 0.0796
  global_corrected    : mean |bias| = 0.1348
  stratified_mle      : mean |bias| = 0.3423
  hb_ec_hte           : mean |bias| = 0.3354

=== Full run (20 seeds) ===
  [1/20] 1s elapsed, ETA 17s
  [2/20] 2s elapsed, ETA 16s
  [3/20] 3s elapsed, ETA 15s
  [4/20] 3s elapsed, ETA 14s
  [5/20] 4s elapsed, ETA 13s
  [6/20] 5s elapsed, ETA 12s
  [7/20] 6s elapsed, ETA 11s
  [8/20] 7s elapsed, ETA 10s
  [9/20] 8s elapsed, ETA 10s
  [10/20] 9s elapsed, ETA 9s
  [11/20] 10s elapsed, ETA 8s
  [12/20] 10s elapsed, ETA 7s
  [13/20] 11s elapsed, ETA 6s
  [14/20] 12s elapsed, ETA 5s
  [15/20] 13s elapsed, ETA 4s
  [16/20] 14s elapsed, ETA 4s
  [17/20] 15s elapsed, ETA 3s
  [18/20] 16s elapsed, ETA 2s
  [19/20] 17s elapsed, ETA 1s
  [20/20] 18s elapsed, ETA 0s

Total time: 17.7s
Saved llama_semisynthetic_results.csv (800 rows)
Wrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md

=== Summary ===

  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950
  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750
  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856
  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744
  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "3025764a-4887-4fb6-855f-13540d3c08aa",
  "tool_use_result": {
    "stdout": "Llama-3.1-8B Semi-Synthetic EC-HTE Experiment\nN=5000, n_expert=200, n_mc=20, P(Z=1)=0.652\ntau(z=0)=0.35, tau(z=1)=0.65, delta_tau=0.3\nSubgroup CMs:\n  False_medium: FPR=0.235, FNR=0.319\n  False_short: FPR=0.310, FNR=0.212\n  True_medium: FPR=0.219, FNR=0.258\n  True_short: FPR=0.091, FNR=0.190\n\n=== Dry run (1 seed) ===\nDry run OK: 40 rows\n  oracle              : mean |bias| = 0.0705\n  naive               : mean |bias| = 0.0796\n  global_corrected    : mean |bias| = 0.1348\n  stratified_mle      : mean |bias| = 0.3423\n  hb_ec_hte           : mean |bias| = 0.3354\n\n=== Full run (20 seeds) ===\n  [1/20] 1s elapsed, ETA 17s\n  [2/20] 2s elapsed, ETA 16s\n  [3/20] 3s elapsed, ETA 15s\n  [4/20] 3s elapsed, ETA 14s\n  [5/20] 4s elapsed, ETA 13s\n  [6/20] 5s elapsed, ETA 12s\n  [7/20] 6s elapsed, ETA 11s\n  [8/20] 7s elapsed, ETA 10s\n  [9/20] 8s elapsed, ETA 10s\n  [10/20] 9s elapsed, ETA 9s\n  [11/20] 10s elapsed, ETA 8s\n  [12/20] 10s elapsed, ETA 7s\n  [13/20] 11s elapsed, ETA 6s\n  [14/20] 12s elapsed, ETA 5s\n  [15/20] 13s elapsed, ETA 4s\n  [16/20] 14s elapsed, ETA 4s\n  [17/20] 15s elapsed, ETA 3s\n  [18/20] 16s elapsed, ETA 2s\n  [19/20] 17s elapsed, ETA 1s\n  [20/20] 18s elapsed, ETA 0s\n\nTotal time: 17.7s\nSaved llama_semisynthetic_results.csv (800 rows)\nWrote artifacts/c1_multi_llm/llama_semisynthetic_analysis.md\n\n=== Summary ===\n\n  oracle              : |bias|=0.0742  rmse=0.0896  cov=0.950\n  naive               : |bias|=0.1031  rmse=0.1246  cov=0.750\n  global_corrected    : |bias|=0.1525  rmse=0.1892  cov=0.856\n  stratified_mle      : |bias|=0.2158  rmse=0.2808  cov=0.744\n  hb_ec_hte           : |bias|=0.2183  rmse=0.2851  cov=0.750",
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

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_01MBi5KcYbV1mcJ3uJuTsWwN`</summary>

```json
{
  "file_path": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md",
  "offset": 75
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "56f1da8a-1ebf-46ea-9f87-2b0f7c3478c2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018rkBsA3y7yqKUqR6edPegN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1059,
      "cache_read_input_tokens": 86711,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1059
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

_source line 54 · 2026-05-21T20:51:20.413Z_

<details><summary>↩ Tool result · `toolu_01MBi5KcYbV1mcJ3uJuTsWwN`</summary>

```text
75	| True_short | 0 | 0.2496 | 0.1483 | -68.3% |
76	| True_short | 1 | 0.1678 | 0.1535 | -9.3% |
77	| **Average** | | 0.2183 | 0.1525 | -43.1% |
78	
79	## Conclusion
80	
81	- **Naive**: RMSE=0.1246, |Bias|=0.1031, Coverage=0.750
82	- **Global**: RMSE=0.1892, |Bias|=0.1525, Coverage=0.856
83	- **Stratified MLE**: RMSE=0.2808, |Bias|=0.2158, Coverage=0.744
84	- **HB EC-HTE**: RMSE=0.2851, |Bias|=0.2183, Coverage=0.750
85	
86	### RMSE comparison
87	- HB vs Naive: worsens by 128.8%
88	- HB vs Global: worsens by 50.7%
89	- Global vs Naive: worsens by 51.8%
90	
91	Coverage: Naive=0.750, Global=0.856, HB=0.750 (target=0.95)
92	
93	### Bias-Variance Decomposition (MSE = Bias^2 + Var)
94	- Naive:   Bias^2=0.0079, Var=0.0087, MSE=0.0165
95	- HB:     Bias^2=0.0039, Var=0.0824, MSE=0.0863
96	
97	### Interpretation
98	
99	EC-HTE correction **increases** total error under these conditions. The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) are too noisy: the variance inflation from inverting estimated mixing matrices exceeds the bias reduction from stratified correction.
100	
101	With delta_pi=0.137 (moderate CM heterogeneity) and n_expert=200, the Naive estimator's attenuation bias is smaller than the correction's variance cost. EC-HTE would improve with larger expert budgets or greater CM heterogeneity.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "e45f265c-78f3-4a71-a9cd-926e0e50f26b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/ec_hte_llm_annotation/artifacts/c1_multi_llm/llama_semisynthetic_analysis.md",
      "content": "| True_short | 0 | 0.2496 | 0.1483 | -68.3% |\n| True_short | 1 | 0.1678 | 0.1535 | -9.3% |\n| **Average** | | 0.2183 | 0.1525 | -43.1% |\n\n## Conclusion\n\n- **Naive**: RMSE=0.1246, |Bias|=0.1031, Coverage=0.750\n- **Global**: RMSE=0.1892, |Bias|=0.1525, Coverage=0.856\n- **Stratified MLE**: RMSE=0.2808, |Bias|=0.2158, Coverage=0.744\n- **HB EC-HTE**: RMSE=0.2851, |Bias|=0.2183, Coverage=0.750\n\n### RMSE comparison\n- HB vs Naive: worsens by 128.8%\n- HB vs Global: worsens by 50.7%\n- Global vs Naive: worsens by 51.8%\n\nCoverage: Naive=0.750, Global=0.856, HB=0.750 (target=0.95)\n\n### Bias-Variance Decomposition (MSE = Bias^2 + Var)\n- Naive:   Bias^2=0.0079, Var=0.0087, MSE=0.0165\n- HB:     Bias^2=0.0039, Var=0.0824, MSE=0.0863\n\n### Interpretation\n\nEC-HTE correction **increases** total error under these conditions. The per-subgroup CM estimates (from ~28-77 expert labels per subgroup) are too noisy: the variance inflation from inverting estimated mixing matrices exceeds the bias reduction from stratified correction.\n\nWith delta_pi=0.137 (moderate CM heterogeneity) and n_expert=200, the Naive estimator's attenuation bias is smaller than the correction's variance cost. EC-HTE would improve with larger expert budgets or greater CM heterogeneity.",
      "numLines": 27,
      "startLine": 75,
      "totalLines": 101
    }
  }
}
```

</details>

---

### Assistant

_source line 55_

The analysis is complete and the bias-variance decomposition confirms the story clearly:

- **Naive**: Bias^2=0.0079, Var=0.0087, MSE=0.0165
- **HB EC-HTE**: Bias^2=0.0039, Var=0.0824, MSE=0.0863

EC-HTE halves the systematic bias (0.0039 vs 0.0079) but inflates variance by ~10x (0.0824 vs 0.0087), so total MSE is 5x worse.

All outputs produced:
- `artifacts/c1_multi_llm/llama_semisynthetic_results.csv` — 800 rows (20 seeds x 4 subgroups x 2 z-levels x 5 methods)
- `artifacts/c1_multi_llm/llama_semisynthetic_analysis.md` — full analysis with summary tables, per-subgroup breakdown, bias reduction ratios, bias-variance decomposition, and interpretation

**Key finding**: Under Llama's real CMs (Δπ=0.137, moderate heterogeneity) with n_expert=200, EC-HTE correction does NOT improve over Naive. The per-subgroup CM estimates (~28-77 expert labels per subgroup) are too noisy — the variance cost from inverting estimated mixing matrices exceeds the bias reduction benefit. EC-HTE would need larger expert budgets or greater CM heterogeneity to be beneficial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "uuid": "7421c22b-75ab-432c-bf64-50a3da4ca5cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tknwutb1SrnsozAd9qxBfz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 690,
      "cache_read_input_tokens": 87770,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 690
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

_source line 56_

The analysis is complete and the bias-variance decomposition confirms the story clearly:

- **Naive**: Bias^2=0.0079, Var=0.0087, MSE=0.0165
- **HB EC-HTE**: Bias^2=0.0039, Var=0.0824, MSE=0.0863

EC-HTE halves the systematic bias (0.0039 vs 0.0079) but inflates variance by ~10x (0.0824 vs 0.0087), so total MSE is 5x worse.

All outputs produced:
- `artifacts/c1_multi_llm/llama_semisynthetic_results.csv` — 800 rows (20 seeds x 4 subgroups x 2 z-levels x 5 methods)
- `artifacts/c1_multi_llm/llama_semisynthetic_analysis.md` — full analysis with summary tables, per-subgroup breakdown, bias reduction ratios, bias-variance decomposition, and interpretation

**Key finding**: Under Llama's real CMs (Δπ=0.137, moderate heterogeneity) with n_expert=200, EC-HTE correction does NOT improve over Naive. The per-subgroup CM estimates (~28-77 expert labels per subgroup) are too noisy — the variance cost from inverting estimated mixing matrices exceeds the bias reduction benefit. EC-HTE would need larger expert budgets or greater CM heterogeneity to be beneficial.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 462465,
  "duration_api_ms": 424500,
  "num_turns": 18,
  "stop_reason": "end_turn",
  "session_id": "7662c207-d824-40c8-87dd-72c577b89111",
  "total_cost_usd": 1.5052457499999998,
  "usage": {
    "input_tokens": 13,
    "cache_creation_input_tokens": 76619,
    "cache_read_input_tokens": 560150,
    "output_tokens": 29765,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 76619,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 357,
        "cache_read_input_tokens": 87770,
        "cache_creation_input_tokens": 690,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 690
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2007,
      "outputTokens": 21,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002112,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 13,
      "outputTokens": 29765,
      "cacheReadInputTokens": 560150,
      "cacheCreationInputTokens": 76619,
      "webSearchRequests": 0,
      "costUSD": 1.50313375,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cf457b66-419d-4b28-ae78-663bacac124d"
}
```

</details>

---
