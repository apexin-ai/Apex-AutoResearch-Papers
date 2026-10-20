# Research conversation: I'm conducting an adversarial review of a research proposal about training LLMs to be robust to semantic-preserving code

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-aca4c7bbcf815a9c8.jsonl`
- **Structured JSON:** [`8acbf3f8c0ef394c8963.json`](../../sessions/8a/8acbf3f8c0ef394c8963.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-10T06:25:59.325Z_

I'm conducting an adversarial review of a research proposal about training LLMs to be robust to semantic-preserving code mutations for fault localization (identifying which file/function has a bug). The proposal uses contrastive learning (InfoNCE loss) with mutation-augmented training data.

Please search for competitive and potentially overlooked work:

1. Search "site:arxiv.org contrastive learning code robustness fault localization 2025 2026"
2. Search "code LLM robustness mutation invariant training 2026 arxiv"
3. Search "semantic preserving code transformation robustness training 2026"
4. Search for ContraCode (EMNLP 2021) - "Contrastive Code Representation Learning" - verify it exists and targets general pre-training embeddings, not fault localization
5. Search "MACL-IRFL multi-view adaptive contrastive learning fault localization 2026" - verify this exists
6. Search "SWE-bench fault localization robustness 2026 arxiv"
7. Search "arXiv 2503.23448 semantic preserving transformations limitations" - does this paper exist and does it find 59% of transformations change semantics?
8. Search for any recent (2025-2026) papers on:
   - "program transformation augmentation LLM robustness"
   - "code mutation data augmentation fine-tuning robustness"
   - "fault localization contrastive learning"

Report what you find for each search, including paper titles, venues, and key findings.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "370c6656-7744-4485-a9ee-e151f381413d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-10T06:26:00.546Z_

I'll conduct these searches to identify competitive and potentially overlooked work in this area. Let me start with the arxiv searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "370c6656-7744-4485-a9ee-e151f381413d",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "f773ca08-57eb-483f-941c-adc53cf92f3f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 3 · 2026-05-10T06:26:00.789Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERadmRcPNMpb2vCn2LNCJh`</summary>

```json
{
  "query": "site:arxiv.org contrastive learning code robustness fault localization 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f773ca08-57eb-483f-941c-adc53cf92f3f",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "8b29ab8f-9be4-4cc2-9595-ea6a12691d56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 4 · 2026-05-10T06:26:00.799Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QXrCE18smd7ZTEz9q8SyEa`</summary>

```json
{
  "query": "code LLM robustness mutation invariant training 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b29ab8f-9be4-4cc2-9595-ea6a12691d56",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "04ab8cbc-f779-489b-b395-2f3308ce6265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 5 · 2026-05-10T06:26:00.997Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XkMXw6YML5A4vZ2GkgrnMV`</summary>

```json
{
  "query": "semantic preserving code transformation robustness training 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04ab8cbc-f779-489b-b395-2f3308ce6265",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "ac56b6a2-1d9a-4dcf-a008-3926a561a0d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 6 · 2026-05-10T06:26:01.228Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SrHyqe1m3HYBPN8ihWhnRt`</summary>

```json
{
  "query": "ContraCode contrastive code representation learning EMNLP 2021"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ac56b6a2-1d9a-4dcf-a008-3926a561a0d4",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "c7f6b05f-d594-48f6-a98c-442dc5b51dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 7 · 2026-05-10T06:26:01.406Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019QqRGUSNPtd8iUJjQdiUPu`</summary>

```json
{
  "query": "MACL-IRFL multi-view adaptive contrastive learning fault localization 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7f6b05f-d594-48f6-a98c-442dc5b51dc6",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "9f37c972-57c2-4252-a764-b0df89c02b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 786,
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

_source line 8 · 2026-05-10T06:26:01.520Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Erkcez6qTmUamcBKdwxbxw`</summary>

```json
{
  "query": "SWE-bench fault localization robustness 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f37c972-57c2-4252-a764-b0df89c02b33",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQqT4szz9biEzahjSz8",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "1ab67b02-50c1-4964-80aa-d890bace7050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XZwMC5anazLjbCUbjehJda",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 16155,
      "output_tokens": 355,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 786
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 355,
          "cache_read_input_tokens": 16155,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 786,
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

_source line 9 · 2026-05-10T06:26:05.996Z_

<details><summary>↩ Tool result · `toolu_01SrHyqe1m3HYBPN8ihWhnRt`</summary>

```text
Web search results for query: "ContraCode contrastive code representation learning EMNLP 2021"

Links: [{"title":"Contrastive Code Representation Learning - ACL Anthology","url":"https://aclanthology.org/2021.emnlp-main.482/"},{"title":"Contrastive Code Representation Learning","url":"https://aclanthology.org/2021.emnlp-main.482.pdf"},{"title":"[PDF] Contrastive Code Representation Learning | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Contrastive-Code-Representation-Learning-Jain-Jain/021bbcefc993c389bad6c1daefd8ff92d0fc2441"},{"title":"Contrastive Code Representation Learning - ADS","url":"https://ui.adsabs.harvard.edu/abs/2020arXiv200704973J/abstract"},{"title":"(PDF) Contrastive Code Representation Learning","url":"https://www.academia.edu/87692509/Contrastive_Code_Representation_Learning"},{"title":"GitHub - parasj/contracode: Contrastive Code Representation Learning: functionality-based JavaScript embeddings through self-supervised learning","url":"https://github.com/parasj/contracode"},{"title":"dblp: Contrastive Code Representation Learning.","url":"https://dblp.org/rec/conf/emnlp/0001JZA0S21.html"},{"title":"CONTRASTIVE CODE REPRESENTATION LEARNING","url":"https://openreview.net/pdf?id=uV7hcsjqM-"},{"title":"Contrastive Code Representation Learning | OpenReview","url":"https://openreview.net/forum?id=uV7hcsjqM-"},{"title":"[2007.04973] Contrastive Code Representation Learning","url":"https://arxiv.org/abs/2007.04973"}]

Based on the search results, here's what I found about ContraCode:

## Overview

ContraCode is a contrastive pre-training task that learns code functionality, not form. It was published in the Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP) by Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, and Ion Stoica.

## How It Works

