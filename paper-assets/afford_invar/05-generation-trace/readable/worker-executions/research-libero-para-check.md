# research libero para check

**afford invar** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 31
- **Recorded user turns:** 0
- **Tool calls:** 9
- **Original source:** `logs/workers/worker_research_libero-para-check_20260519T170856.log`
- **Structured JSON:** [`def8a5baf95dd534e36f.json`](../../sessions/de/def8a5baf95dd534e36f.json)

## Before a recorded user message

31 recorded events

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
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
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
  "uuid": "0cf19f32-37ef-49da-a26f-667a24316449",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-projects-afford-invar/memory/"
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
    "resetsAt": 1779223800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5efbf880-1b3f-47e8-8bfc-1032572f7077",
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a"
}
```

---

### Assistant

_source line 4_

我来并行搜索 LIBERO-Para 的相关信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "40b95179-8fcd-4b09-9674-9d6779e6c9f2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7bcdWmoYMDhfVMNuhNCcR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11505,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11505
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HctAsWpwcSVEHKvp9rH4RJ`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
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
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "f964f0d8-7013-4915-80cb-c887638c6e06",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7bcdWmoYMDhfVMNuhNCcR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11505,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11505
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

_source line 6 · 2026-05-19T17:09:08.166Z_

<details><summary>↩ Tool result · `toolu_01HctAsWpwcSVEHKvp9rH4RJ`</summary>

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
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "db53775e-2c66-418a-bdf8-48cc2cb6ede8",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
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
Let me search for LIBERO-Para information in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "3251e3fa-c7fe-4e3b-857a-6eceae1ef531",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

### Assistant

_source line 8_

