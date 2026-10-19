# research pi05 official eval 20260522T092201 retry2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 37
- **Recorded user turns:** 0
- **Tool calls:** 12
- **Original source:** `logs/workers/worker_research_pi05-official-eval_20260522T092201_retry2.log`
- **Structured JSON:** [`021e48e8c8a7680c92f0.json`](../../sessions/02/021e48e8c8a7680c92f0.json)

## Before a recorded user message

37 recorded events

### System

_source line 1_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
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
  "uuid": "02268d85-05ce-47db-ae3c-8dfc26e6a7e4",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1779667200,
    "rateLimitType": "seven_day",
    "utilization": 0.99,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "64973dca-9a0e-4bf4-aba0-66b81dea69ee",
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234"
}
```

---

### Assistant

_source line 3_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to research whether π0.5 / Physical Intelligence has official LIBERO evaluation scripts. Let me launch parallel web searches to gather this information efficiently.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "a7181061-1373-489f-9104-9aeaff04ac3c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cde7yfs79iUpnfCmfEZ2dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11589,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11589
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

开始调研 π0.5 的 LIBERO 评估资源。并行搜索多个方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "94ed39d6-16f5-4652-a76a-2dd918f9458d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cde7yfs79iUpnfCmfEZ2dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11589,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11589
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Rjp591ouDv42YPY7LZT8Fa`</summary>

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
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "5a09a47d-6669-41ec-847b-ad9c73b92010",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cde7yfs79iUpnfCmfEZ2dz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11589,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11589
      },
      "output_tokens": 29,
      "service_tier": "standard",
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

_source line 6 · 2026-05-22T09:22:38.520Z_