ContraCode pre-trains a neural network to identify functionally similar variants of a program among many non-equivalent distractors. It scalably generates these variants using an automated source-to-source compiler as a form of data augmentation.

## Key Results

Contrastive pre-training outperforms RoBERTa on an adversarial code clone detection benchmark by 39% AUROC. ContraCode improves summarization and TypeScript type inference accuracy by 2 to 13 percentage points over competitive baselines.

## Training and Availability

ContraCode was pre-trained over 1.8m unannotated JavaScript methods mined from GitHub. All source code is available at https://github.com/parasj/contracode.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c7f6b05f-d594-48f6-a98c-442dc5b51dc6",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "1fdadace-07fa-4043-afb1-5c9a20bd3cef",
  "sourceToolAssistantUUID": "c7f6b05f-d594-48f6-a98c-442dc5b51dc6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-10T06:26:07.469Z_

<details><summary>↩ Tool result · `toolu_019QqRGUSNPtd8iUJjQdiUPu`</summary>

```text
Web search results for query: "MACL-IRFL multi-view adaptive contrastive learning fault localization 2026"

Links: [{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/html/2409.12519"},{"title":"[2409.12519] Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/abs/2409.12519"},{"title":"A unified Cross-Modal adaptive contrastive learning framework for acoustic fault diagnosis of rolling bearing under limited & imbalanced data - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0888327025014451"},{"title":"MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote ...","url":"http://121.43.168.64:10060/s/org/arxiv/G.https/pdf/2512.16294.pdf"},{"title":"[2512.16294] MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval","url":"https://arxiv.org/abs/2512.16294"},{"title":"MACL: Multi-Label Adaptive Contrastive Learning Loss for Remote Sensing Image Retrieval","url":"https://arxiv.org/html/2512.16294v1"},{"title":"MCLRL: A Multi-Domain Contrastive Learning with Reinforcement Learning Framework for Few-Shot Modulation Recognition","url":"https://arxiv.org/html/2502.19071v1"},{"title":"MCLRL: A Multi-Domain Contrastive Learning with ...","url":"https://www.alphaxiv.org/overview/2502.19071"},{"title":"MACL: A Masked Autoencoder Framework with Contrastive Learning for Efficient Encrypted Malicious Traffic Detection | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-981-96-9812-7_26"}]

Based on the web search results, I found relevant information about MACL-IRFL:

## MACL-IRFL: Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization

MACL-IRFL is a novel approach designed to learn relationships for software fault localization.

### Key Technical Details

Most information retrieval-based techniques for fault localization build representations for bug reports and source code files and match their semantic vectors through similarity measurement. However, such approaches often ignore useful information including: 1) the interaction relationship between bug reports and source code files; 2) the similarity relationship between bug reports; and 3) the co-citation relationship between source code files.

MACL-IRFL models bug reports, source code files, and the relationships between them as structured graphs from three views (report-code interaction view, report-report similarity view, and code-code co-citation view). These views provide auxiliary information that supplements the missing historical connections in the validation and test stages.

### Publication Status

The paper was published in Automated Software Engineering journal in 2026, and is also available on arXiv as a preprint.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f37c972-57c2-4252-a764-b0df89c02b33",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "07a812f6-d327-4acd-a959-8a30a89559e9",
  "sourceToolAssistantUUID": "9f37c972-57c2-4252-a764-b0df89c02b33",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T06:26:07.523Z_

<details><summary>↩ Tool result · `toolu_01XkMXw6YML5A4vZ2GkgrnMV`</summary>

```text
Web search results for query: "semantic preserving code transformation robustness training 2026"

Links: [{"title":"Auto-SPT: AUTOMATING SEMANTIC PRESERVING TRANS","url":"https://openreview.net/pdf/2e35bf66c0608f7bb43cf28acf8769a7c01b5fa1.pdf"},{"title":"Auto-SPT: Automating Semantic Preserving Transformations for Code","url":"https://arxiv.org/html/2512.06042v1"},{"title":"Semantic Robustness of Models of Source Code | IEEE Conference Publication | IEEE Xplore","url":"https://ieeexplore.ieee.org/document/9825895/"},{"title":"Auto-SPT: Automating Semantic Preserving Transformations for Code Ashish Hooda","url":"https://www.arxiv.org/pdf/2512.06042"},{"title":"Semantic Robustness of Models of Source Code","url":"https://pages.cs.wisc.edu/~jjhenkel/papers/semantic-robustness.pdf"},{"title":"How Do Semantically Equivalent Code Transformations Impact","url":"https://arxiv.org/pdf/2512.15468"},{"title":"Exploiting Code Symmetries for Learning Program Semantics","url":"https://s2lab.cs.ucl.ac.uk/downloads/icml24-SymC.pdf"},{"title":"Assessing and improving syntactic adversarial robustness ...","url":"https://chentaolue.github.io/pub-papers/ist25.pdf"},{"title":"Assessing and improving syntactic adversarial robustness of pre-trained models for code translation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0950584925000382"},{"title":"Auto-SPT: Automating Semantic Preserving Transformations for Code | OpenReview","url":"https://openreview.net/forum?id=oEJxn8QfC0"}]

Based on the search results, I found several relevant papers and projects from 2025-2026 on semantic preserving code transformation robustness training:

## Key Findings:

**Auto-SPT: Automating Semantic Preserving Transformations for Code**

Auto-SPT is a novel automated framework leveraging large language models to generate diverse and strong semantic-preserving transformations (SPTs), which addresses the limitations of existing heuristic-based and manually implemented SPTs by automating the design and implementation of transformations, thus significantly reducing manual effort and improving transformation strength and diversity.

The framework is designed to produce Semantic Preserving Transformations (SPTs) that alter a program's syntactic structure while preserving its functionality, using LLMs to craft a diverse set of SPTs, generate strong implementations for these SPTs, and compose them to result into strong transformations.

SPTs are code alterations that modify a program's syntactic or structural representation but maintain its original functionality, enabling several tasks in software engineering, including software testing, robustness evaluation, and data augmentation for training code-understanding models.

**Robustness Training Results**

Auto-SPT generates more diverse SPTs than existing approaches and these SPTs significantly drop the performance of state-of-the-art code clone detectors, with further experiments showing Auto-SPT can be used to enhance code datasets for training to produce code-clone detection models that are robust to real-world, adversarial code transformations.

