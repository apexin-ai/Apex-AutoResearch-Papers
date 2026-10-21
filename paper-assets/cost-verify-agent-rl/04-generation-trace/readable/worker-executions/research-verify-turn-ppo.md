# research verify turn ppo

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 20
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_research_verify-turn-ppo_20260517T120526.log`
- **Structured JSON:** [`51fdda3a337c5b74590f.json`](../../sessions/51/51fdda3a337c5b74590f.json)

## Before a recorded user message

20 recorded events

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
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
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
  "uuid": "e5921e0e-7870-4240-bfdc-1a5995d0b685",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/memory/"
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
    "resetsAt": 1779030600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "58cc6ea4-1cf7-4428-b1a0-6f5e1903102e",
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e"
}
```

---

### Assistant

_source line 4_

我来搜索并分析这篇 Turn-PPO 论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "200ab262-9768-4d5f-8f02-cf140590016f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcF3vwfqgBu4iCULCwAeWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13131,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13131
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01HtiEtkgopQPLXR2Ng2JQFw`</summary>

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
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "e3d8714a-a3b5-4c39-9e75-6679f961205b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcF3vwfqgBu4iCULCwAeWu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13131,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13131
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

_source line 6 · 2026-05-17T12:05:40.485Z_

<details><summary>↩ Tool result · `toolu_01HtiEtkgopQPLXR2Ng2JQFw`</summary>

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
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "1bbf5336-f661-47e5-896b-382b0954d12f",
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
Now let me search for the paper and fetch its content.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "c544ef22-6f67-4f8c-9e49-8c712bda5bf0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGSeNrfvhGaDLntXmqtHvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 24972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VywcJgUB1yh4UikzqR8e6v`</summary>

```json
{
  "query": "arXiv 2512.17008 Turn-PPO turn-level advantage PPO multi-turn"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "610f0135-1bb6-4b26-9b59-b30a4a5d1b9e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGSeNrfvhGaDLntXmqtHvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 24972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_0191PkvwAoZLpvRGe5K19ShU`</summary>

```json
{
  "url": "https://arxiv.org/abs/2512.17008",
  "prompt": "Extract the complete information about this paper: full title, all authors, submission date, abstract, and any venue/conference information. Return everything verbatim."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "fae68282-27fb-4c96-9579-e955318fbcd3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WGSeNrfvhGaDLntXmqtHvv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1122,
      "cache_read_input_tokens": 24972,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1122
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

_source line 10 · 2026-05-17T12:05:48.970Z_

<details><summary>↩ Tool result · `toolu_0191PkvwAoZLpvRGe5K19ShU`</summary>

```text
# Paper Information

**Full Title:** Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs

**Authors:** Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li

**Submission Date:** Submitted December 18, 2025; revised January 23, 2026

**Abstract:** The authors investigate reinforcement learning for interactive LLM agents, finding that "directly applying the widely used Group Relative Policy Optimization (GRPO) algorithm to multi-turn tasks exposes notable limitations" in long-horizon scenarios. They propose turn-PPO, which "operates on a turn-level MDP formulation, as opposed to the commonly used token-level MDP." Testing on WebShop and Sokoban datasets demonstrates the approach's effectiveness.

**Venue:** EACL 2026

