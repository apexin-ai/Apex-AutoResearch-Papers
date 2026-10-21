# research consistency vs correctness lit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 55
- **Recorded user turns:** 0
- **Tool calls:** 19
- **Original source:** `logs/workers/worker_research_consistency_vs_correctness_lit_20260516T220603.log`
- **Structured JSON:** [`b3374c06d88d217d88a7.json`](../../sessions/b3/b3374c06d88d217d88a7.json)

## Before a recorded user message

55 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie",
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
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
  "uuid": "73e4481e-9478-483d-b957-1050d7601211",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0514-1-projects-struct-self-consist-ie/memory/"
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
    "resetsAt": 1778978400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "5db88852-0fb6-4cea-9944-58da794a385c",
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0"
}
```

---

### Assistant

_source line 4_

我来进行文献调研，搜索 self-consistency 方法在 systematic bias 下失败的相关讨论。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "66a264b1-f9ff-4095-a592-8c049cee1059",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcQWdVtNV5ZLCvk5thYyJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12778
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_015iavf4E9iWimk7gKUDPJf5`</summary>

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
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "eab2c8c3-085d-40af-ba1d-cc92235decf9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QcQWdVtNV5ZLCvk5thYyJZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12778,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12778
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

_source line 6 · 2026-05-16T22:06:12.769Z_

<details><summary>↩ Tool result · `toolu_015iavf4E9iWimk7gKUDPJf5`</summary>

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
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "ed6be9bd-80f7-4f62-9eb2-54c49ca47c9a",
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
Let me search for literature on self-consistency failures, systematic bias, and related topics. I'll run multiple searches in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "604afe66-69fc-4660-a7c8-f0b980989d82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018A8CgxZ7oebmR3bpi8WTV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

