# paper citation attribution audit

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 275
- **Recorded user turns:** 5
- **Tool calls:** 87
- **Original source:** `logs/workers/worker_paper_citation-attribution-audit_20260515T201532.log`
- **Structured JSON:** [`7b31be3032984c9b3147.json`](../../sessions/7b/7b31be3032984c9b3147.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "3fa63ff2-772a-4090-b79d-0474e90fa298",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778886600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "c53c8f08-d237-41f6-afb1-6279038e028c",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me start by finding all the .tex files in the specified directories, then read them to extract all citations and their contextual descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9672358f-b3f4-4fa8-85d8-475918f26c88",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9saNzrYh7dkpEJCHRFsK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11560,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11560
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

_source line 5_

开始审计论文引用方法归因。先找到所有 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8ad187d4-661f-49c7-92a9-e5605c8a40cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9saNzrYh7dkpEJCHRFsK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11560,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11560
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

_source line 6_

<details open><summary>🔧 Tool call — Glob · `toolu_019Y9ADPaspmJLEYhmnET2eN`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "757d8589-50d8-4dcf-94c2-22e72cbbb5d6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9saNzrYh7dkpEJCHRFsK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11560,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11560
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

_source line 7 · 2026-05-15T20:15:44.587Z_

<details><summary>↩ Tool result · `toolu_019Y9ADPaspmJLEYhmnET2eN`</summary>

```text
artifacts/_project/paper/related_work_9c2927.tex
artifacts/_project/paper/introduction_c83872.tex
artifacts/_project/paper/introduction.tex
artifacts/_project/paper/method_section_draft.tex
artifacts/_project/paper/experiments_c64a8c.tex
artifacts/_project/paper/method_fb526b.tex
artifacts/_project/paper/method.tex
artifacts/_project/paper/experiments_ac6246.tex
artifacts/_project/paper/experiments.tex
artifacts/_project/paper/related_work_80791f.tex
artifacts/_project/paper/introduction_scenarioC_607d8d.tex
artifacts/_project/paper/introduction_scenarioC.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/sections/introduction.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e19d5519-2026-49ea-9e97-aa526da69b33",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/related_work_9c2927.tex",
      "artifacts/_project/paper/introduction_c83872.tex",
      "artifacts/_project/paper/introduction.tex",
      "artifacts/_project/paper/method_section_draft.tex",
      "artifacts/_project/paper/experiments_c64a8c.tex",
      "artifacts/_project/paper/method_fb526b.tex",
      "artifacts/_project/paper/method.tex",
      "artifacts/_project/paper/experiments_ac6246.tex",
      "artifacts/_project/paper/experiments.tex",
      "artifacts/_project/paper/related_work_80791f.tex",
      "artifacts/_project/paper/introduction_scenarioC_607d8d.tex",
      "artifacts/_project/paper/introduction_scenarioC.tex",
      "artifacts/_project/paper/related_work.tex",
      "artifacts/_project/paper/sections/introduction.tex"
    ],
    "durationMs": 16,
    "numFiles": 14,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01H273KhYG99QTnmf6MAvKW7`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "c9a04a24-8eae-448e-9bc3-77395a6086f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W9saNzrYh7dkpEJCHRFsK5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11560,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11560
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

_source line 9 · 2026-05-15T20:15:44.795Z_

<details><summary>↩ Tool result · `toolu_01H273KhYG99QTnmf6MAvKW7`</summary>

```text
docs/paper/method.tex
docs/paper/experiments.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "0263ac53-b68d-4275-9b93-7ef4f6ec1c4d",
  "tool_use_result": {
    "filenames": [
      "docs/paper/method.tex",
      "docs/paper/experiments.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 10,
    "numFiles": 3,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 10_

根据任务说明，活跃版本是 `introduction_scenarioC.tex`, `experiments.tex`, `method.tex`, `related_work.tex`。先检查修改时间确认最新版本，然后读取内容。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4f8f9346-559b-4c5a-81d6-227ee28cd8fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPGgmwgispHbVn2zh5i4hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 23401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 547
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

_source line 11_

<details open><summary>🔧 Tool call — Bash · `toolu_014dYX85goW6C3ubgFABH3Qg`</summary>

```json
{
  "command": "ls -lt /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_c64a8c.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex",
  "description": "Check modification times of all tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "074c88d7-73a4-4166-9c11-c9cfbf96ccb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VPGgmwgispHbVn2zh5i4hS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 547,
      "cache_read_input_tokens": 23401,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 547
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

_source line 12 · 2026-05-15T20:15:53.501Z_

<details><summary>↩ Tool result · `toolu_014dYX85goW6C3ubgFABH3Qg`</summary>

```text
-rw-r--r-- 1 ubuntu ubuntu  8099 May 15 19:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  8100 May 15 19:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex
-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex
-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex
-rw-r--r-- 1 ubuntu ubuntu  8094 May 15 19:36 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex
-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:27 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex
-rw-r--r-- 1 ubuntu ubuntu 13333 May 15 19:24 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex
-rw-r--r-- 1 ubuntu ubuntu 10408 May 15 19:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex
-rw-r--r-- 1 ubuntu ubuntu 10408 May 15 19:19 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex
-rw-r--r-- 1 ubuntu ubuntu 10229 May 15 19:14 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex
-rw-r--r-- 1 ubuntu ubuntu 12214 May 13 21:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_c64a8c.tex
-rw-r--r-- 1 ubuntu ubuntu  6382 May 13 17:37 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "672d1314-9a53-403b-ad02-81a2782ee96a",
  "tool_use_result": {
    "stdout": "-rw-r--r-- 1 ubuntu ubuntu  8099 May 15 19:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/related_work.tex\n-rw-r--r-- 1 ubuntu ubuntu  8100 May 15 19:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex\n-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex\n-rw-r--r-- 1 ubuntu ubuntu  7397 May 15 19:50 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC_607d8d.tex\n-rw-r--r-- 1 ubuntu ubuntu  8094 May 15 19:36 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_80791f.tex\n-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/experiments.tex\n-rw-r--r-- 1 ubuntu ubuntu 13669 May 15 19:27 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex\n-rw-r--r-- 1 ubuntu ubuntu 13333 May 15 19:24 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_ac6246.tex\n-rw-r--r-- 1 ubuntu ubuntu 10408 May 15 19:20 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/docs/paper/method.tex\n-rw-r--r-- 1 ubuntu ubuntu 10408 May 15 19:19 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex\n-rw-r--r-- 1 ubuntu ubuntu 10229 May 15 19:14 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method_fb526b.tex\n-rw-r--r-- 1 ubuntu ubuntu 12214 May 13 21:57 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments_c64a8c.tex\n-rw-r--r-- 1 ubuntu ubuntu  6382 May 13 17:37 /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work_9c2927.tex",
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

_source line 13_

现在读取四个最新活跃的 .tex 文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "bcfebb3f-a359-4e6d-bb9a-c6bc77cb9290",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YkrjP2wTNMnv97GBcFVwA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 23948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1683
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

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01UJWeFji844VCdjHgPsJvBx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "312e6c76-0749-470d-8d6e-9592cb6abfe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YkrjP2wTNMnv97GBcFVwA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 23948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1683
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

_source line 15 · 2026-05-15T20:15:56.749Z_

<details><summary>↩ Tool result · `toolu_01UJWeFji844VCdjHgPsJvBx`</summary>

```text
1	\section{Introduction}
2	\label{sec:intro}
3	
4	% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs
5	Vision-language-action models (VLAs) that generate actions via flow matching~\cite{black2024pi0,shukor2025smolvla} achieve 97--99\% success on standard manipulation benchmarks such as LIBERO~\cite{liu2023libero}.
6	Yet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\cite{fei2025liberoplus}.
7	Two families of methods address this robustness gap.
8	\emph{Training-time methods}~\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.
9	\emph{Inference-time methods} leave the policy frozen and intervene at deployment.
10	ReconVLA~\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \emph{sample selection} strategy that cannot produce actions better than the best candidate.
11	SC-VLA~\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.
12	VLA-Pilot~\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\,s per control step.
13	A2C2~\cite{a2c2_2025} trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model.
14	In short, no existing inference-time method combines \emph{learned action correction} on a fully frozen VLA with \emph{offline-only training} and \emph{low latency}.
15	
16	% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?
17	The fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.
18	Learned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.
19	However, a critical open question is what information the correction module should be conditioned on.
20	An intuitive hypothesis is that \emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.
21	We test this hypothesis systematically.
22	
23	% Para 3: Our approach — ACR-VLA pipeline overview
24	We introduce \textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.
25	ACR-VLA operates as a \emph{sample-then-correct} pipeline:
26	(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;
27	(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\cite{braun2025cgs} and select the lowest-scoring candidate;
28	(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.
29	The corrected action is $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta}, \|\boldsymbol{\delta}\|_2 \leq \varepsilon)$, where the norm bound $\varepsilon$ constrains how far the correction can deviate from the selected action.
30	CRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.
31	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\cite{liu2023libero}.
32	
33	% Para 4: Key findings — what we find, including negatives
34	Our experiments yield three findings.
35	\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\% success versus 12.0\% for conformal selection alone, a +7.0\,pp improvement.
36	Three baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\%, indicating that neither averaging nor selection breaks through on this benchmark.
37	\emph{Second}, per-DOF conformal features as CRM conditioning are an \emph{honest negative result}: the perdof variant (11.0\%) performs comparably to argmin selection (12.0\%) and far below observation-only conditioning (19.0\%).
38	This contradicts the intuition that richer uncertainty features should yield better corrections.
39	We attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\cite{ross2011dagger}.
40	\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\|\boldsymbol{\delta}\|_2 \approx 1.42$), CRM achieves 0\% success---compounding error destroys the trajectory entirely.
41	Constraining $\varepsilon$ to $[0.05, 0.2]$ restores stable performance, with observation-conditioned CRM uniquely robust across this range while per-DOF-conditioned CRM collapses at larger bounds.
42	On LIBERO-Spatial (10 tasks with layout changes), all CRM variants achieve 30--35\%, comparable to the argmin baseline (34\%)---a null result that we report prominently.
43	Residual correction at the action level does not help when the challenge is spatial re-planning rather than fine-grained motor adjustment.
44	
45	% Para 5: Contributions
46	Our contributions are:
47	\begin{enumerate}[leftmargin=*,nosep]
48	  \item \textbf{A sample-then-correct pipeline for frozen VLAs.}
49	  We present the first method that combines multi-sample conformal selection with offline-trained learned residual correction on a frozen VLA.
50	  On LIBERO-Object, CRM correction improves success by +7.0\,pp over selection alone (19.0\% vs.\ 12.0\%), demonstrating that learned correction can synthesize actions better than any individual VLA sample.
51	
52	  \item \textbf{Honest negative: per-DOF conformal features do not improve correction.}
53	  Systematic ablation across three conditioning variants---observation embeddings (329K params), per-DOF conformal statistics (339K params), and scalar uncertainty (330K params)---reveals that observation features suffice for effective correction.
54	  Per-DOF conformal statistics, despite their theoretical appeal, yield 11.0\% versus 19.0\% for observation-only conditioning, challenging the intuition from synthetic experiments that richer uncertainty features enable better corrections.
55	
56	  \item \textbf{Correction magnitude control as a critical design factor.}
57	  We show that unbounded residual correction ($\|\boldsymbol{\delta}\|_2 \approx 1.42$) causes catastrophic 0\% success, while the safe operating range $\varepsilon \in [0.05, 0.2]$ yields stable improvements.
58	  Observation-conditioned CRM maintains performance across this range; per-DOF-conditioned CRM degrades sharply beyond $\varepsilon = 0.1$.
59	  This magnitude sensitivity has not been systematically characterized in prior residual policy literature.
60	\end{enumerate}
61	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "27b659a7-3006-432a-95e3-a7df6cccabcb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/introduction_scenarioC.tex",
      "content": "\\section{Introduction}\n\\label{sec:intro}\n\n% Para 1: Problem — VLAs degrade under distribution shift; existing solutions have trade-offs\nVision-language-action models (VLAs) that generate actions via flow matching~\\cite{black2024pi0,shukor2025smolvla} achieve 97--99\\% success on standard manipulation benchmarks such as LIBERO~\\cite{liu2023libero}.\nYet under the distribution shifts common in deployment---object appearance changes, lighting variation, sensor noise---performance degrades substantially~\\cite{fei2025liberoplus}.\nTwo families of methods address this robustness gap.\n\\emph{Training-time methods}~\\cite{robustvla2025,srpo2025,digflow2025} improve the base policy through robustness-aware objectives, but require retraining and remain bounded by the training distribution.\n\\emph{Inference-time methods} leave the policy frozen and intervene at deployment.\nReconVLA~\\cite{chen2026reconvla} draws multiple action samples and selects the best one via conformal scoring---a pure \\emph{sample selection} strategy that cannot produce actions better than the best candidate.\nSC-VLA~\\cite{sc_vla_2026} learns a residual correction via reinforcement learning, requiring per-task environment interaction.\nVLA-Pilot~\\cite{vla_pilot_2025} steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41\\,s per control step.\nA2C2~\\cite{a2c2_2025} trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model.\nIn short, no existing inference-time method combines \\emph{learned action correction} on a fully frozen VLA with \\emph{offline-only training} and \\emph{low latency}.\n\n% Para 2: Gap — sample selection is limited; learned correction can go beyond, but what conditioning?\nThe fundamental limitation of sample selection is that it is bounded by the quality of the available candidates: when all $K$ samples are poor, selecting the best one still yields a poor action.\nLearned correction can synthesize actions beyond the support of the original samples, potentially recovering from systematic biases in the base policy.\nHowever, a critical open question is what information the correction module should be conditioned on.\nAn intuitive hypothesis is that \\emph{structured uncertainty features}---per-degree-of-freedom conformal statistics capturing which action dimensions are uncertain and by how much---should enable more targeted corrections than raw observation features alone.\nWe test this hypothesis systematically.\n\n% Para 3: Our approach — ACR-VLA pipeline overview\nWe introduce \\textbf{ACR-VLA} (Adaptive Conformal Refinement for VLA), an inference-time module that wraps any frozen flow-matching VLA and performs learned residual action correction.\nACR-VLA operates as a \\emph{sample-then-correct} pipeline:\n(i)~draw $K{=}10$ action samples via independent flow-matching rollouts;\n(ii)~score each sample using Mahalanobis nonconformity under a Ledoit--Wolf shrinkage covariance~\\cite{braun2025cgs} and select the lowest-scoring candidate;\n(iii)~apply a lightweight Conformal Residual Module (CRM)---a 3-layer MLP (${\\sim}$329K parameters) that takes the frozen VLA's observation embedding as input and outputs a bounded residual correction.\nThe corrected action is $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta}, \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon)$, where the norm bound $\\varepsilon$ constrains how far the correction can deviate from the selected action.\nCRM is trained offline via $L_2$ regression on demonstration data; the base VLA is never modified.\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA, and evaluate on two LIBERO task suites~\\cite{liu2023libero}.\n\n% Para 4: Key findings — what we find, including negatives\nOur experiments yield three findings.\n\\emph{First}, sample-then-correct outperforms sample-then-select: on LIBERO-Object (10 tasks with novel object instances), observation-conditioned CRM achieves 19.0\\% success versus 12.0\\% for conformal selection alone, a +7.0\\,pp improvement.\nThree baselines---single-sample VLA, 10-sample mean, and argmin selection---all plateau at 12.0\\%, indicating that neither averaging nor selection breaks through on this benchmark.\n\\emph{Second}, per-DOF conformal features as CRM conditioning are an \\emph{honest negative result}: the perdof variant (11.0\\%) performs comparably to argmin selection (12.0\\%) and far below observation-only conditioning (19.0\\%).\nThis contradicts the intuition that richer uncertainty features should yield better corrections.\nWe attribute this to noisy covariance estimation at the $K{=}10$ sample budget ($d/K = 0.6$): while shrinkage stabilizes selection scoring, the per-DOF statistics derived from it carry estimation noise that degrades CRM predictions under the compounding distribution shift of closed-loop evaluation~\\cite{ross2011dagger}.\n\\emph{Third}, correction magnitude control is critical and has not been systematically studied in prior residual policy work~\\cite{silver2018residual,jiang2024transic,xiao2026pld}: without clipping ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$), CRM achieves 0\\% success---compounding error destroys the trajectory entirely.\nConstraining $\\varepsilon$ to $[0.05, 0.2]$ restores stable performance, with observation-conditioned CRM uniquely robust across this range while per-DOF-conditioned CRM collapses at larger bounds.\nOn LIBERO-Spatial (10 tasks with layout changes), all CRM variants achieve 30--35\\%, comparable to the argmin baseline (34\\%)---a null result that we report prominently.\nResidual correction at the action level does not help when the challenge is spatial re-planning rather than fine-grained motor adjustment.\n\n% Para 5: Contributions\nOur contributions are:\n\\begin{enumerate}[leftmargin=*,nosep]\n  \\item \\textbf{A sample-then-correct pipeline for frozen VLAs.}\n  We present the first method that combines multi-sample conformal selection with offline-trained learned residual correction on a frozen VLA.\n  On LIBERO-Object, CRM correction improves success by +7.0\\,pp over selection alone (19.0\\% vs.\\ 12.0\\%), demonstrating that learned correction can synthesize actions better than any individual VLA sample.\n\n  \\item \\textbf{Honest negative: per-DOF conformal features do not improve correction.}\n  Systematic ablation across three conditioning variants---observation embeddings (329K params), per-DOF conformal statistics (339K params), and scalar uncertainty (330K params)---reveals that observation features suffice for effective correction.\n  Per-DOF conformal statistics, despite their theoretical appeal, yield 11.0\\% versus 19.0\\% for observation-only conditioning, challenging the intuition from synthetic experiments that richer uncertainty features enable better corrections.\n\n  \\item \\textbf{Correction magnitude control as a critical design factor.}\n  We show that unbounded residual correction ($\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$) causes catastrophic 0\\% success, while the safe operating range $\\varepsilon \\in [0.05, 0.2]$ yields stable improvements.\n  Observation-conditioned CRM maintains performance across this range; per-DOF-conditioned CRM degrades sharply beyond $\\varepsilon = 0.1$.\n  This magnitude sensitivity has not been systematically characterized in prior residual policy literature.\n\\end{enumerate}\n",
      "numLines": 61,
      "startLine": 1,
      "totalLines": 61
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Read · `toolu_01YazBaasEjJaUfo35Rx8GmP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d17c97a2-239b-44b5-823f-7f1e6f885221",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YkrjP2wTNMnv97GBcFVwA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 23948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1683
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

_source line 17 · 2026-05-15T20:15:57.168Z_

<details><summary>↩ Tool result · `toolu_01YazBaasEjJaUfo35Rx8GmP`</summary>

```text
1	
2	\section{Method}
3	\label{sec:method}
4	
5	\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.
6	
7	\subsection{Problem Setup}
8	\label{sec:problem_setup}
9	
10	Let $\pi_\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\mathbb{R}^{d \times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.
11	
12	At each control step, $\pi_\theta$ can be queried multiple times via independent flow-matching rollouts~\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\pi_\theta$.
13	
14	\subsection{Multi-Sample Generation and Conformal Selection}
15	\label{sec:selection}
16	
17	\paragraph{Sampling and truncation.}
18	We draw $K{=}10$ action chunks from $\pi_\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\{a_h^{(k)}\}_{k=1}^K$ with $a_h^{(k)} \in \mathbb{R}^d$ for each horizon step $h = 1, \dots, H$.
19	
20	\paragraph{Shrinkage covariance estimation.}
21	For each horizon step $h$, we compute the sample mean $\boldsymbol{\mu}_h = \frac{1}{K}\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\cite{ledoit2004well}:
22	\begin{equation}
23	  \boldsymbol{\Sigma}_h = (1 - \alpha_{\mathrm{LW}})\,\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}} + \alpha_{\mathrm{LW}}\,\frac{\mathrm{tr}(\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}})}{d}\,\mathbf{I},
24	  \label{eq:shrinkage}
25	\end{equation}
26	where $\hat{\boldsymbol{\Sigma}}_{\mathrm{emp}}$ is the empirical covariance and $\alpha_{\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\% estimation error; shrinkage reduces this to below 5\%~\cite{ledoit2004well}.
27	
28	\paragraph{Mahalanobis nonconformity score.}
29	For each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:
30	\begin{equation}
31	  s_h(a) = (a - \boldsymbol{\mu}_h)^\top \boldsymbol{\Sigma}_h^{-1} (a - \boldsymbol{\mu}_h).
32	  \label{eq:mahal}
33	\end{equation}
34	This score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\cite{braun2025cgs}.
35	
36	\paragraph{Argmin selection.}
37	We select the sample with the lowest total nonconformity across all horizon steps:
38	\begin{equation}
39	  a_{\mathrm{base}} = \argmin_{k \in \{1,\dots,K\}} \sum_{h=1}^{H} s_h\bigl(a_h^{(k)}\bigr).
40	  \label{eq:argmin}
41	\end{equation}
42	This is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\mathrm{base}} \in \mathbb{R}^{d \times H}$ is the starting point for residual correction.
43	
44	\subsection{Conformal Residual Module}
45	\label{sec:crm}
46	
47	The Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.
48	
49	\paragraph{Architecture.}
50	CRM is a 3-layer MLP with input normalization (input$\to$256$\to$256$\to$30; 329K parameters for the primary obs\_only variant).
51	Its input is the frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\boldsymbol{\delta} \in \mathbb{R}^{d \times H} = \mathbb{R}^{30}$, and the corrected action is:
52	\begin{equation}
53	  \mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}\bigl(\boldsymbol{\delta},\; \|\boldsymbol{\delta}\|_2 \leq \varepsilon\bigr),
54	  \label{eq:crm}
55	\end{equation}
56	where $\varepsilon$ is a norm bound hyperparameter (Section~\ref{sec:magnitude}).
57	
58	\paragraph{Observation-only conditioning.}
59	CRM receives only the observation embedding $\mathbf{z}_{\mathrm{obs}}$ and does \emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.
60	
61	\paragraph{Training.}
62	CRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\cite{liu2023libero}:
63	\begin{equation}
64	  \mathcal{L} = \bigl\|\mathbf{a}^* - \mathbf{a}_{\mathrm{expert}}\bigr\|_2^2.
65	  \label{eq:loss}
66	\end{equation}
67	The training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\ref{eq:argmin}) to obtain $a_{\mathrm{base}}$. The expert action $\mathbf{a}_{\mathrm{expert}}$ is the corresponding demonstration action.
68	
69	We apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\sigma \approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\cite{ross2011dagger}.
70	
71	\paragraph{Base VLA.}
72	We instantiate ACR-VLA on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.
73	
74	\subsection{Magnitude Control}
75	\label{sec:magnitude}
76	
77	The norm bound $\varepsilon$ in~(\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.
78	
79	\paragraph{Unbounded correction fails catastrophically.}
80	Without clipping, the natural CRM output has $\|\boldsymbol{\delta}\|_2 \approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.
81	
82	\paragraph{Small corrections are effective.}
83	Constraining $\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.
84	
85	\paragraph{Connection to residual policy learning.}
86	The necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.
87	
88	\paragraph{Differential sensitivity across CRM variants.}
89	Observation-conditioned CRM (obs\_only) maintains 35--36\% success on LIBERO-Spatial across the full range $\varepsilon \in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\% at $\varepsilon = 0.1$ to 26\% at $\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\ref{sec:ablation}).
90	
91	\subsection{Inference Protocol}
92	\label{sec:inference_protocol}
93	
94	Each control step proceeds as follows:
95	\begin{enumerate}[nosep]
96	  \item Draw $K{=}10$ action chunks from the frozen VLA $\pi_\theta$ and truncate to $H{=}5$ steps.
97	  \item Compute shrinkage covariance $\boldsymbol{\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.
98	  \item Select $a_{\mathrm{base}}$ via argmin over total nonconformity~(\ref{eq:argmin}).
99	  \item Compute residual $\boldsymbol{\delta} = \mathrm{CRM}(\mathbf{z}_{\mathrm{obs}})$ and clip to $\|\boldsymbol{\delta}\|_2 \leq \varepsilon$.
100	  \item Execute the first action of $\mathbf{a}^* = a_{\mathrm{base}} + \mathrm{clip}(\boldsymbol{\delta})$.
101	  \item Observe new state and re-plan from step~1.
102	\end{enumerate}
103	The computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\cite{chen2026reconvla}) plus ${\sim}$3\,ms for CRM inference. The base VLA is never modified.
104	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "99e7597d-aa80-42f3-8aae-f031a79c9fa9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/method.tex",
      "content": "\n\\section{Method}\n\\label{sec:method}\n\n\\textbf{ACR-VLA} improves the actions of a frozen flow-matching VLA at inference time through a sample-then-correct pipeline (Figure~\\ref{fig:pipeline}): draw $K$ action samples, select the best candidate via conformalized scoring, then apply a learned residual correction bounded in magnitude. The base VLA is never retrained.\n\n\\subsection{Problem Setup}\n\\label{sec:problem_setup}\n\nLet $\\pi_\\theta$ be a frozen flow-matching VLA that, given an observation $o_t$ (image + language instruction + proprioceptive state), generates action chunks of length $C{=}50$ in $\\mathbb{R}^{d \\times C}$ with $d{=}6$ (3 translation + 3 rotation). Under receding-horizon execution, only the first $H{=}5$ steps of each chunk influence the robot before re-planning, so we discard the remainder. The gripper dimension is handled separately via direct thresholding and is excluded from the conformal pipeline.\n\nAt each control step, $\\pi_\\theta$ can be queried multiple times via independent flow-matching rollouts~\\cite{lipman2023flow}, yielding $K$ candidate action chunks. Our goal is to exploit these $K$ samples to produce a single action that is more accurate than any individual sample or their aggregate statistics, without modifying $\\pi_\\theta$.\n\n\\subsection{Multi-Sample Generation and Conformal Selection}\n\\label{sec:selection}\n\n\\paragraph{Sampling and truncation.}\nWe draw $K{=}10$ action chunks from $\\pi_\\theta$ via independent flow-matching rollouts. Each chunk is truncated to the first $H{=}5$ steps, yielding samples $\\{a_h^{(k)}\\}_{k=1}^K$ with $a_h^{(k)} \\in \\mathbb{R}^d$ for each horizon step $h = 1, \\dots, H$.\n\n\\paragraph{Shrinkage covariance estimation.}\nFor each horizon step $h$, we compute the sample mean $\\boldsymbol{\\mu}_h = \\frac{1}{K}\\sum_{k=1}^K a_h^{(k)}$ and the Ledoit--Wolf shrinkage covariance~\\cite{ledoit2004well}:\n\\begin{equation}\n  \\boldsymbol{\\Sigma}_h = (1 - \\alpha_{\\mathrm{LW}})\\,\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}} + \\alpha_{\\mathrm{LW}}\\,\\frac{\\mathrm{tr}(\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}})}{d}\\,\\mathbf{I},\n  \\label{eq:shrinkage}\n\\end{equation}\nwhere $\\hat{\\boldsymbol{\\Sigma}}_{\\mathrm{emp}}$ is the empirical covariance and $\\alpha_{\\mathrm{LW}}$ is the analytically optimal shrinkage intensity. With dimension-to-sample ratio $d/K = 0.6$, the eigenvalues of the raw sample covariance suffer 30--40\\% estimation error; shrinkage reduces this to below 5\\%~\\cite{ledoit2004well}.\n\n\\paragraph{Mahalanobis nonconformity score.}\nFor each sample $a_h^{(k)}$ at horizon step $h$, we compute the Mahalanobis nonconformity score:\n\\begin{equation}\n  s_h(a) = (a - \\boldsymbol{\\mu}_h)^\\top \\boldsymbol{\\Sigma}_h^{-1} (a - \\boldsymbol{\\mu}_h).\n  \\label{eq:mahal}\n\\end{equation}\nThis score captures cross-DOF covariance structure: a sample that deviates along the principal axis of variation receives a lower score than one that deviates along a tightly concentrated direction~\\cite{braun2025cgs}.\n\n\\paragraph{Argmin selection.}\nWe select the sample with the lowest total nonconformity across all horizon steps:\n\\begin{equation}\n  a_{\\mathrm{base}} = \\argmin_{k \\in \\{1,\\dots,K\\}} \\sum_{h=1}^{H} s_h\\bigl(a_h^{(k)}\\bigr).\n  \\label{eq:argmin}\n\\end{equation}\nThis is a simplified selection baseline inspired by the conformal selection frontend of ReconVLA~\\cite{chen2026reconvla}, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring to isolate the effect of the downstream correction module. The selected $a_{\\mathrm{base}} \\in \\mathbb{R}^{d \\times H}$ is the starting point for residual correction.\n\n\\subsection{Conformal Residual Module}\n\\label{sec:crm}\n\nThe Conformal Residual Module (CRM) is a lightweight MLP that refines the selected action $a_{\\mathrm{base}}$ by predicting a small residual correction conditioned on the current observation.\n\n\\paragraph{Architecture.}\nCRM is a 3-layer MLP with input normalization (input$\\to$256$\\to$256$\\to$30; 329K parameters for the primary obs\\_only variant).\nIts input is the frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ extracted from the base VLA's vision-language encoder. The output is a residual $\\boldsymbol{\\delta} \\in \\mathbb{R}^{d \\times H} = \\mathbb{R}^{30}$, and the corrected action is:\n\\begin{equation}\n  \\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}\\bigl(\\boldsymbol{\\delta},\\; \\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon\\bigr),\n  \\label{eq:crm}\n\\end{equation}\nwhere $\\varepsilon$ is a norm bound hyperparameter (Section~\\ref{sec:magnitude}).\n\n\\paragraph{Observation-only conditioning.}\nCRM receives only the observation embedding $\\mathbf{z}_{\\mathrm{obs}}$ and does \\emph{not} receive per-DOF conformal statistics, uncertainty features, or any CGS-derived quantities as input. This is a deliberate design choice validated by ablation (Section~\\ref{sec:ablation}): observation features already encode sufficient task-relevant information---object identity, spatial layout, gripper-object relationship---for predicting corrective residuals. Per-DOF conformal statistics, while intuitively richer, add noise at the $K{=}10$ sample budget where covariance estimation is inherently noisy ($d/K = 0.6$). In Section~\\ref{sec:ablation}, we compare against CRM variants conditioned on per-DOF conformal features (input dim 1{,}030; 339K params) and scalar uncertainty (input dim 993; 330K params), and find that observation-only conditioning is uniquely effective.\n\n\\paragraph{Training.}\nCRM is trained offline with an $L_2$ loss on demonstration trajectories from LIBERO~\\cite{liu2023libero}:\n\\begin{equation}\n  \\mathcal{L} = \\bigl\\|\\mathbf{a}^* - \\mathbf{a}_{\\mathrm{expert}}\\bigr\\|_2^2.\n  \\label{eq:loss}\n\\end{equation}\nThe training data comprises 26{,}737 precomputed samples derived from 10 demonstrations per task across 20 LIBERO tasks. For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA~\\cite{shukor2025smolvla}, compute the CGS scores, and apply argmin selection (\\ref{eq:argmin}) to obtain $a_{\\mathrm{base}}$. The expert action $\\mathbf{a}_{\\mathrm{expert}}$ is the corresponding demonstration action.\n\nWe apply two forms of data augmentation during training: (i)~additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and (ii)~noise on the uncertainty features ($\\sigma \\approx 0.006$). Both augmentations improve generalization to the distribution of actions encountered during closed-loop evaluation, where compounding errors cause the state distribution to diverge from the demonstration distribution~\\cite{ross2011dagger}.\n\n\\paragraph{Base VLA.}\nWe instantiate ACR-VLA on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA. SmolVLA generates actions via learned flow matching~\\cite{lipman2023flow}, producing stochastic samples that naturally support multi-sample inference. The method is architecture-agnostic and applies to any flow-matching VLA that supports repeated sampling.\n\n\\subsection{Magnitude Control}\n\\label{sec:magnitude}\n\nThe norm bound $\\varepsilon$ in~(\\ref{eq:crm}) is critical: it determines how much the CRM can deviate from the conformal-selected action.\n\n\\paragraph{Unbounded correction fails catastrophically.}\nWithout clipping, the natural CRM output has $\\|\\boldsymbol{\\delta}\\|_2 \\approx 1.42$. At this magnitude, the corrected action deviates so far from the base VLA's output that compounding error across the trajectory destroys task performance entirely---yielding 0\\% success on LIBERO-Object. This failure mode is analogous to the compounding error problem in imitation learning~\\cite{ross2011dagger}, but manifests at inference time: each over-corrected action shifts the state distribution further from the regime where the CRM was trained, amplifying subsequent correction errors.\n\n\\paragraph{Small corrections are effective.}\nConstraining $\\varepsilon$ to the range $[0.05, 0.2]$ yields stable, beneficial corrections. We use $\\varepsilon = 0.1$ as the default. At this magnitude, the CRM applies corrections small enough to remain within the basin of attraction of the base policy's behavior, while large enough to shift actions toward the expert demonstrations.\n\n\\paragraph{Connection to residual policy learning.}\nThe necessity of magnitude control connects ACR-VLA to the broader residual policy literature. Silver et al.~\\cite{silver2018residual} introduced bounded residual corrections for combining learned and classical controllers. TRANSIC~\\cite{jiang2024transic} uses learned binary gating to selectively apply residual actions across different task phases. PLD~\\cite{xiao2026pld} schedules magnitude bounds during training. ACR-VLA's approach---fixed $L_2$ norm clipping of the CRM output---is the simplest instantiation: no learned gating, no scheduling, just a hard constraint that prevents the correction from overwhelming the base policy.\n\n\\paragraph{Differential sensitivity across CRM variants.}\nObservation-conditioned CRM (obs\\_only) maintains 35--36\\% success on LIBERO-Spatial across the full range $\\varepsilon \\in [0.05, 0.3]$, while per-DOF-conditioned CRM collapses from 35\\% at $\\varepsilon = 0.1$ to 26\\% at $\\varepsilon = 0.3$. This robustness gap provides further evidence that observation features yield more stable conditioning than per-DOF conformal statistics at the $K{=}10$ sample budget (Section~\\ref{sec:ablation}).\n\n\\subsection{Inference Protocol}\n\\label{sec:inference_protocol}\n\nEach control step proceeds as follows:\n\\begin{enumerate}[nosep]\n  \\item Draw $K{=}10$ action chunks from the frozen VLA $\\pi_\\theta$ and truncate to $H{=}5$ steps.\n  \\item Compute shrinkage covariance $\\boldsymbol{\\Sigma}_h$ and Mahalanobis scores $s_h$ for each sample.\n  \\item Select $a_{\\mathrm{base}}$ via argmin over total nonconformity~(\\ref{eq:argmin}).\n  \\item Compute residual $\\boldsymbol{\\delta} = \\mathrm{CRM}(\\mathbf{z}_{\\mathrm{obs}})$ and clip to $\\|\\boldsymbol{\\delta}\\|_2 \\leq \\varepsilon$.\n  \\item Execute the first action of $\\mathbf{a}^* = a_{\\mathrm{base}} + \\mathrm{clip}(\\boldsymbol{\\delta})$.\n  \\item Observe new state and re-plan from step~1.\n\\end{enumerate}\nThe computational overhead consists of $K{=}10$ extra forward passes through the base VLA (shared with any multi-sample selection method such as ReconVLA~\\cite{chen2026reconvla}) plus ${\\sim}$3\\,ms for CRM inference. The base VLA is never modified.\n",
      "numLines": 104,
      "startLine": 1,
      "totalLines": 104
    }
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Read · `toolu_011KFCivBijeSpAm7KdD4HCg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7e956df2-6ef9-472c-a34e-2956839f5ee9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YkrjP2wTNMnv97GBcFVwA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 23948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1683
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

_source line 19 · 2026-05-15T20:15:57.620Z_

<details><summary>↩ Tool result · `toolu_011KFCivBijeSpAm7KdD4HCg`</summary>

```text
1	
2	\section{Experiments}
3	\label{sec:experiments}
4	
5	We evaluate ACR-VLA on two LIBERO task suites to answer three questions:
6	(i)~Does observation-conditioned residual correction improve over conformal selection alone?
7	(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?
8	(iii)~How sensitive is performance to the magnitude bound $\varepsilon$?
9	The answers are: yes (+7.0\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\_only is robust across a wide range.
10	
11	\subsection{Experimental Setup}
12	\label{sec:exp_setup}
13	
14	\paragraph{Benchmarks.}
15	We use two suites from the LIBERO benchmark~\cite{liu2023libero}:
16	\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).
17	Each task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.
18	
19	\paragraph{Base VLA.}
20	We build on SmolVLA~\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.
21	We use the checkpoint \texttt{lerobot/smolvla\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\times}256$) and 8D proprioceptive state.
22	Actions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.
23	
24	\paragraph{Baselines.}
25	All methods use the same frozen SmolVLA checkpoint:
26	\begin{itemize}[nosep]
27	  \item \textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.
28	  \item \textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.
29	  \item \textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\ref{sec:selection}), no CRM correction.
30	\end{itemize}
31	
32	\paragraph{CRM variants.}
33	All CRM variants share the same 3-layer MLP architecture (input$\to$256$\to$256$\to$30) and differ only in their conditioning input:
34	\begin{itemize}[nosep]
35	  \item \textbf{obs\_only}: frozen observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ (329K params). This is our primary method.
36	  \item \textbf{perdof}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).
37	  \item \textbf{scalar}: $\mathbf{z}_{\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).
38	\end{itemize}
39	
40	\paragraph{Training.}
41	CRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.
42	For each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\mathrm{base}}$.
43	Optimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.
44	Data augmentation includes additive Gaussian noise on the mean-action vector ($\sigma \in [0.02, 0.1]$) and uncertainty features ($\sigma \approx 0.006$).
45	The default magnitude bound is $\varepsilon = 0.1$ for all CRM variants unless stated otherwise.
46	
47	\paragraph{Statistical protocol.}
48	We report success rates from seed 42 (10 rollouts $\times$ 10 tasks = 100 episodes per suite).
49	Fisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\textsc{pending}: seed43].
50	Until then, we report absolute differences descriptively without claiming statistical significance.
51	
52	
53	\subsection{Main Results}
54	\label{sec:main_results}
55	
56	Table~\ref{tab:main} compares all methods on both benchmarks.
57	
58	\begin{table}[t]
59	\centering
60	\caption{Task success rate (\%\,$\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\times$ 10 rollouts each, seed 42). $\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}
61	\label{tab:main}
62	\small
63	\begin{tabular}{lccc}
64	\toprule
65	Method & Object (\%) & Spatial (\%) & $\Delta$ Object \\
66	\midrule
67	VLA-only ($K{=}1$)    & 12.0 & 30.0 & $\phantom{+}0.0$ \\
68	VLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\phantom{+}0.0$ \\
69	Argmin ($K{=}10$)      & 12.0 & 34.0 & --- \\
70	\midrule
71	scalar ($\varepsilon{=}0.1$)  & \phantom{0}9.0 & 32.0 & $-3.0$ \\
72	perdof ($\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\
73	\textbf{obs\_only} ($\varepsilon{=}0.1$) & \textbf{19.0} & \textbf{35.0} & $\mathbf{+7.0}$ \\
74	\midrule
75	obs\_only ($\varepsilon{=}0.2$) & \textbf{22.0} & 35.0 & $+10.0$ \\
76	\bottomrule
77	\end{tabular}
78	\end{table}
79	
80	\paragraph{Object benchmark: correction helps.}
81	On LIBERO-Object, obs\_only at $\varepsilon{=}0.1$ achieves 19.0\%, a +7.0\,pp improvement over the Argmin baseline (12.0\%).
82	Increasing the magnitude bound to $\varepsilon{=}0.2$ yields 22.0\% (+10.0\,pp).
83	This is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.
84	
85	Three baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.
86	On LIBERO-Spatial, by contrast, Argmin improves +4\,pp over VLA-only (34\% vs.\ 30\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.
87	The obs\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.
88	
89	\paragraph{Spatial benchmark: correction does not help.}
90	On LIBERO-Spatial, all methods cluster within a 5\,pp band (30--35\%).
91	The best CRM variants (obs\_only, perdof) achieve 35\%, only 1\,pp above the Argmin baseline (34\%).
92	This is a null result that we report prominently.
93	
94	We interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.
95	The VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.
96	Residual correction at the action level is the wrong granularity for this type of generalization.
97	
98	\paragraph{Key finding.}
99	Sample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.
100	For spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.
101	
102	
103	\subsection{CRM Conditioning Ablation}
104	\label{sec:ablation}
105	
106	We focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\ref{tab:main}).
107	
108	\paragraph{Ranking.}
109	obs\_only (19.0\%) $\gg$ Argmin (12.0\%) $\approx$ perdof (11.0\%) $>$ scalar (9.0\%).
110	
111	This ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \emph{hurt} rather than help.
112	Scalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\,pp below the Argmin baseline that uses no correction at all.
113	
114	\paragraph{Why does richer conditioning fail?}
115	We identify three factors:
116	
117	\emph{(1) Noisy covariance estimation.}
118	With $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.
119	While Ledoit--Wolf shrinkage~\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.
120	Feeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).
121	
122	\emph{(2) Observation features are sufficient.}
123	The frozen VLA observation embedding $\mathbf{z}_{\mathrm{obs}} \in \mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.
124	This information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.
125	The CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.
126	
127	\emph{(3) Per-step MSE $\neq$ episode success.}
128	In offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.
129	However, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\cite{ross2011dagger}.
130	The additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.
131	
132	\paragraph{Connection to magnitude sensitivity.}
133	The obs\_only variant is also more robust across magnitude bounds $\varepsilon$ than perdof (Section~\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.
134	
135	
136	\subsection{Magnitude Sensitivity}
137	\label{sec:magnitude_results}
138	
139	The norm bound $\varepsilon$ determines how much CRM can deviate from the conformal-selected action.
140	Figure~\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\varepsilon \in [0.05, 1.42]$.
141	
142	\begin{figure}[t]
143	\centering
144	% \includegraphics[width=\linewidth]{figures/magnitude_sweep.pdf}
145	\fbox{\parbox{0.9\linewidth}{\centering\vspace{2em}[Placeholder: Magnitude sweep --- obs\_only vs.\ perdof vs.\ Argmin reference]\vspace{2em}}}
146	\caption{Success rate (\%) on LIBERO-Spatial as a function of magnitude bound $\varepsilon$. obs\_only (solid blue) maintains 35--36\% across $\varepsilon \in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\varepsilon$. The Argmin baseline (dotted gray, 34\%) is independent of $\varepsilon$. Without magnitude control ($\varepsilon{\approx}1.42$), perdof achieves 0\% on spatial.}
147	\label{fig:magnitude}
148	\end{figure}
149	
150	\begin{table}[t]
151	\centering
152	\caption{Success rate (\%) on LIBERO-Spatial across magnitude bounds $\varepsilon$. The Argmin baseline (34\%, no correction) is independent of $\varepsilon$.}
153	\label{tab:magnitude}
154	\small
155	\begin{tabular}{lcccc}
156	\toprule
157	$\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\
158	\midrule
159	obs\_only & 35.0 & 35.0 & 36.0 & --- \\
160	perdof    & 31.0 & 35.0 & 26.0 & 0.0 \\
161	\midrule
162	Argmin (ref.) & \multicolumn{4}{c}{34.0 (flat, no correction)} \\
163	\bottomrule
164	\end{tabular}
165	\end{table}
166	
167	\paragraph{obs\_only is robust.}
168	The obs\_only variant maintains 35--36\% across the full range $\varepsilon \in [0.05, 0.3]$---a remarkably flat profile.
169	This stability means the practitioner need not carefully tune $\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.
170	
171	\paragraph{perdof is fragile.}
172	In contrast, perdof peaks at 35\% when $\varepsilon{=}0.1$ but collapses to 26\% at $\varepsilon{=}0.3$---a 9\,pp drop.
173	This fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.
174	At $\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.
175	
176	\paragraph{Unbounded correction is catastrophic.}
177	Without magnitude control ($\varepsilon{\approx}1.42$, the natural CRM output norm), perdof achieves 0\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\ref{sec:magnitude}).
178	The Argmin baseline (34\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.
179	The obs\_only variant was not evaluated at $\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.
180	
181	\paragraph{Practical recommendation.}
182	The safe operating range is $\varepsilon \in [0.05, 0.2]$.
183	Within this range, obs\_only is the only variant that consistently matches or exceeds the Argmin baseline.
184	We use $\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.
185	
186	
187	\subsection{Per-Task Analysis}
188	\label{sec:per_task}
189	
190	Per-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.
191	
192	[\textsc{pending}: seed43] --- A per-task heatmap comparing obs\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.
193	We expect the analysis to show that obs\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.
194	Task difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).
195	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d2a76544-aeff-4db2-920a-1ac0b81aa2bd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/experiments.tex",
      "content": "\n\\section{Experiments}\n\\label{sec:experiments}\n\nWe evaluate ACR-VLA on two LIBERO task suites to answer three questions:\n(i)~Does observation-conditioned residual correction improve over conformal selection alone?\n(ii)~Do per-DOF conformal features provide additional benefit beyond observation conditioning?\n(iii)~How sensitive is performance to the magnitude bound $\\varepsilon$?\nThe answers are: yes (+7.0\\,pp on object manipulation), no (honest negative), and critically---unbounded correction is catastrophic, but obs\\_only is robust across a wide range.\n\n\\subsection{Experimental Setup}\n\\label{sec:exp_setup}\n\n\\paragraph{Benchmarks.}\nWe use two suites from the LIBERO benchmark~\\cite{liu2023libero}:\n\\textbf{LIBERO-Spatial} (10 tasks requiring spatial reasoning about object layout) and \\textbf{LIBERO-Object} (10 tasks requiring generalization across novel object instances).\nEach task is evaluated over 10 rollouts with a maximum episode length of 300 steps, yielding 100 episodes per suite. Success is binary: an episode succeeds if the task predicate is satisfied before the step limit.\n\n\\paragraph{Base VLA.}\nWe build on SmolVLA~\\cite{shukor2025smolvla}, a 450M-parameter flow-matching VLA.\nWe use the checkpoint \\texttt{lerobot/smolvla\\_libero}, which receives dual-camera RGB input (agentview + eye-in-hand, $256{\\times}256$) and 8D proprioceptive state.\nActions are 7D: 6D end-effector pose (3 translation + 3 rotation) plus 1D gripper, with the gripper dimension handled outside the conformal pipeline via direct thresholding.\n\n\\paragraph{Baselines.}\nAll methods use the same frozen SmolVLA checkpoint:\n\\begin{itemize}[nosep]\n  \\item \\textbf{VLA-only} ($K{=}1$): single sample from the frozen VLA, no selection or correction.\n  \\item \\textbf{VLA-mean} ($K{=}10$): mean of 10 independent flow-matching samples, no selection or correction.\n  \\item \\textbf{Argmin} ($K{=}10$): conformal selection via Mahalanobis scoring (Section~\\ref{sec:selection}), no CRM correction.\n\\end{itemize}\n\n\\paragraph{CRM variants.}\nAll CRM variants share the same 3-layer MLP architecture (input$\\to$256$\\to$256$\\to$30) and differ only in their conditioning input:\n\\begin{itemize}[nosep]\n  \\item \\textbf{obs\\_only}: frozen observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ (329K params). This is our primary method.\n  \\item \\textbf{perdof}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 40D per-DOF conformal features (per-DOF standard deviations, conformal radii, log-volume; 339K params).\n  \\item \\textbf{scalar}: $\\mathbf{z}_{\\mathrm{obs}}$ concatenated with 3D scalar uncertainty summary (mean, max, min standard deviation; 330K params).\n\\end{itemize}\n\n\\paragraph{Training.}\nCRM is trained on 26{,}737 precomputed samples derived from 10 demonstrations per task across all 20 LIBERO tasks.\nFor each demonstration step, we run $K{=}10$ forward passes through the frozen SmolVLA, compute CGS scores, and apply argmin selection to obtain $a_{\\mathrm{base}}$.\nOptimization uses Adam with learning rate $10^{-3}$, batch size 32, for 50 epochs with seed 42.\nData augmentation includes additive Gaussian noise on the mean-action vector ($\\sigma \\in [0.02, 0.1]$) and uncertainty features ($\\sigma \\approx 0.006$).\nThe default magnitude bound is $\\varepsilon = 0.1$ for all CRM variants unless stated otherwise.\n\n\\paragraph{Statistical protocol.}\nWe report success rates from seed 42 (10 rollouts $\\times$ 10 tasks = 100 episodes per suite).\nFisher's exact test and bootstrap confidence intervals will be computed pending seed 43 replication [\\textsc{pending}: seed43].\nUntil then, we report absolute differences descriptively without claiming statistical significance.\n\n\n\\subsection{Main Results}\n\\label{sec:main_results}\n\nTable~\\ref{tab:main} compares all methods on both benchmarks.\n\n\\begin{table}[t]\n\\centering\n\\caption{Task success rate (\\%\\,$\\uparrow$) on LIBERO-Object and LIBERO-Spatial (10 tasks $\\times$ 10 rollouts each, seed 42). $\\Delta$ denotes improvement over the Argmin selection baseline. All methods use the same frozen SmolVLA checkpoint.}\n\\label{tab:main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nMethod & Object (\\%) & Spatial (\\%) & $\\Delta$ Object \\\\\n\\midrule\nVLA-only ($K{=}1$)    & 12.0 & 30.0 & $\\phantom{+}0.0$ \\\\\nVLA-mean ($K{=}10$)   & 12.0 & 32.0 & $\\phantom{+}0.0$ \\\\\nArgmin ($K{=}10$)      & 12.0 & 34.0 & --- \\\\\n\\midrule\nscalar ($\\varepsilon{=}0.1$)  & \\phantom{0}9.0 & 32.0 & $-3.0$ \\\\\nperdof ($\\varepsilon{=}0.1$)  & 11.0 & 35.0 & $-1.0$ \\\\\n\\textbf{obs\\_only} ($\\varepsilon{=}0.1$) & \\textbf{19.0} & \\textbf{35.0} & $\\mathbf{+7.0}$ \\\\\n\\midrule\nobs\\_only ($\\varepsilon{=}0.2$) & \\textbf{22.0} & 35.0 & $+10.0$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Object benchmark: correction helps.}\nOn LIBERO-Object, obs\\_only at $\\varepsilon{=}0.1$ achieves 19.0\\%, a +7.0\\,pp improvement over the Argmin baseline (12.0\\%).\nIncreasing the magnitude bound to $\\varepsilon{=}0.2$ yields 22.0\\% (+10.0\\,pp).\nThis is the core result: observation-conditioned residual correction recovers performance that conformal selection alone cannot.\n\nThree baselines---VLA-only, VLA-mean, and Argmin---all achieve 12.0\\% on LIBERO-Object, indicating that neither multi-sample averaging nor Mahalanobis-based selection provides meaningful benefit on this benchmark.\nOn LIBERO-Spatial, by contrast, Argmin improves +4\\,pp over VLA-only (34\\% vs.\\ 30\\%), suggesting that object perturbations shift the action distribution more uniformly across samples, limiting the value of selection alone.\nThe obs\\_only CRM breaks through this plateau by synthesizing corrections beyond the support of the original samples, conditioned on the observation embedding.\n\n\\paragraph{Spatial benchmark: correction does not help.}\nOn LIBERO-Spatial, all methods cluster within a 5\\,pp band (30--35\\%).\nThe best CRM variants (obs\\_only, perdof) achieve 35\\%, only 1\\,pp above the Argmin baseline (34\\%).\nThis is a null result that we report prominently.\n\nWe interpret this as follows: spatial perturbations in LIBERO-Spatial involve changes to object layout (e.g., moving target locations), which may require re-planning rather than local action correction.\nThe VLA's observation encoder cannot extract correctable error signals from spatial shifts---the problem is not that actions are inaccurate given the current state, but that the task structure itself has changed.\nResidual correction at the action level is the wrong granularity for this type of generalization.\n\n\\paragraph{Key finding.}\nSample-then-correct outperforms sample-then-select for object manipulation, where the challenge is fine-grained motor control with novel objects.\nFor spatial reasoning, where the challenge is planning under layout changes, correction at the action level provides no benefit over selection alone.\n\n\n\\subsection{CRM Conditioning Ablation}\n\\label{sec:ablation}\n\nWe focus the conditioning ablation on LIBERO-Object, where meaningful differences emerge (Table~\\ref{tab:main}).\n\n\\paragraph{Ranking.}\nobs\\_only (19.0\\%) $\\gg$ Argmin (12.0\\%) $\\approx$ perdof (11.0\\%) $>$ scalar (9.0\\%).\n\nThis ordering is the central negative result of our ablation: per-DOF conformal features, despite being intuitively richer (40 additional dimensions capturing per-DOF standard deviations, conformal radii, and log-volume terms), \\emph{hurt} rather than help.\nScalar uncertainty conditioning (3 additional dimensions) performs even worse, falling 3.0\\,pp below the Argmin baseline that uses no correction at all.\n\n\\paragraph{Why does richer conditioning fail?}\nWe identify three factors:\n\n\\emph{(1) Noisy covariance estimation.}\nWith $K{=}10$ samples in $d{=}6$ dimensions, the dimension-to-sample ratio is $d/K = 0.6$.\nWhile Ledoit--Wolf shrinkage~\\cite{ledoit2004well} stabilizes the covariance estimate for selection (Section~\\ref{sec:selection}), the per-DOF features derived from this estimate---standard deviations, conformal radii---still carry substantial estimation noise.\nFeeding these noisy features as CRM input introduces a distribution shift between training data (where noise patterns are consistent) and closed-loop evaluation (where compounding state-distribution drift produces different noise patterns).\n\n\\emph{(2) Observation features are sufficient.}\nThe frozen VLA observation embedding $\\mathbf{z}_{\\mathrm{obs}} \\in \\mathbb{R}^{990}$ already encodes task-relevant geometric information: object identity, spatial layout, gripper-object relationship, and task progress.\nThis information subsumes what the per-DOF conformal features attempt to capture---namely, which action dimensions are uncertain given the current scene.\nThe CRM learns to map directly from scene understanding to corrective residuals, without the intermediate conformal statistics.\n\n\\emph{(3) Per-step MSE $\\neq$ episode success.}\nIn offline evaluation, per-DOF conformal features reduce the per-step mean squared error between corrected actions and expert demonstrations.\nHowever, this per-step improvement does not translate to higher episode success rates in closed-loop evaluation, where small per-step errors compound and the robot visits states far from the demonstration distribution~\\cite{ross2011dagger}.\nThe additional noise from conformal features may cause occasional large corrections that, while reducing average MSE, lead to catastrophic failures in individual episodes.\n\n\\paragraph{Connection to magnitude sensitivity.}\nThe obs\\_only variant is also more robust across magnitude bounds $\\varepsilon$ than perdof (Section~\\ref{sec:magnitude_results}), providing further evidence that observation-only conditioning yields a more stable correction signal.\n\n\n\\subsection{Magnitude Sensitivity}\n\\label{sec:magnitude_results}\n\nThe norm bound $\\varepsilon$ determines how much CRM can deviate from the conformal-selected action.\nFigure~\\ref{fig:magnitude} shows performance on LIBERO-Spatial across $\\varepsilon \\in [0.05, 1.42]$.\n\n\\begin{figure}[t]\n\\centering\n% \\includegraphics[width=\\linewidth]{figures/magnitude_sweep.pdf}\n\\fbox{\\parbox{0.9\\linewidth}{\\centering\\vspace{2em}[Placeholder: Magnitude sweep --- obs\\_only vs.\\ perdof vs.\\ Argmin reference]\\vspace{2em}}}\n\\caption{Success rate (\\%) on LIBERO-Spatial as a function of magnitude bound $\\varepsilon$. obs\\_only (solid blue) maintains 35--36\\% across $\\varepsilon \\in [0.05, 0.3]$. perdof (dashed orange) collapses at larger $\\varepsilon$. The Argmin baseline (dotted gray, 34\\%) is independent of $\\varepsilon$. Without magnitude control ($\\varepsilon{\\approx}1.42$), perdof achieves 0\\% on spatial.}\n\\label{fig:magnitude}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\caption{Success rate (\\%) on LIBERO-Spatial across magnitude bounds $\\varepsilon$. The Argmin baseline (34\\%, no correction) is independent of $\\varepsilon$.}\n\\label{tab:magnitude}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\n$\\varepsilon$ & 0.05 & 0.1 & 0.3 & 1.42 \\\\\n\\midrule\nobs\\_only & 35.0 & 35.0 & 36.0 & --- \\\\\nperdof    & 31.0 & 35.0 & 26.0 & 0.0 \\\\\n\\midrule\nArgmin (ref.) & \\multicolumn{4}{c}{34.0 (flat, no correction)} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{obs\\_only is robust.}\nThe obs\\_only variant maintains 35--36\\% across the full range $\\varepsilon \\in [0.05, 0.3]$---a remarkably flat profile.\nThis stability means the practitioner need not carefully tune $\\varepsilon$; any value in $[0.05, 0.2]$ yields near-identical performance.\n\n\\paragraph{perdof is fragile.}\nIn contrast, perdof peaks at 35\\% when $\\varepsilon{=}0.1$ but collapses to 26\\% at $\\varepsilon{=}0.3$---a 9\\,pp drop.\nThis fragility suggests that the noisy conformal features cause the CRM to predict unreliable correction directions; when the magnitude bound is loose enough to accommodate these directions, performance degrades.\nAt $\\varepsilon{=}0.1$, the tight bound masks the problem by clipping erroneous corrections.\n\n\\paragraph{Unbounded correction is catastrophic.}\nWithout magnitude control ($\\varepsilon{\\approx}1.42$, the natural CRM output norm), perdof achieves 0\\% on LIBERO-Spatial---compounding error across the trajectory destroys performance entirely (Section~\\ref{sec:magnitude}).\nThe Argmin baseline (34\\%) outperforms all CRM variants at this setting, demonstrating that unbounded correction is harmful.\nThe obs\\_only variant was not evaluated at $\\varepsilon{=}1.42$ on spatial, though analogous catastrophic failure is expected given the magnitude of unconstrained corrections.\n\n\\paragraph{Practical recommendation.}\nThe safe operating range is $\\varepsilon \\in [0.05, 0.2]$.\nWithin this range, obs\\_only is the only variant that consistently matches or exceeds the Argmin baseline.\nWe use $\\varepsilon{=}0.1$ as the default, which provides a conservative margin below the point where perdof begins to degrade.\n\n\n\\subsection{Per-Task Analysis}\n\\label{sec:per_task}\n\nPer-task success rate breakdowns will reveal which task categories benefit most from residual correction and where the method provides no improvement.\n\n[\\textsc{pending}: seed43] --- A per-task heatmap comparing obs\\_only, Argmin, and VLA-only across all 20 tasks (10 LIBERO-Spatial + 10 LIBERO-Object) will be included upon completion of the seed 43 replication.\nWe expect the analysis to show that obs\\_only's gains on LIBERO-Object concentrate on tasks requiring precise object grasping under visual variation, while LIBERO-Spatial tasks remain uniformly unaffected by correction.\nTask difficulty analysis (measured by VLA-only success rate) will additionally test whether CRM helps more on medium-difficulty tasks where the base policy partially succeeds, versus easy tasks (ceiling effect) or hard tasks (base policy too far from success for small corrections to recover).\n",
      "numLines": 195,
      "startLine": 1,
      "totalLines": 195
    }
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Read · `toolu_016so8Ni3MKfsLbnx9ZpfbQe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b16f27b0-c2a7-4577-9c47-7e04efa7097f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012YkrjP2wTNMnv97GBcFVwA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1683,
      "cache_read_input_tokens": 23948,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1683
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

_source line 21 · 2026-05-15T20:15:58.100Z_

<details><summary>↩ Tool result · `toolu_016so8Ni3MKfsLbnx9ZpfbQe`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\subsection{VLA Robustness}
4	
5	Methods for improving VLA robustness divide into training-time and inference-time approaches.
6	
7	\paragraph{Training-time methods.}
8	RobustVLA~\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.
9	SRPO~\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.
10	DiG-Flow~\cite{digflow2025} regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.
11	TT-VLA~\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.
12	A shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.
13	
14	\paragraph{Inference-time methods.}
15	ReconVLA~\cite{chen2026reconvla} uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining.
16	SC-VLA~\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.
17	VLA-Pilot~\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\,s per control step---prohibitive for real-time manipulation.
18	A2C2~\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.
19	
20	ACR-VLA occupies a specific point in this design space: inference-time, plug-and-play (no retraining of the base VLA), and combining conformal selection with learned correction.
21	Selection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.
22	Correction alone (as in A2C2) lacks a mechanism to identify a good starting point.
23	ACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.
24	
25	\subsection{Conformal Prediction in Robotics}
26	
27	Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\cite{angelopoulos2023gentle}.
28	For multivariate outputs, Braun et al.~\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.
29	
30	In robotics, CP has been applied to several safety-critical settings.
31	Conformalized Teleoperation~\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.
32	CP-in-the-Loop~\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.
33	ACP+CBF~\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.
34	A common pattern across these methods is that CP serves as a \emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.
35	
36	ACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \emph{not} claim formal coverage guarantees for the corrected output.
37	CP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\ref{sec:ablation}).
38	The downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.
39	
40	\subsection{Residual Policy Learning}
41	
42	Residual policy learning augments a base controller with a learned additive correction.
43	Silver et al.~\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy.
44	Subsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.
45	TRANSIC~\cite{jiang2024transic} uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse.
46	PLD~\cite{xiao2026pld} introduces a scheduled magnitude bound $\xi$ for residual RL on VLAs, progressively increasing the allowed correction range during training.
47	DRC~\cite{pan2025drc} applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones.
48	
49	Magnitude control is the key connection to ACR-VLA: Silver et al.\ use residual scaling, TRANSIC uses binary gating, PLD uses scheduling, DRC uses temporal decay.
50	ACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\ref{sec:experiments}).
51	We view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.
52	A second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.
53	
54	\subsection{Uncertainty Quantification for VLAs}
55	
56	Recent work has developed UQ methods tailored to VLA architectures.
57	DiU~\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.
58	SAFE~\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.
59	Zollo and Zemel~\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.
60	
61	ACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.
62	The multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.
63	Functionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\cite{zollo2025vla_calibration} targets confidence reliability.
64	Our ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9a1ee76a-69c0-4af4-af4f-2b5b88cce6c5",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\subsection{VLA Robustness}\n\nMethods for improving VLA robustness divide into training-time and inference-time approaches.\n\n\\paragraph{Training-time methods.}\nRobustVLA~\\cite{robustvla2025} combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\nSRPO~\\cite{srpo2025} applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.\nDiG-Flow~\\cite{digflow2025} regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.\nTT-VLA~\\cite{liu2026ttvla} blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\nA shared limitation of these methods is the requirement for retraining, reward engineering, or per-task RL---making them difficult to apply as drop-in improvements to an arbitrary frozen VLA.\n\n\\paragraph{Inference-time methods.}\nReconVLA~\\cite{chen2026reconvla} uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining.\nSC-VLA~\\cite{liu2026scvla} performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy.\nVLA-Pilot~\\cite{li2025vlapilot} applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41\\,s per control step---prohibitive for real-time manipulation.\nA2C2~\\cite{a2c2_2025} learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty.\n\nACR-VLA occupies a specific point in this design space: inference-time, plug-and-play (no retraining of the base VLA), and combining conformal selection with learned correction.\nSelection alone is upper-bounded by sample quality---it cannot produce an action better than the best sample.\nCorrection alone (as in A2C2) lacks a mechanism to identify a good starting point.\nACR-VLA addresses both by selecting a low-nonconformity candidate via Mahalanobis scoring, then applying a bounded residual correction trained offline with supervised $L_2$ loss.\n\n\\subsection{Conformal Prediction in Robotics}\n\nConformal prediction (CP) provides distribution-free coverage guarantees under exchangeability~\\cite{angelopoulos2023gentle}.\nFor multivariate outputs, Braun et al.~\\cite{braun2025cgs} develop Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance---the scoring method ACR-VLA builds upon for its selection stage.\n\nIn robotics, CP has been applied to several safety-critical settings.\nConformalized Teleoperation~\\cite{zhao2024conformalized} uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\nCP-in-the-Loop~\\cite{wang2025cploop} integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\nACP+CBF~\\cite{zhou2025acp_cbf} combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies.\nA common pattern across these methods is that CP serves as a \\emph{binary decision mechanism}---accept or reject, safe or unsafe, execute or abstain.\n\nACR-VLA uses Mahalanobis nonconformity scores derived from shrinkage covariance estimates in its selection stage, but does \\emph{not} claim formal coverage guarantees for the corrected output.\nCP serves here as a scoring mechanism: the Mahalanobis score ranks samples for selection, and the covariance structure is available as conditioning features for the correction module (though our ablations find that observation features alone suffice; Section~\\ref{sec:ablation}).\nThe downstream correction module produces a refined action whose relationship to the original conformal region is no longer governed by coverage theory.\n\n\\subsection{Residual Policy Learning}\n\nResidual policy learning augments a base controller with a learned additive correction.\nSilver et al.~\\cite{silver2018residual} introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy.\nSubsequent work has focused on controlling residual magnitude---a central design concern, since unconstrained corrections lead to compounding error and policy collapse.\nTRANSIC~\\cite{jiang2024transic} uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse.\nPLD~\\cite{xiao2026pld} introduces a scheduled magnitude bound $\\xi$ for residual RL on VLAs, progressively increasing the allowed correction range during training.\nDRC~\\cite{pan2025drc} applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones.\n\nMagnitude control is the key connection to ACR-VLA: Silver et al.\\ use residual scaling, TRANSIC uses binary gating, PLD uses scheduling, DRC uses temporal decay.\nACR-VLA uses fixed $L_2$ norm clipping---the simplest possible scheme---yet our ablations show that the choice of clipping threshold $\\varepsilon$ has an outsized effect on performance, with the optimal value varying across task suites (Section~\\ref{sec:experiments}).\nWe view this as evidence that magnitude control in VLA inference-time correction is an underexplored hyperparameter.\nA second distinction separates ACR-VLA from the above methods: all four require RL training (reward functions, environment interaction, or on-policy rollouts), whereas ACR-VLA's correction module is trained with supervised $L_2$ loss on offline demonstration data, requiring neither reward design nor environment access during training.\n\n\\subsection{Uncertainty Quantification for VLAs}\n\nRecent work has developed UQ methods tailored to VLA architectures.\nDiU~\\cite{xing2026diu} derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling.\nSAFE~\\cite{gu2025safe} trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.\nZollo and Zemel~\\cite{zollo2025vla_calibration} provide the first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks.\n\nACR-VLA takes a multi-sample approach to UQ ($K{=}10$ forward passes), in contrast to DiU's single-pass estimation.\nThe multi-sample strategy is more expensive but captures both epistemic and aleatoric uncertainty components---a property that matters under distribution shift, where epistemic uncertainty rises but single-pass aleatoric estimates may not.\nFunctionally, ACR-VLA uses uncertainty for action selection (identifying the lowest-nonconformity sample), whereas DiU targets efficient uncertainty visualization, SAFE targets failure detection, and VLA calibration~\\cite{zollo2025vla_calibration} targets confidence reliability.\nOur ablations reveal a negative result connecting to this literature: per-DOF conformal features, despite their richer structure, do not improve correction performance when used as CRM input at the $K{=}10$ budget (Section~\\ref{sec:ablation}), suggesting that translating fine-grained uncertainty estimates into actionable correction signals remains an open challenge.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I need to extract all citations from these four files and check the method attribution for each one. Let me compile the list of all citations and their contextual descriptions in the paper.

Let me extract all unique citation keys and how they are described:

From **introduction_scenarioC.tex**:
1. `black2024pi0` - "flow matching" VLA
2. `shukor2025smolvla` - flow matching VLA
3. `liu2023libero` - LIBERO benchmark
4. `fei2025liberoplus` - distribution shift causes performance degradation


5. `robustvla2025` - training-time robustness method
6. `srpo2025` - training-time robustness method
7. `digflow2025` - training-time robustness method
8. `chen2026reconvla` - uses multiple action samples with conformal scoring for selection
9. `sc_vla_2026` - learns residual corrections through reinforcement learning with per-task environment interaction
10. `vla_pilot_2025` - applies evolutionary optimization to a frozen VLA guided by an external multimodal verifier, though it's computationally expensive at 2.41s per step
11. `a2c2` - continuing through the remaining citations

, I see `a2c2_2025` trains an asynchronous correction head alongside the VLA, while `braun2025cgs` applies Mahalanobis nonconformity with Ledoit-Wolf shrinkage covariance. Then there's foundational work like DAgger for handling distribution shift, residual policy approaches from Silver and others, and flow matching techniques. I'm also noting which citations appear across both the main text and method.tex sections.

Now looking at the related work, I'm seeing several test-time adaptation approaches: TT-VLA uses RL with progress rewards, SC-VLA combines sparse world imagination with residual RL, and VLA-Pilot leverages evolutionary diffusion guided by an MLLM verifier. There's also conformal prediction work—both a gentle introduction and Conformalized Teleoperation which applies CP to quantify uncertainty in high-DOF action mappings during shared autonomy, plus CP-in-the-Loop which integrates...

Continuing through the conformal prediction methods: CP-in-the-Loop uses CP regions as feedback constraints in trajectory optimization, ACP+CBF combines adaptive conformal prediction with control barrier functions, and DRC applies temporal decay of correction magnitude across episodes. For flow-matching models, DiU derives a closed-form posterior covariance by computing the velocity field divergence. SAFE trains a multitask failure detector on VLA features and uses conformal prediction to calibrate detection timing. And there's a systematic study on VLA calibration showing that prompt ensembles with Platt scaling improve confidence calibration. I need to verify the method attribution for each of these.

Let me check the bibliography file for full reference details and search for each paper to confirm the attributions. I'm aware there's a known attribution error with chen2026reconvla that I need to account for. Given how many papers there are—especially the recent 2025/2026 ones—I'll need to search systematically through the references.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a44266e4-f41f-454f-aafe-af58c8533cf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bc6Jghu9gV8Ak5Usk1aW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12678,
      "cache_read_input_tokens": 25631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12678
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

_source line 23_

已读取四个 .tex 文件，提取了所有引用。共有约 29 个唯一引用 key。先找 bib 文件获取完整引用信息，然后并行验证方法归因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b309d09f-d909-4d22-8cdc-1d24342de300",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bc6Jghu9gV8Ak5Usk1aW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12678,
      "cache_read_input_tokens": 25631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12678
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

_source line 24_

<details open><summary>🔧 Tool call — Glob · `toolu_012MAdDRycjqpbPpLMEWjmSY`</summary>

```json
{
  "pattern": "**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4aa535d6-4d96-4996-840c-1e3fc8e48585",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G7bc6Jghu9gV8Ak5Usk1aW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12678,
      "cache_read_input_tokens": 25631,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12678
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

_source line 25 · 2026-05-15T20:16:21.643Z_

<details><summary>↩ Tool result · `toolu_012MAdDRycjqpbPpLMEWjmSY`</summary>

```text
artifacts/_project/paper/references_e9d4d2.bib
artifacts/_project/paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "67e30932-536a-4df0-872b-2aa026467435",
  "tool_use_result": {
    "filenames": [
      "artifacts/_project/paper/references_e9d4d2.bib",
      "artifacts/_project/paper/references.bib"
    ],
    "durationMs": 10,
    "numFiles": 2,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01HQhaZMbCsqJ1hdtX5jN9Mh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4a2e7349-4be9-444d-ac9a-097d0d4f356e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XXzra1n5iQFmRXQPpPXyXJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1317,
      "cache_read_input_tokens": 38309,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1317
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

_source line 27 · 2026-05-15T20:16:24.217Z_

<details><summary>↩ Tool result · `toolu_01HQhaZMbCsqJ1hdtX5jN9Mh`</summary>

```text
1	@misc{a2c2_2025,
2	    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},
3	    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},
4	    year={2025},
5	    eprint={2509.23224},
6	    archivePrefix={arXiv},
7	    primaryClass={cs.RO}
8	}
9	
10	@article{angelopoulos2023gentle,
11	    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},
12	    author={Anastasios N. Angelopoulos and Stephen Bates},
13	    journal={Foundations and Trends in Machine Learning},
14	    year={2023},
15	    eprint={2107.07511},
16	    archivePrefix={arXiv},
17	    primaryClass={cs.LG}
18	}
19	
20	@article{barber2023conformal,
21	    title={Conformal Prediction Beyond Exchangeability},
22	    author={Rina Foygel Barber and Emmanuel J. Cand{\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},
23	    journal={Annals of Statistics},
24	    volume={51},
25	    number={2},
26	    pages={816--845},
27	    year={2023}
28	}
29	
30	@misc{black2024pi0,
31	    title={$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},
32	    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},
33	    year={2024},
34	    eprint={2410.24164},
35	    archivePrefix={arXiv},
36	    primaryClass={cs.RO}
37	}
38	
39	@misc{braun2025cgs,
40	    title={Multivariate Standardized Residuals for Conformal Prediction},
41	    author={Sacha Braun and Eug{\`e}ne Berta and Michael I. Jordan and Francis Bach},
42	    year={2025},
43	    eprint={2507.20941},
44	    archivePrefix={arXiv},
45	    primaryClass={stat.ML}
46	}
47	
48	@misc{brohan2023rt2,
49	    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},
50	    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},
51	    year={2023},
52	    eprint={2307.15818},
53	    archivePrefix={arXiv},
54	    primaryClass={cs.RO}
55	}
56	
57	@misc{chen2026reconvla,
58	    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},
59	    author={Lingling Chen and Zongyao Lyu and William J. Beksi},
60	    year={2026},
61	    eprint={2604.16677},
62	    archivePrefix={arXiv},
63	    primaryClass={cs.RO}
64	}
65	
66	@misc{cosmos_policy_2026,
67	    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},
68	    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},
69	    year={2026},
70	    eprint={2601.16163},
71	    archivePrefix={arXiv},
72	    primaryClass={cs.AI}
73	}
74	
75	@misc{digflow2025,
76	    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},
77	    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},
78	    year={2025},
79	    eprint={2512.01715},
80	    archivePrefix={arXiv},
81	    primaryClass={cs.RO}
82	}
83	
84	@misc{fei2025liberoplus,
85	    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},
86	    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},
87	    year={2025},
88	    eprint={2510.13626},
89	    archivePrefix={arXiv},
90	    primaryClass={cs.RO}
91	}
92	
93	@inproceedings{gal2016dropout,
94	    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},
95	    author={Yarin Gal and Zoubin Ghahramani},
96	    booktitle={International Conference on Machine Learning (ICML)},
97	    year={2016}
98	}
99	
100	@misc{ghosh2024octo,
101	    title={Octo: An Open-Source Generalist Robot Policy},
102	    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},
103	    year={2024},
104	    eprint={2405.12213},
105	    archivePrefix={arXiv},
106	    primaryClass={cs.RO}
107	}
108	
109	@inproceedings{gibbs2021aci,
110	    title={Adaptive Conformal Inference Under Distribution Shift},
111	    author={Isaac Gibbs and Emmanuel Cand{\`e}s},
112	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
113	    year={2021}
114	}
115	
116	@inproceedings{gu2025safe,
117	    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},
118	    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},
119	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
120	    year={2025}
121	}
122	
123	@misc{kim2024openvla,
124	    title={OpenVLA: An Open-Source Vision-Language-Action Model},
125	    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},
126	    year={2024},
127	    eprint={2406.09246},
128	    archivePrefix={arXiv},
129	    primaryClass={cs.RO}
130	}
131	
132	@inproceedings{lakshminarayanan2017ensembles,
133	    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},
134	    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},
135	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
136	    year={2017}
137	}
138	
139	@article{ledoit2004well,
140	    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},
141	    author={Olivier Ledoit and Michael Wolf},
142	    journal={Journal of Multivariate Analysis},
143	    volume={88},
144	    number={2},
145	    pages={365--411},
146	    year={2004}
147	}
148	
149	@inproceedings{lipman2023flow,
150	    title={Flow Matching for Generative Modeling},
151	    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},
152	    booktitle={International Conference on Learning Representations (ICLR)},
153	    year={2023}
154	}
155	
156	@inproceedings{liu2023libero,
157	    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},
158	    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},
159	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
160	    year={2023}
161	}
162	
163	@misc{liu2026ttvla,
164	    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},
165	    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},
166	    year={2026},
167	    eprint={2601.06748},
168	    archivePrefix={arXiv},
169	    primaryClass={cs.RO}
170	}
171	
172	@misc{luan2026snapflow,
173	    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},
174	    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},
175	    year={2026},
176	    eprint={2604.05656},
177	    archivePrefix={arXiv},
178	    primaryClass={cs.RO}
179	}
180	
181	@misc{robustvla2025,
182	    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},
183	    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},
184	    year={2025},
185	    eprint={2511.01331},
186	    archivePrefix={arXiv},
187	    primaryClass={cs.RO}
188	}
189	
190	@inproceedings{romano2019cqr,
191	    title={Conformalized Quantile Regression},
192	    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\`e}s},
193	    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},
194	    year={2019}
195	}
196	
197	@article{shafer2008tutorial,
198	    title={A Tutorial on Conformal Prediction},
199	    author={Glenn Shafer and Vladimir Vovk},
200	    journal={Journal of Machine Learning Research},
201	    volume={9},
202	    pages={371--421},
203	    year={2008}
204	}
205	
206	@misc{shukor2025smolvla,
207	    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},
208	    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},
209	    year={2025},
210	    eprint={2506.01844},
211	    archivePrefix={arXiv},
212	    primaryClass={cs.RO}
213	}
214	
215	@misc{srpo2025,
216	    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},
217	    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},
218	    year={2025},
219	    eprint={2511.15605},
220	    archivePrefix={arXiv},
221	    primaryClass={cs.RO}
222	}
223	
224	@misc{vla_gse_2026,
225	    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},
226	    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},
227	    year={2026},
228	    eprint={2605.06175},
229	    archivePrefix={arXiv},
230	    primaryClass={cs.RO}
231	}
232	
233	@misc{wang2025cploop,
234	    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},
235	    author={Han Wang and Chao Ning},
236	    year={2025},
237	    eprint={2510.16376},
238	    archivePrefix={arXiv},
239	    primaryClass={cs.RO}
240	}
241	
242	@misc{xing2026diu,
243	    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},
244	    author={Jiarui Xing and Song Wang and Jian Wang},
245	    year={2026},
246	    eprint={2605.00941},
247	    archivePrefix={arXiv},
248	    primaryClass={cs.LG}
249	}
250	
251	@misc{yuan2026ups,
252	    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},
253	    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},
254	    year={2026},
255	    eprint={2602.22474},
256	    archivePrefix={arXiv},
257	    primaryClass={cs.RO}
258	}
259	
260	@inproceedings{chi2023diffusion_policy,
261	    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},
262	    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},
263	    booktitle={Robotics: Science and Systems (RSS)},
264	    year={2023},
265	    note={Also published in IJRR 2024. arXiv:2303.04137}
266	}
267	
268	@inproceedings{zhao2024conformalized,
269	    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},
270	    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},
271	    booktitle={Robotics: Science and Systems (RSS)},
272	    year={2024}
273	}
274	
275	@inproceedings{silver2018residual,
276	    title={Residual Policy Learning},
277	    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},
278	    booktitle={Robotics: Science and Systems (RSS)},
279	    year={2018},
280	    note={arXiv:1812.06298}
281	}
282	
283	@inproceedings{jiang2024transic,
284	    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},
285	    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},
286	    booktitle={Conference on Robot Learning (CoRL)},
287	    year={2024},
288	    note={arXiv:2405.10315}
289	}
290	
291	@inproceedings{xiao2026pld,
292	    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},
293	    author={Wenli Xiao and others},
294	    booktitle={International Conference on Learning Representations (ICLR)},
295	    year={2026},
296	    note={arXiv:2511.00091}
297	}
298	
299	@misc{pan2025drc,
300	    title={DRC: Decaying Relative Correction for Policy Refinement},
301	    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},
302	    year={2025},
303	    eprint={2503.15368},
304	    archivePrefix={arXiv},
305	    primaryClass={cs.RO}
306	}
307	
308	@inproceedings{zhou2025acp_cbf,
309	    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},
310	    author={Zetian Zhou and Shuo Yang and Wenhao Luo},
311	    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},
312	    year={2025},
313	    note={arXiv:2503.17678}
314	}
315	
316	@misc{zollo2025vla_calibration,
317	    title={Confidence Calibration in Vision-Language-Action Models},
318	    author={Matteo Zollo and Richard Zemel},
319	    year={2025},
320	    eprint={2507.17383},
321	    archivePrefix={arXiv},
322	    primaryClass={cs.RO}
323	}
324	
325	@inproceedings{ross2011dagger,
326	    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},
327	    author={St{\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},
328	    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},
329	    year={2011}
330	}
331	
332	@misc{tang2026shifting,
333	    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},
334	    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},
335	    year={2026},
336	    eprint={2603.18342},
337	    archivePrefix={arXiv},
338	    primaryClass={cs.RO}
339	}
340	
341	@misc{liu2026scvla,
342	    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},
343	    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},
344	    year={2026},
345	    eprint={2602.21633},
346	    archivePrefix={arXiv},
347	    primaryClass={cs.RO}
348	}
349	
350	@misc{li2025vlapilot,
351	    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},
352	    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},
353	    year={2025},
354	    eprint={2511.14178},
355	    archivePrefix={arXiv},
356	    primaryClass={cs.RO}
357	}
358	
359	@inproceedings{zhong2026acotvla,
360	    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},
361	    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},
362	    year={2026},
363	    eprint={2601.11404},
364	    archivePrefix={arXiv},
365	    primaryClass={cs.RO},
366	    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}
367	}
368	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "43d73698-70d8-49f3-80de-5b4a033cb835",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/_project/paper/references.bib",
      "content": "@misc{a2c2_2025,\n    title={Leave No Observation Behind: Real-time Correction for VLA Action Chunks},\n    author={Kohei Sendai and Maxime Alvarez and Tatsuya Matsushima and Yutaka Matsuo and Yusuke Iwasawa},\n    year={2025},\n    eprint={2509.23224},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@article{angelopoulos2023gentle,\n    title={A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification},\n    author={Anastasios N. Angelopoulos and Stephen Bates},\n    journal={Foundations and Trends in Machine Learning},\n    year={2023},\n    eprint={2107.07511},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@article{barber2023conformal,\n    title={Conformal Prediction Beyond Exchangeability},\n    author={Rina Foygel Barber and Emmanuel J. Cand{\\`e}s and Aaditya Ramdas and Ryan J. Tibshirani},\n    journal={Annals of Statistics},\n    volume={51},\n    number={2},\n    pages={816--845},\n    year={2023}\n}\n\n@misc{black2024pi0,\n    title={$\\pi_0$: A Vision-Language-Action Flow Model for General Robot Control},\n    author={Kevin Black and Noah Brown and Danny Driess and Adnan Esmail and Michael Equi and Chelsea Finn and Niccolo Fusai and Lachy Groom and Karol Hausman and Brian Ichter and Szymon Jakubczak and Tim Jones and Liyiming Ke and Sergey Levine and Adrian Li-Bell and Mohith Mothukuri and Suraj Nair and Karl Pertsch and Lucy Xiaoyang Shi and James Tanner and Quan Vuong and Anna Walling and Haohuan Wang and Ury Zhilinsky},\n    year={2024},\n    eprint={2410.24164},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{braun2025cgs,\n    title={Multivariate Standardized Residuals for Conformal Prediction},\n    author={Sacha Braun and Eug{\\`e}ne Berta and Michael I. Jordan and Francis Bach},\n    year={2025},\n    eprint={2507.20941},\n    archivePrefix={arXiv},\n    primaryClass={stat.ML}\n}\n\n@misc{brohan2023rt2,\n    title={RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control},\n    author={Anthony Brohan and Noah Brown and Justice Carbajal and Yevgen Chebotar and Xi Chen and Krzysztof Choromanski and Tianli Ding and Danny Driess and Avinava Dubey and Chelsea Finn and Pete Florence and Chuyuan Fu and Montse Gonzalez Arenas and Keerthana Gopalakrishnan and Kehang Han and Karol Hausman and Alexander Herzog and Jasmine Hsu and Brian Ichter and Alex Irpan and Nikhil Joshi and Ryan Julian and Dmitry Kalashnikov and Yuheng Kuang and Isabel Leal and Lisa Lee and Tsang-Wei Edward Lee and Sergey Levine and Yao Lu and Henryk Michalewski and Igor Mordatch and Karl Pertsch and Kanishka Rao and Krista Reymann and Michael Ryoo and Grecia Salazar and Pannag Sanketi and Pierre Sermanet and Jaspiar Singh and Anikait Singh and Radu Soricut and Huong Tran and Vincent Vanhoucke and Quan Vuong and Ayzaan Wahid and Stefan Welker and Paul Wohlhart and Jialin Wu and Fei Xia and Ted Xiao and Peng Xu and Sichun Xu and Tianhe Yu and Brianna Zitkovich},\n    year={2023},\n    eprint={2307.15818},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{chen2026reconvla,\n    title={ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control},\n    author={Lingling Chen and Zongyao Lyu and William J. Beksi},\n    year={2026},\n    eprint={2604.16677},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{cosmos_policy_2026,\n    title={Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning},\n    author={Moo Jin Kim and Yihuai Gao and Tsung-Yi Lin and Yen-Chen Lin and Yunhao Ge and Grace Lam and Percy Liang and Shuran Song and Ming-Yu Liu and Chelsea Finn and Jinwei Gu},\n    year={2026},\n    eprint={2601.16163},\n    archivePrefix={arXiv},\n    primaryClass={cs.AI}\n}\n\n@misc{digflow2025,\n    title={DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models},\n    author={Wanpeng Zhang and Ye Wang and Hao Luo and Haoqi Yuan and Yicheng Feng and Sipeng Zheng and Qin Jin and Zongqing Lu},\n    year={2025},\n    eprint={2512.01715},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{fei2025liberoplus,\n    title={LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Junhao Shi and Zihao Dai and Jikun Cai and Pengfang Qian and Li Ji and Xinzhe He and Shiduo Zhang and Zhaoye Fei and Jinlan Fu and Jingjing Gong and Xipeng Qiu},\n    year={2025},\n    eprint={2510.13626},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gal2016dropout,\n    title={Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning},\n    author={Yarin Gal and Zoubin Ghahramani},\n    booktitle={International Conference on Machine Learning (ICML)},\n    year={2016}\n}\n\n@misc{ghosh2024octo,\n    title={Octo: An Open-Source Generalist Robot Policy},\n    author={Dibya Ghosh and Homer Walke and Karl Pertsch and Kevin Black and Oier Mees and Sudeep Dasari and Joey Hejna and Tobias Kreiman and Charles Xu and Jianlan Luo and You Liang Tan and Lawrence Yunliang Chen and Pannag Sanketi and Quan Vuong and Ted Xiao and Dorsa Sadigh and Chelsea Finn and Sergey Levine},\n    year={2024},\n    eprint={2405.12213},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{gibbs2021aci,\n    title={Adaptive Conformal Inference Under Distribution Shift},\n    author={Isaac Gibbs and Emmanuel Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2021}\n}\n\n@inproceedings{gu2025safe,\n    title={SAFE: Multitask Failure Detection for Vision-Language-Action Models},\n    author={Qiao Gu and Yuanliang Ju and Shengxiang Sun and Igor Gilitschenski and Haruki Nishimura and Masha Itkina and Florian Shkurti},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2025}\n}\n\n@misc{kim2024openvla,\n    title={OpenVLA: An Open-Source Vision-Language-Action Model},\n    author={Moo Jin Kim and Karl Pertsch and Siddharth Karamcheti and Ted Xiao and Ashwin Balakrishna and Suraj Nair and Rafael Rafailov and Ethan Foster and Grace Lam and Pannag Sanketi and Quan Vuong and Thomas Kollar and Benjamin Burchfiel and Russ Tedrake and Dorsa Sadigh and Sergey Levine and Percy Liang and Chelsea Finn},\n    year={2024},\n    eprint={2406.09246},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{lakshminarayanan2017ensembles,\n    title={Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles},\n    author={Balaji Lakshminarayanan and Alexander Pritzel and Charles Blundell},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2017}\n}\n\n@article{ledoit2004well,\n    title={A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices},\n    author={Olivier Ledoit and Michael Wolf},\n    journal={Journal of Multivariate Analysis},\n    volume={88},\n    number={2},\n    pages={365--411},\n    year={2004}\n}\n\n@inproceedings{lipman2023flow,\n    title={Flow Matching for Generative Modeling},\n    author={Yaron Lipman and Ricky T. Q. Chen and Heli Ben-Hamu and Maximilian Nickel and Matt Le},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2023}\n}\n\n@inproceedings{liu2023libero,\n    title={LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning},\n    author={Bo Liu and Yifeng Zhu and Chongkai Gao and Yihao Feng and Qiang Liu and Yuke Zhu and Peter Stone},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2023}\n}\n\n@misc{liu2026ttvla,\n    title={On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning},\n    author={Changyu Liu and Yiyang Liu and Taowen Wang and Qiao Zhuang and James Chenhao Liang and Wenhao Yang and Renjing Xu and Qifan Wang and Dongfang Liu and Cheng Han},\n    year={2026},\n    eprint={2601.06748},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{luan2026snapflow,\n    title={SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation},\n    author={Wuyang Luan and Junhui Li and Weiguang Zhao and Wenjian Zhang and Tieru Wu and Rui Ma},\n    year={2026},\n    eprint={2604.05656},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{robustvla2025,\n    title={RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models},\n    author={Hongyin Zhang and Shuo Zhang and Junxi Jin and Qixin Zeng and Runze Li and Donglin Wang},\n    year={2025},\n    eprint={2511.01331},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{romano2019cqr,\n    title={Conformalized Quantile Regression},\n    author={Yaniv Romano and Evan Patterson and Emmanuel J. Cand{\\`e}s},\n    booktitle={Advances in Neural Information Processing Systems (NeurIPS)},\n    year={2019}\n}\n\n@article{shafer2008tutorial,\n    title={A Tutorial on Conformal Prediction},\n    author={Glenn Shafer and Vladimir Vovk},\n    journal={Journal of Machine Learning Research},\n    volume={9},\n    pages={371--421},\n    year={2008}\n}\n\n@misc{shukor2025smolvla,\n    title={SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics},\n    author={Mustafa Shukor and Dana Aubakirova and Francesco Capuano and Pepijn Kooijmans and Steven Palma and Adil Zouitine and Michel Aractingi and Caroline Pascal and Martino Russi and Andres Marafioti and Simon Alibert and Matthieu Cord and Thomas Wolf and Remi Cadene},\n    year={2025},\n    eprint={2506.01844},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{srpo2025,\n    title={SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models},\n    author={Senyu Fei and Siyin Wang and Li Ji and Ao Li and Shiduo Zhang and Liming Liu and Jinlong Hou and Jingjing Gong and Xianzhong Zhao and Xipeng Qiu},\n    year={2025},\n    eprint={2511.15605},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{vla_gse_2026,\n    title={VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts},\n    author={Yuhua Jiang and Junjie Lu and Xinyao Qin and Xiaoyu Chen and Kaixin Wang and Feifei Gao and Li Zhao},\n    year={2026},\n    eprint={2605.06175},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{wang2025cploop,\n    title={Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization},\n    author={Han Wang and Chao Ning},\n    year={2025},\n    eprint={2510.16376},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{xing2026diu,\n    title={Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching},\n    author={Jiarui Xing and Song Wang and Jian Wang},\n    year={2026},\n    eprint={2605.00941},\n    archivePrefix={arXiv},\n    primaryClass={cs.LG}\n}\n\n@misc{yuan2026ups,\n    title={When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering},\n    author={Jessie Yuan and Yilin Wu and Andrea Bajcsy},\n    year={2026},\n    eprint={2602.22474},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{chi2023diffusion_policy,\n    title={Diffusion Policy: Visuomotor Policy Learning via Action Diffusion},\n    author={Cheng Chi and Zhenjia Xu and Siyuan Feng and Eric Cousineau and Benjamin Burchfiel and Shuran Song},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2023},\n    note={Also published in IJRR 2024. arXiv:2303.04137}\n}\n\n@inproceedings{zhao2024conformalized,\n    title={Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions},\n    author={Michelle Zhao and Reid Simmons and Henny Admoni and Andrea Bajcsy},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2024}\n}\n\n@inproceedings{silver2018residual,\n    title={Residual Policy Learning},\n    author={Tom Silver and Kelsey Allen and Josh Tenenbaum and Leslie Kaelbling},\n    booktitle={Robotics: Science and Systems (RSS)},\n    year={2018},\n    note={arXiv:1812.06298}\n}\n\n@inproceedings{jiang2024transic,\n    title={TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction},\n    author={Yunfan Jiang and Chen Wang and Ruohan Zhang and Jiajun Wu and Li Fei-Fei},\n    booktitle={Conference on Robot Learning (CoRL)},\n    year={2024},\n    note={arXiv:2405.10315}\n}\n\n@inproceedings{xiao2026pld,\n    title={Self-Improving Vision-Language-Action Models with Data Generation via Residual RL},\n    author={Wenli Xiao and others},\n    booktitle={International Conference on Learning Representations (ICLR)},\n    year={2026},\n    note={arXiv:2511.00091}\n}\n\n@misc{pan2025drc,\n    title={DRC: Decaying Relative Correction for Policy Refinement},\n    author={Xinjie Pan and Ruizhe Shi and Dongjie Yu and Zhiyuan Nan and Xiaowei Hu and Muxin Wei and Pengfei Li and Xin Li and Zhixiang Wang and Liang Gao and Xue Liu},\n    year={2025},\n    eprint={2503.15368},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhou2025acp_cbf,\n    title={Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning},\n    author={Zetian Zhou and Shuo Yang and Wenhao Luo},\n    booktitle={IEEE International Conference on Robotics and Automation (ICRA)},\n    year={2025},\n    note={arXiv:2503.17678}\n}\n\n@misc{zollo2025vla_calibration,\n    title={Confidence Calibration in Vision-Language-Action Models},\n    author={Matteo Zollo and Richard Zemel},\n    year={2025},\n    eprint={2507.17383},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{ross2011dagger,\n    title={A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning},\n    author={St{\\'e}phane Ross and Geoffrey J. Gordon and J. Andrew Bagnell},\n    booktitle={International Conference on Artificial Intelligence and Statistics (AISTATS)},\n    year={2011}\n}\n\n@misc{tang2026shifting,\n    title={Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model},\n    author={Yanchuan Tang and Taowen Wang and Yuefei Chen and Boxuan Zhang and Qiang Guan and Ruixiang Tang},\n    year={2026},\n    eprint={2603.18342},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{liu2026scvla,\n    title={Self-Correcting VLA: Online Action Refinement via Sparse World Imagination},\n    author={Chenyv Liu and Wentao Tan and Lei Zhu and Fengling Li and Jingjing Li and Guoli Yang and Heng Tao Shen},\n    year={2026},\n    eprint={2602.21633},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@misc{li2025vlapilot,\n    title={Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion},\n    author={Zhuo Li and Junjia Liu and Zhipeng Dong and Tao Teng and Quentin Rouxel and Darwin Caldwell and Fei Chen},\n    year={2025},\n    eprint={2511.14178},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO}\n}\n\n@inproceedings{zhong2026acotvla,\n    title={ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models},\n    author={Linqing Zhong and Yi Liu and Yifei Wei and Ziyu Xiong and Maoqing Yao and Si Liu and Guanghui Ren},\n    year={2026},\n    eprint={2601.11404},\n    archivePrefix={arXiv},\n    primaryClass={cs.RO},\n    booktitle={IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)}\n}\n",
      "numLines": 368,
      "startLine": 1,
      "totalLines": 368
    }
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have the full bib file and all the tex files. Let me compile the list of citations that appear in the active tex files and need method attribution verification.

Let me organize the citations by what's actually cited in the active tex files (introduction_scenarioC.tex, method.tex, experiments.tex, related_work.tex):

Citations that need method attribution verification (where the paper makes specific claims about what a cited work does):

1. **black2024pi0** - π₀, "generate actions via flow matching" 
2. **shukor2025smolvla** - SmolVLA, "450M-parameter flow-matching VLA"


3. **liu2023libero** - LIBERO benchmark
4. **fei2025liberoplus** - "distribution shifts... performance degrades substantially"
5. **robustvla2025** - "training-time methods... robustness-aware objectives" / "combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations"
6. **srpo2025** - "training-time methods" / "applies self-referential RL fine-tuning, using the policy's own rollouts as training signal"
7. **digflow2025** - "training-time methods" / "regularizes the flow-matching denoising trajectory via a disc"

Now looking at several inference-time and hybrid approaches: ReconVLA uses conformal scoring to select among multiple action samples and includes outlier detection, while SC-VLA learns residual corrections through per-task RL training. VLA-Pilot takes a different angle by steering a frozen VLA through evolutionary optimization guided by an external multimodal verifier.

Continuing through the methods, A2C² trains an asynchronous correction head jointly with the VLA rather than as a post-hoc module, and there are also classical approaches like Conformalized Gaussian Scoring using Mahalanobis-based scores, DAgger for handling distribution shift, and bounded residual corrections for combining learned and classical controllers.

Looking at more recent work: TRANSIC uses learned binary gating to selectively apply residual actions, PLD schedules magnitude bounds during training for residual RL on VLAs, and TT-VLA adapts VLA parameters at test time through RL with progress rewards. There's also foundational work on flow matching, Ledoit-Wolf shrinkage covariance estimation, and conformal prediction methods that provide distribution-free coverage guarantees under exchangeability.

Several papers integrate conformal prediction into VLA safety and control: one applies it to quantify uncertainty in high-DOF action mappings during shared autonomy, another uses CP regions as feedback constraints in trajectory optimization, and a third combines adaptive conformal prediction with control barrier functions for safety. DRC applies temporal decay of correction magnitude over episodes, while DiU derives closed-form posterior covariance for flow-matching models. SAFE trains a multitask failure detector on VLA features with conformal prediction for calibration, and there's a systematic study of confidence calibration in VLAs examining prompt ensembling approaches.

Now I'm verifying these papers against my knowledge base—I can confirm several foundational works like the Flow Matching paper, Ledoit-Wolf shrinkage, DAgger, Angelopoulos & Bates' conformal prediction introduction, and Residual Policy Learning are all correct.

For the more recent papers from 2025-2026, I'll need to search through my knowledge to verify those citations, particularly the VLA variants and the newer methods like conformalized approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "84ddb3ed-e5c1-4975-9c3d-c459cc9f9e41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUyHbGVAYrj4frhm5sSuqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 39626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6303
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

_source line 29_

已收集全部引用信息。现在需要加载 WebSearch 工具，然后并行验证每个引用的方法归因。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b0895da1-4340-4b47-877b-49a404457a8c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUyHbGVAYrj4frhm5sSuqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 39626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6303
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

_source line 30_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UdWZxZf9BZj1iFff5E7LMU`</summary>

```json
{
  "query": "select:WebSearch",
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
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "629bb98c-e68c-44e7-bba6-0ad03c470746",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QUyHbGVAYrj4frhm5sSuqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6303,
      "cache_read_input_tokens": 39626,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6303
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

_source line 31 · 2026-05-15T20:17:03.687Z_

<details><summary>↩ Tool result · `toolu_01UdWZxZf9BZj1iFff5E7LMU`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
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
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "466fefd8-3f4c-4f32-ab81-5545a57961c3",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 32_

<details><summary>Logged reasoning block</summary>

```text
Now I'll launch parallel agents to verify the method attributions for all citations. Let me split them into manageable groups. I'll create several agents, each handling a batch of citations.

Let me organize the citations into groups:

Group 1 (Known issue + VLA inference-time methods): chen2026reconvla, sc_vla_2026/liu2026scvla, li2025vlapilot, a2c2_2025
Group 2 (VLA training-time methods): robustvla2025, srpo2025, digflow2025, liu2026ttvla, fei2025liberoplus


Group 3 (Conformal prediction papers): braun2025cgs, zhao2024conformalized, wang2025cploop, zhou2025acp_cbf, gu2025safe, zollo2025vla_calibration
Group 4 (Residual policy + UQ): silver2018residual, jiang2024transic, xiao2026pld, pan2025drc, xing2026diu
Group 5 (Foundational/base): black2024pi0, shukor2025smolvla, lipman2023flow, ledoit2004well, ross2011dagger, angelopoulos2023gentle, liu2023libero

Now I'll dispatch these groups to parallel agents for verification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "90f29a6b-23da-4391-905f-de0c46da57b7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### Assistant

_source line 33_

开始并行验证所有引用的方法归因。分5组进行 WebSearch 验证。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7132d593-85b7-4d37-b10b-265bf0554b30",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

_source line 34_

<details open><summary>🔧 Tool call — Agent · `toolu_01UTBsMvrTNRDfUAoqL6Dfkr`</summary>

```json
{
  "description": "Verify VLA inference-time citations",
  "prompt": "You need to verify method attribution accuracy for 4 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. chen2026reconvla** (arXiv: 2604.16677)\nTitle: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\nPaper claims (in 3 places):\n- Introduction: \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate\"\n- Method: \"conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring\"\n- Related work: \"uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining\"\nKNOWN ISSUE: This citation's attribution has been flagged as potentially incorrect. Pay extra attention.\n\n**2. liu2026scvla** (arXiv: 2602.21633)\nTitle: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\nPaper claims:\n- Introduction (cited as sc_vla_2026): \"learns a residual correction via reinforcement learning, requiring per-task environment interaction\"\n- Related work: \"performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy\"\n\n**3. li2025vlapilot** (arXiv: 2511.14178)\nTitle: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\nPaper claims:\n- Introduction (cited as vla_pilot_2025): \"steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step\"\n- Related work: \"applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation\"\n\n**4. a2c2_2025** (arXiv: 2509.23224)\nTitle: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\nPaper claims:\n- Introduction: \"trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model\"\n- Related work: \"learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty\"\n\nSearch for each paper on arXiv and verify the method descriptions. Be thorough.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "dc26a4cd-0869-428b-802b-c5c24af52800",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Verify VLA inference-time citations",
  "task_type": "local_agent",
  "prompt": "You need to verify method attribution accuracy for 4 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. chen2026reconvla** (arXiv: 2604.16677)\nTitle: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\nPaper claims (in 3 places):\n- Introduction: \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate\"\n- Method: \"conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring\"\n- Related work: \"uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining\"\nKNOWN ISSUE: This citation's attribution has been flagged as potentially incorrect. Pay extra attention.\n\n**2. liu2026scvla** (arXiv: 2602.21633)\nTitle: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\nPaper claims:\n- Introduction (cited as sc_vla_2026): \"learns a residual correction via reinforcement learning, requiring per-task environment interaction\"\n- Related work: \"performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy\"\n\n**3. li2025vlapilot** (arXiv: 2511.14178)\nTitle: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\nPaper claims:\n- Introduction (cited as vla_pilot_2025): \"steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step\"\n- Related work: \"applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation\"\n\n**4. a2c2_2025** (arXiv: 2509.23224)\nTitle: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\nPaper claims:\n- Introduction: \"trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model\"\n- Related work: \"learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty\"\n\nSearch for each paper on arXiv and verify the method descriptions. Be thorough.",
  "uuid": "3f9c959e-59f2-4429-aa1d-14d2d2d5b1d3",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

## Round 1

14 recorded events

### User

_source line 36 · 2026-05-15T20:17:23.734Z_

You need to verify method attribution accuracy for 4 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.

**1. chen2026reconvla** (arXiv: 2604.16677)
Title: "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control"
Paper claims (in 3 places):
- Introduction: "draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate"
- Method: "conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring"
- Related work: "uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining"
KNOWN ISSUE: This citation's attribution has been flagged as potentially incorrect. Pay extra attention.

**2. liu2026scvla** (arXiv: 2602.21633)
Title: "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination"
Paper claims:
- Introduction (cited as sc_vla_2026): "learns a residual correction via reinforcement learning, requiring per-task environment interaction"
- Related work: "performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy"

**3. li2025vlapilot** (arXiv: 2511.14178)
Title: "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion"
Paper claims:
- Introduction (cited as vla_pilot_2025): "steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step"
- Related work: "applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation"

**4. a2c2_2025** (arXiv: 2509.23224)
Title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"
Paper claims:
- Introduction: "trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model"
- Related work: "learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty"

Search for each paper on arXiv and verify the method descriptions. Be thorough.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9041f3e4-6568-4691-8a1e-9a6506ff55a0"
}
```

</details>

---

### System

_source line 37_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Verify VLA inference-time citations",
  "usage": {
    "total_tokens": 14717,
    "tool_uses": 1,
    "duration_ms": 2374
  },
  "last_tool_name": "ToolSearch",
  "uuid": "befb6025-495a-4ab2-8a12-254b24b732e3",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 38_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA uncertainty-guided failure-aware vision-…",
  "usage": {
    "total_tokens": 16162,
    "tool_uses": 2,
    "duration_ms": 5570
  },
  "last_tool_name": "WebSearch",
  "uuid": "f2c8ab78-ddc2-4706-a61c-4284d53c6d43",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 39_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for Self-Correcting VLA online action refinement spar…",
  "usage": {
    "total_tokens": 16165,
    "tool_uses": 3,
    "duration_ms": 6923
  },
  "last_tool_name": "WebSearch",
  "uuid": "9e432291-37f5-4b7c-bbbd-0b7aea9cd150",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 40_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for VLA pilot plug-and-play inference-time embodied e…",
  "usage": {
    "total_tokens": 16168,
    "tool_uses": 4,
    "duration_ms": 7608
  },
  "last_tool_name": "WebSearch",
  "uuid": "1f479e16-7b18-475e-8920-feaea3053bd0",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 41_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for Leave No Observation Behind real-time correction …",
  "usage": {
    "total_tokens": 16171,
    "tool_uses": 5,
    "duration_ms": 7786
  },
  "last_tool_name": "WebSearch",
  "uuid": "4dc8e7f8-2aa0-43f6-82b9-fcaeeb1e46cb",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01QwvjkkKKunbC4RCywqMv9i`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7903ec81-8ced-4238-8710-70ba05b05b9f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SSuAE3NBis2pwPeDffGRAV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14680,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14680,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 43 · 2026-05-15T20:17:26.115Z_

<details><summary>↩ Tool result · `toolu_01QwvjkkKKunbC4RCywqMv9i`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "955cbefd-54a3-401b-a7b0-d5f02f111ca1"
}
```

</details>

---

### Tool call

_source line 44_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013WXvp3m65RMStrE35F9jAM`</summary>

```json
{
  "query": "ReconVLA uncertainty-guided failure-aware vision-language-action framework arXiv 2604.16677"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "34d5fba8-5283-482c-81e9-caaf86dfc2b2",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wq7tVa3PE2tM89rj9SASA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017ag8vjxxDozU6kHoRVUzAs`</summary>

```json
{
  "query": "Self-Correcting VLA online action refinement sparse world imagination arXiv 2602.21633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2d4b48e5-233a-4989-befd-5cf658b483ac",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wq7tVa3PE2tM89rj9SASA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 46_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01McRNz8QMppaXuZEj78vqZX`</summary>

```json
{
  "query": "VLA pilot plug-and-play inference-time embodied evolutionary diffusion arXiv 2511.14178"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6cdb0d46-423c-4e83-a738-ff9e1d3a2038",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wq7tVa3PE2tM89rj9SASA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MR3nJYuwqhHVvLDH1wrH2C`</summary>

```json
{
  "query": "Leave No Observation Behind real-time correction VLA action chunks arXiv 2509.23224"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a499ecbc-774e-4083-a7a8-8289eea8eef8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wq7tVa3PE2tM89rj9SASA6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14680,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Agent · `toolu_01F79KsYf2riw7ACdusRvggw`</summary>

```json
{
  "description": "Verify VLA training-time citations",
  "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. robustvla2025** (arXiv: 2511.01331)\nTitle: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\" with \"robustness-aware objectives\"\n- Related work: \"combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations\"\n\n**2. srpo2025** (arXiv: 2511.15605)\nTitle: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"applies self-referential RL fine-tuning, using the policy's own rollouts as training signal\"\n\n**3. digflow2025** (arXiv: 2512.01715)\nTitle: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective\"\n\n**4. liu2026ttvla** (arXiv: 2601.06748)\nTitle: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\nPaper claims:\n- Related work: \"blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment\"\n\n**5. fei2025liberoplus** (arXiv: 2510.13626)\nTitle: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\nPaper claims:\n- Introduction: \"under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially\"\n\nSearch for each paper on arXiv and verify the method descriptions.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3f26c906-30c9-447a-b951-20fdb5e27a44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### System

_source line 49_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Verify VLA training-time citations",
  "task_type": "local_agent",
  "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. robustvla2025** (arXiv: 2511.01331)\nTitle: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\" with \"robustness-aware objectives\"\n- Related work: \"combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations\"\n\n**2. srpo2025** (arXiv: 2511.15605)\nTitle: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"applies self-referential RL fine-tuning, using the policy's own rollouts as training signal\"\n\n**3. digflow2025** (arXiv: 2512.01715)\nTitle: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective\"\n\n**4. liu2026ttvla** (arXiv: 2601.06748)\nTitle: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\nPaper claims:\n- Related work: \"blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment\"\n\n**5. fei2025liberoplus** (arXiv: 2510.13626)\nTitle: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\nPaper claims:\n- Introduction: \"under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially\"\n\nSearch for each paper on arXiv and verify the method descriptions.",
  "uuid": "cca4a47c-0a73-4141-9f31-6a4f8aecb5ff",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

## Round 2

20 recorded events

### User

_source line 50 · 2026-05-15T20:17:31.789Z_

You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.

**1. robustvla2025** (arXiv: 2511.01331)
Title: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
Paper claims:
- Introduction: grouped as "Training-time methods" with "robustness-aware objectives"
- Related work: "combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations"

**2. srpo2025** (arXiv: 2511.15605)
Title: "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models"
Paper claims:
- Introduction: grouped as "Training-time methods"
- Related work: "applies self-referential RL fine-tuning, using the policy's own rollouts as training signal"

**3. digflow2025** (arXiv: 2512.01715)
Title: "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models"
Paper claims:
- Introduction: grouped as "Training-time methods"
- Related work: "regularizes the flow-matching denoising trajectory via a discrepancy-guided objective"

**4. liu2026ttvla** (arXiv: 2601.06748)
Title: "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning"
Paper claims:
- Related work: "blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment"

**5. fei2025liberoplus** (arXiv: 2510.13626)
Title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
Paper claims:
- Introduction: "under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially"

Search for each paper on arXiv and verify the method descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a0116167-071d-41b4-b70e-4530fee5958e"
}
```

</details>

---

### System

_source line 51_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Verify VLA training-time citations",
  "usage": {
    "total_tokens": 14551,
    "tool_uses": 1,
    "duration_ms": 2658
  },
  "last_tool_name": "ToolSearch",
  "uuid": "9558c7f6-3f02-40d5-8736-9d11a03e4bee",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 52_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for RobustVLA arXiv 2511.01331 Jacobian regularizatio…",
  "usage": {
    "total_tokens": 15996,
    "tool_uses": 2,
    "duration_ms": 6014
  },
  "last_tool_name": "WebSearch",
  "uuid": "301a739d-94b6-407f-9965-f16e15d02d65",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 53_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for SRPO Self-Referential Policy Optimization arXiv 2…",
  "usage": {
    "total_tokens": 15999,
    "tool_uses": 3,
    "duration_ms": 6799
  },
  "last_tool_name": "WebSearch",
  "uuid": "39496b7f-9653-41b7-a1b9-06b77135c864",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 54_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for DiG-Flow Discrepancy-Guided Flow Matching arXiv 2…",
  "usage": {
    "total_tokens": 16002,
    "tool_uses": 4,
    "duration_ms": 7588
  },
  "last_tool_name": "WebSearch",
  "uuid": "edfbe7fd-84a2-411d-8152-204cfeb6cdba",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 55_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for On-the-Fly VLA Adaptation Test-Time Reinforcement…",
  "usage": {
    "total_tokens": 16005,
    "tool_uses": 5,
    "duration_ms": 8832
  },
  "last_tool_name": "WebSearch",
  "uuid": "d79eb121-067c-4820-8cf7-e2813faaf2d7",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 56_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for LIBERO-Plus robustness analysis vision-language-a…",
  "usage": {
    "total_tokens": 16008,
    "tool_uses": 6,
    "duration_ms": 9374
  },
  "last_tool_name": "WebSearch",
  "uuid": "50dbf14b-5d80-4fff-8d20-0fd6b920cbae",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 57 · 2026-05-15T20:17:36.617Z_

<details><summary>↩ Tool result · `toolu_013WXvp3m65RMStrE35F9jAM`</summary>

```text
Web search results for query: "ReconVLA uncertainty-guided failure-aware vision-language-action framework arXiv 2604.16677"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/html/2512.03913v1"},{"title":"Computer Science","url":"https://arxiv.org/list/cs/pastweek?skip=263&show=2000"},{"title":"[2512.03913] Hierarchical Vision Language Action Model Using Success and Failure Demonstrations","url":"https://arxiv.org/abs/2512.03913"},{"title":"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.08434v2"},{"title":"Uncertainty-Aware Evaluation for Vision-Language Models","url":"https://arxiv.org/html/2402.14418v1"},{"title":"1 Introduction","url":"https://arxiv.org/html/2512.07564v1"},{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"}]

I found the paper you're looking for! Here's what I found about ReconVLA (arXiv 2604.16677):

## ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework

The paper was published on arXiv on April 17, 2026, by researchers Lingling Chen, Zongyao Lyu, and William J. Beksi from The University of Texas at Arlington's Department of Computer Science and Engineering.

### Overview

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences. However, VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.

### Key Contribution

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.

### Technical Components

ReconVLA augments the base model with two uncertainty-aware components: (i) a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and (ii) an SMD-based detector that monitors latent state distributions to identify OOD or failure-prone conditions. Together, these modules enable robust action selection and proactive failure detection during deployment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "c9d36897-e465-4c2e-a2a1-f0bf02968925"
}
```

</details>

---

### Tool result

_source line 58 · 2026-05-15T20:17:37.692Z_

<details><summary>↩ Tool result · `toolu_017ag8vjxxDozU6kHoRVUzAs`</summary>

```text
Web search results for query: "Self-Correcting VLA online action refinement sparse world imagination arXiv 2602.21633"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633v1"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"[2602.01811] From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/abs/2602.01811"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/html/2602.01811"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"DriveFine: Refining-Augmented Masked Diffusion VLA for Precise and Robust Driving","url":"https://arxiv.org/html/2602.14577"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v2"}]

I found the paper you're looking for! Here's what the search revealed:

## Self-Correcting VLA: Online Action Refinement via Sparse World Imagination

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

**Key Components:**

1. **Sparse World Imagination**: The framework integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

2. **Online Action Refinement Module**: The online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.

**Performance:**

SC-VLA achieves state-of-the-art performance on challenging robot manipulation tasks from simulation benchmarks and real-world settings, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

**Paper Details:**
- **arXiv ID**: 2602.21633
- **Posted**: February 25, 2026
- **Authors**: Chenyv Liu, Wentao Tan, and colleagues
- **Code**: Available on GitHub at [Kisaragi0/SC-VLA](https://github.com/Kisaragi0/SC-VLA)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "968a2510-f97c-4162-a7dd-5943dfee2af4"
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-15T20:17:38.403Z_

<details><summary>↩ Tool result · `toolu_01McRNz8QMppaXuZEj78vqZX`</summary>

```text
Web search results for query: "VLA pilot plug-and-play inference-time embodied evolutionary diffusion arXiv 2511.14178"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play...","url":"https://arxiv.org/abs/2511.14178"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"Paper page - EvoVLA: Self-Evolving Vision-Language-Action Model","url":"https://huggingface.co/papers/2511.16166"},{"title":"VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/html/2511.16449"},{"title":"[2511.16449] VLA-Pruner: Temporal-Aware Dual-Level Visual Token Pruning for Efficient Vision-Language-Action Inference","url":"https://arxiv.org/abs/2511.16449"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/html/2511.01718v1"},{"title":"Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments","url":"https://arxiv.org/html/2602.09430v1"},{"title":"[2511.01718] Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denoising Diffusion Process","url":"https://arxiv.org/abs/2511.01718"},{"title":"VLSA: Vision-Language-Action Models with Plug-and-Play Safety Constraint Layer","url":"https://arxiv.org/html/2512.11891v1"},{"title":"Anticipation-VLA: Solving Long-Horizon Embodied Tasks via Anticipation-based Subgoal Generation","url":"https://arxiv.org/html/2605.01772v1"}]

Based on the search results, I found the paper you're looking for. Here's information about it:

## VLA-Pilot: Plug-and-Play Inference-Time VLA Policy Steering

The full title is "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion" (arXiv 2511.14178).

**Overview:**
VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection. Pre-trained VLA policies suffer from substantial performance degradation during downstream deployment, and although fine-tuning can mitigate this issue, its reliance on costly demonstration collection and intensive computation makes it impractical in real-world settings.

**Technical Approach:**
The core idea leverages Multimodal Large Language Models (MLLMs) as open-world verifiers to enhance generalization, and employs an Evolutionary Diffusion process as an action optimizer to improve task alignment. VLA-Pilot uses an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs, which removes the need for training task-specific verifiers and significantly improves generalization to out-of-distribution tasks.

**Evaluation:**
VLA-Pilot was evaluated on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "14cc3ee8-ec57-41d1-b7a9-49f09db8d14d"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-15T20:17:40.601Z_

<details><summary>↩ Tool result · `toolu_01MR3nJYuwqhHVvLDH1wrH2C`</summary>

```text
Web search results for query: "Leave No Observation Behind real-time correction VLA action chunks arXiv 2509.23224"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224"},{"title":"LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS","url":"https://www.arxiv.org/pdf/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks | OpenReview","url":"https://openreview.net/forum?id=y5SGBsndWv"},{"title":"A Vision-Language-Action-Critic Model for Robotic Real-World Reinforcement Learning","url":"https://arxiv.org/html/2509.15937v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"[2509.03974] Real-time adaptive quantum error correction by model-free multi-agent learning","url":"https://arxiv.org/abs/2509.03974"},{"title":"Focusing on What Matters: Object-Agent-centric Tokenization for Vision Language Action Models","url":"https://arxiv.org/html/2509.23655v1"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"},{"title":"Latent Action Pretraining Through World Modeling","url":"https://arxiv.org/html/2509.18428v1"}]

I found the paper! Here's information about the research:

## Leave No Observation Behind: Real-time Correction for VLA Action Chunks (arXiv 2509.23224)

Vision-Language-Action (VLA) models often predict action chunks to improve efficiency and temporal coherence; however, this action chunking harms reactivity under inference delay and long horizons.

The paper introduces Asynchronous Action Chunk Correction (A2C2), a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

**Key Features:**

- This preserves the base model's competence while restoring closed-loop responsiveness.
- The approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).

**Results:**

On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, the method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay.

Since the correction head is small and fast, there is minimal overhead compared to the inference of large VLA models, and A2C2 is an effective, plug-in mechanism for deploying high-capacity chunking policies in real-time control.

The paper was submitted on September 27, 2025, by authors including Kohei Sendai, Maxime Alvarez, Tatsuya Matsushima, Yutaka Matsuo, and Yusuke Iwasawa.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "25e039fd-5e94-4a91-ad02-34cea16e6312"
}
```

</details>

---

### Tool call

_source line 61_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0164LJboAtqPMJPdbf5ZQRzu`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d90e9d72-6f4b-40b8-93ad-a915134750d4",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018Zei9pC2eAZBrZRrn6HcYL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6396,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6396,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 62 · 2026-05-15T20:17:34.450Z_

<details><summary>↩ Tool result · `toolu_0164LJboAtqPMJPdbf5ZQRzu`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "41ae69e4-eaa7-4f53-bbd0-dd179b4a28d6"
}
```

</details>

---

### Tool call

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YMh96uuoHtNbRQEngshYuC`</summary>

```json
{
  "query": "RobustVLA arXiv 2511.01331 Jacobian regularization reinforcement learning VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "04bc58ae-344c-4080-a06e-c5691bc60f6d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016bzvej3eJDnSFrENmWgDSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELh3M242SBhuJzxbGPzUyv`</summary>

```json
{
  "query": "SRPO Self-Referential Policy Optimization arXiv 2511.15605 VLA reinforcement learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "436dc040-8303-4353-8026-3204d1c6fbb5",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016bzvej3eJDnSFrENmWgDSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AE8wBJQGi5netJNavYoLJQ`</summary>

```json
{
  "query": "DiG-Flow Discrepancy-Guided Flow Matching arXiv 2512.01715 robust VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "cccca4e8-eaec-4dc6-8b50-b9308851fc04",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016bzvej3eJDnSFrENmWgDSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MZqUAmoXKhHJHwKjyhibyr`</summary>

```json
{
  "query": "On-the-Fly VLA Adaptation Test-Time Reinforcement Learning arXiv 2601.06748"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6e72f32c-b552-4a45-bd40-687c4867220b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016bzvej3eJDnSFrENmWgDSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011oZvM6Fv6rwTc3hvNn3xTE`</summary>

```json
{
  "query": "LIBERO-Plus robustness analysis vision-language-action models arXiv 2510.13626"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "f8b065ba-37d2-4ffe-b443-a05ba3052ee6",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_016bzvej3eJDnSFrENmWgDSq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Agent · `toolu_01L86JccRo9WBFQiZfrovSAF`</summary>

```json
{
  "description": "Verify conformal prediction citations",
  "prompt": "You need to verify method attribution accuracy for 6 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. braun2025cgs** (arXiv: 2507.20941)\nTitle: \"Multivariate Standardized Residuals for Conformal Prediction\"\nAuthors: Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach\nPaper claims: \"Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance\"\n\n**2. zhao2024conformalized** (RSS 2024)\nTitle: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\nAuthors: Michelle Zhao, Reid Simmons, Henny Admoni, Andrea Bajcsy\nPaper claims: \"uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review\"\n\n**3. wang2025cploop** (arXiv: 2510.16376)\nTitle: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\nAuthors: Han Wang, Chao Ning\nPaper claims: \"integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty\"\n\n**4. zhou2025acp_cbf** (ICRA 2025, arXiv: 2503.17678)\nTitle: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nAuthors: Zetian Zhou, Shuo Yang, Wenhao Luo\nPaper claims: \"combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies\"\n\n**5. gu2025safe** (NeurIPS 2025)\nTitle: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\nAuthors: Qiao Gu et al.\nPaper claims: \"trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected\"\n\n**6. zollo2025vla_calibration** (arXiv: 2507.17383)\nTitle: \"Confidence Calibration in Vision-Language-Action Models\"\nAuthors: Matteo Zollo, Richard Zemel\nPaper claims: \"first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks\"\n\nSearch for each paper and verify the method descriptions.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e5191f41-ea81-42bf-b8a1-5a94990787e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### System

_source line 69_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Verify conformal prediction citations",
  "task_type": "local_agent",
  "prompt": "You need to verify method attribution accuracy for 6 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. braun2025cgs** (arXiv: 2507.20941)\nTitle: \"Multivariate Standardized Residuals for Conformal Prediction\"\nAuthors: Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach\nPaper claims: \"Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance\"\n\n**2. zhao2024conformalized** (RSS 2024)\nTitle: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\nAuthors: Michelle Zhao, Reid Simmons, Henny Admoni, Andrea Bajcsy\nPaper claims: \"uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review\"\n\n**3. wang2025cploop** (arXiv: 2510.16376)\nTitle: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\nAuthors: Han Wang, Chao Ning\nPaper claims: \"integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty\"\n\n**4. zhou2025acp_cbf** (ICRA 2025, arXiv: 2503.17678)\nTitle: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nAuthors: Zetian Zhou, Shuo Yang, Wenhao Luo\nPaper claims: \"combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies\"\n\n**5. gu2025safe** (NeurIPS 2025)\nTitle: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\nAuthors: Qiao Gu et al.\nPaper claims: \"trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected\"\n\n**6. zollo2025vla_calibration** (arXiv: 2507.17383)\nTitle: \"Confidence Calibration in Vision-Language-Action Models\"\nAuthors: Matteo Zollo, Richard Zemel\nPaper claims: \"first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks\"\n\nSearch for each paper and verify the method descriptions.",
  "uuid": "49c2526b-25ea-435a-9c22-7cb05c15b392",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

## Round 3

21 recorded events

### User

_source line 70 · 2026-05-15T20:17:41.788Z_

You need to verify method attribution accuracy for 6 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.

**1. braun2025cgs** (arXiv: 2507.20941)
Title: "Multivariate Standardized Residuals for Conformal Prediction"
Authors: Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach
Paper claims: "Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance"

**2. zhao2024conformalized** (RSS 2024)
Title: "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions"
Authors: Michelle Zhao, Reid Simmons, Henny Admoni, Andrea Bajcsy
Paper claims: "uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review"

**3. wang2025cploop** (arXiv: 2510.16376)
Title: "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization"
Authors: Han Wang, Chao Ning
Paper claims: "integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty"

**4. zhou2025acp_cbf** (ICRA 2025, arXiv: 2503.17678)
Title: "Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning"
Authors: Zetian Zhou, Shuo Yang, Wenhao Luo
Paper claims: "combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies"

**5. gu2025safe** (NeurIPS 2025)
Title: "SAFE: Multitask Failure Detection for Vision-Language-Action Models"
Authors: Qiao Gu et al.
Paper claims: "trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected"

**6. zollo2025vla_calibration** (arXiv: 2507.17383)
Title: "Confidence Calibration in Vision-Language-Action Models"
Authors: Matteo Zollo, Richard Zemel
Paper claims: "first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks"

Search for each paper and verify the method descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "f1ca5015-53fb-4857-be1c-d0ad96716c6b"
}
```

</details>

---

### System

_source line 71_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Verify conformal prediction citations",
  "usage": {
    "total_tokens": 14682,
    "tool_uses": 1,
    "duration_ms": 2898
  },
  "last_tool_name": "ToolSearch",
  "uuid": "c91bf5f7-c7bb-4a9c-9fcc-b9048bc6ebd8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 72_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA 2604.16677 CQR conformal quantile regres…",
  "usage": {
    "total_tokens": 20023,
    "tool_uses": 6,
    "duration_ms": 23248
  },
  "last_tool_name": "WebSearch",
  "uuid": "b96f2108-ad48-4a7c-96ee-aec6137ae30a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 73_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for SC-VLA 2602.21633 reinforcement learning residual…",
  "usage": {
    "total_tokens": 20024,
    "tool_uses": 7,
    "duration_ms": 23554
  },
  "last_tool_name": "WebSearch",
  "uuid": "b0de67f2-6891-46b6-b4a2-daf10cf1b88c",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 74_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Braun Berta Jordan Bach \"Multivariate Standardize…",
  "usage": {
    "total_tokens": 16127,
    "tool_uses": 2,
    "duration_ms": 6508
  },
  "last_tool_name": "WebSearch",
  "uuid": "1436381d-797a-4601-982b-f25e2f12298c",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 75_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Zhao Simmons Admoni Bajcsy \"Conformalized Teleope…",
  "usage": {
    "total_tokens": 16130,
    "tool_uses": 3,
    "duration_ms": 7272
  },
  "last_tool_name": "WebSearch",
  "uuid": "36657d30-003c-46c3-9f5a-f3b6205d614d",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 76_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Wang Ning \"Conformal Prediction in The Loop\" traj…",
  "usage": {
    "total_tokens": 16133,
    "tool_uses": 4,
    "duration_ms": 8018
  },
  "last_tool_name": "WebSearch",
  "uuid": "7bf38212-c916-4106-a9dd-38de0b4f5140",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 77_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0156SqMwYXmjDjhqvhYW5rNa`</summary>

```json
{
  "query": "ReconVLA 2604.16677 CQR conformal quantile regression action selection method site:arxiv.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2c9134a6-b7a7-4d27-a70d-7a35790f3d1c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQvESC5mn6HDXXv7cQWF7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3852,
      "cache_read_input_tokens": 16119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3852,
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

### Tool call

_source line 78_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Lnhc98qgH3Czd5rr78hBJo`</summary>

```json
{
  "query": "SC-VLA 2602.21633 reinforcement learning residual correction training method sparse world imagination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "c8cc6720-1f58-47fc-92f7-761c31255b5b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VQvESC5mn6HDXXv7cQWF7p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3852,
      "cache_read_input_tokens": 16119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3852,
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

_source line 79 · 2026-05-15T20:17:45.001Z_

<details><summary>↩ Tool result · `toolu_01YMh96uuoHtNbRQEngshYuC`</summary>

```text
Web search results for query: "RobustVLA arXiv 2511.01331 Jacobian regularization reinforcement learning VLA"

Links: [{"title":"[2511.01331] RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.01331"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"},{"title":"1 Introduction","url":"https://arxiv.org/html/2511.01331v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/397231717_RobustVLA_Robustness-Aware_Reinforcement_Post-Training_for_Vision-Language-Action_Models"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=9g7UXLqD4B"},{"title":"Robust Learning with Jacobian Regularization","url":"https://arxiv.org/pdf/1908.02729"},{"title":"[1908.02729] Robust Learning with Jacobian Regularization","url":"https://arxiv.org/abs/1908.02729"},{"title":"Robust Learning with Jacobian Regularization - ADS","url":"https://ui.adsabs.harvard.edu/abs/2019arXiv190802729H/abstract"},{"title":"Robust Learning with Jacobian Regularization | OpenReview","url":"https://openreview.net/forum?id=ryl-RTEYvB"},{"title":"Jump-Start Reinforcement Learning with Vision-Language-Action Regularization","url":"https://arxiv.org/html/2604.13733"}]

Based on the search results, here's what I found about RobustVLA (arXiv 2511.01331):

## Overview

RobustVLA is a lightweight online RL post-training method designed to explicitly enhance the resilience of VLA models. Vision-Language-Action (VLA) models have emerged as powerful general-purpose policies for robotic manipulation, but often fail to generalize reliably in out-of-distribution deployments where disturbances such as observation noise, sensor errors, or actuation perturbations become prevalent.

## Key Contributions

Through a systematic robustness analysis, the paper identifies two key regularizations: Jacobian regularization, which mitigates sensitivity to observation noise, and smoothness regularization, which stabilizes policies under action perturbations.

The robustness gap under observation perturbations is governed by the Jacobian sensitivity of the VLA model, whereas under action perturbations it is controlled by the smoothness of the VLA model update. This theoretical insight motivates the introduction of Jacobian and smoothness regularization into the online RL fine-tuning process, which together constrain the worst-case robustness gap and promote robust decision-making.

## Theoretical Analysis

The paper includes theoretical analysis with error amplification bounds under observation perturbations that relate to model Jacobian sensitivity, return drift control under action noise exploring the relationship between return gap and cumulative model drift, and robust stability guarantees in combined settings involving both observation and action perturbations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "0e6cf603-ed64-4d4b-9e49-d8918a49b3a3"
}
```

</details>

---

### Tool result

_source line 80 · 2026-05-15T20:17:46.490Z_

<details><summary>↩ Tool result · `toolu_01ELh3M242SBhuJzxbGPzUyv`</summary>

```text
Web search results for query: "SRPO Self-Referential Policy Optimization arXiv 2511.15605 VLA reinforcement learning"

Links: [{"title":"[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15605v2"},{"title":"Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.15605v1"},{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"},{"title":"[2506.01713v1] SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning","url":"https://arxiv.org/abs/2506.01713v1"},{"title":"SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning","url":"https://arxiv.org/html/2506.01713v1"},{"title":"[2506.01713] SRPO: Enhancing Multimodal LLM Reasoning via Reflection-Aware Reinforcement Learning","url":"https://arxiv.org/abs/2506.01713"}]

I've successfully found information about SRPO (Self-Referential Policy Optimization) from arXiv paper 2511.15605. Here's a summary of the key findings:

## SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models

SRPO is a novel framework for Vision-Language-Action (VLA) models designed to overcome the constraints of heavy reliance on expert demonstrations, which leads to demonstration bias and limiting performance.

### Core Problem and Solution

Current VLA-RL methods, including group-based optimization approaches, are hindered by severe reward sparsity, with reliance on binary success indicators wasting valuable information in failed trajectories and resulting in low training efficiency. 

To solve this, SRPO eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference.

### Key Technical Innovation

A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, the method utilizes compressed, transferable encodings from a world model's latent space that naturally capture progress patterns across environments.

### Performance Results

On the LIBERO benchmark, SRPO achieves a state-of-the-art success rate of 99.2% in just 200 RL steps, starting from a supervised baseline with 48.9% success, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "0d0dbf92-58ab-44f7-8163-a1de6ba5142b"
}
```

</details>

---

### Tool result

_source line 81 · 2026-05-15T20:17:46.908Z_

<details><summary>↩ Tool result · `toolu_01AE8wBJQGi5netJNavYoLJQ`</summary>

```text
Web search results for query: "DiG-Flow Discrepancy-Guided Flow Matching arXiv 2512.01715 robust VLA"

Links: [{"title":"BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/abs/2512.01715"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/html/2512.01715v1"},{"title":"DiG-Flow","url":"https://beingbeyond.github.io/DiG-Flow/"},{"title":"GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://github.com/BeingBeyond/DiG-Flow"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models - Takara TLDR | Takara TLDR","url":"https://tldr.takara.ai/p/2512.01715"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"[Quick Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://liner.com/review/digflow-discrepancyguided-flow-matching-for-robust-vla-models"},{"title":"[Literature Review] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://www.themoonlight.io/en/review/dig-flow-discrepancy-guided-flow-matching-for-robust-vla-models"},{"title":"[2506.02070] An Introduction to Flow Matching and Diffusion Models","url":"https://arxiv.org/abs/2506.02070"}]

Based on the search results, here's what I found about DiG-Flow:

## DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models

DiG-Flow is a principled framework that enhances VLA (Vision-Language-Action) robustness through geometric regularization.

### Key Innovation

The key insight is that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment.

### How It Works

DiG-Flow is a plug-and-play module for flow-matching based VLAs that rebalances control between the autoregressive foundation model and the flow expert, embedding model inputs and flow outputs into a unified discrepancy space and using this signal to gate the flow path to prevent shortcut transports.

### Performance Benefits

DiG-Flow integrates into existing VLA architectures with negligible overhead and consistently improves performance, with particularly pronounced gains on complex multi-step tasks and under limited training data. DiG-Flow integrates seamlessly into diverse VLA architectures, including π, GR00T, and Being-H.

### Theoretical Grounding

The paper provides theoretical guarantees showing that discrepancy-guided training provably decreases the training objective, and that guided inference refinement converges with contraction.

The paper was submitted to arXiv on December 1, 2025, with the identifier 2512.01715.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "14a50a0c-31ab-4585-8136-4d0af38bac51"
}
```

</details>

---

### Tool result

_source line 82 · 2026-05-15T20:17:48.515Z_

<details><summary>↩ Tool result · `toolu_011oZvM6Fv6rwTc3hvNn3xTE`</summary>

```text
Web search results for query: "LIBERO-Plus robustness analysis vision-language-action models arXiv 2510.13626"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v1"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2510.13626v1] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626v1"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"[Literature Review] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/libero-plus-in-depth-robustness-analysis-of-vision-language-action-models"},{"title":"LIBERO-X: Robustness Litmus for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.06556v1"}]

I found comprehensive information about the LIBERO-Plus paper (arXiv 2510.13626). Here's what the research reveals:

## Overview

Visual-Language-Action (VLA) models report impressive success rates on robotic manipulation benchmarks, yet these results may mask fundamental weaknesses in robustness.

## Methodology

The researchers perform a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Key Findings

Models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Surprisingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

Additional findings include models exhibit a reliance on superficial visual cues, such as positional bias, rather than a genuine semantic understanding of task-relevant objects.

## The Tool

LIBERO-plus is a generalized benchmark for in-depth robustness analysis of vision-language-action models. The official repository is available on GitHub at sylvestf/LIBERO-plus.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "53dc83f7-038b-4967-8bf1-c341cbccd25a"
}
```

</details>

---

### Tool result

_source line 83 · 2026-05-15T20:17:48.951Z_

<details><summary>↩ Tool result · `toolu_01MZqUAmoXKhHJHwKjyhibyr`</summary>

```text
Web search results for query: "On-the-Fly VLA Adaptation Test-Time Reinforcement Learning arXiv 2601.06748"

Links: [{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"[2601.06748] On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.06748"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning | Request PDF","url":"https://www.researchgate.net/publication/399707107_On-the-Fly_VLA_Adaptation_via_Test-Time_Reinforcement_Learning"},{"title":"Test-Time RL for VLAs","url":"https://www.emergentmind.com/topics/test-time-reinforcement-learning-for-vlas-tt-vla"},{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement ...","url":"https://www.semanticscholar.org/paper/On-the-Fly-VLA-Adaptation-via-Test-Time-Learning-Liu-Liu/bc8fdd096876e0d46ae8411fe1610f3c85e045e3"},{"title":"Retrieve-then-Steer: Online Success Memory for Test-Time Adaptation of Generative VLAs","url":"https://arxiv.org/html/2605.10094v2"},{"title":"AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.14148v1"},{"title":"EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.14666v1"},{"title":"Test-Time Adaptation for Online Vision-Language Navigation with Feedback-based Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=K4GaB4fdIq"}]

I found the research paper you were looking for. Here's what I found:

## On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning

This paper was submitted on January 11, 2026 (with a most recent revision on April 7, 2026) and has authors including Changyu Liu, Yiyang Liu, Taowen Wang, and others.

**Overview:**

Vision-Language-Action models have emerged as a powerful paradigm for general-purpose robot learning, enabling agents to map visual observations and natural-language instructions into executable robotic actions. Though popular, they are primarily trained via supervised fine-tuning or training-time reinforcement learning, requiring explicit fine-tuning phases, human interventions, or controlled data collection. Consequently, existing methods remain unsuitable for challenging simulated- or physical-world deployments, where robots must respond autonomously and flexibly to evolving environments.

**The Proposed Solution:**

To address this limitation, the authors introduce a Test-Time Reinforcement Learning for VLAs (TT-VLA), a framework that enables on-the-fly policy adaptation during inference. TT-VLA formulates a dense reward mechanism that leverages step-by-step task-progress signals to refine action policies during test time while preserving the SFT/RL-trained priors.

**Results:**

Empirical results show that their approach enhances overall adaptability, stability, and task success in dynamic, previously unseen scenarios under simulated and real-world settings.

The full paper is available on arXiv at [arxiv.org/abs/2601.06748](https://arxiv.org/abs/2601.06748).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a0c0ac73-3012-4b82-b215-60f3acc18ce4"
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Ams28AMN9zxCSNd1Qbu7Rr`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "dca10bc3-97f5-4259-93df-309644a15576",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_011zr3qDTpf3MXYqdu8amwAy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6528,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6528,
        "ephemeral_1h_input_tokens": 0
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

_source line 85 · 2026-05-15T20:17:44.691Z_

<details><summary>↩ Tool result · `toolu_01Ams28AMN9zxCSNd1Qbu7Rr`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "ce58f702-7c6c-482e-a72d-c13427729750"
}
```

</details>

---

### Tool call

_source line 86_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ssj1jKDgehpottH5u9MzGc`</summary>

```json
{
  "query": "Braun Berta Jordan Bach \"Multivariate Standardized Residuals for Conformal Prediction\" arXiv 2507.20941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "fa972801-b00a-4c5e-838e-7fe2e3de4b43",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H9nKokk9mxLhDY38e4pQ5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RphzKT7m2ZBKQLvChyibwv`</summary>

```json
{
  "query": "Zhao Simmons Admoni Bajcsy \"Conformalized Teleoperation\" RSS 2024 conformal prediction robot actions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6637d09e-d894-41bb-9244-a11e0a52791c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H9nKokk9mxLhDY38e4pQ5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 88_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GsKRLgtFzCHhAckVqHJGMZ`</summary>

```json
{
  "query": "Wang Ning \"Conformal Prediction in The Loop\" trajectory optimization arXiv 2510.16376"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "859b0e8c-7294-4a13-ad7f-29dd70f9b1cf",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01H9nKokk9mxLhDY38e4pQ5g",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14646,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Agent · `toolu_019JGFjdzV7p1jtKiKLHkHpd`</summary>

```json
{
  "description": "Verify residual policy + UQ citations",
  "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. silver2018residual** (RSS 2018, arXiv: 1812.06298)\nTitle: \"Residual Policy Learning\"\nAuthors: Tom Silver, Kelsey Allen, Josh Tenenbaum, Leslie Kaelbling\nPaper claims:\n- \"introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy\"\n- \"introduced bounded residual corrections for combining learned and classical controllers\"\n\n**2. jiang2024transic** (CoRL 2024, arXiv: 2405.10315)\nTitle: \"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction\"\nAuthors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei\nPaper claims:\n- \"uses learned binary gating to selectively apply residual actions across different task phases\"\n- \"uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse\"\n\n**3. xiao2026pld** (ICLR 2026, arXiv: 2511.00091)\nTitle: \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\"\nPaper claims:\n- \"schedules magnitude bounds during training\"\n- \"introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training\"\nNote: The paper title in the bib says \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\" but cited as \"PLD\" in text. Verify what PLD stands for and if the method description matches.\n\n**4. pan2025drc** (arXiv: 2503.15368)\nTitle: \"DRC: Decaying Relative Correction for Policy Refinement\"\nAuthors: Xinjie Pan et al.\nPaper claims: \"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n\n**5. xing2026diu** (arXiv: 2605.00941)\nTitle: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\nAuthors: Jiarui Xing, Song Wang, Jian Wang\nPaper claims: \"derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling\"\n\nSearch for each paper and verify the method descriptions.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "88da0b11-7281-40b5-b66f-a8ea2fb55306",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### System

_source line 90_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Verify residual policy + UQ citations",
  "task_type": "local_agent",
  "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. silver2018residual** (RSS 2018, arXiv: 1812.06298)\nTitle: \"Residual Policy Learning\"\nAuthors: Tom Silver, Kelsey Allen, Josh Tenenbaum, Leslie Kaelbling\nPaper claims:\n- \"introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy\"\n- \"introduced bounded residual corrections for combining learned and classical controllers\"\n\n**2. jiang2024transic** (CoRL 2024, arXiv: 2405.10315)\nTitle: \"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction\"\nAuthors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei\nPaper claims:\n- \"uses learned binary gating to selectively apply residual actions across different task phases\"\n- \"uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse\"\n\n**3. xiao2026pld** (ICLR 2026, arXiv: 2511.00091)\nTitle: \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\"\nPaper claims:\n- \"schedules magnitude bounds during training\"\n- \"introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training\"\nNote: The paper title in the bib says \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\" but cited as \"PLD\" in text. Verify what PLD stands for and if the method description matches.\n\n**4. pan2025drc** (arXiv: 2503.15368)\nTitle: \"DRC: Decaying Relative Correction for Policy Refinement\"\nAuthors: Xinjie Pan et al.\nPaper claims: \"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n\n**5. xing2026diu** (arXiv: 2605.00941)\nTitle: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\nAuthors: Jiarui Xing, Song Wang, Jian Wang\nPaper claims: \"derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling\"\n\nSearch for each paper and verify the method descriptions.",
  "uuid": "75b57a10-dfce-4339-b3b9-8ff8c830a2e6",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

## Round 4

36 recorded events

### User

_source line 91 · 2026-05-15T20:17:52.735Z_

You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.

**1. silver2018residual** (RSS 2018, arXiv: 1812.06298)
Title: "Residual Policy Learning"
Authors: Tom Silver, Kelsey Allen, Josh Tenenbaum, Leslie Kaelbling
Paper claims:
- "introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy"
- "introduced bounded residual corrections for combining learned and classical controllers"

**2. jiang2024transic** (CoRL 2024, arXiv: 2405.10315)
Title: "TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction"
Authors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei
Paper claims:
- "uses learned binary gating to selectively apply residual actions across different task phases"
- "uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse"

**3. xiao2026pld** (ICLR 2026, arXiv: 2511.00091)
Title: "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL"
Paper claims:
- "schedules magnitude bounds during training"
- "introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training"
Note: The paper title in the bib says "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL" but cited as "PLD" in text. Verify what PLD stands for and if the method description matches.

**4. pan2025drc** (arXiv: 2503.15368)
Title: "DRC: Decaying Relative Correction for Policy Refinement"
Authors: Xinjie Pan et al.
Paper claims: "applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones"

**5. xing2026diu** (arXiv: 2605.00941)
Title: "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching"
Authors: Jiarui Xing, Song Wang, Jian Wang
Paper claims: "derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling"

Search for each paper and verify the method descriptions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "fb57b0a9-2d93-4614-8895-19b4c71d1d2b"
}
```

</details>

---

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Verify residual policy + UQ citations",
  "usage": {
    "total_tokens": 14697,
    "tool_uses": 1,
    "duration_ms": 2086
  },
  "last_tool_name": "ToolSearch",
  "uuid": "07e06f67-cb77-4f42-a681-a527bf4feadc",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for SRPO 2511.15605 self-referential rollouts trainin…",
  "usage": {
    "total_tokens": 20976,
    "tool_uses": 7,
    "duration_ms": 23511
  },
  "last_tool_name": "WebSearch",
  "uuid": "90419350-c505-44a9-8895-7d57fad489db",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for DiG-Flow 2512.01715 flow matching denoising traje…",
  "usage": {
    "total_tokens": 20977,
    "tool_uses": 8,
    "duration_ms": 24338
  },
  "last_tool_name": "WebSearch",
  "uuid": "1e814be0-7a30-4dea-bb34-58f1711d9152",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "description": "Searching for LIBERO-Plus 2510.13626 distribution shift object …",
  "usage": {
    "total_tokens": 20978,
    "tool_uses": 9,
    "duration_ms": 24748
  },
  "last_tool_name": "WebSearch",
  "uuid": "9101b908-dca7-4950-8304-0f2245e2a0d6",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 96_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Zhou Yang Luo \"Adaptive Conformal Prediction with…",
  "usage": {
    "total_tokens": 19023,
    "tool_uses": 5,
    "duration_ms": 16986
  },
  "last_tool_name": "WebSearch",
  "uuid": "4b4b79e4-15da-4721-b684-c24069f70711",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 97_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for Silver Allen Tenenbaum Kaelbling \"Residual Policy…",
  "usage": {
    "total_tokens": 16142,
    "tool_uses": 2,
    "duration_ms": 6097
  },
  "last_tool_name": "WebSearch",
  "uuid": "a18c441c-ae73-4ace-83f7-df0f5ff2ea28",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Gu \"SAFE Multitask Failure Detection Vision-Langu…",
  "usage": {
    "total_tokens": 19058,
    "tool_uses": 6,
    "duration_ms": 17906
  },
  "last_tool_name": "WebSearch",
  "uuid": "3c33a590-709f-41d4-b615-853c60f70517",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA 2604.16677 \"draws multiple action sample…",
  "usage": {
    "total_tokens": 21953,
    "tool_uses": 8,
    "duration_ms": 35994
  },
  "last_tool_name": "WebSearch",
  "uuid": "50666328-55d9-4146-b861-3dfd4be2721e",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 100_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for TRANSIC \"sim-to-real policy transfer\" Jiang Wang …",
  "usage": {
    "total_tokens": 16145,
    "tool_uses": 3,
    "duration_ms": 7474
  },
  "last_tool_name": "WebSearch",
  "uuid": "798e7ee2-3111-4fdf-a4bb-babdad6ebdbb",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 101_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for SC-VLA 2602.21633 \"residual\" OR \"correction\" RL r…",
  "usage": {
    "total_tokens": 21954,
    "tool_uses": 9,
    "duration_ms": 36768
  },
  "last_tool_name": "WebSearch",
  "uuid": "836d6b6d-fb53-4619-9dd8-6a82750fe33c",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 102_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Zollo Zemel \"Confidence Calibration in Vision-Lan…",
  "usage": {
    "total_tokens": 19093,
    "tool_uses": 7,
    "duration_ms": 18718
  },
  "last_tool_name": "WebSearch",
  "uuid": "cf6d4ef6-19f4-4f2d-83b4-9a643355f452",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 103_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for \"Self-Improving Vision-Language-Action Models\" \"D…",
  "usage": {
    "total_tokens": 16148,
    "tool_uses": 4,
    "duration_ms": 8592
  },
  "last_tool_name": "WebSearch",
  "uuid": "4d8405c8-baf2-4e0e-a8aa-db38dd5c08cd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### System

_source line 104_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for VLA-Pilot 2511.14178 \"2.41s\" OR \"2.41 seconds\" pe…",
  "usage": {
    "total_tokens": 21955,
    "tool_uses": 10,
    "duration_ms": 38011
  },
  "last_tool_name": "WebSearch",
  "uuid": "9623e595-cfea-4e2f-94e5-a7e296190057",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 105 · 2026-05-15T20:17:54.733Z_

<details><summary>↩ Tool result · `toolu_01Lnhc98qgH3Czd5rr78hBJo`</summary>

```text
Web search results for query: "SC-VLA 2602.21633 reinforcement learning residual correction training method sparse world imagination"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"Paper page - RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models","url":"https://huggingface.co/papers/2602.12628"},{"title":"[2409.12917] Training Language Models to Self-Correct via Reinforcement Learning","url":"https://arxiv.org/abs/2409.12917"}]

Based on the search results, I found information about the paper you're looking for:

## Self-Correcting VLA (SC-VLA) - ArXiv 2602.21633

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

**Key Technical Components:**

The approach designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. It introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.

**Motivation:**

Standard vision-language-action (VLA) models rely on fitting statistical data priors, limiting their robust understanding of underlying physical dynamics, while reinforcement learning enhances physical grounding through exploration yet typically relies on external reward signals that remain isolated from the agent's internal states.

**Results:**

Evaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

The paper was published on February 25, 2026, and the code is available on GitHub at the repository Kisaragi0/SC-VLA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "1c505236-d096-41ce-98dc-c029abf5f563"
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-15T20:17:55.468Z_

<details><summary>↩ Tool result · `toolu_0156SqMwYXmjDjhqvhYW5rNa`</summary>

```text
Web search results for query: "ReconVLA 2604.16677 CQR conformal quantile regression action selection method site:arxiv.org"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Conformalized Quantile Regression Yaniv Romano Department of Statistics","url":"https://arxiv.org/pdf/1905.03222"},{"title":"[1905.03222] Conformalized Quantile Regression","url":"https://arxiv.org/abs/1905.03222"},{"title":"Conformal prediction for uncertainties in the neutron star equation of state","url":"https://arxiv.org/html/2604.21039"},{"title":"[2306.08693] Integrating Uncertainty Awareness into Conformalized Quantile Regression","url":"https://arxiv.org/abs/2306.08693"},{"title":"Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling","url":"https://arxiv.org/html/2601.17437"},{"title":"Density-Calibrated Conformal Quantile Regression","url":"https://arxiv.org/html/2411.19523v1"},{"title":"Conformal Quantile Regression for Probabilistic ...","url":"https://arxiv.org/pdf/2601.17437"},{"title":"Conformalized High-Density Quantile Regression via Dynamic Prototypes-based Probability Density Estimation","url":"https://arxiv.org/html/2411.01266v1"},{"title":"A Systematic Review of Conformal Inference Procedures for Treatment Effect Estimation: Methods and Challenges","url":"https://arxiv.org/html/2509.21660v1"}]

I found the arxiv paper you were searching for. Here's what I found:

## ReconVLA: Paper 2604.16677

ReconVLA (reliable conformal VLA) is an uncertainty-guided control framework that endows VLAs (Vision-Language-Action models) with calibrated uncertainty estimation and proactive failure detection.

### CQR Method for Action Selection

The paper employs CQR (Conformalized Quantile Regression) to produce a high-confidence prediction interval for each action token, combining traditional quantile regression with conformal prediction to guarantee that the true action lies within the predicted interval with a prescribed probability (e.g., 90% confidence).

### How CQR Works in ReconVLA

The authors construct a CQR model that predicts how far the VLA-generated action is expected to deviate from an expert demonstration. CQR estimates an upper quantile of the true error and then adjusts this estimate through conformal calibration to achieve reliable finite-sample coverage. The QR model provides an initial prediction of a high-percentile error value, and the conformal correction accounts for model bias and uncertainty in unseen scenarios, resulting in a calibrated bound that upper-limits the expected deviation with a specified confidence level.

### Overall Framework

ReconVLA augments the base VLA model with two uncertainty-aware components: (i) a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and (ii) an SMD-based detector that monitors latent state distributions to identify OOD or failure-prone conditions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d026cd7d-2c33-4cb4-b686-b53c741c7f5f"
}
```

</details>

---

### Tool call

_source line 107_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XN7GTnLU2r56MEHqMwqKFe`</summary>

```json
{
  "query": "ReconVLA 2604.16677 \"draws multiple action samples\" OR \"sample selection\" OR \"best candidate\" conformal scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "de4dd8dc-a92d-4571-9a88-2f86c32310aa",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ym6Uq5CHcxuZdszUJNsza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 19971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1042,
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

### Tool call

_source line 108_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TehTDMyuQZDBxz7HuZTQfP`</summary>

```json
{
  "query": "SC-VLA 2602.21633 \"residual\" OR \"correction\" RL reinforcement learning \"per-task\" OR \"task-level\" training mechanism"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "f23968c3-78e3-484b-abf1-70f7a325f938",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ym6Uq5CHcxuZdszUJNsza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 19971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1042,
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

### Tool call

_source line 109_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01427s2Esu1BTDun76EAy88M`</summary>

```json
{
  "query": "VLA-Pilot 2511.14178 \"2.41s\" OR \"2.41 seconds\" per control step latency inference time"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "70bfffac-af51-4b26-8716-182b81bbcaeb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ym6Uq5CHcxuZdszUJNsza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 19971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1042,
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

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WyPi9jeBXFqzpWG7fMTGsJ`</summary>

```json
{
  "query": "SRPO 2511.15605 self-referential rollouts training signal robustness VLA method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8658e3c6-8bed-44f2-a0c3-f3adb2db1b50",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CoU2PcZFgEXC64oDZnRiQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 4093,
      "cache_read_input_tokens": 15953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4093,
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

### Tool call

_source line 111_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018eoetP3wwoKradundhyJz8`</summary>

```json
{
  "query": "DiG-Flow 2512.01715 flow matching denoising trajectory discrepancy method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "ca6bb16d-2ce8-4496-8d48-ebdc2fedb395",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CoU2PcZFgEXC64oDZnRiQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 4093,
      "cache_read_input_tokens": 15953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4093,
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

### Tool call

_source line 112_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01T32YfkS3T5A3XsyLtCmuLs`</summary>

```json
{
  "query": "LIBERO-Plus 2510.13626 distribution shift object appearance lighting sensor noise performance degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2b0ed437-63c3-4ad2-9b66-fead8c0474dc",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01CoU2PcZFgEXC64oDZnRiQq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 876,
      "cache_creation_input_tokens": 4093,
      "cache_read_input_tokens": 15953,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4093,
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

_source line 113 · 2026-05-15T20:18:02.102Z_

<details><summary>↩ Tool result · `toolu_01T32YfkS3T5A3XsyLtCmuLs`</summary>

```text
Web search results for query: "LIBERO-Plus 2510.13626 distribution shift object appearance lighting sensor noise performance degradation"

Links: [{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"OpenMOSS LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-","url":"https://arxiv.org/pdf/2510.13626"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626"},{"title":"Sylvest/LIBERO-plus · Datasets at Hugging Face","url":"https://huggingface.co/datasets/Sylvest/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2510.13626"},{"title":"LIBERO-plus/index.html at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/index.html"},{"title":"LIBERO-plus/README.md at main · sylvestf/LIBERO-plus","url":"https://github.com/sylvestf/LIBERO-plus/blob/main/README.md"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2510.13626v2"}]

Based on the search results, here's information about LIBERO-Plus (arxiv 2510.13626):

## Overview

LIBERO-Plus is a paper on in-depth robustness analysis of Vision-Language-Action (VLA) models, authored by Senyu Fei and colleagues.

## Key Focus Areas

The research performs a systematic vulnerability analysis by introducing controlled perturbations across seven dimensions: objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures and sensor noise.

## Major Findings

The study comprehensively analyzed multiple state-of-the-art models and revealed consistent brittleness beneath apparent competence. More specifically, models exhibit extreme sensitivity to perturbation factors, including camera viewpoints and robot initial states, with performance dropping from 95% to below 30% under modest perturbations.

Interestingly, models are largely insensitive to language variations, with further experiments revealing that models tend to ignore language instructions completely.

## Conclusion

The analysis indicates that, rather than achieving true multimodal understanding, current VLA architectures rely on overfitting to specific, narrowly defined cues provided during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "539ef616-f9bf-4392-a18b-bcf8d0956652"
}
```

</details>

---

### Tool result

_source line 114 · 2026-05-15T20:17:55.191Z_

<details><summary>↩ Tool result · `toolu_01RphzKT7m2ZBKQLvChyibwv`</summary>

```text
Web search results for query: "Zhao Simmons Admoni Bajcsy "Conformalized Teleoperation" RSS 2024 conformal prediction robot actions"

Links: [{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"[2406.07767v1] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"http://arxiv.org/abs/2406.07767v1"},{"title":"dblp: Robotics: Science and Systems 2024","url":"https://dblp.org/db/conf/rss/rss2024.html"},{"title":"Conformalized Teleoperation: Confidently Mapping Human ...","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Publications | Henny Admoni","url":"https://www.hennyadmoni.com/publications/"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/8/"},{"title":"[2410.08852] Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback","url":"https://arxiv.org/abs/2410.08852"},{"title":"Accepted Papers · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/"},{"title":"Reid SIMMONS | Carnegie Mellon University, Pittsburgh | CMU | Robotics Institute | Research profile","url":"https://www.researchgate.net/profile/Reid-Simmons"}]

I found the paper you were looking for! Here's the information about the work:

## Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions

The paper "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions" was authored by Michelle Zhao, Reid Simmons, Henny Admoni, and Andrea Bajcsy, all from Carnegie Mellon University's Robotics Institute.

### Publication Details
The paper was published at Robotics: Science and Systems (RSS) in 2024, with the conference taking place July 15-19, 2024, in Delft, Netherlands.

### Research Overview
Assistive robotic arms often have more degrees-of-freedom than a human teleoperator can control with a low-dimensional input, like a joystick. The key approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.

### Methodology
The research was evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching. The authors propose an uncertainty-interval-based mechanism for detecting high-uncertainty user inputs and robot states.

The paper addresses the important problem of using conformal prediction techniques to quantify uncertainty when mapping human inputs to robot actions in assistive robotic systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8a002e42-3226-4d75-aae7-8a08250f3fb2"
}
```

</details>

---

### Tool result

_source line 115 · 2026-05-15T20:17:55.256Z_

<details><summary>↩ Tool result · `toolu_01Ssj1jKDgehpottH5u9MzGc`</summary>

```text
Web search results for query: "Braun Berta Jordan Bach "Multivariate Standardized Residuals for Conformal Prediction" arXiv 2507.20941"

Links: [{"title":"[2507.20941] Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/abs/2507.20941"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/pdf/2507.20941"},{"title":"(PDF) Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://www.researchgate.net/publication/394081259_Multivariate_Conformal_Prediction_via_Conformalized_Gaussian_Scoring"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/html/2507.20941v1"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://www.semanticscholar.org/paper/Multivariate-Standardized-Residuals-for-Conformal-Braun-Berta/facf01ce49dc3c1ba5203984238e35cc70d0bc76"},{"title":"Sacha Braun","url":"https://elsacho.github.io/"},{"title":"[PDF] Multivariate Conformal Prediction via Conformalized Gaussian Scoring | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-via-Conformalized-Braun-Berta/eb97eda6c4159d62c1fd5d2ca6404b323e44123c"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian ...","url":"https://ribbitribbit.co/paper/arxiv.2507.20941-Multivariate-Conformal-Prediction-via-Conformalized-Gaussian-Scoring"},{"title":"Publications - People @EECS","url":"https://people.eecs.berkeley.edu/~jordan/publications.html"},{"title":"Conformal and 𝑘NN Predictive Uncertainty Quantification Algorithms in Metric Spaces","url":"https://arxiv.org/html/2507.15741v1"}]

Based on the search results, I found detailed information about the paper you're looking for.

## Paper Summary

The paper "Multivariate Standardized Residuals for Conformal Prediction" is authored by Sacha Braun, Eugène Berta, Michael I. Jordan, and Francis Bach (arXiv 2507.20941).

### Main Contributions

While split conformal prediction guarantees marginal coverage, approaching the stronger property of conditional coverage is essential for reliable uncertainty quantification. Naive conformal scores, however, suffer from poor conditional coverage in heteroskedastic settings.

The paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.

Using the Mahalanobis distance induced by a learned local covariance as a non-conformity score provides a closed-form, computationally efficient mechanism for capturing inter-output correlations and heteroskedasticity, avoiding the expensive sampling required by previous methods based on cumulative distribution functions.

### Key Extensions and Results

The structure unlocks several practical extensions, including the handling of missing output values, the refinement of conformal sets when partial information is revealed, and the construction of valid conformal sets for transformations of the output.

The paper provides extensive empirical evidence on both synthetic and real-world datasets showing that the approach yields conformal sets that improve upon the conditional coverage of existing multivariate baselines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3799a757-b81a-4736-aac3-98ec0cb33b2f"
}
```

</details>

---

### Tool result

_source line 116 · 2026-05-15T20:17:55.721Z_

<details><summary>↩ Tool result · `toolu_01GsKRLgtFzCHhAckVqHJGMZ`</summary>

```text
Web search results for query: "Wang Ning "Conformal Prediction in The Loop" trajectory optimization arXiv 2510.16376"

Links: [{"title":"[2510.16376] Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/abs/2510.16376"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://arxiv.org/html/2510.16376v1"},{"title":"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=lg51XnHt2H"},{"title":"Ning Research Group - Publications","url":"https://www.docu-lab.org/publications"},{"title":"Conformal Prediction in The Loop: A Feedback-Based ...","url":"https://www.researchgate.net/publication/396714858_Conformal_Prediction_in_The_Loop_A_Feedback-Based_Uncertainty_Model_for_Trajectory_Optimization"},{"title":"NeurIPS Poster Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization","url":"https://neurips.cc/virtual/2025/poster/116267"},{"title":"Han Wang","url":"https://scholar.google.com/citations?user=wEmfGAYAAAAJ&hl=en&oi=sra"},{"title":"End-to-End Conformal Prediction for Trajectory Optimization | OpenReview","url":"https://openreview.net/forum?id=ilcsm8B7Pe"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://arxiv.org/html/2508.13362v1"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"}]

Based on the search results, I found the paper you're looking for. Here are the key details:

**Paper:** Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization

**Authors:** Han Wang and Chao Ning

**arXiv ID:** 2510.16376 (submitted October 18, 2025)

**Main Contribution:** The paper proposes a novel Feedback-Based CP (Fb-CP) framework for shrinking-horizon trajectory optimization with a joint risk constraint over the entire mission time.

**Key Problem Addressed:** Existing methods predominantly employ a sequential scheme, where decisions rely unidirectionally on the prediction regions, and consequently the information from decision-making fails to be fed back to instruct CP.

**Background:** Conformal Prediction (CP) is a powerful statistical machine learning tool to construct uncertainty sets with coverage guarantees, which has fueled its extensive adoption in generating prediction regions for decision-making tasks, e.g., Trajectory Optimization (TO) in uncertain environments.

The paper has also been accepted to The Thirty-ninth Annual Conference on Neural Information Processing Systems (NeurIPS).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "1c529453-176c-455e-8900-c2131098ecee"
}
```

</details>

---

### Tool call

_source line 117_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019zdy4osvbQGP4dN6csrQhi`</summary>

```json
{
  "query": "Zhou Yang Luo \"Adaptive Conformal Prediction with Control Barrier Functions\" safe reinforcement learning ICRA 2025 arXiv 2503.17678"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b4562f0c-3647-4a5a-828e-5bf9871870eb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DJdbPUHKNfRuqsc9xVdzM4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 16085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2857,
        "ephemeral_1h_input_tokens": 0
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

### Tool call

_source line 118_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q5N2HPwHNaNueUSuNEGTML`</summary>

```json
{
  "query": "Gu \"SAFE Multitask Failure Detection Vision-Language-Action Models\" NeurIPS 2025 conformal prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3f8a7895-699f-45ef-a9ef-1eed455427fe",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DJdbPUHKNfRuqsc9xVdzM4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 16085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2857,
        "ephemeral_1h_input_tokens": 0
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

### Tool call

_source line 119_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UmqkPnRfDwNdQbMghR2yvi`</summary>

```json
{
  "query": "Zollo Zemel \"Confidence Calibration in Vision-Language-Action Models\" arXiv 2507.17383"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "34848a9d-cf87-49b4-a203-1011c7f1f2eb",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01DJdbPUHKNfRuqsc9xVdzM4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2857,
      "cache_read_input_tokens": 16085,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2857,
        "ephemeral_1h_input_tokens": 0
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

### Tool call

_source line 120_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015VBkSsNgr4jKQwyJ6D4ZgK`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b63596bf-1289-49cf-afa9-0e9bd4554390",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015q4d81wwEP8YqsmNn41GAj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6542,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6542,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
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

_source line 121 · 2026-05-15T20:17:54.827Z_

<details><summary>↩ Tool result · `toolu_015VBkSsNgr4jKQwyJ6D4ZgK`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "63cd87df-55ab-4bc7-bdc2-6adfb140857d"
}
```

</details>

---

### Tool call

_source line 122_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P7FHKfFJNJFDy2UBSfrYGb`</summary>

```json
{
  "query": "Silver Allen Tenenbaum Kaelbling \"Residual Policy Learning\" arXiv 1812.06298 RSS 2018 zero-initialization bounded corrections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8b176ae5-1f0f-420b-b6b4-5f8bc2a8dcbf",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014mwQG8cN9a1jVkz7bu4UwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 123_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PL4uD6H2VnvFUQE5bWGGE9`</summary>

```json
{
  "query": "TRANSIC \"sim-to-real policy transfer\" Jiang Wang Zhang Wu Fei-Fei arXiv 2405.10315 binary gate residual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "1c4563f9-1a9a-40e0-91a3-664a286dcb4e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014mwQG8cN9a1jVkz7bu4UwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 124_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cdp9eaK9QGHsy68BbRrBuL`</summary>

```json
{
  "query": "\"Self-Improving Vision-Language-Action Models\" \"Data Generation via Residual RL\" arXiv 2511.00091 PLD scheduled magnitude bound"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "70c0c88d-4a59-4bb5-b029-29bf307b099e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014mwQG8cN9a1jVkz7bu4UwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Agent · `toolu_017WkxnZx3dim1JbwEHs2DP8`</summary>

```json
{
  "description": "Verify foundational/base citations",
  "prompt": "You need to verify method attribution accuracy for 7 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. black2024pi0** (arXiv: 2410.24164)\nTitle: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\"\nPaper claims: VLAs that \"generate actions via flow matching\"\n\n**2. shukor2025smolvla** (arXiv: 2506.01844)\nTitle: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\nPaper claims: \"a 450M-parameter flow-matching VLA\"\n\n**3. liu2023libero** (NeurIPS 2023)\nTitle: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\nPaper claims: \"standard manipulation benchmarks such as LIBERO\" - used as a benchmark for evaluation\n\n**4. lipman2023flow** (ICLR 2023)\nTitle: \"Flow Matching for Generative Modeling\"\nAuthors: Yaron Lipman et al.\nPaper claims: foundational flow matching method; VLA \"generates actions via learned flow matching\"\n\n**5. ledoit2004well** (Journal of Multivariate Analysis, 2004)\nTitle: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\nAuthors: Olivier Ledoit, Michael Wolf\nPaper claims: Ledoit-Wolf shrinkage covariance estimation; \"analytically optimal shrinkage intensity\"\n\n**6. ross2011dagger** (AISTATS 2011)\nTitle: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\nAuthors: Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell\nPaper claims: cited for \"compounding distribution shift\" / \"compounding error problem in imitation learning\"\n\n**7. angelopoulos2023gentle** (arXiv: 2107.07511)\nTitle: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\nAuthors: Anastasios N. Angelopoulos, Stephen Bates\nPaper claims: \"Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability\"\n\nSearch for each paper and verify the method descriptions. These are mostly foundational/well-known papers so quick verification should suffice.",
  "model": "sonnet"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8ae73afa-6279-4693-966b-1b8f9701bf4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G4KSPBf6LLNXNf2FQNvz6i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2319,
      "cache_read_input_tokens": 45929,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2319
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

### System

_source line 126_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Verify foundational/base citations",
  "task_type": "local_agent",
  "prompt": "You need to verify method attribution accuracy for 7 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. black2024pi0** (arXiv: 2410.24164)\nTitle: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\"\nPaper claims: VLAs that \"generate actions via flow matching\"\n\n**2. shukor2025smolvla** (arXiv: 2506.01844)\nTitle: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\nPaper claims: \"a 450M-parameter flow-matching VLA\"\n\n**3. liu2023libero** (NeurIPS 2023)\nTitle: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\nPaper claims: \"standard manipulation benchmarks such as LIBERO\" - used as a benchmark for evaluation\n\n**4. lipman2023flow** (ICLR 2023)\nTitle: \"Flow Matching for Generative Modeling\"\nAuthors: Yaron Lipman et al.\nPaper claims: foundational flow matching method; VLA \"generates actions via learned flow matching\"\n\n**5. ledoit2004well** (Journal of Multivariate Analysis, 2004)\nTitle: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\nAuthors: Olivier Ledoit, Michael Wolf\nPaper claims: Ledoit-Wolf shrinkage covariance estimation; \"analytically optimal shrinkage intensity\"\n\n**6. ross2011dagger** (AISTATS 2011)\nTitle: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\nAuthors: Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell\nPaper claims: cited for \"compounding distribution shift\" / \"compounding error problem in imitation learning\"\n\n**7. angelopoulos2023gentle** (arXiv: 2107.07511)\nTitle: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\nAuthors: Anastasios N. Angelopoulos, Stephen Bates\nPaper claims: \"Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability\"\n\nSearch for each paper and verify the method descriptions. These are mostly foundational/well-known papers so quick verification should suffice.",
  "uuid": "a9bd1796-4d05-4ae6-9380-ff74ad17bc1c",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

## Round 5

149 recorded events

### User

_source line 127 · 2026-05-15T20:18:02.344Z_

You need to verify method attribution accuracy for 7 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.

**1. black2024pi0** (arXiv: 2410.24164)
Title: "π₀: A Vision-Language-Action Flow Model for General Robot Control"
Paper claims: VLAs that "generate actions via flow matching"

**2. shukor2025smolvla** (arXiv: 2506.01844)
Title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
Paper claims: "a 450M-parameter flow-matching VLA"

**3. liu2023libero** (NeurIPS 2023)
Title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
Paper claims: "standard manipulation benchmarks such as LIBERO" - used as a benchmark for evaluation

**4. lipman2023flow** (ICLR 2023)
Title: "Flow Matching for Generative Modeling"
Authors: Yaron Lipman et al.
Paper claims: foundational flow matching method; VLA "generates actions via learned flow matching"

**5. ledoit2004well** (Journal of Multivariate Analysis, 2004)
Title: "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices"
Authors: Olivier Ledoit, Michael Wolf
Paper claims: Ledoit-Wolf shrinkage covariance estimation; "analytically optimal shrinkage intensity"

**6. ross2011dagger** (AISTATS 2011)
Title: "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning"
Authors: Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell
Paper claims: cited for "compounding distribution shift" / "compounding error problem in imitation learning"

**7. angelopoulos2023gentle** (arXiv: 2107.07511)
Title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
Authors: Anastasios N. Angelopoulos, Stephen Bates
Paper claims: "Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability"

Search for each paper and verify the method descriptions. These are mostly foundational/well-known papers so quick verification should suffice.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "082a1c38-7e8a-427d-8e80-085399c16766"
}
```

</details>

---

### System

_source line 128_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for A2C2 2509.23224 \"jointly\" OR \"joint training\" OR …",
  "usage": {
    "total_tokens": 21956,
    "tool_uses": 11,
    "duration_ms": 38647
  },
  "last_tool_name": "WebSearch",
  "uuid": "f15379bd-f724-4da8-9568-87291484bfcf",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 129_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0195wet5TjfiDcGWRUC36WVs`</summary>

```json
{
  "query": "A2C2 2509.23224 \"jointly\" OR \"joint training\" OR \"frozen\" base VLA correction head training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "34eb3f04-5cad-4145-b198-ceec8971e320",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019ym6Uq5CHcxuZdszUJNsza",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 886,
      "cache_creation_input_tokens": 1042,
      "cache_read_input_tokens": 19971,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1042,
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

_source line 130 · 2026-05-15T20:18:03.653Z_

<details><summary>↩ Tool result · `toolu_01WyPi9jeBXFqzpWG7fMTGsJ`</summary>

```text
Web search results for query: "SRPO 2511.15605 self-referential rollouts training signal robustness VLA method details"

Links: [{"title":"[2511.15605] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/abs/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.15605v1"},{"title":"Paper page - SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://huggingface.co/papers/2511.15605"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.15605v1"},{"title":"[Literature Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/srpo-self-referential-policy-optimization-for-vision-language-action-models"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models | Request PDF","url":"https://www.researchgate.net/publication/397780691_SRPO_Self-Referential_Policy_Optimization_for_Vision-Language-Action_Models"},{"title":"[Quick Review] SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://liner.com/review/srpo-selfreferential-policy-optimization-for-visionlanguageaction-models"},{"title":"SRPO Code Implementation Explained — siiRL documentation","url":"https://siirl.readthedocs.io/en/latest/programming_guide/srpo_code_explained.html"},{"title":"Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing","url":"https://arxiv.org/html/2604.02288v1"},{"title":"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models","url":"https://arxiv.org/html/2511.01331"}]

Based on the search results, here are the details about SRPO (Self-Referential Policy Optimization) 2511.15605:

## Overview

SRPO is a novel VLA-RL framework that eliminates the need for external demonstrations or manual reward engineering by leveraging the model's own successful trajectories, generated within the current training batch, as a self-reference.

## Key Method Details

**Self-Referential Rollouts:** SRPO assigns a progress-wise reward to failed attempts. Rather than relying on sparse binary success signals, relying on binary success indicators wastes valuable information in failed trajectories, resulting in low training efficiency.

**Training Signal & Robustness:** A core innovation is the use of latent world representations to measure behavioral progress robustly. Instead of relying on raw pixels or requiring domain-specific fine-tuning, the method utilizes the compressed, transferable encodings from a world model's latent space, which naturally capture progress patterns across environments, enabling accurate, generalized trajectory comparison.

## Performance Results

Starting from a supervised baseline with 48.9% success, SRPO achieves a new state-of-the-art success rate of 99.2% in just 200 RL steps, representing a 103% relative improvement without any extra supervision. Furthermore, SRPO shows substantial robustness, achieving a 167% performance improvement on the LIBERO-Plus benchmark.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6c69bcea-a7c0-4b99-a912-56678c3e7d56"
}
```

</details>

---

### System

_source line 131_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Verify foundational/base citations",
  "usage": {
    "total_tokens": 14623,
    "tool_uses": 1,
    "duration_ms": 2083
  },
  "last_tool_name": "ToolSearch",
  "uuid": "b7658c04-2c6a-483a-85f5-9a0655a04b32",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01JH5hUURi84okbC1BjT61QB`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "c89229aa-d30f-43d3-b2d3-a09d1e81d2c1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01J8QApRFWQ2WpboyrZ5tETv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 6469,
      "cache_read_input_tokens": 8118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6469,
        "ephemeral_1h_input_tokens": 0
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

_source line 133 · 2026-05-15T20:18:04.436Z_

<details><summary>↩ Tool result · `toolu_01JH5hUURi84okbC1BjT61QB`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "de283803-9ff4-44ed-9820-66508e941040"
}
```

</details>

---

### Tool result

_source line 134 · 2026-05-15T20:18:04.644Z_

<details><summary>↩ Tool result · `toolu_019zdy4osvbQGP4dN6csrQhi`</summary>

```text
Web search results for query: "Zhou Yang Luo "Adaptive Conformal Prediction with Control Barrier Functions" safe reinforcement learning ICRA 2025 arXiv 2503.17678"

Links: [{"title":"[2407.03569] Safety-Critical Control with Uncertainty Quantification using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2407.03569"},{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"},{"title":"Safety-Critical Control with Uncertainty Quantification using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2407.03569"},{"title":"CONDITIONAL CONFORMAL RISK ADAPTATION Rui Luo Department of Systems Engineering","url":"https://arxiv.org/pdf/2504.07611"},{"title":"CPED-NCBFs: A Conformal Prediction for Expert Demonstration-based Neural Control Barrier Functions - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250715022M/abstract"},{"title":"(PDF) CPED-NCBFs: A Conformal Prediction for Expert Demonstration-based Neural Control Barrier Functions","url":"https://www.researchgate.net/publication/393890396_CPED-NCBFs_A_Conformal_Prediction_for_Expert_Demonstration-based_Neural_Control_Barrier_Functions"},{"title":"CPED-NCBFs: A Conformal Prediction for Expert Demonstration-based Neural Control Barrier Functions","url":"https://arxiv.org/html/2507.15022"},{"title":"[2507.15022] CPED-NCBFs: A Conformal Prediction for Expert Demonstration-based Neural Control Barrier Functions","url":"https://arxiv.org/abs/2507.15022"},{"title":"[2504.07611] Conditional Conformal Risk Adaptation","url":"https://arxiv.org/abs/2504.07611"}]

Perfect! I found the exact paper you're looking for. Here are the search results:

## Found: arXiv 2503.17678

The paper is titled "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction" and was submitted on March 22, 2025.

### Key Details:

**Authors:** Hao Zhou, Yanze Zhang, and Wenhao Luo from the Department of Computer Science, University of Illinois Chicago

**Main Contribution:** The paper uses Adaptive Conformal Prediction (ACP) to quantify uncertainty from online observations and combines it with Control Barrier Functions (CBF) to characterize uncertainty-aware safe control constraints under learned dynamics

**Technical Approach:** The framework first employs Quadrature Fourier Features (QFF) for kernel function approximation of Gaussian Processes (GPs) to enable efficient approximation of unknown dynamics, and an optimism-based exploration strategy is integrated with ACP-based CBFs for safe exploration and near-optimal safe nonlinear control

The paper addresses safe reinforcement learning with formal safety guarantees using distribution-free uncertainty quantification techniques combined with control barrier functions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "287046aa-58e7-408f-9986-b388f6777a10"
}
```

</details>

---

### Tool result

_source line 135 · 2026-05-15T20:18:05.228Z_

<details><summary>↩ Tool result · `toolu_018eoetP3wwoKradundhyJz8`</summary>

```text
Web search results for query: "DiG-Flow 2512.01715 flow matching denoising trajectory discrepancy method details"

Links: [{"title":"BeingBeyond ∝ DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/pdf/2512.01715"},{"title":"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/html/2512.01715"},{"title":"[2512.01715] DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://arxiv.org/abs/2512.01715"},{"title":"GitHub - BeingBeyond/DiG-Flow: DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models","url":"https://github.com/BeingBeyond/DiG-Flow"},{"title":"GitHub - iszhanjiawei/flow_matching_arxiv_daily · GitHub","url":"https://github.com/iszhanjiawei/flow_matching_arxiv_daily"},{"title":"Diffusion Meets Flow Matching","url":"https://diffusionflow.github.io/"},{"title":"Robot Manipulation with Flow Matching Fan Zhang, Michael Gienger","url":"https://openreview.net/pdf?id=l8DzhzIcEj"},{"title":"GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation","url":"https://openaccess.thecvf.com/content/CVPR2025/papers/Xing_GoalFlow_Goal-Driven_Flow_Matching_for_Multimodal_Trajectories_Generation_in_End-to-End_CVPR_2025_paper.pdf"},{"title":"Variational Flow Matching for Graph Generation Floor Eijkelboom∗","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/15b780350b302a1bf9a3bd273f5c15a4-Paper-Conference.pdf"},{"title":"25. Flow Matching - Machine Learning with a Honk","url":"https://mlhonk.substack.com/p/25-flow-matching"}]

Based on the web search results, I found detailed information about DiG-Flow (arXiv:2512.01715). Here are the key details about the trajectory discrepancy method:

## Overview

DiG-Flow is a principled framework that enhances VLA (Vision-Language-Action) robustness through geometric regularization.

## Core Method Details

The key insight is that the distributional discrepancy between observation and action embeddings provides a meaningful geometric signal: lower transport cost indicates compatible representations, while higher cost suggests potential misalignment.

When observation features from the vision-language backbone and action embeddings from the policy head exhibit low distributional discrepancy, their representations are geometrically compatible, suggesting semantic coherence. Conversely, high discrepancy signals potential misalignment that may indicate spurious patterns or out-of-distribution observations.

## Architecture Components

The DiG-Flow framework includes 3 main components: a discrepancy function (among others). The DiG-Block uses act/obs projections to compute D(µH, µZ) and a gate g, and performs a gated residual update.

The flow-matching head produces action trajectories from noise as in standard VLA models, and the DiG-Refine module can apply a small number of refinement steps entirely within the action head to further polish the predicted actions.

## Training Details

By default, DiG-Block modules use 32 sliced projections for the discrepancy, a temperature of τ = 1.0, residual strength λ = 0.4, and a spectral norm bound of BR = 2.0.

This intervention operates at the representation level without modifying the flow matching path or target vector field. The framework provides theoretical guarantees showing that discrepancy-guided training provably decreases the training objective, and that guided inference refinement converges with contraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e9ac4150-a2c3-48dd-85dc-aa680ee5aad5"
}
```

</details>

---

### System

_source line 136_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for DRC \"Decaying Relative Correction\" policy refinem…",
  "usage": {
    "total_tokens": 16151,
    "tool_uses": 5,
    "duration_ms": 12902
  },
  "last_tool_name": "WebSearch",
  "uuid": "509d6705-f125-4c01-8bba-dc8cf457423a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 137_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DyNDXmp7XY3qGEKSWh8umq`</summary>

```json
{
  "query": "DRC \"Decaying Relative Correction\" policy refinement Pan arXiv 2503.15368 temporal decay correction magnitude"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d095625e-6d48-45ba-b0a2-b667e1187c97",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014mwQG8cN9a1jVkz7bu4UwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 138 · 2026-05-15T20:18:05.616Z_

<details><summary>↩ Tool result · `toolu_01P7FHKfFJNJFDy2UBSfrYGb`</summary>

```text
Web search results for query: "Silver Allen Tenenbaum Kaelbling "Residual Policy Learning" arXiv 1812.06298 RSS 2018 zero-initialization bounded corrections"

Links: [{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"Residual Policy Learning","url":"https://arxiv.org/pdf/1812.06298v2"},{"title":"[1812.06298] Residual Policy Learning - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.06298"},{"title":"[PDF] Residual Policy Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Residual-Policy-Learning-Silver-Allen/8c21a1d8844e6b58fd74b2b94c512a23497029c1"},{"title":"Google Scholar","url":"https://scholar.google.com/scholar_lookup?title=Residual+policy+learning&amp=&author=T+Silver&amp=&author=K+Allen&amp=&author=J+Tenenbaum&amp=&author=L+Kaelbling&amp=&publication_year=2018&amp=&journal=arXiv+preprint+arXiv:1812.06298"},{"title":"Residual Policy Learning","url":"https://www.researchgate.net/publication/329734796_Residual_Policy_Learning"},{"title":"[1812.06298v2] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298v2"},{"title":"GitHub - k-r-allen/residual-policy-learning: Residual policy learning · GitHub","url":"https://github.com/k-r-allen/residual-policy-learning"},{"title":"Residual Policy Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181206298S/abstract"},{"title":"GitHub - k-r-allen/residual-policy-learning: Residual policy learning","url":"https://github.com/k-r-allen/residual-policy-learning/tree/master"}]

I found the paper you're looking for. Here are the key results:

## Paper Information

The paper "Residual Policy Learning" is authored by Tom Silver, Kelsey Allen, Josh Tenenbaum, and Leslie Kaelbling, and was posted to arXiv on January 3, 2019 with identifier 1812.06298.

## Overview

The paper presents Residual Policy Learning (RPL): a simple method for improving nondifferentiable policies using model-free deep reinforcement learning. RPL thrives in complex robotic manipulation tasks where good but imperfect controllers are available.

## Key Findings

In these tasks, reinforcement learning from scratch remains data-inefficient or intractable, but learning a residual on top of the initial controller can yield substantial improvements. RPL is able to substantially improve on the original policies, while requiring far less data than learning from scratch to achieve the same performance.

## Experimental Design

The researchers studied RPL in six challenging MuJoCo tasks involving partial observability, sensor noise, model misspecification, and controller miscalibration, considering both hand-designed policies and model-predictive controllers with known or learned transition models.

You can access the paper directly at https://arxiv.org/abs/1812.06298 and find code and additional resources at https://k-r-allen.github.io/residual-policy-learning/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6793f9b5-c328-46b7-b8ae-f68014fb3da2"
}
```

</details>

---

### System

_source line 139_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for \"Divergence is Uncertainty\" closed-form posterior…",
  "usage": {
    "total_tokens": 16154,
    "tool_uses": 6,
    "duration_ms": 13303
  },
  "last_tool_name": "WebSearch",
  "uuid": "19dde1f8-b532-4f66-98ae-9d831dc99954",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 140_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UmoVKLFNget8s8gQCrczcs`</summary>

```json
{
  "query": "\"Divergence is Uncertainty\" closed-form posterior covariance flow matching Xing Wang arXiv 2605.00941"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "38b0dc4b-967c-4bb9-bcf9-d8fb1bdbdbbc",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014mwQG8cN9a1jVkz7bu4UwP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14660,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 141 · 2026-05-15T20:18:06.129Z_

<details><summary>↩ Tool result · `toolu_01TehTDMyuQZDBxz7HuZTQfP`</summary>

```text
Web search results for query: "SC-VLA 2602.21633 "residual" OR "correction" RL reinforcement learning "per-task" OR "task-level" training mechanism"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/html/2509.09674v1"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"(PDF) Residual Policy Adaptation for Vision-Language-Action Models in Precision Robotic Assembly","url":"https://www.researchgate.net/publication/401122606_Residual_Policy_Adaptation_for_Vision-Language-Action_Models_in_Precision_Robotic_Assembly"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"RL-VLA3: A Flexible and Asynchronous Reinforcement Learning Framework for VLA Training","url":"https://arxiv.org/html/2602.05765"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"}]

Perfect! I found the paper you were searching for. Here are the results:

## SC-VLA 2602.21633 - Self-Correcting VLA

The paper proposes Self-Correcting VLA (SC-VLA), which achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The approach designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends.

### Key Context

Standard vision-language-action (VLA) models rely on fitting statistical data priors, limiting their robust understanding of underlying physical dynamics, while reinforcement learning enhances physical grounding through exploration yet typically relies on external reward signals that remain isolated from the agent's internal states.

The paper (arXiv:2602.21633) was published on February 25, 2026, and is directly available at: https://arxiv.org/html/2602.21633

This appears to be a recent and relevant work on VLA models that incorporates reinforcement learning mechanisms for online action refinement and self-improvement in robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "0e5c510f-2e50-49ec-8bfe-fbc134953d88"
}
```

</details>

---

### Tool result

_source line 142 · 2026-05-15T20:18:06.355Z_

<details><summary>↩ Tool result · `toolu_01PL4uD6H2VnvFUQE5bWGGE9`</summary>

```text
Web search results for query: "TRANSIC "sim-to-real policy transfer" Jiang Wang Zhang Wu Fei-Fei arXiv 2405.10315 binary gate residual"

Links: [{"title":"[2405.10315] TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/abs/2405.10315"},{"title":"Transic: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/html/2405.10315v1"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | alphaXiv","url":"https://www.alphaxiv.org/overview/2405.10315v3"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction (2024) | Yunfan Jiang | 10 Citations","url":"https://scispace.com/papers/transic-sim-to-real-policy-transfer-by-learning-from-online-2heee0h3xd"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://www.researchgate.net/publication/380635321_TRANSIC_Sim-to-Real_Policy_Transfer_by_Learning_from_Online_Correction"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning ...","url":"https://arxiv-sanity-lite.com/?rank=pid&pid=2405.10315"},{"title":"TRANSIC: Human-in-the-Loop Sim-to-Real Transfer","url":"https://www.emergentmind.com/papers/2405.10315"},{"title":"GitHub - transic-robot/transic · GitHub","url":"https://github.com/transic-robot/transic"},{"title":"transic-robot/data · Datasets at Hugging Face","url":"https://huggingface.co/datasets/transic-robot/data"},{"title":"TRANSIC | Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://transic-robot.github.io/"}]

I found the paper! TRANSIC is authored by Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, and Li Fei-Fei, with the arXiv identifier 2405.10315.

TRANSIC is a data-driven approach to enable successful sim-to-real transfer based on a human-in-the-loop framework. It allows humans to augment simulation policies to overcome various unmodeled sim-to-real gaps holistically through intervention and online correction. Residual policies can be learned from human corrections and integrated with simulation policies for autonomous execution.

The paper addresses the key challenge of addressing simulation-to-reality (sim-to-real) gaps. Once the base robot policies are acquired from simulation training, they are deployed onto real robots where human operators monitor the execution. When the robot makes mistakes or gets stuck, humans interrupt and assist robot policies through teleoperation.

The approach can achieve successful sim-to-real transfer in complex and contact-rich manipulation tasks such as furniture assembly.

Regarding the specific technical terms you mentioned (binary gate residual), the search results don't provide detailed information about this particular architectural component. To find more specific technical details about the binary gate residual mechanism, you may want to review the full paper PDF directly from the arXiv link.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2e0b79e5-1f40-48c0-8d68-a47e3c94c217"
}
```

</details>

---

### Tool result

_source line 143 · 2026-05-15T20:18:06.943Z_

<details><summary>↩ Tool result · `toolu_01427s2Esu1BTDun76EAy88M`</summary>

```text
Web search results for query: "VLA-Pilot 2511.14178 "2.41s" OR "2.41 seconds" per control step latency inference time"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning","url":"https://arxiv.org/abs/2511.14178"},{"title":"Real-Time Execution of Action Chunking Flow Policies Kevin Black1,2,","url":"https://www.pi.website/download/real_time_chunking.pdf"},{"title":"Running VLAs at Real-time Speed","url":"https://arxiv.org/html/2510.26742v1"},{"title":"How Fast Can I Run My VLA? Demystifying VLA Inference Performance with VLA-Perf","url":"https://arxiv.org/html/2602.18397v1"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224v1"},{"title":"TIDAL: Temporally Interleaved Diffusion and Action Loop for High-Frequency VLA Control","url":"https://arxiv.org/html/2601.14945"},{"title":"Trade-off between Movement Quality and Inference Speed in Vision-Language-Action Models for Robotic Systems | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/trade-off-between-movement-quality-and-inference-speed-in-vision-language-action-models-for-robotic-52af173ff1bd"},{"title":"Asynchronous Fast-Slow Vision-Language-Action Policies for Whole-Body Robotic Manipulation","url":"https://arxiv.org/html/2512.20188v1"},{"title":"LEAVE NO OBSERVATION BEHIND: REAL-TIME COR- RECTION FOR VLA ACTION CHUNKS","url":"https://www.arxiv.org/pdf/2509.23224"}]

Based on the search results, I found the information you're looking for:

VLA-Pilot has an overall inference time of 2.41 seconds per control step. The main bottleneck lies in MLLM-based reward reasoning, and this latency reflects a reasonable trade-off between generalization and efficiency, similar to prior FMs-based steering pipelines like FOREWARN (3.7s).

This information comes from the paper titled "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion" (arXiv:2511.14178).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "40db35e9-46fe-449c-a5d1-f2fe0a81d494"
}
```

</details>

---

### System

_source line 144_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for pi0 arXiv 2410.24164 vision-language-action flow …",
  "usage": {
    "total_tokens": 16068,
    "tool_uses": 2,
    "duration_ms": 5083
  },
  "last_tool_name": "WebSearch",
  "uuid": "dcfd0dcb-5cc6-4f75-b9d4-1b9fed209cca",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 145_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QzUDcPXjEiuRrVrWG2FwBp`</summary>

```json
{
  "query": "pi0 arXiv 2410.24164 vision-language-action flow matching robot control"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "82a14fe4-75fa-486f-8125-75adafbcb162",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 146 · 2026-05-15T20:18:07.913Z_

<details><summary>↩ Tool result · `toolu_01UmqkPnRfDwNdQbMghR2yvi`</summary>

```text
Web search results for query: "Zollo Zemel "Confidence Calibration in Vision-Language-Action Models" arXiv 2507.17383"

Links: [{"title":"[2507.17383] Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/abs/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models Thomas Zollo","url":"https://arxiv.org/pdf/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"(PDF) Confidence Calibration in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"},{"title":"Robotics Jul 2025","url":"https://www.arxiv.org/list/cs.RO/2025-07?skip=450&show=250"},{"title":"Confidence Calibration in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=aiPC7jAd2f"},{"title":"Richard Zemel's research works | Columbia University and other places","url":"https://www.researchgate.net/scientific-contributions/Richard-Zemel-2218797115"},{"title":"confidence-calibration-in-vision-language-action-models - Ask this paper | Bohrium","url":"https://www.bohrium.com/paper-details/confidence-calibration-in-vision-language-action-models/1155114182379569160-108625"},{"title":"[2604.19444] Unsupervised Confidence Calibration for Reasoning LLMs from a Single Generation","url":"https://arxiv.org/abs/2604.19444"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=2650&show=25"}]

I found the paper! Here's what I discovered about this research:

## Paper Details

"Confidence Calibration in Vision-Language-Action Models" is authored by Thomas P Zollo and Richard Zemel, with the arXiv identifier 2507.17383.

## Overview

The paper presents a first-of-its-kind study of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.

## Main Contributions

The researchers establish a confidence baseline for VLAs, examine how task success relates to calibration error and how calibration evolves over time, and introduce two lightweight techniques to remedy the miscalibration they observe: prompt ensembles and action-wise Platt scaling.

## Key Motivation

A well-calibrated robot policy produces confidence estimates that align with its probability of task success—for example, the robot should succeed on 95% of instances for which it expresses 95% confidence.

The paper was submitted on July 23, 2025, with a revised version on December 22, 2025. You can access the full paper at https://arxiv.org/abs/2507.17383.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6b1b1dff-9e29-4ac7-8fcd-ea712b196577"
}
```

</details>

---

### Tool result

_source line 147 · 2026-05-15T20:18:07.935Z_

<details><summary>↩ Tool result · `toolu_01Q5N2HPwHNaNueUSuNEGTML`</summary>

```text
Web search results for query: "Gu "SAFE Multitask Failure Detection Vision-Language-Action Models" NeurIPS 2025 conformal prediction"

Links: [{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"NeurIPS Poster SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117510"},{"title":"[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09937"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09937v2"},{"title":"[PDF] SAFE: Multitask Failure Detection for Vision-Language-Action Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SAFE:-Multitask-Failure-Detection-for-Models-Gu-Ju/8165f26c174bd327506242ee898cf18a3abe61cf"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=XPyAukgsFf"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models | Toyota Research Institute","url":"https://www.tri.global/research/safe-multitask-failure-detection-vision-language-action-models"},{"title":"[Literature Review] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://www.themoonlight.io/en/review/safe-multitask-failure-detection-for-vision-language-action-models"},{"title":"Paper page - SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://huggingface.co/papers/2506.09937"}]

Based on the search results, I found comprehensive information about the paper "SAFE: Multitask Failure Detection for Vision-Language-Action Models":

## Overview

SAFE is a failure detector for generalist robot policies such as vision-language-action models (VLAs) that was published at NeurIPS 2025. The paper was authored by Qiao Gu, Yuanliang Ju, Shengxiang Sun, Igor Gilitschenski, Haruki Nishimura, Masha Itkina, and Florian Shkurti.

## Problem and Motivation

While VLAs have shown promising robotic behaviors across a diverse set of manipulation tasks, they achieve limited success rates when deployed on novel tasks out of the box. Existing failure detectors are trained and tested only on one or a few specific tasks, while generalist VLAs require the detector to generalize and detect failures also in unseen tasks and novel environments.

## Technical Approach

The work analyzes the VLA feature space and finds that VLAs have sufficient high-level knowledge about task success and failure, which is generic across different tasks. 

SAFE has three main components: (1) feature extraction from the last layer of a VLA model, (2) learning a failure detector using an MLP or LSTM backbone, and (3) calibration and deployment using functional conformal prediction (CP) on a hold-out calibration set.

## Conformal Prediction

SAFE achieves state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction. All baselines use the same conformal prediction framework as SAFE to determine the time-varying threshold.

## Evaluation and Results

The method was tested on OpenVLA, π0, and π0-FAST in both simulated and real-world environments. The paper includes official code and resources available on GitHub and a project webpage.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "33a18f3d-1c3c-4fc7-ad6e-291f83dd85a1"
}
```

</details>

---

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for SmolVLA arXiv 2506.01844 vision-language-action m…",
  "usage": {
    "total_tokens": 16071,
    "tool_uses": 3,
    "duration_ms": 6089
  },
  "last_tool_name": "WebSearch",
  "uuid": "7eff4147-3947-40fc-9327-f2f3044b4309",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 149_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0142uJiG5SuXrpQH77TC2fsf`</summary>

```json
{
  "query": "SmolVLA arXiv 2506.01844 vision-language-action model parameters"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "51569c37-dd6a-4c68-9b73-557c1ac0feb9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 150 · 2026-05-15T20:18:08.910Z_

<details><summary>↩ Tool result · `toolu_01Cdp9eaK9QGHsy68BbRrBuL`</summary>

```text
Web search results for query: ""Self-Improving Vision-Language-Action Models" "Data Generation via Residual RL" arXiv 2511.00091 PLD scheduled magnitude bound"

Links: [{"title":"[2511.00091] Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/abs/2511.00091"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091"},{"title":"(PDF) Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://www.researchgate.net/publication/397231758_Self-Improving_Vision-Language-Action_Models_with_Data_Generation_via_Residual_RL"},{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"},{"title":"[PDF] Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Improving-Vision-Language-Action-Models-with-Xiao-Lin/14c584af2fda0b9b5851b1e8573c4e2dd2c8fd0b"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2511.00091"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"Interesting Directions in Vision-Language-Action Model Research","url":"https://itcanthink.substack.com/p/interesting-directions-in-vision"}]

I found the paper! Here's what I discovered:

## Self-Improving Vision-Language-Action Models with Data Generation via Residual RL

The paper proposes Probe, Learn, Distill (PLD), a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection.

### The Three Stages:

1. **Stage 1 (Specialist Acquisition):** Lightweight residual actors are trained to probe failure regions of the VLA generalist.

2. **Stage 2 (Data Collection):** A hybrid rollout scheme aligns collected trajectories with the generalist's deployment distribution while capturing recovery behaviors.

3. **Stage 3 (Fine-tuning):** The curated trajectories are distilled back into the generalist with standard SFT.

### Results:

PLD achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

**Paper Details:**
- **ArXiv ID:** 2511.00091
- **Published:** October 30, 2025
- **Status:** Accepted to ICLR 2026

Regarding the specific technical terms you mentioned (PLD scheduled magnitude bound), the search results don't contain detailed technical specifications about those particular parameters. You may need to review the full paper PDF on arXiv for those implementation details.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "bc633776-d1ce-42a1-b9c6-9c3ea6222027"
}
```

</details>

---

### Tool result

_source line 151 · 2026-05-15T20:18:09.059Z_

<details><summary>↩ Tool result · `toolu_0195wet5TjfiDcGWRUC36WVs`</summary>

```text
Web search results for query: "A2C2 2509.23224 "jointly" OR "joint training" OR "frozen" base VLA correction head training"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224"},{"title":"SeqVLA: Sequential Task Execution for Long-Horizon Manipulation with Completion-Aware Vision-Language-Action Model","url":"https://arxiv.org/html/2509.14138"},{"title":"Forces Command Regulation (FORSCOM Reg.) 350-5: Joint Training Exercises | The Afterlives of Government Documents","url":"https://documentafterlives.newmedialab.cuny.edu/content/forces-command-regulation-forscom-reg-350-5-joint-training-exercises"},{"title":"BY ORDER OF THE SECRETARY OF THE AIR FORCE AIR FORCE INSTRUCTION 10-204","url":"https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-204/afi10-204.pdf"},{"title":"JOINT TRAINING MANUAL FOR THE ARMED FORCES OF THE UNITED STATES CJCSM 3500.03E","url":"https://www.jcs.mil/Portals/36/Documents/Doctrine/training/cjcsm3500_03e%20.pdf?ver=2017-12-29-171247-397"},{"title":"UNCLASSIFIED UNCLASSIFIED JOINT TRAINING POLICY FOR THE ARMED FORCES OF","url":"https://www.jcs.mil/Portals/36/Documents/Doctrine/training/cjcsi3500_01j.pdf?ver=2020-01-21-111919-340"},{"title":"JOINT TRAINING MANUAL FOR THE ARMED FORCES ...","url":"https://www.jcs.mil/Portals/36/Documents/Library/Manuals/m350003.pdf"},{"title":"Joint Live Virtual Constructive Modernization","url":"https://www.jcs.mil/Doctrine/Joint-Training/JLVC/"},{"title":"[2509.22199] MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training","url":"https://arxiv.org/abs/2509.22199"}]

Based on the search results, I found the arXiv paper 2509.23224 about A2C2 (Asynchronous Action Chunk Correction). Here's what the paper covers:

A2C2 is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

Importantly for your query: The approach requires no retraining of the base policy, and the correction head is trained on the same dataset as the base policy and, in principle, can be added to any off-the-shelf VLAs.

On the dynamic Kinetix task suite (12 tasks) and LIBERO Spatial, the method yields consistent success rate improvements across increasing delays and execution horizons (+23% point and +7% point respectively, compared to RTC), and also improves robustness for long horizons even with zero injected delay.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "32f8c7c0-ca1e-4365-8d70-c0ca2084dd44"
}
```

</details>

---

### System

_source line 152_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for LIBERO NeurIPS 2023 benchmarking knowledge transf…",
  "usage": {
    "total_tokens": 16074,
    "tool_uses": 4,
    "duration_ms": 6752
  },
  "last_tool_name": "WebSearch",
  "uuid": "5c648c79-c778-4c80-996a-69fbe2a82399",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 153_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TsRMHQi7fESmHt4Je4KgRG`</summary>

```json
{
  "query": "LIBERO NeurIPS 2023 benchmarking knowledge transfer lifelong robot learning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d4fd435b-5912-4a15-871e-f8adc632bd66",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### System

_source line 154_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for Lipman 2023 Flow Matching for Generative Modeling…",
  "usage": {
    "total_tokens": 16077,
    "tool_uses": 5,
    "duration_ms": 7223
  },
  "last_tool_name": "WebSearch",
  "uuid": "003989e1-1f5d-4b9a-aec7-178984e56535",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 155_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EVvu3dNoeJbinCjsE5W79U`</summary>

```json
{
  "query": "Lipman 2023 Flow Matching for Generative Modeling ICLR"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7ef13553-6e71-4b61-9c92-4cadd4d0208d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### System

_source line 156_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for Ledoit Wolf 2004 well-conditioned estimator large…",
  "usage": {
    "total_tokens": 16080,
    "tool_uses": 6,
    "duration_ms": 8026
  },
  "last_tool_name": "WebSearch",
  "uuid": "de6b18b9-9c6b-4c4c-a770-156d5e4f3b5e",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 157_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WbxCvHiWbaRAQSnfkKCU1p`</summary>

```json
{
  "query": "Ledoit Wolf 2004 well-conditioned estimator large-dimensional covariance matrices shrinkage"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "bda9ddbe-3ae8-4fe5-a19a-6cf08ea75746",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### System

_source line 158_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for Ross Gordon Bagnell 2011 DAgger AISTATS imitation…",
  "usage": {
    "total_tokens": 16083,
    "tool_uses": 7,
    "duration_ms": 8853
  },
  "last_tool_name": "WebSearch",
  "uuid": "9523a09a-eefd-45b9-bbaf-3b0aeeb0d6ac",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 159_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G4XXhHmBbRD8xaYsTxb9ph`</summary>

```json
{
  "query": "Ross Gordon Bagnell 2011 DAgger AISTATS imitation learning compounding error"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "73f4c8ca-5771-49bb-b89d-8e32d1801cfd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 160 · 2026-05-15T20:18:11.850Z_

<details><summary>↩ Tool result · `toolu_01DyNDXmp7XY3qGEKSWh8umq`</summary>

```text
Web search results for query: "DRC "Decaying Relative Correction" policy refinement Pan arXiv 2503.15368 temporal decay correction magnitude"

Links: [{"title":"[2503.15368] Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/abs/2503.15368"},{"title":"Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/html/2503.15368"},{"title":"Multi-Layer GRPO: Enhancing Reasoning and Self-Correction in Large Language Models","url":"https://arxiv.org/html/2506.04746v1"},{"title":"[2512.15596] Corrective Diffusion Language Models","url":"https://arxiv.org/abs/2512.15596"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=11175&show=1000"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"Computer Science Jul 2025","url":"https://www.arxiv.org/list/cs/2025-07?skip=4275&show=2000"},{"title":"Computer Science Jan 2025","url":"https://arxiv.org/list/cs/2025-01?skip=0&show=2000"},{"title":"DCDP: Decoupled Data Consistency via Diffusion Purification for Solving General Inverse Problems","url":"https://arxiv.org/html/2403.06054v6"},{"title":"Machine Learning May 2025","url":"https://arxiv.org/list/cs.LG/2025-05?skip=1500&show=2000"}]

Based on the search results, I found the paper you're looking for. Here's what the research reveals about the DRC method:

Decaying Relative Correction (DRC) is a correction method based upon the spatial offset vector provided by the expert. The method is part of a paper titled "Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation" by Cheng Pan and co-authors (arXiv 2503.15368).

**Key characteristics of DRC:**

The relative correction motion provided by the experts teleoperation provides the vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate. This temporal decay is central to the method's design.

**Performance benefits:**

DRC reduces the required expert intervention rate by 30% compared to a standard absolute corrective method. Additionally, integrating DRC within an online imitation learning framework rapidly increases the success rate of manipulation tasks such as raspberry harvesting and cloth wiping.

**Implementation context:**

The cable handle enables human experts to provide corrective signals with continuous magnitudes, allowing intuitive corrective teleportation for online imitation learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7749a493-3afd-47bc-9fc8-c09985f5a972"
}
```

</details>

---

### System

_source line 161_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for Angelopoulos Bates 2107.07511 gentle introduction…",
  "usage": {
    "total_tokens": 16086,
    "tool_uses": 8,
    "duration_ms": 9836
  },
  "last_tool_name": "WebSearch",
  "uuid": "9c9b4359-f5fb-4a6b-8890-aeca38c11c18",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 162_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01H9wYpDe4yuX5fSxobwCSMh`</summary>

```json
{
  "query": "Angelopoulos Bates 2107.07511 gentle introduction conformal prediction distribution-free"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6dbed621-3e71-4b3d-897e-eb1bad95b5cd",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Fkq2yuhhyACVQZ8PuAsdfK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 14587,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 163 · 2026-05-15T20:18:12.567Z_

<details><summary>↩ Tool result · `toolu_01UmoVKLFNget8s8gQCrczcs`</summary>

```text
Web search results for query: ""Divergence is Uncertainty" closed-form posterior covariance flow matching Xing Wang arXiv 2605.00941"

Links: [{"title":"[2605.00941] Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/abs/2605.00941"},{"title":"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching","url":"https://arxiv.org/html/2605.00941"},{"title":"[2106.00941] Self-Training Sampling with Monolingual Data Uncertainty for Neural Machine Translation","url":"https://arxiv.org/abs/2106.00941"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/stat.ML/2025-02?skip=200&show=100"},{"title":"Possibilistic Predictive Uncertainty for Deep Learning","url":"https://arxiv.org/html/2605.00600"},{"title":"Uncertainty Estimation on Graphs with Structure Informed Stochastic Partial Differential Equations","url":"https://arxiv.org/html/2506.06907v1"},{"title":"[2605.14570] Uncertainty Quantification for Large Language Diffusion Models","url":"https://arxiv.org/abs/2605.14570"},{"title":"Uncertainty Quantification for Large Language Diffusion Models","url":"https://arxiv.org/html/2605.14570"},{"title":"Computer Science Jul 2025","url":"https://arxiv.org/list/cs/2025-07?skip=1975&show=2000"},{"title":"Machine Learning Jul 2024","url":"https://web3.arxiv.org/list/cs.LG/2024-07?skip=60&show=1000"}]

I found the paper you're looking for. Here's what I found:

The paper "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching" addresses the problem of quantifying uncertainty in flow matching generative models. It proves that for any pre-trained flow matching velocity field, the trace of the posterior covariance over the clean data given the current state equals, in closed form, the divergence of the velocity field, up to a known time-dependent prefactor and an additive constant.

Existing approaches to uncertainty quantification in flow matching retrain the model with auxiliary variance heads, maintain costly ensembles, or propagate approximate covariance through many integration steps, trading off training cost, inference cost, or accuracy. The paper shows that none of these trade-offs is necessary.

The authors call this result the "divergence-uncertainty identity" for flow matching, and the matrix-level form of the identity is similarly closed-form, depending solely on the velocity Jacobian.

The paper was submitted on May 1, 2026 and was authored by Jiarui Xing, Song Wang, and Jian Wang.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a06d36d9-ab8d-4200-932d-9ee8a4dc09ac"
}
```

</details>

---

### Tool result

_source line 164 · 2026-05-15T20:18:13.859Z_

<details><summary>↩ Tool result · `toolu_0142uJiG5SuXrpQH77TC2fsf`</summary>

```text
Web search results for query: "SmolVLA arXiv 2506.01844 vision-language-action model parameters"

Links: [{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"[PDF] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Semantic Scholar","url":"https://www.semanticscholar.org/paper/SmolVLA:-A-Vision-Language-Action-Model-for-and-Shukor-Aubakirova/6ab4d113676d00e74b55e918fee4c7affaa8652f"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://www.researchgate.net/publication/392370918_SmolVLA_A_Vision-Language-Action_Model_for_Affordable_and_Efficient_Robotics"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250601844S/abstract"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2506.01844"},{"title":"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/smolvla-vision-language-action-model-affordable-efficient"}]

I've found information about SmolVLA from arXiv paper 2506.01844. Here's what I discovered:

## Overview

SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.

## Key Characteristics

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. Despite its compact size, SmolVLA achieves performance comparable to VLAs that are 10× larger.

## Model Architecture

For the VLM backbone, SmolVLA uses SmolVLM-2, an efficient model optimized for multi-image inputs, which relies on SigLIP to encode visual features for a SmolLM2 language decoder.

SmolVLA employs several optimization techniques: Visual token reduction (limiting visual tokens to 64 per frame), layer skipping (using only the first half of VLM layers), and interleaved attention (combining cross-attention and self-attention layers in the action expert).

## Training Data

SmolVLA is trained end-to-end on fewer than 30k episodes drawn entirely from publicly available, community-contributed datasets.

The paper demonstrates that this compact approach achieves strong performance for robotics applications while being significantly more accessible and affordable to train and deploy compared to existing vision-language-action models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2e428675-fb9a-4e99-8c01-caa84c3c99c6"
}
```

</details>

---

### System

_source line 165_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for arXiv 2406.07767 \"Conformalized Teleoperation\" ab…",
  "usage": {
    "total_tokens": 22034,
    "tool_uses": 8,
    "duration_ms": 32331
  },
  "last_tool_name": "WebSearch",
  "uuid": "41830240-284f-4889-8582-700a5b2da90a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 166_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013eM4LUfqhA5qxS5wdVRML5`</summary>

```json
{
  "query": "arXiv 2406.07767 \"Conformalized Teleoperation\" abstract method uncertainty flagging human review shared autonomy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "059cc8e8-ad1f-43d4-bac4-87409cfebb4b",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ei4XyGjCa6CxDJm4R4jWzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 814,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 18942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
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

_source line 167_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for arXiv 2503.17678 authors \"Zetian Zhou\" OR \"Shuo Y…",
  "usage": {
    "total_tokens": 22035,
    "tool_uses": 9,
    "duration_ms": 33006
  },
  "last_tool_name": "WebSearch",
  "uuid": "3450c2c7-9124-45b3-97b3-70448aeb5009",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 168_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NaYS4qivoyMe8DYcZQnQKh`</summary>

```json
{
  "query": "arXiv 2503.17678 authors \"Zetian Zhou\" OR \"Shuo Yang\" safe reinforcement learning conformal prediction"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3a089f32-287f-4f52-a9a3-a4bc4cad83ce",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Ei4XyGjCa6CxDJm4R4jWzJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 814,
      "cache_creation_input_tokens": 2126,
      "cache_read_input_tokens": 18942,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2126,
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

_source line 169 · 2026-05-15T20:18:15.033Z_

<details><summary>↩ Tool result · `toolu_01QzUDcPXjEiuRrVrWG2FwBp`</summary>

```text
Web search results for query: "pi0 arXiv 2410.24164 vision-language-action flow matching robot control"

Links: [{"title":"[2410.24164] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164"},{"title":"𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/html/2410.24164v1"},{"title":"Paper page - π_0: A Vision-Language-Action Flow Model for General Robot Control","url":"https://huggingface.co/papers/2410.24164"},{"title":"$π_0$: A Vision-Language-Action Flow Model for General Robot Control - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241024164B/abstract"},{"title":"[2410.24164] 𝜋₀: A Vision-Language-Action Flow Model for General Robot Control","url":"https://ar5iv.labs.arxiv.org/html/2410.24164"},{"title":"[2410.24164v1] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164v1"},{"title":"Notes on: \"π0: A Vision-Language-Action Flow Model for General Robot Control\" | cloderic.com","url":"https://www.cloderic.com/content/2025-02-27-notes-on-pi0"},{"title":"[PDF] π0: A Vision-Language-Action Flow Model for General Robot Control | Semantic Scholar","url":"https://www.semanticscholar.org/paper/%CF%800:-A-Vision-Language-Action-Flow-Model-for-General-Black-Brown/ef0c2a66b7bc82a2f90ac298310c064a49da8213"},{"title":"Vision-Language-Action Models and the Search for a Generalist Robot Policy","url":"https://itcanthink.substack.com/p/vision-language-action-models-and"},{"title":"[2410.24164v3] $π_0$: A Vision-Language-Action Flow Model for General Robot Control","url":"https://arxiv.org/abs/2410.24164v3"}]

Based on the search results, here's what I found about the paper:

## π₀: A Vision-Language-Action Flow Model for General Robot Control

The paper proposes a novel flow matching architecture built on top of a pre-trained vision-language model (VLM) that can be trained on a large and diverse dataset from multiple dexterous robot platforms, including single-arm robots, dual-arm robots, and mobile manipulators.

### Key Contributions

The work consists of a novel generalist robot policy architecture based on VLM pre-training and flow matching, and an empirical investigation of pre-training/post-training recipes for robot foundation models.

The approach uses a novel action expert that augments the standard VLM with flow-based outputs.

### Training Approach

The training recipe mirrors the pre-training/post-training separation commonly seen in exascale language and image-language models, where the model is first pre-trained on a very large and diverse corpus, and then fine-tuned on more narrow and more carefully curated data to induce the desired pattern of behavior.

### Capabilities and Evaluation

The model is evaluated for zero-shot control with language commands, with fine-tuning to downstream tasks, and in combination with a high-level semantic policy that outputs intermediate language commands to perform complex and temporally extended tasks. π₀ is designed for zero-shot generalization, fine-tuning for specific tasks, and real-time control up to 50Hz.

The approach is evaluated by pre-training on over 10,000 hours of robot data and fine-tuning to a variety of dexterous tasks.

The paper was submitted to arXiv on October 31, 2024, and is associated with Physical Intelligence, a robotics company founded by Sergey Levine and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7fc6072a-ff01-4dac-ac4a-533b6e3c9656"
}
```

</details>

---

### Tool result

_source line 170 · 2026-05-15T20:18:15.502Z_

<details><summary>↩ Tool result · `toolu_01XN7GTnLU2r56MEHqMwqKFe`</summary>

```text
Web search results for query: "ReconVLA 2604.16677 "draws multiple action samples" OR "sample selection" OR "best candidate" conformal scoring"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://zionchow.github.io/ReconVLA/"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Conformal Prediction Advanced Topics in Statistical Learning, Spring 2023","url":"https://www.stat.berkeley.edu/~ryantibs/statlearn-s23/lectures/conformal.pdf"},{"title":"ICML Poster A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression","url":"https://icml.cc/virtual/2025/poster/45852"},{"title":"A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression","url":"https://arxiv.org/html/2501.10533v2"},{"title":"(PDF) Multi-Output Conformal Regression: A Unified Comparative Study with New Conformity Scores","url":"https://www.researchgate.net/publication/388232003_Multi-Output_Conformal_Regression_A_Unified_Comparative_Study_with_New_Conformity_Scores"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/html/2507.20941v1"},{"title":"A unified comparative study with generalized conformity scores for multi-output conformal regression | Proceedings of the 42nd International Conference on Machine Learning","url":"https://dl.acm.org/doi/10.5555/3780338.3780852"},{"title":"[2501.10533] A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression","url":"https://arxiv.org/abs/2501.10533"}]

The search results show two different papers both titled "ReconVLA" but with different paper IDs. The first result (arxiv 2604.16677) is the one you're looking for. Let me search more specifically for the conformal scoring method details in that paper.

No links found.

Let me try a different search approach:

Links: [{"title":"Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/html/2604.16217"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"[2604.17984] Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization","url":"https://arxiv.org/abs/2604.17984"},{"title":"Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics","url":"https://arxiv.org/html/2512.17048v1"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/html/2507.20941v1"},{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"},{"title":"Debiased Machine Learning for Conformal Prediction of Counterfactual Outcomes Under Runtime Confounding","url":"https://arxiv.org/html/2604.03772v1"},{"title":"Conformal Predictions for Human Action Recognition with Vision-Language Models","url":"https://arxiv.org/html/2502.06631"},{"title":"Adaptive Conformal Prediction Intervals Over Trajectory Ensembles","url":"https://arxiv.org/html/2508.13362v1"},{"title":"[2604.06464v1] Weighted Bayesian Conformal Prediction","url":"https://arxiv.org/abs/2604.06464v1"}]

Let me search more directly for the specific methodology used in the ReconVLA paper with arxiv 2604.16677:

No links found.

Let me try a different approach to find the specific methodology:

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"[2502.16677] Reasoning within and between collective action problems","url":"https://arxiv.org/abs/2502.16677"},{"title":"Label-Noise-Robust Action-Prompted Video Segmentation ...","url":"https://www.arxiv.org/pdf/2509.16677"},{"title":"OmniVLA-RL: A Vision-Language-Action Model with Spatial Understanding and Online RL","url":"https://arxiv.org/html/2604.17706"},{"title":"Action Recommendations for Sequentially Rational Strategic Agents","url":"https://arxiv.org/html/2605.09785"},{"title":"EAST: Early Action Prediction Sampling Strategy with Token Masking","url":"https://arxiv.org/html/2604.18367"},{"title":"Deep Reinforcement Learning Approach for Trading Automation in The Stock Market","url":"https://arxiv.org/pdf/2208.07165"},{"title":"Where to Intervene: Action Selection in Deep Reinforcement Learning","url":"https://arxiv.org/html/2507.04187v1"}]

Based on my search results, I found information about ReconVLA paper (arxiv 2604.16677) by Chen, Lyu, and Beksi. The paper is titled "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control."

The ReconVLA framework includes a CQR (Conformal Quantile Regression)-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability. However, I was unable to find specific details in the search results about whether the method "draws multiple action samples," uses "sample selection," or selects the "best candidate" in its conformal scoring approach.

The search results confirm that the approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.

To get the specific technical details about the action sampling and selection strategy you're asking about, I would recommend accessing the full paper directly from arXiv at https://arxiv.org/html/2604.16677v1, as the publicly available excerpts in the search results don't contain that level of methodological detail.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "204e27f8-347d-4395-8e90-dc06a2627e3a"
}
```

</details>

---

### Tool result

_source line 171 · 2026-05-15T20:18:15.516Z_

<details><summary>↩ Tool result · `toolu_01TsRMHQi7fESmHt4Je4KgRG`</summary>

```text
Web search results for query: "LIBERO NeurIPS 2023 benchmarking knowledge transfer lifelong robot learning"

Links: [{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning | OpenReview","url":"https://openreview.net/forum?id=xzEtNSuDJk"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html"},{"title":"NeurIPS Poster LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://neurips.cc/virtual/2023/poster/73415"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning [Quick Review]","url":"https://liner.com/review/libero-benchmarking-knowledge-transfer-for-lifelong-robot-learning"},{"title":"[2306.03310] LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/abs/2306.03310"},{"title":"Peter Stone: LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning","url":"https://www.cs.utexas.edu/~pstone/Papers/bib2html/b2hd-liu_zhu_NeurIPS2023.html"},{"title":"LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning – UT Austin Robot Perception and Learning Lab","url":"https://rpl.cs.utexas.edu/publications/2023/12/10/liu-neurips23-libero/"},{"title":"GitHub - Lifelong-Robot-Learning/LIBERO: Benchmarking Knowledge Transfer in Lifelong Robot Learning · GitHub","url":"https://github.com/Lifelong-Robot-Learning/LIBERO"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.nips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html"}]

Based on the search results, here's what I found about LIBERO at NeurIPS 2023:

## Overview

LIBERO is a novel benchmark of lifelong learning for robot manipulation that was published at NeurIPS 2023 Datasets and Benchmarks Track.

## Key Research Topics

LIBERO highlights five key research topics in lifelong learning in decision-making (LLDM): 1) how to efficiently transfer declarative knowledge, procedural knowledge, or the mixture of both; 2) how to design effective policy architectures and 3) effective algorithms for LLDM; 4) the robustness of a lifelong learner with respect to task ordering; and 5) the effect of model pretraining for LLDM.

## Benchmark Contents

Four task suites (130 tasks in total) were created, and high-quality human-teleoperated demonstration data is provided for all tasks. The benchmark includes an extendible procedural generation pipeline that can in principle generate infinitely many tasks.

## Key Findings

Extensive experiments revealed that sequential finetuning outperforms existing lifelong learning methods in forward transfer, no single visual encoder architecture excels at all types of knowledge transfer, and naive supervised pretraining can hinder agents' performance in the subsequent LLDM.

The work was authored by Bo Liu, Yifeng Zhu, Chongkai Gao, Yihao Feng, Qiang Liu, Yuke Zhu, and Peter Stone.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "27cf26aa-835b-4178-a767-33d59bc45fca"
}
```

</details>

---

### Tool result

_source line 172 · 2026-05-15T20:18:17.069Z_

<details><summary>↩ Tool result · `toolu_01WbxCvHiWbaRAQSnfkKCU1p`</summary>

```text
Web search results for query: "Ledoit Wolf 2004 well-conditioned estimator large-dimensional covariance matrices shrinkage"

Links: [{"title":"A well-conditioned estimator for large-dimensional covariance matrices - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0047259X03000964"},{"title":"A Well-Conditioned Estimator For Large-Dimensional Covariance Matrices","url":"http://www.ledoit.net/ole1a.pdf"},{"title":"A well-conditioned estimator for large-dimensional ...","url":"https://perso.ens-lyon.fr/patrick.flandrin/LedoitWolf_JMA2004.pdf"},{"title":"A well-conditioned estimator for large-dimensional covariance matrices","url":"https://ideas.repec.org/a/eee/jmvana/v88y2004i2p365-411.html"},{"title":"[PDF] A well-conditioned estimator for large-dimensional covariance matrices | Semantic Scholar","url":"https://www.semanticscholar.org/paper/A-well-conditioned-estimator-for-large-dimensional-Ledoit-Wolf/b40890f3d917379ac4bd2e0933a134d45b4dc251"},{"title":"A well-conditioned estimator for large-dimensional covariance matrices | Journal of Multivariate Analysis","url":"https://dl.acm.org/doi/10.1016/S0047-259X(03)00096-4"},{"title":"LedoitWolf — scikit-learn 1.8.0 documentation","url":"https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html"},{"title":"Honey, I Shrunk the Sample Covariance Matrix Olivier Ledoit Equities Division","url":"http://www.ledoit.net/honey.pdf"},{"title":"Ledoit, Olivier, Michael Wolf (2004b) A well-conditioned estimator for large-dimensional covariance matrices. Journal of Multivariate Analysis 88: 365-411.","url":"https://www.sciepub.com/reference/61383"},{"title":"Analytical nonlinear shrinkage of large-dimensional ...","url":"https://projecteuclid.org/journals/annals-of-statistics/volume-48/issue-5/Analytical-nonlinear-shrinkage-of-large-dimensional-covariance-matrices/10.1214/19-AOS1921.pdf"}]

I've found comprehensive results about the Ledoit-Wolf 2004 paper on well-conditioned estimators for large-dimensional covariance matrices. Here's a summary of the key findings:

## Overview

The paper introduces an estimator that is both well-conditioned and more accurate than the sample covariance matrix asymptotically. This estimator is distribution-free and has a simple explicit formula that is easy to compute and interpret.

## The Shrinkage Approach

The paper proposes to estimate the covariance matrix by an optimally weighted average of two existing estimators: the sample covariance matrix and single-index covariance matrix. This method is generally known as shrinkage, and it is standard in decision theory and in empirical Bayesian statistics.

## Problem Being Addressed

Many applied problems require a covariance matrix estimator that is not only invertible, but also well-conditioned (that is, inverting it does not amplify estimation error). For large-dimensional covariance matrices, the usual estimator--the sample covariance matrix--is typically not well-conditioned and may not even be invertible.

## Key Results

The suggested shrinkage estimator can serve as an all-purpose alternative to the sample covariance matrix. It has smaller risk and is better-conditioned. The asymptotically optimal shrinkage intensity can be estimated consistently, which leads to a feasible estimator.

## Publication Details

The paper was published in the Journal of Multivariate Analysis, Volume 88, Issue 2, February 2004, pages 365-411.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7a84868c-c9d3-4be8-bddf-c1ad94c065e1"
}
```

</details>

---

### Tool result

_source line 173 · 2026-05-15T20:18:18.354Z_

<details><summary>↩ Tool result · `toolu_01H9wYpDe4yuX5fSxobwCSMh`</summary>

```text
Web search results for query: "Angelopoulos Bates 2107.07511 gentle introduction conformal prediction distribution-free"

Links: [{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://www.researchgate.net/publication/353284898_A_Gentle_Introduction_to_Conformal_Prediction_and_Distribution-Free_Uncertainty_Quantification"},{"title":"μ & σ - A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://people.eecs.berkeley.edu/~angelopoulos/blog/posts/gentle-intro/"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification - ADS","url":"https://ui.adsabs.harvard.edu/abs/2021arXiv210707511A/abstract"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification | alphaXiv","url":"https://www.alphaxiv.org/overview/2107.07511v1"},{"title":"Conformal Prediction: : A Gentle Introduction: Foundations and Trends® in Machine Learning: Vol 16, No 4","url":"https://dl.acm.org/doi/10.1561/2200000101"},{"title":"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/html/2107.07511v6"},{"title":"GitHub - aangelopoulos/conformal-prediction: Lightweight, useful implementation of conformal prediction on real data. · GitHub","url":"https://github.com/aangelopoulos/conformal-prediction"},{"title":"[PDF] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification | Semantic Scholar","url":"https://www.semanticscholar.org/paper/c3ea8eb80bc8ca0b21efa273b9e4a9fd059c65be"},{"title":"Conformal Prediction & Uncertainty Quantification","url":"https://www.emergentmind.com/papers/2107.07511"}]

I found the paper you're looking for! Here are the key details:

**Title:** A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification

**Authors:** Anastasios N. Angelopoulos and Stephen Bates

**ArXiv ID:** 2107.07511

**Overview:**
Conformal prediction is a user-friendly paradigm for creating statistically rigorous uncertainty sets/intervals for the predictions of such models. Critically, the sets are valid in a distribution-free sense: they possess explicit, non-asymptotic guarantees even without distributional assumptions or model assumptions.

**Purpose and Content:**
This hands-on introduction is aimed to provide the reader a working understanding of conformal prediction and related distribution-free uncertainty quantification techniques with one self-contained document. The authors lead the reader through practical theory for and examples of conformal prediction and describe its extensions to complex machine learning tasks involving structured outputs, distribution shift, time-series, outliers, models that abstain, and more.

Throughout, there are many explanatory illustrations, examples, and code samples in Python. With each code sample comes a Jupyter notebook implementing the method on a real-data example.

The paper is available on arXiv at https://arxiv.org/abs/2107.07511, and there is also a blog and tutorial video available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "f925fabe-a155-4488-b7c3-b2101065a923"
}
```

</details>

---

### Tool result

_source line 174 · 2026-05-15T20:18:18.976Z_

<details><summary>↩ Tool result · `toolu_01EVvu3dNoeJbinCjsE5W79U`</summary>

```text
Web search results for query: "Lipman 2023 Flow Matching for Generative Modeling ICLR"

Links: [{"title":"Flow Matching for Generative Modeling - Weizmann Institute of Science","url":"https://weizmann.elsevierpure.com/en/publications/flow-matching-for-generative-modeling/"},{"title":"[2210.02747] Flow Matching for Generative Modeling","url":"https://arxiv.org/abs/2210.02747"},{"title":"Flow Matching for Generative Modeling: Scalable CNFs","url":"https://hunterheidenreich.com/notes/machine-learning/generative-models/flow-matching-for-generative-modeling/"},{"title":"Flow Matching for Generative Modeling | OpenReview","url":"https://openreview.net/forum?id=PqvMRDCJT9t"},{"title":"FLOW MATCHING FOR GENERATIVE MODELING","url":"https://openreview.net/pdf/e99034416acd1ca82991f5d63735e77130fc06a7.pdf"},{"title":"[PDF] Flow Matching for Generative Modeling | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Flow-Matching-for-Generative-Modeling-Lipman-Chen/af68f10ab5078bfc519caae377c90ee6d9c504e9"},{"title":"ICLR Poster Flow Matching for Generative Modeling","url":"https://iclr.cc/virtual/2023/poster/11309"},{"title":"Flow Matching for Generative Modeling [Quick Review]","url":"https://liner.com/review/flow-matching-for-generative-modeling"},{"title":"GitHub - dongzhuoyao/awesome-flow-matching: A summary of related works about flow matching, stochastic interpolants · GitHub","url":"https://github.com/dongzhuoyao/awesome-flow-matching"},{"title":"Flow matching in Latent Space","url":"https://vinairesearch.github.io/LFM/"}]

I found the paper "Flow Matching for Generative Modeling" by Lipman et al. from ICLR 2023. Here's a summary of the key information:

## Paper Overview

The paper introduces Flow Matching, a new paradigm for generative modeling built on Continuous Normalizing Flows (CNFs), allowing them to train CNFs at unprecedented scale.

## Main Contribution

Flow Matching (FM) is a simulation-free approach for training CNFs based on regressing vector fields of fixed conditional probability paths. Flow Matching is compatible with a general family of Gaussian probability paths for transforming between noise and data samples—which subsumes existing diffusion paths as specific instances.

## Key Features

**Alternative Probability Paths**: The approach enables using Optimal Transport (OT) displacement interpolation to define conditional probability paths, which are more efficient than diffusion paths, provide faster training and sampling, and result in better generalization.

**Empirical Results**: Training CNFs using Flow Matching on ImageNet leads to consistently better performance than alternative diffusion-based methods in terms of both likelihood and sample quality, and allows fast and reliable sample generation using off-the-shelf numerical ODE solvers.

## Publication Details

The paper was presented at the 11th International Conference on Learning Representations, ICLR 2023, in Kigali, Rwanda. The authors are Yaron Lipman, Ricky T.Q. Chen, Heli Ben-Hamu, Maximilian Nickel, and Matt Le.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e44b3034-7e6e-4491-91f8-e9f0b6be1c02"
}
```

</details>

---

### Tool result

_source line 175 · 2026-05-15T20:18:19.405Z_

<details><summary>↩ Tool result · `toolu_01NaYS4qivoyMe8DYcZQnQKh`</summary>

```text
Web search results for query: "arXiv 2503.17678 authors "Zetian Zhou" OR "Shuo Yang" safe reinforcement learning conformal prediction"

Links: [{"title":"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/html/2503.17678"},{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"Computer Science Mar 2024","url":"http://arxiv.org/list/cs/2024-03?skip=8780&show=500"},{"title":"Machine Learning Mar 2025","url":"https://www.arxiv.org/list/cs.LG/2025-03?skip=3325&show=2000"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"},{"title":"Machine Learning Mar 2025","url":"https://arxiv.org/list/cs.LG/2025-03?skip=800&show=2000"},{"title":"Artificial Intelligence Jun 2025","url":"https://www.arxiv.org/list/cs.AI/2025-06?skip=1500&show=2000"},{"title":"Computer Science Jun 2023","url":"https://arxiv.org/list/cs/2023-06?skip=7220&show=1000"},{"title":"Computer Vision and Pattern Recognition","url":"https://web3.arxiv.org/list/cs.CV/recent?skip=145&show=500"},{"title":"Machine Learning Feb 2025","url":"https://arxiv.org/list/cs.LG/2025-02?skip=200&show=1000"}]

Based on the search results, I found information about arXiv paper 2503.17678:

The paper is titled "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction".

However, regarding your specific query about the authors "Zetian Zhou" or "Shuo Yang": The paper's authors are Hao Zhou, Yanze Zhang, and Wenhao Luo. Neither "Zetian Zhou" nor "Shuo Yang" appear to be authors of this paper.

The paper addresses safety in learning-enabled autonomous systems by proposing a provably sample efficient episodic safe learning framework with quantified uncertainty for online control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8e75cf47-305d-45e0-9fab-3d7e6db8c64c"
}
```

</details>

---

### Tool result

_source line 176 · 2026-05-15T20:18:19.772Z_

<details><summary>↩ Tool result · `toolu_01G4XXhHmBbRD8xaYsTxb9ph`</summary>

```text
Web search results for query: "Ross Gordon Bagnell 2011 DAgger AISTATS imitation learning compounding error"

Links: [{"title":"A Reduction of Imitation Learning and Structured Prediction","url":"https://www.ri.cmu.edu/pub_files/2011/4/Ross-AISTATS11-NoRegret.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://proceedings.mlr.press/v15/ross11a.html"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (DAgger) - HackMD","url":"https://hackmd.io/@XiNyAicATy2jGaBhGc2ZRg/r1a97tfCU"},{"title":"A Reduction of Imitation Learning and Structured Prediction to ...","url":"https://www.cs.cmu.edu/~sross1/publications/Ross-AIStats11-NoRegret.pdf"},{"title":"[1011.0686] A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://arxiv.org/abs/1011.0686"},{"title":"A Reduction of Imitation Learning and Structure Prediction ...","url":"https://www.cl.uni-heidelberg.de/courses/ws18/iml/dagger.pdf"},{"title":"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.researchgate.net/publication/47646552_A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No-RegretOnline_Learning"},{"title":"Deep-RL-and-IL/docs/DAgger.md at master · NiloFreitas/Deep-RL-and-IL","url":"https://github.com/NiloFreitas/Deep-RL-and-IL/blob/master/docs/DAgger.md"},{"title":"(PDF) A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning","url":"https://www.academia.edu/24009408/A_Reduction_of_Imitation_Learning_and_Structured_Prediction_to_No_Regret_Online_Learning"},{"title":"An Invitation to Imitation J. Andrew Bagnell March 15, 2015","url":"https://gwern.net/doc/reinforcement-learning/model-free/2015-bagnell.pdf"}]

I've found the paper you're looking for. Here's the information about this influential work on imitation learning:

## Paper Details

The paper "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning" was authored by Ross, S., Gordon, G. & Bagnell, D. and published in the Proceedings of the Fourteenth International Conference on Artificial Intelligence and Statistics (AISTATS) in 2011, pages 627-635.

## Key Contributions

The paper introduces the **DAgger (Dataset Aggregation)** algorithm to address a fundamental problem in imitation learning. Sequential prediction problems such as imitation learning, where future observations depend on previous predictions (actions), violate the common i.i.d. assumptions made in statistical learning, which leads to poor performance in theory and often in practice.

The paper proposes a new iterative algorithm, which trains a stationary deterministic policy, that can be seen as a no regret algorithm in an online learning setting, and shows that any such no regret algorithm, combined with additional reduction assumptions, must find a policy with good performance under the distribution of observations it induces in such sequential settings.

## Impact

The dataset aggregation (DAgger) algorithm (Ross et al., 2011) is a seminal imitation learning method that addresses covariate shift. DAgger achieves linear growth in error with respect to task horizon T, improving performance in imitation learning.

The paper directly addresses the issue of compounding error through its iterative approach that distributes training data across the policy's induced state distribution rather than just the expert's demonstrations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6f900874-0eab-4487-8a37-8c3b45fb2f40"
}
```

</details>

---

### System

_source line 177_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for arXiv 1812.06298 \"residual policy learning\" zero …",
  "usage": {
    "total_tokens": 20713,
    "tool_uses": 7,
    "duration_ms": 28003
  },
  "last_tool_name": "WebSearch",
  "uuid": "6e9cc032-9c17-40bc-b61e-f36e65541607",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 178_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014LuVzRVBr8hVELjjhGyHrK`</summary>

```json
{
  "query": "arXiv 1812.06298 \"residual policy learning\" zero initialization bounded action corrections classical controller framework"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "ffa728d9-82af-4e77-ba16-e5069f9257ec",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QmpfDwddTnK9pU9Hn2MmPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 16099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4559,
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

_source line 179 · 2026-05-15T20:18:20.972Z_

<details><summary>↩ Tool result · `toolu_013eM4LUfqhA5qxS5wdVRML5`</summary>

```text
Web search results for query: "arXiv 2406.07767 "Conformalized Teleoperation" abstract method uncertainty flagging human review shared autonomy"

Links: [{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767"},{"title":"[2406.07767v1] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"http://arxiv.org/abs/2406.07767v1"},{"title":"Conformalized Teleoperation: Confidently Mapping Human ...","url":"https://arxiv.org/pdf/2406.07767"},{"title":"Conformalized Teleoperation: Confidently Mapping Human ...","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Conformalized Interactive Imitation Learning: Handling Expert Shift and Intermittent Feedback","url":"https://conformalized-assistive-teleoperation.github.io/"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions · Robotics: Science and Systems","url":"https://roboticsconference.org/2024/program/papers/8/"},{"title":"Teleoperation of a robotic manipulator in peri-personal space: a virtual wand approach","url":"https://arxiv.org/html/2406.09309"},{"title":"Publications","url":"https://cmu-intentlab.github.io/publications.html"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions - YouTube","url":"https://www.youtube.com/watch?v=rkydo1yUGZY"}]

I found the paper arXiv 2406.07767 "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions" by Michelle Zhao and co-authors.

## Summary

The paper addresses the challenge that assistive robotic arms have more degrees-of-freedom than a human teleoperator can control with a low-dimensional input like a joystick, and existing approaches use data-driven methods to learn a mapping from low-dimensional human inputs to high-dimensional robot actions.

The key problem is determining if such a black-box mapping can confidently infer a user's intended high-dimensional action from low-dimensional inputs.

## Methodology

The key idea is to adapt the assistive map at training time to additionally estimate high-dimensional action quantiles, then calibrate these quantiles via uncertainty quantification methods, specifically leveraging adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.

## Uncertainty Detection and Human Review

The authors propose an uncertainty-interval-based mechanism for detecting high-uncertainty user inputs and robot states. This work is presented as a key step towards enabling robots to quantify their own uncertainty and proactively seek intervention when needed.

## Evaluation

The approach is evaluated in a 2D assistive navigation task and two 7DOF Kinova Jaco tasks involving assistive cup grasping and goal reaching.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e0bb9c97-0318-4953-b243-e81831fe6dba"
}
```

</details>

---

### System

_source line 180_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for TRANSIC 2405.10315 \"binary gate\" OR \"gating\" resi…",
  "usage": {
    "total_tokens": 20714,
    "tool_uses": 8,
    "duration_ms": 29296
  },
  "last_tool_name": "WebSearch",
  "uuid": "3471557b-ae4e-411d-b4c1-21d3002e16bc",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 181_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011AWLPH1jHv6TWFGAPFWCSE`</summary>

```json
{
  "query": "TRANSIC 2405.10315 \"binary gate\" OR \"gating\" residual action sim-to-real correction architecture details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e54f407b-59d2-4f6b-9132-6d059c6731e0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QmpfDwddTnK9pU9Hn2MmPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 16099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4559,
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

_source line 182_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA arxiv 2604.16677 action selection \"multi…",
  "usage": {
    "total_tokens": 26613,
    "tool_uses": 12,
    "duration_ms": 59302
  },
  "last_tool_name": "WebSearch",
  "uuid": "f8d6d08b-f753-45eb-a76c-093c34c2bc64",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 183_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TREnyon22F4yEMTt5jp47x`</summary>

```json
{
  "query": "ReconVLA arxiv 2604.16677 action selection \"multiple samples\" OR \"N samples\" OR \"best action\" OR \"conformal score\" methodology abstract"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "839340d5-c5a6-45db-96f9-fc806412be89",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013qEqJ8T3FnzR2AWXPMW739",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3054,
      "cache_read_input_tokens": 21013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3054,
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

_source line 184_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for SC-VLA 2602.21633 \"dense reward\" \"progress\" \"onli…",
  "usage": {
    "total_tokens": 26614,
    "tool_uses": 13,
    "duration_ms": 59351
  },
  "last_tool_name": "WebSearch",
  "uuid": "a90587ac-f4ed-4cc6-97cb-52864a53b233",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 185_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YMYuyt5s22pmzyRCSEoRhD`</summary>

```json
{
  "query": "SC-VLA 2602.21633 \"dense reward\" \"progress\" \"online\" training method NOT reinforcement learning explicitly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "aa5874ec-1448-47c9-9625-cc5170a188e8",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013qEqJ8T3FnzR2AWXPMW739",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3054,
      "cache_read_input_tokens": 21013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3054,
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

_source line 186_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for A2C2 2509.23224 \"trained jointly\" OR \"joint\" OR \"…",
  "usage": {
    "total_tokens": 26615,
    "tool_uses": 14,
    "duration_ms": 59388
  },
  "last_tool_name": "WebSearch",
  "uuid": "0c9bca99-c121-49a5-bd99-5bf6a6eb24d6",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 187_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01K6BMeWaYwbDJBqmouirqjy`</summary>

```json
{
  "query": "A2C2 2509.23224 \"trained jointly\" OR \"joint\" OR \"trained separately\" OR \"frozen VLA\" correction head training procedure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "36ed883c-0f9c-439c-8d11-81e872f06c62",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_013qEqJ8T3FnzR2AWXPMW739",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2487,
      "cache_creation_input_tokens": 3054,
      "cache_read_input_tokens": 21013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3054,
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

_source line 188_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for PLD \"self-improving VLA\" arXiv 2511.00091 \"magnit…",
  "usage": {
    "total_tokens": 20715,
    "tool_uses": 9,
    "duration_ms": 30459
  },
  "last_tool_name": "WebSearch",
  "uuid": "5eb8d638-5e13-4c15-ad08-5f7567c7394a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 189_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Gu8c2DqnVJQERbhB8gNm72`</summary>

```json
{
  "query": "PLD \"self-improving VLA\" arXiv 2511.00091 \"magnitude bound\" OR \"action bound\" OR \"correction bound\" residual RL scheduled xi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8f519216-c2ec-4827-a23e-6c68c7fea48c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QmpfDwddTnK9pU9Hn2MmPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 16099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4559,
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

_source line 190_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for arXiv 2503.15368 \"decaying relative correction\" D…",
  "usage": {
    "total_tokens": 20716,
    "tool_uses": 10,
    "duration_ms": 30800
  },
  "last_tool_name": "WebSearch",
  "uuid": "0a7c3b66-1c0d-4283-bc46-4c47250e057f",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 191_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UK2rHRhRdiVmf259G7zVf3`</summary>

```json
{
  "query": "arXiv 2503.15368 \"decaying relative correction\" DRC episode temporal decay early late correction teleoperation manipulation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "5844d9f7-9929-48bc-8327-95acd20bbb46",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01QmpfDwddTnK9pU9Hn2MmPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4559,
      "cache_read_input_tokens": 16099,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4559,
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

_source line 192_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for \"Zetian Zhou\" \"Shuo Yang\" \"Wenhao Luo\" conformal …",
  "usage": {
    "total_tokens": 23812,
    "tool_uses": 10,
    "duration_ms": 41824
  },
  "last_tool_name": "WebSearch",
  "uuid": "69e4912a-21bf-4a73-a937-63ded3d16570",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 193_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PUVMshRT2DxNMgmEuCRai6`</summary>

```json
{
  "query": "\"Zetian Zhou\" \"Shuo Yang\" \"Wenhao Luo\" conformal prediction control barrier functions safe RL ICRA 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e29146c6-075f-4221-b1be-8639b1089fe9",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WjgoEVfkvTifx4jLQVeT7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 21068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 194_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for SAFE VLA \"functional conformal prediction\" \"detec…",
  "usage": {
    "total_tokens": 23864,
    "tool_uses": 11,
    "duration_ms": 42844
  },
  "last_tool_name": "WebSearch",
  "uuid": "ea06cab1-84a4-4cc0-9d81-61a77dc82430",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 195_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5JTfiACjdE8NQndjUFZDF`</summary>

```json
{
  "query": "SAFE VLA \"functional conformal prediction\" \"detection timing\" fallback Qiao Gu NeurIPS 2025 method details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8fe01543-7648-4842-b232-b91cb6065c4d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01WjgoEVfkvTifx4jLQVeT7X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 661,
      "cache_creation_input_tokens": 1878,
      "cache_read_input_tokens": 21068,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1878,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 52,
      "service_tier": "standard",
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

_source line 196_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "description": "Searching for SmolVLA 450M parameters flow matching action expe…",
  "usage": {
    "total_tokens": 23386,
    "tool_uses": 9,
    "duration_ms": 23686
  },
  "last_tool_name": "WebSearch",
  "uuid": "65130d90-49e2-4ad6-956a-7a491408e3e6",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 197_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01431v2wrKksezsDpVL1SLvG`</summary>

```json
{
  "query": "SmolVLA 450M parameters flow matching action expert 2506.01844"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "929c8a96-de92-400b-96cb-5450d9a1a44c",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0123brjDEDtgFsw5xUWWuhGB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 922,
      "cache_creation_input_tokens": 6379,
      "cache_read_input_tokens": 16026,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6379,
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

_source line 198 · 2026-05-15T20:18:27.255Z_

<details><summary>↩ Tool result · `toolu_01Gu8c2DqnVJQERbhB8gNm72`</summary>

```text
Web search results for query: "PLD "self-improving VLA" arXiv 2511.00091 "magnitude bound" OR "action bound" OR "correction bound" residual RL scheduled xi"

No links found.

The search did not return any results. This could mean:

1. The specific arXiv paper (2511.00091) may not yet be indexed or widely available online
2. The exact combination of technical terms and identifiers may not match any indexed content
3. The paper might be very recent and not yet fully indexed by search engines

If you're looking for this arXiv paper, I'd recommend:
- Visiting arXiv.org directly and searching for the paper ID: 2511.00091
- Searching for just the paper ID (2511.00091) on arXiv
- Checking if the paper title or authors might help you find it through alternative search terms

Would you like me to try a different search approach, or do you have additional information about this paper that might help locate it?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "76bbd719-1596-4c2c-be91-b3cce09eae5d"
}
```

</details>

---

### Tool result

_source line 199 · 2026-05-15T20:18:28.066Z_

<details><summary>↩ Tool result · `toolu_01YMYuyt5s22pmzyRCSEoRhD`</summary>

```text
Web search results for query: "SC-VLA 2602.21633 "dense reward" "progress" "online" training method NOT reinforcement learning explicitly"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/html/2602.06508v1"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models","url":"https://arxiv.org/html/2512.14666"},{"title":"Improve Your VLA training: Using Reward Models to Filter Best Training Data - Tiny struggles","url":"https://www.tinystruggles.com/posts/improving_vla_training_with_reward_model/"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"NeurIPS A Practitioner's Guide to Multi-turn Agentic Reinforcement Learning","url":"https://neurips.cc/virtual/2025/127960"}]

I found the paper! Here are the search results for SC-VLA 2602.21633:

The Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination, and introduces an online action refinement module to reshape progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.

The method designs sparse world imagination by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

The paper was published on arXiv on February 25, 2026, and addresses limitations in standard Vision-Language-Action (VLA) models by combining world models with explicit self-improvement mechanisms through progress prediction and dense reward shaping.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "5fff188c-8f7b-455f-8872-c748e9f17f25"
}
```

</details>

---

### Tool result

_source line 200 · 2026-05-15T20:18:28.422Z_

<details><summary>↩ Tool result · `toolu_01K6BMeWaYwbDJBqmouirqjy`</summary>

```text
Web search results for query: "A2C2 2509.23224 "trained jointly" OR "joint" OR "trained separately" OR "frozen VLA" correction head training procedure"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224"},{"title":"1 APRIL 2024","url":"https://www.jcs.mil/Portals/36/Documents/JKO/JKO_Course_Catalog.pdf?ver=jy-yABnnNzXvOIvC1bZbUg%3D%3D"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"[2509.22199] MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training","url":"https://arxiv.org/abs/2509.22199"},{"title":"Forces Command Regulation (FORSCOM Reg.) 350-5: Joint Training Exercises | The Afterlives of Government Documents","url":"https://documentafterlives.newmedialab.cuny.edu/content/forces-command-regulation-forscom-reg-350-5-joint-training-exercises"},{"title":"BY ORDER OF THE SECRETARY OF THE AIR FORCE AIR FORCE INSTRUCTION 10-204","url":"https://static.e-publishing.af.mil/production/1/af_a3/publication/afi10-204/afi10-204.pdf"},{"title":"JOINT TRAINING MANUAL FOR THE ARMED FORCES OF THE UNITED STATES CJCSM 3500.03E","url":"https://www.jcs.mil/Portals/36/Documents/Doctrine/training/cjcsm3500_03e%20.pdf?ver=2017-12-29-171247-397"},{"title":"Joint Training","url":"https://www.jcs.mil/Doctrine/Joint-Training/"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"}]

I found the A2C2 paper (arxiv 2509.23224). Based on the search results, here's what I found regarding the correction head training procedure:

The correction head is trained on the same dataset as the base policy and, in principle, can be added to any off-the-shelf VLAs. Additionally, the approach requires no retraining of the base policy, which means the base VLA model remains frozen while the correction head is trained.

The search results indicate that the correction head operates as a lightweight add-on module that combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

While the search results don't provide explicit details about whether the correction head components themselves are "trained jointly" or "trained separately," they do confirm that the base VLA policy remains frozen and the correction head is trained independently on the same dataset.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a7b7b4e5-c173-45f6-8afb-8cf505c36837"
}
```

</details>

---

### Tool result

_source line 201 · 2026-05-15T20:18:28.486Z_

<details><summary>↩ Tool result · `toolu_011AWLPH1jHv6TWFGAPFWCSE`</summary>

```text
Web search results for query: "TRANSIC 2405.10315 "binary gate" OR "gating" residual action sim-to-real correction architecture details"

Links: [{"title":"[2405.10315] Transic: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://ar5iv.labs.arxiv.org/html/2405.10315"},{"title":"Transic: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://arxiv.org/html/2405.10315"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction","url":"https://www.researchgate.net/publication/380635321_TRANSIC_Sim-to-Real_Policy_Transfer_by_Learning_from_Online_Correction"},{"title":"TRANSIC: Human-in-the-Loop Sim-to-Real Transfer","url":"https://www.emergentmind.com/papers/2405.10315"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction | alphaXiv","url":"https://www.alphaxiv.org/overview/2405.10315v3"},{"title":"(PDF) TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction (2024) | Yunfan Jiang | 10 Citations","url":"https://scispace.com/papers/transic-sim-to-real-policy-transfer-by-learning-from-online-2heee0h3xd"},{"title":"TRANSIC | Sim-to-Real Policy Transfer by Learning from ...","url":"https://transic-robot.github.io/"},{"title":"TRANSIC: Sim-to-Real Policy Transfer by Learning ...","url":"https://arxiv-sanity-lite.com/?rank=pid&pid=2405.10315"},{"title":"GitHub - transic-robot/transic · GitHub","url":"https://github.com/transic-robot/transic"},{"title":"When Robot Shows Human-Like Recovery and Safety Behaviors | HackerNoon","url":"https://hackernoon.com/when-robot-shows-human-like-recovery-and-safety-behaviors"}]

Based on the search results for TRANSIC (arXiv 2405.10315), here are the key architecture details regarding the binary gate and gating mechanism for the residual action correction:

## Gated Residual Policy Architecture

Learning a gating function to control whether to apply residual actions or not leads to better empirical performance, creating what is called a learned gated residual policy.

### Gating Function Design

The gating function shares the same feature encoder with the residual policy and is jointly learned through classification on the same correction dataset. At inference time, a binary gate is used to determine whether to apply the predicted residual actions.

### Integrated Deployment Policy

The policy effectively being deployed to autonomously complete tasks is an integration of base policy and residual policy, gated by the gating function.

### Why Gating Was Adopted

In practice, learning a gating function to predict whether to apply the residual policy or not leads to smoother and more human-like behaviors. This gating mechanism was found to be necessary as Transic learns gated residual policies only from human correction to avoid catastrophic forgetting of the base simulation policy.

### Performance of Learned Gating

The learned gating mechanism only incurs negligible performance drops compared to human gating, suggesting that Transic can reliably operate in a fully autonomous setting once the gating mechanism is learned.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "739eab2e-c2f6-4fb8-8925-07e7ff5b3e23"
}
```

</details>

---

### Tool result

_source line 202 · 2026-05-15T20:18:29.593Z_

<details><summary>↩ Tool result · `toolu_01TREnyon22F4yEMTt5jp47x`</summary>

```text
Web search results for query: "ReconVLA arxiv 2604.16677 action selection "multiple samples" OR "N samples" OR "best action" OR "conformal score" methodology abstract"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Equivariant Action Sampling for Reinforcement Learning and Planning","url":"https://arxiv.org/html/2412.12237v1"},{"title":"[2507.04187] Where to Intervene: Action Selection in Deep Reinforcement Learning","url":"https://arxiv.org/abs/2507.04187"},{"title":"Where to Intervene: Action Selection in Deep Reinforcement Learning","url":"https://arxiv.org/html/2507.04187v1"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Efficient Action-Constrained Reinforcement Learning via Acceptance-Rejection Method and Augmented MDPs","url":"https://arxiv.org/html/2503.12932v1"},{"title":"Automating Aggregation Strategy Selection in Federated Learning","url":"https://arxiv.org/html/2604.08056v1"},{"title":"Context Engineering: A Methodology for Structured Human-AI Collaboration","url":"https://arxiv.org/html/2604.04258v1"}]

Based on the search results, I found the ReconVLA paper (arxiv 2604.16677). Here's what the methodology describes regarding action selection:

ReconVLA augments its base VLA model with a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability. 

The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. The framework leverages conformal prediction to compute statistically rigorous and actionable confidence bounds on the model's action outputs, incorporating conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process.

The methodology focuses on addressing the problem that VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4cddf518-a29e-4de5-8f93-ef65fc3f585d"
}
```

</details>

---

### Tool result

_source line 203 · 2026-05-15T20:18:29.790Z_

<details><summary>↩ Tool result · `toolu_01PUVMshRT2DxNMgmEuCRai6`</summary>

```text
Web search results for query: ""Zetian Zhou" "Shuo Yang" "Wenhao Luo" conformal prediction control barrier functions safe RL ICRA 2025"

Links: [{"title":"Wenhao Luo - Computer Science - University of Illinois Chicago","url":"https://www.cs.uic.edu/~wenhao/"},{"title":"[2503.17678] Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction","url":"https://arxiv.org/abs/2503.17678"},{"title":"[PDF] Dynamic Control Barrier Function-based Model Predictive Control to Safety-Critical Obstacle-Avoidance of Mobile Robot | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Dynamic-Control-Barrier-Function-based-Model-to-of-Jian-Yan/c75841c3223bac648fbf347072e38aa3373278b8"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=1000&show=100"},{"title":"Machine Learning Jul 2025","url":"https://arxiv.org/list/cs.LG/2025-07?skip=1075&show=2000"},{"title":"Selective Conformal Risk Control Yunpeng Xu1 Wenge Guo2 Zhi Wei1","url":"https://www.arxiv.org/pdf/2512.12844"},{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"Safety, Robustness, and Interpretability in Machine Learning Samuel Pfrommer","url":"https://www2.eecs.berkeley.edu/Pubs/TechRpts/2025/EECS-2025-67.pdf"},{"title":"Artificial Intelligence Jun 2025","url":"https://arxiv.org/list/cs.AI/2025-06?skip=1800&show=2000"}]

Based on the search results, I found a relevant paper matching your query:

The paper "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction" by Hao Zhou, Yanze Zhang, and Wenhao Luo was accepted to the IEEE International Conference on Robotics and Automation (ICRA) 2025.

The paper proposes a provably sample efficient episodic safe learning framework that remains robust across various model choices with quantified uncertainty for online control tasks, employing Quadrature Fourier Features (QFF) for kernel function approximation of Gaussian Processes (GPs) to enable efficient approximation of unknown dynamics.

However, I should note that the search results show the authors as **Hao Zhou, Yanze Zhang, and Wenhao Luo** rather than the names you mentioned (Zetian Zhou, Shuo Yang, Wenhao Luo). The paper does focus on combining conformal prediction with safe reinforcement learning for ICRA 2025, which aligns with the topic of your query. It's possible the author names in your query may have been slightly different, or there could be multiple related papers on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8829c564-3a94-4416-a3f5-d73054ae1ce8"
}
```

</details>

---

### Tool result

_source line 204 · 2026-05-15T20:18:31.112Z_

<details><summary>↩ Tool result · `toolu_01UK2rHRhRdiVmf259G7zVf3`</summary>

```text
Web search results for query: "arXiv 2503.15368 "decaying relative correction" DRC episode temporal decay early late correction teleoperation manipulation"

Links: [{"title":"[2503.15368] Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/abs/2503.15368"},{"title":"Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation","url":"https://arxiv.org/html/2503.15368"},{"title":"[2503.19357] Correcting Deviations from Normality: A Reformulated Diffusion Model for Multi-Class Unsupervised Anomaly Detection","url":"https://arxiv.org/abs/2503.19357"},{"title":"Recoil-induced errors and their correction in photon-mediated entanglement between atomic qubits","url":"https://arxiv.org/html/2503.16837v1"},{"title":"Abstract","url":"https://arxiv.org/html/2503.20610"},{"title":"A correspondence between quantum error correcting ...","url":"https://arxiv.org/pdf/2412.15317"},{"title":"Passive quantum error correction of photon loss at breakeven","url":"https://arxiv.org/html/2510.19794v1"},{"title":"On the Importance of Error Mitigation for Quantum Computation","url":"https://arxiv.org/html/2503.17243v1"},{"title":"[2503.17759] Approximate Quantum Error Correction with 1D Log-Depth Circuits","url":"https://arxiv.org/abs/2503.17759"},{"title":"Error-Corrected Eternal Lifetime Storage","url":"https://arxiv.org/html/2503.22355"}]

I found the paper! Here are the search results for arXiv paper 2503.15368:

## Paper: Online Imitation Learning for Manipulation via Decaying Relative Correction through Teleoperation

The paper proposes a correction method termed Decaying Relative Correction (DRC) which is based upon the spatial offset vector provided by the expert and exists temporarily, and which reduces the intervention steps required by an expert.

### Key Results

DRC reduces the required expert intervention rate by 30% compared to a standard absolute corrective method. Integrating DRC within an online imitation learning framework rapidly increases the success rate of manipulation tasks such as raspberry harvesting and cloth wiping.

### How DRC Works

The relative correction motion provided by the experts teleoperation provides the vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate. Since trends in relative corrections (e.g., continuous adjustments over time) could remain valid for subsequent states or actions, leveraging this temporal consistency is crucial for improving the efficiency of online imitation learning systems.

### Experimental Setup

This correction mode is made possible by a use of 8 degree of freedom (DoF) teleoperation system and cable driven robot. Using this method shows how the success rate of two tasks (raspberry harvesting and wiping with a cloth) increases from 30% to above 80%.

The paper was submitted to arXiv on March 19, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "00452f54-1810-4a12-9d62-6b8f1de2c959"
}
```

</details>

---

### Tool result

_source line 205 · 2026-05-15T20:18:31.558Z_

<details><summary>↩ Tool result · `toolu_01B5JTfiACjdE8NQndjUFZDF`</summary>

```text
Web search results for query: "SAFE VLA "functional conformal prediction" "detection timing" fallback Qiao Gu NeurIPS 2025 method details"

Links: [{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"NeurIPS Poster SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://neurips.cc/virtual/2025/poster/117510"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"[2506.09937] SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/abs/2506.09937"},{"title":"NeurIPS Poster Conformal Prediction Beyond the Seen: A Missing Mass Perspective for Uncertainty Quantification in Generative Models","url":"https://neurips.cc/virtual/2025/loc/san-diego/poster/118606"},{"title":"NeurIPS Poster Conformal Prediction Beyond the Horizon: Distribution-Free Inference for Policy Evaluation","url":"https://neurips.cc/virtual/2025/poster/118031"},{"title":"NeurIPS Poster Conformal Prediction for Time-series Forecasting with Change Points","url":"https://neurips.cc/virtual/2025/poster/118881"},{"title":"NeurIPS Poster One Sample is Enough to Make Conformal Prediction Robust","url":"https://neurips.cc/virtual/2025/poster/116678"},{"title":"Conformal Prediction for Time-series Forecasting with Change Points | OpenReview","url":"https://openreview.net/forum?id=HgLaVgCpCl"},{"title":"NeurIPS Poster Topology-Aware Conformal Prediction for Stream Networks","url":"https://neurips.cc/virtual/2025/poster/118542"}]

Based on the search results, I found detailed information about the SAFE method presented by Qiao Gu and colleagues at NeurIPS 2025:

## Method Overview

SAFE is a failure detector for generalist robot policies such as VLAs that learns from VLA internal features and predicts a single scalar indicating the likelihood of task failure.

## Key Components

SAFE extracts latent features from the last layer of a VLA model and sequentially processes these features using an MLP or LSTM backbone to predict a failure score.

## Functional Conformal Prediction for Detection Timing

SAFE determines a time-varying threshold using functional conformal prediction (CP) on a hold-out calibration set, and if the predicted score exceeds the threshold during testing, SAFE confidently detects a failure. By varying the significance level α used in functional conformal prediction, SAFE can control the conservativeness of failure detection, which gives a trade-off between detection accuracy and detection time, plotting balanced accuracy against average detection time for different α values.

## Training and Evaluation

SAFE is trained on both successful and failed rollouts and is evaluated on unseen tasks. The method is tested on OpenVLA, π₀, and π₀-FAST in both simulated and real-world environments, achieving state-of-the-art failure detection performance and the best trade-off between accuracy and detection time using conformal prediction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "bf581494-d635-4ae3-9041-91ad0c3b84d9"
}
```

</details>

---

### Tool result

_source line 206 · 2026-05-15T20:18:32.299Z_

<details><summary>↩ Tool result · `toolu_014LuVzRVBr8hVELjjhGyHrK`</summary>

```text
Web search results for query: "arXiv 1812.06298 "residual policy learning" zero initialization bounded action corrections classical controller framework"

Links: [{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"[1812.06298] Residual Policy Learning - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.06298"},{"title":"Residual Policy Learning","url":"https://arxiv.org/pdf/1812.06298v2"},{"title":"Residual Policy Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2018arXiv181206298S/abstract"},{"title":"[1812.06298v2] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298v2"},{"title":"Accelerating Residual Reinforcement Learning with Uncertainty Estimation","url":"https://arxiv.org/html/2506.17564v1"},{"title":"From Imitation to Refinement – Residual RL for Precise Assembly","url":"https://arxiv.org/html/2407.16677v4"},{"title":"[2602.10539] What Makes Value Learning Efficient in Residual Reinforcement Learning?","url":"https://arxiv.org/abs/2602.10539"},{"title":"Machine Learning","url":"https://arxiv.org/list/cs.LG/new"},{"title":"Computer Science Apr 2025","url":"https://www.arxiv.org/list/cs/2025-04?skip=1775&show=2000"}]

I found the paper arXiv 1812.06298 on "Residual Policy Learning." Here's what the search reveals:

The paper presents Residual Policy Learning (RPL): a simple method for improving nondifferentiable policies using model-free deep reinforcement learning that thrives in complex robotic manipulation tasks where good but imperfect controllers are available.

In these tasks, reinforcement learning from scratch remains data-inefficient or intractable, but learning a residual on top of the initial controller can yield substantial improvements.

The researchers study RPL in six challenging MuJoCo tasks involving partial observability, sensor noise, model misspecification, and controller miscalibration. For initial controllers, they consider both hand-designed policies and model-predictive controllers with known or learned transition models.

There are two ways to see the role of the residual: if the initial policy is nearly perfect, the residual may be viewed as a corrective term; but if the initial policy is far from ideal, the outputs may be interpreted as merely "hints" to guide exploration.

Related to your mention of bounded action corrections, residual reinforcement learning enables stable online refinement of expressive pretrained policies by freezing the base and learning only bounded corrections.

The paper demonstrates how RPL combines classical control approaches with deep reinforcement learning to achieve results that neither method alone can accomplish.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "079160b6-5dfe-46e9-ba92-a31a63c269fa"
}
```

</details>

---

### Tool result

_source line 207 · 2026-05-15T20:18:33.244Z_

<details><summary>↩ Tool result · `toolu_01431v2wrKksezsDpVL1SLvG`</summary>

```text
Web search results for query: "SmolVLA 450M parameters flow matching action expert 2506.01844"

Links: [{"title":"SmolVLA: Efficient Vision-Language-Action Model trained on Lerobot Community Data","url":"https://huggingface.co/blog/smolvla"},{"title":"arXiv:2506.01844v1 [cs.LG] 2 Jun 2025 SmolVLA: A vision-language-action model","url":"https://arxiv.org/pdf/2506.01844"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://arxiv.org/abs/2506.01844"},{"title":"Paper page - SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"https://huggingface.co/papers/2506.01844"},{"title":"SmolVLA: Efficient Vision Language Action Model - LeRobot","url":"https://learnopencv.com/smolvla-lerobot-vision-language-action-model/"},{"title":"SmolVLA: A vision-language-action model for affordable and efficient robotics","url":"https://arxiv.org/html/2506.01844v1"},{"title":"blog/zh/smolvla.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/zh/smolvla.md"},{"title":"[2506.01844] SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics","url":"http://export.arxiv.org/abs/2506.01844"},{"title":"zk0 Architecture: Federated Learning for SmolVLA Robotics AI | zk0 - Decentralized Robotics AI","url":"https://zk0.bot/docs/ARCHITECTURE.html"},{"title":"phospho starter pack documentation","url":"https://docs.phospho.ai/learn/policies"}]

Based on the search results, here's what I found about SmolVLA 450M parameters with flow matching and action expert:

## Overview

SmolVLA is a compact (450M), open-source Vision-Language-Action model for robotics that runs on consumer hardware. SmolVLA is a small, efficient, and community-driven VLA that drastically reduces both training and inference costs, while retaining competitive performance.

## Architecture & Technical Details

Architecturally, it combines Transformers with flow-matching decoders, and is optimized for speed and low-latency inference. More specifically, the action expert uses a flow matching transformer (~100M trainable parameters).

## Performance

SmolVLA-450M outperforms much larger VLAs and strong baselines such as ACT on simulation (LIBERO, Meta-World) and real-world tasks (SO100, SO101). Despite using fewer than 30k training episodes—an order of magnitude less than other VLAs—SmolVLA matches or exceeds the performance of much larger models, both in simulation and the real world.

## Deployment

SmolVLA is designed to be trained on a single GPU and deployed on consumer-grade GPUs or even CPUs. It supports asynchronous inference for 30% faster response and 2× task throughput.

The paper reference 2506.01844 was published on June 2, 2025, by authors including Mustafa Shukor and others from Hugging Face and related institutions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d990d6a0-a58f-493f-a6f2-c3f63fb402c6"
}
```

</details>

---

### System

_source line 208_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for arXiv 2507.20941 \"Conformalized Gaussian Scoring\"…",
  "usage": {
    "total_tokens": 25818,
    "tool_uses": 12,
    "duration_ms": 53872
  },
  "last_tool_name": "WebSearch",
  "uuid": "fbe832c3-1d34-4c70-8deb-acf93addd685",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 209_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EjAeAggup2q1o2Tj4duC7S`</summary>

```json
{
  "query": "arXiv 2507.20941 \"Conformalized Gaussian Scoring\" CGS Mahalanobis nonconformity score prediction regions covariance method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "8c6f30c0-bc08-4cd1-bbb0-13e852977b1d",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KEqaoQ22xU3GT2L4ugNKVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 22946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 210_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "aa5885ddef856d60d",
  "tool_use_id": "toolu_01F79KsYf2riw7ACdusRvggw",
  "status": "completed",
  "output_file": "",
  "summary": "Verify VLA training-time citations",
  "usage": {
    "total_tokens": 23964,
    "tool_uses": 9,
    "duration_ms": 64200
  },
  "uuid": "80edf767-b915-472c-838b-ae02df63a94a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 211 · 2026-05-15T20:18:35.991Z_

<details><summary>↩ Tool result · `toolu_01F79KsYf2riw7ACdusRvggw`</summary>

```text
I have sufficient information to evaluate all 5 citations. Here are the findings:

---

**1. robustvla2025** (arXiv: 2511.01331) — CORRECT

- Paper claims: Training-time method with "robustness-aware objectives"; "combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations."
- Actual method: Exactly as described. The paper introduces online RL post-training with two key regularizations—Jacobian regularization (addressing sensitivity to observation/visual noise) and smoothness regularization (addressing action perturbations). The Jacobian regularization specifically mitigates sensitivity to observation noise. This is an accurate description.

---

**2. srpo2025** (arXiv: 2511.15605) — NEEDS_REVIEW

- Paper claims: Training-time method; "applies self-referential RL fine-tuning, using the policy's own rollouts as training signal."
- Actual method: SRPO does use the policy's own successful trajectories from the current training batch as self-reference (self-referential), and it is RL-based fine-tuning. However, the claim slightly oversimplifies: the training signal is not just "own rollouts" but specifically own *successful* rollouts used as reference to assign progress-wise rewards to *failed* trajectories—enabled by a latent world model's representations. The "own rollouts as training signal" framing is directionally correct but omits the crucial distinction that failed trajectories are compared against successful in-batch ones. Classifying as NEEDS_REVIEW because the description is not wrong but imprecise enough to potentially mislead about what "self-referential" means mechanistically.

---

**3. digflow2025** (arXiv: 2512.01715) — INCORRECT

- Paper claims: "regularizes the flow-matching denoising trajectory via a discrepancy-guided objective."
- Actual method: DiG-Flow does not regularize the denoising trajectory itself. Instead, it operates at the representation level: it computes distributional discrepancy between observation embeddings and action embeddings (from the vision-language backbone and policy head respectively), and uses this as a gating signal (DiG-Block) that rebalances control between the foundation model and the flow expert. The flow matching *path/target vector field* is explicitly stated to be unmodified. The paper also includes a refinement module (DiG-Refine) operating in action space post-flow. Describing it as "regularizing the denoising trajectory" misrepresents the mechanism—the intervention is at the representation/embedding level, not on the trajectory/denoising path.

---

**4. liu2026ttvla** (arXiv: 2601.06748) — CORRECT

- Paper claims: "blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment."
- Actual method: The paper (TT-VLA) proposes exactly this: test-time RL adaptation with a dense reward mechanism using step-by-step task-progress signals to refine action policies during inference while preserving prior training. Gradient updates happen at test time. The per-task reward design requirement and gradient-update-at-deployment characterization are accurate limitations implied by the approach.

---

**5. fei2025liberoplus** (arXiv: 2510.13626) — NEEDS_REVIEW

- Paper claims: "under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially."
- Actual findings: LIBERO-Plus does show substantial performance degradation (95% → below 30%) under perturbations, and the benchmark does cover light conditions and sensor noise. However, the specific framing of "object appearance changes" does not precisely match the paper's seven perturbation dimensions (objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise). The paper covers *background textures* and *objects layout*, not "object appearance changes" per se. More importantly, the paper's headline finding is that models are most sensitive to camera viewpoints and robot initial states—not the three dimensions highlighted in the claim. The claim is selectively accurate but omits the paper's most prominent findings and mis-describes one perturbation type. Classifying as NEEDS_REVIEW rather than INCORRECT because the general conclusion (performance degrades under these types of shifts) is supported, but the specific attribution is imprecise.

---

**Summary table:**

| Citation | Verdict |
|---|---|
| robustvla2025 | CORRECT |
| srpo2025 | NEEDS_REVIEW |
| digflow2025 | INCORRECT |
| liu2026ttvla | CORRECT |
| fei2025liberoplus | NEEDS_REVIEW |

Sources:
- [RobustVLA arXiv 2511.01331](https://arxiv.org/abs/2511.01331)
- [SRPO arXiv 2511.15605](https://arxiv.org/abs/2511.15605)
- [DiG-Flow arXiv 2512.01715](https://arxiv.org/abs/2512.01715)
- [On-the-Fly VLA Adaptation arXiv 2601.06748](https://arxiv.org/abs/2601.06748)
- [LIBERO-Plus arXiv 2510.13626](https://arxiv.org/abs/2510.13626)

agentId: aa5885ddef856d60d (use SendMessage with to: 'aa5885ddef856d60d' to continue this agent)
&lt;usage>total_tokens: 25203
tool_uses: 9
duration_ms: 64202&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "a6cda516-5819-4f33-a49e-74d7c330d143",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. robustvla2025** (arXiv: 2511.01331)\nTitle: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\" with \"robustness-aware objectives\"\n- Related work: \"combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations\"\n\n**2. srpo2025** (arXiv: 2511.15605)\nTitle: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"applies self-referential RL fine-tuning, using the policy's own rollouts as training signal\"\n\n**3. digflow2025** (arXiv: 2512.01715)\nTitle: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\nPaper claims:\n- Introduction: grouped as \"Training-time methods\"\n- Related work: \"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective\"\n\n**4. liu2026ttvla** (arXiv: 2601.06748)\nTitle: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\nPaper claims:\n- Related work: \"blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment\"\n\n**5. fei2025liberoplus** (arXiv: 2510.13626)\nTitle: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\nPaper claims:\n- Introduction: \"under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially\"\n\nSearch for each paper on arXiv and verify the method descriptions.",
    "agentId": "aa5885ddef856d60d",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I have sufficient information to evaluate all 5 citations. Here are the findings:\n\n---\n\n**1. robustvla2025** (arXiv: 2511.01331) — CORRECT\n\n- Paper claims: Training-time method with \"robustness-aware objectives\"; \"combines RL post-training with Jacobian regularization to stabilize action predictions under visual perturbations.\"\n- Actual method: Exactly as described. The paper introduces online RL post-training with two key regularizations—Jacobian regularization (addressing sensitivity to observation/visual noise) and smoothness regularization (addressing action perturbations). The Jacobian regularization specifically mitigates sensitivity to observation noise. This is an accurate description.\n\n---\n\n**2. srpo2025** (arXiv: 2511.15605) — NEEDS_REVIEW\n\n- Paper claims: Training-time method; \"applies self-referential RL fine-tuning, using the policy's own rollouts as training signal.\"\n- Actual method: SRPO does use the policy's own successful trajectories from the current training batch as self-reference (self-referential), and it is RL-based fine-tuning. However, the claim slightly oversimplifies: the training signal is not just \"own rollouts\" but specifically own *successful* rollouts used as reference to assign progress-wise rewards to *failed* trajectories—enabled by a latent world model's representations. The \"own rollouts as training signal\" framing is directionally correct but omits the crucial distinction that failed trajectories are compared against successful in-batch ones. Classifying as NEEDS_REVIEW because the description is not wrong but imprecise enough to potentially mislead about what \"self-referential\" means mechanistically.\n\n---\n\n**3. digflow2025** (arXiv: 2512.01715) — INCORRECT\n\n- Paper claims: \"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective.\"\n- Actual method: DiG-Flow does not regularize the denoising trajectory itself. Instead, it operates at the representation level: it computes distributional discrepancy between observation embeddings and action embeddings (from the vision-language backbone and policy head respectively), and uses this as a gating signal (DiG-Block) that rebalances control between the foundation model and the flow expert. The flow matching *path/target vector field* is explicitly stated to be unmodified. The paper also includes a refinement module (DiG-Refine) operating in action space post-flow. Describing it as \"regularizing the denoising trajectory\" misrepresents the mechanism—the intervention is at the representation/embedding level, not on the trajectory/denoising path.\n\n---\n\n**4. liu2026ttvla** (arXiv: 2601.06748) — CORRECT\n\n- Paper claims: \"blurs the training/inference boundary by adapting VLA parameters at test time through RL with progress rewards, but still requires per-task reward design and gradient updates during deployment.\"\n- Actual method: The paper (TT-VLA) proposes exactly this: test-time RL adaptation with a dense reward mechanism using step-by-step task-progress signals to refine action policies during inference while preserving prior training. Gradient updates happen at test time. The per-task reward design requirement and gradient-update-at-deployment characterization are accurate limitations implied by the approach.\n\n---\n\n**5. fei2025liberoplus** (arXiv: 2510.13626) — NEEDS_REVIEW\n\n- Paper claims: \"under the distribution shifts common in deployment—object appearance changes, lighting variation, sensor noise—performance degrades substantially.\"\n- Actual findings: LIBERO-Plus does show substantial performance degradation (95% → below 30%) under perturbations, and the benchmark does cover light conditions and sensor noise. However, the specific framing of \"object appearance changes\" does not precisely match the paper's seven perturbation dimensions (objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise). The paper covers *background textures* and *objects layout*, not \"object appearance changes\" per se. More importantly, the paper's headline finding is that models are most sensitive to camera viewpoints and robot initial states—not the three dimensions highlighted in the claim. The claim is selectively accurate but omits the paper's most prominent findings and mis-describes one perturbation type. Classifying as NEEDS_REVIEW rather than INCORRECT because the general conclusion (performance degrades under these types of shifts) is supported, but the specific attribution is imprecise.\n\n---\n\n**Summary table:**\n\n| Citation | Verdict |\n|---|---|\n| robustvla2025 | CORRECT |\n| srpo2025 | NEEDS_REVIEW |\n| digflow2025 | INCORRECT |\n| liu2026ttvla | CORRECT |\n| fei2025liberoplus | NEEDS_REVIEW |\n\nSources:\n- [RobustVLA arXiv 2511.01331](https://arxiv.org/abs/2511.01331)\n- [SRPO arXiv 2511.15605](https://arxiv.org/abs/2511.15605)\n- [DiG-Flow arXiv 2512.01715](https://arxiv.org/abs/2512.01715)\n- [On-the-Fly VLA Adaptation arXiv 2601.06748](https://arxiv.org/abs/2601.06748)\n- [LIBERO-Plus arXiv 2510.13626](https://arxiv.org/abs/2510.13626)"
      }
    ],
    "totalDurationMs": 64202,
    "totalTokens": 25203,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 845,
      "cache_creation_input_tokens": 3015,
      "cache_read_input_tokens": 20046,
      "output_tokens": 1297,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3015
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 845,
          "output_tokens": 1297,
          "cache_read_input_tokens": 20046,
          "cache_creation_input_tokens": 3015,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3015,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  }
}
```

</details>

---

### System

_source line 212_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "description": "Searching for Zollo Zemel VLA calibration 2507.17383 \"prompt en…",
  "usage": {
    "total_tokens": 25856,
    "tool_uses": 13,
    "duration_ms": 54618
  },
  "last_tool_name": "WebSearch",
  "uuid": "c4523f95-89c8-44cf-a56a-d1298a630bd8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 213_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014BUFKzL2GmUJYY3u96eeWz`</summary>

```json
{
  "query": "Zollo Zemel VLA calibration 2507.17383 \"prompt ensemble\" \"Platt scaling\" first author name"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9f0acaf0-9180-45e2-a24e-96763a36087a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KEqaoQ22xU3GT2L4ugNKVw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2576,
      "cache_read_input_tokens": 22946,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2576,
        "ephemeral_1h_input_tokens": 0
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

### System

_source line 214_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for site:arxiv.org/html/2604.16677 ReconVLA \"action s…",
  "usage": {
    "total_tokens": 29237,
    "tool_uses": 15,
    "duration_ms": 72767
  },
  "last_tool_name": "WebSearch",
  "uuid": "4f438acc-5c12-4725-927d-0ddc7cd66666",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 215_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LTTjqumvMjAxPEvsgz3nLf`</summary>

```json
{
  "query": "site:arxiv.org/html/2604.16677 ReconVLA \"action samples\" OR \"multiple\" OR \"N actions\" OR \"sample\" conformal"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4abe7255-73c7-4722-b990-b3108f898378",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KU8MsN4W8zn9n4xBVPhPw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1633,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3474,
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

_source line 216_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for site:arxiv.org/html/2602.21633 SC-VLA \"reinforcem…",
  "usage": {
    "total_tokens": 29238,
    "tool_uses": 16,
    "duration_ms": 73232
  },
  "last_tool_name": "WebSearch",
  "uuid": "6246c643-326d-420e-a9e5-6fe377c4fef8",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 217_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MqPLLTnyP8rMKMAmDGxDrG`</summary>

```json
{
  "query": "site:arxiv.org/html/2602.21633 SC-VLA \"reinforcement learning\" OR \"RL\" OR \"residual\" online action refinement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "80f804c2-3f53-432a-9570-e68a2ebecd79",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KU8MsN4W8zn9n4xBVPhPw2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1633,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 24067,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3474,
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

_source line 218_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for ar5iv residual policy learning 1812.06298 \"zero\" …",
  "usage": {
    "total_tokens": 23792,
    "tool_uses": 11,
    "duration_ms": 46509
  },
  "last_tool_name": "WebSearch",
  "uuid": "6e1f5131-8615-4d02-81b5-0e8c6c88f89a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 219_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WUC7CjNbdpwootg2TTVo9E`</summary>

```json
{
  "query": "ar5iv residual policy learning 1812.06298 \"zero\" initialization \"bounded\" clipping action space classical controller"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b660bb56-fb05-45a2-acaa-10a5b178a03f",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KUDd3xMzQtZ8cZkfZ8vKPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 20658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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

_source line 220 · 2026-05-15T20:18:39.579Z_

<details><summary>↩ Tool result · `toolu_01LTTjqumvMjAxPEvsgz3nLf`</summary>

```text
Web search results for query: "site:arxiv.org/html/2604.16677 ReconVLA "action samples" OR "multiple" OR "N actions" OR "sample" conformal"

No links found.

I wasn't able to find results with that specific query. This appears to be a search for a specific arXiv paper (2604.16677) with particular search terms. The site operator syntax you used may not work as expected with my search tool, and the combination of technical terms specific to that paper may not yield search results.

If you're looking for information about this arXiv paper, I'd recommend:
1. Visiting the paper directly at `arxiv.org/html/2604.16677`
2. Searching for "ReconVLA arxiv" to find the paper
3. Searching for the specific terms without the site operator

Would you like me to try a different search approach, such as searching for "ReconVLA" more broadly?


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "233d1e91-7bbb-4772-a83e-12ea608d3297"
}
```

</details>

---

### System

_source line 221_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Searching for PLD \"probe learn distill\" VLA residual RL 2511.00…",
  "usage": {
    "total_tokens": 23793,
    "tool_uses": 12,
    "duration_ms": 47324
  },
  "last_tool_name": "WebSearch",
  "uuid": "a129d5e1-3a32-408d-b0aa-d23ca0c876a1",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 222_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TRAWEyNguCsYPW1AwMHnfB`</summary>

```json
{
  "query": "PLD \"probe learn distill\" VLA residual RL 2511.00091 \"action bound\" OR \"clipping\" OR \"magnitude\" OR \"epsilon\" OR \"xi\" correction range training curriculum"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "66ec8f6c-5b05-4985-8b78-2d01aaa3f651",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KUDd3xMzQtZ8cZkfZ8vKPD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1976,
      "cache_creation_input_tokens": 1099,
      "cache_read_input_tokens": 20658,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1099,
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

_source line 223 · 2026-05-15T20:18:41.033Z_

<details><summary>↩ Tool result · `toolu_014BUFKzL2GmUJYY3u96eeWz`</summary>

```text
Web search results for query: "Zollo Zemel VLA calibration 2507.17383 "prompt ensemble" "Platt scaling" first author name"

Links: [{"title":"[2507.17383] Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/abs/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models Thomas Zollo","url":"https://arxiv.org/pdf/2507.17383"},{"title":"(PDF) Confidence Calibration in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"},{"title":"Confidence Calibration in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=aiPC7jAd2f"},{"title":"Improving Predictor Reliability with Selective Recalibration","url":"https://arxiv.org/html/2410.05407v1"},{"title":"Platt Scaling for Model Calibration: A Visual Guide","url":"https://blog.dailydoseofds.com/p/platt-scaling-for-model-calibration"},{"title":"Using Platt’s scaling for calibration after undersampling — limitations and how to address them | OpenReview","url":"https://openreview.net/forum?id=80b2zaeTUe"},{"title":"(PDF) Using Platt's scaling for calibration after undersampling -- limitations and how to address them","url":"https://www.researchgate.net/publication/385216394_Using_Platt's_scaling_for_calibration_after_undersampling_--_limitations_and_how_to_address_them"},{"title":"Optimal and Provable Calibration in High-Dimensional Binary Classification: Angular Calibration and Platt Scaling","url":"https://arxiv.org/html/2502.15131v1"}]

Based on the search results, I found the information about the paper with arXiv ID 2507.17383:

The first author name is Thomas Zollo, and the second author is Richard Zemel, both from Columbia University.

The paper is titled "Confidence Calibration in Vision-Language-Action Models," which presents a study of confidence calibration in vision-language-action (VLA) foundation models and introduces two lightweight techniques to remedy miscalibration: prompt ensembles and action-wise Platt scaling.

Note: The paper focuses on Vision-Language-Action (VLA) models for robotics, not VLA calibration in the context of radio astronomy as the "VLA" acronym might suggest.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3decffd3-2459-4449-960f-d9d43f7c65c6"
}
```

</details>

---

### Tool result

_source line 224 · 2026-05-15T20:18:42.725Z_

<details><summary>↩ Tool result · `toolu_01EjAeAggup2q1o2Tj4duC7S`</summary>

```text
Web search results for query: "arXiv 2507.20941 "Conformalized Gaussian Scoring" CGS Mahalanobis nonconformity score prediction regions covariance method"

Links: [{"title":"[2507.20941] Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/abs/2507.20941"},{"title":"(PDF) Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://www.researchgate.net/publication/394081259_Multivariate_Conformal_Prediction_via_Conformalized_Gaussian_Scoring"},{"title":"[PDF] Multivariate Conformal Prediction via Conformalized Gaussian Scoring | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-via-Conformalized-Braun-Berta/eb97eda6c4159d62c1fd5d2ca6404b323e44123c"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian ...","url":"https://ribbitribbit.co/paper/arxiv.2507.20941-Multivariate-Conformal-Prediction-via-Conformalized-Gaussian-Scoring"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/pdf/2507.20941"},{"title":"Methodology Jul 2025","url":"https://www.arxiv.org/list/stat.ME/2025-07?skip=350&show=500"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/html/2507.20941"},{"title":"A Kernel Nonconformity Score for Multivariate Conformal Prediction","url":"https://arxiv.org/html/2604.21595"},{"title":"Statistics Jul 2025","url":"https://www.arxiv.org/list/stat/2025-07?skip=550&show=2000"},{"title":"Statistics","url":"https://www.arxiv.org/list/stat/recent?skip=111&show=25"}]

Based on the web search results, here's what I found about arXiv paper 2507.20941:

## Paper Overview

The paper is titled "Multivariate Standardized Residuals for Conformal Prediction" (arXiv 2507.20941), authored by Sacha Braun, Eugène Berta, Michael I. Jordan, and Francis Bach.

## Core Contributions

While split conformal prediction guarantees marginal coverage, the paper addresses the need for conditional coverage in uncertainty quantification, as naive conformal scores suffer from poor conditional coverage in heteroskedastic settings.

The work proposes a natural extension of non-conformity score normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.

## Key Technical Method

The CDF-based score reduces to a Mahalanobis distance in the case of Gaussian scores, yielding a closed-form expression that can be directly conformalized. The approach uses the Mahalanobis distance induced by a learned local covariance as a non-conformity score to provide a closed-form, computationally efficient mechanism for capturing inter-output correlations and heteroskedasticity.

## Practical Extensions and Results

The use of a Gaussian-based score enables extensions including construction of conformal sets with missing output values, refinement of conformal sets as partial information becomes available, and construction on transformations of the output space.

Empirical results indicate the approach produces conformal sets that more closely approximate conditional coverage in multivariate settings compared to alternative methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "cc64435d-4ad5-4a06-be2a-2f1b88bddad6"
}
```

</details>

---

### Tool result

_source line 225 · 2026-05-15T20:18:44.088Z_

<details><summary>↩ Tool result · `toolu_01MqPLLTnyP8rMKMAmDGxDrG`</summary>

```text
Web search results for query: "site:arxiv.org/html/2602.21633 SC-VLA "reinforcement learning" OR "RL" OR "residual" online action refinement"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"From Imitation to Refinement—Residual RL for Precise Assembly","url":"https://residual-assembly.github.io/"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"GitHub - PRIME-RL/SimpleVLA-RL: [ICLR 2026] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning · GitHub","url":"https://github.com/PRIME-RL/SimpleVLA-RL"},{"title":"SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning | OpenReview","url":"https://openreview.net/forum?id=TQhSodCM4r"},{"title":"[2509.09674] SimpleVLA-RL: Scaling VLA Training via Reinforcement Learning","url":"https://arxiv.org/abs/2509.09674"}]

Based on the search results from arxiv.org/html/2602.21633, here's what I found about SC-VLA and its approach to online action refinement:

## SC-VLA Overview

SC-VLA is a self-correcting framework that integrates offline action generation with online refinement. The paper addresses key limitations in standard VLA models by combining two key innovations:

## Core Technical Approach

The framework jointly generates actions while predicting sparse future states, enabling fine-grained trajectory refinement via residual reinforcement learning for complex manipulation tasks.

### Sparse World Imagination (SPI)

By introducing sparse world imagination to forecast sparse future states, it constrains the policy to encode physical evolution. The framework integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

### Online Action Refinement (OAR)

The framework develops online action refinement with residual reinforcement learning to adjust trajectory orientation, constructing progress-dependent dense rewards using predicted future states, explicitly guiding the policy to align with the imagined future behavioral trends.

## Performance Results

SC-VLA achieves the best performance in task throughput and success rate on complex manipulation tasks. More specifically, SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "898384bb-5649-49b4-8310-2cde12a13c74"
}
```

</details>

---

### Tool result

_source line 226 · 2026-05-15T20:18:44.269Z_

<details><summary>↩ Tool result · `toolu_01WUC7CjNbdpwootg2TTVo9E`</summary>

```text
Web search results for query: "ar5iv residual policy learning 1812.06298 "zero" initialization "bounded" clipping action space classical controller"

Links: [{"title":"[1812.06298] Residual Policy Learning - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.06298"},{"title":"[1812.06298] Residual Policy Learning","url":"https://arxiv.org/abs/1812.06298"},{"title":"Soft Actor-Critic Algorithms and Applications - ar5iv - arXiv","url":"https://ar5iv.labs.arxiv.org/html/1812.05905"},{"title":"[1805.09613] A0C: Alpha Zero in Continuous Action Space","url":"https://ar5iv.labs.arxiv.org/html/1805.09613"},{"title":"[2010.02798] Policy learning in 𝑆⁢𝐸⁢(3) action spaces","url":"https://ar5iv.labs.arxiv.org/html/2010.02798"},{"title":"[2002.03069] 1 INTRODUCTION","url":"https://ar5iv.labs.arxiv.org/html/2002.03069"},{"title":"Residual Reinforcement Learning for Robot Control","url":"https://arxiv.org/pdf/1812.03201"},{"title":"[1901.09321] Fixup Initialization: Residual Learning Without Normalization","url":"https://ar5iv.labs.arxiv.org/html/1901.09321"},{"title":"[1509.02971] Continuous control with deep reinforcement learning","url":"https://arxiv.org/abs/1509.02971"},{"title":"[2110.12661] ZerO Initialization: Initializing Neural Networks with only Zeros and Ones","url":"https://ar5iv.labs.arxiv.org/html/2110.12661"}]

I found the ar5iv page for paper 1812.06298, which is about Residual Policy Learning (RPL). Based on the search results:

Residual Policy Learning (RPL) is a simple method for improving nondifferentiable policies using model-free deep reinforcement learning. RPL thrives in complex robotic manipulation tasks where good but imperfect controllers are available.

For initial controllers, the approach considers both hand-designed policies and model-predictive controllers with known or learned transition models. By combining learning with control algorithms, RPL can perform long-horizon, sparse-reward tasks for which reinforcement learning alone fails.

The full ar5iv HTML version of the paper is available at: https://ar5iv.labs.arxiv.org/html/1812.06298

You can access the paper directly to find the specific details about zero initialization, bounded clipping, action space, and classical controller implementation that you're looking for.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d92edc3a-2ee3-4e26-9bb1-2eaf335618c0"
}
```

</details>

---

### Tool result

_source line 227 · 2026-05-15T20:18:47.353Z_

<details><summary>↩ Tool result · `toolu_01TRAWEyNguCsYPW1AwMHnfB`</summary>

```text
Web search results for query: "PLD "probe learn distill" VLA residual RL 2511.00091 "action bound" OR "clipping" OR "magnitude" OR "epsilon" OR "xi" correction range training curriculum"

Links: [{"title":"[2511.00091] Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/abs/2511.00091"},{"title":"PLD: Self-Improving Vision-Language-Action Models (ICLR 2026)","url":"https://wenlixiao.com/self-improve-VLA-PLD"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | OpenReview","url":"https://openreview.net/forum?id=eUGoqrZ6Ea"},{"title":"(PDF) Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://www.researchgate.net/publication/397231758_Self-Improving_Vision-Language-Action_Models_with_Data_Generation_via_Residual_RL"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2511.00091"},{"title":"SELF-IMPROVING VISION-LANGUAGE-ACTION","url":"https://arxiv.org/pdf/2511.00091"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"[PDF] Self-Improving Vision-Language-Action Models with Data Generation via Residual RL | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Improving-Vision-Language-Action-Models-with-Xiao-Lin/14c584af2fda0b9b5851b1e8573c4e2dd2c8fd0b"},{"title":"Interesting Directions in Vision-Language-Action Model Research","url":"https://itcanthink.substack.com/p/interesting-directions-in-vision"}]

Based on the search results, I found the paper you're looking for:

**PLD (Probe, Learn, Distill)** is a three-stage plug-and-play framework that improves VLAs through residual reinforcement learning (RL) and distribution-aware data collection.

The framework consists of three stages:

1. **Stage 1 (Specialist Acquisition)**: The VLA backbone is frozen and lightweight residual actors are trained via off-policy RL, which take over in states where the base policy fails, thereby probing failure regions of the VLA generalist.

2. **Stage 2 (Data Collection)**: A hybrid rollout scheme is employed that biases residual interventions toward states frequently visited by the base policy, aligning collected trajectories with the generalist's deployment distribution while capturing recovery behaviors.

3. **Stage 3 (Fine-tuning)**: The curated trajectories are distilled back into the generalist with standard SFT, applicable to both flow-matching and autoregressive heads.

**Results**: PLD achieves a near-saturated 99% task success rate on the LIBERO benchmark, delivers over 50% performance gains in SimplerEnv, and demonstrates a 100% success rate on real-world Franka arm and YAM arm dexterous manipulation tasks.

The paper (arXiv:2511.00091) was published in October 2025 and demonstrates that RL-generated, policy-aligned data can surpass teleoperation-only demonstrations, offering a scalable path toward self-improving VLA models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "fac44470-5f14-4380-ab24-91a3677748bc"
}
```

</details>

---

### System

_source line 228_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA 2604.16677 Chen Lyu Beksi \"action select…",
  "usage": {
    "total_tokens": 30667,
    "tool_uses": 17,
    "duration_ms": 85851
  },
  "last_tool_name": "WebSearch",
  "uuid": "7bd6ca84-a924-43ae-8793-937c7497505a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 229_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CXnxAnz1ZmEydkufEtKTh5`</summary>

```json
{
  "query": "ReconVLA 2604.16677 Chen Lyu Beksi \"action selection\" abstract methodology overview conformal prediction VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "28eade7d-64b2-42eb-bc46-34e6b9414f99",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PQ88z4nDo6EESMwczm3cYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 27541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3055,
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

### System

_source line 230_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for \"Leave No Observation Behind\" A2C2 2509.23224 \"tr…",
  "usage": {
    "total_tokens": 30670,
    "tool_uses": 18,
    "duration_ms": 87117
  },
  "last_tool_name": "WebSearch",
  "uuid": "98c6d7ef-17e4-49dc-a611-27f141c45a58",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 231_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BEyKdVxFLJgWh5qzGPB7X`</summary>

```json
{
  "query": "\"Leave No Observation Behind\" A2C2 2509.23224 \"trained\" OR \"training\" correction head \"base policy\" frozen jointly"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9a96ecc8-aa3f-4fa5-8cca-6864ae082800",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01PQ88z4nDo6EESMwczm3cYu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3055,
      "cache_read_input_tokens": 27541,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3055,
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

### System

_source line 232_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Verify residual policy + UQ citations",
  "usage": {
    "total_tokens": 25733,
    "tool_uses": 13,
    "duration_ms": 58178
  },
  "last_tool_name": "ToolSearch",
  "uuid": "066bfc9f-ceaf-4d91-9d9c-4021c0748c93",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 233_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DPKJU5SYHgR7WijHwRU92y`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "36fe1b38-a5b8-4668-b5b5-f667f5cb5e2a",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VLUvi74NvvBRLCTVf7bnwC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3913,
      "cache_read_input_tokens": 21757,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3913,
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

_source line 234 · 2026-05-15T20:18:50.919Z_

<details><summary>↩ Tool result · `toolu_01DPKJU5SYHgR7WijHwRU92y`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "101332cf-a87b-43e6-ac92-e7446df5ca82"
}
```

</details>

---

### System

_source line 235_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Fetching https://ar5iv.labs.arxiv.org/html/1812.06298",
  "usage": {
    "total_tokens": 26361,
    "tool_uses": 14,
    "duration_ms": 62869
  },
  "last_tool_name": "WebFetch",
  "uuid": "6c25949c-f558-4baf-b931-521f7c8a0e24",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 236_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EgoGcpz1VXeLqhH2B2LQU1`</summary>

```json
{
  "url": "https://ar5iv.labs.arxiv.org/html/1812.06298",
  "prompt": "Does the paper discuss zero-initialization of the residual policy network? Does it use bounded corrections or action clipping to limit the residual? Is it specifically framed for classical controllers? Extract the key technical design choices."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7fcc6df8-c2df-4c0a-a140-ad6f6a44b9e0",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Db9DxKW4jCUUcnARZNwQcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 237 · 2026-05-15T20:18:55.787Z_

<details><summary>↩ Tool result · `toolu_016BEyKdVxFLJgWh5qzGPB7X`</summary>

```text
Web search results for query: ""Leave No Observation Behind" A2C2 2509.23224 "trained" OR "training" correction head "base policy" frozen jointly"

Links: [{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224"}]

I found the research paper you're searching for. Here's what the search reveals:

"Leave No Observation Behind" introduces Asynchronous Action Chunk Correction (A2C2), which is a lightweight real-time chunk correction head that runs every control step and adds a time-aware correction to any off-the-shelf VLA's action chunk. 

The module combines the latest observation, the predicted action from VLA (base action), a positional feature that encodes the index of the base action within the chunk, and some features from the base policy, then outputs a per-step correction.

The approach requires no retraining of the base policy, and the correction head is trained on the same dataset as the base policy.

The paper (arXiv:2509.23224) demonstrates that A2C2 is an effective plug-in mechanism for deploying vision-language-action models in real-time robotic control scenarios.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d3850e22-a5fe-4981-b4cd-88f9a02d8f49"
}
```

</details>

---

### Tool result

_source line 238 · 2026-05-15T20:18:55.861Z_

<details><summary>↩ Tool result · `toolu_01CXnxAnz1ZmEydkufEtKTh5`</summary>

```text
Web search results for query: "ReconVLA 2604.16677 Chen Lyu Beksi "action selection" abstract methodology overview conformal prediction VLA"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/html/2602.01166v2"},{"title":"Conformal Predictions for Human Action Recognition with Vision-Language Models","url":"https://arxiv.org/html/2502.06631v2"},{"title":"[2602.01166] Latent Reasoning VLA: Latent Thinking and Prediction for Vision-Language-Action Models","url":"https://arxiv.org/abs/2602.01166"},{"title":"[2502.06631] Conformal Predictions for Human Action Recognition with Vision-Language Models","url":"https://arxiv.org/abs/2502.06631"},{"title":"[2503.16809] Online Selective Conformal Prediction: Errors and Solutions","url":"https://arxiv.org/abs/2503.16809"},{"title":"[2604.17984] Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization","url":"https://arxiv.org/abs/2604.17984"}]

Based on the search results, I found the paper you're looking for:

**ReconVLA (arXiv:2604.16677)** is a research paper authored by Lingling Chen, Zongyao Lyu, and William J. Beksi from the Department of Computer Science and Engineering at The University of Texas at Arlington.

**Abstract/Overview:**

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences. However, VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.

**Methodology:**

ReconVLA introduces a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates.

The paper addresses a key limitation in VLA systems by incorporating uncertainty quantification through conformal prediction, enabling more reliable action selection for robotic control tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "43d70876-87d4-49fc-90b9-dc26d4dff1f9"
}
```

</details>

---

### System

_source line 239_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Fetching https://arxiv.org/html/2511.00091",
  "usage": {
    "total_tokens": 26362,
    "tool_uses": 15,
    "duration_ms": 64966
  },
  "last_tool_name": "WebFetch",
  "uuid": "20ecc7b6-027e-47dc-a644-52e796990e59",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 240_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013RLagYkAKrpjAc6X3x8Tvj`</summary>

```json
{
  "url": "https://arxiv.org/html/2511.00091",
  "prompt": "Does the paper introduce a scheduled magnitude bound (xi or epsilon) for residual RL corrections on VLAs? Does the allowed correction range progressively increase during training? What are the specific technical design choices around action bounds or clipping for the residual actor?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4f40de7c-066a-46cf-b441-ad3afc840f78",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Db9DxKW4jCUUcnARZNwQcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 241_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Fetching https://arxiv.org/html/2503.15368",
  "usage": {
    "total_tokens": 26363,
    "tool_uses": 16,
    "duration_ms": 67797
  },
  "last_tool_name": "WebFetch",
  "uuid": "5b52f10a-11b0-417b-8133-39726eedf306",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 242_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01JhLXmsHd7Fy7fs84MYLgLY`</summary>

```json
{
  "url": "https://arxiv.org/html/2503.15368",
  "prompt": "How exactly does the \"decaying\" in Decaying Relative Correction work? Is the decay about temporal position within an episode (early vs late corrections), or is it about spatial correction vectors that temporarily persist and fade? What is the paper's rationale for temporal decay?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "bbd6b1c1-dbf9-49e8-8838-6485440dc4d1",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Db9DxKW4jCUUcnARZNwQcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 243_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA 2604.16677 \"N\" OR \"multiple\" action samp…",
  "usage": {
    "total_tokens": 32099,
    "tool_uses": 19,
    "duration_ms": 97415
  },
  "last_tool_name": "WebSearch",
  "uuid": "009c06b9-b1db-468f-8a13-a8f079fd4360",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 244_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxHWQZrLuddP1tPt22Fi83`</summary>

```json
{
  "query": "ReconVLA 2604.16677 \"N\" OR \"multiple\" action samples generated ranked selected conformal uncertainty score"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "b0d303e5-a2bc-4068-9d66-a8a9547fa245",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VyjqyCyMqv547hh7iwKn2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 30596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1045,
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

_source line 245_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "ac29a39f9d517f690",
  "tool_use_id": "toolu_017WkxnZx3dim1JbwEHs2DP8",
  "status": "completed",
  "output_file": "",
  "summary": "Verify foundational/base citations",
  "usage": {
    "total_tokens": 24358,
    "tool_uses": 9,
    "duration_ms": 59708
  },
  "uuid": "6491c8da-413f-4da3-b032-9603f94170ed",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 246 · 2026-05-15T20:19:02.055Z_

<details><summary>↩ Tool result · `toolu_017WkxnZx3dim1JbwEHs2DP8`</summary>

```text
All 7 citations verified. Here are the results:

---

**1. black2024pi0** — arXiv 2410.24164
- Paper claims: VLA that "generates actions via flow matching"
- Actual: π₀ is explicitly a "Vision-Language-Action **Flow** Model" that uses a flow-matching action expert built on top of a pre-trained VLM.
- **CORRECT**

---

**2. shukor2025smolvla** — arXiv 2506.01844
- Paper claims: "a 450M-parameter flow-matching VLA"
- Actual: SmolVLA is confirmed at 450M total parameters; its action expert uses a flow matching transformer (~100M trainable params). The "450M flow-matching VLA" description is accurate.
- **CORRECT**

---

**3. liu2023libero** — NeurIPS 2023
- Paper claims: cited as a "standard manipulation benchmark"
- Actual: LIBERO is a benchmark for lifelong robot learning with 130 manipulation tasks across four task suites, published in NeurIPS 2023 Datasets & Benchmarks track. It is widely used as a manipulation evaluation benchmark (SmolVLA itself evaluates on LIBERO).
- **CORRECT**

---

**4. lipman2023flow** — ICLR 2023
- Paper claims: foundational flow matching method; VLA "generates actions via learned flow matching"
- Actual: Lipman et al. introduced Flow Matching for training Continuous Normalizing Flows via simulation-free regression on vector fields, published at ICLR 2023. This is the canonical foundational FM paper.
- **CORRECT**

---

**5. ledoit2004well** — Journal of Multivariate Analysis, 2004
- Paper claims: Ledoit-Wolf shrinkage covariance estimation with "analytically optimal shrinkage intensity"
- Actual: The paper introduces shrinkage estimation of covariance matrices as a weighted average of the sample covariance and a structured target; the asymptotically optimal shrinkage intensity is estimated consistently. The 2004 paper derives a linear shrinkage formula — the "analytically optimal" characterization is broadly accurate for this version. (Note: the fully analytical closed-form nonlinear shrinkage came in later Ledoit-Wolf work from 2020, but the 2004 paper does derive an analytically consistent estimator for the optimal shrinkage coefficient.)
- **CORRECT** (with minor nuance: if the paper specifically invokes "analytically optimal" to mean closed-form nonlinear shrinkage, the correct cite would be Ledoit & Wolf 2020; but for linear shrinkage with consistent optimal intensity, 2004 is the right reference)

---

**6. ross2011dagger** — AISTATS 2011
- Paper claims: cited for "compounding distribution shift" / "compounding error problem in imitation learning"
- Actual: This is the DAgger paper, whose central contribution is precisely diagnosing and solving the compounding error / covariate shift problem in imitation learning. This attribution is the standard use of this citation.
- **CORRECT**

---

**7. angelopoulos2023gentle** — arXiv 2107.07511
- Paper claims: "Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability"
- Actual: The paper explicitly provides distribution-free, non-asymptotic coverage guarantees for conformal prediction under the exchangeability assumption. This is the central theorem of the work.
- **CORRECT**

---

**Summary:** All 7 citations are **CORRECT**. No attribution errors detected. The one item worth a secondary glance is #5 (ledoit2004well) — if the surrounding text specifically claims *nonlinear* analytical shrinkage, that would belong to the 2020 Annals of Statistics paper by the same authors, but for the standard linear Ledoit-Wolf shrinkage the 2004 citation is appropriate.

Sources:
- [π₀: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)
- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)
- [SmolVLA HuggingFace Blog](https://huggingface.co/blog/smolvla)
- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html)
- [Flow Matching for Generative Modeling (ICLR 2023)](https://arxiv.org/abs/2210.02747)
- [A well-conditioned estimator for large-dimensional covariance matrices](https://www.sciencedirect.com/science/article/pii/S0047259X03000964)
- [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (AISTATS 2011)](https://proceedings.mlr.press/v15/ross11a.html)
- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511)

agentId: ac29a39f9d517f690 (use SendMessage with to: 'ac29a39f9d517f690' to continue this agent)
&lt;usage>total_tokens: 25601
tool_uses: 9
duration_ms: 59710&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "9f2367bf-5bcb-422d-bdd0-e8cb59d87514",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to verify method attribution accuracy for 7 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. black2024pi0** (arXiv: 2410.24164)\nTitle: \"π₀: A Vision-Language-Action Flow Model for General Robot Control\"\nPaper claims: VLAs that \"generate actions via flow matching\"\n\n**2. shukor2025smolvla** (arXiv: 2506.01844)\nTitle: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\nPaper claims: \"a 450M-parameter flow-matching VLA\"\n\n**3. liu2023libero** (NeurIPS 2023)\nTitle: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\nPaper claims: \"standard manipulation benchmarks such as LIBERO\" - used as a benchmark for evaluation\n\n**4. lipman2023flow** (ICLR 2023)\nTitle: \"Flow Matching for Generative Modeling\"\nAuthors: Yaron Lipman et al.\nPaper claims: foundational flow matching method; VLA \"generates actions via learned flow matching\"\n\n**5. ledoit2004well** (Journal of Multivariate Analysis, 2004)\nTitle: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\nAuthors: Olivier Ledoit, Michael Wolf\nPaper claims: Ledoit-Wolf shrinkage covariance estimation; \"analytically optimal shrinkage intensity\"\n\n**6. ross2011dagger** (AISTATS 2011)\nTitle: \"A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning\"\nAuthors: Stéphane Ross, Geoffrey J. Gordon, J. Andrew Bagnell\nPaper claims: cited for \"compounding distribution shift\" / \"compounding error problem in imitation learning\"\n\n**7. angelopoulos2023gentle** (arXiv: 2107.07511)\nTitle: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\nAuthors: Anastasios N. Angelopoulos, Stephen Bates\nPaper claims: \"Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability\"\n\nSearch for each paper and verify the method descriptions. These are mostly foundational/well-known papers so quick verification should suffice.",
    "agentId": "ac29a39f9d517f690",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "All 7 citations verified. Here are the results:\n\n---\n\n**1. black2024pi0** — arXiv 2410.24164\n- Paper claims: VLA that \"generates actions via flow matching\"\n- Actual: π₀ is explicitly a \"Vision-Language-Action **Flow** Model\" that uses a flow-matching action expert built on top of a pre-trained VLM.\n- **CORRECT**\n\n---\n\n**2. shukor2025smolvla** — arXiv 2506.01844\n- Paper claims: \"a 450M-parameter flow-matching VLA\"\n- Actual: SmolVLA is confirmed at 450M total parameters; its action expert uses a flow matching transformer (~100M trainable params). The \"450M flow-matching VLA\" description is accurate.\n- **CORRECT**\n\n---\n\n**3. liu2023libero** — NeurIPS 2023\n- Paper claims: cited as a \"standard manipulation benchmark\"\n- Actual: LIBERO is a benchmark for lifelong robot learning with 130 manipulation tasks across four task suites, published in NeurIPS 2023 Datasets & Benchmarks track. It is widely used as a manipulation evaluation benchmark (SmolVLA itself evaluates on LIBERO).\n- **CORRECT**\n\n---\n\n**4. lipman2023flow** — ICLR 2023\n- Paper claims: foundational flow matching method; VLA \"generates actions via learned flow matching\"\n- Actual: Lipman et al. introduced Flow Matching for training Continuous Normalizing Flows via simulation-free regression on vector fields, published at ICLR 2023. This is the canonical foundational FM paper.\n- **CORRECT**\n\n---\n\n**5. ledoit2004well** — Journal of Multivariate Analysis, 2004\n- Paper claims: Ledoit-Wolf shrinkage covariance estimation with \"analytically optimal shrinkage intensity\"\n- Actual: The paper introduces shrinkage estimation of covariance matrices as a weighted average of the sample covariance and a structured target; the asymptotically optimal shrinkage intensity is estimated consistently. The 2004 paper derives a linear shrinkage formula — the \"analytically optimal\" characterization is broadly accurate for this version. (Note: the fully analytical closed-form nonlinear shrinkage came in later Ledoit-Wolf work from 2020, but the 2004 paper does derive an analytically consistent estimator for the optimal shrinkage coefficient.)\n- **CORRECT** (with minor nuance: if the paper specifically invokes \"analytically optimal\" to mean closed-form nonlinear shrinkage, the correct cite would be Ledoit & Wolf 2020; but for linear shrinkage with consistent optimal intensity, 2004 is the right reference)\n\n---\n\n**6. ross2011dagger** — AISTATS 2011\n- Paper claims: cited for \"compounding distribution shift\" / \"compounding error problem in imitation learning\"\n- Actual: This is the DAgger paper, whose central contribution is precisely diagnosing and solving the compounding error / covariate shift problem in imitation learning. This attribution is the standard use of this citation.\n- **CORRECT**\n\n---\n\n**7. angelopoulos2023gentle** — arXiv 2107.07511\n- Paper claims: \"Conformal prediction (CP) provides distribution-free coverage guarantees under exchangeability\"\n- Actual: The paper explicitly provides distribution-free, non-asymptotic coverage guarantees for conformal prediction under the exchangeability assumption. This is the central theorem of the work.\n- **CORRECT**\n\n---\n\n**Summary:** All 7 citations are **CORRECT**. No attribution errors detected. The one item worth a secondary glance is #5 (ledoit2004well) — if the surrounding text specifically claims *nonlinear* analytical shrinkage, that would belong to the 2020 Annals of Statistics paper by the same authors, but for the standard linear Ledoit-Wolf shrinkage the 2004 citation is appropriate.\n\nSources:\n- [π₀: A Vision-Language-Action Flow Model for General Robot Control](https://arxiv.org/abs/2410.24164)\n- [SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics](https://arxiv.org/abs/2506.01844)\n- [SmolVLA HuggingFace Blog](https://huggingface.co/blog/smolvla)\n- [LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning (NeurIPS 2023)](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8c3c666820ea055a77726d66fc7d447f-Abstract-Datasets_and_Benchmarks.html)\n- [Flow Matching for Generative Modeling (ICLR 2023)](https://arxiv.org/abs/2210.02747)\n- [A well-conditioned estimator for large-dimensional covariance matrices](https://www.sciencedirect.com/science/article/pii/S0047259X03000964)\n- [A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning (AISTATS 2011)](https://proceedings.mlr.press/v15/ross11a.html)\n- [A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification](https://arxiv.org/abs/2107.07511)"
      }
    ],
    "totalDurationMs": 59710,
    "totalTokens": 25601,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1892,
      "cache_read_input_tokens": 22405,
      "output_tokens": 1303,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1892
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1303,
          "cache_read_input_tokens": 22405,
          "cache_creation_input_tokens": 1892,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1892,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 9
    }
  }
}
```

</details>

---

### System

_source line 247_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for \"arxiv.org\" \"2509.23224\" A2C2 correction head \"jo…",
  "usage": {
    "total_tokens": 32100,
    "tool_uses": 20,
    "duration_ms": 98331
  },
  "last_tool_name": "WebSearch",
  "uuid": "a9a9ccb6-e4b3-4ac2-a997-798d31563c8b",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 248_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Wguq3RTcgfX7rVt44g6HhM`</summary>

```json
{
  "query": "\"arxiv.org\" \"2509.23224\" A2C2 correction head \"jointly trained\" OR \"trained jointly\" OR \"separately\" OR \"post-hoc\" frozen base"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "20627a0e-c58d-4b6a-8122-2c6625931c83",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01VyjqyCyMqv547hh7iwKn2q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 383,
      "cache_creation_input_tokens": 1045,
      "cache_read_input_tokens": 30596,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1045,
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

_source line 249 · 2026-05-15T20:19:01.961Z_

<details><summary>↩ Tool result · `toolu_01EgoGcpz1VXeLqhH2B2LQU1`</summary>

```text
# Key Technical Design Choices in Residual Policy Learning

## Zero-Initialization

Yes, the paper explicitly discusses zero-initialization. Section IV-A states: "We therefore endeavor to initialize the residual function so that fθ(s)=0 for all s∈𝒮. We do this by initializing the last layer of the network to be zero."

This ensures the method preserves good initial policies rather than degrading them.

## Action Clipping and Bounded Corrections

The paper does **not** use explicit bounded corrections or clipping of the residual term. The residual is learned without constraints within the standard action space 𝒜=[-1,1]^D. The composite policy πθ(s)=π(s)+fθ(s) can theoretically exceed action bounds, though practical experiments show the learned residuals remain reasonable.

## Classical Controller Focus

The approach is **broadly applicable** rather than specifically framed for classical controllers. The paper emphasizes generality: "RPL is indifferent to the deep RL method applied or architecture used." It works with:

- Hand-designed reactive policies
- Model-predictive controllers (MPC)
- Learned transition models (PETS)

The versatility is a key strength—the method combines complementary strengths of "deep reinforcement learning and robotic control" without requiring controller-specific assumptions.

## Summary of Design Choices

1. **Initialization**: Last layer zeroed to preserve initial policy performance
2. **No explicit constraints**: Residuals learned within standard bounded action space
3. **Universal applicability**: Works with diverse controller types without modification
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "c4e4f6b7-b25c-444f-ba89-e126fa184f1d"
}
```

</details>

---

### System

_source line 250_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "description": "Fetching https://arxiv.org/html/2405.10315",
  "usage": {
    "total_tokens": 26364,
    "tool_uses": 17,
    "duration_ms": 69726
  },
  "last_tool_name": "WebFetch",
  "uuid": "5e61684c-a1f1-4704-8445-7c68cb13246a",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 251_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01WzU2jPMqyS5ZtyTp7SAoaG`</summary>

```json
{
  "url": "https://arxiv.org/html/2405.10315",
  "prompt": "Does TRANSIC use a learned binary gate to selectively apply residual actions across different task phases? What is the exact mechanism — is it binary (0/1 gate), and does it select based on task phases? Does the paper claim ungated correction causes model collapse?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "aa4ed74d-a1a7-454e-8daf-1639b2958115",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Db9DxKW4jCUUcnARZNwQcJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 25670,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 624,
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

_source line 252 · 2026-05-15T20:19:04.017Z_

<details><summary>↩ Tool result · `toolu_013RLagYkAKrpjAc6X3x8Tvj`</summary>

```text
# Residual Action Magnitude Bounds in PLD

Yes, the paper introduces a scheduled magnitude bound for residual RL corrections. The approach uses a scaling parameter ξ (xi) to constrain delta actions within [-ξ, ξ].

## Key Design Choices

**Initial Constraint Strategy:**
The paper states that delta actions are "scaled down to [-ξ,ξ], where ξ∈[0,1] is tuned by a scheduler" to modulate exploration and prevent drastic deviation from the base policy during early training phases.

**Progressive Scheduling:**
While the paper mentions a scheduler controls ξ, it doesn't specify the exact scheduling function. However, the ablation study in Section B.2 (Action Scale) reveals important findings:

- Setting ξ too large initially degrades early performance
- Small ξ values lead to insufficient exploration and lower asymptotic performance
- Careful tuning is necessary to enable exploration while minimizing performance drops

**Recommended Values:**
The authors suggest practical settings: ξ=0.5 for LIBERO tasks and ξ=0.1 for SimplerEnv based on their ablations.

**Motivation:**
This bounded residual design serves a dual purpose: it leverages the base policy's prior knowledge as a useful initialization while preventing the lightweight residual actor from diverging excessively during training.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "4f0daf3d-fc54-4728-b00a-6f287e853c1e"
}
```

</details>

---

### Tool result

_source line 253 · 2026-05-15T20:19:06.037Z_

<details><summary>↩ Tool result · `toolu_01JhLXmsHd7Fy7fs84MYLgLY`</summary>

````text
# Decaying Relative Correction: How the Decay Works

The decay in DRC is **temporal persistence of spatial correction vectors**, not about timing within episodes.

## Mechanism

When an expert provides a correction vector, it creates a temporary spatial offset that persists beyond the immediate correction. The paper states: "The relative correction motion provided by the experts teleoperation provides the vector of correction which is only temporary, and stays valid for only a period of time, disappearing with a given decay rate."

The mathematical formulation shows the correction decays exponentially over subsequent timesteps:

```
a't = at + v^DRC(1 - r^decay)^(t - t^DRC)
```

After an expert inputs a correction vector, it gradually diminishes according to this decay function rather than stopping immediately.

## Rationale

The paper's core reasoning is that **corrective trends remain valid across multiple timesteps**. By allowing a single correction to persist and gradually fade, the system reduces how many intervention steps experts must make. The paper explains: "since trends in relative corrections (e.g., continuous adjustments over time) could remain valid for subsequent states or actions, leveraging this temporal consistency is crucial for improving the efficiency."

This contrasts with absolute correction, which requires continuous expert input at every timestep the robot deviates from desired behavior.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "6c2110f7-461e-49f6-a514-831606767118"
}
```

</details>

---

### Tool result

_source line 254 · 2026-05-15T20:19:06.645Z_

<details><summary>↩ Tool result · `toolu_01Wguq3RTcgfX7rVt44g6HhM`</summary>

```text
Web search results for query: ""arxiv.org" "2509.23224" A2C2 correction head "jointly trained" OR "trained jointly" OR "separately" OR "post-hoc" frozen base"

Links: [{"title":"Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/html/2509.23224"},{"title":"[2509.23224] Leave No Observation Behind: Real-time Correction for VLA Action Chunks","url":"https://arxiv.org/abs/2509.23224"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2505.23224"},{"title":"When a language model solves a math problem in its head ...","url":"https://www.facebook.com/0xSojalSec/posts/when-a-language-model-solves-a-math-problem-in-its-head-where-in-the-network-is-/1319304646390602/"},{"title":"Md - When a language model solves a math problem ...","url":"https://www.facebook.com/0xSojalSec/photos/when-a-language-model-solves-a-math-problem-in-its-head-where-in-the-network-is-/1319304473057286/"},{"title":"Physics-Informed GNN for Medium-High Voltage AC Power Flow with Edge-Aware Attention and Line Search Correction Operator","url":"https://arxiv.org/html/2509.22458"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=25&show=2000"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=50&show=2000"},{"title":"A correspondence between quantum error correcting ...","url":"https://arxiv.org/pdf/2412.15317"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=585&show=1000"}]

Based on the search results, I found information about the A2C2 correction head from arxiv paper 2509.23224. Regarding how the correction head is trained in relation to the base policy:

The correction head is trained on the same dataset as the base policy and, in principle, can be added to any off-the-shelf VLAs. Additionally, the approach requires no retraining of the base policy and is orthogonal to asynchronous execution schemes such as Real Time Chunking (RTC).

This indicates that the A2C2 correction head is trained separately from the base policy with a frozen base, rather than being jointly trained or trained post-hoc on top of a frozen base that was already trained together.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "ad760553-7202-4a84-bc7a-f7f69ae74db9"
}
```

</details>

---

### Tool result

_source line 255 · 2026-05-15T20:19:08.350Z_

<details><summary>↩ Tool result · `toolu_01WzU2jPMqyS5ZtyTp7SAoaG`</summary>

```text
# TRANSIC's Gating Mechanism

**Binary Gate Structure:**
Yes, TRANSIC uses a learned binary gate. The paper states: "At the inference time, we effectively use gψ as an indicator function 𝟙g to determine whether to apply the predicted residual actions."

The deployed policy formula is: πdeployed = πB ⊕ 𝟙g πR, where the gating function gψ acts as a binary selector.

**Mechanism Details:**
The gating function "shares the same feature encoder with the residual policy πR and is jointly learned through classification on the same correction dataset 𝒟H." It operates as a learned classifier rather than being explicitly tied to task phases—it learns to activate residual corrections based on observed state features.

**Model Collapse Claim:**
The paper does claim that ungated approaches cause failure. It states: "directly fine-tuning the base policy πB on human correction dataset 𝒟H leads to large motions and even model collapse." This motivated their adoption of the gated residual policy design, which prevents catastrophic forgetting by keeping the base policy intact and selectively applying corrections.

The gating mechanism thus serves as the key architectural innovation preventing the base policy from being overwritten by limited human correction data.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "2d15cd4f-92c7-41b5-9614-259ab7a05b66"
}
```

</details>

---

### Tool result

_source line 256 · 2026-05-15T20:19:08.458Z_

<details><summary>↩ Tool result · `toolu_01PxHWQZrLuddP1tPt22Fi83`</summary>

```text
Web search results for query: "ReconVLA 2604.16677 "N" OR "multiple" action samples generated ranked selected conformal uncertainty score"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"[2410.13735] Generative Conformal Prediction with Vectorized Non-Conformity Scores","url":"https://arxiv.org/abs/2410.13735"},{"title":"1 Introduction","url":"https://arxiv.org/html/2410.13735v1/"},{"title":"Reliable classification through rank-based conformal prediction sets - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0031320325009914"},{"title":"ICML Poster A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression","url":"https://icml.cc/virtual/2025/poster/45852"},{"title":"A Unified Comparative Study with Generalized Conformity Scores for Multi-Output Conformal Regression","url":"https://arxiv.org/html/2501.10533v2"},{"title":"(PDF) Multi-Output Conformal Regression: A Unified Comparative Study with New Conformity Scores","url":"https://www.researchgate.net/publication/388232003_Multi-Output_Conformal_Regression_A_Unified_Comparative_Study_with_New_Conformity_Scores"},{"title":"Conformity Score: Definition & Applications","url":"https://www.emergentmind.com/topics/conformity-score"},{"title":"[2604.25235] VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation","url":"https://arxiv.org/abs/2604.25235"},{"title":"VLM Judges Can Rank but Cannot Score: Task-Dependent Uncertainty in Multimodal Evaluation","url":"https://arxiv.org/html/2604.25235v1"}]

Based on the search results, I found relevant information about ReconVLA (arxiv 2604.16677). Here's what the paper covers:

## ReconVLA Overview

ReconVLA (reliable conformal VLA) is an uncertainty-guided control framework that endows VLAs with calibrated uncertainty estimation and proactive failure detection.

## Core Technical Approach

The approach leverages recent advances in conformal prediction (CP) to compute statistically rigorous and actionable confidence bounds on the model's action outputs, incorporating conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring.

## Key Features

The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. Additionally, conformal prediction is extended to the robot state space to detect outliers or unsafe states before failures occur, providing a failure detection mechanism that complements the action-level uncertainty.

## Uncertainty Sources

The framework focuses on two major sources of uncertainty: the robot's perceptual/state uncertainty (caused by ambiguous or novel inputs, e.g., blurred images, occluded scenes, semantically ambiguous instructions, or unseen environments) and action outcome uncertainty (stemming from stochastic policy behavior or environmental noise).

The paper represents a significant contribution to making Vision-Language-Action models more reliable and trustworthy for robotic control applications through uncertainty quantification.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "11fb12ad-978b-4699-8b4f-4333a36809df"
}
```

</details>

---

### System

_source line 257_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "description": "Searching for ReconVLA 2604.16677 abstract \"action\" \"uncertaint…",
  "usage": {
    "total_tokens": 33968,
    "tool_uses": 21,
    "duration_ms": 109557
  },
  "last_tool_name": "WebSearch",
  "uuid": "346fb333-37dd-489e-a906-5be2506e0fe9",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool call

_source line 258_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YKk719A1AVTZCU14efaXwt`</summary>

```json
{
  "query": "ReconVLA 2604.16677 abstract \"action\" \"uncertainty\" \"conformal\" \"selection\" full text arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3cb10b19-b763-415b-bc6f-e0caa7a8941e",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SWFZDHpjyweTCUYpMkn4RH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 722,
      "cache_creation_input_tokens": 1527,
      "cache_read_input_tokens": 31641,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1527,
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

_source line 259_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a44f8c614b291b8ff",
  "tool_use_id": "toolu_01L86JccRo9WBFQiZfrovSAF",
  "status": "completed",
  "output_file": "",
  "summary": "Verify conformal prediction citations",
  "usage": {
    "total_tokens": 27683,
    "tool_uses": 13,
    "duration_ms": 96926
  },
  "uuid": "0920eb40-d386-4792-b409-a6b2507b0e36",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 260 · 2026-05-15T20:19:18.717Z_

<details><summary>↩ Tool result · `toolu_01L86JccRo9WBFQiZfrovSAF`</summary>

```text
I now have enough information to report on all 6 citations. Here are the findings:

---

**1. braun2025cgs** — arXiv 2507.20941

- **Paper claims:** CGS uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance.
- **Actual method:** The paper (also known as "Multivariate Conformal Prediction via Conformalized Gaussian Scoring") does exactly this — it uses the Mahalanobis distance induced by a learned local covariance as the nonconformity score, whitening residuals to decouple output correlations and standardize local variance. The CDF-based score reduces to a Mahalanobis distance in the Gaussian case.
- **Verdict: CORRECT.** The attribution accurately describes both the acronym CGS and the Mahalanobis-based mechanism.

---

**2. zhao2024conformalized** — RSS 2024 (arXiv 2406.07767)

- **Paper claims:** Uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.
- **Actual method:** Uses adaptive conformal prediction (adjusting intervals over time) on the mapping from low-dimensional joystick inputs to high-dimensional robot actions. It detects high-uncertainty states via an uncertainty-interval mechanism and proactively seeks intervention — which is effectively "flagging for human review." The setting is assistive/shared autonomy teleoperation.
- **Verdict: CORRECT**, though slightly imprecise. The paper uses adaptive CP (intervals tighten/relax over time), not static CP. The core claim about flagging unreliable predictions for human intervention is accurate.

---

**3. wang2025cploop** — arXiv 2510.16376

- **Paper claims:** Integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.
- **Actual method:** The paper proposes a "Feedback-Based CP" (Fb-CP) framework where CP regions are integrated into shrinking-horizon trajectory optimization as a joint risk constraint. Crucially, the feedback loop goes both directions — decisions feed back to inform CP, not just unidirectional CP → decision. It was accepted at NeurIPS 2025.
- **Verdict: CORRECT.** The core description of integrating CP as feedback constraints with tightening/relaxing behavior is accurate.

---

**4. zhou2025acp_cbf** — ICRA 2025, arXiv 2503.17678

- **Paper claims:** Combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies. Authors listed as Zetian Zhou, Shuo Yang, Wenhao Luo.
- **Actual method:** arXiv 2503.17678 is titled "Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction," and its actual authors are **Hao Zhou, Yanze Zhang, and Wenhao Luo** (not Zetian Zhou and Shuo Yang). It does combine ACP with CBFs for safe RL, and was accepted to ICRA 2025. The technical description matches, but the author attribution is wrong.
- **Verdict: INCORRECT** on author attribution. The first two authors named (Zetian Zhou, Shuo Yang) do not appear in the actual paper; the real authors are Hao Zhou and Yanze Zhang. The method description itself is accurate.

---

**5. gu2025safe** — NeurIPS 2025 (arXiv 2506.09937)

- **Paper claims:** Trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.
- **Actual method:** SAFE extracts features from the last layer of a VLA, trains an MLP/LSTM failure detector, then uses **functional conformal prediction** on a hold-out calibration set to set a time-varying threshold for failure detection. Detection time/accuracy tradeoff is controlled via the CP significance level α. The paper does not explicitly emphasize "safe fallback behaviors" as a system component — it focuses on failure detection and timing; fallback action upon detection is implied but not the paper's contribution.
- **Verdict: CORRECT** in substance. "VLA internal features," CP-calibrated detection timing, and anomaly-triggered response are all accurate. The "safe fallback behaviors" framing is a mild overstatement of what the paper claims as its contribution (it focuses on detection, not the fallback policy), but it is not wrong.

---

**6. zollo2025vla_calibration** — arXiv 2507.17383

- **Paper claims:** First systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks. Author listed as Matteo Zollo.
- **Actual method:** The paper is indeed the first systematic study of VLA calibration, introducing prompt ensembles and action-wise Platt scaling as remedies. However, the first author's name is **Thomas Zollo**, not Matteo Zollo.
- **Verdict: INCORRECT** on author name. "Matteo Zollo" does not exist in this paper; the author is Thomas Zollo. The method description is otherwise accurate.

---

**Summary table:**

| Citation | Author/Venue | Method Description | Verdict |
|---|---|---|---|
| braun2025cgs | Correct | Correct | **CORRECT** |
| zhao2024conformalized | Correct | Correct (adaptive CP detail omitted) | **CORRECT** |
| wang2025cploop | Correct | Correct | **CORRECT** |
| zhou2025acp_cbf | Wrong authors (Zetian Zhou → Hao Zhou; Shuo Yang → Yanze Zhang) | Correct | **INCORRECT** |
| gu2025safe | Correct | Mostly correct; "fallback behaviors" overstated | **NEEDS_REVIEW** |
| zollo2025vla_calibration | Wrong first name (Matteo → Thomas) | Correct | **INCORRECT** |

Sources:
- [arXiv 2507.20941 – Multivariate Standardized Residuals for Conformal Prediction](https://arxiv.org/abs/2507.20941)
- [arXiv 2406.07767 – Conformalized Teleoperation](https://arxiv.org/abs/2406.07767)
- [arXiv 2510.16376 – Conformal Prediction in The Loop](https://arxiv.org/abs/2510.16376)
- [arXiv 2503.17678 – Computationally and Sample Efficient Safe RL Using ACP](https://arxiv.org/abs/2503.17678)
- [arXiv 2506.09937 – SAFE: Multitask Failure Detection for VLAs](https://arxiv.org/abs/2506.09937)
- [arXiv 2507.17383 – Confidence Calibration in VLAs](https://arxiv.org/abs/2507.17383)

agentId: a44f8c614b291b8ff (use SendMessage with to: 'a44f8c614b291b8ff' to continue this agent)
&lt;usage>total_tokens: 29077
tool_uses: 13
duration_ms: 96927&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3b78ae4c-2dbe-481f-a2aa-9634b578aa82",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to verify method attribution accuracy for 6 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. braun2025cgs** (arXiv: 2507.20941)\nTitle: \"Multivariate Standardized Residuals for Conformal Prediction\"\nAuthors: Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach\nPaper claims: \"Conformalized Gaussian Scoring (CGS), which uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance\"\n\n**2. zhao2024conformalized** (RSS 2024)\nTitle: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\nAuthors: Michelle Zhao, Reid Simmons, Henny Admoni, Andrea Bajcsy\nPaper claims: \"uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review\"\n\n**3. wang2025cploop** (arXiv: 2510.16376)\nTitle: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\nAuthors: Han Wang, Chao Ning\nPaper claims: \"integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty\"\n\n**4. zhou2025acp_cbf** (ICRA 2025, arXiv: 2503.17678)\nTitle: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\nAuthors: Zetian Zhou, Shuo Yang, Wenhao Luo\nPaper claims: \"combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies\"\n\n**5. gu2025safe** (NeurIPS 2025)\nTitle: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\nAuthors: Qiao Gu et al.\nPaper claims: \"trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected\"\n\n**6. zollo2025vla_calibration** (arXiv: 2507.17383)\nTitle: \"Confidence Calibration in Vision-Language-Action Models\"\nAuthors: Matteo Zollo, Richard Zemel\nPaper claims: \"first systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks\"\n\nSearch for each paper and verify the method descriptions.",
    "agentId": "a44f8c614b291b8ff",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough information to report on all 6 citations. Here are the findings:\n\n---\n\n**1. braun2025cgs** — arXiv 2507.20941\n\n- **Paper claims:** CGS uses Mahalanobis-based nonconformity scores to construct prediction regions that respect cross-dimensional covariance.\n- **Actual method:** The paper (also known as \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\") does exactly this — it uses the Mahalanobis distance induced by a learned local covariance as the nonconformity score, whitening residuals to decouple output correlations and standardize local variance. The CDF-based score reduces to a Mahalanobis distance in the Gaussian case.\n- **Verdict: CORRECT.** The attribution accurately describes both the acronym CGS and the Mahalanobis-based mechanism.\n\n---\n\n**2. zhao2024conformalized** — RSS 2024 (arXiv 2406.07767)\n\n- **Paper claims:** Uses CP to quantify uncertainty in high-DOF action mappings during shared autonomy, flagging unreliable predictions for human review.\n- **Actual method:** Uses adaptive conformal prediction (adjusting intervals over time) on the mapping from low-dimensional joystick inputs to high-dimensional robot actions. It detects high-uncertainty states via an uncertainty-interval mechanism and proactively seeks intervention — which is effectively \"flagging for human review.\" The setting is assistive/shared autonomy teleoperation.\n- **Verdict: CORRECT**, though slightly imprecise. The paper uses adaptive CP (intervals tighten/relax over time), not static CP. The core claim about flagging unreliable predictions for human intervention is accurate.\n\n---\n\n**3. wang2025cploop** — arXiv 2510.16376\n\n- **Paper claims:** Integrates conformal prediction regions as feedback constraints in trajectory optimization, tightening or relaxing plans based on calibrated uncertainty.\n- **Actual method:** The paper proposes a \"Feedback-Based CP\" (Fb-CP) framework where CP regions are integrated into shrinking-horizon trajectory optimization as a joint risk constraint. Crucially, the feedback loop goes both directions — decisions feed back to inform CP, not just unidirectional CP → decision. It was accepted at NeurIPS 2025.\n- **Verdict: CORRECT.** The core description of integrating CP as feedback constraints with tightening/relaxing behavior is accurate.\n\n---\n\n**4. zhou2025acp_cbf** — ICRA 2025, arXiv 2503.17678\n\n- **Paper claims:** Combines adaptive conformal prediction with control barrier functions to maintain safety constraints under distribution shift in RL policies. Authors listed as Zetian Zhou, Shuo Yang, Wenhao Luo.\n- **Actual method:** arXiv 2503.17678 is titled \"Computationally and Sample Efficient Safe Reinforcement Learning Using Adaptive Conformal Prediction,\" and its actual authors are **Hao Zhou, Yanze Zhang, and Wenhao Luo** (not Zetian Zhou and Shuo Yang). It does combine ACP with CBFs for safe RL, and was accepted to ICRA 2025. The technical description matches, but the author attribution is wrong.\n- **Verdict: INCORRECT** on author attribution. The first two authors named (Zetian Zhou, Shuo Yang) do not appear in the actual paper; the real authors are Hao Zhou and Yanze Zhang. The method description itself is accurate.\n\n---\n\n**5. gu2025safe** — NeurIPS 2025 (arXiv 2506.09937)\n\n- **Paper claims:** Trains a multitask failure detector on VLA internal features and uses conformal prediction to calibrate detection timing, triggering safe fallback behaviors when anomalous states are detected.\n- **Actual method:** SAFE extracts features from the last layer of a VLA, trains an MLP/LSTM failure detector, then uses **functional conformal prediction** on a hold-out calibration set to set a time-varying threshold for failure detection. Detection time/accuracy tradeoff is controlled via the CP significance level α. The paper does not explicitly emphasize \"safe fallback behaviors\" as a system component — it focuses on failure detection and timing; fallback action upon detection is implied but not the paper's contribution.\n- **Verdict: CORRECT** in substance. \"VLA internal features,\" CP-calibrated detection timing, and anomaly-triggered response are all accurate. The \"safe fallback behaviors\" framing is a mild overstatement of what the paper claims as its contribution (it focuses on detection, not the fallback policy), but it is not wrong.\n\n---\n\n**6. zollo2025vla_calibration** — arXiv 2507.17383\n\n- **Paper claims:** First systematic study of confidence calibration in VLAs, finding that prompt ensembles combined with Platt scaling improve calibration across manipulation tasks. Author listed as Matteo Zollo.\n- **Actual method:** The paper is indeed the first systematic study of VLA calibration, introducing prompt ensembles and action-wise Platt scaling as remedies. However, the first author's name is **Thomas Zollo**, not Matteo Zollo.\n- **Verdict: INCORRECT** on author name. \"Matteo Zollo\" does not exist in this paper; the author is Thomas Zollo. The method description is otherwise accurate.\n\n---\n\n**Summary table:**\n\n| Citation | Author/Venue | Method Description | Verdict |\n|---|---|---|---|\n| braun2025cgs | Correct | Correct | **CORRECT** |\n| zhao2024conformalized | Correct | Correct (adaptive CP detail omitted) | **CORRECT** |\n| wang2025cploop | Correct | Correct | **CORRECT** |\n| zhou2025acp_cbf | Wrong authors (Zetian Zhou → Hao Zhou; Shuo Yang → Yanze Zhang) | Correct | **INCORRECT** |\n| gu2025safe | Correct | Mostly correct; \"fallback behaviors\" overstated | **NEEDS_REVIEW** |\n| zollo2025vla_calibration | Wrong first name (Matteo → Thomas) | Correct | **INCORRECT** |\n\nSources:\n- [arXiv 2507.20941 – Multivariate Standardized Residuals for Conformal Prediction](https://arxiv.org/abs/2507.20941)\n- [arXiv 2406.07767 – Conformalized Teleoperation](https://arxiv.org/abs/2406.07767)\n- [arXiv 2510.16376 – Conformal Prediction in The Loop](https://arxiv.org/abs/2510.16376)\n- [arXiv 2503.17678 – Computationally and Sample Efficient Safe RL Using ACP](https://arxiv.org/abs/2503.17678)\n- [arXiv 2506.09937 – SAFE: Multitask Failure Detection for VLAs](https://arxiv.org/abs/2506.09937)\n- [arXiv 2507.17383 – Confidence Calibration in VLAs](https://arxiv.org/abs/2507.17383)"
      }
    ],
    "totalDurationMs": 96927,
    "totalTokens": 29077,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 724,
      "cache_creation_input_tokens": 1103,
      "cache_read_input_tokens": 25522,
      "output_tokens": 1728,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1103
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 724,
          "output_tokens": 1728,
          "cache_read_input_tokens": 25522,
          "cache_creation_input_tokens": 1103,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1103,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 13
    }
  }
}
```

</details>

---

### Tool result

_source line 261 · 2026-05-15T20:19:20.404Z_

<details><summary>↩ Tool result · `toolu_01YKk719A1AVTZCU14efaXwt`</summary>

```text
Web search results for query: "ReconVLA 2604.16677 abstract "action" "uncertainty" "conformal" "selection" full text arxiv 2026"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | alphaXiv","url":"https://www.alphaxiv.org/overview/2508.10333v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"[PDF] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver | Semantic Scholar","url":"https://www.semanticscholar.org/paper/ReconVLA:-Reconstructive-Vision-Language-Action-as-Song-Zhou/c87ea2afcd9212e5128e01daf17c733d285ac345"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model ...","url":"https://www.aimodels.fyi/papers/arxiv/reconvla-reconstructive-vision-language-action-model-as"},{"title":"Beyond ReconVLA: Annotation-Free Visual Grounding via Language-Attention Masked Reconstruction | HackerNoon","url":"https://hackernoon.com/beyond-reconvla-annotation-free-visual-grounding-via-language-attention-masked-reconstruction"},{"title":"[2603.16677] Correlated Quantum Phenomena in Confined Two-Dimensional Hexagonal Crystals","url":"https://arxiv.org/abs/2603.16677"},{"title":"[2601.16677] Sim-to-Real Transfer via a Style-Identified Cycle Consistent Generative Adversarial Network: Zero-Shot Deployment on Robotic Manipulators through Visual Domain Adaptation","url":"https://arxiv.org/abs/2601.16677"},{"title":"[2507.16677] Random quotients preserve acylindrical and hierarchical hyperbolicity","url":"https://arxiv.org/abs/2507.16677"}]

Based on the search results, I found the paper you're looking for. Here's the information about ReconVLA (arXiv:2604.16677):

## ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control

**Key Information:**
- arXiv:2604.16677v1 [cs.RO] 17 Apr 2026
- **Authors:** Lingling Chen, Zongyao Lyu, and William J. Beksi (The University of Texas at Arlington)

**Abstract Summary:**

Vision-language-action (VLA) models have emerged as generalist robotic controllers capable of mapping visual observations and natural language instructions to continuous action sequences. However, VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.

To address this problem the authors introduce ReconVLA, a reliable conformal model that produces uncertainty-guided and failure-aware control signals.

**Key Technical Contributions:**
- The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.
- The framework extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.

The full text is available on arXiv at https://arxiv.org/html/2604.16677v1


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "ce93077d-7ef9-484b-84b2-112d5908ca7e"
}
```

</details>

---

### System

_source line 262_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a4316cb586af54921",
  "tool_use_id": "toolu_019JGFjdzV7p1jtKiKLHkHpd",
  "status": "completed",
  "output_file": "",
  "summary": "Verify residual policy + UQ citations",
  "usage": {
    "total_tokens": 28235,
    "tool_uses": 17,
    "duration_ms": 115322
  },
  "uuid": "cd543ef6-681a-4565-93a8-6abbeced6fb0",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 263 · 2026-05-15T20:19:48.059Z_

<details><summary>↩ Tool result · `toolu_019JGFjdzV7p1jtKiKLHkHpd`</summary>

```text
Now I have enough information to make accurate assessments. Let me compile the final verdict for each citation.

---

## Citation Verification Report

---

### 1. silver2018residual — arXiv 1812.06298, "Residual Policy Learning"

**Paper claims:**
- "introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy"
- "introduced bounded residual corrections for combining learned and classical controllers"

**Actual method:**
- Zero-initialization: CORRECT — the paper explicitly zeroes the last layer of the network so the residual starts at zero, preserving the initial policy.
- Bounded corrections: INCORRECT — the paper does NOT use explicit bounded/clipped residual corrections. The composite policy operates within the standard action space but there is no mechanism constraining the residual magnitude.
- "Specifically for classical controllers": PARTIALLY INCORRECT — RPL is framed as broadly applicable to any base policy (hand-designed, MPC, learned), not specifically to "classical controllers." Classical controllers are one example, not the focus.

**Verdict: INCORRECT**
Zero-initialization is accurately attributed. However, "bounded corrections" is a fabricated mechanism — the paper has no explicit bounding/clipping of the residual. The framing "for classical controllers" overstates specificity; the paper is general.

---

### 2. jiang2024transic — arXiv 2405.10315, "TRANSIC"

**Paper claims:**
- "uses learned binary gating to selectively apply residual actions across different task phases"
- "uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse"

**Actual method:**
- Learned binary gate: CORRECT — TRANSIC uses a learned gating function `g_ψ` that acts as an indicator function `𝟙_g`, a binary selector for applying residual actions.
- "Across different task phases": NEEDS_REVIEW — the gate is state-conditioned (learned classifier on state features), not explicitly structured around named "task phases." The paper does not frame it as phase-based gating.
- Model collapse from ungated correction: CORRECT — the paper explicitly states that directly fine-tuning the base policy on correction data leads to "large motions and even model collapse."

**Verdict: NEEDS_REVIEW**
The binary gate and model-collapse claims are accurate. However, describing the gate as operating "across different task phases" mischaracterizes the mechanism — it is a state-conditioned binary classifier, not a phase-based switcher.

---

### 3. xiao2026pld — arXiv 2511.00091, "Self-Improving VLAs with Data Generation via Residual RL" (PLD)

**Paper claims:**
- "schedules magnitude bounds during training"
- "introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training"

**Actual method:**
- PLD = "Probe, Learn, Distill" — three-stage self-improvement framework for VLAs.
- Scheduled magnitude bound ξ: PARTIALLY CORRECT — the paper does introduce ξ as an action scale bound for the residual actor, tuned by a scheduler. However, the fetched content does not confirm the bound is *progressively increased* during training; rather ξ is a fixed hyperparameter tuned per benchmark (0.5 for LIBERO, 0.1 for SimplerEnv). The ablation shows setting ξ too large early hurts, but the scheduling direction (start small, grow) is not confirmed.

**Verdict: NEEDS_REVIEW**
The ξ bound and scheduler exist in the paper, but the specific characterization of "progressively increasing the allowed correction range during training" is not confirmed by retrieved content — ξ appears to be a fixed hyperparameter rather than a curriculum that grows during training.

---

### 4. pan2025drc — arXiv 2503.15368, "Online Imitation Learning via Decaying Relative Correction"

**Paper claims:** "applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones"

**Actual method:**
DRC applies a spatial correction vector (from expert teleoperation) that persists and fades exponentially over subsequent timesteps after the expert input — decay rate is `(1-r_decay)^(t - t_DRC)`. The rationale is that corrective trends remain valid across nearby timesteps, reducing required expert interventions.

The framing "early corrections matter more than late ones" (within-episode temporal weighting) is a fabricated interpretation. The decay is not about episode position but about persistence of each correction event over time after it is applied.

**Verdict: INCORRECT**
The paper's decay mechanism is temporal persistence of individual correction vectors (fading after each expert input), not a within-episode weighting scheme privileging early-episode corrections. The claimed intuition is wrong.

---

### 5. xing2026diu — arXiv 2605.00941, "Divergence is Uncertainty"

**Paper claims:** "derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling"

**Actual method:**
The paper proves that the trace of the posterior covariance over clean data equals, in closed form, the divergence of the velocity field (up to a known time-dependent prefactor and additive constant) — the "divergence-uncertainty identity." The matrix-level identity depends on the velocity Jacobian.

- Closed-form posterior covariance via velocity field divergence: CORRECT.
- Single-pass without additional sampling or ensemble: CORRECT — explicitly contrasted against retraining with variance heads, ensembles, or multi-step propagation.
- "Per-DOF uncertainty estimation": CORRECT — the matrix-level form gives per-degree-of-freedom covariance via the Jacobian.

**Verdict: CORRECT**
All elements of the attribution accurately describe the paper's contribution.

---

## Summary Table

| Citation | Verdict | Key Issue |
|---|---|---|
| silver2018residual | INCORRECT | "Bounded corrections" does not exist in the paper; "for classical controllers" overstates specificity. Zero-initialization is correct. |
| jiang2024transic | NEEDS_REVIEW | Binary gate and model-collapse claims are accurate; "across different task phases" mischaracterizes a state-conditioned classifier as phase-based. |
| xiao2026pld | NEEDS_REVIEW | ξ bound exists; "progressively increasing during training" not confirmed — ξ appears to be a fixed per-benchmark hyperparameter. |
| pan2025drc | INCORRECT | Decay is per-correction-event temporal persistence, not within-episode weighting favoring early corrections. Intuition stated is fabricated. |
| xing2026diu | CORRECT | All claims accurately match the paper. |

Sources:
- [Residual Policy Learning (arXiv:1812.06298)](https://arxiv.org/abs/1812.06298)
- [ar5iv HTML: Residual Policy Learning](https://ar5iv.labs.arxiv.org/html/1812.06298)
- [TRANSIC (arXiv:2405.10315)](https://arxiv.org/abs/2405.10315)
- [TRANSIC HTML](https://arxiv.org/html/2405.10315)
- [PLD: Self-Improving VLAs (arXiv:2511.00091)](https://arxiv.org/abs/2511.00091)
- [PLD HTML](https://arxiv.org/html/2511.00091)
- [DRC (arXiv:2503.15368)](https://arxiv.org/abs/2503.15368)
- [DRC HTML](https://arxiv.org/html/2503.15368)
- [Divergence is Uncertainty (arXiv:2605.00941)](https://arxiv.org/abs/2605.00941)

agentId: a4316cb586af54921 (use SendMessage with to: 'a4316cb586af54921' to continue this agent)
&lt;usage>total_tokens: 30095
tool_uses: 17
duration_ms: 115325&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "e716441f-a45c-4c11-a742-701d3c270649",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to verify method attribution accuracy for 5 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID or venue. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. silver2018residual** (RSS 2018, arXiv: 1812.06298)\nTitle: \"Residual Policy Learning\"\nAuthors: Tom Silver, Kelsey Allen, Josh Tenenbaum, Leslie Kaelbling\nPaper claims:\n- \"introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy\"\n- \"introduced bounded residual corrections for combining learned and classical controllers\"\n\n**2. jiang2024transic** (CoRL 2024, arXiv: 2405.10315)\nTitle: \"TRANSIC: Sim-to-Real Policy Transfer by Learning from Online Correction\"\nAuthors: Yunfan Jiang, Chen Wang, Ruohan Zhang, Jiajun Wu, Li Fei-Fei\nPaper claims:\n- \"uses learned binary gating to selectively apply residual actions across different task phases\"\n- \"uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse\"\n\n**3. xiao2026pld** (ICLR 2026, arXiv: 2511.00091)\nTitle: \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\"\nPaper claims:\n- \"schedules magnitude bounds during training\"\n- \"introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training\"\nNote: The paper title in the bib says \"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL\" but cited as \"PLD\" in text. Verify what PLD stands for and if the method description matches.\n\n**4. pan2025drc** (arXiv: 2503.15368)\nTitle: \"DRC: Decaying Relative Correction for Policy Refinement\"\nAuthors: Xinjie Pan et al.\nPaper claims: \"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n\n**5. xing2026diu** (arXiv: 2605.00941)\nTitle: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\nAuthors: Jiarui Xing, Song Wang, Jian Wang\nPaper claims: \"derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling\"\n\nSearch for each paper and verify the method descriptions.",
    "agentId": "a4316cb586af54921",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have enough information to make accurate assessments. Let me compile the final verdict for each citation.\n\n---\n\n## Citation Verification Report\n\n---\n\n### 1. silver2018residual — arXiv 1812.06298, \"Residual Policy Learning\"\n\n**Paper claims:**\n- \"introduced the framework for classical controllers, using zero-initialization and bounded corrections to ensure the learned residual improves upon rather than overrides the base policy\"\n- \"introduced bounded residual corrections for combining learned and classical controllers\"\n\n**Actual method:**\n- Zero-initialization: CORRECT — the paper explicitly zeroes the last layer of the network so the residual starts at zero, preserving the initial policy.\n- Bounded corrections: INCORRECT — the paper does NOT use explicit bounded/clipped residual corrections. The composite policy operates within the standard action space but there is no mechanism constraining the residual magnitude.\n- \"Specifically for classical controllers\": PARTIALLY INCORRECT — RPL is framed as broadly applicable to any base policy (hand-designed, MPC, learned), not specifically to \"classical controllers.\" Classical controllers are one example, not the focus.\n\n**Verdict: INCORRECT**\nZero-initialization is accurately attributed. However, \"bounded corrections\" is a fabricated mechanism — the paper has no explicit bounding/clipping of the residual. The framing \"for classical controllers\" overstates specificity; the paper is general.\n\n---\n\n### 2. jiang2024transic — arXiv 2405.10315, \"TRANSIC\"\n\n**Paper claims:**\n- \"uses learned binary gating to selectively apply residual actions across different task phases\"\n- \"uses a learned binary gate to decide whether to apply a sim-to-real residual at each step, demonstrating that ungated correction causes model collapse\"\n\n**Actual method:**\n- Learned binary gate: CORRECT — TRANSIC uses a learned gating function `g_ψ` that acts as an indicator function `𝟙_g`, a binary selector for applying residual actions.\n- \"Across different task phases\": NEEDS_REVIEW — the gate is state-conditioned (learned classifier on state features), not explicitly structured around named \"task phases.\" The paper does not frame it as phase-based gating.\n- Model collapse from ungated correction: CORRECT — the paper explicitly states that directly fine-tuning the base policy on correction data leads to \"large motions and even model collapse.\"\n\n**Verdict: NEEDS_REVIEW**\nThe binary gate and model-collapse claims are accurate. However, describing the gate as operating \"across different task phases\" mischaracterizes the mechanism — it is a state-conditioned binary classifier, not a phase-based switcher.\n\n---\n\n### 3. xiao2026pld — arXiv 2511.00091, \"Self-Improving VLAs with Data Generation via Residual RL\" (PLD)\n\n**Paper claims:**\n- \"schedules magnitude bounds during training\"\n- \"introduces a scheduled magnitude bound ξ for residual RL on VLAs, progressively increasing the allowed correction range during training\"\n\n**Actual method:**\n- PLD = \"Probe, Learn, Distill\" — three-stage self-improvement framework for VLAs.\n- Scheduled magnitude bound ξ: PARTIALLY CORRECT — the paper does introduce ξ as an action scale bound for the residual actor, tuned by a scheduler. However, the fetched content does not confirm the bound is *progressively increased* during training; rather ξ is a fixed hyperparameter tuned per benchmark (0.5 for LIBERO, 0.1 for SimplerEnv). The ablation shows setting ξ too large early hurts, but the scheduling direction (start small, grow) is not confirmed.\n\n**Verdict: NEEDS_REVIEW**\nThe ξ bound and scheduler exist in the paper, but the specific characterization of \"progressively increasing the allowed correction range during training\" is not confirmed by retrieved content — ξ appears to be a fixed hyperparameter rather than a curriculum that grows during training.\n\n---\n\n### 4. pan2025drc — arXiv 2503.15368, \"Online Imitation Learning via Decaying Relative Correction\"\n\n**Paper claims:** \"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n\n**Actual method:**\nDRC applies a spatial correction vector (from expert teleoperation) that persists and fades exponentially over subsequent timesteps after the expert input — decay rate is `(1-r_decay)^(t - t_DRC)`. The rationale is that corrective trends remain valid across nearby timesteps, reducing required expert interventions.\n\nThe framing \"early corrections matter more than late ones\" (within-episode temporal weighting) is a fabricated interpretation. The decay is not about episode position but about persistence of each correction event over time after it is applied.\n\n**Verdict: INCORRECT**\nThe paper's decay mechanism is temporal persistence of individual correction vectors (fading after each expert input), not a within-episode weighting scheme privileging early-episode corrections. The claimed intuition is wrong.\n\n---\n\n### 5. xing2026diu — arXiv 2605.00941, \"Divergence is Uncertainty\"\n\n**Paper claims:** \"derives a closed-form posterior covariance for flow-matching models by computing the divergence of the velocity field, enabling single-pass per-DOF uncertainty estimation without additional sampling\"\n\n**Actual method:**\nThe paper proves that the trace of the posterior covariance over clean data equals, in closed form, the divergence of the velocity field (up to a known time-dependent prefactor and additive constant) — the \"divergence-uncertainty identity.\" The matrix-level identity depends on the velocity Jacobian.\n\n- Closed-form posterior covariance via velocity field divergence: CORRECT.\n- Single-pass without additional sampling or ensemble: CORRECT — explicitly contrasted against retraining with variance heads, ensembles, or multi-step propagation.\n- \"Per-DOF uncertainty estimation\": CORRECT — the matrix-level form gives per-degree-of-freedom covariance via the Jacobian.\n\n**Verdict: CORRECT**\nAll elements of the attribution accurately describe the paper's contribution.\n\n---\n\n## Summary Table\n\n| Citation | Verdict | Key Issue |\n|---|---|---|\n| silver2018residual | INCORRECT | \"Bounded corrections\" does not exist in the paper; \"for classical controllers\" overstates specificity. Zero-initialization is correct. |\n| jiang2024transic | NEEDS_REVIEW | Binary gate and model-collapse claims are accurate; \"across different task phases\" mischaracterizes a state-conditioned classifier as phase-based. |\n| xiao2026pld | NEEDS_REVIEW | ξ bound exists; \"progressively increasing during training\" not confirmed — ξ appears to be a fixed per-benchmark hyperparameter. |\n| pan2025drc | INCORRECT | Decay is per-correction-event temporal persistence, not within-episode weighting favoring early corrections. Intuition stated is fabricated. |\n| xing2026diu | CORRECT | All claims accurately match the paper. |\n\nSources:\n- [Residual Policy Learning (arXiv:1812.06298)](https://arxiv.org/abs/1812.06298)\n- [ar5iv HTML: Residual Policy Learning](https://ar5iv.labs.arxiv.org/html/1812.06298)\n- [TRANSIC (arXiv:2405.10315)](https://arxiv.org/abs/2405.10315)\n- [TRANSIC HTML](https://arxiv.org/html/2405.10315)\n- [PLD: Self-Improving VLAs (arXiv:2511.00091)](https://arxiv.org/abs/2511.00091)\n- [PLD HTML](https://arxiv.org/html/2511.00091)\n- [DRC (arXiv:2503.15368)](https://arxiv.org/abs/2503.15368)\n- [DRC HTML](https://arxiv.org/html/2503.15368)\n- [Divergence is Uncertainty (arXiv:2605.00941)](https://arxiv.org/abs/2605.00941)"
      }
    ],
    "totalDurationMs": 115325,
    "totalTokens": 30095,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1872,
      "cache_read_input_tokens": 26294,
      "output_tokens": 1928,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1872
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1928,
          "cache_read_input_tokens": 26294,
          "cache_creation_input_tokens": 1872,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1872,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 17
    }
  }
}
```

</details>

---

### System

_source line 264_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a0b893d44a9c65a59",
  "tool_use_id": "toolu_01UTBsMvrTNRDfUAoqL6Dfkr",
  "status": "completed",
  "output_file": "",
  "summary": "Verify VLA inference-time citations",
  "usage": {
    "total_tokens": 35118,
    "tool_uses": 21,
    "duration_ms": 156733
  },
  "uuid": "a9e757e7-26f1-4e89-b5f1-27ca596b1f03",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e"
}
```

---

### Tool result

_source line 265 · 2026-05-15T20:20:00.470Z_

<details><summary>↩ Tool result · `toolu_01UTBsMvrTNRDfUAoqL6Dfkr`</summary>

```text
I now have enough information to make my assessments. Let me compile the final analysis based on all search results.

---

## Citation Attribution Verification Report

---

### 1. chen2026reconvla — arXiv:2604.16677
**Title:** ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control

**What the paper claims:**
- (Introduction) "draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate"
- (Method) "conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring"
- (Related work) "uses conformal prediction over multiple VLA samples for action selection and failure detection"

**What ReconVLA actually does:**
The actual ReconVLA (2604.16677) applies conformal prediction directly to the action token outputs of a single pretrained VLA policy to produce **calibrated uncertainty bounds**, not to rank/select among multiple generated samples. It uses:
- A **CQR-based estimator** (Conformalized Quantile Regression) to compute calibrated action-level uncertainty intervals, guiding reliable action selection under generative variability.
- An **SMD-based detector** (Squared Mahalanobis Distance) on latent state distributions for OOD/failure detection.

The framework does **not** operate by drawing N candidate actions and picking the best via a conformity score. Rather, it estimates uncertainty over a single action output and uses that uncertainty to guide control decisions. The "multiple samples + select best" paradigm described in the citing paper is a mischaracterization of ReconVLA's mechanism.

**Verdict: INCORRECT**

The introduction claim that ReconVLA "draws multiple action samples and selects the best one via conformal scoring" does not match the actual method. ReconVLA applies CQR-based uncertainty quantification to a single VLA output stream, not a sample-and-select procedure. The related work description partially overlaps (conformal prediction, failure detection, operates without retraining) but the core "multiple samples → select best" framing is wrong. The method section's claim that "our variant uses only Mahalanobis-based scoring" while ReconVLA uses "conformal selection" is also partly inverted — ReconVLA itself uses CQR + SMD (Mahalanobis), meaning the citing paper may have swapped which component belongs to which system.

---

### 2. liu2026scvla — arXiv:2602.21633
**Title:** Self-Correcting VLA: Online Action Refinement via Sparse World Imagination

**What the paper claims:**
- (Introduction) "learns a residual correction via reinforcement learning, requiring per-task environment interaction"
- (Related work) "performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy"

**What SC-VLA actually does:**
SC-VLA introduces: (1) **Sparse World Imagination** — auxiliary predictive heads that forecast task progress and future trajectory trends; (2) an **Online Action Refinement module** that uses **residual RL with progress-dependent dense rewards** shaped by the predicted sparse future states to adjust trajectory orientation.

The sparse world imagination component provides intrinsic reward signals (progress-dependent dense rewards), which are then used by the residual RL module to refine actions online.

**Verdict: CORRECT** (with a nuance)

The core claims — residual correction via RL, sparse world imagination — match the actual method. The claim that it "requires per-task environment interaction" is consistent with the RL-based refinement that relies on environment feedback. The description is accurate.

---

### 3. li2025vlapilot — arXiv:2511.14178
**Title:** Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion

**What the paper claims:**
- (Introduction) "steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step"
- (Related work) "applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation"

**What VLA-Pilot actually does:**
VLA-Pilot uses an **Embodied Evolutionary Diffusion** process as an action optimizer combined with an **MLLM-based open-world verifier** (via Embodied Policy Steering Chain-of-Thought, EPS-CoT) to steer a frozen pretrained VLA without any fine-tuning. The 2.41s per control step latency is confirmed in the paper (MLLM-based reward reasoning is the bottleneck). It is explicitly plug-and-play, requires no fine-tuning or task-specific training.

**Verdict: CORRECT**

All three elements — evolutionary optimization, MLLM verifier guidance, 2.41s latency, frozen VLA, plug-and-play — match the actual paper.

---

### 4. a2c2_2025 — arXiv:2509.23224
**Title:** Leave No Observation Behind: Real-time Correction for VLA Action Chunks

**What the paper claims:**
- (Introduction) "trains an asynchronous correction head **jointly with the VLA**, rather than as a post-hoc module on a frozen model"
- (Related work) "learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally..."

**What A2C2 actually does:**
A2C2 is a lightweight correction head that is trained on the **same dataset as the base policy**, but the base VLA remains **frozen** — "the approach requires no retraining of the base policy." The correction head is added as a plug-in to any off-the-shelf VLA and trained independently, not jointly with the VLA backbone.

**Verdict: INCORRECT**

The introduction's claim that A2C2 "trains an asynchronous correction head **jointly with the VLA**" directly contradicts the actual paper, which states the base policy is not retrained and the correction head is added post-hoc to a frozen VLA. A2C2 is precisely a "post-hoc module on a frozen model" — the opposite of what is claimed. The related work description (runs in parallel, reduces latency, applies correction unconditionally) is accurate, but the training characterization in the introduction is wrong.

---

## Summary Table

| # | Citation | Claim | Verdict |
|---|----------|-------|---------|
| 1 | chen2026reconvla (2604.16677) | Draws multiple samples, selects best via conformal scoring; conformal selection frontend | **INCORRECT** — ReconVLA uses CQR uncertainty bounds on a single action stream, not multi-sample selection |
| 2 | liu2026scvla (2602.21633) | Residual correction via RL, requires per-task environment interaction | **CORRECT** — SC-VLA uses residual RL with progress-dependent dense rewards from sparse world imagination |
| 3 | li2025vlapilot (2511.14178) | Evolutionary diffusion + MLLM verifier, 2.41s/step, plug-and-play | **CORRECT** — All details confirmed in the actual paper |
| 4 | a2c2_2025 (2509.23224) | Trains correction head jointly with the VLA | **INCORRECT** — A2C2 trains a correction head on a frozen base VLA; no joint training |

Sources:
- [ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control](https://arxiv.org/html/2604.16677v1)
- [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633)
- [Self-Correcting VLA HTML](https://arxiv.org/html/2602.21633)
- [Towards Deploying VLA without Fine-Tuning](https://arxiv.org/abs/2511.14178)
- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/abs/2509.23224)
- [Leave No Observation Behind HTML](https://arxiv.org/html/2509.23224)

agentId: a0b893d44a9c65a59 (use SendMessage with to: 'a0b893d44a9c65a59' to continue this agent)
&lt;usage>total_tokens: 37090
tool_uses: 21
duration_ms: 156735&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "3e6ad031-7af9-4cd1-b72c-519a4469ad3a",
  "tool_use_result": {
    "status": "completed",
    "prompt": "You need to verify method attribution accuracy for 4 citations in an academic paper. For each citation, I'll give you the citation key, what the paper claims about it, and the arXiv ID. Use WebSearch to verify each one. Report for each: what the paper claims, what the actual method is, and whether the attribution is CORRECT, INCORRECT, or NEEDS_REVIEW.\n\n**1. chen2026reconvla** (arXiv: 2604.16677)\nTitle: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\nPaper claims (in 3 places):\n- Introduction: \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate\"\n- Method: \"conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring\"\n- Related work: \"uses conformal prediction over multiple VLA samples for action selection and failure detection, providing a principled uncertainty-aware framework that operates without retraining\"\nKNOWN ISSUE: This citation's attribution has been flagged as potentially incorrect. Pay extra attention.\n\n**2. liu2026scvla** (arXiv: 2602.21633)\nTitle: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\nPaper claims:\n- Introduction (cited as sc_vla_2026): \"learns a residual correction via reinforcement learning, requiring per-task environment interaction\"\n- Related work: \"performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy\"\n\n**3. li2025vlapilot** (arXiv: 2511.14178)\nTitle: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\nPaper claims:\n- Introduction (cited as vla_pilot_2025): \"steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step\"\n- Related work: \"applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation\"\n\n**4. a2c2_2025** (arXiv: 2509.23224)\nTitle: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\nPaper claims:\n- Introduction: \"trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model\"\n- Related work: \"learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally without first selecting a high-quality starting action or modulating correction magnitude based on uncertainty\"\n\nSearch for each paper on arXiv and verify the method descriptions. Be thorough.",
    "agentId": "a0b893d44a9c65a59",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have enough information to make my assessments. Let me compile the final analysis based on all search results.\n\n---\n\n## Citation Attribution Verification Report\n\n---\n\n### 1. chen2026reconvla — arXiv:2604.16677\n**Title:** ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\n\n**What the paper claims:**\n- (Introduction) \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy that cannot produce actions better than the best candidate\"\n- (Method) \"conformal selection frontend of ReconVLA, which additionally incorporates outlier detection and failure anticipation; our variant uses only Mahalanobis-based scoring\"\n- (Related work) \"uses conformal prediction over multiple VLA samples for action selection and failure detection\"\n\n**What ReconVLA actually does:**\nThe actual ReconVLA (2604.16677) applies conformal prediction directly to the action token outputs of a single pretrained VLA policy to produce **calibrated uncertainty bounds**, not to rank/select among multiple generated samples. It uses:\n- A **CQR-based estimator** (Conformalized Quantile Regression) to compute calibrated action-level uncertainty intervals, guiding reliable action selection under generative variability.\n- An **SMD-based detector** (Squared Mahalanobis Distance) on latent state distributions for OOD/failure detection.\n\nThe framework does **not** operate by drawing N candidate actions and picking the best via a conformity score. Rather, it estimates uncertainty over a single action output and uses that uncertainty to guide control decisions. The \"multiple samples + select best\" paradigm described in the citing paper is a mischaracterization of ReconVLA's mechanism.\n\n**Verdict: INCORRECT**\n\nThe introduction claim that ReconVLA \"draws multiple action samples and selects the best one via conformal scoring\" does not match the actual method. ReconVLA applies CQR-based uncertainty quantification to a single VLA output stream, not a sample-and-select procedure. The related work description partially overlaps (conformal prediction, failure detection, operates without retraining) but the core \"multiple samples → select best\" framing is wrong. The method section's claim that \"our variant uses only Mahalanobis-based scoring\" while ReconVLA uses \"conformal selection\" is also partly inverted — ReconVLA itself uses CQR + SMD (Mahalanobis), meaning the citing paper may have swapped which component belongs to which system.\n\n---\n\n### 2. liu2026scvla — arXiv:2602.21633\n**Title:** Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\n\n**What the paper claims:**\n- (Introduction) \"learns a residual correction via reinforcement learning, requiring per-task environment interaction\"\n- (Related work) \"performs online action refinement through sparse world imagination combined with residual RL, but requires task-level RL training for the correction policy\"\n\n**What SC-VLA actually does:**\nSC-VLA introduces: (1) **Sparse World Imagination** — auxiliary predictive heads that forecast task progress and future trajectory trends; (2) an **Online Action Refinement module** that uses **residual RL with progress-dependent dense rewards** shaped by the predicted sparse future states to adjust trajectory orientation.\n\nThe sparse world imagination component provides intrinsic reward signals (progress-dependent dense rewards), which are then used by the residual RL module to refine actions online.\n\n**Verdict: CORRECT** (with a nuance)\n\nThe core claims — residual correction via RL, sparse world imagination — match the actual method. The claim that it \"requires per-task environment interaction\" is consistent with the RL-based refinement that relies on environment feedback. The description is accurate.\n\n---\n\n### 3. li2025vlapilot — arXiv:2511.14178\n**Title:** Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\n\n**What the paper claims:**\n- (Introduction) \"steers a frozen VLA through evolutionary optimization guided by an external multimodal verifier, but incurs 2.41s per control step\"\n- (Related work) \"applies evolutionary diffusion optimization guided by an MLLM verifier, achieving plug-and-play correction at the cost of 2.41s per control step—prohibitive for real-time manipulation\"\n\n**What VLA-Pilot actually does:**\nVLA-Pilot uses an **Embodied Evolutionary Diffusion** process as an action optimizer combined with an **MLLM-based open-world verifier** (via Embodied Policy Steering Chain-of-Thought, EPS-CoT) to steer a frozen pretrained VLA without any fine-tuning. The 2.41s per control step latency is confirmed in the paper (MLLM-based reward reasoning is the bottleneck). It is explicitly plug-and-play, requires no fine-tuning or task-specific training.\n\n**Verdict: CORRECT**\n\nAll three elements — evolutionary optimization, MLLM verifier guidance, 2.41s latency, frozen VLA, plug-and-play — match the actual paper.\n\n---\n\n### 4. a2c2_2025 — arXiv:2509.23224\n**Title:** Leave No Observation Behind: Real-time Correction for VLA Action Chunks\n\n**What the paper claims:**\n- (Introduction) \"trains an asynchronous correction head **jointly with the VLA**, rather than as a post-hoc module on a frozen model\"\n- (Related work) \"learns an asynchronous residual correction that runs in parallel with the base policy's chunk generation, reducing latency; however, it applies correction unconditionally...\"\n\n**What A2C2 actually does:**\nA2C2 is a lightweight correction head that is trained on the **same dataset as the base policy**, but the base VLA remains **frozen** — \"the approach requires no retraining of the base policy.\" The correction head is added as a plug-in to any off-the-shelf VLA and trained independently, not jointly with the VLA backbone.\n\n**Verdict: INCORRECT**\n\nThe introduction's claim that A2C2 \"trains an asynchronous correction head **jointly with the VLA**\" directly contradicts the actual paper, which states the base policy is not retrained and the correction head is added post-hoc to a frozen VLA. A2C2 is precisely a \"post-hoc module on a frozen model\" — the opposite of what is claimed. The related work description (runs in parallel, reduces latency, applies correction unconditionally) is accurate, but the training characterization in the introduction is wrong.\n\n---\n\n## Summary Table\n\n| # | Citation | Claim | Verdict |\n|---|----------|-------|---------|\n| 1 | chen2026reconvla (2604.16677) | Draws multiple samples, selects best via conformal scoring; conformal selection frontend | **INCORRECT** — ReconVLA uses CQR uncertainty bounds on a single action stream, not multi-sample selection |\n| 2 | liu2026scvla (2602.21633) | Residual correction via RL, requires per-task environment interaction | **CORRECT** — SC-VLA uses residual RL with progress-dependent dense rewards from sparse world imagination |\n| 3 | li2025vlapilot (2511.14178) | Evolutionary diffusion + MLLM verifier, 2.41s/step, plug-and-play | **CORRECT** — All details confirmed in the actual paper |\n| 4 | a2c2_2025 (2509.23224) | Trains correction head jointly with the VLA | **INCORRECT** — A2C2 trains a correction head on a frozen base VLA; no joint training |\n\nSources:\n- [ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control](https://arxiv.org/html/2604.16677v1)\n- [Self-Correcting VLA: Online Action Refinement via Sparse World Imagination](https://arxiv.org/abs/2602.21633)\n- [Self-Correcting VLA HTML](https://arxiv.org/html/2602.21633)\n- [Towards Deploying VLA without Fine-Tuning](https://arxiv.org/abs/2511.14178)\n- [Leave No Observation Behind: Real-time Correction for VLA Action Chunks](https://arxiv.org/abs/2509.23224)\n- [Leave No Observation Behind HTML](https://arxiv.org/html/2509.23224)"
      }
    ],
    "totalDurationMs": 156735,
    "totalTokens": 37090,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1870,
      "cache_read_input_tokens": 33168,
      "output_tokens": 2051,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1870
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2051,
          "cache_read_input_tokens": 33168,
          "cache_creation_input_tokens": 1870,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1870,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 21
    }
  }
}
```

</details>

---

### Assistant

_source line 266_

<details><summary>Logged reasoning block</summary>

```text
All 5 agents have returned. Let me compile the results and create the audit report. Let me summarize all findings:

**INCORRECT (need fixing):**
1. **chen2026reconvla** — Paper claims "draws multiple action samples and selects the best one via conformal scoring." Actual: ReconVLA uses CQR-based uncertainty bounds on a single action stream, not multi-sample selection.
2. **a2c2_2025** — Paper claims "trains an asynchronous correction head jointly with the VLA." Actual: A2C2 trains on a frozen base VLA; it IS a post-hoc module.


3. **digflow2025** — Paper claims "regularizes the flow-matching denoising trajectory via a discrepancy-guided objective." Actual: DiG-Flow operates at the representation level with a gating signal, not regularizing the denoising trajectory.
4. **silver2018residual** — Paper claims "bounded corrections." Actual: No explicit bounding/clipping in the paper. Zero-initialization is correct.
5. **pan2025drc** — Paper claims "temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones." Actual: Decay is per-correction-event temporal persistence, not within-episode weighting.

Now I'm catching some bibliographic errors and method description issues. Zhou2025acp_cbf has the wrong author names listed (should be Hao Zhou and Yanze Zhang, not Zetian Zhou and Shuo Yang), though the method itself is described accurately. Similarly, zollo2025vla_calibration has a first name error in the bibliography (Thomas, not Matteo), but the method description is fine. I'm also flagging several entries that need closer review: srpo2025's "self-referential" concept needs clarification, fei2025liberoplus's perturbation types don't quite match what the paper describes, jiang2024transic's binary gate characterization misrepresents the task phase aspect, xiao2026pld's ξ bound claim lacks confirmation about progressive increase, and gu2025safe's description appears incomplete.

I've verified that the remaining fifteen entries are accurate. Now I need to compile the audit report and make sure to highlight those bibliography errors alongside the method attribution issues, then register the findings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "93df50b1-b7a8-48d0-952b-25e2822d651a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rud91qKgtqyiqHK6FDuzYV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 48248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

_source line 267_

全部验证完成。汇总结果：7 个 INCORRECT，5 个 NEEDS_REVIEW，15 个 CORRECT。现在写审计报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "7c488067-b240-4dad-8530-e4cfddbd12db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rud91qKgtqyiqHK6FDuzYV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 48248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

_source line 268_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TBZfDosCyUDcBgGVXqKBSn`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "45322cef-0810-477d-863e-81e13130a545",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Rud91qKgtqyiqHK6FDuzYV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12953,
      "cache_read_input_tokens": 48248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12953
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

_source line 269 · 2026-05-15T20:20:19.449Z_

<details><summary>↩ Tool result · `toolu_01TBZfDosCyUDcBgGVXqKBSn`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
}
```

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
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "deed3861-1fd5-4f04-b397-9f44545901c0",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__register_artifact",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__register_artifact,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Tool call

_source line 270_

<details open><summary>🔧 Tool call — Write · `toolu_01JK4NDSrEQxEBtS7SkvF4Fx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md",
  "content": "# Citation Attribution Audit — 2026-05-15\n\n## 审计范围\n- introduction_scenarioC.tex, method.tex, experiments.tex, related_work.tex\n- 共 27 个唯一引用，每个均通过 WebSearch 验证方法归因准确性\n\n## 审计结果\n\n| Citation Key | 论文中的描述 | 实际方法 | 状态 | 备注 |\n|---|---|---|---|---|\n| black2024pi0 | VLA that generates actions via flow matching | π₀ is a Vision-Language-Action Flow Model | CORRECT | — |\n| shukor2025smolvla | 450M-parameter flow-matching VLA | SmolVLA confirmed 450M params, flow matching action expert | CORRECT | — |\n| liu2023libero | Standard manipulation benchmark | LIBERO is a NeurIPS 2023 benchmark with 130 manipulation tasks | CORRECT | — |\n| fei2025liberoplus | Distribution shifts (object appearance, lighting, sensor noise) cause performance degradation | LIBERO-Plus covers 7 perturbation types; \"object appearance changes\" not a precise match—paper covers objects layout, background textures, camera viewpoints, etc. | NEEDS_REVIEW | 论文中 \"object appearance changes\" 应改为更准确的描述，如 \"visual perturbations\" |\n| robustvla2025 | Combines RL post-training with Jacobian regularization | Confirmed: online RL post-training + Jacobian regularization + smoothness regularization | CORRECT | — |\n| srpo2025 | Self-referential RL fine-tuning, using policy's own rollouts as training signal | Uses own *successful* rollouts as reference to reward *failed* trajectories via latent world model | NEEDS_REVIEW | \"own rollouts as training signal\" 方向正确但过于简化；核心是成功/失败轨迹对比 |\n| digflow2025 | Regularizes the flow-matching denoising trajectory via a discrepancy-guided objective | DiG-Flow operates at representation level: computes distributional discrepancy between observation/action embeddings as gating signal (DiG-Block); flow matching path is NOT modified | **INCORRECT** | 论文不是 \"regularize denoising trajectory\"，而是在 representation level 用 discrepancy gating |\n| chen2026reconvla | Draws multiple action samples and selects the best via conformal scoring—a pure sample selection strategy | ReconVLA uses CQR-based uncertainty bounds on single action output stream + SMD-based OOD detection; NOT multi-sample selection | **INCORRECT** | 已知问题确认。Introduction/Method/Related Work 三处均有错误描述 |\n| liu2026scvla (sc_vla_2026) | Learns residual correction via RL, requiring per-task environment interaction | SC-VLA uses sparse world imagination + residual RL with progress-dependent dense rewards | CORRECT | — |\n| li2025vlapilot (vla_pilot_2025) | Evolutionary optimization guided by MLLM verifier, 2.41s/step | Embodied Evolutionary Diffusion + EPS-CoT MLLM verifier, 2.41s confirmed | CORRECT | — |\n| a2c2_2025 | Trains correction head **jointly with the VLA**, not a post-hoc module on frozen model | A2C2 trains correction head on **frozen** base VLA; IS a post-hoc module | **INCORRECT** | Introduction 中 \"jointly with the VLA\" 与实际完全相反 |\n| braun2025cgs | CGS uses Mahalanobis-based nonconformity scores respecting cross-dimensional covariance | Confirmed: Mahalanobis distance from learned local covariance as nonconformity score | CORRECT | — |\n| ross2011dagger | Compounding error in imitation learning | DAgger paper, central contribution is compounding error/covariate shift | CORRECT | — |\n| silver2018residual | Introduced bounded residual corrections for combining learned and classical controllers; zero-initialization | Zero-initialization: CORRECT. **Bounded corrections: NOT in the paper**—no explicit bounding/clipping. \"For classical controllers\" overstates specificity | **INCORRECT** | 需删除 \"bounded corrections\" 归因；Silver et al. 用的是 zero-initialization，不是 bounded corrections |\n| jiang2024transic | Learned binary gating to selectively apply residual actions across different task phases; ungated causes model collapse | Binary gate: CORRECT. Model collapse: CORRECT. \"Across task phases\" 不准确—gate 是 state-conditioned binary classifier，不是 phase-based | NEEDS_REVIEW | \"across different task phases\" 改为 \"conditioned on the current state\" |\n| xiao2026pld | Scheduled magnitude bound ξ, progressively increasing during training | ξ bound exists; but \"progressively increasing\" 未确认—ξ 似乎是 per-benchmark 固定超参 (LIBERO=0.5, SimplerEnv=0.1) | NEEDS_REVIEW | \"progressively increasing\" 可能不准确，需要进一步确认或改为 \"tuned per benchmark\" |\n| pan2025drc | Temporal decay of correction magnitude over episode; early corrections matter more | Decay is per-correction-event exponential persistence after each expert input, NOT within-episode weighting favoring early corrections | **INCORRECT** | 描述的 intuition 完全错误；DRC 的 decay 是每次纠正事件后的衰减，不是 episode 级别 |\n| lipman2023flow | Foundational flow matching method | Flow Matching for Continuous Normalizing Flows, ICLR 2023 | CORRECT | — |\n| ledoit2004well | Ledoit-Wolf shrinkage with analytically optimal shrinkage intensity | Linear shrinkage with consistent optimal intensity estimator | CORRECT | — |\n| liu2026ttvla | Test-time RL with progress rewards, requires per-task reward design and gradient updates | Confirmed: test-time RL adaptation with step-by-step progress signals | CORRECT | — |\n| angelopoulos2023gentle | CP provides distribution-free coverage guarantees under exchangeability | Confirmed: central theorem of the tutorial | CORRECT | — |\n| zhao2024conformalized | CP for uncertainty in high-DOF action mappings in shared autonomy, flagging unreliable predictions | Uses adaptive CP on joystick-to-robot action mapping, proactive intervention seeking | CORRECT | — |\n| wang2025cploop | CP regions as feedback constraints in trajectory optimization | Fb-CP framework, bidirectional feedback between CP and trajectory optimization | CORRECT | — |\n| zhou2025acp_cbf | Combines ACP with CBFs for safe RL under distribution shift | Method description CORRECT, but **authors wrong in bib**: should be Hao Zhou, Yanze Zhang (not Zetian Zhou, Shuo Yang) | **INCORRECT** | Bib 文件作者需修正 |\n| gu2025safe | Multitask failure detector on VLA features, CP-calibrated detection timing, safe fallback | Failure detection + functional CP for timing threshold: CORRECT. \"Safe fallback behaviors\" 轻微夸大—论文聚焦检测，不是 fallback 策略 | NEEDS_REVIEW | \"triggering safe fallback behaviors\" 可简化为 \"triggering intervention\" |\n| xing2026diu | Closed-form posterior covariance via velocity field divergence, single-pass per-DOF UQ | Confirmed: divergence-uncertainty identity, single-pass without sampling | CORRECT | — |\n| zollo2025vla_calibration | First systematic VLA calibration study; prompt ensembles + Platt scaling | Method description CORRECT, but **first author name wrong in bib**: Thomas Zollo (not Matteo Zollo) | **INCORRECT** | Bib 文件作者名需修正 |\n\n## 统计\n- **CORRECT**: 15/27\n- **INCORRECT**: 7/27 (chen2026reconvla, a2c2_2025, digflow2025, silver2018residual, pan2025drc, zhou2025acp_cbf, zollo2025vla_calibration)\n- **NEEDS_REVIEW**: 5/27 (fei2025liberoplus, srpo2025, jiang2024transic, xiao2026pld, gu2025safe)\n\n## 需要修正的引用\n\n### 🔴 INCORRECT — 必须修正\n\n**1. chen2026reconvla (Introduction + Method + Related Work)**\n- 错误：描述为 \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy\"\n- 实际：ReconVLA 使用 CQR (Conformalized Quantile Regression) 对单次 action 输出计算校准不确定性区间 + SMD-based OOD 检测，不是多样本选择\n- 修改建议：\n  - Introduction: 改为 \"applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states via Mahalanobis distance—an uncertainty quantification and failure detection framework that does not perform multi-sample selection\"\n  - Method (Eq. 4 上方): 改为 \"inspired by conformal scoring methods such as ReconVLA\" 而非 \"conformal selection frontend of ReconVLA\"\n  - Related Work: 修正描述，强调 CQR-based UQ + OOD detection\n\n**2. a2c2_2025 (Introduction)**\n- 错误：\"trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model\"\n- 实际：A2C2 的 base VLA 是 frozen 的，correction head 是 post-hoc 添加并独立训练的\n- 修改建议：改为 \"adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection\"\n\n**3. digflow2025 (Related Work)**\n- 错误：\"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective\"\n- 实际：DiG-Flow 在 representation level 计算 observation/action embedding 之间的分布差异作为 gating signal (DiG-Block)，flow matching path 本身不被修改\n- 修改建议：改为 \"uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance control between the foundation model and the flow expert\"\n\n**4. silver2018residual (Introduction + Related Work)**\n- 错误：归因了 \"bounded corrections\"\n- 实际：Silver et al. 使用 zero-initialization 使 residual 从零开始，但没有显式的 bounded/clipped corrections\n- 修改建议：\n  - Related Work: 改为 \"introduced the framework, using zero-initialization to ensure the learned residual starts as a no-op and gradually improves upon the base policy\"\n  - 删除所有 \"bounded corrections\" 归因到 Silver et al. 的地方\n\n**5. pan2025drc (Related Work)**\n- 错误：\"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n- 实际：DRC 的 decay 是每次专家纠正事件后的指数衰减持续性，不是 episode 级别的时间权重\n- 修改建议：改为 \"applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over subsequent timesteps after application\"\n\n**6. zhou2025acp_cbf (references.bib)**\n- 错误：作者 \"Zetian Zhou, Shuo Yang, Wenhao Luo\"\n- 实际：应为 \"Hao Zhou, Yanze Zhang, Wenhao Luo\"\n- 修改建议：更新 bib 中的 author 字段\n\n**7. zollo2025vla_calibration (references.bib)**\n- 错误：作者 \"Matteo Zollo\"\n- 实际：应为 \"Thomas Zollo\"\n- 修改建议：更新 bib 中的 author 字段\n\n### 🟡 NEEDS_REVIEW — 建议修正\n\n**8. fei2025liberoplus (Introduction)**\n- \"object appearance changes\" 不是 LIBERO-Plus 的精确描述；论文覆盖 objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise\n- 建议改为 \"visual and physical perturbations\" 或列举更准确的类别\n\n**9. srpo2025 (Related Work)**\n- \"using the policy's own rollouts as training signal\" 过于简化\n- 建议改为 \"using the policy's own successful rollouts as reference to shape rewards for failed trajectories\"\n\n**10. jiang2024transic (Related Work)**\n- \"across different task phases\" 不准确，gate 是 state-conditioned 的\n- 建议改为 \"conditioned on the current state to decide whether to apply correction at each step\"\n\n**11. xiao2026pld (Related Work)**\n- \"progressively increasing the allowed correction range during training\" 未确认\n- 建议改为 \"introducing a magnitude bound ξ for the residual actor, tuned per benchmark\"\n\n**12. gu2025safe (Related Work)**\n- \"triggering safe fallback behaviors\" 轻微夸大\n- 建议改为 \"triggering intervention when anomalous states are detected\"\n\n## 总结\n27 个引用中有 7 个方法归因错误（包括 2 个 bib 作者错误），5 个需要措辞调整。最严重的问题是 chen2026reconvla（核心机制描述完全错误，出现在三个章节）和 a2c2_2025（训练方式描述与实际相反）。这两个修正是提交前的 blocking items。silver2018residual 的 \"bounded corrections\" 归因错误也需要修正，因为它影响了 Related Work 中 magnitude control 叙事的准确性。\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "dfa96c56-e5f6-4e84-aeeb-0f8e31a3ba43",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MPdnW9Hya2916dYUuEPrRe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1767,
      "cache_read_input_tokens": 61201,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1767
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 271 · 2026-05-15T20:21:31.587Z_

<details><summary>↩ Tool result · `toolu_01JK4NDSrEQxEBtS7SkvF4Fx`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "996d07a6-11b1-43e0-a53d-f7411f665660",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md",
    "content": "# Citation Attribution Audit — 2026-05-15\n\n## 审计范围\n- introduction_scenarioC.tex, method.tex, experiments.tex, related_work.tex\n- 共 27 个唯一引用，每个均通过 WebSearch 验证方法归因准确性\n\n## 审计结果\n\n| Citation Key | 论文中的描述 | 实际方法 | 状态 | 备注 |\n|---|---|---|---|---|\n| black2024pi0 | VLA that generates actions via flow matching | π₀ is a Vision-Language-Action Flow Model | CORRECT | — |\n| shukor2025smolvla | 450M-parameter flow-matching VLA | SmolVLA confirmed 450M params, flow matching action expert | CORRECT | — |\n| liu2023libero | Standard manipulation benchmark | LIBERO is a NeurIPS 2023 benchmark with 130 manipulation tasks | CORRECT | — |\n| fei2025liberoplus | Distribution shifts (object appearance, lighting, sensor noise) cause performance degradation | LIBERO-Plus covers 7 perturbation types; \"object appearance changes\" not a precise match—paper covers objects layout, background textures, camera viewpoints, etc. | NEEDS_REVIEW | 论文中 \"object appearance changes\" 应改为更准确的描述，如 \"visual perturbations\" |\n| robustvla2025 | Combines RL post-training with Jacobian regularization | Confirmed: online RL post-training + Jacobian regularization + smoothness regularization | CORRECT | — |\n| srpo2025 | Self-referential RL fine-tuning, using policy's own rollouts as training signal | Uses own *successful* rollouts as reference to reward *failed* trajectories via latent world model | NEEDS_REVIEW | \"own rollouts as training signal\" 方向正确但过于简化；核心是成功/失败轨迹对比 |\n| digflow2025 | Regularizes the flow-matching denoising trajectory via a discrepancy-guided objective | DiG-Flow operates at representation level: computes distributional discrepancy between observation/action embeddings as gating signal (DiG-Block); flow matching path is NOT modified | **INCORRECT** | 论文不是 \"regularize denoising trajectory\"，而是在 representation level 用 discrepancy gating |\n| chen2026reconvla | Draws multiple action samples and selects the best via conformal scoring—a pure sample selection strategy | ReconVLA uses CQR-based uncertainty bounds on single action output stream + SMD-based OOD detection; NOT multi-sample selection | **INCORRECT** | 已知问题确认。Introduction/Method/Related Work 三处均有错误描述 |\n| liu2026scvla (sc_vla_2026) | Learns residual correction via RL, requiring per-task environment interaction | SC-VLA uses sparse world imagination + residual RL with progress-dependent dense rewards | CORRECT | — |\n| li2025vlapilot (vla_pilot_2025) | Evolutionary optimization guided by MLLM verifier, 2.41s/step | Embodied Evolutionary Diffusion + EPS-CoT MLLM verifier, 2.41s confirmed | CORRECT | — |\n| a2c2_2025 | Trains correction head **jointly with the VLA**, not a post-hoc module on frozen model | A2C2 trains correction head on **frozen** base VLA; IS a post-hoc module | **INCORRECT** | Introduction 中 \"jointly with the VLA\" 与实际完全相反 |\n| braun2025cgs | CGS uses Mahalanobis-based nonconformity scores respecting cross-dimensional covariance | Confirmed: Mahalanobis distance from learned local covariance as nonconformity score | CORRECT | — |\n| ross2011dagger | Compounding error in imitation learning | DAgger paper, central contribution is compounding error/covariate shift | CORRECT | — |\n| silver2018residual | Introduced bounded residual corrections for combining learned and classical controllers; zero-initialization | Zero-initialization: CORRECT. **Bounded corrections: NOT in the paper**—no explicit bounding/clipping. \"For classical controllers\" overstates specificity | **INCORRECT** | 需删除 \"bounded corrections\" 归因；Silver et al. 用的是 zero-initialization，不是 bounded corrections |\n| jiang2024transic | Learned binary gating to selectively apply residual actions across different task phases; ungated causes model collapse | Binary gate: CORRECT. Model collapse: CORRECT. \"Across task phases\" 不准确—gate 是 state-conditioned binary classifier，不是 phase-based | NEEDS_REVIEW | \"across different task phases\" 改为 \"conditioned on the current state\" |\n| xiao2026pld | Scheduled magnitude bound ξ, progressively increasing during training | ξ bound exists; but \"progressively increasing\" 未确认—ξ 似乎是 per-benchmark 固定超参 (LIBERO=0.5, SimplerEnv=0.1) | NEEDS_REVIEW | \"progressively increasing\" 可能不准确，需要进一步确认或改为 \"tuned per benchmark\" |\n| pan2025drc | Temporal decay of correction magnitude over episode; early corrections matter more | Decay is per-correction-event exponential persistence after each expert input, NOT within-episode weighting favoring early corrections | **INCORRECT** | 描述的 intuition 完全错误；DRC 的 decay 是每次纠正事件后的衰减，不是 episode 级别 |\n| lipman2023flow | Foundational flow matching method | Flow Matching for Continuous Normalizing Flows, ICLR 2023 | CORRECT | — |\n| ledoit2004well | Ledoit-Wolf shrinkage with analytically optimal shrinkage intensity | Linear shrinkage with consistent optimal intensity estimator | CORRECT | — |\n| liu2026ttvla | Test-time RL with progress rewards, requires per-task reward design and gradient updates | Confirmed: test-time RL adaptation with step-by-step progress signals | CORRECT | — |\n| angelopoulos2023gentle | CP provides distribution-free coverage guarantees under exchangeability | Confirmed: central theorem of the tutorial | CORRECT | — |\n| zhao2024conformalized | CP for uncertainty in high-DOF action mappings in shared autonomy, flagging unreliable predictions | Uses adaptive CP on joystick-to-robot action mapping, proactive intervention seeking | CORRECT | — |\n| wang2025cploop | CP regions as feedback constraints in trajectory optimization | Fb-CP framework, bidirectional feedback between CP and trajectory optimization | CORRECT | — |\n| zhou2025acp_cbf | Combines ACP with CBFs for safe RL under distribution shift | Method description CORRECT, but **authors wrong in bib**: should be Hao Zhou, Yanze Zhang (not Zetian Zhou, Shuo Yang) | **INCORRECT** | Bib 文件作者需修正 |\n| gu2025safe | Multitask failure detector on VLA features, CP-calibrated detection timing, safe fallback | Failure detection + functional CP for timing threshold: CORRECT. \"Safe fallback behaviors\" 轻微夸大—论文聚焦检测，不是 fallback 策略 | NEEDS_REVIEW | \"triggering safe fallback behaviors\" 可简化为 \"triggering intervention\" |\n| xing2026diu | Closed-form posterior covariance via velocity field divergence, single-pass per-DOF UQ | Confirmed: divergence-uncertainty identity, single-pass without sampling | CORRECT | — |\n| zollo2025vla_calibration | First systematic VLA calibration study; prompt ensembles + Platt scaling | Method description CORRECT, but **first author name wrong in bib**: Thomas Zollo (not Matteo Zollo) | **INCORRECT** | Bib 文件作者名需修正 |\n\n## 统计\n- **CORRECT**: 15/27\n- **INCORRECT**: 7/27 (chen2026reconvla, a2c2_2025, digflow2025, silver2018residual, pan2025drc, zhou2025acp_cbf, zollo2025vla_calibration)\n- **NEEDS_REVIEW**: 5/27 (fei2025liberoplus, srpo2025, jiang2024transic, xiao2026pld, gu2025safe)\n\n## 需要修正的引用\n\n### 🔴 INCORRECT — 必须修正\n\n**1. chen2026reconvla (Introduction + Method + Related Work)**\n- 错误：描述为 \"draws multiple action samples and selects the best one via conformal scoring—a pure sample selection strategy\"\n- 实际：ReconVLA 使用 CQR (Conformalized Quantile Regression) 对单次 action 输出计算校准不确定性区间 + SMD-based OOD 检测，不是多样本选择\n- 修改建议：\n  - Introduction: 改为 \"applies conformal quantile regression to calibrate action-level uncertainty bounds and detects out-of-distribution states via Mahalanobis distance—an uncertainty quantification and failure detection framework that does not perform multi-sample selection\"\n  - Method (Eq. 4 上方): 改为 \"inspired by conformal scoring methods such as ReconVLA\" 而非 \"conformal selection frontend of ReconVLA\"\n  - Related Work: 修正描述，强调 CQR-based UQ + OOD detection\n\n**2. a2c2_2025 (Introduction)**\n- 错误：\"trains an asynchronous correction head jointly with the VLA, rather than as a post-hoc module on a frozen model\"\n- 实际：A2C2 的 base VLA 是 frozen 的，correction head 是 post-hoc 添加并独立训练的\n- 修改建议：改为 \"adds a lightweight asynchronous correction head to a frozen VLA that runs in parallel with chunk generation, but applies correction unconditionally without uncertainty-guided selection\"\n\n**3. digflow2025 (Related Work)**\n- 错误：\"regularizes the flow-matching denoising trajectory via a discrepancy-guided objective\"\n- 实际：DiG-Flow 在 representation level 计算 observation/action embedding 之间的分布差异作为 gating signal (DiG-Block)，flow matching path 本身不被修改\n- 修改建议：改为 \"uses distributional discrepancy between observation and action embeddings as a gating signal to rebalance control between the foundation model and the flow expert\"\n\n**4. silver2018residual (Introduction + Related Work)**\n- 错误：归因了 \"bounded corrections\"\n- 实际：Silver et al. 使用 zero-initialization 使 residual 从零开始，但没有显式的 bounded/clipped corrections\n- 修改建议：\n  - Related Work: 改为 \"introduced the framework, using zero-initialization to ensure the learned residual starts as a no-op and gradually improves upon the base policy\"\n  - 删除所有 \"bounded corrections\" 归因到 Silver et al. 的地方\n\n**5. pan2025drc (Related Work)**\n- 错误：\"applies temporal decay of correction magnitude over the course of an episode, reflecting the intuition that early corrections matter more than late ones\"\n- 实际：DRC 的 decay 是每次专家纠正事件后的指数衰减持续性，不是 episode 级别的时间权重\n- 修改建议：改为 \"applies exponential decay to each expert correction event, allowing corrective signals to persist and fade over subsequent timesteps after application\"\n\n**6. zhou2025acp_cbf (references.bib)**\n- 错误：作者 \"Zetian Zhou, Shuo Yang, Wenhao Luo\"\n- 实际：应为 \"Hao Zhou, Yanze Zhang, Wenhao Luo\"\n- 修改建议：更新 bib 中的 author 字段\n\n**7. zollo2025vla_calibration (references.bib)**\n- 错误：作者 \"Matteo Zollo\"\n- 实际：应为 \"Thomas Zollo\"\n- 修改建议：更新 bib 中的 author 字段\n\n### 🟡 NEEDS_REVIEW — 建议修正\n\n**8. fei2025liberoplus (Introduction)**\n- \"object appearance changes\" 不是 LIBERO-Plus 的精确描述；论文覆盖 objects layout, camera viewpoints, robot initial states, language instructions, light conditions, background textures, sensor noise\n- 建议改为 \"visual and physical perturbations\" 或列举更准确的类别\n\n**9. srpo2025 (Related Work)**\n- \"using the policy's own rollouts as training signal\" 过于简化\n- 建议改为 \"using the policy's own successful rollouts as reference to shape rewards for failed trajectories\"\n\n**10. jiang2024transic (Related Work)**\n- \"across different task phases\" 不准确，gate 是 state-conditioned 的\n- 建议改为 \"conditioned on the current state to decide whether to apply correction at each step\"\n\n**11. xiao2026pld (Related Work)**\n- \"progressively increasing the allowed correction range during training\" 未确认\n- 建议改为 \"introducing a magnitude bound ξ for the residual actor, tuned per benchmark\"\n\n**12. gu2025safe (Related Work)**\n- \"triggering safe fallback behaviors\" 轻微夸大\n- 建议改为 \"triggering intervention when anomalous states are detected\"\n\n## 总结\n27 个引用中有 7 个方法归因错误（包括 2 个 bib 作者错误），5 个需要措辞调整。最严重的问题是 chen2026reconvla（核心机制描述完全错误，出现在三个章节）和 a2c2_2025（训练方式描述与实际相反）。这两个修正是提交前的 blocking items。silver2018residual 的 \"bounded corrections\" 归因错误也需要修正，因为它影响了 Related Work 中 magnitude control 叙事的准确性。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Tool call

_source line 272_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01RGzqRHVgLYxZHJd4Tm2Rrq`</summary>

```json
{
  "name": "Citation Attribution Audit",
  "type": "report",
  "description": "CoRL 2026 论文全量引用方法归因审计。27个引用验证结果：7 INCORRECT, 5 NEEDS_REVIEW, 15 CORRECT。含具体修改建议。",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/citation_attribution_audit.md",
  "tags": [
    "paper",
    "citation-audit",
    "pre-submission"
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
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "d9a044ee-c374-4319-95c2-3c41b4546343",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Afb7C5DL5aR51JopUTKsCy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3774,
      "cache_read_input_tokens": 62968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3774
      },
      "output_tokens": 56,
      "service_tier": "standard",
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

_source line 273 · 2026-05-15T20:21:39.928Z_

<details><summary>↩ Tool result · `toolu_01RGzqRHVgLYxZHJd4Tm2Rrq`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6621ce\", \"name\": \"Citation Attribution Audit\", \"type\": \"report\", \"description\": \"CoRL 2026 论文全量引用方法归因审计。27个引用验证结果：7 INCORRECT, 5 NEEDS_REVIEW, 15 CORRECT。含具体修改建议。\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/citation_attribution_audit.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:21:39.672457+00:00\", \"tags\": [\"paper\", \"citation-audit\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "eb0eea7f-d14f-4eb5-94b8-d50187800551",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260515_6621ce\\\", \\\"name\\\": \\\"Citation Attribution Audit\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"CoRL 2026 论文全量引用方法归因审计。27个引用验证结果：7 INCORRECT, 5 NEEDS_REVIEW, 15 CORRECT。含具体修改建议。\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/citation_attribution_audit.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-15T20:21:39.672457+00:00\\\", \\\"tags\\\": [\\\"paper\\\", \\\"citation-audit\\\", \\\"pre-submission\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260515_6621ce\", \"name\": \"Citation Attribution Audit\", \"type\": \"report\", \"description\": \"CoRL 2026 论文全量引用方法归因审计。27个引用验证结果：7 INCORRECT, 5 NEEDS_REVIEW, 15 CORRECT。含具体修改建议。\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/citation_attribution_audit.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-15T20:21:39.672457+00:00\", \"tags\": [\"paper\", \"citation-audit\", \"pre-submission\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 274_

审计完成。报告已写入 `artifacts/citation_attribution_audit.md` 并注册。

## 结果摘要

**27 引用中：7 INCORRECT / 5 NEEDS_REVIEW / 15 CORRECT**

### 最严重的问题（Blocking）

| 引用 | 错误性质 |
|---|---|
| **chen2026reconvla** | 核心机制完全错误——论文说"多样本选择"，实际是 CQR 单流不确定性量化。三个章节都有 |
| **a2c2_2025** | 训练方式说反了——论文说"jointly with VLA"，实际 base VLA 是 frozen 的 |
| **silver2018residual** | "bounded corrections" 不存在于原文，只有 zero-initialization |
| **digflow2025** | "regularizes denoising trajectory" 错误——实际是 representation-level gating |
| **pan2025drc** | decay 机制描述完全错误（不是 episode-level 衰减） |
| **zhou2025acp_cbf** | bib 作者错误 (Zetian Zhou → Hao Zhou) |
| **zollo2025vla_calibration** | bib 作者名错误 (Matteo → Thomas) |

chen2026reconvla 和 a2c2_2025 是最高优先级修正项，因为它们影响论文的 positioning 叙事。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "uuid": "99f9107f-4987-4254-91f8-3a279d113c08",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YbHNy34gRW6QH6oiBec2ts",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 582,
      "cache_read_input_tokens": 66742,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 582
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

_source line 275_

审计完成。报告已写入 `artifacts/citation_attribution_audit.md` 并注册。

## 结果摘要

**27 引用中：7 INCORRECT / 5 NEEDS_REVIEW / 15 CORRECT**

### 最严重的问题（Blocking）

| 引用 | 错误性质 |
|---|---|
| **chen2026reconvla** | 核心机制完全错误——论文说"多样本选择"，实际是 CQR 单流不确定性量化。三个章节都有 |
| **a2c2_2025** | 训练方式说反了——论文说"jointly with VLA"，实际 base VLA 是 frozen 的 |
| **silver2018residual** | "bounded corrections" 不存在于原文，只有 zero-initialization |
| **digflow2025** | "regularizes denoising trajectory" 错误——实际是 representation-level gating |
| **pan2025drc** | decay 机制描述完全错误（不是 episode-level 衰减） |
| **zhou2025acp_cbf** | bib 作者错误 (Zetian Zhou → Hao Zhou) |
| **zollo2025vla_calibration** | bib 作者名错误 (Matteo → Thomas) |

chen2026reconvla 和 a2c2_2025 是最高优先级修正项，因为它们影响论文的 positioning 叙事。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 371941,
  "duration_api_ms": 1023304,
  "num_turns": 19,
  "stop_reason": "end_turn",
  "session_id": "ed0d2f5e-153b-4103-85df-4943ad37c09e",
  "total_cost_usd": 3.4912637999999987,
  "usage": {
    "input_tokens": 19,
    "cache_creation_input_tokens": 55483,
    "cache_read_input_tokens": 447844,
    "output_tokens": 13865,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 55483,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 401,
        "cache_read_input_tokens": 66742,
        "cache_creation_input_tokens": 582,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 582
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 984085,
      "outputTokens": 27482,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 63,
      "costUSD": 1.7514949999999994,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 19,
      "outputTokens": 13865,
      "cacheReadInputTokens": 447844,
      "cacheCreationInputTokens": 55483,
      "webSearchRequests": 0,
      "costUSD": 0.9174107499999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    },
    "claude-sonnet-4-6": {
      "inputTokens": 12971,
      "outputTokens": 14068,
      "cacheReadInputTokens": 599146,
      "cacheCreationInputTokens": 104715,
      "webSearchRequests": 0,
      "costUSD": 0.82235805,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "a2de5a6c-8812-4acd-a4e6-07cbd39ae6fa"
}
```

</details>

---
