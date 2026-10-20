# research pride formula verify

**afford invar** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_research_pride-formula-verify_20260519T232737.log`
- **Structured JSON:** [`a8ab625472bb08a66ea7.json`](../../sessions/a8/a8ab625472bb08a66ea7.json)

## Before a recorded user message

61 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
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
  "uuid": "20574c23-b22d-4d3a-b127-4bd10d6ea8b0",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-5/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-afford-invar/memory/"
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
    "resetsAt": 1779244200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "9cf0ae92-f768-481c-b0eb-5d0bfb869e30",
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e"
}
```

---

### Assistant

_source line 4_

I'll search for the PRIDE metric definition and the referenced paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "a4295277-cdc1-4e50-8166-9da380aeaaa1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRa1kDSu9QWkFV8zxsoxEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11157,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11157
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015r7tfUqYqMNCysZH7Ho79D`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "ec70bbe8-bfb3-40fb-bcc6-1123b661184f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PRa1kDSu9QWkFV8zxsoxEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11157,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11157
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

_source line 6 · 2026-05-19T23:27:48.668Z_

<details><summary>↩ Tool result · `toolu_015r7tfUqYqMNCysZH7Ho79D`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "e3fa55c9-909d-44c0-9a7e-08dfa8fc720b",
  "tool_use_result": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
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
Let me search for the PRIDE metric and the referenced paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "420776c3-c85d-4c81-a726-291241e91b61",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfbdsXVVrPLDYeZyK3YPPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 22998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
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

### Tool call

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01N7HqmFLzS4nKf1s8AQvF3m`</summary>

```json
{
  "query": "PRIDE metric LIBERO paraphrase robustness VLA"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "eb611581-4fb2-4df9-9772-bd7c70160b77",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfbdsXVVrPLDYeZyK3YPPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 22998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
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

### Tool call

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0142W5uS4YoQ6Zu4CBW2y3KC`</summary>

```json
{
  "query": "arXiv 2603.28301"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "fef725fc-fb39-480c-8ea9-47319e55d014",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UfbdsXVVrPLDYeZyK3YPPY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 619,
      "cache_read_input_tokens": 22998,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 619
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

_source line 10 · 2026-05-19T23:27:58.891Z_

<details><summary>↩ Tool result · `toolu_01N7HqmFLzS4nKf1s8AQvF3m`</summary>

```text
Web search results for query: "PRIDE metric LIBERO paraphrase robustness VLA"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"paraphrase · GitHub Topics · GitHub","url":"https://github.com/topics/paraphrase"}]

Based on the search results, here's what I found:

PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) is a metric that combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis.

PRIDE quantifies paraphrase difficulty using semantic and syntactic factors, and it is a difficulty-aware metric that goes beyond binary success rate, giving more credit for succeeding on harder paraphrases.

PRIDE was introduced as part of LIBERO-Para, a controlled benchmark for evaluating paraphrase robustness in VLA (Vision-Language-Action) models. LIBERO-Para is grounded in the linguistic structure of robotic manipulation instructions—where actions and objects serve as core semantic elements—and adopts a two-axis design that independently varies action expressions and object references.

The research addresses a key finding: degradation is primarily driven by object-level lexical variation; even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rather than semantic grounding.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "35f0b9f0-1b23-40e8-b6e3-564fe5e46031",
  "tool_use_result": {
    "query": "PRIDE metric LIBERO paraphrase robustness VLA",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EryzW3eBNcprYQH6AgZqMG",
        "content": [
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://cau-hai-lab.github.io/LIBERO-Para/"
          },
          {
            "title": "GitHub - cau-hai-lab/LIBERO-Para · GitHub",
            "url": "https://github.com/cau-hai-lab/LIBERO-Para"
          },
          {
            "title": "Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://huggingface.co/papers/2603.28301"
          },
          {
            "title": "paraphrase · GitHub Topics · GitHub",
            "url": "https://github.com/topics/paraphrase"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nPRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) is a metric that combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis.\n\nPRIDE quantifies paraphrase difficulty using semantic and syntactic factors, and it is a difficulty-aware metric that goes beyond binary success rate, giving more credit for succeeding on harder paraphrases.\n\nPRIDE was introduced as part of LIBERO-Para, a controlled benchmark for evaluating paraphrase robustness in VLA (Vision-Language-Action) models. LIBERO-Para is grounded in the linguistic structure of robotic manipulation instructions—where actions and objects serve as core semantic elements—and adopts a two-axis design that independently varies action expressions and object references.\n\nThe research addresses a key finding: degradation is primarily driven by object-level lexical variation; even simple synonym substitutions cause large drops, indicating reliance on surface-level matching rather than semantic grounding."
    ],
    "durationSeconds": 7.318055638
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-19T23:28:18.022Z_

<details><summary>↩ Tool result · `toolu_0142W5uS4YoQ6Zu4CBW2y3KC`</summary>

```text
Web search results for query: "arXiv 2603.28301"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"Immune escape and attenuated severity associated with the SARS-CoV-2 BA.2.86/JN.1 lineage","url":"https://www.medrxiv.org/content/10.1101/2024.04.17.24305964.full.pdf"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"Evolution and neutralization escape of the SARS-CoV-2 BA.2.86 subvariant","url":"https://www.medrxiv.org/content/10.1101/2023.09.08.23295250.full.pdf"},{"title":"Symphonizing pileup and full-alignment for deep learning-based long-read variant calling","url":"https://www.biorxiv.org/content/10.1101/2021.12.29.474431.full.pdf"}]

Based on the search results, arXiv 2603.28301 is a paper titled "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models" by Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, and Dahuin Jung, from Soongsil University and Chung-Ang University, published on March 30, 2026.

The paper introduces LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. The research addresses a gap in Vision-Language-Action (VLA) models, which are typically fine-tuned with limited data in downstream robotic settings, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. The study found consistent performance degradation of 22–52 percentage points under paraphrasing across seven VLA configurations ranging from 0.6B–7.5B parameters.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "025a8288-6189-4877-9a7e-77dbd8fe3a16",
  "tool_use_result": {
    "query": "arXiv 2603.28301",
    "results": [
      {
        "tool_use_id": "srvtoolu_01M7wZMtMpQUegy1JDkCU7c8",
        "content": [
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301"
          },
          {
            "title": "Immune escape and attenuated severity associated with the SARS-CoV-2 BA.2.86/JN.1 lineage",
            "url": "https://www.medrxiv.org/content/10.1101/2024.04.17.24305964.full.pdf"
          },
          {
            "title": "my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"
          },
          {
            "title": "Evolution and neutralization escape of the SARS-CoV-2 BA.2.86 subvariant",
            "url": "https://www.medrxiv.org/content/10.1101/2023.09.08.23295250.full.pdf"
          },
          {
            "title": "Symphonizing pileup and full-alignment for deep learning-based long-read variant calling",
            "url": "https://www.biorxiv.org/content/10.1101/2021.12.29.474431.full.pdf"
          }
        ]
      },
      "Based on the search results, arXiv 2603.28301 is a paper titled \"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\" by Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, and Dahuin Jung, from Soongsil University and Chung-Ang University, published on March 30, 2026.\n\nThe paper introduces LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. The research addresses a gap in Vision-Language-Action (VLA) models, which are typically fine-tuned with limited data in downstream robotic settings, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored. The study found consistent performance degradation of 22–52 percentage points under paraphrasing across seven VLA configurations ranging from 0.6B–7.5B parameters."
    ],
    "durationSeconds": 26.2417866
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
I found the paper. Now let me read the actual paper to get the precise PRIDE formula definition.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "99112b15-deba-4742-b627-e24f62528855",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2ssGd3vun3adQoUXLCMRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 23617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 13_

找到论文了，现在读取原文获取精确公式定义。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "1b4d55f9-fc28-4fe0-8412-d73ac747633c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2ssGd3vun3adQoUXLCMRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 23617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TAfxYtANHvCgGjoSwwUpNS`</summary>

```json
{
  "query": "PRIDE formula \"Paraphrase Robustness\" site:arxiv.org 2603.28301 SK ST alpha"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "7701857c-99d2-4ead-ba57-7a21a921c7c5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2ssGd3vun3adQoUXLCMRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 23617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AVGyxXosKYXAjqWMWyzXAz`</summary>

```json
{
  "query": "\"PRIDE\" \"paraphrase difficulty\" formula definition arxiv LIBERO-Para 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "0ffcc2f8-8969-4aef-ba5c-b1666c575055",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R2ssGd3vun3adQoUXLCMRz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1359,
      "cache_read_input_tokens": 23617,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1359
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

_source line 16 · 2026-05-19T23:28:30.748Z_

<details><summary>↩ Tool result · `toolu_01AVGyxXosKYXAjqWMWyzXAz`</summary>

```text
Web search results for query: ""PRIDE" "paraphrase difficulty" formula definition arxiv LIBERO-Para 2026"

Links: [{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"cau-hai-lab · GitHub","url":"https://github.com/cau-hai-lab"},{"title":"paraphrase · GitHub Topics · GitHub","url":"https://github.com/topics/paraphrase"}]

Based on the search results, I found detailed information about PRIDE and the LIBERO-Para benchmark.

PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors. More specifically, PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then measuring the ratio of PD-weighted successes to total possible PD, normalized to 0–100.

PRIDE combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis. Unlike plain success rate, PRIDE gives more credit for succeeding on harder, more deviated paraphrases.

This metric was introduced as part of the LIBERO-Para benchmark, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization in Vision-Language-Action (VLA) models. The paper was published on arXiv in March 2026 (arXiv:2603.28301).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "515b24ea-b577-4f8f-899f-9d78c94d8a49",
  "tool_use_result": {
    "query": "\"PRIDE\" \"paraphrase difficulty\" formula definition arxiv LIBERO-Para 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011941FGh9KM8FAJW2EmmKtF",
        "content": [
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          },
          {
            "title": "Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://huggingface.co/papers/2603.28301"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://cau-hai-lab.github.io/LIBERO-Para/"
          },
          {
            "title": "GitHub - cau-hai-lab/LIBERO-Para · GitHub",
            "url": "https://github.com/cau-hai-lab/LIBERO-Para"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "cau-hai-lab · GitHub",
            "url": "https://github.com/cau-hai-lab"
          },
          {
            "title": "paraphrase · GitHub Topics · GitHub",
            "url": "https://github.com/topics/paraphrase"
          }
        ]
      },
      "Based on the search results, I found detailed information about PRIDE and the LIBERO-Para benchmark.\n\nPRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors. More specifically, PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then measuring the ratio of PD-weighted successes to total possible PD, normalized to 0–100.\n\nPRIDE combines keyword similarity (lexical shift) and structural similarity (syntactic variation) with task success to enable fine-grained robustness analysis. Unlike plain success rate, PRIDE gives more credit for succeeding on harder, more deviated paraphrases.\n\nThis metric was introduced as part of the LIBERO-Para benchmark, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization in Vision-Language-Action (VLA) models. The paper was published on arXiv in March 2026 (arXiv:2603.28301)."
    ],
    "durationSeconds": 6.303324093999996
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-19T23:28:32.486Z_

<details><summary>↩ Tool result · `toolu_01TAfxYtANHvCgGjoSwwUpNS`</summary>

```text
Web search results for query: "PRIDE formula "Paraphrase Robustness" site:arxiv.org 2603.28301 SK ST alpha"

Links: [{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"Robustness to Modification with Shared Words in Paraphrase   Identification","url":"https://arxiv.org/pdf/1909.02560"},{"title":"Evaluating Paraphrastic Robustness in Textual Entailment Models","url":"https://arxiv.org/pdf/2306.16722"},{"title":"RoParQ: Paraphrase-Aware Alignment of Large Language Models Towards Robustness to Paraphrased Questions","url":"https://arxiv.org/pdf/2511.21568"},{"title":"Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing","url":"https://arxiv.org/pdf/2511.12784"}]

Based on the search results, I found information about the PRIDE formula from the arxiv paper 2603.28301:

PRIDE is a metric that quantifies the linguistic deviation between an original instruction and its paraphrase. PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors.

The paper is titled "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models" and was published on March 30, 2026. However, the search results don't contain detailed information about the specific formula components you mentioned (SK, ST, alpha). To get the complete mathematical definition of the PRIDE formula with those specific parameters, you would need to access the full paper at https://arxiv.org/html/2603.28301v1 or https://arxiv.org/pdf/2603.28301.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "f8a6616e-feb9-4808-87c3-3a7e782bb74c",
  "tool_use_result": {
    "query": "PRIDE formula \"Paraphrase Robustness\" site:arxiv.org 2603.28301 SK ST alpha",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UAjpqCfo6xSEZFZ3h4Ue4g",
        "content": [
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301v1"
          },
          {
            "title": "Robustness to Modification with Shared Words in Paraphrase   Identification",
            "url": "https://arxiv.org/pdf/1909.02560"
          },
          {
            "title": "Evaluating Paraphrastic Robustness in Textual Entailment Models",
            "url": "https://arxiv.org/pdf/2306.16722"
          },
          {
            "title": "RoParQ: Paraphrase-Aware Alignment of Large Language Models Towards Robustness to Paraphrased Questions",
            "url": "https://arxiv.org/pdf/2511.21568"
          },
          {
            "title": "Evaluating Autoformalization Robustness via Semantically Similar Paraphrasing",
            "url": "https://arxiv.org/pdf/2511.12784"
          }
        ]
      },
      "Based on the search results, I found information about the PRIDE formula from the arxiv paper 2603.28301:\n\nPRIDE is a metric that quantifies the linguistic deviation between an original instruction and its paraphrase. PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors.\n\nThe paper is titled \"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models\" and was published on March 30, 2026. However, the search results don't contain detailed information about the specific formula components you mentioned (SK, ST, alpha). To get the complete mathematical definition of the PRIDE formula with those specific parameters, you would need to access the full paper at https://arxiv.org/html/2603.28301v1 or https://arxiv.org/pdf/2603.28301."
    ],
    "durationSeconds": 8.605916824
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
I need to get the actual formula details. Let me try to access the HTML version of the paper or the project page to get the exact formula.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "78b728a2-212d-4e3e-96ba-726da67062bf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N8FxRYMiRiBzcrRyrJzHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 655,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 24976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
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

搜索结果给出了概述但缺少精确公式。让我直接获取论文HTML页面和GitHub代码。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "5b237e65-0b4a-4b40-8282-f6fa3f9ee0dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N8FxRYMiRiBzcrRyrJzHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 655,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 24976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01NGcoNe8BYk4j1X3wP8rRHM`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "cedb99aa-277c-433f-8738-b058d1df267d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013N8FxRYMiRiBzcrRyrJzHo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 655,
      "cache_creation_input_tokens": 710,
      "cache_read_input_tokens": 24976,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 710
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

_source line 21 · 2026-05-19T23:28:39.133Z_

<details><summary>↩ Tool result · `toolu_01NGcoNe8BYk4j1X3wP8rRHM`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "5bfefdd6-2d6a-457b-9483-57c8e18e2c9b",
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

_source line 22_

<details open><summary>🔧 Tool call — WebFetch · `toolu_014XYf1CGizZoDc3HRkJobgi`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28301v1",
  "prompt": "Extract the EXACT mathematical formula/definition of PRIDE metric, including:\n1. The full formula for Paraphrase Distance (PD) - what is SK, ST, alpha, and how they combine\n2. The full formula for PRIDE score itself\n3. The default value of alpha\n4. Whether PRIDE is higher=better or lower=better\n5. What SK (keyword similarity) and ST (structural similarity) precisely measure and how they are computed\n6. The OFT baseline PRIDE score reported in the paper\n7. Any other baseline PRIDE scores reported\n\nBe very precise about the math - extract exact equations, not paraphrases."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "c00c1826-97e8-4a70-a103-23bae00465cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW9KBbRyWzVRvys8rhs5ow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1330,
      "cache_read_input_tokens": 25686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1330
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

### Tool call

