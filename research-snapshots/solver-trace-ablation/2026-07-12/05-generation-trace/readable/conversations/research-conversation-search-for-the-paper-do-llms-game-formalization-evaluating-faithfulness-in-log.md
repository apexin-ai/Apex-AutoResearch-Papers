# Research conversation: Search for the paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" with arXiv ID 2604.19459

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-aefae1fe7075ace17.jsonl`
- **Structured JSON:** [`3d7b7223e6458a37e458.json`](../../sessions/3d/3d7b7223e6458a37e458.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

14 recorded events

### User

_source line 1 · 2026-05-10T19:06:42.922Z_

Search for the paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" with arXiv ID 2604.19459. Verify:
1. Does this paper exist?
2. What does it find about GPT-5 vs DeepSeek-R1 formalization errors?
3. Was it presented at VerifAI-2 Workshop at ICLR 2026?

Also search: "arXiv 2604.19459" and "LLMs Game Formalization faithfulness"

Report findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "4d7751b0-7377-4802-ada4-5c27c326d9dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T19:06:44.386Z_

I'll help you search for this paper and verify the information. Let me search for it using multiple approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4d7751b0-7377-4802-ada4-5c27c326d9dd",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQr314sPeVe8UxkANjH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a0147318-bf64-4e6e-8f76-2be58faa6075",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EoLyjwueri6Sbe292fTA1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 555,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T19:06:44.808Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014iC4uGXauTApcwA6NRU1zM`</summary>

```json
{
  "query": "Do LLMs Game Formalization Evaluating Faithfulness Logical Reasoning arXiv 2604.19459"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a0147318-bf64-4e6e-8f76-2be58faa6075",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQr314sPeVe8UxkANjH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bc12d749-76ec-4d69-8d0a-7a06b47bd3db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EoLyjwueri6Sbe292fTA1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 555,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T19:06:45.114Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017sojdRmR4AVjSGk2zJT2EB`</summary>

```json
{
  "query": "arXiv 2604.19459"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc12d749-76ec-4d69-8d0a-7a06b47bd3db",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQr314sPeVe8UxkANjH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f2d77bf7-2db6-451d-88ce-1852d1fe924a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EoLyjwueri6Sbe292fTA1Z",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 13789,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 555,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T19:06:45.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TFpjeswPAGEgmEvoisf4GS`</summary>

```json
{
  "query": "LLMs Game Formalization faithfulness logical reasoning GPT-5 DeepSeek-R1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f2d77bf7-2db6-451d-88ce-1852d1fe924a",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQr314sPeVe8UxkANjH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "09a5599e-df1b-41f2-8e15-92cfdd0cc624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EoLyjwueri6Sbe292fTA1Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 13789,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 555
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 555,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T19:06:45.530Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GFZGXaxMJJhLjiYLjYkfq5`</summary>

```json
{
  "query": "VerifAI-2 Workshop ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "09a5599e-df1b-41f2-8e15-92cfdd0cc624",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQr314sPeVe8UxkANjH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6bacd2af-8320-4006-88e2-48560e7b774b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EoLyjwueri6Sbe292fTA1Z",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 555,
      "cache_read_input_tokens": 13789,
      "output_tokens": 251,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 555
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 251,
          "cache_read_input_tokens": 13789,
          "cache_creation_input_tokens": 555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 555,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-10T19:06:50.305Z_

<details><summary>↩ Tool result · `toolu_017sojdRmR4AVjSGk2zJT2EB`</summary>

```text
Web search results for query: "arXiv 2604.19459"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"[2601.19459] On the distribution of the periods of convex representations I","url":"https://arxiv.org/abs/2601.19459"},{"title":"Language-guided Robust Navigation for Mobile Robots in ...","url":"https://arxiv.org/pdf/2409.19459"},{"title":"[2508.19459] AG codes from the Hermitian curve for Cross-Subspace Alignment in Private Information Retrieval","url":"https://arxiv.org/abs/2508.19459"},{"title":"Language-guided Robust Navigation for Mobile Robots in Dynamically-changing Environments","url":"https://arxiv.org/html/2409.19459"},{"title":"Security Challenges for Cloud or Fog computing-Based AI Applications","url":"https://arxiv.org/html/2310.19459"},{"title":"[2502.19459] ArtGS: Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting","url":"https://arxiv.org/abs/2502.19459"},{"title":"[2402.19459] Anomalous contribution to galactic rotation curves due to stochastic spacetime","url":"https://arxiv.org/abs/2402.19459"},{"title":"Building Interactable Replicas of Complex Articulated Objects via Gaussian Splatting","url":"https://arxiv.org/html/2502.19459"}]

