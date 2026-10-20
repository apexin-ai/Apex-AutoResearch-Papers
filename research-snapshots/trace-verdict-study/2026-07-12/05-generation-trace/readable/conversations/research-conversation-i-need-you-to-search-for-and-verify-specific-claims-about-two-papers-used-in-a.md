# Research conversation: I need you to search for and verify specific claims about two papers used in a multilingual NLP research proposal. **Tas

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 32
- **Recorded user turns:** 1
- **Tool calls:** 13
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aa73e51c9c574eb03.jsonl`
- **Structured JSON:** [`0ff6be084344125db4c8.json`](../../sessions/0f/0ff6be084344125db4c8.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

32 recorded events

### User

_source line 1 · 2026-05-10T08:21:20.257Z_

I need you to search for and verify specific claims about two papers used in a multilingual NLP research proposal.

**Task 1: Verify "Less is More: The Effectiveness of Compact Typological Language Representations" (arXiv:2509.20129, EMNLP 2025)**

The proposal claims:
- This paper's Laplacian Score 300-feature URIEL+ subset achieves Spearman ρ=0.358 (p=0.061) measured against linguistic distance alignment metric G_d (Table 1)
- The full 800-feature set achieves ρ=0.260
- It yields +7.8% improvement on LangRank downstream tasks

Please search for this paper and try to verify these specific ρ values. Search for:
1. "Less is More Compact Typological Language Representations EMNLP 2025"
2. "arXiv 2509.20129"
3. Try to fetch the abstract from arxiv.org/abs/2509.20129

**Task 2: Verify Budget-Xfer status**
Search for "Budget-Xfer arXiv 2603.27651" to confirm it is still a preprint submitted to SIGIR 2026 (not yet accepted/published).

**Task 3: Search for new competing papers (last 3 months, April-May 2026)**
Search for:
1. "typological distance multilingual instruction tuning 2026"
2. "multi-pivot cross-lingual transfer low-resource 2026"
3. "URIEL typological instruction tuning arxiv 2026"
4. "Kazakh Mongolian Uyghur LLM instruction tuning 2026"

Report what you find for each task, including specific numbers, dates, and URLs.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "600832d3-3049-4d7a-a721-2f3a342784eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:21:21.988Z_

I'll help you verify these claims about the papers and search for competing work. Let me start by searching for the papers systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "600832d3-3049-4d7a-a721-2f3a342784eb",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f98f02e3-ebae-4c05-9fbb-14380aea06bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T08:21:22.223Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012AJFT5rSxFwd26gqq6f73c`</summary>

```json
{
  "query": "Less is More Compact Typological Language Representations EMNLP 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f98f02e3-ebae-4c05-9fbb-14380aea06bc",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "26e28bbe-10b0-4ef3-a1c3-ca689da2ada6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T08:21:22.426Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KM7CMxa1DdUocSVWrxVZe2`</summary>

```json
{
  "query": "arXiv 2509.20129"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26e28bbe-10b0-4ef3-a1c3-ca689da2ada6",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c99e505-6196-41e3-886b-d3ff02a991bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T08:21:22.900Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01V3QiR9MZedYBERDzk9kS7B`</summary>

```json
{
  "url": "https://arxiv.org/abs/2509.20129",
  "prompt": "Find the Spearman correlation values, linguistic distance alignment metric G_d, and LangRank improvement numbers mentioned in the paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c99e505-6196-41e3-886b-d3ff02a991bd",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fc4c233f-cb32-4303-8d49-2176d1ee6fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T08:21:23.113Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012QFRrxDUBAy5x5LijoCq41`</summary>

```json
{
  "query": "Budget-Xfer arXiv 2603.27651"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fc4c233f-cb32-4303-8d49-2176d1ee6fbb",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "004f579e-908c-4dfa-8a6b-c10971e34f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-10T08:21:23.322Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KxRkuAR7opAYszCoMrjYni`</summary>

```json
{
  "query": "typological distance multilingual instruction tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "004f579e-908c-4dfa-8a6b-c10971e34f56",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "facf51a7-a138-4ac2-a549-9065f3ab074b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-10T08:21:23.545Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UQekc7W5sCP6csQQpgy8vK`</summary>

```json
{
  "query": "multi-pivot cross-lingual transfer low-resource 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "facf51a7-a138-4ac2-a549-9065f3ab074b",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d054b2e9-10d8-43bf-93a7-0b22cbe7880a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-10T08:21:23.553Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Fjbhi6dBPAd77PZm1aaorn`</summary>

```json
{
  "query": "URIEL typological instruction tuning arxiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d054b2e9-10d8-43bf-93a7-0b22cbe7880a",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "18a92184-ce8c-4b85-8bef-c53dc4f4cb5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14639,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T08:21:23.694Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TnDbYzvTquWwcx2mcUH2kX`</summary>

```json
{
  "query": "Kazakh Mongolian Uyghur LLM instruction tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18a92184-ce8c-4b85-8bef-c53dc4f4cb5c",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZdd5brbTh9yXXkBdtC",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d642e184-f282-484a-b5c4-7149ab8b439b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01SVE6m86QnhuuJcVDz2eaA1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14639,
      "cache_read_input_tokens": 0,
      "output_tokens": 476,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 14639
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 476,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 14639,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 14639,
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

_source line 11 · 2026-05-10T08:21:25.764Z_

<details><summary>↩ Tool result · `toolu_01KM7CMxa1DdUocSVWrxVZe2`</summary>

```text
Web search results for query: "arXiv 2509.20129"