_source line 23_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01GKHX45XVuWUY2qNNrtcmGX`</summary>

```json
{
  "url": "https://github.com/cau-hai-lab/LIBERO-Para",
  "prompt": "Find the implementation of the PRIDE metric. Look for:\n1. The code that computes PD (Paraphrase Distance) from SK and ST\n2. The code that computes the final PRIDE score\n3. The default alpha value\n4. Any constants or thresholds used\nExtract the relevant code snippets."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "29158fe8-b500-4086-b1da-0b1a2c4c7acc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RW9KBbRyWzVRvys8rhs5ow",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1330,
      "cache_read_input_tokens": 25686,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1330
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

_source line 24 · 2026-05-19T23:28:53.157Z_

<details><summary>↩ Tool result · `toolu_01GKHX45XVuWUY2qNNrtcmGX`</summary>

```text
# PRIDE Metric Implementation

Based on the GitHub repository content provided, I can confirm that **PRIDE metric implementation details are documented but the actual code snippets are not included in the web page content you've shared**.

## What the Repository Indicates:

The README states that PRIDE computes a **Paraphrase Distance (PD)** from two components:
- **SK** (keyword similarity)
- **ST** (structural similarity)

The metric then "measures the ratio of PD-weighted successes to total possible PD, normalized to 0–100."

## Where to Find the Implementation:

The actual code is located in:
1. **`metrics/README.md`** - Contains detailed metric documentation
2. **`metrics/PRIDE_metric_playground.ipynb`** - Interactive notebook with implementation
3. **`metrics/analyze_results.py`** - Analysis script using the metric
4. **`metrics/libero_para_metadata.csv`** - Supporting data

## Next Steps:

To access the actual code implementation including:
- PD computation formula
- SK and ST calculation methods
- Default alpha values
- Specific thresholds

You'll need to visit the GitHub repository directly and examine the files in the `metrics/` directory, which aren't rendered in this web page excerpt.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "22a2e982-a310-489d-a0ca-d55341a4e48c",
  "tool_use_result": {
    "bytes": 324174,
    "code": 200,
    "codeText": "OK",
    "result": "# PRIDE Metric Implementation\n\nBased on the GitHub repository content provided, I can confirm that **PRIDE metric implementation details are documented but the actual code snippets are not included in the web page content you've shared**.\n\n## What the Repository Indicates:\n\nThe README states that PRIDE computes a **Paraphrase Distance (PD)** from two components:\n- **SK** (keyword similarity)\n- **ST** (structural similarity)\n\nThe metric then \"measures the ratio of PD-weighted successes to total possible PD, normalized to 0–100.\"\n\n## Where to Find the Implementation:\n\nThe actual code is located in:\n1. **`metrics/README.md`** - Contains detailed metric documentation\n2. **`metrics/PRIDE_metric_playground.ipynb`** - Interactive notebook with implementation\n3. **`metrics/analyze_results.py`** - Analysis script using the metric\n4. **`metrics/libero_para_metadata.csv`** - Supporting data\n\n## Next Steps:\n\nTo access the actual code implementation including:\n- PD computation formula\n- SK and ST calculation methods\n- Default alpha values\n- Specific thresholds\n\nYou'll need to visit the GitHub repository directly and examine the files in the `metrics/` directory, which aren't rendered in this web page excerpt.",
    "durationMs": 5068,
    "url": "https://github.com/cau-hai-lab/LIBERO-Para"
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-19T23:28:54.348Z_

<details><summary>↩ Tool result · `toolu_014XYf1CGizZoDc3HRkJobgi`</summary>

````text
# PRIDE Metric: Mathematical Formulation

## Paraphrase Distance (PD) Formula

**Equation 3** from the paper defines PD as:

```
PD = 1 - (α·S_K(O,P) + (1-α)·S_T(T_O, T_P))
```

Where:
- **S_K(O,P)**: Keyword similarity (ranges 0-1, higher = more similar)
- **S_T(T_O, T_P)**: Structural similarity (ranges 0-1, higher = more similar)
- **α**: Weighting parameter, **default value = 0.5**

## PRIDE Score Formula

**Equation 4** defines PRIDE as:

```
PRIDE = { PD,  if success
        { 0,   if failure
```

**Interpretation**: Higher PRIDE = better robustness (more difficult paraphrases successfully handled). When a task fails, PRIDE = 0 regardless of paraphrase difficulty.

## S_K (Keyword Similarity) Computation

**Equation 1**:

```
S_K(O,P) = (1/n) Σ(i=1 to n) max(j∈{1,...,m}) cos(e(o_i), e(p_j))
```

Measures semantic preservation of task-critical content words via embedding cosine similarity from Sentence-BERT.

## S_T (Structural Similarity) Computation

**Equation 2**:

```
S_T(T_O, T_P) = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)
```

Uses tree edit distance (TED) on dependency parse trees with POS tags as node labels. Normalized by combined tree sizes.

## Reported PRIDE Scores (Table 3)

| Model | PRIDE Score |
|-------|------------|
| OpenVLA-OFTgoal | 58.8 |
| π₀.₅ (expert-only) | 32.0 |
| X-VLA | 52.7 |
| OpenVLA-OFTmixed | 56.3 |
| Xiaomi-Robotics-0 | 69.2 |
| π₀.₅ | 65.4 |
| VLA-Adapter | 36.1 |
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "18a20372-9417-42f1-90c7-434752a213a2",
  "tool_use_result": {
    "bytes": 404368,
    "code": 200,
    "codeText": "OK",
    "result": "# PRIDE Metric: Mathematical Formulation\n\n## Paraphrase Distance (PD) Formula\n\n**Equation 3** from the paper defines PD as:\n\n```\nPD = 1 - (α·S_K(O,P) + (1-α)·S_T(T_O, T_P))\n```\n\nWhere:\n- **S_K(O,P)**: Keyword similarity (ranges 0-1, higher = more similar)\n- **S_T(T_O, T_P)**: Structural similarity (ranges 0-1, higher = more similar)\n- **α**: Weighting parameter, **default value = 0.5**\n\n## PRIDE Score Formula\n\n**Equation 4** defines PRIDE as:\n\n```\nPRIDE = { PD,  if success\n        { 0,   if failure\n```\n\n**Interpretation**: Higher PRIDE = better robustness (more difficult paraphrases successfully handled). When a task fails, PRIDE = 0 regardless of paraphrase difficulty.\n\n## S_K (Keyword Similarity) Computation\n\n**Equation 1**:\n\n```\nS_K(O,P) = (1/n) Σ(i=1 to n) max(j∈{1,...,m}) cos(e(o_i), e(p_j))\n```\n\nMeasures semantic preservation of task-critical content words via embedding cosine similarity from Sentence-BERT.\n\n## S_T (Structural Similarity) Computation\n\n**Equation 2**:\n\n```\nS_T(T_O, T_P) = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)\n```\n\nUses tree edit distance (TED) on dependency parse trees with POS tags as node labels. Normalized by combined tree sizes.\n\n## Reported PRIDE Scores (Table 3)\n\n| Model | PRIDE Score |\n|-------|------------|\n| OpenVLA-OFTgoal | 58.8 |\n| π₀.₅ (expert-only) | 32.0 |\n| X-VLA | 52.7 |\n| OpenVLA-OFTmixed | 56.3 |\n| Xiaomi-Robotics-0 | 69.2 |\n| π₀.₅ | 65.4 |\n| VLA-Adapter | 36.1 |",
    "durationMs": 7602,
    "url": "https://arxiv.org/html/2603.28301v1"
  }
}
````

</details>

---

### Assistant

_source line 26_

<details><summary>Logged reasoning block</summary>

```text
I got the key details from the paper. Let me also try to access the project page for any additional information, and check the actual code implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "5b534745-a5fa-4702-85e1-37243b5989ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kwmd9a3fv4QaxmSuUDgL7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 321,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 27016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1084
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

_source line 27_

Let me also check the project page and the actual code implementation for the aggregation formula.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "be7a4a14-09ee-4609-a7ee-13db693f642e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kwmd9a3fv4QaxmSuUDgL7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 321,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 27016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1084
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

_source line 28_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RcoU2iEz3Lt1KEipV89zWe`</summary>

```json
{
  "url": "https://cau-hai-lab.github.io/LIBERO-Para/",
  "prompt": "Extract the PRIDE metric formula and definition. Specifically look for:\n1. How PRIDE is aggregated across multiple tasks/paraphrases (is it averaged? summed? ratio?)\n2. The exact aggregation formula - is it sum of PD for successes divided by sum of all PD?\n3. Any normalization (e.g., multiplied by 100)\n4. The OFT baseline PRIDE value"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "527ed3e4-d256-4036-8541-91bf3f98de1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kwmd9a3fv4QaxmSuUDgL7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 321,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 27016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1084
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

_source line 29_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NEmFiGvoXRfv1VEcwoSWUy`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/analyze_results.py",
  "prompt": "Extract the complete PRIDE metric computation code. Show the exact formulas used for:\n1. PD (Paraphrase Distance) computation from SK and ST\n2. PRIDE score computation from PD and success\n3. How PRIDE is aggregated across multiple samples\n4. The default alpha value\n5. Any normalization steps"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "cce9a7aa-1561-4346-a1d2-56b4c2f19d4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Kwmd9a3fv4QaxmSuUDgL7e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 321,
      "cache_creation_input_tokens": 1084,
      "cache_read_input_tokens": 27016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1084
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

_source line 30 · 2026-05-19T23:29:08.181Z_

<details><summary>↩ Tool result · reported error · `toolu_01NEmFiGvoXRfv1VEcwoSWUy`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "309f87ed-b599-41e9-b7c2-54632c949a73",
  "tool_use_result": "Error: Request failed with status code 404"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-19T23:29:14.298Z_

<details><summary>↩ Tool result · `toolu_01RcoU2iEz3Lt1KEipV89zWe`</summary>

```text
# PRIDE Metric Extraction

Based on the provided content, here's what can be determined about the PRIDE metric:

## Definition
"PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) addresses this by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then weighting success by difficulty."

## Components
- **Paraphrase Distance (PD)**: Derived from keyword similarity (SK) and structural similarity (ST)
- **SK**: Measures semantic similarity between task-critical content words
- **ST**: Uses dependency-tree edit distance to capture structural variation

## Aggregation Method
The document does not explicitly specify the exact aggregation formula (e.g., whether PD values are summed, averaged, or used in a ratio calculation). It only states that "success by difficulty" is weighted, with harder paraphrases receiving more credit than easier ones.

## Normalization
The document does not clearly specify if results are normalized (e.g., multiplied by 100).

## Baseline Values
For the OFT models:
- OpenVLA-OFTmixed PRIDE: **56.3**
- OpenVLA-OFTgoal PRIDE: **58.8**

The precise mathematical formula for aggregating PD across all paraphrases is not provided in this webpage content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "a870330b-9d30-4d43-8d6f-164a8f7dee28",
  "tool_use_result": {
    "bytes": 26696,
    "code": 200,
    "codeText": "OK",
    "result": "# PRIDE Metric Extraction\n\nBased on the provided content, here's what can be determined about the PRIDE metric:\n\n## Definition\n\"PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) addresses this by computing a Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then weighting success by difficulty.\"\n\n## Components\n- **Paraphrase Distance (PD)**: Derived from keyword similarity (SK) and structural similarity (ST)\n- **SK**: Measures semantic similarity between task-critical content words\n- **ST**: Uses dependency-tree edit distance to capture structural variation\n\n## Aggregation Method\nThe document does not explicitly specify the exact aggregation formula (e.g., whether PD values are summed, averaged, or used in a ratio calculation). It only states that \"success by difficulty\" is weighted, with harder paraphrases receiving more credit than easier ones.\n\n## Normalization\nThe document does not clearly specify if results are normalized (e.g., multiplied by 100).\n\n## Baseline Values\nFor the OFT models:\n- OpenVLA-OFTmixed PRIDE: **56.3**\n- OpenVLA-OFTgoal PRIDE: **58.8**\n\nThe precise mathematical formula for aggregating PD across all paraphrases is not provided in this webpage content.",
    "durationMs": 7793,
    "url": "https://cau-hai-lab.github.io/LIBERO-Para/"
  }
}
```

</details>

---

### Tool call

_source line 32_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015v3wV5L2GEBcnSGLJQr54T`</summary>

```json
{
  "url": "https://raw.githubusercontent.com/cau-hai-lab/LIBERO-Para/main/metrics/PRIDE_metric_playground.ipynb",
  "prompt": "Extract the exact PRIDE metric implementation code. Show:\n1. How PD is computed from SK and ST (the formula)\n2. How PRIDE is computed from PD values and success indicators\n3. The aggregation formula across tasks\n4. Default alpha value\n5. Any normalization (e.g. multiply by 100)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "12779a4d-d65f-45b9-9ce1-36edee88053d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XmyVAcZSZ9S5gjHi9Di5AK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 39,
      "cache_creation_input_tokens": 1063,
      "cache_read_input_tokens": 28100,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1063
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

_source line 33 · 2026-05-19T23:29:19.510Z_

<details><summary>↩ Tool result · reported error · `toolu_015v3wV5L2GEBcnSGLJQr54T`</summary>

```text
Request failed with status code 404
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "3063f52d-3b4b-47c4-940b-e3fca79fdcf3",
  "tool_use_result": "Error: Request failed with status code 404"
}
```

</details>

---

### Tool call

_source line 34_

<details open><summary>🔧 Tool call — Bash · `toolu_01RdpMLVx1au6VXWwwYiubCA`</summary>

```json
{
  "command": "cd /tmp && git clone --depth 1 https://github.com/cau-hai-lab/LIBERO-Para.git 2>&1 | tail -5",
  "description": "Clone LIBERO-Para repo to inspect PRIDE implementation",
  "timeout": 30000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "c047b101-d790-4bb6-a882-ebc35f2ff54e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L1fTWTq2YjLWw28Y61837e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 239,
      "cache_read_input_tokens": 29163,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 239
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

### System

_source line 35_

```json
{
  "type": "system",
  "subtype": "task_started",
  "task_id": "bsro37lwb",
  "tool_use_id": "toolu_01RdpMLVx1au6VXWwwYiubCA",
  "description": "Clone LIBERO-Para repo to inspect PRIDE implementation",
  "task_type": "local_bash",
  "uuid": "fba01942-8430-4acc-9347-af9631f3bff0",
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e"
}
```

---

### System

_source line 36_

```json
{
  "type": "system",
  "subtype": "task_notification",
  "task_id": "bsro37lwb",
  "tool_use_id": "toolu_01RdpMLVx1au6VXWwwYiubCA",
  "status": "completed",
  "output_file": "",
  "summary": "Clone LIBERO-Para repo to inspect PRIDE implementation",
  "uuid": "8d9031fd-1c38-46bd-ae40-a7e18216c67c",
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e"
}
```

---

### Tool result

_source line 37 · 2026-05-19T23:29:41.471Z_

<details><summary>↩ Tool result · `toolu_01RdpMLVx1au6VXWwwYiubCA`</summary>

```text
Cloning into 'LIBERO-Para'...
Updating files:   8% (432/5241)Updating files:   9% (472/5241)Updating files:  10% (525/5241)Updating files:  11% (577/5241)Updating files:  12% (629/5241)Updating files:  13% (682/5241)Updating files:  14% (734/5241)Updating files:  15% (787/5241)Updating files:  16% (839/5241)Updating files:  17% (891/5241)Updating files:  18% (944/5241)Updating files:  19% (996/5241)Updating files:  20% (1049/5241)Updating files:  21% (1101/5241)Updating files:  22% (1154/5241)Updating files:  23% (1206/5241)Updating files:  24% (1258/5241)Updating files:  25% (1311/5241)Updating files:  26% (1363/5241)Updating files:  27% (1416/5241)Updating files:  28% (1468/5241)Updating files:  29% (1520/5241)Updating files:  30% (1573/5241)Updating files:  31% (1625/5241)Updating files:  32% (1678/5241)Updating files:  33% (1730/5241)Updating files:  34% (1782/5241)Updating files:  35% (1835/5241)Updating files:  36% (1887/5241)Updating files:  37% (1940/5241)Updating files:  38% (1992/5241)Updating files:  39% (2044/5241)Updating files:  40% (2097/5241)Updating files:  41% (2149/5241)Updating files:  42% (2202/5241)Updating files:  43% (2254/5241)Updating files:  44% (2307/5241)Updating files:  45% (2359/5241)Updating files:  46% (2411/5241)Updating files:  47% (2464/5241)Updating files:  48% (2516/5241)Updating files:  49% (2569/5241)Updating files:  50% (2621/5241)Updating files:  51% (2673/5241)Updating files:  52% (2726/5241)Updating files:  53% (2778/5241)Updating files:  54% (2831/5241)Updating files:  55% (2883/5241)Updating files:  56% (2935/5241)Updating files:  57% (2988/5241)Updating files:  58% (3040/5241)Updating files:  59% (3093/5241)Updating files:  60% (3145/5241)Updating files:  61% (3198/5241)Updating files:  62% (3250/5241)Updating files:  63% (3302/5241)Updating files:  64% (3355/5241)Updating files:  65% (3407/5241)Updating files:  66% (3460/5241)Updating files:  67% (3512/5241)Updating files:  68% (3564/5241)Updating files:  69% (3617/5241)Updating files:  70% (3669/5241)Updating files:  71% (3722/5241)Updating files:  72% (3774/5241)Updating files:  73% (3826/5241)Updating files:  74% (3879/5241)Updating files:  75% (3931/5241)Updating files:  76% (3984/5241)Updating files:  77% (4036/5241)Updating files:  78% (4088/5241)Updating files:  79% (4141/5241)Updating files:  80% (4193/5241)Updating files:  81% (4246/5241)Updating files:  82% (4298/5241)Updating files:  83% (4351/5241)Updating files:  84% (4403/5241)Updating files:  85% (4455/5241)Updating files:  86% (4508/5241)Updating files:  87% (4560/5241)Updating files:  88% (4613/5241)Updating files:  89% (4665/5241)Updating files:  90% (4717/5241)Updating files:  91% (4770/5241)Updating files:  92% (4822/5241)Updating files:  93% (4875/5241)Updating files:  94% (4927/5241)Updating files:  95% (4979/5241)Updating files:  96% (5032/5241)Updating files:  97% (5084/5241)Updating files:  98% (5137/5241)Updating files:  99% (5189/5241)Updating files: 100% (5241/5241)Updating files: 100% (5241/5241), done.
Shell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "60b3a0fa-f303-4d34-b3a3-6e147efaa499",
  "tool_use_result": {
    "stdout": "Cloning into 'LIBERO-Para'...\nUpdating files:   8% (432/5241)\rUpdating files:   9% (472/5241)\rUpdating files:  10% (525/5241)\rUpdating files:  11% (577/5241)\rUpdating files:  12% (629/5241)\rUpdating files:  13% (682/5241)\rUpdating files:  14% (734/5241)\rUpdating files:  15% (787/5241)\rUpdating files:  16% (839/5241)\rUpdating files:  17% (891/5241)\rUpdating files:  18% (944/5241)\rUpdating files:  19% (996/5241)\rUpdating files:  20% (1049/5241)\rUpdating files:  21% (1101/5241)\rUpdating files:  22% (1154/5241)\rUpdating files:  23% (1206/5241)\rUpdating files:  24% (1258/5241)\rUpdating files:  25% (1311/5241)\rUpdating files:  26% (1363/5241)\rUpdating files:  27% (1416/5241)\rUpdating files:  28% (1468/5241)\rUpdating files:  29% (1520/5241)\rUpdating files:  30% (1573/5241)\rUpdating files:  31% (1625/5241)\rUpdating files:  32% (1678/5241)\rUpdating files:  33% (1730/5241)\rUpdating files:  34% (1782/5241)\rUpdating files:  35% (1835/5241)\rUpdating files:  36% (1887/5241)\rUpdating files:  37% (1940/5241)\rUpdating files:  38% (1992/5241)\rUpdating files:  39% (2044/5241)\rUpdating files:  40% (2097/5241)\rUpdating files:  41% (2149/5241)\rUpdating files:  42% (2202/5241)\rUpdating files:  43% (2254/5241)\rUpdating files:  44% (2307/5241)\rUpdating files:  45% (2359/5241)\rUpdating files:  46% (2411/5241)\rUpdating files:  47% (2464/5241)\rUpdating files:  48% (2516/5241)\rUpdating files:  49% (2569/5241)\rUpdating files:  50% (2621/5241)\rUpdating files:  51% (2673/5241)\rUpdating files:  52% (2726/5241)\rUpdating files:  53% (2778/5241)\rUpdating files:  54% (2831/5241)\rUpdating files:  55% (2883/5241)\rUpdating files:  56% (2935/5241)\rUpdating files:  57% (2988/5241)\rUpdating files:  58% (3040/5241)\rUpdating files:  59% (3093/5241)\rUpdating files:  60% (3145/5241)\rUpdating files:  61% (3198/5241)\rUpdating files:  62% (3250/5241)\rUpdating files:  63% (3302/5241)\rUpdating files:  64% (3355/5241)\rUpdating files:  65% (3407/5241)\rUpdating files:  66% (3460/5241)\rUpdating files:  67% (3512/5241)\rUpdating files:  68% (3564/5241)\rUpdating files:  69% (3617/5241)\rUpdating files:  70% (3669/5241)\rUpdating files:  71% (3722/5241)\rUpdating files:  72% (3774/5241)\rUpdating files:  73% (3826/5241)\rUpdating files:  74% (3879/5241)\rUpdating files:  75% (3931/5241)\rUpdating files:  76% (3984/5241)\rUpdating files:  77% (4036/5241)\rUpdating files:  78% (4088/5241)\rUpdating files:  79% (4141/5241)\rUpdating files:  80% (4193/5241)\rUpdating files:  81% (4246/5241)\rUpdating files:  82% (4298/5241)\rUpdating files:  83% (4351/5241)\rUpdating files:  84% (4403/5241)\rUpdating files:  85% (4455/5241)\rUpdating files:  86% (4508/5241)\rUpdating files:  87% (4560/5241)\rUpdating files:  88% (4613/5241)\rUpdating files:  89% (4665/5241)\rUpdating files:  90% (4717/5241)\rUpdating files:  91% (4770/5241)\rUpdating files:  92% (4822/5241)\rUpdating files:  93% (4875/5241)\rUpdating files:  94% (4927/5241)\rUpdating files:  95% (4979/5241)\rUpdating files:  96% (5032/5241)\rUpdating files:  97% (5084/5241)\rUpdating files:  98% (5137/5241)\rUpdating files:  99% (5189/5241)\rUpdating files: 100% (5241/5241)\rUpdating files: 100% (5241/5241), done.",
    "stderr": "\nShell cwd was reset to /home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
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

<details open><summary>🔧 Tool call — Bash · `toolu_01RQpY59sXsxH1KLfcTak7dG`</summary>

```json
{
  "command": "find /tmp/LIBERO-Para/metrics -type f -name \"*.py\" -o -name \"*.ipynb\" | head -20",
  "description": "List metric implementation files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "433f5f43-98d6-4b31-bc2e-8d1a75968c20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CvtCzrXm6g7AX4EM9jxdGY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1500,
      "cache_read_input_tokens": 29402,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1500
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

_source line 39 · 2026-05-19T23:29:45.418Z_

<details><summary>↩ Tool result · `toolu_01RQpY59sXsxH1KLfcTak7dG`</summary>

```text
/tmp/LIBERO-Para/metrics/compute_pride_score_example.py
/tmp/LIBERO-Para/metrics/analyze_results.py
/tmp/LIBERO-Para/metrics/PRIDE_metric_playground.ipynb
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "ecfe5186-91ab-4db5-9059-4aaf45e5fd71",
  "tool_use_result": {
    "stdout": "/tmp/LIBERO-Para/metrics/compute_pride_score_example.py\n/tmp/LIBERO-Para/metrics/analyze_results.py\n/tmp/LIBERO-Para/metrics/PRIDE_metric_playground.ipynb",
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

_source line 40_

<details open><summary>🔧 Tool call — Read · `toolu_01BH6NMExYcEw8upCVXzxAeJ`</summary>

```json
{
  "file_path": "/tmp/LIBERO-Para/metrics/compute_pride_score_example.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "8b4c27c1-4194-4975-b635-584793dbce4e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHZSvZaTjRXXe4k5Fbg2BW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 30902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 173
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

_source line 41 · 2026-05-19T23:29:48.417Z_

<details><summary>↩ Tool result · `toolu_01BH6NMExYcEw8upCVXzxAeJ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	Add similarity scores to verified CSV
4	
5	기존 compute_similarity.py의 로직을 사용해서 verified_csv에 
6	structural_similarity, keyword_similarity 등을 추가해서 저장.
7	
8	Usage:
9	    python add_similarity_to_verified.py --verified_csv /path/to/verified.csv --output_csv /path/to/output.csv
10	
11	Requirements:
12	    pip install spacy sentence-transformers pandas numpy tqdm
13	    python -m spacy download en_core_web_sm
14	"""
15	
16	import argparse
17	import pandas as pd
18	import numpy as np
19	from pathlib import Path
20	from datetime import datetime
21	import warnings
22	warnings.filterwarnings('ignore')
23	
24	
25	# =============================================================================
26	# Dependency Check
27	# =============================================================================
28	
29	def check_dependencies():
30	    missing = []
31	    try:
32	        import spacy
33	    except ImportError:
34	        missing.append("spacy")
35	    try:
36	        from sentence_transformers import SentenceTransformer
37	    except ImportError:
38	        missing.append("sentence-transformers")
39	    try:
40	        from tqdm import tqdm
41	    except ImportError:
42	        missing.append("tqdm")
43	    
44	    if missing:
45	        print("Missing dependencies. Please install:")
46	        print(f"  pip install {' '.join(missing)}")
47	        if "spacy" not in missing:
48	            print("  python -m spacy download en_core_web_sm")
49	        exit(1)
50	
51	
52	# =============================================================================
53	# 1. Tree Edit Distance (Zhang-Shasha Algorithm)
54	# =============================================================================
55	
56	class TreeNode:
57	    def __init__(self, label, children=None):
58	        self.label = label
59	        self.children = children or []
60	
61	
62	def build_dependency_tree(doc) -> TreeNode:
63	    root_token = None
64	    for token in doc:
65	        if token.dep_ == "ROOT":
66	            root_token = token
67	            break
68	    
69	    if root_token is None:
70	        return TreeNode(("ROOT", "X"))
71	    
72	    def build_subtree(token):
73	        label = (token.dep_, token.pos_)
74	        children = [build_subtree(child) for child in token.children]
75	        children.sort(key=lambda x: x.label)
76	        return TreeNode(label, children)
77	    
78	    return build_subtree(root_token)
79	
80	
81	def tree_to_list(node: TreeNode) -> list:
82	    result = []
83	    for child in node.children:
84	        result.extend(tree_to_list(child))
85	    result.append(node)
86	    return result
87	
88	
89	def get_leftmost_leaf_indices(nodes: list) -> list:
90	    n = len(nodes)
91	    leftmost = [0] * n
92	    
93	    for i, node in enumerate(nodes):
94	        if not node.children:
95	            leftmost[i] = i
96	        else:
97	            min_idx = i
98	            for child in node.children:
99	                child_idx = nodes.index(child)
100	                if leftmost[child_idx] < min_idx:
101	                    min_idx = leftmost[child_idx]
102	            leftmost[i] = min_idx
103	    
104	    return leftmost
105	
106	
107	def zhang_shasha_distance(tree1: TreeNode, tree2: TreeNode) -> int:
108	    nodes1 = tree_to_list(tree1)
109	    nodes2 = tree_to_list(tree2)
110	    
111	    n1, n2 = len(nodes1), len(nodes2)
112	    
113	    if n1 == 0 and n2 == 0:
114	        return 0
115	    if n1 == 0:
116	        return n2
117	    if n2 == 0:
118	        return n1
119	    
120	    l1 = get_leftmost_leaf_indices(nodes1)
121	    l2 = get_leftmost_leaf_indices(nodes2)
122	    
123	    def get_keyroots(nodes, leftmost):
124	        keyroots = []
125	        seen_leftmost = set()
126	        for i in range(len(nodes) - 1, -1, -1):
127	            if leftmost[i] not in seen_leftmost:
128	                keyroots.append(i)
129	                seen_leftmost.add(leftmost[i])
130	        return sorted(keyroots)
131	    
132	    kr1 = get_keyroots(nodes1, l1)
133	    kr2 = get_keyroots(nodes2, l2)
134	    
135	    TD = np.zeros((n1 + 1, n2 + 1))
136	    
137	    def compute_forest_distance(i, j):
138	        FD = np.zeros((n1 + 1, n2 + 1))
139	        
140	        li, lj = l1[i], l2[j]
141	        FD[li][lj] = 0
142	        
143	        for x in range(li, i + 1):
144	            FD[x + 1][lj] = FD[x][lj] + 1
145	        
146	        for y in range(lj, j + 1):
147	            FD[li][y + 1] = FD[li][y] + 1
148	        
149	        for x in range(li, i + 1):
150	            for y in range(lj, j + 1):
151	                cost = 0 if nodes1[x].label == nodes2[y].label else 1
152	                
153	                if l1[x] == li and l2[y] == lj:
154	                    FD[x + 1][y + 1] = min(
155	                        FD[x][y + 1] + 1,
156	                        FD[x + 1][y] + 1,
157	                        FD[x][y] + cost
158	                    )
159	                    TD[x + 1][y + 1] = FD[x + 1][y + 1]
160	                else:
161	                    FD[x + 1][y + 1] = min(
162	                        FD[x][y + 1] + 1,
163	                        FD[x + 1][y] + 1,
164	                        FD[l1[x]][l2[y]] + TD[x + 1][y + 1]
165	                    )
166	    
167	    for i in kr1:
168	        for j in kr2:
169	            compute_forest_distance(i, j)
170	    
171	    return int(TD[n1][n2])
172	
173	
174	class StructuralSimilarity:
175	    def __init__(self, nlp):
176	        self.nlp = nlp
177	    
178	    def compute(self, text1: str, text2: str) -> dict:
179	        doc1 = self.nlp(text1.lower())
180	        doc2 = self.nlp(text2.lower())
181	        
182	        tree1 = build_dependency_tree(doc1)
183	        tree2 = build_dependency_tree(doc2)
184	        
185	        size1 = len(tree_to_list(tree1))
186	        size2 = len(tree_to_list(tree2))
187	        
188	        ted = zhang_shasha_distance(tree1, tree2)
189	        
190	        # 변경: max(size1, size2) → size1 + size2
191	        total_size = size1 + size2
192	        similarity = 1.0 - (ted / total_size) if total_size > 0 else 1.0
193	        
194	        return {
195	            "tree_edit_distance": ted,
196	            "structural_similarity": similarity,
197	            "tree_size_1": size1,
198	            "tree_size_2": size2,
199	        }
200	
201	
202	# =============================================================================
203	# 2. Keyword Similarity (Max Matching)
204	# =============================================================================
205	
206	class KeywordSimilarity:
207	    def __init__(self, nlp, encoder):
208	        self.nlp = nlp
209	        self.encoder = encoder
210	        self.embedding_cache = {}
211	    
212	    def extract_content_words(self, text: str) -> list:
213	        """
214	        Extract content words (NOUN, VERB, ADJ, ADV)
215	        - put, open 같은 task-critical verb 포함
216	        - is_stop 체크 안 함 (로봇 task에서는 이런 verb가 중요)
217	        """
218	        doc = self.nlp(text.lower())
219	        content_pos = {"NOUN", "VERB", "ADJ", "ADV", "PROPN"}
220	        
221	        words = []
222	        for token in doc:
223	            if token.pos_ in content_pos:
224	                words.append(token.lemma_)
225	        
226	        return words
227	    
228	    def get_embeddings_batch(self, words: list) -> np.ndarray:
229	        if not words:
230	            return None
231	        
232	        uncached = [w for w in words if w not in self.embedding_cache]
233	        if uncached:
234	            embeddings = self.encoder.encode(uncached, convert_to_numpy=True)
235	            for w, emb in zip(uncached, embeddings):
236	                self.embedding_cache[w] = emb
237	        
238	        return np.array([self.embedding_cache[w] for w in words])
239	    
240	    def cosine_sim_matrix(self, emb1: np.ndarray, emb2: np.ndarray) -> np.ndarray:
241	        emb1_norm = emb1 / (np.linalg.norm(emb1, axis=1, keepdims=True) + 1e-8)
242	        emb2_norm = emb2 / (np.linalg.norm(emb2, axis=1, keepdims=True) + 1e-8)
243	        return np.dot(emb1_norm, emb2_norm.T)
244	    
245	    def max_matching_similarity(self, orig_words: list, para_words: list) -> tuple:
246	        if not orig_words or not para_words:
247	            return 0.0, [], []
248	        
249	        orig_embs = self.get_embeddings_batch(orig_words)
250	        para_embs = self.get_embeddings_batch(para_words)
251	        
252	        sim_matrix = self.cosine_sim_matrix(orig_embs, para_embs)
253	        
254	        max_sims = sim_matrix.max(axis=1)
255	        best_match_idx = sim_matrix.argmax(axis=1)
256	        best_matches = [(orig_words[i], para_words[best_match_idx[i]], max_sims[i]) 
257	                        for i in range(len(orig_words))]
258	        
259	        return float(max_sims.mean()), max_sims.tolist(), best_matches
260	    
261	    def jaccard_sim(self, words1: list, words2: list) -> float:
262	        set1 = set(words1)
263	        set2 = set(words2)
264	        if len(set1 | set2) == 0:
265	            return 1.0
266	        return len(set1 & set2) / len(set1 | set2)
267	    
268	    def compute(self, text1: str, text2: str) -> dict:
269	        words1 = self.extract_content_words(text1)
270	        words2 = self.extract_content_words(text2)
271	        
272	        jaccard = self.jaccard_sim(words1, words2)
273	        keyword_sim, individual_sims, best_matches = self.max_matching_similarity(words1, words2)
274	        
275	        doc1 = self.nlp(text1.lower())
276	        doc2 = self.nlp(text2.lower())
277	        
278	        nouns1 = [t.lemma_ for t in doc1 if t.pos_ in ["NOUN", "PROPN"]]
279	        nouns2 = [t.lemma_ for t in doc2 if t.pos_ in ["NOUN", "PROPN"]]
280	        
281	        verbs1 = [t.lemma_ for t in doc1 if t.pos_ == "VERB"]
282	        verbs2 = [t.lemma_ for t in doc2 if t.pos_ == "VERB"]
283	        
284	        noun_sim, _, _ = self.max_matching_similarity(nouns1, nouns2)
285	        verb_sim, _, _ = self.max_matching_similarity(verbs1, verbs2)
286	        
287	        return {
288	            "content_words_1": words1,
289	            "content_words_2": words2,
290	            "jaccard_similarity": jaccard,
291	            "keyword_similarity": keyword_sim,
292	            "noun_similarity": noun_sim,
293	            "verb_similarity": verb_sim,
294	        }
295	
296	
297	# =============================================================================
298	# 3. Main Processing
299	# =============================================================================
300	
301	def add_similarity_to_csv(verified_csv: str, output_csv: str):
302	    """verified CSV에 similarity 점수 추가"""
303	    from tqdm import tqdm
304	    import spacy
305	    from sentence_transformers import SentenceTransformer
306	    
307	    # Load data
308	    print(f"Loading CSV: {verified_csv}")
309	    df = pd.read_csv(verified_csv)
310	    print(f"Loaded {len(df)} rows")
311	    
312	    # Initialize
313	    print("\nInitializing models...")
314	    try:
315	        nlp = spacy.load("en_core_web_sm")
316	    except OSError:
317	        print("Downloading spacy model...")
318	        import subprocess
319	        subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
320	        nlp = spacy.load("en_core_web_sm")
321	    
322	    print("Loading Sentence-BERT model: all-MiniLM-L6-v2")
323	    encoder = SentenceTransformer("all-MiniLM-L6-v2")
324	    
325	    struct_sim = StructuralSimilarity(nlp)
326	    keyword_sim = KeywordSimilarity(nlp, encoder)
327	    
328	    # Compute similarities
329	    print("\nComputing similarities...")
330	    
331	    structural_similarities = []
332	    tree_edit_distances = []
333	    keyword_similarities = []
334	    jaccard_similarities = []
335	    noun_similarities = []
336	    verb_similarities = []
337	    
338	    for idx, row in tqdm(df.iterrows(), total=len(df)):
339	        original = row['original_instruction']
340	        paraphrase = row['new_instruction']
341	        
342	        # Structural similarity
343	        struct_result = struct_sim.compute(original, paraphrase)
344	        structural_similarities.append(struct_result['structural_similarity'])
345	        tree_edit_distances.append(struct_result['tree_edit_distance'])
346	        
347	        # Keyword similarity
348	        kw_result = keyword_sim.compute(original, paraphrase)
349	        keyword_similarities.append(kw_result['keyword_similarity'])
350	        jaccard_similarities.append(kw_result['jaccard_similarity'])
351	        noun_similarities.append(kw_result['noun_similarity'])
352	        verb_similarities.append(kw_result['verb_similarity'])
353	    
354	    # Add columns to dataframe
355	    df['structural_similarity'] = structural_similarities
356	    df['tree_edit_distance'] = tree_edit_distances
357	    df['keyword_similarity'] = keyword_similarities
358	    df['jaccard_similarity'] = jaccard_similarities
359	    df['noun_similarity'] = noun_similarities
360	    df['verb_similarity'] = verb_similarities
361	    
362	    # Create output directory if needed
363	    output_dir = Path(output_csv).parent
364	    if output_dir and not output_dir.exists():
365	        output_dir.mkdir(parents=True, exist_ok=True)
366	    
367	    # Save
368	    df.to_csv(output_csv, index=False)
369	    print(f"\n✓ Saved to: {output_csv}")
370	    
371	    # Print summary
372	    print("\n" + "="*70)
373	    print("SIMILARITY SUMMARY")
374	    print("="*70)
375	    print(f"Total samples: {len(df)}")
376	    print(f"Structural Similarity: {df['structural_similarity'].mean():.3f} ± {df['structural_similarity'].std():.3f}")
377	    print(f"Tree Edit Distance:    {df['tree_edit_distance'].mean():.1f} ± {df['tree_edit_distance'].std():.1f}")
378	    print(f"Keyword Similarity:    {df['keyword_similarity'].mean():.3f} ± {df['keyword_similarity'].std():.3f}")
379	    print(f"Jaccard Similarity:    {df['jaccard_similarity'].mean():.3f} ± {df['jaccard_similarity'].std():.3f}")
380	    print(f"Noun Similarity:       {df['noun_similarity'].mean():.3f} ± {df['noun_similarity'].std():.3f}")
381	    print(f"Verb Similarity:       {df['verb_similarity'].mean():.3f} ± {df['verb_similarity'].std():.3f}")
382	    
383	    # By category if available
384	    if 'high' in df.columns:
385	        print("\n" + "-"*70)
386	        print("By HIGH Category:")
387	        for cat in sorted(df['high'].unique()):
388	            subset = df[df['high'] == cat]
389	            print(f"  {cat}: Struct={subset['structural_similarity'].mean():.3f}, Kw={subset['keyword_similarity'].mean():.3f} (n={len(subset)})")
390	    
391	    return df
392	
393	
394	def main():
395	    parser = argparse.ArgumentParser(description='Add similarity scores to verified CSV')
396	    parser.add_argument('--verified_csv', type=str, required=True, help='Path to verified CSV')
397	    parser.add_argument('--output_csv', type=str, default=None, help='Output CSV path (default: adds _with_similarity suffix)')
398	    args = parser.parse_args()
399	    
400	    check_dependencies()
401	    
402	    # Default output path
403	    if args.output_csv is None:
404	        input_path = Path(args.verified_csv)
405	        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
406	        args.output_csv = str(input_path.parent / f"{input_path.stem}_with_similarity_{timestamp}.csv")
407	    else:
408	        # If output_csv is a directory, generate filename
409	        output_path = Path(args.output_csv)
410	        if output_path.is_dir() or (not output_path.suffix and not output_path.exists()):
411	            # It's a directory path
412	            output_path.mkdir(parents=True, exist_ok=True)
413	            input_path = Path(args.verified_csv)
414	            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
415	            args.output_csv = str(output_path / f"{input_path.stem}_with_similarity_{timestamp}.csv")
416	    
417	    add_similarity_to_csv(args.verified_csv, args.output_csv)
418	    
419	    print("\n✅ Complete!")
420	
421	
422	if __name__ == "__main__":
423	    main()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "d181acdf-fb61-4fcb-8ba8-e151d08aa13d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/LIBERO-Para/metrics/compute_pride_score_example.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\nAdd similarity scores to verified CSV\n\n기존 compute_similarity.py의 로직을 사용해서 verified_csv에 \nstructural_similarity, keyword_similarity 등을 추가해서 저장.\n\nUsage:\n    python add_similarity_to_verified.py --verified_csv /path/to/verified.csv --output_csv /path/to/output.csv\n\nRequirements:\n    pip install spacy sentence-transformers pandas numpy tqdm\n    python -m spacy download en_core_web_sm\n\"\"\"\n\nimport argparse\nimport pandas as pd\nimport numpy as np\nfrom pathlib import Path\nfrom datetime import datetime\nimport warnings\nwarnings.filterwarnings('ignore')\n\n\n# =============================================================================\n# Dependency Check\n# =============================================================================\n\ndef check_dependencies():\n    missing = []\n    try:\n        import spacy\n    except ImportError:\n        missing.append(\"spacy\")\n    try:\n        from sentence_transformers import SentenceTransformer\n    except ImportError:\n        missing.append(\"sentence-transformers\")\n    try:\n        from tqdm import tqdm\n    except ImportError:\n        missing.append(\"tqdm\")\n    \n    if missing:\n        print(\"Missing dependencies. Please install:\")\n        print(f\"  pip install {' '.join(missing)}\")\n        if \"spacy\" not in missing:\n            print(\"  python -m spacy download en_core_web_sm\")\n        exit(1)\n\n\n# =============================================================================\n# 1. Tree Edit Distance (Zhang-Shasha Algorithm)\n# =============================================================================\n\nclass TreeNode:\n    def __init__(self, label, children=None):\n        self.label = label\n        self.children = children or []\n\n\ndef build_dependency_tree(doc) -> TreeNode:\n    root_token = None\n    for token in doc:\n        if token.dep_ == \"ROOT\":\n            root_token = token\n            break\n    \n    if root_token is None:\n        return TreeNode((\"ROOT\", \"X\"))\n    \n    def build_subtree(token):\n        label = (token.dep_, token.pos_)\n        children = [build_subtree(child) for child in token.children]\n        children.sort(key=lambda x: x.label)\n        return TreeNode(label, children)\n    \n    return build_subtree(root_token)\n\n\ndef tree_to_list(node: TreeNode) -> list:\n    result = []\n    for child in node.children:\n        result.extend(tree_to_list(child))\n    result.append(node)\n    return result\n\n\ndef get_leftmost_leaf_indices(nodes: list) -> list:\n    n = len(nodes)\n    leftmost = [0] * n\n    \n    for i, node in enumerate(nodes):\n        if not node.children:\n            leftmost[i] = i\n        else:\n            min_idx = i\n            for child in node.children:\n                child_idx = nodes.index(child)\n                if leftmost[child_idx] < min_idx:\n                    min_idx = leftmost[child_idx]\n            leftmost[i] = min_idx\n    \n    return leftmost\n\n\ndef zhang_shasha_distance(tree1: TreeNode, tree2: TreeNode) -> int:\n    nodes1 = tree_to_list(tree1)\n    nodes2 = tree_to_list(tree2)\n    \n    n1, n2 = len(nodes1), len(nodes2)\n    \n    if n1 == 0 and n2 == 0:\n        return 0\n    if n1 == 0:\n        return n2\n    if n2 == 0:\n        return n1\n    \n    l1 = get_leftmost_leaf_indices(nodes1)\n    l2 = get_leftmost_leaf_indices(nodes2)\n    \n    def get_keyroots(nodes, leftmost):\n        keyroots = []\n        seen_leftmost = set()\n        for i in range(len(nodes) - 1, -1, -1):\n            if leftmost[i] not in seen_leftmost:\n                keyroots.append(i)\n                seen_leftmost.add(leftmost[i])\n        return sorted(keyroots)\n    \n    kr1 = get_keyroots(nodes1, l1)\n    kr2 = get_keyroots(nodes2, l2)\n    \n    TD = np.zeros((n1 + 1, n2 + 1))\n    \n    def compute_forest_distance(i, j):\n        FD = np.zeros((n1 + 1, n2 + 1))\n        \n        li, lj = l1[i], l2[j]\n        FD[li][lj] = 0\n        \n        for x in range(li, i + 1):\n            FD[x + 1][lj] = FD[x][lj] + 1\n        \n        for y in range(lj, j + 1):\n            FD[li][y + 1] = FD[li][y] + 1\n        \n        for x in range(li, i + 1):\n            for y in range(lj, j + 1):\n                cost = 0 if nodes1[x].label == nodes2[y].label else 1\n                \n                if l1[x] == li and l2[y] == lj:\n                    FD[x + 1][y + 1] = min(\n                        FD[x][y + 1] + 1,\n                        FD[x + 1][y] + 1,\n                        FD[x][y] + cost\n                    )\n                    TD[x + 1][y + 1] = FD[x + 1][y + 1]\n                else:\n                    FD[x + 1][y + 1] = min(\n                        FD[x][y + 1] + 1,\n                        FD[x + 1][y] + 1,\n                        FD[l1[x]][l2[y]] + TD[x + 1][y + 1]\n                    )\n    \n    for i in kr1:\n        for j in kr2:\n            compute_forest_distance(i, j)\n    \n    return int(TD[n1][n2])\n\n\nclass StructuralSimilarity:\n    def __init__(self, nlp):\n        self.nlp = nlp\n    \n    def compute(self, text1: str, text2: str) -> dict:\n        doc1 = self.nlp(text1.lower())\n        doc2 = self.nlp(text2.lower())\n        \n        tree1 = build_dependency_tree(doc1)\n        tree2 = build_dependency_tree(doc2)\n        \n        size1 = len(tree_to_list(tree1))\n        size2 = len(tree_to_list(tree2))\n        \n        ted = zhang_shasha_distance(tree1, tree2)\n        \n        # 변경: max(size1, size2) → size1 + size2\n        total_size = size1 + size2\n        similarity = 1.0 - (ted / total_size) if total_size > 0 else 1.0\n        \n        return {\n            \"tree_edit_distance\": ted,\n            \"structural_similarity\": similarity,\n            \"tree_size_1\": size1,\n            \"tree_size_2\": size2,\n        }\n\n\n# =============================================================================\n# 2. Keyword Similarity (Max Matching)\n# =============================================================================\n\nclass KeywordSimilarity:\n    def __init__(self, nlp, encoder):\n        self.nlp = nlp\n        self.encoder = encoder\n        self.embedding_cache = {}\n    \n    def extract_content_words(self, text: str) -> list:\n        \"\"\"\n        Extract content words (NOUN, VERB, ADJ, ADV)\n        - put, open 같은 task-critical verb 포함\n        - is_stop 체크 안 함 (로봇 task에서는 이런 verb가 중요)\n        \"\"\"\n        doc = self.nlp(text.lower())\n        content_pos = {\"NOUN\", \"VERB\", \"ADJ\", \"ADV\", \"PROPN\"}\n        \n        words = []\n        for token in doc:\n            if token.pos_ in content_pos:\n                words.append(token.lemma_)\n        \n        return words\n    \n    def get_embeddings_batch(self, words: list) -> np.ndarray:\n        if not words:\n            return None\n        \n        uncached = [w for w in words if w not in self.embedding_cache]\n        if uncached:\n            embeddings = self.encoder.encode(uncached, convert_to_numpy=True)\n            for w, emb in zip(uncached, embeddings):\n                self.embedding_cache[w] = emb\n        \n        return np.array([self.embedding_cache[w] for w in words])\n    \n    def cosine_sim_matrix(self, emb1: np.ndarray, emb2: np.ndarray) -> np.ndarray:\n        emb1_norm = emb1 / (np.linalg.norm(emb1, axis=1, keepdims=True) + 1e-8)\n        emb2_norm = emb2 / (np.linalg.norm(emb2, axis=1, keepdims=True) + 1e-8)\n        return np.dot(emb1_norm, emb2_norm.T)\n    \n    def max_matching_similarity(self, orig_words: list, para_words: list) -> tuple:\n        if not orig_words or not para_words:\n            return 0.0, [], []\n        \n        orig_embs = self.get_embeddings_batch(orig_words)\n        para_embs = self.get_embeddings_batch(para_words)\n        \n        sim_matrix = self.cosine_sim_matrix(orig_embs, para_embs)\n        \n        max_sims = sim_matrix.max(axis=1)\n        best_match_idx = sim_matrix.argmax(axis=1)\n        best_matches = [(orig_words[i], para_words[best_match_idx[i]], max_sims[i]) \n                        for i in range(len(orig_words))]\n        \n        return float(max_sims.mean()), max_sims.tolist(), best_matches\n    \n    def jaccard_sim(self, words1: list, words2: list) -> float:\n        set1 = set(words1)\n        set2 = set(words2)\n        if len(set1 | set2) == 0:\n            return 1.0\n        return len(set1 & set2) / len(set1 | set2)\n    \n    def compute(self, text1: str, text2: str) -> dict:\n        words1 = self.extract_content_words(text1)\n        words2 = self.extract_content_words(text2)\n        \n        jaccard = self.jaccard_sim(words1, words2)\n        keyword_sim, individual_sims, best_matches = self.max_matching_similarity(words1, words2)\n        \n        doc1 = self.nlp(text1.lower())\n        doc2 = self.nlp(text2.lower())\n        \n        nouns1 = [t.lemma_ for t in doc1 if t.pos_ in [\"NOUN\", \"PROPN\"]]\n        nouns2 = [t.lemma_ for t in doc2 if t.pos_ in [\"NOUN\", \"PROPN\"]]\n        \n        verbs1 = [t.lemma_ for t in doc1 if t.pos_ == \"VERB\"]\n        verbs2 = [t.lemma_ for t in doc2 if t.pos_ == \"VERB\"]\n        \n        noun_sim, _, _ = self.max_matching_similarity(nouns1, nouns2)\n        verb_sim, _, _ = self.max_matching_similarity(verbs1, verbs2)\n        \n        return {\n            \"content_words_1\": words1,\n            \"content_words_2\": words2,\n            \"jaccard_similarity\": jaccard,\n            \"keyword_similarity\": keyword_sim,\n            \"noun_similarity\": noun_sim,\n            \"verb_similarity\": verb_sim,\n        }\n\n\n# =============================================================================\n# 3. Main Processing\n# =============================================================================\n\ndef add_similarity_to_csv(verified_csv: str, output_csv: str):\n    \"\"\"verified CSV에 similarity 점수 추가\"\"\"\n    from tqdm import tqdm\n    import spacy\n    from sentence_transformers import SentenceTransformer\n    \n    # Load data\n    print(f\"Loading CSV: {verified_csv}\")\n    df = pd.read_csv(verified_csv)\n    print(f\"Loaded {len(df)} rows\")\n    \n    # Initialize\n    print(\"\\nInitializing models...\")\n    try:\n        nlp = spacy.load(\"en_core_web_sm\")\n    except OSError:\n        print(\"Downloading spacy model...\")\n        import subprocess\n        subprocess.run([\"python\", \"-m\", \"spacy\", \"download\", \"en_core_web_sm\"])\n        nlp = spacy.load(\"en_core_web_sm\")\n    \n    print(\"Loading Sentence-BERT model: all-MiniLM-L6-v2\")\n    encoder = SentenceTransformer(\"all-MiniLM-L6-v2\")\n    \n    struct_sim = StructuralSimilarity(nlp)\n    keyword_sim = KeywordSimilarity(nlp, encoder)\n    \n    # Compute similarities\n    print(\"\\nComputing similarities...\")\n    \n    structural_similarities = []\n    tree_edit_distances = []\n    keyword_similarities = []\n    jaccard_similarities = []\n    noun_similarities = []\n    verb_similarities = []\n    \n    for idx, row in tqdm(df.iterrows(), total=len(df)):\n        original = row['original_instruction']\n        paraphrase = row['new_instruction']\n        \n        # Structural similarity\n        struct_result = struct_sim.compute(original, paraphrase)\n        structural_similarities.append(struct_result['structural_similarity'])\n        tree_edit_distances.append(struct_result['tree_edit_distance'])\n        \n        # Keyword similarity\n        kw_result = keyword_sim.compute(original, paraphrase)\n        keyword_similarities.append(kw_result['keyword_similarity'])\n        jaccard_similarities.append(kw_result['jaccard_similarity'])\n        noun_similarities.append(kw_result['noun_similarity'])\n        verb_similarities.append(kw_result['verb_similarity'])\n    \n    # Add columns to dataframe\n    df['structural_similarity'] = structural_similarities\n    df['tree_edit_distance'] = tree_edit_distances\n    df['keyword_similarity'] = keyword_similarities\n    df['jaccard_similarity'] = jaccard_similarities\n    df['noun_similarity'] = noun_similarities\n    df['verb_similarity'] = verb_similarities\n    \n    # Create output directory if needed\n    output_dir = Path(output_csv).parent\n    if output_dir and not output_dir.exists():\n        output_dir.mkdir(parents=True, exist_ok=True)\n    \n    # Save\n    df.to_csv(output_csv, index=False)\n    print(f\"\\n✓ Saved to: {output_csv}\")\n    \n    # Print summary\n    print(\"\\n\" + \"=\"*70)\n    print(\"SIMILARITY SUMMARY\")\n    print(\"=\"*70)\n    print(f\"Total samples: {len(df)}\")\n    print(f\"Structural Similarity: {df['structural_similarity'].mean():.3f} ± {df['structural_similarity'].std():.3f}\")\n    print(f\"Tree Edit Distance:    {df['tree_edit_distance'].mean():.1f} ± {df['tree_edit_distance'].std():.1f}\")\n    print(f\"Keyword Similarity:    {df['keyword_similarity'].mean():.3f} ± {df['keyword_similarity'].std():.3f}\")\n    print(f\"Jaccard Similarity:    {df['jaccard_similarity'].mean():.3f} ± {df['jaccard_similarity'].std():.3f}\")\n    print(f\"Noun Similarity:       {df['noun_similarity'].mean():.3f} ± {df['noun_similarity'].std():.3f}\")\n    print(f\"Verb Similarity:       {df['verb_similarity'].mean():.3f} ± {df['verb_similarity'].std():.3f}\")\n    \n    # By category if available\n    if 'high' in df.columns:\n        print(\"\\n\" + \"-\"*70)\n        print(\"By HIGH Category:\")\n        for cat in sorted(df['high'].unique()):\n            subset = df[df['high'] == cat]\n            print(f\"  {cat}: Struct={subset['structural_similarity'].mean():.3f}, Kw={subset['keyword_similarity'].mean():.3f} (n={len(subset)})\")\n    \n    return df\n\n\ndef main():\n    parser = argparse.ArgumentParser(description='Add similarity scores to verified CSV')\n    parser.add_argument('--verified_csv', type=str, required=True, help='Path to verified CSV')\n    parser.add_argument('--output_csv', type=str, default=None, help='Output CSV path (default: adds _with_similarity suffix)')\n    args = parser.parse_args()\n    \n    check_dependencies()\n    \n    # Default output path\n    if args.output_csv is None:\n        input_path = Path(args.verified_csv)\n        timestamp = datetime.now().strftime(\"%Y%m%d_%H%M%S\")\n        args.output_csv = str(input_path.parent / f\"{input_path.stem}_with_similarity_{timestamp}.csv\")\n    else:\n        # If output_csv is a directory, generate filename\n        output_path = Path(args.output_csv)\n        if output_path.is_dir() or (not output_path.suffix and not output_path.exists()):\n            # It's a directory path\n            output_path.mkdir(parents=True, exist_ok=True)\n            input_path = Path(args.verified_csv)\n            timestamp = datetime.now().strftime(\"%Y%m%d_%H%M%S\")\n            args.output_csv = str(output_path / f\"{input_path.stem}_with_similarity_{timestamp}.csv\")\n    \n    add_similarity_to_csv(args.verified_csv, args.output_csv)\n    \n    print(\"\\n✅ Complete!\")\n\n\nif __name__ == \"__main__\":\n    main()",
      "numLines": 423,
      "startLine": 1,
      "totalLines": 423
    }
  }
}
```

</details>

---

### Tool call

_source line 42_

<details open><summary>🔧 Tool call — Read · `toolu_01QVRW8AxtrzE1xUGNRCCQiJ`</summary>

```json
{
  "file_path": "/tmp/LIBERO-Para/metrics/analyze_results.py"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "bad99e68-724b-45ad-9b63-1ac212021ab0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KHZSvZaTjRXXe4k5Fbg2BW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 173,
      "cache_read_input_tokens": 30902,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 173
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

_source line 43 · 2026-05-19T23:29:48.732Z_

<details><summary>↩ Tool result · `toolu_01QVRW8AxtrzE1xUGNRCCQiJ`</summary>

```text
1	#!/usr/bin/env python3
2	"""
3	generate_paraphrase_table.py
4	
5	Generates a 4x11 (obj x act) paraphrase success rate heatmap from
6	structured JSON eval logs.
7	
8	Directory structure expected:
9	    model_path/
10	        seed7/
11	            eval0.json  ... eval9.json
12	            meta.json
13	            summary.json
14	        seed8/
15	        ...
16	        seed11/
17	
18	Each eval{N}.json has:
19	    {
20	      "eval_id": N,
21	      "original_instruction": ...,
22	      "episodes": [
23	        {
24	          "paraphrase_type": "act" | "obj" | "comp",
25	          "categories": [...],
26	          "subcategories": [...],  # comp: [obj_subcat, act_subcat]
27	          "success": true/false,
28	          ...
29	        }, ...
30	      ]
31	    }
32	
33	Usage:
34	    python generate_paraphrase_table.py \
35	        --model_path ../logs_para/xiaomi \
36	        --model_name "OpenVLA-OFT" \
37	        --output_dir ./metrics/output
38	"""
39	
40	import argparse
41	import json
42	import glob
43	import os
44	import sys
45	from collections import defaultdict
46	from typing import Dict, List, Tuple, Optional
47	
48	import numpy as np
49	import pandas as pd
50	import matplotlib.pyplot as plt
51	import seaborn as sns
52	from matplotlib.colors import LinearSegmentedColormap
53	
54	
55	# ============================================================================
56	# Constants
57	# ============================================================================
58	
59	# Y-axis (obj paraphrase types)
60	OBJ_TYPES_ORDER = [
61	    "None",
62	    "addition_deletion",
63	    "same_polarity_contextual",
64	    "same_polarity_habitual",
65	]
66	
67	# X-axis (act paraphrase types)
68	ACT_TYPES_ORDER = [
69	    "None",
70	    "addition_deletion",
71	    "same_polarity_contextual",
72	    "same_polarity_habitual",
73	    "coordination",
74	    "subordination",
75	    "need_statement",
76	    "embedded_imperative",
77	    "permission_directive",
78	    "question_directive",
79	    "hint",
80	]
81	
82	# Fixed model display order
83	MODEL_ORDER = [
84	    "OpenVLA-OFT-goal",
85	    "OpenVLA-OFT_mixed",
86	    "Pi05",
87	    "Pi05-ExpertOnly",
88	    "X-VLA",
89	    "VLA-Adapter",
90	    "Xiaomi-Robotics-0",
91	]
92	
93	# Fixed model colors (consistent across all plots)
94	MODEL_COLORS_FIXED = {
95	    "OpenVLA-OFT-goal":   "#1f77b4",  # blue
96	    "OpenVLA-OFT_mixed":  "#ff7f0e",  # orange
97	    "Pi05":               "#d62728",  # red
98	    "Pi05-ExpertOnly":    "#8c564b",  # brown
99	    "X-VLA":              "#9467bd",  # purple
100	    "VLA-Adapter":        "#2ca02c",  # green
101	    "Xiaomi-Robotics-0":  "#17becf",  # cyan
102	}
103	
104	# Display labels (shorter names for heatmap axes)
105	OBJ_DISPLAY = {
106	    "None": "None",
107	    "addition_deletion": "Addition",
108	    "same_polarity_contextual": "SP-contextual",
109	    "same_polarity_habitual": "SP-habitual",
110	}
111	
112	ACT_DISPLAY = {
113	    "None": "None",
114	    "addition_deletion": "Addition",
115	    "same_polarity_contextual": "SP-contextual",
116	    "same_polarity_habitual": "SP-habitual",
117	    "coordination": "Coordination",
118	    "subordination": "Subordination",
119	    "need_statement": "Need",
120	    "embedded_imperative": "Embedded",
121	    "permission_directive": "Permission",
122	    "question_directive": "Question",
123	    "hint": "Hint",
124	}
125	
126	# Act paraphrase categories (indices into ACT_TYPES_ORDER, excluding "None" at 0)
127	ACT_CATEGORIES = {
128	    "Lexical":     ["addition_deletion", "same_polarity_contextual", "same_polarity_habitual"],
129	    "Structural":  ["coordination", "subordination"],
130	    "Pragmatic":   ["need_statement", "embedded_imperative", "permission_directive",
131	                    "question_directive", "hint"],
132	}
133	
134	CATEGORY_COLORS = {
135	    "Lexical":    "#2166ac",
136	    "Structural": "#d6604d",
137	    "Pragmatic":  "#7b3294",
138	}
139	
140	# Act types excluding None (for bar charts)
141	ACT_TYPES_PARA = ACT_TYPES_ORDER[1:]
142	
143	ACT_DISPLAY_SHORT = {
144	    "addition_deletion": "Addition",
145	    "same_polarity_contextual": "SP-ctx",
146	    "same_polarity_habitual": "SP-hab",
147	    "coordination": "Coord",
148	    "subordination": "Subord",
149	    "need_statement": "Need",
150	    "embedded_imperative": "Embedded",
151	    "permission_directive": "Permission",
152	    "question_directive": "Question",
153	    "hint": "Hint",
154	}
155	
156	# Map each act type to its category
157	ACT_TYPE_TO_CATEGORY = {}
158	for cat, types in ACT_CATEGORIES.items():
159	    for t in types:
160	        ACT_TYPE_TO_CATEGORY[t] = cat
161	
162	
163	def discover_seeds(model_path: str) -> List[str]:
164	    """Find all seed directories under model_path."""
165	    seed_dirs = sorted(glob.glob(os.path.join(model_path, "seed*")))
166	    seed_dirs = [d for d in seed_dirs if os.path.isdir(d)]
167	    if not seed_dirs:
168	        print(f"[ERROR] No seed directories found in: {model_path}")
169	        sys.exit(1)
170	    print(f"Found {len(seed_dirs)} seeds: {[os.path.basename(d) for d in seed_dirs]}")
171	    return seed_dirs
172	
173	
174	def load_eval_jsons(seed_dir: str) -> List[dict]:
175	    """Load all eval{N}.json files from a seed directory."""
176	    eval_files = sorted(glob.glob(os.path.join(seed_dir, "eval*.json")))
177	    # Exclude eval_unknown.json if exists
178	    eval_files = [f for f in eval_files if "unknown" not in os.path.basename(f)]
179	    
180	    all_episodes = []
181	    for ef in eval_files:
182	        with open(ef, "r") as f:
183	            data = json.load(f)
184	        eval_id = data.get("eval_id", -1)
185	        for ep in data.get("episodes", []):
186	            ep["_eval_id"] = eval_id
187	            all_episodes.append(ep)
188	    
189	    return all_episodes
190	
191	
192	def episode_to_cell(ep: dict) -> Tuple[str, str]:
193	    """
194	    Map an episode to (obj_low, act_low) cell coordinates.
195	
196	    Rules:
197	        act  → obj_low = "None",             act_low = subcategories[0]
198	        obj  → obj_low = subcategories[0],    act_low = "None"
199	        comp → obj_low = subcategories[0],    act_low = subcategories[1]
200	    """
201	    ptype = ep["paraphrase_type"]
202	    subcats = ep.get("subcategories", [])
203	
204	    if ptype == "act":
205	        return ("None", subcats[0] if subcats else "unknown")
206	    elif ptype == "obj":
207	        return (subcats[0] if subcats else "unknown", "None")
208	    elif ptype == "comp":
209	        obj_sub = subcats[0] if len(subcats) > 0 else "unknown"
210	        act_sub = subcats[1] if len(subcats) > 1 else "unknown"
211	        return (obj_sub, act_sub)
212	    else:
213	        return ("unknown", "unknown")
214	
215	
216	# ============================================================================
217	# Aggregation
218	# ============================================================================
219	
220	def aggregate_seed(episodes: List[dict]) -> Dict[Tuple[str, str], dict]:
221	    """
222	    Aggregate episodes within one seed into per-cell stats.
223	    Returns: {(obj_low, act_low): {"successes": int, "total": int}}
224	    """
225	    cells = defaultdict(lambda: {"successes": 0, "total": 0})
226	    for ep in episodes:
227	        obj_low, act_low = episode_to_cell(ep)
228	        cells[(obj_low, act_low)]["total"] += 1
229	        if ep.get("success", False):
230	            cells[(obj_low, act_low)]["successes"] += 1
231	    return dict(cells)
232	
233	
234	def aggregate_across_seeds(
235	    model_path: str,
236	) -> Tuple[pd.DataFrame, pd.DataFrame, dict, pd.DataFrame]:
237	    """
238	    Load all seeds, compute per-seed cell stats, then average across seeds.
239	
240	    Returns:
241	        heatmap_df: DataFrame with mean success rates (index=obj, columns=act)
242	        std_df: DataFrame with std of success rates
243	        per_seed_stats: {seed_name: {(obj, act): {successes, total, sr}}}
244	        full_df: DataFrame with all rows (obj, act, mean, std, n_seeds, per-seed SRs)
245	    """
246	    seed_dirs = discover_seeds(model_path)
247	    per_seed_stats = {}
248	    all_cell_srs = defaultdict(list)  # {(obj, act): [sr_seed1, sr_seed2, ...]}
249	    seed_names = []
250	
251	    for seed_dir in seed_dirs:
252	        seed_name = os.path.basename(seed_dir)
253	        seed_names.append(seed_name)
254	        episodes = load_eval_jsons(seed_dir)
255	        print(f"  {seed_name}: {len(episodes)} episodes loaded")
256	
257	        cell_stats = aggregate_seed(episodes)
258	
259	        # Compute per-seed SR for each cell
260	        for cell_key, stats in cell_stats.items():
261	            sr = stats["successes"] / stats["total"] if stats["total"] > 0 else 0.0
262	            stats["success_rate"] = sr
263	            all_cell_srs[cell_key].append(sr)
264	
265	        per_seed_stats[seed_name] = cell_stats
266	
267	    # Build full dataframe rows
268	    rows = []
269	    for obj_low in OBJ_TYPES_ORDER:
270	        for act_low in ACT_TYPES_ORDER:
271	            srs = all_cell_srs.get((obj_low, act_low), [])
272	            mean_sr = np.mean(srs) * 100 if srs else np.nan
273	            std_sr = np.std(srs) * 100 if len(srs) > 1 else 0.0
274	            var_sr = np.var(srs) * 10000 if len(srs) > 1 else 0.0  # variance in %^2
275	
276	            row = {
277	                "obj_type": obj_low,
278	                "act_type": act_low,
279	                "mean_sr": mean_sr,
280	                "std_sr": std_sr,
281	                "var_sr": var_sr,
282	                "n_seeds": len(srs),
283	            }
284	            # Add per-seed SR columns
285	            for i, sname in enumerate(sorted(seed_names)):
286	                cell = per_seed_stats.get(sname, {}).get((obj_low, act_low), {})
287	                seed_sr = cell.get("success_rate", np.nan)
288	                row[sname] = round(seed_sr * 100, 2) if not np.isnan(seed_sr) else np.nan
289	            rows.append(row)
290	
291	    full_df = pd.DataFrame(rows)
292	
293	    heatmap_df = full_df.pivot(index="obj_type", columns="act_type", values="mean_sr")
294	    heatmap_df = heatmap_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)
295	
296	    std_df = full_df.pivot(index="obj_type", columns="act_type", values="std_sr")
297	    std_df = std_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)
298	
299	    return heatmap_df, std_df, per_seed_stats, full_df
300	
301	
302	# ============================================================================
303	# CSV Export
304	# ============================================================================
305	
306	def save_aggregated_csv(full_df: pd.DataFrame, output_dir: str, model_name: str):
307	    """
308	    Save aggregated CSV with columns:
309	        obj_type, act_type, mean_sr, std_sr, var_sr, n_seeds, seed7, seed8, ...
310	    Also computes overall summary rows (total paraphrase avg, per-type avg, etc.)
311	    """
312	    # --- Per-cell CSV ---
313	    csv_path = os.path.join(output_dir, f"{model_name}_aggregated.csv")
314	    
315	    # Round numeric columns
316	    export_df = full_df.copy()
317	    for col in export_df.columns:
318	        if col not in ("obj_type", "act_type", "n_seeds"):
319	            export_df[col] = export_df[col].round(2)
320	    
321	    # Sort by obj_type order, then act_type order
322	    obj_order = {v: i for i, v in enumerate(OBJ_TYPES_ORDER)}
323	    act_order = {v: i for i, v in enumerate(ACT_TYPES_ORDER)}
324	    export_df["_obj_order"] = export_df["obj_type"].map(obj_order)
325	    export_df["_act_order"] = export_df["act_type"].map(act_order)
326	    export_df = export_df.sort_values(["_obj_order", "_act_order"]).drop(columns=["_obj_order", "_act_order"])
327	    
328	    export_df.to_csv(csv_path, index=False)
329	    print(f"  Saved: {csv_path}")
330	
331	    # --- Summary CSV (marginals + overall) ---
332	    summary_rows = []
333	    
334	    # Filter out (None, None) = original instruction
335	    para_df = full_df[~((full_df["obj_type"] == "None") & (full_df["act_type"] == "None"))].copy()
336	    
337	    # Overall paraphrase average
338	    overall_mean = para_df["mean_sr"].mean()
339	    overall_std = para_df["mean_sr"].std()
340	    summary_rows.append({
341	        "category": "ALL_PARAPHRASE",
342	        "type": "overall",
343	        "mean_sr": round(overall_mean, 2),
344	        "std_across_cells": round(overall_std, 2),
345	        "n_cells": len(para_df),
346	    })
347	
348	    # Per obj_type marginal (average across all act_types)
349	    for obj in OBJ_TYPES_ORDER:
350	        subset = para_df[para_df["obj_type"] == obj]
351	        if len(subset) > 0:
352	            summary_rows.append({
353	                "category": "obj_marginal",
354	                "type": obj,
355	                "mean_sr": round(subset["mean_sr"].mean(), 2),
356	                "std_across_cells": round(subset["mean_sr"].std(), 2),
357	                "n_cells": len(subset),
358	            })
359	
360	    # Per act_type marginal (average across all obj_types)
361	    for act in ACT_TYPES_ORDER:
362	        subset = para_df[para_df["act_type"] == act]
363	        if len(subset) > 0:
364	            summary_rows.append({
365	                "category": "act_marginal",
366	                "type": act,
367	                "mean_sr": round(subset["mean_sr"].mean(), 2),
368	                "std_across_cells": round(subset["mean_sr"].std(), 2),
369	                "n_cells": len(subset),
370	            })
371	
372	    # act-only average (obj=None, act!=None)
373	    act_only = para_df[(para_df["obj_type"] == "None") & (para_df["act_type"] != "None")]
374	    if len(act_only) > 0:
375	        summary_rows.append({
376	            "category": "paraphrase_scope",
377	            "type": "act_only",
378	            "mean_sr": round(act_only["mean_sr"].mean(), 2),
379	            "std_across_cells": round(act_only["mean_sr"].std(), 2),
380	            "n_cells": len(act_only),
381	        })
382	
383	    # obj-only average (obj!=None, act=None)
384	    obj_only = para_df[(para_df["obj_type"] != "None") & (para_df["act_type"] == "None")]
385	    if len(obj_only) > 0:
386	        summary_rows.append({
387	            "category": "paraphrase_scope",
388	            "type": "obj_only",
389	            "mean_sr": round(obj_only["mean_sr"].mean(), 2),
390	            "std_across_cells": round(obj_only["mean_sr"].std(), 2),
391	            "n_cells": len(obj_only),
392	        })
393	
394	    # comp average (obj!=None, act!=None)
395	    comp = para_df[(para_df["obj_type"] != "None") & (para_df["act_type"] != "None")]
396	    if len(comp) > 0:
397	        summary_rows.append({
398	            "category": "paraphrase_scope",
399	            "type": "comp",
400	            "mean_sr": round(comp["mean_sr"].mean(), 2),
401	            "std_across_cells": round(comp["mean_sr"].std(), 2),
402	            "n_cells": len(comp),
403	        })
404	
405	    summary_df = pd.DataFrame(summary_rows)
406	    summary_path = os.path.join(output_dir, f"{model_name}_summary.csv")
407	    summary_df.to_csv(summary_path, index=False)
408	    print(f"  Saved: {summary_path}")
409	
410	
411	# ============================================================================
412	# Saving per-seed JSON
413	# ============================================================================
414	
415	def save_per_seed_json(per_seed_stats: dict, output_dir: str, model_name: str):
416	    """Save per-seed cell success rates as JSON."""
417	    for seed_name, cell_stats in per_seed_stats.items():
418	        out = {}
419	        for (obj_low, act_low), stats in cell_stats.items():
420	            key = f"{obj_low}+{act_low}"
421	            out[key] = {
422	                "obj_low": obj_low,
423	                "act_low": act_low,
424	                "successes": stats["successes"],
425	                "total": stats["total"],
426	                "success_rate": round(stats.get("success_rate", 0.0) * 100, 2),
427	            }
428	
429	        path = os.path.join(output_dir, f"{model_name}_{seed_name}_cells.json")
430	        with open(path, "w") as f:
431	            json.dump(out, f, indent=2)
432	        print(f"  Saved: {path}")
433	
434	
435	def save_aggregated_json(heatmap_df: pd.DataFrame, std_df: pd.DataFrame,
436	                         output_dir: str, model_name: str):
437	    """Save the aggregated (mean across seeds) heatmap data as JSON."""
438	    result = {}
439	    for obj_low in OBJ_TYPES_ORDER:
440	        for act_low in ACT_TYPES_ORDER:
441	            key = f"{obj_low}+{act_low}"
442	            mean_val = heatmap_df.loc[obj_low, act_low]
443	            std_val = std_df.loc[obj_low, act_low]
444	            result[key] = {
445	                "obj_low": obj_low,
446	                "act_low": act_low,
447	                "mean_sr": round(float(mean_val), 2) if not np.isnan(mean_val) else None,
448	                "std_sr": round(float(std_val), 2) if not np.isnan(std_val) else None,
449	            }
450	
451	    path = os.path.join(output_dir, f"{model_name}_aggregated_cells.json")
452	    with open(path, "w") as f:
453	        json.dump(result, f, indent=2)
454	    print(f"  Saved: {path}")
455	
456	
457	# ============================================================================
458	# Heatmap Visualization
459	# ============================================================================
460	
461	def get_colormap():
462	    """Custom red-to-green colormap: aggressive red for low success, green only for high."""
463	    colors = [
464	        (0.0,  "#67001f"),   # 0%  - dark crimson
465	        (0.10, "#d73027"),   # 10%
466	        (0.30, "#fc8d59"),   # 30%
467	        (0.50, "#fee090"),   # 50%
468	        (0.65, "#d9ef8b"),   # 65%
469	        (0.80, "#66bd63"),   # 80%
470	        (0.92, "#1a9850"),   # 92%
471	        (1.0,  "#00441b"),   # 100%
472	    ]
473	    return LinearSegmentedColormap.from_list(
474	        "custom_red_green", [(pos, c) for pos, c in colors], N=256
475	    )
476	
477	
478	def plot_heatmap(
479	    heatmap_df: pd.DataFrame,
480	    std_df: pd.DataFrame,
481	    png_path: str,
482	    model_name: str = "",
483	):
484	    """
485	    Plot 4x11 paraphrase combination heatmap.
486	    (None, None) cell is masked.
487	    """
488	    # Build mask: (None, None) = original, mask it
489	    mask = np.zeros_like(heatmap_df.values, dtype=bool)
490	    if "None" in heatmap_df.index and "None" in heatmap_df.columns:
491	        none_row = list(heatmap_df.index).index("None")
492	        none_col = list(heatmap_df.columns).index("None")
493	        mask[none_row, none_col] = True
494	
495	    # Build annotation strings
496	    annot_array = np.empty_like(heatmap_df.values, dtype=object)
497	    for i, obj in enumerate(heatmap_df.index):
498	        for j, act in enumerate(heatmap_df.columns):
499	            val = heatmap_df.iloc[i, j]
500	            std = std_df.iloc[i, j]
501	            if mask[i, j]:
502	                annot_array[i, j] = ""
503	            elif np.isnan(val):
504	                annot_array[i, j] = "N/A"
505	            else:
506	                annot_array[i, j] = f"{val:.1f}"
507	
508	    fig, ax = plt.subplots(figsize=(18, 5.5))
509	    cmap = get_colormap()
510	
511	    obj_display = [OBJ_DISPLAY.get(o, o) for o in heatmap_df.index]
512	    act_display = [ACT_DISPLAY.get(a, a) for a in heatmap_df.columns]
513	
514	    sns.heatmap(
515	        heatmap_df.values.astype(float),
516	        annot=annot_array,
517	        fmt="",
518	        cmap=cmap,
519	        mask=mask,
520	        cbar_kws={"label": "Success Rate (%)", "shrink": 0.8},
521	        linewidths=0.8,
522	        linecolor="white",
523	        ax=ax,
524	        vmin=0,
525	        vmax=100,
526	        annot_kws={"fontsize": 20, "fontweight": "bold"},
527	        xticklabels=act_display,
528	        yticklabels=obj_display,
529	    )
530	
531	    title = "Success Rate by Paraphrase Type Combination"
532	    if model_name:
533	        title = f"{model_name}: {title}"
534	    ax.set_xlabel("Act Paraphrase Type", fontsize=16, fontweight="normal", labelpad=10)
535	    ax.set_ylabel("Obj Paraphrase Type", fontsize=16, fontweight="normal", labelpad=10)
536	    ax.set_title(title, fontsize=18, fontweight="bold", pad=15)
537	
538	    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right", fontsize=16, fontweight="bold")
539	    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=16, fontweight="bold")
540	
541	    cbar = ax.collections[0].colorbar
542	    cbar.ax.tick_params(labelsize=12)
543	    cbar.ax.set_ylabel("Success Rate (%)", fontsize=14, fontweight="normal")
544	
545	    plt.tight_layout()
546	    plt.savefig(png_path, dpi=300, bbox_inches="tight")
547	    plt.close()
548	    print(f"  Saved: {png_path}")
549	
550	
551	# ============================================================================
552	# Action-axis Bar Charts
553	# ============================================================================
554	
555	def _extract_act_marginals(heatmap_df: pd.DataFrame,
556	                           baseline_sr: float = None) -> Dict[str, float]:
557	    """
558	    From a 4x11 heatmap_df, compute act-axis marginal SR.
559	    For each act type, average SR across all obj types.
560	
561	    If baseline_sr is provided, include act="None" marginal
562	    using baseline_sr for the (None, None) cell.
563	    """
564	    marginals = {}
565	
566	    # Include "None" if baseline_sr is given
567	    if baseline_sr is not None:
568	        vals = [baseline_sr]  # (None, None) cell
569	        for obj in OBJ_TYPES_ORDER:
570	            if obj == "None":
571	                continue
572	            v = heatmap_df.loc[obj, "None"]
573	            if not np.isnan(v):
574	                vals.append(v)
575	        marginals["None"] = np.mean(vals) if vals else np.nan
576	
577	    for act in ACT_TYPES_PARA:
578	        vals = []
579	        for obj in OBJ_TYPES_ORDER:
580	            v = heatmap_df.loc[obj, act]
581	            if not np.isnan(v):
582	                vals.append(v)
583	        marginals[act] = np.mean(vals) if vals else np.nan
584	    return marginals
585	
586	
587	def _extract_act_marginals_from_json(json_path: str) -> Dict[str, float]:
588	    """Extract act marginals from aggregated_cells.json."""
589	    with open(json_path, "r") as f:
590	        data = json.load(f)
591	
592	    # Collect per act type
593	    act_vals = defaultdict(list)
594	    for key, val in data.items():
595	        obj_low = val["obj_low"]
596	        act_low = val["act_low"]
597	        sr = val["mean_sr"]
598	        if act_low == "None":
599	            continue  # skip obj-only rows for act analysis
600	        if obj_low == "None" and act_low == "None":
601	            continue
602	        if sr is not None:
603	            act_vals[act_low].append(sr)
604	
605	    marginals = {}
606	    for act in ACT_TYPES_PARA:
607	        vals = act_vals.get(act, [])
608	        marginals[act] = np.mean(vals) if vals else np.nan
609	    return marginals
610	
611	
612	def plot_act_type_bars(
613	    model_marginals: Dict[str, Dict[str, float]],
614	    output_dir: str,
615	    filename_prefix: str = "act_type_bars",
616	):
617	    """
618	    Chart 1 (1-column): Mean SR per act type, bar color = category.
619	    If "None" is present in marginals, show it as first bar (gray).
620	    """
621	    # Determine act types to plot
622	    has_none = any("None" in m for m in model_marginals.values())
623	    act_types = (["None"] + ACT_TYPES_PARA) if has_none else ACT_TYPES_PARA
624	    n_types = len(act_types)
625	    x = np.arange(n_types)
626	
627	    means, bar_colors = [], []
628	    for act in act_types:
629	        vals = [m.get(act, np.nan) for m in model_marginals.values()]
630	        vals = [v for v in vals if not np.isnan(v)]
631	        means.append(np.mean(vals) if vals else 0)
632	        if act == "None":
633	            bar_colors.append("#555555")
634	        else:
635	            cat = ACT_TYPE_TO_CATEGORY.get(act, "Lexical")
636	            bar_colors.append(CATEGORY_COLORS.get(cat, "#333333"))
637	
638	    fig, ax = plt.subplots(figsize=(7, 3.5))
639	
640	    ax.bar(x, means, 0.7, color=bar_colors,
641	           edgecolor="white", linewidth=0.5, alpha=0.85)
642	
643	    for xi, m in zip(x, means):
644	        ax.text(xi, m + 0.8, f"{m:.1f}", ha="center", va="bottom",
645	                fontsize=7, fontweight="bold")
646	
647	    act_labels = []
648	    for a in act_types:
649	        if a == "None":
650	            act_labels.append("None")
651	        else:
652	            act_labels.append(ACT_DISPLAY_SHORT.get(a, a))
653	    ax.set_xticks(x)
654	    ax.set_xticklabels(act_labels, rotation=45, ha="right", fontsize=8, fontweight="bold")
655	    for tick_label, act in zip(ax.get_xticklabels(), act_types):
656	        if act == "None":
657	            tick_label.set_color("#555555")
658	        else:
659	            cat = ACT_TYPE_TO_CATEGORY.get(act, "")
660	            tick_label.set_color(CATEGORY_COLORS.get(cat, "black"))
661	
662	    _draw_category_spans(ax, act_types)
663	
664	    ax.set_xlabel("Act Paraphrase Type", fontsize=9, fontweight="bold", labelpad=6)
665	    ax.set_ylabel("Success Rate (%)", fontsize=9, fontweight="bold")
666	    ax.set_ylim(0, 105)
667	    ax.grid(axis="y", alpha=0.2, linestyle="--")
668	    ax.tick_params(axis="y", labelsize=7)
669	
670	    plt.tight_layout()
671	    path = os.path.join(output_dir, f"{filename_prefix}.png")
672	    plt.savefig(path, dpi=300, bbox_inches="tight")
673	    print(f"  Saved: {path}")
674	    plt.close()
675	
676	
677	def plot_act_category_bars(
678	    model_marginals: Dict[str, Dict[str, float]],
679	    output_dir: str,
680	    filename_prefix: str = "act_category_bars",
681	):
682	    """
683	    Chart 2 (1-column): Mean SR per category (Lexical/Structural/Pragmatic).
684	    Error bar = std across models' category-level means.
685	    """
686	    categories = list(ACT_CATEGORIES.keys())
687	    x = np.arange(len(categories))
688	
689	    cat_means, cat_colors = [], []
690	    for cat in categories:
691	        cat_types = ACT_CATEGORIES[cat]
692	        per_model = []
693	        for marginals in model_marginals.values():
694	            vals = [marginals.get(t, np.nan) for t in cat_types]
695	            vals = [v for v in vals if not np.isnan(v)]
696	            if vals:
697	                per_model.append(np.mean(vals))
698	        cat_means.append(np.mean(per_model) if per_model else 0)
699	        cat_colors.append(CATEGORY_COLORS[cat])
700	
701	    fig, ax = plt.subplots(figsize=(4, 3.5))
702	
703	    ax.bar(x, cat_means, 0.55, color=cat_colors,
704	           edgecolor="white", linewidth=0.5, alpha=0.85)
705	
706	    for xi, m in zip(x, cat_means):
707	        ax.text(xi, m + 1.0, f"{m:.1f}", ha="center", va="bottom",
708	                fontsize=9, fontweight="bold")
709	
710	    ax.set_xticks(x)
711	    ax.set_xticklabels(categories, fontsize=10, fontweight="bold")
712	    for tick_label, cat in zip(ax.get_xticklabels(), categories):
713	        tick_label.set_color(CATEGORY_COLORS.get(cat, "black"))
714	
715	    ax.set_ylabel("Success Rate (%)", fontsize=9, fontweight="bold")
716	    ax.set_ylim(0, 105)
717	    ax.grid(axis="y", alpha=0.2, linestyle="--")
718	    ax.tick_params(axis="y", labelsize=7)
719	
720	    plt.tight_layout()
721	    path = os.path.join(output_dir, f"{filename_prefix}.png")
722	    plt.savefig(path, dpi=300, bbox_inches="tight")
723	    print(f"  Saved: {path}")
724	    plt.close()
725	
726	
727	
728	def _draw_category_spans(ax, act_types):
729	    """Draw category bracket lines above the x-axis area."""
730	    # Find index ranges for each category
731	    for cat, cat_types in ACT_CATEGORIES.items():
732	        indices = [i for i, a in enumerate(act_types) if a in cat_types]
733	        if not indices:
734	            continue
735	        color = CATEGORY_COLORS[cat]
736	        x_left = min(indices) - 0.4
737	        x_right = max(indices) + 0.4
738	        x_center = (x_left + x_right) / 2
739	
740	        y_pos = 1.02
741	        h = 0.02
742	
743	        ax.plot([x_left, x_right], [y_pos, y_pos],
744	                color=color, linewidth=2.5, clip_on=False,
745	                transform=ax.get_xaxis_transform())
746	        ax.plot([x_left, x_left], [y_pos - h, y_pos],
747	                color=color, linewidth=2.5, clip_on=False,
748	                transform=ax.get_xaxis_transform())
749	        ax.plot([x_right, x_right], [y_pos - h, y_pos],
750	                color=color, linewidth=2.5, clip_on=False,
751	                transform=ax.get_xaxis_transform())
752	        ax.text(x_center, y_pos + 0.03, cat,
753	                ha="center", va="bottom", fontsize=9, fontweight="bold",
754	                color=color, transform=ax.get_xaxis_transform(), clip_on=False)
755	
756	
757	def generate_action_bar_charts(
758	    model_heatmaps: Dict[str, pd.DataFrame],
759	    output_dir: str,
760	    baseline_srs: Dict[str, float] = None,
761	):
762	    """
763	    Entry point: given {model_name: heatmap_df}, generate all 3 action bar charts.
764	    baseline_srs: {model_name: baseline SR for (None,None) cell}.
765	                  If None, "None" bar is omitted.
766	    """
767	    os.makedirs(output_dir, exist_ok=True)
768	
769	    # 1. Extract marginals
770	    model_marginals = {}
771	    model_baselines = {}
772	    for model, hdf in model_heatmaps.items():
773	        bl = baseline_srs.get(model) if baseline_srs else None
774	        model_marginals[model] = _extract_act_marginals(hdf, baseline_sr=bl)
775	        # Baseline = overall paraphrase mean (all cells excl None,None)
776	        vals = []
777	        for obj in OBJ_TYPES_ORDER:
778	            for act in ACT_TYPES_ORDER:
779	                if obj == "None" and act == "None":
780	                    continue
781	                v = hdf.loc[obj, act]
782	                if not np.isnan(v):
783	                    vals.append(v)
784	        model_baselines[model] = np.mean(vals) if vals else 0
785	
786	    # 2. Plot
787	    print("\n  [Action Bars 1/3] Per act type...")
788	    plot_act_type_bars(model_marginals, output_dir)
789	
790	    print("  [Action Bars 2/3] Per category...")
791	    plot_act_category_bars(model_marginals, output_dir)
792	
793	    print("  [Action Bars] Done.")
794	
795	
796	# ============================================================================
797	# PRIDE computation (SK + ST + PD from pre-computed CSV)
798	# ============================================================================
799	
800	
801	def load_pride_csv(csv_path: str) -> dict:
802	    """
803	    Load pre-computed SK/ST CSV.
804	    Key by instruction text (unique per paraphrase).
805	    Returns lookup: instruction_text -> {"sk": keyword_sim, "st": structural_sim}
806	    """
807	    df = pd.read_csv(csv_path)
808	    lookup = {}
809	    for _, row in df.iterrows():
810	        key = str(row["new_instruction"]).strip().lower()
811	        lookup[key] = {
812	            "sk": float(row["keyword_similarity"]),
813	            "st": float(row["structural_similarity"]),
814	        }
815	
816	    print(f"  Lookup: {len(lookup)} unique instructions (from {len(df)} CSV rows)")
817	    if lookup:
818	        sample = list(lookup.items())[:3]
819	        for k, v in sample:
820	            print(f"    \"{k[:50]}...\" → sk={v['sk']:.3f}, st={v['st']:.3f}")
821	
822	    return lookup
823	
824	
825	def compute_model_pride(model_path: str, pride_lookup: dict,
826	                        alphas: List[float] = None) -> dict:
827	    """
828	    Compute PRIDE score for a single model.
829	
830	    PD_i = 1 - (alpha * SK_i + (1 - alpha) * ST_i)
831	    PRIDE(alpha) = sum(success_i * PD_i) / sum(PD_i) * 100
832	    """
833	    if alphas is None:
834	        alphas = [0.0, 0.5, 1.0]
835	
836	    seed_dirs = discover_seeds(model_path)
837	
838	    # Collect per-episode (sk, st, success) for alpha sweep
839	    episode_data = []
840	    n_total = 0
841	    n_matched = 0
842	    unmatched_keys = []
843	
844	    for seed_dir in seed_dirs:
845	        episodes = load_eval_jsons(seed_dir)
846	        for ep in episodes:
847	            key = str(ep.get("paraphrased_instruction", "")).strip().lower()
848	            n_total += 1
849	
850	            info = pride_lookup.get(key)
851	            if info is None:
852	                if len(unmatched_keys) < 5:
853	                    unmatched_keys.append(key[:60])
854	                continue
855	
856	            n_matched += 1
857	            sk = info["sk"]
858	            st = info["st"]
859	            success = 1.0 if ep.get("success", False) else 0.0
860	            episode_data.append((sk, st, success))
861	
862	    print(f"  Matching: {n_matched}/{n_total} episodes ({n_total - n_matched} unmatched)")
863	    if unmatched_keys:
864	        print(f"  Sample unmatched: {unmatched_keys[:3]}")
865	    if episode_data:
866	        sks = [d[0] for d in episode_data]
867	        sts = [d[1] for d in episode_data]
868	        print(f"  Similarity ranges: SK=[{min(sks):.3f}, {max(sks):.3f}], "
869	              f"ST=[{min(sts):.3f}, {max(sts):.3f}]")
870	
871	    n_episodes = len(episode_data)
872	    n_success = int(sum(s for _, _, s in episode_data))
873	    sr = round(n_success / n_episodes * 100, 1) if n_episodes > 0 else 0
874	
875	    results = {"sr": sr, "n_episodes": n_episodes, "n_success": n_success}
876	
877	    for alpha in alphas:
878	        actual = 0.0
879	        total = 0.0
880	        for sk, st, success in episode_data:
881	            pd = 1.0 - (alpha * sk + (1.0 - alpha) * st)
882	            total += pd
883	            if success:
884	                actual += pd
885	        score = round(actual / total * 100, 1) if total > 0 else 0
886	        results[f"pride_a{alpha:.2f}"] = score
887	
888	    results["sk_score"] = results.get("pride_a1.00", 0)
889	    results["st_score"] = results.get("pride_a0.00", 0)
890	    results["pride"] = results.get("pride_a0.50", 0)
891	
892	    return results
893	
894	
895	ALPHA_SWEEP = [round(x * 0.1, 1) for x in range(11)]  # [0.0, 0.1, ..., 1.0]
896	
897	
898	def discover_models(base_dir: str) -> List[Tuple[str, str]]:
899	    """Discover model directories under base_dir."""
900	    models = []
901	    for entry in sorted(os.listdir(base_dir)):
902	        model_dir = os.path.join(base_dir, entry)
903	        if not os.path.isdir(model_dir):
904	            continue
905	        seed_dirs = glob.glob(os.path.join(model_dir, "seed*"))
906	        if seed_dirs:
907	            models.append((entry, model_dir))
908	    return models
909	
910	
911	PRIDE_CSV_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libero_para_metadata.csv")
912	
913	
914	def batch_pride(base_dir: str, output_dir: str, pride_csv: str,
915	                baseline_sr: float = None):
916	    """
917	    Run PRIDE computation for all models under base_dir.
918	    Also generates action-axis bar charts and PRIDE sweep.
919	    """
920	    models = discover_models(base_dir)
921	    if not models:
922	        print(f"[ERROR] No models found under: {base_dir}")
923	        return
924	
925	    print(f"Loading PRIDE CSV: {pride_csv}")
926	    pride_lookup = load_pride_csv(pride_csv)
927	    print(f"  {len(pride_lookup)} paraphrase entries loaded")
928	
929	    os.makedirs(output_dir, exist_ok=True)
930	
931	    # ---- Collect heatmaps for action bar charts ----
932	    model_heatmaps = {}
933	    for model_name, model_path in models:
934	        print(f"\n--- Aggregating {model_name} for action bars ---")
935	        heatmap_df, _, _, _ = aggregate_across_seeds(model_path)
936	        model_heatmaps[model_name] = heatmap_df
937	
938	    # ---- Generate action bar charts ----
939	    print(f"\n{'#'*75}")
940	    print(f"  Generating Action-axis Bar Charts")
941	    print(f"{'#'*75}")
942	    bl_dict = {m: baseline_sr for m in model_heatmaps} if baseline_sr else None
943	    generate_action_bar_charts(model_heatmaps, output_dir, baseline_srs=bl_dict)
944	
945	    # ---- PRIDE sweep ----
946	    print(f"\n{'#'*75}")
947	    print(f"  PRIDE Sweep")
948	    print(f"{'#'*75}")
949	
950	    rows = []
951	    for model_name, model_path in models:
952	        print(f"\n--- {model_name} ---")
953	        result = compute_model_pride(model_path, pride_lookup, alphas=ALPHA_SWEEP)
954	        row = {"model": model_name, "sr": result["sr"]}
955	        for alpha in ALPHA_SWEEP:
956	            row[f"a{alpha:.2f}"] = result[f"pride_a{alpha:.2f}"]
957	        rows.append(row)
958	
959	    order_map = {name: i for i, name in enumerate(MODEL_ORDER)}
960	    rows.sort(key=lambda r: order_map.get(r["model"], len(MODEL_ORDER)))
961	
962	    print(f"\n[PRIDE]")
963	    print("=" * 75)
964	    print(f"{'Model':<30} {'SR':>8} {'PRIDE':>10} {'S_K':>10} {'S_T':>10}")
965	    print(f"{'':30} {'':>8} {'(SK.5/ST.5)':>10} {'(SK1/ST0)':>10} {'(SK0/ST1)':>10}")
966	    print("-" * 75)
967	    for r in rows:
968	        print(f"{r['model']:<30} {r['sr']:>8.1f} {r['a0.50']:>10.1f} "
969	              f"{r['a1.00']:>10.1f} {r['a0.00']:>10.1f}")
970	    print("=" * 75)
971	
972	    df = pd.DataFrame(rows)
973	    rename_map = {}
974	    for a in ALPHA_SWEEP:
975	        rename_map[f"a{a:.2f}"] = f"SK={a:.1f}/ST={1-a:.1f}"
976	    df = df.rename(columns=rename_map)
977	    csv_path = os.path.join(output_dir, "pride_comparison.csv")
978	    df.to_csv(csv_path, index=False)
979	    print(f"\nSaved: {csv_path}")
980	
981	    plot_path = os.path.join(output_dir, "pride_sweep.png")
982	    plot_pride_sweep(csv_path, plot_path, mode_label="PRIDE")
983	
984	
985	
986	def plot_pride_sweep(csv_path: str, output_path: str, mode_label: str = "PD"):
987	    """
988	    Line plot: x = SK weight (0.0 → 1.0), y = PRIDE score.
989	    One line per model. SR shown as dashed horizontal.
990	    Shows per-model slope and average slope.
991	    """
992	    df = pd.read_csv(csv_path)
993	
994	    alpha_cols = [c for c in df.columns if c.startswith("SK=")]
995	    alphas = []
996	    for c in alpha_cols:
997	        sk_val = float(c.split("/")[0].split("=")[1])
998	        alphas.append(sk_val)
999	
1000	    sorted_pairs = sorted(zip(alphas, alpha_cols))
1001	    alphas_sorted = [p[0] for p in sorted_pairs]
1002	    cols_sorted = [p[1] for p in sorted_pairs]
1003	
1004	    # ★ Sort by score at α=0 (top line in chart = top row in table)
1005	    df["_score"] = df[cols_sorted[0]]  # α=0.0 score
1006	    df = df.sort_values("_score", ascending=False).reset_index(drop=True)
1007	    df = df.drop(columns=["_score"])
1008	
1009	    # ★ Wider figure + more table space
1010	    fig, (ax, ax_tbl) = plt.subplots(1, 2, figsize=(11, 5),
1011	                                      gridspec_kw={"width_ratios": [2.5, 1.5]})
1012	
1013	    slopes = []
1014	    model_names_list = []
1015	    model_colors_used = []
1016	    for idx, (_, row) in enumerate(df.iterrows()):
1017	        model = row["model"]
1018	        sr = row["sr"]
1019	        scores = [row[c] for c in cols_sorted]
1020	        color = MODEL_COLORS_FIXED.get(model, plt.cm.tab10(idx / max(len(df), 1)))
1021	
1022	        slope = np.polyfit(alphas_sorted, scores, 1)[0]
1023	        slopes.append(slope)
1024	        model_names_list.append(model)
1025	        model_colors_used.append(color)
1026	
1027	        ax.plot(alphas_sorted, scores, "-o", color=color, linewidth=2.5,
1028	                markersize=6, alpha=0.85)
1029	        ax.axhline(y=sr, color=color, linestyle=":", linewidth=1, alpha=0.25)
1030	
1031	    ax.set_xticks(alphas_sorted)
1032	    x_labels = []
1033	    for a in alphas_sorted:
1034	        if a == 0.0:
1035	            x_labels.append(f"{a:.1f}\n$S_K$=0\n$S_T$=1")
1036	        elif a == 0.5:
1037	            x_labels.append(f"{a:.1f}\n$S_K$=.5\n$S_T$=.5")
1038	        elif a == 1.0:
1039	            x_labels.append(f"{a:.1f}\n$S_K$=1\n$S_T$=0")
1040	        else:
1041	            x_labels.append(f"{a:.1f}")
1042	    ax.set_xticklabels(x_labels, fontsize=7)
1043	    ax.set_xlabel("α", fontsize=11, fontweight="bold")
1044	    ax.set_ylabel("PRIDE Score", fontsize=11, fontweight="bold")
1045	    ax.set_ylim(20, 85)
1046	    ax.grid(axis="y", alpha=0.2, linestyle="--")
1047	    ax.tick_params(axis="y", labelsize=9)
1048	
1049	    ax_tbl.axis("off")
1050	
1051	    avg_slope = np.mean(slopes)
1052	    table_data = []
1053	    cell_colors = []
1054	    for i, (m, s) in enumerate(zip(model_names_list, slopes)):
1055	        color = model_colors_used[i]
1056	        table_data.append([m, f"{s:+.1f}"])
1057	        rgba = plt.cm.colors.to_rgba(color)
1058	        cell_colors.append([(rgba[0], rgba[1], rgba[2], 0.15), "white"])
1059	    table_data.append(["Average", f"{avg_slope:+.1f}"])
1060	    cell_colors.append(["#F5F5DC", "#F5F5DC"])
1061	
1062	    # ★ colWidths: Model gets more space, Slope gets less
1063	    tbl = ax_tbl.table(
1064	        cellText=table_data,
1065	        colLabels=["Model", "Slope"],
1066	        colWidths=[0.42, 0.18],
1067	        loc="center",
1068	        cellLoc="left",
1069	        cellColours=cell_colors,
1070	    )
1071	    tbl.auto_set_font_size(False)
1072	    tbl.set_fontsize(11)
1073	    tbl.scale(1.3, 2.3)
1074	
1075	    for j in range(2):
1076	        tbl[0, j].set_facecolor("#D8D8D8")
1077	        tbl[0, j].set_text_props(fontweight="bold", fontsize=10)
1078	        tbl[len(table_data), j].set_text_props(fontweight="bold", fontsize=10)
1079	    # Color model names + bold slope values
1080	    for i, (m, color) in enumerate(zip(model_names_list, model_colors_used)):
1081	        tbl[i + 1, 0].set_text_props(color=color, fontweight="bold")
1082	        tbl[i + 1, 1].set_text_props(fontweight="bold")
1083	
1084	    fig.suptitle(f"PRIDE α Sweep — {mode_label}",
1085	                 fontsize=12, fontweight="bold", y=0.99)
1086	
1087	    plt.tight_layout(rect=[0, 0, 1, 0.95])
1088	    plt.savefig(output_path, dpi=200, bbox_inches="tight")
1089	    plt.close()
1090	    print(f"  Saved: {output_path}")
1091	    print(f"  Avg slope: {avg_slope:+.1f} pp per 1.0 SK shift")
1092	
1093	
1094	
1095	# ============================================================================
1096	# Model-wise average heatmap
1097	# ============================================================================
1098	
1099	def average_heatmap(json_paths: List[Tuple[str, str]], output_dir: str,
1100	                    baseline_sr: float = None, pride_sweep_dir: str = None):
1101	    """
1102	    Load multiple models' aggregated_cells.json, average SR cell-by-cell,
1103	    and plot a single "average across models" heatmap + action bar charts.
1104	    """
1105	    os.makedirs(output_dir, exist_ok=True)
1106	
1107	    cell_srs = defaultdict(list)
1108	
1109	    model_heatmaps = {}
1110	
1111	    for model_name, json_path in json_paths:
1112	        print(f"  Loading: {model_name} from {json_path}")
1113	        with open(json_path, "r") as f:
1114	            data = json.load(f)
1115	
1116	        # Build per-model heatmap for action bars
1117	        rows = []
1118	        for key, val in data.items():
1119	            obj_low = val["obj_low"]
1120	            act_low = val["act_low"]
1121	            mean_sr = val["mean_sr"]
1122	            if mean_sr is not None:
1123	                cell_srs[(obj_low, act_low)].append(mean_sr)
1124	            rows.append({"obj": obj_low, "act": act_low, "sr": mean_sr if mean_sr is not None else np.nan})
1125	
1126	        mdf = pd.DataFrame(rows)
1127	        hdf = mdf.pivot(index="obj", columns="act", values="sr")
1128	        hdf = hdf.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)
1129	        model_heatmaps[model_name] = hdf
1130	
1131	    # Build averaged heatmap
1132	    rows = []
1133	    for obj in OBJ_TYPES_ORDER:
1134	        for act in ACT_TYPES_ORDER:
1135	            srs = cell_srs.get((obj, act), [])
1136	            mean = np.mean(srs) if srs else np.nan
1137	            std = np.std(srs) if len(srs) > 1 else 0.0
1138	            rows.append({"obj": obj, "act": act, "mean_sr": mean, "std_sr": std,
1139	                          "n_models": len(srs)})
1140	
1141	    df = pd.DataFrame(rows)
1142	
1143	    heatmap_df = df.pivot(index="obj", columns="act", values="mean_sr")
1144	    heatmap_df = heatmap_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)
1145	
1146	    std_df = df.pivot(index="obj", columns="act", values="std_sr")
1147	    std_df = std_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)
1148	
1149	    print(f"\n{'='*60}")
1150	    print("Model-wise Average Heatmap (43 cells)")
1151	    print(f"{'='*60}")
1152	    for obj in OBJ_TYPES_ORDER:
1153	        for act in ACT_TYPES_ORDER:
1154	            if obj == "None" and act == "None":
1155	                continue
1156	            val = heatmap_df.loc[obj, act]
1157	            std = std_df.loc[obj, act]
1158	            if not np.isnan(val):
1159	                print(f"  {OBJ_DISPLAY.get(obj, obj):>15} × {ACT_DISPLAY.get(act, act):<15}  "
1160	                      f"{val:5.1f} ± {std:4.1f}")
1161	
1162	    para_vals = []
1163	    for obj in OBJ_TYPES_ORDER:
1164	        for act in ACT_TYPES_ORDER:
1165	            if obj == "None" and act == "None":
1166	                continue
1167	            v = heatmap_df.loc[obj, act]
1168	            if not np.isnan(v):
1169	                para_vals.append(v)
1170	    print(f"\n  Overall avg: {np.mean(para_vals):.1f} ± {np.std(para_vals):.1f}")
1171	
1172	    csv_path = os.path.join(output_dir, "model_average_heatmap.csv")
1173	    df.to_csv(csv_path, index=False)
1174	    print(f"\n  Saved: {csv_path}")
1175	
1176	    png_path = os.path.join(output_dir, "model_average_heatmap.png")
1177	    plot_heatmap(heatmap_df, std_df, png_path,
1178	                 model_name="Model Average")
1179	
1180	    # ---- Action bar charts from individual models ----
1181	    print(f"\n  Generating Action-axis Bar Charts...")
1182	    bl_dict = {m: baseline_sr for m in model_heatmaps} if baseline_sr else None
1183	    generate_action_bar_charts(model_heatmaps, output_dir, baseline_srs=bl_dict)
1184	
1185	    # ---- PRIDE sweep plots (if CSV exists) ----
1186	    if pride_sweep_dir:
1187	        csv_path = os.path.join(pride_sweep_dir, "pride_comparison.csv")
1188	        if os.path.exists(csv_path):
1189	            plot_path = os.path.join(output_dir, "pride_sweep.png")
1190	            print(f"\n  Generating PRIDE sweep plot from {csv_path}...")
1191	            plot_pride_sweep(csv_path, plot_path, mode_label="PRIDE")
1192	        else:
1193	            print(f"  [SKIP] {csv_path} not found")
1194	
1195	
1196	# ============================================================================
1197	# Main
1198	# ============================================================================
1199	
1200	def main():
1201	    parser = argparse.ArgumentParser(
1202	        description="Generate paraphrase success rate heatmap from structured JSON logs."
1203	    )
1204	    parser.add_argument(
1205	        "--model_path", type=str, default=None,
1206	        help="Path to model log directory containing seed* folders.",
1207	    )
1208	    parser.add_argument(
1209	        "--model_name", type=str, default=None,
1210	        help="Display name for the model (used in title & filenames). "
1211	             "Defaults to last component of model_path.",
1212	    )
1213	    parser.add_argument(
1214	        "--output_dir", type=str, default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "output"),
1215	        help="Output directory for heatmap images and JSONs.",
1216	    )
1217	    parser.add_argument(
1218	        "--base_dir", type=str, default=None,
1219	        help="Base directory with multiple model subdirs. "
1220	             "Runs PRIDE comparison across all models.",
1221	    )
1222	    parser.add_argument(
1223	        "--pride_csv", type=str, default=PRIDE_CSV_DEFAULT,
1224	        help="Path to pre-computed SK/ST CSV.",
1225	    )
1226	    parser.add_argument(
1227	        "--plot_only", action="store_true",
1228	        help="Skip computation, re-plot from existing pride_comparison_*.csv in output_dir.",
1229	    )
1230	    parser.add_argument(
1231	        "--average_models", nargs="+", default=None,
1232	        help="Compute model-wise average heatmap. Specs as 'Name:path/to/aggregated_cells.json'",
1233	    )
1234	    parser.add_argument(
1235	        "--baseline_sr", type=float, default=None,
1236	        help="Baseline SR for (None,None) cell in action bar charts. "
1237	             "Adds 'Original' bar. E.g., --baseline_sr 95.0",
1238	    )
1239	    parser.add_argument(
1240	        "--pride_sweep_dir", type=str, default=None,
1241	        help="Directory containing pride_comparison.csv. "
1242	             "If provided, PRIDE sweep plots are generated in --average_models mode.",
1243	    )
1244	    args = parser.parse_args()
1245	
1246	    # Average models mode
1247	    if args.average_models:
1248	        print("=== Model-wise Average Heatmap ===")
1249	        json_paths = []
1250	        for spec in args.average_models:
1251	            name, path = spec.split(":", 1)
1252	            json_paths.append((name, path))
1253	        average_heatmap(json_paths, args.output_dir, baseline_sr=args.baseline_sr,
1254	                        pride_sweep_dir=args.pride_sweep_dir)
1255	        return
1256	
1257	    # Plot-only mode
1258	    if args.plot_only:
1259	        print("=== Plot-only mode ===")
1260	        csv_path = os.path.join(args.output_dir, "pride_comparison.csv")
1261	        if os.path.exists(csv_path):
1262	            plot_path = os.path.join(args.output_dir, "pride_sweep.png")
1263	            plot_pride_sweep(csv_path, plot_path, mode_label="PRIDE")
1264	        else:
1265	            print(f"  [SKIP] {csv_path} not found")
1266	        return
1267	
1268	    # Batch mode
1269	    if args.base_dir:
1270	        batch_pride(args.base_dir, args.output_dir, args.pride_csv,
1271	                    baseline_sr=args.baseline_sr)
1272	        return
1273	
1274	    # Single model mode
1275	    if args.model_path is None:
1276	        print("[ERROR] --model_path or --base_dir required")
1277	        sys.exit(1)
1278	
1279	    dir_name = os.path.basename(args.model_path.rstrip("/"))
1280	    if args.model_name is None:
1281	        args.model_name = dir_name
1282	
1283	    # Output goes into metrics/output/&lt;dir_name>/
1284	    output_base = os.path.join(args.output_dir, dir_name)
1285	    vis_dir = os.path.join(output_base, "visualization")
1286	    res_dir = os.path.join(output_base, "results")
1287	    os.makedirs(vis_dir, exist_ok=True)
1288	    os.makedirs(res_dir, exist_ok=True)
1289	
1290	    print("=" * 70)
1291	    print(f"Model: {args.model_name}")
1292	    print(f"Path:  {args.model_path}")
1293	    print(f"Output: {output_base}")
1294	    print("=" * 70)
1295	
1296	    # 1. Aggregate
1297	    print("\n[1/6] Aggregating across seeds...")
1298	    heatmap_df, std_df, per_seed_stats, full_df = aggregate_across_seeds(args.model_path)
1299	
1300	    # 2. Save JSONs (detail)
1301	    print("\n[2/6] Saving JSON results...")
1302	    save_per_seed_json(per_seed_stats, res_dir, args.model_name)
1303	    save_aggregated_json(heatmap_df, std_df, res_dir, args.model_name)
1304	
1305	    # 3. Save CSVs (detail + overview)
1306	    print("\n[3/6] Saving CSV results...")
1307	    save_aggregated_csv(full_df, res_dir, args.model_name)
1308	
1309	    # 4. Plot heatmap
1310	    print("\n[4/6] Plotting heatmap...")
1311	    heatmap_png = os.path.join(vis_dir, "paraphrase_heatmap.png")
1312	    plot_heatmap(
1313	        heatmap_df, std_df, heatmap_png,
1314	        model_name=args.model_name,
1315	    )
1316	
1317	    # 5. Action bar charts (single model)
1318	    print("\n[5/6] Generating action-axis bar charts...")
1319	    act_bar_dir = vis_dir
1320	    bl_dict = {args.model_name: args.baseline_sr} if args.baseline_sr else None
1321	    generate_action_bar_charts(
1322	        {args.model_name: heatmap_df},
1323	        act_bar_dir,
1324	        baseline_srs=bl_dict,
1325	    )
1326	
1327	    # 6. PRIDE
1328	    print(f"\n[6/6] Computing PRIDE (α sweep)...")
1329	    pride_lookup = load_pride_csv(args.pride_csv)
1330	
1331	    result = compute_model_pride(args.model_path, pride_lookup, alphas=ALPHA_SWEEP)
1332	
1333	    print(f"\n[PRIDE]")
1334	    print(f"{'='*65}")
1335	    print(f"  Model:   {args.model_name}")
1336	    print(f"  SR:      {result['sr']:.1f}")
1337	    print(f"  PRIDE:   {result['pride']:.1f}  (SK=0.5/ST=0.5)")
1338	    print(f"  S_K:     {result['sk_score']:.1f}  (SK=1.0/ST=0.0)")
1339	    print(f"  S_T:     {result['st_score']:.1f}  (SK=0.0/ST=1.0)")
1340	    print(f"  ---")
1341	    for a in ALPHA_SWEEP:
1342	        print(f"  SK={a:.1f}/ST={1-a:.1f}:  {result[f'pride_a{a:.2f}']:.1f}")
1343	    print(f"{'='*65}")
1344	
1345	    row = {"model": args.model_name, "sr": result["sr"]}
1346	    for a in ALPHA_SWEEP:
1347	        row[f"SK={a:.1f}/ST={1-a:.1f}"] = result[f"pride_a{a:.2f}"]
1348	    pride_row = pd.DataFrame([row])
1349	    csv_path = os.path.join(res_dir, "pride_comparison.csv")
1350	    if os.path.exists(csv_path):
1351	        existing = pd.read_csv(csv_path)
1352	        existing = existing[existing["model"] != args.model_name]
1353	        pride_row = pd.concat([existing, pride_row], ignore_index=True)
1354	    pride_row.to_csv(csv_path, index=False)
1355	    print(f"  Appended to: {csv_path}")
1356	
1357	    plot_path = os.path.join(vis_dir, "pride_sweep.png")
1358	    plot_pride_sweep(csv_path, plot_path, mode_label="PRIDE")
1359	
1360	    print("\n" + "=" * 70)
1361	    print("DONE")
1362	    print("=" * 70)
1363	
1364	
1365	if __name__ == "__main__":
1366	    main()
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "160e657d-f127-4042-8595-32162d868788",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/tmp/LIBERO-Para/metrics/analyze_results.py",
      "content": "#!/usr/bin/env python3\n\"\"\"\ngenerate_paraphrase_table.py\n\nGenerates a 4x11 (obj x act) paraphrase success rate heatmap from\nstructured JSON eval logs.\n\nDirectory structure expected:\n    model_path/\n        seed7/\n            eval0.json  ... eval9.json\n            meta.json\n            summary.json\n        seed8/\n        ...\n        seed11/\n\nEach eval{N}.json has:\n    {\n      \"eval_id\": N,\n      \"original_instruction\": ...,\n      \"episodes\": [\n        {\n          \"paraphrase_type\": \"act\" | \"obj\" | \"comp\",\n          \"categories\": [...],\n          \"subcategories\": [...],  # comp: [obj_subcat, act_subcat]\n          \"success\": true/false,\n          ...\n        }, ...\n      ]\n    }\n\nUsage:\n    python generate_paraphrase_table.py \\\n        --model_path ../logs_para/xiaomi \\\n        --model_name \"OpenVLA-OFT\" \\\n        --output_dir ./metrics/output\n\"\"\"\n\nimport argparse\nimport json\nimport glob\nimport os\nimport sys\nfrom collections import defaultdict\nfrom typing import Dict, List, Tuple, Optional\n\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nimport seaborn as sns\nfrom matplotlib.colors import LinearSegmentedColormap\n\n\n# ============================================================================\n# Constants\n# ============================================================================\n\n# Y-axis (obj paraphrase types)\nOBJ_TYPES_ORDER = [\n    \"None\",\n    \"addition_deletion\",\n    \"same_polarity_contextual\",\n    \"same_polarity_habitual\",\n]\n\n# X-axis (act paraphrase types)\nACT_TYPES_ORDER = [\n    \"None\",\n    \"addition_deletion\",\n    \"same_polarity_contextual\",\n    \"same_polarity_habitual\",\n    \"coordination\",\n    \"subordination\",\n    \"need_statement\",\n    \"embedded_imperative\",\n    \"permission_directive\",\n    \"question_directive\",\n    \"hint\",\n]\n\n# Fixed model display order\nMODEL_ORDER = [\n    \"OpenVLA-OFT-goal\",\n    \"OpenVLA-OFT_mixed\",\n    \"Pi05\",\n    \"Pi05-ExpertOnly\",\n    \"X-VLA\",\n    \"VLA-Adapter\",\n    \"Xiaomi-Robotics-0\",\n]\n\n# Fixed model colors (consistent across all plots)\nMODEL_COLORS_FIXED = {\n    \"OpenVLA-OFT-goal\":   \"#1f77b4\",  # blue\n    \"OpenVLA-OFT_mixed\":  \"#ff7f0e\",  # orange\n    \"Pi05\":               \"#d62728\",  # red\n    \"Pi05-ExpertOnly\":    \"#8c564b\",  # brown\n    \"X-VLA\":              \"#9467bd\",  # purple\n    \"VLA-Adapter\":        \"#2ca02c\",  # green\n    \"Xiaomi-Robotics-0\":  \"#17becf\",  # cyan\n}\n\n# Display labels (shorter names for heatmap axes)\nOBJ_DISPLAY = {\n    \"None\": \"None\",\n    \"addition_deletion\": \"Addition\",\n    \"same_polarity_contextual\": \"SP-contextual\",\n    \"same_polarity_habitual\": \"SP-habitual\",\n}\n\nACT_DISPLAY = {\n    \"None\": \"None\",\n    \"addition_deletion\": \"Addition\",\n    \"same_polarity_contextual\": \"SP-contextual\",\n    \"same_polarity_habitual\": \"SP-habitual\",\n    \"coordination\": \"Coordination\",\n    \"subordination\": \"Subordination\",\n    \"need_statement\": \"Need\",\n    \"embedded_imperative\": \"Embedded\",\n    \"permission_directive\": \"Permission\",\n    \"question_directive\": \"Question\",\n    \"hint\": \"Hint\",\n}\n\n# Act paraphrase categories (indices into ACT_TYPES_ORDER, excluding \"None\" at 0)\nACT_CATEGORIES = {\n    \"Lexical\":     [\"addition_deletion\", \"same_polarity_contextual\", \"same_polarity_habitual\"],\n    \"Structural\":  [\"coordination\", \"subordination\"],\n    \"Pragmatic\":   [\"need_statement\", \"embedded_imperative\", \"permission_directive\",\n                    \"question_directive\", \"hint\"],\n}\n\nCATEGORY_COLORS = {\n    \"Lexical\":    \"#2166ac\",\n    \"Structural\": \"#d6604d\",\n    \"Pragmatic\":  \"#7b3294\",\n}\n\n# Act types excluding None (for bar charts)\nACT_TYPES_PARA = ACT_TYPES_ORDER[1:]\n\nACT_DISPLAY_SHORT = {\n    \"addition_deletion\": \"Addition\",\n    \"same_polarity_contextual\": \"SP-ctx\",\n    \"same_polarity_habitual\": \"SP-hab\",\n    \"coordination\": \"Coord\",\n    \"subordination\": \"Subord\",\n    \"need_statement\": \"Need\",\n    \"embedded_imperative\": \"Embedded\",\n    \"permission_directive\": \"Permission\",\n    \"question_directive\": \"Question\",\n    \"hint\": \"Hint\",\n}\n\n# Map each act type to its category\nACT_TYPE_TO_CATEGORY = {}\nfor cat, types in ACT_CATEGORIES.items():\n    for t in types:\n        ACT_TYPE_TO_CATEGORY[t] = cat\n\n\ndef discover_seeds(model_path: str) -> List[str]:\n    \"\"\"Find all seed directories under model_path.\"\"\"\n    seed_dirs = sorted(glob.glob(os.path.join(model_path, \"seed*\")))\n    seed_dirs = [d for d in seed_dirs if os.path.isdir(d)]\n    if not seed_dirs:\n        print(f\"[ERROR] No seed directories found in: {model_path}\")\n        sys.exit(1)\n    print(f\"Found {len(seed_dirs)} seeds: {[os.path.basename(d) for d in seed_dirs]}\")\n    return seed_dirs\n\n\ndef load_eval_jsons(seed_dir: str) -> List[dict]:\n    \"\"\"Load all eval{N}.json files from a seed directory.\"\"\"\n    eval_files = sorted(glob.glob(os.path.join(seed_dir, \"eval*.json\")))\n    # Exclude eval_unknown.json if exists\n    eval_files = [f for f in eval_files if \"unknown\" not in os.path.basename(f)]\n    \n    all_episodes = []\n    for ef in eval_files:\n        with open(ef, \"r\") as f:\n            data = json.load(f)\n        eval_id = data.get(\"eval_id\", -1)\n        for ep in data.get(\"episodes\", []):\n            ep[\"_eval_id\"] = eval_id\n            all_episodes.append(ep)\n    \n    return all_episodes\n\n\ndef episode_to_cell(ep: dict) -> Tuple[str, str]:\n    \"\"\"\n    Map an episode to (obj_low, act_low) cell coordinates.\n\n    Rules:\n        act  → obj_low = \"None\",             act_low = subcategories[0]\n        obj  → obj_low = subcategories[0],    act_low = \"None\"\n        comp → obj_low = subcategories[0],    act_low = subcategories[1]\n    \"\"\"\n    ptype = ep[\"paraphrase_type\"]\n    subcats = ep.get(\"subcategories\", [])\n\n    if ptype == \"act\":\n        return (\"None\", subcats[0] if subcats else \"unknown\")\n    elif ptype == \"obj\":\n        return (subcats[0] if subcats else \"unknown\", \"None\")\n    elif ptype == \"comp\":\n        obj_sub = subcats[0] if len(subcats) > 0 else \"unknown\"\n        act_sub = subcats[1] if len(subcats) > 1 else \"unknown\"\n        return (obj_sub, act_sub)\n    else:\n        return (\"unknown\", \"unknown\")\n\n\n# ============================================================================\n# Aggregation\n# ============================================================================\n\ndef aggregate_seed(episodes: List[dict]) -> Dict[Tuple[str, str], dict]:\n    \"\"\"\n    Aggregate episodes within one seed into per-cell stats.\n    Returns: {(obj_low, act_low): {\"successes\": int, \"total\": int}}\n    \"\"\"\n    cells = defaultdict(lambda: {\"successes\": 0, \"total\": 0})\n    for ep in episodes:\n        obj_low, act_low = episode_to_cell(ep)\n        cells[(obj_low, act_low)][\"total\"] += 1\n        if ep.get(\"success\", False):\n            cells[(obj_low, act_low)][\"successes\"] += 1\n    return dict(cells)\n\n\ndef aggregate_across_seeds(\n    model_path: str,\n) -> Tuple[pd.DataFrame, pd.DataFrame, dict, pd.DataFrame]:\n    \"\"\"\n    Load all seeds, compute per-seed cell stats, then average across seeds.\n\n    Returns:\n        heatmap_df: DataFrame with mean success rates (index=obj, columns=act)\n        std_df: DataFrame with std of success rates\n        per_seed_stats: {seed_name: {(obj, act): {successes, total, sr}}}\n        full_df: DataFrame with all rows (obj, act, mean, std, n_seeds, per-seed SRs)\n    \"\"\"\n    seed_dirs = discover_seeds(model_path)\n    per_seed_stats = {}\n    all_cell_srs = defaultdict(list)  # {(obj, act): [sr_seed1, sr_seed2, ...]}\n    seed_names = []\n\n    for seed_dir in seed_dirs:\n        seed_name = os.path.basename(seed_dir)\n        seed_names.append(seed_name)\n        episodes = load_eval_jsons(seed_dir)\n        print(f\"  {seed_name}: {len(episodes)} episodes loaded\")\n\n        cell_stats = aggregate_seed(episodes)\n\n        # Compute per-seed SR for each cell\n        for cell_key, stats in cell_stats.items():\n            sr = stats[\"successes\"] / stats[\"total\"] if stats[\"total\"] > 0 else 0.0\n            stats[\"success_rate\"] = sr\n            all_cell_srs[cell_key].append(sr)\n\n        per_seed_stats[seed_name] = cell_stats\n\n    # Build full dataframe rows\n    rows = []\n    for obj_low in OBJ_TYPES_ORDER:\n        for act_low in ACT_TYPES_ORDER:\n            srs = all_cell_srs.get((obj_low, act_low), [])\n            mean_sr = np.mean(srs) * 100 if srs else np.nan\n            std_sr = np.std(srs) * 100 if len(srs) > 1 else 0.0\n            var_sr = np.var(srs) * 10000 if len(srs) > 1 else 0.0  # variance in %^2\n\n            row = {\n                \"obj_type\": obj_low,\n                \"act_type\": act_low,\n                \"mean_sr\": mean_sr,\n                \"std_sr\": std_sr,\n                \"var_sr\": var_sr,\n                \"n_seeds\": len(srs),\n            }\n            # Add per-seed SR columns\n            for i, sname in enumerate(sorted(seed_names)):\n                cell = per_seed_stats.get(sname, {}).get((obj_low, act_low), {})\n                seed_sr = cell.get(\"success_rate\", np.nan)\n                row[sname] = round(seed_sr * 100, 2) if not np.isnan(seed_sr) else np.nan\n            rows.append(row)\n\n    full_df = pd.DataFrame(rows)\n\n    heatmap_df = full_df.pivot(index=\"obj_type\", columns=\"act_type\", values=\"mean_sr\")\n    heatmap_df = heatmap_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)\n\n    std_df = full_df.pivot(index=\"obj_type\", columns=\"act_type\", values=\"std_sr\")\n    std_df = std_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)\n\n    return heatmap_df, std_df, per_seed_stats, full_df\n\n\n# ============================================================================\n# CSV Export\n# ============================================================================\n\ndef save_aggregated_csv(full_df: pd.DataFrame, output_dir: str, model_name: str):\n    \"\"\"\n    Save aggregated CSV with columns:\n        obj_type, act_type, mean_sr, std_sr, var_sr, n_seeds, seed7, seed8, ...\n    Also computes overall summary rows (total paraphrase avg, per-type avg, etc.)\n    \"\"\"\n    # --- Per-cell CSV ---\n    csv_path = os.path.join(output_dir, f\"{model_name}_aggregated.csv\")\n    \n    # Round numeric columns\n    export_df = full_df.copy()\n    for col in export_df.columns:\n        if col not in (\"obj_type\", \"act_type\", \"n_seeds\"):\n            export_df[col] = export_df[col].round(2)\n    \n    # Sort by obj_type order, then act_type order\n    obj_order = {v: i for i, v in enumerate(OBJ_TYPES_ORDER)}\n    act_order = {v: i for i, v in enumerate(ACT_TYPES_ORDER)}\n    export_df[\"_obj_order\"] = export_df[\"obj_type\"].map(obj_order)\n    export_df[\"_act_order\"] = export_df[\"act_type\"].map(act_order)\n    export_df = export_df.sort_values([\"_obj_order\", \"_act_order\"]).drop(columns=[\"_obj_order\", \"_act_order\"])\n    \n    export_df.to_csv(csv_path, index=False)\n    print(f\"  Saved: {csv_path}\")\n\n    # --- Summary CSV (marginals + overall) ---\n    summary_rows = []\n    \n    # Filter out (None, None) = original instruction\n    para_df = full_df[~((full_df[\"obj_type\"] == \"None\") & (full_df[\"act_type\"] == \"None\"))].copy()\n    \n    # Overall paraphrase average\n    overall_mean = para_df[\"mean_sr\"].mean()\n    overall_std = para_df[\"mean_sr\"].std()\n    summary_rows.append({\n        \"category\": \"ALL_PARAPHRASE\",\n        \"type\": \"overall\",\n        \"mean_sr\": round(overall_mean, 2),\n        \"std_across_cells\": round(overall_std, 2),\n        \"n_cells\": len(para_df),\n    })\n\n    # Per obj_type marginal (average across all act_types)\n    for obj in OBJ_TYPES_ORDER:\n        subset = para_df[para_df[\"obj_type\"] == obj]\n        if len(subset) > 0:\n            summary_rows.append({\n                \"category\": \"obj_marginal\",\n                \"type\": obj,\n                \"mean_sr\": round(subset[\"mean_sr\"].mean(), 2),\n                \"std_across_cells\": round(subset[\"mean_sr\"].std(), 2),\n                \"n_cells\": len(subset),\n            })\n\n    # Per act_type marginal (average across all obj_types)\n    for act in ACT_TYPES_ORDER:\n        subset = para_df[para_df[\"act_type\"] == act]\n        if len(subset) > 0:\n            summary_rows.append({\n                \"category\": \"act_marginal\",\n                \"type\": act,\n                \"mean_sr\": round(subset[\"mean_sr\"].mean(), 2),\n                \"std_across_cells\": round(subset[\"mean_sr\"].std(), 2),\n                \"n_cells\": len(subset),\n            })\n\n    # act-only average (obj=None, act!=None)\n    act_only = para_df[(para_df[\"obj_type\"] == \"None\") & (para_df[\"act_type\"] != \"None\")]\n    if len(act_only) > 0:\n        summary_rows.append({\n            \"category\": \"paraphrase_scope\",\n            \"type\": \"act_only\",\n            \"mean_sr\": round(act_only[\"mean_sr\"].mean(), 2),\n            \"std_across_cells\": round(act_only[\"mean_sr\"].std(), 2),\n            \"n_cells\": len(act_only),\n        })\n\n    # obj-only average (obj!=None, act=None)\n    obj_only = para_df[(para_df[\"obj_type\"] != \"None\") & (para_df[\"act_type\"] == \"None\")]\n    if len(obj_only) > 0:\n        summary_rows.append({\n            \"category\": \"paraphrase_scope\",\n            \"type\": \"obj_only\",\n            \"mean_sr\": round(obj_only[\"mean_sr\"].mean(), 2),\n            \"std_across_cells\": round(obj_only[\"mean_sr\"].std(), 2),\n            \"n_cells\": len(obj_only),\n        })\n\n    # comp average (obj!=None, act!=None)\n    comp = para_df[(para_df[\"obj_type\"] != \"None\") & (para_df[\"act_type\"] != \"None\")]\n    if len(comp) > 0:\n        summary_rows.append({\n            \"category\": \"paraphrase_scope\",\n            \"type\": \"comp\",\n            \"mean_sr\": round(comp[\"mean_sr\"].mean(), 2),\n            \"std_across_cells\": round(comp[\"mean_sr\"].std(), 2),\n            \"n_cells\": len(comp),\n        })\n\n    summary_df = pd.DataFrame(summary_rows)\n    summary_path = os.path.join(output_dir, f\"{model_name}_summary.csv\")\n    summary_df.to_csv(summary_path, index=False)\n    print(f\"  Saved: {summary_path}\")\n\n\n# ============================================================================\n# Saving per-seed JSON\n# ============================================================================\n\ndef save_per_seed_json(per_seed_stats: dict, output_dir: str, model_name: str):\n    \"\"\"Save per-seed cell success rates as JSON.\"\"\"\n    for seed_name, cell_stats in per_seed_stats.items():\n        out = {}\n        for (obj_low, act_low), stats in cell_stats.items():\n            key = f\"{obj_low}+{act_low}\"\n            out[key] = {\n                \"obj_low\": obj_low,\n                \"act_low\": act_low,\n                \"successes\": stats[\"successes\"],\n                \"total\": stats[\"total\"],\n                \"success_rate\": round(stats.get(\"success_rate\", 0.0) * 100, 2),\n            }\n\n        path = os.path.join(output_dir, f\"{model_name}_{seed_name}_cells.json\")\n        with open(path, \"w\") as f:\n            json.dump(out, f, indent=2)\n        print(f\"  Saved: {path}\")\n\n\ndef save_aggregated_json(heatmap_df: pd.DataFrame, std_df: pd.DataFrame,\n                         output_dir: str, model_name: str):\n    \"\"\"Save the aggregated (mean across seeds) heatmap data as JSON.\"\"\"\n    result = {}\n    for obj_low in OBJ_TYPES_ORDER:\n        for act_low in ACT_TYPES_ORDER:\n            key = f\"{obj_low}+{act_low}\"\n            mean_val = heatmap_df.loc[obj_low, act_low]\n            std_val = std_df.loc[obj_low, act_low]\n            result[key] = {\n                \"obj_low\": obj_low,\n                \"act_low\": act_low,\n                \"mean_sr\": round(float(mean_val), 2) if not np.isnan(mean_val) else None,\n                \"std_sr\": round(float(std_val), 2) if not np.isnan(std_val) else None,\n            }\n\n    path = os.path.join(output_dir, f\"{model_name}_aggregated_cells.json\")\n    with open(path, \"w\") as f:\n        json.dump(result, f, indent=2)\n    print(f\"  Saved: {path}\")\n\n\n# ============================================================================\n# Heatmap Visualization\n# ============================================================================\n\ndef get_colormap():\n    \"\"\"Custom red-to-green colormap: aggressive red for low success, green only for high.\"\"\"\n    colors = [\n        (0.0,  \"#67001f\"),   # 0%  - dark crimson\n        (0.10, \"#d73027\"),   # 10%\n        (0.30, \"#fc8d59\"),   # 30%\n        (0.50, \"#fee090\"),   # 50%\n        (0.65, \"#d9ef8b\"),   # 65%\n        (0.80, \"#66bd63\"),   # 80%\n        (0.92, \"#1a9850\"),   # 92%\n        (1.0,  \"#00441b\"),   # 100%\n    ]\n    return LinearSegmentedColormap.from_list(\n        \"custom_red_green\", [(pos, c) for pos, c in colors], N=256\n    )\n\n\ndef plot_heatmap(\n    heatmap_df: pd.DataFrame,\n    std_df: pd.DataFrame,\n    png_path: str,\n    model_name: str = \"\",\n):\n    \"\"\"\n    Plot 4x11 paraphrase combination heatmap.\n    (None, None) cell is masked.\n    \"\"\"\n    # Build mask: (None, None) = original, mask it\n    mask = np.zeros_like(heatmap_df.values, dtype=bool)\n    if \"None\" in heatmap_df.index and \"None\" in heatmap_df.columns:\n        none_row = list(heatmap_df.index).index(\"None\")\n        none_col = list(heatmap_df.columns).index(\"None\")\n        mask[none_row, none_col] = True\n\n    # Build annotation strings\n    annot_array = np.empty_like(heatmap_df.values, dtype=object)\n    for i, obj in enumerate(heatmap_df.index):\n        for j, act in enumerate(heatmap_df.columns):\n            val = heatmap_df.iloc[i, j]\n            std = std_df.iloc[i, j]\n            if mask[i, j]:\n                annot_array[i, j] = \"\"\n            elif np.isnan(val):\n                annot_array[i, j] = \"N/A\"\n            else:\n                annot_array[i, j] = f\"{val:.1f}\"\n\n    fig, ax = plt.subplots(figsize=(18, 5.5))\n    cmap = get_colormap()\n\n    obj_display = [OBJ_DISPLAY.get(o, o) for o in heatmap_df.index]\n    act_display = [ACT_DISPLAY.get(a, a) for a in heatmap_df.columns]\n\n    sns.heatmap(\n        heatmap_df.values.astype(float),\n        annot=annot_array,\n        fmt=\"\",\n        cmap=cmap,\n        mask=mask,\n        cbar_kws={\"label\": \"Success Rate (%)\", \"shrink\": 0.8},\n        linewidths=0.8,\n        linecolor=\"white\",\n        ax=ax,\n        vmin=0,\n        vmax=100,\n        annot_kws={\"fontsize\": 20, \"fontweight\": \"bold\"},\n        xticklabels=act_display,\n        yticklabels=obj_display,\n    )\n\n    title = \"Success Rate by Paraphrase Type Combination\"\n    if model_name:\n        title = f\"{model_name}: {title}\"\n    ax.set_xlabel(\"Act Paraphrase Type\", fontsize=16, fontweight=\"normal\", labelpad=10)\n    ax.set_ylabel(\"Obj Paraphrase Type\", fontsize=16, fontweight=\"normal\", labelpad=10)\n    ax.set_title(title, fontsize=18, fontweight=\"bold\", pad=15)\n\n    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha=\"right\", fontsize=16, fontweight=\"bold\")\n    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, fontsize=16, fontweight=\"bold\")\n\n    cbar = ax.collections[0].colorbar\n    cbar.ax.tick_params(labelsize=12)\n    cbar.ax.set_ylabel(\"Success Rate (%)\", fontsize=14, fontweight=\"normal\")\n\n    plt.tight_layout()\n    plt.savefig(png_path, dpi=300, bbox_inches=\"tight\")\n    plt.close()\n    print(f\"  Saved: {png_path}\")\n\n\n# ============================================================================\n# Action-axis Bar Charts\n# ============================================================================\n\ndef _extract_act_marginals(heatmap_df: pd.DataFrame,\n                           baseline_sr: float = None) -> Dict[str, float]:\n    \"\"\"\n    From a 4x11 heatmap_df, compute act-axis marginal SR.\n    For each act type, average SR across all obj types.\n\n    If baseline_sr is provided, include act=\"None\" marginal\n    using baseline_sr for the (None, None) cell.\n    \"\"\"\n    marginals = {}\n\n    # Include \"None\" if baseline_sr is given\n    if baseline_sr is not None:\n        vals = [baseline_sr]  # (None, None) cell\n        for obj in OBJ_TYPES_ORDER:\n            if obj == \"None\":\n                continue\n            v = heatmap_df.loc[obj, \"None\"]\n            if not np.isnan(v):\n                vals.append(v)\n        marginals[\"None\"] = np.mean(vals) if vals else np.nan\n\n    for act in ACT_TYPES_PARA:\n        vals = []\n        for obj in OBJ_TYPES_ORDER:\n            v = heatmap_df.loc[obj, act]\n            if not np.isnan(v):\n                vals.append(v)\n        marginals[act] = np.mean(vals) if vals else np.nan\n    return marginals\n\n\ndef _extract_act_marginals_from_json(json_path: str) -> Dict[str, float]:\n    \"\"\"Extract act marginals from aggregated_cells.json.\"\"\"\n    with open(json_path, \"r\") as f:\n        data = json.load(f)\n\n    # Collect per act type\n    act_vals = defaultdict(list)\n    for key, val in data.items():\n        obj_low = val[\"obj_low\"]\n        act_low = val[\"act_low\"]\n        sr = val[\"mean_sr\"]\n        if act_low == \"None\":\n            continue  # skip obj-only rows for act analysis\n        if obj_low == \"None\" and act_low == \"None\":\n            continue\n        if sr is not None:\n            act_vals[act_low].append(sr)\n\n    marginals = {}\n    for act in ACT_TYPES_PARA:\n        vals = act_vals.get(act, [])\n        marginals[act] = np.mean(vals) if vals else np.nan\n    return marginals\n\n\ndef plot_act_type_bars(\n    model_marginals: Dict[str, Dict[str, float]],\n    output_dir: str,\n    filename_prefix: str = \"act_type_bars\",\n):\n    \"\"\"\n    Chart 1 (1-column): Mean SR per act type, bar color = category.\n    If \"None\" is present in marginals, show it as first bar (gray).\n    \"\"\"\n    # Determine act types to plot\n    has_none = any(\"None\" in m for m in model_marginals.values())\n    act_types = ([\"None\"] + ACT_TYPES_PARA) if has_none else ACT_TYPES_PARA\n    n_types = len(act_types)\n    x = np.arange(n_types)\n\n    means, bar_colors = [], []\n    for act in act_types:\n        vals = [m.get(act, np.nan) for m in model_marginals.values()]\n        vals = [v for v in vals if not np.isnan(v)]\n        means.append(np.mean(vals) if vals else 0)\n        if act == \"None\":\n            bar_colors.append(\"#555555\")\n        else:\n            cat = ACT_TYPE_TO_CATEGORY.get(act, \"Lexical\")\n            bar_colors.append(CATEGORY_COLORS.get(cat, \"#333333\"))\n\n    fig, ax = plt.subplots(figsize=(7, 3.5))\n\n    ax.bar(x, means, 0.7, color=bar_colors,\n           edgecolor=\"white\", linewidth=0.5, alpha=0.85)\n\n    for xi, m in zip(x, means):\n        ax.text(xi, m + 0.8, f\"{m:.1f}\", ha=\"center\", va=\"bottom\",\n                fontsize=7, fontweight=\"bold\")\n\n    act_labels = []\n    for a in act_types:\n        if a == \"None\":\n            act_labels.append(\"None\")\n        else:\n            act_labels.append(ACT_DISPLAY_SHORT.get(a, a))\n    ax.set_xticks(x)\n    ax.set_xticklabels(act_labels, rotation=45, ha=\"right\", fontsize=8, fontweight=\"bold\")\n    for tick_label, act in zip(ax.get_xticklabels(), act_types):\n        if act == \"None\":\n            tick_label.set_color(\"#555555\")\n        else:\n            cat = ACT_TYPE_TO_CATEGORY.get(act, \"\")\n            tick_label.set_color(CATEGORY_COLORS.get(cat, \"black\"))\n\n    _draw_category_spans(ax, act_types)\n\n    ax.set_xlabel(\"Act Paraphrase Type\", fontsize=9, fontweight=\"bold\", labelpad=6)\n    ax.set_ylabel(\"Success Rate (%)\", fontsize=9, fontweight=\"bold\")\n    ax.set_ylim(0, 105)\n    ax.grid(axis=\"y\", alpha=0.2, linestyle=\"--\")\n    ax.tick_params(axis=\"y\", labelsize=7)\n\n    plt.tight_layout()\n    path = os.path.join(output_dir, f\"{filename_prefix}.png\")\n    plt.savefig(path, dpi=300, bbox_inches=\"tight\")\n    print(f\"  Saved: {path}\")\n    plt.close()\n\n\ndef plot_act_category_bars(\n    model_marginals: Dict[str, Dict[str, float]],\n    output_dir: str,\n    filename_prefix: str = \"act_category_bars\",\n):\n    \"\"\"\n    Chart 2 (1-column): Mean SR per category (Lexical/Structural/Pragmatic).\n    Error bar = std across models' category-level means.\n    \"\"\"\n    categories = list(ACT_CATEGORIES.keys())\n    x = np.arange(len(categories))\n\n    cat_means, cat_colors = [], []\n    for cat in categories:\n        cat_types = ACT_CATEGORIES[cat]\n        per_model = []\n        for marginals in model_marginals.values():\n            vals = [marginals.get(t, np.nan) for t in cat_types]\n            vals = [v for v in vals if not np.isnan(v)]\n            if vals:\n                per_model.append(np.mean(vals))\n        cat_means.append(np.mean(per_model) if per_model else 0)\n        cat_colors.append(CATEGORY_COLORS[cat])\n\n    fig, ax = plt.subplots(figsize=(4, 3.5))\n\n    ax.bar(x, cat_means, 0.55, color=cat_colors,\n           edgecolor=\"white\", linewidth=0.5, alpha=0.85)\n\n    for xi, m in zip(x, cat_means):\n        ax.text(xi, m + 1.0, f\"{m:.1f}\", ha=\"center\", va=\"bottom\",\n                fontsize=9, fontweight=\"bold\")\n\n    ax.set_xticks(x)\n    ax.set_xticklabels(categories, fontsize=10, fontweight=\"bold\")\n    for tick_label, cat in zip(ax.get_xticklabels(), categories):\n        tick_label.set_color(CATEGORY_COLORS.get(cat, \"black\"))\n\n    ax.set_ylabel(\"Success Rate (%)\", fontsize=9, fontweight=\"bold\")\n    ax.set_ylim(0, 105)\n    ax.grid(axis=\"y\", alpha=0.2, linestyle=\"--\")\n    ax.tick_params(axis=\"y\", labelsize=7)\n\n    plt.tight_layout()\n    path = os.path.join(output_dir, f\"{filename_prefix}.png\")\n    plt.savefig(path, dpi=300, bbox_inches=\"tight\")\n    print(f\"  Saved: {path}\")\n    plt.close()\n\n\n\ndef _draw_category_spans(ax, act_types):\n    \"\"\"Draw category bracket lines above the x-axis area.\"\"\"\n    # Find index ranges for each category\n    for cat, cat_types in ACT_CATEGORIES.items():\n        indices = [i for i, a in enumerate(act_types) if a in cat_types]\n        if not indices:\n            continue\n        color = CATEGORY_COLORS[cat]\n        x_left = min(indices) - 0.4\n        x_right = max(indices) + 0.4\n        x_center = (x_left + x_right) / 2\n\n        y_pos = 1.02\n        h = 0.02\n\n        ax.plot([x_left, x_right], [y_pos, y_pos],\n                color=color, linewidth=2.5, clip_on=False,\n                transform=ax.get_xaxis_transform())\n        ax.plot([x_left, x_left], [y_pos - h, y_pos],\n                color=color, linewidth=2.5, clip_on=False,\n                transform=ax.get_xaxis_transform())\n        ax.plot([x_right, x_right], [y_pos - h, y_pos],\n                color=color, linewidth=2.5, clip_on=False,\n                transform=ax.get_xaxis_transform())\n        ax.text(x_center, y_pos + 0.03, cat,\n                ha=\"center\", va=\"bottom\", fontsize=9, fontweight=\"bold\",\n                color=color, transform=ax.get_xaxis_transform(), clip_on=False)\n\n\ndef generate_action_bar_charts(\n    model_heatmaps: Dict[str, pd.DataFrame],\n    output_dir: str,\n    baseline_srs: Dict[str, float] = None,\n):\n    \"\"\"\n    Entry point: given {model_name: heatmap_df}, generate all 3 action bar charts.\n    baseline_srs: {model_name: baseline SR for (None,None) cell}.\n                  If None, \"None\" bar is omitted.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n\n    # 1. Extract marginals\n    model_marginals = {}\n    model_baselines = {}\n    for model, hdf in model_heatmaps.items():\n        bl = baseline_srs.get(model) if baseline_srs else None\n        model_marginals[model] = _extract_act_marginals(hdf, baseline_sr=bl)\n        # Baseline = overall paraphrase mean (all cells excl None,None)\n        vals = []\n        for obj in OBJ_TYPES_ORDER:\n            for act in ACT_TYPES_ORDER:\n                if obj == \"None\" and act == \"None\":\n                    continue\n                v = hdf.loc[obj, act]\n                if not np.isnan(v):\n                    vals.append(v)\n        model_baselines[model] = np.mean(vals) if vals else 0\n\n    # 2. Plot\n    print(\"\\n  [Action Bars 1/3] Per act type...\")\n    plot_act_type_bars(model_marginals, output_dir)\n\n    print(\"  [Action Bars 2/3] Per category...\")\n    plot_act_category_bars(model_marginals, output_dir)\n\n    print(\"  [Action Bars] Done.\")\n\n\n# ============================================================================\n# PRIDE computation (SK + ST + PD from pre-computed CSV)\n# ============================================================================\n\n\ndef load_pride_csv(csv_path: str) -> dict:\n    \"\"\"\n    Load pre-computed SK/ST CSV.\n    Key by instruction text (unique per paraphrase).\n    Returns lookup: instruction_text -> {\"sk\": keyword_sim, \"st\": structural_sim}\n    \"\"\"\n    df = pd.read_csv(csv_path)\n    lookup = {}\n    for _, row in df.iterrows():\n        key = str(row[\"new_instruction\"]).strip().lower()\n        lookup[key] = {\n            \"sk\": float(row[\"keyword_similarity\"]),\n            \"st\": float(row[\"structural_similarity\"]),\n        }\n\n    print(f\"  Lookup: {len(lookup)} unique instructions (from {len(df)} CSV rows)\")\n    if lookup:\n        sample = list(lookup.items())[:3]\n        for k, v in sample:\n            print(f\"    \\\"{k[:50]}...\\\" → sk={v['sk']:.3f}, st={v['st']:.3f}\")\n\n    return lookup\n\n\ndef compute_model_pride(model_path: str, pride_lookup: dict,\n                        alphas: List[float] = None) -> dict:\n    \"\"\"\n    Compute PRIDE score for a single model.\n\n    PD_i = 1 - (alpha * SK_i + (1 - alpha) * ST_i)\n    PRIDE(alpha) = sum(success_i * PD_i) / sum(PD_i) * 100\n    \"\"\"\n    if alphas is None:\n        alphas = [0.0, 0.5, 1.0]\n\n    seed_dirs = discover_seeds(model_path)\n\n    # Collect per-episode (sk, st, success) for alpha sweep\n    episode_data = []\n    n_total = 0\n    n_matched = 0\n    unmatched_keys = []\n\n    for seed_dir in seed_dirs:\n        episodes = load_eval_jsons(seed_dir)\n        for ep in episodes:\n            key = str(ep.get(\"paraphrased_instruction\", \"\")).strip().lower()\n            n_total += 1\n\n            info = pride_lookup.get(key)\n            if info is None:\n                if len(unmatched_keys) < 5:\n                    unmatched_keys.append(key[:60])\n                continue\n\n            n_matched += 1\n            sk = info[\"sk\"]\n            st = info[\"st\"]\n            success = 1.0 if ep.get(\"success\", False) else 0.0\n            episode_data.append((sk, st, success))\n\n    print(f\"  Matching: {n_matched}/{n_total} episodes ({n_total - n_matched} unmatched)\")\n    if unmatched_keys:\n        print(f\"  Sample unmatched: {unmatched_keys[:3]}\")\n    if episode_data:\n        sks = [d[0] for d in episode_data]\n        sts = [d[1] for d in episode_data]\n        print(f\"  Similarity ranges: SK=[{min(sks):.3f}, {max(sks):.3f}], \"\n              f\"ST=[{min(sts):.3f}, {max(sts):.3f}]\")\n\n    n_episodes = len(episode_data)\n    n_success = int(sum(s for _, _, s in episode_data))\n    sr = round(n_success / n_episodes * 100, 1) if n_episodes > 0 else 0\n\n    results = {\"sr\": sr, \"n_episodes\": n_episodes, \"n_success\": n_success}\n\n    for alpha in alphas:\n        actual = 0.0\n        total = 0.0\n        for sk, st, success in episode_data:\n            pd = 1.0 - (alpha * sk + (1.0 - alpha) * st)\n            total += pd\n            if success:\n                actual += pd\n        score = round(actual / total * 100, 1) if total > 0 else 0\n        results[f\"pride_a{alpha:.2f}\"] = score\n\n    results[\"sk_score\"] = results.get(\"pride_a1.00\", 0)\n    results[\"st_score\"] = results.get(\"pride_a0.00\", 0)\n    results[\"pride\"] = results.get(\"pride_a0.50\", 0)\n\n    return results\n\n\nALPHA_SWEEP = [round(x * 0.1, 1) for x in range(11)]  # [0.0, 0.1, ..., 1.0]\n\n\ndef discover_models(base_dir: str) -> List[Tuple[str, str]]:\n    \"\"\"Discover model directories under base_dir.\"\"\"\n    models = []\n    for entry in sorted(os.listdir(base_dir)):\n        model_dir = os.path.join(base_dir, entry)\n        if not os.path.isdir(model_dir):\n            continue\n        seed_dirs = glob.glob(os.path.join(model_dir, \"seed*\"))\n        if seed_dirs:\n            models.append((entry, model_dir))\n    return models\n\n\nPRIDE_CSV_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), \"libero_para_metadata.csv\")\n\n\ndef batch_pride(base_dir: str, output_dir: str, pride_csv: str,\n                baseline_sr: float = None):\n    \"\"\"\n    Run PRIDE computation for all models under base_dir.\n    Also generates action-axis bar charts and PRIDE sweep.\n    \"\"\"\n    models = discover_models(base_dir)\n    if not models:\n        print(f\"[ERROR] No models found under: {base_dir}\")\n        return\n\n    print(f\"Loading PRIDE CSV: {pride_csv}\")\n    pride_lookup = load_pride_csv(pride_csv)\n    print(f\"  {len(pride_lookup)} paraphrase entries loaded\")\n\n    os.makedirs(output_dir, exist_ok=True)\n\n    # ---- Collect heatmaps for action bar charts ----\n    model_heatmaps = {}\n    for model_name, model_path in models:\n        print(f\"\\n--- Aggregating {model_name} for action bars ---\")\n        heatmap_df, _, _, _ = aggregate_across_seeds(model_path)\n        model_heatmaps[model_name] = heatmap_df\n\n    # ---- Generate action bar charts ----\n    print(f\"\\n{'#'*75}\")\n    print(f\"  Generating Action-axis Bar Charts\")\n    print(f\"{'#'*75}\")\n    bl_dict = {m: baseline_sr for m in model_heatmaps} if baseline_sr else None\n    generate_action_bar_charts(model_heatmaps, output_dir, baseline_srs=bl_dict)\n\n    # ---- PRIDE sweep ----\n    print(f\"\\n{'#'*75}\")\n    print(f\"  PRIDE Sweep\")\n    print(f\"{'#'*75}\")\n\n    rows = []\n    for model_name, model_path in models:\n        print(f\"\\n--- {model_name} ---\")\n        result = compute_model_pride(model_path, pride_lookup, alphas=ALPHA_SWEEP)\n        row = {\"model\": model_name, \"sr\": result[\"sr\"]}\n        for alpha in ALPHA_SWEEP:\n            row[f\"a{alpha:.2f}\"] = result[f\"pride_a{alpha:.2f}\"]\n        rows.append(row)\n\n    order_map = {name: i for i, name in enumerate(MODEL_ORDER)}\n    rows.sort(key=lambda r: order_map.get(r[\"model\"], len(MODEL_ORDER)))\n\n    print(f\"\\n[PRIDE]\")\n    print(\"=\" * 75)\n    print(f\"{'Model':<30} {'SR':>8} {'PRIDE':>10} {'S_K':>10} {'S_T':>10}\")\n    print(f\"{'':30} {'':>8} {'(SK.5/ST.5)':>10} {'(SK1/ST0)':>10} {'(SK0/ST1)':>10}\")\n    print(\"-\" * 75)\n    for r in rows:\n        print(f\"{r['model']:<30} {r['sr']:>8.1f} {r['a0.50']:>10.1f} \"\n              f\"{r['a1.00']:>10.1f} {r['a0.00']:>10.1f}\")\n    print(\"=\" * 75)\n\n    df = pd.DataFrame(rows)\n    rename_map = {}\n    for a in ALPHA_SWEEP:\n        rename_map[f\"a{a:.2f}\"] = f\"SK={a:.1f}/ST={1-a:.1f}\"\n    df = df.rename(columns=rename_map)\n    csv_path = os.path.join(output_dir, \"pride_comparison.csv\")\n    df.to_csv(csv_path, index=False)\n    print(f\"\\nSaved: {csv_path}\")\n\n    plot_path = os.path.join(output_dir, \"pride_sweep.png\")\n    plot_pride_sweep(csv_path, plot_path, mode_label=\"PRIDE\")\n\n\n\ndef plot_pride_sweep(csv_path: str, output_path: str, mode_label: str = \"PD\"):\n    \"\"\"\n    Line plot: x = SK weight (0.0 → 1.0), y = PRIDE score.\n    One line per model. SR shown as dashed horizontal.\n    Shows per-model slope and average slope.\n    \"\"\"\n    df = pd.read_csv(csv_path)\n\n    alpha_cols = [c for c in df.columns if c.startswith(\"SK=\")]\n    alphas = []\n    for c in alpha_cols:\n        sk_val = float(c.split(\"/\")[0].split(\"=\")[1])\n        alphas.append(sk_val)\n\n    sorted_pairs = sorted(zip(alphas, alpha_cols))\n    alphas_sorted = [p[0] for p in sorted_pairs]\n    cols_sorted = [p[1] for p in sorted_pairs]\n\n    # ★ Sort by score at α=0 (top line in chart = top row in table)\n    df[\"_score\"] = df[cols_sorted[0]]  # α=0.0 score\n    df = df.sort_values(\"_score\", ascending=False).reset_index(drop=True)\n    df = df.drop(columns=[\"_score\"])\n\n    # ★ Wider figure + more table space\n    fig, (ax, ax_tbl) = plt.subplots(1, 2, figsize=(11, 5),\n                                      gridspec_kw={\"width_ratios\": [2.5, 1.5]})\n\n    slopes = []\n    model_names_list = []\n    model_colors_used = []\n    for idx, (_, row) in enumerate(df.iterrows()):\n        model = row[\"model\"]\n        sr = row[\"sr\"]\n        scores = [row[c] for c in cols_sorted]\n        color = MODEL_COLORS_FIXED.get(model, plt.cm.tab10(idx / max(len(df), 1)))\n\n        slope = np.polyfit(alphas_sorted, scores, 1)[0]\n        slopes.append(slope)\n        model_names_list.append(model)\n        model_colors_used.append(color)\n\n        ax.plot(alphas_sorted, scores, \"-o\", color=color, linewidth=2.5,\n                markersize=6, alpha=0.85)\n        ax.axhline(y=sr, color=color, linestyle=\":\", linewidth=1, alpha=0.25)\n\n    ax.set_xticks(alphas_sorted)\n    x_labels = []\n    for a in alphas_sorted:\n        if a == 0.0:\n            x_labels.append(f\"{a:.1f}\\n$S_K$=0\\n$S_T$=1\")\n        elif a == 0.5:\n            x_labels.append(f\"{a:.1f}\\n$S_K$=.5\\n$S_T$=.5\")\n        elif a == 1.0:\n            x_labels.append(f\"{a:.1f}\\n$S_K$=1\\n$S_T$=0\")\n        else:\n            x_labels.append(f\"{a:.1f}\")\n    ax.set_xticklabels(x_labels, fontsize=7)\n    ax.set_xlabel(\"α\", fontsize=11, fontweight=\"bold\")\n    ax.set_ylabel(\"PRIDE Score\", fontsize=11, fontweight=\"bold\")\n    ax.set_ylim(20, 85)\n    ax.grid(axis=\"y\", alpha=0.2, linestyle=\"--\")\n    ax.tick_params(axis=\"y\", labelsize=9)\n\n    ax_tbl.axis(\"off\")\n\n    avg_slope = np.mean(slopes)\n    table_data = []\n    cell_colors = []\n    for i, (m, s) in enumerate(zip(model_names_list, slopes)):\n        color = model_colors_used[i]\n        table_data.append([m, f\"{s:+.1f}\"])\n        rgba = plt.cm.colors.to_rgba(color)\n        cell_colors.append([(rgba[0], rgba[1], rgba[2], 0.15), \"white\"])\n    table_data.append([\"Average\", f\"{avg_slope:+.1f}\"])\n    cell_colors.append([\"#F5F5DC\", \"#F5F5DC\"])\n\n    # ★ colWidths: Model gets more space, Slope gets less\n    tbl = ax_tbl.table(\n        cellText=table_data,\n        colLabels=[\"Model\", \"Slope\"],\n        colWidths=[0.42, 0.18],\n        loc=\"center\",\n        cellLoc=\"left\",\n        cellColours=cell_colors,\n    )\n    tbl.auto_set_font_size(False)\n    tbl.set_fontsize(11)\n    tbl.scale(1.3, 2.3)\n\n    for j in range(2):\n        tbl[0, j].set_facecolor(\"#D8D8D8\")\n        tbl[0, j].set_text_props(fontweight=\"bold\", fontsize=10)\n        tbl[len(table_data), j].set_text_props(fontweight=\"bold\", fontsize=10)\n    # Color model names + bold slope values\n    for i, (m, color) in enumerate(zip(model_names_list, model_colors_used)):\n        tbl[i + 1, 0].set_text_props(color=color, fontweight=\"bold\")\n        tbl[i + 1, 1].set_text_props(fontweight=\"bold\")\n\n    fig.suptitle(f\"PRIDE α Sweep — {mode_label}\",\n                 fontsize=12, fontweight=\"bold\", y=0.99)\n\n    plt.tight_layout(rect=[0, 0, 1, 0.95])\n    plt.savefig(output_path, dpi=200, bbox_inches=\"tight\")\n    plt.close()\n    print(f\"  Saved: {output_path}\")\n    print(f\"  Avg slope: {avg_slope:+.1f} pp per 1.0 SK shift\")\n\n\n\n# ============================================================================\n# Model-wise average heatmap\n# ============================================================================\n\ndef average_heatmap(json_paths: List[Tuple[str, str]], output_dir: str,\n                    baseline_sr: float = None, pride_sweep_dir: str = None):\n    \"\"\"\n    Load multiple models' aggregated_cells.json, average SR cell-by-cell,\n    and plot a single \"average across models\" heatmap + action bar charts.\n    \"\"\"\n    os.makedirs(output_dir, exist_ok=True)\n\n    cell_srs = defaultdict(list)\n\n    model_heatmaps = {}\n\n    for model_name, json_path in json_paths:\n        print(f\"  Loading: {model_name} from {json_path}\")\n        with open(json_path, \"r\") as f:\n            data = json.load(f)\n\n        # Build per-model heatmap for action bars\n        rows = []\n        for key, val in data.items():\n            obj_low = val[\"obj_low\"]\n            act_low = val[\"act_low\"]\n            mean_sr = val[\"mean_sr\"]\n            if mean_sr is not None:\n                cell_srs[(obj_low, act_low)].append(mean_sr)\n            rows.append({\"obj\": obj_low, \"act\": act_low, \"sr\": mean_sr if mean_sr is not None else np.nan})\n\n        mdf = pd.DataFrame(rows)\n        hdf = mdf.pivot(index=\"obj\", columns=\"act\", values=\"sr\")\n        hdf = hdf.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)\n        model_heatmaps[model_name] = hdf\n\n    # Build averaged heatmap\n    rows = []\n    for obj in OBJ_TYPES_ORDER:\n        for act in ACT_TYPES_ORDER:\n            srs = cell_srs.get((obj, act), [])\n            mean = np.mean(srs) if srs else np.nan\n            std = np.std(srs) if len(srs) > 1 else 0.0\n            rows.append({\"obj\": obj, \"act\": act, \"mean_sr\": mean, \"std_sr\": std,\n                          \"n_models\": len(srs)})\n\n    df = pd.DataFrame(rows)\n\n    heatmap_df = df.pivot(index=\"obj\", columns=\"act\", values=\"mean_sr\")\n    heatmap_df = heatmap_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)\n\n    std_df = df.pivot(index=\"obj\", columns=\"act\", values=\"std_sr\")\n    std_df = std_df.reindex(index=OBJ_TYPES_ORDER, columns=ACT_TYPES_ORDER)\n\n    print(f\"\\n{'='*60}\")\n    print(\"Model-wise Average Heatmap (43 cells)\")\n    print(f\"{'='*60}\")\n    for obj in OBJ_TYPES_ORDER:\n        for act in ACT_TYPES_ORDER:\n            if obj == \"None\" and act == \"None\":\n                continue\n            val = heatmap_df.loc[obj, act]\n            std = std_df.loc[obj, act]\n            if not np.isnan(val):\n                print(f\"  {OBJ_DISPLAY.get(obj, obj):>15} × {ACT_DISPLAY.get(act, act):<15}  \"\n                      f\"{val:5.1f} ± {std:4.1f}\")\n\n    para_vals = []\n    for obj in OBJ_TYPES_ORDER:\n        for act in ACT_TYPES_ORDER:\n            if obj == \"None\" and act == \"None\":\n                continue\n            v = heatmap_df.loc[obj, act]\n            if not np.isnan(v):\n                para_vals.append(v)\n    print(f\"\\n  Overall avg: {np.mean(para_vals):.1f} ± {np.std(para_vals):.1f}\")\n\n    csv_path = os.path.join(output_dir, \"model_average_heatmap.csv\")\n    df.to_csv(csv_path, index=False)\n    print(f\"\\n  Saved: {csv_path}\")\n\n    png_path = os.path.join(output_dir, \"model_average_heatmap.png\")\n    plot_heatmap(heatmap_df, std_df, png_path,\n                 model_name=\"Model Average\")\n\n    # ---- Action bar charts from individual models ----\n    print(f\"\\n  Generating Action-axis Bar Charts...\")\n    bl_dict = {m: baseline_sr for m in model_heatmaps} if baseline_sr else None\n    generate_action_bar_charts(model_heatmaps, output_dir, baseline_srs=bl_dict)\n\n    # ---- PRIDE sweep plots (if CSV exists) ----\n    if pride_sweep_dir:\n        csv_path = os.path.join(pride_sweep_dir, \"pride_comparison.csv\")\n        if os.path.exists(csv_path):\n            plot_path = os.path.join(output_dir, \"pride_sweep.png\")\n            print(f\"\\n  Generating PRIDE sweep plot from {csv_path}...\")\n            plot_pride_sweep(csv_path, plot_path, mode_label=\"PRIDE\")\n        else:\n            print(f\"  [SKIP] {csv_path} not found\")\n\n\n# ============================================================================\n# Main\n# ============================================================================\n\ndef main():\n    parser = argparse.ArgumentParser(\n        description=\"Generate paraphrase success rate heatmap from structured JSON logs.\"\n    )\n    parser.add_argument(\n        \"--model_path\", type=str, default=None,\n        help=\"Path to model log directory containing seed* folders.\",\n    )\n    parser.add_argument(\n        \"--model_name\", type=str, default=None,\n        help=\"Display name for the model (used in title & filenames). \"\n             \"Defaults to last component of model_path.\",\n    )\n    parser.add_argument(\n        \"--output_dir\", type=str, default=os.path.join(os.path.dirname(os.path.abspath(__file__)), \"output\"),\n        help=\"Output directory for heatmap images and JSONs.\",\n    )\n    parser.add_argument(\n        \"--base_dir\", type=str, default=None,\n        help=\"Base directory with multiple model subdirs. \"\n             \"Runs PRIDE comparison across all models.\",\n    )\n    parser.add_argument(\n        \"--pride_csv\", type=str, default=PRIDE_CSV_DEFAULT,\n        help=\"Path to pre-computed SK/ST CSV.\",\n    )\n    parser.add_argument(\n        \"--plot_only\", action=\"store_true\",\n        help=\"Skip computation, re-plot from existing pride_comparison_*.csv in output_dir.\",\n    )\n    parser.add_argument(\n        \"--average_models\", nargs=\"+\", default=None,\n        help=\"Compute model-wise average heatmap. Specs as 'Name:path/to/aggregated_cells.json'\",\n    )\n    parser.add_argument(\n        \"--baseline_sr\", type=float, default=None,\n        help=\"Baseline SR for (None,None) cell in action bar charts. \"\n             \"Adds 'Original' bar. E.g., --baseline_sr 95.0\",\n    )\n    parser.add_argument(\n        \"--pride_sweep_dir\", type=str, default=None,\n        help=\"Directory containing pride_comparison.csv. \"\n             \"If provided, PRIDE sweep plots are generated in --average_models mode.\",\n    )\n    args = parser.parse_args()\n\n    # Average models mode\n    if args.average_models:\n        print(\"=== Model-wise Average Heatmap ===\")\n        json_paths = []\n        for spec in args.average_models:\n            name, path = spec.split(\":\", 1)\n            json_paths.append((name, path))\n        average_heatmap(json_paths, args.output_dir, baseline_sr=args.baseline_sr,\n                        pride_sweep_dir=args.pride_sweep_dir)\n        return\n\n    # Plot-only mode\n    if args.plot_only:\n        print(\"=== Plot-only mode ===\")\n        csv_path = os.path.join(args.output_dir, \"pride_comparison.csv\")\n        if os.path.exists(csv_path):\n            plot_path = os.path.join(args.output_dir, \"pride_sweep.png\")\n            plot_pride_sweep(csv_path, plot_path, mode_label=\"PRIDE\")\n        else:\n            print(f\"  [SKIP] {csv_path} not found\")\n        return\n\n    # Batch mode\n    if args.base_dir:\n        batch_pride(args.base_dir, args.output_dir, args.pride_csv,\n                    baseline_sr=args.baseline_sr)\n        return\n\n    # Single model mode\n    if args.model_path is None:\n        print(\"[ERROR] --model_path or --base_dir required\")\n        sys.exit(1)\n\n    dir_name = os.path.basename(args.model_path.rstrip(\"/\"))\n    if args.model_name is None:\n        args.model_name = dir_name\n\n    # Output goes into metrics/output/&lt;dir_name>/\n    output_base = os.path.join(args.output_dir, dir_name)\n    vis_dir = os.path.join(output_base, \"visualization\")\n    res_dir = os.path.join(output_base, \"results\")\n    os.makedirs(vis_dir, exist_ok=True)\n    os.makedirs(res_dir, exist_ok=True)\n\n    print(\"=\" * 70)\n    print(f\"Model: {args.model_name}\")\n    print(f\"Path:  {args.model_path}\")\n    print(f\"Output: {output_base}\")\n    print(\"=\" * 70)\n\n    # 1. Aggregate\n    print(\"\\n[1/6] Aggregating across seeds...\")\n    heatmap_df, std_df, per_seed_stats, full_df = aggregate_across_seeds(args.model_path)\n\n    # 2. Save JSONs (detail)\n    print(\"\\n[2/6] Saving JSON results...\")\n    save_per_seed_json(per_seed_stats, res_dir, args.model_name)\n    save_aggregated_json(heatmap_df, std_df, res_dir, args.model_name)\n\n    # 3. Save CSVs (detail + overview)\n    print(\"\\n[3/6] Saving CSV results...\")\n    save_aggregated_csv(full_df, res_dir, args.model_name)\n\n    # 4. Plot heatmap\n    print(\"\\n[4/6] Plotting heatmap...\")\n    heatmap_png = os.path.join(vis_dir, \"paraphrase_heatmap.png\")\n    plot_heatmap(\n        heatmap_df, std_df, heatmap_png,\n        model_name=args.model_name,\n    )\n\n    # 5. Action bar charts (single model)\n    print(\"\\n[5/6] Generating action-axis bar charts...\")\n    act_bar_dir = vis_dir\n    bl_dict = {args.model_name: args.baseline_sr} if args.baseline_sr else None\n    generate_action_bar_charts(\n        {args.model_name: heatmap_df},\n        act_bar_dir,\n        baseline_srs=bl_dict,\n    )\n\n    # 6. PRIDE\n    print(f\"\\n[6/6] Computing PRIDE (α sweep)...\")\n    pride_lookup = load_pride_csv(args.pride_csv)\n\n    result = compute_model_pride(args.model_path, pride_lookup, alphas=ALPHA_SWEEP)\n\n    print(f\"\\n[PRIDE]\")\n    print(f\"{'='*65}\")\n    print(f\"  Model:   {args.model_name}\")\n    print(f\"  SR:      {result['sr']:.1f}\")\n    print(f\"  PRIDE:   {result['pride']:.1f}  (SK=0.5/ST=0.5)\")\n    print(f\"  S_K:     {result['sk_score']:.1f}  (SK=1.0/ST=0.0)\")\n    print(f\"  S_T:     {result['st_score']:.1f}  (SK=0.0/ST=1.0)\")\n    print(f\"  ---\")\n    for a in ALPHA_SWEEP:\n        print(f\"  SK={a:.1f}/ST={1-a:.1f}:  {result[f'pride_a{a:.2f}']:.1f}\")\n    print(f\"{'='*65}\")\n\n    row = {\"model\": args.model_name, \"sr\": result[\"sr\"]}\n    for a in ALPHA_SWEEP:\n        row[f\"SK={a:.1f}/ST={1-a:.1f}\"] = result[f\"pride_a{a:.2f}\"]\n    pride_row = pd.DataFrame([row])\n    csv_path = os.path.join(res_dir, \"pride_comparison.csv\")\n    if os.path.exists(csv_path):\n        existing = pd.read_csv(csv_path)\n        existing = existing[existing[\"model\"] != args.model_name]\n        pride_row = pd.concat([existing, pride_row], ignore_index=True)\n    pride_row.to_csv(csv_path, index=False)\n    print(f\"  Appended to: {csv_path}\")\n\n    plot_path = os.path.join(vis_dir, \"pride_sweep.png\")\n    plot_pride_sweep(csv_path, plot_path, mode_label=\"PRIDE\")\n\n    print(\"\\n\" + \"=\" * 70)\n    print(\"DONE\")\n    print(\"=\" * 70)\n\n\nif __name__ == \"__main__\":\n    main()",
      "numLines": 1366,
      "startLine": 1,
      "totalLines": 1366
    }
  }
}
```

</details>

---

### Assistant

_source line 44_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need. Let me also check our project's implementation to compare.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "6fc9229b-f829-429d-981a-06eb879e5bb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaiYrFFnZjVQkcGt4SfKCu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25700,
      "cache_read_input_tokens": 31075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25700
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

_source line 45_

现在查看我们项目的 PRIDE 实现。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "8084aa31-1b79-454e-919a-28ee99e5e9ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaiYrFFnZjVQkcGt4SfKCu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25700,
      "cache_read_input_tokens": 31075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25700
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

_source line 46_

<details open><summary>🔧 Tool call — Grep · `toolu_01GZhDGY39C5fkeZdLMRyKmN`</summary>

```json
{
  "pattern": "PRIDE|pride|paraphrase_distance|PD",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "2f5f9e0d-94b4-4342-aa3d-c18e6e58d4f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VaiYrFFnZjVQkcGt4SfKCu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 25700,
      "cache_read_input_tokens": 31075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 25700
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

_source line 47 · 2026-05-19T23:30:04.381Z_

<details><summary>↩ Tool result · `toolu_01GZhDGY39C5fkeZdLMRyKmN`</summary>

```text
Found 80 files
logs/workers/worker_research_pride-formula-verify_20260519T232737.log
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl
logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl
.claude/sessions/director_21ca1cc3/AGENTS.md
.claude/sessions/director_21ca1cc3/CLAUDE.md
AGENTS.md
.claude/CLAUDE.md
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl
report.md
checkpoints/phase1_lconsist_v1_cont_RUNNING_20260519T232658.json
registry.yaml
checkpoints/phase1_lconsist_v1_cont_ALLOCATED_20260519T232652.json
checkpoints/phase1_lconsist_v1_cont_QUEUED_20260519T232647.json
checkpoints/phase1_lconsist_v1_cont_PENDING_20260519T232644.json
checkpoints/phase1_lconsist_v1_DONE_20260519T232445.json
.claude/sessions/reviewer_8c7bb198/AGENTS.md
.claude/sessions/reviewer_8c7bb198/CLAUDE.md
logs/workers/worker_infra_restart-lconsist-training_20260519T231922.log
logs/workers/worker_code_merge-consist-transfer_20260519T232011.log
.claude/sessions/agent_413a00de/AGENTS.md
.claude/sessions/agent_413a00de/CLAUDE.md
ROADMAP.md
decisions.yaml
logs/workers/worker_code_l-transfer-dryrun_20260519T225748.log
checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225818.json
memory.md
logs/workers/worker_analysis_phase1_lconsist_v1_20260519T225345.log
logs/chats/cron_hook_phase1_lconsist_v1.jsonl
.claude/sessions/agent_56997cc0/AGENTS.md
.claude/sessions/agent_56997cc0/CLAUDE.md
checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225208.json
logs/workers/worker_code_eval-fixes_20260519T224913_result.json
logs/workers/worker_code_eval-fixes_20260519T224913.log
logs/workers/worker_code_training-status-fix_20260519T224853.log
logs/workers/worker_code_fix-and-relaunch_20260519T222907.log
logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json
logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log
logs/workers/worker_code_l-transfer-pair-validation_20260519T222514.log
logs/workers/worker_code_paraphrase-hit-rate_20260519T222554.log
checkpoints/phase1_lconsist_v1_RUNNING_20260519T222330.json
checkpoints/phase1_lconsist_v1_ALLOCATED_20260519T222324.json
checkpoints/phase1_lconsist_v1_QUEUED_20260519T222321.json
checkpoints/phase1_lconsist_v1_PENDING_20260519T222309.json
logs/workers/worker_code_l-transfer-impl_20260519T220356.log
logs/workers/worker_code_dryrun-v3-and-submit_20260519T213942.log
logs/workers/worker_code_add-grad-monitor_20260519T212023.log
logs/workers/worker_code_phase1-dryrun-v2_20260519T211248.log
logs/workers/worker_code_read-layer-scan-results_20260519T211524.log
logs/workers/worker_code_layer-scan_20260519T210734.log
logs/workers/worker_code_fix-finetune-bugs-v3_20260519T210640.log
logs/workers/worker_code_lconsist-training_20260519T202726.log
logs/workers/worker_code_fix-decoder-bugs_20260519T204639.log
logs/workers/worker_code_affordance-decoder_20260519T202650.log
logs/workers/worker_code_heatmap-eval-metrics_20260519T202807.log
logs/workers/worker_code_real-image-divergence_20260519T201328.log
logs/workers/worker_code_hidden-state-divergence_20260519T201201.log
logs/workers/worker_code_run-phase0_20260519T200204.log
logs/workers/worker_code_phase0-run_20260519T194852.log
logs/workers/worker_code_fix-phase0-embedding-v2_20260519T194639.log
logs/workers/worker_code_paraphrase-gen_20260519T190517.log
logs/workers/worker_infra_fix-transformers-fork_20260519T192624.log
logs/workers/worker_infra_verify-8b-and-fork_20260519T192426.log
logs/workers/worker_infra_download-check-and-fix_20260519T184720.log
logs/workers/worker_code_fix-run-phase0-import_20260519T184808.log
logs/workers/worker_code_fix-embedding-v2_20260519T180135.log
logs/workers/worker_code_fix-phase0-embedding-v2_20260519T180010.log
logs/workers/worker_infra_qwen3-verify_20260519T180549.log
logs/workers/worker_infra_qwen3-download-v3_20260519T180106.log
logs/workers/worker_infra_download-qwen3-retry_20260519T174031.log
logs/workers/worker_code_fix-phase0-embedding_20260519T172335.log
logs/workers/worker_infra_download-qwen3_20260519T171131.log
logs/workers/worker_infra_kill-hdf5-download_20260519T173428.log
logs/workers/worker_infra_download-libero_20260519T171147.log
logs/workers/worker_code_phase0-eval_20260519T170924.log
logs/workers/worker_research_libero-para-check_20260519T170856_result.json
logs/workers/worker_research_libero-para-check_20260519T170856.log
logs/workers/worker_infra_disk-and-download_20260519T164506.log
logs/workers/worker_infra_env-fix-critical_20260519T163640.log
logs/workers/worker_infra_env-setup_20260519T161651.log
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "24fb5689-e202-4007-b72b-8ada43a5a09b",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_research_pride-formula-verify_20260519T232737.log",
      "logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl",
      "logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl",
      ".claude/sessions/director_21ca1cc3/AGENTS.md",
      ".claude/sessions/director_21ca1cc3/CLAUDE.md",
      "AGENTS.md",
      ".claude/CLAUDE.md",
      "logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl",
      "report.md",
      "checkpoints/phase1_lconsist_v1_cont_RUNNING_20260519T232658.json",
      "registry.yaml",
      "checkpoints/phase1_lconsist_v1_cont_ALLOCATED_20260519T232652.json",
      "checkpoints/phase1_lconsist_v1_cont_QUEUED_20260519T232647.json",
      "checkpoints/phase1_lconsist_v1_cont_PENDING_20260519T232644.json",
      "checkpoints/phase1_lconsist_v1_DONE_20260519T232445.json",
      ".claude/sessions/reviewer_8c7bb198/AGENTS.md",
      ".claude/sessions/reviewer_8c7bb198/CLAUDE.md",
      "logs/workers/worker_infra_restart-lconsist-training_20260519T231922.log",
      "logs/workers/worker_code_merge-consist-transfer_20260519T232011.log",
      ".claude/sessions/agent_413a00de/AGENTS.md",
      ".claude/sessions/agent_413a00de/CLAUDE.md",
      "ROADMAP.md",
      "decisions.yaml",
      "logs/workers/worker_code_l-transfer-dryrun_20260519T225748.log",
      "checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225818.json",
      "memory.md",
      "logs/workers/worker_analysis_phase1_lconsist_v1_20260519T225345.log",
      "logs/chats/cron_hook_phase1_lconsist_v1.jsonl",
      ".claude/sessions/agent_56997cc0/AGENTS.md",
      ".claude/sessions/agent_56997cc0/CLAUDE.md",
      "checkpoints/phase1_lconsist_v1_ANALYZING_20260519T225208.json",
      "logs/workers/worker_code_eval-fixes_20260519T224913_result.json",
      "logs/workers/worker_code_eval-fixes_20260519T224913.log",
      "logs/workers/worker_code_training-status-fix_20260519T224853.log",
      "logs/workers/worker_code_fix-and-relaunch_20260519T222907.log",
      "logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json",
      "logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log",
      "logs/workers/worker_code_l-transfer-pair-validation_20260519T222514.log",
      "logs/workers/worker_code_paraphrase-hit-rate_20260519T222554.log",
      "checkpoints/phase1_lconsist_v1_RUNNING_20260519T222330.json",
      "checkpoints/phase1_lconsist_v1_ALLOCATED_20260519T222324.json",
      "checkpoints/phase1_lconsist_v1_QUEUED_20260519T222321.json",
      "checkpoints/phase1_lconsist_v1_PENDING_20260519T222309.json",
      "logs/workers/worker_code_l-transfer-impl_20260519T220356.log",
      "logs/workers/worker_code_dryrun-v3-and-submit_20260519T213942.log",
      "logs/workers/worker_code_add-grad-monitor_20260519T212023.log",
      "logs/workers/worker_code_phase1-dryrun-v2_20260519T211248.log",
      "logs/workers/worker_code_read-layer-scan-results_20260519T211524.log",
      "logs/workers/worker_code_layer-scan_20260519T210734.log",
      "logs/workers/worker_code_fix-finetune-bugs-v3_20260519T210640.log",
      "logs/workers/worker_code_lconsist-training_20260519T202726.log",
      "logs/workers/worker_code_fix-decoder-bugs_20260519T204639.log",
      "logs/workers/worker_code_affordance-decoder_20260519T202650.log",
      "logs/workers/worker_code_heatmap-eval-metrics_20260519T202807.log",
      "logs/workers/worker_code_real-image-divergence_20260519T201328.log",
      "logs/workers/worker_code_hidden-state-divergence_20260519T201201.log",
      "logs/workers/worker_code_run-phase0_20260519T200204.log",
      "logs/workers/worker_code_phase0-run_20260519T194852.log",
      "logs/workers/worker_code_fix-phase0-embedding-v2_20260519T194639.log",
      "logs/workers/worker_code_paraphrase-gen_20260519T190517.log",
      "logs/workers/worker_infra_fix-transformers-fork_20260519T192624.log",
      "logs/workers/worker_infra_verify-8b-and-fork_20260519T192426.log",
      "logs/workers/worker_infra_download-check-and-fix_20260519T184720.log",
      "logs/workers/worker_code_fix-run-phase0-import_20260519T184808.log",
      "logs/workers/worker_code_fix-embedding-v2_20260519T180135.log",
      "logs/workers/worker_code_fix-phase0-embedding-v2_20260519T180010.log",
      "logs/workers/worker_infra_qwen3-verify_20260519T180549.log",
      "logs/workers/worker_infra_qwen3-download-v3_20260519T180106.log",
      "logs/workers/worker_infra_download-qwen3-retry_20260519T174031.log",
      "logs/workers/worker_code_fix-phase0-embedding_20260519T172335.log",
      "logs/workers/worker_infra_download-qwen3_20260519T171131.log",
      "logs/workers/worker_infra_kill-hdf5-download_20260519T173428.log",
      "logs/workers/worker_infra_download-libero_20260519T171147.log",
      "logs/workers/worker_code_phase0-eval_20260519T170924.log",
      "logs/workers/worker_research_libero-para-check_20260519T170856_result.json",
      "logs/workers/worker_research_libero-para-check_20260519T170856.log",
      "logs/workers/worker_infra_disk-and-download_20260519T164506.log",
      "logs/workers/worker_infra_env-fix-critical_20260519T163640.log",
      "logs/workers/worker_infra_env-setup_20260519T161651.log",
      "docs/IDEA_BRIEF.md"
    ],
    "numFiles": 80
  }
}
```

</details>

---

### Tool call

_source line 48_

<details open><summary>🔧 Tool call — Grep · `toolu_01YDk9YCT1vynEHVufQ2JPsG`</summary>

```json
{
  "pattern": "PRIDE|pride|paraphrase_distance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "glob": "*.{py,md,yaml}",
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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "223bbfd9-37f3-4b74-be58-073e0ff5fa84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rwZvnWoYcfvwaCcnTD2pJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2103,
      "cache_read_input_tokens": 56775,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2103
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

_source line 49 · 2026-05-19T23:30:14.567Z_

<details><summary>↩ Tool result · `toolu_01YDk9YCT1vynEHVufQ2JPsG`</summary>

```text
decisions.yaml:6:    → LIBERO-Para PRIDE 评估
decisions.yaml:16:    bias。W2: PRIDE 阈值从 "any improvement" 提升到 ≥5pp（单 seed），统计上更可靠。W3: 增加 Phase 0.5
decisions.yaml:18:    无选择性 / PRIDE < +2pp → kill）。MVP 预算从 25h 调至 30-35h。'
decisions.yaml:24:  summary: Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数（Goal 58.8, Mixed 56.3），无需自行跑
decisions.yaml:26:  rationale: LIBERO-Para 论文公开了 OFT 在 Goal suite 的 PRIDE=58.8。我们 MVP pass 目标 ≥63.8（+5pp）。节省
report.md:8:| phase1_lconsist_v1_cont | 从 phase1_lconsist_v1 checkpoint-1000 继续 L_action 训练至 20000 步，获取 OFT baseline SR 数据用于对比。Affordance decoder 已确认 NEGATIVE（不期望 heatmap 改善），但 L_action LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。 | — | — | — |
report.md:15:- **phase1_lconsist_v1** (negative): L_consist (alpha=0.1, lambda_H=0) 作为 LoRA fine-tuning 正则项，引导 affordance decoder 从 Layer-18 features 学到空间 affordance 表征。预期：heatmap peak 到 gripper target 归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8
ROADMAP.md:37:3. LIBERO-Para PRIDE ≥ 63.8
ROADMAP.md:42:- PRIDE < 60.8 → kill
ROADMAP.md:46:- [ ] PRIDE 公式：eval_pride.py 与 ROADMAP 阈值矛盾，需查 LIBERO-Para 论文确认定义
ROADMAP.md:47:- [ ] robosuite/mujoco 安装（LIBERO SR 和 PRIDE 评估依赖）
ROADMAP.md:55:- [ ] Phase 1b: 训练完成后 heatmap eval + LIBERO SR + PRIDE
ROADMAP.md:56:- [ ] PRIDE 公式校正
ROADMAP.md:76:| D003 | 2026-05-19 | Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数 | — |
registry.yaml:10:      归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8
registry.yaml:87:      LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。
registry.yaml:106:      eval_data: LIBERO SR + PRIDE evaluation after training completes
memory.md:70:6. **Heatmap 评估** (`scripts/evaluation/`): extract_ground_truth.py + heatmap_metrics.py + run_heatmap_eval.py + eval_pride.py
memory.md:89:- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5
memory.md:90:- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)
docs/IDEA_BRIEF.md:123:[Omitted long matching line]
docs/IDEA_BRIEF.md:143:- LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — 22–52pp drops under paraphrasing, PRIDE metric (arXiv 2603.28301, March 2026)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "7782f079-e665-408d-88ad-c4ff5fce5a7f",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "decisions.yaml:6:    → LIBERO-Para PRIDE 评估\ndecisions.yaml:16:    bias。W2: PRIDE 阈值从 \"any improvement\" 提升到 ≥5pp（单 seed），统计上更可靠。W3: 增加 Phase 0.5\ndecisions.yaml:18:    无选择性 / PRIDE < +2pp → kill）。MVP 预算从 25h 调至 30-35h。'\ndecisions.yaml:24:  summary: Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数（Goal 58.8, Mixed 56.3），无需自行跑\ndecisions.yaml:26:  rationale: LIBERO-Para 论文公开了 OFT 在 Goal suite 的 PRIDE=58.8。我们 MVP pass 目标 ≥63.8（+5pp）。节省\nreport.md:8:| phase1_lconsist_v1_cont | 从 phase1_lconsist_v1 checkpoint-1000 继续 L_action 训练至 20000 步，获取 OFT baseline SR 数据用于对比。Affordance decoder 已确认 NEGATIVE（不期望 heatmap 改善），但 L_action LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。 | — | — | — |\nreport.md:15:- **phase1_lconsist_v1** (negative): L_consist (alpha=0.1, lambda_H=0) 作为 LoRA fine-tuning 正则项，引导 affordance decoder 从 Layer-18 features 学到空间 affordance 表征。预期：heatmap peak 到 gripper target 归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8\nROADMAP.md:37:3. LIBERO-Para PRIDE ≥ 63.8\nROADMAP.md:42:- PRIDE < 60.8 → kill\nROADMAP.md:46:- [ ] PRIDE 公式：eval_pride.py 与 ROADMAP 阈值矛盾，需查 LIBERO-Para 论文确认定义\nROADMAP.md:47:- [ ] robosuite/mujoco 安装（LIBERO SR 和 PRIDE 评估依赖）\nROADMAP.md:55:- [ ] Phase 1b: 训练完成后 heatmap eval + LIBERO SR + PRIDE\nROADMAP.md:56:- [ ] PRIDE 公式校正\nROADMAP.md:76:| D003 | 2026-05-19 | Phase 0.5 跳过：LIBERO-Para 已公布 OFT baseline PRIDE 分数 | — |\nregistry.yaml:10:      归一化距离 < 0.2，standard LIBERO SR ≥ 95%，LIBERO-Para PRIDE ≥ 63.8\nregistry.yaml:87:      LoRA 正常收敛，需要完整训练的 checkpoint 做 LIBERO SR/PRIDE 评估基线。\nregistry.yaml:106:      eval_data: LIBERO SR + PRIDE evaluation after training completes\nmemory.md:70:6. **Heatmap 评估** (`scripts/evaluation/`): extract_ground_truth.py + heatmap_metrics.py + run_heatmap_eval.py + eval_pride.py\nmemory.md:89:- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5\nmemory.md:90:- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)\ndocs/IDEA_BRIEF.md:123:[Omitted long matching line]\ndocs/IDEA_BRIEF.md:143:- LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models — 22–52pp drops under paraphrasing, PRIDE metric (arXiv 2603.28301, March 2026)",
    "numLines": 22
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Grep · `toolu_01NnUTLCTGSvbmyTkxMtDEM8`</summary>

