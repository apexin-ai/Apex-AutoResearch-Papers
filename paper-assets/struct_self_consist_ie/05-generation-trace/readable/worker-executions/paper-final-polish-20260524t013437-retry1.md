# paper final polish 20260524T013437 retry1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 180
- **Recorded user turns:** 0
- **Tool calls:** 71
- **Original source:** `logs/workers/worker_paper_final-polish_20260524T013437_retry1.log`
- **Structured JSON:** [`59eb9d7663451e736367.json`](../../sessions/59/59eb9d7663451e736367.json)

## Before a recorded user message

180 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
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
  "model": "claude-opus-4-7[1m]",
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
  "uuid": "812e82b6-dc4c-48b4-9cd5-177d0d39c4c4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1779598800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "d6a21684-cd37-4f64-b210-bdd7ccaee7e9",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "437e5c5f-7104-42c4-8207-558b2a83dbd4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XhDypgpASDZkkngU3RgoPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16795,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16795
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

_source line 5_

<details open><summary>🔧 Tool call — Bash · `toolu_01CbeHgmSjqhMLNP32JrxRTp`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/",
  "description": "List paper directory contents"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c45f225a-65c1-4c3b-b5f4-22f76d35ddc1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XhDypgpASDZkkngU3RgoPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16795,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16795
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

_source line 6 · 2026-05-24T01:34:58.116Z_

<details><summary>↩ Tool result · `toolu_01CbeHgmSjqhMLNP32JrxRTp`</summary>

```text
_pdf_images
acl.sty
acl_natbib.bst
figures
main.aux
main.bbl
main.blg
main.fdb_latexmk
main.fls
main.log
main.out
main.pdf
main.tex
references.bib
references.bib.backup
sections
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "900f6b99-4991-4615-b62a-f9d9cb4ffa9b",
  "tool_use_result": {
    "stdout": "_pdf_images\nacl.sty\nacl_natbib.bst\nfigures\nmain.aux\nmain.bbl\nmain.blg\nmain.fdb_latexmk\nmain.fls\nmain.log\nmain.out\nmain.pdf\nmain.tex\nreferences.bib\nreferences.bib.backup\nsections",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01LVcNzEHVUfqGzFQCwFxPNs`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/",
  "description": "List sections directory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "f9613639-9f0d-4bb4-8013-059f791d9ce1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01XhDypgpASDZkkngU3RgoPZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 16795,
      "cache_read_input_tokens": 16241,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 16795
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

_source line 8 · 2026-05-24T01:34:58.685Z_

<details><summary>↩ Tool result · `toolu_01LVcNzEHVUfqGzFQCwFxPNs`</summary>

```text
_archived
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments_main.tex
introduction.tex
limitations.tex
mechanistic.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "14bfab5f-1bc4-40e5-8e97-ef048a8da8ae",
  "tool_use_result": {
    "stdout": "_archived\nabstract.tex\nadaptive.tex\nappendix.tex\nbackground.tex\nchecklist.tex\nconclusion.tex\ndiagnostic.tex\ndiscussion.tex\nexperiments_main.tex\nintroduction.tex\nlimitations.tex\nmechanistic.tex\nmethod.tex\nrelated_work.tex\nsingle_signal.tex\ntheoretical.tex\ntheory.tex",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01LrpkxTn5AYNQeFqT6ona8m`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper && pdflatex -interaction=nonstopmode main.tex > /tmp/compile1.log 2>&1 && bibtex main > /tmp/bibtex.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile2.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile3.log 2>&1; echo \"Compilation done. Exit: $?\"",
  "description": "Compile paper with pdflatex+bibtex chain"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "82bf3b6c-6ab6-442a-9809-d6b8f17d631b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MH8SYTjV4sPWsWQwCceYQe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 593,
      "cache_read_input_tokens": 33036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 593
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

### System

_source line 10_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "b3fw4a11c",
  "tool_use_id": "toolu_01LrpkxTn5AYNQeFqT6ona8m",
  "description": "Compile paper with pdflatex+bibtex chain",
  "task_type": "local_bash",
  "uuid": "40267401-7b26-47a5-a138-c5dbcdc11723",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### System

_source line 11_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "b3fw4a11c",
  "tool_use_id": "toolu_01LrpkxTn5AYNQeFqT6ona8m",
  "status": "completed",
  "output_file": "",
  "summary": "Compile paper with pdflatex+bibtex chain",
  "uuid": "dc5762d4-eb07-4785-8164-26988865645e",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### Tool result

_source line 12 · 2026-05-24T01:35:10.511Z_

<details><summary>↩ Tool result · `toolu_01LrpkxTn5AYNQeFqT6ona8m`</summary>

```text
Compilation done. Exit: 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1bf74e53-e181-461d-ba36-a2457b4a91a4",
  "tool_use_result": {
    "stdout": "Compilation done. Exit: 0",
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

_source line 13_

<details open><summary>🔧 Tool call — Bash · `toolu_015CFHvZedMRXLQ1rUZ9hNvc`</summary>

```json
{
  "command": "echo \"=== Errors ===\" && grep -i \"^!\" main.log | head -20 && echo \"=== Undefined refs ===\" && grep -i \"undefined\" main.log | head -20 && echo \"=== bib warnings ===\" && grep -i \"warning\" main.blg | head -20",
  "description": "Check compilation status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "82c599cc-790d-46b6-a16f-0766d67ae7da",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01HwNAJgfsVXRRT8s8SUTdNS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 328,
      "cache_read_input_tokens": 33629,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 328
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

_source line 14 · 2026-05-24T01:35:14.372Z_

<details><summary>↩ Tool result · `toolu_015CFHvZedMRXLQ1rUZ9hNvc`</summary>

```text
=== Errors ===
=== Undefined refs ===
=== bib warnings ===
warning$ -- 0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "195365a6-df25-4e04-b568-43a739657cd2",
  "tool_use_result": {
    "stdout": "=== Errors ===\n=== Undefined refs ===\n=== bib warnings ===\nwarning$ -- 0",
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

_source line 15_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "625e9fc8-388c-4514-bc90-dd4fc6e357e7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JcSwULcLzWEJfVCEYDnUr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Grep · `toolu_014igfX3eqepURqMkesE8vGP`</summary>

```json
{
  "pattern": "^!",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "f63b16a2-3dce-4e50-81b3-e50a5b8d9563",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JcSwULcLzWEJfVCEYDnUr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 17 · 2026-05-24T01:35:18.199Z_

<details><summary>↩ Tool result · `toolu_014igfX3eqepURqMkesE8vGP`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b82e341c-4e06-498c-93f7-e60fde374335",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 18_

<details open><summary>🔧 Tool call — Grep · `toolu_01FFUX6tbD6oXvModeN6S3KT`</summary>

```json
{
  "pattern": "[Uu]ndefined|[Mm]issing|[Ee]rror",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": 30
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "389b196e-7fcd-482d-9b54-a2d9ddc73555",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JcSwULcLzWEJfVCEYDnUr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 19 · 2026-05-24T01:35:19.903Z_

<details><summary>↩ Tool result · `toolu_01FFUX6tbD6oXvModeN6S3KT`</summary>

```text
150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
1277:\T1/ptm/m/n/10.95 (+20) with the correlated-error mech-a-nism: more
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "eb920fdc-186c-4994-9616-a7365b5254bc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)\n1277:\\T1/ptm/m/n/10.95 (+20) with the correlated-error mech-a-nism: more",
    "numLines": 2
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_017yQqXLpAApC3DdXTye9TKR`</summary>

```json
{
  "pattern": "[Ww]arning",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
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
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "eb74f5bb-23ee-40c2-ac80-cf239a2db374",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JcSwULcLzWEJfVCEYDnUr5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 229,
      "cache_read_input_tokens": 33957,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 229
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

_source line 21 · 2026-05-24T01:35:20.984Z_

<details><summary>↩ Tool result · `toolu_017yQqXLpAApC3DdXTye9TKR`</summary>

```text
150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)
929:LaTeX Warning: Float too large for page by 25.58675pt on input line 404.
969:LaTeX Warning: `h' float specifier changed to `ht'.
1030:LaTeX Warning: `h' float specifier changed to `ht'.
1129:LaTeX Warning: `h' float specifier changed to `ht'.
1151:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1155:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1239:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1243:Package hyperref Warning: Token not allowed in a PDF string (Unicode):
1392:LaTeX Warning: `h' float specifier changed to `ht'.
1395:LaTeX Warning: `h' float specifier changed to `ht'.
1398:LaTeX Warning: `h' float specifier changed to `ht'.
1442:LaTeX Warning: `h' float specifier changed to `ht'.
1460:LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "14bfff17-acca-4786-b04a-3c09c7a531de",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "150:Package: infwarerr 2019/12/03 v1.5 Providing info/warning/error messages (HO)\n929:LaTeX Warning: Float too large for page by 25.58675pt on input line 404.\n969:LaTeX Warning: `h' float specifier changed to `ht'.\n1030:LaTeX Warning: `h' float specifier changed to `ht'.\n1129:LaTeX Warning: `h' float specifier changed to `ht'.\n1151:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1155:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1239:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1243:Package hyperref Warning: Token not allowed in a PDF string (Unicode):\n1392:LaTeX Warning: `h' float specifier changed to `ht'.\n1395:LaTeX Warning: `h' float specifier changed to `ht'.\n1398:LaTeX Warning: `h' float specifier changed to `ht'.\n1442:LaTeX Warning: `h' float specifier changed to `ht'.\n1460:LaTeX Warning: `h' float specifier changed to `ht'.",
    "numLines": 14
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — Bash · `toolu_01Aj2N9dFvDYXJyo1hteJy3a`</summary>

```json
{
  "command": "pdfinfo main.pdf 2>/dev/null | grep -i pages",
  "description": "Get PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "39781f72-3710-4eee-ba16-d56f2f33993d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BYDKLGXCky6RqpBhuRFcUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 34186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
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

_source line 23 · 2026-05-24T01:35:23.955Z_

<details><summary>↩ Tool result · `toolu_01Aj2N9dFvDYXJyo1hteJy3a`</summary>

```text
Pages:           46
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a8544225-6643-472f-afe9-64065b8525ed",
  "tool_use_result": {
    "stdout": "Pages:           46",
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

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_016ygzJ8t6afX7vxtWygqRdA`</summary>

```json
{
  "pattern": "Citation.*undefined|Reference.*undefined|LaTeX Warning",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
  "output_mode": "content",
  "head_limit": 80
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "955d0987-9b34-4e61-9722-c42b4777b030",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BYDKLGXCky6RqpBhuRFcUs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1184,
      "cache_read_input_tokens": 34186,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1184
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

_source line 25 · 2026-05-24T01:35:25.283Z_

<details><summary>↩ Tool result · `toolu_016ygzJ8t6afX7vxtWygqRdA`</summary>

```text
929:LaTeX Warning: Float too large for page by 25.58675pt on input line 404.
969:LaTeX Warning: `h' float specifier changed to `ht'.
1030:LaTeX Warning: `h' float specifier changed to `ht'.
1129:LaTeX Warning: `h' float specifier changed to `ht'.
1392:LaTeX Warning: `h' float specifier changed to `ht'.
1395:LaTeX Warning: `h' float specifier changed to `ht'.
1398:LaTeX Warning: `h' float specifier changed to `ht'.
1442:LaTeX Warning: `h' float specifier changed to `ht'.
1460:LaTeX Warning: `h' float specifier changed to `ht'.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "75ef51e5-ce24-4bcc-8c31-e1c294c0133e",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "929:LaTeX Warning: Float too large for page by 25.58675pt on input line 404.\n969:LaTeX Warning: `h' float specifier changed to `ht'.\n1030:LaTeX Warning: `h' float specifier changed to `ht'.\n1129:LaTeX Warning: `h' float specifier changed to `ht'.\n1392:LaTeX Warning: `h' float specifier changed to `ht'.\n1395:LaTeX Warning: `h' float specifier changed to `ht'.\n1398:LaTeX Warning: `h' float specifier changed to `ht'.\n1442:LaTeX Warning: `h' float specifier changed to `ht'.\n1460:LaTeX Warning: `h' float specifier changed to `ht'.",
    "numLines": 9
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "91e2ded1-e789-4dad-a1ac-32c67ba3f4e8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017ejvegB18S4Z4LMvcCLB6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 629
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 27_

<details open><summary>🔧 Tool call — Read · `toolu_01NqTfxUx1CJCXLojffTZB4H`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "36dd24e8-ef7d-4cca-97e4-501cfbb8a75c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017ejvegB18S4Z4LMvcCLB6Y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 35370,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 629
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 28 · 2026-05-24T01:35:29.388Z_

<details><summary>↩ Tool result · `toolu_01NqTfxUx1CJCXLojffTZB4H`</summary>

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
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{amsthm}
16	\newtheorem{proposition}{Proposition}
17	\newtheorem{theorem}{Theorem}
18	\newtheorem{corollary}{Corollary}
19	\newtheorem{definition}{Definition}
20	\usepackage{multirow}
21	\usepackage{xcolor}
22	\usepackage{subcaption}
23	\usepackage{alphalph}
24	\usepackage{enumitem}
25	
26	\graphicspath{{figures/}}
27	
28	\title{When Self-Consistency Fails for NER:\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}
29	
30	\author{Anonymous}
31	
32	\begin{document}
33	\maketitle
34	
35	\input{sections/abstract}
36	\input{sections/introduction}
37	\input{sections/background}
38	\input{sections/diagnostic}
39	\input{sections/single_signal}
40	\input{sections/adaptive}
41	\input{sections/theory}
42	\input{sections/experiments_main}
43	
44	\section*{Limitations}
45	\input{sections/limitations}
46	
47	\bibliography{references}
48	
49	\appendix
50	\renewcommand{\thesection}{\alphalph{\value{section}}}
51	\input{sections/appendix}
52	
53	\end{document}
54	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "9747c2ef-7a81-4e1c-84ac-d9a5234a2f1c",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{amsthm}\n\\newtheorem{proposition}{Proposition}\n\\newtheorem{theorem}{Theorem}\n\\newtheorem{corollary}{Corollary}\n\\newtheorem{definition}{Definition}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\\usepackage{alphalph}\n\\usepackage{enumitem}\n\n\\graphicspath{{figures/}}\n\n\\title{When Self-Consistency Fails for NER:\\\\ Degeneracy, Signal Collapse, and the Correlation-Selection Gap}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/background}\n\\input{sections/diagnostic}\n\\input{sections/single_signal}\n\\input{sections/adaptive}\n\\input{sections/theory}\n\\input{sections/experiments_main}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\bibliography{references}\n\n\\appendix\n\\renewcommand{\\thesection}{\\alphalph{\\value{section}}}\n\\input{sections/appendix}\n\n\\end{document}\n",
      "numLines": 54,
      "startLine": 1,
      "totalLines": 54
    }
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016fzzqVADfYT2H44gNAAmer`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "052571cd-7300-40d6-aab2-1d751c474df2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014L7Qnz8wqns7L724uHn74B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1012,
      "cache_read_input_tokens": 35999,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1012
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

_source line 30 · 2026-05-24T01:35:31.717Z_

<details><summary>↩ Tool result · `toolu_016fzzqVADfYT2H44gNAAmer`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "703570cd-33ce-4420-9971-752c5e9db381",
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

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01SwRFNpSnNW34UaFnm7vDx2`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "in_progress"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "pending"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "pending"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "pending"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "pending"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "pending"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "pending"
    },
    {
      "content": "Sync to anonymous repo if changes were made",
      "activeForm": "Syncing to anonymous repo",
      "status": "pending"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "6d3195f6-198a-4ac3-aa47-177eb2f1688d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014iXafTy7LVpuLMQKq476Pe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 24282,
      "cache_read_input_tokens": 16334,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 24282
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "tools_changed",
        "cache_missed_input_tokens": 33090
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-24T01:35:39.613Z_

<details><summary>↩ Tool result · `toolu_01SwRFNpSnNW34UaFnm7vDx2`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a114b5fb-984c-4cbb-853b-6298beeaad8c",
  "tool_use_result": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "in_progress",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "pending",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Check abstract word count",
        "status": "pending",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "pending",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a4265dbd-e014-4ea4-a869-4ac042486bc6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Dv6qDfwYdDgyuUw8Ksd77x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01FpUSy36CVZqZYr6zGVWeKH`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -n -E \"(^Limitations|^References|^A\\.[0-9]|Appendix)\" | head -20",
  "description": "Find Limitations location in PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "326efc00-4568-44d5-a43f-054318bd5df6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Dv6qDfwYdDgyuUw8Ksd77x",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 504,
      "cache_read_input_tokens": 40616,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 504
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

_source line 35 · 2026-05-24T01:35:45.432Z_

<details><summary>↩ Tool result · `toolu_01FpUSy36CVZqZYr6zGVWeKH`</summary>

```text
29:015       occurring conditions—degeneracy (i.e., mul-              nally (AUROC 0.63–0.88; Appendix i), exposing                    057
49:030       inference.                                               a distinct bottleneck (40% zero-F1; Appendix q).                 070
103:100         ≈ 0.50; Appendix i).                                      ure into degeneracy and LP compression; (3) pre-                                                                140
157:      rather than relation classification failure (Appendix q).       (entity sets with partial overlap); (b) failure mech-                                                           173
230:192   (x, yi ) → R scores each output independently;                                                      F1 points; Appendix o.1).                                                            222
240:200   tural signals receiving zero weight (Appendix h).
259:237   present/absent labels (Appendix b). VC: mean en-
280:      (Appendix d).                                                                      0.3                            .294
308:262   is structural: four of five signals are instance-level                  range below 0.041 nats (Appendix o), leaving in-                                                       272
316:266   within an instance—selection failure is a design                        instance std ratio 0.97×; Appendix s). Even where                                                      276
333:      Appendix ad); we use constant-F1 as the operationally rele-
339:288   2–3 seeds; Appendix e). All selection experi-               Table 3: Summary of 9 method categories tested (in-
341:                                                                  semble beyond self-verification methods in Appendix i
342:290   reported in Appendix e. The pattern holds across
344:291   CoNLL and WNUT-17 (Table 11). Few-NERD                      dataset in parentheses. Full coverage in Appendix h.4.
371:311   Mechanistic evidence (Appendix i). Why does                 and LLaMA-3.1-8B (Few-NERD) yields +0.42 pp                               343
385:318   0.55; Appendix k), yet cross-dataset transfer drops
392:325   nal alignment collapse observed across all config-          Appendix h.2), as feature importance shifts across                        356
395:328   0.50–0.55; Appendix k), suggesting the introspec-
403:333   gains (§4), we present exploratory attempts in-             sition 1; Table 65; Appendix r.1). Signal-derived                         364
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c7d531f6-bf43-4539-92e1-69d141335cd4",
  "tool_use_result": {
    "stdout": "29:015       occurring conditions—degeneracy (i.e., mul-              nally (AUROC 0.63–0.88; Appendix i), exposing                    057\n49:030       inference.                                               a distinct bottleneck (40% zero-F1; Appendix q).                 070\n103:100         ≈ 0.50; Appendix i).                                      ure into degeneracy and LP compression; (3) pre-                                                                140\n157:      rather than relation classification failure (Appendix q).       (entity sets with partial overlap); (b) failure mech-                                                           173\n230:192   (x, yi ) → R scores each output independently;                                                      F1 points; Appendix o.1).                                                            222\n240:200   tural signals receiving zero weight (Appendix h).\n259:237   present/absent labels (Appendix b). VC: mean en-\n280:      (Appendix d).                                                                      0.3                            .294\n308:262   is structural: four of five signals are instance-level                  range below 0.041 nats (Appendix o), leaving in-                                                       272\n316:266   within an instance—selection failure is a design                        instance std ratio 0.97×; Appendix s). Even where                                                      276\n333:      Appendix ad); we use constant-F1 as the operationally rele-\n339:\f288   2–3 seeds; Appendix e). All selection experi-               Table 3: Summary of 9 method categories tested (in-\n341:                                                                  semble beyond self-verification methods in Appendix i\n342:290   reported in Appendix e. The pattern holds across\n344:291   CoNLL and WNUT-17 (Table 11). Few-NERD                      dataset in parentheses. Full coverage in Appendix h.4.\n371:311   Mechanistic evidence (Appendix i). Why does                 and LLaMA-3.1-8B (Few-NERD) yields +0.42 pp                               343\n385:318   0.55; Appendix k), yet cross-dataset transfer drops\n392:325   nal alignment collapse observed across all config-          Appendix h.2), as feature importance shifts across                        356\n395:328   0.50–0.55; Appendix k), suggesting the introspec-\n403:333   gains (§4), we present exploratory attempts in-             sition 1; Table 65; Appendix r.1). Signal-derived                         364",
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

_source line 36_

<details open><summary>🔧 Tool call — Bash · `toolu_012c3Zjqi7fPdrppHbM7fxp2`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - | grep -n -E \"^[[:space:]]*Limitations|^Limitations|^[[:space:]]*References\" | head",
  "description": "Find Limitations heading"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "ac36bc39-09ff-4c87-a3c4-6fc6010b4a92",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KzZYysESiR4A2qHisYiL5z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 983,
      "cache_read_input_tokens": 41120,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 983
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

_source line 37 · 2026-05-24T01:35:48.603Z_

<details><summary>↩ Tool result · `toolu_012c3Zjqi7fPdrppHbM7fxp2`</summary>

```text
678:                                                                                                                                 Limitations                                                 556
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1dadd0d1-f13f-42bb-b0c2-e94c9c536994",
  "tool_use_result": {
    "stdout": "678:                                                                                                                                 Limitations                                                 556",
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

_source line 38_

<details open><summary>🔧 Tool call — Bash · `toolu_01MsboCHnBJWUgVE1YzJeqMa`</summary>

```json
{
  "command": "pdftotext -layout main.pdf /tmp/main.txt && head -800 /tmp/main.txt | tail -150",
  "description": "Extract end of main text area"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "78667012-08c6-49d1-b83d-f90038f808c9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013RCZgyqRa1gBqLyG5VSuAJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 177,
      "cache_read_input_tokens": 42103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 177
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

_source line 39 · 2026-05-24T01:35:52.113Z_

<details><summary>↩ Tool result · `toolu_01MsboCHnBJWUgVE1YzJeqMa`</summary>

```text
                                                                                         Spearman = 0.052 (p = 0.8141)
                                                                                                     n = 23 conditions           Discussion and conclusion. For discrete-answer              538
                                                  20                 40            60                    80                      reasoning, sample diversity reflects diverse reason-        539
                                                                   Degeneracy Rate (%)
                                                                                                                                 ing paths; for NER, degeneracy (12–68%) reduces             540
      Figure 6: Instance degeneracy vs. LP selection gain                                                                        candidate diversity while signal alignment collapse         541
      across 23 configurations (N =8; ρ=0.052, p=0.81).                                                                          (α→0) limits ranking. The degeneracy decom-                 542
      Within Few-NERD per-entity-type (ρ=−0.881; Ap-                                                                             position (§6.3) identifies α—not degeneracy—as              543
      pendix ab), degeneracy predicts LP gain when align-
                                                                                                                                 the binding constraint (8–33× tighter); this per-           544
      ment is held constant.
                                                                                                                                 sists across families (Yun et al., 2025), scales (4B–       545
                                                                                                                                 72B), and decoding modes (Appendix s). The diag-            546
509   ure mode—diversity among failures rather than                                                                              nostic framework—identifying these co-occurring             547
510   quality-differentiated outputs—despite comparable                                                                          conditions—is our primary contribution; pretrained          548
511   degeneracy (10.1% vs. SciERC NER 12.2%; Ap-                                                                                Qwen2.5-7B at N =32 achieves +3.85 pp MV gain               549
512   pendix q).                                                                                                                 where the framework predicts favorable conditions           550
                                                                                                                                 (D=5.4%; Appendix u). At N =8, high degener-                551
513   7.4                          Robustness                                                                                    acy (> 50%) suggests scaling will not help; low de-         552

514   Signal rankings are robust across temperatures,                                                                            generacy with strong LP-F1 alignment may warrant            553

515   seeds, and N (Table 7; Appendix c); Qwen3-4B                                                                               exploratory entity construction; otherwise, greedy          554

516   QE matches 8B (|∆ρ|=0.042). The gap persists                                                                               decoding remains the default.                               555

517   from 4B to 72B zero-shot to GPT-5.5 (§6.2).
                                                                                                                                 Limitations                                                 556

518   7.5                          Entity Construction (Exploratory)                                                             Our primary evidence is from English NER with               557

519   Entity-level construction. We aggregate enti-                                                                              fine-tuned 7–14B open-weight models; frontier               558

520   ties across samples, retaining those exceeding                                                                                 7
                                                                                                                                      Degenerate instances contribute ∆=0 by construction;
521   θ=2/N with LP-weighted scoring (θ stable in                                                                                all gains concentrate in the non-degenerate subset.


                                                                                                                             8
559   models exhibit markedly different degeneracy pro-               Neural Information Processing Systems, volume 24,       613
560   files (5.5–74%; Table 48), and cross-task exten-                pages 1404–1412.                                        614

561   sions (RE n=397, SQL n=196) are exploratory.
                                                                    Leon Derczynski, Eric Nichols, Marieke van Erp, and       615
562   The framework is diagnostic, not causal: under                  Nut Limsopatham. 2017. Results of the wnut2017          616
563   global Holm–Bonferroni (k=57), the strongest con-               shared task on novel and emerging entity recognition.   617
564   struction claim reaches padj =0.055; our negative               In Proceedings of the 3rd Workshop on Noisy User-       618
565   selection claims are bounded by statistical power               generated Text (W-NUT 2017).                            619

566   (2–3 seeds, MDE ≈1.5 pp). Entity-level construc-              Shrey Desai and Greg Durrett. 2020. Calibration of        620
567   tion requires N × inference cost for modest gains               pre-trained transformers. In Proceedings of the 2020    621
568   (+1–1.4 pp), and we use a single prompt template                Conference on Empirical Methods in Natural Lan-         622
569   per task.                                                       guage Processing (EMNLP), pages 295–302.                623

                                                                    Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang,         624
                                                                      Xu Han, Pengjun Xie, Hai-Tao Zheng, and Zhiyuan         625
570   References                                                      Liu. 2021. Few-NERD: A few-shot named entity            626
571   Pranjal Aggarwal, Aman Madaan, Yiming Yang, and                 recognition dataset. In Proceedings of the 59th An-     627
572     Mausam. 2023. Let’s sample step by step: Adaptive-            nual Meeting of the Association for Computational       628
573     consistency for efficient reasoning and coding with           Linguistics and the 11th International Joint Confer-    629
574     LLMs. In Proceedings of the 2023 Conference on                ence on Natural Language Processing (Volume 1:          630
575     Empirical Methods in Natural Language Processing              Long Papers), pages 3198–3213.                          631
576     (EMNLP 2023).
                                                                    Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang          632
577   Anastasios N. Angelopoulos and Stephen Bates. 2023.             Lai, Ziyi Xu, Yilong Zhao, and Tianqi Chen. 2024.       633
578     Conformal prediction: A gentle introduction. Foun-            XGrammar: Flexible and efficient structured genera-     634
579     dations and Trends in Machine Learning, 16(4):494–            tion engine for large language models. arXiv preprint   635
580     591.                                                          arXiv:2411.15100.                                       636

581   Taylor Berg-Kirkpatrick, David Burkett, and Dan Klein.        Bryan Eikema and Wilker Aziz. 2020. Is MAP decod-         637
582     2012. An empirical investigation of statistical sig-          ing all you need? The inadequacy of the mode in         638
583     nificance in NLP. In Proceedings of the 2012 Joint            neural machine translation. In Proceedings of the       639
584     Conference on Empirical Methods in Natural Lan-               28th International Conference on Computational Lin-     640
585     guage Processing and Computational Natural Lan-               guistics (COLING), pages 4506–4520.                     641
586     guage Learning (EMNLP-CoNLL), pages 995–1005.
587     Association for Computational Linguistics.                  Bryan Eikema and Wilker Aziz. 2022. Sampling-based        642
588   Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald            approximations to minimum Bayes risk decoding for       643
589     Clark, Quoc V. Le, Christopher Ré, and Azalia Mirho-          neural machine translation. In Proceedings of the       644
590     seini. 2024. Large language monkeys: Scaling infer-           2022 Conference on Empirical Methods in Natural         645
591     ence compute with repeated sampling. arXiv preprint           Language Processing, pages 10978–10993.                 646
592     arXiv:2407.21787.
                                                                    Bryan Eikema, Anna Rutkiewicz, and Mario Giulianelli.     647
593   Angelica Chen, Jason Phang, Alicia Parrish, Vishakh             2025. Structure-conditional minimum Bayes risk          648
594     Padmakumar, Chen Zhao, Samuel R. Bowman, and                  decoding. In Proceedings of the 2025 Conference on      649
595     Kyunghyun Cho. 2024a. Two failures of self-                   Empirical Methods in Natural Language Processing.       650
596     consistency in the multi-step reasoning of LLMs.
597     Transactions on Machine Learning Research.                  Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, and       651
                                                                      Yarin Gal. 2024. Detecting hallucinations in large      652
598   Xinyun Chen, Renat Aksitov, Uri Alon, Jie Ren, Kefan            language models using semantic entropy. Nature,         653
599     Xiao, Pengcheng Yin, Sushant Prakash, Charles Sut-            630:625–630.                                            654
600     ton, Xuezhi Wang, and Denny Zhou. 2024b. Univer-
601     sal self-consistency for large language model genera-       Joseph L. Fleiss. 1971. Measuring nominal scale agree-    655
602     tion. In ICML 2024 Workshop on In-Context Learn-               ment among many raters. Psychological Bulletin.        656
603     ing.
604   Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,               Markus Freitag, David Grangier, Qijun Tan, and Bowen      657
605     Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias                Liang. 2022. High quality rather than high model        658
606     Plappert, Jerry Tworek, Jacob Hilton, Reiichiro               probability: Minimum Bayes risk decoding with neu-      659
607     Nakano, Christopher Hesse, and John Schulman.                 ral metrics. Transactions of the Association for Com-   660
608     2021. Training verifiers to solve math word prob-             putational Linguistics, 10:811–825.                     661
609     lems. arXiv preprint arXiv:2110.14168.
                                                                    Leo Gao, John Schulman, and Jacob Hilton. 2023. Scal-     662
610   Krzysztof J. Dembczyński, Willem Waegeman, Weiwei              ing laws for reward model overoptimization. In Pro-     663
611     Cheng, and Eyke Hüllermeier. 2011. An exact algo-             ceedings of the 40th International Conference on        664
612     rithm for F-measure maximization. In Advances in              Machine Learning (ICML).                                665


                                                                9
666   Yonatan Geifman and Ran El-Yaniv. 2017. Selec-                  Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen,       720
667     tive classification for deep neural networks. In Ad-            Jian-Guang Lou, and Weizhu Chen. 2023. Making              721
668     vances in Neural Information Processing Systems,                 large language models better reasoners with step-         722
669     volume 30.                                                       aware verifier. In Proceedings of the 61st Annual         723
                                                                        Meeting of the Association for Computational Lin-          724
670   Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Wein-               guistics (ACL).                                           725
671     berger. 2017. On calibration of modern neural net-
672     works. In Proceedings of the 34th International Con-          Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri          726
673     ference on Machine Learning, pages 1321–1330.                   Edwards, Bowen Baker, Teddy Lee, Jan Leike, John           727
                                                                        Schulman, Ilya Sutskever, and Karl Cobbe. 2024.            728
674   Sture Holm. 1979. A simple sequentially rejective mul-            Let’s verify step by step. In Proceedings of the           729
675      tiple test procedure. Scandinavian Journal of Statis-          Twelfth International Conference on Learning Repre-        730
676      tics, 6(2):65–70.                                              sentations (ICLR 2024).                                    731


677   Jie Huang, Xinyun Chen, Swaroop Mishra,                         Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.          732
678      Huaixiu Steven Zheng, Adams Wei Yu, Xiny-                      Teaching models to express their uncertainty in            733
679      ing Song, and Denny Zhou. 2024. Large language                 words. Transactions on Machine Learning Research.          734
680      models cannot self-correct reasoning yet.        In          Yi Luan, Luheng He, Mari Ostendorf, and Hannaneh             735
681      Proceedings of the Twelfth International Conference            Hajishirzi. 2018. Multi-task identification of entities,   736
682      on Learning Representations (ICLR).                            relations, and coreference for scientific knowledge        737
                                                                        graph construction. In Proceedings of the 2018 Con-        738
683   Yuu Jinnai, Tetsuro Morimura, Ukyo Honda, Kaito                   ference on Empirical Methods in Natural Language           739
684     Ariu, and Kenshi Abe. 2024. Model-based mini-                   Processing.                                                740
685     mum Bayes risk decoding for text generation. In
686     Proceedings of the 41st International Conference on           Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler             741
687     Machine Learning (ICML).                                       Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,              742
                                                                       Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,               743
688   Saurav Kadavath, Tom Conerly, Amanda Askell, Tom                 Shashank Gupta, Bodhisattwa Prasad Majumder,                744
689     Henighan, Dawn Drain, Ethan Perez, Nicholas                    Katherine Hermann, Sean Welleck, Amir Yazdan-               745
690     Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli               bakhsh, and Peter Clark. 2023. Self-refine: Iterative       746
691     Tran-Johnson, Scott Johnston, Sheer El-Showk,                  refinement with self-feedback. In Advances in Neu-          747
692     Andy Jones, Nelson Elhage, Tristan Hume, Anna                  ral Information Processing Systems, volume 36.              748
693     Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, and
694     17 others. 2022. Language models (mostly) know                Andrey Malinin and Mark Gales. 2021. Uncertainty             749
695     what they know. arXiv preprint arXiv:2207.05221.                estimation in autoregressive structured prediction. In     750
                                                                        Proceedings of the Ninth International Conference          751
696   Zhewei Kang, Xuandong Zhao, and Dawn Song. 2025.                  on Learning Representations.                               752
697     Scalable best-of-n selection for large language mod-
698     els via self-certainty. In Advances in Neural Infor-          Niklas Muennighoff, Zitong Yang, Weijia Shi, Xi-             753
699     mation Processing Systems 38 (NeurIPS).                         ang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke         754
                                                                        Zettlemoyer, Percy Liang, Emmanuel Candès, and             755
700   Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. 2023.             Tatsunori Hashimoto. 2025. s1: Simple test-time            756
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "210115db-c3d0-49b8-9ca2-77ec15a6964a",
  "tool_use_result": {
    "stdout": "                                                                                         Spearman = 0.052 (p = 0.8141)\n                                                                                                     n = 23 conditions           Discussion and conclusion. For discrete-answer              538\n                                                  20                 40            60                    80                      reasoning, sample diversity reflects diverse reason-        539\n                                                                   Degeneracy Rate (%)\n                                                                                                                                 ing paths; for NER, degeneracy (12–68%) reduces             540\n      Figure 6: Instance degeneracy vs. LP selection gain                                                                        candidate diversity while signal alignment collapse         541\n      across 23 configurations (N =8; ρ=0.052, p=0.81).                                                                          (α→0) limits ranking. The degeneracy decom-                 542\n      Within Few-NERD per-entity-type (ρ=−0.881; Ap-                                                                             position (§6.3) identifies α—not degeneracy—as              543\n      pendix ab), degeneracy predicts LP gain when align-\n                                                                                                                                 the binding constraint (8–33× tighter); this per-           544\n      ment is held constant.\n                                                                                                                                 sists across families (Yun et al., 2025), scales (4B–       545\n                                                                                                                                 72B), and decoding modes (Appendix s). The diag-            546\n509   ure mode—diversity among failures rather than                                                                              nostic framework—identifying these co-occurring             547\n510   quality-differentiated outputs—despite comparable                                                                          conditions—is our primary contribution; pretrained          548\n511   degeneracy (10.1% vs. SciERC NER 12.2%; Ap-                                                                                Qwen2.5-7B at N =32 achieves +3.85 pp MV gain               549\n512   pendix q).                                                                                                                 where the framework predicts favorable conditions           550\n                                                                                                                                 (D=5.4%; Appendix u). At N =8, high degener-                551\n513   7.4                          Robustness                                                                                    acy (> 50%) suggests scaling will not help; low de-         552\n\n514   Signal rankings are robust across temperatures,                                                                            generacy with strong LP-F1 alignment may warrant            553\n\n515   seeds, and N (Table 7; Appendix c); Qwen3-4B                                                                               exploratory entity construction; otherwise, greedy          554\n\n516   QE matches 8B (|∆ρ|=0.042). The gap persists                                                                               decoding remains the default.                               555\n\n517   from 4B to 72B zero-shot to GPT-5.5 (§6.2).\n                                                                                                                                 Limitations                                                 556\n\n518   7.5                          Entity Construction (Exploratory)                                                             Our primary evidence is from English NER with               557\n\n519   Entity-level construction. We aggregate enti-                                                                              fine-tuned 7–14B open-weight models; frontier               558\n\n520   ties across samples, retaining those exceeding                                                                                 7\n                                                                                                                                      Degenerate instances contribute ∆=0 by construction;\n521   θ=2/N with LP-weighted scoring (θ stable in                                                                                all gains concentrate in the non-degenerate subset.\n\n\n                                                                                                                             8\n\f559   models exhibit markedly different degeneracy pro-               Neural Information Processing Systems, volume 24,       613\n560   files (5.5–74%; Table 48), and cross-task exten-                pages 1404–1412.                                        614\n\n561   sions (RE n=397, SQL n=196) are exploratory.\n                                                                    Leon Derczynski, Eric Nichols, Marieke van Erp, and       615\n562   The framework is diagnostic, not causal: under                  Nut Limsopatham. 2017. Results of the wnut2017          616\n563   global Holm–Bonferroni (k=57), the strongest con-               shared task on novel and emerging entity recognition.   617\n564   struction claim reaches padj =0.055; our negative               In Proceedings of the 3rd Workshop on Noisy User-       618\n565   selection claims are bounded by statistical power               generated Text (W-NUT 2017).                            619\n\n566   (2–3 seeds, MDE ≈1.5 pp). Entity-level construc-              Shrey Desai and Greg Durrett. 2020. Calibration of        620\n567   tion requires N × inference cost for modest gains               pre-trained transformers. In Proceedings of the 2020    621\n568   (+1–1.4 pp), and we use a single prompt template                Conference on Empirical Methods in Natural Lan-         622\n569   per task.                                                       guage Processing (EMNLP), pages 295–302.                623\n\n                                                                    Ning Ding, Guangwei Xu, Yulin Chen, Xiaobin Wang,         624\n                                                                      Xu Han, Pengjun Xie, Hai-Tao Zheng, and Zhiyuan         625\n570   References                                                      Liu. 2021. Few-NERD: A few-shot named entity            626\n571   Pranjal Aggarwal, Aman Madaan, Yiming Yang, and                 recognition dataset. In Proceedings of the 59th An-     627\n572     Mausam. 2023. Let’s sample step by step: Adaptive-            nual Meeting of the Association for Computational       628\n573     consistency for efficient reasoning and coding with           Linguistics and the 11th International Joint Confer-    629\n574     LLMs. In Proceedings of the 2023 Conference on                ence on Natural Language Processing (Volume 1:          630\n575     Empirical Methods in Natural Language Processing              Long Papers), pages 3198–3213.                          631\n576     (EMNLP 2023).\n                                                                    Yixin Dong, Charlie F. Ruan, Yaxing Cai, Ruihang          632\n577   Anastasios N. Angelopoulos and Stephen Bates. 2023.             Lai, Ziyi Xu, Yilong Zhao, and Tianqi Chen. 2024.       633\n578     Conformal prediction: A gentle introduction. Foun-            XGrammar: Flexible and efficient structured genera-     634\n579     dations and Trends in Machine Learning, 16(4):494–            tion engine for large language models. arXiv preprint   635\n580     591.                                                          arXiv:2411.15100.                                       636\n\n581   Taylor Berg-Kirkpatrick, David Burkett, and Dan Klein.        Bryan Eikema and Wilker Aziz. 2020. Is MAP decod-         637\n582     2012. An empirical investigation of statistical sig-          ing all you need? The inadequacy of the mode in         638\n583     nificance in NLP. In Proceedings of the 2012 Joint            neural machine translation. In Proceedings of the       639\n584     Conference on Empirical Methods in Natural Lan-               28th International Conference on Computational Lin-     640\n585     guage Processing and Computational Natural Lan-               guistics (COLING), pages 4506–4520.                     641\n586     guage Learning (EMNLP-CoNLL), pages 995–1005.\n587     Association for Computational Linguistics.                  Bryan Eikema and Wilker Aziz. 2022. Sampling-based        642\n588   Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald            approximations to minimum Bayes risk decoding for       643\n589     Clark, Quoc V. Le, Christopher Ré, and Azalia Mirho-          neural machine translation. In Proceedings of the       644\n590     seini. 2024. Large language monkeys: Scaling infer-           2022 Conference on Empirical Methods in Natural         645\n591     ence compute with repeated sampling. arXiv preprint           Language Processing, pages 10978–10993.                 646\n592     arXiv:2407.21787.\n                                                                    Bryan Eikema, Anna Rutkiewicz, and Mario Giulianelli.     647\n593   Angelica Chen, Jason Phang, Alicia Parrish, Vishakh             2025. Structure-conditional minimum Bayes risk          648\n594     Padmakumar, Chen Zhao, Samuel R. Bowman, and                  decoding. In Proceedings of the 2025 Conference on      649\n595     Kyunghyun Cho. 2024a. Two failures of self-                   Empirical Methods in Natural Language Processing.       650\n596     consistency in the multi-step reasoning of LLMs.\n597     Transactions on Machine Learning Research.                  Sebastian Farquhar, Jannik Kossen, Lorenz Kuhn, and       651\n                                                                      Yarin Gal. 2024. Detecting hallucinations in large      652\n598   Xinyun Chen, Renat Aksitov, Uri Alon, Jie Ren, Kefan            language models using semantic entropy. Nature,         653\n599     Xiao, Pengcheng Yin, Sushant Prakash, Charles Sut-            630:625–630.                                            654\n600     ton, Xuezhi Wang, and Denny Zhou. 2024b. Univer-\n601     sal self-consistency for large language model genera-       Joseph L. Fleiss. 1971. Measuring nominal scale agree-    655\n602     tion. In ICML 2024 Workshop on In-Context Learn-               ment among many raters. Psychological Bulletin.        656\n603     ing.\n604   Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,               Markus Freitag, David Grangier, Qijun Tan, and Bowen      657\n605     Mark Chen, Heewoo Jun, Lukasz Kaiser, Matthias                Liang. 2022. High quality rather than high model        658\n606     Plappert, Jerry Tworek, Jacob Hilton, Reiichiro               probability: Minimum Bayes risk decoding with neu-      659\n607     Nakano, Christopher Hesse, and John Schulman.                 ral metrics. Transactions of the Association for Com-   660\n608     2021. Training verifiers to solve math word prob-             putational Linguistics, 10:811–825.                     661\n609     lems. arXiv preprint arXiv:2110.14168.\n                                                                    Leo Gao, John Schulman, and Jacob Hilton. 2023. Scal-     662\n610   Krzysztof J. Dembczyński, Willem Waegeman, Weiwei              ing laws for reward model overoptimization. In Pro-     663\n611     Cheng, and Eyke Hüllermeier. 2011. An exact algo-             ceedings of the 40th International Conference on        664\n612     rithm for F-measure maximization. In Advances in              Machine Learning (ICML).                                665\n\n\n                                                                9\n\f666   Yonatan Geifman and Ran El-Yaniv. 2017. Selec-                  Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen,       720\n667     tive classification for deep neural networks. In Ad-            Jian-Guang Lou, and Weizhu Chen. 2023. Making              721\n668     vances in Neural Information Processing Systems,                 large language models better reasoners with step-         722\n669     volume 30.                                                       aware verifier. In Proceedings of the 61st Annual         723\n                                                                        Meeting of the Association for Computational Lin-          724\n670   Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Wein-               guistics (ACL).                                           725\n671     berger. 2017. On calibration of modern neural net-\n672     works. In Proceedings of the 34th International Con-          Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri          726\n673     ference on Machine Learning, pages 1321–1330.                   Edwards, Bowen Baker, Teddy Lee, Jan Leike, John           727\n                                                                        Schulman, Ilya Sutskever, and Karl Cobbe. 2024.            728\n674   Sture Holm. 1979. A simple sequentially rejective mul-            Let’s verify step by step. In Proceedings of the           729\n675      tiple test procedure. Scandinavian Journal of Statis-          Twelfth International Conference on Learning Repre-        730\n676      tics, 6(2):65–70.                                              sentations (ICLR 2024).                                    731\n\n\n677   Jie Huang, Xinyun Chen, Swaroop Mishra,                         Stephanie Lin, Jacob Hilton, and Owain Evans. 2022.          732\n678      Huaixiu Steven Zheng, Adams Wei Yu, Xiny-                      Teaching models to express their uncertainty in            733\n679      ing Song, and Denny Zhou. 2024. Large language                 words. Transactions on Machine Learning Research.          734\n680      models cannot self-correct reasoning yet.        In          Yi Luan, Luheng He, Mari Ostendorf, and Hannaneh             735\n681      Proceedings of the Twelfth International Conference            Hajishirzi. 2018. Multi-task identification of entities,   736\n682      on Learning Representations (ICLR).                            relations, and coreference for scientific knowledge        737\n                                                                        graph construction. In Proceedings of the 2018 Con-        738\n683   Yuu Jinnai, Tetsuro Morimura, Ukyo Honda, Kaito                   ference on Empirical Methods in Natural Language           739\n684     Ariu, and Kenshi Abe. 2024. Model-based mini-                   Processing.                                                740\n685     mum Bayes risk decoding for text generation. In\n686     Proceedings of the 41st International Conference on           Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler             741\n687     Machine Learning (ICML).                                       Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,              742\n                                                                       Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,               743\n688   Saurav Kadavath, Tom Conerly, Amanda Askell, Tom                 Shashank Gupta, Bodhisattwa Prasad Majumder,                744\n689     Henighan, Dawn Drain, Ethan Perez, Nicholas                    Katherine Hermann, Sean Welleck, Amir Yazdan-               745\n690     Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli               bakhsh, and Peter Clark. 2023. Self-refine: Iterative       746\n691     Tran-Johnson, Scott Johnston, Sheer El-Showk,                  refinement with self-feedback. In Advances in Neu-          747\n692     Andy Jones, Nelson Elhage, Tristan Hume, Anna                  ral Information Processing Systems, volume 36.              748\n693     Chen, Yuntao Bai, Sam Bowman, Stanislav Fort, and\n694     17 others. 2022. Language models (mostly) know                Andrey Malinin and Mark Gales. 2021. Uncertainty             749\n695     what they know. arXiv preprint arXiv:2207.05221.                estimation in autoregressive structured prediction. In     750\n                                                                        Proceedings of the Ninth International Conference          751\n696   Zhewei Kang, Xuandong Zhao, and Dawn Song. 2025.                  on Learning Representations.                               752\n697     Scalable best-of-n selection for large language mod-\n698     els via self-certainty. In Advances in Neural Infor-          Niklas Muennighoff, Zitong Yang, Weijia Shi, Xi-             753\n699     mation Processing Systems 38 (NeurIPS).                         ang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke         754\n                                                                        Zettlemoyer, Percy Liang, Emmanuel Candès, and             755\n700   Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. 2023.             Tatsunori Hashimoto. 2025. s1: Simple test-time            756",
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

_source line 40_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "ca7f6f3c-6b6a-4d5f-a043-09135d76aded",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mg9eV5kF84iXVWDf3YKWBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5671,
      "cache_read_input_tokens": 42280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5671
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

_source line 41_

<details open><summary>🔧 Tool call — Bash · `toolu_019AbgKu1b4m3dLwPaULKvXe`</summary>

```json
{
  "command": "grep -c \"Citation.*undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log; grep -c \"Reference.*undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log; grep -c \"undefined\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.log",
  "description": "Count undefined references"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b092e609-0c3d-4dd8-bb2f-6bb9a0bbadba",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mg9eV5kF84iXVWDf3YKWBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5671,
      "cache_read_input_tokens": 42280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5671
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

_source line 42 · 2026-05-24T01:36:01.143Z_

<details><summary>↩ Tool result · `toolu_019AbgKu1b4m3dLwPaULKvXe`</summary>

```text
0
0
0
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "91eee901-e088-4771-b46e-fcc20445a819",
  "tool_use_result": {
    "stdout": "0\n0\n0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Bash · `toolu_01UYubXxiifbFKew3W6ccd5q`</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.blg",
  "description": "Read bibtex log"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "43adb1d8-ca9a-4c4b-9ad7-5fdd6e2946be",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Mg9eV5kF84iXVWDf3YKWBK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5671,
      "cache_read_input_tokens": 42280,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5671
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

_source line 44 · 2026-05-24T01:36:02.021Z_

<details><summary>↩ Tool result · `toolu_01UYubXxiifbFKew3W6ccd5q`</summary>

```text
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
Capacity: max_strings=200000, hash_size=200000, hash_prime=170003
The top-level auxiliary file: main.aux
The style file: acl_natbib.bst
Reallocated glb_str_ptr (elt_size=4) to 20 items from 10.
Reallocated global_strs (elt_size=200001) to 20 items from 10.
Reallocated glb_str_end (elt_size=4) to 20 items from 10.
Reallocated singl_function (elt_size=4) to 100 items from 50.
Reallocated singl_function (elt_size=4) to 100 items from 50.
Reallocated wiz_functions (elt_size=4) to 6000 items from 3000.
Database file #1: references.bib
You've used 55 entries,
            3764 wiz_defined-function locations,
            1042 strings with 21025 characters,
and the built_in function-call counts, 46695 in all, are:
= -- 3842
> -- 2739
< -- 35
+ -- 1122
- -- 844
* -- 3249
:= -- 6840
add.period$ -- 227
call.type$ -- 55
change.case$ -- 641
chr.to.int$ -- 58
cite$ -- 55
duplicate$ -- 2765
empty$ -- 3106
format.name$ -- 1021
if$ -- 10056
int.to.chr$ -- 2
int.to.str$ -- 2
missing$ -- 655
newline$ -- 279
num.names$ -- 220
pop$ -- 1805
preamble$ -- 1
purify$ -- 506
quote$ -- 0
skip$ -- 2373
stack$ -- 0
substring$ -- 1228
swap$ -- 1535
text.length$ -- 30
text.prefix$ -- 0
top$ -- 0
type$ -- 495
warning$ -- 0
while$ -- 215
width$ -- 0
write$ -- 694
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "0e1def1d-11fd-41fc-8371-0fdb4a3e7fc2",
  "tool_use_result": {
    "stdout": "This is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nCapacity: max_strings=200000, hash_size=200000, hash_prime=170003\nThe top-level auxiliary file: main.aux\nThe style file: acl_natbib.bst\nReallocated glb_str_ptr (elt_size=4) to 20 items from 10.\nReallocated global_strs (elt_size=200001) to 20 items from 10.\nReallocated glb_str_end (elt_size=4) to 20 items from 10.\nReallocated singl_function (elt_size=4) to 100 items from 50.\nReallocated singl_function (elt_size=4) to 100 items from 50.\nReallocated wiz_functions (elt_size=4) to 6000 items from 3000.\nDatabase file #1: references.bib\nYou've used 55 entries,\n            3764 wiz_defined-function locations,\n            1042 strings with 21025 characters,\nand the built_in function-call counts, 46695 in all, are:\n= -- 3842\n> -- 2739\n< -- 35\n+ -- 1122\n- -- 844\n* -- 3249\n:= -- 6840\nadd.period$ -- 227\ncall.type$ -- 55\nchange.case$ -- 641\nchr.to.int$ -- 58\ncite$ -- 55\nduplicate$ -- 2765\nempty$ -- 3106\nformat.name$ -- 1021\nif$ -- 10056\nint.to.chr$ -- 2\nint.to.str$ -- 2\nmissing$ -- 655\nnewline$ -- 279\nnum.names$ -- 220\npop$ -- 1805\npreamble$ -- 1\npurify$ -- 506\nquote$ -- 0\nskip$ -- 2373\nstack$ -- 0\nsubstring$ -- 1228\nswap$ -- 1535\ntext.length$ -- 30\ntext.prefix$ -- 0\ntop$ -- 0\ntype$ -- 495\nwarning$ -- 0\nwhile$ -- 215\nwidth$ -- 0\nwrite$ -- 694",
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

_source line 45_

Compilation: 0 errors, 0 undefined refs, 0 bib warnings. Main text fits within 8 pages (Limitations starts on page 8). Now let me check abstract word count and dataset naming consistency.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5e69496b-91ad-448e-b561-aa831eaeab4d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K7EWL5kPS7Wb2AwtUvaERQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 47951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1249
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

_source line 46_

<details open><summary>🔧 Tool call — Read · `toolu_01HpKEraaY9xNDAUi7eqpvkg`</summary>

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
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "9cb5c62b-6c65-43d1-a931-7e1e4ac63941",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01K7EWL5kPS7Wb2AwtUvaERQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1249,
      "cache_read_input_tokens": 47951,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1249
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

_source line 47 · 2026-05-24T01:36:05.463Z_

<details><summary>↩ Tool result · `toolu_01HpKEraaY9xNDAUi7eqpvkg`</summary>

```text
1	\begin{abstract}
2	Test-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.
3	We characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary cross-task pilots (RE, SQL).
4	Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\,pp; CI crosses zero), revealing a \textbf{correlation-selection gap}.
5	A diagnostic framework identifies two co-occurring conditions---\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that are jointly associated with scaling returns; cross-task exploration confirms task-specific failure modes.
6	Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
7	The framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "3c8ea5e4-eb7c-4984-b30d-244e7f112fb9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time compute scaling---repeated sampling with self-consistency or best-of-$N$---yields large gains on discrete-answer reasoning, but whether these gains transfer to NER remains open.\nWe characterize when scaling succeeds and fails, using NER (four datasets, primarily 7--14B fine-tuned) as the primary analysis, with preliminary cross-task pilots (RE, SQL).\nQuality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\\,pp; CI crosses zero), revealing a \\textbf{correlation-selection gap}.\nA diagnostic framework identifies two co-occurring conditions---\\textit{degeneracy} (i.e., multiple outputs collapsing to identical predictions) and signal alignment collapse---that are jointly associated with scaling returns; cross-task exploration confirms task-specific failure modes.\nEntity-level construction yields conditional gains ($+1.40$\\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.\nThe framework is primarily diagnostic, with limited predictive power for identifying favorable conditions, informing resource allocation decisions before investing in repeated inference.\n\\end{abstract}\n",
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

_source line 48_

<details open><summary>🔧 Tool call — Bash · `toolu_019xP3xd5VnoXaw4EHCCkPNy`</summary>

```json
{
  "command": "python3 -c \"\nimport re\nwith open('sections/abstract.tex') as f:\n    txt = f.read()\n# Strip latex commands\ntxt = re.sub(r'\\\\\\\\begin\\{[^}]+\\}|\\\\\\\\end\\{[^}]+\\}', '', txt)\ntxt = re.sub(r'\\\\\\\\textbf\\{([^}]*)\\}', r'\\1', txt)\ntxt = re.sub(r'\\\\\\\\textit\\{([^}]*)\\}', r'\\1', txt)\ntxt = re.sub(r'\\\\\\\\emph\\{([^}]*)\\}', r'\\1', txt)\ntxt = re.sub(r'\\\\\\\\text\\w*\\{([^}]*)\\}', r'\\1', txt)\ntxt = re.sub(r'\\\\\\$([^\\$]*)\\\\\\$', r'\\1', txt)\ntxt = re.sub(r'\\\\\\\\,', ' ', txt)\ntxt = re.sub(r'\\\\\\\\[a-zA-Z]+', ' ', txt)\ntxt = re.sub(r'[{}~\\$]', ' ', txt)\ntxt = re.sub(r'-', ' ', txt)\nwords = txt.split()\nprint('words=', len(words))\nprint(' '.join(words[:30]))\n\"",
  "description": "Count abstract words"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "7ee977f7-d002-425a-b78f-afcd4a60cf9b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013usvUsDj2sahag3u33iuwj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 731,
      "cache_read_input_tokens": 49200,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 731
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

_source line 49 · 2026-05-24T01:36:12.876Z_

<details><summary>↩ Tool result · `toolu_019xP3xd5VnoXaw4EHCCkPNy`</summary>

```text
words= 185
Test time compute scaling repeated sampling with self consistency or best of N yields large gains on discrete answer reasoning, but whether these gains transfer to NER remains open. We
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "bb0c4f7f-7bea-4ef4-9096-1a8167127c4b",
  "tool_use_result": {
    "stdout": "words= 185\nTest time compute scaling repeated sampling with self consistency or best of N yields large gains on discrete answer reasoning, but whether these gains transfer to NER remains open. We",
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

_source line 50_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "3d59fdbe-fa49-4d2a-97f6-221733f6713d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01X3eqUzxwWpJJX1bqm5UmnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 49931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01Sy7r3d9NKCBaAxfPhq6eUu`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "completed"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "in_progress"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "pending"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "pending"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "completed"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "pending"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "pending"
    },
    {
      "content": "Sync to anonymous repo if changes were made",
      "activeForm": "Syncing to anonymous repo",
      "status": "pending"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "355752ae-4b27-4b58-aac4-4f72103c1897",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01X3eqUzxwWpJJX1bqm5UmnP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 571,
      "cache_read_input_tokens": 49931,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 571
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

### Tool result

_source line 52 · 2026-05-24T01:36:20.281Z_

<details><summary>↩ Tool result · `toolu_01Sy7r3d9NKCBaAxfPhq6eUu`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "6ffaef0c-8a69-4f87-8c19-36cace162e1e",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "in_progress",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "pending",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Check abstract word count",
        "status": "pending",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "pending",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "in_progress",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "pending",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Grep · `toolu_01NHpbqHBxbkY1wKyoW1HX9E`</summary>

```json
{
  "pattern": "fewnerd|few_NERD|FEWNERD|Few_NERD|FewNERD|Few-nerd",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-i": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d207eb3c-4efd-42dd-ba36-81a882da324e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DoicHomjbVianVQdNjnBBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 50502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 54 · 2026-05-24T01:36:25.057Z_

<details><summary>↩ Tool result · `toolu_01NHpbqHBxbkY1wKyoW1HX9E`</summary>

```text
&lt;persisted-output>
Output too large (33.7KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/56622092-b880-43f3-8cd7-2a5161528236/tool-results/toolu_01NHpbqHBxbkY1wKyoW1HX9E.txt

Preview (first 2KB):
sections/mechanistic.tex:5:[Omitted long matching line]
sections/mechanistic.tex:21:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
sections/mechanistic.tex:23:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\to}$CoNLL) and $0.671$ (CoNLL${\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.
sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
sections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.
sections/checklist.tex:39:Yes. Instance counts are reported in Table~\ref{tab:fewnerd} and throughout Section~\ref{sec:experiments}. Gold-filtering counts, dataset sizes, and evaluation protocol details are in Section~\ref{sec:evaluation}.
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "9656c626-8c32-48ca-9fb8-d9283080a349",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/mechanistic.tex:5:[Omitted long matching line]\nsections/mechanistic.tex:21:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\\ref{app:hidden_probe}).\nsections/mechanistic.tex:23:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\\to}$CoNLL) and $0.671$ (CoNLL${\\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.\nsections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\nsections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.\nsections/checklist.tex:39:Yes. Instance counts are reported in Table~\\ref{tab:fewnerd} and throughout Section~\\ref{sec:experiments}. Gold-filtering counts, dataset sizes, and evaluation protocol details are in Section~\\ref{sec:evaluation}.\nsections/checklist.tex:54:Yes. We report multi-seed results (5 seeds; $\\sigma$ in Table~\\ref{tab:multiseed}), bootstrap 95\\% confidence intervals (Tables~\\ref{tab:selection}, \\ref{tab:fewnerd_full}), paired bootstrap $p$-values throughout, and minimum detectable effect sizes (Section~\\ref{sec:selection_gap}). Tables clearly indicate whether values are single-seed, multi-seed means, or confidence intervals.\nsections/method.tex:65:We evaluate across four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), two model families (Qwen3-8B, LLaMA-3.1-8B-Instruct), and $N \\in \\{2, \\ldots, 64\\}$ samples, with extensions to 4B/14B scale ablations, Qwen2.5-72B and GPT-5.5 zero-shot, RE, and SQL parsing (\\S\\ref{sec:experiments}).\nsections/theory.tex:7:We select $\\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\\,pp (compressed) to $+4.6$\\,pp (non-compressed; Appendix~\\ref{app:fewnerd_epsilon}).\nsections/theory.tex:11:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): Few-NERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, SciERC converges more slowly ($c{\\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\\,pp---a persistent gap.\nsections/theory.tex:12:[Omitted long matching line]\nsections/theory.tex:13:Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\\% vs.\\ Qwen3: $13.0$\\% vs.\\ GPT-5.5: $50$\\% on Few-NERD; Appendix~\\ref{app:cross_scale}).\nsections/theory.tex:24:Methods using $\\theta{=}2/N$ are most affected ($-3.09$\\,pp at $N{=}8$, $-6.90$\\,pp at $N{=}16$ vs.\\ greedy on Few-NERD); majority vote ($\\theta{=}\\tfrac{1}{2}$) reduces the delta to $-0.87$/$-0.60$\\,pp---severity reduction, not immunity (Table~\\ref{tab:theta_sweep}).\nsections/_archived/experiments_OLD.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\nsections/_archived/experiments_OLD.tex:15:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nsections/_archived/experiments_OLD.tex:97:On SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nsections/_archived/experiments_OLD.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\nsections/_archived/experiments_OLD.tex:102:Three factors shape LP selection gains: (1)~\\textit{instance degeneracy} (SciERC 17.8\\%, CoNLL 61.7\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} (CoNLL ${\\approx}4$\\,pp vs.\\ SciERC 13.0\\,pp); (3)~\\textit{LP-quality alignment} (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nsections/_archived/experiments_OLD.tex:103:The pattern matches observations: Few-NERD (low degeneracy, strong alignment) yields $+1.39$\\,pp; SciERC (weak alignment) $+0.04{\\pm}0.48$\\,pp (3-seed; Table~\\ref{tab:multiseed}); CoNLL (high degeneracy) none; WNUT-17 shows reversed LP ($\\rho{=}{-}0.446$) yet QE remains effective (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}).\nsections/_archived/experiments_OLD.tex:104:The factors do not combine into a predictive model ($R^2{<}0$, 23 configurations) but each is supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\nsections/_archived/experiments_OLD.tex:107:\\subsection{Cross-Dataset Contrast: Few-NERD}\nsections/_archived/experiments_OLD.tex:108:\\label{sec:fewnerd}\nsections/_archived/experiments_OLD.tex:113:\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\nsections/_archived/experiments_OLD.tex:114:\\label{tab:fewnerd}\nsections/_archived/experiments_OLD.tex:123:Few-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\nsections/_archived/experiments_OLD.tex:128:Few-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy ($+1.39$~pp, $p{<}0.001$; structural signals degrade: VC $-1.79$, SJ $-2.14$~pp), with LP 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp), generalizing to LLaMA (Table~\\ref{tab:cross_selection}). Training convergence modulates degeneracy (5-epoch: $31$\\%, halving LP gains; Appendix~\\ref{app:epoch_confound}).\nsections/_archived/experiments_OLD.tex:136:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\nsections/_archived/experiments_OLD.tex:192:Few-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\nsections/_archived/experiments_OLD.tex:202:LP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all datasets. Structural signals generalize (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); this comparison simultaneously varies model family, regime, and quantization, so individual effects cannot be disentangled.\nsections/_archived/experiments_OLD.tex:203:LP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\nsections/_archived/experiments_OLD.tex:206:[Omitted long matching line]\nsections/_archived/experiments_OLD.tex:209:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\\% vs.\\ Qwen3-8B: $13.0$\\%; Table~\\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\\to$5 epochs triples degeneracy within the same model (\\S\\ref{sec:fewnerd}).\nsections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\nsections/_archived/experiments_OLD.tex:236:Few-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001^\\dagger$ \\\\\nsections/_archived/experiments_OLD.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$, $p_{\\text{adj}}{=}0.20$; Table~\\ref{tab:entity_construction}), recovering 8--11\\% of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\\ref{app:n_scaling}).\nsections/_archived/experiments_OLD.tex:247:Construction and LP selection are complementary, governed by $\\rho_{\\text{adj}}$: Few-NERD ($\\rho_{\\text{adj}}{=}0.516$) favors both, while SciERC ($\\rho_{\\text{adj}}{=}0.167$) favors construction only. A three-way routing protocol ($\\rho_{\\text{adj}} \\geq 0.3$: LP; $<0.3$ with positive construction: construction; else: greedy) is stable across $\\tau{\\in}[0.2, 0.4]$.\nsections/_archived/experiments_OLD.tex:250:Entity verification features achieve AUC${=}0.923{\\pm}0.002$ (LightGBM, OOF evaluation) but yield only $+0.30$\\,pp overall via construction ($+1.28$\\,pp SciERC, $+0.02$\\,pp Few-NERD).\nsections/_archived/experiments_OLD.tex:251:Cross-dataset transfer is negative (Few-NERD: $-0.76$, $-1.02$\\,pp; Appendix~\\ref{app:verifier_transfer}), demonstrating dataset-specific feature mappings. This motivates distillation approaches using each dataset's own SC consensus as supervision.\nsections/single_signal.tex:42:Few-NERD provides the clearest positive case: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.055$ (BH $p_{\\text{adj}}{=}0.003$).} at low degeneracy (13.0\\% vs.\\ 12.2--67.9\\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\\,pp; \\S\\ref{sec:fewnerd}).\nsections/single_signal.tex:48:(3)~LP compression limits exploitation (Few-NERD within-instance $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nsections/adaptive.tex:27:{\\footnotesize $^\\dagger$Few-NERD only; SciERC $+0.2$\\,pp ($p{=}0.29$). $^\\ddagger$Seed-sensitive ($\\sigma{=}0.48$\\,pp).}\nsections/adaptive.tex:33:Combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (Few-NERD) yields $+0.42$\\,pp over pure LLaMA ($p{<}0.001$, CI $[0.27, 0.58]$; $N{=}8$ total).\nsections/abstract.tex:6:Entity-level construction yields conditional gains ($+1.40$\\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.\nsections/appendix.tex:233:[Omitted long matching line]\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:248:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\nsections/appendix.tex:338:6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:351:19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:358:24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:359:25 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\nsections/appendix.tex:364:30 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\nsections/appendix.tex:370:34 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\nsections/appendix.tex:385:45 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\nsections/appendix.tex:532:DeBERTa achieves $\\rho{=}0.329{\\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\\pm}26.5$\\% of the oracle gap (13 of 15 runs negative; vs.\\ LP's $+4.2{\\pm}10.7$\\%); on Few-NERD, DeBERTa recovers only $+3.5$\\% (single 80/20 split; vs.\\ LP's $+16.3$\\%).\nsections/appendix.tex:540:In-domain OOF construction yields $+0.30$\\,pp overall, with per-dataset gains of $+1.28$\\,pp (SciERC), $+0.55$\\,pp (CoNLL), and $+0.02$\\,pp (Few-NERD).\nsections/appendix.tex:541:The near-zero Few-NERD gain despite high AUC shows that frequency-based threshold construction already captures most of the verifier's signal.\nsections/appendix.tex:542:Cross-dataset transfer to Few-NERD is negative: $-0.76$\\,pp (B2-v2), $-1.02$\\,pp (B2-v3), $-1.27$\\,pp (B2-v4 Replace, AUC${=}0.822$), and $-0.85$\\,pp (B2-v4 Augment, AUC${=}0.855$), all below greedy.\nsections/appendix.tex:550:Unlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\nsections/appendix.tex:552:Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).\nsections/appendix.tex:562:& \\multicolumn{3}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{Few-NERD}} \\\\\nsections/appendix.tex:577:On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\\% vs.\\ $12.3$\\%).\nsections/appendix.tex:578:A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%); LP's bottleneck is not token aggregation.\nsections/appendix.tex:592:Method & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\nsections/appendix.tex:611:[Omitted long matching line]\nsections/appendix.tex:627:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; \\S\\ref{app:hidden_probe}).\nsections/appendix.tex:629:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\\to}$CoNLL) and $0.671$ (CoNLL${\\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.\nsections/appendix.tex:638:Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).\nsections/appendix.tex:643:\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\nsections/appendix.tex:683:ESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\\S\\ref{sec:mechanistic}) generalizes.\nsections/appendix.tex:696:FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\nsections/appendix.tex:920:Few-NERD exhibits substantially stronger alignment ($\\rho{=}0.667$) than SciERC ($\\rho{=}0.262$), consistent with LP selection succeeding only on Few-NERD.\nsections/appendix.tex:935:Few-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\\% \\\\\nsections/appendix.tex:943:\\paragraph{Few-NERD LP compression threshold sensitivity.}\\label{app:fewnerd_epsilon}\nsections/appendix.tex:945:Tables~\\ref{tab:fewnerd_epsilon} and \\ref{tab:fewnerd_lp_bucket} extend the $\\varepsilon$ analysis to Few-NERD ($n{=}32{,}565$, Qwen3-8B, $N{=}8$, seed${=}42$).\nsections/appendix.tex:950:\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\nsections/appendix.tex:951:\\label{tab:fewnerd_epsilon}\nsections/appendix.tex:969:\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\nsections/appendix.tex:970:\\label{tab:fewnerd_lp_bucket}\nsections/appendix.tex:987:The LP-best advantage over MV shows a clear transition: compressed instances (LP range${<}0.05$) gain $+0.8$ to $+2.3$\\,pp, while non-compressed instances gain $+3.6$ to $+5.8$\\,pp (Table~\\ref{tab:fewnerd_lp_bucket}).\nsections/appendix.tex:1249:MV fails to improve F1 on any dataset: Few-NERD $\\Delta{=}{-}2.74$\\,pp, SciERC $-0.74$\\,pp, CoNLL $-0.04$\\,pp.\nsections/appendix.tex:1252:Few-NERD and SciERC ($\\alpha_{\\textup{crit,eff}} {<} 1$) show significantly negative $\\Delta$, indicating that even where structural headroom exists, marginal-entity precision is insufficient.\nsections/appendix.tex:1253:SciERC's lower $\\alpha_{\\textup{crit}}$ ($0.334$, vs.\\ $0.396$ for Few-NERD and $0.456$ for CoNLL) is consistent with it being the only dataset where a trained entity verifier (AUC${=}0.923$) achieves positive gain ($+1.28$\\,pp).\nsections/appendix.tex:1264:Few-NERD & 3 & .791 & .764 & .885 & $-2.74{\\pm}0.54$ & 8.8\\% & 0.396 & 0.434 & $\\Delta < 0$ \\\\\nsections/appendix.tex:1270:\\noindent{\\footnotesize $^*$CoNLL $\\delta{=}60.3$\\% (full test set, 3-seed) vs.\\ $61.7$\\% in Table~\\ref{tab:fewnerd} (gold-filtered); the difference reflects filtering. Tab.~\\ref{tab:pretrained_summary} reports $57$--$60$\\% (seed range, finetuned).}\nsections/appendix.tex:1365: & SciERC & CoNLL & Few-NERD \\\\\nsections/appendix.tex:1381:\\paragraph{Few-NERD NER free-form results.}\nsections/appendix.tex:1382:On Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$), free-form decoding produces near-identical LP distributions (LP std ratio $1.00{\\times}$) and unchanged degeneracy ($9.1$\\%).\nsections/appendix.tex:1502:\\paragraph{Few-NERD $N$-scaling: MV at $N{=}16$.}\nsections/appendix.tex:1503:On Few-NERD (Qwen3-8B, 3-seed), increasing from $N{=}8$ to $N{=}16$ reduces degeneracy ($8.8$\\%$\\to$$4.0{\\pm}1.4$\\%) and attenuates MV degradation ($-2.74$\\,pp$\\to$$-1.65{\\pm}0.61$\\,pp), but MV remains negative.\nsections/appendix.tex:1526:\\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$, seed 42). Values differ from Table~\\ref{tab:selection} (0.645, 2-seed) and Table~\\ref{tab:fewnerd} (0.663, 3-seed) due to seed and aggregation differences; relative trends are consistent.}\nsections/appendix.tex:1558:The exponent $c$ varies with dataset complexity: FewNERD ($c{\\approx}0.61$) scales comparably to reasoning-task estimates ($c{\\approx}0.5$--$0.7$; \\citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.\nsections/appendix.tex:1584:FewNERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:1587:FewNERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1609:Few-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\nsections/appendix.tex:1621:LP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).\nsections/appendix.tex:1622:LP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\nsections/appendix.tex:1625:[Omitted long matching line]\nsections/appendix.tex:1628:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\\% vs.\\ Qwen3-8B: $13.0$\\%; Table~\\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\\to$5 epochs triples degeneracy within the same model (\\S\\ref{sec:fewnerd}).\nsections/appendix.tex:1652:Qwen3-14B fine-tuned on Few-NERD achieves greedy F1${=}0.798$ ($+0.9$\\,pp over 8B) with oracle headroom of 8.1\\,pp ($+1.2$\\,pp over 8B's 6.9\\,pp) and $\\rho$ advantage $+0.029$ over 8B.\nsections/appendix.tex:1672:Few-NERD & Pretrained ($N{=}8$) & .538 & $+$3.9${\\pm}$0.2 & 11.7 & 36\\% & .436 \\\\\nsections/appendix.tex:1686:On Few-NERD ($n{=}32{,}565$, 3-seed), finetuned degeneracy ($8.8$\\%) is \\textit{lower} than pretrained ($11.7$\\%), yet finetuned MV is negative ($-2.74{\\pm}0.54$\\,pp).\nsections/appendix.tex:1689:Fine-tuning thus decouples agreement from quality through dataset-dependent pathways: diversity elimination on CoNLL (degeneracy $36{\\to}57$--$60$\\%), but correlated error patterns on Few-NERD.\nsections/appendix.tex:1701:\\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}\nsections/appendix.tex:1733:\\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}\nsections/appendix.tex:1801:However, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$13\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\nsections/appendix.tex:1930:\\section{Few-NERD Full Results}\\label{app:fewnerd}\nsections/appendix.tex:1932:Table~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nsections/appendix.tex:1939:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:1940:\\label{tab:fewnerd_full}\nsections/appendix.tex:1959:(1)~All five signals achieve positive QE ($\\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.\nsections/appendix.tex:1966:Table~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\nsections/appendix.tex:1975:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\nsections/appendix.tex:2042:MF-Platt can reorder candidates within an instance, yet yields no significant selection improvement: $\\Delta{=}{-}1.1$~pp on SciERC ($p{=}0.72$), $+0.3$~pp on CoNLL ($p{=}0.31$), and $-0.6$~pp on Few-NERD ($p{=}0.83$).\nsections/appendix.tex:2049:[Omitted long matching line]\nsections/appendix.tex:2060:Few-NERD & .771 & .785 & .778 (.83) & & .262 & .080 \\\\\nsections/appendix.tex:2069:Table~\\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; gold-filtered $n{=}32{,}565$, 2-seed mean).\nsections/appendix.tex:2083:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\nsections/appendix.tex:2108:[Omitted long matching line]\nsections/appendix.tex:2109:Even at the most favorable epoch (3-epoch, $\\rho{=}0.319$), SciERC alignment remains below the ${\\sim}$0.5 threshold associated with successful LP selection on Few-NERD.\nsections/appendix.tex:2133:The Few-NERD epoch analysis covers 2 points (3 vs.\\ 5 epochs); the SciERC curve provides a 3-point gradient showing monotonic degeneracy increase with simultaneous within-instance alignment degradation.\nsections/appendix.tex:2135:All Few-NERD results in the main text use the 3-epoch model (standard early stopping); the 5-epoch comparison is a controlled ablation.\nsections/appendix.tex:2142:On SciERC, DALS yields $+0.71{\\pm}0.48$~pp (3-seed mean; individual seeds: $+0.19$ to $+1.14$~pp); on Few-NERD, $+0.30$~pp ($p{<}0.001$; gain remains positive across $\\tau \\in [0.01, 0.15]$); on CoNLL, where pure LP selection degrades F1 ($-0.85$~pp), DALS shows comparable degradation (Qwen: $-0.87$~pp; LLaMA: neutral).\nsections/appendix.tex:2147:Leave-one-out (LOO) cross-validation across datasets shows that the optimal $\\tau$ spans two orders of magnitude: $\\tau^*{=}0.001$ on Few-NERD, $0.05$ on SciERC, and $0.10$ on CoNLL.\nsections/appendix.tex:2154:To test whether LP-quality alignment is associated with selection gains within datasets, we restrict LP selection to the favorable subset: non-degenerate instances whose within-instance LP range exceeds the dataset-specific median (SciERC: 0.040 nats, CoNLL: 0.062, Few-NERD: 0.067).\nsections/appendix.tex:2168:Few-NERD & $+$0.63 & [$-$0.02, $+$1.30] & marginal positive \\\\\nsections/appendix.tex:2176:On Few-NERD, the trend is directionally consistent but the confidence interval crosses zero; the full-dataset result ($+1.39$~pp, $p{<}0.001$) reflects the larger sample size rather than a stronger per-instance effect.\nsections/appendix.tex:2238:\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\nsections/appendix.tex:2247:Few-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\\\\nsections/appendix.tex:2270:Few-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001^\\dagger$ \\\\\nsections/appendix.tex:2281:Table~\\ref{tab:theta_sweep} reports entity construction F1 as a function of the confirmation threshold $\\theta$ across three datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$). The default $\\theta{=}2/N{=}0.25$ achieves the best LP-weighted $\\Delta$F1 on Few-NERD and is within 0.04\\,pp of the optimum on SciERC. Performance is stable across $\\theta \\in [0.15, 0.35]$; below 0.15, spurious entities degrade precision, and above 0.40, aggressive filtering removes correct low-frequency entities.\nsections/appendix.tex:2303:\\multirow{8}{*}{Few-NERD}\nsections/appendix.tex:2339:All three weighting schemes beat greedy on SciERC, where degeneracy is low; LP and VC also improve Few-NERD, though gains are smaller than the Qwen results in Table~\\ref{tab:entity_construction}.\nsections/appendix.tex:2341:SJ-weighted construction degrades on Few-NERD ($-0.20$\\,pp), consistent with SJ over-weighting high-consensus samples, which correlates with the degeneracy direction rather than opposing it.\nsections/appendix.tex:2353:Few-NERD & $+$0.02 & $+$0.15 & $-$0.20 \\\\\nsections/appendix.tex:2379:FewNERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\\\\nsections/appendix.tex:2380:FewNERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\\\\nsections/appendix.tex:2436:SC + LP selection is positive only on Few-NERD ($p{<}0.001$) and neutral to negative elsewhere (SciERC $+0.2$\\,pp, $p{=}0.29$; CoNLL $-0.85$\\,pp).\nsections/appendix.tex:2485:Qwen2.5-72B zero-shot exhibits the same gap: LP $\\rho$ drops without fine-tuning, structural signals generalize (VC $\\rho{=}0.416$ on Few-NERD), and degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: 31.7--46.2\\% vs.\\ Qwen3: 13.0\\%; Appendix~\\ref{app:cross_scale}). The capability ceiling persists from 4B to 72B.\nsections/appendix.tex:2488:The variation is complexity-dependent and interpretable: CoNLL (4 types, 91\\% F1) at 0.882, Few-NERD (8 types, 75\\% F1) at 0.636, SciERC (6 types, 65\\% F1) at 0.630. LODO transfer drops to 0.56--0.67 (\\S\\ref{sec:mechanistic}), confirming dataset-specific encoding. The pattern---not the point estimate---is the finding.\nsections/appendix.tex:2513:We present 9 concrete instances illustrating the three primary failure modes: output degeneracy, LP confidence inversion, and consensus-based verification failure. All examples use Qwen3-8B on Few-NERD ($N{=}8$, $T{=}1.0$) from the MF4v2 pipeline.\nsections/introduction.tex:11:The optimal strategy is dataset-dependent (LP $+1.39$\\,pp on Few-NERD; MV $+0.6$\\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\\% zero-F1; Appendix~\\ref{app:re_extension}).\nsections/introduction.tex:12:Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.\nsections/introduction.tex:19:[Omitted long matching line]\nsections/introduction.tex:30:Entity-level construction yields $+1.40$\\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \\citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.\nsections/experiments_main.tex:8:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:selection_gap}).\nsections/experiments_main.tex:13:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others; Appendix~\\ref{app:epoch_confound}).\nsections/experiments_main.tex:19:\\caption{MV $\\Delta$F1 vs.\\ $\\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\\,pp at $N{=}64$).}\nsections/experiments_main.tex:56:\\subsection{Cross-Dataset Contrast: Few-NERD}\\label{sec:fewnerd}\nsections/experiments_main.tex:62:\\label{tab:fewnerd}\nsections/experiments_main.tex:71:Few-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\nsections/experiments_main.tex:76:[Omitted long matching line]\nsections/experiments_main.tex:86:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\nsections/experiments_main.tex:90:MV gains range from $-2.71$\\,pp (Few-NERD) to $+0.6$\\,pp (CoNLL at $N{=}64$; Figure~\\ref{fig:n_scaling}); the optimal strategy is dataset-dependent (LP-best $+1.4$\\,pp on Few-NERD vs.\\ MV $+0.6$\\,pp on CoNLL).\nsections/experiments_main.tex:104:LP-weighted construction yields $+1.40{\\pm}0.51$\\,pp on Few-NERD (4-seed mean; $p{<}0.001$; Table~\\ref{tab:entity_construction}), consistent with favorable diagnostic conditions ($D{=}13$\\%, headroom${=}12.4$\\,pp), a non-significant $+0.32$\\,pp on SciERC, and no gain on CoNLL ($-0.39$\\,pp).\\footnote{Degenerate instances contribute $\\Delta{=}0$ by construction; all gains concentrate in the non-degenerate subset.}\nsections/experiments_main.tex:106:Construction and LP selection are complementary ($\\rho_{\\text{adj}}$: Few-NERD $0.516$; Table~\\ref{tab:cross_selection}).\nsections/experiments_main.tex:107:Training convergence modulates returns: 5-epoch Few-NERD eliminates LP gains (selection: $+1.39{\\to}+0.12$\\,pp; construction: $+0.88{\\to}+0.20$\\,pp) as degeneracy rises from $9$\\% to $26$\\% (Appendix~\\ref{app:epoch_confound}).",
    "numLines": 157
  }
}
```

</details>

---

### Tool call

_source line 55_

<details open><summary>🔧 Tool call — Grep · `toolu_01TSTMknTSaBjB664o58Pzbu`</summary>

```json
{
  "pattern": "CONLL|Conll|conll",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d6fce318-0230-4627-8982-68631832d4a7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DoicHomjbVianVQdNjnBBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 50502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 56 · 2026-05-24T01:36:26.175Z_

<details><summary>↩ Tool result · `toolu_01TSTMknTSaBjB664o58Pzbu`</summary>

```text
sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
sections/_archived/experiments_OLD.tex:11:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.
sections/appendix.tex:1999:\label{tab:per_type_lp_conll}
sections/experiments_main.tex:9:\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\approx}$91\% F1) serves as a ceiling-effect control.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "dea3fb61-2fc4-4566-9878-dd4518e8478b",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\nsections/_archived/experiments_OLD.tex:11:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control where limited oracle headroom constrains selection gains.\nsections/appendix.tex:1999:\\label{tab:per_type_lp_conll}\nsections/experiments_main.tex:9:\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} (3{,}453 test sentences, 4 entity types, ${\\approx}$91\\% F1) serves as a ceiling-effect control.",
    "numLines": 4
  }
}
```

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Grep · `toolu_01PnVANGScrKrrVN3tLaxw2v`</summary>

```json
{
  "pattern": "scierc|Sci-ERC|Sci-erc|sci-erc",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "e547b5bd-2afd-4bbf-b9ed-ef707659495e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DoicHomjbVianVQdNjnBBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 50502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 58 · 2026-05-24T01:36:27.746Z_

<details><summary>↩ Tool result · `toolu_01PnVANGScrKrrVN3tLaxw2v`</summary>

```text
sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
sections/_archived/experiments_OLD.tex:9:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\approx}$65\% F1.
sections/appendix.tex:2016:\label{tab:per_type_lp_scierc}
sections/appendix.tex:2074:LP selection shows even more dramatic degradation: 5-epoch LP $\Delta{=}{+}0.12{\pm}0.04$\,pp (2-seed mean), a 91\% reduction from the 3-epoch $+1.39$\,pp (both evaluated on the full test set under identical conditions; Table~\ref{tab:epoch_confound}). This confirms that training convergence not only increases degeneracy but also erodes LP's discriminative power within non-degenerate instances, consistent with the alignment degradation observed in SciERC (Table~\ref{tab:epoch_scierc}).
sections/appendix.tex:2102:Table~\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).
sections/appendix.tex:2115:\label{tab:epoch_scierc}
sections/experiments_main.tex:7:\textbf{SciERC} \cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\approx}$65\% F1).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d9a535b2-de23-4a3a-b57c-ffcfefb1a590",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\nsections/_archived/experiments_OLD.tex:9:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed where models achieve ${\\approx}$65\\% F1.\nsections/appendix.tex:2016:\\label{tab:per_type_lp_scierc}\nsections/appendix.tex:2074:LP selection shows even more dramatic degradation: 5-epoch LP $\\Delta{=}{+}0.12{\\pm}0.04$\\,pp (2-seed mean), a 91\\% reduction from the 3-epoch $+1.39$\\,pp (both evaluated on the full test set under identical conditions; Table~\\ref{tab:epoch_confound}). This confirms that training convergence not only increases degeneracy but also erodes LP's discriminative power within non-degenerate instances, consistent with the alignment degradation observed in SciERC (Table~\\ref{tab:epoch_scierc}).\nsections/appendix.tex:2102:Table~\\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).\nsections/appendix.tex:2115:\\label{tab:epoch_scierc}\nsections/experiments_main.tex:7:\\textbf{SciERC} \\cite{luan2018scierc} (551 test instances, 6 entity types) is the primary medium-difficulty test bed (${\\approx}$65\\% F1).",
    "numLines": 7
  }
}
```

</details>

---

### Tool call

_source line 59_

<details open><summary>🔧 Tool call — Grep · `toolu_011XHcvJTSBxTAUrBMWmMmpm`</summary>

```json
{
  "pattern": "Wnut|WNUT17|wnut17|wnut |WnUT",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "f7a0f24e-5d3f-4096-aff6-dd3f44fa313f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DoicHomjbVianVQdNjnBBj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 50502,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 60 · 2026-05-24T01:36:28.970Z_

<details><summary>↩ Tool result · `toolu_011XHcvJTSBxTAUrBMWmMmpm`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a9bc10cd-5660-4759-a78c-482db0b4e412",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 61_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "635f0dcf-765f-4bf8-8605-6edd4f0b5037",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BSo6hG2HgdkMPJBH9awWDS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 51046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3069
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

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Bash · `toolu_0158VYZEuTHH3HaoNbpWPaVj`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/56622092-b880-43f3-8cd7-2a5161528236/tool-results/toolu_01NHpbqHBxbkY1wKyoW1HX9E.txt | head -100",
  "description": "Read fewnerd grep output"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5b339c3a-f7a3-4611-ba3d-940af9b90be1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BSo6hG2HgdkMPJBH9awWDS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 51046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3069
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

_source line 63 · 2026-05-24T01:36:40.559Z_

<details><summary>↩ Tool result · `toolu_0158VYZEuTHH3HaoNbpWPaVj`</summary>

```text
sections/mechanistic.tex:5:[Omitted long matching line]
sections/mechanistic.tex:21:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\ref{app:hidden_probe}).
sections/mechanistic.tex:23:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\to}$CoNLL) and $0.671$ (CoNLL${\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.
sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
sections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.
sections/checklist.tex:39:Yes. Instance counts are reported in Table~\ref{tab:fewnerd} and throughout Section~\ref{sec:experiments}. Gold-filtering counts, dataset sizes, and evaluation protocol details are in Section~\ref{sec:evaluation}.
sections/checklist.tex:54:Yes. We report multi-seed results (5 seeds; $\sigma$ in Table~\ref{tab:multiseed}), bootstrap 95\% confidence intervals (Tables~\ref{tab:selection}, \ref{tab:fewnerd_full}), paired bootstrap $p$-values throughout, and minimum detectable effect sizes (Section~\ref{sec:selection_gap}). Tables clearly indicate whether values are single-seed, multi-seed means, or confidence intervals.
sections/method.tex:65:We evaluate across four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), two model families (Qwen3-8B, LLaMA-3.1-8B-Instruct), and $N \in \{2, \ldots, 64\}$ samples, with extensions to 4B/14B scale ablations, Qwen2.5-72B and GPT-5.5 zero-shot, RE, and SQL parsing (\S\ref{sec:experiments}).
sections/theory.tex:7:We select $\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\,pp (compressed) to $+4.6$\,pp (non-compressed; Appendix~\ref{app:fewnerd_epsilon}).
sections/theory.tex:11:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): Few-NERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, SciERC converges more slowly ($c{\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\,pp---a persistent gap.
sections/theory.tex:12:[Omitted long matching line]
sections/theory.tex:13:Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\% vs.\ Qwen3: $13.0$\% vs.\ GPT-5.5: $50$\% on Few-NERD; Appendix~\ref{app:cross_scale}).
sections/theory.tex:24:Methods using $\theta{=}2/N$ are most affected ($-3.09$\,pp at $N{=}8$, $-6.90$\,pp at $N{=}16$ vs.\ greedy on Few-NERD); majority vote ($\theta{=}\tfrac{1}{2}$) reduces the delta to $-0.87$/$-0.60$\,pp---severity reduction, not immunity (Table~\ref{tab:theta_sweep}).
sections/_archived/experiments_OLD.tex:10:\textbf{Few-NERD} \cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\approx}$75\% F1) provides a low-degeneracy contrast where LP selection succeeds (\S\ref{sec:fewnerd}).
sections/_archived/experiments_OLD.tex:15:\textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \cite{zheng2024llamafactory} (training details in Appendix~\ref{app:training}; Few-NERD uses 3 epochs vs.\ 5 for others due to earlier convergence; Appendix~\ref{app:epoch_confound}).
sections/_archived/experiments_OLD.tex:97:On SciERC ($n{=}529$, 2-seed sign tests\footnote{MDE${\approx}$1.5~pp at 80\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.
sections/_archived/experiments_OLD.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\S\ref{sec:fewnerd}), while structural signals still degrade selection.
sections/_archived/experiments_OLD.tex:102:Three factors shape LP selection gains: (1)~\textit{instance degeneracy} (SciERC 17.8\%, CoNLL 61.7\%; Table~\ref{tab:fewnerd}); (2)~\textit{oracle headroom} (CoNLL ${\approx}4$\,pp vs.\ SciERC 13.0\,pp); (3)~\textit{LP-quality alignment} (Few-NERD $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
sections/_archived/experiments_OLD.tex:103:The pattern matches observations: Few-NERD (low degeneracy, strong alignment) yields $+1.39$\,pp; SciERC (weak alignment) $+0.04{\pm}0.48$\,pp (3-seed; Table~\ref{tab:multiseed}); CoNLL (high degeneracy) none; WNUT-17 shows reversed LP ($\rho{=}{-}0.446$) yet QE remains effective (VC $\rho{=}0.724$, $N{=}16$; Table~\ref{tab:wnut}).
sections/_archived/experiments_OLD.tex:104:The factors do not combine into a predictive model ($R^2{<}0$, 23 configurations) but each is supported by controlled ablations (\S\ref{sec:fewnerd}, \S\ref{sec:discussion}).
sections/_archived/experiments_OLD.tex:107:\subsection{Cross-Dataset Contrast: Few-NERD}
sections/_archived/experiments_OLD.tex:108:\label{sec:fewnerd}
sections/_archived/experiments_OLD.tex:113:\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\ref{tab:multiseed}). $p$: paired bootstrap.}
sections/_archived/experiments_OLD.tex:114:\label{tab:fewnerd}
sections/_archived/experiments_OLD.tex:123:Few-NERD & 32{,}565 & .748 & 13.0\% & .220 & $\mathbf{+1.39}$\,pp & ${<}.001$ \\
sections/_archived/experiments_OLD.tex:128:Few-NERD (Table~\ref{tab:fewnerd}) confirms LP selection at low degeneracy ($+1.39$~pp, $p{<}0.001$; structural signals degrade: VC $-1.79$, SJ $-2.14$~pp), with LP 50$\times$ more seed-stable ($\sigma{=}0.04$ vs.\ SJ $2.02$~pp), generalizing to LLaMA (Table~\ref{tab:cross_selection}). Training convergence modulates degeneracy (5-epoch: $31$\%, halving LP gains; Appendix~\ref{app:epoch_confound}).
sections/_archived/experiments_OLD.tex:136:\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
sections/_archived/experiments_OLD.tex:192:Few-NERD & 7B FT$^\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\
sections/_archived/experiments_OLD.tex:202:LP $\rho$ drops without fine-tuning (Table~\ref{tab:scale_comparison}) and LP selection fails on all datasets. Structural signals generalize (Few-NERD VC $\rho{=}0.416$). Degeneracy increases (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%); this comparison simultaneously varies model family, regime, and quantization, so individual effects cannot be disentangled.
sections/_archived/experiments_OLD.tex:203:LP-weighted construction yields $+1.53$\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\% of headroom. Construction fails on Few-NERD ($-0.20$\,pp) and CoNLL ($-0.37$\,pp) where degeneracy exceeds $46$\%---consistent with FT-regime degeneracy gating.
sections/_archived/experiments_OLD.tex:206:[Omitted long matching line]
sections/_archived/experiments_OLD.tex:209:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\% vs.\ Qwen3-8B: $13.0$\%; Table~\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\to$5 epochs triples degeneracy within the same model (\S\ref{sec:fewnerd}).
sections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): FewNERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$); a single stochastic sample underperforms greedy ($N{\geq}4$ needed to match).
sections/_archived/experiments_OLD.tex:236:Few-NERD & LP & $.748$ & $\mathbf{.762{\pm}.005}$ & $+1.40{\pm}0.51$\,pp & ${<}.001^\dagger$ \\
sections/_archived/experiments_OLD.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\pm}0.51$\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\pm}0.49$\,pp, $p{=}0.004$, $p_{\text{adj}}{=}0.20$; Table~\ref{tab:entity_construction}), recovering 8--11\% of oracle headroom. CoNLL shows no gain ($-0.39$\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\ref{app:n_scaling}).
sections/_archived/experiments_OLD.tex:247:Construction and LP selection are complementary, governed by $\rho_{\text{adj}}$: Few-NERD ($\rho_{\text{adj}}{=}0.516$) favors both, while SciERC ($\rho_{\text{adj}}{=}0.167$) favors construction only. A three-way routing protocol ($\rho_{\text{adj}} \geq 0.3$: LP; $<0.3$ with positive construction: construction; else: greedy) is stable across $\tau{\in}[0.2, 0.4]$.
sections/_archived/experiments_OLD.tex:250:Entity verification features achieve AUC${=}0.923{\pm}0.002$ (LightGBM, OOF evaluation) but yield only $+0.30$\,pp overall via construction ($+1.28$\,pp SciERC, $+0.02$\,pp Few-NERD).
sections/_archived/experiments_OLD.tex:251:Cross-dataset transfer is negative (Few-NERD: $-0.76$, $-1.02$\,pp; Appendix~\ref{app:verifier_transfer}), demonstrating dataset-specific feature mappings. This motivates distillation approaches using each dataset's own SC consensus as supervision.
sections/single_signal.tex:42:Few-NERD provides the clearest positive case: LP achieves $+1.39$\,pp ($p{<}0.001$; Holm $p_{\text{adj}}{=}0.021$, selection family $k{=}21$)\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\text{adj}}{=}0.055$ (BH $p_{\text{adj}}{=}0.003$).} at low degeneracy (13.0\% vs.\ 12.2--67.9\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\,pp; \S\ref{sec:fewnerd}).
sections/single_signal.tex:48:(3)~LP compression limits exploitation (Few-NERD within-instance $\rho{\approx}0.5$--$0.7$ vs.\ SciERC $\rho{\approx}0.26$).
sections/adaptive.tex:27:{\footnotesize $^\dagger$Few-NERD only; SciERC $+0.2$\,pp ($p{=}0.29$). $^\ddagger$Seed-sensitive ($\sigma{=}0.48$\,pp).}
sections/adaptive.tex:33:Combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (Few-NERD) yields $+0.42$\,pp over pure LLaMA ($p{<}0.001$, CI $[0.27, 0.58]$; $N{=}8$ total).
sections/abstract.tex:6:Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
sections/appendix.tex:233:[Omitted long matching line]
sections/appendix.tex:239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
sections/appendix.tex:248:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
sections/appendix.tex:338:6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ & \\
sections/appendix.tex:351:19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ & \\
sections/appendix.tex:358:24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ & \\
sections/appendix.tex:359:25 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\
sections/appendix.tex:364:30 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\
sections/appendix.tex:370:34 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\
sections/appendix.tex:385:45 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\
sections/appendix.tex:532:DeBERTa achieves $\rho{=}0.329{\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\pm}26.5$\% of the oracle gap (13 of 15 runs negative; vs.\ LP's $+4.2{\pm}10.7$\%); on Few-NERD, DeBERTa recovers only $+3.5$\% (single 80/20 split; vs.\ LP's $+16.3$\%).
sections/appendix.tex:540:In-domain OOF construction yields $+0.30$\,pp overall, with per-dataset gains of $+1.28$\,pp (SciERC), $+0.55$\,pp (CoNLL), and $+0.02$\,pp (Few-NERD).
sections/appendix.tex:541:The near-zero Few-NERD gain despite high AUC shows that frequency-based threshold construction already captures most of the verifier's signal.
sections/appendix.tex:542:Cross-dataset transfer to Few-NERD is negative: $-0.76$\,pp (B2-v2), $-1.02$\,pp (B2-v3), $-1.27$\,pp (B2-v4 Replace, AUC${=}0.822$), and $-0.85$\,pp (B2-v4 Augment, AUC${=}0.855$), all below greedy.
sections/appendix.tex:550:Unlike the entity-level probe in \S\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.
sections/appendix.tex:552:Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).
sections/appendix.tex:562:& \multicolumn{3}{c}{\textbf{SciERC}} & \multicolumn{2}{c}{\textbf{Few-NERD}} \\
sections/appendix.tex:577:On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\% vs.\ $12.3$\%).
sections/appendix.tex:578:A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\% vs.\ $55.8$\%); LP's bottleneck is not token aggregation.
sections/appendix.tex:592:Method & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\
sections/appendix.tex:611:[Omitted long matching line]
sections/appendix.tex:627:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; \S\ref{app:hidden_probe}).
sections/appendix.tex:629:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\to}$CoNLL) and $0.671$ (CoNLL${\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.
sections/appendix.tex:638:Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).
sections/appendix.tex:643:\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}
sections/appendix.tex:683:ESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\S\ref{sec:mechanistic}) generalizes.
sections/appendix.tex:696:FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
sections/appendix.tex:920:Few-NERD exhibits substantially stronger alignment ($\rho{=}0.667$) than SciERC ($\rho{=}0.262$), consistent with LP selection succeeding only on Few-NERD.
sections/appendix.tex:935:Few-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\% \\
sections/appendix.tex:943:\paragraph{Few-NERD LP compression threshold sensitivity.}\label{app:fewnerd_epsilon}
sections/appendix.tex:945:Tables~\ref{tab:fewnerd_epsilon} and \ref{tab:fewnerd_lp_bucket} extend the $\varepsilon$ analysis to Few-NERD ($n{=}32{,}565$, Qwen3-8B, $N{=}8$, seed${=}42$).
sections/appendix.tex:950:\caption{$\varepsilon$ threshold vs.\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\%: instances with LP range ${<}\varepsilon$. $\rho$: Spearman correlation between LP and oracle F1. $\varepsilon{=}0.05$ (bold) is the elbow.}
sections/appendix.tex:951:\label{tab:fewnerd_epsilon}
sections/appendix.tex:969:\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\geq}0.05$ show $3$--$6{\times}$ larger advantage.}
sections/appendix.tex:970:\label{tab:fewnerd_lp_bucket}
sections/appendix.tex:987:The LP-best advantage over MV shows a clear transition: compressed instances (LP range${<}0.05$) gain $+0.8$ to $+2.3$\,pp, while non-compressed instances gain $+3.6$ to $+5.8$\,pp (Table~\ref{tab:fewnerd_lp_bucket}).
sections/appendix.tex:1249:MV fails to improve F1 on any dataset: Few-NERD $\Delta{=}{-}2.74$\,pp, SciERC $-0.74$\,pp, CoNLL $-0.04$\,pp.
sections/appendix.tex:1252:Few-NERD and SciERC ($\alpha_{\textup{crit,eff}} {<} 1$) show significantly negative $\Delta$, indicating that even where structural headroom exists, marginal-entity precision is insufficient.
sections/appendix.tex:1253:SciERC's lower $\alpha_{\textup{crit}}$ ($0.334$, vs.\ $0.396$ for Few-NERD and $0.456$ for CoNLL) is consistent with it being the only dataset where a trained entity verifier (AUC${=}0.923$) achieves positive gain ($+1.28$\,pp).
sections/appendix.tex:1264:Few-NERD & 3 & .791 & .764 & .885 & $-2.74{\pm}0.54$ & 8.8\% & 0.396 & 0.434 & $\Delta < 0$ \\
sections/appendix.tex:1270:\noindent{\footnotesize $^*$CoNLL $\delta{=}60.3$\% (full test set, 3-seed) vs.\ $61.7$\% in Table~\ref{tab:fewnerd} (gold-filtered); the difference reflects filtering. Tab.~\ref{tab:pretrained_summary} reports $57$--$60$\% (seed range, finetuned).}
sections/appendix.tex:1365: & SciERC & CoNLL & Few-NERD \\
sections/appendix.tex:1381:\paragraph{Few-NERD NER free-form results.}
sections/appendix.tex:1382:On Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$), free-form decoding produces near-identical LP distributions (LP std ratio $1.00{\times}$) and unchanged degeneracy ($9.1$\%).
sections/appendix.tex:1502:\paragraph{Few-NERD $N$-scaling: MV at $N{=}16$.}
sections/appendix.tex:1503:On Few-NERD (Qwen3-8B, 3-seed), increasing from $N{=}8$ to $N{=}16$ reduces degeneracy ($8.8$\%$\to$$4.0{\pm}1.4$\%) and attenuates MV degradation ($-2.74$\,pp$\to$$-1.65{\pm}0.61$\,pp), but MV remains negative.
sections/appendix.tex:1526:\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$, seed 42). Values differ from Table~\ref{tab:selection} (0.645, 2-seed) and Table~\ref{tab:fewnerd} (0.663, 3-seed) due to seed and aggregation differences; relative trends are consistent.}
sections/appendix.tex:1558:The exponent $c$ varies with dataset complexity: FewNERD ($c{\approx}0.61$) scales comparably to reasoning-task estimates ($c{\approx}0.5$--$0.7$; \citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.
sections/appendix.tex:1584:FewNERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\
sections/appendix.tex:1587:FewNERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\
sections/appendix.tex:1599:\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
sections/appendix.tex:1609:Few-NERD & 7B FT$^\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\
sections/appendix.tex:1621:LP $\rho$ drops without fine-tuning (Table~\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).
sections/appendix.tex:1622:LP-weighted construction yields $+1.53$\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\% of headroom. Construction fails on Few-NERD ($-0.20$\,pp) and CoNLL ($-0.37$\,pp) where degeneracy exceeds $46$\%---consistent with FT-regime degeneracy gating.
sections/appendix.tex:1625:[Omitted long matching line]
sections/appendix.tex:1628:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\% vs.\ Qwen3-8B: $13.0$\%; Table~\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\to$5 epochs triples degeneracy within the same model (\S\ref{sec:fewnerd}).
sections/appendix.tex:1652:Qwen3-14B fine-tuned on Few-NERD achieves greedy F1${=}0.798$ ($+0.9$\,pp over 8B) with oracle headroom of 8.1\,pp ($+1.2$\,pp over 8B's 6.9\,pp) and $\rho$ advantage $+0.029$ over 8B.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "356de64e-0516-4b75-83c2-5f3f72dbed88",
  "tool_use_result": {
    "stdout": "sections/mechanistic.tex:5:[Omitted long matching line]\nsections/mechanistic.tex:21:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; Appendix~\\ref{app:hidden_probe}).\nsections/mechanistic.tex:23:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\\to}$CoNLL) and $0.671$ (CoNLL${\\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.\nsections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\nsections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.\nsections/checklist.tex:39:Yes. Instance counts are reported in Table~\\ref{tab:fewnerd} and throughout Section~\\ref{sec:experiments}. Gold-filtering counts, dataset sizes, and evaluation protocol details are in Section~\\ref{sec:evaluation}.\nsections/checklist.tex:54:Yes. We report multi-seed results (5 seeds; $\\sigma$ in Table~\\ref{tab:multiseed}), bootstrap 95\\% confidence intervals (Tables~\\ref{tab:selection}, \\ref{tab:fewnerd_full}), paired bootstrap $p$-values throughout, and minimum detectable effect sizes (Section~\\ref{sec:selection_gap}). Tables clearly indicate whether values are single-seed, multi-seed means, or confidence intervals.\nsections/method.tex:65:We evaluate across four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), two model families (Qwen3-8B, LLaMA-3.1-8B-Instruct), and $N \\in \\{2, \\ldots, 64\\}$ samples, with extensions to 4B/14B scale ablations, Qwen2.5-72B and GPT-5.5 zero-shot, RE, and SQL parsing (\\S\\ref{sec:experiments}).\nsections/theory.tex:7:We select $\\varepsilon{=}0.05$ at the elbow of the compression curve, where LP-best selection advantage transitions from $+1.5$\\,pp (compressed) to $+4.6$\\,pp (non-compressed; Appendix~\\ref{app:fewnerd_epsilon}).\nsections/theory.tex:11:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): Few-NERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, SciERC converges more slowly ($c{\\approx}0.35$), yet confidence-based aggregation recovers ${<}1$\\,pp---a persistent gap.\nsections/theory.tex:12:[Omitted long matching line]\nsections/theory.tex:13:Degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: $31.7$--$46.2$\\% vs.\\ Qwen3: $13.0$\\% vs.\\ GPT-5.5: $50$\\% on Few-NERD; Appendix~\\ref{app:cross_scale}).\nsections/theory.tex:24:Methods using $\\theta{=}2/N$ are most affected ($-3.09$\\,pp at $N{=}8$, $-6.90$\\,pp at $N{=}16$ vs.\\ greedy on Few-NERD); majority vote ($\\theta{=}\\tfrac{1}{2}$) reduces the delta to $-0.87$/$-0.60$\\,pp---severity reduction, not immunity (Table~\\ref{tab:theta_sweep}).\nsections/_archived/experiments_OLD.tex:10:\\textbf{Few-NERD} \\cite{ding2021fewnerd} (INTRA coarse; 37{,}648 instances, 8 entity types, ${\\approx}$75\\% F1) provides a low-degeneracy contrast where LP selection succeeds (\\S\\ref{sec:fewnerd}).\nsections/_archived/experiments_OLD.tex:15:\\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are LoRA fine-tuned using LLaMA Factory \\cite{zheng2024llamafactory} (training details in Appendix~\\ref{app:training}; Few-NERD uses 3 epochs vs.\\ 5 for others due to earlier convergence; Appendix~\\ref{app:epoch_confound}).\nsections/_archived/experiments_OLD.tex:97:On SciERC ($n{=}529$, 2-seed sign tests\\footnote{MDE${\\approx}$1.5~pp at 80\\% power ($n{=}529$); Few-NERD ($n{=}32{,}565$; MDE${\\approx}$0.22~pp) provides the definitive test.}), the oracle (0.775) reveals 13.0~pp of headroom, but LP achieves $+0.2$~pp ($p{=}0.29$), below the MDE (${\\approx}$1.5~pp); selection effects below this threshold cannot be reliably detected.\nsections/_archived/experiments_OLD.tex:99:Few-NERD provides the definitive contrast: LP achieves $+1.39$~pp ($p{<}0.001$) at low degeneracy (\\S\\ref{sec:fewnerd}), while structural signals still degrade selection.\nsections/_archived/experiments_OLD.tex:102:Three factors shape LP selection gains: (1)~\\textit{instance degeneracy} (SciERC 17.8\\%, CoNLL 61.7\\%; Table~\\ref{tab:fewnerd}); (2)~\\textit{oracle headroom} (CoNLL ${\\approx}4$\\,pp vs.\\ SciERC 13.0\\,pp); (3)~\\textit{LP-quality alignment} (Few-NERD $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nsections/_archived/experiments_OLD.tex:103:The pattern matches observations: Few-NERD (low degeneracy, strong alignment) yields $+1.39$\\,pp; SciERC (weak alignment) $+0.04{\\pm}0.48$\\,pp (3-seed; Table~\\ref{tab:multiseed}); CoNLL (high degeneracy) none; WNUT-17 shows reversed LP ($\\rho{=}{-}0.446$) yet QE remains effective (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}).\nsections/_archived/experiments_OLD.tex:104:The factors do not combine into a predictive model ($R^2{<}0$, 23 configurations) but each is supported by controlled ablations (\\S\\ref{sec:fewnerd}, \\S\\ref{sec:discussion}).\nsections/_archived/experiments_OLD.tex:107:\\subsection{Cross-Dataset Contrast: Few-NERD}\nsections/_archived/experiments_OLD.tex:108:\\label{sec:fewnerd}\nsections/_archived/experiments_OLD.tex:113:\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\nsections/_archived/experiments_OLD.tex:114:\\label{tab:fewnerd}\nsections/_archived/experiments_OLD.tex:123:Few-NERD & 32{,}565 & .748 & 13.0\\% & .220 & $\\mathbf{+1.39}$\\,pp & ${<}.001$ \\\\\nsections/_archived/experiments_OLD.tex:128:Few-NERD (Table~\\ref{tab:fewnerd}) confirms LP selection at low degeneracy ($+1.39$~pp, $p{<}0.001$; structural signals degrade: VC $-1.79$, SJ $-2.14$~pp), with LP 50$\\times$ more seed-stable ($\\sigma{=}0.04$ vs.\\ SJ $2.02$~pp), generalizing to LLaMA (Table~\\ref{tab:cross_selection}). Training convergence modulates degeneracy (5-epoch: $31$\\%, halving LP gains; Appendix~\\ref{app:epoch_confound}).\nsections/_archived/experiments_OLD.tex:136:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\nsections/_archived/experiments_OLD.tex:192:Few-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\nsections/_archived/experiments_OLD.tex:202:LP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all datasets. Structural signals generalize (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); this comparison simultaneously varies model family, regime, and quantization, so individual effects cannot be disentangled.\nsections/_archived/experiments_OLD.tex:203:LP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\nsections/_archived/experiments_OLD.tex:206:[Omitted long matching line]\nsections/_archived/experiments_OLD.tex:209:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\\% vs.\\ Qwen3-8B: $13.0$\\%; Table~\\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\\to$5 epochs triples degeneracy within the same model (\\S\\ref{sec:fewnerd}).\nsections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\nsections/_archived/experiments_OLD.tex:236:Few-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001^\\dagger$ \\\\\nsections/_archived/experiments_OLD.tex:244:LP-weighted construction improves on Few-NERD ($+1.40{\\pm}0.51$\\,pp, $p{<}0.001$; survives Holm--Bonferroni at $k{=}57$) and SciERC ($+1.02{\\pm}0.49$\\,pp, $p{=}0.004$, $p_{\\text{adj}}{=}0.20$; Table~\\ref{tab:entity_construction}), recovering 8--11\\% of oracle headroom. CoNLL shows no gain ($-0.39$\\,pp), consistent with high degeneracy ($N$-scaling in Appendix~\\ref{app:n_scaling}).\nsections/_archived/experiments_OLD.tex:247:Construction and LP selection are complementary, governed by $\\rho_{\\text{adj}}$: Few-NERD ($\\rho_{\\text{adj}}{=}0.516$) favors both, while SciERC ($\\rho_{\\text{adj}}{=}0.167$) favors construction only. A three-way routing protocol ($\\rho_{\\text{adj}} \\geq 0.3$: LP; $<0.3$ with positive construction: construction; else: greedy) is stable across $\\tau{\\in}[0.2, 0.4]$.\nsections/_archived/experiments_OLD.tex:250:Entity verification features achieve AUC${=}0.923{\\pm}0.002$ (LightGBM, OOF evaluation) but yield only $+0.30$\\,pp overall via construction ($+1.28$\\,pp SciERC, $+0.02$\\,pp Few-NERD).\nsections/_archived/experiments_OLD.tex:251:Cross-dataset transfer is negative (Few-NERD: $-0.76$, $-1.02$\\,pp; Appendix~\\ref{app:verifier_transfer}), demonstrating dataset-specific feature mappings. This motivates distillation approaches using each dataset's own SC consensus as supervision.\nsections/single_signal.tex:42:Few-NERD provides the clearest positive case: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.055$ (BH $p_{\\text{adj}}{=}0.003$).} at low degeneracy (13.0\\% vs.\\ 12.2--67.9\\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\\,pp; \\S\\ref{sec:fewnerd}).\nsections/single_signal.tex:48:(3)~LP compression limits exploitation (Few-NERD within-instance $\\rho{\\approx}0.5$--$0.7$ vs.\\ SciERC $\\rho{\\approx}0.26$).\nsections/adaptive.tex:27:{\\footnotesize $^\\dagger$Few-NERD only; SciERC $+0.2$\\,pp ($p{=}0.29$). $^\\ddagger$Seed-sensitive ($\\sigma{=}0.48$\\,pp).}\nsections/adaptive.tex:33:Combining 4 samples each from Qwen3-8B and LLaMA-3.1-8B (Few-NERD) yields $+0.42$\\,pp over pure LLaMA ($p{<}0.001$, CI $[0.27, 0.58]$; $N{=}8$ total).\nsections/abstract.tex:6:Entity-level construction yields conditional gains ($+1.40$\\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.\nsections/appendix.tex:233:[Omitted long matching line]\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:248:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\nsections/appendix.tex:338:6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:351:19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:358:24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ & \\\\\nsections/appendix.tex:359:25 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\nsections/appendix.tex:364:30 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\nsections/appendix.tex:370:34 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\nsections/appendix.tex:385:45 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\nsections/appendix.tex:532:DeBERTa achieves $\\rho{=}0.329{\\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\\pm}26.5$\\% of the oracle gap (13 of 15 runs negative; vs.\\ LP's $+4.2{\\pm}10.7$\\%); on Few-NERD, DeBERTa recovers only $+3.5$\\% (single 80/20 split; vs.\\ LP's $+16.3$\\%).\nsections/appendix.tex:540:In-domain OOF construction yields $+0.30$\\,pp overall, with per-dataset gains of $+1.28$\\,pp (SciERC), $+0.55$\\,pp (CoNLL), and $+0.02$\\,pp (Few-NERD).\nsections/appendix.tex:541:The near-zero Few-NERD gain despite high AUC shows that frequency-based threshold construction already captures most of the verifier's signal.\nsections/appendix.tex:542:Cross-dataset transfer to Few-NERD is negative: $-0.76$\\,pp (B2-v2), $-1.02$\\,pp (B2-v3), $-1.27$\\,pp (B2-v4 Replace, AUC${=}0.822$), and $-0.85$\\,pp (B2-v4 Augment, AUC${=}0.855$), all below greedy.\nsections/appendix.tex:550:Unlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\nsections/appendix.tex:552:Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).\nsections/appendix.tex:562:& \\multicolumn{3}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{Few-NERD}} \\\\\nsections/appendix.tex:577:On Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\\% vs.\\ $12.3$\\%).\nsections/appendix.tex:578:A learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%); LP's bottleneck is not token aggregation.\nsections/appendix.tex:592:Method & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\nsections/appendix.tex:611:[Omitted long matching line]\nsections/appendix.tex:627:A logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; \\S\\ref{app:hidden_probe}).\nsections/appendix.tex:629:Cross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\\to}$CoNLL) and $0.671$ (CoNLL${\\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.\nsections/appendix.tex:638:Three independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).\nsections/appendix.tex:643:\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\nsections/appendix.tex:683:ESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\\S\\ref{sec:mechanistic}) generalizes.\nsections/appendix.tex:696:FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\nsections/appendix.tex:920:Few-NERD exhibits substantially stronger alignment ($\\rho{=}0.667$) than SciERC ($\\rho{=}0.262$), consistent with LP selection succeeding only on Few-NERD.\nsections/appendix.tex:935:Few-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\\% \\\\\nsections/appendix.tex:943:\\paragraph{Few-NERD LP compression threshold sensitivity.}\\label{app:fewnerd_epsilon}\nsections/appendix.tex:945:Tables~\\ref{tab:fewnerd_epsilon} and \\ref{tab:fewnerd_lp_bucket} extend the $\\varepsilon$ analysis to Few-NERD ($n{=}32{,}565$, Qwen3-8B, $N{=}8$, seed${=}42$).\nsections/appendix.tex:950:\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\nsections/appendix.tex:951:\\label{tab:fewnerd_epsilon}\nsections/appendix.tex:969:\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\nsections/appendix.tex:970:\\label{tab:fewnerd_lp_bucket}\nsections/appendix.tex:987:The LP-best advantage over MV shows a clear transition: compressed instances (LP range${<}0.05$) gain $+0.8$ to $+2.3$\\,pp, while non-compressed instances gain $+3.6$ to $+5.8$\\,pp (Table~\\ref{tab:fewnerd_lp_bucket}).\nsections/appendix.tex:1249:MV fails to improve F1 on any dataset: Few-NERD $\\Delta{=}{-}2.74$\\,pp, SciERC $-0.74$\\,pp, CoNLL $-0.04$\\,pp.\nsections/appendix.tex:1252:Few-NERD and SciERC ($\\alpha_{\\textup{crit,eff}} {<} 1$) show significantly negative $\\Delta$, indicating that even where structural headroom exists, marginal-entity precision is insufficient.\nsections/appendix.tex:1253:SciERC's lower $\\alpha_{\\textup{crit}}$ ($0.334$, vs.\\ $0.396$ for Few-NERD and $0.456$ for CoNLL) is consistent with it being the only dataset where a trained entity verifier (AUC${=}0.923$) achieves positive gain ($+1.28$\\,pp).\nsections/appendix.tex:1264:Few-NERD & 3 & .791 & .764 & .885 & $-2.74{\\pm}0.54$ & 8.8\\% & 0.396 & 0.434 & $\\Delta < 0$ \\\\\nsections/appendix.tex:1270:\\noindent{\\footnotesize $^*$CoNLL $\\delta{=}60.3$\\% (full test set, 3-seed) vs.\\ $61.7$\\% in Table~\\ref{tab:fewnerd} (gold-filtered); the difference reflects filtering. Tab.~\\ref{tab:pretrained_summary} reports $57$--$60$\\% (seed range, finetuned).}\nsections/appendix.tex:1365: & SciERC & CoNLL & Few-NERD \\\\\nsections/appendix.tex:1381:\\paragraph{Few-NERD NER free-form results.}\nsections/appendix.tex:1382:On Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$), free-form decoding produces near-identical LP distributions (LP std ratio $1.00{\\times}$) and unchanged degeneracy ($9.1$\\%).\nsections/appendix.tex:1502:\\paragraph{Few-NERD $N$-scaling: MV at $N{=}16$.}\nsections/appendix.tex:1503:On Few-NERD (Qwen3-8B, 3-seed), increasing from $N{=}8$ to $N{=}16$ reduces degeneracy ($8.8$\\%$\\to$$4.0{\\pm}1.4$\\%) and attenuates MV degradation ($-2.74$\\,pp$\\to$$-1.65{\\pm}0.61$\\,pp), but MV remains negative.\nsections/appendix.tex:1526:\\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$, seed 42). Values differ from Table~\\ref{tab:selection} (0.645, 2-seed) and Table~\\ref{tab:fewnerd} (0.663, 3-seed) due to seed and aggregation differences; relative trends are consistent.}\nsections/appendix.tex:1558:The exponent $c$ varies with dataset complexity: FewNERD ($c{\\approx}0.61$) scales comparably to reasoning-task estimates ($c{\\approx}0.5$--$0.7$; \\citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.\nsections/appendix.tex:1584:FewNERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:1587:FewNERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1609:Few-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\nsections/appendix.tex:1621:LP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).\nsections/appendix.tex:1622:LP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\nsections/appendix.tex:1625:[Omitted long matching line]\nsections/appendix.tex:1628:Qwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\\% vs.\\ Qwen3-8B: $13.0$\\%; Table~\\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\\to$5 epochs triples degeneracy within the same model (\\S\\ref{sec:fewnerd}).\nsections/appendix.tex:1652:Qwen3-14B fine-tuned on Few-NERD achieves greedy F1${=}0.798$ ($+0.9$\\,pp over 8B) with oracle headroom of 8.1\\,pp ($+1.2$\\,pp over 8B's 6.9\\,pp) and $\\rho$ advantage $+0.029$ over 8B.",
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

_source line 64_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "145cc836-1aa5-4781-9c55-3bb0efc89ca1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PYm6t16hPCGQkWbNn3q2F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11921,
      "cache_read_input_tokens": 54115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11921
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

### Assistant

_source line 65_

Found "FewNERD" usages that should be "Few-NERD". Let me check each:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d4ced517-d981-454d-b786-4ac8c79d516e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PYm6t16hPCGQkWbNn3q2F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11921,
      "cache_read_input_tokens": 54115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11921
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

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — Grep · `toolu_01KY3PtkmufkQNUMmwp4GHXD`</summary>

```json
{
  "pattern": "FewNERD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "4ea9b764-4353-459b-9f5c-a45c76af019c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PYm6t16hPCGQkWbNn3q2F8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11921,
      "cache_read_input_tokens": 54115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11921
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

### Tool result

_source line 67 · 2026-05-24T01:36:49.317Z_

<details><summary>↩ Tool result · `toolu_01KY3PtkmufkQNUMmwp4GHXD`</summary>

```text
sections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \cdot N^{-c}$ ($R^2 > 0.999$; Figure~\ref{fig:oracle_scaling}): FewNERD ($c{\approx}0.61$) scales comparably to reasoning tasks \cite{brown2024monkeys}, while SciERC converges more slowly ($c{\approx}0.35$); a single stochastic sample underperforms greedy ($N{\geq}4$ needed to match).
sections/appendix.tex:233:[Omitted long matching line]
sections/appendix.tex:239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
sections/appendix.tex:248:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
sections/appendix.tex:550:Unlike the entity-level probe in \S\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.
sections/appendix.tex:696:FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
sections/appendix.tex:1558:The exponent $c$ varies with dataset complexity: FewNERD ($c{\approx}0.61$) scales comparably to reasoning-task estimates ($c{\approx}0.5$--$0.7$; \citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.
sections/appendix.tex:1584:FewNERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\
sections/appendix.tex:1587:FewNERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\
sections/appendix.tex:2379:FewNERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\
sections/appendix.tex:2380:FewNERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "199d8dd4-bb99-493b-b9c8-1707c15d4b47",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/_archived/experiments_OLD.tex:211:Oracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$ ($R^2 > 0.999$; Figure~\\ref{fig:oracle_scaling}): FewNERD ($c{\\approx}0.61$) scales comparably to reasoning tasks \\cite{brown2024monkeys}, while SciERC converges more slowly ($c{\\approx}0.35$); a single stochastic sample underperforms greedy ($N{\\geq}4$ needed to match).\nsections/appendix.tex:233:[Omitted long matching line]\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:248:LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\nsections/appendix.tex:550:Unlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\nsections/appendix.tex:696:FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\nsections/appendix.tex:1558:The exponent $c$ varies with dataset complexity: FewNERD ($c{\\approx}0.61$) scales comparably to reasoning-task estimates ($c{\\approx}0.5$--$0.7$; \\citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.\nsections/appendix.tex:1584:FewNERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:1587:FewNERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\\\\nsections/appendix.tex:2379:FewNERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\\\\nsections/appendix.tex:2380:FewNERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\\\",
    "numLines": 11
  }
}
```

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "bee58042-3acd-44b8-a53c-aab001d4a57d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VECh18c83Thd9xM6yDpims",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 66036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Read · `toolu_01Xati3ZjGr3HhKL2qttdxvH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 696,
  "limit": 5
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "bd8998da-c423-436e-8c7c-10468fec02a2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VECh18c83Thd9xM6yDpims",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1666,
      "cache_read_input_tokens": 66036,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1666
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

_source line 70 · 2026-05-24T01:36:58.366Z_

<details><summary>↩ Tool result · `toolu_01Xati3ZjGr3HhKL2qttdxvH`</summary>

```text
696	FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
697	\bottomrule
698	\end{tabular}
699	\end{table}
700	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "64799e50-4d94-412f-b37a-0e98dc56296b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n",
      "numLines": 5,
      "startLine": 696,
      "totalLines": 2569
    }
  }
}
```

</details>

---

### Tool call

_source line 71_

<details open><summary>🔧 Tool call — Bash · `toolu_014iTLXSbu17mcCH4UJ5aqoM`</summary>

```json
{
  "command": "grep -c \"FewNERD\" /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "description": "Count FewNERD in appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "04738685-fb69-4a85-a9ae-5967ae734849",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013aipURcPVWWEdjfFTUkE4a",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 557,
      "cache_read_input_tokens": 67702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 557
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 72 · 2026-05-24T01:37:01.788Z_

<details><summary>↩ Tool result · `toolu_014iTLXSbu17mcCH4UJ5aqoM`</summary>

```text
10
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "95269764-16c5-4c8f-88e3-445571813694",
  "tool_use_result": {
    "stdout": "10",
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

_source line 73_

<details open><summary>🔧 Tool call — Bash · `toolu_01Kcs8e79JYxfyL12CoEjeft`</summary>

```json
{
  "command": "sed -i 's/FewNERD/Few-NERD/g' sections/appendix.tex && grep -c \"FewNERD\" sections/appendix.tex && echo \"After:\" && grep -c \"Few-NERD\" sections/appendix.tex",
  "description": "Replace FewNERD with Few-NERD in appendix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1207ecbb-5db6-468b-ac9c-f0f43f79417b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FeFPksbTBUDrBpWCg6ADCb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 175,
      "cache_read_input_tokens": 68259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 175
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

_source line 74 · 2026-05-24T01:37:05.272Z_

<details><summary>↩ Tool result · `toolu_01Kcs8e79JYxfyL12CoEjeft`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "4a94fa83-ef55-457b-ac1b-3f10d0ddca33",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 75_

<details open><summary>🔧 Tool call — Bash · `toolu_01SHcdJnN3529SMDCcnfJsFv`</summary>

```json
{
  "command": "grep -c \"Few-NERD\" sections/appendix.tex",
  "description": "Verify Few-NERD count after replacement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c19f1ffd-94b4-4b04-9b71-a9e530460ab5",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01U2iPxkKwJS9UAD3T21dSQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 550,
      "cache_read_input_tokens": 68434,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 550
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

_source line 76 · 2026-05-24T01:37:07.636Z_

<details><summary>↩ Tool result · `toolu_01SHcdJnN3529SMDCcnfJsFv`</summary>

```text
91
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "daa7f747-ad6a-42df-8b2b-f91727ebd4db",
  "tool_use_result": {
    "stdout": "91",
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

_source line 77_

<details open><summary>🔧 Tool call — Grep · `toolu_01Xa4FLHCTiaVAZ1EUhBN5rj`</summary>

```json
{
  "pattern": "WNUT",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex",
  "head_limit": 40
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b9ed4add-aac8-4e9d-9f17-561b0ca1a6bf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RURTSfKAj9DCiJiieTkFao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 130,
      "cache_read_input_tokens": 68984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 130
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

### Tool result

_source line 78 · 2026-05-24T01:37:12.127Z_

<details><summary>↩ Tool result · `toolu_01Xa4FLHCTiaVAZ1EUhBN5rj`</summary>

```text
sections/checklist.tex:24:Yes. All datasets are cited: SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, Few-NERD \cite{ding2021fewnerd}, WNUT-17 \cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \cite{zheng2024llamafactory}. Constrained decoding: XGrammar \cite{dong2024xgrammar}. See Sections~\ref{sec:introduction}, \ref{sec:evaluation}, and Appendix~\ref{app:training}.
sections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.
sections/method.tex:65:We evaluate across four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), two model families (Qwen3-8B, LLaMA-3.1-8B-Instruct), and $N \in \{2, \ldots, 64\}$ samples, with extensions to 4B/14B scale ablations, Qwen2.5-72B and GPT-5.5 zero-shot, RE, and SQL parsing (\S\ref{sec:experiments}).
sections/_archived/experiments_OLD.tex:12:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 51\% zero F1) probes the signal-collapse boundary where model capability is insufficient.
sections/_archived/experiments_OLD.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ at $N{=}16$, but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
sections/_archived/experiments_OLD.tex:49:%% WNUT collapse detail moved to keep main text concise; see Table~\ref{tab:wnut}.
sections/_archived/experiments_OLD.tex:98:The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \textit{degradation} (Appendix~\ref{app:tost}).
sections/_archived/experiments_OLD.tex:103:The pattern matches observations: Few-NERD (low degeneracy, strong alignment) yields $+1.39$\,pp; SciERC (weak alignment) $+0.04{\pm}0.48$\,pp (3-seed; Table~\ref{tab:multiseed}); CoNLL (high degeneracy) none; WNUT-17 shows reversed LP ($\rho{=}{-}0.446$) yet QE remains effective (VC $\rho{=}0.724$, $N{=}16$; Table~\ref{tab:wnut}).
sections/_archived/experiments_OLD.tex:120:WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
sections/single_signal.tex:41:The pattern holds across CoNLL and WNUT-17 (Table~\ref{tab:cross_selection}).
sections/appendix.tex:156:Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
sections/appendix.tex:207:\paragraph{WNUT-17 full signal analysis.}
sections/appendix.tex:208:Table~\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\rho$.
sections/appendix.tex:213:\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
sections/appendix.tex:336:4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\
sections/appendix.tex:400:56 & & WNUT-17 conditional $\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\
sections/appendix.tex:401:57 & & WNUT-17 conditional $\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\
sections/appendix.tex:415:WNUT-17 shows 55\% identical outputs, attributable to the 53.7\% zero-F1 rate.
sections/appendix.tex:430:WNUT-17 & 55\% & --- \\
sections/appendix.tex:764:CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
sections/appendix.tex:784:[Omitted long matching line]
sections/appendix.tex:801:CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\texttt{enable\_thinking=False}).
sections/appendix.tex:1857:These negative correlations reflect the model systematically generating confident but incorrect outputs, a capability failure analogous to WNUT-17 (\S\ref{sec:qe_results}) and not evidence against signal utility.
sections/appendix.tex:1861:This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.
sections/experiments_main.tex:10:\textbf{WNUT-17} \cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\% zero F1) probes the signal-collapse boundary.
sections/experiments_main.tex:53:At the signal-collapse boundary (WNUT-17, F1${\approx}$42\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\rho{=}0.724$ at $N{=}16$, but conditional $\rho{=}0.038$; Table~\ref{tab:wnut}); LP shows the reverse (conditional $\rho{=}0.350$; Figure~\ref{fig:signal_heatmap}).
sections/experiments_main.tex:68:WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "0d3f9df6-9551-4af6-b72c-ebb1f1affad5",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/checklist.tex:24:Yes. All datasets are cited: SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, Few-NERD \\cite{ding2021fewnerd}, WNUT-17 \\cite{derczynski2017wnut}. Models: Qwen3-8B/4B and LLaMA-3.1-8B-Instruct. Training framework: LLaMA Factory \\cite{zheng2024llamafactory}. Constrained decoding: XGrammar \\cite{dong2024xgrammar}. See Sections~\\ref{sec:introduction}, \\ref{sec:evaluation}, and Appendix~\\ref{app:training}.\nsections/checklist.tex:27:Partially. CoNLL-2003 is derived from the Reuters RCV1 corpus, available under a NIST agreement for research. SciERC, Few-NERD, and WNUT-17 are publicly available research benchmarks. Qwen3 and LLaMA-3.1 are open-weight models released under their respective licenses (Qwen License, Llama 3.1 Community License). Code and data will be released upon acceptance.\nsections/method.tex:65:We evaluate across four NER benchmarks spanning a difficulty gradient (SciERC, Few-NERD, CoNLL, WNUT-17), two model families (Qwen3-8B, LLaMA-3.1-8B-Instruct), and $N \\in \\{2, \\ldots, 64\\}$ samples, with extensions to 4B/14B scale ablations, Qwen2.5-72B and GPT-5.5 zero-shot, RE, and SQL parsing (\\S\\ref{sec:experiments}).\nsections/_archived/experiments_OLD.tex:12:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 51\\% zero F1) probes the signal-collapse boundary where model capability is insufficient.\nsections/_archived/experiments_OLD.tex:48:At the signal-collapse boundary (WNUT-17, macro F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ at $N{=}16$, but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nsections/_archived/experiments_OLD.tex:49:%% WNUT collapse detail moved to keep main text concise; see Table~\\ref{tab:wnut}.\nsections/_archived/experiments_OLD.tex:98:The pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}); under stringent TOST anchors, some configurations show significant \\textit{degradation} (Appendix~\\ref{app:tost}).\nsections/_archived/experiments_OLD.tex:103:The pattern matches observations: Few-NERD (low degeneracy, strong alignment) yields $+1.39$\\,pp; SciERC (weak alignment) $+0.04{\\pm}0.48$\\,pp (3-seed; Table~\\ref{tab:multiseed}); CoNLL (high degeneracy) none; WNUT-17 shows reversed LP ($\\rho{=}{-}0.446$) yet QE remains effective (VC $\\rho{=}0.724$, $N{=}16$; Table~\\ref{tab:wnut}).\nsections/_archived/experiments_OLD.tex:120:WNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nsections/single_signal.tex:41:The pattern holds across CoNLL and WNUT-17 (Table~\\ref{tab:cross_selection}).\nsections/appendix.tex:156:Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\nsections/appendix.tex:207:\\paragraph{WNUT-17 full signal analysis.}\nsections/appendix.tex:208:Table~\\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\nsections/appendix.tex:213:\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\nsections/appendix.tex:336:4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\nsections/appendix.tex:400:56 & & WNUT-17 conditional $\\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\\\\nsections/appendix.tex:401:57 & & WNUT-17 conditional $\\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\\\\nsections/appendix.tex:415:WNUT-17 shows 55\\% identical outputs, attributable to the 53.7\\% zero-F1 rate.\nsections/appendix.tex:430:WNUT-17 & 55\\% & --- \\\\\nsections/appendix.tex:764:CoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\nsections/appendix.tex:784:[Omitted long matching line]\nsections/appendix.tex:801:CoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nsections/appendix.tex:1857:These negative correlations reflect the model systematically generating confident but incorrect outputs, a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}) and not evidence against signal utility.\nsections/appendix.tex:1861:This extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\nsections/experiments_main.tex:10:\\textbf{WNUT-17} \\cite{derczynski2017wnut} (1{,}287 social media instances, 53.7\\% zero F1) probes the signal-collapse boundary.\nsections/experiments_main.tex:53:At the signal-collapse boundary (WNUT-17, F1${\\approx}$42\\%), full-set correlations are dominated by the zero/non-zero boundary (VC $\\rho{=}0.724$ at $N{=}16$, but conditional $\\rho{=}0.038$; Table~\\ref{tab:wnut}); LP shows the reverse (conditional $\\rho{=}0.350$; Figure~\\ref{fig:signal_heatmap}).\nsections/experiments_main.tex:68:WNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\",
    "numLines": 27
  }
}
```

</details>

---

### Tool call

_source line 79_

<details open><summary>🔧 Tool call — Grep · `toolu_017GFfuggMmTwQB8UKaY7k4S`</summary>

```json
{
  "pattern": "CoNLL|conll",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "files_with_matches",
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1e4b4074-eb6a-48c3-9535-e1994949e8cf",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RURTSfKAj9DCiJiieTkFao",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 130,
      "cache_read_input_tokens": 68984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 130
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

### Tool result

_source line 80 · 2026-05-24T01:37:13.371Z_

<details><summary>↩ Tool result · `toolu_017GFfuggMmTwQB8UKaY7k4S`</summary>

```text
Found 10 files
sections/appendix.tex
sections/single_signal.tex
sections/introduction.tex
sections/experiments_main.tex
sections/checklist.tex
sections/theory.tex
sections/method.tex
sections/diagnostic.tex
sections/mechanistic.tex
sections/_archived/experiments_OLD.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1a91869a-f18c-43a7-9911-58c5c3d314a4",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "sections/appendix.tex",
      "sections/single_signal.tex",
      "sections/introduction.tex",
      "sections/experiments_main.tex",
      "sections/checklist.tex",
      "sections/theory.tex",
      "sections/method.tex",
      "sections/diagnostic.tex",
      "sections/mechanistic.tex",
      "sections/_archived/experiments_OLD.tex"
    ],
    "numFiles": 10
  }
}
```

</details>

---

### Assistant

_source line 81_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "eebf71bf-72f2-4444-9d05-f1b751a75c5b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BQDs1aqUndCRZEENLY5VuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3141,
      "cache_read_input_tokens": 69114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3141
      },
      "output_tokens": 76,
      "service_tier": "standard",
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

_source line 82_

<details open><summary>🔧 Tool call — Read · `toolu_01Rm8fNwVq7c1C6emCAbmZvz`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 760,
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "9e8b405b-0c94-462b-a84c-7184d83bbe43",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01BQDs1aqUndCRZEENLY5VuX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3141,
      "cache_read_input_tokens": 69114,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3141
      },
      "output_tokens": 76,
      "service_tier": "standard",
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

_source line 83 · 2026-05-24T01:37:20.124Z_

<details><summary>↩ Tool result · `toolu_01Rm8fNwVq7c1C6emCAbmZvz`</summary>

```text
760	Framework & LLaMA Factory \\
761	\midrule
762	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
763	SciERC split & 1861 / 275 / 551 \\
764	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
765	& eval\_steps${=}$200, save\_limit${=}$5 \\
766	\bottomrule
767	\end{tabular}
768	}
769	\end{table}
770	
771	\paragraph{Prompt template.}
772	For NER, we use a structured prompt:
773	\begin{quote}
774	\small
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "994496db-e7ef-478f-b664-48733077b4aa",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "Framework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small",
      "numLines": 15,
      "startLine": 760,
      "totalLines": 2569
    }
  }
}
```

</details>

---

### Tool call

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_01EuZrkUNbnEm2HcgSGHDdZP`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "old_string": "CoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\",
  "new_string": "CoNLL / WNUT-17 & +\\,load\\_best\\_model\\_at\\_end, \\\\"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "19888f94-d7a8-4fcf-9ddd-2b5ca5f55282",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RNEVgMAyvomdAh3J6uucc4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 543,
      "cache_read_input_tokens": 72255,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 543
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

_source line 85 · 2026-05-24T01:37:23.241Z_

<details><summary>↩ Tool result · `toolu_01EuZrkUNbnEm2HcgSGHDdZP`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "99259469-a47e-47f7-80bd-80bed4d65b8e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
    "oldString": "CoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\",
    "newString": "CoNLL / WNUT-17 & +\\,load\\_best\\_model\\_at\\_end, \\\\",
    "originalFile": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\nWe exclude instances with empty gold annotations from all correlation analyses (CoNLL: 697/3{,}453 instances, 20.2\\%; SciERC: 22/551, 4.0\\%).\nFor these instances, F1 is trivially zero regardless of prediction quality, and consistency signals reflect agreement on the empty set rather than extraction quality. Including them inflates or deflates Spearman $\\rho$ depending on signal behavior at the boundary.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.364 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.289 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\quad LP & $T{=}0.7$ & 0.249 & --- \\\\\n\\quad LP & $T{=}1.0$ & 0.205 & 0.266 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.411$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.283 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.474{\\pm}0.009$ & --- \\\\\n\\quad FK &  & $0.467{\\pm}0.009$ & --- \\\\\n\\quad EM &  & $0.473{\\pm}0.010$ & --- \\\\\n\\quad VC &  & $0.470{\\pm}0.006$ & --- \\\\\n\\quad LP &  & $0.311{\\pm}0.003$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.364 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.004.\nFK NER $\\rho$ drops by 0.022, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nLP exhibits the largest temperature effect on NER ($\\rho{=}0.249$ at $T{=}0.7$ vs.\\ $0.205$ at $T{=}1.0$, $\\Delta{=}{+}0.044$), consistent with lower temperature concentrating probability mass and improving LP's discriminative power for quality estimation; RE $T{=}0.7$ LP data is not available.\nAcross all comparisons, the signal hierarchy is preserved at both temperatures on NER (SJ${>}$FK${>}$LP at $T{=}0.7$: $0.364{>}0.289{>}0.249$; at $T{=}1.0$: $0.360{>}0.267{>}0.205$).\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from $0.356{\\pm}0.014$ (5 seeds) to $0.411{\\pm}0.010$ (three seeds: 0.398, 0.423, 0.410), a gain of $+0.055$.\nThe magnitude of $N$-scaling gains is setting-dependent (LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$), though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.042$ (range: $+0.039$ to $+0.044$) while LP gains only $+0.004$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is seed-dependent: Qwen SciERC gains range from $+0.005$ to $+0.023$ across seeds (mean $+0.016$), while LLaMA CoNLL yields $+0.039$ (3-seed mean); individual seed FK shifts vary substantially under the unified pipeline, so this should not be interpreted as a robust trend.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.030$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.034$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows seed-dependent variation that does not constitute a reliable trend, structural and binary-agreement signals are the most robust to $N$.\nAt $N{=}16$, SJ converges to comparable NER performance with VC ($\\Delta{=}0.002$) while exhibiting lower cross-seed variance ($\\sigma{=}0.010$ vs.\\ $0.026$), a more stable alternative at higher sample sizes.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct shows a similar SJ--FK ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$, $\\Delta\\rho{=}0.069$; permutation $p{=}0.06$, borderline).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested NER settings: Qwen SciERC (VC $\\rho{=}0.409$ vs.\\ LP 0.239, $\\Delta{=}{+}0.170$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$),\\footnote{Qwen CoNLL $N{=}16$ was not recomputed under the unified pipeline; LP $\\rho{=}0.328$ may differ slightly from the registry value (0.315) due to instance filtering.} LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.474{\\pm}0.009$ vs.\\ LP $0.311{\\pm}0.003$, $\\Delta{=}{+}0.163$).\n\n\\paragraph{FK independence: instance-level permutation test.}\\label{app:fk_independence}\n\nTo verify that Fleiss' $\\kappa$ reflects genuine within-instance agreement rather than marginal-rate artifacts, we conduct instance-level permutation tests across three configurations.\nFor each instance, we permute sample labels 10{,}000 times to generate a null distribution of FK under independence, then compare the observed FK against this null via a one-sample $t$-test and permutation $p$-value.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\n\\label{tab:fk_independence}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lrcccc}\n\\toprule\nConfig & $n$ & FK mean & 95\\% CI & $t$ & Split-half $r$ \\\\\n\\midrule\nSciERC (Qwen) & 529 & 0.402 & [0.376, 0.428] & 30.8 & 0.395 \\\\\nCoNLL (LLaMA) & 2{,}756 & 0.927 & [0.919, 0.935] & 225.9 & 0.578 \\\\\nCoNLL (Qwen) & 2{,}756 & 0.720 & [0.706, 0.734] & 102.1 & 0.520 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nTable~\\ref{tab:fk_independence} reports the results.\nAll configurations reject the independence null at $p{<}0.001$ ($n{=}529$--$2{,}756$), FK captures genuine inter-sample agreement rather than chance label co-occurrence.\nSplit-half reliability ranges from $r{=}0.395$ (SciERC) to $r{=}0.578$ (CoNLL LLaMA), moderate stability: FK estimates from half the samples correlate positively with those from the other half, though the SciERC value suggests noisier estimation on harder tasks with fewer samples.\nThe higher FK means on CoNLL ($0.720$--$0.927$) vs.\\ SciERC ($0.402$) mirror the difficulty gradient observed in the main quality estimation results.\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives. This is a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$): longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$, all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$; the two selection rules are equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{SJ normalizer robustness.}\nEquation~\\ref{eq:sj} uses $\\max(|g_i|, |g_j|)$ as the denominator; an alternative is the union size $|g_i \\cup g_j|$.\nTable~\\ref{tab:sj_normalizer} compares the two normalizers across all six model--dataset combinations ($N{=}8$, $T{=}1.0$, seed${=}42$): $|\\Delta\\rho|{<}0.01$ in every case, the choice between max and union normalization does not affect conclusions.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\n\\label{tab:sj_normalizer}\n\\begin{tabular}{@{}ll ccc@{}}\n\\toprule\nDataset & Model & $\\rho$(max) & $\\rho$(union) & $\\Delta\\rho$ \\\\\n\\midrule\nCoNLL & Qwen3-8B & .436 & .438 & $-$.002 \\\\\nCoNLL & Qwen3-4B & .422 & .421 & $+$.000 \\\\\nCoNLL & LLaMA-8B & .431 & .432 & $-$.000 \\\\\nSciERC & Qwen3-8B & .360 & .365 & $-$.005 \\\\\nSciERC & Qwen3-4B & .422 & .423 & $-$.001 \\\\\nSciERC & LLaMA-8B & .363 & .372 & $-$.009 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, consistent with the NER structural advantage; on full-set RE, however, the SJ--FK difference is non-significant ($\\Delta\\rho{=}{-}0.005$, $p{=}0.53$; preliminary).\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations: SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$). This holds despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set, where the model demonstrably produces varied outputs, exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17 with full-set and conditional $\\rho$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\n\\label{tab:wnut}\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & .913 & .038 & .487 \\\\\nFK      & .125 & .555 & .169 & .002 \\\\\nSJ      & .089 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nThe full-set $p$-values are: VC ${<}$1e-112, FK $p{=}0.001$, SJ $p{=}0.020$, EM $p{=}0.194$, LP ${<}$1e-28.\nVC's high full-set $\\rho{=}0.724$ is entirely attributable to the zero/non-zero boundary (conditional $\\rho{=}0.038$, $p{=}0.49$), while LP's conditional $\\rho{=}0.350$ is the highest among all signals on the non-zero subset, full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to five additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn LLaMA Few-NERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), consistent with LP being the most stable positive signal across model families (Qwen Few-NERD: $+1.39$~pp, Table~\\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA Few-NERD degeneracy ($23.4{\\pm}4.7$\\%, 3 seeds) is higher than Qwen ($13.0$\\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.4$~pp) and reduced oracle headroom ($10.0$ vs.\\ $12.4$~pp).\nOn CoNLL, 48--87\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\n\\addlinespace\nLLaMA/Few-NERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\n\\addlinespace\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2025scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.047$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals use $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, each additional comparison yields diminishing information.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.163$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound (more draws raise the probability of a high-quality candidate), but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\paragraph{$N{=}16$ CoNLL selection: small but significant.}\nWhile quality estimation benefits sublinearly from $N$-scaling, selection behavior at $N{=}16$ shows a nuanced exception on LLaMA CoNLL.\nVC achieves the largest gain over single-sample ($+0.28$~pp, $p{=}0.003$--$0.027$ across 3 seeds, all significant), with SJ, FK, and EM at $+0.22$--$0.23$~pp and LP at $+0.12$~pp (2/3 seeds significant).\nThese gains are statistically significant but practically minimal: oracle headroom at $N{=}16$ is only 2.5~pp, so VC captures approximately 10\\% of the available headroom.\nThis reinforces the primary finding: even under the most favorable conditions (high baseline performance, more candidates, and aggregated multi-seed evidence), signal-based selection recovers only a fraction of the oracle headroom available.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, the structural advantage reported in \\S\\ref{sec:qe_results} is robust.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant; these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\nAt $N{=}16$ ($B{=}10{,}000$, permutation test), the structural advantage extends to FK comparisons.\nOn SciERC NER ($n{=}529$), SJ--FK ($\\Delta\\rho{=}0.147$--$0.160$, all $p{\\leq}0.002$) and VC--FK ($\\Delta\\rho{=}0.138$--$0.188$, all $p{\\leq}0.003$) are clearly significant across all three seeds; EM--FK is seed-dependent ($\\Delta\\rho{=}0.054$--$0.093$, $p{=}0.048$--$0.15$).\nOn CoNLL ($n{=}2{,}756$), all signals significantly outperform FK: EM $\\Delta\\rho{=}0.071$ ($p{<}0.001$), SJ $\\Delta\\rho{=}0.056$ ($p{<}0.001$), VC $\\Delta\\rho{=}0.022$ ($p{=}0.040$).\n\n\\paragraph{Seed-replication analysis.}\nUnder a separate seed-replication analysis (5 SciERC seeds, Fisher $z$ + Holm correction), SJ~${>}$~LP reaches $p_{\\text{adj}}{=}0.013$ ($\\rho_{\\text{SJ}}{=}0.356{\\pm}0.014$, $\\Delta\\rho{=}0.151{\\pm}0.006$), providing additional evidence for the robustness of structural signals.\n\n\\section{Holm--Bonferroni Enumeration}\\label{app:holm}\n\nTable~\\ref{tab:holm_family} enumerates all $k{=}57$ statistical tests reported in this paper under a single global Holm--Bonferroni correction.\nUnder this most conservative family, no core NER claim survives correction ($p_{\\text{adj}}{=}0.055$ for the most liberal core claim); two peripheral tests also reach significance (CoNLL few-shot entity entropy, RE LP selection reversal under free-form decoding).\nWe report per-family corrections in the main text (\\S\\ref{sec:prescriptive}); the global enumeration is provided here for transparency.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\n\\label{tab:holm_family}\n\\begin{tabular}{clllcc}\n\\toprule\n\\# & Family & Test Description & Raw $p$ & $p_{\\text{adj}}$ & Sig. \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{Selection}} \\\\\n1 & & SciERC NER LP selection ($N{=}8$, Qwen, Table~3) & $0.290$ & $1.0$ &  \\\\\n2 & & SciERC NER SJ selection ($N{=}8$, Qwen, Table~3) & $0.670$ & $1.0$ &  \\\\\n3 & & SciERC NER FK selection ($N{=}8$, Qwen, Table~3) & $0.790$ & $1.0$ &  \\\\\n4 & & WNUT-17 LP selection ($N{=}8$, Qwen) & $0.720$ & $1.0$ &  \\\\\n5 & & CoNLL LP selection ($N{=}8$, Qwen) & $1.0$ & $1.0$ &  \\\\\n6 & & Few-NERD LP selection ($N{=}8$, Qwen, 3-seed) & ${<}.001$ & $0.055$ & \\\\\n7 & & SciERC NER SJ selection ($N{=}8$, LLaMA-3B) & $0.175$ & $1.0$ &  \\\\\n8 & & SciERC NER LP selection ($N{=}32$, Qwen) & $0.091$ & $1.0$ &  \\\\\n9 & & SciERC NER FK selection ($N{=}32$, Qwen) & $0.101$ & $1.0$ &  \\\\\n10 & & SciERC NER SJ selection ($N{=}32$, Qwen) & $0.244$ & $1.0$ &  \\\\\n11 & & SciERC NER EM selection ($N{=}32$, Qwen) & $0.355$ & $1.0$ &  \\\\\n12 & & SciERC NER VC selection ($N{=}32$, Qwen) & $1.0$ & $1.0$ &  \\\\\n13 & & SciERC RE LP selection ($N{=}16$, 4B, Fisher) & $0.058$ & $1.0$ &  \\\\\n14 & & SciERC RE VC selection ($N{=}16$, 4B, Fisher) & $0.973$ & $1.0$ &  \\\\\n15 & & SciERC RE FK selection ($N{=}16$, 4B, Fisher) & $0.985$ & $1.0$ &  \\\\\n16 & & SciERC RE SJ selection ($N{=}16$, 4B, Fisher) & $0.993$ & $1.0$ &  \\\\\n17 & & SciERC RE EM selection ($N{=}16$, 4B, Fisher) & $0.999$ & $1.0$ &  \\\\\n18 & & SciERC LP selection, non-tied subset ($\\varepsilon{=}0.05$) & $0.004$ & $0.180$ &  \\\\\n19 & & Few-NERD LP selection ($N{=}8$, LLaMA, 3-seed) & ${<}.001$ & $0.055$ & \\\\\n20 & & SciERC LP favorable subset ($+$2.47 pp) & $0.015$ & $0.585$ &  \\\\\n21 & & CoNLL LP favorable subset ($-$1.78 pp) & ${<}.001$ & $0.055$ & \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Construction}} \\\\\n22 & & SciERC LP-weighted construction (Qwen, 3-seed) & $0.004$ & $0.180$ &  \\\\\n23 & & SciERC uniform construction (Qwen, 3-seed) & $0.023$ & $0.874$ &  \\\\\n24 & & Few-NERD LP-weighted construction (Qwen) & ${<}.001$ & $0.055$ & \\\\\n25 & & Few-NERD uniform construction (Qwen) & $0.003$ & $0.138$ &  \\\\\n26 & & CoNLL uniform construction (Qwen) & $0.500$ & $1.0$ &  \\\\\n27 & & SciERC ZS construction (72B) & $0.008$ & $0.320$ &  \\\\\n28 & & SciERC FS construction (72B) & $0.544$ & $1.0$ &  \\\\\n29 & & CoNLL FS construction (72B) & $0.417$ & $1.0$ &  \\\\\n30 & & Few-NERD FS construction (72B) & $0.401$ & $1.0$ &  \\\\\n31 & & SciERC cross-model LP-weighted construction & ${<}.001$ & $0.055$ & \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Calibration}} \\\\\n32 & & SciERC MF-Platt vs Raw LP & $0.720$ & $1.0$ &  \\\\\n33 & & CoNLL MF-Platt vs Raw LP & $0.310$ & $1.0$ &  \\\\\n34 & & Few-NERD MF-Platt vs Raw LP & $0.830$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Signal $\\Delta\\rho$}} \\\\\n35 & & SciERC $\\Delta\\rho$ SJ$-$LP ($N{=}8$, seed 42) & ${<}.001$ & $0.055$ & \\\\\n36 & & SciERC $\\Delta\\rho$ VC$-$SJ ($N{=}8$, seed 42) & $0.300$ & $1.0$ &  \\\\\n37 & & SciERC $\\Delta\\rho$ SJ$-$EM ($N{=}8$, seed 42) & $0.045$ & $1.0$ &  \\\\\n38 & & CoNLL $\\Delta\\rho$ EM$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ & \\\\\n39 & & CoNLL $\\Delta\\rho$ SJ$-$FK ($N{=}16$) & ${<}.001$ & $0.055$ & \\\\\n40 & & CoNLL $\\Delta\\rho$ VC$-$FK ($N{=}16$) & $0.040$ & $1.0$ &  \\\\\n41 & & SciERC $\\Delta\\rho$ SJ$-$FK (LLaMA, permutation) & $0.060$ & $1.0$ &  \\\\\n42 & & SciERC RE $\\Delta\\rho$ SJ$-$FK (full-set) & $0.530$ & $1.0$ &  \\\\\n43 & & RE SJ $\\rho$ Q1 vs Q4 sentence length (Fisher $z$) & $0.004$ & $0.180$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Correlation}} \\\\\n44 & & Cross-dataset degeneracy--LP gain ($n{=}23$) & $0.810$ & $1.0$ &  \\\\\n45 & & Per-type degeneracy--headroom (Few-NERD, Spearman) & $0.004$ & $0.180$ &  \\\\\n46 & & Per-type degeneracy--headroom (exact permutation) & $0.005$ & $0.205$ &  \\\\\n47 & & Per-type degeneracy--headroom ($\\text{df}{=}4$ adjusted) & $0.033$ & $1.0$ &  \\\\\n48 & & SciERC per-type degeneracy--LP ($\\rho{=}0.14$) & $0.790$ & $1.0$ &  \\\\\n49 & & Kruskal--Wallis per-type LP heterogeneity (SciERC) & $0.796$ & $1.0$ &  \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{FS error}} \\\\\n50 & & FS vs ZS error overlap (SciERC, permutation) & $0.840$ & $1.0$ &  \\\\\n51 & & FS vs ZS error overlap (CoNLL, permutation) & $0.640$ & $1.0$ &  \\\\\n52 & & FS vs ZS entity entropy (SciERC) & $0.810$ & $1.0$ &  \\\\\n53 & & FS vs ZS entity entropy (CoNLL, Wilcoxon) & ${<}10^{-4}$ & ${<}.001$ & $\\dagger$ \\\\\n\\addlinespace\n\\multicolumn{6}{l}{\\textit{Other}} \\\\\n54 & & LP distribution seed 42 vs 456 (Mann--Whitney) & $0.550$ & $1.0$ &  \\\\\n55 & & RE LP selection reversal (free-form, 4-seed) & ${<}.001$ & $0.006$ & $\\dagger$ \\\\\n56 & & WNUT-17 conditional $\\rho$ VC ($p$-value) & $0.487$ & $1.0$ &  \\\\\n57 & & WNUT-17 conditional $\\rho$ FK ($p$-value) & $0.002$ & $0.094$ &  \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n% fig_selection_gap promoted to main text (\\S\\ref{sec:selection_gap})\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 59\\% (Qwen) to 89\\% (LLaMA) of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect where single-sample F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, attributable to the 53.7\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding single-sample\\footnote{Oracle-improvable and diversity-stratified analyses use $n{=}529$ (excluding instances with empty gold annotations; see \\S\\ref{sec:evaluation}); the diversity quantification in Table~\\ref{tab:diversity} uses the full test set.}: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, consistent with the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below single-sample, and LP, the only per-sample signal, achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below single-sample and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{Instance degeneracy statistics.}\nTable~\\ref{tab:degeneracy} quantifies instance degeneracy across configurations. ``Constant F1'' denotes instances where all $N$ samples receive identical instance-level F1; ``Constant utility'' denotes instances where MBR (SJ) utility is identical across candidates, preventing ranking.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\n\\label{tab:degeneracy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\n& \\shortstack{SciERC 8B\\\\($N{=}8$)} & \\shortstack{SciERC 4B\\\\($N{=}8$)} & \\shortstack{CoNLL 8B\\\\($N{=}8$)} \\\\\n\\midrule\nConstant F1 & 12.2\\% & 10.4\\% & 61.7\\% \\\\\nConstant utility & 13\\% & 7.0\\% & 64\\% \\\\\nOracle gap closed (non-deg.) & 23\\% & 25.2\\% & 36\\% \\\\\nWithin-inst.\\ SJ $\\rho$ (median) & 0.524 & 0.550 & 0.990 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{TOST equivalence testing.}\\label{app:tost}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to single-sample within a bound $\\delta$.\nThe $\\delta$ values are contextualized against oracle headroom (12--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThese proportions use the same test data that defines the headroom, introducing circularity: $\\delta$ is anchored to the very quantity it contextualizes.\nWe address this below with externally anchored equivalence margins.\nThe breakpoint $\\delta^*$, the minimum equivalence margin at which each signal passes TOST, ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to single-sample (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\n\\label{tab:tost}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{External equivalence margins.}\nThe oracle-headroom anchors above introduce circularity: $\\delta$ is calibrated against the very quantity it contextualizes.\nTo resolve this, we supplement with three externally grounded margins:\n(1) $\\delta_{\\mathrm{SEM}}$: the bootstrapped standard error of single-sample F1 (0.43--1.33~pp depending on configuration), which represents measurement noise;\n(2) $\\delta_{\\mathrm{practical}}{=}0.5$~pp, the threshold below which NER differences are considered negligible \\cite{ratinov2009design};\n(3) $\\delta_{\\mathrm{literature}}{=}1.0$~pp, the approximate significant-difference threshold established in NER evaluation methodology \\cite{bergkirkpatrick2012empirical}.\n\nResults under these external anchors diverge sharply by configuration.\nOn LLaMA CoNLL ($n{=}2{,}756$), all signals pass equivalence at every $\\delta$ ($p{<}0.001$), consistent with the near-zero selection deltas ($|\\Delta|{\\leq}0.1$~pp) and tight CIs at this sample size.\nOn Qwen CoNLL ($n{=}2{,}756$), no signal passes at any external $\\delta$: selection F1 degrades by 0.9--1.5~pp relative to single-sample, which exceeds even $\\delta_{\\mathrm{literature}}$.\nOn SciERC NER ($n{=}529$), only SJ passes at $\\delta_{\\mathrm{SEM}}{=}1.33$~pp (the widest SEM bound); all other signals and tighter margins fail.\nThese external anchors confirm that the equivalence conclusion is configuration-dependent: LLaMA CoNLL selection is robustly equivalent to single-sample under any reasonable margin, while SciERC and Qwen CoNLL selection shows detectable degradation at externally calibrated thresholds.\n\n\\paragraph{Multiple comparison considerations.}\\label{app:multiple_comparisons}\nOur primary selection analysis involves ${\\sim}$20 comparisons (5 signals $\\times$ 3--4 configurations).\nSince all primary selection results are non-significant ($p{>}0.05$), applying Benjamini-Hochberg correction can only make these results more conservative, strengthening the ``no signal beats greedy'' conclusion.\nThe sole positive finding, the non-tied LP subset ($+2.9$~pp, $p{=}0.004$; \\S\\ref{sec:discussion}), survives Bonferroni correction over the 5 signal comparisons ($p_{\\mathrm{adj}}{=}0.020 < 0.05$). However, the $\\varepsilon{=}0.05$ threshold is selected post-hoc from a 7-point sweep (Appendix~\\ref{app:epsilon_robustness}); joint correction across thresholds and signals yields $p_{\\mathrm{adj}}{=}0.14$, so this finding is exploratory.\nFor quality estimation signal rankings, differences between the top signals (e.g., VC vs.\\ SJ on SciERC) should be interpreted as descriptive rather than as statistically confirmed orderings, given the limited power of 3-seed comparisons.\n\n\\paragraph{When would consistency-based selection work?}\\label{app:when_selection_works}\nOur negative results are specific to fine-tuned models with constrained decoding on structured IE. Several conditions outside our experimental scope could restore selection headroom.\n(a)~Models with poor calibration or in-context learning setups (without fine-tuning) produce more diverse outputs, widening the gap between candidates that consistency signals can exploit.\n(b)~Closed-source APIs where log-probabilities are unavailable make consistency signals the only viable selection mechanism; our structural signals (SJ, VC, FK, EM) provide quality estimation ($\\rho$ up to 0.45) even without model-internal access.\n(c)~Ensemble or mixture-of-experts settings generate structurally diverse candidates by design, reducing instance degeneracy below the levels observed in our single-model sampling.\n(d)~Tasks where the model exhibits systematic overconfidence (e.g., hallucination-prone generation) may benefit from consensus filtering, as disagreement among samples would carry more discriminative signal than in our well-calibrated fine-tuned regime.\n\n\\section{Supervised and Model-Internal Signal Analysis}\\label{app:supervised_combination}\n\n\\subsection{Supervised Signal Combination}\n\nSupervised classifiers (logistic regression, MLP, random forest) trained on all five signals (5-fold CV, 3-seed mean, SciERC, $N{=}16$, $+17.9$~pp headroom) all perform at or below greedy (F1${=}0.644$; LR: $-0.4$~pp; MLP: $-1.6$~pp; RF: $-3.1$~pp).\nAdding pairwise interaction features does not help (AUROC 0.634 vs.\\ 0.638).\nTo test whether richer representations could close the gap, we train a DeBERTa-v3-base verifier that encodes input-output pairs and predicts per-sample F1.\nDeBERTa achieves $\\rho{=}0.329{\\pm}0.087$ (5-fold CV, 3 seeds). Despite moderate quality prediction, selection utility is poor: on SciERC, DeBERTa closes $-26.5{\\pm}26.5$\\% of the oracle gap (13 of 15 runs negative; vs.\\ LP's $+4.2{\\pm}10.7$\\%); on Few-NERD, DeBERTa recovers only $+3.5$\\% (single 80/20 split; vs.\\ LP's $+16.3$\\%).\nCross-dataset transfer fails entirely ($-27$\\% to $-72$\\% gap closure).\nGrid-search ensemble optimization over signal weights confirms LP dominance: across configurations, LP receives mean weight $0.78$, while FK and SJ receive zero weight; VC and EM serve only as secondary regularizers.\nNeither handcrafted signal combinations nor learned text representations close the selection gap; only model-internal log-probability provides meaningful selection signal, consistent with an information asymmetry between the generating model and external observers.\n\n\\subsection{Entity-Level Verifier Transfer}\\label{app:verifier_transfer}\n\nA LightGBM entity-level verifier (5 features: agreement count, VC, LP, SJ, FK) achieves AUC${=}0.923{\\pm}0.002$ under out-of-fold evaluation, confirming that entity correctness is learnable from the available signals.\nIn-domain OOF construction yields $+0.30$\\,pp overall, with per-dataset gains of $+1.28$\\,pp (SciERC), $+0.55$\\,pp (CoNLL), and $+0.02$\\,pp (Few-NERD).\nThe near-zero Few-NERD gain despite high AUC shows that frequency-based threshold construction already captures most of the verifier's signal.\nCross-dataset transfer to Few-NERD is negative: $-0.76$\\,pp (B2-v2), $-1.02$\\,pp (B2-v3), $-1.27$\\,pp (B2-v4 Replace, AUC${=}0.822$), and $-0.85$\\,pp (B2-v4 Augment, AUC${=}0.855$), all below greedy.\nThe learned feature--correctness mapping is dataset-specific: entity agreement patterns that predict correctness on scientific text do not transfer to fine-grained entity types.\n\n\\subsection{Hidden State Probes}\\label{app:hidden_probe}\n\nEntity-level probes confirm that quality information is partially encoded in hidden representations (AUROC${=}0.63$\\textendash$0.88$, dataset-dependent; \\S\\ref{sec:mechanistic}); we test whether this translates to sample-level selection gain by training probes on the generating model's hidden states.\n\n\\paragraph{Setup.}\nUnlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on Few-NERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\nFor each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).\nEntity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}\n\\label{tab:hidden_probe}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}l ccc cc@{}}\n\\toprule\n& \\multicolumn{3}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{Few-NERD}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-6}\nMethod & $\\rho$ & Sel.\\ F1 & Gap\\% & $\\rho$ & Gap\\% \\\\\n\\midrule\nLP & .283 & $\\mathbf{.650}$ & $+$4.8 & .606 & 12.3 \\\\\nHidden Linear & $.179{\\pm}.019$ & $.613{\\pm}.002$ & $-$23.4 & \\multicolumn{2}{c}{---} \\\\\nHidden MLP & $\\mathbf{.388{\\pm}.013}$ & $.637{\\pm}.003$ & $-$5.1 & $\\mathbf{.629{\\pm}.007}$ & 11.7 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\paragraph{Cross-dataset asymmetry.}\nOn SciERC, the MLP probe achieves higher quality correlation than LP ($\\rho{=}0.388$ vs.\\ $0.283$, $+37$\\%); hidden states encode information beyond what LP captures.\nYet higher correlation does not yield better selection: MLP selection F1 ($0.637$) falls below LP's ($0.650$), with gap closure turning negative ($-5.1$\\% vs.\\ $+4.8$\\%; Table~\\ref{tab:hidden_probe}).\nThe linear probe performs worse still ($\\rho{=}0.179$, gap closure $-23.4$\\%).\nOn Few-NERD, the MLP provides no increment over LP (gap closure $11.7$\\% vs.\\ $12.3$\\%).\nA learned token-level LP aggregator (1D CNN over per-token log-probabilities) matches mean LP on Few-NERD (gap closure $56.4$\\% vs.\\ $55.8$\\%); LP's bottleneck is not token aggregation.\nDespite partial entity quality encoding in hidden representations (entity-level probe AUROC${=}0.63$\\textendash$0.88$; \\S\\ref{sec:mechanistic}), the correlation-selection gap persists at the sample level: in the high-capability regime (greedy F1${=}0.644$), inter-sample F1 differences are small enough that improved ranking provides no marginal selection value, consistent with the capability-diversity tension (\\S\\ref{sec:discussion}).\n\n\\subsection{Method Coverage Matrix}\\label{app:method_coverage}\n\nTable~\\ref{tab:method_coverage} summarizes the experimental coverage of each entity-level method evaluated in this work. Individual methods were tested on subsets of the full dataset $\\times$ model matrix; the collective coverage spans three NER datasets and two model families.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\n\\label{tab:method_coverage}\n\\begin{tabular}{lccccl}\n\\toprule\nMethod & SciERC & Few-NERD & CoNLL & Qwen & LLaMA \\\\\n\\midrule\nESJ (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nMRSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nLSC (\\S\\ref{sec:mechanistic}) & --- & \\checkmark & --- & \\checkmark & --- \\\\\nHet-T (App.~\\ref{app:robustness}) & \\checkmark & --- & --- & \\checkmark & --- \\\\\nASB (App.~\\ref{app:dals}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nSCD (App.~\\ref{app:supervised_combination}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\nVerifier (\\S\\ref{sec:verifier}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & --- \\\\\n\\midrule\nQE signals (\\S\\ref{sec:qe_results}) & \\checkmark & \\checkmark & \\checkmark & \\checkmark & \\checkmark \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{How Self-Verification Fails}\\label{sec:mechanistic}\n\nThe diagnostic framework (\\S\\ref{sec:method}) identifies \\textit{where} self-consistency fails; this section probes \\textit{why} by testing whether models can self-verify at the entity level.\nProbe experiments use Qwen2.5-7B (not the fine-tuned Qwen3-8B used in main experiments); conclusions are architecture-specific.\nWe evaluate self-verification and diagnostic probes on Qwen2.5-7B\\footnote{ESJ, MRSC, and LSC use Qwen2.5-7B-Instruct (zero-shot self-verification capability) rather than the fine-tuned Qwen3-8B used in the main experiments. Conclusion direction is consistent with the main experiments' negative results across all fine-tuned selection strategies. The pattern---selection failure across all signals---is independently confirmed in the Qwen3-8B main experiments, making the introspection boundary a model-independent finding within our tested scale. Probe conclusions are limited to the Qwen2.5 architecture; linear probes may underestimate representational capacity (nonlinear alternatives are left to future work).} fine-tuned for NER on Few-NERD ($N{=}8$, seed 42; full results in Table~\\ref{tab:self_verification}).\n\n\\paragraph{Entity Self-Judgment (ESJ).}\nFor each extracted entity, we prompt the generating model: ``Is [\\textit{entity}] a [\\textit{type}] entity in this sentence?''\nEntity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$.\nESJ-weighted construction degrades F1 to $0.711$ (vs.\\ greedy $0.794$).\n\n\\paragraph{Multi-Round Self-Consistency (MRSC).}\nFollowing iterative self-refinement \\cite{madaan2023selfrefine}, we re-prompt on disputed entities (agreement ${<}0.6$) with focused verification; P(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\\ $0.4997$).\nMRSC best F1 ($0.763$) falls below greedy.\n\n\\paragraph{Latent Self-Consistency (LSC).}\nMean-pooled final-layer hidden states ($d{=}3584$) provide per-sample latent representations.\nCentroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms majority vote ($0.792$) but does not close the oracle gap ($0.882$).\n\n\\paragraph{Hidden-state probe.}\nA logistic regression on mean-pooled final-layer hidden states at entity spans achieves AUROC $0.636$ (Few-NERD), $0.882$ (CoNLL), $0.630$ (SciERC), evaluated with GroupKFold CV (5-fold ${\\times}$ 3 seeds, groups${=}$source instance to prevent entity-level leakage; \\S\\ref{app:hidden_probe}).\nAll three exceed ESJ ($0.51$); only CoNLL approaches frequency agreement ($0.868$).\nCross-dataset transfer is weak: leave-one-dataset-out AUROC drops to $0.559$ (Few-NERD${\\to}$CoNLL) and $0.671$ (CoNLL${\\to}$Few-NERD), indicating that entity error patterns are dataset-specific rather than reflecting a universal introspection boundary, limiting probe-based approaches without per-dataset calibration.\nAt the sample level, an MLP probe closes only 13.9\\% of the oracle gap on SciERC (\\S\\ref{app:hidden_probe}).\n\n\\paragraph{The introspection boundary.}\nEntity quality is partially encoded in hidden representations: a supervised probe (AUROC $0.63$\\textendash$0.88$) consistently exceeds self-judgment (ESJ $0.51$) but only marginally exceeds multi-sample agreement ($0.87$) on CoNLL, suggesting consensus captures information beyond single-pass representations while the prompt interface fails to access even partial hidden-state signal.\nLODO transfer drops to $0.56$\\textendash$0.67$, so even direct hidden-state access would not yield a universal quality signal---consistent with the negative cross-dataset verifier transfer (\\S\\ref{sec:verifier}).\n\n\\section{Entity-Level Self-Verification Probes}\\label{app:self_verification}\n\nThree independent probes test whether the generating model can self-verify at the entity level, using Qwen2.5-7B fine-tuned on Few-NERD ($N{=}8$, seed 42).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\n\\label{tab:self_verification}\n\\begin{tabular}{@{}lcc@{}}\n\\toprule\nMethod & Key Metric & F1 \\\\\n\\midrule\nGreedy ($T{=}0$) & --- & .794 \\\\\nMV ($\\theta{=}0.375$) & --- & .792 \\\\\nOracle & --- & .882 \\\\\n\\midrule\nESJ (best $\\theta{=}0.02$) & AUROC${=}0.512$ & .711 \\\\\nMRSC (best $\\theta{=}0.5$) & $\\Delta P(\\text{yes}){=}0.001$ & .763 \\\\\nLSC (centroid) & $\\rho_{\\text{LP-latent}}{=}0.52$ & .759 \\\\\nLSC (entity conf.) & --- & .839 \\\\\n\\midrule\nFreq.\\ agreement & AUROC${=}0.868$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Entity Self-Judgment (ESJ).}\nFor each extracted entity, we prompt the model: ``Is [entity] a [type] entity in this sentence?''\nThe entity-level AUROC is $0.512$---indistinguishable from chance---with P(yes$|$correct)${=}0.500$ and P(yes$|$incorrect)${=}0.500$ (separation $0.001$).\nESJ-weighted construction degrades F1 to $0.711$ (vs.\\ greedy $0.794$), confirming the model lacks entity-level self-judgment.\n\n\\paragraph{Multi-Round Self-Consistency (MRSC).}\nWe re-prompt the model on disputed entities (agreement ${<}0.6$) with a focused verification query and aggregate with Round~2 weight${=}2$.\nP(yes) separation between gold and non-gold entities is $0.0006$ ($0.5003$ vs.\\ $0.4997$), and MRSC best F1 ($0.763$) falls below both greedy and MV.\n\n\\paragraph{Latent Self-Consistency (LSC).}\nMean-pooled final-layer hidden states ($d{=}3584$) provide latent representations per sample.\nCentroid selection ($0.759$) underperforms greedy ($0.794$); latent entity confidence ($0.839$) outperforms MV ($0.792$) but does not close the oracle gap ($0.882$).\n\n\\paragraph{Frequency agreement as the viable signal.}\nCross-sample entity frequency agreement achieves AUROC${=}0.868$ for entity correctness prediction; a supervised hidden-state probe (AUROC${=}0.63$\\textendash$0.88$; \\S\\ref{sec:mechanistic}) exceeds this only on the simplest dataset (CoNLL, $0.882$), while falling below on complex NER tasks.\nThe probe consistently exceeds prompt-based self-evaluation (ESJ AUROC${=}0.512$), confirming that hidden states encode partial entity quality signal inaccessible through the prompt interface, consistent with the complexity-dependent introspection boundary diagnosed in the main text (\\S\\ref{sec:mechanistic}).\n\n\\section{Cross-Dataset Entailment Self-Judgment}\\label{app:esj}\n\nTable~\\ref{tab:esj_cross} compares entailment-based self-judgment (ESJ) with agreement-based signals across three datasets.\nESJ achieves near-random AUROC on all datasets, confirming that the self-verification failure observed on Few-NERD (\\S\\ref{sec:mechanistic}) generalizes.\n\n\\begin{table}[h]\n\\small\n\\centering\n\\caption{Entity-level self-verification: ESJ vs.\\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}\n\\label{tab:esj_cross}\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & ESJ AUROC & ESJ $\\rho$ & Agree.\\ AUROC & Agree.\\ $\\rho$ \\\\\n\\midrule\nSciERC  & 0.512 & 0.020 & 0.792 & 0.515 \\\\\nCoNLL   & 0.553 & 0.087 & 0.941 & 0.777 \\\\\nFew-NERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across multiple seeds (Qwen: 5; LLaMA: 3) for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals (rankings are stable across all seeds).\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM. This reversal from the NER ranking reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over seeds.}\n\\label{tab:multiseed}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .205${\\pm}$.015 & .254${\\pm}$.016 & .356${\\pm}$.014 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .579${\\pm}$.008 & .600${\\pm}$.016 & .659${\\pm}$.016 & .677${\\pm}$.011 & .631${\\pm}$.013 \\\\\nLLaMA & .565${\\pm}$.008 & .593${\\pm}$.006 & .632${\\pm}$.012 & .673${\\pm}$.009 & .606${\\pm}$.005 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{dong2024xgrammar, willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Thinking Token Impact Analysis}\\label{app:thinking_token}\n\nQwen3-8B's SciERC checkpoint was trained with empty \\texttt{&lt;think>&lt;/think>} blocks prepended to each response (\\S\\ref{sec:setup}).\nWe quantify the potential impact on LP scores through three complementary arguments.\n\n\\paragraph{LP shift magnitude.}\nEmpty thinking tokens (mean 4.5 per sample) constitute 2.1\\% of tokens on SciERC.\nThe estimated LP shift is 0.001 nats per token (2.68\\% of the median within-instance LP range of 0.041 nats).\nBecause all samples share identical thinking-token LP offsets, cumulative LP rankings are invariant; mean LP changes selection for ${<}1.5\\%$ of instances.\n\n\\paragraph{Constant prefix cancellation.}\nAll $N$ samples within an instance share the same prompt and, under constrained decoding, the same absence of thinking tokens at inference time.\nAny LP bias from the training-time thinking prefix is therefore a near-constant additive shift across all candidates within an instance, leaving within-instance LP \\textit{rankings} unchanged.\n\n\\paragraph{CoNLL control group.}\nCoNLL and WNUT-17 checkpoints were trained without thinking tokens (\\texttt{enable\\_thinking=False}).\nIf thinking tokens caused LP compression on SciERC, CoNLL should exhibit lower tied fractions.\nInstead, CoNLL shows \\textit{higher} tied fractions at both temperatures (86.8\\% at $T{=}1.0$, 95.8\\% at $T{=}0.7$) than SciERC (60.3\\% at $T{=}1.0$), directly contradicting the thinking-token hypothesis.\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}, Figure~\\ref{fig:lp_range_cdf}).\nThe median within-instance LP range is only 0.041 nats; we use $\\varepsilon{=}0.05$ as an illustrative threshold to characterize this compression.\nAt this cutpoint, 60.3\\% of instances ($n{=}529$, excluding empty gold annotations) have a within-sample range below $\\varepsilon$, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nThe CDF rises smoothly with no cliff or discontinuity (Figure~\\ref{fig:lp_range_cdf}); compression is a pervasive regime rather than a bimodal split.\nThis compression is stable across seeds: seed${=}456$ yields median LP range${=}0.040$ nats and tied fraction${=}62.2\\%$ (vs.\\ seed${=}42$: $0.041$ nats, $60.3\\%$).\nSeed~456 uses a different subtask flag (joint vs.\\ ner for seeds 42 and 123); the LP distributions are statistically indistinguishable (median LP: 8.37 vs.\\ 8.20 nats; Mann--Whitney $p{=}0.55$); the subtask change does not affect compression.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold; SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_lp_range_cdf}\n\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\n\\label{fig:lp_range_cdf}\n\\end{figure}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms single-sample ($+2.9$~pp F1, $p{=}0.004$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nAs a continuous complement to the binary tied/non-tied analysis, pooled within-instance $\\rho(\\text{LP}, \\text{F1}){=}0.248$ across all instances confirms weak but positive per-sample signal; however, only 21.6\\% of instances achieve $p{<}0.05$ significance, and $\\rho(\\text{LP range}, \\text{F1 range}){=}0.328$ shows that instances with more LP spread also exhibit more F1 variability. LP carries information, but compression limits its exploitation.\nA free-form NER decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression persists without constrained decoding.\n\n\\paragraph{$\\varepsilon$ sensitivity sweep (post-hoc exploratory).}\nTable~\\ref{tab:epsilon_sweep} sweeps the tied/non-tied threshold from $\\varepsilon{=}0.01$ to $0.20$ as a post-hoc exploratory analysis characterizing how selection gain varies with compression severity.\nThe tied fraction increases smoothly with no cliff or discontinuity, and the selection gain $\\Delta$ grows monotonically as the non-tied subset narrows to progressively higher-spread instances.\n$\\varepsilon{=}0.05$ yields the strongest statistical separation ($p{=}0.004$); at $\\varepsilon{\\geq}0.15$, the non-tied subset becomes too small for reliable inference ($n{\\leq}36$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\n\\label{tab:epsilon_sweep}\n\\begin{tabular}{ccccc}\n\\toprule\n$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\n\\midrule\n0.01 & 1.1\\% & 523 & $+$0.58 & .21 \\\\\n0.02 & 13.6\\% & 457 & $+$0.83 & .15 \\\\\n0.03 & 31.8\\% & 361 & $+$1.31 & .079 \\\\\n\\textbf{0.05} & \\textbf{60.3\\%} & \\textbf{210} & \\textbf{$+$2.86} & \\textbf{.004} \\\\\n0.10 & 83.9\\% & 85 & $+$3.69 & .034 \\\\\n0.15 & 93.2\\% & 36 & $+$4.15 & .11 \\\\\n0.20 & 96.4\\% & 19 & $+$4.59 & .13 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{$\\varepsilon$ robustness of selection F1.}\\label{app:epsilon_robustness}\nThe preceding analysis stratifies LP by a tied/non-tied threshold; consistency-based signals (SJ, FK, VC, EM) also use $\\varepsilon$ to define MBR-style proximity in selection.\nTable~\\ref{tab:epsilon_robustness} reports the maximum selection F1 variation across $\\varepsilon \\in [0, 0.2]$ for all signals and configurations.\nAt $\\varepsilon{=}0.05$, consistency signals change by at most 1.09~pp (mean 0.21~pp), with EM completely $\\varepsilon$-invariant (integer scoring); LP is the most sensitive (up to 3.65~pp across the full range), as expected.\nSpearman $\\rho$, the primary quality estimation metric throughout, is a continuous rank correlation that does not depend on any discretization threshold; the $\\varepsilon$ parameter affects only the selection analysis.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\n\\label{tab:epsilon_robustness}\n\\begin{tabular}{lcccc}\n\\toprule\n& \\multicolumn{2}{c}{\\textbf{SciERC}} & \\multicolumn{2}{c}{\\textbf{CoNLL}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & Qwen & LLaMA & Qwen & LLaMA \\\\\n\\midrule\nSJ & 0.92 & 1.45 & 0.99 & 0.18 \\\\\nFK & 1.03 & 0.93 & 0.60 & 0.15 \\\\\nVC & 2.33 & 0.53 & 0.72 & 0.18 \\\\\nEM & 0.00 & 0.00 & 0.00 & 0.00 \\\\\nLP & 3.65 & 2.58 & 3.00 & 0.31 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset analysis.}\nTable~\\ref{tab:nontied_main} presents the non-tied subset analysis referenced in \\S\\ref{sec:discussion}.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\n\\label{tab:nontied_main}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nSubset & $n$ & $\\rho$(LP,F1) & LP $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nTied (range ${<}0.05$) & 319 & 0.08 & ${\\approx}0$ \\\\\nNon-tied (range ${\\geq}0.05$) & 210 & 0.39 & $+$2.9~pp ($p{=}0.004$) \\\\\n\\midrule\nAll instances & 529 & 0.248 & $+$0.2~pp ($p{=}0.29$) \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Within-instance LP-quality alignment.}\\label{app:within_instance_rho}\n\nTable~\\ref{tab:within_rho} reports median within-instance $\\rho(\\text{LP}, \\text{F1})$ across datasets, computed over non-degenerate instances (those with ${\\geq}2$ distinct F1 values across $N{=}8$ samples).\nFew-NERD exhibits substantially stronger alignment ($\\rho{=}0.667$) than SciERC ($\\rho{=}0.262$), consistent with LP selection succeeding only on Few-NERD.\nCoNLL alignment is moderate ($\\rho{\\approx}0.51$), but the valid-instance fraction is low (38\\% for Qwen, 11\\% for LLaMA) because degeneracy eliminates most headroom before alignment can operate.\nLP-quality alignment is the primary predictor of selection direction; degeneracy constrains headroom but does not independently predict whether LP selection gains materialize (\\S\\ref{sec:discussion}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}\n\\label{tab:within_rho}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccc@{}}\n\\toprule\nDataset & Model & Med.\\ $\\rho$ & $n_{\\text{valid}}$ / $n_{\\text{total}}$ & Valid\\% \\\\\n\\midrule\nSciERC & Qwen3-8B & 0.262 & 435 / 529 & 82\\% \\\\\nFew-NERD & Qwen3-8B & 0.667 & 28{,}055 / 32{,}565 & 86\\% \\\\\nCoNLL & Qwen3-8B & 0.506 & 1{,}124 / 2{,}756 & 41\\% \\\\\nCoNLL & LLaMA-3.1-8B & 0.512 & 298 / 2{,}756 & 11\\% \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\clearpage\n\\paragraph{Few-NERD LP compression threshold sensitivity.}\\label{app:fewnerd_epsilon}\n\nTables~\\ref{tab:fewnerd_epsilon} and \\ref{tab:fewnerd_lp_bucket} extend the $\\varepsilon$ analysis to Few-NERD ($n{=}32{,}565$, Qwen3-8B, $N{=}8$, seed${=}42$).\n\n\\begin{table}[ht!]\n\\centering\n\\small\n\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\n\\label{tab:fewnerd_epsilon}\n\\begin{tabular}{cccc}\n\\toprule\n$\\varepsilon$ & Compressed\\% & $\\rho$(non-comp.) & $\\rho$(all) \\\\\n\\midrule\n0.01 & 9.3 & .682 & .633 \\\\\n0.03 & 19.9 & .695 & .633 \\\\\n\\textbf{0.05} & \\textbf{34.5} & \\textbf{.710} & \\textbf{.633} \\\\\n0.10 & 60.2 & .733 & .633 \\\\\n0.15 & 75.9 & .723 & .633 \\\\\n0.20 & 92.5 & .720 & .633 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[ht!]\n\\centering\n\\small\n\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\n\\label{tab:fewnerd_lp_bucket}\n\\begin{tabular}{lccc}\n\\toprule\nLP range & $n$ & MV F1 & LP$-$MV (pp) \\\\\n\\midrule\n$[0, 0.01)$ & 3{,}018 & .818 & $+$0.8 \\\\\n$[0.01, 0.03)$ & 3{,}457 & .812 & $+$1.5 \\\\\n$[0.03, 0.05)$ & 4{,}744 & .786 & $+$2.3 \\\\\n\\midrule\n$[0.05, 0.10)$ & 8{,}374 & .740 & $+$4.3 \\\\\n$[0.10, 0.20)$ & 10{,}537 & .701 & $+$5.8 \\\\\n$[0.20, \\infty)$ & 2{,}435 & .771 & $+$3.6 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n$\\varepsilon{=}0.05$ sits at the elbow: compressed instances increase from 19.9\\% ($\\varepsilon{=}0.03$) to 34.5\\%, while non-compressed $\\rho$ plateaus at $\\varepsilon{\\geq}0.10$ ($0.72$--$0.73$).\nThe LP-best advantage over MV shows a clear transition: compressed instances (LP range${<}0.05$) gain $+0.8$ to $+2.3$\\,pp, while non-compressed instances gain $+3.6$ to $+5.8$\\,pp (Table~\\ref{tab:fewnerd_lp_bucket}).\n\n\\subsection{Token-Level Signal Comparison}\\label{app:token_signal}\n\nWe compared mean log-probability (length-normalized, used throughout) with sequence-level log-probability (cumulative sum of token log-probs).\nInstance-level Spearman $\\rho$ between the two rankings averages 0.85, with rankings diverging for 10.6\\% of instances where token count coefficient of variation exceeds 0.10.\nOn these disagreement instances, mean LP selection achieves F1${=}0.643$ vs.\\ cumulative LP F1${=}0.219$ ($+42.4$\\,pp).\nOverall, mean LP outperforms cumulative LP by $+4.6$ F1 points (Wilcoxon $p{<}0.001$).\nThe divergence is driven by structured output length variation: sequences with more extracted entities are longer but not necessarily higher quality, and length normalization prevents this bias.\n\n\\section{Consistency-Stratified Selection Analysis}\\label{app:vc_quartile}\n\nTable~\\ref{tab:vc_quartile} stratifies SciERC instances by voting confidence (VC) quartiles and reports selection $\\Delta$ (gain over single-sample) for LP and SJ.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\n\\label{tab:vc_quartile}\n\\begin{tabular}{lcccc}\n\\toprule\nQuartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{NER}} \\\\\nQ1 (low) & 0.30 & $+$1.55 & $+$0.54 & 16.85 \\\\\nQ2 & 0.51 & $-$0.65 & $-$1.89 & 14.35 \\\\\nQ3 & 0.68 & $+$1.97 & $+$1.84 & 16.83 \\\\\nQ4 (high) & 0.92 & $-$0.41 & $-$0.04 & 4.78 \\\\\n\\midrule\n\\multicolumn{5}{l}{\\textit{$^\\dagger$RE}} \\\\\nQ1 (low) & --- & $-$3.56 & --- & --- \\\\\nQ4 (high) & --- & $+$4.01 & --- & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe NER pattern shows two complementary failure modes rather than a monotonic relationship between consistency and selection gain:\n\\begin{itemize}\n\\item \\textbf{Q4 ceiling effect.} High-consistency instances (mean VC${=}0.92$) have oracle headroom of only 4.78~pp. Samples have already converged, leaving little room for any signal to improve selection.\n\\item \\textbf{Q1--Q2 noise.} Low-consistency instances retain large headroom (14--17~pp) but LP rankings are unreliable, and LP rankings produce inconsistent $\\Delta$ signs across quartiles.\n\\end{itemize}\n\nOn $^\\dagger$RE, the pattern differs: Q4 LP achieves $+4.01$~pp; LP may recover selection ability when high consistency coincides with structured output diversity. This is a single-dataset observation and should be interpreted cautiously.\n\nOn CoNLL NER, Q3--Q4 instances have VC${=}1.0$ (all samples identical), and $\\Delta{=}0$ universally; this ceiling effect is even more extreme than SciERC Q4.\n\n\\section{Exploratory Extension to Relation Extraction}\\label{app:re_extension}\n\nWe extend the NER evaluation to relation extraction (RE) on SciERC as an exploratory single-benchmark analysis.\nRE produces sets of (head, relation, tail) triples with partial overlap; 40\\% of RE instances receive zero F1, and entity span errors account for 55.5\\% of RE false negatives, a prerequisite failure that consistency signals cannot detect (\\S\\ref{app:additional}).\nAll RE results use Qwen3-8B unless noted; single-seed ($\\text{seed}{=}42$) for $N{=}8$ analyses, 3-seed for $N{=}16$.\n\n\\paragraph{Diagnostic framework.}\nApplying the diagnostic framework to RE ($N{=}8$): instance degeneracy is $10.1$\\%, comparable to SciERC NER ($13.4$\\%), yet MV $\\Delta{=}{-}5.90$\\,pp---far worse than any NER dataset.\nThe driver is RE's $40$\\% zero-F1 rate (vs.\\ ${\\leq}5.4$\\% in NER): diverse but \\textit{incorrect} samples produce noise that MV amplifies.\nLP-best selection also fails ($\\Delta{=}{-}0.94$\\,pp), despite pooled LP-F1 $\\rho{=}0.350$---above SciERC NER ($0.312$).\nOracle headroom is $+18.1$\\,pp (greedy $0.404$, oracle $0.585$), the largest of any configuration, confirming that correct answers exist among samples but no signal recovers them.\n\n\\paragraph{Quality estimation.}\nRE quality estimation is reported in Table~\\ref{tab:multiseed} (3-seed means).\nThe signal ranking differs from NER: VC leads ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM, a reversal reflecting RE's higher sensitivity to per-sample scoring.\nRE miscalibration is more severe than NER (ECE 0.109--0.339; Figure~\\ref{fig:reliability}).\n\n\\paragraph{Selection.}\nTable~\\ref{tab:re_cond_selection} presents RE selection at $N{=}8$: no signal outperforms single-sample (0.404) on the full set ($n{=}397$) or the non-zero subset ($n{=}238$), with 18.1~pp of unrealized oracle headroom.\nAt $N{=}16$ (Qwen3-4B, Table~\\ref{tab:re_n16_selection}), LP is the sole positive signal ($\\Delta{=}{+}0.7$~pp, $p{=}0.058$), consistent with LP being the strongest RE selection signal across scales.\n\n\\paragraph{Scale ablation.}\nAt 4B scale (Qwen3-4B, $N{=}8$, $\\text{seed}{=}42$), RE quality estimation shows FK $\\rho{=}0.359$ and LP $\\rho{=}0.351$, both above their 8B counterparts (FK 0.275, LP 0.266), while SJ declines ($0.267$ vs.\\ $0.250$).\nSelection remains below single-sample on RE ($\\Delta$ up to $-3.4$~pp) despite 17.1~pp of oracle headroom.\n\n\\paragraph{Free-form decoding.}\nRE LP selection consistently reverses direction under free-form decoding ($+1.8{\\pm}0.1$~pp across 4 seeds vs.\\ $-0.9$~pp under constrained decoding at 8B; \\S\\ref{app:freeform_ablation}); constrained decoding's fixed template likely obscures LP signal in RE (\\S\\ref{app:mbr_discussion}).\n\n\\subsection{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform single-sample on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because single-sample is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{RE $N{=}16$ Selection Analysis}\\label{app:re_n16_selection}\n\nTable~\\ref{tab:re_n16_selection} extends the selection analysis to RE at $N{=}16$ with 3-seed statistics.\nAll four consistency signals underperform single-sample, with EM showing the largest deficit ($\\Delta{=}{-}1.5$~pp, Fisher $p{>}0.99$).\nLP is the only positive signal ($\\Delta{=}{+}0.7$~pp, Fisher $p{=}0.058$), driven primarily by seed~456 ($\\Delta{=}{+}1.5$~pp, $p{=}0.026$); the remaining seeds show smaller effects ($+0.1$ and $+0.6$~pp, $p{>}0.20$).\nEven the most favorable seed captures only ${\\sim}9\\%$ of the 17.1~pp oracle headroom.\nThis cross-task consistency (LP as the only viable selection signal on both NER and RE) reinforces the persistent limitation of instance-level signals for candidate ranking across tested regimes.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\n\\label{tab:re_n16_selection}\n\\begin{tabular}{lccc}\n\\toprule\nMethod & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\n\\midrule\nOracle & $.463{\\pm}.006$ & $+$17.1 & --- \\\\\n\\midrule\nLP & $\\mathbf{.299}{\\pm}.007$ & $+$0.7 & .058 \\\\\nVC & $.284{\\pm}.002$ & $-$0.8 & .973 \\\\\nFK & $.283{\\pm}.005$ & $-$0.9 & .985 \\\\\nSJ & $.281{\\pm}.005$ & $-$1.0 & .993 \\\\\nEM & $.277{\\pm}.007$ & $-$1.5 & .999 \\\\\n\\midrule\nGreedy & $.291{\\pm}.000$ & --- & --- \\\\\nRandom & $.262{\\pm}.001$ & $-$2.9 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Theoretical Results}\\label{app:mbr_discussion}\n\n\\subsection{MBR Framework and Proof}\\label{app:mbr_proof}\n\nEntity-level construction (\\S\\ref{sec:prescriptive}) is a special case of minimum Bayes risk (MBR) decoding \\cite{kumar2004minimum, eikema2020map}, extended from candidate selection ($\\arg\\max_{y \\in \\{y_1,\\ldots,y_N\\}}$) to construction over all subsets of $E_\\cup{=}\\bigcup_i y_i$.\n\n\\begin{proposition}[Entity construction as MBR for balanced set-overlap]\\label{prop:construction_mbr}\nUnder entity-wise independence with utility $u(\\hat{y}, y') = |\\hat{y} \\cap y'| - \\alpha|\\hat{y} \\setminus y'|$ ($\\alpha \\geq 1$), the MBR-optimal constructed set is\n\\begin{equation}\\label{eq:mbr_construction}\n\\hat{y}_{\\textup{MBR}} \\!=\\! \\bigl\\{e \\!{\\in}\\! E_\\cup \\!:\\! \\hat{p}(e) \\!>\\! \\tfrac{\\alpha}{\\alpha{+}1}\\bigr\\},\\; \\hat{p}(e) \\!=\\! \\tfrac{1}{N} \\textstyle\\sum\\nolimits_{i} \\mathbf{1}[e \\!{\\in}\\! y_i]\n\\end{equation}\nThe special case $\\alpha{=}1$ yields $\\hat{p}(e) > \\tfrac{1}{2}$, the majority-vote threshold.\n\\end{proposition}\n\n\\noindent\\textbf{Remark.}\nSet-level F1 is non-linear and admits no closed-form threshold rule \\cite{dembczynski2011exact}. We use balanced linear utility ($\\alpha{=}1$ throughout); balanced set-overlap and F1 induce similar optimal thresholds for typical NER output sizes ($|E_\\cup| \\leq 30$).\n\n\\paragraph{Proof.}\nWe show that under entity-wise independence, the MBR-optimal constructed set with utility $u(\\hat{y}, y') = |\\hat{y} \\cap y'| - \\alpha|\\hat{y} \\setminus y'|$ ($\\alpha \\geq 1$) includes entity $e$ iff $\\hat{p}(e) > \\alpha/(\\alpha+1)$.\nConsider constructing $\\hat{y} \\subseteq E_\\cup$ to maximize expected utility against the empirical sample distribution.\nUnder entity-wise independence, each entity inclusion is an independent binary decision.\nFor entity $e$ with empirical frequency $\\hat{p}(e) = \\frac{1}{N} \\sum_i \\mathbf{1}[e \\in y_i]$, including $e$ contributes $+1$ when $e \\in y_i$ (probability $\\hat{p}(e)$) and $-\\alpha$ when $e \\notin y_i$ (probability $1{-}\\hat{p}(e)$).\nThe expected marginal contribution is $\\hat{p}(e) - \\alpha(1{-}\\hat{p}(e)) = (1{+}\\alpha)\\hat{p}(e) - \\alpha$, which is positive iff $\\hat{p}(e) > \\alpha/(\\alpha+1)$.\nThe special case $\\alpha{=}1$ yields the majority-vote threshold $\\hat{p}(e) > 1/2$ used throughout.\nWith F1 utility, the optimal threshold depends on the full probability vector over $E_\\cup$ \\cite{dembczynski2011exact}; the constant $1/2$ threshold is a close approximation when $|E_\\cup|$ is small (typically 5--15 in our experiments).\nThe independence assumption is approximate; we verify empirically that strict majority vote fails to improve over greedy (\\S\\ref{sec:prescriptive}; Table~\\ref{tab:alpha_crit}), consistent with marginal-entity precision falling below $\\alpha_{\\textup{crit}}$.\n\n\\subsection{Connection to MBR Decoding}\\label{app:mbr_connection}\n\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here: despite positive within-instance utility--F1 correlation, selection gains are limited by instance degeneracy, the core of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs, consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Task-specific decoding interactions.}\nThe free-form ablation shows divergent behavior across tasks.\nOn RE, LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form; preliminary, single RE benchmark), a reversal that spans all 7 relation types and is attributable to selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nThis ablation uses a single seed (seed${=}42$); whether the RE reversal replicates across seeds and generalizes to other RE benchmarks warrants further investigation.\nThe non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472: 87 instances newly gain LP discrimination while others lose it, and the newly non-tied subset shows a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible. Score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\subsection{Degeneracy Decomposition}\\label{app:bound_proof}\n\n\\begin{definition}[Instance-Level Degeneracy]\nGiven model $\\mathcal{M}$, input $x$, and $N$ i.i.d.\\ samples $\\{y_1, \\ldots, y_N\\}$, instance $x$ is \\emph{degenerate} if $y_1 = \\cdots = y_N$. The degeneracy rate is $D = |\\mathcal{D}|^{-1} \\sum_{x} \\mathbb{1}[y_1(x) = \\cdots = y_N(x)]$.\n\\end{definition}\n\n\\begin{definition}[Non-Degenerate Oracle Gap]\n$G_{\\text{nd}} = \\mathbb{E}[F_1^{\\text{oracle}}(x) - F_1^{\\text{greedy}}(x) \\mid x \\in \\mathcal{D}_{\\neg D}]$, where $\\mathcal{D}_{\\neg D}$ is the set of non-degenerate instances.\n\\end{definition}\n\n\\subsection{Proof of the Degeneracy Decomposition}\n\nPartition $\\mathcal{D}$ into degenerate ($\\mathcal{D}_D$, fraction $D$) and non-degenerate ($\\mathcal{D}_{\\neg D}$, fraction $1{-}D$). By total expectation:\n\\begin{equation}\\label{eq:bound_decomp}\n\\mathbb{E}[\\Delta F_1(A)] = D \\cdot \\mathbb{E}[\\Delta F_1 \\mid \\mathcal{D}_D] + (1{-}D) \\cdot \\mathbb{E}[\\Delta F_1 \\mid \\mathcal{D}_{\\neg D}].\n\\end{equation}\nFor degenerate instances, all $N$ samples are identical and equal the greedy output, so $\\Delta F_1 = 0$. For non-degenerate instances, $\\Delta F_1(A,x) \\leq F_1^{\\text{oracle}}(x) - F_1^{\\text{greedy}}(x)$, giving $\\mathbb{E}[\\Delta F_1 \\mid \\mathcal{D}_{\\neg D}] \\leq G_{\\text{nd}}$. Substituting: $\\mathbb{E}[\\Delta F_1(A)] \\leq (1{-}D) \\cdot G_{\\text{nd}}$.\n\nFor signal-based methods, define alignment $\\alpha = \\mathbb{E}[\\Delta F_1(A_s) \\mid \\mathcal{D}_{\\neg D}] / G_{\\text{nd}} \\in [0,1]$. Direct substitution yields $\\mathbb{E}[\\Delta F_1(A_s)] = (1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$.\n\n\\begin{corollary}[Critical Degeneracy Threshold]\\label{cor:theta_crit}\nFor SC gain to exceed significance threshold $\\varepsilon$, the degeneracy rate must satisfy $D < 1 - \\varepsilon / (G_{\\text{nd}} \\cdot \\alpha) \\stackrel{\\text{def}}{=} \\theta_{\\text{crit}}$.\nWith $\\varepsilon{=}0.3$\\,pp, $G_{\\text{nd}}{=}14.8$\\,pp, $\\alpha{=}0.068$: $\\theta_{\\text{crit}} = 1 - 0.3/(14.8 \\times 0.068) = 0.70$.\n\\end{corollary}\n\n\\paragraph{Numerical verification.}\nTable~\\ref{tab:bound_verification} verifies the bound across 16 configurations. All positive-gain configurations have $D < \\theta_{\\text{crit}}$ and actual/bound ratios of 3--12\\% (Figure~\\ref{fig:bound}). The bound is loose because $\\alpha$ (signal alignment) is the bottleneck: the best signal recovers only 6.8\\% of the non-degenerate oracle gap on average.\n\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bound verification across representative configurations ($N{=}8$). $G_{\\text{nd}}$: non-degenerate oracle gap. $\\alpha$: signal alignment. Bound: $(1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$. Ratio: actual$/$weak bound.}\n\\label{tab:bound_verification}\n\\begin{tabular}{@{}lccccr@{}}\n\\toprule\nConfig & $D$ & $G_{\\text{nd}}$ & $\\alpha$ & $\\Delta$ & Ratio \\\\\n\\midrule\nQ3-8B FT FN s123 & .131 & 14.8 & .121 & +1.56 & 12.1\\% \\\\\nQ3-8B FT FN s456 & .120 & 14.5 & .108 & +1.37 & 10.8\\% \\\\\nQ3-8B FT Sci s789 & .214 & 17.0 & .084 & +1.12 & 8.4\\% \\\\\n72B ZS Sci & .210 & 18.9 & .102 & +1.53 & 10.2\\% \\\\\nQ3-8B FT CoN s123 & .630 & 10.9 & .000 & $-$0.42 & --- \\\\\n72B ZS CoN & .677 & 16.4 & .000 & $-$0.37 & --- \\\\\n72B FS CoN & .700 & 17.0 & .047 & +0.24 & 4.7\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Entity Selection Bound: Proof and Validation}\\label{app:alpha_crit}\n\n\\begin{proposition}[Entity Selection Diagnostic]\\label{prop:entity_selection_bound}\nLet $\\mathcal{M}^+ {=} \\hat{y}_{\\textup{MV}} \\setminus \\hat{y}_{\\textup{gr}}$ be entities added by majority vote (precision $\\pi_{\\mathcal{M}^+}$) and $\\delta$ the instance degeneracy rate.\n\\begin{enumerate}[label=\\textup{(\\alph*)},nosep,leftmargin=*]\n\\item On degenerate instances, $\\hat{y}_{\\textup{MV}} {=} \\hat{y}_{\\textup{gr}}$ and $\\Delta F_1 {=} 0$.\n\\item $\\mathbb{E}[\\Delta F_1] = (1{-}\\delta) \\cdot \\mathbb{E}[\\Delta F_1 \\mid \\textup{non-deg.}]$.\n\\item $\\Delta F_1 > 0$ only if $\\pi_{\\mathcal{M}^+} > \\alpha_{\\textup{crit}} \\triangleq F_1^{\\textup{gr}}/2$.\n\\end{enumerate}\n\\end{proposition}\n\n\\begin{proof}[Proof of Proposition~\\ref{prop:entity_selection_bound}]\n\\textbf{Part (a).} On a degenerate instance, all $N$ samples produce the same entity set: $\\textup{entities}(y_1) = \\cdots = \\textup{entities}(y_N)$. For every entity $e \\in E_\\cup$, the agreement count satisfies $k(e) = N$ (if $e$ appears) or $k(e) = 0$ (if not). Hence $k(e)/N \\in \\{0,1\\}$, and the majority-vote threshold $k(e)/N \\geq 1/2$ selects exactly the entities present in any single sample---identical to the greedy output. Thus $\\hat{y}_{\\textup{MV}} = \\hat{y}_{\\textup{gr}}$ and $\\Delta F_1 = 0$.\n\n\\textbf{Part (b).} Partition instances into degenerate (fraction $\\delta$) and non-degenerate (fraction $1{-}\\delta$). By the law of total expectation:\n\\[\n\\mathbb{E}[\\Delta F_1] = \\delta \\cdot \\underbrace{\\mathbb{E}[\\Delta F_1 \\mid \\textup{deg.}]}_{= 0 \\;\\textup{by (a)}} + (1{-}\\delta) \\cdot \\mathbb{E}[\\Delta F_1 \\mid \\textup{non-deg.}].\n\\]\n\n\\textbf{Part (c).} Assume $\\mathcal{M}^- = \\hat{y}_{\\textup{gr}} \\setminus \\hat{y}_{\\textup{MV}} \\approx \\varnothing$ (greedy entities typically have agreement $k(e)/N \\approx 1$). Let $m = |\\mathcal{M}^+|$ and $\\pi = |\\mathcal{M}^+ \\cap G|/|\\mathcal{M}^+|$ denote the number and precision of entities added by MV. Define $S = |\\hat{y}_{\\textup{gr}}| + |G|$. Then:\n\\begin{align*}\n\\Delta F_1 &= \\frac{2(\\textup{TP}_{\\textup{gr}} + m\\pi)}{S + m} - \\frac{2\\,\\textup{TP}_{\\textup{gr}}}{S} \\\\\n&= \\frac{2m\\bigl(\\pi - \\textup{TP}_{\\textup{gr}}/S\\bigr)}{S + m}\n= \\frac{2m\\bigl(\\pi - F_1^{\\textup{gr}}/2\\bigr)}{S + m},\n\\end{align*}\nwhich is positive if and only if $\\pi > F_1^{\\textup{gr}}/2 \\triangleq \\alpha_{\\textup{crit}}$.\n\nWhen $\\mathcal{M}^-$ is non-empty, the condition generalizes: the net precision across the full symmetric difference $\\hat{y}_{\\textup{MV}} \\triangle \\hat{y}_{\\textup{gr}}$ must exceed a corresponding threshold. The addition-only case covers the dominant empirical regime, as greedy entities typically achieve near-unanimous agreement.\n\\end{proof}\n\n\\paragraph{Effective precision threshold.}\nFrom parts (b) and (c), MV gain is attenuated by $(1{-}\\delta)$ and requires marginal-entity precision $> \\alpha_{\\textup{crit}}$.\nEquivalently, defining $\\alpha_{\\textup{crit,eff}} {=} \\alpha_{\\textup{crit}} / (1{-}\\delta)$, MV gain requires marginal-entity precision $> \\alpha_{\\textup{crit,eff}}$; when $\\alpha_{\\textup{crit,eff}} > 1$, the required precision exceeds 1.0 and MV gain is structurally impossible regardless of entity quality.\n\n\\paragraph{Empirical validation.}\nTable~\\ref{tab:alpha_crit} reports MV performance under strict majority (count $> N/2$) using the MF4v2 pipeline (3-seed means).\nMV fails to improve F1 on any dataset: Few-NERD $\\Delta{=}{-}2.74$\\,pp, SciERC $-0.74$\\,pp, CoNLL $-0.04$\\,pp.\nWe define the effective precision threshold $\\alpha_{\\textup{crit,eff}} {=} \\alpha_{\\textup{crit}} / (1{-}\\delta)$; when $\\alpha_{\\textup{crit,eff}} > 1$, the required marginal-entity precision exceeds 1.0, making MV gain structurally impossible.\nCoNLL ($\\alpha_{\\textup{crit,eff}}{=}1.148$) confirms this: $\\Delta{=}{-}0.04{\\pm}0.15$\\,pp is indistinguishable from zero.\nFew-NERD and SciERC ($\\alpha_{\\textup{crit,eff}} {<} 1$) show significantly negative $\\Delta$, indicating that even where structural headroom exists, marginal-entity precision is insufficient.\nSciERC's lower $\\alpha_{\\textup{crit}}$ ($0.334$, vs.\\ $0.396$ for Few-NERD and $0.456$ for CoNLL) is consistent with it being the only dataset where a trained entity verifier (AUC${=}0.923$) achieves positive gain ($+1.28$\\,pp).\n\n\\begin{table}[h]\n\\centering\\small\n\\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$). $\\alpha_{\\textup{crit}} = F_1^{\\textup{gr}}/2$; $\\alpha_{\\textup{crit,eff}} = \\alpha_{\\textup{crit}} / (1{-}\\delta)$. When $\\alpha_{\\textup{crit,eff}} > 1$, MV gain is structurally impossible.}\n\\label{tab:alpha_crit}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lccccccccc@{}}\n\\toprule\nDataset & Seeds & Greedy & MV & Oracle & $\\Delta_{\\textup{SC}}$ (pp) & $\\delta$ & $\\alpha_{\\textup{crit}}$ & $\\alpha_{\\textup{crit,eff}}$ & Prediction \\\\\n\\midrule\nFew-NERD & 3 & .791 & .764 & .885 & $-2.74{\\pm}0.54$ & 8.8\\% & 0.396 & 0.434 & $\\Delta < 0$ \\\\\nCoNLL & 3 & .912 & .912 & .950 & $-0.04{\\pm}0.15$ & 60.3\\%$^*$ & 0.456 & 1.148 & $\\Delta \\approx 0$ \\\\\nSciERC & 3 & .667 & .660 & .781 & $-0.74{\\pm}0.46$ & 12.2\\% & 0.334 & 0.380 & $\\Delta < 0$ \\\\\n\\bottomrule\n\\end{tabular}}\n\n\\noindent{\\footnotesize $^*$CoNLL $\\delta{=}60.3$\\% (full test set, 3-seed) vs.\\ $61.7$\\% in Table~\\ref{tab:fewnerd} (gold-filtered); the difference reflects filtering. Tab.~\\ref{tab:pretrained_summary} reports $57$--$60$\\% (seed range, finetuned).}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B; seed${=}42$ shown, 4-seed RE statistics below).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection consistently reverses direction under free-form decoding across 4 seeds: $+1.84{\\pm}0.12$~pp (seeds 42/123/456/789: $+1.69$, $+1.76$, $+2.00$, $+1.91$~pp) vs.\\ $-0.68$~pp constrained.\nThe constrained reference ($-0.68$~pp) uses the ablation-matched baseline; the primary experiment (Table~\\ref{tab:selection}) yields $-0.9$~pp on the same gold-filtered set.\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\\,/\\,constrained within-instance LP std. Arrows: constrained $\\to$ free-form.}\n\\label{tab:freeform_summary}\n\\begin{tabular}{@{}lccc@{}}\n\\toprule\n & SciERC & CoNLL & Few-NERD \\\\\n\\midrule\nLP std ratio & $0.97{\\times}$ & $0.86{\\times}$ & $1.00{\\times}$ \\\\\nDegen.\\ (\\%) & $13.4 {\\to} 12.1$ & $56.5 {\\to} 58.8$ & $9.1 {\\to} 9.1$ \\\\\nMV $\\Delta$ (pp) & ${-}3.3 {\\to} {-}1.4$ & ${-}1.8 {\\to} {-}2.1$ & ${-}9.6 {\\to} {-}9.6$ \\\\\nGreedy F1 & $.618 {\\to} .620$ & $.907 {\\to} .905$ & $.789 {\\to} .789$ \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{CoNLL NER free-form results.}\nExtending the free-form ablation to CoNLL NER (Qwen3-8B, 4 seeds, $N{=}8$, $T{=}1.0$), LP range median is $0.058{\\pm}0.007$ across seeds, higher than SciERC ($0.041$) but still compressed given CoNLL's 86.8\\% tied fraction under constrained decoding.\nFree-form decoding reduces the tied fraction modestly, yet selection remains below single-sample: LP-selected F1${=}0.896$ vs.\\ single-sample $0.904$ ($\\Delta{=}{-}0.77$~pp).\nQuality estimation under free-form decoding yields SJ $\\rho{=}0.461$, EM $\\rho{=}0.471$, LP $\\rho{=}0.326$, comparable to constrained results (Table~\\ref{tab:quality_estimation}).\nThe failure to improve selection despite reduced compression is consistent with CoNLL's low oracle headroom (4.0~pp at $N{=}8$), which limits the selection space regardless of score distribution quality.\n\n\\paragraph{Few-NERD NER free-form results.}\nOn Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$), free-form decoding produces near-identical LP distributions (LP std ratio $1.00{\\times}$) and unchanged degeneracy ($9.1$\\%).\nGreedy F1 is unchanged ($.789$); MV degradation is comparable under both regimes ($-9.6$~pp).\nTable~\\ref{tab:freeform_summary} summarizes all three datasets: LP std ratios range from $0.86{\\times}$ to $1.00{\\times}$, confirming that LP compression is model-intrinsic and not an artifact of constrained decoding.\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ single-sample F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46); failures are partially systematic (attributable to instance complexity) but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), which constitutes a stable failure core.\n\n\\paragraph{Instance complexity co-occurs with failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher single-sample F1 (0.688 vs.\\ 0.429); LP mis-selects on instances where the model already performs well, precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\n\\label{tab:stable_failures}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is attributable to aggregate variance reallocation rather than systematic instance-level correction.\n\n\\section{$N$-Scaling Detailed Analysis}\\label{app:n_scaling}\n\nTables~\\ref{tab:n-scaling}--\\ref{tab:sigma-comparison} provide detailed $N$-scaling analysis on Qwen3-8B SciERC with 3-seed statistics.\n\n\\begin{table}[t]\n\\centering\n\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\n\\label{tab:n-scaling}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{NER} $\\rho$} & \\multicolumn{3}{c}{\\textbf{RE} $\\rho$} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ & $N\\!=\\!8$ & $N\\!=\\!16$ & $\\Delta$ \\\\\n\\midrule\nSJ & 0.3641 & 0.4105 & \\textbf{+0.0464} & 0.2485 & 0.2758 & \\textbf{+0.0273} \\\\\nFK & 0.2536 & 0.2833 & \\textbf{+0.0297} & 0.2903 & 0.2964 & \\textbf{+0.0061} \\\\\nVC & 0.3861 & 0.4092 & \\textbf{+0.0231} & 0.3088 & 0.3738 & \\textbf{+0.0650} \\\\\nLP & 0.2167 & 0.2393 & \\textbf{+0.0226} & 0.2970 & 0.3100 & \\textbf{+0.0130} \\\\\nEM & 0.3071 & 0.3395 & \\textbf{+0.0324} & 0.1353 & 0.1506 & \\textbf{+0.0153} \\\\\n\\midrule\nMean & 0.3055 & 0.3364 & \\textbf{+0.0308} & 0.2560 & 0.2813 & \\textbf{+0.0253} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\n\\label{tab:ranking-stability}\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ll cc l}\n\\toprule\nModel & Task & $N$ & Kendall's $W$ & Consensus ranking \\\\\n\\midrule\nQwen  & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\nQwen  & NER & 16 & 0.956 & SJ $\\approx$ VC $>$ EM $>$ FK $>$ LP \\\\\nQwen  & RE  & 8  & 0.822 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nQwen  & RE  & 16 & 0.956 & VC $>$ LP $>$ FK $>$ SJ $>$ EM \\\\\nLLaMA & NER & 8  & 1.000 & VC $>$ SJ $>$ EM $>$ FK $>$ LP \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\n\\label{tab:sigma-comparison}\n\\small\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{NER} $\\sigma_\\rho$} & \\multicolumn{2}{c}{\\textbf{RE} $\\sigma_\\rho$} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nSignal & $N\\!=\\!8$ & $N\\!=\\!16$ & $N\\!=\\!8$ & $N\\!=\\!16$ \\\\\n\\midrule\nSJ & 0.0179 & 0.0102 & 0.0015 & 0.0067 \\\\\nFK & 0.0157 & 0.0079 & 0.0121 & 0.0143 \\\\\nVC & 0.0187 & 0.0260 & 0.0244 & 0.0158 \\\\\nEM & 0.0076 & 0.0031 & 0.0157 & 0.0049 \\\\\nLP & 0.0125 & 0.0017 & 0.0218 & 0.0152 \\\\\n\\midrule\nMean & 0.0145 & 0.0098 & 0.0151 & 0.0114 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSignal rankings are consistent across our 3 seeds (Kendall's $W{=}1.000$ for NER at $N{=}8$, both models), dropping to $W{=}0.956$ at $N{=}16$ where SJ and VC converge (Table~\\ref{tab:ranking-stability}); however, with only $n{=}3$ seeds statistical power is insufficient to confirm stability, and additional seeds may reveal ranking changes.\nDoubling $N$ reduces cross-seed $\\sigma$ by 32\\% on NER and 24\\% on RE (Table~\\ref{tab:sigma-comparison}), with the largest reductions for SJ ($-43\\%$ NER) and EM ($-59\\%$ NER); additional samples stabilize structural signals more than LP.\n\n\\paragraph{$N$-scaling: selection headroom vs.\\ selection gain.}\nTable~\\ref{tab:n_scaling_selection} traces the effect of sample count on degeneracy, oracle headroom, and per-signal selection gain.\nOracle headroom grows roughly linearly with $N$ ($+4.4$~pp at $N{=}2$ to $+20.0$~pp at $N{=}32$).\nLP selection improves monotonically with $N$ ($+0.39$~pp at $N{=}8$ to $+0.95$~pp at $N{=}32$), but even at $N{=}32$, where degeneracy falls to 4\\% and oracle headroom reaches ${\\sim}20$~pp, the best signal captures less than 5\\% of the available improvement.\nDegeneracy drops monotonically (43\\% at $N{=}2$ to 4\\% at $N{=}32$), yet reduced degeneracy does not unlock selection, consistent with the LoRA-rank ablation finding (\\S\\ref{sec:robustness_main}).\nVC selection degrades with increasing $N$ ($-2.66$~pp at $N{=}2$ to $-4.35$~pp at $N{=}32$), consistent with mode-seeking bias in voting-based selection as the candidate pool grows.\n\n\\paragraph{Few-NERD $N$-scaling: MV at $N{=}16$.}\nOn Few-NERD (Qwen3-8B, 3-seed), increasing from $N{=}8$ to $N{=}16$ reduces degeneracy ($8.8$\\%$\\to$$4.0{\\pm}1.4$\\%) and attenuates MV degradation ($-2.74$\\,pp$\\to$$-1.65{\\pm}0.61$\\,pp), but MV remains negative.\nAdditional samples reduce the MV penalty but do not reverse it, consistent with the correlated-error mechanism: more samples provide better frequency estimates but cannot overcome systematic shared mistakes.\nSJ $\\rho$ is used for quality estimation at $N{=}16$ (FK conditional $\\rho$ shows sign instability across seeds: mean${=}0.051{\\pm}0.062$).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\n\\label{tab:n_scaling_selection}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ccccccccc}\n\\toprule\n$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\n\\midrule\n2 & 42.7\\% & $+$4.4 & $-$0.89 & $-$2.72 & $-$2.72 & $-$2.72 & $-$2.66 & $-$0.89 \\\\\n4 & 21.0\\% & $+$10.2 & $+$0.03 & $-$0.31 & $-$0.40 & $-$0.74 & $-$2.16 & $+$0.03 \\\\\n8 & 11.0\\% & $+$14.5 & $+$0.39 & $+$0.20 & $+$0.15 & $-$0.77 & $-$2.87 & $+$0.39 \\\\\n16 & 7.4\\% & $+$17.7 & $+$0.78 & $+$0.24 & $-$0.02 & $-$0.06 & $-$3.95 & $+$0.78 \\\\\n32 & 4.0\\% & $+$20.0 & $+$0.95 & $+$0.35 & $+$0.65 & $+$0.22 & $-$4.35 & $+$0.95 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\\footnotetext{$N$-scaling analysis uses gold-filtered evaluation ($n{=}529$, greedy F1${=}0.640$, seed 42). Values differ from Table~\\ref{tab:selection} (0.645, 2-seed) and Table~\\ref{tab:fewnerd} (0.663, 3-seed) due to seed and aggregation differences; relative trends are consistent.}\n\n\\paragraph{Bootstrap significance at $N{=}32$.}\nTable~\\ref{tab:bootstrap_n32} reports bootstrap confidence intervals and $p$-values for selection at $N{=}32$ ($B{=}10{,}000$, $n{=}529$).\nNo signal achieves significant improvement over greedy at $\\alpha{=}0.05$ (LP: $p{=}0.091$; FK: $p{=}0.101$), while VC is significantly \\textit{worse} ($-4.36$~pp, $p{=}1.0$).\nHowever, all signals except VC significantly outperform random selection ($p{<}0.001$, permutation test); the signals carry meaningful quality information yet fail to translate it into reliable selection gains.\nThe oracle gap ($+20.0$~pp, $p{<}0.001$) confirms substantial unrealized headroom.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\n\\label{tab:bootstrap_n32}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\Delta$ (pp) & 95\\% CI & $p_{\\text{greedy}}$ & $p_{\\text{rand}}$ \\\\\n\\midrule\nLP & $+$0.95 & [$-$0.41, $+$2.34] & 0.091 & ${<}$0.001 \\\\\nFK & $+$0.66 & [$-$0.36, $+$1.67] & 0.101 & ${<}$0.001 \\\\\nSJ & $+$0.36 & [$-$0.66, $+$1.38] & 0.244 & ${<}$0.001 \\\\\nEM & $+$0.22 & [$-$0.99, $+$1.44] & 0.355 & ${<}$0.001 \\\\\nVC & $-$4.36 & [$-$6.26, $-$2.37] & 1.000 & 0.741 \\\\\n\\midrule\nOracle & $+$20.00 & [$+$17.98, $+$22.10] & ${<}$0.001 & --- \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Oracle ceiling scaling law.}\nOracle F1 follows $F_1(N) = a - b \\cdot N^{-c}$, with $R^2 > 0.999$ across all model--dataset fits (Figure~\\ref{fig:oracle_scaling}).\nThe exponent $c$ varies with dataset complexity: Few-NERD ($c{\\approx}0.61$) scales comparably to reasoning-task estimates ($c{\\approx}0.5$--$0.7$; \\citealp{brown2024monkeys}), while SciERC converges more slowly ($c{\\approx}0.35$), consistent with complex IE producing less marginal diversity per additional sample.\nCoNLL's narrow headroom ($b{=}0.04$--$0.10$) makes $c$ unreliable (inter-model variance $2.5{\\times}$); we report only $a$ and $b$ for CoNLL.\nA single stochastic sample ($N{=}1$, $T{=}1.0$) underperforms greedy by 1--3\\,pp because sampling noise outweighs diversity; $N{\\geq}4$ is needed to match greedy.\n\n\n\\paragraph{Degeneracy and inverse scaling.}\\label{app:degen_inverse}\nTable~\\ref{tab:degen_inverse} stratifies $N$-transitions by instance degeneracy status across all dataset--regime combinations.\nDegenerate instances exhibit near-zero inverse scaling ($1.3$\\% vs.\\ $11.1$\\% for non-degenerate; OR${=}0.109$, $p{<}10^{-300}$, Fisher's exact test over $195{,}675$ transitions).\nThis is expected: degenerate instances produce identical entity sets across all $N$ samples, so MV F1 is constant by construction---they cannot exhibit inverse scaling.\nThe effect holds across all settings (Table~\\ref{tab:degen_inverse}), with the sole exception of SciERC pretrained ($p{=}0.083$), where low degeneracy (${\\leq}10$\\%) yields too few degenerate transitions for adequate power.\nPretrained models show a stronger protective effect (OR${=}0.066$ vs.\\ $0.166$ for finetuned), consistent with higher overall inverse scaling rates creating more room for the degeneracy--stability association.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Inverse scaling rate by degeneracy status. An $N{\\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}\n\\label{tab:degen_inverse}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrrrrrc@{}}\n\\toprule\nSetting & \\multicolumn{2}{c}{Degenerate} & \\multicolumn{2}{c}{Non-degenerate} & OR & $p$ \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\n & Trans. & Inv.\\% & Trans. & Inv.\\% & & \\\\\n\\midrule\nSciERC FT & 485 & 0.8 & 2{,}160 & 9.6 & 0.078 & ${<}10^{-6}$ \\\\\nCoNLL FT & 8{,}256 & 0.3 & 5{,}524 & 4.1 & 0.060 & ${<}10^{-6}$ \\\\\nFew-NERD FT & 22{,}298 & 1.9 & 75{,}397 & 8.4 & 0.213 & ${<}10^{-6}$ \\\\\nSciERC PT & 81 & 3.7 & 2{,}564 & 9.9 & 0.350 & 0.083 \\\\\nCoNLL PT & 5{,}284 & 0.3 & 8{,}496 & 7.9 & 0.033 & ${<}10^{-6}$ \\\\\nFew-NERD PT & 18{,}007 & 1.4 & 47{,}123 & 16.8 & 0.071 & ${<}10^{-6}$ \\\\\n\\midrule\n\\textbf{All} & \\textbf{54{,}411} & \\textbf{1.3} & \\textbf{141{,}264} & \\textbf{11.1} & \\textbf{0.109} & $\\mathbf{{<}10^{-300}}$ \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Cross-Scale and Cross-Family Comparison}\\label{app:cross_scale}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .667 & 11.4 & 12.2 & .326 & .324 & .177 & .159 \\\\\n       & 72B ZS$^\\star$ & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\n         & 8B FT & .748 & 12.4 & 13.0 & .386 & .300 & .313 & .220 \\\\\n         & 14B FT & .798 & 8.1 & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ \\\\\n         & 72B ZS$^\\star$ & .628 & ---$^\\dagger$ & 46.2 & .416 & .345 & ---$^\\dagger$ & .119 \\\\\n         & GPT-5.5 ZS$^\\ddagger$ & .638 & 8.2 & 50.0 & ---$^\\dagger$ & .346 & ---$^\\dagger$ & ---$^\\dagger$ \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS$^\\star$ & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\n\n\\paragraph{Few-shot demonstrations improve QE but not construction.}\nAdding 3-shot demonstrations to 72B improves greedy on SciERC and CoNLL ($+3.3$--$6.2$\\,pp) but not Few-NERD ($-0.9$\\,pp), and strengthens structural QE (CoNLL SJ $\\rho$ $.304{\\to}.442$, LP $-.002{\\to}.106$). Yet construction is ineffective across all three datasets (SciERC $-0.08$\\,pp, CoNLL $+0.03$\\,pp, Few-NERD $+0.02$\\,pp; all n.s.). On SciERC, this failure despite low degeneracy shows the bottleneck is regime-dependent (Appendix~\\ref{app:fs_error}); on Few-NERD, high FS degeneracy ($45.2$\\%) places it in the expected failure regime.\n\n\\paragraph{Degeneracy is model-family-dependent, not scale-dependent.}\nQwen2.5 exhibits systematically higher degeneracy than Qwen3 on Few-NERD (7B--72B: $31.7$--$46.2$\\% vs.\\ Qwen3-8B: $13.0$\\%; Table~\\ref{tab:scale_comparison}), confirming degeneracy is shaped by architecture rather than parameter count. Construction fails for all Qwen2.5 configurations on Few-NERD (both n.s.); 3$\\to$5 epochs triples degeneracy within the same model (\\S\\ref{sec:fewnerd}).\n\n\\paragraph{Qwen3 8B vs.\\ 4B scale ablation.}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Scale ablation: Qwen3 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\n\\label{tab:scale_ablation_app}\n\\begin{tabular}{@{}ll cc r@{}}\n\\toprule\n& & \\textbf{8B} & \\textbf{4B} & $\\Delta$ \\\\\n\\midrule\nCoNLL & SJ & .436 & .422 & $-$.014 \\\\\n      & FK & .400 & .418 & $+$.018 \\\\\nSciERC & SJ & .360 & .422 & $+$.062 \\\\\n       & FK & .267 & .326 & $+$.059 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDegeneracy scales with capability: 8B shows 12.2\\% vs.\\ 4B's 10.4\\% on SciERC (Table~\\ref{tab:degeneracy}).\n\n\\paragraph{14B scale extension.}\nQwen3-14B fine-tuned on Few-NERD achieves greedy F1${=}0.798$ ($+0.9$\\,pp over 8B) with oracle headroom of 8.1\\,pp ($+1.2$\\,pp over 8B's 6.9\\,pp) and $\\rho$ advantage $+0.029$ over 8B.\nThe ceiling grows with model capability: larger models improve both greedy and oracle performance, but the aggregation gap widens rather than closes.\n\n\\paragraph{Pre-trained baseline (no fine-tuning).}\nTable~\\ref{tab:pretrained_summary} summarizes pretrained-vs-finetuned MV performance across three datasets (Qwen2.5-7B-Instruct pretrained, Qwen3-8B LoRA finetuned; $N{=}8$, $T{=}1.0$).\nAcross all three datasets, pretrained models benefit from MV aggregation ($+1.7$ to $+9.2$\\,pp), while all finetuned models show negligible or negative MV gains.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Pretrained vs.\\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\\text{MV}\\,\\Delta / \\text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\\pm}\\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}\n\\label{tab:pretrained_summary}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccc@{}}\n\\toprule\nDataset & Setting & Greedy & MV $\\Delta$ (pp) & Degen.\\% & Capture & $\\rho_{\\textup{SJ}}$ \\\\\n\\midrule\nCoNLL & Pretrained & .536 & $+$9.2 & 36 & 98\\% & .467 \\\\\n      & Finetuned & .912 & ${<}$0.1 & 57--60 & ${<}$2\\% & .41--.45 \\\\\n\\addlinespace\nFew-NERD & Pretrained ($N{=}8$) & .538 & $+$3.9${\\pm}$0.2 & 11.7 & 36\\% & .436 \\\\\n         & Pretrained ($N{=}16$) & .537 & $+$4.1 & 7.6 & 29\\% & .453 \\\\\n         & Pretrained ($N{=}32$) & .539 & $+$3.9 & 5.4 & 19\\% & .456 \\\\\n         & Finetuned & .791 & $-$2.7${\\pm}$0.5 & 8.8 & neg. & .31 \\\\\n\\addlinespace\nSciERC & Pretrained & .244 & $+$1.7${\\pm}$0.4 & 0.8 & --- & --- \\\\\n       & Finetuned & .667 & ${<}$0.1 & 12.2 & --- & .36 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nOn CoNLL, MV captures $98$\\% of oracle headroom for the pretrained model (greedy${=}0.536$, MV${=}0.628$, oracle${=}0.630$, degeneracy${=}36$\\%) versus ${<}2$\\% finetuned (greedy${=}0.912$, MV${=}0.912$, oracle${=}0.954$, degeneracy $57$--$60$\\%).\nSignal quality is comparable ($\\rho_{\\textup{SJ}}{=}0.47$ pretrained vs.\\ $0.41$--$0.45$ finetuned).\n\nOn Few-NERD ($n{=}32{,}565$, 3-seed), finetuned degeneracy ($8.8$\\%) is \\textit{lower} than pretrained ($11.7$\\%), yet finetuned MV is negative ($-2.74{\\pm}0.54$\\,pp).\nDoubling the sample budget ($N{=}8{\\to}16$) maintains the pretrained MV advantage ($+4.06$\\,pp) while reducing degeneracy ($11.7{\\to}7.6$\\%) and expanding oracle headroom ($+2.9$\\,pp); however, capture rate decreases ($36{\\to}29$\\%), indicating diminishing marginal returns from additional samples.\n$N{=}32$ confirms the plateau (MV $\\Delta{=}+3.9$\\,pp), with capture rate declining further to $19$\\%.\nFine-tuning thus decouples agreement from quality through dataset-dependent pathways: diversity elimination on CoNLL (degeneracy $36{\\to}57$--$60$\\%), but correlated error patterns on Few-NERD.\nA baseline quality confound exists (pretrained greedy${=}0.538$ vs.\\ finetuned${=}0.791$); per-type analysis (Appendix~\\ref{app:pertype}) partially addresses this by showing MV degradation concentrates in low-F1 entity types ($\\rho{=}0.90$, $p{=}0.002$).\n\nOn SciERC, MV gains $+1.67{\\pm}0.40$\\,pp despite very low greedy F1 ($0.244$) with near-zero degeneracy ($0.8$\\%), contradicting a ``MV only works at high baseline'' explanation.\nStructural signals outperform surface on CoNLL ($\\rho_{\\textup{SJ}}{=}0.467$, $\\rho_{\\textup{FK}}{=}0.435$) and LP AUROC${=}0.580$.\nSciERC's low greedy F1 does establish a scope boundary for entity-level \\textit{construction}: 46\\% of samples produce F1${=}0$, so partial-correctness-based aggregation cannot improve over greedy.\n\n\\subsection{Per-Type MV Analysis}\\label{app:pertype}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}\n\\label{tab:pertype_mv}\n\\begin{tabular}{@{}lrccc@{}}\n\\toprule\n& & & \\multicolumn{2}{c}{MV $\\Delta$ (pp)} \\\\\n\\cmidrule(lr){4-5}\nEntity type & $n$ & Greedy F1 & Pretr. & Finetuned \\\\\n\\midrule\nperson & ${\\sim}$7{,}200 & .820 & $+$4.17 & $-$0.67 \\\\\nlocation & ${\\sim}$8{,}800 & .797 & $+$2.47 & $-$1.52 \\\\\nart & ${\\sim}$1{,}250 & .755 & $+$0.73 & $-$1.51 \\\\\norganization & ${\\sim}$6{,}700 & .725 & $+$3.15 & $-$2.65 \\\\\nbuilding & ${\\sim}$1{,}540 & .696 & $+$1.98 & $-$3.90 \\\\\nproduct & ${\\sim}$2{,}260 & .657 & $+$1.78 & $-$3.38 \\\\\nevent & ${\\sim}$1{,}315 & .645 & $+$2.34 & $-$3.17 \\\\\nother & ${\\sim}$3{,}485 & .639 & $-$0.45 & $-$3.02 \\\\\n\\midrule\n\\multicolumn{3}{@{}l}{$r$(greedy F1, MV\\,$\\Delta$)} & .86 & .90 \\\\\n\\multicolumn{3}{@{}l}{$p$-value} & .006 & .002 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\nMV direction flips between pretrained and finetuned decoding for 7 of 8 entity types (Table~\\ref{tab:pertype_mv}): types that benefit from MV under pretrained decoding ($+0.73$ to $+4.17$\\,pp) are uniformly harmed under finetuning ($-0.67$ to $-3.90$\\,pp), with only \\textit{other} (lowest-F1) remaining negative in both regimes.\nThe correlation between greedy F1 and MV $\\Delta$ is strong in both regimes ($r{=}0.86$, $p{=}0.006$ pretrained; $r{=}0.90$, $p{=}0.002$ finetuned), indicating entity-type difficulty predicts MV magnitude regardless of direction.\nThis rules out entity-type-specific factors as the explanation for MV failure: the same types succeed with pretrained decoding and fail with finetuned decoding, implicating the finetuning process itself.\nUnder a liberal MV threshold ($\\theta{\\geq}N/2$ instead of $\\theta{>}N/2$), per-type correlation direction is unstable; all results above use strict MV, consistent with the main paper.\n\n\\subsection{Frontier Model Self-Consistency}\\label{app:frontier_sc}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}\n\\label{tab:frontier_sc_cross}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lcccccc@{}}\n\\toprule\nModel & Greedy & MV ($\\Delta$) & Oracle & Degen.\\% & Sel.\\ gap & Parse\\% \\\\\n\\midrule\nDeepSeek & .399 & .424 ($+2.5$) & .714 & 5.5 & .290 & 46.9 \\\\\nGemini 2.5 Pro & .630 & .645 ($+1.5$) & .758 & 28.5 & .113 & 11.9 \\\\\nGPT-5.5 & .638 & .652 ($+1.4$) & .720 & 50.0 & .068 & 10.1 \\\\\nClaude Son.~4 & .607 & .623 ($+1.6$) & .654 & 74.0 & .032 & 6.4 \\\\\n\\midrule\nQwen3-8B FT & .789 & .792 ($+0.3$) & .858 & 13.0 & .066 & ${\\approx}$0 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nAll four frontier families exhibit the correlation-selection gap (Table~\\ref{tab:frontier_sc_cross}): MV recovers only a fraction of oracle headroom regardless of model capability.\nDegeneracy and selection gap are negatively correlated across families: Claude Sonnet~4 (74\\% degen, 0.032 gap) vs.\\ DeepSeek (5.5\\%, 0.290)---higher degeneracy eliminates the instances where aggregation could help.\nGemini 2.5 Pro achieves the highest oracle F1 (.758) and the highest QE correlation ($\\rho_{\\textup{SJ}}{=}0.350$, $\\rho_{\\textup{agr}}{=}0.389$) among frontier models, with balanced degeneracy (28.5\\%) preserving a 0.113 selection gap---the largest gap among models with ${\\geq}85$\\% parse success.\nDeepSeek's low degeneracy preserves the largest absolute gap (.290), but 47\\% parse failures reduce effective $N$ to ${\\approx}4.2$, limiting aggregation benefit.\nGPT-5.5 occupies the middle ground: 50\\% degeneracy with 6.8\\,pp unrealized oracle headroom.\n\n\\paragraph{Parse failure handling.}\n10.1\\% of GPT-5.5 samples produced output that could not be parsed into valid entity sets.\nThese samples are excluded from all aggregation metrics (degeneracy, oracle, MV, selection); for instances where all $N$ samples fail parsing, the instance is excluded entirely.\nThe effective sample size per instance is therefore $N_{\\textit{eff}} \\leq 8$ (mean ${\\approx}7.2$).\n\n\\paragraph{Entity matching methodology.}\nLocal experiments (fine-tuned models with constrained decoding) use offset-based matching: two entities match iff \\texttt{(start, end, type)} are identical.\nFrontier API experiments use text-based matching: \\texttt{(text.lower(), type)}, because API outputs lack character-offset information.\nText-based matching is slightly more permissive (e.g., ignoring whitespace differences at span boundaries), producing ${\\approx}2$\\,pp higher MV $\\Delta$ on controlled comparisons.\nAll within-pipeline comparisons (greedy vs.\\ MV vs.\\ oracle) use the same matching, so relative conclusions are unaffected; cross-pipeline absolute F1 values should not be directly compared.\n\n\\section{Temperature Ablation}\\label{app:t_ablation}\n\nTable~\\ref{tab:t_ablation} reports the effect of sampling temperature on QE signals, oracle headroom, and output quality across four temperatures on SciERC NER.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\n\\label{tab:t_ablation}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ccccccc}\n\\toprule\n$T$ & Oracle gap (pp) & SJ $\\rho$ & LP $\\rho$ & $\\kappa$ & Sample F1 \\\\\n\\midrule\n0.5 & $+$9.1 & 0.297 & 0.218 & 0.577 & 0.636 \\\\\n0.8 & $+$12.5 & 0.359 & 0.253 & 0.451 & 0.622 \\\\\n1.0 & $+$13.0 & 0.360 & 0.205 & ${\\approx}$0.39 & ${\\approx}$0.612 \\\\\n1.2 & $+$14.6 & 0.377 & 0.196 & 0.356 & 0.594 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nOracle headroom increases monotonically with temperature ($+9.1$~pp at $T{=}0.5$ to $+14.6$~pp at $T{=}1.2$), confirming that higher temperature consistently expands the oracle ceiling under constrained structured decoding.\nStructural QE signals improve with temperature: SJ $\\rho$ rises from $0.297$ ($T{=}0.5$) to $0.377$ ($T{=}1.2$), consistent with more diverse outputs providing richer pairwise evidence.\nLP $\\rho$ peaks at $T{=}0.8$ ($0.253$) then degrades to $0.196$ at $T{=}1.2$.\nThis divergence confirms that LP compression is model-intrinsic: higher temperature increases between-instance LP variance (benefiting structural signals) but does not resolve within-instance compression, degrading LP's discriminative power.\nInter-sample agreement ($\\kappa$) decreases monotonically ($0.577$ to $0.356$); higher temperature generates more diverse outputs. Mean sample F1 also decreases ($0.636$ to $0.594$), consistent with the quality--diversity trade-off.\nThe $T{=}0.7$ and $T{=}1.0$ comparison in Table~\\ref{tab:robustness} is consistent with the trends reported here.\n\n\\paragraph{Temperature modulates degeneracy and LP spread.}\nTable~\\ref{tab:t_degeneracy} reports instance degeneracy (constant F1, gold-filtered) and median within-instance LP range across four temperatures on SciERC.\nBoth quantities are strictly monotonic in $T$: degeneracy falls from 41.4\\% ($T{=}0.5$) to 14.9\\% ($T{=}1.2$), while LP range increases from 0.015 to 0.058 nats.\nTemperature thus provides a direct lever for practitioners to shift the degeneracy regime.\nHowever, even at $T{=}1.2$ where degeneracy (14.9\\%) approaches Few-NERD levels (${\\sim}$13\\%), within-instance $\\rho(\\text{LP}, \\text{F1})$ remains at 0.225, far below Few-NERD's ${\\sim}$0.5.\nThis confirms that temperature modulates degeneracy but cannot improve LP-quality alignment, which is largely associated with task structure and remains relatively stable across generation configurations (\\S\\ref{app:epoch_confound}). LP-quality alignment, not degeneracy, is the primary predictor of LP selection direction (\\S\\ref{sec:discussion}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\n\\label{tab:t_degeneracy}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ccccc}\n\\toprule\n$T$ & Degen.\\% & LP range (nats) & Fleiss' $\\kappa$ & SJ mean \\\\\n\\midrule\n0.5 & 41.4 & 0.015 & 0.572 & 0.830 \\\\\n0.8 & 23.8 & 0.031 & 0.471 & 0.752 \\\\\n1.0 & 17.8 & 0.042 & 0.405 & 0.700 \\\\\n1.2 & 14.9 & 0.058 & 0.352 & 0.647 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\section{Cross-Dataset OOD Analysis}\\label{app:ood}\n\nTo test whether confidence signals generalize under domain shift, we evaluate models on out-of-distribution data: a SciERC-trained model applied to CoNLL instances (wider$\\to$narrower schema) and vice versa (Table~\\ref{tab:ood}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\n\\label{tab:ood}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{\\textbf{SciERC$\\to$CoNLL}} & \\multicolumn{3}{c}{\\textbf{CoNLL$\\to$SciERC}} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & $\\rho$ & In-dom. & $\\Delta$ & $\\rho$ & In-dom. & $\\Delta$ \\\\\n\\midrule\nVC & .469\\textsuperscript{***} & .379 & +.090 & +.105\\textsuperscript{*} & .379 & $-$.274 \\\\\nSJ & .378\\textsuperscript{***} & .360 & +.018 & $-$.186\\textsuperscript{***} & .360 & $-$.546 \\\\\nEM & .300\\textsuperscript{***} & .295 & +.005 & $-$.202\\textsuperscript{***} & .295 & $-$.497 \\\\\nFK & .285\\textsuperscript{***} & .267 & +.018 & $-$.070 & .267 & $-$.337 \\\\\nLP & .246\\textsuperscript{***} & .205 & +.041 & $-$.152\\textsuperscript{***} & .205 & $-$.357 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Wider-to-narrower schema transfer.}\nWhen the SciERC-trained model (6 NER types) is applied to CoNLL (4 types), all signals remain significant ($p{<}0.001$) and structural signals improve over their in-domain levels (same model, seed${=}42$, $N{=}8$; in-domain $\\rho$ from Table~\\ref{tab:quality_estimation}): VC reaches $\\rho{=}0.469$ (in-domain $0.379$, $\\Delta{=}{+}0.090$), SJ $\\rho{=}0.378$ (in-domain $0.360$, $\\Delta{=}{+}0.018$), and FK $\\rho{=}0.285$ (in-domain $0.267$, $\\Delta{=}{+}0.018$).\nThe wider training schema subsumes CoNLL's narrower schema, so the model produces reasonable outputs even out-of-domain (single-sample F1${=}0.522$), and structural signals benefit from the simpler target schema's reduced output ambiguity.\n\n\\paragraph{Narrower-to-wider schema transfer (excluded).}\nThe reverse direction is excluded from our conclusions due to catastrophic model failure, not signal failure.\nThe CoNLL-trained model recognizes only 4 news entity types (PER, ORG, LOC, MISC) and has no relation extraction capability; when applied to SciERC's 6 scientific entity types and 7 relation types, the model cannot produce meaningful structured outputs (single-sample NER F1${=}0.009$, RE F1${=}0.001$).\nUnder this regime, most signals flip to negative or near-zero correlations (Table~\\ref{tab:ood}); only VC retains weak positive correlation ($\\rho{=}0.105$, $p{=}0.016$).\nThese negative correlations reflect the model systematically generating confident but incorrect outputs, a capability failure analogous to WNUT-17 (\\S\\ref{sec:qe_results}) and not evidence against signal utility.\n\n\\paragraph{Asymmetry interpretation.}\nThe directional asymmetry is attributable to schema coverage: wider$\\to$narrower preserves signal utility because the SciERC model's 6-type schema subsumes CoNLL's 4 types, while narrower$\\to$wider fails because the CoNLL model lacks the entity and relation types required by SciERC.\nThis extends the capability boundary identified on WNUT-17 to the domain-shift setting: confidence signals require sufficient model capability as a prerequisite, and results from the CoNLL$\\to$SciERC direction should not be interpreted as evidence of signal degradation under domain shift.\n\n\\section{Verbalized Confidence}\\label{app:verbalized_confidence}\n\nWe evaluate verbalized confidence (VerbConf) as a second per-sample signal following \\citet{lin2022teaching} and \\citet{tian2023calibration}: after generating each structured output, the model is prompted to rate its confidence on a 1--10 scale.\nTable~\\ref{tab:verbconf} reports quality estimation and selection results.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\n\\label{tab:verbconf}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{l cc cc}\n\\toprule\n & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{CoNLL NER}} \\\\\n\\cmidrule(lr){2-3} \\cmidrule(lr){4-5}\nMetric & VerbConf & LP & VerbConf & LP \\\\\n\\midrule\n$\\rho$ & 0.297 & 0.205 & 0.337 & 0.316 \\\\\nAUROC & 0.681 & 0.578 & 0.747 & 0.753 \\\\\nSelection F1 & 0.620 & 0.647 & 0.889 & 0.904 \\\\\n$\\Delta$ vs.\\ greedy & $-$2.45\\,pp & $+$0.2\\,pp & $-$1.93\\,pp & $-$0.77\\,pp \\\\\n\\midrule\nMean score & 8.58\\,/\\,10 & --- & 9.24\\,/\\,10 & --- \\\\\nParse fail rate & 0.26\\% & --- & 0\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Severe overconfidence.}\nVerbConf exhibits extreme score compression: mean confidence is 8.58/10 on SciERC (single-sample F1${=}0.645$) and 9.24/10 on CoNLL (single-sample F1${=}0.904$), with most scores concentrated in the 8--10 range.\nThis compression is more severe than LP (which spans a 0.041-nat median range); score compression is a general property of model self-assessment, not an artifact of log-probability computation.\n\n\\paragraph{QE--selection decoupling.}\nVerbConf achieves higher $\\rho$ than LP on both datasets (SciERC: 0.297 vs.\\ 0.205; CoNLL: 0.337 vs.\\ 0.316) and competitive AUROC (SciERC: 0.681 vs.\\ 0.578; CoNLL: 0.747 vs.\\ 0.753), yet yields the worst selection among all signals ($\\Delta{=}{-}2.45$~pp on SciERC, $-1.93$~pp on CoNLL).\nThis dissociation further demonstrates the correlation-selection gap: a signal can rank instances by expected quality without being able to discriminate candidates within an instance.\nThe AUROC--$\\rho$ decoupling on CoNLL (LP leads AUROC at 0.753 while VerbConf leads $\\rho$ at 0.337) reflects differing sensitivity to binary vs.\\ ordinal discrimination.\n\n\\section{LLaMA-3.2-3B Scale Ablation}\\label{app:llama3b}\n\nTo extend scale coverage below 4B, we fine-tune LLaMA-3.2-3B-Instruct on SciERC NER under identical training conditions (LoRA rank${=}32$, $\\alpha{=}64$, 5 epochs) and evaluate quality estimation and selection (Table~\\ref{tab:llama3b}).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\n\\label{tab:llama3b}\n\\begin{tabular}{l cc cc}\n\\toprule\nSignal & $\\rho$ & AUROC & Sel.\\ F1 & $\\Delta$ vs.\\ greedy \\\\\n\\midrule\nVC & \\textbf{.460} & .743 & 0.611 & $-$1.54\\,pp \\\\\nSJ & .375 & .738 & \\textbf{0.633} & $+$0.61\\,pp \\\\\nEM & .334 & \\textbf{.776} & --- & --- \\\\\nFK & .268 & .671 & 0.630 & $+$0.28\\,pp \\\\\nLP & .266 & .633 & 0.628 & $+$0.12\\,pp \\\\\n\\midrule\nGreedy & --- & --- & 0.627 & --- \\\\\nOracle & --- & --- & 0.763 & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe $\\rho$ ranking at 3B (VC $>$ SJ $>$ EM $>$ FK $\\approx$ LP) preserves the structural-over-LP ordering from 8B (Table~\\ref{tab:quality_estimation}); ranking stability holds across two model families spanning 3B--8B.\nAUROC rankings differ (EM $>$ VC $>$ SJ $>$ FK $>$ LP), consistent with the $\\rho$--AUROC dissociation noted in the main text.\nDespite 13.63~pp of oracle headroom, no signal achieves significant selection improvement (best: SJ, $+0.61$~pp, $p{=}0.175$); VC, the strongest QE signal, yields the worst selection ($-1.54$~pp), consistent with the correlation-selection gap observed at larger scales.\n\n\\section{Few-NERD Full Results}\\label{app:fewnerd}\n\nTable~\\ref{tab:fewnerd_full} reports the complete Few-NERD INTRA coarse evaluation (Qwen3-8B, LoRA rank${=}32$, 3 epochs, $N{=}8$, $T{=}1.0$).\nAfter gold-filtering (removing instances with no gold entities), the evaluation set contains $n{=}32{,}565$ instances across 8 coarse entity types; 11.9\\% receive zero F1 under greedy decoding.\nInstance degeneracy is 13.0\\% (vs.\\ 12.2\\% on SciERC, 61.7\\% on CoNLL).\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:fewnerd_full}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\nSignal & $\\rho$ & Sample AUROC & Sel.\\ $\\Delta$ & 95\\% CI \\\\\n\\midrule\nLP & .220 & .578 & $\\mathbf{+1.39}$\\,pp & [+1.18, +1.53] \\\\\nVC & .386 & --- & $-$1.79\\,pp & --- \\\\\nFK & .313 & --- & $-$2.26\\,pp & --- \\\\\nSJ & .300 & --- & $-$2.14\\,pp & --- \\\\\nEM & .287 & --- & $-$3.85\\,pp & --- \\\\\n\\midrule\n\\multicolumn{3}{l}{Greedy: 0.748 \\quad Oracle: 0.872} & \\multicolumn{2}{l}{Headroom: 12.4\\,pp} \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Key observations.}\n(1)~All five signals achieve positive QE ($\\rho$ 0.22--0.39); quality estimation works on Few-NERD. VC leads ($\\rho{=}0.39$), followed by FK ($0.31$), SJ ($0.30$), EM ($0.29$), LP ($0.22$); the ranking matches SciERC where structural signals also outperform LP for quality estimation.\n(2)~LP is the only signal achieving significant positive selection ($+1.39$~pp, $p{<}0.001$, CI excludes zero). The sample-level AUROC of 0.578 confirms LP provides per-sample discriminability beyond instance-level quality prediction.\n(3)~Despite positive $\\rho$, all structural signals degrade selection ($-1.79$ to $-3.85$~pp), further confirming that the correlation-selection gap is not an artifact of weak QE.\n(4)~Low degeneracy (13.0\\%) combined with strong LP-quality alignment ($\\rho{\\approx}0.5$--$0.7$) enables LP selection: candidates differ in F1 more often, and LP can rank them effectively. This contrasts with SciERC (12.2\\% degeneracy but weak alignment $\\rho{\\approx}0.16$, LP $+0.61$~pp) and CoNLL (61.7\\%, LP $-0.85$~pp).\n\n\\section{Per-Entity-Type LP Selection Analysis}\\label{app:per_type_lp}\n\nTable~\\ref{tab:per_type_lp} stratifies LP selection by entity type on Few-NERD, sorted by degeneracy rate.\nThe degeneracy-gating mechanism holds at entity-type granularity: 7 of 8 types show positive LP selection gains, and the sole negative type (Art, $-0.17$~pp) has the highest degeneracy (19.8\\%).\nThe correlation between per-type degeneracy and oracle headroom is strong and significant (Spearman $\\rho{=}{-}0.881$, $p{=}0.004$; exact permutation $p{=}0.005$); degeneracy directly constrains the headroom available for selection.\nUnder a conservative $\\text{df}{=}4$ adjustment for within-type dependence, the correlation remains significant ($p{=}0.033$).\nEntity types show near-zero intra-class correlation (ICC $= -0.004$), supporting the independence assumption underlying per-type analysis.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\n\\label{tab:per_type_lp}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lrrrrrrr}\n\\toprule\nEntity Type & $n$ & Degen.\\% & Greedy & LP Sel & $\\Delta$ (pp) & LP $\\rho$ & Headroom \\\\\n\\midrule\nEvent & 1{,}306 & 6.0 & .655 & .662 & $+$0.65 & .457 & 16.1\\,pp \\\\\nOther & 3{,}433 & 6.6 & .637 & .685 & $\\mathbf{+4.73}$ & .491 & 19.4\\,pp \\\\\nOrganization & 6{,}647 & 6.7 & .720 & .732 & $+$1.21 & .509 & 13.3\\,pp \\\\\nBuilding & 1{,}587 & 7.2 & .702 & .705 & $+$0.23 & .478 & 14.9\\,pp \\\\\nProduct & 2{,}276 & 8.2 & .656 & .677 & $+$2.01 & .483 & 15.8\\,pp \\\\\nLocation & 8{,}023 & 11.4 & .793 & .798 & $+$0.53 & .520 & 10.3\\,pp \\\\\nPerson & 8{,}016 & 13.4 & .822 & .835 & $+$1.25 & .544 & 9.2\\,pp \\\\\nArt & 1{,}277 & 19.8 & .756 & .754 & $-$0.17 & .451 & 9.2\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\n\\label{tab:per_type_lp_conll}\n\\begin{tabular}{lrrr}\n\\toprule\nEntity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n\\midrule\nMISC & 23.2 & $-$2.19 \\\\\nPER & 42.6 & $-$1.08 \\\\\nLOC & 47.5 & $-$0.62 \\\\\nORG & 54.3 & $-$0.55 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\n\\label{tab:per_type_lp_scierc}\n\\begin{tabular}{lrrr}\n\\toprule\nEntity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\n\\midrule\nTask & 10.1 & $+$2.58 \\\\\nGeneric & 10.0 & $+$2.07 \\\\\nMaterial & 20.0 & $+$0.91 \\\\\nMetric & 12.5 & $-$0.06 \\\\\nMethod & 16.3 & $-$0.03 \\\\\nOtherScientificTerm & 6.2 & $-$0.57 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nThe cross-dataset degeneracy gradient (61.7\\% $\\to$ 13.0\\% $\\to$ 12.2\\%) is inversely associated with LP selection effectiveness at the macro level ($n{=}3$ datasets; exploratory).\\footnote{Partial Spearman correlation controlling for entity-type frequency yields $\\rho{=}{-}0.47$ (vs.\\ raw $\\rho{=}{-}0.38$); type frequency does not confound the degeneracy--LP relationship.}\nAt finer per-type granularity, selection depends on the interaction of degeneracy, oracle headroom, and type-specific LP-quality alignment.\nA Kruskal-Wallis test finds no significant per-type heterogeneity in LP selection gains on SciERC ($p{=}0.796$), consistent with the small per-type sample sizes ($n{=}54$--$296$).\nLow degeneracy alone does not ensure selection gains: CoNLL MISC (23\\%, headroom 12.6~pp) and SciERC OtherScientificTerm (6.2\\%, headroom 12.5~pp) both show negative LP selection despite available headroom; LP correlation strength with the type-specific quality function is an additional prerequisite.\n\n\\section{Calibration Baseline}\\label{app:calibration_baseline}\n\nStandard calibration methods are monotonic transforms of log-probability and therefore preserve within-instance sample rankings: Platt scaling \\cite{platt1999probabilistic} fits a logistic regression $\\sigma(a \\cdot \\text{LP} + b)$, and temperature scaling \\cite{guo2017calibration} divides logits by a scalar $\\tau$.\nSince both preserve the argmax, selection F1 is identical to raw LP on all three datasets (Table~\\ref{tab:calibration}).\n\nTo break monotonicity, we fit a multi-feature Platt model (MF-Platt) using LP, token count, and entity count as inputs, trained on a held-out calibration split (20\\% of the test set, 5-fold cross-validation on the remainder).\nMF-Platt can reorder candidates within an instance, yet yields no significant selection improvement: $\\Delta{=}{-}1.1$~pp on SciERC ($p{=}0.72$), $+0.3$~pp on CoNLL ($p{=}0.31$), and $-0.6$~pp on Few-NERD ($p{=}0.83$).\nPlatt scaling substantially improves probability calibration (ECE drops from 0.26--0.39 to 0.01--0.08), but better-calibrated probabilities do not translate to better selection.\nThis parallels the supervised signal combination result (\\S\\ref{sec:robustness_main}): neither stronger aggregation nor additional features can compensate for weak per-sample discriminative signal.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Calibration baseline results ($T{=}1.0$; single seed). SciERC uses $N{=}8$; CoNLL and Few-NERD use $N{=}16$ ($N$ does not affect greedy F1 or calibration conclusions). Platt and TempScale are monotonic transforms of LP that preserve the within-instance argmax (selection F1 $\\equiv$ Raw LP, omitted). MF-Platt uses LP $+$ token count $+$ entity count; $p$: bootstrap test vs.\\ Raw LP. Few-NERD evaluated on the first 5K test instances without gold-filtering (greedy .771; cf.\\ gold-filtered full-set .748 in Table~\\ref{tab:fewnerd}).}\n\\label{tab:calibration}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{l cccc cc}\n\\toprule\n& & \\multicolumn{2}{c}{Selection F1} & & \\multicolumn{2}{c}{ECE} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){6-7}\nDataset & Greedy & Raw LP & MF-Platt ($p$) & & Raw & Platt \\\\\n\\midrule\nSciERC & .644 & .650 & .639 (.72) & & .260 & .048 \\\\\nCoNLL & .909 & .898 & .901 (.31) & & .392 & .012 \\\\\nFew-NERD & .771 & .785 & .778 (.83) & & .262 & .080 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\section{Epoch Confound Analysis}\\label{app:epoch_confound}\n\n\\paragraph{Training convergence modulates degeneracy.}\nTable~\\ref{tab:epoch_confound} compares the 3-epoch model (used throughout the main text) with a 5-epoch variant on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; gold-filtered $n{=}32{,}565$, 2-seed mean).\nExtended training increases greedy F1 by $+0.7$~pp ($0.791 \\to 0.798$) and triples instance degeneracy ($8.8$\\% $\\to$ $26.4$\\%), reducing the fraction of instances with non-degenerate outputs.\nThe 5-epoch MV $\\Delta$ ($-0.40$\\,pp) appears smaller than 3-epoch ($-2.74$\\,pp), but this is misleading: $26$\\% of instances are fully degenerate (MV${\\equiv}$greedy, $\\Delta{=}0$), diluting the aggregate.\nOn non-degenerate instances, MV $\\Delta{\\approx}{-}0.55$\\,pp, still negative---degeneracy masks the MV penalty rather than improving it.\n\nLP selection shows even more dramatic degradation: 5-epoch LP $\\Delta{=}{+}0.12{\\pm}0.04$\\,pp (2-seed mean), a 91\\% reduction from the 3-epoch $+1.39$\\,pp (both evaluated on the full test set under identical conditions; Table~\\ref{tab:epoch_confound}). This confirms that training convergence not only increases degeneracy but also erodes LP's discriminative power within non-degenerate instances, consistent with the alignment degradation observed in SciERC (Table~\\ref{tab:epoch_scierc}).\n\nEvaluation loss increases after epoch 3, and the best checkpoint by validation loss occurs at approximately epoch 3.9.\nStandard early stopping practice thus naturally selects the low-degeneracy regime.\nThis finding refines the narrative: degeneracy is not a fixed property of datasets but is modulated by the degree of training convergence. Over-trained models compress their output distributions, collapsing diversity even on datasets that support it under well-regularized training.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\n\\label{tab:epoch_confound}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcc}\n\\toprule\nMetric & 3-epoch & 5-epoch \\\\\n\\midrule\nGreedy F1 & 0.791 & 0.798 \\\\\nMV $\\Delta$ (pp) & $-$2.74 & $-$0.40 \\\\\nInstance degen.\\ (\\%) & 8.8 & 26.4 \\\\\nSJ mean & 0.685 & 0.802 \\\\\nLP $\\Delta$ (pp) & $+$1.39 & $+$0.12${\\pm}$0.04 \\\\\nEntity constr.\\ $\\Delta$ (pp) & $+$0.88 & $+$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{SciERC epoch curve.}\nTable~\\ref{tab:epoch_scierc} extends the analysis to SciERC with a 3-point curve (3, 5, 10 epochs; Qwen3-8B, $N{=}8$, $T{=}1.0$).\nDegeneracy increases monotonically (6.4\\% $\\to$ 17.8\\% $\\to$ 47.8\\%), and within-instance LP-quality correlation degrades in tandem (median $\\rho$: 0.319 $\\to$ 0.262 $\\to$ 0.112; mean $\\rho$: 0.273 $\\to$ 0.179 $\\to$ 0.066), confirming that overtraining erodes both diversity and LP alignment simultaneously.\nThe fraction of instances with positive LP-quality correlation also declines (76.4\\% at 3 epochs $\\to$ 64.1\\% at 5 epochs $\\to$ 54.0\\% at 10 epochs).\nLP selection does not yield significant gains at any training duration ($-1.24$, $+0.64$, $+1.02$~pp; all below the ${\\approx}$1.5~pp MDE), despite oracle headroom ranging from 8.4 to 15.0~pp.\nThe 3-epoch model has higher within-instance alignment ($\\rho{=}0.319$) than the 5-epoch model ($\\rho{=}0.262$), yet LP selection is worse ($-1.24$ vs.\\ $+0.64$~pp): at 6.4\\% degeneracy, more non-degenerate instances enter the candidate pool, but LP ranking precision is too low to exploit them, so the broader pool hurts rather than helps. This illustrates that low degeneracy does not ensure selection gains; LP-quality alignment predicts selection direction.\nAt 10 epochs, the model retains competitive greedy F1 (0.649 vs.\\ 0.650 at 3 epochs) yet conditions are unfavorable: 47.8\\% degenerate instances and $\\rho{=}0.112$.\nThe gradient confirms that degeneracy is convergence-driven rather than a fixed dataset property: extended training compresses output distributions, degrading both diversity and within-instance alignment. However, the epoch-to-epoch alignment variation ($\\Delta\\rho_{\\text{median}}{=}0.057$) is small relative to the cross-dataset gap (SciERC ${\\sim}$0.3 vs.\\ Few-NERD ${\\sim}$0.5), consistent with alignment being primarily dataset-intrinsic: training convergence modulates alignment at the margin but cannot shift a dataset into the strong-alignment regime.\nEven at the most favorable epoch (3-epoch, $\\rho{=}0.319$), SciERC alignment remains below the ${\\sim}$0.5 threshold associated with successful LP selection on Few-NERD.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{SciERC NER epoch curve (Qwen3-8B, $N{=}8$, $T{=}1.0$). Training duration modulates both instance degeneracy and within-instance LP-quality alignment. ``Degen.'': constant-F1 instance degeneracy (gold-filtered). ``LP $\\Delta$'': LP selection gain over greedy (gold-filtered; none reaches the ${\\approx}$1.5~pp MDE). ``$\\rho$ med'': median within-instance LP-quality correlation. Greedy F1 uses span-based evaluation consistent with Tables 1--3; $\\rho$ and LP $\\Delta$ use text-based matching consistent with Table~\\ref{tab:within_rho}.}\n\\label{tab:epoch_scierc}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nMetric & 3-epoch & 5-epoch & 10-epoch \\\\\n\\midrule\nGreedy F1 & 0.650 & 0.644 & 0.649 \\\\\nInstance degen.\\ (\\%) & 6.4 & 17.8 & 47.8 \\\\\nLP $\\Delta$ (pp) & $-$1.24 & $+$0.64 & $+$1.02 \\\\\nWithin-inst.\\ $\\rho$ (median) & 0.319 & 0.262 & 0.112 \\\\\nWithin-inst.\\ $\\rho$ (mean) & 0.273 & 0.179 & 0.066 \\\\\n\\% positive $\\rho$ & 76.4 & 64.1 & 54.0 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\paragraph{Scope of epoch analysis.}\nThe Few-NERD epoch analysis covers 2 points (3 vs.\\ 5 epochs); the SciERC curve provides a 3-point gradient showing monotonic degeneracy increase with simultaneous within-instance alignment degradation.\nCoNLL epoch variation remains unverified; high-degeneracy datasets (CoNLL at 59--89\\%) may exhibit a ceiling effect where additional training has limited marginal impact.\nAll Few-NERD results in the main text use the 3-epoch model (standard early stopping); the 5-epoch comparison is a controlled ablation.\nAll SciERC results use the 5-epoch model; the 3- and 10-epoch variants serve as controlled ablations.\n\n\\subsection{Degeneracy-Aware LP Selection}\\label{app:dals}\n\nThe non-tied subset analysis (Table~\\ref{tab:nontied_main}) identifies within-instance LP range (max minus min LP across $N$ samples) as a per-instance degeneracy proxy: instances with near-zero LP range carry no discriminative signal.\nDegeneracy-aware LP selection (DALS) operationalizes this: when LP range exceeds $\\tau{=}0.05$ (the threshold independently motivated by the non-tied analysis; Appendix~\\ref{app:epsilon_robustness}), select the highest-LP sample; otherwise fall back to greedy.\nOn SciERC, DALS yields $+0.71{\\pm}0.48$~pp (3-seed mean; individual seeds: $+0.19$ to $+1.14$~pp); on Few-NERD, $+0.30$~pp ($p{<}0.001$; gain remains positive across $\\tau \\in [0.01, 0.15]$); on CoNLL, where pure LP selection degrades F1 ($-0.85$~pp), DALS shows comparable degradation (Qwen: $-0.87$~pp; LLaMA: neutral).\nDALS improves over pure LP selection when degeneracy is moderate, provides partial damage control when LP selection is harmful, and defaults to greedy when LP range signals no information.\nWhile gains are modest and seed-sensitive, LP range serves as an operationally accessible degeneracy proxy, though the mixed cross-dataset results confirm that degeneracy gating alone cannot ensure positive selection outcomes.\n\n\\paragraph{LOO $\\tau$ sensitivity.}\nLeave-one-out (LOO) cross-validation across datasets shows that the optimal $\\tau$ spans two orders of magnitude: $\\tau^*{=}0.001$ on Few-NERD, $0.05$ on SciERC, and $0.10$ on CoNLL.\nLOO regret (the gap between oracle and LOO-selected $\\tau$) ranges from 0.51 to 1.21~pp.\nThe best single cross-dataset $\\tau$ ($\\tau{=}0.05$) matches the independently motivated non-tied threshold, but yields dataset-specific suboptimality: even with oracle $\\tau$, CoNLL remains at $-0.31$~pp.\nThis sensitivity reinforces the diagnostic framing of DALS: per-dataset $\\tau$ tuning is required for positive gains, and even optimally tuned DALS cannot overcome weak LP-quality alignment on high-degeneracy datasets.\n\n\\subsection{Conditional Decomposition of LP Selection}\\label{app:conditional_decomp}\n\nTo test whether LP-quality alignment is associated with selection gains within datasets, we restrict LP selection to the favorable subset: non-degenerate instances whose within-instance LP range exceeds the dataset-specific median (SciERC: 0.040 nats, CoNLL: 0.062, Few-NERD: 0.067).\nTable~\\ref{tab:conditional_decomp} reports results across three datasets.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\n\\label{tab:conditional_decomp}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lccc}\n\\toprule\nDataset & LP $\\Delta$ (pp) & 95\\% CI & Interpretation \\\\\n\\midrule\nSciERC & $+$2.47 & [$+$0.30, $+$4.70] & significant positive \\\\\nFew-NERD & $+$0.63 & [$-$0.02, $+$1.30] & marginal positive \\\\\nCoNLL & $-$1.78 & [$-$2.83, $-$0.76] & significant negative \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nOn SciERC, restricting to the favorable subset recovers a significant LP gain, consistent with LP-quality alignment predicting selection within the non-degenerate pool.\nOn Few-NERD, the trend is directionally consistent but the confidence interval crosses zero; the full-dataset result ($+1.39$~pp, $p{<}0.001$) reflects the larger sample size rather than a stronger per-instance effect.\nCoNLL remains negative even on the favorable subset, consistent with the ceiling-regime interpretation: at $>$90\\% greedy F1, residual errors are idiosyncratic and LP cannot rank corrections.\n\n\\subsection{Power Analysis for Cross-Dataset Degeneracy--LP Correlation}\\label{app:power_analysis}\n\nTable~\\ref{tab:power_analysis} reports post-hoc power for the $n{=}23$ cross-dataset correlation between degeneracy and LP selection gain ($\\rho{=}0.052$, $p{=}0.81$; Figure~\\ref{fig:degeneracy_scatter}).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\\alpha{=}0.05$). At this sample size, only large correlations ($\\rho{\\geq}0.5$) are detectable with adequate power.}\n\\label{tab:power_analysis}\n\\begin{tabular}{lc}\n\\toprule\nTrue $\\rho$ & Power at $n{=}23$ \\\\\n\\midrule\n0.1 & 0.07 \\\\\n0.2 & 0.13 \\\\\n0.3 & 0.25 \\\\\n0.4 & 0.44 \\\\\n0.5 & 0.65 \\\\\n0.6 & 0.84 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\noindent 80\\% power requires $n{\\approx}85$ for $\\rho{=}0.3$ and $n{\\approx}47$ for $\\rho{=}0.5$. The null result should be interpreted as absence of evidence for a large effect rather than evidence of absence.\n\n\\subsection{Entity-Token LP Decomposition}\\label{app:entity_token_lp}\n\nFull-sequence LP averages over all output tokens, diluting entity-relevant signal with formatting and schema tokens.\nEntity-token LP restricts the average to tokens within entity text and type spans, yielding $4{\\times}$ higher within-instance variance (median 0.000644 vs.\\ 0.000161).\nTable~\\ref{tab:entity_token_lp} compares the two aggregation strategies on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$).\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\n\\label{tab:entity_token_lp}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\nAggregation & Med.\\ var. & $\\rho$ & AUROC & $\\Delta$ (pp) \\\\\n\\midrule\nFull-sequence & 0.000161 & 0.297 & 0.642 & $+$0.35 \\\\\nEntity text+type & 0.000644 & 0.440 & 0.719 & $-$0.73 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nDespite stronger correlation ($+$48\\%) and higher AUROC, entity-token LP produces worse selection, reinforcing that compression operates at the representation level rather than token aggregation: the correlation-selection gap persists even with a more targeted signal.\n\n\\subsection{Entity-Level Majority Voting}\\label{app:entity_merge}\n\nEntity-level majority voting constructs a merged output by including all (text, type) entity tuples that appear in at least $k$ of $N$ samples (with $k = N/2$ as the default majority threshold).\nUnlike best-of-$N$ selection (which picks one complete sample), merge combines evidence across samples at entity granularity.\nWe sweep $k \\in \\{2, 3, \\ldots, 8\\}$ on each dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$) and report the best threshold per dataset.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\n\\label{tab:entity_merge}\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{lcccc}\n\\toprule\nDataset & Greedy & Best merge ($k^*$) & $\\Delta$ (pp) & Recovery (\\%) \\\\\n\\midrule\nSciERC & 0.644 & 0.660 ($k{=}3$) & $+$1.57 & $+$11.9 \\\\\nCoNLL & 0.907 & 0.903 ($k{=}3$) & $-$0.38 & $-$9.0 \\\\\nFew-NERD & 0.748 & 0.744 ($k{=}2$) & $-$0.43 & $-$3.6 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\nOn degenerate subsets (instances where all $N$ samples yield identical F1), merge is uniformly negative across all three datasets, confirming that entity-level aggregation cannot bypass the diversity bottleneck identified in the main text (\\S\\ref{sec:discussion}).\n\n\\subsection{Entity Construction Results}\\label{app:entity_construction_table}\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. $^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}\n\\label{tab:entity_construction}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llcccc@{}}\n\\toprule\nDataset & Wt. & Greedy & Constr. & $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC & LP & $.667{\\pm}.001$ & $.670{\\pm}.003$ & $+0.32$\\,pp & n.s. \\\\\n       & Unif. & $.667{\\pm}.001$ & $.660{\\pm}.004$ & $-0.74$\\,pp & n.s. \\\\\n\\addlinespace\nFew-NERD & LP & $.748$ & $\\mathbf{.762{\\pm}.005}$ & $+1.40{\\pm}0.51$\\,pp & ${<}.001^\\dagger$ \\\\\n         & Unif. & $.748$ & $\\mathbf{.756{\\pm}.006}$ & $+0.74{\\pm}0.58$\\,pp & .003 \\\\\n\\addlinespace\nCoNLL$^\\ddagger$ & Unif. & .908 & .904 & $-0.39$\\,pp & n.s. \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\subsection{Entity Construction Threshold Sensitivity}\n\\label{app:theta_sweep}\n\nTable~\\ref{tab:theta_sweep} reports entity construction F1 as a function of the confirmation threshold $\\theta$ across three datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$). The default $\\theta{=}2/N{=}0.25$ achieves the best LP-weighted $\\Delta$F1 on Few-NERD and is within 0.04\\,pp of the optimum on SciERC. Performance is stable across $\\theta \\in [0.15, 0.35]$; below 0.15, spurious entities degrade precision, and above 0.40, aggressive filtering removes correct low-frequency entities.\n\n\\begin{table}[h]\n\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\n\\label{tab:theta_sweep}\n\\centering\n\\small\n\\resizebox{\\columnwidth}{!}{\n\\begin{tabular}{ll rr rr}\n\\toprule\nDataset & $\\theta$ & LP-w F1 & Unif.\\ F1 & $\\Delta$ LP-w & $\\Delta$ Unif.\\ \\\\\n\\midrule\n\\multirow{8}{*}{SciERC}\n & 0.10 & .620 & .620 & $-$2.37 & $-$2.37 \\\\\n & 0.15 & .659 & .659 & $+$1.54 & $+$1.54 \\\\\n & 0.20 & .659 & .659 & $+$1.54 & $+$1.54 \\\\\n & 0.25 & .661 & .659 & $+$1.67 & $+$1.54 \\\\\n & 0.30 & .661 & .661 & \\textbf{$+$1.71} & \\textbf{$+$1.71} \\\\\n & 0.35 & .661 & .661 & \\textbf{$+$1.71} & \\textbf{$+$1.71} \\\\\n & 0.40 & .653 & .654 & $+$0.94 & $+$0.97 \\\\\n & 0.50 & .649 & .654 & $+$0.46 & $+$0.97 \\\\\n\\midrule\n\\multirow{8}{*}{Few-NERD}\n & 0.10 & .677 & .676 & $-$7.12 & $-$7.15 \\\\\n & 0.15 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\n & 0.20 & .751 & .751 & $+$0.32 & $+$0.32 \\\\\n & 0.25 & .757 & .751 & \\textbf{$+$0.88} & $+$0.32 \\\\\n & 0.30 & .750 & .750 & $+$0.21 & $+$0.21 \\\\\n & 0.35 & .750 & .750 & $+$0.21 & $+$0.21 \\\\\n & 0.40 & .729 & .728 & $-$1.90 & $-$2.01 \\\\\n & 0.50 & .725 & .728 & $-$2.25 & $-$2.01 \\\\\n\\midrule\n\\multirow{8}{*}{CoNLL}\n & 0.10 & .844 & .842 & $-$6.44 & $-$6.56 \\\\\n & 0.15 & .896 & .896 & $-$1.19 & $-$1.19 \\\\\n & 0.20 & .896 & .896 & $-$1.19 & $-$1.19 \\\\\n & 0.25 & .901 & .896 & $-$0.71 & $-$1.19 \\\\\n & 0.30 & .904 & .904 & \\textbf{$-$0.39} & \\textbf{$-$0.39} \\\\\n & 0.35 & .904 & .904 & $-$0.41 & \\textbf{$-$0.39} \\\\\n & 0.40 & .900 & .899 & $-$0.83 & $-$0.94 \\\\\n & 0.50 & .897 & .899 & $-$1.12 & $-$0.94 \\\\\n\\bottomrule\n\\end{tabular}\n}\n\\end{table}\n\n\\subsection{Few-Shot Error Correlation Analysis}\\label{app:fs_error}\n\nWe investigated whether few-shot demonstrations induce correlated entity-level errors that explain construction failure.\nPairwise error overlap (Jaccard similarity of per-sample false-positive and false-negative entity sets) shows no significant difference between FS and ZS regimes (SciERC: $0.454$ vs.\\ $0.452$, $p{=}0.84$; CoNLL: $0.103$ vs.\\ $0.104$, $p{=}0.64$; permutation tests, 10{,}000 resamples).\nWe additionally measure entity-level prediction entropy across $N{=}8$ samples per instance.\nOn SciERC, FS and ZS entropies are indistinguishable ($0.483$ vs.\\ $0.485$, $p{=}0.81$).\nOn CoNLL, however, entity prediction entropy is significantly \\emph{higher} under FS ($0.209$ vs.\\ $0.184$, $p{<}10^{-9}$, $r{=}0.106$, small effect; Wilcoxon signed-rank test), contrary to the hypothesis that demonstrations concentrate predictions---they instead \\emph{increase} output diversity on this dataset.\nThe mechanism by which few-shot demonstrations undermine construction remains an open question; entity-level error overlap is preserved while prediction entropy may even rise, suggesting that the \\emph{nature} rather than the \\emph{diversity} of errors shifts in ways that defeat LP-weighted voting.\n\n\\subsection{Construction Weighting Variants}\\label{app:weighting_variants}\n\nTable~\\ref{tab:weighting_variants} compares LP-weighted, VC-weighted, and SJ-weighted entity construction on LLaMA-3.1-8B (3-seed mean, $N{=}8$, $T{=}1.0$, $\\theta{=}2/N$).\nAll three weighting schemes beat greedy on SciERC, where degeneracy is low; LP and VC also improve Few-NERD, though gains are smaller than the Qwen results in Table~\\ref{tab:entity_construction}.\nThe optimal weighting scheme is model-dependent (VC leads on LLaMA SciERC; LP leads on Qwen), but the core finding is robust: entity-level voting improves F1 in low-degeneracy regimes regardless of the specific weighting function.\nSJ-weighted construction degrades on Few-NERD ($-0.20$\\,pp), consistent with SJ over-weighting high-consensus samples, which correlates with the degeneracy direction rather than opposing it.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\\theta{=}2/N$, 3-seed mean). $\\Delta$: F1 difference vs.\\ greedy in pp. Main-text construction results (Table~\\ref{tab:entity_construction}) use Qwen3-8B.}\n\\label{tab:weighting_variants}\n\\begin{tabular}{lccc}\n\\toprule\nDataset & LP-wt $\\Delta$ & VC-wt $\\Delta$ & SJ-wt $\\Delta$ \\\\\n\\midrule\nSciERC & $+$0.91 & $+$1.05 & $+$0.72 \\\\\nFew-NERD & $+$0.02 & $+$0.15 & $-$0.20 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\subsection{Zero-Shot vs.\\ Few-Shot Comparison}\\label{app:zs_vs_fs}\n\nTable~\\ref{tab:72b_zs_vs_fs} presents the full zero-shot (ZS) vs.\\ few-shot (FS) comparison on Qwen2.5-72B-Instruct-AWQ.\nLP-weighted construction yields a significant gain only on SciERC under ZS ($+$1.53\\,pp, $p{=}.008$); all five FS configurations show non-significant deltas ($|{\\Delta}| \\leq 0.08$\\,pp).\nFew-shot demonstrations raise the greedy baseline (e.g., SciERC: .399$\\to$.461) but do not translate into construction improvements, suggesting that the dual-gating mechanism---where both signal quality and diversity are necessary---holds within the FT+ZS regime while FS introduces an independent failure mode whose origin remains open (\\S\\ref{app:fs_error}).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\n\\label{tab:72b_zs_vs_fs}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{ll rrrrr rr r}\n\\toprule\nDataset & Regime & Degen\\% & LP $\\rho$ & SJ $\\rho$ & FK $\\rho$ & VC $\\rho$ & Greedy F1 & Constr $\\Delta$ & $p$ \\\\\n\\midrule\nSciERC  & ZS & 21.0 & .081  & .217 & .227 & .277 & .399 & \\textbf{+1.53} & .008 \\\\\nSciERC  & FS & 16.6 & .060  & .293 & .301 & .258 & .461 & $-$0.08 & .544 \\\\\n\\midrule\nCoNLL   & ZS & 67.7 & $-$.002 & .304 & .302 & .297 & .712 & $-$0.37 & --- \\\\\nCoNLL   & FS & 70.0 & .106  & .442 & .451 & .426 & .745 & +0.03 & .417 \\\\\n\\midrule\nFew-NERD & ZS & 46.2 & .119  & .345 & .321 & .416 & .628 & $-$0.20 & --- \\\\\nFew-NERD & FS & 45.2 & .161  & .345 & .327 & .410 & .619 & +0.02 & .401 \\\\\n\\bottomrule\n\\end{tabular}%\n}\n\\end{table*}\n\n\\section{Evaluation Protocol for Structured Self-Consistency}\\label{app:eval_protocol}\n\nWe distill our experimental methodology into a reusable three-step protocol for assessing test-time compute scaling on set-valued structured prediction tasks.\n\n\\paragraph{Step 1: Measure instance degeneracy.}\nGiven $N$ stochastic samples per instance, compute the fraction of instances where all samples produce identical task-metric scores (\\S\\ref{sec:evaluation}).\nDegeneracy ${>}30$\\% indicates limited headroom for any selection or aggregation strategy.\nReport degeneracy alongside all test-time scaling results to contextualize gains.\n\n\\paragraph{Step 2: Assess signal--quality alignment.}\nFor each candidate signal, compute (a)~cross-instance Spearman $\\rho$ with the task metric (quality estimation strength) and (b)~within-instance $\\rho$ between signal and task metric, restricted to non-degenerate instances (selection discriminability).\nA large gap between (a) and (b) indicates the correlation-selection gap: reliable QE but poor selection prospects.\n\n\\paragraph{Step 3: Evaluate aggregation strategies.}\nCompare three regimes against greedy ($T{=}0$) and oracle baselines:\n\\begin{itemize}\n    \\item \\textit{Instance-level selection}: best-of-$N$ via per-sample signals (e.g., LP) and consensus-proximity (MBR utility).\n    \\item \\textit{Entity-level construction}: majority-voted entity aggregation with threshold $\\theta$ (e.g., $\\theta{=}2/N$), optionally weighted by signal confidence.\n    \\item \\textit{Selective prediction}: abstain on low-confidence instances; report coverage--F1 tradeoff.\n\\end{itemize}\n\n\\paragraph{Reporting standards.}\nReport: (1)~degeneracy percentage, (2)~oracle headroom (oracle $-$ greedy), (3)~signal $\\rho$ (cross-instance and within-instance), (4)~selection $\\Delta$F1 with bootstrap $p$-values and effect sizes (Cohen's $d$), (5)~construction $\\Delta$F1, (6)~selective prediction AUPRC and coverage--F1 curve.\nUse paired bootstrap tests ($B{\\geq}10{,}000$); report minimum detectable effect at 80\\% power given the test set size.\n\n\\section{Cost-Benefit Analysis}\\label{app:cost_benefit}\n\nTable~\\ref{tab:cost_benefit} summarizes the inference cost and F1 gain of each aggregation strategy relative to greedy decoding.\nEntity construction achieves the only consistently positive result at zero marginal cost (reusing the $N$ samples already drawn for quality estimation); cross-model ensemble requires $2N{\\times}$ inference for a smaller gain.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\\Delta$F1 reports the primary result (dataset in parentheses).}\n\\label{tab:cost_benefit}\n\\begin{tabular}{@{}lcll@{}}\n\\toprule\nMethod & Cost & $\\Delta$F1 & Verdict \\\\\n\\midrule\nGreedy ($T{=}0$) & $1{\\times}$ & baseline & default \\\\\nSC + MV & $N{\\times}$ & ${\\approx}0$\\,pp & no gain \\\\\nSC + LP selection & $N{\\times}$ & $+1.39$\\,pp (FN) & dataset-dep. \\\\\nSC + construction & $N{\\times}$ & $+0.32$\\textendash$1.40$\\,pp & \\textbf{positive} \\\\\nCross-model SC & $2N{\\times}$ & $+0.42$\\,pp (FN) & positive, $2{\\times}$ cost \\\\\nSC + DALS & $N{\\times}$ & $+0.71$\\,pp (SciERC) & seed-sensitive \\\\\nSC + verifier & $N{\\times}{+}\\text{train}$ & $+0.30$\\,pp & no transfer \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nSC + LP selection is positive only on Few-NERD ($p{<}0.001$) and neutral to negative elsewhere (SciERC $+0.2$\\,pp, $p{=}0.29$; CoNLL $-0.85$\\,pp).\nEntity construction is the only strategy that is positive on multiple datasets without additional model access, achieving zero marginal cost by reusing the $N$ samples already generated.\nCross-model ensemble breaks within-model degeneracy but doubles inference cost.\n\n\\section{Prior Work Differentiation Matrix}\\label{app:differentiation}\n\nTable~\\ref{tab:differentiation} positions this work relative to four closely related studies.\nAll four investigate settings where self-consistency underperforms; we are the first to provide a multi-stage diagnostic with mechanistic probes, theory, and exhaustive method evaluation on structured generation.\n\n\\begin{table*}[h]\n\\centering\n\\small\n\\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}\n\\label{tab:differentiation}\n\\resizebox{\\textwidth}{!}{%\n\\begin{tabular}{@{}l p{2.8cm} p{2.5cm} p{2.5cm} p{2.8cm} p{3.2cm}@{}}\n\\toprule\nAspect & \\citet{yun2025price} & \\citet{chen2023twofailures} & \\citet{aggarwal2023adaptive} & \\citet{farquhar2024detecting} & \\textbf{Ours} \\\\\n\\midrule\nRoot cause & Constrained decoding suppresses diversity & Reasoning failures (hypothetical, compositional) & Sample efficiency in allocation & Hallucination via semantic inconsistency & Capability ceiling (degeneracy $+$ LP compression $+$ verification failure) \\\\\n\\addlinespace\nTasks & Math, QA, structured gen. & Reasoning, QA & Math, code & QA, open-ended & NER ($+$SQL, RE) \\\\\n\\addlinespace\nMethods tested & 1 (diversity analysis) & 1 (failure taxonomy) & 1 (adaptive $N$) & 1 (semantic entropy) & 9 categories (Table~\\ref{tab:method_summary}) \\\\\n\\addlinespace\nTheoretical contrib. & None & None & Allocation bounds & Entropy-based & MBR equivalence, degeneracy bound, scaling laws \\\\\n\\addlinespace\nMechanistic probe & No & No & No & No & Yes (ESJ, MRSC, LSC, hidden-state) \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table*}\n\n\\section{Extended Discussion}\\label{app:objections}\n\n\\paragraph{Open questions.}\nThree directions remain: (1)~whether learned verifiers (e.g., reward models) can break the introspection boundary and exploit hidden-state quality signals that prompt-based methods cannot access; (2)~whether diversity-promoting decoding strategies can preserve candidate variety without sacrificing output quality, mitigating the capability-diversity tension; (3)~whether the diagnostic framework transfers to other structured prediction tasks (e.g., coreference resolution, syntactic parsing) where output spaces similarly resist equivalence-class aggregation.\n\nWe address twelve anticipated objections, each referencing specific evidence in the paper.\n\n\\paragraph{O1: Results are NER-specific and may not generalize.}\nWe validate the diagnostic framework on Spider SQL parsing (GPT-5.5, $n{=}196$; \\S\\ref{sec:introduction}): degeneracy reaches 87.2\\%, confirming the failure mode beyond NER. An RE extension on SciERC (Appendix~\\ref{app:re_extension}) shows compound error propagation worsens all signals. The structural mismatch (set-valued outputs without equivalence classes) applies to any structured generation task.\n\n\\paragraph{O2: Cross-model gain of $+$0.42\\,pp is marginal.}\n$+0.42$\\,pp is the only unconditionally positive result among 9 method categories tested (Table~\\ref{tab:method_summary}). Its significance ($p{<}0.001$, CI $[0.27, 0.58]$; \\S\\ref{sec:cross_model}) and theoretical motivation (architecturally distinct models produce independent error distributions, breaking within-model degeneracy) distinguish it from the null results of other categories.\n\n\\paragraph{O3: Hyperparameters may not be optimal.}\nWe report full sweeps: construction threshold $\\theta \\in [0.05, 0.50]$ (Appendix~\\ref{app:theta_sweep}), DALS threshold $\\tau$ with LOO cross-validation (regret 0.51--1.21\\,pp; Appendix~\\ref{app:dals}), LP compression threshold $\\varepsilon \\in [0, 0.2]$ (Appendix~\\ref{app:epsilon_robustness}), and temperature $T \\in \\{0.5, 0.7, 1.0, 1.2\\}$ (Appendix~\\ref{app:t_ablation}).\n\n\\paragraph{O4: Findings may be a fine-tuning artifact.}\nQwen2.5-72B zero-shot exhibits the same gap: LP $\\rho$ drops without fine-tuning, structural signals generalize (VC $\\rho{=}0.416$ on Few-NERD), and degeneracy is model-family-dependent rather than scale-dependent (Qwen2.5: 31.7--46.2\\% vs.\\ Qwen3: 13.0\\%; Appendix~\\ref{app:cross_scale}). The capability ceiling persists from 4B to 72B.\n\n\\paragraph{O5: Probe AUROC varies widely (0.63--0.88); why trust the result?}\nThe variation is complexity-dependent and interpretable: CoNLL (4 types, 91\\% F1) at 0.882, Few-NERD (8 types, 75\\% F1) at 0.636, SciERC (6 types, 65\\% F1) at 0.630. LODO transfer drops to 0.56--0.67 (\\S\\ref{sec:mechanistic}), confirming dataset-specific encoding. The pattern---not the point estimate---is the finding.\n\n\\paragraph{O6: Theory is disconnected from experiments.}\nEach formal result has explicit empirical validation: Proposition~\\ref{prop:construction_mbr} (MBR equivalence) $\\to$ Table~\\ref{tab:entity_construction}; Proposition~\\ref{prop:entity_selection_bound} (entity selection bound) $\\to$ Table~\\ref{tab:alpha_crit} across 3 datasets; Degeneracy Decomposition $\\to$ Figure~\\ref{fig:bound} across 16 configurations (\\S\\ref{sec:theory}); oracle scaling law $\\to$ Figure~\\ref{fig:oracle_scaling} ($R^2 > 0.999$; \\S\\ref{sec:scaling}).\n\n\\paragraph{O7: Why not use standard MBR decoding?}\nMajority vote \\textit{is} MBR decoding under set-overlap utility (Proposition~\\ref{prop:construction_mbr}; \\S\\ref{sec:mbr_theory}). LP-weighted construction is the quality-aware MBR variant (\\S\\ref{sec:mbr_theory}). This follows directly from \\citet{eikema2022sampling}; \\citet{eikema2025structured} confirm that MBR utilities degrade on structured outputs, consistent with our LP compression findings.\n\n\\paragraph{O8: No qualitative error analysis.}\nAppendix~\\ref{app:failure_gallery} provides a failure mode gallery with 9 concrete instances: 3 degenerate (all samples identical), 3 LP selection failures (high-LP sample worse than low-LP), and 3 self-verification failures (ESJ misclassifies entity correctness). Each includes instance text, gold annotations, predictions, and signal values.\n\n\\paragraph{O9: Evaluation metric choice may bias results.}\nWe report per-instance F1 averaged across instances (macro F1) as the primary selection metric. Aggregate micro-F1 (pooled TP/FP/FN) confirms MV fails to improve over greedy: $\\Delta$ ranges from $-2.74$ to ${\\approx}0$\\,pp (Table~\\ref{tab:alpha_crit}; Appendix~\\ref{app:alpha_crit}). The correlation-selection gap holds under both aggregations; the selection failure is not an artifact of the metric.\n\n\\paragraph{O10: Computational cost analysis is missing.}\nTable~\\ref{tab:cost_benefit} (Appendix~\\ref{app:cost_benefit}) provides a cost-benefit breakdown. Entity construction achieves the best cost-efficiency: $+0.32$--$1.40$\\,pp at $N{\\times}$ cost with zero marginal overhead beyond sampling. Cross-model ensemble doubles inference cost for $+0.42$\\,pp.\n\n\\paragraph{O11: Reproducibility concerns.}\nAll experiments use open-weight models (Qwen3-8B, LLaMA-3.1-8B, Qwen3-4B, Qwen2.5-7B, Qwen2.5-72B) and public benchmarks. Multi-seed stability ($\\sigma{\\leq}0.026$ for QE; Table~\\ref{tab:multiseed}) and full hyperparameter sweeps are reported. Code, checkpoints, and per-seed results will be released upon acceptance.\n\n\\paragraph{O12: Overlap with \\citet{yun2025price}.}\n\\S\\ref{sec:yun_contrast} provides a three-way differentiation. Our LP compression (median 0.041 nats) corroborates Yun et al.'s diversity collapse, but we diverge in root cause (model-internal vs.\\ format-induced), diagnostic depth (diagnostic framework with 9 method categories vs.\\ diversity analysis), and scale ($4{\\times}$: Qwen2.5-72B). Table~\\ref{tab:differentiation} (Appendix~\\ref{app:differentiation}) provides the full comparison matrix.\n\n\\section{Failure Mode Gallery}\\label{app:failure_gallery}\n\nWe present 9 concrete instances illustrating the three primary failure modes: output degeneracy, LP confidence inversion, and consensus-based verification failure. All examples use Qwen3-8B on Few-NERD ($N{=}8$, $T{=}1.0$) from the MF4v2 pipeline.\n\n\\paragraph{Degenerate instances (3/3).}\nAll $N$ samples produce identical entity sets, eliminating any room for selection or construction improvement.\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Type confusion.} \\textit{``His undergraduate studies at the University of Notre Dame were interrupted by Army service in World War II.''} Gold: \\{University of Notre Dame / building\\}. All 8 samples: \\{University of Notre Dame / \\textbf{organization}, World War II / event\\}. F1${=}0.00$: correct span, wrong type, plus hallucinated entity.\n\n\\item \\textbf{Type confusion (minimal).} \\textit{``...the deployment of the `SPQ' template...''} Gold: \\{SPQ / organization\\}. All 8 samples: \\{SPQ / \\textbf{product}\\}. F1${=}0.00$: entity text matches exactly but type disagrees across all samples.\n\n\\item \\textbf{Complete miss.} \\textit{``On stage, the band uses different kinds of instruments like synths, guitars, cello, glockenspiel and a bass played with a sickle.''} Gold: 6 entities (synths, guitars, cello, glockenspiel, bass, sickle / product). All 8 samples: $\\emptyset$. F1${=}0.00$: total recall failure on all gold entities.\n\\end{itemize}\n\n\\paragraph{LP confidence failures (3/3).}\nHigh log-probability does not guarantee correctness at the entity level. These entities appear in all 8 samples with near-zero negative log-probability (high confidence), yet are absent from the gold annotation.\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textit{``Cramer pitched for the Orange County Flyers of the independent Golden League in 2008.''} Entity: Cramer / person (mean LP${=}{-}0.046$, 8/8 samples). Gold: \\{Orange County Flyers / org, independent Golden League / org\\}. Plausible entity, not annotated.\n\n\\item \\textit{``...according to UK Royal Air Force Wing Commander and FOD researcher Richard Friend.''} Entity: Richard Friend / person (mean LP${=}{-}0.050$, 8/8). Gold: \\{UK Royal Air Force / org, FOD / org\\}. Likely annotation gap: Richard Friend is a real person mentioned by name; gold omits it.\n\n\\item \\textit{``...the Navy's forces within South Vietnam were operationally controlled by COMUSMACV.''} Entity: COMUSMACV / org (mean LP${=}{-}0.050$, 8/8). Gold: \\{Seventh Fleet / org, South Vietnam / location\\}. Model confidently extracts a valid entity missing from gold.\n\\end{itemize}\n\n\\noindent These examples highlight a fundamental limitation: LP signals the model's confidence, not correctness. When the model is correctly confident about entities that gold annotations omit, LP cannot serve as an error detector.\n\n\\paragraph{Consensus-based verification failures (3/3).}\nEntity consensus frequency (fraction of $N$ samples containing a given entity) serves as the primary self-verification signal. It fails in both directions.\n\n\\begin{itemize}[nosep,leftmargin=*]\n\\item \\textbf{Overconfident.} \\textit{``Les Blank...was an American documentary filmmaker best known for his portraits of American traditional musicians.''} Entity: American / location (8/8 samples, consensus${=}1.0$). Gold: \\{Les Blank / person\\}. Maximum consensus for non-gold entity.\n\n\\item \\textbf{Overconfident.} \\textit{``Cramer pitched for the Orange County Flyers of the independent Golden League in 2008.''} Entity: Cramer / person (8/8 samples, consensus${=}1.0$). Gold: \\{Orange County Flyers / org, independent Golden League / org\\}. Same instance as LP failure above---simultaneous failure of both signals.\n\n\\item \\textbf{Underconfident.} \\textit{``They finished the season 14--19, 9--9 in C-USA play to finish in seventh place.''} Gold entity: C-USA play / event (consensus${=}0.0$, never predicted in any of 8 samples). Zero consensus for a correct entity.\n\\end{itemize}\n\n\\noindent These examples illustrate that the failure modes identified by the diagnostic framework are not statistical abstractions but manifest in individual instances. The LP and consensus failures frequently co-occur (e.g., ``Cramer'' instance), confirming that the signals share common blind spots rather than providing independent error detection.\n\n\\section{Practical Recommendations}\\label{app:recommendations}\n\nMeasuring degeneracy and LP-F1 alignment at $N{=}8$ suffices: if ${>}50$\\% degenerate, scaling provides no benefit; if degeneracy ${<}20$\\% with $\\rho{>}0.70$, construction may yield gains; otherwise prefer greedy.\n\n\\section{Use of AI Assistants}\n\\label{app:ai-assistants}\n\nWe used Claude (Anthropic) as an AI coding and writing assistant\nthroughout this work. Specifically:\n\\begin{itemize}\n    \\item \\textbf{Code:} drafting experiment scripts, data-processing\n    pipelines, and analysis utilities; debugging and refactoring.\n    \\item \\textbf{Writing:} drafting and revising paper sections,\n    polishing prose, and reformatting LaTeX.\n    \\item \\textbf{Literature:} summarizing related papers to inform\n    related-work section.\n\\end{itemize}\n",
    "structuredPatch": [
      {
        "oldStart": 761,
        "oldLines": 7,
        "newStart": 761,
        "newLines": 7,
        "lines": [
          " \\midrule",
          " \\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\",
          " SciERC split & 1861 / 275 / 551 \\\\",
          "-CoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\",
          "+CoNLL / WNUT-17 & +\\,load\\_best\\_model\\_at\\_end, \\\\",
          " & eval\\_steps${=}$200, save\\_limit${=}$5 \\\\",
          " \\bottomrule",
          " \\end{tabular}"
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

_source line 86_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a33b0e95-dbad-4d3e-b94d-d687a9d1886d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtLiDTbURbEkHEyMEqPsmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 72798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 333
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

### Tool call

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01Ht3vhn7MtdQdBputmGUEvY`</summary>

```json
{
  "command": "grep -P \"\\b(CONLL|Conll|conll)\\b\" sections/*.tex 2>/dev/null | grep -v \"_archived\" | grep -v \"\\\\\\\\cite{.*conll\\|\\\\\\\\label{.*conll\\|tjongkimsang2003conll\"",
  "description": "Find non-standard conll references excluding labels/citations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "2b6a37e4-9686-43ef-ab49-e82cb3ef2667",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DtLiDTbURbEkHEyMEqPsmJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 333,
      "cache_read_input_tokens": 72798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 333
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

### Tool result

_source line 88 · 2026-05-24T01:37:30.137Z_

<details><summary>↩ Tool result · `toolu_01Ht3vhn7MtdQdBputmGUEvY`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1c2984ec-8b7e-4d01-8666-f99258a43d0e",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_01BoJuErLCMnmDE5bUvdBDSr`</summary>

```json
{
  "command": "grep -Pn \"\\b(SCIERC|sci-erc|Sci-erc|Sci-ERC)\\b\" sections/*.tex 2>/dev/null | grep -v \"_archived\"",
  "description": "Find non-standard SciERC variants"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "4d364424-8bf6-4cb7-b57c-6c3b20293749",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NhHAJVWgLsqehzCmHZusoz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 355,
      "cache_read_input_tokens": 73131,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 355
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 90 · 2026-05-24T01:37:33.048Z_

<details><summary>↩ Tool result · `toolu_01BoJuErLCMnmDE5bUvdBDSr`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "fa0c0779-07ab-47f9-a4e2-1bd0c8664b19",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01S329Ym1gJENaTiVxvFfeym`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /tmp/compile1.log 2>&1 && bibtex main > /tmp/bibtex.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile2.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile3.log 2>&1; echo \"Exit: $?\"; pdfinfo main.pdf | grep -i pages",
  "description": "Recompile after dataset name fixes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a28bb0f3-7a9d-4281-b63e-a2ccbd4b01b9",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01YEXXEwg3ZfL9HKxBGDp7pS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 181,
      "cache_read_input_tokens": 73486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 181
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

### System

_source line 92_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bme6xwyzy",
  "tool_use_id": "toolu_01S329Ym1gJENaTiVxvFfeym",
  "description": "Recompile after dataset name fixes",
  "task_type": "local_bash",
  "uuid": "14a681f3-e569-4d19-a4bb-d242c9a2ede0",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### System

_source line 93_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bme6xwyzy",
  "tool_use_id": "toolu_01S329Ym1gJENaTiVxvFfeym",
  "status": "completed",
  "output_file": "",
  "summary": "Recompile after dataset name fixes",
  "uuid": "675b9b7a-558f-48fe-a7c2-2bdf7d55c29f",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### Tool result

_source line 94 · 2026-05-24T01:37:43.980Z_

<details><summary>↩ Tool result · `toolu_01S329Ym1gJENaTiVxvFfeym`</summary>

```text
Exit: 0
Pages:           46
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "21471a22-8703-485a-8f8f-0e9209ec2f1b",
  "tool_use_result": {
    "stdout": "Exit: 0\nPages:           46",
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

_source line 95_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01KrMTn29m9NAsH2iht9LKy7`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "completed"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "completed"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "in_progress"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "pending"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "completed"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "pending"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "pending"
    },
    {
      "content": "Sync to anonymous repo if changes were made",
      "activeForm": "Syncing to anonymous repo",
      "status": "pending"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "0228a773-568b-418f-9a3b-c84a9c5a15e8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FwwLhCKL9NeCvvSiR9PcvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 285,
      "cache_read_input_tokens": 73667,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 285
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

_source line 96 · 2026-05-24T01:37:52.298Z_

<details><summary>↩ Tool result · `toolu_01KrMTn29m9NAsH2iht9LKy7`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "947ade8c-9921-495f-a48a-2a46b52790ef",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "in_progress",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "pending",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "in_progress",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 97_

<details open><summary>🔧 Tool call — Read · `toolu_017eGaghK2pQfR63ehfg5Y36`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
  "offset": 1590,
  "limit": 35
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "44123493-0010-49b4-a09f-f46a0210ee50",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01RTaiKus7jX5eFBmTpNG6Xx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 498,
      "cache_read_input_tokens": 73952,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 498
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 98 · 2026-05-24T01:37:56.692Z_

<details><summary>↩ Tool result · `toolu_017eGaghK2pQfR63ehfg5Y36`</summary>

```text
1590	\bottomrule
1591	\end{tabular}}
1592	\end{table}
1593	
1594	\section{Cross-Scale and Cross-Family Comparison}\label{app:cross_scale}
1595	
1596	\begin{table}[t]
1597	\centering
1598	\small
1599	\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
1600	\label{tab:scale_comparison}
1601	\resizebox{\columnwidth}{!}{%
1602	\begin{tabular}{@{}llccccccc@{}}
1603	\toprule
1604	Dataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\
1605	\midrule
1606	SciERC & 8B FT  & .667 & 11.4 & 12.2 & .326 & .324 & .177 & .159 \\
1607	       & 72B ZS$^\star$ & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\
1608	\midrule
1609	Few-NERD & 7B FT$^\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\
1610	         & 8B FT & .748 & 12.4 & 13.0 & .386 & .300 & .313 & .220 \\
1611	         & 14B FT & .798 & 8.1 & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ & ---$^\dagger$ \\
1612	         & 72B ZS$^\star$ & .628 & ---$^\dagger$ & 46.2 & .416 & .345 & ---$^\dagger$ & .119 \\
1613	         & GPT-5.5 ZS$^\ddagger$ & .638 & 8.2 & 50.0 & ---$^\dagger$ & .346 & ---$^\dagger$ & ---$^\dagger$ \\
1614	\midrule
1615	CoNLL  & 8B FT  & .908 & ${\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\
1616	       & 72B ZS$^\star$ & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\
1617	\bottomrule
1618	\end{tabular}}
1619	\end{table}
1620	
1621	LP $\rho$ drops without fine-tuning (Table~\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\% vs.\ $13.0$\%; CoNLL: $67.7$\% vs.\ $61.7$\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).
1622	LP-weighted construction yields $+1.53$\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\% of headroom. Construction fails on Few-NERD ($-0.20$\,pp) and CoNLL ($-0.37$\,pp) where degeneracy exceeds $46$\%---consistent with FT-regime degeneracy gating.
1623	
1624	\paragraph{Few-shot demonstrations improve QE but not construction.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "fe178818-8cbc-492a-ad25-e7f901305993",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\bottomrule\n\\end{tabular}}\n\\end{table}\n\n\\section{Cross-Scale and Cross-Family Comparison}\\label{app:cross_scale}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\n\\label{tab:scale_comparison}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}llccccccc@{}}\n\\toprule\nDataset & Regime & Greedy & Hdr. & Degen. & VC & SJ & FK & LP \\\\\n\\midrule\nSciERC & 8B FT  & .667 & 11.4 & 12.2 & .326 & .324 & .177 & .159 \\\\\n       & 72B ZS$^\\star$ & .399 & 15.0 & 21.0 & .277 & .217 & .227 & .081 \\\\\n\\midrule\nFew-NERD & 7B FT$^\\star$ & .784 & 9.2 & 31.7 & .404 & .388 & .315 & .346 \\\\\n         & 8B FT & .748 & 12.4 & 13.0 & .386 & .300 & .313 & .220 \\\\\n         & 14B FT & .798 & 8.1 & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ & ---$^\\dagger$ \\\\\n         & 72B ZS$^\\star$ & .628 & ---$^\\dagger$ & 46.2 & .416 & .345 & ---$^\\dagger$ & .119 \\\\\n         & GPT-5.5 ZS$^\\ddagger$ & .638 & 8.2 & 50.0 & ---$^\\dagger$ & .346 & ---$^\\dagger$ & ---$^\\dagger$ \\\\\n\\midrule\nCoNLL  & 8B FT  & .908 & ${\\approx}$4 & 61.7 & .424 & .436 & .400 & .302 \\\\\n       & 72B ZS$^\\star$ & .712 & 5.3 & 67.7 & .297 & .304 & .302 & $-$.002 \\\\\n\\bottomrule\n\\end{tabular}}\n\\end{table}\n\nLP $\\rho$ drops without fine-tuning (Table~\\ref{tab:scale_comparison}) and LP selection fails on all 72B zero-shot datasets. Structural signals generalize better (Few-NERD VC $\\rho{=}0.416$). Degeneracy increases at 72B (Few-NERD: $46.2$\\% vs.\\ $13.0$\\%; CoNLL: $67.7$\\% vs.\\ $61.7$\\%); the gap persists under this specific 72B zero-shot configuration, though scale, training regime, and quantization effects are confounded (see Limitations).\nLP-weighted construction yields $+1.53$\\,pp on SciERC 72B ZS ($p{=}0.008$, CI [$+0.25$, $+2.82$]), recovering $10.2$\\% of headroom. Construction fails on Few-NERD ($-0.20$\\,pp) and CoNLL ($-0.37$\\,pp) where degeneracy exceeds $46$\\%---consistent with FT-regime degeneracy gating.\n\n\\paragraph{Few-shot demonstrations improve QE but not construction.}",
      "numLines": 35,
      "startLine": 1590,
      "totalLines": 2569
    }
  }
}
```

</details>

---

### Assistant

_source line 99_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5f77616f-a2f1-4a07-aa3d-c1eb6b3afd88",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KhcF6FU9uBpRQNvHVBKPLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 74450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1575
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 100_

<details open><summary>🔧 Tool call — Bash · `toolu_01A64TFURpivSA2N3h1ng4SS`</summary>

```json
{
  "command": "grep -n \"label{tab:fewnerd}\\|label{tab:selection}\" sections/*.tex 2>/dev/null | grep -v \"_archived\"",
  "description": "Check tab labels"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "6d619671-2767-4d90-bb85-260253d3d71a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KhcF6FU9uBpRQNvHVBKPLH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1575,
      "cache_read_input_tokens": 74450,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1575
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 101 · 2026-05-24T01:38:04.188Z_

<details><summary>↩ Tool result · `toolu_01A64TFURpivSA2N3h1ng4SS`</summary>

```text
sections/experiments_main.tex:62:\label{tab:fewnerd}
sections/single_signal.tex:13:\label{tab:selection}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "848e8aad-6e1c-4c50-bded-6a0a6f9759e2",
  "tool_use_result": {
    "stdout": "sections/experiments_main.tex:62:\\label{tab:fewnerd}\nsections/single_signal.tex:13:\\label{tab:selection}",
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

_source line 102_

<details open><summary>🔧 Tool call — Read · `toolu_01979bVJdkzKKjT7inryds1k`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
  "offset": 55,
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "266f19d6-146f-4c11-ab8b-abd62ca03d07",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P4aXRauGsLp2i2AYGgnH56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 76025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 518
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 103 · 2026-05-24T01:38:08.623Z_

<details><summary>↩ Tool result · `toolu_01979bVJdkzKKjT7inryds1k`</summary>

```text
55	%% ============================================================
56	\subsection{Cross-Dataset Contrast: Few-NERD}\label{sec:fewnerd}
57	
58	\begin{table}[t]
59	\centering
60	\small
61	\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}
62	\label{tab:fewnerd}
63	\resizebox{\columnwidth}{!}{%
64	\begin{tabular}{@{}lrccccr@{}}
65	\toprule
66	Dataset & $n$ & Greedy & Degen.\% & LP $\rho$ & LP $\Delta$ & $p$ \\
67	\midrule
68	WNUT-17 & 1{,}287 & .452 & 67.9\% & $-$.446 & $-$0.45\,pp & .72 \\
69	CoNLL & 2{,}756 & .908 & 61.7\% & .302 & $-$0.85\,pp & 1.0 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "4c53ee9a-b3e3-4bf5-845e-667944f4013a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments_main.tex",
      "content": "%% ============================================================\n\\subsection{Cross-Dataset Contrast: Few-NERD}\\label{sec:fewnerd}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}\n\\label{tab:fewnerd}\n\\resizebox{\\columnwidth}{!}{%\n\\begin{tabular}{@{}lrccccr@{}}\n\\toprule\nDataset & $n$ & Greedy & Degen.\\% & LP $\\rho$ & LP $\\Delta$ & $p$ \\\\\n\\midrule\nWNUT-17 & 1{,}287 & .452 & 67.9\\% & $-$.446 & $-$0.45\\,pp & .72 \\\\\nCoNLL & 2{,}756 & .908 & 61.7\\% & .302 & $-$0.85\\,pp & 1.0 \\\\",
      "numLines": 15,
      "startLine": 55,
      "totalLines": 116
    }
  }
}
```

</details>

---

### Tool call

_source line 104_

<details open><summary>🔧 Tool call — Read · `toolu_01Ps3Ee7t11UjRcYQzTiJXbt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
  "offset": 1,
  "limit": 25
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "7f6432c9-45ef-4fb4-ad56-df142f77a892",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01P4aXRauGsLp2i2AYGgnH56",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 518,
      "cache_read_input_tokens": 76025,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 518
      },
      "output_tokens": 41,
      "service_tier": "standard",
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

_source line 105 · 2026-05-24T01:38:09.798Z_

<details><summary>↩ Tool result · `toolu_01Ps3Ee7t11UjRcYQzTiJXbt`</summary>

```text
1	\section{Single-Signal Selection Results}\label{sec:selection_gap}
2	
3	\paragraph{Definitional vs.\ empirical.}
4	We decompose the correlation-selection gap into two layers.
5	The first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\S\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.
6	The second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\ref{app:logprob_ties}), leaving insufficient variation for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\times}$; Appendix~\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.
7	Cross-instance $\rho$ (Table~\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.
8	
9	\begin{table}[t]
10	\centering
11	\small
12	\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
13	\label{tab:selection}
14	\begin{tabular}{lcc}
15	\toprule
16	Method & NER F1 & $p$ \\
17	\midrule
18	Oracle & $0.775 \pm 0.001$ & --- \\
19	Greedy ($T{=}0$) & $0.645 \pm 0.001$ & --- \\
20	\midrule
21	LP           & $\mathbf{0.647} \pm 0.005$ & .29 \\
22	SJ           & $0.646 \pm 0.002$ & .67 \\
23	FK           & $0.646 \pm 0.001$ & .79 \\
24	EM           & $0.637 \pm 0.001$ & n/a$^\dagger$ \\
25	VC           & $0.623 \pm 0.004$ & n/a$^\dagger$ \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "4701d3b3-7864-463b-a4b8-e946215f14c2",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/single_signal.tex",
      "content": "\\section{Single-Signal Selection Results}\\label{sec:selection_gap}\n\n\\paragraph{Definitional vs.\\ empirical.}\nWe decompose the correlation-selection gap into two layers.\nThe first is structural: four of five signals are instance-level aggregates that assign identical scores to all $N$ candidates from a given input (\\S\\ref{sec:formulation}), so they estimate quality across inputs but cannot rank candidates within an instance---selection failure is a design property, not an empirical finding.\nThe second layer is empirical and constitutes the core diagnostic: LP---the only per-sample signal---suffers compression under constrained decoding, with 60\\% of SciERC instances showing within-instance LP range below 0.041 nats (Appendix~\\ref{app:logprob_ties}), leaving insufficient variation for sample discrimination. This compression is model-intrinsic: free-form decoding yields nearly identical LP distributions (within-instance std ratio $0.97{\\times}$; Appendix~\\ref{app:freeform_ablation}). Even where LP varies, selection gains depend on LP-quality alignment rather than degeneracy alone.\nCross-instance $\\rho$ (Table~\\ref{tab:quality_estimation}) is attenuated by varying instance difficulty; within-instance $\\rho$ directly measures whether LP discriminates candidates for a fixed input, making it the relevant predictor of selection success.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\\pm}\\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\\dagger$One score per input.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & $p$ \\\\\n\\midrule\nOracle & $0.775 \\pm 0.001$ & --- \\\\\nGreedy ($T{=}0$) & $0.645 \\pm 0.001$ & --- \\\\\n\\midrule\nLP           & $\\mathbf{0.647} \\pm 0.005$ & .29 \\\\\nSJ           & $0.646 \\pm 0.002$ & .67 \\\\\nFK           & $0.646 \\pm 0.001$ & .79 \\\\\nEM           & $0.637 \\pm 0.001$ & n/a$^\\dagger$ \\\\\nVC           & $0.623 \\pm 0.004$ & n/a$^\\dagger$ \\\\",
      "numLines": 25,
      "startLine": 1,
      "totalLines": 57
    }
  }
}
```

</details>

---

### Assistant

_source line 106_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "e08fabff-a58b-4de1-b41e-03e54ab321f6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SPWEJWoysywQbAdjdNCekE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1696,
      "cache_read_input_tokens": 76543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1696
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

### Assistant

_source line 107_

The cross-table footnote already exists with the proper explanation and cross-ref. Moving to captions review.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d5bf623c-0e5f-4034-b3b5-bb63d0120a59",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SPWEJWoysywQbAdjdNCekE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1696,
      "cache_read_input_tokens": 76543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1696
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

_source line 108_

<details open><summary>🔧 Tool call — Grep · `toolu_019eS8e29prb7umxvB6Pr2Yj`</summary>

```json
{
  "pattern": "\\\\caption\\{",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "805b60fc-57fb-4905-aa94-2b0e0aed0ddc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SPWEJWoysywQbAdjdNCekE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1696,
      "cache_read_input_tokens": 76543,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1696
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

_source line 109 · 2026-05-24T01:38:21.896Z_

<details><summary>↩ Tool result · `toolu_019eS8e29prb7umxvB6Pr2Yj`</summary>

```text
&lt;persisted-output>
Output too large (23.6KB). Full output saved to: /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/56622092-b880-43f3-8cd7-2a5161528236/tool-results/toolu_019eS8e29prb7umxvB6Pr2Yj.txt

Preview (first 2KB):
sections/theory.tex:18:\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\S\ref{sec:selection_gap}) limits how much is actually recoverable.}
sections/theory.tex:43:\caption{SC gain vs.\ degeneracy across 16 configurations (SciERC-specific $\alpha$). Red: signal-adjusted bound ($\alpha{=}0.068$); vertical dashed: $\theta_{\text{crit}}{=}0.70$; horizontal dotted: $\varepsilon{=}0.3$\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}
sections/_archived/experiments_OLD.tex:25:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
sections/_archived/experiments_OLD.tex:63:\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\pm}\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \textbf{bold}. Non-tied subset in \S\ref{sec:discussion}; RE in Appendix~\ref{app:re_extension}. $^\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}
sections/_archived/experiments_OLD.tex:89:\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\rho$ (seed 42); line with error bars: $\Delta$F1 vs.\ greedy (3-seed mean, seeds 42/123/456). Despite $\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}
...
&lt;/persisted-output>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "e612a92e-55af-450c-9a19-1cc2ca433883",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/theory.tex:18:\\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \\cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\\S\\ref{sec:selection_gap}) limits how much is actually recoverable.}\nsections/theory.tex:43:\\caption{SC gain vs.\\ degeneracy across 16 configurations (SciERC-specific $\\alpha$). Red: signal-adjusted bound ($\\alpha{=}0.068$); vertical dashed: $\\theta_{\\text{crit}}{=}0.70$; horizontal dotted: $\\varepsilon{=}0.3$\\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}\nsections/_archived/experiments_OLD.tex:25:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 3-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\nsections/_archived/experiments_OLD.tex:63:\\caption{Best-of-$N$ NER selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$, 2-seed mean${\\pm}\\sigma$). LP is per-sample; others use consensus-proximity. Best non-oracle in \\textbf{bold}. Non-tied subset in \\S\\ref{sec:discussion}; RE in Appendix~\\ref{app:re_extension}. $^\\dagger$Instance-level signals assign one score per input; per-sample ranking $p$-values are undefined.}\nsections/_archived/experiments_OLD.tex:89:\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: quality estimation $\\rho$ (seed 42); line with error bars: $\\Delta$F1 vs.\\ greedy (3-seed mean, seeds 42/123/456). Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy (all $p{>}0.05$; Table~\\ref{tab:selection}). Dashed green: oracle upper bound ($+13.0$~pp); dotted gray: random baseline.}\nsections/_archived/experiments_OLD.tex:113:\\caption{LP selection across datasets (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered). Few-NERD/CoNLL: 3-seed means; SciERC: single-seed (3-seed in Table~\\ref{tab:multiseed}). $p$: paired bootstrap.}\nsections/_archived/experiments_OLD.tex:136:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type analysis ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}\nsections/_archived/experiments_OLD.tex:151:\\caption{Scale ablation: 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\nsections/_archived/experiments_OLD.tex:182:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed.}\nsections/_archived/experiments_OLD.tex:226:\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. Best in \\textbf{bold}. $^\\dagger$Survives Holm--Bonferroni correction ($k{=}57$). $^\\ddagger$LP-weighted not computed; uniform only.}\nsections/single_signal.tex:12:\\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\\pm}\\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\\dagger$One score per input.}\nsections/single_signal.tex:35:\\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\\rho$; line: $\\Delta$F1 vs.\\ greedy (3-seed mean). Despite $\\rho$ up to 0.38, no signal outperforms greedy (all $p{\\geq}0.29$). Dashed green: oracle headroom ($+13.0$\\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}\nsections/adaptive.tex:9:\\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\\ref{sec:mechanistic} and adaptive methods in this section). $\\Delta$F1 vs.\\ greedy; dataset in parentheses. Full coverage in Appendix~\\ref{app:method_coverage}.}\nsections/background.tex:21:\\caption{Novelty comparison with closest related work along six dimensions.}\nsections/appendix.tex:25:\\caption{Notation used throughout the paper.}\nsections/appendix.tex:37:\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\nsections/appendix.tex:70:\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\nsections/appendix.tex:102:\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\nsections/appendix.tex:127:\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\nsections/appendix.tex:139:\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\nsections/appendix.tex:164:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\nsections/appendix.tex:183:\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\nsections/appendix.tex:213:\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:280:\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\nsections/appendix.tex:326:\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\nsections/appendix.tex:420:\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\nsections/appendix.tex:450:\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\nsections/appendix.tex:480:\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\nsections/appendix.tex:557:\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}\nsections/appendix.tex:588:\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\nsections/appendix.tex:643:\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\nsections/appendix.tex:688:\\caption{Entity-level self-verification: ESJ vs.\\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}\nsections/appendix.tex:711:\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over seeds.}\nsections/appendix.tex:740:\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\nsections/appendix.tex:818:\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\nsections/appendix.tex:825:\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\nsections/appendix.tex:852:\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\nsections/appendix.tex:878:\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\nsections/appendix.tex:901:\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\nsections/appendix.tex:927:\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}\nsections/appendix.tex:950:\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\nsections/appendix.tex:969:\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\nsections/appendix.tex:1004:\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\nsections/appendix.tex:1072:\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\nsections/appendix.tex:1101:\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\nsections/appendix.tex:1196:\\caption{Bound verification across representative configurations ($N{=}8$). $G_{\\text{nd}}$: non-degenerate oracle gap. $\\alpha$: signal alignment. Bound: $(1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$. Ratio: actual$/$weak bound.}\nsections/appendix.tex:1257:\\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$). $\\alpha_{\\textup{crit}} = F_1^{\\textup{gr}}/2$; $\\alpha_{\\textup{crit,eff}} = \\alpha_{\\textup{crit}} / (1{-}\\delta)$. When $\\alpha_{\\textup{crit,eff}} > 1$, MV gain is structurally impossible.}\nsections/appendix.tex:1284:\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\nsections/appendix.tex:1361:\\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\\,/\\,constrained within-instance LP std. Arrows: constrained $\\to$ free-form.}\nsections/appendix.tex:1402:\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\nsections/appendix.tex:1428:\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\nsections/appendix.tex:1452:\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\nsections/appendix.tex:1472:\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\nsections/appendix.tex:1510:\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\nsections/appendix.tex:1537:\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\nsections/appendix.tex:1573:\\caption{Inverse scaling rate by degeneracy status. An $N{\\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1635:\\caption{Scale ablation: Qwen3 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\nsections/appendix.tex:1662:\\caption{Pretrained vs.\\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\\text{MV}\\,\\Delta / \\text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\\pm}\\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}\nsections/appendix.tex:1701:\\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}\nsections/appendix.tex:1733:\\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}\nsections/appendix.tex:1774:\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\nsections/appendix.tex:1807:\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\nsections/appendix.tex:1830:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\nsections/appendix.tex:1871:\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\nsections/appendix.tex:1908:\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\nsections/appendix.tex:1939:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:1975:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\nsections/appendix.tex:1998:\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\nsections/appendix.tex:2015:\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\nsections/appendix.tex:2049:[Omitted long matching line]\nsections/appendix.tex:2083:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\nsections/appendix.tex:2114:[Omitted long matching line]\nsections/appendix.tex:2160:\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:2186:\\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\\alpha{=}0.05$). At this sample size, only large correlations ($\\rho{\\geq}0.5$) are detectable with adequate power.}\nsections/appendix.tex:2213:\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\nsections/appendix.tex:2238:\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\nsections/appendix.tex:2260:\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. $^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}\nsections/appendix.tex:2284:\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\nsections/appendix.tex:2346:\\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\\theta{=}2/N$, 3-seed mean). $\\Delta$: F1 difference vs.\\ greedy in pp. Main-text construction results (Table~\\ref{tab:entity_construction}) use Qwen3-8B.}\nsections/appendix.tex:2366:\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\nsections/appendix.tex:2419:\\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\\Delta$F1 reports the primary result (dataset in parentheses).}\nsections/appendix.tex:2448:\\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}\nsections/introduction.tex:19:[Omitted long matching line]\nsections/experiments_main.tex:19:\\caption{MV $\\Delta$F1 vs.\\ $\\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\\,pp at $N{=}64$).}\nsections/experiments_main.tex:29:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\nsections/experiments_main.tex:61:\\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}\nsections/experiments_main.tex:86:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}",
    "numLines": 89
  }
}
```

</details>

---

### Tool call

_source line 110_

<details open><summary>🔧 Tool call — Bash · `toolu_01A8H8hjBCAoeM7R2jcQmtgK`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/56622092-b880-43f3-8cd7-2a5161528236/tool-results/toolu_019eS8e29prb7umxvB6Pr2Yj.txt | grep -v \"_archived\" | head -200",
  "description": "Read all captions from active files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d0a385f1-492b-464b-bef0-0356d4e3fbf6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018ZPj6396ah3T4gyhz3aKh9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1766,
      "cache_read_input_tokens": 78239,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1766
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

_source line 111 · 2026-05-24T01:38:29.547Z_

<details><summary>↩ Tool result · `toolu_01A8H8hjBCAoeM7R2jcQmtgK`</summary>

```text
sections/theory.tex:18:\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\S\ref{sec:selection_gap}) limits how much is actually recoverable.}
sections/theory.tex:43:\caption{SC gain vs.\ degeneracy across 16 configurations (SciERC-specific $\alpha$). Red: signal-adjusted bound ($\alpha{=}0.068$); vertical dashed: $\theta_{\text{crit}}{=}0.70$; horizontal dotted: $\varepsilon{=}0.3$\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}
sections/single_signal.tex:12:\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
sections/single_signal.tex:35:\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up to 0.38, no signal outperforms greedy (all $p{\geq}0.29$). Dashed green: oracle headroom ($+13.0$\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}
sections/adaptive.tex:9:\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
sections/background.tex:21:\caption{Novelty comparison with closest related work along six dimensions.}
sections/appendix.tex:25:\caption{Notation used throughout the paper.}
sections/appendix.tex:37:\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
sections/appendix.tex:70:\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
sections/appendix.tex:102:\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
sections/appendix.tex:127:\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
sections/appendix.tex:139:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
sections/appendix.tex:164:\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
sections/appendix.tex:183:\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
sections/appendix.tex:213:\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
sections/appendix.tex:239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
sections/appendix.tex:280:\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
sections/appendix.tex:326:\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\dagger$Survives correction at $\alpha{=}0.05$.}
sections/appendix.tex:420:\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
sections/appendix.tex:450:\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
sections/appendix.tex:480:\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
sections/appendix.tex:557:\caption{Hidden state probes vs.\ LP for sample selection (5-fold CV ${\times}$ 3 seeds). $\rho$: Spearman correlation with per-sample F1. Sel.\ F1: selection F1. Gap\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}
sections/appendix.tex:588:\caption{Experimental coverage of entity-level methods. \checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}
sections/appendix.tex:643:\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}
sections/appendix.tex:688:\caption{Entity-level self-verification: ESJ vs.\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}
sections/appendix.tex:711:\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over seeds.}
sections/appendix.tex:740:\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
sections/appendix.tex:818:\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
sections/appendix.tex:825:\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
sections/appendix.tex:852:\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
sections/appendix.tex:878:\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
sections/appendix.tex:901:\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Table~\ref{tab:epsilon_sweep}.}
sections/appendix.tex:927:\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\text{valid}}$: ${\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}
sections/appendix.tex:950:\caption{$\varepsilon$ threshold vs.\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\%: instances with LP range ${<}\varepsilon$. $\rho$: Spearman correlation between LP and oracle F1. $\varepsilon{=}0.05$ (bold) is the elbow.}
sections/appendix.tex:969:\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\geq}0.05$ show $3$--$6{\times}$ larger advantage.}
sections/appendix.tex:1004:\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
sections/appendix.tex:1072:\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
sections/appendix.tex:1101:\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
sections/appendix.tex:1196:\caption{Bound verification across representative configurations ($N{=}8$). $G_{\text{nd}}$: non-degenerate oracle gap. $\alpha$: signal alignment. Bound: $(1{-}D) \cdot G_{\text{nd}} \cdot \alpha$. Ratio: actual$/$weak bound.}
sections/appendix.tex:1257:\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\pm}\sigma$). $\alpha_{\textup{crit}} = F_1^{\textup{gr}}/2$; $\alpha_{\textup{crit,eff}} = \alpha_{\textup{crit}} / (1{-}\delta)$. When $\alpha_{\textup{crit,eff}} > 1$, MV gain is structurally impossible.}
sections/appendix.tex:1284:\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
sections/appendix.tex:1361:\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\,/\,constrained within-instance LP std. Arrows: constrained $\to$ free-form.}
sections/appendix.tex:1402:\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
sections/appendix.tex:1428:\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
sections/appendix.tex:1452:\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
sections/appendix.tex:1472:\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
sections/appendix.tex:1510:\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
sections/appendix.tex:1537:\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\Delta$: selection gain vs.\ greedy. CI: 95\% bootstrap percentile interval. $p_{\text{greedy}}$: one-sided $p$-value vs.\ greedy; $p_{\text{rand}}$: permutation test vs.\ random selection.}
sections/appendix.tex:1573:\caption{Inverse scaling rate by degeneracy status. An $N{\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}
sections/appendix.tex:1599:\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
sections/appendix.tex:1635:\caption{Scale ablation: Qwen3 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
sections/appendix.tex:1662:\caption{Pretrained vs.\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\text{MV}\,\Delta / \text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\pm}\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}
sections/appendix.tex:1701:\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}
sections/appendix.tex:1733:\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}
sections/appendix.tex:1774:\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
sections/appendix.tex:1807:\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}
sections/appendix.tex:1830:\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
sections/appendix.tex:1871:\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
sections/appendix.tex:1908:\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
sections/appendix.tex:1939:\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
sections/appendix.tex:1975:\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
sections/appendix.tex:1998:\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\%).}
sections/appendix.tex:2015:\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}
sections/appendix.tex:2049:[Omitted long matching line]
sections/appendix.tex:2083:\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\Delta$'': MV gain on non-degenerate instances only. LP $\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\ref{tab:fewnerd}.}
sections/appendix.tex:2114:[Omitted long matching line]
sections/appendix.tex:2160:\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\% confidence interval.}
sections/appendix.tex:2186:\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\alpha{=}0.05$). At this sample size, only large correlations ($\rho{\geq}0.5$) are detectable with adequate power.}
sections/appendix.tex:2213:\caption{Full-sequence vs.\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}
sections/appendix.tex:2238:\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \in \{2, \ldots, 8\}$. ``$\Delta$'': merge F1 minus greedy. ``Recovery'': $\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}
sections/appendix.tex:2260:\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. $^\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\text{adj}}{=}0.055$ (Appendix~\ref{app:holm}). $^\ddagger$LP-weighted not computed.}
sections/appendix.tex:2284:\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\Delta$: F1 difference vs.\ greedy in percentage points. Best $\Delta$ per dataset--weighting pair in \textbf{bold}.}
sections/appendix.tex:2346:\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$, 3-seed mean). $\Delta$: F1 difference vs.\ greedy in pp. Main-text construction results (Table~\ref{tab:entity_construction}) use Qwen3-8B.}
sections/appendix.tex:2366:\caption{Full zero-shot vs.\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}
sections/appendix.tex:2419:\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\Delta$F1 reports the primary result (dataset in parentheses).}
sections/appendix.tex:2448:\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}
sections/introduction.tex:19:[Omitted long matching line]
sections/experiments_main.tex:19:\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
sections/experiments_main.tex:29:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
sections/experiments_main.tex:61:\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}
sections/experiments_main.tex:86:\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c68e4c5e-c0e1-4f4a-aef9-bec9c5c8a54f",
  "tool_use_result": {
    "stdout": "sections/theory.tex:18:\\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \\cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\\S\\ref{sec:selection_gap}) limits how much is actually recoverable.}\nsections/theory.tex:43:\\caption{SC gain vs.\\ degeneracy across 16 configurations (SciERC-specific $\\alpha$). Red: signal-adjusted bound ($\\alpha{=}0.068$); vertical dashed: $\\theta_{\\text{crit}}{=}0.70$; horizontal dotted: $\\varepsilon{=}0.3$\\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}\nsections/single_signal.tex:12:\\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\\pm}\\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\\dagger$One score per input.}\nsections/single_signal.tex:35:\\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\\rho$; line: $\\Delta$F1 vs.\\ greedy (3-seed mean). Despite $\\rho$ up to 0.38, no signal outperforms greedy (all $p{\\geq}0.29$). Dashed green: oracle headroom ($+13.0$\\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}\nsections/adaptive.tex:9:\\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\\ref{sec:mechanistic} and adaptive methods in this section). $\\Delta$F1 vs.\\ greedy; dataset in parentheses. Full coverage in Appendix~\\ref{app:method_coverage}.}\nsections/background.tex:21:\\caption{Novelty comparison with closest related work along six dimensions.}\nsections/appendix.tex:25:\\caption{Notation used throughout the paper.}\nsections/appendix.tex:37:\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\nsections/appendix.tex:70:\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\nsections/appendix.tex:102:\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\nsections/appendix.tex:127:\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\nsections/appendix.tex:139:\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\nsections/appendix.tex:164:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\nsections/appendix.tex:183:\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\nsections/appendix.tex:213:\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:280:\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\nsections/appendix.tex:326:\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\nsections/appendix.tex:420:\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\nsections/appendix.tex:450:\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\nsections/appendix.tex:480:\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\nsections/appendix.tex:557:\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}\nsections/appendix.tex:588:\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\nsections/appendix.tex:643:\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\nsections/appendix.tex:688:\\caption{Entity-level self-verification: ESJ vs.\\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}\nsections/appendix.tex:711:\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over seeds.}\nsections/appendix.tex:740:\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\nsections/appendix.tex:818:\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\nsections/appendix.tex:825:\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\nsections/appendix.tex:852:\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\nsections/appendix.tex:878:\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\nsections/appendix.tex:901:\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\nsections/appendix.tex:927:\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}\nsections/appendix.tex:950:\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\nsections/appendix.tex:969:\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\nsections/appendix.tex:1004:\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\nsections/appendix.tex:1072:\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\nsections/appendix.tex:1101:\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\nsections/appendix.tex:1196:\\caption{Bound verification across representative configurations ($N{=}8$). $G_{\\text{nd}}$: non-degenerate oracle gap. $\\alpha$: signal alignment. Bound: $(1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$. Ratio: actual$/$weak bound.}\nsections/appendix.tex:1257:\\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$). $\\alpha_{\\textup{crit}} = F_1^{\\textup{gr}}/2$; $\\alpha_{\\textup{crit,eff}} = \\alpha_{\\textup{crit}} / (1{-}\\delta)$. When $\\alpha_{\\textup{crit,eff}} > 1$, MV gain is structurally impossible.}\nsections/appendix.tex:1284:\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\nsections/appendix.tex:1361:\\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\\,/\\,constrained within-instance LP std. Arrows: constrained $\\to$ free-form.}\nsections/appendix.tex:1402:\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\nsections/appendix.tex:1428:\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\nsections/appendix.tex:1452:\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\nsections/appendix.tex:1472:\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\nsections/appendix.tex:1510:\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\nsections/appendix.tex:1537:\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\nsections/appendix.tex:1573:\\caption{Inverse scaling rate by degeneracy status. An $N{\\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1635:\\caption{Scale ablation: Qwen3 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\nsections/appendix.tex:1662:\\caption{Pretrained vs.\\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\\text{MV}\\,\\Delta / \\text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\\pm}\\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}\nsections/appendix.tex:1701:\\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}\nsections/appendix.tex:1733:\\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}\nsections/appendix.tex:1774:\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\nsections/appendix.tex:1807:\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\nsections/appendix.tex:1830:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\nsections/appendix.tex:1871:\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\nsections/appendix.tex:1908:\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\nsections/appendix.tex:1939:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:1975:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\nsections/appendix.tex:1998:\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\nsections/appendix.tex:2015:\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\nsections/appendix.tex:2049:[Omitted long matching line]\nsections/appendix.tex:2083:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\nsections/appendix.tex:2114:[Omitted long matching line]\nsections/appendix.tex:2160:\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:2186:\\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\\alpha{=}0.05$). At this sample size, only large correlations ($\\rho{\\geq}0.5$) are detectable with adequate power.}\nsections/appendix.tex:2213:\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\nsections/appendix.tex:2238:\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\nsections/appendix.tex:2260:\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. $^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}\nsections/appendix.tex:2284:\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\nsections/appendix.tex:2346:\\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\\theta{=}2/N$, 3-seed mean). $\\Delta$: F1 difference vs.\\ greedy in pp. Main-text construction results (Table~\\ref{tab:entity_construction}) use Qwen3-8B.}\nsections/appendix.tex:2366:\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\nsections/appendix.tex:2419:\\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\\Delta$F1 reports the primary result (dataset in parentheses).}\nsections/appendix.tex:2448:\\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}\nsections/introduction.tex:19:[Omitted long matching line]\nsections/experiments_main.tex:19:\\caption{MV $\\Delta$F1 vs.\\ $\\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\\,pp at $N{=}64$).}\nsections/experiments_main.tex:29:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\nsections/experiments_main.tex:61:\\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}\nsections/experiments_main.tex:86:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}",
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

_source line 112_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d2a13b00-4388-4dbe-a3cf-9c0d643a209a",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VpcGWnKLwPpKnKxe34CUN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10844,
      "cache_read_input_tokens": 80005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10844
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

### Tool call

_source line 113_

<details open><summary>🔧 Tool call — Bash · `toolu_01HpJXWZ7YytyrMwfNJL5U6V`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/56622092-b880-43f3-8cd7-2a5161528236/tool-results/toolu_019eS8e29prb7umxvB6Pr2Yj.txt | grep -v \"_archived\" | tail -100",
  "description": "Continue reading captions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d0ddae77-e4e1-4e75-bafe-8e51eb655ca0",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01VpcGWnKLwPpKnKxe34CUN5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10844,
      "cache_read_input_tokens": 80005,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10844
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

_source line 114 · 2026-05-24T01:38:39.125Z_

<details><summary>↩ Tool result · `toolu_01HpJXWZ7YytyrMwfNJL5U6V`</summary>

```text
sections/theory.tex:18:\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\S\ref{sec:selection_gap}) limits how much is actually recoverable.}
sections/theory.tex:43:\caption{SC gain vs.\ degeneracy across 16 configurations (SciERC-specific $\alpha$). Red: signal-adjusted bound ($\alpha{=}0.068$); vertical dashed: $\theta_{\text{crit}}{=}0.70$; horizontal dotted: $\varepsilon{=}0.3$\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}
sections/single_signal.tex:12:\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\pm}\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\dagger$One score per input.}
sections/single_signal.tex:35:\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up to 0.38, no signal outperforms greedy (all $p{\geq}0.29$). Dashed green: oracle headroom ($+13.0$\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}
sections/adaptive.tex:9:\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\ref{sec:mechanistic} and adaptive methods in this section). $\Delta$F1 vs.\ greedy; dataset in parentheses. Full coverage in Appendix~\ref{app:method_coverage}.}
sections/background.tex:21:\caption{Novelty comparison with closest related work along six dimensions.}
sections/appendix.tex:25:\caption{Notation used throughout the paper.}
sections/appendix.tex:37:\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\sigma$ computed as sample standard deviation.}
sections/appendix.tex:70:\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\Delta\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}
sections/appendix.tex:102:\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}
sections/appendix.tex:127:\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}
sections/appendix.tex:139:\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
sections/appendix.tex:164:\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
sections/appendix.tex:183:\caption{SJ normalizer comparison (Spearman $\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\max(|g_i|,|g_j|)$; Union: $|g_i \cup g_j|$.}
sections/appendix.tex:213:\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\rho$ reflects binary success prediction; conditional $\rho$ measures quality gradation. LP's conditional $\rho$ is highest despite negative full-set $\rho$.}
sections/appendix.tex:239:\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
sections/appendix.tex:280:\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
sections/appendix.tex:326:\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\dagger$Survives correction at $\alpha{=}0.05$.}
sections/appendix.tex:420:\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
sections/appendix.tex:450:\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}
sections/appendix.tex:480:\caption{TOST equivalence testing: signals vs.\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ single-sample).}
sections/appendix.tex:557:\caption{Hidden state probes vs.\ LP for sample selection (5-fold CV ${\times}$ 3 seeds). $\rho$: Spearman correlation with per-sample F1. Sel.\ F1: selection F1. Gap\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}
sections/appendix.tex:588:\caption{Experimental coverage of entity-level methods. \checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}
sections/appendix.tex:643:\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}
sections/appendix.tex:688:\caption{Entity-level self-verification: ESJ vs.\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}
sections/appendix.tex:711:\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$). $\sigma$ is population standard deviation over seeds.}
sections/appendix.tex:740:\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
sections/appendix.tex:818:\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}
sections/appendix.tex:825:\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
sections/appendix.tex:852:\caption{$\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\%'' = fraction with within-instance LP range ${<}\varepsilon$. $\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\varepsilon{=}0.05$ yields the strongest statistical separation.}
sections/appendix.tex:878:\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
sections/appendix.tex:901:\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\varepsilon{=}0.05$. Within-instance $\rho$ and selection gain both concentrate in the non-tied subset. Full $\varepsilon$ sweep in Table~\ref{tab:epsilon_sweep}.}
sections/appendix.tex:927:\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\text{valid}}$: ${\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}
sections/appendix.tex:950:\caption{$\varepsilon$ threshold vs.\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\%: instances with LP range ${<}\varepsilon$. $\rho$: Spearman correlation between LP and oracle F1. $\varepsilon{=}0.05$ (bold) is the elbow.}
sections/appendix.tex:969:\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\geq}0.05$ show $3$--$6{\times}$ larger advantage.}
sections/appendix.tex:1004:\caption{Selection $\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}
sections/appendix.tex:1072:\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
sections/appendix.tex:1101:\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\pm}\sigma$, $n{=}551$). Fisher combined $p$ vs.\ greedy. LP is the only signal with positive $\Delta$. $\sigma$ is population standard deviation over 3 seeds.}
sections/appendix.tex:1196:\caption{Bound verification across representative configurations ($N{=}8$). $G_{\text{nd}}$: non-degenerate oracle gap. $\alpha$: signal alignment. Bound: $(1{-}D) \cdot G_{\text{nd}} \cdot \alpha$. Ratio: actual$/$weak bound.}
sections/appendix.tex:1257:\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\pm}\sigma$). $\alpha_{\textup{crit}} = F_1^{\textup{gr}}/2$; $\alpha_{\textup{crit,eff}} = \alpha_{\textup{crit}} / (1{-}\delta)$. When $\alpha_{\textup{crit,eff}} > 1$, MV gain is structurally impossible.}
sections/appendix.tex:1284:\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\pm}0.12$~pp).}
sections/appendix.tex:1361:\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\,/\,constrained within-instance LP std. Arrows: constrained $\to$ free-form.}
sections/appendix.tex:1402:\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}
sections/appendix.tex:1428:\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\rho$).}
sections/appendix.tex:1452:\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}
sections/appendix.tex:1472:\caption{Cross-seed standard deviation ($\sigma$) of Spearman $\rho$ at $N\!=\!8$ vs.\ $N\!=\!16$ (Qwen3-8B, SciERC, 3 seeds). $\sigma$ is population standard deviation.}
sections/appendix.tex:1510:\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\_025).\protect\footnotemark\ ``Best $\Delta$'': highest selection gain across all 5 signals. Per-signal $\Delta$ in pp vs.~greedy.}
sections/appendix.tex:1537:\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\Delta$: selection gain vs.\ greedy. CI: 95\% bootstrap percentile interval. $p_{\text{greedy}}$: one-sided $p$-value vs.\ greedy; $p_{\text{rand}}$: permutation test vs.\ random selection.}
sections/appendix.tex:1573:\caption{Inverse scaling rate by degeneracy status. An $N{\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}
sections/appendix.tex:1599:\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
sections/appendix.tex:1635:\caption{Scale ablation: Qwen3 8B vs.\ 4B QE $\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\ref{app:re_extension}.}
sections/appendix.tex:1662:\caption{Pretrained vs.\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\text{MV}\,\Delta / \text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\pm}\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}
sections/appendix.tex:1701:\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}
sections/appendix.tex:1733:\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}
sections/appendix.tex:1774:\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\rho$ across four temperatures. $\kappa$: Fleiss' $\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}
sections/appendix.tex:1807:\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}
sections/appendix.tex:1830:\caption{Cross-dataset OOD quality estimation (Spearman $\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\rho$ from Table~\ref{tab:quality_estimation} (same model, same seed). \textsuperscript{***}$p{<}0.001$, \textsuperscript{*}$p{<}0.05$.}
sections/appendix.tex:1871:\caption{Verbalized confidence (VerbConf) vs.\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}
sections/appendix.tex:1908:\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}
sections/appendix.tex:1939:\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\ $\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\% confidence interval.}
sections/appendix.tex:1975:\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\Delta$; Art (highest degeneracy) is the sole exception.}
sections/appendix.tex:1998:\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\%).}
sections/appendix.tex:2015:\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}
sections/appendix.tex:2049:[Omitted long matching line]
sections/appendix.tex:2083:\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\Delta$'': MV gain on non-degenerate instances only. LP $\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\ref{tab:fewnerd}.}
sections/appendix.tex:2114:[Omitted long matching line]
sections/appendix.tex:2160:\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\% confidence interval.}
sections/appendix.tex:2186:\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\alpha{=}0.05$). At this sample size, only large correlations ($\rho{\geq}0.5$) are detectable with adequate power.}
sections/appendix.tex:2213:\caption{Full-sequence vs.\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}
sections/appendix.tex:2238:\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \in \{2, \ldots, 8\}$. ``$\Delta$'': merge F1 minus greedy. ``Recovery'': $\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}
sections/appendix.tex:2260:\caption{Entity construction vs.\ greedy ($\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\pm}\sigma$). $\theta{=}2/N$. $p$: paired bootstrap vs.\ greedy. $^\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\text{adj}}{=}0.055$ (Appendix~\ref{app:holm}). $^\ddagger$LP-weighted not computed.}
sections/appendix.tex:2284:\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\Delta$: F1 difference vs.\ greedy in percentage points. Best $\Delta$ per dataset--weighting pair in \textbf{bold}.}
sections/appendix.tex:2346:\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\theta{=}2/N$, 3-seed mean). $\Delta$: F1 difference vs.\ greedy in pp. Main-text construction results (Table~\ref{tab:entity_construction}) use Qwen3-8B.}
sections/appendix.tex:2366:\caption{Full zero-shot vs.\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}
sections/appendix.tex:2419:\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\Delta$F1 reports the primary result (dataset in parentheses).}
sections/appendix.tex:2448:\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}
sections/introduction.tex:19:[Omitted long matching line]
sections/experiments_main.tex:19:\caption{MV $\Delta$F1 vs.\ $\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\,pp at $N{=}64$).}
sections/experiments_main.tex:29:\caption{NER quality estimation ($\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\sigma{\leq}0.026$ in Table~\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \textbf{bold}. RE in Appendix~\ref{app:re_extension}; $N{=}16$ in Table~\ref{tab:robustness}.}
sections/experiments_main.tex:61:\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}
sections/experiments_main.tex:86:\caption{Instance degeneracy vs.\ LP selection gain across 23 configurations ($N{=}8$; $\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\rho{=}{-}0.881$; Appendix~\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "aabcd735-1f2f-437c-9574-5fee3c82b1f1",
  "tool_use_result": {
    "stdout": "sections/theory.tex:18:\\caption{Oracle $F_1$ as a function of sample count $N$, fitted with $F_1(N) = a - b \\cdot N^{-c}$. All fits $R^2 > 0.999$. Horizontal dashed lines: greedy ($T{=}0$) F1. The ceiling grows monotonically with $N$, but the correlation-selection gap (\\S\\ref{sec:selection_gap}) limits how much is actually recoverable.}\nsections/theory.tex:43:\\caption{SC gain vs.\\ degeneracy across 16 configurations (SciERC-specific $\\alpha$). Red: signal-adjusted bound ($\\alpha{=}0.068$); vertical dashed: $\\theta_{\\text{crit}}{=}0.70$; horizontal dotted: $\\varepsilon{=}0.3$\\,pp. All positive gains fall within the bound (right panel: ratio to weak bound, all ${<}0.13$).}\nsections/single_signal.tex:12:\\caption{Best-of-$N$ selection (macro F1) on SciERC ($N{=}8$, $T{=}1.0$). Selection signals: 2-seed mean${\\pm}\\sigma$; baselines: 3-seed (Oracle${=}0.775$, Greedy${=}0.645$). LP is per-sample; others use consensus-proximity. $^\\dagger$One score per input.}\nsections/single_signal.tex:35:\\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\\rho$; line: $\\Delta$F1 vs.\\ greedy (3-seed mean). Despite $\\rho$ up to 0.38, no signal outperforms greedy (all $p{\\geq}0.29$). Dashed green: oracle headroom ($+13.0$\\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}\nsections/adaptive.tex:9:\\caption{Summary of 9 method categories tested (including MV baseline, LP selection, and cross-model ensemble beyond self-verification methods in Appendix~\\ref{sec:mechanistic} and adaptive methods in this section). $\\Delta$F1 vs.\\ greedy; dataset in parentheses. Full coverage in Appendix~\\ref{app:method_coverage}.}\nsections/background.tex:21:\\caption{Novelty comparison with closest related work along six dimensions.}\nsections/appendix.tex:25:\\caption{Notation used throughout the paper.}\nsections/appendix.tex:37:\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.013$; individual: 0.398, 0.423, 0.410). $\\sigma$ computed as sample standard deviation.}\nsections/appendix.tex:70:\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP shows the largest NER temperature effect ($\\Delta\\rho{=}{+}0.044$); RE $T{=}0.7$ LP data unavailable.}\nsections/appendix.tex:102:\\caption{Instance-level FK independence test. Permutation tests confirm FK reflects true within-instance agreement (all $p{<}0.001$). Split-half reliability $r$ computed by randomly partitioning $N$ samples into two halves and correlating their FK scores.}\nsections/appendix.tex:127:\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), RE calibration remains challenging for compound extraction tasks.}\nsections/appendix.tex:139:\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC NER while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\nsections/appendix.tex:164:\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\nsections/appendix.tex:183:\\caption{SJ normalizer comparison (Spearman $\\rho$; $N{=}8$, $T{=}1.0$, seed${=}42$). Max: $\\max(|g_i|,|g_j|)$; Union: $|g_i \\cup g_j|$.}\nsections/appendix.tex:213:\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}16$, $T{=}1.0$, $n{=}689$). Cond: non-zero F1 instances ($n{=}334$). Full-set $\\rho$ reflects binary success prediction; conditional $\\rho$ measures quality gradation. LP's conditional $\\rho$ is highest despite negative full-set $\\rho$.}\nsections/appendix.tex:239:\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\nsections/appendix.tex:280:\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\nsections/appendix.tex:326:\\caption{Complete enumeration of $k{=}57$ statistical tests subject to Holm--Bonferroni correction. Raw $p$: uncorrected $p$-value as reported. $p_{\\text{adj}}$: Holm--Bonferroni adjusted $p$-value. $^\\dagger$Survives correction at $\\alpha{=}0.05$.}\nsections/appendix.tex:420:\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\nsections/appendix.tex:450:\\caption{Instance degeneracy statistics ($T{=}1.0$). ``Constant F1'': all $N$ samples receive identical instance-level F1. ``Constant utility'': MBR (SJ) utility identical across candidates. 4B data confirms degeneracy scales with model capability.}\nsections/appendix.tex:480:\\caption{TOST equivalence testing: signals vs.\\ single-sample on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ single-sample).}\nsections/appendix.tex:557:\\caption{Hidden state probes vs.\\ LP for sample selection (5-fold CV ${\\times}$ 3 seeds). $\\rho$: Spearman correlation with per-sample F1. Sel.\\ F1: selection F1. Gap\\%: oracle gap closure. SciERC greedy${=}0.644$ (seed 42), oracle${=}0.775$ (seed 42).}\nsections/appendix.tex:588:\\caption{Experimental coverage of entity-level methods. \\checkmark = tested; --- = not tested. All methods use $N{=}8$, $T{=}1.0$ unless noted. Section references indicate where results appear.}\nsections/appendix.tex:643:\\caption{Entity-level self-verification probes (Qwen2.5-7B, Few-NERD, $N{=}8$). ESJ: entity self-judgment via yes/no prompts. MRSC: multi-round re-prompting on disputed entities. LSC: latent-space centroid selection. MV: majority vote baseline.}\nsections/appendix.tex:688:\\caption{Entity-level self-verification: ESJ vs.\\ agreement-based signals across datasets (Qwen3-8B, $N{=}8$). ESJ AUROC is indistinguishable from chance on all datasets.}\nsections/appendix.tex:711:\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$; Qwen: 5 seeds (42, 123, 456, 2024, 3141); LLaMA: 3 seeds (42, 123, 456)). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$). $\\sigma$ is population standard deviation over seeds.}\nsections/appendix.tex:740:\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\nsections/appendix.tex:818:\\caption{CDF of within-instance LP range on SciERC NER ($N{=}8$, $n{=}529$). The median LP range is 0.041 nats (dashed line), below $\\varepsilon{=}0.05$. The smooth CDF confirms compression is pervasive, not bimodal.}\nsections/appendix.tex:825:\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\nsections/appendix.tex:852:\\caption{$\\varepsilon$ sensitivity sweep for LP selection on SciERC NER ($N{=}8$, seed${=}42$, $n{=}529$). ``Tied\\%'' = fraction with within-instance LP range ${<}\\varepsilon$. $\\Delta$: selection F1 gain over single-sample on the non-tied subset. The tied fraction increases smoothly; $\\varepsilon{=}0.05$ yields the strongest statistical separation.}\nsections/appendix.tex:878:\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\nsections/appendix.tex:901:\\caption{Non-tied subset analysis (SciERC, Qwen3-8B, $N{=}8$, $T{=}1.0$). Instances split at LP range $\\varepsilon{=}0.05$. Within-instance $\\rho$ and selection gain both concentrate in the non-tied subset. Full $\\varepsilon$ sweep in Table~\\ref{tab:epsilon_sweep}.}\nsections/appendix.tex:927:\\caption{Within-instance LP-quality alignment across datasets ($N{=}8$, $T{=}1.0$). $\\rho$: median Spearman correlation between LP and F1 within each instance, over non-degenerate instances ($n_{\\text{valid}}$: ${\\geq}2$ distinct F1 values). Counts are from the primary seed (seed 42); text references use 3-seed mean degeneracy rates.}\nsections/appendix.tex:950:\\caption{$\\varepsilon$ threshold vs.\\ LP compression on Few-NERD ($N{=}8$, seed${=}42$). Compressed\\%: instances with LP range ${<}\\varepsilon$. $\\rho$: Spearman correlation between LP and oracle F1. $\\varepsilon{=}0.05$ (bold) is the elbow.}\nsections/appendix.tex:969:\\caption{LP-best selection advantage over MV by LP range bucket on Few-NERD ($N{=}8$, seed${=}42$). Instances with LP range ${\\geq}0.05$ show $3$--$6{\\times}$ larger advantage.}\nsections/appendix.tex:1004:\\caption{Selection $\\Delta$ (pp over single-sample) stratified by VC quartile on SciERC ($N{=}8$, Qwen3-8B). Oracle headroom collapses at Q4; LP rankings are unreliable at Q1--Q2. Neither quartile supports consistent selection gains.}\nsections/appendix.tex:1072:\\caption{RE selection F1 (macro, instance-averaged) on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\nsections/appendix.tex:1101:\\caption{RE best-of-$N$ selection F1 (macro, instance-averaged) on SciERC (Qwen3-4B, $N{=}16$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$, $n{=}551$). Fisher combined $p$ vs.\\ greedy. LP is the only signal with positive $\\Delta$. $\\sigma$ is population standard deviation over 3 seeds.}\nsections/appendix.tex:1196:\\caption{Bound verification across representative configurations ($N{=}8$). $G_{\\text{nd}}$: non-degenerate oracle gap. $\\alpha$: signal alignment. Bound: $(1{-}D) \\cdot G_{\\text{nd}} \\cdot \\alpha$. Ratio: actual$/$weak bound.}\nsections/appendix.tex:1257:\\caption{MV performance under strict majority (count $> N/2$; Qwen3-8B FT, $N{=}8$, $T{=}1.0$, 3-seed mean${\\pm}\\sigma$). $\\alpha_{\\textup{crit}} = F_1^{\\textup{gr}}/2$; $\\alpha_{\\textup{crit,eff}} = \\alpha_{\\textup{crit}} / (1{-}\\delta)$. When $\\alpha_{\\textup{crit,eff}} > 1$, MV gain is structurally impossible.}\nsections/appendix.tex:1284:\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$; RE selection gap replicates across 4 seeds: $+1.84{\\pm}0.12$~pp).}\nsections/appendix.tex:1361:\\caption{Cross-dataset free-form decoding summary (Qwen3-8B, $N{=}8$, $T{=}1.0$). LP std ratio = free-form\\,/\\,constrained within-instance LP std. Arrows: constrained $\\to$ free-form.}\nsections/appendix.tex:1402:\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high single-sample F1.}\nsections/appendix.tex:1428:\\caption{Effect of sample pool size on signal quality (Qwen3-8B, SciERC, 3-seed mean Spearman $\\rho$).}\nsections/appendix.tex:1452:\\caption{Cross-seed signal ranking stability (Kendall's $W$, 3 seeds).}\nsections/appendix.tex:1472:\\caption{Cross-seed standard deviation ($\\sigma$) of Spearman $\\rho$ at $N\\!=\\!8$ vs.\\ $N\\!=\\!16$ (Qwen3-8B, SciERC, 3 seeds). $\\sigma$ is population standard deviation.}\nsections/appendix.tex:1510:\\caption{Effect of sample count on selection (SciERC NER, Qwen3-8B, $T{=}1.0$, gold-filtered, seed${=}42$; exp\\_025).\\protect\\footnotemark\\ ``Best $\\Delta$'': highest selection gain across all 5 signals. Per-signal $\\Delta$ in pp vs.~greedy.}\nsections/appendix.tex:1537:\\caption{Bootstrap significance test at $N{=}32$ (SciERC NER, Qwen3-8B, $T{=}1.0$, $B{=}10{,}000$, $n{=}529$ gold-non-empty instances; 22 instances with no gold entities are excluded as they contribute zero selection differential). $\\Delta$: selection gain vs.\\ greedy. CI: 95\\% bootstrap percentile interval. $p_{\\text{greedy}}$: one-sided $p$-value vs.\\ greedy; $p_{\\text{rand}}$: permutation test vs.\\ random selection.}\nsections/appendix.tex:1573:\\caption{Inverse scaling rate by degeneracy status. An $N{\\to}N'$ transition is ``inverse'' if MV F1 at $N'$ is strictly lower than at $N$. OR: odds ratio (Fisher's exact test).}\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1635:\\caption{Scale ablation: Qwen3 8B vs.\\ 4B QE $\\rho$ ($N{=}8$, $T{=}1.0$, seed 42). RE in Appendix~\\ref{app:re_extension}.}\nsections/appendix.tex:1662:\\caption{Pretrained vs.\\ finetuned MV ($T{=}1.0$). Pretrained: Qwen2.5-7B-Instruct; finetuned: Qwen3-8B LoRA ($N{=}8$ unless noted). MV: strict majority ($>N/2$). Capture: $\\text{MV}\\,\\Delta / \\text{oracle headroom}$. CoNLL pretrained single-seed; others 3-seed mean${\\pm}\\sigma$ ($N{=}8$) or single-seed ($N{=}16{,}32$).}\nsections/appendix.tex:1701:\\caption{Per-entity-type MV gain on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, 3-seed mean). Strict MV ($\\theta{>}N/2$). Types sorted by finetuned greedy F1. 7/8 types flip MV direction between pretrained and finetuned.}\nsections/appendix.tex:1733:\\caption{Cross-family frontier SC on Few-NERD ($N{=}8$, $T{=}1.0$, 200 instances, zero-shot). Parse failures excluded from all metrics; $N_{\\textit{eff}}$: mean effective samples after exclusion. Selection gap $= $ oracle $-$ MV. Text-based entity matching (Appendix~\\ref{app:frontier_sc}, entity matching paragraph). Qwen3-8B FT shown for reference.}\nsections/appendix.tex:1774:\\caption{Temperature ablation on SciERC NER (Qwen3-8B, $N{=}8$, seed${=}42$). Oracle gap and QE $\\rho$ across four temperatures. $\\kappa$: Fleiss' $\\kappa$ (inter-sample agreement). $T{=}0.5$ and $T{=}1.0$ use joint (NER+RE) subtask; $T{=}0.8$ and $T{=}1.2$ use NER-only.}\nsections/appendix.tex:1807:\\caption{Temperature sensitivity of degeneracy and LP spread (SciERC NER, Qwen3-8B, $N{=}8$). Degeneracy: constant-F1, gold-filtered. LP range: median within-instance range.}\nsections/appendix.tex:1830:\\caption{Cross-dataset OOD quality estimation (Spearman $\\rho$, Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). SciERC$\\to$CoNLL: SciERC-trained model on CoNLL instances ($n{=}2756$). CoNLL$\\to$SciERC: CoNLL-trained model on SciERC instances ($n{=}529$, excluded from conclusions due to catastrophic model failure). In-domain $\\rho$ from Table~\\ref{tab:quality_estimation} (same model, same seed). \\textsuperscript{***}$p{<}0.001$, \\textsuperscript{*}$p{<}0.05$.}\nsections/appendix.tex:1871:\\caption{Verbalized confidence (VerbConf) vs.\\ log-probability selection (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed${=}42$). Parse fail: fraction of samples where the confidence score could not be extracted.}\nsections/appendix.tex:1908:\\caption{LLaMA-3.2-3B SciERC NER quality estimation and selection ($N{=}8$, $T{=}1.0$, seed${=}42$). Greedy F1${=}0.627$, Oracle F1${=}0.763$, headroom${=}13.63$~pp.}\nsections/appendix.tex:1939:\\caption{Few-NERD INTRA coarse: complete quality estimation and selection results (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$). $\\rho$: Spearman correlation with instance F1. Sample AUROC: per-sample LP discrimination. Sel.\\ $\\Delta$: selection F1 minus greedy (0.748). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:1975:\\caption{Per-entity-type LP selection on Few-NERD INTRA coarse (Qwen3-8B, $N{=}8$, $T{=}1.0$), sorted by degeneracy. LP $\\Delta$: LP selection F1 minus greedy. 7/8 types show positive $\\Delta$; Art (highest degeneracy) is the sole exception.}\nsections/appendix.tex:1998:\\caption{CoNLL-2003 per-type LP selection (Qwen3-8B, $N{=}16$, $T{=}1.0$). All types exceed 20\\% degeneracy and show negative LP selection, consistent with the dataset's ceiling-regime performance (F1 $>$ 90\\%).}\nsections/appendix.tex:2015:\\caption{SciERC per-type LP selection (Qwen3-8B, $N{=}8$, $T{=}1.0$). Within-dataset, degeneracy alone does not predict LP effectiveness (Spearman $\\rho{=}0.14$, $p{=}0.79$); additional type-specific factors likely modulate selection at this granularity.}\nsections/appendix.tex:2049:[Omitted long matching line]\nsections/appendix.tex:2083:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\nsections/appendix.tex:2114:[Omitted long matching line]\nsections/appendix.tex:2160:\\caption{LP selection on the favorable subset (non-degenerate instances with LP range above the dataset-specific median) per dataset (Qwen3-8B, $N{=}8$, $T{=}1.0$). CI: bootstrap 95\\% confidence interval.}\nsections/appendix.tex:2186:\\caption{Post-hoc power analysis ($n{=}23$, two-tailed, $\\alpha{=}0.05$). At this sample size, only large correlations ($\\rho{\\geq}0.5$) are detectable with adequate power.}\nsections/appendix.tex:2213:\\caption{Full-sequence vs.\\ entity-token LP on SciERC NER (Qwen3-8B, $N{=}8$, $T{=}1.0$). Entity-token LP has higher variance and stronger correlation, yet selection degrades.}\nsections/appendix.tex:2238:\\caption{Entity-level majority voting results (Qwen3-8B, $N{=}8$, $T{=}1.0$). ``Greedy'': $T{=}0$ baseline. ``Best merge'': optimal $k$ per dataset from sweep $k \\in \\{2, \\ldots, 8\\}$. ``$\\Delta$'': merge F1 minus greedy. ``Recovery'': $\\Delta$ / (oracle $-$ greedy). Only SciERC shows positive recovery; even with oracle $k$, CoNLL and Few-NERD degrade.}\nsections/appendix.tex:2260:\\caption{Entity construction vs.\\ greedy ($\\Delta$ macro F1; $N{=}8$, $T{=}1.0$, Qwen3-8B, multi-seed mean${\\pm}\\sigma$). $\\theta{=}2/N$. $p$: paired bootstrap vs.\\ greedy. $^\\dagger$Survives per-family Holm--Bonferroni correction (construction, $k{=}10$); global correction ($k{=}57$) yields $p_{\\text{adj}}{=}0.055$ (Appendix~\\ref{app:holm}). $^\\ddagger$LP-weighted not computed.}\nsections/appendix.tex:2284:\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}\nsections/appendix.tex:2346:\\caption{Construction weighting variants (LLaMA-3.1-8B, $N{=}8$, $T{=}1.0$, $\\theta{=}2/N$, 3-seed mean). $\\Delta$: F1 difference vs.\\ greedy in pp. Main-text construction results (Table~\\ref{tab:entity_construction}) use Qwen3-8B.}\nsections/appendix.tex:2366:\\caption{Full zero-shot vs.\\ few-shot comparison for Qwen2.5-72B-Instruct-AWQ ($N{=}8$). Only SciERC under zero-shot yields a significant construction gain.}\nsections/appendix.tex:2419:\\caption{Cost-benefit summary of aggregation strategies (Qwen3-8B, $N{=}8$, $T{=}1.0$). Inference cost is relative to greedy ($T{=}0$, single forward pass). $\\Delta$F1 reports the primary result (dataset in parentheses).}\nsections/appendix.tex:2448:\\caption{Differentiation matrix: positioning relative to prior work on self-consistency limitations. ``Methods tested'' counts the number of distinct aggregation/selection categories evaluated (not hyperparameter variants).}\nsections/introduction.tex:19:[Omitted long matching line]\nsections/experiments_main.tex:19:\\caption{MV $\\Delta$F1 vs.\\ $\\log_2 N$ across three datasets (Qwen3-8B FT, seed${=}42$). Dotted gray: $\\Delta{=}0$. Gains are dataset-dependent: persistently negative on Few-NERD, near zero on SciERC at higher $N$, marginally positive on CoNLL ($+0.6$\\,pp at $N{=}64$).}\nsections/experiments_main.tex:29:\\caption{NER quality estimation ($\\rho$ and AUROC; $N{=}8$, primary seed${=}42$; 5-seed $\\sigma{\\leq}0.026$ in Table~\\ref{tab:multiseed}). AUROC binarizes at per-dataset median F1. Best in \\textbf{bold}. RE in Appendix~\\ref{app:re_extension}; $N{=}16$ in Table~\\ref{tab:robustness}.}\nsections/experiments_main.tex:61:\\caption{LP selection across datasets (instance-averaged F1; Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered, 3-seed means). $p$: paired bootstrap.}\nsections/experiments_main.tex:86:\\caption{Instance degeneracy vs.\\ LP selection gain across 23 configurations ($N{=}8$; $\\rho{=}0.052$, $p{=}0.81$). Within Few-NERD per-entity-type ($\\rho{=}{-}0.881$; Appendix~\\ref{app:per_type_lp}), degeneracy predicts LP gain when alignment is held constant.}",
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

_source line 115_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b9dc0b56-9379-4b6f-bc9c-99413778ce6d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DK2QSAJ1dqxoYjNT2NWe2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10991,
      "cache_read_input_tokens": 90849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10991
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

### Tool call

_source line 116_

<details open><summary>🔧 Tool call — Read · `toolu_01WW8XJLMrbys8sRF8bp3kic`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "offset": 15,
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "baf2ac05-6257-4a75-96fd-8e8db817c366",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01DK2QSAJ1dqxoYjNT2NWe2M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 10991,
      "cache_read_input_tokens": 90849,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 10991
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

### Tool result

_source line 117 · 2026-05-24T01:38:44.440Z_

<details><summary>↩ Tool result · `toolu_01WW8XJLMrbys8sRF8bp3kic`</summary>

```text
15	
16	\begin{figure*}[t]
17	\centering
18	\includegraphics[width=\textwidth]{fig_overview}
19	\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain). Representative values across datasets: AUROC from CoNLL EM; $\rho$ and entity-construction gain from Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; Tables~\ref{tab:quality_estimation},~\ref{tab:entity_construction}). \textbf{Left}: consistency signals estimate instance quality. \textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \textbf{Right}: LP-weighted entity construction ($\theta{=}2/N$) yields conditional gains ($+1.40$\,pp on Few-NERD; \S\ref{sec:prescriptive}).}
20	\label{fig:overview}
21	\end{figure*}
22	
23	Our investigation proceeds in three stages:
24	\begin{enumerate}[nosep]
25	\item \textbf{Discover} [\S\ref{sec:qe_results}].
26	QE signals achieve AUROC up to $0.82$; while \citet{yao2026consistency} report task-level correlation ($\rho$ up to 0.47), our instance-level decomposition reveals why correlation does not yield selection gains.
27	\item \textbf{Diagnose} [\S\ref{sec:selection_gap}, \S\ref{sec:adaptive}, \S\ref{sec:theory}].
28	A diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\alpha$, LP range). A necessary condition bound (\S\ref{sec:theory}) confirms $\alpha$ as the binding constraint (3--12\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\ ESJ $\approx 0.50$; Appendix~\ref{sec:mechanistic}).
29	\item \textbf{Construct (exploratory)} [\S\ref{sec:prescriptive}].
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "dbe40a3c-7b92-46e4-9d6c-48bd27029f3e",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain). Representative values across datasets: AUROC from CoNLL EM; $\\rho$ and entity-construction gain from Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; Tables~\\ref{tab:quality_estimation},~\\ref{tab:entity_construction}). \\textbf{Left}: consistency signals estimate instance quality. \\textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \\textbf{Right}: LP-weighted entity construction ($\\theta{=}2/N$) yields conditional gains ($+1.40$\\,pp on Few-NERD; \\S\\ref{sec:prescriptive}).}\n\\label{fig:overview}\n\\end{figure*}\n\nOur investigation proceeds in three stages:\n\\begin{enumerate}[nosep]\n\\item \\textbf{Discover} [\\S\\ref{sec:qe_results}].\nQE signals achieve AUROC up to $0.82$; while \\citet{yao2026consistency} report task-level correlation ($\\rho$ up to 0.47), our instance-level decomposition reveals why correlation does not yield selection gains.\n\\item \\textbf{Diagnose} [\\S\\ref{sec:selection_gap}, \\S\\ref{sec:adaptive}, \\S\\ref{sec:theory}].\nA diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \\citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\\alpha$, LP range). A necessary condition bound (\\S\\ref{sec:theory}) confirms $\\alpha$ as the binding constraint (3--12\\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\\ ESJ $\\approx 0.50$; Appendix~\\ref{sec:mechanistic}).\n\\item \\textbf{Construct (exploratory)} [\\S\\ref{sec:prescriptive}].",
      "numLines": 15,
      "startLine": 15,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Assistant

_source line 118_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c1405f0e-582f-4ef0-a946-5e1a649fe360",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014AvG8MRoxYwRqbcFnxYavy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 101840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Grep · `toolu_01DxmDCj2s3xfRzXaYWRrhCa`</summary>

```json
{
  "pattern": "percentage points|\\(pp\\)|percentage point",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections",
  "output_mode": "content",
  "-n": true,
  "glob": "*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "988d7889-767d-430b-b691-b8c213e889ca",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014AvG8MRoxYwRqbcFnxYavy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1034,
      "cache_read_input_tokens": 101840,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1034
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 120 · 2026-05-24T01:38:50.188Z_

<details><summary>↩ Tool result · `toolu_01DxmDCj2s3xfRzXaYWRrhCa`</summary>

```text
sections/_archived/experiments_OLD.tex:182:\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed.}
sections/appendix.tex:856:$\varepsilon$ & Tied\% & Non-tied $n$ & $\Delta$ (pp) & $p$ \\
sections/appendix.tex:878:\caption{Maximum selection F1 variation (pp) across $\varepsilon \in [0, 0.2]$. At $\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}
sections/appendix.tex:973:LP range & $n$ & MV F1 & LP$-$MV (pp) \\
sections/appendix.tex:1008:Quartile & Mean VC & LP $\Delta$ & SJ $\Delta$ & Oracle (pp) \\
sections/appendix.tex:1105:Method & F1 & $\Delta$ (pp) & $p$(Fisher) \\
sections/appendix.tex:1262:Dataset & Seeds & Greedy & MV & Oracle & $\Delta_{\textup{SC}}$ (pp) & $\delta$ & $\alpha_{\textup{crit}}$ & $\alpha_{\textup{crit,eff}}$ & Prediction \\
sections/appendix.tex:1369:MV $\Delta$ (pp) & ${-}3.3 {\to} {-}1.4$ & ${-}1.8 {\to} {-}2.1$ & ${-}9.6 {\to} {-}9.6$ \\
sections/appendix.tex:1515:$N$ & Degen.\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\Delta$ \\
sections/appendix.tex:1542:Signal & $\Delta$ (pp) & 95\% CI & $p_{\text{greedy}}$ & $p_{\text{rand}}$ \\
sections/appendix.tex:1599:\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}. $^\star$Qwen2.5; unmarked: Qwen3. $^\dagger$Not computed. $^\ddagger$200-instance subset; 10.1\% parse failures excluded.}
sections/appendix.tex:1667:Dataset & Setting & Greedy & MV $\Delta$ (pp) & Degen.\% & Capture & $\rho_{\textup{SJ}}$ \\
sections/appendix.tex:1705:& & & \multicolumn{2}{c}{MV $\Delta$ (pp)} \\
sections/appendix.tex:1779:$T$ & Oracle gap (pp) & SJ $\rho$ & LP $\rho$ & $\kappa$ & Sample F1 \\
sections/appendix.tex:1980:Entity Type & $n$ & Degen.\% & Greedy & LP Sel & $\Delta$ (pp) & LP $\rho$ & Headroom \\
sections/appendix.tex:2002:Entity Type & Degen.\% & LP $\Delta$ (pp) \\
sections/appendix.tex:2019:Entity Type & Degen.\% & LP $\Delta$ (pp) \\
sections/appendix.tex:2083:\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\Delta$'': MV gain on non-degenerate instances only. LP $\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\ref{tab:fewnerd}.}
sections/appendix.tex:2091:MV $\Delta$ (pp) & $-$2.74 & $-$0.40 \\
sections/appendix.tex:2094:LP $\Delta$ (pp) & $+$1.39 & $+$0.12${\pm}$0.04 \\
sections/appendix.tex:2095:Entity constr.\ $\Delta$ (pp) & $+$0.88 & $+$0.20 \\
sections/appendix.tex:2123:LP $\Delta$ (pp) & $-$1.24 & $+$0.64 & $+$1.02 \\
sections/appendix.tex:2165:Dataset & LP $\Delta$ (pp) & 95\% CI & Interpretation \\
sections/appendix.tex:2218:Aggregation & Med.\ var. & $\rho$ & AUROC & $\Delta$ (pp) \\
sections/appendix.tex:2243:Dataset & Greedy & Best merge ($k^*$) & $\Delta$ (pp) & Recovery (\%) \\
sections/appendix.tex:2284:\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\Delta$: F1 difference vs.\ greedy in percentage points. Best $\Delta$ per dataset--weighting pair in \textbf{bold}.}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "82961690-e2d4-499b-bfa8-a25117a3cf84",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "sections/_archived/experiments_OLD.tex:182:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed.}\nsections/appendix.tex:856:$\\varepsilon$ & Tied\\% & Non-tied $n$ & $\\Delta$ (pp) & $p$ \\\\\nsections/appendix.tex:878:\\caption{Maximum selection F1 variation (pp) across $\\varepsilon \\in [0, 0.2]$. At $\\varepsilon{=}0.05$ (used throughout), consistency signals change by ${\\leq}1.09$~pp; EM is invariant (integer scoring). LP is most sensitive as $\\varepsilon$ corresponds to its tied/non-tied partition. SciERC: $n{=}529$; CoNLL: $n{=}2{,}756$.}\nsections/appendix.tex:973:LP range & $n$ & MV F1 & LP$-$MV (pp) \\\\\nsections/appendix.tex:1008:Quartile & Mean VC & LP $\\Delta$ & SJ $\\Delta$ & Oracle (pp) \\\\\nsections/appendix.tex:1105:Method & F1 & $\\Delta$ (pp) & $p$(Fisher) \\\\\nsections/appendix.tex:1262:Dataset & Seeds & Greedy & MV & Oracle & $\\Delta_{\\textup{SC}}$ (pp) & $\\delta$ & $\\alpha_{\\textup{crit}}$ & $\\alpha_{\\textup{crit,eff}}$ & Prediction \\\\\nsections/appendix.tex:1369:MV $\\Delta$ (pp) & ${-}3.3 {\\to} {-}1.4$ & ${-}1.8 {\\to} {-}2.1$ & ${-}9.6 {\\to} {-}9.6$ \\\\\nsections/appendix.tex:1515:$N$ & Degen.\\% & Oracle (pp) & LP & SJ & FK & EM & VC & Best $\\Delta$ \\\\\nsections/appendix.tex:1542:Signal & $\\Delta$ (pp) & 95\\% CI & $p_{\\text{greedy}}$ & $p_{\\text{rand}}$ \\\\\nsections/appendix.tex:1599:\\caption{Cross-scale and cross-family comparison ($N{=}8$, $T{=}1.0$). Hdr.\\ = oracle $-$ greedy (pp). Degen.: instance degeneracy (\\%). F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\\ref{tab:fewnerd}. $^\\star$Qwen2.5; unmarked: Qwen3. $^\\dagger$Not computed. $^\\ddagger$200-instance subset; 10.1\\% parse failures excluded.}\nsections/appendix.tex:1667:Dataset & Setting & Greedy & MV $\\Delta$ (pp) & Degen.\\% & Capture & $\\rho_{\\textup{SJ}}$ \\\\\nsections/appendix.tex:1705:& & & \\multicolumn{2}{c}{MV $\\Delta$ (pp)} \\\\\nsections/appendix.tex:1779:$T$ & Oracle gap (pp) & SJ $\\rho$ & LP $\\rho$ & $\\kappa$ & Sample F1 \\\\\nsections/appendix.tex:1980:Entity Type & $n$ & Degen.\\% & Greedy & LP Sel & $\\Delta$ (pp) & LP $\\rho$ & Headroom \\\\\nsections/appendix.tex:2002:Entity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\nsections/appendix.tex:2019:Entity Type & Degen.\\% & LP $\\Delta$ (pp) \\\\\nsections/appendix.tex:2083:\\caption{Training convergence confound on Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$, gold-filtered $n{=}32{,}565$, 2-seed mean). ``Degen.'': entity-set exact-match degeneracy (all $N$ samples produce identical entity sets). ``MV $\\Delta$'': strict majority vote gain over greedy (pp). ``Non-degen MV $\\Delta$'': MV gain on non-degenerate instances only. LP $\\Delta$ evaluated on the full test set ($n{=}37{,}648$, including gold-empty instances) for consistency with Table~\\ref{tab:fewnerd}.}\nsections/appendix.tex:2091:MV $\\Delta$ (pp) & $-$2.74 & $-$0.40 \\\\\nsections/appendix.tex:2094:LP $\\Delta$ (pp) & $+$1.39 & $+$0.12${\\pm}$0.04 \\\\\nsections/appendix.tex:2095:Entity constr.\\ $\\Delta$ (pp) & $+$0.88 & $+$0.20 \\\\\nsections/appendix.tex:2123:LP $\\Delta$ (pp) & $-$1.24 & $+$0.64 & $+$1.02 \\\\\nsections/appendix.tex:2165:Dataset & LP $\\Delta$ (pp) & 95\\% CI & Interpretation \\\\\nsections/appendix.tex:2218:Aggregation & Med.\\ var. & $\\rho$ & AUROC & $\\Delta$ (pp) \\\\\nsections/appendix.tex:2243:Dataset & Greedy & Best merge ($k^*$) & $\\Delta$ (pp) & Recovery (\\%) \\\\\nsections/appendix.tex:2284:\\caption{Entity construction threshold sensitivity ($N{=}8$, Qwen3-8B, $T{=}1.0$). $\\Delta$: F1 difference vs.\\ greedy in percentage points. Best $\\Delta$ per dataset--weighting pair in \\textbf{bold}.}",
    "numLines": 26
  }
}
```

</details>

---

### Assistant

_source line 121_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "7a2cab92-4627-4362-bbed-a22314906058",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TFJ37x62j9JVaJnxu2hQFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 102874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2834
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 122_

<details open><summary>🔧 Tool call — Bash · `toolu_01921KDYCwU2GfEnwnGAGGsi`</summary>

```json
{
  "command": "grep -n \"\\\\\\\\,pp\\|~pp\\| pp \" sections/introduction.tex sections/abstract.tex sections/background.tex sections/diagnostic.tex sections/single_signal.tex sections/adaptive.tex sections/theory.tex sections/experiments_main.tex 2>/dev/null | head -10",
  "description": "Find first usage of pp"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "825ca804-fa9b-4ec2-b502-99bb64d667f6",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01TFJ37x62j9JVaJnxu2hQFo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2834,
      "cache_read_input_tokens": 102874,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2834
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 123 · 2026-05-24T01:38:56.528Z_

<details><summary>↩ Tool result · `toolu_01921KDYCwU2GfEnwnGAGGsi`</summary>

```text
sections/introduction.tex:6:Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
sections/introduction.tex:11:The optimal strategy is dataset-dependent (LP $+1.39$\,pp on Few-NERD; MV $+0.6$\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\% zero-F1; Appendix~\ref{app:re_extension}).
sections/introduction.tex:12:Exploratory entity-level construction yields conditional improvement ($+1.40$\,pp on Few-NERD, 3-epoch; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.
sections/introduction.tex:19:\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain). Representative values across datasets: AUROC from CoNLL EM; $\rho$ and entity-construction gain from Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; Tables~\ref{tab:quality_estimation},~\ref{tab:entity_construction}). \textbf{Left}: consistency signals estimate instance quality. \textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \textbf{Right}: LP-weighted entity construction ($\theta{=}2/N$) yields conditional gains ($+1.40$\,pp on Few-NERD; \S\ref{sec:prescriptive}).}
sections/introduction.tex:30:Entity-level construction yields $+1.40$\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.
sections/abstract.tex:4:Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\,pp; CI crosses zero), revealing a \textbf{correlation-selection gap}.
sections/abstract.tex:6:Entity-level construction yields conditional gains ($+1.40$\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.
sections/single_signal.tex:35:\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\rho$; line: $\Delta$F1 vs.\ greedy (3-seed mean). Despite $\rho$ up to 0.38, no signal outperforms greedy (all $p{\geq}0.29$). Dashed green: oracle headroom ($+13.0$\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}
sections/single_signal.tex:39:Despite $\rho$ up to 0.38, no signal outperforms greedy on SciERC (Table~\ref{tab:selection}; Figure~\ref{fig:selection_gap}); the oracle shows 13.0\,pp headroom, but LP achieves $+0.2$\,pp ($p{=}0.29$), below MDE (${\approx}$1.5\,pp at $n{=}529$, 2--3 seeds; Appendix~\ref{app:bootstrap_signal}).
sections/single_signal.tex:42:Few-NERD provides the clearest positive case: LP achieves $+1.39$\,pp ($p{<}0.001$; Holm $p_{\text{adj}}{=}0.021$, selection family $k{=}21$)\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\text{adj}}{=}0.055$ (BH $p_{\text{adj}}{=}0.003$).} at low degeneracy (13.0\% vs.\ 12.2--67.9\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\,pp; \S\ref{sec:fewnerd}).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b8c7d61b-1b74-4887-97fc-e8740fef90ce",
  "tool_use_result": {
    "stdout": "sections/introduction.tex:6:Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \\textbf{correlation-selection gap}: quality estimation signals predict output quality ($\\rho$ up to $0.45$, AUROC $0.82$; Table~\\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).\nsections/introduction.tex:11:The optimal strategy is dataset-dependent (LP $+1.39$\\,pp on Few-NERD; MV $+0.6$\\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\\% zero-F1; Appendix~\\ref{app:re_extension}).\nsections/introduction.tex:12:Exploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.\nsections/introduction.tex:19:\\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain). Representative values across datasets: AUROC from CoNLL EM; $\\rho$ and entity-construction gain from Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; Tables~\\ref{tab:quality_estimation},~\\ref{tab:entity_construction}). \\textbf{Left}: consistency signals estimate instance quality. \\textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \\textbf{Right}: LP-weighted entity construction ($\\theta{=}2/N$) yields conditional gains ($+1.40$\\,pp on Few-NERD; \\S\\ref{sec:prescriptive}).}\nsections/introduction.tex:30:Entity-level construction yields $+1.40$\\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \\citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.\nsections/abstract.tex:4:Quality estimation signals predict output quality (AUROC up to $0.82$), yet instance-level selection yields no detectable gains (${<}1$\\,pp; CI crosses zero), revealing a \\textbf{correlation-selection gap}.\nsections/abstract.tex:6:Entity-level construction yields conditional gains ($+1.40$\\,pp on Few-NERD under 3-epoch training; collapses at convergence; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition) but exhibits inverse scaling in most configurations.\nsections/single_signal.tex:35:\\caption{Correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Bars: QE $\\rho$; line: $\\Delta$F1 vs.\\ greedy (3-seed mean). Despite $\\rho$ up to 0.38, no signal outperforms greedy (all $p{\\geq}0.29$). Dashed green: oracle headroom ($+13.0$\\,pp; oracle headroom $=$ best-of-$N$ F1 $-$ greedy F1); dotted gray: random.}\nsections/single_signal.tex:39:Despite $\\rho$ up to 0.38, no signal outperforms greedy on SciERC (Table~\\ref{tab:selection}; Figure~\\ref{fig:selection_gap}); the oracle shows 13.0\\,pp headroom, but LP achieves $+0.2$\\,pp ($p{=}0.29$), below MDE (${\\approx}$1.5\\,pp at $n{=}529$, 2--3 seeds; Appendix~\\ref{app:bootstrap_signal}).\nsections/single_signal.tex:42:Few-NERD provides the clearest positive case: LP achieves $+1.39$\\,pp ($p{<}0.001$; Holm $p_{\\text{adj}}{=}0.021$, selection family $k{=}21$)\\footnote{Under global correction ($k{=}57$), LP-best selection reaches Holm $p_{\\text{adj}}{=}0.055$ (BH $p_{\\text{adj}}{=}0.003$).} at low degeneracy (13.0\\% vs.\\ 12.2--67.9\\%), while structural signals still degrade (VC $-1.79$, SJ $-2.14$\\,pp; \\S\\ref{sec:fewnerd}).",
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

_source line 124_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "c7a2bdd1-3e94-4f49-a3ed-3654249f2280",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01T3PRNTxz7ipFrgH2BzkPS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2099,
      "cache_read_input_tokens": 105708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2099
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Read · `toolu_01E2KebaZ9cLsHqvp4J9HPGH`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "offset": 1,
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "35284121-ef72-4c93-a630-cb63e6e4c785",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01T3PRNTxz7ipFrgH2BzkPS5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2099,
      "cache_read_input_tokens": 105708,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2099
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 126 · 2026-05-24T01:39:05.271Z_

<details><summary>↩ Tool result · `toolu_01E2KebaZ9cLsHqvp4J9HPGH`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Test-time compute scaling---self-consistency \cite{wang2023selfconsistency}, best-of-$N$ \cite{snell2025scaling, brown2024monkeys}, extended reasoning \cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.
4	For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \cite{yao2026consistency} and qualitative diversity collapse \cite{yun2025price} but no instance-level diagnostic framework.
5	
6	Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \textbf{correlation-selection gap}: quality estimation signals predict output quality ($\rho$ up to $0.45$, AUROC $0.82$; Table~\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\,pp even at $N{=}64$ (Figure~\ref{fig:n_scaling}; Table~\ref{tab:selection}).
7	This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\S\ref{sec:selection_gap}).
8	A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\textendash$0.88$; Appendix~\ref{sec:mechanistic}), exposing an \textit{introspection boundary} \cite{huang2024large}.
9	A \textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\%) and signal alignment collapse ($\alpha{\to}0$; $\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\ref{tab:method_summary}).
10	The framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori; our analysis is observational and all reported associations are correlational, not causal.
11	The optimal strategy is dataset-dependent (LP $+1.39$\,pp on Few-NERD; MV $+0.6$\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\% zero-F1; Appendix~\ref{app:re_extension}).
12	Exploratory entity-level construction yields conditional improvement ($+1.40$\,pp on Few-NERD, 3-epoch; global Holm $p_{\text{adj}}{=}0.055$, suggestive; per-family $p_{\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.
13	
14	These findings rest on four NER benchmarks, two model families with 4B--72B ablations, $N {\in} \{2, \ldots, 64\}$, and exploratory extensions to RE\footnote{RE F1 is confounded by entity span errors: the majority of zero-F1 RE instances reflect upstream NER mismatches rather than relation classification failure (Appendix~\ref{app:re_extension}).} and SQL parsing ($87.2$\% degeneracy).
15	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a350baa8-0b41-4301-90e1-0ab631b2189a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time compute scaling---self-consistency \\cite{wang2023selfconsistency}, best-of-$N$ \\cite{snell2025scaling, brown2024monkeys}, extended reasoning \\cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.\nFor NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \\cite{yao2026consistency} and qualitative diversity collapse \\cite{yun2025price} but no instance-level diagnostic framework.\n\nUsing NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \\textbf{correlation-selection gap}: quality estimation signals predict output quality ($\\rho$ up to $0.45$, AUROC $0.82$; Table~\\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).\nThis gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\\S\\ref{sec:selection_gap}).\nA hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\\textendash$0.88$; Appendix~\\ref{sec:mechanistic}), exposing an \\textit{introspection boundary} \\cite{huang2024large}.\nA \\textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\\%) and signal alignment collapse ($\\alpha{\\to}0$; $\\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\\ref{tab:method_summary}).\nThe framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori; our analysis is observational and all reported associations are correlational, not causal.\nThe optimal strategy is dataset-dependent (LP $+1.39$\\,pp on Few-NERD; MV $+0.6$\\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\\% zero-F1; Appendix~\\ref{app:re_extension}).\nExploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.\n\nThese findings rest on four NER benchmarks, two model families with 4B--72B ablations, $N {\\in} \\{2, \\ldots, 64\\}$, and exploratory extensions to RE\\footnote{RE F1 is confounded by entity span errors: the majority of zero-F1 RE instances reflect upstream NER mismatches rather than relation classification failure (Appendix~\\ref{app:re_extension}).} and SQL parsing ($87.2$\\% degeneracy).\n",
      "numLines": 15,
      "startLine": 1,
      "totalLines": 34
    }
  }
}
```

</details>

---

### Tool call

_source line 127_

<details open><summary>🔧 Tool call — Edit · `toolu_015qbpP9KQ7aFjemC9aQcDUb`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
  "old_string": "yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).",
  "new_string": "yet selection yields no detectable gains---MV ${<}1$ percentage point (pp) even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection})."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b91b9dbe-12bc-4dab-91d6-fb777e5ee708",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01SBjH8nKCZhraCJvLuMVn9i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1679,
      "cache_read_input_tokens": 107807,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1679
      },
      "output_tokens": 60,
      "service_tier": "standard",
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

_source line 128 · 2026-05-24T01:39:11.721Z_

<details><summary>↩ Tool result · `toolu_015qbpP9KQ7aFjemC9aQcDUb`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d5ea277b-bd15-404d-b788-56a352fb3993",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
    "oldString": "yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).",
    "newString": "yet selection yields no detectable gains---MV ${<}1$ percentage point (pp) even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).",
    "originalFile": "\\section{Introduction}\\label{sec:introduction}\n\nTest-time compute scaling---self-consistency \\cite{wang2023selfconsistency}, best-of-$N$ \\cite{snell2025scaling, brown2024monkeys}, extended reasoning \\cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.\nFor NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \\cite{yao2026consistency} and qualitative diversity collapse \\cite{yun2025price} but no instance-level diagnostic framework.\n\nUsing NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \\textbf{correlation-selection gap}: quality estimation signals predict output quality ($\\rho$ up to $0.45$, AUROC $0.82$; Table~\\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).\nThis gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\\S\\ref{sec:selection_gap}).\nA hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\\textendash$0.88$; Appendix~\\ref{sec:mechanistic}), exposing an \\textit{introspection boundary} \\cite{huang2024large}.\nA \\textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\\%) and signal alignment collapse ($\\alpha{\\to}0$; $\\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\\ref{tab:method_summary}).\nThe framework decomposes observed failures post-hoc rather than predicting which instances will fail a priori; our analysis is observational and all reported associations are correlational, not causal.\nThe optimal strategy is dataset-dependent (LP $+1.39$\\,pp on Few-NERD; MV $+0.6$\\,pp on CoNLL), and RE reveals a distinct bottleneck ($40$\\% zero-F1; Appendix~\\ref{app:re_extension}).\nExploratory entity-level construction yields conditional improvement ($+1.40$\\,pp on Few-NERD, 3-epoch; global Holm $p_{\\text{adj}}{=}0.055$, suggestive; per-family $p_{\\text{adj}}{=}0.006$, post-hoc family partition; diminishes at convergence) where the framework identifies favorable conditions---low degeneracy and LP-F1 alignment---but inverse scaling in most $N$-transitions confirms that scaling is harmful in the majority of configurations.\n\nThese findings rest on four NER benchmarks, two model families with 4B--72B ablations, $N {\\in} \\{2, \\ldots, 64\\}$, and exploratory extensions to RE\\footnote{RE F1 is confounded by entity span errors: the majority of zero-F1 RE instances reflect upstream NER mismatches rather than relation classification failure (Appendix~\\ref{app:re_extension}).} and SQL parsing ($87.2$\\% degeneracy).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{Overview of the correlation-selection gap (diagnostic sequence, not causal chain). Representative values across datasets: AUROC from CoNLL EM; $\\rho$ and entity-construction gain from Few-NERD (Qwen3-8B, $N{=}8$, $T{=}1.0$; Tables~\\ref{tab:quality_estimation},~\\ref{tab:entity_construction}). \\textbf{Left}: consistency signals estimate instance quality. \\textbf{Center}: instance-level signals assign identical scores to all $N$ candidates, so selection cannot outperform greedy. \\textbf{Right}: LP-weighted entity construction ($\\theta{=}2/N$) yields conditional gains ($+1.40$\\,pp on Few-NERD; \\S\\ref{sec:prescriptive}).}\n\\label{fig:overview}\n\\end{figure*}\n\nOur investigation proceeds in three stages:\n\\begin{enumerate}[nosep]\n\\item \\textbf{Discover} [\\S\\ref{sec:qe_results}].\nQE signals achieve AUROC up to $0.82$; while \\citet{yao2026consistency} report task-level correlation ($\\rho$ up to 0.47), our instance-level decomposition reveals why correlation does not yield selection gains.\n\\item \\textbf{Diagnose} [\\S\\ref{sec:selection_gap}, \\S\\ref{sec:adaptive}, \\S\\ref{sec:theory}].\nA diagnostic cascade---degeneracy, LP compression, signal alignment---quantifies failure mechanisms at entity level; \\citet{yun2025price} describe diversity collapse qualitatively, we provide quantitative decomposition ($D$, $\\alpha$, LP range). A necessary condition bound (\\S\\ref{sec:theory}) confirms $\\alpha$ as the binding constraint (3--12\\% recovery ratio). Hidden-state probes reveal an introspection boundary (AUROC $0.63$--$0.88$ vs.\\ ESJ $\\approx 0.50$; Appendix~\\ref{sec:mechanistic}).\n\\item \\textbf{Construct (exploratory)} [\\S\\ref{sec:prescriptive}].\nEntity-level construction yields $+1.40$\\,pp on Few-NERD where the cascade identifies favorable conditions. Unlike \\citet{xie2023zeroshot}'s zero-shot entity voting, we aggregate stochastic samples from fine-tuned models.\n\\end{enumerate}\n\nThe paper is organized as follows: \\S\\ref{sec:related} contextualizes our contributions relative to prior art; \\S\\ref{sec:method} defines the diagnostic framework and confidence signals; \\S\\ref{sec:selection_gap} establishes the correlation-selection gap; \\S\\ref{sec:adaptive} evaluates adaptive methods; \\S\\ref{sec:theory_scaling} provides scaling analysis and degeneracy decomposition; \\S\\ref{sec:experiments} presents the main experimental results.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 7,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " Test-time compute scaling---self-consistency \\cite{wang2023selfconsistency}, best-of-$N$ \\cite{snell2025scaling, brown2024monkeys}, extended reasoning \\cite{muennighoff2025s1}---yields large gains on discrete-answer tasks where outputs admit equivalence classes or execution-based verification.",
          " For NER, where outputs are entity sets with partial overlap, the boundary conditions for effective scaling are unknown; prior work reports task-level correlations \\cite{yao2026consistency} and qualitative diversity collapse \\cite{yun2025price} but no instance-level diagnostic framework.",
          " ",
          "-Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \\textbf{correlation-selection gap}: quality estimation signals predict output quality ($\\rho$ up to $0.45$, AUROC $0.82$; Table~\\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$\\,pp even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).",
          "+Using NER (four datasets, primarily 7--14B fine-tuned; tentative cross-scale observations to 72B) and RE as case studies, we identify a \\textbf{correlation-selection gap}: quality estimation signals predict output quality ($\\rho$ up to $0.45$, AUROC $0.82$; Table~\\ref{tab:quality_estimation}), yet selection yields no detectable gains---MV ${<}1$ percentage point (pp) even at $N{=}64$ (Figure~\\ref{fig:n_scaling}; Table~\\ref{tab:selection}).",
          " This gap decomposes into a definitional layer---four instance-level signals assign identical scores to all candidates---and an empirical one: LP, the only per-sample signal, also yields no gains, through within-instance compression (\\S\\ref{sec:selection_gap}).",
          " A hidden-state probe confirms models encode entity quality internally (AUROC $0.63$\\textendash$0.88$; Appendix~\\ref{sec:mechanistic}), exposing an \\textit{introspection boundary} \\cite{huang2024large}.",
          " A \\textit{diagnostic framework} localizes the failure to two co-occurring conditions---degeneracy ($12$--$68$\\%) and signal alignment collapse ($\\alpha{\\to}0$; $\\alpha$ here denotes LP-F1 alignment)---which co-occur with selection failure (Table~\\ref{tab:method_summary})."
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

_source line 129_

Now let me check anonymization:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "99ed8595-7f2e-4772-95b8-a3e84c4cb71d",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012qnhonXJJYyJpAZNmUaKQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 109486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 130_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01DgHWvWzg6cQVLvfmsvNMcC`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "completed"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "completed"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "completed"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "completed"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "completed"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "in_progress"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "pending"
    },
    {
      "content": "Sync to anonymous repo if changes were made",
      "activeForm": "Syncing to anonymous repo",
      "status": "pending"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1ea192d5-d7f5-4cb3-b482-c019c75992cc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_012qnhonXJJYyJpAZNmUaKQh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 411,
      "cache_read_input_tokens": 109486,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 411
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

_source line 131 · 2026-05-24T01:39:18.714Z_

<details><summary>↩ Tool result · `toolu_01DgHWvWzg6cQVLvfmsvNMcC`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "65f449cb-42c5-45de-8baf-52eda0760d88",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "in_progress",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "pending",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "pending",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "completed",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "completed",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "in_progress",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 132_

<details open><summary>🔧 Tool call — Bash · `toolu_01Cubhre9w5ke2rmyHq5jVP3`</summary>

```json
{
  "command": "grep -rni \"github\\.com\" sections/*.tex 2>/dev/null | grep -v \"anonymous-nlp-2026\\|_archived\"; echo \"---\"; grep -rniE \"@[a-zA-Z0-9._-]+\\.(com|edu|org)\" sections/*.tex 2>/dev/null | grep -v \"_archived\\|anonymous@\\|noreply@\"; echo \"---\"; grep -rni \"/root/\\|/home/\\|/Users/\\|autodl\\|AutoDL\" sections/*.tex 2>/dev/null | grep -v \"_archived\"",
  "description": "Check anonymization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "06d6baef-3725-4a86-b7eb-f49c9f013d73",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01JiTLLHN6FDdAG3t8nW8XSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 509,
      "cache_read_input_tokens": 109897,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 509
      },
      "output_tokens": 51,
      "service_tier": "standard",
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

_source line 133 · 2026-05-24T01:39:23.628Z_

<details><summary>↩ Tool result · `toolu_01Cubhre9w5ke2rmyHq5jVP3`</summary>

```text
---
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "86eb6bd4-9920-4f1c-9142-834f46f58963",
  "tool_use_result": {
    "stdout": "---\n---",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 134_

<details open><summary>🔧 Tool call — Bash · `toolu_011QKsDWvsirSL2WdQJBuZ22`</summary>

```json
{
  "command": "grep -rniE \"\\b(university|institute|department|laborator)\" sections/*.tex 2>/dev/null | grep -v \"_archived\\|\\\\\\\\cite\\|\\\\\\\\citet\\|\\\\\\\\citep\\|bibliography\\|tab:\\|fig:\\|Appendix\\|appendix\"",
  "description": "Check for university/institute mentions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "ea924a13-1303-48e5-8c81-117b0dd73c4f",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01CCipGkFMz4fES1nsHtSW53",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 110406,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 296
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 135 · 2026-05-24T01:39:32.226Z_

<details><summary>↩ Tool result · `toolu_011QKsDWvsirSL2WdQJBuZ22`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "2201a79c-d73d-425e-850c-74810df22d21",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 136_

<details open><summary>🔧 Tool call — Bash · `toolu_015wXYvpCfwbqj3W8PRHaHgk`</summary>

```json
{
  "command": "grep -niE \"anonymous-nlp-2026|github\\.com|gitlab\\.com|huggingface\\.co/[a-zA-Z]\" sections/*.tex 2>/dev/null | grep -v \"_archived\"",
  "description": "Find URLs in sections"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "54805c23-8689-4446-8520-da2bef58b22b",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01EHXZQkdzh6FtQx9W9Dy38W",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 212,
      "cache_read_input_tokens": 110702,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 212
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

### Tool result

_source line 137 · 2026-05-24T01:39:39.451Z_

<details><summary>↩ Tool result · `toolu_015wXYvpCfwbqj3W8PRHaHgk`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "f3341ff9-8bed-4fed-8992-1e8b31bbc18a",
  "tool_use_result": {
    "stdout": "",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 138_

<details open><summary>🔧 Tool call — Bash · `toolu_01RKTdfYTrHTPSZ4z9tyHYxy`</summary>

```json
{
  "command": "grep -niE \"anonymous|anon|withheld\" sections/*.tex 2>/dev/null | grep -v \"_archived\" | head -10",
  "description": "Find anonymization markers"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5b1f9018-6fab-44c2-84a9-c2b088b48a92",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01MieHrD9yK22j8Us5efbnHZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 186,
      "cache_read_input_tokens": 110914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 186
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 139 · 2026-05-24T01:39:48.423Z_

<details><summary>↩ Tool result · `toolu_01RKTdfYTrHTPSZ4z9tyHYxy`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "18d929b0-bebf-49aa-b576-17a2b1364de9",
  "tool_use_result": {
    "stdout": "",
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

_source line 140_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "78f1ef69-8ea7-46f1-bd22-35a6344616f3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NopcNw1p99CYwc6mAMRVoM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 111100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

### Tool call

_source line 141_

<details open><summary>🔧 Tool call — Bash · `toolu_01Qprpt7Kpm7rAqnLSC6Djap`</summary>

```json
{
  "command": "grep -nE \"^@\" references.bib | awk -F'[@{,]' '{print $3}' | sort | uniq -d | head -5; echo \"---\"; grep -cE \"^@\" references.bib",
  "description": "Find duplicate bib keys"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "6cfc32ce-2601-462f-a029-0d12d401b6a8",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NopcNw1p99CYwc6mAMRVoM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 159,
      "cache_read_input_tokens": 111100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 159
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

_source line 142 · 2026-05-24T01:39:54.143Z_

<details><summary>↩ Tool result · `toolu_01Qprpt7Kpm7rAqnLSC6Djap`</summary>

```text
---
60
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d7fc7845-711f-4cd4-8ce7-646284a22d5f",
  "tool_use_result": {
    "stdout": "---\n60",
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

_source line 143_

<details open><summary>🔧 Tool call — Bash · `toolu_012pKn9PwQhZYUEFEvZkD3ec`</summary>

```json
{
  "command": "grep -iE \"anonymous|withheld|TODO|XXX|FIXME\" references.bib | head -10",
  "description": "Check bib for any placeholders or self-identification"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "731d65cd-e4a9-448e-902e-b214016aef2c",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014j9Fze9k6oufadCEQ6S8Hv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 248,
      "cache_read_input_tokens": 111259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 248
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 144 · 2026-05-24T01:39:57.207Z_

<details><summary>↩ Tool result · `toolu_012pKn9PwQhZYUEFEvZkD3ec`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1ec921b6-2fde-4367-9c25-95fec85dbba8",
  "tool_use_result": {
    "stdout": "",
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

_source line 145_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01HLZHmetEVXXyWfcWnZ3Rhv`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "completed"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "completed"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "completed"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "completed"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "completed"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "completed"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "completed"
    },
    {
      "content": "Recompile and sync to anonymous repo",
      "activeForm": "Recompiling and syncing",
      "status": "in_progress"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a6d5201d-720f-4494-9362-fcf0987033fa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Y54F5tXsg4qQR85jvnhRDP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 155,
      "cache_read_input_tokens": 111507,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 155
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

_source line 146 · 2026-05-24T01:40:03.938Z_

<details><summary>↩ Tool result · `toolu_01HLZHmetEVXXyWfcWnZ3Rhv`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "69795581-1094-42bc-ae26-597ff2cf1cf0",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "completed",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "completed",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "in_progress",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "pending",
        "activeForm": "Checking bib"
      },
      {
        "content": "Sync to anonymous repo if changes were made",
        "status": "pending",
        "activeForm": "Syncing to anonymous repo"
      }
    ],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "completed",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "completed",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "completed",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "completed",
        "activeForm": "Checking bib"
      },
      {
        "content": "Recompile and sync to anonymous repo",
        "status": "in_progress",
        "activeForm": "Recompiling and syncing"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Tool call

_source line 147_

<details open><summary>🔧 Tool call — Bash · `toolu_01SHcy7CH2FE5JCRS9Zyf1H6`</summary>

```json
{
  "command": "pdflatex -interaction=nonstopmode main.tex > /tmp/compile1.log 2>&1 && bibtex main > /tmp/bibtex.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile2.log 2>&1 && pdflatex -interaction=nonstopmode main.tex > /tmp/compile3.log 2>&1; echo \"Exit: $?\"; pdfinfo main.pdf | grep -i pages",
  "description": "Recompile after all edits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "fe3eabaa-16f4-4fc3-98cb-7bb0a15ea9f4",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_014qQPqHqTDLd6v6Wy3CteyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 495,
      "cache_read_input_tokens": 111662,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 495
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

### System

_source line 148_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bzar45a7o",
  "tool_use_id": "toolu_01SHcy7CH2FE5JCRS9Zyf1H6",
  "description": "Recompile after all edits",
  "task_type": "local_bash",
  "uuid": "4ce251ad-dfaa-4446-8848-f42dfa5ffa8b",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### System

_source line 149_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bzar45a7o",
  "tool_use_id": "toolu_01SHcy7CH2FE5JCRS9Zyf1H6",
  "status": "completed",
  "output_file": "",
  "summary": "Recompile after all edits",
  "uuid": "9b641a83-e6f5-471b-9ae5-347d6c168a1c",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236"
}
```

---

### Tool result

_source line 150 · 2026-05-24T01:40:14.804Z_

<details><summary>↩ Tool result · `toolu_01SHcy7CH2FE5JCRS9Zyf1H6`</summary>

```text
Exit: 0
Pages:           46
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "9bf9e9f5-f052-412d-84f1-c5e703f0abca",
  "tool_use_result": {
    "stdout": "Exit: 0\nPages:           46",
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

_source line 151_

<details open><summary>🔧 Tool call — Bash · `toolu_01KZ7ekg4K8p2YRKB5GeeYhQ`</summary>

```json
{
  "command": "grep -cE \"^!|undefined|Citation.*undefined\" main.log",
  "description": "Final error check"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5ebd8a75-e20d-44c2-9dae-54de9cdb60cd",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NxpEfzyrPNb456B89J7NHK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 281,
      "cache_read_input_tokens": 112157,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 281
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 152 · 2026-05-24T01:40:17.426Z_

<details><summary>↩ Tool result · `toolu_01KZ7ekg4K8p2YRKB5GeeYhQ`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "05b6aecf-2494-4f22-b2d5-62e42e98381a",
  "tool_use_result": {
    "stdout": "0",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "returnCodeInterpretation": "No matches found",
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 153_

<details open><summary>🔧 Tool call — Bash · `toolu_01H5AYDPTWUvG4SVSkNerzM4`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | grep -n \"^Limitations\\|^[[:space:]]*Limitations\" | head -3",
  "description": "Confirm Limitations location"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "148dad37-bb8f-498b-8472-12fbf8c3311e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_011FdnCw4fWQd18t32gg4UJU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 124,
      "cache_read_input_tokens": 112438,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 124
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 154 · 2026-05-24T01:40:21.240Z_

<details><summary>↩ Tool result · `toolu_01H5AYDPTWUvG4SVSkNerzM4`</summary>

```text
678:                                                                                                                                 Limitations                                                 556
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "dcb79e89-ca7f-437f-9278-106d849591eb",
  "tool_use_result": {
    "stdout": "678:                                                                                                                                 Limitations                                                 556",
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

_source line 155_

<details open><summary>🔧 Tool call — Bash · `toolu_01Eytjq82M1HoeqNkoRgv3DR`</summary>

```json
{
  "command": "pdftotext -layout main.pdf - 2>/dev/null | awk '/^[[:space:]]*[0-9]+[[:space:]]*$/{print NR\": \"$0}' | head -20",
  "description": "Find page number positions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "01eb5712-4a8f-4a38-84f8-a569f1cd1e14",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_013VA1oGvDmhN1Sx4DLHLYua",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 176,
      "cache_read_input_tokens": 112562,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 176
      },
      "output_tokens": 61,
      "service_tier": "standard",
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

_source line 156 · 2026-05-24T01:40:25.744Z_

<details><summary>↩ Tool result · `toolu_01Eytjq82M1HoeqNkoRgv3DR`</summary>

```text
64:                                                                       1
68:                                                                1
160:                                                                   2
247:                                                                                                     3
320:           2
323:           3
338:                                                                           4
406:           4
412:                                                               5
509:                   5
516:                                                                                                         6
523: 434
531: 440
532:                                                                            3
535: 442
593:                                                               7
617:                                            529
689:                                                                                                                              8
757:                                                                 9
825:                                                                  10
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "93e59941-88c7-47d4-8a2d-8e5384a43f81",
  "tool_use_result": {
    "stdout": "64:                                                                       1\n68:                                                                1\n160:                                                                   2\n247:                                                                                                     3\n320:           2\n323:           3\n338:                                                                           4\n406:           4\n412:                                                               5\n509:                   5\n516:                                                                                                         6\n523: 434\n531: 440\n532:                                                                            3\n535: 442\n593:                                                               7\n617:                                            529\n689:                                                                                                                              8\n757:                                                                 9\n825:                                                                  10",
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

_source line 157_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "085a2463-b308-4087-8337-dfcf436ad4b3",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0162xCuVqqybjE35G9ok2C3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 112738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 158_

<details open><summary>🔧 Tool call — Bash · `toolu_017zqznuC6YYESzTsAHyT8kk`</summary>

```json
{
  "command": "ls /tmp/anon_repo/ 2>/dev/null && echo \"exists\" || echo \"NOT_EXISTS\"",
  "description": "Check if anonymous repo exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "2508b5a0-371e-4abd-bc23-57908f418dd1",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_0162xCuVqqybjE35G9ok2C3p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 320,
      "cache_read_input_tokens": 112738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 320
      },
      "output_tokens": 58,
      "service_tier": "standard",
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

_source line 159 · 2026-05-24T01:40:32.555Z_

<details><summary>↩ Tool result · `toolu_017zqznuC6YYESzTsAHyT8kk`</summary>

```text
AI_DISCLOSURE.md
LICENSE
README.md
analysis_d141_conditional_decomp.py
analysis_d141_entity_merge.py
analysis_d141_scatter_plot.py
analysis_r21_q1_alignment.py
analyze_freeform_ablation.py
analyze_freeform_conll.py
analyze_lp_compression.py
auto_launch_mf4.sh
b7_adaptive_budget.py
b7_adaptive_budget_v2.py
bootstrap_analysis.py
bootstrap_analysis2.py
code
compute_error_correlation.py
compute_fk_excess.py
compute_missing_n8.py
compute_seed42_degentable.py
configs
deberta_verifier_5fold.py
deep_freeform_analysis.py
docs
e_theta_v1.py
e_theta_v2_mlp.py
e_theta_v3_no_dataset.py
e_theta_v4_no_model.py
env.sh
evaluate_verifier.py
examples
experiments
launch_seeds.sh
logprob_tie_analysis.py
logprob_tie_structural.py
merge_4b.py
merge_4b_ckpt4200.py
merge_and_infer_seed123.sh
merge_conll.py
merge_lora.py
merge_shards_exp021.sh
multiseed_flip_analysis.py
multiseed_flip_analysis_part2.py
patch_scripts.py
requirements.txt
rho_audit.py
run_32b_fewnerd_inference.sh
run_bootstrap_loo.py
run_conll_seed456.sh
run_distill_verifier.py
run_exp017_llama_conll_pipeline.sh
run_fewnerd_seed123.sh
run_fewnerd_seed456.sh
run_freeform_conll.py
run_freeform_fewnerd.py
run_freeform_inference.py
run_het_temp_all.sh
run_llama_conll_bootstrap.py
run_loo_v2.py
run_parallel_exp021.sh
scripts
train_supervised_verifier.py
exists
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "e7f65784-3abb-4b06-a074-9fcf77d964dd",
  "tool_use_result": {
    "stdout": "AI_DISCLOSURE.md\nLICENSE\nREADME.md\nanalysis_d141_conditional_decomp.py\nanalysis_d141_entity_merge.py\nanalysis_d141_scatter_plot.py\nanalysis_r21_q1_alignment.py\nanalyze_freeform_ablation.py\nanalyze_freeform_conll.py\nanalyze_lp_compression.py\nauto_launch_mf4.sh\nb7_adaptive_budget.py\nb7_adaptive_budget_v2.py\nbootstrap_analysis.py\nbootstrap_analysis2.py\ncode\ncompute_error_correlation.py\ncompute_fk_excess.py\ncompute_missing_n8.py\ncompute_seed42_degentable.py\nconfigs\ndeberta_verifier_5fold.py\ndeep_freeform_analysis.py\ndocs\ne_theta_v1.py\ne_theta_v2_mlp.py\ne_theta_v3_no_dataset.py\ne_theta_v4_no_model.py\nenv.sh\nevaluate_verifier.py\nexamples\nexperiments\nlaunch_seeds.sh\nlogprob_tie_analysis.py\nlogprob_tie_structural.py\nmerge_4b.py\nmerge_4b_ckpt4200.py\nmerge_and_infer_seed123.sh\nmerge_conll.py\nmerge_lora.py\nmerge_shards_exp021.sh\nmultiseed_flip_analysis.py\nmultiseed_flip_analysis_part2.py\npatch_scripts.py\nrequirements.txt\nrho_audit.py\nrun_32b_fewnerd_inference.sh\nrun_bootstrap_loo.py\nrun_conll_seed456.sh\nrun_distill_verifier.py\nrun_exp017_llama_conll_pipeline.sh\nrun_fewnerd_seed123.sh\nrun_fewnerd_seed456.sh\nrun_freeform_conll.py\nrun_freeform_fewnerd.py\nrun_freeform_inference.py\nrun_het_temp_all.sh\nrun_llama_conll_bootstrap.py\nrun_loo_v2.py\nrun_parallel_exp021.sh\nscripts\ntrain_supervised_verifier.py\nexists",
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

_source line 160_

<details open><summary>🔧 Tool call — Bash · `toolu_01BbXecq6FggcUA19CCJB1VD`</summary>

```json
{
  "command": "ls /tmp/anon_repo/docs/paper/sections/ 2>/dev/null | head",
  "description": "Check anonymous repo sections dir"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d0355e9a-45a0-4875-b3c8-60c8d1b4c557",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01FUUKXJhNtjd58rDKD2JhXj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1193,
      "cache_read_input_tokens": 113058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1193
      },
      "output_tokens": 62,
      "service_tier": "standard",
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

_source line 161 · 2026-05-24T01:40:35.050Z_

<details><summary>↩ Tool result · `toolu_01BbXecq6FggcUA19CCJB1VD`</summary>

```text
appendix.tex
experiments_main.tex
introduction.tex
single_signal.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "f2fda451-bc97-49a1-bea8-33f2ee85b5a7",
  "tool_use_result": {
    "stdout": "appendix.tex\nexperiments_main.tex\nintroduction.tex\nsingle_signal.tex",
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

_source line 162_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1468b279-4b42-4da3-a972-663b8528865e",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NwhF1BebuU4jKqf4rs1kP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 169,
      "cache_read_input_tokens": 114251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 169
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

### Tool call

_source line 163_

<details open><summary>🔧 Tool call — Bash · `toolu_017aixuRV7PWRiJHgkbQYcxE`</summary>

```json
{
  "command": "cd /tmp/anon_repo && git status 2>&1 | head -20",
  "description": "Check anon repo git status"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "5be30b2c-7d48-4051-9ce2-89351ab8c0c2",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01NwhF1BebuU4jKqf4rs1kP9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 169,
      "cache_read_input_tokens": 114251,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 169
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

### Tool result

_source line 164 · 2026-05-24T01:40:38.711Z_

<details><summary>↩ Tool result · `toolu_017aixuRV7PWRiJHgkbQYcxE`</summary>

```text
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "8c630d09-9e48-4b49-8bab-c6b6fe95fe63",
  "tool_use_result": {
    "stdout": "On branch main\nYour branch is up to date with 'origin/main'.\n\nnothing to commit, working tree clean",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 165_

<details open><summary>🔧 Tool call — Bash · `toolu_01JxVgpzLQ82sZsCe6BALtuL`</summary>

```json
{
  "command": "cp /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/*.tex /tmp/anon_repo/docs/paper/sections/ && ls /tmp/anon_repo/docs/paper/sections/",
  "description": "Copy section files to anon repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "dc5648e2-d66d-4339-be81-f1d0513ac533",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01KmUAV9ZznJc2JbXVgCAEFA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 304,
      "cache_read_input_tokens": 114420,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 304
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

_source line 166 · 2026-05-24T01:40:41.987Z_

<details><summary>↩ Tool result · `toolu_01JxVgpzLQ82sZsCe6BALtuL`</summary>

```text
abstract.tex
adaptive.tex
appendix.tex
background.tex
checklist.tex
conclusion.tex
diagnostic.tex
discussion.tex
experiments_main.tex
introduction.tex
limitations.tex
mechanistic.tex
method.tex
related_work.tex
single_signal.tex
theoretical.tex
theory.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "93f0c39b-7417-4b24-905a-dd7623f8f9fb",
  "tool_use_result": {
    "stdout": "abstract.tex\nadaptive.tex\nappendix.tex\nbackground.tex\nchecklist.tex\nconclusion.tex\ndiagnostic.tex\ndiscussion.tex\nexperiments_main.tex\nintroduction.tex\nlimitations.tex\nmechanistic.tex\nmethod.tex\nrelated_work.tex\nsingle_signal.tex\ntheoretical.tex\ntheory.tex",
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

_source line 167_

<details open><summary>🔧 Tool call — Bash · `toolu_012fKNZQD9STZg6V6BeDKjDm`</summary>

```json
{
  "command": "cd /tmp/anon_repo && git status 2>&1 | head -30",
  "description": "Check what changed in anon repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "b03c5e1e-f7c1-413d-9d43-040b367fc239",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01293Q37PGBqe2aJ1Cf55cfv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 329,
      "cache_read_input_tokens": 114724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 329
      },
      "output_tokens": 68,
      "service_tier": "standard",
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

_source line 168 · 2026-05-24T01:40:44.699Z_

<details><summary>↩ Tool result · `toolu_012fKNZQD9STZg6V6BeDKjDm`</summary>

```text
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add &lt;file>..." to update what will be committed)
  (use "git restore &lt;file>..." to discard changes in working directory)
	modified:   docs/paper/sections/appendix.tex
	modified:   docs/paper/sections/introduction.tex

Untracked files:
  (use "git add &lt;file>..." to include in what will be committed)
	docs/paper/sections/abstract.tex
	docs/paper/sections/adaptive.tex
	docs/paper/sections/background.tex
	docs/paper/sections/checklist.tex
	docs/paper/sections/conclusion.tex
	docs/paper/sections/diagnostic.tex
	docs/paper/sections/discussion.tex
	docs/paper/sections/limitations.tex
	docs/paper/sections/mechanistic.tex
	docs/paper/sections/method.tex
	docs/paper/sections/related_work.tex
	docs/paper/sections/theoretical.tex
	docs/paper/sections/theory.tex

no changes added to commit (use "git add" and/or "git commit -a")
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "51f9bf1b-05e6-46e3-a02b-c55af86655ba",
  "tool_use_result": {
    "stdout": "On branch main\nYour branch is up to date with 'origin/main'.\n\nChanges not staged for commit:\n  (use \"git add &lt;file>...\" to update what will be committed)\n  (use \"git restore &lt;file>...\" to discard changes in working directory)\n\tmodified:   docs/paper/sections/appendix.tex\n\tmodified:   docs/paper/sections/introduction.tex\n\nUntracked files:\n  (use \"git add &lt;file>...\" to include in what will be committed)\n\tdocs/paper/sections/abstract.tex\n\tdocs/paper/sections/adaptive.tex\n\tdocs/paper/sections/background.tex\n\tdocs/paper/sections/checklist.tex\n\tdocs/paper/sections/conclusion.tex\n\tdocs/paper/sections/diagnostic.tex\n\tdocs/paper/sections/discussion.tex\n\tdocs/paper/sections/limitations.tex\n\tdocs/paper/sections/mechanistic.tex\n\tdocs/paper/sections/method.tex\n\tdocs/paper/sections/related_work.tex\n\tdocs/paper/sections/theoretical.tex\n\tdocs/paper/sections/theory.tex\n\nno changes added to commit (use \"git add\" and/or \"git commit -a\")",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 169_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "42037276-24c4-449d-9a89-e243afab0114",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01H24Zao2gQDGfxwo7td6YGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 575,
      "cache_read_input_tokens": 115053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 575
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 170_

<details open><summary>🔧 Tool call — Bash · `toolu_01E5ouhbNjhLbvGvsh2nvKvu`</summary>

```json
{
  "command": "cd /tmp/anon_repo && git diff docs/paper/sections/ | head -50",
  "description": "Check diff of modified files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "8d03f767-ca96-400e-bd5c-4ac6b53c0adc",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01H24Zao2gQDGfxwo7td6YGy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 575,
      "cache_read_input_tokens": 115053,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 575
      },
      "output_tokens": 50,
      "service_tier": "standard",
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

_source line 171 · 2026-05-24T01:40:55.103Z_

<details><summary>↩ Tool result · `toolu_01E5ouhbNjhLbvGvsh2nvKvu`</summary>

```text
diff --git a/docs/paper/sections/appendix.tex b/docs/paper/sections/appendix.tex
index 6440fe5..3347773 100644
--- a/docs/paper/sections/appendix.tex
+++ b/docs/paper/sections/appendix.tex
@@ -230,13 +230,13 @@ VC's high full-set $\rho{=}0.724$ is entirely attributable to the zero/non-zero
 \paragraph{Cross-configuration selection analysis.}
 Table~\ref{tab:cross_selection} extends the selection analysis to five additional configurations.
 On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
-On LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), consistent with LP being the most stable positive signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA FewNERD degeneracy ($23.4{\pm}4.7$\%, 3 seeds) is higher than Qwen ($13.0$\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.4$~pp) and reduced oracle headroom ($10.0$ vs.\ $12.4$~pp).
+On LLaMA Few-NERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), consistent with LP being the most stable positive signal across model families (Qwen Few-NERD: $+1.39$~pp, Table~\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA Few-NERD degeneracy ($23.4{\pm}4.7$\%, 3 seeds) is higher than Qwen ($13.0$\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.4$~pp) and reduced oracle headroom ($10.0$ vs.\ $12.4$~pp).
 On CoNLL, 48--87\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
 
 \begin{table*}[t]
 \centering
 \small
-\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
+\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
 \label{tab:cross_selection}
 \begin{tabular}{llccccccc}
 \toprule
@@ -245,7 +245,7 @@ Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
 LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
 LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
 \addlinespace
-LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
+LLaMA/Few-NERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \textbf{.788} & .760 \\
 \addlinespace
 Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
 LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
@@ -547,7 +547,7 @@ The learned feature--correctness mapping is dataset-specific: entity agreement p
 Entity-level probes confirm that quality information is partially encoded in hidden representations (AUROC${=}0.63$\textendash$0.88$, dataset-dependent; \S\ref{sec:mechanistic}); we test whether this translates to sample-level selection gain by training probes on the generating model's hidden states.
 
 \paragraph{Setup.}
-Unlike the entity-level probe in \S\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.
+Unlike the entity-level probe in \S\ref{sec:mechanistic} (which classifies individual entities on Few-NERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.
 For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).
 Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).
 
@@ -693,7 +693,7 @@ Dataset & ESJ AUROC & ESJ $\rho$ & Agree.\ AUROC & Agree.\ $\rho$ \\
 \midrule
 SciERC  & 0.512 & 0.020 & 0.792 & 0.515 \\
 CoNLL   & 0.553 & 0.087 & 0.941 & 0.777 \\
-FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
+Few-NERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\
 \bottomrule
 \end{tabular}
 \end{table}
@@ -761,7 +761,7 @@ Framework & LLaMA Factory \\
 \midrule
 \multicolumn{2}{l}{\textit{Dataset-specific}} \\
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "18f93895-bc66-48fe-8e01-10551770e611",
  "tool_use_result": {
    "stdout": "diff --git a/docs/paper/sections/appendix.tex b/docs/paper/sections/appendix.tex\nindex 6440fe5..3347773 100644\n--- a/docs/paper/sections/appendix.tex\n+++ b/docs/paper/sections/appendix.tex\n@@ -230,13 +230,13 @@ VC's high full-set $\\rho{=}0.724$ is entirely attributable to the zero/non-zero\n \\paragraph{Cross-configuration selection analysis.}\n Table~\\ref{tab:cross_selection} extends the selection analysis to five additional configurations.\n On LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of single-sample (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\n-On LLaMA FewNERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), consistent with LP being the most stable positive signal across model families (Qwen FewNERD: $+1.39$~pp, Table~\\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA FewNERD degeneracy ($23.4{\\pm}4.7$\\%, 3 seeds) is higher than Qwen ($13.0$\\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.4$~pp) and reduced oracle headroom ($10.0$ vs.\\ $12.4$~pp).\n+On LLaMA Few-NERD ($n{=}32{,}565$, 3-seed mean), LP is the only signal with positive selection ($+0.36$~pp), consistent with LP being the most stable positive signal across model families (Qwen Few-NERD: $+1.39$~pp, Table~\\ref{tab:fewnerd}). All structural signals degrade selection (VC $-2.39$~pp, SJ $-0.52$~pp), consistent with the Qwen pattern. LLaMA Few-NERD degeneracy ($23.4{\\pm}4.7$\\%, 3 seeds) is higher than Qwen ($13.0$\\%), illustrating the capability-diversity tension: LLaMA achieves stronger greedy F1 ($0.784$ vs.\\ $0.748$, $+3.6$~pp) but at the cost of higher degeneracy ($+10.4$~pp) and reduced oracle headroom ($10.0$ vs.\\ $12.4$~pp).\n On CoNLL, 48--87\\% of instances produce identical outputs across all $N$ samples; this reflects a ceiling effect (single-sample F1 ${\\approx}$0.91--0.92) rather than signal failure, and selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n \n \\begin{table*}[t]\n \\centering\n \\small\n-\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both FewNERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n+\\caption{Best-of-$N$ selection F1 (macro, instance-averaged) across configurations ($T{=}1.0$, 3-seed mean). Best non-oracle signal per row in \\textbf{bold}. LP is the only signal with positive selection on both Few-NERD configurations (Qwen $+1.39$~pp, Table~\\ref{tab:fewnerd}; LLaMA $+0.36$~pp). At $N{=}16$ on LLaMA CoNLL, VC achieves small but significant gains ($+0.28$~pp, $p{<}0.03$; see text below). CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n \\label{tab:cross_selection}\n \\begin{tabular}{llccccccc}\n \\toprule\n@@ -245,7 +245,7 @@ Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\n LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\n \\addlinespace\n-LLaMA/FewNERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\n+LLaMA/Few-NERD $N{=}8$ & 32{,}565 & .784 & .884 & .779 & .779 & .774 & \\textbf{.788} & .760 \\\\\n \\addlinespace\n Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\n LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n@@ -547,7 +547,7 @@ The learned feature--correctness mapping is dataset-specific: entity agreement p\n Entity-level probes confirm that quality information is partially encoded in hidden representations (AUROC${=}0.63$\\textendash$0.88$, dataset-dependent; \\S\\ref{sec:mechanistic}); we test whether this translates to sample-level selection gain by training probes on the generating model's hidden states.\n \n \\paragraph{Setup.}\n-Unlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on FewNERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\n+Unlike the entity-level probe in \\S\\ref{sec:mechanistic} (which classifies individual entities on Few-NERD/CoNLL/SciERC), this sample-level analysis uses all 551 SciERC instances (including 22 with empty gold annotations) to predict per-sample F1.\n For each of $N{=}8$ samples per instance, we extract the mean-pooled final-layer hidden state ($d{=}4096$) from the generating Qwen3-8B model and train a linear probe and a two-layer MLP (hidden dim${=}256$) to predict per-sample F1 (5-fold CV, 3 seeds).\n Entity-level probes use dataset-specific generation temperatures ($T{=}0.5$ for Few-NERD, $T{=}0.8$ for CoNLL, $T{=}1.0$ for SciERC).\n \n@@ -693,7 +693,7 @@ Dataset & ESJ AUROC & ESJ $\\rho$ & Agree.\\ AUROC & Agree.\\ $\\rho$ \\\\\n \\midrule\n SciERC  & 0.512 & 0.020 & 0.792 & 0.515 \\\\\n CoNLL   & 0.553 & 0.087 & 0.941 & 0.777 \\\\\n-FewNERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\n+Few-NERD & 0.495 & $-$0.008 & 0.881 & 0.673 \\\\\n \\bottomrule\n \\end{tabular}\n \\end{table}\n@@ -761,7 +761,7 @@ Framework & LLaMA Factory \\\\\n \\midrule\n \\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Assistant

_source line 172_

<details><summary>Logged reasoning block</summary>

```text

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "25b56a17-6e8f-49a9-9c3a-c3cd34980ad7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017KTX6BfPh3MZodkcgkiqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 115628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4015
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 173_

<details open><summary>🔧 Tool call — Bash · `toolu_017QGipQ63CgSm7J8WfUpyxc`</summary>

```json
{
  "command": "cd /tmp/anon_repo && git add -A docs/paper/sections/ && git -c user.name=\"Anonymous\" -c user.email=\"anonymous@example.com\" commit -m \"Final camera-ready polish: captions, consistency, formatting\" 2>&1 | head -20",
  "description": "Commit changes in anon repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "ac09932e-a4c3-4e30-94d8-d5daf89411da",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_017KTX6BfPh3MZodkcgkiqRh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4015,
      "cache_read_input_tokens": 115628,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4015
      },
      "output_tokens": 45,
      "service_tier": "standard",
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

_source line 174 · 2026-05-24T01:41:00.494Z_

<details><summary>↩ Tool result · `toolu_017QGipQ63CgSm7J8WfUpyxc`</summary>

```text
[main f803b24] Final camera-ready polish: captions, consistency, formatting
 15 files changed, 426 insertions(+), 13 deletions(-)
 create mode 100644 docs/paper/sections/abstract.tex
 create mode 100644 docs/paper/sections/adaptive.tex
 create mode 100644 docs/paper/sections/background.tex
 create mode 100644 docs/paper/sections/checklist.tex
 create mode 100644 docs/paper/sections/conclusion.tex
 create mode 100644 docs/paper/sections/diagnostic.tex
 create mode 100644 docs/paper/sections/discussion.tex
 create mode 100644 docs/paper/sections/limitations.tex
 create mode 100644 docs/paper/sections/mechanistic.tex
 create mode 100644 docs/paper/sections/method.tex
 create mode 100644 docs/paper/sections/related_work.tex
 create mode 100644 docs/paper/sections/theoretical.tex
 create mode 100644 docs/paper/sections/theory.tex
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "716b40db-0b86-4607-8ef5-daa1aa777f5c",
  "tool_use_result": {
    "stdout": "[main f803b24] Final camera-ready polish: captions, consistency, formatting\n 15 files changed, 426 insertions(+), 13 deletions(-)\n create mode 100644 docs/paper/sections/abstract.tex\n create mode 100644 docs/paper/sections/adaptive.tex\n create mode 100644 docs/paper/sections/background.tex\n create mode 100644 docs/paper/sections/checklist.tex\n create mode 100644 docs/paper/sections/conclusion.tex\n create mode 100644 docs/paper/sections/diagnostic.tex\n create mode 100644 docs/paper/sections/discussion.tex\n create mode 100644 docs/paper/sections/limitations.tex\n create mode 100644 docs/paper/sections/mechanistic.tex\n create mode 100644 docs/paper/sections/method.tex\n create mode 100644 docs/paper/sections/related_work.tex\n create mode 100644 docs/paper/sections/theoretical.tex\n create mode 100644 docs/paper/sections/theory.tex",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 175_

<details open><summary>🔧 Tool call — Bash · `toolu_01Y9ZeApY3RTvKRp3gac1DJF`</summary>

```json
{
  "command": "cd /tmp/anon_repo && git push origin main 2>&1 | tail -10",
  "description": "Push to anon repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d0416a1e-93e1-460c-a363-332f42a77af7",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_018ZBXKTuikdUe6Yf35FRd6S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 749,
      "cache_read_input_tokens": 119643,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 749
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

_source line 176 · 2026-05-24T01:41:04.359Z_

<details><summary>↩ Tool result · `toolu_01Y9ZeApY3RTvKRp3gac1DJF`</summary>

```text
To https://github.com/anonymous-nlp-2026/struct_self_consist_ie.git
   70ed395..f803b24  main -> main
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "8d5bd8b3-bd7a-466b-a90e-551cc1c72efd",
  "tool_use_result": {
    "stdout": "To https://github.com/anonymous-nlp-2026/struct_self_consist_ie.git\n   70ed395..f803b24  main -> main",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 177_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01E1f97DvqgbZLPGsLhRMJAX`</summary>

```json
{
  "todos": [
    {
      "content": "Verify compilation, page count, undefined refs",
      "activeForm": "Verifying compilation",
      "status": "completed"
    },
    {
      "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
      "activeForm": "Checking dataset names",
      "status": "completed"
    },
    {
      "content": "Check cross-table consistency footnote (tab:scale_comparison)",
      "activeForm": "Checking cross-table footnote",
      "status": "completed"
    },
    {
      "content": "Review and refine captions in all sections",
      "activeForm": "Reviewing captions",
      "status": "completed"
    },
    {
      "content": "Check abstract word count",
      "activeForm": "Checking abstract word count",
      "status": "completed"
    },
    {
      "content": "Check anonymization",
      "activeForm": "Checking anonymization",
      "status": "completed"
    },
    {
      "content": "Check bib for undefined/duplicate",
      "activeForm": "Checking bib",
      "status": "completed"
    },
    {
      "content": "Recompile and sync to anonymous repo",
      "activeForm": "Recompiling and syncing",
      "status": "completed"
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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "a6ac6966-981f-4276-bf35-95c413a488fa",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01PXVQw285nUMJSRBM5ieyhm",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 230,
      "cache_read_input_tokens": 120392,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 230
      },
      "output_tokens": 54,
      "service_tier": "standard",
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

_source line 178 · 2026-05-24T01:41:09.983Z_

<details><summary>↩ Tool result · `toolu_01E1f97DvqgbZLPGsLhRMJAX`</summary>

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
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "1d963dc8-779c-4b37-9861-d9876302d677",
  "tool_use_result": {
    "oldTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "completed",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "completed",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "completed",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "completed",
        "activeForm": "Checking bib"
      },
      {
        "content": "Recompile and sync to anonymous repo",
        "status": "in_progress",
        "activeForm": "Recompiling and syncing"
      }
    ],
    "newTodos": [
      {
        "content": "Verify compilation, page count, undefined refs",
        "status": "completed",
        "activeForm": "Verifying compilation"
      },
      {
        "content": "Check dataset name consistency (SciERC/CoNLL/Few-NERD/WNUT-17)",
        "status": "completed",
        "activeForm": "Checking dataset names"
      },
      {
        "content": "Check cross-table consistency footnote (tab:scale_comparison)",
        "status": "completed",
        "activeForm": "Checking cross-table footnote"
      },
      {
        "content": "Review and refine captions in all sections",
        "status": "completed",
        "activeForm": "Reviewing captions"
      },
      {
        "content": "Check abstract word count",
        "status": "completed",
        "activeForm": "Checking abstract word count"
      },
      {
        "content": "Check anonymization",
        "status": "completed",
        "activeForm": "Checking anonymization"
      },
      {
        "content": "Check bib for undefined/duplicate",
        "status": "completed",
        "activeForm": "Checking bib"
      },
      {
        "content": "Recompile and sync to anonymous repo",
        "status": "completed",
        "activeForm": "Recompiling and syncing"
      }
    ],
    "verificationNudgeNeeded": false
  }
}
```

</details>

---

### Assistant

_source line 179_

## Final Polish Report

### 1. 编译验证
- Errors: 0
- Undefined refs: 0
- Main text pages: 8 (Limitations starts on page 8, References on page 9)
- Bib warnings: 0

### 2. Caption 检查
- [PASS] Captions are self-contained: model name (Qwen3-8B/LLaMA-3.1-8B), dataset, N, T, seed counts are stated; symbol abbreviations (VC, SJ, FK, LP, EM, MV) are spelled out in tab:scale_comparison, tab:entity_probes, etc.
- [FIXED] First "pp" usage in `introduction.tex` line 6 now expanded as "percentage point (pp)".

### 3. Cross-table 脚注
- [PASS] tab:scale_comparison caption already states: *"F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}"* — no addition needed.

### 4. Abstract word count
- Word count: **185 / 200** (under limit)

### 5. 匿名检查
- [PASS] No GitHub URLs (except anonymous-nlp-2026), no emails, no local paths, no university/department mentions, no "AutoDL", no self-citation markers in references.bib.

### 6. Bib 检查
- Undefined citations: 0
- Duplicate keys: 0
- 60 unique bib entries.

### Additional fixes applied
- **Few-NERD naming**: replaced 10 occurrences of "FewNERD" → "Few-NERD" in `sections/appendix.tex` (caption text and table rows).
- **WNUT-17 naming**: fixed 1 occurrence of bare "WNUT" → "WNUT-17" in training config table.
- **Synced** to anonymous repo (commit f803b24); recompiled successfully (0 errors, 8-page main text preserved).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "uuid": "d2c5b1f8-389e-4028-a406-7eb85087dfed",
  "message": {
    "model": "claude-opus-4-7",
    "id": "msg_01Qb85yBdJD5bvQzFfE65Qgn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 493,
      "cache_read_input_tokens": 120622,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 493
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

_source line 180_

## Final Polish Report

### 1. 编译验证
- Errors: 0
- Undefined refs: 0
- Main text pages: 8 (Limitations starts on page 8, References on page 9)
- Bib warnings: 0

### 2. Caption 检查
- [PASS] Captions are self-contained: model name (Qwen3-8B/LLaMA-3.1-8B), dataset, N, T, seed counts are stated; symbol abbreviations (VC, SJ, FK, LP, EM, MV) are spelled out in tab:scale_comparison, tab:entity_probes, etc.
- [FIXED] First "pp" usage in `introduction.tex` line 6 now expanded as "percentage point (pp)".

### 3. Cross-table 脚注
- [PASS] tab:scale_comparison caption already states: *"F1 values are entity-type-averaged macro-F1, which differs from the instance-averaged F1 in Table~\ref{tab:fewnerd}"* — no addition needed.

### 4. Abstract word count
- Word count: **185 / 200** (under limit)

### 5. 匿名检查
- [PASS] No GitHub URLs (except anonymous-nlp-2026), no emails, no local paths, no university/department mentions, no "AutoDL", no self-citation markers in references.bib.

### 6. Bib 检查
- Undefined citations: 0
- Duplicate keys: 0
- 60 unique bib entries.

### Additional fixes applied
- **Few-NERD naming**: replaced 10 occurrences of "FewNERD" → "Few-NERD" in `sections/appendix.tex` (caption text and table rows).
- **WNUT-17 naming**: fixed 1 occurrence of bare "WNUT" → "WNUT-17" in training config table.
- **Synced** to anonymous repo (commit f803b24); recompiled successfully (0 errors, 8-page main text preserved).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 388563,
  "duration_api_ms": 363878,
  "num_turns": 72,
  "stop_reason": "end_turn",
  "session_id": "56622092-b880-43f3-8cd7-2a5161528236",
  "total_cost_usd": 3.7508892500000006,
  "usage": {
    "input_tokens": 71,
    "cache_creation_input_tokens": 125551,
    "cache_read_input_tokens": 4944393,
    "output_tokens": 19640,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 125551,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 660,
        "cache_read_input_tokens": 120622,
        "cache_creation_input_tokens": 493,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 493
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2544,
      "outputTokens": 20,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.0026439999999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-7[1m]": {
      "inputTokens": 71,
      "outputTokens": 19640,
      "cacheReadInputTokens": 4944393,
      "cacheCreationInputTokens": 125551,
      "webSearchRequests": 0,
      "costUSD": 3.7482452500000005,
      "contextWindow": 1000000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b42c862f-308c-4053-a897-51fbb754a073"
}
```

</details>

---
