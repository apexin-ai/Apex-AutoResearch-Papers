# Research conversation: I'm reviewing an NLP research paper idea called TWMP (Typologically-Weighted Multi-Pivot). I need to independently verif

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 61
- **Recorded user turns:** 1
- **Tool calls:** 26
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-af9cb2e5e5a668192.jsonl`
- **Structured JSON:** [`ecdbf2cd64598da2fbbe.json`](../../sessions/ec/ecdbf2cd64598da2fbbe.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

61 recorded events

### User

_source line 1 · 2026-05-10T07:56:22.365Z_

I'm reviewing an NLP research paper idea called TWMP (Typologically-Weighted Multi-Pivot). I need to independently verify several cited papers exist and find any competing work. Use WebSearch and WebFetch.

1. Verify LangGPS exists: "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning" arXiv:2511.10229 AAAI 2026. Search for it, check abstract.

2. Verify Budget-Xfer exists: arXiv:2603.27651 SIGIR 2026 on budget-constrained source language selection for cross-lingual transfer to African languages. Search for "Budget-Xfer cross-lingual African languages SIGIR 2026" or the arXiv ID.

3. Search for competing papers that combine typological language features (URIEL/URIEL+) with data weighting for cross-lingual NLP:
   - site:arxiv.org "URIEL" "instruction tuning" 2025 2026
   - "typological features" "data selection" multilingual 2026
   - "lang2vec" OR "URIEL" "cross-lingual transfer" "curriculum" 2025 OR 2026

4. Search Papers With Code for SOTA on Kazakh/Mongolian MMLU-style benchmarks:
   - site:paperswithcode.com KazMMLU
   - site:paperswithcode.com MiLiC-Eval
   - "Kazakh language model benchmark 2026"

5. Search for any papers on typological similarity-based adapter aggregation or LoRA merging for multilingual NLP in 2025-2026:
   - "typological similarity LoRA" multilingual 2025 2026
   - "TIPA typological adapter" multilingual 2026

Report all findings including whether the cited papers exist as described, and importantly whether any NEW papers have appeared that would compete with TWMP's novelty claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "d3e08555-acc3-43ed-bf75-dfae3389d431",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T07:56:23.465Z_

I'll conduct a comprehensive search to verify the cited papers and identify competing work. Let me start with multiple searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d3e08555-acc3-43ed-bf75-dfae3389d431",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dd58b857-fe28-4949-a30b-146c693a8a98",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-10T07:56:23.720Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F6hhtTNSW1F2DaoHzVgMah`</summary>

```json
{
  "query": "LangGPS Language Separability Guided Data Pre-Selection Joint Multilingual Instruction Tuning arXiv:2511.10229"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dd58b857-fe28-4949-a30b-146c693a8a98",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "3eeeca33-b00b-47d8-900d-ab1efc909537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 4 · 2026-05-10T07:56:23.923Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0121yU8tuCyTqTQW8XDF5WMf`</summary>

```json
{
  "query": "Budget-Xfer cross-lingual African languages SIGIR 2026 arXiv:2603.27651"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eeeca33-b00b-47d8-900d-ab1efc909537",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aed606b4-63be-472e-b19a-a2b1171da4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-10T07:56:24.133Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012hjgL3UzQjqBB6vnGRarQT`</summary>

```json
{
  "query": "site:arxiv.org URIEL instruction tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aed606b4-63be-472e-b19a-a2b1171da4aa",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "fdf62317-5298-4bab-a96e-fda16284cbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 896,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-10T07:56:24.337Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XZ1ND9J4y5n29W4uLiQJ7F`</summary>

```json
{
  "query": "typological features data selection multilingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fdf62317-5298-4bab-a96e-fda16284cbad",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c2b8056c-c70f-45eb-ae6e-314f4b80f7bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 896,
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

_source line 7 · 2026-05-10T07:56:24.398Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01X8SNg8ygK2scZFfHdK3WK8`</summary>

```json
{
  "query": "lang2vec URIEL cross-lingual transfer curriculum 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c2b8056c-c70f-45eb-ae6e-314f4b80f7bd",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjCuVCHSH21xPVS4wX",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "597461cc-8f2f-44e3-95ab-c1081f96d215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QopboAtKKcqJaVMZssZCPN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 896,
      "cache_read_input_tokens": 13791,
      "output_tokens": 318,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 896
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 318,
          "cache_read_input_tokens": 13791,
          "cache_creation_input_tokens": 896,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 896,
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

_source line 8 · 2026-05-10T07:56:29.641Z_

<details><summary>↩ Tool result · `toolu_012hjgL3UzQjqBB6vnGRarQT`</summary>

```text
Web search results for query: "site:arxiv.org URIEL instruction tuning 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 DATAPROPHET:","url":"https://arxiv.org/pdf/2603.19688"},{"title":"Instruction-based Time Series Editing","url":"https://arxiv.org/html/2508.01504v2"},{"title":"Instruction-Tuning Open-Weight Language Models for BPMN Model Generation","url":"https://arxiv.org/html/2512.12063v1"},{"title":"Semi-supervised Instruction Tuning for Large Language Models","url":"https://www.arxiv.org/pdf/2601.12807"},{"title":"Building Instruction-Tuning Datasets from Human-Written Instructions with Open-Weight Large Language Models","url":"https://arxiv.org/html/2503.23714v1"},{"title":"GraphIF: Enhancing Multi-Turn Instruction Following for Large Language Models with Relation Graph Prompt","url":"https://arxiv.org/html/2511.10051v2"},{"title":"[2308.10792] Instruction Tuning for Large Language Models: A Survey","url":"https://arxiv.org/abs/2308.10792"},{"title":"The Future of Continual Learning in the Era of Foundation Models: Three Key Directions","url":"https://arxiv.org/html/2506.03320v1"},{"title":"Computer Science Feb 2025","url":"https://arxiv.org/list/cs/2025-02?skip=1225&show=2000"},{"title":"[2203.02155] Training language models to follow instructions with human feedback","url":"https://arxiv.org/abs/2203.02155"}]

The search results don't contain specific information about "URIEL instruction tuning" research. While the search returned several papers about instruction tuning from 2025-2026, none of them mention URIEL specifically.

The results include papers on:
- Data selection for instruction tuning (DataProphet)
- Instruction-based time series editing
- Instruction tuning for BPMN model generation
- Semi-supervised instruction tuning for LLMs
- Building instruction-tuning datasets from human-written instructions
- Multi-turn instruction following with graph prompts
- A comprehensive survey on instruction tuning

However, none of these papers appear to be specifically about "URIEL instruction tuning." It's possible that:
1. URIEL instruction tuning is a very recent or specialized research topic not yet widely indexed
2. The exact term "URIEL instruction tuning" may not be the standard way this research is referred to on arXiv
3. It may be a proprietary or internal project name not published on arXiv

If you're looking for a specific URIEL-related paper, you might want to try searching with different keywords or check if URIEL is an acronym that stands for something specific that might help refine the search.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fdf62317-5298-4bab-a96e-fda16284cbad",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "2f0658be-b914-4647-9a48-b29a3900456f",
  "sourceToolAssistantUUID": "fdf62317-5298-4bab-a96e-fda16284cbad",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-10T07:56:30.215Z_

<details><summary>↩ Tool result · `toolu_0121yU8tuCyTqTQW8XDF5WMf`</summary>

```text
Web search results for query: "Budget-Xfer cross-lingual African languages SIGIR 2026 arXiv:2603.27651"

Links: [{"title":"[2603.27651] Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/abs/2603.27651"},{"title":"Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages","url":"https://arxiv.org/html/2603.27651"},{"title":"Multi-Source Cross-Lingual Model Transfer: Learning What to Share | Request PDF","url":"https://www.researchgate.net/publication/335780754_Multi-Source_Cross-Lingual_Model_Transfer_Learning_What_to_Share"},{"title":"[2409.10965] Cross-lingual transfer of multilingual models on low resource African Languages","url":"https://arxiv.org/abs/2409.10965"},{"title":"Cross-lingual transfer of multilingual models on low resource African Languages","url":"https://arxiv.org/html/2409.10965v1"},{"title":"[2305.06897] AfriQA: Cross-lingual Open-Retrieval Question Answering for African Languages","url":"https://arxiv.org/abs/2305.06897"},{"title":"AfroXLMR-Comet: Multilingual Knowledge Distillation with Attention Matching for Low-Resource languages","url":"https://arxiv.org/html/2502.18020v1"},{"title":"(PDF) \\`It\\`ak\\'ur\\`oso: Exploiting Cross-Lingual Transferability for Natural Language Generation of Dialogues in Low-Resource, African Languages","url":"https://www.researchgate.net/publication/360030642_Itak'uroso_Exploiting_Cross-Lingual_Transferability_for_Natural_Language_Generation_of_Dialogues_in_Low-Resource_African_Languages"},{"title":"[2603.19273] LSR: Linguistic Safety Robustness Benchmark for Low-Resource West African Languages","url":"https://arxiv.org/abs/2603.19273"},{"title":"[2204.08083] AfriWOZ: Corpus for Exploiting Cross-Lingual Transferability for Generation of Dialogues in Low-Resource, African Languages","url":"https://arxiv.org/abs/2204.08083"}]

I found the paper! Here's what I discovered about Budget-Xfer:

## Overview

Budget-Xfer is a framework that formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem, which jointly optimizes which source languages to include and how much data to allocate from each.

## Key Details

**Authors and Affiliation:** The paper was authored by Tewodros Kederalah Idris from Carnegie Mellon University AfricaRwanda, Roald Eiselen from North-West University South Africa, and Prasenjit Mitra from Carnegie Mellon University AfricaRwanda.

**Submission Date:** The paper was submitted on March 29, 2026.

**Research Focus:** The authors evaluated four allocation strategies across named entity recognition and sentiment analysis for three African target languages (Hausa, Yoruba, Swahili) using two multilingual models, conducting 288 experiments.

