# research reference verification

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 24
- **Recorded user turns:** 0
- **Tool calls:** 7
- **Original source:** `logs/workers/worker_research_reference-verification_20260524T033647.log`
- **Structured JSON:** [`620f8868fdfd74c88cb5.json`](../../sessions/62/620f8868fdfd74c88cb5.json)

## Before a recorded user message

24 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval",
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
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
  "uuid": "59b5cbcb-2efa-4a32-a20d-42d8489d32c6",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0519-2-projects-cert-manip-resist-eval/memory/"
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
    "resetsAt": 1779610200,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "0ee382a8-4e61-4934-a867-63bd0261f7d7",
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
I need to verify 3 papers suggested by reviewers. Let me search for each one using WebSearch, then fetch details with WebFetch.

Let me first load the WebSearch and WebFetch tools.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "d2d5e990-1a0a-4f64-af85-c03603f4505c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtM3tbaL2Jz42BxeZR9xTr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12069
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01BvibRma98rF35MNYbvfDax`</summary>

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
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "23186a7e-802f-4799-a1f0-561825fa6425",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XtM3tbaL2Jz42BxeZR9xTr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 12069,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12069
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

_source line 6 · 2026-05-24T03:37:01.715Z_

<details><summary>↩ Tool result · `toolu_01BvibRma98rF35MNYbvfDax`</summary>

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
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "7f4cfdbb-e42d-4f62-8be5-9decb50f3672",
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
Now let me search for all 3 papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "2d00ff35-3b8d-4e68-bab0-cb2712977597",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tSDdxeRChGHWqpNytYbdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
      },
      "output_tokens": 18,
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

并行搜索 3 篇论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "8cd61786-9c5c-4bfc-8658-14b29c47fc31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tSDdxeRChGHWqpNytYbdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BYbne41DnLDbx6uojHRqHF`</summary>

```json
{
  "query": "arXiv 2505.13348 Maloyan prompt injection LLM-as-Judge"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "f47e2d9a-c192-43bd-b676-333f8087af5d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tSDdxeRChGHWqpNytYbdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GyMaxq2qTH7cJfgMrXzEAp`</summary>

```json
{
  "query": "arXiv 2511.05269 TAMAS multi-agent adversarial benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "c91fb824-542f-4bfe-8f97-2501ee02229f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tSDdxeRChGHWqpNytYbdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D52i9Le9AjgSq6McnbY9na`</summary>

```json
{
  "query": "arXiv 2505.24239 adversary-resistant multi-agent credibility scoring"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "41a37939-71cf-42e4-96fd-eeefa6619acd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013tSDdxeRChGHWqpNytYbdh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1159,
      "cache_read_input_tokens": 23910,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1159
      },
      "output_tokens": 18,
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

_source line 12 · 2026-05-24T03:37:11.479Z_

<details><summary>↩ Tool result · `toolu_01BYbne41DnLDbx6uojHRqHF`</summary>

```text
Web search results for query: "arXiv 2505.13348 Maloyan prompt injection LLM-as-Judge"