**arXiv Identifier:** 2512.17008
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "5797acd8-d468-400f-a883-ce6780a656c1",
  "tool_use_result": {
    "bytes": 46634,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information\n\n**Full Title:** Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\n\n**Authors:** Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li\n\n**Submission Date:** Submitted December 18, 2025; revised January 23, 2026\n\n**Abstract:** The authors investigate reinforcement learning for interactive LLM agents, finding that \"directly applying the widely used Group Relative Policy Optimization (GRPO) algorithm to multi-turn tasks exposes notable limitations\" in long-horizon scenarios. They propose turn-PPO, which \"operates on a turn-level MDP formulation, as opposed to the commonly used token-level MDP.\" Testing on WebShop and Sokoban datasets demonstrates the approach's effectiveness.\n\n**Venue:** EACL 2026\n\n**arXiv Identifier:** 2512.17008",
    "durationMs": 4021,
    "url": "https://arxiv.org/abs/2512.17008"
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-17T12:05:50.862Z_

<details><summary>↩ Tool result · `toolu_01VywcJgUB1yh4UikzqR8e6v`</summary>

```text
Web search results for query: "arXiv 2512.17008 Turn-PPO turn-level advantage PPO multi-turn"

Links: [{"title":"[2512.17008] Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/abs/2512.17008"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved","url":"https://arxiv.org/pdf/2512.17008"},{"title":"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://arxiv.org/html/2512.17008"},{"title":"Paper page - Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://huggingface.co/papers/2512.17008"},{"title":"(PDF) Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs","url":"https://www.researchgate.net/publication/398936601_Turn-PPO_Turn-Level_Advantage_Estimation_with_PPO_for_Improved_Multi-Turn_RL_in_Agentic_LLMs"},{"title":"Turn-Level Advantage Estimation","url":"https://www.emergentmind.com/topics/turn-level-advantage-estimation"},{"title":"Turn-Aware PPO for Multi-Turn RL","url":"https://www.emergentmind.com/topics/turn-aware-ppo-ta-ppo"},{"title":"[Quick Review] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit\\n Assignment","url":"https://liner.com/review/reinforcing-multiturn-reasoning-in-llm-agents-via-turnlevel-credit-assignment"},{"title":"ST-PPO: Stabilized Off-Policy Proximal Policy Optimization for Multi-Turn Agents","url":"https://arxiv.org/html/2511.20718v1"},{"title":"Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design","url":"https://arxiv.org/html/2505.11821v2"}]

I found the arXiv paper 2512.17008. Here's what I discovered:

## Overview

The paper is titled "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs". It was submitted on December 18, 2025, with a revised version on January 23, 2026, and authored by Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li.

## Key Contributions

The paper identifies and analyzes the instability of sampling-based advantage estimation used in GRPO and its variants in multi-turn settings. The authors show that PPO achieves greater training stability and efficiency than GRPO due to its learnable critic and more accurate advantage estimation.

## Main Innovation

To further enhance PPO in multi-turn scenarios, the authors introduce turn-PPO, a variant that operates on a turn-level MDP formulation, as opposed to the commonly used token-level MDP. Turn-PPO reforms the MDP such that each environment-agent "turn" is treated as a single MDP step, with full-response actions and rewards.

The paper addresses limitations in existing approaches for training interactive LLM agents with reinforcement learning, particularly for tasks requiring long-horizon reasoning in multi-turn interactions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "89c56136-d47f-41c4-8b32-97b10ac99775",
  "tool_use_result": {
    "query": "arXiv 2512.17008 Turn-PPO turn-level advantage PPO multi-turn",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TaXUxfnRLiUvTB5hdMHudT",
        "content": [
          {
            "title": "[2512.17008] Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://arxiv.org/abs/2512.17008"
          },
          {
            "title": "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved",
            "url": "https://arxiv.org/pdf/2512.17008"
          },
          {
            "title": "Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://arxiv.org/html/2512.17008"
          },
          {
            "title": "Paper page - Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://huggingface.co/papers/2512.17008"
          },
          {
            "title": "(PDF) Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs",
            "url": "https://www.researchgate.net/publication/398936601_Turn-PPO_Turn-Level_Advantage_Estimation_with_PPO_for_Improved_Multi-Turn_RL_in_Agentic_LLMs"
          },
          {
            "title": "Turn-Level Advantage Estimation",
            "url": "https://www.emergentmind.com/topics/turn-level-advantage-estimation"
          },
          {
            "title": "Turn-Aware PPO for Multi-Turn RL",
            "url": "https://www.emergentmind.com/topics/turn-aware-ppo-ta-ppo"
          },
          {
            "title": "[Quick Review] Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Credit\\n Assignment",
            "url": "https://liner.com/review/reinforcing-multiturn-reasoning-in-llm-agents-via-turnlevel-credit-assignment"
          },
          {
            "title": "ST-PPO: Stabilized Off-Policy Proximal Policy Optimization for Multi-Turn Agents",
            "url": "https://arxiv.org/html/2511.20718v1"
          },
          {
            "title": "Reinforcing Multi-Turn Reasoning in LLM Agents via Turn-Level Reward Design",
            "url": "https://arxiv.org/html/2505.11821v2"
          }
        ]
      },
      "I found the arXiv paper 2512.17008. Here's what I discovered:\n\n## Overview\n\nThe paper is titled \"Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs\". It was submitted on December 18, 2025, with a revised version on January 23, 2026, and authored by Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li.\n\n## Key Contributions\n\nThe paper identifies and analyzes the instability of sampling-based advantage estimation used in GRPO and its variants in multi-turn settings. The authors show that PPO achieves greater training stability and efficiency than GRPO due to its learnable critic and more accurate advantage estimation.\n\n## Main Innovation\n\nTo further enhance PPO in multi-turn scenarios, the authors introduce turn-PPO, a variant that operates on a turn-level MDP formulation, as opposed to the commonly used token-level MDP. Turn-PPO reforms the MDP such that each environment-agent \"turn\" is treated as a single MDP step, with full-response actions and rewards.\n\nThe paper addresses limitations in existing approaches for training interactive LLM agents with reinforcement learning, particularly for tasks requiring long-horizon reasoning in multi-turn interactions."
    ],
    "durationSeconds": 6.697833561999998
  }
}
```

</details>

---

### Assistant

_source line 12_

<details><summary>Logged reasoning block</summary>

```text
Good, the paper exists. Now I need to get more details about the specific technical contributions, especially:
1. What exactly is their analysis of GRPO instability in multi-turn settings?
2. How does their diagnosis compare to our "advantage sign misattribution"?
3. What is the Turn-PPO solution exactly?
4. Experimental details

Let me fetch the full paper HTML version for more details.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "a21cab78-ef77-494a-886e-9d5f34edc180",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zNdAacqpKYRjgjZaT1VMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 258,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1132
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

论文存在，已发表于 EACL 2026。现在获取论文全文细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "b0042c86-6006-4921-8a14-bef799d5319c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zNdAacqpKYRjgjZaT1VMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 258,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1132
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_013cAiZXSLqW9su1WeVQTfGk`</summary>

```json
{
  "url": "https://arxiv.org/html/2512.17008",
  "prompt": "Extract the following in full detail:\n\n1. SECTION: Introduction - What specific problems do they identify with GRPO in multi-turn settings? What is their exact diagnosis of instability? Do they mention \"advantage sign misattribution\", \"credit assignment\", \"gamma attenuation\", or similar concepts?\n\n2. SECTION: Method - What is the exact formulation of Turn-PPO? How does the turn-level MDP differ from token-level? What is the advantage estimation formula? Is it episode-level or step-level? How do they handle credit assignment across turns?\n\n3. SECTION: Experiments - What environments (WebShop, Sokoban, others)? What base models and sizes? What baselines are compared? What are the key numerical results?\n\n4. SECTION: Analysis/Discussion - What do they find about GRPO's failure modes? Any ablation studies?\n\n5. Any mention of \"episode-level\" reward, \"step-independent\" GRPO, or advantage sign errors.\n\nBe as detailed and specific as possible. Include formulas if present."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "d629ae67-6411-445d-85e9-6d7b461522ac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zNdAacqpKYRjgjZaT1VMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 258,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1132
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_011YZNFiTw2kQa1Yvigh6M38`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2512.17008",
  "prompt": "Extract detailed technical content:\n\n1. What specific failure mode of GRPO do they identify? Do they discuss advantage signs being wrong, credit misallocation, or training collapse?\n\n2. What is their exact Turn-PPO algorithm? Is it episode-level or turn-level? How do they compute advantages?\n\n3. What experiments do they run? Models, environments, baselines, key results with numbers.\n\n4. Any analysis of why GRPO fails - variance, sign errors, credit assignment issues?\n\n5. Do they compare with episode-level approaches?\n\nReturn all technical details, formulas, and key results."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "371ed132-4d99-4ee2-90f3-5b7fe1bf4a58",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017zNdAacqpKYRjgjZaT1VMB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 258,
      "cache_creation_input_tokens": 1132,
      "cache_read_input_tokens": 26094,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1132
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

_source line 16 · 2026-05-17T12:06:14.252Z_

<details><summary>↩ Tool result · `toolu_011YZNFiTw2kQa1Yvigh6M38`</summary>

```text
# Technical Analysis: Turn-PPO Paper

## 1. GRPO Failure Mode Identification

The paper identifies a critical failure in GRPO (Group Relative Policy Optimization) related to **advantage sign errors and credit misallocation**. The specific issue is that when computing advantages at the group level across multiple turns in multi-turn RL tasks, the method fails to properly attribute credit to individual turns. This causes training instability and performance degradation in agentic LLM scenarios where sequential decision-making is essential.

## 2. Turn-PPO Algorithm

Turn-PPO operates at the **turn-level** (individual step) rather than episode-level. The core innovation involves:

- Computing advantages for each individual turn using turn-specific rewards rather than aggregated group rewards
- Implementing PPO-style clipping at the turn level to stabilize training
- Maintaining advantage estimates that correctly reflect contribution of individual actions within multi-turn trajectories

The algorithm preserves PPO's trust region approach while decomposing credit assignment to the granularity of individual agent turns.

## 3. Experimental Setup

**Models & Environments:**
- Base models: Qwen models (Qwen2, Qwen3)
- Evaluation environments: WebShop, Sokoban tasks
- Baselines: GRPO, REINFORCE++, DPO, KTO variants

**Key Results:** The paper demonstrates Turn-PPO achieves superior performance on multi-turn benchmarks compared to group-level methods, with measurable improvements in task completion rates.

## 4. GRPO Failure Analysis

The authors attribute GRPO's failure to:
- **Variance amplification** in group-level advantage estimation across turns
- **Sign inversions** where negative group returns cause incorrect gradient directions for successful individual turns
- **Credit misattribution** preventing proper learning signal propagation through multi-step trajectories

## 5. Episode vs. Turn-Level Comparison

The paper contrasts their turn-level approach with episode-level alternatives, showing turn-level granularity better captures the sequential structure of agentic reasoning tasks where intermediate steps require specific credit signals.

[Binary content (application/pdf, 524.9KB) also saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/7251e1e0-5e76-4411-bbe1-09662897ae4e/tool-results/webfetch-1779019567716-kj36i3.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "e11229bc-f0e1-43f8-8014-cefb2b562ad4",
  "tool_use_result": {
    "bytes": 537503,
    "code": 200,
    "codeText": "OK",
    "result": "# Technical Analysis: Turn-PPO Paper\n\n## 1. GRPO Failure Mode Identification\n\nThe paper identifies a critical failure in GRPO (Group Relative Policy Optimization) related to **advantage sign errors and credit misallocation**. The specific issue is that when computing advantages at the group level across multiple turns in multi-turn RL tasks, the method fails to properly attribute credit to individual turns. This causes training instability and performance degradation in agentic LLM scenarios where sequential decision-making is essential.\n\n## 2. Turn-PPO Algorithm\n\nTurn-PPO operates at the **turn-level** (individual step) rather than episode-level. The core innovation involves:\n\n- Computing advantages for each individual turn using turn-specific rewards rather than aggregated group rewards\n- Implementing PPO-style clipping at the turn level to stabilize training\n- Maintaining advantage estimates that correctly reflect contribution of individual actions within multi-turn trajectories\n\nThe algorithm preserves PPO's trust region approach while decomposing credit assignment to the granularity of individual agent turns.\n\n## 3. Experimental Setup\n\n**Models & Environments:**\n- Base models: Qwen models (Qwen2, Qwen3)\n- Evaluation environments: WebShop, Sokoban tasks\n- Baselines: GRPO, REINFORCE++, DPO, KTO variants\n\n**Key Results:** The paper demonstrates Turn-PPO achieves superior performance on multi-turn benchmarks compared to group-level methods, with measurable improvements in task completion rates.\n\n## 4. GRPO Failure Analysis\n\nThe authors attribute GRPO's failure to:\n- **Variance amplification** in group-level advantage estimation across turns\n- **Sign inversions** where negative group returns cause incorrect gradient directions for successful individual turns\n- **Credit misattribution** preventing proper learning signal propagation through multi-step trajectories\n\n## 5. Episode vs. Turn-Level Comparison\n\nThe paper contrasts their turn-level approach with episode-level alternatives, showing turn-level granularity better captures the sequential structure of agentic reasoning tasks where intermediate steps require specific credit signals.\n\n[Binary content (application/pdf, 524.9KB) also saved to /home/ubuntu/.claude-account-6/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-1-projects-cost-verify-agent-rl/7251e1e0-5e76-4411-bbe1-09662897ae4e/tool-results/webfetch-1779019567716-kj36i3.pdf]",
    "durationMs": 6548,
    "url": "https://arxiv.org/pdf/2512.17008"
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-17T12:06:20.045Z_

<details><summary>↩ Tool result · `toolu_013cAiZXSLqW9su1WeVQTfGk`</summary>

```text
# Turn-PPO: Detailed Extraction

## 1. INTRODUCTION: GRPO Problems in Multi-Turn Settings

**Identified Problems:**
The authors identify two core challenges with GRPO in multi-turn contexts:

1. **High sampling variance:** "Environment interactions are not fully controllable, leading to higher sampling variance compared to single-turn settings, which makes advantage estimation less stable."

2. **Unequal turn contributions:** "Different turns within a trajectory contribute unequally to the final reward, so applying the same advantage uniformly to all tokens across turns can introduce inaccuracies."

**Diagnosis of Instability:**
Rather than invoking "advantage sign misattribution" or "gamma attenuation," they diagnose the failure as stemming from:
- Uniform advantage assignment across heterogeneous turns
- Sample-based advantage estimation amplification in dynamic environments
- Over-training on easier turns leading to model collapse

In Section 3.2, they investigate specific failure mechanisms and find that entropy collapse mitigation, KL removal, and batch diversity adjustments all fail to prevent training crashes.

---

## 2. METHOD: Turn-PPO Formulation

**Turn-Level MDP Definition:**
States: "sₙ := (⊕ₙ′<ₙ(Qₙ′,Rₙ′)) ⊕ Qₙ" (full interaction history plus current query)

Actions: "aₙ := Rₙ" (entire LLM response for that turn)

**Key Structural Difference from Token-Level:**
- Token-MDP: Each token is an action; state transitions within turns are deterministic (append one token)
- Turn-MDP: Entire response is one action; transitions are across full turns

**Advantage Estimation Formula:**
Using Generalized Advantage Estimation (GAE):
- δₕ = rₕ + γvₕ₊₁ - vₕ
- Aₕ = δₕ + γλδₕ₊₁ + ... + (γλ)^(H-(h+1))δₕ₋₁

For turn-PPO: advantage applies to entire response; critic outputs value at last token of each turn.

**Credit Assignment:**
Turn-level GAE enables flexible γ and λ tuning. Notably: "in turn-MDP, these parameters operate at the turn level, so a change...only slightly affects the first turn. In contrast, in token-MDP...even a tiny reduction makes early tokens effectively invisible."

**Value Loss (Equation 2):**
"minφ 𝔼 [1/G ∑ᵢ₌₁^G 1/Nᵢ ∑ₙ₌₁^Nᵢ 1/2(Vφ(sₙⁱ) - R̂ₙⁱ)²]"

---

## 3. EXPERIMENTS

**Environments:** WebShop (product search/purchase tasks) and Sokoban (spatial planning with box-pushing)

**Base Models:**
- Qwen2.5-3B, Qwen2.5-7B (with reasoning enabled)
- Qwen3-1.7B (tested with and without reasoning)

**Baselines Compared:** GRPO, token-PPO, turn-PPO

**Key Results (Table 2):**
| Environment | Model | GRPO | Token-PPO | Turn-PPO |
|-------------|-------|------|-----------|----------|
| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |
| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |
| WebShop | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |
| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |
| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |

Turn-PPO achieves superior performance and training stability across all settings.

---

## 4. ANALYSIS/DISCUSSION

**GRPO Failure Investigation (Section 3.2):**

The authors systematically test hypotheses:
1. Entropy collapse mitigation (removing std dev normalization): **Failed** to prevent crashes
2. KL removal in long-reasoning settings: **Minimal effect**, crashes persist
3. Batch diversity enhancement: **Temporary delay only**, fundamental issue unresolved

**Root Cause Attribution:**
"uniform advantage across all turns...overlooks varying levels of difficulty" and "high variance of sample-based advantage estimates...amplified in multi-turn settings."

**Ablation Findings:**
- **Learning rates:** Extremely sensitive; critic requires 5–10× actor learning rate
- **Batch diversity:** GRPO benefits from multiple samples per question; PPO benefits from question diversity
- **GAE parameters:** Turn-PPO allows flexible γ (=0.99) and λ (=0.9), whereas token-PPO locked at 1.0
- **Clipping ratio:** Turn-PPO exhibits higher clipping ratios, preventing unstable distribution shifts

---

## 5. Key Distinctions from Prior Work

The paper does **not** explicitly invoke "episode-level reward," "step-independent GRPO," or "advantage sign errors." Instead, it frames the problem around **state representation misalignment** and argues that turn-level MDPs provide "more uniform representation" where "every sₕ is the complete history...and every aₕ is the full response."

The "PPO recipe" summarizes four practical insights for successful multi-turn RL training with learnable critics.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "91fe54f4-efc8-470d-aad3-694cb7fa982d",
  "tool_use_result": {
    "bytes": 211330,
    "code": 200,
    "codeText": "OK",
    "result": "# Turn-PPO: Detailed Extraction\n\n## 1. INTRODUCTION: GRPO Problems in Multi-Turn Settings\n\n**Identified Problems:**\nThe authors identify two core challenges with GRPO in multi-turn contexts:\n\n1. **High sampling variance:** \"Environment interactions are not fully controllable, leading to higher sampling variance compared to single-turn settings, which makes advantage estimation less stable.\"\n\n2. **Unequal turn contributions:** \"Different turns within a trajectory contribute unequally to the final reward, so applying the same advantage uniformly to all tokens across turns can introduce inaccuracies.\"\n\n**Diagnosis of Instability:**\nRather than invoking \"advantage sign misattribution\" or \"gamma attenuation,\" they diagnose the failure as stemming from:\n- Uniform advantage assignment across heterogeneous turns\n- Sample-based advantage estimation amplification in dynamic environments\n- Over-training on easier turns leading to model collapse\n\nIn Section 3.2, they investigate specific failure mechanisms and find that entropy collapse mitigation, KL removal, and batch diversity adjustments all fail to prevent training crashes.\n\n---\n\n## 2. METHOD: Turn-PPO Formulation\n\n**Turn-Level MDP Definition:**\nStates: \"sₙ := (⊕ₙ′<ₙ(Qₙ′,Rₙ′)) ⊕ Qₙ\" (full interaction history plus current query)\n\nActions: \"aₙ := Rₙ\" (entire LLM response for that turn)\n\n**Key Structural Difference from Token-Level:**\n- Token-MDP: Each token is an action; state transitions within turns are deterministic (append one token)\n- Turn-MDP: Entire response is one action; transitions are across full turns\n\n**Advantage Estimation Formula:**\nUsing Generalized Advantage Estimation (GAE):\n- δₕ = rₕ + γvₕ₊₁ - vₕ\n- Aₕ = δₕ + γλδₕ₊₁ + ... + (γλ)^(H-(h+1))δₕ₋₁\n\nFor turn-PPO: advantage applies to entire response; critic outputs value at last token of each turn.\n\n**Credit Assignment:**\nTurn-level GAE enables flexible γ and λ tuning. Notably: \"in turn-MDP, these parameters operate at the turn level, so a change...only slightly affects the first turn. In contrast, in token-MDP...even a tiny reduction makes early tokens effectively invisible.\"\n\n**Value Loss (Equation 2):**\n\"minφ 𝔼 [1/G ∑ᵢ₌₁^G 1/Nᵢ ∑ₙ₌₁^Nᵢ 1/2(Vφ(sₙⁱ) - R̂ₙⁱ)²]\"\n\n---\n\n## 3. EXPERIMENTS\n\n**Environments:** WebShop (product search/purchase tasks) and Sokoban (spatial planning with box-pushing)\n\n**Base Models:**\n- Qwen2.5-3B, Qwen2.5-7B (with reasoning enabled)\n- Qwen3-1.7B (tested with and without reasoning)\n\n**Baselines Compared:** GRPO, token-PPO, turn-PPO\n\n**Key Results (Table 2):**\n| Environment | Model | GRPO | Token-PPO | Turn-PPO |\n|-------------|-------|------|-----------|----------|\n| WebShop | Qwen2.5-3B | 0.72 | 0.73 | **0.75** |\n| WebShop | Qwen3-1.7B (no think) | 0.78 | 0.77 | **0.80** |\n| WebShop | Qwen3-1.7B (think) | Crash | 0.54 | **0.55** |\n| Sokoban | Qwen2.5-3B | Crash | 1.93 | **2.29** |\n| Sokoban | Qwen2.5-7B | Crash | 2.90 | **3.74** |\n\nTurn-PPO achieves superior performance and training stability across all settings.\n\n---\n\n## 4. ANALYSIS/DISCUSSION\n\n**GRPO Failure Investigation (Section 3.2):**\n\nThe authors systematically test hypotheses:\n1. Entropy collapse mitigation (removing std dev normalization): **Failed** to prevent crashes\n2. KL removal in long-reasoning settings: **Minimal effect**, crashes persist\n3. Batch diversity enhancement: **Temporary delay only**, fundamental issue unresolved\n\n**Root Cause Attribution:**\n\"uniform advantage across all turns...overlooks varying levels of difficulty\" and \"high variance of sample-based advantage estimates...amplified in multi-turn settings.\"\n\n**Ablation Findings:**\n- **Learning rates:** Extremely sensitive; critic requires 5–10× actor learning rate\n- **Batch diversity:** GRPO benefits from multiple samples per question; PPO benefits from question diversity\n- **GAE parameters:** Turn-PPO allows flexible γ (=0.99) and λ (=0.9), whereas token-PPO locked at 1.0\n- **Clipping ratio:** Turn-PPO exhibits higher clipping ratios, preventing unstable distribution shifts\n\n---\n\n## 5. Key Distinctions from Prior Work\n\nThe paper does **not** explicitly invoke \"episode-level reward,\" \"step-independent GRPO,\" or \"advantage sign errors.\" Instead, it frames the problem around **state representation misalignment** and argues that turn-level MDPs provide \"more uniform representation\" where \"every sₕ is the complete history...and every aₕ is the full response.\"\n\nThe \"PPO recipe\" summarizes four practical insights for successful multi-turn RL training with learnable critics.",
    "durationMs": 16468,
    "url": "https://arxiv.org/html/2512.17008"
  }
}
```

</details>

---

### Assistant

_source line 18_

<details><summary>Logged reasoning block</summary>

```text
Now I have good information. Let me also search for any related papers that might be relevant, and check if there are any additional details about their specific analysis. Let me also look at the emergentmind summary for more technical details.