<details><summary>↩ Tool result · `toolu_01Rjp591ouDv42YPY7LZT8Fa`</summary>

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
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "650091b4-7801-4865-81bd-35f01eb9fa95",
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

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01R7vNwvHeRED2ycyQWmhUTd`</summary>

```json
{
  "query": "pi0.5 physical intelligence github lerobot LIBERO evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "a4ded93d-a9f4-4062-a3f2-f7569e5aeea1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDJ2GJgYa6WT7hDAHPW373",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 23430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
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

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UR4D7KLXJzckJv78siaKEs`</summary>

```json
{
  "query": "huggingface lerobot LIBERO benchmark eval script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "822740b5-fdbf-4f1d-90a9-d2560da0f6b8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDJ2GJgYa6WT7hDAHPW373",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 23430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AMphrGSmTNqwhNxuip1vR3`</summary>

```json
{
  "query": "pi0.5 paper LIBERO success rate benchmark results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "26fd39e9-6ba2-472b-b21c-83933010a8d1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GDJ2GJgYa6WT7hDAHPW373",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 685,
      "cache_read_input_tokens": 23430,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 685
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

_source line 10 · 2026-05-22T09:22:51.713Z_

<details><summary>↩ Tool result · `toolu_01R7vNwvHeRED2ycyQWmhUTd`</summary>

```text
Web search results for query: "pi0.5 physical intelligence github lerobot LIBERO evaluation"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/pi0_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_libero_base"},{"title":"Run pi0.5 on Libero, incorrect version of transformers · Issue #2697 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2697"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"}]

Based on the web search results, here's what I found about pi0.5, Physical Intelligence, LeRobot, and LIBERO evaluation:

## Overview

π₀.₅ is a Vision-Language-Action (VLA) model with open-world generalization from Physical Intelligence, co-trained on robot demonstrations and large-scale multimodal data to execute long-horizon tasks in unseen real-world environments.

## GitHub and Implementation

The π₀.₅ model is demonstrated on the LIBERO dataset as a running example for how to fine-tune a base model on your own data. The LeRobot implementation is adapted from their open source OpenPI repository.

## LIBERO Evaluation

LIBERO is a benchmark designed to study lifelong robot learning — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on knowledge transfer: how well a robot can apply what it has already learned to new situations.

π₀.₅ has demonstrated strong performance on the Libero benchmark suite. LeRobot finetuned the libero base model for an additional 6k steps on the Libero dataset and compared the results to the OpenPI reference results.

## Available Models

Several pretrained models are available on Hugging Face Hub, including base models (pi05_libero_base) and finetuned versions (pi05_libero_finetuned) that can be evaluated using the LeRobot evaluation tools.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "21be9c36-4d74-4579-b80e-b89980584226",
  "tool_use_result": {
    "query": "pi0.5 physical intelligence github lerobot LIBERO evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DpJ9agkYf1NMF8DtCkFUop",
        "content": [
          {
            "title": "GitHub - Physical-Intelligence/openpi · GitHub",
            "url": "https://github.com/Physical-Intelligence/openpi"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "lerobot/pi0_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi0_libero_base"
          },
          {
            "title": "Run pi0.5 on Libero, incorrect version of transformers · Issue #2697 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2697"
          },
          {
            "title": "lerobot/pi05_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_base"
          },
          {
            "title": "lerobot/pi05_libero_finetuned · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned"
          },
          {
            "title": "lerobot/pi05_libero_finetuned_v044 · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned_v044"
          },
          {
            "title": "π₀.₅ (Pi05) Policy · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi05"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "lerobot/docs/source/pi05.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"
          }
        ]
      },
      "Based on the web search results, here's what I found about pi0.5, Physical Intelligence, LeRobot, and LIBERO evaluation:\n\n## Overview\n\nπ₀.₅ is a Vision-Language-Action (VLA) model with open-world generalization from Physical Intelligence, co-trained on robot demonstrations and large-scale multimodal data to execute long-horizon tasks in unseen real-world environments.\n\n## GitHub and Implementation\n\nThe π₀.₅ model is demonstrated on the LIBERO dataset as a running example for how to fine-tune a base model on your own data. The LeRobot implementation is adapted from their open source OpenPI repository.\n\n## LIBERO Evaluation\n\nLIBERO is a benchmark designed to study lifelong robot learning — the idea that robots need to keep learning and adapting with their users over time, not just be pretrained once. It provides a set of standardized manipulation tasks that focus on knowledge transfer: how well a robot can apply what it has already learned to new situations.\n\nπ₀.₅ has demonstrated strong performance on the Libero benchmark suite. LeRobot finetuned the libero base model for an additional 6k steps on the Libero dataset and compared the results to the OpenPI reference results.\n\n## Available Models\n\nSeveral pretrained models are available on Hugging Face Hub, including base models (pi05_libero_base) and finetuned versions (pi05_libero_finetuned) that can be evaluated using the LeRobot evaluation tools."
    ],
    "durationSeconds": 6.741305190000001
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-22T09:22:52.548Z_

<details><summary>↩ Tool result · `toolu_01AMphrGSmTNqwhNxuip1vR3`</summary>

```text
Web search results for query: "pi0.5 paper LIBERO success rate benchmark results"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"},{"title":"Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2114"},{"title":"pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2533"},{"title":"[Quick Review] π_RL: Online RL Fine-tuning for Flow-based\\n Vision-Language-Action Models","url":"https://liner.com/review/%CF%80_rl-online-rl-finetuning-for-flowbased-visionlanguageaction-models"},{"title":"Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"},{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"}]

Based on the search results, here are the key benchmark results for pi0.5 on LIBERO:

## Standard LIBERO Benchmark Results

Pi0.5 achieves success rates of 97.4% on libero_spatial, 98.4% on libero_object, 97.6% on libero_goal, and 93.0% on libero_10.

## Performance Under Perturbations (LIBERO-PRO)

The results are notably different when models are tested on a more robust evaluation suite called LIBERO-PRO, which introduces perturbations:

Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0. This highlights a significant gap between standard benchmark performance and robustness to real-world variations.

Pi0.5 exhibits improved resilience compared to other models and sustains non-trivial accuracy up to 0.4 units of displacement before collapsing to zero success, though this still represents a dramatic drop from its ~97% performance on standard LIBERO.

## Key Insight

Despite achieving over 90% on the standard LIBERO benchmark, the reported scores reflect rote recall rather than genuine task understanding, suggesting that pi0.5's high standard benchmark scores may not translate to robust real-world performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "e556c732-57ce-4fc4-a126-952f2f40e43c",
  "tool_use_result": {
    "query": "pi0.5 paper LIBERO success rate benchmark results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PGRn3HS1KX28Atqg3Kp7yG",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "(PDF) LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://www.researchgate.net/publication/396249917_LIBERO-PRO_Towards_Robust_and_Fair_Evaluation_of_Vision-Language-Action_Models_Beyond_Memorization"
          },
          {
            "title": "Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2114"
          },
          {
            "title": "pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2533"
          },
          {
            "title": "[Quick Review] π_RL: Online RL Fine-tuning for Flow-based\\n Vision-Language-Action Models",
            "url": "https://liner.com/review/%CF%80_rl-online-rl-finetuning-for-flowbased-visionlanguageaction-models"
          },
          {
            "title": "Success rates of OpenVLA, pi0, pi0.5, and univla under object position... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Success-rates-of-OpenVLA-pi0-pi05-and-univla-under-object-position-perturbations_fig1_396249917"
          },
          {
            "title": "Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/734"
          },
          {
            "title": "PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/711"
          }
        ]
      },
      "Based on the search results, here are the key benchmark results for pi0.5 on LIBERO:\n\n## Standard LIBERO Benchmark Results\n\nPi0.5 achieves success rates of 97.4% on libero_spatial, 98.4% on libero_object, 97.6% on libero_goal, and 93.0% on libero_10.\n\n## Performance Under Perturbations (LIBERO-PRO)\n\nThe results are notably different when models are tested on a more robust evaluation suite called LIBERO-PRO, which introduces perturbations:\n\nPi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0. This highlights a significant gap between standard benchmark performance and robustness to real-world variations.\n\nPi0.5 exhibits improved resilience compared to other models and sustains non-trivial accuracy up to 0.4 units of displacement before collapsing to zero success, though this still represents a dramatic drop from its ~97% performance on standard LIBERO.\n\n## Key Insight\n\nDespite achieving over 90% on the standard LIBERO benchmark, the reported scores reflect rote recall rather than genuine task understanding, suggesting that pi0.5's high standard benchmark scores may not translate to robust real-world performance."
    ],
    "durationSeconds": 6.673242252
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-22T09:22:53.069Z_

<details><summary>↩ Tool result · `toolu_01UR4D7KLXJzckJv78siaKEs`</summary>

```text
Web search results for query: "huggingface lerobot LIBERO benchmark eval script"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"lerobot/xvla-libero · Hugging Face","url":"https://huggingface.co/lerobot/xvla-libero"},{"title":"lerobot/pi0_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi0_libero_base"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"π₀-FAST (Pi0-FAST) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0fast"},{"title":"Adding a New Benchmark · Hugging Face","url":"https://huggingface.co/docs/lerobot/adding_benchmarks"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"}]

Based on the search results, here's information about the Hugging Face LeRobot LIBERO benchmark evaluation script:

## Evaluation Script Overview

LeRobot provides a unified evaluation script to evaluate your policies in simulation or on real hardware, and LeRobot supports standard benchmarks like LIBERO, MetaWorld and more to come.

## Basic Usage

The evaluation is performed using the `lerobot-eval` command. A basic example is: `lerobot-eval --policy.path="your-policy-id" --env.type=libero --env.task=libero_object --eval.batch_size=2 --eval.n_episodes=3`

## Key Parameters

The `--env.task` parameter picks the suite (libero_object, libero_spatial, etc.), while `--env.task_ids` restricts to specific task indices ([0], [1,2,3], etc.), and you can omit it to run all tasks in the suite. The `--eval.batch_size` parameter controls how many environments run in parallel, and `--eval.n_episodes` sets how many episodes to run per task.

## Benchmarking Standard

For reproducible benchmarking, use 10 episodes per task across all four standard suites (Spatial, Object, Goal, Long), which gives 400 total episodes and matches the protocol used for published results.

## Multiple Suites

You can benchmark a policy across multiple suites at once by passing a comma-separated list, for example: `lerobot-eval --policy.path="your-policy-id" --env.type=libero --env.task=libero_object,libero_spatial --eval.batch_size=1 --eval.n_episodes=2`


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "303a02f5-9dc1-4639-86bf-098a883b5030",
  "tool_use_result": {
    "query": "huggingface lerobot LIBERO benchmark eval script",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HtmLpPLCgAbtHBQCiNdvCT",
        "content": [
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "lerobot/pi05_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_base"
          },
          {
            "title": "lerobot/xvla-libero · Hugging Face",
            "url": "https://huggingface.co/lerobot/xvla-libero"
          },
          {
            "title": "lerobot/pi0_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi0_libero_base"
          },
          {
            "title": "GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.",
            "url": "https://github.com/huggingface/lerobot-libero"
          },
          {
            "title": "π₀-FAST (Pi0-FAST) · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi0fast"
          },
          {
            "title": "Adding a New Benchmark · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/adding_benchmarks"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          }
        ]
      },
      "Based on the search results, here's information about the Hugging Face LeRobot LIBERO benchmark evaluation script:\n\n## Evaluation Script Overview\n\nLeRobot provides a unified evaluation script to evaluate your policies in simulation or on real hardware, and LeRobot supports standard benchmarks like LIBERO, MetaWorld and more to come.\n\n## Basic Usage\n\nThe evaluation is performed using the `lerobot-eval` command. A basic example is: `lerobot-eval --policy.path=\"your-policy-id\" --env.type=libero --env.task=libero_object --eval.batch_size=2 --eval.n_episodes=3`\n\n## Key Parameters\n\nThe `--env.task` parameter picks the suite (libero_object, libero_spatial, etc.), while `--env.task_ids` restricts to specific task indices ([0], [1,2,3], etc.), and you can omit it to run all tasks in the suite. The `--eval.batch_size` parameter controls how many environments run in parallel, and `--eval.n_episodes` sets how many episodes to run per task.\n\n## Benchmarking Standard\n\nFor reproducible benchmarking, use 10 episodes per task across all four standard suites (Spatial, Object, Goal, Long), which gives 400 total episodes and matches the protocol used for published results.\n\n## Multiple Suites\n\nYou can benchmark a policy across multiple suites at once by passing a comma-separated list, for example: `lerobot-eval --policy.path=\"your-policy-id\" --env.type=libero --env.task=libero_object,libero_spatial --eval.batch_size=1 --eval.n_episodes=2`"
    ],
    "durationSeconds": 7.572046730999999
  }
}
```

</details>

---

### Assistant

_source line 13_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a lot of useful information. Let me now dig deeper into a few specific areas:

1. The lerobot LIBERO eval documentation page
2. The openpi repo for LIBERO eval scripts
3. The lerobot issues about replicating pi0.5 LIBERO results
4. The official reported numbers

Let me search for more details on the specific issues and the openpi repo.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "456d59ad-64c2-4500-b587-db541bf60cb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZfWZqdrn4E4EgZdfDXXZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
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

_source line 14_

找到关键信息，继续深挖几个具体方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "0b5d5487-0428-4b3e-9ecf-019d4ddfb2bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZfWZqdrn4E4EgZdfDXXZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L15dsVa9EZoWjRVs1D1XeS`</summary>

```json
{
  "query": "site:github.com/Physical-Intelligence/openpi LIBERO evaluation script"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "fcc9b3a6-d5b4-4ac0-918a-5fcad3756583",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZfWZqdrn4E4EgZdfDXXZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01L9AwQXZbscTb6Nx7nzMejM`</summary>

```json
{
  "query": "site:github.com/huggingface/lerobot/issues/2114 pi0.5 LIBERO success rate replicate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "8bb26311-ddda-4876-ad73-f73f452466cb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZfWZqdrn4E4EgZdfDXXZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
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

_source line 17_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011AmjpRYbriistv8h4NtQ4d`</summary>