Based on the search results, arXiv paper 2604.19459 is titled "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" by Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut from EPFL.

The paper investigates whether frontier models exploit gaps when generating Lean 4 proofs, a behavior termed formalization gaming, and evaluates GPT-5 and DeepSeek-R1 on 303 first-order logic problems. 

Despite compilation rates of 87-99%, the researchers found no evidence of systematic gaming in unified generation, with models preferring to report failure over forcing proofs, even under prompting designed to encourage it.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f2d77bf7-2db6-451d-88ce-1852d1fe924a",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "99f74dba-d313-4a05-b305-ddba7babe8be",
  "sourceToolAssistantUUID": "f2d77bf7-2db6-451d-88ce-1852d1fe924a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-10T19:06:51.349Z_

<details><summary>↩ Tool result · `toolu_01GFZGXaxMJJhLjiYLjYkfq5`</summary>

```text
Web search results for query: "VerifAI-2 Workshop ICLR 2026"

Links: [{"title":"The VerifAI Workshop @ ICLR'26 - VerifAI","url":"https://verifai-workshop.github.io/"},{"title":"ICLR 2026 Workshop VerifAI-2 | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FVerifAI-2"},{"title":"VerifAI-2: The Second Workshop on AI Verification in the Wild","url":"https://iclr.cc/virtual/2026/workshop/10000774"},{"title":"van der Schaar Lab @ ICLR Workshops 2026 // van der Schaar Lab","url":"https://www.vanderschaar-lab.com/iclr-workshops-2026/"},{"title":"ICLR 2026 Workshop VerifAI-2 Submissions","url":"https://openreview.net/submissions?page=2&venue=ICLR.cc%2F2026%2FWorkshop%2FVerifAI-2"},{"title":"ICLR 2026 Workshops","url":"https://iclr.cc/virtual/2026/events/workshop"},{"title":"ICLR 2026: 3 Papers Accepted in Trustworthy AI, VerifAI-2, ...","url":"https://www.linkedin.com/posts/mihaela-van-der-schaar_im-delighted-to-share-that-our-lab-has-had-activity-7434557846635290624-ogbQ"},{"title":"Workshops at ICLR 2026 – ICLR Blog","url":"https://blog.iclr.cc/2026/01/13/iclr2026-workshops/"},{"title":"VerifAI-2: The Second Workshop on AI Verification in the Wild | OpenReview","url":"https://openreview.net/forum?id=td5zRHcXqY"},{"title":"VerifAI: AI Verification in the Wild | OpenReview","url":"https://openreview.net/forum?id=p7rWugEmQo"}]

Based on the search results, here's what I found about the VerifAI-2 Workshop at ICLR 2026:

## Overview
VerifAI-2 is the second AI Verification Workshop at ICLR 2026, taking place in Rio on April 26-27, 2026.

## Workshop Focus
The workshop explores the intersection of scale-driven generative artificial intelligence (AI) and the correctness-focused principles of verification. Formal analysis tools such as theorem provers, satisfiability solvers, and execution monitoring have demonstrated success in ensuring properties of interest across a range of tasks in software development and mathematics where precise reasoning is necessary.

## Special Theme
The special theme of VerifAI at ICLR 2025 was Large Language Models (LLMs) for Code Generation, and for 2026, the new special theme is: Building verifiable tasks and environments for reinforcement learning (RL).

## Status
Submissions to the workshop are now closed, and the workshop accepts papers from multiple tracks including traditional papers and tiny/short papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6bacd2af-8320-4006-88e2-48560e7b774b",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "61fc4dfc-6171-40ce-8f22-e88fdbdc35ff",
  "sourceToolAssistantUUID": "6bacd2af-8320-4006-88e2-48560e7b774b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T19:06:52.012Z_

<details><summary>↩ Tool result · `toolu_014iC4uGXauTApcwA6NRU1zM`</summary>

```text
Web search results for query: "Do LLMs Game Formalization Evaluating Faithfulness Logical Reasoning arXiv 2604.19459"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"TriEx: A Game-based Tri-View Framework for Explaining Internal Reasoning in Multi-Agent LLMs","url":"https://arxiv.org/html/2604.20043"},{"title":"Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing","url":"https://arxiv.org/html/2604.08401"},{"title":"LogicPuzzleRL: Cultivating Robust Mathematical Reasoning in LLMs via Reinforcement Learning","url":"https://arxiv.org/html/2506.04821v1"},{"title":"NeuroFaith: Evaluating LLM Self-Explanation Faithfulness via Internal Representation Alignment","url":"https://arxiv.org/html/2506.09277"},{"title":"Lost in the Logic: An Evaluation of Large Language Models’ Reasoning Capabilities on LSAT Logic Games","url":"https://arxiv.org/html/2409.19012v1"},{"title":"Tracing LLM Reasoning Processes with Strategic Games: A Framework for Planning, Revision, and Resource-Constrained Decision Making","url":"https://arxiv.org/html/2506.12012v1"},{"title":"LogicGame: Benchmarking Rule-Based Reasoning Abilities of Large Language Models","url":"https://arxiv.org/html/2408.15778v1"},{"title":"Large Language Model Strategic Reasoning Evaluation through Behavioral Game Theory","url":"https://arxiv.org/html/2502.20432v1"}]