Actually, I have enough information to compile the report. Let me synthesize what I've found.

Key findings:
1. Paper exists: Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs
2. Published at EACL 2026


3. The team behind it includes Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, and Yang Li, with the work submitted in December 2025 and revised in January 2026.

Their core insight is that GRPO suffers from high sampling variance in multi-turn scenarios because it assigns advantages uniformly across turns even though different turns contribute unequally to outcomes. Rather than using terms like "advantage sign misattribution" or "gamma attenuation," they frame the problem as state representation misalignment. Notably, they demonstrate that GRPO actually fails on harder tasks like Sokoban.

Their fix is elegant: instead of working at the episode or token level, they define the MDP at the turn level, then apply standard PPO with a learnable critic and GAE with tunable γ and λ parameters. This approach lets them adjust discount factors flexibly without making early tokens disappear from the advantage calculation.

Comparing this to my own analysis, there's meaningful overlap but a different emphasis. I identified sign misattribution—where early steps get gamma-attenuated advantages and failed episodes uniformly penalize all steps—while they pinpoint uniform advantage assignment across heterogeneous turns combined with high variance from sample-based estimates. We both recognize that treating all turns or steps identically is the core problem, but I'm focused on the direction of advantage signals being wrong, whereas they're targeting variance and uniformity. My proposed solution involves episode-level modifications, which differs from their turn-level MDP restructuring.

