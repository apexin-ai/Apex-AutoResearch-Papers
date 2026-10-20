# Research conversation: <agent_context> 项目 cost-verify-agent-rl：基于 Self-Guide + RAGEN 框架。exp_001 训练 step 2-6 advantage/pg_loss=0（16 episodes 全部  — Part 2 of 2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction (July export snapshot)** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../research-conversation-agent-context-cost-verify-agent-rl-self-guide-ragen-exp-001-step-2-6-advantage.md) · [Structured JSON](../../../sessions/4f/4f789db6c40bd72d88fa.json)

## Round 1

### Assistant

_source line 253 · 2026-05-13T19:22:32.244Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me now fix the max_model_len in _alfworld_exp001b.yaml (the latest one). Let me also note my findings:

## Complete Analysis

### 1. RAGEN Official ALFWorld Config vs Our Config

RAGEN has **NO official ALFWorld training config**. The numbered configs are: `_1_bandit`, `_2_sokoban`, `_3_frozen_lake`, `_4_countdown`, `_5_metamathqa`, `_6_webshop`, `_7_lean`, `_8_sudoku`, `_9_2048`, `_9_search`, `_10_rubikscube`, `_10_deepcoder`.


ALFWorld environment code exists in the codebase and the environments are registered, but there's no official training configuration for it. Looking at the key differences between the base defaults and our experiment setup, I notice a critical mismatch: we're using Qwen3-1.7B (base model) instead of the Qwen2.5-3B-Instruct that base.yaml specifies, and the max_model_len parameter needs adjustment.

Examining the rest of the configuration changes, I see we've made several modifications for ALFWorld specifically—increasing max_turn to 10 since the environment requires more interaction steps, reducing batch sizes significantly (env_groups from 8 to 4, group_size from 16 to 4), and switching from PPO's GAE to GRPO with its corresponding loss aggregation mode. The micro_batch_size stays at 1 per GPU, but ppo_mini_batch_size drops to 16, and we're constraining actions to 1 per turn.

Looking at the reward structure, the environment gives a binary 10.0 points for success and 0 otherwise with no intermediate rewards, while the format penalty applies -0.1 per turn whenever action parsing fails, accumulating across all turns.

The final reward gets normalized through GRPO's advantage calculation: for each group of 4 samples sharing the same prompt, it computes (R - mean(R)) / std(R). When all rollouts in a group fail, they all get the same reward (like -1.0), making the standard deviation zero and collapsing the advantage to zero—which explains why there's no gradient signal when the model consistently fails.

The dry-run confirmed this with a mean score of -0.9625, reflecting that most episodes accumulate around 9-10 format penalties of -0.1 each because the model struggles with the `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` format structure.

RAGEN doesn't have a built-in SFT or warm-start mechanism for ALFWorld—the entire training starts from zero-shot RL using the model's existing capabilities.

The framework defaults to Qwen2.5-3B-Instruct, which is designed to follow chat formats and understand the structured tags. Using Qwen3-1.7B, a base model that doesn't comprehend these instructions or tag formats, is why it's generating random completions instead of valid actions.

The system prompt requires the model to produce self-assessments, reasoning within specific XML tags, and select from admissible actions—a level of instruction-following that base models simply can't perform. The response parser looks for the `&lt;think>/&lt;answer>` pattern, and when it doesn't find it (which happens almost every time with the base model), it returns an empty action list, triggering a format penalty of -0.1 per turn and causing the episode to fail.

This creates a bootstrap problem: the base model generates random text without the required tags, the parser finds nothing, no valid actions reach the environment, and every rollout ends up with a total reward around -1.0. Since GRPO normalizes rewards within groups and all four rollouts get the same penalty, there's zero variance and zero gradient signal to learn from.