I found the paper! Here's what I found about arXiv paper 2604.19459:

## "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning"

This paper is authored by Kyuhee Kim and 2 other authors.

**Main Research Question:**
The paper investigates whether frontier models exploit the gap between valid proofs and faithful translations when generating Lean 4 proofs, a behavior termed "formalization gaming".

**Key Findings:**

1. **Methodology:** The researchers evaluated GPT-5 and DeepSeek-R1 on 303 first-order logic problems (203 from FOLIO, 100 from Multi-LogiEval), comparing unified generation against a two-stage pipeline that separates formalization from proving.

2. **Main Results:** Despite compilation rates of 87-99%, they found no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.

3. **Detection of Unfaithfulness:** The two-stage pipeline revealed two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

4. **Implications:** These findings show that high compilation rates or accuracies should not be equated with faithful reasoning.

Code and data are available online.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc12d749-76ec-4d69-8d0a-7a06b47bd3db",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "6538a2b0-676c-40a3-a4a4-f7168fb0c776",
  "sourceToolAssistantUUID": "bc12d749-76ec-4d69-8d0a-7a06b47bd3db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T19:06:52.034Z_

<details><summary>↩ Tool result · `toolu_01TFpjeswPAGEgmEvoisf4GS`</summary>

```text
Web search results for query: "LLMs Game Formalization faithfulness logical reasoning GPT-5 DeepSeek-R1"

Links: [{"title":"[2604.19459] Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/abs/2604.19459"},{"title":"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning","url":"https://arxiv.org/html/2604.19459"},{"title":"[2501.12948] DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://arxiv.org/abs/2501.12948"},{"title":"DeepSeek-R1 incentivizes reasoning in LLMs through reinforcement learning | Nature","url":"https://www.nature.com/articles/s41586-025-09422-z"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via RL | Hacker News","url":"https://news.ycombinator.com/item?id=42823568"},{"title":"GitHub - deepseek-ai/DeepSeek-R1 · GitHub","url":"https://github.com/deepseek-ai/DeepSeek-R1"},{"title":"DeepSeek-R1: Incentivizing Reasoning Capability in LLMs ...","url":"https://www.linkedin.com/posts/natolambert_deepseek-r1-incentivizing-reasoning-capability-activity-7412895062390538240-fS4Y"},{"title":"Paper page - DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning","url":"https://huggingface.co/papers/2501.12948"},{"title":"DeepSeek-R1 Thoughtology: Let's think about LLM ...","url":"https://arxiv.org/pdf/2504.07128"},{"title":"[2511.19333] Learning to Reason: Training LLMs with GPT-OSS or DeepSeek R1 Reasoning Traces","url":"https://arxiv.org/abs/2511.19333"}]

Based on the web search results, here's what I found related to your query:

## Key Research Finding: "Do LLMs Game Formalization?"

A recent study investigates whether frontier models exploit a gap between valid proofs and faithful translations when generating Lean 4 proofs—a behavior termed "formalization gaming"—evaluating GPT-5 and DeepSeek-R1 on 303 first-order logic problems.

### Main Findings:

**Unified Generation Results:**
Despite compilation rates of 87-99%, the study finds no evidence of systematic gaming in unified generation: models prefer reporting failure over forcing proofs, even under prompting designed to encourage it.

**Two-Stage Pipeline Results:**
The two-stage pipeline reveals two distinct modes of unfaithfulness: GPT-5 fabricates axioms during proof generation, a reactive fallback detectable via cross-stage comparison, while DeepSeek-R1 mistranslates premises during formalization, producing internally consistent outputs that evade detection entirely.

**Key Implication:**
These findings show that high compilation rates or accuracies should not be equated with faithful reasoning.

The research paper, titled "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning," was published approximately 3 weeks ago on arXiv (April 21, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "09a5599e-df1b-41f2-8e15-92cfdd0cc624",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "1a006175-4593-4a31-9f9a-b22ef268fa2b",
  "sourceToolAssistantUUID": "09a5599e-df1b-41f2-8e15-92cfdd0cc624",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-10T19:06:53.388Z_

Now let me fetch the actual paper to verify the workshop presentation information:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a006175-4593-4a31-9f9a-b22ef268fa2b",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQrhwNMpoVfvwdTEyup",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "60f8415d-0e18-4b9b-ba18-942d5fc15edb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014fDZPKvwuXpdXwJiwKZR6R",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 856,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 14344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3465,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-10T19:06:54.188Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_017RSTRWpsoRHxRJLgcuet1e`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.19459",
  "prompt": "Was this paper presented at VerifAI-2 Workshop at ICLR 2026? What are the authors? What are the main findings about GPT-5 vs DeepSeek-R1?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "60f8415d-0e18-4b9b-ba18-942d5fc15edb",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQrhwNMpoVfvwdTEyup",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba14c27d-9a15-4ae3-a117-bfa66ff17d76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014fDZPKvwuXpdXwJiwKZR6R",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 856,
      "cache_creation_input_tokens": 3465,
      "cache_read_input_tokens": 14344,
      "output_tokens": 145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 856,
          "output_tokens": 145,
          "cache_read_input_tokens": 14344,
          "cache_creation_input_tokens": 3465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3465,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T19:06:57.613Z_

