# research backup plan expert sft

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 0
- **Tool calls:** 11
- **Original source:** `logs/workers/worker_research_backup-plan-expert-sft_20260514T081623.log`
- **Structured JSON:** [`40993e1ce2cc83f3c099.json`](../../sessions/40/40993e1ce2cc83f3c099.json)

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
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
  "uuid": "57de5205-0e8f-4f91-9801-bfb80e392a47",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "status": "allowed_warning",
    "resetsAt": 1778821200,
    "rateLimitType": "seven_day",
    "utilization": 0.95,
    "isUsingOverage": false,
    "surpassedThreshold": 0.75
  },
  "uuid": "fbb254e9-c348-4814-9925-c097486f014a",
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275"
}
```

---

### Assistant

_source line 4_

我来调研 Expert Trajectory SFT 作为 GRPO 冷启动的 backup plan。先并行搜索文献和数据源。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "e5693dfb-2537-45ab-9f6f-477f3e2f09b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUZdXKLC9oF4Ebnp3vdgxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11735,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11735
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01Xp5pvJAcuP4j9evc3Nwx97`</summary>

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
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "b6e3d685-ac7b-4471-b183-27f5a65ce3f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KUZdXKLC9oF4Ebnp3vdgxE",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11735,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11735
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

_source line 6 · 2026-05-14T08:16:33.689Z_