_source line 8_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RHKqW5eEzzrAhzZWbeL5km`</summary>

```json
{
  "query": "self-consistency LLM \"systematic bias\" failure mode limitation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "16b18d0c-d536-4186-9257-9ddfe8db13ad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018A8CgxZ7oebmR3bpi8WTV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016poe2KNEeqfcRQmNHd56cy`</summary>

```json
{
  "query": "majority voting \"correlated errors\" language model bias failure"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "9656aa42-ec1f-4aa7-baa4-50efad5af944",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018A8CgxZ7oebmR3bpi8WTV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

_source line 10_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ELGMPUyFJduyA57vjoLghN`</summary>

```json
{
  "query": "Wang et al 2023 self-consistency chain of thought failure modes limitations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "cefe94ef-f162-4ec3-baad-e466d29323df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018A8CgxZ7oebmR3bpi8WTV1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 640,
      "cache_read_input_tokens": 24619,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 640
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

_source line 11 · 2026-05-16T22:06:22.926Z_

<details><summary>↩ Tool result · `toolu_01ELGMPUyFJduyA57vjoLghN`</summary>

```text
Web search results for query: "Wang et al 2023 self-consistency chain of thought failure modes limitations"

Links: [{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"Prompting extension->Self-consistency | Prompt Engineering Course, Resource and News","url":"https://egoalpha.com/paper/COT/key%20works/Self-consistency.html"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"},{"title":"Self-Consistency | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/techniques/consistency"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Self-Consistency with Chain of Thought (CoT-SC) | by Johannes Koeppern | Medium","url":"https://medium.com/@johannes.koeppern/self-consistency-with-chain-of-thought-cot-sc-2f7a1ea9f941"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/media/iclr-2023/Slides/11718.pdf"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/self-consistency.pdf"},{"title":"dblp: Self-Consistency Improves Chain of Thought Reasoning in Language Models.","url":"https://dblp.org/rec/conf/iclr/0002WSLCNCZ23.html"}]

Based on the search results, I found information about the Wang et al. 2023 paper on self-consistency in chain-of-thought reasoning. Here's what the paper proposes:

## Overview

Wang et al. propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths.

## Key Results

The paper shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

## Limitations and Failure Modes

Unfortunately, the search results primarily focus on the method's benefits rather than detailed discussions of its failure modes and limitations. While one result mentions that "the same methods also create new surfaces for failure," the specific failure modes and limitations of self-consistency are not comprehensively detailed in these search results.

To find more specific information about failure modes and limitations of the Wang et al. 2023 self-consistency approach, you may need to access the full paper directly through ArXiv (arXiv:2203.11171) or review subsequent papers that cite and critique this work.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "33ac749f-b81b-40ed-9167-1f4e02fc9986",
  "tool_use_result": {
    "query": "Wang et al 2023 self-consistency chain of thought failure modes limitations",
    "results": [
      {
        "tool_use_id": "srvtoolu_012ThHJTufQdq6oTyfLHoCax",
        "content": [
          {
            "title": "[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://arxiv.org/abs/2203.11171"
          },
          {
            "title": "[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"
          },
          {
            "title": "Prompting extension->Self-consistency | Prompt Engineering Course, Resource and News",
            "url": "https://egoalpha.com/paper/COT/key%20works/Self-consistency.html"
          },
          {
            "title": "(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"
          },
          {
            "title": "Self-Consistency | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/techniques/consistency"
          },
          {
            "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=1PL1NIMMrw"
          },
          {
            "title": "Self-Consistency with Chain of Thought (CoT-SC) | by Johannes Koeppern | Medium",
            "url": "https://medium.com/@johannes.koeppern/self-consistency-with-chain-of-thought-cot-sc-2f7a1ea9f941"
          },
          {
            "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://iclr.cc/media/iclr-2023/Slides/11718.pdf"
          },
          {
            "title": "Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/self-consistency.pdf"
          },
          {
            "title": "dblp: Self-Consistency Improves Chain of Thought Reasoning in Language Models.",
            "url": "https://dblp.org/rec/conf/iclr/0002WSLCNCZ23.html"
          }
        ]
      },
      "Based on the search results, I found information about the Wang et al. 2023 paper on self-consistency in chain-of-thought reasoning. Here's what the paper proposes:\n\n## Overview\n\nWang et al. propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths.\n\n## Key Results\n\nThe paper shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).\n\n## Limitations and Failure Modes\n\nUnfortunately, the search results primarily focus on the method's benefits rather than detailed discussions of its failure modes and limitations. While one result mentions that \"the same methods also create new surfaces for failure,\" the specific failure modes and limitations of self-consistency are not comprehensively detailed in these search results.\n\nTo find more specific information about failure modes and limitations of the Wang et al. 2023 self-consistency approach, you may need to access the full paper directly through ArXiv (arXiv:2203.11171) or review subsequent papers that cite and critique this work."
    ],
    "durationSeconds": 6.01302158
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-16T22:06:23.492Z_

<details><summary>↩ Tool result · `toolu_01RHKqW5eEzzrAhzZWbeL5km`</summary>

```text
Web search results for query: "self-consistency LLM "systematic bias" failure mode limitation"

Links: [{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/html/2411.01101"},{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.625/136156/Self-Consistency-Falls-Short-The-Adverse-Effects"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"},{"title":"LLM Behavioral Failure Modes: 12 Failure Patterns and the Defense Map","url":"https://ceaksan.com/en/llm-behavioral-failure-modes"},{"title":"Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work","url":"https://www.mdpi.com/2504-4990/8/3/74"},{"title":"LLM Inconsistency: Types, Metrics & Remedies","url":"https://www.emergentmind.com/topics/llm-inconsistency"},{"title":"Certainty robustness: Evaluating LLM stability under self-challenging prompts","url":"https://arxiv.org/html/2603.03330v1"},{"title":"Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence","url":"https://www.nature.com/articles/s42256-026-01217-9"},{"title":"Existing LLMs Are Not Self-Consistent For Simple Tasks","url":"https://arxiv.org/html/2506.18781v1"},{"title":"Self-Consistency | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/techniques/consistency"}]

Based on the search results, here's what I found about self-consistency in LLMs and its systematic bias and failure mode limitations:

## Key Findings on Self-Consistency Limitations

### Positional Bias in Long-Context Settings

Self-consistency not only fails to improve but actively degrades performance on long-context tasks. This degradation is driven by persistent position bias, which worsens with longer context lengths and smaller model sizes but remains invariant to prompt format or task type. Unlike short-context tasks, where self-consistency diversifies reasoning paths, long-context self-consistency amplifies positional errors.

### Systematic Bias Through Correlated Errors

Position bias undermines self-consistency's core assumption of error independence by inducing strongly correlated errors. Self-consistency's failures stem from correlated positional errors.

### Self-Consistent Error Masking

Self-consistency can mask model errors when all samples converge on the same incorrect output ("self-consistent errors"), and in the context of very long input contexts may actively degrade performance due to correlated, position-biased errors.

### Broader Inconsistency Issues

State-of-the-art models, including GPT-4-mini and DeepSeek R1, show improved self-consistency but do not achieve complete self-consistency. Additionally, when LLMs view their initial answers, they exhibit inflated confidence and maintain their original responses at rates exceeding optimal decision-making, even when presented with contrary evidence.

These findings reveal that self-consistency has fundamental limitations beyond simple implementation issues, particularly in handling long-context problems where its underlying assumptions break down.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "92456ff3-9bfb-4dd9-81c7-7834366a59ac",
  "tool_use_result": {
    "query": "self-consistency LLM \"systematic bias\" failure mode limitation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FGHiM2ygvE9JHJmpdgcwPz",
        "content": [
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/html/2411.01101"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.625/136156/Self-Consistency-Falls-Short-The-Adverse-Effects"
          },
          {
            "title": "Self-Consistency in Language Models",
            "url": "https://www.emergentmind.com/topics/self-consistency-in-language-models"
          },
          {
            "title": "LLM Behavioral Failure Modes: 12 Failure Patterns and the Defense Map",
            "url": "https://ceaksan.com/en/llm-behavioral-failure-modes"
          },
          {
            "title": "Towards Reliable LLM Grading Through Self-Consistency and Selective Human Review: Higher Accuracy, Less Work",
            "url": "https://www.mdpi.com/2504-4990/8/3/74"
          },
          {
            "title": "LLM Inconsistency: Types, Metrics & Remedies",
            "url": "https://www.emergentmind.com/topics/llm-inconsistency"
          },
          {
            "title": "Certainty robustness: Evaluating LLM stability under self-challenging prompts",
            "url": "https://arxiv.org/html/2603.03330v1"
          },
          {
            "title": "Competing Biases underlie Overconfidence and Underconfidence in LLMs | Nature Machine Intelligence",
            "url": "https://www.nature.com/articles/s42256-026-01217-9"
          },
          {
            "title": "Existing LLMs Are Not Self-Consistent For Simple Tasks",
            "url": "https://arxiv.org/html/2506.18781v1"
          },
          {
            "title": "Self-Consistency | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/techniques/consistency"
          }
        ]
      },
      "Based on the search results, here's what I found about self-consistency in LLMs and its systematic bias and failure mode limitations:\n\n## Key Findings on Self-Consistency Limitations\n\n### Positional Bias in Long-Context Settings\n\nSelf-consistency not only fails to improve but actively degrades performance on long-context tasks. This degradation is driven by persistent position bias, which worsens with longer context lengths and smaller model sizes but remains invariant to prompt format or task type. Unlike short-context tasks, where self-consistency diversifies reasoning paths, long-context self-consistency amplifies positional errors.\n\n### Systematic Bias Through Correlated Errors\n\nPosition bias undermines self-consistency's core assumption of error independence by inducing strongly correlated errors. Self-consistency's failures stem from correlated positional errors.\n\n### Self-Consistent Error Masking\n\nSelf-consistency can mask model errors when all samples converge on the same incorrect output (\"self-consistent errors\"), and in the context of very long input contexts may actively degrade performance due to correlated, position-biased errors.\n\n### Broader Inconsistency Issues\n\nState-of-the-art models, including GPT-4-mini and DeepSeek R1, show improved self-consistency but do not achieve complete self-consistency. Additionally, when LLMs view their initial answers, they exhibit inflated confidence and maintain their original responses at rates exceeding optimal decision-making, even when presented with contrary evidence.\n\nThese findings reveal that self-consistency has fundamental limitations beyond simple implementation issues, particularly in handling long-context problems where its underlying assumptions break down."
    ],
    "durationSeconds": 7.593479546
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-16T22:06:24.504Z_

<details><summary>↩ Tool result · `toolu_016poe2KNEeqfcRQmNHd56cy`</summary>

```text
Web search results for query: "majority voting "correlated errors" language model bias failure"

Links: [{"title":"Bias in Large Language Models: Origin, Evaluation, and Mitigation","url":"https://arxiv.org/html/2411.10915v1"},{"title":"Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2512.15146"},{"title":"Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction","url":"https://arxiv.org/html/2605.13624"},{"title":"BEYOND CONSENSUS: MITIGATING THE AGREEABLE- NESS BIAS IN LLM JUDGE EVALUATIONS","url":"https://aicet.comp.nus.edu.sg/wp-content/uploads/2025/10/Beyond-Consensus-Mitigating-the-agreeableness-bias-in-LLM-judge-evaluations.pdf"},{"title":"RETHINKING SELECTION BIAS IN LLMS","url":"https://openreview.net/pdf?id=pndOF7p9iw"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"Ithy - Enhancing Large Language Model Reliability: Majority Voting Architecture","url":"https://ithy.com/article/majority-voting-llm-architecture-c0sdzh27"},{"title":"Biases in Large Language Models: Origins, Inventory, and Discussion | Journal of Data and Information Quality","url":"https://dl.acm.org/doi/10.1145/3597307"},{"title":"Explicitly unbiased large language models still form biased ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11874501/"},{"title":"(PDF) A theoretical analysis of the limits of majority voting errors for multiple classifier systems","url":"https://www.academia.edu/2213479/A_theoretical_analysis_of_the_limits_of_majority_voting_errors_for_multiple_classifier_systems"}]

I've found relevant research on your topic. Here are the key findings:

## Correlated Errors and Majority Voting Failure

Recent research observes that naively adding more models to ensembles does not guarantee performance improvement, with scaling studies identifying diminishing or negative returns from coordination, and systematic failure analysis identifies inter-agent misalignment as a dominant failure mode in multi-agent systems—pointing to error correlation as the culprit.

Large language models are often strongly correlated, raising the question of which models should be selected when forming ensembles, and to explain why performance can saturate even with many models, researchers model the correlated errors using Gaussian-copula to show an information-theoretic error floor for ensemble performance.

## Language Model Bias and Majority Voting

Majority voting in test-time reinforcement learning represents a bottleneck because its coarse-grained estimation treats all votes equally regardless of underlying confidence, leading to confirmation bias where models risk reinforcing their own errors from incorrect label estimation, particularly when the majority consensus aligns with a plausible but incorrect answer.

Inherent biases within a model can be reinforced through majority voting, as the most frequent answers may reflect these biases, necessitating careful consideration of the model's training data and potential biases.

## Addressing the Problem

Recent work proposes SCOPE (subgroup-specific step-wise confidence-weighted pseudo-label estimation), a framework integrating model confidence and dynamic subgroup partitioning that integrates step-wise confidence into pseudo-label estimation prioritizing high-quality reasoning paths over simple frequency count, and dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "ca85ccc7-075a-4a3f-8153-c16343713c23",
  "tool_use_result": {
    "query": "majority voting \"correlated errors\" language model bias failure",
    "results": [
      {
        "tool_use_id": "srvtoolu_01375mK3ewdMVqD3uLE36b9F",
        "content": [
          {
            "title": "Bias in Large Language Models: Origin, Evaluation, and Mitigation",
            "url": "https://arxiv.org/html/2411.10915v1"
          },
          {
            "title": "Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.15146"
          },
          {
            "title": "Edit-level Majority Voting Mitigates Over-Correction in LLM-based Grammatical Error Correction",
            "url": "https://arxiv.org/html/2605.13624"
          },
          {
            "title": "BEYOND CONSENSUS: MITIGATING THE AGREEABLE- NESS BIAS IN LLM JUDGE EVALUATIONS",
            "url": "https://aicet.comp.nus.edu.sg/wp-content/uploads/2025/10/Beyond-Consensus-Mitigating-the-agreeableness-bias-in-LLM-judge-evaluations.pdf"
          },
          {
            "title": "RETHINKING SELECTION BIAS IN LLMS",
            "url": "https://openreview.net/pdf?id=pndOF7p9iw"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003"
          },
          {
            "title": "Ithy - Enhancing Large Language Model Reliability: Majority Voting Architecture",
            "url": "https://ithy.com/article/majority-voting-llm-architecture-c0sdzh27"
          },
          {
            "title": "Biases in Large Language Models: Origins, Inventory, and Discussion | Journal of Data and Information Quality",
            "url": "https://dl.acm.org/doi/10.1145/3597307"
          },
          {
            "title": "Explicitly unbiased large language models still form biased ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11874501/"
          },
          {
            "title": "(PDF) A theoretical analysis of the limits of majority voting errors for multiple classifier systems",
            "url": "https://www.academia.edu/2213479/A_theoretical_analysis_of_the_limits_of_majority_voting_errors_for_multiple_classifier_systems"
          }
        ]
      },
      "I've found relevant research on your topic. Here are the key findings:\n\n## Correlated Errors and Majority Voting Failure\n\nRecent research observes that naively adding more models to ensembles does not guarantee performance improvement, with scaling studies identifying diminishing or negative returns from coordination, and systematic failure analysis identifies inter-agent misalignment as a dominant failure mode in multi-agent systems—pointing to error correlation as the culprit.\n\nLarge language models are often strongly correlated, raising the question of which models should be selected when forming ensembles, and to explain why performance can saturate even with many models, researchers model the correlated errors using Gaussian-copula to show an information-theoretic error floor for ensemble performance.\n\n## Language Model Bias and Majority Voting\n\nMajority voting in test-time reinforcement learning represents a bottleneck because its coarse-grained estimation treats all votes equally regardless of underlying confidence, leading to confirmation bias where models risk reinforcing their own errors from incorrect label estimation, particularly when the majority consensus aligns with a plausible but incorrect answer.\n\nInherent biases within a model can be reinforced through majority voting, as the most frequent answers may reflect these biases, necessitating careful consideration of the model's training data and potential biases.\n\n## Addressing the Problem\n\nRecent work proposes SCOPE (subgroup-specific step-wise confidence-weighted pseudo-label estimation), a framework integrating model confidence and dynamic subgroup partitioning that integrates step-wise confidence into pseudo-label estimation prioritizing high-quality reasoning paths over simple frequency count, and dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity."
    ],
    "durationSeconds": 8.133802316
  }
}
```

</details>

---

### Assistant

_source line 14_

<details><summary>Logged reasoning block</summary>

```text
Good findings so far. Let me search for more specific topics - the paper about self-consistency falling short due to positional bias, and also for structured prediction / NER specific issues with self-consistency, and debiasing approaches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "a755ecac-6318-4cf3-871c-606e57fc4c8d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1qTi32MTmwaZjknS9SDN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 966,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2061
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

_source line 15_

找到了几篇重要线索。继续深入搜索。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "5526a851-285b-419e-8e34-d9104c285b0c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1qTi32MTmwaZjknS9SDN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 966,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2061
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BiwNHUWRn2Y5LrKV8LmWFw`</summary>

```json
{
  "query": "\"Self-Consistency Falls Short\" positional bias long-context 2024 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "b431376e-6fef-4d8e-884d-cdb88abbd505",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1qTi32MTmwaZjknS9SDN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 966,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2061
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_011oUqS3gtyCPVXxuNmzsq2n`</summary>

```json
{
  "query": "self-consistency NER \"structured prediction\" \"information extraction\" LLM sampling"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "d6e542d5-3d4b-4ab9-903b-5d5c98ede660",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1qTi32MTmwaZjknS9SDN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 966,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2061
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019SyR2Qdctq5ekmxSMxikLP`</summary>

```json
{
  "query": "\"beyond majority voting\" reward model test-time reinforcement learning SCOPE confidence"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "1889a2e5-a1a8-4805-b933-8b8aaeb2aafe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Y1qTi32MTmwaZjknS9SDN7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 966,
      "cache_creation_input_tokens": 2061,
      "cache_read_input_tokens": 25259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2061
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

_source line 19 · 2026-05-16T22:06:35.873Z_

<details><summary>↩ Tool result · `toolu_01BiwNHUWRn2Y5LrKV8LmWFw`</summary>

```text
Web search results for query: ""Self-Consistency Falls Short" positional bias long-context 2024 arxiv"

Links: [{"title":"[2411.01101] Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/abs/2411.01101"},{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems","url":"https://arxiv.org/html/2411.01101"},{"title":"Self-Consistency Falls Short! The Adverse Effects of ...","url":"https://arxiv.org/pdf/2411.01101"},{"title":"Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems | Transactions of the Association for Computational Linguistics | MIT Press","url":"https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.625/136156/Self-Consistency-Falls-Short-The-Adverse-Effects"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"}]

I found the paper you were searching for! Here are the key details:

## Paper Summary

**Title:** Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems

**Authors:** Adam Byerly and Daniel Khashabi

**Publication:** arXiv 2411.01101, first submitted November 2, 2024

## Main Findings

The research finds that self-consistency not only fails to improve but actively degrades performance on long-context tasks. 

In long-context tasks, systematic position biases induce correlated errors, violating self-consistency's core assumption. Unlike short-context tasks, where self-consistency diversifies reasoning paths, long-context self-consistency amplifies positional errors.

This degradation is driven by persistent position bias, which worsens with longer context lengths and smaller model sizes but remains invariant to prompt format or task type.

## Methodology

The study conducts extensive experiments across state-of-the-art models (GPT-4o, LLaMA-3.3-70B, and Qwen-2.5-72B) and their smaller variants, evaluating nine diverse long-context tasks spanning summarization, question answering, multi-hop reasoning, and controlled position experiments.

The paper is available on arXiv at https://arxiv.org/abs/2411.01101


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "59e93c20-3dbd-45d5-86fb-e75d63568fb9",
  "tool_use_result": {
    "query": "\"Self-Consistency Falls Short\" positional bias long-context 2024 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_017U6xKnKFvHMCYiUqUvncL5",
        "content": [
          {
            "title": "[2411.01101] Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/abs/2411.01101"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems",
            "url": "https://arxiv.org/html/2411.01101"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of ...",
            "url": "https://arxiv.org/pdf/2411.01101"
          },
          {
            "title": "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems | Transactions of the Association for Computational Linguistics | MIT Press",
            "url": "https://direct.mit.edu/tacl/article/doi/10.1162/TACL.a.625/136156/Self-Consistency-Falls-Short-The-Adverse-Effects"
          },
          {
            "title": "Self-Consistency in Language Models",
            "url": "https://www.emergentmind.com/topics/self-consistency-in-language-models"
          }
        ]
      },
      "I found the paper you were searching for! Here are the key details:\n\n## Paper Summary\n\n**Title:** Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\n\n**Authors:** Adam Byerly and Daniel Khashabi\n\n**Publication:** arXiv 2411.01101, first submitted November 2, 2024\n\n## Main Findings\n\nThe research finds that self-consistency not only fails to improve but actively degrades performance on long-context tasks. \n\nIn long-context tasks, systematic position biases induce correlated errors, violating self-consistency's core assumption. Unlike short-context tasks, where self-consistency diversifies reasoning paths, long-context self-consistency amplifies positional errors.\n\nThis degradation is driven by persistent position bias, which worsens with longer context lengths and smaller model sizes but remains invariant to prompt format or task type.\n\n## Methodology\n\nThe study conducts extensive experiments across state-of-the-art models (GPT-4o, LLaMA-3.3-70B, and Qwen-2.5-72B) and their smaller variants, evaluating nine diverse long-context tasks spanning summarization, question answering, multi-hop reasoning, and controlled position experiments.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2411.01101"
    ],
    "durationSeconds": 6.826901753000002
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T22:06:36.731Z_

<details><summary>↩ Tool result · `toolu_011oUqS3gtyCPVXxuNmzsq2n`</summary>

```text
Web search results for query: "self-consistency NER "structured prediction" "information extraction" LLM sampling"

Links: [{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction","url":"https://arxiv.org/html/2402.13364v1"},{"title":"Large language models for generative information extraction: a survey","url":"https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"},{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"When is the consistent prediction likely to be a correct prediction?","url":"https://arxiv.org/html/2407.05778v1"},{"title":"Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning","url":"https://arxiv.org/html/2601.02970v1"},{"title":"Structured information extraction from scientific text with large language models | Nature Communications","url":"https://www.nature.com/articles/s41467-024-45563-x"},{"title":"Statistical Network Analysis for LLMs via Knowledge Graphs","url":"https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"},{"title":"llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models","url":"https://arxiv.org/html/2406.04528v1"}]

Based on the search results, here's what I found about self-consistency, NER, structured prediction, information extraction, and LLM sampling:

## Self-Consistency Sampling with LLMs

Self-consistency involves sampling multiple answers for a question and considering the most consistent answer, as this consistent answer is more likely to be the correct answer. Self-consistency sampling and its descendants have become central to the inference and training workflows of contemporary LLMs for multi-step reasoning, relevance ranking, open-ended text, and structured data generation.

## Application to Structured Prediction and Information Extraction

Self-consistency can be combined with other strategies to further elevate LLM capabilities in various structured text generation tasks. In information extraction, LLMs make predictions on unlabeled corpus, generating self-annotated datasets through self-consistency.

## NER and Structured Information Extraction

Testing on zero-shot NER and RE (Relation Extraction), results indicate significant improvement in LLM performance with minimal additional efforts. Pretrained large language models can be fine-tuned to extract useful records of complex scientific knowledge through joint named entity recognition and relation extraction.

## Consistency in Structured Prediction

An important consideration is how consistency is measured: In structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording. Repeated sampling involves generating multiple outputs from the same prompt to assess the stability of the model's predictions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "100f1199-239e-457a-8f4a-82b1d87d9a63",
  "tool_use_result": {
    "query": "self-consistency NER \"structured prediction\" \"information extraction\" LLM sampling",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Pwq9UmbkkwDgiAu5WZyE4",
        "content": [
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "A Simple but Effective Approach to Improve Structured Language Model Output for Information Extraction",
            "url": "https://arxiv.org/html/2402.13364v1"
          },
          {
            "title": "Large language models for generative information extraction: a survey",
            "url": "https://journal.hep.com.cn/fcs/EN/10.1007/s11704-024-40555-y"
          },
          {
            "title": "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"
          },
          {
            "title": "Self-Consistency Sampling in LLMs",
            "url": "https://www.emergentmind.com/topics/self-consistency-sampling"
          },
          {
            "title": "When is the consistent prediction likely to be a correct prediction?",
            "url": "https://arxiv.org/html/2407.05778v1"
          },
          {
            "title": "Reliability-Aware Adaptive Self-Consistency for Efficient Sampling in LLM Reasoning",
            "url": "https://arxiv.org/html/2601.02970v1"
          },
          {
            "title": "Structured information extraction from scientific text with large language models | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-024-45563-x"
          },
          {
            "title": "Statistical Network Analysis for LLMs via Knowledge Graphs",
            "url": "https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"
          },
          {
            "title": "llmNER: (Zero|Few)-Shot Named Entity Recognition, Exploiting the Power of Large Language Models",
            "url": "https://arxiv.org/html/2406.04528v1"
          }
        ]
      },
      "Based on the search results, here's what I found about self-consistency, NER, structured prediction, information extraction, and LLM sampling:\n\n## Self-Consistency Sampling with LLMs\n\nSelf-consistency involves sampling multiple answers for a question and considering the most consistent answer, as this consistent answer is more likely to be the correct answer. Self-consistency sampling and its descendants have become central to the inference and training workflows of contemporary LLMs for multi-step reasoning, relevance ranking, open-ended text, and structured data generation.\n\n## Application to Structured Prediction and Information Extraction\n\nSelf-consistency can be combined with other strategies to further elevate LLM capabilities in various structured text generation tasks. In information extraction, LLMs make predictions on unlabeled corpus, generating self-annotated datasets through self-consistency.\n\n## NER and Structured Information Extraction\n\nTesting on zero-shot NER and RE (Relation Extraction), results indicate significant improvement in LLM performance with minimal additional efforts. Pretrained large language models can be fine-tuned to extract useful records of complex scientific knowledge through joint named entity recognition and relation extraction.\n\n## Consistency in Structured Prediction\n\nAn important consideration is how consistency is measured: In structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording. Repeated sampling involves generating multiple outputs from the same prompt to assess the stability of the model's predictions."
    ],
    "durationSeconds": 7.220444295000001
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-16T22:06:37.904Z_

<details><summary>↩ Tool result · `toolu_019SyR2Qdctq5ekmxSMxikLP`</summary>

```text
Web search results for query: ""beyond majority voting" reward model test-time reinforcement learning SCOPE confidence"

Links: [{"title":"Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2512.15146"},{"title":"[2512.15146] Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://arxiv.org/abs/2512.15146"},{"title":"GitHub - szu-tera/SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement","url":"https://github.com/szu-tera/SCOPE"},{"title":"(PDF) Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning","url":"https://www.researchgate.net/publication/398806159_Beyond_Majority_Voting_Towards_Fine-grained_and_More_Reliable_Reward_Signal_for_Test-Time_Reinforcement_Learning"},{"title":"Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation","url":"https://arxiv.org/html/2602.09305v1"},{"title":"GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"},{"title":"Self-Harmony: Learning to Harmonize Self-Supervision and Self-Play in Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2511.01191"},{"title":"Maximizing Confidence Alone Improves Reasoning","url":"https://arxiv.org/pdf/2505.22660"},{"title":"confidence is all you need: few-shot rl fine-tuning","url":"https://arxiv.org/pdf/2506.06395"},{"title":"Awesome-Inference-Time-Scaling/README.md at master · ThreeSR/Awesome-Inference-Time-Scaling","url":"https://github.com/ThreeSR/Awesome-Inference-Time-Scaling/blob/master/README.md"}]

I found comprehensive results about your search query. Here's what the research shows:

## SCOPE: A New Approach to Test-Time Reinforcement Learning

SCOPE (Subgroup-specific step-wise confidence-weighted pseudo-label estimation) is a framework integrating model confidence and dynamic subgroup partitioning to address issues in test-time reinforcement learning.

### Key Motivation

The traditional majority voting approach treats all votes equally regardless of their underlying confidence, leading to confirmation bias where the model risks reinforcing its own errors from incorrect label estimation, and sparse rewards since the binary nature of voting fails to capture dense, fine-grained signals.

### How SCOPE Works

SCOPE integrates step-wise confidence into pseudo-label estimation, prioritizing high-quality reasoning paths over simple frequency count. Additionally, it dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity.

### Performance Results

The framework shows strong empirical results: For Qwen2.5-Math-1.5B, SCOPE achieves an average score of 41.36, surpassing TTRL (36.95) by an absolute margin of 4.41 (+11.9%). On the challenging AIME 2024 benchmark, SCOPE boosts the performance from 16.48 to 22.50, a remarkable relative improvement of 36.5%.

The research is available on arXiv (paper 2512.15146) with code released on GitHub.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "02a39ca3-80eb-4c47-bcba-a5b95dc8aad0",
  "tool_use_result": {
    "query": "\"beyond majority voting\" reward model test-time reinforcement learning SCOPE confidence",
    "results": [
      {
        "tool_use_id": "srvtoolu_016FaXpJmC6ycpX3XLo5R9CK",
        "content": [
          {
            "title": "Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.15146"
          },
          {
            "title": "[2512.15146] Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/abs/2512.15146"
          },
          {
            "title": "GitHub - szu-tera/SCOPE: Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement",
            "url": "https://github.com/szu-tera/SCOPE"
          },
          {
            "title": "(PDF) Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning",
            "url": "https://www.researchgate.net/publication/398806159_Beyond_Majority_Voting_Towards_Fine-grained_and_More_Reliable_Reward_Signal_for_Test-Time_Reinforcement_Learning"
          },
          {
            "title": "Reward Modeling for Reinforcement Learning-Based LLM Reasoning: Design, Challenges, and Evaluation",
            "url": "https://arxiv.org/html/2602.09305v1"
          },
          {
            "title": "GitHub - ThreeSR/Awesome-Inference-Time-Scaling: Paper List of Inference/Test Time Scaling/Computing · GitHub",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling"
          },
          {
            "title": "Self-Harmony: Learning to Harmonize Self-Supervision and Self-Play in Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2511.01191"
          },
          {
            "title": "Maximizing Confidence Alone Improves Reasoning",
            "url": "https://arxiv.org/pdf/2505.22660"
          },
          {
            "title": "confidence is all you need: few-shot rl fine-tuning",
            "url": "https://arxiv.org/pdf/2506.06395"
          },
          {
            "title": "Awesome-Inference-Time-Scaling/README.md at master · ThreeSR/Awesome-Inference-Time-Scaling",
            "url": "https://github.com/ThreeSR/Awesome-Inference-Time-Scaling/blob/master/README.md"
          }
        ]
      },
      "I found comprehensive results about your search query. Here's what the research shows:\n\n## SCOPE: A New Approach to Test-Time Reinforcement Learning\n\nSCOPE (Subgroup-specific step-wise confidence-weighted pseudo-label estimation) is a framework integrating model confidence and dynamic subgroup partitioning to address issues in test-time reinforcement learning.\n\n### Key Motivation\n\nThe traditional majority voting approach treats all votes equally regardless of their underlying confidence, leading to confirmation bias where the model risks reinforcing its own errors from incorrect label estimation, and sparse rewards since the binary nature of voting fails to capture dense, fine-grained signals.\n\n### How SCOPE Works\n\nSCOPE integrates step-wise confidence into pseudo-label estimation, prioritizing high-quality reasoning paths over simple frequency count. Additionally, it dynamically partitions the candidate outputs pool into independent subgroups by balancing reasoning quality against exploration diversity.\n\n### Performance Results\n\nThe framework shows strong empirical results: For Qwen2.5-Math-1.5B, SCOPE achieves an average score of 41.36, surpassing TTRL (36.95) by an absolute margin of 4.41 (+11.9%). On the challenging AIME 2024 benchmark, SCOPE boosts the performance from 16.48 to 22.50, a remarkable relative improvement of 36.5%.\n\nThe research is available on arXiv (paper 2512.15146) with code released on GitHub."
    ],
    "durationSeconds": 7.663179595000002
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Excellent. I found two very relevant papers. Let me now search for more specific topics:

1. The "consistency-accuracy correlation" paper from PMC that was about plant-health data
2. The "When is the consistent prediction likely to be a correct prediction?" paper
3. Diverse prompting / contrastive decoding as solutions
4. Universal Self-Consistency or similar improvements
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "35ae5748-55b7-4e8c-834d-d05aa9839adf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hG8dvGqXxgxULDG81tVxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3693,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3693
      },
      "output_tokens": 24,
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

_source line 23_

非常好，找到关键论文线索。继续搜索更细分的方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "49569ce8-0b02-4a05-8d3f-aa5a9857f2e8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hG8dvGqXxgxULDG81tVxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3693,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3693
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YWUFYuEcKxLW1mLEH2cPDr`</summary>

```json
{
  "query": "\"When is the consistent prediction likely to be a correct prediction\" arxiv 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "b4e5716e-b6c8-4515-a5ac-adf21efe9765",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hG8dvGqXxgxULDG81tVxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3693,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3693
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZbvbCsb2XT2hDSSYpLfkN`</summary>

```json
{
  "query": "\"consistency accuracy correlation\" entity relation extraction plant health LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "417e3dd9-bd11-4af8-8e06-66781a7d2914",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hG8dvGqXxgxULDG81tVxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3693,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3693
      },
      "output_tokens": 24,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Hcp2PWeC9jo7oAnZnP73f2`</summary>

```json
{
  "query": "self-consistency \"diverse prompting\" debiasing \"contrastive decoding\" improve LLM systematic errors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "136c6870-161f-4e7d-a19f-f1858ad44a84",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hG8dvGqXxgxULDG81tVxx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3693,
      "cache_read_input_tokens": 27320,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3693
      },
      "output_tokens": 24,
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

_source line 27 · 2026-05-16T22:06:50.968Z_

<details><summary>↩ Tool result · `toolu_01YWUFYuEcKxLW1mLEH2cPDr`</summary>

```text
Web search results for query: ""When is the consistent prediction likely to be a correct prediction" arxiv 2024"

Links: [{"title":"[2407.05778] When is the consistent prediction likely to be a correct prediction?","url":"https://arxiv.org/abs/2407.05778"},{"title":"When is the consistent prediction likely to be a correct prediction?","url":"https://arxiv.org/html/2407.05778v1"},{"title":"When is the consistent prediction likely to be a correct prediction? - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240705778N/abstract"},{"title":"Published in Transactions on Machine Learning Research (5/2025)","url":"https://arxiv.org/pdf/2411.02454"},{"title":"Predicting Empirical AI Research Outcomes with Language Models","url":"https://arxiv.org/html/2506.00794v1"},{"title":"To model human linguistic prediction, make LLMs less superhuman","url":"https://arxiv.org/html/2510.05141"},{"title":"Published in Transactions on Machine Learning Research (07/2024)","url":"https://arxiv.org/pdf/2403.06906"},{"title":"Published as a conference paper at ICLR 2025","url":"https://arxiv.org/pdf/2502.00818"},{"title":"Another look at inference after prediction","url":"https://arxiv.org/html/2411.19908v2/"},{"title":"Introducing FOReCAst: The Future Outcome Reasoning and Confidence Assessment Benchmark","url":"https://arxiv.org/html/2502.19676v3"}]

Based on the search results, I found the arXiv paper you were looking for. Here's what it's about:

## "When is the consistent prediction likely to be a correct prediction?"

This is an arXiv paper (2407.05778) published in July 2024.

**Key Findings:**

The paper's main observation is that consistent answers derived through more computation (i.e., longer reasoning texts), rather than simply the most consistent answer across all outputs, are more likely to be correct.

The researchers demonstrate that large language models can autonomously produce chain-of-thought (CoT) style reasoning with no custom prompts merely while generating longer responses, which lead to consistent predictions that are more accurate.

**Practical Results:**

In the zero-shot setting, by sampling the Mixtral-8x7B model multiple times and considering longer responses, they achieve 86% of its self-consistency performance obtained through zero-shot CoT prompting on the GSM8K and MultiArith datasets.

**Key Challenge:**

The researchers demonstrate that the probability of LLMs generating a longer response is quite low, highlighting the need for decoding strategies conditioned on output length.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "1e99f550-9610-4eec-952c-54c4ecfe5bbc",
  "tool_use_result": {
    "query": "\"When is the consistent prediction likely to be a correct prediction\" arxiv 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_016wzrfLJUzoHZPFDtevUvAM",
        "content": [
          {
            "title": "[2407.05778] When is the consistent prediction likely to be a correct prediction?",
            "url": "https://arxiv.org/abs/2407.05778"
          },
          {
            "title": "When is the consistent prediction likely to be a correct prediction?",
            "url": "https://arxiv.org/html/2407.05778v1"
          },
          {
            "title": "When is the consistent prediction likely to be a correct prediction? - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240705778N/abstract"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (5/2025)",
            "url": "https://arxiv.org/pdf/2411.02454"
          },
          {
            "title": "Predicting Empirical AI Research Outcomes with Language Models",
            "url": "https://arxiv.org/html/2506.00794v1"
          },
          {
            "title": "To model human linguistic prediction, make LLMs less superhuman",
            "url": "https://arxiv.org/html/2510.05141"
          },
          {
            "title": "Published in Transactions on Machine Learning Research (07/2024)",
            "url": "https://arxiv.org/pdf/2403.06906"
          },
          {
            "title": "Published as a conference paper at ICLR 2025",
            "url": "https://arxiv.org/pdf/2502.00818"
          },
          {
            "title": "Another look at inference after prediction",
            "url": "https://arxiv.org/html/2411.19908v2/"
          },
          {
            "title": "Introducing FOReCAst: The Future Outcome Reasoning and Confidence Assessment Benchmark",
            "url": "https://arxiv.org/html/2502.19676v3"
          }
        ]
      },
      "Based on the search results, I found the arXiv paper you were looking for. Here's what it's about:\n\n## \"When is the consistent prediction likely to be a correct prediction?\"\n\nThis is an arXiv paper (2407.05778) published in July 2024.\n\n**Key Findings:**\n\nThe paper's main observation is that consistent answers derived through more computation (i.e., longer reasoning texts), rather than simply the most consistent answer across all outputs, are more likely to be correct.\n\nThe researchers demonstrate that large language models can autonomously produce chain-of-thought (CoT) style reasoning with no custom prompts merely while generating longer responses, which lead to consistent predictions that are more accurate.\n\n**Practical Results:**\n\nIn the zero-shot setting, by sampling the Mixtral-8x7B model multiple times and considering longer responses, they achieve 86% of its self-consistency performance obtained through zero-shot CoT prompting on the GSM8K and MultiArith datasets.\n\n**Key Challenge:**\n\nThe researchers demonstrate that the probability of LLMs generating a longer response is quite low, highlighting the need for decoding strategies conditioned on output length."
    ],
    "durationSeconds": 6.202501379999994
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T22:06:51.980Z_

<details><summary>↩ Tool result · `toolu_01QZbvbCsb2XT2hDSSYpLfkN`</summary>

```text
Web search results for query: ""consistency accuracy correlation" entity relation extraction plant health LLM"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Statistical Network Analysis for LLMs via Knowledge Graphs","url":"https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"},{"title":"Benchmarking large language models for biomedical natural language processing applications and recommendations | Nature Communications","url":"https://www.nature.com/articles/s41467-025-56989-2"},{"title":"A survey on cutting-edge relation extraction techniques based on language models","url":"https://arxiv.org/html/2411.18157v1"},{"title":"Automated identification of contextually relevant biomedical entities with grounded LLMs | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-35492-8"},{"title":"Large language models for data extraction from unstructured ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/"},{"title":"Revisiting Relation Extraction in the era of Large Language Models - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"},{"title":"Visual analysis of LLM-based entity resolution from scientific papers - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2468502X25000178"},{"title":"Revisiting Relation Extraction in the era of Large Language ...","url":"https://aclanthology.org/2023.acl-long.868.pdf"},{"title":"Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction","url":"https://arxiv.org/html/2506.17203v1"}]

Based on the search results, I found highly relevant research on your topic. Here are the key findings:

## Main Research Finding

A systematic evaluation examined the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction, using four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus—a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.

## Key Results

While some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity. More specifically, high consistency does not strongly correlate with high accuracy. Across all tested models, the correlation between consistency and accuracy was weak, suggesting that consistency alone should not be relied upon as a proxy for prediction quality in relational IE tasks.

## Consistency Definition

Consistency is defined as the stability of model outputs across repeated runs and has recently been proposed as a complementary signal of reliability. Additionally, the research distinguishes between recoverable output variations—those that preserve the meaning of the extracted information—and critical ones that result in semantic errors.

## Performance Comparison

Among the evaluated models, GPT-4o achieved the highest average accuracy and consistency scores overall.

This research provides important insights for using LLMs in plant health information extraction, suggesting that consistency metrics alone are not reliable indicators of model performance quality.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "ee6c3e29-f781-42dc-8e05-81418478892e",
  "tool_use_result": {
    "query": "\"consistency accuracy correlation\" entity relation extraction plant health LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UQfcuietL17b9Cxc5DzPgn",
        "content": [
          {
            "title": "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"
          },
          {
            "title": "Statistical Network Analysis for LLMs via Knowledge Graphs",
            "url": "https://www.techrxiv.org/users/972913/articles/1347041/master/file/data/KG__Paper%20(4)/KG__Paper%20(4).pdf?inline=true"
          },
          {
            "title": "Benchmarking large language models for biomedical natural language processing applications and recommendations | Nature Communications",
            "url": "https://www.nature.com/articles/s41467-025-56989-2"
          },
          {
            "title": "A survey on cutting-edge relation extraction techniques based on language models",
            "url": "https://arxiv.org/html/2411.18157v1"
          },
          {
            "title": "Automated identification of contextually relevant biomedical entities with grounded LLMs | Scientific Reports",
            "url": "https://www.nature.com/articles/s41598-026-35492-8"
          },
          {
            "title": "Large language models for data extraction from unstructured ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language Models - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10482322/"
          },
          {
            "title": "Visual analysis of LLM-based entity resolution from scientific papers - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S2468502X25000178"
          },
          {
            "title": "Revisiting Relation Extraction in the era of Large Language ...",
            "url": "https://aclanthology.org/2023.acl-long.868.pdf"
          },
          {
            "title": "Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction",
            "url": "https://arxiv.org/html/2506.17203v1"
          }
        ]
      },
      "Based on the search results, I found highly relevant research on your topic. Here are the key findings:\n\n## Main Research Finding\n\nA systematic evaluation examined the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction, using four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus—a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.\n\n## Key Results\n\nWhile some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity. More specifically, high consistency does not strongly correlate with high accuracy. Across all tested models, the correlation between consistency and accuracy was weak, suggesting that consistency alone should not be relied upon as a proxy for prediction quality in relational IE tasks.\n\n## Consistency Definition\n\nConsistency is defined as the stability of model outputs across repeated runs and has recently been proposed as a complementary signal of reliability. Additionally, the research distinguishes between recoverable output variations—those that preserve the meaning of the extracted information—and critical ones that result in semantic errors.\n\n## Performance Comparison\n\nAmong the evaluated models, GPT-4o achieved the highest average accuracy and consistency scores overall.\n\nThis research provides important insights for using LLMs in plant health information extraction, suggesting that consistency metrics alone are not reliable indicators of model performance quality."
    ],
    "durationSeconds": 6.729563848999998
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-16T22:06:53.643Z_

<details><summary>↩ Tool result · `toolu_01Hcp2PWeC9jo7oAnZnP73f2`</summary>

```text
Web search results for query: "self-consistency "diverse prompting" debiasing "contrastive decoding" improve LLM systematic errors"

Links: [{"title":"Internal Consistency and Self-Feedback in Large Language Models: A Survey","url":"https://arxiv.org/html/2407.14507v3"},{"title":"Self-Consistency Prompting for Robust LLM Reasoning","url":"https://www.emergentmind.com/topics/self-consistency-prompting"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"},{"title":"Self-Consistency | Prompt Engineering Guide&lt;!-- -->","url":"https://www.promptingguide.ai/techniques/consistency"},{"title":"Self-Adaptive Cognitive Debiasing for Large Language Models in Decision-Making","url":"https://arxiv.org/html/2504.04141"},{"title":"Prompt Engineering 101 — Enhancing Chain-of-Thought Reasoning with Self-Consistency | by Luis Valencia | Python in Plain English","url":"https://python.plainenglish.io/prompt-engineering-101-enhancing-chain-of-thought-reasoning-with-self-consistency-9e1136db568d?gi=6aa18931f49e"},{"title":"Debiasing Large Visual Language Models","url":"https://arxiv.org/html/2403.05262v1"},{"title":"Towards trustworthy LLMs: a review on debiasing and dehallucinating in large language models | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-024-10896-y"},{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"Self-Consistency and Universal Self-Consistency Prompting | by Dan Cleary | Medium","url":"https://medium.com/@dan_43009/self-consistency-and-universal-self-consistency-prompting-00b14f2d1992"}]

I've completed the web search for your query about self-consistency, diverse prompting, debiasing, contrastive decoding, and improving LLM systematic errors. Here are the key findings:

## Self-Consistency and Diverse Prompting

Self-consistency prompting is a sampling-based decoding methodology designed to improve the accuracy and reliability of reasoning in LLMs, most notably within the context of chain-of-thought (CoT) prompting. It samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths.

The output diversity is engineered through stochasticity in sampling, making the marginalization akin to ensembling over a model's own "thoughts," and this diversity improves reliability by reducing overfitting to any local pattern or error that a single trace might exhibit.

## Debiasing Approaches

LLMs can exhibit human-like cognitive biases despite lacking human cognitive structures, a phenomenon attributed to training on large volumes of human-generated data, which may encode biased reasoning patterns. Some approaches focus on automatic generation of counterfactual data or contrast sets, with the goal of mitigating systematic oversights.

## Contrastive Decoding

For more intricate open-ended generation tasks, debiasing methods extend to "Debias sampling", drawing inspirations from contrastive decoding methods. Contrastive optimization obtains consistency signals through the comparison between different expressions and optimizes towards consistency.

## Limitations with Self-Consistent Errors

It's worth noting that if all samples repeatedly produce the same (incorrect) answer, self-consistency-based detection methods are blind, and the incidence of such errors does not diminish with scaling and requires cross-model probing for detection.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "fac6db7b-55f3-4510-bcb5-a9aa299ffffd",
  "tool_use_result": {
    "query": "self-consistency \"diverse prompting\" debiasing \"contrastive decoding\" improve LLM systematic errors",
    "results": [
      {
        "tool_use_id": "srvtoolu_0129sAWNRxLcP8ADHDujDorp",
        "content": [
          {
            "title": "Internal Consistency and Self-Feedback in Large Language Models: A Survey",
            "url": "https://arxiv.org/html/2407.14507v3"
          },
          {
            "title": "Self-Consistency Prompting for Robust LLM Reasoning",
            "url": "https://www.emergentmind.com/topics/self-consistency-prompting"
          },
          {
            "title": "Self-Consistency in Language Models",
            "url": "https://www.emergentmind.com/topics/self-consistency-in-language-models"
          },
          {
            "title": "Self-Consistency | Prompt Engineering Guide&lt;!-- -->",
            "url": "https://www.promptingguide.ai/techniques/consistency"
          },
          {
            "title": "Self-Adaptive Cognitive Debiasing for Large Language Models in Decision-Making",
            "url": "https://arxiv.org/html/2504.04141"
          },
          {
            "title": "Prompt Engineering 101 — Enhancing Chain-of-Thought Reasoning with Self-Consistency | by Luis Valencia | Python in Plain English",
            "url": "https://python.plainenglish.io/prompt-engineering-101-enhancing-chain-of-thought-reasoning-with-self-consistency-9e1136db568d?gi=6aa18931f49e"
          },
          {
            "title": "Debiasing Large Visual Language Models",
            "url": "https://arxiv.org/html/2403.05262v1"
          },
          {
            "title": "Towards trustworthy LLMs: a review on debiasing and dehallucinating in large language models | Artificial Intelligence Review | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10462-024-10896-y"
          },
          {
            "title": "[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models",
            "url": "https://arxiv.org/abs/2203.11171"
          },
          {
            "title": "Self-Consistency and Universal Self-Consistency Prompting | by Dan Cleary | Medium",
            "url": "https://medium.com/@dan_43009/self-consistency-and-universal-self-consistency-prompting-00b14f2d1992"
          }
        ]
      },
      "I've completed the web search for your query about self-consistency, diverse prompting, debiasing, contrastive decoding, and improving LLM systematic errors. Here are the key findings:\n\n## Self-Consistency and Diverse Prompting\n\nSelf-consistency prompting is a sampling-based decoding methodology designed to improve the accuracy and reliability of reasoning in LLMs, most notably within the context of chain-of-thought (CoT) prompting. It samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths.\n\nThe output diversity is engineered through stochasticity in sampling, making the marginalization akin to ensembling over a model's own \"thoughts,\" and this diversity improves reliability by reducing overfitting to any local pattern or error that a single trace might exhibit.\n\n## Debiasing Approaches\n\nLLMs can exhibit human-like cognitive biases despite lacking human cognitive structures, a phenomenon attributed to training on large volumes of human-generated data, which may encode biased reasoning patterns. Some approaches focus on automatic generation of counterfactual data or contrast sets, with the goal of mitigating systematic oversights.\n\n## Contrastive Decoding\n\nFor more intricate open-ended generation tasks, debiasing methods extend to \"Debias sampling\", drawing inspirations from contrastive decoding methods. Contrastive optimization obtains consistency signals through the comparison between different expressions and optimizes towards consistency.\n\n## Limitations with Self-Consistent Errors\n\nIt's worth noting that if all samples repeatedly produce the same (incorrect) answer, self-consistency-based detection methods are blind, and the incidence of such errors does not diminish with scaling and requires cross-model probing for detection."
    ],
    "durationSeconds": 7.762731816
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
This is great. Let me search for a few more specific papers:
1. The "Universal Self-Consistency" paper
2. The "Internal Consistency and Self-Feedback" survey paper
3. Any work specifically on "agreement ≠ correctness" or calibration and self-consistency
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "b54879d2-1211-4abf-bd95-21ce93bffc8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2fFWuKihqfxZ5HU1yErSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 31013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2926
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

找到了非常关键的论文。再搜几个补充方向。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "cd490635-92f9-4d6b-8de6-14dc3c627563",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2fFWuKihqfxZ5HU1yErSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 31013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2926
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PvXCDiQGA5s3Yes3ZSrFsB`</summary>

```json
{
  "query": "\"universal self-consistency\" LLM free-form answers selection 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "671317aa-06bf-4a8a-afa3-5332c82f7824",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2fFWuKihqfxZ5HU1yErSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 31013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2926
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AgSJBWsZGDN2rrgUM15CzN`</summary>

```json
{
  "query": "LLM ensemble \"error correlation\" \"diversity\" voting structured output 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "7b83e6f5-1135-474b-ba83-ff25c0e6c284",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2fFWuKihqfxZ5HU1yErSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 31013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2926
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

_source line 34_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015EHhYm6QKmaxgDUgyp4fbt`</summary>

```json
{
  "query": "\"self-consistency\" calibration overconfidence \"high agreement\" wrong answer LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "3acf7394-0738-45a4-9568-15d2022ab6df",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q2fFWuKihqfxZ5HU1yErSv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2926,
      "cache_read_input_tokens": 31013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2926
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

_source line 35 · 2026-05-16T22:07:09.808Z_

<details><summary>↩ Tool result · `toolu_01PvXCDiQGA5s3Yes3ZSrFsB`</summary>

```text
Web search results for query: ""universal self-consistency" LLM free-form answers selection 2024"

Links: [{"title":"Universal Self-Consistency","url":"https://learnprompting.org/docs/advanced/ensembling/universal_self_consistency"},{"title":"Universal Self-Consistency in LLM Generation","url":"https://www.emergentmind.com/papers/2311.17311"},{"title":"Universal Self-Consistency in LLM Generation - A7AR","url":"https://a7ar.com/2024/10/09/universal-self-consistency-in-llm-generation/"},{"title":"PromptHub Blog: Self-Consistency and Universal Self-Consistency Prompting","url":"https://www.prompthub.us/blog/self-consistency-and-universal-self-consistency-prompting"},{"title":"[2311.17311] Universal Self-Consistency for Large Language Model Generation","url":"https://arxiv.org/abs/2311.17311"},{"title":"Universal Self-Consistency for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=LjsjHF7nAN"},{"title":"ICML Universal Self-Consistency for Large Language Models","url":"https://icml.cc/virtual/2024/38387"},{"title":"Self-Consistency and Universal Self-Consistency Prompting | by Dan Cleary | Medium","url":"https://medium.com/@dan_43009/self-consistency-and-universal-self-consistency-prompting-00b14f2d1992"},{"title":"Self-Consistency Sampling in LLMs","url":"https://www.emergentmind.com/topics/self-consistency-sampling"},{"title":"Achieving Greater Self-Consistency in Large Language Models | Towards Data Science","url":"https://towardsdatascience.com/achieving-greater-self-consistency-in-large-language-models-6e6cb5f3c5b7/"}]

Based on the search results, here's what I found about Universal Self-Consistency (USC) for LLM free-form answer selection:

## Overview

Universal Self-Consistency (USC) leverages LLMs themselves to select the most consistent answer among multiple candidates. USC enhances traditional self-consistency by supporting free-form answers, which is essential for tasks like summarization, open-ended Q&A, and code generation.

## How It Works

The method begins by prompting the LLM several times on the same question and recording each unique answer. Then, all responses are compiled into a new prompt, asking the LLM to select the most accurate or reasonable answer. Rather than aggregating the outputs and looking for the most popular, it concatenates all the outputs and uses an LLM to figure out which is the most consistent.

## Key Advantages

Traditional self-consistency relies on the answer extraction process to aggregate multiple solutions, which is not applicable to free-form answers. USC extends traditional self-consistency by effectively handling free-form answers, demonstrating robust improvements in tasks like mathematical reasoning and code generation, while offering computational efficiency and greater adaptability across diverse task formats.

## 2024 Evaluation

USC was presented as an ICML 2024 Workshop poster, and it was evaluated on a variety of benchmarks, including mathematical reasoning, code generation, long-context summarization, and open-ended question answering, where it effectively leverages multiple samples and improves performance on open-ended generation tasks while matching standard self-consistency performance for math reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "e68f89ce-6ce6-4e55-9999-2461b9ccb677",
  "tool_use_result": {
    "query": "\"universal self-consistency\" LLM free-form answers selection 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WN2KvpqoSUemFC5RY61VLo",
        "content": [
          {
            "title": "Universal Self-Consistency",
            "url": "https://learnprompting.org/docs/advanced/ensembling/universal_self_consistency"
          },
          {
            "title": "Universal Self-Consistency in LLM Generation",
            "url": "https://www.emergentmind.com/papers/2311.17311"
          },
          {
            "title": "Universal Self-Consistency in LLM Generation - A7AR",
            "url": "https://a7ar.com/2024/10/09/universal-self-consistency-in-llm-generation/"
          },
          {
            "title": "PromptHub Blog: Self-Consistency and Universal Self-Consistency Prompting",
            "url": "https://www.prompthub.us/blog/self-consistency-and-universal-self-consistency-prompting"
          },
          {
            "title": "[2311.17311] Universal Self-Consistency for Large Language Model Generation",
            "url": "https://arxiv.org/abs/2311.17311"
          },
          {
            "title": "Universal Self-Consistency for Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=LjsjHF7nAN"
          },
          {
            "title": "ICML Universal Self-Consistency for Large Language Models",
            "url": "https://icml.cc/virtual/2024/38387"
          },
          {
            "title": "Self-Consistency and Universal Self-Consistency Prompting | by Dan Cleary | Medium",
            "url": "https://medium.com/@dan_43009/self-consistency-and-universal-self-consistency-prompting-00b14f2d1992"
          },
          {
            "title": "Self-Consistency Sampling in LLMs",
            "url": "https://www.emergentmind.com/topics/self-consistency-sampling"
          },
          {
            "title": "Achieving Greater Self-Consistency in Large Language Models | Towards Data Science",
            "url": "https://towardsdatascience.com/achieving-greater-self-consistency-in-large-language-models-6e6cb5f3c5b7/"
          }
        ]
      },
      "Based on the search results, here's what I found about Universal Self-Consistency (USC) for LLM free-form answer selection:\n\n## Overview\n\nUniversal Self-Consistency (USC) leverages LLMs themselves to select the most consistent answer among multiple candidates. USC enhances traditional self-consistency by supporting free-form answers, which is essential for tasks like summarization, open-ended Q&A, and code generation.\n\n## How It Works\n\nThe method begins by prompting the LLM several times on the same question and recording each unique answer. Then, all responses are compiled into a new prompt, asking the LLM to select the most accurate or reasonable answer. Rather than aggregating the outputs and looking for the most popular, it concatenates all the outputs and uses an LLM to figure out which is the most consistent.\n\n## Key Advantages\n\nTraditional self-consistency relies on the answer extraction process to aggregate multiple solutions, which is not applicable to free-form answers. USC extends traditional self-consistency by effectively handling free-form answers, demonstrating robust improvements in tasks like mathematical reasoning and code generation, while offering computational efficiency and greater adaptability across diverse task formats.\n\n## 2024 Evaluation\n\nUSC was presented as an ICML 2024 Workshop poster, and it was evaluated on a variety of benchmarks, including mathematical reasoning, code generation, long-context summarization, and open-ended question answering, where it effectively leverages multiple samples and improves performance on open-ended generation tasks while matching standard self-consistency performance for math reasoning."
    ],
    "durationSeconds": 9.304855741999999
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-16T22:07:10.218Z_

<details><summary>↩ Tool result · `toolu_015EHhYm6QKmaxgDUgyp4fbt`</summary>

```text
Web search results for query: ""self-consistency" calibration overconfidence "high agreement" wrong answer LLM"

Links: [{"title":"Certainty robustness: Evaluating LLM stability under self-challenging prompts","url":"https://arxiv.org/html/2603.03330v1"},{"title":"A better method for identifying overconfident large language models | MIT News | Massachusetts Institute of Technology","url":"https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319"},{"title":"A study of calibration as a measurement of trustworthiness of large language models in biomedical natural language processing - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/"},{"title":"Self-Consistency in Language Models","url":"https://www.emergentmind.com/topics/self-consistency-in-language-models"},{"title":"Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models","url":"https://arxiv.org/html/2502.11028v1"},{"title":"A Calibrated Reflection Approach for Enhancing ...","url":"https://aclanthology.org/2025.trustnlp-main.26.pdf"},{"title":"Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers","url":"https://arxiv.org/html/2602.07842v1"},{"title":"Two Samples Are Enough: Verbal Confidence Meets Self-Consistency in Reasoning LLMs | OpenReview","url":"https://openreview.net/forum?id=66D3rZrNjV"},{"title":"Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection","url":"https://arxiv.org/html/2603.06604"},{"title":"When Can We Trust LLM Graders? Calibrating Confidence for Automated Assessment","url":"https://arxiv.org/html/2603.29559"}]

I've performed the web search on your query. Here are the key findings related to self-consistency, calibration, overconfidence, and LLM errors:

## Key Results:

**Self-Consistency and Wrong Answers:**
If all samples repeatedly produce the same (incorrect) answer, self-consistency-based detection methods are blind, and such errors do not diminish with scaling and require cross-model probing for detection.

**High Agreement Problems:**
The self-consistency method measures confidence, but even the most impressive LLM might be confidently wrong. High rates of output agreement can serve as an implicit confidence measure. However, models may display over- or under-confidence in self-assessment, with gaps between actual cross-context consistency and model self-judgments.

**Overconfidence Issues:**
Techniques like chain-of-thought reasoning and self-consistency have been explored to improve the model's self-evaluation, yet often yield overconfident estimates. LLMs tend to be overconfident: models exhibited general overconfidence in their answers when questioned.

**Self-Consistency as a Calibration Measure:**
Self-consistency was consistently more reliable than other strategies. Yet self-reported confidence consistently achieved the best calibration across all conditions compared to self-consistency voting, which remained 38% worse despite requiring 5 samples.

The research indicates that while self-consistency is a useful technique, it has fundamental limitations in detecting errors when the model consistently produces the same wrong answer with high agreement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "ae29129b-7899-4a03-898a-38868ddd6829",
  "tool_use_result": {
    "query": "\"self-consistency\" calibration overconfidence \"high agreement\" wrong answer LLM",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HDpW9QaHnf5CmdjC6S1s5i",
        "content": [
          {
            "title": "Certainty robustness: Evaluating LLM stability under self-challenging prompts",
            "url": "https://arxiv.org/html/2603.03330v1"
          },
          {
            "title": "A better method for identifying overconfident large language models | MIT News | Massachusetts Institute of Technology",
            "url": "https://news.mit.edu/2026/better-method-identifying-overconfident-large-language-models-0319"
          },
          {
            "title": "A study of calibration as a measurement of trustworthiness of large language models in biomedical natural language processing - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12249208/"
          },
          {
            "title": "Self-Consistency in Language Models",
            "url": "https://www.emergentmind.com/topics/self-consistency-in-language-models"
          },
          {
            "title": "Mind the Confidence Gap: Overconfidence, Calibration, and Distractor Effects in Large Language Models",
            "url": "https://arxiv.org/html/2502.11028v1"
          },
          {
            "title": "A Calibrated Reflection Approach for Enhancing ...",
            "url": "https://aclanthology.org/2025.trustnlp-main.26.pdf"
          },
          {
            "title": "Evaluating and Calibrating LLM Confidence on Questions with Multiple Correct Answers",
            "url": "https://arxiv.org/html/2602.07842v1"
          },
          {
            "title": "Two Samples Are Enough: Verbal Confidence Meets Self-Consistency in Reasoning LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=66D3rZrNjV"
          },
          {
            "title": "Know When You’re Wrong: Aligning Confidence with Correctness for LLM Error Detection",
            "url": "https://arxiv.org/html/2603.06604"
          },
          {
            "title": "When Can We Trust LLM Graders? Calibrating Confidence for Automated Assessment",
            "url": "https://arxiv.org/html/2603.29559"
          }
        ]
      },
      "I've performed the web search on your query. Here are the key findings related to self-consistency, calibration, overconfidence, and LLM errors:\n\n## Key Results:\n\n**Self-Consistency and Wrong Answers:**\nIf all samples repeatedly produce the same (incorrect) answer, self-consistency-based detection methods are blind, and such errors do not diminish with scaling and require cross-model probing for detection.\n\n**High Agreement Problems:**\nThe self-consistency method measures confidence, but even the most impressive LLM might be confidently wrong. High rates of output agreement can serve as an implicit confidence measure. However, models may display over- or under-confidence in self-assessment, with gaps between actual cross-context consistency and model self-judgments.\n\n**Overconfidence Issues:**\nTechniques like chain-of-thought reasoning and self-consistency have been explored to improve the model's self-evaluation, yet often yield overconfident estimates. LLMs tend to be overconfident: models exhibited general overconfidence in their answers when questioned.\n\n**Self-Consistency as a Calibration Measure:**\nSelf-consistency was consistently more reliable than other strategies. Yet self-reported confidence consistently achieved the best calibration across all conditions compared to self-consistency voting, which remained 38% worse despite requiring 5 samples.\n\nThe research indicates that while self-consistency is a useful technique, it has fundamental limitations in detecting errors when the model consistently produces the same wrong answer with high agreement."
    ],
    "durationSeconds": 8.018294155000003
  }
}
```

</details>

---

### Tool result

_source line 37 · 2026-05-16T22:07:10.521Z_

<details><summary>↩ Tool result · `toolu_01AgSJBWsZGDN2rrgUM15CzN`</summary>

```text
Web search results for query: "LLM ensemble "error correlation" "diversity" voting structured output 2024 2025"

Links: [{"title":"LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity","url":"https://aclanthology.org/2024.findings-emnlp.698.pdf"},{"title":"Majority Rules: LLM Ensemble is a Winning Approach for Content Categorization","url":"https://arxiv.org/html/2511.15714v1"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity","url":"https://arxiv.org/html/2410.03953v1"},{"title":"LLM Evaluation in 2025: Metrics, RAG, LLM-as-Judge & Best Practices | by QuarkAndCode | Medium","url":"https://medium.com/@QuarkAndCode/llm-evaluation-in-2025-metrics-rag-llm-as-judge-best-practices-ad2872cfa7cb"},{"title":"An LLM-based Multi-Agent Collaborative Approach for ...","url":"https://www.medrxiv.org/content/10.1101/2025.08.11.25333429v2.full.pdf"},{"title":"On the Effect of Sampling Diversity in Scaling LLM Inference","url":"https://arxiv.org/pdf/2502.11027"},{"title":"SLOT: Structuring the Output of Large Language Models","url":"https://aclanthology.org/2025.emnlp-industry.32.pdf"},{"title":"Unraveling the Consensus-Diversity Tradeoff in Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.772.pdf"},{"title":"A Simple Ensemble Strategy for LLM Inference: Towards More Stable Text ClassificationThis manuscript has been accepted for the 30th International Conference on Natural Language & Information Systems (NLDB 2025). The final version will appear in the Springer LNCS proceedings. Codes are available at GitHub: https://github.com/jniimi/ensemble_inference","url":"https://arxiv.org/html/2504.18884v1"}]

I've completed the web search for your query on LLM ensemble methods focusing on error correlation, diversity, and voting strategies for structured outputs in 2024-2025. Here are the key findings:

## Recent Research Highlights

**Error Correlation & Diversity Metrics:**
Error correlation has been identified as a critical issue in LLM ensembles, with recent approaches including second-order statistics for optimal weight aggregation, LLM-TOPLA's focal diversity metrics for ensemble pruning, and MUSE applying Jensen-Shannon divergence to select well-calibrated LLM subsets.

**LLM-TOPLA (2024):**
LLM-TOPLA introduces a focal diversity metric to capture the diversity-performance correlation among component LLMs and develops a diversity-optimized ensemble pruning algorithm to select top-k sub-ensembles from a pool of N base LLMs. The method generates new output for each prompt query by utilizing a learn-to-ensemble approach, which learns to detect and resolve output inconsistency among all component LLMs.

**Voting & Structured Aggregation (2025):**
Recent CDM (Collective Decision-Making) frameworks treat each LLM as a bounded rational agent and define decision criteria—such as majority, weighted consensus, or quorum-based voting—optimized for structured label spaces. These methods integrate independent model judgments under explicit aggregation rules, ensuring hierarchical validity while suppressing common error modes such as hallucination and off-ontology labeling.

**Model Selection Approach (February 2026):**
A recent study takes a fundamentally different approach by asking which models to select in the first place, providing a principled probabilistic framework based on Gaussian-copula correlation structure.

**Structured Output Methods (2025):**
The SLOT method addresses limitations by decoupling output formatting from the natural language task, offering a model-agnostic solution that maintains task performance while ensuring structural validity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "44295414-4734-4be0-9320-11a4fdf4621e",
  "tool_use_result": {
    "query": "LLM ensemble \"error correlation\" \"diversity\" voting structured output 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TGkBm1vUMK7CfQX8CFMi51",
        "content": [
          {
            "title": "LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity",
            "url": "https://aclanthology.org/2024.findings-emnlp.698.pdf"
          },
          {
            "title": "Majority Rules: LLM Ensemble is a Winning Approach for Content Categorization",
            "url": "https://arxiv.org/html/2511.15714v1"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003"
          },
          {
            "title": "LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity",
            "url": "https://arxiv.org/html/2410.03953v1"
          },
          {
            "title": "LLM Evaluation in 2025: Metrics, RAG, LLM-as-Judge & Best Practices | by QuarkAndCode | Medium",
            "url": "https://medium.com/@QuarkAndCode/llm-evaluation-in-2025-metrics-rag-llm-as-judge-best-practices-ad2872cfa7cb"
          },
          {
            "title": "An LLM-based Multi-Agent Collaborative Approach for ...",
            "url": "https://www.medrxiv.org/content/10.1101/2025.08.11.25333429v2.full.pdf"
          },
          {
            "title": "On the Effect of Sampling Diversity in Scaling LLM Inference",
            "url": "https://arxiv.org/pdf/2502.11027"
          },
          {
            "title": "SLOT: Structuring the Output of Large Language Models",
            "url": "https://aclanthology.org/2025.emnlp-industry.32.pdf"
          },
          {
            "title": "Unraveling the Consensus-Diversity Tradeoff in Adaptive ...",
            "url": "https://aclanthology.org/2025.emnlp-main.772.pdf"
          },
          {
            "title": "A Simple Ensemble Strategy for LLM Inference: Towards More Stable Text ClassificationThis manuscript has been accepted for the 30th International Conference on Natural Language & Information Systems (NLDB 2025). The final version will appear in the Springer LNCS proceedings. Codes are available at GitHub: https://github.com/jniimi/ensemble_inference",
            "url": "https://arxiv.org/html/2504.18884v1"
          }
        ]
      },
      "I've completed the web search for your query on LLM ensemble methods focusing on error correlation, diversity, and voting strategies for structured outputs in 2024-2025. Here are the key findings:\n\n## Recent Research Highlights\n\n**Error Correlation & Diversity Metrics:**\nError correlation has been identified as a critical issue in LLM ensembles, with recent approaches including second-order statistics for optimal weight aggregation, LLM-TOPLA's focal diversity metrics for ensemble pruning, and MUSE applying Jensen-Shannon divergence to select well-calibrated LLM subsets.\n\n**LLM-TOPLA (2024):**\nLLM-TOPLA introduces a focal diversity metric to capture the diversity-performance correlation among component LLMs and develops a diversity-optimized ensemble pruning algorithm to select top-k sub-ensembles from a pool of N base LLMs. The method generates new output for each prompt query by utilizing a learn-to-ensemble approach, which learns to detect and resolve output inconsistency among all component LLMs.\n\n**Voting & Structured Aggregation (2025):**\nRecent CDM (Collective Decision-Making) frameworks treat each LLM as a bounded rational agent and define decision criteria—such as majority, weighted consensus, or quorum-based voting—optimized for structured label spaces. These methods integrate independent model judgments under explicit aggregation rules, ensuring hierarchical validity while suppressing common error modes such as hallucination and off-ontology labeling.\n\n**Model Selection Approach (February 2026):**\nA recent study takes a fundamentally different approach by asking which models to select in the first place, providing a principled probabilistic framework based on Gaussian-copula correlation structure.\n\n**Structured Output Methods (2025):**\nThe SLOT method addresses limitations by decoupling output formatting from the natural language task, offering a model-agnostic solution that maintains task performance while ensuring structural validity."
    ],
    "durationSeconds": 8.990007885999999
  }
}
```

</details>

---

### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now let me get the details on the most relevant papers:

1. **"Self-Consistency Falls Short!"** (Byerly & Khashabi, 2024) - directly relevant to our finding
2. **"Consistency-accuracy correlation in hard-prompted LLMs for entity and relation extraction"** - directly relevant (NER/RE + consistency ≠ accuracy)
3. **"Beyond Majority Voting: SCOPE"** (2024) - proposes solution
4. **"Don't Always Pick the Highest-Performing Model"** - error correlation in ensembles


5. **"Unraveling the Consensus-Diversity Tradeoff"** - explores how consensus and diversity interact in model outputs

Let me dig into the specifics of these papers to understand the full landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "579ea9fb-4009-4035-bc66-5a3676343212",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hmwpEtqF3ySskcMoBeP8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 2199,
      "cache_read_input_tokens": 33939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2199
      },
      "output_tokens": 12,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fERdJVw51oumuWVRSggxA`</summary>

```json
{
  "query": "\"Unraveling the Consensus-Diversity Tradeoff\" adaptive self-consistency EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "f16936ca-e218-4030-b9b8-e279b83d9778",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hmwpEtqF3ySskcMoBeP8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 2199,
      "cache_read_input_tokens": 33939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2199
      },
      "output_tokens": 12,
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013JLKc5PDovi5tkX3935yBK`</summary>

```json
{
  "query": "\"consistency accuracy correlation\" \"hard-prompted\" LLM entity extraction EPOP authors venue year"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "437ad240-eb2d-4307-ade0-a3a9414affa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018hmwpEtqF3ySskcMoBeP8p",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 869,
      "cache_creation_input_tokens": 2199,
      "cache_read_input_tokens": 33939,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2199
      },
      "output_tokens": 12,
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

_source line 41 · 2026-05-16T22:07:25.236Z_

<details><summary>↩ Tool result · `toolu_013JLKc5PDovi5tkX3935yBK`</summary>

```text
Web search results for query: ""consistency accuracy correlation" "hard-prompted" LLM entity extraction EPOP authors venue year"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"},{"title":"Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction","url":"https://arxiv.org/html/2506.17203v1"},{"title":"Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction","url":"https://assets.amazon.science/03/bb/db4fedf948cebfd88475be8bb191/11-confidence-scoring-for-llm.pdf"},{"title":"Structured Entity Extraction Using Large Language Models","url":"https://arxiv.org/html/2402.04437v3"},{"title":"Confidence Estimation for LLM-Based Dialogue State Tracking","url":"https://arxiv.org/html/2409.09629v2"},{"title":"2025-01-16: Do Large Language Models Agree on Entity Extraction?","url":"https://ws-dl.blogspot.com/2025/01/2025-01-16-do-large-language-models.html"},{"title":"Cracking the code: Judge LLM for Entity Extraction (Part 2- No Ground Truth!) | by Albin Thomas | Medium","url":"https://medium.com/@albinthomas231/cracking-the-code-judge-llm-for-entity-extraction-part-2-no-ground-truth-b5d8e5bf3e59"},{"title":"GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub","url":"https://github.com/quqxui/Awesome-LLM4IE-Papers"},{"title":"Large language models for data extraction from unstructured ...","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/"},{"title":"Semantic Consistency for Assuring Reliability of Large Language Models","url":"https://arxiv.org/html/2308.09138"}]

Based on the search results, I found the paper you're looking for:

**Paper Title:** "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data"

**Authors:** The paper examines the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction using four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus.

**Venue/Source:** The paper is published in PMC (PubMed Central), available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/

**Year:** Based on the publication in PMC, this appears to be a recent publication (2024-2025 period based on the PMC article ID range).

**Key Focus:** The work examines the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction, conducting systematic evaluation on the EPOP corpus, a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "114af4cc-4967-45a3-acea-17ccab36810a",
  "tool_use_result": {
    "query": "\"consistency accuracy correlation\" \"hard-prompted\" LLM entity extraction EPOP authors venue year",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AsYMMc3yHiq8FKsJQujPAT",
        "content": [
          {
            "title": "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"
          },
          {
            "title": "Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction",
            "url": "https://arxiv.org/html/2506.17203v1"
          },
          {
            "title": "Confidence Scoring for LLM-Generated SQL in Supply Chain Data Extraction",
            "url": "https://assets.amazon.science/03/bb/db4fedf948cebfd88475be8bb191/11-confidence-scoring-for-llm.pdf"
          },
          {
            "title": "Structured Entity Extraction Using Large Language Models",
            "url": "https://arxiv.org/html/2402.04437v3"
          },
          {
            "title": "Confidence Estimation for LLM-Based Dialogue State Tracking",
            "url": "https://arxiv.org/html/2409.09629v2"
          },
          {
            "title": "2025-01-16: Do Large Language Models Agree on Entity Extraction?",
            "url": "https://ws-dl.blogspot.com/2025/01/2025-01-16-do-large-language-models.html"
          },
          {
            "title": "Cracking the code: Judge LLM for Entity Extraction (Part 2- No Ground Truth!) | by Albin Thomas | Medium",
            "url": "https://medium.com/@albinthomas231/cracking-the-code-judge-llm-for-entity-extraction-part-2-no-ground-truth-b5d8e5bf3e59"
          },
          {
            "title": "GitHub - quqxui/Awesome-LLM4IE-Papers: Awesome papers about generative Information Extraction (IE) using Large Language Models (LLMs) · GitHub",
            "url": "https://github.com/quqxui/Awesome-LLM4IE-Papers"
          },
          {
            "title": "Large language models for data extraction from unstructured ...",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC11751965/"
          },
          {
            "title": "Semantic Consistency for Assuring Reliability of Large Language Models",
            "url": "https://arxiv.org/html/2308.09138"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n**Paper Title:** \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\"\n\n**Authors:** The paper examines the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction using four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus.\n\n**Venue/Source:** The paper is published in PMC (PubMed Central), available at: https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n\n**Year:** Based on the publication in PMC, this appears to be a recent publication (2024-2025 period based on the PMC article ID range).\n\n**Key Focus:** The work examines the relationship between accuracy and consistency in hard-prompted generative LLMs applied to entity and relation extraction, conducting systematic evaluation on the EPOP corpus, a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints."
    ],
    "durationSeconds": 5.3818730150000045
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T22:07:26.682Z_

<details><summary>↩ Tool result · `toolu_015fERdJVw51oumuWVRSggxA`</summary>

```text
Web search results for query: ""Unraveling the Consensus-Diversity Tradeoff" adaptive self-consistency EMNLP 2025"

Links: [{"title":"The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.772/"},{"title":"Unraveling the Consensus-Diversity Tradeoff in Adaptive ...","url":"https://aclanthology.org/2025.emnlp-main.772.pdf"},{"title":"[2502.16565] The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems","url":"https://arxiv.org/abs/2502.16565"},{"title":"Enhancing LLM Reasoning via Collective Consensus","url":"https://aclanthology.org/2025.emnlp-main.574.pdf"},{"title":"Zhuosheng Zhang, Shanghai Jiao Tong University - BCMI Lab","url":"https://bcmi.sjtu.edu.cn/home/zhangzs/"},{"title":"Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest","url":"https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"},{"title":"Guided Generation for Enhanced Output Diversity in LLMs","url":"https://aclanthology.org/2025.emnlp-main.713.pdf"},{"title":"Thought Pruning for Efficient Scaling with Self-Consistency","url":"https://aclanthology.org/2025.emnlp-main.1750.pdf"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Truth Ensembles and Consensus Verification · GitHub","url":"https://gist.github.com/bigsnarfdude/21cbae2ef56c01e0f53c223b0e2ca0b1"}]

Based on the search results, I found information about the paper you're looking for:

The paper is titled "The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems" by Wu and Ito, published at EMNLP 2025 in Suzhou, China on pages 15277–15297.

## Key Findings:

The paper addresses consensus formation as pivotal in multi-agent systems (MAS), balancing collective coherence with individual diversity. The authors argue that conventional LLM-based MAS primarily rely on explicit coordination, e.g., prompts or voting, risking premature homogenization.

The paper proposes that implicit consensus, where agents exchange information yet independently form decisions via in-context learning, can be more effective in dynamic environments that require long-horizon adaptability. By retaining partial diversity, systems can better explore novel strategies and cope with external shocks, and the authors formalize a consensus-diversity tradeoff, showing conditions where implicit methods outperform explicit ones.

Experiments on three scenarios – Dynamic Disaster Response, Information Spread and Manipulation, and Dynamic Public-Goods Provision – confirm partial deviation from group norms boosts exploration, robustness, and performance.

The paper is available on the ACL Anthology and arXiv (2502.16565).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "edf49b4e-9b37-4932-9376-aa325b1c51b2",
  "tool_use_result": {
    "query": "\"Unraveling the Consensus-Diversity Tradeoff\" adaptive self-consistency EMNLP 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GEqU2Sm18pDRxfhnRSQvT8",
        "content": [
          {
            "title": "The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.772/"
          },
          {
            "title": "Unraveling the Consensus-Diversity Tradeoff in Adaptive ...",
            "url": "https://aclanthology.org/2025.emnlp-main.772.pdf"
          },
          {
            "title": "[2502.16565] The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems",
            "url": "https://arxiv.org/abs/2502.16565"
          },
          {
            "title": "Enhancing LLM Reasoning via Collective Consensus",
            "url": "https://aclanthology.org/2025.emnlp-main.574.pdf"
          },
          {
            "title": "Zhuosheng Zhang, Shanghai Jiao Tong University - BCMI Lab",
            "url": "https://bcmi.sjtu.edu.cn/home/zhangzs/"
          },
          {
            "title": "Paper Digest: EMNLP 2025 Papers & Highlights – Paper Digest",
            "url": "https://www.paperdigest.org/2025/11/emnlp-2025-papers-highlights/"
          },
          {
            "title": "Guided Generation for Enhanced Output Diversity in LLMs",
            "url": "https://aclanthology.org/2025.emnlp-main.713.pdf"
          },
          {
            "title": "Thought Pruning for Efficient Scaling with Self-Consistency",
            "url": "https://aclanthology.org/2025.emnlp-main.1750.pdf"
          },
          {
            "title": "Accepted Main Conference Papers - EMNLP 2025",
            "url": "https://2025.emnlp.org/program/main_papers/"
          },
          {
            "title": "Truth Ensembles and Consensus Verification · GitHub",
            "url": "https://gist.github.com/bigsnarfdude/21cbae2ef56c01e0f53c223b0e2ca0b1"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nThe paper is titled \"The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems\" by Wu and Ito, published at EMNLP 2025 in Suzhou, China on pages 15277–15297.\n\n## Key Findings:\n\nThe paper addresses consensus formation as pivotal in multi-agent systems (MAS), balancing collective coherence with individual diversity. The authors argue that conventional LLM-based MAS primarily rely on explicit coordination, e.g., prompts or voting, risking premature homogenization.\n\nThe paper proposes that implicit consensus, where agents exchange information yet independently form decisions via in-context learning, can be more effective in dynamic environments that require long-horizon adaptability. By retaining partial diversity, systems can better explore novel strategies and cope with external shocks, and the authors formalize a consensus-diversity tradeoff, showing conditions where implicit methods outperform explicit ones.\n\nExperiments on three scenarios – Dynamic Disaster Response, Information Spread and Manipulation, and Dynamic Public-Goods Provision – confirm partial deviation from group norms boosts exploration, robustness, and performance.\n\nThe paper is available on the ACL Anthology and arXiv (2502.16565)."
    ],
    "durationSeconds": 6.957657227000003
  }
}
```

</details>

---

### Assistant

_source line 43_

<details><summary>Logged reasoning block</summary>

```text
Let me now fetch the details of the consistency-accuracy paper and also search for any additional relevant work on structured prediction self-consistency failures.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "7951fc49-e819-407d-989f-2c214b9c537a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGtAiB4AHFqFUJbxsksAJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 36138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_012BKRsBUqyVtQzAcDbsg7Tg`</summary>

```json
{
  "query": "site:pmc.ncbi.nlm.nih.gov \"Consistency–accuracy correlation\" \"hard-prompted\" plant-health authors doi"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "659b261f-9abb-479d-994c-ff3e06302016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGtAiB4AHFqFUJbxsksAJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 36138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0186gUjKs67A4t2Tu1w8Xhpj`</summary>

```json
{
  "query": "\"sampling diversity\" scaling LLM inference test-time compute coverage diversity 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "76eefd1d-2c1d-41ce-a0b8-4ac5aa5b2629",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AGtAiB4AHFqFUJbxsksAJa",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 864,
      "cache_creation_input_tokens": 2079,
      "cache_read_input_tokens": 36138,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2079
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

_source line 46 · 2026-05-16T22:07:36.597Z_

<details><summary>↩ Tool result · `toolu_012BKRsBUqyVtQzAcDbsg7Tg`</summary>

```text
Web search results for query: "site:pmc.ncbi.nlm.nih.gov "Consistency–accuracy correlation" "hard-prompted" plant-health authors doi"

Links: [{"title":"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"}]

I found the research paper you're looking for. Here are the details:

**Title:** "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data"

**Source:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/

**Key Information:**
- The study evaluates four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus, a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.

- The results show that while some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity.

- In structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording.

The paper is published under a Creative Commons Attribution 4.0 International License. You can access the full article directly at the PMC link above.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "cfae2b75-0fef-4ce3-ac6e-72cd905552ee",
  "tool_use_result": {
    "query": "site:pmc.ncbi.nlm.nih.gov \"Consistency–accuracy correlation\" \"hard-prompted\" plant-health authors doi",
    "results": [
      {
        "tool_use_id": "srvtoolu_01SjfC29DEN5rTXLyN8sbfS5",
        "content": [
          {
            "title": "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/"
          }
        ]
      },
      "I found the research paper you're looking for. Here are the details:\n\n**Title:** \"Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data\"\n\n**Source:** https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/\n\n**Key Information:**\n- The study evaluates four LLMs (GPT, DeepSeek, Qwen, Kimi) on the EPOP corpus, a plant-health dataset with rich entity types, long-range relations, overlapping relations, and strong argument constraints.\n\n- The results show that while some positive correlation between accuracy and consistency exists, it is model-dependent and varies with task complexity.\n\n- In structured prediction tasks, consistency should be measured at the semantic level, ignoring superficial variations in format or wording.\n\nThe paper is published under a Creative Commons Attribution 4.0 International License. You can access the full article directly at the PMC link above."
    ],
    "durationSeconds": 5.945523604999995
  }
}
```

</details>

---

### Tool result

_source line 47 · 2026-05-16T22:07:39.134Z_

<details><summary>↩ Tool result · `toolu_0186gUjKs67A4t2Tu1w8Xhpj`</summary>

```text
Web search results for query: ""sampling diversity" scaling LLM inference test-time compute coverage diversity 2025"

Links: [{"title":"On the Effect of Sampling Diversity in Scaling LLM Inference","url":"https://arxiv.org/html/2502.11027v3"},{"title":"Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters","url":"https://arxiv.org/html/2408.03314v1"},{"title":"Wider or Deeper? Scaling LLM Inference-Time Compute ...","url":"https://arxiv.org/pdf/2503.04412"},{"title":"Efficient Inference-Time Scaling for Flow Models: Enhancing Sampling Diversity and Compute Allocation - MarkTechPost","url":"https://www.marktechpost.com/2025/03/29/efficient-inference-time-scaling-for-flow-models-enhancing-sampling-diversity-and-compute-allocation/"},{"title":"[2502.11027] Diversified Sampling Improves Scaling LLM inference","url":"https://ar5iv.labs.arxiv.org/html/2502.11027"},{"title":"Diversified Sampling Improves Scaling LLM inference","url":"https://arxiv.org/html/2502.11027v1"},{"title":"NeurIPS Poster Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search","url":"https://neurips.cc/virtual/2025/poster/116491"},{"title":"Published as a conference paper at ICLR 2025 INFERENCE SCALING LAWS:","url":"https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf"},{"title":"Scaling Test-time Compute for LLM Agents","url":"https://arxiv.org/pdf/2506.12928"},{"title":"Scaling LLM Inference Efficiently with Optimized Sample ...","url":"https://aclanthology.org/2025.naacl-long.404.pdf"}]

I found comprehensive research on sampling diversity and scaling LLM inference with test-time compute. Here are the key findings:

## Key Research Areas

**Sampling Diversity and Coverage:**

N sampling is a typical form of test-time scaling that aims to maximize the utility of pre-trained models by efficiently exploring multiple responses and selecting the most accurate one. However, sampling solutions from an LLM using the same prompt often leads to similar outputs, "trapped" into a local cluster.

Sampling from diversified natural language prompts can mitigate performance shortfalls in reasoning, math, and code generation tasks. Diversity strategies include Role, Instruction, and Jabberwocky perturbations, representing different styles of prompt injection to promote varied responses.

**Scaling LLM Inference Compute:**

Scaling up test-time computation can already serve to be more preferable to scaling up pretraining, with only more improvements to be attained as test-time strategies mature. As n increases, the coverage of generated answers improves.

**Advanced Inference Strategies:**

Adaptive Branching Monte Carlo Tree Search (AB-MCTS) is a novel inference-time framework that generalizes repeated sampling with principled multi-turn exploration and exploitation, dynamically deciding whether to 'go wider' by expanding new candidate responses or 'go deeper' by revisiting existing ones based on external feedback signals.

More diverse rollouts mean the agent has a greater chance of exploring and discovering the correct answer.

The research from 2025 demonstrates that leveraging sampling diversity is crucial for effective test-time scaling of LLM inference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "f80e39d7-971d-4328-b9c5-3f982e4bc1cf",
  "tool_use_result": {
    "query": "\"sampling diversity\" scaling LLM inference test-time compute coverage diversity 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_0173tAPBDhMJQaTWC553qUc4",
        "content": [
          {
            "title": "On the Effect of Sampling Diversity in Scaling LLM Inference",
            "url": "https://arxiv.org/html/2502.11027v3"
          },
          {
            "title": "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters",
            "url": "https://arxiv.org/html/2408.03314v1"
          },
          {
            "title": "Wider or Deeper? Scaling LLM Inference-Time Compute ...",
            "url": "https://arxiv.org/pdf/2503.04412"
          },
          {
            "title": "Efficient Inference-Time Scaling for Flow Models: Enhancing Sampling Diversity and Compute Allocation - MarkTechPost",
            "url": "https://www.marktechpost.com/2025/03/29/efficient-inference-time-scaling-for-flow-models-enhancing-sampling-diversity-and-compute-allocation/"
          },
          {
            "title": "[2502.11027] Diversified Sampling Improves Scaling LLM inference",
            "url": "https://ar5iv.labs.arxiv.org/html/2502.11027"
          },
          {
            "title": "Diversified Sampling Improves Scaling LLM inference",
            "url": "https://arxiv.org/html/2502.11027v1"
          },
          {
            "title": "NeurIPS Poster Wider or Deeper? Scaling LLM Inference-Time Compute with Adaptive Branching Tree Search",
            "url": "https://neurips.cc/virtual/2025/poster/116491"
          },
          {
            "title": "Published as a conference paper at ICLR 2025 INFERENCE SCALING LAWS:",
            "url": "https://proceedings.iclr.cc/paper_files/paper/2025/file/8c3caae2f725c8e2a55ecd600563d172-Paper-Conference.pdf"
          },
          {
            "title": "Scaling Test-time Compute for LLM Agents",
            "url": "https://arxiv.org/pdf/2506.12928"
          },
          {
            "title": "Scaling LLM Inference Efficiently with Optimized Sample ...",
            "url": "https://aclanthology.org/2025.naacl-long.404.pdf"
          }
        ]
      },
      "I found comprehensive research on sampling diversity and scaling LLM inference with test-time compute. Here are the key findings:\n\n## Key Research Areas\n\n**Sampling Diversity and Coverage:**\n\nN sampling is a typical form of test-time scaling that aims to maximize the utility of pre-trained models by efficiently exploring multiple responses and selecting the most accurate one. However, sampling solutions from an LLM using the same prompt often leads to similar outputs, \"trapped\" into a local cluster.\n\nSampling from diversified natural language prompts can mitigate performance shortfalls in reasoning, math, and code generation tasks. Diversity strategies include Role, Instruction, and Jabberwocky perturbations, representing different styles of prompt injection to promote varied responses.\n\n**Scaling LLM Inference Compute:**\n\nScaling up test-time computation can already serve to be more preferable to scaling up pretraining, with only more improvements to be attained as test-time strategies mature. As n increases, the coverage of generated answers improves.\n\n**Advanced Inference Strategies:**\n\nAdaptive Branching Monte Carlo Tree Search (AB-MCTS) is a novel inference-time framework that generalizes repeated sampling with principled multi-turn exploration and exploitation, dynamically deciding whether to 'go wider' by expanding new candidate responses or 'go deeper' by revisiting existing ones based on external feedback signals.\n\nMore diverse rollouts mean the agent has a greater chance of exploring and discovering the correct answer.\n\nThe research from 2025 demonstrates that leveraging sampling diversity is crucial for effective test-time scaling of LLM inference."
    ],
    "durationSeconds": 7.8549235230000045
  }
}
```

</details>

---

### Assistant

_source line 48_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough material to compile a comprehensive literature survey. Let me now use the MCP tool to save the results. But first, let me organize my findings.

Let me compile the key papers and insights:

## Most Relevant Papers

### 1. "Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems"
- **Authors**: Adam Byerly, Daniel Khashabi
- **Year**: 2024 (arXiv: 2411.01101), published in TACL


- **Venue**: Transactions of the Association for Computational Linguistics (TACL)
- **Key Insight**: Self-consistency actively *degrades* performance on long-context tasks due to systematic positional bias. Position bias induces correlated errors across samples, violating the core assumption of error independence. This directly parallels our finding: systematic bias (type semantic overlap) causes all samples to agree on the wrong answer.
- **Relation to our work**: Strongest validation. They formally show that when errors are correlated (position bias in their case, type semantic overlap in ours), self-consistency amplifies rather than corrects errors.

### 2. "Consistency–accuracy correlation in hard-prompted LLMs for entity and relation extraction: empirical findings from plant-health data"

This 2025 PMC article demonstrates that consistency doesn't necessarily track with accuracy in IE tasks—the relationship is model and task-dependent. Their findings on entity extraction directly mirror what we observed with Few-NERD.

### 3. "Beyond Majority Voting: Towards Fine-grained and More Reliable Reward Signal for Test-Time Reinforcement Learning" (SCOPE)

SCOPE addresses the problem of naive majority voting by incorporating confidence-weighted pseudo-labels and dynamic subgroup partitioning to break error correlation—a concrete approach we could apply by weighting votes by model confidence rather than treating them equally.

### 4. "Diversified Sampling Improves Scaling LLM Inference"

This work shows that sampling from the same prompt creates outputs clustered in a local region, but using diversified prompting strategies—varying roles, instructions, and perturbations—breaks this correlation and expands coverage. This directly suggests a solution: if we diversify our prompting approach, we can reduce the systematic biases causing correlated errors.

### 5. "The Hidden Strength of Disagreement: Unraveling the Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems"

Wu & Ito argue that explicit coordination through voting causes premature homogenization in multi-agent systems, while implicit consensus where agents decide independently preserves diversity and performs better in dynamic settings. This frames our problem theoretically—our structural consistency signals are explicit consensus measures that might be pushing all samples toward the same wrong answer.

### 6. "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection"

Examining ensemble selection approaches...

### 7. Wang et al. 2023 "Self-Consistency Improves Chain of Thought Reasoning in Language Models"

The self-consistency paper assumes diverse reasoning paths lead to correct answers, but doesn't address the critical failure case where systematic bias causes all paths to converge on the same incorrect answer.

Now I'm organizing these findings into a comprehensive report and saving it to the project file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "348ce348-c355-4271-bcd5-17c5d8b32cf8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJrj5PNbWzvbyh1xuVHVcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2351,
      "cache_read_input_tokens": 38217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2351
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

_source line 49_

搜索完成，下面整理结果并保存。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "f6268e1c-912e-4c54-9d1b-ef4ccda9a7fb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJrj5PNbWzvbyh1xuVHVcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2351,
      "cache_read_input_tokens": 38217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2351
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01C3sj4rgVDDMos1ChVMN8do`</summary>

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
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "0927f7e7-bf56-4c26-a958-7bcd0cd0744f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SJrj5PNbWzvbyh1xuVHVcP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2351,
      "cache_read_input_tokens": 38217,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2351
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

