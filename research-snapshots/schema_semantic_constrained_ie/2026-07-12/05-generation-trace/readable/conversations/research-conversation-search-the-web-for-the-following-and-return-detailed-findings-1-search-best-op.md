# Research conversation: Search the web for the following and return detailed findings: 1. Search "best open source LLM 2026" - what are the curr

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 15
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a9de7cafc51ea998f.jsonl`
- **Structured JSON:** [`f454dd225ec43c7d6bfb.json`](../../sessions/f4/f454dd225ec43c7d6bfb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

15 recorded events

### User

_source line 1 · 2026-05-10T06:50:06.474Z_

Search the web for the following and return detailed findings:

1. Search "best open source LLM 2026" - what are the current frontier open-source language models as of early 2026?
2. Search "SOTA open source language model leaderboard 2026" - current rankings
3. Search "best open source model information extraction NER event extraction 2026"
4. Search "Llama 4 OR Qwen3 OR Mistral 2026 language model" - what are the latest model versions
5. Search "huggingface open source LLM benchmark 2026"
6. Search "self-consistency Wang 2023 NLP citation" to verify the Wang et al. 2023 self-consistency paper

For each search, report model names, organizations, benchmark scores, and release dates. I need to know what open-source models are at the frontier in 2026 for NLP/IE tasks.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "06e65ff5-265f-4b06-a87a-d89209354951",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:50:08.612Z_

I'll search for current information on frontier open-source language models in 2026. Let me run all these searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "06e65ff5-265f-4b06-a87a-d89209354951",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9aad2e1-3e94-444b-8fc0-3632cd068e92",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 642,
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

_source line 3 · 2026-05-10T06:50:08.820Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012NUWSih7wYFHQVL6vDbTZ3`</summary>

```json
{
  "query": "best open source LLM 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a9aad2e1-3e94-444b-8fc0-3632cd068e92",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "7e6bfaa6-de4f-493d-b40b-2091e69ad395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 642,
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

_source line 4 · 2026-05-10T06:50:09.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014AxB2MDeCDmNs7dDrpJgeh`</summary>

```json
{
  "query": "SOTA open source language model leaderboard 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e6bfaa6-de4f-493d-b40b-2091e69ad395",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "561fc902-e95c-4aec-8c5a-2fed33d388b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 642,
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

_source line 5 · 2026-05-10T06:50:09.096Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FwnN6SXRp3p3uJc2SK459m`</summary>

```json
{
  "query": "best open source model information extraction NER event extraction 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "561fc902-e95c-4aec-8c5a-2fed33d388b8",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9d6e9492-ee83-49e2-b51f-ff0f7c3b0759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 642,
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

_source line 6 · 2026-05-10T06:50:09.268Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01G2fdGF8jd4Mr3cdK8w6PUq`</summary>

```json
{
  "query": "Llama 4 OR Qwen3 OR Mistral 2026 language model"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9d6e9492-ee83-49e2-b51f-ff0f7c3b0759",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "13e75706-d734-41ba-9f58-6d01e6abd422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 642,
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

_source line 7 · 2026-05-10T06:50:09.472Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SQ7wpYGgsubqRBw2f5Ng5y`</summary>

```json
{
  "query": "huggingface open source LLM benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "13e75706-d734-41ba-9f58-6d01e6abd422",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f3870de8-1312-4cdd-85fa-4fc677f781dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 642,
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

_source line 8 · 2026-05-10T06:50:09.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BUFxK11LfJfaxLSEP6PeGW`</summary>

```json
{
  "query": "self-consistency Wang 2023 NLP citation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3870de8-1312-4cdd-85fa-4fc677f781dd",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSg8F2hWpK5jiLTrJdP",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8be15e63-a5d6-403a-af05-ec12e30b93d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01EuL5joU1JFd7J2v8Wr6Yf1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 642,
      "cache_read_input_tokens": 16155,
      "output_tokens": 329,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 642
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 329,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 642,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 642,
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

_source line 9 · 2026-05-10T06:50:14.760Z_

<details><summary>↩ Tool result · `toolu_01BUFxK11LfJfaxLSEP6PeGW`</summary>

```text
Web search results for query: "self-consistency Wang 2023 NLP citation"

