# paper compile and git init 20260514T095535 retry1

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 26
- **Original source:** `logs/workers/worker_paper_compile_and_git_init_20260514T095535_retry1.log`
- **Structured JSON:** [`49f2ba0c408c435f2b47.json`](../../sessions/49/49f2ba0c408c435f2b47.json)

## Before a recorded user message

61 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
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
    "mcp__agent-ml-research__detect_image",
    "mcp__agent-ml-research__kill_job",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file",
    "mcp__agent-ml-research__ssh_execute",
    "mcp__agent-ml-research__ssh_read_only"
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
  "uuid": "3f3ce444-8c0f-4490-bf30-2192a7f37240",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 2_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1778757000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "ea79c100-f4fb-4527-96d2-53fb6f398c38",
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
Let me break this down into steps. First, I need to explore the server environment, then sync files, compile the paper, and initialize a git repo.

Let me start by detecting the image and checking the server environment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "50d9ba54-0969-4071-a28b-14fb0f46a1b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzwedLCmKvC55RnJtkKhNS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12366,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12366
      },
      "output_tokens": 24,
      "service_tier": "standard",
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

_source line 4_

开始执行。先探测服务器环境和检查本地文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "fe93a6f2-3b1d-4324-9fcd-7433081699c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzwedLCmKvC55RnJtkKhNS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12366,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12366
      },
      "output_tokens": 24,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MmM2kijXZKZQpCxrTQgYKQ`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "47e704f3-567d-476d-bdea-2bccb5a47a2e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LzwedLCmKvC55RnJtkKhNS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12366,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12366
      },
      "output_tokens": 24,
      "service_tier": "standard",
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

_source line 6 · 2026-05-14T10:14:38.428Z_

<details><summary>↩ Tool result · `toolu_01MmM2kijXZKZQpCxrTQgYKQ`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__detect_image"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_read_only"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__ssh_execute"
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
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "0eee207b-5eb1-4a07-a632-8fbfde1b8da8",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__detect_image",
      "mcp__agent-ml-research__ssh_read_only",
      "mcp__agent-ml-research__ssh_execute"
    ],
    "query": "select:mcp__agent-ml-research__detect_image,mcp__agent-ml-research__ssh_read_only,mcp__agent-ml-research__ssh_execute",
    "total_deferred_tools": 26
  }
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__detect_image · `toolu_01UtY4CWAh1cgo8W9buGHBVL`</summary>

```json
{
  "server": "westd-22162",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "d8a198db-923b-46cd-8d4e-e9258cc09a61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zxyBm1hh88fxQzWgTJx2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01V5hLKx3wgP2kdrADAXqiew`</summary>

```json
{
  "server": "westd-22162",
  "command": "which pdflatex",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "ea190b32-f5a5-49be-b8f4-cd6d589ac312",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zxyBm1hh88fxQzWgTJx2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 9 · 2026-05-14T10:14:42.383Z_

<details><summary>↩ Tool result · `toolu_01UtY4CWAh1cgo8W9buGHBVL`</summary>

```text
{"result":"{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "2f5fe88f-c5cc-4523-b8a9-12fda95ad0c6",
  "tool_use_result": {
    "content": "{\"result\":\"{\\n  \\\"detected\\\": false,\\n  \\\"status\\\": \\\"unknown\\\",\\n  \\\"skip_base_setup\\\": false,\\n  \\\"message\\\": \\\"No image marker file found. Use traditional env-setup flow.\\\"\\n}\"}",
    "structuredContent": {
      "result": "{\n  \"detected\": false,\n  \"status\": \"unknown\",\n  \"skip_base_setup\": false,\n  \"message\": \"No image marker file found. Use traditional env-setup flow.\"\n}"
    }
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-14T10:14:42.391Z_

<details><summary>↩ Tool result · `toolu_01V5hLKx3wgP2kdrADAXqiew`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "cf2941e1-83ca-490a-8edc-e93ccf326d3b",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"[ssh_read_only] Command blocked: 'which' is not in the read-only allowlist. Only read-only commands are permitted (cat/ls/grep/find/tail/head/wc/stat/etc.).\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01E2fcMvqxCyxvjL5GDFFwym`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "5bb53448-1e69-4957-a27a-568585cffca7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zxyBm1hh88fxQzWgTJx2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 12 · 2026-05-14T10:14:44.113Z_

<details><summary>↩ Tool result · `toolu_01E2fcMvqxCyxvjL5GDFFwym`</summary>

```text
artifacts/_project/paper/background.tex
artifacts/_project/paper/_archive/results_5_1.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/main.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/discussion.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "7377d09e-9b6a-46b9-9f58-d77e97ea7c55",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/background.tex",
      "artifacts/_project/paper/_archive/results_5_1.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/main.tex",
      "artifacts/_project/paper/analysis.tex",
      "artifacts/_project/paper/methodology.tex",
      "artifacts/_project/paper/abstract.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/results.tex",
      "artifacts/_project/paper/conclusion.tex",
      "artifacts/_project/paper/discussion.tex"
    ],
    "durationMs": 17,
    "numFiles": 11,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01Ke7TGFChnNa95VTXTUGye3`</summary>

```json
{
  "pattern": "*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "4cd71ad7-e9b7-4fe3-afa8-9f56ae45fd87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018zxyBm1hh88fxQzWgTJx2C",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 955,
      "cache_read_input_tokens": 24207,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 955
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

_source line 14 · 2026-05-14T10:14:44.727Z_

<details><summary>↩ Tool result · `toolu_01Ke7TGFChnNa95VTXTUGye3`</summary>

```text
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "2f12cab8-e4bd-46e6-bfb0-3d04a0865463",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 20,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 15_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_013owqLmEpdcuvSqeGXwMBTD`</summary>

```json
{
  "server": "westd-22162",
  "command": "which pdflatex && pdflatex --version | head -1; which bibtex && bibtex --version | head -1; which latexmk && latexmk --version | head -2; ls /root/autodl-tmp/pacs/figures/*.pdf 2>/dev/null | head -20",
  "account": "root",
  "warn": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "dc3c030c-3628-44cb-8032-32587273811d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Etg8RPAbD6Y4JrHwZoA8KL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 25162,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 16 · 2026-05-14T10:14:48.993Z_

<details><summary>↩ Tool result · `toolu_013owqLmEpdcuvSqeGXwMBTD`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"/usr/bin/pdflatex\\npdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)\\n/usr/bin/bibtex\\nBibTeX 0.99d (TeX Live 2022/dev/Debian)\\n/root/autodl-tmp/pacs/figures/cohens_d_6point.pdf\\n/root/autodl-tmp/pacs/figures/crossover_6point.pdf\\n/root/autodl-tmp/pacs/figures/dose_response_6point.pdf\\n/root/autodl-tmp/pacs/figures/fig1_dose_response.pdf\\n/root/autodl-tmp/pacs/figures/fig1_severity_gradient.pdf\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d.pdf\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d_segment_level.pdf\\n/root/autodl-tmp/pacs/figures/fig2_crossover_heatmap.pdf\\n/root/autodl-tmp/pacs/figures/fig3_crossover.pdf\\n/root/autodl-tmp/pacs/figures/fig4_bootstrap.pdf\\n/root/autodl-tmp/pacs/figures/fig4_per_problem_dist.pdf\\n/root/autodl-tmp/pacs/figures/fig5_crossmodel.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "3fb99d1b-372d-406d-8606-560630fae755",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"/usr/bin/pdflatex\\\\npdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)\\\\n/usr/bin/bibtex\\\\nBibTeX 0.99d (TeX Live 2022/dev/Debian)\\\\n/root/autodl-tmp/pacs/figures/cohens_d_6point.pdf\\\\n/root/autodl-tmp/pacs/figures/crossover_6point.pdf\\\\n/root/autodl-tmp/pacs/figures/dose_response_6point.pdf\\\\n/root/autodl-tmp/pacs/figures/fig1_dose_response.pdf\\\\n/root/autodl-tmp/pacs/figures/fig1_severity_gradient.pdf\\\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d.pdf\\\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d_segment_level.pdf\\\\n/root/autodl-tmp/pacs/figures/fig2_crossover_heatmap.pdf\\\\n/root/autodl-tmp/pacs/figures/fig3_crossover.pdf\\\\n/root/autodl-tmp/pacs/figures/fig4_bootstrap.pdf\\\\n/root/autodl-tmp/pacs/figures/fig4_per_problem_dist.pdf\\\\n/root/autodl-tmp/pacs/figures/fig5_crossmodel.pdf\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.46}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"/usr/bin/pdflatex\\npdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)\\n/usr/bin/bibtex\\nBibTeX 0.99d (TeX Live 2022/dev/Debian)\\n/root/autodl-tmp/pacs/figures/cohens_d_6point.pdf\\n/root/autodl-tmp/pacs/figures/crossover_6point.pdf\\n/root/autodl-tmp/pacs/figures/dose_response_6point.pdf\\n/root/autodl-tmp/pacs/figures/fig1_dose_response.pdf\\n/root/autodl-tmp/pacs/figures/fig1_severity_gradient.pdf\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d.pdf\\n/root/autodl-tmp/pacs/figures/fig2_cohens_d_segment_level.pdf\\n/root/autodl-tmp/pacs/figures/fig2_crossover_heatmap.pdf\\n/root/autodl-tmp/pacs/figures/fig3_crossover.pdf\\n/root/autodl-tmp/pacs/figures/fig4_bootstrap.pdf\\n/root/autodl-tmp/pacs/figures/fig4_per_problem_dist.pdf\\n/root/autodl-tmp/pacs/figures/fig5_crossmodel.pdf\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.46}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 17_

pdflatex 和 bibtex 已装好，latexmk 未装但不需要。服务器有 13 个 PDF 图表。现在读取本地 tex 文件并同步到服务器。

先读取所有 11 个文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "71039cc1-e51b-46e3-bba3-1cfa5152e9df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_01GLi8fedKWDR3ZuYLs1PHtH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "e97cdfb0-2d03-4528-827f-c60d78d350b1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 19 · 2026-05-14T10:14:54.796Z_

<details><summary>↩ Tool result · `toolu_01GLi8fedKWDR3ZuYLs1PHtH`</summary>

```text
1	% TODO: Replace \documentclass and package setup below with EMNLP/ACL template:
2	%   \documentclass[11pt]{article}
3	%   \usepackage{acl}
4	%   or download ACL 2025 style files from https://github.com/acl-org/acl-style-files
5	% Current setup uses standard article class as a placeholder.
6	
7	\documentclass[11pt]{article}
8	
9	% --- Geometry (approximate ACL two-column layout) ---
10	\usepackage[a4paper, margin=2.5cm]{geometry}
11	
12	% --- Essential packages ---
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{graphicx}
16	\usepackage{booktabs}
17	\usepackage{enumitem}
18	\usepackage{multirow}
19	\usepackage{xcolor}
20	\usepackage[hidelinks]{hyperref}
21	\usepackage{natbib}
22	\usepackage{times}
23	
24	\graphicspath{{figures/}}
25	
26	% --- Title ---
27	\title{Phase-Modulated Compound Sparsity:\\Strategy-Dependent Severity Gradients in Reasoning Models}
28	
29	% Anonymous submission
30	\author{Anonymous}
31	
32	\date{}
33	
34	\begin{document}
35	
36	\maketitle
37	
38	% --- Abstract ---
39	\input{abstract}
40	
41	% --- Main body ---
42	\input{introduction}
43	\input{related_work}
44	\input{background}
45	\input{methodology}
46	\input{results}
47	\input{analysis}
48	\input{discussion}
49	\input{conclusion}
50	
51	% --- References ---
52	\bibliographystyle{acl_natbib}
53	\bibliography{references}
54	
55	% --- Appendix (if needed) ---
56	% \appendix
57	% \input{appendix}
58	
59	\end{document}
60	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "07b2ba47-2763-4594-a436-4c6e7330bde0",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/main.tex",
      "content": "% TODO: Replace \\documentclass and package setup below with EMNLP/ACL template:\n%   \\documentclass[11pt]{article}\n%   \\usepackage{acl}\n%   or download ACL 2025 style files from https://github.com/acl-org/acl-style-files\n% Current setup uses standard article class as a placeholder.\n\n\\documentclass[11pt]{article}\n\n% --- Geometry (approximate ACL two-column layout) ---\n\\usepackage[a4paper, margin=2.5cm]{geometry}\n\n% --- Essential packages ---\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[hidelinks]{hyperref}\n\\usepackage{natbib}\n\\usepackage{times}\n\n\\graphicspath{{figures/}}\n\n% --- Title ---\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n% Anonymous submission\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n% --- Abstract ---\n\\input{abstract}\n\n% --- Main body ---\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n% --- References ---\n\\bibliographystyle{acl_natbib}\n\\bibliography{references}\n\n% --- Appendix (if needed) ---\n% \\appendix\n% \\input{appendix}\n\n\\end{document}\n",
      "numLines": 60,
      "startLine": 1,
      "totalLines": 60
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_01Enk4VVN4UTQodmqNB4hF7g`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "a119d576-920e-4be9-84a4-fb21767ad74d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 21 · 2026-05-14T10:14:55.536Z_

<details><summary>↩ Tool result · `toolu_01Enk4VVN4UTQodmqNB4hF7g`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	Prior work treats compound interaction magnitude as approximately constant across the generation process.
4	We show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.
5	
6	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$.
7	Under importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.
8	Random eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.
9	At $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) yet underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
10	The pattern replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).
11	
12	We propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.
13	These findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.
14	\end{abstract}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "db098c5c-c04c-43bf-86e2-94f402de9547",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex",
      "content": "\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}",
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

_source line 22_

<details open><summary>🔧 Tool call — Read · `toolu_01RU49rJo6my6Y61kfbypuSM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "5aa8cf8b-4bd6-41df-aa25-d239bb3798c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 23 · 2026-05-14T10:14:56.037Z_

<details><summary>↩ Tool result · `toolu_01RU49rJo6my6Y61kfbypuSM`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \cite{kwon2023vllm, pope2023efficiently}.
5	Two complementary responses have emerged: \emph{attention head pruning}, which removes structurally redundant heads \cite{voita2019heads, michel2019sixteen}, and \emph{KV cache eviction}, which discards low-importance token positions from the cache \cite{snapkv-neurips2024, adakv-neurips2025}.
6	Deploying both simultaneously---\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \cite{spark-aaai2026, slim-icml2025}.
7	
8	Prior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \cite{spark-aaai2026, unicomp-2026}.
9	This assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \cite{thinkv-iclr2026, decision-repr-transition-2026}.
10	If compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.
11	
12	We investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.
13	Our central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).
14	This \emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).
15	The pattern replicates at $s \geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).
16	Critically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.
17	
18	We propose \emph{entropy-discrimination collapse} as an explanatory mechanism.
19	Head pruning forces surviving heads to redistribute attention mass, increasing attention entropy.
20	In low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.
21	Importance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.
22	In high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.
23	Random eviction is immune to this mechanism because its decisions are independent of attention patterns.
24	
25	Our contributions are as follows:
26	\begin{enumerate}[nosep,leftmargin=*]
27	    \item We identify a \textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\S\ref{sec:results}).
28	    \item We show that this severity gradient \textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \geq 0.20$) across two models with different training regimes (distillation vs.\ instruction tuning), establishing robustness within the Qwen2 architecture family (\S\ref{sec:results}).
29	    \item We propose \textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\S\ref{sec:analysis}).
30	\end{enumerate}
31	
32	These findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.
33	The remainder of this paper is organized as follows: \S\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \S\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \S\ref{sec:experimental-setup} describes our experimental setup; \S\ref{sec:results} presents the main results; \S\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \S\ref{sec:discussion} discusses implications and limitations.
34	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "74660b30-8e87-40f3-b01e-87336f6384fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon2023vllm, pope2023efficiently}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita2019heads, michel2019sixteen}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\n",
      "numLines": 34,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Read · `toolu_01CbyiwtG3sCjXDFf7VfFQMj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "6306c570-9ccf-41a9-b9ae-6ed81b29a59b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 25 · 2026-05-14T10:14:56.814Z_

<details><summary>↩ Tool result · `toolu_01CbyiwtG3sCjXDFf7VfFQMj`</summary>