```json
{
  "pattern": "pride|PRIDE|paraphrase_distance",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "glob": "*.py",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "869e6d9d-32c3-4b79-a40c-6d1e6489f607",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KSzjcWJDAtrBcHnUW5CsXL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1291,
      "cache_read_input_tokens": 58878,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1291
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

### Tool result

_source line 51 · 2026-05-19T23:30:19.627Z_

<details><summary>↩ Tool result · `toolu_01NnUTLCTGSvbmyTkxMtDEM8`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "1fa7b99d-47f0-419d-93d1-8bc7baba4642",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [],
    "numFiles": 0
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Grep · `toolu_01TXTYbCHPdgFQ1RtmQUoupH`</summary>

```json
{
  "pattern": "eval_pride",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar",
  "output_mode": "files_with_matches"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "3814a5ce-967c-4c83-98bf-56af9f2235ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014DmkE6rQ1xfRoPXjYJ7beP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 157,
      "cache_read_input_tokens": 60169,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 157
      },
      "output_tokens": 65,
      "service_tier": "standard",
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

_source line 53 · 2026-05-19T23:30:22.969Z_

<details><summary>↩ Tool result · `toolu_01TXTYbCHPdgFQ1RtmQUoupH`</summary>

```text
Found 11 files
logs/workers/worker_research_pride-formula-verify_20260519T232737.log
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl
logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl
logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl
logs/workers/worker_code_merge-consist-transfer_20260519T232011.log
ROADMAP.md
memory.md
logs/workers/worker_code_eval-fixes_20260519T224913_result.json
logs/workers/worker_code_eval-fixes_20260519T224913.log
logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json
logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "8fc1bea5-8181-4481-8d7e-175d2a111f0b",
  "tool_use_result": {
    "mode": "files_with_matches",
    "filenames": [
      "logs/workers/worker_research_pride-formula-verify_20260519T232737.log",
      "logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c_reviewer.jsonl",
      "logs/chats/feishu_group_oc_bfa3708ecf42097843150f45348b3760_director.jsonl",
      "logs/chats/feishu_group_oc_e0fe8d2f0d417545f5bf6f650173c34c.jsonl",
      "logs/workers/worker_code_merge-consist-transfer_20260519T232011.log",
      "ROADMAP.md",
      "memory.md",
      "logs/workers/worker_code_eval-fixes_20260519T224913_result.json",
      "logs/workers/worker_code_eval-fixes_20260519T224913.log",
      "logs/workers/worker_code_eval-pipeline-prep_20260519T222535_result.json",
      "logs/workers/worker_code_eval-pipeline-prep_20260519T222535.log"
    ],
    "numFiles": 11
  }
}
```

