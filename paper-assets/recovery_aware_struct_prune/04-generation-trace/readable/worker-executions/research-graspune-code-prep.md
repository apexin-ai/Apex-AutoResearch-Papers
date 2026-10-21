# research graspune code prep

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 73
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_research_graspune-code-prep_20260514T082040.log`
- **Structured JSON:** [`d42f04ccb61b59bec553.json`](../../sessions/d4/d42f04ccb61b59bec553.json)

## Before a recorded user message

73 recorded events

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
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
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
  "uuid": "cdad59a7-355b-40a7-a339-6f87f7ed03e6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-17-projects-recovery-aware-struct-prune/memory/"
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
    "resetsAt": 1778763000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "11689778-200c-4282-96c9-53441bbab0c3",
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01"
}
```

---

### Assistant

_source line 4_

我来做 GRASPrune 的文献调研和代码调研，产出实现方案报告。

先并行做三件事：搜索论文、搜索代码实现、读现有的 pruning.py 了解当前框架。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "f5242113-ced8-451a-9a81-a6a48fd03dba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkWnN4Q45m31jyhyhL8re7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11873
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Cy4tdLoqVit1UyYWeyhA1b`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
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
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "4d64befe-e132-446e-8db6-28577b59c60d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MkWnN4Q45m31jyhyhL8re7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11873,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11873
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

_source line 6 · 2026-05-14T08:20:53.086Z_

<details><summary>↩ Tool result · `toolu_01Cy4tdLoqVit1UyYWeyhA1b`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "e0f6a0fc-d3f6-4ac5-aac5-7a0b97106bde",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me launch parallel searches and read the existing code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "a4c29a30-a487-431c-9cdd-1968baa920a0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NwHC1ACxHXJ4sbA8pHkLA5`</summary>

```json
{
  "query": "GRASPrune gradient signal preservation pruning neural network paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "89650509-eb32-4784-bc0f-186cb2e43326",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TxaCMh79SK6Ec28f4iPfKQ`</summary>

```json
{
  "query": "GRASPrune structured pruning implementation GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "bd61bf71-dd3f-4a6d-80a0-f34adf326b32",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UxhcVJJ8KszkueadehkHsR`</summary>