Links: [{"title":"[2505.13348] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/abs/2505.13348"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge ...","url":"https://arxiv.org/pdf/2505.13348"},{"title":"(PDF) Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://www.researchgate.net/publication/391911310_Investigating_the_Vulnerability_of_LLM-as-a-Judge_Architectures_to_Prompt-Injection_Attacks"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/html/2505.13348v1"},{"title":"[PDF] Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Adversarial-Attacks-on-LLM-as-a-Judge-Systems:-from-Maloyan-Namiot/502b573666af63c5baa7bc24673c9d4c78dd28e8"},{"title":"[2504.18333] Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections","url":"https://arxiv.org/abs/2504.18333"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250513348M/abstract"},{"title":"Security in LLM-as-a-Judge: A Comprehensive SoK","url":"https://arxiv.org/html/2603.29403v2"},{"title":"Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/adversarial-attacks-llm-as-judge-systems-insights"}]

I found the paper you're looking for. Here's the information about arXiv 2505.13348:

**Title:** Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks

**Authors:** Narek Maloyan, Bislan Ashinov, and Dmitry Namiot

**Submission Date:** May 19, 2025

**Overview:** Large Language Models (LLMs) are increasingly employed as evaluators (LLM-as-a-Judge) for assessing the quality of machine-generated text. This paradigm offers scalability and cost-effectiveness compared to human annotation. However, the paper investigates the vulnerability of LLM-as-a-Judge architectures to prompt-injection attacks, where malicious inputs are designed to compromise the judge's decision-making process.

**Key Attack Methods:** The paper formalizes two primary attack strategies: Comparative Undermining Attack (CUA), which directly targets the final decision output, and Justification Manipulation Attack (JMA), which aims to alter the model's generated reasoning. The researchers craft adversarial suffixes appended to one of the responses being compared using the Greedy Coordinate Gradient (GCG) optimization method.

The full paper is available on arXiv at https://arxiv.org/abs/2505.13348.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "cb7c2a07-82db-449c-ad5b-fadbe126aa7b",
  "tool_use_result": {
    "query": "arXiv 2505.13348 Maloyan prompt injection LLM-as-Judge",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U121RvUjBQ4UWYMQEmoS4a",
        "content": [
          {
            "title": "[2505.13348] Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks",
            "url": "https://arxiv.org/abs/2505.13348"
          },
          {
            "title": "Investigating the Vulnerability of LLM-as-a-Judge ...",
            "url": "https://arxiv.org/pdf/2505.13348"
          },
          {
            "title": "(PDF) Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks",
            "url": "https://www.researchgate.net/publication/391911310_Investigating_the_Vulnerability_of_LLM-as-a-Judge_Architectures_to_Prompt-Injection_Attacks"
          },
          {
            "title": "Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks",
            "url": "https://arxiv.org/html/2505.13348v1"
          },
          {
            "title": "[PDF] Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Adversarial-Attacks-on-LLM-as-a-Judge-Systems:-from-Maloyan-Namiot/502b573666af63c5baa7bc24673c9d4c78dd28e8"
          },
          {
            "title": "[2504.18333] Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections",
            "url": "https://arxiv.org/abs/2504.18333"
          },
          {
            "title": "Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250513348M/abstract"
          },
          {
            "title": "Security in LLM-as-a-Judge: A Comprehensive SoK",
            "url": "https://arxiv.org/html/2603.29403v2"
          },
          {
            "title": "Adversarial Attacks on LLM-as-a-Judge Systems: Insights from Prompt Injections | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/adversarial-attacks-llm-as-judge-systems-insights"
          }
        ]
      },
      "I found the paper you're looking for. Here's the information about arXiv 2505.13348:\n\n**Title:** Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks\n\n**Authors:** Narek Maloyan, Bislan Ashinov, and Dmitry Namiot\n\n**Submission Date:** May 19, 2025\n\n**Overview:** Large Language Models (LLMs) are increasingly employed as evaluators (LLM-as-a-Judge) for assessing the quality of machine-generated text. This paradigm offers scalability and cost-effectiveness compared to human annotation. However, the paper investigates the vulnerability of LLM-as-a-Judge architectures to prompt-injection attacks, where malicious inputs are designed to compromise the judge's decision-making process.\n\n**Key Attack Methods:** The paper formalizes two primary attack strategies: Comparative Undermining Attack (CUA), which directly targets the final decision output, and Justification Manipulation Attack (JMA), which aims to alter the model's generated reasoning. The researchers craft adversarial suffixes appended to one of the responses being compared using the Greedy Coordinate Gradient (GCG) optimization method.\n\nThe full paper is available on arXiv at https://arxiv.org/abs/2505.13348."
    ],
    "durationSeconds": 6.106078582
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-24T03:37:12.332Z_

<details><summary>↩ Tool result · `toolu_01GyMaxq2qTH7cJfgMrXzEAp`</summary>

```text
Web search results for query: "arXiv 2511.05269 TAMAS multi-agent adversarial benchmark"

Links: [{"title":"[2511.05269] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/abs/2511.05269"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | alphaXiv","url":"https://www.alphaxiv.org/resources/2511.05269v1"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/pdf/2511.05269"},{"title":"TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://arxiv.org/html/2511.05269v1"},{"title":"[PDF] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | Semantic Scholar","url":"https://www.semanticscholar.org/paper/TAMAS:-Benchmarking-Adversarial-Risks-in-LLM-Kavathekar-Jain/6aba9c3fc42286af5e8d42712c07a1033a763cc2"},{"title":"Ponnurangam Kumaraguru “PK” on X: \"🚨 New Paper Alert! 🚀 We introduce TAMAS, a benchmark for evaluating adversarial risks in multi-agent LLM systems. Multi-agent setups are powerful, but they bring new vulnerabilities we can’t ignore! Preprint: https://t.co/JeCuw7Z4nt Code: https://t.co/Cw44Bc3BNh 1/n 🧵 https://t.co/m3FFMqSCxd\" / X","url":"https://x.com/ponguru/status/2003675865666978081"},{"title":"Benchmarking Adversarial Risks in Multi-Agent LLM Systems","url":"https://openreview.net/pdf/2aa259f9b8c9ba825cef9cb90e54b40eaed01030.pdf"}]

Based on the search results, here's what I found about arXiv paper 2511.05269:

TAMAS (Threats and Attacks in Multi-Agent Systems) is a benchmark designed to evaluate the robustness and safety of multi-agent LLM systems.

**Key Details:**

- **Authors:** Ishan Kavathekar, Hemang Jain, Ameya Rathod, Ponnurangam Kumaraguru, and Tanuja Ganu
- **Submission Date:** Submitted on 7 November 2025

**Benchmark Contents:**

TAMAS includes five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools, along with 100 harmless tasks. It spans five high-impact domains (education, legal, healthcare, finance, and news).

**Evaluation Methodology:**

The paper assesses system performance across ten backbone LLMs and three agent interaction configurations from Autogen and CrewAI frameworks. It introduces Effective Robustness Score (ERS) to assess the tradeoff between safety and task effectiveness of these frameworks.

**Findings:**

The findings show that multi-agent systems are highly vulnerable to adversarial attacks, underscoring the urgent need for stronger defenses.

Code is available at https://github.com/microsoft/TAMAS.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "7d6c9af6-c312-464d-960c-25729d1faf62",
  "tool_use_result": {
    "query": "arXiv 2511.05269 TAMAS multi-agent adversarial benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fzw93pRSr3yJsfUhirKpsr",
        "content": [
          {
            "title": "[2511.05269] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems",
            "url": "https://arxiv.org/abs/2511.05269"
          },
          {
            "title": "TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | alphaXiv",
            "url": "https://www.alphaxiv.org/resources/2511.05269v1"
          },
          {
            "title": "TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems",
            "url": "https://arxiv.org/pdf/2511.05269"
          },
          {
            "title": "TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems",
            "url": "https://arxiv.org/html/2511.05269v1"
          },
          {
            "title": "[PDF] TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/TAMAS:-Benchmarking-Adversarial-Risks-in-LLM-Kavathekar-Jain/6aba9c3fc42286af5e8d42712c07a1033a763cc2"
          },
          {
            "title": "Ponnurangam Kumaraguru “PK” on X: \"🚨 New Paper Alert! 🚀 We introduce TAMAS, a benchmark for evaluating adversarial risks in multi-agent LLM systems. Multi-agent setups are powerful, but they bring new vulnerabilities we can’t ignore! Preprint: https://t.co/JeCuw7Z4nt Code: https://t.co/Cw44Bc3BNh 1/n 🧵 https://t.co/m3FFMqSCxd\" / X",
            "url": "https://x.com/ponguru/status/2003675865666978081"
          },
          {
            "title": "Benchmarking Adversarial Risks in Multi-Agent LLM Systems",
            "url": "https://openreview.net/pdf/2aa259f9b8c9ba825cef9cb90e54b40eaed01030.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2511.05269:\n\nTAMAS (Threats and Attacks in Multi-Agent Systems) is a benchmark designed to evaluate the robustness and safety of multi-agent LLM systems.\n\n**Key Details:**\n\n- **Authors:** Ishan Kavathekar, Hemang Jain, Ameya Rathod, Ponnurangam Kumaraguru, and Tanuja Ganu\n- **Submission Date:** Submitted on 7 November 2025\n\n**Benchmark Contents:**\n\nTAMAS includes five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools, along with 100 harmless tasks. It spans five high-impact domains (education, legal, healthcare, finance, and news).\n\n**Evaluation Methodology:**\n\nThe paper assesses system performance across ten backbone LLMs and three agent interaction configurations from Autogen and CrewAI frameworks. It introduces Effective Robustness Score (ERS) to assess the tradeoff between safety and task effectiveness of these frameworks.\n\n**Findings:**\n\nThe findings show that multi-agent systems are highly vulnerable to adversarial attacks, underscoring the urgent need for stronger defenses.\n\nCode is available at https://github.com/microsoft/TAMAS."
    ],
    "durationSeconds": 5.954536779999999
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-24T03:37:12.576Z_

<details><summary>↩ Tool result · `toolu_01D52i9Le9AjgSq6McnbY9na`</summary>

```text
Web search results for query: "arXiv 2505.24239 adversary-resistant multi-agent credibility scoring"

Links: [{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/html/2505.24239v1"},{"title":"Multiagent Systems May 2025","url":"https://www.arxiv.org/list/cs.MA/2025-05?skip=50&show=50"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.90/"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring | Request PDF","url":"https://www.researchgate.net/publication/402602390_An_Adversary-Resistant_Multi-Agent_LLM_System_via_Credibility_Scoring"},{"title":"SentinelNet: Safeguarding Multi-Agent Collaboration Through Credit-Based Dynamic Threat Detection","url":"https://arxiv.org/pdf/2510.16219"},{"title":"An Adversary-Resistant Multi-Agent LLM System via ...","url":"https://arxiv.org/pdf/2505.24239"},{"title":"Multi-agent systems and credibility-based advanced scoring mechanism in fact-checking | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-41862-z"}]

I found the paper you're looking for! Here's what I found about arXiv 2505.24239:

**Title:** An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring

**Authors:** Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh

**Publication:** Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics. 2025.

**Key Concept:** Multi-agent LLM systems are highly vulnerable to adversarial and low-performing agents, and the paper addresses this issue by introducing a general and adversary-resistant multi-agent LLM framework based on credibility scoring.

**Approach:** The system models the collaborative query-answering process as an iterative game where agents communicate and contribute to a final system output. It associates a credibility score used when aggregating team outputs, with credibility scores learned gradually based on the past contributions of each agent in query answering.

The paper is available on arXiv with PDF and HTML versions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "0ff5d1a5-f57e-4550-af15-4b989b6367fc",
  "tool_use_result": {
    "query": "arXiv 2505.24239 adversary-resistant multi-agent credibility scoring",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YRSsiB7yFa7JpTcHyXJSaR",
        "content": [
          {
            "title": "[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring",
            "url": "https://arxiv.org/abs/2505.24239"
          },
          {
            "title": "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring",
            "url": "https://arxiv.org/html/2505.24239v1"
          },
          {
            "title": "Multiagent Systems May 2025",
            "url": "https://www.arxiv.org/list/cs.MA/2025-05?skip=50&show=50"
          },
          {
            "title": "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology",
            "url": "https://aclanthology.org/2025.ijcnlp-long.90/"
          },
          {
            "title": "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring | Request PDF",
            "url": "https://www.researchgate.net/publication/402602390_An_Adversary-Resistant_Multi-Agent_LLM_System_via_Credibility_Scoring"
          },
          {
            "title": "SentinelNet: Safeguarding Multi-Agent Collaboration Through Credit-Based Dynamic Threat Detection",
            "url": "https://arxiv.org/pdf/2510.16219"
          },
          {
            "title": "An Adversary-Resistant Multi-Agent LLM System via ...",
            "url": "https://arxiv.org/pdf/2505.24239"
          },
          {
            "title": "Multi-agent systems and credibility-based advanced scoring mechanism in fact-checking | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-41862-z"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I found about arXiv 2505.24239:\n\n**Title:** An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring\n\n**Authors:** Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh\n\n**Publication:** Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics. 2025.\n\n**Key Concept:** Multi-agent LLM systems are highly vulnerable to adversarial and low-performing agents, and the paper addresses this issue by introducing a general and adversary-resistant multi-agent LLM framework based on credibility scoring.\n\n**Approach:** The system models the collaborative query-answering process as an iterative game where agents communicate and contribute to a final system output. It associates a credibility score used when aggregating team outputs, with credibility scores learned gradually based on the past contributions of each agent in query answering.\n\nThe paper is available on arXiv with PDF and HTML versions."
    ],
    "durationSeconds": 5.756770178999999
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
All 3 papers found. Let me fetch the arXiv abstract pages to get precise author lists and abstracts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "3200e9c6-1cf6-4555-a2db-20e8f5d000e5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ph9CaUG47DjgGnxQkPdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 25069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
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

_source line 16_

3 篇全部搜索到，获取 arXiv 页面确认详细信息。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "fdb3c15f-80cd-4585-88a8-0bb20b41b8de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ph9CaUG47DjgGnxQkPdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 25069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_014Ne9oRd9BH3d7yJG9TfdF4`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.13348",
  "prompt": "Extract: full title, all authors, submission date, arXiv ID, and the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "febc16c5-c94e-4fd0-9233-f1ea65897b64",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ph9CaUG47DjgGnxQkPdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 25069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VvdiVfs52hAU6878156SwN`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.05269",
  "prompt": "Extract: full title, all authors, submission date, arXiv ID, and the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "412a7506-f959-42d7-ad90-42a222d0fd21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ph9CaUG47DjgGnxQkPdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 25069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
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

<details open><summary>🔧 Tool call — WebFetch · `toolu_01B6nYB2wnYTTW6YvPQCNHBR`</summary>

```json
{
  "url": "https://arxiv.org/abs/2505.24239",
  "prompt": "Extract: full title, all authors, submission date, arXiv ID, and the complete abstract text."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "56d46720-008b-4b1f-af47-cec28408a465",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018Ph9CaUG47DjgGnxQkPdEJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2817,
      "cache_read_input_tokens": 25069,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2817
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

_source line 20 · 2026-05-24T03:37:32.606Z_

<details><summary>↩ Tool result · `toolu_01VvdiVfs52hAU6878156SwN`</summary>

```text
# TAMAS Research Paper Details

**Full Title:** TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems

**Authors:**
- Ishan Kavathekar
- Hemang Jain
- Ameya Rathod
- Ponnurangam Kumaraguru
- Tanuja Ganu

**Submission Date:** November 7, 2025

**arXiv ID:** 2511.05269

**Abstract:**
This research introduces a benchmark for evaluating robustness in multi-agent LLM systems. The work addresses a gap in existing safety assessments, which predominantly focus on single-agent scenarios. The benchmark comprises "five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools" alongside harmless baseline tasks. Testing across ten LLM models and configurations from Autogen and CrewAI frameworks revealed significant vulnerabilities. The researchers propose the Effective Robustness Score metric to measure the balance between safety and operational performance. Their findings demonstrate that such systems face substantial adversarial exposure, highlighting the necessity for improved defensive mechanisms in multi-agent deployments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "0ecd7e78-9266-42ed-ae9b-1c37522fa090",
  "tool_use_result": {
    "bytes": 47332,
    "code": 200,
    "codeText": "OK",
    "result": "# TAMAS Research Paper Details\n\n**Full Title:** TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems\n\n**Authors:**\n- Ishan Kavathekar\n- Hemang Jain\n- Ameya Rathod\n- Ponnurangam Kumaraguru\n- Tanuja Ganu\n\n**Submission Date:** November 7, 2025\n\n**arXiv ID:** 2511.05269\n\n**Abstract:**\nThis research introduces a benchmark for evaluating robustness in multi-agent LLM systems. The work addresses a gap in existing safety assessments, which predominantly focus on single-agent scenarios. The benchmark comprises \"five distinct scenarios comprising 300 adversarial instances across six attack types and 211 tools\" alongside harmless baseline tasks. Testing across ten LLM models and configurations from Autogen and CrewAI frameworks revealed significant vulnerabilities. The researchers propose the Effective Robustness Score metric to measure the balance between safety and operational performance. Their findings demonstrate that such systems face substantial adversarial exposure, highlighting the necessity for improved defensive mechanisms in multi-agent deployments.",
    "durationMs": 4151,
    "url": "https://arxiv.org/abs/2511.05269"
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-24T03:37:32.812Z_

<details><summary>↩ Tool result · `toolu_014Ne9oRd9BH3d7yJG9TfdF4`</summary>

```text
# Research Paper Details

**Full Title:** Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks

**Authors:**
- Narek Maloyan
- Bislan Ashinov
- Dmitry Namiot

**Submission Date:** May 19, 2025

**arXiv ID:** 2505.13348

**Abstract:**

Large Language Models are increasingly used as evaluators for assessing machine-generated text quality, offering scalability advantages over human annotation. However, their security and robustness against adversarial manipulation warrant investigation. This research examines how LLM-as-a-Judge systems respond to prompt-injection attacks through two strategies: Comparative Undermining Attack, targeting final decisions, and Justification Manipulation Attack, altering the model's reasoning processes. Using the Greedy Coordinate Gradient optimization technique, researchers developed adversarial suffixes attached to compared responses. Testing on the MT-Bench Human Judgments dataset with smaller instruction-tuned models showed concerning results, with "an Attack Success Rate (ASR) exceeding 30%" for the first method. The findings demonstrate substantial security gaps, emphasizing the necessity for protective measures and additional investigation into evaluation trustworthiness.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "7e6718da-98e4-4681-a439-aebe66dfc331",
  "tool_use_result": {
    "bytes": 46804,
    "code": 200,
    "codeText": "OK",
    "result": "# Research Paper Details\n\n**Full Title:** Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks\n\n**Authors:**\n- Narek Maloyan\n- Bislan Ashinov\n- Dmitry Namiot\n\n**Submission Date:** May 19, 2025\n\n**arXiv ID:** 2505.13348\n\n**Abstract:**\n\nLarge Language Models are increasingly used as evaluators for assessing machine-generated text quality, offering scalability advantages over human annotation. However, their security and robustness against adversarial manipulation warrant investigation. This research examines how LLM-as-a-Judge systems respond to prompt-injection attacks through two strategies: Comparative Undermining Attack, targeting final decisions, and Justification Manipulation Attack, altering the model's reasoning processes. Using the Greedy Coordinate Gradient optimization technique, researchers developed adversarial suffixes attached to compared responses. Testing on the MT-Bench Human Judgments dataset with smaller instruction-tuned models showed concerning results, with \"an Attack Success Rate (ASR) exceeding 30%\" for the first method. The findings demonstrate substantial security gaps, emphasizing the necessity for protective measures and additional investigation into evaluation trustworthiness.",
    "durationMs": 5300,
    "url": "https://arxiv.org/abs/2505.13348"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-24T03:37:33.109Z_

<details><summary>↩ Tool result · `toolu_01B6nYB2wnYTTW6YvPQCNHBR`</summary>

```text
# Paper Extraction

**Full Title:** An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring

**Authors:** Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh

**Submission Date:** 30 May 2025

**arXiv ID:** 2505.24239

**Complete Abstract:**

"While multi-agent LLM systems show strong capabilities in various domains, they are highly vulnerable to adversarial and low-performing agents. To resolve this issue, in this paper, we introduce a general and adversary-resistant multi-agent LLM framework based on credibility scoring. We model the collaborative query-answering process as an iterative game, where the agents communicate and contribute to a final system output. Our system associates a credibility score that is used when aggregating the team outputs. The credibility scores are learned gradually based on the past contributions of each agent in query answering. Our experiments across multiple tasks and settings demonstrate our system's effectiveness in mitigating adversarial influence and enhancing the resilience of multi-agent cooperation, even in the adversary-majority settings."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "e958c8d2-5e85-41e8-8f8d-10861e612c91",
  "tool_use_result": {
    "bytes": 45167,
    "code": 200,
    "codeText": "OK",
    "result": "# Paper Extraction\n\n**Full Title:** An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring\n\n**Authors:** Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh\n\n**Submission Date:** 30 May 2025\n\n**arXiv ID:** 2505.24239\n\n**Complete Abstract:**\n\n\"While multi-agent LLM systems show strong capabilities in various domains, they are highly vulnerable to adversarial and low-performing agents. To resolve this issue, in this paper, we introduce a general and adversary-resistant multi-agent LLM framework based on credibility scoring. We model the collaborative query-answering process as an iterative game, where the agents communicate and contribute to a final system output. Our system associates a credibility score that is used when aggregating the team outputs. The credibility scores are learned gradually based on the past contributions of each agent in query answering. Our experiments across multiple tasks and settings demonstrate our system's effectiveness in mitigating adversarial influence and enhancing the resilience of multi-agent cooperation, even in the adversary-majority settings.\"",
    "durationMs": 4082,
    "url": "https://arxiv.org/abs/2505.24239"
  }
}
```

</details>

---

### Assistant

_source line 23_

3 篇论文全部验证完毕。

---

### Paper 1: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **arXiv ID**: 存在 — [2505.13348](https://arxiv.org/abs/2505.13348)
- **标题**: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **作者**: Narek Maloyan, Bislan Ashinov, Dmitry Namiot
- **年份**: 2025 (May 19)
- **Abstract 摘要**: 研究 LLM-as-a-Judge 系统对 prompt injection 攻击的脆弱性，提出两种攻击策略（CUA 和 JMA），使用 GCG 优化生成对抗后缀，在 MT-Bench 上 ASR 超过 30%。
- **与审稿人描述匹配**: **是** — 审稿人描述 "prompt injection on LLM-as-Judge" 完全准确
- **与本项目相关性**: 本项目研究 certification manipulation resistance，该论文展示了 LLM 评估器可被 prompt injection 操纵，是攻击面的直接相关工作
- **状态**: **verified** ✓

---

### Paper 2: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **arXiv ID**: 存在 — [2511.05269](https://arxiv.org/abs/2511.05269)
- **标题**: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **作者**: Ishan Kavathekar, Hemang Jain, Ameya Rathod, Ponnurangam Kumaraguru, Tanuja Ganu
- **年份**: 2025 (November 7)
- **Abstract 摘要**: 提出多智能体 LLM 系统的对抗风险评估基准，包含 5 个场景、300 个对抗实例、6 种攻击类型，在 10 个 LLM 和 Autogen/CrewAI 框架上评测，引入 Effective Robustness Score (ERS) 指标。
- **与审稿人描述匹配**: **是** — 审稿人描述 "multi-agent adversarial benchmark" 完全准确
- **与本项目相关性**: 作为多智能体系统对抗评估的 benchmark，与本项目的评估框架构成互补/对比关系
- **状态**: **verified** ✓

---

### Paper 3: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **arXiv ID**: 存在 — [2505.24239](https://arxiv.org/abs/2505.24239)
- **标题**: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **作者**: Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh
- **年份**: 2025 (May 30)；已发表于 AACL-IJCNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.ijcnlp-long.90/))
- **Abstract 摘要**: 提出基于 credibility scoring 的对抗鲁棒多智能体 LLM 框架，将协作问答建模为迭代博弈，根据历史贡献学习可信度分数进行输出聚合，即使在对抗方占多数时仍有效。
- **与审稿人描述匹配**: **是** — 审稿人描述 "adversary-resistant multi-agent system" 完全准确
- **与本项目相关性**: 该论文提出的 credibility scoring 防御机制与本项目的 manipulation resistance 评估直接相关，是防御方法的关键 baseline
- **状态**: **verified** ✓

---

**总结**: 3 篇论文全部真实存在，arXiv ID、标题、作者、内容均与审稿人描述一致，无幻觉引用。

Sources:
- [arXiv:2505.13348 - Maloyan et al.](https://arxiv.org/abs/2505.13348)
- [arXiv:2511.05269 - TAMAS](https://arxiv.org/abs/2511.05269)
- [arXiv:2505.24239 - Credibility Scoring](https://arxiv.org/abs/2505.24239)
- [ACL Anthology - Ebrahimi et al.](https://aclanthology.org/2025.ijcnlp-long.90/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "uuid": "bc7e7f32-f5f3-438c-8112-533700b5735c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NuXkr44P1AVhEV1MocSvf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1225,
      "cache_read_input_tokens": 27886,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1225
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

_source line 24_

3 篇论文全部验证完毕。

---

### Paper 1: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **arXiv ID**: 存在 — [2505.13348](https://arxiv.org/abs/2505.13348)
- **标题**: Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks
- **作者**: Narek Maloyan, Bislan Ashinov, Dmitry Namiot
- **年份**: 2025 (May 19)
- **Abstract 摘要**: 研究 LLM-as-a-Judge 系统对 prompt injection 攻击的脆弱性，提出两种攻击策略（CUA 和 JMA），使用 GCG 优化生成对抗后缀，在 MT-Bench 上 ASR 超过 30%。
- **与审稿人描述匹配**: **是** — 审稿人描述 "prompt injection on LLM-as-Judge" 完全准确
- **与本项目相关性**: 本项目研究 certification manipulation resistance，该论文展示了 LLM 评估器可被 prompt injection 操纵，是攻击面的直接相关工作
- **状态**: **verified** ✓

---

### Paper 2: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **arXiv ID**: 存在 — [2511.05269](https://arxiv.org/abs/2511.05269)
- **标题**: TAMAS: Benchmarking Adversarial Risks in Multi-Agent LLM Systems
- **作者**: Ishan Kavathekar, Hemang Jain, Ameya Rathod, Ponnurangam Kumaraguru, Tanuja Ganu
- **年份**: 2025 (November 7)
- **Abstract 摘要**: 提出多智能体 LLM 系统的对抗风险评估基准，包含 5 个场景、300 个对抗实例、6 种攻击类型，在 10 个 LLM 和 Autogen/CrewAI 框架上评测，引入 Effective Robustness Score (ERS) 指标。
- **与审稿人描述匹配**: **是** — 审稿人描述 "multi-agent adversarial benchmark" 完全准确
- **与本项目相关性**: 作为多智能体系统对抗评估的 benchmark，与本项目的评估框架构成互补/对比关系
- **状态**: **verified** ✓

---

### Paper 3: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **arXiv ID**: 存在 — [2505.24239](https://arxiv.org/abs/2505.24239)
- **标题**: An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring
- **作者**: Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh
- **年份**: 2025 (May 30)；已发表于 AACL-IJCNLP 2025 ([ACL Anthology](https://aclanthology.org/2025.ijcnlp-long.90/))
- **Abstract 摘要**: 提出基于 credibility scoring 的对抗鲁棒多智能体 LLM 框架，将协作问答建模为迭代博弈，根据历史贡献学习可信度分数进行输出聚合，即使在对抗方占多数时仍有效。
- **与审稿人描述匹配**: **是** — 审稿人描述 "adversary-resistant multi-agent system" 完全准确
- **与本项目相关性**: 该论文提出的 credibility scoring 防御机制与本项目的 manipulation resistance 评估直接相关，是防御方法的关键 baseline
- **状态**: **verified** ✓

---

**总结**: 3 篇论文全部真实存在，arXiv ID、标题、作者、内容均与审稿人描述一致，无幻觉引用。

Sources:
- [arXiv:2505.13348 - Maloyan et al.](https://arxiv.org/abs/2505.13348)
- [arXiv:2511.05269 - TAMAS](https://arxiv.org/abs/2511.05269)
- [arXiv:2505.24239 - Credibility Scoring](https://arxiv.org/abs/2505.24239)
- [ACL Anthology - Ebrahimi et al.](https://aclanthology.org/2025.ijcnlp-long.90/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 56282,
  "duration_api_ms": 78156,
  "num_turns": 8,
  "stop_reason": "end_turn",
  "session_id": "b9c0bc57-ca80-4324-a332-66eb81bbb765",
  "total_cost_usd": 0.2848205,
  "usage": {
    "input_tokens": 7,
    "cache_creation_input_tokens": 17270,
    "cache_read_input_tokens": 88706,
    "output_tokens": 2021,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 17270,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 1313,
        "cache_read_input_tokens": 27886,
        "cache_creation_input_tokens": 1225,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 1225
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 40805,
      "outputTokens": 2233,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 3,
      "costUSD": 0.08197,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 7,
      "outputTokens": 2021,
      "cacheReadInputTokens": 88706,
      "cacheCreationInputTokens": 17270,
      "webSearchRequests": 0,
      "costUSD": 0.2028505,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "b0630988-1c95-483b-b366-f977dc14e70d"
}
```

</details>

---