Links: [{"title":"[2203.11171] Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://arxiv.org/abs/2203.11171"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models | OpenReview","url":"https://openreview.net/forum?id=1PL1NIMMrw"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://iclr.cc/media/iclr-2023/Slides/11718.pdf"},{"title":"[PDF] Self-Consistency Improves Chain of Thought Reasoning in Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Self-Consistency-Improves-Chain-of-Thought-in-Wang-Wei/5f19ae1135a9500940978104ec15a5b8751bc7d2"},{"title":"Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.cs.toronto.edu/~cmaddis/courses/csc2541_w25/presentations/self-consistency.pdf"},{"title":"arXiv:2407.12994v2 [cs.CL] 24 Jul 2024","url":"https://arxiv.org/pdf/2407.12994"},{"title":"(PDF) Self-Consistency Improves Chain of Thought Reasoning in Language Models","url":"https://www.researchgate.net/publication/359390115_Self-Consistency_Improves_Chain_of_Thought_Reasoning_in_Language_Models"},{"title":"dblp: Self-Consistency Improves Chain of Thought Reasoning in Language Models.","url":"https://dblp.org/rec/conf/iclr/0002WSLCNCZ23.html"},{"title":"Self-Consistency with Chain of Thought (CoT-SC) | by Johannes Koeppern | Medium","url":"https://medium.com/@johannes.koeppern/self-consistency-with-chain-of-thought-cot-sc-2f7a1ea9f941"},{"title":"SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT ...","url":"http://webdocs.cs.ualberta.ca/~dale/papers/iclr23b.pdf"}]

Based on the search results, here's information about the Self-Consistency paper by Wang et al. from 2023:

## Citation Information

The authors are Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, and Denny Zhou. The paper was published at ICLR 2023.

## Paper Overview

The paper proposes a new decoding strategy called self-consistency to replace the naive greedy decoding used in chain-of-thought prompting, which first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths.

## Key Results

Empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

The paper's arXiv preprint is available at https://arxiv.org/abs/2203.11171.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8be15e63-a5d6-403a-af05-ec12e30b93d0",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "bcce7af9-e288-4c69-b33d-3034537a7f32",
  "sourceToolAssistantUUID": "8be15e63-a5d6-403a-af05-ec12e30b93d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:50:16.085Z_

<details><summary>↩ Tool result · `toolu_01FwnN6SXRp3p3uJc2SK459m`</summary>

```text
Web search results for query: "best open source model information extraction NER event extraction 2026"

Links: [{"title":"GitHub - gkiril/oie-resources: A curated list of Open Information Extraction (OIE) resources: papers, code, data, etc. · GitHub","url":"https://github.com/gkiril/oie-resources"},{"title":"GitHub - zjunlp/Low-resource-KEPapers: A Paper List of Low-resource Information Extraction","url":"https://github.com/zjunlp/Low-resource-KEPapers"},{"title":"information-extraction · GitHub Topics · GitHub","url":"https://github.com/topics/information-extraction"},{"title":"Information Extraction in NLP - GeeksforGeeks","url":"https://www.geeksforgeeks.org/nlp/information-extraction-in-nlp/"},{"title":"GitHub - wutong8023/Awesome_Information_Extraction: Literature Survey of Information Extraction, especially Relation Extraction, Event Extraction, and Slot Filling. · GitHub","url":"https://github.com/wutong8023/Awesome_Information_Extraction"},{"title":"6 best named entity recognition APIs for entity detection","url":"https://www.assemblyai.com/blog/6-best-named-entity-recognition-apis-entity-detection"},{"title":"Benchmarking LLM-based Information Extraction Tools for Medical Documents | medRxiv","url":"https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full"},{"title":"Task: Named Entity Recognition · Explosion · Developer tools and consulting for AI, Machine Learning and NLP","url":"https://explosion.ai/_/task/ner"},{"title":"Information Extraction from Multi-Domain Scientific Documents: Methods and Insights","url":"https://www.mdpi.com/2076-3417/15/16/9086"},{"title":"What is Information Extraction? IE for Machine Learning Engineers","url":"https://kili-technology.com/blog/information-extraction-ie-guide"}]

Based on the search results, here's what I found about the best open-source models for information extraction, NER, and event extraction in 2026:

## Top Open-Source Options

**spaCy** is a leading open-source NLP library for these tasks. Spacy is an open-source NLP library that helps MLEs with language processing and extraction, lets you train NLP models to extract information from large datasets efficiently with the GPU pipeline, and provides easy-to-use language extraction components, such as NER, part-of-speech tagging, lemmatization, and text classifications.

**GLiNER** is another promising option. GLiNER is a generalist model for Named Entity Recognition that can be integrated with spaCy's versatile NLP environment. When comparing state-of-the-art models such as BERT, LLaMA, GLiNER, and spaCy across diverse domains, the findings highlight the promise of spaCy and GLiNER for practical deployment in under-resourced language settings.

**Google's Gemma3** is the best-performing open-source model according to recent benchmarks. Google's Gemma3 with 27B parameters, given image inputs and a zero-shot prompt, achieved an average F1 score of 41.3 for information extraction tasks.

## Available Resources

Recent approaches include Dynamic Prefix-Tuning for Generative Template-based Event Extraction (ACL 2022), Contextualized Soft Prompts for Extraction of Event Arguments (ACL 2023, Findings), and Unified Multimodal Information Extraction with Instruction Tuning (arXiv, 2024).

**Hugging Face** provides another pathway for accessing models. Hugging Face provides various pre-trained transformer models to shorten development time and reduce computing costs when building deep learning applications, with MLEs able to download and access hundreds of large language models via API, including Bert, RoBERTa, GPT, and Transformer-XL.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d6e9492-ee83-49e2-b51f-ff0f7c3b0759",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "57915d41-4b49-4b4c-afde-28cb9b49bcff",
  "sourceToolAssistantUUID": "9d6e9492-ee83-49e2-b51f-ff0f7c3b0759",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:50:16.090Z_

<details><summary>↩ Tool result · `toolu_01SQ7wpYGgsubqRBw2f5Ng5y`</summary>

```text
Web search results for query: "huggingface open source LLM benchmark 2026"

Links: [{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"open-llm-leaderboard (Open LLM Leaderboard)","url":"https://huggingface.co/open-llm-leaderboard"},{"title":"salttechno/LLM-Model-Comparison-2026 · Datasets at Hugging Face","url":"https://huggingface.co/datasets/salttechno/LLM-Model-Comparison-2026"},{"title":"Hugging Face Releases ml-intern: An Open-Source Agent That Automates Post-Training","url":"https://rits.shanghai.nyu.edu/ai/hugging-face-releases-ml-intern-an-open-source-agent-that-automates-post-training/"},{"title":"LLM Performance Leaderboard - a Hugging Face Space by ArtificialAnalysis","url":"https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard"},{"title":"Hugging Face Releases ml-intern: An Open-Source AI Agent that Automates the LLM Post-Training Workflow - MarkTechPost","url":"https://www.marktechpost.com/2026/04/21/hugging-face-releases-ml-intern-an-open-source-ai-agent-that-automates-the-llm-post-training-workflow/"},{"title":"The Big Benchmarks Collection - a open-llm-leaderboard Collection","url":"https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection"},{"title":"HuggingFace ml-intern: Open-Source ML Research Agent - AgentConn Blog","url":"https://agentconn.com/blog/huggingface-ml-intern-open-source-ml-research-agent-2026/"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"blog/open-llm-leaderboard-mmlu.md at main · huggingface/blog","url":"https://github.com/huggingface/blog/blob/main/open-llm-leaderboard-mmlu.md"}]

Based on the search results, here's what I found about Hugging Face open source LLM benchmarks in 2026:

## Open LLM Leaderboard

The Open LLM Leaderboard lets you explore and compare the performance of open‑source large language models on a range of tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU‑PRO. The Open LLM Leaderboard is a wrapper running the open-source benchmarking library Eleuther AI LM Evaluation Harness, which runs evaluations on the spare cycles of Hugging Face's compute cluster, and stores the results in a dataset on the hub.

## Recent Developments (2026)

On April 21, 2026, HuggingFace shipped ml-intern — an open-source AI agent that automates the end-to-end ML post-training loop. In less than 10 hours, the agent pushed a Qwen3-1.7B model's scientific reasoning score on the GPQA benchmark from 8.5% to 32%, outperforming the specific GPQA results of Claude Code (22.99%).

## Other Benchmark Resources

An open dataset compares 16 large language models from 7 providers across 22 fields: pricing, benchmark scores, context windows, latency, API features, and recommended use cases. Benchmark scores include MMLU, HumanEval, MATH, and MT-Bench scores from original model papers, provider technical reports, or verified third-party evaluations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3870de8-1312-4cdd-85fa-4fc677f781dd",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "3337c359-c832-4261-98aa-35af63a43706",
  "sourceToolAssistantUUID": "f3870de8-1312-4cdd-85fa-4fc677f781dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T06:50:16.821Z_

<details><summary>↩ Tool result · `toolu_01G2fdGF8jd4Mr3cdK8w6PUq`</summary>

```text
Web search results for query: "Llama 4 OR Qwen3 OR Mistral 2026 language model"

Links: [{"title":"10 Best Open-Source LLM Models (2025 Updated): Llama 4, Qwen 3 and DeepSeek R1","url":"https://huggingface.co/blog/daya-shankar/open-source-llms"},{"title":"Best Small AI Models to Run with Ollama (2026): Phi-4, Gemma 3, Qwen 3, GGUF Picks | Local AI Master","url":"https://localaimaster.com/blog/small-language-models-guide-2026"},{"title":"Top 5 Local LLM Tools and Models in 2026 - Pinggy","url":"https://pinggy.io/blog/top_5_local_llm_tools_and_models/"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"Local AI in 2026: The Best Models to Run on Your Own Hardware (Qwen, Mistral, Llama Updated) | AI Magicx Blog | AI Magicx","url":"https://www.aimagicx.com/blog/local-ai-models-2026-qwen-mistral-llama-hardware-guide"},{"title":"library","url":"https://ollama.com/library"},{"title":"New Ollama Models May 2026: Latest Releases & Updates","url":"https://www.promptquorum.com/local-llms/top-open-source-models-ollama"},{"title":"Model Catalog - LM Studio","url":"https://lmstudio.ai/models"},{"title":"Open-Source LLMs Compared 2026 – 25+ Models… – Till Freitag","url":"https://till-freitag.com/en/blog/open-source-llm-comparison"},{"title":"Best Local LLM Models 2026 | Developer Comparison","url":"https://www.sitepoint.com/best-local-llm-models-2026/"}]

Based on the search results, here's what I found about Llama 4, Qwen 3, and Mistral models in 2026:

## Llama 4

Meta's Llama 4 family includes Scout and Maverick, which are instruction-tuned variants with 128k context and strong general performance. Llama 4 Scout is among the most downloaded models on Ollama in 2026 as the best overall MoE model.

## Qwen 3

Qwen3 is the latest generation of large language models in Qwen series, offering a comprehensive suite of dense and mixture-of-experts (MoE) models. Qwen3 8B is described as the best local coding model for 8 GB VRAM machines, achieving 76% HumanEval and using 5 GB of memory with multilingual support. Qwen3.5 was released in March 2026, and Qwen3.6 was released in April 2026.

## Mistral 2026 Models

Mistral AI's Mistral Large 3 is a state-of-the-art open-weight mixture-of-experts model trained with 41B active and 675B total parameters on 3000 NVIDIA H200 GPUs. Mistral Small 4 has 119B total parameters but only activates 24B per inference pass.

Mistral is noted as the most efficient model among the most downloaded on Ollama in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13e75706-d734-41ba-9f58-6d01e6abd422",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "3e5d7959-ecfa-47aa-b1a6-d76b44844e5f",
  "sourceToolAssistantUUID": "13e75706-d734-41ba-9f58-6d01e6abd422",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:50:17.197Z_

<details><summary>↩ Tool result · `toolu_014AxB2MDeCDmNs7dDrpJgeh`</summary>

```text
Web search results for query: "SOTA open source language model leaderboard 2026"

Links: [{"title":"LLM Leaderboard 2026 — Compare Top AI Models - Vellum","url":"https://www.vellum.ai/llm-leaderboard"},{"title":"LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/llm"},{"title":"LLM Leaderboard 2026: Compare 300+ Top AI Models by Intelligence, Speed & Price","url":"https://llm-stats.com/"},{"title":"Code Generation Benchmarks 2026: SOTA LLMs for Programming | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/code-generation"},{"title":"Speech AI Leaderboard 2026: Best STT, ASR and TTS Models | CodeSOTA | CodeSOTA","url":"https://www.codesota.com/speech"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"SOTA AI Models: Benchmarks, Metrics & Deployment Guide","url":"https://huggingface.co/blog/daya-shankar/sota-ai-models"},{"title":"Open LLM Leaderboard - a Hugging Face Space by open-llm-leaderboard","url":"https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"},{"title":"Top Open-Source LLMs 2026: The Best Models & Comparison","url":"https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/"},{"title":"The New King of Open Source ASR: Real-Time, SOTA, and Unmatched Accuracy | by Bytefer | Mar, 2026 | Medium","url":"https://medium.com/@bytefer/the-new-king-of-open-source-asr-real-time-sota-and-unmatched-accuracy-d56e3bf953f0"}]

Based on the search results, here's what I found about SOTA open source language model leaderboards in 2026:

## Key Leaderboards

The open source LLM leaderboard displays the latest public benchmark performance for open-weight and open-source models released after April 2024, and you can compare open-source and open-weight LLM benchmarks for Llama, DeepSeek, Qwen, Kimi and more across reasoning, coding, math, and multilingual tasks.

The Open LLM Leaderboard lets you explore and compare the performance of open‑source large language models on a range of tests such as IFEval, BBH, MATH, GPQA, MUSR, and MMLU‑PRO.

## Top Open-Source Models

Kimi K2.6 currently leads among open-weights LLMs (90.5% gpqa), and the open-weights ecosystem is dominated by Llama, Qwen, DeepSeek, Mistral, GLM and Gemma.

The best open-source LLMs in 2026 are Meta Llama 4 for general reasoning, Mistral Large for speed and efficiency, and Qwen 2.5 for multilingual tasks, with other top models including DeepSeek for coding and Microsoft Phi-4 for high-performance reasoning in small-scale deployments.

## Notable Resources

For comprehensive leaderboards, you can check Vellum's Open LLM Leaderboard, the Hugging Face Open LLM Leaderboard, and CodeSOTA's specialized benchmarks for coding, speech, and other modalities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "561fc902-e95c-4aec-8c5a-2fed33d388b8",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "eb878821-7db0-4378-a561-d52e581c13c3",
  "sourceToolAssistantUUID": "561fc902-e95c-4aec-8c5a-2fed33d388b8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:50:17.524Z_

<details><summary>↩ Tool result · `toolu_012NUWSih7wYFHQVL6vDbTZ3`</summary>

```text
Web search results for query: "best open source LLM 2026"

Links: [{"title":"Best Open Source LLM Leaderboard 2026 | Open Source Model Rankings and Tier List | Onyx AI","url":"https://onyx.app/open-llm-leaderboard"},{"title":"The Best Open-Source LLMs in 2026","url":"https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models"},{"title":"Best Open Source LLM 2026 Ranking + Ollama Guide","url":"https://whatllm.org/best-open-source-llm"},{"title":"Best Open Source LLMs in 2026: Rankings and Licensing Comparison | Onyx AI","url":"https://onyx.app/insights/best-open-source-llms-2026"},{"title":"Top 7 open source LLMs for 2026","url":"https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/"},{"title":"Best Open Source LLMs: Complete 2026 Guide | Contabo Blog","url":"https://contabo.com/blog/open-source-llms/"},{"title":"Best Open Source LLMs in 2026: We Reviewed 7 Models","url":"https://fireworks.ai/blog/best-open-source-llms"},{"title":"Open Source LLM Leaderboard 2026 — Compare Open-Weight Models","url":"https://www.vellum.ai/open-llm-leaderboard"},{"title":"Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings","url":"https://llm-stats.com/leaderboards/open-llm-leaderboard"},{"title":"11 Top Open-Source LLMs for 2026 and Their Uses | DataCamp","url":"https://www.datacamp.com/blog/top-open-source-llms"}]

Based on the search results, here's a comprehensive overview of the best open-source LLMs in 2026:

## Top Performing Models

The top-ranked models for various tasks include GLM-5, Kimi K2.5, and Qwen 3.5, with Kimi K2.5 leading in code generation and reasoning.

### Notable Top Models:

**Kimi K2.5**: Recommended when you want the strongest combination of code generation, math performance, and permissive licensing in one model. It has MIT licensing, 1T total / 32B active parameters, 76.8% SWE-bench, 87.6% GPQA Diamond, 96.1% AIME 2025, and 99.0% HumanEval.

**GLM-5**: Listed as MIT-licensed with 744B total / 40B active parameters, 77.8% SWE-bench, 86.0% GPQA Diamond, and 1,451 Arena Elo.

**DeepSeek-V4**: Designed for long-context reasoning, coding, and agentic workflows with DeepSeek-V4-Pro (1.6T total, 49B active) as the flagship model and DeepSeek-V4-Flash (284B total, 13B active) as a more cost-efficient option.

**MiMo-V2.5**: The latest open-source model family from Xiaomi for agentic coding and long-horizon reasoning, with MiMo-V2.5-Pro (1.02T total, 42B active) as the flagship for coding agents.

## Licensing Considerations

MIT and Apache 2.0 licensed models that allow commercial use without restriction include Kimi K2.5, GLM-4.7, GLM-5, MiMo-V2-Flash, GPT-oss 120B, Qwen 3.5, and Qwen 3 235B.

The "best" model ultimately depends on your specific use case, hardware constraints, and whether you need specialized capabilities like coding, reasoning, or multimodal support.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7e6bfaa6-de4f-493d-b40b-2091e69ad395",
  "isSidechain": true,
  "promptId": "ba2b72ef-a65d-494f-b65d-bdbbc7cb5597",
  "agentId": "a9de7cafc51ea998f",
  "type": "user",
  "uuid": "0b5e6350-4f47-4b42-8a29-f46ca903c825",
  "sourceToolAssistantUUID": "7e6bfaa6-de4f-493d-b40b-2091e69ad395",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T06:50:50.511Z_

## Detailed Findings on Frontier Open-Source LLMs and NLP/IE Models in 2026

### 1. Best Open-Source LLMs (Frontier Models)

**Top-Performing Models:**
- **Kimi K2.5/K2.6** - Leads in overall benchmarks with MIT licensing. K2.6 achieves 90.5% on GPQA. Parameters: 1T total / 32B active. Notable scores: SWE-bench 76.8%, GPQA Diamond 87.6%, AIME 2025 96.1%, HumanEval 99.0%
- **GLM-5** - MIT-licensed with 744B total / 40B active parameters. Scores: SWE-bench 77.8%, GPQA Diamond 86.0%, Arena Elo 1,451
- **DeepSeek-V4** - Deep reasoning specialist with two variants: V4-Pro (1.6T total, 49B active) and V4-Flash (284B total, 13B active) for cost-efficiency
- **MiMo-V2.5** - Xiaomi's latest family for coding agents and long-horizon reasoning. MiMo-V2.5-Pro: 1.02T total, 42B active
- **Meta Llama 4** - With Scout and Maverick instruction-tuned variants, 128k context window
- **Qwen 3.x series** - Qwen 3.5 (March 2026) and Qwen 3.6 (April 2026) releases; Qwen 3 8B achieves 76% HumanEval with multilingual support
- **Mistral Large 3** - 41B active / 675B total parameters, trained on 3000 NVIDIA H200 GPUs
- **Microsoft Phi-4** - High-performance reasoning in small-scale deployments

### 2. Current Leaderboard Rankings (SOTA)

The ecosystem is dominated by:
- Llama, Qwen, DeepSeek, Mistral, GLM, and Gemma families
- Benchmarks tracked: IFEval, BBH, MATH, GPQA, MUSR, MMLU-PRO
- Kimi K2.6 currently leads among open-weights LLMs
- Models trained after April 2024 are evaluated on the Open LLM Leaderboard

**Key Benchmark Leaders:**
- Code generation: Kimi K2.5 (99.0% HumanEval)
- Math reasoning: Kimi K2.5 (96.1% AIME 2025)
- Coding tasks: DeepSeek-V4 specialist
- Efficiency: Mistral noted as most efficient among top downloaded models

### 3. Information Extraction & NER Models (2026)

**Top Open-Source IE/NER Tools:**
- **spaCy** - Leading open-source NLP library with GPU pipeline support, offers NER, POS tagging, lemmatization, text classification
- **GLiNER** - Generalist Named Entity Recognition model that integrates with spaCy
- **Google Gemma3** (27B parameters) - Best-performing open-source model for IE tasks with average F1 score of 41.3 for information extraction with zero-shot prompting
- **Hugging Face transformer models** - BERT, RoBERTa, GPT, Transformer-XL available via API
- **Recent approaches** (2022-2024):
  - Dynamic Prefix-Tuning for Template-based Event Extraction (ACL 2022)
  - Contextualized Soft Prompts for Event Arguments (ACL 2023)
  - Unified Multimodal Information Extraction with Instruction Tuning (2024)

### 4. Latest Model Versions (Llama 4, Qwen 3, Mistral)

**Meta Llama 4:**
- Scout and Maverick instruction-tuned variants
- 128k context window
- Among most downloaded on Ollama 2026
- Best overall MoE (Mixture of Experts) model

**Qwen 3 Series:**
- Qwen 3.5 - Released March 2026
- Qwen 3.6 - Released April 2026
- Qwen 3 8B - 76% HumanEval, 5GB memory footprint for 8GB VRAM machines
- Dense and MoE model variants

**Mistral 2026 Models:**
- Mistral Large 3 - 41B active / 675B total parameters
- Mistral Small 4 - 119B total, 24B active per inference
- Most efficient model among top downloaded

### 5. Hugging Face Open LLM Benchmark (2026)

**Benchmark Infrastructure:**
- Open LLM Leaderboard uses Eleuther AI LM Evaluation Harness
- Evaluations run on Hugging Face spare compute clusters
- Covers: IFEval, BBH, MATH, GPQA, MUSR, MMLU-PRO
- Models evaluated: 16+ LLMs from 7 providers with 22 tracked metrics

**Recent Development (April 2026):**
- HuggingFace released **ml-intern** - An open-source AI agent automating the entire ML post-training loop
- Achieved: Qwen3-1.7B scientific reasoning (GPQA) improved from 8.5% to 32% in under 10 hours
- Performance note: Outperformed Claude Code's 22.99% GPQA score

### 6. Self-Consistency Paper Verification (Wang et al. 2023)

**Confirmed Citation:**
- **Title:** "Self-Consistency Improves Chain of Thought Reasoning in Language Models"
- **Authors:** Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou
- **Venue:** ICLR 2023 (International Conference on Learning Representations)
- **ArXiv:** https://arxiv.org/abs/2203.11171

**Key Contribution:**
- Proposes self-consistency decoding strategy as replacement for greedy decoding in chain-of-thought prompting
- Method: Samples diverse reasoning paths, then selects most consistent answer by marginalizing sampled paths
- **Performance improvements:**
  - GSM8K: +17.9%
  - SVAMP: +11.0%
  - AQuA: +12.2%
  - StrategyQA: +6.4%
  - ARC-challenge: +3.9%

---

## Sources:
- [Best Open Source LLM Leaderboard 2026](https://onyx.app/open-llm-leaderboard)
- [The Best Open-Source LLMs in 2026](https://www.bentoml.com/blog/navigating-the-world-of-open-source-large-language-models)
- [Best Open Source LLM 2026 Ranking + Ollama Guide](https://whatllm.org/best-open-source-llm)
- [Best Open Source LLMs in 2026: Rankings and Licensing Comparison](https://onyx.app/insights/best-open-source-llms-2026)
- [Top 7 open source LLMs for 2026](https://www.instaclustr.com/education/open-source-ai/top-7-open-source-llms-for-2026/)
- [Best Open Source LLMs: Complete 2026 Guide](https://contabo.com/blog/open-source-llms/)
- [Best Open Source LLMs in 2026: We Reviewed 7 Models](https://fireworks.ai/blog/best-open-source-llms)
- [Open Source LLM Leaderboard 2026 — Compare Open-Weight Models](https://www.vellum.ai/open-llm-leaderboard)
- [Open LLM Leaderboard 2026 - Compare Open Source LLM Rankings](https://llm-stats.com/leaderboards/open-llm-leaderboard)
- [11 Top Open-Source LLMs for 2026 and Their Uses](https://www.datacamp.com/blog/top-open-source-llms)
- [LLM Leaderboard 2026 — Compare Top AI Models - Vellum](https://www.vellum.ai/llm-leaderboard)
- [LLM Benchmark Leaderboard 2026: Coding, Math, Reasoning and Agents](https://www.codesota.com/llm)
- [LLM Leaderboard 2026: Compare 300+ Top AI Models](https://llm-stats.com/)
- [Code Generation Benchmarks 2026: SOTA LLMs for Programming](https://www.codesota.com/code-generation)
- [Open Source LLM Leaderboard 2026 — Compare Open-Weight Models](https://www.vellum.ai/open-llm-leaderboard)
- [SOTA AI Models: Benchmarks, Metrics & Deployment Guide](https://huggingface.co/blog/daya-shankar/sota-ai-models)
- [Open LLM Leaderboard - Hugging Face Space](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Top Open-Source LLMs 2026: The Best Models & Comparison](https://kairntech.com/blog/articles/top-open-source-llm-models-in-2026/)
- [GitHub - Open Information Extraction Resources](https://github.com/gkiril/oie-resources)
- [GitHub - Low-resource Information Extraction Papers](https://github.com/zjunlp/Low-resource-KEPapers)
- [Benchmarking LLM-based Information Extraction Tools for Medical Documents](https://www.medrxiv.org/content/10.64898/2026.01.19.26344287v1.full)
- [Best Named Entity Recognition APIs for Entity Detection](https://www.assemblyai.com/blog/6-best-named-entity-recognition-apis-entity-detection)
- [10 Best Open-Source LLM Models (2025 Updated): Llama 4, Qwen 3 and DeepSeek R1](https://huggingface.co/blog/daya-shankar/open-source-llms)
- [Best Small AI Models to Run with Ollama (2026)](https://localaimaster.com/blog/small-language-models-guide-2026)
- [Top 5 Local LLM Tools and Models in 2026 - Pinggy](https://pinggy.io/blog/top_5_local_llm_tools_and_models/)
- [AI Updates Today (May 2026) – Latest AI Model Releases](https://llm-stats.com/llm-updates)
- [Local AI in 2026: The Best Models to Run on Your Own Hardware](https://www.aimagicx.com/blog/local-ai-models-2026-qwen-mistral-llama-hardware-guide)
- [Open LLM Leaderboard - Hugging Face](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)
- [Hugging Face Releases ml-intern: An Open-Source Agent That Automates Post-Training](https://rits.shanghai.nyu.edu/ai/hugging-face-releases-ml-intern-an-open-source-agent-that-automates-post-training/)
- [Hugging Face Releases ml-intern: Open-Source ML Research Agent](https://www.marktechpost.com/2026/04/21/hugging-face-releases-ml-intern-an-open-source-agent-that-automates-the-llm-post-training-workflow/)
- [HuggingFace ml-intern: Open-Source ML Research Agent](https://agentconn.com/blog/huggingface-ml-intern-open-source-ml-research-agent-2026/)
- [Self-Consistency Improves Chain of Thought Reasoning in Language Models (arXiv)](https://arxiv.org/abs/2203.11171)
- [Self-Consistency Paper on OpenReview](https://openreview.net/forum?id=1PL1NIMMrw)
- [Self-Consistency Paper PDF (ICLR)](https://iclr.cc/media/iclr-2023/Slides/11718.pdf)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b5e6350-4f47-4b42-8a29-f46ca903c825",
  "isSidechain": true,
  "agentId": "a9de7cafc51ea998f",
  "requestId": "req_011CatSgxTSdnnCzGaYFaaZ9",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "405d0d9a-2d14-4906-ad74-619effbe16df",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "3cb2b6ec-a481-4f45-829a-a7e6ba1de78e",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01LyNbCAqE3L8B6L92tAEQ7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4830,
      "cache_creation_input_tokens": 2155,
      "cache_read_input_tokens": 16797,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2155,
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