<details><summary>↩ Tool result · `toolu_01Xp5pvJAcuP4j9evc3Nwx97`</summary>

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
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "087a5505-4991-449b-9d0b-444bc8262692",
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
Now let me launch parallel web searches to gather information on all the relevant topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "792810f1-86a8-4e37-ac1f-9200a9434889",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNepopqCPai7G1dtd5n4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Vr9JKizaTA327B6aDpZu2Y`</summary>

```json
{
  "query": "expert trajectory SFT warm start RL cold start demonstrations language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "7f554dcd-455f-452e-bcab-a01ae3c4a723",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNepopqCPai7G1dtd5n4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DPubBW9jYg9UVpmKdMrKrv`</summary>

```json
{
  "query": "ALFWorld expert trajectory imitation learning success rate"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "4fecc11e-7eda-4c65-ac0f-7891c966b098",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNepopqCPai7G1dtd5n4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HghAsu5P88rr1kLiFJW1Va`</summary>

```json
{
  "query": "ALFWorld walkthrough expert solution data SFT dataset"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "b702c53d-526d-4edc-b840-89368079e401",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNepopqCPai7G1dtd5n4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_018Ptw6EshNwEycmQ3yi3yPm`</summary>

```json
{
  "query": "sparse reward RL text games demonstrations curriculum learning overcome collapse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "1720c6bf-6217-44a9-b598-ea3221e37c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FyNepopqCPai7G1dtd5n4B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 647,
      "cache_read_input_tokens": 23576,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 647
      },
      "output_tokens": 20,
      "service_tier": "standard",
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

_source line 12 · 2026-05-14T08:16:43.982Z_

<details><summary>↩ Tool result · `toolu_01HghAsu5P88rr1kLiFJW1Va`</summary>

```text
Web search results for query: "ALFWorld walkthrough expert solution data SFT dataset"

Links: [{"title":"u-10bei/sft_alfworld_trajectory_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v2"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v3 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v3"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v4 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v4"},{"title":"GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub","url":"https://github.com/stevenyangyj/Emma-Alfworld"},{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"zjunlp/WKM-mistral-alfworld · Hugging Face","url":"https://huggingface.co/zjunlp/WKM-mistral-alfworld"},{"title":"alfworld: aligning text and embodied environments for ...","url":"https://arxiv.org/pdf/2010.03768"}]

Based on the search results, here's information about ALFWorld walkthrough expert solution data and SFT datasets:

## SFT Dataset Overview

There are synthetic SFT (Supervised Fine-Tuning) datasets designed for agent training in ALFWorld-compatible environments that programmatically generate expert trajectories without requiring an actual ALFWorld environment or a large language model.

## Dataset Characteristics

These datasets feature several key components:

- Template-based Simulation: Lightweight simulator based on published ALFWorld information (papers, ReAct prompt examples).
- Subgoal Decomposition: Rule-based expert system supporting 6 task types.
- Observation & Thought Diversity: Various templates for diversifying observation and thought texts.
- Multiple Formats: Supports both function-calling and ReAct formats.

## Available Versions

Multiple versions of these SFT trajectory datasets are available on Hugging Face (versions 1-5), with the datasets being a collection of datasets created to improve AgentBench scores.

## Expert Trajectories in Original ALFWorld

For the original ALFWorld framework, a rule-based expert for supervision is used, where a given task is decomposed into sequence of subgoals (e.g., for heat & place: find the object, pick the object, find the microwave, heat the object with the microwave, find the receptacle, place the object in the receptacle).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "d0498dd8-45e4-48ae-8b57-b444164471e5",
  "tool_use_result": {
    "query": "ALFWorld walkthrough expert solution data SFT dataset",
    "results": [
      {
        "tool_use_id": "srvtoolu_016uGDddregHHvciKoMfqbux",
        "content": [
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v2 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v2"
          },
          {
            "title": "ALFWorld",
            "url": "https://alfworld.github.io/"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v3 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v3"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v5 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v4 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v4"
          },
          {
            "title": "GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub",
            "url": "https://github.com/stevenyangyj/Emma-Alfworld"
          },
          {
            "title": "GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub",
            "url": "https://github.com/alfworld/alfworld"
          },
          {
            "title": "zjunlp/WKM-mistral-alfworld · Hugging Face",
            "url": "https://huggingface.co/zjunlp/WKM-mistral-alfworld"
          },
          {
            "title": "alfworld: aligning text and embodied environments for ...",
            "url": "https://arxiv.org/pdf/2010.03768"
          }
        ]
      },
      "Based on the search results, here's information about ALFWorld walkthrough expert solution data and SFT datasets:\n\n## SFT Dataset Overview\n\nThere are synthetic SFT (Supervised Fine-Tuning) datasets designed for agent training in ALFWorld-compatible environments that programmatically generate expert trajectories without requiring an actual ALFWorld environment or a large language model.\n\n## Dataset Characteristics\n\nThese datasets feature several key components:\n\n- Template-based Simulation: Lightweight simulator based on published ALFWorld information (papers, ReAct prompt examples).\n- Subgoal Decomposition: Rule-based expert system supporting 6 task types.\n- Observation & Thought Diversity: Various templates for diversifying observation and thought texts.\n- Multiple Formats: Supports both function-calling and ReAct formats.\n\n## Available Versions\n\nMultiple versions of these SFT trajectory datasets are available on Hugging Face (versions 1-5), with the datasets being a collection of datasets created to improve AgentBench scores.\n\n## Expert Trajectories in Original ALFWorld\n\nFor the original ALFWorld framework, a rule-based expert for supervision is used, where a given task is decomposed into sequence of subgoals (e.g., for heat & place: find the object, pick the object, find the microwave, heat the object with the microwave, find the receptacle, place the object in the receptacle)."
    ],
    "durationSeconds": 6.321545847000001
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T08:16:44.821Z_

<details><summary>↩ Tool result · `toolu_01DPubBW9jYg9UVpmKdMrKrv`</summary>

```text
Web search results for query: "ALFWorld expert trajectory imitation learning success rate"

Links: [{"title":"Language Models are Few-Shot Butlers","url":"https://aclanthology.org/2021.emnlp-main.734.pdf"},{"title":"alfworld: aligning text and embodied environments for ...","url":"https://arxiv.org/pdf/2010.03768"},{"title":"Prospector: Improving LLM Agents with Self-Asking and ...","url":"https://aclanthology.org/2024.findings-emnlp.879.pdf"},{"title":"ALFWORLD: ALIGNING TEXT AND EMBODIED ...","url":"https://openreview.net/pdf?id=0IOX0YcCdTn"},{"title":"Exploration-Based Trajectory Optimization for LLM Agents 3⃣","url":"https://aclanthology.org/2024.acl-long.409.pdf"},{"title":"ALFWorld Benchmark","url":"https://www.emergentmind.com/topics/alfworld-benchmark"},{"title":"Tackling AlfWorld with Action Attention and Common Sense from Pretrained LMs","url":"https://openreview.net/pdf?id=AqkPRUZ-YkO"},{"title":"Language Agent Meets Offline Reinforcement Learning Critic","url":"https://aclanthology.org/2024.emnlp-main.268.pdf"},{"title":"Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld","url":"https://arxiv.org/html/2311.16714"},{"title":"Learning Hierarchical Procedural Memory for LLM Agents ...","url":"https://arxiv.org/pdf/2512.18950"}]

Based on the search results, I found information about ALFWorld and expert trajectory imitation learning success rates:

## Key Findings:

Training in ALFWorld leverages imitation learning paradigms where trajectories are supervised by a rule-based or scripted expert, enabling the agent to mimic correct behaviors, both in the symbolic and embodied domains.

### Success Rate Results:

Several approaches have reported impressive success rates on ALFWorld using expert trajectories and imitation learning:

- InterAct, integrating role-specialized ChatGPT modules, achieves an average 98% success rate on six representative ALFWorld tasks, outperforming single-policy ReAct-style baselines by 25%.

- ReSpAct, harmonizing reasoning, action, and context-driven dialogue, outperforms ReAct by an absolute 6% on ALFWorld, reducing invalid action frequency from 13% to 3%.

- MACLA achieves 82% success using only the first 1,425 trajectories (50% of training data) without any parameter training.

- One approach achieved a significantly higher success rate (absolute 50% over the baseline) with a novel object masking - action attention method.

### Training Efficiency:

Training first in the abstract text-based environment is not only 7× faster, but also yields better performance than training from scratch in the embodied world.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "c660e119-f18e-4b32-8f45-ce916f9f393d",
  "tool_use_result": {
    "query": "ALFWorld expert trajectory imitation learning success rate",
    "results": [
      {
        "tool_use_id": "srvtoolu_016DNYLWqbmgo1fTNupUiXEP",
        "content": [
          {
            "title": "Language Models are Few-Shot Butlers",
            "url": "https://aclanthology.org/2021.emnlp-main.734.pdf"
          },
          {
            "title": "alfworld: aligning text and embodied environments for ...",
            "url": "https://arxiv.org/pdf/2010.03768"
          },
          {
            "title": "Prospector: Improving LLM Agents with Self-Asking and ...",
            "url": "https://aclanthology.org/2024.findings-emnlp.879.pdf"
          },
          {
            "title": "ALFWORLD: ALIGNING TEXT AND EMBODIED ...",
            "url": "https://openreview.net/pdf?id=0IOX0YcCdTn"
          },
          {
            "title": "Exploration-Based Trajectory Optimization for LLM Agents 3⃣",
            "url": "https://aclanthology.org/2024.acl-long.409.pdf"
          },
          {
            "title": "ALFWorld Benchmark",
            "url": "https://www.emergentmind.com/topics/alfworld-benchmark"
          },
          {
            "title": "Tackling AlfWorld with Action Attention and Common Sense from Pretrained LMs",
            "url": "https://openreview.net/pdf?id=AqkPRUZ-YkO"
          },
          {
            "title": "Language Agent Meets Offline Reinforcement Learning Critic",
            "url": "https://aclanthology.org/2024.emnlp-main.268.pdf"
          },
          {
            "title": "Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld",
            "url": "https://arxiv.org/html/2311.16714"
          },
          {
            "title": "Learning Hierarchical Procedural Memory for LLM Agents ...",
            "url": "https://arxiv.org/pdf/2512.18950"
          }
        ]
      },
      "Based on the search results, I found information about ALFWorld and expert trajectory imitation learning success rates:\n\n## Key Findings:\n\nTraining in ALFWorld leverages imitation learning paradigms where trajectories are supervised by a rule-based or scripted expert, enabling the agent to mimic correct behaviors, both in the symbolic and embodied domains.\n\n### Success Rate Results:\n\nSeveral approaches have reported impressive success rates on ALFWorld using expert trajectories and imitation learning:\n\n- InterAct, integrating role-specialized ChatGPT modules, achieves an average 98% success rate on six representative ALFWorld tasks, outperforming single-policy ReAct-style baselines by 25%.\n\n- ReSpAct, harmonizing reasoning, action, and context-driven dialogue, outperforms ReAct by an absolute 6% on ALFWorld, reducing invalid action frequency from 13% to 3%.\n\n- MACLA achieves 82% success using only the first 1,425 trajectories (50% of training data) without any parameter training.\n\n- One approach achieved a significantly higher success rate (absolute 50% over the baseline) with a novel object masking - action attention method.\n\n### Training Efficiency:\n\nTraining first in the abstract text-based environment is not only 7× faster, but also yields better performance than training from scratch in the embodied world."
    ],
    "durationSeconds": 7.461952006999998
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T08:16:45.662Z_

<details><summary>↩ Tool result · `toolu_01Vr9JKizaTA327B6aDpZu2Y`</summary>

```text
Web search results for query: "expert trajectory SFT warm start RL cold start demonstrations language model"

Links: [{"title":"From Expert Trajectories to Step-wise Reasoning","url":"https://arxiv.org/pdf/2510.25992"},{"title":"Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning","url":"https://arxiv.org/pdf/2509.06948"},{"title":"How Much Backtracking is Enough? Exploring the Interplay of SFT and RL in Enhancing LLM Reasoning","url":"https://arxiv.org/html/2505.24273v1"},{"title":"Rethinking Expert Trajectory Utilization in LLM Post-training","url":"https://arxiv.org/html/2512.11470v1"},{"title":"SuperRL: Reinforcement Learning with Supervision to Boost Language Model Reasoning","url":"https://arxiv.org/html/2506.01096"},{"title":"Harmonizing Supervised Fine-Tuning and Reinforcement ...","url":"https://arxiv.org/pdf/2508.11408"},{"title":"[2512.11470] Rethinking Expert Trajectory Utilization in LLM Post-training","url":"https://arxiv.org/abs/2512.11470"},{"title":"BREAD: Branched Rollouts from Expert Anchors Bridge SFT & RL for Reasoning","url":"https://arxiv.org/html/2506.17211v1"},{"title":"Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning","url":"https://arxiv.org/html/2510.25992v1"},{"title":"GitHub - waltonfuture/RL-with-Cold-Start: SFT+RL boosts multimodal reasoning","url":"https://github.com/waltonfuture/RL-with-Cold-Start"}]

Based on the search results, here's what I found about expert trajectory SFT warm start RL cold start demonstrations and language models:

## Key Concepts

The two-stage approach, often referred to as "cold start," ensures that the model first learns to imitate expert reasoning patterns, providing a strong initialization for subsequent RL training.

## Main Approaches and Findings

**Sequential SFT-then-RL Pipeline**: The Sequential SFT-then-RL pipeline is established as the superior standard, overcoming the stability deficits of synchronized approaches.

**Challenges with Traditional Cold Start**: Cold-start begins with extremely long responses due to SFT warm-up, causing slow training, followed by a sharp decline and gradual recovery. This "dip-then-rise" pattern indicates the model initially loses expert behavior acquired during SFT, then slowly explores new strategies.

**Alternative Approaches**: Researchers have developed various methods to improve upon traditional cold-start training:

1. SuperRL proposes a unified training framework that dynamically switches between RL and SFT at the instance level. When all rollouts fail, SuperRL falls back to SFT on expert demonstrations.

2. Supervised Reinforcement Learning (SRL) reformulates problem-solving as a sequential decision-making process. Rather than optimizing for a final answer or imitating an entire expert trajectory, SRL trains the model to reproduce the sequence of key actions underlying expert reasoning, following an RL-style objective.

3. BREAD uses part of an expert trace as an anchor, then generates additional rollouts that branch from its intermediate episodes. These branched trajectories provide denser, higher-quality feedback.

These methods aim to address the fundamental trade-off between leveraging expert demonstrations for stable initialization and enabling effective exploration through reinforcement learning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "f5ad0eef-45be-4de3-9078-add8602b015b",
  "tool_use_result": {
    "query": "expert trajectory SFT warm start RL cold start demonstrations language model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CdPDAT5SqhinDyabwX6bs7",
        "content": [
          {
            "title": "From Expert Trajectories to Step-wise Reasoning",
            "url": "https://arxiv.org/pdf/2510.25992"
          },
          {
            "title": "Beyond Two-Stage Training: Cooperative SFT and RL for LLM Reasoning",
            "url": "https://arxiv.org/pdf/2509.06948"
          },
          {
            "title": "How Much Backtracking is Enough? Exploring the Interplay of SFT and RL in Enhancing LLM Reasoning",
            "url": "https://arxiv.org/html/2505.24273v1"
          },
          {
            "title": "Rethinking Expert Trajectory Utilization in LLM Post-training",
            "url": "https://arxiv.org/html/2512.11470v1"
          },
          {
            "title": "SuperRL: Reinforcement Learning with Supervision to Boost Language Model Reasoning",
            "url": "https://arxiv.org/html/2506.01096"
          },
          {
            "title": "Harmonizing Supervised Fine-Tuning and Reinforcement ...",
            "url": "https://arxiv.org/pdf/2508.11408"
          },
          {
            "title": "[2512.11470] Rethinking Expert Trajectory Utilization in LLM Post-training",
            "url": "https://arxiv.org/abs/2512.11470"
          },
          {
            "title": "BREAD: Branched Rollouts from Expert Anchors Bridge SFT & RL for Reasoning",
            "url": "https://arxiv.org/html/2506.17211v1"
          },
          {
            "title": "Supervised Reinforcement Learning: From Expert Trajectories to Step-wise Reasoning",
            "url": "https://arxiv.org/html/2510.25992v1"
          },
          {
            "title": "GitHub - waltonfuture/RL-with-Cold-Start: SFT+RL boosts multimodal reasoning",
            "url": "https://github.com/waltonfuture/RL-with-Cold-Start"
          }
        ]
      },
      "Based on the search results, here's what I found about expert trajectory SFT warm start RL cold start demonstrations and language models:\n\n## Key Concepts\n\nThe two-stage approach, often referred to as \"cold start,\" ensures that the model first learns to imitate expert reasoning patterns, providing a strong initialization for subsequent RL training.\n\n## Main Approaches and Findings\n\n**Sequential SFT-then-RL Pipeline**: The Sequential SFT-then-RL pipeline is established as the superior standard, overcoming the stability deficits of synchronized approaches.\n\n**Challenges with Traditional Cold Start**: Cold-start begins with extremely long responses due to SFT warm-up, causing slow training, followed by a sharp decline and gradual recovery. This \"dip-then-rise\" pattern indicates the model initially loses expert behavior acquired during SFT, then slowly explores new strategies.\n\n**Alternative Approaches**: Researchers have developed various methods to improve upon traditional cold-start training:\n\n1. SuperRL proposes a unified training framework that dynamically switches between RL and SFT at the instance level. When all rollouts fail, SuperRL falls back to SFT on expert demonstrations.\n\n2. Supervised Reinforcement Learning (SRL) reformulates problem-solving as a sequential decision-making process. Rather than optimizing for a final answer or imitating an entire expert trajectory, SRL trains the model to reproduce the sequence of key actions underlying expert reasoning, following an RL-style objective.\n\n3. BREAD uses part of an expert trace as an anchor, then generates additional rollouts that branch from its intermediate episodes. These branched trajectories provide denser, higher-quality feedback.\n\nThese methods aim to address the fundamental trade-off between leveraging expert demonstrations for stable initialization and enabling effective exploration through reinforcement learning."
    ],
    "durationSeconds": 8.307189755999998
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T08:16:46.219Z_

