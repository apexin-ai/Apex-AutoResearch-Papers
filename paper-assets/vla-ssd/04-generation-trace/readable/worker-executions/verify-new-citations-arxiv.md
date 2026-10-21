# verify new citations arxiv

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 0
- **Tool calls:** 6
- **Original source:** `logs/workers/worker_verify_new_citations_arxiv_20260524T013515.log`
- **Structured JSON:** [`3a33a8e94a5f86d0cb47.json`](../../sessions/3a/3a33a8e94a5f86d0cb47.json)

## Before a recorded user message

22 recorded events

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
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
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
  "uuid": "92300f83-7f3b-4cdf-9166-df860660d66f",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779593400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "8ab03e24-e8a0-46ca-b41e-e25c63f5a6ae",
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to verify two arXiv papers to check if they are real or hallucinated citations. I need to search for each paper using WebSearch. Let me load the WebSearch tool first.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "de25f264-17a9-4e58-a04a-b13722c4f09b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3YSYyb4tXxdwRRg8xn2KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11474,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11474
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01TdoVDUVjk2fZV9YLAMSGpn`</summary>

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
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "3ddf03f0-27bf-4259-a53e-1c6ed44269ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01J3YSYyb4tXxdwRRg8xn2KJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11474,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11474
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

_source line 6 · 2026-05-24T01:35:25.878Z_

<details><summary>↩ Tool result · `toolu_01TdoVDUVjk2fZV9YLAMSGpn`</summary>

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
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "7f601653-4c84-488e-8883-d75c54d53e5d",
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

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Now let me search for both papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "b5c49d82-92a6-40b6-b356-be818eeae613",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 8_

开始验证两篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "46b1adc7-86b5-4fcc-8aaa-52644f2b1ca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NaSYgoS2SBZxnvfmfyDtrR`</summary>

```json
{
  "query": "arXiv 2603.03818"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "0d5feede-0197-4a6a-8759-a33599128a5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014xvYKs6LGCwDV5wGH6xZyR`</summary>

```json
{
  "query": "arXiv 2509.11417"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "6eb458ca-3eed-4daf-94b0-a5fcfb4958d3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MZDFut4HGDm23JkGYEDNrr`</summary>

```json
{
  "query": "Pretrained VLAs Resistant to Forgetting continual learning arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "eb786c9f-b313-4ef9-a8fb-2cb8ef53c691",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFUkSSN4b7irXozyqjgifd`</summary>

```json
{
  "query": "Enhancing Generalization VLA Preserving Pretrained Representations arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "562edf72-ae8f-4c08-8b51-099d8c0dc9ec",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y5jnRqD26wWkTQXYvMLtVe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 662,
      "cache_read_input_tokens": 23315,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 662
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

_source line 13 · 2026-05-24T01:35:42.711Z_

<details><summary>↩ Tool result · `toolu_01NaSYgoS2SBZxnvfmfyDtrR`</summary>

```text
Web search results for query: "arXiv 2603.03818"

