# research citation verification

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 30
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_research_citation-verification_20260520T104340.log`
- **Structured JSON:** [`31529e5868d5fe7a0b29.json`](../../sessions/31/31529e5868d5fe7a0b29.json)

## Before a recorded user message

30 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_2/projects/entrainment_gated_ft",
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
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
    "Write"
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
  "uuid": "eb7fcc58-c0e2-43ab-8d83-29b9460710c4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-4/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-2-projects-entrainment-gated-ft/memory/"
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
    "resetsAt": 1779286200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "cff4a652-079a-48b2-9b32-e1cf050dc151",
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to verify 6 paper citations that a reviewer mentioned. I need to search for each one to confirm if they're real or hallucinated. Let me launch parallel searches for all 6 papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "15f57f9a-34d3-4a98-851a-f9e4151c0d53",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V5RnyW1FWfX1hs2ojAQAv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12325,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12325
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

_source line 5_

逐一搜索验证这 6 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "4a49856e-83bd-48ad-b341-8ad71929be6d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V5RnyW1FWfX1hs2ojAQAv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12325,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12325
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01UC8mjWNXauPESMrPMqhQjo`</summary>

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
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "2aff71b8-cbd8-42ea-8aee-3050fbcb7a4c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011V5RnyW1FWfX1hs2ojAQAv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12325,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12325
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

_source line 7 · 2026-05-20T10:43:53.508Z_

<details><summary>↩ Tool result · `toolu_01UC8mjWNXauPESMrPMqhQjo`</summary>

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
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "bd7e0f7e-c684-4b41-a242-a2b43d96912b",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for all 6 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "453864b4-a835-4325-841d-483ef83665e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 9_