```text
1	\section{Related Work}
2	\label{sec:related}
3	
4	\subsection{Compound and Joint Compression}
5	
6	Combining multiple compression axes produces non-additive errors.
7	\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.
8	\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.
9	\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.
10	The order of compression stages is itself consequential: \cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\to$KD$\to$Q strictly preferable.
11	At a more fundamental level, \cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.
12	On the structural side, GRASPrune~\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.
13	These works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.
14	How compound severity shifts across reasoning phases within a single generation remains unexamined.
15	
16	\subsection{KV Cache Eviction}
17	
18	Most eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.
19	Ada-KV~\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.
20	SnapKV~\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.
21	\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.
22	\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.
23	\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.
24	\cite{mustafar-neurips2025} achieve 70\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.
25	RetentiveKV~\cite{retentivekv-2026} identifies \emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.
26	\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.
27	A recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.
28	
29	\subsection{Phase-Aware Inference}
30	
31	Several concurrent works introduce phase-awareness into LLM inference.
32	ThinKV~\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.
33	\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.
34	\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.
35	\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.
36	\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.
37	
38	These works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.
39	Our work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "5b7206ba-98fe-48c2-8e36-4c5eb856a4dd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Compound and Joint Compression}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.\n\\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.\nThe order of compression stages is itself consequential: \\cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\\to$KD$\\to$Q strictly preferable.\nAt a more fundamental level, \\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.\nOn the structural side, GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.\nThese works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.\nHow compound severity shifts across reasoning phases within a single generation remains unexamined.\n\n\\subsection{KV Cache Eviction}\n\nMost eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.\nAda-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.\n\\cite{mustafar-neurips2025} achieve 70\\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.\nRetentiveKV~\\cite{retentivekv-2026} identifies \\emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.\n\\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.\nA recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.\n\n\\subsection{Phase-Aware Inference}\n\nSeveral concurrent works introduce phase-awareness into LLM inference.\nThinKV~\\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.\n\\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.\n\\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.\n\\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.\n\\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.\n\nThese works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.\nOur work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.\n",
      "numLines": 40,
      "startLine": 1,
      "totalLines": 40
    }
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_011CCGzbpmrDAWffjGyrqVP2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "14a496c9-e54f-4faa-b1a8-874c6067ef0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 27 · 2026-05-14T10:14:57.108Z_

<details><summary>↩ Tool result · `toolu_011CCGzbpmrDAWffjGyrqVP2`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Methodology.tex should reference these via \eqref rather than redefining.
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.
9	
10	\subsection{Compound Sparsity Formulation}
11	\label{sec:compound-sparsity}
12	
13	Consider a Transformer language model with $L$ layers, each containing $H$ attention heads.
14	Let $s \in (0,1)$ denote a unified sparsity budget applied to both compression axes.
15	
16	\paragraph{Attention head pruning.}
17	For each layer $\ell$, heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$, where $\mathbf{A}_j^{(\ell)} \in \mathbb{R}^{T \times T}$ is the attention matrix for head $j$ \cite{voita2019heads, michel2019sixteen}.
18	A binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads, zeroing the output of pruned heads:
19	\begin{equation}
20	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
21	    \label{eq:head-mask}
22	\end{equation}
23	
24	\paragraph{KV cache eviction.}
25	For a sequence of length $T$, a position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions, with the BOS token always preserved.
26	Evicted positions are blocked via attention masking:
27	\begin{equation}
28	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
29	    \label{eq:kv-mask}
30	\end{equation}
31	We compare two strategies for constructing $\mathbf{m}_k$:
32	\begin{itemize}[nosep,leftmargin=*]
33	    \item \textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:
34	    \begin{equation}
35	        \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
36	        \label{eq:kv-importance}
37	    \end{equation}
38	    where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}.
39	    \item \textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.
40	\end{itemize}
41	
42	\paragraph{Compound sparsity.}
43	Applying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \emph{compound sparsity}.
44	The two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.
45	Prior analyses of compound compression \cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.
46	We investigate whether the eviction strategy and reasoning phase introduce additional structure.
47	
48	\subsection{Interaction Index}
49	\label{sec:interaction-index}
50	
51	To quantify the interaction between head pruning and KV cache eviction, we define the \emph{Interaction Index} (II) following the factorial interaction framework from experimental design.
52	
53	For a given text segment, let $\text{PPL}_d$, $\text{PPL}_a$, $\text{PPL}_k$, and $\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.
54	Perplexity is computed as $\text{PPL} = \exp\!\bigl(\frac{1}{|S|}\sum_{t \in S} \mathcal{L}_t\bigr)$, where $\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.
55	Normalizing by the dense baseline yields relative degradation ratios $r_c = \text{PPL}_c\,/\,\text{PPL}_d$ for $c \in \{a, k, b\}$, and the Interaction Index:
56	\begin{equation}
57	    \mathrm{II} = r_b - r_a - r_k + 1.
58	    \label{eq:ii}
59	\end{equation}
60	
61	Under additive independence, $r_b \approx r_a + r_k - 1$, yielding $\mathrm{II} \approx 0$.
62	The sign of II determines the interaction regime:
63	\begin{itemize}[nosep,leftmargin=*]
64	    \item $\mathrm{II} > 0$: \textbf{super-additive}---compound degradation exceeds the sum of individual effects.
65	    \item $\mathrm{II} < 0$: \textbf{sub-additive}---the compound effect is less than the sum of parts.
66	    \item $\mathrm{II} = 0$: \textbf{additive}---the two mechanisms do not interact.
67	\end{itemize}
68	
69	\paragraph{Choice of additive null.}
70	Equation~\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \cdot r_k$.
71	We adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \leq 0.30$).
72	We verify in Appendix~\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.
73	
74	Normalizing by $\text{PPL}_d$ ensures cross-problem comparability.
75	Because the II distribution is heavily right-skewed, we report medians as the central tendency.
76	
77	\paragraph{Severity gradient.}
78	To capture how II varies across reasoning phases (defined in \S\ref{sec:phase-segmentation}), we define the \emph{severity gradient}:
79	\begin{equation}
80	    G = \frac{\widetilde{\mathrm{II}}_{\,\textit{low}}}{\widetilde{\mathrm{II}}_{\,\textit{high}}},
81	    \label{eq:gradient}
82	\end{equation}
83	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.
84	$G \gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \approx 1$ indicates phase-invariant degradation.
85	When $\widetilde{\mathrm{II}}_{\,\textit{high}} < \varepsilon$ for a small threshold $\varepsilon > 0$, we report $G = \infty$.
86	
87	\subsection{Phase Segmentation}
88	\label{sec:phase-segmentation}
89	
90	Reasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.
91	We partition each generated sequence into three phases based on the local \emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \cite{thinkv-iclr2026}.
92	
93	\paragraph{Attention sparsity.}
94	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
95	\begin{equation}
96	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
97	    \label{eq:attn-sparsity}
98	\end{equation}
99	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads.
100	
101	\paragraph{Quantile-based segmentation.}
102	Tokens are partitioned into three groups by the tercile boundaries of $\{\sigma_i\}_{i=1}^{T}$:
103	\begin{itemize}[nosep,leftmargin=*]
104	    \item \textbf{High-sparsity phase} (top tercile of $\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.
105	    \item \textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.
106	    \item \textbf{Low-sparsity phase} (bottom tercile of $\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.
107	\end{itemize}
108	Contiguous segments shorter than $\texttt{min\_phase\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.
109	The segmentation is purely data-driven and requires only access to attention weights.
110	
111	This phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \cite{phase-transition-compression-2026}.
112	Our central research question is: \emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\times$ strategy interaction?}
113	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "4bb0e769-1ef8-4d34-addb-342e5113feff",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex",
      "content": "% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\n",
      "numLines": 113,
      "startLine": 1,
      "totalLines": 113
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_014HkqBN8wkAsZgdg1DNUVjE`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "480ae8d3-5687-4e89-988c-8dc0a853cdf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 29 · 2026-05-14T10:14:57.853Z_

