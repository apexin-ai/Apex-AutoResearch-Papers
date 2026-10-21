# paper page compress and hedge

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 128
- **Recorded user turns:** 1
- **Tool calls:** 43
- **Original source:** `logs/workers/worker_paper_page_compress_and_hedge_20260519T120340.log`
- **Structured JSON:** [`8b96c6757d7d0747b269.json`](../../sessions/8b/8b96c6757d7d0747b269.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
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
  "uuid": "6bcbfb53-4be7-4276-929b-55f1b9ebe0c0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779207000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "31828744-de55-45b6-99d0-b9ce49cb371f",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the paper files to understand the current state, then tackle both tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "8aad8adb-3c98-4d97-87f5-8a98596efacc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS9sq6BpCuuTTNPPM4furp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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

<details open><summary>🔧 Tool call — Agent · `toolu_01T5moRizawBLUddMZ7E7hS8`</summary>

```json
{
  "description": "Grep for sole/exclusive claims",
  "subagent_type": "Explore",
  "prompt": "Search for \"sole\" and \"exclusive\" in all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/. Show the matching lines with context (2 lines before and after). Also search for em-dash \"—\" and en-dash \" – \" patterns."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "c912d433-4993-4ae5-8292-b60c83af5ed0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS9sq6BpCuuTTNPPM4furp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "description": "Grep for sole/exclusive claims",
  "task_type": "local_agent",
  "prompt": "Search for \"sole\" and \"exclusive\" in all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/. Show the matching lines with context (2 lines before and after). Also search for em-dash \"—\" and en-dash \" – \" patterns.",
  "uuid": "0607b0cb-ee82-4f57-9232-d2bb3e1e9ff8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

## Round 1

122 recorded events

### User

_source line 7 · 2026-05-19T12:03:55.272Z_

Search for "sole" and "exclusive" in all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/. Show the matching lines with context (2 lines before and after). Also search for em-dash "—" and en-dash " – " patterns.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "21f8aa50-e80d-4b6e-8089-bad1420498b4"
}
```

</details>

---

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — Glob · `toolu_01CSSus5M7CFmyoQwcdC3Be7`</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "86667360-21ae-4ee9-899f-5dd304c082c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LS9sq6BpCuuTTNPPM4furp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12976,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12976
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

_source line 9 · 2026-05-19T12:03:55.516Z_

<details><summary>↩ Tool result · `toolu_01CSSus5M7CFmyoQwcdC3Be7`</summary>

```text
docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "0a4c4404-0553-4357-a570-cbaa876a09d2",
  "tool_use_result": {
    "filenames": [
      "docs/paper/corl_example.tex",
      "docs/paper/main.tex",
      "docs/paper/abstract.tex",
      "docs/paper/introduction.tex",
      "docs/paper/conclusion.tex",
      "docs/paper/method.tex",
      "docs/paper/discussion.tex",
      "docs/paper/experiments.tex",
      "docs/paper/appendix.tex",
      "docs/paper/related_work.tex"
    ],
    "durationMs": 18,
    "numFiles": 10,
    "truncated": false
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
  "subtype": "task_progress",
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "description": "Finding /home/ubuntu/.agent-ml-research-idea_gen_0509_15/…",
  "usage": {
    "total_tokens": 17849,
    "tool_uses": 1,
    "duration_ms": 1689
  },
  "last_tool_name": "Glob",
  "uuid": "bd264dad-fd8f-4fa0-93e4-f791d23805c8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_01NJ3tv5yuoprdG2h5LiyuCT`</summary>

```json
{
  "pattern": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/**/*.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "148a6bca-1c87-430b-8fda-87a69061e6f0",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbzwaH6xNvGB8jrBoPuxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17836,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17836,
        "ephemeral_1h_input_tokens": 0
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

_source line 12 · 2026-05-19T12:03:56.980Z_

<details><summary>↩ Tool result · `toolu_01NJ3tv5yuoprdG2h5LiyuCT`</summary>

```text
docs/paper/corl_example.tex
docs/paper/main.tex
docs/paper/abstract.tex
docs/paper/introduction.tex
docs/paper/conclusion.tex
docs/paper/method.tex
docs/paper/discussion.tex
docs/paper/experiments.tex
docs/paper/appendix.tex
docs/paper/related_work.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "b8ae3a45-3fe8-4633-8b25-7db4632c0956"
}
```

</details>

---

### System

_source line 13_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "description": "Searching for sole|exclusive",
  "usage": {
    "total_tokens": 17854,
    "tool_uses": 2,
    "duration_ms": 2146
  },
  "last_tool_name": "Grep",
  "uuid": "1b06b138-7f11-44ec-9968-9ec6e584160b",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Grep · `toolu_01JTgQkBEcmwzksUagDBfiLe`</summary>

```json
{
  "pattern": "sole|exclusive",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "68bf7987-a44e-47fa-b203-7f36b202c934",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbzwaH6xNvGB8jrBoPuxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17836,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17836,
        "ephemeral_1h_input_tokens": 0
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

_source line 15 · 2026-05-19T12:03:57.458Z_

<details><summary>↩ Tool result · `toolu_01JTgQkBEcmwzksUagDBfiLe`</summary>

```text
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-25-These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-26-The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
docs/paper/related_work.tex:27:Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-28-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-29-\paragraph{Token-level functional specialization in transformers.}
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-30-[Omitted long context line]
docs/paper/related_work.tex:31:We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-32-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex-33-\paragraph{Representation similarity and probing methodology.}
--
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-25-\paragraph{Readout token as multimodal hub.}
docs/paper/experiments.tex-26-Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
docs/paper/experiments.tex:27:The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-28-
/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex-29-\begin{table}[t]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "859549ff-245f-4547-b63f-0e94781170ff"
}
```

</details>

---

### System

_source line 16_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "description": "Searching for —",
  "usage": {
    "total_tokens": 17859,
    "tool_uses": 3,
    "duration_ms": 2550
  },
  "last_tool_name": "Grep",
  "uuid": "6f76c772-0e5b-4d14-854a-0d0ebe1a23f4",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_012FBHAKEwSUZXNrwVKzokuN`</summary>

```json
{
  "pattern": "—",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "d7e3a390-9558-4a2f-b3aa-a743fb999dc4",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbzwaH6xNvGB8jrBoPuxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17836,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17836,
        "ephemeral_1h_input_tokens": 0
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

_source line 18 · 2026-05-19T12:03:57.837Z_

<details><summary>↩ Tool result · `toolu_012FBHAKEwSUZXNrwVKzokuN`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "37a35099-ce41-44fb-8703-c6ad14298e95"
}
```

</details>

---

### System

_source line 19_

```json
{
  "type": "system",
  "subtype": "task_progress",
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "description": "Searching for  – ",
  "usage": {
    "total_tokens": 17864,
    "tool_uses": 4,
    "duration_ms": 2977
  },
  "last_tool_name": "Grep",
  "uuid": "67709212-ffd6-4c7d-8bfa-4aca7f970656",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_012bhkuDo1LTSXkRed4tAHoc`</summary>

```json
{
  "pattern": " – ",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
  "type": "tex",
  "output_mode": "content",
  "context": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "4938bb74-3503-49ae-a749-b8631effb164",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01JbzwaH6xNvGB8jrBoPuxrK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17836,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 17836,
        "ephemeral_1h_input_tokens": 0
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

_source line 21 · 2026-05-19T12:03:58.270Z_

<details><summary>↩ Tool result · `toolu_012bhkuDo1LTSXkRed4tAHoc`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "98a096dd-6d99-4b5e-a3f9-ba92c9c03825"
}
```

</details>

---

### System

_source line 22_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "a728162d83b3f87b9",
  "tool_use_id": "toolu_01T5moRizawBLUddMZ7E7hS8",
  "status": "completed",
  "output_file": "",
  "summary": "Grep for sole/exclusive claims",
  "usage": {
    "total_tokens": 20282,
    "tool_uses": 4,
    "duration_ms": 8965
  },
  "uuid": "408cdb86-d64e-455d-a3b0-3a565aa2891c",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool result

_source line 23 · 2026-05-19T12:04:04.240Z_

<details><summary>↩ Tool result · `toolu_01T5moRizawBLUddMZ7E7hS8`</summary>

````text
Perfect! Here are the search results for the specified terms in the .tex files:

## Matches for "sole" and "exclusive":

**File: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex**

Line 27:
```
Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
```

Line 31:
```
We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
```

**File: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex**

Line 27:
```
The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
```

## Dash patterns:

- **Em-dash "—"**: No matches found
- **En-dash " – "**: No matches found

The paper consistently uses "sole" and "exclusive" when describing the readout token's role as the primary multimodal integration point in the VLA architecture. No Unicode em-dashes or en-dashes were detected in the .tex files.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "48b32f9a-ad9c-4ba3-9fdb-e28f208b79fe",
  "tool_use_result": {
    "status": "completed",
    "prompt": "Search for \"sole\" and \"exclusive\" in all .tex files under /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/. Show the matching lines with context (2 lines before and after). Also search for em-dash \"—\" and en-dash \" – \" patterns.",
    "agentId": "a728162d83b3f87b9",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Here are the search results for the specified terms in the .tex files:\n\n## Matches for \"sole\" and \"exclusive\":\n\n**File: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex**\n\nLine 27:\n```\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n```\n\nLine 31:\n```\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n```\n\n**File: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex**\n\nLine 27:\n```\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n```\n\n## Dash patterns:\n\n- **Em-dash \"—\"**: No matches found\n- **En-dash \" – \"**: No matches found\n\nThe paper consistently uses \"sole\" and \"exclusive\" when describing the readout token's role as the primary multimodal integration point in the VLA architecture. No Unicode em-dashes or en-dashes were detected in the .tex files."
      }
    ],
    "totalDurationMs": 8967,
    "totalTokens": 20701,
    "totalToolUseCount": 4,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2413,
      "cache_read_input_tokens": 17836,
      "output_tokens": 445,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2413
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 445,
          "cache_read_input_tokens": 17836,
          "cache_creation_input_tokens": 2413,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2413,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 4,
      "bashCount": 0,
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

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Let me also check the abstract for "sole" and read the key files to understand the structure.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7dac9b0b-a3eb-443d-bca3-73f3d6d6fc72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 25_

Let me read all the key files to assess section lengths and find the remaining "sole" in abstract.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "c9acc224-9df6-42f9-8460-a072893ae3a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 26_

<details open><summary>🔧 Tool call — Read · `toolu_01NdVpW47Bo7GBrfZKrDoY4p`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7a6b3b03-3f4d-4aca-971b-e28bdae27f3f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 27 · 2026-05-19T12:04:08.292Z_

<details><summary>↩ Tool result · `toolu_01NdVpW47Bo7GBrfZKrDoY4p`</summary>

```text
1	Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.
2	We present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.
3	Three findings emerge.
4	First, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).
5	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
6	Second, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.
7	Architecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "8050a3d1-06f5-4551-b861-c170e293f415",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/abstract.tex",
      "content": "Vision-language-action models (VLAs) fine-tune large language models (LLMs) on robot demonstrations, but what fine-tuning changes at the representational level remains unclear.\nWe present a systematic framework for token-level analysis of VLAs, applying cross-instruction probes, attention analysis, Representational Similarity Analysis (RSA), and functional probes across all 32 LLM layers of OpenVLA-7B on LIBERO, with factorial trained/pretrained/untrained controls.\nThree findings emerge.\nFirst, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth, while VLA training shifts this to entry-layer routing (L0--L1) with exit-layer re-engagement (L31).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\nSecond, vision encoder representations show a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training effects concentrated at the readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry.\nArchitecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check.\n",
      "numLines": 8,
      "startLine": 1,
      "totalLines": 8
    }
  }
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — Read · `toolu_01HPqYGipRRwCUZkzUkhdtfv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "50eb4a0e-9d1d-47a4-98e2-ec782f0cee12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 29 · 2026-05-19T12:04:08.769Z_

<details><summary>↩ Tool result · `toolu_01HPqYGipRRwCUZkzUkhdtfv`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	While instruction tuning in NLP focuses on behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.
8	We test this assumption at the representational level through per-layer, per-token-type decomposition.
9	
10	\paragraph{Mechanistic interpretability in transformers.}
11	A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.
12	Elhage et al.~\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.
13	Building on this, Olsson et al.~\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.
14	Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\cite{wang2023_ioi} and greater-than comparison~\cite{conmy2023}.
15	Meng et al.~\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
16	Attention probing has shown that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}.
17	Michel et al.~\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.
18	Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.
19	
20	\paragraph{Behavioral and mechanistic analysis of VLAs.}
21	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
22	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
23	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
24	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
25	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
26	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
27	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
28	
29	\paragraph{Token-level functional specialization in transformers.}
30	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
31	We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.
32	
33	\paragraph{Representation similarity and probing methodology.}
34	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
35	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
36	We adopt RSA and MLP probes, with CKA in the appendix.
37	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7929da54-8d53-4169-be86-15e20b2812c7",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
      "numLines": 37,
      "startLine": 1,
      "totalLines": 37
    }
  }
}
```

</details>

---

### Tool call

_source line 30_

<details open><summary>🔧 Tool call — Read · `toolu_01HfB2dov7HfXrWuAsNjpgDB`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "b1e5b8a2-8d94-40af-9533-833cebfa411c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 31 · 2026-05-19T12:04:09.241Z_

<details><summary>↩ Tool result · `toolu_01HfB2dov7HfXrWuAsNjpgDB`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains the visual dominance of Grant et al.~\cite{grant2026}: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.
8	\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \to 0.64$; Figure~\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\ref{tab:counterfactual}).
9	\emph{Supporting}: (3)~attention gradient ($0 \to 9 \to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).
10	\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\times$; Table~\ref{tab:specificity_control}).
11	
12	\paragraph{Mechanistic interpretation.}
13	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.
14	The instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.
15	Counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
16	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
17	
18	\paragraph{Functional stages and predictions.}
19	The per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).
20	The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\S\ref{sec:learned_routing}).
21	This is an $N=2$ comparison (OpenVLA-7B vs.\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\ LIBERO 500 demonstrations) may also contribute to the L31 change.
22	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
23	
24	\paragraph{Task-dependent routing.}
25	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\ref{sec:task_complexity}).
26	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
27	
28	\paragraph{Limitations and scope.}
29	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
30	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
31	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "d37a6d60-72a2-42ed-8c15-c95d5206439a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
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

_source line 32_

<details open><summary>🔧 Tool call — Read · `toolu_015z9uraWoRr3wHPuoJJfSah`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7f964b24-eff7-4b67-b617-0afaabbf520e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 33 · 2026-05-19T12:04:09.715Z_