```json
{
  "query": "lerobot pi05_libero_finetuned evaluation results success rate official"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "fb3a557b-9bd9-4109-83b6-d17eec696056",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CZfWZqdrn4E4EgZdfDXXZn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 968,
      "cache_creation_input_tokens": 1923,
      "cache_read_input_tokens": 24115,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1923
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

_source line 18 · 2026-05-22T09:23:07.462Z_

<details><summary>↩ Tool result · `toolu_01L15dsVa9EZoWjRVs1D1XeS`</summary>

```text
Web search results for query: "site:github.com/Physical-Intelligence/openpi LIBERO evaluation script"

Links: [{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub","url":"https://github.com/Tonghe-Zhang/openpi-physical-intelligence"},{"title":"GitHub - RUreadyo/openpi · GitHub","url":"https://github.com/RUreadyo/openpi"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"GitHub - chancharikmitra/openpi_robotv · GitHub","url":"https://github.com/chancharikmitra/openpi_robotv"},{"title":"GitHub - Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"},{"title":"GitHub - gist-ailab/contact-openpi · GitHub","url":"https://github.com/gist-ailab/contact-openpi"},{"title":"Does VLA model really have generalisation capabilities? Or is it just a overfit? | by Yanan Chen | Medium","url":"https://medium.com/@yananchen1116/does-vla-model-really-have-generalisation-capabilities-or-is-it-just-a-overfit-270ffd7a04db"}]

Based on the search results from the Physical-Intelligence/openpi GitHub repository, here's what I found regarding the LIBERO evaluation script:

Once training is complete, you can run inference by spinning up a policy server and querying it from a LIBERO evaluation script. For running the LIBERO eval, they provide and recommend using a Dockerized workflow that handles both the policy server and the evaluation script together, with details available in the LIBERO README.

The typical workflow involves:

1. Launching a model server using `uv run scripts/serve_policy.py` with appropriate checkpoint configuration, which spins up a server listening on port 8000 and waits for observations to be sent to it.

2. Running the LIBERO evaluation script to query the server, with instructions on how to install LIBERO and run the evaluation script available in the LIBERO README.

For more specific details about the evaluation script itself, you'll want to consult the dedicated LIBERO README file in the repository, which contains the complete instructions for installation and execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "601fd443-d29d-4410-bcf7-914f591aa2b1",
  "tool_use_result": {
    "query": "site:github.com/Physical-Intelligence/openpi LIBERO evaluation script",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CZQPYFgTaFdMct1Y3Y2dJp",
        "content": [
          {
            "title": "GitHub - Physical-Intelligence/openpi · GitHub",
            "url": "https://github.com/Physical-Intelligence/openpi"
          },
          {
            "title": "GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub",
            "url": "https://github.com/Tonghe-Zhang/openpi-physical-intelligence"
          },
          {
            "title": "GitHub - RUreadyo/openpi · GitHub",
            "url": "https://github.com/RUreadyo/openpi"
          },
          {
            "title": "openpi/README.md at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/README.md"
          },
          {
            "title": "GitHub - chancharikmitra/openpi_robotv · GitHub",
            "url": "https://github.com/chancharikmitra/openpi_robotv"
          },
          {
            "title": "GitHub - Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"
          },
          {
            "title": "GitHub - gist-ailab/contact-openpi · GitHub",
            "url": "https://github.com/gist-ailab/contact-openpi"
          },
          {
            "title": "Does VLA model really have generalisation capabilities? Or is it just a overfit? | by Yanan Chen | Medium",
            "url": "https://medium.com/@yananchen1116/does-vla-model-really-have-generalisation-capabilities-or-is-it-just-a-overfit-270ffd7a04db"
          }
        ]
      },
      "Based on the search results from the Physical-Intelligence/openpi GitHub repository, here's what I found regarding the LIBERO evaluation script:\n\nOnce training is complete, you can run inference by spinning up a policy server and querying it from a LIBERO evaluation script. For running the LIBERO eval, they provide and recommend using a Dockerized workflow that handles both the policy server and the evaluation script together, with details available in the LIBERO README.\n\nThe typical workflow involves:\n\n1. Launching a model server using `uv run scripts/serve_policy.py` with appropriate checkpoint configuration, which spins up a server listening on port 8000 and waits for observations to be sent to it.\n\n2. Running the LIBERO evaluation script to query the server, with instructions on how to install LIBERO and run the evaluation script available in the LIBERO README.\n\nFor more specific details about the evaluation script itself, you'll want to consult the dedicated LIBERO README file in the repository, which contains the complete instructions for installation and execution."
    ],
    "durationSeconds": 6.076491520999996
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T09:23:08.202Z_

<details><summary>↩ Tool result · `toolu_011AmjpRYbriistv8h4NtQ4d`</summary>

```text
Web search results for query: "lerobot pi05_libero_finetuned evaluation results success rate official"

Links: [{"title":"Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2114"},{"title":"pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2533"},{"title":"Libero - LeRobot","url":"https://www.mintlify.com/huggingface/lerobot/simulation/libero"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"},{"title":"PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/952"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi05"}]

Based on the search results, here are the evaluation results for the `pi05_libero_finetuned` model:

## Official Reported Success Rates

According to the official LeRobot documentation, the π₀.₅ model achieves the following benchmark results on LIBERO tasks:
- Libero Spatial: 98.8%
- Libero Object: 98.2%
- Libero Goal: 98.0%
- Libero 10: 92.4%
- Average: 96.85%

## Known Issues with Reproduction

However, there are documented discrepancies when attempting to reproduce these results. One GitHub issue reported observed success rates of: libero_spatial 77%, libero_object 66%, libero_goal 89%, libero_10 55%, with a total of 71.75%, which is significantly lower than the official reported rates.

The reported success rates for both models are about 10-20% higher than the observed ones, suggesting there may be configuration or environment setup differences between the official benchmarking and community reproduction attempts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "8eb1d4d7-636a-44ff-ad40-5f029a19401e",
  "tool_use_result": {
    "query": "lerobot pi05_libero_finetuned evaluation results success rate official",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CfZmbV6tvUZ6GrXUm6pkBT",
        "content": [
          {
            "title": "Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2114"
          },
          {
            "title": "pi0.5 on LIBERO simulation reproduce, zero success rate on pi05_libero_base · Issue #2533 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2533"
          },
          {
            "title": "Libero - LeRobot",
            "url": "https://www.mintlify.com/huggingface/lerobot/simulation/libero"
          },
          {
            "title": "PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/711"
          },
          {
            "title": "lerobot/docs/source/pi05.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"
          },
          {
            "title": "PI0 Evaluation results on LIBERO is very low · Issue #952 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/952"
          },
          {
            "title": "lerobot/pi05_libero_finetuned · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned"
          },
          {
            "title": "lerobot/pi05_libero_finetuned_v044 · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned_v044"
          },
          {
            "title": "π₀.₅ (Pi05) Policy · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi05"
          }
        ]
      },
      "Based on the search results, here are the evaluation results for the `pi05_libero_finetuned` model:\n\n## Official Reported Success Rates\n\nAccording to the official LeRobot documentation, the π₀.₅ model achieves the following benchmark results on LIBERO tasks:\n- Libero Spatial: 98.8%\n- Libero Object: 98.2%\n- Libero Goal: 98.0%\n- Libero 10: 92.4%\n- Average: 96.85%\n\n## Known Issues with Reproduction\n\nHowever, there are documented discrepancies when attempting to reproduce these results. One GitHub issue reported observed success rates of: libero_spatial 77%, libero_object 66%, libero_goal 89%, libero_10 55%, with a total of 71.75%, which is significantly lower than the official reported rates.\n\nThe reported success rates for both models are about 10-20% higher than the observed ones, suggesting there may be configuration or environment setup differences between the official benchmarking and community reproduction attempts."
    ],
    "durationSeconds": 5.525625865999995
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-22T09:23:08.310Z_

<details><summary>↩ Tool result · `toolu_01L9AwQXZbscTb6Nx7nzMejM`</summary>

```text
Web search results for query: "site:github.com/huggingface/lerobot/issues/2114 pi0.5 LIBERO success rate replicate"

Links: [{"title":"Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2114"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/pdf/2510.13626"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://arxiv.org/pdf/2306.03310"},{"title":"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2511.15605"},{"title":"LeRobot: An Open-Source Library for End-to-End Robot Learning","url":"https://arxiv.org/pdf/2602.22818"},{"title":"MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation","url":"https://arxiv.org/pdf/2603.16861"}]

Based on the search results, I found the GitHub issue #2114 you were looking for. Here's what it contains:

The issue reports that π0 (pi0) models achieve lower success rates on LIBERO tasks (libero_spatial 69%, libero_object 72%, libero_goal 83%, libero_10 35%, overall 64.75%) compared to π0.5 (pi0.5) models (libero_spatial 77%, libero_object 66%, libero_goal 89%, libero_10 55%, total 71.75%).

The user reports that the reported success rates for both models are about 10-20% higher than what they observed when attempting to replicate the results using the specified evaluation commands. They asked whether there are any known issues or specific configurations needed for these models that might not be documented, and sought guidance on how to achieve the reported success rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "96f489a4-981e-4649-ae6f-25d3ccf2c8da",
  "tool_use_result": {
    "query": "site:github.com/huggingface/lerobot/issues/2114 pi0.5 LIBERO success rate replicate",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Bm7EKRPS8AJmr9DBFw2rxo",
        "content": [
          {
            "title": "Fine-tuned π0 and π0.5 models fail to replicate reported success rates on LIBERO benchmark · Issue #2114 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2114"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2510.13626"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://arxiv.org/pdf/2306.03310"
          },
          {
            "title": "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2511.15605"
          },
          {
            "title": "LeRobot: An Open-Source Library for End-to-End Robot Learning",
            "url": "https://arxiv.org/pdf/2602.22818"
          },
          {
            "title": "MolmoB0T: Large-Scale Simulation Enables Zero-Shot Manipulation",
            "url": "https://arxiv.org/pdf/2603.16861"
          }
        ]
      },
      "Based on the search results, I found the GitHub issue #2114 you were looking for. Here's what it contains:\n\nThe issue reports that π0 (pi0) models achieve lower success rates on LIBERO tasks (libero_spatial 69%, libero_object 72%, libero_goal 83%, libero_10 35%, overall 64.75%) compared to π0.5 (pi0.5) models (libero_spatial 77%, libero_object 66%, libero_goal 89%, libero_10 55%, total 71.75%).\n\nThe user reports that the reported success rates for both models are about 10-20% higher than what they observed when attempting to replicate the results using the specified evaluation commands. They asked whether there are any known issues or specific configurations needed for these models that might not be documented, and sought guidance on how to achieve the reported success rates."
    ],
    "durationSeconds": 5.972449584000001
  }
}
```

</details>

---

### Assistant

_source line 21_

<details><summary>Logged reasoning block</summary>

```text
Now let me get more details about the openpi LIBERO evaluation setup and the lerobot LIBERO documentation page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "59584112-49fb-42d6-8ce1-0d1c9df38670",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXBtXPV8g5L6Jtf2nbU4Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 810,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 26038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