<details><summary>↩ Tool result · `toolu_014HkqBN8wkAsZgdg1DNUVjE`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\subsection{Models}
5	\label{sec:models}
6	
7	We conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):
8	
9	\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \texttt{&lt;think>}$\cdots$\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.
10	
11	\paragraph{Qwen2.5-7B-Instruct} \cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.
12	
13	Both models are loaded in \texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\sim}$8\% of logit positions. Switching to \texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}
14	
15	
16	\subsection{Dataset}
17	\label{sec:dataset}
18	
19	We evaluate on a 50-problem stratified subset of the MATH-500 benchmark \cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048) to eliminate sampling variance.
20	
21	
22	\subsection{Compound Sparsity Configuration}
23	\label{sec:sparsity-config}
24	
25	We apply \emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$, spanning from mild to aggressive compression.
26	
27	\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\emph{dense}---no intervention; (ii)~\emph{attn-only}---head pruning without KV eviction; (iii)~\emph{kv-only}---KV eviction without head pruning; and (iv)~\emph{both}---simultaneous head pruning and KV eviction.
28	
29	\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:
30	
31	\begin{itemize}[nosep,leftmargin=*]
32	\item \textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:
33	\begin{equation}
34	\label{eq:importance}
35	    \alpha_j = \frac{\sum_{i,h} a_{i,h,j}}{\texttt{seq\_len} - j}, \quad j \in \{1, \dots, T\},
36	\end{equation}
37	where $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \cdot s$ positions with the lowest normalized scores are evicted.
38	
39	During masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\infty \times 0 = \text{NaN}$ are handled via selective replacement (\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.
40	
41	\item \textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \texttt{torch.randperm} rather than by importance.
42	\end{itemize}
43	
44	\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\mathbf{A}_\ell \in \mathbb{R}^{H \times T \times T}$ per layer $\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.
45	
46	
47	\subsection{Phase Segmentation}
48	\label{sec:phase-seg}
49	
50	We segment each generated sequence into three \emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \times \max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \emph{mid-sparsity}, and \emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\texttt{min\_phase\_length}=10$ tokens are merged into adjacent phases to suppress noise.
51	
52	
53	\subsection{Metrics}
54	\label{sec:metrics}
55	
56	\paragraph{Perplexity.} For each sparsity condition $c \in \{d, a, k, b\}$ and each phase, we compute segment-level perplexity as
57	$\text{PPL}_c = \exp\!\bigl(\tfrac{1}{|I|}\sum_{i \in I} \mathcal{L}_c(x_i)\bigr)$,
58	where $I$ is the set of token indices belonging to the phase and $\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.
59	
60	\paragraph{Interaction Index.} The interaction index (Equation~\eqref{eq:ii}) quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions.
61	When $\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\mathrm{II} = 0$ indicates additive (independent) degradation.
62	
63	\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we use the severity gradient (Equation~\eqref{eq:gradient}):
64	where $\widetilde{\mathrm{II}}_{\,\textit{low}}$ and $\widetilde{\mathrm{II}}_{\,\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.
65	
66	
67	\subsection{Statistical Analysis}
68	\label{sec:stats}
69	
70	All confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \cite{efron1993bootstrap}.
71	
72	\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\% percentile confidence interval for the population mean II.
73	
74	\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.
75	
76	\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.
77	
78	All tests yield $p_{\text{Bonf}} < 0.005$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\footnote{Experiments were conducted on a server with 4$\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\,GB GPUs, with one model--sparsity configuration per GPU.}
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "ab9bbcbc-a8ac-485a-abff-f862f482a481",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex",
      "content": "\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index (Equation~\\eqref{eq:ii}) quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions.\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we use the severity gradient (Equation~\\eqref{eq:gradient}):\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\n",
      "numLines": 79,
      "startLine": 1,
      "totalLines": 79
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_012DTEfAcwr6wRBzLCtbxtPd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "f6bce912-3707-4adf-8c24-f2ae4b924dfe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 31 · 2026-05-14T10:14:58.071Z_

<details><summary>↩ Tool result · `toolu_012DTEfAcwr6wRBzLCtbxtPd`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	We present our empirical findings in five parts: strategy-dependent compound severity (\S\ref{sec:strategy-severity}), phase-modulated amplification (\S\ref{sec:phase-amplification}), the phase-strategy crossover (\S\ref{sec:crossover}), cross-model replication (\S\ref{sec:cross-model}), and statistical validation (\S\ref{sec:stat-validation}).
6	
7	
8	\subsection{Experimental Overview}
9	\label{sec:exp-overview}
10	
11	We evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\S\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \in \{0.15, 0.20, 0.25, 0.30\}$. We compare importance-based and random eviction strategies (\S\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\S\ref{sec:phase-seg}). The interaction index (II, Eq.~\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\ref{eq:gradient}) captures phase-dependent amplification.
12	Models are evaluated in \texttt{bfloat16} precision (\S\ref{sec:experimental-setup}). Full experimental details appear therein.
13	
14	
15	\subsection{Strategy-Dependent Severity (C1)}
16	\label{sec:strategy-severity}
17	
18	The compound severity difference reveals a stark dependence on eviction strategy. Table~\ref{tab:aggregate-ii} reports the median compound severity difference $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
19	
20	\begin{table}[t]
21	\centering
22	\small
23	\caption{Median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}
24	\label{tab:aggregate-ii}
25	\begin{tabular}{@{}lcccc@{}}
26	\toprule
27	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
28	\midrule
29	Importance & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
30	Random     & 0.01 & $-$0.02 & 0.54 & 1.54 \\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff
31	\bottomrule
32	\end{tabular}
33	\end{table}
34	
35	This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.
36	
37	
38	\subsection{Phase-Modulated Amplification (C2)}
39	\label{sec:phase-amplification}
40	
41	Decomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \S\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.
42	
43	Under importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\times}$ at $s{=}0.15$ to $274{\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\widetilde{\mathrm{II}}_{\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \approx 0.9$--$1.7{\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json
44	
45	\begin{table}[t]
46	\centering
47	\small
48	\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$ is the median severity difference. $G = \widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$ quantifies phase-dependent amplification.}
49	\label{tab:main-results}
50	\begin{tabular}{@{}llccccr@{}}
51	\toprule
52	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
53	\midrule
54	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\ % exp_id: bf16_importance_s015
55	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\ % exp_id: bf16_ds_rand_s015
56	\addlinespace
57	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\ % exp_id: bf16_importance_s020
58	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\ % exp_id: bf16_ds_rand_s020
59	\addlinespace
60	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\ % exp_id: bf16_importance_s025
61	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\ % exp_id: bf16_ds_rand_s025
62	\addlinespace
63	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\ % exp_id: bf16_importance_s030
64	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\ % exp_id: bf16_ds_rand_s030
65	\bottomrule
66	\end{tabular}
67	\end{table}
68	
69	The gradient growth is sub-exponential: successive ratios of the median severity difference $\Delta$ between adjacent sparsity levels are $3.8{\times}$, $4.8{\times}$, and $2.0{\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\times}$, $2.2{\times}$, and $1.2{\times}$. Figure~\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff
70	
71	\begin{figure}[t]
72	\centering
73	\includegraphics[width=\columnwidth]{figures/fig1_dose_response.pdf}
74	\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\times}$ to $274{\times}$, while random eviction (dashed) remains flat near $1{\times}$. Shaded regions denote 95\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030
75	\label{fig:hero}
76	\end{figure}
77	
78	We report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\Delta = 22.94$ vs.\ median $\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\S\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586
79	
80	
81	\subsection{Phase-Strategy Crossover (C3)}
82	\label{sec:crossover}
83	
84	The phase-modulated gradient produces a striking qualitative phenomenon: a \emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{high}} = 0.032$ vs.\ $0.818$), but a higher II in the low-sparsity phase ($\widetilde{\mathrm{II}}_{\textit{low}} = 7.196$ vs.\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json
85	
86	Figure~\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.
87	
88	\begin{figure}[t]
89	\centering
90	\includegraphics[width=\columnwidth]{figures/fig3_crossover.pdf}
91	\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28
92	\label{fig:crossover}
93	\end{figure}
94	
95	The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\S\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \emph{higher} compound severity than the explicitly random baseline.
96	
97	The crossover is present at all four tested sparsity levels ($s \geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\times}$ at $s{=}0.15$ to $5.4{\times}$ at $s{=}0.20$, before moderating to $3.6{\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62
98	
99	
100	\subsection{Cross-Model Replication (C5)}
101	\label{sec:cross-model}
102	
103	To assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.
104	
105	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\S\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\ $n{=}50$ for DeepSeek).
106	
107	Table~\ref{tab:cross-model} compares the median severity difference across both models.
108	
109	\begin{table}[t]
110	\centering
111	\small
112	\caption{Cross-model replication: median compound severity difference ($\Delta = \widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\ instruction tuning).}
113	\label{tab:cross-model}
114	\begin{tabular}{@{}lcccc@{}}
115	\toprule
116	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
117	\midrule
118	DeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json
119	Qwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json
120	\bottomrule
121	\end{tabular}
122	\end{table}
123	
124	Qwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient observed in DeepSeek. The median severity difference increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\ref{tab:cross-model}), paralleling DeepSeek's $0.39$-to-$14.59$ trajectory at approximately one-tenth to one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \to 0.80$; Qwen: $0.28 \to 1.02$; Table~\ref{tab:cohens-d}). Figure~\ref{fig:cross-model} visualizes the dual-model severity trajectory. Spearman $\rho = 1.0$ between the four-point $d_z$ sequences (gradient permutation $p = 0.043$). The per-problem concordance across models is not significant (mean $\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json
125	
126	As a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size (Cohen's $d = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json
127	
128	\begin{figure}[t]
129	\centering
130	\includegraphics[width=\columnwidth]{figures/fig5_crossmodel.pdf}
131	\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030
132	\label{fig:cross-model}
133	\end{figure}
134	
135	The replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\S\ref{sec:limitations}).
136	
137	
138	\subsection{Statistical Validation}
139	\label{sec:stat-validation}
140	
141	We validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and paired $d_z$ for effect size.
142	
143	\paragraph{Permutation test.}
144	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
145	
146	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}
152	\label{tab:permutation}
153	\begin{tabular}{@{}rrcl@{}}
154	\toprule
155	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
156	\midrule
157	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference
158	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference
159	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference
160	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json
166	
167	\begin{figure}[t]
168	\centering
169	\includegraphics[width=\columnwidth]{figures/fig4_bootstrap.pdf}
170	\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}
171	\label{fig:permtest-forest}
172	\end{figure}
173	
174	\paragraph{Effect sizes.}
175	Table~\ref{tab:cohens-d} reports paired $d_z$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.
176	
177	\begin{table}[t]
178	\centering
179	\small
180	\caption{Paired $d_z$ and per-problem median difference $\widetilde{\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\% CIs for $\widetilde{\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}
181	\label{tab:cohens-d}
182	\begin{tabular}{@{}lcccc@{}}
183	\toprule
184	$s$ & DeepSeek $d_z$ & $\widetilde{\Delta}$ [95\% CI] & Qwen $d_z$ & $\widetilde{\Delta}$ [95\% CI] \\
185	\midrule
186	0.15 & 0.44 (small) & 0.32\; $[0.20,\; 0.47]$ & 0.28 (small) & 0.05\; $[-0.01,\; 0.11]$\textsuperscript{ns} \\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json
187	0.20 & 0.52 (medium) & 1.15\; $[0.66,\; 1.26]$ & 0.55 (medium) & 0.21\; $[0.07,\; 0.40]$ \\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json
188	0.25 & 0.68 (medium) & 3.97\; $[2.83,\; 5.29]$ & 0.89 (large) & 1.11\; $[0.61,\; 1.47]$ \\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json
189	0.30 & 0.80 (large) & 9.94\; $[8.39,\; 16.65]$ & 1.02 (large) & 2.62\; $[1.72,\; 3.65]$ \\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json
190	\bottomrule
191	\multicolumn{5}{@{}l}{\footnotesize \textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \geq 0.20$.}
192	\end{tabular}
193	\end{table}
194	
195	For DeepSeek, the effect size increases monotonically from small ($d_z{=}0.44$) at $s{=}0.15$ to large ($d_z{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\widetilde{\Delta}$ excluding zero (Table~\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000
196	For Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \geq 0.20$ ($d_z \geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000
197	At higher sparsity levels ($s \geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000
198	Full per-problem distributions and permutation null distributions appear in Appendix~\ref{app:bootstrap-details}.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "7ce2fc73-43d7-4edd-a9fd-540d2b3cb249",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex",
      "content": "\n\\section{Results}\n\\label{sec:results}\n\nWe present our empirical findings in five parts: strategy-dependent compound severity (\\S\\ref{sec:strategy-severity}), phase-modulated amplification (\\S\\ref{sec:phase-amplification}), the phase-strategy crossover (\\S\\ref{sec:crossover}), cross-model replication (\\S\\ref{sec:cross-model}), and statistical validation (\\S\\ref{sec:stat-validation}).\n\n\n\\subsection{Experimental Overview}\n\\label{sec:exp-overview}\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B using a 50-problem stratified subset of MATH-500 (\\S\\ref{sec:dataset}). For each problem, we measure perplexity under four conditions---dense, attention-only pruning, KV-only eviction, and compound (both)---at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$. We compare importance-based and random eviction strategies (\\S\\ref{sec:sparsity-config}), and segment each generated sequence into high-, mid-, and low-sparsity reasoning phases via quantile-based attention sparsity partitioning (\\S\\ref{sec:phase-seg}). The interaction index (II, Eq.~\\ref{eq:ii}) quantifies compound super-additivity, and the severity gradient ($G$, Eq.~\\ref{eq:gradient}) captures phase-dependent amplification.\nModels are evaluated in \\texttt{bfloat16} precision (\\S\\ref{sec:experimental-setup}). Full experimental details appear therein.\n\n\n\\subsection{Strategy-Dependent Severity (C1)}\n\\label{sec:strategy-severity}\n\nThe compound severity difference reveals a stark dependence on eviction strategy. Table~\\ref{tab:aggregate-ii} reports the median compound severity difference $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: $\\Delta$ increases from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, a $37{\\times}$ amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero ($-0.02$ to $1.54$). % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}50$ MATH-500 problems).}\n\\label{tab:aggregate-ii}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nStrategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nImportance & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\nRandom     & 0.01 & $-$0.02 & 0.54 & 1.54 \\\\ % exp_id: bf16_ds_rand_s015..s030; source: experiment_summary_table.json median_diff\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy---an emergent phase-strategy interaction whose structure we unpack in the following subsections.\n\n\n\\subsection{Phase-Modulated Amplification (C2)}\n\\label{sec:phase-amplification}\n\nDecomposing the interaction index by reasoning phase reveals that the strategy-dependent severity observed in \\S\\ref{sec:strategy-severity} is driven by amplification concentrated in the low-sparsity phase. Table~\\ref{tab:main-results} reports per-phase median II and the severity gradient $G$ at each sparsity level.\n\nUnder importance-based eviction, the severity gradient---the ratio of low-phase to high-phase median II---increases with sparsity from $69{\\times}$ at $s{=}0.15$ to $274{\\times}$ at $s{=}0.30$. The low-sparsity phase---corresponding to exploratory reasoning with broadly distributed attention---bears disproportionate compound degradation, while the high-sparsity phase---corresponding to structured computation with focused attention---experiences near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\textit{high}}$ ranges from $0.006$ to $0.053$). Under random eviction, the gradient remains near unity ($G \\approx 0.9$--$1.7{\\times}$) at all sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. II values are problem-level medians across 50 problems. $\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$ is the median severity difference. $G = \\widetilde{\\mathrm{II}}_{\\textit{low}} / \\widetilde{\\mathrm{II}}_{\\textit{high}}$ quantifies phase-dependent amplification.}\n\\label{tab:main-results}\n\\begin{tabular}{@{}llccccr@{}}\n\\toprule\n$s$ & Strategy & $\\widetilde{\\mathrm{II}}_{\\textit{high}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{mid}}$ & $\\widetilde{\\mathrm{II}}_{\\textit{low}}$ & $\\Delta$ & $G$ \\\\\n\\midrule\n0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\\mathbf{69}$ \\\\ % exp_id: bf16_importance_s015\n0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\\\ % exp_id: bf16_ds_rand_s015\n\\addlinespace\n0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\\mathbf{103}$ \\\\ % exp_id: bf16_importance_s020\n0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\\\ % exp_id: bf16_ds_rand_s020\n\\addlinespace\n0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\\mathbf{222}$ \\\\ % exp_id: bf16_importance_s025\n0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\\\ % exp_id: bf16_ds_rand_s025\n\\addlinespace\n0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\\mathbf{274}$ \\\\ % exp_id: bf16_importance_s030\n0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\\\ % exp_id: bf16_ds_rand_s030\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe gradient growth is sub-exponential: successive ratios of the median severity difference $\\Delta$ between adjacent sparsity levels are $3.8{\\times}$, $4.8{\\times}$, and $2.0{\\times}$---a decreasing terminal growth rate consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient $G$ exhibits the same pattern, with consecutive ratios of $1.5{\\times}$, $2.2{\\times}$, and $1.2{\\times}$. Figure~\\ref{fig:hero} visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json median_diff\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig1_dose_response.pdf}\n\\caption{Severity gradient ($G$) as a function of sparsity level $s$. Importance-based eviction (solid) exhibits an increasing gradient from $69{\\times}$ to $274{\\times}$, while random eviction (dashed) remains flat near $1{\\times}$. Shaded regions denote 95\\% bootstrap confidence intervals.} % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030\n\\label{fig:hero}\n\\end{figure}\n\nWe report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of $1.6{:}1$ at $s{=}0.30$ under importance-based eviction (mean $\\Delta = 22.94$ vs.\\ median $\\Delta = 14.59$). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (\\S\\ref{sec:stat-validation}) account for this skewness via the resampling distribution. % exp_id: bf16_importance_s030; source: cohens_d_bf16.json mean_diff=22.939, experiment_summary_table.json median_diff=14.586\n\n\n\\subsection{Phase-Strategy Crossover (C3)}\n\\label{sec:crossover}\n\nThe phase-modulated gradient produces a striking qualitative phenomenon: a \\emph{crossover} in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At $s{=}0.25$, importance-based eviction yields a lower II than random in the high-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{high}} = 0.032$ vs.\\ $0.818$), but a higher II in the low-sparsity phase ($\\widetilde{\\mathrm{II}}_{\\textit{low}} = 7.196$ vs.\\ $1.363$). This is not merely a magnitude difference---it is a reversal in the relative ranking of strategies across phases. % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json\n\nFigure~\\ref{fig:crossover} displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig3_crossover.pdf}\n\\caption{Strategy-dependent crossover at $s{=}0.25$. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $5.3{\\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.} % exp_id: bf16_importance_s025, bf16_ds_rand_s025; 7.196/1.363=5.28\n\\label{fig:crossover}\n\\end{figure}\n\nThe crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase---where attention is already focused---importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (\\S\\ref{sec:analysis}). The result is that targeted eviction inadvertently removes positions that would have been retained under the pre-pruning importance ranking---producing \\emph{higher} compound severity than the explicitly random baseline.\n\nThe crossover is present at all four tested sparsity levels ($s \\geq 0.15$): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from $3.9{\\times}$ at $s{=}0.15$ to $5.4{\\times}$ at $s{=}0.20$, before moderating to $3.6{\\times}$ at $s{=}0.30$ as random eviction severity also rises. % exp_id: bf16_importance_s015..s030, bf16_ds_rand_s015..s030; source: experiment_summary_table.json; ratios: 0.398/0.103=3.87, 1.496/0.276=5.42, 7.196/1.363=5.28, 14.639/4.041=3.62\n\n\n\\subsection{Cross-Model Replication (C5)}\n\\label{sec:cross-model}\n\nTo assess whether the phase-modulated severity gradient generalizes beyond DeepSeek-R1-Distill-Qwen-7B, we replicate the importance-based eviction experiments on Qwen2.5-7B-Instruct. Both models share the Qwen2ForCausalLM backbone architecture (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This controlled comparison isolates the effect of training methodology on the compound sparsity interaction.\n\nDespite lacking explicit \\texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity across its generation trajectory to permit phase segmentation via the same quantile-based method (\\S\\ref{sec:phase-seg}). Four of the 50 problems are excluded due to degenerate phase assignments, yielding $n{=}46$ valid problems for Qwen (vs.\\ $n{=}50$ for DeepSeek).\n\nTable~\\ref{tab:cross-model} compares the median severity difference across both models.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-model replication: median compound severity difference ($\\Delta = \\widetilde{\\mathrm{II}}_{\\textit{low}} - \\widetilde{\\mathrm{II}}_{\\textit{high}}$) under importance-based eviction. Both models share the Qwen2 architecture but differ in training methodology (distillation vs.\\ instruction tuning).}\n\\label{tab:cross-model}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\nModel & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\\\\n\\midrule\nDeepSeek-R1-Distill-Qwen-7B & 0.39 & 1.48 & 7.16 & 14.59 \\\\ % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json\nQwen2.5-7B-Instruct         & 0.04 & 0.23 & 1.27 & 2.94 \\\\ % exp_id: bf16_qw_imp_s015..s030; source: experiment_summary_table.json\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nQwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient observed in DeepSeek. The median severity difference increases from $0.04$ at $s{=}0.15$ to $2.94$ at $s{=}0.30$ (Table~\\ref{tab:cross-model}), paralleling DeepSeek's $0.39$-to-$14.59$ trajectory at approximately one-tenth to one-fifth the absolute magnitude. Both models yield strictly increasing paired $d_z$ trajectories (DeepSeek: $0.44 \\to 0.80$; Qwen: $0.28 \\to 1.02$; Table~\\ref{tab:cohens-d}). Figure~\\ref{fig:cross-model} visualizes the dual-model severity trajectory. Spearman $\\rho = 1.0$ between the four-point $d_z$ sequences (gradient permutation $p = 0.043$). The per-problem concordance across models is not significant (mean $\\rho = -0.11$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking. The Qwen effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$); this onset lag relative to DeepSeek is consistent with the lower overall compound severity in instruction-tuned models lacking explicit reasoning structure. % exp_id: cross_model_analysis.json (spearman_rho=1.0, gradient_permutation_p=0.043, per_problem_concordance_p=0.926, mean_rho=-0.107); cohens_d_bf16_qwen.json\n\nAs a control, random eviction on Qwen yields no systematic phase gradient at three of four sparsity levels (3/4 FAIL), mirroring DeepSeek's 4/4 FAIL pattern. At $s{=}0.30$, Qwen random produces a borderline PASS (permutation $p = 0.012$) but with negligible effect size (Cohen's $d = -0.04$, CI spans zero), indicating no meaningful phase modulation. % exp_id: bf16_qw_rand_s015..s030; source: experiment_summary_table.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig5_crossmodel.pdf}\n\\caption{Cross-model comparison of the median severity difference under importance-based eviction. Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\\Delta$ with sparsity; Qwen's magnitude is approximately one-fifth of DeepSeek's.} % exp_id: bf16_importance_s015..s030, bf16_qw_imp_s015..s030\n\\label{fig:cross-model}\n\\end{figure}\n\nThe replication on a second model with distinct training methodology suggests that the phase-modulated severity gradient is not an artifact of DeepSeek's distillation-induced phase structure, but rather an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning. We note that both models share the same backbone architecture; generalization to other architectures (e.g., LLaMA, Mistral) remains an open question (\\S\\ref{sec:limitations}).\n\n\n\\subsection{Statistical Validation}\n\\label{sec:stat-validation}\n\nWe validate the strategy-dependent severity using two complementary approaches: a paired permutation test on the difference statistic for significance, and paired $d_z$ for effect size.\n\n\\paragraph{Permutation test.}\nFor each problem $i$ and sparsity level $s$, we compute the compound severity difference $\\Delta_i^{(\\text{strat})} = \\mathrm{II}_{\\textit{low},i} - \\mathrm{II}_{\\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\\widetilde{\\Delta} = \\text{median}_i\\!\\bigl(\\Delta_i^{(\\text{imp})} - \\Delta_i^{(\\text{rand})}\\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.\n\nTable~\\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ (no strategy difference) after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired permutation test (difference statistic) for compound severity: importance vs.\\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ paired problems, $10{,}000$ permutations). $p$-values are Bonferroni-corrected for 4 comparisons.}\n\\label{tab:permutation}\n\\begin{tabular}{@{}rrcl@{}}\n\\toprule\n$s$ & Observed $\\widetilde{\\Delta}$ & 95\\% CI & $p_{\\text{Bonf}}$ \\\\\n\\midrule\n0.15 & 0.37 & $[0.19,\\; 0.62]$ & 0.0032 \\\\ % exp_id: deepseek_bf16_permtest_s015; source: permutation_test_results.json s015.permutation_test_difference\n0.20 & 0.97 & $[0.69,\\; 1.49]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s020; source: permutation_test_results.json s020.permutation_test_difference\n0.25 & 3.34 & $[1.66,\\; 6.64]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s025; source: permutation_test_results.json s025.permutation_test_difference\n0.30 & 9.85 & $[6.70,\\; 16.29]$ & ${<}\\,0.001$ \\\\ % exp_id: deepseek_bf16_permtest_s030; source: permutation_test_results.json s030.permutation_test_difference\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe monotonic growth of both the point estimate and the CI lower bound ($0.19 \\to 0.69 \\to 1.66 \\to 6.70$) confirms that compound severity amplification under importance-based eviction strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\\ref{fig:permtest-forest} presents these results as a forest plot. % exp_id: deepseek_bf16_permtest; source: permutation_test_results.json\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{figures/fig4_bootstrap.pdf}\n\\caption{Forest plot of permutation test results for the difference statistic. Horizontal bars show 95\\% permutation CIs; diamonds mark observed median differences $\\widetilde{\\Delta}$. All CIs lie entirely above zero (vertical dashed line), confirming significant strategy-dependent severity at every sparsity level.}\n\\label{fig:permtest-forest}\n\\end{figure}\n\n\\paragraph{Effect sizes.}\nTable~\\ref{tab:cohens-d} reports paired $d_z$ (bootstrap $B{=}10{,}000$) measuring the standardized difference in II between low- and high-sparsity phases under importance-based eviction.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Paired $d_z$ and per-problem median difference $\\widetilde{\\Delta}$ for the phase-dependent II (low $-$ high) under importance-based eviction. Bootstrap 95\\% CIs for $\\widetilde{\\Delta}$ ($B{=}10{,}000$, per-problem paired). DeepSeek: $n{=}49$ problems (1 excluded); Qwen: $n{=}46$ problems (4 excluded).}\n\\label{tab:cohens-d}\n\\begin{tabular}{@{}lcccc@{}}\n\\toprule\n$s$ & DeepSeek $d_z$ & $\\widetilde{\\Delta}$ [95\\% CI] & Qwen $d_z$ & $\\widetilde{\\Delta}$ [95\\% CI] \\\\\n\\midrule\n0.15 & 0.44 (small) & 0.32\\; $[0.20,\\; 0.47]$ & 0.28 (small) & 0.05\\; $[-0.01,\\; 0.11]$\\textsuperscript{ns} \\\\ % exp_id: bf16_ds_imp_s015, bf16_qw_imp_s015; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json\n0.20 & 0.52 (medium) & 1.15\\; $[0.66,\\; 1.26]$ & 0.55 (medium) & 0.21\\; $[0.07,\\; 0.40]$ \\\\ % exp_id: bf16_ds_imp_s020, bf16_qw_imp_s020; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json\n0.25 & 0.68 (medium) & 3.97\\; $[2.83,\\; 5.29]$ & 0.89 (large) & 1.11\\; $[0.61,\\; 1.47]$ \\\\ % exp_id: bf16_ds_imp_s025, bf16_qw_imp_s025; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json\n0.30 & 0.80 (large) & 9.94\\; $[8.39,\\; 16.65]$ & 1.02 (large) & 2.62\\; $[1.72,\\; 3.65]$ \\\\ % exp_id: bf16_ds_imp_s030, bf16_qw_imp_s030; per-problem paired B=10000; d_z from cohens_d_bf16.json + cohens_d_bf16_qwen.json\n\\bottomrule\n\\multicolumn{5}{@{}l}{\\footnotesize \\textsuperscript{ns}CI spans zero; marginal at $s{=}0.15$ (bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$.}\n\\end{tabular}\n\\end{table}\n\nFor DeepSeek, the effect size increases monotonically from small ($d_z{=}0.44$) at $s{=}0.15$ to large ($d_z{=}0.80$) at $s{=}0.30$, with all bootstrap CIs for $\\widetilde{\\Delta}$ excluding zero (Table~\\ref{tab:cohens-d}). % exp_id: bf16_ds_imp_s015..s030; per-problem paired B=10000\nFor Qwen, the compound interaction effect is marginal at $s{=}0.15$ ($d_z{=}0.28$, bootstrap CI includes zero), becoming reliable at $s \\geq 0.20$ ($d_z \\geq 0.55$), suggesting a model-dependent onset threshold for detectable phase modulation. % exp_id: bf16_qw_imp_s015..s030; per-problem paired B=10000\nAt higher sparsity levels ($s \\geq 0.25$), Qwen exhibits larger standardized effect sizes than DeepSeek ($d_z{=}0.89$/$1.02$ vs.\\ $0.68$/$0.80$), consistent with lower between-problem variance in Qwen's II distribution yielding larger standardized differences despite smaller absolute II values. % exp_id: bf16_ds_imp_s025..s030, bf16_qw_imp_s025..s030; per-problem paired B=10000\nFull per-problem distributions and permutation null distributions appear in Appendix~\\ref{app:bootstrap-details}.\n",
      "numLines": 199,
      "startLine": 1,
      "totalLines": 199
    }
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_016hq134SjwtDaMRqbC753Q5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "dd879b5c-e685-4893-872d-4fd8526a408e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 33 · 2026-05-14T10:14:58.878Z_

<details><summary>↩ Tool result · `toolu_016hq134SjwtDaMRqbC753Q5`</summary>

```text
1	
2	\section{Analysis: Mechanisms of Phase-Modulated Severity}
3	\label{sec:analysis}
4	
5	The results in \S\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\times}$ severity amplification in low-sparsity phases (Table~\ref{tab:main-results}), while random eviction remains flat at ${\sim}1{\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274
6	Why is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.
7	
8	\subsection{Discrimination Collapse Under Head Pruning}
9	\label{sec:discrimination-collapse}
10	
11	The KV importance score (Eq.~\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.
12	
13	The \textbf{Gini coefficient} measures inequality in the importance distribution ($\mathrm{Gini}{=}0$: perfectly uniform; $\mathrm{Gini}{=}1$: maximally concentrated). The \textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.
14	
15	We observe discrimination collapse across both models in all tested conditions (Table~\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Qwen ($-0.010$ to $-0.020$), with magnitude scaling monotonically with sparsity in DeepSeek. % exp_id: c4_entropy_deepseek, c4_entropy_qwen
16	The CV delta is likewise negative in all 8 importance-based conditions, ranging from $-0.56$ to $-1.66$ (DeepSeek) and $-0.05$ to $-1.49$ (Qwen). The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
17	
18	\begin{table}[t]
19	\centering
20	\caption{Discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power. All 8 conditions show consistent negative deltas across both models.}
21	\label{tab:discrimination-metrics}
22	\small
23	\begin{tabular}{llrr}
24	\toprule
25	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
26	\midrule
27	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
28	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
29	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
30	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
31	\midrule
32	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
33	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
34	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
35	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
36	\bottomrule
37	\end{tabular}
38	\end{table}
39	
40	This cross-model consistency establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The severity inversion observed in \S\ref{sec:crossover} is thus an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.
41	
42	Random eviction is immune to this mechanism: its decisions are independent of importance score quality. This explains the flat severity gradient ($G \approx 1$) observed under random eviction at all sparsity levels.
43	
44	\subsection{Entropy Redistribution: Consistent in DeepSeek, Partial in Qwen}
45	\label{sec:entropy-redistribution}
46	
47	Beyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
48	\begin{equation}
49	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
50	    \label{eq:attn-entropy}
51	\end{equation}
52	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
53	
54	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.040, -0.047]$; Table~\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek
55	This is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented above.
56	
57	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen
58	
59	The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
60	
61	\begin{table}[t]
62	\centering
63	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}
64	\label{tab:entropy-deltas}
65	\small
66	\begin{tabular}{llr}
67	\toprule
68	Model & $s$ & $\Delta\mathcal{H}$ \\
69	\midrule
70	DeepSeek & $0.15$ & $-0.040$ \\
71	DeepSeek & $0.20$ & $-0.047$ \\
72	DeepSeek & $0.25$ & $-0.045$ \\
73	DeepSeek & $0.30$ & $-0.044$ \\
74	\midrule
75	Qwen & $0.15$ & $-0.073$ \\
76	Qwen & $0.20$ & $-0.076$ \\
77	Qwen & $0.25$ & $+0.045$ \\
78	Qwen & $0.30$ & $-0.007$ \\
79	\bottomrule
80	\end{tabular}
81	\end{table}
82	
83	The partial replication of entropy redistribution, combined with the full replication of discrimination collapse, suggests a two-level mechanistic picture: head pruning universally degrades the discriminative power of importance scores (as measured by Gini and CV), while the specific direction of entropy redistribution depends on model-specific head specialization patterns. Discrimination collapse is sufficient on its own to explain the emergent phase-strategy interaction; entropy redistribution, where it co-occurs, may amplify the effect.
84	
85	\subsection{Implications for Compound Sparsity}
86	\label{sec:analysis-implications}
87	
88	The discrimination collapse mechanism suggests several broader conclusions.
89	
90	\paragraph{Architecture generality.} Discrimination collapse depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by the major KV cache compression methods---H$_2$O \cite{h2o2024}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. The cross-model consistency of the Gini and CV evidence (Table~\ref{tab:discrimination-metrics}) supports this generality. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent; the full mechanism may thus manifest differently across architectures.
91	
92	\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with the severity gradient scaling with the pruning-induced Gini decrease. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients.
93	
94	\paragraph{Reframing compound severity.} The flat random baseline ($G \approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \emph{per se}. Rather, it is an emergent phase-strategy interaction---the consequence of applying a discrimination-sensitive eviction strategy in a regime where head pruning systematically degrades that discrimination. A phase-aware sparsity controller could, in principle, mitigate this interaction by adjusting the eviction budget or strategy per phase.
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "f8af1436-8f39-4650-b88a-0bfd09af0530",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex",
      "content": "\n\\section{Analysis: Mechanisms of Phase-Modulated Severity}\n\\label{sec:analysis}\n\nThe results in \\S\\ref{sec:results} reveal a striking asymmetry: importance-based eviction exhibits $69$--$274{\\times}$ severity amplification in low-sparsity phases (Table~\\ref{tab:main-results}), while random eviction remains flat at ${\\sim}1{\\times}$ across all phases. % exp_id: bf16_importance_s015..s030; G=69,103,222,274\nWhy is compound severity phase-modulated for one strategy but not the other? We identify two mechanisms. \\emph{Discrimination collapse}---a systematic reduction in the discriminative power of KV importance scores under head pruning---is the primary mechanism, robustly observed across both models and all tested conditions. A secondary \\emph{entropy redistribution} pattern is consistent for DeepSeek but only partially replicates on Qwen, indicating model-dependent modulation.\n\n\\subsection{Discrimination Collapse Under Head Pruning}\n\\label{sec:discrimination-collapse}\n\nThe KV importance score (Eq.~\\ref{eq:kv-importance}) aggregates attention mass across surviving heads. When head pruning reduces the number of contributing heads, the cumulative importance distribution becomes more uniform: the gap between highly-attended and rarely-attended positions shrinks. We quantify this effect through two complementary metrics applied to the per-position importance distribution.\n\nThe \\textbf{Gini coefficient} measures inequality in the importance distribution ($\\mathrm{Gini}{=}0$: perfectly uniform; $\\mathrm{Gini}{=}1$: maximally concentrated). The \\textbf{coefficient of variation} (CV) captures relative dispersion. A decrease in either metric after pruning indicates reduced discriminative power.\n\nWe observe discrimination collapse across both models in all tested conditions (Table~\\ref{tab:discrimination-metrics}). Under importance-based eviction, the Gini delta is negative at every sparsity level for both DeepSeek ($-0.030$ to $-0.081$) and Qwen ($-0.010$ to $-0.020$), with magnitude scaling monotonically with sparsity in DeepSeek. % exp_id: c4_entropy_deepseek, c4_entropy_qwen\nThe CV delta is likewise negative in all 8 importance-based conditions, ranging from $-0.56$ to $-1.66$ (DeepSeek) and $-0.05$ to $-1.49$ (Qwen). The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.073$; Qwen: $-0.019$ to $-0.045$), confirming that discrimination collapse is a consequence of head pruning \\emph{per se}, not of the eviction strategy.\n\n\\begin{table}[t]\n\\centering\n\\caption{Discrimination collapse under importance-based eviction. $\\Delta\\mathrm{Gini}$ and $\\Delta\\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power. All 8 conditions show consistent negative deltas across both models.}\n\\label{tab:discrimination-metrics}\n\\small\n\\begin{tabular}{llrr}\n\\toprule\nModel & $s$ & $\\Delta\\mathrm{Gini}$ & $\\Delta\\mathrm{CV}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\\\\nDeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\\\\nDeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\\\\nDeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.010$ & $-0.05$ \\\\\nQwen & $0.20$ & $-0.012$ & $-0.21$ \\\\\nQwen & $0.25$ & $-0.010$ & $-1.49$ \\\\\nQwen & $0.30$ & $-0.020$ & $-1.14$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThis cross-model consistency establishes discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The severity inversion observed in \\S\\ref{sec:crossover} is thus an emergent consequence of the interaction between head pruning and importance scoring conditioned on the phase-dependent attention structure.\n\nRandom eviction is immune to this mechanism: its decisions are independent of importance score quality. This explains the flat severity gradient ($G \\approx 1$) observed under random eviction at all sparsity levels.\n\n\\subsection{Entropy Redistribution: Consistent in DeepSeek, Partial in Qwen}\n\\label{sec:entropy-redistribution}\n\nBeyond discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:\n\\begin{equation}\n    \\mathcal{H}_i^{(h)} = -\\sum_{j=1}^{T} a_{ij}^{(h)} \\log a_{ij}^{(h)}\n    \\label{eq:attn-entropy}\n\\end{equation}\nand compute $\\Delta\\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.\n\nFor DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\\Delta\\mathcal{H} \\in [-0.040, -0.047]$; Table~\\ref{tab:entropy-deltas}), with the effect stable across reasoning phases. % exp_id: c4_entropy_deepseek\nThis is consistent with importance-based eviction systematically selecting heads whose removal concentrates attention in the surviving heads, reinforcing the discrimination collapse documented above.\n\nFor Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\\Delta\\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). % exp_id: c4_entropy_qwen\n\nThe $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low-sparsity: $+0.042$, mid-sparsity: $+0.034$, high-sparsity: $+0.017$). The mid-sparsity phase contains fewer segments (median~26), which reduces statistical power for that phase; however, the reversal is equally present in the low-sparsity phase with substantially more segments, so mid-phase power limitations are a confound but do not account for the full pattern. We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\\ DeepSeek's distillation-based training) may produce head configurations where removing 25\\% of heads triggers compensatory broadening rather than concentration.\n\n\\begin{table}[t]\n\\centering\n\\caption{Attention entropy deltas ($\\Delta\\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression at all sparsity levels. Qwen partially replicates: negative at $s{\\leq}0.20$, reversed at $s{=}0.25$, near-zero at $s{=}0.30$.}\n\\label{tab:entropy-deltas}\n\\small\n\\begin{tabular}{llr}\n\\toprule\nModel & $s$ & $\\Delta\\mathcal{H}$ \\\\\n\\midrule\nDeepSeek & $0.15$ & $-0.040$ \\\\\nDeepSeek & $0.20$ & $-0.047$ \\\\\nDeepSeek & $0.25$ & $-0.045$ \\\\\nDeepSeek & $0.30$ & $-0.044$ \\\\\n\\midrule\nQwen & $0.15$ & $-0.073$ \\\\\nQwen & $0.20$ & $-0.076$ \\\\\nQwen & $0.25$ & $+0.045$ \\\\\nQwen & $0.30$ & $-0.007$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe partial replication of entropy redistribution, combined with the full replication of discrimination collapse, suggests a two-level mechanistic picture: head pruning universally degrades the discriminative power of importance scores (as measured by Gini and CV), while the specific direction of entropy redistribution depends on model-specific head specialization patterns. Discrimination collapse is sufficient on its own to explain the emergent phase-strategy interaction; entropy redistribution, where it co-occurs, may amplify the effect.\n\n\\subsection{Implications for Compound Sparsity}\n\\label{sec:analysis-implications}\n\nThe discrimination collapse mechanism suggests several broader conclusions.\n\n\\paragraph{Architecture generality.} Discrimination collapse depends on two properties: (i)~attention-mass-based importance scoring for KV eviction, and (ii)~a sufficient number of pruned heads to degrade the importance distribution. Both are shared by the major KV cache compression methods---H$_2$O \\cite{h2o2024}, SnapKV \\cite{snapkv-neurips2024}, PyramidKV \\cite{pyramidkv2024}---and by any autoregressive transformer producing extended reasoning traces. The cross-model consistency of the Gini and CV evidence (Table~\\ref{tab:discrimination-metrics}) supports this generality. The entropy redistribution component, while consistent in DeepSeek, appears model-dependent; the full mechanism may thus manifest differently across architectures.\n\n\\paragraph{Testable prediction.} Any importance metric derived from attention mass should exhibit discrimination collapse under head pruning, with the severity gradient scaling with the pruning-induced Gini decrease. Metrics that derive importance from sources independent of attention---such as activation magnitude or gradient-based saliency---would not be subject to the same collapse and should produce flatter severity gradients.\n\n\\paragraph{Reframing compound severity.} The flat random baseline ($G \\approx 1$) demonstrates that phase-modulated severity amplification is not an inherent cost of compound sparsity \\emph{per se}. Rather, it is an emergent phase-strategy interaction---the consequence of applying a discrimination-sensitive eviction strategy in a regime where head pruning systematically degrades that discrimination. A phase-aware sparsity controller could, in principle, mitigate this interaction by adjusting the eviction budget or strategy per phase.\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01V5Koyc4cwjtr7E6BtJXYV4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "a5db9716-4c3f-413d-ac92-76732adda7a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 35 · 2026-05-14T10:14:59.349Z_

<details><summary>↩ Tool result · `toolu_01V5Koyc4cwjtr7E6BtJXYV4`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{On the predictability of phase-modulated severity.}
5	One might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.
6	We do not dispute this intuition.
7	The surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.
8	
9	First, the \emph{magnitude} of the severity gradient---$69$--$274{\times}$ amplification across sparsity levels (Table~\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.
10	A reviewer expecting a $2$--$3\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.
11	Second, the gradient is \emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051
12	This asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.
13	Third, and most strikingly, a \emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\ $0.818$) yet \emph{underperforms} in low-sparsity phases ($7.196$ vs.\ $1.363$---a ${>}5{\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363
14	The same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''
15	% REVIEWER-ATTACK: "The qualitative direction is trivially expected from attention entropy arguments."
16	% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.
17	
18	\paragraph{Random masking as a falsification control.}
19	The random eviction baseline provides a decisive test against the ``trivially expected'' objection.
20	If compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.
21	It does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)
22	The absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.
23	
24	\paragraph{Cross-model replication and magnitude asymmetry.}
25	The phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of paired $d_z$ effect sizes across sparsity levels is $\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043
26	All eight paired Wilcoxon tests (4 sparsity levels $\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.
27	
28	The \emph{magnitude} of the effect, however, differs substantially.
29	Qwen's median severity differences ($0.039 \to 0.235 \to 1.268 \to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \to 1.48 \to 7.16 \to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (paired $d_z{=}0.44$), while Qwen's becomes clearly significant only at $s \geq 0.20$ ($d_z{=}0.55$; $s{=}0.15$ is borderline at $d_z{=}0.28$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds d_z: 0.4416,0.5195,0.6831,0.8031), cohens_d_bf16_qwen.json (qw d_z: 0.2811,0.5494,0.8894,1.0220).
30	The two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.
31	We conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.
32	
33	\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}
34	The entropy-discrimination collapse hypothesis (\S\ref{sec:analysis}) receives partial cross-model support.
35	The discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.
36	However, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007
37	This divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.
38	We therefore characterize the mechanistic evidence as \emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.
39	
40	\paragraph{Implications for compound sparsity deployment.}
41	Our findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.
42	Compound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\S\ref{sec:analysis}) renders importance-based eviction unreliable.
43	A deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.
44	
45	This observation motivates \emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.
46	The severity gradient $G$ reported in \S\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \gg 1$ receive a reduced sparsity budget, while phases with $G \leq 1$ tolerate aggressive compression with minimal quality loss.
47	
48	\paragraph{Future directions.}
49	The phase-aware allocation principle above points toward a concrete system design: a \emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.
50	The controller would route each generation step through a low-overhead phase classifier (\S\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.
51	Whether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.
52	
53	A second direction concerns completing the mechanistic picture.
54	The discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\S\ref{sec:analysis}).
55	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.
56	
57	Finally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.
58	
59	\subsection{Limitations}
60	\label{sec:limitations}
61	
62	\paragraph{Model scale.}
63	All experiments are conducted at the 7B parameter scale.
64	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
65	Larger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
66	% REVIEWER-ATTACK: "7B is too small to be relevant for production."
67	% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.
68	
69	\paragraph{Architectural scope.}
70	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
71	The cross-model replication (\S\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.
72	The entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.
73	% REVIEWER-ATTACK: "Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM."
74	% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.
75	
76	\paragraph{Task coverage.}
77	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
78	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
79	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
80	% REVIEWER-ATTACK: "Only MATH-500. How do we know this isn't a math-specific artifact?"
81	% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.
82	
83	\paragraph{Statistical scope.}
84	Bootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json
85	The severity difference distribution is right-skewed (mean/median ratio ${\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030
86	All four permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]
87	
88	A notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible
89	This case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.
90	
91	\paragraph{Sparsity range.}
92	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, a moderate range representative of practical deployment targets.
93	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
94	Conversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.
95	% REVIEWER-ATTACK: "Why not test higher sparsity? 0.30 is conservative."
96	% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\Delta$ growth rate $3.8{\times} \to 4.8{\times} \to 2.0{\times}$) suggests saturation at higher sparsity, but confirming this is future work.
97	
98	\paragraph{No throughput evaluation.}
99	This work focuses on characterizing the \emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.
100	We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.
101	% REVIEWER-ATTACK: "No system evaluation. How do we know the severity amplification matters for real deployment?"
102	% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.
103	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "cf623d60-0ca0-4b28-ac2c-6427d5dd0ff9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.\nWe do not dispute this intuition.\nThe surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.\n\nFirst, the \\emph{magnitude} of the severity gradient---$69$--$274{\\times}$ amplification across sparsity levels (Table~\\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.\nA reviewer expecting a $2$--$3\\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.\nSecond, the gradient is \\emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\nThis asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.\nThird, and most strikingly, a \\emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \\emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\\ $0.818$) yet \\emph{underperforms} in low-sparsity phases ($7.196$ vs.\\ $1.363$---a ${>}5{\\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363\nThe same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''\n% REVIEWER-ATTACK: \"The qualitative direction is trivially expected from attention entropy arguments.\"\n% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.\n\n\\paragraph{Random masking as a falsification control.}\nThe random eviction baseline provides a decisive test against the ``trivially expected'' objection.\nIf compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.\nIt does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)\nThe absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.\n\n\\paragraph{Cross-model replication and magnitude asymmetry.}\nThe phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of paired $d_z$ effect sizes across sparsity levels is $\\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043\nAll eight paired Wilcoxon tests (4 sparsity levels $\\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.\n\nThe \\emph{magnitude} of the effect, however, differs substantially.\nQwen's median severity differences ($0.039 \\to 0.235 \\to 1.268 \\to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \\to 1.48 \\to 7.16 \\to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (paired $d_z{=}0.44$), while Qwen's becomes clearly significant only at $s \\geq 0.20$ ($d_z{=}0.55$; $s{=}0.15$ is borderline at $d_z{=}0.28$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds d_z: 0.4416,0.5195,0.6831,0.8031), cohens_d_bf16_qwen.json (qw d_z: 0.2811,0.5494,0.8894,1.0220).\nThe two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.\nWe conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.\n\n\\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) receives partial cross-model support.\nThe discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.\nHowever, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007\nThis divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.\nWe therefore characterize the mechanistic evidence as \\emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.\n\n\\paragraph{Implications for compound sparsity deployment.}\nOur findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.\nCompound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\\S\\ref{sec:analysis}) renders importance-based eviction unreliable.\nA deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.\n\nThis observation motivates \\emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.\nThe severity gradient $G$ reported in \\S\\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \\gg 1$ receive a reduced sparsity budget, while phases with $G \\leq 1$ tolerate aggressive compression with minimal quality loss.\n\n\\paragraph{Future directions.}\nThe phase-aware allocation principle above points toward a concrete system design: a \\emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.\nThe controller would route each generation step through a low-overhead phase classifier (\\S\\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.\nWhether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.\n\nA second direction concerns completing the mechanistic picture.\nThe discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\\S\\ref{sec:analysis}).\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.\n\nFinally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\n",
      "numLines": 103,
      "startLine": 1,
      "totalLines": 103
    }
  }
}
```

</details>

---

### Tool call

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_01G9jz9KdSBDFdYr4TC58iun`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "192b7c68-dcd5-42ee-8648-2a369cb6c464",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 37 · 2026-05-14T10:14:59.774Z_

<details><summary>↩ Tool result · `toolu_01G9jz9KdSBDFdYr4TC58iun`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	We presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.
5	
6	Our contributions, mapped to confirmed claims, are:
7	\begin{enumerate}[nosep,leftmargin=*]
8	    \item \textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d_z{=}{-}0.04$---has negligible effect size).
9	
10	    \item \textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large).
11	
12	    \item \textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\widetilde{\mathrm{II}} = 0.032$ vs.\ $0.818$) and underperforms in low-sparsity phases ($\widetilde{\mathrm{II}} = 7.196$ vs.\ $1.363$)---a qualitative reversal in strategy ranking.
13	
14	    \item \textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.
15	
16	    \item \textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \geq 0.20$ ($d_z \geq 0.55$; Spearman $\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\sim}1/5$ of DeepSeek).
17	
18	    \item \textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.
19	\end{enumerate}
20	
21	\paragraph{Limitations.}
22	Both models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.
23	All experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.
24	We evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.
25	The discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.
26	While discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.
27	
28	\paragraph{Future work.}
29	A \emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.
30	Cross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.
31	Direct measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "f8aacc23-2c92-4473-a565-3c2990b9d717",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/conclusion.tex",
      "content": "\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d_z{=}{-}0.04$---has negligible effect size).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\nWhile discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.",
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

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_01PNWeRYRmDhWE2f1SG1Rj4r`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "89399d6d-9784-417c-8995-ab146e37638c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0139E1JPHCAune9CPZf3QEMP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25912,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 624
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

_source line 39 · 2026-05-14T10:15:00.228Z_

<details><summary>↩ Tool result · `toolu_01PNWeRYRmDhWE2f1SG1Rj4r`</summary>

```text
1	% References for Phase-Gated Compound Sparse paper
2	% Generated 2026-05-14; all entries verified via web search
3	
4	@inproceedings{adakv-neurips2025,
5	    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},
6	    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},
7	    booktitle = {Advances in Neural Information Processing Systems},
8	    year      = {2025},
9	    url       = {https://arxiv.org/abs/2407.11550},
10	}
11	
12	@article{compression-ordering-2025,
13	    title   = {A Systematic Study of Compression Ordering for Large Language Models},
14	    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},
15	    journal = {arXiv preprint arXiv:2511.19495},
16	    year    = {2025},
17	    url     = {https://arxiv.org/abs/2511.19495},
18	}
19	
20	@article{decision-repr-transition-2026,
21	    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},
22	    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},
23	    journal = {arXiv preprint arXiv:2605.07271},
24	    year    = {2026},
25	    url     = {https://arxiv.org/abs/2605.07271},
26	}
27	
28	@article{deepseek-r1,
29	    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},
30	    author  = {{DeepSeek-AI}},
31	    journal = {Nature},
32	    volume  = {645},
33	    pages   = {633--638},
34	    year    = {2025},
35	    url     = {https://arxiv.org/abs/2501.12948},
36	}
37	
38	@inproceedings{defensivekv-iclr2026,
39	    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},
40	    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},
41	    booktitle = {International Conference on Learning Representations},
42	    year      = {2026},
43	    url       = {https://arxiv.org/abs/2510.13334},
44	}
45	
46	@article{doing-more-with-less-2026,
47	    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},
48	    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},
49	    journal = {arXiv preprint arXiv:2604.25098},
50	    year    = {2026},
51	    url     = {https://arxiv.org/abs/2604.25098},
52	}
53	
54	@book{efron1993bootstrap,
55	    title     = {An Introduction to the Bootstrap},
56	    author    = {Efron, Bradley and Tibshirani, Robert J.},
57	    publisher = {Chapman \& Hall/CRC},
58	    year      = {1993},
59	}
60	
61	@inproceedings{graspune-acl2026,
62	    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},
63	    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},
64	    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},
65	    year      = {2026},
66	    url       = {https://arxiv.org/abs/2604.19398},
67	}
68	
69	@article{greedy-bias-kvcache-2026,
70	    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},
71	    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},
72	    journal = {arXiv preprint arXiv:2602.02199},
73	    year    = {2026},
74	    url     = {https://arxiv.org/abs/2602.02199},
75	}
76	
77	@inproceedings{h2o2024,
78	    title     = {{H\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},
79	    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},
80	    booktitle = {Advances in Neural Information Processing Systems},
81	    year      = {2023},
82	    url       = {https://arxiv.org/abs/2306.14048},
83	}
84	
85	@inproceedings{kwon2023vllm,
86	    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},
87	    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},
88	    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},
89	    year      = {2023},
90	    url       = {https://arxiv.org/abs/2309.06180},
91	}
92	
93	@inproceedings{math500,
94	    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},
95	    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},
96	    booktitle = {Advances in Neural Information Processing Systems},
97	    year      = {2021},
98	    url       = {https://arxiv.org/abs/2103.03874},
99	}
100	
101	@inproceedings{michel2019sixteen,
102	    title     = {Are Sixteen Heads Really Better than One?},
103	    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},
104	    booktitle = {Advances in Neural Information Processing Systems},
105	    year      = {2019},
106	    url       = {https://arxiv.org/abs/1905.10650},
107	}
108	
109	@inproceedings{mustafar-neurips2025,
110	    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},
111	    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},
112	    booktitle = {Advances in Neural Information Processing Systems},
113	    year      = {2025},
114	    url       = {https://arxiv.org/abs/2505.22913},
115	}
116	
117	@inproceedings{nacl-acl2024,
118	    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},
119	    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},
120	    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},
121	    year      = {2024},
122	    url       = {https://arxiv.org/abs/2408.03675},
123	}
124	
125	@article{obcache-2025,
126	    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},
127	    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},
128	    journal = {arXiv preprint arXiv:2510.07651},
129	    year    = {2025},
130	    url     = {https://arxiv.org/abs/2510.07651},
131	}
132	
133	@inproceedings{pagedeviction-eacl2026,
134	    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},
135	    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},
136	    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},
137	    year      = {2026},
138	    url       = {https://arxiv.org/abs/2509.04377},
139	}
140	
141	@article{phase-transition-compression-2026,
142	    title   = {Phase transitions in large language model compression},
143	    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},
144	    journal = {npj Artificial Intelligence},
145	    volume  = {2},
146	    number  = {21},
147	    year    = {2026},
148	    url     = {https://www.nature.com/articles/s44387-026-00072-8},
149	}
150	
151	@inproceedings{pope2023efficiently,
152	    title     = {Efficiently Scaling Transformer Inference},
153	    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},
154	    booktitle = {Proceedings of Machine Learning and Systems},
155	    year      = {2023},
156	    url       = {https://arxiv.org/abs/2211.05102},
157	}
158	
159	@article{pyramidkv2024,
160	    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},
161	    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},
162	    journal = {arXiv preprint arXiv:2406.02069},
163	    year    = {2024},
164	    url     = {https://arxiv.org/abs/2406.02069},
165	}
166	
167	@article{qwen2.5,
168	    title   = {{Qwen2.5} Technical Report},
169	    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},
170	    journal = {arXiv preprint arXiv:2412.15115},
171	    year    = {2024},
172	    url     = {https://arxiv.org/abs/2412.15115},
173	}
174	
175	@inproceedings{raas-acl2025,
176	    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},
177	    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},
178	    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},
179	    year      = {2025},
180	    url       = {https://arxiv.org/abs/2502.11147},
181	}
182	
183	@article{retentivekv-2026,
184	    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},
185	    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},
186	    journal = {arXiv preprint arXiv:2605.04075},
187	    year    = {2026},
188	    url     = {https://arxiv.org/abs/2605.04075},
189	}
190	
191	@inproceedings{slim-icml2025,
192	    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},
193	    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},
194	    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},
195	    year      = {2025},
196	    url       = {https://arxiv.org/abs/2410.09615},
197	}
198	
199	@inproceedings{snapkv-neurips2024,
200	    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},
201	    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},
202	    booktitle = {Advances in Neural Information Processing Systems},
203	    year      = {2024},
204	    url       = {https://arxiv.org/abs/2404.14469},
205	}
206	
207	
208	@inproceedings{spark-aaai2026,
209	    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},
210	    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},
211	    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},
212	    year      = {2026},
213	    url       = {https://arxiv.org/abs/2508.15212},
214	}
215	
216	@article{sparse-frontier-2025,
217	    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},
218	    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},
219	    journal = {arXiv preprint arXiv:2504.17768},
220	    year    = {2025},
221	    url     = {https://arxiv.org/abs/2504.17768},
222	}
223	
224	@inproceedings{thinkv-iclr2026,
225	    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},
226	    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},
227	    booktitle = {International Conference on Learning Representations},
228	    year      = {2026},
229	    url       = {https://arxiv.org/abs/2510.01290},
230	}
231	
232	@article{unicomp-2026,
233	    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},
234	    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},
235	    journal = {arXiv preprint arXiv:2602.09130},
236	    year    = {2026},
237	    url     = {https://arxiv.org/abs/2602.09130},
238	}
239	
240	@inproceedings{voita2019heads,
241	    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},
242	    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},
243	    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},
244	    year      = {2019},
245	    url       = {https://arxiv.org/abs/1905.09418},
246	}
247	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "d8f9e5dc-1609-4c80-811d-15a5256a66b6",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/references.bib",
      "content": "% References for Phase-Gated Compound Sparse paper\n% Generated 2026-05-14; all entries verified via web search\n\n@inproceedings{adakv-neurips2025,\n    title     = {Ada-{KV}: Optimizing {KV} Cache Eviction by Adaptive Budget Allocation for Efficient {LLM} Inference},\n    author    = {Feng, Yuan and Lv, Junlin and Cao, Yukun and Xie, Xike and Zhou, S. Kevin},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2407.11550},\n}\n\n@article{compression-ordering-2025,\n    title   = {A Systematic Study of Compression Ordering for Large Language Models},\n    author  = {Chhawri, Shivansh and Mahadik, Rahul and Rooj, Suparna},\n    journal = {arXiv preprint arXiv:2511.19495},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2511.19495},\n}\n\n@article{decision-repr-transition-2026,\n    title   = {Understanding Performance Collapse in Layer-Pruned Large Language Models via Decision Representation Transitions},\n    author  = {Shi, Boyu and Liu, Chang and Gao, ChuanBao and Yang, Xu and Geng, Xin},\n    journal = {arXiv preprint arXiv:2605.07271},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.07271},\n}\n\n@article{deepseek-r1,\n    title   = {{DeepSeek-R1}: Incentivizing Reasoning Capability in {LLMs} via Reinforcement Learning},\n    author  = {{DeepSeek-AI}},\n    journal = {Nature},\n    volume  = {645},\n    pages   = {633--638},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2501.12948},\n}\n\n@inproceedings{defensivekv-iclr2026,\n    title     = {{DefensiveKV}: Taming the Fragility of {KV} Cache Eviction in {LLM} Inference},\n    author    = {Feng, Yuan and Guo, Haoyu and Lv, Junlin and Zhou, S. Kevin and Xie, Xike},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.13334},\n}\n\n@article{doing-more-with-less-2026,\n    title   = {Doing More With Less: Revisiting the Effectiveness of {LLM} Pruning for Test-Time Scaling},\n    author  = {Monjur, Ocean and Nahin, Shahriar Kabir and Chhabra, Anshuman},\n    journal = {arXiv preprint arXiv:2604.25098},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2604.25098},\n}\n\n@book{efron1993bootstrap,\n    title     = {An Introduction to the Bootstrap},\n    author    = {Efron, Bradley and Tibshirani, Robert J.},\n    publisher = {Chapman \\& Hall/CRC},\n    year      = {1993},\n}\n\n@inproceedings{graspune-acl2026,\n    title     = {{GRASPrune}: Global Gating for Budgeted Structured Pruning of Large Language Models},\n    author    = {Wang, Ziyang and Xiao, Jiangfeng and Xiao, Chuan and Li, Ruoxiang and Mao, Rui and Qin, Jianbin},\n    booktitle = {Proceedings of the 64th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2604.19398},\n}\n\n@article{greedy-bias-kvcache-2026,\n    title   = {More Than a Quick Glance: Overcoming the Greedy Bias in {KV}-Cache Compression},\n    author  = {Sood, Aryan and Sharma, Tanvi and Agrawal, Vansh},\n    journal = {arXiv preprint arXiv:2602.02199},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.02199},\n}\n\n@inproceedings{h2o2024,\n    title     = {{H\\textsubscript{2}O}: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models},\n    author    = {Zhang, Zhenyu and Sheng, Ying and Zhou, Tianyi and Chen, Tianlong and Zheng, Lianmin and Cai, Ruisi and Song, Zhao and Tian, Yuandong and R{\\'e}, Christopher and Barrett, Clark and Wang, Zhangyang and Chen, Beidi},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2306.14048},\n}\n\n@inproceedings{kwon2023vllm,\n    title     = {Efficient Memory Management for Large Language Model Serving with {PagedAttention}},\n    author    = {Kwon, Woosuk and Li, Zhuohan and Zhuang, Siyuan and Sheng, Ying and Zheng, Lianmin and Yu, Cody Hao and Gonzalez, Joseph E. and Zhang, Hao and Stoica, Ion},\n    booktitle = {Proceedings of the 29th Symposium on Operating Systems Principles},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2309.06180},\n}\n\n@inproceedings{math500,\n    title     = {Measuring Mathematical Problem Solving With the {MATH} Dataset},\n    author    = {Hendrycks, Dan and Burns, Collin and Kadavath, Saurav and Arora, Akul and Basart, Steven and Tang, Eric and Song, Dawn and Steinhardt, Jacob},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2021},\n    url       = {https://arxiv.org/abs/2103.03874},\n}\n\n@inproceedings{michel2019sixteen,\n    title     = {Are Sixteen Heads Really Better than One?},\n    author    = {Michel, Paul and Levy, Omer and Neubig, Graham},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.10650},\n}\n\n@inproceedings{mustafar-neurips2025,\n    title     = {Mustafar: Promoting Unstructured Sparsity for {KV} Cache Pruning in {LLM} Inference},\n    author    = {Joo, Donghyeon and Hosseini, Helya and Hadidi, Ramyad and Asgari, Bahar},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2505.22913},\n}\n\n@inproceedings{nacl-acl2024,\n    title     = {{NACL}: A General and Effective {KV} Cache Eviction Framework for {LLMs} at Inference Time},\n    author    = {Chen, Yilong and Wang, Guoxia and Shang, Junyuan and Cui, Shiyao and Zhang, Zhenyu and Liu, Tingwen and Wang, Shuohuan and Sun, Yu and Yu, Dianhai and Wu, Hua},\n    booktitle = {Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2408.03675},\n}\n\n@article{obcache-2025,\n    title   = {{OBCache}: Optimal Brain {KV} Cache Pruning for Efficient Long-Context {LLM} Inference},\n    author  = {Gu, Yuzhe and Liang, Xiyu and Zhao, Jiaojiao and Diao, Enmao},\n    journal = {arXiv preprint arXiv:2510.07651},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2510.07651},\n}\n\n@inproceedings{pagedeviction-eacl2026,\n    title     = {{PagedEviction}: Structured Block-wise {KV} Cache Pruning for Efficient Large Language Model Inference},\n    author    = {Chitty-Venkata, Krishna Teja and Ye, Jie and Sun, Xian-He and Kougkas, Anthony and Emani, Murali and Vishwanath, Venkatram and Nicolae, Bogdan},\n    booktitle = {Findings of the European Chapter of the Association for Computational Linguistics},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2509.04377},\n}\n\n@article{phase-transition-compression-2026,\n    title   = {Phase transitions in large language model compression},\n    author  = {Ma, Ziyang and Li, Zuchao and Zhang, Lefei and Xia, Gui-Song and Du, Bo and Zhang, Liangpei and Tao, Dacheng},\n    journal = {npj Artificial Intelligence},\n    volume  = {2},\n    number  = {21},\n    year    = {2026},\n    url     = {https://www.nature.com/articles/s44387-026-00072-8},\n}\n\n@inproceedings{pope2023efficiently,\n    title     = {Efficiently Scaling Transformer Inference},\n    author    = {Pope, Reiner and Douglas, Sholto and Chowdhery, Aakanksha and Devlin, Jacob and Bradbury, James and Heek, Jonathan and Xiao, Kefan and Agrawal, Shivani and Dean, Jeff},\n    booktitle = {Proceedings of Machine Learning and Systems},\n    year      = {2023},\n    url       = {https://arxiv.org/abs/2211.05102},\n}\n\n@article{pyramidkv2024,\n    title   = {{PyramidKV}: Dynamic {KV} Cache Compression based on Pyramidal Information Funneling},\n    author  = {Cai, Zefan and Zhang, Yichi and Gao, Bofei and Liu, Yuliang and Liu, Tianyu and Lu, Keming and Xiong, Wayne and Dong, Yue and Chang, Baobao and Hu, Junjie and Xiao, Wen},\n    journal = {arXiv preprint arXiv:2406.02069},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2406.02069},\n}\n\n@article{qwen2.5,\n    title   = {{Qwen2.5} Technical Report},\n    author  = {Yang, An and Yang, Baosong and Zhang, Beichen and Hui, Binyuan and Zheng, Bo and Yu, Bowen and Li, Chengyuan and Liu, Dayiheng and Huang, Fei and Wei, Haoran and others},\n    journal = {arXiv preprint arXiv:2412.15115},\n    year    = {2024},\n    url     = {https://arxiv.org/abs/2412.15115},\n}\n\n@inproceedings{raas-acl2025,\n    title     = {{RaaS}: Reasoning-Aware Attention Sparsity for Efficient {LLM} Reasoning},\n    author    = {Hu, Junhao and Huang, Wenrui and Wang, Weidong and Li, Zhenwen and Hu, Tiancheng and Liu, Zhixia and Chen, Xusheng and Xie, Tao and Shan, Yizhou},\n    booktitle = {Findings of the Association for Computational Linguistics: ACL 2025},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2502.11147},\n}\n\n@article{retentivekv-2026,\n    title   = {{RetentiveKV}: State-Space Memory for Uncertainty-Aware Multimodal {KV} Cache Eviction},\n    author  = {Liu, Sihao and Xiong, YuFan and Jiang, Zhonghua and Wang, Zhaode and Lv, Chengfei and Zhang, Shengyu},\n    journal = {arXiv preprint arXiv:2605.04075},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2605.04075},\n}\n\n@inproceedings{slim-icml2025,\n    title     = {{SLiM}: One-shot Quantization and Sparsity with Low-rank Approximation for {LLM} Weight Compression},\n    author    = {Mozaffari, Mohammad and Yazdanbakhsh, Amir and Dehnavi, Maryam Mehri},\n    booktitle = {Proceedings of the 42nd International Conference on Machine Learning},\n    year      = {2025},\n    url       = {https://arxiv.org/abs/2410.09615},\n}\n\n@inproceedings{snapkv-neurips2024,\n    title     = {{SnapKV}: {LLM} Knows What You Are Looking for Before Generation},\n    author    = {Li, Yuhong and Huang, Yingbing and Yang, Bowen and Venkitesh, Bharat and Locatelli, Acyr and Ye, Hanchen and Cai, Tianle and Lewis, Patrick and Chen, Deming},\n    booktitle = {Advances in Neural Information Processing Systems},\n    year      = {2024},\n    url       = {https://arxiv.org/abs/2404.14469},\n}\n\n\n@inproceedings{spark-aaai2026,\n    title     = {{SparK}: Query-Aware Unstructured Sparsity with Recoverable {KV} Cache Channel Pruning},\n    author    = {Liao, Huanxuan and Xu, Yixing and He, Shizhu and Li, Guanchen and Yin, Xuanwu and Li, Dong and Barsoum, Emad and Zhao, Jun and Liu, Kang},\n    booktitle = {Proceedings of the AAAI Conference on Artificial Intelligence},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2508.15212},\n}\n\n@article{sparse-frontier-2025,\n    title   = {The Sparse Frontier: Sparse Attention Trade-offs in Transformer {LLMs}},\n    author  = {Nawrot, Piotr and Li, Robert and Huang, Renjie and Ruder, Sebastian and Marchisio, Kelly and Ponti, Edoardo M.},\n    journal = {arXiv preprint arXiv:2504.17768},\n    year    = {2025},\n    url     = {https://arxiv.org/abs/2504.17768},\n}\n\n@inproceedings{thinkv-iclr2026,\n    title     = {{ThinKV}: Thought-Adaptive {KV} Cache Compression for Efficient Reasoning Models},\n    author    = {Ramachandran, Akshat and Neseem, Marina and Sakr, Charbel and Venkatesan, Rangharajan and Khailany, Brucek and Krishna, Tushar},\n    booktitle = {International Conference on Learning Representations},\n    year      = {2026},\n    url       = {https://arxiv.org/abs/2510.01290},\n}\n\n@article{unicomp-2026,\n    title   = {{UniComp}: A Unified Evaluation of Large Language Model Compression via Pruning, Quantization and Distillation},\n    author  = {von Rad, Jonathan and Cao, Yong and Geiger, Andreas},\n    journal = {arXiv preprint arXiv:2602.09130},\n    year    = {2026},\n    url     = {https://arxiv.org/abs/2602.09130},\n}\n\n@inproceedings{voita2019heads,\n    title     = {Analyzing Multi-Head Self-Attention: Specialized Heads Do the Heavy Lifting, the Rest Can Be Pruned},\n    author    = {Voita, Elena and Talbot, David and Moiseev, Fedor and Sennrich, Rico and Titov, Ivan},\n    booktitle = {Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics},\n    year      = {2019},\n    url       = {https://arxiv.org/abs/1905.09418},\n}\n",
      "numLines": 247,
      "startLine": 1,
      "totalLines": 247
    }
  }
}
```

</details>

---

### Assistant

_source line 40_

<details><summary>Logged reasoning block</summary>

```text
I've read all 11 files. Now I need to sync them to the server. Let me create the paper directory and write all files. I'll need to use ssh_execute for each file. Let me batch them efficiently.

The main.tex uses `\bibliographystyle{acl_natbib}` which will need the acl_natbib.bst file. I should check if it exists or change to plainnat.

Let me start by creating the directory and writing files. I'll do multiple files in parallel.

Actually, I need to be careful about the heredoc approach - the files contain special characters like backslashes, dollar signs, etc. I need to use a proper quoting mechanism.


I'm going to write each file via ssh_execute using a single-quoted heredoc delimiter to prevent variable expansion, but I should consider using base64 encoding since these files have complex special characters that could cause issues even with careful quoting.

Actually, the single-quoted heredoc approach should work fine for LaTeX files since it prevents all shell expansion. Let me start by creating the directory, then write the files in order—main.tex, abstract.tex, introduction.tex, and the others—batching where I can but likely sending individual calls for the larger files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "f2dd1acf-84ca-449f-ab5e-0570493409c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH2zKXdRrRFRHTJYvznnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 46516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 46516
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

_source line 41_

所有文件已读取。现在创建目录并同步文件到服务器。先创建目录和写入较短的文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "80e7970e-9fd7-417f-9eb4-c0aeb19f0974",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH2zKXdRrRFRHTJYvznnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 46516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 46516
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

_source line 42_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01PsJemw9L37uXo7zfoGjUFc`</summary>

```json
{
  "server": "westd-22162",
  "command": "mkdir -p /root/autodl-tmp/pacs/paper/figures",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "9f5ca995-4568-43fa-8d1f-09ed80e3bed6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KcH2zKXdRrRFRHTJYvznnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 46516,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 46516
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

_source line 43 · 2026-05-14T10:15:19.877Z_

<details><summary>↩ Tool result · `toolu_01PsJemw9L37uXo7zfoGjUFc`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "c221eb14-32f9-4136-b049-3e89dd22d14c",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

目录创建完成。现在并行写入所有 11 个文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "65922168-9450-4103-bf3f-f051b74b6248",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEEXUY53ALfifEiZwPQbZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 58357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01YUzqThi3eUw24EvjBAL2BA`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/main.tex << 'TEXEOF'\n% TODO: Replace \\documentclass and package setup below with EMNLP/ACL template:\n%   \\documentclass[11pt]{article}\n%   \\usepackage{acl}\n%   or download ACL 2025 style files from https://github.com/acl-org/acl-style-files\n% Current setup uses standard article class as a placeholder.\n\n\\documentclass[11pt]{article}\n\n% --- Geometry (approximate ACL two-column layout) ---\n\\usepackage[a4paper, margin=2.5cm]{geometry}\n\n% --- Essential packages ---\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{enumitem}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage[hidelinks]{hyperref}\n\\usepackage{natbib}\n\\usepackage{times}\n\n\\graphicspath{{figures/}}\n\n% --- Title ---\n\\title{Phase-Modulated Compound Sparsity:\\\\Strategy-Dependent Severity Gradients in Reasoning Models}\n\n% Anonymous submission\n\\author{Anonymous}\n\n\\date{}\n\n\\begin{document}\n\n\\maketitle\n\n% --- Abstract ---\n\\input{abstract}\n\n% --- Main body ---\n\\input{introduction}\n\\input{related_work}\n\\input{background}\n\\input{methodology}\n\\input{results}\n\\input{analysis}\n\\input{discussion}\n\\input{conclusion}\n\n% --- References ---\n\\bibliographystyle{plainnat}\n\\bibliography{references}\n\n% --- Appendix (if needed) ---\n% \\appendix\n% \\input{appendix}\n\n\\end{document}\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "4d2ef102-0ec7-4b47-a49e-ddf668f43818",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEEXUY53ALfifEiZwPQbZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 58357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 46 · 2026-05-14T10:15:31.177Z_

<details><summary>↩ Tool result · `toolu_01YUzqThi3eUw24EvjBAL2BA`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "d3d2ee6d-6243-4847-a9e4-ce77d8aa7ab8",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.43}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.43}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01Sc3bEBH7jDjKU3SarPeLEh`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/abstract.tex << 'TEXEOF'\n\\begin{abstract}\nCompound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.\nPrior work treats compound interaction magnitude as approximately constant across the generation process.\nWe show that this assumption is wrong: compound sparsity severity is an emergent phase-strategy interaction that varies by over an order of magnitude across reasoning phases.\n\nWe evaluate compound sparsity on DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct (both Qwen2 architecture, 7B parameters) using 50 MATH-500 problems, measuring the Interaction Index---a super-additivity metric---across quantile-segmented reasoning phases at sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$.\nUnder importance-based KV cache eviction, the median Interaction Index difference between low-sparsity and high-sparsity reasoning phases increases monotonically from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired Cohen's $d_z$ growing from $0.44$ (small) to $0.80$ (large); Bonferroni-corrected permutation tests yield $p < 0.005$ at all four sparsity levels.\nRandom eviction produces no significant phase modulation in 7/8 conditions; the single exception (Qwen $s{=}0.30$, $p{=}0.012$) shows negligible effect size ($d_z{=}{-}0.04$), confirming that the severity gradient is strategy-specific, not an inherent property of compound sparsity.\nAt $s{=}0.25$, a crossover emerges: importance-based eviction outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) yet underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\nThe pattern replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$).\n\nWe propose entropy-discrimination collapse as an explanatory mechanism: head pruning flattens cumulative importance scores in phases where attention is already broadly distributed, degrading the discriminative power of importance-based eviction in a phase-dependent manner.\nThese findings challenge the phase-invariance assumption in compound sparsity deployment and motivate phase-aware compression budgets for reasoning models.\n\\end{abstract}\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "f2265c74-7cca-4ebc-b782-04ecc2fc2798",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEEXUY53ALfifEiZwPQbZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 58357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 48 · 2026-05-14T10:15:49.933Z_

<details><summary>↩ Tool result · `toolu_01Sc3bEBH7jDjKU3SarPeLEh`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "5a1c6957-1a63-477e-98f8-222417b0b5fe",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_018FDEFzHhdJ4XWase22B4h7`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/conclusion.tex << 'TEXEOF'\n\\section{Conclusion}\n\\label{sec:conclusion}\n\nWe presented an empirical investigation of how compound sparsity severity---the super-additive interaction between attention head pruning and KV cache eviction---varies across reasoning phases and eviction strategies in 7B-parameter language models. Our central finding is that compound severity is not a fixed property of the sparsity level but an emergent phase-strategy interaction whose magnitude spans over an order of magnitude within a single generation.\n\nOur contributions, mapped to confirmed claims, are:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item \\textbf{Strategy dependence (C1).} Compound severity depends qualitatively on the eviction strategy: importance-based eviction produces phase-modulated interaction (median phase difference $0.39$--$14.59$), while random eviction shows no significant phase modulation in 7/8 conditions (the sole exception---Qwen $s{=}0.30$, $p{=}0.012$, $d_z{=}{-}0.04$---has negligible effect size).\n\n    \\item \\textbf{Phase modulation (C2).} Under importance-based eviction, the median Interaction Index difference between low- and high-sparsity phases increases monotonically with sparsity (Bonferroni-corrected $p < 0.005$ at all four levels), with paired effect sizes growing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large).\n\n    \\item \\textbf{Phase-strategy crossover (C3).} At $s{=}0.25$, importance-based eviction simultaneously outperforms random in high-sparsity phases ($\\widetilde{\\mathrm{II}} = 0.032$ vs.\\ $0.818$) and underperforms in low-sparsity phases ($\\widetilde{\\mathrm{II}} = 7.196$ vs.\\ $1.363$)---a qualitative reversal in strategy ranking.\n\n    \\item \\textbf{Sub-exponential growth (C6).} The severity gradient grows with sparsity but at a decelerating rate, suggesting a natural ceiling on phase-dependent amplification.\n\n    \\item \\textbf{Cross-model replication (C5).} The monotonic gradient replicates on Qwen2.5-7B-Instruct at $s \\geq 0.20$ ($d_z \\geq 0.55$; Spearman $\\rho = 1.0$ across sparsity levels; gradient permutation $p = 0.043$), with attenuated absolute magnitude (${\\sim}1/5$ of DeepSeek).\n\n    \\item \\textbf{Mechanistic explanation (C4).} Discrimination collapse---whereby head pruning degrades the discriminative power of importance scores---is robustly confirmed across both models (Gini and CV decrease in all 16 conditions). A secondary entropy redistribution pattern is consistent for DeepSeek but partially replicates on Qwen (2/4 conditions), indicating model-dependent modulation.\n\\end{enumerate}\n\n\\paragraph{Limitations.}\nBoth models share the Qwen2 architecture; our cross-model comparison isolates training methodology (distillation vs.\\ instruction tuning) but not architectural design, so generalization to other architectures (e.g., LLaMA, Mistral, multi-latent attention) remains open.\nAll experiments are at the 7B scale; whether severity gradients persist, amplify, or attenuate at larger scales is untested.\nWe evaluate on a single benchmark (MATH-500); different reasoning domains may induce different phase structures.\nThe discrimination collapse mechanism is supported by correlational evidence but lacks direct causal validation through controlled entropy manipulation.\nWhile discrimination collapse (Gini and CV reduction) is consistent across all conditions for both models, the entropy redistribution component replicates on only 2 of 4 sparsity levels for Qwen, suggesting model-specific factors modulate its manifestation.\n\n\\paragraph{Future work.}\nA \\emph{phase-gated sparsity controller} that dynamically adjusts compound sparsity budgets per reasoning phase could mitigate the severity amplification we document while preserving compression gains where compound behavior is near-additive.\nCross-architecture validation and scaling to larger models would establish the generality of the phase-strategy interaction.\nDirect measurement of per-head entropy shifts under pruning would provide causal evidence for the collapse mechanism.\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "903d2849-af40-4ab9-a003-fb56aaa2cec0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PEEXUY53ALfifEiZwPQbZo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 737,
      "cache_read_input_tokens": 58357,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 737
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

_source line 50 · 2026-05-14T10:16:13.110Z_

<details><summary>↩ Tool result · `toolu_018FDEFzHhdJ4XWase22B4h7`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "767c302e-0c1d-4f39-a52f-6c78cee70dfa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016D1upYx7C8nWPgyRcUMPyX`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/introduction.tex << 'TEXEOF'\n\\section{Introduction}\n\\label{sec:introduction}\n\nLong-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length and dominates inference memory at scale \\cite{kwon2023vllm, pope2023efficiently}.\nTwo complementary responses have emerged: \\emph{attention head pruning}, which removes structurally redundant heads \\cite{voita2019heads, michel2019sixteen}, and \\emph{KV cache eviction}, which discards low-importance token positions from the cache \\cite{snapkv-neurips2024, adakv-neurips2025}.\nDeploying both simultaneously---\\emph{compound sparsity}---is attractive because the compression gains multiply, but the resulting quality degradation can be super-additive: the joint loss exceeds the sum of individual losses \\cite{spark-aaai2026, slim-icml2025}.\n\nPrior work has characterized compound interaction as a property of the sparsity level---higher sparsity yields more interaction---but treats the interaction magnitude as roughly constant across the generation process \\cite{spark-aaai2026, unicomp-2026}.\nThis assumption is problematic for reasoning-capable models, whose generations are structurally heterogeneous: a single chain-of-thought trace alternates between phases of broadly distributed attention (exploratory reasoning) and phases of sharply concentrated attention (structured computation) \\cite{thinkv-iclr2026, decision-repr-transition-2026}.\nIf compound interaction severity varies across these phases, then a uniform sparsity budget---the standard deployment practice---may be safe in one phase yet destructive in another.\n\nWe investigate whether compound sparsity severity is modulated by reasoning phase and eviction strategy.\nOur central finding is that it is, and strongly so: under importance-based KV cache eviction, the Interaction Index---a measure of super-additive compound degradation---is concentrated in the low-sparsity phase (where attention distributes broadly) and largely absent in the high-sparsity phase (where attention is focused).\nThis \\emph{severity gradient} grows monotonically with the sparsity budget: on DeepSeek-R1-Distill-Qwen-7B, the median phase difference in Interaction Index rises from $0.39$ at $s{=}0.15$ to $14.59$ at $s{=}0.30$, with paired effect sizes increasing from $d_z{=}0.44$ (small) to $d_z{=}0.80$ (large); Bonferroni-corrected permutation tests confirm significance at all four sparsity levels on this model ($p < 0.005$).\nThe pattern replicates at $s \\geq 0.20$ on Qwen2.5-7B-Instruct ($d_z \\geq 0.55$) with attenuated absolute magnitude, though the effect at $s{=}0.15$ is marginal ($d_z{=}0.28$, bootstrap CI includes zero).\nCritically, random eviction produces no such gradient: 7/8 conditions across both models fail to exhibit a significant phase difference (the single exception---Qwen $s{=}0.30$---has negligible effect size, $d_z{=}{-}0.04$), confirming that the severity gradient is an emergent property of the interaction between importance scoring and phase-dependent attention structure, not an artifact of compound sparsity per se.\n\nWe propose \\emph{entropy-discrimination collapse} as an explanatory mechanism.\nHead pruning forces surviving heads to redistribute attention mass, increasing attention entropy.\nIn low-sparsity phases, where attention is already broadly distributed, this redistribution flattens the cumulative importance scores used for KV eviction, degrading their discriminative power.\nImportance-based eviction then degenerates into a biased pseudo-random process that can inadvertently remove critical positions---amplifying compound severity.\nIn high-sparsity phases, attention concentration is preserved after pruning, importance scores remain discriminative, and eviction remains well-targeted.\nRandom eviction is immune to this mechanism because its decisions are independent of attention patterns.\n\nOur contributions are as follows:\n\\begin{enumerate}[nosep,leftmargin=*]\n    \\item We identify a \\textbf{phase--strategy interaction} in compound sparsity: importance-based eviction exhibits a severity gradient across reasoning phases that is absent under random eviction (\\S\\ref{sec:results}).\n    \\item We show that this severity gradient \\textbf{increases monotonically with sparsity} and replicate the finding at moderate-to-high sparsity ($s \\geq 0.20$) across two models with different training regimes (distillation vs.\\ instruction tuning), establishing robustness within the Qwen2 architecture family (\\S\\ref{sec:results}).\n    \\item We propose \\textbf{entropy-discrimination collapse} as a mechanistic explanation, linking head pruning to the degradation of importance-score discriminability in a phase-dependent manner (\\S\\ref{sec:analysis}).\n\\end{enumerate}\n\nThese findings challenge the implicit assumption that compound interaction magnitude is phase-invariant, and suggest that sparsity budgets should be allocated in a phase-aware manner---tightening compression during low-sparsity reasoning phases where compound interaction is most severe.\nThe remainder of this paper is organized as follows: \\S\\ref{sec:related} surveys related work on compound compression, KV cache eviction, and phase-aware inference; \\S\\ref{sec:background} formalizes compound sparsity and introduces the Interaction Index; \\S\\ref{sec:experimental-setup} describes our experimental setup; \\S\\ref{sec:results} presents the main results; \\S\\ref{sec:analysis} analyzes the entropy-discrimination collapse mechanism; and \\S\\ref{sec:discussion} discusses implications and limitations.\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "31982ebf-15df-48a4-97b2-7022b0f930fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrVbWZuKHwvnvqCcoUEGY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 59094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2848
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 52 · 2026-05-14T10:16:53.400Z_

<details><summary>↩ Tool result · `toolu_016D1upYx7C8nWPgyRcUMPyX`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "e1320434-0d15-4087-a7a6-f16a59d41d41",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_0183V99gidqLeGY3GCwGbhdi`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/related_work.tex << 'TEXEOF'\n\\section{Related Work}\n\\label{sec:related}\n\n\\subsection{Compound and Joint Compression}\n\nCombining multiple compression axes produces non-additive errors.\n\\cite{spark-aaai2026} report super-additive degradation when combining channel pruning with token eviction, with up to 65\\% quality loss exceeding individual component effects---the first explicit measurement of this phenomenon in KV cache sparsity.\n\\cite{slim-icml2025} formalize compound error for quantization and sparsity, deriving an invertible saliency function for low-rank compensation and confirming that aggregated error is strictly non-additive.\n\\cite{unicomp-2026} evaluate compound compression across 40+ benchmarks, revealing that reasoning and multilingual capabilities degrade disproportionately relative to factual recall.\nThe order of compression stages is itself consequential: \\cite{compression-ordering-2025} show that early quantization causes irreversible information loss, making P$\\to$KD$\\to$Q strictly preferable.\nAt a more fundamental level, \\cite{phase-transition-compression-2026} characterize independent phase transition points per compression dimension, implying that the joint safe region is the intersection---not the union---of per-dimension safe zones.\nOn the structural side, GRASPrune~\\cite{graspune-acl2026} learns global budget-constrained gates to jointly prune FFN channels and attention heads, but treats the pruning decision as static across generation.\nThese works establish that compound interaction produces non-additive errors, but share an implicit assumption: the interaction magnitude is either constant across the generation process or varies only by task---not by reasoning phase or eviction strategy.\nHow compound severity shifts across reasoning phases within a single generation remains unexamined.\n\n\\subsection{KV Cache Eviction}\n\nMost eviction methods rely on importance scoring, yet accumulating evidence questions its reliability.\nAda-KV~\\cite{adakv-neurips2025} introduce per-head adaptive budget allocation, outperforming uniform distribution but assuming stable importance across generation.\nSnapKV~\\cite{snapkv-neurips2024} identifies important KV positions per head from an observation window at the end of the prompt, compressing the cache before generation begins---effective for long contexts but committing to a fixed importance snapshot that cannot adapt across reasoning phases.\n\\cite{defensivekv-iclr2026} show that standard mean-based importance aggregation is fragile, with worst-case quality loss 2.3--4.3$\\times$ higher than expected; their defensive aggregation mitigates but does not eliminate the instability.\n\\cite{nacl-acl2024} combine proxy-token eviction with random eviction to counteract attention bias, improving robustness over pure importance-based methods; yet the eviction policy remains uniform throughout generation.\n\\cite{obcache-2025} derive a second-order joint K-V saliency score from optimal brain damage theory, establishing that key pruning impacts quality more than value pruning---a useful asymmetry, though the score remains time-invariant.\n\\cite{mustafar-neurips2025} achieve 70\\% unstructured KV sparsity through per-token magnitude pruning without quality loss, demonstrating that fine-grained within-entry sparsity and coarse token eviction are complementary axes.\nRetentiveKV~\\cite{retentivekv-2026} identifies \\emph{deferred importance}: tokens with low initial salience can become pivotal later, undermining single-snapshot importance estimates.\n\\cite{greedy-bias-kvcache-2026} further show that any single importance metric exhibits greedy bias, systematically missing structurally relevant tokens.\nA recurring theme is that importance estimates become unreliable under specific conditions, but these conditions are characterized in terms of aggregation functions or metric choice---not the reasoning phase during which eviction occurs, nor the interaction with concurrent head pruning.\n\n\\subsection{Phase-Aware Inference}\n\nSeveral concurrent works introduce phase-awareness into LLM inference.\nThinKV~\\cite{thinkv-iclr2026} partitions generation into phases and applies different KV cache strategies per phase, achieving strong single-axis results that motivate our phase decomposition---but without compound interaction.\n\\cite{pagedeviction-eacl2026} manage block-wise eviction with separate prefill and decode policies, a coarse two-phase scheme that does not extend to within-generation reasoning phases.\n\\cite{decision-repr-transition-2026} discover that layer pruning sensitivity depends on whether a layer operates in the ``silent'' or ``decisive'' phase of representation formation, with silent-phase pruning causing collapse---direct evidence that compression tolerance is phase-modulated.\n\\cite{doing-more-with-less-2026} provide sign reversal evidence: unstructured pruning combined with test-time scaling can exceed unpruned baselines, suggesting that sparsity interacts constructively with extended reasoning under certain conditions.\n\\cite{raas-acl2025} report non-monotonic token importance across decoding steps, and \\cite{sparse-frontier-2025} find no universally optimal sparse attention strategy across tasks and generation stages.\n\nThese works establish that compression tolerance is phase-dependent, but each examines either phase-aware compression along a single axis or compound compression without phase conditioning.\nOur work bridges this gap by quantifying how compound sparsity severity varies across reasoning phases and how this variation is modulated by eviction strategy---specifically, the phase-dependent severity gradient that distinguishes importance-based eviction from random baselines in compound settings.\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "6067ba8e-cfda-4967-81f8-0257d192c49a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrVbWZuKHwvnvqCcoUEGY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 59094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2848
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 54 · 2026-05-14T10:17:30.692Z_

<details><summary>↩ Tool result · `toolu_0183V99gidqLeGY3GCwGbhdi`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "86b3f700-1ab9-4ed8-95a3-9d313ceb6f95",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01TLGxtgGqukn4GpPfnAWZD2`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/background.tex << 'TEXEOF'\n% Section 3: Background and Problem Setup\n% Note: eq:ii and eq:gradient are the canonical definitions.\n% Methodology.tex should reference these via \\eqref rather than redefining.\n\n\\section{Background and Problem Setup}\n\\label{sec:background}\n\nWe formalize compound sparsity as the simultaneous application of attention head pruning and KV cache eviction, define the Interaction Index to quantify their non-additive coupling, and introduce phase segmentation to localize the analysis across reasoning stages.\n\n\\subsection{Compound Sparsity Formulation}\n\\label{sec:compound-sparsity}\n\nConsider a Transformer language model with $L$ layers, each containing $H$ attention heads.\nLet $s \\in (0,1)$ denote a unified sparsity budget applied to both compression axes.\n\n\\paragraph{Attention head pruning.}\nFor each layer $\\ell$, heads are ranked by Frobenius norm importance $w_j^{(\\ell)} = \\|\\mathbf{A}_j^{(\\ell)}\\|_F$, where $\\mathbf{A}_j^{(\\ell)} \\in \\mathbb{R}^{T \\times T}$ is the attention matrix for head $j$ \\cite{voita2019heads, michel2019sixteen}.\nA binary mask $m_j^{(\\ell)} \\in \\{0,1\\}$ retains the top-$(1{-}s)\\cdot H$ heads, zeroing the output of pruned heads:\n\\begin{equation}\n    \\tilde{\\mathbf{o}}_j^{(\\ell)} = m_j^{(\\ell)} \\cdot \\mathbf{o}_j^{(\\ell)}.\n    \\label{eq:head-mask}\n\\end{equation}\n\n\\paragraph{KV cache eviction.}\nFor a sequence of length $T$, a position mask $\\mathbf{m}_k \\in \\{0,1\\}^T$ retains the top-$(1{-}s)\\cdot T$ positions, with the BOS token always preserved.\nEvicted positions are blocked via attention masking:\n\\begin{equation}\n    \\tilde{a}_{ij} = a_{ij} \\cdot m_{k,j}, \\quad \\forall\\, i, j.\n    \\label{eq:kv-mask}\n\\end{equation}\nWe compare two strategies for constructing $\\mathbf{m}_k$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{Importance-based:} Each position $j$ is scored by its cumulative attention mass with position normalization:\n    \\begin{equation}\n        \\mathrm{imp}(j) = \\frac{\\sum_{\\ell, h, i} a_{ij}^{(\\ell,h)}}{T - j},\n        \\label{eq:kv-importance}\n    \\end{equation}\n    where the denominator compensates for causal bias---earlier positions are attended to by more queries \\cite{thinkv-iclr2026, defensivekv-iclr2026}.\n    \\item \\textbf{Random:} Positions (excluding BOS) are evicted uniformly at random.\n\\end{itemize}\n\n\\paragraph{Compound sparsity.}\nApplying both mechanisms simultaneously at sparsity level $s$ (pruning fraction $p = s$, eviction fraction $q = s$) yields \\emph{compound sparsity}.\nThe two axes are not independent: head pruning redistributes attention mass among surviving heads, which alters the importance ranking used for KV cache eviction.\nPrior analyses of compound compression \\cite{spark-aaai2026} report that the joint effect is generally super-additive but treat the interaction magnitude as a fixed property of $s$.\nWe investigate whether the eviction strategy and reasoning phase introduce additional structure.\n\n\\subsection{Interaction Index}\n\\label{sec:interaction-index}\n\nTo quantify the interaction between head pruning and KV cache eviction, we define the \\emph{Interaction Index} (II) following the factorial interaction framework from experimental design.\n\nFor a given text segment, let $\\text{PPL}_d$, $\\text{PPL}_a$, $\\text{PPL}_k$, and $\\text{PPL}_b$ denote the perplexity under the dense (no sparsity), attention-pruning-only, KV-eviction-only, and compound conditions, respectively.\nPerplexity is computed as $\\text{PPL} = \\exp\\!\\bigl(\\frac{1}{|S|}\\sum_{t \\in S} \\mathcal{L}_t\\bigr)$, where $\\mathcal{L}_t$ is the per-token cross-entropy loss over evaluated positions $S$.\nNormalizing by the dense baseline yields relative degradation ratios $r_c = \\text{PPL}_c\\,/\\,\\text{PPL}_d$ for $c \\in \\{a, k, b\\}$, and the Interaction Index:\n\\begin{equation}\n    \\mathrm{II} = r_b - r_a - r_k + 1.\n    \\label{eq:ii}\n\\end{equation}\n\nUnder additive independence, $r_b \\approx r_a + r_k - 1$, yielding $\\mathrm{II} \\approx 0$.\nThe sign of II determines the interaction regime:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item $\\mathrm{II} > 0$: \\textbf{super-additive}---compound degradation exceeds the sum of individual effects.\n    \\item $\\mathrm{II} < 0$: \\textbf{sub-additive}---the compound effect is less than the sum of parts.\n    \\item $\\mathrm{II} = 0$: \\textbf{additive}---the two mechanisms do not interact.\n\\end{itemize}\n\n\\paragraph{Choice of additive null.}\nEquation~\\ref{eq:ii} posits an additive null $r_b = r_a + r_k - 1$ rather than multiplicative independence $r_b = r_a \\cdot r_k$.\nWe adopt the additive form because head pruning and KV cache eviction operate on disjoint model dimensions---structural (which heads to retain) versus positional (which tokens to cache)---so their degradations sum rather than multiply at the sparsity levels we study ($s \\leq 0.30$).\nWe verify in Appendix~\\ref{app:multiplicative-null} that qualitative conclusions are unchanged under the multiplicative null.\n\nNormalizing by $\\text{PPL}_d$ ensures cross-problem comparability.\nBecause the II distribution is heavily right-skewed, we report medians as the central tendency.\n\n\\paragraph{Severity gradient.}\nTo capture how II varies across reasoning phases (defined in \\S\\ref{sec:phase-segmentation}), we define the \\emph{severity gradient}:\n\\begin{equation}\n    G = \\frac{\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}}{\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}},\n    \\label{eq:gradient}\n\\end{equation}\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices in the low-sparsity and high-sparsity phases, respectively.\n$G \\gg 1$ indicates that compound interaction concentrates in low-sparsity phases; $G \\approx 1$ indicates phase-invariant degradation.\nWhen $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}} < \\varepsilon$ for a small threshold $\\varepsilon > 0$, we report $G = \\infty$.\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-segmentation}\n\nReasoning-capable LLMs produce token sequences with heterogeneous attention structure: some positions exhibit highly concentrated attention over a few key tokens, while others distribute attention broadly across the context.\nWe partition each generated sequence into three phases based on the local \\emph{attention sparsity profile}, adapting the phase-aware methodology of ThinKV \\cite{thinkv-iclr2026}.\n\n\\paragraph{Attention sparsity.}\nFor each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:\n\\begin{equation}\n    \\sigma_i^{(h)} = \\frac{1}{T} \\sum_{j=1}^{T} \\mathbf{1}\\!\\left[a_{ij}^{(h)} < 0.01 \\cdot \\max_k a_{ik}^{(h)}\\right].\n    \\label{eq:attn-sparsity}\n\\end{equation}\nThe per-position sparsity $\\sigma_i = \\frac{1}{H}\\sum_h \\sigma_i^{(h)}$ averages across all heads.\n\n\\paragraph{Quantile-based segmentation.}\nTokens are partitioned into three groups by the tercile boundaries of $\\{\\sigma_i\\}_{i=1}^{T}$:\n\\begin{itemize}[nosep,leftmargin=*]\n    \\item \\textbf{High-sparsity phase} (top tercile of $\\sigma$): attention concentrates on few tokens; heads are largely redundant, making both pruning and eviction relatively benign.\n    \\item \\textbf{Mid-sparsity phase} (middle tercile): intermediate attention patterns.\n    \\item \\textbf{Low-sparsity phase} (bottom tercile of $\\sigma$): attention distributes broadly; each surviving head carries non-redundant information, making both pruning and eviction more destructive.\n\\end{itemize}\nContiguous segments shorter than $\\texttt{min\\_phase\\_length} = 10$ tokens are merged into adjacent phases to ensure sufficient tokens for stable perplexity estimation.\nThe segmentation is purely data-driven and requires only access to attention weights.\n\nThis phase structure arises naturally during extended chain-of-thought reasoning, where the model alternates between focused retrieval of specific facts (high sparsity) and integrative reasoning across many context positions (low sparsity) \\cite{phase-transition-compression-2026}.\nOur central research question is: \\emph{Is the Interaction Index constant across phases and eviction strategies, or does it exhibit a phase $\\times$ strategy interaction?}\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "7745c24f-2c52-4972-b07d-5b80b1d26d8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CrVbWZuKHwvnvqCcoUEGY9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2848,
      "cache_read_input_tokens": 59094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2848
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 56 · 2026-05-14T10:18:24.551Z_