<details><summary>↩ Tool result · `toolu_018Ptw6EshNwEycmQ3yi3yPm`</summary>

```text
Web search results for query: "sparse reward RL text games demonstrations curriculum learning overcome collapse"

Links: [{"title":"Task Phasing: Automated Curriculum Learning from Demonstrations | Request PDF","url":"https://www.researchgate.net/publication/372053512_Task_Phasing_Automated_Curriculum_Learning_from_Demonstrations"},{"title":"Variational Automatic Curriculum Learning for Sparse- ...","url":"https://proceedings.neurips.cc/paper/2021/file/503e7dbbd6217b9a591f3322f39b5a6c-Paper.pdf"},{"title":"Reinforcement Learning: Dealing with Sparse Reward Environments | by Karam Daaboul | Medium","url":"https://medium.com/@m.k.daaboul/dealing-with-sparse-reward-environments-38c0489c844d"},{"title":"Task Phasing: Automated Curriculum Learning from Demonstrations","url":"https://people.engr.tamu.edu/guni/papers/ICAPS23-phasing.pdf"},{"title":"[2210.10999] Task Phasing: Automated Curriculum Learning from Demonstrations","url":"https://arxiv.org/abs/2210.10999"},{"title":"Reverse Forward Curriculum Learning for Extreme Demo Efficiency in RL","url":"https://reverseforward-cl.github.io/"},{"title":"Reinforcement Learning with Curriculum Learning for Complex Tasks | by Hey Amit | Medium","url":"https://medium.com/@heyamit10/reinforcement-learning-with-curriculum-learning-for-complex-tasks-4f306470ed42"},{"title":"Conviction-Based Planning for Sparse Reward Reinforcement Learning Problems","url":"https://icaps24.icaps-conference.org/program/workshops/prl-papers/8.pdf"},{"title":"(PDF) Curriculum Learning Algorithms for Reward Weighting in Sparse Reward Robotic Manipulation Tasks","url":"https://www.researchgate.net/publication/389766640_Curriculum_Learning_Algorithms_for_Reward_Weighting_in_Sparse_Reward_Robotic_Manipulation_Tasks"},{"title":"Automated Curriculum Learning","url":"https://rlcurriculum.github.io/"}]

Based on the web search results, I found relevant research on addressing sparse reward RL challenges using demonstrations and curriculum learning. Here's what the literature shows:

## Key Approaches to Overcome Sparse Reward Challenges

Applying reinforcement learning (RL) to sparse reward domains is notoriously challenging due to insufficient guiding signals, with common techniques including learning from demonstrations and curriculum learning.

### Task Phasing: Combining Demonstrations and Curriculum Learning

A principled task-phasing approach uses demonstrations to automatically generate a curriculum sequence, gradually increasing task complexity from a simple initial task to the target task while retuning the RL agent in each phasing iteration.

One approach creates a task continuum where each task is a convex combination of an informative dense reward (from inverse RL on demonstrations) and the target sparse reward, with theory proving that under reasonable assumptions, this curriculum produces monotonically non-decreasing policy return in expectation.

### Results in Practice

Experimental results on sparse reward domains demonstrate that task phasing approaches outperform state-of-the-art approaches with respect to asymptotic performance, succeeding in converging to an optimized policy where baseline RL algorithms fail.

### Reverse-Forward Curriculum Learning

An alternative approach for demonstration efficiency involves reverse-forward curriculum learning (RFCL), which achieves much higher sample and demonstration efficiency and solves previously unsolvable tasks from just 1-10 demonstrations and sparse rewards without much hyperparameter tuning.

These methods address the challenge of learning from sparse rewards by leveraging demonstration data to create meaningful task progressions that guide the learning process.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "5e3bdb4c-7346-4f7e-ad40-b30bed2935b6",
  "tool_use_result": {
    "query": "sparse reward RL text games demonstrations curriculum learning overcome collapse",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SjLTqwsaDrRYz4jgrZqE5K",
        "content": [
          {
            "title": "Task Phasing: Automated Curriculum Learning from Demonstrations | Request PDF",
            "url": "https://www.researchgate.net/publication/372053512_Task_Phasing_Automated_Curriculum_Learning_from_Demonstrations"
          },
          {
            "title": "Variational Automatic Curriculum Learning for Sparse- ...",
            "url": "https://proceedings.neurips.cc/paper/2021/file/503e7dbbd6217b9a591f3322f39b5a6c-Paper.pdf"
          },
          {
            "title": "Reinforcement Learning: Dealing with Sparse Reward Environments | by Karam Daaboul | Medium",
            "url": "https://medium.com/@m.k.daaboul/dealing-with-sparse-reward-environments-38c0489c844d"
          },
          {
            "title": "Task Phasing: Automated Curriculum Learning from Demonstrations",
            "url": "https://people.engr.tamu.edu/guni/papers/ICAPS23-phasing.pdf"
          },
          {
            "title": "[2210.10999] Task Phasing: Automated Curriculum Learning from Demonstrations",
            "url": "https://arxiv.org/abs/2210.10999"
          },
          {
            "title": "Reverse Forward Curriculum Learning for Extreme Demo Efficiency in RL",
            "url": "https://reverseforward-cl.github.io/"
          },
          {
            "title": "Reinforcement Learning with Curriculum Learning for Complex Tasks | by Hey Amit | Medium",
            "url": "https://medium.com/@heyamit10/reinforcement-learning-with-curriculum-learning-for-complex-tasks-4f306470ed42"
          },
          {
            "title": "Conviction-Based Planning for Sparse Reward Reinforcement Learning Problems",
            "url": "https://icaps24.icaps-conference.org/program/workshops/prl-papers/8.pdf"
          },
          {
            "title": "(PDF) Curriculum Learning Algorithms for Reward Weighting in Sparse Reward Robotic Manipulation Tasks",
            "url": "https://www.researchgate.net/publication/389766640_Curriculum_Learning_Algorithms_for_Reward_Weighting_in_Sparse_Reward_Robotic_Manipulation_Tasks"
          },
          {
            "title": "Automated Curriculum Learning",
            "url": "https://rlcurriculum.github.io/"
          }
        ]
      },
      "Based on the web search results, I found relevant research on addressing sparse reward RL challenges using demonstrations and curriculum learning. Here's what the literature shows:\n\n## Key Approaches to Overcome Sparse Reward Challenges\n\nApplying reinforcement learning (RL) to sparse reward domains is notoriously challenging due to insufficient guiding signals, with common techniques including learning from demonstrations and curriculum learning.\n\n### Task Phasing: Combining Demonstrations and Curriculum Learning\n\nA principled task-phasing approach uses demonstrations to automatically generate a curriculum sequence, gradually increasing task complexity from a simple initial task to the target task while retuning the RL agent in each phasing iteration.\n\nOne approach creates a task continuum where each task is a convex combination of an informative dense reward (from inverse RL on demonstrations) and the target sparse reward, with theory proving that under reasonable assumptions, this curriculum produces monotonically non-decreasing policy return in expectation.\n\n### Results in Practice\n\nExperimental results on sparse reward domains demonstrate that task phasing approaches outperform state-of-the-art approaches with respect to asymptotic performance, succeeding in converging to an optimized policy where baseline RL algorithms fail.\n\n### Reverse-Forward Curriculum Learning\n\nAn alternative approach for demonstration efficiency involves reverse-forward curriculum learning (RFCL), which achieves much higher sample and demonstration efficiency and solves previously unsolvable tasks from just 1-10 demonstrations and sparse rewards without much hyperparameter tuning.\n\nThese methods address the challenge of learning from sparse rewards by leveraging demonstration data to create meaningful task progressions that guide the learning process."
    ],
    "durationSeconds": 7.900135088000001
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
Good, I have a solid set of results. Let me do a couple more targeted searches to fill in gaps - specifically about GRPO cold start collapse, and about the specific HuggingFace datasets mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "84364b08-4d9a-446a-9d05-bdff5c8e54fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THKFkHx6D4oxE2VZvgCXKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3745
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

_source line 17_

再搜几个针对性方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "d005a8e8-0be9-4648-9439-1840461a3971",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THKFkHx6D4oxE2VZvgCXKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3745
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

_source line 18_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014xtJptJfTRFPmRm4R4KAHz`</summary>