并行搜索 LIBERO-Para 相关信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "23eb1746-b82a-4eac-9f37-8049e581a830",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0198gjCY5Z243jVc7H1x6UmV`</summary>

```json
{
  "query": "LIBERO-Para arXiv 2603.28301 code GitHub"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "5e47ff8e-f535-4f18-9f8f-b5c2c37ccd9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ryS32KJyzLsMzK3KSCr7o`</summary>

```json
{
  "query": "LIBERO-Para paraphrase robustness benchmark GitHub repository"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "fdd389fd-9045-40fc-a65f-26fe1022b19c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKsaRi6r5mUVDn6HNx9Xbc`</summary>

```json
{
  "query": "PRIDE metric paraphrase robustness LIBERO decision-making"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "95b82e08-779c-4bb2-930b-1c3cd5edd5b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

_source line 12_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016F1joTstdqu8j8wVd6xCWa`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.28301",
  "prompt": "Extract all information about: 1) Code/data release links, 2) PRIDE metric definition and formula, 3) OpenVLA-OFT baseline scores on LIBERO-Para, 4) Other baseline PRIDE scores, 5) How paraphrases were generated (LLM used, number per task), 6) Any GitHub repository links mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "a580c4b7-3656-4c29-80ff-65d92028b4ff",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWb7fhhW63FRXSvjLXdLN1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1121,
      "cache_read_input_tokens": 23346,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1121
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

_source line 13 · 2026-05-19T17:09:19.075Z_

<details><summary>↩ Tool result · `toolu_016F1joTstdqu8j8wVd6xCWa`</summary>

```text
# LIBERO-Para Paper Information Extract

## 1) Code/Data Release Links
The paper mentions code availability: "Our benchmark and corresponding code are available at: [this https URL](https://github.com/cau-hai-lab/LIBERO-Para)"

GitHub repository: **https://github.com/cau-hai-lab/LIBERO-Para**

## 2) PRIDE Metric Definition and Formula
The abstract describes the metric purpose but does not provide its mathematical formula in the available content. It states that PRIDE "quantifies paraphrase difficulty using semantic and syntactic factors" and addresses limitations where "binary success rate treats all paraphrases equally."

## 3) OpenVLA-OFT Baseline Scores
No specific baseline scores for OpenVLA-OFT or other models on LIBERO-Para are provided in this excerpt.

## 4) Other Baseline PRIDE Scores
No baseline PRIDE scores are included in the provided content.

## 5) Paraphrase Generation Method
The page does not specify which language model was used to generate paraphrases or how many variations were created per task.

## 6) GitHub Repository Links
Only one GitHub link is mentioned:
- **https://github.com/cau-hai-lab/LIBERO-Para**

**Note:** The full paper PDF would contain additional technical details, experimental results, and methodology specifications not visible in this abstract page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "5a30f601-322b-4bc9-a307-1603c64595f8",
  "tool_use_result": {
    "bytes": 47841,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Para Paper Information Extract\n\n## 1) Code/Data Release Links\nThe paper mentions code availability: \"Our benchmark and corresponding code are available at: [this https URL](https://github.com/cau-hai-lab/LIBERO-Para)\"\n\nGitHub repository: **https://github.com/cau-hai-lab/LIBERO-Para**\n\n## 2) PRIDE Metric Definition and Formula\nThe abstract describes the metric purpose but does not provide its mathematical formula in the available content. It states that PRIDE \"quantifies paraphrase difficulty using semantic and syntactic factors\" and addresses limitations where \"binary success rate treats all paraphrases equally.\"\n\n## 3) OpenVLA-OFT Baseline Scores\nNo specific baseline scores for OpenVLA-OFT or other models on LIBERO-Para are provided in this excerpt.\n\n## 4) Other Baseline PRIDE Scores\nNo baseline PRIDE scores are included in the provided content.\n\n## 5) Paraphrase Generation Method\nThe page does not specify which language model was used to generate paraphrases or how many variations were created per task.\n\n## 6) GitHub Repository Links\nOnly one GitHub link is mentioned:\n- **https://github.com/cau-hai-lab/LIBERO-Para**\n\n**Note:** The full paper PDF would contain additional technical details, experimental results, and methodology specifications not visible in this abstract page.",
    "durationMs": 4616,
    "url": "https://arxiv.org/abs/2603.28301"
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-19T17:09:19.345Z_

<details><summary>↩ Tool result · `toolu_012ryS32KJyzLsMzK3KSCr7o`</summary>

```text
Web search results for query: "LIBERO-Para paraphrase robustness benchmark GitHub repository"

Links: [{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"paraphrase · GitHub Topics · GitHub","url":"https://github.com/topics/paraphrase"},{"title":"cau-hai-lab · GitHub","url":"https://github.com/cau-hai-lab"},{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"LIBERO-Para: Measuring VLA Paraphrase Robustness - YouTube","url":"https://www.youtube.com/watch?v=Yg-GVm-kdk4"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"}]

Based on the search results, I found the LIBERO-Para paraphrase robustness benchmark GitHub repository.

## LIBERO-Para GitHub Repository

The official repository is located at https://github.com/cau-hai-lab/LIBERO-Para and extends LIBERO with 4,000+ paraphrased instructions across 10 evaluation scenarios, all in a single repository.

## About LIBERO-Para

LIBERO-Para is a controlled benchmark that evaluates paraphrase robustness in VLA (Vision-Language-Action) models by independently varying action expressions and object references. The benchmark systematically pairs original task instructions with semantically equivalent paraphrases and measures the performance gap, isolating paraphrase sensitivity by holding the task, scene, and desired outcome constant while varying only the instruction wording.

## Key Features

- LIBERO-Para decomposes paraphrases along two essential axes: object-referring expressions and action-referring expressions, with each axis independently varied to yield compositional paraphrases.
- The repository includes 6 VLA models integrated with per-model conda environments, standalone eval scripts, and step-by-step guides.
- PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "20905b38-cc8f-4316-9a5d-6156402f3a3c",
  "tool_use_result": {
    "query": "LIBERO-Para paraphrase robustness benchmark GitHub repository",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LEfJE5jm8ibpVS7tvFyScF",
        "content": [
          {
            "title": "Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://huggingface.co/papers/2603.28301"
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
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://cau-hai-lab.github.io/LIBERO-Para/"
          },
          {
            "title": "paraphrase · GitHub Topics · GitHub",
            "url": "https://github.com/topics/paraphrase"
          },
          {
            "title": "cau-hai-lab · GitHub",
            "url": "https://github.com/cau-hai-lab"
          },
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          },
          {
            "title": "LIBERO-Para: Measuring VLA Paraphrase Robustness - YouTube",
            "url": "https://www.youtube.com/watch?v=Yg-GVm-kdk4"
          },
          {
            "title": "GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark",
            "url": "https://github.com/Zxy-MLlab/LIBERO-PRO"
          }
        ]
      },
      "Based on the search results, I found the LIBERO-Para paraphrase robustness benchmark GitHub repository.\n\n## LIBERO-Para GitHub Repository\n\nThe official repository is located at https://github.com/cau-hai-lab/LIBERO-Para and extends LIBERO with 4,000+ paraphrased instructions across 10 evaluation scenarios, all in a single repository.\n\n## About LIBERO-Para\n\nLIBERO-Para is a controlled benchmark that evaluates paraphrase robustness in VLA (Vision-Language-Action) models by independently varying action expressions and object references. The benchmark systematically pairs original task instructions with semantically equivalent paraphrases and measures the performance gap, isolating paraphrase sensitivity by holding the task, scene, and desired outcome constant while varying only the instruction wording.\n\n## Key Features\n\n- LIBERO-Para decomposes paraphrases along two essential axes: object-referring expressions and action-referring expressions, with each axis independently varied to yield compositional paraphrases.\n- The repository includes 6 VLA models integrated with per-model conda environments, standalone eval scripts, and step-by-step guides.\n- PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions."
    ],
    "durationSeconds": 6.998495504
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-19T17:09:19.879Z_

<details><summary>↩ Tool result · `toolu_0198gjCY5Z243jVc7H1x6UmV`</summary>

```text
Web search results for query: "LIBERO-Para arXiv 2603.28301 code GitHub"

Links: [{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"GitHub - BaiShuanghao/my_arXiv_daily · GitHub","url":"https://github.com/BaiShuanghao/my_arXiv_daily"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily","url":"https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"A large-scale analysis of bioinformatics code on GitHub","url":"https://www.biorxiv.org/content/10.1101/321919.full.pdf"}]

Based on the web search results, here's what I found about LIBERO-Para (arXiv 2603.28301):

## Paper Overview
LIBERO-Para is a diagnostic benchmark that evaluates paraphrase robustness in Vision-Language-Action (VLA) models by independently varying action expressions and object references for fine-grained analysis of linguistic generalization.

## Key Findings
The research shows that performance degradation is primarily driven by object-level lexical variation, with 80-96% of failures arising from planning-level trajectory divergence rather than execution errors.

## GitHub Repository
The official GitHub repository is available at: **https://github.com/cau-hai-lab/LIBERO-Para**

## Dataset and Resources
The dataset is available on Hugging Face at: https://huggingface.co/datasets/HAI-Lab/LIBERO-Para

The paper was authored by Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, and Dahuin Jung from Soongsil University and Chung-Ang University, and submitted on March 30, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "837a083b-edb9-49b5-8400-8281ae5750c2",
  "tool_use_result": {
    "query": "LIBERO-Para arXiv 2603.28301 code GitHub",
    "results": [
      {
        "tool_use_id": "srvtoolu_011LpRawkK9s9iBwE4j59gYt",
        "content": [
          {
            "title": "[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/abs/2603.28301"
          },
          {
            "title": "GitHub - BaiShuanghao/my_arXiv_daily · GitHub",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily"
          },
          {
            "title": "Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://huggingface.co/papers/2603.28301"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301"
          },
          {
            "title": "my_arXiv_daily/README.md at main · BaiShuanghao/my_arXiv_daily",
            "url": "https://github.com/BaiShuanghao/my_arXiv_daily/blob/main/README.md"
          },
          {
            "title": "GitHub - cau-hai-lab/LIBERO-Para · GitHub",
            "url": "https://github.com/cau-hai-lab/LIBERO-Para"
          },
          {
            "title": "GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark",
            "url": "https://github.com/Zxy-MLlab/LIBERO-PRO"
          },
          {
            "title": "A large-scale analysis of bioinformatics code on GitHub",
            "url": "https://www.biorxiv.org/content/10.1101/321919.full.pdf"
          }
        ]
      },
      "Based on the web search results, here's what I found about LIBERO-Para (arXiv 2603.28301):\n\n## Paper Overview\nLIBERO-Para is a diagnostic benchmark that evaluates paraphrase robustness in Vision-Language-Action (VLA) models by independently varying action expressions and object references for fine-grained analysis of linguistic generalization.\n\n## Key Findings\nThe research shows that performance degradation is primarily driven by object-level lexical variation, with 80-96% of failures arising from planning-level trajectory divergence rather than execution errors.\n\n## GitHub Repository\nThe official GitHub repository is available at: **https://github.com/cau-hai-lab/LIBERO-Para**\n\n## Dataset and Resources\nThe dataset is available on Hugging Face at: https://huggingface.co/datasets/HAI-Lab/LIBERO-Para\n\nThe paper was authored by Chanyoung Kim, Minwoo Kim, Minseok Kang, Hyunwoo Kim, and Dahuin Jung from Soongsil University and Chung-Ang University, and submitted on March 30, 2026."
    ],
    "durationSeconds": 8.026505966
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-19T17:09:20.617Z_

<details><summary>↩ Tool result · `toolu_01JKsaRi6r5mUVDn6HNx9Xbc`</summary>

```text
Web search results for query: "PRIDE metric paraphrase robustness LIBERO decision-making"

Links: [{"title":"[2603.28301] LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/abs/2603.28301"},{"title":"Paper page - LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://huggingface.co/papers/2603.28301"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://cau-hai-lab.github.io/LIBERO-Para/"},{"title":"GitHub - cau-hai-lab/LIBERO-Para · GitHub","url":"https://github.com/cau-hai-lab/LIBERO-Para"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301v1"}]

Based on the search results, here's what I found about PRIDE metric and its relationship to paraphrase robustness in LIBERO:

PRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors. More specifically, PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions.

PRIDE is a difficulty-aware metric that goes beyond binary success rate, giving more credit for succeeding on harder paraphrases.

This metric was introduced as part of LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. The benchmark addresses a gap in testing Vision-Language-Action (VLA) models: in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored.

The benchmark found significant issues: Across seven VLA configurations (0.6B-7.5B), consistent performance degradation of 22-52 pp is observed under paraphrasing.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "d97a5799-ab42-4946-b2dc-0aac3518ecc6",
  "tool_use_result": {
    "query": "PRIDE metric paraphrase robustness LIBERO decision-making",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XfCjc63T9hfhd1Mn99TiVq",
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
          }
        ]
      },
      "Based on the search results, here's what I found about PRIDE metric and its relationship to paraphrase robustness in LIBERO:\n\nPRIDE is a metric that quantifies paraphrase difficulty using semantic and syntactic factors. More specifically, PRIDE (Paraphrase Robustness Index in Robotic Instructional DEviation) evaluates how robustly a VLA model handles paraphrased instructions.\n\nPRIDE is a difficulty-aware metric that goes beyond binary success rate, giving more credit for succeeding on harder paraphrases.\n\nThis metric was introduced as part of LIBERO-Para, a controlled benchmark that independently varies action expressions and object references for fine-grained analysis of linguistic generalization. The benchmark addresses a gap in testing Vision-Language-Action (VLA) models: in downstream robotic settings, they are typically fine-tuned with limited data, leading to overfitting to specific instruction formulations and leaving robustness to paraphrased instructions underexplored.\n\nThe benchmark found significant issues: Across seven VLA configurations (0.6B-7.5B), consistent performance degradation of 22-52 pp is observed under paraphrasing."
    ],
    "durationSeconds": 7.763013751000003
  }
}
```

</details>

---

### Assistant

_source line 17_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the GitHub repo and some basic info. Now I need to dig deeper - fetch the GitHub README for detailed info about PRIDE formula, baseline scores, and data availability. Also fetch the HTML version of the paper for detailed results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "58ebd894-d498-4c5a-a985-add33231b85f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkaQb2H6VtinAGpymKtfSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 351,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 24467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

找到 GitHub repo。继续获取详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "bbdb790b-9c47-4286-ac63-4914a6ded693",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkaQb2H6VtinAGpymKtfSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 351,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 24467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RpqVs1kf2JTq2uxiAKDc4Z`</summary>