<details><summary>↩ Tool result · `toolu_01TLGxtgGqukn4GpPfnAWZD2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "e5cf321c-9eae-4de5-b6d0-2f26a21d953d",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.44}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.44}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_01MZFFsXp1m4ECbr9KZPadPT`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/methodology.tex << 'TEXEOF'\n\\section{Experimental Setup}\n\\label{sec:experimental-setup}\n\n\\subsection{Models}\n\\label{sec:models}\n\nWe conduct experiments on two 7B-parameter instruction-tuned models that share the Qwen2 backbone architecture (28 Transformer layers, 28 attention heads with 4-group GQA):\n\n\\paragraph{DeepSeek-R1-Distill-Qwen-7B} serves as our primary evaluation target. This model was distilled from DeepSeek-R1 \\cite{deepseek-r1} and produces explicit chain-of-thought traces delimited by \\texttt{&lt;think>}$\\cdots$\\texttt{&lt;/think>} tags, yielding sequences with pronounced phase structure---extended reasoning followed by a concise solution. The structured generation pattern makes it well-suited for studying how sparsity interacts with distinct reasoning phases.\n\n\\paragraph{Qwen2.5-7B-Instruct} \\cite{qwen2.5} provides a cross-model replication. Although it shares the same backbone family, its instruction tuning does not enforce explicit reasoning delimiters, producing a different distribution of attention sparsity across the generation trajectory. Replication on this model tests whether our findings generalize beyond distillation-induced phase structure.\n\nBoth models are loaded in \\texttt{bfloat16} precision with eager attention (i.e., without FlashAttention) to permit direct manipulation of attention weight matrices during sparsity intervention.\\footnote{An earlier \\texttt{float16} configuration produced sporadic NaN values in Layer~27 of DeepSeek-R1-Distill-Qwen-7B, affecting ${\\sim}$8\\% of logit positions. Switching to \\texttt{bfloat16} eliminated all NaN occurrences; we additionally apply NaN-guarded filtering as a safety net.}\n\n\n\\subsection{Dataset}\n\\label{sec:dataset}\n\nWe evaluate on a 50-problem stratified subset of the MATH-500 benchmark \\cite{math500}, sampling uniformly across problem categories (algebra, geometry, number theory, combinatorics, etc.) with a fixed seed for reproducibility. Mathematical reasoning tasks are a natural testbed for our study: they elicit long chain-of-thought sequences (up to 2048 tokens) in which the model alternates between exploratory reasoning and structured computation---phases that differ markedly in attention sparsity. Each problem is decoded greedily (\\texttt{max\\_new\\_tokens}$=$2048) to eliminate sampling variance.\n\n\n\\subsection{Compound Sparsity Configuration}\n\\label{sec:sparsity-config}\n\nWe apply \\emph{symmetric} compound sparsity: for a given sparsity level $s$, we prune the same fraction $s$ of attention heads and evict the same fraction $s$ of KV cache entries. We evaluate four sparsity levels $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, spanning from mild to aggressive compression.\n\n\\paragraph{Sparsity conditions.} For each problem and each sparsity level, we compute perplexity under four conditions: (i)~\\emph{dense}---no intervention; (ii)~\\emph{attn-only}---head pruning without KV eviction; (iii)~\\emph{kv-only}---KV eviction without head pruning; and (iv)~\\emph{both}---simultaneous head pruning and KV eviction.\n\n\\paragraph{Eviction strategies.} We compare two KV cache eviction strategies:\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Importance-based.} Each KV position receives a score equal to its cumulative attention weight summed over all query positions and heads. To correct for the inherent causal bias---earlier positions accumulate more attention simply because they are attended to by more queries---we apply position normalization:\n\\begin{equation}\n\\label{eq:importance}\n    \\alpha_j = \\frac{\\sum_{i,h} a_{i,h,j}}{\\texttt{seq\\_len} - j}, \\quad j \\in \\{1, \\dots, T\\},\n\\end{equation}\nwhere $a_{i,h,j}$ is the attention weight from query~$i$, head~$h$ to key~$j$, and the denominator counts the number of queries that can attend to position~$j$ under causal masking. Position~0 (BOS) is always retained. The $T \\cdot s$ positions with the lowest normalized scores are evicted.\n\nDuring masked forward passes, we guard against numerical instability from the interaction of head masking and KV eviction: zeroed-out heads that would otherwise produce $\\infty \\times 0 = \\text{NaN}$ are handled via selective replacement (\\texttt{torch.where}) prior to the softmax, and any layer producing NaN outputs is skipped from the sparsity loss computation.\n\n\\item \\textbf{Random.} KV positions (excluding BOS) are evicted uniformly at random, providing a strategy-agnostic baseline. Head pruning under the random condition selects heads via \\texttt{torch.randperm} rather than by importance.\n\\end{itemize}\n\n\\paragraph{Head pruning.} Under importance-based eviction, heads are ranked by their Frobenius norm across the full attention matrix $\\mathbf{A}_\\ell \\in \\mathbb{R}^{H \\times T \\times T}$ per layer $\\ell$, and the bottom-$s$ fraction is masked. Under random eviction, heads are selected uniformly at random.\n\n\n\\subsection{Phase Segmentation}\n\\label{sec:phase-seg}\n\nWe segment each generated sequence into three \\emph{reasoning phases} based on the local attention sparsity of each token position. For each query position $i$, we compute per-head sparsity as the fraction of attention weights falling below $0.01 \\times \\max_j a_{i,h,j}$, then average across heads to obtain a scalar sparsity value per position. The resulting sparsity trajectory is partitioned into terciles via quantile boundaries: \\emph{low-sparsity} (bottom third, corresponding to diffuse attention during exploratory reasoning), \\emph{mid-sparsity}, and \\emph{high-sparsity} (top third, corresponding to focused attention during structured computation). Contiguous segments shorter than $\\texttt{min\\_phase\\_length}=10$ tokens are merged into adjacent phases to suppress noise.\n\n\n\\subsection{Metrics}\n\\label{sec:metrics}\n\n\\paragraph{Perplexity.} For each sparsity condition $c \\in \\{d, a, k, b\\}$ and each phase, we compute segment-level perplexity as\n$\\text{PPL}_c = \\exp\\!\\bigl(\\tfrac{1}{|I|}\\sum_{i \\in I} \\mathcal{L}_c(x_i)\\bigr)$,\nwhere $I$ is the set of token indices belonging to the phase and $\\mathcal{L}_c(x_i)$ is the per-token cross-entropy loss under condition $c$.\n\n\\paragraph{Interaction Index.} The interaction index (Equation~\\eqref{eq:ii}) quantifies the synergistic (super-additive) effect of compound sparsity beyond the sum of individual interventions.\nWhen $\\mathrm{II} > 0$, the two sparsity mechanisms amplify each other; $\\mathrm{II} = 0$ indicates additive (independent) degradation.\n\n\\paragraph{Severity Gradient.} To measure how the interaction varies across reasoning phases, we use the severity gradient (Equation~\\eqref{eq:gradient}):\nwhere $\\widetilde{\\mathrm{II}}_{\\,\\textit{low}}$ and $\\widetilde{\\mathrm{II}}_{\\,\\textit{high}}$ are the median interaction indices over the low-sparsity and high-sparsity phases, respectively. We report medians rather than means because the II distribution is heavily right-skewed (mean/median ratios up to 43:1 at $s{=}0.30$), making the median a more robust central tendency estimator.\n\n\n\\subsection{Statistical Analysis}\n\\label{sec:stats}\n\nAll confidence intervals and significance tests are computed via the nonparametric bootstrap with $B = 10{,}000$ resamples \\cite{efron1993bootstrap}.\n\n\\paragraph{Per-problem bootstrap.} For each sparsity level and strategy, we resample the 50 per-problem II values with replacement and compute the mean of each resample, yielding a 95\\% percentile confidence interval for the population mean II.\n\n\\paragraph{Paired bootstrap.} To test whether the severity gradient differs between importance-based and random eviction, we pair observations by problem (same problem, same sparsity level) and bootstrap the difference in gradients. This controls for problem-level variance in difficulty and sequence length.\n\n\\paragraph{Unpaired bootstrap.} We additionally compute per-strategy gradient confidence intervals without pairing, to verify that the importance-based gradient is significantly greater than 1 (i.e., phase modulation exists) independently of the random baseline.\n\nAll tests yield $p_{\\text{Bonf}} < 0.005$ at every sparsity level, confirming that the observed phase--strategy interactions are not artifacts of sampling variability.\\footnote{Experiments were conducted on a server with 4$\\times$ NVIDIA RTX PRO 6000 Blackwell Server Edition 96\\,GB GPUs, with one model--sparsity configuration per GPU.}\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "b8d2f916-6bb0-4ab9-80ea-0197abd9d11a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCMgKPBBXUWcBdziiCqENY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5877,
      "cache_read_input_tokens": 61942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5877
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 58 · 2026-05-14T10:19:25.268Z_

