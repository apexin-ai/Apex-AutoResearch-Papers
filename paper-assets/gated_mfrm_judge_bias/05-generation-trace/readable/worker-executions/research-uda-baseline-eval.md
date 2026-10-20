# research uda baseline eval

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 60
- **Recorded user turns:** 0
- **Tool calls:** 21
- **Original source:** `logs/workers/worker_research_uda_baseline_eval_20260522T004400.log`
- **Structured JSON:** [`8968b83f2c6cef74a6fc.json`](../../sessions/89/8968b83f2c6cef74a6fc.json)

## Before a recorded user message

60 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias",
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
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
  "uuid": "14a29824-c835-490a-baf7-3b2eb2a9ce30",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-prod43-projects-gated-mfrm-judge-bias/memory/"
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
    "resetsAt": 1779421800,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "703a9983-da46-4601-8075-6bec70af488f",
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to research the UDA (Unified Debiasing Approach) baseline for their G-MFRM project. Let me start by searching for information about this paper and its code availability. I'll need to use web search and check GitHub for code.

Let me first look at the project context to understand what G-MFRM is and what exp-004 entails.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "c5bcfa18-e7f0-4507-acf9-82b42b85a89d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bkTRBz83TNPwZqu9LmR1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12514,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12514
      },
      "output_tokens": 31,
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

I'll research UDA code availability and method details in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "8fd05fac-c265-4707-a396-dd941bfeb39a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bkTRBz83TNPwZqu9LmR1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12514,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12514
      },
      "output_tokens": 31,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011jetPCcTd14ateuDjfYcH3`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
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
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "092127ff-ab29-4eb6-93c1-c7d6f521542f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012bkTRBz83TNPwZqu9LmR1Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12514,
      "cache_read_input_tokens": 11447,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12514
      },
      "output_tokens": 31,
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

_source line 7 · 2026-05-22T00:44:17.171Z_

<details><summary>↩ Tool result · `toolu_011jetPCcTd14ateuDjfYcH3`</summary>

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
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "2b4d1ec8-1ec7-430c-a555-696e72513f79",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Let me search for UDA paper and code, and also read the project's roadmap/memory for context on what UDA is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "41aafe7a-d30d-4406-8c4b-0c5e9dadd0b0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dUPm4kUxpiexLMHZGSEJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1053
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PJYgqjjk2tbFn6g2LVLST1`</summary>

```json
{
  "query": "UDA \"Unified Debiasing Approach\" LLM judge bias paper code github"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "458b2477-ebe2-41ad-a1e4-a339b249e6ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dUPm4kUxpiexLMHZGSEJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1053
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PXmsicucuUvKAQav8dJw5C`</summary>

```json
{
  "query": "\"unified debiasing approach\" LLM evaluator debiasing arxiv 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "aae5ba5f-d315-4a65-98f9-54d8e240edfd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dUPm4kUxpiexLMHZGSEJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1053
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

_source line 11_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01WmS247AgJz3Cf2T6fuA19U`</summary>

```json
{
  "project": "gated_mfrm_judge_bias",
  "file": "ROADMAP.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "eb3366ba-c96b-456d-b7e0-4527bf597fa9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017dUPm4kUxpiexLMHZGSEJY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 23961,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1053
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

_source line 12 · 2026-05-22T00:44:26.068Z_

<details><summary>↩ Tool result · `toolu_01PJYgqjjk2tbFn6g2LVLST1`</summary>

```text
Web search results for query: "UDA "Unified Debiasing Approach" LLM judge bias paper code github"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"}]

Based on the search results, I found the UDA paper you're looking for:

**Paper Details:**
UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.

**Key Results:**
UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

**Code Availability:**
Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4

**Publication:**
The paper has been published in the proceedings of the AAAI Conference on Artificial Intelligence (2026). You can also find it on arXiv (2508.09724) and the AAAI proceedings website.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "5754f6cc-518b-4b87-b04f-715a1ea15a47",
  "tool_use_result": {
    "query": "UDA \"Unified Debiasing Approach\" LLM judge bias paper code github",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PnU7TUqC5WkNRq8gLhgkBW",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          }
        ]
      },
      "Based on the search results, I found the UDA paper you're looking for:\n\n**Paper Details:**\nUDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.\n\n**Key Results:**\nUDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.\n\n**Code Availability:**\nCode and data are available at https://anonymous.4open.science/r/62AB93CD-23B4\n\n**Publication:**\nThe paper has been published in the proceedings of the AAAI Conference on Artificial Intelligence (2026). You can also find it on arXiv (2508.09724) and the AAAI proceedings website."
    ],
    "durationSeconds": 4.590081416000001
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-22T00:44:30.758Z_

<details><summary>↩ Tool result · `toolu_01PXmsicucuUvKAQav8dJw5C`</summary>

