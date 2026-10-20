# Research conversation: Search for the paper "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" by Sana Ebrahimi, Mohsen De

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af25d18ab8e43d00f.jsonl`
- **Structured JSON:** [`649886540c0ab36711af.json`](../../sessions/64/649886540c0ab36711af.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-26T10:57:19.531Z_

Search for the paper "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" by Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh (arXiv:2505.24239). I need to know: was this paper published at IJCNLP-AACL 2025 or any other conference? If so, what are the exact proceedings title, pages, and year? Currently our bib lists it as an arXiv preprint. Report the exact venue info.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "e0b1d9ec-92dc-40a2-b856-34c5c11c81d6",
  "agentId": "af25d18ab8e43d00f",
  "type": "user",
  "uuid": "f56cec4a-ffff-4916-8644-11a19d104c87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-26T10:57:21.053Z_

I'll search for information about this paper to find its publication venue details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f56cec4a-ffff-4916-8644-11a19d104c87",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4UBkM4JbkFdyVssyKZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b707890e-0106-45fb-9715-d103315c1e03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M21QMUdn7kkA1VJ8mt2eXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 35178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 553,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-26T10:57:21.273Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KoDqSbenQeeShbB2Y7SWbd`</summary>

```json
{
  "query": "Ebrahimi Dehghankar Asudeh \"Adversary-Resistant Multi-Agent LLM\" arXiv:2505.24239"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b707890e-0106-45fb-9715-d103315c1e03",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4UBkM4JbkFdyVssyKZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "016f712c-934b-4a2e-b803-a1b40b9f0007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M21QMUdn7kkA1VJ8mt2eXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 35178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 553,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-26T10:57:21.482Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011xcygsLNzmv3jgNv9ib3i7`</summary>

```json
{
  "query": "\"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring\" IJCNLP AACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "016f712c-934b-4a2e-b803-a1b40b9f0007",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4UBkM4JbkFdyVssyKZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71d50676-1bf8-45dd-b3e1-ef90c1d99b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M21QMUdn7kkA1VJ8mt2eXs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 35178,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 553,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-26T10:57:21.656Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P8rcivWoWyPwbbqK7dythC`</summary>

```json
{
  "query": "arXiv 2505.24239 proceedings conference publication"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71d50676-1bf8-45dd-b3e1-ef90c1d99b89",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4UBkM4JbkFdyVssyKZ",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "89ecb2f0-21c3-4e3f-8021-ac61df281ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01M21QMUdn7kkA1VJ8mt2eXs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 553,
      "cache_read_input_tokens": 35178,
      "output_tokens": 219,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 553
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 219,
          "cache_read_input_tokens": 35178,
          "cache_creation_input_tokens": 553,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 553,
            "ephemeral_1h_input_tokens": 0
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

_source line 6 · 2026-05-26T10:57:30.462Z_

<details><summary>↩ Tool result · `toolu_011xcygsLNzmv3jgNv9ib3i7`</summary>

```text
Web search results for query: ""An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" IJCNLP AACL 2025"