</details>

---

### Assistant

_source line 54_

Now let me check what's in memory.md for the PRIDE definition and if there's an eval_pride.py on the server.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "c6f3fb15-5408-4273-b1c3-9085f03aa5af",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5BhTHkzoHJmPE8qUWgYcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 60326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 398
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

_source line 55_

<details open><summary>🔧 Tool call — Read · `toolu_016Zss75QqDHeZZwDjjjogur`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/memory.md",
  "offset": 85,
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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "d7f92564-4078-43fb-afb6-5cd766d6621e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U5BhTHkzoHJmPE8qUWgYcu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 398,
      "cache_read_input_tokens": 60326,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 398
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

_source line 56 · 2026-05-19T23:30:27.566Z_

<details><summary>↩ Tool result · `toolu_016Zss75QqDHeZZwDjjjogur`</summary>

```text
85	- Total trainable: ~263M (LoRA 111M + action_head 151M + decoder 1.7M)
86	
87	## LIBERO-Para 调研结论 (2026-05-19)
88	
89	- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5
90	- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)
91	- 原始 LIBERO-Goal SR: OFT_goal 97.9%, OFT_mixed 96.1% → paraphrase 退化 ~33pp
92	- 80-96% 失败来自 planning-level trajectory divergence
93	
94	## 环境信息 (2026-05-19)
95	
96	- 服务器: westd-19957, 4x RTX PRO 6000 Blackwell (94GB each)
97	- conda base: Python 3.12.3, PyTorch 2.8.0+cu128
98	- transformers: OFT fork 4.40.1 (moojink/transformers-openvla-oft)
99	- timm: 0.9.16
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "c07cafc7-60d7-4d56-9a87-146be1687645",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0513/projects/afford_invar/memory.md",
      "content": "- Total trainable: ~263M (LoRA 111M + action_head 151M + decoder 1.7M)\n\n## LIBERO-Para 调研结论 (2026-05-19)\n\n- PRIDE 公式: PD = 1 - (α·SK + (1-α)·ST), α=0.5\n- OFT baseline PRIDE: OFT_goal=58.8 (SR 64.7%), OFT_mixed=56.3 (SR 63.7%)\n- 原始 LIBERO-Goal SR: OFT_goal 97.9%, OFT_mixed 96.1% → paraphrase 退化 ~33pp\n- 80-96% 失败来自 planning-level trajectory divergence\n\n## 环境信息 (2026-05-19)\n\n- 服务器: westd-19957, 4x RTX PRO 6000 Blackwell (94GB each)\n- conda base: Python 3.12.3, PyTorch 2.8.0+cu128\n- transformers: OFT fork 4.40.1 (moojink/transformers-openvla-oft)\n- timm: 0.9.16",
      "numLines": 15,
      "startLine": 85,
      "totalLines": 109
    }
  }
}
```