```json
{
  "query": "GRPO training collapse success rate zero sparse reward LLM agent fix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "c9f081ac-f3b3-4140-95e5-0f37f69da938",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THKFkHx6D4oxE2VZvgCXKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3745
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HQxcd2Wyo6Syj2tVp2MW5C`</summary>

```json
{
  "query": "ReAct Reflexion ALFWorld trajectory data open source github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "5af1cd46-3a71-42a1-a37b-80392278cead",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THKFkHx6D4oxE2VZvgCXKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3745
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CRc6qGo8jE8zF1kF1YQfJf`</summary>

```json
{
  "query": "GRPO expert iteration SFT data amount needed cold start small model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "434de211-1729-4b2f-8e73-0c3708770a5f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THKFkHx6D4oxE2VZvgCXKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3745,
      "cache_read_input_tokens": 24223,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3745
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

_source line 21 · 2026-05-14T08:17:01.286Z_

<details><summary>↩ Tool result · `toolu_01HQxcd2Wyo6Syj2tVp2MW5C`</summary>

```text
Web search results for query: "ReAct Reflexion ALFWorld trajectory data open source github"

Links: [{"title":"GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub","url":"https://github.com/noahshinn/reflexion"},{"title":"Alfworld","url":"https://www.catalyzex.com/s/Alfworld"},{"title":"reflexion/alfworld_runs/generate_reflections.py at main · noahshinn/reflexion","url":"https://github.com/noahshinn/reflexion/blob/main/alfworld_runs/generate_reflections.py"},{"title":"Agent Planning with World Knowledge Model","url":"https://knowledge-nlp.github.io/acl2024/papers/20_agent_planning_with_world_know.pdf"},{"title":"LLM Powered Autonomous Agents | Lil'Log","url":"https://lilianweng.github.io/posts/2023-06-23-agent/"},{"title":"Reproducing Alfworld Results · Issue #35 · noahshinn/reflexion","url":"https://github.com/noahshinn/reflexion/issues/35"},{"title":"ReAct: Synergizing Reasoning and Acting in Language Models","url":"https://react-lm.github.io/"},{"title":"GitHub - Dun-sin/react-open-source-projects: A list of open source react/next projects to contribute to · GitHub","url":"https://github.com/Dun-sin/react-open-source-projects"},{"title":"ReAct/alfworld.ipynb at master · ysymyth/ReAct","url":"https://github.com/ysymyth/ReAct/blob/master/alfworld.ipynb"},{"title":"GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub","url":"https://github.com/stevenyangyj/Emma-Alfworld"}]

Based on the search results, here are the key resources for ReAct, Reflexion, and ALFWorld trajectory data available on GitHub:

## Main Repositories

The Reflexion repository contains the code, demos, and log files for Reflexion: Language Agents with Verbal Reinforcement Learning, and it's available at https://github.com/noahshinn/reflexion.

All runs from the paper and additional results are logged in ./alfworld_runs/root for decision-making, ./hotpotqa_runs/root for reasoning, and ./programming_runs/root for programming.

For ReAct, the ReAct repository is available at ysymyth/ReAct, which includes an alfworld.ipynb notebook demonstrating ReAct on ALFWorld.

## Trajectory Data

The Emma-Alfworld repository has released experimental (trajectory) logs of EMMA and reflexion LLM teacher, available at https://github.com/stevenyangyj/Emma-Alfworld. They offer a dataset available from HuggingFace for ALFWorld.

## Important Note

Due to the nature of these experiments, it may not be feasible for individual developers to rerun the results as GPT-4 has limited access and significant API charges.

These repositories provide the foundational open-source resources for ReAct and Reflexion with ALFWorld trajectory data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "86a3613b-0c7c-4102-ac4c-3c945cbe7209",
  "tool_use_result": {
    "query": "ReAct Reflexion ALFWorld trajectory data open source github",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DNo66JsXwC6yDc82XXD8Vd",
        "content": [
          {
            "title": "GitHub - noahshinn/reflexion: [NeurIPS 2023] Reflexion: Language Agents with Verbal Reinforcement Learning · GitHub",
            "url": "https://github.com/noahshinn/reflexion"
          },
          {
            "title": "Alfworld",
            "url": "https://www.catalyzex.com/s/Alfworld"
          },
          {
            "title": "reflexion/alfworld_runs/generate_reflections.py at main · noahshinn/reflexion",
            "url": "https://github.com/noahshinn/reflexion/blob/main/alfworld_runs/generate_reflections.py"
          },
          {
            "title": "Agent Planning with World Knowledge Model",
            "url": "https://knowledge-nlp.github.io/acl2024/papers/20_agent_planning_with_world_know.pdf"
          },
          {
            "title": "LLM Powered Autonomous Agents | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2023-06-23-agent/"
          },
          {
            "title": "Reproducing Alfworld Results · Issue #35 · noahshinn/reflexion",
            "url": "https://github.com/noahshinn/reflexion/issues/35"
          },
          {
            "title": "ReAct: Synergizing Reasoning and Acting in Language Models",
            "url": "https://react-lm.github.io/"
          },
          {
            "title": "GitHub - Dun-sin/react-open-source-projects: A list of open source react/next projects to contribute to · GitHub",
            "url": "https://github.com/Dun-sin/react-open-source-projects"
          },
          {
            "title": "ReAct/alfworld.ipynb at master · ysymyth/ReAct",
            "url": "https://github.com/ysymyth/ReAct/blob/master/alfworld.ipynb"
          },
          {
            "title": "GitHub - stevenyangyj/Emma-Alfworld: Official code for the paper: Embodied Multi-Modal Agent trained by an LLM from a Parallel TextWorld · GitHub",
            "url": "https://github.com/stevenyangyj/Emma-Alfworld"
          }
        ]
      },
      "Based on the search results, here are the key resources for ReAct, Reflexion, and ALFWorld trajectory data available on GitHub:\n\n## Main Repositories\n\nThe Reflexion repository contains the code, demos, and log files for Reflexion: Language Agents with Verbal Reinforcement Learning, and it's available at https://github.com/noahshinn/reflexion.\n\nAll runs from the paper and additional results are logged in ./alfworld_runs/root for decision-making, ./hotpotqa_runs/root for reasoning, and ./programming_runs/root for programming.\n\nFor ReAct, the ReAct repository is available at ysymyth/ReAct, which includes an alfworld.ipynb notebook demonstrating ReAct on ALFWorld.\n\n## Trajectory Data\n\nThe Emma-Alfworld repository has released experimental (trajectory) logs of EMMA and reflexion LLM teacher, available at https://github.com/stevenyangyj/Emma-Alfworld. They offer a dataset available from HuggingFace for ALFWorld.\n\n## Important Note\n\nDue to the nature of these experiments, it may not be feasible for individual developers to rerun the results as GPT-4 has limited access and significant API charges.\n\nThese repositories provide the foundational open-source resources for ReAct and Reflexion with ALFWorld trajectory data."
    ],
    "durationSeconds": 6.5761428680000025
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-14T08:17:02.044Z_

<details><summary>↩ Tool result · `toolu_014xtJptJfTRFPmRm4R4KAHz`</summary>