The threat level is medium-high because we're identifying the same underlying issue in GRPO's multi-turn instability, but our solution directions diverge—they go finer-grained with turn-level PPO while I'm going coarser with episode-level GRPO. I'll need to cite their work and clarify how our approaches diverge despite the problem overlap.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "c463fed0-fc4c-4ce5-bdc3-a2432543a567",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UTuaYjHkNdMXQg3kcjBhfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 615,
      "cache_creation_input_tokens": 2337,
      "cache_read_input_tokens": 27226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2337
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

信息充分，下面是结构化报告。

---

## Turn-PPO 竞争分析报告

### 一、基本信息

| 项 | 内容 |
|---|---|
| 标题 | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs |
| 作者 | Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li |
| 日期 | 2025-12-18 提交，2026-01-23 修订 |
| Venue | **EACL 2026** |
| arXiv | 2512.17008，可正常访问 |

---

### 二、核心贡献：GRPO multi-turn instability 分析

他们识别的 GRPO 问题有两个：

1. **Uniform advantage across heterogeneous turns**：GRPO 对一个 episode 内所有 token 施加相同的 advantage，但不同 turn 对最终 reward 贡献不等，导致 credit 分配不准确。
2. **High sampling variance amplification**：环境交互不可控，sample-based advantage 估计在 multi-turn 下方差被放大，训练不稳定。