</details>

---

### Assistant

_source line 57_

现在我有了全部信息。让我清理克隆的 repo。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "16ca3a03-6625-4cd2-80ed-fd409aac2c2b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GttH4iMdiaCRstueGubcU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 60724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 58_

<details open><summary>🔧 Tool call — Bash · `toolu_01HdWxdMRzqkQ6gDXvcvASJp`</summary>

```json
{
  "command": "rm -rf /tmp/LIBERO-Para",
  "description": "Clean up cloned repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "89b29a0e-a817-4017-88b7-d76b0a495aa7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GttH4iMdiaCRstueGubcU9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 494,
      "cache_read_input_tokens": 60724,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 494
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

_source line 59 · 2026-05-19T23:30:33.350Z_

<details><summary>↩ Tool result · `toolu_01HdWxdMRzqkQ6gDXvcvASJp`</summary>

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
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "295dd5fc-0c38-4715-8f6a-bdf58fd364b8",
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

### Assistant

_source line 60_

## PRIDE 指标验证报告

### 论文原始定义 (arXiv:2603.28301)

**PD (Paraphrase Distance):**
```
PD = 1 - (α·S_K + (1-α)·S_T),  α=0.5
```

- **S_K** (Keyword Similarity): 对原始指令的 content words (NOUN/VERB/ADJ/ADV) 用 Sentence-BERT (all-MiniLM-L6-v2) 编码，每个原始词与所有 paraphrase 词取 max cosine similarity，再取平均：`S_K = (1/n) Σ max_j cos(e(o_i), e(p_j))`
- **S_T** (Structural Similarity): 依赖解析树的 Zhang-Shasha tree edit distance (TED)，节点标签为 (dep, POS)：`S_T = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)`

**PRIDE 聚合公式（关键）:**
```
PRIDE(α) = Σ(success_i × PD_i) / Σ(PD_i) × 100
```

即 **PD 加权成功率**——成功 episode 的 PD 之和除以所有 episode 的 PD 之和，乘 100。Higher = better。

### 与我们当前实现的对比

| 要素 | 论文定义 | 我们 memory.md 记录 | 一致？ |
|------|---------|-------------------|--------|
| PD 公式 | `1 - (α·SK + (1-α)·ST)` | `1 - (α·SK + (1-α)·ST)` | **一致** |
| α 默认值 | 0.5 | 0.5 | **一致** |
| PRIDE 聚合 | `Σ(success×PD) / Σ(PD) × 100` | memory.md 未记录聚合公式 | **需确认** |
| 方向 | Higher = more robust | 未明确 | **需确认** |
| OFT_goal PRIDE | 58.8 | 58.8 | **一致** |
| OFT_mixed PRIDE | 56.3 | 56.3 | **一致** |

### 关键发现

1. **PD 单 episode 公式正确**——与论文 Eq.3 完全一致。

2. **PRIDE 不是简单的 per-episode PD 值**。论文 HTML (Eq.4) 简写为 "PRIDE = PD if success, 0 if failure"，但代码实现的聚合是 **加权比率**：`Σ(success_i × PD_i) / Σ(PD_i) × 100`。这不是简单平均，而是 PD 加权的成功率。更难的 paraphrase（PD 大）在分母中权重更大，成功则在分子中贡献更多。

3. **我们的 eval_pride.py 尚未实现**（项目中无 .py 文件包含 PRIDE 计算）。ROADMAP.md 已标注此为待办项。

4. **实现时需注意**：论文官方代码使用 `paraphrased_instruction` 字段匹配 pre-computed SK/ST CSV，而非实时计算。可直接复用论文的 `libero_para_metadata.csv`。

### 结论

PD 公式和 baseline 数值与论文完全一致，无需修改。实现 eval_pride.py 时需用 **加权比率公式** `Σ(success×PD)/Σ(PD)×100`，不能简单取均值。

Sources:
- [LIBERO-Para Paper (HTML)](https://arxiv.org/html/2603.28301v1)
- [LIBERO-Para Paper (Abstract)](https://arxiv.org/abs/2603.28301)
- [LIBERO-Para GitHub](https://github.com/cau-hai-lab/LIBERO-Para)
- [LIBERO-Para Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "uuid": "56ab08a1-5a2f-4484-b6e9-eefa42046253",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P8Yktb5rcxKZhdqpeFYQrP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 123,
      "cache_read_input_tokens": 61218,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 123
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

_source line 61_

## PRIDE 指标验证报告

### 论文原始定义 (arXiv:2603.28301)

**PD (Paraphrase Distance):**
```
PD = 1 - (α·S_K + (1-α)·S_T),  α=0.5
```

- **S_K** (Keyword Similarity): 对原始指令的 content words (NOUN/VERB/ADJ/ADV) 用 Sentence-BERT (all-MiniLM-L6-v2) 编码，每个原始词与所有 paraphrase 词取 max cosine similarity，再取平均：`S_K = (1/n) Σ max_j cos(e(o_i), e(p_j))`
- **S_T** (Structural Similarity): 依赖解析树的 Zhang-Shasha tree edit distance (TED)，节点标签为 (dep, POS)：`S_T = 1 - TED(T_O, T_P) / (|T_O| + |T_P|)`

**PRIDE 聚合公式（关键）:**
```
PRIDE(α) = Σ(success_i × PD_i) / Σ(PD_i) × 100
```

即 **PD 加权成功率**——成功 episode 的 PD 之和除以所有 episode 的 PD 之和，乘 100。Higher = better。

### 与我们当前实现的对比

| 要素 | 论文定义 | 我们 memory.md 记录 | 一致？ |
|------|---------|-------------------|--------|
| PD 公式 | `1 - (α·SK + (1-α)·ST)` | `1 - (α·SK + (1-α)·ST)` | **一致** |
| α 默认值 | 0.5 | 0.5 | **一致** |
| PRIDE 聚合 | `Σ(success×PD) / Σ(PD) × 100` | memory.md 未记录聚合公式 | **需确认** |
| 方向 | Higher = more robust | 未明确 | **需确认** |
| OFT_goal PRIDE | 58.8 | 58.8 | **一致** |
| OFT_mixed PRIDE | 56.3 | 56.3 | **一致** |

### 关键发现

1. **PD 单 episode 公式正确**——与论文 Eq.3 完全一致。

2. **PRIDE 不是简单的 per-episode PD 值**。论文 HTML (Eq.4) 简写为 "PRIDE = PD if success, 0 if failure"，但代码实现的聚合是 **加权比率**：`Σ(success_i × PD_i) / Σ(PD_i) × 100`。这不是简单平均，而是 PD 加权的成功率。更难的 paraphrase（PD 大）在分母中权重更大，成功则在分子中贡献更多。

3. **我们的 eval_pride.py 尚未实现**（项目中无 .py 文件包含 PRIDE 计算）。ROADMAP.md 已标注此为待办项。

4. **实现时需注意**：论文官方代码使用 `paraphrased_instruction` 字段匹配 pre-computed SK/ST CSV，而非实时计算。可直接复用论文的 `libero_para_metadata.csv`。

### 结论

PD 公式和 baseline 数值与论文完全一致，无需修改。实现 eval_pride.py 时需用 **加权比率公式** `Σ(success×PD)/Σ(PD)×100`，不能简单取均值。

Sources:
- [LIBERO-Para Paper (HTML)](https://arxiv.org/html/2603.28301v1)
- [LIBERO-Para Paper (Abstract)](https://arxiv.org/abs/2603.28301)
- [LIBERO-Para GitHub](https://github.com/cau-hai-lab/LIBERO-Para)
- [LIBERO-Para Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 196488,
  "duration_api_ms": 200355,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "1d0fe09d-e576-45f8-8424-6f37bab2600e",
  "total_cost_usd": 0.866719,
  "usage": {
    "input_tokens": 1035,
    "cache_creation_input_tokens": 49500,
    "cache_read_input_tokens": 642866,
    "output_tokens": 3897,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 49500,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1167,
        "cache_read_input_tokens": 61218,
        "cache_creation_input_tokens": 123,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 123
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 80126,
      "outputTokens": 2637,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 4,
      "costUSD": 0.13331099999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 1035,
      "outputTokens": 3897,
      "cacheReadInputTokens": 642866,
      "cacheCreationInputTokens": 49500,
      "webSearchRequests": 0,
      "costUSD": 0.7334080000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "8cac87e1-dd22-477a-9605-13f572a24c9a"
}
```

</details>

---