```text
Web search results for query: "GRPO training collapse success rate zero sparse reward LLM agent fix"

Links: [{"title":"ShapE-GRPO: Shapley-Enhanced Reward Allocation for Multi-Candidate LLM Training","url":"https://arxiv.org/html/2603.29871"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"hello-agents/docs/chapter11/Chapter11-Agentic-RL.md at main · datawhalechina/hello-agents","url":"https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/Chapter11-Agentic-RL.md"},{"title":"Tree Search for LLM Agent Reinforcement Learning","url":"https://arxiv.org/pdf/2509.21240"},{"title":"DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed","url":"https://arxiv.org/pdf/2503.14476"},{"title":"Discovering Process–Outcome Credit in Multi-Step LLM Reasoning","url":"https://arxiv.org/html/2602.01034.pdf"},{"title":"Training-Free Group Relative Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=tyUnYbE7Gi"},{"title":"XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation","url":"https://arxiv.org/html/2510.06672v2"},{"title":"Group-in-Group Policy Optimization for LLM Agent Training","url":"https://arxiv.org/html/2505.10978v3"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"}]

Based on the search results, I found several relevant findings about GRPO training issues and proposed solutions:

## GRPO Training Issues with Sparse Rewards and Zero Rewards

The naive GRPO baseline suffers from several key issues such as entropy collapse, reward noise, and training instability. The high variance caused by sparse reward signals in GRPO is a significant challenge.

## Zero-Reward Problem (Zero Sparse Reward)

Prompts with no successes (zero reward) can be addressed through an in-context seeding strategy that injects curated exemplars, steering the model into more difficult reasoning trajectories to break the zero-reward symmetry. This is part of the XRPO (eXplore–eXploit GRPO) framework.

## Proposed Fixes for Training Collapse

Several approaches have been developed to address these issues:

1. **Clip-Higher Strategy**: Clip-Higher promotes the diversity of the system and avoids entropy collapse.

2. **ShapE-GRPO**: Shapley-Enhanced GRPO uses a Shapley-enhanced formulation from cooperative game theory to decompose set-level rewards into granular, candidate-specific signals.

3. **Step-wise Rewards**: Unlike the outcome-sparse GRPO baseline, step-wise signals act as dense navigational cues, effectively guiding the policy through complex reasoning paths.

4. **In-Context Learning (ICL)**: Conditioning on verified successes from similar tasks provides contextual guidance that breaks the zero-reward symmetry and enables in-context policy improvement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "d0f611e2-644b-4cec-bbed-a756de39522e",
  "tool_use_result": {
    "query": "GRPO training collapse success rate zero sparse reward LLM agent fix",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RLn8BS2rmPRA67cKDhXT62",
        "content": [
          {
            "title": "ShapE-GRPO: Shapley-Enhanced Reward Allocation for Multi-Candidate LLM Training",
            "url": "https://arxiv.org/html/2603.29871"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "hello-agents/docs/chapter11/Chapter11-Agentic-RL.md at main · datawhalechina/hello-agents",
            "url": "https://github.com/datawhalechina/hello-agents/blob/main/docs/chapter11/Chapter11-Agentic-RL.md"
          },
          {
            "title": "Tree Search for LLM Agent Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2509.21240"
          },
          {
            "title": "DAPO: An Open-Source LLM Reinforcement Learning System at Scale 1ByteDance Seed",
            "url": "https://arxiv.org/pdf/2503.14476"
          },
          {
            "title": "Discovering Process–Outcome Credit in Multi-Step LLM Reasoning",
            "url": "https://arxiv.org/html/2602.01034.pdf"
          },
          {
            "title": "Training-Free Group Relative Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=tyUnYbE7Gi"
          },
          {
            "title": "XRPO: Pushing the limits of GRPO with Targeted Exploration and Exploitation",
            "url": "https://arxiv.org/html/2510.06672v2"
          },
          {
            "title": "Group-in-Group Policy Optimization for LLM Agent Training",
            "url": "https://arxiv.org/html/2505.10978v3"
          },
          {
            "title": "GRPO++: Tricks for Making RL Actually Work",
            "url": "https://cameronrwolfe.substack.com/p/grpo-tricks"
          }
        ]
      },
      "Based on the search results, I found several relevant findings about GRPO training issues and proposed solutions:\n\n## GRPO Training Issues with Sparse Rewards and Zero Rewards\n\nThe naive GRPO baseline suffers from several key issues such as entropy collapse, reward noise, and training instability. The high variance caused by sparse reward signals in GRPO is a significant challenge.\n\n## Zero-Reward Problem (Zero Sparse Reward)\n\nPrompts with no successes (zero reward) can be addressed through an in-context seeding strategy that injects curated exemplars, steering the model into more difficult reasoning trajectories to break the zero-reward symmetry. This is part of the XRPO (eXplore–eXploit GRPO) framework.\n\n## Proposed Fixes for Training Collapse\n\nSeveral approaches have been developed to address these issues:\n\n1. **Clip-Higher Strategy**: Clip-Higher promotes the diversity of the system and avoids entropy collapse.\n\n2. **ShapE-GRPO**: Shapley-Enhanced GRPO uses a Shapley-enhanced formulation from cooperative game theory to decompose set-level rewards into granular, candidate-specific signals.\n\n3. **Step-wise Rewards**: Unlike the outcome-sparse GRPO baseline, step-wise signals act as dense navigational cues, effectively guiding the policy through complex reasoning paths.\n\n4. **In-Context Learning (ICL)**: Conditioning on verified successes from similar tasks provides contextual guidance that breaks the zero-reward symmetry and enables in-context policy improvement."
    ],
    "durationSeconds": 7.552818035000004
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-14T08:17:03.132Z_

<details><summary>↩ Tool result · `toolu_01CRc6qGo8jE8zF1kF1YQfJf`</summary>

```text
Web search results for query: "GRPO expert iteration SFT data amount needed cold start small model"

Links: [{"title":"A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi","url":"https://yugeten.github.io/posts/2025/01/ppogrpo/"},{"title":"How DeepSeek R1, GRPO, and Previous DeepSeek Models Work","url":"https://ghost.oxen.ai/how-deepseek-r1-grpo-and-previous-deepseek-models-work/"},{"title":"Is cold start SFT always necessary before GRPO - Reinforcement Fine-Tuning LLMs with GRPO - DeepLearning.AI","url":"https://community.deeplearning.ai/t/is-cold-start-sft-always-necessary-before-grpo/819556"},{"title":"From Zero to Reasoning Hero: How DeepSeek-R1 Leverages Reinforcement Learning to Master Complex Reasoning","url":"https://huggingface.co/blog/NormalUhr/deepseek-r1-explained"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Why GRPO is Important and How it Works","url":"https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works/"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2501.12948v1"},{"title":"Reinforcement Fine-tuning (GRPO) | Predibase","url":"https://docs.predibase.com/user-guide/fine-tuning/grpo"},{"title":"A Practical Guide to Fine-Tuning Language Models with GRPO - Part 2","url":"https://community.cloudera.com/t5/Engineering-Blogs/A-Practical-Guide-to-Fine-Tuning-Language-Models-with-GRPO/ba-p/413020"},{"title":"Fine-Tuning Techniques - Choosing Between SFT, DPO, and RFT (With a Guide to DPO)","url":"https://developers.openai.com/cookbook/examples/fine_tuning_direct_preference_optimization_guide"}]

Based on the search results, I've found relevant information about GRPO, expert iteration, SFT data amounts, cold start strategies, and small model training. Here's what the research shows:

## Cold-Start SFT Data Amount

The DeepSeek-R1 approach begins by collecting thousands of cold-start data to fine-tune the base model. While the exact number isn't specified in these sources, the cold-start dataset consists of thousands of curated chain-of-thought samples.

## Expert Iteration and Iterative SFT

The GRPO pipeline involves expert iteration through multiple stages:

1. **Cold Start Phase**: Fine-tune a base model on a few thousand curated, human-friendly long CoTs

2. **Iterative Refinement**: After the cold start SFT, they alternate between RL and SFT by using rejection sampling to curate the data for each round. When reasoning-oriented RL converges, they utilize the checkpoint to collect SFT data for the subsequent round, incorporating data from other domains to enhance the model's capabilities.

## Small Model Training Strategy

For smaller models, to train smaller models, directly fine-tune them on 800k responses generated by DeepSeek-R1, with no RL or iterative alignment—just mimicry, with smaller models inheriting reasoning patterns discovered by the larger model's RL. Direct distillation from DeepSeek-R1 outperforms applying RL on smaller models.

## Cold Start Necessity