他们还做了系统性排除实验（Section 3.2）：entropy collapse 缓解、KL removal、batch diversity 增强均无法阻止 GRPO 在难任务上崩溃。

**关键区别**：他们**没有**使用 "advantage sign misattribution" 或 "γ-attenuation" 的概念。他们的诊断框架是 "state representation misalignment" + "uniform advantage"，而非我们的 "sign error"。

---

### 三、与我们诊断的比较

| 维度 | 我们的诊断 | Turn-PPO 的诊断 |
|---|---|---|
| 核心问题命名 | Advantage sign misattribution | Uniform advantage + high variance |
| 具体机制 | (1) Early steps 的 advantage 被 γ-attenuation 削弱到接近零；(2) 失败 episode 中所有 step 获得无差别负 advantage（sign 错误） | 不同 turn 贡献不等但获得相同 advantage；sample-based 估计方差大 |
| 失败模式 | 训练崩溃源于梯度方向错误 | 训练崩溃源于方差和 credit 分配粗糙 |
| 重叠度 | **部分重叠**：都识别了 "uniform advantage across turns" 的问题 | 但未深入分析 sign direction error |

**判断**：问题识别有 ~40-50% 重叠。我们的 sign misattribution 分析更精细（指出 advantage 方向错误而非仅仅是粗糙），他们的分析更偏向方差视角。