Links: [{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818"},{"title":"Accurate PROTAC targeted degradation prediction with DegradeMaster","url":"https://www.biorxiv.org/content/10.1101/2025.02.03.636343.full.pdf"},{"title":"Accurate Prediction of Protein Complex Stoichiometry by Integrating AlphaFold3 and Template Information","url":"https://www.biorxiv.org/content/10.1101/2025.01.12.632663.full.pdf"},{"title":"[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/abs/2603.03818"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"Enhanced sampling of protein conformations in AlphaFold3 with repulsive bias in the diffusion generative model","url":"https://www.biorxiv.org/content/10.64898/2025.12.17.693105.full.pdf"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly","url":"https://arxiv.org/pdf/2603.03818"},{"title":"AutoPM3: Enhancing Variant Interpretation via LLM-driven PM3 Evidence Extraction from Scientific Literature","url":"https://www.biorxiv.org/content/10.1101/2024.10.29.621006.full.pdf"}]

Based on the search results, arXiv:2603.03818 is a paper by Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, and Yuke Zhu, published on March 17, 2026, titled "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning".

The paper addresses continual learning in robot policy learning, finding that pretrained Vision-Language-Action (VLA) models are remarkably resistant to forgetting compared with smaller policy models trained from scratch. The researchers found that simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "d5057382-0e0c-4e42-8114-acab3a07f1c6",
  "tool_use_result": {
    "query": "arXiv 2603.03818",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HMme4nz5SU2ozXVTBWxBXW",
        "content": [
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/html/2603.03818"
          },
          {
            "title": "Accurate PROTAC targeted degradation prediction with DegradeMaster",
            "url": "https://www.biorxiv.org/content/10.1101/2025.02.03.636343.full.pdf"
          },
          {
            "title": "Accurate Prediction of Protein Complex Stoichiometry by Integrating AlphaFold3 and Template Information",
            "url": "https://www.biorxiv.org/content/10.1101/2025.01.12.632663.full.pdf"
          },
          {
            "title": "[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/abs/2603.03818"
          },
          {
            "title": "my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"
          },
          {
            "title": "Enhanced sampling of protein conformations in AlphaFold3 with repulsive bias in the diffusion generative model",
            "url": "https://www.biorxiv.org/content/10.64898/2025.12.17.693105.full.pdf"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly",
            "url": "https://arxiv.org/pdf/2603.03818"
          },
          {
            "title": "AutoPM3: Enhancing Variant Interpretation via LLM-driven PM3 Evidence Extraction from Scientific Literature",
            "url": "https://www.biorxiv.org/content/10.1101/2024.10.29.621006.full.pdf"
          }
        ]
      },
      "Based on the search results, arXiv:2603.03818 is a paper by Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, and Yuke Zhu, published on March 17, 2026, titled \"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning\".\n\nThe paper addresses continual learning in robot policy learning, finding that pretrained Vision-Language-Action (VLA) models are remarkably resistant to forgetting compared with smaller policy models trained from scratch. The researchers found that simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size."
    ],
    "durationSeconds": 6.011414467999999
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T01:35:42.737Z_

<details><summary>↩ Tool result · `toolu_014xvYKs6LGCwDV5wGH6xZyR`</summary>

```text
Web search results for query: "arXiv 2509.11417"

Links: [{"title":"Deubiquitylation and stabilization of p21 by USP11 is critical for cell cycle progression and DNA damage responses","url":"https://www.biorxiv.org/content/10.1101/172999.full.pdf"},{"title":"Large language models for abstract screening in systematic- and scoping reviews: A diagnostic test accuracy study","url":"https://www.medrxiv.org/content/10.1101/2024.10.01.24314702.full.pdf"},{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"System and method for resisting quantum perturbation threats to quantum communication devices","url":"https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11863989"},{"title":"On-target toxicity limits the efficacy of CDK11 inhibition against cancers with 1p36 deletions","url":"https://www.biorxiv.org/content/10.1101/2025.08.03.668359.full.pdf"}]

Based on the search results, arXiv paper 2509.11417 is titled "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" and discusses how vision-language-action (VLA) models finetuned from vision-language models (VLMs) can leverage rich pretrained representations to build generalist robots.

The paper addresses the problem that direct fine-tuning on robot data often disrupts pretrained representations and limits generalization, and presents a framework that better preserves pretrained features while adapting them for robot manipulation.

The approach introduces three key components: a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.

The paper was published on September 14, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "ca43e8d7-ba6e-4131-8c8b-a79302753854",
  "tool_use_result": {
    "query": "arXiv 2509.11417",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MD3KGWgArmkexeyix8YcCZ",
        "content": [
          {
            "title": "Deubiquitylation and stabilization of p21 by USP11 is critical for cell cycle progression and DNA damage responses",
            "url": "https://www.biorxiv.org/content/10.1101/172999.full.pdf"
          },
          {
            "title": "Large language models for abstract screening in systematic- and scoping reviews: A diagnostic test accuracy study",
            "url": "https://www.medrxiv.org/content/10.1101/2024.10.01.24314702.full.pdf"
          },
          {
            "title": "[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/abs/2509.11417"
          },
          {
            "title": "System and method for resisting quantum perturbation threats to quantum communication devices",
            "url": "https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/11863989"
          },
          {
            "title": "On-target toxicity limits the efficacy of CDK11 inhibition against cancers with 1p36 deletions",
            "url": "https://www.biorxiv.org/content/10.1101/2025.08.03.668359.full.pdf"
          }
        ]
      },
      "Based on the search results, arXiv paper 2509.11417 is titled \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" and discusses how vision-language-action (VLA) models finetuned from vision-language models (VLMs) can leverage rich pretrained representations to build generalist robots.\n\nThe paper addresses the problem that direct fine-tuning on robot data often disrupts pretrained representations and limits generalization, and presents a framework that better preserves pretrained features while adapting them for robot manipulation.\n\nThe approach introduces three key components: a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.\n\nThe paper was published on September 14, 2025."
    ],
    "durationSeconds": 5.534230366
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-24T01:35:43.385Z_

<details><summary>↩ Tool result · `toolu_01MZDFut4HGDm23JkGYEDNrr`</summary>

```text
Web search results for query: "Pretrained VLAs Resistant to Forgetting continual learning arXiv"