_source line 51 · 2026-05-16T22:08:09.057Z_

<details><summary>↩ Tool result · `toolu_01C3sj4rgVDDMos1ChVMN8do`</summary>

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
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "7e5a14da-ead8-4e15-9c03-19baeba6ad8b",
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

_source line 52_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01DEbLJiVBS733Kt4EToFoqB`</summary>

```json
{
  "project": "struct_self_consist_ie",
  "file": "memory.md",
  "content": "# 项目记忆\n\n## 文献调研：一致性 ≠ 正确性（2026-05-16）\n\n### 调研背景\nFew-NERD（8类粗粒度NER）上，结构一致性信号（SJ/FK/EM/VC）的 global ρ 为负或近零，selection delta 全为负。根因：模型存在 systematic bias（类型语义重叠 → 8 samples 一致但全错），暴露 self-consistency 的根本假设缺陷。\n\n### 最相关论文（5篇）\n\n#### 1. Self-Consistency Falls Short! The Adverse Effects of Positional Bias on Long-Context Problems\n- **Authors**: Adam Byerly, Daniel Khashabi\n- **Year/Venue**: 2024, TACL (arXiv: 2411.01101)\n- **关系**: **最强验证**。正式证明当 errors correlated 时，self-consistency 放大而非纠正错误\n- **Key insight**: 长上下文任务中，positional bias 导致所有 samples 产生相关错误，违反 self-consistency 的核心假设（error independence）。Self-consistency 不仅无效，反而 actively degrades performance。实验覆盖 GPT-4o、LLaMA-3.3-70B、Qwen-2.5-72B\n- **与我们的平行关系**: 他们的 \"positional bias → correlated errors\" 对应我们的 \"type semantic overlap → systematic misclassification\"。机制不同但失败模式完全相同\n\n#### 2. Consistency–Accuracy Correlation in Hard-Prompted LLMs for Entity and Relation Extraction\n- **Venue**: PMC (PMC12888769), 2025\n- **关系**: **IE 领域直接验证**\n- **Key insight**: 在 EPOP 语料（植物健康数据，实体+关系抽取）上测试 GPT/DeepSeek/Qwen/Kimi 四个模型，发现 high consistency does NOT strongly correlate with high accuracy。相关性是 model-dependent 且随 task complexity 变化。在 relational IE 中，consistency alone 不应被用作 prediction quality 的 proxy\n- **与我们的关系**: 直接在 IE 任务上验证了我们在 NER 上的发现——一致性不等于正确性\n\n#### 3. Beyond Majority Voting: SCOPE (Subgroup-specific Confidence-weighted Pseudo-label Estimation)\n- **Year/Venue**: 2024, arXiv: 2512.15146\n- **关系**: **提出解决方案**\n- **Key insight**: Majority voting 的问题：(1) 所有 votes 权重相同，忽略 confidence；(2) binary voting 无法捕获 fine-grained signals；(3) confirmation bias——模型强化自身错误。SCOPE 用 step-wise confidence 加权替代简单 frequency count，并通过 dynamic subgroup partitioning 平衡 quality 与 diversity\n- **可借鉴**: confidence weighting + subgroup partitioning 思路可用于我们的结构一致性信号设计\n\n#### 4. Diversified Sampling Improves Scaling LLM Inference\n- **Year**: 2025, arXiv: 2502.11027\n- **关系**: **互补——从 sampling 端解决 correlated errors**\n- **Key insight**: 同一 prompt 反复 sampling 导致输出 \"trapped\" 在 local cluster 中。通过 diversified prompts（role perturbation、instruction variation、jabberwocky perturbation）可以打破 error correlation，提升 coverage。在 reasoning/math/code 任务上显著提升\n- **可借鉴**: 如果我们在 NER 中使用多样化 prompt 策略（不同 instruction 模板、不同 few-shot examples、不同 entity type 描述），可能减少 systematic bias 导致的 correlated errors\n\n#### 5. The Hidden Strength of Disagreement: Consensus-Diversity Tradeoff in Adaptive Multi-Agent Systems\n- **Authors**: Wu & Ito\n- **Year/Venue**: 2025, EMNLP (arXiv: 2502.16565)\n- **关系**: **理论框架**\n- **Key insight**: 显式 consensus（voting/prompting）有 premature homogenization 风险。隐式 consensus（agents 独立决策但共享信息）保留了 diversity，在动态环境中优于显式 voting。形式化了 consensus-diversity tradeoff\n- **与我们的关系**: 我们的结构一致性信号是显式 consensus measure，当模型有 systematic bias 时导致 premature homogenization（全部 samples 一致地错）\n\n### 补充相关工作\n\n#### 6. Don't Always Pick the Highest-Performing Model: Information Theoretic View of LLM Ensemble Selection\n- **Year**: 2026, arXiv: 2602.08003\n- 用 Gaussian-copula 建模 correlated errors，证明 ensemble 存在 information-theoretic error floor\n\n#### 7. Wang et al. 2023 Self-Consistency (ICLR 2023, arXiv: 2203.11171)\n- 原文假设 diverse reasoning paths → correct answer 更可能被多数路径选中\n- **未显式讨论** systematic bias 导致所有路径收敛到同一错误答案的 failure mode\n\n#### 8. LLM-TOPLA: Efficient LLM Ensemble by Maximising Diversity\n- **Year/Venue**: 2024, EMNLP Findings\n- 用 focal diversity metric 选择互补性强的 ensemble 成员，减少 error correlation\n\n### 核心结论\n\n#### Q1: 有没有人正式分析过 self-consistency 在什么条件下失败？\n**有。** Byerly & Khashabi (2024, TACL) 是最系统的分析，证明 positional bias 导致 correlated errors 时 self-consistency 失败。但他们聚焦 long-context + positional bias，没有覆盖 structured prediction 中 semantic overlap 导致的 systematic bias。\n\n#### Q2: \"Correlated failures\" 如何破坏 voting-based 方法？\n多篇论文从不同角度论证：error correlation 违反了 voting 的 independence 假设。当 errors correlated，增加 samples 不能提升 accuracy（有 information-theoretic floor），甚至可能 amplify errors。\n\n#### Q3: 有没有人提出过针对 systematic bias 的改进？\n- **Confidence weighting** (SCOPE): 用 confidence 加权替代 equal voting\n- **Diversified sampling**: 用不同 prompt 变体打破 local cluster\n- **Subgroup partitioning**: 将 samples 分组，组间保持 diversity\n- **Cross-model probing**: 用不同模型交叉验证（但成本高）\n\n#### Q4: 结构化预测中 self-consistency 的特殊挑战？\nConsistency-accuracy correlation 论文（PMC12888769）在 IE 任务上直接验证了一致性≠正确性。但目前 **没有** 专门针对 NER/结构化预测中 self-consistency failure modes 的系统性研究——这是我们的 contribution gap。\n\n### 对我们下一步的启示\n\n1. **论文 framing**: 我们的发现（结构一致性在 systematic bias 下失败）有文献支撑但 **在 structured IE 领域是新的**。Byerly & Khashabi 做了 long-context，我们做 structured prediction，互补\n2. **可借鉴技术**:\n   - Confidence-weighted consistency（替代 raw agreement）\n   - Diversified prompting（不同 instruction/few-shot 模板减少 correlated errors）\n   - Adaptive stopping（当 consistency 低时增加 samples，但当 consistency 高且可能是 systematic bias 时需要 different strategy）\n3. **Discussion 要写的**: 引用 Byerly & Khashabi 说明这是 self-consistency 的 general failure mode，我们在 IE 领域首次系统性展示，并分析了结构化预测特有的原因（type semantic overlap、span boundary ambiguity）\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "244b0c10-444f-417a-ab95-a792ec164db8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf12nt8e8HugsF5bspkQFk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1545,
      "cache_read_input_tokens": 40568,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1545
      },
      "output_tokens": 45,
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