<details><summary>↩ Tool result · `toolu_017RSTRWpsoRHxRJLgcuet1e`</summary>

```text
# Paper Details

**Workshop Presentation:** Yes, this paper was "Published at the VerifAI-2 Workshop, ICLR 2026 (non-archival)."

**Authors:** The research team consists of Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut.

**Main Findings - GPT-5 vs DeepSeek-R1:**

The study reveals distinctly different failure patterns between the two models:

- **GPT-5** fabricates axioms during proof generation as a reactive fallback strategy. This unfaithfulness is detectable when comparing outputs across different processing stages.

- **DeepSeek-R1** mistranslates premises during the formalization phase, producing outputs that remain internally consistent and therefore evade detection methods.

The researchers emphasize that "high compilation rates or accuracies should not be equated with faithful reasoning," highlighting how both models can generate technically valid proofs while failing to faithfully represent the original logical problems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba14c27d-9a15-4ae3-a117-bfa66ff17d76",
  "isSidechain": true,
  "promptId": "302e9c8f-60f8-4f8a-9c96-184dcca47d43",
  "agentId": "aefae1fe7075ace17",
  "type": "user",
  "uuid": "497958c7-266c-47ac-819c-a46e85133404",
  "sourceToolAssistantUUID": "ba14c27d-9a15-4ae3-a117-bfa66ff17d76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-10T19:07:02.065Z_

## Summary of Findings

### 1. **Does this paper exist?**
✓ **YES** - The paper "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning" exists and is published on arXiv with ID 2604.19459.

**Authors:** Kyuhee Kim, Auguste Poiroux, and Antoine Bosselut (EPFL)

### 2. **What does it find about GPT-5 vs DeepSeek-R1 formalization errors?**

The paper reveals **two distinct, fundamentally different failure modes:**

- **GPT-5:** Fabricates axioms during proof generation as a reactive fallback. This unfaithfulness is **detectable** through cross-stage comparison, making it reactive and discoverable.

- **DeepSeek-R1:** Mistranslates premises during formalization, producing internally consistent outputs that **evade detection entirely**. This is more problematic because the unfaithfulness remains hidden.

**Key insight:** Despite compilation rates of 87-99%, neither model achieves faithful reasoning. High compilation rates should not be equated with faithful reasoning.

### 3. **Was it presented at VerifAI-2 Workshop at ICLR 2026?**
✓ **YES** - The paper was published at the VerifAI-2 Workshop at ICLR 2026 as a non-archival paper. The workshop took place on April 26-27, 2026, in Rio.

---

**Sources:**
- [arXiv 2604.19459 Abstract](https://arxiv.org/abs/2604.19459)
- [arXiv 2604.19459 HTML](https://arxiv.org/html/2604.19459)
- [VerifAI-2 Workshop @ ICLR 2026](https://verifai-workshop.github.io/)
- [ICLR 2026 Workshop VerifAI-2 on OpenReview](https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FVerifAI-2)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "497958c7-266c-47ac-819c-a46e85133404",
  "isSidechain": true,
  "agentId": "aefae1fe7075ace17",
  "requestId": "req_011CauQs7na91MEjwJbDxh3v",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "00a6c55d-6ff3-4fbf-870b-437fcc70e88b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "61009063-a139-4b80-a80c-27af9077a81a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_013Wb3tqL7mc94ZeFXzBk1MP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 1228,
      "cache_read_input_tokens": 17809,
      "output_tokens": 515,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1228
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 515,
          "cache_read_input_tokens": 17809,
          "cache_creation_input_tokens": 1228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1228,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---