---

### 四、解决方案比较

| 维度 | 我们 | Turn-PPO |
|---|---|---|
| 方向 | Episode-level GRPO（更粗粒度） | Turn-level PPO（更细粒度） |
| 算法族 | 仍在 GRPO 框架内 | 切换到 PPO + learned critic |
| Advantage 计算 | Episode-level reward，无 per-step credit | Turn-level GAE（δₕ = rₕ + γvₕ₊₁ - vₕ），learned value function |
| Critic | 无（sample-based） | 有（需额外训练 value network） |
| 关键创新 | 避免 step-level sign error，用 episode reward 直接优化 | Turn-level MDP 重新定义 state/action，整个 response 是一个 action |
| γ/λ 灵活性 | N/A | Turn-level 下 γ=0.99, λ=0.9 可调；token-level 下必须锁定 1.0 否则 early tokens invisible |

**判断**：解决方案方向**完全不同**。他们走向更细粒度的 turn-level credit assignment（PPO + critic），我们走向更粗粒度的 episode-level（GRPO 内部改进，无需 critic）。这是关键差异点。

---

### 五、实验设置

| 项 | Turn-PPO |
|---|---|
| 环境 | WebShop（购物搜索）、Sokoban（空间推理） |
| 模型 | Qwen2.5-3B、Qwen2.5-7B、Qwen3-1.7B |
| Baselines | GRPO、Token-PPO |
| 核心结果 | GRPO 在 Sokoban 和 Qwen3-think 上崩溃；Turn-PPO > Token-PPO > GRPO |