_source line 53 · 2026-05-16T22:09:02.079Z_

<details><summary>↩ Tool result · `toolu_01DEbLJiVBS733Kt4EToFoqB`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "2083d634-3aeb-42c7-982d-7e647e35c3c3",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 54_

调研完成。以下是结果摘要。

---

## 最相关论文（5篇）

**1. Self-Consistency Falls Short!** (Byerly & Khashabi, 2024, [TACL](https://arxiv.org/abs/2411.01101))
- 最强验证。证明 positional bias 导致 correlated errors 时，self-consistency 放大错误而非纠正。他们的 "position bias → correlated errors" 与我们的 "type semantic overlap → systematic misclassification" 机制不同但失败模式相同。

**2. Consistency–Accuracy Correlation in IE** (2025, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/))
- IE 领域直接验证。在 EPOP 语料（实体+关系抽取）上测 4 个 LLM，发现 **high consistency ≠ high accuracy**，相关性 model-dependent 且随 task complexity 变化。

**3. Beyond Majority Voting: SCOPE** (2024, [arXiv](https://arxiv.org/abs/2512.15146))
- 提出解决方案：用 step-wise confidence 加权替代 equal voting + dynamic subgroup partitioning 打破 error correlation。

**4. Diversified Sampling Improves Scaling LLM Inference** (2025, [arXiv](https://arxiv.org/abs/2502.11027))
- 同一 prompt 反复 sampling → outputs trapped in local cluster。用 diversified prompts 打破 correlation，提升 coverage。

**5. Hidden Strength of Disagreement** (Wu & Ito, 2025, [EMNLP](https://aclanthology.org/2025.emnlp-main.772/))
- 形式化 consensus-diversity tradeoff。显式 voting 有 premature homogenization 风险，隐式 consensus 保留 diversity 反而更优。

---

## 关键回答

**有没有人解决过 "高一致性但系统性错误"？**
有三条技术路线：(1) confidence weighting 替代 raw agreement；(2) diversified prompting 打破 error correlation；(3) subgroup partitioning 保持组间 diversity。但 **没有** 专门针对 structured IE (NER/RE) 中 self-consistency failure 的系统研究——这是我们的 contribution gap。

**对我们的启示：**
- 论文 Discussion 引用 Byerly & Khashabi 说明这是 general failure mode，我们在 IE 领域首次展示
- 可探索 confidence-weighted consistency 或 diversified prompting 作为改进方案
- 我们的 structural signals 本质上是 explicit consensus measures，当 systematic bias 存在时正好触发 premature homogenization

完整调研已保存到 `memory.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "uuid": "60f52d03-7ba0-442e-8724-b672bfaca016",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CUAN8efHz1G3p6QgroefKZ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2444,
      "cache_read_input_tokens": 42113,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2444
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

_source line 55_

调研完成。以下是结果摘要。

---

## 最相关论文（5篇）

**1. Self-Consistency Falls Short!** (Byerly & Khashabi, 2024, [TACL](https://arxiv.org/abs/2411.01101))
- 最强验证。证明 positional bias 导致 correlated errors 时，self-consistency 放大错误而非纠正。他们的 "position bias → correlated errors" 与我们的 "type semantic overlap → systematic misclassification" 机制不同但失败模式相同。

**2. Consistency–Accuracy Correlation in IE** (2025, [PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12888769/))
- IE 领域直接验证。在 EPOP 语料（实体+关系抽取）上测 4 个 LLM，发现 **high consistency ≠ high accuracy**，相关性 model-dependent 且随 task complexity 变化。

**3. Beyond Majority Voting: SCOPE** (2024, [arXiv](https://arxiv.org/abs/2512.15146))
- 提出解决方案：用 step-wise confidence 加权替代 equal voting + dynamic subgroup partitioning 打破 error correlation。

**4. Diversified Sampling Improves Scaling LLM Inference** (2025, [arXiv](https://arxiv.org/abs/2502.11027))
- 同一 prompt 反复 sampling → outputs trapped in local cluster。用 diversified prompts 打破 correlation，提升 coverage。

**5. Hidden Strength of Disagreement** (Wu & Ito, 2025, [EMNLP](https://aclanthology.org/2025.emnlp-main.772/))
- 形式化 consensus-diversity tradeoff。显式 voting 有 premature homogenization 风险，隐式 consensus 保留 diversity 反而更优。

---

## 关键回答

**有没有人解决过 "高一致性但系统性错误"？**
有三条技术路线：(1) confidence weighting 替代 raw agreement；(2) diversified prompting 打破 error correlation；(3) subgroup partitioning 保持组间 diversity。但 **没有** 专门针对 structured IE (NER/RE) 中 self-consistency failure 的系统研究——这是我们的 contribution gap。

**对我们的启示：**
- 论文 Discussion 引用 Byerly & Khashabi 说明这是 general failure mode，我们在 IE 领域首次展示
- 可探索 confidence-weighted consistency 或 diversified prompting 作为改进方案
- 我们的 structural signals 本质上是 explicit consensus measures，当 systematic bias 存在时正好触发 premature homogenization

完整调研已保存到 `memory.md`。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 190235,
  "duration_api_ms": 261859,
  "num_turns": 20,
  "stop_reason": "end_turn",
  "session_id": "06451653-9b98-467a-931a-ef6238b188f0",
  "total_cost_usd": 1.0005144999999998,
  "usage": {
    "input_tokens": 2712,
    "cache_creation_input_tokens": 32716,
    "cache_read_input_tokens": 311027,
    "output_tokens": 5957,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 32716,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 786,
        "cache_read_input_tokens": 42113,
        "cache_creation_input_tokens": 2444,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2444
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 279286,
      "outputTokens": 7751,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 16,
      "costUSD": 0.478041,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 2712,
      "outputTokens": 5957,
      "cacheReadInputTokens": 311027,
      "cacheCreationInputTokens": 32716,
      "webSearchRequests": 0,
      "costUSD": 0.5224735,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "03292756-24ce-462c-8239-9e386eadc487"
}
```

</details>

---