```text
Web search results for query: ""unified debiasing approach" LLM evaluator debiasing arxiv 2024 2025"

Links: [{"title":"Preference Leakage: A Contamination Problem in LLM-as- ...","url":"https://arxiv.org/pdf/2502.01534"},{"title":"Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines","url":"https://arxiv.org/html/2604.23178v1"},{"title":"Towards Universal Debiasing for Language Models-based Tabular Data Generation","url":"https://arxiv.org/pdf/2509.16475"},{"title":"Towards Universal Debiasing for Language Models-based Tabular Data Generation","url":"https://arxiv.org/html/2509.16475"},{"title":"Do LLM Evaluators Prefer Themselves for a Reason?","url":"https://arxiv.org/html/2504.03846v1"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"[2409.13884] A Multi-LLM Debiasing Framework","url":"https://arxiv.org/abs/2409.13884"}]

I've performed a web search on "unified debiasing approach LLM evaluator arxiv 2024 2025". Here are the relevant results:

## Key Papers Found:

1. **Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines** (2025)
   - This paper systematically evaluates multiple bias mitigation strategies including position swapping, multi-model panels, chain-of-thought prompting, debiased training data, and architectural diversity.

2. **UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge** (2025)
   - This work addresses the 'LLM-as-a-judge' paradigm where a large model acts as an autonomous judge to score, rank or critique outputs, and proposes methods for debiasing through consensus among judges.

3. **A Multi-LLM Debiasing Framework** (September 2024)
   - This paper proposes a novel multi-LLM debiasing framework with a centralized method (single central LLM) and a decentralized method (all models communicate directly).

4. **Do LLM Evaluators Prefer Themselves for a Reason?** (April 2025)
   - LLM-Eval introduces a unified approach that prompts an LLM to assess multiple quality dimensions of open-domain conversations.

5. **Towards Universal Debiasing for Language Models-based Tabular Data Generation** (2024)
   - This work proposes two complementary methods: a direct preference optimization (DPO)-based strategy called UDF-DPO, and a targeted debiasing technique called UDF-MIX.

These papers represent recent research efforts on debiasing LLM evaluators and addressing bias in LLM-based evaluation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "1f034432-0374-4160-a0c9-cf79c2753192",
  "tool_use_result": {
    "query": "\"unified debiasing approach\" LLM evaluator debiasing arxiv 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01C9kWRbXHM8vrEkqN1MHUAt",
        "content": [
          {
            "title": "Preference Leakage: A Contamination Problem in LLM-as- ...",
            "url": "https://arxiv.org/pdf/2502.01534"
          },
          {
            "title": "Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines",
            "url": "https://arxiv.org/html/2604.23178v1"
          },
          {
            "title": "Towards Universal Debiasing for Language Models-based Tabular Data Generation",
            "url": "https://arxiv.org/pdf/2509.16475"
          },
          {
            "title": "Towards Universal Debiasing for Language Models-based Tabular Data Generation",
            "url": "https://arxiv.org/html/2509.16475"
          },
          {
            "title": "Do LLM Evaluators Prefer Themselves for a Reason?",
            "url": "https://arxiv.org/html/2504.03846v1"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "[2409.13884] A Multi-LLM Debiasing Framework",
            "url": "https://arxiv.org/abs/2409.13884"
          }
        ]
      },
      "I've performed a web search on \"unified debiasing approach LLM evaluator arxiv 2024 2025\". Here are the relevant results:\n\n## Key Papers Found:\n\n1. **Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines** (2025)\n   - This paper systematically evaluates multiple bias mitigation strategies including position swapping, multi-model panels, chain-of-thought prompting, debiased training data, and architectural diversity.\n\n2. **UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge** (2025)\n   - This work addresses the 'LLM-as-a-judge' paradigm where a large model acts as an autonomous judge to score, rank or critique outputs, and proposes methods for debiasing through consensus among judges.\n\n3. **A Multi-LLM Debiasing Framework** (September 2024)\n   - This paper proposes a novel multi-LLM debiasing framework with a centralized method (single central LLM) and a decentralized method (all models communicate directly).\n\n4. **Do LLM Evaluators Prefer Themselves for a Reason?** (April 2025)\n   - LLM-Eval introduces a unified approach that prompts an LLM to assess multiple quality dimensions of open-domain conversations.\n\n5. **Towards Universal Debiasing for Language Models-based Tabular Data Generation** (2024)\n   - This work proposes two complementary methods: a direct preference optimization (DPO)-based strategy called UDF-DPO, and a targeted debiasing technique called UDF-MIX.\n\nThese papers represent recent research efforts on debiasing LLM evaluators and addressing bias in LLM-based evaluation systems."
    ],
    "durationSeconds": 8.365852597999998
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-22T00:44:30.783Z_

<details><summary>↩ Tool result · `toolu_01WmS247AgJz3Cf2T6fuA19U`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 23:05 UTC | 更新原因: Dream R2 定稿（修正分数），exp-009/012 已 approved+allocated，novelty 天花板应对策略\\n\\n## 核心方向\\nG-MFRM 通过 staged joint calibration 统一校正 LLM 评测中的 judge bias 和 contamination。核心 insight: sequential 方法中 judge severity 与 contamination 存在 omitted variable confounding，joint estimation 方法论必要。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-21 通过）\\n- MVP 验证链: mvp_001→002→003 (PASS: RMSE −43.8%, R̂=1.03, ESS=224)\\n- Dream R1: Best=3.5, Median=3.0, Worst=2.5 → framing 修改（staged joint, Observation）\\n- Dream R2: **Best=3.0, Median=3.0, Worst=2.5** → novelty 天花板确认，不再 re-dream\\n- **exp-009 ALLOCATED cuda:0** (formal OVB observation + c_n validation, ~6h)\\n- **exp-012 ALLOCATED cuda:1** (error propagation sensitivity, ~1.5h)\\n- Framing 已更新：novelty 补充策略 + bibliography 策略 + Tier B+ contingency\\n\\n## Novelty 天花板应对\\nDream R2 Best 从 3.5→3.0：即使数据最理想，\\\"MFRM+1 term\\\" + \\\"textbook OVB\\\" 被视为 combinatorial novelty。\\n应对措施（已写入 paper_framing.md）：\\n1. Identifiability analysis（技术贡献补充）\\n2. Formal e_i uncertainty propagation（超越 sensitivity analysis）\\n3. Diagnostic framework formalization（连接 DIF 传统）\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n| 优先级 | 数量 | GPU·h | 关键实验 |\\n|--------|------|-------|---------|\\n| P0 | 5 | 200 | 数据收集(130h) + 曝光估计(30h) + G-MFRM 拟合(15h) + Baseline+rank change+power(20h) + 污染校准(5h) |\\n| P1 | 5 | 40 | Judge 数量敏感性 + 指标消融 + Facet 诊断+收敛 + Formal observation + Error propagation |\\n| P2 | 2 | 55 | WildBench 复制 + 对抗鲁棒性 |\\n| **Total** | **12** | **295** | Critical path: exp-001→002→003→004/005 |\\n\\n## Dream 观察项（真实实验后评估）\\n- [Dream 观察] Δτ 实际意义 → Tier A/B/B+ 决策（exp-003/004）\\n- [Dream 观察] ConStat 主导性 + uniform e_i 差距仅 0.01τ（exp-007）\\n- [Dream 观察] Rank-1 misfit 率（exp-008）\\n- [Dream 观察] 95% CI coverage（exp-009 验证，target ≥90%）\\n\\n## 近期任务\\n- [x] exp-009 approved + allocated (cuda:0)\\n- [x] exp-012 approved + allocated (cuda:1)\\n- [ ] 等 exp-009/012 完成，审查结果\\n- [ ] 批准 exp-001（critical path 起点，多 judge 数据收集）\\n- [ ] UDA baseline 代码评估（高风险：无公开代码）\\n- [ ] exp-001 启动后 cuda:2/3 空闲 → 铺 exp-009 Part B 或准备 exp-002 代码\\n\\n## GPU 预算\\n4x RTX 6000 96G (rtx6000-4x)。\\n当前：cuda:0 = exp-009, cuda:1 = exp-012, cuda:2/3 = 空闲（待 exp-001 批准后分配）。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-21 | Dream R2 分析定稿：Best 3.0（降0.5）暴露 novelty 天花板，不再 re-d | exp-009, exp-012 |\\n| D005 | 2026-05-21 | Dream 审稿分析完成：修正 framing（staged joint → conditional | exp-012, exp-009, exp-004, exp-008 |\\n| D004 | 2026-05-21 | MVP PASS，进入 research 阶段 | mvp_003 |\\n| D003 | 2026-05-21 | mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标， | mvp_001, mvp_002 |\\n| D002 | 2026-05-21 | MVP FAIL 但不 kill，启动 DGP 参数诊断 | mvp_001 |\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 2793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "80f5ac7f-ea5d-46f2-9e3d-42f4b2669082",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\\\", \\\"content\\\": \\\"# gated_mfrm_judge_bias — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-21 23:05 UTC | 更新原因: Dream R2 定稿（修正分数），exp-009/012 已 approved+allocated，novelty 天花板应对策略\\\\n\\\\n## 核心方向\\\\nG-MFRM 通过 staged joint calibration 统一校正 LLM 评测中的 judge bias 和 contamination。核心 insight: sequential 方法中 judge severity 与 contamination 存在 omitted variable confounding，joint estimation 方法论必要。详见 paper_framing.md。\\\\n\\\\n## 当前进展\\\\n- **阶段**: Research（MVP 2026-05-21 通过）\\\\n- MVP 验证链: mvp_001→002→003 (PASS: RMSE −43.8%, R̂=1.03, ESS=224)\\\\n- Dream R1: Best=3.5, Median=3.0, Worst=2.5 → framing 修改（staged joint, Observation）\\\\n- Dream R2: **Best=3.0, Median=3.0, Worst=2.5** → novelty 天花板确认，不再 re-dream\\\\n- **exp-009 ALLOCATED cuda:0** (formal OVB observation + c_n validation, ~6h)\\\\n- **exp-012 ALLOCATED cuda:1** (error propagation sensitivity, ~1.5h)\\\\n- Framing 已更新：novelty 补充策略 + bibliography 策略 + Tier B+ contingency\\\\n\\\\n## Novelty 天花板应对\\\\nDream R2 Best 从 3.5→3.0：即使数据最理想，\\\\\\\"MFRM+1 term\\\\\\\" + \\\\\\\"textbook OVB\\\\\\\" 被视为 combinatorial novelty。\\\\n应对措施（已写入 paper_framing.md）：\\\\n1. Identifiability analysis（技术贡献补充）\\\\n2. Formal e_i uncertainty propagation（超越 sensitivity analysis）\\\\n3. Diagnostic framework formalization（连接 DIF 传统）\\\\n\\\\n## 实验计划摘要（详见 experiment_plan.yaml）\\\\n| 优先级 | 数量 | GPU·h | 关键实验 |\\\\n|--------|------|-------|---------|\\\\n| P0 | 5 | 200 | 数据收集(130h) + 曝光估计(30h) + G-MFRM 拟合(15h) + Baseline+rank change+power(20h) + 污染校准(5h) |\\\\n| P1 | 5 | 40 | Judge 数量敏感性 + 指标消融 + Facet 诊断+收敛 + Formal observation + Error propagation |\\\\n| P2 | 2 | 55 | WildBench 复制 + 对抗鲁棒性 |\\\\n| **Total** | **12** | **295** | Critical path: exp-001→002→003→004/005 |\\\\n\\\\n## Dream 观察项（真实实验后评估）\\\\n- [Dream 观察] Δτ 实际意义 → Tier A/B/B+ 决策（exp-003/004）\\\\n- [Dream 观察] ConStat 主导性 + uniform e_i 差距仅 0.01τ（exp-007）\\\\n- [Dream 观察] Rank-1 misfit 率（exp-008）\\\\n- [Dream 观察] 95% CI coverage（exp-009 验证，target ≥90%）\\\\n\\\\n## 近期任务\\\\n- [x] exp-009 approved + allocated (cuda:0)\\\\n- [x] exp-012 approved + allocated (cuda:1)\\\\n- [ ] 等 exp-009/012 完成，审查结果\\\\n- [ ] 批准 exp-001（critical path 起点，多 judge 数据收集）\\\\n- [ ] UDA baseline 代码评估（高风险：无公开代码）\\\\n- [ ] exp-001 启动后 cuda:2/3 空闲 → 铺 exp-009 Part B 或准备 exp-002 代码\\\\n\\\\n## GPU 预算\\\\n4x RTX 6000 96G (rtx6000-4x)。\\\\n当前：cuda:0 = exp-009, cuda:1 = exp-012, cuda:2/3 = 空闲（待 exp-001 批准后分配）。\\\\n\\\\n## 目标会议\\\\n- AAAI 2027: July 28, 2026（~68 天）\\\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D006 | 2026-05-21 | Dream R2 分析定稿：Best 3.0（降0.5）暴露 novelty 天花板，不再 re-d | exp-009, exp-012 |\\\\n| D005 | 2026-05-21 | Dream 审稿分析完成：修正 framing（staged joint → conditional | exp-012, exp-009, exp-004, exp-008 |\\\\n| D004 | 2026-05-21 | MVP PASS，进入 research 阶段 | mvp_003 |\\\\n| D003 | 2026-05-21 | mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标， | mvp_001, mvp_002 |\\\\n| D002 | 2026-05-21 | MVP FAIL 但不 kill，启动 DGP 参数诊断 | mvp_001 |\\\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\\\n\\\\n\\\\n\\\", \\\"total_chars\\\": 2793, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-prod43/projects/gated_mfrm_judge_bias/ROADMAP.md\", \"content\": \"# gated_mfrm_judge_bias — Research Dashboard\\n\\n> 最后更新: 2026-05-21 23:05 UTC | 更新原因: Dream R2 定稿（修正分数），exp-009/012 已 approved+allocated，novelty 天花板应对策略\\n\\n## 核心方向\\nG-MFRM 通过 staged joint calibration 统一校正 LLM 评测中的 judge bias 和 contamination。核心 insight: sequential 方法中 judge severity 与 contamination 存在 omitted variable confounding，joint estimation 方法论必要。详见 paper_framing.md。\\n\\n## 当前进展\\n- **阶段**: Research（MVP 2026-05-21 通过）\\n- MVP 验证链: mvp_001→002→003 (PASS: RMSE −43.8%, R̂=1.03, ESS=224)\\n- Dream R1: Best=3.5, Median=3.0, Worst=2.5 → framing 修改（staged joint, Observation）\\n- Dream R2: **Best=3.0, Median=3.0, Worst=2.5** → novelty 天花板确认，不再 re-dream\\n- **exp-009 ALLOCATED cuda:0** (formal OVB observation + c_n validation, ~6h)\\n- **exp-012 ALLOCATED cuda:1** (error propagation sensitivity, ~1.5h)\\n- Framing 已更新：novelty 补充策略 + bibliography 策略 + Tier B+ contingency\\n\\n## Novelty 天花板应对\\nDream R2 Best 从 3.5→3.0：即使数据最理想，\\\"MFRM+1 term\\\" + \\\"textbook OVB\\\" 被视为 combinatorial novelty。\\n应对措施（已写入 paper_framing.md）：\\n1. Identifiability analysis（技术贡献补充）\\n2. Formal e_i uncertainty propagation（超越 sensitivity analysis）\\n3. Diagnostic framework formalization（连接 DIF 传统）\\n\\n## 实验计划摘要（详见 experiment_plan.yaml）\\n| 优先级 | 数量 | GPU·h | 关键实验 |\\n|--------|------|-------|---------|\\n| P0 | 5 | 200 | 数据收集(130h) + 曝光估计(30h) + G-MFRM 拟合(15h) + Baseline+rank change+power(20h) + 污染校准(5h) |\\n| P1 | 5 | 40 | Judge 数量敏感性 + 指标消融 + Facet 诊断+收敛 + Formal observation + Error propagation |\\n| P2 | 2 | 55 | WildBench 复制 + 对抗鲁棒性 |\\n| **Total** | **12** | **295** | Critical path: exp-001→002→003→004/005 |\\n\\n## Dream 观察项（真实实验后评估）\\n- [Dream 观察] Δτ 实际意义 → Tier A/B/B+ 决策（exp-003/004）\\n- [Dream 观察] ConStat 主导性 + uniform e_i 差距仅 0.01τ（exp-007）\\n- [Dream 观察] Rank-1 misfit 率（exp-008）\\n- [Dream 观察] 95% CI coverage（exp-009 验证，target ≥90%）\\n\\n## 近期任务\\n- [x] exp-009 approved + allocated (cuda:0)\\n- [x] exp-012 approved + allocated (cuda:1)\\n- [ ] 等 exp-009/012 完成，审查结果\\n- [ ] 批准 exp-001（critical path 起点，多 judge 数据收集）\\n- [ ] UDA baseline 代码评估（高风险：无公开代码）\\n- [ ] exp-001 启动后 cuda:2/3 空闲 → 铺 exp-009 Part B 或准备 exp-002 代码\\n\\n## GPU 预算\\n4x RTX 6000 96G (rtx6000-4x)。\\n当前：cuda:0 = exp-009, cuda:1 = exp-012, cuda:2/3 = 空闲（待 exp-001 批准后分配）。\\n\\n## 目标会议\\n- AAAI 2027: July 28, 2026（~68 天）\\n- ACL 2027 ARR: August 3, 2026（~74 天）\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-21 | Dream R2 分析定稿：Best 3.0（降0.5）暴露 novelty 天花板，不再 re-d | exp-009, exp-012 |\\n| D005 | 2026-05-21 | Dream 审稿分析完成：修正 framing（staged joint → conditional | exp-012, exp-009, exp-004, exp-008 |\\n| D004 | 2026-05-21 | MVP PASS，进入 research 阶段 | mvp_003 |\\n| D003 | 2026-05-21 | mvp_002 核心效应验证成功（Joint RMSE -32.8%, p=1e-6），收敛未达标， | mvp_001, mvp_002 |\\n| D002 | 2026-05-21 | MVP FAIL 但不 kill，启动 DGP 参数诊断 | mvp_001 |\\n| D001 | 2026-05-21 | MVP 采用合成数据恢复实验验证 joint estimation 优势 | — |\\n\\n\\n\", \"total_chars\": 2793, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Good, I found the paper. It's "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge" published at AAAI 2026, arXiv:2508.09724. The code is at an anonymous repo. Let me search for the actual GitHub repo (non-anonymous) since this was published at AAAI 2026 and should have been de-anonymized by now.

Let me also check the anonymous repo and search for the authors' public repo.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "b0d99249-b8b9-44d0-96f3-729c12fdfb48",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXgRBRZ1j1Fb1qMBPW3Znf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3442,
      "cache_read_input_tokens": 25014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3442
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0182WzeEqK5k8f5SxKYnBB97`</summary>

```json
{
  "query": "UDA \"Unsupervised Debiasing Alignment\" AAAI 2026 github code authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "33de6229-eb16-42da-bfa0-2f7942782afa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXgRBRZ1j1Fb1qMBPW3Znf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3442,
      "cache_read_input_tokens": 25014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3442
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JLHvvWcnChp2pZasfXR8sz`</summary>

```json
{
  "query": "arxiv 2508.09724 UDA debiasing Elo K-factor neural network code"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "9ed014df-c54a-4d94-9080-265212be3a20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXgRBRZ1j1Fb1qMBPW3Znf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3442,
      "cache_read_input_tokens": 25014,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3442
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

_source line 18 · 2026-05-22T00:44:42.561Z_

<details><summary>↩ Tool result · `toolu_01JLHvvWcnChp2pZasfXR8sz`</summary>

```text
Web search results for query: "arxiv 2508.09724 UDA debiasing Elo K-factor neural network code"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"A Near-Optimal Algorithm for Debiasing Trained Machine Learning Models","url":"https://arxiv.org/pdf/2106.12887"},{"title":"Convergence and stationary distribution of Elo rating systems","url":"https://arxiv.org/pdf/2410.09180"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"Unsupervised Learning of Unbiased Visual Representations","url":"https://arxiv.org/pdf/2204.12941"},{"title":"Learning from Failure: Training Debiased Classifier from Biased   Classifier","url":"https://arxiv.org/pdf/2007.02561"}]

