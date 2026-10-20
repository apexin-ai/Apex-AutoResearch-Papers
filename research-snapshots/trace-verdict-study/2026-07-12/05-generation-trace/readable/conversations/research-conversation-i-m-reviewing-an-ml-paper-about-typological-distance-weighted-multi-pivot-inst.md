# Research conversation: I'm reviewing an ML paper about typological-distance-weighted multi-pivot instruction tuning for low-resource languages 

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 22
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-af17d75195abb567d.jsonl`
- **Structured JSON:** [`4928cbdaed21a89668c0.json`](../../sessions/49/4928cbdaed21a89668c0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-10T08:07:22.687Z_

I'm reviewing an ML paper about typological-distance-weighted multi-pivot instruction tuning for low-resource languages (Kazakh, Mongolian, Uyghur). I need you to search for any competing or closely related work that might undermine the novelty of this paper. Please search for:

1. "typological distance multilingual instruction tuning 2025 2026" on arxiv
2. "multi-pivot cross-lingual transfer instruction tuning 2025 2026" 
3. "low-resource Kazakh Mongolian Uyghur language model instruction 2025 2026"
4. "PROM pivoted regulated optimization multilingual NAACL 2025" - verify this exists and its ACL Anthology URL
5. "Budget-Xfer cross-lingual transfer budget constrained arxiv 2603.27651" - verify this exists
6. Search for any recent (2025-2026) papers on cross-lingual instruction tuning with typological features

Report what you find, including paper titles, venues, and whether they overlap with the proposed method's core claims of: (a) typological-distance weighting for pivot selection, (b) staged curriculum from close to distant pivots, (c) multi-source DPO for cross-lingual instruction following.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "5f162943-7998-4e01-855e-b6479f0153e3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T08:07:23.728Z_

I'll conduct a thorough search for competing and related work on typological-distance-weighted multi-pivot instruction tuning for low-resource languages. Let me search the literature systematically.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5f162943-7998-4e01-855e-b6479f0153e3",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6062a84a-1ce8-4fd3-94d5-16ec60e55239",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 3 · 2026-05-10T08:07:23.996Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016PyUbM5cJ7fjqSx7ofDBM1`</summary>

```json
{
  "query": "typological distance multilingual instruction tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6062a84a-1ce8-4fd3-94d5-16ec60e55239",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ee1717b9-add4-4a43-80cc-dc0420733e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 4 · 2026-05-10T08:07:24.158Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ns5fUj5FmQut8Sah9VY17j`</summary>

```json
{
  "query": "multi-pivot cross-lingual transfer instruction tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ee1717b9-add4-4a43-80cc-dc0420733e83",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8c7954d8-32a7-4ea4-8492-540b92d7cd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 5 · 2026-05-10T08:07:24.165Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KzBMPWp4SqJLPVvBoahNNQ`</summary>

```json
{
  "query": "low-resource Kazakh Mongolian Uyghur language model instruction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c7954d8-32a7-4ea4-8492-540b92d7cd32",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "57baea3f-7d42-4228-b293-82363d945a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 6 · 2026-05-10T08:07:24.380Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZg5r4dmKJi6GPhu4t51c1`</summary>

```json
{
  "query": "PROM pivoted regulated optimization multilingual NAACL 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57baea3f-7d42-4228-b293-82363d945a94",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a7a60ba9-f0cc-4216-af11-b6e8ba1c7e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 7 · 2026-05-10T08:07:24.592Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BQ9gWxpRb7Lr1vyCTgdqP5`</summary>

```json
{
  "query": "Budget-Xfer cross-lingual transfer budget constrained arxiv 2603.27651"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a7a60ba9-f0cc-4216-af11-b6e8ba1c7e87",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f5e62190-4f81-4667-ae88-813931c81a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 725,
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

_source line 8 · 2026-05-10T08:07:24.751Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NWf6rsD25e94Ro9WjypALa`</summary>

```json
{
  "query": "cross-lingual instruction tuning typological features 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f5e62190-4f81-4667-ae88-813931c81a89",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYZt2nqCmmNWaU3YuPs",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "51a0e4e1-ed14-41b7-b4c5-bc3526442a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_016TS6ckCVvysVeYwwgUaWac",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 725,
      "cache_read_input_tokens": 16155,
      "output_tokens": 368,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 725
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 368,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 725,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 725,
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

_source line 9 · 2026-05-10T08:07:30.194Z_

<details><summary>↩ Tool result · `toolu_01BQ9gWxpRb7Lr1vyCTgdqP5`</summary>

```text
Web search results for query: "Budget-Xfer cross-lingual transfer budget constrained arxiv 2603.27651"

