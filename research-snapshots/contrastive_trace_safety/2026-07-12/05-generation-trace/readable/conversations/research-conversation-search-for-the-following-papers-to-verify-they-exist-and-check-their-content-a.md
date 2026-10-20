# Research conversation: Search for the following papers to verify they exist and check their content. Also search for competing/related work. 1.

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 9
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-ac72cbccf5bf967e0.jsonl`
- **Structured JSON:** [`794bf1308c9ca4f3f0b4.json`](../../sessions/79/794bf1308c9ca4f3f0b4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

22 recorded events

### User

_source line 1 · 2026-05-10T05:38:29.715Z_

Search for the following papers to verify they exist and check their content. Also search for competing/related work.

1. Search for "arXiv 2504.04372" - "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models" (ICST 2026)
2. Search for "arXiv 2505.10443" - "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"
3. Search for "arXiv 2601.18044" - "Reasoning Guided Fault Localization for LLM-Based Automated Program Repair" (RGFL)
4. Search for "arXiv 2604.05481" - "On the Role of Fault Localization Context for LLM-Based Program Repair"
5. Search for "arXiv 2512.16956" - SpIDER paper
6. Search for "MACL-IRFL" - "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization"
7. Search for recent work (2025-2026) on: "contrastive learning fault localization LLM" and "code robustness semantic mutations fine-tuning"
8. Search for any work combining contrastive learning with fault localization in LLMs

Use web search for each. Report what you find: whether papers exist, their actual content/claims, and any competing/similar work you discover.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "c776309b-b08d-4857-883e-2be61afcfe1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T05:38:30.619Z_

I'll search for these papers and related work systematically using web search.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c776309b-b08d-4857-883e-2be61afcfe1d",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5fa5706b-7df3-4ddc-a0f3-2267ca8d73fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T05:38:31.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0144KZCfTEwFw5eWfNH4w6Uc`</summary>

```json
{
  "query": "arXiv 2504.04372 Assessing Impact Code Changes Fault Localizability LLM"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5fa5706b-7df3-4ddc-a0f3-2267ca8d73fe",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "007ad914-62ce-41ab-b109-15567fb3a726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T05:38:31.289Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AAkTdEzRrgk6c6kHaczwhJ`</summary>

```json
{
  "query": "arXiv 2505.10443 Large Language Models Robust Code Semantic Mutations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "007ad914-62ce-41ab-b109-15567fb3a726",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fea75311-6ed6-4573-b051-3e544352299e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T05:38:31.536Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fpraiw8RPTuRF7btvd19rK`</summary>

```json
{
  "query": "arXiv 2601.18044 Reasoning Guided Fault Localization LLM Program Repair RGFL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fea75311-6ed6-4573-b051-3e544352299e",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "631dd117-1d7d-4627-874c-2dbfc2c1e609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T05:38:31.875Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016V2Kdm7bAT7QrcqYWHrFbM`</summary>

```json
{
  "query": "arXiv 2604.05481 Fault Localization Context LLM Program Repair"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "631dd117-1d7d-4627-874c-2dbfc2c1e609",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9e1fd0ec-ff6e-4ad1-a001-bab640622a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T05:38:31.898Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012SH6cKRhjtWp1qRh6pbxbt`</summary>

```json
{
  "query": "arXiv 2512.16956 SpIDER"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e1fd0ec-ff6e-4ad1-a001-bab640622a5e",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bb424e3e-7a21-46f3-96fa-49252c9d5675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 762,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T05:38:31.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019MHCbThYVACgHZ6sdR4afH`</summary>

```json
{
  "query": "MACL-IRFL Multi-View Adaptive Contrastive Learning Information Retrieval Fault Localization"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bb424e3e-7a21-46f3-96fa-49252c9d5675",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMDPn5uTTQwwZHxPvsY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c59b9bfe-f0db-4485-806c-41bdcade01b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DTBpGQqUuBhtkDs199xfT7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 762,
      "cache_read_input_tokens": 16155,
      "output_tokens": 371,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 762
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 371,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 762,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 762,
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

_source line 9 · 2026-05-10T05:38:36.970Z_

<details><summary>↩ Tool result · `toolu_0144KZCfTEwFw5eWfNH4w6Uc`</summary>

```text
Web search results for query: "arXiv 2504.04372 Assessing Impact Code Changes Fault Localizability LLM"