**Code Translation Robustness (CoTR)**

CoTR consists of two components: CoTR-A and CoTR-D, where CoTR-A generates adversarial examples by transforming programs, while CoTR-D proposes a semantic distance-based sampling data augmentation method and adversarial training method to improve the model's robustness and generalization capabilities.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac56b6a2-1d9a-4dcf-a008-3926a561a0d4",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "11da6bdc-f95c-4db1-8e11-3d3dc939ff68",
  "sourceToolAssistantUUID": "ac56b6a2-1d9a-4dcf-a008-3926a561a0d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-10T06:26:07.983Z_

<details><summary>↩ Tool result · `toolu_01ERadmRcPNMpb2vCn2LNCJh`</summary>

```text
Web search results for query: "site:arxiv.org contrastive learning code robustness fault localization 2025 2026"

Links: [{"title":"ROBUSTNESS EVALUATION OF MACHINE LEARNING MODELS FOR FAULT CLASSIFICATION AND LOCALIZATION IN POWER SYSTEM PROTECTION","url":"https://arxiv.org/html/2512.15385"},{"title":"Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/html/2409.12519"},{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"ZAYAN: Disentangled Contrastive Transformer for Tabular Remote Sensing Data This paper has been accepted for presentation at the 28th International Conference on Pattern Recognition (ICPR 2026) in Lyon, France. Code: https://github.com/zadid6pretam/ZAYAN. PyPI: pip install zayan.","url":"https://arxiv.org/html/2604.27606"},{"title":"Unsupervised Soft Contrastive Learning for Fault Detection ...","url":"https://arxiv.org/abs/2405.16258"},{"title":"Domain-Aware Hierarchical Contrastive Learning for Semi-Supervised Generalization Fault Diagnosis","url":"https://arxiv.org/html/2604.20928"},{"title":"USD: Unsupervised Soft Contrastive Learning for Fault Detection in Multivariate Time Series","url":"https://arxiv.org/html/2405.16258v1"},{"title":"[2409.12519] Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization","url":"https://arxiv.org/abs/2409.12519"},{"title":"[2504.04372v3] Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/abs/2504.04372v3"},{"title":"[2504.14204] DConAD: A Differencing-based Contrastive Representation Learning Framework for Time Series Anomaly Detection","url":"https://arxiv.org/abs/2504.14204"}]

I've performed the web search with your query and found several relevant results from arXiv. Here's a summary of the most relevant papers:

## Key Findings:

**1. Multi-View Adaptive Contrastive Learning for Fault Localization (2025)**
MACL-IRFL is a novel approach designed to learn relationships for software fault localization. The approach uses an adaptive contrastive learning module to suppress noise in auxiliary information aggregation to derive more robust node representations. The results show improvements up to 28.93% on Accuracy@1, 25.57% MAP and 20.35% MRR.

**2. Code Robustness and Fault Localization of LLMs (2026)**
This paper presents the first large-scale empirical investigation into the robustness of LLMs' fault localizability, developing an end-to-end evaluation framework. The study found that semantic-preserving mutations cause LLMs to fail to localize the same fault it correctly localized earlier in 78% of cases.

**3. Contrastive Learning for Fault Detection (2025)**
DConAD generates differential data to provide additional information about time series and implements a KL divergence-based contrastive learning paradigm for enhanced robustness of representation learning.

These papers collectively address contrastive learning approaches for improving code robustness and fault localization across different domains in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b29ab8f-9be4-4cc2-9595-ea6a12691d56",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "f390e0c7-8743-471a-b759-10a435c05fe3",
  "sourceToolAssistantUUID": "8b29ab8f-9be4-4cc2-9595-ea6a12691d56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:26:09.222Z_

<details><summary>↩ Tool result · `toolu_01QXrCE18smd7ZTEz9q8SyEa`</summary>

```text
Web search results for query: "code LLM robustness mutation invariant training 2026 arxiv"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Detecting LLM-generated Code with Subtle Modification by Adversarial Training","url":"https://arxiv.org/pdf/2507.13123"},{"title":"Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting","url":"https://arxiv.org/html/2503.02296"},{"title":"Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics","url":"https://arxiv.org/html/2505.18658v2"},{"title":"Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372v3"},{"title":"[2603.15510] Not All Invariants Are Equal: Curating Training Data to Accelerate Program Verification with SLMs","url":"https://arxiv.org/abs/2603.15510"},{"title":"[2601.00509] Improving LLM-Assisted Secure Code Generation through Retrieval-Augmented-Generation and Multi-Tool Feedback","url":"https://arxiv.org/abs/2601.00509"},{"title":"Syntactic Robustness for LLM-based Code Generation This material is based on research supported by National Science Foundation, Award #2124039, National Science Foundation, Award #2008660, National Science Foundation, Award #1901098.","url":"https://arxiv.org/html/2404.01535v1"},{"title":"DeepTest Tool Competition 2026: Benchmarking an LLM-Based Automotive Assistant","url":"https://arxiv.org/html/2604.12615v1"},{"title":"Increasing LLM Coding Capabilities through Diverse Synthetic Coding Tasks","url":"https://arxiv.org/html/2510.23208v1"}]

Based on the search results, I found several relevant papers from 2026 on arXiv related to code, LLM robustness, mutations, and invariance:

## Key Findings:

**1. "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"** (ICST 2026)

The paper's key insight is that if an LLM can correctly reason about a program's semantics, it should identify deviations that change behavior (faults) and remain invariant to deviations that do not (semantic-preserving mutations). The researchers generate multiple semantic-preserving mutations (SPMs) including identifier renaming, comment insertion/modification, formatting changes, and dead-code insertion to test fault localization robustness.

The results show that semantic-preserving mutations cause LLMs to fail to localize the same fault in 78% of cases, suggesting that LLMs' code-reasoning is tied to code features irrelevant to semantics.

**2. "Detecting LLM-generated Code with Subtle Modification by Adversarial Training"**

This paper proposes CodeGPTSensor+, addressing limitations where LLM-generated code undergoes modifications that significantly degrade detection accuracy by proposing a detection framework fortified with enhanced robustness.

**3. "Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting"**