Links: [{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | alphaXiv","url":"https://www.alphaxiv.org/overview/2603.03818"},{"title":"[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/abs/2603.03818"},{"title":"Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://continual-vlas.github.io/forget-me-not/"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning","url":"https://arxiv.org/html/2603.03818"},{"title":"Pretrained Vision-Language-Action Models are Surprisingly","url":"https://arxiv.org/pdf/2603.03818"},{"title":"Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning","url":"https://arxiv.org/pdf/2602.10503"}]

I found the paper you're looking for! Here are the key findings:

**Paper Details:**
The paper is titled "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning" by Huihan Liu and 4 other authors, and it found that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch.

**Main Findings:**
- Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size.
- Pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities.
- The effectiveness of ER is consistent across multiple VLAs (Pi0, GR00T N1.5) despite differences in architecture, parameter count, and pretraining recipes, suggesting that effectiveness is a general property of pretrained VLAs.

The paper was published on March 17, 2026, and is available on arXiv as 2603.03818. You can access it at https://arxiv.org/abs/2603.03818.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "6b90d7f9-f4b7-4623-a511-6211bd8d1c56",
  "tool_use_result": {
    "query": "Pretrained VLAs Resistant to Forgetting continual learning arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JtymsVQEitS2hJe1kvGe8i",
        "content": [
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2603.03818"
          },
          {
            "title": "[2603.03818] Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/abs/2603.03818"
          },
          {
            "title": "Pretrained VLAs are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://continual-vlas.github.io/forget-me-not/"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning",
            "url": "https://arxiv.org/html/2603.03818"
          },
          {
            "title": "Pretrained Vision-Language-Action Models are Surprisingly",
            "url": "https://arxiv.org/pdf/2603.03818"
          },
          {
            "title": "Towards Long-Lived Robots: Continual Learning VLA Models via Reinforcement Fine-Tuning",
            "url": "https://arxiv.org/pdf/2602.10503"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key findings:\n\n**Paper Details:**\nThe paper is titled \"Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning\" by Huihan Liu and 4 other authors, and it found that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch.\n\n**Main Findings:**\n- Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size.\n- Pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities.\n- The effectiveness of ER is consistent across multiple VLAs (Pi0, GR00T N1.5) despite differences in architecture, parameter count, and pretraining recipes, suggesting that effectiveness is a general property of pretrained VLAs.\n\nThe paper was published on March 17, 2026, and is available on arXiv as 2603.03818. You can access it at https://arxiv.org/abs/2603.03818."
    ],
    "durationSeconds": 5.594960592
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-24T01:35:44.136Z_

<details><summary>↩ Tool result · `toolu_01CFUkSSN4b7irXozyqjgifd`</summary>

```text
Web search results for query: "Enhancing Generalization VLA Preserving Pretrained Representations arXiv"

Links: [{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Enhancing Generalization in Vision-Language-Action Models","url":"https://gen-vla.github.io/"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417v1"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/abs/2511.19878"},{"title":"MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization","url":"https://arxiv.org/pdf/2511.19878"}]

I found the paper you're looking for! Here are the search results:

## Primary Result

The paper "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" is arXiv paper 2509.11417, published in September 2025.

## Paper Overview

Vision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization.

## Key Contributions

The approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.

The paper has been published on arXiv and includes both simulation and real-world evaluations demonstrating improvements in robustness and generalization for robotic manipulation tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "aeaf9a87-841a-40bc-8c1d-b90f0126e25b",
  "tool_use_result": {
    "query": "Enhancing Generalization VLA Preserving Pretrained Representations arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017LNT8gKTRer6pKUNxa5UAM",
        "content": [
          {
            "title": "[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/abs/2509.11417"
          },
          {
            "title": "Enhancing Generalization in Vision-Language-Action Models",
            "url": "https://gen-vla.github.io/"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/html/2509.11417v1"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by",
            "url": "https://arxiv.org/pdf/2509.11417"
          },
          {
            "title": "[2511.19878] MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization",
            "url": "https://arxiv.org/abs/2511.19878"
          },
          {
            "title": "MAPS: Preserving Vision-Language Representations via Module-Wise Proximity Scheduling for Better Vision-Language-Action Generalization",
            "url": "https://arxiv.org/pdf/2511.19878"
          }
        ]
      },
      "I found the paper you're looking for! Here are the search results:\n\n## Primary Result\n\nThe paper \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" is arXiv paper 2509.11417, published in September 2025.\n\n## Paper Overview\n\nVision-language-action (VLA) models finetuned from vision-language models (VLMs) hold the promise of leveraging rich pretrained representations to build generalist robots across diverse tasks and environments. However, direct fine-tuning on robot data often disrupts these representations and limits generalization.\n\n## Key Contributions\n\nThe approach introduces three components: (i) a dual-encoder design with one frozen vision encoder to retain pretrained features and another trainable for task adaptation, (ii) a string-based action tokenizer that casts continuous actions into character sequences aligned with the model's pretraining domain, and (iii) a co-training strategy that combines robot demonstrations with vision-language datasets emphasizing spatial reasoning and affordances.\n\nThe paper has been published on arXiv and includes both simulation and real-world evaluations demonstrating improvements in robustness and generalization for robotic manipulation tasks."
    ],
    "durationSeconds": 5.945332504000001
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Now let me verify the author details for both papers more carefully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "c892114e-4d0b-49d7-84ad-2e48b7fd7ab7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBFQpQn3WdYv6cwjjQbVoP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2722,
      "cache_read_input_tokens": 23977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2722
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

_source line 18_

现在确认作者信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "89beb617-5486-49ff-9d49-2c866021550e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBFQpQn3WdYv6cwjjQbVoP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2722,
      "cache_read_input_tokens": 23977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2722
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

_source line 19_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TwARLoLj5SeUYFtWCBLL6A`</summary>

```json
{
  "query": "arxiv 2509.11417 authors Grover Gopalkrishnan Ai Christensen"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "6be05059-3fb3-49f1-9bb5-ca97a30eb0ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBFQpQn3WdYv6cwjjQbVoP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2722,
      "cache_read_input_tokens": 23977,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2722
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

_source line 20 · 2026-05-24T01:35:55.093Z_

<details><summary>↩ Tool result · `toolu_01TwARLoLj5SeUYFtWCBLL6A`</summary>

```text
Web search results for query: "arxiv 2509.11417 authors Grover Gopalkrishnan Ai Christensen"

Links: [{"title":"[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/abs/2509.11417"},{"title":"Identification and functional characterization of two CXCL17 paralogs from zebrafish","url":"https://www.biorxiv.org/content/10.1101/2025.08.27.672743.full.pdf"},{"title":"Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations","url":"https://arxiv.org/html/2509.11417"},{"title":"Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans","url":"https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"},{"title":"Enhancing Generalization in Vision–Language–Action Models by","url":"https://arxiv.org/pdf/2509.11417"},{"title":"Identification of the orphan GPR25 as a receptor of the chemokine CXCL17","url":"https://www.biorxiv.org/content/10.1101/2024.09.21.614233.full.pdf"}]

Based on the search results, I found the paper you're looking for:

The paper arxiv 2509.11417 is titled "Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations" and is authored by Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, and Xuanlin Li.

The authors are affiliated with UC San Diego and Hillbot. The paper addresses how vision-language-action (VLA) models finetuned from vision-language models (VLMs) can leverage pretrained representations to build generalist robots, and presents a framework that better preserves pretrained features while adapting them for robot manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "5d4e834e-d4ea-4c8f-94f9-0782d60faf7d",
  "tool_use_result": {
    "query": "arxiv 2509.11417 authors Grover Gopalkrishnan Ai Christensen",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QW6tiU4wS2nxjC35BMRvpV",
        "content": [
          {
            "title": "[2509.11417] Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/abs/2509.11417"
          },
          {
            "title": "Identification and functional characterization of two CXCL17 paralogs from zebrafish",
            "url": "https://www.biorxiv.org/content/10.1101/2025.08.27.672743.full.pdf"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by Preserving Pretrained Representations",
            "url": "https://arxiv.org/html/2509.11417"
          },
          {
            "title": "Sample-Efficient Deep Learning for COVID-19 Diagnosis Based on CT Scans",
            "url": "https://www.medrxiv.org/content/10.1101/2020.04.13.20063941.full.pdf"
          },
          {
            "title": "Enhancing Generalization in Vision–Language–Action Models by",
            "url": "https://arxiv.org/pdf/2509.11417"
          },
          {
            "title": "Identification of the orphan GPR25 as a receptor of the chemokine CXCL17",
            "url": "https://www.biorxiv.org/content/10.1101/2024.09.21.614233.full.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe paper arxiv 2509.11417 is titled \"Enhancing Generalization in Vision-Language-Action Models by Preserving Pretrained Representations\" and is authored by Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, and Xuanlin Li.\n\nThe authors are affiliated with UC San Diego and Hillbot. The paper addresses how vision-language-action (VLA) models finetuned from vision-language models (VLMs) can leverage pretrained representations to build generalist robots, and presents a framework that better preserves pretrained features while adapting them for robot manipulation."
    ],
    "durationSeconds": 4.932226560000003
  }
}
```

</details>

---

### Assistant

_source line 21_

两篇论文均已验证完毕。

---

## 论文 1: "Pretrained VLAs are Surprisingly Resistant to Forgetting"
- **arXiv ID 有效**: 是 — [2603.03818](https://arxiv.org/abs/2603.03818) 存在
- **标题准确**: 部分 — 实际标题为 "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning"（声称标题是缩写版）
- **作者匹配**: 是 — Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- **内容摘要**: Pretrained VLAs 在 continual learning 中对遗忘有极强抵抗力；简单的 Experience Replay (ER) 即可实现接近零遗忘；在 Pi0、GR00T N1.5 等多种 VLA 上一致成立
- **发表时间**: 2026年3月17日 ✓
- **结论**: **真实论文** ✓

---

## 论文 2: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **arXiv ID 有效**: 是 — [2509.11417](https://arxiv.org/abs/2509.11417) 存在
- **标题准确**: 部分 — 实际标题为 "Enhancing Generalization in **Vision-Language-Action** Models by Preserving Pretrained Representations"（声称标题用了缩写 VLA）
- **作者匹配**: 是 — Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, Xuanlin Li（声称的姓氏列表匹配，缺了 Xuanlin Li）
- **内容摘要**: VLM→VLA fine-tuning 会破坏 pretrained representations，提出 (1) dual-encoder（一个 frozen + 一个 trainable）, (2) string-based action tokenizer, (3) co-training strategy 结合 robot demo 和 VL 数据集
- **发表时间**: 2025年9月14日 ✓
- **结论**: **真实论文** ✓（作者列表少列了 Li，其余准确）

---

两篇均为真实论文，可安全引用。建议在正式引用时使用完整标题和完整作者列表。

Sources:
- [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- [Continual VLAs project page](https://continual-vlas.github.io/forget-me-not/)
- [Gen-VLA project page](https://gen-vla.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "uuid": "249b2cd9-a57c-49f9-bba9-49a12e47b026",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WpNdVLmEgyb74mAggjjqAp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 659,
      "cache_read_input_tokens": 26699,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 659
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

_source line 22_

两篇论文均已验证完毕。

---

## 论文 1: "Pretrained VLAs are Surprisingly Resistant to Forgetting"
- **arXiv ID 有效**: 是 — [2603.03818](https://arxiv.org/abs/2603.03818) 存在
- **标题准确**: 部分 — 实际标题为 "Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning"（声称标题是缩写版）
- **作者匹配**: 是 — Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu
- **内容摘要**: Pretrained VLAs 在 continual learning 中对遗忘有极强抵抗力；简单的 Experience Replay (ER) 即可实现接近零遗忘；在 Pi0、GR00T N1.5 等多种 VLA 上一致成立
- **发表时间**: 2026年3月17日 ✓
- **结论**: **真实论文** ✓

---

## 论文 2: "Enhancing Generalization in VLA Models by Preserving Pretrained Representations"
- **arXiv ID 有效**: 是 — [2509.11417](https://arxiv.org/abs/2509.11417) 存在
- **标题准确**: 部分 — 实际标题为 "Enhancing Generalization in **Vision-Language-Action** Models by Preserving Pretrained Representations"（声称标题用了缩写 VLA）
- **作者匹配**: 是 — Shresth Grover, Akshay Gopalkrishnan, Bo Ai, Henrik I. Christensen, Hao Su, Xuanlin Li（声称的姓氏列表匹配，缺了 Xuanlin Li）
- **内容摘要**: VLM→VLA fine-tuning 会破坏 pretrained representations，提出 (1) dual-encoder（一个 frozen + 一个 trainable）, (2) string-based action tokenizer, (3) co-training strategy 结合 robot demo 和 VL 数据集
- **发表时间**: 2025年9月14日 ✓
- **结论**: **真实论文** ✓（作者列表少列了 Li，其余准确）

---

两篇均为真实论文，可安全引用。建议在正式引用时使用完整标题和完整作者列表。

Sources:
- [arXiv 2603.03818](https://arxiv.org/abs/2603.03818)
- [arXiv 2509.11417](https://arxiv.org/abs/2509.11417)
- [Continual VLAs project page](https://continual-vlas.github.io/forget-me-not/)
- [Gen-VLA project page](https://gen-vla.github.io/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 50817,
  "duration_api_ms": 70319,
  "num_turns": 7,
  "stop_reason": "end_turn",
  "session_id": "3062f603-ba36-4da7-a7f5-ed0195e13e0b",
  "total_cost_usd": 0.27699824999999995,
  "usage": {
    "input_tokens": 8,
    "cache_creation_input_tokens": 15517,
    "cache_read_input_tokens": 85832,
    "output_tokens": 1284,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 15517,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 793,
        "cache_read_input_tokens": 26699,
        "cache_creation_input_tokens": 659,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 659
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 46656,
      "outputTokens": 1661,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 5,
      "costUSD": 0.10496100000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 8,
      "outputTokens": 1284,
      "cacheReadInputTokens": 85832,
      "cacheCreationInputTokens": 15517,
      "webSearchRequests": 0,
      "costUSD": 0.17203725,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8d6cedbe-6f49-4d1f-8d46-4f9fce919681"
}
```

</details>

---