Links: [{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2025arXiv250404372H/abstract"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/resources/2504.04372v3"},{"title":"Bytez","url":"https://bytez.com/docs/arxiv/2504.04372/paper"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://www.arxiv.org/pdf/2504.04372"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026 - Research Papers) - ICST 2026","url":"https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://zenodo.org/records/18803969"}]

Based on the search results, I found detailed information about the arXiv paper 2504.04372:

## Paper Summary

Generative Large Language Models (LLMs) are increasingly used in non-generative software maintenance tasks, such as fault localization (FL). This paper presents the first large-scale empirical investigation into the robustness of LLMs fault localizability.

## Research Approach

Inspired by mutation testing, the authors develop an end-to-end evaluation framework that addresses key limitations in existing LLM evaluation, including data contamination, scalability, automation, and extensibility. For each program an LLM localizes successfully, they apply semantic-preserving mutations (SPMs) and rerun localization to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics.

## Findings

The study evaluates 10 state-of-the-art LLMs on 750,013 fault localization tasks from over 1,300 Java and Python programs. The key finding is striking: SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, and that LLMs' reasoning on the code found earlier in the context is noticeably better.

These results suggest that LLMs' code-reasoning is tied to code features irrelevant to semantics. Overall, the findings motivate fundamental advances in how LLMs represent, interpret, and prioritize code semantics to reason more deeply about program logic.

The paper was accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "007ad914-62ce-41ab-b109-15567fb3a726",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "8cef59c6-fbbe-469a-ae19-d7ac5e615d51",
  "sourceToolAssistantUUID": "007ad914-62ce-41ab-b109-15567fb3a726",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T05:38:37.541Z_

<details><summary>↩ Tool result · `toolu_019MHCbThYVACgHZ6sdR4afH`</summary>

```text
Web search results for query: "MACL-IRFL Multi-View Adaptive Contrastive Learning Information Retrieval Fault Localization"

Links: [{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"[2409.12519] Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/abs/2409.12519"},{"title":"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/html/2409.12519"},{"title":"Improving Bug Localization with Word Embedding and Enhanced Convolutional Neural Networks | Request PDF","url":"https://www.researchgate.net/publication/327035783_Improving_Bug_Localization_with_Word_Embedding_and_Enhanced_Convolutional_Neural_Networks"},{"title":"Enhancing IR-based Fault Localization using Large Language Models","url":"https://arxiv.org/html/2412.03754"},{"title":"MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote ...","url":"http://121.43.168.64:10060/s/org/arxiv/G.https/pdf/2512.16294.pdf"},{"title":"MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval","url":"https://arxiv.org/html/2512.16294v1"},{"title":"Model-Aware Contrastive Learning: Towards Escaping the Dilemmas","url":"https://proceedings.mlr.press/v202/huang23c/huang23c.pdf"},{"title":"[2512.16294] MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval","url":"https://arxiv.org/abs/2512.16294"},{"title":"Enhancing IR-based Fault Localization using Large Language Models Shuai Shao","url":"https://arxiv.org/pdf/2412.03754"}]

Based on the search results, here's what I found about MACL-IRFL:

## MACL-IRFL Overview

MACL-IRFL (Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization) is a novel approach designed to learn relationships for software fault localization.

## Key Problem It Addresses

Most studies focused on information retrieval-based techniques for fault localization by building representations for bug reports and source code files and matching their semantic vectors through similarity measurement. However, such approaches often ignore useful information including: 1) the interaction relationship between bug reports and source code files; 2) the similarity relationship between bug reports; and 3) the co-citation relationship between source code files.

## Technical Approach

The method models bug reports, source code files, and the relationships between them as structured graphs from three views (i.e., report-code interaction view, report-report similarity view, and code-code co-citation view). These views provide auxiliary information that supplements the missing historical connections in the validation and test stages.

## Publication

The research was published in Automated Software Engineering in 2026. It's also available on arXiv as a preprint from September 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c59b9bfe-f0db-4485-806c-41bdcade01b4",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "538ed6e0-f0c4-41a4-bcd4-c66198d7e388",
  "sourceToolAssistantUUID": "c59b9bfe-f0db-4485-806c-41bdcade01b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T05:38:40.488Z_

<details><summary>↩ Tool result · `toolu_016V2Kdm7bAT7QrcqYWHrFbM`</summary>

```text
Web search results for query: "arXiv 2604.05481 Fault Localization Context LLM Program Repair"

Links: [{"title":"[2604.05481v1] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481v1"},{"title":"[2604.05481] On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/abs/2604.05481"},{"title":"On the Role of Fault Localization Context for LLM-Based Program Repair","url":"https://arxiv.org/html/2604.05481"},{"title":"GALA: Multimodal Graph Alignment for Bug Localization in Automated Program Repair","url":"https://arxiv.org/html/2604.08089"},{"title":"A Study on the Impact of Fault localization Granularity for Repository-Scale Code Repair Tasks","url":"https://arxiv.org/html/2604.00167"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"},{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"(PDF) A Preliminary Evaluation of LLM-Based Fault Localization","url":"https://www.researchgate.net/publication/373046756_A_Preliminary_Evaluation_of_LLM-Based_Fault_Localization"},{"title":"ARISE: A Repository-level Graph Representation and Toolset for Agentic Fault Localization and Program Repair","url":"https://arxiv.org/html/2605.03117"}]

Based on the search results, here's information about arXiv paper 2604.05481:

## Paper Overview

The paper is titled "On the Role of Fault Localization Context for LLM-Based Program Repair" by Melika Sepidband, Hung Viet Pham, and Hadi Hemmati, submitted on April 7, 2026.

## Research Question

Fault Localization (FL) is a key component of Large Language Model (LLM)-based Automated Program Repair (APR), yet its impact remains underexplored. In particular, it is unclear how much localization is needed, whether additional context beyond the predicted buggy location is beneficial, and how such context should be retrieved.

## Methodology

The researchers conducted a large-scale empirical study on 500 SWE-bench Verified instances using GPT-5-mini, evaluating 61 configurations that vary file-level, element-level, and line-level context.

## Key Findings

The results show that more context does not consistently improve repair performance. More specifically:

- File-level localization is the dominant factor, yielding a 15-17x improvement over a no-file baseline.
- Expanding file context is often associated with improved performance, with successful repairs most commonly observed in configurations with approximately 6-10 relevant files.
- Element-level context expansion provides conditional gains that depend strongly on the file context quality, while line-level context expansion frequently degrades performance due to noise amplification.
- LLM-based retrieval generally outperforms structural heuristics while using fewer files and tokens.

Overall, the most effective FL context strategy typically combines a broad semantic understanding at higher abstraction levels with precise line-level localization. These findings challenge the assumption that increasing the localization context uniformly improves APR, and provide practical guidance for designing LLM-based FL strategies.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9e1fd0ec-ff6e-4ad1-a001-bab640622a5e",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "5f5aa0c2-2981-4d18-bd57-646d15ac84b6",
  "sourceToolAssistantUUID": "9e1fd0ec-ff6e-4ad1-a001-bab640622a5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T05:38:40.493Z_

<details><summary>↩ Tool result · `toolu_01Fpraiw8RPTuRF7btvd19rK`</summary>

```text
Web search results for query: "arXiv 2601.18044 Reasoning Guided Fault Localization LLM Program Repair RGFL"

Links: [{"title":"[2601.18044] RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models","url":"https://arxiv.org/html/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair","url":"https://www.arxiv.org/pdf/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | alphaXiv","url":"https://www.alphaxiv.org/abs/2601.18044"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260118044S/abstract"},{"title":"RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models | Scilit","url":"https://www.scilit.com/publications/93a4ab9613be0ae41a0609c084a46a24"},{"title":"A Quantitative and Qualitative Evaluation of LLM-Based Explainable Fault Localization","url":"https://arxiv.org/html/2308.05487v3"},{"title":"[2403.10507] Demystifying Faulty Code with LLM: Step-by-Step Reasoning for Explainable Fault Localization","url":"https://arxiv.org/abs/2403.10507"},{"title":"Explainable Fault Localization for Programming ...","url":"https://arxiv.org/pdf/2509.25676"},{"title":"AgentFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/html/2403.16362v1"}]

I found the paper! Here's a summary of the research:

## RGFL: Reasoning Guided Fault Localization for Automated Program Repair

Fault Localization (FL) is a critical step in Automated Program Repair (APR), and its importance has increased with the rise of Large Language Model (LLM)-based repair agents. In realistic project-level repair scenarios, software repositories often span millions of tokens, far exceeding current LLM context limits. Consequently, models must first identify a small, relevant subset of code, making accurate FL essential for effective repair.

### Core Approach

The method introduces a hierarchical reasoning module that (i) generates structured, bug-specific explanations for candidate files and elements, and (ii) leverages these explanations in a two-stage ranking scheme combining LLM-based and embedding-based signals. For each file or element individually, the LLM explains its functionality, and this explanation is causally related to the reported symptom. By relying on natural language reasoning rather than raw code similarity, the LLM can better capture the semantic and causal connection between the bug report and potential fault locations, leading to more accurate localization.

### Integration and Evaluation

The reasoning module is integrated into the modular APR system, Agentless. The pipeline proceeds in four stages: (1) file localization using code+reasoning ranking, (2) element localization using reasoning within the top-k files (which they use k=3), (3) line localization, and (4) patch generation and validation.

### Results

On SWE-bench Verified, file-level Hit@1 improves from 71.4% to 85%, and MRR from 81.8% to 88.8%. At the element level, Exact Match under top-3 files increases from 36% to 69%. Integrating the localization into Agentless yields a 12.8% end-to-end repair success improvement.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "631dd117-1d7d-4627-874c-2dbfc2c1e609",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "01326225-adbe-4966-a234-49d2ca1dd0f1",
  "sourceToolAssistantUUID": "631dd117-1d7d-4627-874c-2dbfc2c1e609",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T05:38:42.362Z_

<details><summary>↩ Tool result · `toolu_01AAkTdEzRrgk6c6kHaczwhJ`</summary>

```text
Web search results for query: "arXiv 2505.10443 Large Language Models Robust Code Semantic Mutations"

Links: [{"title":"[2505.10443] Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/abs/2505.10443"},{"title":"Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?","url":"https://arxiv.org/html/2505.10443"},{"title":"Are Large Language Models Robust in Understanding Code Against","url":"https://arxiv.org/pdf/2505.10443"},{"title":"How Accurately Do Large Language Models Understand Code?","url":"https://arxiv.org/html/2504.04372v1"},{"title":"GitHub - xiaofangxd/LLM_EA: Evolutionary-Algorithm and Large-Language-Model · GitHub","url":"https://github.com/xiaofangxd/LLM_EA"},{"title":"[2505.14752v1] Large Language Models for Data Synthesis","url":"https://arxiv.org/abs/2505.14752v1"},{"title":"[2504.04372v1] How Accurately Do Large Language Models Understand Code?","url":"https://arxiv.org/abs/2504.04372v1"},{"title":"Identification and Optimization of Redundant Code Using Large Language Models","url":"https://arxiv.org/html/2505.04040"},{"title":"[2504.04372] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372"},{"title":"[2505.23404] MEF: A Capability-Aware Multi-Encryption Framework for Evaluating Vulnerabilities in Black-Box Large Language Models","url":"https://arxiv.org/abs/2505.23404"}]

I found the paper! Here's information about arXiv paper 2505.10443:

## Paper Overview

The paper is titled "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?" It was authored by Pedro Orvalho and Marta Kwiatkowska, submitted on May 15, 2025, with a revised version on August 8, 2025.

## Research Focus

The work evaluates whether state-of-the-art LLMs with up to 8B parameters can reason about Python programs or are simply guessing. While recent studies have assessed LLMs' ability to predict program outputs, most focus solely on the accuracy of those predictions, without evaluating the reasoning behind them. Moreover, it has been observed on mathematical reasoning tasks that LLMs can arrive at correct answers through flawed logic, raising concerns about similar issues in code understanding.

## Methodology

The researchers apply five semantics-preserving code mutations: renaming variables, mirroring comparison expressions, swapping if-else branches, converting for loops to while loops, and loop unrolling. These mutations maintain program semantics while altering its syntax. They evaluated six LLMs and performed a human expert analysis using LiveCodeBench to assess whether the correct predictions are based on sound reasoning, and also evaluated prediction stability across different code mutations on LiveCodeBench and CruxEval.

## Key Findings

The findings show that LLMs trained for code produce correct predictions based on flawed reasoning between 10% and 50% of cases. Furthermore, LLMs often change predictions in response to the code mutations, indicating they do not yet exhibit stable, semantically grounded reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fea75311-6ed6-4573-b051-3e544352299e",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "00a494d4-8056-4e2b-890a-9c5e3e773942",
  "sourceToolAssistantUUID": "fea75311-6ed6-4573-b051-3e544352299e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T05:38:43.889Z_

<details><summary>↩ Tool result · `toolu_012SH6cKRhjtWp1qRh6pbxbt`</summary>

```text
Web search results for query: "arXiv 2512.16956 SpIDER"

Links: [{"title":"[2512.16956] SpIDER: Spatially Informed Dense Embedding Retrieval for Software Issue Localization","url":"https://arxiv.org/abs/2512.16956"},{"title":"SpIDER: Spatially Informed Dense Embedding Retrieval for Software Issue Localization","url":"https://arxiv.org/html/2512.16956"},{"title":"SpIDER: Spatially Informed Dense Embedding Retrieval ...","url":"https://arxiv.org/pdf/2512.16956"},{"title":"[2512.17355] SPIDER, a Waveform Digitizer ASIC for picosecond timing in LHCb PicoCal","url":"https://arxiv.org/abs/2512.17355"},{"title":"[2603.16956] On the Extension Theorem for Packing Steiner Forests","url":"https://arxiv.org/abs/2603.16956"},{"title":"[2512.18805] Spider-Webb: Spatially-Resolved Evidence of Inside-Out Quenching in the Spiderweb Protocluster at $z \\sim 2$","url":"https://arxiv.org/abs/2512.18805"},{"title":"[2604.16956] Waves Everywhere: A Distributional Equation Approach to Front Propagation","url":"https://arxiv.org/abs/2604.16956"},{"title":"SPIDER: Scalable Physics-Informed Dexterous Retargeting","url":"https://arxiv.org/html/2511.09484v1"},{"title":"[1807.01695] SPIDER: Near-Optimal Non-Convex Optimization via Stochastic Path Integrated Differential Estimator","url":"https://arxiv.org/abs/1807.01695"},{"title":"Spider-Webb: Spatially-Resolved Evidence of Inside-Out Quenching in the Spiderweb Protocluster at 𝑧∼2","url":"https://arxiv.org/html/2512.18805"}]

Based on the search results, here's information about arXiv paper 2512.16956:

## SpIDER: Spatially Informed Dense Embedding Retrieval for Software Issue Localization

This paper addresses the challenge of retrieving code units (e.g., files, classes, functions) that are semantically relevant to a given user query, bug report, or feature request from large codebases for LLM-based coding agents.

### Key Contribution

SpIDER is an enhanced dense retrieval approach that incorporates LLM-based reasoning over auxiliary context obtained through graph-based exploration of the codebase.

### Problem It Addresses

While embedding-based approaches can outperform BM25 by large margins, they often lack exploration of the codebase and underutilize its underlying graph structure.

### Results

Empirical results show that SpIDER consistently improves dense retrieval performance across several programming languages.

### Additional Resource

The paper also introduces SpIDER-Bench, a graph-structured evaluation benchmark curated from SWE-PolyBench, SWEBench-Verified and Multi-SWEBench, encompassing Python, Java, JavaScript, and TypeScript repositories.

The paper was submitted to arXiv on December 18, 2025, with authors including Shravan Chaudhari and others.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bb424e3e-7a21-46f3-96fa-49252c9d5675",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "4b31ff58-29db-43c1-959a-d760083a5a8b",
  "sourceToolAssistantUUID": "bb424e3e-7a21-46f3-96fa-49252c9d5675",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T05:38:46.070Z_

Now let me search for the recent work on contrastive learning and code robustness:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4b31ff58-29db-43c1-959a-d760083a5a8b",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMESLf217N5zVrzzdDd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "91e4c36c-d619-48f6-923b-6a835353dd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H3jv2Ga5fe8YicVSfAJf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 5882,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5882,
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

_source line 16 · 2026-05-10T05:38:46.139Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UHyF65Uo2rEH6Hzb2vFiR8`</summary>

```json
{
  "query": "contrastive learning fault localization LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91e4c36c-d619-48f6-923b-6a835353dd2a",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMESLf217N5zVrzzdDd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "05fe5f2b-7875-44fd-96c7-74e23222d05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H3jv2Ga5fe8YicVSfAJf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 5882,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5882,
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

_source line 17 · 2026-05-10T05:38:46.568Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GhQfJ8qqVrhkeieYbRzc8e`</summary>

```json
{
  "query": "code robustness semantic mutations fine-tuning LLM 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05fe5f2b-7875-44fd-96c7-74e23222d05e",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMESLf217N5zVrzzdDd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bdf71397-96e3-43ee-ae6b-dbff6b7902b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H3jv2Ga5fe8YicVSfAJf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 5882,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5882,
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

_source line 18 · 2026-05-10T05:38:46.717Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Xt6ffdoodzmPa7StYFDBmy`</summary>

```json
{
  "query": "contrastive learning automated program repair LLM code understanding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bdf71397-96e3-43ee-ae6b-dbff6b7902b4",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMESLf217N5zVrzzdDd",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ba0bebb7-d038-42e9-ba30-5cb713317937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016H3jv2Ga5fe8YicVSfAJf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 865,
      "cache_creation_input_tokens": 5882,
      "cache_read_input_tokens": 16917,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5882,
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

### Tool result

_source line 19 · 2026-05-10T05:38:53.673Z_

<details><summary>↩ Tool result · `toolu_01UHyF65Uo2rEH6Hzb2vFiR8`</summary>

```text
Web search results for query: "contrastive learning fault localization LLM 2025 2026"

Links: [{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"GitHub - CHAOZHAO-1/LLM-based-PHM: This is a reposotory that includes paper about LLM-based fault diagnosis and prognosis. (基于大模型的故障诊断和预测，持续更新)","url":"https://github.com/CHAOZHAO-1/LLM-based-PHM"},{"title":"Towards LLM-Based Failure Localization in Production-Scale Networks | Proceedings of the ACM SIGCOMM 2025 Conference","url":"https://dl.acm.org/doi/10.1145/3718958.3750505"},{"title":"AGENTFL: Scaling LLM-based Fault Localization to Project-Level Context","url":"https://arxiv.org/pdf/2403.16362"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Enhancing LLM-based Fault Localization with a ...","url":"https://arxiv.org/pdf/2509.20552"},{"title":"GitHub - chrisliu298/awesome-llm-unlearning: A resource repository for machine unlearning in large language models · GitHub","url":"https://github.com/chrisliu298/awesome-llm-unlearning"},{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"Publications | Research Departments | NEC Labs America","url":"https://www.nec-labs.com/publications/"},{"title":"Improving LLM-Based Fault Localization with External Memory and Project Context","url":"https://arxiv.org/html/2506.03585v1"}]

I've found relevant search results for your query. Here's what the current research shows:

## Recent Work on LLM-Based Fault Localization (2025-2026)

**Multi-View Contrastive Learning Approach:**
A novel approach called Multi-View Adaptive Contrastive Learning for Information Retrieval Fault Localization (MACL-IRFL) was proposed to learn relationships for software fault localization. The model can improve over the best baseline up to 28.93%, 25.57% and 20.35% on Accuracy@1, MAP and MRR, respectively.

**LLM-Based Fault Localization with External Memory:**
MemFL is a novel LLM-based fault localization technique that incorporates project-specific knowledge through external memory-based knowledge editing. Evaluations on the Defects4J benchmark demonstrate that MemFL outperforms state-of-the-art LLM-based FL techniques by 12.7%.

**Contrastive Learning in Hardware Fault Diagnosis:**
Recent work includes "Large language model to assist data augmentation in soft contrastive learning for few-shot machinery fault diagnosis", showing applications of contrastive learning with LLMs in industrial fault diagnosis (2025).

**Failure Localization in Networks:**
Research has explored LLM-based agents for root cause analysis in production-scale network environments (2025).

The research shows active development combining contrastive learning techniques with LLMs for fault localization across both software and hardware domains in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05fe5f2b-7875-44fd-96c7-74e23222d05e",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "dc9d19f3-5cdc-45ce-a253-4399dd119205",
  "sourceToolAssistantUUID": "05fe5f2b-7875-44fd-96c7-74e23222d05e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T05:38:54.529Z_

<details><summary>↩ Tool result · `toolu_01Xt6ffdoodzmPa7StYFDBmy`</summary>

```text
Web search results for query: "contrastive learning automated program repair LLM code understanding"

Links: [{"title":"GitHub - iSEngLab/AwesomeLLM4APR: [TOSEM 2026]A Systematic Literature Review on Large Language Models for Automated Program Repair · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4APR"},{"title":"ContrastRepair: Enhancing Conversation-Based Automated Program Repair via Contrastive Test Case Pairs | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3719345"},{"title":"Distinguishing LLM-Generated from Human-Written Code by Contrastive Learning | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3705300"},{"title":"ContrastRepair: Enhancing Conversation-Based Automated Program Repair via Contrastive Test Case Pairs","url":"https://arxiv.org/html/2403.01971"},{"title":"EffiPair: Improving the Efficiency of LLM-generated Code with Relative Contrastive Feedback","url":"https://arxiv.org/html/2604.05137"},{"title":"Hybrid Automated Program Repair by Combining Large Language Models and Program Analysis | ACM Transactions on Software Engineering and Methodology","url":"https://dl.acm.org/doi/10.1145/3715004"},{"title":"An Empirical Study on Fine-Tuning Large Language Models of Code for Automated Program Repair | Proceedings of the 38th IEEE/ACM International Conference on Automated Software Engineering","url":"https://dl.acm.org/doi/10.1109/ASE56229.2023.00181"},{"title":"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v1"},{"title":"Comprehensive Fine-Tuning Large Language Models of Code for Automated Program Repair | IEEE Transactions on Software Engineering","url":"https://dl.acm.org/doi/10.1109/TSE.2025.3532759"},{"title":"A Survey of LLM-based Software Repair: Taxonomies, Design Paradigms, and Applications","url":"https://arxiv.org/html/2506.23749v2"}]

I've found comprehensive research on the intersection of contrastive learning, automated program repair, and LLM code understanding. Here are the key findings:

## ContrastRepair: A Key Example

A prominent approach called ContrastRepair involves constructing contrastive test case pairs, consisting of a failing test case and a corresponding passing test case, to enhance conversation-based automated program repair. The failing test and passing test are sufficiently similar, which allows LLMs to deduce critical changes based on their minor differences leading to triggering the bug.

## How Contrastive Pairs Help LLMs Understand Code

Critical changes hold valuable insights into understanding the root cause of bugs, making them essential for successful bug localization and repair, and the objective is to identify and provide critical change information to LLMs. Incorporating similarity-based pair selection and dependent functions in prompts significantly improves the effectiveness of LLMs in generating more correct fixes and reduces the number of API calls.

## Other Contrastive Learning Approaches for Code

Beyond program repair, CodeGPTSensor is a contrastive learning-based approach to detect code generated by LLMs, based on a contrastive learning framework and a semantic encoder built with UniXcoder. Additionally, Relative Contrastive Feedback (RCF) is an optimization signal for LLM-based program synthesis defined as structured feedback derived from pairwise comparisons between candidate programs based on their execution behavior, transforming efficiency optimization from scalar reward maximization into a contrastive learning problem over program executions.

## Recent Survey Findings

ContrastRepair augments conversation-based APR by supplying ChatGPT with a contrastive pair of nearly identical test cases to focus the model on the specific code change that triggers the bug, with richer feedback yielding higher fix rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ba0bebb7-d038-42e9-ba30-5cb713317937",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "5eea862d-9624-413d-91c9-609dc3aacb2f",
  "sourceToolAssistantUUID": "ba0bebb7-d038-42e9-ba30-5cb713317937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T05:38:54.732Z_

<details><summary>↩ Tool result · `toolu_01GhQfJ8qqVrhkeieYbRzc8e`</summary>

```text
Web search results for query: "code robustness semantic mutations fine-tuning LLM 2025 2026"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"Semantic-Aware Fuzzing: An Empirical Framework for LLM-Guided, Reasoning-Driven Input Mutation","url":"https://arxiv.org/html/2509.19533v1"},{"title":"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats - ADS","url":"https://ui.adsabs.harvard.edu/abs/2024arXiv241022293S/abstract"},{"title":"Are Large Language Models Robust in Understanding Code Against","url":"https://arxiv.org/pdf/2505.10443"},{"title":"Understanding Robustness of Model Editing in Code LLMs: An Empirical Study","url":"https://arxiv.org/pdf/2511.03182"},{"title":"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats","url":"https://arxiv.org/html/2410.22293v1"},{"title":"[2602.11411] Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data","url":"https://arxiv.org/abs/2602.11411"},{"title":"Awesome-Code-LLM/README.md at main · codefuse-ai/Awesome-Code-LLM","url":"https://github.com/codefuse-ai/Awesome-Code-LLM/blob/main/README.md"},{"title":"[2511.03182] Understanding Robustness of Model Editing in Code LLMs: An Empirical Study","url":"https://arxiv.org/abs/2511.03182"}]

I've found several relevant research papers and resources on code robustness, semantic mutations, and fine-tuning Large Language Models from 2025-2026. Here's what the search revealed:

## Key Findings:

### LLM Code Robustness and Semantic Mutations

A large-scale empirical investigation into the robustness of LLMs' fault localizability presents an end-to-end evaluation framework that addresses limitations in current LLM evaluation, including data contamination, scalability, automation, and extensibility. The research applies semantic-preserving mutations (SPMs) and reruns localization to assess the LLM's robustness and whether the LLM's reasoning relies on syntactic cues rather than semantics.

SPMs cause an LLM to fail to localize the same fault it correctly localized earlier in 78% of cases, suggesting that LLMs' code-reasoning is tied to code features irrelevant to semantics.

### Fine-Tuning for Robustness

A systematic evaluation of LLM robustness involved fine-tuning models using datasets perturbed at character-level, word-level, and sentence-level, finding that fine-tuning LLMs with perturbed datasets significantly improves model robustness (RD usually drops around 4% - 6%).

### Code Mutation Training

Code mutation training involves increasing variations of codes synthesized by a pre-trained LLM through fine-tuning, with approaches involving restructuring code at the subroutine level while maintaining semantic integrity verified through unit testing.

### LLM-Guided Fuzzing

Future work will explore fine-tuning LLMs—guided by automated mutation feedback and implemented through reinforcement learning or Direct Preference Optimization (DPO)—to improve both syntactic correctness and mutation diversity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bdf71397-96e3-43ee-ae6b-dbff6b7902b4",
  "isSidechain": true,
  "promptId": "073f59e2-5eca-44b2-8b49-13d14d4d8dca",
  "agentId": "ac72cbccf5bf967e0",
  "type": "user",
  "uuid": "70c4745d-ea33-4e48-a309-8a36ce3f6c55",
  "sourceToolAssistantUUID": "bdf71397-96e3-43ee-ae6b-dbff6b7902b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 22 · 2026-05-10T05:39:14.767Z_

Based on my comprehensive web search, here's my findings on the papers and related work you requested:

## Papers Found and Verified

### 1. **arXiv 2504.04372** - CONFIRMED
**Title**: "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"
- **Status**: Accepted at IEEE ICST 2026 (International Conference on Software Testing, Verification and Validation)
- **Key Finding**: Uses semantic-preserving mutations (SPMs) to evaluate LLM robustness. Results show that SPMs cause LLMs to fail in 78% of cases where they previously succeeded in fault localization, indicating that LLMs rely on syntactic cues rather than semantic understanding.
- **Scope**: Evaluates 10 state-of-the-art LLMs on 750,013 fault localization tasks from 1,300+ Java and Python programs.

### 2. **arXiv 2505.10443** - CONFIRMED
**Title**: "Are Large Language Models Robust in Understanding Code Against Semantics-Preserving Mutations?"
- **Authors**: Pedro Orvalho and Marta Kwiatkowska
- **Key Finding**: LLMs produce correct predictions based on flawed reasoning in 10-50% of cases. LLMs frequently change predictions in response to semantic-preserving code mutations, indicating unstable and non-semantic reasoning.
- **Methodology**: Tests five types of mutations (variable renaming, comparison mirroring, if-else swapping, for-to-while conversion, loop unrolling) on 6 LLMs using LiveCodeBench and CruxEval.

### 3. **arXiv 2601.18044** - CONFIRMED
**Title**: "RGFL: Reasoning Guided Fault Localization for Automated Program Repair Using Large Language Models"
- **Key Approach**: Introduces a hierarchical reasoning module that generates structured bug-specific explanations and uses a two-stage ranking scheme combining LLM-based and embedding-based signals.
- **Results**: File-level Hit@1 improves from 71.4% to 85%, and element-level Exact Match increases from 36% to 69%. End-to-end repair success improves by 12.8%.
- **Context**: Addresses limitations of project-level repair scenarios where repositories exceed LLM context limits.

### 4. **arXiv 2604.05481** - CONFIRMED
**Title**: "On the Role of Fault Localization Context for LLM-Based Program Repair"
- **Authors**: Melika Sepidband, Hung Viet Pham, Hadi Hemmati
- **Scale**: Large-scale empirical study on 500 SWE-bench Verified instances using GPT-5-mini with 61 configuration variants
- **Key Finding**: More context does not consistently improve repair performance. File-level localization yields 15-17x improvement over baseline. Optimal configurations use 6-10 relevant files. Line-level context expansion frequently degrades performance due to noise.

### 5. **arXiv 2512.16956** - CONFIRMED
**Title**: "SpIDER: Spatially Informed Dense Embedding Retrieval for Software Issue Localization"
- **Key Contribution**: Enhanced dense retrieval approach incorporating LLM-based reasoning over auxiliary context from graph-based codebase exploration.
- **Resource**: Introduces SpIDER-Bench evaluation benchmark from SWE-PolyBench and SWEBench-Verified, covering Python, Java, JavaScript, and TypeScript.
- **Advantage**: Outperforms embedding-based approaches by leveraging codebase graph structure.

### 6. **MACL-IRFL** - CONFIRMED
**Title**: "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization"
- **Publication**: Published in Automated Software Engineering (2026), also available on arXiv 2409.12519
- **Key Approach**: Models three views: (1) bug report-code interaction, (2) bug report similarity, (3) code co-citation relationships using structured graphs
- **Improvements**: Up to 28.93% on Accuracy@1, 25.57% on MAP, and 20.35% on MRR over baselines

## Competing/Related Work (2025-2026)

### Contrastive Learning in Program Repair
- **ContrastRepair**: Uses contrastive test case pairs (failing vs. passing) to enhance conversation-based automated program repair, focusing LLMs on critical code changes
- **EffiPair**: Applies relative contrastive feedback to improve efficiency of LLM-generated code
- **CodeGPTSensor**: Contrastive learning framework to distinguish LLM-generated from human-written code

### LLM-Based Fault Localization
- **MemFL**: Incorporates project-specific knowledge through external memory-based knowledge editing, outperforming state-of-the-art by 12.7% on Defects4J
- **AgentFL**: Scaling LLM-based fault localization to project-level context
- **ARISE**: Repository-level graph representation and toolset for agentic fault localization and program repair

### Code Robustness Research
- **arXiv 2602.11411**: "Improving the Robustness of Large Language Models for Code Tasks via Fine-tuning with Perturbed Data" - Shows fine-tuning with character/word/sentence-level perturbations improves robustness by 4-6%
- **arXiv 2511.03182**: "Understanding Robustness of Model Editing in Code LLMs: An Empirical Study"
- **Semantic-Aware Fuzzing**: LLM-guided, reasoning-driven input mutation framework

## Key Trend: Combining Contrastive Learning with Fault Localization

The research shows active development in integrating contrastive learning with LLM-based fault localization (MACL-IRFL, ContrastRepair) and improving code robustness through semantic mutation testing (papers 1 and 2). The papers you listed appear to be at the forefront of examining both the robustness limitations of LLMs on code understanding (papers 1 and 2) and advanced techniques to address these limitations through reasoning-guided approaches (papers 3 and 4).

---

## Sources:
- [arXiv 2504.04372 - Assessing the Impact of Code Changes](https://arxiv.org/abs/2504.04372)
- [ICST 2026 Conference Paper](https://conf.researchr.org/details/icst-2026/icst-2026-research/30/Assessing-the-Impact-of-Code-Changes-on-the-Fault-Localizability-of-Large-Language-Mo)
- [arXiv 2505.10443 - Code Robustness Paper](https://arxiv.org/abs/2505.10443)
- [arXiv 2601.18044 - RGFL Paper](https://arxiv.org/abs/2601.18044)
- [arXiv 2604.05481 - Fault Localization Context Paper](https://arxiv.org/abs/2604.05481)
- [arXiv 2512.16956 - SpIDER Paper](https://arxiv.org/abs/2512.16956)
- [arXiv 2409.12519 - MACL-IRFL Paper](https://arxiv.org/abs/2409.12519)
- [MACL-IRFL Published in Springer](https://link.springer.com/article/10.1007/s10515-025-00573-x)
- [ContrastRepair - ACM TOSEM](https://dl.acm.org/doi/10.1145/3719345)
- [MemFL - External Memory Fault Localization](https://arxiv.org/html/2506.03585v1)
- [arXiv 2602.11411 - Fine-tuning with Perturbed Data](https://arxiv.org/abs/2602.11411)
- [arXiv 2511.03182 - Model Editing Robustness](https://arxiv.org/abs/2511.03182)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70c4745d-ea33-4e48-a309-8a36ce3f6c55",
  "isSidechain": true,
  "agentId": "ac72cbccf5bf967e0",
  "requestId": "req_011CatMFEhCEMmUcPA37tmrq",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "17bad4ac-9048-498d-9cc2-55d1276eae91",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "924d92b4-a5d4-492f-8ca6-f254c2b0392e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01PXo9LUKMdUT2ZQYWMCogei",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1038,
      "cache_creation_input_tokens": 3153,
      "cache_read_input_tokens": 22799,
      "output_tokens": 1980,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3153
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1038,
          "output_tokens": 1980,
          "cache_read_input_tokens": 22799,
          "cache_creation_input_tokens": 3153,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3153,
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