This work finds that mutation induces moderate drops in performance, paraphrase is nearly invariant, and rewrites are most disruptive—suggesting harmful memorization beyond surface-level robustness.

These papers investigate how LLMs maintain or lose robustness when code is modified through mutations and semantic-preserving transformations.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "04ab8cbc-f779-489b-b395-2f3308ce6265",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "dba2f784-77b5-432b-908d-88a574cf8101",
  "sourceToolAssistantUUID": "04ab8cbc-f779-489b-b395-2f3308ce6265",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-10T06:26:14.618Z_

<details><summary>↩ Tool result · `toolu_01Erkcez6qTmUamcBKdwxbxw`</summary>

```text
Web search results for query: "SWE-bench fault localization robustness 2026 arxiv"

Links: [{"title":"Accepted at the 2026 IEEE International Conference on Software Testing, Verification and Validation (ICST 2026) Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models","url":"https://arxiv.org/html/2504.04372"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and Architectures of LLM- and Agent-Based Repair Systems","url":"https://arxiv.org/html/2506.17208v2"},{"title":"Introducing SWE-bench Verified | OpenAI","url":"https://openai.com/index/introducing-swe-bench-verified/"},{"title":"Published as a conference paper at ICLR 2024 SWE-BENCH:","url":"https://arxiv.org/pdf/2310.06770"},{"title":"Dissecting the SWE-Bench Leaderboards: Profiling Submitters and","url":"https://arxiv.org/pdf/2506.17208"},{"title":"GitHub - SWE-bench/SWE-bench: SWE-bench: Can Language Models Resolve Real-world Github Issues? · GitHub","url":"https://github.com/swe-bench/SWE-bench"},{"title":"Are “Solved Issues” in SWE-bench Really Solved Correctly? An Empirical Study","url":"https://arxiv.org/html/2503.15223v2"},{"title":"[2310.06770] SWE-bench: Can Language Models Resolve Real-World GitHub Issues?","url":"https://arxiv.org/abs/2310.06770"},{"title":"SWE-bench Goes Live!","url":"https://arxiv.org/html/2505.23419v2"},{"title":"What’s in a Benchmark? The Case of SWE-Bench in Automated Program Repair","url":"https://arxiv.org/pdf/2602.04449"}]

Based on the search results, I found several relevant papers on arXiv related to SWE-bench, fault localization, and robustness from 2026:

## Key Findings:

**1. Fault Localization Robustness Study (ICST 2026)**

The first large-scale empirical investigation into the robustness of LLMs' fault localizability was presented, developing an end-to-end evaluation framework that addresses limitations in current LLM evaluation including data contamination, scalability, automation, and extensibility. The study involved automatically injecting semantic-preserving mutations with varying strengths, types, and locations to create unique fault localization programs, then recording LLM responses to capture fault localization accuracy and identify LLM robustness in the presence of non-functional code changes.

**2. SWE-Bench Leaderboards Analysis**

A comprehensive study of all submissions to the SWE-Bench Lite (79 entries) and Verified (99 entries) leaderboards analyzed 80 unique approaches across dimensions such as submitter type, product availability, LLM usage, and system architecture. CodeFuse-AAIS proposes improvements including adaptive fault localization and expansion of the sampling space by combining multiple LLMs.

**3. Patch Correctness on SWE-bench**

An in-depth empirical study of the correctness of plausible generated patches on SWE-bench was presented as a call to arms for more robust and reliable evaluation of issue-solving tools.

These papers address the robustness challenges in fault localization and SWE-bench evaluation within the 2026 timeframe.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1ab67b02-50c1-4964-80aa-d890bace7050",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "0d124cc9-6621-482c-8f5c-7ad85e8f4bbf",
  "sourceToolAssistantUUID": "1ab67b02-50c1-4964-80aa-d890bace7050",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T06:26:15.629Z_

Let me continue with the remaining searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d124cc9-6621-482c-8f5c-7ad85e8f4bbf",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQraPSYHYKE1vuHune3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "cbf72313-8d8f-4368-8702-0a905185118a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DPHvHXgmTcQrU9sfeaoio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6612,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6612,
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

_source line 16 · 2026-05-10T06:26:16.128Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UDSeBWov3LZyFY6Kj28g9v`</summary>

```json
{
  "query": "arXiv 2503.23448 semantic preserving transformations"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cbf72313-8d8f-4368-8702-0a905185118a",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQraPSYHYKE1vuHune3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "810bbb2d-fa4b-4e31-aa33-3314800d5ac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DPHvHXgmTcQrU9sfeaoio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6612,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6612,
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

_source line 17 · 2026-05-10T06:26:16.721Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PLKiZb2DRT1PHqwCSYi4DL`</summary>

```json
{
  "query": "program transformation augmentation LLM robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "810bbb2d-fa4b-4e31-aa33-3314800d5ac7",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQraPSYHYKE1vuHune3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "70ce43d0-46cd-40e4-91d8-afdf1d64a917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DPHvHXgmTcQrU9sfeaoio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6612,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6612,
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

_source line 18 · 2026-05-10T06:26:16.979Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RhqCXN7qBvt2kUCxCceLvA`</summary>

```json
{
  "query": "code mutation data augmentation fine-tuning robustness 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "70ce43d0-46cd-40e4-91d8-afdf1d64a917",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQraPSYHYKE1vuHune3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "84801779-7040-41b8-aba7-48bf0d571a0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DPHvHXgmTcQrU9sfeaoio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6612,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6612,
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

_source line 19 · 2026-05-10T06:26:17.067Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MBbeUXyAEjjRthhhBgzEyN`</summary>

```json
{
  "query": "fault localization contrastive learning neural networks 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84801779-7040-41b8-aba7-48bf0d571a0d",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQraPSYHYKE1vuHune3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "d5334ed0-f495-4c09-a5bc-8cf481c8e99a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_019DPHvHXgmTcQrU9sfeaoio",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 6612,
      "cache_read_input_tokens": 16941,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6612,
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

_source line 20 · 2026-05-10T06:26:23.339Z_

<details><summary>↩ Tool result · `toolu_01UDSeBWov3LZyFY6Kj28g9v`</summary>

```text
Web search results for query: "arXiv 2503.23448 semantic preserving transformations"