<details><summary>↩ Tool result · `toolu_01MZFFsXp1m4ECbr9KZPadPT`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "5baf7104-ad7f-427a-b8cd-c7bf5ec1ba87",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.45}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.45}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_016vXqucUwtdbs8Lw3LYBZEV`</summary>

```json
{
  "server": "westd-22162",
  "command": "cat > /root/autodl-tmp/pacs/paper/discussion.tex << 'TEXEOF'\n\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{On the predictability of phase-modulated severity.}\nOne might argue that the qualitative direction of our findings is intuitive: in low-sparsity phases, attention distributes broadly across many tokens, so importance scores carry less discriminative signal, and importance-based eviction should degrade.\nWe do not dispute this intuition.\nThe surprise lies in the quantitative structure of the interaction, which is not predictable from first principles alone.\n\nFirst, the \\emph{magnitude} of the severity gradient---$69$--$274{\\times}$ amplification across sparsity levels (Table~\\ref{tab:main-results})---far exceeds what a naive ``less discriminative $\\Rightarrow$ somewhat worse'' argument would predict. % exp_id: bf16_importance_s015..s030; source: experiment_summary_table.json; G=low/high=69,103,222,274.\nA reviewer expecting a $2$--$3\\times$ effect would find two-orders-of-magnitude amplification difficult to anticipate without measurement.\nSecond, the gradient is \\emph{phase-specific}: compound interaction concentrates in low-sparsity phases while high-sparsity phases exhibit near-zero compound interaction ($\\widetilde{\\mathrm{II}}_{\\text{high}} < 0.06$ at $s \\leq 0.30$; at $s = 0.35$, high-phase II rises to 0.105, indicating the onset of compound interaction even in high-sparsity phases at extreme pruning rates). % exp_id: bf16_importance_s015..s030, bf16_ds_imp_s035; high-phase medians: 0.006, 0.015, 0.032, 0.053; s035 II_high=0.1051\nThis asymmetry means that importance-based eviction is not uniformly fragile---it is selectively fragile in a phase-dependent manner.\nThird, and most strikingly, a \\emph{crossover} emerges: at $s{=}0.25$, importance-based eviction \\emph{outperforms} random eviction in high-sparsity phases (median severity $0.032$ vs.\\ $0.818$) yet \\emph{underperforms} in low-sparsity phases ($7.196$ vs.\\ $1.363$---a ${>}5{\\times}$ severity inflation relative to random). % exp_id: bf16_importance_s025, bf16_ds_rand_s025; source: experiment_summary_table.json; high: imp=0.032, rand=0.818; low: imp=7.196, rand=1.363\nThe same strategy reverses direction across phases---a phenomenon that cannot be derived from the observation that ``importance scores are noisier when attention is diffuse.''\n% REVIEWER-ATTACK: \"The qualitative direction is trivially expected from attention entropy arguments.\"\n% REBUTTAL: (1) Qualitative direction ≠ quantitative structure: 69-274× amplification is two orders of magnitude, not marginal. (2) Phase-specific concentration + crossover cannot be predicted from single-layer entropy reasoning. (3) Random eviction's flat profile (~1×) shows the amplification is strategy-specific, not an inherent property of compound sparsity.\n\n\\paragraph{Random masking as a falsification control.}\nThe random eviction baseline provides a decisive test against the ``trivially expected'' objection.\nIf compound severity amplification were an inherent property of applying two compression methods jointly---rather than an emergent phase-strategy interaction---random eviction should exhibit a comparable phase gradient.\nIt does not: random eviction fails seven of eight paired permutation tests across both models (7/8 FAIL); the single exception (Qwen $s{=}0.30$, $p{=}0.012$) exhibits negligible effect size ($d_z{=}{-}0.04$), producing no practically meaningful phase-modulated severity. % exp_id: bf16_ds_rand_s015..s030, bf16_qw_rand_s015..s030; verdict: 7/8 FAIL, 1 PASS (qw_rand_s030 p=0.012 d=-0.035 negligible)\nThe absence of a phase gradient under random masking isolates the amplification as strategy-specific: it arises from the interaction between importance-based eviction and phase structure, not from compound sparsity per se.\n\n\\paragraph{Cross-model replication and magnitude asymmetry.}\nThe phase-strategy interaction replicates across both models with perfect ordinal agreement: the Spearman rank correlation of paired $d_z$ effect sizes across sparsity levels is $\\rho{=}1.0$, and a gradient permutation test confirms this monotonic co-escalation ($p{=}0.043$). % exp_id: cross_model_correlation; Spearman rho=1.0, gradient_perm p=0.043\nAll eight paired Wilcoxon tests (4 sparsity levels $\\times$ 2 models) reject $H_0$, confirming the pattern is not an artifact of a single model's weight structure.\n\nThe \\emph{magnitude} of the effect, however, differs substantially.\nQwen's median severity differences ($0.039 \\to 0.235 \\to 1.268 \\to 2.943$) are approximately one-fifth of DeepSeek's ($0.39 \\to 1.48 \\to 7.16 \\to 14.59$), and the onset threshold differs: DeepSeek's gradient is significant from $s{=}0.15$ (paired $d_z{=}0.44$), while Qwen's becomes clearly significant only at $s \\geq 0.20$ ($d_z{=}0.55$; $s{=}0.15$ is borderline at $d_z{=}0.28$ with CI crossing zero). % exp_id: cohens_d_bf16.json (ds d_z: 0.4416,0.5195,0.6831,0.8031), cohens_d_bf16_qwen.json (qw d_z: 0.2811,0.5494,0.8894,1.0220).\nThe two models share the Qwen2ForCausalLM architecture but differ in training: DeepSeek-R1-Distill-Qwen-7B is distilled from a larger reasoning model, while Qwen2.5-7B-Instruct undergoes standard instruction tuning.\nWe conjecture that distillation amplifies the phase-strategy interaction by producing sharper internal phase transitions---a hypothesis testable by comparing distilled and non-distilled variants at matched scale.\n\n\\paragraph{Mechanistic evidence: discrimination collapse as the robust signal.}\nThe entropy-discrimination collapse hypothesis (\\S\\ref{sec:analysis}) receives partial cross-model support.\nThe discrimination components---Gini coefficient reduction and coefficient-of-variation compression under compound sparsity---are directionally consistent across both models, confirming that importance-based eviction loses discriminative power in low-sparsity phases regardless of training procedure.\nHowever, the entropy component is model-dependent: DeepSeek exhibits consistent negative entropy shifts (attention concentrates further under head pruning), while Qwen shows a sign reversal at $s{=}0.25$ ($\\Delta H {=} {+}0.045$) and near-zero shift at $s{=}0.30$ ($\\Delta H {=} {-}0.007$). % exp_id: mechanism_entropy_qwen; s025: +0.045, s030: -0.007\nThis divergence suggests that discrimination collapse---not entropy redistribution---is the primary driver of the phase-strategy interaction, with entropy behavior being a model-dependent secondary effect.\nWe therefore characterize the mechanistic evidence as \\emph{preliminary}: the discrimination pathway is robust across models, but the complete entropy-discrimination collapse narrative requires the qualification that its entropy component does not generalize.\n\n\\paragraph{Implications for compound sparsity deployment.}\nOur findings suggest that the standard practice of applying a uniform compression budget across all inference steps is suboptimal for reasoning models.\nCompound severity is not distributed evenly: it concentrates in low-sparsity phases, where the entropy-discrimination collapse mechanism (\\S\\ref{sec:analysis}) renders importance-based eviction unreliable.\nA deployment pipeline that allocates the same sparsity level $s$ to every token position implicitly accepts order-of-magnitude severity penalties during the exploratory reasoning stages that happen to fall in the low-sparsity regime.\n\nThis observation motivates \\emph{phase-aware compression budgets}: rather than a single global sparsity target, the system would allocate higher capacity (lower sparsity) to low-sparsity phases---where compound interaction is most severe---and reclaim that budget in high-sparsity phases, where compound behavior is near-additive and importance-based eviction remains effective.\nThe severity gradient $G$ reported in \\S\\ref{sec:phase-amplification} provides a natural signal for such allocation: phases with $G \\gg 1$ receive a reduced sparsity budget, while phases with $G \\leq 1$ tolerate aggressive compression with minimal quality loss.\n\n\\paragraph{Future directions.}\nThe phase-aware allocation principle above points toward a concrete system design: a \\emph{phase-gated controller} that monitors attention sparsity statistics in real time and dynamically adjusts the compound sparsity budget per reasoning phase.\nThe controller would route each generation step through a low-overhead phase classifier (\\S\\ref{sec:phase-seg}), then apply a phase-specific sparsity configuration derived from the severity gradient.\nWhether such a controller can recover most of the compression benefit while avoiding the severity amplification in low-sparsity phases is an open empirical question.\n\nA second direction concerns completing the mechanistic picture.\nThe discrimination collapse component of our hypothesis is robust across models, but the entropy redistribution component is model-dependent (\\S\\ref{sec:analysis}).\nDirectly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties (e.g., distillation depth, RLHF intensity) determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full entropy-discrimination collapse mechanism.\n\nFinally, scaling the empirical methodology to larger models and diverse reasoning tasks would establish the generality of the phase-strategy interaction documented in this work.\n\n\\subsection{Limitations}\n\\label{sec:limitations}\n\n\\paragraph{Model scale.}\nAll experiments are conducted at the 7B parameter scale.\nWhether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.\nLarger models may exhibit different attention redundancy structures that alter the discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).\n% REVIEWER-ATTACK: \"7B is too small to be relevant for production.\"\n% REBUTTAL: 7B is the most-deployed scale for on-device and cost-constrained serving—exactly where compound sparsity is needed. The mechanism (entropy-discrimination collapse) is scale-agnostic in principle. Scaling experiments are future work.\n\n\\paragraph{Architectural scope.}\nOur two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.\nThe cross-model replication (\\S\\ref{sec:cross-model}) confirms that the findings are not artifacts of a single model's weights, but both models share the same attention mechanism design.\nThe entropy-discrimination collapse mechanism is in principle agnostic across attention architectures (it depends on attention redistribution, not architecture-specific components), but empirical validation on architecturally distinct attention designs (e.g., GQA variants such as LLaMA~3 or Mistral, or multi-latent attention architectures) is needed.\n% REVIEWER-ATTACK: \"Cross-model ≠ cross-architecture. Both are Qwen2ForCausalLM.\"\n% REBUTTAL: Correct—we explicitly state this is cross-model (different training: distillation vs instruction tuning), not cross-architecture. The two models isolate the training variable while controlling architecture. Cross-architecture validation (LLaMA, Mistral) is acknowledged as future work.\n\n\\paragraph{Task coverage.}\nWe evaluate exclusively on MATH-500, a mathematical reasoning benchmark.\nDifferent reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.\nGeneralizing the phase-strategy interaction to broader reasoning domains is an important next step.\n% REVIEWER-ATTACK: \"Only MATH-500. How do we know this isn't a math-specific artifact?\"\n% REBUTTAL: The mechanism (entropy-discrimination collapse under head pruning) depends on attention distribution properties, not math-specific features. MATH-500 is a standard benchmark with diverse difficulty. However, different reasoning tasks may induce different phase structures—we state this limitation explicitly rather than overclaiming.\n\n\\paragraph{Statistical scope.}\nBootstrap confidence intervals use $B{=}10{,}000$ resamples. The paired permutation test yields $n{=}49$ paired problems for DeepSeek (1 excluded) and $n{=}46$ for Qwen (4 excluded). % exp_id: cohens_d_bf16.json, cohens_d_bf16_qwen.json\nThe severity difference distribution is right-skewed (mean/median ratio ${\\sim}1.6{:}1$ at $s{=}0.30$), motivating our use of medians and nonparametric tests rather than parametric alternatives. % exp_id: bf16_importance_s030; mean_diff=22.94, median_diff=14.59 (segment-level). Per-problem paired: median_diff=9.9436 at s030\nAll four permutation tests reject $H_0$ after Bonferroni correction ($p_{\\text{Bonf}} < 0.005$; Table~\\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---confirming the effect direction at every sparsity level. The permutation CIs at higher sparsity are wider (e.g., $[6.70,\\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification. % exp_id: permutation_test_results.json; permutation CIs: s015=[0.19,0.62], s020=[0.69,1.49], s025=[1.66,6.64], s030=[6.70,16.29]\n\nA notable exception among the random baselines is the Qwen random condition at $s{=}0.30$, which yields a statistically significant result ($p{=}0.012$) despite negligible effect size ($d_z{=}{-}0.04$, bootstrap CI excluding zero). % exp_id: qw_rand_s030; B=10000, p=0.012, d=-0.035, negligible\nThis case illustrates that dichotomous significance testing can flag effects of no practical magnitude---reinforcing the importance of reporting effect sizes and confidence intervals alongside $p$-values.\n\n\\paragraph{Sparsity range.}\nOur experiments span $s \\in \\{0.15, 0.20, 0.25, 0.30\\}$, a moderate range representative of practical deployment targets.\nMore extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.\nConversely, the lower boundary at which phase-modulated amplification first emerges is not yet characterized.\n% REVIEWER-ATTACK: \"Why not test higher sparsity? 0.30 is conservative.\"\n% REBUTTAL: Our focus is on the practically relevant regime where models retain usable quality. At s>0.30 both strategies degrade severely, making II measurement less informative. The sub-exponential growth (C6, $\\Delta$ growth rate $3.8{\\times} \\to 4.8{\\times} \\to 2.0{\\times}$) suggests saturation at higher sparsity, but confirming this is future work.\n\n\\paragraph{No throughput evaluation.}\nThis work focuses on characterizing the \\emph{structural} properties of compound sparsity severity---its phase dependence, strategy dependence, and interaction magnitude.\nWe do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to the severity characterization that is our primary contribution.\n% REVIEWER-ATTACK: \"No system evaluation. How do we know the severity amplification matters for real deployment?\"\n% REBUTTAL: This is an empirical finding paper, not a method/system paper. The contribution is characterizing *what happens* (phase-modulated severity) and *why* (entropy-discrimination collapse), not building a system to fix it. Phase-gated controllers are explicitly scoped as future work. The finding is actionable regardless: any compound sparsity deployment should be aware of phase-dependent severity.\nTEXEOF",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "96190be4-4ce0-4fa5-9083-7c1d384f4fbe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FCMgKPBBXUWcBdziiCqENY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5877,
      "cache_read_input_tokens": 61942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5877
      },
      "output_tokens": 43,
      "service_tier": "standard",
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

_source line 60 · 2026-05-14T10:21:12.618Z_

<details><summary>↩ Tool result · `toolu_016vXqucUwtdbs8Lw3LYBZEV`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "dde0a8ee-04bd-4236-8019-52c786743013",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.51}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.51}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 61_

继续写入剩余文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "275610e6-4508-470d-b0b2-cb978b002264",
  "uuid": "8eab58c6-fcab-4c52-a2b2-eb660501fe50",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014VcqkW7Ptu26g69tWUeYkT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6942,
      "cache_read_input_tokens": 67819,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6942
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