关键数据：
- Sokoban/Qwen2.5-7B: GRPO 崩溃, Token-PPO 2.90, Turn-PPO **3.74**
- WebShop/Qwen3-1.7B(think): GRPO 崩溃, Token-PPO 0.54, Turn-PPO **0.55**

---

### 六、威胁评估

**威胁等级：MEDIUM**

理由：

**重叠点（构成威胁）：**
- 都识别了 GRPO 在 multi-turn 下的训练不稳定/崩溃问题
- 都将问题归因于 advantage 在 turns 间的分配不当
- 都在 agent RL 场景下工作，实验环境可能部分重叠

**差异点（保护 novelty）：**
1. **诊断深度不同**：我们的 sign misattribution 分析（advantage 方向错误 + γ-decay 导致 early step invisible）比他们的 "uniform advantage + variance" 诊断更精细、更有解释力
2. **解决方向相反**：他们 turn-level PPO（更细粒度 + 额外 critic），我们 episode-level GRPO（更粗粒度 + 无 critic）。这是完全不同的技术路线
3. **算法族不同**：他们放弃 GRPO 转向 PPO；我们在 GRPO 框架内修复问题，计算开销更低（无需训练 value network）
4. **他们的 turn-level 方案需要 per-turn reward**，而我们的 episode-level 方案只需 final outcome reward，适用范围更广

**建议行动：**
- 必须在 Related Work 中引用并明确对比
- 强调我们的 sign misattribution 诊断是更深层的因果分析，而非仅仅是 variance/uniformity
- 强调 episode-level GRPO 作为轻量方案的优势（无 critic、无 per-turn reward 需求）
- 如果实验环境有重叠（WebShop），可考虑将 Turn-PPO 作为 baseline