Links: [{"title":"[2503.23448] Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/abs/2503.23448"},{"title":"Semantic-Preserving Transformations as Mutation Operators","url":"https://arxiv.org/pdf/2503.23448"},{"title":"Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://arxiv.org/html/2503.23448"},{"title":"(PDF) Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection","url":"https://www.researchgate.net/publication/390353442_Semantic-Preserving_Transformations_as_Mutation_Operators_A_Study_on_Their_Effectiveness_in_Defect_Detection"},{"title":"Semantically-Preserving Transformations","url":"https://www.emergentmind.com/topics/semantically-preserving-transformations"},{"title":"Linguistic Loops and Geometric Invariants as a Way to Pre-Verbal Thought?","url":"https://arxiv.org/html/2503.23311"},{"title":"The semantic preserving transformations, that we used in our experiments. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/The-semantic-preserving-transformations-that-we-used-in-our-experiments_tbl1_371988814"},{"title":"Type-changing rewriting and semantics-preserving transformation - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S0167642315001434"},{"title":"[2503.23301] Holonomy preserving transformations of weighted graphs and its application to knot theory","url":"https://arxiv.org/abs/2503.23301"},{"title":"Parameter-Efficient Architectural Modifications for Translation-Invariant CNNs","url":"https://arxiv.org/html/2604.27870"}]

Based on the search results, here's information about arXiv paper 2503.23448:

## Paper Overview

The study aims to determine whether semantic-preserving transformations can be used, analogous to mutation operators, to improve the performance of defect detection tools in the testing stage.

## Key Findings

The researchers found 28 publications with 94 different transformations, and implemented 39 transformations from four of the publications, but a manual check revealed that 23 out of 39 transformations change code semantics. Using the 16 remaining correct transformations and three ensemble strategies, they were not able to increase the accuracy of the defect detection models.

## Background

Recent advances in defect detection use language models, with existing works enhancing training data to improve the models' robustness when applied to semantically identical code. However, the use of semantically identical code has not been considered for improving the tools during their application—a concept closely related to metamorphic testing.

## Authors and Publication Date

The paper was authored by Max Hort, Linas Vidziunas, and Leon Moonen, and was published on March 30, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "810bbb2d-fa4b-4e31-aa33-3314800d5ac7",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "9a601698-1754-45ed-a022-c88426e69485",
  "sourceToolAssistantUUID": "810bbb2d-fa4b-4e31-aa33-3314800d5ac7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-10T06:26:24.387Z_

<details><summary>↩ Tool result · `toolu_01RhqCXN7qBvt2kUCxCceLvA`</summary>

```text
Web search results for query: "code mutation data augmentation fine-tuning robustness 2025 2026"

Links: [{"title":"Enhancing robustness of AI offensive code generators via data augmentation | Empirical Software Engineering","url":"https://link.springer.com/article/10.1007/s10664-024-10569-y"},{"title":"New framework pinpoints conditions that make data augmentation improve robustness","url":"https://techxplore.com/news/2026-01-framework-conditions-augmentation-robustness.html"},{"title":"[2306.05079] Enhancing Robustness of AI Offensive Code Generators via Data Augmentation","url":"https://arxiv.org/abs/2306.05079"},{"title":"Empirical Software Engineering manuscript No. (will be inserted by the editor)","url":"https://arxiv.org/pdf/2306.05079"},{"title":"Fine-tuned representation models boost LLM systems. Here's how | Snorkel AI","url":"https://snorkel.ai/blog/fine-tuning-representation-models-boost-llm-systems-here-s-how/"},{"title":"LLMxCPG: Context-Aware Vulnerability Detection Through ...","url":"https://www.usenix.org/system/files/usenixsecurity25-lekssays.pdf"},{"title":"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats","url":"https://arxiv.org/html/2410.22293v1"},{"title":"Data Augmentation: 2026 Techniques That Work in Real-World Models | Label Your Data","url":"https://labelyourdata.com/articles/data-augmentation"},{"title":"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning","url":"https://arxiv.org/html/2511.01490v1"},{"title":"Data Augmentation Methods for Enhancing Robustness in Text Classification Tasks","url":"https://www.mdpi.com/1999-4893/16/1/59"}]

I've completed the web search for "code mutation data augmentation fine-tuning robustness 2025 2026". Here are the relevant findings:

## Key Research Areas

**Code Mutation and Robustness:**
Data augmentation increases the variability and diversity of natural language descriptions in training data, proving its effectiveness against both perturbed and non-perturbed code descriptions. One approach involves adding perturbations to code descriptions to create new natural language inputs that differ from the original, and analyzing how and to what extent these perturbations affect AI code generator performance.

**Mathematical Framework for Data Augmentation (2026):**
A mathematical framework has been developed that explains exactly when and how data augmentation improves a model's resilience against unexpected changes in data distribution, paving the way for more systematic and effective design of augmentation strategies. This study was accepted as an official paper at the 40th Annual AAAI Conference on Artificial Intelligence (AAAI-26), held in Singapore from January 20-27, 2026.

**Fine-Tuning with Synthetic Data (2025-2026):**
Synthetic fine-tuning data leads to decreases in LLMs' adversarial robustness while preserving output quality, while human training data tends to decrease both, and the diversity of synthetic data sources and the size of data-generating models jointly affect the adversarial robustness of fine-tuned models.

**Code Mutation for LLMs:**
Code mutation has traditionally been employed to increase software robustness in mission-critical applications, and mutation engines have been exploited by malware developers to evade signature-based detection methods.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "84801779-7040-41b8-aba7-48bf0d571a0d",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "2f9b939b-c5c2-42d1-a39c-8240d4e5cd24",
  "sourceToolAssistantUUID": "84801779-7040-41b8-aba7-48bf0d571a0d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-10T06:26:25.200Z_

<details><summary>↩ Tool result · `toolu_01PLKiZb2DRT1PHqwCSYi4DL`</summary>

```text
Web search results for query: "program transformation augmentation LLM robustness 2025 2026"