```json
{
  "query": "GRASP pruning \"gradient signal preservation\" LLM structured pruning 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "56fc7486-a9e7-4fd0-b977-c1a856c521d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 11_

<details open><summary>🔧 Tool call — Glob · `toolu_015Lzr15HYEagqKUcn9LpLko`</summary>

```json
{
  "pattern": "**/artifacts/src/pruning.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "e482492b-d5ee-48b4-874e-32e61ff3984d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 12 · 2026-05-14T08:20:58.868Z_

<details><summary>↩ Tool result · `toolu_015Lzr15HYEagqKUcn9LpLko`</summary>

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
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "08b56893-1ab2-41e4-b6ac-d518d064f350",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 8,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Glob · `toolu_01JkeVCJbNrjJt353skafWtF`</summary>

```json
{
  "pattern": "**/artifacts/src/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "3f3a95e1-b9e5-4d13-8da5-2f40b72f3bee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016ZCsDDTZxHZd37DVc7un2U",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1275,
      "cache_read_input_tokens": 23714,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1275
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

_source line 14 · 2026-05-14T08:20:59.458Z_

<details><summary>↩ Tool result · `toolu_01JkeVCJbNrjJt353skafWtF`</summary>

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
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "06e5ee32-f5c6-4fff-bffc-728b72eb4537",
  "tool_use_result": {
    "filenames": [],
    "durationMs": 18,
    "numFiles": 0,
    "truncated": false
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T08:21:03.384Z_

<details><summary>↩ Tool result · `toolu_01NwHC1ACxHXJ4sbA8pHkLA5`</summary>

```text
Web search results for query: "GRASPrune gradient signal preservation pruning neural network paper"

Links: [{"title":"Pruning neural networks without any data by iteratively conserving synaptic ﬂow","url":"https://proceedings.neurips.cc/paper/2020/file/46a4378f835dc8040c8057beb6a2da52-Paper.pdf"},{"title":"Winning Tickets: Gradient Flow Preservation","url":"https://www.emergentmind.com/papers/2002.07376"},{"title":"[2002.07376] Picking Winning Tickets Before Training by Preserving Gradient Flow","url":"https://arxiv.org/abs/2002.07376"},{"title":"Picking Winning Tickets Before Training by Preserving Gradient Flow | OpenReview","url":"https://openreview.net/forum?id=SkgsACVKPH"},{"title":"Recent Advances on Neural Network Pruning at Initialization","url":"https://www.ijcai.org/proceedings/2022/0786.pdf"},{"title":"Dynamic Pruning of a Neural Network via Gradient Signal- ...","url":"https://assets.amazon.science/13/93/313fb3ff48a1af7e9a2fab004811/dynamic-pruning-of-a-neural-network-via-gradient-signal-to-noise-ratio.pdf"},{"title":"Picking Winning Tickets Before Training by Preserving Gradient Flow","url":"https://papertalk.org/papertalks/4012"},{"title":"Pruning neural networks without any data by iteratively conserving synaptic ﬂow","url":"https://ganguli-gang.stanford.edu/pdf/20.Pruning.pdf"},{"title":"GitHub - alecwangcq/GraSP: Code for \"Picking Winning Tickets Before Training by Preserving Gradient Flow\" https://openreview.net/pdf?id=SkgsACVKPH","url":"https://github.com/alecwangcq/GraSP"},{"title":"ScoringNet: A Neural Network Based Pruning Criteria for Structured Pruning - Wang - 2023 - Scientific Programming - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1155/2023/9983781"}]

Based on the search results, I found comprehensive information about the GRASPrune (Gradient Signal Preservation) paper:

## GRASPrune - Gradient Signal Preservation Paper

GraSP (Gradient Signal Preservation) is a pruning criterion that preserves gradient flow through the network.

### Key Concept
The method aims to prune networks at initialization, thereby saving resources at training time as well, based on the argument that efficient training requires preserving the gradient flow through the network.

### Technical Approach
GraSP evaluates a weight's significance through how its removal would impact the network's gradient flow, relying on higher-order automatic differentiation to compute the Hessian-gradient product efficiently, which serves as a decisive metric in pruning decisions.

### Performance Results
The method can prune 80% of the weights of a VGG-16 network on ImageNet at initialization, with only a 1.6% drop in top-1 accuracy.

### Experimental Scope
The method was empirically investigated with extensive experiments on CIFAR-10, CIFAR-100, Tiny-ImageNet and ImageNet, using VGGNet and ResNet architectures.

The official implementation is available on GitHub at https://github.com/alecwangcq/GraSP, and the paper is titled "Picking Winning Tickets Before Training by Preserving Gradient Flow."


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "72911950-5d37-4590-a2bc-c7f1615b9b74",
  "tool_use_result": {
    "query": "GRASPrune gradient signal preservation pruning neural network paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_017zne4Ar7WvSGkbk8GzRWrj",
        "content": [
          {
            "title": "Pruning neural networks without any data by iteratively conserving synaptic ﬂow",
            "url": "https://proceedings.neurips.cc/paper/2020/file/46a4378f835dc8040c8057beb6a2da52-Paper.pdf"
          },
          {
            "title": "Winning Tickets: Gradient Flow Preservation",
            "url": "https://www.emergentmind.com/papers/2002.07376"
          },
          {
            "title": "[2002.07376] Picking Winning Tickets Before Training by Preserving Gradient Flow",
            "url": "https://arxiv.org/abs/2002.07376"
          },
          {
            "title": "Picking Winning Tickets Before Training by Preserving Gradient Flow | OpenReview",
            "url": "https://openreview.net/forum?id=SkgsACVKPH"
          },
          {
            "title": "Recent Advances on Neural Network Pruning at Initialization",
            "url": "https://www.ijcai.org/proceedings/2022/0786.pdf"
          },
          {
            "title": "Dynamic Pruning of a Neural Network via Gradient Signal- ...",
            "url": "https://assets.amazon.science/13/93/313fb3ff48a1af7e9a2fab004811/dynamic-pruning-of-a-neural-network-via-gradient-signal-to-noise-ratio.pdf"
          },
          {
            "title": "Picking Winning Tickets Before Training by Preserving Gradient Flow",
            "url": "https://papertalk.org/papertalks/4012"
          },
          {
            "title": "Pruning neural networks without any data by iteratively conserving synaptic ﬂow",
            "url": "https://ganguli-gang.stanford.edu/pdf/20.Pruning.pdf"
          },
          {
            "title": "GitHub - alecwangcq/GraSP: Code for \"Picking Winning Tickets Before Training by Preserving Gradient Flow\" https://openreview.net/pdf?id=SkgsACVKPH",
            "url": "https://github.com/alecwangcq/GraSP"
          },
          {
            "title": "ScoringNet: A Neural Network Based Pruning Criteria for Structured Pruning - Wang - 2023 - Scientific Programming - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1155/2023/9983781"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about the GRASPrune (Gradient Signal Preservation) paper:\n\n## GRASPrune - Gradient Signal Preservation Paper\n\nGraSP (Gradient Signal Preservation) is a pruning criterion that preserves gradient flow through the network.\n\n### Key Concept\nThe method aims to prune networks at initialization, thereby saving resources at training time as well, based on the argument that efficient training requires preserving the gradient flow through the network.\n\n### Technical Approach\nGraSP evaluates a weight's significance through how its removal would impact the network's gradient flow, relying on higher-order automatic differentiation to compute the Hessian-gradient product efficiently, which serves as a decisive metric in pruning decisions.\n\n### Performance Results\nThe method can prune 80% of the weights of a VGG-16 network on ImageNet at initialization, with only a 1.6% drop in top-1 accuracy.\n\n### Experimental Scope\nThe method was empirically investigated with extensive experiments on CIFAR-10, CIFAR-100, Tiny-ImageNet and ImageNet, using VGGNet and ResNet architectures.\n\nThe official implementation is available on GitHub at https://github.com/alecwangcq/GraSP, and the paper is titled \"Picking Winning Tickets Before Training by Preserving Gradient Flow.\""
    ],
    "durationSeconds": 6.559143214000001
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T08:21:04.012Z_

<details><summary>↩ Tool result · `toolu_01TxaCMh79SK6Ec28f4iPfKQ`</summary>

```text
Web search results for query: "GRASPrune structured pruning implementation GitHub"

Links: [{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"GitHub - he-y/Awesome-Pruning: A curated list of neural network pruning resources. · GitHub","url":"https://github.com/he-y/Awesome-Pruning"},{"title":"GitHub - Hahn-Schickard/Automatic-Structured-Pruning: We have implemented a framework that supports developers to structured prune neural networks of Tensorflow Models · GitHub","url":"https://github.com/Hahn-Schickard/Automatic-Structured-Pruning"},{"title":"structured-pruning · GitHub Topics · GitHub","url":"https://github.com/topics/structured-pruning"},{"title":"GitHub - VainF/Torch-Pruning: [CVPR 2023] DepGraph: Towards Any Structural Pruning; LLMs, Vision Foundation Models, etc. · GitHub","url":"https://github.com/VainF/Torch-Pruning"},{"title":"GitHub - polarizationpruning/PolarizationPruning: Implementation of Neuron-level Structured Pruning using Polarization Regularizer","url":"https://github.com/polarizationpruning/PolarizationPruning"},{"title":"pruning · GitHub Topics · GitHub","url":"https://github.com/topics/pruning"},{"title":"GitHub - hrcheng1066/awesome-pruning · GitHub","url":"https://github.com/hrcheng1066/awesome-pruning"}]

Based on the search results, I found the GRASPrune implementation on GitHub:

## GRASPrune GitHub Repository

The official implementation of GRASPrune is available on GitHub, a post-training structured pruning method accepted to ACL 2026 Main Conference for global gating on budgeted structured pruning of LLMs.

**Repository Link:** https://github.com/ZiY-Wang/GRASPrune

### Key Details:

**What it does:** GRASPrune is a post-training structured pruning toolkit for decoder-only LLMs that learns global gates over FFN intermediate channels and attention KV groups, projects them into budget-feasible hard masks, applies lightweight rescale compensation, and exports a dense pruned checkpoint.

**Supported Models:** The code currently supports LLaMA-style and Qwen-style models, including meta-llama/Llama-2-7b-hf and Qwen/Qwen3-8B.

**Performance:** On LLaMA-2-7B, GRASPrune removes 50% of parameters and achieves 12.18 perplexity on WikiText-2 while maintaining competitive average zero-shot accuracy on five benchmarks, using four epochs on 512 unlabeled calibration sequences on a single NVIDIA A100 80GB GPU.

**Requirements:** Python 3.10 is recommended.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "c9ea892b-2f6b-4502-9468-03a3207de048",
  "tool_use_result": {
    "query": "GRASPrune structured pruning implementation GitHub",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JQ3TbL61jDEERkRGSibigG",
        "content": [
          {
            "title": "GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub",
            "url": "https://github.com/ZiY-Wang/GRASPrune"
          },
          {
            "title": "GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/html/2604.19398"
          },
          {
            "title": "[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2604.19398"
          },
          {
            "title": "GitHub - he-y/Awesome-Pruning: A curated list of neural network pruning resources. · GitHub",
            "url": "https://github.com/he-y/Awesome-Pruning"
          },
          {
            "title": "GitHub - Hahn-Schickard/Automatic-Structured-Pruning: We have implemented a framework that supports developers to structured prune neural networks of Tensorflow Models · GitHub",
            "url": "https://github.com/Hahn-Schickard/Automatic-Structured-Pruning"
          },
          {
            "title": "structured-pruning · GitHub Topics · GitHub",
            "url": "https://github.com/topics/structured-pruning"
          },
          {
            "title": "GitHub - VainF/Torch-Pruning: [CVPR 2023] DepGraph: Towards Any Structural Pruning; LLMs, Vision Foundation Models, etc. · GitHub",
            "url": "https://github.com/VainF/Torch-Pruning"
          },
          {
            "title": "GitHub - polarizationpruning/PolarizationPruning: Implementation of Neuron-level Structured Pruning using Polarization Regularizer",
            "url": "https://github.com/polarizationpruning/PolarizationPruning"
          },
          {
            "title": "pruning · GitHub Topics · GitHub",
            "url": "https://github.com/topics/pruning"
          },
          {
            "title": "GitHub - hrcheng1066/awesome-pruning · GitHub",
            "url": "https://github.com/hrcheng1066/awesome-pruning"
          }
        ]
      },
      "Based on the search results, I found the GRASPrune implementation on GitHub:\n\n## GRASPrune GitHub Repository\n\nThe official implementation of GRASPrune is available on GitHub, a post-training structured pruning method accepted to ACL 2026 Main Conference for global gating on budgeted structured pruning of LLMs.\n\n**Repository Link:** https://github.com/ZiY-Wang/GRASPrune\n\n### Key Details:\n\n**What it does:** GRASPrune is a post-training structured pruning toolkit for decoder-only LLMs that learns global gates over FFN intermediate channels and attention KV groups, projects them into budget-feasible hard masks, applies lightweight rescale compensation, and exports a dense pruned checkpoint.\n\n**Supported Models:** The code currently supports LLaMA-style and Qwen-style models, including meta-llama/Llama-2-7b-hf and Qwen/Qwen3-8B.\n\n**Performance:** On LLaMA-2-7B, GRASPrune removes 50% of parameters and achieves 12.18 perplexity on WikiText-2 while maintaining competitive average zero-shot accuracy on five benchmarks, using four epochs on 512 unlabeled calibration sequences on a single NVIDIA A100 80GB GPU.\n\n**Requirements:** Python 3.10 is recommended."
    ],
    "durationSeconds": 6.648377407999998
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T08:21:04.370Z_

<details><summary>↩ Tool result · `toolu_01UxhcVJJ8KszkueadehkHsR`</summary>

```text
Web search results for query: "GRASP pruning "gradient signal preservation" LLM structured pruning 2024 2025"

Links: [{"title":"Picking Winning Tickets Before Training by Preserving Gradient Flow | OpenReview","url":"https://openreview.net/forum?id=SkgsACVKPH"},{"title":"[2002.07376] Picking Winning Tickets Before Training by Preserving Gradient Flow","url":"https://arxiv.org/abs/2002.07376"},{"title":"FGGP: Fixed-Rate Gradient-First Gradual Pruning","url":"https://www.arxiv.org/pdf/2411.05500"},{"title":"Rethinking Layer Removal: A Hybrid Pruning Framework Combining Layer Removal and Singular Value Selection for Efficient LLM Compression","url":"https://arxiv.org/html/2501.00339v2"},{"title":"GRASP: Replace Redundant Layers with Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.1338.pdf"},{"title":"GitHub - alecwangcq/GraSP: Code for \"Picking Winning Tickets Before Training by Preserving Gradient Flow\" https://openreview.net/pdf?id=SkgsACVKPH","url":"https://github.com/alecwangcq/GraSP"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"Winning Tickets: Gradient Flow Preservation","url":"https://www.emergentmind.com/papers/2002.07376"},{"title":"NeurIPS Poster LLM-Pruner: On the Structural Pruning of Large Language Models","url":"https://neurips.cc/virtual/2023/poster/72074"},{"title":"GradPruner: Gradient-guided Layer Pruning Enabling Efficient Fine-Tuning and Inference for LLMs","url":"https://arxiv.org/html/2601.19503v1"}]

Based on the search results, here's what I found regarding GRASP pruning and gradient signal preservation in LLM structured pruning for 2024-2025:

## Key Findings

**Original GraSP Method:**
Gradient Signal Preservation (GraSP) is a pruning criterion developed for pruning networks at initialization, published in 2019-2020. The method is based on the principle that efficient training requires preserving the gradient flow through the network.

**Recent GRASP Framework for LLMs (2024-2025):**
There are two contemporary frameworks using the GRASP acronym for LLM compression:

1. **GRASP (Gradient-guided compression framework):** A novel hybrid gradient-guided compression framework designed to compress redundant layers in LLMs while preserving representation-critical transformations. The method consists of identifying redundant layers based on cosine similarity, and selecting and retaining representation-critical singular values and their corresponding singular vectors using gradient-based attribution.

2. **GRASPrune (Global Gating for Budgeted Structured Pruning):** A structured pruning method which removes channels, heads, or layers from LLMs, appearing to be a more recent 2025 approach.

Both methods leverage gradient-based approaches for structured pruning of large language models, representing recent advances in making LLMs more efficient while maintaining their representation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "cf1cea4f-4e35-4b9f-9b67-0399d80a7915",
  "tool_use_result": {
    "query": "GRASP pruning \"gradient signal preservation\" LLM structured pruning 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PhxnfT73RuFCmDszMrzRaq",
        "content": [
          {
            "title": "Picking Winning Tickets Before Training by Preserving Gradient Flow | OpenReview",
            "url": "https://openreview.net/forum?id=SkgsACVKPH"
          },
          {
            "title": "[2002.07376] Picking Winning Tickets Before Training by Preserving Gradient Flow",
            "url": "https://arxiv.org/abs/2002.07376"
          },
          {
            "title": "FGGP: Fixed-Rate Gradient-First Gradual Pruning",
            "url": "https://www.arxiv.org/pdf/2411.05500"
          },
          {
            "title": "Rethinking Layer Removal: A Hybrid Pruning Framework Combining Layer Removal and Singular Value Selection for Efficient LLM Compression",
            "url": "https://arxiv.org/html/2501.00339v2"
          },
          {
            "title": "GRASP: Replace Redundant Layers with Adaptive ...",
            "url": "https://aclanthology.org/2025.emnlp-main.1338.pdf"
          },
          {
            "title": "GitHub - alecwangcq/GraSP: Code for \"Picking Winning Tickets Before Training by Preserving Gradient Flow\" https://openreview.net/pdf?id=SkgsACVKPH",
            "url": "https://github.com/alecwangcq/GraSP"
          },
          {
            "title": "GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/html/2604.19398"
          },
          {
            "title": "Winning Tickets: Gradient Flow Preservation",
            "url": "https://www.emergentmind.com/papers/2002.07376"
          },
          {
            "title": "NeurIPS Poster LLM-Pruner: On the Structural Pruning of Large Language Models",
            "url": "https://neurips.cc/virtual/2023/poster/72074"
          },
          {
            "title": "GradPruner: Gradient-guided Layer Pruning Enabling Efficient Fine-Tuning and Inference for LLMs",
            "url": "https://arxiv.org/html/2601.19503v1"
          }
        ]
      },
      "Based on the search results, here's what I found regarding GRASP pruning and gradient signal preservation in LLM structured pruning for 2024-2025:\n\n## Key Findings\n\n**Original GraSP Method:**\nGradient Signal Preservation (GraSP) is a pruning criterion developed for pruning networks at initialization, published in 2019-2020. The method is based on the principle that efficient training requires preserving the gradient flow through the network.\n\n**Recent GRASP Framework for LLMs (2024-2025):**\nThere are two contemporary frameworks using the GRASP acronym for LLM compression:\n\n1. **GRASP (Gradient-guided compression framework):** A novel hybrid gradient-guided compression framework designed to compress redundant layers in LLMs while preserving representation-critical transformations. The method consists of identifying redundant layers based on cosine similarity, and selecting and retaining representation-critical singular values and their corresponding singular vectors using gradient-based attribution.\n\n2. **GRASPrune (Global Gating for Budgeted Structured Pruning):** A structured pruning method which removes channels, heads, or layers from LLMs, appearing to be a more recent 2025 approach.\n\nBoth methods leverage gradient-based approaches for structured pruning of large language models, representing recent advances in making LLMs more efficient while maintaining their representation capabilities."
    ],
    "durationSeconds": 6.53233753
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Good findings! The key discovery is that there are actually TWO different things called "GRASP":

1. **Original GraSP (2020)** - "Picking Winning Tickets Before Training by Preserving Gradient Flow" - unstructured pruning at initialization, uses Hessian-gradient product
2. **GRASPrune (ACL 2026)** - "Global Gating for Budgeted Structured Pruning of Large Language Models" - this is a structured pruning method for LLMs, exactly what we need!


Now I need to dig into the GRASPrune paper itself to understand how it works, so I'll pull the arXiv version and check out their implementation on GitHub to see the actual pruning logic.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "4eec9804-be99-436b-82c7-64b2005399be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQLmhxkQKufq6Cho8TuH2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 24989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
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

_source line 19_

发现了关键信息：GRASPrune (ACL 2026 Main) 是一个专门针对 LLM 的 structured pruning 方法，有官方实现且支持 Qwen 架构。让我深入调研论文和代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "d384f062-c208-49c7-8048-a0ea99f6536f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQLmhxkQKufq6Cho8TuH2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 24989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
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

_source line 20_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XR1F2MRvEMJkz2w6F6GcHt`</summary>

```json
{
  "query": "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning LLM details method"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "56aff8c1-4486-4918-bd18-075247a0859b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQLmhxkQKufq6Cho8TuH2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 24989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
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

_source line 21_

<details open><summary>🔧 Tool call — Bash · `toolu_013QZD1PB7nn3TyJWwuoxBgj`</summary>

```json
{
  "command": "cd /tmp && rm -rf graspune_refs && mkdir -p graspune_refs && cd graspune_refs && git clone --depth 1 https://github.com/ZiY-Wang/GRASPrune.git 2>&1 | tail -5",
  "description": "Clone GRASPrune official repo",
  "timeout": 60000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "ead26afc-fb4b-455f-bcdb-e5a11cb9d2a4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQLmhxkQKufq6Cho8TuH2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 24989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
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

_source line 22_

<details open><summary>🔧 Tool call — Glob · `toolu_01Vvgn7j2iWzQZxxekyg7eD6`</summary>

```json
{
  "pattern": "**/artifacts/**/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "09cdc4c0-3972-435d-ab66-147ecdb9385a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RQLmhxkQKufq6Cho8TuH2b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 61,
      "cache_creation_input_tokens": 3092,
      "cache_read_input_tokens": 24989,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3092
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

_source line 23 · 2026-05-14T08:21:19.704Z_

<details><summary>↩ Tool result · `toolu_01XR1F2MRvEMJkz2w6F6GcHt`</summary>

```text
Web search results for query: "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning LLM details method"

Links: [{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"StructPrune: Structured Global Pruning asymptotics with 𝒪⁢(√𝑁) GPU Memory","url":"https://arxiv.org/html/2510.03246v1"},{"title":"From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models","url":"https://arxiv.org/html/2510.18030v1"},{"title":"Optimization-based Structural Pruning for Large Language Models without Back-Propagation","url":"https://arxiv.org/html/2406.10576v1"},{"title":"[2004.02164] DSA: More Efficient Budgeted Pruning via Differentiable Sparsity Allocation","url":"https://arxiv.org/abs/2004.02164"},{"title":"[2503.09657] Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization","url":"https://arxiv.org/abs/2503.09657"},{"title":"HAP-E: HESSIAN-AWARE STRUCTURED PRUNING OF LLMS FOR EFFICIENT INFERENCE | OpenReview","url":"https://openreview.net/forum?id=B0C0bt2R7l"},{"title":"[1811.09332] Structured Pruning of Neural Networks with Budget-Aware Regularization","url":"https://arxiv.org/abs/1811.09332"}]

Based on the search results, here are the details about GRASPrune (arxiv 2604.19398):

## Overview
GRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget.

## Method Details
GRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step while keeping the backbone weights frozen. After the mask is fixed, the method calibrates scaling factors on the retained units to mitigate scale mismatch caused by pruning, and folds these factors into the pruned weights to obtain a smaller dense checkpoint with no extra parameters at inference.

## Key Characteristics
The backbone weights remain frozen, and the method optimizes only a small set of scalar gates on a small unlabeled calibration set. The method uses parameter count as the budget proxy and also reports KV cache and throughput results to connect pruning to serving performance.

## Performance Results
On LLaMA-2-7B, the pruned model reaches 12.18 perplexity on WikiText-2 at a 50% parameter ratio and 16.65 at 40%, with learning taking roughly 6 minutes on a single A100 80GB GPU.

## Implementation
The paper was accepted to ACL 2026 Main Conference with official implementation available.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "53b7a211-dfc8-4acf-846f-b416fc4d3fae",
  "tool_use_result": {
    "query": "arxiv 2604.19398 GRASPrune global gating budgeted structured pruning LLM details method",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LNgocCSrNzBSk51qnqexmS",
        "content": [
          {
            "title": "[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2604.19398"
          },
          {
            "title": "GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/html/2604.19398"
          },
          {
            "title": "GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub",
            "url": "https://github.com/ZiY-Wang/GRASPrune"
          },
          {
            "title": "StructPrune: Structured Global Pruning asymptotics with 𝒪⁢(√𝑁) GPU Memory",
            "url": "https://arxiv.org/html/2510.03246v1"
          },
          {
            "title": "From Local to Global: Revisiting Structured Pruning Paradigms for Large Language Models",
            "url": "https://arxiv.org/html/2510.18030v1"
          },
          {
            "title": "Optimization-based Structural Pruning for Large Language Models without Back-Propagation",
            "url": "https://arxiv.org/html/2406.10576v1"
          },
          {
            "title": "[2004.02164] DSA: More Efficient Budgeted Pruning via Differentiable Sparsity Allocation",
            "url": "https://arxiv.org/abs/2004.02164"
          },
          {
            "title": "[2503.09657] Týr-the-Pruner: Structural Pruning LLMs via Global Sparsity Distribution Optimization",
            "url": "https://arxiv.org/abs/2503.09657"
          },
          {
            "title": "HAP-E: HESSIAN-AWARE STRUCTURED PRUNING OF LLMS FOR EFFICIENT INFERENCE | OpenReview",
            "url": "https://openreview.net/forum?id=B0C0bt2R7l"
          },
          {
            "title": "[1811.09332] Structured Pruning of Neural Networks with Budget-Aware Regularization",
            "url": "https://arxiv.org/abs/1811.09332"
          }
        ]
      },
      "Based on the search results, here are the details about GRASPrune (arxiv 2604.19398):\n\n## Overview\nGRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget.\n\n## Method Details\nGRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step while keeping the backbone weights frozen. After the mask is fixed, the method calibrates scaling factors on the retained units to mitigate scale mismatch caused by pruning, and folds these factors into the pruned weights to obtain a smaller dense checkpoint with no extra parameters at inference.\n\n## Key Characteristics\nThe backbone weights remain frozen, and the method optimizes only a small set of scalar gates on a small unlabeled calibration set. The method uses parameter count as the budget proxy and also reports KV cache and throughput results to connect pruning to serving performance.\n\n## Performance Results\nOn LLaMA-2-7B, the pruned model reaches 12.18 perplexity on WikiText-2 at a 50% parameter ratio and 16.65 at 40%, with learning taking roughly 6 minutes on a single A100 80GB GPU.\n\n## Implementation\nThe paper was accepted to ACL 2026 Main Conference with official implementation available."
    ],
    "durationSeconds": 7.431247563000005
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-14T08:21:20.473Z_

<details><summary>↩ Tool result · `toolu_013QZD1PB7nn3TyJWwuoxBgj`</summary>

```text
Cloning into 'GRASPrune'...
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "4a07bcbd-ca10-47cd-8117-aa3871ad6f38",
  "tool_use_result": {
    "stdout": "Cloning into 'GRASPrune'...",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-14T08:21:20.493Z_

<details><summary>↩ Tool result · `toolu_01Vvgn7j2iWzQZxxekyg7eD6`</summary>

```text
artifacts/correlation_analysis.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "bbbbcb6a-ca2b-4f45-b3f9-9fd872e560b3",
  "tool_use_result": {
    "filenames": [
      "artifacts/correlation_analysis.py"
    ],
    "durationMs": 15,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
The repo cloned. Let me now explore the GRASPrune code structure and read the key files, plus the arXiv HTML paper for more details. Also need to find the actual pruning.py on the server or locally.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "20c815aa-8428-4000-85ef-05524d0cfb49",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xZ3mH83XAc51jWY9RxuLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 28081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 27_

<details open><summary>🔧 Tool call — Bash · `toolu_016CuGKUnXEwaMuuosog4GE3`</summary>

```json
{
  "command": "find /tmp/graspune_refs/GRASPrune -type f -name \"*.py\" | head -30",
  "description": "List Python files in GRASPrune repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "6b10e648-379d-45fa-a773-3adeb8ee876e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xZ3mH83XAc51jWY9RxuLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 28081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 28 · 2026-05-14T08:21:24.609Z_

<details><summary>↩ Tool result · `toolu_016CuGKUnXEwaMuuosog4GE3`</summary>

```text
/tmp/graspune_refs/GRASPrune/train.py
/tmp/graspune_refs/GRASPrune/rebuild.py
/tmp/graspune_refs/GRASPrune/pipeline.py
/tmp/graspune_refs/GRASPrune/gates.py
/tmp/graspune_refs/GRASPrune/evals.py
/tmp/graspune_refs/GRASPrune/eval_pruned_ppl.py
/tmp/graspune_refs/GRASPrune/eval_pruned_acc.py
/tmp/graspune_refs/GRASPrune/data.py
/tmp/graspune_refs/GRASPrune/config.py
/tmp/graspune_refs/GRASPrune/__init__.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "dbc9aad0-7277-4ceb-bfcd-f7c05d293aaa",
  "tool_use_result": {
    "stdout": "/tmp/graspune_refs/GRASPrune/train.py\n/tmp/graspune_refs/GRASPrune/rebuild.py\n/tmp/graspune_refs/GRASPrune/pipeline.py\n/tmp/graspune_refs/GRASPrune/gates.py\n/tmp/graspune_refs/GRASPrune/evals.py\n/tmp/graspune_refs/GRASPrune/eval_pruned_ppl.py\n/tmp/graspune_refs/GRASPrune/eval_pruned_acc.py\n/tmp/graspune_refs/GRASPrune/data.py\n/tmp/graspune_refs/GRASPrune/config.py\n/tmp/graspune_refs/GRASPrune/__init__.py",
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

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_011EqKCuygspAPBcus433os5`</summary>

```json
{
  "command": "ls -la /tmp/graspune_refs/GRASPrune/",
  "description": "List GRASPrune repo root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "db088ca1-97af-4af8-bf3c-94421b2bb13d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xZ3mH83XAc51jWY9RxuLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 28081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 30 · 2026-05-14T08:21:25.118Z_

<details><summary>↩ Tool result · `toolu_011EqKCuygspAPBcus433os5`</summary>

```text
total 116
drwxr-xr-x 3 ubuntu ubuntu   360 May 14 08:21 .
drwxr-xr-x 3 ubuntu ubuntu    60 May 14 08:21 ..
drwxr-xr-x 7 ubuntu ubuntu   260 May 14 08:21 .git
-rw-r--r-- 1 ubuntu ubuntu   382 May 14 08:21 .gitignore
-rw-r--r-- 1 ubuntu ubuntu     5 May 14 08:21 .python-version
-rw-r--r-- 1 ubuntu ubuntu 11357 May 14 08:21 LICENSE
-rw-r--r-- 1 ubuntu ubuntu  3262 May 14 08:21 README.md
-rw-r--r-- 1 ubuntu ubuntu   131 May 14 08:21 __init__.py
-rw-r--r-- 1 ubuntu ubuntu  1814 May 14 08:21 config.py
-rw-r--r-- 1 ubuntu ubuntu  2804 May 14 08:21 data.py
-rw-r--r-- 1 ubuntu ubuntu  1690 May 14 08:21 eval_pruned_acc.py
-rw-r--r-- 1 ubuntu ubuntu  2043 May 14 08:21 eval_pruned_ppl.py
-rw-r--r-- 1 ubuntu ubuntu  6420 May 14 08:21 evals.py
-rw-r--r-- 1 ubuntu ubuntu 22092 May 14 08:21 gates.py
-rw-r--r-- 1 ubuntu ubuntu 21231 May 14 08:21 pipeline.py
-rw-r--r-- 1 ubuntu ubuntu  4914 May 14 08:21 rebuild.py
-rw-r--r-- 1 ubuntu ubuntu   122 May 14 08:21 requirements.txt
-rw-r--r-- 1 ubuntu ubuntu  3155 May 14 08:21 train.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "b9ebc67c-7954-4be1-a9c5-dda1c94c077d",
  "tool_use_result": {
    "stdout": "total 116\ndrwxr-xr-x 3 ubuntu ubuntu   360 May 14 08:21 .\ndrwxr-xr-x 3 ubuntu ubuntu    60 May 14 08:21 ..\ndrwxr-xr-x 7 ubuntu ubuntu   260 May 14 08:21 .git\n-rw-r--r-- 1 ubuntu ubuntu   382 May 14 08:21 .gitignore\n-rw-r--r-- 1 ubuntu ubuntu     5 May 14 08:21 .python-version\n-rw-r--r-- 1 ubuntu ubuntu 11357 May 14 08:21 LICENSE\n-rw-r--r-- 1 ubuntu ubuntu  3262 May 14 08:21 README.md\n-rw-r--r-- 1 ubuntu ubuntu   131 May 14 08:21 __init__.py\n-rw-r--r-- 1 ubuntu ubuntu  1814 May 14 08:21 config.py\n-rw-r--r-- 1 ubuntu ubuntu  2804 May 14 08:21 data.py\n-rw-r--r-- 1 ubuntu ubuntu  1690 May 14 08:21 eval_pruned_acc.py\n-rw-r--r-- 1 ubuntu ubuntu  2043 May 14 08:21 eval_pruned_ppl.py\n-rw-r--r-- 1 ubuntu ubuntu  6420 May 14 08:21 evals.py\n-rw-r--r-- 1 ubuntu ubuntu 22092 May 14 08:21 gates.py\n-rw-r--r-- 1 ubuntu ubuntu 21231 May 14 08:21 pipeline.py\n-rw-r--r-- 1 ubuntu ubuntu  4914 May 14 08:21 rebuild.py\n-rw-r--r-- 1 ubuntu ubuntu   122 May 14 08:21 requirements.txt\n-rw-r--r-- 1 ubuntu ubuntu  3155 May 14 08:21 train.py",
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

_source line 31_

<details open><summary>🔧 Tool call — Glob · `toolu_017tpY2m8yKqY49NgMNg7aM5`</summary>

```json
{
  "pattern": "**/src/*.py",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "a11afbb2-9429-48b6-92e1-a0be52c1d390",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xZ3mH83XAc51jWY9RxuLt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1818,
      "cache_read_input_tokens": 28081,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1818
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

_source line 32 · 2026-05-14T08:21:25.711Z_

<details><summary>↩ Tool result · `toolu_017tpY2m8yKqY49NgMNg7aM5`</summary>

```text
src/importance_score.py
src/rasp_scoring.py
src/prune.py
src/train_grpo.py
src/eval_gsm8k.py
src/correlation_analysis.py
src/cka_overlap.py
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "f86de785-b436-468e-8ac5-aab35954e6b0",
  "tool_use_result": {
    "filenames": [
      "src/importance_score.py",
      "src/rasp_scoring.py",
      "src/prune.py",
      "src/train_grpo.py",
      "src/eval_gsm8k.py",
      "src/correlation_analysis.py",
      "src/cka_overlap.py"
    ],
    "durationMs": 6,
    "numFiles": 7,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Read · `toolu_01RWv6gJvNF8TsKV8eiU5FxV`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/gates.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "25237da8-7acc-4be0-b5ad-167ea26cf061",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Read · `toolu_017XoQG6t4AxTs42GSThFDSu`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/pipeline.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "485c30ab-e78c-4b2f-a2eb-e29f4a9bb517",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_013JMbVZqYDNdPLDuJXdGtt6`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/train.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "f472047e-a801-4dba-a689-0da99909f087",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 36 · 2026-05-14T08:21:30.997Z_

<details><summary>↩ Tool result · `toolu_01RWv6gJvNF8TsKV8eiU5FxV`</summary>

```text
1	from __future__ import annotations
2	
3	import torch
4	import torch.nn as nn
5	from transformers.activations import ACT2FN
6	from transformers.models.llama.modeling_llama import (
7	    ALL_ATTENTION_FUNCTIONS,
8	    apply_rotary_pos_emb,
9	    eager_attention_forward,
10	)
11	
12	
13	def get_transformer_layers(model):
14	    if hasattr(model, "model") and hasattr(model.model, "layers"):
15	        return list(model.model.layers)
16	    raise RuntimeError("Unable to locate decoder layers at model.model.layers.")
17	
18	
19	def infer_model_family(model_or_config) -> str:
20	    config = getattr(model_or_config, "config", model_or_config)
21	    model_type = str(getattr(config, "model_type", "")).lower()
22	    architectures = " ".join(getattr(config, "architectures", []) or []).lower()
23	    if "qwen" in model_type or "qwen" in architectures:
24	        return "qwen"
25	    return "llama"
26	
27	
28	class LlamaMLPGate(nn.Module):
29	    def __init__(self, cfg, src: nn.Module, gate_init: float, tau: float, device: str):
30	        super().__init__()
31	        self.hidden_size = cfg.hidden_size
32	        self.intermediate_size = cfg.intermediate_size
33	        self.act_fn = ACT2FN[cfg.hidden_act]
34	        self.tau = tau
35	
36	        self.gate_proj = src.gate_proj
37	        self.up_proj = src.up_proj
38	        self.down_proj = src.down_proj
39	        for parameter in (
40	            list(self.gate_proj.parameters())
41	            + list(self.up_proj.parameters())
42	            + list(self.down_proj.parameters())
43	        ):
44	            parameter.requires_grad_(False)
45	
46	        self.gate_score = nn.Parameter(torch.full((self.intermediate_size,), gate_init, device=device))
47	
48	    def forward(self, x: torch.Tensor) -> torch.Tensor:
49	        up = self.up_proj(x)
50	        gate = self.act_fn(self.gate_proj(x))
51	        inter = up * gate
52	        act_dtype = inter.dtype
53	
54	        if getattr(self, "_rescale_mode", False) and hasattr(self, "eval_keep_mask"):
55	            mask = self.eval_keep_mask.to(act_dtype).view(1, 1, -1)
56	            alpha = getattr(self, "rescale_alpha", 0.5)
57	            scale = 1.0 + alpha * torch.tanh(self.gate_score.to(act_dtype)).view(1, 1, -1)
58	            z = mask * scale
59	            return self.down_proj(inter * z)
60	
61	        if self.training and hasattr(self, "_batch_mask"):
62	            hard_mask = self._batch_mask.to(act_dtype)
63	            soft_prob = torch.sigmoid(self.gate_score / self.tau).to(act_dtype).view(1, 1, -1)
64	            z = hard_mask + (soft_prob - soft_prob.detach())
65	        elif hasattr(self, "eval_keep_mask"):
66	            z = self.eval_keep_mask.to(act_dtype).view(1, 1, -1)
67	        else:
68	            z = torch.sigmoid(self.gate_score / self.tau).to(act_dtype).view(1, 1, -1)
69	
70	        return self.down_proj(inter * z)
71	
72	    @torch.no_grad()
73	    def register_hard_mask(self, keep_mask_1d: torch.Tensor) -> None:
74	        if hasattr(self, "eval_keep_mask"):
75	            self.eval_keep_mask.data = keep_mask_1d.float()
76	        else:
77	            self.register_buffer("eval_keep_mask", keep_mask_1d.float())
78	
79	    @torch.no_grad()
80	    def materialize_pruning(self) -> None:
81	        if not hasattr(self, "eval_keep_mask"):
82	            return
83	
84	        keep = self.eval_keep_mask.to(torch.bool)
85	        idx = keep.nonzero(as_tuple=False).squeeze(1)
86	        if idx.numel() == 0:
87	            idx = torch.tensor([0], device=keep.device)
88	
89	        scale_keep = None
90	        if getattr(self, "_rescale_mode", False) and hasattr(self, "gate_score"):
91	            alpha = getattr(self, "rescale_alpha", 0.5)
92	            full_scale = 1.0 + alpha * torch.tanh(self.gate_score.detach().to(self.down_proj.weight.dtype))
93	            scale_keep = full_scale[keep]
94	
95	        def prune_out(linear: nn.Linear, indices: torch.Tensor) -> nn.Linear:
96	            weight = linear.weight.data[indices, :].clone()
97	            bias = linear.bias.data[indices].clone() if linear.bias is not None else None
98	            new_linear = nn.Linear(linear.in_features, indices.numel(), bias=(linear.bias is not None)).to(
99	                weight.device, dtype=weight.dtype
100	            )
101	            new_linear.weight.data.copy_(weight)
102	            if bias is not None:
103	                new_linear.bias.data.copy_(bias)
104	            return new_linear
105	
106	        def prune_in(linear: nn.Linear, indices: torch.Tensor, scale_vec: torch.Tensor | None = None) -> nn.Linear:
107	            weight = linear.weight.data[:, indices].clone()
108	            if scale_vec is not None:
109	                weight = weight * scale_vec.view(1, -1)
110	            new_linear = nn.Linear(indices.numel(), linear.out_features, bias=(linear.bias is not None)).to(
111	                weight.device, dtype=weight.dtype
112	            )
113	            new_linear.weight.data.copy_(weight)
114	            if linear.bias is not None:
115	                new_linear.bias.data.copy_(linear.bias.data)
116	            return new_linear
117	
118	        self.up_proj = prune_out(self.up_proj, idx)
119	        self.gate_proj = prune_out(self.gate_proj, idx)
120	        self.down_proj = prune_in(self.down_proj, idx, scale_keep)
121	
122	        for attr_name in ("gate_score", "eval_keep_mask", "_rescale_mode", "rescale_alpha"):
123	            if hasattr(self, attr_name):
124	                delattr(self, attr_name)
125	
126	
127	class LlamaAttnGate(nn.Module):
128	    def __init__(self, cfg, layer_idx: int, src: nn.Module, gate_init: float, tau: float, device: str):
129	        super().__init__()
130	        self.config = cfg
131	        self.layer_idx = layer_idx
132	        self.head_dim = getattr(cfg, "head_dim", cfg.hidden_size // cfg.num_attention_heads)
133	        self.num_heads = cfg.num_attention_heads
134	        self.num_key_value_heads = cfg.num_key_value_heads
135	        self.num_key_value_groups = max(1, self.num_heads // max(1, self.num_key_value_heads))
136	        self.scaling = self.head_dim ** -0.5
137	        self.attention_dropout = cfg.attention_dropout
138	        self.is_causal = True
139	        self.tau = tau
140	
141	        self.q_proj = src.q_proj
142	        self.k_proj = src.k_proj
143	        self.v_proj = src.v_proj
144	        self.o_proj = src.o_proj
145	        for parameter in (
146	            list(self.q_proj.parameters())
147	            + list(self.k_proj.parameters())
148	            + list(self.v_proj.parameters())
149	            + list(self.o_proj.parameters())
150	        ):
151	            parameter.requires_grad_(False)
152	
153	        self.gate_score_kv = nn.Parameter(torch.full((self.num_key_value_heads,), gate_init, device=device))
154	
155	    def forward(
156	        self,
157	        hidden_states: torch.Tensor,
158	        position_embeddings,
159	        attention_mask=None,
160	        past_key_value=None,
161	        cache_position=None,
162	        **kwargs,
163	    ):
164	        input_shape = hidden_states.shape[:-1]
165	        hidden_shape = (*input_shape, -1, self.head_dim)
166	
167	        q = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)
168	        k = self.k_proj(hidden_states).view(hidden_shape).transpose(1, 2)
169	        v = self.v_proj(hidden_states).view(hidden_shape).transpose(1, 2)
170	
171	        cos, sin = position_embeddings
172	        q, k = apply_rotary_pos_emb(q, k, cos, sin)
173	
174	        if past_key_value is not None:
175	            cache_kwargs = {"sin": sin, "cos": cos, "cache_position": cache_position}
176	            k, v = past_key_value.update(k, v, self.layer_idx, cache_kwargs)
177	
178	        act_dtype = q.dtype
179	        if getattr(self, "_rescale_mode", False) and hasattr(self, "eval_keep_mask_kv"):
180	            mask_kv = self.eval_keep_mask_kv.to(act_dtype)
181	            alpha = getattr(self, "rescale_alpha", 0.5)
182	            scale_kv = 1.0 + alpha * torch.tanh(self.gate_score_kv.to(act_dtype))
183	            z = mask_kv * scale_kv
184	        elif self.training and hasattr(self, "_batch_mask"):
185	            hard_mask = self._batch_mask.to(act_dtype)
186	            soft_prob = torch.sigmoid(self.gate_score_kv / self.tau).to(act_dtype)
187	            z = hard_mask + (soft_prob - soft_prob.detach())
188	        elif hasattr(self, "eval_keep_mask_kv"):
189	            z = self.eval_keep_mask_kv.to(act_dtype)
190	        else:
191	            z = torch.sigmoid(self.gate_score_kv / self.tau).to(act_dtype)
192	
193	        kv_gate = z.view(1, -1, 1, 1)
194	        k = k * kv_gate
195	        v = v * kv_gate
196	
197	        attention_interface = eager_attention_forward
198	        if self.config._attn_implementation != "eager":
199	            if not (
200	                self.config._attn_implementation == "sdpa"
201	                and kwargs.get("output_attentions", False)
202	            ):
203	                attention_interface = ALL_ATTENTION_FUNCTIONS[self.config._attn_implementation]
204	
205	        out, attn = attention_interface(
206	            self,
207	            q,
208	            k,
209	            v,
210	            attention_mask,
211	            dropout=0.0 if not self.training else self.attention_dropout,
212	            scaling=self.scaling,
213	            **kwargs,
214	        )
215	        out = out.reshape(*input_shape, -1).contiguous()
216	        out = self.o_proj(out)
217	        return out, attn
218	
219	    @torch.no_grad()
220	    def register_hard_mask_kv(self, keep_mask_kv: torch.Tensor) -> None:
221	        if hasattr(self, "eval_keep_mask_kv"):
222	            self.eval_keep_mask_kv.data = keep_mask_kv.float()
223	        else:
224	            self.register_buffer("eval_keep_mask_kv", keep_mask_kv.float())
225	
226	    @torch.no_grad()
227	    def materialize_pruning(self) -> None:
228	        if not hasattr(self, "eval_keep_mask_kv"):
229	            return
230	
231	        keep_kv = self.eval_keep_mask_kv.to(torch.bool)
232	        if keep_kv.sum() == 0:
233	            keep_kv = keep_kv.clone()
234	            keep_kv[0] = True
235	
236	        num_heads = self.num_heads
237	        num_kv_heads = self.num_key_value_heads
238	        head_dim = self.head_dim
239	        group_size = max(1, num_heads // max(1, num_kv_heads))
240	        keep_heads = keep_kv.repeat_interleave(group_size)
241	
242	        scale_keep_kv = None
243	        if getattr(self, "_rescale_mode", False) and hasattr(self, "gate_score_kv"):
244	            alpha = getattr(self, "rescale_alpha", 0.5)
245	            full_scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.detach().to(self.k_proj.weight.dtype))
246	            scale_keep_kv = full_scale[keep_kv]
247	
248	        def prune_q_out(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:
249	            weight = linear.weight.data
250	            out_features, in_features = weight.shape
251	            assert out_features == num_heads * head_dim
252	            weight = weight.view(num_heads, head_dim, in_features)[keep_mask_h, :, :]
253	            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(
254	                weight.device, dtype=weight.dtype
255	            )
256	            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))
257	            if linear.bias is not None:
258	                bias = linear.bias.data.view(num_heads, head_dim)[keep_mask_h, :].reshape(-1)
259	                new_linear.bias.data.copy_(bias)
260	            return new_linear
261	
262	        def prune_kv_out(
263	            linear: nn.Linear,
264	            keep_mask: torch.Tensor,
265	            scale_vec: torch.Tensor | None = None,
266	        ) -> nn.Linear:
267	            weight = linear.weight.data
268	            out_features, in_features = weight.shape
269	            assert out_features == num_kv_heads * head_dim
270	            weight = weight.view(num_kv_heads, head_dim, in_features)[keep_mask, :, :]
271	            if scale_vec is not None:
272	                weight = scale_vec.view(-1, 1, 1) * weight
273	            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(
274	                weight.device, dtype=weight.dtype
275	            )
276	            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))
277	            if linear.bias is not None:
278	                bias = linear.bias.data.view(num_kv_heads, head_dim)[keep_mask, :].reshape(-1)
279	                new_linear.bias.data.copy_(bias)
280	            return new_linear
281	
282	        def prune_o_in(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:
283	            weight = linear.weight.data
284	            out_features, in_features = weight.shape
285	            assert in_features == num_heads * head_dim
286	            weight = weight.view(out_features, num_heads, head_dim)[:, keep_mask_h, :].reshape(out_features, -1)
287	            new_linear = nn.Linear(weight.shape[1], out_features, bias=(linear.bias is not None)).to(
288	                weight.device, dtype=weight.dtype
289	            )
290	            new_linear.weight.data.copy_(weight)
291	            if linear.bias is not None:
292	                new_linear.bias.data.copy_(linear.bias.data)
293	            return new_linear
294	
295	        self.q_proj = prune_q_out(self.q_proj, keep_heads)
296	        self.k_proj = prune_kv_out(self.k_proj, keep_kv, scale_keep_kv)
297	        self.v_proj = prune_kv_out(self.v_proj, keep_kv, scale_keep_kv)
298	        self.o_proj = prune_o_in(self.o_proj, keep_heads)
299	
300	        self.num_heads = int(keep_heads.sum().item())
301	        self.num_key_value_heads = int(keep_kv.sum().item())
302	        self.num_key_value_groups = max(1, self.num_heads // max(1, self.num_key_value_heads))
303	
304	        for attr_name in ("gate_score_kv", "eval_keep_mask_kv", "_rescale_mode", "rescale_alpha"):
305	            if hasattr(self, attr_name):
306	                delattr(self, attr_name)
307	
308	
309	class QwenMLPGate(LlamaMLPGate):
310	    pass
311	
312	
313	class QwenAttnGate(nn.Module):
314	    def __init__(self, cfg, layer_idx: int, src: nn.Module, gate_init: float, tau: float, device: str):
315	        super().__init__()
316	        del layer_idx
317	        self.config = cfg
318	        self.src = src
319	        self.tau = tau
320	        self.num_heads = int(getattr(cfg, "num_attention_heads", getattr(src, "num_heads", 0)))
321	        self.num_key_value_heads = int(getattr(cfg, "num_key_value_heads", getattr(src, "num_key_value_heads", 0)))
322	        if self.num_heads <= 0 or self.num_key_value_heads <= 0:
323	            raise RuntimeError("Unable to infer num_attention_heads / num_key_value_heads for Qwen.")
324	        self.head_dim = int(getattr(cfg, "head_dim", cfg.hidden_size // self.num_heads))
325	
326	        for parameter in self.src.parameters():
327	            parameter.requires_grad_(False)
328	
329	        self.gate_score_kv = nn.Parameter(torch.full((self.num_key_value_heads,), gate_init, device=device))
330	        self._hook_handles = []
331	        if hasattr(self.src, "k_proj") and isinstance(self.src.k_proj, nn.Module):
332	            self._hook_handles.append(self.src.k_proj.register_forward_hook(self._k_hook))
333	        if hasattr(self.src, "v_proj") and isinstance(self.src.v_proj, nn.Module):
334	            self._hook_handles.append(self.src.v_proj.register_forward_hook(self._v_hook))
335	
336	    def _compute_kv_gate(self, dtype: torch.dtype) -> torch.Tensor:
337	        if getattr(self, "_rescale_mode", False) and hasattr(self, "eval_keep_mask_kv"):
338	            mask = self.eval_keep_mask_kv.to(dtype)
339	            alpha = getattr(self, "rescale_alpha", 0.5)
340	            scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.to(dtype))
341	            return mask * scale
342	        if self.training and hasattr(self, "_batch_mask"):
343	            hard_mask = self._batch_mask.to(dtype)
344	            soft_prob = torch.sigmoid(self.gate_score_kv / self.tau).to(dtype)
345	            return hard_mask + (soft_prob - soft_prob.detach())
346	        if hasattr(self, "eval_keep_mask_kv"):
347	            return self.eval_keep_mask_kv.to(dtype)
348	        return torch.sigmoid(self.gate_score_kv / self.tau).to(dtype)
349	
350	    def _apply_gate(self, out: torch.Tensor) -> torch.Tensor:
351	        if (not torch.is_tensor(out)) or out.dim() != 3:
352	            return out
353	        num_kv_heads, head_dim = int(self.num_key_value_heads), int(self.head_dim)
354	        expected = num_kv_heads * head_dim
355	        z = self._compute_kv_gate(out.dtype).view(1, 1, num_kv_heads, 1)
356	        if out.shape[-1] == expected:
357	            batch_size, seq_len, channels = out.shape
358	            gated = out.view(batch_size, seq_len, num_kv_heads, head_dim) * z
359	            return gated.view(batch_size, seq_len, channels)
360	        if out.shape[1] == expected:
361	            batch_size, channels, seq_len = out.shape
362	            gated = out.view(batch_size, num_kv_heads, head_dim, seq_len) * z.permute(0, 2, 3, 1)
363	            return gated.view(batch_size, channels, seq_len)
364	        return out
365	
366	    def _k_hook(self, module, inputs, output):
367	        del module, inputs
368	        return self._apply_gate(output)
369	
370	    def _v_hook(self, module, inputs, output):
371	        del module, inputs
372	        return self._apply_gate(output)
373	
374	    def forward(self, *args, **kwargs):
375	        return self.src(*args, **kwargs)
376	
377	    @torch.no_grad()
378	    def register_hard_mask_kv(self, keep_mask_kv: torch.Tensor) -> None:
379	        if hasattr(self, "eval_keep_mask_kv"):
380	            self.eval_keep_mask_kv.data = keep_mask_kv.float()
381	        else:
382	            self.register_buffer("eval_keep_mask_kv", keep_mask_kv.float())
383	
384	    @torch.no_grad()
385	    def materialize_pruning(self):
386	        if not hasattr(self, "eval_keep_mask_kv"):
387	            return self.src
388	
389	        keep_kv = self.eval_keep_mask_kv.to(torch.bool)
390	        if keep_kv.sum() == 0:
391	            keep_kv = keep_kv.clone()
392	            keep_kv[0] = True
393	
394	        num_heads = int(self.num_heads)
395	        num_kv_heads = int(self.num_key_value_heads)
396	        head_dim = int(self.head_dim)
397	        group_size = max(1, num_heads // max(1, num_kv_heads))
398	        keep_heads = keep_kv.repeat_interleave(group_size)
399	
400	        scale_keep_kv = None
401	        if getattr(self, "_rescale_mode", False) and hasattr(self, "gate_score_kv"):
402	            alpha = getattr(self, "rescale_alpha", 0.5)
403	            full_scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.detach().to(self.src.k_proj.weight.dtype))
404	            scale_keep_kv = full_scale[keep_kv]
405	
406	        def prune_q_out(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:
407	            weight = linear.weight.data
408	            out_features, in_features = weight.shape
409	            assert out_features == num_heads * head_dim
410	            weight = weight.view(num_heads, head_dim, in_features)[keep_mask_h, :, :]
411	            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(
412	                weight.device, dtype=weight.dtype
413	            )
414	            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))
415	            if linear.bias is not None:
416	                bias = linear.bias.data.view(num_heads, head_dim)[keep_mask_h, :].reshape(-1)
417	                new_linear.bias.data.copy_(bias)
418	            return new_linear
419	
420	        def prune_kv_out(linear: nn.Linear, keep_mask: torch.Tensor, scale_vec: torch.Tensor | None = None) -> nn.Linear:
421	            weight = linear.weight.data
422	            out_features, in_features = weight.shape
423	            assert out_features == num_kv_heads * head_dim
424	            weight = weight.view(num_kv_heads, head_dim, in_features)[keep_mask, :, :]
425	            if scale_vec is not None:
426	                weight = scale_vec.view(-1, 1, 1) * weight
427	            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(
428	                weight.device, dtype=weight.dtype
429	            )
430	            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))
431	            if linear.bias is not None:
432	                bias = linear.bias.data.view(num_kv_heads, head_dim)[keep_mask, :].reshape(-1)
433	                new_linear.bias.data.copy_(bias)
434	            return new_linear
435	
436	        def prune_o_in(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:
437	            weight = linear.weight.data
438	            out_features, in_features = weight.shape
439	            assert in_features == num_heads * head_dim
440	            weight = weight.view(out_features, num_heads, head_dim)[:, keep_mask_h, :].reshape(out_features, -1)
441	            new_linear = nn.Linear(weight.shape[1], out_features, bias=(linear.bias is not None)).to(
442	                weight.device, dtype=weight.dtype
443	            )
444	            new_linear.weight.data.copy_(weight)
445	            if linear.bias is not None:
446	                new_linear.bias.data.copy_(linear.bias.data)
447	            return new_linear
448	
449	        self.src.q_proj = prune_q_out(self.src.q_proj, keep_heads)
450	        self.src.k_proj = prune_kv_out(self.src.k_proj, keep_kv, scale_keep_kv)
451	        self.src.v_proj = prune_kv_out(self.src.v_proj, keep_kv, scale_keep_kv)
452	        self.src.o_proj = prune_o_in(self.src.o_proj, keep_heads)
453	
454	        self.src.num_heads = int(keep_heads.sum().item())
455	        self.src.num_key_value_heads = int(keep_kv.sum().item())
456	        self.src.num_key_value_groups = max(1, self.src.num_heads // max(1, self.src.num_key_value_heads))
457	        self.src.head_dim = head_dim
458	        if hasattr(self.src, "hidden_size"):
459	            self.src.hidden_size = int(self.src.num_heads * head_dim)
460	
461	        for handle in self._hook_handles:
462	            handle.remove()
463	        self._hook_handles = []
464	        return self.src
465	
466	
467	@torch.no_grad()
468	def attach_pruning_gates(model, gate_init: float, tau: float, device: str, model_family: str = "auto") -> None:
469	    family = infer_model_family(model) if model_family == "auto" else model_family.lower()
470	    for layer_idx, block in enumerate(get_transformer_layers(model)):
471	        if family == "qwen":
472	            block.mlp = QwenMLPGate(model.config, block.mlp, gate_init=gate_init, tau=tau, device=device)
473	            block.self_attn = QwenAttnGate(
474	                model.config,
475	                layer_idx,
476	                block.self_attn,
477	                gate_init=gate_init,
478	                tau=tau,
479	                device=device,
480	            )
481	        else:
482	            block.mlp = LlamaMLPGate(model.config, block.mlp, gate_init=gate_init, tau=tau, device=device)
483	            block.self_attn = LlamaAttnGate(
484	                model.config,
485	                layer_idx,
486	                block.self_attn,
487	                gate_init=gate_init,
488	                tau=tau,
489	                device=device,
490	            )
491	
492	
493	def get_decoder_layers(model):
494	    return get_transformer_layers(model)
495	
496	
497	def inject_gates(model, gate_init: float, tau: float, device: str, model_family: str = "auto") -> None:
498	    attach_pruning_gates(model, gate_init=gate_init, tau=tau, device=device, model_family=model_family)
499	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "36e53dfb-f8c7-4af6-9f41-12330fb2af9b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/gates.py",
      "content": "from __future__ import annotations\n\nimport torch\nimport torch.nn as nn\nfrom transformers.activations import ACT2FN\nfrom transformers.models.llama.modeling_llama import (\n    ALL_ATTENTION_FUNCTIONS,\n    apply_rotary_pos_emb,\n    eager_attention_forward,\n)\n\n\ndef get_transformer_layers(model):\n    if hasattr(model, \"model\") and hasattr(model.model, \"layers\"):\n        return list(model.model.layers)\n    raise RuntimeError(\"Unable to locate decoder layers at model.model.layers.\")\n\n\ndef infer_model_family(model_or_config) -> str:\n    config = getattr(model_or_config, \"config\", model_or_config)\n    model_type = str(getattr(config, \"model_type\", \"\")).lower()\n    architectures = \" \".join(getattr(config, \"architectures\", []) or []).lower()\n    if \"qwen\" in model_type or \"qwen\" in architectures:\n        return \"qwen\"\n    return \"llama\"\n\n\nclass LlamaMLPGate(nn.Module):\n    def __init__(self, cfg, src: nn.Module, gate_init: float, tau: float, device: str):\n        super().__init__()\n        self.hidden_size = cfg.hidden_size\n        self.intermediate_size = cfg.intermediate_size\n        self.act_fn = ACT2FN[cfg.hidden_act]\n        self.tau = tau\n\n        self.gate_proj = src.gate_proj\n        self.up_proj = src.up_proj\n        self.down_proj = src.down_proj\n        for parameter in (\n            list(self.gate_proj.parameters())\n            + list(self.up_proj.parameters())\n            + list(self.down_proj.parameters())\n        ):\n            parameter.requires_grad_(False)\n\n        self.gate_score = nn.Parameter(torch.full((self.intermediate_size,), gate_init, device=device))\n\n    def forward(self, x: torch.Tensor) -> torch.Tensor:\n        up = self.up_proj(x)\n        gate = self.act_fn(self.gate_proj(x))\n        inter = up * gate\n        act_dtype = inter.dtype\n\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"eval_keep_mask\"):\n            mask = self.eval_keep_mask.to(act_dtype).view(1, 1, -1)\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            scale = 1.0 + alpha * torch.tanh(self.gate_score.to(act_dtype)).view(1, 1, -1)\n            z = mask * scale\n            return self.down_proj(inter * z)\n\n        if self.training and hasattr(self, \"_batch_mask\"):\n            hard_mask = self._batch_mask.to(act_dtype)\n            soft_prob = torch.sigmoid(self.gate_score / self.tau).to(act_dtype).view(1, 1, -1)\n            z = hard_mask + (soft_prob - soft_prob.detach())\n        elif hasattr(self, \"eval_keep_mask\"):\n            z = self.eval_keep_mask.to(act_dtype).view(1, 1, -1)\n        else:\n            z = torch.sigmoid(self.gate_score / self.tau).to(act_dtype).view(1, 1, -1)\n\n        return self.down_proj(inter * z)\n\n    @torch.no_grad()\n    def register_hard_mask(self, keep_mask_1d: torch.Tensor) -> None:\n        if hasattr(self, \"eval_keep_mask\"):\n            self.eval_keep_mask.data = keep_mask_1d.float()\n        else:\n            self.register_buffer(\"eval_keep_mask\", keep_mask_1d.float())\n\n    @torch.no_grad()\n    def materialize_pruning(self) -> None:\n        if not hasattr(self, \"eval_keep_mask\"):\n            return\n\n        keep = self.eval_keep_mask.to(torch.bool)\n        idx = keep.nonzero(as_tuple=False).squeeze(1)\n        if idx.numel() == 0:\n            idx = torch.tensor([0], device=keep.device)\n\n        scale_keep = None\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"gate_score\"):\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            full_scale = 1.0 + alpha * torch.tanh(self.gate_score.detach().to(self.down_proj.weight.dtype))\n            scale_keep = full_scale[keep]\n\n        def prune_out(linear: nn.Linear, indices: torch.Tensor) -> nn.Linear:\n            weight = linear.weight.data[indices, :].clone()\n            bias = linear.bias.data[indices].clone() if linear.bias is not None else None\n            new_linear = nn.Linear(linear.in_features, indices.numel(), bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight)\n            if bias is not None:\n                new_linear.bias.data.copy_(bias)\n            return new_linear\n\n        def prune_in(linear: nn.Linear, indices: torch.Tensor, scale_vec: torch.Tensor | None = None) -> nn.Linear:\n            weight = linear.weight.data[:, indices].clone()\n            if scale_vec is not None:\n                weight = weight * scale_vec.view(1, -1)\n            new_linear = nn.Linear(indices.numel(), linear.out_features, bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight)\n            if linear.bias is not None:\n                new_linear.bias.data.copy_(linear.bias.data)\n            return new_linear\n\n        self.up_proj = prune_out(self.up_proj, idx)\n        self.gate_proj = prune_out(self.gate_proj, idx)\n        self.down_proj = prune_in(self.down_proj, idx, scale_keep)\n\n        for attr_name in (\"gate_score\", \"eval_keep_mask\", \"_rescale_mode\", \"rescale_alpha\"):\n            if hasattr(self, attr_name):\n                delattr(self, attr_name)\n\n\nclass LlamaAttnGate(nn.Module):\n    def __init__(self, cfg, layer_idx: int, src: nn.Module, gate_init: float, tau: float, device: str):\n        super().__init__()\n        self.config = cfg\n        self.layer_idx = layer_idx\n        self.head_dim = getattr(cfg, \"head_dim\", cfg.hidden_size // cfg.num_attention_heads)\n        self.num_heads = cfg.num_attention_heads\n        self.num_key_value_heads = cfg.num_key_value_heads\n        self.num_key_value_groups = max(1, self.num_heads // max(1, self.num_key_value_heads))\n        self.scaling = self.head_dim ** -0.5\n        self.attention_dropout = cfg.attention_dropout\n        self.is_causal = True\n        self.tau = tau\n\n        self.q_proj = src.q_proj\n        self.k_proj = src.k_proj\n        self.v_proj = src.v_proj\n        self.o_proj = src.o_proj\n        for parameter in (\n            list(self.q_proj.parameters())\n            + list(self.k_proj.parameters())\n            + list(self.v_proj.parameters())\n            + list(self.o_proj.parameters())\n        ):\n            parameter.requires_grad_(False)\n\n        self.gate_score_kv = nn.Parameter(torch.full((self.num_key_value_heads,), gate_init, device=device))\n\n    def forward(\n        self,\n        hidden_states: torch.Tensor,\n        position_embeddings,\n        attention_mask=None,\n        past_key_value=None,\n        cache_position=None,\n        **kwargs,\n    ):\n        input_shape = hidden_states.shape[:-1]\n        hidden_shape = (*input_shape, -1, self.head_dim)\n\n        q = self.q_proj(hidden_states).view(hidden_shape).transpose(1, 2)\n        k = self.k_proj(hidden_states).view(hidden_shape).transpose(1, 2)\n        v = self.v_proj(hidden_states).view(hidden_shape).transpose(1, 2)\n\n        cos, sin = position_embeddings\n        q, k = apply_rotary_pos_emb(q, k, cos, sin)\n\n        if past_key_value is not None:\n            cache_kwargs = {\"sin\": sin, \"cos\": cos, \"cache_position\": cache_position}\n            k, v = past_key_value.update(k, v, self.layer_idx, cache_kwargs)\n\n        act_dtype = q.dtype\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"eval_keep_mask_kv\"):\n            mask_kv = self.eval_keep_mask_kv.to(act_dtype)\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            scale_kv = 1.0 + alpha * torch.tanh(self.gate_score_kv.to(act_dtype))\n            z = mask_kv * scale_kv\n        elif self.training and hasattr(self, \"_batch_mask\"):\n            hard_mask = self._batch_mask.to(act_dtype)\n            soft_prob = torch.sigmoid(self.gate_score_kv / self.tau).to(act_dtype)\n            z = hard_mask + (soft_prob - soft_prob.detach())\n        elif hasattr(self, \"eval_keep_mask_kv\"):\n            z = self.eval_keep_mask_kv.to(act_dtype)\n        else:\n            z = torch.sigmoid(self.gate_score_kv / self.tau).to(act_dtype)\n\n        kv_gate = z.view(1, -1, 1, 1)\n        k = k * kv_gate\n        v = v * kv_gate\n\n        attention_interface = eager_attention_forward\n        if self.config._attn_implementation != \"eager\":\n            if not (\n                self.config._attn_implementation == \"sdpa\"\n                and kwargs.get(\"output_attentions\", False)\n            ):\n                attention_interface = ALL_ATTENTION_FUNCTIONS[self.config._attn_implementation]\n\n        out, attn = attention_interface(\n            self,\n            q,\n            k,\n            v,\n            attention_mask,\n            dropout=0.0 if not self.training else self.attention_dropout,\n            scaling=self.scaling,\n            **kwargs,\n        )\n        out = out.reshape(*input_shape, -1).contiguous()\n        out = self.o_proj(out)\n        return out, attn\n\n    @torch.no_grad()\n    def register_hard_mask_kv(self, keep_mask_kv: torch.Tensor) -> None:\n        if hasattr(self, \"eval_keep_mask_kv\"):\n            self.eval_keep_mask_kv.data = keep_mask_kv.float()\n        else:\n            self.register_buffer(\"eval_keep_mask_kv\", keep_mask_kv.float())\n\n    @torch.no_grad()\n    def materialize_pruning(self) -> None:\n        if not hasattr(self, \"eval_keep_mask_kv\"):\n            return\n\n        keep_kv = self.eval_keep_mask_kv.to(torch.bool)\n        if keep_kv.sum() == 0:\n            keep_kv = keep_kv.clone()\n            keep_kv[0] = True\n\n        num_heads = self.num_heads\n        num_kv_heads = self.num_key_value_heads\n        head_dim = self.head_dim\n        group_size = max(1, num_heads // max(1, num_kv_heads))\n        keep_heads = keep_kv.repeat_interleave(group_size)\n\n        scale_keep_kv = None\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"gate_score_kv\"):\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            full_scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.detach().to(self.k_proj.weight.dtype))\n            scale_keep_kv = full_scale[keep_kv]\n\n        def prune_q_out(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert out_features == num_heads * head_dim\n            weight = weight.view(num_heads, head_dim, in_features)[keep_mask_h, :, :]\n            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))\n            if linear.bias is not None:\n                bias = linear.bias.data.view(num_heads, head_dim)[keep_mask_h, :].reshape(-1)\n                new_linear.bias.data.copy_(bias)\n            return new_linear\n\n        def prune_kv_out(\n            linear: nn.Linear,\n            keep_mask: torch.Tensor,\n            scale_vec: torch.Tensor | None = None,\n        ) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert out_features == num_kv_heads * head_dim\n            weight = weight.view(num_kv_heads, head_dim, in_features)[keep_mask, :, :]\n            if scale_vec is not None:\n                weight = scale_vec.view(-1, 1, 1) * weight\n            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))\n            if linear.bias is not None:\n                bias = linear.bias.data.view(num_kv_heads, head_dim)[keep_mask, :].reshape(-1)\n                new_linear.bias.data.copy_(bias)\n            return new_linear\n\n        def prune_o_in(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert in_features == num_heads * head_dim\n            weight = weight.view(out_features, num_heads, head_dim)[:, keep_mask_h, :].reshape(out_features, -1)\n            new_linear = nn.Linear(weight.shape[1], out_features, bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight)\n            if linear.bias is not None:\n                new_linear.bias.data.copy_(linear.bias.data)\n            return new_linear\n\n        self.q_proj = prune_q_out(self.q_proj, keep_heads)\n        self.k_proj = prune_kv_out(self.k_proj, keep_kv, scale_keep_kv)\n        self.v_proj = prune_kv_out(self.v_proj, keep_kv, scale_keep_kv)\n        self.o_proj = prune_o_in(self.o_proj, keep_heads)\n\n        self.num_heads = int(keep_heads.sum().item())\n        self.num_key_value_heads = int(keep_kv.sum().item())\n        self.num_key_value_groups = max(1, self.num_heads // max(1, self.num_key_value_heads))\n\n        for attr_name in (\"gate_score_kv\", \"eval_keep_mask_kv\", \"_rescale_mode\", \"rescale_alpha\"):\n            if hasattr(self, attr_name):\n                delattr(self, attr_name)\n\n\nclass QwenMLPGate(LlamaMLPGate):\n    pass\n\n\nclass QwenAttnGate(nn.Module):\n    def __init__(self, cfg, layer_idx: int, src: nn.Module, gate_init: float, tau: float, device: str):\n        super().__init__()\n        del layer_idx\n        self.config = cfg\n        self.src = src\n        self.tau = tau\n        self.num_heads = int(getattr(cfg, \"num_attention_heads\", getattr(src, \"num_heads\", 0)))\n        self.num_key_value_heads = int(getattr(cfg, \"num_key_value_heads\", getattr(src, \"num_key_value_heads\", 0)))\n        if self.num_heads <= 0 or self.num_key_value_heads <= 0:\n            raise RuntimeError(\"Unable to infer num_attention_heads / num_key_value_heads for Qwen.\")\n        self.head_dim = int(getattr(cfg, \"head_dim\", cfg.hidden_size // self.num_heads))\n\n        for parameter in self.src.parameters():\n            parameter.requires_grad_(False)\n\n        self.gate_score_kv = nn.Parameter(torch.full((self.num_key_value_heads,), gate_init, device=device))\n        self._hook_handles = []\n        if hasattr(self.src, \"k_proj\") and isinstance(self.src.k_proj, nn.Module):\n            self._hook_handles.append(self.src.k_proj.register_forward_hook(self._k_hook))\n        if hasattr(self.src, \"v_proj\") and isinstance(self.src.v_proj, nn.Module):\n            self._hook_handles.append(self.src.v_proj.register_forward_hook(self._v_hook))\n\n    def _compute_kv_gate(self, dtype: torch.dtype) -> torch.Tensor:\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"eval_keep_mask_kv\"):\n            mask = self.eval_keep_mask_kv.to(dtype)\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.to(dtype))\n            return mask * scale\n        if self.training and hasattr(self, \"_batch_mask\"):\n            hard_mask = self._batch_mask.to(dtype)\n            soft_prob = torch.sigmoid(self.gate_score_kv / self.tau).to(dtype)\n            return hard_mask + (soft_prob - soft_prob.detach())\n        if hasattr(self, \"eval_keep_mask_kv\"):\n            return self.eval_keep_mask_kv.to(dtype)\n        return torch.sigmoid(self.gate_score_kv / self.tau).to(dtype)\n\n    def _apply_gate(self, out: torch.Tensor) -> torch.Tensor:\n        if (not torch.is_tensor(out)) or out.dim() != 3:\n            return out\n        num_kv_heads, head_dim = int(self.num_key_value_heads), int(self.head_dim)\n        expected = num_kv_heads * head_dim\n        z = self._compute_kv_gate(out.dtype).view(1, 1, num_kv_heads, 1)\n        if out.shape[-1] == expected:\n            batch_size, seq_len, channels = out.shape\n            gated = out.view(batch_size, seq_len, num_kv_heads, head_dim) * z\n            return gated.view(batch_size, seq_len, channels)\n        if out.shape[1] == expected:\n            batch_size, channels, seq_len = out.shape\n            gated = out.view(batch_size, num_kv_heads, head_dim, seq_len) * z.permute(0, 2, 3, 1)\n            return gated.view(batch_size, channels, seq_len)\n        return out\n\n    def _k_hook(self, module, inputs, output):\n        del module, inputs\n        return self._apply_gate(output)\n\n    def _v_hook(self, module, inputs, output):\n        del module, inputs\n        return self._apply_gate(output)\n\n    def forward(self, *args, **kwargs):\n        return self.src(*args, **kwargs)\n\n    @torch.no_grad()\n    def register_hard_mask_kv(self, keep_mask_kv: torch.Tensor) -> None:\n        if hasattr(self, \"eval_keep_mask_kv\"):\n            self.eval_keep_mask_kv.data = keep_mask_kv.float()\n        else:\n            self.register_buffer(\"eval_keep_mask_kv\", keep_mask_kv.float())\n\n    @torch.no_grad()\n    def materialize_pruning(self):\n        if not hasattr(self, \"eval_keep_mask_kv\"):\n            return self.src\n\n        keep_kv = self.eval_keep_mask_kv.to(torch.bool)\n        if keep_kv.sum() == 0:\n            keep_kv = keep_kv.clone()\n            keep_kv[0] = True\n\n        num_heads = int(self.num_heads)\n        num_kv_heads = int(self.num_key_value_heads)\n        head_dim = int(self.head_dim)\n        group_size = max(1, num_heads // max(1, num_kv_heads))\n        keep_heads = keep_kv.repeat_interleave(group_size)\n\n        scale_keep_kv = None\n        if getattr(self, \"_rescale_mode\", False) and hasattr(self, \"gate_score_kv\"):\n            alpha = getattr(self, \"rescale_alpha\", 0.5)\n            full_scale = 1.0 + alpha * torch.tanh(self.gate_score_kv.detach().to(self.src.k_proj.weight.dtype))\n            scale_keep_kv = full_scale[keep_kv]\n\n        def prune_q_out(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert out_features == num_heads * head_dim\n            weight = weight.view(num_heads, head_dim, in_features)[keep_mask_h, :, :]\n            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))\n            if linear.bias is not None:\n                bias = linear.bias.data.view(num_heads, head_dim)[keep_mask_h, :].reshape(-1)\n                new_linear.bias.data.copy_(bias)\n            return new_linear\n\n        def prune_kv_out(linear: nn.Linear, keep_mask: torch.Tensor, scale_vec: torch.Tensor | None = None) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert out_features == num_kv_heads * head_dim\n            weight = weight.view(num_kv_heads, head_dim, in_features)[keep_mask, :, :]\n            if scale_vec is not None:\n                weight = scale_vec.view(-1, 1, 1) * weight\n            new_linear = nn.Linear(in_features, int(weight.numel() // in_features), bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight.reshape(new_linear.weight.shape))\n            if linear.bias is not None:\n                bias = linear.bias.data.view(num_kv_heads, head_dim)[keep_mask, :].reshape(-1)\n                new_linear.bias.data.copy_(bias)\n            return new_linear\n\n        def prune_o_in(linear: nn.Linear, keep_mask_h: torch.Tensor) -> nn.Linear:\n            weight = linear.weight.data\n            out_features, in_features = weight.shape\n            assert in_features == num_heads * head_dim\n            weight = weight.view(out_features, num_heads, head_dim)[:, keep_mask_h, :].reshape(out_features, -1)\n            new_linear = nn.Linear(weight.shape[1], out_features, bias=(linear.bias is not None)).to(\n                weight.device, dtype=weight.dtype\n            )\n            new_linear.weight.data.copy_(weight)\n            if linear.bias is not None:\n                new_linear.bias.data.copy_(linear.bias.data)\n            return new_linear\n\n        self.src.q_proj = prune_q_out(self.src.q_proj, keep_heads)\n        self.src.k_proj = prune_kv_out(self.src.k_proj, keep_kv, scale_keep_kv)\n        self.src.v_proj = prune_kv_out(self.src.v_proj, keep_kv, scale_keep_kv)\n        self.src.o_proj = prune_o_in(self.src.o_proj, keep_heads)\n\n        self.src.num_heads = int(keep_heads.sum().item())\n        self.src.num_key_value_heads = int(keep_kv.sum().item())\n        self.src.num_key_value_groups = max(1, self.src.num_heads // max(1, self.src.num_key_value_heads))\n        self.src.head_dim = head_dim\n        if hasattr(self.src, \"hidden_size\"):\n            self.src.hidden_size = int(self.src.num_heads * head_dim)\n\n        for handle in self._hook_handles:\n            handle.remove()\n        self._hook_handles = []\n        return self.src\n\n\n@torch.no_grad()\ndef attach_pruning_gates(model, gate_init: float, tau: float, device: str, model_family: str = \"auto\") -> None:\n    family = infer_model_family(model) if model_family == \"auto\" else model_family.lower()\n    for layer_idx, block in enumerate(get_transformer_layers(model)):\n        if family == \"qwen\":\n            block.mlp = QwenMLPGate(model.config, block.mlp, gate_init=gate_init, tau=tau, device=device)\n            block.self_attn = QwenAttnGate(\n                model.config,\n                layer_idx,\n                block.self_attn,\n                gate_init=gate_init,\n                tau=tau,\n                device=device,\n            )\n        else:\n            block.mlp = LlamaMLPGate(model.config, block.mlp, gate_init=gate_init, tau=tau, device=device)\n            block.self_attn = LlamaAttnGate(\n                model.config,\n                layer_idx,\n                block.self_attn,\n                gate_init=gate_init,\n                tau=tau,\n                device=device,\n            )\n\n\ndef get_decoder_layers(model):\n    return get_transformer_layers(model)\n\n\ndef inject_gates(model, gate_init: float, tau: float, device: str, model_family: str = \"auto\") -> None:\n    attach_pruning_gates(model, gate_init=gate_init, tau=tau, device=device, model_family=model_family)\n",
      "numLines": 499,
      "startLine": 1,
      "totalLines": 499
    }
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-14T08:21:30.996Z_

<details><summary>↩ Tool result · `toolu_017XoQG6t4AxTs42GSThFDSu`</summary>

```text
1	from __future__ import annotations
2	
3	import csv
4	import json
5	import os
6	import random
7	from typing import Any
8	
9	import torch
10	from safetensors.torch import save_file as st_save_file
11	from torch.utils.data import DataLoader
12	from tqdm import tqdm
13	from transformers import AutoModelForCausalLM, AutoTokenizer
14	
15	from config import PruningConfig
16	from data import TokenBlockDataset, load_text_dataset
17	from evals import evaluate_accuracy, evaluate_perplexity
18	from gates import (
19	    LlamaAttnGate,
20	    LlamaMLPGate,
21	    QwenAttnGate,
22	    QwenMLPGate,
23	    attach_pruning_gates,
24	    get_transformer_layers,
25	)
26	from rebuild import load_pruned_model
27	
28	
29	def set_seed(seed: int) -> None:
30	    random.seed(seed)
31	    torch.manual_seed(seed)
32	    if torch.cuda.is_available():
33	        torch.cuda.manual_seed_all(seed)
34	
35	
36	@torch.no_grad()
37	def compute_ffn_unit_cost(device: str) -> torch.Tensor:
38	    return torch.tensor(1.0, device=device)
39	
40	
41	@torch.no_grad()
42	def compute_attention_group_cost(cfg: Any, device: str) -> torch.Tensor:
43	    num_heads = cfg.num_attention_heads
44	    num_kv_heads = cfg.num_key_value_heads
45	    head_dim = getattr(cfg, "head_dim", cfg.hidden_size // max(1, num_heads))
46	    group_size = max(1, num_heads // max(1, num_kv_heads))
47	    alpha_param = ((2 * group_size + 2) * head_dim) / 3.0
48	    return torch.tensor(alpha_param, dtype=torch.float32, device=device)
49	
50	
51	@torch.no_grad()
52	def build_batch_budget_masks(
53	    model: Any,
54	    f_cost: torch.Tensor,
55	    a_cost: torch.Tensor,
56	    keep_ratio: float,
57	    tau: float,
58	):
59	    scores, costs, holders = [], [], []
60	
61	    for layer_idx, block in enumerate(get_transformer_layers(model)):
62	        if hasattr(block.mlp, "gate_score"):
63	            values = torch.sigmoid(block.mlp.gate_score.detach().float() / tau)
64	            scores.append(values)
65	            costs.append(torch.full_like(values, f_cost))
66	            holders.append(("ffn", block.mlp, values.numel(), layer_idx))
67	        if hasattr(block.self_attn, "gate_score_kv"):
68	            values = torch.sigmoid(block.self_attn.gate_score_kv.detach().float() / tau)
69	            scores.append(values)
70	            costs.append(torch.full_like(values, a_cost))
71	            holders.append(("kv", block.self_attn, values.numel(), layer_idx))
72	
73	    if not scores:
74	        return []
75	
76	    score_tensor = torch.cat(scores)
77	    cost_tensor = torch.cat(costs)
78	    budget = max(1.0, cost_tensor.sum().item() * keep_ratio)
79	
80	    order = torch.argsort(score_tensor, descending=True)
81	    cumsum = torch.cumsum(cost_tensor[order], dim=0)
82	    chosen = order[cumsum <= budget]
83	    if chosen.numel() == 0:
84	        chosen = order[:1]
85	
86	    masks, base = [], 0
87	    for kind, module, length, layer_idx in holders:
88	        take = torch.zeros(length, dtype=torch.bool, device=score_tensor.device)
89	        selected = chosen[(chosen >= base) & (chosen < base + length)] - base
90	        if selected.numel() > 0:
91	            take[selected.long()] = True
92	        masks.append((kind, module, take, layer_idx))
93	        base += length
94	
95	    per_layer: dict[int, dict[str, tuple[Any, torch.Tensor]]] = {}
96	    for kind, module, take, layer_idx in masks:
97	        per_layer.setdefault(layer_idx, {})[kind] = (module, take)
98	
99	    for layer_idx, grouped in per_layer.items():
100	        if "ffn" in grouped:
101	            module, take = grouped["ffn"]
102	            if take.sum() == 0:
103	                score = torch.sigmoid(module.gate_score.detach().float() / tau)
104	                take[torch.argmax(score).item()] = True
105	        if "kv" in grouped:
106	            module, take = grouped["kv"]
107	            if take.sum() == 0:
108	                score = torch.sigmoid(module.gate_score_kv.detach().float() / tau)
109	                take[torch.argmax(score).item()] = True
110	
111	    return [(kind, module, take) for kind, module, take, _ in masks]
112	
113	
114	def build_train_dataloader(tokenizer: Any, config: PruningConfig) -> DataLoader:
115	    raw_dataset = load_text_dataset(config.train_dataset_name, config.train_split)
116	    dataset = TokenBlockDataset(raw_dataset, tokenizer, config.max_len)
117	    dataset = torch.utils.data.Subset(dataset, list(range(min(config.num_samples, len(dataset)))))
118	    return DataLoader(dataset, batch_size=config.batch_size, shuffle=True)
119	
120	
121	def train_gates(model: Any, tokenizer: Any, config: PruningConfig) -> None:
122	    dataloader = build_train_dataloader(tokenizer, config)
123	    f_cost = compute_ffn_unit_cost(config.device)
124	    a_cost = compute_attention_group_cost(model.config, config.device)
125	
126	    f_params, a_params = [], []
127	    for name, parameter in model.named_parameters():
128	        if not parameter.requires_grad:
129	            continue
130	        if name.endswith("mlp.gate_score"):
131	            f_params.append(parameter)
132	        elif name.endswith("self_attn.gate_score_kv"):
133	            a_params.append(parameter)
134	
135	    optimizer = torch.optim.AdamW(
136	        [{"params": f_params, "lr": config.lr}, {"params": a_params, "lr": config.lr}],
137	        betas=(0.9, 0.99),
138	        eps=1e-8,
139	        weight_decay=0.0,
140	    )
141	
142	    model.train()
143	    for epoch in range(config.epochs):
144	        progress = tqdm(dataloader, desc=f"Epoch {epoch + 1}")
145	        for batch in progress:
146	            batch = {key: value.to(config.device) for key, value in batch.items()}
147	            masks = build_batch_budget_masks(model, f_cost, a_cost, config.keep_ratio, config.tau)
148	            for kind, module, take in masks:
149	                module._batch_mask = take.view(1, 1, -1) if kind == "ffn" else take
150	
151	            output = model(**batch, labels=batch["input_ids"])
152	            loss = output.loss
153	            optimizer.zero_grad(set_to_none=True)
154	            loss.backward()
155	            optimizer.step()
156	
157	            for _, module, _ in masks:
158	                if hasattr(module, "_batch_mask"):
159	                    delattr(module, "_batch_mask")
160	
161	            with torch.no_grad():
162	                mean_ffn = []
163	                mean_kv = []
164	                for block in get_transformer_layers(model):
165	                    if hasattr(block.mlp, "gate_score"):
166	                        mean_ffn.append(torch.sigmoid(block.mlp.gate_score / config.tau).mean().item())
167	                    if hasattr(block.self_attn, "gate_score_kv"):
168	                        mean_kv.append(torch.sigmoid(block.self_attn.gate_score_kv / config.tau).mean().item())
169	            progress.set_postfix(
170	                loss=f"{loss.item():.3f}",
171	                p_ffn=f"{sum(mean_ffn) / max(1, len(mean_ffn)):.3f}",
172	                p_kv=f"{sum(mean_kv) / max(1, len(mean_kv)):.3f}",
173	            )
174	
175	
176	@torch.no_grad()
177	def apply_final_hard_masks(model: Any, config: PruningConfig) -> None:
178	    f_cost = compute_ffn_unit_cost(config.device)
179	    a_cost = compute_attention_group_cost(model.config, config.device)
180	    masks = build_batch_budget_masks(model, f_cost, a_cost, keep_ratio=config.keep_ratio, tau=config.tau)
181	
182	    for kind, module, take in masks:
183	        if kind == "ffn":
184	            module.register_hard_mask(take)
185	        else:
186	            module.register_hard_mask_kv(take)
187	
188	    for block in get_transformer_layers(model):
189	        if hasattr(block.mlp, "eval_keep_mask"):
190	            take = block.mlp.eval_keep_mask.to(torch.bool)
191	            if take.sum() == 0:
192	                score = torch.sigmoid(block.mlp.gate_score.detach().float() / config.tau)
193	                take[torch.argmax(score).item()] = True
194	                block.mlp.register_hard_mask(take)
195	        if hasattr(block.self_attn, "eval_keep_mask_kv"):
196	            take = block.self_attn.eval_keep_mask_kv.to(torch.bool)
197	            if take.sum() == 0:
198	                score = torch.sigmoid(block.self_attn.gate_score_kv.detach().float() / config.tau)
199	                take[torch.argmax(score).item()] = True
200	                block.self_attn.register_hard_mask_kv(take)
201	
202	
203	@torch.no_grad()
204	def summarize_pruning_masks(model: Any, config: PruningConfig) -> list[dict[str, float]]:
205	    device = next(model.parameters()).device
206	    cfg = model.config
207	    f_unit = compute_ffn_unit_cost(str(device)).to(device)
208	    a_unit = compute_attention_group_cost(cfg, str(device)).to(device)
209	    num_heads = cfg.num_attention_heads
210	    num_kv_heads = cfg.num_key_value_heads
211	    group_size = max(1, num_heads // max(1, num_kv_heads))
212	
213	    rows = []
214	    total_ffn_all = total_ffn_keep = 0
215	    total_kv_all = total_kv_keep = 0
216	    total_params_kept = 0.0
217	
218	    for layer_idx, block in enumerate(get_transformer_layers(model)):
219	        if hasattr(block.mlp, "eval_keep_mask"):
220	            f_keep = int(block.mlp.eval_keep_mask.to(torch.bool).sum().item())
221	            f_total = int(block.mlp.eval_keep_mask.numel())
222	        else:
223	            score = getattr(block.mlp, "gate_score", None)
224	            f_total = int(score.numel()) if score is not None else getattr(block.mlp.up_proj, "out_features", 0)
225	            f_keep = f_total
226	
227	        if hasattr(block.self_attn, "eval_keep_mask_kv"):
228	            a_keep = int(block.self_attn.eval_keep_mask_kv.to(torch.bool).sum().item())
229	            a_total = int(block.self_attn.eval_keep_mask_kv.numel())
230	        else:
231	            score = getattr(block.self_attn, "gate_score_kv", None)
232	            a_total = int(score.numel()) if score is not None else cfg.num_key_value_heads
233	            a_keep = a_total
234	
235	        total_ffn_all += f_total
236	        total_ffn_keep += f_keep
237	        total_kv_all += a_total
238	        total_kv_keep += a_keep
239	        kept_cost = float(f_unit) * f_keep + float(a_unit) * a_keep
240	        total_params_kept += kept_cost
241	
242	        rows.append(
243	            {
244	                "layer": layer_idx,
245	                "ffn_keep": f_keep,
246	                "ffn_total": f_total,
247	                "ffn_ratio": f_keep / max(1, f_total),
248	                "kv_keep": a_keep,
249	                "kv_total": a_total,
250	                "kv_ratio": a_keep / max(1, a_total),
251	                "head_keep_eq": int(a_keep * group_size),
252	                "head_total": int(num_heads),
253	                "head_ratio_eq": a_keep * group_size / max(1, num_heads),
254	                "~params_kept": int(kept_cost),
255	            }
256	        )
257	
258	    total_prunable = float(f_unit) * total_ffn_all + float(a_unit) * total_kv_all
259	    target_cost = total_prunable * config.keep_ratio
260	    diff = total_params_kept - target_cost
261	    pct = (diff / max(1.0, target_cost)) * 100.0
262	
263	    print("\n[Final HARD Masks Report] (KV-based)")
264	    print("-" * 112)
265	    print(
266	        f"{'Layer':>5} | {'FFN keep/total (ratio)':>26} | {'KV keep/total (ratio)':>26} | "
267	        f"{'Head≈keep/total':>18} | {'~Params kept':>14}"
268	    )
269	    print("-" * 112)
270	    for row in rows:
271	        print(
272	            f"{row['layer']:5d} | {row['ffn_keep']:5d}/{row['ffn_total']:5d} ({row['ffn_ratio'] * 100:6.2f}%) | "
273	            f"{row['kv_keep']:4d}/{row['kv_total']:4d} ({row['kv_ratio'] * 100:6.2f}%) | "
274	            f"{row['head_keep_eq']:4d}/{row['head_total']:4d} ({row['head_ratio_eq'] * 100:6.2f}%) | "
275	            f"{row['~params_kept']:14,d}"
276	        )
277	    print("-" * 112)
278	    print(
279	        f"TOTAL: FFN {total_ffn_keep}/{total_ffn_all} ({(total_ffn_keep / max(1, total_ffn_all)) * 100:.2f}%) | "
280	        f"KV {total_kv_keep}/{total_kv_all} ({(total_kv_keep / max(1, total_kv_all)) * 100:.2f}%) | "
281	        f"~Params kept ≈ {int(total_params_kept):,}"
282	    )
283	    print(f"TARGET keep_ratio={config.keep_ratio:.3f}: ~Params ≈ {int(target_cost):,}")
284	    print(f"DIFF: {int(diff):,} ({pct:+.3f}%)\n")
285	
286	    if config.report_csv:
287	        os.makedirs(os.path.dirname(config.report_csv), exist_ok=True)
288	        with open(config.report_csv, "w", newline="", encoding="utf-8") as handle:
289	            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
290	            writer.writeheader()
291	            writer.writerows(rows)
292	        print(f"[Saved] layer-wise mask report -> {config.report_csv}")
293	
294	    return rows
295	
296	
297	@torch.no_grad()
298	def materialize_all_pruning(model: Any) -> None:
299	    for block in get_transformer_layers(model):
300	        if hasattr(block.mlp, "materialize_pruning"):
301	            block.mlp.materialize_pruning()
302	        if hasattr(block.self_attn, "materialize_pruning"):
303	            new_attn = block.self_attn.materialize_pruning()
304	            if new_attn is not None:
305	                block.self_attn = new_attn
306	
307	
308	@torch.no_grad()
309	def export_pruned_state_dict_safetensors(model: Any, path: str) -> None:
310	    state_dict = model.state_dict()
311	    cpu_state_dict = {key: value.detach().cpu() for key, value in state_dict.items() if torch.is_tensor(value)}
312	    os.makedirs(os.path.dirname(path), exist_ok=True)
313	    st_save_file(cpu_state_dict, path)
314	    print(f"[Saved] pruned state_dict (safetensors) -> {path}")
315	
316	
317	@torch.no_grad()
318	def export_pruning_metadata(model: Any, config: PruningConfig) -> dict[str, Any]:
319	    cfg = model.config
320	    base_head_dim = getattr(cfg, "head_dim", None)
321	    if not isinstance(base_head_dim, int) or base_head_dim <= 0:
322	        base_head_dim = cfg.hidden_size // max(1, getattr(cfg, "num_attention_heads", 1))
323	
324	    num_heads_orig = getattr(cfg, "num_attention_heads", None)
325	    num_kv_heads_orig = getattr(cfg, "num_key_value_heads", None)
326	    if not isinstance(num_heads_orig, int) or num_heads_orig <= 0:
327	        num_heads_orig = getattr(get_transformer_layers(model)[0].self_attn, "num_heads", 1)
328	    if not isinstance(num_kv_heads_orig, int) or num_kv_heads_orig <= 0:
329	        num_kv_heads_orig = getattr(get_transformer_layers(model)[0].self_attn, "num_key_value_heads", 1)
330	    group_size = max(1, num_heads_orig // max(1, num_kv_heads_orig))
331	
332	    export_format = "materialized"
333	    meta = {
334	        "model_id": config.model_id,
335	        "model_family": config.model_family,
336	        "dtype": str(config.dtype),
337	        "export_format": export_format,
338	        "rescale_alpha": float(config.rescale_alpha),
339	        "layers": [],
340	    }
341	    for layer_idx, block in enumerate(get_transformer_layers(model)):
342	        assert hasattr(block.mlp, "eval_keep_mask"), (
343	            f"Layer {layer_idx} mlp missing eval_keep_mask. Run apply_final_hard_masks first."
344	        )
345	        assert hasattr(block.self_attn, "eval_keep_mask_kv"), (
346	            f"Layer {layer_idx} attn missing eval_keep_mask_kv. Run apply_final_hard_masks first."
347	        )
348	
349	        ffn_keep = int(block.mlp.eval_keep_mask.to(torch.bool).sum().item())
350	        kv_mask = block.self_attn.eval_keep_mask_kv.to(torch.bool)
351	        num_kv_heads = int(kv_mask.sum().item())
352	        num_heads = max(1, min(num_heads_orig, num_kv_heads * group_size))
353	        layer_info = {
354	            "ffn_intermediate_size": max(1, ffn_keep),
355	            "num_heads": int(num_heads),
356	            "num_key_value_heads": max(1, int(num_kv_heads)),
357	            "head_dim": int(base_head_dim),
358	        }
359	        meta["layers"].append(layer_info)
360	
361	    os.makedirs(os.path.dirname(config.pruned_meta_path), exist_ok=True)
362	    with open(config.pruned_meta_path, "w", encoding="utf-8") as handle:
363	        json.dump(meta, handle, ensure_ascii=False, indent=2)
364	    print(f"[Saved] meta(from masks) -> {config.pruned_meta_path}")
365	    return meta
366	
367	
368	def train_rescale(model: Any, tokenizer: Any, config: PruningConfig) -> None:
369	    for block in get_transformer_layers(model):
370	        if isinstance(block.mlp, (LlamaMLPGate, QwenMLPGate)):
371	            block.mlp.rescale_alpha = config.rescale_alpha
372	        if isinstance(block.self_attn, (LlamaAttnGate, QwenAttnGate)):
373	            block.self_attn.rescale_alpha = config.rescale_alpha
374	
375	    for parameter in model.parameters():
376	        parameter.requires_grad_(False)
377	
378	    rescale_params = []
379	    for block in get_transformer_layers(model):
380	        if isinstance(block.mlp, (LlamaMLPGate, QwenMLPGate)) and hasattr(block.mlp, "eval_keep_mask"):
381	            with torch.no_grad():
382	                block.mlp.gate_score.zero_()
383	            block.mlp.gate_score.requires_grad_(True)
384	            block.mlp._rescale_mode = True
385	            rescale_params.append(block.mlp.gate_score)
386	        if isinstance(block.self_attn, (LlamaAttnGate, QwenAttnGate)) and hasattr(block.self_attn, "eval_keep_mask_kv"):
387	            with torch.no_grad():
388	                block.self_attn.gate_score_kv.zero_()
389	            block.self_attn.gate_score_kv.requires_grad_(True)
390	            block.self_attn._rescale_mode = True
391	            rescale_params.append(block.self_attn.gate_score_kv)
392	
393	    if not rescale_params:
394	        print("[Stage B] No rescale params found, skip.")
395	        return
396	
397	    optimizer = torch.optim.AdamW(
398	        rescale_params,
399	        lr=config.rescale_lr,
400	        betas=(0.9, 0.99),
401	        eps=1e-8,
402	        weight_decay=0.0,
403	    )
404	
405	    raw_dataset = load_text_dataset("wikitext2", "validation")
406	    dataset = TokenBlockDataset(raw_dataset, tokenizer, config.max_len)
407	    dataset = torch.utils.data.Subset(
408	        dataset,
409	        list(range(min(config.rescale_num_samples, len(dataset)))),
410	    )
411	    dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)
412	
413	    model.train()
414	    for epoch in range(config.rescale_epochs):
415	        progress = tqdm(dataloader, desc=f"[Stage B] Epoch {epoch + 1}")
416	        for batch in progress:
417	            batch = {key: value.to(config.device) for key, value in batch.items()}
418	            output = model(**batch, labels=batch["input_ids"])
419	            loss = output.loss
420	            optimizer.zero_grad(set_to_none=True)
421	            loss.backward()
422	            optimizer.step()
423	            progress.set_postfix(loss=f"{loss.item():.3f}")
424	
425	
426	def load_model_and_tokenizer(config: PruningConfig):
427	    tokenizer = AutoTokenizer.from_pretrained(
428	        config.model_id,
429	        use_fast=False if config.model_family != "qwen" else True,
430	        local_files_only=config.local_only,
431	        trust_remote_code=config.trust_remote_code,
432	        token=config.hf_token,
433	    )
434	    if tokenizer.pad_token is None:
435	        tokenizer.pad_token = tokenizer.eos_token
436	
437	    model = AutoModelForCausalLM.from_pretrained(
438	        config.model_id,
439	        torch_dtype=config.dtype,
440	        local_files_only=config.local_only,
441	        trust_remote_code=config.trust_remote_code,
442	        token=config.hf_token,
443	    ).to(config.device)
444	
445	    torch.backends.cuda.matmul.allow_tf32 = True
446	    torch.backends.cudnn.allow_tf32 = True
447	    return model, tokenizer
448	
449	
450	def run_pruning_pipeline(config: PruningConfig) -> dict[str, Any]:
451	    set_seed(config.seed)
452	    model, tokenizer = load_model_and_tokenizer(config)
453	
454	    attach_pruning_gates(
455	        model,
456	        gate_init=config.gate_init,
457	        tau=config.tau,
458	        device=config.device,
459	        model_family=config.model_family,
460	    )
461	    train_gates(model, tokenizer, config)
462	    apply_final_hard_masks(model, config)
463	    summarize_pruning_masks(model, config)
464	    meta = export_pruning_metadata(model, config)
465	    train_rescale(model, tokenizer, config)
466	
467	    materialize_all_pruning(model)
468	    export_pruned_state_dict_safetensors(model, config.pruned_state_dict_path)
469	
470	    metrics: dict[str, Any] = {"meta": meta}
471	    if config.run_ppl_eval:
472	        eval_model, eval_tokenizer, _ = load_pruned_model(
473	            model_id=config.model_id,
474	            state_dict_path=config.pruned_state_dict_path,
475	            meta_path=config.pruned_meta_path,
476	            torch_dtype=config.dtype,
477	            device=config.device,
478	            use_fast_tokenizer=(config.model_family == "qwen"),
479	            trust_remote_code=config.trust_remote_code,
480	            hf_token=config.hf_token,
481	            local_only=config.local_only,
482	        )
483	        metrics["ppl"] = evaluate_perplexity(
484	            eval_model,
485	            eval_tokenizer,
486	            datasets=config.ppl_datasets,
487	            device=config.device,
488	        )
489	    if config.run_acc_eval:
490	        if not config.run_ppl_eval:
491	            eval_model, eval_tokenizer, _ = load_pruned_model(
492	                model_id=config.model_id,
493	                state_dict_path=config.pruned_state_dict_path,
494	                meta_path=config.pruned_meta_path,
495	                torch_dtype=config.dtype,
496	                device=config.device,
497	                use_fast_tokenizer=(config.model_family == "qwen"),
498	                trust_remote_code=config.trust_remote_code,
499	                hf_token=config.hf_token,
500	                local_only=config.local_only,
501	            )
502	        metrics["acc"] = evaluate_accuracy(eval_model, eval_tokenizer, device=config.device)
503	    print("[Done] Pruning pipeline finished.")
504	    return metrics
505	
506	
507	def ffn_unit_cost(device: str) -> torch.Tensor:
508	    return compute_ffn_unit_cost(device)
509	
510	
511	def attn_kv_group_cost(cfg: Any, device: str) -> torch.Tensor:
512	    return compute_attention_group_cost(cfg, device)
513	
514	
515	def build_batch_budget_mask(
516	    model: Any,
517	    f_cost: torch.Tensor,
518	    a_cost: torch.Tensor,
519	    keep_ratio: float,
520	    tau: float,
521	):
522	    return build_batch_budget_masks(model, f_cost, a_cost, keep_ratio, tau)
523	
524	
525	def final_hardening_apply(model: Any, config: PruningConfig) -> None:
526	    apply_final_hard_masks(model, config)
527	
528	
529	def report_masks(model: Any, config: PruningConfig) -> list[dict[str, float]]:
530	    return summarize_pruning_masks(model, config)
531	
532	
533	def export_meta_from_masks(model: Any, config: PruningConfig) -> dict[str, Any]:
534	    return export_pruning_metadata(model, config)
535	
536	
537	def create_model_and_tokenizer(config: PruningConfig):
538	    return load_model_and_tokenizer(config)
539	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "ec7dd42e-f38f-4573-a4d2-ea68f5fbacb3",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/pipeline.py",
      "content": "from __future__ import annotations\n\nimport csv\nimport json\nimport os\nimport random\nfrom typing import Any\n\nimport torch\nfrom safetensors.torch import save_file as st_save_file\nfrom torch.utils.data import DataLoader\nfrom tqdm import tqdm\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nfrom config import PruningConfig\nfrom data import TokenBlockDataset, load_text_dataset\nfrom evals import evaluate_accuracy, evaluate_perplexity\nfrom gates import (\n    LlamaAttnGate,\n    LlamaMLPGate,\n    QwenAttnGate,\n    QwenMLPGate,\n    attach_pruning_gates,\n    get_transformer_layers,\n)\nfrom rebuild import load_pruned_model\n\n\ndef set_seed(seed: int) -> None:\n    random.seed(seed)\n    torch.manual_seed(seed)\n    if torch.cuda.is_available():\n        torch.cuda.manual_seed_all(seed)\n\n\n@torch.no_grad()\ndef compute_ffn_unit_cost(device: str) -> torch.Tensor:\n    return torch.tensor(1.0, device=device)\n\n\n@torch.no_grad()\ndef compute_attention_group_cost(cfg: Any, device: str) -> torch.Tensor:\n    num_heads = cfg.num_attention_heads\n    num_kv_heads = cfg.num_key_value_heads\n    head_dim = getattr(cfg, \"head_dim\", cfg.hidden_size // max(1, num_heads))\n    group_size = max(1, num_heads // max(1, num_kv_heads))\n    alpha_param = ((2 * group_size + 2) * head_dim) / 3.0\n    return torch.tensor(alpha_param, dtype=torch.float32, device=device)\n\n\n@torch.no_grad()\ndef build_batch_budget_masks(\n    model: Any,\n    f_cost: torch.Tensor,\n    a_cost: torch.Tensor,\n    keep_ratio: float,\n    tau: float,\n):\n    scores, costs, holders = [], [], []\n\n    for layer_idx, block in enumerate(get_transformer_layers(model)):\n        if hasattr(block.mlp, \"gate_score\"):\n            values = torch.sigmoid(block.mlp.gate_score.detach().float() / tau)\n            scores.append(values)\n            costs.append(torch.full_like(values, f_cost))\n            holders.append((\"ffn\", block.mlp, values.numel(), layer_idx))\n        if hasattr(block.self_attn, \"gate_score_kv\"):\n            values = torch.sigmoid(block.self_attn.gate_score_kv.detach().float() / tau)\n            scores.append(values)\n            costs.append(torch.full_like(values, a_cost))\n            holders.append((\"kv\", block.self_attn, values.numel(), layer_idx))\n\n    if not scores:\n        return []\n\n    score_tensor = torch.cat(scores)\n    cost_tensor = torch.cat(costs)\n    budget = max(1.0, cost_tensor.sum().item() * keep_ratio)\n\n    order = torch.argsort(score_tensor, descending=True)\n    cumsum = torch.cumsum(cost_tensor[order], dim=0)\n    chosen = order[cumsum <= budget]\n    if chosen.numel() == 0:\n        chosen = order[:1]\n\n    masks, base = [], 0\n    for kind, module, length, layer_idx in holders:\n        take = torch.zeros(length, dtype=torch.bool, device=score_tensor.device)\n        selected = chosen[(chosen >= base) & (chosen < base + length)] - base\n        if selected.numel() > 0:\n            take[selected.long()] = True\n        masks.append((kind, module, take, layer_idx))\n        base += length\n\n    per_layer: dict[int, dict[str, tuple[Any, torch.Tensor]]] = {}\n    for kind, module, take, layer_idx in masks:\n        per_layer.setdefault(layer_idx, {})[kind] = (module, take)\n\n    for layer_idx, grouped in per_layer.items():\n        if \"ffn\" in grouped:\n            module, take = grouped[\"ffn\"]\n            if take.sum() == 0:\n                score = torch.sigmoid(module.gate_score.detach().float() / tau)\n                take[torch.argmax(score).item()] = True\n        if \"kv\" in grouped:\n            module, take = grouped[\"kv\"]\n            if take.sum() == 0:\n                score = torch.sigmoid(module.gate_score_kv.detach().float() / tau)\n                take[torch.argmax(score).item()] = True\n\n    return [(kind, module, take) for kind, module, take, _ in masks]\n\n\ndef build_train_dataloader(tokenizer: Any, config: PruningConfig) -> DataLoader:\n    raw_dataset = load_text_dataset(config.train_dataset_name, config.train_split)\n    dataset = TokenBlockDataset(raw_dataset, tokenizer, config.max_len)\n    dataset = torch.utils.data.Subset(dataset, list(range(min(config.num_samples, len(dataset)))))\n    return DataLoader(dataset, batch_size=config.batch_size, shuffle=True)\n\n\ndef train_gates(model: Any, tokenizer: Any, config: PruningConfig) -> None:\n    dataloader = build_train_dataloader(tokenizer, config)\n    f_cost = compute_ffn_unit_cost(config.device)\n    a_cost = compute_attention_group_cost(model.config, config.device)\n\n    f_params, a_params = [], []\n    for name, parameter in model.named_parameters():\n        if not parameter.requires_grad:\n            continue\n        if name.endswith(\"mlp.gate_score\"):\n            f_params.append(parameter)\n        elif name.endswith(\"self_attn.gate_score_kv\"):\n            a_params.append(parameter)\n\n    optimizer = torch.optim.AdamW(\n        [{\"params\": f_params, \"lr\": config.lr}, {\"params\": a_params, \"lr\": config.lr}],\n        betas=(0.9, 0.99),\n        eps=1e-8,\n        weight_decay=0.0,\n    )\n\n    model.train()\n    for epoch in range(config.epochs):\n        progress = tqdm(dataloader, desc=f\"Epoch {epoch + 1}\")\n        for batch in progress:\n            batch = {key: value.to(config.device) for key, value in batch.items()}\n            masks = build_batch_budget_masks(model, f_cost, a_cost, config.keep_ratio, config.tau)\n            for kind, module, take in masks:\n                module._batch_mask = take.view(1, 1, -1) if kind == \"ffn\" else take\n\n            output = model(**batch, labels=batch[\"input_ids\"])\n            loss = output.loss\n            optimizer.zero_grad(set_to_none=True)\n            loss.backward()\n            optimizer.step()\n\n            for _, module, _ in masks:\n                if hasattr(module, \"_batch_mask\"):\n                    delattr(module, \"_batch_mask\")\n\n            with torch.no_grad():\n                mean_ffn = []\n                mean_kv = []\n                for block in get_transformer_layers(model):\n                    if hasattr(block.mlp, \"gate_score\"):\n                        mean_ffn.append(torch.sigmoid(block.mlp.gate_score / config.tau).mean().item())\n                    if hasattr(block.self_attn, \"gate_score_kv\"):\n                        mean_kv.append(torch.sigmoid(block.self_attn.gate_score_kv / config.tau).mean().item())\n            progress.set_postfix(\n                loss=f\"{loss.item():.3f}\",\n                p_ffn=f\"{sum(mean_ffn) / max(1, len(mean_ffn)):.3f}\",\n                p_kv=f\"{sum(mean_kv) / max(1, len(mean_kv)):.3f}\",\n            )\n\n\n@torch.no_grad()\ndef apply_final_hard_masks(model: Any, config: PruningConfig) -> None:\n    f_cost = compute_ffn_unit_cost(config.device)\n    a_cost = compute_attention_group_cost(model.config, config.device)\n    masks = build_batch_budget_masks(model, f_cost, a_cost, keep_ratio=config.keep_ratio, tau=config.tau)\n\n    for kind, module, take in masks:\n        if kind == \"ffn\":\n            module.register_hard_mask(take)\n        else:\n            module.register_hard_mask_kv(take)\n\n    for block in get_transformer_layers(model):\n        if hasattr(block.mlp, \"eval_keep_mask\"):\n            take = block.mlp.eval_keep_mask.to(torch.bool)\n            if take.sum() == 0:\n                score = torch.sigmoid(block.mlp.gate_score.detach().float() / config.tau)\n                take[torch.argmax(score).item()] = True\n                block.mlp.register_hard_mask(take)\n        if hasattr(block.self_attn, \"eval_keep_mask_kv\"):\n            take = block.self_attn.eval_keep_mask_kv.to(torch.bool)\n            if take.sum() == 0:\n                score = torch.sigmoid(block.self_attn.gate_score_kv.detach().float() / config.tau)\n                take[torch.argmax(score).item()] = True\n                block.self_attn.register_hard_mask_kv(take)\n\n\n@torch.no_grad()\ndef summarize_pruning_masks(model: Any, config: PruningConfig) -> list[dict[str, float]]:\n    device = next(model.parameters()).device\n    cfg = model.config\n    f_unit = compute_ffn_unit_cost(str(device)).to(device)\n    a_unit = compute_attention_group_cost(cfg, str(device)).to(device)\n    num_heads = cfg.num_attention_heads\n    num_kv_heads = cfg.num_key_value_heads\n    group_size = max(1, num_heads // max(1, num_kv_heads))\n\n    rows = []\n    total_ffn_all = total_ffn_keep = 0\n    total_kv_all = total_kv_keep = 0\n    total_params_kept = 0.0\n\n    for layer_idx, block in enumerate(get_transformer_layers(model)):\n        if hasattr(block.mlp, \"eval_keep_mask\"):\n            f_keep = int(block.mlp.eval_keep_mask.to(torch.bool).sum().item())\n            f_total = int(block.mlp.eval_keep_mask.numel())\n        else:\n            score = getattr(block.mlp, \"gate_score\", None)\n            f_total = int(score.numel()) if score is not None else getattr(block.mlp.up_proj, \"out_features\", 0)\n            f_keep = f_total\n\n        if hasattr(block.self_attn, \"eval_keep_mask_kv\"):\n            a_keep = int(block.self_attn.eval_keep_mask_kv.to(torch.bool).sum().item())\n            a_total = int(block.self_attn.eval_keep_mask_kv.numel())\n        else:\n            score = getattr(block.self_attn, \"gate_score_kv\", None)\n            a_total = int(score.numel()) if score is not None else cfg.num_key_value_heads\n            a_keep = a_total\n\n        total_ffn_all += f_total\n        total_ffn_keep += f_keep\n        total_kv_all += a_total\n        total_kv_keep += a_keep\n        kept_cost = float(f_unit) * f_keep + float(a_unit) * a_keep\n        total_params_kept += kept_cost\n\n        rows.append(\n            {\n                \"layer\": layer_idx,\n                \"ffn_keep\": f_keep,\n                \"ffn_total\": f_total,\n                \"ffn_ratio\": f_keep / max(1, f_total),\n                \"kv_keep\": a_keep,\n                \"kv_total\": a_total,\n                \"kv_ratio\": a_keep / max(1, a_total),\n                \"head_keep_eq\": int(a_keep * group_size),\n                \"head_total\": int(num_heads),\n                \"head_ratio_eq\": a_keep * group_size / max(1, num_heads),\n                \"~params_kept\": int(kept_cost),\n            }\n        )\n\n    total_prunable = float(f_unit) * total_ffn_all + float(a_unit) * total_kv_all\n    target_cost = total_prunable * config.keep_ratio\n    diff = total_params_kept - target_cost\n    pct = (diff / max(1.0, target_cost)) * 100.0\n\n    print(\"\\n[Final HARD Masks Report] (KV-based)\")\n    print(\"-\" * 112)\n    print(\n        f\"{'Layer':>5} | {'FFN keep/total (ratio)':>26} | {'KV keep/total (ratio)':>26} | \"\n        f\"{'Head≈keep/total':>18} | {'~Params kept':>14}\"\n    )\n    print(\"-\" * 112)\n    for row in rows:\n        print(\n            f\"{row['layer']:5d} | {row['ffn_keep']:5d}/{row['ffn_total']:5d} ({row['ffn_ratio'] * 100:6.2f}%) | \"\n            f\"{row['kv_keep']:4d}/{row['kv_total']:4d} ({row['kv_ratio'] * 100:6.2f}%) | \"\n            f\"{row['head_keep_eq']:4d}/{row['head_total']:4d} ({row['head_ratio_eq'] * 100:6.2f}%) | \"\n            f\"{row['~params_kept']:14,d}\"\n        )\n    print(\"-\" * 112)\n    print(\n        f\"TOTAL: FFN {total_ffn_keep}/{total_ffn_all} ({(total_ffn_keep / max(1, total_ffn_all)) * 100:.2f}%) | \"\n        f\"KV {total_kv_keep}/{total_kv_all} ({(total_kv_keep / max(1, total_kv_all)) * 100:.2f}%) | \"\n        f\"~Params kept ≈ {int(total_params_kept):,}\"\n    )\n    print(f\"TARGET keep_ratio={config.keep_ratio:.3f}: ~Params ≈ {int(target_cost):,}\")\n    print(f\"DIFF: {int(diff):,} ({pct:+.3f}%)\\n\")\n\n    if config.report_csv:\n        os.makedirs(os.path.dirname(config.report_csv), exist_ok=True)\n        with open(config.report_csv, \"w\", newline=\"\", encoding=\"utf-8\") as handle:\n            writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))\n            writer.writeheader()\n            writer.writerows(rows)\n        print(f\"[Saved] layer-wise mask report -> {config.report_csv}\")\n\n    return rows\n\n\n@torch.no_grad()\ndef materialize_all_pruning(model: Any) -> None:\n    for block in get_transformer_layers(model):\n        if hasattr(block.mlp, \"materialize_pruning\"):\n            block.mlp.materialize_pruning()\n        if hasattr(block.self_attn, \"materialize_pruning\"):\n            new_attn = block.self_attn.materialize_pruning()\n            if new_attn is not None:\n                block.self_attn = new_attn\n\n\n@torch.no_grad()\ndef export_pruned_state_dict_safetensors(model: Any, path: str) -> None:\n    state_dict = model.state_dict()\n    cpu_state_dict = {key: value.detach().cpu() for key, value in state_dict.items() if torch.is_tensor(value)}\n    os.makedirs(os.path.dirname(path), exist_ok=True)\n    st_save_file(cpu_state_dict, path)\n    print(f\"[Saved] pruned state_dict (safetensors) -> {path}\")\n\n\n@torch.no_grad()\ndef export_pruning_metadata(model: Any, config: PruningConfig) -> dict[str, Any]:\n    cfg = model.config\n    base_head_dim = getattr(cfg, \"head_dim\", None)\n    if not isinstance(base_head_dim, int) or base_head_dim <= 0:\n        base_head_dim = cfg.hidden_size // max(1, getattr(cfg, \"num_attention_heads\", 1))\n\n    num_heads_orig = getattr(cfg, \"num_attention_heads\", None)\n    num_kv_heads_orig = getattr(cfg, \"num_key_value_heads\", None)\n    if not isinstance(num_heads_orig, int) or num_heads_orig <= 0:\n        num_heads_orig = getattr(get_transformer_layers(model)[0].self_attn, \"num_heads\", 1)\n    if not isinstance(num_kv_heads_orig, int) or num_kv_heads_orig <= 0:\n        num_kv_heads_orig = getattr(get_transformer_layers(model)[0].self_attn, \"num_key_value_heads\", 1)\n    group_size = max(1, num_heads_orig // max(1, num_kv_heads_orig))\n\n    export_format = \"materialized\"\n    meta = {\n        \"model_id\": config.model_id,\n        \"model_family\": config.model_family,\n        \"dtype\": str(config.dtype),\n        \"export_format\": export_format,\n        \"rescale_alpha\": float(config.rescale_alpha),\n        \"layers\": [],\n    }\n    for layer_idx, block in enumerate(get_transformer_layers(model)):\n        assert hasattr(block.mlp, \"eval_keep_mask\"), (\n            f\"Layer {layer_idx} mlp missing eval_keep_mask. Run apply_final_hard_masks first.\"\n        )\n        assert hasattr(block.self_attn, \"eval_keep_mask_kv\"), (\n            f\"Layer {layer_idx} attn missing eval_keep_mask_kv. Run apply_final_hard_masks first.\"\n        )\n\n        ffn_keep = int(block.mlp.eval_keep_mask.to(torch.bool).sum().item())\n        kv_mask = block.self_attn.eval_keep_mask_kv.to(torch.bool)\n        num_kv_heads = int(kv_mask.sum().item())\n        num_heads = max(1, min(num_heads_orig, num_kv_heads * group_size))\n        layer_info = {\n            \"ffn_intermediate_size\": max(1, ffn_keep),\n            \"num_heads\": int(num_heads),\n            \"num_key_value_heads\": max(1, int(num_kv_heads)),\n            \"head_dim\": int(base_head_dim),\n        }\n        meta[\"layers\"].append(layer_info)\n\n    os.makedirs(os.path.dirname(config.pruned_meta_path), exist_ok=True)\n    with open(config.pruned_meta_path, \"w\", encoding=\"utf-8\") as handle:\n        json.dump(meta, handle, ensure_ascii=False, indent=2)\n    print(f\"[Saved] meta(from masks) -> {config.pruned_meta_path}\")\n    return meta\n\n\ndef train_rescale(model: Any, tokenizer: Any, config: PruningConfig) -> None:\n    for block in get_transformer_layers(model):\n        if isinstance(block.mlp, (LlamaMLPGate, QwenMLPGate)):\n            block.mlp.rescale_alpha = config.rescale_alpha\n        if isinstance(block.self_attn, (LlamaAttnGate, QwenAttnGate)):\n            block.self_attn.rescale_alpha = config.rescale_alpha\n\n    for parameter in model.parameters():\n        parameter.requires_grad_(False)\n\n    rescale_params = []\n    for block in get_transformer_layers(model):\n        if isinstance(block.mlp, (LlamaMLPGate, QwenMLPGate)) and hasattr(block.mlp, \"eval_keep_mask\"):\n            with torch.no_grad():\n                block.mlp.gate_score.zero_()\n            block.mlp.gate_score.requires_grad_(True)\n            block.mlp._rescale_mode = True\n            rescale_params.append(block.mlp.gate_score)\n        if isinstance(block.self_attn, (LlamaAttnGate, QwenAttnGate)) and hasattr(block.self_attn, \"eval_keep_mask_kv\"):\n            with torch.no_grad():\n                block.self_attn.gate_score_kv.zero_()\n            block.self_attn.gate_score_kv.requires_grad_(True)\n            block.self_attn._rescale_mode = True\n            rescale_params.append(block.self_attn.gate_score_kv)\n\n    if not rescale_params:\n        print(\"[Stage B] No rescale params found, skip.\")\n        return\n\n    optimizer = torch.optim.AdamW(\n        rescale_params,\n        lr=config.rescale_lr,\n        betas=(0.9, 0.99),\n        eps=1e-8,\n        weight_decay=0.0,\n    )\n\n    raw_dataset = load_text_dataset(\"wikitext2\", \"validation\")\n    dataset = TokenBlockDataset(raw_dataset, tokenizer, config.max_len)\n    dataset = torch.utils.data.Subset(\n        dataset,\n        list(range(min(config.rescale_num_samples, len(dataset)))),\n    )\n    dataloader = DataLoader(dataset, batch_size=config.batch_size, shuffle=True)\n\n    model.train()\n    for epoch in range(config.rescale_epochs):\n        progress = tqdm(dataloader, desc=f\"[Stage B] Epoch {epoch + 1}\")\n        for batch in progress:\n            batch = {key: value.to(config.device) for key, value in batch.items()}\n            output = model(**batch, labels=batch[\"input_ids\"])\n            loss = output.loss\n            optimizer.zero_grad(set_to_none=True)\n            loss.backward()\n            optimizer.step()\n            progress.set_postfix(loss=f\"{loss.item():.3f}\")\n\n\ndef load_model_and_tokenizer(config: PruningConfig):\n    tokenizer = AutoTokenizer.from_pretrained(\n        config.model_id,\n        use_fast=False if config.model_family != \"qwen\" else True,\n        local_files_only=config.local_only,\n        trust_remote_code=config.trust_remote_code,\n        token=config.hf_token,\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    model = AutoModelForCausalLM.from_pretrained(\n        config.model_id,\n        torch_dtype=config.dtype,\n        local_files_only=config.local_only,\n        trust_remote_code=config.trust_remote_code,\n        token=config.hf_token,\n    ).to(config.device)\n\n    torch.backends.cuda.matmul.allow_tf32 = True\n    torch.backends.cudnn.allow_tf32 = True\n    return model, tokenizer\n\n\ndef run_pruning_pipeline(config: PruningConfig) -> dict[str, Any]:\n    set_seed(config.seed)\n    model, tokenizer = load_model_and_tokenizer(config)\n\n    attach_pruning_gates(\n        model,\n        gate_init=config.gate_init,\n        tau=config.tau,\n        device=config.device,\n        model_family=config.model_family,\n    )\n    train_gates(model, tokenizer, config)\n    apply_final_hard_masks(model, config)\n    summarize_pruning_masks(model, config)\n    meta = export_pruning_metadata(model, config)\n    train_rescale(model, tokenizer, config)\n\n    materialize_all_pruning(model)\n    export_pruned_state_dict_safetensors(model, config.pruned_state_dict_path)\n\n    metrics: dict[str, Any] = {\"meta\": meta}\n    if config.run_ppl_eval:\n        eval_model, eval_tokenizer, _ = load_pruned_model(\n            model_id=config.model_id,\n            state_dict_path=config.pruned_state_dict_path,\n            meta_path=config.pruned_meta_path,\n            torch_dtype=config.dtype,\n            device=config.device,\n            use_fast_tokenizer=(config.model_family == \"qwen\"),\n            trust_remote_code=config.trust_remote_code,\n            hf_token=config.hf_token,\n            local_only=config.local_only,\n        )\n        metrics[\"ppl\"] = evaluate_perplexity(\n            eval_model,\n            eval_tokenizer,\n            datasets=config.ppl_datasets,\n            device=config.device,\n        )\n    if config.run_acc_eval:\n        if not config.run_ppl_eval:\n            eval_model, eval_tokenizer, _ = load_pruned_model(\n                model_id=config.model_id,\n                state_dict_path=config.pruned_state_dict_path,\n                meta_path=config.pruned_meta_path,\n                torch_dtype=config.dtype,\n                device=config.device,\n                use_fast_tokenizer=(config.model_family == \"qwen\"),\n                trust_remote_code=config.trust_remote_code,\n                hf_token=config.hf_token,\n                local_only=config.local_only,\n            )\n        metrics[\"acc\"] = evaluate_accuracy(eval_model, eval_tokenizer, device=config.device)\n    print(\"[Done] Pruning pipeline finished.\")\n    return metrics\n\n\ndef ffn_unit_cost(device: str) -> torch.Tensor:\n    return compute_ffn_unit_cost(device)\n\n\ndef attn_kv_group_cost(cfg: Any, device: str) -> torch.Tensor:\n    return compute_attention_group_cost(cfg, device)\n\n\ndef build_batch_budget_mask(\n    model: Any,\n    f_cost: torch.Tensor,\n    a_cost: torch.Tensor,\n    keep_ratio: float,\n    tau: float,\n):\n    return build_batch_budget_masks(model, f_cost, a_cost, keep_ratio, tau)\n\n\ndef final_hardening_apply(model: Any, config: PruningConfig) -> None:\n    apply_final_hard_masks(model, config)\n\n\ndef report_masks(model: Any, config: PruningConfig) -> list[dict[str, float]]:\n    return summarize_pruning_masks(model, config)\n\n\ndef export_meta_from_masks(model: Any, config: PruningConfig) -> dict[str, Any]:\n    return export_pruning_metadata(model, config)\n\n\ndef create_model_and_tokenizer(config: PruningConfig):\n    return load_model_and_tokenizer(config)\n",
      "numLines": 539,
      "startLine": 1,
      "totalLines": 539
    }
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-14T08:21:30.993Z_

<details><summary>↩ Tool result · `toolu_013JMbVZqYDNdPLDuJXdGtt6`</summary>

```text
1	from __future__ import annotations
2	
3	import argparse
4	
5	import torch
6	
7	from config import PruningConfig
8	from pipeline import run_pruning_pipeline
9	
10	
11	DTYPE_MAP = {
12	    "float16": torch.float16,
13	    "bfloat16": torch.bfloat16,
14	    "float32": torch.float32,
15	}
16	
17	
18	def build_parser() -> argparse.ArgumentParser:
19	    parser = argparse.ArgumentParser(description="Run GRASPrune gate pruning on a LLaMA-style model.")
20	    parser.add_argument("--model-id", default="meta-llama/Llama-2-7b-hf")
21	    parser.add_argument("--model-family", default="auto", choices=["auto", "llama", "qwen"])
22	    parser.add_argument("--device", default=None)
23	    parser.add_argument("--dtype", choices=sorted(DTYPE_MAP.keys()), default="bfloat16")
24	    parser.add_argument("--keep-ratio", type=float, default=0.6)
25	    parser.add_argument("--epochs", type=int, default=4)
26	    parser.add_argument("--batch-size", type=int, default=1)
27	    parser.add_argument("--num-samples", type=int, default=512)
28	    parser.add_argument("--max-len", type=int, default=512)
29	    parser.add_argument("--lr", type=float, default=1e-2)
30	    parser.add_argument("--tau", type=float, default=1.5)
31	    parser.add_argument("--gate-init", type=float, default=0.0)
32	    parser.add_argument("--train-dataset", default="wikitext2")
33	    parser.add_argument("--train-split", default="train")
34	    parser.add_argument("--output-dir", default=None)
35	    parser.add_argument("--report-csv", default=None)
36	    parser.add_argument("--run-ppl-eval", action="store_true")
37	    parser.add_argument("--skip-acc-eval", action="store_true")
38	    parser.add_argument("--rescale-num-samples", type=int, default=512)
39	    parser.add_argument("--rescale-epochs", type=int, default=1)
40	    parser.add_argument("--rescale-lr", type=float, default=1e-2)
41	    parser.add_argument("--rescale-alpha", type=float, default=0.5)
42	    parser.add_argument("--allow-remote-model", action="store_true")
43	    parser.add_argument("--trust-remote-code", action="store_true")
44	    parser.add_argument("--hf-token", default=None)
45	    return parser
46	
47	
48	def main() -> None:
49	    args = build_parser().parse_args()
50	    config = PruningConfig(
51	        model_id=args.model_id,
52	        model_family=args.model_family,
53	        dtype=DTYPE_MAP[args.dtype],
54	        device=args.device or PruningConfig().device,
55	        local_only=not args.allow_remote_model,
56	        trust_remote_code=args.trust_remote_code,
57	        hf_token=args.hf_token,
58	        max_len=args.max_len,
59	        batch_size=args.batch_size,
60	        epochs=args.epochs,
61	        lr=args.lr,
62	        tau=args.tau,
63	        gate_init=args.gate_init,
64	        keep_ratio=args.keep_ratio,
65	        train_split=args.train_split,
66	        num_samples=args.num_samples,
67	        train_dataset_name=args.train_dataset,
68	        run_ppl_eval=args.run_ppl_eval,
69	        run_acc_eval=not args.skip_acc_eval,
70	        rescale_num_samples=args.rescale_num_samples,
71	        rescale_epochs=args.rescale_epochs,
72	        rescale_lr=args.rescale_lr,
73	        rescale_alpha=args.rescale_alpha,
74	        report_csv=args.report_csv,
75	        output_dir=args.output_dir,
76	    )
77	    run_pruning_pipeline(config)
78	
79	
80	if __name__ == "__main__":
81	    main()
82	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "9f0c9df9-5f64-4179-9626-7cbde4e503cd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/train.py",
      "content": "from __future__ import annotations\n\nimport argparse\n\nimport torch\n\nfrom config import PruningConfig\nfrom pipeline import run_pruning_pipeline\n\n\nDTYPE_MAP = {\n    \"float16\": torch.float16,\n    \"bfloat16\": torch.bfloat16,\n    \"float32\": torch.float32,\n}\n\n\ndef build_parser() -> argparse.ArgumentParser:\n    parser = argparse.ArgumentParser(description=\"Run GRASPrune gate pruning on a LLaMA-style model.\")\n    parser.add_argument(\"--model-id\", default=\"meta-llama/Llama-2-7b-hf\")\n    parser.add_argument(\"--model-family\", default=\"auto\", choices=[\"auto\", \"llama\", \"qwen\"])\n    parser.add_argument(\"--device\", default=None)\n    parser.add_argument(\"--dtype\", choices=sorted(DTYPE_MAP.keys()), default=\"bfloat16\")\n    parser.add_argument(\"--keep-ratio\", type=float, default=0.6)\n    parser.add_argument(\"--epochs\", type=int, default=4)\n    parser.add_argument(\"--batch-size\", type=int, default=1)\n    parser.add_argument(\"--num-samples\", type=int, default=512)\n    parser.add_argument(\"--max-len\", type=int, default=512)\n    parser.add_argument(\"--lr\", type=float, default=1e-2)\n    parser.add_argument(\"--tau\", type=float, default=1.5)\n    parser.add_argument(\"--gate-init\", type=float, default=0.0)\n    parser.add_argument(\"--train-dataset\", default=\"wikitext2\")\n    parser.add_argument(\"--train-split\", default=\"train\")\n    parser.add_argument(\"--output-dir\", default=None)\n    parser.add_argument(\"--report-csv\", default=None)\n    parser.add_argument(\"--run-ppl-eval\", action=\"store_true\")\n    parser.add_argument(\"--skip-acc-eval\", action=\"store_true\")\n    parser.add_argument(\"--rescale-num-samples\", type=int, default=512)\n    parser.add_argument(\"--rescale-epochs\", type=int, default=1)\n    parser.add_argument(\"--rescale-lr\", type=float, default=1e-2)\n    parser.add_argument(\"--rescale-alpha\", type=float, default=0.5)\n    parser.add_argument(\"--allow-remote-model\", action=\"store_true\")\n    parser.add_argument(\"--trust-remote-code\", action=\"store_true\")\n    parser.add_argument(\"--hf-token\", default=None)\n    return parser\n\n\ndef main() -> None:\n    args = build_parser().parse_args()\n    config = PruningConfig(\n        model_id=args.model_id,\n        model_family=args.model_family,\n        dtype=DTYPE_MAP[args.dtype],\n        device=args.device or PruningConfig().device,\n        local_only=not args.allow_remote_model,\n        trust_remote_code=args.trust_remote_code,\n        hf_token=args.hf_token,\n        max_len=args.max_len,\n        batch_size=args.batch_size,\n        epochs=args.epochs,\n        lr=args.lr,\n        tau=args.tau,\n        gate_init=args.gate_init,\n        keep_ratio=args.keep_ratio,\n        train_split=args.train_split,\n        num_samples=args.num_samples,\n        train_dataset_name=args.train_dataset,\n        run_ppl_eval=args.run_ppl_eval,\n        run_acc_eval=not args.skip_acc_eval,\n        rescale_num_samples=args.rescale_num_samples,\n        rescale_epochs=args.rescale_epochs,\n        rescale_lr=args.rescale_lr,\n        rescale_alpha=args.rescale_alpha,\n        report_csv=args.report_csv,\n        output_dir=args.output_dir,\n    )\n    run_pruning_pipeline(config)\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 82,
      "startLine": 1,
      "totalLines": 82
    }
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Read · `toolu_01VQRQCEEUugoqHacj7EBEwz`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/rebuild.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "f4d96f20-309d-4ee0-9e2b-17074db16757",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 40 · 2026-05-14T08:21:31.068Z_

<details><summary>↩ Tool result · `toolu_01VQRQCEEUugoqHacj7EBEwz`</summary>

```text
1	from __future__ import annotations
2	
3	import json
4	from collections import OrderedDict
5	from typing import Any
6	
7	import torch
8	import torch.nn as nn
9	from safetensors.torch import load_file as st_load_file
10	from transformers import AutoModelForCausalLM, AutoTokenizer
11	
12	from gates import get_transformer_layers
13	
14	
15	def restore_dense_ffn(block: nn.Module, intermediate_size: int) -> None:
16	    hidden_size = block.mlp.down_proj.out_features
17	    input_hidden = block.mlp.gate_proj.in_features
18	
19	    new_gate = nn.Linear(input_hidden, intermediate_size, bias=(block.mlp.gate_proj.bias is not None))
20	    new_up = nn.Linear(input_hidden, intermediate_size, bias=(block.mlp.up_proj.bias is not None))
21	    new_down = nn.Linear(intermediate_size, hidden_size, bias=(block.mlp.down_proj.bias is not None))
22	
23	    dtype = block.mlp.gate_proj.weight.dtype
24	    device = block.mlp.gate_proj.weight.device
25	    block.mlp.gate_proj = new_gate.to(device, dtype=dtype)
26	    block.mlp.up_proj = new_up.to(device, dtype=dtype)
27	    block.mlp.down_proj = new_down.to(device, dtype=dtype)
28	
29	    if hasattr(block.mlp, "intermediate_size"):
30	        block.mlp.intermediate_size = int(intermediate_size)
31	
32	
33	def restore_dense_attention_projections(
34	    block: nn.Module,
35	    num_heads: int,
36	    num_kv_heads: int,
37	    head_dim: int,
38	) -> None:
39	    hidden_size = block.self_attn.q_proj.in_features
40	    q_out = int(num_heads) * int(head_dim)
41	    kv_out = int(num_kv_heads) * int(head_dim)
42	    o_out = block.self_attn.o_proj.out_features
43	
44	    dtype = block.self_attn.q_proj.weight.dtype
45	    device = block.self_attn.q_proj.weight.device
46	
47	    block.self_attn.q_proj = nn.Linear(hidden_size, q_out, bias=(block.self_attn.q_proj.bias is not None)).to(
48	        device, dtype=dtype
49	    )
50	    block.self_attn.k_proj = nn.Linear(hidden_size, kv_out, bias=(block.self_attn.k_proj.bias is not None)).to(
51	        device, dtype=dtype
52	    )
53	    block.self_attn.v_proj = nn.Linear(hidden_size, kv_out, bias=(block.self_attn.v_proj.bias is not None)).to(
54	        device, dtype=dtype
55	    )
56	    block.self_attn.o_proj = nn.Linear(q_out, o_out, bias=(block.self_attn.o_proj.bias is not None)).to(
57	        device, dtype=dtype
58	    )
59	
60	    block.self_attn.num_heads = int(num_heads)
61	    block.self_attn.num_key_value_heads = int(num_kv_heads)
62	    block.self_attn.num_key_value_groups = max(
63	        1,
64	        block.self_attn.num_heads // max(1, block.self_attn.num_key_value_heads),
65	    )
66	    block.self_attn.head_dim = int(head_dim)
67	    block.self_attn.hidden_size = int(num_heads * head_dim)
68	
69	
70	def rebuild_from_meta(model: Any, meta: dict[str, Any]) -> None:
71	    layers = get_transformer_layers(model)
72	    assert "layers" in meta, "meta.json must contain key: layers"
73	    assert len(meta["layers"]) == len(layers), f"meta layers={len(meta['layers'])} != model layers={len(layers)}"
74	
75	    for idx, block in enumerate(layers):
76	        info = meta["layers"][idx]
77	        restore_dense_ffn(block, intermediate_size=int(info["ffn_intermediate_size"]))
78	        restore_dense_attention_projections(
79	            block,
80	            num_heads=int(info["num_heads"]),
81	            num_kv_heads=int(info["num_key_value_heads"]),
82	            head_dim=int(info["head_dim"]),
83	        )
84	
85	
86	def load_pruned_model(
87	    model_id: str,
88	    state_dict_path: str,
89	    meta_path: str,
90	    torch_dtype: torch.dtype,
91	    device: str,
92	    *,
93	    use_fast_tokenizer: bool = False,
94	    trust_remote_code: bool = False,
95	    hf_token: str | None = None,
96	    local_only: bool = True,
97	):
98	    model = AutoModelForCausalLM.from_pretrained(
99	        model_id,
100	        torch_dtype=torch_dtype,
101	        local_files_only=local_only,
102	        trust_remote_code=trust_remote_code,
103	        token=hf_token,
104	        low_cpu_mem_usage=True,
105	    ).to(device)
106	    model.eval()
107	
108	    with open(meta_path, "r", encoding="utf-8") as handle:
109	        meta = json.load(handle)
110	    rebuild_from_meta(model, meta)
111	
112	    state_dict = OrderedDict(st_load_file(state_dict_path, device="cpu"))
113	    missing, unexpected = model.load_state_dict(state_dict, strict=False)
114	    if missing:
115	        print("[WARN] missing keys:", len(missing))
116	    if unexpected:
117	        print("[WARN] unexpected keys:", len(unexpected))
118	
119	    tokenizer = AutoTokenizer.from_pretrained(
120	        model_id,
121	        use_fast=use_fast_tokenizer,
122	        local_files_only=local_only,
123	        trust_remote_code=trust_remote_code,
124	        token=hf_token,
125	    )
126	    if tokenizer.pad_token is None:
127	        tokenizer.pad_token = tokenizer.eos_token
128	
129	    return model, tokenizer, meta
130	
131	
132	def replace_ffn_with_plain(block: nn.Module, inter_size: int) -> None:
133	    restore_dense_ffn(block, intermediate_size=inter_size)
134	
135	
136	def replace_attn_proj_with_plain(block: nn.Module, num_heads: int, num_kv_heads: int, head_dim: int) -> None:
137	    restore_dense_attention_projections(
138	        block,
139	        num_heads=num_heads,
140	        num_kv_heads=num_kv_heads,
141	        head_dim=head_dim,
142	    )
143	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "3349cd11-22c1-4405-88a8-57a4f8291f71",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/rebuild.py",
      "content": "from __future__ import annotations\n\nimport json\nfrom collections import OrderedDict\nfrom typing import Any\n\nimport torch\nimport torch.nn as nn\nfrom safetensors.torch import load_file as st_load_file\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nfrom gates import get_transformer_layers\n\n\ndef restore_dense_ffn(block: nn.Module, intermediate_size: int) -> None:\n    hidden_size = block.mlp.down_proj.out_features\n    input_hidden = block.mlp.gate_proj.in_features\n\n    new_gate = nn.Linear(input_hidden, intermediate_size, bias=(block.mlp.gate_proj.bias is not None))\n    new_up = nn.Linear(input_hidden, intermediate_size, bias=(block.mlp.up_proj.bias is not None))\n    new_down = nn.Linear(intermediate_size, hidden_size, bias=(block.mlp.down_proj.bias is not None))\n\n    dtype = block.mlp.gate_proj.weight.dtype\n    device = block.mlp.gate_proj.weight.device\n    block.mlp.gate_proj = new_gate.to(device, dtype=dtype)\n    block.mlp.up_proj = new_up.to(device, dtype=dtype)\n    block.mlp.down_proj = new_down.to(device, dtype=dtype)\n\n    if hasattr(block.mlp, \"intermediate_size\"):\n        block.mlp.intermediate_size = int(intermediate_size)\n\n\ndef restore_dense_attention_projections(\n    block: nn.Module,\n    num_heads: int,\n    num_kv_heads: int,\n    head_dim: int,\n) -> None:\n    hidden_size = block.self_attn.q_proj.in_features\n    q_out = int(num_heads) * int(head_dim)\n    kv_out = int(num_kv_heads) * int(head_dim)\n    o_out = block.self_attn.o_proj.out_features\n\n    dtype = block.self_attn.q_proj.weight.dtype\n    device = block.self_attn.q_proj.weight.device\n\n    block.self_attn.q_proj = nn.Linear(hidden_size, q_out, bias=(block.self_attn.q_proj.bias is not None)).to(\n        device, dtype=dtype\n    )\n    block.self_attn.k_proj = nn.Linear(hidden_size, kv_out, bias=(block.self_attn.k_proj.bias is not None)).to(\n        device, dtype=dtype\n    )\n    block.self_attn.v_proj = nn.Linear(hidden_size, kv_out, bias=(block.self_attn.v_proj.bias is not None)).to(\n        device, dtype=dtype\n    )\n    block.self_attn.o_proj = nn.Linear(q_out, o_out, bias=(block.self_attn.o_proj.bias is not None)).to(\n        device, dtype=dtype\n    )\n\n    block.self_attn.num_heads = int(num_heads)\n    block.self_attn.num_key_value_heads = int(num_kv_heads)\n    block.self_attn.num_key_value_groups = max(\n        1,\n        block.self_attn.num_heads // max(1, block.self_attn.num_key_value_heads),\n    )\n    block.self_attn.head_dim = int(head_dim)\n    block.self_attn.hidden_size = int(num_heads * head_dim)\n\n\ndef rebuild_from_meta(model: Any, meta: dict[str, Any]) -> None:\n    layers = get_transformer_layers(model)\n    assert \"layers\" in meta, \"meta.json must contain key: layers\"\n    assert len(meta[\"layers\"]) == len(layers), f\"meta layers={len(meta['layers'])} != model layers={len(layers)}\"\n\n    for idx, block in enumerate(layers):\n        info = meta[\"layers\"][idx]\n        restore_dense_ffn(block, intermediate_size=int(info[\"ffn_intermediate_size\"]))\n        restore_dense_attention_projections(\n            block,\n            num_heads=int(info[\"num_heads\"]),\n            num_kv_heads=int(info[\"num_key_value_heads\"]),\n            head_dim=int(info[\"head_dim\"]),\n        )\n\n\ndef load_pruned_model(\n    model_id: str,\n    state_dict_path: str,\n    meta_path: str,\n    torch_dtype: torch.dtype,\n    device: str,\n    *,\n    use_fast_tokenizer: bool = False,\n    trust_remote_code: bool = False,\n    hf_token: str | None = None,\n    local_only: bool = True,\n):\n    model = AutoModelForCausalLM.from_pretrained(\n        model_id,\n        torch_dtype=torch_dtype,\n        local_files_only=local_only,\n        trust_remote_code=trust_remote_code,\n        token=hf_token,\n        low_cpu_mem_usage=True,\n    ).to(device)\n    model.eval()\n\n    with open(meta_path, \"r\", encoding=\"utf-8\") as handle:\n        meta = json.load(handle)\n    rebuild_from_meta(model, meta)\n\n    state_dict = OrderedDict(st_load_file(state_dict_path, device=\"cpu\"))\n    missing, unexpected = model.load_state_dict(state_dict, strict=False)\n    if missing:\n        print(\"[WARN] missing keys:\", len(missing))\n    if unexpected:\n        print(\"[WARN] unexpected keys:\", len(unexpected))\n\n    tokenizer = AutoTokenizer.from_pretrained(\n        model_id,\n        use_fast=use_fast_tokenizer,\n        local_files_only=local_only,\n        trust_remote_code=trust_remote_code,\n        token=hf_token,\n    )\n    if tokenizer.pad_token is None:\n        tokenizer.pad_token = tokenizer.eos_token\n\n    return model, tokenizer, meta\n\n\ndef replace_ffn_with_plain(block: nn.Module, inter_size: int) -> None:\n    restore_dense_ffn(block, intermediate_size=inter_size)\n\n\ndef replace_attn_proj_with_plain(block: nn.Module, num_heads: int, num_kv_heads: int, head_dim: int) -> None:\n    restore_dense_attention_projections(\n        block,\n        num_heads=num_heads,\n        num_kv_heads=num_kv_heads,\n        head_dim=head_dim,\n    )\n",
      "numLines": 143,
      "startLine": 1,
      "totalLines": 143
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Read · `toolu_016zxAiF1deZSRstGYBHB3sC`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/config.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "d0d709b6-be4c-4baf-a235-997017d7691f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01KBVg3aq2xkfjexDQAR8U1b`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "1b4267a6-70c4-4345-95e7-278df50fb624",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 43 · 2026-05-14T08:21:31.185Z_

<details><summary>↩ Tool result · `toolu_016zxAiF1deZSRstGYBHB3sC`</summary>

```text
1	from __future__ import annotations
2	
3	from dataclasses import dataclass, field
4	from pathlib import Path
5	from typing import Tuple
6	
7	import torch
8	
9	
10	def default_device() -> str:
11	    return "cuda:0" if torch.cuda.is_available() else "cpu"
12	
13	
14	@dataclass
15	class PruningConfig:
16	    model_id: str = "meta-llama/Llama-2-7b-hf"
17	    model_family: str = "auto"
18	    dtype: torch.dtype = torch.bfloat16
19	    device: str = field(default_factory=default_device)
20	    local_only: bool = True
21	    trust_remote_code: bool = False
22	    hf_token: str | None = None
23	    seed: int = 42
24	
25	    max_len: int = 512
26	    batch_size: int = 1
27	    epochs: int = 4
28	    lr: float = 1e-2
29	    tau: float = 1.5
30	    gate_init: float = 0.0
31	    keep_ratio: float = 0.6
32	    train_split: str = "train"
33	    num_samples: int = 512
34	
35	    train_dataset_name: str = "wikitext2"
36	    ppl_datasets: Tuple[str, ...] = ("wikitext2", "ptb", "c4")
37	    run_ppl_eval: bool = False
38	    run_acc_eval: bool = True
39	
40	    rescale_num_samples: int = 512
41	    rescale_epochs: int = 1
42	    rescale_lr: float = 1e-2
43	    rescale_alpha: float = 0.5
44	
45	    report_csv: str | None = None
46	    output_dir: str | None = None
47	    qwen_eval_in_mask_state: bool = False
48	
49	    def __post_init__(self) -> None:
50	        root_dir = Path(__file__).resolve().parent
51	        if self.output_dir is None:
52	            model_slug = self.model_id.split("/")[-1]
53	            self.output_dir = str(root_dir / "outputs" / f"{model_slug}_pruned_{int(self.keep_ratio * 100)}")
54	        if self.report_csv is None:
55	            self.report_csv = str(Path(self.output_dir) / "layer_mask_report.csv")
56	
57	    @property
58	    def pruned_state_dict_path(self) -> str:
59	        return f"{self.output_dir}/pruned_state_dict.safetensors"
60	
61	    @property
62	    def pruned_meta_path(self) -> str:
63	        return f"{self.output_dir}/meta.json"
64	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "148a1452-6942-4ffe-a30a-228b21c00acb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/config.py",
      "content": "from __future__ import annotations\n\nfrom dataclasses import dataclass, field\nfrom pathlib import Path\nfrom typing import Tuple\n\nimport torch\n\n\ndef default_device() -> str:\n    return \"cuda:0\" if torch.cuda.is_available() else \"cpu\"\n\n\n@dataclass\nclass PruningConfig:\n    model_id: str = \"meta-llama/Llama-2-7b-hf\"\n    model_family: str = \"auto\"\n    dtype: torch.dtype = torch.bfloat16\n    device: str = field(default_factory=default_device)\n    local_only: bool = True\n    trust_remote_code: bool = False\n    hf_token: str | None = None\n    seed: int = 42\n\n    max_len: int = 512\n    batch_size: int = 1\n    epochs: int = 4\n    lr: float = 1e-2\n    tau: float = 1.5\n    gate_init: float = 0.0\n    keep_ratio: float = 0.6\n    train_split: str = \"train\"\n    num_samples: int = 512\n\n    train_dataset_name: str = \"wikitext2\"\n    ppl_datasets: Tuple[str, ...] = (\"wikitext2\", \"ptb\", \"c4\")\n    run_ppl_eval: bool = False\n    run_acc_eval: bool = True\n\n    rescale_num_samples: int = 512\n    rescale_epochs: int = 1\n    rescale_lr: float = 1e-2\n    rescale_alpha: float = 0.5\n\n    report_csv: str | None = None\n    output_dir: str | None = None\n    qwen_eval_in_mask_state: bool = False\n\n    def __post_init__(self) -> None:\n        root_dir = Path(__file__).resolve().parent\n        if self.output_dir is None:\n            model_slug = self.model_id.split(\"/\")[-1]\n            self.output_dir = str(root_dir / \"outputs\" / f\"{model_slug}_pruned_{int(self.keep_ratio * 100)}\")\n        if self.report_csv is None:\n            self.report_csv = str(Path(self.output_dir) / \"layer_mask_report.csv\")\n\n    @property\n    def pruned_state_dict_path(self) -> str:\n        return f\"{self.output_dir}/pruned_state_dict.safetensors\"\n\n    @property\n    def pruned_meta_path(self) -> str:\n        return f\"{self.output_dir}/meta.json\"\n",
      "numLines": 64,
      "startLine": 1,
      "totalLines": 64
    }
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T08:21:31.187Z_

<details><summary>↩ Tool result · `toolu_01KBVg3aq2xkfjexDQAR8U1b`</summary>

```text
1	"""
2	Structured Pruning for Qwen2.5 architecture.
3	
4	Removes attention heads and MLP channel groups based on RASP or standard importance scores.
5	Handles GQA (grouped query attention) correctly: when all query heads sharing a KV head
6	are pruned, the corresponding KV head is also removed.
7	
8	Input:  pretrained model + pruning scores
9	Output: pruned model saved to disk
10	"""
11	
12	import argparse
13	import copy
14	import logging
15	import os
16	import random
17	
18	import numpy as np
19	import torch
20	from transformers import AutoModelForCausalLM, AutoTokenizer
21	
22	logging.basicConfig(
23	    level=logging.INFO,
24	    format="%(asctime)s [%(levelname)s] %(message)s",
25	)
26	logger = logging.getLogger(__name__)
27	
28	
29	def set_seed(seed: int):
30	    random.seed(seed)
31	    np.random.seed(seed)
32	    torch.manual_seed(seed)
33	    torch.cuda.manual_seed_all(seed)
34	
35	
36	def compute_pruning_masks(scores: dict, n_to_prune: int) -> dict:
37	    """Determine which structures to prune globally.
38	
39	    Returns dict[layer_idx -> list of struct indices to KEEP].
40	    """
41	    ranking = []
42	    for layer_idx, layer_scores in scores.items():
43	        for struct_idx in range(layer_scores.shape[0]):
44	            ranking.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
45	    ranking.sort(key=lambda x: x[0])
46	
47	    prune_set = set()
48	    for i in range(min(n_to_prune, len(ranking))):
49	        _, layer_idx, struct_idx = ranking[i]
50	        prune_set.add((layer_idx, struct_idx))
51	
52	    keep_masks = {}
53	    for layer_idx, layer_scores in scores.items():
54	        n_structs = layer_scores.shape[0]
55	        keep = [i for i in range(n_structs) if (layer_idx, i) not in prune_set]
56	        keep_masks[layer_idx] = keep
57	    return keep_masks
58	
59	
60	def prune_attention_heads(model, attn_keep_masks: dict):
61	    """Prune attention heads from the model by slicing weight matrices in-place.
62	
63	    For GQA: KV heads are removed only when ALL query heads mapped to them are pruned.
64	    """
65	    config = model.config
66	    n_heads = config.num_attention_heads
67	    n_kv_heads = config.num_key_value_heads
68	    head_dim = config.hidden_size // n_heads
69	    heads_per_kv = n_heads // n_kv_heads
70	
71	    total_pruned_q = 0
72	    total_pruned_kv = 0
73	
74	    for layer_idx, keep_heads in attn_keep_masks.items():
75	        layer = model.model.layers[layer_idx]
76	        attn = layer.self_attn
77	        n_keep = len(keep_heads)
78	        pruned_q = n_heads - n_keep
79	
80	        # Q indices to keep
81	        q_indices = []
82	        for h in keep_heads:
83	            start = h * head_dim
84	            q_indices.extend(range(start, start + head_dim))
85	        q_indices = torch.tensor(q_indices, dtype=torch.long)
86	
87	        # Determine which KV heads to keep
88	        kv_keep = set()
89	        for h in keep_heads:
90	            kv_keep.add(h // heads_per_kv)
91	        kv_keep = sorted(kv_keep)
92	        n_kv_keep = len(kv_keep)
93	        pruned_kv = n_kv_heads - n_kv_keep
94	
95	        kv_indices = []
96	        for kv in kv_keep:
97	            start = kv * head_dim
98	            kv_indices.extend(range(start, start + head_dim))
99	        kv_indices = torch.tensor(kv_indices, dtype=torch.long)
100	
101	        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep*head_dim, hidden]
102	        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])
103	        if attn.q_proj.bias is not None:
104	            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])
105	
106	        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_kv_keep*head_dim, hidden]
107	        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])
108	        if attn.k_proj.bias is not None:
109	            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])
110	
111	        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])
112	        if attn.v_proj.bias is not None:
113	            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])
114	
115	        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep*head_dim]
116	        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])
117	
118	        # Update config attributes on the layer
119	        attn.num_heads = n_keep
120	        attn.num_key_value_heads = n_kv_keep
121	        attn.head_dim = head_dim
122	
123	        total_pruned_q += pruned_q
124	        total_pruned_kv += pruned_kv
125	
126	        if pruned_q > 0:
127	            logger.info(
128	                f"  Layer {layer_idx}: pruned {pruned_q}/{n_heads} Q heads, "
129	                f"{pruned_kv}/{n_kv_heads} KV heads"
130	            )
131	
132	    logger.info(f"Total attention pruning: {total_pruned_q} Q heads, {total_pruned_kv} KV heads removed")
133	
134	
135	def prune_mlp_channels(model, mlp_keep_masks: dict):
136	    """Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj."""
137	    config = model.config
138	    intermediate_size = config.intermediate_size
139	    n_heads = config.num_attention_heads
140	    n_groups = n_heads
141	    group_size = intermediate_size // n_groups
142	
143	    total_pruned = 0
144	
145	    for layer_idx, keep_groups in mlp_keep_masks.items():
146	        layer = model.model.layers[layer_idx]
147	        mlp = layer.mlp
148	        n_keep = len(keep_groups)
149	        pruned = n_groups - n_keep
150	
151	        if pruned == 0:
152	            continue
153	
154	        # Channel indices to keep
155	        indices = []
156	        for g in keep_groups:
157	            start = g * group_size
158	            indices.extend(range(start, start + group_size))
159	        # Also keep any remainder channels beyond n_groups*group_size
160	        remainder_start = n_groups * group_size
161	        if remainder_start < intermediate_size:
162	            indices.extend(range(remainder_start, intermediate_size))
163	        indices = torch.tensor(indices, dtype=torch.long)
164	
165	        # gate_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
166	        mlp.gate_proj.weight = torch.nn.Parameter(mlp.gate_proj.weight.data[indices])
167	        if mlp.gate_proj.bias is not None:
168	            mlp.gate_proj.bias = torch.nn.Parameter(mlp.gate_proj.bias.data[indices])
169	
170	        # up_proj: [intermediate, hidden] -> [n_keep_channels, hidden]
171	        mlp.up_proj.weight = torch.nn.Parameter(mlp.up_proj.weight.data[indices])
172	        if mlp.up_proj.bias is not None:
173	            mlp.up_proj.bias = torch.nn.Parameter(mlp.up_proj.bias.data[indices])
174	
175	        # down_proj: [hidden, intermediate] -> [hidden, n_keep_channels]
176	        mlp.down_proj.weight = torch.nn.Parameter(mlp.down_proj.weight.data[:, indices])
177	
178	        total_pruned += pruned
179	        logger.info(
180	            f"  Layer {layer_idx}: pruned {pruned}/{n_groups} MLP groups "
181	            f"({pruned * group_size} channels)"
182	        )
183	
184	    logger.info(f"Total MLP pruning: {total_pruned} groups removed")
185	
186	
187	def count_parameters(model) -> int:
188	    return sum(p.numel() for p in model.parameters())
189	
190	
191	def main():
192	    parser = argparse.ArgumentParser(description="Execute structured pruning on Qwen2.5 model")
193	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
194	    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
195	    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt")
196	    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], required=True)
197	    parser.add_argument("--sparsity", type=float, default=0.35, help="Target sparsity ratio")
198	    parser.add_argument("--alpha", type=float, default=1.0, help="RASP alpha parameter")
199	    parser.add_argument("--output_path", type=str, required=True, help="Output path for pruned model")
200	    parser.add_argument("--seed", type=int, default=42)
201	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
202	    args = parser.parse_args()
203	
204	    set_seed(args.seed)
205	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
206	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
207	    torch_dtype = dtype_map[args.dtype]
208	
209	    logger.info(f"Loading model from {args.model_path}")
210	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
211	    model = AutoModelForCausalLM.from_pretrained(
212	        args.model_path,
213	        torch_dtype=torch_dtype,
214	        device_map="cpu",  # load on CPU for manipulation
215	        trust_remote_code=True,
216	    )
217	
218	    original_params = count_parameters(model)
219	    logger.info(f"Original model parameters: {original_params:,}")
220	
221	    # Load scores
222	    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
223	    attn_importance = importance_data["attn_importance"]
224	    mlp_importance = importance_data["mlp_importance"]
225	
226	    if args.mode == "rasp":
227	        if args.cka_path is None:
228	            raise ValueError("--cka_path required for rasp mode")
229	        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
230	        attn_overlap = cka_data["attn_overlap"]
231	        mlp_overlap = cka_data["mlp_overlap"]
232	        # S(h) = I(h) * (1 - F(h))^alpha
233	        attn_scores = {}
234	        for k in attn_importance:
235	            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)
236	        mlp_scores = {}
237	        for k in mlp_importance:
238	            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)
239	        logger.info(f"Using RASP scoring with alpha={args.alpha}")
240	    else:
241	        attn_scores = {k: v.float() for k, v in attn_importance.items()}
242	        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
243	        logger.info("Using standard importance-only scoring")
244	
245	    # Compute how many structures to prune for target sparsity
246	    # Approximate: distribute sparsity proportionally between attn and MLP
247	    config = model.config
248	    n_layers = config.num_hidden_layers
249	    n_heads = config.num_attention_heads
250	    head_dim = config.hidden_size // n_heads
251	    intermediate_size = config.intermediate_size
252	    n_groups = n_heads
253	    group_size = intermediate_size // n_groups
254	
255	    total_attn_heads = n_layers * n_heads
256	    total_mlp_groups = n_layers * n_groups
257	
258	    # Estimate parameter counts
259	    # Per attention head: q_proj + share of k/v_proj + o_proj
260	    hidden = config.hidden_size
261	    attn_params_per_head = head_dim * hidden * 2  # q + o contribution
262	    mlp_params_per_group = group_size * hidden * 3  # gate + up + down contribution
263	
264	    total_prunable = total_attn_heads * attn_params_per_head + total_mlp_groups * mlp_params_per_group
265	    target_prune_params = original_params * args.sparsity
266	
267	    # Use a unified ranking approach: merge attn and MLP scores
268	    all_entries = []
269	    for layer_idx in range(n_layers):
270	        for h in range(n_heads):
271	            score = attn_scores[layer_idx][h].item()
272	            params = attn_params_per_head
273	            all_entries.append((score, "attn", layer_idx, h, params))
274	        for g in range(n_groups):
275	            score = mlp_scores[layer_idx][g].item()
276	            params = mlp_params_per_group
277	            all_entries.append((score, "mlp", layer_idx, g, params))
278	
279	    all_entries.sort(key=lambda x: x[0])
280	
281	    # Greedily select structures to prune until reaching target sparsity
282	    pruned_params = 0
283	    attn_prune_set = set()
284	    mlp_prune_set = set()
285	
286	    # Keep at least 4 heads per layer and 4 MLP groups per layer
287	    min_keep_per_layer = 4
288	    attn_prune_count = {i: 0 for i in range(n_layers)}
289	    mlp_prune_count = {i: 0 for i in range(n_layers)}
290	
291	    for score, stype, layer_idx, struct_idx, params in all_entries:
292	        if pruned_params >= target_prune_params:
293	            break
294	        if stype == "attn":
295	            if attn_prune_count[layer_idx] >= n_heads - min_keep_per_layer:
296	                continue
297	            attn_prune_set.add((layer_idx, struct_idx))
298	            attn_prune_count[layer_idx] += 1
299	        else:
300	            if mlp_prune_count[layer_idx] >= n_groups - min_keep_per_layer:
301	                continue
302	            mlp_prune_set.add((layer_idx, struct_idx))
303	            mlp_prune_count[layer_idx] += 1
304	        pruned_params += params
305	
306	    logger.info(f"Target sparsity: {args.sparsity:.0%}, pruning {len(attn_prune_set)} attn heads + "
307	                f"{len(mlp_prune_set)} MLP groups ({pruned_params:,} params)")
308	
309	    # Build keep masks
310	    attn_keep_masks = {}
311	    for layer_idx in range(n_layers):
312	        keep = [h for h in range(n_heads) if (layer_idx, h) not in attn_prune_set]
313	        attn_keep_masks[layer_idx] = keep
314	
315	    mlp_keep_masks = {}
316	    for layer_idx in range(n_layers):
317	        keep = [g for g in range(n_groups) if (layer_idx, g) not in mlp_prune_set]
318	        mlp_keep_masks[layer_idx] = keep
319	
320	    # Execute pruning
321	    logger.info("Pruning attention heads...")
322	    prune_attention_heads(model, attn_keep_masks)
323	
324	    logger.info("Pruning MLP channels...")
325	    prune_mlp_channels(model, mlp_keep_masks)
326	
327	    pruned_params_actual = count_parameters(model)
328	    actual_sparsity = 1.0 - pruned_params_actual / original_params
329	    logger.info(
330	        f"Pruned model parameters: {pruned_params_actual:,} "
331	        f"(actual sparsity: {actual_sparsity:.2%})"
332	    )
333	
334	    # Save
335	    logger.info(f"Saving pruned model to {args.output_path}")
336	    os.makedirs(args.output_path, exist_ok=True)
337	    model.save_pretrained(args.output_path)
338	    tokenizer.save_pretrained(args.output_path)
339	
340	    # Save pruning metadata
341	    metadata = {
342	        "mode": args.mode,
343	        "sparsity_target": args.sparsity,
344	        "sparsity_actual": actual_sparsity,
345	        "alpha": args.alpha if args.mode == "rasp" else None,
346	        "original_params": original_params,
347	        "pruned_params": pruned_params_actual,
348	        "attn_keep_masks": attn_keep_masks,
349	        "mlp_keep_masks": mlp_keep_masks,
350	    }
351	    torch.save(metadata, os.path.join(args.output_path, "pruning_metadata.pt"))
352	    logger.info("Done.")
353	
354	
355	if __name__ == "__main__":
356	    main()
357	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "091f03e4-494d-41f8-8bad-54bb6b8c1e64",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/prune.py",
      "content": "\"\"\"\nStructured Pruning for Qwen2.5 architecture.\n\nRemoves attention heads and MLP channel groups based on RASP or standard importance scores.\nHandles GQA (grouped query attention) correctly: when all query heads sharing a KV head\nare pruned, the corresponding KV head is also removed.\n\nInput:  pretrained model + pruning scores\nOutput: pruned model saved to disk\n\"\"\"\n\nimport argparse\nimport copy\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport torch\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef compute_pruning_masks(scores: dict, n_to_prune: int) -> dict:\n    \"\"\"Determine which structures to prune globally.\n\n    Returns dict[layer_idx -> list of struct indices to KEEP].\n    \"\"\"\n    ranking = []\n    for layer_idx, layer_scores in scores.items():\n        for struct_idx in range(layer_scores.shape[0]):\n            ranking.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))\n    ranking.sort(key=lambda x: x[0])\n\n    prune_set = set()\n    for i in range(min(n_to_prune, len(ranking))):\n        _, layer_idx, struct_idx = ranking[i]\n        prune_set.add((layer_idx, struct_idx))\n\n    keep_masks = {}\n    for layer_idx, layer_scores in scores.items():\n        n_structs = layer_scores.shape[0]\n        keep = [i for i in range(n_structs) if (layer_idx, i) not in prune_set]\n        keep_masks[layer_idx] = keep\n    return keep_masks\n\n\ndef prune_attention_heads(model, attn_keep_masks: dict):\n    \"\"\"Prune attention heads from the model by slicing weight matrices in-place.\n\n    For GQA: KV heads are removed only when ALL query heads mapped to them are pruned.\n    \"\"\"\n    config = model.config\n    n_heads = config.num_attention_heads\n    n_kv_heads = config.num_key_value_heads\n    head_dim = config.hidden_size // n_heads\n    heads_per_kv = n_heads // n_kv_heads\n\n    total_pruned_q = 0\n    total_pruned_kv = 0\n\n    for layer_idx, keep_heads in attn_keep_masks.items():\n        layer = model.model.layers[layer_idx]\n        attn = layer.self_attn\n        n_keep = len(keep_heads)\n        pruned_q = n_heads - n_keep\n\n        # Q indices to keep\n        q_indices = []\n        for h in keep_heads:\n            start = h * head_dim\n            q_indices.extend(range(start, start + head_dim))\n        q_indices = torch.tensor(q_indices, dtype=torch.long)\n\n        # Determine which KV heads to keep\n        kv_keep = set()\n        for h in keep_heads:\n            kv_keep.add(h // heads_per_kv)\n        kv_keep = sorted(kv_keep)\n        n_kv_keep = len(kv_keep)\n        pruned_kv = n_kv_heads - n_kv_keep\n\n        kv_indices = []\n        for kv in kv_keep:\n            start = kv * head_dim\n            kv_indices.extend(range(start, start + head_dim))\n        kv_indices = torch.tensor(kv_indices, dtype=torch.long)\n\n        # Slice q_proj: [n_heads*head_dim, hidden] -> [n_keep*head_dim, hidden]\n        attn.q_proj.weight = torch.nn.Parameter(attn.q_proj.weight.data[q_indices])\n        if attn.q_proj.bias is not None:\n            attn.q_proj.bias = torch.nn.Parameter(attn.q_proj.bias.data[q_indices])\n\n        # Slice k_proj, v_proj: [n_kv*head_dim, hidden] -> [n_kv_keep*head_dim, hidden]\n        attn.k_proj.weight = torch.nn.Parameter(attn.k_proj.weight.data[kv_indices])\n        if attn.k_proj.bias is not None:\n            attn.k_proj.bias = torch.nn.Parameter(attn.k_proj.bias.data[kv_indices])\n\n        attn.v_proj.weight = torch.nn.Parameter(attn.v_proj.weight.data[kv_indices])\n        if attn.v_proj.bias is not None:\n            attn.v_proj.bias = torch.nn.Parameter(attn.v_proj.bias.data[kv_indices])\n\n        # Slice o_proj: [hidden, n_heads*head_dim] -> [hidden, n_keep*head_dim]\n        attn.o_proj.weight = torch.nn.Parameter(attn.o_proj.weight.data[:, q_indices])\n\n        # Update config attributes on the layer\n        attn.num_heads = n_keep\n        attn.num_key_value_heads = n_kv_keep\n        attn.head_dim = head_dim\n\n        total_pruned_q += pruned_q\n        total_pruned_kv += pruned_kv\n\n        if pruned_q > 0:\n            logger.info(\n                f\"  Layer {layer_idx}: pruned {pruned_q}/{n_heads} Q heads, \"\n                f\"{pruned_kv}/{n_kv_heads} KV heads\"\n            )\n\n    logger.info(f\"Total attention pruning: {total_pruned_q} Q heads, {total_pruned_kv} KV heads removed\")\n\n\ndef prune_mlp_channels(model, mlp_keep_masks: dict):\n    \"\"\"Prune MLP channel groups by slicing gate_proj, up_proj, and down_proj.\"\"\"\n    config = model.config\n    intermediate_size = config.intermediate_size\n    n_heads = config.num_attention_heads\n    n_groups = n_heads\n    group_size = intermediate_size // n_groups\n\n    total_pruned = 0\n\n    for layer_idx, keep_groups in mlp_keep_masks.items():\n        layer = model.model.layers[layer_idx]\n        mlp = layer.mlp\n        n_keep = len(keep_groups)\n        pruned = n_groups - n_keep\n\n        if pruned == 0:\n            continue\n\n        # Channel indices to keep\n        indices = []\n        for g in keep_groups:\n            start = g * group_size\n            indices.extend(range(start, start + group_size))\n        # Also keep any remainder channels beyond n_groups*group_size\n        remainder_start = n_groups * group_size\n        if remainder_start < intermediate_size:\n            indices.extend(range(remainder_start, intermediate_size))\n        indices = torch.tensor(indices, dtype=torch.long)\n\n        # gate_proj: [intermediate, hidden] -> [n_keep_channels, hidden]\n        mlp.gate_proj.weight = torch.nn.Parameter(mlp.gate_proj.weight.data[indices])\n        if mlp.gate_proj.bias is not None:\n            mlp.gate_proj.bias = torch.nn.Parameter(mlp.gate_proj.bias.data[indices])\n\n        # up_proj: [intermediate, hidden] -> [n_keep_channels, hidden]\n        mlp.up_proj.weight = torch.nn.Parameter(mlp.up_proj.weight.data[indices])\n        if mlp.up_proj.bias is not None:\n            mlp.up_proj.bias = torch.nn.Parameter(mlp.up_proj.bias.data[indices])\n\n        # down_proj: [hidden, intermediate] -> [hidden, n_keep_channels]\n        mlp.down_proj.weight = torch.nn.Parameter(mlp.down_proj.weight.data[:, indices])\n\n        total_pruned += pruned\n        logger.info(\n            f\"  Layer {layer_idx}: pruned {pruned}/{n_groups} MLP groups \"\n            f\"({pruned * group_size} channels)\"\n        )\n\n    logger.info(f\"Total MLP pruning: {total_pruned} groups removed\")\n\n\ndef count_parameters(model) -> int:\n    return sum(p.numel() for p in model.parameters())\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Execute structured pruning on Qwen2.5 model\")\n    parser.add_argument(\"--model_path\", type=str, required=True, help=\"Path to pretrained model\")\n    parser.add_argument(\"--importance_path\", type=str, required=True, help=\"Path to importance scores .pt\")\n    parser.add_argument(\"--cka_path\", type=str, default=None, help=\"Path to CKA overlap scores .pt\")\n    parser.add_argument(\"--mode\", type=str, choices=[\"standard\", \"rasp\"], required=True)\n    parser.add_argument(\"--sparsity\", type=float, default=0.35, help=\"Target sparsity ratio\")\n    parser.add_argument(\"--alpha\", type=float, default=1.0, help=\"RASP alpha parameter\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output path for pruned model\")\n    parser.add_argument(\"--seed\", type=int, default=42)\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\", choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    dtype_map = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16, \"float32\": torch.float32}\n    torch_dtype = dtype_map[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch_dtype,\n        device_map=\"cpu\",  # load on CPU for manipulation\n        trust_remote_code=True,\n    )\n\n    original_params = count_parameters(model)\n    logger.info(f\"Original model parameters: {original_params:,}\")\n\n    # Load scores\n    importance_data = torch.load(args.importance_path, map_location=\"cpu\", weights_only=True)\n    attn_importance = importance_data[\"attn_importance\"]\n    mlp_importance = importance_data[\"mlp_importance\"]\n\n    if args.mode == \"rasp\":\n        if args.cka_path is None:\n            raise ValueError(\"--cka_path required for rasp mode\")\n        cka_data = torch.load(args.cka_path, map_location=\"cpu\", weights_only=True)\n        attn_overlap = cka_data[\"attn_overlap\"]\n        mlp_overlap = cka_data[\"mlp_overlap\"]\n        # S(h) = I(h) * (1 - F(h))^alpha\n        attn_scores = {}\n        for k in attn_importance:\n            attn_scores[k] = attn_importance[k].float() * (1.0 - attn_overlap[k].float()).pow(args.alpha)\n        mlp_scores = {}\n        for k in mlp_importance:\n            mlp_scores[k] = mlp_importance[k].float() * (1.0 - mlp_overlap[k].float()).pow(args.alpha)\n        logger.info(f\"Using RASP scoring with alpha={args.alpha}\")\n    else:\n        attn_scores = {k: v.float() for k, v in attn_importance.items()}\n        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}\n        logger.info(\"Using standard importance-only scoring\")\n\n    # Compute how many structures to prune for target sparsity\n    # Approximate: distribute sparsity proportionally between attn and MLP\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    head_dim = config.hidden_size // n_heads\n    intermediate_size = config.intermediate_size\n    n_groups = n_heads\n    group_size = intermediate_size // n_groups\n\n    total_attn_heads = n_layers * n_heads\n    total_mlp_groups = n_layers * n_groups\n\n    # Estimate parameter counts\n    # Per attention head: q_proj + share of k/v_proj + o_proj\n    hidden = config.hidden_size\n    attn_params_per_head = head_dim * hidden * 2  # q + o contribution\n    mlp_params_per_group = group_size * hidden * 3  # gate + up + down contribution\n\n    total_prunable = total_attn_heads * attn_params_per_head + total_mlp_groups * mlp_params_per_group\n    target_prune_params = original_params * args.sparsity\n\n    # Use a unified ranking approach: merge attn and MLP scores\n    all_entries = []\n    for layer_idx in range(n_layers):\n        for h in range(n_heads):\n            score = attn_scores[layer_idx][h].item()\n            params = attn_params_per_head\n            all_entries.append((score, \"attn\", layer_idx, h, params))\n        for g in range(n_groups):\n            score = mlp_scores[layer_idx][g].item()\n            params = mlp_params_per_group\n            all_entries.append((score, \"mlp\", layer_idx, g, params))\n\n    all_entries.sort(key=lambda x: x[0])\n\n    # Greedily select structures to prune until reaching target sparsity\n    pruned_params = 0\n    attn_prune_set = set()\n    mlp_prune_set = set()\n\n    # Keep at least 4 heads per layer and 4 MLP groups per layer\n    min_keep_per_layer = 4\n    attn_prune_count = {i: 0 for i in range(n_layers)}\n    mlp_prune_count = {i: 0 for i in range(n_layers)}\n\n    for score, stype, layer_idx, struct_idx, params in all_entries:\n        if pruned_params >= target_prune_params:\n            break\n        if stype == \"attn\":\n            if attn_prune_count[layer_idx] >= n_heads - min_keep_per_layer:\n                continue\n            attn_prune_set.add((layer_idx, struct_idx))\n            attn_prune_count[layer_idx] += 1\n        else:\n            if mlp_prune_count[layer_idx] >= n_groups - min_keep_per_layer:\n                continue\n            mlp_prune_set.add((layer_idx, struct_idx))\n            mlp_prune_count[layer_idx] += 1\n        pruned_params += params\n\n    logger.info(f\"Target sparsity: {args.sparsity:.0%}, pruning {len(attn_prune_set)} attn heads + \"\n                f\"{len(mlp_prune_set)} MLP groups ({pruned_params:,} params)\")\n\n    # Build keep masks\n    attn_keep_masks = {}\n    for layer_idx in range(n_layers):\n        keep = [h for h in range(n_heads) if (layer_idx, h) not in attn_prune_set]\n        attn_keep_masks[layer_idx] = keep\n\n    mlp_keep_masks = {}\n    for layer_idx in range(n_layers):\n        keep = [g for g in range(n_groups) if (layer_idx, g) not in mlp_prune_set]\n        mlp_keep_masks[layer_idx] = keep\n\n    # Execute pruning\n    logger.info(\"Pruning attention heads...\")\n    prune_attention_heads(model, attn_keep_masks)\n\n    logger.info(\"Pruning MLP channels...\")\n    prune_mlp_channels(model, mlp_keep_masks)\n\n    pruned_params_actual = count_parameters(model)\n    actual_sparsity = 1.0 - pruned_params_actual / original_params\n    logger.info(\n        f\"Pruned model parameters: {pruned_params_actual:,} \"\n        f\"(actual sparsity: {actual_sparsity:.2%})\"\n    )\n\n    # Save\n    logger.info(f\"Saving pruned model to {args.output_path}\")\n    os.makedirs(args.output_path, exist_ok=True)\n    model.save_pretrained(args.output_path)\n    tokenizer.save_pretrained(args.output_path)\n\n    # Save pruning metadata\n    metadata = {\n        \"mode\": args.mode,\n        \"sparsity_target\": args.sparsity,\n        \"sparsity_actual\": actual_sparsity,\n        \"alpha\": args.alpha if args.mode == \"rasp\" else None,\n        \"original_params\": original_params,\n        \"pruned_params\": pruned_params_actual,\n        \"attn_keep_masks\": attn_keep_masks,\n        \"mlp_keep_masks\": mlp_keep_masks,\n    }\n    torch.save(metadata, os.path.join(args.output_path, \"pruning_metadata.pt\"))\n    logger.info(\"Done.\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 357,
      "startLine": 1,
      "totalLines": 357
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Read · `toolu_01JXUULps1G3Y9UWzvCjiwiu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "c3194e15-eb49-40ca-a9cc-53143f1c6127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Et9nfjbmjngwo17zs8UuY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1220,
      "cache_read_input_tokens": 29899,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1220
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

_source line 46 · 2026-05-14T08:21:31.252Z_

<details><summary>↩ Tool result · `toolu_01JXUULps1G3Y9UWzvCjiwiu`</summary>

```text
1	"""
2	Gradient-based Importance Scoring for structured pruning.
3	
4	Computes Taylor-expansion importance I(h) = ||w_h * grad_h||_2 for each
5	attention head and MLP channel group on calibration data.
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure I(h) scores saved as dict in .pt file
9	        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_importance'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import os
16	import random
17	
18	import numpy as np
19	import torch
20	from datasets import load_dataset
21	from transformers import AutoModelForCausalLM, AutoTokenizer
22	
23	logging.basicConfig(
24	    level=logging.INFO,
25	    format="%(asctime)s [%(levelname)s] %(message)s",
26	)
27	logger = logging.getLogger(__name__)
28	
29	
30	def set_seed(seed: int):
31	    random.seed(seed)
32	    np.random.seed(seed)
33	    torch.manual_seed(seed)
34	    torch.cuda.manual_seed_all(seed)
35	
36	
37	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
38	    """Load GSM8K train questions as calibration prompts with labels for loss computation."""
39	    ds = load_dataset("openai/gsm8k", "main", split="train")
40	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
41	
42	    encodings = []
43	    for example in ds:
44	        text = f"Question: {example['question']}\nAnswer: {example['answer']}"
45	        ids = tokenizer(text, return_tensors="pt", truncation=True, max_length=max_length)
46	        encodings.append(ids)
47	    return encodings
48	
49	
50	def compute_importance(model, calibration_data, device):
51	    """Compute gradient-based importance for attention heads and MLP groups.
52	
53	    Uses Taylor expansion: I(h) = ||w_h * grad_h||_2
54	    Accumulates over calibration batches.
55	    """
56	    config = model.config
57	    n_layers = config.num_hidden_layers
58	    n_heads = config.num_attention_heads
59	    head_dim = config.hidden_size // n_heads
60	    intermediate_size = config.intermediate_size
61	    n_groups = n_heads  # match attention head count for MLP groups
62	    group_size = intermediate_size // n_groups
63	
64	    attn_importance = {i: torch.zeros(n_heads, device="cpu") for i in range(n_layers)}
65	    mlp_importance = {i: torch.zeros(n_groups, device="cpu") for i in range(n_layers)}
66	
67	    model.train()
68	
69	    for batch_idx, enc in enumerate(calibration_data):
70	        input_ids = enc["input_ids"].to(device)
71	        attention_mask = enc["attention_mask"].to(device)
72	        labels = input_ids.clone()
73	
74	        model.zero_grad()
75	        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)
76	        loss = outputs.loss
77	        loss.backward()
78	
79	        with torch.no_grad():
80	            for layer_idx in range(n_layers):
81	                layer = model.model.layers[layer_idx]
82	
83	                # Attention head importance via q_proj weights
84	                q_weight = layer.self_attn.q_proj.weight  # [n_heads*head_dim, hidden]
85	                q_grad = layer.self_attn.q_proj.weight.grad
86	                if q_grad is not None:
87	                    # Reshape to [n_heads, head_dim, hidden]
88	                    w = q_weight.view(n_heads, head_dim, -1)
89	                    g = q_grad.view(n_heads, head_dim, -1)
90	                    taylor = (w * g).float()  # [n_heads, head_dim, hidden]
91	                    # L2 norm per head
92	                    head_scores = taylor.view(n_heads, -1).norm(dim=1)  # [n_heads]
93	                    attn_importance[layer_idx] += head_scores.cpu()
94	
95	                # Also incorporate k_proj and v_proj for attention importance
96	                for proj_name in ["k_proj", "v_proj", "o_proj"]:
97	                    proj = getattr(layer.self_attn, proj_name)
98	                    w = proj.weight
99	                    g = proj.weight.grad
100	                    if g is None:
101	                        continue
102	                    if proj_name == "o_proj":
103	                        # o_proj: [hidden, n_heads*head_dim] — split on dim=1
104	                        w_r = w.view(-1, n_heads, head_dim)
105	                        g_r = g.view(-1, n_heads, head_dim)
106	                        taylor = (w_r * g_r).float()
107	                        head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)
108	                    elif proj_name == "k_proj":
109	                        # GQA: k_proj has n_kv_heads, broadcast to n_heads
110	                        n_kv = config.num_key_value_heads
111	                        kv_head_dim = config.hidden_size // n_heads
112	                        w_r = w.view(n_kv, kv_head_dim, -1)
113	                        g_r = g.view(n_kv, kv_head_dim, -1)
114	                        taylor = (w_r * g_r).float()
115	                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
116	                        # Broadcast KV heads to query heads
117	                        heads_per_kv = n_heads // n_kv
118	                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
119	                    elif proj_name == "v_proj":
120	                        n_kv = config.num_key_value_heads
121	                        kv_head_dim = config.hidden_size // n_heads
122	                        w_r = w.view(n_kv, kv_head_dim, -1)
123	                        g_r = g.view(n_kv, kv_head_dim, -1)
124	                        taylor = (w_r * g_r).float()
125	                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)
126	                        heads_per_kv = n_heads // n_kv
127	                        head_scores = kv_scores.repeat_interleave(heads_per_kv)
128	                    attn_importance[layer_idx] += head_scores.cpu()
129	
130	                # MLP importance via gate_proj
131	                gate_w = layer.mlp.gate_proj.weight  # [intermediate, hidden]
132	                gate_g = layer.mlp.gate_proj.weight.grad
133	                if gate_g is not None:
134	                    usable = n_groups * group_size
135	                    w_r = gate_w[:usable].view(n_groups, group_size, -1)
136	                    g_r = gate_g[:usable].view(n_groups, group_size, -1)
137	                    taylor = (w_r * g_r).float()
138	                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
139	                    mlp_importance[layer_idx] += group_scores.cpu()
140	
141	                # Also use up_proj for MLP importance
142	                up_w = layer.mlp.up_proj.weight
143	                up_g = layer.mlp.up_proj.weight.grad
144	                if up_g is not None:
145	                    usable = n_groups * group_size
146	                    w_r = up_w[:usable].view(n_groups, group_size, -1)
147	                    g_r = up_g[:usable].view(n_groups, group_size, -1)
148	                    taylor = (w_r * g_r).float()
149	                    group_scores = taylor.view(n_groups, -1).norm(dim=1)
150	                    mlp_importance[layer_idx] += group_scores.cpu()
151	
152	        if (batch_idx + 1) % 50 == 0:
153	            logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
154	
155	    # Average over samples
156	    n = len(calibration_data)
157	    for layer_idx in range(n_layers):
158	        attn_importance[layer_idx] /= n
159	        mlp_importance[layer_idx] /= n
160	
161	    return attn_importance, mlp_importance
162	
163	
164	def main():
165	    parser = argparse.ArgumentParser(description="Compute gradient-based importance scores for RASP")
166	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
167	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for importance scores")
168	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
169	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
170	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
171	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
172	    args = parser.parse_args()
173	
174	    set_seed(args.seed)
175	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
176	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
177	    torch_dtype = dtype_map[args.dtype]
178	
179	    logger.info(f"Loading model from {args.model_path}")
180	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
181	    model = AutoModelForCausalLM.from_pretrained(
182	        args.model_path,
183	        torch_dtype=torch_dtype,
184	        device_map=device,
185	        trust_remote_code=True,
186	    )
187	
188	    logger.info(f"Loading {args.n_samples} calibration samples")
189	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
190	
191	    logger.info("Computing gradient-based importance scores...")
192	    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)
193	
194	    for layer_idx in range(model.config.num_hidden_layers):
195	        a = attn_importance[layer_idx]
196	        m = mlp_importance[layer_idx]
197	        logger.info(
198	            f"  Layer {layer_idx}: attn I(h) range [{a.min():.6f}, {a.max():.6f}], "
199	            f"mlp I(h) range [{m.min():.6f}, {m.max():.6f}]"
200	        )
201	
202	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
203	    result = {"attn_importance": attn_importance, "mlp_importance": mlp_importance}
204	    torch.save(result, args.output_path)
205	    logger.info(f"Saved importance scores to {args.output_path}")
206	
207	
208	if __name__ == "__main__":
209	    main()
210	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "24ed7c0d-4fb5-4151-ba81-9a6c3b7872fd",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/importance_score.py",
      "content": "\"\"\"\nGradient-based Importance Scoring for structured pruning.\n\nComputes Taylor-expansion importance I(h) = ||w_h * grad_h||_2 for each\nattention head and MLP channel group on calibration data.\n\nInput:  model + calibration data (GSM8K train subset)\nOutput: per-structure I(h) scores saved as dict in .pt file\n        Keys: 'attn_importance' (dict[layer_idx -> tensor[n_heads]]),\n              'mlp_importance'  (dict[layer_idx -> tensor[n_groups]])\n\"\"\"\n\nimport argparse\nimport logging\nimport os\nimport random\n\nimport numpy as np\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    \"\"\"Load GSM8K train questions as calibration prompts with labels for loss computation.\"\"\"\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n\n    encodings = []\n    for example in ds:\n        text = f\"Question: {example['question']}\\nAnswer: {example['answer']}\"\n        ids = tokenizer(text, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef compute_importance(model, calibration_data, device):\n    \"\"\"Compute gradient-based importance for attention heads and MLP groups.\n\n    Uses Taylor expansion: I(h) = ||w_h * grad_h||_2\n    Accumulates over calibration batches.\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    head_dim = config.hidden_size // n_heads\n    intermediate_size = config.intermediate_size\n    n_groups = n_heads  # match attention head count for MLP groups\n    group_size = intermediate_size // n_groups\n\n    attn_importance = {i: torch.zeros(n_heads, device=\"cpu\") for i in range(n_layers)}\n    mlp_importance = {i: torch.zeros(n_groups, device=\"cpu\") for i in range(n_layers)}\n\n    model.train()\n\n    for batch_idx, enc in enumerate(calibration_data):\n        input_ids = enc[\"input_ids\"].to(device)\n        attention_mask = enc[\"attention_mask\"].to(device)\n        labels = input_ids.clone()\n\n        model.zero_grad()\n        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=labels)\n        loss = outputs.loss\n        loss.backward()\n\n        with torch.no_grad():\n            for layer_idx in range(n_layers):\n                layer = model.model.layers[layer_idx]\n\n                # Attention head importance via q_proj weights\n                q_weight = layer.self_attn.q_proj.weight  # [n_heads*head_dim, hidden]\n                q_grad = layer.self_attn.q_proj.weight.grad\n                if q_grad is not None:\n                    # Reshape to [n_heads, head_dim, hidden]\n                    w = q_weight.view(n_heads, head_dim, -1)\n                    g = q_grad.view(n_heads, head_dim, -1)\n                    taylor = (w * g).float()  # [n_heads, head_dim, hidden]\n                    # L2 norm per head\n                    head_scores = taylor.view(n_heads, -1).norm(dim=1)  # [n_heads]\n                    attn_importance[layer_idx] += head_scores.cpu()\n\n                # Also incorporate k_proj and v_proj for attention importance\n                for proj_name in [\"k_proj\", \"v_proj\", \"o_proj\"]:\n                    proj = getattr(layer.self_attn, proj_name)\n                    w = proj.weight\n                    g = proj.weight.grad\n                    if g is None:\n                        continue\n                    if proj_name == \"o_proj\":\n                        # o_proj: [hidden, n_heads*head_dim] — split on dim=1\n                        w_r = w.view(-1, n_heads, head_dim)\n                        g_r = g.view(-1, n_heads, head_dim)\n                        taylor = (w_r * g_r).float()\n                        head_scores = taylor.permute(1, 0, 2).reshape(n_heads, -1).norm(dim=1)\n                    elif proj_name == \"k_proj\":\n                        # GQA: k_proj has n_kv_heads, broadcast to n_heads\n                        n_kv = config.num_key_value_heads\n                        kv_head_dim = config.hidden_size // n_heads\n                        w_r = w.view(n_kv, kv_head_dim, -1)\n                        g_r = g.view(n_kv, kv_head_dim, -1)\n                        taylor = (w_r * g_r).float()\n                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)\n                        # Broadcast KV heads to query heads\n                        heads_per_kv = n_heads // n_kv\n                        head_scores = kv_scores.repeat_interleave(heads_per_kv)\n                    elif proj_name == \"v_proj\":\n                        n_kv = config.num_key_value_heads\n                        kv_head_dim = config.hidden_size // n_heads\n                        w_r = w.view(n_kv, kv_head_dim, -1)\n                        g_r = g.view(n_kv, kv_head_dim, -1)\n                        taylor = (w_r * g_r).float()\n                        kv_scores = taylor.view(n_kv, -1).norm(dim=1)\n                        heads_per_kv = n_heads // n_kv\n                        head_scores = kv_scores.repeat_interleave(heads_per_kv)\n                    attn_importance[layer_idx] += head_scores.cpu()\n\n                # MLP importance via gate_proj\n                gate_w = layer.mlp.gate_proj.weight  # [intermediate, hidden]\n                gate_g = layer.mlp.gate_proj.weight.grad\n                if gate_g is not None:\n                    usable = n_groups * group_size\n                    w_r = gate_w[:usable].view(n_groups, group_size, -1)\n                    g_r = gate_g[:usable].view(n_groups, group_size, -1)\n                    taylor = (w_r * g_r).float()\n                    group_scores = taylor.view(n_groups, -1).norm(dim=1)\n                    mlp_importance[layer_idx] += group_scores.cpu()\n\n                # Also use up_proj for MLP importance\n                up_w = layer.mlp.up_proj.weight\n                up_g = layer.mlp.up_proj.weight.grad\n                if up_g is not None:\n                    usable = n_groups * group_size\n                    w_r = up_w[:usable].view(n_groups, group_size, -1)\n                    g_r = up_g[:usable].view(n_groups, group_size, -1)\n                    taylor = (w_r * g_r).float()\n                    group_scores = taylor.view(n_groups, -1).norm(dim=1)\n                    mlp_importance[layer_idx] += group_scores.cpu()\n\n        if (batch_idx + 1) % 50 == 0:\n            logger.info(f\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\")\n\n    # Average over samples\n    n = len(calibration_data)\n    for layer_idx in range(n_layers):\n        attn_importance[layer_idx] /= n\n        mlp_importance[layer_idx] /= n\n\n    return attn_importance, mlp_importance\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Compute gradient-based importance scores for RASP\")\n    parser.add_argument(\"--model_path\", type=str, required=True, help=\"Path to pretrained model\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output .pt file for importance scores\")\n    parser.add_argument(\"--n_samples\", type=int, default=512, help=\"Number of calibration samples\")\n    parser.add_argument(\"--max_length\", type=int, default=512, help=\"Max token length for calibration inputs\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\", choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    dtype_map = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16, \"float32\": torch.float32}\n    torch_dtype = dtype_map[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch_dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n\n    logger.info(f\"Loading {args.n_samples} calibration samples\")\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\n\n    logger.info(\"Computing gradient-based importance scores...\")\n    attn_importance, mlp_importance = compute_importance(model, calibration_data, device)\n\n    for layer_idx in range(model.config.num_hidden_layers):\n        a = attn_importance[layer_idx]\n        m = mlp_importance[layer_idx]\n        logger.info(\n            f\"  Layer {layer_idx}: attn I(h) range [{a.min():.6f}, {a.max():.6f}], \"\n            f\"mlp I(h) range [{m.min():.6f}, {m.max():.6f}]\"\n        )\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    result = {\"attn_importance\": attn_importance, \"mlp_importance\": mlp_importance}\n    torch.save(result, args.output_path)\n    logger.info(f\"Saved importance scores to {args.output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 210,
      "startLine": 1,
      "totalLines": 210
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
Now let me also read the remaining files in our project (rasp_scoring.py, cka_overlap.py) and the GRASPrune data.py and README for full context.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "6cf00061-ef4d-4300-b3cb-6a4b26b39b9b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 48_

Now let me read the remaining key files and the GRASPrune paper HTML for the mathematical details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "b5956da3-c853-4a7e-b399-8739b98dcd68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 49_

<details open><summary>🔧 Tool call — Read · `toolu_01GM75BZQdAgwR1WxxQc5jrk`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "1381bf8f-fdb6-4140-bfc3-2ece37e73db3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 50 · 2026-05-14T08:21:38.038Z_

<details><summary>↩ Tool result · `toolu_01GM75BZQdAgwR1WxxQc5jrk`</summary>

```text
1	"""
2	RASP Scoring: combine importance I(h) and functional overlap F(h).
3	
4	S(h) = I(h) * (1 - F(h))^alpha
5	
6	Structures with lower S(h) are pruned first.
7	Standard baseline uses only I(h) for ranking.
8	"""
9	
10	import argparse
11	import logging
12	import os
13	
14	import torch
15	
16	logging.basicConfig(
17	    level=logging.INFO,
18	    format="%(asctime)s [%(levelname)s] %(message)s",
19	)
20	logger = logging.getLogger(__name__)
21	
22	
23	def compute_rasp_scores(importance: dict, overlap: dict, alpha: float = 1.0) -> dict:
24	    """Compute S(h) = I(h) * (1 - F(h))^alpha for each structure.
25	
26	    Args:
27	        importance: dict[layer_idx -> tensor of I(h)]
28	        overlap: dict[layer_idx -> tensor of F(h)]
29	        alpha: recoverability penalty exponent
30	
31	    Returns:
32	        dict[layer_idx -> tensor of S(h)]
33	    """
34	    scores = {}
35	    for layer_idx in importance:
36	        ih = importance[layer_idx].float()
37	        fh = overlap[layer_idx].float()
38	        sh = ih * (1.0 - fh).pow(alpha)
39	        scores[layer_idx] = sh
40	    return scores
41	
42	
43	def rank_structures(scores: dict) -> list:
44	    """Flatten and rank all structures globally by score (ascending = prune first).
45	
46	    Returns list of (score, layer_idx, struct_idx) sorted ascending.
47	    """
48	    entries = []
49	    for layer_idx, layer_scores in scores.items():
50	        for struct_idx in range(layer_scores.shape[0]):
51	            entries.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))
52	    entries.sort(key=lambda x: x[0])
53	    return entries
54	
55	
56	def main():
57	    parser = argparse.ArgumentParser(description="Compute RASP pruning scores")
58	    parser.add_argument("--importance_path", type=str, required=True, help="Path to importance scores .pt")
59	    parser.add_argument("--cka_path", type=str, default=None, help="Path to CKA overlap scores .pt (None for standard mode)")
60	    parser.add_argument("--mode", type=str, choices=["standard", "rasp"], default="rasp")
61	    parser.add_argument("--alpha", type=float, default=1.0, help="Recoverability penalty exponent")
62	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for pruning scores")
63	    args = parser.parse_args()
64	
65	    importance_data = torch.load(args.importance_path, map_location="cpu", weights_only=True)
66	    attn_importance = importance_data["attn_importance"]
67	    mlp_importance = importance_data["mlp_importance"]
68	
69	    if args.mode == "rasp":
70	        if args.cka_path is None:
71	            raise ValueError("--cka_path required for rasp mode")
72	        cka_data = torch.load(args.cka_path, map_location="cpu", weights_only=True)
73	        attn_overlap = cka_data["attn_overlap"]
74	        mlp_overlap = cka_data["mlp_overlap"]
75	
76	        attn_scores = compute_rasp_scores(attn_importance, attn_overlap, args.alpha)
77	        mlp_scores = compute_rasp_scores(mlp_importance, mlp_overlap, args.alpha)
78	        logger.info(f"Computed RASP scores with alpha={args.alpha}")
79	    else:
80	        # Standard: score = importance only
81	        attn_scores = {k: v.float() for k, v in attn_importance.items()}
82	        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}
83	        logger.info("Computed standard importance-only scores")
84	
85	    attn_ranking = rank_structures(attn_scores)
86	    mlp_ranking = rank_structures(mlp_scores)
87	
88	    logger.info(f"Attention heads total: {len(attn_ranking)}, lowest 5 scores: "
89	                f"{[f'L{e[1]}H{e[2]}={e[0]:.6f}' for e in attn_ranking[:5]]}")
90	    logger.info(f"MLP groups total: {len(mlp_ranking)}, lowest 5 scores: "
91	                f"{[f'L{e[1]}G{e[2]}={e[0]:.6f}' for e in mlp_ranking[:5]]}")
92	
93	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
94	    result = {
95	        "attn_scores": attn_scores,
96	        "mlp_scores": mlp_scores,
97	        "attn_ranking": attn_ranking,
98	        "mlp_ranking": mlp_ranking,
99	        "mode": args.mode,
100	        "alpha": args.alpha,
101	    }
102	    torch.save(result, args.output_path)
103	    logger.info(f"Saved pruning scores to {args.output_path}")
104	
105	
106	if __name__ == "__main__":
107	    main()
108	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "25de9ed6-0aee-466a-9bdd-0772a9d156d9",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/rasp_scoring.py",
      "content": "\"\"\"\nRASP Scoring: combine importance I(h) and functional overlap F(h).\n\nS(h) = I(h) * (1 - F(h))^alpha\n\nStructures with lower S(h) are pruned first.\nStandard baseline uses only I(h) for ranking.\n\"\"\"\n\nimport argparse\nimport logging\nimport os\n\nimport torch\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef compute_rasp_scores(importance: dict, overlap: dict, alpha: float = 1.0) -> dict:\n    \"\"\"Compute S(h) = I(h) * (1 - F(h))^alpha for each structure.\n\n    Args:\n        importance: dict[layer_idx -> tensor of I(h)]\n        overlap: dict[layer_idx -> tensor of F(h)]\n        alpha: recoverability penalty exponent\n\n    Returns:\n        dict[layer_idx -> tensor of S(h)]\n    \"\"\"\n    scores = {}\n    for layer_idx in importance:\n        ih = importance[layer_idx].float()\n        fh = overlap[layer_idx].float()\n        sh = ih * (1.0 - fh).pow(alpha)\n        scores[layer_idx] = sh\n    return scores\n\n\ndef rank_structures(scores: dict) -> list:\n    \"\"\"Flatten and rank all structures globally by score (ascending = prune first).\n\n    Returns list of (score, layer_idx, struct_idx) sorted ascending.\n    \"\"\"\n    entries = []\n    for layer_idx, layer_scores in scores.items():\n        for struct_idx in range(layer_scores.shape[0]):\n            entries.append((layer_scores[struct_idx].item(), layer_idx, struct_idx))\n    entries.sort(key=lambda x: x[0])\n    return entries\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Compute RASP pruning scores\")\n    parser.add_argument(\"--importance_path\", type=str, required=True, help=\"Path to importance scores .pt\")\n    parser.add_argument(\"--cka_path\", type=str, default=None, help=\"Path to CKA overlap scores .pt (None for standard mode)\")\n    parser.add_argument(\"--mode\", type=str, choices=[\"standard\", \"rasp\"], default=\"rasp\")\n    parser.add_argument(\"--alpha\", type=float, default=1.0, help=\"Recoverability penalty exponent\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output .pt file for pruning scores\")\n    args = parser.parse_args()\n\n    importance_data = torch.load(args.importance_path, map_location=\"cpu\", weights_only=True)\n    attn_importance = importance_data[\"attn_importance\"]\n    mlp_importance = importance_data[\"mlp_importance\"]\n\n    if args.mode == \"rasp\":\n        if args.cka_path is None:\n            raise ValueError(\"--cka_path required for rasp mode\")\n        cka_data = torch.load(args.cka_path, map_location=\"cpu\", weights_only=True)\n        attn_overlap = cka_data[\"attn_overlap\"]\n        mlp_overlap = cka_data[\"mlp_overlap\"]\n\n        attn_scores = compute_rasp_scores(attn_importance, attn_overlap, args.alpha)\n        mlp_scores = compute_rasp_scores(mlp_importance, mlp_overlap, args.alpha)\n        logger.info(f\"Computed RASP scores with alpha={args.alpha}\")\n    else:\n        # Standard: score = importance only\n        attn_scores = {k: v.float() for k, v in attn_importance.items()}\n        mlp_scores = {k: v.float() for k, v in mlp_importance.items()}\n        logger.info(\"Computed standard importance-only scores\")\n\n    attn_ranking = rank_structures(attn_scores)\n    mlp_ranking = rank_structures(mlp_scores)\n\n    logger.info(f\"Attention heads total: {len(attn_ranking)}, lowest 5 scores: \"\n                f\"{[f'L{e[1]}H{e[2]}={e[0]:.6f}' for e in attn_ranking[:5]]}\")\n    logger.info(f\"MLP groups total: {len(mlp_ranking)}, lowest 5 scores: \"\n                f\"{[f'L{e[1]}G{e[2]}={e[0]:.6f}' for e in mlp_ranking[:5]]}\")\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    result = {\n        \"attn_scores\": attn_scores,\n        \"mlp_scores\": mlp_scores,\n        \"attn_ranking\": attn_ranking,\n        \"mlp_ranking\": mlp_ranking,\n        \"mode\": args.mode,\n        \"alpha\": args.alpha,\n    }\n    torch.save(result, args.output_path)\n    logger.info(f\"Saved pruning scores to {args.output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 108,
      "startLine": 1,
      "totalLines": 108
    }
  }
}
```

</details>

---

### Tool call

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_01KdtdjcWeDSDpJA4fj3vitC`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "6edb226f-53e5-4350-9cb3-3ea9ff3c6f21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 52 · 2026-05-14T08:21:38.958Z_

<details><summary>↩ Tool result · `toolu_01KdtdjcWeDSDpJA4fj3vitC`</summary>

```text
1	"""
2	CKA Overlap Computation for RASP.
3	
4	Computes intra-layer functional overlap F(h) for each attention head and MLP channel group
5	using linear CKA (Centered Kernel Alignment via HSIC).
6	
7	Input:  model + calibration data (GSM8K train subset)
8	Output: per-structure F(h) scores saved as dict in .pt file
9	        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),
10	              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])
11	"""
12	
13	import argparse
14	import logging
15	import math
16	import os
17	import random
18	
19	import numpy as np
20	import torch
21	from datasets import load_dataset
22	from transformers import AutoModelForCausalLM, AutoTokenizer
23	
24	logging.basicConfig(
25	    level=logging.INFO,
26	    format="%(asctime)s [%(levelname)s] %(message)s",
27	)
28	logger = logging.getLogger(__name__)
29	
30	
31	def set_seed(seed: int):
32	    random.seed(seed)
33	    np.random.seed(seed)
34	    torch.manual_seed(seed)
35	    torch.cuda.manual_seed_all(seed)
36	
37	
38	def linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:
39	    """Linear CKA between two activation matrices.
40	    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].
41	    """
42	    X = X - X.mean(0)
43	    Y = Y - Y.mean(0)
44	    hsic_xy = torch.norm(X.T @ Y, "fro") ** 2
45	    hsic_xx = torch.norm(X.T @ X, "fro") ** 2
46	    hsic_yy = torch.norm(Y.T @ Y, "fro") ** 2
47	    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()
48	
49	
50	def load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):
51	    """Load GSM8K train questions as calibration prompts."""
52	    ds = load_dataset("openai/gsm8k", "main", split="train")
53	    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))
54	
55	    encodings = []
56	    for example in ds:
57	        prompt = f"Question: {example['question']}\nAnswer: Let me think step by step.\n"
58	        ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length)
59	        encodings.append(ids)
60	    return encodings
61	
62	
63	def collect_head_activations(model, tokenizer, calibration_data, device):
64	    """Run calibration data through model and collect per-head activations for each layer.
65	
66	    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]
67	    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.
68	    """
69	    config = model.config
70	    n_layers = config.num_hidden_layers
71	    n_heads = config.num_attention_heads
72	    head_dim = config.hidden_size // n_heads
73	
74	    layer_activations = {i: [] for i in range(n_layers)}
75	    hooks = []
76	
77	    def make_hook(layer_idx):
78	        def hook_fn(module, input, output):
79	            # output of attention: (hidden_states, attn_weights, past_kv)
80	            # We hook into q_proj to get query states, then reshape per-head
81	            pass
82	        return hook_fn
83	
84	    # Hook into each attention layer's output (the hidden_states after o_proj)
85	    # We instead hook the q_proj to capture per-head representations
86	    q_proj_outputs = {i: [] for i in range(n_layers)}
87	
88	    def make_q_hook(layer_idx):
89	        def hook_fn(module, input, output):
90	            # output shape: [batch, seq_len, n_heads * head_dim]
91	            q_proj_outputs[layer_idx].append(output.detach())
92	        return hook_fn
93	
94	    for i in range(n_layers):
95	        layer = model.model.layers[i]
96	        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))
97	        hooks.append(h)
98	
99	    model.eval()
100	    with torch.no_grad():
101	        for batch_idx, enc in enumerate(calibration_data):
102	            input_ids = enc["input_ids"].to(device)
103	            attention_mask = enc["attention_mask"].to(device)
104	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
105	            if (batch_idx + 1) % 50 == 0:
106	                logger.info(f"  Processed {batch_idx + 1}/{len(calibration_data)} samples")
107	
108	    for h in hooks:
109	        h.remove()
110	
111	    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]
112	    for layer_idx in range(n_layers):
113	        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]
114	        per_head_list = []
115	        for t in tensors:
116	            t = t.squeeze(0)  # [seq, n_heads*head_dim]
117	            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]
118	            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq
119	            per_head_list.append(t)
120	        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]
121	        q_proj_outputs[layer_idx] = None  # free memory
122	
123	    return layer_activations
124	
125	
126	def collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):
127	    """Collect MLP intermediate activations grouped into channel groups.
128	
129	    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]
130	    """
131	    config = model.config
132	    n_layers = config.num_hidden_layers
133	    intermediate_size = config.intermediate_size
134	    group_size = intermediate_size // n_groups
135	
136	    gate_outputs = {i: [] for i in range(n_layers)}
137	    hooks = []
138	
139	    def make_gate_hook(layer_idx):
140	        def hook_fn(module, input, output):
141	            gate_outputs[layer_idx].append(output.detach())
142	        return hook_fn
143	
144	    for i in range(n_layers):
145	        layer = model.model.layers[i]
146	        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))
147	        hooks.append(h)
148	
149	    model.eval()
150	    with torch.no_grad():
151	        for enc in calibration_data:
152	            input_ids = enc["input_ids"].to(device)
153	            attention_mask = enc["attention_mask"].to(device)
154	            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)
155	
156	    for h in hooks:
157	        h.remove()
158	
159	    layer_activations = {}
160	    for layer_idx in range(n_layers):
161	        tensors = gate_outputs[layer_idx]
162	        per_group_list = []
163	        for t in tensors:
164	            t = t.squeeze(0)  # [seq, intermediate_size]
165	            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq
166	            # Truncate to exact multiple of group_size
167	            usable = n_groups * group_size
168	            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]
169	            per_group_list.append(t)
170	        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]
171	        gate_outputs[layer_idx] = None
172	
173	    return layer_activations
174	
175	
176	def compute_overlap(activations_dict: dict, structure_name: str) -> tuple:
177	    """Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.
178	
179	    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]
180	    Returns: (overlap_scores, cka_matrices)
181	        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]
182	        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA
183	    """
184	    overlap_scores = {}
185	    cka_matrices = {}
186	    for layer_idx, acts in activations_dict.items():
187	        n_samples, n_structs, dim = acts.shape
188	        matrix = torch.zeros(n_structs, n_structs)
189	        for i in range(n_structs):
190	            matrix[i, i] = 1.0
191	            for j in range(i + 1, n_structs):
192	                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())
193	                matrix[i, j] = val
194	                matrix[j, i] = val
195	        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)
196	        overlap_scores[layer_idx] = scores
197	        cka_matrices[layer_idx] = matrix
198	        logger.info(
199	            f"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], "
200	            f"mean={scores.mean():.4f}"
201	        )
202	    return overlap_scores, cka_matrices
203	
204	
205	def main():
206	    parser = argparse.ArgumentParser(description="Compute CKA-based functional overlap scores for RASP")
207	    parser.add_argument("--model_path", type=str, required=True, help="Path to pretrained model")
208	    parser.add_argument("--output_path", type=str, required=True, help="Output .pt file for overlap scores")
209	    parser.add_argument("--n_samples", type=int, default=512, help="Number of calibration samples")
210	    parser.add_argument("--max_length", type=int, default=512, help="Max token length for calibration inputs")
211	    parser.add_argument("--mlp_groups", type=int, default=28, help="Number of MLP channel groups per layer")
212	    parser.add_argument("--seed", type=int, default=42, help="Random seed")
213	    parser.add_argument("--dtype", type=str, default="bfloat16", choices=["float16", "bfloat16", "float32"])
214	    args = parser.parse_args()
215	
216	    set_seed(args.seed)
217	    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
218	    dtype_map = {"float16": torch.float16, "bfloat16": torch.bfloat16, "float32": torch.float32}
219	    torch_dtype = dtype_map[args.dtype]
220	
221	    logger.info(f"Loading model from {args.model_path}")
222	    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)
223	    model = AutoModelForCausalLM.from_pretrained(
224	        args.model_path,
225	        torch_dtype=torch_dtype,
226	        device_map=device,
227	        trust_remote_code=True,
228	    )
229	
230	    logger.info(f"Loading {args.n_samples} calibration samples from GSM8K train")
231	    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)
232	
233	    logger.info("Collecting attention head activations...")
234	    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)
235	
236	    logger.info("Computing attention head overlap F(h)...")
237	    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, "attn_heads")
238	    del head_acts
239	    torch.cuda.empty_cache()
240	
241	    logger.info("Collecting MLP activations...")
242	    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)
243	
244	    logger.info("Computing MLP group overlap F(h)...")
245	    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, "mlp_groups")
246	    del mlp_acts
247	    torch.cuda.empty_cache()
248	
249	    os.makedirs(os.path.dirname(args.output_path) or ".", exist_ok=True)
250	    result = {
251	        "attn_overlap": attn_overlap,
252	        "mlp_overlap": mlp_overlap,
253	        "attn_cka_matrix": attn_cka_matrix,
254	        "mlp_cka_matrix": mlp_cka_matrix,
255	    }
256	    torch.save(result, args.output_path)
257	    logger.info(f"Saved CKA overlap scores to {args.output_path}")
258	
259	
260	if __name__ == "__main__":
261	    main()
262	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "ef5bbece-9462-435c-971d-5e7b7ab3b9ab",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/src/cka_overlap.py",
      "content": "\"\"\"\nCKA Overlap Computation for RASP.\n\nComputes intra-layer functional overlap F(h) for each attention head and MLP channel group\nusing linear CKA (Centered Kernel Alignment via HSIC).\n\nInput:  model + calibration data (GSM8K train subset)\nOutput: per-structure F(h) scores saved as dict in .pt file\n        Keys: 'attn_overlap' (dict[layer_idx -> tensor[n_heads]]),\n              'mlp_overlap'  (dict[layer_idx -> tensor[n_groups]])\n\"\"\"\n\nimport argparse\nimport logging\nimport math\nimport os\nimport random\n\nimport numpy as np\nimport torch\nfrom datasets import load_dataset\nfrom transformers import AutoModelForCausalLM, AutoTokenizer\n\nlogging.basicConfig(\n    level=logging.INFO,\n    format=\"%(asctime)s [%(levelname)s] %(message)s\",\n)\nlogger = logging.getLogger(__name__)\n\n\ndef set_seed(seed: int):\n    random.seed(seed)\n    np.random.seed(seed)\n    torch.manual_seed(seed)\n    torch.cuda.manual_seed_all(seed)\n\n\ndef linear_cka(X: torch.Tensor, Y: torch.Tensor) -> float:\n    \"\"\"Linear CKA between two activation matrices.\n    X: [n, p], Y: [n, q]. Returns scalar similarity in [0, 1].\n    \"\"\"\n    X = X - X.mean(0)\n    Y = Y - Y.mean(0)\n    hsic_xy = torch.norm(X.T @ Y, \"fro\") ** 2\n    hsic_xx = torch.norm(X.T @ X, \"fro\") ** 2\n    hsic_yy = torch.norm(Y.T @ Y, \"fro\") ** 2\n    return (hsic_xy / (torch.sqrt(hsic_xx) * torch.sqrt(hsic_yy) + 1e-8)).item()\n\n\ndef load_calibration_data(tokenizer, n_samples: int, max_length: int = 512, seed: int = 42):\n    \"\"\"Load GSM8K train questions as calibration prompts.\"\"\"\n    ds = load_dataset(\"openai/gsm8k\", \"main\", split=\"train\")\n    ds = ds.shuffle(seed=seed).select(range(min(n_samples, len(ds))))\n\n    encodings = []\n    for example in ds:\n        prompt = f\"Question: {example['question']}\\nAnswer: Let me think step by step.\\n\"\n        ids = tokenizer(prompt, return_tensors=\"pt\", truncation=True, max_length=max_length)\n        encodings.append(ids)\n    return encodings\n\n\ndef collect_head_activations(model, tokenizer, calibration_data, device):\n    \"\"\"Run calibration data through model and collect per-head activations for each layer.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_heads, pooled_dim]\n    where pooled_dim collapses (seq_len, head_dim) via mean-pool over seq_len.\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    n_heads = config.num_attention_heads\n    head_dim = config.hidden_size // n_heads\n\n    layer_activations = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output of attention: (hidden_states, attn_weights, past_kv)\n            # We hook into q_proj to get query states, then reshape per-head\n            pass\n        return hook_fn\n\n    # Hook into each attention layer's output (the hidden_states after o_proj)\n    # We instead hook the q_proj to capture per-head representations\n    q_proj_outputs = {i: [] for i in range(n_layers)}\n\n    def make_q_hook(layer_idx):\n        def hook_fn(module, input, output):\n            # output shape: [batch, seq_len, n_heads * head_dim]\n            q_proj_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.self_attn.q_proj.register_forward_hook(make_q_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for batch_idx, enc in enumerate(calibration_data):\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n            if (batch_idx + 1) % 50 == 0:\n                logger.info(f\"  Processed {batch_idx + 1}/{len(calibration_data)} samples\")\n\n    for h in hooks:\n        h.remove()\n\n    # Reshape and mean-pool: [batch, seq, n_heads*head_dim] -> per-head [batch, head_dim]\n    for layer_idx in range(n_layers):\n        tensors = q_proj_outputs[layer_idx]  # list of [1, seq, n_heads*head_dim]\n        per_head_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, n_heads*head_dim]\n            t = t.view(t.shape[0], n_heads, head_dim)  # [seq, n_heads, head_dim]\n            t = t.mean(dim=0)  # [n_heads, head_dim] — mean pool over seq\n            per_head_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_head_list, dim=0)  # [n_samples, n_heads, head_dim]\n        q_proj_outputs[layer_idx] = None  # free memory\n\n    return layer_activations\n\n\ndef collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups: int = 28):\n    \"\"\"Collect MLP intermediate activations grouped into channel groups.\n\n    Returns dict[layer_idx] -> tensor[n_samples, n_groups, group_dim]\n    \"\"\"\n    config = model.config\n    n_layers = config.num_hidden_layers\n    intermediate_size = config.intermediate_size\n    group_size = intermediate_size // n_groups\n\n    gate_outputs = {i: [] for i in range(n_layers)}\n    hooks = []\n\n    def make_gate_hook(layer_idx):\n        def hook_fn(module, input, output):\n            gate_outputs[layer_idx].append(output.detach())\n        return hook_fn\n\n    for i in range(n_layers):\n        layer = model.model.layers[i]\n        h = layer.mlp.gate_proj.register_forward_hook(make_gate_hook(i))\n        hooks.append(h)\n\n    model.eval()\n    with torch.no_grad():\n        for enc in calibration_data:\n            input_ids = enc[\"input_ids\"].to(device)\n            attention_mask = enc[\"attention_mask\"].to(device)\n            model(input_ids=input_ids, attention_mask=attention_mask, use_cache=False)\n\n    for h in hooks:\n        h.remove()\n\n    layer_activations = {}\n    for layer_idx in range(n_layers):\n        tensors = gate_outputs[layer_idx]\n        per_group_list = []\n        for t in tensors:\n            t = t.squeeze(0)  # [seq, intermediate_size]\n            t = t.mean(dim=0)  # [intermediate_size] — mean pool over seq\n            # Truncate to exact multiple of group_size\n            usable = n_groups * group_size\n            t = t[:usable].view(n_groups, group_size)  # [n_groups, group_size]\n            per_group_list.append(t)\n        layer_activations[layer_idx] = torch.stack(per_group_list, dim=0)  # [n_samples, n_groups, group_size]\n        gate_outputs[layer_idx] = None\n\n    return layer_activations\n\n\ndef compute_overlap(activations_dict: dict, structure_name: str) -> tuple:\n    \"\"\"Compute F(h) = mean CKA similarity and pairwise CKA matrix per layer.\n\n    activations_dict: dict[layer_idx] -> tensor[n_samples, n_structures, dim]\n    Returns: (overlap_scores, cka_matrices)\n        overlap_scores: dict[layer_idx] -> tensor[n_structures] of overlap F(h) in [0, 1]\n        cka_matrices: dict[layer_idx] -> tensor[n_structures, n_structures] pairwise CKA\n    \"\"\"\n    overlap_scores = {}\n    cka_matrices = {}\n    for layer_idx, acts in activations_dict.items():\n        n_samples, n_structs, dim = acts.shape\n        matrix = torch.zeros(n_structs, n_structs)\n        for i in range(n_structs):\n            matrix[i, i] = 1.0\n            for j in range(i + 1, n_structs):\n                val = linear_cka(acts[:, i, :].float(), acts[:, j, :].float())\n                matrix[i, j] = val\n                matrix[j, i] = val\n        scores = (matrix.sum(dim=1) - 1.0) / max(n_structs - 1, 1)\n        overlap_scores[layer_idx] = scores\n        cka_matrices[layer_idx] = matrix\n        logger.info(\n            f\"  Layer {layer_idx} {structure_name}: F(h) range [{scores.min():.4f}, {scores.max():.4f}], \"\n            f\"mean={scores.mean():.4f}\"\n        )\n    return overlap_scores, cka_matrices\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=\"Compute CKA-based functional overlap scores for RASP\")\n    parser.add_argument(\"--model_path\", type=str, required=True, help=\"Path to pretrained model\")\n    parser.add_argument(\"--output_path\", type=str, required=True, help=\"Output .pt file for overlap scores\")\n    parser.add_argument(\"--n_samples\", type=int, default=512, help=\"Number of calibration samples\")\n    parser.add_argument(\"--max_length\", type=int, default=512, help=\"Max token length for calibration inputs\")\n    parser.add_argument(\"--mlp_groups\", type=int, default=28, help=\"Number of MLP channel groups per layer\")\n    parser.add_argument(\"--seed\", type=int, default=42, help=\"Random seed\")\n    parser.add_argument(\"--dtype\", type=str, default=\"bfloat16\", choices=[\"float16\", \"bfloat16\", \"float32\"])\n    args = parser.parse_args()\n\n    set_seed(args.seed)\n    device = torch.device(\"cuda\" if torch.cuda.is_available() else \"cpu\")\n    dtype_map = {\"float16\": torch.float16, \"bfloat16\": torch.bfloat16, \"float32\": torch.float32}\n    torch_dtype = dtype_map[args.dtype]\n\n    logger.info(f\"Loading model from {args.model_path}\")\n    tokenizer = AutoTokenizer.from_pretrained(args.model_path, trust_remote_code=True)\n    model = AutoModelForCausalLM.from_pretrained(\n        args.model_path,\n        torch_dtype=torch_dtype,\n        device_map=device,\n        trust_remote_code=True,\n    )\n\n    logger.info(f\"Loading {args.n_samples} calibration samples from GSM8K train\")\n    calibration_data = load_calibration_data(tokenizer, args.n_samples, args.max_length, args.seed)\n\n    logger.info(\"Collecting attention head activations...\")\n    head_acts = collect_head_activations(model, tokenizer, calibration_data, device)\n\n    logger.info(\"Computing attention head overlap F(h)...\")\n    attn_overlap, attn_cka_matrix = compute_overlap(head_acts, \"attn_heads\")\n    del head_acts\n    torch.cuda.empty_cache()\n\n    logger.info(\"Collecting MLP activations...\")\n    mlp_acts = collect_mlp_activations(model, tokenizer, calibration_data, device, n_groups=args.mlp_groups)\n\n    logger.info(\"Computing MLP group overlap F(h)...\")\n    mlp_overlap, mlp_cka_matrix = compute_overlap(mlp_acts, \"mlp_groups\")\n    del mlp_acts\n    torch.cuda.empty_cache()\n\n    os.makedirs(os.path.dirname(args.output_path) or \".\", exist_ok=True)\n    result = {\n        \"attn_overlap\": attn_overlap,\n        \"mlp_overlap\": mlp_overlap,\n        \"attn_cka_matrix\": attn_cka_matrix,\n        \"mlp_cka_matrix\": mlp_cka_matrix,\n    }\n    torch.save(result, args.output_path)\n    logger.info(f\"Saved CKA overlap scores to {args.output_path}\")\n\n\nif __name__ == \"__main__\":\n    main()\n",
      "numLines": 262,
      "startLine": 1,
      "totalLines": 262
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Read · `toolu_017DyRbFMz9iyicZeg7a7Gj6`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/data.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "c046f52c-f702-480a-af1f-0d649aeead8f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 54 · 2026-05-14T08:21:39.395Z_

<details><summary>↩ Tool result · `toolu_017DyRbFMz9iyicZeg7a7Gj6`</summary>

```text
1	from __future__ import annotations
2	
3	from pathlib import Path
4	from typing import Any
5	
6	import torch
7	from datasets import load_dataset
8	from datasets.utils.logging import disable_progress_bar
9	from torch.utils.data import Dataset
10	
11	
12	class TokenBlockDataset(Dataset):
13	    """Concatenate text samples and slice them into fixed-length token blocks."""
14	
15	    def __init__(self, ds: Any, tokenizer: Any, block_size: int, text_key: str | None = None):
16	        self.block_size = int(block_size)
17	
18	        if text_key is None:
19	            for candidate in ("text", "sentence", "content", "document"):
20	                if candidate in ds.column_names:
21	                    text_key = candidate
22	                    break
23	        if text_key is None:
24	            raise KeyError(
25	                f"No text column found in dataset columns={ds.column_names}. "
26	                "Pass text_key explicitly."
27	            )
28	
29	        texts = ds[text_key]
30	        tokenized = tokenizer("\n\n".join(map(str, texts)), return_tensors="pt", add_special_tokens=False)
31	        self.tokens = tokenized["input_ids"][0]
32	
33	        if self.tokens.numel() < self.block_size + 1:
34	            raise ValueError(
35	                f"Too few tokens: {self.tokens.numel()} < block_size + 1 = {self.block_size + 1}"
36	            )
37	
38	    def __len__(self) -> int:
39	        return (self.tokens.numel() - 1) // self.block_size
40	
41	    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:
42	        start = idx * self.block_size
43	        end = start + self.block_size
44	        input_ids = self.tokens[start:end].clone()
45	        attention_mask = torch.ones_like(input_ids)
46	        return {"input_ids": input_ids, "attention_mask": attention_mask}
47	
48	
49	def load_local_c4_dataset():
50	    c4_path = Path(__file__).resolve().parent / "data" / "c4-validation.json"
51	    try:
52	        disable_progress_bar()
53	        return load_dataset("json", data_files=str(c4_path))["train"]
54	    except Exception as exc:
55	        raise FileNotFoundError(
56	            "C4 evaluation/training support expects a local file named "
57	            "`data/c4-validation.json` in the GRASPrune root directory. "
58	            "Please download or prepare it manually before using dataset='c4'."
59	        ) from exc
60	
61	
62	def load_text_dataset(name: str, split: str):
63	    if name == "wikitext2":
64	        return load_dataset("wikitext", "wikitext-2-raw-v1", split=split)
65	    if name == "ptb":
66	        return load_dataset("ptb_text_only", "penn_treebank", split=split)
67	    if name == "c4":
68	        ds = load_local_c4_dataset()
69	        return ds.select(range(min(2000, len(ds)))) if split != "train" else ds
70	    raise ValueError(f"Unsupported dataset: {name}")
71	
72	
73	def _load_local_c4_json():
74	    return load_local_c4_dataset()
75	
76	
77	def load_raw_dataset(name: str, split: str):
78	    return load_text_dataset(name, split)
79	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "24c0fcd1-6339-438d-a2fd-95d6e3816b8d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/data.py",
      "content": "from __future__ import annotations\n\nfrom pathlib import Path\nfrom typing import Any\n\nimport torch\nfrom datasets import load_dataset\nfrom datasets.utils.logging import disable_progress_bar\nfrom torch.utils.data import Dataset\n\n\nclass TokenBlockDataset(Dataset):\n    \"\"\"Concatenate text samples and slice them into fixed-length token blocks.\"\"\"\n\n    def __init__(self, ds: Any, tokenizer: Any, block_size: int, text_key: str | None = None):\n        self.block_size = int(block_size)\n\n        if text_key is None:\n            for candidate in (\"text\", \"sentence\", \"content\", \"document\"):\n                if candidate in ds.column_names:\n                    text_key = candidate\n                    break\n        if text_key is None:\n            raise KeyError(\n                f\"No text column found in dataset columns={ds.column_names}. \"\n                \"Pass text_key explicitly.\"\n            )\n\n        texts = ds[text_key]\n        tokenized = tokenizer(\"\\n\\n\".join(map(str, texts)), return_tensors=\"pt\", add_special_tokens=False)\n        self.tokens = tokenized[\"input_ids\"][0]\n\n        if self.tokens.numel() < self.block_size + 1:\n            raise ValueError(\n                f\"Too few tokens: {self.tokens.numel()} < block_size + 1 = {self.block_size + 1}\"\n            )\n\n    def __len__(self) -> int:\n        return (self.tokens.numel() - 1) // self.block_size\n\n    def __getitem__(self, idx: int) -> dict[str, torch.Tensor]:\n        start = idx * self.block_size\n        end = start + self.block_size\n        input_ids = self.tokens[start:end].clone()\n        attention_mask = torch.ones_like(input_ids)\n        return {\"input_ids\": input_ids, \"attention_mask\": attention_mask}\n\n\ndef load_local_c4_dataset():\n    c4_path = Path(__file__).resolve().parent / \"data\" / \"c4-validation.json\"\n    try:\n        disable_progress_bar()\n        return load_dataset(\"json\", data_files=str(c4_path))[\"train\"]\n    except Exception as exc:\n        raise FileNotFoundError(\n            \"C4 evaluation/training support expects a local file named \"\n            \"`data/c4-validation.json` in the GRASPrune root directory. \"\n            \"Please download or prepare it manually before using dataset='c4'.\"\n        ) from exc\n\n\ndef load_text_dataset(name: str, split: str):\n    if name == \"wikitext2\":\n        return load_dataset(\"wikitext\", \"wikitext-2-raw-v1\", split=split)\n    if name == \"ptb\":\n        return load_dataset(\"ptb_text_only\", \"penn_treebank\", split=split)\n    if name == \"c4\":\n        ds = load_local_c4_dataset()\n        return ds.select(range(min(2000, len(ds)))) if split != \"train\" else ds\n    raise ValueError(f\"Unsupported dataset: {name}\")\n\n\ndef _load_local_c4_json():\n    return load_local_c4_dataset()\n\n\ndef load_raw_dataset(name: str, split: str):\n    return load_text_dataset(name, split)\n",
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_016cSpPKcnK53pwMTpiBZwZH`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/README.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "e0370ab2-f326-4b69-890f-a47daf59f950",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 56 · 2026-05-14T08:21:39.873Z_

<details><summary>↩ Tool result · `toolu_016cSpPKcnK53pwMTpiBZwZH`</summary>

````text
1	# GRASPrune
2	
3	Official implementation of **GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models**, accepted to **ACL 2026 Main Conference**.
4	
5	[[Paper]](https://arxiv.org/abs/2604.19398)
6	
7	GRASPrune is a post-training structured pruning toolkit for decoder-only LLMs. It learns global gates over FFN intermediate channels and attention KV groups, projects them into budget-feasible hard masks, applies lightweight rescale compensation, and exports a dense pruned checkpoint.
8	
9	The code currently supports LLaMA-style and Qwen-style models, including `meta-llama/Llama-2-7b-hf` and `Qwen/Qwen3-8B`.
10	
11	## Installation
12	
13	Python 3.10 is recommended.
14	
15	```bash
16	pip install -r requirements.txt
17	```
18	
19	## Pruning
20	
21	Run commands from the repository root.
22	
23	### LLaMA
24	
25	```bash
26	python train.py \
27	  --model-id meta-llama/Llama-2-7b-hf \
28	  --model-family llama \
29	  --device cuda:0 \
30	  --keep-ratio 0.6 \
31	  --epochs 4 \
32	  --num-samples 512
33	```
34	
35	### Qwen
36	
37	```bash
38	python train.py \
39	  --model-id Qwen/Qwen3-8B \
40	  --model-family qwen \
41	  --trust-remote-code \
42	  --device cuda:0 \
43	  --keep-ratio 0.8 \
44	  --epochs 4 \
45	  --num-samples 512
46	```
47	
48	If the model is not cached locally, add:
49	
50	```bash
51	--allow-remote-model
52	```
53	
54	Main options:
55	
56	- `--keep-ratio`: retained structural budget.
57	- `--epochs`: number of gate-training epochs.
58	- `--num-samples`: number of calibration sequences.
59	- `--max-len`: calibration sequence length.
60	- `--output-dir`: custom output directory.
61	
62	## Outputs
63	
64	Checkpoints are saved under `outputs/` by default. Each output directory contains:
65	
66	```text
67	pruned_state_dict.safetensors
68	meta.json
69	layer_mask_report.csv
70	```
71	
72	where `pruned_state_dict.safetensors` stores the exported dense pruned weights, `meta.json` stores the pruning metadata required for loading, and `layer_mask_report.csv` records layer-wise retention statistics.
73	
74	## Evaluation
75	
76	### Perplexity
77	
78	```bash
79	python eval_pruned_ppl.py \
80	  --model-id meta-llama/Llama-2-7b-hf \
81	  --sd outputs/Llama-2-7b-hf_pruned_60/pruned_state_dict.safetensors \
82	  --meta outputs/Llama-2-7b-hf_pruned_60/meta.json \
83	  --device cuda:0
84	```
85	
86	For Qwen:
87	
88	```bash
89	python eval_pruned_ppl.py \
90	  --model-id Qwen/Qwen3-8B \
91	  --sd outputs/Qwen3-8B_pruned_80/pruned_state_dict.safetensors \
92	  --meta outputs/Qwen3-8B_pruned_80/meta.json \
93	  --trust-remote-code \
94	  --use-fast-tokenizer \
95	  --device cuda:0
96	```
97	
98	### Accuracy
99	
100	```bash
101	python eval_pruned_acc.py \
102	  --model-id meta-llama/Llama-2-7b-hf \
103	  --sd outputs/Llama-2-7b-hf_pruned_60/pruned_state_dict.safetensors \
104	  --meta outputs/Llama-2-7b-hf_pruned_60/meta.json \
105	  --device cuda:0
106	```
107	
108	Accuracy evaluation uses `lm-eval`.
109	
110	## C4 Evaluation
111	
112	C4 evaluation is optional. To enable it, prepare:
113	
114	```text
115	data/c4-validation.json
116	```
117	
118	WikiText-2 and PTB are loaded through Hugging Face `datasets`.
119	
120	## Citation
121	
122	If you find GRASPrune useful, please cite:
123	
124	```bibtex
125	@misc{wang2026grasprune,
126	      title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models}, 
127	      author={Ziyang Wang and Jiangfeng Xiao and Chuan Xiao and Ruoxiang Li and Rui Mao and Jianbin Qin},
128	      year={2026},
129	      eprint={2604.19398},
130	      archivePrefix={arXiv},
131	      primaryClass={cs.AI},
132	      url={https://arxiv.org/abs/2604.19398}, 
133	}
134	```
135	
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "f789c450-1fab-4fba-a614-a6bda9dbd41b",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/README.md",
      "content": "# GRASPrune\n\nOfficial implementation of **GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models**, accepted to **ACL 2026 Main Conference**.\n\n[[Paper]](https://arxiv.org/abs/2604.19398)\n\nGRASPrune is a post-training structured pruning toolkit for decoder-only LLMs. It learns global gates over FFN intermediate channels and attention KV groups, projects them into budget-feasible hard masks, applies lightweight rescale compensation, and exports a dense pruned checkpoint.\n\nThe code currently supports LLaMA-style and Qwen-style models, including `meta-llama/Llama-2-7b-hf` and `Qwen/Qwen3-8B`.\n\n## Installation\n\nPython 3.10 is recommended.\n\n```bash\npip install -r requirements.txt\n```\n\n## Pruning\n\nRun commands from the repository root.\n\n### LLaMA\n\n```bash\npython train.py \\\n  --model-id meta-llama/Llama-2-7b-hf \\\n  --model-family llama \\\n  --device cuda:0 \\\n  --keep-ratio 0.6 \\\n  --epochs 4 \\\n  --num-samples 512\n```\n\n### Qwen\n\n```bash\npython train.py \\\n  --model-id Qwen/Qwen3-8B \\\n  --model-family qwen \\\n  --trust-remote-code \\\n  --device cuda:0 \\\n  --keep-ratio 0.8 \\\n  --epochs 4 \\\n  --num-samples 512\n```\n\nIf the model is not cached locally, add:\n\n```bash\n--allow-remote-model\n```\n\nMain options:\n\n- `--keep-ratio`: retained structural budget.\n- `--epochs`: number of gate-training epochs.\n- `--num-samples`: number of calibration sequences.\n- `--max-len`: calibration sequence length.\n- `--output-dir`: custom output directory.\n\n## Outputs\n\nCheckpoints are saved under `outputs/` by default. Each output directory contains:\n\n```text\npruned_state_dict.safetensors\nmeta.json\nlayer_mask_report.csv\n```\n\nwhere `pruned_state_dict.safetensors` stores the exported dense pruned weights, `meta.json` stores the pruning metadata required for loading, and `layer_mask_report.csv` records layer-wise retention statistics.\n\n## Evaluation\n\n### Perplexity\n\n```bash\npython eval_pruned_ppl.py \\\n  --model-id meta-llama/Llama-2-7b-hf \\\n  --sd outputs/Llama-2-7b-hf_pruned_60/pruned_state_dict.safetensors \\\n  --meta outputs/Llama-2-7b-hf_pruned_60/meta.json \\\n  --device cuda:0\n```\n\nFor Qwen:\n\n```bash\npython eval_pruned_ppl.py \\\n  --model-id Qwen/Qwen3-8B \\\n  --sd outputs/Qwen3-8B_pruned_80/pruned_state_dict.safetensors \\\n  --meta outputs/Qwen3-8B_pruned_80/meta.json \\\n  --trust-remote-code \\\n  --use-fast-tokenizer \\\n  --device cuda:0\n```\n\n### Accuracy\n\n```bash\npython eval_pruned_acc.py \\\n  --model-id meta-llama/Llama-2-7b-hf \\\n  --sd outputs/Llama-2-7b-hf_pruned_60/pruned_state_dict.safetensors \\\n  --meta outputs/Llama-2-7b-hf_pruned_60/meta.json \\\n  --device cuda:0\n```\n\nAccuracy evaluation uses `lm-eval`.\n\n## C4 Evaluation\n\nC4 evaluation is optional. To enable it, prepare:\n\n```text\ndata/c4-validation.json\n```\n\nWikiText-2 and PTB are loaded through Hugging Face `datasets`.\n\n## Citation\n\nIf you find GRASPrune useful, please cite:\n\n```bibtex\n@misc{wang2026grasprune,\n      title={GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models}, \n      author={Ziyang Wang and Jiangfeng Xiao and Chuan Xiao and Ruoxiang Li and Rui Mao and Jianbin Qin},\n      year={2026},\n      eprint={2604.19398},\n      archivePrefix={arXiv},\n      primaryClass={cs.AI},\n      url={https://arxiv.org/abs/2604.19398}, \n}\n```\n",
      "numLines": 135,
      "startLine": 1,
      "totalLines": 135
    }
  }
}
````

</details>

---

### Tool call

_source line 57_

<details open><summary>🔧 Tool call — Read · `toolu_01AVuoU6BAXh365AfkAZvQzm`</summary>

```json
{
  "file_path": "/tmp/graspune_refs/GRASPrune/evals.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "5a5ec6be-365e-477f-b2e2-8dbbbba47a09",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LoqrBPYyruZdcZ28F43bVx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 30020,
      "cache_read_input_tokens": 31119,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 30020
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

_source line 58 · 2026-05-14T08:21:40.022Z_

<details><summary>↩ Tool result · `toolu_01AVuoU6BAXh365AfkAZvQzm`</summary>

```text
1	from __future__ import annotations
2	
3	import json
4	import logging
5	import os
6	from pathlib import Path
7	from typing import Any, Dict, Iterable
8	
9	import numpy as np
10	import torch
11	from datasets import load_dataset
12	from datasets.utils.logging import disable_progress_bar
13	from torch.utils.data import DataLoader, Dataset
14	from tqdm import tqdm
15	
16	os.environ.setdefault("HF_DATASETS_DISABLE_CACHING", "1")
17	os.environ.setdefault("HF_HUB_DISABLE_TELEMETRY", "1")
18	
19	DEFAULT_LM_EVAL_TASKS = ("piqa", "winogrande", "hellaswag", "arc_easy", "arc_challenge")
20	
21	
22	class EvalSequenceDataset(Dataset):
23	    def __init__(self, tensors: torch.Tensor):
24	        self.tensors = tensors
25	
26	    def __getitem__(self, index: int) -> torch.Tensor:
27	        return self.tensors[index]
28	
29	    def __len__(self) -> int:
30	        return len(self.tensors)
31	
32	
33	def load_local_c4_dataset():
34	    c4_path = Path(__file__).resolve().parent / "data" / "c4-validation.json"
35	    try:
36	        disable_progress_bar()
37	        return load_dataset("json", data_files=str(c4_path))["train"]
38	    except Exception as exc:
39	        raise FileNotFoundError(
40	            "C4 evaluation expects a local file named `data/c4-validation.json` "
41	            "in the GRASPrune root directory. Please download or prepare it manually."
42	        ) from exc
43	
44	
45	def build_eval_sequence_dataset(
46	    samples: Any,
47	    tokenizer: Any,
48	    seq_len: int,
49	    field_name: str,
50	) -> EvalSequenceDataset:
51	    test_ids = tokenizer("\n\n".join(samples[field_name]), return_tensors="pt").input_ids[0]
52	    num_samples = test_ids.numel() // seq_len
53	    batches = [test_ids[i * seq_len : (i + 1) * seq_len] for i in range(num_samples)]
54	    return EvalSequenceDataset(torch.stack(batches))
55	
56	
57	def build_eval_dataloader(name: str, tokenizer: Any, seq_len: int = 2048, batch_size: int = 8) -> DataLoader:
58	    if name == "wikitext2":
59	        test_data = load_dataset("wikitext", "wikitext-2-raw-v1", split="test")
60	        dataset = build_eval_sequence_dataset(test_data, tokenizer, seq_len, "text")
61	    elif name == "ptb":
62	        test_data = load_dataset("ptb_text_only", "penn_treebank", split="test")
63	        dataset = build_eval_sequence_dataset(test_data, tokenizer, seq_len, "sentence")
64	    elif name == "c4":
65	        test_data = load_local_c4_dataset()
66	        dataset = build_eval_sequence_dataset(test_data[:2000], tokenizer, seq_len, "text")
67	    else:
68	        raise ValueError(f"Unsupported evaluation dataset: {name}")
69	    return DataLoader(dataset, batch_size=batch_size, shuffle=False)
70	
71	
72	@torch.no_grad()
73	def evaluate_perplexity(
74	    model: Any,
75	    tokenizer: Any,
76	    datasets: Iterable[str] = ("wikitext2", "ptb", "c4"),
77	    model_seq_len: int = 2048,
78	    batch_size: int = 8,
79	    device: str = "cuda",
80	) -> Dict[str, float]:
81	    model.to(device)
82	    model.eval()
83	
84	    ppls: Dict[str, float] = {}
85	    for dataset in datasets:
86	        print(f"\n=== Evaluating {dataset} ===")
87	        test_loader = build_eval_dataloader(dataset, tokenizer, seq_len=model_seq_len, batch_size=batch_size)
88	        nlls = []
89	        for batch in tqdm(test_loader):
90	            batch = batch.to(device)
91	            output = model(batch, use_cache=False)
92	            logits = output.logits
93	            if not torch.isfinite(logits).all():
94	                continue
95	
96	            shift_logits = logits[:, :-1, :].contiguous()
97	            shift_labels = batch[:, 1:].contiguous()
98	            loss_fct = torch.nn.CrossEntropyLoss(reduction="none")
99	            loss = loss_fct(shift_logits.reshape(-1, shift_logits.size(-1)), shift_labels.view(-1))
100	            nlls.append(loss)
101	
102	        ppl = np.exp(torch.cat(nlls, dim=-1).mean().item())
103	        ppls[dataset] = float(ppl)
104	
105	    print(f"\nPPL results: {ppls}")
106	    if torch.cuda.is_available():
107	        print(f"Weight Memory: {torch.cuda.memory_allocated() / 1024 / 1024:.2f} MiB\n")
108	    return ppls
109	
110	
111	def evaluate_accuracy(model: Any, tokenizer: Any, device: str, batch_size: int = 8) -> dict[str, float]:
112	    try:
113	        import lm_eval
114	        from lm_eval import utils as lm_eval_utils
115	        from lm_eval.api.registry import ALL_TASKS
116	        from lm_eval.models.huggingface import HFLM
117	        from lm_eval.tasks import initialize_tasks
118	    except ImportError as exc:
119	        raise ImportError(
120	            "Accuracy evaluation requires `lm-eval` to be installed in the current environment. "
121	            "Please install dependencies from requirements.txt before running accuracy evaluation."
122	        ) from exc
123	
124	    model.to(device)
125	    initialize_tasks()
126	
127	    hflm = HFLM(pretrained=model, tokenizer=tokenizer, batch_size=batch_size)
128	    task_names = lm_eval_utils.pattern_match(list(DEFAULT_LM_EVAL_TASKS), ALL_TASKS)
129	    if not task_names:
130	        raise ValueError("No lm-eval tasks matched the default accuracy task list.")
131	
132	    logging.info("Selected lm-eval tasks: %s", task_names)
133	    results = lm_eval.simple_evaluate(
134	        model=hflm,
135	        tasks=task_names,
136	        num_fewshot=0,
137	        batch_size=batch_size,
138	    )["results"]
139	
140	    metric_vals = {
141	        task: round(float(result.get("acc_norm,none", result["acc,none"])), 4)
142	        for task, result in results.items()
143	    }
144	    metric_vals["avg_accuracy"] = round(sum(metric_vals.values()) / len(metric_vals), 4)
145	    logging.info("Accuracy metrics:\n%s", json.dumps(metric_vals, indent=2, ensure_ascii=False))
146	    return metric_vals
147	
148	
149	IndexDataset = EvalSequenceDataset
150	
151	
152	def _load_local_c4_json():
153	    return load_local_c4_dataset()
154	
155	
156	def _process_eval_data(samples: Any, tokenizer: Any, seq_len: int, field_name: str) -> EvalSequenceDataset:
157	    return build_eval_sequence_dataset(samples, tokenizer, seq_len, field_name)
158	
159	
160	def get_test_loader(name: str, tokenizer: Any, seq_len: int = 2048, batch_size: int = 8) -> DataLoader:
161	    return build_eval_dataloader(name, tokenizer, seq_len=seq_len, batch_size=batch_size)
162	
163	
164	def ppl_eval(
165	    model: Any,
166	    tokenizer: Any,
167	    datasets: Iterable[str] = ("wikitext2", "ptb", "c4"),
168	    model_seq_len: int = 2048,
169	    batch_size: int = 8,
170	    device: str = "cuda",
171	) -> Dict[str, float]:
172	    return evaluate_perplexity(
173	        model,
174	        tokenizer,
175	        datasets=datasets,
176	        model_seq_len=model_seq_len,
177	        batch_size=batch_size,
178	        device=device,
179	    )
180	
181	
182	def acc_eval(model: Any, tokenizer: Any, device: str, batch_size: int = 8) -> dict[str, float]:
183	    return evaluate_accuracy(model, tokenizer, device=device, batch_size=batch_size)
184	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "1983e3af-5e96-41d6-9406-81983172a4f1",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/graspune_refs/GRASPrune/evals.py",
      "content": "from __future__ import annotations\n\nimport json\nimport logging\nimport os\nfrom pathlib import Path\nfrom typing import Any, Dict, Iterable\n\nimport numpy as np\nimport torch\nfrom datasets import load_dataset\nfrom datasets.utils.logging import disable_progress_bar\nfrom torch.utils.data import DataLoader, Dataset\nfrom tqdm import tqdm\n\nos.environ.setdefault(\"HF_DATASETS_DISABLE_CACHING\", \"1\")\nos.environ.setdefault(\"HF_HUB_DISABLE_TELEMETRY\", \"1\")\n\nDEFAULT_LM_EVAL_TASKS = (\"piqa\", \"winogrande\", \"hellaswag\", \"arc_easy\", \"arc_challenge\")\n\n\nclass EvalSequenceDataset(Dataset):\n    def __init__(self, tensors: torch.Tensor):\n        self.tensors = tensors\n\n    def __getitem__(self, index: int) -> torch.Tensor:\n        return self.tensors[index]\n\n    def __len__(self) -> int:\n        return len(self.tensors)\n\n\ndef load_local_c4_dataset():\n    c4_path = Path(__file__).resolve().parent / \"data\" / \"c4-validation.json\"\n    try:\n        disable_progress_bar()\n        return load_dataset(\"json\", data_files=str(c4_path))[\"train\"]\n    except Exception as exc:\n        raise FileNotFoundError(\n            \"C4 evaluation expects a local file named `data/c4-validation.json` \"\n            \"in the GRASPrune root directory. Please download or prepare it manually.\"\n        ) from exc\n\n\ndef build_eval_sequence_dataset(\n    samples: Any,\n    tokenizer: Any,\n    seq_len: int,\n    field_name: str,\n) -> EvalSequenceDataset:\n    test_ids = tokenizer(\"\\n\\n\".join(samples[field_name]), return_tensors=\"pt\").input_ids[0]\n    num_samples = test_ids.numel() // seq_len\n    batches = [test_ids[i * seq_len : (i + 1) * seq_len] for i in range(num_samples)]\n    return EvalSequenceDataset(torch.stack(batches))\n\n\ndef build_eval_dataloader(name: str, tokenizer: Any, seq_len: int = 2048, batch_size: int = 8) -> DataLoader:\n    if name == \"wikitext2\":\n        test_data = load_dataset(\"wikitext\", \"wikitext-2-raw-v1\", split=\"test\")\n        dataset = build_eval_sequence_dataset(test_data, tokenizer, seq_len, \"text\")\n    elif name == \"ptb\":\n        test_data = load_dataset(\"ptb_text_only\", \"penn_treebank\", split=\"test\")\n        dataset = build_eval_sequence_dataset(test_data, tokenizer, seq_len, \"sentence\")\n    elif name == \"c4\":\n        test_data = load_local_c4_dataset()\n        dataset = build_eval_sequence_dataset(test_data[:2000], tokenizer, seq_len, \"text\")\n    else:\n        raise ValueError(f\"Unsupported evaluation dataset: {name}\")\n    return DataLoader(dataset, batch_size=batch_size, shuffle=False)\n\n\n@torch.no_grad()\ndef evaluate_perplexity(\n    model: Any,\n    tokenizer: Any,\n    datasets: Iterable[str] = (\"wikitext2\", \"ptb\", \"c4\"),\n    model_seq_len: int = 2048,\n    batch_size: int = 8,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    model.to(device)\n    model.eval()\n\n    ppls: Dict[str, float] = {}\n    for dataset in datasets:\n        print(f\"\\n=== Evaluating {dataset} ===\")\n        test_loader = build_eval_dataloader(dataset, tokenizer, seq_len=model_seq_len, batch_size=batch_size)\n        nlls = []\n        for batch in tqdm(test_loader):\n            batch = batch.to(device)\n            output = model(batch, use_cache=False)\n            logits = output.logits\n            if not torch.isfinite(logits).all():\n                continue\n\n            shift_logits = logits[:, :-1, :].contiguous()\n            shift_labels = batch[:, 1:].contiguous()\n            loss_fct = torch.nn.CrossEntropyLoss(reduction=\"none\")\n            loss = loss_fct(shift_logits.reshape(-1, shift_logits.size(-1)), shift_labels.view(-1))\n            nlls.append(loss)\n\n        ppl = np.exp(torch.cat(nlls, dim=-1).mean().item())\n        ppls[dataset] = float(ppl)\n\n    print(f\"\\nPPL results: {ppls}\")\n    if torch.cuda.is_available():\n        print(f\"Weight Memory: {torch.cuda.memory_allocated() / 1024 / 1024:.2f} MiB\\n\")\n    return ppls\n\n\ndef evaluate_accuracy(model: Any, tokenizer: Any, device: str, batch_size: int = 8) -> dict[str, float]:\n    try:\n        import lm_eval\n        from lm_eval import utils as lm_eval_utils\n        from lm_eval.api.registry import ALL_TASKS\n        from lm_eval.models.huggingface import HFLM\n        from lm_eval.tasks import initialize_tasks\n    except ImportError as exc:\n        raise ImportError(\n            \"Accuracy evaluation requires `lm-eval` to be installed in the current environment. \"\n            \"Please install dependencies from requirements.txt before running accuracy evaluation.\"\n        ) from exc\n\n    model.to(device)\n    initialize_tasks()\n\n    hflm = HFLM(pretrained=model, tokenizer=tokenizer, batch_size=batch_size)\n    task_names = lm_eval_utils.pattern_match(list(DEFAULT_LM_EVAL_TASKS), ALL_TASKS)\n    if not task_names:\n        raise ValueError(\"No lm-eval tasks matched the default accuracy task list.\")\n\n    logging.info(\"Selected lm-eval tasks: %s\", task_names)\n    results = lm_eval.simple_evaluate(\n        model=hflm,\n        tasks=task_names,\n        num_fewshot=0,\n        batch_size=batch_size,\n    )[\"results\"]\n\n    metric_vals = {\n        task: round(float(result.get(\"acc_norm,none\", result[\"acc,none\"])), 4)\n        for task, result in results.items()\n    }\n    metric_vals[\"avg_accuracy\"] = round(sum(metric_vals.values()) / len(metric_vals), 4)\n    logging.info(\"Accuracy metrics:\\n%s\", json.dumps(metric_vals, indent=2, ensure_ascii=False))\n    return metric_vals\n\n\nIndexDataset = EvalSequenceDataset\n\n\ndef _load_local_c4_json():\n    return load_local_c4_dataset()\n\n\ndef _process_eval_data(samples: Any, tokenizer: Any, seq_len: int, field_name: str) -> EvalSequenceDataset:\n    return build_eval_sequence_dataset(samples, tokenizer, seq_len, field_name)\n\n\ndef get_test_loader(name: str, tokenizer: Any, seq_len: int = 2048, batch_size: int = 8) -> DataLoader:\n    return build_eval_dataloader(name, tokenizer, seq_len=seq_len, batch_size=batch_size)\n\n\ndef ppl_eval(\n    model: Any,\n    tokenizer: Any,\n    datasets: Iterable[str] = (\"wikitext2\", \"ptb\", \"c4\"),\n    model_seq_len: int = 2048,\n    batch_size: int = 8,\n    device: str = \"cuda\",\n) -> Dict[str, float]:\n    return evaluate_perplexity(\n        model,\n        tokenizer,\n        datasets=datasets,\n        model_seq_len=model_seq_len,\n        batch_size=batch_size,\n        device=device,\n    )\n\n\ndef acc_eval(model: Any, tokenizer: Any, device: str, batch_size: int = 8) -> dict[str, float]:\n    return evaluate_accuracy(model, tokenizer, device=device, batch_size=batch_size)\n",
      "numLines": 184,
      "startLine": 1,
      "totalLines": 184
    }
  }
}
```

</details>

---

### Assistant

_source line 59_

<details><summary>Logged reasoning block</summary>

```text
Now I have a thorough understanding of both:

1. **GRASPrune (ACL 2026)** - the official structured pruning method for LLMs
2. **Our project's existing code** - standard importance + RASP pruning

Let me now fetch the arXiv paper HTML for the mathematical details, and also look at the original GraSP paper to understand the naming distinction.

Actually, I have enough information now to write a comprehensive report. Let me summarize what I know:

### GRASPrune (ACL 2026) - Key Algorithm Details

From the code analysis:


The core approach injects learnable gate parameters into the model—scalar gates for each FFN channel and each KV head group—then trains these gates under a budget constraint to identify which components are most important to keep. For Llama models, the gates are implemented as direct parameters on the gate modules, while Qwen uses a hook-based approach for attention gating.

During training, I compute soft probabilities from the gate scores using a temperature-scaled sigmoid, then project them globally by ranking all gates and greedily selecting the top ones until the budget is exhausted. The forward pass uses hard binary masks for efficiency, but the backward pass flows gradients through the soft probabilities via a straight-through estimator. The cost model treats FFN units uniformly while accounting for the actual computational cost of attention groups based on their size and head dimension, with the total budget derived from the model's cost multiplied by the desired keep ratio.

Building the budget mask... Finishing the materialization step by removing the pruned projections and exporting the final checkpoint. Then I'm noting that GRASPrune targets KV head granularity with hook-based gating, which aligns perfectly with GQA structure, while our current one-shot approach uses Taylor expansion importance scores that RASP further refines by factoring in CKA overlap to penalize redundant heads.

For our DeepSeek model, the MLP grouping creates uneven splits since we're dividing 18944 intermediate dimensions by 28 heads, but GRASPrune handles this through iterative gate training with budget constraints over a few epochs, applying projected STE for differentiable enforcement and then rescaling to compensate. The simplest path forward is to run GRASPrune directly on the Qwen architecture since it already supports it. -ratio 0.65`
- Export produces dense checkpoint compatible with `load_pruned_model()`

**Option B: Implement GRASPrune-style scoring in our framework**
- Extract the learned gate scores after training
- Use them as a replacement for our Taylor importance scores
- Still use our pruning execution code

For a fair baseline comparison, Option A is cleaner — run GRASPrune as its own pipeline, get the pruned model, then continue with our GRPO recovery pipeline.

### Adaptation plan for our codebase:

The key consideration is that our pipeline is:
1. Compute importance → 2. (Optionally compute CKA) → 3. Prune → 4. GRPO recovery → 5. Eval

For GRASPrune as baseline:
1. Run GRASPrune pipeline (gate training + rescale) → 2. Export pruned model → 3. GRPO recovery → 4. Eval

The integration point is after step 2/3 — we need the pruned model in a format that our GRPO training can consume. GRASPrune exports the materialized dense weights and per-layer dimensions, which our existing `load_pruned_model()` function in `rebuild.py` already expects. Since GRASPrune has its own `rebuild.py` with the same interface, the integration is straightforward: install GRASPrune as a dependency, run its pipeline on our model, then feed the output directly into our GRPO recovery stage.

Now I'm checking the GQA group constraint — DeepSeek-R1-Distill-Qwen-7B has 28 query heads and 4 key-value heads, so each KV group contains 7 query heads. GRASPrune's attention gating operates at the KV group level, which aligns perfectly with our constraint, while its MLP gating is at the individual channel level, which is actually finer-grained and better for structured pruning than our group-level approach. I should write up the report now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "fb139239-f162-471f-8a9f-1d169df58a17",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eQxUw2HY9xmawQhibqGz4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11055,
      "cache_read_input_tokens": 61139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11055
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

_source line 60_

All code and paper details collected. Let me now also fetch the arXiv paper for mathematical formulation details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "02bbec25-5fb7-4951-89ac-cb14d0b5e0eb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eQxUw2HY9xmawQhibqGz4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11055,
      "cache_read_input_tokens": 61139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11055
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

_source line 61_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01J211JgQJPbsia2efMVgnZt`</summary>

```json
{
  "query": "arxiv.org 2604.19398 GRASPrune method formulation projected straight-through estimator budget constraint loss function"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "2c4ec647-11fe-400e-9571-df3ca7a453c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016eQxUw2HY9xmawQhibqGz4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 11055,
      "cache_read_input_tokens": 61139,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11055
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

_source line 62 · 2026-05-14T08:22:32.833Z_

<details><summary>↩ Tool result · `toolu_01J211JgQJPbsia2efMVgnZt`</summary>

```text
Web search results for query: "arxiv.org 2604.19398 GRASPrune method formulation projected straight-through estimator budget constraint loss function"

Links: [{"title":"[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/abs/2604.19398"},{"title":"GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models","url":"https://arxiv.org/html/2604.19398"},{"title":"GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub","url":"https://github.com/ZiY-Wang/GRASPrune"},{"title":"Arxiv","url":"https://arxiv.org/pdf/2502.19398"},{"title":"[2604.26216] Unsupervised Graph Modeling for Anomaly Detection in Accounting Subject Relationships","url":"https://arxiv.org/abs/2604.26216"},{"title":"Localization with Hopping Disorder in Quasi-periodic Synthetic Momentum Lattice","url":"https://arxiv.org/html/2604.11855"},{"title":"[2604.27781] The Grand Software Supply Chain of AI Systems","url":"https://arxiv.org/abs/2604.27781"},{"title":"arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals","url":"https://scispace.com/journals/arxiv-org-bl5k1ptr"},{"title":"[2604.02760] AI Disclosure with DAISY","url":"https://arxiv.org/abs/2604.02760"},{"title":"General Relativity and Quantum Cosmology","url":"https://arxiv.org/list/gr-qc/new"}]

Based on the search results for arxiv.org paper 2604.19398, here's information about the GRASPrune method's formulation:

## GRASPrune Method Overview

GRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget.

## Method Formulation with Projected Straight-Through Estimator

GRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step while keeping the backbone weights frozen. This is a key distinction from traditional approaches, as instead of learning importance scores without constraints and applying the budget only after training, GRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step.

## Budget Constraint Loss Function

The method incorporates a single global budget constraint through its optimization process. GRASPrune is a structured pruning framework with a single resource budget, where the backbone weights remain frozen and only a small set of scalar gates on a small unlabeled calibration set are optimized.

## Post-Pruning Calibration

After the mask is fixed, scaling factors on the retained units are calibrated to mitigate scale mismatch caused by pruning, and these factors are folded into the pruned weights to obtain a smaller dense checkpoint with no extra parameters at inference.

For more detailed technical information about the loss function formulation, I recommend consulting the full paper PDF available at arxiv.org/abs/2604.19398.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "840bc341-7c09-42f5-b2b2-8e522b20d9d4",
  "tool_use_result": {
    "query": "arxiv.org 2604.19398 GRASPrune method formulation projected straight-through estimator budget constraint loss function",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Eb8tQAZMbEtqs3H17UZUW8",
        "content": [
          {
            "title": "[2604.19398] GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/abs/2604.19398"
          },
          {
            "title": "GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models",
            "url": "https://arxiv.org/html/2604.19398"
          },
          {
            "title": "GitHub - ZiY-Wang/GRASPrune: Official implementation of GRASPrune, ACL 2026 Main: global gating for budgeted structured pruning of LLMs. · GitHub",
            "url": "https://github.com/ZiY-Wang/GRASPrune"
          },
          {
            "title": "Arxiv",
            "url": "https://arxiv.org/pdf/2502.19398"
          },
          {
            "title": "[2604.26216] Unsupervised Graph Modeling for Anomaly Detection in Accounting Subject Relationships",
            "url": "https://arxiv.org/abs/2604.26216"
          },
          {
            "title": "Localization with Hopping Disorder in Quasi-periodic Synthetic Momentum Lattice",
            "url": "https://arxiv.org/html/2604.11855"
          },
          {
            "title": "[2604.27781] The Grand Software Supply Chain of AI Systems",
            "url": "https://arxiv.org/abs/2604.27781"
          },
          {
            "title": "arXiv.org | 232753 Publications | 16958 Citations | Top authors | Related journals",
            "url": "https://scispace.com/journals/arxiv-org-bl5k1ptr"
          },
          {
            "title": "[2604.02760] AI Disclosure with DAISY",
            "url": "https://arxiv.org/abs/2604.02760"
          },
          {
            "title": "General Relativity and Quantum Cosmology",
            "url": "https://arxiv.org/list/gr-qc/new"
          }
        ]
      },
      "Based on the search results for arxiv.org paper 2604.19398, here's information about the GRASPrune method's formulation:\n\n## GRASPrune Method Overview\n\nGRASPrune is a structured pruning framework applied after pretraining that jointly prunes FFN channels and KV head groups under a single global budget.\n\n## Method Formulation with Projected Straight-Through Estimator\n\nGRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step while keeping the backbone weights frozen. This is a key distinction from traditional approaches, as instead of learning importance scores without constraints and applying the budget only after training, GRASPrune learns lightweight gate scores with a projected straight-through estimator that enforces a hard mask satisfying the budget at every step.\n\n## Budget Constraint Loss Function\n\nThe method incorporates a single global budget constraint through its optimization process. GRASPrune is a structured pruning framework with a single resource budget, where the backbone weights remain frozen and only a small set of scalar gates on a small unlabeled calibration set are optimized.\n\n## Post-Pruning Calibration\n\nAfter the mask is fixed, scaling factors on the retained units are calibrated to mitigate scale mismatch caused by pruning, and these factors are folded into the pruned weights to obtain a smaller dense checkpoint with no extra parameters at inference.\n\nFor more detailed technical information about the loss function formulation, I recommend consulting the full paper PDF available at arxiv.org/abs/2604.19398."
    ],
    "durationSeconds": 7.065147989999998
  }
}
```

</details>

---

### Assistant

_source line 63_

<details><summary>Logged reasoning block</summary>

```text
Let me try to fetch the actual paper HTML to get the mathematical formulations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "8851932a-ba45-4141-be61-ef59c4ffb073",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JmUbN8pMRrekhMMcgKhVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 72194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 64_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01RpkuYX7hJRBR7ujHU6av88`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "892543a7-9c23-4ea8-954a-87dc47532cef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012JmUbN8pMRrekhMMcgKhVN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2753,
      "cache_read_input_tokens": 72194,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2753
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

_source line 65 · 2026-05-14T08:22:36.485Z_

<details><summary>↩ Tool result · `toolu_01RpkuYX7hJRBR7ujHU6av88`</summary>

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
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "6ac5a722-0918-4f5a-8c68-7d48f6603046",
  "tool_use_result": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 66_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AGsqAf7qpd5JqzZUK2f9Sd`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.19398",
  "prompt": "Extract ALL mathematical formulations from this paper, including:\n1. The gate scoring function and how gates are parameterized\n2. The projected straight-through estimator (PSTE) formulation\n3. The budget constraint formulation (how cost is computed for FFN and attention)\n4. The loss function used during gate training\n5. The rescale compensation formulation\n6. The hard mask projection algorithm (how budget-feasible masks are obtained from soft scores)\n7. Any equations related to the pruning criterion\n\nGive me the exact mathematical notation used in the paper. Also extract the algorithm pseudocode if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "5f69812f-716f-4279-a1d5-4414d177d864",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kucTQ5bb66UMyhqwVEP2F",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 626,
      "cache_read_input_tokens": 74947,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 626
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

_source line 67 · 2026-05-14T08:22:53.359Z_

<details><summary>↩ Tool result · `toolu_01AGsqAf7qpd5JqzZUK2f9Sd`</summary>

````text
# Mathematical Formulations from GRASPrune Paper

## 1. Budget-Constrained Optimization Problem

The core formulation treats structured pruning as:

```
min_{z ∈ {0,1}^|S|} L(θ; z)  s.t.  Σ_{i∈S} c_i z_i ≤ B
```

Where z_i ∈ {0,1} indicates unit retention, c_i represents unit cost, and B = ρ Σ_{i∈S} c_i is the global budget with target keep ratio ρ.

## 2. Cost Model

FFN channels have unit cost c_i = 1, while KV head groups have cost:

```
α = (2G + 2)d_h / 3
```

Where G = H/H^kv (query-to-KV head ratio) and d_h is head dimension.

## 3. Hard Forward, Soft Backward (STE)

The surrogate gate formulation is:

```
z̃_i = m_i + (p_i - stopgrad(p_i))
```

Where m_i is the hard mask and p_i represents soft probabilities. The gradient with respect to gate scores s_i becomes:

```
∂L/∂s_i = (1/τ)(∂L/∂z̃_i) p_i(1-p_i)
```

This represents standard Bernoulli STE with temperature τ = 1.5.

## 4. Hard Mask Projection

The `Project(p, c, B)` function performs budget-feasible selection by:
- Sorting units by p_i in descending order
- Setting m_i = 1 until adding the next unit would exceed budget B
- Using cost only for feasibility enforcement, not ranking

## 5. Hard-Mask Objective

The objective being optimized via STE is:

```
L̃(s) = E_x[L(f(x; θ, m̂(p(s))))]
```

Where m̂(p) denotes the hard mask returned by the projection operator.

## 6. Scaling Calibration

Post-pruning, multiplicative scalars {γ_i}_{i∈I} are learned on retained units I = {i | m_i = 1}, then folded into sliced weights as diagonal reweighting without adding inference overhead.

## Key Implementation Details

- **Gate initialization**: All scores s_i initialized to zero
- **Optimizer**: AdamW with learning rate 1×10^-2
- **Training**: 4 epochs on 512 sequences of length 512
- **Computational cost**: Projection is O(n log n) but accounts for only 0.11-0.14% of total gate-learning time

The paper does not provide explicit pseudocode but describes the projection as "one global sort and one linear scan" per training step.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "1f9b5fa0-bd8f-449d-920c-5dd1cbc4e978",
  "tool_use_result": {
    "bytes": 391056,
    "code": 200,
    "codeText": "OK",
    "result": "# Mathematical Formulations from GRASPrune Paper\n\n## 1. Budget-Constrained Optimization Problem\n\nThe core formulation treats structured pruning as:\n\n```\nmin_{z ∈ {0,1}^|S|} L(θ; z)  s.t.  Σ_{i∈S} c_i z_i ≤ B\n```\n\nWhere z_i ∈ {0,1} indicates unit retention, c_i represents unit cost, and B = ρ Σ_{i∈S} c_i is the global budget with target keep ratio ρ.\n\n## 2. Cost Model\n\nFFN channels have unit cost c_i = 1, while KV head groups have cost:\n\n```\nα = (2G + 2)d_h / 3\n```\n\nWhere G = H/H^kv (query-to-KV head ratio) and d_h is head dimension.\n\n## 3. Hard Forward, Soft Backward (STE)\n\nThe surrogate gate formulation is:\n\n```\nz̃_i = m_i + (p_i - stopgrad(p_i))\n```\n\nWhere m_i is the hard mask and p_i represents soft probabilities. The gradient with respect to gate scores s_i becomes:\n\n```\n∂L/∂s_i = (1/τ)(∂L/∂z̃_i) p_i(1-p_i)\n```\n\nThis represents standard Bernoulli STE with temperature τ = 1.5.\n\n## 4. Hard Mask Projection\n\nThe `Project(p, c, B)` function performs budget-feasible selection by:\n- Sorting units by p_i in descending order\n- Setting m_i = 1 until adding the next unit would exceed budget B\n- Using cost only for feasibility enforcement, not ranking\n\n## 5. Hard-Mask Objective\n\nThe objective being optimized via STE is:\n\n```\nL̃(s) = E_x[L(f(x; θ, m̂(p(s))))]\n```\n\nWhere m̂(p) denotes the hard mask returned by the projection operator.\n\n## 6. Scaling Calibration\n\nPost-pruning, multiplicative scalars {γ_i}_{i∈I} are learned on retained units I = {i | m_i = 1}, then folded into sliced weights as diagonal reweighting without adding inference overhead.\n\n## Key Implementation Details\n\n- **Gate initialization**: All scores s_i initialized to zero\n- **Optimizer**: AdamW with learning rate 1×10^-2\n- **Training**: 4 epochs on 512 sequences of length 512\n- **Computational cost**: Projection is O(n log n) but accounts for only 0.11-0.14% of total gate-learning time\n\nThe paper does not provide explicit pseudocode but describes the projection as \"one global sort and one linear scan\" per training step.",
    "durationMs": 10486,
    "url": "https://arxiv.org/html/2604.19398"
  }
}
````

</details>

---

### Assistant

_source line 68_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write a comprehensive report. Let me also check what the original GraSP (2020) paper's formulation is, since the user mentioned "GRASPrune" which is specifically the ACL 2026 paper, not the 2020 GraSP. Let me confirm this distinction is clear.

Actually, the user specifically said "GRASPrune" and their context says "GRASPrune 作为额外 baseline pruning method". The ACL 2026 GRASPrune is the right one — it's a structured pruning method for LLMs, which is exactly what we need. 

The 2020 GraSP is a different approach focused on unstructured pruning at initialization, so I'll make sure that distinction is clear in the report. Now let me compile everything into a comprehensive document.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "6d2e9730-9ec6-4592-ad46-dcd8c80c6153",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmwesR8QR6dVE1upfnK4DN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 69_

All information collected. Now writing the comprehensive report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "2f0eaf5e-7f28-4bef-93b1-e758735ce417",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmwesR8QR6dVE1upfnK4DN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 70_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01KPcbkkmEFHhsUpZjG4UkEp`</summary>

````json
{
  "project": "recovery_aware_struct_prune",
  "file": "memory.md",
  "content": "# GRASPrune 调研报告 — Phase 2 P1 Baseline 实现方案\n\n> 调研日期: 2026-05-14\n> 目标: 将 GRASPrune 作为 Phase 2 P1 的额外 baseline pruning method\n\n---\n\n## 1. GRASPrune 概述\n\n**论文**: GRASPrune: Global Gating for Budgeted Structured Pruning of Large Language Models\n**会议**: ACL 2026 Main Conference\n**arXiv**: 2604.19398\n**代码**: https://github.com/ZiY-Wang/GRASPrune\n**作者**: Ziyang Wang, Jiangfeng Xiao, Chuan Xiao, Ruoxiang Li, Rui Mao, Jianbin Qin\n\nGRASPrune 是一个 post-training structured pruning 框架，对 decoder-only LLM 做 FFN channel 和 attention KV group 的联合剪枝。核心特点：\n- **Global gating**: 所有层的 FFN channel 和 KV group 共享一个全局 budget\n- **Projected STE**: 每个 training step 都投影到 budget-feasible 的 hard mask\n- **Rescale compensation**: 剪枝后学习 scaling factor 补偿 scale mismatch\n- 支持 LLaMA 和 **Qwen** 架构（直接兼容我们的 DeepSeek-R1-Distill-Qwen-7B）\n\n---\n\n## 2. 核心算法\n\n### 2.1 问题形式化\n\n将 structured pruning 建模为 budget-constrained binary optimization:\n\n$$\\min_{z \\in \\{0,1\\}^{|S|}} \\mathcal{L}(\\theta; z) \\quad \\text{s.t.} \\quad \\sum_{i \\in S} c_i z_i \\leq B$$\n\n其中:\n- $S$ = 所有可剪枝 structural unit 的集合（FFN channels + KV groups across all layers）\n- $z_i \\in \\{0,1\\}$: unit $i$ 的保留标志\n- $c_i$: unit $i$ 的参数代价\n- $B = \\rho \\sum_{i \\in S} c_i$: 全局 budget，$\\rho$ = keep_ratio\n\n### 2.2 代价模型 (Cost Model)\n\n**FFN channel**: $c_i = 1$（归一化单位代价）\n\n**KV group (attention)**: \n$$\\alpha = \\frac{(2G + 2) d_h}{3}$$\n\n其中 $G = H / H^{kv}$（query-to-KV head ratio），$d_h$ = head_dim。\n\n对于 DeepSeek-R1-Distill-Qwen-7B:\n- $H = 28$, $H^{kv} = 4$, $G = 7$, $d_h = 128$\n- $\\alpha = (2 \\times 7 + 2) \\times 128 / 3 = 16 \\times 128 / 3 \\approx 682.67$\n\n### 2.3 Gate Parameterization\n\n为每个 structural unit 引入可学习 scalar gate $s_i$：\n- **FFN**: `gate_score` — shape `(intermediate_size,)` = `(18944,)` per layer\n- **KV group**: `gate_score_kv` — shape `(num_key_value_heads,)` = `(4,)` per layer\n\nSoft probability: $p_i = \\sigma(s_i / \\tau)$，其中 $\\tau = 1.5$ 为 temperature。\n\n### 2.4 Projected Straight-Through Estimator (PSTE)\n\n**Forward pass** (hard mask):\n1. 收集所有 gate 的 soft probabilities $\\{p_i\\}$\n2. Budget projection `Project(p, c, B)`:\n   - 按 $p_i$ 降序排列\n   - 贪心选择 $m_i = 1$ 直到 $\\sum c_i m_i \\leq B$\n   - 复杂度: $O(n \\log n)$ 排序 + $O(n)$ 扫描\n3. 得到 hard mask $\\hat{m}$\n\n**STE trick** (soft backward):\n$$\\tilde{z}_i = m_i + (p_i - \\text{stopgrad}(p_i))$$\n\nForward 用 hard mask $m_i \\in \\{0,1\\}$，backward 梯度穿过 soft $p_i$:\n$$\\frac{\\partial \\mathcal{L}}{\\partial s_i} = \\frac{1}{\\tau} \\frac{\\partial \\mathcal{L}}{\\partial \\tilde{z}_i} p_i(1 - p_i)$$\n\n**Training objective**:\n$$\\tilde{\\mathcal{L}}(s) = \\mathbb{E}_x[\\mathcal{L}(f(x; \\theta, \\hat{m}(p(s))))]$$\n\n其中 $\\theta$ 冻结，只优化 gate scores $\\{s_i\\}$。\n\n### 2.5 Rescale Compensation (Stage B)\n\nHard mask 固定后，对保留 unit 学习 multiplicative scaling:\n$$\\text{output}_i = m_i \\cdot (1 + \\alpha_r \\cdot \\tanh(s_i)) \\cdot \\text{activation}_i$$\n\n其中 $\\alpha_r = 0.5$（rescale_alpha）。学习完成后，scaling factor 折叠进 weight matrix，推理时无额外开销。\n\n### 2.6 算法伪代码\n\n```\nAlgorithm: GRASPrune Pipeline\n\nInput: pretrained model θ, keep_ratio ρ, calibration data D\nOutput: pruned dense checkpoint\n\n# Stage A: Gate Training\n1. Attach gate scores {s_i} to all FFN channels and KV groups, init s_i = 0\n2. Freeze all backbone weights θ\n3. Compute cost vector c (FFN: 1.0, KV group: α)\n4. Budget B = ρ * Σ c_i\n5. For epoch = 1..4:\n     For batch x in D:\n       p_i = sigmoid(s_i / τ)  for all i\n       m = Project(p, c, B)    # greedy top-k by probability\n       z̃_i = m_i + (p_i - stopgrad(p_i))  # STE\n       Apply z̃ as mask to FFN channels and KV groups\n       loss = CrossEntropyLoss(model(x; θ, z̃), x)\n       Backprop through z̃ → update {s_i} via AdamW\n\n# Finalize Hard Masks\n6. Compute final p_i, run Project → get final hard masks\n7. Register masks on all gate modules\n\n# Stage B: Rescale Compensation\n8. Zero gate scores, enable rescale mode\n9. For epoch = 1..1:\n     For batch x in D_val:\n       Apply mask with rescale: output_i = m_i * (1 + 0.5 * tanh(s_i)) * act_i\n       loss = CrossEntropyLoss(model(x), x)\n       Backprop → update {s_i}\n\n# Export\n10. Materialize pruning: physically remove pruned dimensions from weight matrices\n11. Fold rescale factors into weights\n12. Export pruned_state_dict.safetensors + meta.json\n```\n\n---\n\n## 3. 与现有方法的对比\n\n| 特性 | Standard (我们的) | RASP (我们的) | GRASPrune (baseline) |\n|------|-------------------|---------------|---------------------|\n| Scoring | Taylor: $I(h) = \\|w_h \\cdot g_h\\|_2$ | $S(h) = I(h) \\cdot (1-F(h))^\\alpha$ | Learned gates via PSTE |\n| 优化方式 | One-shot (无迭代) | One-shot (无迭代) | 迭代 gate training (4 epochs) |\n| Budget 约束 | 事后贪心裁剪 | 事后贪心裁剪 | 每步投影到 feasible set |\n| Attn 粒度 | Q head → 推导 KV | Q head → 推导 KV | **直接 KV group** |\n| MLP 粒度 | n_heads 个 group | n_heads 个 group | **Per-channel** |\n| 补偿 | 无 | 无 | Rescale compensation |\n| 校准数据 | GSM8K train | GSM8K train | WikiText2 train |\n| 耗时 | ~10 min (importance) | ~30 min (importance+CKA) | ~6 min (A100 80G) |\n\n### 关键区别:\n1. **GRASPrune 的 attention pruning 天然在 KV group 粒度**，`gate_score_kv` shape = `(num_key_value_heads,)`。这完美满足我们的 GQA group 硬约束。\n2. **MLP pruning 更细粒度**: per-channel 而非 per-group，理论上更优但也更多参数要学。\n3. **有 rescale 补偿**: 这给 GRASPrune 额外优势，公平起见实验中可能需要注意。\n\n---\n\n## 4. 集成方案\n\n### 4.1 推荐方案: 直接使用 GRASPrune 官方代码\n\nGRASPrune 已原生支持 Qwen 架构，输出格式 (safetensors + meta.json) 与我们的 `load_pruned_model()` 完全兼容。\n\n**Pipeline**:\n```\nGRASPrune(DeepSeek-R1-Distill-Qwen-7B, keep_ratio=0.65)\n    → pruned_state_dict.safetensors + meta.json\n    → load_pruned_model()  # 用我们的 rebuild.py\n    → GRPO recovery training\n    → eval (GSM8K)\n```\n\n**服务器部署步骤**:\n```bash\n# 1. Clone GRASPrune 到服务器\ncd /root\ngit clone https://github.com/ZiY-Wang/GRASPrune.git\ncd GRASPrune\npip install -r requirements.txt\n\n# 2. 运行 GRASPrune pruning (keep_ratio=0.65 ↔ 35% sparsity)\npython train.py \\\n  --model-id /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B \\\n  --model-family qwen \\\n  --trust-remote-code \\\n  --device cuda:0 \\\n  --keep-ratio 0.65 \\\n  --epochs 4 \\\n  --num-samples 512 \\\n  --max-len 512 \\\n  --batch-size 1 \\\n  --output-dir /root/recovery_aware_struct_prune/outputs/graspune_qwen7b_65\n\n# 3. 验证 pruned model\npython eval_pruned_ppl.py \\\n  --model-id /root/autodl-tmp/models/DeepSeek-R1-Distill-Qwen-7B \\\n  --sd /root/recovery_aware_struct_prune/outputs/graspune_qwen7b_65/pruned_state_dict.safetensors \\\n  --meta /root/recovery_aware_struct_prune/outputs/graspune_qwen7b_65/meta.json \\\n  --trust-remote-code \\\n  --use-fast-tokenizer \\\n  --device cuda:0\n\n# 4. 接入我们的 GRPO recovery pipeline\ncd /root/recovery_aware_struct_prune\npython src/train_grpo.py \\\n  --pruned_model_path /root/recovery_aware_struct_prune/outputs/graspune_qwen7b_65 \\\n  ...\n```\n\n### 4.2 meta.json 格式兼容性\n\nGRASPrune 的 `meta.json` 格式:\n```json\n{\n  \"model_id\": \"...\",\n  \"model_family\": \"qwen\",\n  \"dtype\": \"torch.bfloat16\",\n  \"export_format\": \"materialized\",\n  \"rescale_alpha\": 0.5,\n  \"layers\": [\n    {\n      \"ffn_intermediate_size\": 12345,\n      \"num_heads\": 21,\n      \"num_key_value_heads\": 3,\n      \"head_dim\": 128\n    },\n    ...\n  ]\n}\n```\n\n我们的 `rebuild.py` 中 `rebuild_from_meta()` 读取 `meta[\"layers\"]` 的 `ffn_intermediate_size`、`num_heads`、`num_key_value_heads`、`head_dim`，然后 resize linear layers 并 load state_dict。两边完全兼容，无需修改。\n\n### 4.3 需要注意的兼容性问题\n\n1. **Qwen 的 bias**: DeepSeek-R1-Distill-Qwen-7B 的 attention 有 bias（q_proj, k_proj, v_proj 有 bias），GRASPrune 的 `QwenAttnGate.materialize_pruning()` 已正确处理 bias 的 slicing。\n\n2. **GQA group 映射**: GRASPrune 的 attention materialization 逻辑:\n   ```python\n   # gate_score_kv shape = (num_key_value_heads,) = (4,)\n   # keep_kv: bool mask on KV heads\n   # keep_heads = keep_kv.repeat_interleave(group_size)  # expand to Q heads\n   # group_size = num_heads // num_key_value_heads = 28 // 4 = 7\n   ```\n   这正是我们要求的 GQA group 粒度: 1 KV head + 7 Q heads = 1 group。\n\n3. **校准数据**: GRASPrune 默认用 WikiText2 train，我们的 importance/CKA 用 GSM8K train。为公平对比，可以考虑让 GRASPrune 也用 GSM8K（需要修改 `data.py` 或 `config.train_dataset_name`）。\n\n---\n\n## 5. 参考代码关键片段\n\n### 5.1 Gate 注入 (`gates.py`)\n\n```python\n# FFN gate: per-channel scalar\nclass LlamaMLPGate(nn.Module):\n    def __init__(self, cfg, src, gate_init, tau, device):\n        self.gate_score = nn.Parameter(\n            torch.full((cfg.intermediate_size,), gate_init, device=device)\n        )\n    \n    def forward(self, x):\n        inter = self.up_proj(x) * self.act_fn(self.gate_proj(x))\n        # STE: hard_mask + (soft - stopgrad(soft))\n        if self.training and hasattr(self, \"_batch_mask\"):\n            hard_mask = self._batch_mask\n            soft_prob = torch.sigmoid(self.gate_score / self.tau)\n            z = hard_mask + (soft_prob - soft_prob.detach())\n        return self.down_proj(inter * z)\n\n# Attention gate: per-KV-group scalar  \nclass LlamaAttnGate(nn.Module):\n    def __init__(self, cfg, layer_idx, src, gate_init, tau, device):\n        self.gate_score_kv = nn.Parameter(\n            torch.full((cfg.num_key_value_heads,), gate_init, device=device)\n        )\n    \n    def forward(self, hidden_states, ...):\n        # ... compute q, k, v, apply RoPE ...\n        # Gate KV at head level\n        kv_gate = z.view(1, -1, 1, 1)  # [1, num_kv_heads, 1, 1]\n        k = k * kv_gate\n        v = v * kv_gate\n        # ... attention computation ...\n```\n\n### 5.2 Budget Mask Projection (`pipeline.py`)\n\n```python\ndef build_batch_budget_masks(model, f_cost, a_cost, keep_ratio, tau):\n    scores, costs, holders = [], [], []\n    for block in get_transformer_layers(model):\n        # FFN gates\n        values = sigmoid(block.mlp.gate_score.detach() / tau)\n        scores.append(values); costs.append(full_like(values, f_cost))\n        # KV gates\n        values = sigmoid(block.self_attn.gate_score_kv.detach() / tau)\n        scores.append(values); costs.append(full_like(values, a_cost))\n    \n    score_tensor = cat(scores)\n    cost_tensor = cat(costs)\n    budget = cost_tensor.sum() * keep_ratio\n    \n    # Greedy top-k by probability (not by cost-efficiency)\n    order = argsort(score_tensor, descending=True)\n    cumsum = cumsum(cost_tensor[order])\n    chosen = order[cumsum <= budget]\n    \n    # Distribute back to per-module masks\n    ...\n```\n\n### 5.3 Materialization (`gates.py`)\n\n```python\n# Attention: physically slice weight matrices\ndef materialize_pruning(self):\n    keep_kv = self.eval_keep_mask_kv.to(torch.bool)  # [num_kv_heads]\n    keep_heads = keep_kv.repeat_interleave(group_size)  # [num_heads]\n    \n    # With optional rescale folding\n    if self._rescale_mode:\n        scale = 1.0 + alpha * tanh(gate_score)\n        scale_keep_kv = scale[keep_kv]\n    \n    self.q_proj = prune_q_out(self.q_proj, keep_heads)\n    self.k_proj = prune_kv_out(self.k_proj, keep_kv, scale_keep_kv)\n    self.v_proj = prune_kv_out(self.v_proj, keep_kv, scale_keep_kv)\n    self.o_proj = prune_o_in(self.o_proj, keep_heads)\n```\n\n---\n\n## 6. 实现建议\n\n### 对下一个 Worker 的指引:\n\n1. **最简路径**: 在服务器上 clone GRASPrune repo，直接用 `python train.py` 跑。不需要改我们的代码。\n\n2. **校准数据一致性**: 如果 reviewer 要求公平对比，需要让 GRASPrune 也用 GSM8K 校准数据。修改方法:\n   - 在 GRASPrune 的 `data.py` 中添加 GSM8K loader\n   - 或在 `config.py` 中把 `train_dataset_name` 改为自定义名\n\n3. **GPU 约束**: 必须指定 `--device cuda:0` 或 `cuda:1`（C001 约束），GRASPrune 单卡即可运行。\n\n4. **接入 GRPO recovery**: GRASPrune 产出的 `pruned_state_dict.safetensors` + `meta.json` 可直接用我们的 `rebuild.py:load_pruned_model()` 加载。\n\n5. **实验矩阵** (Phase 2 P1):\n\n   | Method | Pruning | Recovery | Eval |\n   |--------|---------|----------|------|\n   | Standard | importance-only pruning | GRPO | GSM8K |\n   | RASP | importance × (1-CKA)^α | GRPO | GSM8K |\n   | **GRASPrune** | learned gates + rescale | GRPO | GSM8K |\n\n6. **公平性考虑**:\n   - GRASPrune 有 rescale compensation，Standard 和 RASP 没有。如果差距太大可以考虑也给 Standard/RASP 加 rescale（或者在论文中讨论这个差异）。\n   - GRASPrune 是 gradient-free 对 backbone 的（backbone frozen），而我们的 importance scoring 需要 backward through backbone。这意味着 GRASPrune 对 backbone 权重无任何修改。\n\n---\n\n## 7. 参考文献\n\n- [GRASPrune paper (arXiv)](https://arxiv.org/abs/2604.19398)\n- [GRASPrune official code](https://github.com/ZiY-Wang/GRASPrune)\n- [Original GraSP (2020) — 不同的方法](https://arxiv.org/abs/2002.07376): \"Picking Winning Tickets Before Training by Preserving Gradient Flow\"，这是 unstructured pruning at initialization，与 GRASPrune 是完全不同的工作。\n- [GraSP official code (2020)](https://github.com/alecwangcq/GraSP)\n\n**注意命名区分**:\n- **GraSP** (2020, ICLR): Gradient Signal Preservation，unstructured，pruning at initialization\n- **GRASPrune** (2026, ACL): Global Gating for Budgeted Structured Pruning，structured，post-training，这是我们要用的\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "866289b4-f782-4a23-ae94-837b7c446639",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KmwesR8QR6dVE1upfnK4DN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1036,
      "cache_read_input_tokens": 75573,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1036
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

_source line 71 · 2026-05-14T08:24:46.009Z_

<details><summary>↩ Tool result · `toolu_01KPcbkkmEFHhsUpZjG4UkEp`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "37d4c8c3-c05b-4702-9f0b-f4d36c6e55b1",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_17/projects/recovery_aware_struct_prune/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 72_

报告已保存到项目 `memory.md`。

总结：

**GRASPrune (ACL 2026)** 是一个现成可用的 structured pruning baseline。核心发现：

1. **直接兼容**: 原生支持 Qwen 架构，attention pruning 天然在 KV group 粒度（`gate_score_kv` shape = `(num_key_value_heads,)`），完美满足 GQA group 硬约束。

2. **输出格式兼容**: 产出 `pruned_state_dict.safetensors` + `meta.json`，可直接被我们的 `rebuild.py:load_pruned_model()` 加载，无需修改现有代码。

3. **推荐方案**: 在服务器 clone 官方 repo，跑 `python train.py --model-family qwen --keep-ratio 0.65`，然后接入我们的 GRPO recovery pipeline。不需要重新实现。

4. **公平性注意点**: GRASPrune 有 rescale compensation（Standard/RASP 没有），校准数据默认用 WikiText2（我们用 GSM8K），论文中需讨论这些差异。

Sources:
- [GRASPrune paper](https://arxiv.org/abs/2604.19398)
- [GRASPrune GitHub](https://github.com/ZiY-Wang/GRASPrune)
- [Original GraSP (2020)](https://arxiv.org/abs/2002.07376)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "uuid": "fdce2890-3ea5-46f2-a755-f9371967d4bb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0154Nfw8UpbQCFVJ1bphABga",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6150,
      "cache_read_input_tokens": 76609,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6150
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

_source line 73_

报告已保存到项目 `memory.md`。

总结：

**GRASPrune (ACL 2026)** 是一个现成可用的 structured pruning baseline。核心发现：

1. **直接兼容**: 原生支持 Qwen 架构，attention pruning 天然在 KV group 粒度（`gate_score_kv` shape = `(num_key_value_heads,)`），完美满足 GQA group 硬约束。

2. **输出格式兼容**: 产出 `pruned_state_dict.safetensors` + `meta.json`，可直接被我们的 `rebuild.py:load_pruned_model()` 加载，无需修改现有代码。

3. **推荐方案**: 在服务器 clone 官方 repo，跑 `python train.py --model-family qwen --keep-ratio 0.65`，然后接入我们的 GRPO recovery pipeline。不需要重新实现。

4. **公平性注意点**: GRASPrune 有 rescale compensation（Standard/RASP 没有），校准数据默认用 WikiText2（我们用 GSM8K），论文中需讨论这些差异。

Sources:
- [GRASPrune paper](https://arxiv.org/abs/2604.19398)
- [GRASPrune GitHub](https://github.com/ZiY-Wang/GRASPrune)
- [Original GraSP (2020)](https://arxiv.org/abs/2002.07376)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 247766,
  "duration_api_ms": 263367,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "14848000-4b5f-41f3-93ef-f3b147968e01",
  "total_cost_usd": 1.1448310000000002,
  "usage": {
    "input_tokens": 77,
    "cache_creation_input_tokens": 70918,
    "cache_read_input_tokens": 510105,
    "output_tokens": 11033,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 70918,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 425,
        "cache_read_input_tokens": 76609,
        "cache_creation_input_tokens": 6150,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 6150
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 104976,
      "outputTokens": 3071,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.170331,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 77,
      "outputTokens": 11033,
      "cacheReadInputTokens": 510105,
      "cacheCreationInputTokens": 70918,
      "webSearchRequests": 0,
      "costUSD": 0.9745000000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "ee39a7b4-5ef2-4ace-972e-acbf895c687e"
}
```

</details>

---