开始并行搜索全部 6 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "80f1f9f4-55ed-4b99-95f6-b54382b41e54",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0179UkUsdYNRoz5tNfw5aZ4X`</summary>

```json
{
  "query": "\"Cross-Model Disagreement as Label-Free Correctness Signal\" arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "9bfff10e-5f4c-4b23-aa26-5d62776b8d87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PxeNHCkLKxgimepYE9YAYb`</summary>

```json
{
  "query": "\"The Hidden Attention of Mamba Models\" ACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "3f8c38fd-7012-43d0-8c17-af853f11f649",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015homSFq44PxeuuyiXFdSZV`</summary>

```json
{
  "query": "\"Reconciling Model Multiplicity for Downstream Decision Making\" ICLR 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "f415e118-c212-4d30-bd14-ff69adba7d05",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F89Z4egJJe2TKJwd2jU8Df`</summary>

```json
{
  "query": "\"Resolving Predictive Multiplicity for the Rashomon Set\" arXiv 2601.09071"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "c223dc74-e58e-4ae9-b4c9-c10848ec889f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LJFa3KUcBBf9vPkQ7nZJtR`</summary>

```json
{
  "query": "\"Mamba-3\" ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "3fd53e4c-d150-47b4-9a41-743db4c2fd29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B9bCgr12Q4Bc8pT6YfKSjm`</summary>

```json
{
  "query": "D'Amour \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" JMLR 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "def7f8da-ca3b-451c-8438-730341e02c02",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JaKU1pxcmbzBiHdP8nS9MS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 682,
      "cache_read_input_tokens": 24166,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 682
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

_source line 16 · 2026-05-20T10:44:06.658Z_

<details><summary>↩ Tool result · `toolu_0179UkUsdYNRoz5tNfw5aZ4X`</summary>

```text
Web search results for query: ""Cross-Model Disagreement as Label-Free Correctness Signal" arXiv 2026"

Links: [{"title":"[2603.25450] Cross-Model Disagreement as a Label-Free Correctness Signal","url":"https://arxiv.org/abs/2603.25450"},{"title":"Cross-Model Disagreement as a Label-Free Correctness Signal","url":"https://arxiv.org/pdf/2603.25450"},{"title":"Cross-Model Disagreement as a Label-Free Correctness Signal","url":"https://arxiv.org/html/2603.25450"},{"title":"[2604.14152] From Black Box to Glass Box: Cross-Model ASR Disagreement to Prioto Review in Ambient AI Scribe Documentation","url":"https://arxiv.org/abs/2604.14152"},{"title":"Zoom Consistency: A Free Confidence Signal in Multi-Step ...","url":"https://arxiv.org/pdf/2604.15376"}]

I found the paper! Here are the details:

**Title:** Cross-Model Disagreement as a Label-Free Correctness Signal

**arXiv ID:** 2603.25450

**Date:** March 26, 2026

**Authors:** Matt Gorbett and Suman Jana

**Summary:**

The paper establishes cross-model disagreement as a practical, training-free approach to label-free correctness estimation, with direct applications in deployment monitoring, model routing, selective prediction, data filtering, and scalable oversight.

The approach works by having a second verifier model assess how surprised or uncertain it is when reading a generated answer via a single forward pass, with no generation from the verifying model required and no correctness labels needed.

The researchers instantiate this principle as Cross-Model Perplexity (CMP), which measures the verifying model's surprise at the generating model's answer tokens, and Cross-Model Entropy (CME), which measures the verifying model's uncertainty at those positions.

**Results:**

Both CMP and CME outperform within-model uncertainty baselines across benchmarks spanning reasoning, retrieval, and mathematical problem solving (MMLU, TriviaQA, and GSM8K). On MMLU, CMP achieves a mean AUROC of 0.75 against a within-model entropy baseline of 0.59.

The paper is available at: https://arxiv.org/abs/2603.25450


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "8bf5fc0e-07c2-48c5-ada2-ff7a039bc463",
  "tool_use_result": {
    "query": "\"Cross-Model Disagreement as Label-Free Correctness Signal\" arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013ufdqsaV7aAm5QC41i9mqz",
        "content": [
          {
            "title": "[2603.25450] Cross-Model Disagreement as a Label-Free Correctness Signal",
            "url": "https://arxiv.org/abs/2603.25450"
          },
          {
            "title": "Cross-Model Disagreement as a Label-Free Correctness Signal",
            "url": "https://arxiv.org/pdf/2603.25450"
          },
          {
            "title": "Cross-Model Disagreement as a Label-Free Correctness Signal",
            "url": "https://arxiv.org/html/2603.25450"
          },
          {
            "title": "[2604.14152] From Black Box to Glass Box: Cross-Model ASR Disagreement to Prioto Review in Ambient AI Scribe Documentation",
            "url": "https://arxiv.org/abs/2604.14152"
          },
          {
            "title": "Zoom Consistency: A Free Confidence Signal in Multi-Step ...",
            "url": "https://arxiv.org/pdf/2604.15376"
          }
        ]
      },
      "I found the paper! Here are the details:\n\n**Title:** Cross-Model Disagreement as a Label-Free Correctness Signal\n\n**arXiv ID:** 2603.25450\n\n**Date:** March 26, 2026\n\n**Authors:** Matt Gorbett and Suman Jana\n\n**Summary:**\n\nThe paper establishes cross-model disagreement as a practical, training-free approach to label-free correctness estimation, with direct applications in deployment monitoring, model routing, selective prediction, data filtering, and scalable oversight.\n\nThe approach works by having a second verifier model assess how surprised or uncertain it is when reading a generated answer via a single forward pass, with no generation from the verifying model required and no correctness labels needed.\n\nThe researchers instantiate this principle as Cross-Model Perplexity (CMP), which measures the verifying model's surprise at the generating model's answer tokens, and Cross-Model Entropy (CME), which measures the verifying model's uncertainty at those positions.\n\n**Results:**\n\nBoth CMP and CME outperform within-model uncertainty baselines across benchmarks spanning reasoning, retrieval, and mathematical problem solving (MMLU, TriviaQA, and GSM8K). On MMLU, CMP achieves a mean AUROC of 0.75 against a within-model entropy baseline of 0.59.\n\nThe paper is available at: https://arxiv.org/abs/2603.25450"
    ],
    "durationSeconds": 6.556395648000001
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-20T10:44:06.970Z_

<details><summary>↩ Tool result · `toolu_01PxeNHCkLKxgimepYE9YAYb`</summary>

```text
Web search results for query: ""The Hidden Attention of Mamba Models" ACL 2025"

Links: [{"title":"The Hidden Attention of Mamba Models - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.76/"},{"title":"GitHub - AmeenAli/HiddenMambaAttn: Official PyTorch Implementation of \"The Hidden Attention of Mamba Models\" · GitHub","url":"https://github.com/AmeenAli/HiddenMambaAttn"},{"title":"The Hidden Attention of Mamba Models","url":"https://aclanthology.org/2025.acl-long.76.pdf"},{"title":"Revealing and Mitigating the Local Pattern Shortcuts of ...","url":"https://aclanthology.org/2025.findings-acl.629.pdf"},{"title":"The Hidden Attention of Mamba Models","url":"https://arxiv.org/pdf/2403.01590"},{"title":"The Hidden Attention of Mamba Models","url":"https://www.researchgate.net/publication/394274145_The_Hidden_Attention_of_Mamba_Models"},{"title":"[2403.01590] The Hidden Attention of Mamba Models","url":"https://arxiv.org/abs/2403.01590"},{"title":"Accepted Main Conference Papers - ACL 2025","url":"https://2025.aclweb.org/program/main_papers/"},{"title":"LAMB: A Training-Free Method to Enhance the Long- ...","url":"https://aclanthology.org/2025.acl-short.96.pdf"}]

Based on the search results, here's what I found about "The Hidden Attention of Mamba Models":

## Paper Details

The paper "The Hidden Attention of Mamba Models" was authored by Ameen Ali Ali, Itamar Zimerman, and Lior Wolf and was accepted to the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) as a long paper, published in Vienna, Austria in July 2025.

## Main Contributions

The Mamba layer offers an efficient selective state-space model (SSM) that is effective in modeling multiple domains including NLP, long-range sequence processing, and computer vision. Selective SSMs are viewed as dual models, in which one trains in parallel on the entire sequence via an IO-aware parallel scan, and deploys in an autoregressive manner.

The paper adds a third view and shows that such models can be viewed as attention-driven models. This new perspective enables empirical and theoretical comparison of the underlying mechanisms to that of attention in transformers and allows exploration of the inner workings of the Mamba model with explainability methods.

The code is publicly available.

The paper makes an important theoretical contribution by revealing that Mamba models, despite being state-space models, can be understood through an attention-based lens, which opens up new avenues for interpreting and analyzing these models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "20656bbc-0190-476c-aa99-4388dff99535",
  "tool_use_result": {
    "query": "\"The Hidden Attention of Mamba Models\" ACL 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N59G4Kaxac9EzGSuyNanXy",
        "content": [
          {
            "title": "The Hidden Attention of Mamba Models - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.76/"
          },
          {
            "title": "GitHub - AmeenAli/HiddenMambaAttn: Official PyTorch Implementation of \"The Hidden Attention of Mamba Models\" · GitHub",
            "url": "https://github.com/AmeenAli/HiddenMambaAttn"
          },
          {
            "title": "The Hidden Attention of Mamba Models",
            "url": "https://aclanthology.org/2025.acl-long.76.pdf"
          },
          {
            "title": "Revealing and Mitigating the Local Pattern Shortcuts of ...",
            "url": "https://aclanthology.org/2025.findings-acl.629.pdf"
          },
          {
            "title": "The Hidden Attention of Mamba Models",
            "url": "https://arxiv.org/pdf/2403.01590"
          },
          {
            "title": "The Hidden Attention of Mamba Models",
            "url": "https://www.researchgate.net/publication/394274145_The_Hidden_Attention_of_Mamba_Models"
          },
          {
            "title": "[2403.01590] The Hidden Attention of Mamba Models",
            "url": "https://arxiv.org/abs/2403.01590"
          },
          {
            "title": "Accepted Main Conference Papers - ACL 2025",
            "url": "https://2025.aclweb.org/program/main_papers/"
          },
          {
            "title": "LAMB: A Training-Free Method to Enhance the Long- ...",
            "url": "https://aclanthology.org/2025.acl-short.96.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about \"The Hidden Attention of Mamba Models\":\n\n## Paper Details\n\nThe paper \"The Hidden Attention of Mamba Models\" was authored by Ameen Ali Ali, Itamar Zimerman, and Lior Wolf and was accepted to the 63rd Annual Meeting of the Association for Computational Linguistics (ACL 2025) as a long paper, published in Vienna, Austria in July 2025.\n\n## Main Contributions\n\nThe Mamba layer offers an efficient selective state-space model (SSM) that is effective in modeling multiple domains including NLP, long-range sequence processing, and computer vision. Selective SSMs are viewed as dual models, in which one trains in parallel on the entire sequence via an IO-aware parallel scan, and deploys in an autoregressive manner.\n\nThe paper adds a third view and shows that such models can be viewed as attention-driven models. This new perspective enables empirical and theoretical comparison of the underlying mechanisms to that of attention in transformers and allows exploration of the inner workings of the Mamba model with explainability methods.\n\nThe code is publicly available.\n\nThe paper makes an important theoretical contribution by revealing that Mamba models, despite being state-space models, can be understood through an attention-based lens, which opens up new avenues for interpreting and analyzing these models."
    ],
    "durationSeconds": 6.394821239999997
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T10:44:07.406Z_

<details><summary>↩ Tool result · `toolu_015homSFq44PxeuuyiXFdSZV`</summary>

```text
Web search results for query: ""Reconciling Model Multiplicity for Downstream Decision Making" ICLR 2025"

Links: [{"title":"Published as a conference paper at ICLR 2025 RECONCILING MODEL MULTIPLICITY","url":"https://openreview.net/pdf?id=uy4EavBEwl"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making","url":"https://arxiv.org/html/2405.19667v1"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making | OpenReview","url":"https://openreview.net/forum?id=uy4EavBEwl"},{"title":"[2405.19667] Reconciling Model Multiplicity for Downstream Decision Making","url":"https://arxiv.org/abs/2405.19667"},{"title":"[Quick Review] Reconciling Model Multiplicity for Downstream Decision Making","url":"https://liner.com/review/reconciling-model-multiplicity-for-downstream-decision-making"},{"title":"Reconciling Predictive Multiplicity in Practice | Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency","url":"https://dl.acm.org/doi/10.1145/3715275.3732216"},{"title":"Reconciling Model Multiplicity for Downstream Decision Making | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/reconciling-model-multiplicity-downstream-decision-making"},{"title":"[Literature Review] Reconciling Predictive Multiplicity in Practice","url":"https://www.themoonlight.io/en/review/reconciling-predictive-multiplicity-in-practice"}]

I found the paper! Here are the search results for "Reconciling Model Multiplicity for Downstream Decision Making" which was published at ICLR 2025:

## Paper Overview

The paper studies the problem of reconciling model multiplicity for multiple downstream decision-making tasks, where decision-makers have two predictive models with nearly equivalent accuracy but may lead to vastly different best-response actions for a significant number of individuals in the population.

## Key Problem

The paper shows that even when two predictive models approximately agree on their individual predictions almost everywhere, it is still possible for their induced best-response actions to differ on a substantial portion of the population.

## Proposed Solution

The paper introduces an algorithm, ReDCal (Reconcile Decision Calibration), which outputs predictive models calibrated to a finite set of downstream decision-making tasks. The algorithm, leveraging tools from multi-calibration, first reconciles differences in individual probability prediction, then calibrates the updated models such that they are indistinguishable from the true probability distribution to the decision-maker.

## Results

The proposed algorithm creates a pair of predictive models with improved downstream decision-making losses and agrees on their best-response actions almost everywhere compared to existing work.

The paper is authored by Ally Yalei Du, Dung Daniel Ngo, and Zhiwei Steven Wu and is available on OpenReview and arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "22ac0657-f0c1-49d7-ac24-a70198f44060",
  "tool_use_result": {
    "query": "\"Reconciling Model Multiplicity for Downstream Decision Making\" ICLR 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BPYxv4HSk651gq5fwyS6ak",
        "content": [
          {
            "title": "Published as a conference paper at ICLR 2025 RECONCILING MODEL MULTIPLICITY",
            "url": "https://openreview.net/pdf?id=uy4EavBEwl"
          },
          {
            "title": "Reconciling Model Multiplicity for Downstream Decision Making",
            "url": "https://arxiv.org/html/2405.19667v1"
          },
          {
            "title": "Reconciling Model Multiplicity for Downstream Decision Making | OpenReview",
            "url": "https://openreview.net/forum?id=uy4EavBEwl"
          },
          {
            "title": "[2405.19667] Reconciling Model Multiplicity for Downstream Decision Making",
            "url": "https://arxiv.org/abs/2405.19667"
          },
          {
            "title": "[Quick Review] Reconciling Model Multiplicity for Downstream Decision Making",
            "url": "https://liner.com/review/reconciling-model-multiplicity-for-downstream-decision-making"
          },
          {
            "title": "Reconciling Predictive Multiplicity in Practice | Proceedings of the 2025 ACM Conference on Fairness, Accountability, and Transparency",
            "url": "https://dl.acm.org/doi/10.1145/3715275.3732216"
          },
          {
            "title": "Reconciling Model Multiplicity for Downstream Decision Making | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/reconciling-model-multiplicity-downstream-decision-making"
          },
          {
            "title": "[Literature Review] Reconciling Predictive Multiplicity in Practice",
            "url": "https://www.themoonlight.io/en/review/reconciling-predictive-multiplicity-in-practice"
          }
        ]
      },
      "I found the paper! Here are the search results for \"Reconciling Model Multiplicity for Downstream Decision Making\" which was published at ICLR 2025:\n\n## Paper Overview\n\nThe paper studies the problem of reconciling model multiplicity for multiple downstream decision-making tasks, where decision-makers have two predictive models with nearly equivalent accuracy but may lead to vastly different best-response actions for a significant number of individuals in the population.\n\n## Key Problem\n\nThe paper shows that even when two predictive models approximately agree on their individual predictions almost everywhere, it is still possible for their induced best-response actions to differ on a substantial portion of the population.\n\n## Proposed Solution\n\nThe paper introduces an algorithm, ReDCal (Reconcile Decision Calibration), which outputs predictive models calibrated to a finite set of downstream decision-making tasks. The algorithm, leveraging tools from multi-calibration, first reconciles differences in individual probability prediction, then calibrates the updated models such that they are indistinguishable from the true probability distribution to the decision-maker.\n\n## Results\n\nThe proposed algorithm creates a pair of predictive models with improved downstream decision-making losses and agrees on their best-response actions almost everywhere compared to existing work.\n\nThe paper is authored by Ally Yalei Du, Dung Daniel Ngo, and Zhiwei Steven Wu and is available on OpenReview and arXiv."
    ],
    "durationSeconds": 6.827158045
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T10:44:07.889Z_

<details><summary>↩ Tool result · `toolu_01F89Z4egJJe2TKJwd2jU8Df`</summary>

```text
Web search results for query: ""Resolving Predictive Multiplicity for the Rashomon Set" arXiv 2601.09071"

Links: [{"title":"[2601.09071] Resolving Predictive Multiplicity for the Rashomon Set","url":"https://arxiv.org/abs/2601.09071"},{"title":"Resolving Predictive Multiplicity for the Rashomon Set | Request PDF","url":"https://www.researchgate.net/publication/402661358_Resolving_Predictive_Multiplicity_for_the_Rashomon_Set"},{"title":"Resolving Predictive Multiplicity for the Rashomon Set","url":"https://arxiv.org/pdf/2601.09071"},{"title":"Dropout-Based Rashomon Set Exploration for Efficient Predictive   Multiplicity Estimation","url":"https://arxiv.org/pdf/2402.00728"},{"title":"CASHomon Sets: Efficient Rashomon Sets Across Multiple Model Classes and their Hyperparameters","url":"https://arxiv.org/pdf/2603.15321"}]

Based on the search results, here's what I found about the paper:

## "Resolving Predictive Multiplicity for the Rashomon Set" (arXiv 2601.09071)

The paper addresses predictive multiplicity, where a "Rashomon set" of models achieve similar accuracy but diverge in their individual predictions. This inconsistency undermines trust in high-stakes applications where consistent predictions are desired.

The authors propose three main approaches to reduce inconsistency:

1. **Outlier Correction**: An outlier has a label that none of the good models are capable of predicting correctly. Outliers can cause the Rashomon set to have high variance predictions in a local area, so fixing them can lower variance.

2. **Local Patching**: In a local region around a test point, models may disagree with each other because some of them are biased. The method detects and fixes such biases using a validation set, which also reduces multiplicity.

3. A third approach is mentioned but the search results don't provide full details.

Outlier correction is most useful as a preprocessing step for subsequent reconciliation, particularly when correcting validation outlier labels provides cleaner data for the local patching method.

The paper was published on January 14, 2026, and is authored by Parian Haghighat, Hadis Anahideh, and Cynthia Rudin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "f41e136d-d696-4756-aae1-5d4025733323",
  "tool_use_result": {
    "query": "\"Resolving Predictive Multiplicity for the Rashomon Set\" arXiv 2601.09071",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SHVZeNPuSyJusuY3KtfjHg",
        "content": [
          {
            "title": "[2601.09071] Resolving Predictive Multiplicity for the Rashomon Set",
            "url": "https://arxiv.org/abs/2601.09071"
          },
          {
            "title": "Resolving Predictive Multiplicity for the Rashomon Set | Request PDF",
            "url": "https://www.researchgate.net/publication/402661358_Resolving_Predictive_Multiplicity_for_the_Rashomon_Set"
          },
          {
            "title": "Resolving Predictive Multiplicity for the Rashomon Set",
            "url": "https://arxiv.org/pdf/2601.09071"
          },
          {
            "title": "Dropout-Based Rashomon Set Exploration for Efficient Predictive   Multiplicity Estimation",
            "url": "https://arxiv.org/pdf/2402.00728"
          },
          {
            "title": "CASHomon Sets: Efficient Rashomon Sets Across Multiple Model Classes and their Hyperparameters",
            "url": "https://arxiv.org/pdf/2603.15321"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n## \"Resolving Predictive Multiplicity for the Rashomon Set\" (arXiv 2601.09071)\n\nThe paper addresses predictive multiplicity, where a \"Rashomon set\" of models achieve similar accuracy but diverge in their individual predictions. This inconsistency undermines trust in high-stakes applications where consistent predictions are desired.\n\nThe authors propose three main approaches to reduce inconsistency:\n\n1. **Outlier Correction**: An outlier has a label that none of the good models are capable of predicting correctly. Outliers can cause the Rashomon set to have high variance predictions in a local area, so fixing them can lower variance.\n\n2. **Local Patching**: In a local region around a test point, models may disagree with each other because some of them are biased. The method detects and fixes such biases using a validation set, which also reduces multiplicity.\n\n3. A third approach is mentioned but the search results don't provide full details.\n\nOutlier correction is most useful as a preprocessing step for subsequent reconciliation, particularly when correcting validation outlier labels provides cleaner data for the local patching method.\n\nThe paper was published on January 14, 2026, and is authored by Parian Haghighat, Hadis Anahideh, and Cynthia Rudin."
    ],
    "durationSeconds": 6.843033642000002
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T10:44:08.905Z_

<details><summary>↩ Tool result · `toolu_01LJFa3KUcBBf9vPkQ7nZJtR`</summary>

```text
Web search results for query: ""Mamba-3" ICLR 2026"

Links: [{"title":"Mamba-3: The Next Evolution in Sequence Modeling - Oreate AI Blog","url":"https://www.oreateai.com/blog/mamba3-the-next-evolution-in-sequence-modeling/de3cf24bf677944d35913641965acf2f"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiviq.substack.com/p/mamba-3-improved-sequence-modeling"},{"title":"Published as a conference paper at ICLR 2026 MAMBA-3:","url":"https://openreview.net/pdf?id=HwCvaJOiCj"},{"title":"ちょこちょこ噂になってるMamba-3の論文、これか ICLR 2026 ...","url":"https://x.com/hpp_ricecake/status/1976858860439920750"},{"title":"ICLR Poster Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://iclr.cc/virtual/2026/poster/10010352"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles | OpenReview","url":"https://openreview.net/forum?id=HwCvaJOiCj"},{"title":"[2603.15569] Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiv.org/abs/2603.15569"},{"title":"Under review as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2510.03279"}]

Based on the search results, here's what I found about Mamba-3 at ICLR 2026:

## Overview

Mamba-3 represents a groundbreaking advancement in sequence modeling architectures at ICLR 2026 with enhanced precision and efficiency aimed at outperforming traditional Transformer models.

## Key Technical Improvements

The method integrates three key technical improvements: a trapezoidal discretization scheme (replacing Euler's method), a Multi-Input Multi-Output (MIMO) formulation to increase arithmetic intensity, and a theoretical bridge connecting complex-valued SSMs to Data-Dependent Rotary Embeddings (RoPE).

More specifically, the improvements combine a more expressive recurrence, a complex state update rule that enables richer state tracking, and a multi-input, multi-output formulation together, resulting in a stronger model that better exploits hardware parallelism during decoding.

## Performance Results

At the 1.5B scale, Mamba-3 improves average downstream accuracy by 0.6 percentage points compared to the next best model (Gated DeltaNet), with Mamba-3's MIMO variant further improving accuracy by another 1.2 points for a total 1.8 point gain. Additionally, Mamba-3 achieves comparable perplexity to Mamba-2 despite using half of its predecessor's state size.

## Hardware Efficiency

Mamba-3 (MIMO) improves hardware utilization and increases decoding FLOPs by up to 4× relative to Mamba-2 at fixed state size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "849b5d81-7afa-4880-b987-ca9e0aa43a57",
  "tool_use_result": {
    "query": "\"Mamba-3\" ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01As6yTNhscuZa6UJBbJDng7",
        "content": [
          {
            "title": "Mamba-3: The Next Evolution in Sequence Modeling - Oreate AI Blog",
            "url": "https://www.oreateai.com/blog/mamba3-the-next-evolution-in-sequence-modeling/de3cf24bf677944d35913641965acf2f"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiviq.substack.com/p/mamba-3-improved-sequence-modeling"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 MAMBA-3:",
            "url": "https://openreview.net/pdf?id=HwCvaJOiCj"
          },
          {
            "title": "ちょこちょこ噂になってるMamba-3の論文、これか ICLR 2026 ...",
            "url": "https://x.com/hpp_ricecake/status/1976858860439920750"
          },
          {
            "title": "ICLR Poster Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://iclr.cc/virtual/2026/poster/10010352"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles | OpenReview",
            "url": "https://openreview.net/forum?id=HwCvaJOiCj"
          },
          {
            "title": "[2603.15569] Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiv.org/abs/2603.15569"
          },
          {
            "title": "Under review as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2510.03279"
          }
        ]
      },
      "Based on the search results, here's what I found about Mamba-3 at ICLR 2026:\n\n## Overview\n\nMamba-3 represents a groundbreaking advancement in sequence modeling architectures at ICLR 2026 with enhanced precision and efficiency aimed at outperforming traditional Transformer models.\n\n## Key Technical Improvements\n\nThe method integrates three key technical improvements: a trapezoidal discretization scheme (replacing Euler's method), a Multi-Input Multi-Output (MIMO) formulation to increase arithmetic intensity, and a theoretical bridge connecting complex-valued SSMs to Data-Dependent Rotary Embeddings (RoPE).\n\nMore specifically, the improvements combine a more expressive recurrence, a complex state update rule that enables richer state tracking, and a multi-input, multi-output formulation together, resulting in a stronger model that better exploits hardware parallelism during decoding.\n\n## Performance Results\n\nAt the 1.5B scale, Mamba-3 improves average downstream accuracy by 0.6 percentage points compared to the next best model (Gated DeltaNet), with Mamba-3's MIMO variant further improving accuracy by another 1.2 points for a total 1.8 point gain. Additionally, Mamba-3 achieves comparable perplexity to Mamba-2 despite using half of its predecessor's state size.\n\n## Hardware Efficiency\n\nMamba-3 (MIMO) improves hardware utilization and increases decoding FLOPs by up to 4× relative to Mamba-2 at fixed state size."
    ],
    "durationSeconds": 7.393014833000001
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-20T10:44:09.633Z_

<details><summary>↩ Tool result · `toolu_01B9bCgr12Q4Bc8pT6YfKSjm`</summary>

```text
Web search results for query: "D'Amour "Underspecification Presents Challenges for Credibility in Modern Machine Learning" JMLR 2022"

Links: [{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy","url":"https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"},{"title":"Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research","url":"https://dl.acm.org/doi/10.5555/3586589.3586815"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.jmlr.org/papers/v23/20-1335.html"},{"title":"(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.researchgate.net/publication/364089505_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"},{"title":"[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://arxiv.org/abs/2011.03395"},{"title":"Underspecification Presents Challenges for Credibility in ...","url":"https://www.jmlr.org/papers/volume23/20-1335/20-1335.pdf"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine   Learning","url":"https://arxiv.org/pdf/2011.03395"},{"title":"[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"},{"title":"(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.academia.edu/66837133/Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"}]

I found the paper you're looking for. Here are the details:

**Publication Information:**

The paper "Underspecification Presents Challenges for Credibility in Modern Machine Learning" was authored by Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, and D. Sculley, and was published in 2022 in Volume 23, Issue 226, pages 1-61 of JMLR.

**Main Contribution:**

The paper identifies that machine learning systems often exhibit unexpectedly poor behavior when deployed in real-world domains, and identifies underspecification in ML pipelines as a key reason for these failures. Predictors returned by underspecified pipelines are often treated as equivalent based on their training domain performance, but the paper shows that such predictors can behave very differently in deployment domains, leading to instability and poor model behavior.

**Scope:**

The paper demonstrates that this problem appears in a wide variety of practical ML pipelines, using examples from computer vision, medical imaging, natural language processing, clinical risk prediction based on electronic health records, and medical genomics.

The paper is available at the JMLR website and on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "813954fe-c3a9-49da-ba2d-c1b77f63258e",
  "tool_use_result": {
    "query": "D'Amour \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" JMLR 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_018zqUWqvf84AFFcVD3CbDqA",
        "content": [
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning. | BibSonomy",
            "url": "https://www.bibsonomy.org/bibtex/11392e00397b9939b73ae7159630384bc"
          },
          {
            "title": "Underspecification presents challenges for credibility in modern machine learning | The Journal of Machine Learning Research",
            "url": "https://dl.acm.org/doi/10.5555/3586589.3586815"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.jmlr.org/papers/v23/20-1335.html"
          },
          {
            "title": "(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.researchgate.net/publication/364089505_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"
          },
          {
            "title": "[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://arxiv.org/abs/2011.03395"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in ...",
            "url": "https://www.jmlr.org/papers/volume23/20-1335/20-1335.pdf"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine   Learning",
            "url": "https://arxiv.org/pdf/2011.03395"
          },
          {
            "title": "[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"
          },
          {
            "title": "(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.academia.edu/66837133/Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"
          }
        ]
      },
      "I found the paper you're looking for. Here are the details:\n\n**Publication Information:**\n\nThe paper \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" was authored by Alexander D'Amour, Katherine Heller, Dan Moldovan, Ben Adlam, Babak Alipanahi, Alex Beutel, Christina Chen, Jonathan Deaton, Jacob Eisenstein, Matthew D. Hoffman, Farhad Hormozdiari, Neil Houlsby, Shaobo Hou, Ghassen Jerfel, Alan Karthikesalingam, Mario Lucic, Yian Ma, Cory McLean, Diana Mincu, Akinori Mitani, Andrea Montanari, Zachary Nado, Vivek Natarajan, Christopher Nielson, Thomas F. Osborne, Rajiv Raman, Kim Ramasamy, Rory Sayres, Jessica Schrouff, Martin Seneviratne, Shannon Sequeira, Harini Suresh, Victor Veitch, Max Vladymyrov, Xuezhi Wang, Kellie Webster, Steve Yadlowsky, Taedong Yun, Xiaohua Zhai, and D. Sculley, and was published in 2022 in Volume 23, Issue 226, pages 1-61 of JMLR.\n\n**Main Contribution:**\n\nThe paper identifies that machine learning systems often exhibit unexpectedly poor behavior when deployed in real-world domains, and identifies underspecification in ML pipelines as a key reason for these failures. Predictors returned by underspecified pipelines are often treated as equivalent based on their training domain performance, but the paper shows that such predictors can behave very differently in deployment domains, leading to instability and poor model behavior.\n\n**Scope:**\n\nThe paper demonstrates that this problem appears in a wide variety of practical ML pipelines, using examples from computer vision, medical imaging, natural language processing, clinical risk prediction based on electronic health records, and medical genomics.\n\nThe paper is available at the JMLR website and on arXiv."
    ],
    "durationSeconds": 7.825383642
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now let me get more details on some papers. I need to verify the exact authors for some of them. Let me also check the D'Amour paper's arXiv date vs JMLR publication date.

From the search results:
1. **Cross-Model Disagreement** - ✅ Real, arXiv 2603.25450, March 2026, by Matt Gorbett and Suman Jana
2. **Hidden Attention of Mamba Models** - ✅ Real, ACL 2025, by Ameen Ali, Itamar Zimerman, Lior Wolf. arXiv 2403.01590


3. **Reconciling Model Multiplicity** - ✅ Real, ICLR 2025, by Ally Yalei Du, Dung Daniel Ngo, Zhiwei Steven Wu. arXiv 2405.19667
4. **Resolving Predictive Multiplicity for the Rashomon Set** - ✅ Real, arXiv 2601.09071, Jan 2026, by Parian Haghighat, Hadis Anahideh, Cynthia Rudin
5. **Mamba-3** - ✅ Real, ICLR 2026, arXiv 2603.15569.

I need to track down the full title for Mamba-3 and confirm the authors. Also clarifying that the D'Amour Underspecification paper's JMLR 2022 citation is correct—the reviewer was pointing to the earlier arXiv preprint from 2020, but the published version is what should be cited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "38ffdea8-bb5f-45e8-9718-80bd5587a323",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JxHyQwrRDcDs8KDfXhLfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5089,
      "cache_read_input_tokens": 24848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5089
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

需要补充 Mamba-3 作者信息和 D'Amour 论文的 arXiv 日期确认。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "cd3a180c-75cb-4bcd-be85-2356975a48d7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JxHyQwrRDcDs8KDfXhLfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5089,
      "cache_read_input_tokens": 24848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5089
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GazPDAuAE8nAYf8WgFYVKs`</summary>

```json
{
  "query": "Mamba-3 arXiv 2603.15569 authors \"Improved Sequence Modeling\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "edbb9510-2590-406e-ae96-f1d7f2295cf5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JxHyQwrRDcDs8KDfXhLfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5089,
      "cache_read_input_tokens": 24848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5089
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TYRhDRMj4r7ycqo9gXFQ3r`</summary>

```json
{
  "query": "arXiv 2011.03395 D'Amour underspecification submission date 2020"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "f0ff1ce3-3d4a-4760-a04a-6375291b9d93",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013JxHyQwrRDcDs8KDfXhLfE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5089,
      "cache_read_input_tokens": 24848,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5089
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

_source line 26 · 2026-05-20T10:44:25.826Z_

<details><summary>↩ Tool result · `toolu_01GazPDAuAE8nAYf8WgFYVKs`</summary>

```text
Web search results for query: "Mamba-3 arXiv 2603.15569 authors "Improved Sequence Modeling""

Links: [{"title":"[2603.15569] Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiv.org/abs/2603.15569"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.15569"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles | Request PDF","url":"https://www.researchgate.net/publication/402480967_Mamba-3_Improved_Sequence_Modeling_using_State_Space_Principles"},{"title":"[2603.15569v1] Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiv.org/abs/2603.15569v1"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiv.org/pdf/2603.15569"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://arxiviq.substack.com/p/mamba-3-improved-sequence-modeling"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles | Princeton Language and Intelligence","url":"https://pli.princeton.edu/blog/2026/mamba-3-improved-sequence-modeling-using-state-space-principles"},{"title":"GitHub - state-spaces/mamba: Mamba SSM architecture · GitHub","url":"https://github.com/state-spaces/mamba"},{"title":"ICLR Poster Mamba-3: Improved Sequence Modeling using State Space Principles","url":"https://iclr.cc/virtual/2026/poster/10010352"},{"title":"Mamba-3: Improved Sequence Modeling using State Space Principles | OpenReview","url":"https://openreview.net/forum?id=HwCvaJOiCj"}]

Based on the search results, here's what I found about the paper:

**Title:** Mamba-3: Improved Sequence Modeling using State Space Principles

**Authors:** Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, and Albert Gu

**arXiv ID:** 2603.15569, submitted on March 16, 2026

**Affiliations:** The authors are from Carnegie Mellon University, Princeton University, Together AI, and Cartesia AI

**Key Contributions:** The paper introduces three core methodological improvements inspired by the state space model viewpoint of linear models, combining: a more expressive recurrence derived from SSM discretization, a complex-valued state update rule that enables richer state tracking, and a multi-input configuration.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "02286faa-a279-4802-86f5-10b5340c6dd6",
  "tool_use_result": {
    "query": "Mamba-3 arXiv 2603.15569 authors \"Improved Sequence Modeling\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_015QP4rxP2MgyjEnxGeL8yRM",
        "content": [
          {
            "title": "[2603.15569] Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiv.org/abs/2603.15569"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.15569"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles | Request PDF",
            "url": "https://www.researchgate.net/publication/402480967_Mamba-3_Improved_Sequence_Modeling_using_State_Space_Principles"
          },
          {
            "title": "[2603.15569v1] Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiv.org/abs/2603.15569v1"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiv.org/pdf/2603.15569"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://arxiviq.substack.com/p/mamba-3-improved-sequence-modeling"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles | Princeton Language and Intelligence",
            "url": "https://pli.princeton.edu/blog/2026/mamba-3-improved-sequence-modeling-using-state-space-principles"
          },
          {
            "title": "GitHub - state-spaces/mamba: Mamba SSM architecture · GitHub",
            "url": "https://github.com/state-spaces/mamba"
          },
          {
            "title": "ICLR Poster Mamba-3: Improved Sequence Modeling using State Space Principles",
            "url": "https://iclr.cc/virtual/2026/poster/10010352"
          },
          {
            "title": "Mamba-3: Improved Sequence Modeling using State Space Principles | OpenReview",
            "url": "https://openreview.net/forum?id=HwCvaJOiCj"
          }
        ]
      },
      "Based on the search results, here's what I found about the paper:\n\n**Title:** Mamba-3: Improved Sequence Modeling using State Space Principles\n\n**Authors:** Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, and Albert Gu\n\n**arXiv ID:** 2603.15569, submitted on March 16, 2026\n\n**Affiliations:** The authors are from Carnegie Mellon University, Princeton University, Together AI, and Cartesia AI\n\n**Key Contributions:** The paper introduces three core methodological improvements inspired by the state space model viewpoint of linear models, combining: a more expressive recurrence derived from SSM discretization, a complex-valued state update rule that enables richer state tracking, and a multi-input configuration."
    ],
    "durationSeconds": 4.321477706000005
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-20T10:44:26.051Z_

<details><summary>↩ Tool result · `toolu_01TYRhDRMj4r7ycqo9gXFQ3r`</summary>

```text
Web search results for query: "arXiv 2011.03395 D'Amour underspecification submission date 2020"

Links: [{"title":"[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://arxiv.org/abs/2011.03395"},{"title":"(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning","url":"https://www.researchgate.net/publication/345555232_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"},{"title":"[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"},{"title":"Figure 13 from Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b/figure/19"},{"title":"Underspecification Presents Challenges for Credibility in Modern Machine Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv201103395D/abstract"},{"title":"dblp: Underspecification Presents Challenges for Credibility in Modern Machine Learning.","url":"https://dblp.org/rec/journals/corr/abs-2011-03395.html"}]

The search results contain information about the arXiv paper you're looking for. Here's what I found:

The paper was submitted on Friday, November 6, 2020. The paper is titled "Underspecification Presents Challenges for Credibility in Modern Machine Learning" and was authored by Alexander D'Amour, Katherine Heller, Dan Moldovan, and others.

The paper identifies underspecification as a key reason for ML failures, defining an ML pipeline as underspecified when it can return many predictors with equivalently strong held-out performance in the training domain. The paper shows that predictors returned by underspecified pipelines can behave very differently in deployment domains despite equivalent training domain performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "96e9a565-fef5-491f-a287-d7e8321e9dcc",
  "tool_use_result": {
    "query": "arXiv 2011.03395 D'Amour underspecification submission date 2020",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gdp3XeKiMm2ZMES55zvEag",
        "content": [
          {
            "title": "[2011.03395] Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://arxiv.org/abs/2011.03395"
          },
          {
            "title": "(PDF) Underspecification Presents Challenges for Credibility in Modern Machine Learning",
            "url": "https://www.researchgate.net/publication/345555232_Underspecification_Presents_Challenges_for_Credibility_in_Modern_Machine_Learning"
          },
          {
            "title": "[PDF] Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b"
          },
          {
            "title": "Figure 13 from Underspecification Presents Challenges for Credibility in Modern Machine Learning | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Underspecification-Presents-Challenges-for-in-D'Amour-Heller/71a85e735a3686bef8cce3725ae5ba82e2cabb1b/figure/19"
          },
          {
            "title": "Underspecification Presents Challenges for Credibility in Modern Machine Learning - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2020arXiv201103395D/abstract"
          },
          {
            "title": "dblp: Underspecification Presents Challenges for Credibility in Modern Machine Learning.",
            "url": "https://dblp.org/rec/journals/corr/abs-2011-03395.html"
          }
        ]
      },
      "The search results contain information about the arXiv paper you're looking for. Here's what I found:\n\nThe paper was submitted on Friday, November 6, 2020. The paper is titled \"Underspecification Presents Challenges for Credibility in Modern Machine Learning\" and was authored by Alexander D'Amour, Katherine Heller, Dan Moldovan, and others.\n\nThe paper identifies underspecification as a key reason for ML failures, defining an ML pipeline as underspecified when it can return many predictors with equivalently strong held-out performance in the training domain. The paper shows that predictors returned by underspecified pipelines can behave very differently in deployment domains despite equivalent training domain performance."
    ],
    "durationSeconds": 4.275444092999998
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me compile the results.

1. **Cross-Model Disagreement** - ✅ Real, arXiv 2603.25450, March 2026, Matt Gorbett, Suman Jana (Columbia University)
2. **Hidden Attention of Mamba Models** - ✅ Real, ACL 2025 (long paper), arXiv 2403.01590, Ameen Ali, Itamar Zimerman, Lior Wolf


3. **Reconciling Model Multiplicity** - ✅ Real, ICLR 2025, arXiv 2405.19667, Ally Yalei Du, Dung Daniel Ngo, Zhiwei Steven Wu
4. **Resolving Predictive Multiplicity for the Rashomon Set** - ✅ Real, arXiv 2601.09071, Jan 2026, Parian Haghighat, Hadis Anahideh, Cynthia Rudin
5. **Mamba-3** - ✅ Real, ICLR 2026, arXiv 2603.15569, Aakash Lahoti

, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
6. **D'Amour** - The preprint came out in November 2020, but the official JMLR publication is from 2022, so the current bibliography entry listing JMLR 2022 is correct.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "1bdf8aed-a9db-411f-a685-653ede4a55f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q2ryTbJz6VCD2L9Hr48TE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2158,
      "cache_read_input_tokens": 29937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2158
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

全部 6 篇搜索完毕，结果如下：

---

## 论文 1: Cross-Model Disagreement as a Label-Free Correctness Signal
- 存在性: ✅ 真实存在
- 实际标题: Cross-Model Disagreement as a Label-Free Correctness Signal
- 作者: Matt Gorbett, Suman Jana
- Venue: arXiv preprint, March 2026
- arXiv ID: 2603.25450
- URL: https://arxiv.org/abs/2603.25450
- BibTeX:
```bibtex
@article{gorbett2026crossmodel,
  title={Cross-Model Disagreement as a Label-Free Correctness Signal},
  author={Gorbett, Matt and Jana, Suman},
  journal={arXiv preprint arXiv:2603.25450},
  year={2026}
}
```
- 与本文相关性: 提出 Cross-Model Perplexity/Entropy 作为无标签正确性信号，与 §4.3 per-example divergence 的思路有交叉但角度不同——他们聚焦 deployment monitoring/selective prediction，本文聚焦 fine-tuning gating。可以在 Related Work 中讨论。

---

## 论文 2: The Hidden Attention of Mamba Models
- 存在性: ✅ 真实存在
- 实际标题: The Hidden Attention of Mamba Models
- 作者: Ameen Ali, Itamar Zimerman, Lior Wolf
- Venue: ACL 2025 (Long Paper)
- arXiv ID: 2403.01590
- URL: https://aclanthology.org/2025.acl-long.76/
- BibTeX:
```bibtex
@inproceedings{ali2025hidden,
  title={The Hidden Attention of Mamba Models},
  author={Ali, Ameen and Zimerman, Itamar and Wolf, Lior},
  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2025}
}
```
- 与本文相关性: 揭示 Mamba SSM 可等价为隐式 attention，与 Appendix D attention pattern analysis 方法论相关。如果 Appendix D 分析了 SSM-based 模型的 attention patterns，应当引用。

---

## 论文 3: Reconciling Model Multiplicity for Downstream Decision Making
- 存在性: ✅ 真实存在
- 实际标题: Reconciling Model Multiplicity for Downstream Decision Making
- 作者: Ally Yalei Du, Dung Daniel Ngo, Zhiwei Steven Wu
- Venue: ICLR 2025
- arXiv ID: 2405.19667
- URL: https://openreview.net/forum?id=uy4EavBEwl
- BibTeX:
```bibtex
@inproceedings{du2025reconciling,
  title={Reconciling Model Multiplicity for Downstream Decision Making},
  author={Du, Ally Yalei and Ngo, Dung Daniel and Wu, Zhiwei Steven},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025}
}
```
- 与本文相关性: 直接处理 predictive multiplicity 下的 model reconciliation，与本文 entrainment gating 框架在 multiplicity 层面有理论联系。建议引用。

---

## 论文 4: Resolving Predictive Multiplicity for the Rashomon Set
- 存在性: ✅ 真实存在
- 实际标题: Resolving Predictive Multiplicity for the Rashomon Set
- 作者: Parian Haghighat, Hadis Anahideh, Cynthia Rudin
- Venue: arXiv preprint, January 2026
- arXiv ID: 2601.09071
- URL: https://arxiv.org/abs/2601.09071
- BibTeX:
```bibtex
@article{haghighat2026resolving,
  title={Resolving Predictive Multiplicity for the Rashomon Set},
  author={Haghighat, Parian and Anahideh, Hadis and Rudin, Cynthia},
  journal={arXiv preprint arXiv:2601.09071},
  year={2026}
}
```
- 与本文相关性: Rashomon set 上通过 outlier correction + local patching 降低 multiplicity，是 predictive multiplicity 理论的最新进展。如果本文涉及 Rashomon set 或 multiplicity resolution，应引用。

---

## 论文 5: Mamba-3
- 存在性: ✅ 真实存在
- 实际标题: Mamba-3: Improved Sequence Modeling using State Space Principles
- 作者: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- Venue: ICLR 2026
- arXiv ID: 2603.15569
- URL: https://openreview.net/forum?id=HwCvaJOiCj
- BibTeX:
```bibtex
@inproceedings{lahoti2026mamba3,
  title={Mamba-3: Improved Sequence Modeling using State Space Principles},
  author={Lahoti, Aakash and Li, Kevin Y. and Chen, Berlin and Wang, Caitlin and Bick, Aviv and Kolter, J. Zico and Dao, Tri and Gu, Albert},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2026}
}
```
- 与本文相关性: 最新 hybrid SSM architecture，如果本文实验涉及 Mamba 系列模型或讨论 hybrid architectures，可在 Related Work 中提及作为最新进展。

---

## 论文 6: D'Amour et al. Underspecification 年份验证
- 存在性: ⚠️ 存在，审稿人年份质疑不成立
- 实际情况:
  - arXiv 预印本: 2020 年 11 月 6 日 (arXiv:2011.03395)
  - JMLR 正式发表: 2022 年, Volume 23, Issue 226, pp. 1–61
- **结论: 当前 bib 引用 JMLR 2022 是正确的。** 审稿人说"应为 2020"是混淆了 arXiv 预印本日期和正式发表日期。学术引用应以正式发表版本为准。
- URL: https://www.jmlr.org/papers/v23/20-1335.html
- 当前 BibTeX 无需修改。

---

## 总结

| # | 论文 | 存在性 | 审稿人信息准确度 |
|---|------|--------|-----------------|
| 1 | Cross-Model Disagreement | ✅ 真实 | arXiv ID、年份均正确 |
| 2 | Hidden Attention of Mamba | ✅ 真实 | Venue、年份均正确 |
| 3 | Reconciling Model Multiplicity | ✅ 真实 | Venue、年份均正确 |
| 4 | Resolving Predictive Multiplicity | ✅ 真实 | arXiv ID、年份均正确 |
| 5 | Mamba-3 | ✅ 真实 | Venue、年份均正确 |
| 6 | D'Amour underspecification | ⚠️ 审稿人有误 | JMLR 2022 正确，非 2020 |

**5 篇遗漏引用全部真实存在**，非 AI 幻觉。论文 6 的年份质疑不成立，当前 bib 无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "uuid": "c301cc62-43ac-456d-986c-c51a396b0563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019Q2ryTbJz6VCD2L9Hr48TE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2158,
      "cache_read_input_tokens": 29937,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2158
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

_source line 30_

全部 6 篇搜索完毕，结果如下：

---

## 论文 1: Cross-Model Disagreement as a Label-Free Correctness Signal
- 存在性: ✅ 真实存在
- 实际标题: Cross-Model Disagreement as a Label-Free Correctness Signal
- 作者: Matt Gorbett, Suman Jana
- Venue: arXiv preprint, March 2026
- arXiv ID: 2603.25450
- URL: https://arxiv.org/abs/2603.25450
- BibTeX:
```bibtex
@article{gorbett2026crossmodel,
  title={Cross-Model Disagreement as a Label-Free Correctness Signal},
  author={Gorbett, Matt and Jana, Suman},
  journal={arXiv preprint arXiv:2603.25450},
  year={2026}
}
```
- 与本文相关性: 提出 Cross-Model Perplexity/Entropy 作为无标签正确性信号，与 §4.3 per-example divergence 的思路有交叉但角度不同——他们聚焦 deployment monitoring/selective prediction，本文聚焦 fine-tuning gating。可以在 Related Work 中讨论。

---

## 论文 2: The Hidden Attention of Mamba Models
- 存在性: ✅ 真实存在
- 实际标题: The Hidden Attention of Mamba Models
- 作者: Ameen Ali, Itamar Zimerman, Lior Wolf
- Venue: ACL 2025 (Long Paper)
- arXiv ID: 2403.01590
- URL: https://aclanthology.org/2025.acl-long.76/
- BibTeX:
```bibtex
@inproceedings{ali2025hidden,
  title={The Hidden Attention of Mamba Models},
  author={Ali, Ameen and Zimerman, Itamar and Wolf, Lior},
  booktitle={Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (ACL)},
  year={2025}
}
```
- 与本文相关性: 揭示 Mamba SSM 可等价为隐式 attention，与 Appendix D attention pattern analysis 方法论相关。如果 Appendix D 分析了 SSM-based 模型的 attention patterns，应当引用。

---

## 论文 3: Reconciling Model Multiplicity for Downstream Decision Making
- 存在性: ✅ 真实存在
- 实际标题: Reconciling Model Multiplicity for Downstream Decision Making
- 作者: Ally Yalei Du, Dung Daniel Ngo, Zhiwei Steven Wu
- Venue: ICLR 2025
- arXiv ID: 2405.19667
- URL: https://openreview.net/forum?id=uy4EavBEwl
- BibTeX:
```bibtex
@inproceedings{du2025reconciling,
  title={Reconciling Model Multiplicity for Downstream Decision Making},
  author={Du, Ally Yalei and Ngo, Dung Daniel and Wu, Zhiwei Steven},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2025}
}
```
- 与本文相关性: 直接处理 predictive multiplicity 下的 model reconciliation，与本文 entrainment gating 框架在 multiplicity 层面有理论联系。建议引用。

---

## 论文 4: Resolving Predictive Multiplicity for the Rashomon Set
- 存在性: ✅ 真实存在
- 实际标题: Resolving Predictive Multiplicity for the Rashomon Set
- 作者: Parian Haghighat, Hadis Anahideh, Cynthia Rudin
- Venue: arXiv preprint, January 2026
- arXiv ID: 2601.09071
- URL: https://arxiv.org/abs/2601.09071
- BibTeX:
```bibtex
@article{haghighat2026resolving,
  title={Resolving Predictive Multiplicity for the Rashomon Set},
  author={Haghighat, Parian and Anahideh, Hadis and Rudin, Cynthia},
  journal={arXiv preprint arXiv:2601.09071},
  year={2026}
}
```
- 与本文相关性: Rashomon set 上通过 outlier correction + local patching 降低 multiplicity，是 predictive multiplicity 理论的最新进展。如果本文涉及 Rashomon set 或 multiplicity resolution，应引用。

---

## 论文 5: Mamba-3
- 存在性: ✅ 真实存在
- 实际标题: Mamba-3: Improved Sequence Modeling using State Space Principles
- 作者: Aakash Lahoti, Kevin Y. Li, Berlin Chen, Caitlin Wang, Aviv Bick, J. Zico Kolter, Tri Dao, Albert Gu
- Venue: ICLR 2026
- arXiv ID: 2603.15569
- URL: https://openreview.net/forum?id=HwCvaJOiCj
- BibTeX:
```bibtex
@inproceedings{lahoti2026mamba3,
  title={Mamba-3: Improved Sequence Modeling using State Space Principles},
  author={Lahoti, Aakash and Li, Kevin Y. and Chen, Berlin and Wang, Caitlin and Bick, Aviv and Kolter, J. Zico and Dao, Tri and Gu, Albert},
  booktitle={Proceedings of the International Conference on Learning Representations (ICLR)},
  year={2026}
}
```
- 与本文相关性: 最新 hybrid SSM architecture，如果本文实验涉及 Mamba 系列模型或讨论 hybrid architectures，可在 Related Work 中提及作为最新进展。

---

## 论文 6: D'Amour et al. Underspecification 年份验证
- 存在性: ⚠️ 存在，审稿人年份质疑不成立
- 实际情况:
  - arXiv 预印本: 2020 年 11 月 6 日 (arXiv:2011.03395)
  - JMLR 正式发表: 2022 年, Volume 23, Issue 226, pp. 1–61
- **结论: 当前 bib 引用 JMLR 2022 是正确的。** 审稿人说"应为 2020"是混淆了 arXiv 预印本日期和正式发表日期。学术引用应以正式发表版本为准。
- URL: https://www.jmlr.org/papers/v23/20-1335.html
- 当前 BibTeX 无需修改。

---

## 总结

| # | 论文 | 存在性 | 审稿人信息准确度 |
|---|------|--------|-----------------|
| 1 | Cross-Model Disagreement | ✅ 真实 | arXiv ID、年份均正确 |
| 2 | Hidden Attention of Mamba | ✅ 真实 | Venue、年份均正确 |
| 3 | Reconciling Model Multiplicity | ✅ 真实 | Venue、年份均正确 |
| 4 | Resolving Predictive Multiplicity | ✅ 真实 | arXiv ID、年份均正确 |
| 5 | Mamba-3 | ✅ 真实 | Venue、年份均正确 |
| 6 | D'Amour underspecification | ⚠️ 审稿人有误 | JMLR 2022 正确，非 2020 |

**5 篇遗漏引用全部真实存在**，非 AI 幻觉。论文 6 的年份质疑不成立，当前 bib 无需修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 74958,
  "duration_api_ms": 114706,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "4dd870c8-18ba-46bc-822a-2620514d1627",
  "total_cost_usd": 0.4448915,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 20254,
    "cache_read_input_tokens": 90792,
    "output_tokens": 3804,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 20254,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 2618,
        "cache_read_input_tokens": 29937,
        "cache_creation_input_tokens": 2158,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2158
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 79798,
      "outputTokens": 3595,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 8,
      "costUSD": 0.17777300000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 3804,
      "cacheReadInputTokens": 90792,
      "cacheCreationInputTokens": 20254,
      "webSearchRequests": 0,
      "costUSD": 0.2671185,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "013757a0-02cd-4b84-afc2-73e1ace4c793"
}
```

</details>

---