Links: [{"title":"IEEE SaTML 2026 · Program","url":"https://satml.org/program/"},{"title":"GitHub - iSEngLab/AwesomeLLM4SE: [SCIS 2025] A Survey on Large Language Models for Software Engineering · GitHub","url":"https://github.com/iSEngLab/AwesomeLLM4SE"},{"title":"A data-augmented model routing framework for efficient LLM deployment in edge–cloud environments | The Journal of Supercomputing | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11227-025-08034-8"},{"title":"The State Of LLMs 2025: Progress, Progress, and Predictions","url":"https://magazine.sebastianraschka.com/p/state-of-llms-2025"},{"title":"Advancing adversarial and LLM robustness in trustworthy AI: a comprehensive survey | Artificial Intelligence Review | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10462-026-11558-x"},{"title":"LLM Research Papers: The 2025 List (July to December)","url":"https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2"},{"title":"(PDF) Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics","url":"https://www.researchgate.net/publication/392104377_Robustness_in_Large_Language_Models_A_Survey_of_Mitigation_Strategies_and_Evaluation_Metrics"},{"title":"The Silent Evolution of LLMs in 2026 - DEV Community","url":"https://dev.to/synergy_shock/the-silent-evolution-of-llms-in-2026-2mc4"},{"title":"LLM Benchmarks 2026 - Compare AI Benchmarks and Tests","url":"https://llm-stats.com/benchmarks"},{"title":"A Comprehensive Survey on LLM‐Based Network Management and Operations - Hong - 2025 - International Journal of Network Management - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/full/10.1002/nem.70029"}]

Based on the web search results, here are some key findings about program transformation, augmentation, LLM robustness in 2025-2026:

## Data Augmentation for Program Generation

A data-augmented routing method for program generation tasks leverages heterogeneous LLM engines, introducing a mask-based data augmentation strategy that enriches the prompt dataset with varying difficulty levels, improving the router's generalization capability and robustness to unseen inputs.

## LLM Robustness and Augmentation Techniques

Recent approaches like the Adversarial Augmentation Approach (A3) combine adversarial training with NLP-specific data augmentation, employing a paraphrasing model guided by a separate generator to produce reusable adversarial examples, optimized for specific tasks via a discriminator. Additionally, SALAD (Structure Aware and LLM-driven Augmented Data) is a contrastive learning approach that employs a tagging-based method for generating structure-aware positive samples and leverages LLMs to create diverse counterfactual negative samples for triplet loss optimization.

## Program Repair with LLMs

ReAPR (automatic program repair via retrieval-augmented large language models) was published in 2025. This represents recent work applying augmented LLMs to program transformation tasks.

## RAG and Robustness

Retrieval-augmented generation (RAG) is susceptible to retrieval corruption attacks, where malicious passages injected into retrieval results can lead to inaccurate model responses, and RobustRAG is proposed as the first defense framework with certifiable robustness against retrieval corruption attacks.

These developments reflect growing focus on making LLMs more robust through data augmentation and transformation techniques specifically tailored for program synthesis and analysis tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "70ce43d0-46cd-40e4-91d8-afdf1d64a917",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "b30d2e6a-cee5-4256-a793-e67e33e5ca1b",
  "sourceToolAssistantUUID": "70ce43d0-46cd-40e4-91d8-afdf1d64a917",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-10T06:26:25.843Z_

<details><summary>↩ Tool result · `toolu_01MBbeUXyAEjjRthhhBgzEyN`</summary>

```text
Web search results for query: "fault localization contrastive learning neural networks 2025 2026"

Links: [{"title":"Multi-view adaptive contrastive learning for information retrieval based fault localization | Automated Software Engineering | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10515-025-00573-x"},{"title":"Multi-Dimensional Anomaly Detection and Fault Localization in Microservice Architectures: A Dual-Channel Deep Learning Approach with Causal Inference for Intelligent Sensing","url":"https://www.mdpi.com/1424-8220/25/11/3396"},{"title":"SupConFL: Fault Localization with Supervised Contrastive Learning | Request PDF","url":"https://www.researchgate.net/publication/374494097_SupConFL_Fault_Localization_with_Supervised_Contrastive_Learning"},{"title":"A Comprehensive Review of Deep Transfer Learning for Intelligent Fault Diagnosis in Rotating Machines - Feisa - 2025 - Engineering Reports - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1002/eng2.70494"},{"title":"Contrastive Learning for Fault Detection and Diagnostics in the Context of Changing Operating Conditions and Novel Fault Types - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/34065164/"},{"title":"Improving Graph Learning-Based Fault Localization with Tailored Semi-supervised Learning | Proceedings of the ACM on Software Engineering","url":"https://dl.acm.org/doi/10.1145/3715788"},{"title":"Deep learning based approaches for intelligent industrial machinery health management and fault diagnosis in resource-constrained environments | Scientific Reports","url":"https://www.nature.com/articles/s41598-024-79151-2"},{"title":"A self-attention based contrastive learning method for bearing fault diagnosis - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0957417423021474"},{"title":"Online Fault Detection, Classification and Localization in PV Arrays Using Feedforward Neural Networks and Residual-Based Modeling","url":"https://www.mdpi.com/2227-7080/14/2/130"},{"title":"Contrastive Learning for Fault Detection and Diagnostics in the Context of Changing Operating Conditions and Novel Fault Types - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC8161334/"}]

I've completed the web search for "fault localization contrastive learning neural networks 2025 2026". Here are the key findings:

## Recent Research on Fault Localization with Contrastive Learning

**Software Fault Localization:**

A 2025 paper published in Automated Software Engineering proposes "Multi-view adaptive contrastive learning for information retrieval based fault localization" and was published on November 6, 2025. The approach, named MACL-IRFL, learns relationships between bug reports and source code files through graph neural networks.

Another 2025 publication on "Enhancing Fault Localization in Industrial Software Systems via Contrastive Learning" appeared in the 2025 IEEE/ACM 47th International Conference on Software Engineering (ICSE).

**Microservice Architectures:**

A May 2025 paper proposes using contrastive learning to create unified representations of diverse service metrics and incorporates causal inference mechanisms to trace fault propagation paths in microservice systems.

**Industrial Machinery:**

Recent research proposed a semi-supervised contrastive domain adaptation network for rotating machinery fault diagnosis, integrating in-domain contrastive learning and local MMD to enhance feature adaptation.

**General Applications:**

Contrastive learning combined with noise disturbance has been used as an auxiliary task to extract global and local features of vibrational data and encourage feature separability between different classes of samples.

The search results show significant recent activity (2025-2026) in applying contrastive learning techniques to various fault localization and diagnosis tasks, particularly in software engineering, microservices, and industrial machinery domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d5334ed0-f495-4c09-a5bc-8cf481c8e99a",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "0bdbfb7b-8caf-4b6e-bf92-c3c61839846a",
  "sourceToolAssistantUUID": "d5334ed0-f495-4c09-a5bc-8cf481c8e99a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-10T06:26:27.553Z_

Now let me fetch the actual paper (2503.23448) to verify the specific claim about 59% of transformations changing semantics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0bdbfb7b-8caf-4b6e-bf92-c3c61839846a",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQsQQTD6r8edwap4si3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "5e262a4d-8178-4efe-b3ff-5ebbb5efbc93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XxFS8yA2Df1BTrkVJjtbx7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4161,
      "cache_read_input_tokens": 23553,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4161,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    }
  }
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-10T06:26:28.099Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01NaSJgmaemBSVH2EcSYhApS`</summary>