```json
{
  "url": "https://github.com/cau-hai-lab/LIBERO-Para",
  "prompt": "Extract all information about: 1) What data files are available (paraphrase JSON/CSV files), 2) PRIDE metric code location and formula, 3) How to download/use the paraphrase dataset, 4) What VLA models are supported as baselines, 5) Is OpenVLA-OFT included, 6) Installation and evaluation instructions, 7) Directory structure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "6f61f329-e6a3-4f53-a5f2-7946c0c5c7ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkaQb2H6VtinAGpymKtfSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 351,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 24467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FMo7vgB4uTntNj4epowFWt`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28301v1",
  "prompt": "Extract: 1) The exact PRIDE metric formula and definition, 2) All experimental results tables - especially success rates and PRIDE scores for each model on each LIBERO suite (LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, LIBERO-Long), 3) OpenVLA-OFT specific scores, 4) How paraphrases were generated (which LLM, how many per task, what prompt template), 5) The paraphrase taxonomy (action vs object variations), 6) Any other baseline model scores"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "50dbff74-88e5-48a2-9c8f-24d0e7865f74",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkaQb2H6VtinAGpymKtfSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 351,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 24467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QYUnwiGdotopRSCjihv8sV`</summary>

```json
{
  "url": "https://huggingface.co/datasets/HAI-Lab/LIBERO-Para",
  "prompt": "Extract: 1) Dataset format and structure, 2) Download instructions, 3) Number of paraphrases, 4) File formats available, 5) How the data is organized (per task, per suite, etc.)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "ace4569f-9270-4d38-8712-58d9e44d21e2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JkaQb2H6VtinAGpymKtfSd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 351,
      "cache_creation_input_tokens": 2517,
      "cache_read_input_tokens": 24467,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2517
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

_source line 22 · 2026-05-19T17:09:36.919Z_

<details><summary>↩ Tool result · `toolu_01RpqVs1kf2JTq2uxiAKDc4Z`</summary>

````text
# LIBERO-Para: Key Information Summary

## 1) Data Files Available
The repository includes "4,000+ paraphrased instructions across 10 evaluation scenarios." A metadata file exists at `metrics/libero_para_metadata.csv`. The dataset is available on HuggingFace at the HAI-Lab organization. Example results are provided in `logs_para/example_xiaomi-robotics-0/seed7/`.

## 2) PRIDE Metric Location & Formula
**Location**: `metrics/` directory with detailed documentation in `metrics/README.md` and an interactive notebook at `metrics/PRIDE_metric_playground.ipynb`

**Formula Overview**: PRIDE computes Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then "measures the ratio of PD-weighted successes to total possible PD, normalized to 0–100." It prioritizes success on harder, more deviated paraphrases versus plain success rates.

## 3) Dataset Download/Usage
Access the dataset via "HuggingFace Dataset" badge linking to `datasets/HAI-Lab/LIBERO-Para`. The repository combines paraphrased instructions with the original LIBERO benchmark suites (Spatial, Object, Goal, LIBERO-10, LIBERO-90).

## 4) Supported VLA Model Baselines
Six models are integrated:
- OpenVLA-OFT (Goal & Mixed variants, 7.5B parameters)
- Pi0.5 (3.3B, VLM + Action Expert)
- X-VLA (0.9B, Soft-prompted)
- VLA-Adapter (0.6B, Bridge-based)
- Xiaomi-Robotics-0 (4.7B, VLM + Action Expert)

## 5) OpenVLA-OFT Inclusion
**Yes**, fully included with guides and evaluation scripts for both Goal and Mixed configurations.

## 6) Installation & Evaluation
**Setup**:
```bash
conda create -n libero-para python=3.10 -y
pip install -r metrics/requirements.txt
python -m spacy download en_core_web_sm
```

**Evaluation**: Each model uses standalone scripts in `eval_scripts/examples/` with model-specific conda environments. Run: `python metrics/analyze_results.py --model_path logs_para/example_xiaomi-robotics-0`

## 7) Directory Structure
```
LIBERO-Para/
├── libero/                    # Benchmark core
├── metrics/                   # PRIDE metric & analysis
├── eval_guides/               # Per-model setup guides
├── eval_scripts/examples/     # Model-specific eval scripts
├── logs_para/                 # Evaluation results
└── benchmark_scripts/scripts/ # Utility scripts
```
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "b5d06542-c75e-40b0-b0ab-984cbc0a2326",
  "tool_use_result": {
    "bytes": 324288,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Para: Key Information Summary\n\n## 1) Data Files Available\nThe repository includes \"4,000+ paraphrased instructions across 10 evaluation scenarios.\" A metadata file exists at `metrics/libero_para_metadata.csv`. The dataset is available on HuggingFace at the HAI-Lab organization. Example results are provided in `logs_para/example_xiaomi-robotics-0/seed7/`.\n\n## 2) PRIDE Metric Location & Formula\n**Location**: `metrics/` directory with detailed documentation in `metrics/README.md` and an interactive notebook at `metrics/PRIDE_metric_playground.ipynb`\n\n**Formula Overview**: PRIDE computes Paraphrase Distance (PD) from keyword similarity (SK) and structural similarity (ST), then \"measures the ratio of PD-weighted successes to total possible PD, normalized to 0–100.\" It prioritizes success on harder, more deviated paraphrases versus plain success rates.\n\n## 3) Dataset Download/Usage\nAccess the dataset via \"HuggingFace Dataset\" badge linking to `datasets/HAI-Lab/LIBERO-Para`. The repository combines paraphrased instructions with the original LIBERO benchmark suites (Spatial, Object, Goal, LIBERO-10, LIBERO-90).\n\n## 4) Supported VLA Model Baselines\nSix models are integrated:\n- OpenVLA-OFT (Goal & Mixed variants, 7.5B parameters)\n- Pi0.5 (3.3B, VLM + Action Expert)\n- X-VLA (0.9B, Soft-prompted)\n- VLA-Adapter (0.6B, Bridge-based)\n- Xiaomi-Robotics-0 (4.7B, VLM + Action Expert)\n\n## 5) OpenVLA-OFT Inclusion\n**Yes**, fully included with guides and evaluation scripts for both Goal and Mixed configurations.\n\n## 6) Installation & Evaluation\n**Setup**:\n```bash\nconda create -n libero-para python=3.10 -y\npip install -r metrics/requirements.txt\npython -m spacy download en_core_web_sm\n```\n\n**Evaluation**: Each model uses standalone scripts in `eval_scripts/examples/` with model-specific conda environments. Run: `python metrics/analyze_results.py --model_path logs_para/example_xiaomi-robotics-0`\n\n## 7) Directory Structure\n```\nLIBERO-Para/\n├── libero/                    # Benchmark core\n├── metrics/                   # PRIDE metric & analysis\n├── eval_guides/               # Per-model setup guides\n├── eval_scripts/examples/     # Model-specific eval scripts\n├── logs_para/                 # Evaluation results\n└── benchmark_scripts/scripts/ # Utility scripts\n```",
    "durationMs": 9653,
    "url": "https://github.com/cau-hai-lab/LIBERO-Para"
  }
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-19T17:09:38.185Z_

<details><summary>↩ Tool result · `toolu_01QYUnwiGdotopRSCjihv8sV`</summary>

````text
# LIBERO-Para Dataset: Format, Structure, and Access

## 1. Dataset Format and Structure

LIBERO-Para is organized as a **diagnostic benchmark for evaluating paraphrase robustness in Vision-Language-Action (VLA) models**. The dataset structure is:

```
LIBERO-Para/
├── README.md
└── bddl_files/
    └── ...
```

The data uses **BDDL (Behavior Description Definition Language) files** compatible with the LIBERO evaluation environment.

## 2. Download Instructions

1. Download the dataset from Hugging Face
2. Extract the `bddl_files/` directory
3. Place files into your LIBERO installation:
   ```bash
   mv bddl_files/* /path/to/libero/libero/bddl_files/
   ```

For detailed setup and analysis scripts, see the [GitHub repository](https://github.com/cau-hai-lab/LIBERO-Para).

## 3. Number of Paraphrases

- **4,092** total paraphrased instructions
- **10** original LIBERO-Goal instructions
- **~100** samples per variation type cell
- **43** distinct paraphrase type combinations (3 Object types × 10 Action types, plus combinations)

## 4. File Formats Available

- **BDDL files** (primary format for LIBERO evaluation)
- **Total dataset size:** 12.1 MB
- Last month downloads: 151

## 5. Data Organization

The dataset is organized by a **two-axis paraphrase scheme**:

| Axis | Variation Types | Count |
|------|---|---|
| **Object** | Addition, SP-contextual, SP-habitual | 3 types |
| **Action** | Lexical (3), Structural (2), Pragmatic (5) | 10 types |
| **Combined** | Object × Action paraphrases | 30 types |

**Example distribution table:** The dataset provides ~100 samples per cell, with 4,092 total paraphrases distributed across 11 rows (object types) and 11 columns (action types).
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "160d6056-09bd-45f3-ba43-d916905334be",
  "tool_use_result": {
    "bytes": 131083,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Para Dataset: Format, Structure, and Access\n\n## 1. Dataset Format and Structure\n\nLIBERO-Para is organized as a **diagnostic benchmark for evaluating paraphrase robustness in Vision-Language-Action (VLA) models**. The dataset structure is:\n\n```\nLIBERO-Para/\n├── README.md\n└── bddl_files/\n    └── ...\n```\n\nThe data uses **BDDL (Behavior Description Definition Language) files** compatible with the LIBERO evaluation environment.\n\n## 2. Download Instructions\n\n1. Download the dataset from Hugging Face\n2. Extract the `bddl_files/` directory\n3. Place files into your LIBERO installation:\n   ```bash\n   mv bddl_files/* /path/to/libero/libero/bddl_files/\n   ```\n\nFor detailed setup and analysis scripts, see the [GitHub repository](https://github.com/cau-hai-lab/LIBERO-Para).\n\n## 3. Number of Paraphrases\n\n- **4,092** total paraphrased instructions\n- **10** original LIBERO-Goal instructions\n- **~100** samples per variation type cell\n- **43** distinct paraphrase type combinations (3 Object types × 10 Action types, plus combinations)\n\n## 4. File Formats Available\n\n- **BDDL files** (primary format for LIBERO evaluation)\n- **Total dataset size:** 12.1 MB\n- Last month downloads: 151\n\n## 5. Data Organization\n\nThe dataset is organized by a **two-axis paraphrase scheme**:\n\n| Axis | Variation Types | Count |\n|------|---|---|\n| **Object** | Addition, SP-contextual, SP-habitual | 3 types |\n| **Action** | Lexical (3), Structural (2), Pragmatic (5) | 10 types |\n| **Combined** | Object × Action paraphrases | 30 types |\n\n**Example distribution table:** The dataset provides ~100 samples per cell, with 4,092 total paraphrases distributed across 11 rows (object types) and 11 columns (action types).",
    "durationMs": 6313,
    "url": "https://huggingface.co/datasets/HAI-Lab/LIBERO-Para"
  }
}
````

</details>

---

### Tool result

_source line 24 · 2026-05-19T17:09:40.886Z_

<details><summary>↩ Tool result · `toolu_01FMo7vgB4uTntNj4epowFWt`</summary>

```text
# LIBERO-Para: Key Findings Summary

## PRIDE Metric Formula

The metric combines two components:

**Paraphrase Distance (PD):**
`PD = 1 - (α·SK(O,P) + (1-α)·ST(T_O,T_P))`

**PRIDE Score:**
`PRIDE = {PD if success, 0 if failure}`

Where SK measures "keyword similarity using semantic matching between task-critical content words" and ST uses "tree edit distance on dependency trees normalized by combined tree size."

## Core Experimental Results

**Success Rate Degradation (LIBERO-Goal vs LIBERO-Para):**
- OpenVLA-OFTgoal: 97.9% → 64.7% (−33.2pp)
- OpenVLA-OFTmixed: 96.1% → 63.7% (−32.4pp)
- π0.5: 97.6% → 71.4% (−26.2pp)
- VLA-Adapter: 98.2% → 46.3% (−51.9pp)
- X-VLA: 97.8% → 62.1% (−35.7pp)
- Xiaomi-Robotics-0: 98.8% → 76.0% (−22.8pp)

**PRIDE Scores on LIBERO-Para:**
Xiaomi-Robotics-0 achieved the highest PRIDE (69.2), while VLA-Adapter scored lowest (36.1).

## Paraphrase Taxonomy

**Action Axis (10 types):**
- Lexical: same-polarity habitual/contextual substitution, addition
- Structural: coordination, subordination
- Pragmatic: need statements, embedded imperatives, permission directives, question directives, hints

**Object Axis (3 types):**
- Same-polarity habitual/contextual substitution
- Addition

Total: "43 fine-grained variation types" across 4,092 paraphrased instructions from 10 original tasks.

## Generation Methodology

"Paraphrases are generated using Gemini 2.5 Pro" through an axis-wise approach: independent action and object paraphrase generation, verification via LLM, merging, and final validation. Human evaluation on 5% of data yielded "Gwet's AC1 of 0.854" (strong agreement), with 99.51% judged as meaning-preserving under majority vote.

## Critical Finding

"80–96% of failures arise from planning-level trajectory divergence rather than execution errors," suggesting "errors in task identification rather than motor control."

Human evaluation details: "15 annotators independently judged whether each original–paraphrase pair would elicit the same successful behavior" with high consensus (94.18% marked Yes).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "cc04842f-b653-4e49-aef0-512bbdf916e5",
  "tool_use_result": {
    "bytes": 404368,
    "code": 200,
    "codeText": "OK",
    "result": "# LIBERO-Para: Key Findings Summary\n\n## PRIDE Metric Formula\n\nThe metric combines two components:\n\n**Paraphrase Distance (PD):**\n`PD = 1 - (α·SK(O,P) + (1-α)·ST(T_O,T_P))`\n\n**PRIDE Score:**\n`PRIDE = {PD if success, 0 if failure}`\n\nWhere SK measures \"keyword similarity using semantic matching between task-critical content words\" and ST uses \"tree edit distance on dependency trees normalized by combined tree size.\"\n\n## Core Experimental Results\n\n**Success Rate Degradation (LIBERO-Goal vs LIBERO-Para):**\n- OpenVLA-OFTgoal: 97.9% → 64.7% (−33.2pp)\n- OpenVLA-OFTmixed: 96.1% → 63.7% (−32.4pp)\n- π0.5: 97.6% → 71.4% (−26.2pp)\n- VLA-Adapter: 98.2% → 46.3% (−51.9pp)\n- X-VLA: 97.8% → 62.1% (−35.7pp)\n- Xiaomi-Robotics-0: 98.8% → 76.0% (−22.8pp)\n\n**PRIDE Scores on LIBERO-Para:**\nXiaomi-Robotics-0 achieved the highest PRIDE (69.2), while VLA-Adapter scored lowest (36.1).\n\n## Paraphrase Taxonomy\n\n**Action Axis (10 types):**\n- Lexical: same-polarity habitual/contextual substitution, addition\n- Structural: coordination, subordination\n- Pragmatic: need statements, embedded imperatives, permission directives, question directives, hints\n\n**Object Axis (3 types):**\n- Same-polarity habitual/contextual substitution\n- Addition\n\nTotal: \"43 fine-grained variation types\" across 4,092 paraphrased instructions from 10 original tasks.\n\n## Generation Methodology\n\n\"Paraphrases are generated using Gemini 2.5 Pro\" through an axis-wise approach: independent action and object paraphrase generation, verification via LLM, merging, and final validation. Human evaluation on 5% of data yielded \"Gwet's AC1 of 0.854\" (strong agreement), with 99.51% judged as meaning-preserving under majority vote.\n\n## Critical Finding\n\n\"80–96% of failures arise from planning-level trajectory divergence rather than execution errors,\" suggesting \"errors in task identification rather than motor control.\"\n\nHuman evaluation details: \"15 annotators independently judged whether each original–paraphrase pair would elicit the same successful behavior\" with high consensus (94.18% marked Yes).",
    "durationMs": 10112,
    "url": "https://arxiv.org/html/2603.28301v1"
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Now I have most of the information. Let me also check if there are per-suite PRIDE scores (Spatial, Object, Goal, Long) for OpenVLA-OFT. The results I got seem to be only for LIBERO-Goal. Let me check if the paper has results for other suites too. Actually, looking more carefully at the data, LIBERO-Para seems to be specifically built on top of LIBERO-Goal (10 tasks from LIBERO-Goal), not all suites. Let me check this.

Actually, looking at the results:
- The paper says "10 original tasks" and "10 evaluation scenarios"


- The dataset is built from LIBERO-Goal tasks
- Results show success rates for LIBERO-Goal → LIBERO-Para degradation

So LIBERO-Para is specifically a paraphrase extension of LIBERO-Goal, not all suites. There don't seem to be separate suite breakdowns (Spatial, Object, Long) because those suites have different tasks. I have enough information now to compile the full report, and I found the GitHub repo is public at https://github.com/cau-hai-lab/LIBERO.

The dataset is available on HuggingFace under HAI-Lab/LIBERO-Para in BDDL format with 4,092 paraphrases plus metadata CSV. The PRIDE metric code is in the metrics directory with the formula extracted. For OpenVLA-OFT, I'm seeing significant degradation from LIBERO-Goal to LIBERO-Para: OpenVLA-OFTgoal drops from 97.9% to 64.7% (−33.2pp) and OpenVLA-OFTmixed from 96.1% to 63.7% (−32.4pp), with individual PRIDE scores ranging from 69.2 for Xiaomi-Robotics-0 down to 36.1 for VLA-Adapter.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "d0965814-68d5-4eee-8b62-7777cc3a2b23",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Noyprrmi54iBGhwvVc7f5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 542,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 26984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2411
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

_source line 26_

获取 PRIDE 分数完整表格。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "76638321-9162-42a3-91ed-89c966c4ce92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Noyprrmi54iBGhwvVc7f5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 542,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 26984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2411
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01L9kA7twKVT1h7R8GphStb6`</summary>

```json
{
  "url": "https://arxiv.org/html/2603.28301v1",
  "prompt": "Find and extract the COMPLETE table of PRIDE scores for ALL models. I need the exact PRIDE numerical scores for: OpenVLA-OFT (Goal), OpenVLA-OFT (Mixed), Pi0.5, X-VLA, VLA-Adapter, Xiaomi-Robotics-0. Also extract: 1) Are results broken down by suite (Spatial/Object/Goal/Long) or only LIBERO-Goal? 2) The exact PRIDE formula with all notation defined (what is alpha, what is SK, what is ST, how is final PRIDE aggregated across tasks). 3) Any per-task or per-axis breakdown of PRIDE scores."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "76b4e577-8976-487b-b127-b5b6d47d46db",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Noyprrmi54iBGhwvVc7f5X",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 542,
      "cache_creation_input_tokens": 2411,
      "cache_read_input_tokens": 26984,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2411
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

_source line 28 · 2026-05-19T17:10:04.537Z_

<details><summary>↩ Tool result · `toolu_01L9kA7twKVT1h7R8GphStb6`</summary>

````text
# PRIDE Score Extraction and Analysis

## Complete PRIDE Scores by Model

Based on Table 3 in the document:

| Model | SR | PRIDE | Overestimation (%) |
|-------|----|----|---|
| VLA-Adapter | 46.3 | 36.1 | 22.0 |
| π0.5 (expert-only) | 39.1 | 32.0 | 18.2 |
| X-VLA | 62.1 | 52.7 | 15.1 |
| OpenVLA-OFTmixed | 63.7 | 56.3 | 11.6 |
| OpenVLA-OFTgoal | 64.7 | 58.8 | 9.1 |
| Xiaomi-Robotics-0 | 76.0 | 69.2 | 8.9 |
| π0.5 | 71.4 | 65.4 | 8.4 |

## Evaluation Scope

Results are **exclusively from LIBERO-Goal**, not broken down by task suites. The paper states: "LIBERO-Para is constructed on top of LIBERO-Goal, a setting in which linguistic understanding is essential."

## PRIDE Formula Complete Definition

**Paraphrase Distance (PD):**
```
PD = 1 - (α·SK(O,P) + (1-α)·ST(T_O, T_P))
```

Where:
- **SK (Keyword Similarity)**: "matching each content word o_i in the original instruction to the most similar word in the paraphrase, measured by cosine similarity"
- **ST (Structural Similarity)**: Based on "tree edit distance (TED) between the dependency trees" using "POS tags and dependency relations"
- **α**: Weighting parameter controlling keyword vs. structural contribution (default α=0.5)

**Final PRIDE Score:**
```
PRIDE = {PD,    if success
        {0,    if failure
```

## Per-Axis Breakdown

Figures 10-11 provide Object × Action cell breakdowns showing averaged keyword distance and structural distance separately, but aggregate PRIDE scores by cell aren't explicitly tabulated in the main text.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "f19b985b-d179-4291-86e2-19bb946b2a7b",
  "tool_use_result": {
    "bytes": 404368,
    "code": 200,
    "codeText": "OK",
    "result": "# PRIDE Score Extraction and Analysis\n\n## Complete PRIDE Scores by Model\n\nBased on Table 3 in the document:\n\n| Model | SR | PRIDE | Overestimation (%) |\n|-------|----|----|---|\n| VLA-Adapter | 46.3 | 36.1 | 22.0 |\n| π0.5 (expert-only) | 39.1 | 32.0 | 18.2 |\n| X-VLA | 62.1 | 52.7 | 15.1 |\n| OpenVLA-OFTmixed | 63.7 | 56.3 | 11.6 |\n| OpenVLA-OFTgoal | 64.7 | 58.8 | 9.1 |\n| Xiaomi-Robotics-0 | 76.0 | 69.2 | 8.9 |\n| π0.5 | 71.4 | 65.4 | 8.4 |\n\n## Evaluation Scope\n\nResults are **exclusively from LIBERO-Goal**, not broken down by task suites. The paper states: \"LIBERO-Para is constructed on top of LIBERO-Goal, a setting in which linguistic understanding is essential.\"\n\n## PRIDE Formula Complete Definition\n\n**Paraphrase Distance (PD):**\n```\nPD = 1 - (α·SK(O,P) + (1-α)·ST(T_O, T_P))\n```\n\nWhere:\n- **SK (Keyword Similarity)**: \"matching each content word o_i in the original instruction to the most similar word in the paraphrase, measured by cosine similarity\"\n- **ST (Structural Similarity)**: Based on \"tree edit distance (TED) between the dependency trees\" using \"POS tags and dependency relations\"\n- **α**: Weighting parameter controlling keyword vs. structural contribution (default α=0.5)\n\n**Final PRIDE Score:**\n```\nPRIDE = {PD,    if success\n        {0,    if failure\n```\n\n## Per-Axis Breakdown\n\nFigures 10-11 provide Object × Action cell breakdowns showing averaged keyword distance and structural distance separately, but aggregate PRIDE scores by cell aren't explicitly tabulated in the main text.",
    "durationMs": 7531,
    "url": "https://arxiv.org/html/2603.28301v1"
  }
}
````

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information needed. Let me compile the report.

Key takeaways:
1. GitHub repo: Public ✓
2. Data: Available on HuggingFace ✓ (BDDL format + metadata CSV)
3. PRIDE: Code available ✓ (metrics/ directory, notebook, formula extracted)
4. OpenVLA-OFT PRIDE scores: 
   - OFTgoal: SR=64.7%, PRIDE=58.8
   - OFTmixed: SR=63.7%, PRIDE=56.3
5. LIBERO-Para is ONLY for LIBERO-Goal (not Spatial/Object/Long)


6. Gemini 2.5 Pro generated 4,092 paraphrases across 43 variation types, and the overestimation column quantifies how much SR overstates robustness compared to PRIDE

For Phase 0.5, since LIBERO-Para only covers LIBERO-Goal, I'd need to either restrict evaluation to just that suite or extend the paraphrase approach to the others myself. The good news is the OpenVLA-OFT baseline scores are already available, so I won't need to re-run those for the LIBERO-Para evaluation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "cc618566-c389-4ed3-a342-6fbc3bc5f2f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W59adZQg1xk13sYevKhVps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 29395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

信息收集完毕。以下是完整报告。

---

## LIBERO-Para 可用性验证报告

### 1. 代码/数据: **完全可用**

| 资源 | 链接 | 状态 |
|------|------|------|
| GitHub repo | [cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para) | 公开，含评估脚本+PRIDE代码 |
| HuggingFace 数据集 | [HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para) | 公开，12.1MB |
| 数据格式 | BDDL 文件 + `metrics/libero_para_metadata.csv` | 可直接用于 LIBERO 评估 |

**数据规模**: 4,092 条 paraphrase 指令，来自 10 个 LIBERO-Goal 原始任务，43 种变体类型（3 Object × 10 Action + 组合）。

**生成方法**: Gemini 2.5 Pro 生成，axis-wise 独立生成 action/object paraphrase → LLM 验证 → 合并 → 人工验证（5% 抽检，Gwet's AC1=0.854，99.51% meaning-preserving）。

### 2. PRIDE Metric: **有代码 + 公式**

代码位置: `metrics/` 目录，含 `PRIDE_metric_playground.ipynb` 交互笔记本和 `analyze_results.py`。

**公式**:
```
PD(O, P) = 1 - (α · SK(O, P) + (1-α) · ST(T_O, T_P))

PRIDE = PD   if success
        0    if failure
```
- **SK**: keyword similarity，content word 的 cosine similarity
- **ST**: structural similarity，dependency tree edit distance
- **α**: 默认 0.5
- PRIDE 越高越好，给困难 paraphrase 更多权重

### 3. OpenVLA-OFT Baseline PRIDE 分数: **有**

| Model | Params | SR (%) | PRIDE | Overestimation (%) |
|-------|--------|--------|-------|---------------------|
| VLA-Adapter | 0.6B | 46.3 | 36.1 | 22.0 |
| π0.5 (expert-only) | 3.3B | 39.1 | 32.0 | 18.2 |
| X-VLA | 0.9B | 62.1 | 52.7 | 15.1 |
| **OpenVLA-OFT_mixed** | **7.5B** | **63.7** | **56.3** | **11.6** |
| **OpenVLA-OFT_goal** | **7.5B** | **64.7** | **58.8** | **9.1** |
| π0.5 | 3.3B | 71.4 | 65.4 | 8.4 |
| Xiaomi-Robotics-0 | 4.7B | 76.0 | 69.2 | 8.9 |

原始 LIBERO-Goal SR → Para SR 退化：OFT_goal 97.9% → 64.7% (−33.2pp)，OFT_mixed 96.1% → 63.7% (−32.4pp)。

### 4. 关键限制

**LIBERO-Para 仅覆盖 LIBERO-Goal**（10 个任务），不含 Spatial/Object/Long 套件。论文原文："LIBERO-Para is constructed on top of LIBERO-Goal, a setting in which linguistic understanding is essential."

### 5. 对 Phase 0.5 的影响

- **不需要自行跑 OFT baseline** — 论文已提供 OFT_goal 和 OFT_mixed 的 PRIDE 分数
- **可直接复用** LIBERO-Para 的 paraphrase 数据和 PRIDE 评估代码
- **局限**: 如需在 Spatial/Object/Long 上评估 paraphrase robustness，需自行扩展 paraphrase 数据（可参考其 Gemini 2.5 Pro 生成 pipeline）
- 核心发现（80-96% 失败来自 planning-level trajectory divergence）与我们的 affordance invariance 方向高度相关

Sources:
- [arXiv 2603.28301](https://arxiv.org/abs/2603.28301)
- [GitHub: cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)
- [HuggingFace: HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para)
- [Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "uuid": "1ed8fcf5-216b-425d-beae-23c70b21733d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01W59adZQg1xk13sYevKhVps",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1875,
      "cache_read_input_tokens": 29395,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1875
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

_source line 31_

信息收集完毕。以下是完整报告。

---

## LIBERO-Para 可用性验证报告

### 1. 代码/数据: **完全可用**

| 资源 | 链接 | 状态 |
|------|------|------|
| GitHub repo | [cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para) | 公开，含评估脚本+PRIDE代码 |
| HuggingFace 数据集 | [HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para) | 公开，12.1MB |
| 数据格式 | BDDL 文件 + `metrics/libero_para_metadata.csv` | 可直接用于 LIBERO 评估 |

**数据规模**: 4,092 条 paraphrase 指令，来自 10 个 LIBERO-Goal 原始任务，43 种变体类型（3 Object × 10 Action + 组合）。

**生成方法**: Gemini 2.5 Pro 生成，axis-wise 独立生成 action/object paraphrase → LLM 验证 → 合并 → 人工验证（5% 抽检，Gwet's AC1=0.854，99.51% meaning-preserving）。

### 2. PRIDE Metric: **有代码 + 公式**

代码位置: `metrics/` 目录，含 `PRIDE_metric_playground.ipynb` 交互笔记本和 `analyze_results.py`。

**公式**:
```
PD(O, P) = 1 - (α · SK(O, P) + (1-α) · ST(T_O, T_P))

PRIDE = PD   if success
        0    if failure
```
- **SK**: keyword similarity，content word 的 cosine similarity
- **ST**: structural similarity，dependency tree edit distance
- **α**: 默认 0.5
- PRIDE 越高越好，给困难 paraphrase 更多权重

### 3. OpenVLA-OFT Baseline PRIDE 分数: **有**

| Model | Params | SR (%) | PRIDE | Overestimation (%) |
|-------|--------|--------|-------|---------------------|
| VLA-Adapter | 0.6B | 46.3 | 36.1 | 22.0 |
| π0.5 (expert-only) | 3.3B | 39.1 | 32.0 | 18.2 |
| X-VLA | 0.9B | 62.1 | 52.7 | 15.1 |
| **OpenVLA-OFT_mixed** | **7.5B** | **63.7** | **56.3** | **11.6** |
| **OpenVLA-OFT_goal** | **7.5B** | **64.7** | **58.8** | **9.1** |
| π0.5 | 3.3B | 71.4 | 65.4 | 8.4 |
| Xiaomi-Robotics-0 | 4.7B | 76.0 | 69.2 | 8.9 |

原始 LIBERO-Goal SR → Para SR 退化：OFT_goal 97.9% → 64.7% (−33.2pp)，OFT_mixed 96.1% → 63.7% (−32.4pp)。

### 4. 关键限制

**LIBERO-Para 仅覆盖 LIBERO-Goal**（10 个任务），不含 Spatial/Object/Long 套件。论文原文："LIBERO-Para is constructed on top of LIBERO-Goal, a setting in which linguistic understanding is essential."

### 5. 对 Phase 0.5 的影响

- **不需要自行跑 OFT baseline** — 论文已提供 OFT_goal 和 OFT_mixed 的 PRIDE 分数
- **可直接复用** LIBERO-Para 的 paraphrase 数据和 PRIDE 评估代码
- **局限**: 如需在 Spatial/Object/Long 上评估 paraphrase robustness，需自行扩展 paraphrase 数据（可参考其 Gemini 2.5 Pro 生成 pipeline）
- 核心发现（80-96% 失败来自 planning-level trajectory divergence）与我们的 affordance invariance 方向高度相关

Sources:
- [arXiv 2603.28301](https://arxiv.org/abs/2603.28301)
- [GitHub: cau-hai-lab/LIBERO-Para](https://github.com/cau-hai-lab/LIBERO-Para)
- [HuggingFace: HAI-Lab/LIBERO-Para](https://huggingface.co/datasets/HAI-Lab/LIBERO-Para)
- [Project Page](https://cau-hai-lab.github.io/LIBERO-Para/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 86488,
  "duration_api_ms": 123454,
  "num_turns": 10,
  "stop_reason": "end_turn",
  "session_id": "96dbfa24-ddd7-4883-9e64-bfd17b440d5a",
  "total_cost_usd": 0.43059575,
  "usage": {
    "input_tokens": 899,
    "cache_creation_input_tokens": 19429,
    "cache_read_input_tokens": 116033,
    "output_tokens": 3500,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 19429,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1695,
        "cache_read_input_tokens": 29395,
        "cache_creation_input_tokens": 1875,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1875
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 109153,
      "outputTokens": 4000,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.159153,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 899,
      "outputTokens": 3500,
      "cacheReadInputTokens": 116033,
      "cacheCreationInputTokens": 19429,
      "webSearchRequests": 0,
      "costUSD": 0.27144274999999995,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "cb396669-a86c-4c0e-b780-d18499c3a990"
}
```

</details>

---