Links: [{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.90/"},{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via ...","url":"https://aclanthology.org/2025.ijcnlp-long.90.pdf"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/html/2505.24239v1"},{"title":"An Adversary-Resistant Multi-Agent LLM System via ...","url":"https://arxiv.org/pdf/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring | Request PDF","url":"https://www.researchgate.net/publication/402602390_An_Adversary-Resistant_Multi-Agent_LLM_System_via_Credibility_Scoring"},{"title":"An Adversary-Resistant Multi-Agent LLM System via ...","url":"https://asudeh.github.io/files/MA_LLM_AACL2025_Slides.pdf"},{"title":"ma-llm-refactored/README.md at main · sanaebrahimi/ma-llm-refactored","url":"https://github.com/sanaebrahimi/ma-llm-refactored/blob/main/README.md"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=19775&show=50"},{"title":"STOCHASTIC SELF-ORGANIZATION IN MULTI-AGENT SYSTEMS","url":"https://openreview.net/pdf/2ca3b516918958df3fbb7c7554820ff531e52d5b.pdf"}]

I found the paper! Here are the key details:

## Paper Information

The paper "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" was authored by Sana Ebrahimi, Mohsen Dehghankar, and Abolfazl Asudeh, and was published in 2025 in the Proceedings of the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (pages 1676–1693, Mumbai, India).

## Key Contributions

While multi-agent LLM systems show strong capabilities in various domains, they are highly vulnerable to adversarial and low-performing agents. To resolve this issue, the authors introduce a general and adversary-resistant multi-agent LLM framework based on credibility scoring.

The system models the collaborative query-answering process as an iterative game, where the agents communicate and contribute to a final system output. The system associates a credibility score that is used when aggregating the team outputs. The credibility scores are learned gradually based on the past contributions of each agent in query answering.

Their experiments across multiple tasks and settings demonstrate the system's effectiveness in mitigating adversarial influence and enhancing the resilience of multi-agent cooperation, even in the adversary-majority settings.

**Resources:**
- ACL Anthology: https://aclanthology.org/2025.ijcnlp-long.90/
- arXiv: https://arxiv.org/abs/2505.24239
- GitHub: https://github.com/sanaebrahimi/ma-llm-refactored/


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71d50676-1bf8-45dd-b3e1-ef90c1d99b89",
  "isSidechain": true,
  "promptId": "e0b1d9ec-92dc-40a2-b856-34c5c11c81d6",
  "agentId": "af25d18ab8e43d00f",
  "type": "user",
  "uuid": "bc44ec00-84f8-4c19-9e45-7251c2dc790c",
  "sourceToolAssistantUUID": "71d50676-1bf8-45dd-b3e1-ef90c1d99b89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern"
}
```

</details>

---

### Tool result

_source line 7 · 2026-05-26T10:57:30.516Z_

<details><summary>↩ Tool result · `toolu_01KoDqSbenQeeShbB2Y7SWbd`</summary>

```text
Web search results for query: "Ebrahimi Dehghankar Asudeh "Adversary-Resistant Multi-Agent LLM" arXiv:2505.24239"

Links: [{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/html/2505.24239v1"},{"title":"An Adversary-Resistant Multi-Agent LLM System via ...","url":"https://arxiv.org/pdf/2505.24239"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring - ACL Anthology","url":"https://aclanthology.org/2025.ijcnlp-long.90/"},{"title":"Computer Science May 2025","url":"https://arxiv.org/list/cs/2025-05?skip=12600&show=100"},{"title":"Multiagent Systems May 2025","url":"https://arxiv.org/list/cs.MA/2025-05?skip=75&show=25"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=19775&show=50"},{"title":"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring | Request PDF","url":"https://www.researchgate.net/publication/402602390_An_Adversary-Resistant_Multi-Agent_LLM_System_via_Credibility_Scoring"},{"title":"Stochastic Self-Organization in Multi-Agent Systems","url":"https://arxiv.org/html/2510.00685v1"}]

I found the paper! Here's what I can tell you about it:

## Paper Summary

The paper is titled "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" by authors Sana Ebrahimi, Mohsen Dehghankar, and Abolfazl Asudeh from the University of Illinois Chicago.

### Key Contributions

While multi-agent LLM systems show strong capabilities in various domains, they are highly vulnerable to adversarial and low-performing agents. To resolve this issue, the paper introduces a general and adversary-resistant multi-agent LLM framework based on credibility scoring.

### Approach

The system models the collaborative query-answering process as an iterative game, where the agents communicate and contribute to a final system output. The system associates a credibility score that is used when aggregating the team outputs. The credibility scores are learned gradually based on the past contributions of each agent in query answering.

### Results

Across all four benchmarks (MMLU, GSM8K, MATH, ResearchQA) and for every backbone (LLaMA3.2, Mistral7B, Qwen2.57B), introducing the Credibility Score (CrS) raises accuracy by 6–30 percentage points.

The paper was accepted at the 14th International Joint Conference on Natural Language Processing and the 4th Conference of the Asia-Pacific Chapter of the Association for Computational Linguistics (IJCNLP-AACL 2025) in Mumbai, India.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "016f712c-934b-4a2e-b803-a1b40b9f0007",
  "isSidechain": true,
  "promptId": "e0b1d9ec-92dc-40a2-b856-34c5c11c81d6",
  "agentId": "af25d18ab8e43d00f",
  "type": "user",
  "uuid": "ab52bfeb-d67a-47bf-8ff6-6084b4656122",
  "sourceToolAssistantUUID": "016f712c-934b-4a2e-b803-a1b40b9f0007",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-26T10:57:40.354Z_

<details><summary>↩ Tool result · `toolu_01P8rcivWoWyPwbbqK7dythC`</summary>

```text
Web search results for query: "arXiv 2505.24239 proceedings conference publication"

Links: [{"title":"[2505.24239] An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring","url":"https://arxiv.org/abs/2505.24239"},{"title":"Computer Science May 2025","url":"https://www.arxiv.org/list/cs/2025-05?skip=11150&show=250"},{"title":"Sinchana Ramakanth Bhat","url":"https://scholar.google.com/citations?user=TjCSfN8AAAAJ&hl=en"},{"title":"Author-Based Analysis of Conference versus Journal ...","url":"https://arxiv.org/pdf/1806.10674"},{"title":"Submit a Paper List for Conference Proceedings - arXiv info","url":"https://info.arxiv.org/help/submit_index.html"},{"title":"A Survey of Long-Document Retrieval in the PLM and LLM Era","url":"https://arxiv.org/html/2509.07759"},{"title":"Zhuangcheng Gu - Google 學術搜尋","url":"https://scholar.google.com/citations?user=QJy2ZyIAAAAJ&hl=zh-TW"},{"title":"Computer Vision and Pattern Recognition May 2025","url":"https://arxiv.org/list/cs.CV/2025-05?skip=775&show=1000"},{"title":"[2505.21700] Rethinking Chunk Size For Long-Document Retrieval: A Multi-Dataset Analysis","url":"https://arxiv.org/abs/2505.21700"},{"title":"Machine Learning","url":"https://web3.arxiv.org/list/cs.LG/recent?skip=217&show=250"}]

Based on the search results, I found information about arXiv paper 2505.24239, titled "An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring" by Sana Ebrahimi, Mohsen Dehghankar, and Abolfazl Asudeh, submitted on May 30, 2025.

However, the search results do not indicate that this paper has been published in conference proceedings. The paper appears to be available on arXiv as a preprint. The abstract page does not show any conference publication information or journal reference. If this paper is intended for conference publication, that information is not currently reflected in the arXiv record based on these search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89ecb2f0-21c3-4e3f-8021-ac61df281ab3",
  "isSidechain": true,
  "promptId": "e0b1d9ec-92dc-40a2-b856-34c5c11c81d6",
  "agentId": "af25d18ab8e43d00f",
  "type": "user",
  "uuid": "df50d1a5-1e98-452d-99f5-4dca7577efa7",
  "sourceToolAssistantUUID": "89ecb2f0-21c3-4e3f-8021-ac61df281ab3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern"
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-26T10:57:41.825Z_

Excellent! I found the publication information. Let me fetch the ACL Anthology page to get the exact proceedings details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df50d1a5-1e98-452d-99f5-4dca7577efa7",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4VijSwUh1L2vXuoenL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f9b276d2-8c0d-4a3f-8805-5a67cbc5064b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014yrEBaH68VzccGDS2SKkqh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3550,
      "cache_read_input_tokens": 35731,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3550,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 7,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-26T10:57:42.408Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01To4FDMxxxxqNjZUugxPGYG`</summary>

```json
{
  "url": "https://aclanthology.org/2025.ijcnlp-long.90/",
  "prompt": "proceedings title pages year publication details"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9b276d2-8c0d-4a3f-8805-5a67cbc5064b",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4VijSwUh1L2vXuoenL",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e65bd9d-d3b0-4250-ba1e-360b85e73b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_014yrEBaH68VzccGDS2SKkqh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3550,
      "cache_read_input_tokens": 35731,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3550
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 122,
          "cache_read_input_tokens": 35731,
          "cache_creation_input_tokens": 3550,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3550,
            "ephemeral_1h_input_tokens": 0
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

_source line 11 · 2026-05-26T10:57:46.000Z_

<details><summary>↩ Tool result · `toolu_01To4FDMxxxxqNjZUugxPGYG`</summary>

```text
# Paper Summary

**Title:** An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring

**Authors:** Sana Ebrahimi, Mohsen Dehghankar, Abolfazl Asudeh

**Publication Details:**
- Conference: 14th International Joint Conference on Natural Language Processing (IJCNLP) and 4th Asia-Pacific Chapter Conference (AACL)
- Location: Mumbai, India
- Month/Year: December 2025
- Pages: 1676–1693
- DOI: 10.18653/v1/2025.ijcnlp-long.90

**Key Contribution:**

The authors present a framework designed to strengthen multi-agent language model systems against malicious participants. Their approach introduces "a credibility score that is used when aggregating the team outputs" where "credibility scores are learned gradually based on the past contributions of each agent in query answering."

The research demonstrates effectiveness "even in the adversary-majority settings," addressing a significant vulnerability in collaborative LLM systems.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e65bd9d-d3b0-4250-ba1e-360b85e73b65",
  "isSidechain": true,
  "promptId": "e0b1d9ec-92dc-40a2-b856-34c5c11c81d6",
  "agentId": "af25d18ab8e43d00f",
  "type": "user",
  "uuid": "b7ee3edc-fe36-49cc-a2ae-46fdef37668f",
  "sourceToolAssistantUUID": "4e65bd9d-d3b0-4250-ba1e-360b85e73b65",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-26T10:57:51.186Z_

Perfect! I have found the exact publication information for this paper.

## Summary

The paper **"An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring"** by Sana Ebrahimi, Mohsen Dehghankar, and Abolfazl Asudeh **WAS published** at IJCNLP-AACL 2025.

### Exact Publication Details:

- **Proceedings Title:** Proceedings of the 14th International Joint Conference on Natural Language Processing (IJCNLP) and 4th Asia-Pacific Chapter Conference (AACL)
- **Pages:** 1676–1693
- **Year:** 2025
- **Location:** Mumbai, India
- **Month:** December 2025
- **DOI:** 10.18653/v1/2025.ijcnlp-long.90
- **ACL Anthology ID:** 2025.ijcnlp-long.90

Your bibliography entry should be updated from the arXiv preprint to reflect the conference publication. The paper is available at the [ACL Anthology](https://aclanthology.org/2025.ijcnlp-long.90/) and [arXiv](https://arxiv.org/abs/2505.24239).

Sources:
- [ACL Anthology entry](https://aclanthology.org/2025.ijcnlp-long.90/)
- [arXiv preprint](https://arxiv.org/abs/2505.24239)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b7ee3edc-fe36-49cc-a2ae-46fdef37668f",
  "isSidechain": true,
  "agentId": "af25d18ab8e43d00f",
  "requestId": "req_011CbR4W8pHWhwHRQo3Sk5qG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "b0e02c2e-c6f5-411a-9154-fbdce7a9871d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0519_2/projects/cert_manip_resist_eval/.claude/sessions/agent_0c5aa23b",
  "sessionId": "e30200cf-3b9a-4571-acdd-cebfd006e51e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "calm-weaving-fern",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_015HsSS5nzQpTHYrEmicWGzq",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 377,
      "cache_read_input_tokens": 39281,
      "output_tokens": 364,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 377
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 364,
          "cache_read_input_tokens": 39281,
          "cache_creation_input_tokens": 377,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 377,
            "ephemeral_1h_input_tokens": 0
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