```json
{
  "url": "https://arxiv.org/abs/2503.23448",
  "prompt": "What percentage or fraction of semantic-preserving transformations were found to actually change semantics?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e262a4d-8178-4efe-b3ff-5ebbb5efbc93",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQsQQTD6r8edwap4si3",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "2e570309-8ef1-4a61-9c2a-1649f7b4cc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01XxFS8yA2Df1BTrkVJjtbx7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 4161,
      "cache_read_input_tokens": 23553,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4161
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 132,
          "cache_read_input_tokens": 23553,
          "cache_creation_input_tokens": 4161,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4161,
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

_source line 26 · 2026-05-10T06:26:30.693Z_

<details><summary>↩ Tool result · `toolu_01NaSJgmaemBSVH2EcSYhApS`</summary>

```text
# Semantic-Preserving Transformations Analysis

According to the research findings, **59% of the implemented transformations actually changed semantics** despite being labeled as semantic-preserving.

The study details this in their abstract: "a manual check revealed that 23 out 39 transformations change code semantics." This means only 16 of the 39 transformations they attempted to implement were truly semantic-preserving (41%).

This finding highlights a significant challenge the researchers identified: "reusing shared semantic-preserving transformation is difficult, sometimes even causing wrongful changes to the semantics."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e570309-8ef1-4a61-9c2a-1649f7b4cc83",
  "isSidechain": true,
  "promptId": "8a09dbd9-e583-41b3-80a8-91bab2c64b9d",
  "agentId": "aca4c7bbcf815a9c8",
  "type": "user",
  "uuid": "140cdc66-70f8-4f86-b31a-ac0eb4d222a1",
  "sourceToolAssistantUUID": "2e570309-8ef1-4a61-9c2a-1649f7b4cc83",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-10T06:26:55.399Z_

Perfect! Now let me compile the comprehensive report of all findings.

## Comprehensive Competitive Work Analysis Report

I've completed an extensive search for competitive and potentially overlooked work on LLM robustness to semantic-preserving code mutations for fault localization. Here are the key findings:

---

### **1. Direct Competition on Fault Localization Robustness (2026)**

