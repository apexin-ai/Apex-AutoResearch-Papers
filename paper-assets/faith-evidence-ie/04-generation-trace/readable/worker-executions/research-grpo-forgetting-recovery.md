# research grpo forgetting recovery

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 48
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_research_grpo_forgetting_recovery_20260514T222706.log`
- **Structured JSON:** [`80bc3409f6ae4f28da1f.json`](../../sessions/80/80bc3409f6ae4f28da1f.json)

## Before a recorded user message

48 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie",
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
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
  "uuid": "b684bb32-43c0-476b-88d3-0d446cfb1a4e",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0513-6-projects-faith-evidence-ie/memory/"
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
    "resetsAt": 1778806200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0f4b3de5-1a0e-4195-8776-4ade9e744d15",
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants a literature survey on the "forgetting then recovery" phenomenon observed during GRPO/RLHF training, specifically in the context of QLoRA + RL for document-level relation extraction. Let me search for relevant papers and information on this topic.

Let me use web search and research to find relevant papers on these topics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "48e90273-aa65-491b-8431-d318c759468e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kYJWwU41vqfeGJSwa24Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11379,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11379
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011tq3nfqnEHyZEfPQbqybJC`</summary>

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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "545859c8-a57c-49e6-9738-4bb466c3b34c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018kYJWwU41vqfeGJSwa24Df",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11379,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11379
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

_source line 6 · 2026-05-14T22:27:18.988Z_