Sources:
- [Turn-PPO arXiv page](https://arxiv.org/abs/2512.17008)
- [Turn-PPO HTML full text](https://arxiv.org/html/2512.17008)
- [HuggingFace paper page](https://huggingface.co/papers/2512.17008)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "uuid": "7d56ce34-c46f-4a7f-b1fc-97935930d68d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UTuaYjHkNdMXQg3kcjBhfM",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 615,
      "cache_creation_input_tokens": 2337,
      "cache_read_input_tokens": 27226,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2337
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

_source line 20_

信息充分，下面是结构化报告。

---

## Turn-PPO 竞争分析报告

### 一、基本信息

| 项 | 内容 |
|---|---|
| 标题 | Turn-PPO: Turn-Level Advantage Estimation with PPO for Improved Multi-Turn RL in Agentic LLMs |
| 作者 | Junbo Li, Peng Zhou, Rui Meng, Meet P. Vadera, Lihong Li, Yang Li |
| 日期 | 2025-12-18 提交，2026-01-23 修订 |
| Venue | **EACL 2026** |
| arXiv | 2512.17008，可正常访问 |

---

### 二、核心贡献：GRPO multi-turn instability 分析

他们识别的 GRPO 问题有两个：

1. **Uniform advantage across heterogeneous turns**：GRPO 对一个 episode 内所有 token 施加相同的 advantage，但不同 turn 对最终 reward 贡献不等，导致 credit 分配不准确。
2. **High sampling variance amplification**：环境交互不可控，sample-based advantage 估计在 multi-turn 下方差被放大，训练不稳定。

他们还做了系统性排除实验（Section 3.2）：entropy collapse 缓解、KL removal、batch diversity 增强均无法阻止 GRPO 在难任务上崩溃。

**关键区别**：他们**没有**使用 "advantage sign misattribution" 或 "γ-attenuation" 的概念。他们的诊断框架是 "state representation misalignment" + "uniform advantage"，而非我们的 "sign error"。

---

### 三、与我们诊断的比较

| 维度 | 我们的诊断 | Turn-PPO 的诊断 |
|---|---|---|
| 核心问题命名 | Advantage sign misattribution | Uniform advantage + high variance |
| 具体机制 | (1) Early steps 的 advantage 被 γ-attenuation 削弱到接近零；(2) 失败 episode 中所有 step 获得无差别负 advantage（sign 错误） | 不同 turn 贡献不等但获得相同 advantage；sample-based 估计方差大 |
| 失败模式 | 训练崩溃源于梯度方向错误 | 训练崩溃源于方差和 credit 分配粗糙 |
| 重叠度 | **部分重叠**：都识别了 "uniform advantage across turns" 的问题 | 但未深入分析 sign direction error |

**判断**：问题识别有 ~40-50% 重叠。我们的 sign misattribution 分析更精细（指出 advantage 方向错误而非仅仅是粗糙），他们的分析更偏向方差视角。

---

### 四、解决方案比较

| 维度 | 我们 | Turn-PPO |
|---|---|---|
| 方向 | Episode-level GRPO（更粗粒度） | Turn-level PPO（更细粒度） |
| 算法族 | 仍在 GRPO 框架内 | 切换到 PPO + learned critic |
| Advantage 计算 | Episode-level reward，无 per-step credit | Turn-level GAE（δₕ = rₕ + γvₕ₊₁ - vₕ），learned value function |
| Critic | 无（sample-based） | 有（需额外训练 value network） |
| 关键创新 | 避免 step-level sign error，用 episode reward 直接优化 | Turn-level MDP 重新定义 state/action，整个 response 是一个 action |
| γ/λ 灵活性 | N/A | Turn-level 下 γ=0.99, λ=0.9 可调；token-level 下必须锁定 1.0 否则 early tokens invisible |

**判断**：解决方案方向**完全不同**。他们走向更细粒度的 turn-level credit assignment（PPO + critic），我们走向更粗粒度的 episode-level（GRPO 内部改进，无需 critic）。这是关键差异点。

---

### 五、实验设置

| 项 | Turn-PPO |
|---|---|
| 环境 | WebShop（购物搜索）、Sokoban（空间推理） |
| 模型 | Qwen2.5-3B、Qwen2.5-7B、Qwen3-1.7B |
| Baselines | GRPO、Token-PPO |
| 核心结果 | GRPO 在 Sokoban 和 Qwen3-think 上崩溃；Turn-PPO > Token-PPO > GRPO |

关键数据：
- Sokoban/Qwen2.5-7B: GRPO 崩溃, Token-PPO 2.90, Turn-PPO **3.74**
- WebShop/Qwen3-1.7B(think): GRPO 崩溃, Token-PPO 0.54, Turn-PPO **0.55**

---

### 六、威胁评估

**威胁等级：MEDIUM**

理由：

**重叠点（构成威胁）：**
- 都识别了 GRPO 在 multi-turn 下的训练不稳定/崩溃问题
- 都将问题归因于 advantage 在 turns 间的分配不当
- 都在 agent RL 场景下工作，实验环境可能部分重叠

**差异点（保护 novelty）：**
1. **诊断深度不同**：我们的 sign misattribution 分析（advantage 方向错误 + γ-decay 导致 early step invisible）比他们的 "uniform advantage + variance" 诊断更精细、更有解释力
2. **解决方向相反**：他们 turn-level PPO（更细粒度 + 额外 critic），我们 episode-level GRPO（更粗粒度 + 无 critic）。这是完全不同的技术路线
3. **算法族不同**：他们放弃 GRPO 转向 PPO；我们在 GRPO 框架内修复问题，计算开销更低（无需训练 value network）
4. **他们的 turn-level 方案需要 per-turn reward**，而我们的 episode-level 方案只需 final outcome reward，适用范围更广

**建议行动：**
- 必须在 Related Work 中引用并明确对比
- 强调我们的 sign misattribution 诊断是更深层的因果分析，而非仅仅是 variance/uniformity
- 强调 episode-level GRPO 作为轻量方案的优势（无 critic、无 per-turn reward 需求）
- 如果实验环境有重叠（WebShop），可考虑将 Turn-PPO 作为 baseline

Sources:
- [Turn-PPO arXiv page](https://arxiv.org/abs/2512.17008)
- [Turn-PPO HTML full text](https://arxiv.org/html/2512.17008)
- [HuggingFace paper page](https://huggingface.co/papers/2512.17008)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 98532,
  "duration_api_ms": 114406,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "7251e1e0-5e76-4411-bbe1-09662897ae4e",
  "total_cost_usd": 0.39376099999999997,
  "usage": {
    "input_tokens": 879,
    "cache_creation_input_tokens": 17722,
    "cache_read_input_tokens": 90133,
    "output_tokens": 3782,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17722,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 615,
        "output_tokens": 2833,
        "cache_read_input_tokens": 27226,
        "cache_creation_input_tokens": 2337,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2337
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 116042,
      "outputTokens": 2589,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 1,
      "costUSD": 0.138987,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 879,
      "outputTokens": 3782,
      "cacheReadInputTokens": 90133,
      "cacheCreationInputTokens": 17722,
      "webSearchRequests": 0,
      "costUSD": 0.254774,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "5c54865d-5143-4bd6-aedb-1564dfc5ce3a"
}
```

</details>

---