**Primary Competitive Work: "Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models"**
- **Venue:** ICST 2026 (IEEE International Conference on Software Testing, Verification and Validation)
- **ArXiv ID:** [2504.04372](https://arxiv.org/abs/2504.04372)
- **Key Finding:** 78% failure rate - When semantic-preserving mutations are applied, LLMs fail to localize the same fault they correctly identified previously in 78% of cases
- **Approach:** Tests LLM fault localization robustness using multiple semantic-preserving mutation types (identifier renaming, comment insertion/modification, formatting changes, dead-code insertion)
- **Critical Issue:** This directly addresses the core problem your proposal targets and reports empirically that LLMs' fault reasoning is tied to syntactically-irrelevant features

---

### **2. Multi-View Adaptive Contrastive Learning Approach (MACL-IRFL, 2025)**

**Paper:** "Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization"
- **Venue:** Automated Software Engineering journal (published November 6, 2025), also [arXiv 2409.12519](https://arxiv.org/abs/2409.12519)
- **Publisher:** Springer Nature
- **Key Innovation:** Uses graph neural networks modeling three views:
  - Report-code interaction relationships
  - Report-report similarity relationships  
  - Code-code co-citation relationships
- **Results:** Up to 28.93% improvement on Accuracy@1, 25.57% MAP, 20.35% MRR
- **Approach Similarity:** Uses contrastive learning for fault localization but focuses on multi-view graph modeling rather than mutation-based augmentation

---

### **3. Semantic-Preserving Transformation Limitations (Critical, March 2025)**

**Paper:** "Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection"
- **ArXiv ID:** [2503.23448](https://arxiv.org/abs/2503.23448)
- **Authors:** Max Hort, Linas Vidziunas, Leon Moonen
- **Publication Date:** March 30, 2025
- **CRITICAL FINDING:** **59% of implemented transformations actually change semantics** (23 of 39 transformations changed semantics; only 16 of 39 were truly semantic-preserving)
- **Implication:** This directly undermines the foundation of mutation-based augmentation approaches - the authors found they could not improve defect detection models even with supposedly semantic-preserving transformations
- **Conclusion:** "reusing shared semantic-preserving transformation is difficult, sometimes even causing wrongful changes to the semantics"

---

### **4. ContraCode (EMNLP 2021) - Foundational Pre-training Work**

**Paper:** "Contrastive Code Representation Learning"
- **Venue:** EMNLP 2021
- **Authors:** Paras Jain, Ajay Jain, Tianjun Zhang, Pieter Abbeel, Joseph Gonzalez, Ion Stoica
- **ArXiv ID:** [2007.04973](https://arxiv.org/abs/2007.04973)
- **GitHub:** [github.com/parasj/contracode](https://github.com/parasj/contracode)
- **Key Focus:** General pre-training embeddings using contrastive learning, NOT fault localization
- **Approach:** Pre-trains on 1.8m JavaScript methods from GitHub using source-to-source compiler transformations to generate functionally similar variants
- **Results:** 39% AUROC improvement on adversarial code clone detection; 2-13 point improvements on summarization and type inference
- **Relevance:** Demonstrates that contrastive pre-training on mutation variants improves robustness, but targets general code understanding, not fault localization specifically

---

### **5. Automated Semantic-Preserving Transformations (Auto-SPT, December 2024)**

**Paper:** "Auto-SPT: Automating Semantic Preserving Transformations for Code"
- **ArXiv ID:** [2512.06042](https://arxiv.org/abs/2512.06042)
- **Venue:** OpenReview (appears to be under review/accepted)
- **Key Innovation:** Uses LLMs to automatically generate diverse and strong semantic-preserving transformations, addressing the problem that heuristic-based transformations are limited
- **Results:** Successfully generates more diverse SPTs than existing heuristic approaches; significantly drops performance of code clone detectors when applied
- **Practical Finding:** Successfully uses Auto-SPT to augment training data and improve robustness of code clone detection models
- **Relevance:** Provides a potentially more reliable way to generate mutation-augmented training data than manual/heuristic approaches

---

### **6. Code Mutation-Based Robustness Studies (2025-2026)**

**"Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting"**
- **ArXiv ID:** [2503.02296](https://arxiv.org/abs/2503.02296)
- **Finding:** Mutation causes moderate performance drops; paraphrase is nearly invariant; rewrites are most disruptive - suggests harmful memorization beyond surface-level robustness

**"Fine-Tuning LLMs for Code Mutation: A New Era of Cyber Threats"**
- **ArXiv ID:** [2410.22293](https://arxiv.org/abs/2410.22293)
- **Finding:** Explores how fine-tuning LLMs on mutated code creates cybersecurity risks

---

### **7. Data Augmentation Framework Results (AAAI-26, January 2026)**

**"When Does Data Augmentation Improve Robustness?"** (accepted AAAI-26)
- **Key Finding:** Mathematical framework shows data augmentation increases variability and diversity in training data, but the relationship between diversity and robustness is complex and context-dependent
- **Implication:** Simply augmenting with more mutations doesn't guarantee robustness improvements

---

### **8. Synthetic Data and Fine-tuning Robustness Trade-offs (2025)**

**"Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning"**
- **ArXiv ID:** [2511.01490](https://arxiv.org/abs/2511.01490)
- **Critical Finding:** Synthetic fine-tuning data (including augmented variants) can **decrease adversarial robustness** while preserving output quality
- **Implication:** Your contrastive learning approach using augmented data must carefully balance robustness gains against potential degradation in other robustness dimensions

---

### **9. Robustness in LLMs - General Survey (2025)**

**"Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics"**
- **ArXiv ID:** [2505.18658](https://arxiv.org/abs/2505.18658)
- **Published:** 2025
- **Scope:** Comprehensive survey of robustness techniques; provides context for where mutation-based augmentation fits in the broader landscape

---

## Key Overlaps and Gaps Identified

### Direct Competition:
1. **ICST 2026 paper (2504.04372)** - Likely the most direct competitor, also studies fault localization robustness to semantic-preserving mutations
2. **MACL-IRFL** - Different approach (multi-view graphs) but same fault localization problem domain

### Critical Vulnerabilities in Your Approach:
1. **arXiv 2503.23448** - Demonstrates that 59% of "semantic-preserving" transformations actually change semantics, undermining the foundation of mutation-augmented training
2. **arXiv 2511.01490** - Shows synthetic augmented data can degrade adversarial robustness in fine-tuning
3. **The 78% failure rate (ICST 2026)** - Shows the scale of the problem is severe; contrastive learning with current mutation approaches may not solve this

### Potentially Overlooked Opportunities:
1. **Auto-SPT** - Could improve your mutation generation quality by using LLM-based transformation generation rather than heuristic/manual approaches
2. **ContraCode pre-training** - Your work could build on ContraCode's general pre-training approach but adapt it specifically for fault localization
3. **Multi-view contrastive approaches** - MACL-IRFL suggests that modeling multiple relationship types (not just code-fault pairs) could improve results

---

## Summary Assessment

Your proposal directly addresses a critical gap identified in ICST 2026 (the 78% robustness failure), and uses a promising technique (contrastive learning with InfoNCE loss). However, you face substantial competitive and methodological challenges:

- **Direct competitor:** ICST 2026 paper already quantifies the problem you're solving
- **Methodological risk:** arXiv 2503.23448 shows 59% of supposedly semantic-preserving transformations actually change semantics—this is a fundamental threat to mutation-based augmentation approaches
- **Data augmentation risk:** Recent work shows synthetic augmentation can paradoxically reduce robustness
- **Potential mitigation:** Adopt LLM-based transformation generation (Auto-SPT) and consider multi-view contrastive approaches (MACL-IRFL model)

Sources:
- [Assessing the Impact of Code Changes on the Fault Localizability of Large Language Models (ICST 2026)](https://arxiv.org/abs/2504.04372)
- [Multi-View Adaptive Contrastive Learning for Information Retrieval Based Fault Localization](https://arxiv.org/abs/2409.12519)
- [Semantic-Preserving Transformations as Mutation Operators: A Study on Their Effectiveness in Defect Detection](https://arxiv.org/abs/2503.23448)
- [Contrastive Code Representation Learning (ContraCode)](https://arxiv.org/abs/2007.04973)
- [Auto-SPT: Automating Semantic Preserving Transformations for Code](https://arxiv.org/abs/2512.06042)
- [Memorize or Generalize? Evaluating LLM Code Generation with Code Rewriting](https://arxiv.org/abs/2503.02296)
- [Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning](https://arxiv.org/abs/2511.01490)
- [Robustness in Large Language Models: A Survey of Mitigation Strategies and Evaluation Metrics](https://arxiv.org/abs/2505.18658)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "140cdc66-70f8-4f86-b31a-ac0eb4d222a1",
  "isSidechain": true,
  "agentId": "aca4c7bbcf815a9c8",
  "requestId": "req_011CatQsm7tTTrGH5qYGZ8dG",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "a9dc4387-825d-4f4b-93f9-ebddf62a0db5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "818c6f04-ca23-4de4-b570-59c5989a81dd",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01CuiHytx9Myfrv3r8WK7aL2",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 273,
      "cache_read_input_tokens": 27714,
      "output_tokens": 2696,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 273
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2696,
          "cache_read_input_tokens": 27714,
          "cache_creation_input_tokens": 273,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 273,
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