继续查 openpi repo 的 LIBERO eval 具体实现和 lerobot 官方文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "828b4797-ccc7-40c8-abb9-1d18525a8231",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXBtXPV8g5L6Jtf2nbU4Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 810,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 26038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CFarDzmxdb91YzBFbxevqQ`</summary>

```json
{
  "query": "github Physical-Intelligence openpi examples libero evaluate.py README"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "97bea9f2-c606-4adb-bbc0-c8cc8a9dc217",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXBtXPV8g5L6Jtf2nbU4Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 810,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 26038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RC3Jrvd1K4KxNT3Y4HVekF`</summary>

```json
{
  "query": "huggingface lerobot docs libero evaluation command pi05 benchmark protocol"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "a49cb16f-2d62-4d23-a839-6abedb0e7b0d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXBtXPV8g5L6Jtf2nbU4Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 810,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 26038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012DHuTC9D4YY6PJpqpCg79L`</summary>

```json
{
  "query": "github huggingface lerobot-libero fork evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "3b3c1f5c-0e11-4bc7-b707-49edae1af470",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LXBtXPV8g5L6Jtf2nbU4Z1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 810,
      "cache_creation_input_tokens": 2532,
      "cache_read_input_tokens": 26038,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2532
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

_source line 26 · 2026-05-22T09:23:17.893Z_

<details><summary>↩ Tool result · `toolu_01CFarDzmxdb91YzBFbxevqQ`</summary>

```text
Web search results for query: "github Physical-Intelligence openpi examples libero evaluate.py README"

Links: [{"title":"openpi/examples/libero/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"openpi/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/README.md"},{"title":"openpi/examples/droid/README.md at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/examples/droid/README.md"},{"title":"GitHub - Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"},{"title":"openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"},{"title":"openpi/src/openpi/policies/libero_policy.py at main · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/policies/libero_policy.py"},{"title":"GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub","url":"https://github.com/Tonghe-Zhang/openpi-physical-intelligence"},{"title":"Trendshift - Ask AI","url":"https://trendshift.io/admin/repository/ask-ai/12902"}]

I found the relevant documentation! Here's what the search results show:

## Summary

The search results point to the LIBERO README in the openpi repository, which provides instructions for setting up a virtual environment, installing dependencies, and running simulations.

Key information about the LIBERO evaluation setup:

- To run the simulation, you use `python examples/libero/main.py`, with an optional `MUJOCO_GL=glx` environment variable if you encounter EGL errors

- The evaluation involves running a policy server in one terminal with `uv run scripts/serve_policy.py --env LIBERO`

- There is a pre-trained checkpoint available at `gs://openpi-assets/checkpoints/pi05_libero/` that was trained with the pi05_libero config

- You can customize the loaded checkpoint and task suite by providing additional SERVER_ARGS and CLIENT_ARGS parameters

The full README with detailed setup instructions is located at: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "07df7f94-2b92-4f15-95ba-8c5d37e41830",
  "tool_use_result": {
    "query": "github Physical-Intelligence openpi examples libero evaluate.py README",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XNxZhczGP62Boj511Ny6qf",
        "content": [
          {
            "title": "openpi/examples/libero/README.md at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md"
          },
          {
            "title": "GitHub - Physical-Intelligence/openpi · GitHub",
            "url": "https://github.com/Physical-Intelligence/openpi"
          },
          {
            "title": "openpi/README.md at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/README.md"
          },
          {
            "title": "openpi/examples/droid/README.md at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/examples/droid/README.md"
          },
          {
            "title": "GitHub - Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi?tab=readme-ov-file"
          },
          {
            "title": "openpi/src/openpi/training/config.py at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/training/config.py"
          },
          {
            "title": "https://raw.githubusercontent.com/Physical-Intelli...",
            "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"
          },
          {
            "title": "openpi/src/openpi/policies/libero_policy.py at main · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/blob/main/src/openpi/policies/libero_policy.py"
          },
          {
            "title": "GitHub - Tonghe-Zhang/openpi-physical-intelligence · GitHub",
            "url": "https://github.com/Tonghe-Zhang/openpi-physical-intelligence"
          },
          {
            "title": "Trendshift - Ask AI",
            "url": "https://trendshift.io/admin/repository/ask-ai/12902"
          }
        ]
      },
      "I found the relevant documentation! Here's what the search results show:\n\n## Summary\n\nThe search results point to the LIBERO README in the openpi repository, which provides instructions for setting up a virtual environment, installing dependencies, and running simulations.\n\nKey information about the LIBERO evaluation setup:\n\n- To run the simulation, you use `python examples/libero/main.py`, with an optional `MUJOCO_GL=glx` environment variable if you encounter EGL errors\n\n- The evaluation involves running a policy server in one terminal with `uv run scripts/serve_policy.py --env LIBERO`\n\n- There is a pre-trained checkpoint available at `gs://openpi-assets/checkpoints/pi05_libero/` that was trained with the pi05_libero config\n\n- You can customize the loaded checkpoint and task suite by providing additional SERVER_ARGS and CLIENT_ARGS parameters\n\nThe full README with detailed setup instructions is located at: https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md"
    ],
    "durationSeconds": 5.480733094000003
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-22T09:23:20.037Z_

<details><summary>↩ Tool result · `toolu_01RC3Jrvd1K4KxNT3Y4HVekF`</summary>

```text
Web search results for query: "huggingface lerobot docs libero evaluation command pi05 benchmark protocol"

Links: [{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"},{"title":"π₀.₅ (Pi05) Policy · Hugging Face","url":"https://huggingface.co/docs/lerobot/en/pi05"},{"title":"lerobot/docs/source/pi05.mdx at main · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"},{"title":"π₀-FAST (Pi0-FAST) · Hugging Face","url":"https://huggingface.co/docs/lerobot/pi0fast"},{"title":"lerobot/pi05_libero_finetuned · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned"},{"title":"LIBERO","url":"https://huggingface.co/docs/lerobot/main/en/libero"},{"title":"lerobot/pi05_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_base"},{"title":"lerobot/pi05_libero_finetuned_v044 · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_finetuned_v044"},{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"}]

I found comprehensive documentation about the HuggingFace LeRobot LIBERO evaluation command for the Pi0.5 benchmark. Here's what the search results show:

## Pi0.5 LIBERO Evaluation Command

To evaluate the finetuned pi05 model on LIBERO, you run: `lerobot-eval \ --output_dir=/logs/ \ --env.type=libero \ --env.task=libero_spatial,libero_object,libero_goal,libero_10 \ --eval.batch_size=1 \ --eval.n_episodes=10 \ --policy.path=pi05_libero_finetuned \ --policy.n_action_steps=10 \ --output_dir=./eval_logs/ \ --env.max_parallel_tasks=1`

## Benchmark Protocol Details

The Pi0.5 results are reproduced on the LIBERO benchmark using the LeRobot implementation by taking the Physical Intelligence LIBERO base model (pi05_libero) and finetuning for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.

The note states that n_action_steps=10 is set, similar to the original OpenPI implementation.

## Task Suites

LIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100. The first three task suites have controlled distribution shifts, while LIBERO-100 consists of 100 manipulation tasks that require the transfer of entangled knowledge.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "d09c709e-d683-4900-9060-e5b125b1cbcf",
  "tool_use_result": {
    "query": "huggingface lerobot docs libero evaluation command pi05 benchmark protocol",
    "results": [
      {
        "tool_use_id": "srvtoolu_0126DWxfWkZj1Ws3ko7nhvW7",
        "content": [
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "lerobot/pi05_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_base"
          },
          {
            "title": "π₀.₅ (Pi05) Policy · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/en/pi05"
          },
          {
            "title": "lerobot/docs/source/pi05.mdx at main · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/blob/main/docs/source/pi05.mdx"
          },
          {
            "title": "π₀-FAST (Pi0-FAST) · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/pi0fast"
          },
          {
            "title": "lerobot/pi05_libero_finetuned · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned"
          },
          {
            "title": "LIBERO",
            "url": "https://huggingface.co/docs/lerobot/main/en/libero"
          },
          {
            "title": "lerobot/pi05_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_base"
          },
          {
            "title": "lerobot/pi05_libero_finetuned_v044 · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_finetuned_v044"
          },
          {
            "title": "GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.",
            "url": "https://github.com/huggingface/lerobot-libero"
          }
        ]
      },
      "I found comprehensive documentation about the HuggingFace LeRobot LIBERO evaluation command for the Pi0.5 benchmark. Here's what the search results show:\n\n## Pi0.5 LIBERO Evaluation Command\n\nTo evaluate the finetuned pi05 model on LIBERO, you run: `lerobot-eval \\ --output_dir=/logs/ \\ --env.type=libero \\ --env.task=libero_spatial,libero_object,libero_goal,libero_10 \\ --eval.batch_size=1 \\ --eval.n_episodes=10 \\ --policy.path=pi05_libero_finetuned \\ --policy.n_action_steps=10 \\ --output_dir=./eval_logs/ \\ --env.max_parallel_tasks=1`\n\n## Benchmark Protocol Details\n\nThe Pi0.5 results are reproduced on the LIBERO benchmark using the LeRobot implementation by taking the Physical Intelligence LIBERO base model (pi05_libero) and finetuning for an additional 6k steps in bfloat16, with batch size of 256 on 8 H100 GPUs using the HuggingFace LIBERO dataset.\n\nThe note states that n_action_steps=10 is set, similar to the original OpenPI implementation.\n\n## Task Suites\n\nLIBERO provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100. The first three task suites have controlled distribution shifts, while LIBERO-100 consists of 100 manipulation tasks that require the transfer of entangled knowledge."
    ],
    "durationSeconds": 6.675787873000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-22T09:23:20.881Z_

<details><summary>↩ Tool result · `toolu_012DHuTC9D4YY6PJpqpCg79L`</summary>

```text
Web search results for query: "github huggingface lerobot-libero fork evaluation"

Links: [{"title":"GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.","url":"https://github.com/huggingface/lerobot-libero"},{"title":"GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning","url":"https://github.com/huggingface/lerobot"},{"title":"LIBERO-plus · Hugging Face","url":"https://huggingface.co/docs/lerobot/main/libero_plus"},{"title":"LIBERO · Hugging Face","url":"https://huggingface.co/docs/lerobot/libero"},{"title":"[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/1316"},{"title":"Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2294"},{"title":"Releases · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/releases"},{"title":"Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot","url":"https://github.com/huggingface/lerobot/issues/2375"},{"title":"lerobot-libero/LICENSE at main · huggingface/lerobot-libero","url":"https://github.com/huggingface/lerobot-libero/blob/main/LICENSE"},{"title":"lerobot/pi05_libero_base · Hugging Face","url":"https://huggingface.co/lerobot/pi05_libero_base"}]

I found comprehensive information about the GitHub Hugging Face LeRobot-LIBERO fork and its evaluation capabilities. Here's what I found:

## Overview

The lerobot-libero repository started as a fork of the official LIBERO benchmark and is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.

## LIBERO Benchmark

LIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. It provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.

## Evaluation Approach

By default, policies are evaluated on the fly during training, and if you have limited GPU computing resources, an evaluation script is offered to evaluate models separately.

The repository provides a dedicated evaluation script that can be run independently:

The evaluation command syntax is: `python libero/lifelong/evaluate.py --benchmark BENCHMARK_NAME --task_id TASK_ID --algo ALGO_NAME --policy POLICY_NAME --seed SEED --ep EPOCH --load_task LOAD_TASK --device_id CUDA_ID`

## Integration with LeRobot

LeRobot supports evaluating policies in simulation or on real hardware using a unified evaluation script and supports standard benchmarks like LIBERO.

The repository includes a GitHub page at https://github.com/huggingface/lerobot-libero where you can find more detailed documentation and examples for using the fork with evaluation capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "c09fc69d-865f-4713-b491-fffb112aec7d",
  "tool_use_result": {
    "query": "github huggingface lerobot-libero fork evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FY98qpaepmeLi4iMwUUodE",
        "content": [
          {
            "title": "GitHub - huggingface/lerobot-libero: A fork of the official LIBERO benchmark, extended for Hugging Face’s LeRobot integration and large-scale robotics experiments.",
            "url": "https://github.com/huggingface/lerobot-libero"
          },
          {
            "title": "GitHub - huggingface/lerobot: 🤗 LeRobot: Making AI for Robotics more accessible with end-to-end learning",
            "url": "https://github.com/huggingface/lerobot"
          },
          {
            "title": "LIBERO-plus · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/main/libero_plus"
          },
          {
            "title": "LIBERO · Hugging Face",
            "url": "https://huggingface.co/docs/lerobot/libero"
          },
          {
            "title": "[Question] SmolVLA LIBERO / MetaWorld evaluation · Issue #1316 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/1316"
          },
          {
            "title": "Question about the HuggingFaceVLA/smolvla_libero Model Configuration · Issue #2294 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2294"
          },
          {
            "title": "Releases · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/releases"
          },
          {
            "title": "Reproducing pi0.5 results on libero · Issue #2375 · huggingface/lerobot",
            "url": "https://github.com/huggingface/lerobot/issues/2375"
          },
          {
            "title": "lerobot-libero/LICENSE at main · huggingface/lerobot-libero",
            "url": "https://github.com/huggingface/lerobot-libero/blob/main/LICENSE"
          },
          {
            "title": "lerobot/pi05_libero_base · Hugging Face",
            "url": "https://huggingface.co/lerobot/pi05_libero_base"
          }
        ]
      },
      "I found comprehensive information about the GitHub Hugging Face LeRobot-LIBERO fork and its evaluation capabilities. Here's what I found:\n\n## Overview\n\nThe lerobot-libero repository started as a fork of the official LIBERO benchmark and is now maintained by the Hugging Face team, with modifications for compatibility with LeRobot, simplified installation, and large-scale robotics experiments.\n\n## LIBERO Benchmark\n\nLIBERO is designed for studying knowledge transfer in multitask and lifelong robot learning problems. It provides 130 tasks grouped into four task suites: LIBERO-Spatial, LIBERO-Object, LIBERO-Goal, and LIBERO-100.\n\n## Evaluation Approach\n\nBy default, policies are evaluated on the fly during training, and if you have limited GPU computing resources, an evaluation script is offered to evaluate models separately.\n\nThe repository provides a dedicated evaluation script that can be run independently:\n\nThe evaluation command syntax is: `python libero/lifelong/evaluate.py --benchmark BENCHMARK_NAME --task_id TASK_ID --algo ALGO_NAME --policy POLICY_NAME --seed SEED --ep EPOCH --load_task LOAD_TASK --device_id CUDA_ID`\n\n## Integration with LeRobot\n\nLeRobot supports evaluating policies in simulation or on real hardware using a unified evaluation script and supports standard benchmarks like LIBERO.\n\nThe repository includes a GitHub page at https://github.com/huggingface/lerobot-libero where you can find more detailed documentation and examples for using the fork with evaluation capabilities."
    ],
    "durationSeconds": 7.419939371000001
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Now let me get the actual openpi LIBERO eval script details and the official numbers from the lerobot docs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "ad370672-9f99-46c1-84fb-7bf334ad5512",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ad22gYDUumVnpyABZsovhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3769,
      "cache_read_input_tokens": 28570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3769
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

最后查一下 openpi 的官方 LIBERO 数字和 issue #734 的讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "614f0d5b-6088-4e91-8832-a074ecea4c4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ad22gYDUumVnpyABZsovhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3769,
      "cache_read_input_tokens": 28570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3769
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qt6nCZFAdkoi46k38p1N6i`</summary>

```json
{
  "query": "github Physical-Intelligence openpi issue 734 pi0.5 LIBERO-90 success rate finetuned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "c8f96c2a-3a35-4545-9556-4a212bb7251f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ad22gYDUumVnpyABZsovhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3769,
      "cache_read_input_tokens": 28570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3769
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EGqjXb2WQL7U6ZPaZrin4Y`</summary>

```json
{
  "query": "pi0.5 paper arxiv \"LIBERO\" official results table"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "cc4a642a-73f6-49d3-b4df-73683bdd8127",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ad22gYDUumVnpyABZsovhF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3769,
      "cache_read_input_tokens": 28570,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3769
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

_source line 33 · 2026-05-22T09:23:31.732Z_

<details><summary>↩ Tool result · `toolu_01EGqjXb2WQL7U6ZPaZrin4Y`</summary>

```text
Web search results for query: "pi0.5 paper arxiv "LIBERO" official results table"

Links: [{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark","url":"https://github.com/Zxy-MLlab/LIBERO-PRO"},{"title":"RLinf/RLinf-Pi05-LIBERO-SFT · Hugging Face","url":"https://huggingface.co/RLinf/RLinf-Pi05-LIBERO-SFT"},{"title":"[2505.03500] Task Reconstruction and Extrapolation for $π_0$ using Text Latent","url":"https://arxiv.org/abs/2505.03500"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization","url":"https://arxiv.org/abs/2504.16054"}]

Based on the search results, I found information about pi0.5 performance on LIBERO benchmarks. Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0.

The search results reference Table 2: Task-wise LIBERO and LIBERO-PRO performance of three VLA models on the libero-goal benchmark from the LIBERO-PRO paper. However, the specific numerical results table isn't fully displayed in the search results provided. 

The main papers found are:
1. **LIBERO-PRO** (arXiv 2510.03827) - evaluates pi0.5 under robustness perturbations
2. **π₀.₅: a Vision-Language-Action Model with Open-World Generalization** (arXiv 2504.16054) - the original pi0.5 paper

For the complete official results table from the pi0.5 paper, you may want to access the PDF directly from arxiv.org/abs/2504.16054, which appears to be the original pi0.5 paper on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "40c1814d-390d-4c88-b15c-23b24b221c45",
  "tool_use_result": {
    "query": "pi0.5 paper arxiv \"LIBERO\" official results table",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BDq91vGX1LDcewhJFzpmGv",
        "content": [
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "GitHub - Zxy-MLlab/LIBERO-PRO: LIBERO-PRO is the official repository of the LIBERO-PRO — an evaluation extension of the original LIBERO benchmark",
            "url": "https://github.com/Zxy-MLlab/LIBERO-PRO"
          },
          {
            "title": "RLinf/RLinf-Pi05-LIBERO-SFT · Hugging Face",
            "url": "https://huggingface.co/RLinf/RLinf-Pi05-LIBERO-SFT"
          },
          {
            "title": "[2505.03500] Task Reconstruction and Extrapolation for $π_0$ using Text Latent",
            "url": "https://arxiv.org/abs/2505.03500"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "[2504.16054] $π_{0.5}$: a Vision-Language-Action Model with Open-World Generalization",
            "url": "https://arxiv.org/abs/2504.16054"
          }
        ]
      },
      "Based on the search results, I found information about pi0.5 performance on LIBERO benchmarks. Pi0.5 achieves a 0.38 success rate in the libero-goal task under position changes, compared to 0 for OpenVLA and Pi0.\n\nThe search results reference Table 2: Task-wise LIBERO and LIBERO-PRO performance of three VLA models on the libero-goal benchmark from the LIBERO-PRO paper. However, the specific numerical results table isn't fully displayed in the search results provided. \n\nThe main papers found are:\n1. **LIBERO-PRO** (arXiv 2510.03827) - evaluates pi0.5 under robustness perturbations\n2. **π₀.₅: a Vision-Language-Action Model with Open-World Generalization** (arXiv 2504.16054) - the original pi0.5 paper\n\nFor the complete official results table from the pi0.5 paper, you may want to access the PDF directly from arxiv.org/abs/2504.16054, which appears to be the original pi0.5 paper on arXiv."
    ],
    "durationSeconds": 5.605271372999996
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T09:23:32.325Z_

<details><summary>↩ Tool result · `toolu_01Qt6nCZFAdkoi46k38p1N6i`</summary>

```text
Web search results for query: "github Physical-Intelligence openpi issue 734 pi0.5 LIBERO-90 success rate finetuned"

Links: [{"title":"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/734"},{"title":"PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/711"},{"title":"GitHub - Physical-Intelligence/openpi · GitHub","url":"https://github.com/Physical-Intelligence/openpi"},{"title":"Poor training performance (3.3% success rate) with pi0 model on locally downloaded official LIBERO dataset · Issue #804 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/804"},{"title":"How to finetune torch-based pi0.5 with libero dataset? · Issue #743 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/743"},{"title":"question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues/672"},{"title":"https://raw.githubusercontent.com/Physical-Intelli...","url":"https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"},{"title":"Issues · Physical-Intelligence/openpi","url":"https://github.com/Physical-Intelligence/openpi/issues"},{"title":"Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success","url":"https://arxiv.org/pdf/2502.19645"}]

Based on the search results, I found information about Issue #734 from the Physical-Intelligence/openpi repository.

The issue, opened on October 20, 2025, asks "Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%?" The issue mentions success rates for other LIBERO task suites: libero_spatial at 97.4%, libero_object at 98.4%, libero_goal at 97.6%, and libero_10 at 93.0%.

The issue specifically raises a concern about the surprisingly low 18% success rate on LIBERO-90 compared to the much higher success rates on the individual LIBERO task suites (spatial, object, goal) when using a finetuned PI0.5 model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "c19808e9-ec87-4a86-bc3e-2e5d35ca8d59",
  "tool_use_result": {
    "query": "github Physical-Intelligence openpi issue 734 pi0.5 LIBERO-90 success rate finetuned",
    "results": [
      {
        "tool_use_id": "srvtoolu_019PkqFuyhuZ1Qz6aAhS5iWP",
        "content": [
          {
            "title": "Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%? · Issue #734 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/734"
          },
          {
            "title": "PI05 lora fine-tune on libero dataset & differences about the norm_stats · Issue #711 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/711"
          },
          {
            "title": "GitHub - Physical-Intelligence/openpi · GitHub",
            "url": "https://github.com/Physical-Intelligence/openpi"
          },
          {
            "title": "Poor training performance (3.3% success rate) with pi0 model on locally downloaded official LIBERO dataset · Issue #804 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/804"
          },
          {
            "title": "How to finetune torch-based pi0.5 with libero dataset? · Issue #743 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/743"
          },
          {
            "title": "question about lora fine-tuning for pi0.5 · Issue #672 · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues/672"
          },
          {
            "title": "https://raw.githubusercontent.com/Physical-Intelli...",
            "url": "https://raw.githubusercontent.com/Physical-Intelligence/openpi/main/src/openpi/training/config.py"
          },
          {
            "title": "Issues · Physical-Intelligence/openpi",
            "url": "https://github.com/Physical-Intelligence/openpi/issues"
          },
          {
            "title": "Fine-Tuning Vision-Language-Action Models: Optimizing Speed and Success",
            "url": "https://arxiv.org/pdf/2502.19645"
          }
        ]
      },
      "Based on the search results, I found information about Issue #734 from the Physical-Intelligence/openpi repository.\n\nThe issue, opened on October 20, 2025, asks \"Is PI0.5 finetuned by all LIBERO datasets? Success rate of LIBERO-90 is only 18%?\" The issue mentions success rates for other LIBERO task suites: libero_spatial at 97.4%, libero_object at 98.4%, libero_goal at 97.6%, and libero_10 at 93.0%.\n\nThe issue specifically raises a concern about the surprisingly low 18% success rate on LIBERO-90 compared to the much higher success rates on the individual LIBERO task suites (spatial, object, goal) when using a finetuned PI0.5 model."
    ],
    "durationSeconds": 6.609036312999997
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile a comprehensive report. Let me summarize:

1. **π0.5 官方 repo / 发布渠道**:
   - OpenPI: https://github.com/Physical-Intelligence/openpi
   - lerobot HuggingFace: models at lerobot/pi05_libero_base, lerobot/pi05_libero_finetuned, lerobot/pi05_libero_finetuned_v044
   - Paper: arXiv 2504.16054

2. **是否有 LIBERO eval 脚本**: YES — 两个渠道都有
   - OpenPI repo 提供了 `examples/libero/main.py` 和 serve_policy.py 的评估方式，而 lerobot 则通过 `lerobot-eval` 命令行工具来运行评估

3. **官方/社区 LIBERO SR 数字**: 两个版本的性能都很接近，OpenPI finetuned 在 libero_spatial 达到 97.4%、libero_object 98.4%、libero_goal 97.6%、libero_10 93.0%，而 lerobot finetuned 则分别为 98.8%、98.2%、98.0% 和 92.4%

但社区的复现结果差异很大，issue #2114 报告的数字是 libero_spatial 77%、libero_object 66%、libero_goal 89%、libero_10 55%，远低于官方声称的水平，issue #2533 甚至在 base model 上得到了零成功率。我们自己的评估结果（Object 81.5%、Spatial 84.2% on VLA-only）也接近社区复现的水平，这表明官方数字可能是基于特定的 finetuned checkpoint，而 base model 的性能本身就较低，加上不同环境配置的差异，都可能导致这种性能差异。现在我需要把这些发现整理成一份报告并保存到 artifact 中。
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "cf78c92f-dac8-4ca4-bfb9-e56f6065e117",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EznUQNprs4TjGCS1utTYJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 32339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
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

_source line 36_

调研完成。以下是完整结果。

---

## π0.5 LIBERO 评估调研报告

### 1. π0.5 官方 repo / 发布渠道

| 渠道 | 链接 |
|------|------|
| OpenPI (Physical Intelligence 官方) | [github.com/Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |
| lerobot HuggingFace 模型 (base) | [lerobot/pi05_libero_base](https://huggingface.co/lerobot/pi05_libero_base) |
| lerobot HuggingFace 模型 (finetuned) | [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned) |
| lerobot LIBERO fork | [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) |
| π0.5 论文 | [arXiv 2504.16054](https://arxiv.org/abs/2504.16054) |

### 2. LIBERO eval 脚本：**Yes，两套**

**方案 A — OpenPI 官方（server-client 架构）**

位于 [`examples/libero/`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)：

```bash
# Terminal 1: 启动 policy server
uv run scripts/serve_policy.py --env LIBERO

# Terminal 2: 运行 LIBERO eval
MUJOCO_GL=glx python examples/libero/main.py
```

预训练 checkpoint: `gs://openpi-assets/checkpoints/pi05_libero/`

**方案 B — lerobot 统一 eval（推荐，更简洁）**

```bash
lerobot-eval \
  --policy.path=lerobot/pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1 \
  --output_dir=./eval_logs/
```

标准 benchmark protocol: 每 task 10 episodes，4 个 suite 共 400 episodes。

### 3. 官方与社区报告的 LIBERO SR 数字

| 来源 | Spatial | Object | Goal | Long (10) | 备注 |
|------|---------|--------|------|-----------|------|
| **OpenPI 官方 finetuned** | 97.4% | 98.4% | 97.6% | 93.0% | [issue #734](https://github.com/Physical-Intelligence/openpi/issues/734) |
| **lerobot 官方 finetuned** | 98.8% | 98.2% | 98.0% | 92.4% | [lerobot docs](https://huggingface.co/docs/lerobot/pi05) |
| 社区复现 (issue #2114) | 77% | 66% | 89% | 55% | finetuned model, 远低于官方 |
| 社区复现 (issue #2533) | 0% | — | — | — | base model, 完全失败 |
| **我们的数字 (VLA-only)** | **84.2%** | **81.5%** | — | — | 与社区复现数量级一致 |

### 4. 关键发现与分析

**官方数字 vs 社区复现存在巨大差距（20-30%）**，这是已知问题：

- [lerobot issue #2114](https://github.com/huggingface/lerobot/issues/2114): "Fine-tuned π0 and π0.5 models fail to replicate reported success rates"
- [lerobot issue #2533](https://github.com/huggingface/lerobot/issues/2533): base model 零成功率
- [lerobot issue #2375](https://github.com/huggingface/lerobot/issues/2375): "Reproducing pi0.5 results on libero"

差距可能来源于：
- lerobot 的 finetuned checkpoint 是在 8×H100 上额外训练 6k steps 得到的特定版本
- 评估时的 action chunking 配置 (`n_action_steps=10`) 对结果敏感
- 环境版本和渲染后端差异
- LIBERO-PRO 论文 ([arXiv 2510.03827](https://arxiv.org/abs/2510.03827)) 直接指出官方数字反映的是 "rote recall rather than genuine task understanding"

### 5. 对我们论文的影响

**我们的数字（81.5% Object, 84.2% Spatial）是合理的**，与社区独立复现的数量级一致。论文中建议：

1. **引用 lerobot issue #2114** 作为复现困难的证据
2. **报告我们自己的 baseline** 而非抄官方数字，注明使用 `evaluate.py` 独立评估
3. **核心论点不变**：无论 VLA-only baseline 是 80% 还是 98%，conformal refinement 的增量改进都是有效的（因为是同 pipeline 对比）
4. 可以补充一句："Our VLA-only baselines are consistent with community reproduction results (lerobot issue #2114), which are 20-30% lower than the originally reported numbers."

### 6. lerobot 对 LIBERO 的支持情况

- **完整支持**：lerobot 原生集成 LIBERO，提供 `lerobot-eval` 统一评估命令
- **HuggingFace fork**：[huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) 是 LIBERO 的官方 fork，简化了安装
- **支持的 suite**：libero_spatial, libero_object, libero_goal, libero_10 (即 LIBERO-Long)
- **支持的模型**：pi0, pi0.5, pi0-FAST, SmolVLA 等均可通过 `--policy.path` 指定

Sources:
- [OpenPI GitHub](https://github.com/Physical-Intelligence/openpi)
- [OpenPI LIBERO README](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)
- [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- [lerobot π0.5 docs](https://huggingface.co/docs/lerobot/pi05)
- [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [Issue #2114 - fail to replicate](https://github.com/huggingface/lerobot/issues/2114)
- [Issue #2533 - zero success rate](https://github.com/huggingface/lerobot/issues/2533)
- [Issue #734 - LIBERO-90 18%](https://github.com/Physical-Intelligence/openpi/issues/734)
- [LIBERO-PRO paper](https://arxiv.org/abs/2510.03827)
- [π0.5 paper](https://arxiv.org/abs/2504.16054)
- [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "uuid": "b0434c22-be22-45b6-a0ca-1b374f6d53d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EznUQNprs4TjGCS1utTYJy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 709,
      "cache_creation_input_tokens": 907,
      "cache_read_input_tokens": 32339,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 907
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

_source line 37_

调研完成。以下是完整结果。

---

## π0.5 LIBERO 评估调研报告

### 1. π0.5 官方 repo / 发布渠道

| 渠道 | 链接 |
|------|------|
| OpenPI (Physical Intelligence 官方) | [github.com/Physical-Intelligence/openpi](https://github.com/Physical-Intelligence/openpi) |
| lerobot HuggingFace 模型 (base) | [lerobot/pi05_libero_base](https://huggingface.co/lerobot/pi05_libero_base) |
| lerobot HuggingFace 模型 (finetuned) | [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned) |
| lerobot LIBERO fork | [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) |
| π0.5 论文 | [arXiv 2504.16054](https://arxiv.org/abs/2504.16054) |

### 2. LIBERO eval 脚本：**Yes，两套**

**方案 A — OpenPI 官方（server-client 架构）**

位于 [`examples/libero/`](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)：

```bash
# Terminal 1: 启动 policy server
uv run scripts/serve_policy.py --env LIBERO

# Terminal 2: 运行 LIBERO eval
MUJOCO_GL=glx python examples/libero/main.py
```

预训练 checkpoint: `gs://openpi-assets/checkpoints/pi05_libero/`

**方案 B — lerobot 统一 eval（推荐，更简洁）**

```bash
lerobot-eval \
  --policy.path=lerobot/pi05_libero_finetuned \
  --policy.n_action_steps=10 \
  --env.type=libero \
  --env.task=libero_spatial,libero_object,libero_goal,libero_10 \
  --eval.batch_size=1 \
  --eval.n_episodes=10 \
  --env.max_parallel_tasks=1 \
  --output_dir=./eval_logs/
```

标准 benchmark protocol: 每 task 10 episodes，4 个 suite 共 400 episodes。

### 3. 官方与社区报告的 LIBERO SR 数字

| 来源 | Spatial | Object | Goal | Long (10) | 备注 |
|------|---------|--------|------|-----------|------|
| **OpenPI 官方 finetuned** | 97.4% | 98.4% | 97.6% | 93.0% | [issue #734](https://github.com/Physical-Intelligence/openpi/issues/734) |
| **lerobot 官方 finetuned** | 98.8% | 98.2% | 98.0% | 92.4% | [lerobot docs](https://huggingface.co/docs/lerobot/pi05) |
| 社区复现 (issue #2114) | 77% | 66% | 89% | 55% | finetuned model, 远低于官方 |
| 社区复现 (issue #2533) | 0% | — | — | — | base model, 完全失败 |
| **我们的数字 (VLA-only)** | **84.2%** | **81.5%** | — | — | 与社区复现数量级一致 |

### 4. 关键发现与分析

**官方数字 vs 社区复现存在巨大差距（20-30%）**，这是已知问题：

- [lerobot issue #2114](https://github.com/huggingface/lerobot/issues/2114): "Fine-tuned π0 and π0.5 models fail to replicate reported success rates"
- [lerobot issue #2533](https://github.com/huggingface/lerobot/issues/2533): base model 零成功率
- [lerobot issue #2375](https://github.com/huggingface/lerobot/issues/2375): "Reproducing pi0.5 results on libero"

差距可能来源于：
- lerobot 的 finetuned checkpoint 是在 8×H100 上额外训练 6k steps 得到的特定版本
- 评估时的 action chunking 配置 (`n_action_steps=10`) 对结果敏感
- 环境版本和渲染后端差异
- LIBERO-PRO 论文 ([arXiv 2510.03827](https://arxiv.org/abs/2510.03827)) 直接指出官方数字反映的是 "rote recall rather than genuine task understanding"

### 5. 对我们论文的影响

**我们的数字（81.5% Object, 84.2% Spatial）是合理的**，与社区独立复现的数量级一致。论文中建议：

1. **引用 lerobot issue #2114** 作为复现困难的证据
2. **报告我们自己的 baseline** 而非抄官方数字，注明使用 `evaluate.py` 独立评估
3. **核心论点不变**：无论 VLA-only baseline 是 80% 还是 98%，conformal refinement 的增量改进都是有效的（因为是同 pipeline 对比）
4. 可以补充一句："Our VLA-only baselines are consistent with community reproduction results (lerobot issue #2114), which are 20-30% lower than the originally reported numbers."

### 6. lerobot 对 LIBERO 的支持情况

- **完整支持**：lerobot 原生集成 LIBERO，提供 `lerobot-eval` 统一评估命令
- **HuggingFace fork**：[huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero) 是 LIBERO 的官方 fork，简化了安装
- **支持的 suite**：libero_spatial, libero_object, libero_goal, libero_10 (即 LIBERO-Long)
- **支持的模型**：pi0, pi0.5, pi0-FAST, SmolVLA 等均可通过 `--policy.path` 指定

Sources:
- [OpenPI GitHub](https://github.com/Physical-Intelligence/openpi)
- [OpenPI LIBERO README](https://github.com/Physical-Intelligence/openpi/blob/main/examples/libero/README.md)
- [lerobot LIBERO docs](https://huggingface.co/docs/lerobot/libero)
- [lerobot π0.5 docs](https://huggingface.co/docs/lerobot/pi05)
- [lerobot/pi05_libero_finetuned](https://huggingface.co/lerobot/pi05_libero_finetuned)
- [Issue #2114 - fail to replicate](https://github.com/huggingface/lerobot/issues/2114)
- [Issue #2533 - zero success rate](https://github.com/huggingface/lerobot/issues/2533)
- [Issue #734 - LIBERO-90 18%](https://github.com/Physical-Intelligence/openpi/issues/734)
- [LIBERO-PRO paper](https://arxiv.org/abs/2510.03827)
- [π0.5 paper](https://arxiv.org/abs/2504.16054)
- [huggingface/lerobot-libero](https://github.com/huggingface/lerobot-libero)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 117873,
  "duration_api_ms": 163777,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "f8c93318-d4f2-4174-b1f6-0d6baebb4234",
  "total_cost_usd": 0.58521775,
  "usage": {
    "input_tokens": 2493,
    "cache_creation_input_tokens": 21405,
    "cache_read_input_tokens": 146333,
    "output_tokens": 3711,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21405,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 709,
        "output_tokens": 2646,
        "cache_read_input_tokens": 32339,
        "cache_creation_input_tokens": 907,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 907
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 140200,
      "outputTokens": 4566,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 11,
      "costUSD": 0.27303,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2493,
      "outputTokens": 3711,
      "cacheReadInputTokens": 146333,
      "cacheCreationInputTokens": 21405,
      "webSearchRequests": 0,
      "costUSD": 0.31218775,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "85193180-9bbe-4679-a1b0-500d4613b5f5"
}
```

</details>

---