I found the paper! Here's what I discovered:

UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor for each pairwise comparison. The framework operates in a fully unsupervised manner, guided solely by minimizing dispersion among Elo trajectories of all judges to achieve alignment towards collective consensus.

Experiments show that UDA significantly reduces inter-judge rating standard deviation by up to 63.4% and improves average correlation with human judgments by 24.7%, while elevating the performance of poorly performing judges to achieve parity with high-quality ones.

Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "5cb54555-9808-4175-a057-e2f29e54a062",
  "tool_use_result": {
    "query": "arxiv 2508.09724 UDA debiasing Elo K-factor neural network code",
    "results": [
      {
        "tool_use_id": "srvtoolu_014ccJ7y3SxkGysUNcXAFJiX",
        "content": [
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "A Near-Optimal Algorithm for Debiasing Trained Machine Learning Models",
            "url": "https://arxiv.org/pdf/2106.12887"
          },
          {
            "title": "Convergence and stationary distribution of Elo rating systems",
            "url": "https://arxiv.org/pdf/2410.09180"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "Unsupervised Learning of Unbiased Visual Representations",
            "url": "https://arxiv.org/pdf/2204.12941"
          },
          {
            "title": "Learning from Failure: Training Debiased Classifier from Biased   Classifier",
            "url": "https://arxiv.org/pdf/2007.02561"
          }
        ]
      },
      "I found the paper! Here's what I discovered:\n\nUDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor for each pairwise comparison. The framework operates in a fully unsupervised manner, guided solely by minimizing dispersion among Elo trajectories of all judges to achieve alignment towards collective consensus.\n\nExperiments show that UDA significantly reduces inter-judge rating standard deviation by up to 63.4% and improves average correlation with human judgments by 24.7%, while elevating the performance of poorly performing judges to achieve parity with high-quality ones.\n\nCode and data are available at https://anonymous.4open.science/r/62AB93CD-23B4."
    ],
    "durationSeconds": 5.513129593000005
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-22T00:44:45.314Z_

<details><summary>↩ Tool result · `toolu_0182WzeEqK5k8f5SxKYnBB97`</summary>

```text
Web search results for query: "UDA "Unsupervised Debiasing Alignment" AAAI 2026 github code authors"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"GitHub - jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation: [TPAMI 2026] CLIP-Powered Domain Generalization and Domain Adaptation: A Comprehensive Survey. · GitHub","url":"https://github.com/jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation"},{"title":"GitHub - BaiShuanghao/Prompt-based-Distribution-Alignment: [AAAI 2024] Prompt-based Distribution Alignment for Unsupervised Domain Adaptation","url":"https://github.com/BaiShuanghao/Prompt-based-Distribution-Alignment"},{"title":"Prompt-Based Distribution Alignment for Unsupervised Domain Adaptation","url":"https://ojs.aaai.org/index.php/AAAI/article/view/27830/27688"}]

Based on the search results, I found information about the UDA paper for AAAI 2026:

## Authors and Publication

The authors are Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J. The paper is titled "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge" and was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861.

## Paper Details

UDA is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner.

## GitHub Code

The search results do not contain information about a GitHub repository link for this paper. The AAAI proceedings page (https://ojs.aaai.org/index.php/AAAI/article/view/40788) and the arXiv paper (https://arxiv.org/abs/2508.09724) are available, but no GitHub code repository was found in these results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "b8e5e575-85ed-4197-9116-b3886e609c34",
  "tool_use_result": {
    "query": "UDA \"Unsupervised Debiasing Alignment\" AAAI 2026 github code authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PhQ3Ux7Y2S98BSKUF98Cdf",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "GitHub - jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation: [TPAMI 2026] CLIP-Powered Domain Generalization and Domain Adaptation: A Comprehensive Survey. · GitHub",
            "url": "https://github.com/jindongli-Ai/Survey_on_CLIP-Powered_Domain_Generalization_and_Adaptation"
          },
          {
            "title": "GitHub - BaiShuanghao/Prompt-based-Distribution-Alignment: [AAAI 2024] Prompt-based Distribution Alignment for Unsupervised Domain Adaptation",
            "url": "https://github.com/BaiShuanghao/Prompt-based-Distribution-Alignment"
          },
          {
            "title": "Prompt-Based Distribution Alignment for Unsupervised Domain Adaptation",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/27830/27688"
          }
        ]
      },
      "Based on the search results, I found information about the UDA paper for AAAI 2026:\n\n## Authors and Publication\n\nThe authors are Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J. The paper is titled \"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\" and was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41), 34854–34861.\n\n## Paper Details\n\nUDA is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner.\n\n## GitHub Code\n\nThe search results do not contain information about a GitHub repository link for this paper. The AAAI proceedings page (https://ojs.aaai.org/index.php/AAAI/article/view/40788) and the arXiv paper (https://arxiv.org/abs/2508.09724) are available, but no GitHub code repository was found in these results."
    ],
    "durationSeconds": 8.852356309000003
  }
}
```

</details>

---

### Assistant

_source line 20_

<details><summary>Logged reasoning block</summary>

```text
The anonymous repo link is still the only code link. Let me try to access it and also search for the authors' GitHub profiles. The authors are Zhang, Y., Wang, C., Wu, L., Yu, W., Wang, Y., Bao, G., & Tang, J.

Let me search for the specific author names and see if they have released it publicly. Also let me check the anonymous.4open.science link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "da2541d4-c2d2-484b-a6a8-d8e2914d43b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD4S5oT9rPMAWbuJ6CU6Fh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 28456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jt9M75Xod47q3YCrKnG7db`</summary>

```json
{
  "query": "site:github.com \"unsupervised debiasing alignment\" OR \"UDA\" Elo judge pairwise"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "b9c34b96-d19b-4cb6-b840-57d275485f55",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD4S5oT9rPMAWbuJ6CU6Fh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 28456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01GsVQnt9JCGgi5vsfaVpUXa`</summary>

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
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "7ec17afd-6d7a-46c4-9df4-59d44446387d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YD4S5oT9rPMAWbuJ6CU6Fh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 653,
      "cache_creation_input_tokens": 1142,
      "cache_read_input_tokens": 28456,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1142
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

_source line 23 · 2026-05-22T00:44:51.274Z_

<details><summary>↩ Tool result · `toolu_01GsVQnt9JCGgi5vsfaVpUXa`</summary>

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
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "49e97949-c6c7-4cf5-a353-ec87a6f58ca8",
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

### Tool result

_source line 24 · 2026-05-22T00:44:56.484Z_

<details><summary>↩ Tool result · `toolu_01Jt9M75Xod47q3YCrKnG7db`</summary>

```text
Web search results for query: "site:github.com "unsupervised debiasing alignment" OR "UDA" Elo judge pairwise"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"Aligning with Human Judgement: The Role of Pairwise Preference in Large   Language Model Evaluators","url":"https://arxiv.org/pdf/2403.16950"},{"title":"Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2601.13649"},{"title":"A General Framework for Pairwise Unbiased Learning to Rank","url":"https://arxiv.org/pdf/2207.08537"},{"title":"GitHub - google-research/uda: Unsupervised Data Augmentation (UDA) · GitHub","url":"https://github.com/google-research/uda"}]

Based on the search results, I found information about UDA in the context of LLM evaluation. Here's what I found:

UDA (Unsupervised Debiasing Alignment) is a framework that addresses preference bias in pairwise evaluation of Large Language Models. The framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities for each pairwise comparison.

UDA operates in a fully unsupervised manner, guided by minimizing dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable evaluation. Experiments show that UDA significantly reduces inter-judge rating standard deviation by up to 63.4% and improves average correlation with human judgments by 24.7%.

The search results also indicate that code and data are available at an anonymous repository, though the specific GitHub link from the search didn't appear in the results. The research appears to be recent and focuses on addressing systematic biases in LLM-based pairwise evaluations using Elo rating adjustments.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "d6d80e6e-47cb-4979-93b2-8ec6ccf00a8d",
  "tool_use_result": {
    "query": "site:github.com \"unsupervised debiasing alignment\" OR \"UDA\" Elo judge pairwise",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MrkQZn2wFS28VzWpeP5TzK",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "Aligning with Human Judgement: The Role of Pairwise Preference in Large   Language Model Evaluators",
            "url": "https://arxiv.org/pdf/2403.16950"
          },
          {
            "title": "Fairness or Fluency? An Investigation into Language Bias of Pairwise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2601.13649"
          },
          {
            "title": "A General Framework for Pairwise Unbiased Learning to Rank",
            "url": "https://arxiv.org/pdf/2207.08537"
          },
          {
            "title": "GitHub - google-research/uda: Unsupervised Data Augmentation (UDA) · GitHub",
            "url": "https://github.com/google-research/uda"
          }
        ]
      },
      "Based on the search results, I found information about UDA in the context of LLM evaluation. Here's what I found:\n\nUDA (Unsupervised Debiasing Alignment) is a framework that addresses preference bias in pairwise evaluation of Large Language Models. The framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where a compact neural network learns to adaptively set the K-factor and refine win probabilities for each pairwise comparison.\n\nUDA operates in a fully unsupervised manner, guided by minimizing dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable evaluation. Experiments show that UDA significantly reduces inter-judge rating standard deviation by up to 63.4% and improves average correlation with human judgments by 24.7%.\n\nThe search results also indicate that code and data are available at an anonymous repository, though the specific GitHub link from the search didn't appear in the results. The research appears to be recent and focuses on addressing systematic biases in LLM-based pairwise evaluations using Elo rating adjustments."
    ],
    "durationSeconds": 5.781227934000002
  }
}
```

</details>

---

### Assistant

_source line 25_

<details><summary>Logged reasoning block</summary>

```text
Let me try to fetch the anonymous repo and the arxiv page to get more details about the method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "f7cf4547-b51b-4d18-bd87-81f7d9a1de8a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113aNurpZvwNQ22sVsok67i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 29598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2003
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HvYjAV5jARs3QfFSXqxr6H`</summary>

```json
{
  "url": "https://anonymous.4open.science/r/62AB93CD-23B4",
  "prompt": "Is this repository accessible? List all files and directories visible. If there's a README, extract the key information about installation and usage."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "e4a3a746-104a-45da-b051-04285e50a8ae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113aNurpZvwNQ22sVsok67i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 29598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2003
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

_source line 27 · 2026-05-22T00:45:00.865Z_

<details><summary>↩ Tool result · reported error · `toolu_01HvYjAV5jARs3QfFSXqxr6H`</summary>

```text
Request failed with status code 403
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "4b5ee615-02ee-4599-b410-31fb80e0ee1d",
  "tool_use_result": "Error: Request failed with status code 403"
}
```

</details>

---

### Tool call

_source line 28_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01RKv7f23v4tLTZ8U7b7W6FL`</summary>

```json
{
  "url": "https://arxiv.org/abs/2508.09724",
  "prompt": "Extract: 1) Full author list with affiliations 2) Complete abstract 3) Any links to code repositories mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "5834031f-49ca-4244-b61e-6ce12a265947",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0113aNurpZvwNQ22sVsok67i",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2003,
      "cache_read_input_tokens": 29598,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2003
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

_source line 29 · 2026-05-22T00:45:09.240Z_

<details><summary>↩ Tool result · `toolu_01RKv7f23v4tLTZ8U7b7W6FL`</summary>

```text
# UDA: Unsupervised Debiasing Alignment Paper Summary

## 1) Author List with Affiliations

The paper lists seven authors:
- Yang Zhang
- Cunxiang Wang
- Lindong Wu
- Wenbo Yu
- Yidong Wang
- Guangsheng Bao
- Jie Tang

**Note:** The provided webpage does not include institutional affiliations for any of the authors.

## 2) Complete Abstract

"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at [this https URL](https://anonymous.4open.science/r/62AB93CD-23B4)."

## 3) Code Repository Links