The solution is straightforward—switch to an instruction-tuned model like Qwen3-1.7B-Instruct or Qwen2.5-3B-Instruct that can actually follow the formatting requirements. Now I'm updating the max_model_len parameter across both experiment configuration files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9c7256d-f9b8-4b09-bdad-d0cf7be2ce32",
  "isSidechain": false,
  "requestId": "req_011Cb17QriXnEHaDZyWuf5aj",
  "type": "assistant",
  "uuid": "fa372772-84f4-445a-b241-9fd98be52957",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxQrtpphbxpdwi4Z52Pujg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3328,
      "cache_read_input_tokens": 89628,
      "output_tokens": 2290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2290,
          "cache_read_input_tokens": 89628,
          "cache_creation_input_tokens": 3328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Assistant

_source line 254 · 2026-05-13T19:22:32.378Z_

调研完成。现在修复 `max_model_len`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa372772-84f4-445a-b241-9fd98be52957",
  "isSidechain": false,
  "requestId": "req_011Cb17QriXnEHaDZyWuf5aj",
  "type": "assistant",
  "uuid": "77a76fa9-9260-4879-850e-1e8ff77fae59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxQrtpphbxpdwi4Z52Pujg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3328,
      "cache_read_input_tokens": 89628,
      "output_tokens": 2290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2290,
          "cache_read_input_tokens": 89628,
          "cache_creation_input_tokens": 3328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 255 · 2026-05-13T19:22:35.055Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_execute · `toolu_015rd9WFEWHx2UbMtsZc6usB`</summary>

```json
{
  "server": "bjb1-17606",
  "command": "sed -i 's/max_model_len: 4096/max_model_len: 16384/' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp001.yaml && sed -i 's/max_model_len: 8192/max_model_len: 16384/' /root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp001b.yaml && echo \"DONE\"",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "77a76fa9-9260-4879-850e-1e8ff77fae59",
  "isSidechain": false,
  "requestId": "req_011Cb17QriXnEHaDZyWuf5aj",
  "type": "assistant",
  "uuid": "8ad34151-0539-49ff-b100-4f29ca6b3b90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VxQrtpphbxpdwi4Z52Pujg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3328,
      "cache_read_input_tokens": 89628,
      "output_tokens": 2290,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2290,
          "cache_read_input_tokens": 89628,
          "cache_creation_input_tokens": 3328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 256 · 2026-05-13T19:22:35.424Z_

<details><summary>↩ Tool result · `toolu_015rd9WFEWHx2UbMtsZc6usB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8ad34151-0539-49ff-b100-4f29ca6b3b90",
  "isSidechain": false,
  "promptId": "24c04077-24c6-4093-bf72-7ef6193859a1",
  "type": "user",
  "uuid": "76607f90-1eae-4103-a1aa-6f0206376b38",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"DONE\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"DONE\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "8ad34151-0539-49ff-b100-4f29ca6b3b90",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Runtime record

_source line 257 · 2026-05-13T19:22:35.429Z_

```json
{
  "parentUuid": "76607f90-1eae-4103-a1aa-6f0206376b38",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "0e6ec74c-d2eb-4f6f-b714-b3ba100aad3d",
  "timestamp": "2026-05-13T19:22:35.429Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---


### Assistant

_source line 258 · 2026-05-13T19:22:38.650Z_

验证修改。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e6ec74c-d2eb-4f6f-b714-b3ba100aad3d",
  "isSidechain": false,
  "requestId": "req_011Cb17UzmLJRh3HdXEqBBjj",
  "type": "assistant",
  "uuid": "0cb0c248-0125-4f49-aed1-4c88344fbb3a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqRYoubcr9r1sKn8DGZCGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 92956,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 92956,
          "cache_creation_input_tokens": 2466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2466
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool call

_source line 259 · 2026-05-13T19:22:39.596Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_01Q3KTJZBEhR6g7KJ4rQo3uj`</summary>