<details><summary>↩ Tool result · `toolu_015z9uraWoRr3wHPuoJJfSah`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	We evaluate OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each).
8	Representations are extracted from six sources spanning the VLA pipeline (\S\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\_mean and readout tokens at each of 32 layers, DINOv2~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), CLIP~\cite{radford2021_clip} (\texttt{patch\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).
9	Three LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\S\ref{sec:model_data}).
10	RSA computes Spearman $\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\S\ref{sec:rsa}).
11	MLP probes (input $\to$ 256 $\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\S\ref{sec:probes}).
12	This yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\text{eff} = 10$) and probes use demo-level train/test splits.
13	All patterns reproduce with a linear probe (Appendix~\ref{sec:linear_probe}).
14	
15	%------------------------------------------------------------------
16	\subsection{Framework Validation: Token-Level Specialization}
17	\label{sec:token_specialization}
18	
19	As a sanity check on the experimental framework, we train cross-instruction probes (\S\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.
20	
21	\paragraph{Image tokens are instruction-blind (expected).}
22	As predicted by the causal mask and frozen encoder, image\_mean instruction classification remains at chance ($10\%$) across all 32 layers in all conditions (Table~\ref{tab:dense_routing_main}).
23	Both linear and MLP probes corroborate this, as does standalone DINOv2 ($10\%$; Appendix~\ref{sec:instruction_invariance_appendix}).
24	
25	\paragraph{Readout token as multimodal hub.}
26	Trained readout achieves $100\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\ref{sec:loocv}); untrained achieves $100\%$ at L1 but decays to $82\%$ by L31.
27	The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\%$ vs.\ $82.7\%$; Appendix~\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\ref{sec:cross_benchmark_appendix}).
28	
29	\begin{table}[t]
30	\centering
31	\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\ref{sec:dense_routing}). Image\_mean remains at chance ($10\%$) in all conditions; trained readout reaches $100\%$ at L1 and holds; untrained readout decays from L1 to L31.}
32	\label{tab:dense_routing_main}
33	\small
34	\begin{tabular}{lccc}
35	\toprule
36	Layer & Trained readout & Untrained readout & Image\_mean \\
37	\midrule
38	L0 & 10.0\% & 10.0\% & 10.0\% \\
39	L1 & 100.0\% & 100.0\% & 10.0\% \\
40	L4 & 100.0\% & 99.1\% & 10.0\% \\
41	L8 & 100.0\% & 98.2\% & 10.0\% \\
42	L16 & 100.0\% & 92.3\% & 10.0\% \\
43	L31 & 100.0\% & 82.0\% & 10.0\% \\
44	\bottomrule
45	\end{tabular}
46	\end{table}
47	
48	%------------------------------------------------------------------
49	\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}
50	\label{sec:learned_routing}
51	
52	\paragraph{Three-level routing gradient at L1.}
53	L1 readout attention across three conditions (Table~\ref{tab:routing_gradient}; Figure~\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\%$ text); Llama-2 base 9/32 ($36.5\%$); VLA fine-tuning 24/32 ($57.7\%$), a redistribution beyond inherited priors.
54	Per-token normalization ($38.2\times$ text-to-image ratio; Appendix~\ref{sec:attention_decomp}) corroborates this redistribution.
55	
56	\paragraph{Redistribution of routing across depth.}
57	The 32-layer profile (Figure~\ref{fig:attention_profile}) shows qualitatively distinct patterns.
58	Llama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).
59	VLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).
60	Head counts reflect single-sample extraction; threshold sensitivity (30\%--70\%) analysis confirms ordering robustness across classification boundaries (Appendix~\ref{sec:threshold_sensitivity}).
61	
62	\paragraph{Task-specific sharpening.}
63	A fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.
64	Probe accuracy is preserved (L1: $99.7\%$; Appendix~\ref{app:finetuned_probe}).
65	
66	\paragraph{Probe robustness corroborates the pattern.}
67	Cross-instruction probes corroborate the three-condition gradient (Appendix Figure~\ref{fig:probe_conditions_appendix}).
68	Training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\_mean changes minimally ($\Delta \leq 1.7\%$; Appendix~\ref{sec:training_effect_summary},~\ref{sec:action_r2_threecond}).
69	
70	\paragraph{Open-loop functional sensitivity.}
71	We ablate attention to instruction tokens at the readout position.
72	Ablating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\footnote{$R^2$ values differ from Table~\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.
73	We compare against 10 random subsets of 24 heads (Appendix~\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \pm 0.013$ ($z = -2.73$, $p = 0.003$).
74	Dominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.
75	In the original extraction pipeline (\S\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\Delta \approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\ref{tab:per_task_r2}).
76	
77	\paragraph{Action trajectory validation.}
78	Ablating 24 instruction-dominant heads alters $72.3\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\%$), concentrated on the gripper dimension (shift $0.291$ vs.\ $< 0.034$; Tables~\ref{tab:attention_decomp},~\ref{tab:per_dim_mae}; Appendix~\ref{sec:action_trajectory}).
79	
80	\paragraph{Dose-response gradient.}
81	Ablating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \to 0.639$; Figure~\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\ref{sec:action_trajectory}).
82	
83	\paragraph{Counterfactual instruction analysis.}
84	Replacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\ref{tab:counterfactual}).
85	Token novelty ($1 - \text{Jaccard}$) predicts the ordering ($\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.
86	L1 ablation ($d = 0.65$) falls within this range (Appendix~\ref{sec:action_trajectory}).
87	
88	\begin{table}[t]
89	\centering
90	\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\% vs.\ 100.0\% in Table~\ref{tab:dense_routing_main}): task-level vs.\ LOOCV splits.}
91	\label{tab:routing_gradient}
92	\small
93	\begin{tabular}{lccccc}
94	\toprule
95	Condition & Heads & Text attn & L1 acc & L31 acc & Mode \\
96	\midrule
97	VLA Trained & 24/32 & 57.7\% & 99.6\% & 100.0\% & immed.+stable \\
98	Llama-2 base & 9/32 & 36.5\% & 80.2\% & 100.0\% & gradual+stable \\
99	Untrained & 0/32 & 11.7\% & 100.0\% & 82.0\% & incid.+forget \\
100	\bottomrule
101	\end{tabular}
102	\end{table}
103	
104	\begin{figure}[t]
105	\centering
106	\includegraphics[width=0.75\columnwidth]{figures/fig_32layer_attention.pdf}
107	\caption{Instruction-dominant heads ($>50\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\ref{fig:probe_conditions_appendix}.}
108	\label{fig:attention_profile}
109	\end{figure}
110	
111	%------------------------------------------------------------------
112	\subsection{Non-Monotonic Refinement of Vision Encoder Output}
113	\label{sec:nonmonotonic}
114	
115	\paragraph{Vision encoder provides geometric foundation.}
116	Table~\ref{tab:rsa_overview} reports RSA $\rho$ and probe $R^2$ between representations and actions.
117	DINOv2 \texttt{cls\_token} achieves the highest RSA ($\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\ref{sec:cka_appendix}).
118	
119	\paragraph{Middle-layer peak (metric-dependent).}
120	Under RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\_mean $\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).
121	The readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\Delta = 0.048$ (Table~\ref{tab:rsa_overview}).
122	Under linear CKA, this pattern disappears (monotonic increase; Appendix~\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.
123	
124	\paragraph{Training primarily enhances readout decodability.}
125	Best-vs-best RSA gain is non-significant on LIBERO-Goal ($\Delta\rho = 0.017$, $3\%$, $N{=}10$ tasks; Appendix Table~\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\Delta = +0.023$, $p < 0.001$; Appendix~\ref{sec:cross_benchmark_appendix}).
126	The $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.
127	Functional improvements are larger: readout $R^2$ $\Delta = +0.069$ ($p < 0.0001$, 95\% CI $[0.047, 0.090]$), image\_mean $\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.
128	
129	\begin{table}[t]
130	\centering
131	\caption{RSA $\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\ref{sec:cka_appendix}). VLA rows: peak values. \textbf{Bold}: best; \underline{underline}: second.}
132	\label{tab:rsa_overview}
133	\small
134	\begin{tabular}{lcccc}
135	\toprule
136	Source & RSA $\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\
137	\midrule
138	DINOv2 cls\_token & \textbf{0.692} & 0.634 & --- & --- \\
139	VLA Trained readout & \underline{0.643} & \textbf{0.678} & L12 & L13 \\
140	Fused DinoSigLIP & 0.634 & --- & --- & --- \\
141	VLA Trained image\_mean & 0.628 & \underline{0.655} & L12 & L8--L10$^\dagger$ \\
142	DinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\
143	VLA Untrained image\_mean & 0.612 & 0.640 & L0 & L0 \\
144	VLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\
145	CLIP ViT-L/14$^\ddagger$ & 0.557 & 0.587 & --- & --- \\
146	\bottomrule
147	\multicolumn{5}{l}{\footnotesize $^\dagger$$R^2$ peak region across 5 seeds ($0.655 \pm 0.002$; Appendix~\ref{sec:seed_sensitivity}).} \\
148	\multicolumn{5}{l}{\footnotesize $^\ddagger$RSA uses \texttt{patch\_mean}; $R^2$ uses \texttt{cls\_token} (each encoder's best aggregation).}
149	\end{tabular}
150	\end{table}
151	
152	\begin{figure}[t]
153	\centering
154	\includegraphics[width=0.92\columnwidth]{figures/fig3.pdf}
155	\caption{Per-layer RSA ($\rho$). Trained image\_mean follows an inverted-U (L0 $0.612 \to$ L12 $0.628 \to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}
156	\label{fig:layer_curves}
157	\end{figure}
158	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "eef5ade2-313a-408b-818c-86e240f0881d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nL1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
      "numLines": 158,
      "startLine": 1,
      "totalLines": 158
    }
  }
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_01VEtWDYmtDGPyj4hCkS5YyL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7ce320ed-90d6-4f8e-9b7a-863729ffa527",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 35 · 2026-05-19T12:04:10.248Z_

<details><summary>↩ Tool result · `toolu_01VEtWDYmtDGPyj4hCkS5YyL`</summary>

```text
1	\documentclass{article}
2	
3	\usepackage{corl_2026}
4	
5	\usepackage[utf8]{inputenc}
6	\usepackage[T1]{fontenc}
7	\usepackage{url}
8	\usepackage{booktabs}
9	\usepackage{amsfonts}
10	\usepackage{amsmath}
11	\usepackage{nicefrac}
12	\usepackage[expansion=false]{microtype}
13	\usepackage{graphicx}
14	\usepackage{enumitem}
15	
16	\title{Vision Encodes, Language Routes:\\ Token-Level Functional Specialization in a Vision-Language-Action Model}
17	
18	\author{Anonymous}
19	
20	\begin{document}
21	
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{discussion}
33	\input{conclusion}
34	
35	\bibliography{references}
36	
37	\input{appendix}
38	
39	\end{document}
40	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "ee694336-3a8a-4838-a4bd-9d421b716e21",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
      "content": "\\documentclass{article}\n\n\\usepackage{corl_2026}\n\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{url}\n\\usepackage{booktabs}\n\\usepackage{amsfonts}\n\\usepackage{amsmath}\n\\usepackage{nicefrac}\n\\usepackage[expansion=false]{microtype}\n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\n\\title{Vision Encodes, Language Routes:\\\\ Token-Level Functional Specialization in a Vision-Language-Action Model}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
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

_source line 36_

<details open><summary>🔧 Tool call — Read · `toolu_015hgGPaDXYXdzW3uifiWw8V`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "6d2d07ec-1fa4-48f0-9cee-90406ac68969",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 37 · 2026-05-19T12:04:10.714Z_

<details><summary>↩ Tool result · `toolu_015hgGPaDXYXdzW3uifiWw8V`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	What does fine-tuning change inside a Vision-Language-Action model (VLA)?
5	VLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.
6	Instruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.
7	
8	Recent behavioral studies reveal that VLAs rely disproportionately on visual input~\cite{grant2026}, with language instructions largely ignored by the action pathway~\cite{haon2025}.
9	These findings suggest internal specialization but do not explain \emph{how} instruction information reaches the action-generating readout token, \emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \emph{whether} training creates new representational structure or reconfigures inherited geometry.
10	Existing analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.
11	
12	We address this gap by decomposing OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\cite{touvron2023_llama2}.
13	We extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\cite{oquab2024_dinov2}, CLIP~\cite{radford2021_clip}).
14	We compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\cite{alain2017} for functional decodability.
15	
16	Three findings emerge from our analysis of OpenVLA-7B on LIBERO.
17	\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).
18	Seven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\times$ stronger for instruction-discriminative tasks ($p = 0.033$).
19	\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\ref{sec:cka_appendix}).
20	Training yields substantial functional improvement at the readout ($R^2$ $\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\Delta\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).
21	Architecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check (\S\ref{sec:token_specialization}).
22	
23	Our contributions are: (i)~evidence from seven complementary analyses that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub and routing dependence modulated by task instruction-discriminability; (ii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training primarily enhancing readout-token integration; and (iii)~a systematic framework for token-level representational analysis of VLAs with factorial controls.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1517133b-d12b-44c3-8bd5-2c0da8e3ba38",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/introduction.tex",
      "content": "\\section{Introduction}\n\\label{sec:introduction}\n\nWhat does fine-tuning change inside a Vision-Language-Action model (VLA)?\nVLAs fine-tune large language models on robot demonstrations to produce actions from visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla}, but the decoder-only causal mask prevents image tokens from attending to instructions.\nInstruction information must reach action-generating positions through learned attention routing, yet how fine-tuning reshapes this routing remains uncharacterized.\n\nRecent behavioral studies reveal that VLAs rely disproportionately on visual input~\\cite{grant2026}, with language instructions largely ignored by the action pathway~\\cite{haon2025}.\nThese findings suggest internal specialization but do not explain \\emph{how} instruction information reaches the action-generating readout token, \\emph{what} routing strategy fine-tuning learns compared to language pretraining alone, or \\emph{whether} training creates new representational structure or reconfigures inherited geometry.\nExisting analyses have not combined systematic per-layer probing with factorial trained/pretrained/untrained controls, leaving the representational mechanisms of VLA fine-tuning opaque.\n\nWe address this gap by decomposing OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, a VLA chaining a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2}, an MLP projector, and Llama-2 7B~\\cite{touvron2023_llama2}.\nWe extract representations from each of 32 LLM layers at both image-token and readout-token positions, and from external baselines (DINOv2~\\cite{oquab2024_dinov2}, CLIP~\\cite{radford2021_clip}).\nWe compare three LLM conditions (VLA-trained, pretrained Llama-2 base, and randomly initialized) crossed with instruction presence, and apply four complementary analyses: cross-instruction probes for token-level specialization, L1 attention pattern analysis for routing mechanisms, RSA~\\cite{kriegeskorte2008} for geometric alignment, and MLP probes~\\cite{alain2017} for functional decodability.\n\nThree findings emerge from our analysis of OpenVLA-7B on LIBERO.\n\\emph{First}, VLA fine-tuning front-loads instruction routing: language pretraining concentrates instruction attention at mid-depth (L9--L16, 15--22 heads), while VLA training shifts this to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18 heads).\nSeven complementary analyses, including dose-response ablation (8 conditions, monotonic $d = 0.48 \\to 0.64$) and counterfactual instruction analysis (4 perturbation types, $d = 0.63$--$0.97$), support instruction-conditioned action generation through distributed L1 routing, with routing dependence $2.5\\times$ stronger for instruction-discriminative tasks ($p = 0.033$).\n\\emph{Second}, under RSA and action-probe decodability, vision encoder representations show a middle-layer peak ($R^2$ at L8--L14, RSA at L12), but this pattern is metric-dependent (CKA diverges; Appendix~\\ref{sec:cka_appendix}).\nTraining yields substantial functional improvement at the readout ($R^2$ $\\Delta = +0.069$, $p < 0.0001$) with limited geometric gain ($\\Delta\\rho = 0.017$ on LIBERO-Goal; significant on LIBERO-Spatial, $p < 0.001$).\nArchitecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check (\\S\\ref{sec:token_specialization}).\n\nOur contributions are: (i)~evidence from seven complementary analyses that VLA fine-tuning front-loads instruction routing from mid-depth to entry-exit, with L1 as the primary routing hub and routing dependence modulated by task instruction-discriminability; (ii)~the observation that vision encoder representations follow a metric-dependent middle-layer peak (RSA/probes corroborate; CKA diverges), with training primarily enhancing readout-token integration; and (iii)~a systematic framework for token-level representational analysis of VLAs with factorial controls.\n",
      "numLines": 24,
      "startLine": 1,
      "totalLines": 24
    }
  }
}
```

</details>

---

### Tool call

_source line 38_

<details open><summary>🔧 Tool call — Read · `toolu_016qgjXaFa8ZbjwNhgGX7vvi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "51d2834c-cc2a-4c1a-a6af-a14d907a7e98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 39 · 2026-05-19T12:04:11.640Z_

<details><summary>↩ Tool result · `toolu_016qgjXaFa8ZbjwNhgGX7vvi`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.
5	
6	%------------------------------------------------------------------
7	\subsection{Model and Data}
8	\label{sec:model_data}
9	
10	We study OpenVLA-7B~\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\to$ 4{,}096-D), and Llama-2 7B~\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.
11	We use the base checkpoint pretrained on Open X-Embodiment~\cite{padalkar2023_oxe} (970K episodes spanning multiple robot platforms and task types) and evaluate on LIBERO-Goal~\cite{liu2023_libero} (10 tasks, 50 demonstrations each), which was not part of the pretraining mixture.
12	We compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \texttt{from\_config()}); a fourth condition (task-specific fine-tuning on LIBERO) is compared in \S\ref{sec:learned_routing}.
13	All three share the same frozen vision encoder and projector.
14	
15	%------------------------------------------------------------------
16	\subsection{Representation Extraction}
17	\label{sec:repr_extraction}
18	
19	We extract representations from six sources spanning the VLA pipeline:
20	(a)~\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;
21	(b)~\textbf{LLM image\_mean}, the mean image-token activation at each of 32 layers;
22	(c)~\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);
23	(d)~\textbf{DINOv2 ViT-L/14}~\cite{oquab2024_dinov2} (\texttt{cls\_token}/\texttt{patch\_mean}), a self-supervised baseline;
24	(e)~\textbf{CLIP ViT-L/14}~\cite{radford2021_clip} (\texttt{patch\_mean}), a VL-pretrained baseline;
25	(f)~\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.
26	Throughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.
27	We cross two factors: \emph{training status} (trained vs.\ untrained) and \emph{instruction presence} (with vs.\ without task description) in a $2\times 2$ factorial design.
28	
29	%------------------------------------------------------------------
30	\subsection{Cross-Instruction Probes}
31	\label{sec:cross_instruction_probes}
32	
33	To test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.
34	A linear classifier (10-way) is trained to identify which instruction was present, separately for image\_mean and readout token positions.
35	We validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to verify that results reflect generalizable instruction encoding rather than memorization.
36	
37	%------------------------------------------------------------------
38	\subsection{Attention Pattern Analysis}
39	\label{sec:attention_analysis}
40	
41	We analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.
42	This complements the cross-instruction probe by revealing the \emph{mechanism} through which instruction information reaches the readout token.
43	
44	%------------------------------------------------------------------
45	\subsection{Representational Similarity Analysis}
46	\label{sec:rsa}
47	
48	We adopt RSA~\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.
49	For each task, we compute pairwise $N \times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.
50	Alignment is measured via Spearman $\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\rho$ indicates that representationally similar observations require similar actions.
51	We report mean $\rho$ across 10 tasks with 95\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\cite{nili2014toolbox}.
52	
53	%------------------------------------------------------------------
54	\subsection{Functional Action Probes}
55	\label{sec:probes}
56	
57	RSA measures geometric alignment but not decodability.
58	We complement it with MLP probes~\cite{alain2017}: two-layer networks ($d_\text{in} \to 256 \to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\ 40--49).
59	We report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).
60	
61	\paragraph{Why RSA over CKA.}
62	RSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\ 7-D).
63	CKA~\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.
64	We report both in Appendix~\ref{sec:cka_appendix}; the divergence between metrics (\S\ref{sec:nonmonotonic}) indicates neither alone fully characterizes representational structure.
65	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "008519bf-aaa8-4646-b2b0-423f45a2fe44",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/method.tex",
      "content": "\\section{Method}\n\\label{sec:method}\n\nWe investigate how action-relevant structure is distributed across a VLA by combining four complementary analyses: cross-instruction probes, attention pattern analysis, RSA, and functional probes.\n\n%------------------------------------------------------------------\n\\subsection{Model and Data}\n\\label{sec:model_data}\n\nWe study OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024}, chaining a frozen DinoSigLIP vision backbone~\\cite{zhai2023_siglip,oquab2024_dinov2} (DINOv2 ViT-L/14 + SigLIP-SO400M), an MLP projector (2{,}176-D $\\to$ 4{,}096-D), and Llama-2 7B~\\cite{touvron2023_llama2} (6.74B parameters) that autoregressively decodes 7-D actions.\nWe use the base checkpoint pretrained on Open X-Embodiment~\\cite{padalkar2023_oxe} (970K episodes spanning multiple robot platforms and task types) and evaluate on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each), which was not part of the pretraining mixture.\nWe compare three LLM conditions: (1)~VLA-trained (released checkpoint), (2)~Llama-2 base (pretrained backbone, no VLA fine-tuning), and (3)~untrained (6.74B parameters reinitialized via \\texttt{from\\_config()}); a fourth condition (task-specific fine-tuning on LIBERO) is compared in \\S\\ref{sec:learned_routing}.\nAll three share the same frozen vision encoder and projector.\n\n%------------------------------------------------------------------\n\\subsection{Representation Extraction}\n\\label{sec:repr_extraction}\n\nWe extract representations from six sources spanning the VLA pipeline:\n(a)~\\textbf{DinoSigLIP+Projector}, the projector output (4{,}096-D), immediately before LLM processing;\n(b)~\\textbf{LLM image\\_mean}, the mean image-token activation at each of 32 layers;\n(c)~\\textbf{LLM readout}, the hidden state at the final pre-action token position at each layer (located after both image and instruction tokens in the causal sequence, it can attend to all preceding context and is thus the natural site for multimodal integration before action prediction);\n(d)~\\textbf{DINOv2 ViT-L/14}~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), a self-supervised baseline;\n(e)~\\textbf{CLIP ViT-L/14}~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), a VL-pretrained baseline;\n(f)~\\textbf{Branch-split}, the DINOv2 (1{,}024-D) and SigLIP (1{,}152-D) branches before fusion.\nThroughout, L0 denotes the embedding layer output, L1--L31 the 32 transformer layers, and L32 the output after the final layer norm.\nWe cross two factors: \\emph{training status} (trained vs.\\ untrained) and \\emph{instruction presence} (with vs.\\ without task description) in a $2\\times 2$ factorial design.\n\n%------------------------------------------------------------------\n\\subsection{Cross-Instruction Probes}\n\\label{sec:cross_instruction_probes}\n\nTo test whether different token types encode instruction identity, we construct a cross-instruction dataset: each visual frame is paired with all 10 task instructions, producing 10 representation vectors per frame per layer.\nA linear classifier (10-way) is trained to identify which instruction was present, separately for image\\_mean and readout token positions.\nWe validate with leave-one-out cross-validation (LOOCV) over 10 folds, each holding out one task's instructions, to verify that results reflect generalizable instruction encoding rather than memorization.\n\n%------------------------------------------------------------------\n\\subsection{Attention Pattern Analysis}\n\\label{sec:attention_analysis}\n\nWe analyze attention distributions at the readout token position across all 32 layers, categorizing each head as instruction-dominant ($>50\\%$ attention to instruction tokens) or image-dominant, with detailed per-head decomposition at L1.\nThis complements the cross-instruction probe by revealing the \\emph{mechanism} through which instruction information reaches the readout token.\n\n%------------------------------------------------------------------\n\\subsection{Representational Similarity Analysis}\n\\label{sec:rsa}\n\nWe adopt RSA~\\cite{kriegeskorte2008} to quantify geometric alignment between representations and the action space.\nFor each task, we compute pairwise $N \\times N$ representational dissimilarity matrices (RDMs) using cosine distances for representations and Euclidean distances for 7-D action vectors, using within-task observation pairs from 50 demonstrations.\nAlignment is measured via Spearman $\\rho$ between the upper-triangular entries of the representation and action RDMs; higher $\\rho$ indicates that representationally similar observations require similar actions.\nWe report mean $\\rho$ across 10 tasks with 95\\% confidence intervals from 10{,}000 bootstrap resamples; resampling is performed at the task level ($N=10$), treating each task's pairwise RDM entries as a block to preserve within-task dependency structure~\\cite{nili2014toolbox}.\n\n%------------------------------------------------------------------\n\\subsection{Functional Action Probes}\n\\label{sec:probes}\n\nRSA measures geometric alignment but not decodability.\nWe complement it with MLP probes~\\cite{alain2017}: two-layer networks ($d_\\text{in} \\to 256 \\to 7$) trained to predict 7-D action vectors from frozen representations (Adam, lr${}=10^{-3}$, batch 256, 50 epochs, early stopping patience 5), with demo-level train/test splits (demos 0--39 vs.\\ 40--49).\nWe report per-task macro-averaged $R^2$ across 10 tasks with bootstrap paired comparisons (10{,}000 resamples).\n\n\\paragraph{Why RSA over CKA.}\nRSA captures relative distance structure via scale-invariant Spearman rank correlation, suited to comparing high- and low-dimensional spaces (4{,}096-D vs.\\ 7-D).\nCKA~\\cite{kornblith2019} measures global subspace overlap, which can remain high even when geometric structure differs.\nWe report both in Appendix~\\ref{sec:cka_appendix}; the divergence between metrics (\\S\\ref{sec:nonmonotonic}) indicates neither alone fully characterizes representational structure.\n",
      "numLines": 65,
      "startLine": 1,
      "totalLines": 65
    }
  }
}
```

</details>

---

### Tool call

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_013F7QbghSa2BWCYJ9aRoYE2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "49e4607f-a188-47b8-9666-8e39bd26920f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LanMvELzMoEF5JHS21KNcV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 116,
      "cache_creation_input_tokens": 750,
      "cache_read_input_tokens": 24817,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 750
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

_source line 41 · 2026-05-19T12:04:11.714Z_

<details><summary>↩ Tool result · `toolu_013F7QbghSa2BWCYJ9aRoYE2`</summary>

```text
1	\paragraph{Conclusion.}
2	We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with L1 as the primary hub, supported by seven complementary analyses.
3	Code and data will be released upon acceptance.
4	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e41e4e9b-795f-41ae-b57e-9933c339deb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/conclusion.tex",
      "content": "\\paragraph{Conclusion.}\nWe find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with L1 as the primary hub, supported by seven complementary analyses.\nCode and data will be released upon acceptance.\n",
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
Now I have a good picture of all the files. Let me plan the work:

**Task 2 (Strong claims):** I need to change:
1. abstract.tex - I need to find "sole" in it. Looking at the abstract, I don't see "sole" directly. Let me re-read... Line 4 says "sole" isn't there. Wait, the user said abstract.tex:4. Let me check again... Line 6 says "readout token ($R^2$ $+0.069$, attention $+46$pp) rather than visual geometry." Line 7 says "Architecture-expected token specialization (instruction-blind image tokens, perfect readout classification from L1) is empirically verified as a framework sanity check."


I'm not finding "sole" in abstract.tex, so the line numbers must have shifted during the first task. Let me search for both "sole" and "exclusive" across the files to locate where these words actually appear.

From the search results, I can see three instances: "sole" appears in related_work.tex twice and experiments.tex once, while "exclusive" shows up in related_work.tex. There's nothing in abstract.tex, so I'm working with 3 instances total, not 4.

Now I need to think about Task 1 and which sections can be compressed to save space.  Related Work is 37 lines and Discussion is 32 lines—those are my main targets. Let me start making the edits for Task 2 first, then tackle the page compression by adjusting spacing and trimming verbose sections.

For the Related Work compression, I'm looking at a few key areas: that bridging sentence about instruction tuning could be tightened, and the Michel et al. citation about attention head pruning is doing too much work—I can fold that insight into the surrounding context more efficiently. Lines 13-18 are particularly dense and could be consolidated.

In the Discussion section, I'm noticing the Synthesis paragraph is largely restating what the experiments already showed, and the mechanistic interpretation part overlaps with that too. The functional stages paragraph is worth keeping but needs to be more concise.

For the actual implementation, I can adjust the LaTeX spacing parameters to reduce whitespace around floats and section headings without sacrificing readability. Let me compile the current version first to see where we stand on page count, then apply these targeted cuts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "ca43e52a-55d6-4629-95a7-56e4e62a0695",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 43_

Good, I have all the files. Let me first compile to check current page count, then make the edits.

"sole" appears in related_work.tex:27, related_work.tex:31 ("exclusive"), and experiments.tex:27. It does NOT appear in abstract.tex. I'll fix all 3 instances found.

Starting with Task 2 (claim hedging) and compilation in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "9e11cddc-c850-45fa-a857-b638784e8ae8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 44_

<details open><summary>🔧 Tool call — Bash · `toolu_016Q95GYBk59pFA51YBRFktd`</summary>

```json
{
  "command": "cd /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper && latexmk -pdf main.tex 2>&1 | tail -20",
  "description": "Compile paper to check current page count",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "228cd8f8-2428-47e5-9bb8-4ad384842cc6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 45 · 2026-05-19T12:04:43.911Z_

<details><summary>↩ Tool result · `toolu_016Q95GYBk59pFA51YBRFktd`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "2f02cc60-8bb9-4778-ae98-ec33b9972176",
  "tool_use_result": {
    "stdout": "Rc files read:\n  /etc/LatexMk\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'main.tex'.\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 46_

<details open><summary>🔧 Tool call — Edit · `toolu_011Qnj2sXSsdY1fHEoVviaPV`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "identify the readout token as the sole multimodal integration site",
  "new_string": "identify the readout token as the primary multimodal integration site"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "d10edf7a-7388-462a-b699-c8541cd8de49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 47 · 2026-05-19T12:04:44.967Z_

<details><summary>↩ Tool result · `toolu_011Qnj2sXSsdY1fHEoVviaPV`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "edd63779-b14a-495e-b62c-4ee4aa6222ae",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "identify the readout token as the sole multimodal integration site",
    "newString": "identify the readout token as the primary multimodal integration site",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.",
          " These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.",
          " The closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.",
          "-Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the sole multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
          "+Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
          " ",
          " \\paragraph{Token-level functional specialization in transformers.}",
          " In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs."
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

_source line 48_

<details open><summary>🔧 Tool call — Edit · `toolu_019xQNfrWmYFZuiE2aAP825Q`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "the readout token serves as the exclusive multimodal hub",
  "new_string": "the readout token serves as the primary multimodal hub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "eb2ddc5b-d300-4690-ab0e-ac141507d665",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 49 · 2026-05-19T12:04:45.997Z_

<details><summary>↩ Tool result · `toolu_019xQNfrWmYFZuiE2aAP825Q`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "27fd3f26-de94-4213-b88e-7191c24be5dc",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "the readout token serves as the exclusive multimodal hub",
    "newString": "the readout token serves as the primary multimodal hub",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 28,
        "oldLines": 7,
        "newStart": 28,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Token-level functional specialization in transformers.}",
          " In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.",
          "-We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the exclusive multimodal hub.",
          "+We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.",
          " ",
          " \\paragraph{Representation similarity and probing methodology.}",
          " RSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations."
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

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01JRxXQeXDsX7U7pMKJkaHu8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
  "old_string": "The readout is thus the sole locus of multimodal integration",
  "new_string": "The readout is thus the primary locus of multimodal integration"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "92bfe71a-d618-49e1-84ff-6d68a6693723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MeQrwCPdGmz45dXGA2sGZW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12347,
      "cache_read_input_tokens": 25567,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12347
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

_source line 51 · 2026-05-19T12:04:47.001Z_

<details><summary>↩ Tool result · `toolu_01JRxXQeXDsX7U7pMKJkaHu8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "f90d1f86-33cb-409f-90b8-275b915bd501",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/experiments.tex",
    "oldString": "The readout is thus the sole locus of multimodal integration",
    "newString": "The readout is thus the primary locus of multimodal integration",
    "originalFile": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\nWe evaluate OpenVLA-7B~\\cite{kim2024_openvla,karamcheti2024} on LIBERO-Goal~\\cite{liu2023_libero} (10 tasks, 50 demonstrations each).\nRepresentations are extracted from six sources spanning the VLA pipeline (\\S\\ref{sec:repr_extraction}): DinoSigLIP+Projector, LLM image\\_mean and readout tokens at each of 32 layers, DINOv2~\\cite{oquab2024_dinov2} (\\texttt{cls\\_token}/\\texttt{patch\\_mean}), CLIP~\\cite{radford2021_clip} (\\texttt{patch\\_mean}), and branch-split (DINOv2 1{,}024-D / SigLIP 1{,}152-D before fusion).\nThree LLM conditions are compared: VLA-trained, pretrained Llama-2 base (no VLA fine-tuning), and untrained (6.74B parameters reinitialized to random weights), crossed with instruction presence (\\S\\ref{sec:model_data}).\nRSA computes Spearman $\\rho$ between cosine-distance representation RDMs and Euclidean-distance action RDMs, with 10{,}000 bootstrap CIs (\\S\\ref{sec:rsa}).\nMLP probes (input $\\to$ 256 $\\to$ 7; Adam, lr${}=10^{-3}$, 50 epochs, early stopping) report mean $R^2$ (\\S\\ref{sec:probes}).\nThis yields $N = 63{,}228$ observations (after excluding terminal frames without next-action labels; $63{,}728$ total); RSA uses task-level blocking ($N_\\text{eff} = 10$) and probes use demo-level train/test splits.\nAll patterns reproduce with a linear probe (Appendix~\\ref{sec:linear_probe}).\n\n%------------------------------------------------------------------\n\\subsection{Framework Validation: Token-Level Specialization}\n\\label{sec:token_specialization}\n\nAs a sanity check on the experimental framework, we train cross-instruction probes (\\S\\ref{sec:cross_instruction_probes}): given the same visual frame with each of 10 task instructions, we classify which instruction was present from per-layer activations.\n\n\\paragraph{Image tokens are instruction-blind (expected).}\nAs predicted by the causal mask and frozen encoder, image\\_mean instruction classification remains at chance ($10\\%$) across all 32 layers in all conditions (Table~\\ref{tab:dense_routing_main}).\nBoth linear and MLP probes corroborate this, as does standalone DINOv2 ($10\\%$; Appendix~\\ref{sec:instruction_invariance_appendix}).\n\n\\paragraph{Readout token as multimodal hub.}\nTrained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.\nThe readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Cross-instruction 10-way classification at selected layers (full profile in Appendix~\\ref{sec:dense_routing}). Image\\_mean remains at chance ($10\\%$) in all conditions; trained readout reaches $100\\%$ at L1 and holds; untrained readout decays from L1 to L31.}\n\\label{tab:dense_routing_main}\n\\small\n\\begin{tabular}{lccc}\n\\toprule\nLayer & Trained readout & Untrained readout & Image\\_mean \\\\\n\\midrule\nL0 & 10.0\\% & 10.0\\% & 10.0\\% \\\\\nL1 & 100.0\\% & 100.0\\% & 10.0\\% \\\\\nL4 & 100.0\\% & 99.1\\% & 10.0\\% \\\\\nL8 & 100.0\\% & 98.2\\% & 10.0\\% \\\\\nL16 & 100.0\\% & 92.3\\% & 10.0\\% \\\\\nL31 & 100.0\\% & 82.0\\% & 10.0\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n%------------------------------------------------------------------\n\\subsection{VLA Fine-Tuning Front-Loads Instruction Routing}\n\\label{sec:learned_routing}\n\n\\paragraph{Three-level routing gradient at L1.}\nL1 readout attention across three conditions (Table~\\ref{tab:routing_gradient}; Figure~\\ref{fig:attention_profile}): untrained allocates 0/32 instruction-dominant heads ($11.7\\%$ text); Llama-2 base 9/32 ($36.5\\%$); VLA fine-tuning 24/32 ($57.7\\%$), a redistribution beyond inherited priors.\nPer-token normalization ($38.2\\times$ text-to-image ratio; Appendix~\\ref{sec:attention_decomp}) corroborates this redistribution.\n\n\\paragraph{Redistribution of routing across depth.}\nThe 32-layer profile (Figure~\\ref{fig:attention_profile}) shows qualitatively distinct patterns.\nLlama-2 base concentrates instruction attention at mid-depth (L9--L16: 15--22 heads).\nVLA fine-tuning shifts to an entry-exit pattern (L0--L1: 21--24 heads, L31: 18), with intermediate layers markedly lower (0--11 at L2--L30).\nHead counts reflect single-sample extraction; threshold sensitivity (30\\%--70\\%) analysis confirms ordering robustness across classification boundaries (Appendix~\\ref{sec:threshold_sensitivity}).\n\n\\paragraph{Task-specific sharpening.}\nA fourth condition (OpenVLA-7B fine-tuned on LIBERO) shows stable L1 entry routing (22/32 heads) but complete loss of L31 exit re-engagement (0 vs.\\ 18 heads) and further mid-depth compression (L9--L16: 1--7 vs.\\ 6--11), an $N=2$ comparison consistent with the hypothesis that exit routing serves multi-task flexibility, though training data diversity differences may also contribute.\nProbe accuracy is preserved (L1: $99.7\\%$; Appendix~\\ref{app:finetuned_probe}).\n\n\\paragraph{Probe robustness corroborates the pattern.}\nCross-instruction probes corroborate the three-condition gradient (Appendix Figure~\\ref{fig:probe_conditions_appendix}).\nTraining effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) while image\\_mean changes minimally ($\\Delta \\leq 1.7\\%$; Appendix~\\ref{sec:training_effect_summary},~\\ref{sec:action_r2_threecond}).\n\n\\paragraph{Open-loop functional sensitivity.}\nWe ablate attention to instruction tokens at the readout position.\nAblating all 24 dominant heads at L1 increases action $R^2$ by $+0.042$ (baseline $0.517$)\\footnote{$R^2$ values differ from Table~\\ref{tab:rsa_overview} due to the feature reconstruction pipeline; all comparisons are within-experiment.}.\nWe compare against 10 random subsets of 24 heads (Appendix~\\ref{sec:random_subset_ablation}): random ablation yields a larger mean increase of $+0.077 \\pm 0.013$ ($z = -2.73$, $p = 0.003$).\nDominant heads produce a smaller gain because they carry organized routing signals (structured noise for the probe); random heads lack such organization.\nIn the original extraction pipeline (\\S\\ref{sec:repr_extraction}), L1 ablation increases $R^2$ by $+0.059$ vs.\\ no-ablation baseline, decaying at deeper layers (L8: $+0.018$; L13: $\\Delta \\approx 0$); instruction routing is an entry-layer phenomenon, consistent across all 10 tasks (Table~\\ref{tab:per_task_r2}).\n\n\\paragraph{Action trajectory validation.}\nAblating 24 instruction-dominant heads alters $72.3\\%$ of action tokens ($d = 0.65$); control ablation (8 heads) yields $d = 0.41$ ($29.3\\%$), concentrated on the gripper dimension (shift $0.291$ vs.\\ $< 0.034$; Tables~\\ref{tab:attention_decomp},~\\ref{tab:per_dim_mae}; Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Dose-response gradient.}\nAblating 4--32 instruction-dominant heads yields monotonic divergence ($d = 0.482 \\to 0.639$; Figure~\\ref{fig:dose_response}), with steep rise through 12 heads and plateau beyond 20 (Appendix~\\ref{sec:action_trajectory}).\n\n\\paragraph{Counterfactual instruction analysis.}\nReplacing the original instruction with four perturbation types all produce substantial divergence: empty ($d = 0.968$), wrong task ($0.844$), paraphrased ($0.697$), shuffled ($0.625$; Table~\\ref{tab:counterfactual}).\nToken novelty ($1 - \\text{Jaccard}$) predicts the ordering ($\\rho = 1.0$): paraphrased (Jaccard $0.533$) exceeds shuffled (Jaccard $1.0$), though shuffled $d = 0.625$ with identical tokens reveals positional sensitivity.\nL1 ablation ($d = 0.65$) falls within this range (Appendix~\\ref{sec:action_trajectory}).\n\n\\begin{table}[t]\n\\centering\n\\caption{Instruction routing at L1. Mode: immed./gradual/incid. $=$ acquisition speed; +stable/+forget $=$ retention. Accuracy gap (99.6\\% vs.\\ 100.0\\% in Table~\\ref{tab:dense_routing_main}): task-level vs.\\ LOOCV splits.}\n\\label{tab:routing_gradient}\n\\small\n\\begin{tabular}{lccccc}\n\\toprule\nCondition & Heads & Text attn & L1 acc & L31 acc & Mode \\\\\n\\midrule\nVLA Trained & 24/32 & 57.7\\% & 99.6\\% & 100.0\\% & immed.+stable \\\\\nLlama-2 base & 9/32 & 36.5\\% & 80.2\\% & 100.0\\% & gradual+stable \\\\\nUntrained & 0/32 & 11.7\\% & 100.0\\% & 82.0\\% & incid.+forget \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.75\\columnwidth]{figures/fig_32layer_attention.pdf}\n\\caption{Instruction-dominant heads ($>50\\%$ text) across 32 layers. VLA-trained: entry-exit (L0--L1: 21--24, L31: 18); Llama-2 base: mid-depth (L9--L16: 15--22); untrained: zero. Probe accuracy in Appendix Figure~\\ref{fig:probe_conditions_appendix}.}\n\\label{fig:attention_profile}\n\\end{figure}\n\n%------------------------------------------------------------------\n\\subsection{Non-Monotonic Refinement of Vision Encoder Output}\n\\label{sec:nonmonotonic}\n\n\\paragraph{Vision encoder provides geometric foundation.}\nTable~\\ref{tab:rsa_overview} reports RSA $\\rho$ and probe $R^2$ between representations and actions.\nDINOv2 \\texttt{cls\\_token} achieves the highest RSA ($\\rho = 0.692$), exceeding the VLA peak ($0.628$ at L12) and CLIP ($0.557$); this ordering is metric-dependent (CKA reverses it; Appendix~\\ref{sec:cka_appendix}).\n\n\\paragraph{Middle-layer peak (metric-dependent).}\nUnder RSA and action-probe decodability, visual representations show a middle-layer peak: trained image\\_mean $\\rho$ is stable through L12 ($0.628$), then declines to $0.422$ at L32 (Figure~\\ref{fig:layer_curves}); probe $R^2$ peaks at L8--L10 ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).\nThe readout achieves $R^2 = 0.678$ (L13), exceeding the projector by $\\Delta = 0.048$ (Table~\\ref{tab:rsa_overview}).\nUnder linear CKA, this pattern disappears (monotonic increase; Appendix~\\ref{sec:cka_appendix}); the non-monotonic trajectory characterizes rank-order geometry specifically, not global covariance structure.\n\n\\paragraph{Training primarily enhances readout decodability.}\nBest-vs-best RSA gain is non-significant on LIBERO-Goal ($\\Delta\\rho = 0.017$, $3\\%$, $N{=}10$ tasks; Appendix Table~\\ref{tab:training_effects}), though LIBERO-Spatial yields a significant geometric gain ($\\Delta = +0.023$, $p < 0.001$; Appendix~\\ref{sec:cross_benchmark_appendix}).\nThe $N = 10$ instruction set limits statistical power for detecting small effects; non-significant differences should not be interpreted as evidence of absence.\nFunctional improvements are larger: readout $R^2$ $\\Delta = +0.069$ ($p < 0.0001$, 95\\% CI $[0.047, 0.090]$), image\\_mean $\\Delta = +0.015$ ($p = 0.006$), surviving FDR correction at 29--30/33 layers.\n\n\\begin{table}[t]\n\\centering\n\\caption{RSA $\\rho$ and probe $R^2$ alignment with actions. DINOv2 achieves highest RSA ($0.692$); ordering is metric-dependent (Appendix~\\ref{sec:cka_appendix}). VLA rows: peak values. \\textbf{Bold}: best; \\underline{underline}: second.}\n\\label{tab:rsa_overview}\n\\small\n\\begin{tabular}{lcccc}\n\\toprule\nSource & RSA $\\rho$ & $R^2$ & RSA Peak & $R^2$ Peak \\\\\n\\midrule\nDINOv2 cls\\_token & \\textbf{0.692} & 0.634 & --- & --- \\\\\nVLA Trained readout & \\underline{0.643} & \\textbf{0.678} & L12 & L13 \\\\\nFused DinoSigLIP & 0.634 & --- & --- & --- \\\\\nVLA Trained image\\_mean & 0.628 & \\underline{0.655} & L12 & L8--L10$^\\dagger$ \\\\\nDinoSigLIP+Projector & 0.615 & 0.630 & --- & --- \\\\\nVLA Untrained image\\_mean & 0.612 & 0.640 & L0 & L0 \\\\\nVLA Untrained readout & 0.626 & 0.609 & L1 & L32 \\\\\nCLIP ViT-L/14$^\\ddagger$ & 0.557 & 0.587 & --- & --- \\\\\n\\bottomrule\n\\multicolumn{5}{l}{\\footnotesize $^\\dagger$$R^2$ peak region across 5 seeds ($0.655 \\pm 0.002$; Appendix~\\ref{sec:seed_sensitivity}).} \\\\\n\\multicolumn{5}{l}{\\footnotesize $^\\ddagger$RSA uses \\texttt{patch\\_mean}; $R^2$ uses \\texttt{cls\\_token} (each encoder's best aggregation).}\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=0.92\\columnwidth]{figures/fig3.pdf}\n\\caption{Per-layer RSA ($\\rho$). Trained image\\_mean follows an inverted-U (L0 $0.612 \\to$ L12 $0.628 \\to$ L32 $0.422$); untrained decays monotonically. Dashed: DINOv2 cls ($0.692$), DinoSigLIP ($0.634$), Projector ($0.615$).}\n\\label{fig:layer_curves}\n\\end{figure}\n",
    "structuredPatch": [
      {
        "oldStart": 24,
        "oldLines": 7,
        "newStart": 24,
        "newLines": 7,
        "lines": [
          " ",
          " \\paragraph{Readout token as multimodal hub.}",
          " Trained readout achieves $100\\%$ 10-way classification from L1 through L31 (LOOCV-confirmed; Appendix~\\ref{sec:loocv}); untrained achieves $100\\%$ at L1 but decays to $82\\%$ by L31.",
          "-The readout is thus the sole locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).",
          "+The readout is thus the primary locus of multimodal integration, with richer task-relevant content than standalone DINOv2 (QA probe $86.3\\%$ vs.\\ $82.7\\%$; Appendix~\\ref{sec:qa_probe}), replicating on LIBERO-Spatial (Appendix~\\ref{sec:cross_benchmark_appendix}).",
          " ",
          " \\begin{table}[t]",
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

### Assistant

_source line 52_

Task 2 done (3 instances fixed). Let me check current page count from the existing PDF.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "3e545fb1-848b-4902-a921-d61152c581a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXtUti8SipZGp9BMtYEMhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 37914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2198
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

<details open><summary>🔧 Tool call — Bash · `toolu_01NW1SNuc9KGpZLLoDSZiwDt`</summary>

```json
{
  "command": "pdfinfo main.pdf 2>/dev/null | grep Pages || echo \"pdfinfo not available\"; python3 -c \"\nimport subprocess\nresult = subprocess.run(['pdftotext', 'main.pdf', '-'], capture_output=True, text=True)\ntext = result.stdout\n# Count pages by form feed\npages = text.count('\\f') + 1\nprint(f'Total pages: {pages}')\n\" 2>/dev/null || echo \"pdftotext not available\"",
  "description": "Check PDF page count"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "f289fc86-1a74-45c3-9d06-eab9f3c994c0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXtUti8SipZGp9BMtYEMhn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2198,
      "cache_read_input_tokens": 37914,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2198
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

_source line 54 · 2026-05-19T12:04:55.652Z_

<details><summary>↩ Tool result · `toolu_01NW1SNuc9KGpZLLoDSZiwDt`</summary>

```text
Pages:           28
Total pages: 29
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "52bd9ee6-4cb8-4460-8b29-872cb9d7168b",
  "tool_use_result": {
    "stdout": "Pages:           28\nTotal pages: 29",
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

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
28 pages total including appendix. I need to find where the main body ends (before \bibliography or \appendix). Let me look at the structure more carefully. The main content goes: abstract, introduction, related_work, method, experiments, discussion, conclusion, then bibliography, then appendix.

I need to check how many pages the body takes. Let me recompile and then check. But first, let me look at what's on pages 8-9 to understand where the page break falls.

Let me try extracting text from the PDF for specific pages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "377eac08-7f3d-41cd-b802-dc158e2fc2bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYZMDxRySk7m4GAA8EmeDn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 40112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

<details open><summary>🔧 Tool call — Bash · `toolu_01B1nQdZFpKkfVvC4HUdgwT3`</summary>

```json
{
  "command": "pdftotext -f 8 -l 10 main.pdf - 2>/dev/null | head -80",
  "description": "Check content around pages 8-10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "65c57561-49b4-4902-a88c-9d9cd52f72e9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YYZMDxRySk7m4GAA8EmeDn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 234,
      "cache_read_input_tokens": 40112,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 234
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

_source line 57 · 2026-05-19T12:05:02.471Z_

<details><summary>↩ Tool result · `toolu_01B1nQdZFpKkfVvC4HUdgwT3`</summary>

```text
DINOv2 cls (0.692)

RSA with Action Space ( )

0.70

Peak L12
(0.628)

0.65

Fused (0.634)
Proj (0.615)

0.60
0.55
0.50
0.45
Trained image_mean
Untrained image_mean

0.40
0

4

8

12

16

LLM Layer

20

24

28

32

Figure 2: Per-layer RSA (ρ). Trained image_mean follows an inverted-U (L0 0.612 → L12 0.628 →
L32 0.422); untrained decays monotonically. Dashed: DINOv2 cls (0.692), DinoSigLIP (0.634),
Projector (0.615).

262
263

264
265
266
267
268
269
270
271
272

273
274
275
276
277
278
279
280
281
282

283
284
285
286
287

(6) per-head bootstrap CIs (collective d: 0.65 vs. 0.41; p = 0.0018); (7) specificity control (1.08×;
Table 23).
Mechanistic interpretation. Matched-size ablation (d: instruction 0.65, random 0.60, image
0.58; Table 23) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "9b3fa3a6-ce64-4223-8adb-a79d57d4cef4",
  "tool_use_result": {
    "stdout": "DINOv2 cls (0.692)\n\nRSA with Action Space ( )\n\n0.70\n\nPeak L12\n(0.628)\n\n0.65\n\nFused (0.634)\nProj (0.615)\n\n0.60\n0.55\n0.50\n0.45\nTrained image_mean\nUntrained image_mean\n\n0.40\n0\n\n4\n\n8\n\n12\n\n16\n\nLLM Layer\n\n20\n\n24\n\n28\n\n32\n\nFigure 2: Per-layer RSA (ρ). Trained image_mean follows an inverted-U (L0 0.612 → L12 0.628 →\nL32 0.422); untrained decays monotonically. Dashed: DINOv2 cls (0.692), DinoSigLIP (0.634),\nProjector (0.615).\n\n262\n263\n\n264\n265\n266\n267\n268\n269\n270\n271\n272\n\n273\n274\n275\n276\n277\n278\n279\n280\n281\n282\n\n283\n284\n285\n286\n287\n\n(6) per-head bootstrap CIs (collective d: 0.65 vs. 0.41; p = 0.0018); (7) specificity control (1.08×;\nTable 23).\nMechanistic interpretation. Matched-size ablation (d: instruction 0.65, random 0.60, image\n0.58; Table 23) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed",
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

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01MgzjMLztdR7jgrYYGaWQMA`</summary>

```json
{
  "command": "pdftotext -f 9 -l 9 main.pdf - 2>/dev/null | head -60",
  "description": "Check page 9 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "b66890ea-2061-4e42-a485-43c19c157b42",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NSkf6HJmeyfMq531uDcd3E",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 617,
      "cache_read_input_tokens": 40346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 617
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-19T12:05:05.160Z_

<details><summary>↩ Tool result · `toolu_01MgzjMLztdR7jgrYYGaWQMA`</summary>

```text
288
289
290
291
292
293

Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K
episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural
constraints [1, 12, 50], but routing may differ across scales and paradigms (Appendix A.9, A.1).
Llama-2’s 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates
fine-tuning effects. All analyses are open-loop; our routing analysis (where) complements Häon et
al.’s [4] (what is encoded); closed-loop evaluation combining both is a natural extension.

296

Conclusion. We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with
L1 as the primary hub, supported by seven complementary analyses. Code and data will be released
upon acceptance.

297

References

294
295

298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "7145ac8b-1600-4b7f-bd3d-05f7ca026d90",
  "tool_use_result": {
    "stdout": "288\n289\n290\n291\n292\n293\n\nLimitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K\nepisodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural\nconstraints [1, 12, 50], but routing may differ across scales and paradigms (Appendix A.9, A.1).\nLlama-2’s 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates\nfine-tuning effects. All analyses are open-loop; our routing analysis (where) complements Häon et\nal.’s [4] (what is encoded); closed-loop evaluation combining both is a natural extension.\n\n296\n\nConclusion. We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with\nL1 as the primary hub, supported by seven complementary analyses. Code and data will be released\nupon acceptance.\n\n297\n\nReferences\n\n294\n295\n\n298\n299\n300\n301\n302\n303\n304\n305\n306\n307\n308\n309\n310\n311\n312\n313\n314\n315\n316\n317\n318\n319\n320\n321\n322\n323\n324\n325\n326\n327\n328\n329\n330",
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

_source line 60_

<details><summary>Logged reasoning block</summary>

```text
So page 9 has the end of Discussion (Limitations paragraph), Conclusion, and the beginning of References. The body text ends at the Conclusion paragraph, which is on page 9. I need to compress it to fit on page 8.

The Conclusion is only 3 lines, so I need to compress roughly a full page from the body. Let me think about the most effective strategies:

1. **LaTeX spacing tricks** - These are the easiest and least invasive
2. **Related Work compression** - Can tighten significantly 
3. **Discussion compression** - Can remove some repetition


I'll start by adjusting the LaTeX spacing parameters to reclaim space around floats and captions, then move into text compression if needed.

For the Related Work section, I'm thinking about merging some transitions more tightly and significantly condensing the mechanistic interpretability paragraph to cut down on redundancy. I need to save roughly a full page of content, so I'll be aggressive with both the spacing tweaks and the actual text editing.

In the Discussion section, I can tighten up the synthesis paragraph that recaps findings, and there's some overlap between the mechanistic interpretation paragraph and the experiments that I can streamline. The functional stages part is important but still has room to be more concise.

I should also look at the method section—it's running long at 65 lines, and that "Why RSA over CKA" explanation might be a good candidate for shortening.

My plan is to adjust the spacing commands in the main file, compress key paragraphs in related work and discussion, and potentially trim the method section justification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "64961155-7244-4a99-81ed-c213300181c9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAoeQvHmWF3SSgbEw6WQDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 40963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 409
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

_source line 61_

Page 9 has Discussion's "Limitations" paragraph, Conclusion, and start of References. I need to push Conclusion+References onto page 8. That requires ~1 page of savings.

Starting with LaTeX spacing tricks and text compression.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "73ef1c18-2fac-4d3e-b902-27ef2636e3e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAoeQvHmWF3SSgbEw6WQDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 40963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 409
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

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_0139kMbS2K1Hs9mWftp3sLoD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
  "old_string": "\\usepackage{enumitem}\n\n\\title",
  "new_string": "\\usepackage{enumitem}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "43c516e0-8afa-49e2-ad96-3b56815018e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LAoeQvHmWF3SSgbEw6WQDN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 409,
      "cache_read_input_tokens": 40963,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 409
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

_source line 63 · 2026-05-19T12:05:24.904Z_

<details><summary>↩ Tool result · `toolu_0139kMbS2K1Hs9mWftp3sLoD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "933ec121-5e6d-4b35-b4a5-a9818aa9460e",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/main.tex",
    "oldString": "\\usepackage{enumitem}\n\n\\title",
    "newString": "\\usepackage{enumitem}\n\n\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\intextsep}{8pt plus 2pt minus 2pt}\n\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}\n\\setlength{\\abovecaptionskip}{4pt}\n\\setlength{\\belowcaptionskip}{0pt}\n\n\\title",
    "originalFile": "\\documentclass{article}\n\n\\usepackage{corl_2026}\n\n\\usepackage[utf8]{inputenc}\n\\usepackage[T1]{fontenc}\n\\usepackage{url}\n\\usepackage{booktabs}\n\\usepackage{amsfonts}\n\\usepackage{amsmath}\n\\usepackage{nicefrac}\n\\usepackage[expansion=false]{microtype}\n\\usepackage{graphicx}\n\\usepackage{enumitem}\n\n\\title{Vision Encodes, Language Routes:\\\\ Token-Level Functional Specialization in a Vision-Language-Action Model}\n\n\\author{Anonymous}\n\n\\begin{document}\n\n\\maketitle\n\n\\begin{abstract}\n\\input{abstract}\n\\end{abstract}\n\n\\input{introduction}\n\\input{related_work}\n\\input{method}\n\\input{experiments}\n\\input{discussion}\n\\input{conclusion}\n\n\\bibliography{references}\n\n\\input{appendix}\n\n\\end{document}\n",
    "structuredPatch": [
      {
        "oldStart": 13,
        "oldLines": 6,
        "newStart": 13,
        "newLines": 12,
        "lines": [
          " \\usepackage{graphicx}",
          " \\usepackage{enumitem}",
          " ",
          "+\\setlength{\\textfloatsep}{8pt plus 2pt minus 4pt}",
          "+\\setlength{\\intextsep}{8pt plus 2pt minus 2pt}",
          "+\\setlength{\\floatsep}{8pt plus 2pt minus 4pt}",
          "+\\setlength{\\abovecaptionskip}{4pt}",
          "+\\setlength{\\belowcaptionskip}{0pt}",
          "+",
          " \\title{Vision Encodes, Language Routes:\\\\ Token-Level Functional Specialization in a Vision-Language-Action Model}",
          " ",
          " \\author{Anonymous}"
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

_source line 64_

Now compress Related Work. The Mechanistic interpretability paragraph is the longest and most compressible.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "12081d07-644a-46d5-919f-e18c09a1698c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01932ddfYfSLFntNMR58EsMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 41372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1261
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Edit · `toolu_017DbcvkVRRqggsgyQMzwJqc`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.",
  "new_string": "\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "aed84c7d-bced-4439-87ba-aa6f03de3e53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01932ddfYfSLFntNMR58EsMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1261,
      "cache_read_input_tokens": 41372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1261
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-19T12:05:43.215Z_

<details><summary>↩ Tool result · `toolu_017DbcvkVRRqggsgyQMzwJqc`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "840b4d7e-137f-4664-831b-8d5a6b34593a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.",
    "newString": "\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nA growing body of work analyzes transformer internals at the level of individual attention heads and circuits.\nElhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.\nBuilding on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.\nCircuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.\nMeng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.\nMichel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.\nOur Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 8,
        "oldLines": 14,
        "newStart": 8,
        "newLines": 9,
        "lines": [
          " We test this assumption at the representational level through per-layer, per-token-type decomposition.",
          " ",
          " \\paragraph{Mechanistic interpretability in transformers.}",
          "-A growing body of work analyzes transformer internals at the level of individual attention heads and circuits.",
          "-Elhage et al.~\\cite{elhage2021} introduced the residual stream framework, in which each layer reads from and writes to a shared communication channel.",
          "-Building on this, Olsson et al.~\\cite{olsson2022} identified induction heads as a mechanistic basis for in-context learning; these specialized attention heads implement token-copying algorithms.",
          "-Circuit-level analyses have since traced complete computational subgraphs for tasks such as indirect object identification~\\cite{wang2023_ioi} and greater-than comparison~\\cite{conmy2023}.",
          "-Meng et al.~\\cite{meng2022_rome} developed causal tracing for factual associations, Belrose et al.~\\cite{belrose2023_tunedlens} introduced the tuned lens for per-layer prediction, and feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
          "-Attention probing has shown that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}.",
          "-Michel et al.~\\cite{michel2019sixteen} showed that most attention heads can be pruned without performance loss; our dose-response analysis extends this to VLA instruction routing, finding that progressive head ablation yields monotonic rather than threshold-like effects.",
          "-Our Layer-1 attention head analysis extends this tradition to the VLA domain; unlike knowledge editing or prediction lens approaches, we use functional ablation to study task-specific routing and find that 24 of 32 heads become instruction-dominant after fine-tuning.",
          "+Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.",
          "+Attention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.",
          "+Our L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.",
          " ",
          " \\paragraph{Behavioral and mechanistic analysis of VLAs.}",
          " Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}."
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

_source line 67_

Now compress the VLA behavioral/mechanistic paragraph in Related Work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e466e826-b45c-4876-8ec1-0be3558296e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dWztSManyjLirhhxdASWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 41372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2178
      },
      "output_tokens": 4,
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

### Tool call

_source line 68_

<details open><summary>🔧 Tool call — Read · `toolu_012PsFp6bRju2xyn2kXbQfnh`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "f5d17989-b49d-4e6d-a284-5dfe4175ffa6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015dWztSManyjLirhhxdASWR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2178,
      "cache_read_input_tokens": 41372,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2178
      },
      "output_tokens": 4,
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

_source line 69 · 2026-05-19T12:05:46.101Z_

<details><summary>↩ Tool result · `toolu_012PsFp6bRju2xyn2kXbQfnh`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.
7	While instruction tuning in NLP focuses on behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.
8	We test this assumption at the representational level through per-layer, per-token-type decomposition.
9	
10	\paragraph{Mechanistic interpretability in transformers.}
11	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
12	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
13	Our L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.
14	
15	\paragraph{Behavioral and mechanistic analysis of VLAs.}
16	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
17	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
18	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
19	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
20	These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.
21	The closest work to ours is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.
22	Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.
23	
24	\paragraph{Token-level functional specialization in transformers.}
25	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
26	We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.
27	
28	\paragraph{Representation similarity and probing methodology.}
29	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
30	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
31	We adopt RSA and MLP probes, with CKA in the appendix.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "70613d99-2efb-4c0f-ae65-eb72e1386a94",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
      "numLines": 32,
      "startLine": 1,
      "totalLines": 32
    }
  }
}
```

</details>

---

### Assistant

_source line 70_

<details><summary>Logged reasoning block</summary>

```text
Good. Let me now compress more. I can:

1. Merge lines 7-8 in the VLA paragraph - they say similar things. "We study the representational mechanism..." and "We test this assumption..." are somewhat redundant.

2. The "Behavioral and mechanistic analysis of VLAs" paragraph (lines 15-22) could be tightened. Lines 20-22 specifically have a 3-item comparison that's verbose.

3. The "Token-level functional specialization" paragraph (lines 24-26) and the "Representation similarity" paragraph (lines 28-31) are relatively short already.


Now I'm looking at the Discussion section for compression opportunities. For the VLA paragraph, I can combine those opening lines about fine-tuning assumptions and representational testing into a single statement that contrasts with NLP instruction tuning while establishing the core claim about how action-relevant knowledge gets routed through the network.

For the Behavioral paragraph, that list of three respects is unnecessarily verbose—I should tighten it significantly. And the Synthesis paragraph is restating experimental findings in a way that's too drawn out, so I'll compress that down to the essential takeaways.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "9696cb10-06b7-44d9-9dd0-f19251202aa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1xfoX8Z71Bx6a8fGPUfA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 43550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1383
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

_source line 71_

Now compress the VLA paragraph (merge lines 6-8 into one sentence).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "9fb9f252-5bd1-4099-89d3-55a13074628c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1xfoX8Z71Bx6a8fGPUfA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 43550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1383
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

_source line 72_

<details open><summary>🔧 Tool call — Edit · `toolu_018a1TyCDK7uKiX7zRwW9XiU`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.",
  "new_string": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "379c72ed-99e5-4cd2-a4a2-4e35c739838a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P1xfoX8Z71Bx6a8fGPUfA4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1383,
      "cache_read_input_tokens": 43550,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1383
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

_source line 73 · 2026-05-19T12:05:57.613Z_

<details><summary>↩ Tool result · `toolu_018a1TyCDK7uKiX7zRwW9XiU`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "a6a425ac-0d1a-4b78-a692-5d9329fa8036",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.",
    "newString": "A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.\nWhile instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.\nWe test this assumption at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 3,
        "oldLines": 9,
        "newStart": 3,
        "newLines": 7,
        "lines": [
          " \\paragraph{Vision-language-action models.}",
          " VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.",
          " This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.",
          "-A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations.",
          "-While instruction tuning in NLP focuses on behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we study the representational mechanism by which instruction information is routed to action-generating positions.",
          "-We test this assumption at the representational level through per-layer, per-token-type decomposition.",
          "+A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.",
          " ",
          " \\paragraph{Mechanistic interpretability in transformers.}",
          " Mechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}."
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

_source line 74_

Compress the Behavioral/mechanistic paragraph: tighten the 3-item comparison and merge with the context.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1cdbfa4e-104a-4630-b5f7-b025576973e1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7c2iTKJyWE2wX21QmgECP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 44933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

_source line 75_

<details open><summary>🔧 Tool call — Edit · `toolu_01MapqgcrHu7ugkLyehPCJj4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
  "old_string": "Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
  "new_string": "Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThe closest work is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study and found visual dominance.\nWe differ by decomposing at the token level (identifying the readout as the primary integration site), tracking all 32 layers to reveal a non-monotonic profile, and including trained-vs-untrained factorial controls that isolate fine-tuning effects on attention routing."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "6d57487f-5a37-43c8-8950-c6b80488fa15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01D7c2iTKJyWE2wX21QmgECP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 44933,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 805
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

_source line 76 · 2026-05-19T12:06:04.487Z_

<details><summary>↩ Tool result · `toolu_01MapqgcrHu7ugkLyehPCJj4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e2f0a4c1-da2e-4c5f-b8c0-e7d25116b2c4",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
    "oldString": "Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
    "newString": "Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThe closest work is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study and found visual dominance.\nWe differ by decomposing at the token level (identifying the readout as the primary integration site), tracking all 32 layers to reveal a non-monotonic profile, and including trained-vs-untrained factorial controls that isolate fine-tuning effects on attention routing.",
    "originalFile": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThese studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.\nThe closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.\nOur work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
    "structuredPatch": [
      {
        "oldStart": 15,
        "oldLines": 9,
        "newStart": 15,
        "newLines": 8,
        "lines": [
          " At the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.",
          " Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.",
          " Fang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.",
          "-These studies analyze individual components or aggregate statistics; we provide a systematic per-layer decomposition with trained-vs-untrained controls absent from prior work.",
          "-The closest work to ours is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study of VLAs and found visual dominance in internal representations.",
          "-Our work differs in three respects: (1) we decompose at the token level rather than the feature level and identify the readout token as the primary multimodal integration site; (2) we track representations across all 32 layers and reveal a non-monotonic transformation profile invisible to whole-model analyses; and (3) we include trained-vs-untrained factorial controls that isolate the effect of fine-tuning on attention routing mechanisms.",
          "+The closest work is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study and found visual dominance.",
          "+We differ by decomposing at the token level (identifying the readout as the primary integration site), tracking all 32 layers to reveal a non-monotonic profile, and including trained-vs-untrained factorial controls that isolate fine-tuning effects on attention routing.",
          " ",
          " \\paragraph{Token-level functional specialization in transformers.}",
          " In Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs."
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

_source line 77_

Now compress Discussion. The Synthesis paragraph repeats experimental findings verbosely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "86f41251-6da9-4981-9dee-cafc3ee3043f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mzXvhpVvjbVNnf9nS8fhg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 45738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

<details open><summary>🔧 Tool call — Edit · `toolu_01LKz1DgPxkdvcV9h5Mq4qYo`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).",
  "new_string": "\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "a502485c-e795-471d-8965-f7ed732f5d60",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016mzXvhpVvjbVNnf9nS8fhg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 544,
      "cache_read_input_tokens": 45738,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 544
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

_source line 79 · 2026-05-19T12:06:24.583Z_

<details><summary>↩ Tool result · `toolu_01LKz1DgPxkdvcV9h5Mq4qYo`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "ad05ddc8-1cf8-4de4-8159-4532b88830bf",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).",
    "newString": "\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.\n\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).\n\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).\n\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 2,
        "oldLines": 12,
        "newStart": 2,
        "newLines": 9,
        "lines": [
          " \\label{sec:discussion}",
          " ",
          " \\paragraph{Synthesis.}",
          "-VLA fine-tuning primarily reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).",
          "-This explains the visual dominance of Grant et al.~\\cite{grant2026}: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).",
          "-Seven complementary analyses support instruction-conditioned action generation through distributed L1 routing, where instruction-attention fraction predicts per-head contribution magnitude.",
          "-\\emph{Interventional}: (1)~dose-response (8 conditions, $d = 0.48 \\to 0.64$; Figure~\\ref{fig:dose_response}); (2)~counterfactual analysis (4 perturbations, $d = 0.63$--$0.97$; Table~\\ref{tab:counterfactual}).",
          "-\\emph{Supporting}: (3)~attention gradient ($0 \\to 9 \\to 24$ heads); (4)~$R^2$ ablation gradient ($+0.059$ at L1); (5)~trajectory divergence ($d = 0.65$).",
          "-\\emph{Constraining}: (6)~per-head bootstrap CIs (collective $d$: $0.65$ vs.\\ $0.41$; $p = 0.0018$); (7)~specificity control ($1.08\\times$; Table~\\ref{tab:specificity_control}).",
          "+VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).",
          "+This explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).",
          "+Seven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).",
          " ",
          " \\paragraph{Mechanistic interpretation.}",
          " Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing."
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

_source line 80_

Now compress Discussion's Mechanistic interpretation paragraph.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "ced267d7-782c-4f8b-9e00-dcce2b7d3311",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES7sW9bsEHqacg2nMVTkWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 46282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1005
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

_source line 81_

<details open><summary>🔧 Tool call — Edit · `toolu_01K6x57jCKAaLHPup4XHoUcK`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
  "new_string": "\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1cc6f27a-2d11-4da9-a5a8-ddcd26f2da72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ES7sW9bsEHqacg2nMVTkWD",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1005,
      "cache_read_input_tokens": 46282,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1005
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

_source line 82 · 2026-05-19T12:06:39.631Z_

<details><summary>↩ Tool result · `toolu_01K6x57jCKAaLHPup4XHoUcK`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "fd8e8694-c571-4722-96df-2fd8d735d69d",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
    "newString": "\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.\nThe instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 7,
        "oldLines": 8,
        "newStart": 7,
        "newLines": 7,
        "lines": [
          " Seven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).",
          " ",
          " \\paragraph{Mechanistic interpretation.}",
          "-Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing.",
          "-The instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds); the modest magnitude supports distributed rather than dedicated routing.",
          "+Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).",
          " Counterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).",
          " That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
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

### Assistant

_source line 83_

Now compress the Functional stages paragraph in Discussion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "6c04395a-58d0-4dfc-b804-3ed8db4e3577",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DM73AU29VimetYoZXQ4igf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 47287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 753
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

_source line 84_

<details open><summary>🔧 Tool call — Edit · `toolu_0116W4GmHmRUrwLqFri44ykT`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
  "old_string": "\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
  "new_string": "\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "af253453-70f7-40c7-a8a7-5094389a50ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DM73AU29VimetYoZXQ4igf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 753,
      "cache_read_input_tokens": 47287,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 753
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

_source line 85 · 2026-05-19T12:06:58.681Z_

<details><summary>↩ Tool result · `toolu_0116W4GmHmRUrwLqFri44ykT`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "db828245-2178-4c3a-98fc-4a8eca7bb16f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
    "oldString": "\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
    "newString": "\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
    "originalFile": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nThe per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).\nThe entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).\nThis is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
    "structuredPatch": [
      {
        "oldStart": 12,
        "oldLines": 9,
        "newStart": 12,
        "newLines": 8,
        "lines": [
          " That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.",
          " ",
          " \\paragraph{Functional stages and predictions.}",
          "-The per-layer profiles suggest three functional stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; both $R^2$ and RSA decline, suggesting pruning potential).",
          "-The entry-exit pattern characterizes general VLA training; task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads), consistent with the hypothesis that exit routing serves multi-task flexibility (\\S\\ref{sec:learned_routing}).",
          "-This is an $N=2$ comparison (OpenVLA-7B vs.\\ LIBERO-finetuned); differences in training data diversity (OXE 970K episodes vs.\\ LIBERO 500 demonstrations) may also contribute to the L31 change.",
          "+Per-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).",
          "+Task-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.",
          " Predictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.",
          " ",
          " \\paragraph{Task-dependent routing.}"
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

Now compile to check progress.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "5cc607c4-7bf8-4b8c-9f11-31346181e700",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj1j5HXF4upqQbnUXxCfLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 48040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 808
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

_source line 87_

<details open><summary>🔧 Tool call — Bash · `toolu_01Smf7q4JVatVcgxhbLkvzrG`</summary>

```json
{
  "command": "latexmk -pdf main.tex 2>&1 | tail -5",
  "description": "Recompile paper",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "824ee049-2b26-4d09-9006-3fe600886ee0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uj1j5HXF4upqQbnUXxCfLW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 48040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 808
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

_source line 88 · 2026-05-19T12:07:04.730Z_

<details><summary>↩ Tool result · `toolu_01Smf7q4JVatVcgxhbLkvzrG`</summary>

```text
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "b6081bd0-4e8a-40d2-9447-695d7dcc09b6",
  "tool_use_result": {
    "stdout": "  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 89_

<details open><summary>🔧 Tool call — Bash · `toolu_018rQwuwsP9koNXhYzs1armV`</summary>

```json
{
  "command": "latexmk -pdf -f main.tex 2>&1 | tail -10",
  "description": "Force recompile paper",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "8efe493a-c04e-40b3-9e21-f2b9f45d8acc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KU9duxUYrU4KsXbKUngXht",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 187,
      "cache_read_input_tokens": 48848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 187
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

_source line 90 · 2026-05-19T12:07:07.748Z_

<details><summary>↩ Tool result · `toolu_018rQwuwsP9koNXhYzs1armV`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: Nothing to do for 'main.tex'.
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "c22b9c2e-e7f4-46cb-8a8b-c172bc347212",
  "tool_use_result": {
    "stdout": "Rc files read:\n  /etc/LatexMk\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Nothing to do for 'main.tex'.\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 91_

<details open><summary>🔧 Tool call — Bash · `toolu_01T5S61pCk7ijYUC6WrYmTyc`</summary>

```json
{
  "command": "rm -f main.aux main.fls main.fdb_latexmk && latexmk -pdf main.tex 2>&1 | tail -15",
  "description": "Force clean recompile",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "df3354e5-3465-488f-8794-ffcdccfeb815",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013yR8GBBggPRANKEXedEdPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 206,
      "cache_read_input_tokens": 49035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 206
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": {
      "cache_miss_reason": {
        "type": "unavailable"
      }
    },
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 92 · 2026-05-19T12:07:11.353Z_

<details><summary>↩ Tool result · `toolu_01T5S61pCk7ijYUC6WrYmTyc`</summary>

```text
The top-level auxiliary file: main.aux
I found no \citation commands---while reading file main.aux
I found no \bibdata command---while reading file main.aux
I found no \bibstyle command---while reading file main.aux
(There were 3 error messages)
Latexmk: Errors, so I did not complete making targets
Collected error summary (may duplicate other messages):
  bibtex main: Bibtex errors: See file 'main.blg'

Latexmk: Sometimes, the -f option can be used to get latexmk
  to try to force complete processing.
  But normally, you will need to correct the file(s) that caused the
  error, and then rerun latexmk.
  In some cases, it is best to clean out generated files before rerunning
  latexmk after you've corrected the files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "bd9d5f45-35f0-4e75-907d-db5199b6f3e0",
  "tool_use_result": {
    "stdout": "The top-level auxiliary file: main.aux\nI found no \\citation commands---while reading file main.aux\nI found no \\bibdata command---while reading file main.aux\nI found no \\bibstyle command---while reading file main.aux\n(There were 3 error messages)\nLatexmk: Errors, so I did not complete making targets\nCollected error summary (may duplicate other messages):\n  bibtex main: Bibtex errors: See file 'main.blg'\n\nLatexmk: Sometimes, the -f option can be used to get latexmk\n  to try to force complete processing.\n  But normally, you will need to correct the file(s) that caused the\n  error, and then rerun latexmk.\n  In some cases, it is best to clean out generated files before rerunning\n  latexmk after you've corrected the files.",
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

_source line 93_

<details open><summary>🔧 Tool call — Bash · `toolu_0122mBNrmxtA8ipfZpHAwAkW`</summary>

```json
{
  "command": "latexmk -C main.tex 2>&1; latexmk -pdf main.tex 2>&1 | tail -10",
  "description": "Clean build and recompile",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "22d1eda5-9f8a-4608-bfb9-3e80874a947c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToXo4aNPP3mFs29zuZyq3o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 554,
      "cache_read_input_tokens": 49035,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 554
      },
      "output_tokens": 44,
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

### System

_source line 94_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "byc7c8jth",
  "tool_use_id": "toolu_0122mBNrmxtA8ipfZpHAwAkW",
  "description": "Clean build and recompile",
  "task_type": "local_bash",
  "uuid": "e78ce06b-949e-496b-858b-6db8f07a640b",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### System

_source line 95_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "byc7c8jth",
  "tool_use_id": "toolu_0122mBNrmxtA8ipfZpHAwAkW",
  "status": "completed",
  "output_file": "",
  "summary": "Clean build and recompile",
  "uuid": "aeed7eb4-7299-4448-9786-afa0369bb912",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool result

_source line 96 · 2026-05-19T12:07:19.108Z_

<details><summary>↩ Tool result · `toolu_0122mBNrmxtA8ipfZpHAwAkW`</summary>

```text
Rc files read:
  /etc/LatexMk
Latexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.
Latexmk: Doing full clean up for 'main.tex'

Latexmk: Examining 'main.fls'
Latexmk: Examining 'main.log'
Latexmk: Found input bbl file 'main.bbl'
Latexmk: Log file says output to 'main.pdf'
Latexmk: Using bibtex to make bibliography file(s).
  ===Source file 'main.bbl' for 'pdflatex'
Latexmk: Found bibliography file(s):
  ./references.bib
Latexmk: All targets (main.pdf) are up-to-date
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1fac85cc-4b3a-4422-ad14-b52b940493e0",
  "tool_use_result": {
    "stdout": "Rc files read:\n  /etc/LatexMk\nLatexmk: This is Latexmk, John Collins, 15 June 2025. Version 4.87.\nLatexmk: Doing full clean up for 'main.tex'\n\nLatexmk: Examining 'main.fls'\nLatexmk: Examining 'main.log'\nLatexmk: Found input bbl file 'main.bbl'\nLatexmk: Log file says output to 'main.pdf'\nLatexmk: Using bibtex to make bibliography file(s).\n  ===Source file 'main.bbl' for 'pdflatex'\nLatexmk: Found bibliography file(s):\n  ./references.bib\nLatexmk: All targets (main.pdf) are up-to-date",
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

_source line 97_

<details open><summary>🔧 Tool call — Bash · `toolu_01QYL5Q11TPgFa9Re5wT6BNj`</summary>

```json
{
  "command": "pdflatex main.tex 2>&1 | tail -15 && bibtex main 2>&1 | tail -5 && pdflatex main.tex 2>&1 | tail -5 && pdflatex main.tex 2>&1 | tail -5",
  "description": "Manual compilation sequence",
  "timeout": 120000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "c4c7b8e3-9961-46d9-b592-abf982d3f0dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MScK4w9qvTAW3gTkDpcVRc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 348,
      "cache_read_input_tokens": 49589,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 348
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

_source line 98_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bw9lr79a5",
  "tool_use_id": "toolu_01QYL5Q11TPgFa9Re5wT6BNj",
  "description": "Manual compilation sequence",
  "task_type": "local_bash",
  "uuid": "0e0d848b-075a-47df-adf7-217d26c31bd8",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### System

_source line 99_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bw9lr79a5",
  "tool_use_id": "toolu_01QYL5Q11TPgFa9Re5wT6BNj",
  "status": "completed",
  "output_file": "",
  "summary": "Manual compilation sequence",
  "uuid": "9938b73e-3fd9-413a-ac3b-e696a5f50f06",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e"
}
```

---

### Tool result

_source line 100 · 2026-05-19T12:07:26.999Z_

<details><summary>↩ Tool result · `toolu_01QYL5Q11TPgFa9Re5wT6BNj`</summary>

```text
mf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis
t/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts
/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/
public/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a
msfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/
cm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1
0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><
/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh
are/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex
live/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 563910 bytes).
Transcript written on main.log.
This is BibTeX, Version 0.99d (TeX Live 2025/Debian)
The top-level auxiliary file: main.aux
The style file: corlabbrvnat.bst
Database file #1: references.bib
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 563910 bytes).
Transcript written on main.log.
ist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1
/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr
i8a.pfb>
Output written on main.pdf (27 pages, 563910 bytes).
Transcript written on main.log.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "12130c71-e901-49e0-b614-10f91b1ae4a3",
  "tool_use_result": {
    "stdout": "mf-dist/fonts/type1/public/amsfonts/cm/cmmi10.pfb>&lt;/usr/share/texlive/texmf-dis\nt/fonts/type1/public/amsfonts/cm/cmmi9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts\n/type1/public/amsfonts/cm/cmr10.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/\npublic/amsfonts/cm/cmr6.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/a\nmsfonts/cm/cmr7.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/\ncm/cmr9.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy1\n0.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy6.pfb><\n/usr/share/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy7.pfb>&lt;/usr/sh\nare/texlive/texmf-dist/fonts/type1/public/amsfonts/cm/cmsy9.pfb>&lt;/usr/share/tex\nlive/texmf-dist/fonts/type1/urw/helvetic/uhvr8a.pfb>&lt;/usr/share/texlive/texmf-d\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 563910 bytes).\nTranscript written on main.log.\nThis is BibTeX, Version 0.99d (TeX Live 2025/Debian)\nThe top-level auxiliary file: main.aux\nThe style file: corlabbrvnat.bst\nDatabase file #1: references.bib\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 563910 bytes).\nTranscript written on main.log.\nist/fonts/type1/urw/times/utmb8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1\n/urw/times/utmr8a.pfb>&lt;/usr/share/texlive/texmf-dist/fonts/type1/urw/times/utmr\ni8a.pfb>\nOutput written on main.pdf (27 pages, 563910 bytes).\nTranscript written on main.log.",
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

_source line 101_

<details><summary>Logged reasoning block</summary>

```text
Good, the paper compiled to 27 pages (down from 28). Let me check what's on pages 8-9 now to see where the body ends.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e48fe9e2-d725-4ff5-b656-7472d77f6d41",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCWRyp7rwM44LaKi7SMjvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 49937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1082
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

_source line 102_

Compiled: 27 pages (down from 28). Let me check where the body ends now.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1344ce0b-4893-456b-aa76-12c51e6128a9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCWRyp7rwM44LaKi7SMjvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 49937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1082
      },
      "output_tokens": 13,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — Bash · `toolu_015ALdY5wwtMy9EX6EUHT7kU`</summary>

```json
{
  "command": "pdftotext -f 8 -l 9 main.pdf - 2>/dev/null | head -80",
  "description": "Check pages 8-9 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "1731375e-ad51-4a5f-98f0-b97131c541b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCWRyp7rwM44LaKi7SMjvP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1082,
      "cache_read_input_tokens": 49937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1082
      },
      "output_tokens": 13,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 104 · 2026-05-19T12:07:31.410Z_

<details><summary>↩ Tool result · `toolu_015ALdY5wwtMy9EX6EUHT7kU`</summary>

```text
DINOv2 cls (0.692)

RSA with Action Space ( )

0.70

Peak L12
(0.628)

0.65

Fused (0.634)
Proj (0.615)

0.60
0.55
0.50
0.45
Trained image_mean
Untrained image_mean

0.40
0

4

8

12

16

LLM Layer

20

24

28

32

Figure 2: Per-layer RSA (ρ). Trained image_mean follows an inverted-U (L0 0.612 → L12 0.628 →
L32 0.422); untrained decays monotonically. Dashed: DINOv2 cls (0.692), DinoSigLIP (0.634),
Projector (0.615).
257
258
259
260
261
262
263
264

265
266
267
268
269

270
271
272
273
274
275

Functional stages and predictions. Per-layer profiles suggest three stages: routing (L0–L1; probe
99.6%, 24/32 instruction-dominant heads), computation (L8–L13; R2 peak 0.655–0.678), and decay
(L14–L32, ∼56% of parameters; declining R2 and RSA suggest pruning potential). Task-specific
fine-tuning eliminates L31 re-engagement (18 → 0 heads; §4.3), consistent with exit routing serving
multi-task flexibility, though this N = 2 comparison (OXE 970K vs. LIBERO 500) may also reflect
data diversity differences. Predictions: cross-attention VLAs (π0 [12], Octo [50]) should lack L1
routing heads; decoder-only VLAs (RT-2 [1]) should show similar routing; larger VLAs should yield
flatter per-head contributions.
Task-dependent routing. The routing effect is task-dependent: instruction-discriminative tasks
show 2.5× larger |∆R2 | under L1 ablation than visually-sufficient tasks (p = 0.033; Table 22), rising to 6.5× (p = 0.008) under a stricter criterion; no single task drives the effect (Appendix A.22).
For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K
episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e92b7b37-2185-4249-98b1-e74261193ecf",
  "tool_use_result": {
    "stdout": "DINOv2 cls (0.692)\n\nRSA with Action Space ( )\n\n0.70\n\nPeak L12\n(0.628)\n\n0.65\n\nFused (0.634)\nProj (0.615)\n\n0.60\n0.55\n0.50\n0.45\nTrained image_mean\nUntrained image_mean\n\n0.40\n0\n\n4\n\n8\n\n12\n\n16\n\nLLM Layer\n\n20\n\n24\n\n28\n\n32\n\nFigure 2: Per-layer RSA (ρ). Trained image_mean follows an inverted-U (L0 0.612 → L12 0.628 →\nL32 0.422); untrained decays monotonically. Dashed: DINOv2 cls (0.692), DinoSigLIP (0.634),\nProjector (0.615).\n257\n258\n259\n260\n261\n262\n263\n264\n\n265\n266\n267\n268\n269\n\n270\n271\n272\n273\n274\n275\n\nFunctional stages and predictions. Per-layer profiles suggest three stages: routing (L0–L1; probe\n99.6%, 24/32 instruction-dominant heads), computation (L8–L13; R2 peak 0.655–0.678), and decay\n(L14–L32, ∼56% of parameters; declining R2 and RSA suggest pruning potential). Task-specific\nfine-tuning eliminates L31 re-engagement (18 → 0 heads; §4.3), consistent with exit routing serving\nmulti-task flexibility, though this N = 2 comparison (OXE 970K vs. LIBERO 500) may also reflect\ndata diversity differences. Predictions: cross-attention VLAs (π0 [12], Octo [50]) should lack L1\nrouting heads; decoder-only VLAs (RT-2 [1]) should show similar routing; larger VLAs should yield\nflatter per-head contributions.\nTask-dependent routing. The routing effect is task-dependent: instruction-discriminative tasks\nshow 2.5× larger |∆R2 | under L1 ablation than visually-sufficient tasks (p = 0.033; Table 22), rising to 6.5× (p = 0.008) under a stricter criterion; no single task drives the effect (Appendix A.22).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\nLimitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K\nepisodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural",
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

_source line 105_

<details open><summary>🔧 Tool call — Bash · `toolu_011qL6s7Cdz2bqDAqU2hja6J`</summary>

```json
{
  "command": "pdftotext -f 9 -l 9 main.pdf - 2>/dev/null | head -40",
  "description": "Check page 9 content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "20ef4fd6-3174-4fcc-8bd3-ea4142a7d63b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WiLMfpGq5gZkgbGKYgu7DA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 833,
      "cache_read_input_tokens": 51019,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 833
      },
      "output_tokens": 63,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 106 · 2026-05-19T12:07:34.725Z_

<details><summary>↩ Tool result · `toolu_011qL6s7Cdz2bqDAqU2hja6J`</summary>

```text
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "441376c1-1105-4ef3-a34a-9bd899b6483d",
  "tool_use_result": {
    "stdout": "283\n284\n285\n286\n287\n288\n289\n290\n291\n292\n293\n294\n295\n296\n297\n298\n299\n300\n301\n302\n303\n304\n305\n306\n307\n308\n309\n310\n311\n312\n313\n314\n315\n316\n317\n318\n319\n320\n321\n322",
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

_source line 107_

<details><summary>Logged reasoning block</summary>

```text
That's the References page. Let me check the end of page 8 to see where the body ends.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "5eb2c715-34b2-4210-a120-06c52103f88a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbZLRGmM2Mrss9Vcp6K63s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 51852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 192
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

_source line 108_

<details open><summary>🔧 Tool call — Bash · `toolu_01TGsSZqdX1en3KWiQQZK9wD`</summary>

```json
{
  "command": "pdftotext -f 8 -l 8 main.pdf - 2>/dev/null | tail -30",
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
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "d05fe48e-3ae5-4fdd-a9fe-ce94a7285ffc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TbZLRGmM2Mrss9Vcp6K63s",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 192,
      "cache_read_input_tokens": 51852,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 192
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

_source line 109 · 2026-05-19T12:07:37.950Z_

<details><summary>↩ Tool result · `toolu_01TGsSZqdX1en3KWiQQZK9wD`</summary>

```text
Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K
episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural
constraints [1, 12, 50], but routing may differ across scales and paradigms (Appendix A.9, A.1).
Llama-2’s 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates
fine-tuning effects. All analyses are open-loop; our routing analysis (where) complements Häon et
al.’s [4] (what is encoded); closed-loop evaluation combining both is a natural extension.

278

Conclusion. We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with
L1 as the primary hub, supported by seven complementary analyses. Code and data will be released
upon acceptance.

279

References

276
277

280
281
282

[1] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess,
A. Dubey, C. Finn, et al. RT-2: Vision-language-action models transfer web knowledge to
robotic control. arXiv preprint arXiv:2307.15818, 2023.
8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "320070e2-5562-49a8-8d27-05d138a4f7c6",
  "tool_use_result": {
    "stdout": "Limitations and scope. We study OpenVLA-7B, trained on multi-platform data (OXE, 970K\nepisodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural\nconstraints [1, 12, 50], but routing may differ across scales and paradigms (Appendix A.9, A.1).\nLlama-2’s 9/32 pretrained instruction heads may partly reflect text bias; the +15-head delta isolates\nfine-tuning effects. All analyses are open-loop; our routing analysis (where) complements Häon et\nal.’s [4] (what is encoded); closed-loop evaluation combining both is a natural extension.\n\n278\n\nConclusion. We find that VLA fine-tuning reorganizes instruction routing to entry-exit layers with\nL1 as the primary hub, supported by seven complementary analyses. Code and data will be released\nupon acceptance.\n\n279\n\nReferences\n\n276\n277\n\n280\n281\n282\n\n[1] A. Brohan, N. Brown, J. Carbajal, Y. Chebotar, X. Chen, K. Choromanski, T. Ding, D. Driess,\nA. Dubey, C. Finn, et al. RT-2: Vision-language-action models transfer web knowledge to\nrobotic control. arXiv preprint arXiv:2307.15818, 2023.\n8",
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

_source line 110_

The body now ends on page 8 with Conclusion, and References start on the same page. The body is exactly 8 pages. Let me verify there are 0 compilation errors.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "02bce63d-fb99-45a4-a666-68e9ebf304af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177jSwZFCVcg8oKpB5dYDWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 52044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
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

<details open><summary>🔧 Tool call — Bash · `toolu_01VJLomM93TDQvbydZvUxAK4`</summary>

```json
{
  "command": "grep -c \"^!\" main.log 2>/dev/null; grep \"^!\" main.log 2>/dev/null | head -5; echo \"---\"; grep \"Warning.*undefined\" main.log | head -5",
  "description": "Check for LaTeX errors and warnings"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "2e58adc1-1112-4cd0-8b0c-57b4adf17d74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0177jSwZFCVcg8oKpB5dYDWo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 481,
      "cache_read_input_tokens": 52044,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 481
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

_source line 112 · 2026-05-19T12:07:42.502Z_

<details><summary>↩ Tool result · `toolu_01VJLomM93TDQvbydZvUxAK4`</summary>

```text
0
---
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "bbd0253e-085e-4f9f-b357-b27e5404bc3f",
  "tool_use_result": {
    "stdout": "0\n---",
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

_source line 113_

0 errors. Let me verify the exact page where References start and confirm the body is <= 8 pages.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "94447076-133f-4a9c-9b01-cc132a5d5fed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaudmiT2ZZBuH6JudVzW7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 52525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 114_

<details open><summary>🔧 Tool call — Bash · `toolu_01TvRG5dt2Jic5mYJ9c1CCyi`</summary>

```json
{
  "command": "pdftotext -f 1 -l 1 main.pdf - 2>/dev/null | head -5; echo \"=== Page 7 end ===\"; pdftotext -f 7 -l 7 main.pdf - 2>/dev/null | tail -10; echo \"=== Page 8 end ===\"; pdftotext -f 8 -l 8 main.pdf - 2>/dev/null | tail -5",
  "description": "Verify body fits in 8 pages"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "db145240-363d-4dfe-9184-1054f1da8cfc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaudmiT2ZZBuH6JudVzW7R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 182,
      "cache_read_input_tokens": 52525,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 182
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

_source line 115 · 2026-05-19T12:07:47.256Z_

<details><summary>↩ Tool result · `toolu_01TvRG5dt2Jic5mYJ9c1CCyi`</summary>

```text
Vision Encodes, Language Routes:
Token-Level Functional Specialization in a
Vision-Language-Action Model
Anonymous Author(s)
Affiliation
=== Page 7 end ===
trajectory d = 0.65), and constraining (bootstrap CIs, p = 0.0018; specificity 1.08×).
Mechanistic interpretation. Matched-size ablation (d: instruction 0.65, random 0.60, image
0.58; Table 23) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed
routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations
(Nrand = 5 seeds). Counterfactual ordering follows token novelty (ρ = 1.0; §4.3). That ablation
raises R2 yet alters trajectories (d = 0.65) without increasing ground-truth error (∆MSE ≈ 0; Appendix A.8) reflects an information-computation dissociation [45]: routing controls direction rather
than precision, and random ablation yields a larger R2 gain (+0.077 vs. +0.042) because unstructured perturbation releases probe capacity without disrupting organized computation.
7

=== Page 8 end ===
A. Dubey, C. Finn, et al. RT-2: Vision-language-action models transfer web knowledge to
robotic control. arXiv preprint arXiv:2307.15818, 2023.
8
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "77b30c01-0ad6-429d-a205-97649a87a544",
  "tool_use_result": {
    "stdout": "Vision Encodes, Language Routes:\nToken-Level Functional Specialization in a\nVision-Language-Action Model\nAnonymous Author(s)\nAffiliation\n=== Page 7 end ===\ntrajectory d = 0.65), and constraining (bootstrap CIs, p = 0.0018; specificity 1.08×).\nMechanistic interpretation. Matched-size ablation (d: instruction 0.65, random 0.60, image\n0.58; Table 23) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed\nrouting; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations\n(Nrand = 5 seeds). Counterfactual ordering follows token novelty (ρ = 1.0; §4.3). That ablation\nraises R2 yet alters trajectories (d = 0.65) without increasing ground-truth error (∆MSE ≈ 0; Appendix A.8) reflects an information-computation dissociation [45]: routing controls direction rather\nthan precision, and random ablation yields a larger R2 gain (+0.077 vs. +0.042) because unstructured perturbation releases probe capacity without disrupting organized computation.\n7\n\n\f=== Page 8 end ===\nA. Dubey, C. Finn, et al. RT-2: Vision-language-action models transfer web knowledge to\nrobotic control. arXiv preprint arXiv:2307.15818, 2023.\n8",
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

_source line 116_

<details><summary>Logged reasoning block</summary>

```text
The body (Introduction through Conclusion) fits on pages 1-8, with References starting at the bottom of page 8. The body is exactly 8 pages, which meets the CoRL ≤8 page requirement.

Now let me verify all the "sole"/"exclusive" changes and do a final check.

Let me also check if "sole" or "exclusive" appears anywhere else that I might have missed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "326ecd1b-5649-46d3-978f-88f8e0892d6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ceQche8FNQjok2yHmb7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 52707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 588
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

_source line 117_

Body ends on page 8 with Conclusion + start of References. Let me do a final verification of all changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "d132f198-ffd1-4d48-b5bd-b18640e551e6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ceQche8FNQjok2yHmb7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 52707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 588
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

_source line 118_

<details open><summary>🔧 Tool call — Grep · `toolu_017i25dnXpdefxAjLt1GGpog`</summary>

```json
{
  "pattern": "\\b(sole|exclusive)\\b",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "308dfe19-08e4-4049-a42a-55cb2d7d7a15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ceQche8FNQjok2yHmb7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 52707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 588
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

_source line 119 · 2026-05-19T12:07:54.571Z_

<details><summary>↩ Tool result · `toolu_017i25dnXpdefxAjLt1GGpog`</summary>

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
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "02a510e2-2730-4d37-b906-6f1a9321cafe",
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

_source line 120_

<details open><summary>🔧 Tool call — Grep · `toolu_019rLzur8727eBJGuCf6U18B`</summary>

```json
{
  "pattern": "—",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper",
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
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "a6ffc77d-e836-429c-99c5-76aba878e369",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011ceQche8FNQjok2yHmb7QN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 588,
      "cache_read_input_tokens": 52707,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 588
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

_source line 121 · 2026-05-19T12:07:55.525Z_

<details><summary>↩ Tool result · `toolu_019rLzur8727eBJGuCf6U18B`</summary>

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
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "24a70246-87ed-4fd3-8726-f17881e626d3",
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

_source line 122_

All "sole"/"exclusive" instances eliminated, no em-dashes found. Let me verify the final state of the edited files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "b7751936-e118-480c-af55-ac78ccca4c6b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XHgiMiKCfnzLadPFBAQJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 53295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
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

_source line 123_

<details open><summary>🔧 Tool call — Read · `toolu_01Cbz8jCNQivPv6qFiHPU9Lk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "e9dbcfa4-8ed2-483a-88ca-80671712c875",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XHgiMiKCfnzLadPFBAQJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 53295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
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

_source line 124 · 2026-05-19T12:07:59.684Z_

<details><summary>↩ Tool result · `toolu_01Cbz8jCNQivPv6qFiHPU9Lk`</summary>

```text
1	\section{Related Work}\label{sec:related_work}
2	
3	\paragraph{Vision-language-action models.}
4	VLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.
5	This architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.
6	A central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.
7	
8	\paragraph{Mechanistic interpretability in transformers.}
9	Mechanistic analyses have identified residual stream communication~\cite{elhage2021}, induction heads for in-context learning~\cite{olsson2022}, complete circuits for specific tasks~\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\cite{bills2023language,templeton2024scaling}.
10	Attention probing reveals that individual heads encode syntactic relations~\cite{clark2019}, capture depth-dependent patterns~\cite{vig2019}, and that a small subset accounts for most performance~\cite{voita2019}; Michel et al.~\cite{michel2019sixteen} showed most heads can be pruned without loss.
11	Our L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.
12	
13	\paragraph{Behavioral and mechanistic analysis of VLAs.}
14	Behavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\cite{grant2026,hou2026,fei2025}.
15	At the mechanistic level, H\"aon et al.~\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.
16	Sparse autoencoder studies have uncovered interpretable features and memorized action sequences~\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\cite{lu2025,molinari2025}.
17	Fang et al.~\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.
18	The closest work is Grant et al.~\cite{grant2026}, who performed a feature-level mechanistic study and found visual dominance.
19	We differ by decomposing at the token level (identifying the readout as the primary integration site), tracking all 32 layers to reveal a non-monotonic profile, and including trained-vs-untrained factorial controls that isolate fine-tuning effects on attention routing.
20	
21	\paragraph{Token-level functional specialization in transformers.}
22	In Vision Transformers, the CLS token aggregates global information~\cite{dosovitskiy2021} and certain patch positions serve as registers~\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\cite{geva2021}, probing reveals increasingly abstract features across depth~\cite{tenney2019}, the logit lens~\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\cite{neo2025} identified task-specific neurons in multi-task LLMs.
23	We extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.
24	
25	\paragraph{Representation similarity and probing methodology.}
26	RSA~\cite{kriegeskorte2008}, SVCCA~\cite{raghu2017}, CCA~\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\cite{raghu2021} applied these tools to compare ViT and CNN representations.
27	Linear probes~\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.
28	We adopt RSA and MLP probes, with CKA in the appendix.
29	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "4558f81e-6b8f-4795-be3e-6e73b95d9e1a",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/related_work.tex",
      "content": "\\section{Related Work}\\label{sec:related_work}\n\n\\paragraph{Vision-language-action models.}\nVLAs fine-tune large language models on robot demonstrations to produce action tokens conditioned on visual observations and language instructions~\\cite{brohan2023_rt2,kim2024_openvla,karamcheti2024,black2024_pi0}.\nThis architecture family inherits the transformer backbone and its multi-modal fusion mechanisms from vision-language models, but repurposes them for continuous control.\nA central assumption is that fine-tuning injects action-relevant knowledge into pretrained representations; unlike NLP instruction tuning, which targets behavioral compliance~\\cite{wei2022finetuned,ouyang2022training}, we test this at the representational level through per-layer, per-token-type decomposition.\n\n\\paragraph{Mechanistic interpretability in transformers.}\nMechanistic analyses have identified residual stream communication~\\cite{elhage2021}, induction heads for in-context learning~\\cite{olsson2022}, complete circuits for specific tasks~\\cite{wang2023_ioi,conmy2023}, causal tracing for factual recall~\\cite{meng2022_rome}, and the tuned lens for per-layer prediction~\\cite{belrose2023_tunedlens}, while feature-level methods have scaled to dictionary learning over millions of features~\\cite{bills2023language,templeton2024scaling}.\nAttention probing reveals that individual heads encode syntactic relations~\\cite{clark2019}, capture depth-dependent patterns~\\cite{vig2019}, and that a small subset accounts for most performance~\\cite{voita2019}; Michel et al.~\\cite{michel2019sixteen} showed most heads can be pruned without loss.\nOur L1 analysis extends this to VLAs: we use functional ablation to study routing and find that 24 of 32 heads become instruction-dominant after fine-tuning, with progressive ablation yielding monotonic rather than threshold-like effects.\n\n\\paragraph{Behavioral and mechanistic analysis of VLAs.}\nBehavioral evaluations reveal that current VLAs rely disproportionately on visual input, with language instructions largely ignored during action generation~\\cite{grant2026,hou2026,fei2025}.\nAt the mechanistic level, H\\\"aon et al.~\\cite{haon2025} identified sparse semantic directions in VLA residual streams linked to action selection.\nSparse autoencoder studies have uncovered interpretable features and memorized action sequences~\\cite{swann2026,buurmeijer2026}, while probing work has tested for symbolic state representations and emergent world models~\\cite{lu2025,molinari2025}.\nFang et al.~\\cite{fang2025} showed that fine-tuning erodes general VLM reasoning capabilities.\nThe closest work is Grant et al.~\\cite{grant2026}, who performed a feature-level mechanistic study and found visual dominance.\nWe differ by decomposing at the token level (identifying the readout as the primary integration site), tracking all 32 layers to reveal a non-monotonic profile, and including trained-vs-untrained factorial controls that isolate fine-tuning effects on attention routing.\n\n\\paragraph{Token-level functional specialization in transformers.}\nIn Vision Transformers, the CLS token aggregates global information~\\cite{dosovitskiy2021} and certain patch positions serve as registers~\\cite{darcet2024}; in language models, feed-forward layers store factual associations in position-specific patterns~\\cite{geva2021}, probing reveals increasingly abstract features across depth~\\cite{tenney2019}, the logit lens~\\cite{nostalgebraist2020} tracks prediction evolution, and Neo et al.~\\cite{neo2025} identified task-specific neurons in multi-task LLMs.\nWe extend this to VLAs: image tokens remain instruction-blind while the readout token serves as the primary multimodal hub.\n\n\\paragraph{Representation similarity and probing methodology.}\nRSA~\\cite{kriegeskorte2008}, SVCCA~\\cite{raghu2017}, CCA~\\cite{morcos2018}, and Centered Kernel Alignment (CKA)~\\cite{kornblith2019} compare geometric structure between representation spaces; Raghu et al.~\\cite{raghu2021} applied these tools to compare ViT and CNN representations.\nLinear probes~\\cite{alain2017,hewitt2019,hewitt2019control,belinkov2022} complement geometric methods with functional evaluation.\nWe adopt RSA and MLP probes, with CKA in the appendix.\n",
      "numLines": 29,
      "startLine": 1,
      "totalLines": 29
    }
  }
}
```

</details>

---

### Tool call

_source line 125_

<details open><summary>🔧 Tool call — Read · `toolu_016f56JSLCrRSfmvTojcDTWY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "70b53794-c493-4acc-b40e-7df31a7f422b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018XHgiMiKCfnzLadPFBAQJs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 564,
      "cache_read_input_tokens": 53295,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 564
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

_source line 126 · 2026-05-19T12:07:59.767Z_

<details><summary>↩ Tool result · `toolu_016f56JSLCrRSfmvTojcDTWY`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Synthesis.}
5	VLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\Delta \leq 1.7\%$).
6	This explains Grant et al.'s~\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\ $0.634$).
7	Seven analyses support distributed L1 routing: \emph{interventional} (dose-response, $d = 0.48 \to 0.64$; counterfactual, $d = 0.63$--$0.97$), \emph{supporting} (attention gradient $0 \to 9 \to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\times$).
8	
9	\paragraph{Mechanistic interpretation.}
10	Matched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\text{rand}}=5$ seeds).
11	Counterfactual ordering follows token novelty ($\rho = 1.0$; \S\ref{sec:learned_routing}).
12	That ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\Delta\text{MSE} \approx 0$; Appendix~\ref{sec:action_trajectory}) reflects an information-computation dissociation~\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.
13	
14	\paragraph{Functional stages and predictions.}
15	Per-layer profiles suggest three stages: routing (L0--L1; probe $99.6\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\sim}56\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).
16	Task-specific fine-tuning eliminates L31 re-engagement (18 $\to$ 0 heads; \S\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\ LIBERO 500) may also reflect data diversity differences.
17	Predictions: cross-attention VLAs ($\pi_0$~\cite{black2024_pi0}, Octo~\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.
18	
19	\paragraph{Task-dependent routing.}
20	The routing effect is task-dependent: instruction-discriminative tasks show $2.5\times$ larger $|\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\ref{tab:task_complexity}), rising to $6.5\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\ref{sec:task_complexity}).
21	For deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.
22	
23	\paragraph{Limitations and scope.}
24	We study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\ref{sec:ood_diagnostics},~\ref{sec:cka_appendix}).
25	Llama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.
26	All analyses are open-loop; our routing analysis (\emph{where}) complements H\"aon et al.'s~\cite{haon2025} (\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.
27	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "0e591fdf-f2cf-4882-af17-84bfe048ee22",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/docs/paper/discussion.tex",
      "content": "\\section{Discussion}\n\\label{sec:discussion}\n\n\\paragraph{Synthesis.}\nVLA fine-tuning reorganizes instruction routing rather than visual geometry: training effects concentrate at the readout ($R^2$ $+0.069$, attention $+46$pp) rather than images ($\\Delta \\leq 1.7\\%$).\nThis explains Grant et al.'s~\\cite{grant2026} visual dominance finding: DINOv2 has the highest geometric alignment ($\\rho = 0.692$), yet VLA readout surpasses it in decodability ($R^2 = 0.678$ vs.\\ $0.634$).\nSeven analyses support distributed L1 routing: \\emph{interventional} (dose-response, $d = 0.48 \\to 0.64$; counterfactual, $d = 0.63$--$0.97$), \\emph{supporting} (attention gradient $0 \\to 9 \\to 24$ heads; $R^2$ ablation $+0.059$; trajectory $d = 0.65$), and \\emph{constraining} (bootstrap CIs, $p = 0.0018$; specificity $1.08\\times$).\n\n\\paragraph{Mechanistic interpretation.}\nMatched-size ablation ($d$: instruction $0.65$, random $0.60$, image $0.58$; Table~\\ref{tab:specificity_control}) and dose-response (steep through 12 heads, plateau beyond 20) indicate distributed routing; the instruction-dominant group exceeds the random baseline by 2.4 standard deviations ($N_{\\text{rand}}=5$ seeds).\nCounterfactual ordering follows token novelty ($\\rho = 1.0$; \\S\\ref{sec:learned_routing}).\nThat ablation raises $R^2$ yet alters trajectories ($d = 0.65$) without increasing ground-truth error ($\\Delta\\text{MSE} \\approx 0$; Appendix~\\ref{sec:action_trajectory}) reflects an information-computation dissociation~\\cite{hewitt2019control}: routing controls direction rather than precision, and random ablation yields a larger $R^2$ gain ($+0.077$ vs.\\ $+0.042$) because unstructured perturbation releases probe capacity without disrupting organized computation.\n\n\\paragraph{Functional stages and predictions.}\nPer-layer profiles suggest three stages: routing (L0--L1; probe $99.6\\%$, 24/32 instruction-dominant heads), computation (L8--L13; $R^2$ peak $0.655$--$0.678$), and decay (L14--L32, ${\\sim}56\\%$ of parameters; declining $R^2$ and RSA suggest pruning potential).\nTask-specific fine-tuning eliminates L31 re-engagement (18 $\\to$ 0 heads; \\S\\ref{sec:learned_routing}), consistent with exit routing serving multi-task flexibility, though this $N=2$ comparison (OXE 970K vs.\\ LIBERO 500) may also reflect data diversity differences.\nPredictions: cross-attention VLAs ($\\pi_0$~\\cite{black2024_pi0}, Octo~\\cite{ghosh2024_octo}) should lack L1 routing heads; decoder-only VLAs (RT-2~\\cite{brohan2023_rt2}) should show similar routing; larger VLAs should yield flatter per-head contributions.\n\n\\paragraph{Task-dependent routing.}\nThe routing effect is task-dependent: instruction-discriminative tasks show $2.5\\times$ larger $|\\Delta R^2|$ under L1 ablation than visually-sufficient tasks ($p = 0.033$; Table~\\ref{tab:task_complexity}), rising to $6.5\\times$ ($p = 0.008$) under a stricter criterion; no single task drives the effect (Appendix~\\ref{sec:task_complexity}).\nFor deployments, L1 routing probes can flag instruction-discriminative tasks and L1 attention entropy can monitor instruction under-attendance at runtime.\n\n\\paragraph{Limitations and scope.}\nWe study OpenVLA-7B, trained on multi-platform data (OXE, 970K episodes) and evaluated on held-out LIBERO; the framework generalizes via shared architectural constraints~\\cite{brohan2023_rt2,black2024_pi0,ghosh2024_octo}, but routing may differ across scales and paradigms (Appendix~\\ref{sec:ood_diagnostics},~\\ref{sec:cka_appendix}).\nLlama-2's 9/32 pretrained instruction heads may partly reflect text bias; the $+15$-head delta isolates fine-tuning effects.\nAll analyses are open-loop; our routing analysis (\\emph{where}) complements H\\\"aon et al.'s~\\cite{haon2025} (\\emph{what} is encoded); closed-loop evaluation combining both is a natural extension.\n",
      "numLines": 27,
      "startLine": 1,
      "totalLines": 27
    }
  }
}
```

</details>

---

### Assistant

_source line 127_

All edits are clean. Here's the summary:

## 任务 2：强 claim 修改（3 处，非 4 处）

abstract.tex 中不存在 "sole"/"exclusive"，实际只有 3 处：

| 位置 | 原文 | 修改后 |
|------|------|--------|
| `related_work.tex:19` | "the sole multimodal integration site" | "the primary multimodal integration site" |
| `related_work.tex:23` | "the exclusive multimodal hub" | "the primary multimodal hub" |
| `experiments.tex:27` | "the sole locus of multimodal integration" | "the primary locus of multimodal integration" |

## 任务 1：页数压缩 9→8

**LaTeX 间距** (`main.tex`): 添加 `\textfloatsep`/`\intextsep`/`\floatsep`/`\abovecaptionskip`/`\belowcaptionskip` 压缩浮动体间距。

**Related Work 压缩**:
- VLA 段落：3 句合并为 1 句（lines 6-8 → line 6）
- Mechanistic interpretability 段落：9 句压缩为 3 句（删除冗余展开，保留所有引用）
- Behavioral 段落：删除过渡句 "These studies analyze..."，3-item 对比改为紧凑单句

**Discussion 压缩**:
- Synthesis 段落：7-analysis 枚举从 4 行压为 1 行紧凑列表
- Mechanistic interpretation：删除重复的 "modest magnitude supports distributed" 句
- Functional stages：删除重复的 "entry-exit pattern characterizes" 句，合并 N=2 caveat

## 验证结果

- 编译 0 errors，0 undefined references
- **正文 ≤ 8 页**（Conclusion 结束于 page 8 上半部分，References 从 page 8 下方开始）
- 全文无 "sole"/"exclusive"，无 em-dash

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "uuid": "eb13f5d4-1767-499b-bd47-a348e1e792b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01K5wMpLDUz18HXGB57zxFKK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2675,
      "cache_read_input_tokens": 53859,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2675
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

### Task result

_source line 128_

All edits are clean. Here's the summary:

## 任务 2：强 claim 修改（3 处，非 4 处）

abstract.tex 中不存在 "sole"/"exclusive"，实际只有 3 处：

| 位置 | 原文 | 修改后 |
|------|------|--------|
| `related_work.tex:19` | "the sole multimodal integration site" | "the primary multimodal integration site" |
| `related_work.tex:23` | "the exclusive multimodal hub" | "the primary multimodal hub" |
| `experiments.tex:27` | "the sole locus of multimodal integration" | "the primary locus of multimodal integration" |

## 任务 1：页数压缩 9→8

**LaTeX 间距** (`main.tex`): 添加 `\textfloatsep`/`\intextsep`/`\floatsep`/`\abovecaptionskip`/`\belowcaptionskip` 压缩浮动体间距。

**Related Work 压缩**:
- VLA 段落：3 句合并为 1 句（lines 6-8 → line 6）
- Mechanistic interpretability 段落：9 句压缩为 3 句（删除冗余展开，保留所有引用）
- Behavioral 段落：删除过渡句 "These studies analyze..."，3-item 对比改为紧凑单句

**Discussion 压缩**:
- Synthesis 段落：7-analysis 枚举从 4 行压为 1 行紧凑列表
- Mechanistic interpretation：删除重复的 "modest magnitude supports distributed" 句
- Functional stages：删除重复的 "entry-exit pattern characterizes" 句，合并 N=2 caveat

## 验证结果

- 编译 0 errors，0 undefined references
- **正文 ≤ 8 页**（Conclusion 结束于 page 8 上半部分，References 从 page 8 下方开始）
- 全文无 "sole"/"exclusive"，无 em-dash

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 264685,
  "duration_api_ms": 255353,
  "num_turns": 40,
  "stop_reason": "end_turn",
  "session_id": "e82be8f2-0b85-428d-be87-1d57da06926e",
  "total_cost_usd": 1.2096723499999997,
  "usage": {
    "input_tokens": 144,
    "cache_creation_input_tokens": 46160,
    "cache_read_input_tokens": 1193879,
    "output_tokens": 11597,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 46160,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 570,
        "cache_read_input_tokens": 53859,
        "cache_creation_input_tokens": 2675,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2675
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1603,
      "outputTokens": 978,
      "cacheReadInputTokens": 17836,
      "cacheCreationInputTokens": 20249,
      "webSearchRequests": 0,
      "costUSD": 0.03358785,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 144,
      "outputTokens": 11597,
      "cacheReadInputTokens": 1193879,
      "cacheCreationInputTokens": 46160,
      "webSearchRequests": 0,
      "costUSD": 1.1760844999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "041dd8dc-b37b-4da4-abaf-d589f281e5cf"
}
```

</details>

---