The paper mentions code availability: "Code and data are available at this https URL" linking to `https://anonymous.4open.science/r/62AB93CD-23B4`, though this appears to be an anonymous submission URL rather than a permanent public repository.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "51c95b38-7f3e-40fa-9e80-9b1d543c4d57",
  "tool_use_result": {
    "bytes": 47530,
    "code": 200,
    "codeText": "OK",
    "result": "# UDA: Unsupervised Debiasing Alignment Paper Summary\n\n## 1) Author List with Affiliations\n\nThe paper lists seven authors:\n- Yang Zhang\n- Cunxiang Wang\n- Lindong Wu\n- Wenbo Yu\n- Yidong Wang\n- Guangsheng Bao\n- Jie Tang\n\n**Note:** The provided webpage does not include institutional affiliations for any of the authors.\n\n## 2) Complete Abstract\n\n\"Pairwise evaluation of Large Language Models (LLMs) is a common paradigm, but it is prone to preference bias, where judges systematically favor certain outputs, such as their own. This bias leads to inconsistent and skewed rankings across different judges. To address this, we first empirically demonstrate significant and heterogeneous biases in cross-model evaluations. We then propose UDA (Unsupervised Debiasing Alignment), a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. Crucially, UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges. This forces an alignment towards a collective consensus, which serves as an unsupervised proxy for a more stable and reproducible evaluation. In addition, we provide theoretical motivation demonstrating how alignment towards a consensus can reduce aggregate system bias. Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%. Notably, UDA elevates the performance of poorly performing judges to achieve parity with high-quality ones, fostering a more robust and reliable evaluation ecosystem. Code and data are available at [this https URL](https://anonymous.4open.science/r/62AB93CD-23B4).\"\n\n## 3) Code Repository Links\n\nThe paper mentions code availability: \"Code and data are available at this https URL\" linking to `https://anonymous.4open.science/r/62AB93CD-23B4`, though this appears to be an anonymous submission URL rather than a permanent public repository.",
    "durationMs": 7664,
    "url": "https://arxiv.org/abs/2508.09724"
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
The anonymous repo returns 403 (still not accessible). The paper is published at AAAI 2026, but the code still only points to the anonymous repo. Let me search for the authors on GitHub to see if they have released the code on their personal accounts.

The authors are:
- Yang Zhang
- Cunxiang Wang
- Lindong Wu
- Wenbo Yu
- Yidong Wang
- Guangsheng Bao
- Jie Tang

Jie Tang is the famous professor from Tsinghua (KnowledgeGraph, AMiner). 

Now I'll check if any of the other authors have published the code under their own GitHub profiles.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "0b95e92d-ec22-42ea-997f-b02a8551f223",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWWxyWKU2L8XrdpwUscuZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 31601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 919
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011u41HtR8QFCJYbAEWRhhF8`</summary>

```json
{
  "query": "Cunxiang Wang github \"UDA\" OR \"debiasing alignment\" OR \"judge bias\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "f651bbe2-074f-47df-abea-7a2fc903b56d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWWxyWKU2L8XrdpwUscuZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 31601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 919
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HMuTuHFafi1w4b2wgXjHFy`</summary>

```json
{
  "query": "Guangsheng Bao github LLM judge evaluation debiasing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "246b63e3-97bd-4d5d-935b-26c2be567030",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PWWxyWKU2L8XrdpwUscuZQ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 919,
      "cache_read_input_tokens": 31601,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 919
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

_source line 33 · 2026-05-22T00:45:20.941Z_

<details><summary>↩ Tool result · `toolu_01HMuTuHFafi1w4b2wgXjHFy`</summary>

```text
Web search results for query: "Guangsheng Bao github LLM judge evaluation debiasing"

Links: [{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/html/2508.09724"},{"title":"Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization","url":"https://arxiv.org/pdf/2603.08091"},{"title":"GitHub - sksoumik/llm-as-judge: Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines · GitHub","url":"https://github.com/sksoumik/llm-as-judge"},{"title":"Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector","url":"https://arxiv.org/pdf/2505.17100"},{"title":"Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation","url":"https://arxiv.org/pdf/2603.05485"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"Debiasing LLM Judges: Understanding and correcting AI Evaluation Bias - DEV Community","url":"https://dev.to/gyani_s/debiasing-llm-judges-understanding-and-correcting-ai-evaluation-bias-2ce4"}]

I found research related to Guangsheng Bao and LLM judge evaluation debiasing. Here are the key findings:

Guangsheng Bao is one of the authors on the paper "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge". The UDA framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.

The research addresses a significant problem: Pairwise evaluation of LLMs is prone to preference bias, where judges systematically favor certain outputs, and this bias leads to inconsistent and skewed rankings across different judges.

The paper was published on arXiv in November 2025. While I found references to this research, the web search results don't contain a direct link to Guangsheng Bao's GitHub repository. If you're looking for the code implementation, you might want to search for the paper on arXiv or GitHub directly using the paper title "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge" or check the author's institutional repositories.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "3ca41ba4-c73b-4d0c-b044-7c1dbd374327",
  "tool_use_result": {
    "query": "Guangsheng Bao github LLM judge evaluation debiasing",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QRtrrDSpF8SFQxW328dsEx",
        "content": [
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2508.09724"
          },
          {
            "title": "Toward Robust LLM-Based Judges: Taxonomic Bias Evaluation and Debiasing Optimization",
            "url": "https://arxiv.org/pdf/2603.08091"
          },
          {
            "title": "GitHub - sksoumik/llm-as-judge: Judging the Judges: A Systematic Evaluation of Bias Mitigation Strategies in LLM-as-a-Judge Pipelines · GitHub",
            "url": "https://github.com/sksoumik/llm-as-judge"
          },
          {
            "title": "Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector",
            "url": "https://arxiv.org/pdf/2505.17100"
          },
          {
            "title": "Towards Provably Unbiased LLM Judges via Bias-Bounded Evaluation",
            "url": "https://arxiv.org/pdf/2603.05485"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          },
          {
            "title": "Debiasing LLM Judges: Understanding and correcting AI Evaluation Bias - DEV Community",
            "url": "https://dev.to/gyani_s/debiasing-llm-judges-understanding-and-correcting-ai-evaluation-bias-2ce4"
          }
        ]
      },
      "I found research related to Guangsheng Bao and LLM judge evaluation debiasing. Here are the key findings:\n\nGuangsheng Bao is one of the authors on the paper \"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\". The UDA framework reduces inter-judge disagreement by dynamically adjusting the Elo rating system. For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.\n\nThe research addresses a significant problem: Pairwise evaluation of LLMs is prone to preference bias, where judges systematically favor certain outputs, and this bias leads to inconsistent and skewed rankings across different judges.\n\nThe paper was published on arXiv in November 2025. While I found references to this research, the web search results don't contain a direct link to Guangsheng Bao's GitHub repository. If you're looking for the code implementation, you might want to search for the paper on arXiv or GitHub directly using the paper title \"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge\" or check the author's institutional repositories."
    ],
    "durationSeconds": 5.7920017530000045
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-22T00:45:21.925Z_

<details><summary>↩ Tool result · `toolu_011u41HtR8QFCJYbAEWRhhF8`</summary>

```text
Web search results for query: "Cunxiang Wang github "UDA" OR "debiasing alignment" OR "judge bias""

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"A Statistical Framework for Alignment with Biased AI Feedback","url":"https://arxiv.org/pdf/2602.08259"},{"title":"Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector","url":"https://arxiv.org/html/2505.17100v1"}]

I found search results related to Cunxiang Wang and the UDA research on debiasing alignment for LLM judges. Here's what I found:

## Main Research

UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. The research addresses preference bias in pairwise evaluation of Large Language Models (LLMs), where judges systematically favor certain outputs, such as their own.

## How UDA Works

For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges.

## Results

Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

## Code Availability

Code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4 (this was the anonymous submission link).

The paper has been published in the AAAI Conference on Artificial Intelligence 2026 proceedings. Cunxiang Wang is one of the authors on this project alongside Yang Zhang and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "0085f117-bc50-4896-8574-161c1fc1f8d1",
  "tool_use_result": {
    "query": "Cunxiang Wang github \"UDA\" OR \"debiasing alignment\" OR \"judge bias\"",
    "results": [
      {
        "tool_use_id": "srvtoolu_01323dCFtdR2fZhVWLvMe9PH",
        "content": [
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "A Statistical Framework for Alignment with Biased AI Feedback",
            "url": "https://arxiv.org/pdf/2602.08259"
          },
          {
            "title": "Any Large Language Model Can Be a Reliable Judge: Debiasing with a Reasoning-based Bias Detector",
            "url": "https://arxiv.org/html/2505.17100v1"
          }
        ]
      },
      "I found search results related to Cunxiang Wang and the UDA research on debiasing alignment for LLM judges. Here's what I found:\n\n## Main Research\n\nUDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. The research addresses preference bias in pairwise evaluation of Large Language Models (LLMs), where judges systematically favor certain outputs, such as their own.\n\n## How UDA Works\n\nFor each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities, operating in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges.\n\n## Results\n\nExperiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.\n\n## Code Availability\n\nCode and data are available at https://anonymous.4open.science/r/62AB93CD-23B4 (this was the anonymous submission link).\n\nThe paper has been published in the AAAI Conference on Artificial Intelligence 2026 proceedings. Cunxiang Wang is one of the authors on this project alongside Yang Zhang and others."
    ],
    "durationSeconds": 6.893576676000012
  }
}
```

</details>

---

### Assistant

_source line 35_

<details><summary>Logged reasoning block</summary>

```text
Let me also try to read the HTML version of the paper on arXiv to understand the method in detail, and also search for Guangsheng Bao's GitHub directly.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "36006536-eb3f-43b0-83e8-a010ee3de897",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKK8tXaU2sge9dYZk69dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

Now let me get the method details from the paper and check authors' GitHub profiles.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "e0c79431-ab93-4ef3-97f6-c239baa255f1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKK8tXaU2sge9dYZk69dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