Links: [{"title":"[2509.20129] Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/abs/2509.20129"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3125&show=2000"},{"title":"Cascade! Human in the loop shortcomings can increase the risk of failures in recommender systems","url":"https://arxiv.org/html/2509.20099v2"},{"title":"Computer Science","url":"https://www.arxiv.org/list/cs/recent?skip=2609&show=250"},{"title":"[2509.24175] Very High Frequency Interpolation for Direct Torque Control","url":"https://arxiv.org/abs/2509.24175"},{"title":"TASAM: Terrain-and-Aware Segment Anything Model for Temporal-Scale Remote Sensing Segmentation","url":"https://arxiv.org/html/2509.15795.pdf"},{"title":"[2509.16738] Mixture of Noise for Pre-Trained Model-Based Class-Incremental Learning","url":"https://arxiv.org/abs/2509.16738"},{"title":"[2509.23165v1] Untangling Vascular Trees for Surgery and Interventional Radiology","url":"https://arxiv.org/abs/2509.23165v1"},{"title":"Abstract","url":"https://arxiv.org/html/2509.26218"},{"title":"On Code-Induced Reasoning in LLMs","url":"https://arxiv.org/html/2509.21499v1"}]

Based on the search results, I found information about arXiv paper 2509.20129:

The paper "Less is More: The Effectiveness of Compact Typological Language Representations" proposes a pipeline to optimize the URIEL+ typological feature space by combining feature selection and imputation, producing compact yet interpretable typological representations. The paper was submitted to arXiv on September 24, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c99e505-6196-41e3-886b-d3ff02a991bd",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "a68e682b-e437-46f5-ab79-90888afd3d7f",
  "sourceToolAssistantUUID": "8c99e505-6196-41e3-886b-d3ff02a991bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:21:28.979Z_

<details><summary>↩ Tool result · `toolu_01V3QiR9MZedYBERDzk9kS7B`</summary>

```text
# Analysis

Based on the webpage content provided, I cannot locate the specific quantitative values you're requesting.

The page displays only the **abstract** of the arXiv paper (arXiv:2509.20129), which states that researchers "evaluate these feature subsets on linguistic distance alignment and downstream tasks, demonstrating that reduced-size representations of language typology can yield more informative distance metrics and improve performance in multilingual NLP applications."

However, the abstract does not include:
- Specific Spearman correlation values
- The linguistic distance alignment metric G_d figures
- LangRank improvement numbers

These detailed results would typically appear in the paper's results section, tables, or figures, which are not visible in this abstract-only webpage excerpt. To find these metrics, you would need to access the full paper via the PDF or HTML links provided on the page.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fc4c233f-cb32-4303-8d49-2176d1ee6fbb",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "9bb7f051-d730-461e-b5f2-95154fd5691b",
  "sourceToolAssistantUUID": "fc4c233f-cb32-4303-8d49-2176d1ee6fbb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:21:29.754Z_

<details><summary>↩ Tool result · `toolu_012AJFT5rSxFwd26gqq6f73c`</summary>

```text
Web search results for query: "Less is More Compact Typological Language Representations EMNLP 2025"

Links: [{"title":"Less is More: The Effectiveness of Compact Typological Language Representations - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1310/"},{"title":"Less is More: The Effectiveness of Compact Typological ...","url":"https://aclanthology.org/2025.emnlp-main.1310.pdf"},{"title":"[2509.20129] Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/abs/2509.20129"},{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129v1"},{"title":"The 2025 Conference on Empirical Methods in Natural Language Processing - EMNLP 2025","url":"https://2025.emnlp.org/"},{"title":"EMNLP.2025 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/EMNLP.2025"},{"title":"Findings of the Association for Computational Linguistics: EMNLP 2025 - ACL Anthology","url":"https://aclanthology.org/volumes/2025.findings-emnlp/"},{"title":"dblp: EMNLP","url":"https://dblp.org/db/conf/emnlp/index.html"},{"title":"EMNLP: Empirical Methods in Natural Language Processing 2027 2026 2025 ...","url":"http://www.wikicfp.com/cfp/program?id=883"},{"title":"EMNLP 2025 - NAVER LABS Europe","url":"https://europe.naverlabs.com/updates/emnlp/"}]

Based on the search results, I found detailed information about this paper:

## "Less is More: The Effectiveness of Compact Typological Language Representations"

The paper is by York Hay Ng, Phuong Hanh Hoang, and En-Shiun Annie Lee, published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025), held in Suzhou, China on pages 25805–25816.

### Main Contribution

The authors propose a pipeline to optimize the URIEL+ typological feature space by combining feature selection and imputation, producing compact yet interpretable typological representations.

### Key Details

The experiments are performed on the URIEL+ typological dataset, which is a three-dimensional array of languages (4,555), features (800), and data sources (14).

The paper's main contributions include: (1) the first principled framework for analyzing and selecting typological features, moving beyond treating all features as equally informative; (2) a robust imputation strategy with SoftImpute to handle missing values within these compact representations; and (3) an empirical demonstration that these feature subsets improve linguistic distance alignment and downstream task performance.

The research demonstrates that reduced-size representations of language typology can yield more informative distance metrics and improve performance in multilingual NLP applications.

The paper addresses the challenges of high dimensionality and sparsity in linguistic feature datasets that have limited the effectiveness of distance metrics for modeling cross-lingual relationships.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "26e28bbe-10b0-4ef3-a1c3-ca689da2ada6",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "1e9207cb-c941-472f-8900-010203a958b3",
  "sourceToolAssistantUUID": "26e28bbe-10b0-4ef3-a1c3-ca689da2ada6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T08:21:30.308Z_

<details><summary>↩ Tool result · `toolu_01UQekc7W5sCP6csQQpgy8vK`</summary>

```text
Web search results for query: "multi-pivot cross-lingual transfer low-resource 2026"

Links: [{"title":"Zero-shot English–Assamese neural machine translation via pivot-based cross-lingual embedding alignment and transfer learning | Scientific Reports","url":"https://www.nature.com/articles/s41598-026-44209-w"},{"title":"Cross-Lingual Transfer Learning: Applications in Low-Resource Languages | Academic Journal of Science and Technology","url":"https://drpress.org/ojs/index.php/ajst/article/view/33384"},{"title":"Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models","url":"https://arxiv.org/html/2505.16385v1"},{"title":"Multi-Source Cross-Lingual Model Transfer: Learning What to Share | Request PDF","url":"https://www.researchgate.net/publication/335780754_Multi-Source_Cross-Lingual_Model_Transfer_Learning_What_to_Share"},{"title":"Improving Many-to-Many Neural Machine Translation via Selective and Aligned Online Data Augmentation","url":"https://www.mdpi.com/2076-3417/13/6/3946"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"},{"title":"[2502.02722] Cross-Lingual Transfer for Low-Resource Natural Language Processing","url":"https://arxiv.org/abs/2502.02722"},{"title":"CMC | Free Full-Text | PNMT: Zero-Resource Machine Translation with Pivot-Based Feature Converter","url":"https://www.techscience.com/cmc/v84n3/63133/html"},{"title":"Enhancing distant low-resource neural machine translation with semantic pivot - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1110016824016727"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"}]

Based on the search results, here's what I found regarding multi-pivot cross-lingual transfer for low-resource languages in 2026:

## Recent Research on Multi-Pivot Cross-Lingual Transfer

Neural Machine Translation for low-resource languages such as Assamese faces significant challenges due to scarcity of parallel corpora, and researchers have proposed zero-shot translation frameworks that leverage linguistic proximity between languages.

### Key Approaches in 2026

Recent approaches combine multilingual transfer learning architectures based on mBART with cross-lingual embedding alignment via Procrustes optimization, unifying multiple languages into a shared semantic space. Transfer learning and cross-lingual alignment has proven effective in bridging resource gaps for linguistically proximate languages.

### Multi-Pivot Strategy Effectiveness

To address challenges of imbalanced foundational abilities of LLMs across different languages, researchers propose utilizing high-resource languages, primarily English, as a pivot to enhance instruction tuning in lower-resource languages by training the model to first process instructions in the pivot language, then produce responses in the target language.

Cross-lingual transfer learning research aims at leveraging data and models from high-resource languages to improve NLP performance for low-resource languages through improved translation and annotation projection techniques, enhanced model-based transfer learning approaches utilizing state-of-the-art multilingual models.

The research demonstrates that pivot-based approaches provide a practical solution for improving translation quality and NLP tasks in low-resource settings where direct parallel data is unavailable.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d054b2e9-10d8-43bf-93a7-0b22cbe7880a",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "99e95f67-b607-4eec-be0f-730b63217b5e",
  "sourceToolAssistantUUID": "d054b2e9-10d8-43bf-93a7-0b22cbe7880a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-10T08:21:31.358Z_

<details><summary>↩ Tool result · `toolu_01TnDbYzvTquWwcx2mcUH2kX`</summary>

```text
Web search results for query: "Kazakh Mongolian Uyghur LLM instruction tuning 2026"

Links: [{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh","url":"https://arxiv.org/html/2503.01493v1"},{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting | OpenReview","url":"https://openreview.net/forum?id=wRcTCcb0H5"},{"title":"Do Chinese models speak Chinese languages?","url":"https://arxiv.org/html/2504.00289v1"},{"title":"Hunyuan MT (HY-MT1.5): High-Quality Machine Translation at Small Scale | by Mehul Gupta | Data Science in Your Pocket | Medium","url":"https://medium.com/data-science-in-your-pocket/hunyuan-mt-hy-mt1-5-high-quality-machine-translation-at-small-scale-d68cb6123a79"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"Sherkala-Chat: Building a State-of-the-Art LLM for Kazakh in a Moderately Resourced Setting","url":"https://arxiv.org/html/2503.01493v2"},{"title":"Low-Resource Language Expansion and Translation ...","url":"https://aclanthology.org/2025.coling-main.559.pdf"}]

Based on the search results, here are key findings about LLM instruction tuning for Kazakh, Mongolian, and Uyghur languages in 2026:

## Recent Developments (2025-2026)

**Sherkala-Chat for Kazakh:** Llama-3.1-Sherkala-8B-Chat is a state-of-the-art instruction-tuned open generative large language model designed for Kazakh. Sherkala-Chat (8B) is trained on 45.3B tokens across Kazakh, English, Russian, and Turkish. To ensure effective and responsible alignment, they leverage translated instruction datasets, a Kazakhstan-specific instruction dataset that is automatically constructed and manually verified, and Kazakh-specific safety data.

**Kazakh Text Simplification:** KazSim is an instruction-tuned model built on multilingual large language models (LLMs) that addresses text simplification task for Kazakh, a morphologically rich, low-resource language.

**Uyghur Language Expansion:** A strategy involves four stages: collecting and pre-processing monolingual data, conducting continuous pre-training with extensive monolingual data, fine-tuning with less parallel corpora using translation supervision, and proposing a direct preference optimization based on translation self-evolution (DPOSE).

**Multilingual Evaluation (MiLiC-Eval):** MiLiC-Eval is a comprehensive framework with 24K instances across 9 tasks, focusing on 4 Minority Languages in China. This framework evaluates LLM capabilities across Kazakh, Mongolian, Uyghur, and Tibetan.

These recent developments demonstrate significant progress in instruction tuning for these underrepresented languages, though challenges remain in handling their unique writing systems and limited training data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d642e184-f282-484a-b5c4-7149ab8b439b",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "7553714b-4410-4d9d-b585-2ea4d3871976",
  "sourceToolAssistantUUID": "d642e184-f282-484a-b5c4-7149ab8b439b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T08:21:31.652Z_

<details><summary>↩ Tool result · `toolu_012QFRrxDUBAy5x5LijoCq41`</summary>

```text
Web search results for query: "Budget-Xfer arXiv 2603.27651"

Links: [{"title":"[2603.27651] Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/abs/2603.27651"},{"title":"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/html/2603.27651"},{"title":"[2603.27274] Budgeted Robust Intervention Design for Financial Networks with Common Asset Exposures","url":"https://arxiv.org/abs/2603.27274"},{"title":"[2603.00230] The Baryon Budget of Galaxies across the First Billion Years -- Theoretical Predictions for Gas Phases, Depletion Times, and Stellar Return Fractions","url":"https://arxiv.org/abs/2603.00230"},{"title":"[2603.17541] Temporal Gains, Spatial Costs: Revisiting Video Fine-Tuning in Multimodal Large Language Models","url":"https://arxiv.org/abs/2603.17541"},{"title":"[2603.03459] Half the Nonlinearity Is Wasted: Measuring and Reallocating the Transformer's MLP Budget","url":"https://arxiv.org/abs/2603.03459"},{"title":"Increasing the Thinking Budget is Not All You Need","url":"https://arxiv.org/html/2512.19585v1"},{"title":"[2603.21606] mSFT: Addressing Dataset Mixtures Overfitting Heterogeneously in Multi-task SFT","url":"https://arxiv.org/abs/2603.21606"},{"title":"[2603.12634] Spend Less, Reason Better: Budget-Aware Value Tree Search for LLM Agents","url":"https://arxiv.org/abs/2603.12634"},{"title":"[2603.16440] Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models","url":"https://arxiv.org/abs/2603.16440"}]

Based on the search results, here's information about the Budget-Xfer paper:

Budget-Xfer is a framework that formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem, jointly optimizing which source languages to include and how much data to allocate from each given a fixed annotation budget.

The research evaluates four allocation strategies across named entity recognition and sentiment analysis for three African target languages (Hausa, Yoruba, Swahili) using two multilingual models, conducting 288 experiments.

The results indicate that practitioners should always distribute data across multiple source languages rather than concentrating on a single source, as single-source strategies face a structural budget underutilization bottleneck where, on average, only 57% of the allocated budget is used. Once data is distributed across multiple sources, the specific allocation mechanism has a comparatively small effect, with no single multi-source strategy consistently dominating.

The paper was submitted to arXiv on March 29, 2026, by authors Tewodros Kederalah Idris, Roald Eiselen, and Prasenjit Mitra.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "004f579e-908c-4dfa-8a6b-c10971e34f56",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "626152dd-ab88-4ddc-9f41-c6aa00e20ed5",
  "sourceToolAssistantUUID": "004f579e-908c-4dfa-8a6b-c10971e34f56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-10T08:21:31.998Z_

<details><summary>↩ Tool result · `toolu_01KxRkuAR7opAYszCoMrjYni`</summary>

```text
Web search results for query: "typological distance multilingual instruction tuning 2026"

Links: [{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"Pretrained Multilingual Transformers Reveal Quantitative Distance Between Human Languages","url":"https://arxiv.org/html/2603.17912"},{"title":"Language Steering for Multilingual In-Context Learning","url":"https://arxiv.org/html/2602.02326"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality - ACL Anthology","url":"https://aclanthology.org/2024.findings-acl.136/"},{"title":"(PDF) Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://www.researchgate.net/publication/384811791_Linguistically-Informed_Multilingual_Instruction_Tuning_Is_There_an_Optimal_Set_of_Languages_to_Tune"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://dl.acm.org/doi/pdf/10.1145/3777411"},{"title":"Multilingual Instruction-Tuning: Do Polyglot Models Need it?","url":"https://lamarr-institute.org/blog/multilingual-instruction-tuning-ai-model/"}]

Based on the web search results, I found several recent research papers and articles related to typological distance and multilingual instruction tuning. Here's what I found:

## Key Research Areas

Recent work hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner, investigating various language selection techniques and how they compare to baselines such as randomly selected subsets and single language family representatives.

### Typological Features in Language Selection

Researchers employ 289-dimensional binary features containing syntactic, phonological, and phonetic inventory features extracted from the URIEL database, incorporating data from databases like WALS and PHOIBLE.

Linguistically informed selection techniques range from common methods such as typological feature vectors to semantic typology features, with a simple k-means clustering algorithm applied to select a fixed number of languages based on each technique.

### Recent Findings on Language Diversity

While non-English over-tokenization and typological distance provide partial explanations, controlled fine-tuning experiments on the effects of language diversity during fine-tuning remain unexplored in translation tasks.

Languages that are typologically and scripturally similar to English cluster at lower norms indicating their representations lie close to English, while languages with distinct scripts or typological structure show markedly larger norms reflecting greater representational distance from English.

### Practical Applications

Only 40 multilingual examples integrated in an English tuning set substantially improve multilingual instruction-following, and diversifying the instruction tuning set with even just 2-4 languages significantly improves cross-lingual generalization.

These recent studies (from 2024-2026) demonstrate that typological distance is an important factor in designing effective multilingual instruction tuning strategies, though it's often used alongside other linguistic features rather than in isolation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "facf51a7-a138-4ac2-a549-9065f3ab074b",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "42da24a2-3ca9-4537-a2d8-b8a99e2f6f8a",
  "sourceToolAssistantUUID": "facf51a7-a138-4ac2-a549-9065f3ab074b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-10T08:21:32.722Z_

<details><summary>↩ Tool result · `toolu_01Fjbhi6dBPAd77PZm1aaorn`</summary>

```text
Web search results for query: "URIEL typological instruction tuning arxiv 2026"

Links: [{"title":"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/html/2510.27183"},{"title":"[2409.18472] URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/abs/2409.18472"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base","url":"https://arxiv.org/html/2409.18472"},{"title":"[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/abs/2510.19217"},{"title":"[2510.27183] Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/abs/2510.27183"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"arXiv:2409.18472v3 [cs.CL] 14 Feb 2025","url":"https://arxiv.org/pdf/2409.18472"},{"title":"Less is More: The Effectiveness of Compact Typological Language Representations","url":"https://arxiv.org/html/2509.20129v1"},{"title":"GitHub - LeeLanguageLab/URIELPlus: URIEL+ knowledge base for natural language processing · GitHub","url":"https://github.com/LeeLanguageLab/URIELPlus"},{"title":"A Reproducibility Study on Quantifying Language Similarity: The Impact of Missing Values in the URIEL Knowledge Base","url":"https://arxiv.org/html/2405.11125v1"}]

Based on the search results, I found several relevant papers about URIEL and typological instruction tuning from 2025-2026:

## Key Papers Found:

1. **URIEL+: Enhancing Linguistic Inclusion and Usability in a Typological and Multilingual Knowledge Base** (2025)
   - URIEL is a knowledge base offering geographical, phylogenetic, and typological vector representations for 7970 languages with distance measures between these vectors for 4005 languages, accessible via the lang2vec tool.
   - URIEL+ is an enhanced version that addresses limitations by expanding typological feature coverage for 2898 languages and improving customizable distance calculations.

2. **Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+** (March 2026)
   - This work extends URIEL+ by introducing script vectors for 7,488 languages, integrating Glottolog to add 18,710 additional languages, and expanding lineage imputation for 26,449 languages by propagating typological and script features across genealogies.
   - These improvements reduce feature sparsity by 14% for script vectors, increase language coverage by up to 19,015 languages (1,007%), and boost imputation quality metrics by up to 35%.

3. **Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+** (March 2026)
   - The paper proposes novel, structure-aware representations for each distance type: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and a latent variables model for typology.

4. **Less is More: The Effectiveness of Compact Typological Language Representations** (2025)
   - This work proposes a pipeline to optimize the URIEL+ typological feature space by combining feature selection and imputation, demonstrating that reduced-size representations of language typology can yield more informative distance metrics and improve multilingual NLP performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18a92184-ce8c-4b85-8bef-c53dc4f4cb5c",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "223bcc86-dc9c-41cb-8797-3d34deb5e823",
  "sourceToolAssistantUUID": "18a92184-ce8c-4b85-8bef-c53dc4f4cb5c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 19 · 2026-05-10T08:21:34.199Z_

Now let me fetch the full PDF or HTML version of the "Less is More" paper to try to find the specific numerical values you mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "223bcc86-dc9c-41cb-8797-3d34deb5e823",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZeYMciy2dhD9wFDkLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f64eb5f2-7b2d-4ae5-a29e-0d9d2fef3bd1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRzib9uqg1MsBMUhM6MHNB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 6628,
      "cache_read_input_tokens": 14639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6628,
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

_source line 20 · 2026-05-10T08:21:35.658Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QJUXuK1NRksj4NsZsC5V2G`</summary>

```json
{
  "url": "https://arxiv.org/pdf/2509.20129",
  "prompt": "Find Table 1 with Spearman correlation ρ values, specifically the Laplacian Score 300-feature URIEL+ subset ρ=0.358 (p=0.061), full 800-feature ρ=0.260, and the linguistic distance alignment metric G_d values"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f64eb5f2-7b2d-4ae5-a29e-0d9d2fef3bd1",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZeYMciy2dhD9wFDkLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "11cd62be-6eb2-45fb-8f99-7b0c558c3d43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRzib9uqg1MsBMUhM6MHNB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 6628,
      "cache_read_input_tokens": 14639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6628,
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

_source line 21 · 2026-05-10T08:21:36.363Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Jy8aZEPKXcHqHMerjEKP3Z`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.20129v1",
  "prompt": "Find the specific Spearman correlation values for Table 1 and LangRank downstream task improvements"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11cd62be-6eb2-45fb-8f99-7b0c558c3d43",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZeYMciy2dhD9wFDkLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "08326b05-da3a-4177-a871-32bd3e374981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRzib9uqg1MsBMUhM6MHNB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 6628,
      "cache_read_input_tokens": 14639,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6628,
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

_source line 22 · 2026-05-10T08:21:36.692Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Pin1MKUYfKHy1wTsUVrkNR`</summary>

```json
{
  "url": "https://aclanthology.org/2025.emnlp-main.1310.pdf",
  "prompt": "Find Table 1 with Spearman correlation values ρ and the LangRank +7.8% improvement mentioned"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08326b05-da3a-4177-a871-32bd3e374981",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZeYMciy2dhD9wFDkLr",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f6b97f9b-8957-4f3b-b1bc-27a05b6535fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NRzib9uqg1MsBMUhM6MHNB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1034,
      "cache_creation_input_tokens": 6628,
      "cache_read_input_tokens": 14639,
      "output_tokens": 373,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6628
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1034,
          "output_tokens": 373,
          "cache_read_input_tokens": 14639,
          "cache_creation_input_tokens": 6628,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6628,
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

_source line 23 · 2026-05-10T08:21:39.937Z_

<details><summary>↩ Tool result · `toolu_01QJUXuK1NRksj4NsZsC5V2G`</summary>

```text
I cannot locate Table 1 with the specific Spearman correlation values you've requested in the provided PDF content. The document appears to be a research paper titled "Less is More: The Effectiveness of Compact Typological Language Representations" by York Hay Ng, Phuong Hanh Hoang, and En-Shiun Annie Lee, but the PDF content provided consists primarily of metadata and structural information rather than the actual table data.

To find these specific correlation values (ρ=0.358 for the 300-feature subset, ρ=0.260 for the full 800-feature URIEL+, and the G_d linguistic distance alignment metrics), you would need to access the full rendered PDF or the paper's main content pages where Table 1 is displayed.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-/4b90db97-abf7-43ca-8746-d63916fc40be/tool-results/webfetch-1778401296540-jkl6hb.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "11cd62be-6eb2-45fb-8f99-7b0c558c3d43",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "da9ae722-5c14-4ab0-9b7a-c07f7c4dbf06",
  "sourceToolAssistantUUID": "11cd62be-6eb2-45fb-8f99-7b0c558c3d43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T08:21:40.772Z_

<details><summary>↩ Tool result · `toolu_01Jy8aZEPKXcHqHMerjEKP3Z`</summary>

```text
# Specific Correlation and Performance Values

## Table 1: Spearman Correlation Values

The paper presents alignment results comparing feature selection methods against the baseline URIEL+ dataset:

- **URIEL+ (Baseline)**: ρ = 0.260
- **Variance method**: ρ = 0.295 (at subset size 500)
- **PCA Loadings**: ρ = 0.292 (at subset size 700)
- **Laplacian Score**: ρ = 0.358 (at subset size 300) — best performer
- **Correlation-based FS**: ρ = 0.264 (at subset size 200)

## LangRank Downstream Task Improvements

Regarding cross-lingual transfer prediction performance, the research indicates: "For LangRank, the LS and CFS methods outperform the full feature set baseline at smaller subset sizes, with peak gains of +7.8% (size 300) and +6.0% (size 100) respectively."

The Laplacian Score method achieved the strongest improvement at approximately 7.8%, while Correlation-based Feature Selection reached around 6.0% improvement over the baseline URIEL+ approach when applied to the LangRank framework.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08326b05-da3a-4177-a871-32bd3e374981",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "22a48ae9-05a3-4879-8488-e33e9ea2bbe5",
  "sourceToolAssistantUUID": "08326b05-da3a-4177-a871-32bd3e374981",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T08:21:42.907Z_

<details><summary>↩ Tool result · `toolu_01Pin1MKUYfKHy1wTsUVrkNR`</summary>

```text
I've examined the provided PDF content, which appears to be a heavily compressed/encoded academic paper. While the document contains extensive data and tables, I cannot locate a clearly readable "Table 1" with specific Spearman correlation values (ρ) or the "+7.8%" LangRank improvement metric you're referencing.

The PDF encoding makes precise table extraction difficult. To help you find this information, I'd recommend:

1. **Access the original paper directly** - Request the PDF from the authors or your institution's library
2. **Check the paper's abstract or results section** - The key metrics are typically highlighted there
3. **Search for "LangRank"** in the document's searchable text version if available

If you can provide a clearer image or the paper's title/authors, I'd be happy to help locate these specific statistics in a more readable format.

[Binary content (application/pdf, 1.1MB) also saved to /home/ubuntu/.claude-account-1/projects/-/4b90db97-abf7-43ca-8746-d63916fc40be/tool-results/webfetch-1778401298620-ypxvrr.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f6b97f9b-8957-4f3b-b1bc-27a05b6535fa",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "2d6c7cf4-b7cf-4c64-bc18-10fc1299a3e7",
  "sourceToolAssistantUUID": "f6b97f9b-8957-4f3b-b1bc-27a05b6535fa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T08:21:44.279Z_

Excellent! I found the specific values. Now let me fetch the Budget-Xfer paper details and verify the p-value information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d6c7cf4-b7cf-4c64-bc18-10fc1299a3e7",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZfHpY48E4VzVcP9xHe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "969b5cbd-c55f-4fc7-8d3b-31396a73c82d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HjEarG4f8RARrxHb1zVHjz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2302,
      "cache_read_input_tokens": 21267,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2302,
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

_source line 27 · 2026-05-10T08:21:44.799Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AzmNX5ZZ6K73VkXbkfJCK6`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.27651",
  "prompt": "Confirm the submission status - is this a preprint submitted to SIGIR 2026 or already accepted/published?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "969b5cbd-c55f-4fc7-8d3b-31396a73c82d",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZfHpY48E4VzVcP9xHe",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aaa71e37-037d-4a34-b6aa-788c62e2657b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01HjEarG4f8RARrxHb1zVHjz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2302,
      "cache_read_input_tokens": 21267,
      "output_tokens": 138,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2302
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 138,
          "cache_read_input_tokens": 21267,
          "cache_creation_input_tokens": 2302,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2302,
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

_source line 28 · 2026-05-10T08:21:47.375Z_

<details><summary>↩ Tool result · `toolu_01AzmNX5ZZ6K73VkXbkfJCK6`</summary>

```text
# Submission Status

Based on the webpage content, this paper is a **preprint submitted to a conference**, not yet accepted or published.

The submission history clearly indicates: **"[v1] Sun, 29 Mar 2026 11:55:45 UTC"** with comments noting it was **"Submitted to SIGIR 2026 Short Paper track."**

The authors are presenting Budget-Xfer as a conference submission rather than a final accepted or published work. The paper's status remains that of a preprint awaiting peer review and acceptance decisions from the conference organizers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aaa71e37-037d-4a34-b6aa-788c62e2657b",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "06466e4e-251d-43d4-b506-dc7cfb5ed704",
  "sourceToolAssistantUUID": "aaa71e37-037d-4a34-b6aa-788c62e2657b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 29 · 2026-05-10T08:21:48.787Z_

Perfect! Now let me check on the p-value for the Laplacian Score result to see if p=0.061 is mentioned.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06466e4e-251d-43d4-b506-dc7cfb5ed704",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZfcyiAiU9Ea1PE7uYY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a59acec4-de22-4a8a-9958-4597b96cdbd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017qh8QKK6jxGEiHFCc22fNC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 23569,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 279,
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

_source line 30 · 2026-05-10T08:21:49.209Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01HmUrVpCb3VaJ3ZfhFB7Bfq`</summary>

```json
{
  "url": "https://arxiv.org/html/2509.20129v1",
  "prompt": "Find the statistical significance p-value associated with the Laplacian Score ρ=0.358 result, specifically looking for p=0.061"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a59acec4-de22-4a8a-9958-4597b96cdbd7",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZfcyiAiU9Ea1PE7uYY",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de0def48-b18a-44b8-8446-7c9dda2ce488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_017qh8QKK6jxGEiHFCc22fNC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 279,
      "cache_read_input_tokens": 23569,
      "output_tokens": 149,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 279
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 149,
          "cache_read_input_tokens": 23569,
          "cache_creation_input_tokens": 279,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 279,
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

_source line 31 · 2026-05-10T08:21:52.290Z_

<details><summary>↩ Tool result · `toolu_01HmUrVpCb3VaJ3ZfhFB7Bfq`</summary>

```text
# Statistical Significance of Laplacian Score Result

The p-value associated with the Laplacian Score alignment result is explicitly stated in the paper. According to the authors:

> "Notably, the Laplacian Score strategy achieves the strongest GdG_{d} alignment, with ρ=0.358 (p=0.061)"

While this correlation coefficient shows improvement over the baseline, the authors acknowledge that this result **does not reach conventional statistical significance** at the p=0.05 threshold. However, they argue the finding remains meaningful given the small sample size of 28 language pairs, stating: "the stronger alignments demonstrate the improved accuracy of distance-based comparisons between languages despite utilizing smaller feature sets."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de0def48-b18a-44b8-8446-7c9dda2ce488",
  "isSidechain": true,
  "promptId": "a0312e2a-edf7-40cd-ada9-d0cdec3b971e",
  "agentId": "aa73e51c9c574eb03",
  "type": "user",
  "uuid": "0df51c57-54e5-4403-8bf9-33f6c43213ff",
  "sourceToolAssistantUUID": "de0def48-b18a-44b8-8446-7c9dda2ce488",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T08:22:11.244Z_

Excellent! All the claims have been verified. Let me compile my findings:

## VERIFICATION REPORT

### **Task 1: "Less is More: The Effectiveness of Compact Typological Language Representations" (arXiv:2509.20129, EMNLP 2025)**

**VERIFIED - All specific claims are accurate:**

✓ **Laplacian Score 300-feature URIEL+ subset**: ρ = 0.358 (p = 0.061) - **CONFIRMED**
  - This is indeed measured against linguistic distance alignment metric G_d (Table 1)
  - The p-value of 0.061 indicates it approaches but does not reach conventional significance (p<0.05)

✓ **Full 800-feature set baseline**: ρ = 0.260 - **CONFIRMED**
  - This is the baseline URIEL+ result in Table 1

✓ **LangRank downstream task improvement**: +7.8% - **CONFIRMED**
  - Specifically: "For LangRank, the LS [Laplacian Score] and CFS methods outperform the full feature set baseline at smaller subset sizes, with peak gains of +7.8% (size 300)"

**Paper Details:**
- Published at EMNLP 2025 (Suzhou, China)
- Authors: York Hay Ng, Phuong Hanh Hoang, En-Shiun Annie Lee
- ACL Anthology: [https://aclanthology.org/2025.emnlp-main.1310/](https://aclanthology.org/2025.emnlp-main.1310/)
- arXiv: [https://arxiv.org/abs/2509.20129](https://arxiv.org/abs/2509.20129)

---

### **Task 2: Budget-Xfer Status (arXiv:2603.27651)**

**VERIFIED - Preprint status confirmed:**

✓ **Still a preprint**: Submitted to SIGIR 2026 Short Paper track - **CONFIRMED**
- Submission date: March 29, 2026
- Status: Not yet accepted/published
- arXiv: [https://arxiv.org/abs/2603.27651](https://arxiv.org/abs/2603.27651)

**Paper Details:**
- Title: "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages"
- Authors: Tewodros Kederalah Idris, Roald Eiselen, Prasenjit Mitra
- Focus: Multi-source cross-lingual transfer for African languages (Hausa, Yoruba, Swahili)
- Key finding: Practitioners should distribute data across multiple source languages rather than concentrate on a single source

---

### **Task 3: Competing Papers (April-May 2026)**

**Search 1: "typological distance multilingual instruction tuning 2026"**
- Found relevant work: "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?" (arXiv:2410.07809)
  - Uses 289-dimensional URIEL features for language selection
  - Employs k-means clustering for language subset selection
  - Finding: Only 40 multilingual examples + diversifying with 2-4 languages significantly improves cross-lingual generalization

**Search 2: "multi-pivot cross-lingual transfer low-resource 2026"**
- Found: "Semantic Pivots Enable Cross-Lingual Transfer in Large Language Models" (arXiv:2505.16385)
- Found: "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning"
- Key approach: Using high-resource languages (e.g., English) as pivots to enhance instruction tuning in lower-resource languages

**Search 3: "URIEL typological instruction tuning arxiv 2026"**
- **"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"** (arXiv:2510.27183, March 2026)
  - Extends URIEL+ with script vectors for 7,488 languages
  - Integrates Glottolog adding 18,710 additional languages
  - Results: 14% reduction in feature sparsity, up to 19,015 language coverage increase (1,007%), 35% improvement in imputation metrics
  - arXiv: [https://arxiv.org/abs/2510.27183](https://arxiv.org/abs/2510.27183)

- **"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"** (arXiv:2510.19217, March 2026)
  - Proposes structure-aware representations: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variable models for typology
  - arXiv: [https://arxiv.org/abs/2510.19217](https://arxiv.org/abs/2510.19217)

**Search 4: "Kazakh Mongolian Uyghur LLM instruction tuning 2026"**
- **"MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages"** (2026)
  - Comprehensive framework: 24K instances across 9 tasks
  - Languages: Kazakh, Mongolian, Uyghur, Tibetan
  - arXiv: [https://arxiv.org/html/2503.01150v1](https://arxiv.org/html/2503.01150v1)

- **"Llama-3.1-Sherkala-8B-Chat: An Open Large Language Model for Kazakh"** (2026)
  - State-of-the-art instruction-tuned model
  - Training: 45.3B tokens (Kazakh, English, Russian, Turkish)
  - Leverages translated instruction datasets and Kazakhstan-specific safety data
  - arXiv: [https://arxiv.org/html/2503.01493v1](https://arxiv.org/html/2503.01493v1)

- **"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur"** (COLING 2025)
  - Four-stage strategy: data collection, continuous pre-training, fine-tuning with translation supervision, DPOSE (direct preference optimization based on translation self-evolution)
  - ACL Anthology: [https://aclanthology.org/2025.coling-main.559/](https://aclanthology.org/2025.coling-main.559/)

---

## Summary

All claims in Task 1 are **verified with exact numerical precision**. Task 2 confirms Budget-Xfer remains a preprint. Task 3 identified several competing papers from 2025-2026, with the most directly relevant recent papers being the URIEL+ expansions (March 2026) and the Sherkala-Chat and MiLiC-Eval benchmarks focused on Asian low-resource languages.

Sources:
- [Less is More: EMNLP 2025](https://aclanthology.org/2025.emnlp-main.1310/)
- [arXiv 2509.20129](https://arxiv.org/abs/2509.20129)
- [Budget-Xfer arXiv 2603.27651](https://arxiv.org/abs/2603.27651)
- [Simple Additions, Substantial Gains URIEL+ (2510.27183)](https://arxiv.org/abs/2510.27183)
- [Modality Matching Matters URIEL+ (2510.19217)](https://arxiv.org/abs/2510.19217)
- [MiLiC-Eval](https://arxiv.org/html/2503.01150v1)
- [Sherkala-Chat for Kazakh](https://arxiv.org/html/2503.01493v1)
- [Low-Resource Uyghur LLM](https://aclanthology.org/2025.coling-main.559/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0df51c57-54e5-4403-8bf9-33f6c43213ff",
  "isSidechain": true,
  "agentId": "aa73e51c9c574eb03",
  "requestId": "req_011CatZfyv3BT3ojyghFaVpU",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fecdff0b-433d-4e81-baa8-b1fc5c4738b9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "4b90db97-abf7-43ca-8746-d63916fc40be",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01H9rtc8Zpd8VDW7ftv7odG1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 319,
      "cache_read_input_tokens": 23848,
      "output_tokens": 2003,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 319
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 2003,
          "cache_read_input_tokens": 23848,
          "cache_creation_input_tokens": 319,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 319,
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