DeepSeek-R1-Zero completely skips the SFT part and applies RL directly to the base model, though this approach likely won't work without a very good base model.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "07093766-f106-40c5-908c-593bec7d3802",
  "tool_use_result": {
    "query": "GRPO expert iteration SFT data amount needed cold start small model",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RX5dp3x9LAsbcmRjeXpsB3",
        "content": [
          {
            "title": "A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi",
            "url": "https://yugeten.github.io/posts/2025/01/ppogrpo/"
          },
          {
            "title": "How DeepSeek R1, GRPO, and Previous DeepSeek Models Work",
            "url": "https://ghost.oxen.ai/how-deepseek-r1-grpo-and-previous-deepseek-models-work/"
          },
          {
            "title": "Is cold start SFT always necessary before GRPO - Reinforcement Fine-Tuning LLMs with GRPO - DeepLearning.AI",
            "url": "https://community.deeplearning.ai/t/is-cold-start-sft-always-necessary-before-grpo/819556"
          },
          {
            "title": "From Zero to Reasoning Hero: How DeepSeek-R1 Leverages Reinforcement Learning to Master Complex Reasoning",
            "url": "https://huggingface.co/blog/NormalUhr/deepseek-r1-explained"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "Why GRPO is Important and How it Works",
            "url": "https://ghost.oxen.ai/why-grpo-is-important-and-how-it-works/"
          },
          {
            "title": "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning",
            "url": "https://arxiv.org/html/2501.12948v1"
          },
          {
            "title": "Reinforcement Fine-tuning (GRPO) | Predibase",
            "url": "https://docs.predibase.com/user-guide/fine-tuning/grpo"
          },
          {
            "title": "A Practical Guide to Fine-Tuning Language Models with GRPO - Part 2",
            "url": "https://community.cloudera.com/t5/Engineering-Blogs/A-Practical-Guide-to-Fine-Tuning-Language-Models-with-GRPO/ba-p/413020"
          },
          {
            "title": "Fine-Tuning Techniques - Choosing Between SFT, DPO, and RFT (With a Guide to DPO)",
            "url": "https://developers.openai.com/cookbook/examples/fine_tuning_direct_preference_optimization_guide"
          }
        ]
      },
      "Based on the search results, I've found relevant information about GRPO, expert iteration, SFT data amounts, cold start strategies, and small model training. Here's what the research shows:\n\n## Cold-Start SFT Data Amount\n\nThe DeepSeek-R1 approach begins by collecting thousands of cold-start data to fine-tune the base model. While the exact number isn't specified in these sources, the cold-start dataset consists of thousands of curated chain-of-thought samples.\n\n## Expert Iteration and Iterative SFT\n\nThe GRPO pipeline involves expert iteration through multiple stages:\n\n1. **Cold Start Phase**: Fine-tune a base model on a few thousand curated, human-friendly long CoTs\n\n2. **Iterative Refinement**: After the cold start SFT, they alternate between RL and SFT by using rejection sampling to curate the data for each round. When reasoning-oriented RL converges, they utilize the checkpoint to collect SFT data for the subsequent round, incorporating data from other domains to enhance the model's capabilities.\n\n## Small Model Training Strategy\n\nFor smaller models, to train smaller models, directly fine-tune them on 800k responses generated by DeepSeek-R1, with no RL or iterative alignment—just mimicry, with smaller models inheriting reasoning patterns discovered by the larger model's RL. Direct distillation from DeepSeek-R1 outperforms applying RL on smaller models.\n\n## Cold Start Necessity\n\nDeepSeek-R1-Zero completely skips the SFT part and applies RL directly to the base model, though this approach likely won't work without a very good base model."
    ],
    "durationSeconds": 7.581165199999999
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check the ALFWorld repo for built-in expert walkthroughs, and look at the specific HuggingFace datasets mentioned.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "bc84b469-792f-4baf-a630-c78f9c1b9190",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehji3TYJdkrnXgHoMBdm1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 27968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3080
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