**Key Finding:** The results show that multi-source transfer significantly outperforms single-source transfer (Cohen's d = 0.80 to 1.98), driven by a structural budget underutilization bottleneck.

The paper addresses the important problem of how to optimally select and allocate training data from multiple source languages when working with low-resource African languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aed606b4-63be-472e-b19a-a2b1171da4aa",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "ff3b2bef-226d-4d1f-95d5-ac188923cd4c",
  "sourceToolAssistantUUID": "aed606b4-63be-472e-b19a-a2b1171da4aa",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T07:56:30.661Z_

<details><summary>↩ Tool result · `toolu_01F6hhtTNSW1F2DaoHzVgMah`</summary>

```text
Web search results for query: "LangGPS Language Separability Guided Data Pre-Selection Joint Multilingual Instruction Tuning arXiv:2511.10229"

Links: [{"title":"[2511.10229] LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/abs/2511.10229"},{"title":"LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning","url":"https://arxiv.org/html/2511.10229"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v1"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Multilingual Pretraining and Instruction Tuning Improve Cross-Lingual Knowledge Alignment, But Only Shallowly","url":"https://arxiv.org/html/2404.04659v1"},{"title":"[2401.01854] Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/abs/2401.01854"},{"title":"Exploring Polyglot Harmony: On Multilingual Data Allocation for Large Language Models Pretraining","url":"https://arxiv.org/html/2509.15556v1"}]

Based on the search results, here's information about the arXiv paper:

LangGPS is a lightweight two-stage pre-selection framework guided by language separability which quantifies how well samples in different languages can be distinguished in the model's representation space.

Joint multilingual instruction tuning is a widely adopted approach to improve the multilingual instruction-following ability and downstream performance of large language models (LLMs), but the resulting multilingual capability remains highly sensitive to the composition and selection of the training data. Existing selection methods, often based on features like text quality, diversity, or task relevance, typically overlook the intrinsic linguistic structure of multilingual data.

**How it works:**
LangGPS first filters training data based on separability scores and then refines the subset using existing selection methods.

**Results:**
Extensive experiments across six benchmarks and 22 languages demonstrate that applying LangGPS on top of existing selection methods improves their effectiveness and generalizability in multilingual training, especially for understanding tasks and low-resource languages.

**Key findings:**
Highly separable samples facilitate the formation of clearer language boundaries and support faster adaptation, while low-separability samples tend to function as bridges for cross-lingual alignment. Language separability can serve as an effective signal for multilingual curriculum learning, where interleaving samples with diverse separability levels yields stable and generalizable gains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3eeeca33-b00b-47d8-900d-ab1efc909537",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "365257b1-695c-4c78-95e0-b77dafff6db6",
  "sourceToolAssistantUUID": "3eeeca33-b00b-47d8-900d-ab1efc909537",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T07:56:31.029Z_

<details><summary>↩ Tool result · `toolu_01XZ1ND9J4y5n29W4uLiQJ7F`</summary>

```text
Web search results for query: "typological features data selection multilingual 2026"

Links: [{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.109/"},{"title":"SIGTYP 2026 Workshop, @EACL","url":"https://sigtyp.github.io/workshop.html"},{"title":"[2602.03551] Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models","url":"https://arxiv.org/abs/2602.03551"},{"title":"Incorporating Typological Features into Language Selection for Multilingual Neural Machine Translation | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-030-85896-4_27"},{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models","url":"https://arxiv.org/html/2602.03551"},{"title":"Revisiting Multilingual Data Mixtures in Language Model Pretraining","url":"https://arxiv.org/html/2510.25947v1"},{"title":"Modeling Language Variation and Universals: A Survey on Typological Linguistics for Natural Language Processing | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/article/view/1245"},{"title":"Modeling Language Variation and Universals: A Survey on Typological Linguistics for Natural Language Processing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/45/3/559/93372/Modeling-Language-Variation-and-Universals-A"},{"title":"A survey of multilingual large language models: Patterns","url":"https://www.cell.com/patterns/fulltext/S2666-3899(24)00290-3"},{"title":"Assessing the Impact of Typological Features on ...","url":"https://aclanthology.org/2026.eacl-long.109.pdf"}]

Based on the search results, I found several relevant papers and resources related to typological features, data selection, and multilingual work from 2026:

## Key Findings

**Recent 2026 Research:**

A 2026 EACL paper analyzes two large pre-trained multilingual translation models (NLLB-200 and Tower+) and finds that target language typology drives translation quality of both models, even after controlling for factors like data resourcedness and writing script. The research releases a set of fine-grained typological properties for 212 languages of the FLORES+ MT evaluation benchmark.

**Typological Features and Data Selection:**

Typological knowledge is being used for interpretation of hidden representations of multilingual neural models, multilingual data generation and selection, and typological annotation of texts. In 2026, there is special emphasis on the utility of LLMs for typological research.

**Workshop Focus:**

Topics of interest include the integration of typological features in language transfer and joint multilingual learning.

The search results show active research in 2026 on how typological features can improve data selection strategies for multilingual NLP systems, with particular focus on machine translation and the role of large language models in typological research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c2b8056c-c70f-45eb-ae6e-314f4b80f7bd",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "069d5265-0208-4f0f-817e-d515ba39a424",
  "sourceToolAssistantUUID": "c2b8056c-c70f-45eb-ae6e-314f4b80f7bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T07:56:31.160Z_

<details><summary>↩ Tool result · `toolu_01X8SNg8ygK2scZFfHdK3WK8`</summary>

```text
Web search results for query: "lang2vec URIEL cross-lingual transfer curriculum 2025 2026"

Links: [{"title":"[PDF] URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/URIEL-and-lang2vec:-Representing-languages-as-and-Levin-Littell/e3a824e59ac66ceaaa420e0de4f2b5d809231f6e"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning | Request PDF","url":"https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"},{"title":"(PDF) URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors","url":"https://www.academia.edu/87901461/URIEL_and_lang2vec_Representing_languages_as_typological_geographical_and_phylogenetic_vectors"},{"title":"SIGTYP 2023 The 5th Workshop on Research in Computational Linguistic","url":"https://sigtyp.github.io/workshops/2023/sigtyp/papers/SIGTYP2023_proceedings.pdf"},{"title":"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/html/2510.27183"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning","url":"https://aclanthology.org/P19-1301.pdf"},{"title":"Cross-Lingual Transfer: Language Selection","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-language-selection"},{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"Untangling the Influence of Typology, Data and Model Architecture on Ranking Transfer Languages for Cross-Lingual POS Tagging","url":"https://arxiv.org/html/2503.19979"},{"title":"Figure 1 from URIEL and lang2vec: Representing languages as typological, geographical, and phylogenetic vectors | Semantic Scholar","url":"https://www.semanticscholar.org/paper/URIEL-and-lang2vec:-Representing-languages-as-and-Levin-Littell/e3a824e59ac66ceaaa420e0de4f2b5d809231f6e/figure/1"}]

Based on the web search results, I found relevant information about lang2vec, URIEL, cross-lingual transfer, and recent curriculum-related work. Here are the key findings:

## Overview of lang2vec and URIEL

The URIEL knowledge base and lang2vec utility provide information-rich vector identifications of languages drawn from typological, geographical, and phylogenetic databases with standardized formats and semantics. The goal is to enable multilingual NLP, especially on less-resourced languages and make possible types of experiments that are otherwise difficult due to data sparsity.

## Recent Developments (2025-2026)

URIEL+ (2025) partially addresses data sparsity and transparency issues in the original URIEL by expanding data coverage to over 8,000 languages.

## Cross-Lingual Transfer Applications

Through the lang2vec tool, URIEL provides pre-computed language distances whose downstream applications include cross-lingual transfer, dependency parsing, and performance prediction. Recent research evaluates the impact of these additions on cross-lingual transfer using the LangRank framework, which ranks potential transfer languages for multilingual NLP tasks using gradient-boosted decision trees trained on language distances.

## Curriculum-Related Research

While the search results show substantial work on cross-lingual transfer language selection for various NLP tasks, specific information about curriculum learning approaches with lang2vec/URIEL in 2025-2026 was not explicitly highlighted in these results. The research does focus heavily on transfer language selection and ranking, which are related to curriculum design concepts.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "597461cc-8f2f-44e3-95ab-c1081f96d215",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "bc65db09-c9d1-41e9-a4af-3c7f8137a500",
  "sourceToolAssistantUUID": "597461cc-8f2f-44e3-95ab-c1081f96d215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 13 · 2026-05-10T07:56:32.535Z_

Let me continue with more targeted searches for Papers with Code and competing typological work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc65db09-c9d1-41e9-a4af-3c7f8137a500",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "72f26791-88f2-4612-aaae-d6380799d880",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

_source line 14 · 2026-05-10T07:56:32.956Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CkWzsZGhFhvPgcUe8V1fEr`</summary>

```json
{
  "query": "site:paperswithcode.com KazMMLU benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "72f26791-88f2-4612-aaae-d6380799d880",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c98775c1-60fe-4c31-a47b-46be60c1529f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

_source line 15 · 2026-05-10T07:56:33.397Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UvYgMVRgi9gkjmq9UW9yVH`</summary>

```json
{
  "query": "site:paperswithcode.com MiLiC-Eval multilingual"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c98775c1-60fe-4c31-a47b-46be60c1529f",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8f7209a0-ee12-402d-862b-a8e095e7ba2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

_source line 16 · 2026-05-10T07:56:33.615Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QvCqoqVKfsRdwqtn1fkdra`</summary>

```json
{
  "query": "Kazakh language model benchmark 2026 MMLU"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8f7209a0-ee12-402d-862b-a8e095e7ba2e",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0563bf80-0b32-4a27-9572-5f6d4d64bd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

_source line 17 · 2026-05-10T07:56:33.846Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TdWxV7g4cC9oTfcVSboRhs`</summary>

```json
{
  "query": "typological similarity LoRA multilingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0563bf80-0b32-4a27-9572-5f6d4d64bd2a",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f755ed14-0efb-46c6-8b81-b2eee47f61c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

_source line 18 · 2026-05-10T07:56:34.063Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_017xgdbCUtjU2pN6jfFpcsCE`</summary>

```json
{
  "query": "TIPA typological adapter multilingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f755ed14-0efb-46c6-8b81-b2eee47f61c2",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXjrWRtRu2ZcAdhpkRM",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d718db3e-3456-40ef-9d4e-e1be31552f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XByeHJt4a4GYDB1e8UteJb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 5522,
      "cache_read_input_tokens": 14687,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 5522,
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

### Tool result

_source line 19 · 2026-05-10T07:56:36.676Z_

<details><summary>↩ Tool result · `toolu_01CkWzsZGhFhvPgcUe8V1fEr`</summary>

```text
Web search results for query: "site:paperswithcode.com KazMMLU benchmark"

Links: [{"title":"cais/mmlu · Datasets at Hugging Face","url":"https://paperswithcode.com/dataset/mmlu"},{"title":"MML Benchmark (Multi-task Language Understanding)","url":"https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu"},{"title":"Papers with Code - MMLU (5-Shot) Benchmark (Multi-task Language Understanding)","url":"https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu-5-1"},{"title":"MMLU (Mathematics) Benchmark (Mathematical Reasoning)","url":"https://paperswithcode.com/sota/mathematical-reasoning-on-mmlu-mathematics"},{"title":"MMLU (Clinical Knowledge) Benchmark (Multiple Choice ...","url":"https://paperswithcode.com/sota/multiple-choice-question-answering-mcqa-on-23"},{"title":"Trending Papers - Hugging Face","url":"https://paperswithcode.com/dataset/mmlu-pro"},{"title":"Papers with Code - MMLU (Machine Learning) Benchmark (Multiple Choice Question Answering (MCQA))","url":"https://paperswithcode.com/sota/multiple-choice-question-answering-mcqa-on-6"},{"title":"MMLU-PRO (5-shot) Benchmark (Text Generation)","url":"https://paperswithcode.com/sota/text-generation-on-mmlu-pro-5-shot"},{"title":"MMLU-Pro Benchmark (MMLU)","url":"https://paperswithcode.com/sota/mmlu-on-mmlu-pro"},{"title":"Papers with Code - MMLU (High School Mathematics) Benchmark (Multiple Choice Question Answering (MCQA))","url":"https://paperswithcode.com/sota/multiple-choice-question-answering-mcqa-on-16"}]

The search results did not contain specific information about a "KazMMLU" benchmark on Papers with Code. The results returned information about the MMLU benchmark and various MMLU-related variants (such as MMLU-Pro, MMLU 5-Shot, and different subject areas like mathematics and clinical knowledge), but there was no mention of KazMMLU specifically.

It's possible that:
1. KazMMLU may not be indexed on Papers with Code
2. The benchmark may be named differently on the platform
3. It may be a newer or less widely known benchmark

If you're looking for information about KazMMLU specifically, you might want to try searching directly on the Papers with Code website or providing additional context about what this benchmark measures.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c98775c1-60fe-4c31-a47b-46be60c1529f",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "51ca7d2c-e402-4295-aad3-2e1037680d57",
  "sourceToolAssistantUUID": "c98775c1-60fe-4c31-a47b-46be60c1529f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-10T07:56:37.379Z_

<details><summary>↩ Tool result · `toolu_01UvYgMVRgi9gkjmq9UW9yVH`</summary>

```text
Web search results for query: "site:paperswithcode.com MiLiC-Eval multilingual"

Links: [{"title":"MiLiC-Eval: Benchmarking Multilingual LLMs for China's ...","url":"https://paperswithcode.com/paper/milic-eval-benchmarking-multilingual-llms-for"},{"title":"Paper page - Common Sense Beyond English: Evaluating and Improving Multilingual Language Models for Commonsense Reasoning","url":"https://paperswithcode.com/paper/common-sense-beyond-english-evaluating-and"},{"title":"Paper page - M-IFEval: Multilingual Instruction-Following Evaluation","url":"https://paperswithcode.com/paper/m-ifeval-multilingual-instruction-following"},{"title":"cais/mmlu · Datasets at Hugging Face","url":"https://paperswithcode.com/dataset/mmlu"},{"title":"MML Benchmark (Multi-task Language Understanding)","url":"https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu"},{"title":"Papers with Code - Guillaume Jacquet","url":"https://paperswithcode.com/search?q=author:Guillaume+Jacquet&order_by=stars"},{"title":"Papers with Code - McEval: Massively Multilingual Code Evaluation","url":"https://cs.paperswithcode.com/paper/mceval-massively-multilingual-code-evaluation"},{"title":"openai/openai_humaneval · Datasets at Hugging Face","url":"https://paperswithcode.com/dataset/humaneval"},{"title":"Towards Multilingual LLM Evaluation for European Languages | Papers With Code","url":"https://paperswithcode.com/paper/towards-cross-lingual-llm-evaluation-for"},{"title":"Vassilis Papavassiliou | Papers With Code","url":"https://paperswithcode.com/search?q=author:Vassilis+Papavassiliou&order_by=stars"}]

The search found a Papers with Code page for MiLiC-Eval. Papers with Code has 13 repositories available related to this paper, though the specific page content appears to have had loading issues in the search results.

The first search result (index 1) points to the paper page for "MiLiC-Eval: Benchmarking Multilingual LLMs for China's..." on Papers with Code at https://paperswithcode.com/paper/milic-eval-benchmarking-multilingual-llms-for, but the full details of the paper aren't fully captured in the search results provided. The page indicates it has associated code repositories on GitHub that can be followed.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8f7209a0-ee12-402d-862b-a8e095e7ba2e",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "1526194a-175b-4db5-83b8-7232c7f4b513",
  "sourceToolAssistantUUID": "8f7209a0-ee12-402d-862b-a8e095e7ba2e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T07:56:40.267Z_

<details><summary>↩ Tool result · `toolu_01QvCqoqVKfsRdwqtn1fkdra`</summary>

```text
Web search results for query: "Kazakh language model benchmark 2026 MMLU"

Links: [{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/html/2502.12829v2"},{"title":"[2502.12829] KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://arxiv.org/abs/2502.12829"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian,","url":"https://arxiv.org/pdf/2502.12829v1"},{"title":"KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan - ACL Anthology","url":"https://aclanthology.org/2025.acl-long.701/"},{"title":"[Quick Review] KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://liner.com/review/kazmmlu-evaluating-language-models-on-kazakh-russian-and-regional-knowledge"},{"title":"(PDF) KazMMLU: Evaluating Language Models on Kazakh, Russian, and Regional Knowledge of Kazakhstan","url":"https://www.researchgate.net/publication/389130089_KazMMLU_Evaluating_Language_Models_on_Kazakh_Russian_and_Regional_Knowledge_of_Kazakhstan"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Evaluating Language Models on Kazakh, Russian, and Regional ...","url":"https://www.semanticscholar.org/paper/KazMMLU:-Evaluating-Language-Models-on-Kazakh,-and-Togmanov-Mukhituly/ba3263d9dcda13c29f4240f2b3e53257589e6425"},{"title":"MMMLU Leaderboard","url":"https://llm-stats.com/benchmarks/mmmlu"}]

Based on the search results, I found comprehensive information about the Kazakh language model benchmark:

## KazMMLU: Kazakh Language Model Benchmark

KazMMLU is the first MMLU-style dataset specifically designed for Kazakh language. KazMMLU comprises 23,000 questions that cover various educational levels, including STEM, humanities, and social sciences, sourced from authentic educational materials and manually validated by native speakers and educators.

### Dataset Composition

The dataset includes 10,969 Kazakh questions and 12,031 Russian questions, reflecting Kazakhstan's bilingual education system and rich local context. The High School section includes questions in both Kazakh and Russian, covering subjects such as Mathematics, Physics, and Kazakh Literature. The University section only features questions in Russian, focusing on professional disciplines such as Law, Economics, and Medicine.

### Model Performance Results

GPT-4o and DeepSeek V3 emerge as the top performers, achieving remarkably similar average scores of 76.6% and 76.9% respectively, outperforming other models. Gemma-2-27B instruction-tuned model achieved the highest open-source score (57.4%), followed by Llama3.1-70B (56.2%) and its base variant (55.7%).

The benchmark was presented at the ACL 2025 conference and addresses a significant gap in NLP research, as Kazakhstan's culture and language remain underrepresented in the field of natural language processing despite having a population of twenty million.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0563bf80-0b32-4a27-9572-5f6d4d64bd2a",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "cbb7de6d-1fbd-43ff-87dc-003cdf96153c",
  "sourceToolAssistantUUID": "0563bf80-0b32-4a27-9572-5f6d4d64bd2a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T07:56:40.925Z_

<details><summary>↩ Tool result · `toolu_01TdWxV7g4cC9oTfcVSboRhs`</summary>

```text
Web search results for query: "typological similarity LoRA multilingual 2025 2026"

Links: [{"title":"Cross-Lingual Transfer and Parameter-Efficient Adaptation in the Turkic Language Family: A Theoretical Framework for Low-Resource Language Models","url":"https://arxiv.org/html/2604.06202"},{"title":"Typological Transcoding Through LoRA and Diffusion Models: A Methodological Framework for Stylistic Emulation of Eclectic Facades in Krakow","url":"https://www.mdpi.com/2075-5309/15/13/2292"},{"title":"A Unified Study of LoRA Variants: Taxonomy, Review, ...","url":"https://arxiv.org/pdf/2601.22708"},{"title":"One Voice, Many Tongues: Cross-Lingual Voice Cloning for Scientific Speech","url":"https://arxiv.org/html/2604.26136"},{"title":"Efficient Multilingual Expansion for LLMs via Layer-wise ...","url":"https://aclanthology.org/2025.acl-long.878.pdf"},{"title":"What Language(s) Does Aya-23 Think In? How ...","url":"https://aclanthology.org/2025.globalnlp-1.18.pdf"},{"title":"META-LORA: DATA-EFFICIENT MULTI-TASK FINE-TUNING FOR LARGE LANGUAGE MODELS","url":"https://arxiv.org/pdf/2510.11598"},{"title":"Progressive LoRA for Multimodal Continual Instruction ...","url":"https://aclanthology.org/2025.findings-acl.143.pdf"},{"title":"Mixture of Experts in Large Language Models †: Corresponding author: Junhao Song (junhao.song23@imperial.ac.uk)","url":"https://arxiv.org/html/2507.11181v2"},{"title":"Typological Limitations in Multilingual Models for Meitei ...","url":"https://aclanthology.org/2026.sigtyp-main.5.pdf"}]

Based on the web search results, I found several relevant papers and studies on the intersection of typological similarity, LoRA (Low-Rank Adaptation), and multilingual approaches from 2025-2026. Here are the key findings:

## Key Research Areas

**1. Turkic Language Family and Cross-Lingual Transfer**

A March 2026 paper develops a theoretical framework for language model adaptation within the Turkic language family (Azerbaijani, Kazakh, Uzbek, Turkmen, and Gagauz), which share strong typological similarities. The analysis integrates insights from multilingual representation learning and parameter-efficient fine-tuning methods such as Low-Rank Adaptation (LoRA). The framework highlights how typological similarity can enable efficient multilingual adaptation while also identifying structural limits in extremely low-resource settings.

**2. Multilingual LLM Expansion**

A 2025 ACL paper on "Efficient Multilingual Expansion for LLMs via Layer-wise" approaches discusses methods for expanding language models across multiple languages.

**3. LoRA Variants and Theory**

Low-Rank Adaptation (LoRA) has emerged as one of the most widely adopted parameter-efficient fine-tuning (PEFT) methods, though surveys on LoRA provide varying levels of depth regarding the theoretical foundations and design principles that distinguish LoRA variants.

**4. Typological Understanding in Multilingual Models**

Research shows that multilingual models leverage typological relationships, and analysis further demonstrates that script similarity and typological relations impact processing across model types.

These recent studies demonstrate active research into how typological properties of language families can be leveraged for more efficient multilingual model adaptation using parameter-efficient methods like LoRA.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f755ed14-0efb-46c6-8b81-b2eee47f61c2",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "3e8ad07f-0e99-4903-961d-2ce0c6c6b3e1",
  "sourceToolAssistantUUID": "f755ed14-0efb-46c6-8b81-b2eee47f61c2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T07:56:41.137Z_

<details><summary>↩ Tool result · `toolu_017xgdbCUtjU2pN6jfFpcsCE`</summary>

```text
Web search results for query: "TIPA typological adapter multilingual 2026"

Links: [{"title":"TIPA: Typologically Informed Parameter Aggregation - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.119/"},{"title":"[2601.16629] Typologically Informed Parameter Aggregation","url":"https://arxiv.org/abs/2601.16629"},{"title":"(PDF) Typologically Informed Parameter Aggregation","url":"https://www.researchgate.net/publication/400071787_Typologically_Informed_Parameter_Aggregation"},{"title":"Typologically Informed Parameter Aggregation Stef Accou⋄† and Wessel Poelman⋄","url":"https://arxiv.org/pdf/2601.16629"},{"title":"UDapter: Typology-based Language Adapters for Multilingual Dependency Parsing and Sequence Labeling | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/3/555/110444/UDapter-Typology-based-Language-Adapters-for"},{"title":"TIPA/README.md at master · stefaccou/TIPA","url":"https://github.com/stefaccou/TIPA/blob/master/README.md"},{"title":"SIGTYP 2026 Workshop, @EACL","url":"https://sigtyp.github.io/workshop.html"},{"title":"UCxn: Typologically Informed Annotation of Constructions Atop Universal Dependencies","url":"https://www.researchgate.net/publication/401325423_UCxn_Typologically_Informed_Annotation_of_Constructions_Atop_Universal_Dependencies"},{"title":"Typological Limitations in Multilingual Models for Meitei ...","url":"https://aclanthology.org/2026.sigtyp-main.5.pdf"},{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.109/"}]

Based on the search results, I found relevant information about TIPA and multilingual work in 2026:

## TIPA: Typologically Informed Parameter Aggregation

TIPA is a training-free framework that constructs proxy language adapters by aggregating existing ones, weighted by typological similarity. 

The research was published in the Findings of the Association for Computational Linguistics: EACL 2026. The work was conducted by Stef Accou and Wessel Poelman.

### Key Features and Results

TIPA was evaluated on five NLP tasks and over 230 languages, and consistently outperforms baselines such as English-only fine-tuning and selecting the typologically closest-language adapter, with the largest gains for languages lacking dedicated adapters.

The results demonstrate that typologically informed aggregation provides a viable alternative to language-specific modules without any training needed.

### Technical Approach

Integrated into the MAD-X framework, these proxies enable zero-shot cross-lingual transfer without additional training.

TIPA is a package for typologically informed parameter aggregation that provides tools to combine any number of architecturally identical modules, with a customisable weighting function.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d718db3e-3456-40ef-9d4e-e1be31552f04",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "5d38c2bb-4c61-4ce2-bb34-315f28afaf54",
  "sourceToolAssistantUUID": "d718db3e-3456-40ef-9d4e-e1be31552f04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T07:56:42.716Z_

Excellent. Now let me fetch the actual papers to verify details and get more specific information about TIPA and other competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5d38c2bb-4c61-4ce2-bb34-315f28afaf54",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXkb8VbQe6M4NKouRuH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "0b1c766d-5a53-4b0c-bac3-55a55bd6e6e1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WwUX6nCnTwTFHPmVVFpgSb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4402,
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

_source line 25 · 2026-05-10T07:56:43.158Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01DVrEksdeQJTF13sDeJYdtK`</summary>

```json
{
  "url": "https://arxiv.org/abs/2511.10229",
  "prompt": "What is the abstract and key contributions of LangGPS?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b1c766d-5a53-4b0c-bac3-55a55bd6e6e1",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXkb8VbQe6M4NKouRuH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f401888f-af55-422d-9b83-e4c21ecdd2ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WwUX6nCnTwTFHPmVVFpgSb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4402,
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

_source line 26 · 2026-05-10T07:56:43.608Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01ReKh2jUxMVSctFXyKbqfn8`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.27651",
  "prompt": "What is the abstract and key methodology of Budget-Xfer?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f401888f-af55-422d-9b83-e4c21ecdd2ec",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXkb8VbQe6M4NKouRuH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a73b418a-7ba9-41f0-a8d1-3038ec722506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WwUX6nCnTwTFHPmVVFpgSb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4402,
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

_source line 27 · 2026-05-10T07:56:44.047Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01QoTGTiocoyY3J6D4s7R5Q9`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.16629",
  "prompt": "What is TIPA and how does it use typological similarity for parameter aggregation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a73b418a-7ba9-41f0-a8d1-3038ec722506",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXkb8VbQe6M4NKouRuH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f7ca567e-b2d3-41d0-b027-685cabb26ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WwUX6nCnTwTFHPmVVFpgSb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20209,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4402,
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

_source line 28 · 2026-05-10T07:56:44.330Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_015cBEYSQ6gmDrminMxd4ecf`</summary>

```json
{
  "url": "https://arxiv.org/abs/2602.03551",
  "prompt": "What typological features are used and how are they applied to multilingual machine translation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f7ca567e-b2d3-41d0-b027-685cabb26ef3",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXkb8VbQe6M4NKouRuH",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d45ab16b-6440-44c0-ab5c-0d12be9fbff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01WwUX6nCnTwTFHPmVVFpgSb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4402,
      "cache_read_input_tokens": 20209,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4402
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 367,
          "cache_read_input_tokens": 20209,
          "cache_creation_input_tokens": 4402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4402,
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

_source line 29 · 2026-05-10T07:56:46.969Z_

<details><summary>↩ Tool result · `toolu_01ReKh2jUxMVSctFXyKbqfn8`</summary>

```text
# Budget-Xfer: Abstract and Methodology

## Abstract Overview

Budget-Xfer addresses a gap in cross-lingual transfer learning by introducing a framework that "formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem." Rather than simply selecting source languages, the approach simultaneously decides which languages to include and how much annotated data to use from each, given a fixed annotation budget.

## Key Methodology

The research employs a systematic experimental design involving:

- **Tasks evaluated:** Named entity recognition and sentiment analysis
- **Target languages:** Three African languages (Hausa, Yoruba, and Swahili)
- **Scale:** 288 experiments across two multilingual models
- **Strategies tested:** Four different allocation approaches for distributing training data across source languages

## Primary Findings

The work demonstrates that multi-source transfer substantially outperforms single-source approaches. Notably, the study reveals that embedding similarity—a common heuristic for language selection—shows task-dependent effectiveness, with random selection proving superior for some applications.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a73b418a-7ba9-41f0-a8d1-3038ec722506",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "94ef5197-1fc2-49b8-a634-b8294a680453",
  "sourceToolAssistantUUID": "a73b418a-7ba9-41f0-a8d1-3038ec722506",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-10T07:56:47.532Z_

<details><summary>↩ Tool result · `toolu_01DVrEksdeQJTF13sDeJYdtK`</summary>

```text
# LangGPS: Abstract and Key Contributions

## Abstract Overview

LangGPS addresses a challenge in multilingual instruction tuning: while joint training improves LLMs' multilingual capabilities, results remain sensitive to training data composition. The paper proposes that existing selection methods overlook "the intrinsic linguistic structure of multilingual data."

## Key Contributions

**Core Innovation**: A two-stage pre-selection framework using language separability—measuring "how well samples in different languages can be distinguished in the model's representation space."

**Methodology**: The approach first filters data by separability scores, then refines selections using existing methods.

**Empirical Results**: Testing across six benchmarks and 22 languages shows improvements in:
- Effectiveness and generalizability for existing selection methods
- Performance on understanding tasks and low-resource languages

**Insights Discovered**:
- High-separability samples create clearer language boundaries and enable faster adaptation
- Low-separability samples function as bridges for cross-lingual alignment
- Language separability supports multilingual curriculum learning when samples with diverse separability levels are interleaved

The work offers a linguistically-informed perspective on data utility in multilingual training contexts.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f401888f-af55-422d-9b83-e4c21ecdd2ec",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "830dcc0c-9af7-467e-b054-06b97ce414d0",
  "sourceToolAssistantUUID": "f401888f-af55-422d-9b83-e4c21ecdd2ec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-10T07:56:48.025Z_

<details><summary>↩ Tool result · `toolu_01QoTGTiocoyY3J6D4s7R5Q9`</summary>

```text
# TIPA: Typologically Informed Parameter Aggregation

TIPA is a training-free method for multilingual language models. According to the abstract, it "constructs proxy language adapters by aggregating existing ones, weighted by typological similarity."

## How It Works

The approach operates within the MAD-X framework and leverages linguistic typology to improve cross-lingual transfer. Rather than training new adapters for each language, TIPA combines existing adapter parameters using weights based on how linguistically similar languages are to one another.

## Key Benefits

The method enables "zero-shot cross-lingual transfer without additional training," making it computationally efficient. The researchers tested TIPA across five NLP tasks spanning over 230 languages and found it "consistently outperform[ed] or match[ed]" conventional baselines like English-only fine-tuning or selecting the closest language's adapter.

The largest performance improvements appeared for languages lacking dedicated adapters, demonstrating that typologically informed aggregation provides a viable alternative to language-specific modules when training resources are limited.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7ca567e-b2d3-41d0-b027-685cabb26ef3",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "5df3ddcd-350c-4546-82a3-2a06429af1ef",
  "sourceToolAssistantUUID": "f7ca567e-b2d3-41d0-b027-685cabb26ef3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-10T07:56:48.142Z_

<details><summary>↩ Tool result · `toolu_015cBEYSQ6gmDrminMxd4ecf`</summary>

```text
# Typological Features in Multilingual Machine Translation

Based on the paper abstract, the specific typological features used aren't detailed in the provided content. However, the research approach is clear:

The study analyzes how **"target language typology drives translation quality"** across two major models: NLLB-200 and Tower+. The researchers examined these effects while controlling for factors like training data availability and writing systems.

## Key Application Method

The typological properties are applied to understand why translation quality varies across languages. The findings suggest that certain linguistic characteristics make languages inherently more difficult to model, even in large pre-trained systems.

## Research Output

To support future work, the authors **released fine-grained typological properties for 212 languages** from the FLORES+ benchmark dataset. This dataset enables researchers to correlate specific linguistic features with translation performance.

## Notable Finding

Languages with particular typological properties reportedly benefit from broader search strategies beyond standard left-to-right beam search during decoding, suggesting that linguistic structure influences optimal translation approaches.

The full paper would contain detailed descriptions of which specific typological features were measured and analyzed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d45ab16b-6440-44c0-ab5c-0d12be9fbff9",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "33a8a7fa-e6e9-4830-91f0-842fb233b326",
  "sourceToolAssistantUUID": "d45ab16b-6440-44c0-ab5c-0d12be9fbff9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 33 · 2026-05-10T07:56:49.498Z_

Let me do some additional searches to check for more competing work on typological weighting for multilingual learning.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "33a8a7fa-e6e9-4830-91f0-842fb233b326",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5b0f0efe-acc2-47ce-9c4a-d2477ac9275b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 34 · 2026-05-10T07:56:49.728Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G7XNNYQG9KhAidbxfs4cv3`</summary>

```json
{
  "query": "\"typological weighting\" multilingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b0f0efe-acc2-47ce-9c4a-d2477ac9275b",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "4e4ae0e6-8c1a-4b6a-b169-34d0990dc727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 35 · 2026-05-10T07:56:49.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LHi8Cnco5m58cdzscbygX8`</summary>

```json
{
  "query": "URIEL+ language weighting cross-lingual 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4e4ae0e6-8c1a-4b6a-b169-34d0990dc727",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "51c7adeb-8a45-4172-a138-aba151cb648f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 36 · 2026-05-10T07:56:50.657Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MpFAxajw1VH2sPZQe6JFMx`</summary>

```json
{
  "query": "\"language similarity\" \"data weighting\" instruction tuning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51c7adeb-8a45-4172-a138-aba151cb648f",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ff7017b0-8c05-4b48-b5bd-08fb265f5733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 37 · 2026-05-10T07:56:50.696Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011KhMvMEMER9aoeVfnkRbiE`</summary>

```json
{
  "query": "multilingual adapter merging typological 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff7017b0-8c05-4b48-b5bd-08fb265f5733",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8a48218a-ec0c-4a84-b52b-a0478d4b95e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

_source line 38 · 2026-05-10T07:56:51.076Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GVZnBfLxU9sdgLc8qu1YJK`</summary>

```json
{
  "query": "pivot language selection multilingual NLP 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8a48218a-ec0c-4a84-b52b-a0478d4b95e5",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXm72ppXGw7QuDe8CZP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5c5f1878-4a96-4812-ab52-a4f8289beab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01DRvxCjSBxaRHU9rmgfsBZu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1439,
      "cache_read_input_tokens": 24611,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1439,
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

### Tool result

_source line 39 · 2026-05-10T07:56:57.438Z_

<details><summary>↩ Tool result · `toolu_011KhMvMEMER9aoeVfnkRbiE`</summary>

```text
Web search results for query: "multilingual adapter merging typological 2025 2026"

Links: [{"title":"One Model to Translate Them All? A Journey to Mount Doom for Multilingual Model Merging","url":"https://arxiv.org/html/2604.02881"},{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.109/"},{"title":"UDapter: Typology-based Language Adapters for Multilingual Dependency Parsing and Sequence Labeling | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/48/3/555/110444/UDapter-Typology-based-Language-Adapters-for"},{"title":"SIGTYP 2026 Workshop, @EACL","url":"https://sigtyp.github.io/workshop.html"},{"title":"Adapting Multilingual Models to Code-Mixed Tasks via Model Merging","url":"https://arxiv.org/html/2510.19782"},{"title":"AdaMergeX: Cross-Lingual Transfer with Large Language Models via Adaptive Adapter Merging | Request PDF","url":"https://www.researchgate.net/publication/392503822_AdaMergeX_Cross-Lingual_Transfer_with_Large_Language_Models_via_Adaptive_Adapter_Merging"},{"title":"SIGTYP 2025 The 7th Workshop on Research in Computational Linguistic","url":"https://aclanthology.org/2025.sigtyp-1.0.pdf"},{"title":"MULTILINGUAL MATTERS 2025-2026 www.multilingual-matters.com","url":"https://www.multilingual-matters.com/resources/pdfs/catalogues/MM%20Catalogue%202025-2026.pdf"},{"title":"Typological Limitations in Multilingual Models for Meitei ...","url":"https://aclanthology.org/2026.sigtyp-main.5.pdf"},{"title":"Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights","url":"https://arxiv.org/html/2603.28263"}]

Based on the search results, here are the key findings related to multilingual adapter merging and typological features in 2025-2026:

## Multilingual Adapter Merging Research

Recent approaches rely on merging language-specific adapters, operating in a parameter-efficient setting; while modular and scalable, such adapter-only updates offers limited capacity.

A notable 2025 paper on this topic is AdaMergeX: Cross-lingual transfer with large language models via adaptive adapter merging, presented at the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics.

## Typology and Multilingual Machine Translation

Two large pre-trained multilingual translation models, NLLB-200 and Tower+, which are state-of-the-art representatives of encoder-decoder and decoder-only machine translation, show that target language typology drives translation quality of both models. This research appears in a 2026 publication in the Proceedings of the European Chapter of the Association for Computational Linguistics.

## Integration of Typological Features

Integration of typological features in language transfer and joint multilingual learning is an active research area, with investigation into alternative ways to encoding heterogeneous external knowledge in machine learning algorithms. In 2026, there is a special emphasis on the utility of LLMs for typological research as evidenced by the SIGTYP workshop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8a48218a-ec0c-4a84-b52b-a0478d4b95e5",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "35afd9a7-58e5-466d-9903-006454545a2e",
  "sourceToolAssistantUUID": "8a48218a-ec0c-4a84-b52b-a0478d4b95e5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-10T07:56:57.447Z_

<details><summary>↩ Tool result · `toolu_01G7XNNYQG9KhAidbxfs4cv3`</summary>

```text
Web search results for query: ""typological weighting" multilingual 2025 2026"

Links: [{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models - ACL Anthology","url":"https://aclanthology.org/2026.eacl-long.109/"},{"title":"SIGTYP 2026 Workshop, @EACL","url":"https://sigtyp.github.io/workshop.html"},{"title":"[2602.03551] Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models","url":"https://arxiv.org/abs/2602.03551"},{"title":"Assessing the Impact of Typological Features on Multilingual Machine Translation in the Age of Large Language Models","url":"https://arxiv.org/html/2602.03551"},{"title":"MULTILINGUAL MATTERS 2025-2026 www.multilingual-matters.com","url":"https://www.multilingual-matters.com/resources/pdfs/catalogues/MM%20Catalogue%202025-2026.pdf"},{"title":"Full article: Measuring Linguistic Diversity: Limits and Extensions of the Greenberg Index","url":"https://www.tandfonline.com/doi/full/10.1080/09296174.2025.2567699"},{"title":"SIGTYP 2025 The 7th Workshop on Research in Computational Linguistic","url":"https://aclanthology.org/2025.sigtyp-1.0.pdf"},{"title":"Multilingual Multi-Label Emotion Classification at Scale with Synthetic Data","url":"https://arxiv.org/html/2604.12633v1"},{"title":"Typological Limitations in Multilingual Models for Meitei ...","url":"https://aclanthology.org/2026.sigtyp-main.5.pdf"},{"title":"MMLU-ProX: A Multilingual Benchmark for","url":"https://arxiv.org/pdf/2503.10497"}]

Here are the search results for "typological weighting" multilingual 2025 2026:

## Key Research Findings

Recent research finds that target language typology drives translation quality of multilingual machine translation models, even after controlling for more trivial factors, such as data resourcedness and writing script.

Two large pre-trained multilingual translation models analyzed are NLLB-200 and Tower+, which are state-of-the-art representatives of encoder-decoder and decoder-only machine translation, respectively.

Additionally, languages with certain typological properties benefit more from a wider search of the output space, suggesting that such languages could profit from alternative decoding strategies beyond the standard left-to-right beam search.

To facilitate further research in this area, a set of fine-grained typological properties for 212 languages of the FLORES+ MT evaluation benchmark has been released.

## Workshop and Community Activity

The 8th edition of SIGTYP workshop (scheduled for 2026) acts as a platform for exchange between typology-related research, multilingual NLP, and other research areas, with specific aims of raising awareness of linguistic typology and its potential in supporting multilingual NLP.

Research topics include the integration of typological features in language transfer and joint multilingual learning, examining alternative ways to encoding heterogeneous external knowledge in machine learning algorithms beyond established techniques such as "selective sharing".


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4e4ae0e6-8c1a-4b6a-b169-34d0990dc727",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "8c3e9603-eba0-422a-976f-d7d0b5cbeb19",
  "sourceToolAssistantUUID": "4e4ae0e6-8c1a-4b6a-b169-34d0990dc727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-10T07:56:57.853Z_

<details><summary>↩ Tool result · `toolu_01MpFAxajw1VH2sPZQe6JFMx`</summary>

```text
Web search results for query: ""language similarity" "data weighting" instruction tuning 2026"

Links: [{"title":"Neuron-Aware Data Selection in Instruction Tuning for Large Language Models | OpenReview","url":"https://openreview.net/forum?id=uq6UWRgzMr"},{"title":"Fine-Tuning Large Language Models for Specialized Use Cases - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S2949761224001147"},{"title":"What Makes Good Instruction-Tuning Data? An In-Context Learning Perspective","url":"https://arxiv.org/html/2604.25132"},{"title":"Published as a conference paper at ICLR 2026 DATAPROPHET:","url":"https://arxiv.org/pdf/2603.19688"},{"title":"Fine-tuning large language models (LLMs) in 2026 | SuperAnnotate","url":"https://www.superannotate.com/blog/llm-fine-tuning"},{"title":"Multilingual Instruction Tuning With Just a Pinch of Multilinguality","url":"https://arxiv.org/html/2401.01854"},{"title":"LESS: Selecting Influential Data for Targeted Instruction Tuning","url":"https://arxiv.org/html/2402.04333v1"},{"title":"Instruction Tuning for Large Language Models: A Survey | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3777411"},{"title":"Neuron-Aware Data Selection in Instruction Tuning for Large Language Models","url":"https://arxiv.org/html/2603.13201v1"},{"title":"[2402.04333] LESS: Selecting Influential Data for Targeted Instruction Tuning","url":"https://arxiv.org/abs/2402.04333"}]

I found several recent research papers on language similarity, data weighting, and instruction tuning from 2026. Here are the key findings:

## Recent Research (2026)

A framework called Nait evaluates the impact of instruction tuning data on LLMs performance by analyzing the similarity of neuron activation patterns between the instruction tuning dataset and the target domain capability. Training on a 10% Alpaca-GPT4 instruction tuning data subset selected by Nait consistently outperforms methods that rely on external advanced models or uncertainty-based features across various tasks.

The DATAPROPHET framework determines each dataset's relative weighting in a mixture using DATAPROPHET scores, where datasets assigned higher scores are expected to contribute more positively to target performance and are allocated a larger proportion of samples in the mixture. DATAPROPHET is described as a simple, training-free and interpretable metric that integrates cross-modal similarity, multimodal perplexity, and source dataset diversity.

## Multilingual Instruction Tuning Findings

Interestingly, research testing potential factors that might influence cross-lingual transfer found no significant correlations between language similarity and the degree of cross-lingual transfer. However, multilingual instruction tuning improves cross-lingual generalization while preserving performance on English under a fixed budget, with capable multilingual instruction-following models able to be tuned even with a minimal amount of multilingual data.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ff7017b0-8c05-4b48-b5bd-08fb265f5733",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "38ca825b-365b-4186-a71a-54ad106db267",
  "sourceToolAssistantUUID": "ff7017b0-8c05-4b48-b5bd-08fb265f5733",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-10T07:56:57.935Z_

<details><summary>↩ Tool result · `toolu_01GVZnBfLxU9sdgLc8qu1YJK`</summary>

```text
Web search results for query: "pivot language selection multilingual NLP 2025 2026"

Links: [{"title":"SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/html/2605.02601"},{"title":"Enhancing distant low-resource neural machine translation with semantic pivot - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1110016824016727"},{"title":"Pivoted Low Resource Multilingual Translation with NER Optimization | ACM Transactions on Asian and Low-Resource Language Information Processing","url":"https://dl.acm.org/doi/10.1145/3727876"},{"title":"Multilingual NLP: Code-Switching, Variants & Dialects | Appen","url":"https://www.appen.com/blog/emnlp-2025-multilingual-nlp"},{"title":"CFP: Recent Advances in Natural Language Processing (RANLP) 2025 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/recent-advances-natural-language-processing-2025-0"},{"title":"Advanced NLP Tools in 2026: The Ultimate Guide to Language AI & Automation - Tech2Geek","url":"https://www.tech2geek.net/advanced-nlp-tools-in-2025-the-ultimate-guide-to-language-ai-automation/"},{"title":"How to Choose the Best Pivot Language for Automatic Translation of Low-Resource Languages | ACM Transactions on Asian Language Information Processing","url":"https://dl.acm.org/doi/10.1145/2505126"},{"title":"[2505.14553] Pivot Language for Low-Resource Machine Translation","url":"https://arxiv.org/abs/2505.14553"},{"title":"Can Linguistically Related Languages Guide LLM Translation in Low-Resource Settings?","url":"https://arxiv.org/html/2603.16660v1"},{"title":"ICNLP 2026","url":"https://www.icnlp.net/"}]

Based on the search results, here's what I found about pivot language selection in multilingual NLP during 2025-2026:

## Recent Research and Applications

Multilingual strategies for NLP systems incorporate pivot translation or direct prompting in the target language, alongside techniques like strict formatting controls and grammar-checking post-processing.

## Pivot Language for Low-Resource Translation

Recent approaches combine linguistically related few-shot examples with a pivot language—a higher-resource language closely related to the target—to provide additional contextual grounding during generation. Research has used Hindi as a pivot language to translate Nepali into English, examining what makes Hindi a good candidate for the pivot.

## Language Selection Strategy

Experimental results using state-of-the-art statistical machine translation techniques revealed that the translation quality of 54.8% of the language pairs improved when a non-English pivot language was chosen. This suggests that careful pivot language selection—choosing a language other than English—can significantly benefit translation outcomes.

## Current Challenges in Multilingual NLP

Even with coverage across 80+ languages, models still struggle under heavy code-mixing and rapid domain shift. Additionally, NLP research and model development remain heavily skewed toward a small set of high-resource languages despite the existence of over 7,000 languages worldwide.

The research indicates that pivot language selection remains an important technique for improving multilingual NLP systems, particularly for low-resource languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5c5f1878-4a96-4812-ab52-a4f8289beab8",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "9ba267cc-bd43-450b-b532-b6c37eb5992d",
  "sourceToolAssistantUUID": "5c5f1878-4a96-4812-ab52-a4f8289beab8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-10T07:56:57.991Z_

<details><summary>↩ Tool result · `toolu_01LHi8Cnco5m58cdzscbygX8`</summary>

```text
Web search results for query: "URIEL+ language weighting cross-lingual 2025 2026"

Links: [{"title":"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/html/2510.19217"},{"title":"[2510.19217] Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://arxiv.org/abs/2510.19217"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning | Request PDF","url":"https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"},{"title":"[2510.27183] Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+","url":"https://arxiv.org/abs/2510.27183"},{"title":"arXiv:2409.18472v3 [cs.CL] 14 Feb 2025","url":"https://arxiv.org/pdf/2409.18472"},{"title":"Rethinking what Matters: Effective and Robust Multilingual Realignment for Low-Resource Languages","url":"https://arxiv.org/html/2511.06497"},{"title":"(PDF) Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+","url":"https://www.researchgate.net/publication/396787299_Modality_Matching_Matters_Calibrating_Language_Distances_for_Cross-Lingual_Transfer_in_URIEL"},{"title":"URIEL+: Enhancing Linguistic Inclusion and Usability in a ...","url":"https://aclanthology.org/2025.coling-main.463.pdf"},{"title":"Cross-Lingual Transfer: Language Selection","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-language-selection"},{"title":"Effective and Robust Multilingual Realignment for Low- ...","url":"https://aclanthology.org/2025.ijcnlp-long.102.pdf"}]

Based on the search results, I found several recent papers (from 2025-2026) related to URIEL+, language weighting, and cross-lingual transfer:

## Key Findings

**1. "Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+" (March 2026)**

This work develops a composite distance: a weighted average of distances from individual modalities, providing a single value that simplifies applications in cross-lingual transfer. The paper proposes novel, structure-aware representations for each distance type: speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, and a latent variables model for typology. On most of the tasks evaluated, including Entity Linking and XNLI, it reduces performance loss compared to using URIEL+ distances alone.

**2. "Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+" (March 2026)**

This work extends URIEL+ by introducing script vectors to represent writing system properties for 7,488 languages, integrating Glottolog to add 18,710 additional languages, and expanding lineage imputation for 26,449 languages, with improvements reducing feature sparsity by 14% for script vectors and increasing language coverage by up to 19,015 languages (1,007%).

**3. URIEL+ Overview (2025)**

URIEL+ is a language vector resource that encodes languages based on typological, geographic, phonological, syntactic, and phonetic inventory feature vectors.

These papers represent recent work on improving language weighting and distance metrics for cross-lingual transfer learning using the URIEL+ knowledge base.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "51c7adeb-8a45-4172-a138-aba151cb648f",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "2ae2a4e8-6f2b-41dd-8b74-a32c4964249c",
  "sourceToolAssistantUUID": "51c7adeb-8a45-4172-a138-aba151cb648f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 44 · 2026-05-10T07:57:00.472Z_

Let me fetch a couple more papers to get additional details on competing approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2ae2a4e8-6f2b-41dd-8b74-a32c4964249c",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXmqFpzGYutyGsaAF7m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "92dc1d5e-5286-4494-9301-15bca3fe61f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CYuEgeHpKDggrDWSYzhcUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2600,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 26050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
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

_source line 45 · 2026-05-10T07:57:01.449Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Co7kfawKDQzCaLE2CUVTes`</summary>

```json
{
  "url": "https://arxiv.org/abs/2510.19217",
  "prompt": "What are the key methods and findings about calibrating language distances in URIEL+ for cross-lingual transfer?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92dc1d5e-5286-4494-9301-15bca3fe61f1",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXmqFpzGYutyGsaAF7m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "bcc5dd99-4498-4fc8-bd00-2679eb1a8430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CYuEgeHpKDggrDWSYzhcUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2600,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 26050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
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

_source line 46 · 2026-05-10T07:57:01.737Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01SbnCFNPYKPBbAos1AovrG3`</summary>

```json
{
  "url": "https://arxiv.org/abs/2603.28263",
  "prompt": "What is the core approach to merging and weighting multilingual models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcc5dd99-4498-4fc8-bd00-2679eb1a8430",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXmqFpzGYutyGsaAF7m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "59271ccb-ca2a-4427-898e-3b39dac56e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CYuEgeHpKDggrDWSYzhcUH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2600,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 26050,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2106,
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

_source line 47 · 2026-05-10T07:57:01.943Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TEdw1acGCFFJi5nCAnTJ9w`</summary>

```json
{
  "query": "\"multi-source\" language selection instruction tuning 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "59271ccb-ca2a-4427-898e-3b39dac56e2f",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXmqFpzGYutyGsaAF7m",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2337387e-2049-4054-8fbb-5046bc3b23ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CYuEgeHpKDggrDWSYzhcUH",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2600,
      "cache_creation_input_tokens": 2106,
      "cache_read_input_tokens": 26050,
      "output_tokens": 252,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2106
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2600,
          "output_tokens": 252,
          "cache_read_input_tokens": 26050,
          "cache_creation_input_tokens": 2106,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2106,
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

_source line 48 · 2026-05-10T07:57:05.337Z_

<details><summary>↩ Tool result · `toolu_01SbnCFNPYKPBbAos1AovrG3`</summary>

```text
# Core Approach to Merging Multilingual Models

Based on the paper, the fundamental technique involves **merging an instruction-tuned LLM with language-specific base models** to transfer language knowledge without requiring extensive resources.

The method works by:

1. **Combining models through merging**: Rather than continual pre-training or fine-tuning, the researchers merge weights from a base language model into an instruction-following model.

2. **Eliminating redundant processes**: As stated in the abstract, this approach eliminates "the need of language-specific instructions and repeated fine-tuning processes whenever stronger instructed variants become available."

3. **Supporting multilingual capability**: The technique enables "multilingual capability through the combination of multiple language-specific models," allowing a single system to handle multiple low-resource languages simultaneously.

The key innovation is treating model merging as a **lightweight alternative to traditional adaptation methods**—avoiding the computational demands of continual pre-training and the data requirements of instruction-tuning while achieving competitive performance across Basque, Catalan, Galician, and Spanish.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "59271ccb-ca2a-4427-898e-3b39dac56e2f",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "22bc3dc5-1e80-4220-95b3-9dedd9e5d79c",
  "sourceToolAssistantUUID": "59271ccb-ca2a-4427-898e-3b39dac56e2f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 49 · 2026-05-10T07:57:05.726Z_

<details><summary>↩ Tool result · `toolu_01Co7kfawKDQzCaLE2CUVTes`</summary>

```text
# Key Methods and Findings on Calibrating Language Distances in URIEL+

## Core Methods

The research introduces "type-matched language distances" with structure-aware representations for each distance category:

- **Geography**: "speaker-weighted distributions for geography"
- **Genealogy**: "hyperbolic embeddings for genealogy"
- **Typology**: "a latent variables model for typology"

These specialized representations address a fundamental limitation: existing approaches use "one-size-fits-all vector representations" that don't account for different linguistic data structures.

## Main Innovation

The framework unifies these three distance signals into what the authors describe as "a robust, task-agnostic composite distance," providing a principled aggregation method that was previously lacking in linguistic knowledge bases.

## Key Findings

Across multiple zero-shot transfer benchmarks, the research demonstrates:

- **Type-matched representations** significantly improve performance when the distance type aligns with task requirements
- **Composite distance** consistently yields gains across most evaluated tasks

This work was accepted to the EACL 2026 Student Research Workshop, suggesting meaningful contributions to cross-lingual NLP transfer learning methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bcc5dd99-4498-4fc8-bd00-2679eb1a8430",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "183b6643-cd61-469c-9014-22e9c098dafa",
  "sourceToolAssistantUUID": "bcc5dd99-4498-4fc8-bd00-2679eb1a8430",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 50 · 2026-05-10T07:57:09.654Z_

<details><summary>↩ Tool result · `toolu_01TEdw1acGCFFJi5nCAnTJ9w`</summary>

```text
Web search results for query: ""multi-source" language selection instruction tuning 2025 2026"

Links: [{"title":"Published as a conference paper at ICLR 2026 DATAPROPHET:","url":"https://arxiv.org/pdf/2603.19688"},{"title":"LuxIT: A Luxembourgish Instruction Tuning Dataset from Monolingual Seed Data","url":"https://arxiv.org/html/2510.24434"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions? | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/investigating-multilingual-instruction-tuning-do-polyglot-models"},{"title":"Ultimate Guide – The Best Fine-Tuning Platforms of Open Source LLM 2026","url":"https://www.siliconflow.com/articles/en/the-best-fine-tuning-platforms-of-open-source-llm"},{"title":"Instruction Tuning for Large Language Models: A Survey","url":"https://dl.acm.org/doi/pdf/10.1145/3777411"},{"title":"Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/html/2402.13703v3"},{"title":"Exploring Two-Phase Continual Instruction Fine-tuning for Multilingual Adaptation in Large Language Models","url":"https://arxiv.org/html/2410.16006v3"},{"title":"[2402.13703] Investigating Multilingual Instruction-Tuning: Do Polyglot Models Demand for Multilingual Instructions?","url":"https://arxiv.org/abs/2402.13703"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"},{"title":"Multilingual Instruction-Tuning: Do Polyglot Models Need it?","url":"https://lamarr-institute.org/blog/multilingual-instruction-tuning-ai-model/"}]

I've successfully performed the web search for "multi-source language selection instruction tuning 2025 2026". Here are the key findings:

## Recent Research Highlights

**DATAPROPHET (Published at ICLR 2026):**
The research uses fourteen vision-language datasets as candidate sources and determines each dataset's relative weighting in the mixture using DATAPROPHET scores, with datasets assigned higher scores expected to contribute more positively to target performance and allocated a larger proportion of samples.

**Multilingual Instruction Tuning:**
Research demonstrates that instruction-tuning on parallel instead of monolingual corpora benefits cross-lingual instruction following capabilities by up to 9.9%.

**Luxembourgish Instruction Tuning (LuxIT):**
Researchers use DeepSeek-R1 to synthetically create instruction-answer pairs in Luxembourgish from filtered RTL news and Wikipedia articles, generating three instruction-answer pairs for each seed, yielding a total of 245,624 synthetic pairs.

**Continual Instruction Fine-tuning for Multilingual Models:**
A two-phase CFT process involves an English-only end-to-end instruction fine-tuned LLM (Phase 1) that is sequentially fine-tuned on a multilingual instruction dataset (Phase 2).

**Comprehensive IT Survey:**
A recent survey organized findings into primary categories including general methodology of IT, construction of IT datasets, instruction-tuned models and their characteristics, multimodal IT, domain-specific applications, efficiency techniques, and evaluation frameworks.

These results show active research in combining multiple data sources, language selection strategies, and instruction tuning across 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2337387e-2049-4054-8fbb-5046bc3b23ae",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "e8d93297-5034-4cc3-81c9-37df602216a1",
  "sourceToolAssistantUUID": "2337387e-2049-4054-8fbb-5046bc3b23ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-10T07:57:13.893Z_

Perfect. Now let me do one final search to check for any papers specifically on "pivot language" weighted instruction tuning or similar multi-pivot approaches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8d93297-5034-4cc3-81c9-37df602216a1",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXnh7Dbqk4DT4UzbsXG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "304cc03b-1618-4a13-bfe8-a50cebe81754",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QqZAd2Feg9nPHeqkTwZ8tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4356,
      "cache_read_input_tokens": 28156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4356,
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

_source line 52 · 2026-05-10T07:57:14.232Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012d1gEoq81T9XHKsc2N2vPH`</summary>

```json
{
  "query": "\"pivot languages\" weighting multilingual instruction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "304cc03b-1618-4a13-bfe8-a50cebe81754",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXnh7Dbqk4DT4UzbsXG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "39b5e1e8-426b-4c3d-a11b-65dc7f96d951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QqZAd2Feg9nPHeqkTwZ8tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4356,
      "cache_read_input_tokens": 28156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4356,
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

_source line 53 · 2026-05-10T07:57:14.427Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Qq1fTHG17hxBDsVas7vvFA`</summary>

```json
{
  "query": "typological \"language clustering\" instruction tuning cross-lingual 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39b5e1e8-426b-4c3d-a11b-65dc7f96d951",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXnh7Dbqk4DT4UzbsXG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "31314c15-1597-42e7-bd35-b0de9cdd224c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QqZAd2Feg9nPHeqkTwZ8tB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4356,
      "cache_read_input_tokens": 28156,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4356,
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

_source line 54 · 2026-05-10T07:57:21.818Z_

<details><summary>↩ Tool result · `toolu_012d1gEoq81T9XHKsc2N2vPH`</summary>

```text
Web search results for query: ""pivot languages" weighting multilingual instruction 2025 2026"

Links: [{"title":"PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning - ACL Anthology","url":"https://aclanthology.org/2025.naacl-short.19/"},{"title":"[2311.08711] PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/abs/2311.08711"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning | NSF Public Access Repository","url":"https://par.nsf.gov/biblio/10517622-plug-leveraging-pivot-language-cross-lingual-instruction-tuning"},{"title":"Large Multilingual Models Pivot Zero-Shot Multimodal Learning across Languages","url":"https://arxiv.org/html/2308.12038v3"},{"title":"Enhancing distant low-resource neural machine translation with semantic pivot - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1110016824016727"},{"title":"GitHub - ytyz1307zzh/PLUG: Code for the ACL 2024 paper \"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning\"","url":"https://github.com/ytyz1307zzh/PLUG"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://arxiv.org/pdf/2311.08711"},{"title":"SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures","url":"https://arxiv.org/html/2605.02601"},{"title":"[2311.07439] Investigating Multi-Pivot Ensembling with Massively Multilingual Machine Translation Models","url":"https://arxiv.org/abs/2311.07439"},{"title":"PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning","url":"https://par.nsf.gov/servlets/purl/10517622"}]

Based on the search results, I found relevant recent research on pivot languages in multilingual instruction learning. Here are the key findings:

## PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning (2025)

The research identifies English as an internal pivot language and proposes to disentangle the roles of English and target language data in training by designing two roles as pivoted objectives and regulating between the two to better generalize for under-represented languages. This addresses negative interference observed when appending English tuning data with its translated pair when adapting English-centric LLMs to other languages. This work was published at the 2025 NAACL Conference (North American Chapter of ACL) in Albuquerque, New Mexico.

## PLUG: Leveraging Pivot Language in Cross-Lingual Instruction Tuning

PLUG proposes using a high-resource language, primarily English, as the pivot to enhance instruction tuning in lower-resource languages.

## Multilingual Strategies in 2026 Tasks

Recent systems have incorporated multilingual strategies including pivot translation or direct prompting in the target language for multilingual evaluation tasks.

These approaches demonstrate the importance of pivot languages, particularly English, in addressing the challenge of extending instruction-tuned large language models beyond English to support diverse languages.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "39b5e1e8-426b-4c3d-a11b-65dc7f96d951",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "a8d4da20-4c08-499c-a86d-677d1b664679",
  "sourceToolAssistantUUID": "39b5e1e8-426b-4c3d-a11b-65dc7f96d951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-10T07:57:22.119Z_

<details><summary>↩ Tool result · `toolu_01Qq1fTHG17hxBDsVas7vvFA`</summary>

```text
Web search results for query: "typological "language clustering" instruction tuning cross-lingual 2026"

Links: [{"title":"Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?","url":"https://arxiv.org/html/2410.07809"},{"title":"Cross-Lingual Transfer: Language Selection","url":"https://www.emergentmind.com/topics/cross-lingual-transfer-language-selection"},{"title":"The Effect of Language Diversity When Fine-Tuning Large Language Models for Translation","url":"https://arxiv.org/html/2505.13090v2"},{"title":"Cross-Lingual Transfer with Language-Specific Subnetworks for Low-Resource Dependency Parsing | Computational Linguistics | MIT Press","url":"https://direct.mit.edu/coli/article/49/3/613/116157/Cross-Lingual-Transfer-with-Language-Specific"},{"title":"Linguistically-Informed Multilingual Instruction Tuning","url":"https://arxiv.org/pdf/2410.07809"},{"title":"Published in Transactions on Machine Learning Research (11/2025)","url":"https://openreview.net/pdf?id=oapsbIO1Bd"},{"title":"Against All Odds: Overcoming Typology, Script, and Language Confusion in","url":"https://ojs.aaai.org/index.php/AAAI/article/view/34533/36688"},{"title":"Analyzing the Effect of Linguistic Similarity on Cross- ...","url":"https://aclanthology.org/2025.findings-acl.454.pdf"},{"title":"Choosing Transfer Languages for Cross-Lingual Learning | Request PDF","url":"https://www.researchgate.net/publication/335779022_Choosing_Transfer_Languages_for_Cross-Lingual_Learning"},{"title":"Breaking the Curse of Multilinguality with Cross-lingual Expert Language Models","url":"https://arxiv.org/html/2401.10440v1"}]

I found several highly relevant research papers and resources on this topic. Here's a summary of the search results:

## Recent Research on Typological Language Clustering and Instruction Tuning

Recent work investigates linguistically informed language selection techniques using typological feature vectors and k-means clustering algorithms to select languages based for instruction tuning. Models from different families are instruction-tuned using LoRA on specific language subsets, measuring their cross-lingual and cross-task performance on natural language understanding and commonsense reasoning tasks.

### Key Methodologies

For many-to-many transfer, clustering languages by combined typological metrics (e.g., weighted sums of syntax, phonology, and inventory distances) and selecting cluster medoids ensures that each major typological cluster is represented. Multi-source language training with optimally chosen language triplets selected to maximize typological or embedding-based dissimilarity reliably surpasses single-language baselines.

### Specialized Approaches

The Cross-lingual Expert Language Models (X-ELM) framework mitigates parameter competition by training multiple smaller "expert" models, each specialized on a distinct cluster of languages. Using typological structure to specialize experts provides additional benefits over automatic data clustering, and training along the hierarchy of language families in multiple rounds yields further performance benefits.

### Language Diversity Effects

Fine-tuning on broader language sets consistently improves translation across all categories: fully supervised, partially supervised, and zero-shot pairs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31314c15-1597-42e7-bd35-b0de9cdd224c",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "52ed1d17-c4ed-4c22-a4ed-5889deeecfd6",
  "sourceToolAssistantUUID": "31314c15-1597-42e7-bd35-b0de9cdd224c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 56 · 2026-05-10T07:57:23.613Z_

Let me fetch the two most directly relevant papers to get specific details.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52ed1d17-c4ed-4c22-a4ed-5889deeecfd6",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXocMjn5z1PmKn2jcfN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "62049994-0d91-4bd2-9e4c-a4da133160d8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011H3U43EZCDm1QMtJLJnJmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 32512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1877,
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

_source line 57 · 2026-05-10T07:57:24.076Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Xz5d3GrA8VTEYbEACKQV1t`</summary>

```json
{
  "url": "https://arxiv.org/abs/2410.07809",
  "prompt": "What is the main approach using typological features and language clustering for instruction tuning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62049994-0d91-4bd2-9e4c-a4da133160d8",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXocMjn5z1PmKn2jcfN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "eac10414-579d-4724-a0b1-ddd27fc0caed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011H3U43EZCDm1QMtJLJnJmB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 32512,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1877,
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

_source line 58 · 2026-05-10T07:57:24.910Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0131nbqHcY2bRgKZuVQkQ5uk`</summary>

```json
{
  "url": "https://aclanthology.org/2025.naacl-short.19/",
  "prompt": "What is PROM and how does it use pivoted optimization for multilingual instruction learning?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eac10414-579d-4724-a0b1-ddd27fc0caed",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXocMjn5z1PmKn2jcfN",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d9ec450a-0c96-416b-9b1e-2c3b0d3d4c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_011H3U43EZCDm1QMtJLJnJmB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 1877,
      "cache_read_input_tokens": 32512,
      "output_tokens": 204,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1877
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 204,
          "cache_read_input_tokens": 32512,
          "cache_creation_input_tokens": 1877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1877,
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

_source line 59 · 2026-05-10T07:57:28.276Z_

<details><summary>↩ Tool result · `toolu_01Xz5d3GrA8VTEYbEACKQV1t`</summary>

```text
# Linguistically-Informed Language Selection for Instruction Tuning

Based on the provided abstract, the paper proposes selecting languages for multilingual instruction tuning using linguistic features rather than random selection.

## Main Approach

The researchers employ "a simple algorithm to choose diverse languages" informed by linguistic characteristics. Rather than tuning on all available languages (which causes performance degradation through the "curse of multilinguality"), they strategically select a subset of typologically diverse languages.

## Key Innovation

The approach demonstrates that "careful selection generally leads to better outcomes than choosing languages at random." By selecting languages based on their linguistic diversity and properties, the method aims to improve model performance across multiple languages and tasks while reducing computational costs.

## Significance

This methodology addresses a critical challenge in multilingual NLP: the tension between comprehensive language coverage and model performance. The authors provide code and resources for their language selection algorithm, enabling reproducible research and better-informed dataset creation for multilingual systems.

The study suggests that strategic, linguistically-motivated language selection is more effective than either random selection or indiscriminate inclusion of all available languages.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eac10414-579d-4724-a0b1-ddd27fc0caed",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "1d99baaf-86af-419c-b6ff-944ff07ee6d9",
  "sourceToolAssistantUUID": "eac10414-579d-4724-a0b1-ddd27fc0caed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-10T07:57:29.666Z_

<details><summary>↩ Tool result · `toolu_0131nbqHcY2bRgKZuVQkQ5uk`</summary>

```text
# PROM: Pivoted and Regulated Optimization for Multilingual Instruction Learning

PROM is a research approach designed to improve how large language models can be adapted to languages beyond English. The core challenge it addresses is that when researchers combine English instruction-tuning data with translated versions for other languages, the two datasets interfere with each other negatively.

## How Pivoted Optimization Works

The key innovation involves treating "English as an internal pivot language." Rather than simply mixing English and target-language data together, PROM distinguishes between their separate roles during training. As the abstract explains:

> "we first design two roles as pivoted objectives, and also propose to regulate between the two, to better generalize for under-represented languages"

This means the method creates distinct training objectives for English and target languages, then carefully balances between them rather than letting them compete.

## Practical Impact

By disentangling how English and target-language data contribute to model training, PROM aims to improve performance across various languages on multiple benchmarks. The researchers have made their code publicly available, facilitating further development of multilingual instruction-tuning methods.

The paper was published at NAACL 2025 (April, Albuquerque) and spans pages 222-228 in the conference proceedings.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d9ec450a-0c96-416b-9b1e-2c3b0d3d4c28",
  "isSidechain": true,
  "promptId": "1f700693-258e-4aad-b8a0-4e13fb09d714",
  "agentId": "af9cb2e5e5a668192",
  "type": "user",
  "uuid": "e1e7bcdd-c447-4a3c-ab88-77213c11f046",
  "sourceToolAssistantUUID": "d9ec450a-0c96-416b-9b1e-2c3b0d3d4c28",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 61 · 2026-05-10T07:58:02.614Z_

Excellent. Now I have comprehensive information. Let me compile my findings into a detailed report.

## COMPREHENSIVE VERIFICATION REPORT: TWMP (Typologically-Weighted Multi-Pivot) Paper Review

### 1. VERIFICATION OF CITED PAPERS

#### LangGPS - VERIFIED ✓
**Citation:** "LangGPS: Language Separability Guided Data Pre-Selection for Joint Multilingual Instruction Tuning" arXiv:2511.10229 AAAI 2026

**Status:** Paper exists and is accurately described
**Abstract:** LangGPS proposes a two-stage pre-selection framework using "language separability"—quantifying how well samples in different languages can be distinguished in the model's representation space. It filters training data based on separability scores, then refines selections using existing methods.
**Key Results:** Tested across six benchmarks and 22 languages; demonstrates improvements in effectiveness for low-resource languages and understanding tasks. Shows that high-separability samples create clearer language boundaries while low-separability samples function as bridges for cross-lingual alignment.
**Source:** [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)

#### Budget-Xfer - VERIFIED ✓
**Citation:** "Budget-Xfer: Budget-Constrained Source Language Selection for Cross-Lingual Transfer to African Languages" arXiv:2603.27651 SIGIR 2026

**Status:** Paper exists and is accurately described
**Abstract:** Formulates multi-source cross-lingual transfer as a budget-constrained resource allocation problem. Jointly optimizes which source languages to include AND how much data to allocate from each language, given a fixed annotation budget.
**Key Results:** Evaluated on named entity recognition and sentiment analysis for Hausa, Yoruba, and Swahili using two multilingual models (288 experiments). Demonstrates that multi-source transfer significantly outperforms single-source transfer (Cohen's d = 0.80 to 1.98). Interestingly reveals that embedding similarity (common heuristic for language selection) shows task-dependent effectiveness.
**Source:** [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)

---

### 2. COMPETING/RELATED WORK IDENTIFIED

#### DIRECT COMPETITORS TO TWMP'S CORE NOVELTY:

**A. TIPA (Typologically Informed Parameter Aggregation) - 2026 - STRONG COMPETITOR**
**Citation:** [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629), Findings of EACL 2026
- **Core Innovation:** Constructs proxy language adapters by **aggregating existing adapters weighted by typological similarity** (zero-shot, training-free)
- **Scope:** Evaluated on 5 NLP tasks across 230+ languages
- **Key Result:** Consistently outperforms baselines like English-only fine-tuning and selecting the closest-language adapter; largest gains for languages lacking dedicated adapters
- **Relation to TWMP:** Directly uses typological similarity for weighting multilingual modules. This is very similar conceptually to TWMP's use of typological weighting for multi-pivot data.
- **Source:** [TIPA on ACL Anthology](https://aclanthology.org/2026.findings-eacl.119/)

**B. URIEL+ Recent Enhancements (2025-2026) - COMPLEMENTARY BUT RELEVANT**
- **"Simple Additions, Substantial Gains: Expanding Scripts, Languages, and Lineage Coverage in URIEL+"** (arXiv:2510.27183, March 2026)
  - Extends URIEL+ with script vectors for 7,488 languages and integrates Glottolog for 18,710 additional languages
  - Reduces feature sparsity by 14% for script vectors
- **"Modality Matching Matters: Calibrating Language Distances for Cross-Lingual Transfer in URIEL+"** (arXiv:2510.19217, March 2026, EACL 2026 Student Workshop)
  - Introduces type-matched language distances with structure-aware representations (speaker-weighted distributions for geography, hyperbolic embeddings for genealogy, latent variables model for typology)
  - Creates robust composite distance for cross-lingual transfer
- **Relation to TWMP:** These improve the typological distance metrics that TWMP would rely on, but don't themselves implement multi-pivot weighting or data selection
- **Sources:** [arXiv:2510.27183](https://arxiv.org/abs/2510.27183), [arXiv:2510.19217](https://arxiv.org/abs/2510.19217)

**C. PROM (Pivoted and Regulated Optimization) - 2025 - RELATED APPROACH**
**Citation:** Published at NAACL 2025 (April, Albuquerque)
- **Core Innovation:** Treats English as an "internal pivot language" and disentangles roles of English vs. target-language data via separate training objectives with regulation between them
- **Problem Addressed:** Negative interference when combining English instruction-tuning data with translated versions
- **Relation to TWMP:** Also uses pivoting concept for multilingual instruction learning, but focuses on English as single pivot rather than multi-pivot weighting scheme
- **Source:** [PROM on ACL Anthology](https://aclanthology.org/2025.naacl-short.19/)

**D. Linguistically-Informed Multilingual Instruction Tuning - 2024**
**Citation:** [Linguistically-Informed Multilingual Instruction Tuning: Is There an Optimal Set of Languages to Tune?](https://arxiv.org/abs/2410.07809), Published in Transactions on Machine Learning Research (November 2025)
- **Approach:** Uses typological feature vectors and k-means clustering to select diverse languages for instruction tuning
- **Finding:** Careful selection based on linguistic diversity outperforms random language selection; addresses "curse of multilinguality"
- **Relation to TWMP:** Also uses typological features for language selection in instruction tuning, but focuses on selecting a subset of languages rather than weighting multiple sources

#### TANGENTIALLY RELATED RECENT WORK:

**E. "Assessing the Impact of Typological Features on Multilingual Machine Translation"** (arXiv:2602.03551, 2026 EACL)
- Analyzes how target language typology drives translation quality in NLLB-200 and Tower+ models
- Releases fine-grained typological properties for 212 languages in FLORES+ benchmark
- Shows that certain typological properties benefit from broader decoding strategies

**F. "Merge and Conquer: Instructing Multilingual Models by Adding Target Language Weights"** (arXiv:2603.28263)
- Merges instruction-tuned LLMs with language-specific base models for multilingual capability
- Avoids continual pre-training and repeated fine-tuning
- Lightweight alternative to traditional adaptation for low-resource languages

**G. Cross-Lingual Expert Language Models (X-ELM)** (arXiv:2401.10440)
- Uses typological structure to specialize expert models for distinct language clusters
- Training along language family hierarchies provides performance benefits
- Multi-source language training with typologically/embedding-based dissimilar triplets outperforms single-language baselines

**H. DATAPROPHET (ICLR 2026)** (arXiv:2603.19688)
- Determines dataset weighting in mixtures using DATAPROPHET scores
- Integrates cross-modal similarity, multimodal perplexity, and dataset diversity
- Training-free, interpretable metric for data weighting

**I. Recent Work on Multi-Source Selection:**
- KazMMLU (arXiv:2502.12829, ACL 2025): First MMLU-style benchmark for Kazakh (23,000 questions)
- Budget-Xfer (as cited above) addresses multi-source optimization for African languages
- PLUG (arXiv:2311.08711, ACL 2024): Leverages English pivot in cross-lingual instruction tuning

---

### 3. BENCHMARKS AND EVALUATION GAPS FOUND

**KazMMLU:** Successfully identified and verified
- First MMLU-style dataset specifically for Kazakh
- 23,000 questions (10,969 Kazakh + 12,031 Russian)
- Presented at ACL 2025; covers STEM, humanities, social sciences
- **Source:** [KazMMLU on arXiv](https://arxiv.org/abs/2502.12829)

**MiLiC-Eval:** Partially verified
- Located on Papers with Code: [MiLiC-Eval: Benchmarking Multilingual LLMs for China's...](https://paperswithcode.com/paper/milic-eval-benchmarking-multilingual-llms-for)
- Appears to be a benchmark for multilingual LLMs, but full details not retrieved

---

### 4. KEY FINDINGS ON NOVELTY

**STRENGTHS OF TWMP'S NOVELTY CLAIM:**

1. **Multi-Pivot Weighting Not Yet Fully Explored:** While TIPA weights adapter aggregation by typological similarity and PROM uses pivot languages, TWMP appears to be the **first systematic approach to combine BOTH concepts**: using multiple typologically-diverse pivot languages with learned or typologically-informed weighting for data selection in instruction tuning.

2. **Data Selection vs. Module Aggregation:** TIPA aggregates existing trained adapters; TWMP appears to weight raw instruction-tuning data before training, which is a different problem.

3. **Pivot Language Strategy Evolution:** PLUG and PROM focus on English as pivot; TWMP's multi-pivot approach with typological weighting is more sophisticated.

**POTENTIAL OVERLAP/CONCERNS:**

1. **TIPA's March 2026 publication (same venue cycle as TWMP):** TIPA demonstrates that typological similarity weighting for multilingual modules is effective. If TWMP's core novelty is similar weighting applied to data rather than adapters, the conceptual distance may be narrow.

2. **Typological feature integration:** Multiple papers (X-ELM, Linguistically-Informed Instruction Tuning, URIEL+ enhancements) all demonstrate value of typological features for language selection/clustering in recent 2025-2026 work.

3. **Data weighting literature:** DATAPROPHET and other data weighting approaches are relatively recent (ICLR 2026), suggesting this is an active research area.

---

### 5. CRITICAL ASSESSMENT

**TWMP appears to have legitimate novelty IF:**
- The combination of typological distance metrics (URIEL/URIEL+) with multi-source pivot language selection for instruction data weighting is novel
- The specific weighting formulation or curriculum learning approach is non-obvious
- Empirical results on Kazakh/Mongolian and other low-resource language benchmarks are strong

**AREAS OF CONCERN:**
1. TIPA (published March 2026 in EACL Findings) demonstrates the effectiveness of typological-similarity-based weighting for multilingual NLP at scale (230+ languages, 5 tasks)
2. The conceptual gap between "weight adapters by typology" (TIPA) and "weight data sources by typology" (TWMP) may not be substantial enough to constitute strong novelty
3. Pivot language selection with typological grounding is well-explored (PLUG, PROM, recent work on language families)

**RECOMMENDATIONS FOR AUTHORS:**
1. Clearly differentiate from TIPA's adapter aggregation approach—emphasize why data-level weighting is fundamentally different/better
2. Demonstrate superiority over simpler baselines combining URIEL+ distances with standard multi-source selection
3. Show that typological weighting outperforms embedding-based or other heuristic weighting (as Budget-Xfer found embedding similarity isn't always better)
4. Provide extensive evaluation on truly low-resource languages (Kazakh, Mongolian, African languages) where the approach should shine

---

## SOURCES

### Verified Cited Papers
- [LangGPS on arXiv](https://arxiv.org/abs/2511.10229)
- [Budget-Xfer on arXiv](https://arxiv.org/abs/2603.27651)

### Major Competing/Related Work (2025-2026)
- [TIPA: Typologically Informed Parameter Aggregation](https://arxiv.org/abs/2601.16629) - EACL 2026 Findings
- [URIEL+ Script Expansion](https://arxiv.org/abs/2510.27183) - March 2026
- [Modality Matching in URIEL+](https://arxiv.org/abs/2510.19217) - EACL 2026 Student Workshop
- [PROM: Pivoted Optimization](https://aclanthology.org/2025.naacl-short.19/) - NAACL 2025
- [Linguistically-Informed Instruction Tuning](https://arxiv.org/abs/2410.07809) - TMLR November 2025
- [Assessing Typological Features in MT](https://arxiv.org/abs/2602.03551) - EACL 2026
- [Merge and Conquer Multilingual Models](https://arxiv.org/abs/2603.28263)
- [Cross-Lingual Expert Language Models](https://arxiv.org/abs/2401.10440)
- [DATAPROPHET Data Weighting](https://arxiv.org/abs/2603.19688) - ICLR 2026
- [KazMMLU Benchmark](https://arxiv.org/abs/2502.12829) - ACL 2025

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1e7bcdd-c447-4a3c-ab88-77213c11f046",
  "isSidechain": true,
  "agentId": "af9cb2e5e5a668192",
  "requestId": "req_011CatXpAfC8qfLNZ1MKJrv6",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3d15102-8423-46fb-bfef-bf3419115cc3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "dafd8ad2-3dfd-4271-968b-e119b82cd34e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01QdFBAbnJo1BMASsobaGBBn",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 783,
      "cache_read_input_tokens": 34389,
      "output_tokens": 3344,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 783
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3344,
          "cache_read_input_tokens": 34389,
          "cache_creation_input_tokens": 783,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 783,
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
