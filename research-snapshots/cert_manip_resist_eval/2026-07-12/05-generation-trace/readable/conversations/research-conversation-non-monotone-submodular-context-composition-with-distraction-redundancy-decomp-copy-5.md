# Research conversation: Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition ## Core Problem How can post-retri

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-3/f988eca0-c845-4095-a440-89da68837519.jsonl`
- **Structured JSON:** [`c4f107c688acd622a701.json`](../../sessions/c4/c4f107c688acd622a701.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-30T06:49:55.677Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-30T06:49:55.677Z",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "content": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition\n\n## Core Problem\n\nHow can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?\n\n## Research Opportunity\n\nThree independently developed building blocks have converged in the past 6 months but never been combined: (1) AdaGReS (Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP. The critical insight enabling the combination is that subtracting a distraction penalty from AdaGReS's objective makes it non-monotone — invalidating AdaGReS's monotone greedy guarantees — but the resulting function may satisfy the γ-w...\n\n## Research Landscape\n\nCurrent SOTA for post-retrieval context composition splits into two disjoint camps with a verified gap between them. Camp 1 (formal guarantees, distraction-blind): AdaGReS achieves ε-approximate submodularity with adaptive β* = α·E[sim(q,x)] / ((k̄−1)/2·E[sim(x,y)]) but only models redundancy, evaluated on just 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and strict saddle/local-max dichotomy via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but has no distraction term and its authors explicitly ask whether adding a third penalty term breaks the clean quadratic landscape. Camp 2 (distraction-aware, no formal guarantees): LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization g...\n\n## Proposed Approach\n\nDefine f(S)=Σ rel(q,p) − β·Σ sim(p,p') − λ·Σ DE_q(p|S\\{p}), separating redundancy (pairwise cosine overlap) from distraction (answer-conditional interference via LLM no-response probability). Prove γ-weak DR-submodularity under bounded-embedding conditions, enabling Φ_γ approximation via AAMAS double-greedy. Compute DE_q via Qwen3-8B no-response scoring. Evaluate on NQ, ASQA, QAMPARI using Qwen3-Embedding-8B + Llama-4-Scout, against AdaGReS, CCBQP, LDAR, DynamicRAG.\n\n## Detailed Description\n\nThis work formalizes post-retrieval RAG context composition as constrained non-monotone submodular maximization with explicit distraction-redundancy decomposition. We define a set objective f(S) combining query-passage relevance, a pairwise redundancy penalty (intra-set semantic overlap), and a per-passage distraction penalty measuring answer-conditional interference via the Distracting Effect score DE_q(p). The distraction term makes f non-monotone—adding passages can decrease quality—invalidating standard greedy guarantees used by AdaGReS. Our key theoretical contribution proves f satisfies γ-weak DR-submodularity under practical bounded-embedding conditions, enabling the AAMAS 2026 Frank-Wolfe + double-greedy framework with Φ_γ > γe^{−γ} approximation guarantees. This is the first method simultaneously post-retrieval, formally grounded with provable bounds, and distraction-aware. We instantiate DE_q via LLM no-response probability and redundancy via embedding cosine similarity. Experiments on Natural Questions, ASQA, and QAMPARI using Qwen3-Embedding-8B and Llama-4-Scout compare against AdaGReS, CCBQP, LDAR, and DynamicRAG across accuracy, coverage, and token efficiency.\n\n## Key References\n\n- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)\n- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)\n- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)\n- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv Apr 2026)\n- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)\n- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)\n- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)\n- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-30T06:49:55.680Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-30T06:49:55.680Z",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-30T06:49:55.693Z_

# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition

## Core Problem

How can post-retrieval context composition for RAG be formalized as a constrained non-monotone submodular optimization problem that provably distinguishes between redundancy (intra-set semantic overlap) and distraction (answer-conditional interference) as separate penalty terms, yielding greedy approximation guarantees even when adding passages can decrease generation quality?

## Research Opportunity

Three independently developed building blocks have converged in the past 6 months but never been combined: (1) AdaGReS (Dec 2025) proved ε-approximate submodularity for redundancy-penalized context selection but only handles monotone objectives; (2) The Distracting Effect (ACL 2025) provides a concrete per-passage distraction measure DE_q(p) = 1−P(NO-RESPONSE|q,p) but performs no set-level optimization; (3) the AAMAS 2026 γ-weakly DR-submodular paper provides approximation guarantees Φ_γ for non-monotone objectives but has zero empirical applications to NLP. The critical insight enabling the combination is that subtracting a distraction penalty from AdaGReS's objective makes it non-monotone — invalidating AdaGReS's monotone greedy guarantees — but the resulting function may satisfy the γ-w...

## Research Landscape

Current SOTA for post-retrieval context composition splits into two disjoint camps with a verified gap between them. Camp 1 (formal guarantees, distraction-blind): AdaGReS achieves ε-approximate submodularity with adaptive β* = α·E[sim(q,x)] / ((k̄−1)/2·E[sim(x,y)]) but only models redundancy, evaluated on just 2 benchmarks. CCBQP (arXiv 2604.02554, Apr 2026) provides Frank-Wolfe with O(nd) iterations and strict saddle/local-max dichotomy via diagonal loading λ≥2, dominating MMR and DPP on the relevance-diversity Pareto frontier (QAMPARI/ASQA), but has no distraction term and its authors explicitly ask whether adding a third penalty term breaks the clean quadratic landscape. Camp 2 (distraction-aware, no formal guarantees): LDAR (ICLR 2026) is a distraction-aware retriever operating at retrieval time across 6 benchmarks but provides no post-retrieval composition or approximation bounds. DynamicRAG (NeurIPS 2025) uses RL with LLM feedback across 7 benchmarks but offers no optimization g...

## Proposed Approach

Define f(S)=Σ rel(q,p) − β·Σ sim(p,p') − λ·Σ DE_q(p|S\{p}), separating redundancy (pairwise cosine overlap) from distraction (answer-conditional interference via LLM no-response probability). Prove γ-weak DR-submodularity under bounded-embedding conditions, enabling Φ_γ approximation via AAMAS double-greedy. Compute DE_q via Qwen3-8B no-response scoring. Evaluate on NQ, ASQA, QAMPARI using Qwen3-Embedding-8B + Llama-4-Scout, against AdaGReS, CCBQP, LDAR, DynamicRAG.

## Detailed Description

This work formalizes post-retrieval RAG context composition as constrained non-monotone submodular maximization with explicit distraction-redundancy decomposition. We define a set objective f(S) combining query-passage relevance, a pairwise redundancy penalty (intra-set semantic overlap), and a per-passage distraction penalty measuring answer-conditional interference via the Distracting Effect score DE_q(p). The distraction term makes f non-monotone—adding passages can decrease quality—invalidating standard greedy guarantees used by AdaGReS. Our key theoretical contribution proves f satisfies γ-weak DR-submodularity under practical bounded-embedding conditions, enabling the AAMAS 2026 Frank-Wolfe + double-greedy framework with Φ_γ > γe^{−γ} approximation guarantees. This is the first method simultaneously post-retrieval, formally grounded with provable bounds, and distraction-aware. We instantiate DE_q via LLM no-response probability and redundancy via embedding cosine similarity. Experiments on Natural Questions, ASQA, and QAMPARI using Qwen3-Embedding-8B and Llama-4-Scout compare against AdaGReS, CCBQP, LDAR, and DynamicRAG across accuracy, coverage, and token efficiency.

## Key References

- AdaGReS: Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG (arXiv Dec 2025)
- The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025)
- Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization (AAMAS 2026)
- Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming (arXiv Apr 2026)
- Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding (ICLR 2026)
- DynamicRAG: Leveraging Outputs of LLM as Feedback for Dynamic Reranking in RAG (NeurIPS 2025)
- Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning (arXiv Dec 2025)
- AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop RAG (arXiv May 2026)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "128ee497-7062-4a92-9178-2c783a8364ee",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-30T06:49:55.692Z_

```json
{
  "parentUuid": "128ee497-7062-4a92-9178-2c783a8364ee",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "66bdd6ab-dd01-4c36-b344-77a5890160d2",
  "timestamp": "2026-05-30T06:49:55.692Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-30T06:49:55.693Z_

```json
{
  "parentUuid": "66bdd6ab-dd01-4c36-b344-77a5890160d2",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "259e33d8-5c07-49ff-a226-dc47ad9b7955",
  "timestamp": "2026-05-30T06:49:55.693Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Assistant

_source line 7 · 2026-05-30T06:50:02.766Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze this research proposal about "Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition" for RAG systems. 

Let me first read the proposal carefully, then do web searches to understand the current landscape before giving my assessment.

The proposal is about:
1. Formalizing post-retrieval context composition for RAG as a constrained non-monotone submodular optimization problem


2. Distinguishing between redundancy (semantic overlap within the retrieved set) and distraction (how irrelevant information interferes with answer generation)
3. Establishing theoretical guarantees through γ-weak DR-submodularity under bounded-embedding conditions
4. Applying the AAMAS 2026 double-greedy framework to achieve approximation guarantees

Now I need to search the web to understand the current state of research in this area.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "259e33d8-5c07-49ff-a226-dc47ad9b7955",
  "isSidechain": false,
  "requestId": "req_011CbYJqePxmGLprFNJrs3pz",
  "type": "assistant",
  "uuid": "1becd4e0-7804-43e6-a32d-9164f3e20730",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBBHny4h7agnryPySuymM8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5953,
      "cache_read_input_tokens": 11014,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 315,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5953
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

_source line 8 · 2026-05-30T06:50:02.769Z_

I need to do thorough pre-research before evaluating this proposal. Let me search for the key related works and the current landscape simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1becd4e0-7804-43e6-a32d-9164f3e20730",
  "isSidechain": false,
  "requestId": "req_011CbYJqePxmGLprFNJrs3pz",
  "type": "assistant",
  "uuid": "9f86abc5-a985-4a4e-829a-c60c50e58936",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBBHny4h7agnryPySuymM8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5953,
      "cache_read_input_tokens": 11014,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 315,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5953
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

_source line 9 · 2026-05-30T06:50:03.064Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01LgD8XPdnNMJghEqzF9wrRk`</summary>

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
  "parentUuid": "9f86abc5-a985-4a4e-829a-c60c50e58936",
  "isSidechain": false,
  "requestId": "req_011CbYJqePxmGLprFNJrs3pz",
  "type": "assistant",
  "uuid": "e9845f66-22d4-4bfd-90e5-a71272e8c40f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YBBHny4h7agnryPySuymM8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 5953,
      "cache_read_input_tokens": 11014,
      "output_tokens": 315,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 315,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 5953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5953
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

_source line 10 · 2026-05-30T06:50:03.072Z_

<details><summary>↩ Tool result · `toolu_01LgD8XPdnNMJghEqzF9wrRk`</summary>

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
  "parentUuid": "e9845f66-22d4-4bfd-90e5-a71272e8c40f",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "921ab190-9cf1-4643-9cc4-a244c510f008",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "e9845f66-22d4-4bfd-90e5-a71272e8c40f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-30T06:50:06.601Z_

Now let me run multiple searches in parallel to cover the key areas of this proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "921ab190-9cf1-4643-9cc4-a244c510f008",
  "isSidechain": false,
  "requestId": "req_011CbYJrCBQkSeMzRh87iWAy",
  "type": "assistant",
  "uuid": "8c42a8a0-db16-4e63-9a74-a05172c12265",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cr97EjFfUQtHTP6XKRDQJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 16967,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 16967,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 842
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

_source line 12 · 2026-05-30T06:50:07.448Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Un4v22ZQ2hjy7gmn89ep8u`</summary>

```json
{
  "query": "AdaGReS adaptive greedy context selection redundancy-aware RAG submodular 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c42a8a0-db16-4e63-9a74-a05172c12265",
  "isSidechain": false,
  "requestId": "req_011CbYJrCBQkSeMzRh87iWAy",
  "type": "assistant",
  "uuid": "47d04124-51f6-4354-948c-f96aed32afe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Cr97EjFfUQtHTP6XKRDQJm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 842,
      "cache_read_input_tokens": 16967,
      "output_tokens": 92,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 92,
          "cache_read_input_tokens": 16967,
          "cache_creation_input_tokens": 842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 842
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

_source line 13 · 2026-05-30T06:50:15.979Z_

<details><summary>↩ Tool result · `toolu_01Un4v22ZQ2hjy7gmn89ep8u`</summary>

```text
Web search results for query: "AdaGReS adaptive greedy context selection redundancy-aware RAG submodular 2025"

Links: [{"title":"[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/abs/2512.25052"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/html/2512.25052"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/html/2605.05245"}]

I found detailed information about AdaGReS. Here's what the search results reveal:

AdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. The framework performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits.

A key theoretical contribution is that the proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.

The paper addresses a practical problem in RAG systems: standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation.

Experiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.

The paper appears to be a recent 2025 publication available on arXiv (arXiv:2512.25052).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "47d04124-51f6-4354-948c-f96aed32afe5",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "3ccb440a-4584-46b9-b279-6f6735d6a764",
  "toolUseResult": {
    "query": "AdaGReS adaptive greedy context selection redundancy-aware RAG submodular 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_014u9jhD2Bi8VvBRgYZHuZ5x",
        "content": [
          {
            "title": "[2512.25052] AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/abs/2512.25052"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/html/2512.25052"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "(PDF) AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://www.researchgate.net/publication/399276683_AdaGReSAdaptive_Greedy_Context_Selection_via_Redundancy-Aware_Scoring_for_Token-Budgeted_RAG"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2605.05245"
          }
        ]
      },
      "I found detailed information about AdaGReS. Here's what the search results reveal:\n\nAdaGReS is a redundancy-aware context selection framework for token-budgeted RAG that optimizes a set-level objective combining query-chunk relevance and intra-set redundancy penalties. The framework performs greedy selection under a token-budget constraint using marginal gains derived from the objective, and introduces a closed-form, instance-adaptive calibration of the relevance-redundancy trade-off parameter to eliminate manual tuning and adapt to candidate-pool statistics and budget limits.\n\nA key theoretical contribution is that the proposed objective exhibits epsilon-approximate submodularity under practical embedding similarity conditions, yielding near-optimality guarantees for greedy selection.\n\nThe paper addresses a practical problem in RAG systems: standard top-k retrieval often returns redundant or near-duplicate chunks that waste token budget and degrade downstream generation.\n\nExperiments on open-domain question answering (Natural Questions) and a high-redundancy biomedical (drug) corpus demonstrate consistent improvements in redundancy control and context quality, translating to better end-to-end answer quality and robustness across settings.\n\nThe paper appears to be a recent 2025 publication available on arXiv (arXiv:2512.25052)."
    ],
    "durationSeconds": 8.524261602,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "47d04124-51f6-4354-948c-f96aed32afe5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-30T06:50:19.670Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LaFS6JjFkBbysVPvhtzrbb`</summary>

```json
{
  "query": "distracting effect irrelevant passages RAG ACL 2025 no-response probability"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ccb440a-4584-46b9-b279-6f6735d6a764",
  "isSidechain": false,
  "requestId": "req_011CbYJs93AzieoXWx97h4iP",
  "type": "assistant",
  "uuid": "9c2e25ed-9aa6-477a-a26a-00f69c27e48c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJ8a58S7AUa19sBJFXjeCU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 758,
      "cache_read_input_tokens": 17809,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 758,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 17809,
          "cache_creation_input_tokens": 758,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 758
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

_source line 15 · 2026-05-30T06:50:29.707Z_

<details><summary>↩ Tool result · `toolu_01LaFS6JjFkBbysVPvhtzrbb`</summary>

```text
Web search results for query: "distracting effect irrelevant passages RAG ACL 2025 no-response probability"

Links: [{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.892/"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube","url":"https://www.youtube.com/watch?v=BtLsxjA5D0A"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/html/2505.06914v1"},{"title":"The Distracting Effect: Understanding Irrelevant Passages ...","url":"https://aclanthology.org/2025.acl-long.892.pdf"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/abs/2505.06914"},{"title":"Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://huggingface.co/papers/2505.06914"},{"title":"Redefining Retrieval Evaluation in the Era of LLMs","url":"https://aclanthology.org/2026.eacl-long.391.pdf"}]

Great! I found information about this paper. Here are the search results:

The paper addresses a well-known issue with Retrieval Augmented Generation (RAG) where retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response. The researchers formulate the distracting effect of a passage with respect to a query and an LLM, and provide a quantifiable measure of the distracting effect of a passage.

The research introduces novel methods for identifying and using hard distracting passages to improve RAG systems. By fine-tuning LLMs with these carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.

The contribution is two-fold: first, they move beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, they develop and analyze multiple methods for finding hard distracting passages.

The paper proposes a continuous score to measure the distracting effect of irrelevant passages. Formally, they compute the distracting effect DEq(p) of an irrelevant passage p for question q as the probability of the LLM answer.

This paper was published at ACL 2025 by Amiraz, Cuconasu, Filice, and Karnin.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c2e25ed-9aa6-477a-a26a-00f69c27e48c",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "0be6cdfe-08b0-4ebb-ba00-6ebcd4d7d46d",
  "toolUseResult": {
    "query": "distracting effect irrelevant passages RAG ACL 2025 no-response probability",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WRjuZ9LvyVrgeNXimarqRa",
        "content": [
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG - ACL Anthology",
            "url": "https://aclanthology.org/2025.acl-long.892/"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG (ACL 2025) - YouTube",
            "url": "https://www.youtube.com/watch?v=BtLsxjA5D0A"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/html/2505.06914v1"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages ...",
            "url": "https://aclanthology.org/2025.acl-long.892.pdf"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          },
          {
            "title": "[2505.06914] The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/abs/2505.06914"
          },
          {
            "title": "Paper page - The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://huggingface.co/papers/2505.06914"
          },
          {
            "title": "Redefining Retrieval Evaluation in the Era of LLMs",
            "url": "https://aclanthology.org/2026.eacl-long.391.pdf"
          }
        ]
      },
      "Great! I found information about this paper. Here are the search results:\n\nThe paper addresses a well-known issue with Retrieval Augmented Generation (RAG) where retrieved passages that are irrelevant to the query sometimes distract the answer-generating LLM, causing it to provide an incorrect response. The researchers formulate the distracting effect of a passage with respect to a query and an LLM, and provide a quantifiable measure of the distracting effect of a passage.\n\nThe research introduces novel methods for identifying and using hard distracting passages to improve RAG systems. By fine-tuning LLMs with these carefully selected distracting passages, they achieve up to a 7.5% increase in answering accuracy compared to counterparts fine-tuned on conventional RAG datasets.\n\nThe contribution is two-fold: first, they move beyond the simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and second, they develop and analyze multiple methods for finding hard distracting passages.\n\nThe paper proposes a continuous score to measure the distracting effect of irrelevant passages. Formally, they compute the distracting effect DEq(p) of an irrelevant passage p for question q as the probability of the LLM answer.\n\nThis paper was published at ACL 2025 by Amiraz, Cuconasu, Filice, and Karnin."
    ],
    "durationSeconds": 10.032970517999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c2e25ed-9aa6-477a-a26a-00f69c27e48c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "0be6cdfe-08b0-4ebb-ba00-6ebcd4d7d46d",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Tool call

_source line 18 · 2026-05-30T06:50:32.175Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KDQPWVjiZvCqyX1MNqDjd`</summary>

```json
{
  "query": "gamma weakly DR-submodular non-monotone maximization approximation guarantees AAMAS 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0be6cdfe-08b0-4ebb-ba00-6ebcd4d7d46d",
  "isSidechain": false,
  "requestId": "req_011CbYJtARnmtYJdRmUPi3Ui",
  "type": "assistant",
  "uuid": "114a5811-255d-47a5-b470-bf10f06ea35f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013q6x4Bkuuea3o7fCXNovpk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 18567,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 805,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 18567,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 805
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

_source line 19 · 2026-05-30T06:50:39.406Z_

<details><summary>↩ Tool result · `toolu_015KDQPWVjiZvCqyX1MNqDjd`</summary>

```text
Web search results for query: "gamma weakly DR-submodular non-monotone maximization approximation guarantees AAMAS 2026"

Links: [{"title":"Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization","url":"https://arxiv.org/html/2601.00611"},{"title":"Stronger Approximation Guarantees for Non-Monotone γ-Weakly","url":"https://arxiv.org/pdf/2601.00611"},{"title":"[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization","url":"https://arxiv.org/abs/2601.00611"},{"title":"A Unified Approach for Maximizing Continuous $\\gamma$-weakly DR-submodular Functions – Optimization Online","url":"https://optimization-online.org/2024/03/a-unified-approach-for-maximizing-continuous-gamma-weakly-dr-submodular-functions/"},{"title":"Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees","url":"https://arxiv.org/pdf/1905.09595"},{"title":"Boosting Gradient Ascent for Continuous DR-submodular Maximization","url":"https://arxiv.org/pdf/2401.08330"},{"title":"Submodular Maximization Beyond Non-negativity:","url":"https://arxiv.org/pdf/1904.09354"},{"title":"Weakly Submodular Function Maximization Using Local Submodularity Ratio","url":"https://arxiv.org/pdf/2004.14650"},{"title":"[2401.08330] Boosting Gradient Ascent for Continuous DR-submodular Maximization","url":"https://arxiv.org/abs/2401.08330"}]

Based on the search results, I found relevant information about your query:

This work will be presented in part in International Conference on Autonomous Agents and Multiagent Systems (AAMAS), May 2026. The paper is titled "Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization" by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal.

The work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body, with an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) their bound recovers the 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.

The approach combines a Frank–Wolfe–guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity. γ-weakly DR-submodular objectives naturally arise when full DR-submodular models, such as continuous budget allocation, DPP-based diversity objectives, and mean-field inference for probabilistic submodular models, are augmented with practical penalties including over-exposure costs, risk or variance regularization, and intensity constraints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "114a5811-255d-47a5-b470-bf10f06ea35f",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "270f3764-7d1a-4603-b6a2-200673ce52d1",
  "toolUseResult": {
    "query": "gamma weakly DR-submodular non-monotone maximization approximation guarantees AAMAS 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PcKaCuTCYVTd6hT5HQVpAS",
        "content": [
          {
            "title": "Stronger Approximation Guarantees for Non-Monotone 𝛾-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/html/2601.00611"
          },
          {
            "title": "Stronger Approximation Guarantees for Non-Monotone γ-Weakly",
            "url": "https://arxiv.org/pdf/2601.00611"
          },
          {
            "title": "[2601.00611] Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization",
            "url": "https://arxiv.org/abs/2601.00611"
          },
          {
            "title": "A Unified Approach for Maximizing Continuous $\\gamma$-weakly DR-submodular Functions – Optimization Online",
            "url": "https://optimization-online.org/2024/03/a-unified-approach-for-maximizing-continuous-gamma-weakly-dr-submodular-functions/"
          },
          {
            "title": "Non-monotone DR-submodular Maximization: Approximation and Regret   Guarantees",
            "url": "https://arxiv.org/pdf/1905.09595"
          },
          {
            "title": "Boosting Gradient Ascent for Continuous DR-submodular Maximization",
            "url": "https://arxiv.org/pdf/2401.08330"
          },
          {
            "title": "Submodular Maximization Beyond Non-negativity:",
            "url": "https://arxiv.org/pdf/1904.09354"
          },
          {
            "title": "Weakly Submodular Function Maximization Using Local Submodularity Ratio",
            "url": "https://arxiv.org/pdf/2004.14650"
          },
          {
            "title": "[2401.08330] Boosting Gradient Ascent for Continuous DR-submodular Maximization",
            "url": "https://arxiv.org/abs/2401.08330"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nThis work will be presented in part in International Conference on Autonomous Agents and Multiagent Systems (AAMAS), May 2026. The paper is titled \"Stronger Approximation Guarantees for Non-Monotone γ-Weakly DR-Submodular Maximization\" by Hareshkumar Jadav, Ranveer Singh, and Vaneet Aggarwal.\n\nThe work studies the maximization of a nonnegative, non-monotone γ-weakly DR-submodular function over a down-closed convex body, with an approximation algorithm whose guarantee depends smoothly on γ; when γ=1 (the DR-submodular case) their bound recovers the 0.401 approximation factor, while for γ<1 the guarantee degrades gracefully and improves upon previously reported bounds.\n\nThe approach combines a Frank–Wolfe–guided continuous-greedy framework with a γ-aware double-greedy step, yielding a simple yet effective procedure for handling non-monotonicity. γ-weakly DR-submodular objectives naturally arise when full DR-submodular models, such as continuous budget allocation, DPP-based diversity objectives, and mean-field inference for probabilistic submodular models, are augmented with practical penalties including over-exposure costs, risk or variance regularization, and intensity constraints."
    ],
    "durationSeconds": 7.226983135000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "114a5811-255d-47a5-b470-bf10f06ea35f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-30T06:50:42.051Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AjduEFH67ZZqGppq9johNn`</summary>

```json
{
  "query": "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "270f3764-7d1a-4603-b6a2-200673ce52d1",
  "isSidechain": false,
  "requestId": "req_011CbYJtsGCmpKqodBMuq7tJ",
  "type": "assistant",
  "uuid": "0c57c339-0c05-4b54-8059-96e5a05a7c03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WCtSQEPP2mDYvq9wWyzGrp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 902,
      "cache_read_input_tokens": 19372,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 902,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 19372,
          "cache_creation_input_tokens": 902,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 902
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

_source line 21 · 2026-05-30T06:50:50.332Z_

<details><summary>↩ Tool result · `toolu_01AjduEFH67ZZqGppq9johNn`</summary>

```text
Web search results for query: "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026 arXiv"

Links: [{"title":"[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/abs/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/html/2604.02554"},{"title":"Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming","url":"https://arxiv.org/pdf/2604.02554"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/pdf/2604.03240"},{"title":"[2603.14744] Towards Exponential Quantum Improvements in Solving Cardinality-Constrained Binary Optimization","url":"https://arxiv.org/abs/2603.14744"}]

The search returned several relevant results. Here's what I found:

## Main Result: CCBQP for Diversity-Aware RAG Retrieval

A paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.

The work addresses diversity-aware retrieval for Retrieval-Augmented Generation (RAG), noting that existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.

**Key Technical Contributions:**

The authors develop a non-convex tight continuous relaxation and a Frank-Wolfe based algorithm with landscape analysis and convergence guarantees.

**Results:**

Extensive experiments demonstrate that the method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.

**Paper Details:**
- **Authors:** Qiheng Lu & Nicholas D. Sidiropoulos (University of Virginia)
- **arXiv ID:** 2604.02554
- **Date:** April 2, 2026

This appears to be a recent preprint that directly addresses your search query, providing a principled optimization-based approach to balancing relevance and diversity in retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0c57c339-0c05-4b54-8059-96e5a05a7c03",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "eff97a38-1009-4a4d-8720-4374b54e4e41",
  "toolUseResult": {
    "query": "CCBQP cardinality-constrained binary quadratic programming diversity retrieval RAG 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Htop29zvFjM5pGwKjvzvCc",
        "content": [
          {
            "title": "[2604.02554] Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/abs/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/html/2604.02554"
          },
          {
            "title": "Principled and Scalable Diversity-Aware Retrieval via Cardinality-Constrained Binary Quadratic Programming",
            "url": "https://arxiv.org/pdf/2604.02554"
          },
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/pdf/2604.03240"
          },
          {
            "title": "[2603.14744] Towards Exponential Quantum Improvements in Solving Cardinality-Constrained Binary Optimization",
            "url": "https://arxiv.org/abs/2603.14744"
          }
        ]
      },
      "The search returned several relevant results. Here's what I found:\n\n## Main Result: CCBQP for Diversity-Aware RAG Retrieval\n\nA paper proposes a principled formulation of diversity retrieval as a cardinality-constrained binary quadratic programming (CCBQP), which explicitly balances relevance and semantic diversity through an interpretable trade-off parameter.\n\nThe work addresses diversity-aware retrieval for Retrieval-Augmented Generation (RAG), noting that existing methods lack theoretical guarantees and face scalability issues as the number of retrieved passages increases.\n\n**Key Technical Contributions:**\n\nThe authors develop a non-convex tight continuous relaxation and a Frank-Wolfe based algorithm with landscape analysis and convergence guarantees.\n\n**Results:**\n\nExtensive experiments demonstrate that the method consistently dominates baselines on the relevance-diversity Pareto frontier, while achieving significant speedup.\n\n**Paper Details:**\n- **Authors:** Qiheng Lu & Nicholas D. Sidiropoulos (University of Virginia)\n- **arXiv ID:** 2604.02554\n- **Date:** April 2, 2026\n\nThis appears to be a recent preprint that directly addresses your search query, providing a principled optimization-based approach to balancing relevance and diversity in retrieval-augmented generation systems."
    ],
    "durationSeconds": 8.275038959000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "0c57c339-0c05-4b54-8059-96e5a05a7c03",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-30T06:50:53.862Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015ycUALkPYVV5QrcUEWWH23`</summary>

```json
{
  "query": "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding beyond RAG long context"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eff97a38-1009-4a4d-8720-4374b54e4e41",
  "isSidechain": false,
  "requestId": "req_011CbYJufvbsLzFFX6LMSygA",
  "type": "assistant",
  "uuid": "dc3a3f09-0ea6-481e-b565-f417e7df3310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012V3QR1uDYaXduxcHCqw7Tm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 691,
      "cache_read_input_tokens": 20274,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 20274,
          "cache_creation_input_tokens": 691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 691
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

_source line 23 · 2026-05-30T06:50:59.722Z_

<details><summary>↩ Tool result · `toolu_015ycUALkPYVV5QrcUEWWH23`</summary>

```text
Web search results for query: "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding beyond RAG long context"

Links: [{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding | OpenReview","url":"https://openreview.net/forum?id=c8CZWLy4T4"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"[2509.21865] Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/abs/2509.21865"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/html/2509.21865v2"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"}]

Based on the search results, I found information about your query:

## LDAR: Learning Distraction-Aware Retrieval

LDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.

### The Problem It Addresses

The research addresses a key trade-off in knowledge grounding for Large Language Models. While recent advancements in context window size allow LLMs to process inputs of up to 128K tokens or more, offering an alternative to RAG by supplying full document context directly, this strategy has notable limitations: it is token-inefficient to handle large and potentially redundant contexts, exacerbates the "lost in the middle" phenomenon, and amplifies distraction, ultimately degrading LLM output quality.

### Validation

Extensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of LDAR, highlighting the importance of balancing the trade-off between information coverage and distraction.

This work appears to be published at ICLR 2026, as indicated by the conference proceedings, and represents a significant contribution to the field of efficient knowledge grounding beyond traditional RAG and long-context approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dc3a3f09-0ea6-481e-b565-f417e7df3310",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "ae54b807-6860-4d70-b0b5-757ea5c41cd6",
  "toolUseResult": {
    "query": "LDAR distraction-aware retrieval ICLR 2026 knowledge grounding beyond RAG long context",
    "results": [
      {
        "tool_use_id": "srvtoolu_0134dMzkYT9QC4MRjxQa8J2V",
        "content": [
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding | OpenReview",
            "url": "https://openreview.net/forum?id=c8CZWLy4T4"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "[2509.21865] Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/abs/2509.21865"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/html/2509.21865v2"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          }
        ]
      },
      "Based on the search results, I found information about your query:\n\n## LDAR: Learning Distraction-Aware Retrieval\n\nLDAR (Learning Distraction-Aware Retrieval) is an adaptive retriever that learns to retrieve contexts in a way that mitigates interference from distracting passages, thereby achieving significantly higher performance with reduced token usage compared to long-context approaches.\n\n### The Problem It Addresses\n\nThe research addresses a key trade-off in knowledge grounding for Large Language Models. While recent advancements in context window size allow LLMs to process inputs of up to 128K tokens or more, offering an alternative to RAG by supplying full document context directly, this strategy has notable limitations: it is token-inefficient to handle large and potentially redundant contexts, exacerbates the \"lost in the middle\" phenomenon, and amplifies distraction, ultimately degrading LLM output quality.\n\n### Validation\n\nExtensive experiments across diverse LLM architectures and six knowledge-intensive benchmarks demonstrate the effectiveness and robustness of LDAR, highlighting the importance of balancing the trade-off between information coverage and distraction.\n\nThis work appears to be published at ICLR 2026, as indicated by the conference proceedings, and represents a significant contribution to the field of efficient knowledge grounding beyond traditional RAG and long-context approaches."
    ],
    "durationSeconds": 5.855759964999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dc3a3f09-0ea6-481e-b565-f417e7df3310",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-30T06:51:02.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TtVyip2Lsfzm7qUtRdFsb5`</summary>

```json
{
  "query": "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae54b807-6860-4d70-b0b5-757ea5c41cd6",
  "isSidechain": false,
  "requestId": "req_011CbYJvN36xPnBGLih3pFpF",
  "type": "assistant",
  "uuid": "f186a654-8fc2-453c-bbe8-e0208b685005",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016RfSsQUgbbBexbEPDAqgH7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 676,
      "cache_read_input_tokens": 20965,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 676,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 20965,
          "cache_creation_input_tokens": 676,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 676
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

_source line 25 · 2026-05-30T06:51:10.926Z_

<details><summary>↩ Tool result · `toolu_01TtVyip2Lsfzm7qUtRdFsb5`</summary>

```text
Web search results for query: "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025"

Links: [{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | OpenReview","url":"https://openreview.net/forum?id=NuCtKoflsV"},{"title":"GitHub - GasolSun36/DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation · GitHub","url":"https://github.com/GasolSun36/DynamicRAG"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/html/2505.07233v2"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2505.07233"},{"title":"[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2505.07233"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | Space Frontiers","url":"https://spacefrontiers.org/r/10.48550/arxiv.2505.07233"},{"title":"DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250507233S/abstract"},{"title":"NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://neurips.cc/virtual/2025/poster/118330"},{"title":"Paper page - DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation","url":"https://huggingface.co/papers/2505.07233"}]

The search found comprehensive information about DynamicRAG. Here are the key findings:

## Overview
DynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, using reinforcement learning to adaptively rerank documents based on LLM's responses as feedback.

## Key Technical Approach
The reranker dynamically adjusts both the order and number of retrieved documents based on the query, and is modeled as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality.

## Problem it Addresses
The challenge of selecting the optimal number of documents (k) remains unsolved: too few may omit critical information, while too many introduce noise and inefficiencies. Although recent studies have explored LLM-based rerankers, they primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.

## Performance and Publication
Across seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results. The paper was accepted by NeurIPS 2025.

## Availability
The model, data and code are available at https://github.com/GasolSun36/DynamicRAG.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f186a654-8fc2-453c-bbe8-e0208b685005",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "dfb27623-e8b3-48f6-9506-14e0715ae02c",
  "toolUseResult": {
    "query": "DynamicRAG LLM feedback dynamic reranking NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_013Trvy64PD59V72kHExQBue",
        "content": [
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | OpenReview",
            "url": "https://openreview.net/forum?id=NuCtKoflsV"
          },
          {
            "title": "GitHub - GasolSun36/DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation · GitHub",
            "url": "https://github.com/GasolSun36/DynamicRAG"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2505.07233v2"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.07233"
          },
          {
            "title": "[2505.07233] DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2505.07233"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation | Space Frontiers",
            "url": "https://spacefrontiers.org/r/10.48550/arxiv.2505.07233"
          },
          {
            "title": "DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2025arXiv250507233S/abstract"
          },
          {
            "title": "NeurIPS Poster DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://neurips.cc/virtual/2025/poster/118330"
          },
          {
            "title": "Paper page - DynamicRAG: Leveraging Outputs of Large Language Model as Feedback for Dynamic Reranking in Retrieval-Augmented Generation",
            "url": "https://huggingface.co/papers/2505.07233"
          }
        ]
      },
      "The search found comprehensive information about DynamicRAG. Here are the key findings:\n\n## Overview\nDynamicRAG is a novel RAG framework where the reranker dynamically adjusts both the order and number of retrieved documents based on the query, using reinforcement learning to adaptively rerank documents based on LLM's responses as feedback.\n\n## Key Technical Approach\nThe reranker dynamically adjusts both the order and number of retrieved documents based on the query, and is modeled as an agent optimized through reinforcement learning (RL), using rewards derived from LLM output quality.\n\n## Problem it Addresses\nThe challenge of selecting the optimal number of documents (k) remains unsolved: too few may omit critical information, while too many introduce noise and inefficiencies. Although recent studies have explored LLM-based rerankers, they primarily leverage internal model knowledge and overlook the rich supervisory signals that LLMs can provide, such as using response quality as feedback for optimizing reranking decisions.\n\n## Performance and Publication\nAcross seven knowledge-intensive datasets, DynamicRAG demonstrates superior performance, achieving state-of-the-art results. The paper was accepted by NeurIPS 2025.\n\n## Availability\nThe model, data and code are available at https://github.com/GasolSun36/DynamicRAG."
    ],
    "durationSeconds": 8.43330608600001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f186a654-8fc2-453c-bbe8-e0208b685005",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-30T06:51:13.375Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DXfGTPsGJxupxfQuFr1boP`</summary>

```json
{
  "query": "post-retrieval context selection RAG submodular optimization 2026 recent work"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfb27623-e8b3-48f6-9506-14e0715ae02c",
  "isSidechain": false,
  "requestId": "req_011CbYJwBxuHwDfTahnoo4K9",
  "type": "assistant",
  "uuid": "63a881e4-25b7-4830-a7e5-100b633ad33f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DH68ipk2AkiETtPN2zzLEL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1000,
      "cache_read_input_tokens": 21641,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1000,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 21641,
          "cache_creation_input_tokens": 1000,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1000
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

_source line 27 · 2026-05-30T06:51:22.072Z_

<details><summary>↩ Tool result · `toolu_01DXfGTPsGJxupxfQuFr1boP`</summary>

```text
Web search results for query: "post-retrieval context selection RAG submodular optimization 2026 recent work"

Links: [{"title":"RAG Techniques Compared: A Practical Guide to Retrieval Augmented Generation in 2026","url":"https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI","url":"https://www.techment.com/blogs/rag-in-2026/"},{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval","url":"https://arxiv.org/pdf/2409.13992"},{"title":"Retrieval-Augmented Generation as In-Context Optimization: A Gradient Descent Perspective | OpenReview","url":"https://openreview.net/forum?id=fz1WJWeITf"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"},{"title":"Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach","url":"https://arxiv.org/pdf/2603.20286"}]

Based on the search results, I found recent work on post-retrieval context selection in RAG systems with connections to optimization approaches:

## Key Recent Work (2025-2026)

**AdaGReS: Adaptive Greedy Context Selection with Submodular Optimization**

A recent paper provides theoretical analysis and proof of ε-approximate submodularity for a context selection objective, offering theoretical guarantees for the near-global optimality of the greedy selection algorithm. This work addresses the challenge that retrieved results need to exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval, especially when documents are chunked densely or the corpus is highly redundant.

**SMART-RAG: Determinantal Point Process Selection**

SMART (Selection using Matrices for Augmented ReTrieval) is a fully unsupervised and training-free framework designed to optimize context selection in RAG that leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict.

**Context Merging Approaches**

RAG is constrained by the LLM's context window, and the standard practice adopts a retrieve-then-select paradigm, typically retaining only the top-k chunks based on semantic similarity scores. However, this greedy selection approach suffers from information loss and introduces significant semantic redundancy.

These recent works in 2025-2026 focus on balancing relevance and diversity in post-retrieval context selection, with submodular optimization serving as a theoretical foundation for approximating high-quality diverse selections.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63a881e4-25b7-4830-a7e5-100b633ad33f",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "0ce6b182-c2b9-4e7a-8620-a041146d087f",
  "toolUseResult": {
    "query": "post-retrieval context selection RAG submodular optimization 2026 recent work",
    "results": [
      {
        "tool_use_id": "srvtoolu_0112pWLUbJAMwZNGGyLv8La2",
        "content": [
          {
            "title": "RAG Techniques Compared: A Practical Guide to Retrieval Augmented Generation in 2026",
            "url": "https://blog.starmorph.com/blog/rag-techniques-compared-best-practices-guide"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "RAG in 2026: How Retrieval-Augmented Generation Works for Enterprise AI",
            "url": "https://www.techment.com/blogs/rag-in-2026/"
          },
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval",
            "url": "https://arxiv.org/pdf/2409.13992"
          },
          {
            "title": "Retrieval-Augmented Generation as In-Context Optimization: A Gradient Descent Perspective | OpenReview",
            "url": "https://openreview.net/forum?id=fz1WJWeITf"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          },
          {
            "title": "Rethinking Retrieval-Augmentation as Synthesis: A Query-Aware Context Merging Approach",
            "url": "https://arxiv.org/pdf/2603.20286"
          }
        ]
      },
      "Based on the search results, I found recent work on post-retrieval context selection in RAG systems with connections to optimization approaches:\n\n## Key Recent Work (2025-2026)\n\n**AdaGReS: Adaptive Greedy Context Selection with Submodular Optimization**\n\nA recent paper provides theoretical analysis and proof of ε-approximate submodularity for a context selection objective, offering theoretical guarantees for the near-global optimality of the greedy selection algorithm. This work addresses the challenge that retrieved results need to exhibit sufficient diversity in content, as systems tend to return overlapping or near-duplicate chunks under top-k retrieval, especially when documents are chunked densely or the corpus is highly redundant.\n\n**SMART-RAG: Determinantal Point Process Selection**\n\nSMART (Selection using Matrices for Augmented ReTrieval) is a fully unsupervised and training-free framework designed to optimize context selection in RAG that leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict.\n\n**Context Merging Approaches**\n\nRAG is constrained by the LLM's context window, and the standard practice adopts a retrieve-then-select paradigm, typically retaining only the top-k chunks based on semantic similarity scores. However, this greedy selection approach suffers from information loss and introduces significant semantic redundancy.\n\nThese recent works in 2025-2026 focus on balancing relevance and diversity in post-retrieval context selection, with submodular optimization serving as a theoretical foundation for approximating high-quality diverse selections."
    ],
    "durationSeconds": 8.692819485,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "63a881e4-25b7-4830-a7e5-100b633ad33f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28 · 2026-05-30T06:51:22.076Z_

```json
{
  "parentUuid": "0ce6b182-c2b9-4e7a-8620-a041146d087f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "328219c6-67ab-4236-ab28-5b294bb9448b",
  "timestamp": "2026-05-30T06:51:22.076Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "328219c6-67ab-4236-ab28-5b294bb9448b",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Tool call

_source line 31 · 2026-05-30T06:51:24.488Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RzBVK4nzRqHokgupHkucsw`</summary>

```json
{
  "query": "non-monotone submodular maximization NLP information retrieval document selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "328219c6-67ab-4236-ab28-5b294bb9448b",
  "isSidechain": false,
  "requestId": "req_011CbYJx1dpWVoHvrsiK7N2Z",
  "type": "assistant",
  "uuid": "3edfe4cc-559f-4c0f-88e8-7422af0980db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BLSNRMd4uXEpzgt4qEusCz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 932,
      "cache_read_input_tokens": 22641,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 932,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 22641,
          "cache_creation_input_tokens": 932,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 932
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

_source line 32 · 2026-05-30T06:51:31.904Z_

<details><summary>↩ Tool result · `toolu_01RzBVK4nzRqHokgupHkucsw`</summary>

```text
Web search results for query: "non-monotone submodular maximization NLP information retrieval document selection 2025 2026"

Links: [{"title":"[1808.06932] Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and Query Complexity","url":"https://arxiv.org/abs/1808.06932"},{"title":"Data Summarization beyond Monotonicity: Non-monotone Two-Stage   Submodular Maximization","url":"https://arxiv.org/pdf/2309.05183"},{"title":"Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and Query Complexity","url":"https://proceedings.mlr.press/v97/fahrbach19a.html"},{"title":"Practical and Parallelizable Algorithms for Non-Monotone Submodular   Maximization with Size Constraint","url":"https://arxiv.org/pdf/2009.01947"},{"title":"Non-monotone submodular maximization under matroid and knapsack   constraints","url":"https://arxiv.org/pdf/0902.0353"},{"title":"Non-monotone Sequential Submodular Maximization","url":"https://arxiv.org/pdf/2308.08641"},{"title":"Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and   Query Complexity","url":"https://arxiv.org/pdf/1808.06932"}]

I found several research papers on non-monotone submodular maximization. Here's what the search revealed:

## Key Research Areas

Non-monotone submodular maximization is a general optimization problem with applications in machine learning including active learning, clustering, and feature selection.

## Recent Developments

Several important algorithmic advances have been made:

1. **Adaptivity and Query Complexity**: One approach gives the first constant-factor approximation algorithm for maximizing a non-monotone submodular function subject to a cardinality constraint that runs in O(log(n)) adaptive rounds and makes O(n log(k)) oracle queries.

2. **Two-Stage Submodular Maximization**: A significant contribution is the development of the first constant-factor approximation algorithm for the non-monotone two-stage submodular maximization problem, with an approximation ratio of 1/2e.

3. **Parallelizable Algorithms**: Recent work improved the best approximation factor for algorithms with optimal adaptivity and query complexity from 0.039 - ε to 0.193 - ε, with one algorithm achieving approximation ratio 1/6 - ε with O(log n) adaptivity and O(n log k) query complexity.

## Applications

Real-world applications include feature selection, profit maximization, maximum cut, and data summarization, as submodular functions are often non-monotone in these scenarios.

However, the search results primarily cover papers from 2018-2023, with no specific results explicitly focused on NLP, information retrieval, or document selection applications from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3edfe4cc-559f-4c0f-88e8-7422af0980db",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "582ee587-4ea5-49e6-9a17-3d1cab6dc76e",
  "toolUseResult": {
    "query": "non-monotone submodular maximization NLP information retrieval document selection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kk9bEdBVUdZeBZvxxWZfPF",
        "content": [
          {
            "title": "[1808.06932] Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and Query Complexity",
            "url": "https://arxiv.org/abs/1808.06932"
          },
          {
            "title": "Data Summarization beyond Monotonicity: Non-monotone Two-Stage   Submodular Maximization",
            "url": "https://arxiv.org/pdf/2309.05183"
          },
          {
            "title": "Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and Query Complexity",
            "url": "https://proceedings.mlr.press/v97/fahrbach19a.html"
          },
          {
            "title": "Practical and Parallelizable Algorithms for Non-Monotone Submodular   Maximization with Size Constraint",
            "url": "https://arxiv.org/pdf/2009.01947"
          },
          {
            "title": "Non-monotone submodular maximization under matroid and knapsack   constraints",
            "url": "https://arxiv.org/pdf/0902.0353"
          },
          {
            "title": "Non-monotone Sequential Submodular Maximization",
            "url": "https://arxiv.org/pdf/2308.08641"
          },
          {
            "title": "Non-monotone Submodular Maximization with Nearly Optimal Adaptivity and   Query Complexity",
            "url": "https://arxiv.org/pdf/1808.06932"
          }
        ]
      },
      "I found several research papers on non-monotone submodular maximization. Here's what the search revealed:\n\n## Key Research Areas\n\nNon-monotone submodular maximization is a general optimization problem with applications in machine learning including active learning, clustering, and feature selection.\n\n## Recent Developments\n\nSeveral important algorithmic advances have been made:\n\n1. **Adaptivity and Query Complexity**: One approach gives the first constant-factor approximation algorithm for maximizing a non-monotone submodular function subject to a cardinality constraint that runs in O(log(n)) adaptive rounds and makes O(n log(k)) oracle queries.\n\n2. **Two-Stage Submodular Maximization**: A significant contribution is the development of the first constant-factor approximation algorithm for the non-monotone two-stage submodular maximization problem, with an approximation ratio of 1/2e.\n\n3. **Parallelizable Algorithms**: Recent work improved the best approximation factor for algorithms with optimal adaptivity and query complexity from 0.039 - ε to 0.193 - ε, with one algorithm achieving approximation ratio 1/6 - ε with O(log n) adaptivity and O(n log k) query complexity.\n\n## Applications\n\nReal-world applications include feature selection, profit maximization, maximum cut, and data summarization, as submodular functions are often non-monotone in these scenarios.\n\nHowever, the search results primarily cover papers from 2018-2023, with no specific results explicitly focused on NLP, information retrieval, or document selection applications from 2025-2026."
    ],
    "durationSeconds": 7.413078622000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3edfe4cc-559f-4c0f-88e8-7422af0980db",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-30T06:51:34.388Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018MaNVWv4YaJ3DuokadjZ5t`</summary>

```json
{
  "query": "redundancy distraction RAG context composition decomposition passage selection optimization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "582ee587-4ea5-49e6-9a17-3d1cab6dc76e",
  "isSidechain": false,
  "requestId": "req_011CbYJxjcS7u9GCTuhKyhiW",
  "type": "assistant",
  "uuid": "7ac34845-a5f7-45f6-be45-091f4c1cf891",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U9bGv6Ub8PRSzdzt94QBRX",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 808,
      "cache_read_input_tokens": 23573,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 808,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 23573,
          "cache_creation_input_tokens": 808,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 808
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

_source line 34 · 2026-05-30T06:51:43.395Z_

<details><summary>↩ Tool result · `toolu_018MaNVWv4YaJ3DuokadjZ5t`</summary>

```text
Web search results for query: "redundancy distraction RAG context composition decomposition passage selection optimization 2025 2026"

Links: [{"title":"RAGSmith: A Framework for Finding the Optimal Composition of","url":"https://arxiv.org/pdf/2511.01386"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/pdf/2512.14313"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/html/2512.14313v1"},{"title":"Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding","url":"https://arxiv.org/pdf/2509.21865"},{"title":"From RAG to Context - A 2025 year-end review of RAG | RAGFlow","url":"https://ragflow.io/blog/rag-review-2025-from-rag-to-context"}]

Based on the search results, here are the key findings related to your query about redundancy, distraction, RAG context composition, decomposition, and passage selection optimization in 2025-2026:

## Key Challenges in RAG Systems

As the number of retrieved passages grows, models may face attention dilution where relevant evidence competes with distractors. RAG systems often suffer from two critical challenges: misleading irrelevant retrieved documents (distractors) that can distort generation results, and the 'lost-in-the-middle' phenomenon.

## Redundancy-Aware Selection

Many systems apply redundancy-aware selection such as Maximal Marginal Relevance (MMR), which trades off relevance and novelty, so that the final context covers diverse supporting evidence instead of repeating the same snippet.

## Dynamic Context Selection

Recent research (2025-2026) is addressing these issues through adaptive approaches. A classifier has been introduced that predicts the optimal number of contexts to retrieve (k), to dynamically adapt the context length to the specific informational requirements of each query. Additionally, DynamicRAG (2025) adaptively determines both the ranking and the number (k) of retrieved documents for each query.

## Distracting Passages

Distracting passages contain irrelevant yet semantically related information that may mislead the LLM and thus hurt answer generation. Both open and closed-source LLMs can fail to answer questions even when the gold passage is retrieved, due to interference from additionally retrieved passages.

These developments represent significant progress in optimizing RAG context composition and mitigating the negative effects of redundancy and distraction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7ac34845-a5f7-45f6-be45-091f4c1cf891",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "af5e051d-b18b-4447-a1ae-d413124b9416",
  "toolUseResult": {
    "query": "redundancy distraction RAG context composition decomposition passage selection optimization 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01S7e2fwViwm8iB6Q7EfnhWx",
        "content": [
          {
            "title": "RAGSmith: A Framework for Finding the Optimal Composition of",
            "url": "https://arxiv.org/pdf/2511.01386"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/html/2512.14313v1"
          },
          {
            "title": "Beyond RAG vs. Long-Context: Learning Distraction-Aware Retrieval for Efficient Knowledge Grounding",
            "url": "https://arxiv.org/pdf/2509.21865"
          },
          {
            "title": "From RAG to Context - A 2025 year-end review of RAG | RAGFlow",
            "url": "https://ragflow.io/blog/rag-review-2025-from-rag-to-context"
          }
        ]
      },
      "Based on the search results, here are the key findings related to your query about redundancy, distraction, RAG context composition, decomposition, and passage selection optimization in 2025-2026:\n\n## Key Challenges in RAG Systems\n\nAs the number of retrieved passages grows, models may face attention dilution where relevant evidence competes with distractors. RAG systems often suffer from two critical challenges: misleading irrelevant retrieved documents (distractors) that can distort generation results, and the 'lost-in-the-middle' phenomenon.\n\n## Redundancy-Aware Selection\n\nMany systems apply redundancy-aware selection such as Maximal Marginal Relevance (MMR), which trades off relevance and novelty, so that the final context covers diverse supporting evidence instead of repeating the same snippet.\n\n## Dynamic Context Selection\n\nRecent research (2025-2026) is addressing these issues through adaptive approaches. A classifier has been introduced that predicts the optimal number of contexts to retrieve (k), to dynamically adapt the context length to the specific informational requirements of each query. Additionally, DynamicRAG (2025) adaptively determines both the ranking and the number (k) of retrieved documents for each query.\n\n## Distracting Passages\n\nDistracting passages contain irrelevant yet semantically related information that may mislead the LLM and thus hurt answer generation. Both open and closed-source LLMs can fail to answer questions even when the gold passage is retrieved, due to interference from additionally retrieved passages.\n\nThese developments represent significant progress in optimizing RAG context composition and mitigating the negative effects of redundancy and distraction."
    ],
    "durationSeconds": 9.001117824000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7ac34845-a5f7-45f6-be45-091f4c1cf891",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-30T06:51:46.124Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FG2v5Y9zxg58E5Y2WPmhEF`</summary>

```json
{
  "query": "AdaGATE adaptive gap-aware token-efficient multi-hop RAG 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af5e051d-b18b-4447-a1ae-d413124b9416",
  "isSidechain": false,
  "requestId": "req_011CbYJyaoPVG1oioo24iK42",
  "type": "assistant",
  "uuid": "c7e645ba-066b-4c80-a380-39978251e325",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MxomHUaq9AyVLrCBqXueWU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 769,
      "cache_read_input_tokens": 24381,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 769,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 24381,
          "cache_creation_input_tokens": 769,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 769
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

_source line 36 · 2026-05-30T06:51:52.992Z_

<details><summary>↩ Tool result · `toolu_01FG2v5Y9zxg58E5Y2WPmhEF`</summary>

```text
Web search results for query: "AdaGATE adaptive gap-aware token-efficient multi-hop RAG 2026"

Links: [{"title":"[2605.05245] AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2605.05245"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation","url":"https://arxiv.org/html/2605.05245"},{"title":"AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for","url":"https://arxiv.org/pdf/2605.05245"},{"title":"CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering","url":"https://arxiv.org/html/2602.05728v1"},{"title":"FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2510.22344"},{"title":"[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG","url":"https://arxiv.org/abs/2511.09803"},{"title":"Think Straight, Stop Smart: Structured Reasoning for Efficient Multi-Hop RAG","url":"https://arxiv.org/pdf/2510.19171"},{"title":"Curriculum Guided Reinforcement Learning for Efficient Multi Hop Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2505.17391"}]

Based on the search results, I found detailed information about AdaGATE:

## AdaGATE Overview

AdaGATE is a training-free evidence controller for multi-hop RAG that frames evidence selection as a token-constrained repair problem. It combines entity centric gap tracking, targeted micro-query generation, and a utility based selection mechanism that balances gap coverage, corroboration, novelty, redundancy, and direct question relevance.

## Key Results

AdaGATE achieves the best evidence F1 among compared controllers, reaching 62.3% on clean data and 71.2% under redundancy injection, while using 2.6x fewer input tokens than Adaptive-k.

## Problem it Addresses

AdaGATE addresses the issue that multi-hop RAG remains brittle on multi-hop questions in realistic deployment settings, where retrieved evidence may be noisy or redundant and only limited context can be passed to the generator.

## Evaluation

The method was evaluated on HotpotQA under clean, redundancy, and noise injected retrieval conditions.

The paper was published on arXiv in May 2026 (arXiv:2605.05245) and appears to be a recent research contribution to improving the efficiency and robustness of multi-hop retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7e645ba-066b-4c80-a380-39978251e325",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "d02b5351-f96d-4a50-8335-877f6e40b2b7",
  "toolUseResult": {
    "query": "AdaGATE adaptive gap-aware token-efficient multi-hop RAG 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TneLs6mTtq2VbvaY3vn2eJ",
        "content": [
          {
            "title": "[2605.05245] AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2605.05245"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for Multi-Hop Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2605.05245"
          },
          {
            "title": "AdaGATE: Adaptive Gap-Aware Token-Efficient Evidence Assembly for",
            "url": "https://arxiv.org/pdf/2605.05245"
          },
          {
            "title": "CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering",
            "url": "https://arxiv.org/html/2602.05728v1"
          },
          {
            "title": "FAIR-RAG: Faithful Adaptive Iterative Refinement for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2510.22344"
          },
          {
            "title": "[2511.09803] Retrieval as a Decision: Training-Free Adaptive Gating for Efficient RAG",
            "url": "https://arxiv.org/abs/2511.09803"
          },
          {
            "title": "Think Straight, Stop Smart: Structured Reasoning for Efficient Multi-Hop RAG",
            "url": "https://arxiv.org/pdf/2510.19171"
          },
          {
            "title": "Curriculum Guided Reinforcement Learning for Efficient Multi Hop Retrieval Augmented Generation",
            "url": "https://arxiv.org/pdf/2505.17391"
          }
        ]
      },
      "Based on the search results, I found detailed information about AdaGATE:\n\n## AdaGATE Overview\n\nAdaGATE is a training-free evidence controller for multi-hop RAG that frames evidence selection as a token-constrained repair problem. It combines entity centric gap tracking, targeted micro-query generation, and a utility based selection mechanism that balances gap coverage, corroboration, novelty, redundancy, and direct question relevance.\n\n## Key Results\n\nAdaGATE achieves the best evidence F1 among compared controllers, reaching 62.3% on clean data and 71.2% under redundancy injection, while using 2.6x fewer input tokens than Adaptive-k.\n\n## Problem it Addresses\n\nAdaGATE addresses the issue that multi-hop RAG remains brittle on multi-hop questions in realistic deployment settings, where retrieved evidence may be noisy or redundant and only limited context can be passed to the generator.\n\n## Evaluation\n\nThe method was evaluated on HotpotQA under clean, redundancy, and noise injected retrieval conditions.\n\nThe paper was published on arXiv in May 2026 (arXiv:2605.05245) and appears to be a recent research contribution to improving the efficiency and robustness of multi-hop retrieval-augmented generation systems."
    ],
    "durationSeconds": 6.864745154999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c7e645ba-066b-4c80-a380-39978251e325",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-30T06:51:55.265Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G9kmn4abeGT2Jr8EbxB8Jg`</summary>

```json
{
  "query": "\"context-picker\" dynamic context selection multi-stage reinforcement learning RAG 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d02b5351-f96d-4a50-8335-877f6e40b2b7",
  "isSidechain": false,
  "requestId": "req_011CbYJzHnyG6WxLS6ZnrvzS",
  "type": "assistant",
  "uuid": "f7722693-095f-4d57-b600-79371782536a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013ppHqvm7KHffxNrXHjeQCF",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 810,
      "cache_read_input_tokens": 25150,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 810,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 25150,
          "cache_creation_input_tokens": 810,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 810
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

_source line 38 · 2026-05-30T06:52:03.504Z_

<details><summary>↩ Tool result · `toolu_01G9kmn4abeGT2Jr8EbxB8Jg`</summary>

```text
Web search results for query: ""context-picker" dynamic context selection multi-stage reinforcement learning RAG 2025"

Links: [{"title":"Dynamic context selection using multi-stage reinforcement ...","url":"https://arxiv.org/pdf/2512.14465"},{"title":"Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning","url":"https://arxiv.org/html/2512.14465"},{"title":"[2512.14465] Context-Picker: Dynamic context selection using multi-stage reinforcement learning","url":"https://arxiv.org/abs/2512.14465"},{"title":"Context-Picker: Optimal Context Selection","url":"https://www.emergentmind.com/topics/context-picker"},{"title":"Paper page - Context-Picker: Dynamic context selection using multi-stage reinforcement learning","url":"https://huggingface.co/papers/2512.14465"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating","url":"https://arxiv.org/pdf/2512.14313"},{"title":"Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias","url":"https://arxiv.org/html/2512.14313v1"},{"title":"Overview of the Context-Picker framework. The pipeline consists of two... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Overview-of-the-Context-Picker-framework-The-pipeline-consists-of-two-parts-1-Offline_fig1_398765792"}]

I found relevant results about Context-Picker. Here's what the search revealed:

## Context-Picker Overview

Context-Picker is a reasoning-aware framework that shifts the context selection paradigm from similarity-based ranking to minimal sufficient subset selection. In long-context question answering, selecting the appropriate scope of context for a query remains a key challenge, as insufficient context can lead to missing essential information, whereas excessive context often introduces noise and degrades answer quality.

## Multi-Stage Reinforcement Learning Approach

Context-Picker uses a human-inspired two-stage reinforcement learning schedule: stage 1 focuses on improving the recall rate of critical passages, and stage 2 prioritizes pruning redundancy to distill a compact evidence set. To resolve reward sparsity, the framework proposes an offline evidence distillation pipeline that mines "minimal sufficient sets" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision.

## Performance Results

Experiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths.

The paper appears to be from December 2025 (arXiv identifier 2512.14465) and represents recent work in improving RAG systems through principled context selection optimization.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7722693-095f-4d57-b600-79371782536a",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "548561aa-e439-4fb5-80b9-acbf62a4e7a6",
  "toolUseResult": {
    "query": "\"context-picker\" dynamic context selection multi-stage reinforcement learning RAG 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XBa8NWngEDZkeB2bp1XMw9",
        "content": [
          {
            "title": "Dynamic context selection using multi-stage reinforcement ...",
            "url": "https://arxiv.org/pdf/2512.14465"
          },
          {
            "title": "Context-Picker: Dynamic Context Selection Using Multi-stage Reinforcement Learning",
            "url": "https://arxiv.org/html/2512.14465"
          },
          {
            "title": "[2512.14465] Context-Picker: Dynamic context selection using multi-stage reinforcement learning",
            "url": "https://arxiv.org/abs/2512.14465"
          },
          {
            "title": "Context-Picker: Optimal Context Selection",
            "url": "https://www.emergentmind.com/topics/context-picker"
          },
          {
            "title": "Paper page - Context-Picker: Dynamic context selection using multi-stage reinforcement learning",
            "url": "https://huggingface.co/papers/2512.14465"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating",
            "url": "https://arxiv.org/pdf/2512.14313"
          },
          {
            "title": "Dynamic Context Selection for Retrieval-Augmented Generation: Mitigating Distractors and Positional Bias",
            "url": "https://arxiv.org/html/2512.14313v1"
          },
          {
            "title": "Overview of the Context-Picker framework. The pipeline consists of two... | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Overview-of-the-Context-Picker-framework-The-pipeline-consists-of-two-parts-1-Offline_fig1_398765792"
          }
        ]
      },
      "I found relevant results about Context-Picker. Here's what the search revealed:\n\n## Context-Picker Overview\n\nContext-Picker is a reasoning-aware framework that shifts the context selection paradigm from similarity-based ranking to minimal sufficient subset selection. In long-context question answering, selecting the appropriate scope of context for a query remains a key challenge, as insufficient context can lead to missing essential information, whereas excessive context often introduces noise and degrades answer quality.\n\n## Multi-Stage Reinforcement Learning Approach\n\nContext-Picker uses a human-inspired two-stage reinforcement learning schedule: stage 1 focuses on improving the recall rate of critical passages, and stage 2 prioritizes pruning redundancy to distill a compact evidence set. To resolve reward sparsity, the framework proposes an offline evidence distillation pipeline that mines \"minimal sufficient sets\" via a Leave-One-Out (LOO) procedure, providing dense, task-aligned supervision.\n\n## Performance Results\n\nExperiments on five long-context and multi-hop QA benchmarks demonstrate that Context-Picker significantly outperforms strong RAG baselines, achieving superior answer accuracy with comparable or reduced context lengths.\n\nThe paper appears to be from December 2025 (arXiv identifier 2512.14465) and represents recent work in improving RAG systems through principled context selection optimization."
    ],
    "durationSeconds": 8.210497806,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f7722693-095f-4d57-b600-79371782536a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-30T06:52:06.632Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YBqVg2Za7nN8sSZzgx4Gpp`</summary>

```json
{
  "query": "SMART-RAG DPP determinantal point process context selection RAG diversity relevance 2024 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "548561aa-e439-4fb5-80b9-acbf62a4e7a6",
  "isSidechain": false,
  "requestId": "req_011CbYK14ypFmsTgNc1bL19E",
  "type": "assistant",
  "uuid": "22d1e16d-082a-481e-981a-2eca361413d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013sZj6e54i6aQiLcndQUQ75",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 25960,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 25960,
          "cache_creation_input_tokens": 774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 774
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

_source line 40 · 2026-05-30T06:52:14.940Z_

<details><summary>↩ Tool result · `toolu_01YBqVg2Za7nN8sSZzgx4Gpp`</summary>

```text
Web search results for query: "SMART-RAG DPP determinantal point process context selection RAG diversity relevance 2024 2025"

Links: [{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval","url":"https://arxiv.org/pdf/2409.13992"},{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval","url":"https://arxiv.org/html/2409.13992v1"},{"title":"SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv240913992L/abstract"},{"title":"(PDF) SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval","url":"https://www.researchgate.net/publication/384266865_SMART-RAG_Selection_using_Determinantal_Matrices_for_Augmented_Retrieval"},{"title":"[Literature Review] SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval","url":"https://www.themoonlight.io/en/review/smart-rag-selection-using-determinantal-matrices-for-augmented-retrieval"},{"title":"[2409.13992] SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval","url":"https://arxiv.org/abs/2409.13992"},{"title":"Determinantal Point Processes for Machine Learning","url":"https://www.researchgate.net/publication/230568602_Determinantal_Point_Processes_for_Machine_Learning"},{"title":"Scaling DPPs for RAG: Density Meets Diversity","url":"https://arxiv.org/html/2604.03240"}]

Based on the search results, I found comprehensive information about SMART-RAG and its use of Determinantal Point Processes (DPPs) for context selection in RAG systems.

## SMART-RAG Overview

SMART (Selection using Matrices for Augmented Retrieval) is a fully unsupervised and training-free framework designed to optimize context selection in RAG for question answering tasks.

## Key Innovation: DPP-Based Context Selection

SMART leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict, ensuring the selection of potentially high-quality contexts. A crucial factor for producing accurate, coherent answers lies in striking a balance between relevance and diversity while minimizing contradictions.

## Problem Being Addressed

Conventional RAG approaches, which prioritize top-ranked documents based solely on query-context relevance, often introduce redundancy and conflicting information. This issue is particularly evident in unsupervised retrieval settings, where there are no mechanisms to effectively mitigate these problems, leading to suboptimal context selection.

## Methodology

The pipeline involves two key stages: (1) Data Processing, where Query-Context (QC) and Context-Context (CC) relations are constructed, and (2) Context Selection, leveraging Determinantal Point Processes (DPP) to balance relevance and diversity while resolving conflicts between contexts.

## Results

Experimental results across multiple datasets demonstrate that SMART significantly enhances QA performance and surpasses previous unsupervised context selection methods, showing a promising strategy for RAG. The paper was published in September 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "22d1e16d-082a-481e-981a-2eca361413d4",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "d884d8af-155b-4664-88e8-6cf8e7fa7509",
  "toolUseResult": {
    "query": "SMART-RAG DPP determinantal point process context selection RAG diversity relevance 2024 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QzJST8LxzJJUxuA7uMaqm7",
        "content": [
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented   Retrieval",
            "url": "https://arxiv.org/pdf/2409.13992"
          },
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval",
            "url": "https://arxiv.org/html/2409.13992v1"
          },
          {
            "title": "SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2024arXiv240913992L/abstract"
          },
          {
            "title": "(PDF) SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval",
            "url": "https://www.researchgate.net/publication/384266865_SMART-RAG_Selection_using_Determinantal_Matrices_for_Augmented_Retrieval"
          },
          {
            "title": "[Literature Review] SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval",
            "url": "https://www.themoonlight.io/en/review/smart-rag-selection-using-determinantal-matrices-for-augmented-retrieval"
          },
          {
            "title": "[2409.13992] SMART-RAG: Selection using Determinantal Matrices for Augmented Retrieval",
            "url": "https://arxiv.org/abs/2409.13992"
          },
          {
            "title": "Determinantal Point Processes for Machine Learning",
            "url": "https://www.researchgate.net/publication/230568602_Determinantal_Point_Processes_for_Machine_Learning"
          },
          {
            "title": "Scaling DPPs for RAG: Density Meets Diversity",
            "url": "https://arxiv.org/html/2604.03240"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about SMART-RAG and its use of Determinantal Point Processes (DPPs) for context selection in RAG systems.\n\n## SMART-RAG Overview\n\nSMART (Selection using Matrices for Augmented Retrieval) is a fully unsupervised and training-free framework designed to optimize context selection in RAG for question answering tasks.\n\n## Key Innovation: DPP-Based Context Selection\n\nSMART leverages Determinantal Point Processes (DPPs) to simultaneously model relevance, diversity and conflict, ensuring the selection of potentially high-quality contexts. A crucial factor for producing accurate, coherent answers lies in striking a balance between relevance and diversity while minimizing contradictions.\n\n## Problem Being Addressed\n\nConventional RAG approaches, which prioritize top-ranked documents based solely on query-context relevance, often introduce redundancy and conflicting information. This issue is particularly evident in unsupervised retrieval settings, where there are no mechanisms to effectively mitigate these problems, leading to suboptimal context selection.\n\n## Methodology\n\nThe pipeline involves two key stages: (1) Data Processing, where Query-Context (QC) and Context-Context (CC) relations are constructed, and (2) Context Selection, leveraging Determinantal Point Processes (DPP) to balance relevance and diversity while resolving conflicts between contexts.\n\n## Results\n\nExperimental results across multiple datasets demonstrate that SMART significantly enhances QA performance and surpasses previous unsupervised context selection methods, showing a promising strategy for RAG. The paper was published in September 2024."
    ],
    "durationSeconds": 8.30391401399998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "22d1e16d-082a-481e-981a-2eca361413d4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "d884d8af-155b-4664-88e8-6cf8e7fa7509",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Assistant

_source line 43 · 2026-05-30T06:52:17.870Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me do one more search to check if there's any work that already combines distraction and redundancy in a submodular framework:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d884d8af-155b-4664-88e8-6cf8e7fa7509",
  "isSidechain": false,
  "requestId": "req_011CbYK1udXUytvPx5rzhUqs",
  "type": "assistant",
  "uuid": "b25d267e-0005-4ec6-b862-685d2c32e264",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fijviXaEeQduNV23W6gjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 26734,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26734,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 44 · 2026-05-30T06:52:18.315Z_

Let me do one more critical search to check if anyone has already combined distraction and submodularity in a single framework.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b25d267e-0005-4ec6-b862-685d2c32e264",
  "isSidechain": false,
  "requestId": "req_011CbYK1udXUytvPx5rzhUqs",
  "type": "assistant",
  "uuid": "2acadf94-388c-4713-8833-dfd7c991d672",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fijviXaEeQduNV23W6gjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 26734,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26734,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 45 · 2026-05-30T06:52:19.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XX7cS27wZo5h4eVod5cPq4`</summary>

```json
{
  "query": "submodular optimization distraction penalty RAG passage selection non-monotone context composition 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2acadf94-388c-4713-8833-dfd7c991d672",
  "isSidechain": false,
  "requestId": "req_011CbYK1udXUytvPx5rzhUqs",
  "type": "assistant",
  "uuid": "236d1cf6-88e8-4b72-8fb2-53ca7026104c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017fijviXaEeQduNV23W6gjQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 913,
      "cache_read_input_tokens": 26734,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 913,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 145,
          "cache_read_input_tokens": 26734,
          "cache_creation_input_tokens": 913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 913
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

_source line 46 · 2026-05-30T06:52:27.067Z_

<details><summary>↩ Tool result · `toolu_01XX7cS27wZo5h4eVod5cPq4`</summary>

```text
Web search results for query: "submodular optimization distraction penalty RAG passage selection non-monotone context composition 2025 2026"

Links: [{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"The Distracting Effect: Understanding Irrelevant Passages in RAG","url":"https://arxiv.org/pdf/2505.06914"},{"title":"Proceedings - Retrieval Augmented Generation (RAG) 2025 - TREC Browser","url":"https://pages.nist.gov/trec-browser/trec34/rag/proceedings/"},{"title":"OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation","url":"https://arxiv.org/pdf/2601.05027"},{"title":"AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG","url":"https://arxiv.org/pdf/2512.25052"},{"title":"Submodular Evaluation Subset Selection in Automatic Prompt Optimization","url":"https://arxiv.org/pdf/2601.03493"}]

I found several relevant results for your search query. Here's what I found:

## Key Research Areas

**Submodular Optimization for RAG Passage Selection:**
Recent work combines greedy submodular evidence selection, evidence-card compression, and citation-first answer generation, with applications to RAG tasks in 2025. Submodular evidence selection for grounded answer generation has been explored in TREC RAG 2025.

**Distraction Penalty and Irrelevant Passages:**
Distracting passages contain irrelevant yet semantically related information that may mislead the LLM and thus hurt answer generation. Recent research moves beyond simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and develops methods for finding hard distracting passages.

**Context Composition and Selection:**
A persistent challenge in RAG remains the redundancy and overlap among selected context chunks. Recent work provides theoretical analysis and proof of approximate submodularity for context selection objectives, offering theoretical guarantees for near-global optimality of greedy selection algorithms.

The search results show active research in 2025-2026 combining submodular optimization with RAG passage selection, addressing both the problem of distraction penalties from irrelevant passages and achieving better context composition through principled mathematical frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "236d1cf6-88e8-4b72-8fb2-53ca7026104c",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "73e5b297-e164-40f8-b124-dbb95db73ced",
  "toolUseResult": {
    "query": "submodular optimization distraction penalty RAG passage selection non-monotone context composition 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016axo6JY3yDUxt56GEnJp1W",
        "content": [
          {
            "title": "Submodular Optimization for Text Selection, Passage Reranking & Context Engineering",
            "url": "https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"
          },
          {
            "title": "The Distracting Effect: Understanding Irrelevant Passages in RAG",
            "url": "https://arxiv.org/pdf/2505.06914"
          },
          {
            "title": "Proceedings - Retrieval Augmented Generation (RAG) 2025 - TREC Browser",
            "url": "https://pages.nist.gov/trec-browser/trec34/rag/proceedings/"
          },
          {
            "title": "OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/pdf/2601.05027"
          },
          {
            "title": "AdaGReS:Adaptive Greedy Context Selection via Redundancy-Aware Scoring for Token-Budgeted RAG",
            "url": "https://arxiv.org/pdf/2512.25052"
          },
          {
            "title": "Submodular Evaluation Subset Selection in Automatic Prompt Optimization",
            "url": "https://arxiv.org/pdf/2601.03493"
          }
        ]
      },
      "I found several relevant results for your search query. Here's what I found:\n\n## Key Research Areas\n\n**Submodular Optimization for RAG Passage Selection:**\nRecent work combines greedy submodular evidence selection, evidence-card compression, and citation-first answer generation, with applications to RAG tasks in 2025. Submodular evidence selection for grounded answer generation has been explored in TREC RAG 2025.\n\n**Distraction Penalty and Irrelevant Passages:**\nDistracting passages contain irrelevant yet semantically related information that may mislead the LLM and thus hurt answer generation. Recent research moves beyond simple binary classification of irrelevant passages as either completely unrelated vs. distracting, and develops methods for finding hard distracting passages.\n\n**Context Composition and Selection:**\nA persistent challenge in RAG remains the redundancy and overlap among selected context chunks. Recent work provides theoretical analysis and proof of approximate submodularity for context selection objectives, offering theoretical guarantees for near-global optimality of greedy selection algorithms.\n\nThe search results show active research in 2025-2026 combining submodular optimization with RAG passage selection, addressing both the problem of distraction penalties from irrelevant passages and achieving better context composition through principled mathematical frameworks."
    ],
    "durationSeconds": 7.6823704080000175,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "236d1cf6-88e8-4b72-8fb2-53ca7026104c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-30T06:52:29.347Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015fT58YUrtCuMLPZD2oY1FK`</summary>

```json
{
  "query": "Jina submodular optimization text selection passage reranking context engineering 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "73e5b297-e164-40f8-b124-dbb95db73ced",
  "isSidechain": false,
  "requestId": "req_011CbYK2oVDN5HBWmNDjygwj",
  "type": "assistant",
  "uuid": "15094fcc-813c-4b5d-b8d8-23fca787f3ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01T35A1i2ZZxXguwku2TrUMv",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 27647,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 27647,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 779
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

_source line 48 · 2026-05-30T06:52:40.999Z_

<details><summary>↩ Tool result · `toolu_015fT58YUrtCuMLPZD2oY1FK`</summary>

```text
Web search results for query: "Jina submodular optimization text selection passage reranking context engineering 2025 2026"

Links: [{"title":"Submodular Optimization for Text Selection, Passage Reranking & Context Engineering","url":"https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"},{"title":"Reranker API","url":"https://jina.ai/reranker/"},{"title":"Jina AI on X: \"Submodular optimization for token/sentence selection from long contexts. Here's an interesting exp: first used jina-embeddings-v4's multi-vector feature to extract token-level embeddings from a passage, then applied submodular optimization to cherry-pick the tokens that provide https://t.co/vXDQNkdLMl\" / X","url":"https://x.com/JinaAI_/status/1943052306028933328"},{"title":"jina-reranker-v3: Last but Not Late Interaction for Listwise Document Reranking","url":"https://arxiv.org/pdf/2509.25085"},{"title":"Query-focused and Memory-aware Reranker for Long Context Processing","url":"https://arxiv.org/pdf/2602.12192"},{"title":"Reranking Passages with Coarse-to-Fine Neural Retriever Enhanced by   List-Context Information","url":"https://arxiv.org/pdf/2308.12022"},{"title":"From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation","url":"https://arxiv.org/pdf/2508.09497"},{"title":"Hybrid and Collaborative Passage Reranking","url":"https://arxiv.org/pdf/2305.09313"},{"title":"Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning","url":"https://arxiv.org/pdf/2604.02091"}]

Based on the search results, here's what I found about Jina's work on submodular optimization for text selection, passage reranking, and context engineering:

## Key Findings

Jina demonstrated that both text selection and passage reranking yield to submodular optimization, which provides rigorous solutions. Submodular functions work based on "diminishing returns," where starting with an empty set and incrementally adding selected text or passages provides value, but the marginal benefit decreases—capturing the intuition that diverse, non-redundant selections are most valuable.

### Practical Implementation

Jina used jina-embeddings-v4's multi-vector feature to extract token-level embeddings from a passage, then applied submodular optimization to cherry-pick the tokens that provide the best coverage, finally calling the tokenizer and converting selections back to strings at their original positions.

### Context Engineering Framework

Jina positions submodular optimization as providing a principled framework with theoretical guarantees for better context engineering, in contrast to approaches that rely on prompt tuning. Jina has published work on submodular optimization for context engineering including query fan-out, text selection, and passage reranking.

The article demonstrating these concepts was published on July 15, 2025, on Jina's website, showing this is a recent development in their approach to handling long contexts and improving retrieval-augmented generation systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "15094fcc-813c-4b5d-b8d8-23fca787f3ad",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "2d1653aa-53ab-4686-955e-940ec39a0b57",
  "toolUseResult": {
    "query": "Jina submodular optimization text selection passage reranking context engineering 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BBXzFvsDhL5r7dpLacPBj6",
        "content": [
          {
            "title": "Submodular Optimization for Text Selection, Passage Reranking & Context Engineering",
            "url": "https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/"
          },
          {
            "title": "Reranker API",
            "url": "https://jina.ai/reranker/"
          },
          {
            "title": "Jina AI on X: \"Submodular optimization for token/sentence selection from long contexts. Here's an interesting exp: first used jina-embeddings-v4's multi-vector feature to extract token-level embeddings from a passage, then applied submodular optimization to cherry-pick the tokens that provide https://t.co/vXDQNkdLMl\" / X",
            "url": "https://x.com/JinaAI_/status/1943052306028933328"
          },
          {
            "title": "jina-reranker-v3: Last but Not Late Interaction for Listwise Document Reranking",
            "url": "https://arxiv.org/pdf/2509.25085"
          },
          {
            "title": "Query-focused and Memory-aware Reranker for Long Context Processing",
            "url": "https://arxiv.org/pdf/2602.12192"
          },
          {
            "title": "Reranking Passages with Coarse-to-Fine Neural Retriever Enhanced by   List-Context Information",
            "url": "https://arxiv.org/pdf/2308.12022"
          },
          {
            "title": "From Ranking to Selection: A Simple but Efficient Dynamic Passage Selector for Retrieval Augmented Generation",
            "url": "https://arxiv.org/pdf/2508.09497"
          },
          {
            "title": "Hybrid and Collaborative Passage Reranking",
            "url": "https://arxiv.org/pdf/2305.09313"
          },
          {
            "title": "Optimizing RAG Rerankers with LLM Feedback via Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2604.02091"
          }
        ]
      },
      "Based on the search results, here's what I found about Jina's work on submodular optimization for text selection, passage reranking, and context engineering:\n\n## Key Findings\n\nJina demonstrated that both text selection and passage reranking yield to submodular optimization, which provides rigorous solutions. Submodular functions work based on \"diminishing returns,\" where starting with an empty set and incrementally adding selected text or passages provides value, but the marginal benefit decreases—capturing the intuition that diverse, non-redundant selections are most valuable.\n\n### Practical Implementation\n\nJina used jina-embeddings-v4's multi-vector feature to extract token-level embeddings from a passage, then applied submodular optimization to cherry-pick the tokens that provide the best coverage, finally calling the tokenizer and converting selections back to strings at their original positions.\n\n### Context Engineering Framework\n\nJina positions submodular optimization as providing a principled framework with theoretical guarantees for better context engineering, in contrast to approaches that rely on prompt tuning. Jina has published work on submodular optimization for context engineering including query fan-out, text selection, and passage reranking.\n\nThe article demonstrating these concepts was published on July 15, 2025, on Jina's website, showing this is a recent development in their approach to handling long contexts and improving retrieval-augmented generation systems."
    ],
    "durationSeconds": 11.645418309,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "15094fcc-813c-4b5d-b8d8-23fca787f3ad",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 49 · 2026-05-30T06:52:45.781Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDp4ChLsXNAx5U8Sq53NAB`</summary>

```json
{
  "query": "OptiSet unified optimizing set selection ranking retrieval augmented generation 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d1653aa-53ab-4686-955e-940ec39a0b57",
  "isSidechain": false,
  "requestId": "req_011CbYK3qGeNJM4iurMprkC5",
  "type": "assistant",
  "uuid": "318e6d4e-6beb-4060-97d8-0c226ae59ead",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YJoUxHXAoWGMaRAZiYoJGx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 28426,
      "output_tokens": 68,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 68,
          "cache_read_input_tokens": 28426,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 50 · 2026-05-30T06:52:53.854Z_

<details><summary>↩ Tool result · `toolu_01UDp4ChLsXNAx5U8Sq53NAB`</summary>

```text
Web search results for query: "OptiSet unified optimizing set selection ranking retrieval augmented generation 2026"

Links: [{"title":"GitHub - liunian-Jay/OptiSet: [Under Review] OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation","url":"https://github.com/liunian-Jay/OptiSet"},{"title":"[2601.05027] OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation","url":"https://arxiv.org/abs/2601.05027"},{"title":"OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation","url":"https://arxiv.org/html/2601.05027"},{"title":"OptiSet: Unified Optimizing Set Selection and Ranking for ...","url":"https://arxiv.org/pdf/2601.05027"},{"title":"Passage Re Ranking","url":"https://www.catalyzex.com/s/Passage%20Re%20Ranking"},{"title":"Shifting from Ranking to Set Selection for Retrieval Augmented Generation","url":"https://arxiv.org/html/2507.06838"},{"title":"GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.","url":"https://github.com/liunian-Jay/Awesome-RAG"}]

Based on the search results, here's what I found about OptiSet:

OptiSet is a set-centric framework that unifies set selection and set-level ranking for RAG, adopting an "Expand-then-Refine" paradigm where it first expands a query into multiple perspectives to enable a diverse candidate pool and then refines the candidate pool via re-selection to form a compact evidence set.

**Key Problem It Addresses:**
Most existing RAG methods rely on statically selecting top-k passages based on individual relevance, which fails to exploit combinatorial gains among passages and often introduces substantial redundancy.

**Methodology:**
OptiSet devises a self-synthesis strategy without strong LLM supervision to derive preference labels from the set conditional utility changes of the generator, thereby identifying complementary and redundant evidence. It introduces a set-list wise training strategy that jointly optimizes set selection and set-level ranking, enabling the model to favor compact, high-gain evidence sets.

**Authors and Availability:**
The paper is authored by Yi Jiang, Sendong Zhao, Jianbo Li, Bairui Hu, Yanrui Du, Haochun Wang, and Bing Qin, with an arXiv preprint (2601.05027) from January 2026.

The project has a GitHub repository available for the implementation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "318e6d4e-6beb-4060-97d8-0c226ae59ead",
  "isSidechain": false,
  "promptId": "7b1a8718-cc94-46ac-8657-1a47c12cf9cd",
  "type": "user",
  "uuid": "6831cc9c-6b1f-43aa-8dc1-cc2f4e8391ba",
  "toolUseResult": {
    "query": "OptiSet unified optimizing set selection ranking retrieval augmented generation 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019DaabpfYQBy56x8LoFxHwo",
        "content": [
          {
            "title": "GitHub - liunian-Jay/OptiSet: [Under Review] OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation",
            "url": "https://github.com/liunian-Jay/OptiSet"
          },
          {
            "title": "[2601.05027] OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/abs/2601.05027"
          },
          {
            "title": "OptiSet: Unified Optimizing Set Selection and Ranking for Retrieval-Augmented Generation",
            "url": "https://arxiv.org/html/2601.05027"
          },
          {
            "title": "OptiSet: Unified Optimizing Set Selection and Ranking for ...",
            "url": "https://arxiv.org/pdf/2601.05027"
          },
          {
            "title": "Passage Re Ranking",
            "url": "https://www.catalyzex.com/s/Passage%20Re%20Ranking"
          },
          {
            "title": "Shifting from Ranking to Set Selection for Retrieval Augmented Generation",
            "url": "https://arxiv.org/html/2507.06838"
          },
          {
            "title": "GitHub - liunian-Jay/Awesome-RAG: 💡 Awesome RAG: A resource of Retrieval-Augmented Generation (RAG) for LLMs, focusing on the development of technology.",
            "url": "https://github.com/liunian-Jay/Awesome-RAG"
          }
        ]
      },
      "Based on the search results, here's what I found about OptiSet:\n\nOptiSet is a set-centric framework that unifies set selection and set-level ranking for RAG, adopting an \"Expand-then-Refine\" paradigm where it first expands a query into multiple perspectives to enable a diverse candidate pool and then refines the candidate pool via re-selection to form a compact evidence set.\n\n**Key Problem It Addresses:**\nMost existing RAG methods rely on statically selecting top-k passages based on individual relevance, which fails to exploit combinatorial gains among passages and often introduces substantial redundancy.\n\n**Methodology:**\nOptiSet devises a self-synthesis strategy without strong LLM supervision to derive preference labels from the set conditional utility changes of the generator, thereby identifying complementary and redundant evidence. It introduces a set-list wise training strategy that jointly optimizes set selection and set-level ranking, enabling the model to favor compact, high-gain evidence sets.\n\n**Authors and Availability:**\nThe paper is authored by Yi Jiang, Sendong Zhao, Jianbo Li, Bairui Hu, Yanrui Du, Haochun Wang, and Bing Qin, with an arXiv preprint (2601.05027) from January 2026.\n\nThe project has a GitHub repository available for the implementation."
    ],
    "durationSeconds": 8.067171563000011,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "318e6d4e-6beb-4060-97d8-0c226ae59ead",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-30T06:53:43.118Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the landscape. Let me synthesize my findings and provide my analysis as the 发掘 agent.

Key findings from my research:

1. **AdaGReS** (Dec 2025): ε-approximate submodularity for redundancy-penalized context selection, monotone only. Evaluated on NQ and a biomedical corpus.

2. **The Distracting Effect** (ACL 2025): Defines DE_q(p) as a continuous distraction measure for irrelevant passages. No set-level optimization.


3. **γ-weakly DR-submodular** (AAMAS 2026): Offers approximation guarantees for non-monotone functions in this class, though without applications to NLP tasks.
4. **CCBQP** (Apr 2026): Uses binary quadratic programming to balance relevance and diversity in retrieval, but the authors themselves question whether adding a distraction penalty would maintain their theoretical properties.
5. **LDAR** (ICLR 2026): Incorporates distraction awareness directly during retrieval across six benchmarks, though it lacks formal approximation guarantees and doesn't compose with post-retrieval methods.
6. **DynamicRAG** (N...

Continuing through the recent approaches, I see several methods tackling context selection and reranking—DynamicRAG uses reinforcement learning with LLM feedback across seven benchmarks, SMART-RAG applies determinantal point processes to model relevance, diversity, and conflicts without training, and Context-Picker employs a two-stage RL framework for finding minimal sufficient subsets. OptiSet frames this as a set-centric problem with expand-then-refine logic, Jina applies submodular optimization to passage selection, and AdaGATE provides a training-free controller for multi-hop reasoning that balances coverage gaps, corroboration, and novelty.

Now I'm evaluating the proposal itself. The core innovation genuinely stands out—it combines three distinct components: AdaGReS's submodular framework, the distraction measure from The Distracting Effect, and γ-weakly DR-submodular guarantees from AAMAS 2026 into a single approach that's post-retrieval, formally grounded with provable bounds, and distraction-aware. No existing work achieves all three properties together, which represents a real gap in the literature.

But there's a critical challenge to address: why not simply filter out high-distraction passages as a preprocessing step before running AdaGReS on what remains? This two-stage approach would be much simpler, so the proposal needs to make a compelling case for why integrating distraction directly into the optimization is superior to this straightforward alternative.

I'm also questioning the practical constraints. The theoretical contribution relies on proving γ-weak DR-submodularity under "bounded-embedding conditions," but those conditions need precise definition—if they're too restrictive or only apply to specific embedding distributions, the real-world applicability becomes questionable. Additionally, computing DE_q(p|S\{p}) for each passage requires querying the LLM with every possible remaining set, which balloons the computational cost to at least O(n²) LLM calls during the greedy algorithm.

The proposal could strengthen its novelty by highlighting that distraction operates as a fundamentally non-decomposable property—something that can't be easily separated from the optimization process itself. set-level phenomenon - a passage that's distracting in isolation might not be distracting in the presence of other supporting passages. This is why the two-stage pipeline (filter then select) is provably suboptimal, and why joint optimization matters. This directly counters the trivial alternative.

2. **The CCBQP connection**: CCBQP explicitly asks whether adding a third penalty term breaks their landscape. This proposal could position itself as answering that open question - by showing that the γ-weakly DR-submodular framework provides guarantees even with the third (distraction) term.

3. **Significance framing**: The current framing is about RAG context composition. But the broader significance is about formalization of "when does adding more information hurt?" - this is relevant beyond RAG to any context engineering problem. The non-monotonicity insight has broader implications.

Now I'm looking at the objective function more carefully. The distraction term is conditioned on the rest of the set, meaning a passage's distracting effect depends on what else is selected - that's what creates the non-monotonicity and makes this computationally interesting. But I need to verify whether the original Distracting Effect paper defines this as a set-conditional score or just a per-passage metric, since my initial understanding might be off. proposal writes DE_q(p|S\{p}), which is a set-conditional version. This is an extension of the original DE_q(p). But this raises a question: is the set-conditional version well-defined? How do you compute it efficiently?

Actually, this is interesting. The proposal seems to be proposing a set-conditional version of DE_q, which is novel but also raises computational concerns. But computational concerns are for the补救 agent.

Let me focus on my role - idea-level insights:

**Key Discovery Points:**

1. **Sharpen the "distraction ≠ redundancy" insight**: The strongest novelty claim is the formal decomposition. The proposal should make a crystal-clear argument about WHY these are fundamentally different penalties that cannot be collapsed. Redundancy wastes tokens when two passages say the same thing, but distraction actively interferes with answer generation—a qualitatively different failure mode. The most compelling evidence would be examples where these two diverge most sharply.

2. **The trivial alternative threat**: The two-stage pipeline (filter distractors → monotone submodular selection) is the main competitor. The key argument for joint optimization: distraction is context-dependent, so a passage might be distracting in isolation but not when paired with supporting passages, meaning you can't filter it independently.

3. **CCBQP open question**: The proposal can explicitly position itself as answering CCBQP's open question about adding a third penalty term.

4. **Broader significance**: The non-monotonicity insight (adding information can hurt) is fundamental to context engineering beyond RAG.

There's meaningful discovery space here, particularly around sharpening the distraction-redundancy distinction and making a stronger case against the simpler two-stage alternative.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6831cc9c-6b1f-43aa-8dc1-cc2f4e8391ba",
  "isSidechain": false,
  "requestId": "req_011CbYK4n5BmhMakjUQdLU2j",
  "type": "assistant",
  "uuid": "642a8b8e-39e3-4bf4-af06-02892cd5cdf1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ShnYVuJ3rNDi2Rsqy7y3b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 29314,
      "output_tokens": 5866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5866,
          "cache_read_input_tokens": 29314,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 52 · 2026-05-30T06:55:03.124Z_

Now I have a comprehensive view of the landscape. Let me compile my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- [AdaGReS, arXiv:2512.25052](https://arxiv.org/abs/2512.25052) (Dec 2025): 证明了 redundancy-penalized context selection 的 ε-approximate submodularity，但仅处理 monotone 目标函数。仅在 NQ 和一个生物医学语料库上评估，benchmark 覆盖有限。核心贡献是 closed-form adaptive β* 消除手动调参。
- [The Distracting Effect, ACL 2025](https://aclanthology.org/2025.acl-long.892/): 定义了 per-passage DE_q(p) 作为连续 distraction 度量（非二元分类），但这是一个 **个体 passage 级别** 的度量，不做 set-level 优化，也不考虑 passage 间的交互效应。
- [γ-weakly DR-submodular, arXiv:2601.00611](https://arxiv.org/abs/2601.00611) (AAMAS 2026): 提供了非单调 γ-weakly DR-submodular 函数的 Frank-Wolfe + double-greedy 近似保证（γ=1 时恢复 0.401 近似比），但零 NLP 实证应用，纯理论工作。
- [CCBQP, arXiv:2604.02554](https://arxiv.org/abs/2604.02554) (Apr 2026): Frank-Wolfe + landscape analysis 用于 relevance-diversity trade-off，**作者在论文中明确提出 open question：添加第三个 penalty term 是否会破坏其 clean quadratic landscape**。这是 proposal 可以直接回应的已发表 open problem。
- [LDAR, ICLR 2026](https://openreview.net/forum?id=c8CZWLy4T4): Distraction-aware 但在 retrieval time 操作，不是 post-retrieval composition，无近似保证。
- [DynamicRAG, NeurIPS 2025](https://openreview.net/forum?id=NuCtKoflsV): RL + LLM feedback 动态调整 k 和排序，7 个 benchmark 上 SOTA，但完全是 learned 方法，无理论保证。
- [SMART-RAG, arXiv:2409.13992](https://arxiv.org/abs/2409.13992) (Sep 2024): DPP-based 同时建模 relevance, diversity, conflict，training-free，但没有 distraction 概念，没有非单调优化保证。
- [OptiSet, arXiv:2601.05027](https://arxiv.org/abs/2601.05027) (Jan 2026): Set-centric 的 expand-then-refine 框架，用 self-synthesis 生成 preference labels，但无 formal optimization guarantees。
- [Context-Picker, arXiv:2512.14465](https://arxiv.org/abs/2512.14465) (Dec 2025): 两阶段 RL（先提高 recall，再剪裁冗余），本质是 learned pipeline 而非 principled optimization。
- [Jina Submodular Blog](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/) (Jul 2025): 工程实践层面将 submodular optimization 用于 passage reranking，但无理论分析，也无 distraction 建模。
- [AdaGATE, arXiv:2605.05245](https://arxiv.org/abs/2605.05245) (May 2026): 面向 multi-hop RAG 的 training-free evidence controller，用 utility-based selection 平衡 gap coverage / novelty / redundancy，但不建模 distraction，也无 submodular 理论保证。

**调研总结**：这个领域当前存在一个被明确感知但尚未被形式化解决的 gap——formal optimization guarantees 和 distraction-awareness 是两个不相交的阵营。所有有理论保证的方法（AdaGReS、CCBQP、SMART-RAG/DPP）都只建模 relevance-redundancy/diversity trade-off；所有 distraction-aware 的方法（LDAR、DynamicRAG、Context-Picker）都依赖 learned approaches 而无 formal bounds。这个 proposal 的核心定位——bridging this gap——在调研后确认是真实的、尚未被其他工作占据的。

---

【发掘点 1】
- 维度: trivial alternative 威胁
- 内容: 这个 proposal 面临一个必须正面回应的 trivial alternative：**两阶段 pipeline——先过滤高 distraction passages（用 DE_q 阈值剔除），再对剩余 passages 运行 AdaGReS 的 monotone submodular greedy**。这个方案实现简单、不需要任何新理论（复用 AdaGReS 现有保证），看起来就能同时 "distraction-aware" 且 "有 formal bounds"。如果 proposal 不主动论证 joint optimization 优于这个 pipeline，审稿人几乎一定会提出。**核心反驳必须建立在 "distraction 是 context-dependent" 这个论点上**：一个 passage 在孤立评估时可能看起来有 distraction（DE_q 单独评估值高），但在特定 passage 组合中可能反而提供了有价值的 disambiguation cue；反过来，一个 DE_q 个体评估安全的 passage 在某些组合中可能触发 distraction。proposal 的目标函数中写了 DE_q(p|S\{p})——set-conditional 版本——但需要用具体 case 或 toy example 说明为什么这种 context-dependency 在实际中是 substantial 而非 marginal 的。
- 价值: 直接回应最强的 trivial alternative 威胁，是 novelty 成立的前提条件。如果 pipeline 方案效果接近，整个非单调理论框架的 incremental value 就被质疑。（命中 Novelty）
- 调研依据: AdaGReS 提供了 monotone greedy 的现成保证；The Distracting Effect 的 DE_q 定义本身是 per-passage 的（非 set-conditional），这使得 "先过滤再选择" 成为一个自然的 baseline。

【发掘点 2】
- 维度: significance 提升
- 内容: proposal 目前将自身定位为 "post-retrieval RAG context composition" 的优化，这个 framing 虽然准确但 **significance 天花板受限于 RAG pipeline 的一个环节**。更有力的 framing 是将核心贡献抽象为回答一个更根本的问题：**"when does adding more information provably hurt, and how can we formally characterize the boundary?"** 这不仅仅是 RAG 的问题——它是 context engineering 的核心张力（所有 in-context learning、tool-use composition、multi-document summarization 都面对同样的 non-monotonicity）。Proposal 可以在 Introduction 中先建立这个 broader problem 的重要性，再 instantiate 到 RAG 场景。这样做的好处是：(1) 让 AAAI 更广泛的 AI 审稿人（不仅是 NLP/RAG track）能 appreciate 这个工作；(2) 将 distraction-redundancy decomposition 定位为一个 general-purpose 的分析框架而非 RAG-specific trick。
- 价值: 显著提升 significance 维度的评分。"A general formalization of when more context hurts" 的 appeal 远大于 "a better RAG passage selector"。（命中 Significance）
- 调研依据: Jina 的 submodular optimization blog 已经在工程实践层面将 submodular context selection 推广到 text selection 和 passage reranking；OptiSet 也在 set selection 而非仅 ranking 层面思考问题。领域趋势已经在走向 "context composition as a first-class optimization problem"，proposal 可以 ride 这个 trend 并提供 formal underpinning。

【发掘点 3】
- 维度: related work 差异化
- 内容: proposal 应该**显式回应 CCBQP 的 open question**。CCBQP 论文中作者明确提问 "添加第三个 penalty term 是否会破坏 clean quadratic landscape"，这是一个已发表的 open problem。proposal 的工作本质上在回答这个问题——答案是 "会破坏 monotonicity，但可以通过 γ-weakly DR-submodular 框架恢复近似保证"。将这个联系在 Introduction 或 Related Work 中明确写出来有两个好处：(1) 给出一个 concrete, published motivation，比泛泛说 "two camps haven't been combined" 更有说服力；(2) 让审稿人看到这个工作不是 arbitrary combination，而是在解决一个该领域的研究者已经在问但还没回答的问题。
- 价值: 大幅强化 novelty 叙事的说服力——从 "我们把三个东西组合了" 升级为 "我们回答了一个已发表的 open question"。（命中 Novelty + Related Work 差异化）
- 调研依据: CCBQP (arXiv:2604.02554) 作者明确提出这一 open question。

【发掘点 4】
- 维度: 前提假设质疑
- 内容: proposal 的理论核心是证明 f(S) 满足 γ-weak DR-submodularity "under bounded-embedding conditions"。但这个前提假设的实际约束力目前是不透明的。**如果 bounded-embedding conditions 过于严格（例如要求 embedding 均匀分布在单位球上，或要求 pairwise similarity 有某个上界），则现实中的 embedding 分布（通常是 clustered, anisotropic 的）可能不满足这些条件**。proposal 的可信度关键在于：(1) 明确写出 bounded-embedding conditions 的具体数学形式；(2) 验证主流 embedding 模型（如 Qwen3-Embedding-8B）在典型 benchmark 上的 embedding 分布是否 empirically 满足这些条件（例如统计 pairwise similarity 的分布、embedding norm 的集中程度等）。如果条件过强而实际不满足，则近似保证变成 vacuous guarantee——理论正确但实际无用。
- 价值: 直接关系到核心理论贡献是否 sound。如果 bounded-embedding conditions 被审稿人认为过于严格或不现实，整篇论文的理论 contribution 会被视为 toy result。（命中 Novelty——理论 novelty 的实际价值取决于条件的 tightness）
- 调研依据: γ-weakly DR-submodular 论文 (AAMAS 2026) 的保证依赖于 γ 的具体取值，而 γ 由目标函数的具体形式决定。AdaGReS 的 ε-approximate submodularity 证明依赖于 embedding similarity 的有界性假设，但那是 monotone case，非 monotone case 对条件的要求可能更强。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: proposal 目前的 claim 是 "first method simultaneously post-retrieval, formally grounded, and distraction-aware"。这个 claim 的 "formally grounded" 部分可以进一步锐化。当前领域中的 learned approaches（DynamicRAG、LDAR、Context-Picker）虽然 empirically strong，但有一个根本性局限：**它们的 generalization 完全依赖于训练分布，面对 distribution shift（新 domain、新 LLM、新 retriever）时没有任何保证**。Proposal 可以强化以下对比：submodular 框架提供的是 **distribution-free, model-agnostic** 的近似保证——不管 embedding 来自哪个模型、不管 generator 是什么 LLM，只要 γ-weak DR-submodularity 条件满足，近似比就成立。这与 learned approaches 的 "在训练分布上效果好但换个 domain 可能崩溃" 形成鲜明对比。这个差异化 angle 比 "有 formal bounds" 更具体、更有说服力。
- 价值: 将 "formally grounded" 从一个 abstract 属性强化为一个具有 practical implication 的优势——distribution-free generalization。（命中 Novelty + Significance）
- 调研依据: DynamicRAG 用 RL 在特定 benchmark 上训练；LDAR 通过 learning distraction-aware retriever 也需要训练数据。Context-Picker 的两阶段 RL 同样 distribution-dependent。这些方法在 cross-domain transfer 上的表现均未被验证。

Sources:
- [AdaGReS](https://arxiv.org/abs/2512.25052)
- [The Distracting Effect](https://aclanthology.org/2025.acl-long.892/)
- [γ-weakly DR-submodular](https://arxiv.org/abs/2601.00611)
- [CCBQP](https://arxiv.org/abs/2604.02554)
- [LDAR](https://openreview.net/forum?id=c8CZWLy4T4)
- [DynamicRAG](https://openreview.net/forum?id=NuCtKoflsV)
- [SMART-RAG](https://arxiv.org/abs/2409.13992)
- [OptiSet](https://arxiv.org/abs/2601.05027)
- [Context-Picker](https://arxiv.org/abs/2512.14465)
- [Jina Submodular Blog](https://jina.ai/news/submodular-optimization-for-text-selection-passage-reranking-context-engineering/)
- [AdaGATE](https://arxiv.org/abs/2605.05245)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "642a8b8e-39e3-4bf4-af06-02892cd5cdf1",
  "isSidechain": false,
  "requestId": "req_011CbYK4n5BmhMakjUQdLU2j",
  "type": "assistant",
  "uuid": "df9a9928-7916-4db7-a794-09250e69ac76",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_adversarial",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014ShnYVuJ3rNDi2Rsqy7y3b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 772,
      "cache_read_input_tokens": 29314,
      "output_tokens": 5866,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 772,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5866,
          "cache_read_input_tokens": 29314,
          "cache_creation_input_tokens": 772,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 772
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "df9a9928-7916-4db7-a794-09250e69ac76",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# Non-Monotone Submodular Context Composition with Distraction-Redundancy Decomposition  ## Core Problem  How can post-retrieval context composition for RAG be formalized as a constrained non-monotone…",
  "leafUuid": "df9a9928-7916-4db7-a794-09250e69ac76",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Non-monotone submodular RAG context composition",
  "sessionId": "f988eca0-c845-4095-a440-89da68837519"
}
```

---