再查一下 ALFWorld 自带的 expert data 和 HF 数据集详情。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "6acc1cd4-0823-4836-a2f3-e1af321944fa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehji3TYJdkrnXgHoMBdm1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 27968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3080
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012curerx5mjR1L5kmSoZM8i`</summary>

```json
{
  "query": "alfworld github expert walkthrough json training data TWRecipe"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "6f0fbbde-0514-4c0b-9c34-75c53b1bca8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehji3TYJdkrnXgHoMBdm1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 27968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3080
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_017TXbUR3Yu7WaX2xjJFumjC`</summary>

```json
{
  "query": "yijunyang alfworld-sft-dataset huggingface quality"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "71eff8bf-a923-4081-9d69-9edf075bacc8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ehji3TYJdkrnXgHoMBdm1o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3080,
      "cache_read_input_tokens": 27968,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3080
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

_source line 28 · 2026-05-14T08:17:13.534Z_

<details><summary>↩ Tool result · `toolu_017TXbUR3Yu7WaX2xjJFumjC`</summary>

```text
Web search results for query: "yijunyang alfworld-sft-dataset huggingface quality"

Links: [{"title":"yijunyang/alfworld-sft-dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/yijunyang/alfworld-sft-dataset"},{"title":"u-10bei/sft_alfworld_trajectory_dataset · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v2 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v2"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v4 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v4"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v3 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v3"},{"title":"alfworld - benchmark's activity","url":"https://huggingface.co/organizations/benchmark/activity/all"},{"title":"u-10bei/sft_alfworld_trajectory_dataset_v5 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5"},{"title":"Awesome SFT datasets - a HuggingFaceH4 Collection","url":"https://huggingface.co/collections/HuggingFaceH4/awesome-sft-datasets"},{"title":"data/alfworld-00000-of-00001-302ad687bb3817a4.parquet · zai-org/AgentInstruct at main","url":"https://huggingface.co/datasets/zai-org/AgentInstruct/blob/main/data/alfworld-00000-of-00001-302ad687bb3817a4.parquet"},{"title":"hkust-nlp/agentboard · Datasets at Hugging Face","url":"https://huggingface.co/datasets/hkust-nlp/agentboard"}]

Based on the search results, here's what I found:

The yijunyang/alfworld-sft-dataset on Hugging Face currently has a data viewer issue, with only a preview of rows available. The dataset page appears to be experiencing technical difficulties, as there is a DatasetGenerationError with a KeyError related to 'jpg' file handling in the webdataset module.

The search results also show that yijunyang has authored several papers related to ALFWorld and agent benchmarking. However, specific information about the dataset quality, size, or detailed characteristics is not available in these search results due to the viewer error on the dataset page itself.

If you need more detailed information about this dataset, you may want to check the dataset's GitHub repository or contact the dataset author directly for documentation on its quality metrics and specifications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "559c63f5-d131-4b4d-93ed-a314eca9ae5c",
  "tool_use_result": {
    "query": "yijunyang alfworld-sft-dataset huggingface quality",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ENQCgye2DvzYhVLoHxiFN8",
        "content": [
          {
            "title": "yijunyang/alfworld-sft-dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/yijunyang/alfworld-sft-dataset"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v2 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v2"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v4 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v4"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v3 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v3"
          },
          {
            "title": "alfworld - benchmark's activity",
            "url": "https://huggingface.co/organizations/benchmark/activity/all"
          },
          {
            "title": "u-10bei/sft_alfworld_trajectory_dataset_v5 · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset_v5"
          },
          {
            "title": "Awesome SFT datasets - a HuggingFaceH4 Collection",
            "url": "https://huggingface.co/collections/HuggingFaceH4/awesome-sft-datasets"
          },
          {
            "title": "data/alfworld-00000-of-00001-302ad687bb3817a4.parquet · zai-org/AgentInstruct at main",
            "url": "https://huggingface.co/datasets/zai-org/AgentInstruct/blob/main/data/alfworld-00000-of-00001-302ad687bb3817a4.parquet"
          },
          {
            "title": "hkust-nlp/agentboard · Datasets at Hugging Face",
            "url": "https://huggingface.co/datasets/hkust-nlp/agentboard"
          }
        ]
      },
      "Based on the search results, here's what I found:\n\nThe yijunyang/alfworld-sft-dataset on Hugging Face currently has a data viewer issue, with only a preview of rows available. The dataset page appears to be experiencing technical difficulties, as there is a DatasetGenerationError with a KeyError related to 'jpg' file handling in the webdataset module.\n\nThe search results also show that yijunyang has authored several papers related to ALFWorld and agent benchmarking. However, specific information about the dataset quality, size, or detailed characteristics is not available in these search results due to the viewer error on the dataset page itself.\n\nIf you need more detailed information about this dataset, you may want to check the dataset's GitHub repository or contact the dataset author directly for documentation on its quality metrics and specifications."
    ],
    "durationSeconds": 4.964042608000003
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-14T08:17:15.663Z_

<details><summary>↩ Tool result · `toolu_012curerx5mjR1L5kmSoZM8i`</summary>

```text
Web search results for query: "alfworld github expert walkthrough json training data TWRecipe"

Links: [{"title":"GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub","url":"https://github.com/alfworld/alfworld"},{"title":"ALFWorld","url":"https://alfworld.github.io/"},{"title":"alfworld/alfworld/data at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/tree/master/alfworld/data"},{"title":"alfworld - Overview","url":"https://github.com/alfworld/"},{"title":"Following expert actions doesn't always lead to finishing the task · Issue #87 · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/issues/87"},{"title":"Releases · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/releases"},{"title":"GitHub - askforalfred/alfred: ALFRED - A Benchmark for Interpreting Grounded Instructions for Everyday Tasks · GitHub","url":"https://github.com/askforalfred/alfred"},{"title":"agentquest/agentquest/benchmarks/alfworld/README.md at main · nec-research/agentquest","url":"https://github.com/nec-research/agentquest/blob/main/agentquest/benchmarks/alfworld/README.md"},{"title":"alfworld/configs/base_config.yaml at master · alfworld/alfworld","url":"https://github.com/alfworld/alfworld/blob/master/configs/base_config.yaml"},{"title":"LLF-Bench/llfbench/envs/alfworld/alfworld.py at main · microsoft/LLF-Bench","url":"https://github.com/microsoft/LLF-Bench/blob/main/llfbench/envs/alfworld/alfworld.py"}]

Based on the search results, I found relevant information about ALFWorld, the expert walkthrough, and the JSON training data structure:

## ALFWorld Overview

ALFWorld contains interactive TextWorld environments that parallel embodied worlds in the ALFRED dataset, where aligned environments allow agents to reason and learn high-level policies in an abstract space before solving embodied tasks through low-level actuation.

## Training Data Structure

The JSON training data is organized with trajectory metadata in traj_data.json files, PDDL descriptions of initial states, and textworld game files (game.tw-pddl) within directories structured by task_type, object, movableReceptacle, receptacle, and sceneNum.

Each trajectory contains metadata including a unique trajectory ID, task type (such as "pick_heat_then_place_in_recep"), and PDDL parameters that define the object target, parent target, movable receptacle target, and toggle target for the task.

## Expert and Game Generation

The alfworld-generate tool generates game.tw-pddl files from initial_state.pddls and uses the expert to check if the text game is solvable before dumping a game file used by the text-engine.

## Task Categories

ALFWorld consists of tasks among six categories: pick_and_place, look_at_obj_in_light, pick_clean_then_place, pick_heat_then_place, pick_cool_then_place and pick_two_obj_and_place.

The search results contain documentation from the official ALFWorld GitHub repository, which provides comprehensive details about the dataset structure and expert walkthroughs for training data generation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "9627cfb2-ef06-4e03-9fb5-ba024270d49a",
  "tool_use_result": {
    "query": "alfworld github expert walkthrough json training data TWRecipe",
    "results": [
      {
        "tool_use_id": "srvtoolu_019EhNz4HZ16hh2NvukMPvia",
        "content": [
          {
            "title": "GitHub - alfworld/alfworld: ALFWorld: Aligning Text and Embodied Environments for Interactive Learning · GitHub",
            "url": "https://github.com/alfworld/alfworld"
          },
          {
            "title": "ALFWorld",
            "url": "https://alfworld.github.io/"
          },
          {
            "title": "alfworld/alfworld/data at master · alfworld/alfworld",
            "url": "https://github.com/alfworld/alfworld/tree/master/alfworld/data"
          },
          {
            "title": "alfworld - Overview",
            "url": "https://github.com/alfworld/"
          },
          {
            "title": "Following expert actions doesn't always lead to finishing the task · Issue #87 · alfworld/alfworld",
            "url": "https://github.com/alfworld/alfworld/issues/87"
          },
          {
            "title": "Releases · alfworld/alfworld",
            "url": "https://github.com/alfworld/alfworld/releases"
          },
          {
            "title": "GitHub - askforalfred/alfred: ALFRED - A Benchmark for Interpreting Grounded Instructions for Everyday Tasks · GitHub",
            "url": "https://github.com/askforalfred/alfred"
          },
          {
            "title": "agentquest/agentquest/benchmarks/alfworld/README.md at main · nec-research/agentquest",
            "url": "https://github.com/nec-research/agentquest/blob/main/agentquest/benchmarks/alfworld/README.md"
          },
          {
            "title": "alfworld/configs/base_config.yaml at master · alfworld/alfworld",
            "url": "https://github.com/alfworld/alfworld/blob/master/configs/base_config.yaml"
          },
          {
            "title": "LLF-Bench/llfbench/envs/alfworld/alfworld.py at main · microsoft/LLF-Bench",
            "url": "https://github.com/microsoft/LLF-Bench/blob/main/llfbench/envs/alfworld/alfworld.py"
          }
        ]
      },
      "Based on the search results, I found relevant information about ALFWorld, the expert walkthrough, and the JSON training data structure:\n\n## ALFWorld Overview\n\nALFWorld contains interactive TextWorld environments that parallel embodied worlds in the ALFRED dataset, where aligned environments allow agents to reason and learn high-level policies in an abstract space before solving embodied tasks through low-level actuation.\n\n## Training Data Structure\n\nThe JSON training data is organized with trajectory metadata in traj_data.json files, PDDL descriptions of initial states, and textworld game files (game.tw-pddl) within directories structured by task_type, object, movableReceptacle, receptacle, and sceneNum.\n\nEach trajectory contains metadata including a unique trajectory ID, task type (such as \"pick_heat_then_place_in_recep\"), and PDDL parameters that define the object target, parent target, movable receptacle target, and toggle target for the task.\n\n## Expert and Game Generation\n\nThe alfworld-generate tool generates game.tw-pddl files from initial_state.pddls and uses the expert to check if the text game is solvable before dumping a game file used by the text-engine.\n\n## Task Categories\n\nALFWorld consists of tasks among six categories: pick_and_place, look_at_obj_in_light, pick_clean_then_place, pick_heat_then_place, pick_cool_then_place and pick_two_obj_and_place.\n\nThe search results contain documentation from the official ALFWorld GitHub repository, which provides comprehensive details about the dataset structure and expert walkthroughs for training data generation."
    ],
    "durationSeconds": 7.625283702000001
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to write the research report. Let me also check one more thing - the ALFWorld expert walkthroughs that come with the package.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "e5beb1d5-5a70-414a-b5ad-fa4db4a4d4c3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vi4fmAKMc5MZT7eLWKB3at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 31048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1070
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

_source line 31_

信息收集充分，现在写调研报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "23f0f070-e94b-4104-8afa-937c205023ef",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vi4fmAKMc5MZT7eLWKB3at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 31048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1070
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01EQveoRvFeiqjNsWYv6ko7M`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "f24d063b-8ed8-46ac-b62b-c26fdd3f2bba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vi4fmAKMc5MZT7eLWKB3at",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 827,
      "cache_creation_input_tokens": 1070,
      "cache_read_input_tokens": 31048,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1070
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

_source line 33 · 2026-05-14T08:17:20.408Z_

<details><summary>↩ Tool result · `toolu_01EQveoRvFeiqjNsWYv6ko7M`</summary>

````text
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
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "30a0688e-bfc7-4182-8f3f-8519a261d7de",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 34_

---

## 调研报告：Expert Trajectory SFT 作为 GRPO 冷启动 Backup Plan

### 问题诊断

当前 SFT warmup (1200条) 教会了格式但未教策略，导致 GRPO 初始 success rate 仅 4-8%。GRPO 在 sparse reward 下因 zero-reward symmetry 无法产生有效梯度信号，grad_norm→0, pg_loss→0，策略崩塌。核心需求：**提升 GRPO 初始 success rate 到 >5%，打破 zero-reward 死锁**。

### 可行方案（按可行性排序）

**方案 1：ALFWorld 自带 Expert Walkthrough 生成完整轨迹 SFT 数据**
- 数据来源：`alfworld` 包自带 rule-based expert，用 `alfworld-generate` 可对每个 game 生成 expert solution。每个 task 被分解为子目标序列（find→pick→find→heat→find→place）
- 工作量：**1-2 天**。写脚本调 ALFWorld expert 在 3000+ train games 上跑通，收集成功轨迹，转为 multi-turn SFT 格式
- 预期效果：3000+ 条 expert 完整轨迹 SFT 后，初始 success rate 预计 15-30%（参考 MACLA 用 1425 条轨迹达 82%，但那是大模型）
- **推荐度：最高**。数据质量有保证（100% 成功），数量充足，无需外部依赖

**方案 2：HuggingFace 现成 SFT 数据集**
- 数据来源：`u-10bei/sft_alfworld_trajectory_dataset` (v1-v5) — 模板生成的 expert 轨迹，支持 ReAct 和 function-calling 格式；`yijunyang/alfworld-sft-dataset` — 数据查看器有报错，质量待验证
- 工作量：**半天**。下载 → 格式转换 → SFT
- 预期效果：取决于数据与你的环境/prompt 格式对齐程度。模板生成数据可能与真实 ALFWorld 交互有 gap
- 风险：格式不匹配需要大量适配工作，v1-v5 多个版本说明作者也在迭代质量

**方案 3：Reflexion/ReAct GPT-4 轨迹蒸馏**
- 数据来源：[Reflexion repo](https://github.com/noahshinn/reflexion) 的 `alfworld_runs/root` 有 GPT-4 运行日志；[Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld) 有 LLM teacher 轨迹
- 工作量：**1-2 天**。解析日志 → 筛选成功轨迹 → 格式化
- 预期效果：GPT-4 轨迹质量高但风格可能不适合小模型直接模仿，需要 filtering
- 风险：日志格式非标准 SFT 格式，解析工作量不确定

**方案 4：XRPO 式 In-Context Seeding（不改 SFT，改 GRPO）**
- 做法：在 GRPO rollout 时注入 few-shot expert 示例，打破 zero-reward symmetry
- 工作量：**半天**。修改 prompt 模板，加入 2-3 个 expert 示例
- 预期效果：不改变模型权重但能提升 rollout 中的成功概率，让 GRPO 有正样本可学
- 风险：增加 context 长度，可能影响训练效率

**方案 5：SuperRL 式 SFT-RL 动态切换**
- 做法：当 GRPO batch 中所有 rollout 失败时，fallback 到 expert trajectory 做 SFT 更新
- 工作量：**2-3 天**。需要修改训练循环，实现 RL/SFT 动态切换逻辑
- 预期效果：理论上最优——防止崩塌同时保留探索。[SuperRL](https://arxiv.org/html/2506.01096) 和 [BREAD](https://arxiv.org/html/2506.17211v1) 均验证有效
- 风险：工程复杂度高，调参难度大

### 关于数据量

- DeepSeek-R1 冷启动用 "thousands" 条 CoT 数据
- 对 1.7B 小模型 + ALFWorld 6 类任务：**每类 200-500 条完整成功轨迹（共 1200-3000 条）** 应足够将初始 success rate 提到 10-20%
- 必须是 **multi-step 完整轨迹**（含 observation-action 交互），单步 action-only 不够教策略

### 推荐

**首选方案 1**（ALFWorld 自带 expert）+ **方案 4**（in-context seeding）组合：先用 expert 生成 3000 条高质量轨迹做 SFT warmup 替换现有 1200 条，同时在 GRPO 中加 few-shot seeding。两者工作量合计 2 天，互相正交，效果叠加。

Sources:
- [Rethinking Expert Trajectory Utilization in LLM Post-training](https://arxiv.org/abs/2512.11470)
- [SuperRL: RL with Supervision](https://arxiv.org/html/2506.01096)
- [BREAD: Branched Rollouts from Expert Anchors](https://arxiv.org/html/2506.17211v1)
- [XRPO: Targeted Exploration for GRPO](https://arxiv.org/html/2510.06672v2)
- [GRPO++ Tricks](https://cameronrwolfe.substack.com/p/grpo-tricks)
- [ALFWorld GitHub](https://github.com/alfworld/alfworld)
- [Reflexion GitHub (ALFWorld runs)](https://github.com/noahshinn/reflexion)
- [Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld)
- [u-10bei ALFWorld SFT Dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset)
- [Task Phasing: Curriculum from Demonstrations](https://arxiv.org/abs/2210.10999)
- [DeepSeek-R1](https://arxiv.org/html/2501.12948v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "uuid": "f378e3c7-53d9-4b7f-846f-d3a779fb13f4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01N7ijzBeucJjZe6Vo4Kid7Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1254,
      "cache_read_input_tokens": 32118,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1254
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

_source line 35_

---

## 调研报告：Expert Trajectory SFT 作为 GRPO 冷启动 Backup Plan

### 问题诊断

当前 SFT warmup (1200条) 教会了格式但未教策略，导致 GRPO 初始 success rate 仅 4-8%。GRPO 在 sparse reward 下因 zero-reward symmetry 无法产生有效梯度信号，grad_norm→0, pg_loss→0，策略崩塌。核心需求：**提升 GRPO 初始 success rate 到 >5%，打破 zero-reward 死锁**。

### 可行方案（按可行性排序）

**方案 1：ALFWorld 自带 Expert Walkthrough 生成完整轨迹 SFT 数据**
- 数据来源：`alfworld` 包自带 rule-based expert，用 `alfworld-generate` 可对每个 game 生成 expert solution。每个 task 被分解为子目标序列（find→pick→find→heat→find→place）
- 工作量：**1-2 天**。写脚本调 ALFWorld expert 在 3000+ train games 上跑通，收集成功轨迹，转为 multi-turn SFT 格式
- 预期效果：3000+ 条 expert 完整轨迹 SFT 后，初始 success rate 预计 15-30%（参考 MACLA 用 1425 条轨迹达 82%，但那是大模型）
- **推荐度：最高**。数据质量有保证（100% 成功），数量充足，无需外部依赖

**方案 2：HuggingFace 现成 SFT 数据集**
- 数据来源：`u-10bei/sft_alfworld_trajectory_dataset` (v1-v5) — 模板生成的 expert 轨迹，支持 ReAct 和 function-calling 格式；`yijunyang/alfworld-sft-dataset` — 数据查看器有报错，质量待验证
- 工作量：**半天**。下载 → 格式转换 → SFT
- 预期效果：取决于数据与你的环境/prompt 格式对齐程度。模板生成数据可能与真实 ALFWorld 交互有 gap
- 风险：格式不匹配需要大量适配工作，v1-v5 多个版本说明作者也在迭代质量

**方案 3：Reflexion/ReAct GPT-4 轨迹蒸馏**
- 数据来源：[Reflexion repo](https://github.com/noahshinn/reflexion) 的 `alfworld_runs/root` 有 GPT-4 运行日志；[Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld) 有 LLM teacher 轨迹
- 工作量：**1-2 天**。解析日志 → 筛选成功轨迹 → 格式化
- 预期效果：GPT-4 轨迹质量高但风格可能不适合小模型直接模仿，需要 filtering
- 风险：日志格式非标准 SFT 格式，解析工作量不确定

**方案 4：XRPO 式 In-Context Seeding（不改 SFT，改 GRPO）**
- 做法：在 GRPO rollout 时注入 few-shot expert 示例，打破 zero-reward symmetry
- 工作量：**半天**。修改 prompt 模板，加入 2-3 个 expert 示例
- 预期效果：不改变模型权重但能提升 rollout 中的成功概率，让 GRPO 有正样本可学
- 风险：增加 context 长度，可能影响训练效率

**方案 5：SuperRL 式 SFT-RL 动态切换**
- 做法：当 GRPO batch 中所有 rollout 失败时，fallback 到 expert trajectory 做 SFT 更新
- 工作量：**2-3 天**。需要修改训练循环，实现 RL/SFT 动态切换逻辑
- 预期效果：理论上最优——防止崩塌同时保留探索。[SuperRL](https://arxiv.org/html/2506.01096) 和 [BREAD](https://arxiv.org/html/2506.17211v1) 均验证有效
- 风险：工程复杂度高，调参难度大

### 关于数据量

- DeepSeek-R1 冷启动用 "thousands" 条 CoT 数据
- 对 1.7B 小模型 + ALFWorld 6 类任务：**每类 200-500 条完整成功轨迹（共 1200-3000 条）** 应足够将初始 success rate 提到 10-20%
- 必须是 **multi-step 完整轨迹**（含 observation-action 交互），单步 action-only 不够教策略

### 推荐

**首选方案 1**（ALFWorld 自带 expert）+ **方案 4**（in-context seeding）组合：先用 expert 生成 3000 条高质量轨迹做 SFT warmup 替换现有 1200 条，同时在 GRPO 中加 few-shot seeding。两者工作量合计 2 天，互相正交，效果叠加。

Sources:
- [Rethinking Expert Trajectory Utilization in LLM Post-training](https://arxiv.org/abs/2512.11470)
- [SuperRL: RL with Supervision](https://arxiv.org/html/2506.01096)
- [BREAD: Branched Rollouts from Expert Anchors](https://arxiv.org/html/2506.17211v1)
- [XRPO: Targeted Exploration for GRPO](https://arxiv.org/html/2510.06672v2)
- [GRPO++ Tricks](https://cameronrwolfe.substack.com/p/grpo-tricks)
- [ALFWorld GitHub](https://github.com/alfworld/alfworld)
- [Reflexion GitHub (ALFWorld runs)](https://github.com/noahshinn/reflexion)
- [Emma-Alfworld](https://github.com/stevenyangyj/Emma-Alfworld)
- [u-10bei ALFWorld SFT Dataset](https://huggingface.co/datasets/u-10bei/sft_alfworld_trajectory_dataset)
- [Task Phasing: Curriculum from Demonstrations](https://arxiv.org/abs/2210.10999)
- [DeepSeek-R1](https://arxiv.org/html/2501.12948v1)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 95898,
  "duration_api_ms": 138713,
  "num_turns": 12,
  "stop_reason": "end_turn",
  "session_id": "af55764a-e283-4746-87a7-6c5affc3b275",
  "total_cost_usd": 0.55136975,
  "usage": {
    "input_tokens": 838,
    "cache_creation_input_tokens": 21531,
    "cache_read_input_tokens": 150774,
    "output_tokens": 2826,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21531,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 3,
        "output_tokens": 1899,
        "cache_read_input_tokens": 32118,
        "cache_creation_input_tokens": 1254,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1254
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 154819,
      "outputTokens": 4351,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 9,
      "costUSD": 0.26657400000000003,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 838,
      "outputTokens": 2826,
      "cacheReadInputTokens": 150774,
      "cacheCreationInputTokens": 21531,
      "webSearchRequests": 0,
      "costUSD": 0.28479574999999996,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "0a6c043e-bb22-40cc-8ff5-6b42da0cff87"
}
```

</details>

---