```json
{
  "server": "bjb1-17606",
  "command": "grep \"max_model_len\" /root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp001.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cb0c248-0125-4f49-aed1-4c88344fbb3a",
  "isSidechain": false,
  "requestId": "req_011Cb17UzmLJRh3HdXEqBBjj",
  "type": "assistant",
  "uuid": "fc548ae5-024a-4ed4-936a-f54f3b0a0268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqRYoubcr9r1sKn8DGZCGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 92956,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 92956,
          "cache_creation_input_tokens": 2466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2466
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 260 · 2026-05-13T19:22:39.956Z_

<details><summary>↩ Tool result · `toolu_01Q3KTJZBEhR6g7KJ4rQo3uj`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    max_model_len: 16384\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc548ae5-024a-4ed4-936a-f54f3b0a0268",
  "isSidechain": false,
  "promptId": "24c04077-24c6-4093-bf72-7ef6193859a1",
  "type": "user",
  "uuid": "6d19c019-237f-4f76-b968-b21f871f8b27",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    max_model_len: 16384\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.35}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    max_model_len: 16384\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.35}}"
    }
  },
  "sourceToolAssistantUUID": "fc548ae5-024a-4ed4-936a-f54f3b0a0268",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Tool call

_source line 261 · 2026-05-13T19:22:39.958Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__ssh_read_only · `toolu_014mXWBBThxJSRfJnBg4eRMy`</summary>

```json
{
  "server": "bjb1-17606",
  "command": "grep \"max_model_len\" /root/cost-verify-agent-rl/RAGEN/config/_alfworld_exp001b.yaml",
  "account": "root"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6d19c019-237f-4f76-b968-b21f871f8b27",
  "isSidechain": false,
  "requestId": "req_011Cb17UzmLJRh3HdXEqBBjj",
  "type": "assistant",
  "uuid": "94d9eb4f-8ae2-4c92-a67e-53e1a3d24224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LqRYoubcr9r1sKn8DGZCGi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2466,
      "cache_read_input_tokens": 92956,
      "output_tokens": 260,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2466,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 260,
          "cache_read_input_tokens": 92956,
          "cache_creation_input_tokens": 2466,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2466
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Tool result

_source line 262 · 2026-05-13T19:22:40.378Z_

<details><summary>↩ Tool result · `toolu_014mXWBBThxJSRfJnBg4eRMy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"stdout\": \"    max_model_len: 16384\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "94d9eb4f-8ae2-4c92-a67e-53e1a3d24224",
  "isSidechain": false,
  "promptId": "24c04077-24c6-4093-bf72-7ef6193859a1",
  "type": "user",
  "uuid": "0c668583-d759-41f1-a3e4-21634bc6bf07",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"stdout\\\": \\\"    max_model_len: 16384\\\\n\\\", \\\"stderr\\\": \\\"\\\", \\\"return_code\\\": 0}, \\\"error\\\": null, \\\"metadata\\\": {\\\"elapsed_seconds\\\": 0.41}}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"stdout\": \"    max_model_len: 16384\\n\", \"stderr\": \"\", \"return_code\": 0}, \"error\": null, \"metadata\": {\"elapsed_seconds\": 0.41}}"
    }
  },
  "sourceToolAssistantUUID": "94d9eb4f-8ae2-4c92-a67e-53e1a3d24224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---


### Assistant

_source line 263 · 2026-05-13T19:23:02.842Z_

---

## 调研结果

### 1. RAGEN 官方 ALFWorld Config vs 我们的差异

**RAGEN 没有官方 ALFWorld training config。** 只有环境定义（`envs.yaml` 中的 `Alfworld`/`AlfworldOOD`/`AlfworldSG`），无对应的训练 yaml。所有 `_alfworld_*.yaml` 都是我们写的。

与 base.yaml 默认值对比：

| 参数 | base.yaml 默认 | exp001 | 影响 |
|------|---------------|--------|------|
| **model_path** | `Qwen/Qwen2.5-3B-Instruct` | `Qwen3-1.7B` (base) | **致命问题** |
| train group_size | 16 | 4 | 样本太少 |
| train env_groups | 8 | 4 | 样本太少 |
| max_model_len | 3600 | 4096→16384 (已修) | 已修复 |
| adv_estimator | gae (PPO) | grpo | 不同算法 |
| max_turn | 5 | 10 | ALFWorld 需要多步 |
| max_actions_per_turn | 2 | 1 | OK |

### 2. Reward Function 详细说明

**三层结构：**

- **环境层（env.py）**：纯 0/1 sparse reward → `reward = 10.0 * float(won)`。只有任务完成才给 +10，中间无任何 partial reward。
- **Format penalty（es_manager.py）**：每个 turn 如果 action 解析失败（`_parse_response` 匹配不到 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式），`penalty += -0.1`。10 个 turn 全失败 = -1.0。
- **最终 reward**：`env_reward + accumulated_penalty`。exp_001 中模型完全不输出正确格式 → 每个 episode reward ≈ 0 + (-1.0) = -1.0。

**为什么 advantage = 0：** GRPO 在 group 内归一化 `(R - mean) / std`。group_size=4，4 个 rollout 都得 -1.0 → std = 0 → advantage = 0 → 无梯度。

### 3. SFT/Warm-start 机制

**不存在。** RAGEN 框架无内置 SFT/warm-start。verl 子模块有 SFT trainer 但 RAGEN 训练流程不使用。整个方案依赖模型零样本能力。

### 4. Instruct vs Base 模型

**RAGEN 所有官方配置使用 Instruct 模型**（`Qwen2.5-3B-Instruct`）。框架假定模型已具备：
- 遵循 `&lt;think>...&lt;/think>&lt;answer>...&lt;/answer>` 格式
- 理解 system prompt 中的任务指令
- 从 admissible actions 列表中选择有效 action

**Qwen3-1.7B 是 base 模型**，不理解 chat 格式，不遵循指令，输出随机文本。

### 5. max_model_len 修复

两个配置文件已修改为 16384：
- `_alfworld_exp001.yaml`: 4096 → 16384
- `_alfworld_exp001b.yaml`: 8192 → 16384

### 6. Bootstrap 问题根因分析与修复建议

**根因链路：**
1. Base 模型不遵循指令 → 不输出 `&lt;think>/&lt;answer>` 格式
2. `_parse_response` 返回空 actions → format_penalty 累积
3. 无有效 action 到达环境 → env reward 恒为 0
4. 每个 episode 总 reward ≈ -1.0，group 内全部相同
5. GRPO 归一化 std=0 → advantage=0 → 零梯度

**修复方案（优先级排序）：**

1. **P0: 换 Instruct 模型**。下载 `Qwen3-1.7B-Instruct` 或 `Qwen2.5-3B-Instruct`。这是唯一能立即解决零梯度问题的方案。
2. **P1: 增大 group_size**。从 4 增到 16（匹配 base.yaml 默认值）。更大的 group 增加出现 reward 方差的概率。
3. **P2: 如果坚持用 base 模型**——需要 SFT warm-start：用少量 `&lt;think>reasoning&lt;/think>&lt;answer>valid_action&lt;/answer>` 样本微调，让模型学会格式。但这偏离了 RAGEN 的设计假设。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c668583-d759-41f1-a3e4-21634bc6bf07",
  "isSidechain": false,
  "requestId": "req_011Cb17VMvJxovQw3EM8W2hD",
  "type": "assistant",
  "uuid": "56ecdf20-d3bf-4a76-8206-d559dfecc72b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_1/projects/cost-verify-agent-rl",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017mGz6y5izkerkjVdMb7ZSk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 491,
      "cache_read_input_tokens": 95422,
      "output_tokens": 1366,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 491,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1366,
          "cache_read_input_tokens": 95422,
          "cache_creation_input_tokens": 491,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 491
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---


### Runtime record

_source line 264_

```json
{
  "type": "last-prompt",
  "leafUuid": "56ecdf20-d3bf-4a76-8206-d559dfecc72b",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194"
}
```

---


### Runtime record

_source line 265_

```json
{
  "type": "ai-title",
  "aiTitle": "Debug RAGEN ALFWorld zero-reward issue and bootstrap mechanism",
  "sessionId": "d96ae929-2e6d-4196-bf72-c1b16b337194"
}
```

---