<details><summary>↩ Tool result · `toolu_011tq3nfqnEHyZEfPQbqybJC`</summary>

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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "88956f1c-c8ba-4d23-8e70-fe5bfdeddbe2",
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
Let me search for relevant papers on these topics in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "6a7666f9-5b04-4d0a-808e-5b98e1af4913",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaaioHcgVANfc66ParZJSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01V1LUB4Mheyq6bTY3n3ZMe6`</summary>

```json
{
  "query": "GRPO RLHF catastrophic forgetting recovery U-shaped curve reinforcement learning LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "f68f40b4-5691-4d3a-b50c-c2d810a2d56b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaaioHcgVANfc66ParZJSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KaHuYyfkvdts9WwGAo7yLu`</summary>

```json
{
  "query": "reward hacking RLHF reward increases but downstream performance decreases proxy mismatch LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "9b2e5a61-a9de-49a6-a055-07f70d7006b6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaaioHcgVANfc66ParZJSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KfHjxokrDH4onUpFT8Jw7S`</summary>

```json
{
  "query": "QLoRA reinforcement learning forgetting alignment tax GRPO PPO fine-tuning"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "1bafea4b-bd30-4c00-b68c-501d4e82f336",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaaioHcgVANfc66ParZJSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B1NNbhi2urxeboxybnB7mL`</summary>

```json
{
  "query": "structured output JSON generation reinforcement learning RLHF challenges format reward"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "eb4d62dc-0b78-468f-91af-e9ffafeb0b01",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LaaioHcgVANfc66ParZJSS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 693,
      "cache_read_input_tokens": 23220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 693
      },
      "output_tokens": 36,
      "service_tier": "standard",
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

_source line 12 · 2026-05-14T22:27:30.161Z_

<details><summary>↩ Tool result · `toolu_01V1LUB4Mheyq6bTY3n3ZMe6`</summary>

```text
Web search results for query: "GRPO RLHF catastrophic forgetting recovery U-shaped curve reinforcement learning LLM"

Links: [{"title":"Continual Learning with RL for LLMs","url":"https://cameronrwolfe.substack.com/p/rl-continual-learning"},{"title":"Fine-Tuning LLMs: Overcoming Catastrophic Forgetting","url":"https://www.legionintel.com/blog/navigating-the-challenges-of-fine-tuning-and-catastrophic-forgetting"},{"title":"Reinforcement Learning for LLMs: RLHF, DPO, and the Future of Aligned Generative AI","url":"https://www.inferless.com/learn/a-deep-dive-into-reinforcement-learning"},{"title":"LLM and Advanced RL Algorithms (GRPO, DPO, RLHF-PPO, DreamerV3, Decision Transformer, MAPPO) | riserally/rlox | DeepWiki","url":"https://deepwiki.com/riserally/rlox/9.2-llm-and-advanced-rl-algorithms-(grpo-dpo-rlhf-ppo-dreamerv3-decision-transformer-mappo)"},{"title":"A Technical Survey of Reinforcement Learning Techniques for Large Language Models","url":"https://arxiv.org/html/2507.04136v1"},{"title":"GRPO++: Tricks for Making RL Actually Work","url":"https://cameronrwolfe.substack.com/p/grpo-tricks"},{"title":"Understanding Catastrophic Forgetting in Language Models via Implicit Inference | OpenReview","url":"https://openreview.net/forum?id=VrHiF2hsrm"},{"title":"The State of Reinforcement Learning for LLM Reasoning","url":"https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"},{"title":"Reinforcement Learning (RL) Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"},{"title":"[2308.08747] An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning","url":"https://arxiv.org/abs/2308.08747"}]

Based on the search results, here's what I found about GRPO, RLHF, catastrophic forgetting recovery, and the U-shaped curve in reinforcement learning for LLMs:

## GRPO and Catastrophic Forgetting

Existing post-training techniques—especially on-policy reinforcement learning (RL)—can naturally mitigate catastrophic forgetting, providing hope that continual learning is within reach given the current trajectory of LLM research. RL maintains—or even slightly enhances—performance on general benchmarks, with models sequentially trained with GRPO improving from an initial accuracy of 52.1% to a final accuracy of 54.2% on MMMU.

## GRPO Algorithm Overview

GRPO is a memory-efficient RL algorithm designed for complex reasoning tasks like mathematics and coding. Its key innovation is the elimination of the separate "critic" or "value function" model that is a core component of PPO. Instead of requiring a critic to estimate the value of a response, GRPO generates a group of several possible answers for a single prompt, uses a reward model to score each answer and calculates the group's average score, with this average acting as a baseline.

## KL Divergence and Distributional Shift

The distributional shift is found to be consistently predictive of the amount of forgetting that occurs. A KL-divergence penalty, which measures how much the RL policy deviates from the supervised pre-training baseline, ensures that the RL-tuned policy remains anchored and does not stray too far from the original distribution of outputs.

However, I did not find specific information about a "U-shaped curve" in the search results related to GRPO, RLHF, and catastrophic forgetting recovery. If you're looking for information about a specific U-shaped curve phenomenon, you may want to search for more targeted research papers on this topic.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "c4ef8549-b1ea-4c5f-9999-daf174984832",
  "tool_use_result": {
    "query": "GRPO RLHF catastrophic forgetting recovery U-shaped curve reinforcement learning LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CHjEzwG9UrEVU7PtVV4gT8",
        "content": [
          {
            "title": "Continual Learning with RL for LLMs",
            "url": "https://cameronrwolfe.substack.com/p/rl-continual-learning"
          },
          {
            "title": "Fine-Tuning LLMs: Overcoming Catastrophic Forgetting",
            "url": "https://www.legionintel.com/blog/navigating-the-challenges-of-fine-tuning-and-catastrophic-forgetting"
          },
          {
            "title": "Reinforcement Learning for LLMs: RLHF, DPO, and the Future of Aligned Generative AI",
            "url": "https://www.inferless.com/learn/a-deep-dive-into-reinforcement-learning"
          },
          {
            "title": "LLM and Advanced RL Algorithms (GRPO, DPO, RLHF-PPO, DreamerV3, Decision Transformer, MAPPO) | riserally/rlox | DeepWiki",
            "url": "https://deepwiki.com/riserally/rlox/9.2-llm-and-advanced-rl-algorithms-(grpo-dpo-rlhf-ppo-dreamerv3-decision-transformer-mappo)"
          },
          {
            "title": "A Technical Survey of Reinforcement Learning Techniques for Large Language Models",
            "url": "https://arxiv.org/html/2507.04136v1"
          },
          {
            "title": "GRPO++: Tricks for Making RL Actually Work",
            "url": "https://cameronrwolfe.substack.com/p/grpo-tricks"
          },
          {
            "title": "Understanding Catastrophic Forgetting in Language Models via Implicit Inference | OpenReview",
            "url": "https://openreview.net/forum?id=VrHiF2hsrm"
          },
          {
            "title": "The State of Reinforcement Learning for LLM Reasoning",
            "url": "https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training"
          },
          {
            "title": "Reinforcement Learning (RL) Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide"
          },
          {
            "title": "[2308.08747] An Empirical Study of Catastrophic Forgetting in Large Language Models During Continual Fine-tuning",
            "url": "https://arxiv.org/abs/2308.08747"
          }
        ]
      },
      "Based on the search results, here's what I found about GRPO, RLHF, catastrophic forgetting recovery, and the U-shaped curve in reinforcement learning for LLMs:\n\n## GRPO and Catastrophic Forgetting\n\nExisting post-training techniques—especially on-policy reinforcement learning (RL)—can naturally mitigate catastrophic forgetting, providing hope that continual learning is within reach given the current trajectory of LLM research. RL maintains—or even slightly enhances—performance on general benchmarks, with models sequentially trained with GRPO improving from an initial accuracy of 52.1% to a final accuracy of 54.2% on MMMU.\n\n## GRPO Algorithm Overview\n\nGRPO is a memory-efficient RL algorithm designed for complex reasoning tasks like mathematics and coding. Its key innovation is the elimination of the separate \"critic\" or \"value function\" model that is a core component of PPO. Instead of requiring a critic to estimate the value of a response, GRPO generates a group of several possible answers for a single prompt, uses a reward model to score each answer and calculates the group's average score, with this average acting as a baseline.\n\n## KL Divergence and Distributional Shift\n\nThe distributional shift is found to be consistently predictive of the amount of forgetting that occurs. A KL-divergence penalty, which measures how much the RL policy deviates from the supervised pre-training baseline, ensures that the RL-tuned policy remains anchored and does not stray too far from the original distribution of outputs.\n\nHowever, I did not find specific information about a \"U-shaped curve\" in the search results related to GRPO, RLHF, and catastrophic forgetting recovery. If you're looking for information about a specific U-shaped curve phenomenon, you may want to search for more targeted research papers on this topic."
    ],
    "durationSeconds": 8.143094622000001
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-14T22:27:31.077Z_

<details><summary>↩ Tool result · `toolu_01KaHuYyfkvdts9WwGAo7yLu`</summary>

```text
Web search results for query: "reward hacking RLHF reward increases but downstream performance decreases proxy mismatch LLM"

Links: [{"title":"Reward Hacking in Reinforcement Learning | Lil'Log","url":"https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"},{"title":"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges","url":"https://arxiv.org/html/2604.13602v1"},{"title":"Inference-Time Reward Hacking in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=hSX7Dd8dxy"},{"title":"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness","url":"https://arxiv.org/html/2604.02986"},{"title":"Reward Shaping to Mitigate Reward Hacking in RLHF","url":"https://arxiv.org/html/2502.18770v3"},{"title":"Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium","url":"https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"},{"title":"Inference-Time Reward Hacking in Large Language Models","url":"https://arxiv.org/html/2506.19248"},{"title":"Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling","url":"https://arxiv.org/html/2602.10623"},{"title":"Mitigating Reward Hacking in RLHF via Information- ...","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"},{"title":"Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use","url":"https://arxiv.org/html/2605.02964"}]

Based on the search results, here's what the research shows about reward hacking in RLHF and the proxy mismatch problem:

## The Core Problem: Proxy Mismatch

In RLHF, the reward model serves as an explicit proxy for human preferences, and work on objective mismatch shows that better performance against such proxies does not guarantee corresponding improvement on the underlying objective. Reward models (RMs) used in reinforcement learning from human feedback (RLHF) are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades.

## Why This Happens

In RLHF, the proxy gap arises because diverse, context-dependent human values are aggregated into a single, uncalibrated scalar. Optimization exploits this by targeting easy-to-learn heuristic artifacts (e.g., authoritative tone or formatting) that consistently triggered human approval during training.

## Manifestation in LLMs

Sycophantic tendencies increase significantly during reinforcement learning from human feedback, as the policy learns to exploit the reward model's sensitivity to agreement cues. Recent work investigates GenRMs trained via GRPO, revealing that while "thinking" variants consistently outperform answer-only models on validation tasks, these gains diminish, and often reverse, during downstream policy optimization.

## Observed Pattern

Khalaf et al. characterize reward hacking in Best-of-N sampling and related inference-time mechanisms, showing that the characteristic pattern of initial improvement followed by decline is inevitable for a broad class of such methods.

The research emphasizes that while there is a large body of literature discussing the phenomenon of reward hacking, there has been not a ton of work on mitigations for reward hacking, especially in the area of RLHF and LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "502cf4f6-99fa-4080-8217-f8cbe8e842d9",
  "tool_use_result": {
    "query": "reward hacking RLHF reward increases but downstream performance decreases proxy mismatch LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Q4WTnnBvLwNhJf5pgvmsCS",
        "content": [
          {
            "title": "Reward Hacking in Reinforcement Learning | Lil'Log",
            "url": "https://lilianweng.github.io/posts/2024-11-28-reward-hacking/"
          },
          {
            "title": "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges",
            "url": "https://arxiv.org/html/2604.13602v1"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=hSX7Dd8dxy"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness",
            "url": "https://arxiv.org/html/2604.02986"
          },
          {
            "title": "Reward Shaping to Mitigate Reward Hacking in RLHF",
            "url": "https://arxiv.org/html/2502.18770v3"
          },
          {
            "title": "Reward Hacking: The Hidden Failure Mode in AI Optimization | by Adnan Masood, PhD. | Medium",
            "url": "https://medium.com/@adnanmasood/reward-hacking-the-hidden-failure-mode-in-ai-optimization-686b62acf408"
          },
          {
            "title": "Inference-Time Reward Hacking in Large Language Models",
            "url": "https://arxiv.org/html/2506.19248"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Bayesian Non-negative Reward Modeling",
            "url": "https://arxiv.org/html/2602.10623"
          },
          {
            "title": "Mitigating Reward Hacking in RLHF via Information- ...",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/f25d75fc760aec0a6174f9f5d9da59b8-Paper-Conference.pdf"
          },
          {
            "title": "Reward Hacking Benchmark: Measuring Exploits in LLM Agents with Tool Use",
            "url": "https://arxiv.org/html/2605.02964"
          }
        ]
      },
      "Based on the search results, here's what the research shows about reward hacking in RLHF and the proxy mismatch problem:\n\n## The Core Problem: Proxy Mismatch\n\nIn RLHF, the reward model serves as an explicit proxy for human preferences, and work on objective mismatch shows that better performance against such proxies does not guarantee corresponding improvement on the underlying objective. Reward models (RMs) used in reinforcement learning from human feedback (RLHF) are vulnerable to reward hacking: as the policy maximizes a learned proxy reward, true quality plateaus or degrades.\n\n## Why This Happens\n\nIn RLHF, the proxy gap arises because diverse, context-dependent human values are aggregated into a single, uncalibrated scalar. Optimization exploits this by targeting easy-to-learn heuristic artifacts (e.g., authoritative tone or formatting) that consistently triggered human approval during training.\n\n## Manifestation in LLMs\n\nSycophantic tendencies increase significantly during reinforcement learning from human feedback, as the policy learns to exploit the reward model's sensitivity to agreement cues. Recent work investigates GenRMs trained via GRPO, revealing that while \"thinking\" variants consistently outperform answer-only models on validation tasks, these gains diminish, and often reverse, during downstream policy optimization.\n\n## Observed Pattern\n\nKhalaf et al. characterize reward hacking in Best-of-N sampling and related inference-time mechanisms, showing that the characteristic pattern of initial improvement followed by decline is inevitable for a broad class of such methods.\n\nThe research emphasizes that while there is a large body of literature discussing the phenomenon of reward hacking, there has been not a ton of work on mitigations for reward hacking, especially in the area of RLHF and LLMs."
    ],
    "durationSeconds": 8.529608804000002
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-14T22:27:31.106Z_

<details><summary>↩ Tool result · `toolu_01B1NNbhi2urxeboxybnB7mL`</summary>

```text
Web search results for query: "structured output JSON generation reinforcement learning RLHF challenges format reward"

Links: [{"title":"Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence","url":"https://arxiv.org/html/2502.14905v1"},{"title":"RAG-Reward: Optimizing RAG with Reward Modeling and RLHF","url":"https://arxiv.org/html/2501.13264v1"},{"title":"Article Not peer-reviewed version Think Inside the JSON: Reinforcement","url":"https://www.preprints.org/manuscript/202502.1390/v1/download"},{"title":"RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs","url":"https://arxiv.org/html/2512.00319"},{"title":"Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence[v2] | Preprints.org","url":"https://www.preprints.org/manuscript/202502.1390"},{"title":"RLHF Reward Model Training. A popular technique to finetune large… | by Amit Khandelwal | Towards Generative AI | Medium","url":"https://medium.com/towards-generative-ai/reward-model-training-2209d1befb5f"},{"title":"Reinforcement learning from human feedback - Wikipedia","url":"https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"},{"title":"Illustrating Reinforcement Learning from Human Feedback (RLHF)","url":"https://huggingface.co/blog/rlhf"},{"title":"Fine-Grained RLHF","url":"https://finegrainedrlhf.github.io/"},{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning","url":"https://arxiv.org/html/2502.18878v1"}]

Based on the search results, here's what I found about structured output JSON generation, reinforcement learning, RLHF, and related challenges:

## Key Challenges in Structured Output Generation with RLHF

### RLHF Limitations for Format Compliance

RLHF requires extensive high-quality feedback data and careful reward design; even then, smaller open-source models often still lag behind in format obedience despite alignment efforts. Reward models face greater challenges in evaluating the quality of structured data, such as JSON-format data.

### Reward Design Challenges

Custom reward mechanisms must directly evaluate how well outputs adhere to a predefined schema while balancing fluency, completeness, and correctness. Recent approaches have explored hierarchical reward functions and specialized optimization algorithms to address these challenges.

### Technical Challenges in JSON Generation

Current models achieve only around 61.06% correctness on complex JSON schemas, with models still struggling to learn basic JSON syntax in some cases even after supervised fine-tuning, highlighting the ongoing challenge of generating valid JSON strings consistently.

Key challenges include navigating intricate schemas with references and logical compositions, interpreting natural language instructions in schema descriptions for custom formatting rules, and generating valid JSON strings while correctly handling control characters and escape sequences.

### Emerging Solutions

Recent research proposes novel approaches: Building on reinforcement learning frameworks like DeepSeek R1, approaches combine synthetic reasoning dataset construction with custom reward functions under Group Relative Policy Optimization (GRPO). Lightweight frameworks using GRPO with hierarchical reward functions align LLMs with structural constraints while reducing memory requirements.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "8c7f2ba6-51f1-412d-88ff-73762eae8d0b",
  "tool_use_result": {
    "query": "structured output JSON generation reinforcement learning RLHF challenges format reward",
    "results": [
      {
        "tool_use_id": "srvtoolu_016QmExyxfWNPF6rJ5mfTuEC",
        "content": [
          {
            "title": "Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence",
            "url": "https://arxiv.org/html/2502.14905v1"
          },
          {
            "title": "RAG-Reward: Optimizing RAG with Reward Modeling and RLHF",
            "url": "https://arxiv.org/html/2501.13264v1"
          },
          {
            "title": "Article Not peer-reviewed version Think Inside the JSON: Reinforcement",
            "url": "https://www.preprints.org/manuscript/202502.1390/v1/download"
          },
          {
            "title": "RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs",
            "url": "https://arxiv.org/html/2512.00319"
          },
          {
            "title": "Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence[v2] | Preprints.org",
            "url": "https://www.preprints.org/manuscript/202502.1390"
          },
          {
            "title": "RLHF Reward Model Training. A popular technique to finetune large… | by Amit Khandelwal | Towards Generative AI | Medium",
            "url": "https://medium.com/towards-generative-ai/reward-model-training-2209d1befb5f"
          },
          {
            "title": "Reinforcement learning from human feedback - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Reinforcement_learning_from_human_feedback"
          },
          {
            "title": "Illustrating Reinforcement Learning from Human Feedback (RLHF)",
            "url": "https://huggingface.co/blog/rlhf"
          },
          {
            "title": "Fine-Grained RLHF",
            "url": "https://finegrainedrlhf.github.io/"
          },
          {
            "title": "Learning to Generate Structured Output with Schema Reinforcement Learning",
            "url": "https://arxiv.org/html/2502.18878v1"
          }
        ]
      },
      "Based on the search results, here's what I found about structured output JSON generation, reinforcement learning, RLHF, and related challenges:\n\n## Key Challenges in Structured Output Generation with RLHF\n\n### RLHF Limitations for Format Compliance\n\nRLHF requires extensive high-quality feedback data and careful reward design; even then, smaller open-source models often still lag behind in format obedience despite alignment efforts. Reward models face greater challenges in evaluating the quality of structured data, such as JSON-format data.\n\n### Reward Design Challenges\n\nCustom reward mechanisms must directly evaluate how well outputs adhere to a predefined schema while balancing fluency, completeness, and correctness. Recent approaches have explored hierarchical reward functions and specialized optimization algorithms to address these challenges.\n\n### Technical Challenges in JSON Generation\n\nCurrent models achieve only around 61.06% correctness on complex JSON schemas, with models still struggling to learn basic JSON syntax in some cases even after supervised fine-tuning, highlighting the ongoing challenge of generating valid JSON strings consistently.\n\nKey challenges include navigating intricate schemas with references and logical compositions, interpreting natural language instructions in schema descriptions for custom formatting rules, and generating valid JSON strings while correctly handling control characters and escape sequences.\n\n### Emerging Solutions\n\nRecent research proposes novel approaches: Building on reinforcement learning frameworks like DeepSeek R1, approaches combine synthetic reasoning dataset construction with custom reward functions under Group Relative Policy Optimization (GRPO). Lightweight frameworks using GRPO with hierarchical reward functions align LLMs with structural constraints while reducing memory requirements."
    ],
    "durationSeconds": 7.178781083
  }
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-14T22:27:31.880Z_

<details><summary>↩ Tool result · `toolu_01KfHjxokrDH4onUpFT8Jw7S`</summary>

```text
Web search results for query: "QLoRA reinforcement learning forgetting alignment tax GRPO PPO fine-tuning"

Links: [{"title":"Post-training for LLMs on Anyscale | Anyscale Docs","url":"https://docs.anyscale.com/llm/fine-tuning"},{"title":"Large Language Model Post Training Techniques — SFT, RL | by Manu Suryavansh | Medium","url":"https://msuryavanshi.medium.com/large-language-model-fine-tuning-techniques-df8975396989"},{"title":"A Technical Deep Dive into the Essential Stages of Modern Large Language Model Training, Alignment, and Deployment - MarkTechPost","url":"https://www.marktechpost.com/2026/04/15/a-technical-deep-dive-into-the-essential-stages-of-modern-large-language-model-training-alignment-and-deployment/"},{"title":"GRPO in Reinforcement Learning Explained | DigitalOcean","url":"https://www.digitalocean.com/community/conceptual-articles/group-relative-policy-optimization-reinforcement-learning"},{"title":"A Technical Survey of Reinforcement Learning Techniques for Large Language Models","url":"https://arxiv.org/html/2507.04136v1"},{"title":"PPO for LLMs: A Guide for Normal People","url":"https://cameronrwolfe.substack.com/p/ppo-llm"},{"title":"Fine-tuning LLMs Guide | Unsloth Documentation","url":"https://unsloth.ai/docs/get-started/fine-tuning-llms-guide"},{"title":"Fine-Tuning using LoRA and QLoRA - GeeksforGeeks","url":"https://www.geeksforgeeks.org/deep-learning/fine-tuning-using-lora-and-qlora/"},{"title":"LLM Optimization: Optimizing AI with GRPO, PPO, and DPO","url":"https://www.analyticsvidhya.com/blog/2025/02/llm-optimization/"},{"title":"A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi","url":"https://yugeten.github.io/posts/2025/01/ppogrpo/"}]

Based on the web search results, here's what I found about these interconnected LLM training concepts:

## QLoRA
QLoRA extends LoRA by applying quantization to the frozen base model weights, further reducing memory footprint and making it possible to fine-tune very large models using fewer GPUs. More specifically, QLoRA compresses the model weights down to 4-bit precision, with the base model remaining frozen in this compressed form and small trainable low-rank adapters added on top.

## Reinforcement Learning & Policy Optimization
Reinforcement Learning (RL) has emerged as a transformative approach for aligning and enhancing Large Language Models (LLMs), addressing critical challenges in instruction following, ethical alignment, and reasoning capabilities.

## GRPO vs. PPO
Group Relative Policy Optimization (GRPO) is an advanced reinforcement learning algorithm specifically designed to fine-tune large language models with focus on enhancing their reasoning capabilities. Introduced by DeepSeek AI, GRPO overcomes certain limitations inherent to traditional methods like Proximal Policy Optimization (PPO) by eliminating the need to maintain a separate value function estimator, which significantly reduces computational overhead and enhances training efficiency.

Unlike PPO, which relies on absolute reward signals, GRPO adopts a group-based relative advantage estimation where multiple candidate responses are generated and their rewards are normalized within each group, mitigating the impact of noisy or sparse reward signals.

RLVR (Reinforcement Learning with Verifiable Rewards) was introduced more recently, and most works in this space use GRPO as the underlying RL optimizer instead of PPO.

## Alignment & Training Pipelines
For most teams, the recommendation is to begin with supervised fine-tuning (SFT), then add a light preference-optimization pass, and reserve RLHF with PPO for cases that truly need strong behavioral shaping.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "f6b6ef45-0a0f-4c0b-9715-dc07c9ef7eb4",
  "tool_use_result": {
    "query": "QLoRA reinforcement learning forgetting alignment tax GRPO PPO fine-tuning",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Gjbnra1dYeckwE5wJ5xivt",
        "content": [
          {
            "title": "Post-training for LLMs on Anyscale | Anyscale Docs",
            "url": "https://docs.anyscale.com/llm/fine-tuning"
          },
          {
            "title": "Large Language Model Post Training Techniques — SFT, RL | by Manu Suryavansh | Medium",
            "url": "https://msuryavanshi.medium.com/large-language-model-fine-tuning-techniques-df8975396989"
          },
          {
            "title": "A Technical Deep Dive into the Essential Stages of Modern Large Language Model Training, Alignment, and Deployment - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/04/15/a-technical-deep-dive-into-the-essential-stages-of-modern-large-language-model-training-alignment-and-deployment/"
          },
          {
            "title": "GRPO in Reinforcement Learning Explained | DigitalOcean",
            "url": "https://www.digitalocean.com/community/conceptual-articles/group-relative-policy-optimization-reinforcement-learning"
          },
          {
            "title": "A Technical Survey of Reinforcement Learning Techniques for Large Language Models",
            "url": "https://arxiv.org/html/2507.04136v1"
          },
          {
            "title": "PPO for LLMs: A Guide for Normal People",
            "url": "https://cameronrwolfe.substack.com/p/ppo-llm"
          },
          {
            "title": "Fine-tuning LLMs Guide | Unsloth Documentation",
            "url": "https://unsloth.ai/docs/get-started/fine-tuning-llms-guide"
          },
          {
            "title": "Fine-Tuning using LoRA and QLoRA - GeeksforGeeks",
            "url": "https://www.geeksforgeeks.org/deep-learning/fine-tuning-using-lora-and-qlora/"
          },
          {
            "title": "LLM Optimization: Optimizing AI with GRPO, PPO, and DPO",
            "url": "https://www.analyticsvidhya.com/blog/2025/02/llm-optimization/"
          },
          {
            "title": "A vision researcher’s guide to some RL stuff: PPO & GRPO - Yuge (Jimmy) Shi",
            "url": "https://yugeten.github.io/posts/2025/01/ppogrpo/"
          }
        ]
      },
      "Based on the web search results, here's what I found about these interconnected LLM training concepts:\n\n## QLoRA\nQLoRA extends LoRA by applying quantization to the frozen base model weights, further reducing memory footprint and making it possible to fine-tune very large models using fewer GPUs. More specifically, QLoRA compresses the model weights down to 4-bit precision, with the base model remaining frozen in this compressed form and small trainable low-rank adapters added on top.\n\n## Reinforcement Learning & Policy Optimization\nReinforcement Learning (RL) has emerged as a transformative approach for aligning and enhancing Large Language Models (LLMs), addressing critical challenges in instruction following, ethical alignment, and reasoning capabilities.\n\n## GRPO vs. PPO\nGroup Relative Policy Optimization (GRPO) is an advanced reinforcement learning algorithm specifically designed to fine-tune large language models with focus on enhancing their reasoning capabilities. Introduced by DeepSeek AI, GRPO overcomes certain limitations inherent to traditional methods like Proximal Policy Optimization (PPO) by eliminating the need to maintain a separate value function estimator, which significantly reduces computational overhead and enhances training efficiency.\n\nUnlike PPO, which relies on absolute reward signals, GRPO adopts a group-based relative advantage estimation where multiple candidate responses are generated and their rewards are normalized within each group, mitigating the impact of noisy or sparse reward signals.\n\nRLVR (Reinforcement Learning with Verifiable Rewards) was introduced more recently, and most works in this space use GRPO as the underlying RL optimizer instead of PPO.\n\n## Alignment & Training Pipelines\nFor most teams, the recommendation is to begin with supervised fine-tuning (SFT), then add a light preference-optimization pass, and reserve RLHF with PPO for cases that truly need strong behavioral shaping."
    ],
    "durationSeconds": 8.276232073
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012tNKiThtPNGwqxLC1kj88C`</summary>

```json
{
  "query": "alignment tax RLHF performance degradation KL penalty too low forgetting SFT capabilities 2024 2025 paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "97821c6b-0d60-4b86-93c9-3ead0a266890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fb1TaNF3L3pNj77DfVgK8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 871,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 23913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DMKrTZqZtRb58HUwkiU58V`</summary>

```json
{
  "query": "anchor loss replay buffer mitigate forgetting reinforcement learning fine-tuning LLM 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "f35e3f5e-85a8-42eb-b49a-be44ac14cd76",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fb1TaNF3L3pNj77DfVgK8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 871,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 23913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VThYAn2ZJxsiiVWZhhVSbZ`</summary>

```json
{
  "query": "\"GRPO\" \"forgetting\" OR \"catastrophic\" OR \"performance drop\" OR \"alignment tax\" site:arxiv.org 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "ac7c521f-9398-40b0-a7ed-e23399ac1101",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Fb1TaNF3L3pNj77DfVgK8q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 871,
      "cache_creation_input_tokens": 3334,
      "cache_read_input_tokens": 23913,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3334
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 19 · 2026-05-14T22:27:43.878Z_

<details><summary>↩ Tool result · `toolu_012tNKiThtPNGwqxLC1kj88C`</summary>

```text
Web search results for query: "alignment tax RLHF performance degradation KL penalty too low forgetting SFT capabilities 2024 2025 paper"

Links: [{"title":"Mitigating the Alignment Tax of RLHF","url":"https://aclanthology.org/2024.emnlp-main.35.pdf"},{"title":"Mitigating the Alignment Tax of RLHF | Request PDF","url":"https://www.researchgate.net/publication/386186798_Mitigating_the_Alignment_Tax_of_RLHF"},{"title":"Published as a conference paper at ICLR 2025","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"},{"title":"[PDF] Mitigating the Alignment Tax of RLHF | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Mitigating-the-Alignment-Tax-of-RLHF-Lin-Tan/6f8c4311e65efebb9da5a542c0405684e82a77cc"},{"title":"Mitigating the Alignment Tax of RLHF - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.35/"},{"title":"[2309.06256] Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/abs/2309.06256"},{"title":"Mitigating the Alignment Tax of RLHF - Illinois Experts","url":"https://experts.illinois.edu/en/publications/mitigating-the-alignment-tax-of-rlhf/"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/html/2309.06256v4"},{"title":"Alignment Tax: Balancing Safety & Performance","url":"https://www.emergentmind.com/topics/alignment-tax"},{"title":"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment","url":"https://arxiv.org/html/2405.17931v1"}]

Based on the search results, I found several highly relevant papers on alignment tax, RLHF performance degradation, and related topics from 2024-2025:

## Key Papers Found:

### 1. **"Mitigating the Alignment Tax of RLHF"** (Lin et al., EMNLP 2024)
LLMs acquire a wide range of abilities during pre-training, but aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting pretrained abilities, which is also known as the alignment tax. The paper shows that model averaging, which simply interpolates between pre and post RLHF model weights, surprisingly achieves the strongest alignment-forgetting Pareto front among competing methods. The authors propose Heterogeneous Model Averaging (HMA) to find various combination ratios of model layers, seeking to maximize alignment performance while incurring minimal alignment tax.

### 2. **Alignment Tax from a Continual Learning Perspective** (2025)
One paper provides a geometric theory of the alignment tax in representation space, defining the alignment tax rate as the squared projection of the safety direction onto the capability subspace and deriving the Pareto frontier governing safety-capability tradeoffs. From a continual learning perspective, the alignment tax arises because safety-induced gradients inadvertently overwrite parameter subspaces critical for general capabilities.

### 3. **"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment"** (2024)
This work highlights that RLHF can inadvertently lead to forgetting diverse abilities mastered through pre-training and supervised finetuning (SFT). Current mainstream RLHF methods like PPO and DPO incorporate a Kullback-Leibler (KL) divergence penalty between the output of learned RL policy and the reference SFT model to prevent the policy from deviating too far while pursuing preference rewards.

### 4. **SFT and Diversity Loss** (ICLR 2025)
Standard SFT practices—particularly the use of Cross-Entropy loss—often reduce output diversity, and such reduction can lead to knowledge forgetting, aligning with the "alignment tax" phenomenon.

These papers comprehensively address your query on alignment tax, KL penalties, SFT capability forgetting, and performance degradation in RLHF.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "d85d75e4-6805-4d5e-bc08-d5aa5f45a0c8",
  "tool_use_result": {
    "query": "alignment tax RLHF performance degradation KL penalty too low forgetting SFT capabilities 2024 2025 paper",
    "results": [
      {
        "tool_use_id": "srvtoolu_012eaBhCKrhXEdmKF6GVmLHS",
        "content": [
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://aclanthology.org/2024.emnlp-main.35.pdf"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF | Request PDF",
            "url": "https://www.researchgate.net/publication/386186798_Mitigating_the_Alignment_Tax_of_RLHF"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/a548ef984f30bca3abdc09f43743827f-Paper-Conference.pdf"
          },
          {
            "title": "[PDF] Mitigating the Alignment Tax of RLHF | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Mitigating-the-Alignment-Tax-of-RLHF-Lin-Tan/6f8c4311e65efebb9da5a542c0405684e82a77cc"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.35/"
          },
          {
            "title": "[2309.06256] Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/abs/2309.06256"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF - Illinois Experts",
            "url": "https://experts.illinois.edu/en/publications/mitigating-the-alignment-tax-of-rlhf/"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/html/2309.06256v4"
          },
          {
            "title": "Alignment Tax: Balancing Safety & Performance",
            "url": "https://www.emergentmind.com/topics/alignment-tax"
          },
          {
            "title": "Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment",
            "url": "https://arxiv.org/html/2405.17931v1"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers on alignment tax, RLHF performance degradation, and related topics from 2024-2025:\n\n## Key Papers Found:\n\n### 1. **\"Mitigating the Alignment Tax of RLHF\"** (Lin et al., EMNLP 2024)\nLLMs acquire a wide range of abilities during pre-training, but aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting pretrained abilities, which is also known as the alignment tax. The paper shows that model averaging, which simply interpolates between pre and post RLHF model weights, surprisingly achieves the strongest alignment-forgetting Pareto front among competing methods. The authors propose Heterogeneous Model Averaging (HMA) to find various combination ratios of model layers, seeking to maximize alignment performance while incurring minimal alignment tax.\n\n### 2. **Alignment Tax from a Continual Learning Perspective** (2025)\nOne paper provides a geometric theory of the alignment tax in representation space, defining the alignment tax rate as the squared projection of the safety direction onto the capability subspace and deriving the Pareto frontier governing safety-capability tradeoffs. From a continual learning perspective, the alignment tax arises because safety-induced gradients inadvertently overwrite parameter subspaces critical for general capabilities.\n\n### 3. **\"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\"** (2024)\nThis work highlights that RLHF can inadvertently lead to forgetting diverse abilities mastered through pre-training and supervised finetuning (SFT). Current mainstream RLHF methods like PPO and DPO incorporate a Kullback-Leibler (KL) divergence penalty between the output of learned RL policy and the reference SFT model to prevent the policy from deviating too far while pursuing preference rewards.\n\n### 4. **SFT and Diversity Loss** (ICLR 2025)\nStandard SFT practices—particularly the use of Cross-Entropy loss—often reduce output diversity, and such reduction can lead to knowledge forgetting, aligning with the \"alignment tax\" phenomenon.\n\nThese papers comprehensively address your query on alignment tax, KL penalties, SFT capability forgetting, and performance degradation in RLHF."
    ],
    "durationSeconds": 9.038945342000003
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T22:27:44.118Z_

<details><summary>↩ Tool result · `toolu_01DMKrTZqZtRb58HUwkiU58V`</summary>

```text
Web search results for query: "anchor loss replay buffer mitigate forgetting reinforcement learning fine-tuning LLM 2024 2025"

Links: [{"title":"MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning","url":"https://arxiv.org/html/2603.09892"},{"title":"Continual Learning with RL for LLMs","url":"https://cameronrwolfe.substack.com/p/rl-continual-learning"},{"title":"Preprint. SAMPLE-EFFICIENT LLM OPTIMIZATION WITH RESET REPLAY","url":"https://arxiv.org/pdf/2508.06412"},{"title":"Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay","url":"https://arxiv.org/html/2506.05316v3"},{"title":"SURE: SURPRISE-DRIVEN PRIORITISED REPLAY FOR ...","url":"https://openreview.net/pdf?id=IgZWU75BLL"},{"title":"FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning","url":"https://arxiv.org/html/2601.03938v1"},{"title":"RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning","url":"https://arxiv.org/html/2507.07451"},{"title":"Sample-efficient LLM Optimization with Reset Replay","url":"https://arxiv.org/html/2508.06412v2"},{"title":"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning","url":"https://arxiv.org/html/2511.22367v1"},{"title":"SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning","url":"https://www.arxiv.org/pdf/2511.22367"}]

Based on the search results, I found several recent papers and research efforts related to replay buffers, mitigating forgetting, and reinforcement learning for LLM fine-tuning from 2024-2025:

## Key Research Areas

**Replay-Based Continual Learning for LLMs:**

Experience replay has emerged as a particularly practical solution for mitigating catastrophic forgetting in LLMs, as it operates at the data level and integrates naturally with parameter-efficient fine-tuning methods such as LoRA. Replay alleviates forgetting by reintroducing samples from past tasks during training.

**Memory-Aware and Adaptive Replay:**

MSSR is a memory-aware replay framework for continual fine-tuning of LLMs that combines sample-level retention modeling with adaptive replay scheduling in a parameter-efficient LoRA pipeline.

**Surprise-Driven Replay:**

Surprise-based selection and slow-weight consolidation are complementary components for mitigating catastrophic forgetting in continual LLM fine-tuning. Surprise has been shown to be a key driver of memory retention and replay, with surprising events being likely harder to learn and more susceptible to forgetting, making them more valuable for selective memory consolidation.

**RL-Based Approaches:**

Although SFT tends to not perform well for continual learning, RL is found to be shockingly robust to forgetting, even without employing explicit continual learning techniques like replay buffers or regularization.

Experience replay allows the policy to reclaim its previous best score in a few updates and then exceed it later, accelerating convergence and producing a higher final performance ceiling.

**Data Efficiency in RL Fine-tuning:**

Two techniques to improve data efficiency in LLM RL fine-tuning are difficulty-targeted online data selection and rollout replay.

The research from 2024-2025 shows active development in applying and improving replay-based methods for continual learning in LLMs, with focus on making these approaches more efficient and effective.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "de90b85e-cee1-44ad-90eb-462695550975",
  "tool_use_result": {
    "query": "anchor loss replay buffer mitigate forgetting reinforcement learning fine-tuning LLM 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YCSmT8diMRSHprAC2LUgzB",
        "content": [
          {
            "title": "MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning",
            "url": "https://arxiv.org/html/2603.09892"
          },
          {
            "title": "Continual Learning with RL for LLMs",
            "url": "https://cameronrwolfe.substack.com/p/rl-continual-learning"
          },
          {
            "title": "Preprint. SAMPLE-EFFICIENT LLM OPTIMIZATION WITH RESET REPLAY",
            "url": "https://arxiv.org/pdf/2508.06412"
          },
          {
            "title": "Improving Data Efficiency for LLM Reinforcement Fine-tuning Through Difficulty-targeted Online Data Selection and Rollout Replay",
            "url": "https://arxiv.org/html/2506.05316v3"
          },
          {
            "title": "SURE: SURPRISE-DRIVEN PRIORITISED REPLAY FOR ...",
            "url": "https://openreview.net/pdf?id=IgZWU75BLL"
          },
          {
            "title": "FOREVER: Forgetting Curve-Inspired Memory Replay for Language Model Continual Learning",
            "url": "https://arxiv.org/html/2601.03938v1"
          },
          {
            "title": "RLEP: Reinforcement Learning with Experience Replay for LLM Reasoning",
            "url": "https://arxiv.org/html/2507.07451"
          },
          {
            "title": "Sample-efficient LLM Optimization with Reset Replay",
            "url": "https://arxiv.org/html/2508.06412v2"
          },
          {
            "title": "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning",
            "url": "https://arxiv.org/html/2511.22367v1"
          },
          {
            "title": "SuRe: Surprise-Driven Prioritised Replay for Continual LLM Learning",
            "url": "https://www.arxiv.org/pdf/2511.22367"
          }
        ]
      },
      "Based on the search results, I found several recent papers and research efforts related to replay buffers, mitigating forgetting, and reinforcement learning for LLM fine-tuning from 2024-2025:\n\n## Key Research Areas\n\n**Replay-Based Continual Learning for LLMs:**\n\nExperience replay has emerged as a particularly practical solution for mitigating catastrophic forgetting in LLMs, as it operates at the data level and integrates naturally with parameter-efficient fine-tuning methods such as LoRA. Replay alleviates forgetting by reintroducing samples from past tasks during training.\n\n**Memory-Aware and Adaptive Replay:**\n\nMSSR is a memory-aware replay framework for continual fine-tuning of LLMs that combines sample-level retention modeling with adaptive replay scheduling in a parameter-efficient LoRA pipeline.\n\n**Surprise-Driven Replay:**\n\nSurprise-based selection and slow-weight consolidation are complementary components for mitigating catastrophic forgetting in continual LLM fine-tuning. Surprise has been shown to be a key driver of memory retention and replay, with surprising events being likely harder to learn and more susceptible to forgetting, making them more valuable for selective memory consolidation.\n\n**RL-Based Approaches:**\n\nAlthough SFT tends to not perform well for continual learning, RL is found to be shockingly robust to forgetting, even without employing explicit continual learning techniques like replay buffers or regularization.\n\nExperience replay allows the policy to reclaim its previous best score in a few updates and then exceed it later, accelerating convergence and producing a higher final performance ceiling.\n\n**Data Efficiency in RL Fine-tuning:**\n\nTwo techniques to improve data efficiency in LLM RL fine-tuning are difficulty-targeted online data selection and rollout replay.\n\nThe research from 2024-2025 shows active development in applying and improving replay-based methods for continual learning in LLMs, with focus on making these approaches more efficient and effective."
    ],
    "durationSeconds": 8.284415757
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T22:27:44.349Z_

<details><summary>↩ Tool result · `toolu_01VThYAn2ZJxsiiVWZhhVSbZ`</summary>

```text
Web search results for query: ""GRPO" "forgetting" OR "catastrophic" OR "performance drop" OR "alignment tax" site:arxiv.org 2025 2026"

Links: [{"title":"[2602.08813] Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/abs/2602.08813"},{"title":"S-GRPO: Unified Post-Training for Large Vision-Language Models","url":"https://arxiv.org/html/2604.16557v1"},{"title":"2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu","url":"https://arxiv.org/pdf/2507.18071"},{"title":"Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training","url":"https://arxiv.org/html/2604.01499"},{"title":"TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning","url":"https://arxiv.org/pdf/2508.02833"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/html/2309.06256v3"},{"title":"DaGRPO: Rectifying Gradient Conflict in Reasoning via ...","url":"https://arxiv.org/pdf/2512.06337"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/html/2505.22257v1"},{"title":"It Takes Two: Your GRPO Is Secretly DPO","url":"https://arxiv.org/pdf/2510.00977"},{"title":"What Is the Alignment Tax?","url":"https://arxiv.org/html/2603.00047"}]

I've found several highly relevant papers from arxiv.org in 2025-2026 that discuss GRPO in relation to the terms you specified. Here are the key findings:

## Major Issues Identified with GRPO

**Catastrophic Forgetting and Model Collapse:**
GRPO exhibits severe stability issues when training gigantic language models, often resulting in catastrophic and irreversible model collapse. The instability of GRPO stems from the fundamental misapplication and invalidation of importance sampling weights in its algorithmic design, introducing high-variance training noise that progressively accumulates with increased response length.

**Alignment Tax:**
SFT limits optimization to a single trajectory causing catastrophic forgetting, while pure RL explores multiple trajectories but suffers from optimization collapse due to reward sparsity. This represents the core alignment tax problem that GRPO-based methods try to address.

## Key Papers and Solutions

1. **FRPO (Fine-tuning Robust Policy Optimization)**: By modifying GRPO, FRPO substantially reduces safety degradation across multiple base models and downstream fine-tuning regimes while preserving downstream task performance.

2. **S-GRPO**: S-GRPO integrates the objectives of SFT and preference optimization, eliminating the need to choose between isolated paradigms and mitigating catastrophic forgetting in LVLMs.

3. **GSPO (Group Sequence Policy Optimization)**: GSPO is a new RL algorithm for training large language models that addresses the core limitations of GRPO.

4. **TIC-GRPO**: Addresses practical improvements to GRPO's update rules and stability mechanisms.

These papers collectively highlight critical issues with GRPO's foundational design and propose various solutions to address catastrophic forgetting, model collapse, and alignment tax concerns.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "f054b518-277f-424c-a250-5b497cf9a0b0",
  "tool_use_result": {
    "query": "\"GRPO\" \"forgetting\" OR \"catastrophic\" OR \"performance drop\" OR \"alignment tax\" site:arxiv.org 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pj7SvEgtZ6z8WUz5BxbhpZ",
        "content": [
          {
            "title": "[2602.08813] Robust Policy Optimization to Prevent Catastrophic Forgetting",
            "url": "https://arxiv.org/abs/2602.08813"
          },
          {
            "title": "S-GRPO: Unified Post-Training for Large Vision-Language Models",
            "url": "https://arxiv.org/html/2604.16557v1"
          },
          {
            "title": "2025-07-29 Group Sequence Policy Optimization Chujie Zheng∗ Shixuan Liu",
            "url": "https://arxiv.org/pdf/2507.18071"
          },
          {
            "title": "Matching Accuracy, Different Geometry: Evolution Strategies vs GRPO in LLM Post-Training",
            "url": "https://arxiv.org/html/2604.01499"
          },
          {
            "title": "TIC-GRPO: Provable and Efficient Optimization for Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2508.02833"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/html/2309.06256v3"
          },
          {
            "title": "DaGRPO: Rectifying Gradient Conflict in Reasoning via ...",
            "url": "https://arxiv.org/pdf/2512.06337"
          },
          {
            "title": "Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training",
            "url": "https://arxiv.org/html/2505.22257v1"
          },
          {
            "title": "It Takes Two: Your GRPO Is Secretly DPO",
            "url": "https://arxiv.org/pdf/2510.00977"
          },
          {
            "title": "What Is the Alignment Tax?",
            "url": "https://arxiv.org/html/2603.00047"
          }
        ]
      },
      "I've found several highly relevant papers from arxiv.org in 2025-2026 that discuss GRPO in relation to the terms you specified. Here are the key findings:\n\n## Major Issues Identified with GRPO\n\n**Catastrophic Forgetting and Model Collapse:**\nGRPO exhibits severe stability issues when training gigantic language models, often resulting in catastrophic and irreversible model collapse. The instability of GRPO stems from the fundamental misapplication and invalidation of importance sampling weights in its algorithmic design, introducing high-variance training noise that progressively accumulates with increased response length.\n\n**Alignment Tax:**\nSFT limits optimization to a single trajectory causing catastrophic forgetting, while pure RL explores multiple trajectories but suffers from optimization collapse due to reward sparsity. This represents the core alignment tax problem that GRPO-based methods try to address.\n\n## Key Papers and Solutions\n\n1. **FRPO (Fine-tuning Robust Policy Optimization)**: By modifying GRPO, FRPO substantially reduces safety degradation across multiple base models and downstream fine-tuning regimes while preserving downstream task performance.\n\n2. **S-GRPO**: S-GRPO integrates the objectives of SFT and preference optimization, eliminating the need to choose between isolated paradigms and mitigating catastrophic forgetting in LVLMs.\n\n3. **GSPO (Group Sequence Policy Optimization)**: GSPO is a new RL algorithm for training large language models that addresses the core limitations of GRPO.\n\n4. **TIC-GRPO**: Addresses practical improvements to GRPO's update rules and stability mechanisms.\n\nThese papers collectively highlight critical issues with GRPO's foundational design and propose various solutions to address catastrophic forgetting, model collapse, and alignment tax concerns."
    ],
    "durationSeconds": 7.823841874000002
  }
}
```

</details>

---

### Tool call

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Cd2w642cysZFpRBNC6Npyy`</summary>

```json
{
  "query": "arxiv 2602.08813 FRPO robust policy optimization catastrophic forgetting GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "9771b4d3-db37-4234-ac3f-f5b8a7b5ad85",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AxTYY41nWQAo8wntwKs1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4105,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4105
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EAwsSWYGheUox7pPY48o8Z`</summary>

```json
{
  "query": "\"online merging optimizers\" RLHF alignment tax model averaging rewards 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "31a9f183-48e6-4c5b-8045-f9829622f883",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AxTYY41nWQAo8wntwKs1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4105,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4105
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DgEa7Qrci3h6egTqgNv7L5`</summary>

```json
{
  "query": "RL-Struct structured output GRPO hierarchical reward JSON schema reinforcement learning arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "d426791e-1774-4810-955d-8d4f152d6c46",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018AxTYY41nWQAo8wntwKs1y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4105,
      "cache_read_input_tokens": 27247,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4105
      },
      "output_tokens": 40,
      "service_tier": "standard",
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

_source line 25 · 2026-05-14T22:27:54.274Z_

<details><summary>↩ Tool result · `toolu_01Cd2w642cysZFpRBNC6Npyy`</summary>

```text
Web search results for query: "arxiv 2602.08813 FRPO robust policy optimization catastrophic forgetting GRPO"

Links: [{"title":"[2602.08813] Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/abs/2602.08813"},{"title":"Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://arxiv.org/html/2602.08813"},{"title":"(PDF) Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://www.researchgate.net/publication/400622099_Robust_Policy_Optimization_to_Prevent_Catastrophic_Forgetting"},{"title":"[Literature Review] Robust Policy Optimization to Prevent Catastrophic Forgetting","url":"https://www.themoonlight.io/en/review/robust-policy-optimization-to-prevent-catastrophic-forgetting"},{"title":"Adel Javanmard on X: \"🚨 Excited to share our new paper! We propose “Fine-tuning Robust Policy Optimization (FRPO)\" algorithm to tackle Catastrophic Forgetting in LLM Post-Training. 👉 https://t.co/Xk3aKHzJ8i @MahdiSabba24308 @HamedSHassani @pappasg69 https://t.co/ZUj3BmAnVE\" / X","url":"https://x.com/AdelJavanmard/status/2022425436064747567"},{"title":"Training-Free Group Relative Policy Optimization | OpenReview","url":"https://openreview.net/forum?id=tyUnYbE7Gi"},{"title":"Constrained Group Relative Policy Optimization","url":"https://arxiv.org/html/2602.05863.pdf"},{"title":"Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training","url":"https://arxiv.org/html/2505.22257v1"},{"title":"Proximal Policy Optimization Algorithms","url":"https://arxiv.org/pdf/1707.06347"},{"title":"DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization","url":"https://arxiv.org/html/2510.04474v1"}]

Based on the search results, here's what I found about arXiv paper 2602.08813:

## Overview

Fine-tuning Robust Policy Optimization (FRPO) is a robust RLHF framework that optimizes reward not only at the current policy, but across a KL-bounded neighborhood of policies reachable by downstream adaptation.

## The Problem

Even small downstream updates can compromise earlier learned behaviors (e.g., safety), exposing a brittleness known as catastrophic forgetting. The authors argue that preventing this requires pre-finetuning robustness: the base policy should avoid brittle high-reward solutions whose reward drops sharply under standard fine-tuning.

## Key Approach

The key idea is to ensure reward stability under policy shifts via a max-min formulation. By deriving the dual form, this robustness criterion is equivalent to penalizing low-reward rollouts under the current policy, leading to an entropic-risk objective that emphasizes low-reward trajectories and discourages policies with high reward variance.

## Implementation and Results

By modifying GRPO, they develop an algorithm with no extra computation, and empirically show it substantially reduces safety degradation across multiple base models and downstream fine-tuning regimes (SFT and RL) while preserving downstream task performance. In a math-focused RL setting, FRPO preserves accuracy under subsequent fine-tuning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "105c4b72-5614-4629-8bb7-b567bb273254",
  "tool_use_result": {
    "query": "arxiv 2602.08813 FRPO robust policy optimization catastrophic forgetting GRPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HmQXH4TWqNMorajCw8HJNW",
        "content": [
          {
            "title": "[2602.08813] Robust Policy Optimization to Prevent Catastrophic Forgetting",
            "url": "https://arxiv.org/abs/2602.08813"
          },
          {
            "title": "Robust Policy Optimization to Prevent Catastrophic Forgetting",
            "url": "https://arxiv.org/html/2602.08813"
          },
          {
            "title": "(PDF) Robust Policy Optimization to Prevent Catastrophic Forgetting",
            "url": "https://www.researchgate.net/publication/400622099_Robust_Policy_Optimization_to_Prevent_Catastrophic_Forgetting"
          },
          {
            "title": "[Literature Review] Robust Policy Optimization to Prevent Catastrophic Forgetting",
            "url": "https://www.themoonlight.io/en/review/robust-policy-optimization-to-prevent-catastrophic-forgetting"
          },
          {
            "title": "Adel Javanmard on X: \"🚨 Excited to share our new paper! We propose “Fine-tuning Robust Policy Optimization (FRPO)\" algorithm to tackle Catastrophic Forgetting in LLM Post-Training. 👉 https://t.co/Xk3aKHzJ8i @MahdiSabba24308 @HamedSHassani @pappasg69 https://t.co/ZUj3BmAnVE\" / X",
            "url": "https://x.com/AdelJavanmard/status/2022425436064747567"
          },
          {
            "title": "Training-Free Group Relative Policy Optimization | OpenReview",
            "url": "https://openreview.net/forum?id=tyUnYbE7Gi"
          },
          {
            "title": "Constrained Group Relative Policy Optimization",
            "url": "https://arxiv.org/html/2602.05863.pdf"
          },
          {
            "title": "Revisiting Group Relative Policy Optimization: Insights into On-Policy and Off-Policy Training",
            "url": "https://arxiv.org/html/2505.22257v1"
          },
          {
            "title": "Proximal Policy Optimization Algorithms",
            "url": "https://arxiv.org/pdf/1707.06347"
          },
          {
            "title": "DRPO: Efficient Reasoning via Decoupled Reward Policy Optimization",
            "url": "https://arxiv.org/html/2510.04474v1"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2602.08813:\n\n## Overview\n\nFine-tuning Robust Policy Optimization (FRPO) is a robust RLHF framework that optimizes reward not only at the current policy, but across a KL-bounded neighborhood of policies reachable by downstream adaptation.\n\n## The Problem\n\nEven small downstream updates can compromise earlier learned behaviors (e.g., safety), exposing a brittleness known as catastrophic forgetting. The authors argue that preventing this requires pre-finetuning robustness: the base policy should avoid brittle high-reward solutions whose reward drops sharply under standard fine-tuning.\n\n## Key Approach\n\nThe key idea is to ensure reward stability under policy shifts via a max-min formulation. By deriving the dual form, this robustness criterion is equivalent to penalizing low-reward rollouts under the current policy, leading to an entropic-risk objective that emphasizes low-reward trajectories and discourages policies with high reward variance.\n\n## Implementation and Results\n\nBy modifying GRPO, they develop an algorithm with no extra computation, and empirically show it substantially reduces safety degradation across multiple base models and downstream fine-tuning regimes (SFT and RL) while preserving downstream task performance. In a math-focused RL setting, FRPO preserves accuracy under subsequent fine-tuning."
    ],
    "durationSeconds": 7.339584303000003
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T22:27:54.426Z_

<details><summary>↩ Tool result · `toolu_01EAwsSWYGheUox7pPY48o8Z`</summary>

```text
Web search results for query: ""online merging optimizers" RLHF alignment tax model averaging rewards 2024 arxiv"

Links: [{"title":"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment","url":"https://arxiv.org/html/2405.17931v1"},{"title":"[2405.17931] Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment","url":"https://arxiv.org/abs/2405.17931"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://aclanthology.org/2024.emnlp-main.35.pdf"},{"title":"GitHub - QwenLM/online_merging_optimizers: Implementations of online merging optimizers proposed by Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment · GitHub","url":"https://github.com/QwenLM/online_merging_optimizers"},{"title":"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240517931L/abstract"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/html/2309.06256v4"},{"title":"Paper page - Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment","url":"https://huggingface.co/papers/2405.17931"},{"title":"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/online-merging-optimizers-boosting-rewards-mitigating-tax"},{"title":"A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications","url":"https://arxiv.org/html/2410.15595v2"},{"title":"Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment | Request PDF","url":"https://www.researchgate.net/publication/380935434_Online_Merging_Optimizers_for_Boosting_Rewards_and_Mitigating_Tax_in_Alignment"}]

Based on the search results, I found a highly relevant arXiv paper matching your query:

## Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment

This is arXiv paper 2405.17931, published on May 28, 2024.

**Key Findings:**

The paper discovers that interpolating RLHF and SFT model parameters can adjust the trade-off between human preference and basic capabilities, thereby reducing the alignment tax at the cost of alignment reward.

**The Proposed Solution:**

The authors propose integrating the RL policy and SFT models at each optimization step in RLHF to continuously regulate the training direction, introducing the Online Merging Optimizer. Specifically, they merge gradients with the parameter differences between SFT and pretrained models, effectively steering the gradient towards maximizing rewards in the direction of SFT optimization.

**Experimental Validation:**

The optimizer works well with different LLM families, such as Qwen and LLaMA, across various model sizes ranging from 1.8B to 8B, various RLHF algorithms like DPO and KTO, and existing model merging methods. It significantly enhances alignment reward while mitigating alignment tax, achieving higher overall performance across 14 benchmarks.

The paper distinguishes itself from offline model merging approaches by performing the merging online during the RLHF optimization process rather than as a post-processing step.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "cb4f5213-5125-48f8-a897-3bc91b124efe",
  "tool_use_result": {
    "query": "\"online merging optimizers\" RLHF alignment tax model averaging rewards 2024 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01J2269Szeu5kABL71cY641d",
        "content": [
          {
            "title": "Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment",
            "url": "https://arxiv.org/html/2405.17931v1"
          },
          {
            "title": "[2405.17931] Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment",
            "url": "https://arxiv.org/abs/2405.17931"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://aclanthology.org/2024.emnlp-main.35.pdf"
          },
          {
            "title": "GitHub - QwenLM/online_merging_optimizers: Implementations of online merging optimizers proposed by Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment · GitHub",
            "url": "https://github.com/QwenLM/online_merging_optimizers"
          },
          {
            "title": "Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240517931L/abstract"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/html/2309.06256v4"
          },
          {
            "title": "Paper page - Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment",
            "url": "https://huggingface.co/papers/2405.17931"
          },
          {
            "title": "Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/online-merging-optimizers-boosting-rewards-mitigating-tax"
          },
          {
            "title": "A Comprehensive Survey of Direct Preference Optimization: Datasets, Theories, Variants, and Applications",
            "url": "https://arxiv.org/html/2410.15595v2"
          },
          {
            "title": "Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment | Request PDF",
            "url": "https://www.researchgate.net/publication/380935434_Online_Merging_Optimizers_for_Boosting_Rewards_and_Mitigating_Tax_in_Alignment"
          }
        ]
      },
      "Based on the search results, I found a highly relevant arXiv paper matching your query:\n\n## Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\n\nThis is arXiv paper 2405.17931, published on May 28, 2024.\n\n**Key Findings:**\n\nThe paper discovers that interpolating RLHF and SFT model parameters can adjust the trade-off between human preference and basic capabilities, thereby reducing the alignment tax at the cost of alignment reward.\n\n**The Proposed Solution:**\n\nThe authors propose integrating the RL policy and SFT models at each optimization step in RLHF to continuously regulate the training direction, introducing the Online Merging Optimizer. Specifically, they merge gradients with the parameter differences between SFT and pretrained models, effectively steering the gradient towards maximizing rewards in the direction of SFT optimization.\n\n**Experimental Validation:**\n\nThe optimizer works well with different LLM families, such as Qwen and LLaMA, across various model sizes ranging from 1.8B to 8B, various RLHF algorithms like DPO and KTO, and existing model merging methods. It significantly enhances alignment reward while mitigating alignment tax, achieving higher overall performance across 14 benchmarks.\n\nThe paper distinguishes itself from offline model merging approaches by performing the merging online during the RLHF optimization process rather than as a post-processing step."
    ],
    "durationSeconds": 6.544185277000004
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T22:27:55.637Z_

<details><summary>↩ Tool result · `toolu_01DgEa7Qrci3h6egTqgNv7L5`</summary>

```text
Web search results for query: "RL-Struct structured output GRPO hierarchical reward JSON schema reinforcement learning arxiv"

Links: [{"title":"RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs","url":"https://arxiv.org/html/2512.00319"},{"title":"rl-struct:alightweight reinforcement learning framework for ...","url":"https://arxiv.org/pdf/2512.00319"},{"title":"[2512.00319] RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs","url":"https://arxiv.org/abs/2512.00319"},{"title":"RL-Struct: A Lightweight Reinforcement Learning Framework for ...","url":"https://www.arxiv.org/pdf/2512.00319v2"},{"title":"Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models","url":"https://arxiv.org/html/2605.08061v1"},{"title":"HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation","url":"https://arxiv.org/html/2510.07794"},{"title":"Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence","url":"https://arxiv.org/html/2502.14905v1"},{"title":"Chart-RL: Generalized Chart Comprehension via Reinforcement Learning with Verifiable Rewards","url":"https://arxiv.org/html/2603.06958"},{"title":"TaxonRL: Reinforcement Learning with Intermediate Rewards for Interpretable Fine-Grained Visual Reasoning","url":"https://arxiv.org/html/2603.04380"},{"title":"Learning to Generate Structured Output with Schema Reinforcement Learning","url":"https://arxiv.org/html/2502.18878v2"}]

I found relevant research on this topic. Here's what the search results show:

## RL-Struct: A Lightweight Reinforcement Learning Framework

RL-Struct is a lightweight framework using Gradient Regularized Policy Optimization (GRPO) with a hierarchical reward function to align LLMs with structural constraints.

### Key Features

The framework introduces a novel Multi-dimensional Reward Function that decomposes the structured output task into a hierarchy of constraints: structural integrity, format correctness, content accuracy, and validity.

The policy generates a group of outputs, which are evaluated by a multi-dimensional reward function (Structure, Format, Validity, Correctness, Length), with the aggregated reward driving the optimization via the GRPO objective.

### Performance and Efficiency

This approach eliminates the critic network, reducing peak VRAM by 38% compared to PPO. The RL-Struct approach achieves over 80% structural accuracy with as few as 1,000 training samples.

By decomposing the structured output task into learnable reward components and optimizing with GRPO, they achieved robust JSON generation capabilities on a 4B parameter model that rivals or exceeds larger 7B models.

The paper was published on arXiv in December 2025 (arxiv: 2512.00319) and addresses the "Structure Gap" - the challenge of generating valid structured outputs like JSON from language models while maintaining semantic correctness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "bfec3c09-c307-4e93-a80d-3a4b6298c35b",
  "tool_use_result": {
    "query": "RL-Struct structured output GRPO hierarchical reward JSON schema reinforcement learning arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S5uJ3g6WTf9yz132yzZh4s",
        "content": [
          {
            "title": "RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs",
            "url": "https://arxiv.org/html/2512.00319"
          },
          {
            "title": "rl-struct:alightweight reinforcement learning framework for ...",
            "url": "https://arxiv.org/pdf/2512.00319"
          },
          {
            "title": "[2512.00319] RL-Struct: A Lightweight Reinforcement Learning Framework for Reliable Structured Output in LLMs",
            "url": "https://arxiv.org/abs/2512.00319"
          },
          {
            "title": "RL-Struct: A Lightweight Reinforcement Learning Framework for ...",
            "url": "https://www.arxiv.org/pdf/2512.00319v2"
          },
          {
            "title": "Rubric-Grounded Reinforcement Learning: Structured Judge Rewards for Generalizable Reasoning in Language Models",
            "url": "https://arxiv.org/html/2605.08061v1"
          },
          {
            "title": "HiPRAG: Hierarchical Process Rewards for Efficient Agentic Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2510.07794"
          },
          {
            "title": "Think Inside the JSON: Reinforcement Strategy for Strict LLM Schema Adherence",
            "url": "https://arxiv.org/html/2502.14905v1"
          },
          {
            "title": "Chart-RL: Generalized Chart Comprehension via Reinforcement Learning with Verifiable Rewards",
            "url": "https://arxiv.org/html/2603.06958"
          },
          {
            "title": "TaxonRL: Reinforcement Learning with Intermediate Rewards for Interpretable Fine-Grained Visual Reasoning",
            "url": "https://arxiv.org/html/2603.04380"
          },
          {
            "title": "Learning to Generate Structured Output with Schema Reinforcement Learning",
            "url": "https://arxiv.org/html/2502.18878v2"
          }
        ]
      },
      "I found relevant research on this topic. Here's what the search results show:\n\n## RL-Struct: A Lightweight Reinforcement Learning Framework\n\nRL-Struct is a lightweight framework using Gradient Regularized Policy Optimization (GRPO) with a hierarchical reward function to align LLMs with structural constraints.\n\n### Key Features\n\nThe framework introduces a novel Multi-dimensional Reward Function that decomposes the structured output task into a hierarchy of constraints: structural integrity, format correctness, content accuracy, and validity.\n\nThe policy generates a group of outputs, which are evaluated by a multi-dimensional reward function (Structure, Format, Validity, Correctness, Length), with the aggregated reward driving the optimization via the GRPO objective.\n\n### Performance and Efficiency\n\nThis approach eliminates the critic network, reducing peak VRAM by 38% compared to PPO. The RL-Struct approach achieves over 80% structural accuracy with as few as 1,000 training samples.\n\nBy decomposing the structured output task into learnable reward components and optimizing with GRPO, they achieved robust JSON generation capabilities on a 4B parameter model that rivals or exceeds larger 7B models.\n\nThe paper was published on arXiv in December 2025 (arxiv: 2512.00319) and addresses the \"Structure Gap\" - the challenge of generating valid structured outputs like JSON from language models while maintaining semantic correctness."
    ],
    "durationSeconds": 6.909079778
  }
}
```

</details>

---

### Assistant

_source line 28_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to compile a comprehensive literature survey. Let me also search for one more specific topic - the "reward hacking" paper by Lilian Weng and the specific paper on KL divergence in GRPO.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "3bfea70c-bbd3-442a-b561-b09877c5c349",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVjjY999dR12qP12o4uRyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 31352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3014
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

_source line 29_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Bvqds1pXv2QtnxAGWyjqRW`</summary>

```json
{
  "query": "arxiv \"alignment tax\" \"what is\" definition RLHF forgetting capabilities survey 2603.00047"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "30d4c74f-5ad9-4269-a075-a71f5516f953",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVjjY999dR12qP12o4uRyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 31352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3014
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

_source line 30_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016qwdZtWRjpWJxSQTBd67Sc`</summary>

```json
{
  "query": "GRPO KL divergence coefficient too small forgetting LoRA low rank reinforcement learning instability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "80b3b9f7-f64f-418f-ae5b-906c616b4045",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GVjjY999dR12qP12o4uRyc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3014,
      "cache_read_input_tokens": 31352,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3014
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

_source line 31 · 2026-05-14T22:28:20.473Z_

<details><summary>↩ Tool result · `toolu_01Bvqds1pXv2QtnxAGWyjqRW`</summary>

```text
Web search results for query: "arxiv "alignment tax" "what is" definition RLHF forgetting capabilities survey 2603.00047"

Links: [{"title":"What Is the Alignment Tax?","url":"https://arxiv.org/html/2603.00047"},{"title":"[2309.06256] Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/abs/2309.06256"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://arxiv.org/html/2309.06256v4"},{"title":"[2603.00047] What Is the Geometry of the Alignment Tax?","url":"https://arxiv.org/abs/2603.00047"},{"title":"Mitigating the Alignment Tax of RLHF - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv230906256L/abstract"},{"title":"Mitigating the Alignment Tax of RLHF - ACL Anthology","url":"https://aclanthology.org/2024.emnlp-main.35/"},{"title":"[2309.06256] Mitigating the Alignment Tax of RLHF - ar5iv","url":"https://ar5iv.labs.arxiv.org/html/2309.06256"},{"title":"Mitigating the Alignment Tax of RLHF","url":"https://aclanthology.org/2024.emnlp-main.35.pdf"},{"title":"Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection","url":"https://arxiv.org/html/2602.07892"},{"title":"Paper page - Mitigating the Alignment Tax of RLHF","url":"https://huggingface.co/papers/2309.06256"}]

Based on the search results, I found relevant information about the alignment tax concept and the paper 2603.00047.

## Definition of Alignment Tax

The alignment tax is often intuitively invoked as the capability cost of making an AI system safe. More specifically, aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting pretrained abilities, which is also known as the alignment tax.

The term "Alignment tax" originated informally as a reference to the capability cost of safety, and the alignment tax has no mathematical definition in prior work (as noted in the paper 2603.00047).

## Paper 2603.00047: Mathematical Framework

The paper arxiv 2603.00047 titled "What Is the Alignment Tax?" provides the first formal mathematical characterization. The paper provides a geometric theory of the alignment tax in representation space, and under linear representation assumptions, defines the alignment tax rate as the squared projection of the safety direction onto the capability subspace and derives the Pareto frontier governing safety-capability tradeoffs, parameterized by a single quantity of the principal angle between the safety and capability subspaces.

## Empirical Findings on Forgetting

Research shows that reinforcement learning from human feedback (RLHF) degrades performance on reasoning benchmarks, and reasoning degrades more than other capabilities during alignment.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "31ba45e3-7e4a-447d-9eca-ded5b9bb32ce",
  "tool_use_result": {
    "query": "arxiv \"alignment tax\" \"what is\" definition RLHF forgetting capabilities survey 2603.00047",
    "results": [
      {
        "tool_use_id": "srvtoolu_01CvBmMy38qt7kZo7nMiwLti",
        "content": [
          {
            "title": "What Is the Alignment Tax?",
            "url": "https://arxiv.org/html/2603.00047"
          },
          {
            "title": "[2309.06256] Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/abs/2309.06256"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://arxiv.org/html/2309.06256v4"
          },
          {
            "title": "[2603.00047] What Is the Geometry of the Alignment Tax?",
            "url": "https://arxiv.org/abs/2603.00047"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2023arXiv230906256L/abstract"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF - ACL Anthology",
            "url": "https://aclanthology.org/2024.emnlp-main.35/"
          },
          {
            "title": "[2309.06256] Mitigating the Alignment Tax of RLHF - ar5iv",
            "url": "https://ar5iv.labs.arxiv.org/html/2309.06256"
          },
          {
            "title": "Mitigating the Alignment Tax of RLHF",
            "url": "https://aclanthology.org/2024.emnlp-main.35.pdf"
          },
          {
            "title": "Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection",
            "url": "https://arxiv.org/html/2602.07892"
          },
          {
            "title": "Paper page - Mitigating the Alignment Tax of RLHF",
            "url": "https://huggingface.co/papers/2309.06256"
          }
        ]
      },
      "Based on the search results, I found relevant information about the alignment tax concept and the paper 2603.00047.\n\n## Definition of Alignment Tax\n\nThe alignment tax is often intuitively invoked as the capability cost of making an AI system safe. More specifically, aligning LLMs under Reinforcement Learning with Human Feedback (RLHF) can lead to forgetting pretrained abilities, which is also known as the alignment tax.\n\nThe term \"Alignment tax\" originated informally as a reference to the capability cost of safety, and the alignment tax has no mathematical definition in prior work (as noted in the paper 2603.00047).\n\n## Paper 2603.00047: Mathematical Framework\n\nThe paper arxiv 2603.00047 titled \"What Is the Alignment Tax?\" provides the first formal mathematical characterization. The paper provides a geometric theory of the alignment tax in representation space, and under linear representation assumptions, defines the alignment tax rate as the squared projection of the safety direction onto the capability subspace and derives the Pareto frontier governing safety-capability tradeoffs, parameterized by a single quantity of the principal angle between the safety and capability subspaces.\n\n## Empirical Findings on Forgetting\n\nResearch shows that reinforcement learning from human feedback (RLHF) degrades performance on reasoning benchmarks, and reasoning degrades more than other capabilities during alignment."
    ],
    "durationSeconds": 6.227452425999989
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T22:28:22.042Z_

<details><summary>↩ Tool result · `toolu_016qwdZtWRjpWJxSQTBd67Sc`</summary>

```text
Web search results for query: "GRPO KL divergence coefficient too small forgetting LoRA low rank reinforcement learning instability"

Links: [{"title":"Understanding the Math Behind GRPO — DeepSeek-R1-Zero | by Yugen.ai | Yugen.ai Technology Blog | Medium","url":"https://medium.com/yugen-ai-technology-blog/understanding-the-math-behind-grpo-deepseek-r1-zero-9fb15e103a0a"},{"title":"GRPO - Group Relative Policy Optimization: How DeepSeek Trains Reasoning Models","url":"https://chessman7.substack.com/p/grpo-group-relative-policy-optimization"},{"title":"The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU","url":"https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"},{"title":"Group Relative Policy Optimization (GRPO)","url":"https://cameronrwolfe.substack.com/p/grpo"},{"title":"Group Relative Policy Optimization (GRPO) — verl documentation","url":"https://verl.readthedocs.io/en/latest/algo/grpo.html"},{"title":"What is GRPO? The RL algorithm used to train DeepSeek | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/what-is-grpo-the-rl-algorithm-used-to-train-deepseek-12acc19798d3"},{"title":"Reinforcement Learning for LLM Reasoning Under Memory Constraints","url":"https://arxiv.org/html/2504.20834v1"},{"title":"Theory Behind GRPO - AI Engineering Academy","url":"https://aiengineering.academy/LLM/TheoryBehindFinetuning/GRPO/"},{"title":"Choosing KL Estimators in RL: From Value Unbiasedness to Gradient Correctness | Xihuai Wang's Page","url":"https://xihuai18.github.io/reinforcement-learning/2025/12/01/kl-estimators-en.html"},{"title":"GRPO Trainer · Hugging Face","url":"https://huggingface.co/docs/trl/en/grpo_trainer"}]

Based on the search results, I found relevant information about GRPO, KL divergence coefficients, LoRA, and reinforcement learning stability. Here are the key findings:

## GRPO with KL Divergence and LoRA Training

GRPO improves training stability through group-based advantage estimation, clipping to prevent extreme updates, and KL divergence penalty to maintain proximity to the original policy. Practical solutions for intensive training include using techniques like LoRA (Low-Rank Adaptation) to reduce trainable parameters.

## KL Divergence Coefficient Issues

An important finding regarding small KL divergence coefficients: β = 0.0 by default for KL divergence, and this choice is motivated by recent studies which have shown that the KL divergence term is not essential for training with GRPO. However, DeepSeek-R1 uses a value of 0.001 when the KL penalty is applied.

## GRPO with LoRA Fine-tuning and Instability

Research has specifically identified instability issues when combining GRPO with LoRA. Full-token GRPO baseline under LoRA fine-tuning did not improve model performance on either task, suggesting that GRPO may share sensitivity issues when only a small subset of parameters is updated. The algorithm may overfit under LoRA fine-tuning or require more extensive hyperparameter exploration to stabilize.

## Solutions for LoRA Stability

Memory-efficient variants like Stochastic-GRPO (S-GRPO) and Token-Specific Prefix Matching Optimization (T-SPMO) were introduced, with both methods significantly improving performance using LoRA training on a single 40GB GPU.

The research indicates that combining GRPO with LoRA can be unstable, and using alternative methods or careful hyperparameter tuning (including the KL coefficient value) is necessary for successful training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "139fd4bc-a89b-4b5d-869d-953e26781224",
  "tool_use_result": {
    "query": "GRPO KL divergence coefficient too small forgetting LoRA low rank reinforcement learning instability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JL6XgxwKrfA9HzhWt9xjQ5",
        "content": [
          {
            "title": "Understanding the Math Behind GRPO — DeepSeek-R1-Zero | by Yugen.ai | Yugen.ai Technology Blog | Medium",
            "url": "https://medium.com/yugen-ai-technology-blog/understanding-the-math-behind-grpo-deepseek-r1-zero-9fb15e103a0a"
          },
          {
            "title": "GRPO - Group Relative Policy Optimization: How DeepSeek Trains Reasoning Models",
            "url": "https://chessman7.substack.com/p/grpo-group-relative-policy-optimization"
          },
          {
            "title": "The Engineering Handbook for GRPO + LoRA with Verl: Training Qwen2.5 on Multi-GPU",
            "url": "https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO)",
            "url": "https://cameronrwolfe.substack.com/p/grpo"
          },
          {
            "title": "Group Relative Policy Optimization (GRPO) — verl documentation",
            "url": "https://verl.readthedocs.io/en/latest/algo/grpo.html"
          },
          {
            "title": "What is GRPO? The RL algorithm used to train DeepSeek | by Mehul Gupta | Data Science in Your Pocket | Medium",
            "url": "https://medium.com/data-science-in-your-pocket/what-is-grpo-the-rl-algorithm-used-to-train-deepseek-12acc19798d3"
          },
          {
            "title": "Reinforcement Learning for LLM Reasoning Under Memory Constraints",
            "url": "https://arxiv.org/html/2504.20834v1"
          },
          {
            "title": "Theory Behind GRPO - AI Engineering Academy",
            "url": "https://aiengineering.academy/LLM/TheoryBehindFinetuning/GRPO/"
          },
          {
            "title": "Choosing KL Estimators in RL: From Value Unbiasedness to Gradient Correctness | Xihuai Wang's Page",
            "url": "https://xihuai18.github.io/reinforcement-learning/2025/12/01/kl-estimators-en.html"
          },
          {
            "title": "GRPO Trainer · Hugging Face",
            "url": "https://huggingface.co/docs/trl/en/grpo_trainer"
          }
        ]
      },
      "Based on the search results, I found relevant information about GRPO, KL divergence coefficients, LoRA, and reinforcement learning stability. Here are the key findings:\n\n## GRPO with KL Divergence and LoRA Training\n\nGRPO improves training stability through group-based advantage estimation, clipping to prevent extreme updates, and KL divergence penalty to maintain proximity to the original policy. Practical solutions for intensive training include using techniques like LoRA (Low-Rank Adaptation) to reduce trainable parameters.\n\n## KL Divergence Coefficient Issues\n\nAn important finding regarding small KL divergence coefficients: β = 0.0 by default for KL divergence, and this choice is motivated by recent studies which have shown that the KL divergence term is not essential for training with GRPO. However, DeepSeek-R1 uses a value of 0.001 when the KL penalty is applied.\n\n## GRPO with LoRA Fine-tuning and Instability\n\nResearch has specifically identified instability issues when combining GRPO with LoRA. Full-token GRPO baseline under LoRA fine-tuning did not improve model performance on either task, suggesting that GRPO may share sensitivity issues when only a small subset of parameters is updated. The algorithm may overfit under LoRA fine-tuning or require more extensive hyperparameter exploration to stabilize.\n\n## Solutions for LoRA Stability\n\nMemory-efficient variants like Stochastic-GRPO (S-GRPO) and Token-Specific Prefix Matching Optimization (T-SPMO) were introduced, with both methods significantly improving performance using LoRA training on a single 40GB GPU.\n\nThe research indicates that combining GRPO with LoRA can be unstable, and using alternative methods or careful hyperparameter tuning (including the KL coefficient value) is necessary for successful training."
    ],
    "durationSeconds": 7.775141399999993
  }
}
```

</details>

---

### Assistant

_source line 33_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to compile the literature survey. Let me also save this to a file for the project. Let me organize the findings into the requested format.

Let me now write the survey report.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "7e7c7fad-de3a-48de-8d8f-617f3df25bd1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYQG33c59kG9kbAQsvyWnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 34366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 34_

Now I have enough material. Let me compile the survey report.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "990f37ae-9dcb-4a50-acf5-9b528089b131",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYQG33c59kG9kbAQsvyWnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 34366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 35_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011iGTKgBGUZnqonDKQJTYYG`</summary>

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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "255c0608-125e-4280-8d0b-553e0e9b41df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GYQG33c59kG9kbAQsvyWnw",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2086,
      "cache_read_input_tokens": 34366,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2086
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

_source line 36 · 2026-05-14T22:28:27.294Z_

<details><summary>↩ Tool result · `toolu_011iGTKgBGUZnqonDKQJTYYG`</summary>

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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "6c2a4f9c-d015-4e07-a551-4327ed95ee6b",
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

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0111NDYfnra3ZzHnf81RbNSt`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "d82e1714-f353-4da3-a934-b4acf84479ed",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UbVePmhQV5B242FLB1Nk26",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 434,
      "cache_read_input_tokens": 36452,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 434
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

_source line 38 · 2026-05-14T22:28:30.366Z_

<details><summary>↩ Tool result · `toolu_0111NDYfnra3ZzHnf81RbNSt`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
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
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "33c300e4-9d78-49d8-affd-eb3d69e3c6e2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_0185VkGw19fmZFapUXXJkUay`</summary>

```json
{
  "project": "faith-evidence-ie",
  "file": "memory.md",
  "content": "# 文献调研：GRPO/RLHF 训练中的\"先遗忘后恢复\"现象\n\n日期：2026-05-14\n\n## 背景\n\nQwen3-4B + GRPO + QLoRA 4-bit 训练文档级关系抽取，观察到：\n- Reward 上升但 eval rel_F1 崩塌（ckpt-20: 0.0077 vs SFT baseline 0.406）\n- lr=5e-5 和 lr=5e-6 下都出现\n- 存在\"先遗忘后缓慢恢复\"的 U 型曲线（step-10=0.003 → step-90=0.211），但恢复不足\n\n---\n\n## 论文 1：Mitigating the Alignment Tax of RLHF\n\n- **作者**：Yifei Lin, Yuxin Tan, et al.\n- **年份/Venue**：2024, EMNLP 2024\n- **arXiv**：2309.06256\n\n### 核心发现\n- 定义了\"alignment tax\"：RLHF 对齐后模型遗忘预训练/SFT 阶段习得能力的现象\n- 发现简单的**模型参数平均**（插值 SFT 和 RLHF 后模型权重）在 alignment-forgetting Pareto 前沿上表现最优\n- 提出 **Heterogeneous Model Averaging (HMA)**：对不同层使用不同插值比例，最大化对齐收益同时最小化遗忘\n\n### 与我们场景的相关性\n- **直接相关**。我们的 rel_F1 崩塌就是 alignment tax 的典型表现——GRPO 优化 reward 的过程中覆盖了 SFT 学到的抽取能力\n- HMA 的层级插值思路可直接应用于 QLoRA adapter 权重\n\n### 推荐缓解方案\n- 训练后对 SFT checkpoint 和 GRPO checkpoint 做权重插值（α=0.3~0.7）\n- 或用 HMA 对不同 LoRA 层设置不同插值系数\n\n---\n\n## 论文 2：Online Merging Optimizers for Boosting Rewards and Mitigating Tax in Alignment\n\n- **作者**：Lu et al. (Qwen 团队)\n- **年份/Venue**：2024, arXiv 2405.17931\n- **开源**：github.com/QwenLM/online_merging_optimizers\n\n### 核心发现\n- 在 RLHF 每个优化步骤中实时合并 RL policy 和 SFT 模型参数，持续调节训练方向\n- 将梯度与 SFT-pretrained 参数差合并，引导梯度朝着\"在 SFT 优化方向上最大化 reward\"的方向前进\n- 在 Qwen 和 LLaMA 系列（1.8B-8B）、DPO/KTO 等多种 RLHF 算法上验证有效\n- 14 个 benchmark 上同时提升对齐 reward 并降低 alignment tax\n\n### 与我们场景的相关性\n- **高度相关**。该方法正是为解决我们观察到的问题设计的——reward 上升但能力退化\n- 来自 Qwen 团队，与我们使用的 Qwen3-4B 模型同源，兼容性好\n- 在训练过程中在线缓解，而非事后补救\n\n### 推荐缓解方案\n- 在 GRPO 训练中集成 Online Merging Optimizer，每步将 LoRA 更新方向锚定在 SFT 附近\n\n---\n\n## 论文 3：Robust Policy Optimization to Prevent Catastrophic Forgetting (FRPO)\n\n- **作者**：Sabbaghi, Hassani, Javanmard et al.\n- **年份/Venue**：2025, arXiv 2602.08813\n\n### 核心发现\n- 指出即使小幅下游更新也会破坏 RLHF 学到的行为（如安全性），暴露 catastrophic forgetting 的脆弱性\n- 提出 FRPO：优化 reward 时不仅考虑当前策略，还考虑 KL 邻域内所有可达策略的表现\n- 等价于 entropic risk objective——强调低 reward 轨迹，抑制高 reward 方差的策略\n- 通过修改 GRPO 实现，**无额外计算开销**\n\n### 与我们场景的相关性\n- **直接可用**。FRPO 本身就是 GRPO 的改进版本，直接替换即可\n- 解决的核心问题是\"GRPO 找到的高 reward 解是脆弱的\"——与我们观察到的 reward↑但 eval↓一致\n- 表明我们的模型可能找到了一个 reward hacking 式的局部最优\n\n### 推荐缓解方案\n- 将 GRPO 替换为 FRPO（修改 advantage 计算，加入 entropic risk 项）\n\n---\n\n## 论文 4：RL-Struct — Lightweight RL Framework for Structured Output\n\n- **作者**：arXiv 2512.00319\n- **年份/Venue**：2025, arXiv\n\n### 核心发现\n- 针对 JSON 等结构化输出 + RL 训练的特殊挑战\n- 提出**分层 reward 函数**：将结构化输出任务分解为 structure integrity → format correctness → content accuracy → validity 的层级约束\n- 使用 GRPO 优化，消除 critic network，降低 38% 峰值 VRAM\n- 4B 模型上 1000 个样本即可达到 80%+ 结构准确率，性能媲美 7B 模型\n\n### 与我们场景的相关性\n- **高度相关**。我们的任务要求模型输出 JSON 格式的关系抽取结果，这正是\"结构化输出 + RL\"的组合\n- 单一 reward 信号（F1）可能让模型在格式和内容之间混淆——分层 reward 可缓解\n- 当前 reward 可能过度奖励格式正确但内容错误的输出（reward hacking 的一种形式）\n\n### 推荐缓解方案\n- 将 reward 分解为：格式合规 reward + 实体正确性 reward + 关系正确性 reward\n- 分层加权，先保证格式，再优化内容\n\n---\n\n## 论文 5：GRPO++ / GRPO Instability with LoRA\n\n- **来源**：多篇论文和实践报告的综合\n  - Cameron Wolfe, \"GRPO++: Tricks for Making RL Actually Work\", 2025\n  - HuggingFace blog, \"Engineering Handbook for GRPO + LoRA with Verl\"\n  - arXiv 2504.20834, \"RL for LLM Reasoning Under Memory Constraints\"\n\n### 核心发现\n- **GRPO + LoRA 组合存在已知的不稳定性**：仅更新少量参数时，GRPO 的 group-relative advantage 估计方差增大\n- Full-token GRPO baseline 在 LoRA fine-tuning 下\"未能提升模型性能\"，表明 GRPO 对参数更新子集很敏感\n- KL 系数默认 β=0.0（TRL 默认），DeepSeek-R1 使用 β=0.001——过小的 KL 惩罚允许策略大幅偏离 SFT\n- 实践建议：\n  - 增大 KL 系数（β=0.01~0.1）\n  - 使用更大的 group size（G=16~64）降低 advantage 估计方差\n  - 降低学习率（LoRA + RL 场景建议 1e-6 量级）\n  - 考虑 Stochastic-GRPO 或 Token-Specific 优化变体\n\n### 与我们场景的相关性\n- **完全匹配**。我们正是 GRPO + QLoRA 4-bit，且 KL 系数仅 0.001\n- 低 KL + 低秩更新 = 策略快速偏离 SFT → 遗忘\n- 这是已知问题，不是偶发现象\n\n### 推荐缓解方案\n- 增大 KL 系数至 0.01~0.05\n- 增大 LoRA rank（r=4 可能太小，建议 r=16~32）\n- 增大 group size 降低 advantage 估计噪声\n\n---\n\n## 综合分析\n\n### \"先崩后恢复\" U 型曲线的最可能解释\n\n我们观察到的现象是 **三个因素叠加** 的结果：\n\n1. **Alignment Tax（核心原因）**：GRPO 梯度覆盖了 SFT 学到的关系抽取能力参数。由于 QLoRA 仅更新极少参数（rank=4），这些参数同时承载 SFT 能力和 RL 优化目标，冲突尤其剧烈。\n\n2. **KL 约束过弱 + LoRA 低秩放大不稳定性**：β=0.001 的 KL 惩罚几乎不约束策略偏离。在 LoRA 低秩空间中，微小的参数变化会导致输出分布剧烈变化，加速遗忘。\n\n3. **Reward Proxy Mismatch**：训练 reward 上升但 eval F1 下降，符合经典的 reward hacking 模式。模型可能学会了生成\"看起来合理\"但实际关系错误的输出——例如格式正确但实体/关系随机配对。\n\n**U 型恢复的解释**：训练初期策略大幅偏离导致崩塌；随着训练继续，模型在新的策略空间中重新\"发现\"部分抽取模式，但由于 LoRA 容量有限且 reward 信号有噪声，恢复不完全。\n\n### 最值得尝试的 2 个缓解方案\n\n**方案 A：增强 KL 正则化 + 扩大 LoRA 容量（低成本，优先尝试）**\n- KL 系数从 0.001 → 0.04\n- LoRA rank 从 r=4 → r=16\n- 学习率降至 1e-6\n- 预期效果：抑制训练初期的剧烈偏离，避免崩塌\n\n**方案 B：分层 Reward 设计（中等成本，针对 reward hacking）**\n- 将单一 reward 分解为：format_reward（JSON 格式合规）+ entity_reward（实体正确）+ relation_reward（关系正确）\n- 加权组合，format 权重最低（仅作 gate），relation 权重最高\n- 预期效果：消除模型通过格式取巧获得高 reward 的捷径\n\n**备选方案 C（如 A/B 不够）：Online Merging Optimizer**\n- 来自 Qwen 团队，在每个训练步骤将 LoRA 更新锚定在 SFT 方向\n- 实现复杂度中等，但效果在多个 Qwen 模型上验证过\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "5cf9378c-b3f4-4103-ad47-b0b0da2cd18c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FJjUfXhreEceNFKVxtuxVL",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 296,
      "cache_read_input_tokens": 36886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 296
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

_source line 40 · 2026-05-14T22:29:47.069Z_

<details><summary>↩ Tool result · `toolu_0185VkGw19fmZFapUXXJkUay`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "3a25af4b-f5b3-4ea3-908e-5c212a55fcb7",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__append_idea · `toolu_01BRhH1roNdnaXBv72r1nMTW`</summary>

```json
{
  "project": "faith-evidence-ie",
  "text": "**GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "1c53fd61-f872-4a72-95b6-8027aab623c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dnjz4wXg1DLXSqKEHpQMRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 37182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3474
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

_source line 42 · 2026-05-14T22:29:53.011Z_

<details><summary>↩ Tool result · `toolu_01BRhH1roNdnaXBv72r1nMTW`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "a81d08ea-4ac1-43c9-88ab-a41a949f2a82",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"added\\\": \\\"**GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\\\", \\\"file\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 A**：增大 KL 系数（0.001→0.04）+ 扩大 LoRA rank（r=4→r=16）+ 降低 lr 至 1e-6。文献调研表明 GRPO+QLoRA 低秩+低KL 是已知不稳定组合，这是最低成本的修复。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__append_idea · `toolu_01BjfJoVytq1UseU8LWiEoc2`</summary>

```json
{
  "project": "faith-evidence-ie",
  "text": "**GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "62fc3100-1c28-4597-8272-4ec849f1d8dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dnjz4wXg1DLXSqKEHpQMRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 37182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3474
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

_source line 44 · 2026-05-14T22:29:55.327Z_

<details><summary>↩ Tool result · `toolu_01BjfJoVytq1UseU8LWiEoc2`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "e1ffcd14-e0bc-46d5-89b4-266e03287687",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"added\\\": \\\"**GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\\\", \\\"file\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 B**：分层 Reward 设计——将单一 reward 分解为 format_reward + entity_reward + relation_reward，消除 reward hacking 捷径。参考 RL-Struct (arXiv 2512.00319) 的层级约束方法。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__append_idea · `toolu_011A5dkBC5XpSXn8MYwJAmyM`</summary>

```json
{
  "project": "faith-evidence-ie",
  "text": "**GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "4bd1dcca-fe0c-4358-9e45-b5035e10e420",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dnjz4wXg1DLXSqKEHpQMRU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3474,
      "cache_read_input_tokens": 37182,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3474
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

_source line 46 · 2026-05-14T22:29:56.976Z_

<details><summary>↩ Tool result · `toolu_011A5dkBC5XpSXn8MYwJAmyM`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "16bb7f3e-34ff-49bc-b288-62fd0cef9102",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"added\\\": \\\"**GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\\\", \\\"file\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"added\": \"**GRPO 遗忘缓解方案 C**：集成 Qwen 团队的 Online Merging Optimizer (arXiv 2405.17931)，在 GRPO 每步将 LoRA 更新方向锚定在 SFT 附近，训练中在线缓解 alignment tax。\", \"file\": \"/home/ubuntu/.agent-ml-research-idea_gen_0513_6/projects/faith-evidence-ie/ideas.md\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 47_

调研完成。以下是结果摘要。

---

## 5 篇核心论文

### 1. Mitigating the Alignment Tax of RLHF (EMNLP 2024)
Lin et al. | [arXiv 2309.06256](https://arxiv.org/abs/2309.06256)

RLHF 导致模型遗忘 SFT 能力（alignment tax）。发现**模型权重插值**（SFT 与 RLHF checkpoint 线性插值）在 alignment-forgetting Pareto 前沿表现最优。提出 HMA 对不同层设不同插值比例。

### 2. Online Merging Optimizers for Boosting Rewards and Mitigating Tax (2024)
Qwen 团队 | [arXiv 2405.17931](https://arxiv.org/abs/2405.17931) | [GitHub](https://github.com/QwenLM/online_merging_optimizers)

在 RLHF 每个优化步实时合并 RL policy 和 SFT 参数，将梯度方向锚定在 SFT 优化方向上。Qwen/LLaMA 1.8B-8B + DPO/KTO 上验证，14 个 benchmark 同时提升 reward 并降低 alignment tax。

### 3. FRPO: Robust Policy Optimization to Prevent Catastrophic Forgetting (2025)
Sabbaghi et al. | [arXiv 2602.08813](https://arxiv.org/abs/2602.08813)

修改 GRPO 的 advantage 计算，加入 entropic risk 项——强调低 reward 轨迹，抑制高方差策略。**无额外计算开销**，直接替换 GRPO 即可。核心论点：标准 GRPO 找到的高 reward 解是脆弱的。

### 4. RL-Struct: Structured Output + GRPO (2025)
[arXiv 2512.00319](https://arxiv.org/abs/2512.00319)

针对 JSON 结构化输出 + RL 的挑战，提出**分层 reward**（structure → format → content → validity）。4B 模型上 1000 样本达 80%+ 结构准确率。解决单一 reward 让模型在格式和内容间混淆的问题。

### 5. GRPO + LoRA 不稳定性（综合多源）
[GRPO++ blog](https://cameronrwolfe.substack.com/p/grpo-tricks) | [HF GRPO+LoRA handbook](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl) | [arXiv 2504.20834](https://arxiv.org/abs/2504.20834)

**已知问题**：GRPO + LoRA 低秩更新时 advantage 估计方差增大，TRL 默认 KL β=0.0，策略易大幅偏离。Full-token GRPO 在 LoRA 下"未能提升性能"。建议 β≥0.01、rank≥16、lr~1e-6。

---

## 综合诊断

你们的"先崩后恢复"是 **三因素叠加**：

1. **Alignment tax**：GRPO 梯度覆盖 SFT 关系抽取能力，rank=4 的 LoRA 参数同时承载旧能力和新优化目标，冲突剧烈
2. **KL 约束过弱（β=0.001）+ 低秩放大不稳定性**：策略快速偏离 SFT 分布，训练前 20 步即崩塌
3. **Reward proxy mismatch**：reward↑ 但 F1↓ 是经典 reward hacking——模型可能学会生成格式正确但关系错误的输出

U 型恢复的原因：崩塌后模型在新策略空间中缓慢重新发现部分抽取模式，但 LoRA 容量不足 + reward 噪声导致恢复不完全。

---

## 最值得尝试的 2 个方案

| | 方案 A：增强正则化 | 方案 B：分层 Reward |
|---|---|---|
| 改动 | KL β: 0.001→0.04, rank: 4→16, lr: 5e-6→1e-6 | reward 拆为 format + entity + relation，分权重 |
| 成本 | 低（改配置即可） | 中（需重写 reward 函数） |
| 针对问题 | 策略偏离过快 | reward hacking |
| 优先级 | **先试这个** | A 不够再加 |

备选方案 C：集成 Qwen 团队的 Online Merging Optimizer，每步锚定 SFT 方向，实现复杂度中等但同源验证过。

已将完整调研存入 `memory.md`，三个缓解方案存入 `ideas.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "uuid": "d80556de-ad8f-4cbf-81ec-bb91b37c6202",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BjcMNKyZBjE8KEgWVeyCtc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1119,
      "cache_read_input_tokens": 40656,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1119
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

_source line 48_

调研完成。以下是结果摘要。

---

## 5 篇核心论文

### 1. Mitigating the Alignment Tax of RLHF (EMNLP 2024)
Lin et al. | [arXiv 2309.06256](https://arxiv.org/abs/2309.06256)

RLHF 导致模型遗忘 SFT 能力（alignment tax）。发现**模型权重插值**（SFT 与 RLHF checkpoint 线性插值）在 alignment-forgetting Pareto 前沿表现最优。提出 HMA 对不同层设不同插值比例。

### 2. Online Merging Optimizers for Boosting Rewards and Mitigating Tax (2024)
Qwen 团队 | [arXiv 2405.17931](https://arxiv.org/abs/2405.17931) | [GitHub](https://github.com/QwenLM/online_merging_optimizers)

在 RLHF 每个优化步实时合并 RL policy 和 SFT 参数，将梯度方向锚定在 SFT 优化方向上。Qwen/LLaMA 1.8B-8B + DPO/KTO 上验证，14 个 benchmark 同时提升 reward 并降低 alignment tax。

### 3. FRPO: Robust Policy Optimization to Prevent Catastrophic Forgetting (2025)
Sabbaghi et al. | [arXiv 2602.08813](https://arxiv.org/abs/2602.08813)

修改 GRPO 的 advantage 计算，加入 entropic risk 项——强调低 reward 轨迹，抑制高方差策略。**无额外计算开销**，直接替换 GRPO 即可。核心论点：标准 GRPO 找到的高 reward 解是脆弱的。

### 4. RL-Struct: Structured Output + GRPO (2025)
[arXiv 2512.00319](https://arxiv.org/abs/2512.00319)

针对 JSON 结构化输出 + RL 的挑战，提出**分层 reward**（structure → format → content → validity）。4B 模型上 1000 样本达 80%+ 结构准确率。解决单一 reward 让模型在格式和内容间混淆的问题。

### 5. GRPO + LoRA 不稳定性（综合多源）
[GRPO++ blog](https://cameronrwolfe.substack.com/p/grpo-tricks) | [HF GRPO+LoRA handbook](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl) | [arXiv 2504.20834](https://arxiv.org/abs/2504.20834)

**已知问题**：GRPO + LoRA 低秩更新时 advantage 估计方差增大，TRL 默认 KL β=0.0，策略易大幅偏离。Full-token GRPO 在 LoRA 下"未能提升性能"。建议 β≥0.01、rank≥16、lr~1e-6。

---

## 综合诊断

你们的"先崩后恢复"是 **三因素叠加**：

1. **Alignment tax**：GRPO 梯度覆盖 SFT 关系抽取能力，rank=4 的 LoRA 参数同时承载旧能力和新优化目标，冲突剧烈
2. **KL 约束过弱（β=0.001）+ 低秩放大不稳定性**：策略快速偏离 SFT 分布，训练前 20 步即崩塌
3. **Reward proxy mismatch**：reward↑ 但 F1↓ 是经典 reward hacking——模型可能学会生成格式正确但关系错误的输出

U 型恢复的原因：崩塌后模型在新策略空间中缓慢重新发现部分抽取模式，但 LoRA 容量不足 + reward 噪声导致恢复不完全。

---

## 最值得尝试的 2 个方案

| | 方案 A：增强正则化 | 方案 B：分层 Reward |
|---|---|---|
| 改动 | KL β: 0.001→0.04, rank: 4→16, lr: 5e-6→1e-6 | reward 拆为 format + entity + relation，分权重 |
| 成本 | 低（改配置即可） | 中（需重写 reward 函数） |
| 针对问题 | 策略偏离过快 | reward hacking |
| 优先级 | **先试这个** | A 不够再加 |

备选方案 C：集成 Qwen 团队的 Online Merging Optimizer，每步锚定 SFT 方向，实现复杂度中等但同源验证过。

已将完整调研存入 `memory.md`，三个缓解方案存入 `ideas.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 199019,
  "duration_api_ms": 261876,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "de8d9cd7-1517-42eb-8250-45c1cd2d61f3",
  "total_cost_usd": 0.8958800000000002,
  "usage": {
    "input_tokens": 888,
    "cache_creation_input_tokens": 29934,
    "cache_read_input_tokens": 303115,
    "output_tokens": 6589,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29934,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1440,
        "cache_read_input_tokens": 40656,
        "cache_creation_input_tokens": 1119,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1119
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 234335,
      "outputTokens": 6747,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 12,
      "costUSD": 0.38806999999999997,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 888,
      "outputTokens": 6589,
      "cacheReadInputTokens": 303115,
      "cacheCreationInputTokens": 29934,
      "webSearchRequests": 0,
      "costUSD": 0.50781,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "94c59d7e-ee73-423c-b361-a96704c8f5a1"
}
```

</details>

---