_source line 37_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Ep9sYUyXDzzaFHAAXKUAoA`</summary>

```json
{
  "url": "https://arxiv.org/html/2508.09724",
  "prompt": "Extract the METHODOLOGY section in detail. I need to understand:\n1. How does the Elo rating adjustment work? What is the K-factor adaptation mechanism?\n2. What is the neural network architecture? (input features, layers, output)\n3. What is the loss function / optimization objective?\n4. What are the inputs to UDA? (what format of judge data does it need?)\n5. What are the outputs? (debiased Elo scores? corrected rankings?)\n6. What is the training procedure? (how many iterations, any hyperparameters mentioned?)\n7. Any pseudocode or algorithm descriptions?\nAlso check if there are any OTHER code/data links besides the anonymous repo."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "aceb1cb5-9d74-495f-b929-886c62858486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKK8tXaU2sge9dYZk69dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

_source line 38_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HVeds3H7kogunFatX3NsPZ`</summary>

```json
{
  "query": "github.com guangsheng-bao LLM judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "635dd845-e8ff-441e-9973-40e67fc0a1b5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKK8tXaU2sge9dYZk69dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

_source line 39_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U9XJ8yTkJALEc9krDUMWTJ`</summary>

```json
{
  "query": "github.com cunxiang-wang NLP"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "adb6c75b-56a8-4c33-ad34-9e90b3670e72",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HKKK8tXaU2sge9dYZk69dS",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 773,
      "cache_creation_input_tokens": 1016,
      "cache_read_input_tokens": 32520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1016
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

_source line 40 · 2026-05-22T00:45:41.308Z_

<details><summary>↩ Tool result · `toolu_01HVeds3H7kogunFatX3NsPZ`</summary>

```text
Web search results for query: "github.com guangsheng-bao LLM judge"

Links: [{"title":"Guangsheng Bao","url":"https://baoguangsheng.github.io/"},{"title":"baoguangsheng (Guangsheng Bao) · GitHub","url":"https://github.com/baoguangsheng"},{"title":"GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub","url":"https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"},{"title":"LLM-as-a-judge","url":"https://llm-as-a-judge.github.io/"},{"title":"GitHub - DataArcTech/LLM-as-a-Judge · GitHub","url":"https://github.com/IDEA-FinAI/LLM-as-a-Judge"},{"title":"GitHub - baaivision/JudgeLM: [ICLR 2025 Spotlight] An open-sourced LLM judge for evaluating LLM-generated answers. · GitHub","url":"https://github.com/baaivision/JudgeLM"},{"title":"Using LLM-as-a-judge 🧑‍⚖️ for an automated and versatile ...","url":"https://colab.research.google.com/github/huggingface/cookbook/blob/main/notebooks/en/llm_judge.ipynb"},{"title":"GitHub - databricks/judges: A small library of LLM judges · GitHub","url":"https://github.com/quotient-ai/judges"},{"title":"GitHub - aws-samples/evaluating-large-language-models-using-llm-as-a-judge · GitHub","url":"https://github.com/aws-samples/evaluating-large-language-models-using-llm-as-a-judge"},{"title":"llm-as-a-judge · GitHub Topics · GitHub","url":"https://github.com/topics/llm-as-a-judge"}]

Based on the search results, I found information about Guangsheng Bao and various LLM judge projects. Here's what I found:

## Guangsheng Bao

Guangsheng Bao is currently a Ph.D. candidate at Westlake University and Zhejiang University, advised by Prof. Yue Zhang. His primary research interests lie in the field of trustworthy NLP, encompassing topics like model generalization, the creation of explainable and controllable NLP systems, ensuring the safe application of LLMs, and understanding the reasoning capabilities of LLMs.

His GitHub repositories include "fast-detect-gpt," code base for ICLR 2024 "Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature," and "glimpse," code base for ICLR 2025 "Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection."

## LLM Judge Resources

While Guangsheng Bao's work focuses on GPT detection rather than LLM judges directly, the search revealed several relevant LLM-as-a-judge projects:

- JudgeLM is a scalable language model judge, designed for evaluating LLMs in open-ended scenarios, achieving an agreement exceeding 90% that surpasses human-to-human agreement.

- There is a repository that includes papers discussed in a survey paper on Awesome-LLM-as-a-judge.

- Large Language Model (LLM)-based judgments leverage powerful LLMs to efficiently evaluate candidate content and provide judgment scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "52adccde-a308-4665-be43-8771032bc0c0",
  "tool_use_result": {
    "query": "github.com guangsheng-bao LLM judge",
    "results": [
      {
        "tool_use_id": "srvtoolu_012DASgnt99aQAkn6VbeXrSp",
        "content": [
          {
            "title": "Guangsheng Bao",
            "url": "https://baoguangsheng.github.io/"
          },
          {
            "title": "baoguangsheng (Guangsheng Bao) · GitHub",
            "url": "https://github.com/baoguangsheng"
          },
          {
            "title": "GitHub - llm-as-a-judge/Awesome-LLM-as-a-judge · GitHub",
            "url": "https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge"
          },
          {
            "title": "LLM-as-a-judge",
            "url": "https://llm-as-a-judge.github.io/"
          },
          {
            "title": "GitHub - DataArcTech/LLM-as-a-Judge · GitHub",
            "url": "https://github.com/IDEA-FinAI/LLM-as-a-Judge"
          },
          {
            "title": "GitHub - baaivision/JudgeLM: [ICLR 2025 Spotlight] An open-sourced LLM judge for evaluating LLM-generated answers. · GitHub",
            "url": "https://github.com/baaivision/JudgeLM"
          },
          {
            "title": "Using LLM-as-a-judge 🧑‍⚖️ for an automated and versatile ...",
            "url": "https://colab.research.google.com/github/huggingface/cookbook/blob/main/notebooks/en/llm_judge.ipynb"
          },
          {
            "title": "GitHub - databricks/judges: A small library of LLM judges · GitHub",
            "url": "https://github.com/quotient-ai/judges"
          },
          {
            "title": "GitHub - aws-samples/evaluating-large-language-models-using-llm-as-a-judge · GitHub",
            "url": "https://github.com/aws-samples/evaluating-large-language-models-using-llm-as-a-judge"
          },
          {
            "title": "llm-as-a-judge · GitHub Topics · GitHub",
            "url": "https://github.com/topics/llm-as-a-judge"
          }
        ]
      },
      "Based on the search results, I found information about Guangsheng Bao and various LLM judge projects. Here's what I found:\n\n## Guangsheng Bao\n\nGuangsheng Bao is currently a Ph.D. candidate at Westlake University and Zhejiang University, advised by Prof. Yue Zhang. His primary research interests lie in the field of trustworthy NLP, encompassing topics like model generalization, the creation of explainable and controllable NLP systems, ensuring the safe application of LLMs, and understanding the reasoning capabilities of LLMs.\n\nHis GitHub repositories include \"fast-detect-gpt,\" code base for ICLR 2024 \"Fast-DetectGPT: Efficient Zero-Shot Detection of Machine-Generated Text via Conditional Probability Curvature,\" and \"glimpse,\" code base for ICLR 2025 \"Glimpse: Enabling White-Box Methods to Use Proprietary Models for Zero-Shot LLM-Generated Text Detection.\"\n\n## LLM Judge Resources\n\nWhile Guangsheng Bao's work focuses on GPT detection rather than LLM judges directly, the search revealed several relevant LLM-as-a-judge projects:\n\n- JudgeLM is a scalable language model judge, designed for evaluating LLMs in open-ended scenarios, achieving an agreement exceeding 90% that surpasses human-to-human agreement.\n\n- There is a repository that includes papers discussed in a survey paper on Awesome-LLM-as-a-judge.\n\n- Large Language Model (LLM)-based judgments leverage powerful LLMs to efficiently evaluate candidate content and provide judgment scores."
    ],
    "durationSeconds": 7.855250351000009
  }
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-22T00:45:41.599Z_

<details><summary>↩ Tool result · `toolu_01U9XJ8yTkJALEc9krDUMWTJ`</summary>

```text
Web search results for query: "github.com cunxiang-wang NLP"

Links: [{"title":"Cunxiang Wang, Westlake University","url":"https://wangcunxiang.github.io/"},{"title":"GitHub - MLGroupJLU/LLM-eval-survey: The official GitHub page for the survey paper \"A Survey on Evaluation of Large Language Models\".","url":"https://github.com/mlgroupjlu/llm-eval-survey"},{"title":"GitHub - HancCui/IterSurvey_Autosurveyv2: Code for IterSurvey(Deep Literature Survey Automation with an Iterative Workflow) · GitHub","url":"https://github.com/HancCui/IterSurvey_Autosurveyv2"},{"title":"Qianli Wang","url":"https://qiaw99.github.io/"},{"title":"coolwanglu (Lu Wang) / Followers · GitHub","url":"https://github.com/coolwanglu?tab=followers"},{"title":"Xiaoou Wang - NLP","url":"https://xiaoouwang.github.io/"},{"title":"yuewang-cuhk (WANG Yue) · GitHub","url":"https://github.com/yuewang-cuhk"},{"title":"zhaowei-wang-nlp (Zhaowei Wang) · GitHub","url":"https://github.com/zhaowei-wang-nlp"},{"title":"DivScene: Benchmarking LVLMs for Object Navigation with Diverse Scenes and Objects","url":"https://zhaowei-wang-nlp.github.io/divscene-project-page/"},{"title":"Xiao Wang","url":"https://xiaowangnlp.github.io/"}]

Based on the search results, I found information about Cunxiang Wang and his NLP work:

Cunxiang Wang is affiliated with the Department of Computer Science and Technology at Northeastern University in Shenyang, where he was an undergraduate student from September 2015 to July 2019. He interned at Northeastern NLP Lab from 2016-2019, advised by Prof. Feiliang Ren.

Wang is currently affiliated with Westlake University and has contributed to significant NLP research. Some of his notable projects include:

- A survey on factuality in large language models focusing on knowledge, retrieval, and domain-specificity
- StepMathAgent, a step-wise agent for evaluating mathematical processes through tree-of-error
- TRAMS: Training-free memory selection for long-range language modeling
- Work on evaluating open-QA evaluation

He has also been a co-author on "A Survey on Evaluation of Large Language Models" along with researchers from institutions including Jilin University, Microsoft Research, Carnegie Mellon University, Peking University, and other organizations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "d77f4b80-89c8-48f4-b1de-bb058363cc50",
  "tool_use_result": {
    "query": "github.com cunxiang-wang NLP",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RaRs7EAfwLjMm2F9KwEuhE",
        "content": [
          {
            "title": "Cunxiang Wang, Westlake University",
            "url": "https://wangcunxiang.github.io/"
          },
          {
            "title": "GitHub - MLGroupJLU/LLM-eval-survey: The official GitHub page for the survey paper \"A Survey on Evaluation of Large Language Models\".",
            "url": "https://github.com/mlgroupjlu/llm-eval-survey"
          },
          {
            "title": "GitHub - HancCui/IterSurvey_Autosurveyv2: Code for IterSurvey(Deep Literature Survey Automation with an Iterative Workflow) · GitHub",
            "url": "https://github.com/HancCui/IterSurvey_Autosurveyv2"
          },
          {
            "title": "Qianli Wang",
            "url": "https://qiaw99.github.io/"
          },
          {
            "title": "coolwanglu (Lu Wang) / Followers · GitHub",
            "url": "https://github.com/coolwanglu?tab=followers"
          },
          {
            "title": "Xiaoou Wang - NLP",
            "url": "https://xiaoouwang.github.io/"
          },
          {
            "title": "yuewang-cuhk (WANG Yue) · GitHub",
            "url": "https://github.com/yuewang-cuhk"
          },
          {
            "title": "zhaowei-wang-nlp (Zhaowei Wang) · GitHub",
            "url": "https://github.com/zhaowei-wang-nlp"
          },
          {
            "title": "DivScene: Benchmarking LVLMs for Object Navigation with Diverse Scenes and Objects",
            "url": "https://zhaowei-wang-nlp.github.io/divscene-project-page/"
          },
          {
            "title": "Xiao Wang",
            "url": "https://xiaowangnlp.github.io/"
          }
        ]
      },
      "Based on the search results, I found information about Cunxiang Wang and his NLP work:\n\nCunxiang Wang is affiliated with the Department of Computer Science and Technology at Northeastern University in Shenyang, where he was an undergraduate student from September 2015 to July 2019. He interned at Northeastern NLP Lab from 2016-2019, advised by Prof. Feiliang Ren.\n\nWang is currently affiliated with Westlake University and has contributed to significant NLP research. Some of his notable projects include:\n\n- A survey on factuality in large language models focusing on knowledge, retrieval, and domain-specificity\n- StepMathAgent, a step-wise agent for evaluating mathematical processes through tree-of-error\n- TRAMS: Training-free memory selection for long-range language modeling\n- Work on evaluating open-QA evaluation\n\nHe has also been a co-author on \"A Survey on Evaluation of Large Language Models\" along with researchers from institutions including Jilin University, Microsoft Research, Carnegie Mellon University, Peking University, and other organizations."
    ],
    "durationSeconds": 8.144657030000003
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-22T00:45:46.514Z_

<details><summary>↩ Tool result · `toolu_01Ep9sYUyXDzzaFHAAXKUAoA`</summary>

````text
# UDA Methodology Deep Dive

## 1. Elo Rating Adjustment & K-Factor Adaptation

**Baseline Elo Update:**
The standard formula is: `R_i^(k) ← R_i^(k) + K(r_ij^(k) - p̂_ij^(k))` where K is a global constant and `p̂_ij^(k) = σ(R_i^(k) - R_j^(k))` is the sigmoid-based win probability.

**Adaptive Mechanism:**
UDA replaces the fixed K with an instance-level K_ij and hard binary labels r_ij^(k) with soft labels (s_i, s_j) ∈ (0,1). Both are "output by a compact neural network" that processes comparison-specific features.

## 2. Neural Network Architecture

**Input Features:** A 6D+9 dimensional feature vector φ_ij^(k) constructed from answer embeddings (e_i, e_j) and judge's own embedding (e_k):
- 6 high-dimensional vectors (element-wise differences, normalized products)
- 9 scalars (cosine similarities, KL-divergences, norm differences)

**Model:** "A small Multilayer Perceptron (MLP) f_θ: ℝ^(6D+9) → ℝ^3" maps features to (K_ij, s_i, s_j). Full details provided in Algorithm 1 of the paper.

**Layers:** Described as "3-layer MLP" in training details; no other architectural specifics disclosed.

## 3. Loss Function & Optimization Objective

Three-term objective (Equation 3):
```
L(θ) = α∑_b ||R^(b) - G||_2^2 + σ||R̄ - G||_2^2 + β∑_b(1 - ρ_p(R^(b), G))
```

Where:
- First term: pulls each judge's scores toward consensus anchor G
- Second term: enforces collective agreement across all judges
- Third term: maximizes Pearson rank correlation with consensus

## 4. Required Inputs

- Pairwise judge preferences: r_ij^(k) ∈ {0,1} (binary win/loss for response pair)
- Embeddings: semantic representations of two candidate answers + judge's own generated response
- Current Elo scores: R_i^(k) for all model-judge pairs

**Format:** "All pairwise comparisons issued by a single judge k_b in one forward pass" grouped into judge-homogeneous mini-batches.

## 5. Outputs

- **Debiased Elo scores:** R_i^(k)(UDA) for each model under each judge
- **Soft labels:** (s_i, s_j) replacing hard binary preferences
- **Adaptive K-factors:** Instance-specific weighting (K_ij)

## 6. Training Procedure

**Dataset:** 500 ArenaHard prompts, 10 LLM judges, 450,000 pairwise judgments total

**Details:** "AdamW optimizer" with "learning rate scheduler"; "best model selected based on validation loss." Computation: "8 hours on a single 4090" GPU.

**Hyperparameters:** Loss weights α, σ, β mentioned but specific values relegated to appendix (not provided in excerpt).

## 7. Algorithms & Pseudocode

**Algorithm 1:** Detailed feature construction (6D+9 dimensions from embeddings)

**Algorithm 2:** Adaptive Elo Update
```
Input: responses, judge k, current scores
Output: updated scores R_i^(k), R_j^(k)

1. Compute features φ_ij (Algorithm 1)
2. Forward pass: (K_ij, s_i, s_j) ← f_θ(φ_ij)
3. p̂_ij^(k) ← σ(R_i^(k) - R_j^(k))
4. R_i^(k) ← R_i^(k) + K_ij(s_i - p̂_ij^(k))
5. R_j^(k) ← R_j^(k) + K_ij(s_j - (1 - p̂_ij^(k)))
```

## Additional Code/Data Links

Only one repository mentioned:
- **Anonymous submission:** https://anonymous.4open.science/r/62AB93CD-23B4 (contains code, checkpoints, Human-Annotated Transfer Set)

No alternative public repositories provided in the document.
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "a674488b-89b3-4eab-9bcc-9d0cb1d4a9e9",
  "tool_use_result": {
    "bytes": 301207,
    "code": 200,
    "codeText": "OK",
    "result": "# UDA Methodology Deep Dive\n\n## 1. Elo Rating Adjustment & K-Factor Adaptation\n\n**Baseline Elo Update:**\nThe standard formula is: `R_i^(k) ← R_i^(k) + K(r_ij^(k) - p̂_ij^(k))` where K is a global constant and `p̂_ij^(k) = σ(R_i^(k) - R_j^(k))` is the sigmoid-based win probability.\n\n**Adaptive Mechanism:**\nUDA replaces the fixed K with an instance-level K_ij and hard binary labels r_ij^(k) with soft labels (s_i, s_j) ∈ (0,1). Both are \"output by a compact neural network\" that processes comparison-specific features.\n\n## 2. Neural Network Architecture\n\n**Input Features:** A 6D+9 dimensional feature vector φ_ij^(k) constructed from answer embeddings (e_i, e_j) and judge's own embedding (e_k):\n- 6 high-dimensional vectors (element-wise differences, normalized products)\n- 9 scalars (cosine similarities, KL-divergences, norm differences)\n\n**Model:** \"A small Multilayer Perceptron (MLP) f_θ: ℝ^(6D+9) → ℝ^3\" maps features to (K_ij, s_i, s_j). Full details provided in Algorithm 1 of the paper.\n\n**Layers:** Described as \"3-layer MLP\" in training details; no other architectural specifics disclosed.\n\n## 3. Loss Function & Optimization Objective\n\nThree-term objective (Equation 3):\n```\nL(θ) = α∑_b ||R^(b) - G||_2^2 + σ||R̄ - G||_2^2 + β∑_b(1 - ρ_p(R^(b), G))\n```\n\nWhere:\n- First term: pulls each judge's scores toward consensus anchor G\n- Second term: enforces collective agreement across all judges\n- Third term: maximizes Pearson rank correlation with consensus\n\n## 4. Required Inputs\n\n- Pairwise judge preferences: r_ij^(k) ∈ {0,1} (binary win/loss for response pair)\n- Embeddings: semantic representations of two candidate answers + judge's own generated response\n- Current Elo scores: R_i^(k) for all model-judge pairs\n\n**Format:** \"All pairwise comparisons issued by a single judge k_b in one forward pass\" grouped into judge-homogeneous mini-batches.\n\n## 5. Outputs\n\n- **Debiased Elo scores:** R_i^(k)(UDA) for each model under each judge\n- **Soft labels:** (s_i, s_j) replacing hard binary preferences\n- **Adaptive K-factors:** Instance-specific weighting (K_ij)\n\n## 6. Training Procedure\n\n**Dataset:** 500 ArenaHard prompts, 10 LLM judges, 450,000 pairwise judgments total\n\n**Details:** \"AdamW optimizer\" with \"learning rate scheduler\"; \"best model selected based on validation loss.\" Computation: \"8 hours on a single 4090\" GPU.\n\n**Hyperparameters:** Loss weights α, σ, β mentioned but specific values relegated to appendix (not provided in excerpt).\n\n## 7. Algorithms & Pseudocode\n\n**Algorithm 1:** Detailed feature construction (6D+9 dimensions from embeddings)\n\n**Algorithm 2:** Adaptive Elo Update\n```\nInput: responses, judge k, current scores\nOutput: updated scores R_i^(k), R_j^(k)\n\n1. Compute features φ_ij (Algorithm 1)\n2. Forward pass: (K_ij, s_i, s_j) ← f_θ(φ_ij)\n3. p̂_ij^(k) ← σ(R_i^(k) - R_j^(k))\n4. R_i^(k) ← R_i^(k) + K_ij(s_i - p̂_ij^(k))\n5. R_j^(k) ← R_j^(k) + K_ij(s_j - (1 - p̂_ij^(k)))\n```\n\n## Additional Code/Data Links\n\nOnly one repository mentioned:\n- **Anonymous submission:** https://anonymous.4open.science/r/62AB93CD-23B4 (contains code, checkpoints, Human-Annotated Transfer Set)\n\nNo alternative public repositories provided in the document.",
    "durationMs": 13372,
    "url": "https://arxiv.org/html/2508.09724"
  }
}
````

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Now let me check their GitHub profiles specifically for UDA code.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "83dcca2e-a74d-4ecc-b196-1fce55421ea2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSrcZw4Mwr3Xi3rYGXXu5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1654,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 33536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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

_source line 44_

<details open><summary>🔧 Tool call — WebFetch · `toolu_019YswkCYBGzHX8T2c6QBtVQ`</summary>

```json
{
  "url": "https://github.com/baoguangsheng",
  "prompt": "List all repositories. Is there any repo related to UDA, debiasing, judge bias, Elo rating, or LLM evaluation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "a3dc1556-f447-4ac5-a0f5-cb91b136b4ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSrcZw4Mwr3Xi3rYGXXu5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1654,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 33536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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

_source line 45_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FcvRDE25e64VMy89RXbZcZ`</summary>

```json
{
  "url": "https://github.com/wangcunxiang",
  "prompt": "List all repositories. Is there any repo related to UDA, debiasing, judge bias, Elo rating, or LLM evaluation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "9bbd2231-a2e3-4028-8be9-fa4536b62544",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QSrcZw4Mwr3Xi3rYGXXu5e",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1654,
      "cache_creation_input_tokens": 2339,
      "cache_read_input_tokens": 33536,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2339
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

_source line 46 · 2026-05-22T00:45:54.856Z_

<details><summary>↩ Tool result · `toolu_019YswkCYBGzHX8T2c6QBtVQ`</summary>

```text
# Repository Analysis for baoguangsheng

Based on the visible repositories listed, here are all 6 shown:

1. **fast-detect-gpt** - GPT detection
2. **glimpse** - LLM-generated text detection
3. **g-transformer** - Document-level machine translation
4. **ctx-rewriter-for-summ** - Text summarization
5. **target-side-augmentation** - Machine translation
6. **bart-rewriters** - Text summarization framework

## Relevant to Your Query

**No repositories directly related to UDA, debiasing, judge bias, Elo rating, or LLM evaluation** are visible in this listing.

The closest match is **glimpse**, which addresses "Zero-Shot LLM-Generated Text Detection," but this focuses on detecting AI-generated content rather than evaluating LLM performance through bias assessment or rating systems.

Note: The profile shows "12" total repositories, so additional projects not displayed in the "Popular repositories" section may exist that could relate to your research interests.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "45c3c45f-65be-4423-855c-acca7cc69890",
  "tool_use_result": {
    "bytes": 216060,
    "code": 200,
    "codeText": "OK",
    "result": "# Repository Analysis for baoguangsheng\n\nBased on the visible repositories listed, here are all 6 shown:\n\n1. **fast-detect-gpt** - GPT detection\n2. **glimpse** - LLM-generated text detection\n3. **g-transformer** - Document-level machine translation\n4. **ctx-rewriter-for-summ** - Text summarization\n5. **target-side-augmentation** - Machine translation\n6. **bart-rewriters** - Text summarization framework\n\n## Relevant to Your Query\n\n**No repositories directly related to UDA, debiasing, judge bias, Elo rating, or LLM evaluation** are visible in this listing.\n\nThe closest match is **glimpse**, which addresses \"Zero-Shot LLM-Generated Text Detection,\" but this focuses on detecting AI-generated content rather than evaluating LLM performance through bias assessment or rating systems.\n\nNote: The profile shows \"12\" total repositories, so additional projects not displayed in the \"Popular repositories\" section may exist that could relate to your research interests.",
    "durationMs": 3631,
    "url": "https://github.com/baoguangsheng"
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-22T00:45:55.324Z_

<details><summary>↩ Tool result · `toolu_01FcvRDE25e64VMy89RXbZcZ`</summary>

```text
# Repository Analysis for wangcunxiang

Based on the visible content, only **two pinned repositories** are clearly shown:

1. **QA-Eval** - "The repository for paper &lt;Evaluating Open-QA Evaluation>" (Python)
2. **LLM-Factuality-Survey** - Related to "Survey on Large Language Models Factuality"

## Answer to Your Question

The page indicates there are **26 total repositories**, but only these 2 are displayed. From what's visible, **QA-Eval appears evaluation-related**, which could involve LLM assessment methodologies. However, **the content doesn't explicitly confirm repositories specifically focused on UDA, debiasing, judge bias, Elo rating, or LLM evaluation**.

To find repositories matching your criteria, you would need to visit the full [Repositories tab](/wangcunxiang?tab=repositories) to review all 26 projects, as the overview page displays limited information.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "f3f94ac7-a9c5-429d-b46f-1e320dd5258f",
  "tool_use_result": {
    "bytes": 199550,
    "code": 200,
    "codeText": "OK",
    "result": "# Repository Analysis for wangcunxiang\n\nBased on the visible content, only **two pinned repositories** are clearly shown:\n\n1. **QA-Eval** - \"The repository for paper &lt;Evaluating Open-QA Evaluation>\" (Python)\n2. **LLM-Factuality-Survey** - Related to \"Survey on Large Language Models Factuality\"\n\n## Answer to Your Question\n\nThe page indicates there are **26 total repositories**, but only these 2 are displayed. From what's visible, **QA-Eval appears evaluation-related**, which could involve LLM assessment methodologies. However, **the content doesn't explicitly confirm repositories specifically focused on UDA, debiasing, judge bias, Elo rating, or LLM evaluation**.\n\nTo find repositories matching your criteria, you would need to visit the full [Repositories tab](/wangcunxiang?tab=repositories) to review all 26 projects, as the overview page displays limited information.",
    "durationMs": 3411,
    "url": "https://github.com/wangcunxiang"
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Let me check all repos for both authors, and also check if there's a repo specifically for UDA under either account.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "7dfb30be-01c7-4b08-b181-c17b788644f3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rFiintxRFbGBTeSfWioTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

_source line 49_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015z8qbQ8NQojw1QNDoJqnDa`</summary>

```json
{
  "url": "https://github.com/wangcunxiang?tab=repositories",
  "prompt": "List ALL repositories. Is there any repo related to UDA, debiasing, judge bias, Elo, or LLM evaluation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "a69318bf-0672-48db-8843-872e23a3ae6c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rFiintxRFbGBTeSfWioTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XiRCrzLnHretdGeauNyFsx`</summary>

```json
{
  "query": "paperswithcode \"Unsupervised Debiasing Alignment\" UDA pairwise judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "a934ad79-8e55-433a-883a-f0b78247e522",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015rFiintxRFbGBTeSfWioTo",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2402,
      "cache_read_input_tokens": 35875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2402
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

_source line 51 · 2026-05-22T00:46:06.502Z_

<details><summary>↩ Tool result · `toolu_015z8qbQ8NQojw1QNDoJqnDa`</summary>

```text
# All Repositories Listed

The user has **26 repositories** total. Here's the complete list:

1. LLM-Factuality-Survey
2. wangcunxiang.github.io
3. Graph-aS-Tokens
4. PaperReading
5. Self-Rewarding-Language-Models
6. QA-Eval
7. RFiD
8. Can-PLM-Serve-as-KB-for-CBQA
9. Exploring-Generalization-Ability-of-PLMs-on-Arithmetic-and-Logical-Reasoning
10. fairseq
11. Sen-Making-and-Explanation
12. sensemaking-baselines
13. SemEval2020-Task4-Commonsense-Validation-and-Explanation
14. ML-NLP
15. TextEncoderEnhandedTuckER
16. TuckER
17. Domain-Representation-for-Knowledge-Graph-Embedding
18. kg-bert
19. wangcunxiang.github.io-to-be-constructed
20. self-attentive-parser
21. CSrankings
22. graph-based-deep-learning-literature
23. neural-graph-to-seq-mp
24. samples-for-ai
25. PaintBoard
26. hello-world

## Relevant to Your Query

**QA-Eval** appears most directly relevant: "The repository for paper &lt;Evaluating Open-QA Evaluation>" suggests work in evaluation methodology. **LLM-Factuality-Survey** addresses "Survey on Large Language Models Factuality," potentially covering evaluation aspects.

However, no repositories explicitly mention **UDA, debiasing, judge bias, Elo ratings**, or dedicated LLM evaluation frameworks in their descriptions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "b367801a-a893-4df5-81c5-6d809ca54aa9",
  "tool_use_result": {
    "bytes": 293557,
    "code": 200,
    "codeText": "OK",
    "result": "# All Repositories Listed\n\nThe user has **26 repositories** total. Here's the complete list:\n\n1. LLM-Factuality-Survey\n2. wangcunxiang.github.io\n3. Graph-aS-Tokens\n4. PaperReading\n5. Self-Rewarding-Language-Models\n6. QA-Eval\n7. RFiD\n8. Can-PLM-Serve-as-KB-for-CBQA\n9. Exploring-Generalization-Ability-of-PLMs-on-Arithmetic-and-Logical-Reasoning\n10. fairseq\n11. Sen-Making-and-Explanation\n12. sensemaking-baselines\n13. SemEval2020-Task4-Commonsense-Validation-and-Explanation\n14. ML-NLP\n15. TextEncoderEnhandedTuckER\n16. TuckER\n17. Domain-Representation-for-Knowledge-Graph-Embedding\n18. kg-bert\n19. wangcunxiang.github.io-to-be-constructed\n20. self-attentive-parser\n21. CSrankings\n22. graph-based-deep-learning-literature\n23. neural-graph-to-seq-mp\n24. samples-for-ai\n25. PaintBoard\n26. hello-world\n\n## Relevant to Your Query\n\n**QA-Eval** appears most directly relevant: \"The repository for paper &lt;Evaluating Open-QA Evaluation>\" suggests work in evaluation methodology. **LLM-Factuality-Survey** addresses \"Survey on Large Language Models Factuality,\" potentially covering evaluation aspects.\n\nHowever, no repositories explicitly mention **UDA, debiasing, judge bias, Elo ratings**, or dedicated LLM evaluation frameworks in their descriptions.",
    "durationMs": 6242,
    "url": "https://github.com/wangcunxiang?tab=repositories"
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-22T00:46:09.473Z_

<details><summary>↩ Tool result · `toolu_01XiRCrzLnHretdGeauNyFsx`</summary>

```text
Web search results for query: "paperswithcode "Unsupervised Debiasing Alignment" UDA pairwise judge"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"Privileged Pairwise Judges","url":"https://www.emergentmind.com/topics/privileged-pairwise-judges"},{"title":"(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"}]

I found results for the paper you searched for. Here's what I found:

UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where for each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.

The research addresses preference bias in pairwise evaluation of LLMs, where judges systematically favor certain outputs, leading to inconsistent and skewed rankings across different judges.

UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable and reproducible evaluation.

Key results: Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

The paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "e79ee6e2-666b-4e14-909d-a8eda646b614",
  "tool_use_result": {
    "query": "paperswithcode \"Unsupervised Debiasing Alignment\" UDA pairwise judge",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SXyghZu7EC2U1YpNjzdT7y",
        "content": [
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "Privileged Pairwise Judges",
            "url": "https://www.emergentmind.com/topics/privileged-pairwise-judges"
          },
          {
            "title": "(PDF) UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://www.researchgate.net/publication/394472798_UDA_Unsupervised_Debiasing_Alignment_for_Pair-wise_LLM-as-a-Judge"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          }
        ]
      },
      "I found results for the paper you searched for. Here's what I found:\n\nUDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system, where for each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities.\n\nThe research addresses preference bias in pairwise evaluation of LLMs, where judges systematically favor certain outputs, leading to inconsistent and skewed rankings across different judges.\n\nUDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges, forcing an alignment towards a collective consensus that serves as an unsupervised proxy for more stable and reproducible evaluation.\n\nKey results: Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.\n\nThe paper was published in the Proceedings of the AAAI Conference on Artificial Intelligence, 40(41)."
    ],
    "durationSeconds": 8.810421747999994
  }
}
```

</details>

---

### Assistant

_source line 53_

<details><summary>Logged reasoning block</summary>

```text
Let me also check if the first author (Yang Zhang) has a GitHub repo for UDA, and also check the AAAI proceedings page which might have a supplementary link or code link.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "d4ba0f43-6113-4e89-a0fd-92737c1330b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrSuWBWiBsu8ktDDs86MV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 38277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1407
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

_source line 54_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017JqabyvEXQ1MdqpXaFgvec`</summary>

```json
{
  "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788",
  "prompt": "Is there a link to source code, supplementary materials, or GitHub repository on this page? Extract the DOI and any code/data links."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "a9853a16-0d8d-4d89-a19c-8124f5f13f16",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrSuWBWiBsu8ktDDs86MV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 38277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1407
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

_source line 55_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EcgAyH5AU6dThunJufRkeD`</summary>

```json
{
  "query": "\"Yang Zhang\" \"Yidong Wang\" github UDA Elo debiasing 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "5a0b0b32-fc00-4158-a6da-577759ec4d98",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FrSuWBWiBsu8ktDDs86MV6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1407,
      "cache_read_input_tokens": 38277,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1407
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

_source line 56 · 2026-05-22T00:46:22.778Z_

<details><summary>↩ Tool result · `toolu_017JqabyvEXQ1MdqpXaFgvec`</summary>

```text
# Paper Information

**DOI:** https://doi.org/10.1609/aaai.v40i41.40788

**Code/Data Links:** No links to source code, supplementary materials, or GitHub repository are provided on this page.

The page only offers downloads for the "PDF" and "Poster" associated with the paper, but does not include any external code or data repository links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "f6072382-fed3-4762-ab9a-3c184d1dbd7e",
  "tool_use_result": {
    "bytes": 25551,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Information\n\n**DOI:** https://doi.org/10.1609/aaai.v40i41.40788\n\n**Code/Data Links:** No links to source code, supplementary materials, or GitHub repository are provided on this page.\n\nThe page only offers downloads for the \"PDF\" and \"Poster\" associated with the paper, but does not include any external code or data repository links.",
    "durationMs": 2622,
    "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-22T00:46:25.750Z_

<details><summary>↩ Tool result · `toolu_01EcgAyH5AU6dThunJufRkeD`</summary>

```text
Web search results for query: ""Yang Zhang" "Yidong Wang" github UDA Elo debiasing 2025 2026"

Links: [{"title":"[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/abs/2508.09724"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40788"},{"title":"Yang Zhang","url":"https://www.csauthors.net/yang-zhang/"},{"title":"UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge","url":"https://arxiv.org/pdf/2508.09724"},{"title":"Echoes: Unsupervised Debiasing via Pseudo-bias Labeling in an Echo   Chamber","url":"https://arxiv.org/pdf/2305.04043"}]

Based on the search results, I found information about the research you're looking for:

UDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. The research was authored by Yang Zhang from ZhipuAI and Peking University, along with Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang from ZhipuAI, Guangsheng Bao from Westlake University, and Jie Tang from Tsinghua University.

For each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges.

Experiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.

The paper was published in the Proceedings of the Fortieth AAAI Conference on Artificial Intelligence in 2026, and code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "b700ca38-3927-4102-9bf0-a0ee2d52f8e2",
  "tool_use_result": {
    "query": "\"Yang Zhang\" \"Yidong Wang\" github UDA Elo debiasing 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Au1FkK8Av7XTZCNx91Tw9j",
        "content": [
          {
            "title": "[2508.09724] UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2508.09724"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40788"
          },
          {
            "title": "Yang Zhang",
            "url": "https://www.csauthors.net/yang-zhang/"
          },
          {
            "title": "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2508.09724"
          },
          {
            "title": "Echoes: Unsupervised Debiasing via Pseudo-bias Labeling in an Echo   Chamber",
            "url": "https://arxiv.org/pdf/2305.04043"
          }
        ]
      },
      "Based on the search results, I found information about the research you're looking for:\n\nUDA (Unsupervised Debiasing Alignment) is a framework that reduces inter-judge disagreement by dynamically adjusting the Elo rating system. The research was authored by Yang Zhang from ZhipuAI and Peking University, along with Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang from ZhipuAI, Guangsheng Bao from Westlake University, and Jie Tang from Tsinghua University.\n\nFor each pairwise comparison, a compact neural network learns to adaptively set the K-factor and refine win probabilities. UDA operates in a fully unsupervised manner, guided solely by the objective of minimizing the dispersion among the Elo trajectories of all judges.\n\nExperiments show that UDA significantly reduces the inter-judge rating standard deviation by up to 63.4% and improves the average correlation with human judgments by 24.7%.\n\nThe paper was published in the Proceedings of the Fortieth AAAI Conference on Artificial Intelligence in 2026, and code and data are available at https://anonymous.4open.science/r/62AB93CD-23B4."
    ],
    "durationSeconds": 5.062423269999999
  }
}
```

</details>

---

### Assistant

_source line 58_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also read the project's memory.md to check what was previously noted about UDA.

Key findings:
1. **Code availability**: Anonymous repo (403), no public GitHub repo found. Authors are from ZhipuAI, Peking University, Westlake University, and Tsinghua. None of them have released the code publicly.

2. **Paper details**: 
   - Title: "UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge"
   - Authors: Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang, Guangsheng Bao, Jie Tang
   - Affiliations: ZhipuAI, Peking University, Westlake University, Tsinghua University
   - Venue: AAAI 2026
   - arXiv: 2508.09724

3. **Method summary**: UDA modifies the Elo rating system for pairwise LLM evaluation by using a 3-layer MLP that maps comparison features (6D+9 dimensional) to adjust the rating updates.  The model learns adaptive K-factors per comparison and soft labels instead of hard binary preferences, trained with a loss function combining MSE on rating predictions and Spearman correlation. The approach was trained on 500 ArenaHard prompts with 10 judges producing 450k pairwise judgments, taking 8 hours on a single 4090.

4. **Reimplementation analysis**: To rebuild this, I need to extract features from response embeddings and compute the 6D+9 dimensional feature set including cosine similarity, KL-divergence, and norm differences. Then construct the 3-layer MLP with appropriate input dimensions...

Actually, I'm realizing the feature vector is 6D+9 where D is the embedding dimension, meaning they're using embeddings of both the model responses and the judge's own response to construct the features for each pairwise comparison.

Now I'm thinking through the implementation complexity—this requires coordinating pairwise judgments from multiple judges, embedding all the responses, and having each judge's own response available. Breaking it down, I'd need feature construction, an MLP model, the adaptive Elo update mechanism, a training loop with consensus loss, data loading with embeddings, and evaluation—roughly 300 lines across these components, probably a couple days of work for a solid implementation. I'm also wondering how this relates to G-MFRM, which uses a Rasch model for joint calibration of judge bias and contamination effects.

The key difference is that G-MFRM and UDA operate on different paradigms—one uses Rasch modeling while the other uses Elo-based debiasing—but both ultimately produce debiased scores. To properly compare them, I'd need to get UDA's debiased scores on the same dataset and then write up the comparison.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "509b53e7-ec6b-4474-b332-b13acfc15396",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZvTBXats1YhqJwRQKkthA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 39684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 987
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

_source line 59_

调研完成。以下是 UDA baseline 可行性报告。

---

## UDA 可行性报告

### 1. 论文信息

- **全称**: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge
- **作者**: Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang (ZhipuAI/PKU), Guangsheng Bao (Westlake), Jie Tang (Tsinghua)
- **Venue**: AAAI 2026
- **arXiv**: [2508.09724](https://arxiv.org/abs/2508.09724)
- **核心方法**: 通过可学习的 MLP 动态调整 Elo rating 的 K-factor 和 soft labels，以最小化多 judge 间 Elo 轨迹的 dispersion，达成无监督去偏

### 2. 代码可用性：确认无公开代码

- Anonymous repo (`anonymous.4open.science/r/62AB93CD-23B4`) 返回 **403**，仍不可访问
- AAAI proceedings 页面无代码链接
- 两位关键作者 GitHub（[baoguangsheng](https://github.com/baoguangsheng)、[wangcunxiang](https://github.com/wangcunxiang)）均无 UDA 相关 repo
- PapersWithCode 无收录
- **结论：需要重实现**

### 3. 方法核心描述

**输入**：
- 多 judge 的 pairwise 判断 r_ij^(k) ∈ {0,1}（judge k 对 model i vs j 的 win/loss）
- 每个 response 的 embedding（e_i, e_j）+ judge 自身生成的 response embedding（e_k）

**特征构造**（Algorithm 1）：
- 6D+9 维特征向量 φ_ij^(k)：element-wise differences/products of embeddings（6个D维向量）+ 9个标量（cosine sim、KL-div、norm diff）

**模型**：
- 3-layer MLP: ℝ^(6D+9) → ℝ^3，输出 (K_ij, s_i, s_j)
  - K_ij: 自适应 K-factor（替代固定 K=32）
  - s_i, s_j: soft labels（替代硬 binary 标签）

**Elo 更新**（Algorithm 2）：
```
p̂_ij = σ(R_i - R_j)
R_i ← R_i + K_ij × (s_i - p̂_ij)
R_j ← R_j + K_ij × (s_j - (1 - p̂_ij))
```

**损失函数**：
```
L(θ) = α∑_b ||R^(b) - G||² + σ||R̄ - G||² + β∑_b(1 - ρ_p(R^(b), G))
```
- 第一项：每个 judge 的分数向 consensus anchor G 对齐
- 第二项：集体均值与 G 对齐
- 第三项：Pearson correlation 与 G 一致

**输出**：每个 model 在每个 judge 下的 debiased Elo score

**训练规模**：500 ArenaHard prompts × 10 judges = 450k pairwise judgments，单卡 4090 训练 8h

### 4. 重实现复杂度估算

| 模块 | 行数 | 复杂度 | 说明 |
|------|------|--------|------|
| Feature construction | ~60 | 中 | 6D+9维特征，需 embedding 模型 |
| MLP model | ~30 | 低 | 标准 3-layer MLP |
| Adaptive Elo update | ~40 | 低 | Algorithm 2 直接实现 |
| Consensus loss + training loop | ~100 | 中 | 三项 loss + differentiable Elo |
| Data loader + embedding | ~60 | 中 | 需适配 G-MFRM 数据格式 |
| Evaluation (correlation, std reduction) | ~40 | 低 | 标准指标 |
| **合计** | **~330 行** | — | **预估 2-3 天** |

### 5. 关键难点

1. **Embedding 来源不明**：论文未明确说用什么 embedding 模型。需要选一个（如 sentence-transformers），或论文 appendix 有说明但 HTML 版未完整展示
2. **Judge 自身 response embedding**：UDA 要求 judge 对同一 prompt 也生成 response 并取 embedding——这在 G-MFRM 数据收集时需额外生成
3. **Differentiable Elo**：整个 Elo 更新链需可微（通过 MLP 反传），实现时需注意梯度传播
4. **Consensus anchor G**：论文描述为"mean Elo across judges"，但具体初始化和更新策略需确认

### 6. 与 G-MFRM Pipeline 的接口对接

**兼容性**：
- G-MFRM 的 exp-001 数据收集（多 judge pairwise judgments on ArenaHard）可直接复用为 UDA 的输入
- 需额外：为每个 judge 生成对应 prompt 的 response（用于 e_k 特征）
- 输出：UDA 产出 debiased Elo scores，可与 G-MFRM 的 debiased ability estimates 在 rank correlation / agreement with human 指标上直接对比

**对接方案**：
```python
# 输入接口
def uda_debias(
    pairwise_judgments: dict[str, list[tuple[str, str, int]]],  # judge_id -> [(model_i, model_j, win)]
    response_embeddings: dict[str, np.ndarray],  # model_id -> embedding matrix
    judge_response_embeddings: dict[str, np.ndarray],  # judge_id -> embedding matrix
) -> dict[str, dict[str, float]]:  # judge_id -> {model_id: debiased_elo}
```

### 7. 建议

重实现可行，核心算法描述清晰（两个 Algorithm 伪代码），3-layer MLP + Elo update 本身不复杂。主要工作量在：
1. 确认 embedding 选择（~0.5天）
2. 核心实现 + 调试（~1.5天）
3. 与 G-MFRM 数据格式适配（~0.5天）

**总估计：2-3 天**，与之前调研结论一致。建议在 exp-001 数据收集完成后开始实现，因为 UDA 需要相同的 pairwise judgment 数据。

Sources:
- [arXiv 2508.09724](https://arxiv.org/abs/2508.09724)
- [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40788)
- [Guangsheng Bao GitHub](https://github.com/baoguangsheng)
- [Cunxiang Wang GitHub](https://github.com/wangcunxiang)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "uuid": "44d02b5c-6ae5-4067-aa97-0329f1ba5899",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019ZvTBXats1YhqJwRQKkthA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 987,
      "cache_read_input_tokens": 39684,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 987
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

_source line 60_

调研完成。以下是 UDA baseline 可行性报告。

---

## UDA 可行性报告

### 1. 论文信息

- **全称**: UDA: Unsupervised Debiasing Alignment for Pair-wise LLM-as-a-Judge
- **作者**: Yang Zhang, Cunxiang Wang, Lindong Wu, Wenbo Yu, Yidong Wang (ZhipuAI/PKU), Guangsheng Bao (Westlake), Jie Tang (Tsinghua)
- **Venue**: AAAI 2026
- **arXiv**: [2508.09724](https://arxiv.org/abs/2508.09724)
- **核心方法**: 通过可学习的 MLP 动态调整 Elo rating 的 K-factor 和 soft labels，以最小化多 judge 间 Elo 轨迹的 dispersion，达成无监督去偏

### 2. 代码可用性：确认无公开代码

- Anonymous repo (`anonymous.4open.science/r/62AB93CD-23B4`) 返回 **403**，仍不可访问
- AAAI proceedings 页面无代码链接
- 两位关键作者 GitHub（[baoguangsheng](https://github.com/baoguangsheng)、[wangcunxiang](https://github.com/wangcunxiang)）均无 UDA 相关 repo
- PapersWithCode 无收录
- **结论：需要重实现**

### 3. 方法核心描述

**输入**：
- 多 judge 的 pairwise 判断 r_ij^(k) ∈ {0,1}（judge k 对 model i vs j 的 win/loss）
- 每个 response 的 embedding（e_i, e_j）+ judge 自身生成的 response embedding（e_k）

**特征构造**（Algorithm 1）：
- 6D+9 维特征向量 φ_ij^(k)：element-wise differences/products of embeddings（6个D维向量）+ 9个标量（cosine sim、KL-div、norm diff）

**模型**：
- 3-layer MLP: ℝ^(6D+9) → ℝ^3，输出 (K_ij, s_i, s_j)
  - K_ij: 自适应 K-factor（替代固定 K=32）
  - s_i, s_j: soft labels（替代硬 binary 标签）

**Elo 更新**（Algorithm 2）：
```
p̂_ij = σ(R_i - R_j)
R_i ← R_i + K_ij × (s_i - p̂_ij)
R_j ← R_j + K_ij × (s_j - (1 - p̂_ij))
```

**损失函数**：
```
L(θ) = α∑_b ||R^(b) - G||² + σ||R̄ - G||² + β∑_b(1 - ρ_p(R^(b), G))
```
- 第一项：每个 judge 的分数向 consensus anchor G 对齐
- 第二项：集体均值与 G 对齐
- 第三项：Pearson correlation 与 G 一致

**输出**：每个 model 在每个 judge 下的 debiased Elo score

**训练规模**：500 ArenaHard prompts × 10 judges = 450k pairwise judgments，单卡 4090 训练 8h

### 4. 重实现复杂度估算

| 模块 | 行数 | 复杂度 | 说明 |
|------|------|--------|------|
| Feature construction | ~60 | 中 | 6D+9维特征，需 embedding 模型 |
| MLP model | ~30 | 低 | 标准 3-layer MLP |
| Adaptive Elo update | ~40 | 低 | Algorithm 2 直接实现 |
| Consensus loss + training loop | ~100 | 中 | 三项 loss + differentiable Elo |
| Data loader + embedding | ~60 | 中 | 需适配 G-MFRM 数据格式 |
| Evaluation (correlation, std reduction) | ~40 | 低 | 标准指标 |
| **合计** | **~330 行** | — | **预估 2-3 天** |

### 5. 关键难点

1. **Embedding 来源不明**：论文未明确说用什么 embedding 模型。需要选一个（如 sentence-transformers），或论文 appendix 有说明但 HTML 版未完整展示
2. **Judge 自身 response embedding**：UDA 要求 judge 对同一 prompt 也生成 response 并取 embedding——这在 G-MFRM 数据收集时需额外生成
3. **Differentiable Elo**：整个 Elo 更新链需可微（通过 MLP 反传），实现时需注意梯度传播
4. **Consensus anchor G**：论文描述为"mean Elo across judges"，但具体初始化和更新策略需确认

### 6. 与 G-MFRM Pipeline 的接口对接

**兼容性**：
- G-MFRM 的 exp-001 数据收集（多 judge pairwise judgments on ArenaHard）可直接复用为 UDA 的输入
- 需额外：为每个 judge 生成对应 prompt 的 response（用于 e_k 特征）
- 输出：UDA 产出 debiased Elo scores，可与 G-MFRM 的 debiased ability estimates 在 rank correlation / agreement with human 指标上直接对比

**对接方案**：
```python
# 输入接口
def uda_debias(
    pairwise_judgments: dict[str, list[tuple[str, str, int]]],  # judge_id -> [(model_i, model_j, win)]
    response_embeddings: dict[str, np.ndarray],  # model_id -> embedding matrix
    judge_response_embeddings: dict[str, np.ndarray],  # judge_id -> embedding matrix
) -> dict[str, dict[str, float]]:  # judge_id -> {model_id: debiased_elo}
```

### 7. 建议

重实现可行，核心算法描述清晰（两个 Algorithm 伪代码），3-layer MLP + Elo update 本身不复杂。主要工作量在：
1. 确认 embedding 选择（~0.5天）
2. 核心实现 + 调试（~1.5天）
3. 与 G-MFRM 数据格式适配（~0.5天）

**总估计：2-3 天**，与之前调研结论一致。建议在 exp-001 数据收集完成后开始实现，因为 UDA 需要相同的 pairwise judgment 数据。

Sources:
- [arXiv 2508.09724](https://arxiv.org/abs/2508.09724)
- [AAAI 2026 Proceedings](https://ojs.aaai.org/index.php/AAAI/article/view/40788)
- [Guangsheng Bao GitHub](https://github.com/baoguangsheng)
- [Cunxiang Wang GitHub](https://github.com/wangcunxiang)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 198985,
  "duration_api_ms": 243192,
  "num_turns": 22,
  "stop_reason": "end_turn",
  "session_id": "f0ba1ad2-6c8a-4e3a-9068-da919a2e14b5",
  "total_cost_usd": 0.8211935,
  "usage": {
    "input_tokens": 3094,
    "cache_creation_input_tokens": 29224,
    "cache_read_input_tokens": 329969,
    "output_tokens": 5618,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 29224,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 3047,
        "cache_read_input_tokens": 39684,
        "cache_creation_input_tokens": 987,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 987
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 170874,
      "outputTokens": 7353,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 11,
      "costUSD": 0.317639,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3094,
      "outputTokens": 5618,
      "cacheReadInputTokens": 329969,
      "cacheCreationInputTokens": 29224,
      "webSearchRequests": 0,
      "costUSD": 0.5035544999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "895bd2af-62ca-45a0-a11a-858ccedb87fa"
}
```

</details>

---