Links: [{"title":"[2603.27651] Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/abs/2603.27651"},{"title":"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/html/2603.27651"},{"title":"Multi-Source Cross-Lingual Model Transfer: Learning What to Share | Request PDF","url":"https://www.researchgate.net/publication/335780754_Multi-Source_Cross-Lingual_Model_Transfer_Learning_What_to_Share"},{"title":"[2603.21036] Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/abs/2603.21036"},{"title":"[2505.14297] Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/abs/2505.14297"},{"title":"Cross-Lingual Optimization for Language Transfer in Large Language Models","url":"https://arxiv.org/html/2505.14297v1"},{"title":"An Empirical Study of Cross-Lingual Transfer Learning in Programming Languages","url":"https://arxiv.org/html/2310.16937v2"},{"title":"Cross-Lingual Transfer Learning for Low-Resource Speech Translation","url":"https://arxiv.org/html/2306.00789v3"},{"title":"[2502.02722] Cross-Lingual Transfer for Low-Resource Natural Language Processing","url":"https://arxiv.org/abs/2502.02722"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036"}]

Based on the search results, I found the paper you're looking for:

Budget-Xfer is a framework that formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem. Given a fixed annotation budget B, the framework jointly optimizes which source languages to include and how much data to allocate from each.

The paper addresses the fact that cross-lingual transfer learning enables NLP for low-resource languages by leveraging labeled data from higher-resource sources, yet existing comparisons of source language selection strategies do not control for total training data, confounding language selection effects with data quantity effects.

The researchers evaluated four allocation strategies across named entity recognition and sentiment analysis for three African target languages (Hausa, Yoruba, Swahili) using two multilingual models, conducting 288 experiments.

The paper was submitted to arXiv on March 29, 2026, and is authored by Tewodros Kederalah Idris and two other co-authors. You can access the full paper at https://arxiv.org/abs/2603.27651.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5e62190-4f81-4667-ae88-813931c81a89",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "71f8486a-c1c0-4a52-bb90-d750e78aa0fe",
  "sourceToolAssistantUUID": "f5e62190-4f81-4667-ae88-813931c81a89",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T08:07:31.561Z_

<details><summary>↩ Tool result · `toolu_01NWf6rsD25e94Ro9WjypALa`</summary>

```text
Web search results for query: "cross-lingual instruction tuning typological features 2025 2026"

Links: [{"title":"Empowering Cross-lingual Behavioral Testing of NLP Models with Typological Features","url":"https://www.researchgate.net/publication/372286109_Empowering_Cross-lingual_Behavioral_Testing_of_NLP_Models_with_Typological_Features"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34524/36679"},{"title":"Contrastive pre-training and instruction tuning for cross-lingual aspect-based sentiment analysis | Applied Intelligence | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10489-025-06251-5"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment - ACL Anthology","url":"https://aclanthology.org/2025.sumeval-2.2/"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"Cross-Lingual Knowledge Transfer","url":"https://www.emergentmind.com/topics/cross-lingual-knowledge-transfer"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34524"},{"title":"Tackling Low-Resource NMT with Instruction-Tuned LLaMA","url":"https://www2.statmt.org/wmt25/pdf/2025.wmt-1.97.pdf"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"}]

Based on the search results, I've found several relevant recent studies on cross-lingual instruction tuning and typological features. Here's what the research shows:

## Recent Work on Cross-Lingual Instruction Tuning with Typological Features (2024-2026)

### Key Approaches

Cross-lingual in-context few-shot learning encourages multilingual alignment in instruction tuning with mixed language tokens, while a randomly online CoT (Chain-of-Thought) strategy promotes the multilingual reasoning ability of LLMs.

The CrossIn approach utilizes a mixed composition of cross-lingual instruction tuning data and leverages the compressed representation shared by various languages to efficiently enhance the model's task-solving capabilities and multilingual proficiency within a single process.

### Using Typological Features for Language Selection

Linguistically informed selection techniques range from common methods such as typological feature vectors, to less conventional but promising approaches including language embeddings derived from semantic typology features. K-means clustering can select fixed numbers of languages based on these techniques, with instruction-tuning models measuring cross-lingual and cross-task performance on natural language understanding and commonsense reasoning tasks.

### Performance and Challenges

State-of-the-art language models show generalization failures to specific typological characteristics such as temporal expressions in Swahili and compounding possessives in Finnish.

Research shows conflicting evidence on multilingual fine-tuning strategies, with some studies indicating that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51a0e4e1-ed14-41b7-b4c5-bc3526442a98",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "009f4f32-b80b-4a80-99d1-b6f4072546b3",
  "sourceToolAssistantUUID": "51a0e4e1-ed14-41b7-b4c5-bc3526442a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T08:07:32.120Z_

<details><summary>↩ Tool result · `toolu_016PyUbM5cJ7fjqSx7ofDBM1`</summary>

```text
Web search results for query: "typological distance multilingual instruction tuning 2025 2026"

Links: [{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://dl.acm.org/doi/pdf/10.1145/3777411"},{"title":"Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models","url":"https://arxiv.org/html/2410.16006v3"},{"title":"Instruction Tuning for Large Language Models: A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3777411"},{"title":"How Many Languages Make Good Multilingual Instruction Tuning? A Case Study on BLOOM","url":"https://arxiv.org/html/2404.04850v2"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"[2601.01362] Investigating the Multilingual Calibration Effects of Language Model Instruction-Tuning","url":"https://arxiv.org/abs/2601.01362"}]

Here are the search results for "typological distance multilingual instruction tuning 2025 2026":

## Key Research Areas

The search reveals several recent papers addressing the intersection of typological distance and multilingual instruction tuning:

### Linguistically-Informed Language Selection

Research hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner, investigating various language selection techniques and comparing them to baselines such as randomly selected subsets, subsets curated by picking a single language from each language family, and all languages available in the dataset.

Linguistically informed selection techniques range from common methods, such as typological feature vectors, to less conventional but promising approaches, including language embeddings derived from semantic typology features, with a simple k-means clustering algorithm applied to select a fixed number of languages based on each technique.

### Typological Distance Measures

Research adopts different similarity measures based on syntactic, geographic, phonological, genetic, inventory, and featural distances scored by lang2vec. These measures are used to understand how language similarity affects multilingual instruction tuning outcomes.

### Conflicting Findings on Language Diversity

Current research presents conflicting evidence on multilingual fine-tuning strategies, with some studies showing that scaling the number of tasks or languages during instruction tuning improves cross-lingual generalization, while others report that just 1–3 fine-tuning languages effectively trigger cross-lingual transfer.

### Recent Developments (2025-2026)

A common fine-tuning strategy is to train LLMs on an instruction-following dataset containing a mixture of languages, though these datasets are often heavily skewed toward English and other high-resource languages; further, fine-tuning on a dataset containing only non-English languages can hurt the model's performance on English due to catastrophic forgetting.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ee1717b9-add4-4a43-80cc-dc0420733e83",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "394c8083-7432-47ac-9253-064b6d188745",
  "sourceToolAssistantUUID": "ee1717b9-add4-4a43-80cc-dc0420733e83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T08:07:32.141Z_

<details><summary>↩ Tool result · `toolu_01XZg5r4dmKJi6GPhu4t51c1`</summary>

```text
Web search results for query: "PROM pivoted regulated optimization multilingual NAACL 2025"

Links: [{"title":"PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning - ACL Anthology","url":"https://aclanthology.org/2025.naacl-short.19/"},{"title":"PROM: Pivoted and Regulated Optimization for Multilingual ...","url":"https://aclanthology.org/2025.naacl-short.19.pdf"},{"title":"NAACL 2025 Annual Conference of the Nations of the Americas Chapter of","url":"https://aclanthology.org/2025.naacl-short.0.pdf"},{"title":"Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (Volume 2: Short Papers) - ACL Anthology","url":"https://aclanthology.org/volumes/2025.naacl-short/"},{"title":"NAACL 2025 - Amazon Science","url":"https://www.amazon.science/conferences-and-events/naacl-2025"},{"title":"Accepted Papers - NAACL-HLT 2025","url":"https://2025.naacl.org/program/accepted_papers/"},{"title":"Local Prompt Optimization","url":"https://aclanthology.org/2025.naacl-short.7.pdf"},{"title":"PROPEL: Prompt Optimization with Expert Priors for Small and Medium-sized LLMs - ACL Anthology","url":"https://aclanthology.org/2025.knowledgenlp-1.25/"},{"title":"2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics - NAACL-HLT 2025","url":"https://2025.naacl.org/"},{"title":"EMNLP 2025 The 2025 Conference on Empirical Methods in Natural","url":"https://aclanthology.org/2025.emnlp-tutorials.pdf"}]

I found information about the PROM paper from NAACL 2025. Here are the search results:

## PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning

PROM addresses the challenge of adapting language models to underrepresented languages by identifying English as an internal pivot language and disentangling the roles of English and target language data in training through two pivoted objectives and regulation between them.

**Key Details:**
- Authors: Jaeseong Lee, Seung-won Hwang, Hojin Lee, Yunju Bak, and Changmin Lee, published in the Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL 2025)

- **Problem:** The lack of instruction-tuning datasets in languages other than English limits their application to diverse languages, and researchers have adapted English-centric LLMs to other languages by appending English tuning data with its translated pair

- **Solution:** The contribution identifies English as an internal pivot language and disentangles the roles of English and target language data in training by designing two roles as pivoted objectives, while also proposing to regulate between the two to better generalize for under-represented languages

- **Results:** Experiments across various languages demonstrate the effectiveness of the approach on multiple benchmarks, with code publicly available for further exploration


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7a60ba9-f0cc-4216-af11-b6e8ba1c7e87",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "a6eedfca-a8c7-442c-9b85-d8d74586cad1",
  "sourceToolAssistantUUID": "a7a60ba9-f0cc-4216-af11-b6e8ba1c7e87",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:07:32.956Z_

<details><summary>↩ Tool result · `toolu_01KzBMPWp4SqJLPVvBoahNNQ`</summary>

```text
Web search results for query: "low-resource Kazakh Mongolian Uyghur language model instruction 2025 2026"

Links: [{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China’s Minority Languages","url":"https://arxiv.org/html/2503.01150v1"},{"title":"Speech Recognition and Synthesis Models and Platforms for the Kazakh Language","url":"https://www.mdpi.com/2078-2489/16/10/879"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...","url":"https://aclanthology.org/2025.findings-acl.578.pdf"},{"title":"ISTIC’s Neural Machine Translation Systems for CCMT’ 2023 | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-99-7894-6_9"},{"title":"Fine-Tuning Large Language Models for Kazakh Text Simplification | MDPI","url":"https://www.mdpi.com/2076-3417/15/15/8344"},{"title":"Low-Resource Language Expansion and Translation ...","url":"https://aclanthology.org/2025.coling-main.559.pdf"},{"title":"Do Chinese models speak Chinese languages?","url":"https://arxiv.org/html/2504.00289v1"},{"title":"MiLMo:Minority Multilingual Pre-trained Language Model","url":"https://arxiv.org/pdf/2212.01779"}]

I found several recent research results on low-resource language models for Kazakh, Mongolian, and Uyghur. Here are the key findings:

## Recent Research (2025-2026)

**Low-Resource Language Expansion for Uyghur:**
A study published at COLING 2025 involves four stages: collecting and pre-processing monolingual data, conducting continuous pre-training with extensive monolingual data, fine-tuning with less parallel corpora using translation supervision, and proposing a direct preference optimization based on translation self-evolution (DPOSE). Extensive experiments showed that this strategy effectively expands the low-resource languages supported by large language models and significantly enhances the model's translation ability in Uyghur with less parallel data.

**Kazakh Language Models:**
A 1.94B parameter LLaMA-based model demonstrates how strong, culturally aligned performance can be achieved for Kazakh without massive infrastructure. The model compilation includes a rigorously cleaned, mixed-domain Kazakh corpus with a tokenizer that respects the language's agglutinative morphology, mixed-script usage, and diacritics, built in two stages: causal language modeling from scratch followed by instruction tuning.

**Benchmarking Minority Languages:**
MiLiC-Eval, a comprehensive framework with 24K instances across 9 tasks, was introduced focusing on 4 Minority Languages in China. Current LLMs exhibit a decent understanding of Uyghur, and a preliminary understanding of Tibetan and Kazakh, but struggle with comprehending Mongolian.

**Kazakh Text Simplification:**
KazSim, an instruction-tuned model built on multilingual large language models, addresses text simplification task for Kazakh, a morphologically rich, low-resource language.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "57baea3f-7d42-4228-b293-82363d945a94",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "754fa8ae-f340-497b-ab18-1077b7060852",
  "sourceToolAssistantUUID": "57baea3f-7d42-4228-b293-82363d945a94",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T08:07:34.282Z_

<details><summary>↩ Tool result · `toolu_01Ns5fUj5FmQut8Sah9VY17j`</summary>

```text
Web search results for query: "multi-pivot cross-lingual transfer instruction tuning 2025 2026"

Links: [{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | Request PDF","url":"https://www.researchgate.net/publication/384213466_PLUG_Leveraging_Pivot_Language_in_Cross-Lingual_Instruction_Tuning"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2023arXiv231108711Z/abstract"},{"title":"GitHub - ytyz1307zzh/PLUG: Code for the ACL 2024 paper \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"","url":"https://github.com/ytyz1307zzh/PLUG"},{"title":"Zero-shot cross-lingual transfer in instruction tuning of large language models","url":"https://arxiv.org/html/2402.14778v2"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.379/"},{"title":"(PDF) Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://www.researchgate.net/publication/397087634_Revisiting_Multilingual_Data_Mixtures_in_Language_Model_Pretraining"},{"title":"[2402.14778] Zero-shot cross-lingual transfer in instruction tuning of large language models","url":"https://arxiv.org/abs/2402.14778"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning - Paper Detail","url":"https://deeplearn.org/arxiv/431549/plug:-leveraging-pivot-language-in-cross-lingual-instruction-tuning"}]

Based on the search results, here are the key findings about multi-pivot cross-lingual transfer instruction tuning:

## Key Research: PLUG Method

PLUG (Pivot Language gUided Generation) is an approach that utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages by training the model to first process instructions in the pivot language, and then produce responses in the target language.

PLUG was published in the 62nd Annual Meeting of the Association for Computational Linguistics (ACL 2024).

## Addressing Cross-Lingual Challenges

Despite the success in high-resource languages, instruction tuning's application in lower-resource ones faces challenges due to the imbalanced foundational abilities of LLMs across different languages, stemming from the uneven language distribution in their pre-training data.

## Evaluation and Results

To evaluate the PLUG approach, researchers introduced a benchmark called X-AlpacaEval with instructions in 4 languages (Chinese, Korean, Italian, and Spanish), each annotated by professional translators.

PLUG significantly improves the instruction-following abilities of LLMs in multiple target languages (Chinese, Korean, Italian, Spanish), compared to directly responding in the target language alone.

## Recent Related Work

Using English as a pivot language—a high-resource language that serves as a catalyst for multilingual generalization—yields benefits across language families, and contrary to expectations, selecting a pivot language from within a specific family does not consistently improve performance for languages within that family.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8c7954d8-32a7-4ea4-8492-540b92d7cd32",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "d94fd8ab-fccb-41f7-abbe-1f11726aa659",
  "sourceToolAssistantUUID": "8c7954d8-32a7-4ea4-8492-540b92d7cd32",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T08:07:35.857Z_

Excellent! I've found substantial competing and related work. Let me search for additional details on some of these papers and verify their specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d94fd8ab-fccb-41f7-abbe-1f11726aa659",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4712252b-f0c4-408b-8f5c-69c40bcebad4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-10T08:07:36.549Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0112uxqCV32fzmukAbqfwM9A`</summary>

```json
{
  "url": "https://aclanthology.org/2025.naacl-short.19.pdf",
  "prompt": "What are the core methodological contributions of PROM? Does it use typological distance, multi-pivot selection, or curriculum learning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4712252b-f0c4-408b-8f5c-69c40bcebad4",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "af4968de-d46e-46c8-8ec9-950197ea1cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-10T08:07:37.190Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01XgKZD75fQZgZRzFmKNLp8c`</summary>

```json
{
  "url": "https://aclanthology.org/2024.acl-long.379/",
  "prompt": "What is the PLUG method? Does it use multiple pivots, typological distance, or curriculum learning strategies?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "af4968de-d46e-46c8-8ec9-950197ea1cb3",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "38c27200-b140-4b66-a80e-110d70d4a64a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-10T08:07:37.837Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_013Hi4pjPbsttGMWGmVabyK7`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.07809",
  "prompt": "What methods does this paper use for selecting languages in multilingual instruction tuning? Does it use typological features or distance metrics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c27200-b140-4b66-a80e-110d70d4a64a",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0e69494b-b7a6-4b8a-83e0-30d2fe035d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-10T08:07:37.851Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01AT1Lz5e9dHz3H8JKCBnkAV`</summary>

```json
{
  "query": "XCOT cross-lingual instruction tuning chain of thought AAAI 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0e69494b-b7a6-4b8a-83e0-30d2fe035d8b",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3d204639-9a34-4609-9246-2b5e29b6430c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-10T08:07:38.152Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011Nnbm5jKaexRbedXgd3KM3`</summary>

```json
{
  "query": "CrossIn cross-lingual knowledge alignment instruction tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d204639-9a34-4609-9246-2b5e29b6430c",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "88b80bef-78b7-4021-ba30-708deb46ae4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 3069,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-10T08:07:38.373Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0168ZWucYFW8xbhUinwB1yaL`</summary>

```json
{
  "query": "DPO direct preference optimization multilingual cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88b80bef-78b7-4021-ba30-708deb46ae4c",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYajdJL4kdqGCW7JtHE",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b5c7a66-13d4-49a7-abe2-413fbbacc8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01294PXy11B8dqBfctxuZofY",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3579,
      "cache_creation_input_tokens": 3069,
      "cache_read_input_tokens": 16880,
      "output_tokens": 485,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3069
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3579,
          "output_tokens": 485,
          "cache_read_input_tokens": 16880,
          "cache_creation_input_tokens": 3069,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3069,
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

_source line 22 · 2026-05-10T08:07:40.660Z_

<details><summary>↩ Tool result · `toolu_01XgKZD75fQZgZRzFmKNLp8c`</summary>

```text
# PLUG Method Overview

Based on the provided content, PLUG (pivot language guided generation) is an approach that "utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages."

## Key Mechanism

The method trains models to first process instructions in the pivot language, then generate responses in the target language. This two-stage approach reportedly achieves "a significant improvement in the instruction-following abilities of LLMs by 29% on average" compared to direct target-language responses.

## Multiple Pivots

The document indicates PLUG does explore alternative pivots beyond English. It mentions "employing alternative pivot languages beyond English to assist languages where LLMs exhibit lower proficiency."

## Typological Distance and Curriculum Learning

The provided content does **not** discuss typological distance or curriculum learning strategies. The excerpt focuses on the core pivot mechanism, the X-AlpacaEval benchmark (covering Chinese, Korean, Italian, and Spanish), and empirical improvements, but omits technical details about whether these advanced strategies are employed.

For comprehensive information on these aspects, consulting the full PDF would be necessary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38c27200-b140-4b66-a80e-110d70d4a64a",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "e104b0a3-c602-446b-a57c-69c6fa366e51",
  "sourceToolAssistantUUID": "38c27200-b140-4b66-a80e-110d70d4a64a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T08:07:40.989Z_

<details><summary>↩ Tool result · `toolu_0112uxqCV32fzmukAbqfwM9A`</summary>

```text
I cannot provide a reliable answer based on the content provided. The document appears to be a PDF containing compressed/encoded text streams that are not human-readable in the format presented. While object references to papers and figures are visible (such as references to "intro_fig.pdf" and "analysis_fig.pdf"), the actual textual content describing PROM's methodological contributions is not accessible in the given material.

To answer your question about PROM's core methodological contributions—whether it employs typological distance, multi-pivot selection, or curriculum learning—I would need access to the paper's readable text sections, abstract, or methodology sections.

[Binary content (application/pdf, 260.8KB) also saved to /home/ubuntu/.claude-account-2/projects/-/5ac41372-3de1-44fd-887d-d5fb9f425ba6/tool-results/webfetch-1778400458023-cvxcmu.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af4968de-d46e-46c8-8ec9-950197ea1cb3",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "641e9e6c-8c59-4d3f-b083-50da1e3e7fab",
  "sourceToolAssistantUUID": "af4968de-d46e-46c8-8ec9-950197ea1cb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-10T08:07:41.884Z_

<details><summary>↩ Tool result · `toolu_013Hi4pjPbsttGMWGmVabyK7`</summary>

```text
# Language Selection Methods

Based on the abstract provided, the paper proposes **linguistically-informed language selection** for multilingual instruction tuning, but specific methodological details aren't fully specified in this excerpt.

The abstract states: "Our study proposes a method to select languages for instruction tuning in a linguistically informed way" and mentions "a simple algorithm to choose diverse languages."

It further notes that the approach involves "selecting diverse languages based on linguistic features that could help develop better multilingual systems."

However, the abstract doesn't explicitly detail whether typological features, distance metrics, or other specific technical approaches are used. The paper indicates that "all resources, including the code for language selection...are made available" in their repository, suggesting the complete methodology would be found in the full paper rather than this summary.

To determine the exact methods employed (whether typological features, linguistic distance calculations, or other metrics), you would need to access the complete PDF or HTML version of the paper.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e69494b-b7a6-4b8a-83e0-30d2fe035d8b",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "1892e689-8a23-4bfc-afa4-0999fee257a1",
  "sourceToolAssistantUUID": "0e69494b-b7a6-4b8a-83e0-30d2fe035d8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-10T08:07:43.759Z_

<details><summary>↩ Tool result · `toolu_01AT1Lz5e9dHz3H8JKCBnkAV`</summary>

```text
Web search results for query: "XCOT cross-lingual instruction tuning chain of thought AAAI 2025"

Links: [{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34524"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual","url":"https://ojs.aaai.org/index.php/AAAI/article/download/34524/36679"},{"title":"xCoT | Proceedings of the Thirty-Ninth AAAI Conference on Artificial Intelligence and Thirty-Seventh Conference on Innovative Applications of Artificial Intelligence and Fifteenth Symposium on Educational Advances in Artificial Intelligence","url":"https://dl.acm.org/doi/10.1609/aaai.v39i22.34524"},{"title":"[2401.07037] xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning","url":"https://arxiv.org/abs/2401.07037"},{"title":"AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through Adaptive Multilingual Chain-of-Thought","url":"https://arxiv.org/html/2501.16154"},{"title":"xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning","url":"https://arxiv.org/html/2401.07037v1"},{"title":"AdaMCoT: Rethinking Cross-Lingual Factual Reasoning through","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40678/44639"},{"title":"XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | Request PDF","url":"https://www.researchgate.net/publication/390700232_XCOT_Cross-lingual_Instruction_Tuning_for_Cross-lingual_Chain-of-Thought_Reasoning"},{"title":"[PDF] xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/606b535686f98015ea8dd3c9ba8aa9243bc9dc2d"},{"title":"xCoT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning | OpenReview","url":"https://openreview.net/forum?id=iBeqTjM38s_"}]

I found comprehensive information about XCOT! Here's what the research presents:

## XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning

XCOT was published in the Proceedings of the AAAI Conference on Artificial Intelligence in 2025.

### Overview
Chain-of-thought (CoT) has emerged as a powerful technique to elicit reasoning in large language models, but CoT mainly demonstrates excellent performance in English, while its usage in low-resource languages is constrained due to poor language generalization. To bridge the gap among different languages, XCOT proposes a cross-lingual instruction fine-tuning framework to transfer knowledge from high-resource languages to low-resource languages.

### Key Components
The framework includes three main approaches:

1. **Cross-lingual In-Context Few-Shot Learning (xICL):** This technique accelerates multilingual agreement in instruction tuning, where some fragments of source languages in examples are randomly substituted by their counterpart translations of target languages.

2. **Randomly Online CoT Strategy:** During multilingual instruction tuning, the framework adopts a randomly online CoT strategy to enhance the multilingual reasoning ability of the large language model by first translating the query to another language and then answering in English.

3. **Cross-lingual Distillation:** To further facilitate the language transfer, the framework leverages the high-resource CoT to supervise the training of low-resource languages with cross-lingual distillation.

### Results
Experimental results demonstrate the superior performance of xCoT in reducing the gap among different languages, highlighting its potential to reduce the cross-lingual gap.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d204639-9a34-4609-9246-2b5e29b6430c",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "62a6523d-9496-46cf-b681-18ed3b974ab2",
  "sourceToolAssistantUUID": "3d204639-9a34-4609-9246-2b5e29b6430c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-10T08:07:43.856Z_

<details><summary>↩ Tool result · `toolu_011Nnbm5jKaexRbedXgd3KM3`</summary>

```text
Web search results for query: "CrossIn cross-lingual knowledge alignment instruction tuning 2025"

Links: [{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment - ACL Anthology","url":"https://aclanthology.org/2025.sumeval-2.2/"},{"title":"[2404.11932] CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment","url":"https://arxiv.org/abs/2404.11932"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment","url":"https://arxiv.org/html/2404.11932"},{"title":"[2404.11932v1] CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment","url":"http://arxiv.org/abs/2404.11932v1"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/crossin-efficient-instruction-tuning-approach-cross-lingual"},{"title":"GitHub - Lingy12/CrossIn: CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment · GitHub","url":"https://github.com/Lingy12/CrossIn"},{"title":"[PDF] Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multilingual-Pretraining-and-Instruction-Tuning-But-Gao-Hu/8f2630c308b46ce02a06ff623fcbc130d481481d"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment - Consensus","url":"https://k8s.consensus.app/papers/crossin-an-efficient-instruction-tuning-approach-for-chen-wang/a2c4b6b33c775840a63178b33e6f4a9b/"},{"title":"CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment - 专知论文","url":"https://www.zhuanzhi.ai/paper/d464ab5b8bf8028a523df9e2cf4be38f"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/multilingual-pretraining-instruction-tuning-improve-cross-lingual"}]

Based on the search results, here's what I found about CrossIn:

## Overview

CrossIn is a novel approach that utilizes a mixed composition of cross-lingual instruction tuning data and leverages the compressed representation shared by various languages to efficiently enhance the model's task-solving capabilities and multilingual proficiency within a single process.

## Problem It Addresses

Multilingual proficiency presents a significant challenge for large language models, as English-centric models are usually suboptimal in other languages, particularly those that are linguistically distant from English, stemming from the imbalanced distribution of training data across languages during pre-training and instruction tuning stages.

## Approach

CrossIn utilizes two distinct types of instruction tuning datasets: the Complex Task Dataset (CTD), rich in diverse, high-quality and logical tasks like math and coding, and the Linguistic Uniformity Dataset (LUD), consisting of easier-to-translate, linguistically uniform tasks, merging cross-lingual instruction data from CTD with machine-translated data from LUD to reinforce knowledge alignment during instruction tuning.

## Results

Experimental results demonstrate that the method substantially improves performance across tasks and languages, and provides extensive insights into the impact of cross-lingual data volume and the integration of translation data on enhancing multilingual consistency and accuracy.

## Publication

The paper was published in the Proceedings of the Second Workshop on Scaling Up Multilingual & Multi-Cultural Evaluation in Abu Dhabi in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "88b80bef-78b7-4021-ba30-708deb46ae4c",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "5a199fb7-9f19-4148-9704-5ed56213a1da",
  "sourceToolAssistantUUID": "88b80bef-78b7-4021-ba30-708deb46ae4c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-10T08:07:46.268Z_

<details><summary>↩ Tool result · `toolu_0168ZWucYFW8xbhUinwB1yaL`</summary>

```text
Web search results for query: "DPO direct preference optimization multilingual cross-lingual 2025 2026"

Links: [{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"Backtranslation Augmented Direct Preference Optimization for Neural Machine Translation","url":"https://arxiv.org/html/2604.25702"},{"title":"[2305.18290] Direct Preference Optimization: Your Language Model is Secretly a Reward Model","url":"https://arxiv.org/abs/2305.18290"},{"title":"[2409.17673] Cross-lingual Human-Preference Alignment for Neural Machine Translation with Direct Quality Optimization","url":"https://arxiv.org/abs/2409.17673"},{"title":"Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment | Request PDF","url":"https://www.researchgate.net/publication/389649128_Implicit_Cross-Lingual_Rewarding_for_Efficient_Multilingual_Preference_Alignment"},{"title":"BPO: Revisiting Preference Modeling in Direct Preference Optimization | OpenReview","url":"https://openreview.net/forum?id=b97EwMUWu7"},{"title":"GitHub - junkangwu/Dr_DPO: [ICLR 2025] Official code of \"Towards Robust Alignment of Language Models: Distributionally Robustifying Direct Preference Optimization\" · GitHub","url":"https://github.com/junkangwu/Dr_DPO"},{"title":"[Literature Review] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://www.themoonlight.io/en/review/implicit-cross-lingual-rewarding-for-efficient-multilingual-preference-alignment"},{"title":"Direct Preference Optimization Explained In-depth","url":"https://www.tylerromero.com/posts/2024-04-dpo/"},{"title":"What is direct preference optimization (DPO)? | SuperAnnotate","url":"https://www.superannotate.com/blog/direct-preference-optimization-dpo"}]

Based on the search results, here's what I found about Direct Preference Optimization (DPO) applied to multilingual and cross-lingual settings in 2025-2026:

## Recent Research on Multilingual DPO

Direct Preference Optimization (DPO) has become a prominent method for aligning Large Language Models (LLMs) with human preferences, though multilingual preference alignment is hampered by data scarcity.

### Key 2025 Approach: Implicit Cross-Lingual Rewarding

A notable recent development is a novel approach that captures learned preferences from well-aligned English models by implicit rewards and transfers them to other languages through iterative training. This involves deriving an implicit reward model from the logits of an English DPO-aligned model and its corresponding reference model, then leveraging it to annotate preference relations in cross-lingual instruction-following pairs and using English instructions to evaluate multilingual responses.

Fine-tuning Llama3 for two iterations resulted in a 12.72% average improvement in Win Rate and a 5.97% increase in Length Control Win Rate across all training languages on the X-AlpacaEval leaderboard.

### Cross-Lingual Machine Translation Applications

A cross-lingual human-preference alignment method for neural machine translation using Direct Quality Optimization (DQO) builds on RLHF and DPO principles, introducing a batched online variant of DPO that uses a pre-trained translation quality estimation model as a proxy for human judgments, with improvements measured by BLEU, COMET, and human MQM evaluation.

### DPO Improvements in 2025-2026

Recent work has also focused on refining DPO itself, with research on enhancing preference modeling for direct preference optimization by dynamically balancing the optimization of chosen and rejected responses, addressing how DPO can neglect absolute reward magnitudes.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5b5c7a66-13d4-49a7-abe2-413fbbacc8e2",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "0ac12d9f-359d-49bb-b79a-29f0b6948014",
  "sourceToolAssistantUUID": "5b5c7a66-13d4-49a7-abe2-413fbbacc8e2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 28 · 2026-05-10T08:07:48.335Z_

Let me get more detailed information on specific papers to assess overlap with the proposed method.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ac12d9f-359d-49bb-b79a-29f0b6948014",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYbd2DDybUJSnbUzVZ5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fd547a26-c067-4d62-be1b-0efd9df27f26",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ke1HpXYhQv7wiRiQvYWjs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8075,
      "cache_read_input_tokens": 19949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8075,
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

_source line 29 · 2026-05-10T08:07:49.313Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01VTaEoAG1T4XFA5TEvsjmgv`</summary>

```json
{
  "url": "https://arxiv.org/html/2410.07809",
  "prompt": "Describe the full methodology for language selection. Does it use typological distance weighting? Does it employ curriculum learning or multi-source selection strategies?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fd547a26-c067-4d62-be1b-0efd9df27f26",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYbd2DDybUJSnbUzVZ5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "35aaf5a2-358c-4565-97b8-8d490f0dd220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ke1HpXYhQv7wiRiQvYWjs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8075,
      "cache_read_input_tokens": 19949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8075,
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

_source line 30 · 2026-05-10T08:07:49.956Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_016tSdVYLuhNQsZMvY5QzEyV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2401.07037",
  "prompt": "What is the core methodology of XCOT? Does it use typological distance, pivot language selection, or curriculum learning from close to distant language pairs?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "35aaf5a2-358c-4565-97b8-8d490f0dd220",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYbd2DDybUJSnbUzVZ5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8823ce6b-7cbb-4294-b8ca-511edca26d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ke1HpXYhQv7wiRiQvYWjs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8075,
      "cache_read_input_tokens": 19949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8075,
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

_source line 31 · 2026-05-10T08:07:50.485Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01M2aN5f7ezqNUqwSkgfZtoH`</summary>

```json
{
  "url": "https://arxiv.org/abs/2404.11932",
  "prompt": "What are the key methodological components of CrossIn? Does it use typological distance, multi-pivot selection, or curriculum strategies?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8823ce6b-7cbb-4294-b8ca-511edca26d53",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYbd2DDybUJSnbUzVZ5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1a5d9ed3-18b3-4711-a66e-ac8a067a6205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ke1HpXYhQv7wiRiQvYWjs1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8075,
      "cache_read_input_tokens": 19949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8075,
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

_source line 32 · 2026-05-10T08:07:50.590Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XtbkAdZsnbaqhe5amJdTgH`</summary>

```json
{
  "query": "\"typological distance\" \"curriculum learning\" multilingual instruction tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1a5d9ed3-18b3-4711-a66e-ac8a067a6205",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYbd2DDybUJSnbUzVZ5",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "23bebf4a-fe3c-4ed0-9cef-816d857bc15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Ke1HpXYhQv7wiRiQvYWjs1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 8075,
      "cache_read_input_tokens": 19949,
      "output_tokens": 369,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8075
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 369,
          "cache_read_input_tokens": 19949,
          "cache_creation_input_tokens": 8075,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8075,
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

_source line 33 · 2026-05-10T08:07:53.449Z_

<details><summary>↩ Tool result · `toolu_01M2aN5f7ezqNUqwSkgfZtoH`</summary>

```text
# CrossIn Methodological Components

Based on the provided content, the abstract does not specify the detailed methodological components you're asking about. 

The abstract states that CrossIn "utilizes a mixed composition of cross-lingual instruction tuning data" and "leverages the compressed representation shared by various languages to efficiently enhance the model's task-solving capabilities."

However, the webpage content does not indicate whether the approach employs:
- Typological distance metrics
- Multi-pivot selection strategies
- Curriculum learning approaches

To determine if CrossIn incorporates these specific methodological elements, you would need to access the full paper PDF or HTML version linked on the page, as the abstract provided only describes the general strategy of using cross-lingual instruction data composition without detailing these particular techniques.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1a5d9ed3-18b3-4711-a66e-ac8a067a6205",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "f937f050-9546-422d-ab3c-7ab65e12d259",
  "sourceToolAssistantUUID": "1a5d9ed3-18b3-4711-a66e-ac8a067a6205",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-10T08:07:53.948Z_

<details><summary>↩ Tool result · `toolu_016tSdVYLuhNQsZMvY5QzEyV`</summary>

```text
# xCoT Core Methodology

Based on the provided abstract, xCoT's methodology centers on **cross-lingual knowledge transfer** rather than the specific approaches you mentioned.

The key methodological components are:

1. **Multilingual instruction training data** ("xCOT-INSTRUCT") designed to encourage semantic alignment across languages

2. **Cross-lingual in-context few-shot learning (xICL)**, which "randomly substituted fragments of source languages in examples by their counterpart translations of target languages"

3. **Randomly online CoT strategy** that enhances reasoning by translating queries to alternate languages before responding in English

4. **Cross-lingual distillation**, leveraging "high-resource CoT to supervise the training of low-resource languages"

The abstract does **not mention** typological distance, pivot language selection, or curriculum learning approaches. Instead, xCoT focuses on semantic alignment through mixed-language examples and knowledge transfer from high-resource to low-resource languages, with emphasis on multilingual agreement during instruction tuning.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8823ce6b-7cbb-4294-b8ca-511edca26d53",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "a678fbc0-e30e-47fc-bdba-3a59d510de74",
  "sourceToolAssistantUUID": "8823ce6b-7cbb-4294-b8ca-511edca26d53",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-10T08:07:54.996Z_

<details><summary>↩ Tool result · `toolu_01VTaEoAG1T4XFA5TEvsjmgv`</summary>

```text
# Language Selection Methodology

The paper employs a **straightforward k-means clustering approach** rather than typological distance weighting, curriculum learning, or multi-source strategies.

## Core Algorithm

The method operates in three steps:

1. **Feature Extraction**: Language vectors are obtained from various sources (URIEL typological features, learned embeddings, geographic vectors, or semantic representations).

2. **K-means Clustering**: Features undergo clustering with k=14 clusters. The authors deliberately selected 14 to "align with the number of language families and also avoid the curse of multilinguality."

3. **Language Selection**: For each cluster centroid, the algorithm identifies "the closest feature vector to centroid" and selects that corresponding language, resulting in one representative per cluster.

## Feature Sources Tested

Rather than weighting schemes, the paper compares multiple **independent feature types**:
- TYPO: 289-dimensional binary features from URIEL
- LEARN: Embeddings from neural machine translation with typology prediction
- GEO: Geographic distance vectors
- SEM: Language embeddings from colexification analysis
- FAM: Language family (categorical baseline)
- RND: Random selection

The methodology is explicitly described as "embarrassingly simple," avoiding complex weighting or curriculum approaches in favor of systematic diversity sampling across different linguistic feature spaces.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "35aaf5a2-358c-4565-97b8-8d490f0dd220",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "1fa104f0-2b4f-4d30-aeb3-d5c750d0b6c2",
  "sourceToolAssistantUUID": "35aaf5a2-358c-4565-97b8-8d490f0dd220",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-10T08:07:58.119Z_

<details><summary>↩ Tool result · `toolu_01XtbkAdZsnbaqhe5amJdTgH`</summary>

```text
Web search results for query: ""typological distance" "curriculum learning" multilingual instruction tuning 2025"

Links: [{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Code-Switching Curriculum Learning for Multilingual ...","url":"https://aclanthology.org/2025.findings-acl.407.pdf"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Multilingual Curriculum Learning","url":"https://www.emergentmind.com/topics/multilingual-curriculum-learning"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"GitHub - Wang-ML-Lab/llm-continual-learning-survey: [CSUR 2025] Continual Learning of Large Language Models: A Comprehensive Survey · GitHub","url":"https://github.com/Wang-ML-Lab/llm-continual-learning-survey"}]

I found several relevant research papers on typological distance, curriculum learning, and multilingual instruction tuning from 2025. Here's what the search reveals:

## Key Findings:

**Typological Distance in Multilingual Training:**

Research on multilingual data mixtures explores early competition between strong languages with differing orthographic and typological properties, and recent work challenges the prevailing assumption that cross-lingual interference depends on language family, showing instead that it is primarily related to script.

**Curriculum Learning Approaches:**

Curriculum learning among pivot languages has been investigated as a potential path to greater multilingual generalization. Multilingual curriculum learning refers to training paradigms in which the presentation of training signals spanning multiple languages is dynamically scheduled to optimize generalization and transfer capacity, leveraging inductive biases, linguistic or cognitive theories, or model-centric feedback to arrange training sequences.

**Instruction Tuning with Language Selection:**

Research hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner, investigating various language selection techniques and comparing them to baselines such as randomly selected subsets and subsets curated by picking a single language from each language family.

**Code-Switching Curriculum Learning:**

Code-switching curriculum learning (CSCL) is motivated by patterns in bilingual human learners, with token- and sentence-level code-switched stages facilitating cross-lingual representation alignment and mitigating catastrophic forgetting during monolingual specialization.

The search results show active 2025 research on these topics, with multiple papers exploring how linguistic features and curriculum strategies can optimize multilingual LLM performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "23bebf4a-fe3c-4ed0-9cef-816d857bc15b",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "9be11b69-9c30-4a6d-b587-dd79b1ed8c82",
  "sourceToolAssistantUUID": "23bebf4a-fe3c-4ed0-9cef-816d857bc15b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-10T08:07:59.379Z_

Now let me search for any papers that specifically combine typological distance with staged/curriculum approaches or DPO.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9be11b69-9c30-4a6d-b587-dd79b1ed8c82",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYcVZXDLqif8zihvSov",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "55b6652f-13dd-4a1b-9b20-2545d0997f5a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DPHr5Aw9ig78j785HRCwJc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 28024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 38 · 2026-05-10T08:07:59.619Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q9bW5KVmRrKyBa3vXAGYd3`</summary>

```json
{
  "query": "\"typological distance\" pivot selection instruction tuning arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "55b6652f-13dd-4a1b-9b20-2545d0997f5a",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYcVZXDLqif8zihvSov",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "509cabd7-43ad-48fe-a560-a5a16f8028d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DPHr5Aw9ig78j785HRCwJc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 28024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 39 · 2026-05-10T08:08:00.032Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016zU5oKHPqftjbSyeyn1Phv`</summary>

```json
{
  "query": "staged curriculum close distant language pairs instruction tuning 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "509cabd7-43ad-48fe-a560-a5a16f8028d1",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYcVZXDLqif8zihvSov",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "950e04ff-7981-4e15-a81c-86519f3866fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DPHr5Aw9ig78j785HRCwJc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 28024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 40 · 2026-05-10T08:08:00.240Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QZNgsVkYitiTCXqZvu4oLz`</summary>

```json
{
  "query": "multi-source DPO cross-lingual instruction following 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "950e04ff-7981-4e15-a81c-86519f3866fc",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYcVZXDLqif8zihvSov",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7d0783ba-4acc-49cc-8fb1-24bdcd593580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DPHr5Aw9ig78j785HRCwJc",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 28024,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2019,
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

_source line 41 · 2026-05-10T08:08:00.501Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012TyYz3TFkbVRSW2UVEo1wU`</summary>

```json
{
  "query": "Kazakh instruction tuning DPO 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7d0783ba-4acc-49cc-8fb1-24bdcd593580",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYcVZXDLqif8zihvSov",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a1393358-7fa4-409e-baff-2d77fb72a1bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DPHr5Aw9ig78j785HRCwJc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 2019,
      "cache_read_input_tokens": 28024,
      "output_tokens": 234,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2019
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 234,
          "cache_read_input_tokens": 28024,
          "cache_creation_input_tokens": 2019,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2019,
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

_source line 42 · 2026-05-10T08:08:06.973Z_

<details><summary>↩ Tool result · `toolu_012TyYz3TFkbVRSW2UVEo1wU`</summary>

```text
Web search results for query: "Kazakh instruction tuning DPO 2025 2026"

Links: [{"title":"The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization","url":"https://www.mdpi.com/2504-2289/9/5/137"},{"title":"Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.706/"},{"title":"Direct Preference Optimization: A Technical Deep Dive","url":"https://www.together.ai/blog/direct-preference-optimization"},{"title":"GitHub - allenai/open-instruct: AllenAI's post-training codebase · GitHub","url":"https://github.com/allenai/open-instruct"},{"title":"Evaluating DPO and its Variants Across Multiple Tasks","url":"https://aclanthology.org/2025.acl-srw.26.pdf"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/html/2308.10792v9"},{"title":"Kazakhstan Establishes National Standards for Artificial Intelligence in Education - The Astana Times","url":"https://astanatimes.com/2025/09/kazakhstan-establishes-national-standards-for-artificial-intelligence-in-education/"},{"title":"The Complete Guide to Using AI in the Education Industry in Kazakhstan in 2025","url":"https://www.nucamp.co/blog/coding-bootcamp-kazakhstan-kaz-education-the-complete-guide-to-using-ai-in-the-education-industry-in-kazakhstan-in-2025"},{"title":"Direct Preference Optimization (DPO) - Deep (Learning) Focus","url":"https://cameronrwolfe.substack.com/p/direct-preference-optimization"},{"title":"Data Annotation for LLM Fine-Tuning: RLHF and Instruction Tuning Guide | Second Talent","url":"https://www.secondtalent.com/resources/data-annotation-for-llm-fine-tuning-rlhf-and-instruction-tuning-guide/"}]

Based on the search results, here's what I found about Kazakh instruction tuning and DPO in 2025-2026:

## Research on Kazakh Language Models with DPO

A 1.94B parameter LLaMA-based Kazakh language model demonstrates how strong, culturally aligned performance can be achieved without massive infrastructure. Adapting LLaMA architecture for Kazakh, lowering computational overhead, and applying Direct Preference Optimization (DPO) with contrastive and entropy-based regularization resulted in a stable, high-performing model that surpassed baseline instruction-tuned variants and even larger-scale multilingual systems in key metrics such as accuracy, coherence, and context-awareness.

## Instruction Tuning Datasets for Kazakh

A large-scale (10,600 samples) instruction-following dataset covering key institutional and cultural knowledge relevant to Kazakhstan was introduced, with each entity undergoing full manual verification to ensure high quality. Fine-tuning Qwen, Falcon, and Gemma on this dataset leads to consistent performance improvements in both multiple-choice and generative tasks, demonstrating the potential of LLM-assisted instruction tuning for low-resource languages.

## AI Integration in Kazakh Education (2025-2026)

Starting from the 2025–2026 academic year, elements of artificial intelligence have been integrated into the subjects Digital Literacy and Informatics. This reflects Kazakhstan's broader push to incorporate AI into its education system during this period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a1393358-7fa4-409e-baff-2d77fb72a1bd",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "e2b0e129-37d3-4bb9-a505-dc0848a10888",
  "sourceToolAssistantUUID": "a1393358-7fa4-409e-baff-2d77fb72a1bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T08:08:07.505Z_

<details><summary>↩ Tool result · `toolu_01QZNgsVkYitiTCXqZvu4oLz`</summary>

```text
Web search results for query: "multi-source DPO cross-lingual instruction following 2025 2026"

Links: [{"title":"[2503.04647] Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment","url":"https://arxiv.org/abs/2503.04647"},{"title":"arXiv:2503.04647v2 [cs.CL] 5 Jun 2025 Implicit Cross-Lingual Rewarding","url":"https://nlpr.ia.ac.cn/cip/ZongPublications/2025/2025-YangWen-FindingsACL.pdf"},{"title":"Post-training methods for language models | Red Hat Developer","url":"https://developers.redhat.com/articles/2025/11/04/post-training-methods-language-models"},{"title":"XL-Suite: Cross-Lingual Synthetic Training and Evaluation ...","url":"https://aclanthology.org/2025.findings-emnlp.550.pdf"},{"title":"1 Reasoning Beyond Limits: Advances and Open Problems for LLMs","url":"https://arxiv.org/pdf/2503.22732"},{"title":"Cross-Lingual Vocabulary Transfer for Low-Resource ...","url":"https://aclanthology.org/2025.findings-acl.1333.pdf"},{"title":"CCL-XCoT: An Efficient Cross-Lingual Knowledge Transfer ...","url":"https://aclanthology.org/2025.findings-emnlp.93.pdf"},{"title":"Word-level Cross-lingual Structure in Large Language ...","url":"https://aclanthology.org/2025.coling-main.138.pdf"},{"title":"Accepted Main Conference Papers - EMNLP 2025","url":"https://2025.emnlp.org/program/main_papers/"},{"title":"Aligning LLMs for Multilingual Consistency in Enterprise ...","url":"https://aclanthology.org/2025.emnlp-industry.9.pdf"}]

Based on the search results, I found several relevant papers and research on this topic from 2025-2026. Here are the key findings:

## Key Research on Multi-Source DPO for Cross-Lingual Instruction Following

**Implicit Cross-Lingual Rewarding for Multilingual Preference Alignment**

A novel approach captures learned preferences from well-aligned English models by deriving an implicit reward model from English DPO-aligned logits, which is then leveraged to annotate preference relations in cross-lingual instruction-following pairs using English instructions to evaluate multilingual responses, with the annotated data subsequently used for multilingual DPO fine-tuning.

Fine-tuning Llama3 resulted in a 12.72% average improvement in Win Rate and a 5.97% increase in Length Control Win Rate across all training languages on the X-AlpacaEval leaderboard.

**Related Cross-Lingual Work**

The search also revealed other cross-lingual instruction-following research:

- CROSSIN presents an efficient instruction tuning approach for cross-lingual knowledge alignment.

- The XL-Instruct pipeline involves instruction generation from seed English data, data refinement, response translation into non-English, and data filtering.

- Direct Preference Optimization (DPO) is used as an implicit reward model for aligning LLMs with human preferences.

These papers represent recent advances (2025-2026) in using DPO techniques for improving multilingual and cross-lingual instruction-following capabilities in large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7d0783ba-4acc-49cc-8fb1-24bdcd593580",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "76a4f03a-7c6c-45c8-881e-3d9e1c6d00d6",
  "sourceToolAssistantUUID": "7d0783ba-4acc-49cc-8fb1-24bdcd593580",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-10T08:08:07.521Z_

<details><summary>↩ Tool result · `toolu_01Q9bW5KVmRrKyBa3vXAGYd3`</summary>

```text
Web search results for query: ""typological distance" pivot selection instruction tuning arxiv"

Links: [{"title":"Diversity Measurement and Subset Selection for Instruction Tuning Datasets","url":"https://arxiv.org/pdf/2402.02318"},{"title":"[2402.02318] Diversity Measurement and Subset Selection for Instruction Tuning Datasets","url":"https://arxiv.org/abs/2402.02318"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"[2604.10448] Instruction Data Selection via Answer Divergence","url":"https://arxiv.org/abs/2604.10448"},{"title":"Large-Scale Data Selection for Instruction Tuning","url":"https://arxiv.org/html/2503.01807"},{"title":"Instruction Mining: Instruction Data Selection for Tuning Large Language Models","url":"https://arxiv.org/html/2307.06290v3"},{"title":"ROSE: A Reward-Oriented Data Selection Framework for LLM Task-Specific Instruction Tuning","url":"https://arxiv.org/html/2412.00631"},{"title":"[2602.18584] GIST: Targeted Data Selection for Instruction Tuning via Coupled Optimization Geometry","url":"https://arxiv.org/abs/2602.18584"},{"title":"The Geometry of the Pivot:","url":"https://www.arxiv.org/pdf/2601.03706v2"},{"title":"arXiv:2602.09039v1 [cs.DB] 30 Jan 2026","url":"https://www.arxiv.org/pdf/2602.09039"}]

I found several relevant papers on instruction tuning and data selection. Here are the key results:

## Instruction Tuning and Data Selection

The goal is to select data subsets for the fine-tuning of large language models to more effectively follow instructions. Several arxiv papers address this challenge:

1. **Diversity Measurement and Subset Selection** (arXiv 2402.02318): This paper studies the log determinant distance as a measure of diversity of instruction tuning and preference learning datasets, finding that more diverse datasets yield a log determinant distance curve that is closer to a horizontal line and closer to zero.

2. **PLUG: Leveraging Pivot Language** (arXiv 2311.08711): This approach utilizes a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages, training the model to first process instructions in the pivot language, and then produce responses in the target language.

3. **Answer Divergence-Guided Selection** (arXiv 2604.10448): ADG selects instruction data based on the geometric structure of multi-sample outputs, drawing several high-temperature generations per instruction, mapping responses into an embedding space, and computing an output divergence score that jointly encodes dispersion magnitude and shape anisotropy.

4. **GIST: Targeted Data Selection** (arXiv 2602.18584): Targeted data selection has emerged as a crucial paradigm for efficient instruction tuning, aiming to identify a small yet influential subset of training examples for a specific target task.

The search results also mention TyDi QA, a benchmark for information-seeking question answering in typologically diverse languages, which relates to typological considerations in language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "509cabd7-43ad-48fe-a560-a5a16f8028d1",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "1ecb007c-7858-4017-9455-2798bebbf001",
  "sourceToolAssistantUUID": "509cabd7-43ad-48fe-a560-a5a16f8028d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-10T08:08:07.763Z_

<details><summary>↩ Tool result · `toolu_016zU5oKHPqftjbSyeyn1Phv`</summary>

```text
Web search results for query: "staged curriculum close distant language pairs instruction tuning 2025"

Links: [{"title":"Curriculum Instruction Tuning in LLMs","url":"https://www.emergentmind.com/topics/curriculum-instruction-tuning"},{"title":"A Powerful Pipeline for LLM Instruction Tuning","url":"https://arxiv.org/pdf/2408.14774"},{"title":"Training Large Language Models with Curriculum Learning (2020-2025)","url":"https://aiwithmike.substack.com/p/training-large-language-models-with"},{"title":"Task-Structured Curriculum Learning for Multi-Task Distillation","url":"https://www.techscience.com/cmc/online/detail/25298/pdf"},{"title":"Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models","url":"https://arxiv.org/html/2503.23714v1"},{"title":"Advancing Language Models through Instruction Tuning: Recent Progress and Challenges","url":"https://instruction-tuning-tutorial-2025.github.io/"},{"title":"[PDF] CITING: Large Language Models Create Curriculum for Instruction Tuning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CITING:-Large-Language-Models-Create-Curriculum-for-Feng-Wang/c31396f00c4e4ddba20d085d0da819b89c71bf4a"},{"title":"Instruction-Tuning Open-Weight Language Models for BPMN Model Generation","url":"https://arxiv.org/html/2512.12063v1"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/html/2308.10792v9"},{"title":"A Survey of Instruction Tuning in Large Language Models","url":"https://www.arxiv.org/pdf/2508.17184"}]

Based on the search results, I found relevant information about staged curriculum approaches in instruction tuning for language models in 2025. Here are the key findings:

## Staged Curriculum Instruction Tuning

Curriculum Instruction Tuning (CIT) is the systematic ordering and optimization of training data and schedule for LLMs and related architectures, guided by difficulty metrics, learning outcomes, and pedagogical principles.

### Multi-Stage Training Approaches

Recent 2025 research demonstrates several staged curriculum strategies:

A task-based curriculum learning framework divides training into three consecutive stages: an initial phase focused solely on prediction, a second phase that jointly trains prediction and explanation, and a final phase dedicated to refining explanation generation. This approach consistently outperforms strong baselines, achieving gains of +1.7–2.6 points in accuracy and 0.8–1.2 in ROUGE-L.

### Data Organization Methods

Data is organized through lexicographic ordering, sorted first by stage/complexity and second by cognitive level, or through difficulty assignment where instruction-response pairs are assigned scalar or categorical difficulty via model loss, length, diversity, logic depth, or specially learned adversarial models.

### Curriculum Scope and Challenges

Early heuristic scheduling fails to accommodate evolving model competence or cross-domain disparity, and mapping difficulty from human heuristics may not precisely match LLM perception.

The research indicates that staged curriculum approaches are increasingly important for improving instruction tuning effectiveness, particularly for handling tasks of varying complexity.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "950e04ff-7981-4e15-a81c-86519f3866fc",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "54d2b4ae-378c-47f0-9f92-63601151c310",
  "sourceToolAssistantUUID": "950e04ff-7981-4e15-a81c-86519f3866fc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 46 · 2026-05-10T08:08:09.438Z_

Excellent findings! Let me do one more targeted search to check for any papers that combine all three key elements (typological distance + staged curriculum + multi-source training).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54d2b4ae-378c-47f0-9f92-63601151c310",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYdCnk9tp27RXfy8rij",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0f5ad65b-c8ce-4260-8429-826bfdf9a9f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01788PmX1grx1CJCxwxNCbzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 30043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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

_source line 47 · 2026-05-10T08:08:09.661Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UZqXKsfEpZEhASx871iq6A`</summary>

```json
{
  "query": "lang2vec typological features language selection instruction tuning pivot"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f5ad65b-c8ce-4260-8429-826bfdf9a9f3",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYdCnk9tp27RXfy8rij",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "de4f8353-254f-41f8-abf4-18c281bc8e3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01788PmX1grx1CJCxwxNCbzC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 30043,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2053,
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

_source line 48 · 2026-05-10T08:08:09.909Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XGP9aiEEu4EUZ82Enmg428`</summary>

```json
{
  "query": "cross-lingual transfer low-resource Asian languages Kazakh Mongolian Uyghur 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de4f8353-254f-41f8-abf4-18c281bc8e3b",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYdCnk9tp27RXfy8rij",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3ace8ff3-aee4-4e6a-a2ed-0fcd82db9cae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01788PmX1grx1CJCxwxNCbzC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1815,
      "cache_creation_input_tokens": 2053,
      "cache_read_input_tokens": 30043,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2053
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1815,
          "output_tokens": 157,
          "cache_read_input_tokens": 30043,
          "cache_creation_input_tokens": 2053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2053,
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

_source line 49 · 2026-05-10T08:08:17.129Z_

<details><summary>↩ Tool result · `toolu_01UZqXKsfEpZEhASx871iq6A`</summary>

```text
Web search results for query: "lang2vec typological features language selection instruction tuning pivot"

Links: [{"title":"data2lang2vec: Data Driven Typological Features Completion","url":"https://arxiv.org/html/2409.17373v1"},{"title":"GitHub - antonisa/lang2vec: A simple library for querying the URIEL typological database. · GitHub","url":"https://github.com/antonisa/lang2vec"},{"title":"URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors - ACL Anthology","url":"https://aclanthology.org/E17-2002/"},{"title":"lang2vec/README.md at master · antonisa/lang2vec","url":"https://github.com/antonisa/lang2vec/blob/master/README.md"},{"title":"[2409.17373] data2lang2vec: Data Driven Typological Features Completion","url":"https://arxiv.org/abs/2409.17373"},{"title":"[PDF] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/URIEL-and-lang2vec:-Representing-languages-as-and-Levin-Littell/e3a824e59ac66ceaaa420e0de4f2b5d809231f6e"},{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"piwheels - lang2vec","url":"https://www.piwheels.org/project/lang2vec/"},{"title":"LANG2VEC attention scores for each of the test languages (clustered... | Download Scientific Diagram","url":"https://www.researchgate.net/figure/LANG2VEC-attention-scores-for-each-of-the-test-languages-clustered-group-wise_fig1_376393533"},{"title":"(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors","url":"https://www.academia.edu/82585837/URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors?uc-sb-sw=100511255"}]

Based on the search results, here's what I found regarding lang2vec, typological features, language selection, instruction tuning, and pivot languages:

## Lang2vec and Typological Features

Lang2vec is a utility that provides information-rich vector identifications of languages drawn from typological, geographical, and phylogenetic databases and normalized to have straightforward and consistent formats, naming, and semantics. Lang2vec includes a collection of previously existing databases, namely: WALS, PHOIBLE, Ethnologue, and Glottolog, which are all converted to a uniform format, where each feature is represented as a binary feature.

## Language Selection for Instruction Tuning

Research hypothesizes that optimum language subset selection for multilingual instruction tuning can be achieved in a linguistically informed manner by investigating various language selection techniques and comparing them to baselines such as randomly selected subsets, subsets curated by picking a single language from each language family, and all languages available in the dataset.

Linguistically informed selection techniques range from common methods, such as typological feature vectors, to less conventional but promising approaches, including language embeddings derived from semantic typology features, with a simple k-means clustering algorithm applied to select a fixed number of languages based on each technique.

## Pivot Features in Cross-lingual Transfer

Cross-lingual model transfer is a commonly used technique for parsing low-resource languages, which relies on the existence of pivot features, such as universal part-of-speech tags or crosslingual word embeddings, and requires identifying one or more suitable source languages, a task for which language similarity metrics have been exploited.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "de4f8353-254f-41f8-abf4-18c281bc8e3b",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "48e297bd-e7d8-4d15-949c-4f1394ebbb44",
  "sourceToolAssistantUUID": "de4f8353-254f-41f8-abf4-18c281bc8e3b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T08:08:19.597Z_

<details><summary>↩ Tool result · `toolu_01XGP9aiEEu4EUZ82Enmg428`</summary>

```text
Web search results for query: "cross-lingual transfer low-resource Asian languages Kazakh Mongolian Uyghur 2025"

Links: [{"title":"Shared Weights Pretraining for Extremely Low-Resource ...","url":"https://aclanthology.org/2025.acl-long.893.pdf"},{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...","url":"https://aclanthology.org/2025.findings-acl.578.pdf"},{"title":"Cross-Lingual Vocabulary Transfer for Low-Resource ...","url":"https://aclanthology.org/2025.findings-acl.1333.pdf"},{"title":"Left Behind: Cross-Lingual Transfer as a Bridge for Low-Resource Languages in Large Language Models","url":"https://arxiv.org/html/2603.21036"},{"title":"Large and Small models for collaborative cross-lingual data augmentation in entity relationship extraction for low-resource languages | Journal of King Saud University Computer and Information Sciences | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s44443-025-00055-w"},{"title":"Low-Resource Language Expansion and Translation Capacity Enhancement for LLM: A Study on the Uyghur - ACL Anthology","url":"https://aclanthology.org/2025.coling-main.559/"},{"title":"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon","url":"https://arxiv.org/html/2506.01675"},{"title":"Transliteration-Aided Transfer Learning for Low-Resource ASR: A Case Study on Khalkha Mongolian | MDPI","url":"https://www.mdpi.com/2079-9292/14/6/1137"},{"title":"Neural Machine Translation for Low-Resource Languages from a Chinese-centric Perspective: A Survey | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3665244"},{"title":"Multilingual end-to-end ASR for low-resource Turkic languages with common alphabets | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-64848-1"}]

The search has returned several highly relevant results on cross-lingual transfer learning for low-resource Asian languages, particularly Kazakh, Mongolian, and Uyghur. Here are the key findings:

## Recent Research on Cross-Lingual Transfer for Kazakh, Mongolian, and Uyghur (2025)

### Multilingual Model Benchmarking

Recent research investigates how large language models perform on low-resource languages by benchmarking eight LLMs across five experimental conditions in English, Kazakh, and Mongolian. The research finds a consistent performance gap of 13.8–16.7 percentage points between English and low-resource language conditions, with models maintaining surface-level fluency while producing significantly less accurate content.

### Cross-Lingual Transfer Strategies

Cross-lingual transfer—prompting models to reason in English before translating back—yields selective gains for bilingual architectures (+2.2pp to +4.3pp) but provides no benefit to English-dominant models.

### Shared Weights Pretraining

A shared weight framework for efficiently adapting multilingual encoders includes Uyghur, Kazakh, and Mongolian. This work examines cross-lingual transfer performance of different models on text summarization and machine translation tasks.

### Language-Specific Challenges

The challenge of low-resource languages is particularly evident in agglutinative languages such as Mongolian, Kazakh, Uyghur, and Hungarian, which typically use suffixes or prefixes to convey grammatical functions, such as tense, case, and voice, resulting in highly complex morphological variations.

### Expanding Low-Resource Language Capabilities

Research has shown that a multi-stage strategy effectively expands the low-resource languages supported by large language models and significantly enhances the model's translation ability in Uyghur with less parallel data.

### Asymmetric Knowledge Transfer

For lower-resource languages (Tibetan and Mongolian), an asymmetric transfer pattern is found: knowledge transfer from low-resource languages to English is more pronounced than the reverse direction.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ace8ff3-aee4-4e6a-a2ed-0fcd82db9cae",
  "isSidechain": true,
  "promptId": "3637abe5-7560-4671-bae0-ab31c0ef4383",
  "agentId": "af17d75195abb567d",
  "type": "user",
  "uuid": "530ddc4e-27c2-4d6c-ade7-3eec3561b415",
  "sourceToolAssistantUUID": "3ace8ff3-aee4-4e6a-a2ed-0fcd82db9cae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-10T08:08:47.091Z_

Perfect. I now have comprehensive information. Let me compile my findings report.

## Competitive and Related Work Analysis Report

Based on my systematic search of recent literature (2025-2026), I have identified **significant competing work** that potentially overlaps with your paper's core contributions. Here are the key findings:

### **CRITICAL COMPETITOR: PROM (NAACL 2025 Short Paper)**

**Title:** "PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning"
**Venue:** NAACL 2025 (official proceedings)
**ACL Anthology URL:** https://aclanthology.org/2025.naacl-short.19/

**Methodological Overlap with Your Work:**
- Uses **pivot language approach** (English as internal pivot for underrepresented languages)
- **Disentangles roles of English and target language data** through two pivoted objectives
- **Regulates between pivots** for better generalization to under-represented languages

**Key Distinction:** PROM identifies English as an internal pivot and proposes two pivoted objectives with regulation between them, but the search results don't explicitly confirm use of typological-distance weighting or staged curriculum from close→distant pivots.

---

### **HIGHLY RELEVANT: PLUG (ACL 2024 Long Paper)**

**Title:** "PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning"
**Venue:** ACL 2024
**ACL Anthology URL:** https://aclanthology.org/2024.acl-long.379/
**GitHub:** https://github.com/ytyz1307zzh/PLUG

**Methodological Overlap:**
- Single pivot (English) for cross-lingual instruction tuning
- Two-stage approach: process instructions in pivot language, then generate in target
- Achieves 29% average improvement vs. direct target-language approaches
- Tested on Chinese, Korean, Italian, Spanish with X-AlpacaEval benchmark

**Key Distinction:** PLUG uses only English as pivot, not multiple typologically-weighted pivots. No evidence of typological distance weighting or staged curriculum from close to distant pivots.

---

### **RECENT COMPETITOR: Implicit Cross-Lingual Rewarding (Findings ACL 2025)**

**Title:** "Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment"
**ArXiv:** https://arxiv.org/abs/2503.04647
**Key Contribution:** Uses **DPO (Direct Preference Optimization) for cross-lingual instruction following**

**Methodological Overlap with Your Multi-Source DPO Claim:**
- Derives implicit reward model from English DPO-aligned model logits
- Uses English instructions to evaluate multilingual responses
- Performs multilingual DPO fine-tuning with cross-lingual preference pairs
- 12.72% Win Rate improvement on X-AlpacaEval across multiple languages

**Key Distinction:** Single-source (English) DPO approach, not multi-source. Does not incorporate typological-distance weighting.

---

### **RELEVANT: Linguistically-Informed Multilingual Instruction Tuning (arXiv 2410.07809)**

**Title:** "Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?"
**Venue:** ACL 2025
**Key Contribution:** **Uses typological features for language selection**

**Methodological Overlap:**
- Employs **typological feature vectors** from URIEL/lang2vec
- Tests multiple typological features: TYPO (289-dim URIEL features), LEARN (NMT embeddings), GEO (geographic), SEM (semantic), FAM (family), RND (random)
- K-means clustering for diverse language selection
- No explicit use of distance weighting or curriculum learning

**Key Distinction:** Uses typological features for **diversity sampling** via clustering, not for **distance-weighted pivot selection** or **staged curriculum from close→distant pivots**.

---

### **RELATED: XCOT (AAAI 2025)**

**Title:** "XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning"
**Venue:** AAAI 2025
**ArXiv:** https://arxiv.org/abs/2401.07037

**Methodological Components:**
- Cross-lingual in-context few-shot learning (xICL)
- Randomly online CoT strategy (translates query to alternate language before responding)
- Cross-lingual distillation from high-resource to low-resource languages

**Overlap Assessment:** Addresses cross-lingual transfer for low-resource languages but **no typological distance weighting, no multi-pivot selection, no staged curriculum from close→distant pivots**.

---

### **RELATED: CrossIn (ACL 2025 Workshop)**

**Title:** "CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment"
**Venue:** 2nd Workshop on Scaling Up Multilingual & Multi-Cultural Evaluation (ACL 2025)
**ArXiv:** https://arxiv.org/abs/2404.11932

**Methodological Components:**
- Mixed composition of cross-lingual instruction tuning data
- Complex Task Dataset (CTD) + Linguistic Uniformity Dataset (LUD)
- Merges cross-lingual data from CTD with machine-translated data from LUD

**Overlap Assessment:** Addresses cross-lingual instruction tuning but **no explicit typological distance, pivot selection, or curriculum from close→distant languages**.

---

### **RELATED: Budget-Xfer (ArXiv 2603.27651)**

**Title:** "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages"
**ArXiv:** https://arxiv.org/abs/2603.27651
**Submission Date:** March 29, 2026

**Methodological Components:**
- Formulates multi-source cross-lingual transfer as **budget-constrained resource allocation**
- Jointly optimizes which source languages to include and data allocation amounts
- Four allocation strategies tested on African languages (Hausa, Yoruba, Swahili)

**Overlap Assessment:** Addresses **multi-source language selection** but for African languages, not Kazakh/Mongolian/Uyghur. No explicit typological-distance weighting or staged curriculum.

---

### **RELEVANT: Kazakh Instruction Tuning Research (ACL 2025 Long)**

**Title:** "Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: a Case Study in Kazakh"
**Venue:** ACL 2025 Long Papers
**ACL Anthology:** https://aclanthology.org/2025.acl-long.706/

**Content:** 10,600-sample Kazakh instruction-following dataset with manual verification, fine-tuning on Qwen/Falcon/Gemma.

**Overlap Assessment:** Target language (Kazakh) but **no cross-lingual transfer, multi-pivot, typological distance, or curriculum learning**.

---

### **PARALLEL WORK: Small-Scale Kazakh Models with DPO (MDPI 2025)**

**Title:** "The Development of Small-Scale Language Models for Low-Resource Languages, with a Focus on Kazakh and Direct Preference Optimization"
**Venue:** MDPI 2025

**Content:** 1.94B LLaMA-based Kazakh model using DPO with contrastive and entropy regularization.

**Overlap Assessment:** Focuses on single-language DPO, not multi-pivot or typological-distance weighting.

---

### **BROADER CONTEXT: Mongolian and Uyghur (2025)**

**MiLiC-Eval (ACL 2025 Findings):** Benchmarks 8 LLMs on Kazakh, Mongolian, and English, finding 13.8–16.7pp performance gaps for low-resource languages.

**Low-Resource Language Expansion for Uyghur (COLING 2025):** Uses DPOSE (direct preference optimization with self-evolution) for Uyghur expansion, but focuses on translation rather than instruction tuning.

---

## **NOVELTY ASSESSMENT**

### **Your Core Claims vs. Literature:**

| Contribution | Status | Competing Work |
|---|---|---|
| **Typological-distance weighting for pivot selection** | **NOT FOUND in this exact combination** | "Linguistically-Informed" uses typological features but via k-means clustering, not distance-weighted pivot selection |
| **Staged curriculum: close→distant pivots** | **NOT FOUND in this exact form** | Curriculum learning research exists (Code-Switching CL, etc.), but not explicitly staged close→distant for multi-pivot selection |
| **Multi-source DPO for cross-lingual instruction** | **PARTIALLY OVERLAPPED** | "Implicit Cross-Lingual Rewarding" uses DPO for multilingual instruction but from single English source, not true multi-source |
| **Applied to Kazakh, Mongolian, Uyghur** | **PARTIALLY OVERLAPPED** | Individual languages studied separately (Kazakh in ACL 2025, Uyghur in COLING 2025, Mongolian in MiLiC-Eval), but not as unified typological-distance-weighted multi-pivot system |

---

## **CONCLUSION**

**Your paper's novelty appears defensible**, but with important caveats:

1. **PROM (NAACL 2025)** is the most direct competitor in terms of pivoted multilingual instruction learning, though its approach (regulatory objectives between English and target) differs from typological-distance weighting.

2. **Linguistically-Informed Multilingual IT** validates that typological features can guide language selection, but uses k-means clustering rather than distance weighting for pivot selection or curriculum design.

3. **No single prior work** combines all three of your key claims: (a) typological-distance weighting, (b) staged curriculum from close→distant pivots, and (c) multi-source DPO.

4. The **target language set (Kazakh, Mongolian, Uyghur)** has seen recent attention individually, but not as a unified system with typological-distance-weighted multi-pivot instruction tuning.

**Risk Level:** Moderate. PROM's 2025 NAACL publication and the convergence of related work on DPO + multilingual instruction tuning should be carefully discussed in your related work section to clearly differentiate your typological-distance and curriculum contributions.

---

## Sources

- [PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning](https://aclanthology.org/2025.naacl-short.19/)
- [PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning](https://aclanthology.org/2024.acl-long.379/)
- [Implicit Cross-Lingual Rewarding for Efficient Multilingual Preference Alignment](https://arxiv.org/abs/2503.04647)
- [Linguistically-Informed Multilingual Instruction Tuning](https://arxiv.org/html/2410.07809)
- [XCOT: Cross-lingual Instruction Tuning for Cross-lingual Chain-of-Thought Reasoning](https://arxiv.org/abs/2401.07037)
- [CrossIn: An Efficient Instruction Tuning Approach for Cross-Lingual Knowledge Alignment](https://arxiv.org/abs/2404.11932)
- [Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer](https://arxiv.org/abs/2603.27651)
- [Instruction Tuning on Public Government and Cultural Data for Low-Resource Language: Kazakh](https://aclanthology.org/2025.acl-long.706/)
- [The Development of Small-Scale Language Models for Kazakh and DPO](https://www.mdpi.com/2504-2289/9/5/137)
- [MiLiC-Eval: Benchmarking Multilingual LLMs for China's Minority Languages](https://aclanthology.org/2025.findings-acl.578.pdf)
- [Low-Resource Language Expansion for Uyghur](https://aclanthology.org/2025.coling-main.559/)
- [URIEL and lang2vec: Typological Vectors](https://aclanthology.org/E17-2002/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530ddc4e-27c2-4d6c-ade7-3eec3561b415",
  "isSidechain": true,
  "agentId": "af17d75195abb567d",
  "requestId": "req_011CatYe5PHKgEXTNZ5Ftxpw",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "71c0ba58-a8f7-48d0-b14b-ab504b4ab16d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "5ac41372-3de1-44fd-887d-d5fb9f425ba6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01FhN7n25jdukB6ieE4GPtPJ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4018,
      "cache_read_input_tokens": 32096,
      "output_tokens": 3025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4018
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3025,
          "cache_read_input_tokens": 32096,
          "cache_creation_input_tokens": 4018,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4018,
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
